#kā nolasīt datens saturu?
def lasīt_datni():
    try:
        #Datnes satura ielāde
        with open('darbs.txt',"r",encoding='utf-8') as datne:
            saturs=datne.read(100)
            print(saturs)
    except FileNotFoundError:
        print("Datne nav atrasta")


if __name__=="__main__":
    lasīt_datni()