#! /usr/bin/env python

import re
import work_with_files as files


def delete_matches(pattern: str, line: str) -> str:
    """Replace matches that matches pattern with empty string

    Args:
        pattern (str): regex for search
        line (str): editable line

    Returns:
        str: string with deleted matches
    """
    return re.sub(pattern, "", line)


def delete_extra_service_data(text: list):
    """Delete service data from text"""
    output = []
    for line in text:
        line = delete_matches(r"<c>", line)
        line = delete_matches(r"</c>", line)
        line = delete_matches(r" align:start position:0%", line)
        output.append(delete_matches(r"<\d{2}:\d{2}:\d{2}.\d{3}>", line))

    return output


def main():
    input_file_name = files.get_input_file_name()
    output_file_name = files.get_output_file_name()
    text = files.read_file(input_file_name)
    output = delete_extra_service_data(text)
    files.write_to_file(output, output_file_name)


if __name__ == "__main__":
    main()
