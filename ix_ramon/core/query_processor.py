"""
IX-Ramon Domain-Specific Query Processor

Handles input parsing and intelligent routing of mathematical and cryptographic questions.
Determines if a question is definitional, calculative, or logical.
"""

from math_knowledge import MathKnowledge

class IXRamonQueryProcessor:
    def __init__(self):
        self.knowledge = MathKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "gcd" in query_lower and any(char.isdigit() for char in query_lower):
            try:
                parts = [int(x) for x in query_lower.replace("gcd", "").replace("(", "").replace(")", "").split() if x.isdigit()]
                if len(parts) == 2:
                    from math import gcd
                    result = gcd(parts[0], parts[1])
                    return f"The greatest common divisor of {parts[0]} and {parts[1]} is {result}."
            except Exception as e:
                return f"Failed to compute GCD: {e}"
        else:
            return (
                "I am IX-Ramon, your mathematical AI. Ask me about cryptography, logic, number theory, or algebraic concepts. "
                "For example: 'Define modular arithmetic', 'What is a prime number?', or 'GCD(60 48)'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXRamonQueryProcessor()
    print(qp.process_query("Define modular arithmetic"))
    print(qp.process_query("GCD(60 48)"))
    print(qp.process_query("Explain proof by contradiction"))
