import math


def square(side: float) -> float:
    """
    Calculate the area of a square.

    Parameters:
        side (float): The length of one side of the square.

    Returns:
        float: The area of the square.
    """
    return side * side


def rectangle(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    """
    return (base * height) / 2


def scalene_triangle(first_side: float, second_side: float, third_side: float) -> float:
    """
        Calculates the area of a scalene triangle given the lengths of its three sides.

        Args:
            first_side (float): The length of the first side of the triangle.
            second_side (float): The length of the second side of the triangle.
            third_side (float): The length of the third side of the triangle.

        Returns:
            float: The area of the scalene triangle.
    """
    semiperimeter = (first_side + second_side + third_side) / 2
    return math.sqrt((semiperimeter * (semiperimeter - first_side) * (semiperimeter - second_side) * (semiperimeter - third_side)))


def circle(radius: float) -> float:
    """
    Calculate the area of a circle based on the given radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle rounded to 2 decimal places.
    """
    return round(math.pi * radius * radius, 2)


def area():
    print("\nHere are the available figures: Square, Rectangle, Triangle, Circle")
    figure = input(
        "Please, Type the figure you want to calculate the area of: ")

    if figure.lower() == "square":
        side = float(input("Type the side of the square: "))
        print(f"The area of the square is {square(side)}")
    elif figure.lower() == "rectangle":
        length = float(input("Type the length of the rectangle: "))
        width = float(input("Type the width of the rectangle: "))
        print(f"The area of the rectangle is {rectangle(length, width)}")
    elif figure.lower() == "triangle":
        triangle_list = ["Square", "Rectangle", "Triangle", "Scalene"]
        print(f"Here are the following options: {', '.join(triangle_list)}")
        triangle_choice = input("Type the base of the triangle: ")
        while triangle_choice.lower() not in triangle_choice:
            triangle_choice = input(
                f"This is not a valid option !!!\nTry again using one of the following options [{', '.join(triangle_list)}] : ")
        if triangle_choice.lower() == "scalene":
            first_side = float(input("Type the first side of the triangle: "))
            second_side = float(
                input("Type the second side of the triangle: "))
            third_side = float(input("Type the third side of the triangle: "))
            print(
                f"The area of the scalene triangle is {scalene_triangle(first_side, second_side, third_side)}")
        else:
            base = float(input("Type the base of the triangle: "))
            height = float(input("Type the height of the triangle: "))
            print(f"The area of the triangle is {triangle(base, height)}")
    elif figure.lower() == "circle":
        radius = float(input("Type the radius of the circle: "))
        print(f"The area of the circle is {circle(radius)}")
    else:
        print("This is not a valid figure")
        area()


def main():
    print("".center(80, "*"))
    print("Welcome to the area calculator!".center(80, "*"))
    print("".center(80, "*")+"\n")
    area()


if __name__ == "__main__":
    main()
