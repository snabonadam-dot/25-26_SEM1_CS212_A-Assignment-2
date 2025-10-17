#!/usr/bin/env python3
"""
Python CLI File Manager - Core File Management Module
Contains core file management functionality:
file operations, size calculations, and file system interactions.
Uses only standard library modules.
"""

import os


def format_file_size(size_bytes, precision=2, use_binary=True):
    """
    Convert file size in bytes to human-readable format.
    
    This function teaches:
    - Mathematical calculations
    - Conditional logic with multiple branches
    - String formatting
    - Algorithm design
    - Parameter handling
    """
    if not isinstance(size_bytes, (int, float)) or size_bytes < 0:
        return "Invalid size"
    
    if size_bytes == 0:
        return "0 bytes"
    
    # Define units (binary vs decimal)
    if use_binary:
        units = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']
        divisor = 1024
    else:
        units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
        divisor = 1000
    
    # TODO: Students implement the conversion algorithm
    # This involves loops, mathematical operations, and formatting
    
    return formatted_size


def get_and_display_file_size(filename):
    """Get and display the size of a specified file."""
    if not filename:
        print("Error: No filename provided.")
        return
    else:
        filename = filename.strip()
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return

        # Check if it's a file (not a directory)
        if not os.path.isfile(filename):
            print(f"Error: '{filename}' is not a regular file.")
            return

        # Get file size in bytes
        size_bytes = os.path.getsize(filename)

        # Use format_file_size to get human-readable format
        formatted_size = format_file_size(size_bytes)

        # Display results
        print(f"\nFile: {filename}")
        print(f"Size: {size_bytes} bytes")
        print(f"Size: {formatted_size}")

    except OSError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def list_directory_tree(directory, prefix="", max_depth=3, current_depth=0):
    """
    Display directory structure as a tree using recursion.
    - Tree structures are naturally recursive
    - Clear base cases and recursive cases
    - Visual output helps understand recursion
    - Tests multiple base cases
    """
    # Base case 1: Invalid directory
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        # TODO: return None for the base case

    # Base case 2: Maximum depth reached
    if current_depth >= max_depth:
        print(f"{prefix}... (max depth reached)")
        # TODO: return None for yet another base case

    try:
        # Get and sort directory contents
        items = sorted(os.listdir(directory))

        # Base case 3: Empty directory
        if not items:
            print(f"{prefix}(empty directory)")
            # TODO: return None for yet another base case

        for i, item in enumerate(items):
            item_path = os.path.join(directory, item)
            is_last = i == len(items) - 1

            # Choose the appropriate tree symbols
            if is_last:
                current_prefix = prefix + "└── "
                next_prefix = prefix + "    "
            else:
                current_prefix = prefix + "├── "
                next_prefix = prefix + "│   "

            if os.path.isfile(item_path):
                # Display file with size
                try:
                    size = os.path.getsize(item_path)
                    print(f"{current_prefix}{item} ({size} bytes)")
                except OSError:
                    print(f"{current_prefix}{item} (size unknown)")

            elif os.path.isdir(item_path):
                # Display directory and recurse
                print(f"{current_prefix}{item}/")
                # Recursive case: explore subdirectory
                # TODO: perform recursive function call

    except (OSError, PermissionError) as e:
        print(f"{prefix}Error accessing directory: {e}")


def find_files_by_extension(directory, extension, current_path=""):
    """
    Recursively find all files with a specific extension.
    """
    # Base case: Invalid directory
    if not os.path.isdir(directory):
        # TODO: return an empty list for the base case
        # TODO: remove the pass statement below, only added to avoid syntax error
        pass

    # TODO: Initialize found_files as an empty list

    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.isfile(item_path):
                # Base case: Check if file matches extension
                if item.lower().endswith(extension.lower()):
                    relative_path = (
                        os.path.join(current_path, item) if current_path else item
                    )
                    found_files.append(relative_path)

            elif os.path.isdir(item_path):
                # Recursive case: Search in subdirectory
                sub_path = os.path.join(current_path, item) if current_path else item
                # TODO recursively call find_files_by_extension
                # TODO: Extend found_files with results from recursive call
               

    except (OSError, PermissionError):
        pass  # Skip inaccessible directories

    return found_files
    found_files()


