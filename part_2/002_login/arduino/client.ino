#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your-ssid";
const char* password = "your-password";

void setup() {
  Serial.begin(115200);

  // Connect to WiFi network
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Perform the login request
  auth();
}

void loop() {
  // Your code logic here
}

void auth() {
  HTTPClient http;
  String url = "http://localhost:5000/login";  // Replace with the appropriate URL of the server

  // Prepare the JSON payload
  String payload = "{\"username\":\"admin\",\"password\":\"admin123\"}";

  // Set the content type header
  http.addHeader("Content-Type", "application/json");

  // Perform the POST request
  int httpResponseCode = http.POST(url, payload);

  if (httpResponseCode == 200) {
    Serial.println("Login successful");
  } else {
    Serial.println("Invalid credentials");
  }

  http.end();
}
