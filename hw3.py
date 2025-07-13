# hw03.py

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(path: Path, prefix=""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                print_directory_structure(item, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission Denied] {item}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py <c:/Users/Rui/Desktop/GitHub/goit_pycore_hw_4>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: вказаний шлях не є директорією")
        sys.exit(1)

    print(f"{Fore.YELLOW}Структура директорії: {dir_path}\n")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()
