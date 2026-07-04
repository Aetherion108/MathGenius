"""
MathGenius - AI Math Tutor
Main entry point for the application
"""

import sys
from math_solver import MathSolver
from validator import SolutionValidator

def print_header():
    """Print welcome header"""
    print("\n" + "="*60)
    print("🧮 MathGenius - AI Math Tutor")
    print("="*60)
    print("Solving complex math problems with step-by-step explanations\n")

def print_footer():
    """Print footer"""
    print("\n" + "="*60)
    print("Thank you for using MathGenius! 🚀")
    print("="*60 + "\n")

def main():
    """Main application loop"""
    print_header()
    
    try:
        # Initialize solver
        solver = MathSolver()
        print("✅ Connected to OpenAI API\n")
        
    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("\n📝 Setup Instructions:")
        print("1. Get API key from: https://platform.openai.com/api-keys")
        print("2. Create .env file with: OPENAI_API_KEY=your_key_here")
        print("3. Run again: python main.py")
        return
    
    # Main loop
    while True:
        print("-" * 60)
        print("Enter your math problem (or 'quit' to exit):")
        print("-" * 60)
        
        problem = input("\n📌 Problem: ").strip()
        
        if problem.lower() in ['quit', 'exit', 'q']:
            print_footer()
            break
        
        if not problem:
            print("⚠️  Please enter a problem!")
            continue
        
        print("\n⏳ Solving... Please wait...\n")
        
        # Solve problem
        solution = solver.solve(problem)
        
        # Display solution
        print("\n" + "="*60)
        print("📝 SOLUTION:")
        print("="*60)
        print(solution)
        print("="*60)
        
        # Validate solution
        validation = SolutionValidator.quality_report(solution)
        print(validation)
        
        # Ask if user wants more help
        print("\nNeed more help? (yes/no): ", end="")
        follow_up = input().strip().lower()
        
        if follow_up in ['yes', 'y']:
            print("What else would you like to know?")
            follow_up_question = input("\n❓ Question: ").strip()
            
            if follow_up_question:
                print("\n⏳ Solving... Please wait...\n")
                follow_up_solution = solver.solve_with_context(
                    problem,
                    follow_up_question
                )
                print("\n" + "="*60)
                print("📝 FOLLOW-UP ANSWER:")
                print("="*60)
                print(follow_up_solution)
                print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue on GitHub")
