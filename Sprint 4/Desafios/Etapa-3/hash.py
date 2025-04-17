import hashlib


def main():
    while True:
        entrada = input("Digite uma palavra (ou '0' para sair): ")

        if entrada.lower() == "0":
            print("Encerrando o programa...")
            break

        sha1_hash = hashlib.sha1(entrada.encode()).hexdigest()

        print(f"Hash SHA-1 da string '{entrada}': {sha1_hash}")


if __name__ == "__main__":
    main()
