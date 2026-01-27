import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class Residue:
    def __init__(self, data: str):
        self.resname = data[ms.RESIDUE_NAME_START:ms.RESIDUE_NAME_END]
        self.residx = data[ms.RESIDUE_SEQUENCE_NUM_START:ms.RESIDUE_SEQUENCE_NUM_END]
        self.insertion = data[ms.RESIDUE_INSERTION_CODE_START:ms.RESIDUE_INSERTION_CODE_END]


# //////////////////////////////////////////////////////////////////////////////
