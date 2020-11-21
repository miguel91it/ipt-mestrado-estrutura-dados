from math import inf
import random

class CircularDoublyLinkedListWithHead:

    def __init__(self):
        
        self.head = {
            'key': 'Head',
            'next': None,
            'prev': None,
            'min': inf,
            'max': -inf,
            'list_size': 0
        }

        self.tail = {
            'key': 'Tail',
            'next': None,
            'prev': None
        }

        self.head['next'] = self.tail
        self.head['prev'] = self.tail

        self.tail['next'] = self.head
        self.tail['prev'] = self.head

        self.nodeIterator = self.head

    def __iter__(self):
        return self

    def __next__(self):
        node = self.nodeIterator['next']

        if node == self.tail:

            self.nodeIterator = self.head

            raise StopIteration

        self.nodeIterator = node

        return node

    def add(self, key, fromBeginning=True):

        if fromBeginning:

            new_node = {
                'key': key,
                'next': self.head['next'],
                'prev': self.head
            }
            
            self.head['next'] = new_node

            new_node['next']['prev'] = new_node

            self.head['min'] = key if key < self.head['min'] else self.head['min']
            self.head['max'] = key if key > self.head['max'] else self.head['max']
            self.head['list_size'] += 1

            return 0, f'{key} added succesfuly at the beginning'

        else:

            new_node = {
                'key': key,
                'next': self.tail,
                'prev': self.tail['prev']
            }
            
            self.tail['prev'] = new_node

            new_node['prev']['next'] = new_node

            self.head['min'] = key if key < self.head['min'] else self.head['min']
            self.head['max'] = key if key > self.head['max'] else self.head['max']
            self.head['list_size'] += 1

            return 0, f'{key} added succesfuly in the end'

    def findByIndex(self, index):

        if index < 0 or index > self.head['list_size'] - 1:

            return -1, 'Index out of bounds'
        
        if self.isEmpty():

            return -1, 'Empty List'

        i = 0

        node = self.head['next']

        while i != index and node != self.tail:

            node = node['next']

            i += 1

        return node

    def find(self, key, fromBeginning=True, recursively=True):

        node = self.head if fromBeginning else self.tail

        if recursively:

            return self._findRecursively(key, node)

    def _findRecursively(self, key, node, fromBeginning=True):

        if self.isEmpty():
            return -1, 'Empty List'
        
        elif node['key'] == key:
            
            return node

        elif node == self.tail:
            return -1, f'{key} not found in list'

        else:
            return self._findRecursively(key, node['next'])

    def remove(self, key, recursively=False):

        if not recursively:

            return self._removeIteratively(key)

    def _removeIteratively(self, key):

        node = self.head['next']
        prev = self.head

        while (node != self.tail and node['key'] != key):

            prev = node
            node = node['next']

        if node == self.tail:

            return (-1, f'List doesnt have the key {key} taken')

        else:

            prev['next'] = node['next'] # o anterior do no deletado aponta para o prox do no deletado
            node['next']['prev'] = node['prev'] # prox aponta para o anterior do no deletado
            node['next'] = None # não aponta pra nada depois
            node['prev'] = None # não aponta pra nada antes

            self.head['list_size'] -= 1 # diminui um do size

            if key == self.head['min'] or key == self.head['max']:

                self._updateMinMax()

            return (0, f'Key {key} has been removed succesfully')

    def swapNodes(self, nodeA, nodeB):

        # prev = 'prev'
        # next = 'next'

        # print(f'NA-P {id(nodeA[prev])}')
        # print(f'NA-P-N {id(nodeA[prev][next])}')
        # print(f'NA-N {id(nodeA[next])}')
        # print(f'NA-N-P {id(nodeA[next][prev])}')

        # print(f'NB-P-N {id(nodeB[prev][next])}')
        # print(f'NB-P {id(nodeB[prev])}')
        # print(f'NB-N-P {id(nodeB[next][prev])}')
        # print(f'NB-N {id(nodeB[next])}')
        
        # print()

        # se são elementos vizinhos
        if nodeA['next'] == nodeB and nodeB['prev'] == nodeA:

            nodeB['prev'] = nodeA['prev']
            nodeB['prev']['next'] = nodeB
            nodeA['next'] = nodeB['next']
            nodeA['next']['prev'] = nodeA
            nodeB['next'] = nodeA
            nodeA['prev'] = nodeB

        # se não são elementos vizinhos
        else:

            tmpNodeB_prev = nodeB['prev']
            nodeB['prev'] = nodeA['prev']
            nodeB['prev']['next'] = nodeB
            tmpNodeA_next = nodeA['next']
            nodeA['next'] = nodeB['next']
            nodeA['next']['prev'] = nodeA
            nodeB['next'] = tmpNodeA_next
            nodeA['prev'] = tmpNodeB_prev
            nodeB['next']['prev'] = nodeB
            nodeA['prev']['next'] = nodeA

            # print(f'NA-P {id(nodeA[prev])}')
            # print(f'NA-P-N {id(nodeA[prev][next])}')
            # print(f'NA-N {id(nodeA[next])}')
            # print(f'NA-N-P {id(nodeA[next][prev])}')

            # print(f'NB-P-N {id(nodeB[prev][next])}')
            # print(f'NB-P {id(nodeB[prev])}')
            # print(f'NB-N-P {id(nodeB[next][prev])}')
            # print(f'NB-N {id(nodeB[next])}')

    def _updateMinMax(self):

        node = self.head['next']

        tmp_min = inf
        tmp_max = -inf
        
        while (node != self.tail):

            if node['key'] < tmp_min:
                
                tmp_min = node['key']

            if node['key'] > tmp_max:

                tmp_max = node['key']

            node = node['next']

        self.head['min'] = tmp_min
        self.head['max'] = tmp_max

    def isEmpty(self):
        return self.head['next'] == self.tail

    def printListRecursivamente(self, no):

        if self.isEmpty():
            return 'Empty List'
        
        elif no['key'] == 'Tail':
            return ''
        
        elif no == self.head:
            
            return self.printListRecursivamente(no['next'])[:-6]
        
        else: 
            return str(no['key']) + ' < - > ' + self.printListRecursivamente(no['next'])
        
    def printListIteratively(self):
        
        if self.isEmpty():
            return 'Empty List'

        node = self.head['next']
        
        s = ''

        while node != self.tail:

            s += str(node['key']) + ' < - > ' if node['next'] != self.tail else str(node['key'])

            node = node['next']

        return s

    def __str__(self):
        # return self.printListRecursivamente(self.head)
        return self.printListIteratively()

    def countingSort(self):
        
        if self.isEmpty():

            return

        counting_vector = [0 for i in range(self.head['max'] + 1)]

        # print(f'entryL: {self} | counting_vector: {counting_vector}')

        for i in self:

            k = i['key']

            counting_vector[k] += 1

        outputList = CircularDoublyLinkedListWithHead()

        # print(f'counting_vector: {counting_vector}')

        for index in range(len(counting_vector) ):

            # print(f'index: {index}')

            for n in range(counting_vector[index]):

                outputList.add(index, fromBeginning=False)


        return outputList


