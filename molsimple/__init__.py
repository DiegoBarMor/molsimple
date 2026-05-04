_keys_other = set(globals().keys()) | {"_keys_other"}
LENGTH_RECORD: int = 80
SERIAL_NUM_START: int = 6
SERIAL_NUM_END:   int = 11
ATOM_NAME_START: int = 12
ATOM_NAME_END:   int = 16
ALTLOC_START: int = 16
ALTLOC_END:   int = 17
RESIDUE_NAME_START: int = 17
RESIDUE_NAME_END:   int = 20
CHAIN_ID_START: int = 21
CHAIN_ID_END:   int = 22
RESIDUE_SEQUENCE_NUM_START: int = 22
RESIDUE_SEQUENCE_NUM_END:   int = 26
RESIDUE_INSERTION_CODE_START: int = 26
RESIDUE_INSERTION_CODE_END:   int = 27
X_COORDINATES_START: int = 30
X_COORDINATES_END:   int = 38
Y_COORDINATES_START: int = 38
Y_COORDINATES_END:   int = 46
Z_COORDINATES_START: int = 46
Z_COORDINATES_END:   int = 54
OCCUPANCY_START: int = 54
OCCUPANCY_END:   int = 60
TEMPERATURE_FACTOR_START: int = 60
TEMPERATURE_FACTOR_END:   int = 66
SEGMENT_ID_START: int = 72
SEGMENT_ID_END:   int = 76
ELEMENT_SYMBOL_START: int = 76
ELEMENT_SYMBOL_END:   int = 78
CHARGE_START: int = 78
CHARGE_END:   int = 80
_pdb_constants = {
    k:v for k,v in globals().items() if k not in _keys_other
}
del _keys_other

def get_pdb_constants(skip_length_record: bool = True) -> dict[str, int]:
    obj = _pdb_constants.copy()
    if skip_length_record:
        obj.pop("LENGTH_RECORD")
    return obj

from .parts.atom import Atom
from .parts.residue import Residue
from .parts.chain import Chain

from .core.molsys import MolSys
