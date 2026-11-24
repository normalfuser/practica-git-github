"""Compta les paraules d'una frase."""


def compta_paraules(frase):
    return len(frase.split())


if __name__ == "__main__":
    print(compta_paraules("Practiquem Git amb Python"))
