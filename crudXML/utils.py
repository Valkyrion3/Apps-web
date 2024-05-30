import xml.etree.ElementTree as ET

def parse_xml_content(content):
    root = ET.fromstring(content)
    car_data = {
        'color': root.findtext('color'),
        'textura': root.findtext('textura'),
        'precio': root.findtext('precio'),
        'modelo': root.findtext('modelo'),
        'marca': root.findtext('marca'),
        'potencia': root.findtext('potencia'),
        'vel_max': root.findtext('vel_max'),
        'tipo_transmision': root.findtext('tipo_transmision'),
        'tipo_combustible': root.findtext('tipo_combustible'),
    }
    return car_data