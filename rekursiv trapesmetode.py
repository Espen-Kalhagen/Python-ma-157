import math


def function(x):
    return math.exp(-x**2)

def trapesMetode(f,a,b,Igammel,k):
    if k == 1:
        I = (a-b/2)*(f(a)+f(b))
    else:
        N=2**(k-2)
        h=(b-a)/N
        x=a+h/2

        sum = 0.0
        for i in range(int(N)):
            sum+=f(x)
            x=x+h
        I = Igammel/2+(h*sum)/2
    return I



Inew =0
antallIterasjoner=1
i=0
Ep =0
while True:
    i=i+1
    Iold = Inew
    Inew = trapesMetode(function,0,2,Inew,i)
    try:
        Ep = abs((Inew-Iold)/Inew)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    if(Ep!=0 and Ep<= 10e-3):
        break


print("Ferdig, I=",Inew, "Antall iterasjoner=",i,"Feil prosent:",Ep*100)

