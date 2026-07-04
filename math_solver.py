"""
Core Math Solver using OpenAI API
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from config import MATH_TUTOR_SYSTEM_PROMPT, API_MODEL, MAX_TOKENS, TEMPERATURE

# Load environment variables
load_dotenv()

class MathSolver:
    def __init__(self):
        """Initialize OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        self.client = OpenAI(api_key=api_key)
        self.model = API_MODEL
        self.max_tokens = MAX_TOKENS
        self.temperature = TEMPERATURE
    
    def solve(self, problem: str) -> str:
        """
        Solve a math problem with step-by-step explanation
        
        Args:
            problem (str): The math problem to solve
            
        Returns:
            str: Detailed step-by-step solution
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": MATH_TUTOR_SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": problem
                    }
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"❌ Error: {str(e)}\n\nMake sure your OpenAI API key is valid in .env file"
    
    def solve_with_context(self, problem: str, context: str = "") -> str:
        """
        Solve with additional context/hints
        
        Args:
            problem (str): The math problem
            context (str): Additional context or hint
            
        Returns:
            str: Solution with context considered
        """
        if context:
            full_problem = f"{problem}\n\nContext/Hint: {context}"
        else:
            full_problem = problem
        
        return self.solve(full_problem)
