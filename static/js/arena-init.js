// Create weather effects container on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Arena initialized');
    const container = document.createElement('div');
    container.id = 'weather-effects';
    document.body.appendChild(container);
});

// Add pulse animation to CSS if not already there
if (!document.getElementById('pulse-animation-style')) {
    const style = document.createElement('style');
    style.id = 'pulse-animation-style';
    style.textContent = `
        @keyframes pulse {
            0%, 100% { opacity: 0.3; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.1); }
        }
    `;
    document.head.appendChild(style);
}

