from pathlib import Path  # Handling the path location


class BulkFileRenamer:
    """
    A class to rename files in bulk with a given prefix and numbering.
    """

    def __init__(self, folder_path, prefix_value="file", start=1):
        self.folder = Path(folder_path)
        self.prefix = prefix_value
        self.start = start

    def rename_files(self):

        # Check folder exists AND is directory
        if not self.folder.exists() or not self.folder.is_dir():
            print(" Folder does not exist!")
            return

        # Get only files
        files = [f for f in self.folder.iterdir() if f.is_file()]

        # Empty folder check
        if not files:
            print("No files found!")
            return

        # Sort files
        files.sort()

        count = self.start

        for file in files:

            # Skip hidden files
            if file.name.startswith("."):
                continue

            new_name = f"{self.prefix}_{count}{file.suffix}"
            new_file = self.folder / new_name

            # Avoid overwrite
            if new_file.exists():
                print(f"️ Skipped (exists): {new_name}")
                continue

            try:
                # Rename
                file.rename(new_file)
                print(f" {file.name} → {new_name}")
                count += 1
            except Exception as e:
                print(f" Error renaming {file.name}: {e}")

        print("\n Renaming completed!")


# CLI usage
if __name__ == "__main__":
    print(" Bulk File Renamer (Class Version)")

    path = input("Enter folder path: ")
    prefix = input("Enter prefix (default = file): ") or "file"

    renamer = BulkFileRenamer(path, prefix)
    renamer.rename_files()