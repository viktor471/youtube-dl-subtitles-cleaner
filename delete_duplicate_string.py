#! /usr/bin/env python

import re
import work_with_files as files


def is_empty_line(line: str):
    return bool(re.match(r"\s*\n", line))


def is_time_code(line: str):
    time = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    return bool(re.match(time + r"\s*-->\s*" + time + r"\s*\n", line))


def is_suitable_line(line: str):
    return not is_empty_line(line) and not is_time_code(line)


def delete_duplicate_lines(input_text: list) -> list:
    found_lines = set()
    output_text = list(input_text)

    pairs = list(enumerate(input_text))

    for index, line in reversed(pairs):
        if is_suitable_line(line):
            if line not in found_lines:
                found_lines.add(line)
            else:
                output_text.pop(index)

    return output_text


def main():
    input_file_name = files.get_input_file_name()
    output_file_name = files.get_output_file_name()
    read_text = files.read_file(input_file_name)
    text_for_record = delete_duplicate_lines(read_text)
    files.write_to_file(text_for_record, output_file_name)


if __name__ == "__main__":
    main()

