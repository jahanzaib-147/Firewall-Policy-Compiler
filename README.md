# 🔥 Firewall Policy Compiler

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

A **Domain-Specific Language (DSL)** compiler designed to validate and visualize network firewall rules. This project implements the core phases of compiler construction—Lexical, Syntax, and Semantic Analysis—wrapped in a modern web interface.

## 🚀 Features

- **Custom DSL:** Write human-readable rules (e.g., `ALLOW TCP FROM office TO server PORT 80`).
- **3-Phase Compilation:**
  - **Lexical Analysis:** Tokenizes input and handles errors.
  - **Syntax Analysis:** Builds an Abstract Syntax Tree (AST) using Recursive Descent Parsing.
  - **Semantic Analysis:** Validates logic, scopes, and types (IPs, Ports).
- **Visualizations:** Auto-generates interactive AST diagrams using **Mermaid.js**.
- **Web UI:** Modern, Dark-Mode interface built with **Flask** and **CSS Glassmorphism**.

## 🛠️ Technology Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript
- **Visualization:** Mermaid.js
- **Concepts:** Regex, Context-Free Grammar (CFG), Symbol Tables

## 📸 Screenshots

*(You can drag and drop screenshots of your UI here later)*

## 📦 Installation & Run

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Firewall-Policy-Compiler.git](https://github.com/YOUR_USERNAME/Firewall-Policy-Compiler.git)
   cd Firewall-Policy-Compiler
