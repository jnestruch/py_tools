import os.path
import shutil
import codecs
from pathlib import Path

file1 = codecs.open("/TEMP/temp.csv","a","utf-8")

#Read file path from console
print("Directorio con ficheros:")
sDir = str(input())

print("\nDirectorio:\n{}".format(sDir))
print(Path(sDir).is_dir())

cDir = Path(sDir)
for cFile in cDir.iterdir():
    print("\nProcesando fichero: {}".format(cFile))
    with codecs.open(cFile,"r","utf-8") as ficherin:
        for line in ficherin:
            file1.write(line)
        ficherin = []

file1.close()