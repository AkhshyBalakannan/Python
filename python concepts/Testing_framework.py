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

# PYTHON HAS AN SETUP()
# METHOD WHICH WILL BE INITIALIZED EACH AND EVERY TIME THE TEST CLASS IS CALLED
# THIS CAN BE USED TO INITIALIZE THE NAME OF FILE EACH TIME


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

# WE ALSO HAVE A TEARDOWN METHOD THAT IS USED TO TEAR DOWN THE SETUP METHOD

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
# OR IT COMMON IT DOES NOT HAVE THE SETUP AND TEARDOWN MODULE

# WE CAN USE PYTEST


# PYTEST -H WILL GIVE ALL THE FLAGS

# ASSERT ARE STATEMENT WHICH ARE USED TO CHECK THE FUNCTION WITH EXPECTED VALUES


def test_add():  # we need to import the file
    assert math_func.add(7, 3) == 10
    assert math_func.add(5, 5) == 10
