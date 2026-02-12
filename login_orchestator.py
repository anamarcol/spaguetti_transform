from validator import Validator
from auth_service import AuthService
from security_checker import SecurityChecker
from logger_service import Logger


class LoginSystem:
    def __init__(
        self,
        validator: Validator,
        auth_service: AuthService,
        security_checker: SecurityChecker,
        logger: Logger
    ):
        self.validator = validator
        self.auth_service = auth_service
        self.security_checker = security_checker
        self.logger = logger

    def login(self, user: str, password: str) -> None:
        try:
            self.validator.validate(user, password)
            self.security_checker.check_password(password)

            if self.auth_service.authenticate(user, password):
                print("✅ Login correcto")
                self.logger.log(f"{user} logged in")
            else:
                print("❌ Login incorrecto")

        except ValueError as e:
            print(f"⚠ Error: {e}")
