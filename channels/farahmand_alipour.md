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
<img src="https://cdn4.telesco.pe/file/qqM19uY9OMTMV5DfoLRy8kAIbQJs6_Zb0ry_fy3Ug2rT2oVpchKhQe9ysElDwDDCBG0XQAb2ypPkzyFN4jpmr1y8gXJpkqdEDtutTIktX6LnjyoYS9oAsCCYqshZDVbpJARc1vk-idmWQ38UrwXe5w_Z12ZtiwNga1QeZ1B1xBVvuWPzMCVIuUEHyarqiLaUAt8e71cuKwq5pJXPhEwR2w--HWTBsSiElWxl-XLTDjtrqQrf7sca9TKl4SodnBw7nki7Qj8GbCJ95YY3-ExUXOx0j0i28vB7VrqnLt8Qb1PONBS-ruQav8-r9wAdTclBAhPhVUxrdqMMO5CWSTIVLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 21:37:21</div>
<hr>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=dGG2BDRcGTvmS7JvCGwze6twsoKwbTBTHYI1STxlNBW-uSC388cyTSFDPwxNAjUmlD0txro9h1VZH1uFOimAe-aBi60CaB7LOW6zcnTAsxpjvIG8O33BzFP6QyhIGgmyFCJEA989YoBZzcvZ20HDGWLwNzrNz3Ed3MyfD0nTJ2f7kUldoNQyhDinpwkm6IfHphfBnivAoM_YMTMuv6vEFbAVKV3IIypGLiRl1JPh3Qboe-gfyDB7Ancuxyu-rDP-4ohzcoaxPGDGwKov2AmwFl1BL6VnQ0mJprQjJDPRM_H8Dhlu26XD0Ntrsl9qdW48KY_EbyX_c3BWZDJLPgxoQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=dGG2BDRcGTvmS7JvCGwze6twsoKwbTBTHYI1STxlNBW-uSC388cyTSFDPwxNAjUmlD0txro9h1VZH1uFOimAe-aBi60CaB7LOW6zcnTAsxpjvIG8O33BzFP6QyhIGgmyFCJEA989YoBZzcvZ20HDGWLwNzrNz3Ed3MyfD0nTJ2f7kUldoNQyhDinpwkm6IfHphfBnivAoM_YMTMuv6vEFbAVKV3IIypGLiRl1JPh3Qboe-gfyDB7Ancuxyu-rDP-4ohzcoaxPGDGwKov2AmwFl1BL6VnQ0mJprQjJDPRM_H8Dhlu26XD0Ntrsl9qdW48KY_EbyX_c3BWZDJLPgxoQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fdlLF1PqfzAuZc4PnNdtWgvWGTSseVtw18uVVQE3XIp5rvFLeriCGl15-xQmHZhDaBLbfiyO6VycxEQxOKte79TEMC1xbt1nbwwPCjNMN7BdMLfbasx_VLl1HjWxhHaT2hkBg6PHOrbGYBW8QUScy9r30VbmCLIiANor1Gv6BTIIWnC6t29cVcjsrbm2N6QUnZ6aSq9bNIfPVrOloAkWvn2Mb26WlWeEPeu6uH7VGpMe3i5mNm7s1RXgdUAf1ovRrhV768PjfcVqYVF0HMtcsoGsmbPxOe2lUknbP7Pf5_9hI8mGiWe_yfM4U1d_lqBXLWPBU_uhMj2ceqE4RvagSgKqccMuQiKG8lE4jBXrCxLZRZLsPSa_PTURQP0bBESXmEQEkDlh4kNX_vUQ1egmnjQcHWWVjb6L9Rll5nmCTaQRUJHupJMQeXIS10kSAJXKguCUAExlyS2LJz9vWjwBwgNw45-_gyjw6n6Cn-VwN0-YhRVS2UXEPum49n6LKHKqIE9gd-_3k-AHiZxcKIs5zBKbk2voSDw-dgt7cqE5AHLxQ6IqczP0d9yUdW0HxM6UEEKeiiAgVG2jE0J_8hfd3qdShxbE1aZGv1IKIP-rg2Iesj1KM9q3te-ZOP-hP9eC0tE4uH7O0Wn6CsZqLZOcjhad-sUSIShVuIHRmttftH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fdlLF1PqfzAuZc4PnNdtWgvWGTSseVtw18uVVQE3XIp5rvFLeriCGl15-xQmHZhDaBLbfiyO6VycxEQxOKte79TEMC1xbt1nbwwPCjNMN7BdMLfbasx_VLl1HjWxhHaT2hkBg6PHOrbGYBW8QUScy9r30VbmCLIiANor1Gv6BTIIWnC6t29cVcjsrbm2N6QUnZ6aSq9bNIfPVrOloAkWvn2Mb26WlWeEPeu6uH7VGpMe3i5mNm7s1RXgdUAf1ovRrhV768PjfcVqYVF0HMtcsoGsmbPxOe2lUknbP7Pf5_9hI8mGiWe_yfM4U1d_lqBXLWPBU_uhMj2ceqE4RvagSgKqccMuQiKG8lE4jBXrCxLZRZLsPSa_PTURQP0bBESXmEQEkDlh4kNX_vUQ1egmnjQcHWWVjb6L9Rll5nmCTaQRUJHupJMQeXIS10kSAJXKguCUAExlyS2LJz9vWjwBwgNw45-_gyjw6n6Cn-VwN0-YhRVS2UXEPum49n6LKHKqIE9gd-_3k-AHiZxcKIs5zBKbk2voSDw-dgt7cqE5AHLxQ6IqczP0d9yUdW0HxM6UEEKeiiAgVG2jE0J_8hfd3qdShxbE1aZGv1IKIP-rg2Iesj1KM9q3te-ZOP-hP9eC0tE4uH7O0Wn6CsZqLZOcjhad-sUSIShVuIHRmttftH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0lCcbE_hdZTWgj6kJVfGOKPdahpYon1kuntesK4pNBmaCryBSWd_bWxto8r-HuUPLtod9HdbtR0L-jfGZf9S92sKNHBKQAdaSmHNB3E90pvl0ST3-sq0OYvTCoJDi1KHTeIwEu9Wq2GDwmawBSKyN9kBUr-NvZNINFyj0ShYbMQWy7n0FH2e_Ukd00vhCuFuxgFIOzcdKoss6_zrsksvjbzUrHYomd6I9BUIngIlX9Dz_eJe9hMgm0IGoxq6SRaIrtm9PJT0coHWGRfRSZ8Brp3hOM_QA24y4vy6is33QXuvoQt_4ULdzwnpH2Q7wqZsQQe1OvXNW3LbfjeDxjGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U__yRCJpvI112pHRmV0FUw9pJR5L4-7H-hjwRQ3m1od_0En6G60rujs1N49TgPnwP7w0J6zomiRevFBiTHW5-W-fHmh15lWyHZamGw7KPQvbCgqPMowdkdVSIcLZjFz8WvT_4q7ajCHGgUfzYn9ZVyM0g1jeh0zS0UWbZG_4M654yYkNBc8WIPRIY0tBzmUlYUKlul_up_GHcCGU6aFeoGK5Jh6RbrpdmFuwF6AoMLtd6_pEXarwn-rUCCZ5Pv9xoTZMoJLuGQXWElXLgtHLCZAa3rGcGE3dAatmSSq3cxXNX9X49R0KTlgxWsFNhlZSLGnE659pEJNDv3nO2ACjvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJypucycX-DmyXn2yS2TvRFYMXXyzSph2AkMawunmf4N2pgBmwi99OHwBwyXxWl67_lUVcxCmYrBKDyJhSaorXd41TUAIT2mof6guilnLHiBRUE8JGUbtdufTSXmtEug0sZQ3eb9s8uKgaBoDgLJrtlryRk5a-483BcZtyBLhkjRiXQoxsYEp0_GS3Ff-ylyqwr87dZaqxtVxo-a7Pr-P1VdjEQ6nSp60t_hrZKWSFjW5_5MUH0wKj0QN01OVraIK7TQ8MwlO0EvBimm7oVlL-qkmrS2JutqqZdfWMX3TZSX9BUu0_-Jy4CIYBlo7yF3XVq03WeAmgg3mEUUkU82SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPMtRew9wf4hHdG97oRtD4trIY_5GhstjrYkm88M1VoCNI370F3wJqWA1031BX9sGp5qoOm2-XZinnp5pJ-voqRjbEudRpAGp1ZAAM7mu21pZ1JgMlNtdLIpNXudo7PYWOQ4LumbU21Sss4aaoZ6Nw457HkIWaiKTvPfQMyCNnSDep-3ICteM7rTMmpXDMi30X2hZsBBJZMA-9cy8c7kPSrny1tRdQ-fzXusFUzeoH2Ja4KRXjwWSBh8ALvq5aLFLud_5UfeBXF_Xmq7yqSd3HnqetW2UPXpheptxbKbrfDSxfnOP-QsEzTmsNHuL5pMgMruJcQLIpMUd56yl1CIsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-n3B59qGyUjtkXbCtnY7hdqXyuNuOYoJGm9zIiDD43kucloUsxINq4Ug2sY_54CHDhTlmeV_9lyQaKf7wiiftgy6QgQlKbXAu3M-JNvq3XZndSlj-LRObhhZElnjHrVWS7bMwKcjqgJ41UkYeR0M6GjXg1RJCTaIELwaUnNUwqp-avTdbN0zpM0NOlYvs5LgPeIoO4Xe25KxCCvGPngn0mf3_iIBzZyKRKu5DMM0aSoTmtHuZVflQVs1cHmprzRRhgjOpInp1oTa94wiaS_oBJ5-HIrIF3lECPcklh-Nw3WvvdqC72vQqKDDbbhbkSfnIeALqs_9oIOvaSWRgJTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5M-iWlxZrHTp8IMyRPUi4bQ0Sd4gzG7gixY8sYWtS9VnM8Z5Ni42x-jA-pRoBnSo__lc_gWoh7-Bvz8BxiQNwlkKlW5z2Q2m4I6u_kBPc9stlbx42OZiyeVG4HA4WfQotxB-P7m4C_-u4-w736EByYrjDE1dDSBZxEM754WdAmFdCj7dnW5wWzaHV2BO1J-zk3xTlp-N2-AvvmDSfMXyLPsws3gKhKn6WcN3WyvW6xDLlkKAYbqyvPYs_HQuCJJ41z8mBTCSpU1w7MD4vQYOBar2W9r2p9BJia0NBRf6IcReXpIXB5yR0RuwBGy8hsuS1f96O73OyktqBQDRoZWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9RNMvfzPb8aCFkcAObeEl66HfRV3ehjwcoum1arNky6f_Z1Jh2UV-zkdG9g58HcvNJy9_81xkAA6b27Gdts6fxvG1UvcuN-mREXoon4THIJNKmVGPhHu8ky21X1kvZp1V8Qvy015sFp8pnT-XbVgwf5-MLTE6UQxi2MJOLOkhaPgUEHYRRn4IjLYkz5Fro3UG9iqG34PwwEi6oqIqcsiOghfMkLe9CUpJ_Mhy9_IsANMz4YGrIgKi3wdj_KAos2nJ-2_cKF3MFfqYFepRq88PavTXs6jrb3veO3y-ZirlCWnYj7MAkGEwyZmx2OjLArhZHF-D29SIXF2SMwICZA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWRQQDqlfzhCyxR5C1oMIOthhJOspqnochOT1sCwcYMTZImt6j529Quf-YT6bCqO84qzeboZcUDL5hC5a3Oi3LU9HdWbA6c5BrtMGqd_bDqQdr6AGnSyY2jqh1B__wVt9KOrYYgjBMfVKanhCWbqkJOpaasWC0VnjOEtbdZTJwF7KOeJDgRUP4EdRTi7OGz0D59JypWLhQmuo1G4OJoAVH5PaamIzUy70oo4nxLZEL9ErB5jN4Yh3CaKmTbrLE9_QPGQ_1PkoB-J4NwW9S14Cc0hxxeWZkUhosmpJ7GbjasLTW_ycF6m33RHC9158XfyK3VKF58hwaQxe-FkZF8oRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh4PVsKx9ChgKc4BcK9RoDbHUw09wPusDUj3wVOg1quYMI7gvjko7kB7VBmMqV7AZZLHZoXIkkqCF_V967_vV_ZtwOunJ-sRzAKHBN9L9jDKebeLYTqcSKPuHWsO2P4Yt46GDcTG-e2zvz28U5AFU5J_cCCzw5m-dNsQXC_iH9sN-iLQcaL6IA2KZmANlFvVtNC_13g3onva8MuCd--Bqqag0KsLsiEPu3qa9ifUCt50UeBZsjDFcrR1Q6C09lMFtQAVcGtlTW4SihmrUFSUsy4kiBm31bKUu8ks1nkHpPlduVnbUImLLERV8IBoERmPEEc0JTsgih9EJNV7fUzv-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocikRse9uMmSOq8myYrDV0wYdR0NIUAy0mUKcjLrG4yGFRFZUiQRa0b_OHhm98CCBaVChXNCjpOFnIsdEpfyX3khAsvzsnplDMX1tbMJ713uLc9tThVED-9gELlLf2wnnjmkt2UHP2W7uroXnafSBQS5ip_OdgxbpYWHXod0S3rMryCmMXRa3Ik_uimReLqfWAufFncDnXfzIXASLSNahaM_qfZs3LJlo3oWxZNQULnh6UpN9LmMIPaBe1lwBFR42C7QvBJ1YJrvA6u081bGXeium2zwe5UQ_EZmLo-4BwUewbY5m9EW__YUF60BxL3IGD9gZklO-h-zbblvp7IySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJS5e3UOIiHiXf6TvpKnaVk-xCfT1iwmdic7Hv3R6EFYA6TGLyDHx-lPFbjl-Jy122XK6zIonTuWezuKeC8ESG25WDDOSRM0hDCIS9UXmCS9NxFAzo8hbGJRHt1YeFvWJ2iy-aE2o_j--5khUWyxCWInTScd_AlDsYQo-oL7hWzZPXjGYfoo-nS71mbxkvPYeiM50fYqo_l1AwpPfFFJdlxzj9c_9CZRPnrBmI_2pnayxJU-Fo8xWCuzwgz97LZsaiNNjq4s3PNplhDYE0A7oebtQC4xJSZC9RD54QDojmXLusaFz71HyTZkr0PZ5CZjkBu6ySUfSA9qaiachKllMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ky8rtnNzuvKHTesr_p3X6-snJlnYCpmyjcrnF8rE9cB3uW6yqxXuGB28v-PxqzkP9h_ys2CAEOHUXF1EMNn3bYqANHlPXr6cTsWn2X6thhevh40sjv1uAzMtiavq2igyiWusMaZYhRFb7ko73p_RIUrSwr9xEKbsHYHZZ0iIK8MbnlZBsCeTS-HzVgouV3W9FY16minnlTrUmSpyE3P9XrqHZXkg6iXFSjovr9j4TAB2ocSLjqkt2WlOJfLDMnF68YwOUArye7BKAjGQkraigZ-4_UYUJLo3Uqwx7AiGbx_TzPRFTqd7Sd_Cq5qMq8sDNLeYo9rd_FNQTBYFqz-RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_Hx6_W4vuKtfBo0yKUYv6nND6aw691_Drsr7G-caJNNhGKoWxm7RxIxat4IrxT01r69O67u7NzrdEFokyoJFXVA3Bg1hO4cx_mEfhdaNiCdfPxcBT-f9K9ptIZBsR7UaCQ8Z2193-IRMdIDjotAeff6xYdWODHke9d-qgGrZNArWvxkCCcmc1lt7wcXLfSZip228i33uKowhx0knTVINAvXVSzNeIsu4DrGqbepqKnjER-_6eCVYd02fTmiMJR0CiBgyTfB-yM_k3RZ6Q6zmrM7qP7gICMm0Zy8o0iD0cs78jVhaOvnZnSBT71369ZEAW2Hfpw4yu9i7M31oq6_aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRJ1hXcBP3HmzmMWUTdA5jX1OyXh7Vmx6brXpXtzkuIFitwtppKs7SALlgC6rAez4k6bEBCo9z9-BgUYLN5v9qLQNzc5tPt8eVf0P6USuSwr23cBTCYLZeepe4Rx7AzLZeY_OkCGTqIXjbhZzJdz9nsdtpXAPhKIPCYJVpzO7uUF9PI2QQ5QKatdvJPBaQn3gY148-M4t-sWG2206mNrxoZjRB-0hOwoPIVrGvOJmKUV_7lrdPhrubQb_TtP5egXIitb5ZUzC5ahuhaGDox_VV0NPsMKO2cXUT3MOSQUc3TZXRbb9GFPuRn5YEOP2VI6tw9eHZYTbSqN7NRasph7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWAJ0gG-u9cNR2W5Pzbe4UB8RpTBJ1Mc1xt6rmDP36e2KE3PmKgX4-lvxyFCYIsP12BjTTrac4hifIholM_iwtHXskeeslK5-kBGOUpk47GLCYIgyGh2TEj6zytTtN19mUFZgf5Q74FK-d2XMFGOU-S_VX0AXJDIDSr8QPEs61qH9C-ZBaLZ_NK7_FOYBvDBiLYhqmky6FaG9INB_oUhf7FisEPjCa9KQ1ppOk6-nS3AfXeRTdWllCu0iOLW2RuwcDBYADjbDs8DwXi5Fn00zhjSrO941aoOUFTtTmTow1fS66M6iGB5M_Axc1PlRf_ARoM-jc6yhztMV1gS94Rn0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPzt1UZFRIoGGakbZJw0Naqf-AvN98HG0g0eZy2yTxUgWFq6NqQNg84BqfLRC1UkwsuyfYG2P-MKh0PRza4t-FkzfD3EGJn2pG4Hsp29GHv-HjMwcvPN_bs77-Qmh9T5PJGzjnEdjbb2X1RFvrApjVMPlV1yEP8_oEe6_WgaF7ZuMy3yyU8IomQOV1L2nubPiEewhckx4Y7S3iw29TZsNo_2GF_avJiyDtfmuwhorTQcNYCKy1_hD9GH-yywceN5Gka9-UX2ntKH_GgDUSC_kWf7k35n23AabmqOG2IhukJpxcY5LYkQTvvjyRcJNsoZMwlkPu-W63zYC79j2RqYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=h99XJQZVaRlSIqDdvC9NGyeUOxy7i8aQJt-euhPQ_6gtuttx4kQcLSiU9_JjfWGHY7xXDHI-83WMQsXXY-tjBDv1uPFA_PjNgM78hXh4-Tx6gkz8dyoyWC2RyC7uwVnqn9L4JQvNJWScs2A7eXfnIXZbs1pK9TRWNJ2-yHYKbu1tfYDqCGgMqib8k21DULNfR8scCTxOGgYpiNSfEWCVnV7b8F-eIqESD54-cPc3IfuUAZiWe1-KuXNiEWXdMN44ZGXAHz7sCdbSA5WSY5zBO0NIBa3PXWLeQiqme69I9CIKAw0vPAISrEpKH3IwoM9hxcySnjH0Yib8uXOPPxegrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=h99XJQZVaRlSIqDdvC9NGyeUOxy7i8aQJt-euhPQ_6gtuttx4kQcLSiU9_JjfWGHY7xXDHI-83WMQsXXY-tjBDv1uPFA_PjNgM78hXh4-Tx6gkz8dyoyWC2RyC7uwVnqn9L4JQvNJWScs2A7eXfnIXZbs1pK9TRWNJ2-yHYKbu1tfYDqCGgMqib8k21DULNfR8scCTxOGgYpiNSfEWCVnV7b8F-eIqESD54-cPc3IfuUAZiWe1-KuXNiEWXdMN44ZGXAHz7sCdbSA5WSY5zBO0NIBa3PXWLeQiqme69I9CIKAw0vPAISrEpKH3IwoM9hxcySnjH0Yib8uXOPPxegrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpDV340qTDvwuChr2855V1MjYfhxkl8T7uPJ0CWl3Y0BOoyj-fkR_AZwfuIeUHmN6daCyz77-6d-jbkJyIhGHYMgmWAqr6h9ny68MFqTqU4-TiXJdmXp5hBSys2GTkoVXywTA4I9rTImIVbdmH8m2KYraml4lRFdcri-YKy1sp4SC8Ny0vqkkSnSXBNvIQMzPnhTFgtg8zMP8tuxBy4YlgJB7myN0bfxVvoVmiHqma9ef4jVRc99e0_GjX-zlKs0LpSZih4YKEPIfBgw0fkuc43nomhFrqfVIpsmeNLwxGUhvZQKqZRN5BGRbeqQZ38-SGQRKSK_4ybk5EIbawtmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkQKkY8dXU6yeWAmuYtWDuc_i4-YX_Ivi4NcuBdsyNzF7i5xy74dt7iZpau-qDXJpvhlRdKWjLITg8ZMyrJnA6IKM938u7Y2DZnshbml5vA6t9T-sPjjbdsQA4Zr2s-ucjm4fLr5xwQTCKa4N8n3QPUekKSXTpE-lMPlSBJN3TbpgI6IbeaDFwi9xsLB1riIMeG05HmCp554zTKN7zCdArH0lQAl1p98hSSW0BNd7HWPpMxmklzZjnXGJ8ET7kA-wYJm9M6hyNiQAhg_1nYG2NLBsj6WfrgUGOVvzEELuo0q57K0wYOc-CQaO_qBIU0FQy150_nQYPLd_xfXULOB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XysqOgNzdb10LbdXVX6tDS5RELgUVNVVnn3PmvzNsk1Ca-F14OtmH3503FVvMIld2z8lsxbWidEmu_wskM4VD4imKoUjw4FNg-j9MMcfp3pb6R-mkwQIMO_JpOyXreZjjqd00Kxb6-zkKaDZT_lrm5zsCjjf7ax2Pp-q8hvAH_diUJnlHd6yiCBapekrbPPPHrcHZTjUiyf7VxM8tNWvMdLeHQ-1CC1iXVIjH1uCqmuHR9HmXHQUAoi4DDUzTW8Vd_ghFGItCttyqN9SwhsKKHiuWwbefYTZEOGsmIezlAinPu2gKDKTtTcR286PxzPSX5qpeSafLWYTCocndaKfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=o6dVgFDlDGfryLAdycWAUwcbEJ42mdrZBasY2vnNPSCBfLGoppKUGfsigAM_10ISdlEhvJi7blcLS7C-65BTZvkbO5KJp8uLENHvHd2aFSgrbJBpwUiWU47txPdut7S5Zh_VzN4UZKg2evqrpk-9elH2Ggaueor0hHth2Qfbhy_-VK6yTlc67nHDnuNDbZD_Fr03-DCkQ7lW1ChFJ0q04en4SReFzXRKihnqmkD8FlawIjIIdr3EwtTLFaASln90OSohUazWCC4Te4ZV8AEKKq5-mXDYN7Kz56ef3nA92Pb0K1dMpNxBo41RpkqcvrnYviYckljY0ZhInSPilByJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=o6dVgFDlDGfryLAdycWAUwcbEJ42mdrZBasY2vnNPSCBfLGoppKUGfsigAM_10ISdlEhvJi7blcLS7C-65BTZvkbO5KJp8uLENHvHd2aFSgrbJBpwUiWU47txPdut7S5Zh_VzN4UZKg2evqrpk-9elH2Ggaueor0hHth2Qfbhy_-VK6yTlc67nHDnuNDbZD_Fr03-DCkQ7lW1ChFJ0q04en4SReFzXRKihnqmkD8FlawIjIIdr3EwtTLFaASln90OSohUazWCC4Te4ZV8AEKKq5-mXDYN7Kz56ef3nA92Pb0K1dMpNxBo41RpkqcvrnYviYckljY0ZhInSPilByJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv5YzJTs28LhDMcRfgBwbZhk6IMQwPcOkJFJ8GxuF7eobMpJSTWQmeAV0N3k76qpPK67ekdz6K3mDCAu-lcl_XgcEwqA4nZSokxLmDuC-oMbIZGQji_mM3t0eM6v5ug7ZYYmJ5_zeG2P79yFHdeMP0ywWPKdgqSt1BbsNx1xrXqYUDmzK6ILhjKPKphU6aRKnHGd-xG9Cu5ikGgtpFeuBcCK8Zjok_ivc78oqLjMXhCrKxN2Tm4uOeFACwADVwyoaOCWnVEuDkJ-gdDbVEt1FmqZqgnjAasoqq3U7yU-YmYDPLVW2_K74jF8EVs0S2k1EHPstmciXSSeQFPIiNboNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=VIbdwwxOf-kn09sLnW1rMwPA91Kw9S0F5S3DTdNIm6gAwi-s0iixNnyhJriXQWE6dPre3CxMGufDEeJjvmaQofb93mNBO8EI8x0r6xJt2F_OB0jPWwG7EDlKX_J7LluVX1HfYnMpPonrVbur_EfU6p4LZ-ocyFrNVXZj-Nb_CIc3gVputr8Tk_S45ZbvxOkL2xmI4wNjKrZLH1W8wHXLI2a1jyZBLweAdADk3p_a7DEQsdkhluVKA3RPjH2gsfIlpfuSfMhszP45IE7E2YOQPp2szFNvatpIRdYn1VgTuYOVwO5plVyv7vH3gHrSQtB_z6xWYQToe6MxW1T5s1JA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=VIbdwwxOf-kn09sLnW1rMwPA91Kw9S0F5S3DTdNIm6gAwi-s0iixNnyhJriXQWE6dPre3CxMGufDEeJjvmaQofb93mNBO8EI8x0r6xJt2F_OB0jPWwG7EDlKX_J7LluVX1HfYnMpPonrVbur_EfU6p4LZ-ocyFrNVXZj-Nb_CIc3gVputr8Tk_S45ZbvxOkL2xmI4wNjKrZLH1W8wHXLI2a1jyZBLweAdADk3p_a7DEQsdkhluVKA3RPjH2gsfIlpfuSfMhszP45IE7E2YOQPp2szFNvatpIRdYn1VgTuYOVwO5plVyv7vH3gHrSQtB_z6xWYQToe6MxW1T5s1JA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDo99u1s5Ws1F8XNUYqrwNSTyfHfuvchsLwK98VKGTuhnUVrv_iVy1F7IMjnrGyc-HzyASy7W7GFvgewimrYRJBU6FfUrOl-dN-U_g98kjcyQIsgxCLzy79NkM_0JvBgJkLOuz19lQdPXC2artu4b002P2NfSMIEnR1QlM_KwXpIIp6WupTv1VKpni7oUvF0Z4SRBtXEghp0NKlGnastyuSeKWaLV4cEG-HJ2DwzfSOZRNt4eO7jOdJpRWx5lp_SHdvZUWrDvAhL6J-uGA0JVYbV-5Efhj_xbVMpqedB2oe1FDqi1pOwdVqAV20j3wL4w7-jXSQFtEN2CrtZMM1TQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7uQcqSPdOLpnqe5jhui-vEb3QlNPyc8oyXopn-mDlXE8pGpmWs642k_hbyzPQHVZhuTfTCfe5Eag6ORkQHjTioI3s9okF4RfzTakRhwHYYR9OS7mdc3vv3o7Cm1Yqxq_LtwbLBAhtAznL8l0siiACTZ_J1DKY4HT9dL2nAVDl8xDYSqYSfvDdEjA5zlLAITOYIQo2ZP7xHpAy_Akmsm9egZhFdi6CR8fouWAUpzDd2btWH95uNSWdATaeyNzEiLDFHS9yItAqqubAWbfdbhXaWM-hM5kNq2EI_kJLFWF76ZLoML710CkQlJQhf8csm174KIzPuFwynixeM92xt4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=lzpXgsedmKkXpxeZCU-rFFD3_WeC9NPL6uYHaOj9oRZewQhBjLlFTrxwZWcR0-2-HuWkBp4hgCiUg89_6qOMhlJVClgy4L7qLM4v_3Bgv8ggVt4RZAjA-S8yuKsB5ieAP0F5rlGJAjc-P2CKasv-5_dIkIDBOX6r4jFmLKhRorGHYaZlj4PGYMuAwscdbR8YAHftDKy--0iDlBihY5UVHOftPjvsOR82c2Hs-Z77pRxjXff_lPwcAWwjzfKKqM-fikhQ-nV2gB1DQmE4roD7FRpR0bXX6d3npG6IBdX_ryx1TRqgG4-1LYOKBvvwxcXof24uMD3Dqzv9i-tAzDYMiQ_ZURt_jI-dsT1Nye41tDUx4JTGM3hvbfO5KqLqe0LOxLRDK23nV9r4WghxyJoIsQWTYiDRatAeYtJYaz4kWEeFY7QAAjufys3Fm3AFBvAQbS_Ub8SWBlSXX0hGt-abZpn0QtwcO4Z0RpRDdk2ONgG4OVv8-WG46suQmCnJMGBJt38pSOWFJNhjXqQTrnGrsV5JjRJBY8_Ew5yFG1p1ikDJnrmjApDXmoo27Yd3ylVZqGf0GmQo7vEuHnHJnWMuqPD4CTAVA1zki76l14yGMmNvZqLFAWpUkwGWsDgMyd0DphCLzvk6OLIssspM5ZTeiegjNjPIAFfWYDSw_0hVRRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=lzpXgsedmKkXpxeZCU-rFFD3_WeC9NPL6uYHaOj9oRZewQhBjLlFTrxwZWcR0-2-HuWkBp4hgCiUg89_6qOMhlJVClgy4L7qLM4v_3Bgv8ggVt4RZAjA-S8yuKsB5ieAP0F5rlGJAjc-P2CKasv-5_dIkIDBOX6r4jFmLKhRorGHYaZlj4PGYMuAwscdbR8YAHftDKy--0iDlBihY5UVHOftPjvsOR82c2Hs-Z77pRxjXff_lPwcAWwjzfKKqM-fikhQ-nV2gB1DQmE4roD7FRpR0bXX6d3npG6IBdX_ryx1TRqgG4-1LYOKBvvwxcXof24uMD3Dqzv9i-tAzDYMiQ_ZURt_jI-dsT1Nye41tDUx4JTGM3hvbfO5KqLqe0LOxLRDK23nV9r4WghxyJoIsQWTYiDRatAeYtJYaz4kWEeFY7QAAjufys3Fm3AFBvAQbS_Ub8SWBlSXX0hGt-abZpn0QtwcO4Z0RpRDdk2ONgG4OVv8-WG46suQmCnJMGBJt38pSOWFJNhjXqQTrnGrsV5JjRJBY8_Ew5yFG1p1ikDJnrmjApDXmoo27Yd3ylVZqGf0GmQo7vEuHnHJnWMuqPD4CTAVA1zki76l14yGMmNvZqLFAWpUkwGWsDgMyd0DphCLzvk6OLIssspM5ZTeiegjNjPIAFfWYDSw_0hVRRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=OOcB2wtpEN5D8oxgoPSnYeIog9X07_BLVQSJXcWDsvcuKMW8-BX9VxYReKVVHGU7M0WWY4leErUy3l1ndNxNhj9VCUAXYu7nCFlTAwS2OHxKQJkDMJXz0xMhAVJtJsRCTxRXMbBxlENcNXCKqiKzNnzg7e1paLWz3FtODTKmqdWrMFgbvYHQne0Ixst20hlD4HLMnzcQ15LaYLx4srzDgW6XJ9HGO2-E4EYKApt6qL0odevObhfFA2_hy3Dc7-dA_ZClkhxZXAof8E71oucJBvllmxW7oi-LaxmEV8ndEneetLWCwnjQ1CR3mNK6HVaJC8OYEtyToj3QB3TZzYJYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=OOcB2wtpEN5D8oxgoPSnYeIog9X07_BLVQSJXcWDsvcuKMW8-BX9VxYReKVVHGU7M0WWY4leErUy3l1ndNxNhj9VCUAXYu7nCFlTAwS2OHxKQJkDMJXz0xMhAVJtJsRCTxRXMbBxlENcNXCKqiKzNnzg7e1paLWz3FtODTKmqdWrMFgbvYHQne0Ixst20hlD4HLMnzcQ15LaYLx4srzDgW6XJ9HGO2-E4EYKApt6qL0odevObhfFA2_hy3Dc7-dA_ZClkhxZXAof8E71oucJBvllmxW7oi-LaxmEV8ndEneetLWCwnjQ1CR3mNK6HVaJC8OYEtyToj3QB3TZzYJYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDKApved1ki2Z_AWB0xqjVMOCybwRTleeiF0bJxwP7eRRJnqYxyxz7e_sf78BKO2GN0qY4DpbBg8FiiO36pl4vz5Ea3hTOK1g2JFDPSGlv-sIgp1YZCh6B9SqLs17-KMUpe0CA2G8QKESLCANynQ54s1MBvyyldt1A3YbbmsRzOJn8br3fj2UDXZyGW9vR0-bL6Sd90cENc6qFA3OLO1LEaGoWBAvzLc0T_SwhurZvlGQsVkb45kwIr_iLFNfnkiVLVRScVbF1VbwnLX1DODnswK_iE9mWg6QxtH1P_6pD3AhQgEGI5EEtpbV3EGUVZKNLAygBzjON-1voTf4x2dtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=czs7TIdfPrXqvZD8DO8kB0bJRT3TmOX-QS_ZltcQFTjJSN0O2BoQDm4lFLuBpi1ECM6zi0rx2kic7rhQ3gRvR4EXMitR68jeHJXe-_1VbvtWD4MGIYM9k9WxUmOMs7MA48uX1mWqvPJrdAEzZ7FxVEk9LkhOX1FPeMFlw-RSoRVnrUwAGUzOHrBi9vpR8iRP-xZ9xiwlvbUgwUIrTcp1qQ_-dUux1gs9FiJ5YO0kAvY1bfVrfMDlD1zQxiTwSJ6iDjtkHJlo8ulldQRBB98kOaWFFO3UjFY32ufs9mXVECKRRQEPalrUoUZWu-tLt9cu1TWpRXVI9QRj29Hbk4khmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=czs7TIdfPrXqvZD8DO8kB0bJRT3TmOX-QS_ZltcQFTjJSN0O2BoQDm4lFLuBpi1ECM6zi0rx2kic7rhQ3gRvR4EXMitR68jeHJXe-_1VbvtWD4MGIYM9k9WxUmOMs7MA48uX1mWqvPJrdAEzZ7FxVEk9LkhOX1FPeMFlw-RSoRVnrUwAGUzOHrBi9vpR8iRP-xZ9xiwlvbUgwUIrTcp1qQ_-dUux1gs9FiJ5YO0kAvY1bfVrfMDlD1zQxiTwSJ6iDjtkHJlo8ulldQRBB98kOaWFFO3UjFY32ufs9mXVECKRRQEPalrUoUZWu-tLt9cu1TWpRXVI9QRj29Hbk4khmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN-61YFrTehoKS3MF-dz5aPM5mkbpqU4UFYKWsccUEQTlUz9tTSu3ctkN3Tr_XY6ql8zTbty5R9tuNDcbx5GMwyuCAH-uOSkPlfEU74ZXWFJMHgIQX_h4Giesz5bPQeq9pGlYC3-jyD9ZsF5ySCvGOpxmmgB46qPn-Lc7vU8dDj9I5gMnvuUQkNWitEiQJ7hmpBxRojnwmOl5AyBvpP-YOIvjAsLFTVg4HHl3r0iE0Ipv2dHjntfY0kYCUS4Z_LSdupDj7kv-lTT17VRGyQfPn00nTHLvaaDjGX_R7gZO96qDRDryVQUmHCbWjTczolZ-fNTASbU-SvPSZm2MjtTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxvqVsX_Uq6a25EjBfb5W3nUiHiDhAV8XWKeGLwzqg-8fz6sjHok4k2rPflD-G5m93mhFB-QXUvN-RYhJpCpq9ooYLSNqtLtEmx4aPn04-SNoagjol95hz85yhRMGe0LdEdcPiaqNc9UEWWeh_lga1psZqFh9uX5MV-TVp9VO3DYsZ473l7HG4-1Y7zvhZEMVlGUmKRYVVUhsMPlyTYbIBYwG-F4b-O6RtcRa4Cnfpi-TmOTiyrt2k-Zh3pRHFUrGRxsT4NECz49GWsgmozzGzevy4PwNtJ6igT4jjHpqNu3F5kr10druK5aqAV7IFwMRx5ryCDxaji-SINUn6l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2QjL2corMooc4fUO9_tG0rHKq6QfekmllcXPNdzKXhb6EXdrcWZFNu7NUbJ9stbSjYovpV6A6KWAEr1t1v6p0OwjcUiVfswgq6FI_Tea2Id8MeDJncHTh6afears7WAJLxEGWpQbnrWhhpuhVmA4kh8xE7c25XMp0R83ElMmkct_VybjYuNZmNHgd56fzdNpP4PAaVM4mK5laxigZOT7SyxjBOSb8UdkFZBdo7klqPFfLdGEKA7h80Xw3E3Rjryo9m3459VZAOeCGsMUdrDyYPi4XGhRHGZgyFBDI4yuiOqGduZoQEAfj1Z-4mHqqdNuaQm1gxUxNnZb5SuGfQYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0dfMdjOY4DrfIJ6m7Sx3-hGo43Jez0zEwotygmKmOKw2gLE8ieIEJif9yw6fUCfzezT8xU7hlklZumFRooHOlYpU_jbDah4EKpwp9XtyKSqrxhUk86cTRRTbGo-5ZcYiJCvgv_oMXGGXlep3a_nKT9lTIJ4ogmUjyAqxnl-OtIf4-reB-YRt-e7K_KP_UknzjVSv4-6vZWaovfcRbHeGIzRMdSOCdjVCroYzVJOSo8t7jRKsx2cIecTOsgzCPugUDlsrLxYFxpuoOgr9g4LunWAwNNDznDc0UyLNSeJYdlUm6FtOkTZOUp5wzw7dVU0-8t1FG6EBUpSyRxXwGhG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDH59r7P7gi1lN2a2aUd3uSkAW7-U5yWChyuoGfIUvaiQEu8Peo2a1qzmWNzQJVvGyn_IK1px3ghbjeyrZ3osJ43Wq3naD67FGNV-LPMKAXLuTPhYxKl8dUHPQQuVdFN9jrTcAHNekHyhQOIXcxocSe_VpEWRkKcOgNc5bbbUc4sn3uw6m5xhPFIWhfbRKC55SmHHZwhzO6SllNCmsCsvRwKRRNJYddIw17ZKbiqMICdRc3s32mqMlMPUwKwlkkK4pbo_t4MGvKFbAhhRRvoia7oVoitGpRi12vLChrCKJQywt0X18J2fHVZoVXvhQOcgL_EeGUoORtQwiqBtunkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=qeNJg2X6FFLzs_xZSbCEuBNUdPiP_tYHQVy1N69y0qjsiHnSgDDP-xnOjHGPHIH4y_ZZ6CYVgcLeSyqIhTL9liD9PG79EBhYoEQdyRY50Ak8jdnsbUIpvv_C1rnd7aaesDki23f_BZ1KjJcQ7G_eFRv5O9FjtjI3-be6KtwB6xtQrd4Qwv8r-GLCy0NYm9OLRUSRn5bxS9-Tb8ZrArPYNKVfPyOoL66tB_HALBa9sbo-H5JPL3XrcK4xVkwIgxUbhDH6Y8onvtGiI1LpuZ791nNTcARPAuxpfBbd6A29rTxKP1P0FlF9-vyZPWfNZfDbZAv5WaNjfkZOqxIqhoF9fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=qeNJg2X6FFLzs_xZSbCEuBNUdPiP_tYHQVy1N69y0qjsiHnSgDDP-xnOjHGPHIH4y_ZZ6CYVgcLeSyqIhTL9liD9PG79EBhYoEQdyRY50Ak8jdnsbUIpvv_C1rnd7aaesDki23f_BZ1KjJcQ7G_eFRv5O9FjtjI3-be6KtwB6xtQrd4Qwv8r-GLCy0NYm9OLRUSRn5bxS9-Tb8ZrArPYNKVfPyOoL66tB_HALBa9sbo-H5JPL3XrcK4xVkwIgxUbhDH6Y8onvtGiI1LpuZ791nNTcARPAuxpfBbd6A29rTxKP1P0FlF9-vyZPWfNZfDbZAv5WaNjfkZOqxIqhoF9fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRatKEi69_2a8rkkgyk09dUCLBx6flXIrIywmtJ2BcNUJJ4LyuoB1nsSNcJGK9pKf5XQVy_H4VfR78rm7_yvpX3bN2dTA38LFxr9X8767MofMCjKd_JrPRFONc3T2MUBaadU3EA2z9ef7WnefI0UJ6AVq_AiFh29Flj041mbjU-JBCi7UrwJMcy0HlDKtZZb2ji-jEIL3IhcuXTsAcRABlClezSIX4NEuecpFgOuL6jO3fv9WjfJ__3w2O8UXLD9OEQwAj5xXhA9lKwT4PSyAUS02orVPEk-TcO6Tq5HH5QGfxEYayR73Vr0SWuIazHXPW2zHhNqYgeowGYf5n7dPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE2Kb-r8kf5ZX3P3pxqRpsJxdBSHx7xB2VbGazSmhumb-_XkgHEu238IaiU3c2XB6qHjdamEIKleY3Nd-v3M6u_Ex3xzKsdjN6P1XaiL1eiqL28kYf6oSAS2q9pN218G7ovFQW2K2I6hm7kQhiGqSZB4UFQ1LR5hhlB73e-7r9OLeJ-k3uMsk25TtXDj43KbdDGIOtnLhX7c2g7nEN9ZT8rqQMie901axh-cMFVav_mRlHjRqMiSxGv0L1eIdqUKUxUt31guVntJnXzYEKfLUuEfwbDWH7sEHr23Li9T9JUz_RhRxVdhMe6JVaabruQ24yO-gHkV_JTvcPJTBecHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=W5tx7PUtj5iFasDYvS9VX4DRFdqAwVOlfLhdhG9qeYI6k3EO1DN3W59GtdW3Vpz3LyYy2oMMFMdKgVwzNa95vaaGagUsCOgOxLdF9n_e7kmoE7X0rJXzZ0_El3L7Do1ImkI3QhzVFtCNzMLJQovHcP_aN7NWzI01TPUIX52h-9UGV74g5HaZB207VGhQohxBkWzq50_qtPhnnboYqH_G8yfdvRR0ASKhJ59HJQEL-ubhUrd_fWfH7S8-UWMYK-K22CS30DRu_s3tQ1_ZpQC7Er6J5yFslXiCvIF6wCEcextlU0d-PWd35-3jObg33GlLEhfk19V75Cvk4GOd94XReHMrz5_laanwuZ_Tj1AQpCkifRAH1F7zbbHaz70g6lByoiHoknqgTv3gchok72CvTqKNq2HHz52DPicuL9Bo6ydfV7ZbDtB3wdjdpj0_aruWTdb5PMZ5yFPJb_h5WBMstvJq-Ly54oyIReNY7TO0hdF-6WN9MZnZVNUFBsfrokCnm8DTZdhv849YqFrl3gAxP_Pms6DX9_n4jWOE_REHP6Mh0GK7YKXF__LhV-WdJ23lTvWHgzWlbKsgAaB6NZ2hMhSXNtJU69SFC9a-8xNN8GnXgQNMQB5VAMNOeuUoMa1T9hDS7i1rHHAM7lfKuYS_RlRzscHEilEKF3K7f00J8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=W5tx7PUtj5iFasDYvS9VX4DRFdqAwVOlfLhdhG9qeYI6k3EO1DN3W59GtdW3Vpz3LyYy2oMMFMdKgVwzNa95vaaGagUsCOgOxLdF9n_e7kmoE7X0rJXzZ0_El3L7Do1ImkI3QhzVFtCNzMLJQovHcP_aN7NWzI01TPUIX52h-9UGV74g5HaZB207VGhQohxBkWzq50_qtPhnnboYqH_G8yfdvRR0ASKhJ59HJQEL-ubhUrd_fWfH7S8-UWMYK-K22CS30DRu_s3tQ1_ZpQC7Er6J5yFslXiCvIF6wCEcextlU0d-PWd35-3jObg33GlLEhfk19V75Cvk4GOd94XReHMrz5_laanwuZ_Tj1AQpCkifRAH1F7zbbHaz70g6lByoiHoknqgTv3gchok72CvTqKNq2HHz52DPicuL9Bo6ydfV7ZbDtB3wdjdpj0_aruWTdb5PMZ5yFPJb_h5WBMstvJq-Ly54oyIReNY7TO0hdF-6WN9MZnZVNUFBsfrokCnm8DTZdhv849YqFrl3gAxP_Pms6DX9_n4jWOE_REHP6Mh0GK7YKXF__LhV-WdJ23lTvWHgzWlbKsgAaB6NZ2hMhSXNtJU69SFC9a-8xNN8GnXgQNMQB5VAMNOeuUoMa1T9hDS7i1rHHAM7lfKuYS_RlRzscHEilEKF3K7f00J8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=AkQEfFJizjsOaW6FKNrKMAqG5tM6ylKsm1xiafGZw55WeoOAeKbNml86Kk716Fh9fBKWHRQup1eudw1A9We7YOTXg4VpoiNuxhWmvmBz2pvQ9OVbS5mic3e0ME61MKINkj4YlK9nHrnnlGiTZFtSVCvxlpItKov2CMlzYyl5KVT6hSW51rLbK9O8uN_on6zZzYBhtSnOc5k_u2gV_YqvY_WHzqWxEcZPP0mtJJrTGhPeEjQ4MZk7fv4-AKYoBiVe7W89bleQjR7TvrkKMovdpM4QVWLoeODw9eTKkwf7XW-O0TPqSQO8grTD1NvbPUDJyHq0_mqhU8ZQft1tE9W8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=AkQEfFJizjsOaW6FKNrKMAqG5tM6ylKsm1xiafGZw55WeoOAeKbNml86Kk716Fh9fBKWHRQup1eudw1A9We7YOTXg4VpoiNuxhWmvmBz2pvQ9OVbS5mic3e0ME61MKINkj4YlK9nHrnnlGiTZFtSVCvxlpItKov2CMlzYyl5KVT6hSW51rLbK9O8uN_on6zZzYBhtSnOc5k_u2gV_YqvY_WHzqWxEcZPP0mtJJrTGhPeEjQ4MZk7fv4-AKYoBiVe7W89bleQjR7TvrkKMovdpM4QVWLoeODw9eTKkwf7XW-O0TPqSQO8grTD1NvbPUDJyHq0_mqhU8ZQft1tE9W8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqLNVUXRhA--C09IBa57KD4edTfKJArzWbDqUX0eohN9k-70iB3s4d--_rLEmmwTXbdGesXKLKPRs9tUEw9b1OV8AX-oBk5bSu3beJWZZnmIemXcUYG9idK73WgAEkUhqGMC7B-7J6MTsMeRnl8rLBVeI4PQzQhAVbk2sFwVve_91PBDORgpKEfBgOoJ95AAlxRSWp24S-OyUG-ites3yyLdxic_EFRKKxHhifou_oqT9H-JUnMjGGAP8F0jCMYPLHd8c4NH8HMbQwBe6Mk0by-UHkV0OYdg-rDXu3pMtwDwGl1FiNcGdXNFhMJ2b4KQAhIuJVLBzJZojloaKQnYDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqLNVUXRhA--C09IBa57KD4edTfKJArzWbDqUX0eohN9k-70iB3s4d--_rLEmmwTXbdGesXKLKPRs9tUEw9b1OV8AX-oBk5bSu3beJWZZnmIemXcUYG9idK73WgAEkUhqGMC7B-7J6MTsMeRnl8rLBVeI4PQzQhAVbk2sFwVve_91PBDORgpKEfBgOoJ95AAlxRSWp24S-OyUG-ites3yyLdxic_EFRKKxHhifou_oqT9H-JUnMjGGAP8F0jCMYPLHd8c4NH8HMbQwBe6Mk0by-UHkV0OYdg-rDXu3pMtwDwGl1FiNcGdXNFhMJ2b4KQAhIuJVLBzJZojloaKQnYDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsMqEF2R6AocMkp5zQdV1JzkHD-BzWz7OrqV6NLmU0zb04Qg7qvXRHETjcQpjTfKQboUdLlvlXBNGtITlELHYK5Oa15O-poST2HhQuQO92kt7BHyJnjlXYna72w8G4Ux9NqBz8kPF6fQemxMHqQ0R6j_gsQWvfrY2A3iQCPNBYiORla4A6GpBRN55JBmCDjbPZ5QDGj5Z5ixH1iUgJBqL3d4ZHbDsPy5d9sDXSES_GsyXa-W_Z3GfZ0Xna-F-D5pzNPJEMxSB4nlu22ZUK8J1Y6R_1q84Ud5aPBWrJJjY6IImg8J00sfZJxlQbrd00Ux_xC-Mx0p28c6d8FNDZN70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juvHFzL4pdNyQ8RbHNrKK62LAZ0EJiqh4M2qoj4spUet0khnsRR4Q3wJpUezZwT5z7RL6WkcjCi7a_iJHiY4BxRj0pRHOa1FMkLN-IMGqiZwNXs9HLbgCLKqpgPNpWgWKre2pDvlNSmGkRjkYTM4P5aZKBM8vCV99KUBvkv6xNL9wvAlUpUaCB2lMG1NtUZTjKkhxdCTiMx-ZnYwDOaBGavHj60xL7Oa795edIar1lMu0eU0CvnDNGj5ZVipkjEYg-d6Rso74abFQ5F28aaxAXGJ20OFOYI1-ny3COsHw5j2pU55TOOTCrdua44cZ7F7UmiQdrSjWINBpwI7z6UjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khcDZjYm-V4uDdpRa_XoqQqK1DdZxB_UdF8nNJ13g8WRQY9k6MJsXRYZMifSC_iOm8WR8pe67IYcKHclEuL6rxwneymtHkIBNgh-vwjahwphNSPRgrUPq4ucajT_cHexvP1NOzaGk9qRK7Yfd9fPNtXbK_A2oSw7dNS0f9vctDu9kfOv5oXVeF4JMUt8rbIY3bLQywVTCZYNo2XfPY2pNOF5K51B9U_ni_Khp8Dw99mUqzBpHf-wMVGZKvoigKFRWOHgA68G-5QW39V6nj8sAt8Zl_x2geMxvEnle5vZMWPASeUxfancHO6Ua7heWNj8ba-NfC93bvx9ZIxcV0XSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ghQIAyO091dkva3VX8sSKXEehp5l78Sp6DvbHzOaIHUHJnmRZj7qj58wHv75qlTiLLolvq9x4PWuuD0lmZf_FIPcjNpkCwTa0CPi_RFHSd1HmC5cztdOxYvGNKWqCEHZcGF8dBBhwGUwXIRAv2MdDNcQyVSHgWnqq3v3gD1O0j6jffaEKzkNOhiO44jyJMY3ujVN3I5IS8Yb2iSt5eDF2DRszfTV41yiqaLLLAo50K8Jfk6jr97kzTwyB2iHJUmiqE26W5sXPCTBfN93yuiJKuK2SrrwTGpkt6lFGGHsTPtWvVFJ1WzwBs31guZVqGi67hIQllA7slxa60A8_jgGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ghQIAyO091dkva3VX8sSKXEehp5l78Sp6DvbHzOaIHUHJnmRZj7qj58wHv75qlTiLLolvq9x4PWuuD0lmZf_FIPcjNpkCwTa0CPi_RFHSd1HmC5cztdOxYvGNKWqCEHZcGF8dBBhwGUwXIRAv2MdDNcQyVSHgWnqq3v3gD1O0j6jffaEKzkNOhiO44jyJMY3ujVN3I5IS8Yb2iSt5eDF2DRszfTV41yiqaLLLAo50K8Jfk6jr97kzTwyB2iHJUmiqE26W5sXPCTBfN93yuiJKuK2SrrwTGpkt6lFGGHsTPtWvVFJ1WzwBs31guZVqGi67hIQllA7slxa60A8_jgGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSIXnKTgbuT1R4nUxV1zKaYjcaY0qjN51BA4shkHZ7CF8UGGhTGt55zUurgX4czsjgxl_frUIlwZU1YeMW7RAybMQzkJ0fRbFjlUJhPq6ckgbovrdUln6VB93vjgJRyEBBAVYkSq68mPbTiGm8m2Pact2oDGVJRIZnIC_scuQGdDslJ-c52ShKryHUWGjaShib2xLlX01qhj7_j24AlYRMgyooN4qAdsGXYb1AqehwK4xp7jlW-9fJ8YJDkEBMVA86IoU0FqDCbP-n_w_C8nQCcOM1g0yTrkV-yh370M-geDxjb3fGQH9H1DZ73CBfWq7U0GPOzS5xKCQybBDoCnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trPMB-YLirvJ5sOKMSt7vj5hWefzqxkRP87U6c_dVAPQIfTArTIXahSDbByKncyiREQ4b5nYAsHWHvo4-0tSU5f6CSuovv9w5QIHasA-pRsRqz3JmTjPWyK3HT4ygA0znX3n6F9OPFB2evydIdAUJsZMVJYTu1zlcHnOdI3h8Dcjc7Dc_s9oC--cTNrFCEfxsiRtNd1Iy3iDNNQbExlDFAEQE4bn0PVUHBCoUP0cbCRk6UUF8ik-6oRMNleiXllhIDCHVOLrwvapoRNcKHP7eK9izVvEDMGl7sFkFAnTdGScTHLLzD9S90YOZuZfTiAQQXC0fRrBYKdsKO2SxPRXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwixKuikojUFZi8YksPT41PU35I6wpNxfEs_q1HdtFXo6d1i7x4tUrdZ_0riI4MlvT7UzceMcuRAuDKb2FZjFA72S0SwVB8YjHHKeeS8bidYPLPUR1ik5lmVjHPjePFKCG9J2ykyrzgGNKpXTo10tk-gD1LXzHdOQy0Fqk57VPMLsIaMObr8_I9FTG8VGfvPyNKjRAYrR6OQiNm1zJmPLxjxNaCVBqtH2Jum4scQ3m5fY6sxRpBULvP-b-c8bVeLyvYuyCklfLHWoyZCOV3hN0nqMBsAPk3CfPQVndBS0ccBGUtJO09F0GxcCT-m9hE-gXhxjlsq7a7-USrgzuMxrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgEJjhIsmWs2tu9Y3X0TC-iLdj53lnSGN5zwKTKJw3juXxsJSg42Oni835dO-C17MqH1Udfm7tpf4_iOV68rUW3LYrjNVsfVagYC2So7Wt6oGLpZ6OITjt48nx2jIf16UmST6KJla9wWhroi4cfp_tAT3zISYzw-Y2TjmbpQq5-4arYIk118wbctNGmQiwPWY5CW4h10aNHUplPOvGu4apmeA759JDmKtb6fUffV4R72tSdlut-pmsbbqXRRNa4pMpmYsuQefjZ_42X1v1m18je0adCRvFyBxMqita5oxzPxJAvdDW0U6_4MuJItuk0OlzetkmWohKVWTkxI_Q3bDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=XEY9A5UL1zbfeA4cF0varz6S58URDteym7rEjtNHeVuEMueblOLekUEFeBdEynx9rWLHjGrvU1YMOpUUwepGX22llPXMG09aGTic6C9ZkqAV3PEDN3Sczk-4OKWXraK6vP0L_KN3Jv-h0Obap-U5ISoHo597MxbrwlpggKpw9Sn4OrGPXrDM43s73QOR7jDviKHGhVsYTHOMq426D1dBOFazXNXKVMhyD9ADm9R0DFYmwH4Mdk7RceCLMq7jI8WxhglK7O0l_BaMWtw1Qwv76wpVZRF11RfCKX7-BBfBEJq2NNXhjlQci2CPw4fM3aUVW8B3znE05VAPXhRsdgZbITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=XEY9A5UL1zbfeA4cF0varz6S58URDteym7rEjtNHeVuEMueblOLekUEFeBdEynx9rWLHjGrvU1YMOpUUwepGX22llPXMG09aGTic6C9ZkqAV3PEDN3Sczk-4OKWXraK6vP0L_KN3Jv-h0Obap-U5ISoHo597MxbrwlpggKpw9Sn4OrGPXrDM43s73QOR7jDviKHGhVsYTHOMq426D1dBOFazXNXKVMhyD9ADm9R0DFYmwH4Mdk7RceCLMq7jI8WxhglK7O0l_BaMWtw1Qwv76wpVZRF11RfCKX7-BBfBEJq2NNXhjlQci2CPw4fM3aUVW8B3znE05VAPXhRsdgZbITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=lzf25MLHDMG-EviaPIT7oJbx2_JHB4pNMGioWXfNJVO9z96x1UD1ozeXRjY-2JA_TMJo7KTA2L2pjksODXmVBsumOZvspbfoZQ1CMxvANVc3GI9elELP-VQXWqtTCfCMCy7Zq5V97W4oDkhCQssCIMheLhbD8koncOLbS9PhwybbYcPDW4HlmKPINDmnL5OGpNYDbDqC2uf0mlaxaSN5KoHo99vJAh074FrsmMZvR9La1uV1GZzcc063M7253haBKbObBDE0n6F3QvEax9BgL7oziYJ86m1z9FoMW7_kfrTQWDGKizJJpnJxaALqd-PJnmgRcQBJQ6WNZ_-DNiPJGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=lzf25MLHDMG-EviaPIT7oJbx2_JHB4pNMGioWXfNJVO9z96x1UD1ozeXRjY-2JA_TMJo7KTA2L2pjksODXmVBsumOZvspbfoZQ1CMxvANVc3GI9elELP-VQXWqtTCfCMCy7Zq5V97W4oDkhCQssCIMheLhbD8koncOLbS9PhwybbYcPDW4HlmKPINDmnL5OGpNYDbDqC2uf0mlaxaSN5KoHo99vJAh074FrsmMZvR9La1uV1GZzcc063M7253haBKbObBDE0n6F3QvEax9BgL7oziYJ86m1z9FoMW7_kfrTQWDGKizJJpnJxaALqd-PJnmgRcQBJQ6WNZ_-DNiPJGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=dC8vQ3u6jTXy-XOkiy_zi3wx-fQEEmPRJwTFkTu4iZJaZzQRX6EMmijEiXBOhTeeHez9Fcw4MMpunlq-ynpYubs1WbiBY51xrdkTVVjjyO-ojzH6sA7mzqqistEC6Mc5lVfb--sPWJIXU-eZ1WizaAX8lxeE0SHf0-PWeNDzJcPvIuwumOVKsouw5y4YA2Am6-BwQQxeocYw7h7HBWbdW2QVG83h4UEVVwwhBwt3f3p3up62t8GrRYBG3Ir3KH-mgLO7K5cTmTAxSBqEsqoAa2FIIvsALwZZkU81xRKbMyFL_B7iGc-jLyR8IUy5rhl1GhEhSzSLQVIito-O0hRbBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=dC8vQ3u6jTXy-XOkiy_zi3wx-fQEEmPRJwTFkTu4iZJaZzQRX6EMmijEiXBOhTeeHez9Fcw4MMpunlq-ynpYubs1WbiBY51xrdkTVVjjyO-ojzH6sA7mzqqistEC6Mc5lVfb--sPWJIXU-eZ1WizaAX8lxeE0SHf0-PWeNDzJcPvIuwumOVKsouw5y4YA2Am6-BwQQxeocYw7h7HBWbdW2QVG83h4UEVVwwhBwt3f3p3up62t8GrRYBG3Ir3KH-mgLO7K5cTmTAxSBqEsqoAa2FIIvsALwZZkU81xRKbMyFL_B7iGc-jLyR8IUy5rhl1GhEhSzSLQVIito-O0hRbBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A32ucKsvnHnkhW4bywXfVDDBBpotsG14YC_SCy1OM8vQnh62IYoKyCtliQyFUdauyeZ5ZK1IcyHOyUfa1JydIS5gKXFJyp-d32LXCjN0vSK03xy2eSvehUmyNx5jgRApDQ7cmbGeP7sHO_ZRW6cV0Oit-A7-GZ2BkCuguYEKox7B7mkCIkm2iNXY2jxslKUCh3YcvP9-omFFsVk6l-TqyI7z6erpVJbUm9LCGlYd6HaGWZf_E146sHfIA7M_44lobHYnFNquU8bOUo6e2XE-yO1WsATvvdbkDKoEW8BvtiTFzy-PGGs-IXjgruT2RAkBrrzyIGeuW4IrTZUwvV-fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Nem8PIILAjCLtgERAmqXEGKdlL9wSajYTBQtVL4Pg03b8BHTLDgqhIjFPeRvLmKgad7VE1vJ04OV35Al6UmTDhZtKr6skVcT73J2YD6g40bb0nU0qGVUuYZzy4k-2HMM0CjF5RWGjTa0WEo2gnjWT0sH1J0YSbzDtWZvJn6kdsrfGQOl6gk70l4GUrQ9ezwsNOMBQAe-VV7DNYBvVh4HRhSIlsCJa_DZYKyA1oZ4QeRdtw-pPtYBc-tHT3EwhwsccMLF9jBEJnI5FHDWjdoRQgp0LKQfQuamRHm-Q1_UaofjTkSl5m3bLys-gIT_MAGeVpPMtGF3erPWFZhSyl-RRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Nem8PIILAjCLtgERAmqXEGKdlL9wSajYTBQtVL4Pg03b8BHTLDgqhIjFPeRvLmKgad7VE1vJ04OV35Al6UmTDhZtKr6skVcT73J2YD6g40bb0nU0qGVUuYZzy4k-2HMM0CjF5RWGjTa0WEo2gnjWT0sH1J0YSbzDtWZvJn6kdsrfGQOl6gk70l4GUrQ9ezwsNOMBQAe-VV7DNYBvVh4HRhSIlsCJa_DZYKyA1oZ4QeRdtw-pPtYBc-tHT3EwhwsccMLF9jBEJnI5FHDWjdoRQgp0LKQfQuamRHm-Q1_UaofjTkSl5m3bLys-gIT_MAGeVpPMtGF3erPWFZhSyl-RRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=L7Ot5eLuAgGIYQP80BjPTQOy7uPVDUcJK0Um2YrmowgtAZUbd9Dbb3ZtXR0BSgL6skbYCL04trl-bqxg4F9eHYmm3cavj1xNJ-oiyE_NsHnay_Boq3PeJj3xyVVxcK6N1xRd7bhNdVLScmQax5FvuNdagtoihnzgK4b-pQtfSPKDIHjKkEBjy8JBZ6yrfXPR8pZISZ9qidFrBWy_2iMsnCjEvEEeVExc728ALd39L3q_-_Pe1M0XqT4lLF-MmfT1uL4Y2aNn7I5k_XHQ43BiEV19QDjzPf48ce3VQqiQfP02hGUC2sfZkLuofUmPr7al0mBYrn9qXhX7xUnSRYnT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=L7Ot5eLuAgGIYQP80BjPTQOy7uPVDUcJK0Um2YrmowgtAZUbd9Dbb3ZtXR0BSgL6skbYCL04trl-bqxg4F9eHYmm3cavj1xNJ-oiyE_NsHnay_Boq3PeJj3xyVVxcK6N1xRd7bhNdVLScmQax5FvuNdagtoihnzgK4b-pQtfSPKDIHjKkEBjy8JBZ6yrfXPR8pZISZ9qidFrBWy_2iMsnCjEvEEeVExc728ALd39L3q_-_Pe1M0XqT4lLF-MmfT1uL4Y2aNn7I5k_XHQ43BiEV19QDjzPf48ce3VQqiQfP02hGUC2sfZkLuofUmPr7al0mBYrn9qXhX7xUnSRYnT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=PEXyymy5Ew3dWkiFCETjpOL0a1Tx_d_wGOg2KD-jpT75BNIGJhV1emZ4UJbXtZCWLW-_onVDyc9mlj01J8V5DLf2avCIj-hFhvXoZ0279ekPOp2qPU31aZeJiO0__0TGnJ1Cacmj4xsG37UyulVCbDBaAWa-HMx8kaga3wgLTaO72sQmw2rX1_aw_AB25qrjeb6J9Y1GoWDCiVVTuZmjLRJCPuaken3dUQvpXTsjQzWBRyz9hJE5Y0Vh4fjdAIo4EsOriNyAjMgeANL0InFeDCW2Mvgt3mmYijM6Pv6Hs9_AEoRETHSY4jqxN1XattoN7II0DpPflw3t-mQZbUN9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=PEXyymy5Ew3dWkiFCETjpOL0a1Tx_d_wGOg2KD-jpT75BNIGJhV1emZ4UJbXtZCWLW-_onVDyc9mlj01J8V5DLf2avCIj-hFhvXoZ0279ekPOp2qPU31aZeJiO0__0TGnJ1Cacmj4xsG37UyulVCbDBaAWa-HMx8kaga3wgLTaO72sQmw2rX1_aw_AB25qrjeb6J9Y1GoWDCiVVTuZmjLRJCPuaken3dUQvpXTsjQzWBRyz9hJE5Y0Vh4fjdAIo4EsOriNyAjMgeANL0InFeDCW2Mvgt3mmYijM6Pv6Hs9_AEoRETHSY4jqxN1XattoN7II0DpPflw3t-mQZbUN9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=h06DIAQ5NDET5MrmUsRna_7KPr0Vi8kK1VkvUah9iS2dyaybi5FEw-WyGuUMTUvP_M8a5DehM31g2Ny86n7kmJkulp1H3M0rvw1oNPLD0ITG3auE7eQmyURQPvKMG9Xn4jMFdQj2ooqpH8SdVgZhUHduvzW2efHo8WY4ritD1NAwmoIUqCnokuy-2GX3RkCUwYfvQZZOOPO_GLMFhalsft3tbxaVdq0C4M-lcegWCt7-8ILIltRHtlhCXYn5fRGbH180QT4yBFyisdVFJPeAU6JesLGkl7oADgdPtjwySOuc7IoAKN3beoAaOcWMJ7E4Tl-r_JBzWJOCWrw1PFrtPrBU6cOyczM063H0_UR6notLyqlG_cU7gaPcAkjuFojXxwIpfxCwHsr5eFSqKzDv_Jp2VHeGRb-lRMYYy9bQZbKRj2zy0pTQC_BJUKk3t0NMuRQjBDQiWq6ux4MVdAf8gwYsj6SoesnVIzF1K5hC8f7QCKvpHt6_nYns7TG6j2mgyuv1MhKIYW_hjii8uwkQiE4UfVrQz4rO_XLG-2IiBVGo5YWd5eLkv5eVEtdk43UbmtL-r34hnbYQmrfEpbnsp7_5Apim6UwB4U6s6-PoaYTLoGsTR-1m8KrlrTiPEnqpvo3Ob22jDsuEjJ--9RwdzkWSddraRrhCBFiZjAD6Xno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=h06DIAQ5NDET5MrmUsRna_7KPr0Vi8kK1VkvUah9iS2dyaybi5FEw-WyGuUMTUvP_M8a5DehM31g2Ny86n7kmJkulp1H3M0rvw1oNPLD0ITG3auE7eQmyURQPvKMG9Xn4jMFdQj2ooqpH8SdVgZhUHduvzW2efHo8WY4ritD1NAwmoIUqCnokuy-2GX3RkCUwYfvQZZOOPO_GLMFhalsft3tbxaVdq0C4M-lcegWCt7-8ILIltRHtlhCXYn5fRGbH180QT4yBFyisdVFJPeAU6JesLGkl7oADgdPtjwySOuc7IoAKN3beoAaOcWMJ7E4Tl-r_JBzWJOCWrw1PFrtPrBU6cOyczM063H0_UR6notLyqlG_cU7gaPcAkjuFojXxwIpfxCwHsr5eFSqKzDv_Jp2VHeGRb-lRMYYy9bQZbKRj2zy0pTQC_BJUKk3t0NMuRQjBDQiWq6ux4MVdAf8gwYsj6SoesnVIzF1K5hC8f7QCKvpHt6_nYns7TG6j2mgyuv1MhKIYW_hjii8uwkQiE4UfVrQz4rO_XLG-2IiBVGo5YWd5eLkv5eVEtdk43UbmtL-r34hnbYQmrfEpbnsp7_5Apim6UwB4U6s6-PoaYTLoGsTR-1m8KrlrTiPEnqpvo3Ob22jDsuEjJ--9RwdzkWSddraRrhCBFiZjAD6Xno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=KYcDCZsG8MvlTT6QDPvlrr_MDnr4IcZc8SRrxDpk5om1lHpkUgIjDKSRDRd19MUslCDgcDKsCZWxj3evqTV-4VTkXPEtZKzRaGZEv18IuuPikf5JjLilcGksLuAai3p1Vk4oXHu1HvWopRTP8G9oNlBOB9JalBup2NWgXgA-oduRBGyzBDal-tvHe-siJJ2UxYr3G0zuR5bbWR313MlWMF6BoFfVkfQfzLLadizA29ee6TuQOSqYaSQ7hIujR0DJ9KQ_X_B7CKkSp4FI1hE4YEaH85d08yiMfLn5ZwFD27fANyOGuvRt82ZOD1h_KRA8goh4NaYSEsxnRVolAr-Sfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=KYcDCZsG8MvlTT6QDPvlrr_MDnr4IcZc8SRrxDpk5om1lHpkUgIjDKSRDRd19MUslCDgcDKsCZWxj3evqTV-4VTkXPEtZKzRaGZEv18IuuPikf5JjLilcGksLuAai3p1Vk4oXHu1HvWopRTP8G9oNlBOB9JalBup2NWgXgA-oduRBGyzBDal-tvHe-siJJ2UxYr3G0zuR5bbWR313MlWMF6BoFfVkfQfzLLadizA29ee6TuQOSqYaSQ7hIujR0DJ9KQ_X_B7CKkSp4FI1hE4YEaH85d08yiMfLn5ZwFD27fANyOGuvRt82ZOD1h_KRA8goh4NaYSEsxnRVolAr-Sfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=guql6BdmV4PHL-H-yAIhHjVS6ajzFyxfJBqzW0U11CR2umX1w1jL47qgmtCg3gxOC7-Lr6nKHjkzMFxxDcJFxGzcQ3AXBmvgTbGPFX2XLSWTAThMrsbSutW6tgCTmPikMEuSnNuN2uXLc3kO7bU3qnheUILc2FmADTqX5naAOexQtfpwK2XFMMdlt3BRmQooyJOMkQ6KF0ztQa8499Fr6KTjUy_CPlROS7eotce_hUEhqW49_vDLcc5KswdxnyJMhHlUaDpkr421pf40YUrJ-3fbXvZoqniugiUBmOsPdeC-QEzndy6tRJW4GtnGtfuqoyBDevhgfXgZLNTg2unzsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=guql6BdmV4PHL-H-yAIhHjVS6ajzFyxfJBqzW0U11CR2umX1w1jL47qgmtCg3gxOC7-Lr6nKHjkzMFxxDcJFxGzcQ3AXBmvgTbGPFX2XLSWTAThMrsbSutW6tgCTmPikMEuSnNuN2uXLc3kO7bU3qnheUILc2FmADTqX5naAOexQtfpwK2XFMMdlt3BRmQooyJOMkQ6KF0ztQa8499Fr6KTjUy_CPlROS7eotce_hUEhqW49_vDLcc5KswdxnyJMhHlUaDpkr421pf40YUrJ-3fbXvZoqniugiUBmOsPdeC-QEzndy6tRJW4GtnGtfuqoyBDevhgfXgZLNTg2unzsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1Pi1dExtmktBtXguPvehFYX_tKyhdw14Qrp79VbkOYU7FXXMwkR6XrUUn_GZERKrL6IX8TkPQJUafTiMHu09gaq5NgqmcnLipTLhyBcUOLrFIbrlZzzPG15nrBO9Zkl3fDCLrzCOR2HtvECDvXG1R50mqq7t-4rwNIQe1MIpQl_0qb--jybEMu38tG_FIh__wBxWrDM0PlPSgBRc3mloOfdFXxysWiuSQ7YM7hpnztuGaEPSv95MHxUuKksfuUsbsHZO4wptl2lH4ZbJC7IHt5Dy84A2PsrIf3uFHi40Yh31XSu2aYjchxle0i8pwuxBbE3VmGGSVwEjO6W59wnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8pT_Mc82yNTVNW9_-6BxJwPtAh6PkiZhMdUo1Krx7GyBH8aF7BscgYdwMe5HbN1RdIhWFCsy4E0uiZJt9wp8raQOeh2e8HzIJFTnS3BmYO3kBZhKzpQqUKyxqMk5Kwuixw-nnL87yP-RsoIwbykQQVyP141uSiNiF-fWlTiySATqaFlcwwBNJX7jgCZnoha00gCrosThUwI0Jm2Xuys4eoJNHhpPxSOHCOX8NHSfQluse9bznJeocFfU8o7a0XGPZBZHVXYuVng9k6igGMTFXdzRWgyiOoqm9N5sdLEbyXQoBXZwOOTRF8jzoSFoUpTSogZvEh3lFvYpa5vNEiRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qH4qwH9UKyywluuAbB3AtBpF0ZFft6hDvuP3Ry0XtE7T2NvQEBz-8apvOMxsMpOltkk1NzFIbw_ir1Z5iCOt-LuRhjELzS6xkhZS0G7iapJnwa1b0gh9EZKQ7XJJajN-H6aEk1ctpXLCeYddJEbKRHvc8BVxe8Dky-ZlN5ShoIwe0enr96n_KAX-tNEP-8HNAjWsd-U6Skbnfm02wBE35zKbA46ZzfvToejCKq4LiE3veGlfMacweH4fVGHWM8I1foytFJ4HTM54qwqCMCZQSdJFMLXuT5hDukXcacCiv05VYd_kUFfWnh4vFhqPNMGoVdvnuDdAUjcIssAUQj7SgQSBLEAHXP8fABhSFqx69_jfb8W6H4SF7TuE_3zl6CCuT8R19aAnw5vSz-ceXPVh3pmbgoB9o8-zqIGGdVxLWjrQsBYm4Uc2IyPH5BufpsQJyEwQm4vFFGY9fiAU5HJaT7n8upq5ReAom08K6cxkCpyfUnSyg5B4XoGDUkg430X_PsELT4rLePmThbtn_1OFtxifydled3etWPJm5iI89ad6HiY-2q3MgHqHivdDuTjjwFZy_31LrW1S9NZC14JLS1M7oS0wp2mcEfDFI9HDb01OD1zQtEZCo6BDr3wgLOOUXcZNOt_g-MQrpDxX-7IPnSXLPkgAoqYion90caNfE_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qH4qwH9UKyywluuAbB3AtBpF0ZFft6hDvuP3Ry0XtE7T2NvQEBz-8apvOMxsMpOltkk1NzFIbw_ir1Z5iCOt-LuRhjELzS6xkhZS0G7iapJnwa1b0gh9EZKQ7XJJajN-H6aEk1ctpXLCeYddJEbKRHvc8BVxe8Dky-ZlN5ShoIwe0enr96n_KAX-tNEP-8HNAjWsd-U6Skbnfm02wBE35zKbA46ZzfvToejCKq4LiE3veGlfMacweH4fVGHWM8I1foytFJ4HTM54qwqCMCZQSdJFMLXuT5hDukXcacCiv05VYd_kUFfWnh4vFhqPNMGoVdvnuDdAUjcIssAUQj7SgQSBLEAHXP8fABhSFqx69_jfb8W6H4SF7TuE_3zl6CCuT8R19aAnw5vSz-ceXPVh3pmbgoB9o8-zqIGGdVxLWjrQsBYm4Uc2IyPH5BufpsQJyEwQm4vFFGY9fiAU5HJaT7n8upq5ReAom08K6cxkCpyfUnSyg5B4XoGDUkg430X_PsELT4rLePmThbtn_1OFtxifydled3etWPJm5iI89ad6HiY-2q3MgHqHivdDuTjjwFZy_31LrW1S9NZC14JLS1M7oS0wp2mcEfDFI9HDb01OD1zQtEZCo6BDr3wgLOOUXcZNOt_g-MQrpDxX-7IPnSXLPkgAoqYion90caNfE_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtK0OfMVS_4lf6Zs2E7tJMCWUcWtaW487w-zwEupTYfp9e52p86tPSqBtZJe0RjRhSGjUZUu5WD2MuYoht9KCq88LdUbcazcaF922h5jd3epjLNx_x8qNAGY_1shbA7VWsXKq6dAa1sHrkmMssxK3p3nCSDdnmJkWxkaN0dbo7rOf-lSM0qXWQVGxxZ2VYk5YeVaK5zYaHRygxKofS0R_yE4NMS39l1ZRJz96bhQYAYLEiiwvXueMhios2JdmmzG6HjUp9f8D--Ng3xgtQBCpQPVdYfGQ88vf6wsyFIkIH2dW6vOgb-1Jny1VyM_H3hKUqwu7jEN2JPnFlMnqStnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpH5tW1bjgb_DEqQPtAUzJ5WIZ3iSrtM9i7KX5qX4hoJGyNv0dhxA7S5C7Pg9zQIcPT7Pd6HDDlPSBIWiLDToiKjB79jKrjucikjGWQYf9Tn9sY_MVC88U7lTwWBA_wtxdXXmkcWbtVJq_8zXfA5vORsk184QEPM7jFkRpVkqfQoPOSFTCNxiX2cnPubWnEawWnofaEkkVf3wH-bIqyngiVvf712FF8fpJPwH0WC88cn9kx50Z1JAMWYv-jkhml1AB74evE4KZHqx9xW3na04iiL81lporfrWZYymTEBzZJVvHLYXpiG7O-xNO72s7lpbis1c4gBzrW_g0vZPRkDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfDTVFbZvnPmRV3S_uSYTX_mCWlEIkc0tcSZv675F_UGCFvsr6bfXVuAT_cXASzM7aUFB2W13I5chkw9Qo_O218iDRI0cJWdOZ_q8Z7kK3datXKzdaLK5hr5Coc5NUYB5qwZZuorxh-wppLNRsAqeZF5orznfljm0VnMqte1Ik_NEBtW9so0sk3jP0fb9T15h9vgUfA1yi0o2KLxiBaw-tmb5UMxqj33x7nnKmO6t-x0PR5-MiWg833nsE_WlcXBwq_hUAGmIIwE2GBQR9LNXFxrkEIbFNsS4mQrXJw2A5mxhlWyUsdjp8GueR0rpG1WYKUyZ8x6FUZa2717acYLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
