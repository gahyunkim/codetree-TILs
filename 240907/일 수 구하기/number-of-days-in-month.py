mon=int(input())

if (mon<=7 and mon%2!=0) or (mon>=8 and mon%2==0):
    print("31")
elif (mon<=6 and mon%2==0) or mon==11:
    if mon ==2:
        print("28")
    else:
        print("30")