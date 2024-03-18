"""API
======
"""

import logging

import keyring
from keyring.errors import NoKeyringError

logger = logging.getLogger(__name__)
KEYRING = keyring.get_keyring()


def get_api_key(
    service_name: str = "codestats",
    user_name: str = "localhost",
) -> str:
    """Get API key.

    :param service_name:
    :type service_name: str
    :param user_name:
    :type user_name: str
    :rtype: str
    """
    try:
        password = KEYRING.get_password(service_name, user_name)
    except NoKeyringError:
        logger.error("no installed backend!")
        return ""
    if not password:
        logger.error(service_name + "/" + user_name + "has no password!")
        return ""
    return password
