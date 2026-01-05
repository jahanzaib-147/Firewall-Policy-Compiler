# semantic_phase.py
import re
# Import node types from syntax phase to recognize them
from syntax_phase import ProgramNode, VarDeclNode, RuleNode
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.logs = [] 

    def analyze(self, node):
        self.logs = []
        self.symbol_table = {}
        self.visit(node)
        return self.logs, self.symbol_table

    def visit(self, node):
        if isinstance(node, ProgramNode):
            for stmt in node.statements: 
                self.visit(stmt)

        elif isinstance(node, VarDeclNode):
            if node.name in self.symbol_table: 
                raise Exception(f"Semantic Error: Variable '{node.name}' already defined.")
            
            self.symbol_table[node.name] = {'type': 'IP', 'value': node.ip_value}
            self.logs.append(f"[DEFINE] {node.name} = {node.ip_value}")

        elif isinstance(node, RuleNode):
            # Check Scopes
            for item in [node.src, node.dest]:
                if item != 'ANY' and not self.is_ip(item):
                    if item not in self.symbol_table:
                        raise Exception(f"Semantic Error: Undefined variable '{item}' used in rule.")
            
            # Check Port Range
            if not (0 <= node.port <= 65535): 
                raise Exception(f"Semantic Error: Port {node.port} is invalid (Must be 0-65535)")
            
            self.logs.append(f"[RULE] {node.action} {node.protocol} Port {node.port} Validated.")

    def is_ip(self, value):
        return re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', value)