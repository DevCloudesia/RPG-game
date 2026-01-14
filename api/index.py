"""
Vercel serverless function entry point
This wraps the Flask app for Vercel deployment
"""
from web_game import app

# Vercel serverless function handler
def handler(request):
    return app(request.environ, lambda *args: None)

# For Vercel
app = app





