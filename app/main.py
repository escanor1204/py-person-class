class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and (person["wife"] is not None):
            wife_object = Person.people[person["wife"]]
            current_person.wife = wife_object
        if "husband" in person and (person["husband"] is not None):
            husband_object = Person.people[person["husband"]]
            current_person.husband = husband_object
    return person_list
