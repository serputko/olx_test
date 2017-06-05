import configparser


def get_valid_credentials():
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    credentials = {'User': config['valid_olx.ua']['User'], 'Password': config['valid_olx.ua']['Password']}
    return credentials
