def main():
    #escribe tu código abajo de esta línea
num=0
for i in range(1000000):
    n=input()
    if n=='A':
        print('120')
        num=num+120
    elif n=='B':
        print('250')
        num=num+250
    elif n=='C':
        print('360')
        num=num+360
    elif n=='X':
        print(num)
        break
if __name__=='__main__':
    main()
