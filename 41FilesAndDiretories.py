#Files & Directories

from pathlib import Path

path = Path("FilesAndDiretoriesExtension")
print(path.exists())

for file in path.glob('*.py'):
    print(f"{file}\n")