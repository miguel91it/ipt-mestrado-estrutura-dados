#%%
from linkedList import CircularDoublyLinkedListWithHead as linkedList, createRandomList
import random
import sys
from datetime import datetime
import matplotlib.pyplot as plt

import pandas as pd

tests = [i for i in range(1,100) if i % 5 == 0]

tests += [i for i in range(100,1000) if i % 100 == 0]

tests += [i for i in range(1000,10000) if i % 1000 == 0]

tests += [i for i in range(10000,100000) if i % 10000 == 0]

tests += [i for i in range(100000,1000000) if i % 100000 == 0]

tests += [i for i in range(1000000,10000000) if i % 1000000 == 0]

data = {
    'n': tests,
    'times': {
        'counting_sort': []
        # ,
        # 'quick_sort': []
    }
}

for round in tests:

    list = createRandomList(round,1000000)

    startTime = datetime.now()

    list.countingSort()

    endTime = datetime.now()

    diff = endTime - startTime

    diff_total_sec = diff.total_seconds()

    data['times']['counting_sort'].append(diff_total_sec)

    # startTime = datetime.now()

    # quicksort(list)

    # endTime = datetime.now()

    # diff = endTime - startTime

    # diff_total_sec = diff.total_seconds()

    # data['times']['quick_sort'].append(diff_total_sec)

print('finalizou ordenações')

#%%
df = pd.DataFrame(data['times']['counting_sort'], index=data['n'], columns=['counting_sort'])

print(df)

#%%
plt.figure()


df.plot()
# %%
