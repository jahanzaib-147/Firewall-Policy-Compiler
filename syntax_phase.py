# syntax_phase.py

# --- AST Node Definitions ---
class ASTNode: 
    def get_label(self): return "Node"
    def get_color(self): return "#555" 

class ProgramNode(ASTNode):
    def __init__(self, statements): self.statements = statements
    def get_label(self): return "ROOT\nProgram"
    def get_color(self): return "#61afef" # Blue

class VarDeclNode(ASTNode):
    def __init__(self, name, ip_value, line):
        self.name = name
        self.ip_value = ip_value
        self.line = line
    def get_label(self): return f"DEFINE\n{self.name}"
    def get_color(self): return "#98c379" # Green

class RuleNode(ASTNode):
    def __init__(self, action, protocol, src, dest, port, line):
        self.action = action
        self.protocol = protocol
        self.src = src
        self.dest = dest
        self.port = port
        self.line = line
    def get_label(self): return f"{self.action}\n{self.protocol}"
    def get_color(self): return "#e06c75" if self.action == "BLOCK" else "#e5c07b"

class LeafNode(ASTNode): 
    def __init__(self, value, label=""):
        self.value = value
        self.label = label
    def get_label(self): return f"{self.label}\n{self.value}"
    def get_color(self): return "#abb2bf" # Grey

# --- Syntax Analyzer Class ---
class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == expected_type:
            self.pos += 1
            return self.tokens[self.pos - 1]
        else:
            current = self.tokens[self.pos] if self.pos < len(self.tokens) else "EOF"
            raise Exception(f"Syntax Error: Expected '{expected_type}' but found '{current.value}'")

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            if self.tokens[self.pos].type == 'DEFINE': 
                statements.append(self.parse_var_decl())
            elif self.tokens[self.pos].type == 'ACTION': 
                statements.append(self.parse_rule())
            else: 
                raise Exception(f"Syntax Error: Unexpected token '{self.tokens[self.pos].value}'")
        return ProgramNode(statements)

    def parse_var_decl(self):
        t = self.consume('DEFINE')
        name = self.consume('IDENTIFIER').value
        self.consume('EQUALS')
        ip = self.consume('IP').value
        self.consume('SEMICOLON')
        return VarDeclNode(name, ip, t.line)

    def parse_rule(self):
        t = self.consume('ACTION')
        proto = self.consume('PROTOCOL').value
        self.consume('FROM')
        if self.tokens[self.pos].type in ['IP', 'IDENTIFIER', 'ANY']: 
            src = self.tokens[self.pos].value
        else: 
            raise Exception("Syntax Error: Invalid Source")
        self.pos += 1

        self.consume('TO')
        if self.tokens[self.pos].type in ['IP', 'IDENTIFIER', 'ANY']: 
            dest = self.tokens[self.pos].value
        else: 
            raise Exception("Syntax Error: Invalid Destination")
        self.pos += 1

        self.consume('PORT_KEY')
        port = int(self.consume('NUMBER').value)
        self.consume('SEMICOLON')
        return RuleNode(t.value, proto, src, dest, port, t.line)