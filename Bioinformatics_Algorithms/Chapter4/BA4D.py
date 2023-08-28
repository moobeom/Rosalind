### Compute the number of peptides of given total mass ###

def NumPeptides(m):
    masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    arr = [0]*(m +1)
    arr[m] = 1
    while m > 0:
        for mass in masses:
            arr[m - mass] += arr[m]
        m -= 1
        while arr[m] == 0:
            m -= 1
    return arr[0]

print(NumPeptides(1448))