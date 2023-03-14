
def get_cost_parts() -> list:
    part_names = ['loan payment','insurance','gas','oil','tires', 'maintenance']
    part_costs = []
    for name in part_names:
        cost = float(input(f'What is the monthly cost of the {name}? '))
        part_costs.append(cost)
    return part_costs

def get_cost_total(part_costs: list) -> float:
    return sum(part_costs)

def display_total_cost(total_cost: float) -> None:
    print(f'The total monthly cost of your automobile\'s cost is: {total_cost}')

def main() -> None:
    """Asks user to enter montly cost parts and calculates the total monthly cost."""
    display_total_cost(get_cost_total(get_cost_parts()))

if __name__ == '__main__':
    main()