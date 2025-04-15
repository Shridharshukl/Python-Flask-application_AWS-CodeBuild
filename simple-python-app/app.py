from flask import Flask

app = Flask(__name__)

@app.route('/')
def portfolio():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Shridhar Shukla | Portfolio</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #f0f2f5;
          margin: 0;
          padding: 0;
        }
        header {
          background: #333;
          color: white;
          padding: 2rem;
          text-align: center;
        }
        main {
          padding: 2rem;
          max-width: 800px;
          margin: auto;
          background: white;
          box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
          color: #333;
        }
        .section {
          margin-bottom: 2rem;
        }
        footer {
          text-align: center;
          padding: 1rem;
          background: #333;
          color: white;
          position: fixed;
          width: 100%;
          bottom: 0;
        }
      </style>
    </head>
    <body>

    <header>
      <h1>Shridhar Shukla</h1>
      <p>MCA Student | 5⭐ HackerRank | 650+ LeetCode Qs</p>
    </header>

    <main>
      <div class="section">
        <h2>About Me</h2>
        <p>Hello! I'm Shridhar from India. Passionate about problem-solving, cloud tech, and building cool things in code.</p>
      </div>

      <div class="section">
        <h2>Projects</h2>
        <ul>
          <li>🌦️ Terraform Weather App (Real-time)</li>
          <li>📦 Hostel Management Platform (in progress)</li>
          <li>💻 Many more on GitHub: <a href="https://github.com/Shridharshukl" target="_blank">Shridharshukl</a></li>
        </ul>
      </div>

      <div class="section">
        <h2>Contact</h2>
        <p>Email: shridhar@example.com</p>
        <p>GitHub: <a href="https://github.com/Shridharshukl" target="_blank">Shridharshukl</a></p>
      </div>
    </main>

    <footer>
      &copy; 2025 Shridhar Shukla
    </footer>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
