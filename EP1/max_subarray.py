from max_subarray_crossing_middle import max_subarray_crossing_middle
from json import load

def max_subarray(array, start, end):
    
    if len(array) <= 0:
        
        return -1, -1, -1

    if start == end:

        return 0, 0, array[0]

    else:

        middle = (start + end) // 2

        startLeft, endLeft, sumLeft = max_subarray(array, start, middle)

        startRight, endRight, sumRight = max_subarray(array, middle + 1, end)

        startCross, endCross, sumCross = max_subarray_crossing_middle(array, start, end, middle)

        if sumLeft >= sumRight and sumLeft >= sumCross:

            return startLeft, endLeft, sumLeft

        elif sumRight >= sumLeft and sumRight >= sumCross:

            return startRight, endRight, sumRight

        else:

            return startCross, endCross, sumCross

if __name__ == '__main__':

    with open("inputs.json", "r") as input:


        arrays = load(input)['inputs']

    i = 1

    for array in arrays:

        res = max_subarray( array, 0, len(array) -1 )
        
        txt = f'Inputed Array: {array}\n' \
              f'Results of the Max Subarray algotithm:\n' \
              f'\tLower index: {res[0]}\n' \
              f'\tHigher index: {res[1]}\n' \
              f'\tMax Sum: {res[2]}\n'
        
        print(txt)