def createRandomList(n, max=1000):

        if n < 0:
            return Exception('Trying creating list with size < 0')

        list = CircularDoublyLinkedListWithHead()

        for i in range(n):

            list.add(random.randint(0, max))

        return list




if __name__ == "__main__":
    
    linked_l = CircularDoublyLinkedListWithHead()

    # print(linked_l.add(10))
    # print(linked_l.add(3))
    # print(linked_l.add(1))
    # print(linked_l.add(3))

    # print(linked_l.printListIteratively())

    # print(linked_l)

    # print(linked_l.countingSort())

    # for i in linked_l:
    #     print(i['key'])
        # print(f'\n\n{i['next']}\n\n')

    # myit = iter(linked_l)

    # print('\n\n', next(myit)['key'])
    # print('\n\n', next(myit)['key'])
    # print('\n\n', next(myit)['key'])

    # print('\n\n', next(myit)['key'])

    # print(linked_l.add(-2))
    # print(linked_l.add(-1))
    # print(linked_l.add(1))
    # print(linked_l.add(10))
    # print('Print: ', linked_l, '\n')
    # linked_l.swapNodes(linked_l.head['next'], linked_l.tail['prev'])
    # print('Print: ', linked_l, '\n')

    # print(linked_l.add(10))
    # print(linked_l.add(6))
    # print(linked_l.add(-2))
    # # print(linked_l.add(4, False))
    # print(linked_l.add(12, False))


    # print(linked_l.add(5))
    # print('Print: ', linked_l, '\n')
    # print(linked_l.head)
    # linked_l.swapNodes(linked_l.head['next'], linked_l.tail['prev'])
    # linked_l.swapNodes(linked_l.tail['prev'], linked_l.head['next'])
    # print('Print: ', linked_l, '\n')

    # linked_l.swapNodes(linked_l.tail['prev']['prev'], linked_l.head['next'])
    # print('Print: ', linked_l, '\n')
    # print('find by index: ', linked_l.findByIndex(4))
    # print(linked_l.head)

    # # print('Busca: ', linked_l.find(13))
    # # print('Busca: ', 'id do no encontrado: ', id(linked_l.find(10)), linked_l.find(10))

    # print(linked_l.remove(-1))
    # print(linked_l.remove(-2))
    # print(linked_l.remove(12))
    # print(linked_l.remove(5))
    # print(linked_l.remove(10))

    # print('Print: ', linked_l, '\n')

    # print(linked_l.add(12, False))
    # print(linked_l.add(-2))
    # print(linked_l.remove(8))
    # print('Print: ', linked_l, '\n')
    # print(linked_l.remove(10))
    # print('Print: ', linked_l, '\n')
    # print(linked_l.remove(5))
    # print('Print: ', linked_l, '\n')
    # print(linked_l.remove(4))
    # print('Print: ', linked_l, '\n')