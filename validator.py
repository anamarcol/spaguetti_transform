class Validator:
    def validate(self, user: str, password: str) -> None:
        if not user or not password:
            raise ValueError("Campos vacíos")

        if len(password) < 6:
            raise ValueError("Password demasiado corto")
