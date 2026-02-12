class Logger:
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(message + "\n")
    