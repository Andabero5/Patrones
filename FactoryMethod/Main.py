from ShapeFactory import ShapeFactory


def main():
    while True:
        option = int(input(
            "Elija una opción para dibujar una figura\n1.Circulo\n2.Cuadrado\n3.Rectángulo\n"))
        if option == 1 or 2 or 3:
            print(ShapeFactory.getShape(option))
            break
        else:
            print("Escoja una opcion valida\n")


if __name__ == "__main__":
    main
