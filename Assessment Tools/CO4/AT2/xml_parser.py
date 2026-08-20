import xml.etree.ElementTree as ET

try:
    tree = ET.parse("users.xml")
    root = tree.getroot()

    print("User Details")
    print("------------")

    for user in root:
        print("ID    :", user.find("id").text)
        print("Name  :", user.find("name").text)
        print("Email :", user.find("email").text)
        print()

except FileNotFoundError:
    print("Error: Unable to load XML file")

except ET.ParseError:
    print("Error: Invalid XML file")