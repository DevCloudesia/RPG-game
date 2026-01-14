#!/bin/bash
# Start TWO game instances on different ports

echo "=========================================="
echo "  ⚔️  STARTING TWO GAME INSTANCES  ⚔️"
echo "=========================================="
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
echo "🎮 GAME INSTANCE #1"
echo "=========================================="
echo "Starting on port 8080..."
echo "URL: http://localhost:8080"
echo ""
python web_game.py 8080 > instance1.log 2>&1 &
INSTANCE1_PID=$!
echo "✅ Instance #1 started (PID: $INSTANCE1_PID)"
echo ""

sleep 2

echo "=========================================="
echo "🎮 GAME INSTANCE #2"
echo "=========================================="
echo "Starting on port 8081..."
echo "URL: http://localhost:8081"
echo ""
python web_game.py 8081 > instance2.log 2>&1 &
INSTANCE2_PID=$!
echo "✅ Instance #2 started (PID: $INSTANCE2_PID)"
echo ""

sleep 2

echo "=========================================="
echo "✅ BOTH INSTANCES ARE RUNNING!"
echo "=========================================="
echo ""
echo "🌐 Player 1 URL: http://localhost:8080"
echo "🌐 Player 2 URL: http://localhost:8081"
echo ""
echo "📝 Each player gets their own game instance!"
echo "📝 Separate characters and progress for each"
echo ""
echo "To stop both servers, run:"
echo "  ./stop_instances.sh"
echo ""
echo "Or manually kill processes:"
echo "  kill $INSTANCE1_PID $INSTANCE2_PID"
echo ""
echo "Logs:"
echo "  Instance #1: tail -f instance1.log"
echo "  Instance #2: tail -f instance2.log"
echo ""
echo "=========================================="
echo "Enjoy your adventure! ⚔️"
echo "=========================================="

# Save PIDs to file for easy stopping
echo $INSTANCE1_PID > instance1.pid
echo $INSTANCE2_PID > instance2.pid




