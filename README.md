# Desafio: Criando um Sistema Bancário em Python

Este projeto é uma solução para o desafio proposto pela DIO com o objetivo de desenvolver um sistema bancário simples utilizando a linguagem Python.

## Descrição do Desafio

Fomos contratados por um grande banco para desenvolver a primeira versão de seu novo sistema bancário. O sistema deve permitir:

- Depósitos
- Saques
- Visualização de extrato

A versão inicial será utilizada por apenas **um único usuário**, sem necessidade de autenticação ou identificação de conta.

---

## 🧠 Regras de Negócio

### Depósito

- Apenas valores **positivos** são aceitos.
- Todos os depósitos devem ser **armazenados** e exibidos no extrato.

### Saque

- Limite de **3 saques diários**.
- Valor máximo de **R$ 500,00 por saque**.
- Saques não podem ser realizados se o saldo for insuficiente.
- Todos os saques devem ser **armazenados** e exibidos no extrato.

### Extrato

- Deve listar **todos os depósitos e saques** realizados.
- Exibir o **saldo atual** da conta.
- Se não houver movimentações, exibir a mensagem:  
  `"Não foram realizadas movimentações."`
- Os valores devem ser exibidos no formato: `R$ xxx.xx`

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Lógica de programação estruturada
- Operações com listas e controle de fluxo

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
