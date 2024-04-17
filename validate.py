# load the necessary components
from lxml import etree
from trafilatura.xml import validate_tei

# open a file and parse it
mytree = etree.parse('rune03.xml')

# validate it
print(validate_tei(mytree))
# returns True or an error message