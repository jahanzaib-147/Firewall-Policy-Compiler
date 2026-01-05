from flask import Flask, render_template, request
import uuid

# Import phases
from lexical_phase import LexicalAnalyzer
from syntax_phase import SyntaxAnalyzer, ProgramNode, VarDeclNode, RuleNode, LeafNode
from semantic_phase import SemanticAnalyzer

app = Flask(__name__)

# --- Helper: Convert AST to Mermaid Graph ---
def generate_mermaid(node):
    edges = []
    def traverse(current_node, parent_id=None):
        # Create unique ID for every node
        node_id = f"node_{uuid.uuid4().hex[:6]}"
        
        # Clean label for web display
        label = current_node.get_label().replace('\n', '<br>')
        
        # Assign CSS classes based on node type
        style_class = ":::leaf"
        if isinstance(current_node, ProgramNode): style_class = ":::root"
        elif isinstance(current_node, VarDeclNode): style_class = ":::decl"
        elif isinstance(current_node, RuleNode): style_class = ":::rule"
        
        # Add Node Definition
        edges.append(f'{node_id}["{label}"]{style_class}')

        # Add Edge (Line) from Parent
        if parent_id: 
            edges.append(f"{parent_id} --> {node_id}")

        # Process Children
        children = []
        if isinstance(current_node, ProgramNode): children = current_node.statements
        elif isinstance(current_node, VarDeclNode): children = [LeafNode(current_node.ip_value, "IP")]
        elif isinstance(current_node, RuleNode): 
            children = [LeafNode(current_node.src, "From"), LeafNode(current_node.dest, "To"), LeafNode(str(current_node.port), "Port")]
        
        for child in children: 
            traverse(child, node_id)

    traverse(node)
    return "\n".join(edges)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = "DEFINE server = 192.168.1.50;\nALLOW TCP FROM ANY TO server PORT 80;"
    result = None
    
    if request.method == 'POST':
        # 1. Check for File Upload
        if 'file_upload' in request.files and request.files['file_upload'].filename != '':
            file = request.files['file_upload']
            try:
                code = file.read().decode('utf-8')
                print(">> File Uploaded Successfully")
            except Exception as e:
                return render_template('index.html', code=code, result={"error": f"File Read Error: {e}", "success": False})
        else:
            # 2. Check Text Area
            code = request.form.get('source_code', code)

        print(f">> Compiling Code:\n{code}")

        # --- Compilation Process ---
        try:
            # Phase 1: Lexer
            lexer = LexicalAnalyzer(code)
            tokens = lexer.tokenize()
            
            # Phase 2: Parser
            parser = SyntaxAnalyzer(tokens)
            ast_root = parser.parse()
            graph_data = generate_mermaid(ast_root) # Generate Visual Tree

            # Phase 3: Semantic
            analyzer = SemanticAnalyzer()
            logs, symbols = analyzer.analyze(ast_root)

            result = {
                "tokens": tokens,
                "graph_data": graph_data,
                "logs": logs,
                "symbols": symbols,
                "success": True
            }
            print(">> Compilation Successful!")
            
        except Exception as e:
            print(f">> Error: {e}")
            result = {"error": str(e), "success": False}

    return render_template('index.html', code=code, result=result)

if __name__ == '__main__':
    app.run(debug=True)