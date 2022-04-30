import configparser


class MysqlConfig:
    CONFIG_PATH = "/root/src/env/config.ini"
    config = None

    def __init__(self):
        self.config = self.create_config_parser()

    def create_config_parser(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIG_PATH)
        return config

    def bastion(self):
        return {
            "host": self.config["BASTION"]["host"],
            "ssh_username": self.config["BASTION"]["ssh_username"],
            "ssh_private_key": self.config["BASTION"]["ssh_private_key"],
            "ssh_password": self.config["BASTION"]["ssh_password"],
        }

    def database(self):
        return {
            "localhost": self.config["MYSQL"]["localhost"],
            "user": self.config["MYSQL"]["user"],
            "password": self.config["MYSQL"]["password"],
            "database": self.config["MYSQL"]["database"],
            "port": int(self.config["MYSQL"]["port"]),
        }
