import os

# 🗂️ Folder path containing the music files
folder_path = r"C:\Users\"

# 🔍 Prefix you want to remove from the beginning of the filename
prefix_to_remove = "[SPOTDOWNLOADER.COM] "

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the filename starts with the unwanted prefix
    if filename.startswith(prefix_to_remove):
        # Create the new filename without the prefix
        new_name = filename[len(prefix_to_remove):]
        
        # Get the full paths for the old and new filenames
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Print the change to the console
        print(f"Renamed: {filename} → {new_name}")
