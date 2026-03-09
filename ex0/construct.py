import sys
import os
import site


def is_activate():
    return sys.prefix != sys.base_prefix


def print_activate_env() -> None:
    print("""The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.
    """)


def already_activate() -> None:
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[0])


def main() -> None:
    m_status = ("Welcome to the construct" if is_activate()
                else "You're still plugged in")
    v_env = (os.path.basename(sys.prefix) if is_activate()
             else "None detected")
    env_path = (f"Environment Path: {sys.prefix}" if is_activate() else "")
    wa_su = ("\nSUCCESS: You're in an isolated environment!" if is_activate()
             else "WARNING: You're in the global environment!")

    print(f"MATRIX STATUS: {m_status}\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {v_env}")
    print(env_path)
    print(wa_su)
    if is_activate():
        already_activate()
    else:
        print_activate_env()


if __name__ == "__main__":
    main()
