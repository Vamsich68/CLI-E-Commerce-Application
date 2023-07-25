class Admin:
    def __init__(self, admin_id, username, password):
        self.admin_id = admin_id
        self.username = username
        self.password = password

# List to store admin users 
admin_users = [Admin(admin_id=1, username="admin", password="password")]

def admin_login(username, password):
    # Check if the admin with the given username and password exists
    admin = next((admin for admin in admin_users if admin.username == username and admin.password == password), None)
    admin_user = None
    for admin in admin_users:
        if (admin.username == username and admin.password == password):
            admin_user=admin
            break
    if admin:
        print("Admin login successful.")
        return admin
    else:
        print("Invalid admin credentials.")
        return None

def add_category(category_name):
    # Generate a unique category ID 
    category_id = len(categories) + 1

    # Add the new category to the categories dictionary
    categories[category_id] = category_name

    print(f"Category '{category_name}' added with ID: {category_id}")

def add_product(category_id, product_name, price):
    # Check if the category_id exists in the categories dictionary
    if category_id not in categories:
        print("Category not found.")
        return

    # Generate a unique product ID 
    product_id = len(products) + 1

    # Add the new product to the products dictionary
    products[product_id] = {"name": product_name, "category_id": category_id, "price": price}

    print(f"Product '{product_name}' added with ID: {product_id}")
