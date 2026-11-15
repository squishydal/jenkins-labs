#!/usr/bin/env python3
"""Greeter - a minimal web app for the promotion-pipeline lab.

Serves two things:
  /health -> JSON {"status": "ok", "version": "<build number>"}
  /       -> a tiny HTML page showing the environment and version

Pure standard library, zero dependencies, runs in any python:3.12 image.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "local")
ENV_NAME = os.environ.get("APP_ENV", "unknown")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok", "version": VERSION}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
        else:
            body = ("<h1>Greeter build {}</h1><p>environment: {}</p>"
                    .format(VERSION, ENV_NAME)).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # keep container logs quiet
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8091"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
