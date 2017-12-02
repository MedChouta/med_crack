from hashlib import *
import sys, time

if len(sys.argv) < 3:
    print "\nUsage: med_crack.py [Hash_File] [Dictionary] [Algorithm]\n"
    sys.exit()

try:
    hash_file = open(sys.argv[1], "r")
    dictionary = open(sys.argv[2], "r")
except:
    print "No such files\n"

Algorithms = {
            'md5': md5,
            'sha1': sha1,
            'sha224': sha224,
            'sha256': sha256,
            'sha384': sha384,
            'sha512': sha512
             }

def crack(hash_file, dictionary, alg):
    for line in hash_file:
        crackingString = "Cracking {}".format(line)
        print crackingString + (len(crackingString)-1)*"-"
        for line2 in dictionary:
            print "Testing: '"+line2.rstrip()+"'"
            if  line.rstrip() == alg(line2.rstrip()).hexdigest():
                print "MATCH FOUND: " + line.rstrip() + " == " + line2
                dictionary.seek(0)
                break
            else:
                print "no match found\n"
        dictionary.seek(0)
start = time.time()
try:
    crack(hash_file, dictionary, Algorithms[sys.argv[3]])
except:
    print sys.exc_info()[0]
    print "Supported algorithms: \nmd5\nsha1\nsha224\nsha256\nsha384\nsha512"
end = time.time()
elapsedTime = end - start

print "Elapsed time: "+str(elapsedTime)+"s"

hash_file.close()
dictionary.close()
