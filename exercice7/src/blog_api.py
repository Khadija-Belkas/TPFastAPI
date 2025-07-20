import asyncio
from datetime import datetime
from typing import List, Dict, Optional


class DatabaseConnection:
    """Simule une connexion à la base de données"""

    async def execute_query(self, query: str, params: tuple = ()) -> List[Dict]:
        """Exécute une requête SQL"""
        await asyncio.sleep(0.1)  # Simule latence DB
        # Simulation - retourne des données factices
        return [{'id': 1, 'title': 'Test Post'}]


class NotificationService:
    """Service de notifications"""

    async def send_email(self, to: str, subject: str, body: str) -> bool:
        """Envoie un email"""
        await asyncio.sleep(0.2)  # Simule envoi email
        return True


class BlogAPI:
    def __init__(self, db: DatabaseConnection, notification_service: NotificationService):
        self.db = db
        self.notification_service = notification_service

    async def create_post(self, title: str, content: str, author_email: str) -> Dict:
        """Crée un nouveau post de blog"""
        # Sauvegarder en base
        post_data = await self.db.execute_query(
            "INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, datetime.now())
        )

        post_id = post_data[0]['id'] if post_data else 1

        # Envoyer notification
        await self.notification_service.send_email(
            author_email,
            f"Post créé: {title}",
            f"Votre post '{title}' a été créé avec succès"
        )

        return {
            'id': post_id,
            'title': title,
            'content': content,
            'status': 'published'
        }

    async def get_post(self, post_id: int) -> Optional[Dict]:
        """Récupère un post par ID"""
        result = await self.db.execute_query(
            "SELECT * FROM posts WHERE id = ?",
            (post_id,)
        )

        if not result:
            return None

        return result[0]

    async def delete_post(self, post_id: int, admin_email: str) -> bool:
        """Supprime un post (admin seulement)"""
        # Récupérer le post
        post = await self.get_post(post_id)
        if not post:
            return False

        # Supprimer de la base
        await self.db.execute_query(
            "DELETE FROM posts WHERE id = ?",
            (post_id,)
        )

        # Notifier l'admin
        await self.notification_service.send_email(
            admin_email,
            f"Post supprimé: {post['title']}",
            f"Le post '{post['title']}' a été supprimé"
        )

        return True
