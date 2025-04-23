from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin


def main():
    input_from_console()
    read_from_file_builtin("example.txt")
    read_from_file_pandas("example.csv")

    output_to_console("Hello, world!")
    write_to_file_builtin("output.txt", "Hello, world!")


if __name__ == "__main__":
    main()
