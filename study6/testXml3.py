import xml.etree.ElementTree as ET

if __name__ == '__main__':
    note = ET.Element('note')
    note.attrib['date'] = '20220926'

    to = ET.Element('to')
    to.text = 'AIoT'
    # note.append(to)

    # ET.SubElement(note, 'to').text = 'AIoT'

    ET.SubElement(note, 'from').text = 'freshmea'
    ET.SubElement(note, 'heading').text = 'notice'
    ET.SubElement(note, 'body').text = 'life is too short\n'
    ET.SubElement(note, 'heading').text = 'notice'

    ET.dump(note)
    ET.dump(to)
