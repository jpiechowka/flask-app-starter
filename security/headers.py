import time


def apply_security_headers(response):
    print("Applying security headers to response")

    current_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())

    # Strict Transport Security (HSTS)
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"

    # Security headers
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'; script-src 'self'; " \
                                                  "connect-src 'self'; img-src 'self'; style-src 'self'; " \
                                                  "sandbox; upgrade-insecure-requests;"
    response.headers["Feature-Policy"] = "ambient-light-sensor: 'none'; autoplay:'none'; accelerometer: 'none'; " \
                                         "camera: 'none'; display-capture: 'none'; document-domain: 'none'; " \
                                         "fullscreen: 'none'; geolocation 'none'; gyroscope:'none'; " \
                                         "magnetometer: 'none'; microphone 'none'; midi: 'none'; payment: 'none'; " \
                                         "picture-in-picture: 'none'; speaker: 'none'; sync-xhr: 'none'; usb: 'none'; " \
                                         "wake-lock: 'none'; vibrate 'none'; vr: 'none';"
    response.headers["X-Frame-Options"] = "deny"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-DNS-Prefetch-Control"] = "off"
    response.headers["X-Permitted-Cross-Domain-Policies"] = "none"

    # Cache control headers
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0, post-check=0, pre-check=0"
    response.headers["Last-Modified"] = current_time
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"

    # Spoof server header
    response.headers["Server"] = "PHP running on Apache"

    return response
