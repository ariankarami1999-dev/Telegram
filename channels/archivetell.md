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
<img src="https://cdn4.telesco.pe/file/AtKwh_4hBKPjendd2ecLivNb3WJ1or4l5qq5zLwLPLus3p-7nNFZtIQxb-x8_5z2zxrMUplMm0-b7jJ2btVd36YaUe-JYHpvla7Jbcs_WTiaacfQRc0TLuTpnI1nCk2QbkJQLbdrHW23kmI95y3M72l93A7Na3t4dtSLQaICRk5FJe4smyreuGhylyGAQYcIPHXL6AdtU48hevMX2RAlCUnLS3ev3luy_cw79aFoFZr4gedLb_l3xW5GOr2LDaOQSJHkhE3ZYmrl9XT0SXnuSehsU8hI_Y3QDiM7tSRrzPOHMaC7OVJoWqIVDvmrITpBZS_Z6sSz61snCqOH1Pl3mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.92K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 556 · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=TkIbwgijX7-GssBvyBFgFYtTNqQAqufIa59ZxfugDHx3Y31FtO3gi46ddQgjQiQy3RoKhsi50VvGkBE7ssn5n8y6ply1X5vRYKgOfC6IeTxyW4CmQLlo7ELc3vFt47GPm8YI347J3ojT8nN8bF9KGd1oBH_Naf7iKMhY9Snq-6TSsU0Q3lveIlJN8FR5M5WKanZCDTi4WKkF0vA_TJrgcMh7kVYviz7Bm-7TN084oAMexDIoj-Dk_IvLlWKIl7TFAPjaOpW3e7RtmoGSbu4g8sPvhWgbx2i_ddAaYU26b0wln_YOxdFUXBaLVBuqhxNZO5_VmrDiBjQieI3PevapZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=TkIbwgijX7-GssBvyBFgFYtTNqQAqufIa59ZxfugDHx3Y31FtO3gi46ddQgjQiQy3RoKhsi50VvGkBE7ssn5n8y6ply1X5vRYKgOfC6IeTxyW4CmQLlo7ELc3vFt47GPm8YI347J3ojT8nN8bF9KGd1oBH_Naf7iKMhY9Snq-6TSsU0Q3lveIlJN8FR5M5WKanZCDTi4WKkF0vA_TJrgcMh7kVYviz7Bm-7TN084oAMexDIoj-Dk_IvLlWKIl7TFAPjaOpW3e7RtmoGSbu4g8sPvhWgbx2i_ddAaYU26b0wln_YOxdFUXBaLVBuqhxNZO5_VmrDiBjQieI3PevapZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 762 · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=UBd5YRuqqtverKmKh67iHXwjLOSQXI5yenF4nAPCf5FTUk1dovtX82RLAJZ5b0jAYNtAlPAcSS0yvUuPapVkcfQU0CHoFRG6hB8yyK-YT2N-4M8t0GdQ0w2fig5b7vPu8G4teP1rqMVvPn4jD27FBWdWcLWAn9CZ5YuHFcKoz153gxiC1PP_k5ypYRwGYQduqW705ql9D1S_E6WBoLSBhnFeFPnPdk8zgIeEUKbdM7rA37-PsyJvKzGSaW_rtQbInj7Bd1NIEwCnk4DMqmFU83lfjxQdaG0D8dIxwUmCTqPk7if6_l103aToD_f6lkM8VO9sMY5GVIZatdRiROutNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=UBd5YRuqqtverKmKh67iHXwjLOSQXI5yenF4nAPCf5FTUk1dovtX82RLAJZ5b0jAYNtAlPAcSS0yvUuPapVkcfQU0CHoFRG6hB8yyK-YT2N-4M8t0GdQ0w2fig5b7vPu8G4teP1rqMVvPn4jD27FBWdWcLWAn9CZ5YuHFcKoz153gxiC1PP_k5ypYRwGYQduqW705ql9D1S_E6WBoLSBhnFeFPnPdk8zgIeEUKbdM7rA37-PsyJvKzGSaW_rtQbInj7Bd1NIEwCnk4DMqmFU83lfjxQdaG0D8dIxwUmCTqPk7if6_l103aToD_f6lkM8VO9sMY5GVIZatdRiROutNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=pO_U3xNOtKESa0hVc-2esBZlQMeuz0DX15aBa1zBU-5uClHqRX0ldFI-MuiH78cHNQJQccUYzTyW06n7tXS-Ymybr1gE0pylXdx1wZbl3L06lkSLz7AMWIrCsWM9XCGyzBNTN6HzJW3cj_b1ZX7pcbORdDYLtB7n-Vq-WFfT9q7GQWfjsxfjoNdoBztbuBN6VuuRek8Ab21G1NBQ7KyHAmzgHFQQg2OVfsUkS9IOs4Ya5jEH6GYFK3sOrRDxhhGjhgAANvO5gSzMhhAqxahaLMHgREOKgEuQz3UqVV88Fe9kuOPFDAURoRoSy18cxFM2ZWXZAGlLRrrrb7ZktT3b2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=pO_U3xNOtKESa0hVc-2esBZlQMeuz0DX15aBa1zBU-5uClHqRX0ldFI-MuiH78cHNQJQccUYzTyW06n7tXS-Ymybr1gE0pylXdx1wZbl3L06lkSLz7AMWIrCsWM9XCGyzBNTN6HzJW3cj_b1ZX7pcbORdDYLtB7n-Vq-WFfT9q7GQWfjsxfjoNdoBztbuBN6VuuRek8Ab21G1NBQ7KyHAmzgHFQQg2OVfsUkS9IOs4Ya5jEH6GYFK3sOrRDxhhGjhgAANvO5gSzMhhAqxahaLMHgREOKgEuQz3UqVV88Fe9kuOPFDAURoRoSy18cxFM2ZWXZAGlLRrrrb7ZktT3b2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">100 گیگ مولتی لوکیشن
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=c4cb37f029af5828#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@crope.top:443?security=reality&encryption=none&pbk=Xgq8hNKvlfsBVHeJtXwjytbB5Fv2Tnu7vXJdZOgS8ig&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=crope.top&sid=b5af336756f77990#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@birch.gouher.one:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&host=stream.greenfield.lol&fp=random&type=xhttp&sni=birch.gouher.one&sid=28e92c6d545c9c26#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@meadow.pinevalley.top:443?security=reality&encryption=none&pbk=JfUgtIVRM26EKkksroAENXLWNJp9n28mSG-z-8CDAHc&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=meadow.pinevalley.top&sid=e86995a2ccab9364#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@rouze.click:443?mode=gun&security=reality&encryption=none&authority=rouze.click&pbk=PqunTCzbpHjmqH97ZpXHL0RBMyHaFzjJAO8i3uHr-XE&fp=chrome&type=grpc&serviceName=grpc&sni=rouze.click&sid=7fcb3d98608f93b6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@berry.riverpath.live:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&fp=qq&type=xhttp&sni=berry.riverpath.live&sid=bdf09e70262b409c#%F0%9F%87%A7%F0%9F%87%AABelgium
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@road.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=road.oakvalley.digital&sid=54aafe829679e92f#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@stone.quietgrove.forum:443?mode=gun&security=reality&encryption=none&authority=stone.quietgrove.forum&pbk=MchbHn3bpJaqAX-oqnNXYiXrbUTN0n-K203T8YGr8D4&fp=chrome&type=grpc&serviceName=grpc&sni=stone.quietgrove.forum&sid=0ae20b3e5e2c0bc2#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@flame.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=flame.quietgarden.live&sid=06d7e21ecb57367a#%F0%9F%87%A9%F0%9F%87%AAGermany
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@ember.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=ember.quietgarden.live&sid=fd488ee90cc0b9eb#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@valley.syrniki-iz-samokata.live:443?mode=gun&security=reality&encryption=none&pbk=euMfJzUx3qAGiaXwcvAXqXiqglBQKPOqxkTdSqwnqEw&fp=qq&type=grpc&serviceName=grpc&sni=valley.syrniki-iz-samokata.live&sid=c6046d150f597d04#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@field.wildgarden.digital:443?mode=gun&security=reality&encryption=none&pbk=dtxZ0lFLHE0IGfg45g2t1t7WwHWHuDW4xbfww3zKhDQ&fp=random&type=grpc&serviceName=grpc-bridge&sni=field.wildgarden.digital&sid=bbbbe9607d343bb6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@bridge.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=bridge.oakvalley.digital&sid=5278abf8d6d75483#%F0%9F%87%B9%F0%9F%87%B7Turkey
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@eveningwalk.sunnyside.city:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=eveningwalk.sunnyside.city&sid=54aafe829679e92f#%F0%9F%87%BA%F0%9F%87%B8USA</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/5926" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@areal1.greewebservices.ir:2425?encryption=none&fp=chrome&pbk=xQnXh5EfPDhcEBB7rRiLca33GYrMEeUa35domLL_yA8&security=reality&sid=9b60d3&sni=yahoo.com&type=tcp#@ArchiveTell%20%F0%9F%87%A9%F0%9F%87%AA
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/5921" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کدام مدل‌های هوش مصنوعی روی دستگاه شما قابل اجرا هستند؟
یک ابزار آنلاین که به کاربران کمک می‌کند بر اساس مدل GPU به سرعت بررسی کنند کدام مدل‌های هوش مصنوعی را می‌توانند به صورت محلی اجرا کنند.
https://www.canirun.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5920" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۲۰ گیگ
⚡️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/5919" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سلام و ارادت دوستان...
❤️
کسی از netlen خرید کرده ...  یه چنتا سوال دارم   @Sina_1090</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5918" target="_blank">📅 21:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2ZvKsJ3Brb1YJWucT2KaDlvDWPmT8CA8VZxFAcNe49KkJh4NhLx0O3YOAcfO35vwnX4dK6mGdnIG5vLYpZNh-a3asq9Mnp9eKCaS9KtoglGvVpp4gCG6I_Q2ewldEOiDWqLsqcWb6f_zGP_RR8jNEKd_7FsvBGEbpAlVWlfzKxMyyqOsRSOqTIhuxLcqmSDuBkuc6jIwY4fnZ0d3qo6zLiTtQjesMpmYdYIJ9_qR9YJtl87XpXW0TVAWMzR9D6kMh6ukaqOLbE3odq3Wna8NSq6sGPr5zO95LqriXvS0ZA9YjP6l_e6__d9ISHEmWthKTfrvwWfHmUDzfFGf02EhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚒️
۱۳۰ ابزار که جایگزین تمام نرم‌افزارهای اداری می‌شوند: آفیس، ورد و پاورپوینت. همه چیز مستقیماً در مرورگر کار می‌کند، بدون نیاز به نصب و محدودیت.
در مجموعه:
🕤
ویرایشگرهای تصاویر.
🕤
ابزارهایی برای PDF، ZIP، CSV، Excel و فرمت‌های دیگر.
🕤
تبدیل فایل‌ها بین ده‌ها پسوند.
🕤
فشرده‌سازی تصاویر.
🕤
فرمت‌بندی و پردازش کد.
🕤
کار با صدا و فایل‌های صوتی.
🕤
ضبط صفحه نمایش.
🕤
ابزارهای متنی.
🕤
برنامه‌ها و چت‌های هوش مصنوعی.
🕤
ابزارهای ریاضی، فنی و داده‌ای.
https://github.com/aghyad97/browserytools#-features
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5917" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سلام و ارادت دوستان...
❤️
کسی از netlen خرید کرده ...
یه چنتا سوال دارم
@Sina_1090</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5916" target="_blank">📅 21:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">VideoNote: ابزار یادداشت‌برداری و قالب‌بندی محتوای ویدئویی
یک ابزار یادداشت‌برداری ویدئویی کاملاً محلی که می‌تواند محتوای ویدئو را خلاصه کرده و یادداشت‌ها را قالب‌بندی کند.
https://github.com/xiaokeaijqx/VideoNote
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5915" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVfSlEd6D0MnwlqjxemmjiB50xGECPF1dWY-UpFuJoTYOjbs0ZKXBt0PNr66x4PzN4KVh5rPrvlklY0JPiGpROvUNJnL_3fMPgWiw4jkK0r-C1BTB1_eYL1gtFmYVV6N5dLqRc9wb4HuOlpsgT0egGOA6vqodyOPaJHHR4f5NggJzEd46jfs_IxSQwaNh7uNSQ5NMnQj9boTGWn3kEDsDPIruA9RchKRxPZvBVPYgMd29XHQko7ebyBE4qwQvAmp_KfUr62IujX5Qxb8EXi1kOZ7oTMnk4XS-w-kwVQR9QpOgo4tA7VxXzM3TKChkeav4iHlzCHINfgNkarafLP5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWrWNiX_P6PbsrdwZuKK-OR2y0MR2ZyktcxilPfC07gRKkRtU7Kndt1BVXNiOjkRCWAtaban5vdruFrJ03ONZEf7UMhm7xBf-8u2JjvRTbis3bcjNWSOhuTxEkyZlGjSwxvx5oWxMC5LuDEQtW29M4ZLtieVRxwqqQucbFPv2x_O_xhNZTusPppHtWKVB56e5cznWV7v5bruI8BZ7EEYdunMKbDv393MmliMSBGeuYtlGbWUvHsjUEL3Upq0KSUx70KYPm4xJ_yk2SnySbeIzW43kSqjjM1OstwO7H4FtaSqHnROczc0EEl8DVsOqD1YQq0GZ3hcGwBpbuowmnaKfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت عکس و ویدئو رایگان
https://www.mindvideo.ai/creative-studio/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5913" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://t.me/proxy?server=47.86.102.135&port=443&secret=dd887aa96cd9b760d42f62217afdcc6bc5
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5912" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvjDRcGjcSjjpjF9oAUZ3YaMad_8_RmvoiJfM2-y00fODRIeCk8UlxdhXb4eNNe8adQZWyOiaagxjpNxDWBzX4850gyxusLORUViFcHTs1qggf_Ig_ecqj5RtW4ghig7-kGcuL97sEtxJOSA1uJwhhnm_AcbvGXhpadyYuREhHQBoeY1I2SweTpts3ZhcQZgyAJsEq2BV_YhkUUWKhKK5yOs64t2uLjHgfjnEWtAQ0bPFcZkfVVq5NDpSXVl1OQh5xfH-T8qKmGzveRVFK-3upS21jRIFUZnkiwqDrKoO8tuRLuJtQMYTvUm97rw3vR0cqTOyU6u89c3rf3ZPnpY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ویندوز 11 را تا حداکثر توان ارتقا می‌دهیم
1️⃣
بهترین نسخه‌های ویندوز 11.
🕤
Flibustier 25H2
ایده‌آل برای استفاده روزمره.
🕤
Revision Group 25H2
حداکثر FPS ، مناسب گیم.
🕤
Ghost Spectre 25H2
فوق‌العاده سبک که حداکثر بهره را از سخت‌افزار می‌گیرد.
2️⃣
حذف زباله‌ها و قابلیت‌های اضافی.
🕤
Remove Windows AI
حذف هوش مصنوعی که منابع را مصرف می‌کند.
🕤
Win11 Debloat
حذف برنامه‌های پیش‌فرض.
🕤
Ultimate Tweaker
بیشتر از ۲۰۰ تغییر در یک ابزار کوچک.
🕤
Open Hardware Monitor
کنترل کامل بر سخت‌افزار
3️⃣
نرم‌افزاری که بدون آن ویندوز 11 دردسر است
🕤
WizTree
— بالاخره می‌بینیم فضای دیسک کجا می‌رود.
🕤
Revo Uninstaller
— برنامه‌ها را بدون باقی‌ماندن رد حذف می‌کند.
🕤
TaskExplorer
— مدیر وظیفه با قدرت بیشتر.
🕤
Explorer++
— مرورگری که واقعاً راحت است.
4️⃣
ظاهر و راحتی استفاده
🕤
Windhawk
—
مدهایی برای بازی ها
🕤
Jax Core
— پک‌های بصری و ویجت‌ها.
🕤
Seelen UI
— سفارشی‌سازی عمیق  رابط کاربری.
🕤
Cursor Mania
— هزاران نشانگر موس برای هر سلیقه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5911" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال: @ArchiveTell https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5910" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال:
@ArchiveTell
https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5909" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=26a4&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://104.167.199.23:2096/sub/ugqvbxg55h1u87rw
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5907" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx2qyyTpUAOiFbo5hGTQJwNH6qFveOBCYhE9CTu_oYqs9R8g6JRnRk79QsKxMexb5nUsef_IjZDKpF_prgKNyO9hrP7egKvtqguX58ICB6rKMcr0Du-JQZP43Vre7CKg0UqrTV5lidrHZyCCzaONJZ0XS77gD2Ndp6i07kgctdoluaEIhfAu8cSun_d1tDYoYOY01S9oakS8nPFpXplWzsciS2hcZg1EW2vEgvIPU-dkf5GRX2FKCsPCGVk7swJZMMatvnuCSIvddjXv5QvvHgWEpfDw3DdryAa_2kCm3skru9kZA_dl5xso630JOX5T0tKTysXzr6s-LDZ_J_8R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه ها قبلا ی چاره دیگری هم اندیشیده بودن پرایوسی سکسی</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/5904" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">https://obito.96s.ir:2096/sub/cqx44nj2vnu1mebr
لینک ساب 50 گیگ ...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/5903" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.  آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/5902" target="_blank">📅 18:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ibZy6hL9bq2w30p2m5bt2PeFFkd9vU-N0HtNEoiTL6nHwL6bBvhJRdmK4__G4w-w8kzX7jdN_B8coigk7G5khWvG2Rx0OMgEcnkt1GDNHwZw5ptSJzOl3fA_EABENszYTxYUQiUq6uesiq90f0l__0B2bGrKsTWwWJwMbUgiEmnyAUkX11N5A90dRJBf-viLc4V4Ioe6Mht0g_eyofP81CDuYKz4_Nra2pK0oMoqOOmWo9k_Pu-dDsFcySw7J7PEWzXx3yMV9OoGoS6zGZNN2KEXuVpMf9rcMNtRPJ3xMSoAASoU4c7Ei2OirRwgl_tmqhHenUCsX9BZvENsLMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.
آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر برنامه‌های داخلی.
🕤
اکثر درایورها (فقط ضروری‌ترین آنها باقی مانده‌اند).
🕤
Microsoft Edge و Internet Explorer.
http://github.com/ntdevlabs/nano11
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5901" target="_blank">📅 18:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تولیدکننده ویدئوی تصویری هوش مصنوعی
ابزار آنلاین برای تبدیل تصاویر محصول، پرتره، پوستر و سایر تصاویر ثابت به ویدئوهای کوتاه، پشتیبانی از چندین جریان کاری و کنترل دوربین، مناسب برای صفحات محصول، تبلیغات و تولید محتوای شبکه‌های اجتماعی.
https://image-to-video-ai.best/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/5900" target="_blank">📅 17:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://185.211.101.214:2096/sub/2f6ve5e7v0qim80w
سابلینک 50 گیگ ....
با نت های مختلف تست کنید...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/5899" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLQh87T8xMfEeTMv94p5tQOouVeoZrJtIqNUmTj9aYoJE1eJwBBMYBzr1uZE6LkYDG9dEUW04iMrzXiiF79zwRhiJpI0P_5HQa2VRjJ0wT5EpABRoEg9dZ5ZVSvFeK_gew_uNo8Dg6YKq0d3rnpuofJ6ptloTN0zGzhLs1eoCPRh2yPcGi1AfgjbAUiAk2q9iQ8ZO3oqsG_V4ZU8sClCbNYB5C87mdYwHTooqKJo9Xh2P_3LcTA5l7rfNiDrhGLieBav4cMa0co-3l74wnzJo0y6IG-ZGWKsqNiL15SlrjYCWHpEyeEOJHWyFsI_T6u9cp0YftluhGTXyVWPOgUnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyEvRirKuX9GaY1rrxgnotdRHFMLSINxlTFZbYOy7-uByHuiwuIJSjv0GqGTQ20MshK5W1bCZOx372QfR4lInu0QzaxS5Vy2_7hmM9MPix2auHqpRZqAWik17omn3obJD68BLDfQezwodUAVofEcT1z_T5eVz92iBt7yKE8J-XDiHU_lzJB8Z3h0RCSH1i9MPLfRr-w_6KIi_Ki7C90XTnpV638701lP9le-ojbBhJ_qIWrCq_iE5PqnQJjMyDfUk7o7Z6pnCe4jVQkCQaJuV6yAekN1APMozJRg0kV0vJWNywkA7CnicsEYx2iK8R_ywhv2RjcmneN4Rmufm2klQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">https://khan.shompolexy.shop:2096/sub/tvhnms3g1zjuotay
سابلینک ۱۰۰ گیگ اینترنت
با همراه اول هم وصله..
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/5897" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Gemini Omni تولیدکننده ویدئوی هوش مصنوعی رایگان
پشتیبانی از ورودی متن، تصویر، صدا و ویدئو، قابلیت تولید کلیپ‌های ویدئویی با کیفیت سینمایی
https://omniaipro.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/5894" target="_blank">📅 17:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zb9UFnXGN2Qc_5HheV1ElrTAdMtivi5i7KfPuW4-Pp2TjZSvPnRBoynDSpL67_kDDNqbuqP30d1ZLgkUlxkGH7V1xLT2_F_cfpjURpB3ZNrNv6wlO7fwQAAAYm8vX4vCSPgX3hXTYPoajKTbFN7RNMwpdSKKacdsF1285q92zjDY38a2Iz6sKOu6ScWaI6O3XO65zpCwPhGZ84T0ZcxmNgs3tqFZKdvWr0GJLe-1EFq5ckT59F_-dUa2RQ03h7dqZsswA4I06xPWtocukwcONOlc2PE9L4i5IsToadX9RetVi0gKQwdwdtIr98uu45fLEkPfYNjROznQbi8pEuqr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">slipnet-enc://AVYDFT1SX5QRahOVGapvCIQOi5iX+F+Ayz7d82kXBzKUgbDFGOsXcyY12oASii0n3Ye5Fj9LOHfyxzQpTH6aZzsHCccHQuHa78SADfbTQRNENnLD6CeHOuPxRffHOjkB+5tHdtQ89Kfk8TzpeVOxfFMxXDMxDhTuX7D/hrMsm9KchoxYpj3l1HNlOSDSMkO6td9WttjNX/TrOGk9jSX3n+bBnR1t64wJs9TYIUUycW/wKH9ntwehzsQ0l7MkpkxjVGD4Qqx8G/AGiOGcqy0OHxb4WsNfWIvP+mR1UcoObW2qJCMqPvMmimZQGTCI0cHIbpH1Kx0GLVXI9USz59N6D+2py/TLS4sGIKK40X2xohmjXthNyo3zcIw20FmuSnV8Dez5RVaSAbUhuCY8Iqa5G/B9U2PmqAMcZSVUh+yr4IoK/7Uelbj4rUAT6SfYQlZiliDE6Wkx7eM5dd8rR2Zxmtjl/Lr1X/qtrMeQgbJ5w5QAlxmAltcolUJt3BH58ZOqpwTe</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5893" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">530 B</div>
</div>
<a href="https://t.me/archivetell/5892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/5892" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/5891" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هر کی دلش وایرگارد میخواد
دست بالا کنه....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5890" target="_blank">📅 16:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">100GB مولتی لوکیشن
vless://d49eb175-facd-4c33-b1be-32c746701184@maple.cloudureld.com:443?security=reality&encryption=none&pbk=-VM1_ol58XU8fQHPvCnllupmpqyI6E1_bp6vpD6hD0w&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=maple.cloudureld.com&sid=7e52de801e7c71de#%F0%9F%87%A8%F0%9F%87%A6%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@island.cloudureld.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&fp=qq&type=xhttp&sni=island.cloudureld.com&sid=a7f9e69f037466b1#%F0%9F%87%AC%F0%9F%87%A7%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=9e327f04ce93c187#%F0%9F%87%B3%F0%9F%87%B1%20%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@developer.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=developer.projectauths.com&fp=random&type=xhttp&sni=developer.projectauths.com&sid=68d14e7adba07698#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@dev.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=dev.projectauths.com&fp=random&type=xhttp&sni=dev.projectauths.com&sid=8a9d1d8916227e5b#%F0%9F%87%A9%F0%9F%87%AA%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5889" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4i1uvH-NvE3ObcmSzKOT6NMG8FYiQGKnC-peHPvbkJZabGjccVw328WRN-Yyw_1Or3h-61aj7VG83kbatCVCx9vTBxCvpwdZ0BYAzlDZdnoWQs9dz6KHgb5fSNDsyAcFVBC4yU5dVLx0yRWj7Bq5EYvTT5oLcBMNx8EH2rs80mP0c_7tqBbetTsJW4otKUURzFjF_NrD4I7TYdDudREyrGNbO5rH4IGYr78gC8IppizyL6JDTFwEBD0SOyze6IySdOVD1YUOajJQ7BQs1KX7graVSpIV5_SO7NXHgFgqpjGtwfCYn5G9z5xtcHKf1NK6480sYxHhKWeuoSgF7mrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری اندپوینت endpoint برای
کانفیگای وارپ
اسکن کنیم
داخل لینوکس یا ترموکس این رو بزنید
pkg update -y && pkg upgrade -y && pkg install curl -y
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Warp-Scanner/main/install.sh)
به سوالاتی که میپرسه جواب بدین میگه چندتا اسکن کنم یا سریع باشه یا نرمال. ipv4 رو انتخاب کنید
دقت کنید که اسکن باید بدون فیلتر انجام بشه. اگه فایلش واستون دانلود نمیشه فقط قسمت دانلود فایل رو با فیلترشکن انجام بدین بعد قطع کنید و اسکن کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5888" target="_blank">📅 15:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=a99c6c05&sni=www.samsung.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5887" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">vless://cc074e81-342d-402c-9fa6-fa907728222a@85.198.20.217:80?type=tcp&encryption=none&security=none#tunnel%2050gb
50gb tunnel
تست شده بر روی : ایرانسل , سامانتل , رایتل , اپتل , مخابرات
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5886" target="_blank">📅 14:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5885" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید.
warp-generator.github.io/warp/
‎
فرقی نداره کدومش باشه از Amnezia باشه فقط.
اندپوینتشو تغییر بدید به این
188.114.97.6:7281
بزنش داخل Amnezia WG
با همراه و ایرانسل و مخابرات وصله.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5884" target="_blank">📅 14:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ابزار خط‌فرمان دور زدن DPI روی همه پلتفرم‌ها — با pool تطبیقی چند-IP/چند-SNI
به‌جای یک upstream ثابت، ابزار به‌طور مداوم ترکیب‌های (IP، SNI) را بررسی می‌کند و هر اتصال را از طریق سالم‌ترین جفت هدایت می‌کند — بدون قطع شدن اتصال‌های فعال.
روی Windows، macOS، Linux و Android (Termux) کار می‌کند و برای روش پیش‌فرض نیازی به دسترسی root ندارد.
روش نصب
git clone
https://github.com/hjfisher/SNI-Spoofing-HJ.git
cd SNI-Spoofing-HJ
pip install .
snispf-hj --info
https://github.com/hjfisher/SNISPF-HJ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5883" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=FZKSGbJktwKV9G_HcXNRS_ZPdk1fYK06XwR9y4Ab0Ytm3vSj9r04-WYu--vv3QStHU6E4-V9kcXynuCp0SS4rYLQDFWstRWof_HolHoixefsJp-w_eBDtYwYJAHyZY787S5kJB-7q25S7sCff6nGzTuPH-i9kta2xgTgHymCwxPSbURXuEqpDi9rey07v8N_KUCGpjGduY2ioDm4sV2C0qVhc2DHe-29v9nzq6lf9ZPX9jp9AJfkgc6zZKffqdEmoggqF2LKgqPl-ogU5lU_sjcRBrGdJ1VXYE4Kt8FZB7p04anrx3CST5OywYgloAJIywe-bU_IKVAJzxKnQcyD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=FZKSGbJktwKV9G_HcXNRS_ZPdk1fYK06XwR9y4Ab0Ytm3vSj9r04-WYu--vv3QStHU6E4-V9kcXynuCp0SS4rYLQDFWstRWof_HolHoixefsJp-w_eBDtYwYJAHyZY787S5kJB-7q25S7sCff6nGzTuPH-i9kta2xgTgHymCwxPSbURXuEqpDi9rey07v8N_KUCGpjGduY2ioDm4sV2C0qVhc2DHe-29v9nzq6lf9ZPX9jp9AJfkgc6zZKffqdEmoggqF2LKgqPl-ogU5lU_sjcRBrGdJ1VXYE4Kt8FZB7p04anrx3CST5OywYgloAJIywe-bU_IKVAJzxKnQcyD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
قاتل ChatGPT و Claude از PewDiePie جامعه هوش مصنوعی را منفجر کرد: مخزن Odysseus تنها در دو روز تقریباً ۲۵٬۰۰۰ ستاره در GitHub جمع‌آوری کرد و حتی Anthropic نیز به این پروژه علاقه نشان داد.
این جایگزینی برای چت‌بات‌های شرکتی است که بدون محدودیت و نظارت ساخته شده است. Odysseus پاسخ OpenAI، گوگل و دیگر غول‌های صنعت است.
چرا این پروژه اینقدر سروصدا به پا کرده است:
🕤
راه‌اندازی روی کامپیوتر یا سرور — بدون حساب کاربری.
🕤
تمام داده‌ها در اختیار مالک باقی می‌مانند.
🕤
عامل‌های داخلی: مرور وب، ویرایش فایل‌ها، تحلیل اسناد، مرتب‌سازی ایمیل‌ها و غیره.
🕤
پشتیبانی از تحقیقات عمیق.
🕤
API برای اتصال مدل‌های محلی.
🕤
رابط کاربری آسان و کار با گوشی هوشمند.
🕤
امکان کار آفلاین.
https://github.com/pewdiepie-archdaemon/odysseus
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/5882" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">vless://fec5f560-7e78-4b71-9432-418621738d3f@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--tunnel1gb
1 گیگ تانل
تست کنید با ری اکت بگید</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5881" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😁
❤️
ایرانسل تست شده ، بقیه نتا وصل بود استفاده کنید..
vless://3638b964-5404-4145-b19c-89f7cc8c237b@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=57e7bd&sni=www.amazon.com&type=tcp#@ArchiveTell%2020.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/5880" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه  همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5879" target="_blank">📅 12:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانفیگ نامحدود اهدایی یکی از ممبرای عزیز کانال
⚡️
❤️
trojan://4bdbapq0n755s7cr@168.222.43.197:48309?host=168.222.43.197&path=%2FEmpty&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5878" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه
همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5877" target="_blank">📅 12:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://81a1e8f2-3b97-41e5-8c60-7d7d1576e028@185.92.181.217:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=185.92.181.217&mode=auto&path=%2Fmohraz&pbk=SqXIQC6Q68_mpLX_JVFXLHwCeSLHpyk5JhKvrd1P7DA&security=reality&sid=bbe112&sni=www.nvidia.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5876" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF4A4bwvjLHq8qmJBtrozGeiJTobupt1PxpvPmxkxcOU-OpNWqPe8ZrpD21zBaT_c3n7GM3YW4riAM80LwmXkSFjdmHCtaFl3vg5EE0HbwMgN2uzrPwyQe7Iz3aelgfFv7ompBUTrdxrGb7HiI93MfAndDGHTZnKA7F8iP368teL3XT9oNMyjI57z_wpqGSGEGXI11EWCRRJOj-2ZDw5GLpUG9Fnt-kqq22P8m1xqTcb6dBsvQtgVCZfFHPILzaK7Dd3qdKotSY-i9W1_F-nUE5_AS5wX4nlEy-cIQ5ddVJHvTx_R4rHZFcsxQqTvXfbeTDe082WT3O9SouYIvEA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌏
یادگیری زبان از طریق دیالوگ‌های زنده با هوش مصنوعی — PrettyPolly، سرویسی برای کسانی که به خوبی می‌خوانند و زبان خارجی را می‌فهمند اما در مکالمه معمولی دچار مشکل می‌شوند.
🕤
هم‌صحبت هوش مصنوعی برای تمرین مکالمه — می‌توانید بدون خجالت و ترس از اشتباه، زبان انگلیسی و زبان‌های دیگر را تمرین کنید.
🕤
سناریوهای آماده برای گفتگو — سفر، مصاحبه‌ها، مکالمات روزمره، صحبت‌های کوتاه و موقعیت‌های واقعی دیگر.
🕤
کمک در حین گفتگو — ترجمه، راهنمایی و تصحیح عبارات به صورت آنی در دسترس است.
🕤
بررسی پس از مکالمه — سرویس اشتباهات، نقاط ضعف و کلماتی که باید تکرار شوند را نشان می‌دهد.
🕤
سیستم حفظ پیشرفت — عبارات جدید را می‌توان تثبیت کرد و به تدریج در تمرین‌ها تقویت نمود.
http://prettypolly.app/app
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5875" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=AORmk0wCjD64zM30u7DMTJ-Bj8UANjeT8g-6Lgxde59zOHHZ4uviPAdF-Vn6jgg_cN8OWvZF1BlDv4ktAY25PKUbUI0Fm-Nge70Z1jzvjjGILzXN1PUE8caSrxnrZkOEMejdIoZn3LAdFAqglVRgnWTl3wkxJ9jek7aA7w1j8kdcar1TlOT9dYh8rpjP5TbbNu2qKlA37DhEY9-Qi6mkHd7E6UmyFOO8mJJGC8lZ46ab8_P6QX1SEpYatziEva62ZEqk2vAaObztL1MyutwZY7YbgDwSGzDhO410CXP7qGpemEJmxQWe55iEKHt2Wmu1ZMrvBPloeY9y7rEz57rToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=AORmk0wCjD64zM30u7DMTJ-Bj8UANjeT8g-6Lgxde59zOHHZ4uviPAdF-Vn6jgg_cN8OWvZF1BlDv4ktAY25PKUbUI0Fm-Nge70Z1jzvjjGILzXN1PUE8caSrxnrZkOEMejdIoZn3LAdFAqglVRgnWTl3wkxJ9jek7aA7w1j8kdcar1TlOT9dYh8rpjP5TbbNu2qKlA37DhEY9-Qi6mkHd7E6UmyFOO8mJJGC8lZ46ab8_P6QX1SEpYatziEva62ZEqk2vAaObztL1MyutwZY7YbgDwSGzDhO410CXP7qGpemEJmxQWe55iEKHt2Wmu1ZMrvBPloeY9y7rEz57rToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل راهنمای رسمی پرامپت‌نویسی در Gemini Omni را منتشر کرد
در راهنما چیزهای بسیار جالبی وجود دارد: کنترل دوربین از طریق اصطلاحات حرفه‌ای (dolly zoom، locked off، oner)، همگام‌سازی نور ساختمان با موسیقی، تولید ویدئو بر اساس استوری‌بورد، تغییر سبک با حفظ حرکت، ترکیب ویدئو، تصویر و صدا در یک پرامپت.
نکته کلیدی: کوتاه بنویسید چه می‌خواهید. نیازی به شرح هر فریم نیست.
https://deepmind.google/models/gemini-omni/prompt-guide/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/5874" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://cdn.mozcloud.ir/XS_AZ/cue4q8rhm47n4120
بدون فیلترشکن از بخش اسکنر استفاده کنید و بهترین گزینه رو اعمال و کپی کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/5873" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">AVG Secure VPN  Code:AAUNB7-KK3HT2-4Z4J56  @ArchiveTell | 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/5872" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۱۶۰ گیگ پروکسی اهدایی یکی از ممبرای عزیز کانال
😁
❤️
https://t.me/proxy?server=hdi.mahdii-coder.eu.cc&port=443&secret=dde9a1ae9b1c4ff69a688d03b7257db653
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5871" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5870" target="_blank">📅 11:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
حالا تقریباً هر کسی می‌تواند اولین اپ خودش را بسازد!
دیگر برنامه‌نویسی فقط حفظ کردن کدها و سینتکس‌ها نیست؛ مهم‌تر از همه این است که بتوانی دقیق توضیح بدهی چه می‌خواهی.
🤖
📱
گوشی اندرویدی را به لپ‌تاپ وصل کن، Cursor یا Windsurf یا VS Code AI را باز کن و ایده‌ات را بنویس. هوش مصنوعی بخش زیادی از کار را انجام می‌دهد و نتیجه را مستقیم روی گوشی خودت تست می‌کنی.
💰
مثال:
یک اپ مدیریت هزینه‌های شخصی که آفلاین کار کند، هزینه‌ها را دسته‌بندی کند و آمار روزانه، هفتگی و ماهانه بدهد.
🛠
مراحل:
🔹
گزینه USB Debugging را فعال کن
🔹
گوشی را به لپ‌تاپ وصل کن
🔹
پروژه را با Expo اجرا کن
🔹
خطاها را برای AI بفرست تا رفعشان کند
🔹
نسخه نهایی را روی گوشی نصب کن
💡
ایده‌هایی برای شروع:
✅
ردیاب عادت‌های روزانه
✅
فلش‌کارت درسی
✅
تایمر تمرین ورزشی
✅
اپ یادداشت شخصی
✅
مدیریت مشتریان (Mini CRM)
✅
برنامه‌ریز محتوای تلگرام
🔥
نکته مهم:
امروز لازم نیست از روز اول یک برنامه‌نویس حرفه‌ای باشی. کافی است مشکلت را بشناسی، ایده‌ات را توضیح بدهی و با کمک AI اولین ابزار کاربردی خودت را بسازی.
🌍
دوران جدیدی شروع شده؛ جایی که ساختن نرم‌افزار از همیشه در دسترس‌تر است.
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5869" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">AVG Secure VPN
Code:
AAUNB7-KK3HT2-4Z4J56
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5868" target="_blank">📅 10:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA44hGNG-hkv3B_fxy_zqtjsNU9GKNl5aPx8bBIuZTl5XgBiYOUSEDb5-ZIh8eSWukTIIp51owNpU0hVS4CqY9ZwFEWMgiV_RNDdNv5XzDVIi4m9InkG1dLSRiKotg-2I_7QYydrHd2ORlSQILP_GI_9obZ6SfUNzEE7O5gnz6cpLJo60mfGtzgS4efQ-dJG8WLtO-Yz2sQxOO-GvcI2Lo3ADsKLSMhsm5BY1EsdVXt_gqF1gPbfl31kp35tgArAb-DpbzeueLnsPOTtOwEClURgndi-1c5f5gkBbI1FnIrQdvCZyonNO7-I5jNAmUVdAB03JHzBofID2qx1rdXJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✴️
استایل‌های سفارشی در Krea 2 اکنون برای همه باز شده‌اند
Krea LoRA را برای مدل جدید خود عرضه کرده است، بنابراین می‌توانید آن را با استایل، شخصیت یا شیء خود آموزش دهید و سپس در تولید استفاده کنید.
قبلاً این ویژگی به صورت بتا برای Max و Business بود، اما اکنون دسترسی گسترده‌تر شده است.
https://www.krea.ai/image/k2-large?style=y45oxkkdp
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5867" target="_blank">📅 09:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell_@Lozkc
کانفیگ پینگ پایین منطقه ای
اگ وصل نشد خاموش و روشن کنید احتمالا درست شه چون شبکه باگ میخوره گاها
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5866" target="_blank">📅 09:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIoL8HHHvgQI1MZf6ldbp0dRmjnnvPokhQc393F0OrjKUI5ubHnSpeYEYdNSMQ2cA-0K06uQGyjWfIgEjrPspEyQOKE_yahEIDNWf6W9pe3nVikydSOX1h3chvzbHDMbEA1lCjybqjM1XvXb_hRH__2FZBgMG_r3wTQSQ2e7W8EJQ_Tk8_vGgxL7wARHEIgzxQAbs0FukKmmyBm__gSalV96IsimXAn7Uk3RcbxoqLF8PqT4Lnb-24fyiHMGijcyWhLJ8K9fGeAwu308GDHKrh7weNGijdGEycahrU6zlOOUpRttgna8PCpfW_ElVHrQOUN_3X64jrWsd5stmoR5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ما در حال ارتقای Gemini به حداکثر هستیم - افزونه‌ی Voyager را پیدا کردیم که ویژگی‌هایی را که در ابتدا فاقد آن بود، اضافه می‌کند. مناسب برای کاربران AI Studio و کاربران معمولی:
🕤
حذف واترمارک از تصاویر.
🕤
مدیریت پیشرفته‌ی چت: حذف دسته‌ای چت‌ها، نقل قول پاسخ‌ها، انتخاب مدل پیش‌فرض و موارد دیگر.
🕤
به شما امکان می‌دهد پوشه‌هایی برای مکالمات با همگام‌سازی از طریق Google Drive ایجاد کنید.
🕤
به شما امکان می‌دهد پیام‌های مورد علاقه را ذخیره کرده و از آنها در Gemini، AI Studio و سایر وب‌سایت‌ها استفاده کنید.
🕤
جدول زمانی راحت: در پاسخ‌ها، رشته‌های مکالمه و پیام‌های مورد علاقه حرکت کنید.
🕤
Markdown، نمودارها و چارت‌ها را به خوبی رندر می‌کند.
🕤
مکالمات را به PDF، Markdown و JSON تبدیل می‌کند.
🕤
تاریخچه‌ی افکار را از Deep Research استخراج می‌کند.
🕤
در Chrome، Edge، Firefox و Safari کار می‌کند.
https://voyager.nagi.fun/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/5865" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klbmay0_L6dILiPa_pKUTjXVJEIU9q7qca5Z0ZAJxxSS7x2kn0VLDKchYgU0XxC8cRV8mxQ9LKJJYd69iTNNtk63Nu4M5gpHKw8V4VY2JiUByTnPucxlwdjx30HxmE3wGEuhAeOUFcMGO0EI6TLL7SR_gYbC_2DLE-XiOe2s1osleIFz_q-c_7troakTcaKPW37l4CReu9ZJVkY0rpxPsZdxQRKCGnsvExpmoGTAi0P8_lFxLKgy1S5Bv9-3SniInn1W_l-6C7AfGrjj4cWqvjglmcTi1j-9XyXTZto83wwCn9tNIqHPK4PxDPT8eVa3I9PatVMjldLcSEobMoAmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JePDge7s-o-mcXchTrEiygSv-B8m6iZB94yNmz4g8hyVC47mxMS8n2kID8qVAkifBIbPl1Ma5GVTcUxE2xL1cv_g4ivHY-NkHnQ42D_Ltsp7-13fs15v9SndndomwUwuGoM3KOIGx9186G02vsSCzNW_aCYOcY9xHfbB89hitJcjGaba1wmqobZEJav_ubkDB-1GScomY7POqB6g9z0s1kIXErXnYBemzn10ID0EGTQrGNYe4XkzQimzbQeB0Fm4EdvJaaCqeLAR89trZmpKKmLKsbSh1HIG54VlSxhLSwK1Ahpwf6JevBOj2wa2-jZwfe7MnZdHFA4WC-b-BVTX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TG9QGjNfWotqCMatC1jdRxR7ETFc7wAO-SCcoPgPZYUmug_sZWy81SealOkzSrEev1NsukpB1AaQa4rhX-6g73yCYsfw5flP7_Z3n4pKK2t9CQxxYeoE4aCJ0UUKpsPa2yOUGwUJp8nGEd9c9l6TMY_LZy-oVtZqFsGBiD3Mn9jUqaw3x6jQCoLkzZY2yTH8jZgapXT12yEsdf-qf9Bd68A54-3DPso_PeKBtouvdLKW7pW1DgMG9UTDaGM3t3BVWciYi22u5jkU31bl4_eiYm2npoTyx3tF3OPz7GNjZrkQ5ByVCNIDm2wHLsZCV7Ec2ZSL91Y5YIVSWDTIoQFRmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منبع بی نظیر بازی های PSP
@Ppssppiso2025
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5862" target="_blank">📅 09:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjSN8utlqmx3jg1MtNmq6MMOdZPU5_i77bJ18VWulrEEtlmBjWCgQrJyWibUUkxHFLA54ru9-1I-kI71YK1AqK_GKF9Db-CMOUl-57BASzGkVpi6p6WTxgXMCV7v33arMjeMXUbj5_LBeR2HiUYoZDcVHj0_yXwnd5PRIRhae-L7oWgj3D6CVlgtXBwK7gSEQEDvVbkBG9TfduY_6IEN3yNcj8Gvxl_mI8XC4XjgmuyWc4VI4cd0e8VyWazXUvJCiKMAUCzayFPwQ9CUdL6K_s6TF1sWPj55QAWbR6OslB6zb15XFnb3d8L6Ozvfnr6q4bhmXepp-mq6XTCayXflaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnLM1fwhxvxHww-UZE8R6iDJIYTf93H7Tt_4htS_Wwz3U1InpiWov4lsSB2HZJV3AVG2TAMPJtkslMME9RcH9oL4Ehk2eGuy-Niwxo2Fp7xdKjcmUSkq7L5LO_faxgpFBCXlbcDKNqCkem2N1w7-daiiNPy7qXhwuo08h7pqq87Knp9sk-LYKP5dqCJDYwo_by8_1AqKpEan56_YPJqSJxgTL_1FB47BHe4pM907C_Swmu0b5amxmVoGmvIv6aca-zSwoc6fkhCx2JEMC-3wAPu9LWtZNG_gbc1m9hTIh_AgoNz748jWJMbfAM2JFcCL7bsGk6Ero36kgjn8f5KUDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
اکنون می‌توان PSP را مستقیماً در مرورگر اجرا کرد — یک علاقه‌مند نسخه وب شبیه‌ساز افسانه‌ای PPSSPP را منتشر کرده است.
🕤
همه چیز بسیار ساده کار می‌کند: سایت را باز می‌کنیم، فایل ISO بازی را بارگذاری می‌کنیم و در عرض چند ثانیه بازی را بدون نصب نرم‌افزار جداگانه اجرا می‌کنیم.
🕤
رابط کاربری تقریباً کاملاً مشابه PPSSPP معمولی است، پشتیبانی از گیم‌پدها و بارگذاری بازی‌ها مستقیماً از دستگاه وجود دارد.
🕤
God of War، Tekken 6، GTA: Vice City Stories و دیگر بازی‌های محبوب به راحتی روی کامپیوتر، تبلت و گوشی‌های هوشمند اجرا می‌شوند
https://root-hunter.github.io/ppsspp-web/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5860" target="_blank">📅 08:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اپن سورسه پروژه
البته باید کدش بررسی بشه
ولی شدیدا روونه
و کلا انگار ی اپ دیگه اس
😂
خیلی خوشگله
در کل جای کار داره و ابتدای کارشه پروژه ولی خیلی باحاله
اپشنای خوبیم داره بررسی کنین</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5859" target="_blank">📅 03:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMonoGram</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">monogram-arm64-v8a-0.1.0-release.apk</div>
  <div class="tg-doc-extra">49.1 MB</div>
