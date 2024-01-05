import os

PATH = "/home/savvyhex/Tools/gi-gen"

def main():
    print("Welcome to the gitignore generator!")
    search = input("Enter the language for the gitignore you want : ").lower()
    if search not in list_files():
        print(f"Unrecognized language : {search}")
    data = ""
    with open(f"{PATH}/{search.capitalize()}.gitignore") as f:
        data = f.read()
    with open(".gitignore", "w") as f:
        f.write(data)

def list_files():
    files = []
    for file in os.listdir(PATH):
        if file.endswith(".gitignore"):
            files.append(file)
    return list(map(lambda x : x.split('.')[0], list(map(str.lower, files))))

if __name__ == "__main__":
    main()