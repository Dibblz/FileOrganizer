#Devin Webster
#2024
#File Organizer

import os
import shutil
import argparse
from datetime import datetime

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.md', '.xlsx', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Scripts': ['.py', '.sh', '.bat', '.js'],
    'Executables': ['.exe', '.msi'],
    'Other': []
}

def get_category(extension):
    for category, ext_list in FILE_TYPES.items():
        if extension.lower() in ext_list:
            return category
    return 'Other'

def organize(directory):
    if not os.path.isdir(directory):
        print(f"[!] Directory '{directory}' not found.")
        return

    print(f"[+] Organizing files in: {directory}")
    
    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1]
            category = get_category(ext)
            source = os.path.join(root, file)
            dest_folder = os.path.join(directory, category)
            os.makedirs(dest_folder, exist_ok=True)

            dest = os.path.join(dest_folder, file)
            count = 1
            while os.path.exists(dest):
                name, extension = os.path.splitext(file)
                dest = os.path.join(dest_folder, f"{name}_{count}{extension}")
                count += 1

            shutil.move(source, dest)
            print(f"[*] Moved: {file} → {category}/")

        # Only process top-level directory (no recursion into subfolders)
        break

    print("[+] Done.")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by file type.")
    parser.add_argument("directory", help="Target directory to organize")
    args = parser.parse_args()

    organize(args.directory)

if __name__ == "__main__":
    main()
