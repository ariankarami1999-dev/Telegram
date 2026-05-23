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
<img src="https://cdn4.telesco.pe/file/hvC8Dg3oFDDEddDwRSRBS8PRHchMccPHKAhbZc_l92V0DIjhOg5W0H_hyhzVoepUg70eC5FBwII6iN2xZnVRLyYWgY3nRJsHUtSMqkmX7AL8Xnmu2Au8SkdWHoQ-nKzti2VhngaPMRpnF-yriIUOw2Z7Cg9B_x9X6zHEGP_mJJyoHeBiVNX2HhOLeW96ye9WJfmXepmWjuqYAnghwIsEZp47fpQTnII6qoimHJITycgk8UUrl9e2q_che6PDZKfwsSuHKlvK7ToHBW77bsArLd_iDCuRNcjLX-g8R7PxqqKeC-AG9PWJDuOdWKZDfP6rPt_nxl6EbsxunUHTB7n7YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.93K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 15:25:22</div>
<hr>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kba9ydnLX_qgyby_cLGl48Hb5fFMRuF1RRvvlmA6IwD-7RxEcTAA5YUF8HlaaSq8bS7ncbV9XcSg9G_CU4Z2EBnwd2BzJ4_3yA6SU02pddn-8KXGBXdKW6ZmFj2hb4IA9-DKZGI4cdKlu6t7RVdvy33oBV52GlLTbQin1nQcNHdqOvZuHhPzUZ4--AjXxNA80KkIDiDPLuzreDoN7jZmeCUK1iqeyyfHwyMQVGneuN3m7POBnW5B1d_jFd_g-VpEkkrpNH8xSBWrCdeOra6835tahxkXjdMYYQkaKjSS4kaB8qtxFX20Kw554zFsjmwlRKHUE8o1bxqkr5_MUvZfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://play2go.cloud https://aeza.net مقایسه پلن های پلی 2 گو و آئزا</div>
<div class="tg-footer">👁️ 734 · <a href="https://t.me/archivetell/5310" target="_blank">📅 14:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxwUacU9jze6svHCkDXhWtEADIM63GKKk4qusMCpOetbcDbIV6xCnyHRw3WwJKDrlUp0me5sRQtSAUzTV8nwUqmyO1ytsb3ASXvZAi9wWbZNDwLEMS3YjjcfoxouPdee2QzoEjknvDafDABd0IvN1p1gqoVNH0sAbUMhLMu_Q7U18JD2_Q5RGbXgcrxxkdzG66HtEUro3YjcdstuwfSH_RA9aHMKNRg5KpkuTbLhdsM5zfqr0uZ1TcnnGJRII4znRsLesPH-xxTnqvvIOua1zCNKrDhEEMEcfomgtrbVAzOmdtFjeL3wfAMAPn1ztYrGvnWaFpfx1AVJOdKNkxqeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/archivetell/5309" target="_blank">📅 14:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4TtoWRyrSTz4yn1Y213SLw0KUfMPTSPsvAEH7X9s44gN39s1dcGWk3gqJckvGOLv0vsQloHXwl2yP3tuOw7lsUbpYxO-Jx7LNIjzLb7FBMO66GWVGMvW_eskaVVHYKJ5vqlhUdhY3y3qfKxciJYfqqFzf5LkZ4QUcK8oMIB18IhdIdH8ccgrmEgXXxPrzxU4jIqEY6MXIifbOIZLIj4ziqX1IqAOcH6Znt3QHi58PK4VaWipqQ_tFybi6wTRnTYg2L0qwQ9bKCy3HY_7i4DQAbfpq3Veme2-k7peXwzjcDHFPqIQqHbUeQMN8OIELW8fZgpv8T0HMKXYj0Ghd6YIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/5308" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ربات هوش مصنوعی Claude رایگان
@bs_cluade_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/5307" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">2.17.35.217
2.17.35.40
2.17.35.24
2.17.100.234
2.17.97.137
2.17.106.118
2.17.35.163
2.17.106.137
2.16.53.57
2.16.53.65
شیر و خورشید ایرانسل ، همراه اول و سامانتل
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/5306" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تا یه مدت پیش همینا نمیدونستن متد دی ان اس چیه
😁</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5305" target="_blank">📅 12:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBreak The Barriers</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqWAKHzgj2mPMiH9bI9gxnFGlQddVjsfGRQXz06MRGawPLylYlRkvniGOUZ1gAwHCGSG38KzVDKo2Ryxb8v9AmNGavJH3SiC9qVk9EVVeJZ8EZ1nLzmT9WxsQLQwUUeRziDSVoxbeBceztuJ-NPclNeS7zrQyoMlaAHnpg6RQ668ICbdh66KTBIzIDTbzn7hFEpXSy3TiYhi5scxiD3YLXQhwZ2Sx1ZLSzVlxoLhKDGFFWd6qYyhiSyGWi5gH3f81N0cHGKgSrpl57W4zXwTl0J3hm7VMshxPVHusWCi19vtLWqhZLm0sQmTRjGPRZ73HUfAo67kgI1Dld6mBCNh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که هیچ هزینه‌ای نداده و فقط متد بقیه رو منتشر می‌کنه، به کسی که صدها دلار برای اینترنت رایگان مردم هزینه کرده میگه «احمق»، «مزخرف» و «پولکی».
در این حدود ٣ ماه قطعی من حدود ٣٠٠ دلار هزینه بابت سرورهام دادم.
سرور و اتصال رایگان، با توییت و فحش تأمین مالی نمیشه.
بعضیا فقط بلدن حرف بزنن، نه اینکه بار واقعی چیزی رو به دوش بکشن.</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/5304" target="_blank">📅 12:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خیلیا این چند روز تو دایرکت کانال پیام دادن که اپراتورا خیلی بیشتر از حجم مصرفی از بسته اینترنت کم میکنن..  هیچ جوره جلوی دسترسی مردم رو نمیتونید بگیرید ، اینقدر زور نزنید
😁</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5303" target="_blank">📅 12:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خیلیا این چند روز تو دایرکت کانال پیام دادن که اپراتورا خیلی بیشتر از حجم مصرفی از بسته اینترنت کم میکنن..
هیچ جوره جلوی دسترسی مردم رو نمیتونید بگیرید ، اینقدر زور نزنید
😁</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5302" target="_blank">📅 11:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyKmvs-erv-srXV_L_RcF4HTuNMrQ6Gat0rg6yBj6iI-pV6Le0yU1CosmQiGrQ7nKDSegcufF2F0YZ5_lHDPskm-Xva4Tn2AnIJ6mXBgBf_d74B0t0kjqI5VoUmYlOXMZGs1iIbR9hmXJoc3Ari3vI0MdiJCR-rXJpa1B2fiuXSnOkxqfFBHQbJk3TbOMYzHaaVMG2olJqlszg8lasIJMe6dEWJ8DWZbYBU-rCwYl9a1oW36QZk7fl7-0q2YP_myWQEOD0ZB0FGQw6QVSF-gZOQwb9DmETaY10bWAhwazGsJSgRk7rByy2sNJyLx4fCtY1uMpWkQH-Dy_GBoQnnrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpST4S-_cCOIUilDeCYvMt33s4NutCWmLtVIz5zhaQnyQckhVrqPfwws1oIljwupROyLPTlych4_8PV4ApTgsMhjzB3nkkTRWFxN8bujX-D7HsjRjvaNJdvhy7DlxbgDfGS5JRVIR-iK1f6G2D-CfNpbPiTpNAPZISH3pVspT2pfr2VSaRLrU0jdIQOFYwfmV4ItBvB1JJ37DcxFUz1aRAGTnJ5ycFYJmiGTqa2uCNJdVFwTQr0UCKHG5QbB19vgx6-Z_oKKBP0jdb83VEdTCfrC1gY_nIgW7TTgqaXA2lvX6DHAcsAW-OJNPF-9NUwylRtwe8RFU6s9m8Ovdnts5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه میخواین ترافیک از جایی کم رد و بدل بشه اینجا برین
تو اندروید های بالای ۱۳ هست این اپشن
مثلا نتلیفای که بن نشه
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5300" target="_blank">📅 11:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">46.38.137.156 81.12.32.136 تو sni spoof با hcaptcha.com بزنید جفتشون کار میدن</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5299" target="_blank">📅 11:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
46.38.137.156
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
chat.deepseek.com
"
}</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5298" target="_blank">📅 11:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانفیگ اسپوف
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#%DB%B1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.latonyamadeline.ndjp.net&path=%2F%3Fhttps%3A%2F%2Ft.me%2FProxyVPN11%F0%9F%87%A8%F0%9F%87%B3%3D&security=tls&sni=sni.latonyamadeline.ndjp.net&type=ws#%DB%B2
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B3
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#%DB%B4
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B5
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B7
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#%DB%B8
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B9
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B1%DB%B0</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5297" target="_blank">📅 10:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مخابرات | sni spoofing    hcaptcha.com  46.38.137.156</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5296" target="_blank">📅 10:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مخابرات | sni spoofing
hcaptcha.com
46.38.137.156</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5295" target="_blank">📅 10:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">46.38.137.156
81.12.32.136
تو sni spoof با
hcaptcha.com
بزنید جفتشون کار میدن</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5294" target="_blank">📅 10:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">2.19.126.205
23.216.77.172
2.16.6.219
23.213.161.104
23.48.23.162
23.222.250.244
184.25.52.67
95.101.111.141
2.22.89.33
2.16.55.15
95.101.137.74
2.20.168.195
23.218.225.17
23.48.23.171
96.16.122.153
23.3.89.123
2.16.220.194
95.101.171.159
2.21.2.65
23.11.206.114
2.22.151.183
95.101.29.12
2.21.240.145
2.16.245.170
95.101.29.23
95.101.137.201
23.44.203.191
23.48.23.194
2.22.31.99
96.16.53.156
2.19.126.92
23.216.77.70
2.16.245.177
2.16.55.45
23.3.89.97
2.20.168.16
23.218.225.41
2.16.154.104
2.19.198.75
23.44.203.205
88.221.169.185
185.200.232.8
2.22.89.195
96.16.86.206
185.200.232.65
23.48.224.82
23.219.36.112
2.16.6.206
23.55.244.243
2.18.20.57
23.42.205.29
104.111.202.22
شیر و خورشید شاتل ، پارس آنلاین ، سامانتل و ایرانسل
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5293" target="_blank">📅 09:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ربات ویرایش mp3 و پیام صوتی
@mp3_Service_Bot
🎤
تبدیل تِرَک ها به صدا
🏷
ویرایش برچسب‌ها (عنوان، هنرمند)
🖼
افزودن کاور
🔊
صدای 8D
🎚
مسترینگ (تمیز، بلند، صدای استودیو)
🪄
افکت‌های بیس و ریورب
🔄
تبدیل به MP3، WAV، FLAC، OGG، AAC
📦
پردازش دسته‌ای چندین فایل
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5292" target="_blank">📅 09:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آیدی عددی رو بفرسید این ربات و اطلاعاتش در بیارید
@fustating_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5291" target="_blank">📅 09:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیدا کردن افراد با آیدی عددی با این فرمت :
tg://openmessage?user_id=
بعد از = آیدی عددی بذارید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5290" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سامانتل شیر و خورشید سرعت فضایی
CDN edge IPs :
184.24.77.42
184.25.28.31
184.28.165.4
184.51.252.4
184.86.251.12
184.86.251.27
184.25.52.200
184.28.230.87
184.30.150.142
184.51.252.36
184.51.252.38
185.200.232.40
185.200.232.41
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.50
184.51.252.152
184.51.252.157
184.86.103.210
184.51.252.135
CDN SNI hostname:
snapp.ir
Beast Mode : روشن
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5289" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رایتل شیر و خورشید
142.54.178.211
5.144.129.174
80.191.243.226
2.16.53.50
79.175.169.59
95.38.201.199
5.160.13.85
2.23.170.80
193.148.67.117
2.16.53.11
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5288" target="_blank">📅 08:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همراه اول شیر و خورشید
184.86.251.27
184.51.252.36
185.200.232.50
کلاینت اندروید
کلاینت ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5287" target="_blank">📅 08:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=bCHvfYx3w6kV6wOKN9NfMuS3i4LDHRRHTZ_ltDaCzddYXS03UJnhPjMTE0r7Qo06QN5xA6AEOi0gFy_Zs4d2hJ5JmrqpS-r6SsNtskfWnboKJDcE7QXcjwWp3yYCSBR-QmBniXQU_WQidfID7XYpZjjSQVx-suyubHOVnIMCA2XEWOL2Rh-SnYEaScVJi0hYcUQkofEeDgpDW8u8kwZYCMx3yR1s5t-cdRPI7qLQfCZwZUMjdkOns1gkoE2fCrKjbNWRv1EYSIch9OEKTABcucWJ41F3TQDAwdU-zJyE9tMj-euMpVVfa1GyhYlsdiDQfhFs8DgY8s9mQZfpsWk_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=bCHvfYx3w6kV6wOKN9NfMuS3i4LDHRRHTZ_ltDaCzddYXS03UJnhPjMTE0r7Qo06QN5xA6AEOi0gFy_Zs4d2hJ5JmrqpS-r6SsNtskfWnboKJDcE7QXcjwWp3yYCSBR-QmBniXQU_WQidfID7XYpZjjSQVx-suyubHOVnIMCA2XEWOL2Rh-SnYEaScVJi0hYcUQkofEeDgpDW8u8kwZYCMx3yR1s5t-cdRPI7qLQfCZwZUMjdkOns1gkoE2fCrKjbNWRv1EYSIch9OEKTABcucWJ41F3TQDAwdU-zJyE9tMj-euMpVVfa1GyhYlsdiDQfhFs8DgY8s9mQZfpsWk_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5285" target="_blank">📅 02:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b443b9a9.mp4?token=hasHcmfuTqkZXlYgGRfXMkdR-s0WF3neYoi68ykmio7EWxOWnsMpQZDVH0rfV1CP4mPwjoWvNw4L5xR3j3RAMOTxlBVWAJcJeQkFxKJiub7Eo8YdMHn6VuQ-0qbuOPk1aQ_oExgaEsra1Zf-HGYJXzISQ6bEmC4yqWiwVt5UPWG2Moonn4mdWzwe4rMsEghgMXkeuajSyxt18lj_btGCKaP1Nl12cnp4klu4X_KzXKSvXfhS9cZXKY9LFCcPXoMFqVMuyhfHPV_LyVk7OmZ-r596NDAKDSYNVqsKyFv3V9z1U2Qm8h8jrjUswQVnZsWPvZpqhVtrP9NT--AUJYL-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b443b9a9.mp4?token=hasHcmfuTqkZXlYgGRfXMkdR-s0WF3neYoi68ykmio7EWxOWnsMpQZDVH0rfV1CP4mPwjoWvNw4L5xR3j3RAMOTxlBVWAJcJeQkFxKJiub7Eo8YdMHn6VuQ-0qbuOPk1aQ_oExgaEsra1Zf-HGYJXzISQ6bEmC4yqWiwVt5UPWG2Moonn4mdWzwe4rMsEghgMXkeuajSyxt18lj_btGCKaP1Nl12cnp4klu4X_KzXKSvXfhS9cZXKY9LFCcPXoMFqVMuyhfHPV_LyVk7OmZ-r596NDAKDSYNVqsKyFv3V9z1U2Qm8h8jrjUswQVnZsWPvZpqhVtrP9NT--AUJYL-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5284" target="_blank">📅 02:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSWA6Uw3vawH1hyk--wUkmgjK3em820Bla_E_vNInecUEg9fCo-KF9LJiakllWMH4K9uwWlMlURu1n8ztRS9ZQwRXsc2XgEirFRpLKxQ6e6z8r6dW3eFeiNraWCB1zw7Uj92OUqylaxrq_eM7IXTeR8m5VBegNpyU1cysDrazAPKKD8e_BNiEelQIH0fj1-qm_L6lPBT8CXRdDzEn0QIXR5UTr1ObS-wWccEa_xY9wFzN4p5L_fEFhB079u1-jPhqGowWnxORtuwrucuDhrNGIdmTkvNASTCp4HE7R76lV7sxbzuT5NaHVW6zZSXyIEgtYBhBGnhkalScTYv6-0BWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
در مورد سرور (VPS) برای پروژه‌ها  ---  رفقا شب بخیر!
✋
خیلی‌ها توی دایرکت می‌پرسیدید برای راه‌اندازی پروژه‌هایی مثل GooseRelayVPN یا متودهای تونلینگِ جدید، الان چه سروری بگیریم که هم قیمت‌اش معقول باشه و هم موقع کار اذیت نکنه؟  راستش من خودم این مدت پلن‌های…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5283" target="_blank">📅 23:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
معرفی GooseRelayVPN: کلاینت اختصاصی و قدرتمند اندروید برای متد رله گوگل  ---  اگر از متدهای رله‌ی گوگل (مثل MasterHttpRelayVPN یا مشابه اون) استفاده می‌کنید و دنبال یک اپلیکیشن اندرویدی هستید که هم ظاهرِ تمیز و مدرنی داشته باشه و هم مدیریتِ کانکشن‌ها رو…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5282" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
معرفی GooseRelayVPN: کلاینت اختصاصی و قدرتمند اندروید برای متد رله گوگل
---
اگر از متدهای رله‌ی گوگل (مثل MasterHttpRelayVPN یا مشابه اون) استفاده می‌کنید و دنبال یک اپلیکیشن اندرویدی هستید که هم ظاهرِ تمیز و مدرنی داشته باشه و هم مدیریتِ کانکشن‌ها رو براتون به صورت خودکار (VPN Service) انجام بده،
GooseRelayVPN
دقیقاً همون چیزیه که نیاز دارید.
💡
چرا باید از GooseRelayVPN استفاده کنیم؟
بزرگترین مشکلِ کار با این متدها روی اندروید، محدودیت‌های مرورگر و نیاز به تنظیماتِ دستیِ پروکسی بود. این اپلیکیشن با استفاده از قابلیت
VpnService
سیستم‌عامل اندروید، تمامِ ترافیکِ گوشی (یا اپلیکیشن‌های انتخابی شما) رو به صورت خودکار از تونلِ رمزنگاری‌شده‌ی گوگل عبور میده.
✨
ویژگی‌های کلیدی این کلاینت:
🔸
پشتیبانی از VPN Service:
نیازی به تنظیم پروکسی در مرورگر نیست؛ کلِ گوشی یا اپ‌های منتخب شما به صورت VPN متصل میشن.
🔸
داشبورد حرفه‌ای:
مانیتورینگِ زنده وضعیت اتصال، پینگ و لاگ‌های سیستمی برای عیب‌یابی سریع.
🔸
پشتیبانی از پروتکل‌های هسته‌ی GooseRelay:
این اپلیکیشن از هسته‌ی بهینه شده‌ی این پروژه استفاده می‌کنه که پایداری بسیار بالایی روی اینترنتِ محدود داره.
🔸
مدیریت پروفایل‌ها:
می‌تونید چندین کانفیگ مختلف رو وارد کنید و به راحتی بین اون‌ها سوییچ کنید.
🔸
وارد/خروجی گرفتن با فرمت JSON:
مدیریت کانفیگ‌ها بسیار راحته و می‌تونید اون‌ها رو بین گوشی‌های مختلف جابجا کنید.
---
🛠
چطور راه اندازی کنیم؟
۱.
پیش‌نیاز سرور:
ابتدا باید هسته‌ی اصلی (GooseRelay) روی سرور لینوکسی شما نصب باشه و Deployment ID و کلید امنیتی (Tunnel Key) رو داشته باشید.
۲.
تنظیم اپلیکیشن:
- فایل APK رو نصب کنید.
- یک پروفایل جدید بسازید.
- مقادیر
script_keys
(لینک‌های دیپلوی شده) و
tunnel_key
رو دقیقاً مشابه سرورتون وارد کنید.
۳.
اتصال:
بعد از ذخیره، روی پروفایل ضربه بزنید تا VPN فعال بشه. (در اولین اجرا، اندروید اجازه دسترسی به VPN رو می‌خواد که باید تأیید کنید).
📥
لینک گیت‌هاب و دانلود:
🔗
https://github.com/Hidden-Node/GooseRelayVPN-AndroidClient
📌
نکته فنی:
اگر موقع اتصال، وضعیت روی "Preparing" گیر کرد، حتماً بخش
Logs
توی خودِ اپلیکیشن رو چک کنید. اونجا دقیقاً بهتون میگه مشکل از کجاست (مثلاً اشتباه وارد کردنِ Tunnel Key).
📌
#معرفی_ابزار
#فیلترشکن
#اندروید
#گوگل_رله
#نت_ملی
#GooseRelayVPN
#VPN
#Android
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5281" target="_blank">📅 22:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW3IZrXXowXw6QbwlYgQfFeZ8-hI8ATc3vka3qXOCdqOtLjc1KLr21Yb7ozIgo5MVnc6tgzG4xmPYYZOWa_jKiYaGch46_9DxcGBGqtQo8uGTw-IHxrCP6TozABJhYQOCxfgCHuapEUM7Xw7PdU0Kaq5ItBx-12KRycAHKrJaXnrqnbwzcKAOBnMtigfjNP6xe_d4wN2ODYGZ0JPMJehgDS8trWjTo1xzDWMCF2urlZwTWCOOqoauV-3xvDkeIJqZVoCaclWUNSgMfDdpPlDyrsCabZAEviOqfpwr0ii-iuNIWHjvoLWjXnMzQSqdfdFlQozkBd5GLW-HNd3hfd4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
FileShare یه ابزار ساده برای اشتراک‌گذاری فایل توی شبکه محلیه.
با این برنامه می‌تونی فایل‌ها رو روی سیستم خودت آپلود کنی و از یه دستگاه دیگه داخل همون شبکه، خیلی راحت دانلودشون کنی.
✅
کارش اینه:
- فایل را می‌فرستی داخل ابزار
- برنامه فایل را ذخیره می‌کند
- لینک دانلود و لیست فایل‌ها روی دستگاه‌های دیگر هم در دسترس است
✨
این ابزار کار را برای انتقال فایل بین دو دستگاه خیلی راحت‌تر می‌کند، چون نیازی به فلش، کابل یا نرم‌افزار جانبی نداری.
🔐
درباره فایروال:
اگر دو دستگاه داخل یک شبکه باشند، معمولاً کافی است پورت برنامه باز باشد. در بعضی سیستم‌ها ممکن است فایروال دسترسی را ببندد، پس اگر اتصال برقرار نشد فقط باید اجازه دسترسی به برنامه یا پورت 8887 را بدهی؛ معمولاً لازم نیست فایروال را کامل خاموش کنی.
لینک دانلود داخلی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5280" target="_blank">📅 21:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">exventa.io
پلتفرم مدرن برای ارزهای دیجیتال که از هوش مصنوعی برای ارائه استراتژی‌های معاملاتی استفاده میکنه
- قابلیت‌ها: مشاهده زنده عملکرد، مدیریت امن موجودی و ربات‌های خودکار برای کاربران بی تجربه.
- هدف: ساده‌سازی معامله برای کاربران عادی و ارائه ابزارهای پیشرفته بدون نیاز به دانش فنی.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5279" target="_blank">📅 21:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لینک داخلی آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5278" target="_blank">📅 20:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">scannerv2.zip</div>
  <div class="tg-doc-extra">12.4 KB</div>
