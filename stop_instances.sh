#!/bin/bash
# Stop both game instances

echo "=========================================="
echo "  🛑 STOPPING GAME INSTANCES"
echo "=========================================="
echo ""

# Stop using PID files if they exist
if [ -f instance1.pid ]; then
    PID1=$(cat instance1.pid)
    if kill -0 $PID1 2>/dev/null; then
        kill $PID1
        echo "✅ Stopped Instance #1 (PID: $PID1)"
    else
        echo "⚠️  Instance #1 was not running"
    fi
    rm instance1.pid
else
    echo "⚠️  No PID file for Instance #1"
fi

if [ -f instance2.pid ]; then
    PID2=$(cat instance2.pid)
    if kill -0 $PID2 2>/dev/null; then
        kill $PID2
        echo "✅ Stopped Instance #2 (PID: $PID2)"
    else
        echo "⚠️  Instance #2 was not running"
    fi
    rm instance2.pid
else
    echo "⚠️  No PID file for Instance #2"
fi

echo ""

# Also try to kill by port
echo "🔍 Checking for any remaining Flask processes..."
pkill -f "python.*web_game.py" && echo "✅ Cleaned up remaining processes" || echo "✓ No other processes found"

echo ""
echo "=========================================="
echo "✅ All instances stopped!"
echo "=========================================="




