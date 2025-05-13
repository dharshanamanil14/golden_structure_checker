import os
import sys

# List of required paths (relative to the root directory)
REQUIRED_PATHS = [
    "README",
    "README2",
    "README3",
    "dir1/a.v",
    "dir2/b.v",
    "dir2/dir21/c.v",
    "dir2/dir22/d.v",
    "dir3/e.v",
    "dir3/dir31/dir311/f.v",
    "dir3/dir31/dir312/g.v",
    "dir3/dir32/dir321/h.v",
]

def main():
    # Check if root directory is passed as an argument
    if len(sys.argv) != 2:
        print("Usage: python check_structure.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    print(f"Checking directory structure in: {root_dir}")
    print("-" * 44)

    all_ok = True

    for path in REQUIRED_PATHS:
        full_path = os.path.join(root_dir, path)
        if not os.path.exists(full_path):
            print(f"MISSING: {path}")
            all_ok = False
        else:
            print(f"FOUND: {path}")

    print("-" * 44)
    if all_ok:
        print("All required files and directories are present.")
        sys.exit(0)
    else:
        print("Some files or directories are missing.")
        sys.exit(1)

if __name__ == "__main__":
    main()
