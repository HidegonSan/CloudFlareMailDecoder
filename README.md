# CloudFlareMailProtectionTool
Encryption/Decryption of CloudFlare's email protection

# Example
```py
print(encode_cfmail("info@example.com", 0x12)) # => 127b7c747d52776a737f627e773c717d7f
print(decode_cfmail("127b7c747d52776a737f627e773c717d7f")) # => info@example.com
```
