def NWD(x,y):

    while y!=0 :
        z=x%y
        x=y
        y=z
    return x


def NWW(a,b):
    return (a*b)//NWD(a,b)