def input_from_console() -> str:
    """Отримує текст з консолі"""
    return input("Введіть текст: ")

def read_from_file_builtin(filepath: str) -> str:
    """Зчитує текст з файлу за допомогою вбудованих можливостей Python"""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def read_from_file_pandas(filepath: str):
    """Зчитує дані з файлу за допомогою бібліотеки pandas"""
    import pandas as pd
    return pd.read_csv(filepath)
