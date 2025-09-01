import os
import socket
from flask import Flask, jsonify
import redis

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, db=0)

@app.route("/")
def index():
    # increments a shared counter in Redis
    count = r.incr("hits")
    hostname = socket.gethostname()
    return f"Hello from {hostname}! Seen {count} times.\n"

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
