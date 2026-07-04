"""
Core Math Solver using Local Ollama or OpenAI API
"""

import os
import requests
import json
from dotenv import load_dotenv
from config import (
    USE_LOCAL_MODEL, LOCAL_MODEL, MATH_TUTOR_SYSTEM_PROMPT, 
    OPENAI_MODEL, MAX_TOKENS, TEMPERATURE
)

load_dotenv()

class MathSolver:
    def __init__(self):
        """Initialize solver with local model or OpenAI"""
        self.use_local = USE_LOCAL_MODEL
        self.local_model = LOCAL_MODEL
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS
        
        if self.use_local:
            self._init_local_model()
        else:
            self._init_openai()
    
    def _init_local_model(self):
        """Initialize Ollama local model"""
        try:
            # Test connection to Ollama
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code == 200:
                print(f"✅ Connected to Ollama (using {self.local_model})")
                self.ollama_url = "http://localhost:11434/api/generate"
            else:
                raise ConnectionError("Ollama service not responding")
        except Exception as e:
            raise ValueError(
                f"❌ Ollama not running!\n\n"
                f"Install and start Ollama:\n"
                f"1. Download: https://ollama.ai\n"
                f"2. Run: ollama serve\n"
                f"3. In another terminal: ollama pull {self.local_model}\n"
                f"4. Run MathGenius again\n\n"
                f"Error: {str(e)}"
            )
    
    def _init_openai(self):
        """Initialize OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)
        self.model = OPENAI_MODEL
    
    def solve(self, problem: str) -> str:
        """
        Solve a math problem with step-by-step explanation
        
        Args:
            problem (str): The math problem to solve
            
        Returns:
            str: Detailed step-by-step solution
        """
        try:
            if self.use_local:
                return self._solve_local(problem)
            else:
                return self._solve_openai(problem)
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def _solve_local(self, problem: str) -> str:
        """Solve using local Ollama model"""
        try:
            payload = {
                "model": self.local_model,
                "prompt": f"{MATH_TUTOR_SYSTEM_PROMPT}\n\nProblem: {problem}",
                "stream": False,
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            }
            
            response = requests.post(self.ollama_url, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "No response from model")
        
        except requests.exceptions.Timeout:
            return "⏱️ Timeout: Model is taking too long. Try a simpler problem."
        except Exception as e:
            return f"❌ Ollama Error: {str(e)}"
    
    def _solve_openai(self, problem: str) -> str:
        """Solve using OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": MATH_TUTOR_SYSTEM_PROMPT},
                    {"role": "user", "content": problem}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenAI Error: {str(e)}"
    
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
