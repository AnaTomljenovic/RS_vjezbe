import asyncio
import aiohttp
import time

async def fetch_users():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/users") as response:
            return await response.json()

async def main():
    start = time.time()
    
    tasks = [fetch_users() for _ in range(5)]
    responses = await asyncio.gather(*tasks)
    
    users = responses[0]
    
    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]
    
    end = time.time()
    
    print("Imena korisnika:", names)
    print("Email adrese:", emails)
    print("Korisnička imena:", usernames)
    print(f"Vrijeme izvođenja: {end - start:.2f} sekundi")

asyncio.run(main())
