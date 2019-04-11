**EVP_PKEY**  
structure for storing an algorithm independent private key in memory.  
```
EVP_PKEY * pkey;
pkey = EVP_PKEY_new();
RSA * rsa;
rsa = RSA_generate_key(
    2048,   /* number of bits for the key - 2048 is a sensible value */
    RSA_F4, /* exponent - RSA_F4 is defined as 0x10001L */
    NULL,   /* callback - can be NULL if we aren't displaying progress */
    NULL    /* callback argument - not needed in this case */
);
EVP_PKEY_assign_RSA(pkey, rsa);
```
**X509**  
OpenSSL uses the X509 structure to represent an x509 certificate in memory.  
```
X509 * x509;
x509 = X509_new();
```
Next some poperty like serial number, expiry time, extension, cn, ou ,issuer name etc.  
Set the public key that we generated in key-pair above. 
```X509_sign(x509, pkey, EVP_sha1());```  
This will create a self signed certificate.
Lastly this certificate should be sign by CA private key.  
