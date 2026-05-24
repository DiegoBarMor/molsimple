from pathlib import Path

import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class ParticleGroup:
    def __init__(self, data_pdb: str = ""):
        self.particles: list[ms.Particle] = [
            ms.Particle(line) for line in data_pdb.splitlines()
            if line.startswith("ATOM") or line.startswith("HETATM")
        ]

    # --------------------------------------------------------------------------
    def __repr__(self):
        return f"ParticleGroup({len(self.particles)} particles)"

    # --------------------------------------------------------------------------
    def __len__(self):
        return len(self.particles)

    # --------------------------------------------------------------------------
    def is_empty(self) -> bool:
        return len(self.particles) == 0

    # --------------------------------------------------------------------------
    def format_pdb(self) -> str:
        return "\n".join(map(ms.Particle.format_pdb, self.particles))

    # --------------------------------------------------------------------------
    def save(self, path_pdb: str|Path):
        Path(path_pdb).write_text(
            self.format_pdb() + "\nEND"
        )


# //////////////////////////////////////////////////////////////////////////////
