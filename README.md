# 🔥 Firewall Policy Compiler

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![Mermaid.js](https://img.shields.io/badge/Mermaid.js-Visualization-ff69b4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A **Domain-Specific Language (DSL)** compiler designed to simplify, validate, and visualize network firewall rules. This project implements the core phases of compiler construction—Lexical, Syntax, and Semantic Analysis—wrapped in a modern, dark-themed web interface.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Technology Stack](#-technology-stack)
- [Installation & Setup](#-installation--setup)
- [How to Use](#-how-to-use)
- [Sample Code](#-sample-code)
- [Screenshots](#-screenshots)
- [Author](#-author)
- [License](#-license)

---

## 🛡️ About the Project

Network security configurations are often prone to human error. A single typo in an IP address or a wrong port number can leave a system vulnerable. 

The **Firewall Policy Compiler** solves this by allowing administrators to write rules in a high-level, human-readable language. The compiler parses these rules, checks for logical errors (like undefined variables or invalid IP ranges), and visualizes the logic structure before deployment.

It was built as a semester project for the **Compiler Construction** course to demonstrate the practical application of parsing theory.

---

## 🚀 Key Features

* **Custom DSL:** Write clean rules using keywords like `DEFINE`, `ALLOW`, `BLOCK`, `TCP`, `UDP`.
* **3-Phase Compilation:**
    * **Lexical Analysis:** Tokenizes input and filters whitespace/comments.
    * **Syntax Analysis:** Uses Recursive Descent Parsing to build an Abstract Syntax Tree (AST).
    * **Semantic Analysis:** Validates scope, data types, and logical constraints (e.g., Ports 0-65535).
* **Visual AST:** Automatically renders the Syntax Tree using **Mermaid.js** for debugging.
* **Symbol Table:** Real-time tracking of variable definitions and types.
* **Modern Web UI:** A Cyberpunk/Glassmorphism styled interface built with Flask.
* **File Upload:** Support for uploading `.txt` or `.frl` script files.

---

## 🏗️ Project Architecture

The compiler follows the standard **Analysis-Synthesis Model**:

1.  **Input Source:** Raw text from the web editor or uploaded file.
2.  **Lexer (`lexical_phase.py`):** Scans text and produces a stream of `Token` objects.
3.  **Parser (`syntax_phase.py`):** Consumes tokens to verify grammar and builds the `ASTNode` hierarchy.
4.  **Semantic Analyzer (`semantic_phase.py`):** Traverses the AST to populate the **Symbol Table** and check for logical errors.
5.  **Frontend (`app.py` + HTML):** Receives the AST and logs, converting them into a visual graph and report.

---

## 🛠️ Technology Stack

* **Backend:** Python 3 (Flask Framework)
* **Frontend:** HTML5, CSS3 (Flexbox/Grid), JavaScript
* **Visualization:** Mermaid.js (for Tree Diagrams)
* **Concepts Used:** Regex, Context-Free Grammar (CFG), Recursive Descent Parsing

---

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Firewall-Policy-Compiler.git](https://github.com/YOUR_USERNAME/Firewall-Policy-Compiler.git)
    cd Firewall-Policy-Compiler
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install flask
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the Compiler**
    Open your browser and visit: `http://127.0.0.1:5000`

---

## 🎮 How to Use

1.  **Define Variables:** Use `DEFINE name = IP;` to store IP addresses.
2.  **Write Rules:** Use the format `ACTION PROTOCOL FROM source TO dest PORT number;`.
3.  **Compile:** Click the **"Compile & Visualize"** button.
4.  **Analyze:**
    * Check the **Syntax Tree** to see how the parser understood your code.
    * Review the **Symbol Table** to see stored variables.
    * Check **Logs** for any semantic errors (red) or success messages (green).

---

## 🧪 Sample Code

Copy and paste this into the editor to test the compiler:

```text
DEFINE office_network = 192.168.1.0;
DEFINE web_server = 10.0.0.50;

# Allow HTTP Traffic
ALLOW TCP FROM office_network TO web_server PORT 80;

# Secure Shell (SSH) Access
ALLOW TCP FROM office_network TO web_server PORT 22;

# Block DNS from outside
BLOCK UDP FROM ANY TO office_network PORT 53;
```

## 👤 Author

**Muhammad Jahanzaib**

* 🎓 BSCS Computer Science Student
* 💻 Focus areas: Network Security, and Web Development.

). 
-->

---

## 📄 License

This project is open-source and available under the **MIT License**.

You are free to use, study, modify, and distribute this software for educational or commercial purposes. Please see the `LICENSE` file in this repository for full details.
