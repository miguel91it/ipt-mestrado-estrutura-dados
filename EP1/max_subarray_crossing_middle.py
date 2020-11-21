import math

def max_subarray_crossing_middle(array, start, end, middle):

    if len(array) == 0:
        return -1,-1,-1
    # elif len(array) == 1:
    #     return 0,0,array[0]

    if start == end:
        return 0,0,array[0]

    return_i = -1
    
    return_j = -1

    # define the -inf
    max_left_sum = -1 * math.inf

    sum = 0

    # find the max sub array to the left (i and max sum)   
    for i in reversed( range( start, middle + 1 ) ):

        sum = sum + array[i]

        if sum >= max_left_sum:

            max_left_sum = sum

            return_i = i

    # define the -inf
    max_right_sum = -1 * math.inf

    sum = 0

    # find the max sub array to the right (j and max sum)
    for j in range( middle + 1, end + 1 ):

        sum = sum + array[j]

        if sum >= max_right_sum:

            max_right_sum =  sum
            
            return_j = j

    # return i, j and sum of the sums
    return return_i, return_j, max_left_sum + max_right_sum

if __name__ == '__main__':

    import unittest

    class TestSubArrayCorssingMiddle(unittest.TestCase):

            def test_array_inteiro_positivos_estritos(self):
                array = [2,3,4,5,6]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (start, end, 20) )

            def test_array_inteiro_positivos(self):
                array = [2,0,4,0,6]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (start, end, 12) )

            def test_array_inteiro_zero(self):
                array = [0,0,0,0,0]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (0, 4, 0) )

            def test_array_inteiro_negativos_estritos(self):
                array = [-10,-20,-30,-40,-50]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (2, 3, -70) )

            def test_array_inteiro_negativos(self):
                array = [-10,0,-30,0,-50]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (1, 3, -30) )

            def test_array_inteiro_misto_1(self):
                array = [-10,0,30,0,-50]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (1, 3, 30) )

            def test_array_inteiro_misto_2(self):
                array = [-10,0,30,0]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (1, 3, 30) )

            def test_array_inteiro_misto_3(self):
                array = [-10,0,-30,0]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (1, 3, -30) )

            def test_array_vazio(self):
                array = []
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (-1, -1, -1) )

            def test_array_unitario(self):
                array = [1]
                start = 0
                end = len(array) - 1
                middle = int( (0 + len(array)) / 2 )
                res = max_subarray_crossing_middle(array, start, end, middle )
                print(f'\narray = {array}, res = {res}')
                self.assertEqual(res, (0, 0, 1) )

    unittest.main() 