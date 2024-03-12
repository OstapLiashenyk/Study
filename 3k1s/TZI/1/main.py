class LinearCongruentialGenerator:
    def __init__(self, seed=None):
        if seed is None:
            seed = 7  # вказуємо вручну X0
        self.state = seed

    def generate(self):
        a = 10**3
        c = 377
        m = 2**23 - 1
        self.state = (a * self.state + c) % m
        return self.state

def main():
    try:
        n = int(input("Введіть кількість псевдовипадкових чисел: "))
        filename = input("Введіть ім'я файлу для зберігання результатів: ") or "n.txt"

        random_generator = LinearCongruentialGenerator()

        with open(filename, 'w') as file:
            for _ in range(n):
                random_number = random_generator.generate()
                print(random_number)
                file.write(str(random_number) + '\n')

        print(f"Результати збережено у файлі: {filename}")

    except ValueError:
        print("Будь ласка, введіть правильне ціле число для кількості псевдовипадкових чисел.")
    n = int(input("Перевірити період?(1/0)"))
    if n == 1 :
        generator = LinearCongruentialGenerator()
        counter = 1
        run = generator.generate()
        first = run
        print(first)
        while run != first:
            run = generator.generate()
            counter+=1
        print(counter)
if __name__ == "__main__":
    main()
