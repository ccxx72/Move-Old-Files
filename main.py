import os
from datetime import datetime
import shutil

source = "X:\\"
destination = source + "\\OLD"


def copyfile(path, filename):
    fromfile = path + "\\" + filename
    tofile = destination + path[2:] + "\\" + filename
    print("Copio in " + tofile)
    if os.path.exists(destination + path[2:]):  # se la cartella esiste
        shutil.move(fromfile, tofile)
        print("\n")
    else:
        print(destination + path[2:] + " NON ESISTE")
        print("\n")
        os.makedirs(destination + path[2:])
        shutil.move(fromfile, tofile)


def main():
    for r, d, f in os.walk(source):
        for file in f:
            info = os.stat(r + "\\" + file)
            print(f"{r + file}")  # r contiene il percorso, file contiene il nomefile
            print(info.st_mtime)  # dataora ultima modifica in timestamp
            date_time_obj = datetime.strptime('2016-12-31 23:59:00.0', '%Y-%m-%d %H:%M:%S.%f')  # conversione data limite in timestamp
            print(datetime.fromtimestamp(info.st_mtime))  # conversione della data di ultima modifica da timestamp in formato leggibile
            if info.st_mtime < datetime.timestamp(date_time_obj):
                copyfile(r, file)
            else:
                print("\n")


if __name__ == "__main__":
    main()
