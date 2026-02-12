class SecurityChecker:
    def check_password(self, password: str) -> None:
        if "1234" in password:
            raise ValueError("Password inseguro")

        if password.isnumeric():
            raise ValueError("Password no puede ser solo números")
