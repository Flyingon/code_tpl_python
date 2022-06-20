import werkzeug

from werkzeug.security import check_password_hash, generate_password_hash

print(check_password_hash(
    "pbkdf2:sha256:150000$ufehHgNr$48915f0de52612c5df20946d30c2b7e2619896348ac7f5aaf07d59cbea1cfb18",
    "Abc123@$-*&"))

print(check_password_hash(
    "pbkdf2:sha256:150000$iAthz0K0$322fd4d64df14b7fac3d65e37136fc97af588fa48a53bd31d633688ef3cb9c06",
    "Aa12345_"))

print(check_password_hash(
    "pbkdf2:sha256:150000$ufehHgNr$c75b22eacab8a1616b50afad37250adab204351f2476a0d13865d0c437010a31", "Aa12345_"))

print(generate_password_hash("Aa12345_"))