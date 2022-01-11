from classes import Recipiente, Copo

if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    rec = Recipiente(100)
    print(rec)
    print(rec.esta_limpo())
    rec.sujar()
    print(rec.esta_limpo())
    rec.lavar()
    print(rec.esta_limpo(),"\n")

    cup = Copo(300)
    print(cup)
    cup.encher('cerveja')
    print(cup)
    cup.beber(180)
    print(cup)
    cup.lavar()
    print(cup)
