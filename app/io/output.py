def output_to_console(text: str):
    """Виводить текст у консоль"""
    print(f"Вивід: {text}")

def write_to_file_builtin(filepath: str, text: str):
    """Записує текст у файл за допомогою вбудованих можливостей Python"""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)
