"""1. Declarați o listă care conține următoarele elemente: [‘abc’,123,’1’,1].
- afișarea tipului fiecărui element din lista
- Aflarea numărului numerelor întregi, numerelor float, respectiv a șirurilor din lista"""
"""count=0
count1=0
count2=0
lista1=['abc',123,'1',1.5]
for i in lista1:
    tip=str(type(i))
    print(f"Tipul elementului este :{tip[8:]}\b\b")
    if tip=="<class 'str'>":
        count = count + 1
    if tip == "<class 'int'>":
        count1 = count1 + 1
    if tip == "<class 'float'>":
        count2=count2+1
print(f"Avem {count} elemente de str")
print(f"Avem {count1} elemente de int")
print(f"Avem {count2} elemente de int")"""








""""2. Luati ca input un sir de la utilizator. Transformați șirul într-o lista și numarati vocalele din
aceasta. Afisati numarul vocalelor pe consola.
Introduceti un cuvant: Ananas
Vocale in cuvantul dvs: 3"""

"""count=0
sir1=input("Spune si tu ceva: ")
print(list(sir1))
vocale=['a','e','i','o','u']
for i in list(sir1):
    if i.lower() in vocale:
        count=count+1
print(f"Nr de vocale este :{count}")"""






"""3. Se cere un script pentru noii vecini într-un cartier. Scriptul:
- Cere input cu ce provider de Internet dorește utilizatorul. Providerii disponibili
sunt: A-Mobile, S5Net, TeleNet. Dacă opțiunea utilizatorului nu se afla in lista,
afișați “Utilizatorul nu este disponibil, va rog să alegeți altul.
- Dupa ce utilizatorul a ales un provider valid, se cere tipul de abonament dorit.
Optiunile valide sunt: 500Mbit/s, 1Gb/s, 350Mb/s. Daca utilizatorul nu introduce o
optiune valida, se cere din nou pana cand acesta alege una valida.
- La final se afiseaza mesajul: “Cererea a fost inregistrata. Va multumim.”
Lista de provideri este: ['A-Mobile', 'S5Net', 'TeleNet']
Introduceti providerul ales: S5
Nu ati introdus un provider valid. Va rugam sa incercati din nou.
Lista de provideri este: ['A-Mobile', 'S5Net', 'TeleNet']
Introduceti providerul ales: S5Net
Multumim.
Alegeti un abonament: ['500', '1', '350']
Introduceti abonamentul ales: 5003
Nu ati introdus un abonament valid. Va rugam sa incercati din
nou.
Alegeti un abonament: ['500', '1', '350']
Introduceti abonamentul ales: 500
Multumim. Cererea a fost inregistrata."""


"""lista1=['A-Mobile', 'S5Net', 'TeleNet']
Abonament=['500', '1', '350']
while True:
    U=input("Alege tipul de provider din lista(daca doriti sa iesiti apasati tasta q)")
    if U=="q":
        break
    if U in lista1:
        while True:
            if input("Alege abonamentul dorit") in Abonament:
                print("Cererea a fost inregistrata. Va multumim")
                break
            else:
                print("Incercati din nou")
    else:
        print("Utilizatorul nu este disponibil, va rog să alegeți altul")"""







