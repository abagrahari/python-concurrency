import requests
import threading

urls = [
    "https://appliedbrainresearch.com/",
    "http://www.google.com",
    "http://www.python.org",
]


def fetch_url(url):
    print(f"Starting {url}")
    resp = requests.get(url)
    print(f"Finished {url}; response length: {len(resp.content)}")


def main():
    # Create OS Threads, and keep track
    threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]

    for thread in threads:
        thread.start()
    for thread in threads:
        # blocking wait for threads to finish
        thread.join()


main()

# Program prints something like:
# Starting https://appliedbrainresearch.com/
# Starting http://www.google.com
# Starting http://www.python.org
# Finished http://www.google.com; response length: 14398
# Finished http://www.python.org; response length: 50520
# Finished https://appliedbrainresearch.com/; response length: 24127
