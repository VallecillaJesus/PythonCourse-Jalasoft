import os

def generate_file(path, filename, content):
    foldername = filename.replace('log_','')[:8]
    target = path + foldername + '\\' + filename

    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as file:
        file.write(content)