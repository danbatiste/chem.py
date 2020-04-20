import json

with open('elements.json', 'r') as file:
    data = file.read()
    
elements = json.loads(data)
def atomic_mass(element):
    global elements
    amu_dict = dict([(k, v[0]) for k, v in elements.items()])
    return amu_dict[element]

def atomic_number(element):
    global elements
    an_dict = dict([(k, v[2]) for k, v in elements.items()])
    return an_dict[element]


# Constants
h = 6.62607015*10**-34    ## Planck constant (J*s)
N0 =  6.02214076*10**23   ## Avagadro number (counting number)
c = 299792458             ## Speed of light (m/s)
k = 2.179*10**-18         ## Rydberg constant (J)
R = 10973731.568160       ## Rydberg constant (1/m)