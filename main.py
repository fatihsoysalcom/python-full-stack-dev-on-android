import http.server
import socketserver
import os

# Define the port the server will run on
PORT = 8000

# Create a simple web server handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve files from the current directory
        # This simulates serving static assets for a frontend
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # Simulate a simple backend API endpoint
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received POST data: {post_data.decode('utf-8')}")

        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "Data received successfully!"}')

# Create the server
with socketserver.TCPServer(('', PORT), MyHttpRequestHandler) as httpd:
    print(f"Serving full-stack Python app on port {PORT}")
    print("Access the frontend at http://<your-android-ip>:8000/")
    print("POST data to http://<your-android-ip>:8000/ to test the backend.")

    # To run this on Android, you'll need a Python interpreter like Termux.
    # You can then navigate to the directory containing this file and run:
    # python main.py
    # Then, create a simple index.html file in the same directory to act as your frontend.

    # Example index.html (create this file separately):
    # <!DOCTYPE html>
    # <html>
    # <head>
    #     <title>Android Python Dev</title>
    # </head>
    # <body>
    #     <h1>Welcome to Full-Stack Python on Android!</h1>
    #     <button onclick="sendData()">Send Test Data</button>
    #     <p id="response"></p>
    #     <script>
    #         function sendData() {
    #             fetch('/', { method: 'POST', body: '{"test":"data"}' })
    #                 .then(response => response.json())
    #                 .then(data => { document.getElementById('response').innerText = data.message; });
    #         }
    #     </script>
    # </body>
    # </html>

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.shutdown()
