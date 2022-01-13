def repeat(config_file_name):
    """Вывести повторенную count раз строку str (см. _legend.md)"""
    import configparser

    config = configparser.ConfigParser()
    config.read(config_file_name)

    string = config['DEFAULT']['str']
    count = int(config['DEFAULT']['count'])

    return string * count


def get_connection_info(config_file_name, username):
    """Вывести пару строк (ip, port) для username или для DEFAULT."""
    import configparser

    config = configparser.ConfigParser()
    config.read(config_file_name)

    default_ip = config['DEFAULT']['ip']
    default_port = config['DEFAULT']['port']

    if 'ip' in config[username].keys():
        user_ip = config[username]['ip']

    if 'port' in config[username].keys():
        user_port = config[username]['port']

    if username not in config.keys():
        return (default_ip, default_port)

    return (user_ip, user_port)
