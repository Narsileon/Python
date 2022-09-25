GROWTH_A = 0.005
GROWTH_B = 0.025

population_A = 60000000
population_B = 4000000

years = 0

def main():
    get_years(0.1)
    print("")
    get_years(1)

def get_years(threshold: float):
    global population_A, population_B, years

    while(population_B / population_A < threshold):
        years += 1
        
        population_A += population_A * GROWTH_A
        population_B += population_B * GROWTH_B

    display_result(threshold)

def display_result(threshold: float):
    print(
        "Anzahl der Jahre, bevor die Bevölkerung von Land B {} % der Bevölkerung von Land A erreicht: {}."
        .format("%.0f" % (threshold * 100), years)
    )
    print("- Bevölkerung A: {}M".format("%.2f" % (population_A / 1000000)))
    print("- Bevölkerung B: {}M".format("%.2f" % (population_B / 1000000)))
            
main()
