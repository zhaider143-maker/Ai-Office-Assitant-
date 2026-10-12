from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI(title="AI Office Assistant - Syed Zeeshan Haider | Ugoki Sialkot")

@app.get("/", response_class=HTMLResponse)
async def home():
    return '''
<!DOCTYPE html>
<html>
<head>
<title>AI Office Assistant - Syed Zeeshan Haider | Ugoki, Sialkot</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body { font-family: Arial; background: #0f172a; color: white; margin:0; padding:0; }
.header { background: linear-gradient(90deg,#2563eb,#7c3aed); padding:20px; text-align:center; }
.card { background:#1e293b; max-width:700px; margin:30px auto; padding:25px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.3); }
input, button { width:100%; padding:12px; margin:10px 0; border-radius:8px; border:none; }
button { background:#2563eb; color:white; font-weight:bold; cursor:pointer; }
.chat { background:#0f172a; padding:15px; border-radius:10px; min-height:200px; margin:15px 0; text-align:left; }
.footer { text-align:center; padding:15px; color:#94a3b8; font-size:13px; }
.badge { background:#10b981; padding:5px 10px; border-radius:20px; font-size:12px; }
</style>
</head>
<body>
<div class="header">
<h1>AI Office Assistant</h1>
<p>By Syed Zeeshan Haider | Ugoki, Sialkot, Pakistan</p>
<span class="badge">LIVE & Ready</span>
</div>
<div class="card">
<h3>Talk to AI Receptionist</h3>
<div class="chat" id="chat">
<p><b>AI:</b> Assalam-o-Alaikum! I am AI Assistant from Ugoki, Sialkot. How can I help you today?</p>
</div>
<input type="text" id="msg" placeholder="Type: I want demo">
<button onclick="send()">Send Message</button>
<button onclick="demo()" style="background:#10b981;">Get Demo - Call Zeeshan</button>
</div>
<div class="footer">
<p>Ugoki, Sialkot, Pakistan | Syed Zeeshan Haider | 9 AM - 9 PM PKT</p>
<p>For demo: Call / WhatsApp Zeeshan Haider</p>
<p>Built with love in Pakistan | FREE - No Vapi Fees!</p>
</div>
<script>
function send(){
  let m=document.getElementById('msg').value;
  if(!m) return;
  let c=document.getElementById('chat');
  c.innerHTML+='<p><b>You:</b> '+m+'</p>';
  let reply='';
  if(m.toLowerCase().includes('demo') || m.toLowerCase().includes('price') || m.toLowerCase().includes('buy')){
    reply='For live demo and business details, please call / WhatsApp Syed Zeeshan Haider from Ugoki, Sialkot. Timing: 9 AM to 9 PM PKT.';
  } else {
    reply='Thank you! I am AI Office Assistant serving Ugoki, Sialkot businesses. I can handle appointments and customer queries 24/7. Want demo? Just ask!';
  }
  setTimeout(()=>{ c.innerHTML+='<p><b>AI:</b> '+reply+'</p>'; }, 500);
  document.getElementById('msg').value='';
}
function demo(){
  alert('For LIVE DEMO & Pricing: Call / WhatsApp Syed Zeeshan Haider Ugoki, Sialkot');
}
</script>
</body>
</html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
