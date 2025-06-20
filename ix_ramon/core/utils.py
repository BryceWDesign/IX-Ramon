"""
IX-Ramon Utilities Module

Helper functions for cleaning, validating, and parsing mathematical and cryptographic queries.
Ensures consistent input processing within the IX-Ramon domain.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the query string by stripping whitespace,
    removing excessive spaces, and filtering out unwanted characters.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\+\=\(\)\[\]\.:]+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Validates the query for minimal length and presence of alphanumeric characters.
    """
    return bool(query and len(query) > 3 and any(c.isalnum() for c in query))

# Example usage
if __name__ == "__main__":
    test_queries = [
        "  GCD(24, 36) ",
        "???",
        "Modular Arithmetic",
        "Explain prime number!"
    ]

    for q in test_queries:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"Original: '{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
