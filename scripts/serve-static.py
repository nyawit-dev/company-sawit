#!/usr/bin/env python3
"""Static file server for the click-through check.

`serve` (npm) returns text/html for every file on this box, which makes the
browser refuse to execute the Nuxt entry as a module. Python's http.server
maps extensions to the right MIME types, so the page actually hydrates.
"""
import functools
import http.server
import os
import socketserver
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4177


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        # Nuxt generates 404.html for SPA-style fallback under --single.
        path = self.translate_path(self.path.split("?")[0])
        if not os.path.exists(path) and os.path.exists(os.path.join(ROOT, "index.html")):
            self.path = "/index.html"
        return super().do_GET()


class Server(socketserver.TCPServer):
    allow_reuse_address = True


with Server(("127.0.0.1", PORT), functools.partial(Handler, directory=ROOT)) as httpd:
    print(f"serving {ROOT} on http://127.0.0.1:{PORT}", flush=True)
    httpd.serve_forever()
