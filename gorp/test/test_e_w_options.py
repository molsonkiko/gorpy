from gorp.readfiles import *
from gorp.test.test_ku_options import setup_tempdir
import unittest

og_dir = os.getcwd()
newdirname = os.path.join(gorpdir, "test", "temp")


class E_WOptionTester(unittest.TestCase):
    def setUp(self):
        setup_tempdir()
        self.session = GorpSession(print_output=False)
        os.chdir(newdirname)

    def tearDown(self):
        os.chdir(og_dir)
        self.session.close()

    def test_e_w_options(self):
        ################
        ## W TEST 1: TEST W OPTION IN SIMPLE CASE;
        ## WRITING TO CURRENT DIRECTORY
        ################
        og_listdir = set(os.listdir()) | set(
            os.path.join("subdir", x) for x in os.listdir("subdir")
        )
        query = "-a -i -r 'dict|dance' /. -}} -w 'dance_dict.json'"
        self.session.receive_query(query)
        new_listdir = set(os.listdir()) | set(
            os.path.join("subdir", x) for x in os.listdir("subdir")
        )
        files_to_add = {"dance_dict.json"}
        self.assertEqual(new_listdir - og_listdir, files_to_add, query)
        with open("dance_dict.json") as f:
            dancedict = json.load(f)
        correct_dancedict = {
            os.path.join(newdirname, "The Rolling Stones [ Dance Part 2.py"): 0,
            os.path.join(newdirname, "subdir", "dict size vs memory allocated.png"): 0,
        }
        self.assertEqual(dancedict, correct_dancedict, query)
        ################
        ## E TEST 1: TEST E OPTION IN SIMPLE CASE;
        ## READING FROM CURRENT DIRECTORY
        ## Note that this has to be part of the same test because this
        ## query is going to read the file that was produced by the -w
        ## option query, so everything has to stay as it was after last query.
        ################
        og_listdir = set(os.listdir()) | set(
            os.path.join("subdir", x) for x in os.listdir("subdir")
        )
        query = "-e -a '' /dance_dict.json -}} -a 'png'"
        self.session.receive_query(query)
        new_listdir = set(os.listdir()) | set(
            os.path.join("subdir", x) for x in os.listdir("subdir")
        )
        self.assertEqual(new_listdir, og_listdir, query)
        correct_resultset = [
            os.path.join(newdirname, "subdir", "dict size vs memory allocated.png")
        ]
        self.assertEqual(self.session.resultset, correct_resultset, query)


if __name__ == "__main__":
    unittest.main()
