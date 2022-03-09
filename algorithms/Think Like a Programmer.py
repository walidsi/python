import sys

for i in range(5):
    for j in range(5-i):
        sys.stdout.write('#')
    sys.stdout.write("\n")
    
sys.stdout.write("\n")

for i in range(1, 8):
    for j in range(4 - abs(4 - i)):
        sys.stdout.write('#')
    sys.stdout.write("\n")

