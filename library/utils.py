def is_admin(user):
    """
    Check if the user is an admin.

    Args:
        user: The user object to check.

    Returns:
        True if the user is an admin, False otherwise.
    """
    return user.is_superuser
