"""
Utility methods.
"""
from constants import ADMIN_GROUP_NAME


def is_admin(user):
    """
    Check if given user is an admin.
    """
    return user.groups.filter(name=ADMIN_GROUP_NAME).exists()
