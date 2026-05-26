from pathlib import Path

import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class System:
    def __init__(self, path_pdb: Path|str = None, models: list[ms.ParticleGroup] = None):
        if path_pdb is None:
            if models is None: models = []
        elif models is not None:
            raise ValueError("System constructor requires either a path to a PDB file or a list of ParticleGroup models, but not both.")

        self.models: list[ms.ParticleGroup] # store all the models found inside the PDB file
        self.particles: ms.ParticleGroup # points to the current model
        self._idx_current_model: int = 0 # for display purposes

        self.models = self._parse_pdb(path_pdb) \
            if (path_pdb is not None) else models.copy()

        if not self.models:
            self.models.append(ms.ParticleGroup([]))

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
    def switch_model(self, idx_model: int):
        if idx_model < 0 or idx_model >= len(self.models):
            raise ValueError(f"Invalid model index {idx_model} (must be between 0 and {len(self.models)-1}).")
        self._idx_current_model = idx_model
        self.particles = self.models[idx_model]


    # --------------------------------------------------------------------------
    def _parse_pdb(self, path_pdb: Path|str) -> list[ms.ParticleGroup]:
        path_pdb = Path(path_pdb)
        if not path_pdb.is_file():
            raise ValueError(f"Path '{path_pdb}' isn't a file.")

        raw_pdb = path_pdb.read_text()
        models = list(self._iter_parse_models(raw_pdb))
        if not models:
            raise ValueError(f"No particles found in the '{path_pdb}' file. Make sure it's a PDB file.")

        return models


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
