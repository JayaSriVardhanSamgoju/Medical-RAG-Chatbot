from flask import Flask, render_template, request, session, redirect, url_for
import os
from dotenv import load_dotenv
from markupsafe import Markup

from app.components.retriever import create_qa_chain

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Global QA chain cache to avoid reloading vector store on every request
qa_chain = None

def get_qa_chain():
    global qa_chain
    if qa_chain is None:
        qa_chain = create_qa_chain()
    return qa_chain

def nl2br(value):
    """
    Convert newlines to <br> tags for HTML rendering
    """
    if isinstance(value, str):
        return Markup(value.replace("\n", "<br>\n"))
    return value

app.jinja_env.filters["nl2br"] = nl2br 

@app.route("/", methods=["GET", "POST"])
def index():
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        # Accept 'message' or 'msg' from form or JSON body
        user_input = request.form.get("message") or request.form.get("msg")
        if request.is_json and not user_input:
            data = request.get_json() or {}
            user_input = data.get("message") or data.get("prompt") or data.get("msg")

        if user_input:
            try:
                chain = get_qa_chain()
                result = chain.invoke({"query": user_input})
                answer = result.get("result", "No answer could be retrieved from the medical database.")
            except Exception as e:
                answer = f"Error processing query: {str(e)}"

            # Update session history
            messages = session.get("messages", [])
            messages.append({"role": "user", "content": user_input})
            messages.append({"role": "bot", "content": answer})
            session["messages"] = messages
            session.modified = True

            # If request comes via AJAX/fetch, return JSON
            if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.is_json or request.form.get("ajax"):
                return {"answer": answer, "user_input": user_input}

            return redirect(url_for("index"))

    return render_template("index.html", messages=session.get("messages", []))

@app.route("/clear", methods=["POST"])
def clear():
    session["messages"] = []
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False,use_reloader=False)

