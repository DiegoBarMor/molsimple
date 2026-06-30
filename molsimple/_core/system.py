from pathlib import Path

import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class System:
    def __init__(self, models: list[ms.ParticleGroup]|None = None):

        self.models: list[ms.ParticleGroup] # store all the models found inside the PDB file
        self.particles: ms.ParticleGroup # points to the current model
        self._idx_current_model: int = 0 # for display purposes

        self.models = [m for m in models] if models else [ms.ParticleGroup([])]
        self.particles = self.models[0]


    # --------------------------------------------------------------------------
    def __repr__(self):
        return f"System({len(self.models)} models (current: model #{self._idx_current_model} with {len(self.particles)} particles))"


    # --------------------------------------------------------------------------
    def __len__(self):
        return len(self.particles)


    # --------------------------------------------------------------------------
    def __iter__(self):
        return iter(self.particles)


    # --------------------------------------------------------------------------
    @classmethod
    def from_pdb_string(cls, raw_pdb: str) -> "System":
        obj = cls()
        obj.models = list(obj._iter_parse_models(raw_pdb))
        if not obj.models:
            raise ValueError(f"No particles found in the PBD string.")

        obj.particles = obj.models[0]
        return obj


    # --------------------------------------------------------------------------
    @classmethod
    def read_pdb(cls, path_pdb: Path|str) -> "System":
        path_pdb = Path(path_pdb)
        if not path_pdb.is_file():
            raise ValueError(f"Path '{path_pdb}' isn't a file.")

        return cls.from_pdb_string(raw_pdb = path_pdb.read_text())


    # --------------------------------------------------------------------------
    def switch_model(self, idx_model: int):
        if idx_model < 0 or idx_model >= len(self.models):
            raise ValueError(f"Invalid model index {idx_model} (must be between 0 and {len(self.models)-1}).")
        self._idx_current_model = idx_model
        self.particles = self.models[idx_model]


    # --------------------------------------------------------------------------
    def _iter_parse_models(self, raw_pdb: str):
        def _extract_next_model() -> tuple[int, str]:
            idx_0 = buffer.find("\nMODEL")
            if idx_0 == -1: return -1, buffer

            idx_1 = buffer.find("\nENDMDL", idx_0)
            if idx_1 == -1: return -1, buffer[idx_0:]

            idx_1 += len("\nENDMDL")
            return idx_1, buffer[idx_0:idx_1]

        buffer = '\n' + raw_pdb
        while buffer:
            idx, raw_model = _extract_next_model()
            pg = ms.ParticleGroup.parse_pdb(raw_model)
            if not pg.is_empty(): yield pg
            if idx == -1: break
            buffer = buffer[idx:]


# //////////////////////////////////////////////////////////////////////////////
