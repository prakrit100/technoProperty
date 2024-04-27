load land data from file
display available lands

while not exit:
    choice = get user choice (rent or return land)
    if choice == 'rent':
        customer_name = get customer name
        kitta_numbers = get kitta numbers to rent
        if kitta_numbers are available:
            duration = get rental duration
            total_rent = calculate total rent
            generate rent invoice
            update land status to 'Not Available'
    elif choice == 'return':
        customer_name = get customer name
        kitta_numbers = get kitta numbers to return
        if customer had rented these kitta_numbers:
            duration = get rental duration
            total_rent = calculate total rent (including fines, if any)
            generate return invoice
            update land status to 'Available'
    else:
        display invalid choice message
        