from pathlib import Path

path1 = Path(r"C:\Program Files\Microsoft") / Path(r"\A Folder")
Path.home()  # Home directory of the user

path1.iterdir()  # List of files and directories

with open("__init__.py", "r") as file:
    print(file)

# Or just =>
print(path1.read_text())
