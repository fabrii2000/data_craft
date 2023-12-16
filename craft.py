import random    

class Natante:
    def __init__(self, ID_natante, denominazione, tipo, posti, tassa):
        self.__natante= ID_natante
        self.__denominazione = denominazione
        self.__tipo = tipo
        self.__posti = posti
        self.__tassa = tassa
    def get_natante(self):
        return self.__natante
    def get_denominazione (self):
        return self.__denominazione
    def get_tipo(self):
        return self.__tipo
    def get_posti(self):
        return self.__posti
    def get_tassa(self):
        return self.__tassa     
    def get_dati(self):
        return self.__natante, self.__denominazione, self.__tipo, self.__posti, self.__tassa
    def __str__ (self):
        return "ID:"+ str(self.__natante) +\
               "\nDenominazione:" + str(self.__denominazione) +\
               "\ntipo:" + str(self.__tipo) +\
               "\nposti:" + str(self.__posti) +\
               "\ntassa:" + str(self.__tassa)
    
def caricamento_natanti(n_natanti):
    dic = {}
    for i in range(n_natanti):
        print(i+1)
        nat = int(input("inserire ID natante"))
        den = random.randint(5,100)
        tip = "yacht"
        pos = random.randint(6,10)
        tas = random.randint(5,100)
        tip = tip.lower()
        obj_natante = Natante(nat, den, tip, pos, tas)
        dic[nat] = obj_natante
    return dic
def high(dizionario, n_natanti):
    flag = 0
    for key in dizionario:
        nat, den, tip, pos, tas = dizionario[key].get_dati()
        if pos > 5:
            if flag == 0:
                massimo = tas
                ID_tassa = nat
                flag = 1
            if massimo < tas :
                ID_tassa = nat
                massimo = tas
    print("natante con il valore più alto di tassa")
    print("ID_natante",ID_tassa)
    print("tassa :", massimo)
def lista_yacht(dizionario):
    lista_da_ordinare = []
    print("lista da ordinare")
    for item in dizionario:
        print(dizionario[item].get_dati())
    i = 0
    for key in dizionario:
        if  dizionario[key].get_tipo() == "yacht":
            lista_da_ordinare.insert(i,dizionario[key])
            i = i + 1
    n = len(lista_da_ordinare)
    for j in range(n-2):
        for i in range(n-1-j):
            if lista_da_ordinare[i].get_tassa() > lista_da_ordinare[i+1].get_tassa():
                TEMP = lista_da_ordinare[i]
                lista_da_ordinare[i] = lista_da_ordinare[i+1]
                lista_da_ordinare[i+1] = TEMP
    print("lista ordinata :")
    for item in lista_da_ordinare:
        print(item)
    return lista_da_ordinare

def main():
    NATANTI = 4
    dic = caricamento_natanti(NATANTI)
    high(dic, NATANTI)
    lista_yacht(dic)
main()








