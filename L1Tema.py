"""1. Parola unui sistem este: Passme1n. Cereți input de la utilizator cu parola. Afișați pe
ecran un mesaj (True, False) daca aceasta este Passme1n, respectiv dacă nu este
aceasta
-------------------------------------------------------------------------------------------------------------------"""
"""ps="Passme1n"
iparola=input("Introduceti parola: ")
print(ps==iparola)"""





"""2.Cereți ca input de la utilizator 2 nume. Verificati si afisati:
- Lungimea primului nume
- Dacă cele doua nume date sunt la fel
- Dacă primul nume este mai lung decat al doilea nume
- Inițiala primului nume
- Primul nume inversat

-------------------------------------------------------------------------------------------------------------------"""
"""a=input("Introduceti primul nume: ")
b=input("Introduceti al doilea nume: ")
print(f"Lungimea primului nume este de {len(a)} litere")
print(f"Sunt cele doua nume la fel? {(a==b)}")
print(f"Primul nume este mai lung decat al doilea?{len(a)>len(b)}")
print("Initiala primului nume este: {}".format(a[0]))
print("Primul nume inversat este : {} ".format(a[::-1]))"""




"""3. Folosind codul de la exercitiul 2, mai cereți input de la utilizator cu un număr:
- Afisati primul nume multiplicat de n ori, unde n este numărul introdus de către
utilizator.
Introduceti un nume de referinta: Ana
Introduceti un alt nume: An
Lungimea numelui de referinta este: 3
Numele de referinta este acelasi cu numele dat: False
Numele de referinta este mai lung decat numele dat: True
Initiala numelui de referinta este: A
Numele de referinta inversat este: anA
Introduceti un numar: 3
AnaAnaAna

-------------------------------------------------------------------------------------------------------------------"""
"""n=int(input("Introduceti un numar: "))
print(f"Primul nume multiplicat de {n} ori este: {a*n} ")"""







"""4.4. Declarați o variabila cu șirul: “Ananas”. Afișati șirul în următoarele feluri pe ecran:
- A
n
a
n
a
s
- Ana
nas
- An:ana:s
- Ana_na_s
- nananananananana
-------------------------------------------------------------------------------------------------------------------"""
"""v="Ananas"
print(v[0],v[1],v[2],v[3],v[4],v[5],sep="\n")
print()
print(v[0:3:1],v[3:6:1],sep="\n")
print()
print(v[0:2:1],v[2:5:1],v[5:6],sep=":")
print()
print(v[0:3:1],v[3:5:1],v[5:6],sep="_")
print()
print(v[1:5:1]*4)"""


"""Suplimentar:
1. Cereți input de la utilizator cu un cuvânt. Afișați dacă acest cuvant este palindrom cu
True sau False. Găsiți o metoda pentru a valida inclusiv cazurile în care utilizatorul
introduce o literă mare, folosind una din următoarele metode:
- str.upper() - https://python-reference.readthedocs.io/en/latest/docs/str/upper.html
- str.lower() - https://python-reference.readthedocs.io/en/latest/docs/str/lower.html
"""
"""c=str.upper(input("Introduceti un cuvant"))

print(c[::])
print(c[::-1])

print(f"Este palindrom? {c[::]==c[::-1]}")"""


"""2. Cereti input de la utilizator un cuvant. Folosind metoda upper(), afisati daca prima litera
din cuvant este o majuscula.
Introduceti un sir: Alina
Sirul incepe cu o majuscula: True"""

"""abcd=input("Introduceti un sir: ")
print(abcd[0]==abcd[0].upper())"""
