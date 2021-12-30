import sys
import ntpath


def get_input_file_name(argv=sys.argv) -> str:
    """Get input file name from 1st argument"""
    if len(argv) > 1:
        return argv[1]
    else:
        sys.stderr.write("there is no input file\n")


def get_output_file_name(argv=sys.argv) -> str:
    """Get output file name. It will generated from input file name or got from 2nd argument"""
    if len(argv) < 3:
        return "output_" + ntpath.basename(get_input_file_name())
    else:
        return argv[2]


def read_file(filename: str) -> list:
    with open(filename, "r") as file:
        return file.readlines()


def write_to_file(text: list, filename: str):
    with open(filename, "w") as file:
        file.writelines(text)
