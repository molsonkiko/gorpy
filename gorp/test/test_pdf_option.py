from gorp.readfiles import GorpSession, gorpdir
import itertools
import os
import unittest

try:
    import gorp.pdf_utils  # just importing to get any ImportErrors out of the way
except ImportError as ex:
    warn_first_import_error("pdfminer")
    raise ex
# tested on Python 3.6 - 3.10


ogdir = os.getcwd()


class PDFOptionTester(unittest.TestCase):
    def setUp(self):
        os.chdir(gorpdir)

    def tearDown(self):
        os.chdir(ogdir)

    def test_with_c_i_n_options(self):
        base_query = "-r -a 'pdf$' /testDir -}} "
        regex_dirname = " -i -pdf 'WORLD|html'"
        opt_combos = [("-c", "-n"), ("-n",), ("-c",)]
        bad_combos = {}
        query_results = {}
        with GorpSession(print_output=False) as session:
            for combo in opt_combos:
                with self.subTest(combo=combo):
                    Combo = " ".join(combo)
                    comboset = frozenset(combo)
                    query = base_query + Combo + regex_dirname
                    session.receive_query(query)
                    query_results[comboset] = session.resultset
                    self.assertTrue(
                        query_results[comboset],
                        f"Resultset for query {query} should not be empty, but it is.",
                    )


if __name__ == "__main__":
    unittest.main()
