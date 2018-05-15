from ncclient import manager
import sys
import xml.dom.minidom

HOST='10.1.100.33'

PORT = 830

USER='cisco'
PASS='cisco'

FILE='get_interface_gigabit3.xml'

def get_configured_interfaces(xml_filter):
  with manager.connect(host=HOST, port=PORT, username=USER, password=PASS, hostkey_verify=FALSE, device_params={'name':'default'}, allow_agent=False, look_for_keys) as m:
   with open(xml_filter) as f:
    return(m.get_config('running', f.read()))

def main():
  interfaces = get_configured_interfaces(FILE)
  interfaces = xml.dom.minidom.parseString(interfaces.xml)
  interfaces = interfaces.getElementsBy TagName("interfaces")
  print(interfaces[0].toprettyxml())

if _name_=='_main_':
  sys.exit(main())
