import asyncio
import aiohttp

urls = [
    "https://appliedbrainresearch.com/",
    "http://www.google.com",
    "http://www.python.org",
]


async def fetch_url(url):
    print(f"Starting {url}")
    session = aiohttp.ClientSession()
    response = await session.get(url)  # async functions need to be awaited
    # long running IO functions should be async and then awaited
    data = await response.text()
    print(f"Finished {url}; response length: {len(data)}")
    await session.close()


async def main():
    # Create and start tasks
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]

    for task in tasks:
        # Wait for a task to finish. Doesn't block event loop.
        # Other coroutines besides main() could be run concurrently
        await task


asyncio.run(main())

# Program prints something like:
# Starting https://appliedbrainresearch.com/
# Starting http://www.google.com
# Starting http://www.python.org
# Finished http://www.google.com; response length: 14451
# Finished http://www.python.org; response length: 50517
# Finished https://appliedbrainresearch.com/; response length: 24099
