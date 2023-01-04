# Write a script that takes any number of directories as command-line arguments and
# then lists the contents of each of these directories

directories=$@

if [ -z "$directories" ]; then
  directories='./'
fi
for directory in $directories; do
  echo "Directory: $directory"
  for item in $(ls $directory); do
    echo " - $item"
  done
done