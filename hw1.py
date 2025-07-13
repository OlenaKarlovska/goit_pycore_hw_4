def total_salary(path):
  try:
    with open(path, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      total = 0
      count = 0
      for line in lines:
        try:
          name, salary = line.strip().split(',')
          total += int(salary)
          count += 1
        except ValueError:
          print(f"Невірний формат рядка: {line.strip()}")
          continue
      if count == 0:
        raise ValueError("Файл порожній")
      average = total / count
      return total, average
  except FileNotFoundError:
    print(f"Файл не знайдено: {path}")
    return None, None
  except ValueError as e:
    print(f"Помилка: {e}")
    return None, None

with open('salary_file.txt', 'w', encoding='utf-8') as file:
  file.write('Alex Korp,3000\n')
  file.write('Nikita Borisenko,2000\n')
  file.write('Sitarama Raju,1000\n')

total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")