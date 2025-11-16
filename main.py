from products import Product
from store import Store


product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start():
    """main function for starting the program"""
    print("""1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")

    while True:
        user_input = input("Please choose a number: ")


        if user_input == "1":
            for product in best_buy.get_all_products():
                product.show()

        elif user_input == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")


        elif user_input == "3":

            # Get current active products

            products = best_buy.get_all_products()

            # Print numbered list

            print("------")

            number = 1

            for product in products:
                print(f"{number}. ", end="")

                product.show()

                number += 1

            print("------")

            shopping_list = []

            while True:

                print("When you want to finish order enter empty text.")

                product_choice = input("Which product # do you want? ")

                # Finish order if user presses Enter

                if product_choice == "":

                    if not shopping_list:
                        print("No products selected. Order cancelled.")

                        break

                    total = best_buy.order(shopping_list)

                    print("********")

                    print(f"Order made! Total payment: ${total}")

                    break  # go back to main menu

                # Validate product number

                if not product_choice.isdigit():
                    print("Please enter a valid number.")

                    continue

                product_index = int(product_choice) - 1

                if product_index < 0 or product_index >= len(products):
                    print("Invalid product number, try again.")

                    continue

                # Ask for quantity

                quantity_str = input("What amount do you want? ")

                if not quantity_str.isdigit():
                    print("Please enter a valid quantity.")

                    continue

                quantity = int(quantity_str)

                # Add (Product, quantity) tuple to shopping_list

                chosen_product = products[product_index]

                shopping_list.append((chosen_product, quantity))

                print("Product added to the list!")


        elif user_input == "4":

            print("Goodbye!")

            break


        else:

            print("Invalid choice, try again.")

start()
