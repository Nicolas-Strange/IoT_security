#include <Crypto.h>
#include <CryptoLib.h>
#include <RSA.h>
#include <SHA256.h>

// Server private key
const char* privateKey = "<YOUR_PRIVATE_KEY>";  // Replace with your private key

// Create RSA object
RSA rsa;

void setup() {
  Serial.begin(9600);

  // Initialize the RSA object with the private key
  rsa.setPrivateKey(privateKey);
}

void loop() {
  // Wait for incoming message
  // In this example, let's assume you receive the encrypted message as a string
  String encryptedMessage = "<ENCRYPTED_MESSAGE>";  // Replace with the received encrypted message

  // Decrypt the message
  String decryptedMessage = rsa.decrypt(encryptedMessage);

  // Process the decrypted message
  // Here you can perform any desired actions with the decrypted message
  Serial.println("Decrypted message: " + decryptedMessage);

  delay(1000);  // Adjust delay as needed
}
