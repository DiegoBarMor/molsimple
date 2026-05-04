import sys
from pathlib import Path

import molsimple as ms

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    molsys = ms.MolSys(PATH_STRUCT)
    print(*molsys.atoms)
    print(*molsys.residues)
    print(*molsys.chains)


################################################################################
if __name__ == "__main__":
    PATH_STRUCT = Path(sys.argv[1])
    main()
    print(ms.get_pdb_constants())


################################################################################
# python3 main.py testdata/ade.pdb
