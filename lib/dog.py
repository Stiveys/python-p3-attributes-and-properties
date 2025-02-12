class Dog:
    ALLOWED_BREEDS = ["Labrador", "Golden Retriever", "Poodle"]

    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed
        try:
            self.validate_name()
            self.validate_breed()
        except ValueError as e:
            print(e) # Print the validation error
            self.name = None # Clear the name and breed
            self.breed = None
            # You could instead set a default valid name and breed:
            # self.name = "DefaultName"
            # self.breed = "Labrador"
        else:
             self.name = name
             self.breed = breed

    def validate_name(self):
        if not isinstance(self.name, str):
            raise ValueError("Name must be a string.")
        if not (1 <= len(self.name) <= 25):
            raise ValueError("Name must be string between 1 and 25 characters.")

    def validate_breed(self):
        if self.breed not in self.ALLOWED_BREEDS:
            raise ValueError("Breed must be in list of approved breeds.")

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"