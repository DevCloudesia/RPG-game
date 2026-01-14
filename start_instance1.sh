#!/bin/bash
# Start Game Instance #1 only

echo "=========================================="
echo "  🎮 STARTING GAME INSTANCE #1"
echo "=========================================="
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "Port: 8080"
echo "URL: http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
echo ""

# Start on port 8080
python web_game.py 8080