</div>
<a href="https://t.me/archivetell/5277" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
معرفی نسخه جدید CDN IP Scanner  نسخه جدید CDN IP Scanner منتشر شد؛ یک ابزار سبک، سریع و کاربردی برای اسکن IP، CIDR و لیست‌های CDN با امکانات حرفه‌ای‌تر و backend پایدارتر.
✅
قابلیت‌های ورودی:  * IP تکی * لیست چندخطی IP * CIDR * رنج IP * فایل txt شامل IP…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5277" target="_blank">📅 20:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی  (مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5276" target="_blank">📅 19:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5274" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی
(مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از زیرساخت داخلی دوم
(مدت زمان یک روز)
📱
گیت‌هاب پروژه اسکیرک
💳
حمایت مالی از من
🗣
اینترنت برای همه، یا هیچ‌کس!
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/5273" target="_blank">📅 19:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سامانتل شیر و خورشید سرعت فضایی
CDN edge IPs :
184.24.77.42
184.25.28.31
184.28.165.4
184.51.252.4
184.86.251.12
184.86.251.27
184.25.52.200
184.28.230.87
184.30.150.142
184.51.252.36
184.51.252.38
185.200.232.40
185.200.232.41
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.50
184.51.252.152
184.51.252.157
184.86.103.210
184.51.252.135
CDN SNI hostname:
snapp.ir
Beast Mode : روشن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5272" target="_blank">📅 19:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">78.157.41.60
5.160.13.85
5.160.128.142
37.191.95.70
80.191.243.226
185.200.232.42
sni:
google.com
شیر و خورشید همراه اول
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5271" target="_blank">📅 19:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">23.205.184.9
23.57.90.161
2.23.168.213
23.44.203.211
23.47.27.234
2.23.168.174
104.90.16.63
23.62.54.76
23.203.134.233
104.83.197.135
شیر و خورشید همراه اول
sni:
google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5270" target="_blank">📅 19:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Se7en pro | شیر و خورشید ویندوز
لینک داخلی دانلود
لینک  گیتهاب
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5269" target="_blank">📅 19:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">لینک داخلی شیر و خورشید اندروید
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5268" target="_blank">📅 19:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e93f3bf8.mp4?token=mDgfLTlyz_HcCNznnRTA4ccyobd035f50XuHXpcXOMumWqMwsKTvDJlidtvvzMrMXO2boVdA2VlXmIhOXlLsharYHXDLexx9wB2oNNRv8aFTvB779remXAqmvjqzkjUjfmveXqv_doirnJG7SkUKDn2BtQ_sySZZeoXCj6uXOYCg9Yup6AQSVAF4lf12M_mjc2UUyRG-P3lpXrrmwPXrSKixj9KY4-utb3C8-NhZCCE_EO-xemueOYyvDVIbar8UJMkhs2ENPZmrlOvvqsMk4qPpfthTrS_GgbNGLsGTbpKdSYBOFJkS-HH109oYbGnU-HBvGYu8WO1_sWpfax4E9jrkT9pgxSGBZu8U2TLwlbvIW22aSvU5xxl2frW_w1BlUurN4tVJ6nq_O4R3nsKkZCeB1kOBDQ0a1ruImsoL_qiReQT1NDNKr_LJO7s0fa5v88ojBjG9U4OyNyeA7VRWGjOQRNRxoLsdrD6kAGC1aU4PZE8-JJeCVGq2Fhbi-j1UklLhg4Ka6VsvTs82EH4bMar8Dh8F9M9SPA1Ftu7_8JGE-iUVtaUe-MYif07W201hXEb2ZHkeCaxnxue-RwJb7JXg4qhlSdxBQKHUBBktColdPL67o223XxpSbDJMt2ni8kgXHakBGjAtOYsd_NbKt42N2zexSXiWbeXKIrxIZnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e93f3bf8.mp4?token=mDgfLTlyz_HcCNznnRTA4ccyobd035f50XuHXpcXOMumWqMwsKTvDJlidtvvzMrMXO2boVdA2VlXmIhOXlLsharYHXDLexx9wB2oNNRv8aFTvB779remXAqmvjqzkjUjfmveXqv_doirnJG7SkUKDn2BtQ_sySZZeoXCj6uXOYCg9Yup6AQSVAF4lf12M_mjc2UUyRG-P3lpXrrmwPXrSKixj9KY4-utb3C8-NhZCCE_EO-xemueOYyvDVIbar8UJMkhs2ENPZmrlOvvqsMk4qPpfthTrS_GgbNGLsGTbpKdSYBOFJkS-HH109oYbGnU-HBvGYu8WO1_sWpfax4E9jrkT9pgxSGBZu8U2TLwlbvIW22aSvU5xxl2frW_w1BlUurN4tVJ6nq_O4R3nsKkZCeB1kOBDQ0a1ruImsoL_qiReQT1NDNKr_LJO7s0fa5v88ojBjG9U4OyNyeA7VRWGjOQRNRxoLsdrD6kAGC1aU4PZE8-JJeCVGq2Fhbi-j1UklLhg4Ka6VsvTs82EH4bMar8Dh8F9M9SPA1Ftu7_8JGE-iUVtaUe-MYif07W201hXEb2ZHkeCaxnxue-RwJb7JXg4qhlSdxBQKHUBBktColdPL67o223XxpSbDJMt2ni8kgXHakBGjAtOYsd_NbKt42N2zexSXiWbeXKIrxIZnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش استفاده از اسکنر در ترموکس موبایل با چند کلیک بسیار ساده
لینک داخلی آموزش
Pass :
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5267" target="_blank">📅 19:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">CDN IP Scanner.zip</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5266" target="_blank">📅 19:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN IP Scanner.zip</div>
  <div class="tg-doc-extra">12.4 KB</div>
</div>
<a href="https://t.me/archivetell/5265" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">باعشق
🫶🏻
بازم توسعه بدیم یا نه؟</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5265" target="_blank">📅 19:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آپدیت آپلودر های فعال بدون نیاز به ثبت نام
https://up.zaringo.sbs/
https://rozup.ir/
https://uploadgirl.ir/
https://seup.shop/
http://uplod.ir
https://up.20script.ir
https://punkpaste.ir
https://my.files.ir
https://toolschi.com/tools/upload-center
http://nixfile.com
https://guardts.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5264" target="_blank">📅 17:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آپدیت سایت های فیلم و سریال بدون سانسور و رایگان
https://www.my-f2mx.top/
ravinaz.top
F2mc.top
http://Paradoxmoviz.com
http://F2mede.top
https://www.simindad.top/
https://www.sorkhcloud.top/
Movieyaab.ir
f2mux.top
www.myf2mi.top
F2my.top
http://oldtowns.top
https://dls6.iran-onemovies-dcenter.com/DonyayeSerial/10_thous.html
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5263" target="_blank">📅 17:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🛠
V2RayN: پادشاهِ کلاینت‌های دسکتاپ برای مدیریت اتصالات
---
رفقا سلام!
✋
اگر با کانفیگ‌های V2Ray، Xray یا sing-box کار می‌کنید، حتماً می‌دونید که مدیریت اون‌ها توی محیط ویندوز یا دسکتاپ بدون یک «کلاینت گرافیکی» چقدر می‌تونه سخت باشه. برنامه
V2RayN
(پروژه‌ی 2dust) دقیقاً همون چیزیه که هر کاربر دسکتاپ باید روی سیستمش داشته باشه.
چرا V2RayN ضروریه؟
این برنامه در واقع یک رابط گرافیکی (GUI) هست که به شما اجازه میده هسته‌های قدرتمند شبکه (مثل Xray و sing-box) رو به راحتی کنترل کنید. شما کانفیگ‌ها رو به برنامه می‌دید و اون تبدیل به یک «پروکسی محلی» (Local Proxy) می‌شه تا تمام ترافیک سیستمتون رو امن و مدیریت‌شده عبور بده.
✨
ویژگی‌های کلیدی V2RayN:
🔸
پشتیبانی از هسته‌های قدرتمند:
به راحتی از Xray و sing-box پشتیبانی می‌کنه و اجازه میده بین اون‌ها سوییچ کنید.
🔸
کنترل کامل روی روتینگ:
می‌تونید تعیین کنید چه ترافیکی از پروکسی رد بشه و چه ترافیکی مستقیم (Direct) بره تا آی‌پی سایت‌های ایرانی فاش نشه.
🔸
تست سلامت (Latency Test):
می‌تونید پینگِ تک‌تک سرورهاتون رو چک کنید تا بفهمید کدومشون سریع‌تره.
🔸
چند پلتفرمی:
علاوه بر ویندوز، نسخه‌های لینوکس و مک هم داره تا روی هر سیستمی تجربه یکسانی داشته باشید.
🔸
اپن‌سورس و امن:
چون کدهای برنامه در دسترس هست، با خیال راحت می‌تونید ازش استفاده کنید.
💡
نکته برای حرفه‌ای‌ها:
اگر می‌خواید از تمامی امکاناتِ هسته‌های جدید (مثل قابلیت‌های خاصِ sing-box) استفاده کنید، همیشه این کلاینت رو آپدیت نگه دارید. این برنامه به تنهایی حکمِ «آچار فرانسه» رو برای هر کاربرِ شبکه‌ای داره.
---
📥
لینک‌های دسترسی و دانلود:
🌐
صفحه گیت‌هاب پروژه (لینک اصلی):
🔗
https://github.com/2dust/v2rayN
📥
آخرین نسخه‌های منتشر شده:
🔗
https://github.com/2dust/v2rayN/releases
📚
ویکی آموزشی (برای یادگیری تنظیمات پیشرفته):
🔗
https://github.com/2dust/v2rayN/wiki
---
📌
#معرفی_ابزار
#V2RayN
#دسکتاپ
#ویندوز
#لینوکس
#مک
#Xray
#singbox
#فیلترشکن
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5262" target="_blank">📅 15:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سامانتل شیر و خورشید سرعت فضایی
CDN edge IPs :
184.24.77.42
184.25.28.31
184.28.165.4
184.51.252.4
184.86.251.12
184.86.251.27
184.25.52.200
184.28.230.87
184.30.150.142
184.51.252.36
184.51.252.38
185.200.232.40
185.200.232.41
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.50
184.51.252.152
184.51.252.157
184.86.103.210
184.51.252.135
CDN SNI hostname:
snapp.ir
Beast Mode : روشن
لینک داخلی شیر و خورشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5261" target="_blank">📅 13:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از جستجو برای یک تولیدکننده ویدئوی هوش مصنوعی پریمیوم که واقعاً رایگان باشد خسته شده‌اید؟ امروز بهترین هدیه را برای شما دارم!
🚀
فقط روی این لینک جادویی کلیک کنید:
https://openart.ai/credit/YT%20Affiliate
با حساب گوگل خود وارد شوید، روی Claim بزنید و بوم... 20000 اعتبار رایگان مستقیماً به حساب شما واریز می‌شود! و نگران نباشید، هیچ‌کس اینجا کارت اعتباری یا جزئیات صورتحساب شما را نمی‌خواهد. کاملاً رایگان و امن است.
😎
می‌توانید از این اعتبار عظیم برای اجرای مدل‌های قدرتمندی مثل Seedance 2.0 Pro، Veo 3، Kling و Wan استفاده کنید. ویدئوهای سینمایی با کیفیت بالا و صدا تولید کنید یا تصاویر خیره‌کننده بسازید.
✨
آپدیت : تموم شد
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5260" target="_blank">📅 11:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
جستجو تصاویر Pinterest به صورت درون‌خطی
📌
نحوه استفاده:
• هر چتی را باز کنید
• تایپ کنید
@PinGalleryBot
کلمه کلیدی شما
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5259" target="_blank">📅 11:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رضایت ممبر به این نحو
😐
😂
🎁
کد تخفیف تمدید شد عزیزان:  archivetell  @ArchiveTellbot  --- حجم سفارش بالاست صبوری کنین</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5258" target="_blank">📅 01:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبشکن Beshkan</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PsiphonAndroid-GA-469b.apk</div>
  <div class="tg-doc-extra">24.6 MB</div>
</div>
<a href="https://t.me/archivetell/5257" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه بروزرسانی شده و جدید
سایفون
ویژه اندروید
👍
✍
Beshkan</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5257" target="_blank">📅 23:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
معرفی پروژه Zyrln: عبور از سد فیلترینگ با ترافیک ابری گوگل (آپدیت 1.6.0)  ---  رفقا امشب قصد داریم ابزاری رو معرفی کنیم که با استفاده از دو تکنیک متفاوت، فیلترینگ رو به طور کامل دور می‌زنه و ترافیک شما رو پشت سرورهای گوگل مخفی می‌کنه.  برخلاف فیلترشکن‌های…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5256" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
معرفی پروژه Zyrln: عبور از سد فیلترینگ با ترافیک ابری گوگل (آپدیت 1.6.0)
---
رفقا امشب قصد داریم ابزاری رو معرفی کنیم که با استفاده از دو تکنیک متفاوت، فیلترینگ رو به طور کامل دور می‌زنه و ترافیک شما رو پشت سرورهای گوگل مخفی می‌کنه.
برخلاف فیلترشکن‌های معمولی، Zyrln نیازی به سرورهایی نداره که مرتباً فیلتر بشن. این ابزار دو حالت کاربری داره:
1️⃣
حالت اول: دسترسی سریع به سرویس‌های گوگل (بدون نیاز به هیچ سروری!)
اگر فقط می‌خواید تحریم یا فیلترِ سرویس‌هایی مثل Gmail، Google Drive، Maps، Firebase یا Google Docs رو دور بزنید، نیازی به هیچ سروری ندارید.
Zyrln با تکنیک «قطعه‌قطعه کردن دست‌دهی TLS» (TLS Fragmentation)، کاری می‌کنه که سیستم فیلترینگ (DPI) نتونه آدرس سایت رو بخونه و در نتیجه بدون نیاز به رله یا کانفیگ، سایت‌های گوگل براتون با بالاترین سرعت باز می‌شن.
2️⃣
حالت دوم: دسترسی به همه‌چیز (اینستاگرام، یوتیوب، تلگرام و...)
برای باز کردن کل اینترنت، ترافیک شما وارد اسکریپت‌های رایگان گوگل (Google Apps Script) میشه. سیستم فیلترینگ فقط می‌بینه که شما در حال تبادل دیتا با خودِ گوگل هستید. سپس گوگل ترافیک رو به یک «گره خروجی» (Cloudflare Worker رایگان یا VPS خودتون) می‌فرسته و سایت واقعی رو براتون لود می‌کنه.
✨
تغییرات کلیدی در آپدیت جدید v1.6.0:
🔸
مسیریابی هوشمند (ایران مستقیم):
حالا سایت‌های ایرانی (دامنه‌های .ir) به طور خودکار بدون نیاز به رله باز می‌شن تا سهمیه گوگل اسکریپتِ شما هدر نره.
🔸
بهبود در آپلودهای سنگین:
پایداری در آپلود فایل‌های حجیم به طرز چشمگیری بهتر شده.
🔸
سیستم Failover هوشمند:
اگر چند لینک Apps Script به برنامه بدید، کلاینت فقط از یکی استفاده می‌کنه و درخواست‌ها رو تکراری نمی‌فرسته، اما به محض از کار افتادنش، سریعاً سوییچ می‌کنه روی اسکریپت بعدی.
🔸
رفع باگ‌ها در نسخه اندروید:
مشکل کرش کردن در زمان جابجایی بین حالت‌های Direct و Proxy برطرف شده و رابط کاربری بسیار روان‌تر عمل می‌کنه.
🛠
شروع به کار و راه‌اندازی (مرحله‌به‌مرحله):
راهنمای کاملاً فارسی و روان برای راه‌اندازی دسکتاپ و اندروید در صفحه گیت‌هاب پروژه قرار داده شده.
📥
لینک دانلود مستقیم نسخه‌های دسکتاپ و اندروید:
🔗
https://github.com/ajavadinezhad/zyrln/releases/tag/v1.6.0
آموزش و توضیحات فارسی پروژه:
🔗
https://github.com/ajavadinezhad/zyrln/blob/main/README_FA.md
📌
#معرفی_ابزار
#گوگل_رله
#نت_ملی
#فیلترشکن
#اندروید
#ویندوز
#Zyrln
#Bypass
#Cloudflare
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5255" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🗂
فهرست جامع ابزارها و متدهای اتصال (آرشیو و دسترسی سریع)
---
رفقا سلام!
✋
برای اینکه بتونید خیلی راحت روشِ مناسب خودتون رو پیدا کنید، تمام ابزارها و متدهایی که تا الان تو کانال معرفی کردیم رو بر اساس نوع کاربردشون دسته‌بندی و هشتگ‌گذاری کردیم.
کافیه روی هشتگ اختصاصیِ هر ابزار کلیک کنید تا به پست آموزش و دانلودش هدایت بشید:
☁️
بخش اول: متدهای مبتنی بر گوگل و دامین‌فرانتینگ (کلاد)
این روش‌ها ترافیک شما رو پشت سرورهای ابری (مثل گوگل، ورسل و نتلیفای) مخفی می‌کنن.
🔸
MHRV (نسخه اختصاصی پایتون):
اتصال از طریق رله گوگل با مسیریابی هوشمند، پنل مدیریت ترافیک و فایل اجرایی تک‌فایل (exe). ➔
#MHRV
#Python
🔸
mhrv-rs:
نسخه فوق‌سریع و بهینه‌شده‌ی رله گوگل با زبان Rust (پشتیبانی از مک، لینوکس، ویندوز و اندروید). ➔
#mhrv_rs
#Rust
🔸
NovaProxy:
پروکسی حرفه‌ای دسکتاپ با ترکیب Google Apps Script و Cloudflare Worker. ➔
#نوا_پروکسی
#NovaProxy
🔸
XHTTP-Installer:
اسکریپت ساخت تونل VLESS روی CDNهای Vercel و Netlify (مخصوص سرور). ➔
#XHTTP
#ورسل
#نتلیفای
🎭
بخش دوم: متد SNI Spoofing (تزریق دامنه فیک)
این متدها با ارسال یک پکت فیک به سیستم فیلترینگ، مسیر رو برای دیتای اصلی شما باز می‌کنن.
🔸
Cloak:
کلاینت گرافیکی، ساده و بی‌نظیر برای مدیریت SNI Spoofing روی مک و ویندوز. ➔
#Cloak
🔸
FakeSNI:
ابزار تخصصی و حرفه‌ای تزریق SNI فیک نوشته شده با زبان Go (مخصوص لینوکس). ➔
#FakeSNI
🔸
دامنه مستقیم hCaptcha:
اخبار و کانفیگ‌های مربوط به استفاده از hCaptcha برای اسنیفینگ. ➔
#hCaptcha
#SNI_Spoofing
🔍
بخش سوم: اسکنرها و ابزارهای جستجوی آی‌پی (IP Scanners)
برای پیدا کردن آی‌پی‌های تمیز جهت استفاده در متدهای بالا و برنامه‌های مختلف.
🔸
CDN IP Scanner (تحت وب):
اسکنر بی‌نظیر مرورگر بدون نیاز به نصب هیچ برنامه‌ای. ➔
#اسکنر
#CDN
🔸
Network Checker:
اپلیکیشن اندرویدی همه‌کاره با قابلیت اسکن آکامای و ساخت کانفیگ. ➔
#نتورک_چکر
#Network_Checker
📡
بخش چهارم: دسترسی‌های آفلاین و مبتنی بر فید
ابزارهایی برای مواقع قطعی شدید و خواندن محتوا بدون نیاز به اتصال مستقیم.
🔸
چشم عقاب (Eagle Eye):
دریافت اخبار و کانفیگ فیلترشکن از طریق اسکن بارکدِ شبکه‌های ماهواره‌ای. ➔
#چشم_عقاب
#ماهواره
🔸
TheFeed:
فیدخوان آفلاینِ پرسرعت با قابلیت Query Sharing (برای iOS، اندروید، ویندوز، مک و لینوکس). ➔
#TheFeed
🔸
EzyTel (نسخه بهینه‌شده):
اسکریپت خواندن آفلاین کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت. ➔
#ایزی_تل
#EzyTel
📱
بخش پنجم: کلاینت‌های اتصال (Clients)
برنامه‌های پایه‌ای برای وارد کردن کانفیگ‌ها.
🔸
v2rayNG:
آپدیت‌ها و معرفی قابلیت‌های جدیدِ محبوب‌ترین کلاینت اندروید (نسخه‌های 2.1.7 و 2.1.8). ➔
#v2rayNG
#آپدیت
---
💡
نکته:
برای دسترسی به آموزش هر بخش، روی هشتگ‌های آبی‌رنگِ روبروی آن کلیک کنید.
📌
#فهرست
#دسترسی_سریع
#آموزش
#فیلترشکن
#نت_ملی
#آرشیو
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5254" target="_blank">📅 23:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb86e0d73.mp4?token=cZw5oXsofP9ppXEM84sP5kN8qLse73YBeQ6y33yWXj24zhl86uEtM8bPHnw8KY_qnzjQ6wGZ-ND-rioXMK25p-3pGwMVV_J0_beQ1bgCubbBbEcKNZKZhX015_GBuj50AHKekTOuNmm1aDqr2H0i1iC-8pfbRXVfmcWH8FOyR2M9GvpkLHI7Sn6h5J4Di4VSGT3pxb-09XeUZb5DgvKBFZ7FlOFL8qEp4xv6AYTn1eWDJR6zg5tLgaVsM1lh4CXMLfcMwQ9AWALDJx_4TTURGUlHy4uent8HIaJ23fKExGLWgFVRSpUsQZXMfdU4WQB2O_YTBxWVmDSWhpGIqgb5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb86e0d73.mp4?token=cZw5oXsofP9ppXEM84sP5kN8qLse73YBeQ6y33yWXj24zhl86uEtM8bPHnw8KY_qnzjQ6wGZ-ND-rioXMK25p-3pGwMVV_J0_beQ1bgCubbBbEcKNZKZhX015_GBuj50AHKekTOuNmm1aDqr2H0i1iC-8pfbRXVfmcWH8FOyR2M9GvpkLHI7Sn6h5J4Di4VSGT3pxb-09XeUZb5DgvKBFZ7FlOFL8qEp4xv6AYTn1eWDJR6zg5tLgaVsM1lh4CXMLfcMwQ9AWALDJx_4TTURGUlHy4uent8HIaJ23fKExGLWgFVRSpUsQZXMfdU4WQB2O_YTBxWVmDSWhpGIqgb5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت ممبر به این نحو
😐
😂
🎁
کد تخفیف تمدید شد عزیزان:
archivetell
@ArchiveTellbot
---
حجم سفارش بالاست صبوری کنین</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5253" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عصر بخیر دوستان   تصمیم گرفتیم برای ۲۵ نفر اولی که دنبال اتصال پایدار هستن تخفیف ۱۰ درصدی در نظر بگیریم
❤️
تضمینی
✅
پایدار
✅
1GB: 200,000
➡️
1GB: 180,000  2GB: 400,000
➡️
2GB: 360,000  3GB: 600,000
➡️
3GB: 540,000  4GB: 800,000
➡️
4GB: 720,000  5GB: 1,000…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5252" target="_blank">📅 18:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتمام کد تخفیف
❤️
🙏
مبارکه دوستانی که خریدن</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5251" target="_blank">📅 17:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عصر بخیر دوستان
تصمیم گرفتیم برای ۲۵ نفر اولی که دنبال اتصال پایدار هستن تخفیف ۱۰ درصدی در نظر بگیریم
❤️
تضمینی
✅
پایدار
✅
1GB: 200,000
➡️
1GB: 180,000
2GB: 400,000
➡️
2GB: 360,000
3GB: 600,000
➡️
3GB: 540,000
4GB: 800,000
➡️
4GB: 720,000
5GB: 1,000,000
➡️
5GB: 900,000
این کد
فقط تا ۳۰ دقیقه
اعتبار دارد.
🎁
کد تخفیف:
archivetelloff
🛒
ورود به ربات جهت تهیه کانفیگ پایدار
⚡
:
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5250" target="_blank">📅 17:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عصر بالا باشین
😁
تخفیف داریم تایم محدود
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5249" target="_blank">📅 15:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Samantel@ArchiveTell.txt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/archivetell/5248" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی سامانتل شیر و خورشید</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5248" target="_blank">📅 15:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Se7enPro_Setup.exe</div>
  <div class="tg-doc-extra">76.7 MB</div>
</div>
<a href="https://t.me/archivetell/5247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⬇️
لینک دانلود داخلی
⬇️
لینک گیت هاب</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5247" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔰
اتصال به اینترنت بین الملل با نسخه کاستوم شده سایفون (اختصاصی)
💢
قابلیت های برنامه:
◾️
اضافه شدن قابلیت Beast Mode
◾️
اضافه شدن پروتکل CDN Fronting
◾️
اضافه شدن قابلیت تانل کردن کل سیستم
◾️
اسکنر IP داخلی برنامه + لیست رنج های مورد نیاز
◾️
پشتیبانی از پروکسی های Socks 5/4 در بخش Upstream
◾️
امکان تغییر پورت پروکسی ها (به صورت پیشفرض رندوم هستن)
⬇️
لینک های دانلود:
●
لینک دانلود داخلی برنامه Se7enPro
●
لینک دانلود داخلی آموزش استفاده از برنامه
●
لینک گیت هاب پروژه
⚠️
اتصال اولیه به خاطر لود سرور ها کمی طول میکشه. برای اتصال با پروتکل CDN Fronting ریجن رو روی Auto بزارید و تغییر ندید که به سرور مناسب متصل بشه. هر آیپی که در برنامه شیر و خورشید اندروید براتون متصل میشه روی این نسخه ویندوزی هم اوکی هست.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/archivetell/5246" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیسلایک میزنه
واقعاکه</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5245" target="_blank">📅 14:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واقعا حیف این‌چنل نیست زیر 10 کاست؟</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5244" target="_blank">📅 14:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5243" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">mhrv with panel.zip</div>
  <div class="tg-doc-extra">68.5 KB</div>
</div>
<a href="https://t.me/archivetell/5242" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5242" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTNOvWNUYXyqQnNZ1iMEOPottLzTRcJvPn0YrxvNms-XrWZUS4mnMLe6lKe7JS5Y-VXd1RbT2E7gAaZbiNZvI7Flmup4ChkZKmKCqEhAA_BM523tOZ1ogof46yUkc3ftLNsIwfgZGqqd5tzHtLWIdy13iR5yxVzWCrHeSYkzsD-1_zHE5v8soTT14aS1oQFXF_inydisZ8t6nwpomGICl1etcVTYRHESqPNdv5XfEuk_tzpt0RPpMUFBgRomNawGSE0ZVTvCpt40rgXji0pXcgejvHs-4K7MTzh7bt-B_Ft1n160P5qqdxuC44BD1N3ewh1iFVnT0SvvvMqE2Ucr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
توضیحات تکمیلی درباره عملکرد این نسخه توسعه‌یافته: https://t.me/archivetell/5242  برای دوستانی که پرسیده بودن این نسخه دقیقاً چه فرقی کرده و چرا سرعتش بالاتره، تغییرات رو به زبان ساده اینجا باز می‌کنیم:  ۱. سیستم مسیریابی هوشمند (جلوگیری از هدر رفتن سهمیه):…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5241" target="_blank">📅 14:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💡
توضیحات تکمیلی درباره عملکرد این نسخه توسعه‌یافته:
https://t.me/archivetell/5242
برای دوستانی که پرسیده بودن این نسخه دقیقاً چه فرقی کرده و چرا سرعتش بالاتره، تغییرات رو به زبان ساده اینجا باز می‌کنیم:
۱. سیستم مسیریابی هوشمند (جلوگیری از هدر رفتن سهمیه):
در حالت عادی، ابزار MHRV تمام ترافیک شما (حتی سایت‌هایی که فیلتر نیستند) رو می‌فرسته سمت اسکریپتِ گوگل. این کار هم سرعت رو کم می‌کنه و هم سهمیه ۲۰ هزارتایی روزانه شما رو هدر میده.
اما در این نسخه توسعه‌یافته، یک سیستم هوشمند پیاده‌سازی شده؛ به این شکل که اگر سایت‌هایی مثل خود اسکریپت‌های گوگل، گوگل درایو، گیت‌هاب و ورسل روی اینترنتِ فعلی شما باز (وایت‌لیست) باشن، برنامه اصلاً اون‌ها رو سمت رله نمی‌فرسته و مستقیماً بازشون می‌کنه. نتیجه؟ سرعت به شدت بالا میره و سهمیه شما سیو می‌شه!
۲. پنل کنترل ترافیک:
یک داشبورد مدیریت ترافیک به برنامه اضافه شده. با این پنل می‌تونید دقیقاً ببینید چقدر دیتا داره رد و بدل می‌شه و کنترل کامل‌تری روی مصرف اینترنتتون داشته باشید (مثلاً می‌تونید ترافیک‌های سنگین و پس‌زمینه رو مدیریت کنید).
۳. افزایش سازگاری با سایت‌ها:
کدهای مربوط به ارسال درخواست‌ها بهینه‌سازی شدن تا سایت‌های سنگین و وب‌اپلیکیشن‌ها (مثل تلگرام وب یا سایت‌های هوش مصنوعی) خیلی روان‌تر، با خطای کمتر و سازگاری بیشتر باز بشن.
این نسخه با کلی بی‌خوابی و تست‌های مداوم بهینه‌سازی شده تا پایدارترین تجربه رو روی نت ملی داشته باشید. حتماً تستش کنید!
✌️</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5240" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5239" target="_blank">📅 11:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صداهای ElevenLabs نامحدود و رایگان
صداهای زیاد دیگه‌ای مثل مایکروسافت ، هوش مصنوعی گوگل و موارد دیگه هم داره
https://teamsp.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5238" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxL-dtVjaEakkcgAjn-2W5UBtml3XfNSpxb_MWJMF-ATe-VEV-vx8okEaJTYYmXsVGFr8NJLAuQRPmWaBcUW9tVzdg00-EqQVwNWC1rFuxAPNGDLij4LLClWT7D7rfClQ6tYZ_EsyIhcGbGtVusnhOyS16QrGr71wiosDBUJCb8IAolZw0hi-gChniGepegLglLnrnFXTAtP_ZuQKnTLCPF71C5JzO08uHctDvyIUvNTLsL8Xwp3zarJDc0WPZNPEFdGNMsuLjTV4d4990EcY0AkPyTL4p-SA-BIRat0Sx1jPnOQzr2XT8FploMtDJ_yIgI38WwF9_-RxhE5thwQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت هوشمندانه ‌تر کردن متن بدون اینکه شبیه به متن تولید شده توسط هوش مصنوعی به نظر برسد
Rewrite the text below so it sounds clearer, sharper, and more p
Improve the structure, remove weak wording, and make the message more confident without changing the original meaning.
Text: [paste here]
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5237" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خواندن پست‌ها و نظرات Threads در تلگرام
@threadsreaderbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5236" target="_blank">📅 08:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دانلود مدل های هوش مصنوعی از سرور ایران
Bitgraph.ir/iran-ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5235" target="_blank">📅 08:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جدا الان وقتشه کانفرینگ تنظیم بازار بیاد قیمتا بشکنه
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5234" target="_blank">📅 01:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📘
معرفی پروژه GateRelay
یک reverse relay سبک و حرفه‌ای با Go است که هدف اصلی آن تانل کردن لینک ساب پنل با یک http proxy است و نمی‌خواهید حتی یک درخواست غیرمجاز از proxy عبور کند.
با GateRelay می‌توانید یک دامنه داخلی/قابل‌دسترسی مثل:
https://example1.com/sub/...
را به یک upstream خارجی مثل:
https://example2.com/sub/...
وصل کنید؛ اما فقط بعد از اینکه درخواست از نظر دامنه، مسیر و متد کاملاً تأیید شد.
ویژگی‌ها:
• نوشته‌شده با Go
• پشتیبانی از authenticated HTTP proxy
• جلوگیری از open proxy شدن
• فیلتر سختگیرانه قبل از مصرف proxy
📱
GitHub:
https://github.com/YrustPd/GateRelay
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/archivetell/5232" target="_blank">📅 22:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=YwsQFSDqh1F2xOUOJGzkL5JZuqhwchLHOfNU3jWbxBOZv81vIrg0MrmQB5HgQMGMbrSL6wlijoR0nPUBVP1keRn-ImcH8NcrgcRODZpXJhvp7hgV3ZhikdXrhNPRnSNpT600KqnsMswpNc5Cba9KOEyTmgg5jDAiKms-2Kmc6z2cwrys-TTfGTQIiAfM-POlAVQsdtREOzqPDWth83sRHW_2saoJLJ9PRM88abWaJG30X-b0CHVWKc9kQkBujmq1zoaQfghoAvfvpaX_1DmuGB-S4604aGVcfvRvEbGhLLLY6Afd5FdOcyo_SYgTnZoXamsZ-5ZAsY25WywvJODh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=YwsQFSDqh1F2xOUOJGzkL5JZuqhwchLHOfNU3jWbxBOZv81vIrg0MrmQB5HgQMGMbrSL6wlijoR0nPUBVP1keRn-ImcH8NcrgcRODZpXJhvp7hgV3ZhikdXrhNPRnSNpT600KqnsMswpNc5Cba9KOEyTmgg5jDAiKms-2Kmc6z2cwrys-TTfGTQIiAfM-POlAVQsdtREOzqPDWth83sRHW_2saoJLJ9PRM88abWaJG30X-b0CHVWKc9kQkBujmq1zoaQfghoAvfvpaX_1DmuGB-S4604aGVcfvRvEbGhLLLY6Afd5FdOcyo_SYgTnZoXamsZ-5ZAsY25WywvJODh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5231" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5230" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آموزش بازی های انلاین با پینگ خوب برروی ویندوز با استفاده از روش SNI Spoofing
موارد مورد نیاز:
اتصال به Sni Spoofing
v2rayng
نرم افزار Windscribe که از قبل توش اکانت داشتید حتی اکانت فری و از قبل بهش لاگین کردید .(الان نمیشه بهش لاگین کرد اگه کسی روشی داره بگه بهمون )
شروع:
فرض بر این میگیریم شما با sni وصل هستید به اینترنت ازاد
روی v2ray پروکسی رو بذارید روی Clear system proxy و اصلا نباید حالت TUN روشن باشه .
حالا باید توی تنظمیات وایندسکرایب این تنظیمات رو اعمال کنید :
1-در بخش CONECTION روی split tunneling بزنید و بذارید روی Exclusive و در بخش app همون صفحه روی دکمه + بزنید و برنامه SNI SPOOFING رو پیدا کنید و اضافه ش کنید و مطمین بشید تیکش سبز باشه .
2-برگردید به بخش CONECTION و در قسمت Proxy setting و در بخش پروکسی تغییرش بدید به HTTP و ادرس و پورت زیر رو بذارید
127.0.0.1
10808
3-دوباره برگردید به بخش connection و Firewall رو بذارید روی حالت Manual
4- بخش conncetion Mode رو بذارید روی حالت manual و پروتوکل TCP و پورت 443
دقت کنید فقط پروتوکل TCP رو میتونید با این روش بهش وصل بشید و پینگ خوبی بهتون میده اگه اینترنت نرمالی داشته باشید .
سرور هم میتونید از المان فرانکفورت یا فرانسه جاردین استفاده کنید.
با این روش اینترنت شما مستقیم از وایندسکرایب گرفته میشه که هم اینترنت تمیزی بهتون میده که همه سایت ها و اپلیکیشن ها باز میشن هم پینگ خوبی بهتون میده.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/archivetell/5229" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">sni spoofing
وصله
امنه ، راحت استفاده کنید ، به حرف اونا که میگن مشکل داره و ... گوش نکنید ، واسه سود خودشون اینارو میگن</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5227" target="_blank">📅 21:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده
لینک داخلی v2ray ویندوز
https://seup.shop/f/zp9bi</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/archivetell/5226" target="_blank">📅 21:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5224" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">IP,SNI
185.141.106.238
,
a77.net.akamai.net
185.88.178.196
,
a184.net.akamai.net
185.141.106.238
,
ak.net.akamaized.net
185.50.37.52
,
a77.net.akamai.net
185.141.106.238
,
ds-aksb.akamaized.net
185.50.37.52
,
a104.net.akamai.net
185.88.178.196
,
ds-aksb.akamaized.net
185.141.106.238
,
a104.net.akamai.net
185.88.178.196
,
a77.net.akamai.net
185.50.37.52
,
a184.net.akamai.net
185.137.25.214
,
a248.e.akamai.net
185.88.178.196
,
a104.net.akamai.net
185.141.106.238
,
a184.net.akamai.net
185.88.178.196
,
a248.e.akamai.net
164.138.17.122
,
a184.net.akamai.net
185.88.178.196
,
ak.net.akamaized.net
185.50.37.52
,
ds-aksb.akamaized.net
185.137.25.214
,
a184.net.akamai.net
185.137.25.214
,
a104.net.akamai.net
185.141.106.238
,
a248.e.akamai.net
185.50.37.52
,
ak.net.akamaized.net
185.50.37.52
,
a248.e.akamai.net
185.137.25.214
,
ds-aksb.akamaized.net
185.137.25.214
,
a77.net.akamai.net
185.208.174.167
,
a77.net.akamai.net
185.208.174.167
,
a184.net.akamai.net
185.208.174.167
,
a248.e.akamai.net
185.137.25.214
,
ak.net.akamaized.net
185.208.174.167
,
a104.net.akamai.net
185.208.174.167
,
ak.net.akamaized.net
185.208.174.167
,
ds-aksb.akamaized.net
37.191.95.70
,
a248.e.akamai.net
37.191.95.70
,
ak.net.akamaized.net
37.191.95.70
,
a184.net.akamai.net
37.191.95.70
,
ds-aksb.akamaized.net
37.191.95.70
,
a104.net.akamai.net
37.191.95.70
,
a77.net.akamai.net
برای شیر خورشید
تست شده رو نت ایرانسل
Sni
a248.e.akamai.net
a77.net.akamai.net
a104.net.akamai.net
a184.net.akamai.net
ds-aksb.akamaized.net
ak.net.akamaized.net
Ip
185.88.178.196
185.50.37.52
185.141.106.238
185.137.25.214
164.138.17.122
185.208.175.228
185.208.174.167
5.160.13.85
5.160.13.85
37.191.95.70</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5223" target="_blank">📅 20:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برای شیر و خورشید
IP,SNI
185.141.106.238
,
aparat.com
37.191.95.70
,
snapp.ir
78.39.234.140
,
snapp.ir
81.91.145.2
,
snapp.ir
185.141.106.238
,
telewebion.com
81.91.145.2
,
digikala.com
78.39.234.140
,
varzesh3.com
81.12.72.218
,
varzesh3.com
185.141.106.238
,
digikala.com
37.191.95.70
,
aparat.com
37.191.95.70
,
bmi.ir
185.137.25.214
,
aparat.com
37.191.95.70
,
digikala.com
80.191.243.226
,
aparat.com
80.191.243.226
,
bmi.ir
80.191.243.226
,
snapp.ir
185.137.25.214
,
telewebion.com
78.39.234.140
,
digikala.com
80.191.243.226
,
digikala.com
37.191.95.70
,
telewebion.com
78.39.234.140
,
bmi.ir
81.91.145.2
,
bmi.ir
109.72.197.1
,
varzesh3.com
109.72.197.1
,
telewebion.com
109.72.197.1
,
bmi.ir
185.137.25.214
,
varzesh3.com
109.72.197.1
,
aparat.com
185.141.106.238
,
varzesh3.com
81.91.145.2
,
telewebion.com
78.39.234.140
,
aparat.com
81.12.72.218
,
aparat.com
185.141.106.238
,
bmi.ir
109.72.197.1
,
snapp.ir
78.39.234.140
,
telewebion.com
81.91.145.2
,
aparat.com
5.160.128.142
,
telewebion.com
81.91.145.2
,
varzesh3.com
80.191.243.226
,
telewebion.com
81.12.72.218
,
telewebion.com
185.141.106.238
,
snapp.ir
81.12.72.218
,
digikala.com
5.160.128.142
,
bmi.ir
5.160.128.142
,
varzesh3.com
5.160.128.142
,
snapp.ir
5.160.128.142
,
aparat.com
185.137.25.214
,
snapp.ir
80.191.243.226
,
varzesh3.com
185.137.25.214
,
digikala.com
5.160.128.142
,
digikala.com
185.137.25.214
,
bmi.ir
81.12.72.218
,
snapp.ir
109.72.197.1
,
digikala.com
81.12.72.218
,
bmi.ir
37.191.95.70
,
varzesh3.com
iP
31.214.169.244
185.109.61.27
46.32.31.30
37.255.133.30
37.191.76.110
80.191.243.226
185.141.106.238
81.12.72.218
37.191.95.70
63.141.252.203
142.54.178.211
5.160.13.85
178.252.128.66
94.130.13.19
2.23.168.254
2.23.168.144
78.39.234.140
109.72.197.1
185.137.25.214
2.23.168.7
78.157.41.60
2.23.168.96
185.208.175.228
81.91.145.2
2.23.168.47
185.255.91.60
2.23.170.80
2.23.168.213
2.23.168.174
65.109.34.234
5.160.128.142
SNi
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5222" target="_blank">📅 20:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5221" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4N70kAnLiLdMnCuU5vN9jNdPNC5EboX9NPVRbreykpzcmrHLsa289QpnJeltydq_Ko_nifGfUVoWIMdSHlexB9yfxtnboTVaVKGDJ4dWAKEuTNRLb9_3ny6FIrD5tLZNx8PBgqlklgzK5EgigV2idIVLZIy4Y_mkdm8MjEi5h94StfpJ0tivdgB3V2W9W8SR65V7ClEUiAiwIGHVB6syAD6Upwv-9yYwZ_dJJsrAJ4L8GV2KA1CJbg41p1m-oHDhT1d9U-41X2Z4Gd2oDFdvGLEj435hke7QkJuX6Hwd9pb3YznHJAm9WOPeCViN2h2oEocggLADUS45qqsSlypNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiJQUhl9NkogjVo4AVv1DwXr51HywNiCqgXijbagNpzWhXSylpiqgrj4YErs2JKzxALmpnVHv8F2U2_540aosYhB8jNJ8M8laSmoOiuzkeFubLTnpLJ8pWfogpEebCW-rpgj69DjeTk2jYmUq61SYbulPLIu2o3dQwQZ_Wt6F4PJ2dKB7ObiK5QZfLmUyfYThRFcIPUbMjaC9WARL25H4fkb6ql5izx83FYRZI5mzntNCFYv2BplrGujA038J0tKbifROL-rd4a6gwTFJMGmJ9mvrb9oNkaHomkGepAuEAKDRL3ctHJfxS90Sd-RAo8RbrA7ZGjNzrQvigzb86ouvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرامپت تبدیل تصویر معمولی به تصویری که انگار در یک کتاب کودکانه قدیمی اروپای شرقی دهه ۸۰ پیدا شده است
Turn this photo into a strange vintage Soviet children's book illustration with grotesque humorous cartoon energy. Use thin shaky black ink lines, awkward anatomy, elongated limbs, uncomfortable facial expressions, chaotic movement, weird proportions, sparse composition, and intentionally clumsy drawing style. Make the characters look slightly absurd, nervous, and ridiculous rather than cute. Use pale faded watercolor washes, dirty paper texture, uneven coloring, washed-out muted colors, lots of empty space, careless sketchy linework, and rough old-print illustration texture. Keep the background minimal and random, with small strange details and loose doodles. The mood should feel weird, humorous, slightly unsettling, and authentically like an old Eastern European children's book illustration from the 1980s. Do NOT make it polished, aesthetic, modern, cute, detailed, or realistic.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5219" target="_blank">📅 18:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ربات های کاهش حجم فیلم رایگان
@AdaptiveVideoBot
@Compreseebot
@mediaEasyBot
@wecompress_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5218" target="_blank">📅 17:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
آپدیت حیاتی و بسیار مهم فیلترشکن محبوب mhrv-rs (نسخه v1.9.33) منتشر شد!
---
رفقا سلام!
✋
ابزار
mhrv-rs
(نسخه‌ی سریع و سبک فیلترشکن رله‌ی گوگل به زبان Rust) رو که یادتونه؟ همون متد خفنی که ترافیک شما رو پشت دامنه‌ی اصلی گوگل مخفی می‌کرد و کاملاً هم رایگان بود.
حالا یه آپدیت جدید براش اومده که دست روی بزرگترین باگِ این متد، یعنی
«هدر رفتن سهمیه روزانه جیمیل در زمان بیکاری»
گذاشته و اون رو کاملاً برطرف کرده!
🎯
تمرکز اصلی این آپدیت: جلوگیری از مصرف بی‌رویه‌ی سهمیه گوگل (Google Quota)
توی نسخه‌های قبلی، حتی وقتی در حال وب‌گردی نبودید و سیستم شما کاملاً بیکار (Idle) بود، کلاینت مدام درخواست‌های خالی (Empty Polls) به اکانت جیمیل‌تون می‌فرستاد تا اتصال رو زنده نگه داره. این کار باعث می‌شد سهمیه رایگانِ ۲۰ هزارتایی روزانه‌ی شما خیلی سریع و بیهوده تموم بشه.
⚡️
تغییرات و بهینه‌سازی‌های فنی نسخه v1.9.33:
🔸
سیستم هوشمند Keepalive Backoff:
در حالت Full Tunnel، وقتی اتصال شما کاملاً بیکار بشه، برنامه با یک مکانیزم هوشمند و سخت‌گیرانه‌تر، فرستادن پینگ‌های متوالی رو متوقف می‌کنه تا سهمیه‌تون الکی نسوزه.
🔸
کاهش چشمگیر لودِ سرور:
با این کار، بارِ ترافیکیِ درخواست‌ها روی «گوگل اپس اسکریپت» و
tunnel-node
در زمان‌های سکوتِ شبکه به شدت کاهش پیدا می‌کنه.
🔸
پشتیبانی از ناوگان‌های ترکیبی (Mixed Fleets):
اگر چند دیپلوی مختلفِ جیمیل داشته باشید و حداقل یکی از اونا قابلیت Long-poll سالم رو داشته باشه، کلاینت هوشمندانه ارتباط رو به صورت Round-robin حفظ می‌کنه تا دیتای برگشتی از سمت سرور قفل نشه و اتصالتون همیشه پایدار بمونه.
---
📥
لینک‌های دانلود مستقیم آخرین نسخه (v1.9.33):
📱
نسخه اندروید (Universal):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-android-universal-v1.9.33.apk
💻
نسخه ویندوز (Windows 64-bit):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-windows-amd64.zip
🌐
صفحه گیت‌هاب پروژه (جهت دسترسی به نسخه‌های مک، لینوکس و کدهای جدید):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
📌
#آپدیت
#گوگل_رله
#نت_ملی
#رایگان
#mhrv_rs
#Rust
#Google
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5217" target="_blank">📅 17:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZW-QqNPR7vjwCsy2uMJz6FCnvGUgEw36xoCFZPb9KLhUQSqoiD4NPF5PbVQtuLQbsKl0oV3WMl4-yx8Lxm66vVqVnfePI5CSmPKwzoxIrWs4O71hhgTCQX04pSlVlvFoU9sCrmERzRw8qijvXTX-W3BoSTh5O_9UYJdvH9bXe_UAM_pmIEZil1WjKD3vfxoelV4SmDVHRxTRiCm7IN55-BQR2OIrHGUCvy5lM6ROZEmN1Vxa_KPHlD7Vj2Y3C_XumRbZzX7-_jAmIcwpXdKI6LYHnHQgQy0nhglCjNSuKMbqbufacZmGGOjekAuZVx4Qfj0yRjN-AVP6kGsx3Xn2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBKmlsVO4kPqnreKo4_sn_VnWj6RFMkCpfYZ1LNDYwUxp1dxpzzTLgUHzK8C5g6jrNM1VpaYlvEQbkHVXY9Gh4kYe5sYvblwTmN2dXX6zbgE1ju2CCe9EzEkqFW5X-R-55lf2VvyppT2HuUcxWsys9Q9Oj310Lui7cwonOfAxunQsCQBCFIPQ57RffosynLTrdBwTVcqAuoZYbquzHvdVVPrn5zSg407QiRbDKJoXOw_Y60KZhS0sxBnyrvZEuMTbYMTIwiIQILGG4k2QgF2Dr1RndTBrgMLwWVRL8JY2T-DZxDJq-kjXQ1TeNhFa62ruRSujxU7tDKpEy6UZU3nGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!  ---  رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5215" target="_blank">📅 17:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ezytel-v2_modified-r1@ArchiveTell.zip</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/archivetell/5214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت متد ezytel
باز کردن محتوای تلگرام با استفاده از گوگل ترنسلیت(یچیزی تو مایه های telemirror)
یکی از ممبرای عزیز ، ایزی تل رو ویرایش کرده و باگ هاشو برطرف کرده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5214" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!
---
رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند کانال، اسکریپت
EzyTel
رو کاملاً بهینه‌سازی کرده و یک نسخه‌ی Modified بدون باگ و همه‌کاره ازش داده بیرون.
✨
تغییرات و بهبودهای کلیدی در نسخه modified_r1:
🔸
تغییرات ظاهری و UI جدید:
• اضافه شدن دارک مود اختصاصی با رنگ‌بندی شیکِ Telegram Web.
• شیشه‌ای و شفاف شدن هِدِر کانال‌ها همراه با حذف آواتار و اسم فرستنده برای تمیزتر شدن ظاهر پست‌ها.
• امکان فول‌اسکرین، زوم و جابه‌جایی (Pan) روان با کلیک روی تصاویر کانال.
• رفع مشکل کامل هم‌ترازی (RTL) در متن‌های ترکیبی فارسی و انگلیسی.
• نمایش ارورها به‌صورت Toastهای نرم و محو شونده بجای پاپ‌آپ‌های (Alert) رو اعصاب!
🔸
امکانات کاربردی اضافه شده:
• قابلیت اضافه یا حذف کردن کانال‌ها مستقیماً از داخل محیط خود برنامه (دیگه نیازی به ادیت دستی فایل
channels.txt
نیست!).
• مرتب‌سازی خودکار و هوشمند لیست کانال‌ها بر اساس جدیدترین پیام ارسال شده.
• باز شدن کامل باکس Quoteها برای نمایش متون طولانی و امکان کپی شدن متن داخل کوت با کلیک روی آن.
• اضافه شدن دکمه اختصاصی COPY برای کپی کردن کل متن یک پست با یک کلیک.
🔸
ارتقای فنی و سیستم ضد بلاک (Anti-Block):
• حذف کامل دیتای اضافه و آشغال‌های گوگل ترنسلیت از لینک‌ها و باز شدن آن‌ها در تب جدید.
• استفاده پیش‌فرض ابزار از سیستم سورس
curl
روی پروتکل پرسرعت HTTP/2.
• اضافه شدن دامنه‌های بیشتر از سرورهای گوگل و تزریق Headerها و User-Agentهای کاملاً تصادفی برای دور زدن لیمیت‌ها.
---
⚠️
چطور باگ Rate Limit (خطای Something went wrong) گوگل رو دور بزنیم؟
گوگل روی حجم درخواست‌های پشت‌سرهم حساسه. برای اینکه لیمیت نشید:
1️⃣
خیلی سریع و رگباری روی کانال‌ها کلیک نکنید.
2️⃣
از لیست‌های بیش از حد سنگین و شلوغ استفاده نکنید.
✔️
راهکار رفع لیمیت:
اگر خطای Something went wrong گرفتید، کافیه ۲ الی ۳ دقیقه صبر کنید، یا اینکه یک‌بار حالت هواپیمای گوشی رو روشن/خاموش کنید (یا نت رو بین 4G و 3G سوییچ کنید) تا آی‌پیتون عوض بشه. (این ترفند روی آی‌پی ثابت وای‌فای خانگی جواب نمیده).
❌
محدودیت‌های دائمی:
عدم دانلود فایل‌ها و ویدیوها، کیفیت پایین تصویر و عدم نمایش ایموجی‌های پرمیوم تلگرام به دلیل محدودیت‌های خودِ ساختار گوگل ترنسلیت هستن و کاریش نمیشه کرد. این متد تا زمانی که گوگل در ایران باز باشه، تضمینی کار می‌کنه!
---
🛠️
راهنمای راه‌اندازی قدم‌به‌قدم روی ویندوز و اندروید:
💻
اجرا در ویندوز:
۱. برنامه معروف XAMPP رو دانلود و نصب کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
(محل نصب زامپ) کپی کنید.
۳. برنامه XAMPP Control Panel رو باز کنید و سرویس
Apache
رو استارت (Start) کنید.
۴. مرورگر رو باز کنید و آدرس
localhost/ezytel
یا
127.0.0.1/ezytel
رو بزنید. (اگر نیومد، پورت درج شده جلوی آپاچی رو ته آدرس بذارید، مثل
localhost:80/ezytel
).
🤖
اجرا در اندروید:
۱. برنامه KSWeb رو از استورها نصب و اجرا کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
که در حافظه داخلی گوشیتون ساخته شده کپی کنید.
۳. در برنامه KSWeb به تب APACHE و PHP برید و گزینه‌ی
Enable Server
رو روشن کنید.
۴. مرورگر گوشی رو باز کنید و آدرس
localhost:8000/ezytel
یا
127.0.0.1:8000/ezytel
رو وارد کنید. (ترجیحاً از آپاچی استفاده کنید نه Lighttpd).
📌
#آموزش
#ایزی_تل
#تلگرام_آفلاین
#نت_ملی
#گوگل_ترنسلیت
#EzyTel
#Bypass
#Telemirror
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5213" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
معرفی Cloak: مدیریت حرفه‌ای و ساده‌ی SNI Spoofing روی دسکتاپ!
---
رفقا سلام!
✋
خیلی‌هاتون درگیرِ تنظیماتِ پیچیده‌ی «اسنیفینگ» (SNI Spoofing) توی محیط ترمینال و کنسول بودید. امروز یه ابزار فوق‌العاده به اسم
Cloak
رو معرفی می‌کنیم که کار رو براتون گرافیکی و به‌شدت راحت کرده!
✨
چرا Cloak خاصه؟
این ابزار یه کلاینتِ دسکتاپ (مخصوص مک و ویندوز) هست که خودش همه کارهای پشت‌پرده مثل تزریق SNI فیک (Fake SNI) و مدیریت کانفیگ‌ها رو انجام میده. دیگه نیازی نیست درگیر دستورات پیچیده‌ی ترمینال بشید.
🛠
قابلیت‌های کلیدی:
🔸
مدیریت یکپارچه: وارد کردن فایل‌های کانفیگ V2Ray، Trojan و... با درگ اند دراپ (Drag & Drop).
🔸
تست پینگ و سلامت: تست هم‌زمانِ همه‌ی کانفیگ‌ها و انتخاب سریع‌ترین سرور.
🔸
سیستم پروکسی هوشمند: اشتراک‌گذاری کانکشن با دستگاه‌های دیگه توی شبکه (LAN) تنها با یک کلیک!
🔸
پایداری بالا: مدیریتِ عالیِ Tunnel ها و پایداریِ کانکشن.
💻
آموزش راه‌اندازی سریع:
1️⃣
برنامه رو از لینک گیت‌هاب دانلود و نصب کنید.
2️⃣
در بخش Settings، دکمه «Restore Default» رو بزنید تا کانفیگ اولیه (که شامل آی‌پی‌های تمیزِ پیش‌فرض هست) بارگذاری بشه و بعد Save کنید.
3️⃣
به بخش Profiles برید، روی دکمه Add بزنید و کانفیگ‌های V2Ray/Trojan که دارید رو وارد کنید.
4️⃣
بعد از اضافه شدن، روی کانفیگ کلیک کنید و دکمه Ping رو بزنید. اگر پینگ داد، یعنی کانفیگ سالمه.
5️⃣
دکمه Connect رو بزنید تا پروکسی فعال بشه. (برای اشتراک‌گذاری با گوشی، دکمه LAN رو توی تنظیمات فعال کنید و آی‌پی و پورتی که میده رو توی گوشی وارد کنید).
📥
دانلود برنامه (ویندوز و مک):
صفحه رسمی پروژه در گیت‌هاب:
🔗
https://github.com/PechenyeRU/FakeSNI
⚠️
نکته مهم: این ابزارها برای دور زدن محدودیت‌هاست، همیشه امنیت و رعایت حریم خصوصی رو در اولویت قرار بدید.
📌
#معرفی_ابزار
#Cloak
#SNI_Spoofing
#نت_ملی
#فیلترشکن
#ویندوز
#مک
#v2ray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5212" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتلیفای بای بای</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5210" target="_blank">📅 14:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم دور زدن فیلترینگ با روش SNI Spoofing
روی سرور ایران (ترکیب با پنل 3x-ui)
در این آموزش قصد داریم با استفاده از یک ابزار بسیار سبک و قدرتمند (نوشته شده به زبان Rust)، سیستم SNI Spoofing را روی سرور ایران راه‌اندازی کنیم. این ابزار به ما کمک می‌کند با جعل نام دامنه (مثلاً استفاده از یک سایت تمیز مثل hcaptcha)، سیستم فیلترینگ (DPI) را فریب دهیم و ترافیک را با موفقیت به سرور خارج متصل کنیم.
###
🛠
مرحله اول: دانلود و انتقال ابزار به سرور ایران
ابتدا باید فایل اجرایی پروژه را روی سرور ایران خود قرار دهیم. برای این کار دو روش دارید:
روش اول (پیشنهادی - مستقیم از طریق ترمینال):
وارد ترمینال (SSH) سرور ایران شوید و دستور زیر را وارد کنید تا فایل مستقیماً از گیت‌هاب دانلود شود:
wget https://github.com/therealaleph/sni-spoofing-rust/releases/latest/download/sni-spoof-rs-linux-amd64
روش دوم (از طریق SFTP):
فایل sni-spoof-rs-linux-amd64 را از گیت‌هاب پروژه دانلود کرده و با نرم‌افزارهایی مثل WinSCP یا FileZilla، آن را در دایرکتوری روت (/root/) سرور ایران آپلود کنید.
###
⚙️
مرحله دوم: ساخت فایل کانفیگ (JSON)
حالا باید به برنامه بگوییم که روی چه پورتی گوش دهد و ترافیک را به کجا بفرستد.
۱. در ترمینال سرور، دستور زیر را بزنید تا یک فایل جدید باز شود:
sudo nano config.json
۲. کدهای زیر را دقیقاً در محیط باز شده کپی (Paste) کنید:
{
"graceful_shutdown_sec": 0,
"listeners": [
{
"listen": "127.0.0.1:40443",
"connect": "104.19.229.21:443",
"fake_sni": "hcaptcha.com"
}
]
}
💡
توضیح مقادیر مهم:
*
listen:
آدرس و پورتی است که برنامه روی سرور ایران منتظر دریافت ترافیک می‌ماند (اینجا روی لوکال‌هاست و پورت 40443 تنظیم شده).
*
connect:
آی‌پی سرور مقصد شماست. در این مثال از آی‌پی تمیز کلودفلر (
104.19.229.21
) با پورت 443 استفاده شده است.
*
fake_sni:
دامنه‌ای است که می‌خواهیم فیلترینگ را با آن فریب دهیم (در اینجا
hcaptcha.com
).
۳.
نحوه ذخیره فایل:
کلیدهای Ctrl + X را روی کیبورد بزنید. سپس حرف Y را تایپ کنید و در نهایت Enter بزنید تا فایل ذخیره شود.
###
🏃‍♂️
مرحله سوم: دسترسی دادن و اجرای دائمی برنامه
۱. ابتدا باید به فایلی که دانلود کردیم، اجازه اجرا (Execute) بدهیم:
sudo chmod +x sni-spoof-rs-linux-amd64
۲.
اجرای برنامه در پس‌زمینه:
اگر برنامه را عادی اجرا کنید، با بستن ترمینال برنامه متوقف می‌شود. برای اینکه برنامه همیشه روشن بماند، از ابزار Screen یا Tmux استفاده می‌کنیم. دستور زیر را بزنید تا یک سشن جدید باز شود:
screen -S spoofer
۳. حالا برنامه را با فایل کانفیگ اجرا کنید:
sudo ./sni-spoof-rs-linux-amd64 config.json
*(اگر اروری نداد، یعنی برنامه با موفقیت در حال کار است. حالا کلیدهای Ctrl + A و سپس D را بزنید تا برنامه در پس‌زمینه سرور در حال اجرا باقی بماند).*
###
🔗
مرحله چهارم: اتصال کانفیگ به پنل 3x-ui
حالا که Spoofer در پس‌زمینه سرور ایران کار می‌کند، باید پنل 3x-ui را طوری تنظیم کنیم که ترافیک کاربران را به این برنامه تحویل دهد.
۱. تنظیم اینباند (Inbound - ورودی):
وارد پنل 3x-ui سرور ایران شوید. یک کانفیگ ورودی (مثلاً VLESS یا Trojan) با پورت دلخواه بسازید و به کاربر بدهید. (این قسمت دقیقاً مثل ساخت کانفیگ‌های عادی شماست و تغییری ندارد).
۲. تنظیم اوتباند (Outbound - خروجی) - بخش اصلی:
حالا باید ترافیک را از ایران به خارج بفرستیم.
* در پنل 3x-ui به بخش
Outbounds
(یا Xray Config / Routing بسته به نسخه پنل) بروید.
* یک Outbound جدید ایجاد کنید.
* تنظیمات این Outbound باید
دقیقاً مشابه کانفیگ سرور خارج شما
باشد (همان کانفیگی که در نرم‌افزارهایی مثل v2rayN روی ویندوز وارد می‌کنید؛ با همان UUID، نوع شبکه، TLS و...).
*
تغییر کلیدی:
فقط دو فیلد زیر را تغییر دهید:
*
Address (آدرس):
را روی
127.0.0.1
تنظیم کنید.
*
Port (پورت):
را روی 40443 بگذارید.
۳. تنظیم مسیریابی (Routing):
در بخش تنظیمات Routing پنل، یک قانون (Rule) جدید اضافه کنید و بگویید هر ترافیکی که از Inbound (کانفیگ کاربر) وارد شد، به این Outbound (که ساختید) هدایت شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5208" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://seup.shop/f/nn3o5 از حالت فشرده خارج میکنید میرید توی فولدرش بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام  trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationl…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5207" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
برگ‌ریزون‌ترین آپدیت جمینای؛ کلونِ دیجیتالیِ خودت رو بساز!
🚨
بچه‌ها، قضیه آواتار جدید جمنای (Gemini) خیلی دیوانه‌کننده‌تر از اون چیزیه که فکرشو می‌کردیم!
🤯
این بار گوگل رسماً مرزهای هوش مصنوعی رو جا به جا کرده. تو این آپدیت جدید، جمنای قابلیتی آورده که می‌تونید
دقیقاً با چهره و صدای خودتون
ویدیو تولید کنید!
🎬
🎙️
یعنی چی؟ یعنی کافیه عکس و صدای خودتون رو بهش بدید، تا یه آواتار فوق‌العاده طبیعی و واقعی ازتون بسازه. این آواتار می‌تونه هر متنی رو با لحن، صدا و میمیک صورت خودِ شما بخونه و یه ویدیوی کامل و بی‌نقص تحویلتون بده!
🔥
دیگه برای تولید محتوا حتی نیاز نیست جلوی دوربین بشینید؛ خودِ مجازی‌تون با بالاترین کیفیت همه کارا رو انجام میده! سرعت پیشرفت هوش مصنوعی هم به شدت جذابه، هم یه نمه ترسناک شده...
😨
فکر می‌کنید این تکنولوژی چقدر قراره کار یوتیوبرها و تولیدکننده‌های محتوا رو عوض کنه؟ شما حاضرین آواتار خودتون رو بسازین؟
🤔
👇
#Gemini
#هوش_مصنوعی
#آواتار
#تولید_محتوا
#تکنولوژی
#آپدیت_جدید
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5206" target="_blank">📅 12:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E53tQodz33Ep_tDR87rAQic-P-BUnjF1lB-K3SFT8L2qZw3vvhrVnKS0Z1zmZSC4dvirYRs1j_1uNjVEENT_T_2kht7NHuYdYoJKXcRrnaFm3VHhH-xxCkOco9p2KsGpGu3W9N-_wuhZReOXWE7W9L4rwaq1qDLD3bjwXdEvmkJMIEtw5X_Ab8A3caHZrwPveHGb53v0H6bZjhrRILXZZ3piXCbiCmKzGLgwrq1pQaKIXyu_FupTJaqQMUMjSCGjbDGqoOY3LwEl6oiFsq31DBlLhiuOZIskkyz5C0U4W3Srvdpal64n4yRnt3fj_ctvIBVxlhnbo9_pnm6YXcyAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای ۳.۵ اومد
پر قدرت تر از همیشه
+بنچمارک هاش
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5204" target="_blank">📅 11:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فقط باید داخل سرور اینو بزنید
ping
104.19.229.21
اگه پینگ بده میشه</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5203" target="_blank">📅 10:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">راه اندازی sni spoofing رو سرور ایران
کانفیگی که با این متد وصل هستید رو اوتباند کنید تو پنل و کانفیگ بسازید..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5202" target="_blank">📅 10:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F45ybxpnwt_lsponuvxB5mT4E5DbMv-JFCz6cPfXEcKH8hBLnlPdHMQ3KiRMdWOrK_qq6SL1IhUzcflPty4Q2ale-HrQJRgZKVkDJ9SQf5qM56ZtXhNwAiXvWj_HyV2uSatsikLbu5gC0oO8PS51JfoPK16BGYzD7YmFG9KSex-q7H3NXALYtLPzPQyMKd3tFX2F6YO_SIV9ZRhj8LzYDuBL3fEVD2RndL6QTeJJ_PqtH0P6mq2rwDjrlQAZo2vj58aDJ0HjLVdwwJS0IKNORB1puERy11MWKa6qb09AXaTuldN_5omjRuWj1b8_DpF-T1p1d0SRk6CVhPE7FWGqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Google I/O 2026
جمنای، جستجو، عینک‌های هوشمند
جدیدترین رویداد گوگل موجی از نوآوری‌های هیجان‌انگیز را به همراه داشته است!
🌟
از معرفی جمنای، تا به‌روزرسانی‌های پیشگامانه در جستجو که وعده نتایجی شخصی‌تر و کارآمدتر را می‌دهد، گوگل مرزها را بیش از همیشه گسترش می‌دهد. علاوه بر این، عینک‌های هوشمند گوگل بازگشته‌اند، اکنون با قابلیت‌های پیشرفته واقعیت افزوده و طراحی باریک‌تر، با هدف ادغام بی‌نقص دنیای مجازی با واقعیتی که روزانه در آن حرکت می‌کنیم.
🌐
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5201" target="_blank">📅 09:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spWm4jNaj3iHdovTj38FSTlLyy1T0hfLOS3PnDyD-CuznoIZZa_pocL_WNonRQSsmYKYoR2WyLzzR0NxbHWtWmOyyGfRMLck-sagU3KJaQrMtSwIFKOzJeYsyKHk77liJO53mM37REaIVIOnOPfUwGW_02t0KFeBueysBERIblupNPW79-Ue22p4ee-CSt8lPIjPLXKtJuax5amkXXD2IBEyjSMwCcqTZuwkbCnRsyIC6-_tdTtTghUfGLcIiTf7zbf-TBt6u7T9hGXLDB_HPPWvoEejfyn6ng3Md9BaZsp3wy305hz9QCrY2WUjsWftyAV-u7SEwO6NddLp2hLiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه Gemini 3.5 Flash منتشر شد
این نسخه به‌طور قابل توجهی قوی‌تر از Gemini 3.1 Pro است.
مهم‌ترین نکته این است که گوگل به مشکلات مربوط به عامل‌پذیری (agentness) به طور جدی پرداخته و به ویژه مدل را در این زمینه بهبود داده است. به عنوان مثال، نشان دادند که چگونه Gemini 3.5 Flash در ۱۲ ساعت یک سیستم عامل کوچک نوشت که می‌تواند Doom را اجرا کند. مدل Pro نیز وجود دارد و وعده داده شده که ماه آینده عرضه شود، قیمت‌های آن احتمالاً بسیار بالا خواهد بود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5200" target="_blank">📅 08:52 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
