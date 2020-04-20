# chem.py
Python package for basic chemistry calculations.

```python
>>> from chem import atomic_mass as amu, atomic_number as anum
>>> from chem import *

>>> amu("O")
15.9994

>>> anum("O")
8

>>> orbitals("O")
'1s2 2s2 2p4'

>>> orbitals("O", charge=1)
'1s2 2s2 2p3'

>>> N0   ## Avagadro's number
6.02214076e+23
```
