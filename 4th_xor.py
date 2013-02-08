import sys

def multixor(data,key):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(data,key))

if __name__ == "__main__":
    try:
        fname = sys.argv[1]
    except:
        print "Specify filename"
        quit()
        
    amendment = """The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."""
    
    data = open(fname, 'rb').read()
    enc = multixor(data, amendment)
    open(fname + ".4th", 'wb').write(enc)
    
