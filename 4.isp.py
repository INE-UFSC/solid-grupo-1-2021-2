"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão

from abc import ABC

class IJanela(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
    
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass
"""   
#Forma de resolver: criar a interface Tamanho(métodos maximizar e minimizar) e a interface Menu(mostrar_menu e fechar)

from abc import ABC

class ITamanho(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
        
class IMenu(ABC):
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IMenu):
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(ITamanho):
    def maximizar(self):
        pass

    def minimizar(self):
        pass

