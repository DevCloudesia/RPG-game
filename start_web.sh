#!/bin/bash
# Start the web version of Realm of Legends

echo "=========================================="
echo "  ⚔️  REALM OF LEGENDS - Web Version  ⚔️"
echo "=========================================="
echo ""
echo "Starting web server..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
source venv/bin/activate

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "Installing Flask..."
    pip install Flask
    echo ""
fi

echo "=========================================="
echo "🌐 Open your browser and go to:"
echo "   http://localhost:8080"
echo ""
echo "✨ The game will run in your web browser!"
echo "✨ Check the output for Network URL to"
echo "   share with others on your network!"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start the web server
python web_game.py

