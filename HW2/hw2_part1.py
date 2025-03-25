from math import ceil, pi

def find_volume_sphere(radius):
    return (4/3) * pi * (radius ** 3)

def find_volume_cube(side):
    return side ** 3

if __name__ == "__main__":
    # Input
    radius = float(input("Enter the gum ball radius (in.) => ")) 
    print(radius)

    weekly_sales  = int(input("Enter the weekly sales => "))
    print(weekly_sales )
    print()

    # Calculate values needed for output
    target_gumballs = ceil(1.25 * weekly_sales )
    gumballs_edge = ceil(target_gumballs ** (1/3))
    total_gumballs = gumballs_edge ** 3
    side_length = gumballs_edge * 2 * radius

    # Calculate volumes
    cube = find_volume_cube(side_length)
    sphere = find_volume_sphere(radius)
    
    # Wasted space calculations
    wasted_target = cube - (target_gumballs * sphere)
    wasted_total = cube - (total_gumballs * sphere)

    print("The machine needs to hold",gumballs_edge, "gum balls along each edge.")
    print("Total edge length is {0:.2f} inches.".format(side_length))
    print("Target sales were " + str(target_gumballs)+", but the machine will hold",total_gumballs - target_gumballs,"extra gum balls.")
    print("Wasted space is {0:.2f} cubic inches with the target number of gum balls,".format(wasted_target))
    print("or {0:.2f} cubic inches if you fill up the machine.".format(wasted_total))

