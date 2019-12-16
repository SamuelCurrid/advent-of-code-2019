def fuelCalculation(mass: int):
    """
    Calculates fuel needed based on mass

    :param mass: mass of fuel/module
    :return: mass of fuel required to lift passed mass
    """
    return mass // 3.0 - 2

def totalFuelCalculation(mass: int):
    """
    Calculates total fuel needed based on mass (including fuel needed for fuel)

    :param mass: mass of fuel/module
    :return:  mass of fuel required to lift passed mass plus additional fuel
    """
    requiredFuel = 0
    mass = fuelCalculation(mass)

    while mass > 0:
        requiredFuel += mass
        mass = fuelCalculation(mass)

    return requiredFuel


part1Fuel = 0
part2Fuel = 0

with open("input.txt") as modules:
    for mass in modules:
        part1Fuel += fuelCalculation(int(mass))
        part2Fuel += totalFuelCalculation(int(mass))

print("Part 1: " + str(part1Fuel))
print("Part 2: " + str(part2Fuel))