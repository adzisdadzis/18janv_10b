def ierakstit_faila(lietotaja_vards):
    try:
        with open("lietotaja_vards.txt", 'w') as faila_objekts:
            faila_objekts.write(lietotaja_vards)
        print("Veiksmīgi ievadīts.")
    except KeyError as k:
        print(f"Kļūda: Nevar ierakstīt failu. {k}")

def main():
    try:
        lietotaja_vards = input("Ievadiet savu vārdu: ")
        ierakstit_faila(lietotaja_vards)

    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    main()