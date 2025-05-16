# utils/helpers.py

def validate_user_schema(user_data):
    """
    Schema validation for a user object.
    """
    expected_keys = {"id", "email", "first_name", "last_name", "avatar"}
    return expected_keys.issubset(set(user_data.keys()))
