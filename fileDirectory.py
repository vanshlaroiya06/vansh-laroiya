import os
import shutil

# Define the function to organize files
def organize_files(directory):
    # Ensure the directory path is absolute
    directory = os.path.abspath(directory)

    # Dictionary to map file types to folders
    extensions_folders = {
        'Documents': ['doc', 'docx', 'pdf', 'txt'],
        'Images': ['jpg', 'jpeg', 'png', 'gif'],
        'Videos': ['mp4', 'mkv', 'avi'],
        'Music': ['mp3', 'wav'],
        'Archives': ['zip', 'tar', 'gz'],
        'Others': []  # Files that don't match any specified type will go here
    }

    # Create folders if they don't exist
    for folder in extensions_folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Walk through each file in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct full file path
            src_path = os.path.join(root, file)

            # Extract file extension
            _, extension = os.path.splitext(file)
            extension = extension[1:].lower()  # Remove leading '.' and convert to lowercase

            # Determine destination folder
            destination_folder = 'Others'
            for folder, exts in extensions_folders.items():
                if extension in exts:
                    destination_folder = folder
                    break

            # Move the file to the appropriate folder
            dest_path = os.path.join(directory, destination_folder, file)
            if src_path != dest_path:  # Check if file is not already in destination folder
                shutil.move(src_path, dest_path)
                print(f'Moved: {src_path} --> {dest_path}')

# Main function to execute the script
def main():
    # Directory path to be organized
    directory = input("Enter the path of the directory to organize: ")
    
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        return
    
    organize_files(directory)
    print("File organization complete!")

if __name__ == "__main__":
    main()

