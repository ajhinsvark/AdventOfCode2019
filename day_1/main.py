

def get_fuel(mass):
    return (mass // 3) - 2


def get_fuel_recursive(mass):
    fuel = get_fuel(mass)

    if fuel <= 0:
        return 0
    
    return fuel + get_fuel_recursive(fuel)

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    numbers = []
    for line in lines:
        numbers.append(int(line.strip()))

    # Part 1
    fuels = [get_fuel(mass) for mass in numbers]

    print(sum(fuels))

    # Part 2

    fuels = [get_fuel_recursive(mass) for mass in numbers]

    print(sum(fuels))
