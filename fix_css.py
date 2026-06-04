import re

with open('index.html', 'r') as f:
    content = f.read()

old_body_css = """        body {
            background-color: #1a1a1a;
            color: #e0e0e0;
            font-family: 'Pricedown', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            user-select: none;
        }"""

new_body_css = """        body {
            background-color: #1a1a1a;
            color: #e0e0e0;
            font-family: 'Pricedown', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem 0;
            min-height: 100vh;
            margin: 0;
            user-select: none;
            box-sizing: border-box;
        }"""

content = content.replace(old_body_css, new_body_css)

with open('index.html', 'w') as f:
    f.write(content)
