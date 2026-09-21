<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/MguCARJz5nA0tulXDb1v8LL8mZQQlAVmP8BsMj7bzRxEA6jb0WX7tZi6UKhbi0knTP8Gxs2y9ECL3TRLkRY51_XUK74o3hklWLQklETYRVp6q-_haSotprBnZkFPfN6T2w3sI7lR4QPf467QjSm_0zVIdGLaMEyc45p0yTIti8iQbFtXlcU_OnjeQwAy7Odos2Ez-wVWanZFAP-GJTNR9q-T72uSbVjYgQ2-rTbvochL4b7hM3S3IAgBwKyuGd-TkJQM9P7woc49i9aHU_cREJEFIE6ZW4qErglOZe6ynsxAE8_1AyT1z7EHFRynqzlG6F3mdMG9AsMB7555DGFOWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-72005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید حساب کاخ سفید در پلتفرم ایکس:
چیزی در راه است. منتظر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/news_hut/72005" target="_blank">📅 20:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای حداقل ۲۵ تانکر نیروی هوایی ایالات متحده را در پایگاه هوایی العدید در قطر نشان می‌دهد که بزرگترین حضور تانکرها در آنجا از زمان آغاز جنگ ایران در فوریه است.
این تانکرها در ابتدا به دلیل تهدید حملات موشکی ایران از آنجا خارج شدند و حدود ماه ژوئن شروع به بازگشت کردند.
برخلاف پارکینگ تانکرهای بسیار متراکم مشاهده شده در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، به دلیل اقدامات احتیاطی مداوم علیه حملات ایران، هواپیماها همچنان به طور گسترده در سراسر محوطه پایگاه پراکنده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/news_hut/72003" target="_blank">📅 20:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مربی بدن‌سازی:
خیلی از جوونا هستن باشگاه ثبت نام میکنن ولی تو تایم باشگاه، میرن پارک با دوستاشون مواد میکشن
وقتی هم که خانوادشون بهشون میگه چرا لاغر شدی و قیافت اینجوری شده بهشون میگن رژیم گرفتیم و طبیعیه
@News_Hut</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/news_hut/72002" target="_blank">📅 19:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
ما کاملاً واقفیم که قیمت انرژی به دلیل اقدامات تروریستی ایران علیه کشتیرانی بین‌المللی، افزایش یافته است.
ما تمام تلاش خود را به کار می‌گیریم تا ضمن مهار این قیمت‌ها، در این فاصله باری از دوش مردم آمریکا برداریم.
یکی از اقداماتی که ترامپ درباره آن صحبت کرده، تشویق برخی ایالت‌ها به کاهش یا حذف مالیات بنزین برای مردم آمریکا است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/72001" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
با وجود اینکه ایرانی‌ها هر روز برای کشتی‌ها ایجاد وحشت می‌کنند، ما همچنان شاهد جریان حجم قابل‌توجهی از نفت و گاز از طریق تنگه هرمز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/72000" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97u8l4PoawtrMoe0373WyQuIA7JUPuzcATZE5c1I3TJR3Fd_HigLXcCwcMzmVMwzRT23xaj3DuqA7o9hris2rjY7LUss-AAWCs4XB1CoTYHyuOrFTKKRhw3PKP8VSrk6NwxTlno9X4m6u9h3zm7RMHKloBDJPrxvKmtDT2J4eEptL9XaC2TsHdv7IRykKswMEzhiLdOQJBklu15_HcvW5fZM8PQ2aCEHUN_bWpG-VIwnDS-DIpZi-URnPhrwMHbKX0MerMaojk-FmWq8ukKjgReedWDoNwwAn4bTao9z0rVce8WxclGUZwCQ3kKY89u9SBGMJYj-SqnLAMvbvU5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71999" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران ویدیویی منتشر کرد که مدعی است لحظه رهگیری و انهدام یک پهپاد MQ-1 ارتش آمریکا در صبح امروز را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/news_hut/71998" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/71997" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxFINv-sJH4G46uAr_7JPIAvWFSrzOFVKdW-51T6WWV6KPjlyKlbD5vIBvVTP01cknDyfpR9p0tWOTwPQwKn4EaKaWVYARseETfyBePp99u_40zCh57AOE9u8Ip6_x8qArhATG9suzlPyPPSwzutubngKIWg1s7j0ffaYZEiu1jp0Dl18rG559Onj3BMrw5RNvw1evqBtnV7cPMvT1ELzqS_jkgj7HeLxo3q2AH0Ym1KEfEQ_4-2WKRhtSfNzM6SojZJCwVxwkQ64QyqxsUTtygkFHbry4QL8KY9tL9AKEAqhd8cdXvGY_icmXqjeM9WZNy-5Gm9lJownXNXLDtfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/news_hut/71996" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک: این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد
ایلان ماسک با انتشار ویدیویی آینده‌نگرانه از تعامل انسان و ربات، فناوری‌های پیشرفته و سفرهای فضایی، چشم‌انداز خود از آینده را به تصویر کشید و نوشت: «این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71995" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71994" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت درباره ایران:
در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.
چگونه این کار را انجام می‌دهیم؟
اگر آن‌ها فرود بیایند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛
وگرنه از سیستم دلاری کنار گذاشته خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71993" target="_blank">📅 16:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#مهم
؛اسکات بسنت وزیر خزانه‌داری آمریکا در گفتگو با CNBC: فعالیت ایرلاین‌های ایران از ۲۳ سپتامبر(اول مهر) با محدودیت های جدی مواجه خواهد شد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه ۲۱ سپتامبر اعلام کرد ایالات متحده از ۲۳ سپتامبر (اول مهر) با اعمال تحریم‌های ثانویه علیه ارائه‌دهندگان خدمات هوانوردی، در پی متوقف کردن فعالیت بین‌المللی ایرلاین‌های ایرانی است.
بسنت گفت شرکت‌هایی که به هواپیماهای ایرلاین‌های ایرانی سوخت‌رسانی کنند، خدمات فرودگاهی ارائه دهند یا برای آنها بلیت بفروشند، ممکن است با خطر قطع دسترسی به نظام مالی و دلاری آمریکا مواجه شوند.
این اظهارات پس از آن مطرح شد که وزارت خزانه‌داری آمریکا در ۸ سپتامبر، ۳۶ فرد و نهاد مرتبط با بخش هوانوردی ایران، از جمله ۲۷ ایرلاین ایرانی، را تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71992" target="_blank">📅 16:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده نسل جدید J-36 چین به پروازهای آزمایشی خود در طول روز ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71990" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرکی به نام صدا و سیمای جبلی!
با تراکتور اومده وسط برنامه؛ میگه میخوام باهاش اسرائیل رو شخم بزنم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71989" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL6RjJp5Jz7lEOqz_kEwHYwKMEfYJJIVzukqLw6tXcNsU-qD2aDUvJBF1eAYtLLcmHwr8VXBqgq-xJ_kYhGH5-ZpaG2VYmJIb_VBrGcFkQybUHkqtfjUL9UyC1w6oq16ku6u4_4ndLLede818JBoGzpMPJTI43VpyW7TYp0JifpiAlPySy8-lqajP1dEx_OcbSa92vXBEGKMtB7-wkCMBVihq9LKzvri4KLLUNZjnbDMBN4wuewGwbulKlvD7cBm6SfEe73Qw84QH_wu7R670hLhAnlRhTUPQmbzmMTOtqkqFQnkELyakJToikEVaixySA7UHZUlvy96OKeAFievgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود؛
سخنگوی کمیسیون انرژی مجلس:
این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71988" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=LLWM4EJvS-F09yiZr7byDMpoyEGBljPJE2ijJyfjjq98TLyiRN8f7r8SHNI_Mwug9bFt5l4tPciBepJkbPJSsiqknmND0qj7jgTEmR96gDuz-toT_6UPvz5a0pvrAkNwF47bLmhe_GkwIYv94pnk1t0rG3_iF90tVIO7YzeavnY7u1qMcatBQdj2XKRf26MeOrHBGhprsaOxVhRQ1xSQNUdGvwPPfHMFiXnAvjm9U57P03K-DZz35aNJKW5rQCre_odxQ2uH5yCNYw9jUwwrVUtzGeQcFAWwRvWOa9X5gda-djhYRsc4wEFwD8OipBjjbhgf1bZhXOxMoLZssW-8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=LLWM4EJvS-F09yiZr7byDMpoyEGBljPJE2ijJyfjjq98TLyiRN8f7r8SHNI_Mwug9bFt5l4tPciBepJkbPJSsiqknmND0qj7jgTEmR96gDuz-toT_6UPvz5a0pvrAkNwF47bLmhe_GkwIYv94pnk1t0rG3_iF90tVIO7YzeavnY7u1qMcatBQdj2XKRf26MeOrHBGhprsaOxVhRQ1xSQNUdGvwPPfHMFiXnAvjm9U57P03K-DZz35aNJKW5rQCre_odxQ2uH5yCNYw9jUwwrVUtzGeQcFAWwRvWOa9X5gda-djhYRsc4wEFwD8OipBjjbhgf1bZhXOxMoLZssW-8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان در جریان یک پرواز چهار ساعته بر فراز ایالت های اوکلاهما و آرکانزاس آمریکا، مسیر هواپیمای خود را به شکل چهره مونالیزا ترسیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71987" target="_blank">📅 15:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8tz0nuoaLq1ujUMYa3CB1eDfoBA54tQZr7QmDd_gs7YDgiyRnpH8S3VyJcJEIgPTAd_UIstlpXKPuSZ0_iFMrmfjvboEyG2ZnkrA8U5NchzWrcXcO7DIYuFbm-pQaydAZtOiBTgNfmkNC39BmKUkBnhtquz_6beJFExrkOAX5Pe-ndV1edJc_T4rqGtCL26pqT1U6Zehcgpzh4SLG3VhmBUKvP3W0dMSzUkm776-kuxX1R8yeY29omIuM93wARb8e92TR0Kq5XJ9BXF3vmS5qYkpoQIUu1xJhP4_hURemKdlrp7aERVTFzeyL6u6KALKSfT7i1itfGgKsb3Yju12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولیتیکو، سی‌ان‌ان، ام‌اس ناو و پولیتیکو پس از لغو دسترسی مطبوعاتی‌شان توسط کاخ سفید، از دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدام نقض متمم اول قانون اساسی است.
این رسانه‌ها می‌گویند که به دلیل گزارش‌هایشان هدف قرار گرفته‌اند، در حالی که رئیس جمهور ترامپ از این ممنوعیت دفاع کرد و گفت که ملزم به پذیرش رسانه‌هایی که «داستان‌های منفی» منتشر می‌کنند، در کاخ سفید نیست.
انتظار می‌رود درخواست اضطراری از یک قاضی فدرال در واشنگتن دی سی ارائه شود که احتمالاً منجر به جلسات استماع و استدلال‌هایی از سوی دولت در این هفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71986" target="_blank">📅 14:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر قطر:
از زمان جام جهانی، دیگر روی آرامش را ندیده‌ام.
پس از آن، ماجرای هفتم اکتبر پیش آمد و از آن زمان تاکنون، هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد.
از همه خواهش می‌کنم؛ ما برای سال ۲۰۲۷ به سالی سرشار از صلح و آرامش نیاز داریم.
لطفاً، ما به کمی استراحت نیاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71985" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLpfnTfuOCeoJSJIHF9SLAmmAV0muFeQXyVTTeSRFl43xrUIoWwJCej-JD_2X8veNREQVdMY3tLrdy9tfNMrS3TJngjKKnihWQXAMqXWliLbB632sfuklyQuxLPLNrX7z6abOzsoSJUUirBQAlBSwI-zr9nq5tzHprlWp-L0G7POjASGLTZpnw3Fw0ywmpUjGNq-ouuywno8jyEs3_UC1DLP--XrCUoYzw6XOgS2oFqDxiNnTgBwT_TPZI1jZYwyQfPkoLw_N6y9BxuYxjuNzdp2FNDvtNvBs7kap3Rc1MzXhUQH2o4Bug8LV73kjVdB1eJqPU5Oq8hJMSVcT-zS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
در هشدار شماره ۲۶-۱۴۰ که ساعت ۰۷:۳۰ به وقت هماهنگ جهانی (UTC) صادر شد، گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است. دو تن از خدمه دچار جراحات سطحی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71984" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران دردسرساز است؟
نخست‌وزیر قطر: کاملاً آشکار است که آن‌ها صلح‌جو نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71983" target="_blank">📅 12:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان هم به این شکل زنگ آغاز سال تحصیلی جدید رو به صدا درآورد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71982" target="_blank">📅 12:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71981" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd1F5t8XYfcHu2ffZ-CpBV7bD53gNkxB1tA69-HZJfhEA21dLZhC7fKbgTEKNywyLeR6gHYutmBS0R6_rDTX62Lq2I1n2X2fHULoG4IVPC-yZzxg30FX2AqoqBUAL153ls43X1gjR4VTfcXdfCewaCRbYrrpgf8FKhkbH4_llqV6Mtq06pni7BxKX6Wa80TG1IsQvqTlEKm2ierjd0GNlP2BKHMZcwHciCCU9aOEr1cMQRp8rsA2iBH0dzcYS88vNTJEgE-RdbgVZBbqv8eITEiiWGA3rGGALV1E48qcRNfL-3-jEFWhHuWg3wGH1FVMiflanywP0S3igGnfZKQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71980" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی، یه دختر نصف شب، این شکلی دختر خالشو سورپرایز کرد:
یه دسته گل بزرگ+ آیفون ۱۸ پرومکس+ کلی شکلات!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71979" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=dtTLPILKUoJZ_vgJ4rLpkFxGjT0Vi73oy08gc5u6-TG8nNolFu9mwKSJwuvu8zn6Dur9lb1i5qmTAQqIBJEIPdGFCumeeUDzUSfcx2HhtC9ZbsshU6qe6nb4bDTAp4G6ijzVYboR2Ppm6n6k_4zXVK0dUImMReUHo7HBu5B3n43-kyr-45AJOwKXIdUcD0r5nnUyScANzNs-XsLK3u6e3x0sTOFtVH8-MnRydAcjizIR56DgxKBOGWh3VUDyW_HrrziVGzTJNoR3X5R1FtfhYE7KAlbux5l8wqHdEm_MBtuGPQDfB2eOVwh_w0bqyNYuqSjWGxYezLzr8lUfTsCn9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=dtTLPILKUoJZ_vgJ4rLpkFxGjT0Vi73oy08gc5u6-TG8nNolFu9mwKSJwuvu8zn6Dur9lb1i5qmTAQqIBJEIPdGFCumeeUDzUSfcx2HhtC9ZbsshU6qe6nb4bDTAp4G6ijzVYboR2Ppm6n6k_4zXVK0dUImMReUHo7HBu5B3n43-kyr-45AJOwKXIdUcD0r5nnUyScANzNs-XsLK3u6e3x0sTOFtVH8-MnRydAcjizIR56DgxKBOGWh3VUDyW_HrrziVGzTJNoR3X5R1FtfhYE7KAlbux5l8wqHdEm_MBtuGPQDfB2eOVwh_w0bqyNYuqSjWGxYezLzr8lUfTsCn9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از دو دختر جانفدا به اسم پرنسس های جنگجو؛
میگه همه با دوست پسراشون میان رزمایش من با دوست دخترم
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71978" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محبی، سخنگوی سپاه پاسداران:
در صورت وقوع حمله‌ای دیگر از سوی آمریکا، ایران واکنش نظامی خود را — از جمله «جغرافیای جنگ» و تسلیحات مورد استفاده — به‌طور قابل‌توجهی تغییر خواهد داد.
«ما تسلیحات جدیدی با قابلیت‌های تازه به میدان نبرد خواهیم آورد و جهانیان شگفت‌زده خواهند شد.»
محبی افزود که ایران همچنین «اهداف جدیدی» در اختیار دارد که تاکنون مورد حمله قرار نگرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71977" target="_blank">📅 10:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات پهپادی روسیه به زاپوریژیا به یک مرکز خرید و قدیمی‌ترین ساختمان دانشگاه ملی زاپوریژیا آسیب رساند.
در حملاتی جداگانه در منطقه اودسا، انبارهای مواد غذایی که گفته می‌شود متعلق به فروشگاه‌های زنجیره‌ای «سیلپو» (Silpo) هستند، هدف قرار گرفتند.
در استان کی‌یف، این حملات به ۳۴ نقطه در پنج منطقه، از جمله خانه‌ها، انبارها و زیرساخت‌ها، خسارت وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71975" target="_blank">📅 10:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=BDJQNN6L6XBWlHtvgyHsXUArCSlC3Md_D3B7UsLxKqRWn9f8nxexTx8ww9AUDYhoP_XSI6a5y_QXY4299LKw2Mb5rHyB7cuTtoZRaW-go3upHmoAJ4VszOKYaFpmh9pG19h-YUnqkH31nKgu2qgoEcjJB_mSbiBLz0fb8YLle6V0h5pTrKfntj_ZaHMlqV6thmNfXZILKz1mKaOGUgxsW-RuVI1vjrCU9tNLv2NwOoTT8YIpLU81FMGM29hzx9trB1tDcJ4MtAajzfNjGiE5ZfITmgmsZ0nQScj912geQ7Pg-EuYJjZGrtZokaQ4yoQUydStbTkf1TfdsNE708bh4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=BDJQNN6L6XBWlHtvgyHsXUArCSlC3Md_D3B7UsLxKqRWn9f8nxexTx8ww9AUDYhoP_XSI6a5y_QXY4299LKw2Mb5rHyB7cuTtoZRaW-go3upHmoAJ4VszOKYaFpmh9pG19h-YUnqkH31nKgu2qgoEcjJB_mSbiBLz0fb8YLle6V0h5pTrKfntj_ZaHMlqV6thmNfXZILKz1mKaOGUgxsW-RuVI1vjrCU9tNLv2NwOoTT8YIpLU81FMGM29hzx9trB1tDcJ4MtAajzfNjGiE5ZfITmgmsZ0nQScj912geQ7Pg-EuYJjZGrtZokaQ4yoQUydStbTkf1TfdsNE708bh4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مونا محبی، تراپیست :
«یه بیمار داشتم که سه تا پسر داشت؛ فقط پسر اول بچه شوهرش بود. پسر دوم بچه عموی شوهرش و پسر سوم هم بچه شوهرعمه شوهرش بود!
حالا بچه دوم یه مشکل خونی پیدا کرده و برای تشخیص باید
آزمایش ژنتیک
بده؛ آزمایشی که ممکنه مشخص کنه بچه، بچه شوهرش نیست و این راز بعد از سال‌ها لو بره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71974" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=bPB9k5xpfgF6m8fGTVtntwHyWV54TK16_3bvPwi5M0N4RNh2RNhVvKncqB29v9yjzBFaEQ4lRuYpCinAy7zJqOEdTjmYDSxWK3KVvkJAUhxyuxf2UyX6Yiozr07Q6bnzKAmT5SkKym_xOVaIShJwuI7_dNBtmhy0HLHjAdVxzy7XmDgqOGWdmZ1E8qQvEH2zZTS1UPkUsnqVzeDO8O8XyuQQzcdhEPYJD05Tnqb63-1moRMBCLEECTJiPRipuA9a6I5Goc_QBToi9lqo0kVqiqi31ryEE38KA13KaYMG1FmFzKTMlAGE6FgCD8YzJ50jmDpL07SGTIu3XIEV99_N3aCdpuT5551trwokzlGIQGP2Z4iIpYr5FmiLr0UWWZqEy59a1vAdkANf1KcEESXfO30kZrzeo-eOVTacLrVhpvEzPAdNHTZTpc_AQDt4FdPutr18MhvqrBpX9N00IlZsX3kSV3sF3tvssTyEbOJahL_215CncFjeOJt3g1uOlVb8kEtEQeipfUetEBNQdOQXie2GaF2EkVMLApoTBSxDmxT1fPx3g7XsxLjeBQysPXbPbI-abq2v1sX_HmDn4nc-9co1JUwTJT8ZSvbgDcZgidbCReZtWeTPSl80F4GOUMQrUslDOwfZ_lfXzZGXffokmCvXLFHv9AxiGXCLmbNPNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=bPB9k5xpfgF6m8fGTVtntwHyWV54TK16_3bvPwi5M0N4RNh2RNhVvKncqB29v9yjzBFaEQ4lRuYpCinAy7zJqOEdTjmYDSxWK3KVvkJAUhxyuxf2UyX6Yiozr07Q6bnzKAmT5SkKym_xOVaIShJwuI7_dNBtmhy0HLHjAdVxzy7XmDgqOGWdmZ1E8qQvEH2zZTS1UPkUsnqVzeDO8O8XyuQQzcdhEPYJD05Tnqb63-1moRMBCLEECTJiPRipuA9a6I5Goc_QBToi9lqo0kVqiqi31ryEE38KA13KaYMG1FmFzKTMlAGE6FgCD8YzJ50jmDpL07SGTIu3XIEV99_N3aCdpuT5551trwokzlGIQGP2Z4iIpYr5FmiLr0UWWZqEy59a1vAdkANf1KcEESXfO30kZrzeo-eOVTacLrVhpvEzPAdNHTZTpc_AQDt4FdPutr18MhvqrBpX9N00IlZsX3kSV3sF3tvssTyEbOJahL_215CncFjeOJt3g1uOlVb8kEtEQeipfUetEBNQdOQXie2GaF2EkVMLApoTBSxDmxT1fPx3g7XsxLjeBQysPXbPbI-abq2v1sX_HmDn4nc-9co1JUwTJT8ZSvbgDcZgidbCReZtWeTPSl80F4GOUMQrUslDOwfZ_lfXzZGXffokmCvXLFHv9AxiGXCLmbNPNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پاراگلایدر سوار لحظاتی را که در حین فرود به سرعتی بیش از ۱۲۵ کیلومتر در ساعت می‌رسید، ثبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71973" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=RCsTkQQyD-_zUFRuiMhZg0CUFGByeOuUWKC6XUwp8j9Q-XgiLYlK8tsGWYH9e_WA1ki32aIvFTMsF78S1cjzNn82XQUfbEaO5XLiocgsWh-xQRf0WVS77Sim9jG44NJwrDP7DaiPkfUcpaP5g24RtLBenETlpT1aAf020lNbwnkYzLPhejnXD6LYK3oqUJvq9bzYrtvDZf56-ERq-0B41iTAQbPgYTgAu5uc2bSsZis9Krgj_o0iIiuR7i_naTQpa8TtjXOtOuwAxdcb6bNGZy9VFXZ70BTu8L1VrN_WUgL7iZ8lQpcSUPbGhl2MGm52kdn-laG4hTCfYj5yafzecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=RCsTkQQyD-_zUFRuiMhZg0CUFGByeOuUWKC6XUwp8j9Q-XgiLYlK8tsGWYH9e_WA1ki32aIvFTMsF78S1cjzNn82XQUfbEaO5XLiocgsWh-xQRf0WVS77Sim9jG44NJwrDP7DaiPkfUcpaP5g24RtLBenETlpT1aAf020lNbwnkYzLPhejnXD6LYK3oqUJvq9bzYrtvDZf56-ERq-0B41iTAQbPgYTgAu5uc2bSsZis9Krgj_o0iIiuR7i_naTQpa8TtjXOtOuwAxdcb6bNGZy9VFXZ70BTu8L1VrN_WUgL7iZ8lQpcSUPbGhl2MGm52kdn-laG4hTCfYj5yafzecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شجاعی، از روحانیون حامی جمهوری اسلامی:
امام‌زمان برای ظهور به لشکر نیاز دارد
۵۰ روستا در لبنان را که سال گذشته بازسازی کرده بودیم، از بین رفتند
دیشب طرح آبرسانی به مردم غزه را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71972" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPSNVfUFiI5ikZzYTYW-uYPjn3dc_owb6GcUV3zZSrBewglCBiQU38jnpASBDGkynIfuJGkLKDA8ngx2J0WIasruLAyvvuhStNUcPPD2IQSx6cpzWi19nkUoaxHbiFr1uBz8NlkRzj_ioqVgkYTDfYG46rsp11MZe98jCENwrLSLfM9qm03JFyUY5VsJrs7kPCdm1gTEXW_dHPbw29YLyd8b55oUOJv1Y5gIoS-maJEByIRY_-8pc5jkxhaac3TAhTtKay35Ps2p0ql4fdDjlTMKhTt7-7vQWJ5QzoRJGmW36IeWl1APoVtXxidi7UR5wtXqGnwk76VgusxlGHnxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=Hk-rEsPT1txxKuf9lMjKn1ASyfGxqGF2_GBVkrffktacC-hW7x3h3QUsAGcePE1qE-RumTQSuErmc7nJSbeCZWkzIs45SWuAzHpZwVtemoYKFE1UMNQSVLbDqAiAnSL9MPYazJFDpnPWd8syrlTr8k1sFJCKzfMYUqPAEB08gV6jI2iAm9gILNgTboOsHIPJWcR0GoVIJ9WGSqAvir5Vu_4fNr-kSV9AxtNZFGT8Em9Kvp1dPMiQxLnpUXoZ7eB1UtolZ9-D47gxB54vPAiIhrLDfc0KvSegZ1mqBdmF44mTtRF3aOEO3BpC21UOpAV5LnI-N_WzVOVLoz3h1oKlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=Hk-rEsPT1txxKuf9lMjKn1ASyfGxqGF2_GBVkrffktacC-hW7x3h3QUsAGcePE1qE-RumTQSuErmc7nJSbeCZWkzIs45SWuAzHpZwVtemoYKFE1UMNQSVLbDqAiAnSL9MPYazJFDpnPWd8syrlTr8k1sFJCKzfMYUqPAEB08gV6jI2iAm9gILNgTboOsHIPJWcR0GoVIJ9WGSqAvir5Vu_4fNr-kSV9AxtNZFGT8Em9Kvp1dPMiQxLnpUXoZ7eB1UtolZ9-D47gxB54vPAiIhrLDfc0KvSegZ1mqBdmF44mTtRF3aOEO3BpC21UOpAV5LnI-N_WzVOVLoz3h1oKlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ساعت قبل شخصی این ویدیو رو با این توضیحات منتشر کرده؛صحت ویدیو تایید یا تکذیب نمیشه:
تهران ، اتوبان آزادگان
29 شهریور
از اجرام ناشناخته آسمانی فیلم گرفتم
واقعا نمیدونم چی هست ولی نزدیک ابرها بود نور های خاصی داشت و بدون هیچ صدایی در فضا معلق بود !!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71969" target="_blank">📅 06:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71968" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71967" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=s_TCrgOJs0hG4uKgJxe5poYAcDeuL-5cp3Bvj0m_6b7WBdST_NXVaWCqS1ob_4ZBpAtG92Z2zJ9mAJXO4829wWYwLOB74hhAK73p127U_xNIz902BNoAkihS09ArrJWRhMhDgmvS16QN-52QOt_8UlCrblWEUfT8mJVDzA0x7DYeIpAas56BD4fEG3syP_o08PK-nAR1H9-McRulAKiG9ZQqIBd319d-WFlAOjODZRsAd4uG3LC2fQGW_PzsE26n2i2v5v03lBJsUccSMXUUyROaszd29abz4bK20HlW9SjTyVHRmvtmxbh64EH7wGXTZJAPHiR5WENhSoc8GY-S9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=s_TCrgOJs0hG4uKgJxe5poYAcDeuL-5cp3Bvj0m_6b7WBdST_NXVaWCqS1ob_4ZBpAtG92Z2zJ9mAJXO4829wWYwLOB74hhAK73p127U_xNIz902BNoAkihS09ArrJWRhMhDgmvS16QN-52QOt_8UlCrblWEUfT8mJVDzA0x7DYeIpAas56BD4fEG3syP_o08PK-nAR1H9-McRulAKiG9ZQqIBd319d-WFlAOjODZRsAd4uG3LC2fQGW_PzsE26n2i2v5v03lBJsUccSMXUUyROaszd29abz4bK20HlW9SjTyVHRmvtmxbh64EH7wGXTZJAPHiR5WENhSoc8GY-S9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها:
آری، امروز ما حرمین شریفین را هدف قرار خواهیم داد؛ آن‌ها را هدف می‌گیریم تا از وجود آل سعود پاک‌شان کنیم.
ما این حرمین شریفین را هدف قرار می‌دهیم تا به چراغ راهی برای مسلمانان آزاده بدل شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71966" target="_blank">📅 00:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jg7YJXVRcG9gBXG597rTNOnbkYL6Alk2K9-ctjWvgVxMhhJ1AzDXfILYrHT1-F0YrFn9U60E63O4_TEC8k86MLrwz1jHizDXfrHN-Qjw4tvq6cLkjC-U3HLza6w1Q5UvpYwOAkqEtBK3egOXN_xuD939Ye9STTzaNkpn-8jXmkOcpCD-_qJjf7KzsWcept5Jc1nvK5Gb8XXvpQH_tWSqs1-5gIsstfTBJ32n9Rt5BM5sJdab_dAdSg70fWQuys6sfzLJsgHDodpIVCTgFzDnpJfZhz3OFdubpx_rqRarrj_7ObxBugPYzhBFld_-vs78yuCJq53w2zCXRb9suvVr2nEpsDFacbsgMlnXTbhOL5fIJckXhzz6nyorL2uabqbGVGujgMFagTHNh2Lc-iFVTtMYF6FoAy30LwW3s8Wxb0So1tR4OKnu53V5aizHoSSntYa_bid1SgrNjZFnVgbaAw_SzF3whQfx5n9vIjWZglAgbmJ41THgYjml9GSuzV5l1-NV8LamIYkDen5Rx2_1W7seNcsRF2GITREHMxl0azofAA9W1qfGzU1N3QNxkm2DzFYiRqvIWSPzCvocZt5hIS_P2ruNDOdKcfLKHyV5Q39jVa7W-H5p5wc-HEwwXsfnwdnKfwIs2y9Alti7zFopTCCPqkuAEgs0Ku5GgYe-r1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=jg7YJXVRcG9gBXG597rTNOnbkYL6Alk2K9-ctjWvgVxMhhJ1AzDXfILYrHT1-F0YrFn9U60E63O4_TEC8k86MLrwz1jHizDXfrHN-Qjw4tvq6cLkjC-U3HLza6w1Q5UvpYwOAkqEtBK3egOXN_xuD939Ye9STTzaNkpn-8jXmkOcpCD-_qJjf7KzsWcept5Jc1nvK5Gb8XXvpQH_tWSqs1-5gIsstfTBJ32n9Rt5BM5sJdab_dAdSg70fWQuys6sfzLJsgHDodpIVCTgFzDnpJfZhz3OFdubpx_rqRarrj_7ObxBugPYzhBFld_-vs78yuCJq53w2zCXRb9suvVr2nEpsDFacbsgMlnXTbhOL5fIJckXhzz6nyorL2uabqbGVGujgMFagTHNh2Lc-iFVTtMYF6FoAy30LwW3s8Wxb0So1tR4OKnu53V5aizHoSSntYa_bid1SgrNjZFnVgbaAw_SzF3whQfx5n9vIjWZglAgbmJ41THgYjml9GSuzV5l1-NV8LamIYkDen5Rx2_1W7seNcsRF2GITREHMxl0azofAA9W1qfGzU1N3QNxkm2DzFYiRqvIWSPzCvocZt5hIS_P2ruNDOdKcfLKHyV5Q39jVa7W-H5p5wc-HEwwXsfnwdnKfwIs2y9Alti7zFopTCCPqkuAEgs0Ku5GgYe-r1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=B7f6mS9GtWXIWUVgMFB7mzQD93KN3lt42je-PFrQ3AezOKwRT1Jso1JRJuxb_77i698qX3p6R9T-w1-75du9yzKyIN0eec2HT4Qsv28YRCNBxBBX2p86U8oSMFRMdpxAfMqu2keU18l5ft96WvmGTYRfmmQ2-_DzM87IrDOJZtkjwPoSAaSsFNSUyAw-afx-W_8wkBL9hoSOVnRwAlShrLyTjE9rHrFQMITgOqGHZYuS-wM-wU_1NEgcYkoMj1mhQEb7tGIzYNp_stZZ-dTFmdwg9BAVoMlLlcfYIAAb401s0wPyTcD54KEezzxgCR6fvMOAGS6OSwYnSOn48CM1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=B7f6mS9GtWXIWUVgMFB7mzQD93KN3lt42je-PFrQ3AezOKwRT1Jso1JRJuxb_77i698qX3p6R9T-w1-75du9yzKyIN0eec2HT4Qsv28YRCNBxBBX2p86U8oSMFRMdpxAfMqu2keU18l5ft96WvmGTYRfmmQ2-_DzM87IrDOJZtkjwPoSAaSsFNSUyAw-afx-W_8wkBL9hoSOVnRwAlShrLyTjE9rHrFQMITgOqGHZYuS-wM-wU_1NEgcYkoMj1mhQEb7tGIzYNp_stZZ-dTFmdwg9BAVoMlLlcfYIAAb401s0wPyTcD54KEezzxgCR6fvMOAGS6OSwYnSOn48CM1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Tivmte-haiRScC1dd_DQTZMr6K9zl6u7D3MYsamjLeAIOZknHMvTYOOPwcTSe3jGDiBQM8dFLxjifUcsTp5fAHKDh27N73acTFCdmFurQTohs8B_4J1raC0mGhmiJaJJryirsb2TvW_O6Fgy8TLnooYyiLxrvrdY-ezXS0o2VTz8k9sP5zWOFSM6iJc9v0FJUIpI9qT5WsqBZXri0fs4CiEucw8AsRzMmAdsqHyL_SnB4vcLKvd-bNgKe0OX2yvjZj80shRZZE5fQjaXCBL1EG9Ugp96oXZnwFxGBakjGG7zW6NfX2TRyu4363JhT7tQRh7T7Fo92PsqGCNXUQxv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Tivmte-haiRScC1dd_DQTZMr6K9zl6u7D3MYsamjLeAIOZknHMvTYOOPwcTSe3jGDiBQM8dFLxjifUcsTp5fAHKDh27N73acTFCdmFurQTohs8B_4J1raC0mGhmiJaJJryirsb2TvW_O6Fgy8TLnooYyiLxrvrdY-ezXS0o2VTz8k9sP5zWOFSM6iJc9v0FJUIpI9qT5WsqBZXri0fs4CiEucw8AsRzMmAdsqHyL_SnB4vcLKvd-bNgKe0OX2yvjZj80shRZZE5fQjaXCBL1EG9Ugp96oXZnwFxGBakjGG7zW6NfX2TRyu4363JhT7tQRh7T7Fo92PsqGCNXUQxv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=IUleqVveIpWpfGILlrniQz98iQbSW14WnXwOb0fAjhoXibS9muBtHde7li7WqGdqj8c_CLVnjQKIUO-EA6LcrPsapdvTnogqPt08wI0emZ_I1dFG-Rf6-5eNMVKRWmAGgDmU5WWDE3MaJW2IwDpMZT2b_rGiRlsG_HLMagYMiGdsg7Xb-FKwOAaQLOdylzNnvn_7A0d0dZ81827mJ34mEKyue4h79S5zcPWv72DipRyVehAMne8d0mqTBVS4BTyU_JiglA2yy3sD0xI5doksUQvnBygrmmCkW6d7p1pUMqCy4ecei62FR0OsvmkpHIvc4bmZOFHIkz5WIRfRkNRWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=IUleqVveIpWpfGILlrniQz98iQbSW14WnXwOb0fAjhoXibS9muBtHde7li7WqGdqj8c_CLVnjQKIUO-EA6LcrPsapdvTnogqPt08wI0emZ_I1dFG-Rf6-5eNMVKRWmAGgDmU5WWDE3MaJW2IwDpMZT2b_rGiRlsG_HLMagYMiGdsg7Xb-FKwOAaQLOdylzNnvn_7A0d0dZ81827mJ34mEKyue4h79S5zcPWv72DipRyVehAMne8d0mqTBVS4BTyU_JiglA2yy3sD0xI5doksUQvnBygrmmCkW6d7p1pUMqCy4ecei62FR0OsvmkpHIvc4bmZOFHIkz5WIRfRkNRWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWd1G68pNBJRPYukm0Muia_hv8TvhUSY_jXwjPenKZvVRXdd153GV0MoGzu-YY4B7DUJqi8816OvDsiEo4WHQfdlqgjBbyDwnRzyr7Uxr_DQexzkLk_4ARF370SkNMulJ79vOej6QCpTbKL_Z2hSy0aIyL5UKOvC5ycvDAUte2VLverU5Dy6_rVucDPDuIJ8vbU5HUNaalYwqfAXuDX0GC8Vir4eBzHn9ZXbY8eJOOMx3kg8FXwwEJ6HPLTdizDtoG7httF93bJqm2uw0ywsmmWADQ9LQHJGDQZpiC1plaF5PA68VwPfwIAhlmUKqpr9DSHQoELJ1KH3ThNdI2tMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=O-1km6w7HYtQbJ-sfrFfhHzQJ8CMGkC0lPeM9074_FTL1KlEh_npUX4a48Fxy5MBbqfsiVcm_UYxMMSwI0Yqn-1TNg8TuFVkUY9kDBvDbxO1I4uTXz-FJU4p0xHZBQP5-rnKlV3rWK37dkBc5cJfI3qoCW7we3p8BEKTz7dH2CF-r27fLJdwZxJ1MmwANYb9VETRLs1ZvrqTY4v44MYy_C8hwvmboCq0-mbsP9_ROg6vJjlkVwrzhDZisCPYywUEYWy4wbu2VUj3OcWriJDVyDkDC1RGYOsrt5NAKFkri6Lte43lsD6DP8kEl4KcfE0wtiKhZyIHsSHhhIOr0TRPWKi-oe6OxQu8ZwlkhtQO_SJZoB9LYndOLZyGua4x2LpHg8ksE9He0PPEq0iNTLGPw0FoASEJk-mS2Zbid6aN0B2IeGvt9BJ0uXeUOuqzkOX5wAIxj_Yo-1EP6E4La-IyI26quI0Q2R7VJ57xWfsdRWY0P62er0NEeqlAv0DbtZFD3lzu1pwO8ZYL1tpZYXRn786TCSlgjyr65tXGBFQEt0coMwv81oBZgRt-AP1cHl3PWdyGzqZvtoIVyWMRn_Se85pgJUUHU1-ECTpyk4QOGdOifxjm_Q1VZQlHos8ovi9hHoM6KUK5vzzOdM_7SbDyHJ4NpytndoZsEu5q1tMJeZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=O-1km6w7HYtQbJ-sfrFfhHzQJ8CMGkC0lPeM9074_FTL1KlEh_npUX4a48Fxy5MBbqfsiVcm_UYxMMSwI0Yqn-1TNg8TuFVkUY9kDBvDbxO1I4uTXz-FJU4p0xHZBQP5-rnKlV3rWK37dkBc5cJfI3qoCW7we3p8BEKTz7dH2CF-r27fLJdwZxJ1MmwANYb9VETRLs1ZvrqTY4v44MYy_C8hwvmboCq0-mbsP9_ROg6vJjlkVwrzhDZisCPYywUEYWy4wbu2VUj3OcWriJDVyDkDC1RGYOsrt5NAKFkri6Lte43lsD6DP8kEl4KcfE0wtiKhZyIHsSHhhIOr0TRPWKi-oe6OxQu8ZwlkhtQO_SJZoB9LYndOLZyGua4x2LpHg8ksE9He0PPEq0iNTLGPw0FoASEJk-mS2Zbid6aN0B2IeGvt9BJ0uXeUOuqzkOX5wAIxj_Yo-1EP6E4La-IyI26quI0Q2R7VJ57xWfsdRWY0P62er0NEeqlAv0DbtZFD3lzu1pwO8ZYL1tpZYXRn786TCSlgjyr65tXGBFQEt0coMwv81oBZgRt-AP1cHl3PWdyGzqZvtoIVyWMRn_Se85pgJUUHU1-ECTpyk4QOGdOifxjm_Q1VZQlHos8ovi9hHoM6KUK5vzzOdM_7SbDyHJ4NpytndoZsEu5q1tMJeZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=jDJjrmD-tVM7yudFqqoJ-zAh9GibtLykSYhqNBIQejP8AL7DB0SpRNe43_JjHV1jRJ7FS31emKUO0s2tug9_zAT_CVoJ4oD4sZ-nLE9DLRWcX9gZiIBXfiEti2lA4no-j9yN1ewfuH0I2s5WESf3OpsbHjy2NFP7AyFfBqJuO0RAKGszEhSo9NUWeMdE2zDntIK9AHwh6DgkewcHC16-PD47RrWQsxwNc7Qu8FltRyAn0EDRvDbOOKeG-QFgL1YRicyNibP8Zy0cU8BPsjYVmtQA_VGhv7Xmm35e05y-GNJ_XSRVYwIlEqL8NI9J6gbtDnmVa-IcfTELil2EHO94EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=jDJjrmD-tVM7yudFqqoJ-zAh9GibtLykSYhqNBIQejP8AL7DB0SpRNe43_JjHV1jRJ7FS31emKUO0s2tug9_zAT_CVoJ4oD4sZ-nLE9DLRWcX9gZiIBXfiEti2lA4no-j9yN1ewfuH0I2s5WESf3OpsbHjy2NFP7AyFfBqJuO0RAKGszEhSo9NUWeMdE2zDntIK9AHwh6DgkewcHC16-PD47RrWQsxwNc7Qu8FltRyAn0EDRvDbOOKeG-QFgL1YRicyNibP8Zy0cU8BPsjYVmtQA_VGhv7Xmm35e05y-GNJ_XSRVYwIlEqL8NI9J6gbtDnmVa-IcfTELil2EHO94EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4MrbMov2H2zbl-aSEuBDIZBXRCbcOu-Eu4v8wfSR25yUNdVrKVXtFln8xNYXugYXssbMy4PPMtBeoQnPjL3euXw240BrgGnHWvcYYidIVMmIOytfpu33wmBxTvFobjbIlyZs2U5OHDwJab00lx76gyTNv_r8b-dlEXXB892L9e0UT_8aV92IPQ6TvUWurLzidKVkURdYE-75Vkbr-T-N1T257h3doVU19upMzx8nKHpPNvk_FWTyiWN-jssljEgTHpouzGfLFVFSKzZVh-VWae-wGdcLOQHSZoVfMwFemeuU9_Jg_2sJYZ97dcAJsIl7tBo40LjUUkdnzgBxE5tRRQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4MrbMov2H2zbl-aSEuBDIZBXRCbcOu-Eu4v8wfSR25yUNdVrKVXtFln8xNYXugYXssbMy4PPMtBeoQnPjL3euXw240BrgGnHWvcYYidIVMmIOytfpu33wmBxTvFobjbIlyZs2U5OHDwJab00lx76gyTNv_r8b-dlEXXB892L9e0UT_8aV92IPQ6TvUWurLzidKVkURdYE-75Vkbr-T-N1T257h3doVU19upMzx8nKHpPNvk_FWTyiWN-jssljEgTHpouzGfLFVFSKzZVh-VWae-wGdcLOQHSZoVfMwFemeuU9_Jg_2sJYZ97dcAJsIl7tBo40LjUUkdnzgBxE5tRRQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=h8dcYV40v1w903q6AxYNu0KnOK_xa87UvsVxIshU9NHQxGtJ1eX0bS_Xi9cGam4FGrzdFEJhTZyR9VcFEuyHMt-uM6WL79uFBd7YAQjGUswrO2OJj2uz87PbQvpNlh6lygyxU1s0w6dTK7XSO3WSqqdPzuxBVhkK0fn7WEqgYDm6s6I0nHYHHQxxmNztC6io0Am7MGpqQXO3dEzpLtOak1If5tDZTg8okiMWR_b_IWIOoRzveLUaomARaX8iwk9HMXW8mQKOIYSdBK7TdPNBl_YUXw1ow2luVAoeQFMurzcIjX7qU8Hk22fwKyCJGmuCtR3D8EI-v45lOF_q46_SKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=h8dcYV40v1w903q6AxYNu0KnOK_xa87UvsVxIshU9NHQxGtJ1eX0bS_Xi9cGam4FGrzdFEJhTZyR9VcFEuyHMt-uM6WL79uFBd7YAQjGUswrO2OJj2uz87PbQvpNlh6lygyxU1s0w6dTK7XSO3WSqqdPzuxBVhkK0fn7WEqgYDm6s6I0nHYHHQxxmNztC6io0Am7MGpqQXO3dEzpLtOak1If5tDZTg8okiMWR_b_IWIOoRzveLUaomARaX8iwk9HMXW8mQKOIYSdBK7TdPNBl_YUXw1ow2luVAoeQFMurzcIjX7qU8Hk22fwKyCJGmuCtR3D8EI-v45lOF_q46_SKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHjEsJgpZ4Vbk_90DhEaxg7kHPQSD7z9DFb8nsAkHKCHdwzNPES30bFxoUjYYqjmi4oIwOl4dUUTNE5AmrRHWdtSvMRxiXUVfsZ96ZLJKH0kc2iOWwficFvopg8lpywagYtfTJt7aTFboJ9Vflrfm2LqrsNDKujzu3Z7fbAJEEe6IfNGmcjQYAOMdE8B-0wdVKgoa72_TrY_C8epQyvyd4T4bCZI3nc4FZCT3dihEi6yGT4Qw58SqxJaizR5B6eqGCIrM-cth0BILQEkJ-wC5H46CZiWVi8tZzAodAEOzHPrJBoXVzypoeA2Z_E06XJf0r-_ilpvXiPAB8G24bQyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=j5uiPSBKv5seT-IMwjRwYfbMq3uitXPiCkXSxh0oOObzoi980wBI5AQjkP7jYd6UARdMyWy57yPxyBVuyDMrMr-zXL4BhpB58kzgVRi4N5r-Dq1NJEt7ycoxzO3vs9dP1EcHN7GGid56MIY7eap-T6cIt3UhkEyZFUwe3guYiaVbhgaak8QOHZbGHK7x814YlNX9bryuxqDNOVVJroaT_vM12cRYPjnY6BX7gwolUcIt06D6Wjt6gXPpYZC6HwoaYmoyaw1LxgQRk2OyYPb3YmIYZ-_c5H_7KiLcQA24rUr--28syhwdZ6v-LlaGzjG3_NZ5EdUNXiSpiOpUVQbr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=j5uiPSBKv5seT-IMwjRwYfbMq3uitXPiCkXSxh0oOObzoi980wBI5AQjkP7jYd6UARdMyWy57yPxyBVuyDMrMr-zXL4BhpB58kzgVRi4N5r-Dq1NJEt7ycoxzO3vs9dP1EcHN7GGid56MIY7eap-T6cIt3UhkEyZFUwe3guYiaVbhgaak8QOHZbGHK7x814YlNX9bryuxqDNOVVJroaT_vM12cRYPjnY6BX7gwolUcIt06D6Wjt6gXPpYZC6HwoaYmoyaw1LxgQRk2OyYPb3YmIYZ-_c5H_7KiLcQA24rUr--28syhwdZ6v-LlaGzjG3_NZ5EdUNXiSpiOpUVQbr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=u80B00XZXfWyOeGQdINcHayC1rkizm3IPLF4hXQSuSgAOVB0cSMzIzoXBlFK5BebpmnYoZoW8ovcrYtw4L5798vRAa55LVribLGueYIqnuLEREJTCbNDIdelSH5iiQ_QZzpIwEFDCsbKAft00eoN9xgvd4HkuyLQsjhV5LGDdoTI2sD9yg89KnrMgKuT7QRn4DJpmfmfXfenXas7KXRFBtMoUJrTQxebuhimro49t-P1w_EnHAxPRyGJt5_jxvskhEZu-kDMcSu7yLscsnR7-djWM9Svgj1djwsnKc8YsPxV3iKWJ_0Ei5mziCZgIqmcULUKFh7fezyaDPEZ90asxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=u80B00XZXfWyOeGQdINcHayC1rkizm3IPLF4hXQSuSgAOVB0cSMzIzoXBlFK5BebpmnYoZoW8ovcrYtw4L5798vRAa55LVribLGueYIqnuLEREJTCbNDIdelSH5iiQ_QZzpIwEFDCsbKAft00eoN9xgvd4HkuyLQsjhV5LGDdoTI2sD9yg89KnrMgKuT7QRn4DJpmfmfXfenXas7KXRFBtMoUJrTQxebuhimro49t-P1w_EnHAxPRyGJt5_jxvskhEZu-kDMcSu7yLscsnR7-djWM9Svgj1djwsnKc8YsPxV3iKWJ_0Ei5mziCZgIqmcULUKFh7fezyaDPEZ90asxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=Dvt2H6zj9KwE2ZGedceMrtgCCxOvSQJdJ4FI-RakGhhLVOab5Qim7frphhkxfRotaix3VByROt5bhXRbT_5AXWphant2BWUS_gcx6jkj0yZwydCy1lY1hj8QOx-t_tGCkV2y8ENjt7UFX1rqJuT4gFhsJ9eOWxtnc61-1tuyzu8M4GI2IyhoUIG2ngNw2Inq2KlyaEuSdCYs5IA0y9ElZi5peh2ucPJ7bmEE3dvhFfhEU1tW0euGs6zne3kbvGYTcPnaPGfTCTmzpSGnXiRBHoN-u9dAMQuctsh3wUgvvKaERbm3cD6c-_xMIoqMXFobKPRfzRxSHAUIXNQrNojLYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=Dvt2H6zj9KwE2ZGedceMrtgCCxOvSQJdJ4FI-RakGhhLVOab5Qim7frphhkxfRotaix3VByROt5bhXRbT_5AXWphant2BWUS_gcx6jkj0yZwydCy1lY1hj8QOx-t_tGCkV2y8ENjt7UFX1rqJuT4gFhsJ9eOWxtnc61-1tuyzu8M4GI2IyhoUIG2ngNw2Inq2KlyaEuSdCYs5IA0y9ElZi5peh2ucPJ7bmEE3dvhFfhEU1tW0euGs6zne3kbvGYTcPnaPGfTCTmzpSGnXiRBHoN-u9dAMQuctsh3wUgvvKaERbm3cD6c-_xMIoqMXFobKPRfzRxSHAUIXNQrNojLYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=Vlp-ygeJSDl7v6aXx1mX7EKykwaen4XTE-bd_PzsusaIBJXiYTM5czzMWd7xS8PWaoS6nMadY3cd4biQ9l16i2kdfg-uqjduTxnHWdafVdea1DVfFC0QihdvKWvwbHFCRF3N_9gOsaDpJasF0Sn5rJ6eu-8vD5bykJaxZi8ULtMcPJ6BmF10nVGgxiv54NB5VLHehDhRBH0SjqhzvAH-dX_SxRkyDGZ7RpeFLQrwtps1S-IbNAJD5OZhQKtOJjOBChMD212XOMnceJeOcpYg2RZL8nnDvFSCsm0zcddiG5Kuasbq44233RkrFJcXuzarnWuY3vt89mz-6ylSGf1ghTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=Vlp-ygeJSDl7v6aXx1mX7EKykwaen4XTE-bd_PzsusaIBJXiYTM5czzMWd7xS8PWaoS6nMadY3cd4biQ9l16i2kdfg-uqjduTxnHWdafVdea1DVfFC0QihdvKWvwbHFCRF3N_9gOsaDpJasF0Sn5rJ6eu-8vD5bykJaxZi8ULtMcPJ6BmF10nVGgxiv54NB5VLHehDhRBH0SjqhzvAH-dX_SxRkyDGZ7RpeFLQrwtps1S-IbNAJD5OZhQKtOJjOBChMD212XOMnceJeOcpYg2RZL8nnDvFSCsm0zcddiG5Kuasbq44233RkrFJcXuzarnWuY3vt89mz-6ylSGf1ghTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=X1Wmjk87e0s9dkBB5HBMJtJt2nTTc1-dsmpkPZSpsKeJ2-p52MXiyNzyvWjC2FDYIVvpvhVpmx4I4Ui3Cy_APKeL4zg1JnGtsjt999_OwC7sV1zD9YznotvpUXO9G55CgRO0ajEtmSp4H0L5WvJMUlzjA3hVQRggMpmti84vOKKEnAt4diP-qISgFXcQKTEbhYwazCD32hrfKj9BNE61A7WR5-iZ_Tn0txuugTE02qmZ5dPMkWwkfQ2_9HI6YTNHhVoG9-B44xHziWsO51u0WGLUXrsLlalasJIyp3T3lIlybPcgfVNcDYJmnKD8ntIVMSCS8ndUjzeKNFGrggXWaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=X1Wmjk87e0s9dkBB5HBMJtJt2nTTc1-dsmpkPZSpsKeJ2-p52MXiyNzyvWjC2FDYIVvpvhVpmx4I4Ui3Cy_APKeL4zg1JnGtsjt999_OwC7sV1zD9YznotvpUXO9G55CgRO0ajEtmSp4H0L5WvJMUlzjA3hVQRggMpmti84vOKKEnAt4diP-qISgFXcQKTEbhYwazCD32hrfKj9BNE61A7WR5-iZ_Tn0txuugTE02qmZ5dPMkWwkfQ2_9HI6YTNHhVoG9-B44xHziWsO51u0WGLUXrsLlalasJIyp3T3lIlybPcgfVNcDYJmnKD8ntIVMSCS8ndUjzeKNFGrggXWaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=IDU2W-EeNVyiMGU9vyectm6f17PKKMpSierhAafnP1M10wlmH6DnwU7ZRFMdBCSuVtd7NErLnb9uiXfmjXoZNjByX0NNKBd3NQ1e--XFcvJ3flgnCi4yceBtLN-vfx9inourbZFQzYyRVxgy9OifRyiAtWI2a0BLVlEeynE-VQzBBH7yralM12ccBQoz9D60NpD_vCG9cToSLo4Cw1fyoADA9Xit1MhkaNyQhiT-5OyBBoZVkhu5BXToAzk4qQVEgwA94QWuQVJVHMxSjuAvGphARW2DPVUKQkzXo0WarpVdqQeim1DtieNxeFQvNMWs1cN3CvqjnQkVh-U3L_0CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=IDU2W-EeNVyiMGU9vyectm6f17PKKMpSierhAafnP1M10wlmH6DnwU7ZRFMdBCSuVtd7NErLnb9uiXfmjXoZNjByX0NNKBd3NQ1e--XFcvJ3flgnCi4yceBtLN-vfx9inourbZFQzYyRVxgy9OifRyiAtWI2a0BLVlEeynE-VQzBBH7yralM12ccBQoz9D60NpD_vCG9cToSLo4Cw1fyoADA9Xit1MhkaNyQhiT-5OyBBoZVkhu5BXToAzk4qQVEgwA94QWuQVJVHMxSjuAvGphARW2DPVUKQkzXo0WarpVdqQeim1DtieNxeFQvNMWs1cN3CvqjnQkVh-U3L_0CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=rYch-AxNYhpDvETcbC_E0vDDNDY7REsyKYyCaKBWCVmyii0nVN92d4OYiqRPjejYTpkFmZzuiQ9TiN3m2ToVkIKk5BCnlIM6WSm-ZWV05TOU2DkLeNDtiQV0arvRpF3apkmM6EsC6NQATOSGg_a8fC-MvUx5V8WTWzgmptD2c9UBK9aJpChZHfXfMeK3vH8Af85AhnMuijydeAuSfzGdgYVWUCmF5m_C_pP_LFLlMkb2G0QJoibM2A5ajv-J7B-BKuJg-4BrhvAqrPtXHt7PmBWGtB5GdbO3NY1Ey9LCWct1jpzFwEOZ1Psw65T6QD9FuDXBLgVtkSLbMFja60fagjEOEa6Li7cSiCfDwA0eDWNPzB54PH4oFS1HXdOOcdmr6MdKeQJPCdvMgDcjhXjvbZIxlPFxxm3rZid2bkQA2MoTcqf6ksPrk30f6OSNjtMUEy8XsRLJzi35B63G-wH1Yk2Aphe6kUTD7alUlvV8lChZ4hAnDDnmhMl0Uxz82lUMxKprGAhrJL-R6PEpY1QE-SsztPHNMT_TuxBkkMsbW-Y-0rtpLvfIOEFPmEkX-7fk-6eTQXoq_K9z9wpfMV3mi9EwSH2-rGB3A4-dij2dbrTy0r_hGT3ad_62fc3ynP3LbXRvIT-rjZ8G71ARDmipYOL-p8uDzOkAMpOvgc7Pk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=rYch-AxNYhpDvETcbC_E0vDDNDY7REsyKYyCaKBWCVmyii0nVN92d4OYiqRPjejYTpkFmZzuiQ9TiN3m2ToVkIKk5BCnlIM6WSm-ZWV05TOU2DkLeNDtiQV0arvRpF3apkmM6EsC6NQATOSGg_a8fC-MvUx5V8WTWzgmptD2c9UBK9aJpChZHfXfMeK3vH8Af85AhnMuijydeAuSfzGdgYVWUCmF5m_C_pP_LFLlMkb2G0QJoibM2A5ajv-J7B-BKuJg-4BrhvAqrPtXHt7PmBWGtB5GdbO3NY1Ey9LCWct1jpzFwEOZ1Psw65T6QD9FuDXBLgVtkSLbMFja60fagjEOEa6Li7cSiCfDwA0eDWNPzB54PH4oFS1HXdOOcdmr6MdKeQJPCdvMgDcjhXjvbZIxlPFxxm3rZid2bkQA2MoTcqf6ksPrk30f6OSNjtMUEy8XsRLJzi35B63G-wH1Yk2Aphe6kUTD7alUlvV8lChZ4hAnDDnmhMl0Uxz82lUMxKprGAhrJL-R6PEpY1QE-SsztPHNMT_TuxBkkMsbW-Y-0rtpLvfIOEFPmEkX-7fk-6eTQXoq_K9z9wpfMV3mi9EwSH2-rGB3A4-dij2dbrTy0r_hGT3ad_62fc3ynP3LbXRvIT-rjZ8G71ARDmipYOL-p8uDzOkAMpOvgc7Pk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=IIYXddxUIdUcMILvTOw_SqjXqUHcjJaPGjU-IUlSqzGZ-dkOj_1wzwNpvzUVrcWj0E80_yOIwv_rbkip2tj8FXwa6-SbdpUe9s6r7yuxh2TtB-3Ume1kGywh38LpxZPYJd5XE-6c-O3eD0um5i7ZnP5iP2UmzS8iq3xTtbq4qI10ich1YSCIn7DseobIV1QYEEzIWKfYNlhO6nh81-bVY5DiMXJJTguk2bSfFQnHidzhbiMuhBOA1tGQJacakeLl7cbJIu4TObrYvTP_kpb1W9C7Vi3Fq36c6PWgk1zcbwAFzZz5UUJwp4oYMgamPsR_rmgICKtVUGyvVYc_7-xilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=IIYXddxUIdUcMILvTOw_SqjXqUHcjJaPGjU-IUlSqzGZ-dkOj_1wzwNpvzUVrcWj0E80_yOIwv_rbkip2tj8FXwa6-SbdpUe9s6r7yuxh2TtB-3Ume1kGywh38LpxZPYJd5XE-6c-O3eD0um5i7ZnP5iP2UmzS8iq3xTtbq4qI10ich1YSCIn7DseobIV1QYEEzIWKfYNlhO6nh81-bVY5DiMXJJTguk2bSfFQnHidzhbiMuhBOA1tGQJacakeLl7cbJIu4TObrYvTP_kpb1W9C7Vi3Fq36c6PWgk1zcbwAFzZz5UUJwp4oYMgamPsR_rmgICKtVUGyvVYc_7-xilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=BNeDTyGNiMhaMQHuLSojnyFTisK8pl16O8yLct0SndU5hdaQ5AW_0YZ-1_mD_raE0TP5k_RzJgNJR-9LhJ3dfXJH71Aocg1l4u4yjUjBPQ3TqXSnMI7LfTfkiejN0Eah4xNBgG8eC-E4pewc290qH6MOWQeQU7ntmHyScNnBCBbGc0Sbpyjei5bTIQz8c0skpwrY-UNh831D8eOFbx36AVwlvVEWKuB89Hhpf5oLLxDxTehrMy3coW_AT2bm3CVm2TO4zHhZ8hRTn9La_mUBQHHmuzPD1cwLyEBJBWEF3Enl_lmAtDckE7XoVczCPWh-xKQUXXp7SeiagN_UeI06mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=BNeDTyGNiMhaMQHuLSojnyFTisK8pl16O8yLct0SndU5hdaQ5AW_0YZ-1_mD_raE0TP5k_RzJgNJR-9LhJ3dfXJH71Aocg1l4u4yjUjBPQ3TqXSnMI7LfTfkiejN0Eah4xNBgG8eC-E4pewc290qH6MOWQeQU7ntmHyScNnBCBbGc0Sbpyjei5bTIQz8c0skpwrY-UNh831D8eOFbx36AVwlvVEWKuB89Hhpf5oLLxDxTehrMy3coW_AT2bm3CVm2TO4zHhZ8hRTn9La_mUBQHHmuzPD1cwLyEBJBWEF3Enl_lmAtDckE7XoVczCPWh-xKQUXXp7SeiagN_UeI06mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=uJxy3b4Q6bCReJCz1H4GCEgd-WvU28VbCM5tZKs81mHm6b-cWIBsscsWr6RJsJlGJU9u297B3a7Bpxco-7DltxVQiXvxzjbLAA0ND8dt4FqWIBhNMouvKusNGfXmEBhWG31YLRlTx-HiI1y4K8Z5U51uWyYkXqTC1UjuLAxMuv5qWsmPR_ggnjNNhgbB_pJa3ObbZugSqJw11Gr8QgcBYItcC7ONPZZlY3R9L2jtoZTaHt0Af-G1PsLR2pI7kdHccPFMBQZXgu0j5D1mZDnTc-0HcwaNRNClCcH20bOjD6YJIxyoUfaMOZxlO6iKkJsX-ZGy9Khx4KtaZS84t__4xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=uJxy3b4Q6bCReJCz1H4GCEgd-WvU28VbCM5tZKs81mHm6b-cWIBsscsWr6RJsJlGJU9u297B3a7Bpxco-7DltxVQiXvxzjbLAA0ND8dt4FqWIBhNMouvKusNGfXmEBhWG31YLRlTx-HiI1y4K8Z5U51uWyYkXqTC1UjuLAxMuv5qWsmPR_ggnjNNhgbB_pJa3ObbZugSqJw11Gr8QgcBYItcC7ONPZZlY3R9L2jtoZTaHt0Af-G1PsLR2pI7kdHccPFMBQZXgu0j5D1mZDnTc-0HcwaNRNClCcH20bOjD6YJIxyoUfaMOZxlO6iKkJsX-ZGy9Khx4KtaZS84t__4xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=IwpXWHVdPvANUvanuMCjd-sZGF-E8_0X-DCE2rPHU-M5LARSMCApFUyluAXI_4KqOcWskPAbgB1AQsH-DKd9xwUd_haOXnfKXd1JQ1KsN5wxxtrOTKpUenPsKHW98w6TE9iRnQRMABAlBK3CszgkfuYkM1tlZzdcGB1HamEpC-7Z6Kwncv6nMLqWRaWC1bXfklKV294eVAUM3jHGWN9oFEpusIwL5kVRNSQhEb2Y2Z48LrgJ_6GY_tuqnaukAAY_2QwmBnFJfWCCxnXwmasFE74RppVUAPu256l4k67Tt4agMEQewFNrQldx0-2IAAQDGIFeXuW1I7ckg856_BISPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=IwpXWHVdPvANUvanuMCjd-sZGF-E8_0X-DCE2rPHU-M5LARSMCApFUyluAXI_4KqOcWskPAbgB1AQsH-DKd9xwUd_haOXnfKXd1JQ1KsN5wxxtrOTKpUenPsKHW98w6TE9iRnQRMABAlBK3CszgkfuYkM1tlZzdcGB1HamEpC-7Z6Kwncv6nMLqWRaWC1bXfklKV294eVAUM3jHGWN9oFEpusIwL5kVRNSQhEb2Y2Z48LrgJ_6GY_tuqnaukAAY_2QwmBnFJfWCCxnXwmasFE74RppVUAPu256l4k67Tt4agMEQewFNrQldx0-2IAAQDGIFeXuW1I7ckg856_BISPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=M3X2S3Myhm-GH5NXo4uj9WDx1V2k-ChqmwCA-2PNgnnyndB9R5lpqbfnPa2R140qi01r4p85jM_MmJdZtzqFIDxMDHDSlPJBwt8fOQVm-IMDTpCSq4T1wEC8K7t2qtWoqeOgyE46fjc3zGAi5uGpRuuapl_GgcdGCoRPaf5QL3HB-lDz8rwpjK8SZA34P8xKuyIjDTzTtXeCprWBtwvMGcOy4MwGPtSaARDgeZ9Lhxihcub_g1Fv30e5DUG5FvSJ5wtmiDCKzsXnprUgeoUWZQr7MyZqSFHSWowUt5ArLm_kX77vu3C_cGJBCtg79RW2a_xBC51MsAlqoaLsbVT20A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=M3X2S3Myhm-GH5NXo4uj9WDx1V2k-ChqmwCA-2PNgnnyndB9R5lpqbfnPa2R140qi01r4p85jM_MmJdZtzqFIDxMDHDSlPJBwt8fOQVm-IMDTpCSq4T1wEC8K7t2qtWoqeOgyE46fjc3zGAi5uGpRuuapl_GgcdGCoRPaf5QL3HB-lDz8rwpjK8SZA34P8xKuyIjDTzTtXeCprWBtwvMGcOy4MwGPtSaARDgeZ9Lhxihcub_g1Fv30e5DUG5FvSJ5wtmiDCKzsXnprUgeoUWZQr7MyZqSFHSWowUt5ArLm_kX77vu3C_cGJBCtg79RW2a_xBC51MsAlqoaLsbVT20A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpf0Lln24s0JXlzpBmO_vI6r6wEjha01-EGBzgWMObvGtdsZ7xMqh50jFrXaHL3MdkOpDwA_oVer6mQ3q5oEiHNqZj4mxepvHifOqCTlOGRVQbZmcYK5f0S66oHeWp9H6N78qsHGUJfA-3Y5KI7QDasKp5Bq3T0-MSfB7cFxekxIvEF99tTaioUbOr5__iHaHh_8oBB1L4HmvGybsM1UOPWRDkdq9qmt8sKSNRlv0QBnnSgonWOiNsMNpbOXtSe1QcxZWUxXY8e9V0w9eRkinBM0rxrjQ1mLd4RsVFu-YjTthslXNCAb2_jwT-CpbYLZ7JrmxGONB7uEFyTlYzFYyGWcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpf0Lln24s0JXlzpBmO_vI6r6wEjha01-EGBzgWMObvGtdsZ7xMqh50jFrXaHL3MdkOpDwA_oVer6mQ3q5oEiHNqZj4mxepvHifOqCTlOGRVQbZmcYK5f0S66oHeWp9H6N78qsHGUJfA-3Y5KI7QDasKp5Bq3T0-MSfB7cFxekxIvEF99tTaioUbOr5__iHaHh_8oBB1L4HmvGybsM1UOPWRDkdq9qmt8sKSNRlv0QBnnSgonWOiNsMNpbOXtSe1QcxZWUxXY8e9V0w9eRkinBM0rxrjQ1mLd4RsVFu-YjTthslXNCAb2_jwT-CpbYLZ7JrmxGONB7uEFyTlYzFYyGWcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=SiClRw8iF_TkZAOa8a8efcbevJ6BhOFxNpJVeo2_Ihl_TvEB2vGqQKMovYHpAaBbjEKW7TQtKRtoLpkmA6HQMngnjwAEljKzm3BbPeQfwYcYZNoxmG-feDFCUG5xvgpUd5KV5Mi5sWPDwLg7FGyFIvVAISs7-oAi-o2Gp0MpWt9xmlpFt2HDaS2pQRfogBgE2kAv-4A3P0jfZJ9qQKIDz4rhpJryxSMRQhNJyOFtNPtZjUnLqk0h58HglvPsVpU-HnbNx6BC_HeRteiew4MerxXTvfIgwEvSW92J7z5vd_MPlyfo9c62_lW1Zr1kW9KjAALy_mGt1vsFjC3IaYZ-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=SiClRw8iF_TkZAOa8a8efcbevJ6BhOFxNpJVeo2_Ihl_TvEB2vGqQKMovYHpAaBbjEKW7TQtKRtoLpkmA6HQMngnjwAEljKzm3BbPeQfwYcYZNoxmG-feDFCUG5xvgpUd5KV5Mi5sWPDwLg7FGyFIvVAISs7-oAi-o2Gp0MpWt9xmlpFt2HDaS2pQRfogBgE2kAv-4A3P0jfZJ9qQKIDz4rhpJryxSMRQhNJyOFtNPtZjUnLqk0h58HglvPsVpU-HnbNx6BC_HeRteiew4MerxXTvfIgwEvSW92J7z5vd_MPlyfo9c62_lW1Zr1kW9KjAALy_mGt1vsFjC3IaYZ-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq9ANuc4bU6yqE64vvi2e11-CdUuhY_tSaO0T5XEJKW_Q3AvEn7nuXvX0q36Jfl2y9aG0_kZLFKdLO4xvcqFucjhrEoxDEzXXf1jegdOAdAYcdD3YlXM3NY9gHXYlY36a5SoPJDwKZYp6ypZ5rf83ClO06DJEqbodv6t8ZfT2wJSosiB0rn8WFY_kSCxidz0g4fSbCWZWQfq4Xvxy8Jm9SDTnHwmYyL5S-R70Y-ohB-JHhge3EH4Rdkh69V3_bGxU4fy2Qk5KGVQYdvNKf0X2vIRm0my41XuZvurg1HhCTo1NQbyeXYnLIYwWg1qEkI0zAK8h9nmqyIrPtRD0uG6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=lA7cy62rVu4525SrNJSmArBw_BG7JHBSWjIoF4LUggSFGIors6r4NJWzg4owF-T9WGYTcWkwYl6_bnc3YslO3sABmMMT94QmGSuUbtGVpNG8Rm70WyDeGFD3dGJL1n97F8f1V1SdqyKmrKMnh0iyXXLo99ITaKA5boEiN2IlBBUZS9H8ycqppaU9Fg6LxXekZGfvN8KdcljXCJJtbq_M8EoVXhlTtLb9eAc8_vpqzHX3972JND4YmYKwXzZv4Tkoa1TVcdSYv_4MoBlsdrVbDc3qZ3S_NC7NBdBAABulijruKnqw5LM7KutW63lDrBzysD7D7XblAZYlN-SPObHMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=lA7cy62rVu4525SrNJSmArBw_BG7JHBSWjIoF4LUggSFGIors6r4NJWzg4owF-T9WGYTcWkwYl6_bnc3YslO3sABmMMT94QmGSuUbtGVpNG8Rm70WyDeGFD3dGJL1n97F8f1V1SdqyKmrKMnh0iyXXLo99ITaKA5boEiN2IlBBUZS9H8ycqppaU9Fg6LxXekZGfvN8KdcljXCJJtbq_M8EoVXhlTtLb9eAc8_vpqzHX3972JND4YmYKwXzZv4Tkoa1TVcdSYv_4MoBlsdrVbDc3qZ3S_NC7NBdBAABulijruKnqw5LM7KutW63lDrBzysD7D7XblAZYlN-SPObHMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=qfLEwLmoM43-DUEPR7MciuBXF3aKKxtboY7bGuLfV8haE-z_oUJSwbcQDu_NdZf3ckhrOYehAqCoISGUKanZrmkC55gwbBS5q25_KSiL9m85b4TMfO6oH2dLhxrGbvGfay0siPTkXYaZQpdMdpYtOiQlYM1P5GWTiT_3RpGZMp-ozfxImw94p3irJxE3__rpj1rzXDZEiQqOZmUHxsidcomLrvWFqmCadFWqDi8Ylbpx9q60L6pyUNpxNL5xAt1Y72bd7mqNrvuXi3BOQLvA8Y5BKd2RchG71hCmenSr05HuNQ38zMdVV-CL7gHoMF6Y7yi2T5cpSBf8sHhDlub--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=qfLEwLmoM43-DUEPR7MciuBXF3aKKxtboY7bGuLfV8haE-z_oUJSwbcQDu_NdZf3ckhrOYehAqCoISGUKanZrmkC55gwbBS5q25_KSiL9m85b4TMfO6oH2dLhxrGbvGfay0siPTkXYaZQpdMdpYtOiQlYM1P5GWTiT_3RpGZMp-ozfxImw94p3irJxE3__rpj1rzXDZEiQqOZmUHxsidcomLrvWFqmCadFWqDi8Ylbpx9q60L6pyUNpxNL5xAt1Y72bd7mqNrvuXi3BOQLvA8Y5BKd2RchG71hCmenSr05HuNQ38zMdVV-CL7gHoMF6Y7yi2T5cpSBf8sHhDlub--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=tq-6U-scv8neX76FWa2GrFVHCuvvijXhGunhJ7MPGZRLu5LCdXV7eT6eg0wcNj7eJ1AHOv6yiG558pITz5y7qOOnAky_ZJc8iMj5X5He-1P1AsEzoXy9KQGdIO9Mc0ULbCNLCHiLBpDBDFcT4YNStarcawlOoj4pPnXwYpxZ2fG2jMyjWrjWwynSHNQOdcy2_HP0TWrqoU-CrFCd6HIOs1FcU08v4MzbJSbFhSzGMOncG4AmVBIPF9hhGGwyerX8K7gE-Cpg2FLzU31RVexMEYHlhGWxbVjyAcs1Nkxr5DU1-wPu_Khe2xDS3bgtKZDubFIokWTAsJuypfbdPRvDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=tq-6U-scv8neX76FWa2GrFVHCuvvijXhGunhJ7MPGZRLu5LCdXV7eT6eg0wcNj7eJ1AHOv6yiG558pITz5y7qOOnAky_ZJc8iMj5X5He-1P1AsEzoXy9KQGdIO9Mc0ULbCNLCHiLBpDBDFcT4YNStarcawlOoj4pPnXwYpxZ2fG2jMyjWrjWwynSHNQOdcy2_HP0TWrqoU-CrFCd6HIOs1FcU08v4MzbJSbFhSzGMOncG4AmVBIPF9hhGGwyerX8K7gE-Cpg2FLzU31RVexMEYHlhGWxbVjyAcs1Nkxr5DU1-wPu_Khe2xDS3bgtKZDubFIokWTAsJuypfbdPRvDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=skAjtjxGPBWFQp-tiRtZKbXTxjjN74RkZX4UjJ56AP2g0A0O45h6Ac_eEQi_SDFZT3B1H0nq2_xNI3WEftuqtzN956slsJvCbKgTyNmXQOb5mcIAmvmFlbHqBvO1XccmUx2mbvUnchgYxALCI6XwkaJOaxj3d95wG4OiMLAD-m9JVoQIWGkyW3FxIPPDtVujDF-OXoXgdA8EppMoyrEG_ytXEMXVZK0HieLv6kYUAvnIsTzhlzlxVI8Wjza4Z0BHXAs6fSrkPI3j1F3Lm8xKd8PdeQ5s_16RbG2gVLCWHrgP4h1Xl7jcD94d2sJq99vqVgVP72S5GkSF-fHO8MJAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=skAjtjxGPBWFQp-tiRtZKbXTxjjN74RkZX4UjJ56AP2g0A0O45h6Ac_eEQi_SDFZT3B1H0nq2_xNI3WEftuqtzN956slsJvCbKgTyNmXQOb5mcIAmvmFlbHqBvO1XccmUx2mbvUnchgYxALCI6XwkaJOaxj3d95wG4OiMLAD-m9JVoQIWGkyW3FxIPPDtVujDF-OXoXgdA8EppMoyrEG_ytXEMXVZK0HieLv6kYUAvnIsTzhlzlxVI8Wjza4Z0BHXAs6fSrkPI3j1F3Lm8xKd8PdeQ5s_16RbG2gVLCWHrgP4h1Xl7jcD94d2sJq99vqVgVP72S5GkSF-fHO8MJAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=StdDLq9DGaaTysOW8uzy2HM6CQeXWx8x9sblFGctGv0z7VNj1DnBYjJ27-QDUMW3ElbKuDnRVhRcPK7D89p5P-1ek4zup7omWC5O7Qo4O-w4qoGwBlmHuTG2E85gejNwKXolxdhqbvY9P9RXvvQZ9LsV-TkKluqhQv3dk9EjAupmMn5znQjZt6gALPLFdQkzg6FkCL-iKlEvYo8tIeCKH4ZpW9zFrHdTrXw8ClGGcdWYO4GGi-V4Zik70i5YZ7uIKeXNEydBZDay0delKt3v-Hub54S8tLHlomU-2zG_2cWDh306AYwXXjUWp6_P20SRSrgldygaNRFOGn-M_xYemA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=StdDLq9DGaaTysOW8uzy2HM6CQeXWx8x9sblFGctGv0z7VNj1DnBYjJ27-QDUMW3ElbKuDnRVhRcPK7D89p5P-1ek4zup7omWC5O7Qo4O-w4qoGwBlmHuTG2E85gejNwKXolxdhqbvY9P9RXvvQZ9LsV-TkKluqhQv3dk9EjAupmMn5znQjZt6gALPLFdQkzg6FkCL-iKlEvYo8tIeCKH4ZpW9zFrHdTrXw8ClGGcdWYO4GGi-V4Zik70i5YZ7uIKeXNEydBZDay0delKt3v-Hub54S8tLHlomU-2zG_2cWDh306AYwXXjUWp6_P20SRSrgldygaNRFOGn-M_xYemA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pP_tfRIlnDOb1LoiLmdnREMHTsQ2h2niC1j9jXnfDFQekV03PVag4RjVzUBy2XNaLgv-K8OkCRc5E0UHOEq3HRvUQpdtwem9CJcGDzVStDuCYY403vUmrHucmBUVU72pLeaP0wDk2gB766ba5FNDTTKZFEHtVjoeQzqPQAzWAiABoiTW5yiBo04Gj9_rQWXMU_EYWa_VxisVdZy4L0h0BQTpAOHtnt0r-O8qLnsndBJlG-As4s4kz9jbkuTIuHVwAyKrT7HioEFVfiyT7aU65vIhs0sJ3JaPiVUoPbJxUxJDY2dXs_S_zaKLp_7Z5eTq5cV3xp2eQgHPyvXmWiC4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9M6BRz3qdjbLKR_qt2JH8soAX77-bXFDgfqR8--HQa1h1UzTdp5s92hkvMFgtmpyctSTH2YHcPXUq1MqgIXZGa1_dp9YX7G1qEcHPsDSfO3h-OGm2VwfZA4lmpeqZ3zy9AF-GO1e_omhca0ZbNpZTdvkHw4z7sX8vwqa4uXmnwvpq_MAjh7ZCo9lhf0f_2cudZiIlpnWFGKE9orihQzz2F_A-ueiNWOkv6V50VSkKJ9Yqv_anx4tkj6Ba1IxpKwTU7yTgg8Y9jIUQu03tZxijoVB2qNk2MKF9SldGWrMU7YdqBbp_ng6Dk6vM7rCLocgwv2nJDbSV9w0Z85DhgDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KEapTVz_XGuBR-nGfyI8xmKca6OXPz9UX9hKNgT6p_a1LgSbBzV0R3_pCwx0Y6iSJ4ISlEnmVpI29ILjWQkg15e6opSs27w-yZggfdJ6lQeFz4CYDNBiO7P7XfL3RE7rHAsUpklsldgxDk2kLevWbpmt8LJPSZvlwnj_GfdryawfJDNPGwnc1_-S7WHvWoU_c-08xO1pmWsHuq1Iqr7veHy6u3PbVuEd461jLxf9VIcbm87CebPFqj7vtsZB77crnSTu0TqaIuzl_Ah9zrbdNr5W6gm-KlTPFYV6yHPcOyDBnB66_Uh-Qa4qOsyCK-vrWAayBUSMUVf-scXT0Q8RFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=lPT_3uKggSqWM9A2AV5QipQZkZRCz2-Q0LfdyUeL_WB_Nrxdtg79AjnEyVLjR97qQN8sAm0rtGP3NS4tTtlx3Smck3rIeJxX7eBAEC96bjAJKQ6OW7gdR0XAuiYjJZWs2a0GH-38JEsG9Dr2YP0bkzsD9OjnjmMvjBy_xWEVr-Spl0Jtob_xxlp0qO1uDmd9a1rqClmItDVPa_u8dRQ_obF_LVxA_DOvBQrBjs7fvqZIIiO-APOeE43an3DM2uqBKIPMclDqSKmlHhoLwScta-NIYW6aZ8lOwwPOqmOpnvwuq1wwj-8tCgFTrZP2NEsrzajVK-nvtE5rac6kfVW1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=lPT_3uKggSqWM9A2AV5QipQZkZRCz2-Q0LfdyUeL_WB_Nrxdtg79AjnEyVLjR97qQN8sAm0rtGP3NS4tTtlx3Smck3rIeJxX7eBAEC96bjAJKQ6OW7gdR0XAuiYjJZWs2a0GH-38JEsG9Dr2YP0bkzsD9OjnjmMvjBy_xWEVr-Spl0Jtob_xxlp0qO1uDmd9a1rqClmItDVPa_u8dRQ_obF_LVxA_DOvBQrBjs7fvqZIIiO-APOeE43an3DM2uqBKIPMclDqSKmlHhoLwScta-NIYW6aZ8lOwwPOqmOpnvwuq1wwj-8tCgFTrZP2NEsrzajVK-nvtE5rac6kfVW1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es6puZC2gQY346i_40tepMBk-YaCm_VZuCvlU-aYjgaik-vSJTAfDBJjNPu-tYSkg19KiL4RHswdy2PLk5crIZAltrWwBKRxJIIb82dHR2f9ejG9B2FVmdzlOqUV_nN0I2g_zf8zoahfDHH2veBByZGp7-L1rdkuIaYgtvP_wyYOM-Bn6q1eSlht2wR35LVy1bgQe6XbYWzG4Ny-kpDlyUnWE7aOH4UBMD9ZGaQajNkNL9po5-qwYFD5CDbmVPLl3DeHWKdbBANNKl_ycmWM7OI04LsZqMs1nrFvyRyYzQ7AwDi1qY3JT56Qmxl2s361lJLCfrSbPu7ElnsYmvEWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=Fh-4VlPCtx_1taHEYaYs-rAQJ75R82GJXwa2__IgczEgMkQRxgfm6SvEwQGM_JVyXmCOKLmRbXPD9y15g9o3KXmP2i1TbhZ3hIKj6xgCivaxAG1dxxp9JGMyNrJZ3LVDqO68rmaS4zEVam8kAvLMb5ouOtznu9YiJRkRm3sK34Q4zcMsWEiSrmHw02AoHrkqDnPuWSWZ93IrV69QoPIpM8kA0ls0yB99ISq-Nq5pA-XbNXl1msnkfi2mEKOejiLIENvxnpbgn4XW4ti1NZwxsjV9TpovgJccEkU9sWnHYFkm2heaneEZAxh9TgP1gA3lV1BsFbXhaoPUZg8Pi5lv4BxHHUHZtFFVjU0zo7jpNwe9E2U5bNzpGrryj0wSN2PUQVn5HKQccw1aTc7CCm4AF9dPp11Zs41A4DzNBRe43tkDTepx9uYwATb8aB-HBu0o-qHWCmVcF99ItLp7RzntLqop-9x8ZbVQDLIVgWKC3M_ak4wkZLQnL7KHH0gBM_iiwGhR8rR7KfI3uDoBFHWhy-KeFmWlxHf778j3dr5tOMCCgCACk-ixgyqa1XWCS72ImwLer4by-g6Te01-M-jQUehi97r9Cz51fxeg-9_jM34Fo43b7tYgs3aIG53_wpzwKbn4zNn7iQOPNK-3WTFvRqYxkVXyPeNqjV_QHZOHyH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=Fh-4VlPCtx_1taHEYaYs-rAQJ75R82GJXwa2__IgczEgMkQRxgfm6SvEwQGM_JVyXmCOKLmRbXPD9y15g9o3KXmP2i1TbhZ3hIKj6xgCivaxAG1dxxp9JGMyNrJZ3LVDqO68rmaS4zEVam8kAvLMb5ouOtznu9YiJRkRm3sK34Q4zcMsWEiSrmHw02AoHrkqDnPuWSWZ93IrV69QoPIpM8kA0ls0yB99ISq-Nq5pA-XbNXl1msnkfi2mEKOejiLIENvxnpbgn4XW4ti1NZwxsjV9TpovgJccEkU9sWnHYFkm2heaneEZAxh9TgP1gA3lV1BsFbXhaoPUZg8Pi5lv4BxHHUHZtFFVjU0zo7jpNwe9E2U5bNzpGrryj0wSN2PUQVn5HKQccw1aTc7CCm4AF9dPp11Zs41A4DzNBRe43tkDTepx9uYwATb8aB-HBu0o-qHWCmVcF99ItLp7RzntLqop-9x8ZbVQDLIVgWKC3M_ak4wkZLQnL7KHH0gBM_iiwGhR8rR7KfI3uDoBFHWhy-KeFmWlxHf778j3dr5tOMCCgCACk-ixgyqa1XWCS72ImwLer4by-g6Te01-M-jQUehi97r9Cz51fxeg-9_jM34Fo43b7tYgs3aIG53_wpzwKbn4zNn7iQOPNK-3WTFvRqYxkVXyPeNqjV_QHZOHyH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJIcMKVM8KbBJJVmA7H_rLuD4BfqzUuvPYLdGH1QePZHTw-ZN3YzAhhyVmI5AM8Zpx6I3lvANzK6yRyK3x6y_G8OXVTXhzl0nLTKLbF_msKY2xURwlmB3CBwLOozdKJ0PoNu3Gd8TBiaLp2S4ydZd-jDc5gNU40L2e8rV1ikKxtwN6fux8eUREsW8fml5UD3YCFdDHeALcSM0vgDpnVK-9OrrIYteZny1a6D96X1O_pW2bP_muxpN2W6qZm3UTFSxKPoWN8AObXPtA98Mpvc66lZ2cUPkDeGxlt_6jwyb-nWgpMF-wsj2mqZxn_8HYWjgkoVb4ZlRtvlgTqoEnqGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCO1vSi8LQDUKPQRloU62o6s6r_Gaduxzk2WSBKE_8rsKILX1LP4rxrAYL-3XpwDQ3aFNg5CtgHLeuLJ53AKNwJYSLZpn9jTitWAo9_k_NHiaa2z_eySwOnVlQIyGt139RrpE1ljqQQMxsfmO8NMw20evMKud4ze3XKkpMrw2my4EQFACw0ym6d1NuHZj8TOAyYtvp4633C168Yar3ThqWwhCrlQZh8JnkTPE9Bpp013h7i91JgUt7CKE9vhNewWjah23x9CIzoHOT9kXc7vPm1y9b4D_Ioso-naHYVB3IscX8a7W79QKStUgDFhIAM2ebSa0TiTtfRqFK8f7SLqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=JYpVOBjZiZheitEZLP3ZrHsshc0D5RoDXhHUuRMNKiPJ591-fThvgcgZ6M7YcoJZCWEIIYQo5XDHZguO0Iy-IzpaP26whdz4zRRU1QViPxH5jNruVXh2arTOeXFwNqErd3EtC5vwG2SJEpk7v8PwoJmJt-7j9h2aleGwiWNLHH_Tu8cjmDSLobpLakmDPn0XJtOw54iKexk0gQ7bf5a06Kv5uWrcr3R4icDYR5FYxkCg3mh6YmwIaDZ0f__UsDHXJDG5gk_wLwAa_TZ5FQxxBhO8ZsPROaR1exfx10sKoOSxMsJ3FDo_XT6omkJL3t0F0c8BsC2tSAydGKRi-0sJyAqYaFrtF-qwQ3C4tZbZn-_UbssYa-Hbj1QeGSPlhiviIv-KU4WqKNBzhCGkqe7ymAwgQMUAQCk6LWEgtKkouL5jgue_D5uBrRewLPuc4tejACXFLmG-XJF6R56Y3ItnA-5BwD6jPYKrWQuZSGGiqoJplS_foWFlKj8jRpr7G0UpXzcNZ_SJLjy0FtumgS12dX_Iaagxh2UQL7jWxa0bY_lMsgG90pPFb7-1EsU334lpNFx-aoBUFVDXHHug3tWxwELS0OfK2efgnzNhplp43Pwwx_Z2VsHOaNyNgNHZdmzHKPAhBUu7PJ8pnu41ATj9s81Y931K_dDeTtnffTlhndI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=JYpVOBjZiZheitEZLP3ZrHsshc0D5RoDXhHUuRMNKiPJ591-fThvgcgZ6M7YcoJZCWEIIYQo5XDHZguO0Iy-IzpaP26whdz4zRRU1QViPxH5jNruVXh2arTOeXFwNqErd3EtC5vwG2SJEpk7v8PwoJmJt-7j9h2aleGwiWNLHH_Tu8cjmDSLobpLakmDPn0XJtOw54iKexk0gQ7bf5a06Kv5uWrcr3R4icDYR5FYxkCg3mh6YmwIaDZ0f__UsDHXJDG5gk_wLwAa_TZ5FQxxBhO8ZsPROaR1exfx10sKoOSxMsJ3FDo_XT6omkJL3t0F0c8BsC2tSAydGKRi-0sJyAqYaFrtF-qwQ3C4tZbZn-_UbssYa-Hbj1QeGSPlhiviIv-KU4WqKNBzhCGkqe7ymAwgQMUAQCk6LWEgtKkouL5jgue_D5uBrRewLPuc4tejACXFLmG-XJF6R56Y3ItnA-5BwD6jPYKrWQuZSGGiqoJplS_foWFlKj8jRpr7G0UpXzcNZ_SJLjy0FtumgS12dX_Iaagxh2UQL7jWxa0bY_lMsgG90pPFb7-1EsU334lpNFx-aoBUFVDXHHug3tWxwELS0OfK2efgnzNhplp43Pwwx_Z2VsHOaNyNgNHZdmzHKPAhBUu7PJ8pnu41ATj9s81Y931K_dDeTtnffTlhndI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vElaaY9fsYflEX_WGvk4fueBMlgQ2RHefSzATK7JdnbYhbCGNJleQNqMVIY5oOYN91oaqbKjZthkaqmM-v76CeWX8xvXO4T6gwsOkszfKQPmUKQX5pVT9boIDgmKwxszwdpKY-aK9EH2i-qPVC9RDr-zR83QyejjRZ9I_yPh6JcbV6r-pA9QKJ1eiGSqEnjHitD0_2NWxhRCWOolJnmFhDl4vYUUpLQ8kTsF13c4PL5egUoJpL28Ff2i9QkCMdfGTYfQqvX_qq0lSmSU4ERB8Nev9l_PrszrMq8HKi2_EmbV0DP1jYIgbkgwGn9hvmetHbgUCdiqzqDSw3L87PImMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=cOmIlF8qAFgimzr-0qFsal8DZxVvUi_rBghJ-FnlYOTmMFCslFyRwGP0ghN4X54dScHqb5fsYjB2P12AFG74-mdCWqfUZy066MkTYfq5aMbMgQiTN2sEx4tAIL-HRT9ij-S9xKbhjZPoFCTfC6ezEYUdKNRPZIij7_6oqxHi7QfhaZOzQNnR2AllW2GaXsUt0dW6Egg9d4a9QECAmJxhc0sbrBDO_exWDjTm-Xpwz6A6yTc3UhD2FPLeo_gBgx32g3ULCdpAgEIijov9-ehwE6sd48LXjtRcS984Hv8MJQ243eiH36tMtv9n3oVq-g0YTuCgwLFL4I0c0VSOlORtyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=cOmIlF8qAFgimzr-0qFsal8DZxVvUi_rBghJ-FnlYOTmMFCslFyRwGP0ghN4X54dScHqb5fsYjB2P12AFG74-mdCWqfUZy066MkTYfq5aMbMgQiTN2sEx4tAIL-HRT9ij-S9xKbhjZPoFCTfC6ezEYUdKNRPZIij7_6oqxHi7QfhaZOzQNnR2AllW2GaXsUt0dW6Egg9d4a9QECAmJxhc0sbrBDO_exWDjTm-Xpwz6A6yTc3UhD2FPLeo_gBgx32g3ULCdpAgEIijov9-ehwE6sd48LXjtRcS984Hv8MJQ243eiH36tMtv9n3oVq-g0YTuCgwLFL4I0c0VSOlORtyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdRGeuXCFZhH2pKTK-X9tSQGATkr_RTJ3MlXiSei1oi7KXetigWNGqLpxATLyDrAbMUBSI3RC9668c9fPbB2nWD6h1z_SaufQeIX6EFvUtPEb2v4KK1p4G-DQaQWPaIoG0s_00_ZdnOA-lQ14JyXCN35sVe4tWkE9sPfrY_op0iRW0GXsJ9Fj3VG4gwunXmcZaxZDrFmGlU6bZZ9zy1teDFKYkTIGyz5hDq4_Tq8k86HmW9HtXwM4xfKYok8h6pygsCh7ggoC94j1Z_VZG23chFztHIN9y7aLp0vCwWkYyePSwCWOlfhzihffjWr2uAocLd9RoTLZWUoJoUXo1BpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUjMDp2HJMsgJjGBoM-EU1-C71eOmPYloxmdP_rUuFZQNxHGm72b0S_Nixoz_bHoKueoLfZQVmAQWxvWiP6eE0Kd7OyoO_BApsxjypmm5pFdO4_zt_nI__uBX4QvFcMHy6KSoDSGPNXe_FrOl5jehDCZUa3hugxNNaUg93GkjRWUzYAh5TbmcfP2LFeorOXxxPnzlS3HaEHiwUWmepP3PNbrMlzcD5xQ3U9EPQ_kBMAItQsqMhILab_dSRVHEwJciQkoNFEL8AM8L_eQ5rvE3bRc-XXSxEVyVFBMPdHBDXz5jgLhmQHSjtr1OKH6UU9dS3CcMrhDUOnLBueuwZtAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=kW_Y9RTOKHcR8yjhIIJ2xQU5aKOV2tK6_1QnClHXCa96TGUek7eIZaHypLJNbS0GBvYoOTdJ5oO4jEGswBm5lQ9--432Zg1qmgvamgeigoiXqH5gDxkFg4VGFi3apk5xRtG-JGia8D2UJJG0G_8Gc2Es81DPnEJsMfY8cKazAtsAc7LIB0PAXhDDW8H7ycR_j1w5Lp1lEL6TvWqhgHnkgIb1Ri640aHw_Pre7hT1gffpbEvwuI50EQDiDsO3qynz8jzdWosnhzJM8blCU4KkCJFj4QIB5z45YFEf3TBqNQP7wEu0d1-3Vk_RKgF59uDPayxACHo71UK8kg1WVJUJ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=kW_Y9RTOKHcR8yjhIIJ2xQU5aKOV2tK6_1QnClHXCa96TGUek7eIZaHypLJNbS0GBvYoOTdJ5oO4jEGswBm5lQ9--432Zg1qmgvamgeigoiXqH5gDxkFg4VGFi3apk5xRtG-JGia8D2UJJG0G_8Gc2Es81DPnEJsMfY8cKazAtsAc7LIB0PAXhDDW8H7ycR_j1w5Lp1lEL6TvWqhgHnkgIb1Ri640aHw_Pre7hT1gffpbEvwuI50EQDiDsO3qynz8jzdWosnhzJM8blCU4KkCJFj4QIB5z45YFEf3TBqNQP7wEu0d1-3Vk_RKgF59uDPayxACHo71UK8kg1WVJUJ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=cgZ7VQQUgmEmKabj6jtdNhZlepoCafafWliEJ2PFOGsrOvEax5Nqbu_oxCRujPYWcQQv5b_yGEVqYwTkq6TYFO7UeL7qCqNC2BoKWQ_L9Gv-7WIOUHhaoEnS4ea8-we2y0gqxCGqTS6Q0p7xx9J0MHsr7TZt_lSLKDwg2ZZNgC1e32hOCBKuS1hFDBRqVChDiBySvZNlMMpzAE81iKxT-kCZggGIqssj80tmRCHkvuk3DROLldLCL0IylbJJieRQkhSv1Tweyvhfk24QORzo3_R_wJMBPkqDZSsymRxc2WCIfKQbxtnL38fc8RTXeMu9KP1Fo0VMofX70F2HIimu0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=cgZ7VQQUgmEmKabj6jtdNhZlepoCafafWliEJ2PFOGsrOvEax5Nqbu_oxCRujPYWcQQv5b_yGEVqYwTkq6TYFO7UeL7qCqNC2BoKWQ_L9Gv-7WIOUHhaoEnS4ea8-we2y0gqxCGqTS6Q0p7xx9J0MHsr7TZt_lSLKDwg2ZZNgC1e32hOCBKuS1hFDBRqVChDiBySvZNlMMpzAE81iKxT-kCZggGIqssj80tmRCHkvuk3DROLldLCL0IylbJJieRQkhSv1Tweyvhfk24QORzo3_R_wJMBPkqDZSsymRxc2WCIfKQbxtnL38fc8RTXeMu9KP1Fo0VMofX70F2HIimu0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=FrWiNeN7kYTWfP5_6cstXliWVxONxrurHp10w5kYOOsImn31kwG9P-FwwoYxIy-aJUZt8t38TUUnMQ6AURmTPZ-ptej4eaVhTqBdj5pALFc-vu4VPIG_tJB38IGooKvr1f_P9vhu5OLshcpW-7H7XbQL4NOoKDImG_CJL43MTY-m3M4LK8m7wJdpFgJgsbBb7Eg-GjjqZ8sJbdOre12Ol5ab20-qwkHFR8auZgcCqzJ-owl9MjmHaGzLN4W6qkDrH_sneBddqT9LCsNz02_GT_0D8LPyabvJnqPIej232eO48_v1Tb8nraj0x2-0IMtlBrO77hetzt1vxQpw_RKt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=FrWiNeN7kYTWfP5_6cstXliWVxONxrurHp10w5kYOOsImn31kwG9P-FwwoYxIy-aJUZt8t38TUUnMQ6AURmTPZ-ptej4eaVhTqBdj5pALFc-vu4VPIG_tJB38IGooKvr1f_P9vhu5OLshcpW-7H7XbQL4NOoKDImG_CJL43MTY-m3M4LK8m7wJdpFgJgsbBb7Eg-GjjqZ8sJbdOre12Ol5ab20-qwkHFR8auZgcCqzJ-owl9MjmHaGzLN4W6qkDrH_sneBddqT9LCsNz02_GT_0D8LPyabvJnqPIej232eO48_v1Tb8nraj0x2-0IMtlBrO77hetzt1vxQpw_RKt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF0cFIm96uMd4LvARcsTJ-Va5XdbsXYIBwsIzbbLSSIi4lnvbsgmGtjGMperCyyPFXneWVHJc_okbIIhA1h3lXcWl5vp5E8LYk5Ps-E4J5RJF0RHH3XYA1NiBza0tpjXDPQzrybOxe0xmzijGdlQxi451bE2HL05Pbb8vwT92kegFwMoSsNqWNP8XMiKO2yyKa17bHt_ttDMOUfTeGhHHtK-EYGpWo7CesXINe5buMs8hexSTX49euGgrFtKLgKWCR4Dvul8VCgXLt4Y-0ib1tzm7v8bHSVJD5nxf9DRrV_E_YuOaIHHf5OOrizXZBRDz8AU_TKoPBhBLMo1NFXUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=b_uBZuhpvWq1OMdke6MeKhJjYpmzKIS1I6-9qk_niySnyhdkJzYkm7kk_S5d8H_mZnNRl_bUWtXqKzPk0hmu8wqP1uG69Px5NKHKWnAU6XiRCtMxP0H34LVosTndKYHj4El_BeENOOe5W0LH-U9QJF2dxLuhygYZh8908gGerirIarlZ5BaEt0tUmUipXozMpz-LDpiG66V3YpvLuOi34OD2CZpDU3Ej15FlIREe-7Pr9CWCG4QwW9PO9ePFzri9RhfeuzkAiSARd-1Bp_YSo7P1GSYqcRFz9mZLAvdXof1Y_fweRrgYtNP7kNwjJ-NeeapFn0qfdpYKgMp4POQk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=b_uBZuhpvWq1OMdke6MeKhJjYpmzKIS1I6-9qk_niySnyhdkJzYkm7kk_S5d8H_mZnNRl_bUWtXqKzPk0hmu8wqP1uG69Px5NKHKWnAU6XiRCtMxP0H34LVosTndKYHj4El_BeENOOe5W0LH-U9QJF2dxLuhygYZh8908gGerirIarlZ5BaEt0tUmUipXozMpz-LDpiG66V3YpvLuOi34OD2CZpDU3Ej15FlIREe-7Pr9CWCG4QwW9PO9ePFzri9RhfeuzkAiSARd-1Bp_YSo7P1GSYqcRFz9mZLAvdXof1Y_fweRrgYtNP7kNwjJ-NeeapFn0qfdpYKgMp4POQk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=N_yO1MLnCkkWMtY89bbd56O1KQ0rYTBJ9b7Nv-YtwH9eV5WxSD30PKk7kRCyEb2SLQB00D399Q2Jc0ZpbZ-hcoKrHwDC7zyQFHp-J0iVC4IssYBUm2T-bHcr3Q9uxQyBR-Kg5Z7s-gTfZq4m9qtiMEIKHtb4xH33bv_k2BXUGGYqVo-bJfL6CgMX5WC7jza7T0XJjmSkdtoH989ao1Wc6uLKLQ4Hefa6vLH4J3Be7fTo3YIEzCwDOWepUWD56FdCVFdAYg6OeWkYakId9klj9Uqad4nfbJzDlqhv2sWVL_Hekrcl7mUR25hnPheM3jvZKzvrbA5k1JmRQKX6JcU6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=N_yO1MLnCkkWMtY89bbd56O1KQ0rYTBJ9b7Nv-YtwH9eV5WxSD30PKk7kRCyEb2SLQB00D399Q2Jc0ZpbZ-hcoKrHwDC7zyQFHp-J0iVC4IssYBUm2T-bHcr3Q9uxQyBR-Kg5Z7s-gTfZq4m9qtiMEIKHtb4xH33bv_k2BXUGGYqVo-bJfL6CgMX5WC7jza7T0XJjmSkdtoH989ao1Wc6uLKLQ4Hefa6vLH4J3Be7fTo3YIEzCwDOWepUWD56FdCVFdAYg6OeWkYakId9klj9Uqad4nfbJzDlqhv2sWVL_Hekrcl7mUR25hnPheM3jvZKzvrbA5k1JmRQKX6JcU6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXqGNjj9vyyt9aqktKXKCG0uaWHEy8lpi5eLDz0LaY64o9rqJucGZhe_NjR7UCoXHU_laWgEdByjPUBSCs1fuFXLJrsbjsQw196OMV2-jNQbc9iOZG-1LDtnOhS4yUtmfVK6mg_dhr5qetGgqf6lsOZiZm2UYxn0Voz4rE2sA6CmYRy92sMbqIynOvIT23FX5NwqkDcSAVyLUvZkRsO_5yerleJRdpL1c3PWh9lb3SY5m8CEcvdvP_XH7YFOL1UYayhbUX59NUgqbKxzwOp-z2Ek2YWWl-9bwQXnkVEWIRztJvDPVwPYamtuhpmHPnbZ2zNg_Egl-Jd4oVQ6rGo9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DjzYXDVOg5k955a-Fy5irj8TuISxsFRbyir3valG_HSpjB7aqTJEF31hSviCHE1u-Rt9xJIHHvqVUvL6uM1kEF8jIKbZeaAkcvIql9UkehdxUG8d6HIiY6JGhauHN24wjeW34RuOMxWNRK94t1esarBVB3njsdOH2VBRInFgHh47nb9cTcUPOg6aIC8htdJzd7V0ifIr5lF0EGE2EIH6cH6Wy_58s6kj3SEJPe38DgY9aYVcoArQyvGz9OFzUyxELWiQoCzTZhl0MRLvVTsArfBqZA2uPupgnVjmbUa39P92QQtAdkaDlPyRGkg2RAvHkI51iGgiJFErQx7bhU-gQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DjzYXDVOg5k955a-Fy5irj8TuISxsFRbyir3valG_HSpjB7aqTJEF31hSviCHE1u-Rt9xJIHHvqVUvL6uM1kEF8jIKbZeaAkcvIql9UkehdxUG8d6HIiY6JGhauHN24wjeW34RuOMxWNRK94t1esarBVB3njsdOH2VBRInFgHh47nb9cTcUPOg6aIC8htdJzd7V0ifIr5lF0EGE2EIH6cH6Wy_58s6kj3SEJPe38DgY9aYVcoArQyvGz9OFzUyxELWiQoCzTZhl0MRLvVTsArfBqZA2uPupgnVjmbUa39P92QQtAdkaDlPyRGkg2RAvHkI51iGgiJFErQx7bhU-gQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LJpDtGjSp7hn8b8lLi2qaTTw8ktuQml5XMasg4mTPvJyY52OxfacTrYit6_c0_KkW_nZ1HiBY-E6BKnxSr2n5phYyKX3by1DxfsBc54pIAIhJ_xoTowJr4Bt7Vf_j1iCIRklVXIEr7c8cHnLx4FpoSkuJegeXWDSfplzQV9LEa0IRiKlpDAmIpszWG2vnLuwUDEk5nAynYeZdF0-xLdp88sOlGAZEj91yjC2X0jinbgPY5Csd6MNZ2TgJTkkk7ntB1iAnmAbk088aZ-dxwtfXlCmMIhdpV9ClGGVEN3ADgHdSSsvdggLR1Z3RaTJBgTCyU1cgsVW9Ff82Es_heyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ohoy9i87nTgDsiAUcJcqsCA2PIWaM4H6_GJYEhEzcjm5sMDY6phyNQUxbTBMiB9Q_TsbTQ-MTFn-nD5Fb_J7TXT2cHzclvf7nXON3YUaE6Gm6ofvULDmn_lzwCwOWVcTu0XB8vf0VFypr__j_cirw_12GWVnK_CHc1fBIc9DOrpCV6YLc41OV4eXghF3XqfiYw4GbJAaqZuoQpJBS3kGIG8JlfMybe1cVzSgfqXcivbsDSnqC-Euc0Rk3s18rBmlJrYtCzdDSDY1KIcOyKMn1V9gB7zVWWCHSUW_OKv1ebTlxC21UBZIYeeVbswSjXXeiSL4cF_S-HXfPgHKskBamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WggbVWBxmZSZKP0DRfIPpyfD4Ta2PdhTUtZdc_7GQ_fEqadpbbgpB6X1R2XbFL7nLjXxMZXrV8kGfjxpNZNhPEGoXKtievJTqwAZDHo2uGkzXpsncgCnuWdaC5lH7gnDoltvJJ6XOrFJG7KigWCNHikJpynkE6gHTvNLmSoJWoLUU_Ni3QQ_FmELIsRqZqZxeiJGPyaWZd-wkff_bI-bRmHVUrHcl34NXQT0X43XDXW31HvEGfF6mnN6JKXG-xyoBtdFa8jS6rhzfbJhVFuZyGGQFkPTmsmb9UFXklNPqJVL2OywOfjGr1y68sjUFECQIujf4qo1qId2J3w1-iYGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kpjqBSdDKXGQDcq9blffzheGXm_L0K1ebZq1qYQylGvsBpHZgpBAdGCjAjukw9rNhyjeNNoJpPe4NKvhxMZsI2EJVDX8RN8QjaVktnhHRhzN6lVgD4RZ7Dy_c5zq4LcJqzJUqqMv83ADX7hy_NkQ2bwcvtydRKweW8EKkQ39I3rsOEUrxs38PcXNJ8UVoRgOKpvPlPrib7KMOJnSiEr9P61iluLvbBJ4DstvVbFkGYJSjZeoThv5DnKCbHhUFpBQNqg3p6a06FU7DpZGcMUKcqa-TR7WHhf1xnKXohXOz8oqNseSi7V66eAmLW_F-up2Ri6LnQCZe0-hkJjYfzqTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dGSSpYc-mpCDo7Lf7DvtJ63jGe5L3Y26d_tNdWBRMOzHda5Ckr-zbJWbE6Quixsn_bBHVVpFu2jFsEsdWRN2_DLhoyu9UQWMlEO4J6q-PCaYOYhCjB636UkOVJtM9l6z2T4VoAioRy4-H5EwL8RkkqVeFJ_tlnAznevuvnfBugzBNm5RtxJLlmQdQb955DKtBBb2S0Vm4FpFT944ucbwIcOyu-LYI6YWPk3WqdTBLDKBQY3T8etyZlNDK8wx8Y_wRCKbKyfKa4XvZaLaNSmEAz1fTR7yL9wuipiVGcFnFrFe7t3HfVH4Wcsdaune6MZHYkGzTyDo2H3T7mhUUO8shw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3vFaQ_N8mpj51NMuAf3S_zQe2iu4nM-xBe1-xftxCAkvmMp3KZ71MVa3qAPVC9ABojyJrrFtcAjy5XFazvsbFIqAW3I6MMRgzf3vDqeKnAUfvLH9vg-qgD48PvcPUECtcBJtlYb1dXZpjHLbDXPZqENAk5XfGNaRdiJQuWtipZydLzP-ZoXn7cEfmT37_I0Ub3EtwGoCN3peMaJDF3vtX0PSFOrMFde0Jxlha_a1xEZd5klruofVQxJcXCYC_Xze2FNL5NvyLFW-HY85lvV4skM2t6kscA7Qa6yTfcsQ3J0vCaHYwZSiKDN9_R92jD93UxmnxfA5_v0bci77rciHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4WcFkeGyZrp_WyRAo_d-gPbpQNYnQbPgjg1rGEwm9OO4Kv1-HOZ17eol4jIyt0xtnuBEQZpujDxpUCOMb12o4nlypplDh7bF84TE_VJqcjUzdoKkRTp1cyf5_w8I7bwVf4REOKqjtSF1fDB_OdDNizUTLLIM0JG9UYA_oAO509DR_OgIULjJWmJItlZZwWGb08YAk2wR4AR7rBCvpIj9aFKo-cXbTFaksLwz6706W6Oz5J3EWN0kj5Eb0rxzvdn9OC5ZqFCnL99fct8JT0A_duH_J5qYjLS-pSq1uC2yR6i2WF4M2SNgaSsjRTQML2Xx5FG2gH_crtJvyZq0o6qdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMhl9GCHtuJNGsKzYY6tgJawcf7gawv0Z7lqj1AcoFLNOPPxumgIH-UtYudX26Yqvb9Q8Q3Qc_LCW71AJWU9NL9qbCsFHuQRM4mlv3hgJVddla0TeBYKbb0qMJXEKLHadg7UwGLFpXkMPlNKPEE3f7uQPbdTCvTTp6VvznOpQlqaYs_W0OtRxLRjnQiQVXGy1tfjSByqnr22CNqpFstq5__t2S5XFb5nZI9cxJqz4Uvt0hO4OVDdT-B0q-eT9Cg-Z9Qu0sBJbyn8VQq-i9fij5O_zOJcaU8fD7Q5FEX3XKakYzR5jHpi-WG8OA7GkDPI_Tvhk0ynxWylcVY7lkxC-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=IiCRYOzZZWxory2ZboezkDIjfANTqzHYWblZtT_isg59Um6ctkg0iK4nE5x7Xjfub4hDyp4BMAqBb48OSvIVR2uRZU8L4puqSUGPgTZl1cQfBttPdWKZlehsGj8TyVxVoGGbE2w53BECi_33nzrCQ6YSdoPlOIwJlHrq7_0z4dMjYHsPpWP7pm856RUwmNvSr3FAeTwhF3jqKhP1wPrR5Hbq9uZRFP7-h0q0zU5Zxus7XTjSkVnhWwEfhLe58dpCyQJpD-W6-twUDmO4hFIIoJ8El7kIntflAjZ8X0v63yoMlmKIWqG2q2L1IYYyQ93h4d1Zwxt-yYXurU2YT51Cpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=IiCRYOzZZWxory2ZboezkDIjfANTqzHYWblZtT_isg59Um6ctkg0iK4nE5x7Xjfub4hDyp4BMAqBb48OSvIVR2uRZU8L4puqSUGPgTZl1cQfBttPdWKZlehsGj8TyVxVoGGbE2w53BECi_33nzrCQ6YSdoPlOIwJlHrq7_0z4dMjYHsPpWP7pm856RUwmNvSr3FAeTwhF3jqKhP1wPrR5Hbq9uZRFP7-h0q0zU5Zxus7XTjSkVnhWwEfhLe58dpCyQJpD-W6-twUDmO4hFIIoJ8El7kIntflAjZ8X0v63yoMlmKIWqG2q2L1IYYyQ93h4d1Zwxt-yYXurU2YT51Cpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
