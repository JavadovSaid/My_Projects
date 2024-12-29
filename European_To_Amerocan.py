import shutil, os, re

# Create a regex that matches files with the European date format.
euro_style = re.compile(r'''^(.*?)       # All text before the date
    ((0|1|2|3)?\d)-                      # One or two digits for the day
    ((0|1)?\d)-                          # One or two digits for the month
    ((19|20)?\d\d)                       # Four digits for the year
    (.*?)$                               # All text after the date
    ''', re.VERBOSE)

# Loop over the files in the working directory.
for euro_files in os.listdir('.'):
    mo = euro_style.search(euro_files)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    before = mo.group(1)
    day = mo.group(2)
    month = mo.group(4)
    year = mo.group(6)
    after = mo.group(7)

    # Form the American-style filename.
    american_files = before + month + '-' + day + '-' + year + after

    # Get the full, absolute file paths.
    abs_work_dir = os.path.abspath('.')
    american_files = os.path.join(abs_work_dir, american_files)
    euro_files = os.path.join(abs_work_dir, euro_files)

    # Print out the renaming details.
    print(f"Renaming '{euro_files}' to '{american_files}'...")

    # Uncomment the line below to actually rename the files after testing.
    shutil.move(euro_files, american_files)
