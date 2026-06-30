import sys
import molsimple as ms

# pdb = ms.System()
pdb = ms.System.read_pdb(sys.argv[1])

print(pdb)

for pgroup in pdb.models[:3]:
    print("----------------")
    print(pgroup)
    print(*pgroup.select_idx(1,2,5).particles, sep="\n")
