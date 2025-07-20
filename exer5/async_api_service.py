import aiohttp
import asyncio

async def fetch_user_data(user_id):
    """Simule un appel API asynchrone"""
    await asyncio.sleep(0.5)  # Simule latence réseau

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/users/{user_id}") as response:
            return await response.json()

async def get_user_name(user_id):
    """Récupère le nom d'un utilisateur"""
    user_data = await fetch_user_data(user_id)
    return user_data.get('name', 'Unknown')

async def get_user_email(user_id):
    """Récupère l'email d'un utilisateur"""
    user_data = await fetch_user_data(user_id)
    return user_data.get('email', 'no-email@example.com')

async def get_user_profile(user_id):
    """Récupère le profil complet d'un utilisateur"""
    name = await get_user_name(user_id)
    email = await get_user_email(user_id)
    return {
        'user_id': user_id,
        'name': name,
        'email': email
    }

# Exemple d'exécution (à utiliser dans un script principal)
# if __name__ == "__main__":
#     profile = asyncio.run(get_user_profile(123))
#     print(profile)
