electrons = int(input())
enough_electrons = True
atom_shells = []
shell = 1

while enough_electrons:
    electrons_needed = 2 * shell**2
    if electrons_needed > electrons:
        enough_electrons = False
        atom_shells.append(electrons)
        break
    atom_shells.append(electrons_needed)
    electrons -= electrons_needed
    shell += 1

print(atom_shells)
