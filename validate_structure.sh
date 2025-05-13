#!/bin/bash

# Root directory to check (passed as argument)
ROOT_DIR=$1

# List of required paths relative to $ROOT_DIR
REQUIRED_PATHS=(
  "README"
  "README2"
  "README3"
  "dir1/a.v"
  "dir2/b.v"
  "dir2/dir21/c.v"
  "dir2/dir22/d.v"
  "dir3/e.v"
  "dir3/dir31/dir311/f.v"
  "dir3/dir31/dir312/g.v"
  "dir3/dir32/dir321/h.v"
)

echo "🔍 Checking directory structure in: $ROOT_DIR"
echo "--------------------------------------------"

ALL_OK=true

for path in "${REQUIRED_PATHS[@]}"; do
  if [ ! -e "$ROOT_DIR/$path" ]; then
    echo "❌ MISSING: $path"
    ALL_OK=false
  else
    echo "✅ FOUND: $path"
  fi
done

echo "--------------------------------------------"
if $ALL_OK; then
  echo "🎉 All required files and directories are present."
  exit 0
else
  echo "⚠️ Some files or directories are missing."
  exit 1
fi
