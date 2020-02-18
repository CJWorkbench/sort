sort
----

Workbench module that sorts rows by selected columns' values

Developing
----------

First, get up and running:

#. ``python3 ./setup.py test`` # to test

To add a feature:

#. Write a test in ``test_sort.py``
#. Run ``python3 ./setup.py test`` to prove it breaks
#. Edit ``sort.py`` to make the test pass
#. Run ``python3 ./setup.py test`` to prove it works
#. Commit and submit a pull request

To develop continuously on Workbench:

#. Check this code out in a sibling directory to your checked-out Workbench code
#. Start Workbench with ``bin/dev start``
#. In a separate tab in the Workbench directory, run ``bin/dev develop-module sort``
#. Edit this code; the module will be reloaded in Workbench immediately
