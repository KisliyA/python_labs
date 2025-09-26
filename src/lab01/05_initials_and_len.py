full_name = input()
cleaned_name = ' '.join(full_name.split())
x = full_name.split()
print(f'ФИО: {cleaned_name}')
print(f'Инициалы: {x[0][0]}{x[1][0]}{x[2][0]}.')
print(f'Длина (символов): {len(cleaned_name)}')

