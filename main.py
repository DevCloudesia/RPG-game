#!/usr/bin/env python3
"""
REALM OF LEGENDS - A Text-Based RPG Adventure

Embark on an epic quest to defeat the Dark Lord and save the realm!

Features:
- 4 unique character classes with special abilities
- Dynamic combat system with skills and strategy
- Expansive world with 12+ locations to explore
- Epic quest line with multiple storylines
- Equipment and inventory management
- Save/Load functionality
"""

import os
import sys
from game import Game

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main entry point"""
    clear_screen()
    
    game = Game()
    
    print("\n" + "="*60)
    print(" "*15 + "⚔️  REALM OF LEGENDS  ⚔️")
    print("="*60)
    print("\n1. New Game")
    print("2. Load Game")
    print("3. Exit")
    
    choice = input("\nYour choice: ").strip()
    
    if choice == "1":
        clear_screen()
        game.start_new_game()
        game.run()
    elif choice == "2":
        clear_screen()
        if game.load_game():
            input("\nPress Enter to continue your adventure...")
            game.run()
        else:
            print("\nNo saved game found. Starting new game...")
            input("\nPress Enter to continue...")
            clear_screen()
            game.start_new_game()
            game.run()
    elif choice == "3":
        print("\nThanks for playing! Goodbye!")
        sys.exit(0)
    else:
        print("\nInvalid choice. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        print("Please report this bug!")
        sys.exit(1)






