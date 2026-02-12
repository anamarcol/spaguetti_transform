from validator import Validator
from auth_service import AuthService
from security_checker import SecurityChecker
from logger_service import Logger
from login_orchestator import LoginSystem


def main():
    validator = Validator()
    auth_service = AuthService()
    security_checker = SecurityChecker()
    logger = Logger()

    login_system = LoginSystem(
        validator,
        auth_service,
        security_checker,
        logger
    )

    # Casos de prueba
    login_system.login("admin", "passwordAdminUltraSegura202609")
    login_system.login("admin", "1234")
    login_system.login("", "abc123")


if __name__ == "__main__":
    main()
