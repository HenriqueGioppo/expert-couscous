#code population groth expected in x years using geometric growth

def popGroth():
    #input
    print("This program calculates the population growth in x years/n")
    print("Enter the following information:")
    pop = int(input("Enter the current population: "))
    rate = float(input("Enter the annual growth rate in %: "))
    years = int(input("Enter the number of years: "))
    #process
    rate = rate / 100
    for i in range(years):
        pop = pop + (pop * rate)
    #output
    #round pop to the nearest whole number
    pop = round(pop)
    print("The population in", years, "years will be", pop)

    #user input


popGroth()