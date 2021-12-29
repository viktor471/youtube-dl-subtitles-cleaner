#! /usr/bin/env python

import delete_duplicate_string as dupl
import delete_service_data as srv
import work_with_files as files


def main():
    input_file_name = files.get_input_file_name()
    output_file_name = files.get_output_file_name()
    text = files.read_file(input_file_name)
    output = srv.delete_extra_service_data(text)
    output = dupl.delete_duplicate_lines(output)
    files.write_to_file(output, output_file_name)


if __name__ == "__main__":
    main()
