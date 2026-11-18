#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anthropic 论文阅读 — 局域网静态服务器 (纯标准库，无需联网/无需安装依赖)

用法:
    python serve.py [端口]      # 默认端口 8000
举例:
    python serve.py              # 使用 8000
    python serve.py 9000         # 使用 9000

说明:
    - 以本文件所在目录为站点根目录，局域网设备用浏览器即可访问。
    - 图片以 .img 扩展名存储，但内部是真实的 webp/png/jpg/gif，
      本服务会按文件魔数嗅探并返回正确的 Content-Type，确保能正常显示。
    - 支持中文文件名；首页 '/' 自动跳转到 landing 页 home.html。
    - 绑定 0.0.0.0，同一局域网(手机/平板/其他电脑)均可访问。
"""

import os
import sys
import socket
import mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.abspath(__file__))

# 补全/修正常见类型的 MIME
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("text/markdown", ".md")


def sniff_image(path):
    """读取文件头 16 字节，按魔数判断真实图片类型。"""
    try:
        with open(path, "rb") as f:
            head = f.read(16)
    except OSError:
        return None
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "image/webp"
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if head[:2] == b"\xff\xd8":
        return "image/jpeg"
    if head[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    return None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def guess_type(self, path):
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        if ext == ".img":
            # 注意: send_head 传入的 path 已是翻译后的文件系统绝对路径
            t = sniff_image(path)
            return t if t else "application/octet-stream"
        ctype = super().guess_type(path)
        if ext in (".html", ".htm", ".md", ".txt", ".svg", ".css", ".js"):
            if "charset" not in ctype:
                ctype += "; charset=utf-8"
        return ctype

    def do_GET(self):
        # 根路径 '/' 跳转到 landing 页(home.html, ASCII 文件名, 避免中文 URL)
        if self.path.split("?")[0] == "/":
            self.send_response(302)
            self.send_header("Location", "/home.html")
            self.end_headers()
            return
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except OSError:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def find_free_port(start):
    for p in range(start, start + 20):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("0.0.0.0", p))
            s.close()
            return p
        except OSError:
            continue
    return start


def main():
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    port = find_free_port(port)

    httpd = HTTPServer(("0.0.0.0", port), Handler)
    ip = get_lan_ip()
    bar = "=" * 60
    print(bar)
    print("  Anthropic 论文阅读 — 局域网服务已启动")
    print(bar)
    print("  本机访问 :  http://127.0.0.1:%d/" % port)
    print("  局域网访问 :  http://%s:%d/" % (ip, port))
    print("  阅读入口 :  http://%s:%d/home.html" % (ip, port))
    print("  提示：其他设备需连接同一 Wi-Fi/网段；")
    print("        若打不开，请在 Windows 防火墙放行 %d 端口。" % port)
    print("  停止服务 ：  Ctrl+C 或关闭此窗口" % ())
    print(bar)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止。")
        httpd.server_close()


if __name__ == "__main__":
    main()
