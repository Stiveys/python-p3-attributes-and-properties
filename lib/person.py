class Person:
    ALLOWED_JOBS = ["Teacher", "Engineer", "Doctor"]

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job
        try:
            self.validate_name()
            self.validate_job()
            self.name = self.name.title()
        except ValueError as e:
            print(e)
            self.name = None
            self.job = None
        else:
            self.name = name
            self.job = job

    def validate_name(self):
        if not isinstance(self.name, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(self.name) <= 25):
            raise ValueError("Name must be string between 1 and 25 characters.")

    def validate_job(self):
        if self.job not in self.ALLOWED_JOBS:
            raise ValueError("Job must be in list of approved jobs.")

    def __repr__(self):
        return f"Person(name='{self.name}', job='{self.job}')"