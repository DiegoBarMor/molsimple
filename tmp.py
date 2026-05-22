from pathlib import Path
import molsimple as ms

pg = ms.ParticleGroup.from_pdb(
    Path("testdata/ade.pdb").read_text()
)
print(*pg.particles[:15], sep="\n")
