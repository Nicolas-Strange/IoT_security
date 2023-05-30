#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>
#include <Hash.h>
#include <WiFiClient.h>

ESP8266WebServer server(80);

const char* ssid = "your-ssid";
const char* password = "your-password";

void handleLogin() {
  if (server.method() != HTTP_POST) {
    server.send(405, "text/plain", "Method Not Allowed");
    return;
  }

  String payload = server.arg("plain");
  DynamicJsonDocument json(256);

  DeserializationError error = deserializeJson(json, payload);
  if (error) {
    server.send(400, "text/plain", "Bad Request");
    return;
  }

  String username = json["username"].as<String>();
  String password = json["password"].as<String>();

  // Check the credentials
  if (username.equals("admin") && password.equals("admin123")) {
    server.send(200, "application/json", "{\"message\":\"Login successful\"}");
  } else {
    server.send(401, "application/json", "{\"message\":\"Invalid credentials\"}");
  }
}

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

  // Set up the server routes
  server.on("/login", handleLogin);

  server.begin();
  Serial.println("Server started!");
}

void loop() {
  server.handleClient();
}
