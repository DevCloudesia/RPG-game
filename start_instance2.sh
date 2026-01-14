#!/bin/bash
# Start Game Instance #2 only

echo "=========================================="
echo "  🎮 STARTING GAME INSTANCE #2"
echo "=========================================="
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "Port: 8081"
echo "URL: http://localhost:8081"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
echo ""

# Start on port 8081
python web_game.py 8081




