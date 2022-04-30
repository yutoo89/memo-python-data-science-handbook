import MySQLdb
from sshtunnel import SSHTunnelForwarder
from .mysql_config import MysqlConfig


class MysqlManager:
    config = None

    def __init__(self):
        self.config = MysqlConfig()
        self.server = self.create_ssh_tunnel_forwarder()

    def create_ssh_tunnel_forwarder(self):
        bastion = self.config.bastion()
        database = self.config.database()
        return SSHTunnelForwarder(
            (bastion["host"], 22),
            ssh_username=bastion["ssh_username"],
            ssh_password=bastion["ssh_password"],
            ssh_private_key=bastion["ssh_private_key"],
            remote_bind_address=(database["localhost"], database["port"]),
        )

    def start_server(self):
        return self.server.start()

    def close_server(self):
        return self.server.close()

    def get_local_bind_port(self):
        return self.server.local_bind_port

    def db_connect(self):
        database = self.config.database()
        return MySQLdb.connect(
            host="127.0.0.1",
            port=self.get_local_bind_port(),
            user=database["user"],
            passwd=database["password"],
            db=database["database"],
            charset="utf8",
        )

    def query(self, sql):
        # SSHポート転送開始
        self.start_server()
        # DB接続
        connection = self.db_connect()
        # カーソルの取得
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # カーソルの破棄
        cursor.close
        # DB接続の破棄
        connection.close
        # SSHポート転送終了
        self.close_server()
        return result


mysql = MysqlManager()

# <class 'tuple'>
rows = mysql.query("SELECT name FROM pass_sites;")

for row in rows:
    print(row)
