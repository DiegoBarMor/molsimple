import sys
import molsimple as ms

# pdb = ms.System()
pdb = ms.System(sys.argv[1])
# pdb = ms.System(models = [])
# pdb = ms.System(sys.argv[1], models = []) # should fail

print(pdb)

for pgroup in pdb.models[:3]:
    print("----------------")
    print(pgroup)
    print(*pgroup.select_idx(1,2,5).particles, sep="\n")
