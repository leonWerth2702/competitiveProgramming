class Points:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


n = int(input())
sum_of_coordinates = Points()
for i in range(n):
    x_point, y_point, z_point = map(int, input().split())
    current_coordinates = Points(x_point, y_point, z_point)
    sum_of_coordinates.x += current_coordinates.x
    sum_of_coordinates.y += current_coordinates.y
    sum_of_coordinates.z += current_coordinates.z

if sum_of_coordinates.x == 0 and sum_of_coordinates.y == 0 and sum_of_coordinates.z == 0:
    print("YES")
else:
    print("NO")

