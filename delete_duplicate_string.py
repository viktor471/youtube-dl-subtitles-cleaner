#! /usr/bin/env python

import re
import work_with_files as files


def is_empty_line(line: str):
    """Check if line is empty. Returns True if line contains only whitespaces"""
    return bool(re.match(r"\s*\n", line))


def is_time_code(line: str):
    """Check if line has timecode. Returns True if line contain timecode"""
    time = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    return bool(re.match(time + r"\s*-->\s*" + time + r"\s*\n", line))


def is_suitable_line(line: str):
    return not is_empty_line(line) and not is_time_code(line)


def get_chunk(text: list):
    for index in reversed(range(1, len(text) - 1)):
        yield index, text[index-1:index+2]


def is_empty_timecode(chunk: list):
    return is_empty_line(chunk[0]) and is_time_code(chunk[1]) and is_empty_line(chunk[2])


def del_chunk_with_index(index: int, text: list):
    text.pop(index + 1)
    text.pop(index)
    text.pop(index - 1)


def delete_duplicate_lines(input_text: list) -> list:
    """Take list with lines from read file and returns list of lines without duplicates and extra timecodes

    Args:
        input_text (list): lines from the read file and processed with the help delete_service_data.py script

    Returns:
        list: list without duplicates and extra timecodes
    """
    found_lines = set()
    output_text = list(input_text)

    pairs = list(enumerate(input_text))

    for index, line in reversed(pairs):
        if is_suitable_line(line):
            if line not in found_lines:
                found_lines.add(line)
            else:
                output_text.pop(index)

    for index, chunk in get_chunk(output_text):
        if is_empty_timecode(chunk):
            del_chunk_with_index(index, output_text)

    return output_text


def main():
    input_file_name = files.get_input_file_name()
    output_file_name = files.get_output_file_name()
    read_text = files.read_file(input_file_name)
    text_for_record = delete_duplicate_lines(read_text)
    files.write_to_file(text_for_record, output_file_name)


if __name__ == "__main__":
    main()

