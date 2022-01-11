class AtomProperties:
    """
    A class storing various properties of atoms

    Attributes
    ----------
    element_to_valences: dict of {element: [valence, ->], ->}
        with element (str) an abbreviation of an element of the periodic table,
        and valence (int) a possible number of covalent bonds that element can
        make
    element_to_atomic_nr: dict of {element: atomic nr, ->}
        with element (str) an abbreviation of an element of the periodic table,
        and atomic nr (int) its atomic number
    element_to_radius: dict of {element: radius, ->}
        with element (str) an abbreviation of an element of the periodic table,
        and radius (float) the atom radius of that element in Angstrom.
    element_to_valence_electrons: dict of {element: valence electrons}
        with element (str) an abbreviation of an element of the periodic table,
        and valence electrons (int) the number of electrons in the valence
        shell of that element
    element_to_shell_nr: dict of {element: shell nr, ->}
        with element (str) an abbreviation of an element of the periodic table,
        and shell nr (int) the number of electron shells of that element
    shell_to_electron_nr: dict of {shell: electron nr, ->}
        with shell (int) the index of an electron shell counting from the
        nucleus, and electron nr (int) the number of electrons in that shell
    shell_to_orbitals: dict of {shell: [orbital, ->], ->}
        with shell (int) the index of an electron shell counting from the
        nucleus, and orbital (str) an electron orbital in that shell
    orbital_order: tuple of (orbital, ->)
        with the orbitals (str) placed in order of them being filled with
        electrons in nature
    orbital_type_to_orbital_number: dict of {orbital type: orbital number, ->}
        with orbital type (str) the type of orbital (s, p, d, f, g), and
        orbital number the number of orbitals of that type an atom has

    """
    element_to_valences = {'C': [4],
                           'O': [2],
                           'N': [3],
                           'P': [3, 5],
                           'S': [2, 4, 6],
                           'Cl': [1, 7],
                           'Br': [1, 7],
                           'Se': [2],
                           'Si': [4],
                           'B': [3],
                           'As': [3, 5],
                           'F': [1],
                           'H': [1],
                           'I': [1, 7],
                           'Na': [1],
                           'Fe': [2, 3],
                           '*': [1]}

    element_to_amu = {'H': 1.00797,
                      '*': -1.0,
                      'He': 4.00260,
                      'Li': 6.941,
                      'Be': 9.01218,
                      'B': 10.81,
                      'C': 12.011,
                      'N': 14.0067,
                      'O': 15.9994,
                      'F': 18.998403,
                      'Ne': 20.179,
                      'Na': 22.98977,
                      'Mg': 24.305,
                      'Al': 26.98154,
                      'Si': 28.0855,
                      'P': 30.97376,
                      'S': 32.06,
                      'Cl': 35.453,
                      'Ar': 39.948,
                      'K': 39.0983,
                      'Ca': 40.08,
                      'Sc': 44.9559,
                      'Ti': 47.90,
                      'V': 50.9415,
                      'Cr': 51.996,
                      'Mn': 54.9380,
                      'Fe': 55.847,
                      'Co': 58.9332,
                      'Ni': 58.70,
                      'Cu': 63.546,
                      'Zn': 65.38,
                      'Ga': 69.72,
                      'Ge': 72.59,
                      'As': 74.9216,
                      'Se': 78.96,
                      'Br': 79.904,
                      'Kr': 83.80,
                      'Rb': 85.4678,
                      'Sr': 87.62,
                      'Y': 88.9059,
                      'Zr': 91.22,
                      'Nb': 92.9064,
                      'Mo': 95.94,
                      'Tc': 98,
                      'Ru': 101.07,
                      'Rh': 102.9055,
                      'Pd': 106.4,
                      'Ag': 107.868,
                      'Cd': 112.41,
                      'In': 114.82,
                      'Sn': 118.69,
                      'Sb': 121.75,
                      'I': 126.9045,
                      'Te': 127.60,
                      'Xe': 131.30,
                      'Cs': 132.9054,
                      'Ba': 137.33,
                      'La': 138.9055,
                      'Ce': 140.12,
                      'Pr': 140.9077,
                      'Nd': 144.24,
                      'Pm': 145,
                      'Sm': 150.4,
                      'Eu': 151.96,
                      'Gd': 157.25,
                      'Tb': 158.9254,
                      'Dy': 162.50,
                      'Ho': 164.9304,
                      'Er': 167.26,
                      'Tm': 168.9342,
                      'Yb': 173.04,
                      'Lu': 174.967,
                      'Hf': 178.49,
                      'Ta': 180.9479,
                      'W': 183.85,
                      'Re': 186.207,
                      'Os': 190.2,
                      'Ir': 192.22,
                      'Pt': 195.09,
                      'Au': 196.9665,
                      'Hg': 200.59,
                      'Tl': 204.37,
                      'Pb': 207.2,
                      'Bi': 208.9804,
                      'Po': 209,
                      'At': 210,
                      'Rn': 222,
                      'Fr': 223,
                      'Ra': 226.0254,
                      'Ac': 227.0278,
                      'Pa': 231.0359,
                      'Th': 232.0381,
                      'Np': 237.0482,
                      'U': 238.029,
                      'Pu': 242,
                      'Am': 243,
                      'Bk': 247,
                      'Cm': 247,
                      'No': 250,
                      'Cf': 251,
                      'Es': 252,
                      'Hs': 255,
                      'Mt': 256,
                      'Fm': 257,
                      'Md': 258,
                      'Lr': 260,
                      'Rf': 261,
                      'Bh': 262,
                      'Db': 262,
                      'Sg': 263,
                      'Uun': 269,
                      'Uuu': 272,
                      'Uub': 277,
                      'Uuq': None}

    element_to_atomic_nr = {'H': 1,
                            '*': 1,
                            'He': 2,
                            'Li': 3,
                            'Be': 4,
                            'B': 5,
                            'C': 6,
                            'N': 7,
                            'O': 8,
                            'F': 9,
                            'Ne': 10,
                            'Na': 11,
                            'Mg': 12,
                            'Al': 13,
                            'Si': 14,
                            'P': 15,
                            'S': 16,
                            'Cl': 17,
                            'Ar': 18,
                            'K': 19,
                            'Ca': 20,
                            'Sc': 21,
                            'Ti': 22,
                            'V': 23,
                            'Cr': 24,
                            'Mn': 25,
                            'Fe': 26,
                            'Co': 27,
                            'Ni': 28,
                            'Cu': 29,
                            'Zn': 30,
                            'Ga': 31,
                            'Ge': 32,
                            'As': 33,
                            'Se': 34,
                            'Br': 35,
                            'Kr': 36,
                            'Rb': 37,
                            'Sr': 38,
                            'Y': 39,
                            'Zr': 40,
                            'Nb': 41,
                            'Mo': 42,
                            'Tc': 43,
                            'Ru': 44,
                            'Rh': 45,
                            'Pd': 46,
                            'Ag': 47,
                            'Cd': 48,
                            'In': 49,
                            'Sn': 50,
                            'Sb': 51,
                            'Te': 52,
                            'I': 53,
                            'Xe': 54,
                            'Cs': 55,
                            'Ba': 56,
                            'La': 57,
                            'Ce': 58,
                            'Pr': 59,
                            'Nd': 60,
                            'Pm': 61,
                            'Sm': 62,
                            'Eu': 63,
                            'Gd': 64,
                            'Tb': 65,
                            'Dy': 66,
                            'Ho': 67,
                            'Er': 68,
                            'Tm': 69,
                            'Yb': 70,
                            'Lu': 71,
                            'Hf': 72,
                            'Ta': 73,
                            'W': 74,
                            'Re': 75,
                            'Os': 76,
                            'Ir': 77,
                            'Pt': 78,
                            'Au': 79,
                            'Hg': 80,
                            'Tl': 81,
                            'Pb': 82,
                            'Bi': 83,
                            'Po': 84,
                            'At': 85,
                            'Rn': 86,
                            'Fr': 87,
                            'Ra': 88,
                            'Ac': 89,
                            'Th': 90,
                            'Pa': 91,
                            'U': 92,
                            'Np': 93,
                            'Pu': 94,
                            'Am': 95,
                            'Cm': 96,
                            'Bk': 97,
                            'Cf': 98,
                            'Es': 99,
                            'Fm': 100,
                            'Md': 101,
                            'No': 102,
                            'Lr': 103,
                            'Rf': 104,
                            'Db': 105,
                            'Sg': 106,
                            'Bh': 107,
                            'Hs': 108,
                            'Mt': 109,
                            'Uun': 110,
                            'Uuu': 111,
                            'Uub': 112,
                            'Uuq': 114}

    element_to_radius = {'H': 0.37,
                         '*': 0.37,
                         'He': 0.32,
                         'Li': 1.34,
                         'Be': 0.90,
                         'B': 0.82,
                         'C': 0.77,
                         'N': 0.75,
                         'O': 0.73,
                         'F': 0.71,
                         'Ne': 0.69,
                         'Na': 1.54,
                         'Mg': 1.30,
                         'Al': 1.18,
                         'Si': 1.11,
                         'P': 1.06,
                         'S': 1.02,
                         'Cl': 0.99,
                         'Ar': 0.97,
                         'K': 1.96,
                         'Ca': 1.74,
                         'Sc': 1.44,
                         'Ti': 1.36,
                         'V': 1.25,
                         'Cr': 1.27,
                         'Mn': 1.39,
                         'Fe': 1.25,
                         'Co': 1.26,
                         'Ni': 1.21,
                         'Cu': 1.38,
                         'Zn': 1.31,
                         'Ga': 1.26,
                         'Ge': 1.22,
                         'As': 1.19,
                         'Se': 1.16,
                         'Br': 1.14,
                         'Kr': 1.10,
                         'I': 1.33}

    element_to_valence_electrons = {'H': 1,
                                    '*': 1,
                                    'B': 3,
                                    'C': 4,
                                    'Si': 4,
                                    'As': 5,
                                    'Te': 5,
                                    'O': 6,
                                    'N': 5,
                                    'P': 5,
                                    'S': 6,
                                    'Se': 6,
                                    'Cl': 7,
                                    'Br': 7,
                                    'F': 7,
                                    'I': 7,
                                    'Na': 1}

    element_to_electronegativity = {'Xe': 0.0,
                                    'Fr': 0.7,
                                    'Cs': 0.79,
                                    'Rb': 0.82,
                                    'K': 0.82,
                                    'Ba': 0.89,
                                    'Ra': 0.9,
                                    'Na': 0.93,
                                    'Sr': 0.95,
                                    'Li': 0.98,
                                    'Ca': 1.0,
                                    'Yb': 1.1,
                                    'La': 1.1,
                                    'Ac': 1.1,
                                    'Ce': 1.12,
                                    'Pr': 1.13,
                                    'Pm': 1.13,
                                    'Nd': 1.14,
                                    'Sm': 1.17,
                                    'Tb': 1.2,
                                    'Gd': 1.2,
                                    'Eu': 1.2,
                                    'Dy': 1.22,
                                    'Y': 1.22,
                                    'Ho': 1.23,
                                    'Er': 1.24,
                                    'Tm': 1.25,
                                    'Lu': 1.27,
                                    'Pu': 1.28,
                                    'No': 1.3,
                                    'Es': 1.3,
                                    'Th': 1.3,
                                    'Hf': 1.3,
                                    'Md': 1.3,
                                    'Bk': 1.3,
                                    'Am': 1.3,
                                    'Lr': 1.3,
                                    'Cf': 1.3,
                                    'Cm': 1.3,
                                    'Fm': 1.3,
                                    'Mg': 1.31,
                                    'Zr': 1.33,
                                    'Np': 1.36,
                                    'Sc': 1.36,
                                    'U': 1.38,
                                    'Ta': 1.5,
                                    'Pa': 1.5,
                                    'Ti': 1.54,
                                    'Mn': 1.55,
                                    'Be': 1.57,
                                    'Nb': 1.6,
                                    'Al': 1.61,
                                    'V': 1.63,
                                    'Zn': 1.65,
                                    'Cr': 1.66,
                                    'Cd': 1.69,
                                    'In': 1.78,
                                    'Ga': 1.81,
                                    'Fe': 1.83,
                                    'Co': 1.88,
                                    'Si': 1.9,
                                    'Re': 1.9,
                                    'Tc': 1.9,
                                    'Cu': 1.9,
                                    'Ni': 1.91,
                                    'Ag': 1.93,
                                    'Sn': 1.96,
                                    'Po': 2.0,
                                    'Hg': 2.0,
                                    'Ge': 2.01,
                                    'Bi': 2.02,
                                    'Tl': 2.04,
                                    'B': 2.04,
                                    'Sb': 2.05,
                                    'Te': 2.1,
                                    'Mo': 2.16,
                                    'As': 2.18,
                                    'P': 2.19,
                                    'H': 2.2,
                                    'Ir': 2.2,
                                    'Ru': 2.2,
                                    'Os': 2.2,
                                    'At': 2.2,
                                    'Pd': 2.2,
                                    'Pt': 2.28,
                                    'Rh': 2.28,
                                    'Pb': 2.33,
                                    'W': 2.36,
                                    'Au': 2.54,
                                    'C': 2.55,
                                    'Se': 2.55,
                                    'S': 2.58,
                                    'I': 2.66,
                                    'Br': 2.96,
                                    'N': 3.04,
                                    'Cl': 3.16,
                                    'O': 3.44,
                                    'F': 3.98}

    element_to_shell_nr = {'H': 1,
                           'He': 1,
                           'Li': 2,
                           'Be': 2,
                           'B': 2,
                           'C': 2,
                           'N': 2,
                           'O': 2,
                           'F': 2,
                           'Ne': 2,
                           'Na': 3,
                           'Mg': 3,
                           'Al': 3,
                           'Si': 3,
                           'P': 3,
                           'S': 3,
                           'Cl': 3,
                           'Ar': 3,
                           'K': 4,
                           'Ca': 4,
                           'Sc': 4,
                           'Ti': 4,
                           'V': 4,
                           'Cr': 4,
                           'Mn': 4,
                           'Fe': 4,
                           'Co': 4,
                           'Ni': 4,
                           'Cu': 4,
                           'Zn': 4,
                           'Ga': 4,
                           'Ge': 4,
                           'As': 4,
                           'Se': 4,
                           'Br': 4,
                           'Kr': 4,
                           'Rb': 5,
                           'Sr': 5,
                           'Y': 5,
                           'Zr': 5,
                           'Nb': 5,
                           'Mo': 5,
                           'Tc': 5,
                           'Ru': 5,
                           'Rh': 5,
                           'Pd': 5,
                           'Ag': 5,
                           'Cd': 5,
                           'In': 5,
                           'Sn': 5,
                           'Sb': 5,
                           'Te': 5,
                           'I': 5,
                           'Xe': 5,
                           'Cs': 6,
                           'Ba': 6,
                           'La': 6,
                           'Ce': 6,
                           'Pr': 6,
                           'Nd': 6,
                           'Pm': 6,
                           'Sm': 6,
                           'Eu': 6,
                           'Gd': 6,
                           'Tb': 6,
                           'Dy': 6,
                           'Ho': 6,
                           'Er': 6,
                           'Tm': 6,
                           'Yb': 6,
                           'Lu': 6,
                           'Hf': 6,
                           'Ta': 6,
                           'W': 6,
                           'Re': 6,
                           'Os': 6,
                           'Ir': 6,
                           'Pt': 6,
                           'Au': 6,
                           'Hg': 6,
                           'Tl': 6,
                           'Pb': 6,
                           'Bi': 6,
                           'Po': 6,
                           'At': 6,
                           'Rn': 6,
                           'Fr': 7,
                           'Ra': 7,
                           'Ac': 7,
                           'Th': 7,
                           'Pa': 7,
                           'U': 7,
                           'Np': 7,
                           'Pu': 7,
                           'Am': 7,
                           'Cm': 7,
                           'Bk': 7,
                           'Cf': 7,
                           'Es': 7,
                           'Fm': 7,
                           'Md': 7,
                           'No': 7,
                           'Lr': 7,
                           'Rf': 7,
                           'Db': 7,
                           'Sg': 7,
                           'Bh': 7,
                           'Hs': 7,
                           'Mt': 7,
                           'Ds': 7,
                           'Rg': 7,
                           'Cn': 7,
                           'Nh': 7,
                           'Fl': 7,
                           'Mc': 7,
                           'Lv': 7,
                           'Ts': 7,
                           'Og': 7,

                           '*': 1}

    shell_to_electron_nr = {1: 2,
                            2: 8,
                            3: 18,
                            4: 32,
                            5: 32}

    shell_to_orbitals = {1: ['1s'],
                         2: ['2s', '2p1', '2p2', '2p3'],
                         3: ['3s', '3p1', '3p2', '3p3', '3d1', '3d2', '3d3', '3d4', '3d5'],
                         4: ['4s', '4p1', '4p2', '4p3', '4d1', '4d2', '4d3', '4d4', '4d5', '4f1',
                             '4f2', '4f3', '4f4', '4f5', '4f6', '4f7'],
                         5: ['5s', '5p1', '5p2', '5p3', '5d1', '5d2', '5d3', '5d4', '5d5', '5f1',
                             '5f2', '5f3', '5f4', '5f5', '5f6', '5f7']}

    orbital_order = (
    '1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p',
    '8s', '5g', '6f', '7d', '8p', '9s')

    orbital_type_to_orbital_number = {'s': 1,
                                      'p': 3,
                                      'd': 5,
                                      'f': 7,
                                      'g': 9}

    metals = {'Li', 'Be', 'Na', 'Mg', 'Al', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv'}

    organic = {'C', 'O', 'N', 'P', 'H', 'S', 'Cl', 'Br', 'I', 'F', '*'}

    metal_to_charge = {'Li': {1},
                       'Na': {1},
                       'K': {1},
                       'Rb': {1},
                       'Cs': {1},
                       'Fr': {1},
                       'Be': {2},
                       'Mg': {2},
                       'Ca': {2},
                       'Sr': {2},
                       'Ba': {2},
                       'Ra': {2},
                       'Cr': {3, 6},
                       'Mn': {2},
                       'Fe': {2, 3},
                       'Co': {2},
                       'Ni': {2},
                       'Pt': {2},
                       'Cu': {1, 2},
                       'Ag': {1},
                       'Au': {1, 3},
                       'Zn': {2},
                       'Cd': {2},
                       'Hg': {2},
                       'Al': {3}}


ATOM_PROPERTIES = AtomProperties()