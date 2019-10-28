import shutil
import subprocess
import sys
from os import path, makedirs

from flask import Flask

from controllers.dashboard import dashboard
from security.headers import apply_security_headers

APP_NAME = "Example app"
SERVER_PORT = 13337

# TLS Cert generation config ####################
CERT_DIR = "cert"
CERT_FILENAME = "cert.pem"
KEY_FILENAME = "key.pem"

CERT_KEY_SIZE = 1024 * 8  # 8192
CERT_VALIDITY_DAYS = 30
COMMON_NAME = "localhost"

CERT_GENERATION_CMD = f"openssl req -x509 -nodes -newkey rsa:{CERT_KEY_SIZE} " \
                      f"-keyout {CERT_DIR}/{KEY_FILENAME} -out {CERT_DIR}/{CERT_FILENAME} " \
                      f"-days {CERT_VALIDITY_DAYS} -sha512 -subj \'/CN={COMMON_NAME}\'"

CERT_GENERATION_CMD_TIMEOUT_SECONDS = 60
# TLS Cert generation config END ################


def generate_self_signed_tls_cert(cert_directory: str):
    print(f"Generating self signed certificate. Storing files in ({cert_directory}) directory")

    if path.exists(cert_directory):
        print("Performing cleanup - removing old directory")
        shutil.rmtree(cert_directory)

    makedirs(cert_directory, exist_ok=False)

    try:
        subprocess.run(CERT_GENERATION_CMD, check=True, shell=True, timeout=CERT_GENERATION_CMD_TIMEOUT_SECONDS)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as ex:
        print("Error when generating TLS certificate")
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    generate_self_signed_tls_cert("cert")

    app = Flask(APP_NAME)
    app.after_request(apply_security_headers)
    app.register_blueprint(dashboard)

    # If DEBUG mode is enabled it will cause app to initialize twice. Make sure to generate TLS certs only once!
    # See https://stackoverflow.com/q/25504149
    app.run(ssl_context=(f"{CERT_DIR}/{CERT_FILENAME}", f"{CERT_DIR}/{KEY_FILENAME}"), port=SERVER_PORT)
