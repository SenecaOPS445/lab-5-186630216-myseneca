#!/usr/bin/env python3
#Author: Eliza Silvetsre
#Author ID: esilvestre
#File name: lab5b.py

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as file:
        return [line.strip('\n') for line in file] 

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    with open(file_name_read, 'r') as read_file:
        lines = read_file.readlines()
    with open(file_name_write, 'w') as write_file:
        for i, line in enumerate(lines, start=1):
            write_file.write(str(i) + ':' + line)