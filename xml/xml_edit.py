import time
import xml.etree.cElementTree as ET

def editXML(filename):
    """
    Edit an example XML file
    """
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    for begin_time in root.iter("begin"): #use ElementTree’s iter() method to find all the tags that are labeled “begin”
        begin_time.text = time.ctime(int(begin_time.text))

        tree = ET.ElementTree(root)
    with open("updated.xml", "wb") as f:
        tree.write(f)

if __name__ == "__main__":
    editXML("apts_to_edit.xml")