# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [Unreleased] - yyyy-mm-dd
 
### To Be Added

- Allow '-u' option to be used to update XML files with the '-x' option, and possibly all files with the '-b' option.

- Add "tab" option for reading tabular files like CSV, TSV and Excel.
tabular_excel.py is in gorp as a placeholder.

- For the "tab" option to be really useful, the -w option would have to be 
able to write to CSV and similar as well.

- Determine minimum version of all dependencies and optional dependencies, and
add specifications where appropriate.

- add 'mv' option for moving files
 
### To Be Changed

- Improve gorp.jsonpath.aggregate. Ideas include allowing aggregation by the *values* of fields, rather than just by *keys*.
 
### To Be Fixed
 
- NOTE: Some weird behavior regarding the -f and -a options does persist to the
time of writing:
Even though the directory name is no longer matched by the -f and -a options,
you can't (currently) use -f "^<string>" to find all text-type files with 
base names that start with <string>, even though only the base name is matched.
- The -x option tests are broken for some reason, but the option itself works fine (as of version 2.0.2).
- deal with failing test of PDF option not including redundant copies of files


## [2.0.4] - 2023-08-31

### Fixed

- fixed bug where pdf option results containing PDF text could not be piped to JSON file due to tuple keys.

## [2.0.3] - 2023-03-28

- fixed bug where PDF database would have a bunch of nonexistent files

## [2.0.2] - 2022-03-07

### Added

- The -z option for creating zip files now has two related default options, Z_OPTION_OVERWRITES and PROMPT_Z_OPTION. 
- Similar to the -u option, the -z option now tests to see if a zip file with the given name already exists. If it does, and PROMPT_Z_OPTION is True, it will ask the user if they want to overwrite that file or create a new zip archive with an incremented name.
- If the user agrees to overwrite, or if Z_OPTION_OVERWRITES is True, the file is overwritten.
- If PROMPT_Z_OPTION is False and Z_OPTION_OVERWRITES is False, any name collision will be resolved by incrementing the filename without asking the user for input.

### Changed

- is_iterable now recognizes `bytearray` objects as NOT being iterables, in line with how `str` and `bytes` are treated.
- Upgraded most of my test suite to unittest (gorp.jsonpath is still based on doctest). After FAR too long using a lot of hard-to-read boilerplate code to test gorpy, it was time for a change.
- Used [black](https://github.com/psf/black) to reformat all my code. Nothing can be done for its spaghetti-ness, but at least it will have somewhat professional formatting.
- The -x option will produce an error message when you run the 

## [1.0.0] - 2022-03-02

gorp version 1.0.0 is now available on the Python package index.
It has been tested for Python 3.6 to 3.10.

### Changed

- Changed the way PDF text is stored. Instead of using a JSON file, a sqlite database is now used. 
- This has the added benefit of removing the optional dependency (for the pdf option) on sortedcollections.

### Fixed

- Previously, if pdf text for some filename "X" was cached in pdf_textcache.json, and the file "X" was later changed, the old version of its text that was originally cached would be used. This has been fixed, and now the modified version of the text will correctly overwrite the old text if it is determined that the file was modified. If the file was not modified, it will be left alone.

## [0.4.1] - 2022-02-25

gorp version 0.4.1 is now available on the Python package index. 
It has been tested for Python 3.6 to 3.10.

### Fixed

- "doc m" (see option_docs.py) correctly reflects that you CANNOT use "YYYY-MM-DD hh:mm:ss" datetimes, to filter modification times, and the most precision you can get is YYYY-MM-DD.
- "-s" option won't be auto-triggered when using "-sed" option.
- The "-z" option for zipping files will now work when the query specifies a temporary working directory other than the directory in which the program was when the query was made. For example, queries like `-f 'py' /otherdir -}} -z 'blah.zip'` would previously raise a FileNotFoundError. They should no longer do that.

## [0.4.0] - 2022-02-23

gorp version 0.4.0 is now available on the Python package index. 
It has been tested for Python 3.6 to 3.9.

### Added

- "-m" and "-s" options now allow filtering by modification time and size, respectively. Use "python -m gorp doc m s" to see proper usage.
- A few extensions like 'ts' and 'less' have been added to textTypeFiles.

### Fixed

- "python -m gorp doc f" now displays the text-type files ordered alphabetically.

## [0.3.2] - 2021-11-04

gorp version 0.3.2 is now available on the Python package index. 
It has been tested for Python 3.6 to 3.9.

### Added

- "-tab" option for reading tabular text files (currently supports csv, tsv, 
txt extensions). Syntax used is gorp.jsonpath. Can use pandas or builtin csv. Tests not implemented yet.

### Fixed

- Bug in docx option.

## [0.2.5] - 2021-10-23

gorp version 0.2.5 is now available on the Python package index. 
It has been tested for Python 3.6 to 3.9.

### Added

- "-b" option, which allows you to read raw bytecode of files as if they were text documents.

- The "-z" option for copying files to a ZIP archive now allows for BZIP2 and LZMA compression by calling "-zb" or "-zl", respectively. The default "-z" is still no compression at all.

- "-sed" option for more easily searching for and replacing patterns in text files. This is similar in concept to Linux sed. "(<previous queries> -}})? <options> -sed '<regex>//<repl>' /dirname" means you search all files in dirname (or in the resultset returned by previous queries if there are any) for <regex> and replace every instance with <repl>. See the documentation for the "-u" option and gorp.readfiles.GorpHandler.update(), which this calls behind the scenes.

### Changed

- The "-g" option for running a sequence of commands in a gorp script can now be called from within a Gorp Session.

- The is_iterable() function from gorp.utils now returns False when called on `bytes` objects, in line with how it treats `str` objects. This is probably what users would expect anyway.

### Fixed

- Typos in gorp.jsonpath.aggregate documentation.

## [0.2.4] - 2021-10-08
  
gorp version 0.2.4, which contains gorp.jsonpath 0.2.0, is now available on the
Python package index. It has been tested for Python 3.6 to 3.9.
 
### Added

- '-g' option for reading a series of gorp directives from a text file.
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