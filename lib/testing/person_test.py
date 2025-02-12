import pytest
from lib.person import Person  # Replace 'lib.person' with your actual path

class TestPerson:
    def test_job_not_in_list(self):
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name = "Steve", job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Job must be in list of approved jobs.\n")

    def test_name_not_empty(self):
        import io, sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")