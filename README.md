# A collection of `.gitignore` templates

This is GitHub’s collection of [`.gitignore`][man] file templates.
We use this list to populate the `.gitignore` template choosers available
in the GitHub.com interface when creating new repositories and files.

# Usage
Run the `gi-gen.py` file in your github project. This will run the generator
wizard, allowing you to generate a `.gitignore` file for your desired
language.

# Known issues
The script only works with files in the main folder of the project. This
means that it will not work for files in the `community` or `Global`
folders.