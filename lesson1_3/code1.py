from turtle import circle


class Point:
    color = 'red'
    circle = 2

    def set_coords(self):
        print(f"Call fucn set_coords = D {str(self)}")

x = Point()
x.set_coords()
