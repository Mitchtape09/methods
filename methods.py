
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greeting(self):
        print(f"Hello, my name is {self.name}")


adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")

adrien.greeting()

cool_person.greeting()
