#!/bin/bash

# Start local web server and open the hexagonal grid map
echo "Starting web server on http://localhost:8000"
echo "Opening Geneva Hexagonal Grid Map..."

# Start Python HTTP server in background
python3 -m http.server 8000 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 1

# Open browser
open http://localhost:8000/index.html

echo ""
echo "✅ Server is running!"
echo "📍 Map URL: http://localhost:8000/index.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Wait for server process
wait $SERVER_PID

