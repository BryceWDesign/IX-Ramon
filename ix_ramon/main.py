"""
IX-Ramon CLI Entry Point

Allows terminal-based interaction for mathematical and cryptographic queries.
Outputs answers directly to the console.
"""

import sys
from core.query_processor import IXRamonQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your math or cryptography question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXRamonQueryProcessor()
    response = processor.process_query(query)

    print("\n🔢 IX-Ramon Response 🔢")
    print(response)

if __name__ == "__main__":
    main()
