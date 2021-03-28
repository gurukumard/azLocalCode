import logging

import azure.functions as func

import xml.etree.ElementTree as ET

import glob as g

def converttoxml():
    root = ET.Element('catalog') # root tag name
    root.text = '\n'    # newline before the book element

    path = "C:/Users/124507/Documents/azLocalCode/InsertRecords.csv"
    for filename in g.glob(path):
        with open(filename) as f:
            firstline = f.readlines(1)    
            tags = [word for line in firstline for word in line.split('|')]       
            
            for line in f:   
                            
                if '\n' in line:
                    

                    book = ET.SubElement(root, 'book')
                    book.text = '\n'
                    book.tail = '\n\n'

                # Split the line into a List.
                    F1 = line.split('|')
                                
                count = 0
                for data in F1:                            
                    tags1 = tags[count].strip()     
                    e = ET.SubElement(book, tags1.lower())
                    e.text = data.strip()
                    e.tail = '\n'
                    count += 1                 

        # Display for debugging            
        #ET.dump(root)
            

        # Include the root element to the tree and write the tree
        # to the file.
        tree = ET.ElementTree(root)
        tree.write('C:/Users/124507/Documents/azLocalCode/InsertRecords.xml', encoding='utf-8', xml_declaration=True)
        f.close()
test = converttoxml()