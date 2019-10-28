# Flask application starter
Basic Flask application starter template with self-signed TLS certificate generation and preconfigured security headers.

### Configuration
Some basic configuration options are available in ```app.py``` file

```python
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
```

#### OpenSSL self-signed certificate default generation command
```
openssl req -x509 -nodes -newkey rsa:8192 -keyout cert/key.pem -out cert/cert.pem -days 30 -sha512 -subj '/CN=localhost'
```