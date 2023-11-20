### Construct the Burrows-Wheeler transform of a string ###

def BWT(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    rotations.sort()
    bwt = ''.join(rotation[-1] for rotation in rotations)
    return bwt

if __name__ == '__main__':
    string = open('C:/Users/moveo/Downloads/rosalind_ba9i.txt').readline().rstrip()
    print(BWT(string))