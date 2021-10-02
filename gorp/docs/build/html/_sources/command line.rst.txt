==========
command line
==========

gorpy is most conveniently used from the command line. You can run the package
directly like so::
    C:/Users/mjols/Python39> python -m gorp help
    Welcome to the gorp prompt.
    - The general query format is
        <options> '<pattern>' /<directory or filename>,
        followed by any number of
        <options> '<pattern>' subqueries separated by "-}}" delimiters.
    - You can exit at any time by entering 'e','q','quit', or 'exit'.
    - Enter "options" or 'o' for a list of gorp's optional arguments.
    - You can display the working directory with 'd' or 'dir', change the working
        directory with 'cd <new directory name>', and display the contents of the
        working directory with 'ls'.
    - You can write the results of a query to a JSON or YAML file by terminating
        the query with " -}} -w '<name of file to write to>'.
    - You can also supply a numeric argument to limit the size of the resultset.
    - If you want more extensive documentation on any option(s) just type
        "doc (any number of options separated by spaces)"
        and gorp will display some documentation on each option you named.
    - To change how some options (currently just the -u, -k, and -pdf options)
        behave, and to see if any text files found have bad encodings, enter
        "DEFAULTS".
    - You can reset all the default behaviors to their original values with
        "DEFAULTS.reset()".
    - You can set a DEFAULT option as well, e.g. "DEFAULTS.PROMPT_K_OPTION = True"

or you can start an interactive session::
    
    C:/Users/mjols/Python39/gorp> python -m gorp
    gorp> doc y c
    -y (read YAML files as YAML, using gorp.jsonpath. See -j option documentation)

    -c(ount occurrences of pattern)

    gorp> cd..
    gorp> cd
    C:\Users\mjols\Python39
    gorp> -r -f -i meat /delicious
    Invalid query.
    gorp> -r -f -i 'meat' /delicious
    2 files
    [
    'C:\\Users\\mjols\\Python39\\delicious\\walnut\\AHH_FRESH_MEAT.txt',
    'C:\\Users\\mjols\\Python39\\delicious\\walnut\\waffles\\AHH_FRESH_MEAT.txt'
    ]
    gorp> how do you turn this on
    Invalid query.
    gorp> prev -}} -c 'MEAT'
    1 files
    {
    'C:\\Users\\mjols\\Python39\\delicious\\walnut\\waffles\\AHH_FRESH_MEAT.txt': 10
    }
    gorp> q

    Goodbye!

