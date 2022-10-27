# Py(thon)lha

Projeto desenvolvido durante a matéria de Estrutura de Dados com fins educacionais para o aprendizado de Nodes e Stacks em Python.

## Node:
A classe Node possuí dois atributos, um referente ao seu "valor" (self.data), que armazena um valor qualquer para ser atribuído à esse nó e, o outro atributo (self.next), que armazena o "valor" do próximo nó na pilha.

O único método que essa classe possuí é o método de inicialização, o método "init", que é utilizado quanto instânciamos um novo objeto do tipo Node. Ao instanciarmos esse objeto passamos o parâmetro "data" que será armazenado no atributo "self.data" da classe.

Esse atributo é responsável por armazenar o "valor" desse Node, podendo esse valor ser de qualquer tipo. O atributo "self.next" é responsável por fazer um "apontamento" para o próximo Node da Stack (pilha), armazenando o "self.data" do próximo Node.

````python
class Node:
def __init__(self, data):
    self.data = data
    self.next = None
````

## Stack:
A classe Stack é a classe da pilha, é nela em que estão todos os métodos utilizados para fazer o gerenciamento da Stack.

* __init__: Método responsável pela inicialização da Stack, diferentemente do Node, essa classe não precisa de nenhum parâmetro para sua inicialização. É nele em que são definidos o atributo "self.top" que é responsável por armazenar o elemento que está no topo da pilha e, o atributo "self._size" que é responsável por armazenar a quantidade de elementos na pilha

* __push__: Método responsável por inserir um novo elemento na pilha. O parâmetro "elem" passado ao chamar esse método é utilizado para inicializar um novo Node, que por sua vez é adicionado na pilha.

* __pop__: Método responsável por remover um elemento do topo da pilha e retorná-lo ao usuário. Esse método não necessita de parâmetros para ser utilizado. Caso a pilha esteja vazia, retorna um erro informando o fato.

* __peek__: Método parecido com o __pop__, porém, ao invés de remover um elemento da fila e retorná-lo ao usuário, apenas o retorna sem removê-lo da fila.

* __len__*: Método responsável por retornar a quantidade de itens de um objeto, para que ela possa ser usada na pilha como é utilizada normalmente. Sem a reescrita utilizaríamos a função como:


    ````python
    qtd_elem = pilha.len()
    ````
    ao invés de:
    ````python
    qtd_elem = len(pilha)
    ````

* __repr__*: Método responsável por retornar uma representação imprimível do objeto Stack

<sub>* Magic Methods: Também conhecidos como Special Methods ou Dunder methods, são métodos que utilizamops para reescrever métodos nativos do Python e darmos nossa própria funcionalidade quando forem chamados e receberem a Stack como parâmetro. Por exemplo, não seria possível utilizar a função ````len()```` para retornar a quantidade de elementos da Stack já que ela não funciona como um array.<sub>


````python
from Node import Node

class Stack:
def __init__(self):
    self.top = None
    self._size = 0

def push(self, elem):
    node = Node(elem)
    node.next = self.top
    self.top = node
    self._size = self._size + 1

def pop(self):
    if self._size > 0:
        node = self.top
        self.top = self.top.next
        self._size = self._size - 1
        return node.data
    raise IndexError("The stack is empty")

def peek(self):
    if self._size > 0:
        return self.top.data
    raise IndexError("The stack is empty")

def __len__(self):
    return self._size

def __repr__(self):
    r = ""
    pointer = self.top
    while(pointer):
        r = r + str(pointer.data) + " | "
        pointer = pointer.next
    return r
````