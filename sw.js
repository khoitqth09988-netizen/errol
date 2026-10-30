/* Service worker — "Sự thức giấc của Tiny" (GitHub Pages: /errol/).
   Mục tiêu: cài làm app trên mobile/PC + offline nhẹ.
   Chiến lược: navigation = network-first (luôn lấy bản mới, offline dùng cache);
   asset cùng origin = stale-while-revalidate; font bên ngoài để trình duyệt lo. */
const CACHE = 'tiny-garden-v1';

self.addEventListener('install', () => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
            .then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    const req = event.request;
    if (req.method !== 'GET') return;

    const url = new URL(req.url);
    if (url.origin !== self.location.origin) return;   // fonts/googleapis: network
    if (url.pathname.endsWith('/sw.js')) return;       // SW itself: network
    if (req.headers.has('range')) return;              // audio/video Seeking: network

    if (req.mode === 'navigate') {
        event.respondWith(
            fetch(req)
                .then((res) => {
                    const copy = res.clone();
                    caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
                    return res;
                })
                .catch(async () => {
                    const cached = await caches.match(req);
                    return cached || (await caches.match('index.html')) || Response.error();
                })
        );
        return;
    }

    event.respondWith(
        caches.open(CACHE).then(async (cache) => {
            const hit = await cache.match(req);
            const network = fetch(req)
                .then((res) => {
                    if (res && res.status === 200) cache.put(req, res.clone()).catch(() => {});
                    return res;
                })
                .catch(() => hit);
            return hit || network;
        })
    );
});
