#  Bulk File Renamer

A simple and efficient Python tool to rename multiple files in a folder automatically using a custom prefix and numbering.

---

##  Features

*  Rename files in bulk
*  Automatic numbering
*  Custom prefix support
*  Keeps original file extensions
*  Skips duplicate file names
*  Ignores hidden files
*  Handles edge cases (invalid folder, empty folder)

---

##  Installation

### Clone the repository:

```bash
https://github.com/anuskabhandari/Bulk_file_renamer.git
cd file_renamer
```

### Or install from PyPI:

```bash
pip install file-renamer
```

---

##  Usage

Run the program:

```bash
python file_renamer.py
```

Enter inputs:

```
Enter folder path: test_files
Enter prefix: file
```

---

##  Example (Before & After)

###  Before Renaming
https://drive.google.com/file/d/1so9-L7PhesLv45y6xH4nzYdEk1QlKBrU/view?usp=sharing


###  After Renaming
https://drive.google.com/file/d/1mzY2XGfYv9B4Oisgt4P9Y2gvUfc8zfZu/view?usp=sharing


---

##  Example Output

```
img1.jpg → file_1.jpg
img2.png → file_2.png
doc1.pdf → file_3.pdf

Renaming completed!
```

---

##  Edge Cases Handled

*  Invalid folder path
*  Empty folder
*  Duplicate file names (skipped)
*  Hidden files ignored

---

##  How It Works

1. Access folder using `pathlib`
2. Read all files
3. Loop through files
4. Generate new names using prefix + number
5. Rename files safely

---

##  Author

**Anuska Bhandari**

---

##  License

This project is open-source and available under the MIT License.
