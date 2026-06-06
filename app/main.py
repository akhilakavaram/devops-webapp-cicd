import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


APP_NAME = os.getenv("APP_NAME", "DevOps Starter App")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


def health_payload():
    return {
        "status": "ok",
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }


def readiness_payload():
    return {
        "ready": True,
        "service": APP_NAME,
        "environment": ENVIRONMENT,
    }


def version_payload():
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
    }


def homepage_html():
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{APP_NAME}</title>
    <style>
      body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: #f4f7f8;
        color: #1f2933;
      }}

      main {{
        max-width: 760px;
        margin: 8vh auto;
        padding: 32px;
      }}

      h1 {{
        font-size: 40px;
        margin-bottom: 8px;
      }}

      p {{
        font-size: 18px;
        line-height: 1.5;
      }}

      code {{
        background: #e4ebef;
        padding: 3px 6px;
        border-radius: 4px;
      }}

      .panel {{
        margin-top: 24px;
        padding: 20px;
        border: 1px solid #d8e0e5;
        border-radius: 8px;
        background: #ffffff;
      }}
    </style>
  </head>
  <body>
    <main>
      <h1>{APP_NAME}</h1>
      <p>This is the first DevOps project: a tiny web app with Docker, Docker Compose, tests, and CI/CD.</p>
      <div class="panel">
        <p><strong>Environment:</strong> {ENVIRONMENT}</p>
        <p><strong>Version:</strong> {APP_VERSION}</p>
        <p>Try <code>/health</code>, <code>/ready</code>, and <code>/version</code> for JSON endpoints.</p>
      </div>
    </main>
  </body>
</html>
"""


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": self._homepage,
            "/health": lambda: self._json_response(health_payload()),
            "/ready": lambda: self._json_response(readiness_payload()),
            "/version": lambda: self._json_response(version_payload()),
        }
        handler = routes.get(self.path)
        if handler is None:
            self._not_found()
            return
        handler()

    def log_message(self, format, *args):
        print("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format % args))

    def _homepage(self):
        body = homepage_html().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json_response(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _not_found(self):
        self._json_response({"error": "not found"}, status=404)


def run():
    port = int(os.getenv("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), AppHandler)
    print(f"{APP_NAME} listening on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
