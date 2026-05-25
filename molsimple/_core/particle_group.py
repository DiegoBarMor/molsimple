from pathlib import Path

import molsimple as ms

# //////////////////////////////////////////////////////////////////////////////
class ParticleGroup:
    def __init__(self, particles: tuple[ms.Particle]):
        self.particles: list[ms.Particle] = list(particles)

    # --------------------------------------------------------------------------
    def __repr__(self):
        return f"ParticleGroup({len(self.particles)} particles)"

    # --------------------------------------------------------------------------
    def __len__(self):
        return len(self.particles)

    # --------------------------------------------------------------------------
    def __iter__(self):
        return iter(self.particles)

    # --------------------------------------------------------------------------
    @classmethod
    def parse_pdb(cls, data_pdb: str = ""):
        return cls((
            ms.Particle(line) for line in data_pdb.splitlines()
            if line.startswith("ATOM") or line.startswith("HETATM")
        ))

    # --------------------------------------------------------------------------
    def is_empty(self) -> bool:
        return len(self.particles) == 0

    # --------------------------------------------------------------------------
    def select_idx(self, *idxs: int) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.idx in idxs)

    # --------------------------------------------------------------------------
    def select_name(self, *names: str) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.name in names)

    # --------------------------------------------------------------------------
    def select_resname(self, *resnames: str) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.resname in resnames)

    # --------------------------------------------------------------------------
    def select_chainid(self, *chainids: str) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.chainid in chainids)

    # --------------------------------------------------------------------------
    def select_resid(self, *resids: int) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.resid in resids)

    # --------------------------------------------------------------------------
    def select_chain_resid(self, *chainresids: "ms.ChainResid") -> "ParticleGroup":
        selection = self.select_chainid(*(cr.chain for cr in chainresids))
        return selection.select_resid  (*(cr.resid for cr in chainresids))

    # --------------------------------------------------------------------------
    def format_pdb(self) -> str:
        return "\n".join(map(ms.Particle.format_pdb, self.particles))

    # --------------------------------------------------------------------------
    def save(self, path_pdb: str|Path):
        Path(path_pdb).write_text(
            self.format_pdb() + "\nEND"
        )


# //////////////////////////////////////////////////////////////////////////////
