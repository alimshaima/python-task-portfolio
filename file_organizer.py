# Task 13: Automated File Organizer
import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found!")
        return
    
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.aac']
    }
    
    for category, extensions in categories.items():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f"Moved '{file}' to '{category_path}'")
    
    print("\nFile organisation complete")

# Example usage
folder_path = input("Enter folder path to organize: ")
organize_files(folder_path)
