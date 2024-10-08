import math

# Storing the coordinates
points = [(0, 1), (2, 4), (3, 6), (7, 7)]

# Function to calculate the distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Example usage
distance = calculate_distance(points[0], points[1])
print(f"Distance between {points[0]} and {points[1]}: {distance}")

def to_polar(point):
    r = math.sqrt(point[0]**2 + point[1]**2)
    theta = math.atan2(point[1], point[0])  # Angle in radians
    return (r, math.degrees(theta))  # Convert angle to degrees for readability

# Example usage
polar_coords = to_polar(points[2])
print(f"Polar coordinates of {points[2]}: {polar_coords}")

def move_point(point, dx, dy):
    new_x = point[0] + dx
    new_y = point[1] + dy
    return (new_x, new_y)

# Example usage
new_position = move_point(points[3], 3, -1)
print(f"New position of {points[3]} after moving by (3, -1): {new_position}")
