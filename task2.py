import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()

def main():
    try:
        # Запит користувача про рівень рекурсії
        level = int(input("Введіть рівень рекурсії для фракталу Коха: "))
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути не від'ємним числом.")
        
        # Виклик функції з введеним рівнем рекурсії
        draw_koch_curve(level)
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()