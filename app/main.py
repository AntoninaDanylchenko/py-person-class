class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        if person["name"] not in Person.people:
            Person(person["name"], person["age"])
        find_husband_wife(person)
    return list(Person.people.values())


def find_husband_wife(person: dict) -> None:
    name = person["name"]

    wife_name = person.get("wife")
    if wife_name and wife_name in Person.people:
        setattr(Person.people[name], "wife", Person.people[wife_name])

    husband_name = person.get("husband")
    if husband_name and husband_name in Person.people:
        setattr(Person.people[name], "husband", Person.people[husband_name])
