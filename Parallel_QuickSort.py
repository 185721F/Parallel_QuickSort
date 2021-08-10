import concurrent.futures as confu
import statistics
import random
import os
import time

#クイックソートの関数
def quickSort(ele_num):
    left = []
    right = []
    if len(ele_num) <= 1:
        return ele_num
    median = int(statistics.median(ele_num))
    medianFlg = 0
    for element in ele_num:
        if element < median:
            left.append(element)
        elif element > median:
            right.append(element)
        else:
            medianFlg += 1


    left = quickSort(left)
    right = quickSort(right)


    return left + [median] * medianFlg + right

arr = ([random.randint(0,10**4) for i in range(10000)])

#プロセスで並列処理された結果が出力される。
start_process = time.time()
with confu.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    futures_process = [executor.submit(quickSort(arr))]
print(time.time()-start_process)

answer_process = quickSort(arr)
#print(answer_process)
print('並列処理(プロセス)↑')

#スレッドで並列処理された結果が出力される。
start_thread = time.time()
with confu.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
    futures_thread = executor.submit(quickSort(arr))
print(time.time()-start_thread)

answer_thread = quickSort(arr)
#print(answer_thread)
print('並列処理(スレッド)↑')

#逐次処理されたクイックソートの結果が出力される。
start = time.time()
answer = quickSort(arr)
print(time.time()-start)
#print(answer)
print('逐次処理↑')





