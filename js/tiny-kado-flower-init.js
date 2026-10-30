// extracted from index.html <script id="tiny-kado-flower-init">

(()=>{
  const stage = document.getElementById('smile-stage');
  const frame = document.getElementById('kado-flower-frame');
  if (!stage || !frame) return;
  const flowerDoc = `<!DOCTYPE html><html lang=\"vi\"><head><meta charset=\"utf-8\"><style>\n*{margin:0;padding:0;box-sizing:border-box}\nhtml,body{width:100%;height:100%;overflow:hidden;background:transparent}\nbody{display:flex;align-items:flex-end;justify-content:center;perspective:650px}\n.flowers{position:relative;width:100%;height:100%;transform:scale(.90);transform-origin:bottom center;filter:hue-rotate(132deg) saturate(.91)}\n.flower{position:absolute;bottom:12%;left:46%;transform-origin:bottom center;z-index:5;--fl-speed:.75s}\n.flower--1{left:23%;animation:moving-flower-1 4s ease-in-out infinite alternate}\n.flower--2{left:50%;transform:rotate(18deg);animation:moving-flower-2 4.7s ease-in-out infinite alternate}\n.flower--3{left:72%;transform:rotate(-16deg);animation:moving-flower-3 4.2s ease-in-out infinite alternate}\n.flower__leafs{position:relative;animation:blooming-flower 1.8s backwards}\n.flower__leafs--1{animation-delay:.6s}.flower__leafs--2{animation-delay:.95s}.flower__leafs--3{animation-delay:1.25s}\n.flower__leafs::after{content:\"\";position:absolute;left:0;top:0;transform:translate(-50%,-100%);width:7vmin;height:7vmin;border-radius:50%;background:#6bf0ff;filter:blur(7vmin)}\n.flower__leaf{position:absolute;bottom:0;left:50%;width:8vmin;height:11vmin;border-radius:51% 49% 47% 53% / 44% 45% 55% 69%;background-image:linear-gradient(to top,#54b8aa,#a7ffee);transform-origin:bottom center;opacity:.9;box-shadow:inset 0 0 2vmin rgba(255,255,255,.5)}\n.flower__leaf--1{transform:translate(-10%,1%) rotateY(40deg) rotateX(-50deg)}\n.flower__leaf--2{transform:translate(-50%,-4%) rotateX(40deg)}\n.flower__leaf--3{transform:translate(-90%,0%) rotateY(45deg) rotateX(50deg)}\n.flower__leaf--4{height:8vmin;border-radius:4vmin 10vmin 4vmin 4vmin;transform-origin:bottom left;transform:translate(0,18%) rotateX(70deg) rotate(-43deg);background:linear-gradient(to top,#39c6d6,#a7ffee);z-index:1;opacity:.8}\n.flower__white-circle{position:absolute;left:-3.5vmin;top:-3vmin;width:9vmin;height:4vmin;border-radius:50%;background:#fff}\n.flower__white-circle::after{content:\"\";position:absolute;left:50%;top:45%;width:60%;height:60%;transform:translate(-50%,-50%);border-radius:50%;background:linear-gradient(90deg,#ffeb12,#ffce00)}\n.flower__line{height:54vmin;width:1.5vmin;background:linear-gradient(to left,rgba(0,0,0,.2),transparent,rgba(255,255,255,.2)),linear-gradient(to top,transparent 8%,#14757a,#39c6d6);box-shadow:inset 0 0 2px rgba(0,0,0,.5);animation:grow-flower-tree 2.8s backwards}\n.flower--1 .flower__line{height:65vmin;animation-delay:.35s}\n.flower--2 .flower__line{height:53vmin;animation-delay:.55s}\n.flower--3 .flower__line{height:58vmin;animation-delay:.75s}\n.flower__line__leaf{--w:7vmin;--h:calc(var(--w) + 2vmin);position:absolute;top:20%;left:90%;width:var(--w);height:var(--h);border-top-right-radius:var(--h);border-bottom-left-radius:var(--h);background:linear-gradient(to top,rgba(20,117,122,.4),#39c6d6)}\n.flower__line__leaf--1{transform:rotate(70deg) rotateY(30deg);animation:blooming-leaf-right var(--fl-speed) 1.6s backwards}\n.flower__line__leaf--2{top:45%;transform:rotate(70deg) rotateY(30deg);animation:blooming-leaf-right var(--fl-speed) 1.9s backwards}\n.flower__line__leaf--3,.flower__line__leaf--4,.flower__line__leaf--6{border-top-right-radius:0;border-bottom-left-radius:0;border-top-left-radius:var(--h);border-bottom-right-radius:var(--h);left:-460%;top:12%;transform:rotate(-70deg) rotateY(30deg);animation:blooming-leaf-left var(--fl-speed) 1.45s backwards}\n.flower__line__leaf--4{top:40%;animation-delay:1.85s}\n.flower__line__leaf--5{top:0;transform-origin:left;transform:rotate(70deg) rotateY(30deg) scale(.6);animation:blooming-leaf-right var(--fl-speed) 2.05s backwards}\n.flower__line__leaf--6{top:-2%;left:-450%;transform-origin:right;transform:rotate(-70deg) rotateY(30deg) scale(.6);animation-delay:2.2s}\n.flower__light{position:absolute;bottom:0;width:1vmin;height:1vmin;border-radius:50%;background:#fffb00;filter:blur(.2vmin);animation:light-ans 3.8s linear infinite backwards}\n.flower__light:nth-child(odd){background:#23f0ff}\n.flower__light--1{left:-2vmin;animation-delay:1s}.flower__light--2{left:3vmin;animation-delay:.5s}.flower__light--3{left:-6vmin;animation-delay:.3s}.flower__light--4{left:6vmin;animation-delay:.9s}.flower__light--5{left:-1vmin;animation-delay:1.5s}.flower__light--6{left:-4vmin;animation-delay:3s}.flower__light--7{left:3vmin;animation-delay:2s}.flower__light--8{left:-6vmin;animation-delay:3.5s}\n.kado-grass{position:absolute;bottom:8%;width:100%;height:18%;pointer-events:none;opacity:.52;background:repeating-linear-gradient(105deg,transparent 0 18px,rgba(82,219,198,.12) 19px 21px,transparent 22px 36px);mask-image:linear-gradient(0deg,black,transparent 90%)}\n@keyframes blooming-flower{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}\n@keyframes grow-flower-tree{from{height:0;opacity:.2}}\n@keyframes blooming-leaf-left{from{transform:rotate(-70deg) rotateY(30deg) scale(0)}}\n@keyframes blooming-leaf-right{from{transform:rotate(70deg) rotateY(30deg) scale(0)}}\n@keyframes moving-flower-1{from{transform:rotate(-3deg)}to{transform:rotate(3deg)}}\n@keyframes moving-flower-2{from{transform:rotate(13deg)}to{transform:rotate(22deg)}}\n@keyframes moving-flower-3{from{transform:rotate(-20deg)}to{transform:rotate(-11deg)}}\n@keyframes light-ans{0%,100%{opacity:0;transform:translateY(0) scale(.7)}35%{opacity:.9}75%{opacity:.35;transform:translateY(-13vmin) translateX(7vmin) scale(1.2)}}\n
/* --- INTERACTIVE FINALE STYLES --- */
.tiny-finale-panel {
  position: relative;
  z-index: 20;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: min(92vw, 490px);
  margin-top: clamp(8px, 2.5vh, 18px);
  animation: finaleFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  text-align: center;
  pointer-events: auto;
}
@keyframes finaleFadeUp {
  0% { opacity: 0; transform: translateY(28px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
.finale-status-badge {
  font-size: clamp(12px, 3.2vw, 15px);
  color: #a2eaff;
  letter-spacing: 0.08em;
  margin: 0 0 10px;
  text-shadow: 0 0 10px rgba(162, 234, 255, 0.6);
  font-weight: 600;
}
.finale-wish-card {
  width: 100%;
  background: rgba(18, 26, 48, 0.82);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 185, 222, 0.4);
  border-radius: 22px;
  padding: clamp(16px, 4vw, 24px) clamp(16px, 4.5vw, 26px);
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5), 0 0 25px rgba(255, 150, 205, 0.2);
  box-sizing: border-box;
}
.finale-wish-title {
  margin: 0 0 8px;
  font-size: clamp(15px, 4.2vw, 19px);
  font-weight: 700;
  color: #ffe6f3;
  text-shadow: 0 0 12px rgba(255, 182, 224, 0.65);
}
.finale-wish-desc {
  margin: 0 0 18px;
  font-size: clamp(12px, 3.4vw, 14px);
  line-height: 1.5;
  color: #d1eaff;
}
.finale-btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}
.finale-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  padding: 10px 20px;
  border-radius: 999px;
  font-size: clamp(13px, 3.5vw, 15px);
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  border: none;
  font-family: inherit;
  touch-action: manipulation;
}
.finale-btn:active {
  transform: scale(0.95);
}
.finale-btn-replay {
  background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
  color: #fff;
  box-shadow: 0 4px 15px rgba(255, 117, 140, 0.45);
}
.finale-btn-replay:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 117, 140, 0.65);
}
.finale-btn-share {
  background: rgba(30, 48, 85, 0.85);
  color: #cceeff;
  border: 1px solid rgba(162, 234, 255, 0.55);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
}
.finale-btn-share:hover {
  background: rgba(45, 72, 125, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(162, 234, 255, 0.4);
}
.finale-tap-hint {
  margin: 12px 0 0;
  font-size: clamp(11px, 3vw, 13px);
  color: #ffb8df;
  opacity: 0.85;
  animation: pulseHint 2s infinite ease-in-out;
}
@keyframes pulseHint {
  0%, 100% { opacity: 0.5; transform: scale(0.98); }
  50% { opacity: 1; transform: scale(1.02); }
}
.floating-heart-particle {
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  user-select: none;
  animation: floatHeartAnim 1.4s cubic-bezier(0.12, 0.8, 0.3, 1) forwards;
}
@keyframes floatHeartAnim {
  0% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(0.4) rotate(0deg);
  }
  60% {
    opacity: 0.95;
    transform: translate(calc(-50% + var(--dx, 0px)), calc(-50% - 70px)) scale(1.2) rotate(var(--rot, 0deg));
  }
  100% {
    opacity: 0;
    transform: translate(calc(-50% + var(--dx, 0px)), calc(-50% - 140px)) scale(1.4) rotate(calc(var(--rot, 0deg) * 1.5));
  }
}
#share-flight-scene.share-thank-you .share-tiny {
  animation: tinyBreathe 3s ease-in-out infinite;
}
@keyframes tinyBreathe {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-7px); }
}
/* --- END INTERACTIVE FINALE STYLES --- */
</style></head><body><div class=\"flowers\"><div class=\"flower flower--1\"><div class=\"flower__leafs flower__leafs--1\"><div class=\"flower__leaf flower__leaf--1\"></div><div class=\"flower__leaf flower__leaf--2\"></div><div class=\"flower__leaf flower__leaf--3\"></div><div class=\"flower__leaf flower__leaf--4\"></div><div class=\"flower__white-circle\"></div><div class=\"flower__light flower__light--1\"></div><div class=\"flower__light flower__light--2\"></div><div class=\"flower__light flower__light--3\"></div><div class=\"flower__light flower__light--4\"></div><div class=\"flower__light flower__light--5\"></div><div class=\"flower__light flower__light--6\"></div><div class=\"flower__light flower__light--7\"></div><div class=\"flower__light flower__light--8\"></div></div><div class=\"flower__line\"><div class=\"flower__line__leaf flower__line__leaf--1\"></div><div class=\"flower__line__leaf flower__line__leaf--2\"></div><div class=\"flower__line__leaf flower__line__leaf--3\"></div><div class=\"flower__line__leaf flower__line__leaf--4\"></div><div class=\"flower__line__leaf flower__line__leaf--5\"></div><div class=\"flower__line__leaf flower__line__leaf--6\"></div></div></div><div class=\"flower flower--2\"><div class=\"flower__leafs flower__leafs--2\"><div class=\"flower__leaf flower__leaf--1\"></div><div class=\"flower__leaf flower__leaf--2\"></div><div class=\"flower__leaf flower__leaf--3\"></div><div class=\"flower__leaf flower__leaf--4\"></div><div class=\"flower__white-circle\"></div><div class=\"flower__light flower__light--1\"></div><div class=\"flower__light flower__light--2\"></div><div class=\"flower__light flower__light--3\"></div><div class=\"flower__light flower__light--4\"></div><div class=\"flower__light flower__light--5\"></div><div class=\"flower__light flower__light--6\"></div><div class=\"flower__light flower__light--7\"></div><div class=\"flower__light flower__light--8\"></div></div><div class=\"flower__line\"><div class=\"flower__line__leaf flower__line__leaf--1\"></div><div class=\"flower__line__leaf flower__line__leaf--2\"></div><div class=\"flower__line__leaf flower__line__leaf--3\"></div><div class=\"flower__line__leaf flower__line__leaf--4\"></div></div></div><div class=\"flower flower--3\"><div class=\"flower__leafs flower__leafs--3\"><div class=\"flower__leaf flower__leaf--1\"></div><div class=\"flower__leaf flower__leaf--2\"></div><div class=\"flower__leaf flower__leaf--3\"></div><div class=\"flower__leaf flower__leaf--4\"></div><div class=\"flower__white-circle\"></div><div class=\"flower__light flower__light--1\"></div><div class=\"flower__light flower__light--2\"></div><div class=\"flower__light flower__light--3\"></div><div class=\"flower__light flower__light--4\"></div><div class=\"flower__light flower__light--5\"></div><div class=\"flower__light flower__light--6\"></div><div class=\"flower__light flower__light--7\"></div><div class=\"flower__light flower__light--8\"></div></div><div class=\"flower__line\"><div class=\"flower__line__leaf flower__line__leaf--1\"></div><div class=\"flower__line__leaf flower__line__leaf--2\"></div><div class=\"flower__line__leaf flower__line__leaf--3\"></div><div class=\"flower__line__leaf flower__line__leaf--4\"></div></div></div><div class=\"kado-grass\"></div></div></body></html>`;
  let ready=false;
  const start=()=>{
    if(ready || !stage.classList.contains('hien-thi') || !matchMedia("(min-width:701px) and (pointer:fine)").matches) return;
    ready=true;
    frame.srcdoc=flowerDoc;
  };
  new MutationObserver(start).observe(stage,{attributes:true,attributeFilter:['class']});
  start();
})();
