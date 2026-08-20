# Model
def get_user():
    # Simulated database
    user = {
        "id": 101,
        "name": "John",
        "email": "john@gmail.com"
    }
    return user


# View
def display_user(user):
    print("\n----- User Details -----")
    print("ID    :", user["id"])
    print("Name  :", user["name"])
    print("Email :", user["email"])


# Controller
def controller():
    print("Request received by Controller")

    # Controller calls Model
    user = get_user()

    # Controller sends data to View
    display_user(user)


# Main program
print("User sends request")
print("HTTP Request received by Web Server")

controller()

print("\nHTTP Response sent to User")