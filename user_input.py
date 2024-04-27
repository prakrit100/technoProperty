def get_user_choice():
    while True:
        choice = input("Enter 'rent' to rent land, 'return' to return land, or 'exit' to quit: ").lower()
        if choice in ['rent', 'return', 'exit']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_customer_name():
    return input("Enter customer name: ")

def get_kitta_numbers_to_rent():
    kitta_numbers = input("Enter kitta number(s) to rent (separated by commas): ").split(',')
    kitta_numbers = [number.strip() for number in kitta_numbers]
    return kitta_numbers

def get_kitta_numbers_to_return():
    kitta_numbers = input("Enter kitta number(s) to return (separated by commas): ").split(',')
    kitta_numbers = [number.strip() for number in kitta_numbers]
    return kitta_numbers

def get_rental_duration():
    while True:
        try:
            duration = int(input("Enter rental duration in months: "))
            if duration > 0:
                return duration
            else:
                print("Rental duration must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
        