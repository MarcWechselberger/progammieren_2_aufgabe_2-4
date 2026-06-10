import json
from PIL import Image

def get_person_data():
    """
    Returns the person data loaded from the JSON file.
    """
    with open("data/person_db.json", "r", encoding="utf-8") as file:
        person_data = json.load(file)

    person_object_list = []
    for person_dict in person_data:
        person_object = Person( person_dict["id"],
                                person_dict["date_of_birth"],
                                person_dict["firstname"],
                                person_dict["lastname"],
                                person_dict["picture_path"],
                                person_dict["ekg_tests"],
                                person_dict["gender"]
                                )
        person_object_list.append(person_object)
    return person_object_list


def get_person_object_by_full_name(full_name):
    persons = get_person_data()
    firstname = full_name.split(", ")[1]
    lastname = full_name.split(", ")[0]

    for person in persons:
        if person.firstname==firstname and person.lastname==lastname:
            return person

class Person:

    @staticmethod
    def load_person_data():
        """A Function that knows where the person database is and returns a dictionary with the persons"""
        # Opening JSON file
        file = open("data/person_db.json")
        # Loading the JSON File in a dictionary
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names

    @staticmethod
    def find_person_data_by_name(person_data, name):
        """A Function that takes the persons-dictionary and a name and returns the data of the person with this name"""
        for eintrag in person_data:
            if eintrag["lastname"] + ", " +  eintrag["firstname"] == name:
                return eintrag
        return None
    
    @staticmethod
    def load_by_id():
        pass

    def __init__(self, id : int, date_of_birth : int, firstname, lastname, picture_path, ekg_tests, gender = "Male"):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests
        self.hr_max = 220 - (2026-int(date_of_birth))
        self.gender = gender


    def set_hr(self, hr):
        self.hr_max = hr

    def get_full_name(self):
        return self.lastname + ", " + self.firstname

    def get_image(self):
        image = Image.open(self.picture_path)
        return image
    
    def calc_age(self):
        pass

    def calc_max_hr(self):
        pass



if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name(Person.load_person_data(), "Huber, Julian"))