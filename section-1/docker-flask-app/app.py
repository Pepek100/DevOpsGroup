from flask import Flask  
 
app = Flask(__name__)  
 
@app.route('/')  
def hello():  
    return "Hello, Docker! 🐳"  
 
if __name__ == '__main__':  
    # Run the app on all available network interfaces (0.0.0.0) and port 5000  
    app.run(host='0.0.0.0', port=5000)
