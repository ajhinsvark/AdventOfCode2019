
class Point:

    def __init__(self, x, y):
        """Initialize a point"""
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        else:
            self.x *= other
            self.y *= other

    def __imul__(self, other):
        if isinstance(other, Point):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"



class Line:
    
    _CHAR_DIR_2_VECTOR = {
            "R": Point(1,0),
            "L": Point(-1,0),
            "U": Point(0,1),
            "D": Point(0,-1)
    }

    def __init__(self, start, direction, length):
        self.start = start
        self.direction = self._CHAR_DIR_2_VECTOR[direction]
        self.end = self.start + self.direction * length
        self.length = length
        self.slope = self._slope()

    def _slope(self):
        if self.end.x == self.start.x:
            return float('inf')
        else:
            return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def parallel_to(self, other):
        return self.slope == other.slope

    def __str__(self):
        return f"Line(start={self.start}, dir={self.direction * self.length})"


def intersection(line1, line2):
    if line1.parallel_to(line2):
        return None

    x1, y1 = line1.start.x, line1.start.y
    x2, y2 = line1.end.x, line1.end.y
    x3, y3 = line2.start.x, line2.start.y
    x4, y4 = line2.end.x, line2.end.y

    denom = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3)*(x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2)*(x1 - x3)) / denom

    if 0 <= t <= 1 and 0 <= u <= 1:
        return Point(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    else:
        return None


def manhattan_dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


if __name__ == "__main__":
    wires = []
    with open("input") as f:
        for line in f.readlines():
            wire = []
            cur_point = Point(0, 0)
            for command in line.strip().split(','):
                direction = command[0]
                length = int(command[1:])
                l = Line(cur_point, direction, length)
                wire.append(l)
                cur_point = Point(l.end.x, l.end.y)
            wires.append(wire)
    
    min_dist = float('inf')
    min_steps = float('inf')
    origin = Point(0,0)
    steps_wire1 = 0
    for line in wires[0]:
        steps_wire2 = 0
        for line2 in wires[1]:
            inter_p = intersection(line, line2)
            if inter_p is not None:
                dist = manhattan_dist(origin, inter_p)
                if dist < min_dist:
                    min_dist = dist
                step_dist = (steps_wire1 + manhattan_dist(line.start, inter_p) +
                             steps_wire2 + manhattan_dist(line2.start, inter_p))
                if step_dist < min_steps:
                    min_steps = step_dist
            steps_wire2 += line2.length
        steps_wire1 += line.length

    print(f"Min distance: {min_dist}")
    print(f"Min steps: {min_steps}")



    
