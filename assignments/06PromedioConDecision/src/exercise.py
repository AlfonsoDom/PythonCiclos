def main():
    #escribe tu código abajo de esta línea
tot=0
prom=0
for i in range(5000):
    promedio=float(input())
    if promedio>=0:
        prom= 1+prom
        tot= promedio+tot
    
    if promedio<0:
        print(tot/prom)
        break

if __name__=='__main__':
    main()
