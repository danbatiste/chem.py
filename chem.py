import json

## Get elements data
with open('elements.json', 'r') as file:
    data = file.read()
elements = json.loads(data)

def orbitals(inpt, ion=0, output_type="include_chars"):
    """Returns the orbitals of an element.
    
    inpt: The input, as either a number (34) or an element ("Se")
    ion: Adds charges to the input.
    output_type: "raw", "include_chars", or "numbers".
        - Default: "include_chars"
    """
    ## Overloads the function
    if type(inpt) == str:
        electron_num = atomic_number(inpt)
    else:
        electron_num = inpt + ion
    
    ## Generates the orbitals
    def orbital_gen():
        orbital_chars = "spdfghijklmnopqrstuvwxyz"
        n = 1
        while 1:
            for i in range(1,n+1):
                yield (n, orbital_chars[i-1], 2*(2*i-1))
            n += 1
    gen = orbital_gen()
    orbital_list = []
    while electron_num > 0:
        n, char, es = next(gen)
        electron_num -= es
        if electron_num < 0:
            es = electron_num+es
        if output_type in ["raw", "include_chars"]:
            orbital_list.append([n, char, es])
        elif output_type=="numbers":
            orbital_list.append(es)      
    ## Outputs the correct format
    if output_type == "include_chars":
        formatted = ' '.join([f"{n}{char}{es}" for n, char, es in orbital_list])
        return formatted
    else:
        return orbital_list
    
    
def atomic_mass(element):
    """Returns the atomic mass given an element's symbol."""
    global elements
    amu_dict = dict([(k, v[0]) for k, v in elements.items()])
    return amu_dict[element]


def atomic_number(element):
    """Returns the atomic number given an element's symbol."""
    global elements
    an_dict = dict([(k, v[2]) for k, v in elements.items()])
    return an_dict[element]


# Constants
h = 6.62607015*10**-34    ## Planck constant (J*s)
N0 =  6.02214076*10**23   ## Avagadro number (counting number)
c = 299792458             ## Speed of light (m/s)
k = 2.179*10**-18         ## Rydberg constant (J)
R = 10973731.568160       ## Rydberg constant (1/m)