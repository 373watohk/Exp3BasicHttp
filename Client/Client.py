# クライアントを作成

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('3.113.31.63', 80))
    s.sendall(b'BasicHTTP!')
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
    data = s.recv(1024)
    #
    print(data.decode("utf-8"))