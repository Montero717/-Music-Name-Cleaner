# 🎧 Music Name Cleaner

**Music Name Cleaner** is a simple Python script that removes unwanted prefixes from the beginning of song filenames inside a selected folder. It's perfect for cleaning up names that start with tags like `[SPOTDOWNLOADER.COM]`, `hey`, or any other promotional text.

---

## 💡 What Does It Do?

- Scans all files inside a given folder.
- Detects filenames that start with a specific prefix.
- Removes that prefix from the filename.
- Renames the files automatically.

---

## 🛠️ Requirements

- Python 3.x  
(Tested with Python 3.11+)

---

## 📦 How to Use

1. Open the `music_cleaner.py` file using a code editor like VS Code or Notepad++.
2. Set the correct path to your music folder:

```python
folder_path = r"C:\Users\YourName\Desktop\music old school"
```

3. Set the prefix you want to remove (e.g., `[SPOTDOWNLOADER.COM] `):

```python
prefix_to_remove = "[SPOTDOWNLOADER.COM] "
```

4. Run the script:

```bash
python music_cleaner.py
```

5. The console will show renamed files as they are processed.

---

## 🔒 Notes

- Make sure to **back up** your files before running the script.
- The script only removes the prefix from the **start** of filenames, not from the middle or end.
- It works with all file types, but you can easily limit it to `.mp3`, `.wav`, etc., if needed.

---

## ✨ Example

**Before:**
```
[SPOTDOWNLOADER.COM] Tupac - Changes.mp3
[SPOTDOWNLOADER.COM] Biggie - Juicy.mp3
```

**After:**
```
Tupac - Changes.mp3
Biggie - Juicy.mp3
```

---

## 📃 License

This is an open-source project. Feel free to use or modify it however you like.

---

## 👨‍💻 Created By

Mohamed Saad – 2025
