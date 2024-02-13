# 9, 8, 7, 6, 5, 4, 8, 6, 5, 3, 2 ,1
dum = float('inf')
max_con = 0
cnt = 0

while True:

    inp = int(input())
    if inp < dum:
        dum = inp  # 9, 8,7,6,5,4
        cnt = 0 # 
    else:
        cnt += 1
        max_con = max(max_con, cnt)
        if max_con == 3:
            print("dum= ",dum)
            break

print("Max_con=  ",max_con)
