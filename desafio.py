from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf):
        super().__init__(endereco=None)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return '0001'
    @property
    def cliente(self):  
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    

class ContaCorrente(Conta):
    def __init__(self, cliente, limite=500, limite_saques=3):
        super().__init__(numero=None, cliente=cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        if valor <= self.limite and super().sacar(valor):
            return True
        return False
    
    def depositar(self, valor):
        if super().depositar(valor):
            return True
        return False
    
    def __str__(self):
        return f'Conta Corrente {self.numero} - Saldo: {self.saldo} - Limite: {self.limite} - Saques Restantes: {self.limite_saques}'  
    
    
    class Historico:
        def __init__(self):
            self.transacoes = []
        
        @property
        def transacoes(self):
            return self._transacoes
        
        def adicionar_transacao(self, transacao):
            self._transacoes.append({
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now(),
            })


    class Transacao(ABC):
        @property
        @abstractproperty
        def valor(self):
            pass

        @abstractmethod
        def registrar(self, conta):
            pass
    
    class Saque(Transacao):
        def __init__(self, valor):
            self._valor = valor

        @property
        def valor(self):
            return self._valor

        def registrar(self, conta):
            self.conta = conta
            if self.realizar():
                conta.historico.adicionar_transacao(self)
                return True
            return False


    class Deposito(Transacao):
        def __init__(self, valor):
            self._valor = valor

        @property
        def valor(self):
            return self._valor

        def registrar(self, conta):
            self.conta = conta
            if self.realizar():
                conta.historico.adicionar_transacao(self)
                return True
            return False
