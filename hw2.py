def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8")as file:
            for line in file:
                line = line.strip().split(",")
                if not line:
                    continue
                try:
                    cat_id, name, age = line
                    cat_dict = {"id":cat_id, "name":name, "age":age}
                    cats.append(cat_dict)
                except ValueError:
                    print(f"Невірний формат рядка: {line.strip()}")
                    continue
        return cats
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return None
    except ValueError as e:
        print(f"Помилка: {e}")
        return None
with open("cats_file.txt", "w", encoding="utf-8") as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    file.write("60b90c2413067a15887e1ae2,Vika,1\n")
    file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    file.write("60b90c4613067a15887e1ae5,Tessi,5\n")
cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(cat)
    
