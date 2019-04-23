import os


def load_config():
    """
    Load app configuration from ENV vars into a dictionary.

    Returns:
        dict: Dictionary of configuration options and values.
    """
    cfg = {
        'DEBUG': os.environ.get('FLASK_DEBUG', True),
        'SECRET_KEY': os.environ.get('FLASK_SECRET_KEY', 'abcdef123456'),
    }

    return cfg
