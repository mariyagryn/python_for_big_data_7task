from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin

def main():
    user_input = input_from_console()

    file_text = read_from_file_builtin("data/example.txt")

    read_from_file_pandas("data/example.csv")

    output_to_console(user_input)
    output_to_console(file_text)

    write_to_file_builtin("data/output.txt", user_input + "\n" + file_text)

if __name__ == "__main__":
    main()
