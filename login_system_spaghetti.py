class LoginSystem:

    def login(self, user, password):
        print("Iniciando proceso de login...\n")

        # ---------------- VALIDACIONES ----------------
        if user == "" or password == "":
            print("Error: campos vacíos")

        if len(password) < 6:
            print("Password demasiado corto")

        # ---------------- REGLAS DE SEGURIDAD ----------------
        if "1234" in password:
            print("Password inseguro")

        if password.isnumeric():
            print("Password no puede ser solo números")

        # ---------------- AUTENTICACIÓN ----------------
        # "Base de datos" hardcodeada
        if user == "admin" and password == "1234_secure":
            print("Login correcto")

            # ---------------- LOGGING ----------------
            print("Guardando log...")
            f = open("log.txt", "a")
            f.write(user + " logged in\n")
            f.close()

        else:
            print("Login incorrecto")

        # ---------------- LÓGICA EXTRA MEZCLADA ----------------
        if user == "admin":
            print("Bienvenido administrador")

        print("\nProceso terminado\n")


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    system = LoginSystem()

    system.login("admin", "1234_secure")
    system.login("admin", "1234")
    system.login("", "abc123")