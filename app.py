from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; }
        table { border-collapse: collapse; margin-top: 20px; }
        td, th { border: 1px solid black; padding: 10px; text-align: center; }
        input { padding: 8px; }
        button { padding: 8px; }
    </style>
</head>
<body>
    <h1>Multiplication Table Generator</h1>
    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Generate</button>
    </form>

    {% if table %}
        <h2>Multiplication Table of {{ number }}</h2>
        <table>
            {% for row in table %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>x</td>
                    <td>{{ row[1] }}</td>
                    <td>=</td>
                    <td>{{ row[2] }}</td>
                </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    number = None

    if request.method == "POST":
        number = int(request.form["number"])
        table = [(number, i, number * i) for i in range(1, 11)]

    return render_template_string(html_template, table=table, number=number)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5000, debug=True)

