import hashlib


class AuthService:
    def __init__(self):
        # Simulación base de datos
        self._users_db = {
            "admin": self._hash_password("passwordAdminUltraSegura202609")
        }

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, user: str, password: str) -> bool:
        hashed = self._hash_password(password)

        if user in self._users_db:
            return self._users_db[user] == hashed

        return False
