"""
IX-Ramon Core Mathematics Knowledge Module

Contains foundational rules and definitions for algebra, logic, number theory,
cryptography, and symbolic reasoning. Used for deterministic validation
and symbolic answer generation in the IX-Gibson system.
"""

import math

class MathKnowledge:
    def __init__(self):
        self.facts = {
            "modular arithmetic": "A system of arithmetic for integers, where numbers wrap around after reaching a certain value — the modulus.",
            "greatest common divisor": "The largest integer that divides two or more integers without a remainder.",
            "matrix multiplication": "A binary operation producing a matrix from two matrices by multiplying rows with columns.",
            "cryptographic hash": "A one-way mathematical function that maps data of arbitrary size to fixed-length values.",
            "prime number": "A natural number greater than 1 that has no positive divisors other than 1 and itself.",
            "proof by contradiction": "A mathematical technique that assumes the negation of a statement and derives a contradiction to prove the original."
        }

    def get_fact(self, term: str) -> str:
        t = term.lower().strip()
        return self.facts.get(t, f"Unknown concept: '{term}' — not found in Ramon’s current base.")

# Standalone test
if __name__ == "__main__":
    mk = MathKnowledge()
    print(mk.get_fact("modular arithmetic"))
    print(mk.get_fact("prime number"))
    print(mk.get_fact("fourier transform"))
