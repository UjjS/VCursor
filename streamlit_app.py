import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_code_editor import code_editor
from openai import OpenAI

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI config
st.set_page_config(page_title="Cursor Clone", layout="wide")
st.title("💡 Cursor Clone using Code Editor")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Write your code")

    language = st.selectbox(
        "Select Language",
        ["python", "javascript", "java", "cpp", "csharp", "go", "rust", "typescript", "html", "css", "sql"]
    )

    # Language-specific starter code
    default_code = {
        "python": "def hello(name):\n    return f'Hello, {name}!'",
        "javascript": "function hello(name) {\n    return `Hello, ${name}!`;\n}",
        "java": "public class Hello {\n    public String hello(String name) {\n        return \"Hello, \" + name + \"!\";\n    }\n}",
        "cpp": "#include <iostream>\n\nstd::string hello(std::string name) {\n    return \"Hello, \" + name + \"!\";\n}",
        "csharp": "public string Hello(string name)\n{\n    return $\"Hello, {name}!\";\n}",
        "go": "func hello(name string) string {\n    return fmt.Sprintf(\"Hello, %s!\", name)\n}",
        "rust": "fn hello(name: &str) -> String {\n    format!(\"Hello, {}!\", name)\n}",
        "typescript": "function hello(name: string): string {\n    return `Hello, ${name}!`;\n}",
        "html": "<!DOCTYPE html>\n<html>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>",
        "css": "body {\n    background-color: #f0f0f0;\n    font-family: Arial, sans-serif;\n}",
        "sql": "SELECT * FROM users\nWHERE name = 'John';\n"
    }

    # Initialize editor
    content = {
        "text": default_code[language],
        "language": language,
        "theme": "vs-dark",
    }

    result = code_editor(content, height=400, key="code_
