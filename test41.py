#Files & Directories

from pathlib import Path

path = Path("Test41extension")
print(path.exists())

for file in path.glob('*.py'):
    print(f"{file}\n")
