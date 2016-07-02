#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse("user_data.xml")
root = tree.getroot()

urls = (
    "/persons", "ListPersons",
    "/persons/(.*)", "GetPerson",
)

app = web.application(urls, globals())

class ListPersons:        
    def GET(self):
        output = "[";
        for child in root:
            print "child", child.tag, child.attrib
            output += str(child.attrib).replace("\'", "\"") + ","
        output = output[:-1] + "]";
        return output

class GetPerson:
    def GET(self, personNumber):
        for child in root:
            if child.attrib["personNumber"] == personNumber:
                return str(child.attrib).replace("\'", "\"")
            
if __name__ == "__main__":
    app.run()
