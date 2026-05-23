import sys
import molsimple as ms

pdb = ms.System(sys.argv[1])
print(pdb)

for pgroup in pdb.models[:3]:
    print("----------------")
    print(pgroup)
    print(*pgroup.particles[:5], sep="\n")
