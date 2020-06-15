# socket サーバを作成

import socket

ip = socket.gethostbyname(socket.gethostname())

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('3.113.31.63', 80))
    # 1 接続
    s.listen(1)
    # connection するまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, ip = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                conn.send("Hello: BasicHTTP!")
                conn.send(b"ip: {}".format(ip).encode("utf-8"))
                print()
                # クライアントにデータを返す(b -> byte でないといけない)
                conn.sendall(b'Hello: ' + data)
                