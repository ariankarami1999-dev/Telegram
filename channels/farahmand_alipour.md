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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 00:35:05</div>
<hr>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFPu6x2yAqM0FowWeCOzC7ZD9xUufv3bRPxrBgf5HEk3ADhXHqJZz8Mwd77ZYfzcyUy6ksKYnj2AoFMZbcbNvAR6og1IIwAiRRKii6L3oQc7Df8mTG70c6qpCSfsLTmtTSMbBvXCWwR6u3t7jqE-RaYH3MRAWEePnJ_jgTMgitCzm4cljyEyM5TrgYMoxrFkLtfdkSLfM18F5JO2viqS4kSAY6JUSFiGI4pkEDQtkK_fJeSlXua4pO0sGXY9fErj5ZgLwj-1NNTOMzpld2yy347vjKZxiGiohFsRgAKiAzNH20lVyFz-P2Lsy49-IjskAHUaK9lqryPrYcWmX7Qtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARSf1IpFoiggWOir5QVMbEWZxz4AwgozvoiJ-twE1OkW7lLGBRy851XpTr8RsSznNyK4BF9EOK-ec8CA9aqvjqA59Kk95cUTg3qmvuDks9eWY3V3KjyW1lbwhG-eNtai5zbKXTbSQeU0PQMVo4aa2qTTlQQ9vyIET4GjLHhjuK7bB-7ENhgftftsavjNiFbUWkQX7BrkeW9cZzhCbFhNSD18JKg8KsMVkHKGfWd_YHZMBLZ1ZiP-Uc453te2_YFAUNxe-WQhLQkBWDzi5QG_gvxcSvwHh9iQONEDGJzbBpp95e_GRMkrtVVGGp4oH_n9H9z3z-PKj46jw6JDsu5oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uB66tTXZlp6pIatWbWp_kc4dWcG3KAurDK2C8jaBehHfAyZfYwpZTtiSgHb4Ym6sq8B070eBP7CFj92DlL_bzM7O_A30qZlx8byjulJIpUy2kaQaBCoz1HCPB1GJVJQRTT3z9tFzQjzjKrPdCyJndNe7kTXYXEnzBRsCc1oTGpO6VkMDXinQQOM-QHSrwzv9i-BtxxeZl99FZNSultAoCQgK7aQg6YxPo_mGlwNfitKkbQUfNCpJ8w9TOwtIXoSSMicqXihDDiSGG0DgPweSC9uYg3QwCcGMvNAAsU_WUHrClwM3WWoSvtMktntjVZAsaqi6kNjn3nqd05atre8olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLv-l2fwEiYW03tA8HIWQT6iaN1gnWd7FI10AvZ4MjaRMglA-p34XRSjwUNCbhpRA9q4C9yo_e60YWncVIFWvJQlooLiF2faUVnEonmXvTU8C7l5kzHHcQ9UjUFvpYVNvtj9dDOSjI9qIkSbLLgfmjdv1ZrxaDICBkCLLDnT5E5luZktFXcrCDzCWcduVZ9Q7JW_njwOQX0QelVKBHgeBD0SjbZyEB1khFGkGs2SpDnmNZhOzOveKyXZBZS6P2eOfD6hns9OkcR1hWw9fQ-ijRULgTGU8He1VCzTblc0WbsBFEQQklObsOmZvozelxSkNGfUXPqlscO6R5Jch7zzsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atw7_cTkFBkoIwCQIRG3_pznJ5Ki-nNZQ8kJKt63CTRSTyTCC8C7L-dKVSHFBFjhZviaTUaTznnmBTmCIJ7-y2v2nN6JewTZCdy9KwQnTAwZ-B_StfF7rt9cOWqSkq4b0_BOjnH_0hyn5Dzl4FiooPYfjVyPXWGrWUyPekRPKvXi0YuPKBySABVJYlZuoZfT8HvpCv6gEsHBitw2OYLpizSEIB_8FHtTqBaxMoRqJ-tXqT65IPTN0Gr0DKEAUwIESMNiKR6GaNK0UbeJqGoK9Rm_lQ_Z7bBTHqsDDvntKyX_dBxSjwvuCZOPdTkiqsGFYqXsyVnKb_llI_j7Wk5h0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4-6vDNmdBjmfpoLrHGIMbCZdQwFrsmr8TAXRSaU7QHhSnDbBSwWqyDtD9QXbxac2ng0WhHLmmBfKB8yEPPQIBgMgz9dgmhKhDMBNV6NZtETptv3o4DKD8pLDFG9t65ioG0WWrkCZZBPqvqK6YpNO_MNZOrcfO5iHJtY6y73Btanae5OxUU4Ht9RQO5mVQRSLxi-PUbxCiCE6cxNUOc8ZXRy_X6YFRTi_6fwKSQdpxCeq6DFFUqqAqICpXBWRWuP8YsOe_dur-n_j8NIPOd1wn6CxtmOIEVq5vlqaYDtHBkJWucxua0L-NgsKnfB8LK8DJoPi-myg7hdI8m3BF0JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLAXwwkgu6VEXR-dO361RQoQYbwpkxIOQM06kXX8Ta3CtNKzRaiYgMjeAizQUIK8tUyOaXE_J6C4VKhMMjXfHpMg92GBXsjwGLy4Z8rSTGhBmKFVJHWBBmsf-Aew_7m7PV-J20Rv7pXg274DWnTEeHAfrt-Pz_Ak77yhvhvkn6s2mly79IKcKokZc9trnSSXMHXS1-FFipAdI127R99Eh8xwienuSxz9YbCTne0qPtFXFbtA-hRvh7WUe2iks0YMk4RYk1Sv-NEa1sk4ueE-7pYxZIsJzvW-2A-arBhQLq_YzxKj1byb-D-Eyq36vXK4eNQoCgZrCffwq4ViRJAZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjHX02wxtpU1Gcx2HV-JyuI5wNPbopBj9eQhkAXwYt03FmVBNLdS9vix1XxBcxsnJjjNo3H0O51zmwxx04gln3KNWr-Hwv9T_qgK_z1cUdK9oTty4XLcCRY52yhSTQKXTwcX8Mx48Tpn6lfWIRLT8RwXos_WFMo5rvbsBJFPlv_POrePigHuFiUJr6uGVJDvPCA1dwsb1PTX3KDwM3tcI07_J0zpne2ScnkWmOe9sWy5Whz7WDieJ36qV2ZRfGigrDeyf-qXjR6VlI2OR-Itr9eIU0_nk_5Ub7evrOCqyx-Xcw_p9KC3rvvfQleLVPsLe8k_y6aSd51mxLf5opEI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0iwZLZsTj43Dutkr0l2cO54lzYuTn_Um7jqZbh9rPEM0q9q2Cwgadt06MjxOqSabNKArWE0bR7KrlaY74cq60z8p3niUkV7DhystSfXWOEP7CluzvR7Bk6i6qoJf_csn8mpIagyfEUaTBIv04mnSzHe57buW-c9Yh7KLlLR4IMTb-M6zFKck03mFTj6vKfF4isz9OexLaNzyUiaY9RPlGXiJelJMSRb9Uo4X9LJWwAbehTTpXxn45ZaQCQK34k5h7GiYfyJ01CJpnOw2ddoZm00pk5JwgrsYVhuQGBjKInnTqOO33Ln8tW9GdtQUZPLJM4f-ZqPZvU6jyBj_hOHSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goiVYG6oizv9WzzjYoGhm2Vam4WU7Dgce97hQmWsSoWfDIq8LMg-KPFTOV3dsjXhNynel4LNfZho7JWPuoQU9cFiijZUaizC_TE2sZLEWS_5PpRIvkHJnxx_BtnUjfNlXusO2R201DJSxqJ2Ejk2tkbM2zmw1stHyD0QMEwtjA1RumYbDH5jXWuSdeDlQzHxtVH7VtYpmcI_FS1756AvtpL64Tlhri2ygkOGhhF164rO4k9jZOPXSRPIpKtwfep3RB55u97-BzYGFr-PDeFfOjL4u-cOPkAovLTVDpPIZzBWjUbLUqJwBpfZmjc5PJ2ro263O16oivfCzS8OT5562w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjEwQK4uwoJVVT7x0Z41XFbIEPxtqrJ1-wu-GP01RUFs_wHMoZcW4fFC7gDxDmYKDJzuumkafn0iI5uMxL_w7528QLIYprrdTUvQaLspn0GLBuaJ67Nfkwl8DuD3YWSzjQKinoxaHXk6bgB3Bmqlra0fCxIpIDoIGbE3xRUaudf4-TNjHuc2xIER4wTMGPpyNan-zlVtTe5VYVfKUIVurk-kIuOY0xZrFstLdvaX6ciyA_bBmf0007jClVAbFXR_5xG2u6uJhFZsDlihtbXS_KgQnmtFqNULRShK6PlBLamffUCSXdqb3UjChwRZ0dj8kE1hO_GJPV7PwXhP6Kt_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOJEq7mZmsDk5b_vGA3QlzC014xYvoJokpSeJNqhfatJ9CaexlCmrB328gC8dQkCA6OeycAnOpREO0GTfQKExJA2zGj-txU-s11O6HFVKRl7lWegkOAYGFjkw_BMsIZEGhq-rBReTPYBcn9CHc2belLK9XzW5GedWGlhdIw3YCgctW8FvfZDci1Sj1gXThcfdC2U40V2FfjQJel474lcVKZvcTHnA7rB7dbrpHxTR85nlM30tXzEq0k7PeAXIRhPTas1hXG56YYGnYTj0cAZgy4XCefQzIMwIYi5-qvu2c6UUoaU5ryYQdB1ZgaPe4RHrfrITnx208ReoF-xrVp2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNTnAYL98-04AZY2zACVzcU7GktiRS2tqFfvYvzSKFjYHzNY8aJ6P3dKiJ4VNy9aVRmPhgEoi9-91J3aSX9w6DD3s9y01j-4LYOZtRBRzAjsOww7qVs0IBKWbLPefgWOHCaV0KMJTyrvmRCsi2V33ZCWUag4lXci100CJdDXg8S2DZFQckLV3I423x3a-aFwB9cDG418JgKtmYv4LC0mX5fyXub-ReejqCHKuteLZaHYTlXSPG3gI2KYMUB9RmtAh-rHTlXm5rjNq-rrJWpWEsPjkZ9FaQ7IfPNNYyEU2sJLsLqo2b4bhfk0TRJmDdVNb3UzFs-gAU65GqAPEqc1Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxMUhHCpUdZKiJcwHXk1cSgZ0OtrcKyWpV0LLrFbuRNDgUrxoWATkqPfM8RUuAlvTQGX3MxhLE9VX8cmXBru5giLiSk2zV9_NbD4gnlq0vBg4DpxsP0Wsz6FMdKLCxf76iaWzS6reA-dDveDXektMwKIwFUbACKzmvliovyv79OE43C62ZlxrNGsrtgrEOFPfq68ZEvRTuG3iMVkKy9hxAuOcV23_vWAs0tzXzO7ITHCojt8W6h6BN0nVouXnzzo8kPa5AqG3VY6Qgx-S3goKGPg2Un0FmP7J0bWchVcedm61vCuyH5kTQQYrf5Nshc3geBGsACp2PJ02CZlOaiHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMSy-4IhVg5DC5891ULu_zaVsHAv100ZHfdABFcIUBhSOmMlReiS4ShkdnSlVjYN6rwDannUOJ1uzp8WnYschyrmq9WeHGna4sUpuF-Cytw5aBI-PzMKa3BM_QatIJELoVBIdhkhQv6mnSF4X4x8LOajcyEEgPga_JnEQY1nKyPrHoios31IOtIVdXWfom94rI4JmNfvEhJEAI_v0iWWa08Zap7muMLRfKYfugQN0YsU-dytEEpRhMUaO3mCUVXnYZVazUDjl9HR-NtibS43LwjwacvpDHrJ_Y7QaLjZ_gKwn_5OjS6N2vwNOl_MaVuL92rihFtKpucXd4i281Ox1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBsvtnO1o01VRTYh91VqvWnAFpIK8CNQ1qfBZyKfE9iJKq1S-MDGTdE2XDtL_tjOpIZS89XYtZUUH27NXWcaL4IN1DeSGH0qCwRCC9lbzNH55hfGFLXHzaBiHTLpsx1RHNBDAUJ0z7xZ5qQUEWpISrhDtPH8tS7pmzh-lUG4Q4cyEafjhpjaAHRkPRuJENZc4WZfNtJxY7Ietb5ySHO-0LyYI_8gmvZTEHw4mFYHP9B3D4srFnkUYs8rDYpjTYP9oGXNcFgIDGtv0ktJogZjX9TjVWwDiwPMrFJT5UVnLu0YY-7kUxyVBoj29Lo8k4t1f_o94Tp-h0LV34DCXPKl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=q_kE3k7n-susYaMs7qLlFH-j1xR6FJt8SmbQJ5jF9X0cFxGz2kPARZjxu3RQ_3UUI83kN_z5vPRCwHhLDo7COu575v8xSg35_8ukiin6sd6yRojjTdgBr91tYhZ4bXZ1mf1SObbvfpslu3TEKBHEJUq6k_XBpCtSsAb1IAxk0hNkT-vuMS3nkAhRI4ubOiVI3miO5zOGwwyVrNK1brcPvK4TZUAO_cH-UFkdXlIrq7IaA8kTdlQAiXERE0o0Tr6x_8cUxazkudq24V73bXQqMDPSRTpeJiUSu9gyJqyFH-AEJmDkYsaI8OXi_VSq6QR3mcoaAMSdgVtmK4aU6hVV2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=q_kE3k7n-susYaMs7qLlFH-j1xR6FJt8SmbQJ5jF9X0cFxGz2kPARZjxu3RQ_3UUI83kN_z5vPRCwHhLDo7COu575v8xSg35_8ukiin6sd6yRojjTdgBr91tYhZ4bXZ1mf1SObbvfpslu3TEKBHEJUq6k_XBpCtSsAb1IAxk0hNkT-vuMS3nkAhRI4ubOiVI3miO5zOGwwyVrNK1brcPvK4TZUAO_cH-UFkdXlIrq7IaA8kTdlQAiXERE0o0Tr6x_8cUxazkudq24V73bXQqMDPSRTpeJiUSu9gyJqyFH-AEJmDkYsaI8OXi_VSq6QR3mcoaAMSdgVtmK4aU6hVV2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHe-cyx1hF59wPh7du08vEHdaRrV0-2Su-zi0Ca3JZF-JlCFAhYV7sMdYvgDGDpEd3CHGGJAALKg9RwZ4MhrUS6AnTT10duR3IuWEMSWp2mmAMoBnNVM7n7h5-S-0x5m6gf0k9U8clI2_Zvmfcg2iIJ-NDwOPqHQJrQeAukWO5LcngohETPMJsxSl2jGJsIZvW5--S0b1nNhXmSkO9mxAAHjfGdRcpUtsybNEu23mc81SJR75WBJEzqckA8i8e-0bg_bVoC31ayZlKP-zGGe7QmsN9XdGBhx8SbjT0VchXxyrc_9736iNyoGrrLmZhJ10GB30e_Lk6tSQ66qv5v5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPFpTuz1mZ7XRVzSvlnaqvg2ziyocsedwdFRP3ZpTUpNfVpmPEsyKGgel9tYBJGYvxXLnCMZ80d0npeb-pFK8bR9e4RoTACNEAdm_3oRDkDlaiVBSkMnbNuCi_oI1t7BcczotB5v6fXkfrxw2dzLyOrvKVf-Nkd_YBBJhsJOEErOtElvmHgh9ZymImute2WynZw9H3HFOzb0xEKIvAcvpuCZsGBgvsgZfZhC8TiObijGSLjWKbtLr059jHsG3jHH0KJFy3ICJ5T3ykWho5njCxSAQGJDBDugp-RLyuJVLDJuzm2l6WR6bIkxw_F1dZLbUFZVRzS9M3h0wG7NHR6nHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8A5MA7ZczFtGB_IlmyzPD9yuxFkftOEUjcObzMzz_GPDb5m3aD7kyfe66zvVm3dBa5VgGMvbECryBI31Pjtpo0d6QB8sZZl9wswOXZrnBySLxm5oD4nfUFxnxQgLYVguXaOud_d1i2OTJ1gVvlWbEuIgJTk2faj9SD9oZfMMEInzsNVAMidiIcaX6ub_olEmpWdFzogsMOh7VeyEqux2B906U5pIYGnQolbpT-xRzdqQ1p2OH4lAMzbOuvq1icAtzks8kDFS1aUK3iXaA4XISbTF196MYH0bbi69uBp4i5XwzuLeaKMawaDEhgJ4KVCS0V8W2PmBMoRUHqw-saDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=b6X1WjW9Pz79Z2QpWQbfv7Io0ko5PmWxOVKfRBXpOEgxQRzzWyak2EPfrsdRqOb5whMcHrpBy7hw2FSlY6ckSiZQJRXiKEfcyfC5D0isxJq73hvpb6FdIOOxtVWf1TYJNnTVkpB4vgl5laRF-5qs7KGr8YJvZ9Vf595D3XRVVnjPAnMLxipp-ddyAe8XesB_6yOv2v1F4qBLg87y389S-eJGu2rp65xnRa0PZNXZF3DZPefyUz0Hru1FNO-Ge1ggfSpH1Maufonx8QtFT-Vebi5mdU3TeK5Qg7TiPIMFrMQgHybQtgQCHbTt1xHa2iYw8N6Hnny6A3XRZdWGPT99yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=b6X1WjW9Pz79Z2QpWQbfv7Io0ko5PmWxOVKfRBXpOEgxQRzzWyak2EPfrsdRqOb5whMcHrpBy7hw2FSlY6ckSiZQJRXiKEfcyfC5D0isxJq73hvpb6FdIOOxtVWf1TYJNnTVkpB4vgl5laRF-5qs7KGr8YJvZ9Vf595D3XRVVnjPAnMLxipp-ddyAe8XesB_6yOv2v1F4qBLg87y389S-eJGu2rp65xnRa0PZNXZF3DZPefyUz0Hru1FNO-Ge1ggfSpH1Maufonx8QtFT-Vebi5mdU3TeK5Qg7TiPIMFrMQgHybQtgQCHbTt1xHa2iYw8N6Hnny6A3XRZdWGPT99yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_ZzLTwbYwgCdjSp53aePixSUUyRRgFyA78sY_Yh_3GaE9rXOWdt4LPs5SADbXejgv-2ktQwzXal2J3GBYCA2fYx88mqAAlX0A290ltOw-kDA58PVILGXevIps9BEC2qLdZze9C8QITo0n9ifSg6cXeLLOkxwPuBgpzGQwyUalmZfPRSZiHX9cp10z5I7MUH6SvYLnLumBc0lEs_LDBPZmoAJALkxkGhSfDMQ60ExPlp8QRryyOoi2fv3MFg8tURGR47Z3WYHMJ7P-XXw_BNU73RqpktjH27CTpTQ029Ym9ellDM3PZ-xbhPoXLKGq9RnjgbjGy4xfzN00CbIdkiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=VlVKpJZgCVxy_EPwiniOWoJ33wL8Np4LMTAP4GlsDfIMGTH4H3VdC4vmUS3_7z7LuIQNhZJSNIz4RQQ-JIjNNAGaLnTw3Xo0zQUOtUWFpBEvyIg-uNPjVkp7theIeILNYZkI25LE67ROsv8DADSZrhqJN5mF-3S_ylvI-dT7rnhr3d-REoWMBcVBoRu8DjXHFNkG6sOuxFOG1rZDxj0Vcfb8e9pHit8dE_kuwI12097tMOA5QhR74V5YHsV87iIdeLkLTh93NvlC4AqMPjsgl5UsIsR0wgS_Tb1XNta7jAAWiRf_vnCk5OGbLn2S1gGqrVCiQlYDFID69k4WSXELTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=VlVKpJZgCVxy_EPwiniOWoJ33wL8Np4LMTAP4GlsDfIMGTH4H3VdC4vmUS3_7z7LuIQNhZJSNIz4RQQ-JIjNNAGaLnTw3Xo0zQUOtUWFpBEvyIg-uNPjVkp7theIeILNYZkI25LE67ROsv8DADSZrhqJN5mF-3S_ylvI-dT7rnhr3d-REoWMBcVBoRu8DjXHFNkG6sOuxFOG1rZDxj0Vcfb8e9pHit8dE_kuwI12097tMOA5QhR74V5YHsV87iIdeLkLTh93NvlC4AqMPjsgl5UsIsR0wgS_Tb1XNta7jAAWiRf_vnCk5OGbLn2S1gGqrVCiQlYDFID69k4WSXELTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCvVjr5OoA7iCkLcmlUHDD6yNilHqHVaWcrA0ugK_jx7hbZL8R5fx3ot7F0B6K2Z-DfozZImDqrR6Y67Ct1aWvn5trQb0xbpDreoslmZWO0GnTFRwsj6o4kh-3Jqm2laOjvdozqjDnhdYjirjAlkbL1KYq1tiOVN64Bl3R5rgtUQS0ti6lTkNg1qkxbOTWBbZ_wap1d4E65yJTzN_kK_y5FUkNgIZF12JeZRW3aCj8iTFgQ2P4_mhKg9bkuKeUoksva_Ss9tq0Tlo8ige9IceSVuIVq4_wBjDu2lryK7F4_m2I0xthX-mrXqoHZkYBJc6OF1kr4zaskl6j38ZZS-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nry_NBeupxEqfR1tza1OxItwx7j818ZQ8ByRzjNSHYEb6SK4lxlGcUAe7rtrxao8IYsh2PpRlODDDPNLlwMi_pFNXebk76kDkTMpn2KwpKd4wGpBe-7PgmfcgS6gIYInpx-V6KLKVorZA9YFVGReBff0zWwDs5woT3H20w-ZKP5_JcCvtkfVtO7gHDxJx-DbSqMFru1fQJlXzPX4esgPVzywCGGhCOjoL6DlYKW3itxaFMxWEnb-RLTGK4vSlKkxYsX-3-QyhKyGDf2AFj05pGfn6vqkEvFpnqX_AfuLAZQFq5epJuumX4ruWNNFvt6i09pCxgWCf3TY7qJBsiL3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=gT-DuEXJYqz2CZOb_df4JOAZg_9IaUIotgM9jI9g4claSLkuwn0q9HxECvkOl2HqnYomV1wS434isDfHBqDd3ZYJu7GNSWiZhxzPDCshma6zBWQ6TWxkEyedTgkZzXkfSfI2ZLS7fl4qjDq6k8Tu-pKEZahTGczKCBgfA4IH7nMUswTRc3RZemvJb7b7Jf01TnYsAs22mxbY6Pybq_Fo-NOgcby-kccJZfmMbhTxFZH5d-aV0hPSdnlaohb3ShxnKvALSgms6sPW4m1mb1ae7OM4I68F1XyCYwxPF5RAJlLhGd8oI5Gtg3mynaQbwHjJ7q1iS7l3Qi0ycJ7uuSnvNlTELJ_bBBuKjtX0LxkNlOKDQuWgKJxSNpOu5f2DEdvX-EFIb8Z5fmHR3d5iKQli5777XM5BE3SOQRfW1yBrsTGJTPFxf3ribgNrufm4zxZ0NX1Yjmw6QMv5Z78MYFVGAGJblkwjigSs2Lx_AdMuI8EdCJbzNOJr6Kvg3fRE-2t8TMWcdqabWXkyc9Bv0ZVh4GyG05TQw_lVzpT_hKingSFE1x_uIFlacd0KgJR8Krv2w41bAjMlJWtqoCVQXQlEdoLp6DA_0gPsLaou9tF7UOHns5XTeh047y6vyBDlZALaZuGh5I8p_CssZSc_UyeLsXOmgrAk1mD6CCW1kPoUdJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=gT-DuEXJYqz2CZOb_df4JOAZg_9IaUIotgM9jI9g4claSLkuwn0q9HxECvkOl2HqnYomV1wS434isDfHBqDd3ZYJu7GNSWiZhxzPDCshma6zBWQ6TWxkEyedTgkZzXkfSfI2ZLS7fl4qjDq6k8Tu-pKEZahTGczKCBgfA4IH7nMUswTRc3RZemvJb7b7Jf01TnYsAs22mxbY6Pybq_Fo-NOgcby-kccJZfmMbhTxFZH5d-aV0hPSdnlaohb3ShxnKvALSgms6sPW4m1mb1ae7OM4I68F1XyCYwxPF5RAJlLhGd8oI5Gtg3mynaQbwHjJ7q1iS7l3Qi0ycJ7uuSnvNlTELJ_bBBuKjtX0LxkNlOKDQuWgKJxSNpOu5f2DEdvX-EFIb8Z5fmHR3d5iKQli5777XM5BE3SOQRfW1yBrsTGJTPFxf3ribgNrufm4zxZ0NX1Yjmw6QMv5Z78MYFVGAGJblkwjigSs2Lx_AdMuI8EdCJbzNOJr6Kvg3fRE-2t8TMWcdqabWXkyc9Bv0ZVh4GyG05TQw_lVzpT_hKingSFE1x_uIFlacd0KgJR8Krv2w41bAjMlJWtqoCVQXQlEdoLp6DA_0gPsLaou9tF7UOHns5XTeh047y6vyBDlZALaZuGh5I8p_CssZSc_UyeLsXOmgrAk1mD6CCW1kPoUdJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=TbTfT1j_byeI8ESRL2jZPBA4pZ1zmDG2T14IbAnN3PGX2bSa5E3yzdyHuMcIgZ6qPywIJtewSkZcAlOWKVitnHm-jBobzXyvdypDPJV7o6lZzqFpl9zxt8f_mv4Ws5kRRcXG-TfjJhZEfh7LTVUQWaO1rT-97ku_v_lZFPQyk_aWxQMkvuRTid_gp9A7YxI01HQu057TZ0O9Ek1eCKunRuc6xcv2TntfEEYe43j9j2xvbm-w2X6ky-3AoGG_Lq6xo2LWDMSnHQinIIrTTQjOv7PUGFlRIvbSTa6yQm8WM-wpBrYTNI80Ht-In9OyVPwgK_q1INabiFT5tJgOAshL-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=TbTfT1j_byeI8ESRL2jZPBA4pZ1zmDG2T14IbAnN3PGX2bSa5E3yzdyHuMcIgZ6qPywIJtewSkZcAlOWKVitnHm-jBobzXyvdypDPJV7o6lZzqFpl9zxt8f_mv4Ws5kRRcXG-TfjJhZEfh7LTVUQWaO1rT-97ku_v_lZFPQyk_aWxQMkvuRTid_gp9A7YxI01HQu057TZ0O9Ek1eCKunRuc6xcv2TntfEEYe43j9j2xvbm-w2X6ky-3AoGG_Lq6xo2LWDMSnHQinIIrTTQjOv7PUGFlRIvbSTa6yQm8WM-wpBrYTNI80Ht-In9OyVPwgK_q1INabiFT5tJgOAshL-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Cz2hI6aGjeyiHXclcLX5uxOvTavn_3iO-q87hJNTm_DMwetBX9LRW9ah3FaSAjKtzVaukYUi0ELjMwaQw9AKYoqUL5G-PJzorZv1Tiv1kC4_HfpKVBxw0ezGp4pXKCkZpoZJN8YBZPN4At7Fw4oBJY-SeDeT16Krl-99-QhuvUehpQoeTgktCPacT5PKrG0nhU0rcn3017vqSDhrORi3ODAokQ0ZnZHXmusd4FA29HTIpeqPSzNERd6OcvmwvMAJBcIOTYCbHDIotcO_1CIu5kA2gBVdIMKEcDoSyy9iap72ZJAAnKIPpOYv2Xab3ImYrASIxrBEzuWHi4EhUdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=OU1tVkBduRgiTgYd1XGcbQH2mE-a_Vf70dkWRjrcQYMwXTUCh6a2eTcZNXpUvb2502684sbOnNtVcw71wR7SKvOcBrH_SFFD92KWlXBfR2LGAf0O5w7wCYGPGIr4EC58SwqLypBVP86i3X8qZD7vBf7JzbDmtb0mjTXIC0RSYcLATtBXh7RhV7cfYTPuMyX-UzyGC_LvagEEUrv86FnPynWUJyfxFmIMLnWHgdofj2EVFEE0GOtgmE0nl2AEu_5mNiZtzQ55Z3WC3ZsL8YUJn24YolvUlHSjVWw6LuC9GJv5gx9LDtLNw0Bw_fpq2HN3F_1ySL-kvC-fPPKPeiYDY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=OU1tVkBduRgiTgYd1XGcbQH2mE-a_Vf70dkWRjrcQYMwXTUCh6a2eTcZNXpUvb2502684sbOnNtVcw71wR7SKvOcBrH_SFFD92KWlXBfR2LGAf0O5w7wCYGPGIr4EC58SwqLypBVP86i3X8qZD7vBf7JzbDmtb0mjTXIC0RSYcLATtBXh7RhV7cfYTPuMyX-UzyGC_LvagEEUrv86FnPynWUJyfxFmIMLnWHgdofj2EVFEE0GOtgmE0nl2AEu_5mNiZtzQ55Z3WC3ZsL8YUJn24YolvUlHSjVWw6LuC9GJv5gx9LDtLNw0Bw_fpq2HN3F_1ySL-kvC-fPPKPeiYDY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPCn-2M1r6_3z5vitOWZRbQEhXe8BtlJin5EsQjUhYKSBoT_EOSyM076cEbvCWsWZ3TGGCgQfCBAZle9vqOupNqDbwfHff4zUpbwgyfs43xY_si2iGGZDoRO5cFV3sCiHLG6ONhRCJwzD4kZvFE2RpfSeTOmA_yujxaJbZjNPKhF0Ie-s7qhZ9ct27p4tjJ4erbrO_75ADzBjfLD6Y6yOa3r3U5WuWFPIWGrGShCoFBIxhqG--0QUoMb9baPgDbAzGuN5N1msWsKe3XtRfmjvjzrpjQEMLW1zd0dCdd9DVm-ctOlPa3o2ab73sqBcwtqs7Lsii6f2QWuJ1DpsYcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtTQ_pJPwmda_gCBjcDp3sbuOt5HypAqa7477V2eLyQavbrRLOjUbFSKr2Y9BHopOGLV0Zzqp1cxj_mExe-LBjR3DAhmOOe8UJT3MXEpb63oZdymGcXuFt4taWY4t59By5P1lWMrUOoD60bqyuTHYVaoxVZGCQG4dKn1C06keQ2GmQBVGEjgMhqyStesCbWhuNccwKFhWwy2oOeLRdc_UZAOsCY8-cTUV9QFFwpt9gRo9ynL5xzvtzs7UX3uhYEqUyJh_fWJGy67ECMvRpbvo8BXdJ-OZZ7qaRr-rroKdo0S5YP6wVx5T89qAe9dAexQA6RUKqej05eTSPiWtG-tFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzChFovNSNeKKWueTNd7hzoqp0Q9LDuzhGBi7j7WcjuhIleB4wCiVtdhPF6kc670cypgZCESDMYNTNymtiYBnC2fU5lhlC83iBJZqrfGjSY4fq_PjJIsJOiuFSZvt63GEw6lIZpBB_Qhu41F7iUJ16g1_KEpdF9Avx9DuJnP7DNXOLjFHAoEeviB_6Lsbt5UsyTmri4ad9iQJKawfUBUKSBTKxiBbhGruWcpSeT9atd6C86P1hbU-16zxNaabUSh1cDTbGmhfH_vaohSWLbfsQPAyLLcax28VscViNEovwMTNy4rGlGvyl2HCCqyVlamuJ7E6LPbeKoVXaljJ-TH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-_mmQsS-677c5alNjlTYXhUPh3s5OGKq5_RQzI42qKpMWt_JUExtiqUk1d3NRZNmAM94CD-ikiiZSgu6NIEuQvTzDlOPOxYGN78ck3XnA5g3IDZbf7WG-ImetniUdKXW6kulWM2kwhZ708uZQoRo7r1RhBlm8y4BgrdrLAAHQYDZQ0kxV4q8uKT_3k2yNiW6Q0DUHGU_h_pknGr1Qug-WsWnlHLvUKsd0OkU11AqiuyB0OVuUd8IVdJPw_ZIX2Wgq5Tx7CVXpN9MkrKaZFijik_fOuZS-4FjGsui23ganYFRIWzPZWXZC5p4NP4x5PQJCjaPh8E7VoeRKj6Ol8vIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2cQILXja-zkmy7BR9J6xSaVnS7V0HrqAaT7TYD_DpOl3D8X_JD_-XwsjQHTK0qpE63GRT95dVUqJo9nhjTdM_Ut6NpSSQ-bawvgtOW9-KakEzqcazfxquF6juG5LGHzBr02WWluBD3OjCu1HDOiO2fAIkVqfZPDn5RcX76xVRkxYI4qxDZgCSJjVb5xV9okWXXVePgXLzFXEs4nKheGhgm4maTLc9ovwNVkBG-C8tJ_8qky_orVa2MRuQPQA_ZUXoAw85oe0xdcSBq3OKPNwTE9V2_oyaEskFp9_W3i_Wz6fR-FSNAYw8_sjinjE0Nf1eMjZ5N9ZLPjlS_STMXIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=FvfMxzFS2oKsVYQEaBUxDkviS_dyE2AfPb5Uui71quxLloCp2ES3CNolGz10dZzSI2YwTshpFm1Clg1LjpP9HBCJQlHI-771j7f_sdoDWlhNguhVKcbcEBgCKC4i94_8BcIpuGNLH5BZrx-0Jn4AVLudutOsmu2UuAbPQ0KEKbFMlA_mOMWjZr-g-In5Ma1u-9-X6g0PAhjiVhBfC0Jmus5iBodtNm3uCeJJlY-MYdEtZ8DPwxbdZienoWxTpOjNCGiaJWLYLrP2ltApRIhNNNY0lug6JlNfRRCtSqd_0pgUD9BEL5RhK5DjcFHQF7uFvW4qNdiIXO45o8ptxaPvXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=FvfMxzFS2oKsVYQEaBUxDkviS_dyE2AfPb5Uui71quxLloCp2ES3CNolGz10dZzSI2YwTshpFm1Clg1LjpP9HBCJQlHI-771j7f_sdoDWlhNguhVKcbcEBgCKC4i94_8BcIpuGNLH5BZrx-0Jn4AVLudutOsmu2UuAbPQ0KEKbFMlA_mOMWjZr-g-In5Ma1u-9-X6g0PAhjiVhBfC0Jmus5iBodtNm3uCeJJlY-MYdEtZ8DPwxbdZienoWxTpOjNCGiaJWLYLrP2ltApRIhNNNY0lug6JlNfRRCtSqd_0pgUD9BEL5RhK5DjcFHQF7uFvW4qNdiIXO45o8ptxaPvXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_LUqdGTAcQVCH_iATXswIa0Lw79hpG76HeYSuFucN4lc1TWW_RaTbAhzl03XD9I_0ulmvMuaJTIxCuKU_MPLB_QdkdNRELn8wyEg5MLJ0i1BAo5xR6bPX3ALg-I47iyWhRRpAo5HacSnb_aGA0iFE8m3_JarX3G3z-7R7i3x0vAjIIcFvN_AUz-sfG7TZ9zQs_380QcHG3Pqz_L0s_LzWAtfC5-eZR-Icl0y2PsVFUAKTc3cgLmwznLBMtroGp5MuhqtQ_PR4DjLDTEybgKwshlGoGewG0-INMDFl5Wu8O3sTmTGzK0emReytQOisAJ1SI6quUv7Ylo4pLRjw7N6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLmgUYJxjgc74SPYv7SW9DMyx9VFTTYsph1iNWbSqTB-LZEbaVAdg4rZF9i0Nqwx1Yd4a8539tWUnFJ4pwO1SBYiGtRAy-95uSd3XuwNoqeN48ccUl-kpWJENhiKJBVYLMsvLV9hX2Meagx-4m-XJiY-c3vAOe0v2dcanaXvXnY9eWkmKMGVEye_DanUDvEIcfdHXInm5-qZlbtI_0kodipBObK76CYkYkK9E0EKT0Jebiq16PJxvX5QtzHUnuDYnDqaP0QsOsOAXbIcGDU9M8N91yYTJhugWFlSwU2SdfRdk4jwn7iFloZtodTVAhtTj5wb5thUGuF6KY767Y-66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Q8946jwLnxXSHUttF6O57D7oBoiBiudkB7ZQyvDxfP7YO_FQjJDJ9lsg1Yp7RpQWtM2TSwbQM659dmZv_Zp0qqD4kBu6w2yx5dj443Og0-cHlKOFm01-L_pLKQXIOGQ0TapdeX99Ybw1DJ56LGW9uXLrf6k0SQ_fTRxAWTkvT1gg9Q8-1DYJiC8orXiyfgqenXRW4nZXMuM7WT-dpwXUp1Ep2XT8RN9Cqx_ibYn7XQso1-nnNdgEAXwzZ2AcDZY56TuMSjCNC_MXzzWFSjt9XUzOmuMmCMxesO5dOKQJEPco1X8p-R_ze63GiiS4056cHH1baa--7X5guSsUGVEpEpcqW65S0OmC15Ds1ysSaP-92Et_rwKYFbi8UYO3Q8ylQKOje00GWoGGBFyYuhgJGjddLC8u4ssaKlL3O41UgMXlEDp6uaq5sOefV9qdT0icypz08dWASSOhF40tKhUjeUwqVwhluDvr90z0__5bBZkV4EYG9IpU-qMQt05mzwOL8pnkmc4bXtVyB1JfjxoVxcNHGmwd2ExySeTP1KFoMU8d54OCqWvyEO4-yOGSr_j80_2EDA-l9KU-0O3GAfWiAAtM3sTNbPxyY-4q9oDbVTYtZm24QGENUrRE9HRc0YujsMiGMQrMqCT2PyEwttSGnc_VQfP1zBDmGMhGpwC-uK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Q8946jwLnxXSHUttF6O57D7oBoiBiudkB7ZQyvDxfP7YO_FQjJDJ9lsg1Yp7RpQWtM2TSwbQM659dmZv_Zp0qqD4kBu6w2yx5dj443Og0-cHlKOFm01-L_pLKQXIOGQ0TapdeX99Ybw1DJ56LGW9uXLrf6k0SQ_fTRxAWTkvT1gg9Q8-1DYJiC8orXiyfgqenXRW4nZXMuM7WT-dpwXUp1Ep2XT8RN9Cqx_ibYn7XQso1-nnNdgEAXwzZ2AcDZY56TuMSjCNC_MXzzWFSjt9XUzOmuMmCMxesO5dOKQJEPco1X8p-R_ze63GiiS4056cHH1baa--7X5guSsUGVEpEpcqW65S0OmC15Ds1ysSaP-92Et_rwKYFbi8UYO3Q8ylQKOje00GWoGGBFyYuhgJGjddLC8u4ssaKlL3O41UgMXlEDp6uaq5sOefV9qdT0icypz08dWASSOhF40tKhUjeUwqVwhluDvr90z0__5bBZkV4EYG9IpU-qMQt05mzwOL8pnkmc4bXtVyB1JfjxoVxcNHGmwd2ExySeTP1KFoMU8d54OCqWvyEO4-yOGSr_j80_2EDA-l9KU-0O3GAfWiAAtM3sTNbPxyY-4q9oDbVTYtZm24QGENUrRE9HRc0YujsMiGMQrMqCT2PyEwttSGnc_VQfP1zBDmGMhGpwC-uK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=oZ5_zq7EuXDZJ4bZ83sJtQTx-9_yNryREbaqkPj5XpYu64w6gYDL7tG9STsO2lgSUFZn5hmTg4GxPPlLNwfLydY8Ni72wsJ_cgiJLvaYZm1US-HI1ckNF9oUS4u5n1oqDyFhtyzAtCprZ0XVAUEP0GDz0scxLyNz0utMLCMOLiCyvOowxMYaKKDzuSO8kybJFY8MBy_HfUZpdiyIoemGNGKT1GS8J0IESEyhmQi_0YJS1jMurL_MmzT4pFW59Qn-v27AoZvtIxUcUsElOQ2shgY9qvc67rMSc9701zjbGor2njG4Hfc_AwdrLwVenPk_j9he_taCJjAzZatMft2P2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=oZ5_zq7EuXDZJ4bZ83sJtQTx-9_yNryREbaqkPj5XpYu64w6gYDL7tG9STsO2lgSUFZn5hmTg4GxPPlLNwfLydY8Ni72wsJ_cgiJLvaYZm1US-HI1ckNF9oUS4u5n1oqDyFhtyzAtCprZ0XVAUEP0GDz0scxLyNz0utMLCMOLiCyvOowxMYaKKDzuSO8kybJFY8MBy_HfUZpdiyIoemGNGKT1GS8J0IESEyhmQi_0YJS1jMurL_MmzT4pFW59Qn-v27AoZvtIxUcUsElOQ2shgY9qvc67rMSc9701zjbGor2njG4Hfc_AwdrLwVenPk_j9he_taCJjAzZatMft2P2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KClrP9E9krjYUmioZ5QbJ3LCxh02wNJMZdmaAy5bGiwy6--EuAWFWCrqZXhkvHPpF7vEzqFMGGT1IMseBYm-dkUiEHXl1XloSTnTjyySTgV3BnGwsN-W0HJ2wyCE57wiVO-YR8IfaNqgslel2LezTYcpiU5h0-S4UEQA7n9NGW2n7FCCgufkd3VAQOQAFuwGh22ljiveVA4xAzoxlmsdETy5FFz9OnKOJX99eyqtsTRoMPfUGAXmSZH70XvZ4YKIBkC0X1isCrcT3KshugU9t6NvIb8IjHQ4QZ5sH5X7aUHxrqVlNiILxwI9qc3TrHzxE5Q6hhuyg3g7IvwK4Jma04w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KClrP9E9krjYUmioZ5QbJ3LCxh02wNJMZdmaAy5bGiwy6--EuAWFWCrqZXhkvHPpF7vEzqFMGGT1IMseBYm-dkUiEHXl1XloSTnTjyySTgV3BnGwsN-W0HJ2wyCE57wiVO-YR8IfaNqgslel2LezTYcpiU5h0-S4UEQA7n9NGW2n7FCCgufkd3VAQOQAFuwGh22ljiveVA4xAzoxlmsdETy5FFz9OnKOJX99eyqtsTRoMPfUGAXmSZH70XvZ4YKIBkC0X1isCrcT3KshugU9t6NvIb8IjHQ4QZ5sH5X7aUHxrqVlNiILxwI9qc3TrHzxE5Q6hhuyg3g7IvwK4Jma04w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsvYE4NvKJcSqX9rfpIVSXA8A9Yq25TSAF-zvQimFD2FdYpuWDkUnfYIFSCKTtU3LPjkbbuqIj51Sz6NVU8FQqA3oWWjqoZUdLCPVR0OWzSopHbEMKdIVdhknHQulVcLHlzmH0fL6GleClQVwnPnsBjG-obWE8MNW5byuU2bzaWj88Kp4apZEszj_5Yph_PIn4ixiCD1TFZV5Eknk_eayTXYY0PoKGB87T1SgH3PwVYW0YYRnqkAfhJfl_FmabtT1h1EClOjP5ZxDx9_4lz-6sAuEsqWips_26RAIToEISWsAbY38Jh6wttx4MuiqAboAaX8YASt2id2XIHmj25PgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF14U04UGSD_-Wz4_jqoWujlQiklAGMW2mN_Xvp9XhIsu85qCc6ZtgzmxZCFS6OAU8b4g79zikUFzjYgzv_5up8IYHgxP4GUF4vEGPpoPsvFiPRdRC7f49aCHSvFYrrC2RP0wDXGk2-srwYRKOgCBLz-onUNDAxJqtcN5_i2kAJIRItSzjGxBUXIBITw5TczlnEz-eavvQzKPQnmcHxpa-Xm5h-uc6lC0fLWlnuhGGDa0Pc-ZkNhNPacHbkYkcnfzjh71_zDAGXqH05R2uY6Kjq0q6oCzjelOdEeNGmbA9-S8LZgjiqDkF6UDqbNBcku39Ms9fnPv3X7wF_A9Ydp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXw4snDBJ83tUxYisXmG-fhK4nOx1dTuV3kYXFpPixGo6_hceoO4xIvdV8L6qZ5-7ijNQl8_K_63bnQl_pI7NQEOk64K_PFbI9aPG33bhyPG1S7TalywIOjLUGCQvEuWFd1KfZFXv76Rbpeekf7u9QoNQevV0nzH-xui6Hbc38IL9aO0vPsi_bse4VJNVcM8vnkTh--_fsUUnkEHY_-tvyjMWZ7avMUF8G1svY8_oM0QMG2Xsi8-CuSvc2AmaAuLLktsF-Ix5J11AknadD1muw_tJpvLwHxngDc1oj-gHtQV2l_yLOFgPU1u5eo9GSmIXP-X8nANFPxrywNrvrxQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=GdMcnKrNSQ4o6lJvSS1r7fAo464aCj9Lm1uRGQb3GqhkZ-h_NabyzapT8DDqaYBG4ZtSbuOTdCOUuWmBh9Xj5JGT0uf0zMAiuciOdLxgIe2zPIuvinvYkIUUVhJgSUEhrxgNPE4Sw2STxPFBacRDIxd_2j7eITwH3J_ULPGbA1FFbez4FlC-GKyfL5ieRlRURhK09zCyE068NN0kxxRR_mN0nRg60SZNgCQ4xRcmKGnjqCKN4URggvfLUY5ahVFT2oJqoeOoVrRpzCJx4QHh43MvzzQENcCj4LEFH5tD3UfNZgKlej-g2W5DSEFkmYtHoPEVnIP_WILnNBOWV6Oggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=GdMcnKrNSQ4o6lJvSS1r7fAo464aCj9Lm1uRGQb3GqhkZ-h_NabyzapT8DDqaYBG4ZtSbuOTdCOUuWmBh9Xj5JGT0uf0zMAiuciOdLxgIe2zPIuvinvYkIUUVhJgSUEhrxgNPE4Sw2STxPFBacRDIxd_2j7eITwH3J_ULPGbA1FFbez4FlC-GKyfL5ieRlRURhK09zCyE068NN0kxxRR_mN0nRg60SZNgCQ4xRcmKGnjqCKN4URggvfLUY5ahVFT2oJqoeOoVrRpzCJx4QHh43MvzzQENcCj4LEFH5tD3UfNZgKlej-g2W5DSEFkmYtHoPEVnIP_WILnNBOWV6Oggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ryn-LpT4zNTD679v_d7GaEWxCzuOE3o3-O3h6hUy6S-R6ZMwlbw5cD4ntKyML2gmjvO38wCxZ1kFyQZTVnDggqFsynDBfcPjI6gonnFxGaE92UB6iY5RJFI-76NR64wKA-E5VL2ZMJkfNe8LumSANh5fRTPtzIG3ewm1zBbKZkeq4qDZa9c2T8d2roF3DKBrOmINrvhs2eWhtl8nr0MiS0ZAzIJFx_EhufmSNEyBmzl6TJX8sAggfpBsnbfAef3COn3eUyDHqZ7PISAzLHHu7qa7ScLnQBOAOC3rLM_fIaZeN39Lcpu5-lPZT9AU77l77GKA4i-JLoDPI59YspMAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbZTC2-Wflz5iJzNO0WcT64Akb3k4YIRojjWVtCoYGVzm-xfdBMq1mfszKcpGgUCNtXkQ0HtM6WjRmZKnvof2z5SmRL6Krou2dFjvfSaH0R78PNWSQguiLRsZLZ225_sKKU6aY6L2hxGIar8rMPcghIyl8DRp3zC-S_vfpn3HyIxSTeE9vyCrNWRl0PrV_g5EUhta4HHKhlfmVKaSj5sMQXfV8YU69MwBtGj6x1sz16bKOtruSjFZdIoYyk81KWeM67YGvwhPvRO3tj1MUMJH9SXAygXVLD3YkdEKDmFOpKqnHjs3ojC0JatG7QdAndRmnfBfCd3HDhS7Y2c38hrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbgYoDoAhUHDmRx9ggeAyzyVBumdasyk446V92R4G7Zok6J8xuUgMfGrTp70aA7pZiLLHsU9ov7N0AY7Ik-jBRLyLPNvCyxWeSZb-NvdSWap394jF3zVDHP0lcgPq8FnBtmjeZGZC_9NMGKfFg2m2bhxVmdcQHkCVJj-MdVzo72cWZoR7MdaWKA6JIcyn9U4tJFl_CI3dY7_kjzPGsjPNq_QLYJUW1BZSa79vEg9EhafaCTqEb10muh1zyj0xnJIY1BlhUm9vRJGxOCL53rhu49DDjBHwEARSlKUuXDULUC6l1ErwnBBFbRinG4Z9aXyVjqF6PBsx5umjS0P07K0bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRjuiNO3Zsut7_kB4YGzVkUZzHyww-q3xDBQDIdBchZ2BFjQFQNz-f7RlSVHrbg_F0vTZZlBwdy-Cs3mB97hx0ZxcR6Oc5mcOawyN_QJ0Xjd1OVBQ-8izc2i5OvmVoUqE0rcH-qrQYYIK9OVt6Hw16mYbjLH8lONf7AhvSHhg37WBgGHkndFrYl7N9SCSWN4Z3OigjVpquwMsOrgG2z5bOytTRA0vgCewIIwznmdc17CMLMB_bSGxqwM969h2P3e5vSlSvLt-NU1BTtt6xkFPZLWJA76Vp-06ZCfor9QHSjtwZNxBb-xFXBxnkLpGdLemfgC7UxhcchQg8W5dVgWmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Kn6d9qBXzQ5F8JJjZTpsKS8K2Lg4kSNlpiV7m2Gb0ThshRFq45HRB2PgUP5_96uZkviqczDhOJEBp3EGzRw2DrY1agdYKuQthKRUA5J3yyu7OpsG6Ies0I-Ex0eVx14McCtOQepuiLpxmoLZiFwdwagsp6IjRUTNKa8byk-5pI4uvnYbo2ASTLjLVUX-P05NY9f8xgF-MjwUwpyUyH3Eb3N6WRiYUNEI6lsQEWDplQpZHBm_KJ5LsD6TEJS1qGYp8KaBEpUMsiFNfuWktmR-XygyZZcpV3Ip7Hc4Qs-eELBiad3T_WTbQ_9oz0SOQ-CKwYyz7n9YtVVA0uFuT-sudTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Kn6d9qBXzQ5F8JJjZTpsKS8K2Lg4kSNlpiV7m2Gb0ThshRFq45HRB2PgUP5_96uZkviqczDhOJEBp3EGzRw2DrY1agdYKuQthKRUA5J3yyu7OpsG6Ies0I-Ex0eVx14McCtOQepuiLpxmoLZiFwdwagsp6IjRUTNKa8byk-5pI4uvnYbo2ASTLjLVUX-P05NY9f8xgF-MjwUwpyUyH3Eb3N6WRiYUNEI6lsQEWDplQpZHBm_KJ5LsD6TEJS1qGYp8KaBEpUMsiFNfuWktmR-XygyZZcpV3Ip7Hc4Qs-eELBiad3T_WTbQ_9oz0SOQ-CKwYyz7n9YtVVA0uFuT-sudTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ALjGW8PFjm7QhD9zcKPwydkOMSXSchhEae7usw5lzaTuiTnOMVqjHKfIPJJaA9VbTWMky11GriFVHd94Wvmn_3YCTf4XlDWA1JPHOLDuoKsCws_pJ2YbuI67V23d-Q4hY0VdU46mg0cY7YcN3DhSPAtvvMmTUVpnKH_5vgaz1BMCt_UBCWv9VEEC6GUs6fHmXdJhjxQ_s_xXTRlfVDdEbYKWSmYrcqyTHEF944rCfj9rpuxTyvLa_v3FOblWZuHpEZB0WMwneqspPMWpE4i1aUEuCEjcRTsFXoljz3KNapiW5g7UUx3c_k9dV2Ju2rVpLvDjnFxxyW-f5Ud5-hWeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ALjGW8PFjm7QhD9zcKPwydkOMSXSchhEae7usw5lzaTuiTnOMVqjHKfIPJJaA9VbTWMky11GriFVHd94Wvmn_3YCTf4XlDWA1JPHOLDuoKsCws_pJ2YbuI67V23d-Q4hY0VdU46mg0cY7YcN3DhSPAtvvMmTUVpnKH_5vgaz1BMCt_UBCWv9VEEC6GUs6fHmXdJhjxQ_s_xXTRlfVDdEbYKWSmYrcqyTHEF944rCfj9rpuxTyvLa_v3FOblWZuHpEZB0WMwneqspPMWpE4i1aUEuCEjcRTsFXoljz3KNapiW5g7UUx3c_k9dV2Ju2rVpLvDjnFxxyW-f5Ud5-hWeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ZiOpYhGox-7u1YPqt_XFY6UU1On8clSXwsxp4qYQCoGq2aV1fHIqqVJekNYjbN2CUwd2x7kWnkwDxWw7jMFZK2_xKDbwU-J80wGuOq0ibFR7y_s_3-1xL_Gi1uer_99Mga7dQGiMvcTR2LBoOvexFBajlgbeHrPtFsgfdif9zsKp-M5omekhQSfIP_a79j4pV9KpgvwCxKN6p9aDJSd7B17Qsnf7faA4EV62Oj9EUmWGuQCDE9CPRN65Y5Y--PriOpMw0Byxf4E_CC5_98_AgznCQZYNNoZmxkZNelWG-FVFKcz0EFOp5sYJg2EfN2b1n864cTlwRboQm_JS_3T6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ZiOpYhGox-7u1YPqt_XFY6UU1On8clSXwsxp4qYQCoGq2aV1fHIqqVJekNYjbN2CUwd2x7kWnkwDxWw7jMFZK2_xKDbwU-J80wGuOq0ibFR7y_s_3-1xL_Gi1uer_99Mga7dQGiMvcTR2LBoOvexFBajlgbeHrPtFsgfdif9zsKp-M5omekhQSfIP_a79j4pV9KpgvwCxKN6p9aDJSd7B17Qsnf7faA4EV62Oj9EUmWGuQCDE9CPRN65Y5Y--PriOpMw0Byxf4E_CC5_98_AgznCQZYNNoZmxkZNelWG-FVFKcz0EFOp5sYJg2EfN2b1n864cTlwRboQm_JS_3T6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFq764Bb-UcBXF4Wf5txgh3XbizHlKOgVdYCpP08OJ7A-oMNcYFtDNwwZT6XRjKq28gXtE1_V9UEeR8cg9hl8j3i9kxDJ0b8SypBIRIHzGWfl2Dezw_JkliO5jkIlKWd7UnEfZmkmTWdOqCuNG9Ee-hFpO_lGkRAXa-5LhN5cKp5FlOOtMWf6wFIeXvHN28gOWi_wvQ0WFSXYtgwFQC7v4llaF1Qx9TTi6AXU1doTGw9qOE0v12tu2aFlgTR1ai_QTsW-F9EzLbUKKNntt8wpSPIZ0hrKpAGbfMpRtqXzwsQZUgPm2DIC0j6hjUXQrVr3eWoiVQKSQmsKr6BHevHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=qW51Nv01rhkrTxxDnvqzT1l00J88ZVu3Cj3fphGQQFk1L4IXmfGYTQ3dcfacB4oNP025aaVSPD0t0-V7Rc1g5nc-rG3TM9Wuy0byWVdLUMmx1ocXSsYMUyU6bAFpvO3kakpslcdv6trSGRY75BAF3drMUfvtv1gHixWfKkC3t940sE4ojP6gnYmRT5j7yuWags9C0yaWepDw7RT0YScOrhl8dYlLjVXp-yJ9mILCJFXZprI-tQyylZNV4S6gLDM3VDH28u3RSm_4vsTz7ocD4n9B_rzrcHwEdqMKscHUWLrb-Tac4tOxWaNOJ8JaUpM4URn__ykDvb470G-WFzCjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=qW51Nv01rhkrTxxDnvqzT1l00J88ZVu3Cj3fphGQQFk1L4IXmfGYTQ3dcfacB4oNP025aaVSPD0t0-V7Rc1g5nc-rG3TM9Wuy0byWVdLUMmx1ocXSsYMUyU6bAFpvO3kakpslcdv6trSGRY75BAF3drMUfvtv1gHixWfKkC3t940sE4ojP6gnYmRT5j7yuWags9C0yaWepDw7RT0YScOrhl8dYlLjVXp-yJ9mILCJFXZprI-tQyylZNV4S6gLDM3VDH28u3RSm_4vsTz7ocD4n9B_rzrcHwEdqMKscHUWLrb-Tac4tOxWaNOJ8JaUpM4URn__ykDvb470G-WFzCjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=CNlX2eZd30lfUI2j-EkkBwl4fchiM8uuSufYcVVaJmUXHGJKU0-ikNuUEIypyhWSTSYEwp8xgP5vtMdaCUVSvlRErB0mZE8CnehM7zfbnxmz8UKzx0p9pBRZoE3bfwY02VyNlpEVfVIy1W4uxRIgOJv3-TvVEsZUyK5GzhuLgoSI1fcYArpGhs3VjWUVwNn14LSm4S4f_4gdhssa6v1Q0itgi1KoickY_fisCQmrI1DwqZZqC-ggZITM9dF8RFMNzuHD4qhbOK0mrOLsZ9h331HEfZQPmRo0FpHZ7XAXE2eB2GY8AYxXC21dKif1CzFof5pJ9M681hbdTDHg1Obx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=CNlX2eZd30lfUI2j-EkkBwl4fchiM8uuSufYcVVaJmUXHGJKU0-ikNuUEIypyhWSTSYEwp8xgP5vtMdaCUVSvlRErB0mZE8CnehM7zfbnxmz8UKzx0p9pBRZoE3bfwY02VyNlpEVfVIy1W4uxRIgOJv3-TvVEsZUyK5GzhuLgoSI1fcYArpGhs3VjWUVwNn14LSm4S4f_4gdhssa6v1Q0itgi1KoickY_fisCQmrI1DwqZZqC-ggZITM9dF8RFMNzuHD4qhbOK0mrOLsZ9h331HEfZQPmRo0FpHZ7XAXE2eB2GY8AYxXC21dKif1CzFof5pJ9M681hbdTDHg1Obx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=j5dFnfSiBuK7RjP1oEBmOpRO-sz0bFm-4ZkIS5juYVCGflBRGTyt7eNpKHwGEhvAu5sLnlsnSSCWQqJA131lNDzjwtAqvGV7AThIlQPqCfusJFOpWX8UV6fRpAW0d1IDPwI-I-dFMsiNPC0N19PHpYMxYknwV7TVK0Jt0GXPwbUBDZ7kJwVIiCf_nLFG6uBdguKzqWopxIfSKbzkE2SDztVCP6O9swRbo6Fx86yyxozh2J2B1pa_RZKTL0t_la34qGhUPNyqt1L5ZnUM6ZdpYw6UsEpbgxHAmSDbVHYoheapZfwp4iMCriDlsVCA7QwOv3jyLwDB9Qwm2dtkZPq7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=j5dFnfSiBuK7RjP1oEBmOpRO-sz0bFm-4ZkIS5juYVCGflBRGTyt7eNpKHwGEhvAu5sLnlsnSSCWQqJA131lNDzjwtAqvGV7AThIlQPqCfusJFOpWX8UV6fRpAW0d1IDPwI-I-dFMsiNPC0N19PHpYMxYknwV7TVK0Jt0GXPwbUBDZ7kJwVIiCf_nLFG6uBdguKzqWopxIfSKbzkE2SDztVCP6O9swRbo6Fx86yyxozh2J2B1pa_RZKTL0t_la34qGhUPNyqt1L5ZnUM6ZdpYw6UsEpbgxHAmSDbVHYoheapZfwp4iMCriDlsVCA7QwOv3jyLwDB9Qwm2dtkZPq7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=rxxyxiyVmQDF3jTkPRn_2uZg_82K1Wuuxh-JTiJaa0JvNasJU3rQ0tAEVp3MRlmcAM_tbAbwaRxH9kiWivT4EOgT_vl_r-NThlBcn8CdUw_xae5Sjub77hOGWyjCjneo4j9h82MbKc7T-vQgY1qx5opK5prdl2-nwrMASFBhnpBzQ9QNJxo_v8rPqYPhxqm7bps8dW6vzFaA7RBzlKi5noM4qYnWsIIcSX_YhqRPyZU-vciPgUUu9Mxer_VGdgALI7487Trdf3lsdgE5l3VOos-ah2UDX-RKudjKs3G1_KBDL3druSgP98BjB2vXI1ZmWzzlD8QZ-hfCLRtVv5mhB1_s4ztX-Xgx5wwM8-2fCb3mJ6FC7rAHDgIVjmp_Irwb9Vp5aZBvehUqqZ1Jy7yf8JwqtgeHaVBClir2iVil5Np7Yv9JUZwSIDcqMTNUcEOba-LKM1_xszJXfo0VK5YZfMxuhOK9VyLM3GjwAVlcDWRK2P8iEglWQ7yamjt3JmRlYsCszoGUewan4SlO3gkke1nULC9-9qxNCAHx36mQ1lVC17DBZe9cMUSc2me025Xy16yFRx3JqdXfX1Kq7m6_oz5bd1d0yj3ofyifuIz8UsG1iwSXjunk_6Rr8LKfBq4F_-Ar-lq_KgpZPzo6y19cDcX4FQo8IvmsXdN6A3hYLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=rxxyxiyVmQDF3jTkPRn_2uZg_82K1Wuuxh-JTiJaa0JvNasJU3rQ0tAEVp3MRlmcAM_tbAbwaRxH9kiWivT4EOgT_vl_r-NThlBcn8CdUw_xae5Sjub77hOGWyjCjneo4j9h82MbKc7T-vQgY1qx5opK5prdl2-nwrMASFBhnpBzQ9QNJxo_v8rPqYPhxqm7bps8dW6vzFaA7RBzlKi5noM4qYnWsIIcSX_YhqRPyZU-vciPgUUu9Mxer_VGdgALI7487Trdf3lsdgE5l3VOos-ah2UDX-RKudjKs3G1_KBDL3druSgP98BjB2vXI1ZmWzzlD8QZ-hfCLRtVv5mhB1_s4ztX-Xgx5wwM8-2fCb3mJ6FC7rAHDgIVjmp_Irwb9Vp5aZBvehUqqZ1Jy7yf8JwqtgeHaVBClir2iVil5Np7Yv9JUZwSIDcqMTNUcEOba-LKM1_xszJXfo0VK5YZfMxuhOK9VyLM3GjwAVlcDWRK2P8iEglWQ7yamjt3JmRlYsCszoGUewan4SlO3gkke1nULC9-9qxNCAHx36mQ1lVC17DBZe9cMUSc2me025Xy16yFRx3JqdXfX1Kq7m6_oz5bd1d0yj3ofyifuIz8UsG1iwSXjunk_6Rr8LKfBq4F_-Ar-lq_KgpZPzo6y19cDcX4FQo8IvmsXdN6A3hYLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jWZ12_YlcMTCm20U44BQO6fuVtW2bYwWweOXDLzOywJkvn7SAvRJN4m7HGB3s5QwvTCD_Z3MVr4ALfX6E_-X_7x5FdGsfOoH7_syXsWjsV6uZ1kVhp7ojSRyb7l1C7fUCW6wU-gf-020ktAIHP3uhi95yBIWBAIEvFhTVru_rQlv6pVCqaXlM76lWLNu3dsMqe9YLnwxa9xwSVYcA26jPMgpKTb15ElyEPvl6sIggTyzT9Xobc-23WTiCIAU7ySFTsWacgYdbr1mlphnqQ0YXmtDC-hROMalf2J-KmQMTTYV6BwR-h-gd3e-bzdocxVKg4uPqq35teflb9rhTEte1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jWZ12_YlcMTCm20U44BQO6fuVtW2bYwWweOXDLzOywJkvn7SAvRJN4m7HGB3s5QwvTCD_Z3MVr4ALfX6E_-X_7x5FdGsfOoH7_syXsWjsV6uZ1kVhp7ojSRyb7l1C7fUCW6wU-gf-020ktAIHP3uhi95yBIWBAIEvFhTVru_rQlv6pVCqaXlM76lWLNu3dsMqe9YLnwxa9xwSVYcA26jPMgpKTb15ElyEPvl6sIggTyzT9Xobc-23WTiCIAU7ySFTsWacgYdbr1mlphnqQ0YXmtDC-hROMalf2J-KmQMTTYV6BwR-h-gd3e-bzdocxVKg4uPqq35teflb9rhTEte1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rroBBkoXSh8nQBxOkaochKKxnZsAhG2seH2FFwXrrfBhRNHyX-B_RiWe1oyClr10CQRIc_TRLA1F8YPLZ_pFJ0_niiVu4Yk9AkFkx7iVzWIlmC0twinFA9lBv3G2UAdfCYcq5-_crLsFafpzF-YlqbnQSy6sux16I-NvrS80yEK4cKeHDtJZ4XWo3se947bb7n-tfc8SZZfgcbUnF90-VauD1KaP4lPc0aqbGzPrhzrd3WlNe1pWomced0_IoNhkI8R7wqtc9UXGLb8XOOaqfcCz4a_rUunOb5utt8pdauT88B3PoVvubBPUL-c9XfyvCu8k_Y80TxlQvQc_SotKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=rroBBkoXSh8nQBxOkaochKKxnZsAhG2seH2FFwXrrfBhRNHyX-B_RiWe1oyClr10CQRIc_TRLA1F8YPLZ_pFJ0_niiVu4Yk9AkFkx7iVzWIlmC0twinFA9lBv3G2UAdfCYcq5-_crLsFafpzF-YlqbnQSy6sux16I-NvrS80yEK4cKeHDtJZ4XWo3se947bb7n-tfc8SZZfgcbUnF90-VauD1KaP4lPc0aqbGzPrhzrd3WlNe1pWomced0_IoNhkI8R7wqtc9UXGLb8XOOaqfcCz4a_rUunOb5utt8pdauT88B3PoVvubBPUL-c9XfyvCu8k_Y80TxlQvQc_SotKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R14LpF__GCVKwFXvvBJ2KncHxNH2h877nqz4iWzvtmaPgEai8QVc3w05HI7AsNMtEHwN0mYQwCTj6K29yTWDIBIyNe1yD8cu-H-ZYxV5ziMC7c99WnNzOZTLHH-BgsEWHzRdgxr8wIp6bN517EoB0PDPtATGgZy0N9iUwVnHoyWt8ePcMRwpxsRlpYF0gJlGRNXqHUFl0w7tiv8eQs7dDssRVjE7Sk_c5-PHMkehwyHvneZZun5oGDJYZR1eEK2DWFXXv0jBFgSGl6PwQtRTRWH61gsCBeXT0CK0Jo5iJHHkpJMrOIlbpmggFGHNX0WRmpiLjPW2_HUNB39XlCd_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsuzXRSvVt9vE_Q7rfryrBkqkZ6yegqvBVVlHmaibbWMvvJ-X4UQuxkujXuda-NZ-QIRBYMHAqJ1trIiw2VqZiXySg4nUsKs5pbGJQx3qR3W6Vp29fexinIkR9cLxlH5GhpctpMGkHn44iU_MeA2MY3oEZ3EUwncd2rVk_4i3cdBOkt_xslF7t4jRLIYUoup3UuEL_fyaEp9Qiejl0Dv7LuAQSxZpCSnrwaU1tpJG8Q805zBft5I8AXIB3naiPzueyPOGF-N7vmEEP3-pjKD9bsc9ggn_v6oajT5tqh4PnNuHJcYGvn5zqbolgE7J2g0R6z2WUgrEAeJFrmEsE8WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=EbdwB9VkM1StEp_y7NUkDUJcSBemfZIRK5M7Eu_jQUHYu_KFpCZsL6WGm_G-9OR3zWsbRYETzUQkvOhFt2XOxi3w_nur03g26hjfR8I73CuD14ueyEDlyuGAoTMSlzhMPFjosUzfBh5jMWwgJPPwTkbwJn3yMYWKq89rSSf7FpypcAmYIZ9c7XJ4sDxsn0S3j-WDgGqy0F1cmtM_6-AIxMWPbgBmD5pUisPO4paDnt04NTthVEas-ljUPHLgzOY0FdvzTL96LaGwM-bR6b-TQrrPn3nzKEsskAePCNBFpIZ8hh4fvsnL0Q5Vjw6i2-MMD3NoviRuSGN1EgGdM3dF4ZVmjRInI0Ma5NkbpASTujkv6llUESzmYf4XIHoJsXGamIgjsDiYz0sKUqTQnQN1MhXKl-_gIoNh5mToew9AmfbEIQfHHeq-d47y4Nr47O9r18NSHzVaVuRnGHmr-xjFFhpsjp17Ki86ftJMHIKyRAhblUDiWZCnIEtTKvDXQcOgaWXHtQuqWLODum7QlWEAR4Eb8WoU0f1PisoJ8N2CIuJsrxpqFm8NRL8G-I1HjDoFzXlCO4ArG3GxzVDyx2YqrHbRkOpMEzN0OGZulmfOX7AwalyN567ga3PGCB1gx-SqK2Aw8VLsUDLRd1cRiQhK8qZclX4XW7bNna7TOF_RuNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=EbdwB9VkM1StEp_y7NUkDUJcSBemfZIRK5M7Eu_jQUHYu_KFpCZsL6WGm_G-9OR3zWsbRYETzUQkvOhFt2XOxi3w_nur03g26hjfR8I73CuD14ueyEDlyuGAoTMSlzhMPFjosUzfBh5jMWwgJPPwTkbwJn3yMYWKq89rSSf7FpypcAmYIZ9c7XJ4sDxsn0S3j-WDgGqy0F1cmtM_6-AIxMWPbgBmD5pUisPO4paDnt04NTthVEas-ljUPHLgzOY0FdvzTL96LaGwM-bR6b-TQrrPn3nzKEsskAePCNBFpIZ8hh4fvsnL0Q5Vjw6i2-MMD3NoviRuSGN1EgGdM3dF4ZVmjRInI0Ma5NkbpASTujkv6llUESzmYf4XIHoJsXGamIgjsDiYz0sKUqTQnQN1MhXKl-_gIoNh5mToew9AmfbEIQfHHeq-d47y4Nr47O9r18NSHzVaVuRnGHmr-xjFFhpsjp17Ki86ftJMHIKyRAhblUDiWZCnIEtTKvDXQcOgaWXHtQuqWLODum7QlWEAR4Eb8WoU0f1PisoJ8N2CIuJsrxpqFm8NRL8G-I1HjDoFzXlCO4ArG3GxzVDyx2YqrHbRkOpMEzN0OGZulmfOX7AwalyN567ga3PGCB1gx-SqK2Aw8VLsUDLRd1cRiQhK8qZclX4XW7bNna7TOF_RuNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFq4I32pd9sOD8PYVQ6V_t0UwqZWQzk5iqoFj3gPBqJ4pT-7Lo3C_XFf7I02BGrJDjNHNdNc7ZoWVlmMNhMz14mJTndOI2-r3NpP7Dz8v_9Yuul-Jo75TtLZCmNdDZWTflov4awk2kSyRYPNNF30QQCxfD-DyWXsj3BqaKVQv_nigY0m3ZeyH0YdLtExY18zUUOa6uRBBFLihiQxArEPD9f0PkjdNzigbSSZRDDnQptnGRKkjQwssk7wFhXPnm_qjki3d_wqvlAeOhxVXl3NMmGGqLhavAtqS87UFkBwZgmw4iKPWh0cahGjyvsdmeJOcicIw27E1pyrzyzXn8O46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTs1VILnr0rCy0MOTXOgqR-6sMkt92B_d1dXEGXnYUJO1l3VmU2k1liD3ys8NfX3qhy5vOjPqCehMyu2Wh0Z9Tt-mPvaHr0Fv_pQJRgctH_IhqKxlIWRYHLpOpo32ExYlr8PB51acLM3Yq8FEobj-1XTaxXc9OHU0gtM3Nu29boVzJ8GSEAG_9nydaR8rYj0tNBTsl54HgoxBvdZaMLmDWgjTEmiNtq2PHjiynY5Qv9DEPqVRZPn_KHAVjhf_8B4UALxnb2HfK-drapwVEQNkvp7Se9n3-vBi2D2N4YaleZFN8nHv8Vfp5AxmoXCZoKkXboWC8vBvXC_MEntNIQVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
