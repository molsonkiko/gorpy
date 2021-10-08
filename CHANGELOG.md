# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
### To Be Added

- Add "tab" option for reading tabular files like CSV, TSV and Excel.
tabular_excel.py is in gorp as a placeholder.

- For the "tab" option to be really useful, the -w option would have to be 
able to write to CSV and similar as well.

- Add 'b' option to read raw bytecode in a manner (hopefully) similar to Unix
grep's 'a' option.

- Determine minimum version of all dependencies and optional dependencies, and
add specifications where appropriate.
 
### To Be Changed

- Allow -g option to be used within a Python program or a gorp interactive
session.
 
### To Be Fixed
 
- NOTE: Some weird behavior regarding the -f and -a options does persist to the
time of writing:
Even though the directory name is no longer matched by the -f and -a options,
you can't (currently) use -f "^<string>" to find all text-type files with 
base names that start with <string>, even though only the base name is matched.
 
## [0.2.0] - 2021-10-08
  
gorp version 0.2.0, which contains gorp.jsonpath 0.2.0, is now available on the
Python package index. It has been tested for Python 3.6 to 3.9.
 
### Added

- 'g' option for reading a series of gorp directives from a text file.
Currently this can only be done from the command line, not during an
interactive session or while working in a Python shell. This will change soon.

- Aggregation functionality for jsonpath akin to aggregates with GROUP BY in
SQL. For instance, for some JSON file you could use "AGG sum BY 0" to calculate
the sum of all the lowest-level values (like likes on Facebook or whatever)
grouped by the keys at the highest level (0, the first node on the path).
You can use the "max", "min", "avg"|"mean", "sum", "len"|"count" functions,
or make your own in situ using "f(x)" syntax like `"sum(``float`` map y)\*3"`.

- Documentation for the new aggregation functionality in gorp/option_docs,
gorp/jsonpath/aggregate.py and gorp/jsonpath/jsonpath.py.

- Test suites for the -x, -e, -w, and -z options.
 
### Changed

- jsonpath is now a subpackage rather than a module. The core API of JsonPath
and json_extract is in jsonpath/jsonpath.py, the Filter and GlobalConstraint
classes are in jsonpath/filters.py, the Mutator class and mutate_json
functions are in jsonpath/mutate.py, the parser functions are in
jsonpath/parser.py, and the new aggregation functionality is in
jsonpath/aggregate.py.

- Negative integer arguments can be used to constrain the number of files
shown. This is particularly useful in combination with the -m and -s options,
because it allows the user to see the smallest or the oldest files in a set.

- -z option no longer includes the entire hierarchy of parent directories
leading to a file in zipped file names. Previously, if you used the -z option
to zip "C:/Users/mjols/Python39/foo.py" and "C:/Users/mjols/bar.txt" together,
you'd have to navigate through a bunch of folders containing one subfolder and
nothing else to get to the files. Now os.path.commonpath is used to determine
that e.g., those two files could be zipped together as "Python39/foo.py" and 
"bar.txt" without loss of meaningful information.
 
### Fixed
 
- -e option for reading resultsets in from files was broken. Now it works for
both YAML and JSON files.

- Some extensions in gorp.utils.textTypeFiles were changed to all lower-case.
They have to be because extensions are coerced to lower-case before checking
membership in textTypeFiles for the -f option and most text-reading options.

- -x option for reading XML and HTML did not return all results. Now it returns
every match to an XPath or CSS selector, in the form of the full text of the
matched element, including tags. Since there are likely to be multiple
elements with the same tag with the same parents in an XML or HTML document,
the "path" to an element for purposes of the -n option is treated as 
(root, ancestor_2, ..., ancestor_n, ii), where ii is the 0-indexed position of
the element in the list of elements with the same tag and the same ancestors.
 
## [0.1.6] - 2021-10-02
 
### Added

- Initial commit.

- Fixes to gorp/docs to enable correct display of classes on readthedocs.org.

- .readthedocs.yaml and miscellaneous other files for ReadTheDocs support.

### Changed
- The -f and -a options for matching filenames match only the base name of the
file (i.e. only the "foo.py" part of "C:/Users/mjols/Python39/foo.py".
Prior to commit a7ec4b9, the -f and -a options matched the directory name as well. This is usually undesired, because it can result in all
files in a directory being accidentally matched.

### Fixed

- dateutil was not correctly imported initially

- Incorrect use of relative imports in the test suite.