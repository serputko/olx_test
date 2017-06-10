import configparser


class Utils(object):
    def get_valid_credentials(self):
        config = configparser.ConfigParser()
        config.read('.\\behave_tests\credentials.ini')
        credentials = {'User': config['valid_olx.ua']['User'], 'Password': config['valid_olx.ua']['Password']}
        return credentials

    def get_invalid_credentials(self):
        config = configparser.ConfigParser()
        config.read('.\\behave_tests\credentials.ini')
        invalid_credentials = {'User': config['invalid_olx.ua']['User'],
                               'Password': config['invalid_olx.ua']['Password']}
        return invalid_credentials
