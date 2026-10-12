
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import datetime

app = FastAPI()

# ===== EDIT YOUR DETAILS HERE =====
OWNER_NAME = "Syed Zeeshan Haider"
OWNER_BUSINESS = "AI Office Assistant - Ugoki, Sialkot"
OWNER_MOBILE = "+92 321 6732766"  # YOUR MOBILE + WHATSAPP - Syed Zeeshan Haider
OWNER_LOCATION = "Ugoki, Sialkot, Punjab, Pakistan"
GREETING = "Assalam-o-Alaikum! Thank you for calling Syed Zeeshan Haider from Ugoki, Sialkot. This is my own AI receptionist - LIVE demo on my number +92 321 6732766!"
# ==================================

leads = []

HTML_PAGE = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Receptionist LIVE - {name}</title>
<style>
body{{font-family:Arial;background:#0f172a;color:white;margin:0;padding:12px}}
.card{{max-width:700px;margin:auto;background:#1e293b;border-radius:18px;padding:20px}}
h1{{color:#38bdf8}} .live{{background:#22c55e;color:black;padding:4px 12px;border-radius:20px;font-size:12px}}
.btn{{width:100%;padding:15px;border-radius:12px;border:none;font-weight:bold;margin:8px 0;cursor:pointer;font-size:15px}}
.green{{background:#25D366;color:black}} .blue{{background:#3b82f6;color:white}} .dark{{background:#0f172a;color:#38bdf8;border:1px solid #38bdf8}}
.box{{background:#0f172a;padding:12px;border-radius:10px;margin:10px 0;border-left:4px solid #22c55e}}
#chat{{background:#0f172a;height:200px;overflow-y:auto;padding:10px;border-radius:10px}}
input{{width:100%;padding:12px;border-radius:8px;border:none;background:#0f172a;color:white;box-sizing:border-box;margin:5px 0}}
</style></head>
<body><div class="card">
<h1>📞 AI Receptionist <span class="live">● LIVE ON MY NUMBER</span></h1>
<p><b>{name}</b> | {business}<br>📍 {location}<br>📱 <b>{mobile}</b> (Mobile + WhatsApp)</p>

<div class="box">
<b>🔴 Client asks: "Apke paas khud AI hai?"</b><br>
<b>YOUR ANSWER:</b> "Ji bilkul! Abhi test karo - Mere number {mobile} pe WhatsApp Hi bhejo ya neeche Call button dabao - AI live hai! Yehi apke business pe lagega!"<br><br>
✅ WhatsApp AI - FREE, 24/7<br>
✅ Calling AI - Browser Call FREE<br>
✅ My number SAME - No change!
</div>

<h3>📱 Test 1: WhatsApp AI</h3>
<button class="btn green" onclick="window.open('https://wa.me/{wa}?text=Hi%20Zeeshan%20AI%20demo','_blank')">💬 WhatsApp My AI - {mobile}</button>

<h3>📞 Test 2: Calling AI (FREE - No Replit upgrade)</h3>
<button class="btn blue" id="callBtn" onclick="startCall()">📞 Call My AI - LIVE Voice Demo</button>
<p id="status" style="text-align:center;font-size:13px"></p>

<h3>💬 Test 3: Web Chat</h3>
<div id="chat"><b>AI:</b> {greeting} Apna naam aur business batayen?<br><br></div>
<input id="msg" placeholder="I need AI for my clinic..."><button class="btn dark" onclick="sendChat()">Send</button>

<h3>📋 Leads AI Collected</h3><div id="leads">{leads}</div>
<p style="font-size:10px;opacity:.6;margin-top:12px">FREE hosting on Render - No Replit upgrade - Rs.20K setup for clients</p>
</div>
<script>
async function startCall(){{
  let st=document.getElementById('status'); let btn=document.getElementById('callBtn');
  try{{
    st.innerText='🎤 Starting mic... Allow permission';
    await navigator.mediaDevices.getUserMedia({{audio:true}});
    let u=new SpeechSynthesisUtterance('{greeting} Apna naam aur shop batayen.');
    u.lang='en-IN'; u.rate=0.9; speechSynthesis.speak(u);
    st.innerText='✅ AI Speaking...';
    u.onend=()=>{{
      const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
      if(!SR){{st.innerText='Use Chrome browser'; return;}}
      let r=new SR(); r.lang='en-IN';
      r.onresult=(e)=>{{
        let t=e.results[0][0].transcript;
        st.innerText='You: '+t+' - Sending to Zeeshan...';
        fetch('/collect',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{speech:t, caller:'Browser Call'}})}});
        let rp=new SpeechSynthesisUtterance('Shukria '+t+'! Details Zeeshan ko bhej di. Wo 5 min me call karenge. Ye tha apke business ka live demo. Allah Hafiz!');
        rp.lang='en-IN'; speechSynthesis.speak(rp);
        btn.innerText='✅ Call Done - Lead Sent!';
      }};
      r.start(); st.innerText='🎤 Listening... Boliye';
    }};
  }}catch(e){{st.innerText='❌ Allow mic: '+e.message}}
}}
async function sendChat(){{
  let m=document.getElementById('msg').value; if(!m) return;
  let c=document.getElementById('chat'); c.innerHTML+='<b>You:</b> '+m+'<br>'; document.getElementById('msg').value='';
  let res=await fetch('/chat',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{message:m}})}});
  let d=await res.json(); c.innerHTML+='<b>AI:</b> '+d.reply+'<br><br>'; c.scrollTop=c.scrollHeight;
}}
</script></body></html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    leads_html = "".join([f"<div style='background:#0f172a;padding:6px;margin:4px 0;border-radius:6px'>📞 {l['speech'][:60]} - {l['caller']} - {l['time']}</div>" for l in leads[-5:][::-1]]) or "<i>No calls yet - Waiting...</i>"
    wa = OWNER_MOBILE.replace("+","").replace("-","").replace(" ","")
    return HTML_PAGE.format(name=OWNER_NAME, business=OWNER_BUSINESS, location=OWNER_LOCATION, mobile=OWNER_MOBILE, wa=wa, greeting=GREETING, leads=leads_html)

@app.post("/chat")
async def chat_api(req: Request):
    data = await req.json()
    msg = data.get("message","").lower()
    if "pizza" in msg or "burger" in msg:
        reply = f"Pizza shop ke liye WhatsApp AI - Apka mobile {OWNER_MOBILE} same rahega! Customer WhatsApp karega, AI menu + order lega. Rs.20K setup, no minutes! Test karo - Mere {OWNER_MOBILE} pe WhatsApp Hi bhejo!"
    elif "clinic" in msg:
        reply = f"Clinic ke liye PTCL device Rs.6000 + AI. Number {OWNER_MOBILE} same! AI 24/7. Rs.20K setup. Mere number pe call button dabao - Live demo!"
    else:
        reply = f"Main {OWNER_NAME} ka AI hoon! Mera number {OWNER_MOBILE} pe live hoon. WhatsApp Hi bhejo ya Call button dabao - Demo dekho! Apka business kya hai?"
    return {"reply": reply}

@app.post("/collect")
async def collect(req: Request):
    data = await req.json()
    data["time"] = datetime.datetime.now().strftime("%I:%M %p")
    leads.append(data)
    return {"ok": True}

@app.get("/leads")
async def get_leads():
    return leads
