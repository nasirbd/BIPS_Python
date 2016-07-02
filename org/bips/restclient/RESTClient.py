#!/usr/bin/env python
import requests

def allPersons():
    response = requests.get('http://localhost:8080/persons')
    data = response.json()
    print "Information of all persons: "
    print
    for person in data:
        print "****************************"    
        for field in person.keys():
            print field + ": " + person.get(field)
    
        print "****************************"
        print
    
def getPersonInfoWithPersonNumber(personNumber):
    response = requests.get('http://localhost:8080/persons/' + personNumber)
    data = response.json()
    print "****************************"    
    print "Information of person: "
    print "Person number: " + data.get("personNumber")
    print "Name: " + data.get("name")
    print "Address: " + data.get("address")
    print "****************************"


# allPersons()
getPersonInfoWithPersonNumber("198512203335")
# getPersonInfoWithPersonNumber("199112277604")
# getPersonInfoWithPersonNumber("198401014435")

    