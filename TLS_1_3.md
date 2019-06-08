*TLS	v1.3	supports	5	cipher	suites.*  
– TLS_AES_128_GCM_SHA256  
– TLS_AES_256_GCM_SHA384  
– [TLS_CHACHA20_POLY1305_SHA256](http://loup-vaillant.fr/tutorials/poly1305-design)  
– TLS_AES_128_CCM_SHA256  
– TLS_AES_128_CCM_8_SHA256  

Key	Exchange	algorithms:  
– DHE	&	ECDHE  
• Only	5	ECDHE	curve	groups	supported  
• Only	5	DHE	finite	field	groups	supported  
– Pre-Shared	Key	(PSK)  
– PSK	with	(EC)DHE  
• Digital	Signature	(Authentication)	algorithms:  
– RSA		(PKCS#1	variants)  
– ECDSA	/	EdDSA  
These algorithm are not defined in ciphers but in extension field **supported_groups** in Client Hello request.  
Similary for verifying Sinature Hash Algorithm is defined in another extension.  
![Client Hello](https://github.com/c0D3M/Misc-Writeups/blob/master/tls_1_3.png)


(https://crypto.stackexchange.com/questions/62917/what-is-different-below-two-ciphersuites)  
(https://security.stackexchange.com/questions/100449/what-difference-between-aes-128-gcm-and-aes-128-and-aes-128-cbc-ciphers)  
(https://github.com/johnshajiang/blog/wiki/Exploring-TLS-1.3-with-OpenSSL-1.1.1)    

(RFC: https://tools.ietf.org/html/rfc8446)  
Cipher List: (https://tools.ietf.org/html/rfc8446#appendix-B.4)  

0-RTT:  
1-RTT: 
*TLS 1.3 Extensions*  
https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xml  
*TLS 1.2 Cipher List*
https://tools.ietf.org/html/rfc5289#section-3.2  
