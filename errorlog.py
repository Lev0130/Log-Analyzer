"""Quiero que tu programa sea capaz de:

Leer el archivo

Detectar líneas con "ERROR"

Extraer:

la fecha

el tipo (ERROR, INFO, etc.)

Contar frecuencias (cuántos errores hay)
crear un diccionario anidado, tipos de errores por fecha


add date to dictionary if not exists already
if date the same, append error_type and value
if not, continue
"""
import re
dates = {}
entries = {}
error_count = 0

    
with open("C:/Users/Leo/Desktop/Curso Python/projects/Exercises/logs.log", "r", encoding = "utf-8") as file:
    for line in file:
        patern_date = r"\d{4}-\d{2}-\d{2}"
        search = re.match(patern_date, line)
        date = search.group()
        if date in dates:
            entry = line.split()
            if "ERROR" in entry:
                dates[date]["error_count"] += 1
                try:
                    dates[date][" ".join(entry[3:])] += 1
                except:
                    dates[date][" ".join(entry[3:])] = 1
                    
            else:
                continue
        if date not in dates:
            dates[date] = {}
            entry = line.split()
            if "ERROR" in entry:
                dates[date]["error_count"] = 1
                dates[date][" ".join(entry[3:])] = 1
                    
            else:
                continue
print(dates)
"""
with open("C:/Users/Leo/Desktop/Curso Python/projects/Exercises/logs.log", "r", encoding = "utf-8") as file:
    for line in file:
        entry = line.split()
        if "ERROR" in entry:
            error_count += 1
            try:
                entries[" ".join(entry[3:])] += 1
            except:
                entries[" ".join(entry[3:])] = 1
        else:
            continue
    print("Number of errors: ", error_count, "n", entries)
    """