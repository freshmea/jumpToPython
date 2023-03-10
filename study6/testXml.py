import xml.etree.ElementTree as ET

if __name__ == '__main__':
    filepath = './note.html'
    tree = ET.parse(filepath)
    print(type(tree))
    print(tree)

    note = tree.getroot()
    date = note.get('date')
    print(type(date))
    print(date)

    fromElement = note.find('from')
    print(fromElement.text)
    print(fromElement.items())

    toElement = note.find('to')
    print('to text : ', toElement.text)

    headingElement = note.find('heading')
    print('heading text : ', headingElement.text)

    bodyElement = note.find('body')
    print('body text : ', bodyElement.text)
