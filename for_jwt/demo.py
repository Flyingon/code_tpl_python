import jwt

with open("/xxxx/client.pem", "rb") as f:
    private_key = f.read()
with open("/xxxx/client.pub", "rb") as f:
    public_key = f.read()

print(private_key)
print(public_key)

encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
print(encoded)
decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
print(decoded)
