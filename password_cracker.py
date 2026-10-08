import zipfile
import zlib

ZIP_PATH = "whitehouse_secrets.zip"
PASSWORD_FILE = "Ashley-Madison.txt"


def load_passwords(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f]


def crack(zip_path, passwords):
    for count, password in enumerate(passwords, start=1):
        if count % 10000 == 0:
            print(f"Tried {count} passwords, currently at: {password}")
        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(pwd=password.encode())
            return password
        except (RuntimeError, zipfile.BadZipFile, zlib.error):
            continue
    return None


def main():
    passwords = load_passwords(PASSWORD_FILE)
    found = crack(ZIP_PATH, passwords)
    if found:
        print(f"Password found: {found}")
    else:
        print("No password worked.")


if __name__ == "__main__":
    main()
