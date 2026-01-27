import re

import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class MolSys:
    def __init__(self, path_in):
        with open(path_in, 'r') as file:
            raw_data = file.read()

        self.atoms, self.residues, self.chains = zip(*(
            self._create_components(line.group()) for line in re.finditer("^ATOM.*$", raw_data, re.MULTILINE)
        ))

    # --------------------------------------------------------------------------
    def _create_components(self, raw_data: str):
        padded_data = f"{raw_data:<{ms.LENGTH_RECORD}}"
        chain   = ms.Chain(padded_data)
        residue = ms.Residue(padded_data)
        atom    = ms.Atom(padded_data)
        return atom, residue, chain


# //////////////////////////////////////////////////////////////////////////////
