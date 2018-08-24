# _*_ coding: utf-8 _*_
import xml.sax
import os

class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_node = ""
        self.title = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, name, attr):
        self.current_node = name
        if name == "movie":
            print("*** Movie ***")
            self.title = attr['title']
            print("title: ", self.title)
    
    def characters(self, content):
        if self.current_node == "type":
            self.type = content
        if self.current_node == "format":
            self.format = content
        if self.current_node == "year":
            self.year = content
        if self.current_node == "rating":
            self.rating = content
        if self.current_node == "stars":
            self.stars = content
        if self.current_node == "description":
            self.description = content

    def endElement(self, tag):
        if tag == "type":
            print("Type: ", self.type)
        if tag == "format":
            print("Format: ", self.format)
        if tag == "year":
            print("Year: ", self.year)
        if tag == "rating":
            print("Rating: ", self.rating)
        if tag == "stars":
            print("Stars: ", self.stars)
        if tag == "description":
            print("Description: ", self.description)


if __name__ == "__main__":
    file_path = os.path.abspath("20180823/demo.xml")
    with open(file_path, "r") as f:
        content = f.read()
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        handler = XmlHandler()
        parser.setContentHandler(handler)
        parser.parse(file_path)
