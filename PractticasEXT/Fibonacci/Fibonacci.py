
class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        difference = index - (len(self.sequence) - 2)
        if difference >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


def main():
    print(
        "Serie Fobonacci usando Programacion Dinamica\n",
        sep="",
    )
    
    fibonacci = Fibonacci()

    while True:
        serie: str = input(">> ")
        if serie in {"exit", "quit"}:
            break

        try:
            index: int = int(serie)
        except ValueError:
            print("Enter a number or 'exit'")
            continue

        print(fibonacci.get(index))


if __name__ == "__main__":
    main()