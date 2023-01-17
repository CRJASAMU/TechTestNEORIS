import configparser
def ObtenerConfiguraciones():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    return config
    