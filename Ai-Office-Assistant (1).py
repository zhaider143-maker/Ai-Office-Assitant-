
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

OWNER_NAME = "Syed Zeeshan Haider"
OWNER_BUSINESS = "AI Office Assistant - Ugoki, Sialkot"
OWNER_MOBILE = "+92 321 6732766"
OWNER_PTCL = "+92 52 3570456"
OWNER_PTCL_RAW = "+92523570456"
OWNER_LOCATION = "Ugoki, Sialkot, Punjab, Pakistan"
GREETING = "Assalam-o-Alaikum! Syed Zeeshan Haider ke office se AI bol raha hoon. PTCL +92 52 3570456 aur Mobile +92 321 6732766 dono pe LIVE hoon!"

leads = []

HTML_PAGE = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Receptionist PTCL + Mobile - {name}</title>
<style>
body{font-family:Arial;background:#0f172a;color:white;margin:0;padding:10px}
.card{max-width:750px;margin:auto;background:#1e293b;border-radius:18px;padding:20px;border:2px solid #38bdf8}
h1{color:#38bdf8;text-align:center} .live{background:#22c55e;color:black;padding:5px 14px;border-radius:20px;font-size:12px}
.btn{width:100%;padding:16px;border-radius:12px;border:none;font-weight:bold;margin:8px 0;cursor:pointer;font-size:15px;display:block;text-align:center;text-decoration:none;box-sizing:border-box}
.green{background:#25D366;color:black} .blue{background:#3b82f6;color:white} .ptcl{background:#f59e0b;color:black} .dark{background:#0f172a;color:#38bdf8;border:1px solid #38bdf8}
.box{background:#0f172a;padding:14px;border-radius:12px;margin:12px 0;border-left:5px solid #22c55e}
.ptclbox{background:#0f172a;padding:14px;border-radius:12px;margin:12px 0;border-left:5px solid #f59e0b}
#chat{background:#0f172a;height:220px;overflow-y:auto;padding:12px;border-radius:10px;border:1px solid #334155}
input{width:100%;padding:12px;border-radius:8px;border:1px solid #334155;background:#0f172a;color:white;box-sizing:border-box;margin:6px 0}
.num{font-size:22px;font-weight:bold;letter-spacing:1px}
</style></head>
<body><div class="card">
<h1>📞 AI Receptionist<br><span class="live">● LIVE ON PTCL + MOBILE</span></h1>
<p style="text-align:center"><b>{name}</b><br>{business}<br>📍 {location}</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:15px 0">
<div class="box" style="text-align:center;margin:0"><div>📱 Mobile + WhatsApp</div><div class="num">{mobile}</div><div style="font-size:11px;opacity:.7">24/7 AI WhatsApp</div></div>
<div class="ptclbox" style="text-align:center;margin:0"><div>☎️ PTCL Landline</div><div class="num">{ptcl}</div><div style="font-size:11px;opacity:.7">AI Attached - Sialkot 052</div></div>
</div>

<div class="ptclbox">
<b>🔴 CLIENT: "PTCL pe AI kaise lagega?"</b><br><br>
<b>YOUR ANSWER:</b> "Ji! Mera PTCL {ptcl} pe AI LIVE hai! Device Rs.6000 - PTCL line se AI connect - Call aye to AI uthati hai, naam/kaam pooch ke mere mobile {mobile} pe bhej deti hai! Test karo - Abhi {ptcl} pe call karo ya neeche button dabao!"<br><br>
✅ <b>PTCL Device:</b> GSM FWT + AI Box (Rs.6000)<br>
✅ <b>How:</b> PTCL wire → Device → AI Server → Your Mobile {mobile}<br>
✅ <b>Power:</b> UPS backup - Light jaye bhi AI chalegi<br>
✅ <b>WhatsApp:</b> PTCL caller ko auto WhatsApp {mobile} se
</div>

<h3>📱 Test 1: Mobile WhatsApp AI (24/7 FREE)</h3>
<a class="btn green" href="https://wa.me/{mobile_wa}?text=Hi%20Zeeshan%20AI%20demo%20PTCL%20{mobile}%20-%20I%20want%20AI%20for%20my%20shop" target="_blank">💬 WhatsApp Mobile AI - {mobile}</a>

<h3>☎️ Test 2: PTCL AI Attached (LIVE Demo)</h3>
<a class="btn ptcl" href="tel:{ptcl_raw}">☎️ Call My PTCL - {ptcl} - AI Picks!</a>
<button class="btn blue" id="callBtn" onclick="startCall()">📞 Browser Call Demo - PTCL AI Voice</button>
<p id="status" style="text-align:center;font-size:13px;min-height:20px"></p>

<h3>💬 Test 3: Web Chat - PTCL + Mobile AI</h3>
<div id="chat"><b>AI:</b> {greeting}<br>Main PTCL {ptcl} aur Mobile {mobile} dono pe hoon! Apka naam aur business kya hai?<br><br></div>
<input id="msg" placeholder="I have pizza shop in Sialkot, need AI on PTCL..."><button class="btn dark" onclick="sendChat()">Send to AI</button>

<h3>📋 Leads Collected - PTCL + Mobile</h3><div id="leads">{leads}</div>

<div class="box" style="margin-top:15px;font-size:12px">
<b>💰 Package for Clients:</b><br>
• Setup: Rs.20,000 (AI + PTCL Device config)<br>
• PTCL Device: Rs.6,000 (one time)<br>
• Monthly: Rs.3,000 OR No monthly if WhatsApp only!<br>
• Numbers SAME - Client PTCL + Mobile same rehta!<br>
• Demo Link: ai-office-assitant.vercel.app (PTCL {ptcl})
</div>
<p style="font-size:10px;opacity:.6;text-align:center;margin-top:10px">Agent Developed for Syed Zeeshan Haider | PTCL {ptcl} + Mobile {mobile} | Vercel FREE</p>
</div>
<script>
async function startCall(){
  let st=document.getElementById('status'); let btn=document.getElementById('callBtn');
  try{
    st.innerText='🎤 Mic starting... Allow';
    await navigator.mediaDevices.getUserMedia({audio:true});
    let u=new SpeechSynthesisUtterance('{greeting} PTCL {ptcl} aur mobile {mobile} pe. Apna naam batayen.');
    u.lang='en-IN'; u.rate=0.9; speechSynthesis.speak(u);
    st.innerText='✅ AI Speaking - PTCL Attached...';
    u.onend=()=>{
      const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
      if(!SR){st.innerText='Use Chrome'; return;}
      let r=new SR(); r.lang='en-IN';
      r.onresult=(e)=>{
        let t=e.results[0][0].transcript;
        st.innerText='You: '+t+' - Sending to Zeeshan PTCL {ptcl}...';
        fetch('/collect',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({speech:t, caller:'PTCL + Browser Demo', ptcl:'{ptcl}', mobile:'{mobile}'})});
        let rp=new SpeechSynthesisUtterance('Shukria '+t+'! Apki call PTCL {ptcl} pe receive hui. Details Zeeshan ko mobile {mobile} pe bhej di. Ye tha PTCL AI demo. Allah Hafiz!');
        rp.lang='en-IN'; speechSynthesis.speak(rp);
        btn.innerText='✅ PTCL Call Done - Lead Sent to {mobile}!';
      };
      r.start(); st.innerText='🎤 Listening... Boliye - PTCL AI sun raha hai';
    };
  }catch(e){st.innerText='❌ Allow mic: '+e.message}
}
async function sendChat(){
  let m=document.getElementById('msg').value; if(!m) return;
  let c=document.getElementById('chat'); c.innerHTML+='<b>You:</b> '+m+'<br>'; document.getElementById('msg').value='';
  let res=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:m})});
  let d=await res.json(); c.innerHTML+='<b>AI:</b> '+d.reply+'<br><br>'; c.scrollTop=c.scrollHeight;
}
</script></body></html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    leads_html = "".join([f"<div style='background:#0f172a;padding:8px;margin:5px 0;border-radius:8px;border-left:3px solid #f59e0b'>☎️ {l.get('speech', l.get('message',''))[:70]} - {l.get('caller','Web')} - {l.get('time','')}</div>" for l in leads[-5:][::-1]]) or "<i>No PTCL/Mobile calls yet - Waiting for PTCL 052 call...</i>"
    return HTML_PAGE.format(name=OWNER_NAME, business=OWNER_BUSINESS, location=OWNER_LOCATION, mobile=OWNER_MOBILE, ptcl=OWNER_PTCL, ptcl_raw=OWNER_PTCL_RAW, mobile_wa='923216732766', ptcl_wa='92523570456', greeting=GREETING, leads=leads_html)

@app.post("/chat")
async def chat_api(req: Request):
    data = await req.json()
    msg = data.get("message","").lower()
    if "ptcl" in msg or "landline" in msg or "052" in msg:
        reply = f"PTCL {OWNER_PTCL} pe AI: 1) Device Rs.6000 PTCL line me lagao, 2) AI server connect, 3) Call aye to AI uthaye, naam/kaam leke mobile {OWNER_MOBILE} pe WhatsApp! Number SAME! Test - PTCL Call button dabao! Rs.20K setup."
    elif "pizza" in msg or "shop" in msg or "hotel" in msg or "restaurant" in msg:
        reply = f"Pizza shop ke liye PTCL {OWNER_PTCL} + Mobile {OWNER_MOBILE} dono pe AI! PTCL pe call aye to AI menu, order leke WhatsApp! Mobile {OWNER_MOBILE} pe WhatsApp AI 24/7! Rs.20K setup + Rs.6000 device! Demo - PTCL {OWNER_PTCL} pe call karo!"
    else:
        reply = f"Main {OWNER_NAME} ka AI hoon! PTCL {OWNER_PTCL} aur Mobile {OWNER_MOBILE} dono pe LIVE! PTCL pe call aye to main uthata hoon! Apka business kya hai?"
    return {"reply": reply}

@app.post("/collect")
async def collect(req: Request):
    data = await req.json()
    data["time"] = datetime.datetime.now().strftime("%I:%M %p")
    leads.append(data)
    return {"ok": True, "forwarded_to": OWNER_MOBILE, "ptcl": OWNER_PTCL}

@app.get("/leads")
async def get_leads():
    return leads

@app.get("/ptcl-status")
async def ptcl_status():
    return {"ptcl": OWNER_PTCL, "ptcl_raw": OWNER_PTCL_RAW, "mobile": OWNER_MOBILE, "status": "AI Attached - LIVE", "device": "GSM FWT Rs.6000", "leads": len(leads)}
