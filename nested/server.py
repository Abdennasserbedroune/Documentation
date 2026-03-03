#!/usr/bin/env python3
"""
Simple HTTP Server for sharing documentation on local network
Run this script and share the displayed IP address with others on your network
"""

import http.server
import socketserver
import socket
import os
import sys
from datetime import datetime

def get_local_ip():
    """Get the local IP address for network sharing"""
    try:
        # Create a socket to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def start_server(port=8080):
    """Start the HTTP server"""
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Get local IP
    local_ip = get_local_ip()
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print("=" * 60)
            print("🚀 LOCAL DOCUMENTATION SERVER")
            print("=" * 60)
            print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"📁 Serving directory: {os.getcwd()}")
            print(f"🌐 Local access: http://localhost:{port}")
            print(f"🌐 Network access: http://{local_ip}:{port}")
            print("=" * 60)
            print("📋 Share this URL with others on your network:")
            print(f"    http://{local_ip}:{port}")
            print("=" * 60)
            print("🛑 Press Ctrl+C to stop the server")
            print()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python3 server.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    port = 8080
    
    # Allow custom port from command line
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            if not (1024 <= port <= 65535):
                raise ValueError("Port must be between 1024 and 65535")
        except ValueError as e:
            print(f"❌ Invalid port: {e}")
            print("Usage: python3 server.py [port]")
            sys.exit(1)
    
    start_server(port)
