import random
import math
import string

#print (random.sample(range(1, 18), 4))

# Сортировки
# 16 
# 7
# 13
# 8
# https://habr.com/en/post/335920/


# (12) Функция msd_sort принимает в качестве аргумента список целых чисел arr, который нужно отсортировать. 
# Сначала в этой функции находится максимальное значение в списке arr и сохраняется в переменной max_val. 
# Затем создается переменная exp, которая инициализируется значением 1. Эта переменная будет использоваться для 
# определения разряда чисел при сортировке.

def msd_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

ar = list(range(100))
#ar= [160, 45, 20, 21, 12, 523]
msd_sort(ar)
print("1) ", ar)
print(" ")
        
# (2) Этот код реализует алгоритм сортировки пузырьком. 
# Сначала он создает список из 100 случайных чисел в диапазоне от -1 до 1 
# с помощью генератора списка и функции random.uniform. Затем этот список 
# передается в функцию bubblesort, которая сортирует его в порядке возрастания.
# Функция bubblesort принимает список в качестве аргумента и сортирует его 
# путем сравнения каждого элемента со следующим и обмена их местами, если они 
# находятся в неправильном порядке. Этот процесс повторяется до тех пор, 
# пока все элементы не будут отсортированы. В конце функция возвращает 
# отсортированный список.

def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index - 1] <= arr[index]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

arr = [random.uniform(-1, 1) for _ in range(999)]
gnome_sort(arr)
print("2) ", arr)
print(" ")


# (13) Bucket sort - это алгоритм сортировки, который работает путем 
# распределения элементов в массиве по “ведрам” или “корзинам”, 
# а затем сортирует элементы в каждом ведре отдельно. создает 42000 разных 
# точек комплексной плоскости, лежащие внутри окружности 
# радиуса r = birth_day / birth_month, и сортирует их по модулю 
# числа с использованием метода Bucket sort:

birth_day = 13
birth_month = 11
r = birth_day / birth_month

def bucket_sort(arr):
    max_val = max([abs(x) for x in arr])
    size = max_val/len(arr)
    buckets = [[] for k in range(len(arr))]
    for i in range(len(arr)):
        j = int(abs(arr[i])/size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr)-1].append(arr[i])
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i], key=abs)
    result = []
    for i in range(len(arr)):
        result += buckets[i]
    return result

arr = []
while len(arr) < 100:
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if math.sqrt(x**2 + y**2) <= r:
        arr.append(complex(x,y))

result3 = bucket_sort(arr)
print("3) ", result3)
print(" ")


# (9) Heapsort - это алгоритм сортировки, который использует 
# структуру данных под названием “куча” для сортировки элементов. Он 
# работает путем создания максимальной кучи из входного массива и затем 
# извлечения максимального элемента из кучи и помещения его в конец 
# отсортированного массива. Этот процесс повторяется до тех пор, 
# пока все элементы не будут отсортированы.

file = '2.txt'
book = []
with open(file, encoding='utf-8') as file:
    for line in file:
        for i in line.split():
            book.append(i.strip(string.punctuation))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

text = book[:1000]
heapSort(text)
print("4) ", text)