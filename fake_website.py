from flask import Flask, request, render_template_string

app = Flask(__name__)

FAKE_USERNAME = "user123"
FAKE_PASSWORD = "mypassword"

LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Fake Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required><br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required><br>
        <button type="submit">Login</button>
    </form>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == FAKE_USERNAME and password == FAKE_PASSWORD:
            return "Login successful!"
        else:
            error = "Invalid credentials"
    return render_template_string(LOGIN_PAGE, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