</div>
<a href="https://t.me/archivetell/5855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5855" target="_blank">📅 03:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTDUn1MdCKnN99b1ptXP7DCcrJl9rE3D5Kp3se9X5EgNJr-JGK0PgNeIajPCLsmIDJJEAQQeEpKEv7-GnOlHWCaER3VjkotS61yg-nVIea3VBSNdaASIBKdEDmNKgv2D0A5CGooMck4Qkf-zhgtvDs1LGNoQkOhXkgaCOlX5kcfxexAHWTbLDf9WUYeTmRPAzr3g2jFTcsLMJK8vGhmAJ4f8qwsBA_LCvsnr_a5_LqwoQTWi_j5RT4S7codswYjiXwjfkxchFzpAqDc4R9ecx8jB3IDkyYK6ASicJgaZK32yeIL8Z0rLoVHhC2mGwBm_zYFlFSO5MsLoNYgxxViUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠️
MonoGram؛ یک کلاینت متن‌باز و مستقل برای تلگرام
MonoGram یک اپلیکیشن غیررسمی تلگرام برای اندروید است که برخلاف بسیاری از کلاینت‌ها، از صفر و بر پایه TDLib توسعه داده شده و فورک نسخه رسمی نیست.
✨
ویژگی‌ها:
• رابط کاربری مدرن با Material 3
• عملکرد سریع و روان
• قفل بیومتریک و ذخیره‌سازی امن
• پشتیبانی از جستجوی داخل چت
• مدیریت بهتر فایل‌ها، رسانه‌ها و استیکرها
• متن‌باز و قابل بررسی توسط همه
📌
توسعه‌دهندگان اعلام کرده‌اند که MonoGram روی تجربه پیام‌رسانی، طراحی مدرن و عملکرد بهینه تمرکز دارد و قابلیت‌های NFT و کریپتویی تلگرام را اضافه نخواهد کرد.
این پروژه هنوز در حال توسعه فعال است، اما با انتشار نسخه 0.1.0 امکانات و پایداری آن نسبت به قبل به‌طور محسوسی بهتر شده است.
🔗
GitHub:
https://github.com/monogram-android/monogram
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5854" target="_blank">📅 03:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">100GB
⚡
vless://29f8120c-fa78-4b20-b5a5-5390d9cfbbc9@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=a28e08feb9324fb0#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5853" target="_blank">📅 03:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇫🇷
ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDhhMTZh@51.195.235.71:2083#%F0%9F%87%AB%F0%9F%87%B7%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5852" target="_blank">📅 03:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚡️
چینی‌ها از Qwen3.7-Plus رونمایی کردند؛ یک مدل چندوجهی و Agent محور جدید!
🤖
شرکت Alibaba مدل جدید
Qwen3.7-Plus
را معرفی کرده؛ یک مدل چندوجهی (Multimodal) که بینایی و زبان را در یک معماری واحد ترکیب می‌کند و برای اجرای وظایف پیچیده طراحی شده است.
🔥
قابلیت‌های کلیدی:
🔹
فعالیت به‌عنوان یک Agent کامل در محیط‌های GUI و CLI
🔹
تحلیل همزمان تصاویر و متن
🔹
کمک به برنامه‌نویسی و انجام وظایف بهره‌وری
🔹
پشتیبانی از ورودی‌های چندفرمتی
🔹
درک تصاویر، استدلال روی آن‌ها و ارجاع پاسخ‌ها به اشیای مشخص
🔹
استفاده از جستجو برای افزایش دقت پاسخ‌ها
🔹
سازگاری با فریمورک‌های مختلف Agent
💡
به زبان ساده، Qwen3.7-Plus فقط یک چت‌بات نیست؛ بلکه یک Agent چندرسانه‌ای است که می‌تواند تصویر ببیند، متن تحلیل کند، کد بنویسد و در محیط‌های مختلف عملیاتی شود.
📌
این مدل از طریق API در Alibaba Cloud Model Studio در دسترس قرار گرفته است.
🔗
وبلاگ معرفی:
https://qwen.ai/blog?id=qwen3.7-plus
🔗
نسخه آزمایشی:
https://chat.qwen.ai/?models=qwen3.7-plus
🔗
مستندات API:
https://modelstudio.console.alibabacloud.com/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5851" target="_blank">📅 00:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk2yWyqY0L_QpqEmFK5jeI7UCSRJ7UIYp41s3bWceViwz_4C-iQOUQPOrQbTq9RqHvpeTYQd7d8XEA71v81CSakCw7k8oMwHKBiUQOjXFgMYGmBLmthnRMYCS4zleSPXPcHAha0P8dIApvW8foTHdr0rASWOODWOR6n4BsYzCt4B7PL8Ku0KDko4pNmSAglNYb7Z3bJ4uL7tQx-AwacGuqzDFjPGhC4_6P99M1oDhbKVK-EQ_95TAmSYejPhn1bW2GjlQJHJwXxGrWiI1O8avKmhAYsjKxkF_V4Iov_d7HhNbs4aKkc9ot5pKl0GU6d4Wd-gVTwWdvuMnHwAMo8k5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Golazo پخش زنده متنی فوتبال
⚽️
فوتبال را مستقیماً از طریق ترمینال تماشا کنید
https://github.com/0xjuanma/golazo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5850" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترجمه پیام Void Verge: از زمانی که اینترنت ایران توسط دولت بازگشایی شد، تغییرات گسترده‌ای در سراسر شبکه داخلی کشور در حال رخ دادن است. پس از هفته‌ها قطعی، تقریباً تمام روش‌هایی که در آن دوره استفاده می‌شد، مستندسازی شده و به مقامات تحویل داده شده است. سیستم فیلترینگ در حال آماده‌سازی برای مرحله بعدی قطعی‌هاست. روش‌هایی مانند DNS tunneling، MITM و Domain Fronting قطعاً در قطعی‌های آینده دیگر کار نخواهند کرد.
علاوه بر این، مقامات فیلترینگ گام‌های مهمی برای ایجاد ارائه‌دهندگان واسط برداشته‌اند که خدمات خارجی را با محدودیت‌های شدید به ایرانیان ارائه می‌دهند، یا وب‌سایت‌های ضروری را که نمی‌توانند از روش‌های قبلی استفاده کنند، NAT می‌کنند.
در این شرایط، انتشار علنی و عمومی روش‌ها هیچ فایده‌ای ندارد جز اینکه کار مقامات فیلترینگ را آسان‌تر کند. این مکانیزم باید زیر رادار عمل کند — به صورت سورس‌بسته و بی‌صدا.
در عین حال، مافیای اینترنت ایران قدرت بیشتری پیدا کرده است — مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، ISPها و دیتاسنترهایی که فروش اینترنت نامحدود به فروشندگان VPN را با قیمت صدها میلیون تومان از طریق مکانیزم‌هایی مانند سرویس‌های پروکسی و سرورهای اختصاصی با قابلیت NAT آغاز کرده‌اند.
این مافیا چنان قدرتمند شده است که موفق شده شورای عالی فضای مجازی ایران را به سمت محدودتر نگه داشتن اینترنت سوق دهد تا سود خود را به حداکثر برساند، آن هم علیرغم شرایط بحرانی و جنگی هفته‌های گذشته.
ارائه‌دهندگان ساده میزبانی وب در ایران، تنها پس از دو ماه قطعی، به فروشندگان میلیونر VPN تبدیل شده‌اند.
ما در هفته‌های آینده به جمع‌آوری و انتشار داده‌های لازم ادامه خواهیم داد. اگر این وضعیت ادامه یابد، هدف بعدی ما باید مافیای اینترنت در ایران باشد.
امیدواریم این روزهای سخت برای همه ایرانیان بگذرد. دردی که دشمنان داخلی و دزدانی که به بهانه جنگ مردم را غارت می‌کنند ایجاد می‌کنند، به مراتب بدتر از خود جنگ است!
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5849" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">SNI Spoofing
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.18.35.46
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
replit.com
"
}
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
45.85.118.176
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
shad.ir
"
}
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5848" target="_blank">📅 22:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
آموزش راه‌اندازی VLESS WS با دامنه اختصاصی ابر آروان (روش True CDN Proxy)
این روش آی‌پی سرور خارج شما را کاملاً مخفی می‌کند و با عبور دادن ترافیک از سرورهای داخلی، سیستم فیلترینگ (DPI) را به طور کامل فریب می‌دهد.
پیش‌نیازها
:
* یک سرور مجازی (VPS) خارج و پنل 3x-ui نصب شده.
* یک دامنه بین‌المللی برای سرور اصلی (استفاده از پسوندهایی مثل .shop به جای دامنه‌های ملی، امنیت شبکه شما را بالا می‌برد).
* یک دامنه ارزان .ir برای ثبت در شبکه ابر آروان (به‌عنوان ماسک).
🛠
مرحله ۱: تنظیمات DNS در ابر آروان
1. دامنه .ir خود را در پنل ابر آروان ثبت و تایید کنید.
2. به بخش
رکوردهای DNS
بروید و یک
رکورد A
جدید بسازید.
3. در بخش مقدار (Value)،
آی‌پی سرور خارج
خود را وارد کنید.
4. حتماً نماد
ابر را روشن کنید
(پروکسی شبکه فعال باشد).
⚙️
مرحله ۲: تنظیمات پنل 3x-ui
1. وارد پنل شوید و از بخش Inbounds یک کانفیگ جدید با پروتکل
VLESS
بسازید.
2. پورت را روی یکی از پورت‌های امن و مجاز آروان (مثل
443
یا
8443
) قرار دهید.
3. در تنظیمات Transport، بخش شبکه (Network) را روی
ws (وب‌سوکت)
بگذارید.
4. مسیر (Path) را روی یک عبارت دلخواه تنظیم کنید (مثلاً /secure-tunnel).
5. در فیلد
Host
، نام دامنه .ir خود را که در آروان ثبت کرده‌اید بنویسید و تنظیمات را ذخیره کنید.
📲
مرحله ۳: ویرایش نهایی برای کلاینت (v2rayNG/v2rayN)
1. لینک کانفیگ ساخته شده را از پنل کپی کرده و در کلاینت خود ایمپورت کنید.
2. به بخش ویرایش کانفیگ (Edit) بروید.
3. قسمت
Address (آدرس سرور)
را پاک کرده و
دامنه .ir آروان
خود را جایگزین آن کنید.
4. بررسی کنید که فیلدهای
SNI
و
Host
(یا Peer) نیز دقیقاً همان دامنه .ir باشند. ذخیره کنید و وصل شوید!
💡
چرا این روش عالی و بدون قطعی است؟
در این معماری، کلاینت شما مستقیماً به آی‌پی‌های تایید شده داخلی ابر آروان متصل می‌شود. فایروال محلی فقط یک اتصال امن و داخلی را می‌بیند و ترافیک را مسدود نمی‌کند. سپس خود زیرساخت آروان در نقش یک تونل معکوس، ترافیک شما را به‌صورت کاملاً مخفیانه به سرور خارج منتقل می‌کند! آی‌پی سرور اصلی شما هرگز لو نمی‌رود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5847" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترمینال برنامه‌نویسی هوش مصنوعی با عملکرد بالا
🔥
یک ترمینال کدنویسی بومی هوش مصنوعی مبتنی بر Rust که از همکاری چند عامل هوشمند، رابط کاربری TUI و محیط ایزوله امن پشتیبانی می‌کند و مخصوص توسعه سریع طراحی شده است.
https://github.com/Agions/synerix
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5845" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrDNXej5t_QF2ng4md8dk8bsrXudmxQSa14Y3a4vhrxbTKW9gw5BX3MOLyVsUQmz9KQ89pBBmiJG_uYlEUSIv4Cmd3rqYh_f2nqTjb5hos4ACYK6f-WU4CiDvmrW2sM6rZQajUlWei_qG6dPgFCkfnbyWayWjSJ61DE_7EDWMckLFAwmurK6Qlv3lKTw6yy6sPhFeL8zpkJT6brl6mWY-f0c2d5N-ZFVuTyEyTgcf4f6d4ZF9n3O4FqSNw25T2mCcWOtT7EO0BCsz9PE8LcGHNB85HSqb-Ux8UdEQZvmJmhNNWH9dOsYermU_r3OQX2Iybe9yNYEiCEt6Tp2goofGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
TON رسماً به Gram تغییر نام می‌دهد!
🪙
پاول دوروف اعلام کرد که ارز داخلی اکوسیستم TON از این پس با نام Gram شناخته خواهد شد. این نام در واقع همان نامی است که در اولین وایت‌پیپر پروژه تلگرام استفاده شده بود.
🔹
فرآیند ری‌برندینگ حدود ۳ هفته زمان خواهد برد.
🔹
شبکه بلاکچینی همچنان با نام TON به فعالیت خود ادامه می‌دهد.
🔹
Gram به عنوان نام توکن و ارز اصلی اکوسیستم شناخته خواهد شد.
این اقدام چهارمین مرحله از برنامه ۷ مرحله‌ای «Make TON Great Again» است که دوروف برای بازگرداندن هویت اولیه پروژه TON معرفی کرده است.
📌
خلاصه:
✅
TON = نام شبکه
✅
Gram = نام جدید ارز اکوسیستم
✅
زمان تکمیل تغییرات: حدود ۳ هفته
🪙
به نظر می‌رسد نام تاریخی Gram پس از سال‌ها دوباره به اکوسیستم تلگرام بازگشته است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5844" target="_blank">📅 19:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVrO3AlZPJX3egboNWgPX6XLCyHA7Z8hlYMYpTUvDOnbZKMbrvIc2shCD8svbfJq5AhLf8chx-6UN4dFQq-G0aCwGmGfjjymHyTIsgGdKVeoPlr8g6iednNXQtGIxHOcTxwM5w4L0YInHdJhoQEUgcOYrlH1UI6XSnoTzGsI18eUPIaDK0Oe9dYBZGwDxxg_PGu0TPKXpNJwkvqDhEw3QIPOAOD3pB-PXW5l89QNruTR5gM2aQFGxdfUtNfDRj5e3fNsK3ZW7DIUaGNb2EV5-KOLSOCbeT5gHMrkv3-p3Qsz7l0-YGgX1WxAa-SB6NFO9KrDOYahgv2d-6C_YL4pSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!  اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت [نام شهر شما] را در پرامپت زیر با…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5843" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!
اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت
[نام شهر شما]
را در پرامپت زیر با نام شهر دلخواهتان جایگزین کنید.
🔹
پرامپت را ارسال کنید و منتظر نتیجه بمانید.
🎨
خروجی چه شکلی خواهد بود؟
• پوستر گردشگری سه‌بعدی و ایزومتریک
• نمایش معروف‌ترین جاذبه‌ها و نمادهای شهر
• معماری مینیاتوری بسیار واقع‌گرایانه
• افکت‌های سینمایی و نورپردازی حرفه‌ای
• دریا، ساحل، پل‌ها، جزایر و مناظر شاخص (در صورت وجود)
• تایپوگرافی اختصاصی با نام شهر
• مناسب برای پروفایل، چاپ، پوستر یا شبکه‌های اجتماعی
💡
نکته جذاب اینجاست که مدل به‌صورت خودکار مشهورترین بناها، خیابان‌ها، سواحل و نمادهای شهر را تشخیص می‌دهد و آن‌ها را در قالب یک دیورامای شناور و لوکس ترکیب می‌کند.
Create a premium stylized 3D isometric travel poster of [شهر] designed as a floating miniature world placed on top of a large ticket, postcard, or stamp platform with perforated edges. Automatically include the most iconic coastal landmarks, skyline, architecture, cliffs, islands, harbors, bridges, beaches, or sea views associated with the location. Arrange everything in a compact cinematic composition with realistic geography and recognizable visual identity. Style the scene as: - ultra detailed 3D diorama - photorealistic miniature architecture - cinematic travel advertisement - luxury tourism aesthetic - highly immersive but minimal - clean and elegant composition - realistic textures and reflections - soft atmospheric haze - subtle depth of field - premium Instagram-worthy artwork Environment details: - beautiful coastline and ocean integrated into composition - tiny boats, ferries, or sailboats in water - curved shorelines and waterfront promenades - lush greenery or terrain matching the destination - floating soft volumetric clouds around the city - warm cinematic sunlight - subtle shadows and reflections Add tiny realistic miniature people naturally placed near landmarks or waterfronts: - tourists taking photos - couples walking - tiny silhouettes for scale only - avoid crowds or clutter Typography: On the blank white ticket/poster area, automatically add: - the destination name in large bold elegant typography - a short poetic luxury-travel-style tagline matching the location Typography style: - modern sans-serif - premium travel poster design - minimal and elegant - subtle shadows and clean spacing Background: - smooth vibrant gradient background - color palette should naturally match the destination - minimal distractions - lots of negative space around the floating platform Composition: - floating centered platform - isometric perspective - balanced proportions between sea, architecture, and typography - destination should feel suspended in air - cinematic framing - visually clean and uncluttered Aspect ratio 1:1 Extremely detailed, cinematic, modern, premium, luxurious, artistic, visually striking, travel-poster aesthetic.
🔥
نتیجه نهایی معمولاً شبیه پوسترهای تبلیغاتی حرفه‌ای گردشگری و کارت‌پستال‌های لوکس خواهد بود.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5842" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پروکسی متصل سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.52&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5841" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">trojan://humanity@198.62.62.23:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5840" target="_blank">📅 18:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک استارتاپ هوش مصنوعی چینی یک مدل ۱ تریلیون پارامتری ارائه کرد - کاملاً رایگان و متن‌باز.
👀
نام آن Kimi K2.6 است - ۱۲ روز پیش توسط Moonshot AI منتشر شد و در حال حاضر توجه‌ها را به خود جلب کرده است.
اعداد و ارقام باورنکردنی هستند. ۱ تریلیون پارامتر. فقط ۳۲ میلیارد پارامتر در هر درخواست فعال می‌شود - به این معنی که با وجود حجم عظیمش، به طور کارآمد اجرا می‌شود. پنجره زمینه ۲۵۶ هزارتایی. کل پایگاه‌های کد، اسناد حقوقی و مقالات تحقیقاتی را در یک مرحله مدیریت می‌کند.
اما چیزی که آن را واقعاً خاص می‌کند این است - Cursor، یکی از پرکاربردترین ابزارهای کدنویسی هوش مصنوعی در جهان، مدل Composer 2 خود را مستقیماً بر روی Kimi ساخته است. این اعتبارسنجی نهایی است.
این مدل کدنویسی، استدلال، ساخت وب‌سایت، ایجاد اسلاید، تجزیه و تحلیل داده‌ها و اجرای وظایف چند مرحله‌ای مستقل را انجام می‌دهد - همه در یک فضای کاری تمیز.
و برخلاف GPT یا Claude - کاملاً متن‌باز است. استفاده، اجرا و توسعه رایگان است.
🔗
https://kimi.com
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5839" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMypnebZUIGj_1MDBC0aDlngVVqo9NJPqT9QoEOH2kTxG-81FjE0eT9jHITGbeuFV-yTY9soOdQ8NvTYwdIM_ZRX5mDR30lghU0e4nj-JkEkUOPffS2YKrrQ2J5NByIhqL0v-ULaJhEWdA_Ewp4tSXkohe74dtdNaWy1onecuCObhEJ-sb57hLKb0d3Ddg8HaR9O6OYJzYb46sggZn8KfnUza8bkJiIeIa0lReDW2uU658AI6lft2BSQjExjPrD7G7n7SP01kE75zSt059fymPQeDgSkPcDaAznTACirAU_fdPgkC0iGslYN3TLt8aKoh7f-WItXcRk3XlzIYSMZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گوشی اندرویدی را به یک میکروفون حرفه‌ای تبدیل کنید!
📌
پروژه MicYou به شما اجازه می‌دهد از گوشی اندروید به‌عنوان میکروفون برای کامپیوتر استفاده کنید.
📶
اتصال از طریق Wi-Fi
🔌
پشتیبانی از USB
🔊
حذف نویز و کاهش اکو
🎚
کنترل خودکار حجم صدا (AGC)
💻
سازگار با ویندوز، لینوکس و macOS
⚡
راه‌اندازی سریع با پشتیبانی از Virtual Audio Device
💡
گزینه‌ای کاربردی برای جلسات آنلاین، استریم، ضبط پادکست یا زمانی که میکروفون مناسبی در اختیار ندارید.
📥
لینک پروژه:
github.com/LanRhyme/MicYou
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5838" target="_blank">📅 15:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎁
دسترسی آزمایشی به Claude، GPT و Gemini در یک پنل!
📌
سرویس Bind چندین مدل هوش مصنوعی را در یک داشبورد واحد ارائه می‌کند و برای کاربران جدید دوره آزمایشی دارد.
🤖
Claude Sonnet
🧠
GPT
✨
Gemini
🔄
جابه‌جایی سریع بین مدل‌ها
📋
مدیریت همه چت‌ها در یک محیط
🛠
شروع کار:
🔹
وارد سایت Bind شوید.
🔹
یک حساب کاربری ایجاد کنید.
🔹
گزینه Free Trial را فعال کنید.
🔹
در صورت نیاز، پلن‌های آزمایشی و امکانات تیمی را از داخل پنل بررسی کنید.
💡
اگر می‌خواهید چند مدل مطرح AI را در یک محیط تست کنید، Bind می‌تواند گزینه جالبی باشد.
🌐
app.getbind.co
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5837" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:
* پشتیبانی همزمان از پروتکل‌های VLESS، Trojan و xhttp.
* پنل گرافیکی قدرتمند: مدیریت کانفیگ‌ها تحت وب با دیتابیس KV (اعمال تغییرات در لحظه بدون نیاز به دیپلوی مجدد).
* Sub-converter داخلی: تولید کانفیگ کلاینت‌ها (Clash, Sing-box, V2rayNG و...) بدون نیاز به سرویس خارجی.
* پشتیبانی از ECH: دور زدن محدودیت‌های پیشرفته.
* تست پینگ داخلی: تست و انتخاب خودکار بهترین آی‌پی‌ها.
* پشتیبانی از رابط کاربری فارسی.
🛠
پیش‌نیازها:
یک اکانت کلادفلر + ساخت یک UUID معتبر از سایت
https://www.uuidgenerator.net
(این UUID رمز ورود شما به پنل خواهد بود).
💻
نصب روی Cloudflare Workers:
1. ساخت KV: در کلادفلر، از Storage ➔ KV یک Namespace جدید بسازید.
2. ایجاد Worker: در Workers & Pages یک ورکر جدید بسازید، کدهای قبلی را پاک و سورس CFnew را از گیت‌هاب پیست کنید (Deploy بزنید).
3. تنظیم متغیرها: در Settings ➔ Variables، متغیری با نام U (حرف بزرگ) بسازید و مقدارش را UUID خود قرار دهید.
4. اتصال KV: در Settings ➔ KV Bindings، دیتابیسی که ساختید را با نام C (حرف بزرگ) متصل (Bind) کنید.
5. تاریخ سازگاری: در Settings ➔ Runtime، گزینه Compatibility Date را روی 2026-01-20 تنظیم و ذخیره کنید.
6. اتصال دامنه: در Triggers ➔ Custom Domains، دامنه خود را متصل کنید.
🌐
نصب روی Cloudflare Pages:
1. آپلود فایل‌ها: در Workers & Pages یک Pages ایجاد کنید. با گزینه Direct Upload، فایل Zip پروژه را آپلود کنید.
2. تنظیمات: مشابه روش قبل، در Settings متغیر U (برای UUID) را ساخته و KV Bindings را با نام C متصل کنید.
3. تاریخ سازگاری: در Settings ➔ Runtime، تاریخ را روی 2026-01-20 تنظیم کنید.
4. دیپلوی مجدد (حیاتی): چون متغیرها فوراً اعمال نمیشن، به تب Deployments رفته، Create deployment را بزنید و همان فایل Zip را دوباره آپلود کنید تا پروژه از نو ساخته شود.
🔓
نحوه دسترسی به پنل مدیریت:
مرورگر را باز کرده و آدرس دامنه خود را به همراه UUID وارد کنید (مثال:
yourdomain.com/UUID
). در این پنل گرافیکی و فارسی، می‌توانید لینک‌های اتصال (Subs) بگیرید، ECH را مدیریت کنید و آی‌پی‌های تمیز وارد کنید.
🔄
نحوه آپدیت برای نسخه‌های بعدی:
* اگر از Worker استفاده می‌کنید: کدهای جدید را کپی، جایگزین کدهای قبلی کرده و Deploy کنید.
* اگر از Pages استفاده می‌کنید: در تب Deployments فایل Zip جدید را آپلود کنید (بدون نیاز به تنظیم مجدد).
📥
سورس کد و دانلود زیپ:
https://github.com/byJoey/cfnew
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/archivetell/5836" target="_blank">📅 14:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آیپی تمیز کلودفلر مخابرات و ایرانسل تست شده
45.130.125.96
27.50.48.49
208.103.161.170
45.130.125.0
45.130.125.160
45.130.125.69
66.81.247.155
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5835" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۵ گیگ کانفیگ از پشت cdn رد شده همراهم میاره
vless://6053415d-763c-4132-9445-e4a0329a594b@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--cdn%20-%20tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5834" target="_blank">📅 14:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۱۰ گیگ کانفیگ تانل
🔥
vless://a5400c9e-2f0f-41c9-aa4d-5a77c0787af3@cnxman.ir:17544?security=none&encryption=none&headerType=none&type=tcp#tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5833" target="_blank">📅 14:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">1 ترابایت اهدایی از یکی از ممبر های عزیز
❤️
vless://ZoRoVpn@104.253.18.220:80?security=reality&encryption=none&pbk=D4tCeuAMOZViac1SOVD5ABdN86EkAn9ql3NEuQlneXQ&headerType=none&fp=chrome&spx=%2F1vwstnEi2HFdu63&type=tcp&sni=www.yahoo.com&sid=88ab02c0#1.00TB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5832" target="_blank">📅 13:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVhsH8ruStasL-WeoiVRYMFSGb3Tcmy11WChxLssHNJRcjFoLA5Ld9SdxZB935xlttpR7Due7RweLt_D55J7FRWiBkHjrCRFTAjfJuf0Uj-DanEBTY-Zj6BtNJ5GbBlkexwRl7LB4C2jdWNhsJTgGOm--t34sXroJuKWt_l0hmpQZu5wthykzgh9P5kfcmYMjg6kFJNZyfnGffQaWUUoGIkCKQSJ8pjjIYGkKGsX2_Ksw-pJYiH9oRXlGVT5uPZ9iK4EPr5Zw3cz8r8mjhXpIq_kr4KotZHp6S765sFeu9ob6jmQAPKbkDjlIn3BqYrYWjto6FUtwxHaVt4abDYDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3e809b21-e29b-49ec-a7fb-5301ec7c1cee@food.artmisserver.site:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#Artmis
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5830" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkvNGhu5ew2sXyO0UpwAgzFqtYwM8-XZep8xbGD6We53Me5DDNuu3vhrr2mlmoEZKve1UxTgjvQDiKZAolwM8dNwXSBqURODfyWmirinbKvuZjQhkB1B6uHJV4etKFLMB9UUGGxphICu2AOH80YHKKyrSW8Cm0wApE7GY_t3012zjMXDg7k13QYvolZdpPyLGC8V87D4aCPg-beqGkB2Bh4EkVqa5_ofc_0-0ATihrCKy7hCXyNGjgwUba0Iv1gtWQKa1QeNj7AuMop9rkjt3h_hyt_chkcRj_mR_2gxVKHYUqNLzsXP0iKI5buMvPSV0dXtLNKrcSygdAruYfubig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
تبدیل خودکار هر صدا به متن و خلاصه!
📌
ابزار DeLive صدای در حال پخش روی سیستم را به‌صورت لحظه‌ای دریافت می‌کند و از آن زیرنویس، متن و یادداشت تولید می‌کند.
🎙
تبدیل گفتار به متن در لحظه
💬
نمایش زیرنویس روی صفحه
🌍
پشتیبانی همزمان از دو زبان
👥
تشخیص گوینده‌های مختلف
📋
تولید خلاصه و گزارش از محتوا
❓
امکان پرسش از محتوای ضبط‌شده
💡
مناسب برای کلاس‌های آنلاین، ویدیوهای آموزشی، پادکست‌ها، استریم‌ها و جلسات کاری؛ بدون نیاز به یادداشت‌برداری دستی.
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
https://github.com/XimilalaXiang/DeLive</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5828" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">0BITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5827" target="_blank">📅 12:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://9e48e5db-e5cb-462f-ab0b-6f573aa73728@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=941935f2d0e82539&sni=www.amazon.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5826" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🕵️‍♂️
مرورگر شما چه اطلاعاتی را روی سیستم ذخیره می‌کند؟
📌
یک راهنمای فورنزیک نشان می‌دهد که در مرورگرهای Chrome، Firefox و Edge تقریباً همه ردپاهای کاربر روی سیستم ذخیره می‌شوند.
🔖
بوکمارک‌ها و سایت‌های ذخیره‌شده
🌐
تاریخچه مرور و جستجوها
🔑
رمزهای عبور و لاگین‌ها
🍪
کوکی‌ها و اطلاعات نشست‌ها
📂
فایل‌های دانلودشده
🧩
افزونه‌ها و تنظیمات مرورگر
🖼
تصاویر کش و فاوآیکون سایت‌ها
🛠
همچنین ابزارهایی مثل Hindsight، DB Browser for SQLite و LaZagne برای بررسی و استخراج این داده‌ها وجود دارد.
💡
اگر کسی به سیستم شما دسترسی پیدا کند، بخش زیادی از فعالیت‌های اینترنتی شما قابل بازیابی خواهد بود؛ حتی مواردی که مدت‌ها قبل مشاهده کرده‌اید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5825" target="_blank">📅 11:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤖
یک لیست طلایی از ابزارهای رایگان هوش مصنوعی!
📌
اگر از بین صدها ابزار AI نمی‌دانید کدام‌ها واقعاً ارزش استفاده دارند، این مجموعه می‌تواند نقطه شروع خوبی باشد.
🎨
تولید تصویر: Raphael AI ،Krea AI ،Magnific AI
🎬
تولید و ویرایش ویدیو: Runway ،Kling AI ،Hedra
🎙
صدا و موسیقی: ElevenLabs ،Suno
💻
برنامه‌نویسی: Cursor ،Replit
،Bolt.new
📊
تولید محتوا و ارائه: Gamma ،Napkin AI ،Notion AI
🔎
جستجو و تحقیق: Perplexity ،Phind
🤖
چت‌بات‌ها و مدل‌ها: Claude ،Poe ،Hugging Face
💡
مجموعه‌ای از ابزارهای کاربردی برای تولید محتوا، برنامه‌نویسی، طراحی، تحقیق و ساخت پروژه‌های شخصی؛ بدون نیاز به جستجوی طولانی بین صدها سرویس مختلف.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5824" target="_blank">📅 11:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">80 گیگ کانفیگ از لوکیشن های
🇳🇱
🇫🇷
🇮🇩
🇩🇪
vless://aa918a17-0c07-49b2-aec5-b72809d91a17@185.211.101.214:38200?mode=auto&path=%2Flightyagami&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=JL7JvLV0E3dvB48lp5UpSyzx1ATHPS3Kgjv2Ox9HtjQ&fp=chrome&spx=%2F&type=xhttp&sni=www.yahoo.com&sid=4306#OBITO
vless://c649466f-e700-4d78-be2c-a9d915434f34@82.40.62.67:80?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=49a5ec2ac3&mode=stream-one&path=%2Fm4rg&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=QWHdk8IaYGGm_CkKaBTLeLlOKhFGLx2pA3qBBRmiM3Y&host=light.96s.dpdns.org&spx=%2FMwzynVriGAhj8A1#OBITO-20.00GB%F0%9F%93%8A
vless://1b16b6f8-b8dd-43d7-84f9-8eb8a7e15504@sina.35o.ir:25645?security=reality&encryption=none&pbk=GnAQ0pqW4HGqMuOY7crTmcQ56FuABKPP9YaiJzOS3X8&headerType=&fp=chrome&spx=%2F&type=tcp&sni=www.yahoo.com&sid=d6372f1a0a#OBITO
vless://0c3f5b49-d0ec-451b-bf30-f50e229b645c@panel.96s.ir:8080?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22initStreamReceiveWindow%22%3A8388608%2C%22maxStreamReceiveWindow%22%3A8388608%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIncomingStreams%22%3A1024%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=775a6745d1&mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=0ySdtEa5hyO50lsKB3FdbcHaGCn0tw6BeYvabtJpb2s&host=panel.96s.ir&spx=%2F#%DA%A9%D9%84%D9%88%D8%AF-0BITO
@Sina_1090</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5823" target="_blank">📅 10:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حذف واترمارک ویدئو، PDF، PPTX و اینفوگرافیک‌های NotebookLM به صورت محلی در مرورگر، بدون آپلود فایل.
لینک:
https://notebooklmremover.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5822" target="_blank">📅 09:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گل سر سبد ربات های سرچ تلگرام
@oksearch
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5821" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پروکسی متصل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5820" target="_blank">📅 09:19 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
