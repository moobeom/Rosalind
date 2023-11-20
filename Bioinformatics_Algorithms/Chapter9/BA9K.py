### Generate the last-first mapping of a string ###

def LastToFirst(bwt,idx):
    lastCol = [(i,c) for i,c in enumerate(bwt)]
    firstCol = sorted(lastCol, key=lambda x:x[1])
    f_idx = [i for (i,c) in firstCol].index(idx)
    return f_idx

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba9k (3).txt').readlines()
    string, i = lines[0].rstrip(), int(lines[1].rstrip())
    print(LastToFirst(string,i))