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