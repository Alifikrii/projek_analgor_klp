import random

afile = open("Random10^6ke3.txt", "w" )

try:
    for i in range(1000000):
        line = str(random.randint(1, 100))
        afile.write(line)
        afile.write("\n")
        print(line)
except ValueError:
    # error handling

    afile.close()