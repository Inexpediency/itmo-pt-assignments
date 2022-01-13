import configparser


def repeat(config_file_name):
    """Вывести повторенную count раз строку str (см. _legend.md)"""
    cfg = configparser.ConfigParser()
    cfg.read(config_file_name)

    string = cfg['DEFAULT']['str']
    count = int(cfg['DEFAULT']['count'])

    return string * count


def get_connection_info(config_file_name, username):
    """Вывести пару строк (ip, port) для username или для DEFAULT."""
    cfg = configparser.ConfigParser()
    cfg.read(config_file_name)

    usr_info = cfg[username] if cfg.has_section(username) else cfg['DEFAULT']

    return usr_info['ip'], usr_info['port']
