import land_management
import user_input

def main():
    land_data = land_management.read_land_data()

    while True:
        land_management.display_available_lands(land_data)
        choice = user_input.get_user_choice()

        if choice == 'rent':
            customer_name = user_input.get_customer_name()
            kitta_numbers = user_input.get_kitta_numbers_to_rent()
            rental_duration = user_input.get_rental_duration()

            if land_management.check_land_availability(land_data, kitta_numbers):
                total_rent = land_management.calculate_total_rent(land_data, kitta_numbers, rental_duration)
                land_management.generate_rent_invoice(customer_name, kitta_numbers, rental_duration, total_rent)
                land_management.update_land_status(land_data, kitta_numbers, 'Not Available')

        elif choice == 'return':
            customer_name = user_input.get_customer_name()
            kitta_numbers = user_input.get_kitta_numbers_to_return()

            if land_management.check_customer_rented_land(customer_name, kitta_numbers):
                rental_duration = user_input.get_rental_duration()
                total_rent, fine = land_management.calculate_total_rent_and_fine(land_data, kitta_numbers, rental_duration)
                land_management.generate_return_invoice(customer_name, kitta_numbers, rental_duration, total_rent, fine)
                land_management.update_land_status(land_data, kitta_numbers, 'Available')

        elif choice == 'exit':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()




