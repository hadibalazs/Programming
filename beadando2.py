def elofordulas(a,b):
    db=0
    while True:
        idx=a.find(b)
        if idx>=0:
            db+=1
        else:
            break      #return False
        a=a[idx+1:]

    return db


def main():
    a="fekete kék zöld kék piros kék sárga"
    b="kék"
    print(elofordulas(a,b))


main()
