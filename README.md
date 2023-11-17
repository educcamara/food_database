# Gerenciador de Alimentos

Este script em Python 3.11 é um gerenciador simples de alimentos. 
Ele permite a criação, edição, visualização e exclusão de alimentos, 
com os dados armazenados em um arquivo binário usando a biblioteca `pickle`.

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Armazenamento de Dados](#armazenamento-de-dados)

## Visão Geral

Este script foi desenvolvido como um projeto de estudo de Python, para me introduzir ao uso de banco de dados.
O objetivo do programa é ser capaz de guardar dados como a quantidade de proteínas, carboidratos, gorduras e fibras de um alimentos (por enquanto apenas esses dados),
para que, eventualmente, seja um programa útil para quem deseja controlar a sua dieta.

## Funcionalidades Principais

1. Visualizar Lista de Alimentos

- **Comando:** 1
- **Descrição:** Mostra uma lista detalhada de todos os alimentos armazenados.

2. Visualizar Lista Compacta de Alimentos

- **Comando:** 1.1
- **Descrição:** Mostra uma lista compacta com informações sobre os alimentos.

3. Adicionar Novo Alimento

- **Comando:** 2
- **Descrição:** Permite a adição de um novo alimento ao sistema, fornecendo detalhes como nome, medidas totais, proteínas, carboidratos, gorduras e fibras.

4. Editar Informações de Alimento Existente

- **Comando:** 3
- **Descrição:** Permite a edição das informações de um alimento existente. O usuário é solicitado a fornecer o nome do alimento e o atributo a ser editado com o novo valor.

5. Remover Alimento

- **Comando:** 4
- **Descrição:** Remove um alimento do sistema. O usuário deve fornecer o nome do alimento a ser removido.

## Armazenamento de Dados

Os dados dos alimentos são armazenados no arquivo `food_list`. 
Ao sair do programa ('q' como comando), os dados são salvos nesse arquivo por meio do `pickle` para serem recuperados na próxima execução.

```python
import pickle
from food import Food
...

# em main()
try:
    with open("food_list", "rb") as file: # rb = read binary
        food_list: [Food] = pickle.load(file) # carrega a lista de classe Food do arquivo
except (EOFError, FileNotFoundError): 
    food_list: [Food] = [] # se o arquivo não existir ou estiver vazio, cria uma lista vazia

...
while True: # loop principal
    ...
    if command_input.lower() == 'q':
        with open("food_list", "wb") as file: # wb = write binary
            pickle.dump(food_list, file) # salva a lista de classe Food no arquivo
        print("Saindo do programa...")
        break
    ...
```