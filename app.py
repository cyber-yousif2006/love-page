import json
import streamlit as st
import streamlit.components.v1 as components

# ✏️ نامەکان لێرە بگۆڕە یان زیاد بکە: ["ئیمۆجی", "نامە"]
MESSAGES = [
    ["👀", "من بە یەکەم بینینی چاوت، لە ناو چاوەکانت نقووم بووم."],
    ["🌸", "لەو ڕۆژەوە، هەموو شتێک جوانتر بوو."],
    ["☀️", "زەردەخەنەکەت وەک خۆر، دڵی منی گەرم دەکاتەوە."],
    ["🌙", "لەگەڵ تۆ، هەموو شەوێک ئارامە."],
    ["🎨", "تۆ ئەو ڕەنگەی کە ژیانی منت پێ ڕازاندەوە."],
    ["🪷", "تۆ وەک گوڵی لیلی، پاک و جوانی."],
    ["🦢", "وەک دوو باڵندەی سوان، هەمیشە پێکەوە دەمێنینەوە."],
    ["💛", "خۆشمدەویت، ئەمڕۆ و هەمیشە."],
]

st.set_page_config(page_title="بۆ تۆ 💛", page_icon="💛", layout="centered")
st.markdown(
    "<style>header,footer,#MainMenu{visibility:hidden}"
    ".block-container{padding:0!important;max-width:100%!important}</style>",
    unsafe_allow_html=True,
)

PAGE = r"""<!DOCTYPE html>
<html lang="ckb" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>بۆ ئەو کەسەی دڵمی بردووە 💛</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg1:#ffe1ec;--bg2:#fff3bf;--pink:#ff6fa0;--deep:#c2185b;--sun:#ffc929;--text:#5a1633;--card:rgba(255,255,255,.62);
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
:root:not([data-theme="light"]){color-scheme:light dark}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg1:#3b0f26;--bg2:#4a3a0a;--pink:#ff8fb6;--deep:#ffb3cf;--sun:#ffd54a;--text:#fff0f5;--card:rgba(255,255,255,.1)}}
:root[data-theme="dark"]{--bg1:#3b0f26;--bg2:#4a3a0a;--pink:#ff8fb6;--deep:#ffb3cf;--sun:#ffd54a;--text:#fff0f5;--card:rgba(255,255,255,.1)}
html,body{height:100%;margin:0}
body{background:linear-gradient(160deg,var(--bg1) 0%,var(--bg1) 45%,var(--bg2) 100%);color:var(--text);
font-family:"Noto Naskh Arabic",Tahoma,serif;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.sun{position:absolute;top:-90px;left:-90px;width:300px;height:300px;border-radius:50%;
background:radial-gradient(circle,var(--sun) 0%,rgba(255,201,41,.35) 45%,transparent 70%);animation:glow 6s ease-in-out infinite}
@keyframes glow{50%{transform:scale(1.12);opacity:.85}}
.stage{position:relative;z-index:2;width:min(92vw,460px);text-align:center}
.card{background:var(--card);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:2px solid var(--sun);
border-radius:32px 32px 32px 8px;padding:44px 26px 34px;box-shadow:0 14px 40px rgba(194,24,91,.22);min-height:230px;
display:flex;flex-direction:column;align-items:center;justify-content:center}
.emoji{font-size:2.6rem;margin-bottom:14px;display:inline-block;animation:bob 2.4s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(-8px) scale(1.08)}}
#line{font-size:1.55rem;line-height:2;font-weight:600;margin:0;min-height:6em;display:flex;align-items:center}
.dots{display:flex;gap:8px;justify-content:center;margin:22px 0 18px}
.dots i{width:10px;height:10px;border-radius:50%;background:var(--pink);opacity:.3;transition:.3s}
.dots i.on{opacity:1;background:var(--sun);box-shadow:0 0 0 3px var(--pink);transform:scale(1.2)}
button{font:inherit;font-size:1.1rem;font-weight:700;background:linear-gradient(135deg,var(--pink),var(--deep));color:#fff;border:0;border-radius:999px;padding:13px 38px;cursor:pointer;box-shadow:0 8px 20px rgba(194,24,91,.35)}
button:active{transform:scale(.96)}
button:focus-visible{outline:3px solid var(--sun);outline-offset:3px}
.p{position:fixed;top:-40px;pointer-events:none;z-index:1;animation:fall linear forwards}
@keyframes fall{to{transform:translateY(115vh) rotate(360deg)}}
.swan{position:fixed;bottom:calc(10px + env(safe-area-inset-bottom,0px));font-size:3.2rem;z-index:1;pointer-events:none;animation:swim 20s linear infinite}
@keyframes swim{from{left:100vw}to{left:-80px}}
.lily{position:fixed;bottom:calc(4px + env(safe-area-inset-bottom,0px));z-index:1;pointer-events:none;animation:sway 3.5s ease-in-out infinite;transform-origin:50% 100%}
@keyframes sway{50%{transform:rotate(8deg)}}
@media (prefers-reduced-motion:reduce){.sun,.emoji,.swan,.lily{animation:none}.swan{left:10vw}.p{display:none}}
</style>
</head>
<body>
<div class="sun" aria-hidden="true"></div>
<div aria-hidden="true">
<span class="lily" style="left:4vw;font-size:2.4rem">🪷</span>
<span class="lily" style="left:22vw;font-size:1.8rem;animation-delay:-1s">🪷</span>
<span class="lily" style="left:48vw;font-size:2.2rem;animation-delay:-2s">🪷</span>
<span class="lily" style="left:72vw;font-size:1.9rem;animation-delay:-.5s">🪷</span>
<span class="lily" style="left:90vw;font-size:2.4rem;animation-delay:-1.5s">🪷</span>
<span class="swan">🦢</span>
</div>
<main class="stage">
  <div class="card">
    <span class="emoji" id="emoji">👀</span>
    <p id="line" aria-live="polite"></p>
  </div>
  <div class="dots" id="dots"></div>
  <button id="next">دەست پێ بکە</button>
</main>
<script>
var S=__MESSAGES__;
var i=-1,timer,line=document.getElementById("line"),em=document.getElementById("emoji"),
btn=document.getElementById("next"),dots=document.getElementById("dots");
S.forEach(function(){dots.appendChild(document.createElement("i"))});
function type(t){clearInterval(timer);line.textContent="";var n=0;
timer=setInterval(function(){line.textContent=t.slice(0,++n);if(n>=t.length)clearInterval(timer)},55)}
var icons=["💗","💛","🌸","🪷","🦢","✨"];
function petals(c){for(var k=0;k<c;k++){var s=document.createElement("span");s.className="p";
s.textContent=icons[Math.floor(Math.random()*icons.length)];s.style.left=Math.random()*100+"vw";
s.style.fontSize=(14+Math.random()*20)+"px";s.style.animationDuration=(5+Math.random()*4)+"s";
s.style.animationDelay=(Math.random()*1.5)+"s";document.body.appendChild(s);
setTimeout(function(e){e.remove()},11000,s)}}
function show(){var d=dots.children;for(var k=0;k<d.length;k++)d[k].className=k===i?"on":"";
em.textContent=S[i][0];type(S[i][1]);petals(i===S.length-1?30:8);
btn.textContent=i===S.length-1?"دووبارە 💞":"دواتر"}
btn.addEventListener("click",function(){i=(i+1)%S.length;show()});
</script>
</body>
</html>
"""

components.html(
    PAGE.replace("__MESSAGES__", json.dumps(MESSAGES, ensure_ascii=False)),
    height=760,
    scrolling=False,
)
