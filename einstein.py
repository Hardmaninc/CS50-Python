def calculate_energy(mass_kg):
    speed_of_light = 300000000
    joules = mass_kg * speed_of_light ** 2
    return int(joules)

def main():
    mass_kg = int(input("M: "))
    joules = calculate_energy(mass_kg)
    print("E:" ,joules)

if __name__ == "__main__":
    main()
