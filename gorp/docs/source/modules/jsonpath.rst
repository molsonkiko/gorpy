==========
jsonpath
==========

Contains utilities for performing complex searches in nested Python 
    iterables based on both keys/indices and values.
    This has been tested (using gorp.test.test_jsonpath) on Python 3.6-3.9.
    It might work on 3.5, but no warranty is made except for 3.6-3.9.

The most immediately comparable project in terms of scope is jsonpath_ng, 
    which is fully JsonPath standard-compliant, but which appears to me to 
    lack some of this module's power, such as regex matching on keys.

Some things that you can do with this module:
    * Use regular expressions to match keys as well as values in dicts.
    * Filter layers of JSON based on comparisons of multiple values (e.g., 
        get indices 1:10 of an array only if arr[1] > str(arr[2]))
    * Mutate JSON at the nodes found by a search.
    * Filter pandas DataFrames using the same query language, while still 
        getting their incredibly fast performance.
    * If you prefer not to use a query parser, build layers of filters by an 
        object-oriented approach. See the Filter, GlobalConstraint, Mutator, 
        and JsonPath classes. Thanks to jsonpath_ng for pioneering this 
        approach!
    * Build arithmetic expressions of the values and keys in an iterable 
        without using eval(). See math_eval, and its workhorse function, 
        compute(eqn).

**FUNCTIONS**

.. autofunction:: .jsonpath.json_extract

.. autofunction:: .jsonpath.parse_json_path

.. autofunction:: .jsonpath.mutate_json

.. autofunction:: .jsonpath.mutate_json_repeatedly

**LOANER FUNCTION FROM math_eval**

.. autofunction:: math_eval.compute

**CLASSES**

.. autoclass:: .jsonpath.JsonPath

.. autofunction:: .jsonpath.JsonPath.descend

.. autofunction:: .jsonpath.JsonPath.extract

.. autofunction:: .jsonpath.JsonPath.sub


.. autoclass:: .jsonpath.Filter


.. autoclass:: .jsonpath.GlobalConstraint


.. autoclass:: math_eval.IntRange
