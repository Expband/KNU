import cmath


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    if discriminant == 0 :
        print(f"x = {x1.real:.2f}")
    else:
        print(f"x1 = {x1.real:.2f}")
        print(f"x2 = {x2.real:.2f}")
    print(f"Discriminant = {discriminant.real:.2f}")


if __name__ == "__main__":
    a = float(input("Input a value: "))
    b = float(input("Input b value: "))
    c = float(input("Input c value: "))
    calculate(a, b, c)