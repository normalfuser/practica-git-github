"""Calcula la mitjana aritmètica d'una llista de notes."""


def mitjana(notes):
    if not notes:
        raise ValueError("Cal introduir almenys una nota.")
    return sum(notes) / len(notes)


if __name__ == "__main__":
    print(mitjana([7, 8, 9]))
