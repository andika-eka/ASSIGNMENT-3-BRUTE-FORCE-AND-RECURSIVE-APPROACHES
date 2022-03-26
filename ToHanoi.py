# Recursive Python function to solve tower of hanoi
count = 0

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 6:
        global count
        count += 1
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    # print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
		
# Driver code
n = 10

TowerOfHanoi(n, 'A', 'C', 'B')
print("move : " + str(count))
# A, C, B are the name of rods

# Contributed By Harshit Agrawal
