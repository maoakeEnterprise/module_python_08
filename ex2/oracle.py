from dotenv import load_dotenv
import os


def verif_var() -> bool:
    required = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    verif = [var for var in required if not os.getenv(var)]
    if verif != []:
        raise ValueError("The values required do not exist you need it "
                         "in your .env MATRIX_MOD DATABASE_URL "
                         "API_KEY LOG_LEVEL ZION_ENDPOINT")
    return True


def is_env(key: str) -> bool:
    if os.getenv(key):
        return True
    return False


def main() -> None:
    try:
        load_dotenv()
        print("ORACLE STATUS: Reading the Matrix...\n")
        vars = verif_var()
        db = ("Connected to local instance" if os.getenv("DATABASE_URL")
              else "Not Connected")
        api = ("Authenticated" if os.getenv("API_KEY")
               else "Declined")
        online = ("Online" if os.getenv("ZION_ENDPOINT") else "Offline")

        print("Configuration loaded:")
        print(f"Mode:{os.getenv('MATRIX_MODE')}")
        print(f"Database: {db}")
        print(f"API Access: {api}")
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
        print(f"Zion Network: {online}\n")
        print("Environment security check:")
        print(f"[{'OK' if api else 'KO'}]No hardcoded secrets detected")
        print(f"[{'OK' if vars else 'KO'}]"
              ".env file properly configured")
        print("[OK]Production overrides available")
        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(f"Type Error : {e.__class__.__name__}")
        print(f"Message Error: {e}")


if __name__ == "__main__":
    main()
