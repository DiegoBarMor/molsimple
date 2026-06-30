
import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class Particle:
    __slots__ = (
        "hetatm", "idx", "name", "altloc", "resname", "chainid", "resid", "inscode",
        "xpos", "ypos", "zpos", "occ", "beta", "segid", "element", "charge"
    )

    # --------------------------------------------------------------------------
    def __init__(self, pdb_row: str):
        if len(pdb_row) > ms.ParserPDB.LENGTH_RECORD:
            raise ValueError(
                f"Invalid PDB row length for row '{pdb_row}': "+\
                f"{len(pdb_row)} > {ms.ParserPDB.LENGTH_RECORD}"
            )

        pdb_row = pdb_row.ljust(ms.ParserPDB.LENGTH_RECORD)
        self.hetatm:  bool  = pdb_row.startswith("HETATM")
        self.idx:     int   = ms.ParserPDB.get_idx    (pdb_row) # aka SERIAL_NUM, atomid
        self.name:    str   = ms.ParserPDB.get_name   (pdb_row) # aka ATOM_NAME
        self.altloc:  str   = ms.ParserPDB.get_altloc (pdb_row) # aka ALTLOC
        self.resname: str   = ms.ParserPDB.get_resname(pdb_row) # aka RESIDUE_NAME
        self.chainid: str   = ms.ParserPDB.get_chainid(pdb_row) # aka CHAIN_ID
        self.resid:   int   = ms.ParserPDB.get_resid  (pdb_row) # aka RESIDUE_SEQUENCE_NUM
        self.inscode: str   = ms.ParserPDB.get_inscode(pdb_row) # aka RESIDUE_INSERTION_CODE
        self.xpos:    float = ms.ParserPDB.get_xpos   (pdb_row) # aka X_COORDINATES
        self.ypos:    float = ms.ParserPDB.get_ypos   (pdb_row) # aka Y_COORDINATES
        self.zpos:    float = ms.ParserPDB.get_zpos   (pdb_row) # aka Z_COORDINATES
        self.occ:     float = ms.ParserPDB.get_occ    (pdb_row) # aka OCCUPANCY
        self.beta:    float = ms.ParserPDB.get_beta   (pdb_row) # aka TEMPERATURE_FACTOR
        self.segid:   str   = ms.ParserPDB.get_segid  (pdb_row) # aka SEGMENT_ID
        self.element: str   = ms.ParserPDB.get_element(pdb_row) # aka ELEMENT_SYMBOL
        self.charge:  str   = ms.ParserPDB.get_charge (pdb_row) # aka CHARGE

    # --------------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"Particle({self.idx:>5}:{self.name:<4} @res {self.resid:>4}:{self.resname:<3} @chain {self.chainid}; [{self.xpos},{self.ypos},{self.zpos}])"

    # --------------------------------------------------------------------------
    def format_pdb(self) -> str:
        return ''.join((
           f"{'HETATM' if self.hetatm else 'ATOM  '}{self.idx:>5} {self.name:<4}",
           f"{self.altloc:1}{self.resname:>3} {self.chainid:1}{self.resid:>4}",
           f"{self.inscode:1}   {self.xpos:8.3f}{self.ypos:8.3f}{self.zpos:8.3f}",
           f"{self.occ:6.2f}{self.beta:6.2f}      {self.segid:<4}",
           f"{self.element:>2}{self.charge:>2}"
        ))

    ########## GETTERS
    # --------------------------------------------------------------------------
    def get_position(self) -> tuple[float, float, float]:
        """Returns the position of this particle as a tuple (x, y, z)."""
        return (self.xpos, self.ypos, self.zpos)

    # --------------------------------------------------------------------------
    def get_chain_resid(self) -> "ms.ChainResid":
        """Returns a `ChainResid` object representing the chain and residue of this particle."""
        return ms.ChainResid(self.chainid, self.resid)

    ########## SETTERS
    # --------------------------------------------------------------------------
    def set_chain_resid(self, chain_resid: "ms.ChainResid") -> None:
        """Sets the chain and residue of this particle using a `ChainResid` object."""
        self.chainid = chain_resid.chain
        self.resid = chain_resid.resid

    # --------------------------------------------------------------------------
    def set_position(self, position: tuple[float, float, float]) -> None:
        """Sets the position of this particle."""
        self.xpos, self.ypos, self.zpos = position


# //////////////////////////////////////////////////////////////////////////////
