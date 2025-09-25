<h1>Программирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №1:</h2>

**Задание №1:**
```python
name = input('Имя:')
age = int(input('Возраст:'))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![exe1!](/images/lab01/exe1.png)
-------------------------------------------
**Задание №2:**
```python
num1 = float(input('a:').replace(',','.'))
num2 = float(input('b:').replace(',','.'))
sum = num1 + num2 
avg = (num1 + num2) / 2
print(f'sum={sum:.2f};avg={avg:.2f}')
```
![exe2!](/images/lab01/exe2.png)
-------------------------------------------
**Задание №3:**
```python
price = float(input('Price:'))
discount = float(input('Discount:'))
vat = float(input('Vat:'))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки:{base:.2f} ₽')
print(f'НДС:{vat_amount:.2f} ₽')
print(f'Итого к оплате:{total:.2f} ₽')
```
![exe3!](/images/lab01/exe3.png)
-------------------------------------------
**Задание №4:**
```python
m = int(input('Минуты:'))
print(f'{m // 60}:{m % 60}')

```
![exe4!](/images/lab01/exe4.png)
-------------------------------------------
**Задание №5:**
```python
full_name = input()
cleaned_name = ' '.join(full_name.split())
x = full_name.split()
print(f'ФИО:{cleaned_name}')
print(f'Инициалы:{x[0][0]}{x[1][0]}{x[2][0]}.')
print(f'Длина (символов):{len(cleaned_name)}')
![exe5!](/images/lab01/exe5.png)
-------------------------------------------
