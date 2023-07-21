import argparse
import user
import admin
from user import register_user

# Sample data for categories and products (You can replace this with actual data from a database or data file)
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

    args = parser.parse_args()
    print("")
    email=input("enter your mail: ")
    password= input("password: ")
    

# Sample user data (You can get this from the user through the CLI)
    user_data = {
        'name': email,
        'email': password
        }

# Call the register_user function with the user_data
    register_user(user_data)


    if args.view_categories:
        view_categories()
    elif args.view_products:
        view_products(args.view_products)
    elif args.view_product_details:
        view_product_details(args.view_product_details)
    else:
        print("Please provide a valid option.")

if __name__ == "__main__":
    main()
