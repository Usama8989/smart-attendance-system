def authenticate_fingerprint(user_id):
    print(f"Place your finger for user: {user_id}")
    fingerprint_id = input("Enter simulated fingerprint ID: ")
    if fingerprint_id == user_id:
        return True
    return False
