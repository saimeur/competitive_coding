t = int(input())
for i in range(t):
    line= input().split(":")
    h,m = line
    h = int(h)
    if h==12:
        print(str(h)+":"+ m+" PM")
    elif 9<h<12:
        print(str(h)+":"+ m+" AM")
    elif 0<h<10:
        print("0"+str(h)+":"+ m+" AM")
    elif h==0:
        print("12"+":"+m+" AM")
    elif h<22:
        print("0"+str(h-12)+":"+ m+" PM")
    else:
        print(str(h-12)+":"+ m+" PM")
