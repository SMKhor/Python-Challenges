print("Physics Formula Application")
print("Make sure all the units are already in the appropriate format and units.")
print("speed (m/s) = distance (m)/time (s) is 1")
print("force (N) = mass (kg) x acceleration (ms^-2) is 2")
print("force (N) = spring constant (Nm^-1) x extension (m) is 3")
print("pressure (Pa) = force (N)/area (m^2) is 4")
print("density (kgm^-3) = mass (kg)/volume (m^3) is 5")
formula = input("\nEnter the number of the formula you'd like to use: ")

if formula == "1":
    print("\nspeed (1) = distance (2)/time (3)")
    variable = input("Enter the variable you're calculating for: ")
    if variable == "1":
        d = float(input("Distance: "))
        t = float(input("Time: "))
        speed = d/t
        print("Speed:", speed, "ms^-1")
    if variable == "2":
        s = float(input("Speed: "))
        t = float(input("Time: "))
        distance = s * t
        print("Distance:", distance, "m")
    if variable == "3":
        s = float(input("Speed: "))
        d = float(input("Distance: "))
        time = d/s
        print("Time:", time, "s")


if formula == "2":
    print("\nforce (1) = mass (2) x acceleration (3)")
    variable = input("Enter the variable you're calculating for: ")
    if variable == "1":
        m = float(input("Mass: "))
        a = float(input("Acceleration: "))
        force = m * a
        print("Force:", force, "N")
    if variable == "2":
        f = float(input("Force: "))
        a = float(input("Acceleration: "))
        mass = f/a
        print("Mass:", mass, "kg")
    if variable == "3":
        f = float(input("Force: "))
        m = float(input("Mass: "))
        acceleration = f/m
        print("Acceleration:", acceleration, "ms^-2")



if formula == "3":
    print("\nforce (1) = spring constant (2) x extension (3)")
    variable = input("Enter the variable you're calculating for: ")
    if variable == "1":
        k = float(input("Spring constant: "))
        e = float(input("Extension: "))
        force = k * e
        print("Force:", force, "N")
    if variable == "2":
        f = float(input("Force: "))
        e = float(input("Extension: "))
        k = f/e
        print("Spring constant:", k, "Nm^-1")
    if variable == "3":
        f = float(input("Force: "))
        k = float(input("Spring constant: "))
        e = f/k
        print("Extension:", e, "m")

if formula == "4":
    print("\npressure (1) = force (2)/area (3)")
    variable = input("Enter the variable you're calculating for: ")
    if variable == "1":
        f = float(input("Force: "))
        a = float(input("Area: "))
        pressure = f/a
        print("Pressure:", pressure, "Pa")
    if variable == "2":
        p = float(input("Pressure: "))
        a = float(input("Area: "))
        force = p * a
        print("Force:", force, "N")
    if variable == "3":
        p = float(input("Pressure: "))
        f = float(input("Force: "))
        area = f/p
        print("Area:", area, "m^2")


if formula == "5":
    print("\ndensity (1) = mass (2)/volume (3)")
    variable = input("Enter the variable you're calculating for: ")
    if variable == "1":
        m = float(input("Mass: "))
        v = float(input("Volume: "))
        density = m/v
        print("Density:", density, "kgm^-3")
    if variable == "2":
        d = float(input("Density: "))
        v = float(input("Volume: "))
        mass = d * v
        print("Mass:", mass, "kg")
    if variable == "3":
        d = float(input("Density: "))
        m = float(input("Mass: "))
        volume = m/d
        print("Volume:", volume, "m^3")

