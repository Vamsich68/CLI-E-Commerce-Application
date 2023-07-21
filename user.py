class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.cart = {}  # Dictionary to store products in the cart (product_id: quantity)

# List to store registered users
registered_users = []

def register_user(user_data):
    # Check if the user with the same email already exists
    # Expanded version of finding an existing user based on the user's email
    existing_user = None
    for user in registered_users:
        if user.email == user_data['email']:
            existing_user = user
            break


    if existing_user:
        print("User with this email already exists.")
        return

    # Generate a unique user ID to identify users
    user_id = len(registered_users) + 1
    new_user = User(user_id, user_data['name'], user_data['email'])
    registered_users.append(new_user)

    print("User registration successful.")

def login_user(email):
    # Find the user by email in the registered_users list
    user = next((user for user in registered_users if user.email == email), None)

    if user:
        print("User login successful.")
        return user
    else:
        print("Invalid email. User not found.")
        return None
quantity=0
def add_to_cart(user, product_id, quantity):
    if product_id in user.cart:
        user.cart[product_id] += quantity
    else:
        user.cart[product_id] = quantity

    print(f"{quantity} {products[product_id]['name']} added to the cart.")

def remove_from_cart(user, product_id):
    if product_id in user.cart:
        del user.cart[product_id]
        print("Product removed from the cart.")
    else:
        print("Product not found in the cart.")

def view_cart(user):
    print("Your Cart:")
    for product_id, quantity in user.cart.items():
        product = products[product_id]
        print(f"{product['name']}, Quantity: {quantity}, Price: Rs. {product['price']}")

def calculate_total_amount(user):
    total_amount = 0
    for product_id, quantity in user.cart.items():
        product = products[product_id]
        total_amount += product['price'] * quantity
    print("total amount :", total_amount)
    return total_amount

def apply_discount(total_amount):
    if total_amount > 10000: #applying discount on orders which total amount more than 10000
        return total_amount - 500
    else:
        return total_amount

def generate_bill(user, total_amount, discounted_amount):
    # print("Generating Bill...")
    # print(f"User: {user.name} ({user.email})")
    # print("Items in the cart:")
    view_cart(user)
    print(f"Total Amount: Rs. {total_amount}")
    print(f"Discounted Amount: Rs. {discounted_amount}")
