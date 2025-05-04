#!/usr/bin/env python3
"""
Text File Splitter

This script splits a large text file into multiple smaller files based on word count.
Each output file will be named '{file_name}_{n}' where n is the file number.
By default, each file will contain 10,000 words.
"""

import os
import argparse

def split_file_by_words(input_file, output_dir="split_files", file_prefix=None, words_per_file=10000):
    """
    Split a large text file into multiple files based on word count.
    
    Args:
        input_file (str): Path to the input text file
        output_dir (str): Directory to store the split files
        file_prefix (str): Prefix for output file names
        words_per_file (int): Number of words per output file (default: 10,000)
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # If file_prefix is not provided, use the input filename without extension
    if file_prefix is None:
        file_prefix = os.path.splitext(os.path.basename(input_file))[0]
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into words
    words = content.split()
    total_words = len(words)
    print(f"Total words in file: {total_words}")
    
    # Calculate number of files needed
    file_count = (total_words + words_per_file - 1) // words_per_file  # Ceiling division
    print(f"Splitting into {file_count} files with {words_per_file} words each (last file may have fewer)")
    
    # Split and write files
    for i in range(file_count):
        start_idx = i * words_per_file
        end_idx = min((i + 1) * words_per_file, total_words)
        
        # Extract the words for this file
        file_words = words[start_idx:end_idx]
        file_content = ' '.join(file_words)
        
        # Write to file
        output_file = os.path.join(output_dir, f"{file_prefix}_{i+1}")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(file_content)
        
        print(f"Created file: {output_file} with {len(file_words)} words")


def main():
    parser = argparse.ArgumentParser(description="Split a large text file into multiple smaller files based on word count.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("-o", "--output-dir", default="split_files", 
                        help="Directory to store the split files (default: 'split_files')")
    parser.add_argument("-p", "--prefix", default=None, 
                        help="Prefix for output file names (default: input filename without extension)")
    parser.add_argument("-w", "--words-per-file", type=int, default=10000,
                        help="Number of words per output file (default: 10,000)")
    
    args = parser.parse_args()
    
    print(f"Splitting {args.input_file} into files with {args.words_per_file} words each...")
    split_file_by_words(args.input_file, args.output_dir, args.prefix, args.words_per_file)
    print("Splitting complete!")

if __name__ == "__main__":
    main()