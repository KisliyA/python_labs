<h1>Программирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №2:</h2>

**Задание №1(arrays):**
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    maxi = max(nums)
    mini = min(nums)
    return mini,maxi
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print('ValueError')
print(min_max([1.5,2,2.0,-3.1]))

```
![exe1!](/images/lab02/arrays.png)
-------------------------------------------
**Задание unique sorted:**
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(dict.fromkeys(sorted(nums)))
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([0,1.0,2.5]))
```
![exe2!](/images/lab02/unique_sorted.png)
-------------------------------------------
**Задание flatten:**
```python
def flatten(mat: list[list | tuple]) -> list:
    rez = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for k in mat[i]:
                rez.append(k)
        else:
            return 'TypeError'
    return rez
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1],[], [2, 3]]))
print(flatten([[1, 2], 'ab']))
```
![exe3!](/images/lab02/flatten.png)
-------------------------------------------
**Задание matrix:**
```python
def _verify_row_lengths(mat: list[list[float | int]]) -> bool:
    rowl = len(mat[0])
    for row in mat:
        if len(row) != rowl:
            return False
    return True

def transpose(matrix: list[list[float | int]]) -> list[list[float | int]] | str:
    if not matrix:
        return []
    if not _verify_row_lengths(matrix):
        return "ValueError"
    return [[matrix[row][col] for row in range(len(matrix))] 
            for col in range(len(matrix[0]))]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not _verify_row_lengths(mat):
        return "ValueError"
    return [sum(i) for i in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not _verify_row_lengths(mat):
        return "ValueError"
    return row_sums(transpose(mat))

print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([[1], [2], [3]]))    # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))   # [[1, 3], [2, 4]]
print(transpose([]))                 # []
print(transpose([[1, 2], [3]]))      # ValueError

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

```
![exe4!](/images/lab02/matrix.png)
-------------------------------------------
**Задание tuples:**
```python
def get_formatted_tuple(fio: str, group: str, gpa: float) -> tuple:
    fio_list = fio.strip().split()
    name, surname = fio_list[1], fio_list[0]
    res_fio = f"{surname.capitalize()} {name[0].upper()}"
    if len(fio_list) > 2:
        res_fio += f".{fio_list[2][0].upper()}."
        
    return (res_fio, f'гр. {group}', f"Gpa {gpa:.2f}")

def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec

    if not isinstance(fio, str):
        raise TypeError("fio должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("group должно быть строкой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("gpa должно быть числом")
    
    inf = get_formatted_tuple(fio, group, gpa)
    answer = ', '.join(inf)
    return answer

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![exe5!](/images/lab02/tuples.png)
-------------------------------------------
