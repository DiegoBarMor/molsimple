import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class ChainResid:
    def __init__(self, chain: str, resid: str):
        """Represents a combination of chain ID and residue ID, which can be used to identify a specific **unique** residue in a PDB file."""
        self.chain: str = str(chain)
        self.resid: int = int(resid)


    # --------------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"ChainResid({self.get_dotstr()})"


    # --------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            other = ChainResid.from_dotstr(other)
        if not isinstance(other, ChainResid):
            raise TypeError(f"Cannot compare ChainResid with {type(other)}.")
        return self.chain == other.chain and self.resid == other.resid


    # --------------------------------------------------------------------------
    @classmethod
    def from_dotstr(cls, dotstr: str) -> "ChainResid":
        """Parses a string in the format `chainid.resid`."""
        parts = dotstr.split(".")
        if len(parts) != 2:
            raise ValueError(f"Invalid format for ChainResid: {dotstr}. Expected format: `chainid.resid`.")
        chain, resid = parts
        return cls(chain, resid)


    # --------------------------------------------------------------------------
    def get_dotstr(self) -> str:
        """Returns a string in the format `chainid.resid`."""
        return f"{self.chain}.{self.resid}"


# //////////////////////////////////////////////////////////////////////////////
