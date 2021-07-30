# TESTING FRAME WORK ARE    UNITTEST(D)    NOSE    PYTEST

# UNITTEST IS THE DEFAULT TEST FRAMEWORK THAT IS IN PYTHON

# THIS INCLUDES FOUR STATEMENTS THOSE ARE
# TEST FIXTURE - FIXTURE OF TEST
# TEST CASE - BASE CLASS WITH TEST CASE WHICH MAY CREATE NEW TEST CASE
# TEST SUITE - TEST SUITE IS SUITE OF CODE WHICH RUNS TOGETHER TO EXECUTE MULTI TESTS
# TEST RUNNER - ITS THE GRAPHICAL UNIT IN WHICH THE USER SEE'S THE TEST VALUE

# import math_func.py
import unittest


# CALLING THE CLASS WITH UNITTEST TO INHERENTATE TEST
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # ASSERT EQUAL CHECKS EXACT EQUALITY
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())  # BOOLEAN VALIDATION
        self.assertFalse('Foo'.isupper())  # BOOLEAN VALIDATION

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):  # RAISES ERROR
            s.split(2)


if __name__ == '__main__':
    unittest.main()


# python -m unittest -v test_module
# Unit test support these command lineoptions
# -b --buffer   The standard output and standard error streams are buffered during the test run
# -c, --catch   Control-C during the test run waits for the current test to end and
#               then reports all the results so far
# -f,--failfast Stop the test run on the first error or failure.
# -k            Only run test methods and classes that match the pattern or substring.

# PYTHON HAS AN SETUP()
# METHOD WHICH WILL BE INITIALIZED EACH AND EVERY TIME THE TEST CLASS IS CALLED
# THIS CAN BE USED TO INITIALIZE THE NAME OF FILE EACH TIME


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

# WE ALSO HAVE A TEARDOWN METHOD THAT IS USED TO TEAR DOWN THE SETUP METHOD


# Test Discovery
# cd project_directory
# python - m unittest discover

# The discover sub-command has the following options:

# -v, --verbose                         Verbose output

# -s, --start-directory directory       Directory to start discovery(. default)

# -p, --pattern pattern                 Pattern to match test files(test*.py default)

# -t, --top-level-directory directory   Top level directory of project(defaults to start directory)


# in order to test something, we use one of the assert*() methods
# provided by the TestCase base class. If the test fails, an exception
# will be raised with an explanatory message, and unittest will identify
# the test case as a failure. Any other exceptions will be treated as errors.

# SUITE()
# The subclassing of unititest.TestCase will automatically
# group the functions together and run
# we can also group them how ever we want using the suite method
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


# RE_USING OLD TEST CASE
# Re-using old test case are possible
# Some users will find that they have existing test code that they would like to run
# unittest provides a FunctionTestCase class.
# This subclass of TestCase can be used to wrap an existing test function.
# Set-up and tear-down functions can also be provided.

testcase = unittest.FunctionTestCase(MyTestCase.Test_format,
                                     setUp=startDB,
                                     tearDown=deleteDB)

# The above method is not suggested because creating new testcase can
# solve a lot of headache in future testing purpose

# WE CAN ALSO Skipping tests and expected failures


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass


# SKIPTEST() WILL NOT HAVE THE SETUP METHOD AND TEARDOWN METHOD OR EVEN IN CLASS
# OR IN COMMON IT DOES NOT HAVE THE SETUP AND TEARDOWN MODULE

@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


# We also have subtest that is written inside test function
# this becomes handy when same test should be carried with minor val changes
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
               # the above code is handy because it doesnt stop
                # execution as the first error is encountered


setUpClass()
#   A class method called before tests in an individual class are run.
@classmethod
def setUpClass(cls):


tearDownClass()
# A class method called after tests in an individual class have run.


@classmethod
def tearDownClass(cls):

    # WE CAN USE PYTEST
    # PYTEST -H WILL GIVE ALL THE FLAGS
    # ASSERT ARE STATEMENT WHICH ARE USED TO CHECK THE FUNCTION WITH EXPECTED VALUES


def test_add():  # we need to import the file
    assert math_func.add(7, 3) == 10
    assert math_func.add(5, 5) == 10
