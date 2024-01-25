import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    try:
        # Запит користувача про рівень рекурсії
        level = int(input("Введіть рівень рекурсії для фракталу Коха: "))
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути не від'ємним числом.")
        
        # Виклик функції з введеним рівнем рекурсії
        draw_koch_snowflake(level)
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
