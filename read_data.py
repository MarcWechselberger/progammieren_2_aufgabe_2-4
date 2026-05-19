import json

def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    # Opening JSON file
    file = open("data/person_db.json")
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    return person_data

def get_person_list(person_data):
    """A Function that takes the persons-dictionary and returns a list auf all person names"""
    list_of_names = []

    for eintrag in person_data:
        list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
    return list_of_names

def find_person_data_by_name(person_data, name):
    """A Function that takes the persons-dictionary and a name and returns the data of the person with this name"""
    for eintrag in person_data:
        if eintrag["lastname"] + ", " +  eintrag["firstname"] == name:
            return eintrag
    return None

if __name__ == "__main__":
    #person_data = load_person_data()
    #list_of_names = get_person_list(person_data)
    #print(list_of_names)
    a = find_person_data_by_name(load_person_data(), "Heyer, Yannic")
    print(a)