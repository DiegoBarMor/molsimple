import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class ParticleGroup:
    def __init__(self):
        self.particles: list[ms.Particle] = []


    # --------------------------------------------------------------------------
    @classmethod
    def from_pdb(cls, data_pdb: str) -> "ParticleGroup":
        obj = cls()
        obj.particles = [
            ms.Particle(line) for line in data_pdb.splitlines()
            if line.startswith("ATOM") or line.startswith("HETATM")
        ]
        return obj


# //////////////////////////////////////////////////////////////////////////////
