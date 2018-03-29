for _ in range(int(input())):
    temp = input()
    if temp != "".join(list(reversed(temp))):
        print("NO")
    else:
        if len(temp) % 2 == 0:
            print("YES EVEN")
        else:
            print("YES ODD")
