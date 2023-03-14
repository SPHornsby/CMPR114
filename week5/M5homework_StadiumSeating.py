
CLASS_A_SEATING_COST = 20
CLASS_B_SEATING_COST = 15
CLASS_C_SEATING_COST = 10

def get_inputs() -> list:
    seat_classes = ['A', 'B', 'C']
    seats_sold = []
    for seat_class in seat_classes:
        seats_sold.append(int(input(f'How many class {seat_class} seats were sold? ')))
    return seats_sold
        
def calculate_total_ticket_sales(seats_sold: list) -> int:
    acc = 0
    for i in range(len(seats_sold)):
        acc += seats_sold[i] * (20 - (5*i))
    return acc

def display_ticket_sales(ticket_sales: int) -> None:
    print(f'Total ticket sales was {format_cash(ticket_sales)}.')

def format_cash(value: float) -> str:
    return '${:,.2f}'.format(value)

def main() -> None:
    """Asks user to input how many tickets of each class were sold
    and then calculates and displays the total sales."""
    seats_sold = get_inputs()
    ticket_sales = calculate_total_ticket_sales(seats_sold)
    display_ticket_sales(ticket_sales)
    

if __name__ == '__main__':
    main()