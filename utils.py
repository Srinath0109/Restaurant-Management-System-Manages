def validate_menu_item(data):
    """Validates menu item data."""
    required_fields = ["name", "price"]
    for field in required_fields:
        if field not in data:
            return False
    return True
