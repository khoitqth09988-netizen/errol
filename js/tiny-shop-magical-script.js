// extracted from index.html <script id="tiny-shop-magical-script">

(()=>{
 return; // disabled
 const field=document.getElementById('shop-magical-field');
 if(!field)return;
 let seed=20261020;
 const rand=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};
 const palette=['#b3faff','#ffb8dd','#fff2b7','#c5ceff'];
 const fragment=document.createDocumentFragment();
 // Ambient fireflies and petals, fewer on small viewports, no animation on reduced motion.
 const small=window.matchMedia('(max-width: 700px)').matches;
 const fireCount=TINY_PERF.mobile?8:small?10:23,petalCount=TINY_PERF.mobile?2:small?3:6;
 for(let i=0;i<fireCount+petalCount;i++){
  const petal=i>=fireCount,el=document.createElement('span');
  el.className=petal?'shop-magical-petal':'shop-magical-firefly';
  el.setAttribute('aria-hidden','true');
  const x=petal?(rand()<.5?rand()*15:85+rand()*15):rand()*100;
  const y=20+rand()*73;
  el.style.setProperty('--fx',x.toFixed(2)+'%');
  el.style.setProperty('--fy',y.toFixed(2)+'%');
  el.style.setProperty('--fs',petal?(12+rand()*11).toFixed(1)+'px':(1.8+rand()*2.8).toFixed(1)+'px');
  el.style.setProperty('--fc',palette[Math.floor(rand()*palette.length)]);
  el.style.setProperty('--ft',(petal?6+rand()*5:2.5+rand()*4.5).toFixed(2)+'s');
  el.style.setProperty('--fd',(-rand()*8).toFixed(2)+'s');
  if(petal)el.textContent=['✿','✧','❀'][Math.floor(rand()*3)];
  fragment.appendChild(el);
 }
 field.appendChild(fragment);
})();
