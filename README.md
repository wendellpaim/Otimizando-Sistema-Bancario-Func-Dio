# 💰 Sistema Bancário em Python

Projeto desenvolvido como parte do **Desafio de Código - Criando um Sistema Bancário** do **Bootcamp Santander Backend com Python**, promovido pela [DIO](https://www.dio.me/).

## 📌 Descrição

Este projeto simula um sistema bancário simples, utilizando **Python puro**, com suporte a múltiplos usuários e contas. Ele permite **operações de depósito, saque e extrato**, além de funcionalidades adicionais como **cadastro de usuários**, **criação de contas vinculadas por CPF** e **listagem de contas registradas**.

---

## 🛠️ Funcionalidades

- [x] **Cadastro de Usuário**: Registra o CPF, nome, endereço e data de nascimento.
- [x] **Criação de Conta Bancária**:
  - Vinculada a um usuário existente via CPF.
  - Cada conta possui agência, número e senha.
- [x] **Depósito**: Permite adicionar saldo à conta, desde que o valor seja positivo.
- [x] **Saque**:
  - Limite diário de **3 saques**;
  - Cada saque limitado a **R$ 500,00**;
  - Só é possível sacar se houver saldo suficiente.
- [x] **Extrato**: Mostra o histórico de transações da conta (depósitos e saques).
- [x] **Listagem de Contas**: Exibe todas as contas cadastradas e os usuários correspondentes.
- [x] **Sair**: Encerra o programa com uma mensagem de agradecimento.

---

## 💻 Tecnologias Utilizadas

- Python 3

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python** instalado.
2. Clone este repositório ou copie o código-fonte.
3. Salve o arquivo como `sistema_bancario.py`.
4. Execute no terminal com:

```bash
python sistema_bancario.py
