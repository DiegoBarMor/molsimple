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
    def __getitem__(self, idx: int) -> ms.Particle:
        return self.particles[idx]

    # --------------------------------------------------------------------------
    def __setitem__(self, idx: int, value: ms.Particle) -> None:
        self.particles[idx] = value

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
    def format_pdb(self) -> str:
        return "\n".join(map(ms.Particle.format_pdb, self.particles))

    # --------------------------------------------------------------------------
    def save(self, path_pdb: str|Path):
        Path(path_pdb).write_text(
            self.format_pdb() + "\nEND"
        )


    ########## GETTERS
    # --------------------------------------------------------------------------
    def get_idxs(self) -> list[int]:
        return [p.idx for p in self.particles]

    # --------------------------------------------------------------------------
    def get_names(self) -> list[str]:
        return [p.name for p in self.particles]

    # --------------------------------------------------------------------------
    def get_resnames(self) -> list[str]:
        return [p.resname for p in self.particles]

    # --------------------------------------------------------------------------
    def get_chainids(self) -> list[str]:
        return [p.chainid for p in self.particles]

    # --------------------------------------------------------------------------
    def get_resids(self) -> list[int]:
        return [p.resid for p in self.particles]

    # --------------------------------------------------------------------------
    def get_chain_resids(self) -> "list[ms.ChainResid]":
        return [p.get_chain_resid() for p in self.particles]

    # --------------------------------------------------------------------------
    def get_positions(self) -> list[tuple[float, float, float]]:
        return [p.get_position() for p in self.particles]

    # --------------------------------------------------------------------------
    def get_positions_numpy(self):
        import numpy as np
        return np.array(self.get_positions())

    # --------------------------------------------------------------------------
    def get_betas(self) -> list[float]:
        return [p.beta for p in self.particles]

    # --------------------------------------------------------------------------
    def get_elements(self) -> list[str]:
        return [p.element for p in self.particles]

    # --------------------------------------------------------------------------
    def get_charges(self) -> list[str]:
        return [p.charge for p in self.particles]


    ########## SETTERS
    # --------------------------------------------------------------------------
    def set_idxs(self, idxs: list[int]) -> None:
        assert len(idxs) == len(self.particles), "Length of idxs must match the number of particles."
        for p,idx in zip(self.particles, idxs): p.idx = idx

    # --------------------------------------------------------------------------
    def set_names(self, names: list[str]) -> None:
        assert len(names) == len(self.particles), "Length of names must match the number of particles."
        for p,name in zip(self.particles, names): p.name = name

    # --------------------------------------------------------------------------
    def set_resnames(self, resnames: list[str]) -> None:
        assert len(resnames) == len(self.particles), "Length of resnames must match the number of particles."
        for p,resname in zip(self.particles, resnames): p.resname = resname

    # --------------------------------------------------------------------------
    def set_chainids(self, chainids: list[str]) -> None:
        assert len(chainids) == len(self.particles), "Length of chainids must match the number of particles."
        for p,chainid in zip(self.particles, chainids): p.chainid = chainid

    # --------------------------------------------------------------------------
    def set_resids(self, resids: list[int]) -> None:
        assert len(resids) == len(self.particles), "Length of resids must match the number of particles."
        for p,resid in zip(self.particles, resids): p.resid = resid

    # --------------------------------------------------------------------------
    def set_chain_resids(self, chain_resids: "list[ms.ChainResid]") -> None:
        assert len(chain_resids) == len(self.particles), "Length of chain_resids must match the number of particles."
        for p,chain_resid in zip(self.particles, chain_resids): p.set_chain_resid(chain_resid)

    # --------------------------------------------------------------------------
    def set_positions(self, positions: list[tuple[float, float, float]]) -> None:
        assert len(positions) == len(self.particles), "Length of positions must match the number of particles."
        for p,position in zip(self.particles, positions): p.set_position(position)

    # --------------------------------------------------------------------------
    def set_betas(self, betas: list[float]) -> None:
        assert len(betas) == len(self.particles), "Length of betas must match the number of particles."
        for p,beta in zip(self.particles, betas): p.beta = beta

    # --------------------------------------------------------------------------
    def set_elements(self, elements: list[str]) -> None:
        assert len(elements) == len(self.particles), "Length of elements must match the number of particles."
        for p,element in zip(self.particles, elements): p.element = element

    # --------------------------------------------------------------------------
    def set_charges(self, charges: list[str]) -> None:
        assert len(charges) == len(self.particles), "Length of charges must match the number of particles."
        for p,charge in zip(self.particles, charges): p.charge = charge


    ########## SELECTIONS
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
        """NOTE: `resid` alone isn't enough to define a unique residue, use `chain_resid` instead if that's the intention."""
        return ParticleGroup(p for p in self.particles if p.resid in resids)

    # --------------------------------------------------------------------------
    def select_chain_resid(self, *chainresids: "ms.ChainResid") -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.get_chain_resid() in chainresids)


    ########## SELECTIONS (FANCIER)
    # --------------------------------------------------------------------------
    def select_hydrogens(self) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if p.name.startswith("H"))

    # --------------------------------------------------------------------------
    def select_non_hydrogens(self) -> "ParticleGroup":
        return ParticleGroup(p for p in self.particles if not p.name.startswith("H"))

    # --------------------------------------------------------------------------
    def select_mask(self, mask: list[bool]) -> "ParticleGroup":
        assert len(mask) == len(self.particles), "Length of mask must match the number of particles."
        return ParticleGroup(p for p,m in zip(self.particles, mask) if m)


    ########## SPLITTERS
    # --------------------------------------------------------------------------
    def split_chains(self) -> list["ParticleGroup"]:
        chainids = sorted(set(p.chainid for p in self.particles))
        return [self.select_chainid(chainid) for chainid in chainids]


    # --------------------------------------------------------------------------
    def split_residues(self) -> list["ParticleGroup"]:
        chainresids = sorted(set(p.get_chain_resid() for p in self.particles))
        return [self.select_chain_resid(chainresid) for chainresid in chainresids]


# //////////////////////////////////////////////////////////////////////////////
