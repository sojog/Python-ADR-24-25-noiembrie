## poo -> programare orientata obiect
## oop -> object oriented programming

## CONVENTIE -> numele clasei sa inceapa cu litera mare

## Definirea unei clase (sablon)
class Document:

    ## functie speciala -> initializator (un fel de constructor)
    ## functiile cu "__" se numesc functii magice (private)
    ## self -> este referinta catre obiectul curent (echivalentului this)
    def __init__(self, titlu = "Scrisoare de intentie", semnatar = "necunoscut"):
        # ## atribut (variabila a clasei)
        self.titlu = titlu
        self.semnatar = semnatar

    # functia de conversie a obiect la string
    def __str__(self):
        return f"{self.titlu} semnata de {self.semnatar}"


## Obiect este o instanta (concretizare)
obiect1 = Document("Scrisoare de recomandare", "fostul sef")
print(obiect1)

## Obiect este o instanta (concretizare)
obiect2 = Document("Scrisoare de dragoste")
print(obiect2)

obiect3 = Document()
print(obiect3)


