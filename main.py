import os
from datetime import datetime
import shutil

source = "O:\\"
destination = "A:"
file_log = open("LOG.txt", "w", encoding="utf-8")


def copyfile(path, filename):
    fromfile = path + "\\" + filename
    tofile = destination + path[2:] + "\\" + filename

    if os.path.exists(destination + path[2:]):  # se la cartella esiste
        try:
            shutil.move(fromfile, tofile)
            file_log.write("Copio in " + tofile)
            print("Copio in " + tofile)
        except PermissionError:
            file_log.write("NON TRATTATO " + path + "\\" + filename)
            print("NON TRATTATO " + path + "\\" + filename)
        except OSError:
            file_log.write("NON TRATTATO " + path + "\\" + filename)
            print("NON TRATTATO " + path + "\\" + filename)

    else:
        file_log.write("NON ESISTE " + destination + path[2:])
        print("NON ESISTE " + destination + path[2:])
        try:
            os.makedirs(destination + path[2:])
            print("Creo " + destination + path[2:])
            file_log.write("Creo " + destination + path[2:])
            shutil.move(fromfile, tofile)
            print("Copio in " + tofile)
            file_log.write("Copio in " + tofile)
        except PermissionError:
            file_log.write("NON TRATTATO " + path + "\\" + filename)
            print("NON TRATTATO " + path + "\\" + filename)
        except OSError:
            file_log.write("NON TRATTATO " + path + "\\" + filename)
            print("NON TRATTATO " + path + "\\" + filename)


def main():

    for r, d, f in os.walk(source):
        for file in f:
            try:
                info = os.stat(r + "\\" + file)
            except PermissionError:
                file_log.write("NON TRATTATO " + r + "\\" + file)
                print("NON TRATTATO " + r + "\\" + file)
            except OSError:
                file_log.write("NON TRATTATO " + r + "\\" + file)
                print("NON TRATTATO " + r + "\\" + file)
            else:
                print(r + "\\" + file)
                file_log.write(r + "\\" + file)  # r contiene il percorso, file contiene il nomefile
                file_log.write(str(info.st_atime))  # dataora ultimo accesso in timestamp
                date_time_obj = datetime.strptime('2016-12-31 23:59:00.0', '%Y-%m-%d %H:%M:%S.%f')  # conversione data limite in timestamp
                file_log.write(str(datetime.fromtimestamp(info.st_mtime)))  # conversione della data di ultima modifica da timestamp in formato leggibile
                if info.st_mtime < datetime.timestamp(date_time_obj):
                    copyfile(r, file)
                    print("**********************************************************************************/n")
                #  else:
    file_log.close()


if __name__ == "__main__":
    main()
