"""
Solution validator and error checker
"""

import re

class SolutionValidator:
    """Validates and checks math solutions"""
    
    @staticmethod
    def has_steps(solution: str) -> bool:
        """Check if solution has multiple steps"""
        steps = re.findall(r'Step \d+:|**Step \d+:|step \d+:', solution, re.IGNORECASE)
        return len(steps) > 0
    
    @staticmethod
    def has_final_answer(solution: str) -> bool:
        """Check if solution has a clear final answer"""
        return "Final Answer" in solution or "final answer" in solution.lower()
    
    @staticmethod
    def has_explanation(solution: str) -> bool:
        """Check if solution has explanations (not just calculations)"""
        return len(solution) > 100  # Reasonable length for explanation
    
    @staticmethod
    def validate(solution: str) -> dict:
        """
        Validate solution quality
        
        Returns:
            dict: Validation results
        """
        return {
            "has_steps": SolutionValidator.has_steps(solution),
            "has_final_answer": SolutionValidator.has_final_answer(solution),
            "has_explanation": SolutionValidator.has_explanation(solution),
            "solution_length": len(solution)
        }
    
    @staticmethod
    def quality_report(solution: str) -> str:
        """Generate quality report"""
        validation = SolutionValidator.validate(solution)
        
        report = "📊 Solution Quality Report:\n"
        report += f"✓ Has Steps: {validation['has_steps']}\n"
        report += f"✓ Has Final Answer: {validation['has_final_answer']}\n"
        report += f"✓ Has Explanation: {validation['has_explanation']}\n"
        report += f"✓ Length: {validation['solution_length']} characters\n"
        
        return report
