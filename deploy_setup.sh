#!/bin/bash
# Setup script to prepare for deployment to Vercel and Render

echo "=========================================="
echo "  🚀 RPG GAME DEPLOYMENT SETUP"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

echo "✓ Git is installed"
echo ""

# Check if already initialized
if [ -d .git ]; then
    echo "✓ Git repository already initialized"
else
    echo "📦 Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
fi

echo ""
echo "📝 Configuring .gitignore..."

# Ensure .gitignore exists and has correct entries
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/

# Game save files
savegame.pkl

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Flask
instance/
*.pyc
EOF

echo "✓ .gitignore configured"
echo ""

# Check git config
if ! git config user.name &> /dev/null; then
    echo "⚠️  Git user.name not set"
    read -p "Enter your name for Git commits: " git_name
    git config --global user.name "$git_name"
    echo "✓ Git user.name set"
fi

if ! git config user.email &> /dev/null; then
    echo "⚠️  Git user.email not set"
    read -p "Enter your email for Git commits: " git_email
    git config --global user.email "$git_email"
    echo "✓ Git user.email set"
fi

echo ""
echo "📦 Staging files for commit..."
git add .

echo ""
echo "💾 Creating commit..."
git commit -m "RPG Game - Ready for deployment to Vercel and Render" || echo "✓ Already committed or no changes"

echo ""
echo "=========================================="
echo "  ✅ SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "1️⃣  CREATE GITHUB REPOSITORY:"
echo "   → Go to https://github.com/new"
echo "   → Name: rpg-game"
echo "   → Public or Private: Your choice"
echo "   → Don't initialize with README"
echo "   → Click 'Create repository'"
echo ""
echo "2️⃣  PUSH TO GITHUB:"
echo "   → Copy the commands from GitHub and run them"
echo "   → Or run:"
echo "     git remote add origin https://github.com/YOUR_USERNAME/rpg-game.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo ""
echo "3️⃣  DEPLOY TO VERCEL:"
echo "   → See: DEPLOY_TO_VERCEL.md"
echo "   → Go to https://vercel.com"
echo "   → Import your GitHub repository"
echo ""
echo "4️⃣  DEPLOY TO RENDER:"
echo "   → See: DEPLOY_TO_RENDER.md"
echo "   → Go to https://render.com"
echo "   → Create new Web Service from GitHub"
echo ""
echo "📖 Full guide: DEPLOY_BOTH_PLATFORMS.md"
echo ""
echo "=========================================="
echo "Good luck with your deployment! ⚔️"
echo "=========================================="





