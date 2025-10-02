from prometheus_client import start_http_server, Gauge
import httpx
import time

# List of URLs to monitor
URLS = [
    "https://tools-httpstatus.pickup-services.com/200",
    "https://tools-httpstatus.pickup-services.com/503"
]

# Prometheus metrics
url_up = Gauge('sample_external_url_up', 'URL availability', ['url'])
url_response_ms = Gauge('sample_external_url_response_ms', 'URL response time in milliseconds', ['url'])

def check_urls():
    for url in URLS:
        try:
            start = time.perf_counter()
            response = httpx.get(url, timeout=5.0)
            elapsed_ms = (time.perf_counter() - start) * 1000

            # Update Prometheus metrics
            url_up.labels(url=url).set(1 if response.status_code == 200 else 0)
            url_response_ms.labels(url=url).set(round(elapsed_ms, 2))
        except Exception:
            url_up.labels(url=url).set(0)
            url_response_ms.labels(url=url).set(0)

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on http://localhost:8000/")

    # Periodically check URLs every 10 seconds
    while True:
        check_urls()
        time.sleep(10)

