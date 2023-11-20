### Reconstruct a string from its Burrows-Wheeler transform ###

def InvBWT(bwt):
    lastCol = [(i,c) for i,c in enumerate(bwt)]
    firstCol = sorted(lastCol, key=lambda x:x[1])

    text, idx =  '', firstCol[0][0]
    for i in range(len(bwt)):
        idx,char = firstCol[idx]
        text += char
    return text



if __name__ == '__main__':
    string = open('C:/Users/moveo/Downloads/rosalind_ba9j.txt').readline().rstrip()
    print(InvBWT(string))