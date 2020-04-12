import json

with open('elements.json', 'r') as file:
    data = file.read()
    
elements = json.loads(data)
amu = dict([(k, v[0]) for k, v in elements.items()])

# Constants
h = 6.62607015*10**-34    ## Planck constant (J*s)
N0 =  6.02214076*10**23   ## Avagadro number (counting number)
c = 299792458             ## Speed of light (m/s)
