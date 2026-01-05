Firewall Policy Compiler 🛡️
About The Project
The Firewall Policy Compiler is a domain-specific language (DSL) tool designed to simplify network security configuration. It allows network administrators to write firewall rules in a high-level, human-readable format (e.g., ALLOW TCP FROM office_pc TO server PORT 80) and compiles them into a verified, logical structure.

Unlike traditional command-line tools that are prone to syntax errors, this compiler visualizes the entire parsing process. It implements the three core phases of compiler construction—Lexical Analysis, Syntax Analysis, and Semantic Analysis—providing immediate feedback, error detection, and a dynamic Abstract Syntax Tree (AST) visualization.

Key Features
Custom DSL: Write clean, readable rules using keywords like DEFINE, ALLOW, BLOCK, and any.

3-Phase Compilation:

Lexer: Tokenizes source code and identifies invalid characters.

Parser: Validates grammar and builds a hierarchical AST.

Semantic Analyzer: Checks for logical errors (e.g., undefined variables, invalid IP ranges, port limits).

Visual AST: Automatically draws the Syntax Tree using Mermaid.js, making the parsing logic transparent.

Symbol Table: Tracks variable definitions and types in real-time.

Web Interface: A modern, dark-themed UI built with Flask for an IDE-like experience.

Tech Stack
Backend: Python 3 (Flask)

Frontend: HTML5, CSS3 (Glassmorphism UI), JavaScript

Visualization: Mermaid.js (for Graphing/Trees)

Compiler Concepts: Regex, Recursive Descent Parsing, Context-Free Grammar (CFG)

How It Works
Input: User types rules or uploads a .txt file.

Tokenization: The Lexer breaks the text into a stream of tokens (Keywords, IPs, Numbers).

Parsing: The Parser arranges tokens into a tree structure based on the grammar rules.

Analysis: The Semantic Analyzer walks the tree to ensure the rules make logical sense (e.g., ensuring ports are between 0-65535).

Output: The UI displays the Token Stream, the Visual Syntax Tree, and the Final Symbol Table.
