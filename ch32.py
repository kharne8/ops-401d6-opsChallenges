#!/bin/python

#Script: Ops 401 Class 32 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 31 MAY 2023
#Purpose: 

#Main

import os
import sys
import hashlib

def file_search(dir_name):
    search_results = []

    def hash_file(file_path):
        with open(file_path, 'rb') as file:
            hasher = hashlib.md5()
            for chunk in iter(lambda: file.read(4096), b''):
                hasher.update(chunk)
            return hasher.hexdigest()

    def process_file(file_path):
        print(f"\nFile found: {file_path}")
        try:
            md5_hash = hash_file(file_path)
            timestamp = datetime.datetime.now().isoformat()
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            absolute_path = os.path.abspath(file_path)

            print(f"MD5 Hash: {md5_hash}")
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file_name}")
            print(f"File Size: {file_size}")
            print(f"Complete File Path: {absolute_path}")

            search_results.append(file_path)
        except Exception as error:
            print(f"Error hashing file: {file_path}", error)

    def traverse_directory(dir_path):
        for entry in os.listdir(dir_path):
            entry_path = os.path.join(dir_path, entry)
            if os.path.isdir(entry_path):
                traverse_directory(entry_path)
            elif os.path.isfile(entry_path):
                process_file(entry_path)

    traverse_directory(dir_name)

    return search_results

def start_search():
    while True:
        dir_name = input('\nPlease enter the directory for the files you would like to hash: ')
        if not os.path.isdir(dir_name):
            print('Invalid directory. Please try again.')
        else:
            break

    files_found = file_search(dir_name)

    print('\nTotal files searched:', count_files(dir_name))
    print('\nTotal files found:', len(files_found))

    start_search()

def count_files(dir_name):
    count = 0

    def traverse_directory(dir_path):
        nonlocal count
        for entry in os.listdir(dir_path):
            entry_path = os.path.join(dir_path, entry)
            if os.path.isdir(entry_path):
                traverse_directory(entry_path)
            elif os.path.isfile(entry_path):
                count += 1

    traverse_directory(dir_name)

    return count

start_search()

#End
