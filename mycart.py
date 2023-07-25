import argparse
import user
import admin
from user import register_user, login_user

# Sample data for categories and products
categories = {
    1: "Electronics",
    2: "Clothing",
    3: "Books",
}

products = {
    1: {"name": "Laptop", "category_id": 1, "price": 50000},
    2: {"name": "T-Shirt", "category_id": 2, "price": 800},
    3: {"name": "Python Crash Course", "category_id": 3, "price": 500},
    4: {"name": "mobile", "category_id": 1, "price": 10000}
}

def view_categories():
    print("Available Categories:")
    for category_id, category_name in categories.items():
        print(f"{category_id}: {category_name}")

def view_products(category_id):
    print(f"Products under {categories[category_id]}:")
    for product_id, product in products.items():
        if product["category_id"] == category_id:
            print(f"{product_id}: {product['name']} - Rs. {product['price']}")

def view_product_details(product_id):
    if product_id in products:
        product = products[product_id]
        print(f"Product Details:")
        print(f"Name: {product['name']}")
        print(f"Category: {categories[product['category_id']]}")
        print(f"Price: Rs. {product['price']}")
    else:
        print("Product not found!")

def main():
    parser = argparse.ArgumentParser(description="MyCart - CLI E-commerce App")

    parser.add_argument("--view_categories", action="store_true", help="View all categories")
    parser.add_argument("--view_products", type=int, help="View products under a category (provide category ID)")
    parser.add_argument("--view_product_details", type=int, help="View product details (provide product ID)")

    # args = parser.parse_args()



    # Add arguments for user-related functionalities
    parser.add_argument("--register_user", action="store_true", help="Register a new user")
    parser.add_argument("--login", action="store_true", help="Login with user's email")
    parser.add_argument("--name", type=str, help="User's name")
    parser.add_argument("--email", type=str, help="User's email")

    args = parser.parse_args()

    # Handle the parsed arguments accordingly
    if args.register_user:
    # Handle user registration using the provided name and email arguments
        if args.name and args.email:
            user_data = {
                'name': args.name,
                'email': args.email
            }
            register_user(user_data)
        else:
            print("Please provide both name and email for user registration.")
    else:
        print("Please provide a valid option.")
    if args.login:
        if args.email:
            logged_in_user = login_user(args.email)
            if logged_in_user:
            # If the user login is successful, you can continue with other functionalities for the user.
                pass
        else:
            print("Please provide the email for user login.")
    else:
        print("Please provide a valid option.")

#     print("")
#     email=input("enter your mail: ")
#     password= input("password: ")
    

# # Sample user data (You can get this from the user through the CLI)
#     user_data = {
#         'name': email,
#         'email': password
#         }

# # Call the register_user function with the user_data
#     register_user(user_data)


    # if args.view_categories:
    #     view_categories()
    # elif args.view_products:
    #     view_products(args.view_products)
    # elif args.view_product_details:
    #     view_product_details(args.view_product_details)
    # else:
    #     print("Please provide a valid option.")

if __name__ == "__main__":
    main()
