import ipaddress

class EndIPv4:
    def __init__(self, oct1=0, oct2=0, oct3=0, oct4=0, prefixo=0):
        self._oct1 = oct1
        self._oct2 = oct2
        self._oct3 = oct3
        self._oct4 = oct4 
        self._prefixo = prefixo
        self._classe = ""

    #getters
    def oct1(self):
        return self._oct1
    def oct2(self):
        return self._oct2
    def oct3(self):
        return self._oct3
    def oct4(self):
        return self._oct4
    def prefixo(self):
        return self._prefixo
    def classe(self):
        return self._classe
    
    #setters
    def oct1(self, value):
        if 0 <= value <= 255:
            self._oct1 = value
        else:
            raise ValueError("O octeto deve ser entre 0 e 255")
        
    def oct2(self, value):
        if 0 <= value <= 255:
            self._oct2 = value
        else:
            raise ValueError("O octeto deve ser entre 0 e 255")
    
    def oct3(self, value):
        if 0 <= value <= 255:
            self._oct3 = value
        else:
            raise ValueError("O octeto deve ser entre 0 e 255")
    
    def oct4(self, value):
        if 0 <= value <= 255:
            self._oct4 = value
        else:
            raise ValueError("O octeto deve ser entre 0 e 255")
        
    def prefixo(self, value):
        if 0 <= value <= 32:
            self._prefixo = value
        else:
            print("O prefixo deve estar entre 0 e 32, insira novo: ")

        while value < 0 or 
        


    def GetClass():
        primeiro_octeto = EndIPv4.oct1
        if primeiro_octeto >= 1 and primeiro_octeto <= 126:
            return "Classe A"
        elif primeiro_octeto >= 128 and primeiro_octeto <= 191:
            return "Classe B"
        elif primeiro_octeto >= 192 and primeiro_octeto <= 223:
            return "Classe C"
        elif primeiro_octeto >= 224 and primeiro_octeto <= 239:
            return "Classe D"
        elif primeiro_octeto >= 240 and primeiro_octeto <= 255:
            EndIPv4.
            return "Classe E"
        else:
            return "Endereço inválido"

        
#sets de teste
EndIPv4.oct1 = 257
EndIPv4.oct2 = 168
EndIPv4.oct3 = 1
EndIPv4.oct4 = 1
EndIPv4.prefixo = 24
print (EndIPv4.GetClass())
#print(EndIPv4.oct1) #debug
#print(EndIPv4.oct2) #debug
#print(EndIPv4.oct3) #debug
#print(EndIPv4.oct4) #debug
#print(EndIPv4.prefixo) #debug
    


class DHCP:
    x = 5