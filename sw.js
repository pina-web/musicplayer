const CACHE="haru-music-audiofix-v2";
const STATIC=["./manifest.json","./icon-192.png","./icon-512.png","./audio/test.wav"];
self.addEventListener("install",e=>{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(c=>c.addAll(STATIC)))});
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{
 const u=new URL(e.request.url);
 if(e.request.mode==="navigate"||u.pathname.endsWith("/index.html")||u.pathname.endsWith("/musicplayer/")){
   e.respondWith(fetch(e.request,{cache:"no-store"}).catch(()=>caches.match("./index.html"))); return;
 }
 e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));
});