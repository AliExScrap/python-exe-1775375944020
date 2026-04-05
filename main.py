
import webview
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { background: #121212; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
        .calc { width: 350px; background: #1e1e1e; padding: 25px; border-radius: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid #333; }
        #screen { width: 100%; height: 80px; font-size: 40px; text-align: right; background: rgba(0,0,0,0.2); border: none; color: #00ff88; margin-bottom: 25px; padding: 10px; box-sizing: border-box; border-radius: 15px; outline: none; }
        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }
        button { height: 65px; border-radius: 15px; border: none; background: #2a2a2a; color: white; font-size: 22px; cursor: pointer; transition: all 0.2s; }
        button:hover { background: #3a3a3a; }
        button:active { transform: scale(0.95); }
        .op { background: #ff9500; color: white; font-weight: bold; }
        .eq { background: #00ff88; color: #000; grid-column: span 2; font-weight: bold; }
        .clear { color: #ff4444; background: #332222; }
    </style>
</head>
<body>
    <div class="calc">
        <input type="text" id="screen" readonly value="0">
        <div class="grid">
            <button onclick="clr()" class="clear">C</button>
            <button onclick="add('/')" class="op">÷</button>
            <button onclick="add('*')" class="op">×</button>
            <button onclick="del()" class="op">⌫</button>
            <button onclick="add('7')">7</button><button onclick="add('8')">8</button><button onclick="add('9')">9</button>
            <button onclick="add('-')" class="op">-</button>
            <button onclick="add('4')">4</button><button onclick="add('5')">5</button><button onclick="add('6')">6</button>
            <button onclick="add('+')" class="op">+</button>
            <button onclick="add('1')">1</button><button onclick="add('2')">2</button><button onclick="add('3')">3</button>
            <button onclick="calc()" class="eq">=</button>
            <button onclick="add('0')" style="grid-column: span 2;">0</button>
            <button onclick="add('.')">.</button>
        </div>
    </div>
    <script>
        let s = document.getElementById('screen');
        function add(v) { if(s.value === '0') s.value = v; else s.value += v; }
        function clr() { s.value = '0'; }
        function del() { s.value = s.value.slice(0, -1) || '0'; }
        function calc() { try { s.value = eval(s.value); } catch { s.value = 'Erreur'; } }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    webview.create_window('Calculatrice HTML', html=html_content, width=420, height=600, resizable=False)
    webview.start()
