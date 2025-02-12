import pytest
from lib.dog import Dog # Replace 'lib.dog' with your actual path

class TestDog:
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name=123)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be a string.\n")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_saves_if_valid(self):
        dog = Dog(name = "Sparky", breed = "Labrador")
        assert dog.name == "Sparky"
        assert dog.breed == "Labrador"

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name = "Sparky", breed="Human")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Breed must be in list of approved breeds.\n")

    def test_breed_saves_if_valid(self):
        dog = Dog(name = "Sparky", breed = "Labrador")
        assert dog.name == "Sparky"
        assert dog.breed == "Labrador"