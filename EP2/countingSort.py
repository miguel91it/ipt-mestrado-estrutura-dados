from linkedList import CircularDoublyLinkedListWithHead as linkedList, createRandomList
import random
import sys
from datetime import datetime

# if len(sys.argv) < 2:

#     print('Faltando argumento')

#     exit(0)

# try:
#     n = int(sys.argv[1])

# except Exception as e:

#     print('Argumento passado nao é inteiro: ', e)

#     exit(0)

tests = [i for i in range(1,100) if i % 5 == 0]

tests += [i for i in range(100,1000) if i % 100 == 0]

# tests += [i for i in range(1000,10000) if i % 1000 == 0]

# tests += [i for i in range(10000,100000) if i % 10000 == 0]

# tests += [i for i in range(100000,1000000) if i % 100000 == 0]

# tests += [i for i in range(1000000,10000000) if i % 1000000 == 0]

data = {}

# tests = [1000000]

for round in tests:

    list = createRandomList(round,1000000)

    startTime = datetime.now()

    list.countingSort()

    endTime = datetime.now()

    diff = endTime - startTime

    diff_total_sec = diff.total_seconds()

    data[round] = {
        'counting sort': {
            'started at': startTime.isoformat(),
            'finished at': endTime.isoformat(),
            'duration': diff_total_sec
        }
    }

    # startTime = datetime.now()
    # list.quickSort()
    # endTime = datetime.now()
    # diff = endTime - startTime
    # diff_total_sec = diff.total_seconds()
    # data[round]['quick sort'] = {
    #     'started at': startTime.isoformat(),
    #     'finished at': endTime.isoformat(),
    #     'duration': diff_total_sec
    # }


    # print(diff, diff_total_sec)
    # print(f'start: {startTime.isoformat()} | end: {endTime.isoformat()} | diff: {str(diff_total_sec)}')


import json

print(json.dumps(data))