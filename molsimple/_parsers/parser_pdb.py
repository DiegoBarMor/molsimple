# //////////////////////////////////////////////////////////////////////////////
class ParserPDB:
    LENGTH_RECORD: int = 80

    PDB_IDX_START: dict[str, int] = dict(
        SERIAL_NUM = 6,
        ATOM_NAME = 12,
        ALTLOC = 16,
        RESIDUE_NAME = 17,
        CHAIN_ID = 21,
        RESIDUE_SEQUENCE_NUM = 22,
        RESIDUE_INSERTION_CODE = 26,
        X_COORDINATES = 30,
        Y_COORDINATES = 38,
        Z_COORDINATES = 46,
        OCCUPANCY = 54,
        TEMPERATURE_FACTOR = 60,
        SEGMENT_ID = 72,
        ELEMENT_SYMBOL = 76,
        CHARGE = 78,
    )
    PDB_IDX_END: dict[str, int] = dict(
        SERIAL_NUM = 11,
        ATOM_NAME = 16,
        ALTLOC = 17,
        RESIDUE_NAME = 20,
        CHAIN_ID = 22,
        RESIDUE_SEQUENCE_NUM = 26,
        RESIDUE_INSERTION_CODE = 27,
        X_COORDINATES = 38,
        Y_COORDINATES = 46,
        Z_COORDINATES = 54,
        OCCUPANCY = 60,
        TEMPERATURE_FACTOR = 66,
        SEGMENT_ID = 76,
        ELEMENT_SYMBOL = 78,
        CHARGE = 80,
    )

    # --------------------------------------------------------------------------
    @classmethod
    def get_idx(cls, pdb_row: str) -> int:
        return cls._safe_int(
            cls._get_pdb_section(pdb_row, "SERIAL_NUM")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_name(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "ATOM_NAME")

    # --------------------------------------------------------------------------
    @classmethod
    def get_altloc(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "ALTLOC")

    # --------------------------------------------------------------------------
    @classmethod
    def get_resname(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "RESIDUE_NAME")

    # --------------------------------------------------------------------------
    @classmethod
    def get_chainid(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "CHAIN_ID")

    # --------------------------------------------------------------------------
    @classmethod
    def get_resid(cls, pdb_row: str) -> int:
        return cls._safe_int(
            cls._get_pdb_section(pdb_row, "RESIDUE_SEQUENCE_NUM")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_inscode(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "RESIDUE_INSERTION_CODE")

    # --------------------------------------------------------------------------
    @classmethod
    def get_xpos(cls, pdb_row: str) -> float:
        return cls._safe_float(
            cls._get_pdb_section(pdb_row, "X_COORDINATES")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_ypos(cls, pdb_row: str) -> float:
        return cls._safe_float(
            cls._get_pdb_section(pdb_row, "Y_COORDINATES")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_zpos(cls, pdb_row: str) -> float:
        return cls._safe_float(
            cls._get_pdb_section(pdb_row, "Z_COORDINATES")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_occ(cls, pdb_row: str) -> float:
        return cls._safe_float(
            cls._get_pdb_section(pdb_row, "OCCUPANCY")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_beta(cls, pdb_row: str) -> float:
        return cls._safe_float(
            cls._get_pdb_section(pdb_row, "TEMPERATURE_FACTOR")
        )

    # --------------------------------------------------------------------------
    @classmethod
    def get_segid(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "SEGMENT_ID")

    # --------------------------------------------------------------------------
    @classmethod
    def get_element(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "ELEMENT_SYMBOL")

    # --------------------------------------------------------------------------
    @classmethod
    def get_charge(cls, pdb_row: str) -> str:
        return cls._get_pdb_section(pdb_row, "CHARGE")

    # --------------------------------------------------------------------------
    @classmethod
    def _get_pdb_section(cls, pdb_row: str, key: str) -> str:
        return pdb_row[
            cls.PDB_IDX_START[key]:cls.PDB_IDX_END[key]
        ].strip()

    # --------------------------------------------------------------------------
    @staticmethod
    def _safe_int(s: str) -> int:
        try: return int(s)
        except ValueError: return 0

    # --------------------------------------------------------------------------
    @staticmethod
    def _safe_float(s: str) -> float:
        try: return float(s)
        except ValueError: return 0.0


# //////////////////////////////////////////////////////////////////////////////
