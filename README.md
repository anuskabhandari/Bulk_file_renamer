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

```bash
pip install bulk-renamer-anuska

```
## Project Structure
 bulk_file_renamer/
│
├── dist/
├── file_renamer/
│   ├── __init__.py
│   └── file_renamer.py
│
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.py
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
## Contributing
Contributions are welcome!
Feel free to open issues or submit pull requests.

---
##  License

This project is open-source and available under the MIT License.

---
##  Author

Developed by Anuska Bhandari

