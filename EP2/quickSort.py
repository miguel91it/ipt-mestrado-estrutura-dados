from linkedList import createRandomList, CircularDoublyLinkedListWithHead as linkdList

list = createRandomList(10, 10)

print(list)

def quicksort(list: linkdList):

    def inner_partition(list: linkdList, node_start, node_end):

        # print('começou com node_start: ', node_start)

        if node_start == node_end:
            return node_start
        
        pivot_prev = node_start
        curr = node_start
        pivot = node_end['key']

        temp = None

        while node_start != node_end and node_start not in [list.head, list.tail] and node_end not in [list.head, list.tail]:

            # print(node_start['key'], type(node_start['key']))
            # print(pivot, type(pivot))
            if node_start['key'] < pivot:

                pivot_prev = curr
                temp = curr['key']
                curr['key'] = node_start['key']
                node_start['key'] = temp
                curr = curr['next']

            node_start = node_start['next']

        temp = curr['key']
        curr['key'] = pivot
        node_end['key'] = temp

        return pivot_prev



    def inner_quicksort(list: linkdList, node_start, node_end):
        
        # lista vazia
        if node_start['next'] == list.tail and node_end['prev'] == list.head:

            return

        # quando tem apenas um elemento
        if node_start == node_end:

            return

        if node_start in [list.head, list.tail] or node_end in [list.head, list.tail]:
            return

        # if node_start != list.tail:
        pivot_prev = inner_partition(list, node_start, node_end)

        # print('chamou 1')
        inner_quicksort(list, node_start, pivot_prev)

        if pivot_prev == node_start: # and pivot_prev['next'] != list.tail:
            # print('chamou 2')
            inner_quicksort(list, pivot_prev['next'], node_end)

        elif pivot_prev != list.tail and pivot_prev['next'] != list.tail and pivot_prev['next']['next'] != list.tail:
            # print('chamou 3')
            inner_quicksort(list, pivot_prev['next']['next'], node_end)

    inner_quicksort(list, list.head['next'], list.tail['prev'])

print('list: ', list)
quicksort(list)
print('list: ', list)

# 2 2 3 9 deu erro