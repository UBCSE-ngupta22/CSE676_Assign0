# a=[9,8,8,7,6,5,4,5,3,4,5,6,7,8]
curr_max = 0  # Initialize curr_max to 0
lar = float('inf')  # Initialize lar to positive infinity

while True:
    inp = int(input())
    
    if inp == 0:
        break
    
    if inp <= lar:
        lar = inp
        count = 0
    else:
        count += 1
        curr_max = max(curr_max, count)
        lar = inp
    
    if curr_max == 4:
        break

print("Breaking the loop. curr_max reached 4.")
