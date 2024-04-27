import os

def read_land_data():
    land_data = []
    with open('data.txt', 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            land_data.append({'kitta_number': data[0], 'city': data[1], 'direction': data[2], 'anna': int(data[3]), 'price': int(data[4]), 'status': data[5]})
    return land_data

def display_available_lands(land_data):
    print("Available lands:")
    for land in land_data:
        if land['status'] == 'Available':
            print(f"Kitta Number: {land['kitta_number']}, City: {land['city']}, Direction: {land['direction']}, Anna: {land['anna']}, Price: {land['price']}")

def check_land_availability(land_data, kitta_numbers):
    for kitta_number in kitta_numbers:
        for land in land_data:
            if land['kitta_number'] == kitta_number and land['status'] == 'Not Available':
                return False
    return True

def calculate_total_rent(land_data, kitta_numbers, rental_duration):
    total_rent = 0
    for kitta_number in kitta_numbers:
        for land in land_data:
            if land['kitta_number'] == kitta_number:
                total_rent += land['price'] * rental_duration
    return total_rent

def generate_rent_invoice(customer_namers, rental_duratioe, kitta_numbn, total_rent):
    invoice_filename = f"invoices/rent_invoice_{customer_name}.txt"
    os.makedirs('invoices', exist_ok=True) 
    with open(invoice_filename, 'w') as file:
        file.write(f"Rent Invoice for {customer_name}\n\n")
        file.write("Kitta Numbers: " + ", ".join(kitta_numbers) + "\n")
        file.write(f"Rental Duration: {rental_duration} months\n")
        file.write(f"Total Rent: NPR {total_rent}\n")

def update_land_status(land_data, kitta_numbers, status):
    with open('data.txt', 'w') as file:
        for land in land_data:
            if land['kitta_number'] in kitta_numbers:
                land['status'] = status
            file.write(f"{land['kitta_number']}, {land['city']}, {land['direction']}, {land['anna']}, {land['price']}, {land['status']}\n")

def check_customer_rented_land(customer_name, kitta_numbers):
    # Implement logic to check if the customer had rented the provided kitta_numbers
    # You can access the previously generated rent invoices or maintain a separate record
    return True  # Assuming the customer had rented the land for now

def calculate_total_rent_and_fine(land_data, kitta_numbers, rental_duration):
    total_rent = calculate_total_rent(land_data, kitta_numbers, rental_duration)
    fine = 0  # Implement logic to calculate fine based on rental_duration and other factors
    return total_rent, fine

def generate_return_invoice(customer_name, kitta_numbers, rental_duration, total_rent, fine):
    invoice_filename = f"invoices/return_invoice_{customer_name}.txt"
    os.makedirs('invoices', exist_ok=True) 
    with open(invoice_filename, 'w') as file:
        file.write(f"Return Invoice for {customer_name}\n\n")
        file.write("Kitta Numbers: " + ", ".join(kitta_numbers) + "\n")
        file.write(f"Rental Duration: {rental_duration} months\n")
        file.write(f"Total Rent: NPR {total_rent}\n")
        if fine > 0:
            file.write(f"Fine: NPR {fine}\n")
            file.write(f"Total Amount: NPR {total_rent + fine}\n")


