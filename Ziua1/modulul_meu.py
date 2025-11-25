class Factura:
    
    def __init__(self, valoare, data_scadenta):
        self.valoare = valoare
        self.data_scadenta = data_scadenta

    def __str__(self):
        return f" Factura cu valoare {self.valoare} are data scadenta {self.data_scadenta}"
    
    def pret_cu_tva(self):
        return self.valoare * 1.21

## Aceasta linie de cod se executa doar in momentul in care dau run la fisierul acesta
if __name__ == "__main__":
    f1 = Factura(100, "30-11-2025")
    print(f1)
    
        
