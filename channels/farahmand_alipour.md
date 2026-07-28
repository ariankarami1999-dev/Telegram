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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 03:22:13</div>
<hr>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sit4uA033CUIRbAlhpVWu7DCw-NmO8vCoYQMSBnOl98rSbm9oJvNlQI13kdfGDH4Tf9WpPPCkOjOPTa2G09FrHpx8AFbGMzL8a8SwReXtnlRiBHziqYnqovdfVg-EQ6r9Cy1rOJ_fccqwCjm9J4-IPgLLO7CKCihEgygxwClLAdXMLdtu6bOq1APtVe-w0NDySAw_qo3TPUkwxRhPeeMgba4H24UOZxlvOggcEuCs0ICqOtBEkKxB1dfO4dZZ9bne7XHefvHruq1bwN5t4d_53MU0gNpGWji8EC0XzrUukiZIrzprJaOtCTf9VKcrBehK9SiCxHBqTSplix_xeNxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I57wL3hlgAgSEOjtELYnr7GnzLT9cwzyt6-BIijwfmHSrlGn6OPgBJwzYZFLcGytBk_jiQqMZueHWPwFkl7pK8jkcK-sR8h3ba6UzDStI847gMV4GfHyegeq09bSfZY25dgKJdrnQVkH2e9sXF8x9ahh0ItMfoQboqDv6I6leEhbGGKrgFgVnU-EOoW8rn0RBSGuwvJwlma9mRnrRWBpdpD5CP08r4FJBYAPumP6VbKYe_0QWlDNHYOfpsAlzZ_zQXI93EALbvr-XIRl_b9A5qZ598YedrlVUdv6lQ6qI4uu0FyKPbeptXkDnhQw1CXgxlzFybs1DE-VesMK4Ux9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cix2nW-4fH4QAK6cQKEaAX6iv8dtda08BkWjpBPDpKrD9M5cGTaV1ijxzOd3U7aAqgVQQ8CSECOU9HKrAGE2OlT3ob1G1g-pfM-ygrkh1T1M_xreZipaUNc9iTDfE0f2l9UZ16Yfsgv1TYWrXPEyGJxe9ynMcFTGu003fH0ja42LXKi07EQqretkTT-Cihs6dtDFf4l7A3HPFlOwpp2EFEqrvkGf_6UkZH6XLHmRYHaKnTjY9hbzLkvmRuzYuc8ZVGiF0ya93Y76f2I2M37Z0jpOHZpTfqxI6ENWQVoiPgr2BoISQZa1SLZcv8CoyMbyU-ofJYn8Qmn9762E_LxmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fh6tqZd2kTvg5oCTdii-7We3fx6yA1gsoQKtfvo5ZMIYJcdSB7qhiM5JF_X_VKsS1hm0gCqYcK__3YFclyBYlCl5tPiG8r8-MakLqcuACHLofctApc234V7SUg6R8roam45SabWfmoAg2ftUmWa8SBsRxXVQPlj3nWKRCC1yb3wH9ak7Ee4hBcptellPgl4hTh71InI-Q0qTZflKOoAHjq0hhgJoR6AvMjUlm_d9ccp_0FI37d2Vd1-0BBY4NZbtUU8AoYuH1uIKvzLh-Sp6YvVO3GFPfpMYVN9lcyROTWPxn4Q9ozeXVIs17qlS3G3QHxBE0VOagF2cYTE3OebU1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvLV_R7thV7p4R1XSMQxigRWeke7cVCrMr9x4iBvJBcKqePQt2tEBeRDyj4MmR2M1Q2IpgmjmmXK9cc5KYQXsLv3Z6DM6ASCKeh4IgWnO-yj7t4qBFtOa2Fyoudf54_7-e15a35MnEPxtG_rgeExKBBDav-HlwX0oXVQz6En8_cSPHfyTxfqAH6pJdPu1m_v-BJ53iD450a0JXg6gFGNiAm9SdNL2GOIESr5_FIz1lwbszCZhxDeOYVys6CVidxVB4_8UwTl66ogagXPssDrT-JqK3reSPf8uWBcDLq5AuVePK9iD2YqWmiQsM2HL4Xx2224C6QIDSi0j2jL9Km2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf36iO9hNYTwP-OtDx0Je5PtguDuJwH9pQvosP3wOFq1ffHFA3r6RrAkteayCR757NTMTnGQ263Wj5TOL3O3Ys46eHnIqrULsFHtoST_amiqtwVRVicyLotUzwkYiTFw15_VaMu7vuKtjpgX0UX8mp7ZhDGu14DMi2BK7gDAy3_T-X3Bz1feq7nzNkCAe6_As7vwpX5yvASR0qG8DxA-izWeo_HE4I-lejdiV3mns0wsofo9KzuibQNWIK5KHuz528Caczz0VVu3AZP8rue4z8_L2fWKltCPaMw8I7PfYHmTgWDbbrC9z3TJJ66mE_wjacJES0irgipKtx2Lr-Y4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4K8zlHq7N3t06XTEDgQQ36WXptO58W0yjmQe_9Iut7xI1h0PrSFVSKhxP-34m3wzpFrD7FXP1hDeQCgQTVZdkCLSXQV1vvG-LTcjYtN9GOSnC385Ve7dspEqNaPuTh9Ky6hr1lIpoVa4bcgYBTOFOPgxLacWYvhn28HSRG3ujtOEaKxl3Ec1M8a4adkL2tMos662U6TIXCNab1MZcXUHF8TJAzBAwdSk0WdStRKrXsHentIAkaVLsMg9lnGGaKWaNmhD8c2YXzX1aUkXpYIwh_fDHN85P3sybiu01yGc80w3kxeT0t4JvvZsDZmrV3sPTqBv4-2aoqM4nULbQ7bKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOdMedQHn4h3CgSriPM3ZA_o3WjCZX1Al3qX77SWgOdDRrklLDwV5Sio0y-oTcwJnYjYP2_54u7LHEqZjsmcldlzGTe3xUBG5ebc5BHmoCynKSan0VtX_Althi03PO-EdrDpta7muZE6MAW-dHixNSrHMBQf42LyvSdYm7MP9ttc9-UsffF5fMk9Wzxs3aReC95yjRmPU-E1h9WxMlgijljgc6p4Tm61UiTZUcZHz-6aQ51CeOaqcslQV4x4UNR9tKwm-8GDd9GnogPQTOeEvSGuYP00FB801VRzkP3S8VyRRcNrmEWFauwYADBlnbRd8sSZ-nLn0PETpIO1OSQmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lchqv8x5NBZBvyc7lwc8JYbqrqi0oGoYKxW8K1rztOJkLKRcpoR4Fsp_gXLldg1ldgTf6yowSQJYUKLRYT6qKx5q_r4AR_h25dx-hTRtNtjwXNYjEn2vlNgZuE3eJ75BzCEe29Y4rT8b8TNtWqXslHcpDTNDifHQMosRjjs1hZdYyE7GN4o0jMlblGpx2XSb_xjdNPv7sGDwA6XIX6BQ4ClyhKuI26hyTXgL5QH0E8QRjzFfXGjZGhwT7jkXRwfoxj7oqbHKdwTqE0efBQq1ssi3IfEBEVWz05jqsves5cRlBLhvf-XGhq75xvsugNkE-oy5FUejXA0IMIxdJVVW0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpBD3hbOdkCnpMRxq2GV7xLmDpBlaXI_ylqArzXsUi1sFZw61-ZOhfkQCn2hiYI_A7OM-5a3AJ3GGTOUlbLVh389B20JZq68EbK0dXdfRdCJe4tJeNHR8sOfxwQzkM4zC6JA7thNKfxfabMjzURMWabpX4geDs2JuM2Yd_jCBAi02qUdhra73PzBDJ51kLJ46_XNWVUnRQ8Siz8sTk-VVwkAAnp9bq6WkjXCCZtZzT79_Wm9N_i0YKjZx4tAh3E9M7v666r2foLkUf9-eORGlk1medTqGFJcFCp8QmKbkdk0VxTOnFdxClKJNBPW3qgWAJBhfJvKF5HVRbYf670hiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3dVGozTn1DOmBX-eLUZwzE8ABCyAMcgoC4mpmwbOPQ-cCRAan00o-uE5Ac1M4nlvU9NzSa_aAreZ0DtnSQrA-9rQ9d8jVtbftVOa1kWzKocIrvgdB3iLAW5jmKqxxFJjruE8KBqywD6u8RdQYEnBGxEAT74FfScF56JlLKBa8G12e_yssSFgjFpFt_CcO0Lk00JvzMKch9vv1ZvvSFG-Z1FoymgDcFQ1gQNnn8Sw3qGw1Ou2zb0Ayj9ObxCDG2P9jHRZ8uzdG8D8EGsfVafC2hiWDEHvzt7CaNZ9sHpzAeFcd2qmHfxyLC-J5Bqn-PQPRUnID8NYIFVETQ3GjmZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6oBz0bsAFM7VnQCKUSu-ocPz9ZC0iPo4URhsWByQbrEALKsUiOS2XMSc-uOPGaucwUyHrDqJLRI-xCIxlL_Iyq5wJ5DPGf2YGHXSSlwOzvNtSLggPj9BJySAIKzX0CJVRc--ooSAfXs4qNfPEj8rOxeh-xNrloaWdYuXHJcmuA2oZDzvZ0EmhNbmVqQwIpAtB0CE3kYbMbnnjEBbymEZjEKoVYd_RuOoMP_m-7TcaUWC40PFbJfDpa0mlA9f-IPxjB9zU0Be2xjUgP6PBJ3gu2hzCtyQLNqserQtasCTHofWzI_E7Lo4eophVgjsQ9OZcb5qvLrjMCALDOq9ZVcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oxk5caku7fSoBNSTzzW4OQD4dlZQcFNO05lTJYx8Smrfvk5lZYHsGDWGjsUvlxvqDzigrja2pn29Z1KVHMe9GQRM7S6QwWi8kTfNyHQ_QycOI4D_2s7-o_gkuSe0KrX9kuNP7YnK-n6-XJzIIGSKmkWv-dYibV_BodzQreQ8pHYWv6vJySqkrFiMZppDc_gRFkhS4URPpC97QrYUQ_ehe1rVvmQzqEPFLjv1Bh3_7a9LjZkMg-QAMrdJfzlCyWQFko9Off0-NHttokzHRUQsEUsHaGaXmLMirOfmwp5ClA7s5Q1mMH_HHg_rTAJYgv99U88m2PJYll3OT89WFIyXfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzUKsy2N6OOzcxgq9VcCCzmGuGa-5QfPUWyMUO_y9PvyK5BDEU0ZET55Q5z2oUrj5Yxylkw2bwJ-3lJVE0JJblvFZScnANPx5BLl2OdJYUeSWCK-gQN09wUgeBj89b_aPh5bkcaz2gn6LHMj87uvicUrI3v036ISN4aMZsjXM0BipPx6-lM_ZrbRapPd3RFx8JshGeT0NCQR4P_GiCYu5Q1GgJNjgEmN5gE3jO9M-NiGPOdgGsVO4WjXuH_8lua-8OEdLn5_QamXqXOHCw5ZN4ebWgr5XxGXc7HLWaENVxFKw_H88m2mKTVoMKtSMgW3ovR2eg8rPb8PjwOFLfP-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6a82lIwypWrLuuxjKabIBUG1SnFAAaotJe8q48p9sA9t1kRJD3LnANc9p2A-wKK0VVJB9pVNjrWbW3dnIcm3jQR4hr9hN9vAFi4phBd1x-2Kkd8DAWOZu8oDBnhUOnyje7IqquWD9iz49yLzU0adxnZzro2HEMLKE41kcOdPeXBItLh_pJk3OTeQ8l9FsNKrmrYfncxWeWGttgmX9MGYy7t1yOH-R5ipvxMLudG_QdzkBFTeF9AcoQ6cr5yZcEnFaccE2sbKZqZaORAlxzi3q6dzLOlxWBjXT6uryl3LxdUpE-D6PBI7UY43LsmhnJ2dyCq_Hh6v--mQ_87RnNiJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXlqlkgFFq7ymwZrkpF2AGJ948pEnvSBmXi9YY7jjW1BzTp9oSFjE_HCQd6Kk0rjhvSnJl0BC7UTy-q5N0XxzHriV5GnVM_X_cGNYfV1aLb6emwVsIamiwtClgME-Ea0nVZeuZnJNULQOGITsXkdEhraOVtLdvDfvKEoWi5buYKzdgF8HL6cGc430rRMdAKZPj6a294oeV-31gcAgoEfcZYPgKQ8wlnmXdUiC-ASiJ3c1aWrDqud8BLsdG0fRZKNOrk6IxKipqLBVDg35tNpA5KUix544VxIoRcygISdmQSnUeyBQPcd0ykgsFyFhkT6LKl5RYYgH0y6-eZ7lOszng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=MJWCbDNLvz280acbfmFyrWVJ1qPJoUzJaQTxEXJuGlFSU9NOSZwGw_kPMS2coi_GpZYX5LjCzCRDjzALTKUyt9QZTzfUAo1mJBAs6sLoPvQBCqMSiPtbMR6-AP2YRPtum8w2G49koe2ctiM2mBaAFTkGJ2yf9gUv2ZdRpRDOb9Fi8VgN8Vxys6HZEnsHk-ULMfT1b77b7bWDiRkBtwKUI8t_b8uMgloBLs5Epel_UOC65BKmkExxExtigab4NWOxMOjq6CVVV4PL0lBnWmLGmf--4aN88YfHgnEXqnZBfjFRfz0Ng5wGpe6CqXGQaz0kILnhOHceMJoPdc_MJ8igKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=MJWCbDNLvz280acbfmFyrWVJ1qPJoUzJaQTxEXJuGlFSU9NOSZwGw_kPMS2coi_GpZYX5LjCzCRDjzALTKUyt9QZTzfUAo1mJBAs6sLoPvQBCqMSiPtbMR6-AP2YRPtum8w2G49koe2ctiM2mBaAFTkGJ2yf9gUv2ZdRpRDOb9Fi8VgN8Vxys6HZEnsHk-ULMfT1b77b7bWDiRkBtwKUI8t_b8uMgloBLs5Epel_UOC65BKmkExxExtigab4NWOxMOjq6CVVV4PL0lBnWmLGmf--4aN88YfHgnEXqnZBfjFRfz0Ng5wGpe6CqXGQaz0kILnhOHceMJoPdc_MJ8igKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-VWrK-Zyn7XTVW2N7XZHWvWMWOzrV71z69N11VLMF1UWkQpRE-toTMnzD9SE8PU-y7erOjrg6y_5kfv-RBWs0FiuvdzO6NjJddXgdeUxUeJ_qwSSfUBjFTdtjWqOdgSq5aIEAsvboPxkh4VXtsE8UG6gTEPDP7SG-ApVoYfaVj2P-5-5PD03pnH1xHf1KcxRVYb052q5_-XUR_FC9w091A4kDjPv3i3yEd8PHZGU8wBV4f5s1AVAq0DKDzmWmKtjjNA_RGCiwHhfQPkIytqqGxJU9llaYIvh97Mv5Q-Ax698OlPM0V0cBQG3fRhVsyKIQuqHDWN2zoyFTU9QC7zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtBOCgZAjpCUp_xOMRLYxEtoFwFfq8B58xdRUhUqV95v2ism8GicD4idwV4yuaiLfP-cqcKQyyrxvv3PEaIgUEC70oh0DOQh97gOnybb6yl9ZXmWTPtGztfkKD9kK81sN8i_ORFzTQgO9fcSwRdfjzScvzFPhPyjP-kXixG0xYa61VRYIZOFCuiLzLjiMj1BSrg5Ckfojs9Ei-xzuW5neKOxlAhv_PtlpadWSAbbdr6U74OBCnOgjDgjGIupv2f5FN9dNXqPLqOJu3wXu1263X1B1PvdhocgNK_DGbScmTelpioVsDTxHbs6ZULH9iLr1RTDleQPgAgIxiBEM84uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI97iWCoQ1FwyqcBSixzsOjuuhrSZMYtJsCNX-wxGW2lGBCMchkDjWbmG2vprYn3PQt9mwhi9M770hOBCwaG7AWKaPUL9VvYFMSUx4E-p6tBYz4LTwQKjZa5T6W8yYQRUMcohj9lQO9LFryTTon_1CmvnhFvIim8qe7cYrtp-xbUjj5WfJXUnM2ZYb0sd4N0ykQDTa2IOZMLBJKSzZDgxlvQ7pGuT3WcJ_L3BjJ9bslXLbt-xXg_bDI9SNO_w3wk58noUa63vn3GCHza-GcfMZLUN-ZPD3tkZlT9ast3JI7kDZe2N0QXd-eQOfvj8RmvBQ2PcW1EhJDcc6JKJADvIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=r3ZL7L__23_1X8Y-07t9XsasuHYkpvTi5XdkzlmGwvfay4dciK32FMw3pExY88s99ZqXgTBSlJ-Islx2sDEtrrJbYsNdTv5hSZRxEas_cKrxLreem1q61vYVQtDaJ_3aMiQdR9PzR1sgVaGBl5M7G2rnSljfk5SCLxsOWJ9KKu0Jqs4_X9JaoVapdlaepmt2iz3Mseuo8tYs2hOll08bcDvVjEVPRW2DnloDBFETaQJeCkdF3YcxNgKa-nJqRGmroXHN88s-_xZNTTL632zIFADSG86MK6khJw_-pO9PB0KKmQtc79Q34LrdtAaOESRdvoNR3JVuneO2J1t59EJy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=r3ZL7L__23_1X8Y-07t9XsasuHYkpvTi5XdkzlmGwvfay4dciK32FMw3pExY88s99ZqXgTBSlJ-Islx2sDEtrrJbYsNdTv5hSZRxEas_cKrxLreem1q61vYVQtDaJ_3aMiQdR9PzR1sgVaGBl5M7G2rnSljfk5SCLxsOWJ9KKu0Jqs4_X9JaoVapdlaepmt2iz3Mseuo8tYs2hOll08bcDvVjEVPRW2DnloDBFETaQJeCkdF3YcxNgKa-nJqRGmroXHN88s-_xZNTTL632zIFADSG86MK6khJw_-pO9PB0KKmQtc79Q34LrdtAaOESRdvoNR3JVuneO2J1t59EJy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp_YYz5pnkOtg4EoizBHeth8VYCyGrMSXcbElGZpbstwHHPUMQYmkdENh7LocaKe39eXX6HWX3U5dZG_xClbyAu1wqaqEya2eA7nj382loT_UZRvP9Mn9slHgRZPQbgyIWMZjY_Tz8g9o84FJ-MHtJAYB3MFicoA5MeADBxO-XrT-QVVl8ttcToZ268d1rWJALiHfLSxFV4qLDYiDn7a_H7D4Rmjacyl9gJDw6UYezperk4urcxNQ1Og23wwOfi7qLpSK2SOBzIsKvD-rn_-o9BK6VdREG0n5EFge0eqo2-Bfv1s2Gae1ifo6wkFiEoIWSc4xtT1JKekUNZkWAzkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=PoMQkvzgW8ABPpYjAk3SxQuKcJskShgxQ4s8TaVYJN-XPhV9rD6WfTDMvM8PJkOHwK3zXVIkqfUoeOVIG1uCpkb8RlYt8h7yZyZDoZpjiEVqlE9SUwIzudOZaiuAm0t6YXvPiLagdlpj7mvbMUnawUrS6GyGyd5sYhdTCs-mY85-EeshD9zOTEYHeQ6pHoTNZx9F_q8nxrZ2JcHduBT7l7_Z1PBJtrpP_Bd-XG3ylYg5EdjPHUDfZRchbQSUDhi4t9c17oIa1bvsC5rV9ZncNSZVJOYZAyONpRMzLsB9bpZYVgtS5A0-vlyMkzkmm7hUwYazBpeZmBzIb90T0ZBSdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=PoMQkvzgW8ABPpYjAk3SxQuKcJskShgxQ4s8TaVYJN-XPhV9rD6WfTDMvM8PJkOHwK3zXVIkqfUoeOVIG1uCpkb8RlYt8h7yZyZDoZpjiEVqlE9SUwIzudOZaiuAm0t6YXvPiLagdlpj7mvbMUnawUrS6GyGyd5sYhdTCs-mY85-EeshD9zOTEYHeQ6pHoTNZx9F_q8nxrZ2JcHduBT7l7_Z1PBJtrpP_Bd-XG3ylYg5EdjPHUDfZRchbQSUDhi4t9c17oIa1bvsC5rV9ZncNSZVJOYZAyONpRMzLsB9bpZYVgtS5A0-vlyMkzkmm7hUwYazBpeZmBzIb90T0ZBSdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfUUm85mKVAXKJD5WlfI2MKKZpb1naeHLX4DZF8exKsVVGOEK3aBhOUEMvDNsliI8n-KnOlHgInaO5bO5d6v4lBJdGfWSWxsgcUPFCG9cgLthewZUMqfu864aO6n02lENOqOENBLMQBRqqfa5QnFSr7uSz_aAxYbs-ugV7Bk7qBQv6OVUi4NAVCbEClpxPn_J4gkVAEX3r1qFiLiapcIUPUVsAMYuOvGHnCI9Y6XzaW3MA_QD-Ubo9n5C4K3wz_fKQldcAHAaXTbB79CYADd1xXcErv0gzFovPzeWZYoEbiJWLE20fzKW0X77-v2CYUxiBsPL1IhY9mqocQkQvhzKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmCxEobFbDJCQ297WHJA0oMKT9k9dOqYYhUhjbmXpagqhs_iCBQCCfCuhl81TMV_K4WbJN_oNI8znOZw99sp0exH-TdJYizXTiStcvaHqFaa7l_JOtgcCvFsRTuQjSNprk3CtPP3TSQPjyfYMUa_iFyZjdmYYy7XIdxiouQS8FaymIlebVEWVFOqfPuWiTnmpBfB2Fq--zhNViS0izvurF03gXTrizQM0VPpQEv1wCT70RNm9vbBpbu0AiZYFkjHaXErsZPJm7lqhoMh-tI_bSgKx_vuCgL8saahSfjbcxee1Safm3-1G0nrpsPFhXdAKkUtCKquQedIq7sfxPxZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=uZzpqgmEg1w14dfdY0gUzDEv2Cxc4ALupi1RDWHNWe0fRcirY4j0j-NsMKfJB9POkphQHHX9C8xePiR297LWRa8RMm7pJBLsS0_cg2ltF6IlriNMQRNIciJLr5iOu5IvgZqX15vw4MyUWL5c-c4o9JHfulf5-rlWYToPpLZGeD6Lh8_rnqSlU-5Ez4VTSC1SndnylopZMp7Ejktyaa7XpLLXsFWXuHYKxS4b0gRLW1wBFbS8IuMnLR80LAGzNUdu7eMjoSxIL3mjD5vgLccnyyHVPsZ654DImi2RcoXpsJOonSvyfbhaGnEoVf5_wNDVKTbcV4TlrL-qDLbADkUTg25vWfvPchp4jWQNUZGMAF85MyxyIG_N9ivMA_fAZewJJoh2Sj_RSpcVn0AdMlU6NBkXhSLtwZhqin-NBPvIZjoUuUW8eFbCZ0ELgf1EfxR25SBhymJcsKVVdhSAINHFteJj388Ep2yFn1CwpOU9ieKaOvEVNmVWowds8Lb37t-u3tbB4sVOCfnBTpuOkzzWyd-6Pz7tQ_TArp79dT1hMvqzLIdCm6ly3wqtR38OcnN5IpXQRVaLLlhJpvt9sgLDvndhpm0REmyzEd084Se7qVPHDDhGp9F4ze836nXuwVcJyfpFvs1zMDHAl_dBoV4eWTy69UoFu0UqX0XwotZREDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=uZzpqgmEg1w14dfdY0gUzDEv2Cxc4ALupi1RDWHNWe0fRcirY4j0j-NsMKfJB9POkphQHHX9C8xePiR297LWRa8RMm7pJBLsS0_cg2ltF6IlriNMQRNIciJLr5iOu5IvgZqX15vw4MyUWL5c-c4o9JHfulf5-rlWYToPpLZGeD6Lh8_rnqSlU-5Ez4VTSC1SndnylopZMp7Ejktyaa7XpLLXsFWXuHYKxS4b0gRLW1wBFbS8IuMnLR80LAGzNUdu7eMjoSxIL3mjD5vgLccnyyHVPsZ654DImi2RcoXpsJOonSvyfbhaGnEoVf5_wNDVKTbcV4TlrL-qDLbADkUTg25vWfvPchp4jWQNUZGMAF85MyxyIG_N9ivMA_fAZewJJoh2Sj_RSpcVn0AdMlU6NBkXhSLtwZhqin-NBPvIZjoUuUW8eFbCZ0ELgf1EfxR25SBhymJcsKVVdhSAINHFteJj388Ep2yFn1CwpOU9ieKaOvEVNmVWowds8Lb37t-u3tbB4sVOCfnBTpuOkzzWyd-6Pz7tQ_TArp79dT1hMvqzLIdCm6ly3wqtR38OcnN5IpXQRVaLLlhJpvt9sgLDvndhpm0REmyzEd084Se7qVPHDDhGp9F4ze836nXuwVcJyfpFvs1zMDHAl_dBoV4eWTy69UoFu0UqX0XwotZREDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bTnWQaxVDXtyiWD_yJmVONT1dLZCffu0DzL48stJugrwBDhk0bBTrY_PWluOAz05HYVLsPAaywY19CRP7AKeomZiwFsSILuVi6Sb4huVslf0bgj7DOiiqNuVypJNbwxM5Pidhk0p62uuq8H_MylsXDZU8kzJ-VCDcv45xP6e24h5pXkGU3-zexGFrQWtRrvtbni8v-pkbRrU4vT5dwRDzmDAV8F08m3-2tEDe2vE-0udZqpK3I-w3f8JNN9WHmb9pj_UjOKqwEo7h0o4CKRyloAT5NjrKVSokVlBzQAEBhAJjwNp3-AjPDxpLu-RTD3WuidsMcxmw_oWA_0qzLOTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bTnWQaxVDXtyiWD_yJmVONT1dLZCffu0DzL48stJugrwBDhk0bBTrY_PWluOAz05HYVLsPAaywY19CRP7AKeomZiwFsSILuVi6Sb4huVslf0bgj7DOiiqNuVypJNbwxM5Pidhk0p62uuq8H_MylsXDZU8kzJ-VCDcv45xP6e24h5pXkGU3-zexGFrQWtRrvtbni8v-pkbRrU4vT5dwRDzmDAV8F08m3-2tEDe2vE-0udZqpK3I-w3f8JNN9WHmb9pj_UjOKqwEo7h0o4CKRyloAT5NjrKVSokVlBzQAEBhAJjwNp3-AjPDxpLu-RTD3WuidsMcxmw_oWA_0qzLOTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmO6qOYJTajgd5gn_9dHckTpSK18ZhdHDnIcXyJ4DBvU962tnLwbYtBnH2yslpOX7fT00UMY7X-jPf1si_kXk_lbLtJT0dVjt51ouqWVKeVjfF1Jn0X7mdbfkXDVZj3VXyI8QQmdbALTbitroEFARnsyJFH6LwHA8pkpEJSBtxgw4EPJqiapDa9bf7IO96LhLZaW_k_JhdfejI0Iv2RRx0ShnpYpBHkAOs9swvM6knm5qzoc0bg2SB19THND99dEmm54ri4ucBRsiSb7LWrrGaqzImppfytgM0L4jAWawoblQIgC00x1ccHM-iFd0TwZ8AwawN2Q4KCunbv-UtWxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=lkkMyR7mHTf5_z3g8R_XofhKis7WUG3YSoYMcf8Dy4FUkFNegtSNhVb7KLNY13v35DpGoXPrMT7QwGg40BP7W8uY7yHtNgJOZWzGBSUbbNfJXkh8CaazVWxyFbZdkFiZZ4yRRK0RpRKYhmL-UXnGMETYbddNQUw2vFK_7AUB6keVBmfPUpLL5k9WSE5av8Cov_zYUf6KogvZ1JzsRRLOp2pZLnCM-MnAGRU1JON3PJWeFOC-xB0NWY5BmH79U1c4ez83E-tR1hreEGuNTg7Xbh1szy5X0oisR4SIoHJ4GNr8wqev8yoXJyv-fwXJHehrx3JqS-X_o7epFu_aTNcS8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=lkkMyR7mHTf5_z3g8R_XofhKis7WUG3YSoYMcf8Dy4FUkFNegtSNhVb7KLNY13v35DpGoXPrMT7QwGg40BP7W8uY7yHtNgJOZWzGBSUbbNfJXkh8CaazVWxyFbZdkFiZZ4yRRK0RpRKYhmL-UXnGMETYbddNQUw2vFK_7AUB6keVBmfPUpLL5k9WSE5av8Cov_zYUf6KogvZ1JzsRRLOp2pZLnCM-MnAGRU1JON3PJWeFOC-xB0NWY5BmH79U1c4ez83E-tR1hreEGuNTg7Xbh1szy5X0oisR4SIoHJ4GNr8wqev8yoXJyv-fwXJHehrx3JqS-X_o7epFu_aTNcS8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI0KUyyrwCghVZw57JfE3EowpYRUEp5WjUWfTIP3QoVpyLqTDHum8cZ49uB84n3y5fQdkekA7kOAKffhQjhXdZrYjbq6kFowF_qGnO8R5IXF7ZsczUD6NrQe261ZYbfX2-glm82NoI8vPCUB4iEAJqxYy14APW8_T78OduDDflQ5_aT84hUiWqHydaBtxP_EVSTYXIFC0NYoTqXUE7kql62InsQRA5vymDQRld4ipPvxC4g77RjDDQe-1aJUsPpQp9Fl3_LvAR44chyLmfyK-F3XIAQcNxM3bLFsejUBSdBS1QEmATsEgvf9xa7-q6OJHxWtkoTlWj1ISiPJx0ucQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAFstGPL4gjNnxnioc3S14NSP4iMwPTaWBA16rJc6O90hGZnpd9FjbVed3iwZv938CSpxNdWvalQgcaPqX9voIwZlQxXc1Rs2vekRgKtHoM5Ew3iRm_sA7tzc72uOedLJZJCKnPD3Xl9L_PQvHa3sog7NL9ziqtUMuiT70PaTOpWQtJgB4yslxnEfZn7A8qy1ng92tbppVeD2LDUTLnUwzNx61ocd0NvW4d12TqjTl7bOz87eAC4BE161XDveuWMTXibiv2W8PcRnJ-tb56g-a4CFts4F0xXWCtalS5MGJzXnjo5aVp562a64m0EgEfD5uEylXHIqsdTzxxQE4GPwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6qhhtzf-zW2cGsbwzXyqVrG5Pn4EJjJkHMr2hmL2TdfG6GduMzvDdRD1agmrMQcmm6YqjG_CGW9ZFjQYG7joK9tnm8lYYHUzZsas62kksUvpdwEUpDeVqN3EtuGrTC8HESWu6qShmwfZ-z8BKSZcu8MNP_bNa10QQ4FStadriLlxGyGP8l4RPVR4Zg3vbHL4g87gtax_5e_2lDm3GojvcouX3E8W5dSSSGI4KIYArTbYXtNCXTGg1ldVw2VoQArD4mTts2zlX5WCcItgEzJRZJF_450AgVzDSwTrbZFx_uUJSRhJvSUdU756cxUHy9pNFbUw_a3DBK0gn3sHySesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGZ2pBF46brFbABh4vRpUAVQkfrgAU7hSCcU3yjm07CWpDPgcITxBU_yQD2g7n5tPAtMn_tpeBI8E3h3omCh05MoZcQWCWdg92-C282zSCNhWxkFSMv67XXP3y0sj0MqaBEHLHzNozN4-RLEENHgpj6Zmt8TnQ9kcXmeSDOwPpjV6ux5HBYnobcE3rXYWZJP41JgqrSoi_NOCUlgYvSRn42FsLORltubtbszOryhTi6m9-QOJ_Gn4FxOymeihCnYxJ_zbyZlIOFBYgsUx5YePR2N1YmcrZQ6Qb1xC61BExVhqFHes4fmfR60vVuVsrGZvcXm2pClPr2xmqPg2WSnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGeCT3D3mfwIxAivXKPh3hNiOYVp2vr6yX0AxAE8bzub5TP-1dih4975BjmikvdZmuhLdmlwOaQi0EgpDssoxYjgAuxoRJ3RJwyFXX2Pyp_EGMnNLPV9vX2dDTHxJwVn2-BGu3PoXWjWkSgbKJqI1qjRIohaY7U4IbBrqTbqmjNEzz9dd5DURGF-lZrvgSoUFu2YCMh1ML5gLXUFZ8JP0lPdAie_f3nazUVefwWUz0WFlgE3XVkp_EnYTuJ1Z-83-kjOhzHEBqIouhwGgXKHtE7n6mPujqN_iKR19acZ6xzFoMV-NW3eu752AGwbV8ZMBo_kn0ugTmRFEbZtVeTjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=KJUcHcBxqv0SLGdV8-Xz4mAgcc3JX7K8dGixkj1vO1LuuWuLNMdRgWMswl8m3Gv260NlqceQn0k1_6upAZHwBspQ_7kBoDKLMcKOwJtBpqg8ZeL0HC2sRl9rxtsL7Oq292B2jr98BXy6NLucRkO2DGygkIJyVIOvSkRiblq9kOyqmOk4jnnRNElMOM1KrSB0YMg0Dto4dYArJ6DAwfl62r7rG9V4aA1ctDa-94OCjMYTnDw4aAd3G6QVoYbzaNpZNcNZTBk7eyZxgIFRWz49nEu6Z5pLP0VDdq8ti-WGCRlUn0mlz8CbjepbCjZ8HhxzuAKQaZme07y9-thFnza-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=KJUcHcBxqv0SLGdV8-Xz4mAgcc3JX7K8dGixkj1vO1LuuWuLNMdRgWMswl8m3Gv260NlqceQn0k1_6upAZHwBspQ_7kBoDKLMcKOwJtBpqg8ZeL0HC2sRl9rxtsL7Oq292B2jr98BXy6NLucRkO2DGygkIJyVIOvSkRiblq9kOyqmOk4jnnRNElMOM1KrSB0YMg0Dto4dYArJ6DAwfl62r7rG9V4aA1ctDa-94OCjMYTnDw4aAd3G6QVoYbzaNpZNcNZTBk7eyZxgIFRWz49nEu6Z5pLP0VDdq8ti-WGCRlUn0mlz8CbjepbCjZ8HhxzuAKQaZme07y9-thFnza-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQzOXYVknocSdXQleLcluQTgXHqKJ9ZDQNTAAsOcssBjcDC_Ke5YztCrMB9YgLWlSpc3V0y2H-mpTnBCuBssrA1g0SF2BFxFsV_YjQfyuWOAU8fXAw-fiTrqsDauXfCG3hg8Ryr17awpCDzs5NzASvY4cBhjZmwr2cU_dHxOkb4jOD_DYwZl2wG_TMETcMxobTd26FEVUqIO52Qy0XfdsfGDb8GtzOIU41iZpsbEn_xQkjV_vxVhPadmaL7yCvJmPfuC3AutYL02m39gOs8j_JsPuO-lIYqpclZvCz6CHiFv74frtFsRitHjvtcbGUN8SBXXyrdgM-Ttl0t4V29CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spn_aiE50Gudw-P7HJPtyZ7K-9m5Dk65p0PDuE5jdIiu5gY9noKB8qHPZ4SoOzoE0Ajgthfo3gp_1x48l_E511NXFPHSTk6nIw0WFtlUQbeXARwC2WO9HGssRhXgHzYCWi-vL1KbNEk7WVBSMRTpuNm7EtbFcy-p-OmdLTZl9LRtbtpusOR5M2mLxLoYbjWNFItzpWjsNLmScCbVx69sb9P7Uf74ZE22lJy9q8bgX_pFXN_yoDJDNfbQB-4PgZXVY3n4AI5e-WEkU8lnBIFPJrkl6CudfAxyQ76TKOAxMFyDWc9dmbsvYVrhRf4LPu-_463xr9zssCTtrNGnmBuvXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=M9vcOlmB6gfgfpLmzKuTEeXGXz4bSYWhx-U-oRquNT3nETwt4lesbEGAQ79-pT-nXz8_4vrrX-fb7UyY_BKRZGZNYGN5yKJxy3Dy3ugolA76QBoXVQdDrCg6Ro_-HvkRU5n2Au2_uEQwBnzjW3Mpt9BRjWtbpbWut4McC0ySVxu2EkQXkzZsS7FRGGvR8IQPNVk6mWsX1aiVoWv52Fk-zVqbbRhl-Rvd6uHaSfXBEK1lA-6af3VIZrInnfL3TVoZTLLJf_Ksx-XrTIYfxr_0unlFYEgxAok5yO_XbF_n6KOZn5Yn9R1e2x_YAhAhIUW6iiu0j0Vw2uSa6vda3goQJWA73qWDic3TsV-93RjCbWJQnB02PmlGn1_6nmONP5XYPZkVfU6BHLFpV2CT_-tQjqzQ6_BmOBEf_ldIr4Wey00j5EuhE83RTliltKdma904faF-sdVzVNiHOYNMRpk0UfaV63CPb5I4MaDaaCkOqKuySIo00p2BlEZGfm5NbgUF0wA0bQ3TkQrpiVJtLsD4Ym4gM28l73MiaJpY1o5esio38V-qwJom1is2AiwXj3lcdf8hxZSURPj76sgijjL4jNWSKCQ_RS2t0gZuhGGT_0CefT_4K-poBhw434gaWgT5gcdNMsBogjvHqrviaGLdQ5wRYhuZCGld1R1QzpXaHwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=M9vcOlmB6gfgfpLmzKuTEeXGXz4bSYWhx-U-oRquNT3nETwt4lesbEGAQ79-pT-nXz8_4vrrX-fb7UyY_BKRZGZNYGN5yKJxy3Dy3ugolA76QBoXVQdDrCg6Ro_-HvkRU5n2Au2_uEQwBnzjW3Mpt9BRjWtbpbWut4McC0ySVxu2EkQXkzZsS7FRGGvR8IQPNVk6mWsX1aiVoWv52Fk-zVqbbRhl-Rvd6uHaSfXBEK1lA-6af3VIZrInnfL3TVoZTLLJf_Ksx-XrTIYfxr_0unlFYEgxAok5yO_XbF_n6KOZn5Yn9R1e2x_YAhAhIUW6iiu0j0Vw2uSa6vda3goQJWA73qWDic3TsV-93RjCbWJQnB02PmlGn1_6nmONP5XYPZkVfU6BHLFpV2CT_-tQjqzQ6_BmOBEf_ldIr4Wey00j5EuhE83RTliltKdma904faF-sdVzVNiHOYNMRpk0UfaV63CPb5I4MaDaaCkOqKuySIo00p2BlEZGfm5NbgUF0wA0bQ3TkQrpiVJtLsD4Ym4gM28l73MiaJpY1o5esio38V-qwJom1is2AiwXj3lcdf8hxZSURPj76sgijjL4jNWSKCQ_RS2t0gZuhGGT_0CefT_4K-poBhw434gaWgT5gcdNMsBogjvHqrviaGLdQ5wRYhuZCGld1R1QzpXaHwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=reg16Vhbs3M_ICYTtrLewqyPEGnCCYgoIwc0EIxpnAbEFGyMn61luS7lBP2U5gbq6yrDK_B6vg4dUFvNBYaTld_yrn49-8fEfDWR-g0kkiwwPDytW8_XD49v4xuwsvcCYDXcVww_4Tp1jC_L0RJHEPwI3Qz0hMLINf7uqXUTv0yuMWWkdU9O0qNmaP74lxewyzXDiYpE37L8OlPBtRSXEW9NydM_9PFAzK5k7cBRQgDmkkGWrBEMoXVyVU0OGWnLmz82Mo4QbP1lUQmISZdBwnN48lZV-6ILyyxuxd98cZ4r2JLAj5tQkaOu3KTJjxWVM_fPen0pxVMGzKfVPAkVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=reg16Vhbs3M_ICYTtrLewqyPEGnCCYgoIwc0EIxpnAbEFGyMn61luS7lBP2U5gbq6yrDK_B6vg4dUFvNBYaTld_yrn49-8fEfDWR-g0kkiwwPDytW8_XD49v4xuwsvcCYDXcVww_4Tp1jC_L0RJHEPwI3Qz0hMLINf7uqXUTv0yuMWWkdU9O0qNmaP74lxewyzXDiYpE37L8OlPBtRSXEW9NydM_9PFAzK5k7cBRQgDmkkGWrBEMoXVyVU0OGWnLmz82Mo4QbP1lUQmISZdBwnN48lZV-6ILyyxuxd98cZ4r2JLAj5tQkaOu3KTJjxWVM_fPen0pxVMGzKfVPAkVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCk6xyNoAjNUECSRfklRfEOhY63i_oGhCorLvb3h2-3tWKi9gTbIPgfXu5FawWc6Kr75gjXXGuVRi73ntSmcu-OCiYkrF9gyq0BPrDU-RmTUM-3R4NYWEVr9ueH-TJJNn92aaQ5FAaeww_kaSk79tgCQ1Y1GiHiJU_C2TRx_jGJoGicQSxeCXxwqFfTZM3-_tWmp4f3oXTEg_xcJRaVIFAJIgss1NvE-6kSbP5cTJZFFUCWDsWHvBAtCMwTc2T8jP4wx2hm2_T3hvjsnleWkxUUVFAo4ItxHtFeUyLy3QCeBHRJi1Q_h_0t8g6zWrO5aq4CjoYqHO4A8FtO-QErHYNpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCk6xyNoAjNUECSRfklRfEOhY63i_oGhCorLvb3h2-3tWKi9gTbIPgfXu5FawWc6Kr75gjXXGuVRi73ntSmcu-OCiYkrF9gyq0BPrDU-RmTUM-3R4NYWEVr9ueH-TJJNn92aaQ5FAaeww_kaSk79tgCQ1Y1GiHiJU_C2TRx_jGJoGicQSxeCXxwqFfTZM3-_tWmp4f3oXTEg_xcJRaVIFAJIgss1NvE-6kSbP5cTJZFFUCWDsWHvBAtCMwTc2T8jP4wx2hm2_T3hvjsnleWkxUUVFAo4ItxHtFeUyLy3QCeBHRJi1Q_h_0t8g6zWrO5aq4CjoYqHO4A8FtO-QErHYNpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5iczUXb9HMarl-6rd4G87_l0cdB0JyP455RL5NKuNKORIelRYl0yWboAuKi06TGIvA7nO54c-pdU5POWs8T_HjWNkNzYzxWID4R2SJGtq0LDhm2PxM4696yiPGobCKZeE1MozS5a-o4wb0p6wwlxn5fAFnZ55TfPSkgYHy09-GkdgMM0a95GZUBPyKc0CI1jfcjFJPRMZPEa7NTXRj08fVetnTIXlyC5iM4ixRII_gyU30qG6yOj0JY145Dke91y_IyzgIRUqFt_tjIhlpFyJIgDKD3t82V1G3iqLv3eP5LjosPDF71gH8_3p57Ohot3e8_NTolzCgpqXsREZn88A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz5FyEz2namO5-RbZ5micgMbm53x16_vX41-oYt_EuWlDakQMv1iZda8J0eUIVJDX1GBBRYN8AimBr3No7caf4NK7ubAVaUdNLS7XRt9cOqHyys-5cu5g8lX9NlNI10r2w1c60vEuG7cOqrzjySTEifFKUiDQAnuqqfieiZnGpRSi8tpaSFC3Xl3e4FJ2_oEtzuT3iStWdZMdHwK3gISXtFXoTWS2FdcVBkMDUv1fEvJ924UfbopLQPWu3drOj7L68LMrJx5ov9dd812M2wL4IYrtcuIWrUAVKu63yVLon3aI8M79INV_krpCau99emxLy1mEQ2RNX2PIXFwpAjpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAjha2er-eRL1oyZgGHjZ0OIQEqbBjK14lEEIDO8a8fTjsnyk_J6SIBbUpJSYPmtL0-um3Kw1GLhaiFc7UDbmJd3wZSzxQ13xs58ooH8g7-bSDoPaIXRdwBTzprXVRYEd4OYTo2JNaWbcIIy1syCCtH2Q3nZq48-HhgCHOx9ITVLMs59XxsuIF41NoVhLGOS3Di2XnWM4TWuOH-RtXFsBO6JwtcJyLl2xyaMXL1oB4WT_WFCnSOE99qeTMCu-mUZ5Saruv44mQZzBNb0X-l6zXdlA94BHuS4noeP48zq0QU7h5tLcNAIBn5q_lVO0JTxgFR7h5Alq8Dh9yO4uWJhBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=uMPox4XkcdxBeX62RuaV6qhI6D11sJ66zAoCi0meCBYDQHIfTODVssalkkG6QUHhBbSrnW0ikv-pZ8CQsMrcmpA2IYWlgQ9w6tOAgd082ziCJZhuKiRe6BPMk0TQlwfHGyVwUPZnHLsr_MXjcHMJUJ6nzNZILRMwXWh6PSkiCrYIoMXXj3gNFI31EHES8oxTbklK7jBE4l62JXcbPFPGU2Q0VKUIiXY8hF5C9FosQFGYgPo5PwDrr9LiaTl-fJd77zudAExpfFIXsszBKpfDbSOC632M7NXAHqu2wSm1wbgyy1j2zQz1LgY0j_a7KGQ80gK4BcmQkyDa1o2XyKR9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=uMPox4XkcdxBeX62RuaV6qhI6D11sJ66zAoCi0meCBYDQHIfTODVssalkkG6QUHhBbSrnW0ikv-pZ8CQsMrcmpA2IYWlgQ9w6tOAgd082ziCJZhuKiRe6BPMk0TQlwfHGyVwUPZnHLsr_MXjcHMJUJ6nzNZILRMwXWh6PSkiCrYIoMXXj3gNFI31EHES8oxTbklK7jBE4l62JXcbPFPGU2Q0VKUIiXY8hF5C9FosQFGYgPo5PwDrr9LiaTl-fJd77zudAExpfFIXsszBKpfDbSOC632M7NXAHqu2wSm1wbgyy1j2zQz1LgY0j_a7KGQ80gK4BcmQkyDa1o2XyKR9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2WAlasgJmyGii8EPgTNG_MvstzTIUSYYSSlefV5jh2S_fHbyI4DZ-WLIVixSQum2_00uiBKPf5AUgidGVaMWQ9cVfLlHHm2lxZ5p5rtWlgfKlIohLHaO7OesRSO_3Fr41MV8l55tc_nf8nR9_rUuhfmMZuIybNo2-qFun9-atwHNvRt52qm0PPQcroLgSdktgP0aVhi90yVrfWykl0QYk7dpuERrEflyl3B49UHMo4M1-FFQ_PH2cP1Ma435sseElmhpSRXyYjIn_tdgDm9r1cydsiLA961He2_MGLIQTeCRpqdn3xOf2VII7MNmDh_ZIZNbtvIlLgnWb8BgTmOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Izm5y0qAC_H0MuP2Db0wGFqCLpngUog36iRTSxNXWDCTrFThlV_2naY1QPhoTXzhxVbEmArINeh94lvMJfdYv1JcqqFocDX5BbjZw6tmwnz2QZ7M7DN3FDdXKdvwZmpkBjPunWenS9NRTHpX_xMUc3mJJlkpdwNI1h91JBfjomjjUgO20LGMebju0RYKOxHuBTAIz-nyfObbzNQpcgRRl0Idu4P8sRnyKCQt7v0OHgqaU_-vxdR5y4KCpXtD5zivHUrwymHIUKlfEfXdZGDhZM85GmaYo-8pHlYat46b062RONI2EZz-aBC1e_yYWxXv5cE3CHxhjOQORUc1oGcdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQnmv-6zpFwG838HbgaBmKnC9oMJ0wLncZkzoEL0ultNi9cOD6OHtSlylAaVqSOxs8ehVkj26HcbwuXGImsLsUasrzFNY7b8a8e2rNnjvDPdNXmmJ2qYDPR1i8FZaB-HC4WT0hoqr-n3WNIRwXy0yGXyLvKXsADqb7t4tDUsR5KwUcq4gcliRVDfp7VWN2e2QwgvLo1VLWZ99SdQWulxgm3eagnDfEiC6Byt50zK_oV0yi3ZQUfipYlWkvZxb3xkvEu2BLtGI3DCnV6vY3djNoR4PuiR7JPiUiO87rIGDCiQO6zz18wqwFHm2_CfWNkiwCvAKJV8bYlKHxRgjMoPvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogv015Lg6h8KknM5URmSUWgwtTUpU8RMnsv4sc0s1fnUBw7lrHeQUmMSLepDpSJ50WmmXz-PhmYL4Qn8nveTBZ0zkKG5C2euwso7t_jPJycaCrW7tsbk5T8kPkYm9CYiYPTO_O7AmIpmYfFv2NBgPWgq9Sa5muswl-YfEeewwMzbFDVFNKhoUJQ_qPd-h8t1hqLwrJ6tfi3nCV_Vm7mtiRlzUjCJuRyCXCteey9UQi0mVbPeljpcM03MYxJLN3mT1gxN4kT5vy5xV2GnX6BnvAdjfvxFUvdEwn4DpdAcdK5P7WzL55zho69weO331ZaK1s6qvZL2KULVjv4qHtduVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ConWoOmvCyKdW1OmC6LzvpIuGsaCi9DvxhoI0HV84JxYJSZbed_X-vZVK6ecz6kc3P0Mdf9FclYsJ9cHw_uEaCMA7y6dSvDEnCh8OiL_MnOYwgVsq9jx1rOeye3E5KGUjQB8O4Q6o9ApkfLl7zJYl0NuAoNQzlp5W5Ws-e5qnG_tP-a6WJh9MHa5cBq3P0Pd98rnjMpfuu3iDOZBAwC439t_g4mh01gkmZLnSeeGkH6AQZQAEKzID_6kzfeRBfDriVSCbsuIvS2J390XXa16fj7lNcz9aIq0_bVlncRsbbjEXhR0hG7QseD8W0BU234eXChAOeDaTe6TlMp4kZAOsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ConWoOmvCyKdW1OmC6LzvpIuGsaCi9DvxhoI0HV84JxYJSZbed_X-vZVK6ecz6kc3P0Mdf9FclYsJ9cHw_uEaCMA7y6dSvDEnCh8OiL_MnOYwgVsq9jx1rOeye3E5KGUjQB8O4Q6o9ApkfLl7zJYl0NuAoNQzlp5W5Ws-e5qnG_tP-a6WJh9MHa5cBq3P0Pd98rnjMpfuu3iDOZBAwC439t_g4mh01gkmZLnSeeGkH6AQZQAEKzID_6kzfeRBfDriVSCbsuIvS2J390XXa16fj7lNcz9aIq0_bVlncRsbbjEXhR0hG7QseD8W0BU234eXChAOeDaTe6TlMp4kZAOsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=QbFvEiJEMlK9ZeQ3LsCrb1DREm0jqrgYAaWTJA6pwf3Abkpit_Gc30O0NwDASS2muATTzawZLeejV2V8gYikwUuFw4uKAiljlhVvceqVjkfvFKWHxCnlSs53-CnwRbueHkwXl-s3ObDW4sxIfxqWYyq3_I1XKWTku6YKIhKzKnRZGiVWQeElMX-4oyKvTJJ9zchkkqOEuUGg8FDHtgZoyXBWZW95sYET3JKc93ef1iKNDQ1qsB1KXQH_7-TXzibbWOJgekzMdvVOc499k7kPee-AGP-jkHtYFS0mzXJm2PbHgZBPW2SAkc3K6ilW1u0mOX1KVXtV7IiL5E1XCNTYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=QbFvEiJEMlK9ZeQ3LsCrb1DREm0jqrgYAaWTJA6pwf3Abkpit_Gc30O0NwDASS2muATTzawZLeejV2V8gYikwUuFw4uKAiljlhVvceqVjkfvFKWHxCnlSs53-CnwRbueHkwXl-s3ObDW4sxIfxqWYyq3_I1XKWTku6YKIhKzKnRZGiVWQeElMX-4oyKvTJJ9zchkkqOEuUGg8FDHtgZoyXBWZW95sYET3JKc93ef1iKNDQ1qsB1KXQH_7-TXzibbWOJgekzMdvVOc499k7kPee-AGP-jkHtYFS0mzXJm2PbHgZBPW2SAkc3K6ilW1u0mOX1KVXtV7IiL5E1XCNTYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CPsLEy7bE0_8uWC4E2EZF10gxp2dTwKzVoeHfEcAHnm7y-IZnEa5OwoQ9SHsHypVlJOjBxBsV5pXww428psrtktP4LZ4QCYILXEHK3-C9VL12iPDMt0OUYEYaw6ISDlFiqLZW1finqTOPVhzIv4tJ9Rl33vjhl0YK4IhdxfrDkMs9dRS4IB8Ama7ZqM3uovsFMbNnxMzAp5cuhxQ3jRk6hwee0GALw_0taFaJb62oiMUFR9HsYYYEL6HzEOlZzCM6G_h6YBmaU59oahUXxv5r8RwRSwnZ_EyW8m7KPYScVNW21yt3lOeW7TH4nMdgIh-impNHfLdOixx9dQjuPmHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CPsLEy7bE0_8uWC4E2EZF10gxp2dTwKzVoeHfEcAHnm7y-IZnEa5OwoQ9SHsHypVlJOjBxBsV5pXww428psrtktP4LZ4QCYILXEHK3-C9VL12iPDMt0OUYEYaw6ISDlFiqLZW1finqTOPVhzIv4tJ9Rl33vjhl0YK4IhdxfrDkMs9dRS4IB8Ama7ZqM3uovsFMbNnxMzAp5cuhxQ3jRk6hwee0GALw_0taFaJb62oiMUFR9HsYYYEL6HzEOlZzCM6G_h6YBmaU59oahUXxv5r8RwRSwnZ_EyW8m7KPYScVNW21yt3lOeW7TH4nMdgIh-impNHfLdOixx9dQjuPmHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNGSHWNucrXm6HHhBrvT3stLKe-MjIPJ9K_eJaawbd2QT_lzTTXgqqPplaRy4APmIWSC2eDLGXkHbHnSjIm-0JMo-HPG7GXIJ3STJ8cpXQcV0lzdhvDWA0Dsf5kQgy-C3S8rIo_QvQO4Q1FQ9R9AfWClA2htv-YNSNZm3QbQJLqI4N5k8cGWaGsapBliGsNNQLHG-Hh5RZhl0sYPXyQx8C_iy2V85sqZNzk3rXEufgsz9z0_vUnOEVPS2YHQhR3vewVGdqda83w6HfHCl-Qix9HyyGo9nxoFlnJsTnQQ6Ca0lHVGJZGiWl9IEUSBejQG6aauUUj6nkNy6eKlQYePtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QFcX-UEbabyy0OjPd2VCU2Br0yduMA9ZwneJZoYrQRAsBqlsnhEDj91Z5bM4eKllo5kKrTH-9BcHN-Cf4murgjFJBxJEB1oHcr45AsrqlcCJAmXC3SQ-h6yoBwejxgIbKuYHSWEx_X78F7WCF_ngs0sy2yh-lniF111tOmUOhaZNyCpGt3F8Z1X53TdNseiKT09lSApztxdumslGC9PefTgIOoSTCzexBWysZ0m-RK-4rgYDoLev1yT7nG9pC7rMw2azwb7S1gT5vE6xFY4GeLY3mhvudXEyK2XSgWDAuy3o1qjRb9_wW5JHLT5sxf33oQh1_PgUH7ku1x9WjIXU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QFcX-UEbabyy0OjPd2VCU2Br0yduMA9ZwneJZoYrQRAsBqlsnhEDj91Z5bM4eKllo5kKrTH-9BcHN-Cf4murgjFJBxJEB1oHcr45AsrqlcCJAmXC3SQ-h6yoBwejxgIbKuYHSWEx_X78F7WCF_ngs0sy2yh-lniF111tOmUOhaZNyCpGt3F8Z1X53TdNseiKT09lSApztxdumslGC9PefTgIOoSTCzexBWysZ0m-RK-4rgYDoLev1yT7nG9pC7rMw2azwb7S1gT5vE6xFY4GeLY3mhvudXEyK2XSgWDAuy3o1qjRb9_wW5JHLT5sxf33oQh1_PgUH7ku1x9WjIXU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ngwK95tnQ4e7zl7FxPEYDLf_vzoJJ6z3o8q64-gvDy3SRZYULtozYclmsW384skZGoBt7OTtSvqa5gZ2woPEs5nPEqD96sjzoeZc16ZTaykgCx6CpRYGgYV8WszHaW7XNzepJBvGQknOXGy9ltPUCppZ2CaA3vXkzX1DkygNoA9768FsbuAQcMG83vumaxthdTZzNuj8-dvMxyJpnphhmKXTeh6P5Lx7QLNTj5mnW4ZXVZhrqPZ8qHBbVo7P8WLIP-6wd815M9zVChxw7h108KCIr490CjEH2hMv6F4EsmtHprJzGtlhEBcutgDOhSUQwKLJDYhRf43_3qfCKS2NFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ngwK95tnQ4e7zl7FxPEYDLf_vzoJJ6z3o8q64-gvDy3SRZYULtozYclmsW384skZGoBt7OTtSvqa5gZ2woPEs5nPEqD96sjzoeZc16ZTaykgCx6CpRYGgYV8WszHaW7XNzepJBvGQknOXGy9ltPUCppZ2CaA3vXkzX1DkygNoA9768FsbuAQcMG83vumaxthdTZzNuj8-dvMxyJpnphhmKXTeh6P5Lx7QLNTj5mnW4ZXVZhrqPZ8qHBbVo7P8WLIP-6wd815M9zVChxw7h108KCIr490CjEH2hMv6F4EsmtHprJzGtlhEBcutgDOhSUQwKLJDYhRf43_3qfCKS2NFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=pY4m6Xfa2gxUzhN4YslfoZlyU0Gs5zFlTXPmTbKA3jmi4mOsNrv_6xqSRVCzlE4C2XLioNTHRArC5X_Q7Bto_6XjdgHAavuPQilhKVPSe2d--OYWWsyPexyuCW7lyK2PosvJ_cO4GDpLtikahC7l3J9K44rJm_OdEByPJQViIvSBJ7mqHHIm7vUwBEXQPdMAzqKTaopvegzrhuVix5hV3sHw-Y1MsPpEEZewAGN44LHp7rysUmx0K9kgUKaZ0E_FYhADz_D6rj_rQjr-Ry1bp1kXBZc85fBVvVWEJChc92PqsOS5YIzOWIsS3RMgKQCKTMuDOKkGM7IoXKmBsYevCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=pY4m6Xfa2gxUzhN4YslfoZlyU0Gs5zFlTXPmTbKA3jmi4mOsNrv_6xqSRVCzlE4C2XLioNTHRArC5X_Q7Bto_6XjdgHAavuPQilhKVPSe2d--OYWWsyPexyuCW7lyK2PosvJ_cO4GDpLtikahC7l3J9K44rJm_OdEByPJQViIvSBJ7mqHHIm7vUwBEXQPdMAzqKTaopvegzrhuVix5hV3sHw-Y1MsPpEEZewAGN44LHp7rysUmx0K9kgUKaZ0E_FYhADz_D6rj_rQjr-Ry1bp1kXBZc85fBVvVWEJChc92PqsOS5YIzOWIsS3RMgKQCKTMuDOKkGM7IoXKmBsYevCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=KTKPhliQcoxJnxUtg9eGwEa-C82gHgEEXCq_A6-43gqTye0dug4wNnGUqjPR9-sE0-PUj8IaNrnq8VMcdNx9LNp2-xu5n1jyquRDeCp4r6fMnlrmg6TLVRyBJPg4jyCZYkC2bCN03BXDHh0tGdAJzeiYAZlCCVYE_wcjV9H7COlYw6-DAtauTQfIBfeGFUp7YU5zJOHg36uxgS64aINq5Ln_pRcsJzpfziuSmW_iSxH1AsHdkHLmLvTuKSTCP1qSwrTNiG7iw-bNgcDKQBbD1OAez1yPQBMCKktQGTJwqUZUfvxOHJO5IcMPdU35VKgoP3JGfOzD5QWEm3wL-rzuuC1B5FZCKmq--IJWKW0VYt_wbiWnR5fIDgqHryGuLvPLy9fs8ZC_yEkjXYeGcGrz1taqc7Pn7yqPCSCpU87UmBjwzYmahJ4kzfVITu-2SGDsKKHyj1BkXKr4TEpW7Cz8vWGLRanSuN7jFBuzvj4edb5PK7il-nu9yRW0gNIrS4Qf_cdKqiT_6ZkU_zvAzY_2A92aMtY-RhQrvaWq7GPj4WZoRjcg-dOa2D848cdAbhxQ0MklOE6_-VRTuZ7UraJ-hFodONZbpMJjlPGMMgjAkb5hB75red73n3tyPcc88FGdc9zY_jqZXFRkdf9h1N6pH54M7lMbT8pcF-JM5iLhBwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=KTKPhliQcoxJnxUtg9eGwEa-C82gHgEEXCq_A6-43gqTye0dug4wNnGUqjPR9-sE0-PUj8IaNrnq8VMcdNx9LNp2-xu5n1jyquRDeCp4r6fMnlrmg6TLVRyBJPg4jyCZYkC2bCN03BXDHh0tGdAJzeiYAZlCCVYE_wcjV9H7COlYw6-DAtauTQfIBfeGFUp7YU5zJOHg36uxgS64aINq5Ln_pRcsJzpfziuSmW_iSxH1AsHdkHLmLvTuKSTCP1qSwrTNiG7iw-bNgcDKQBbD1OAez1yPQBMCKktQGTJwqUZUfvxOHJO5IcMPdU35VKgoP3JGfOzD5QWEm3wL-rzuuC1B5FZCKmq--IJWKW0VYt_wbiWnR5fIDgqHryGuLvPLy9fs8ZC_yEkjXYeGcGrz1taqc7Pn7yqPCSCpU87UmBjwzYmahJ4kzfVITu-2SGDsKKHyj1BkXKr4TEpW7Cz8vWGLRanSuN7jFBuzvj4edb5PK7il-nu9yRW0gNIrS4Qf_cdKqiT_6ZkU_zvAzY_2A92aMtY-RhQrvaWq7GPj4WZoRjcg-dOa2D848cdAbhxQ0MklOE6_-VRTuZ7UraJ-hFodONZbpMJjlPGMMgjAkb5hB75red73n3tyPcc88FGdc9zY_jqZXFRkdf9h1N6pH54M7lMbT8pcF-JM5iLhBwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Y4GAFqWJX4VnmvQMPTC3XKvYzV9RIU9kSAJDYHJLp4Z9xg0XmVPIU0kR9AgfzGgI49jOGs9Y0vpwcc8dYoBK4NhdudIu37-7oIc-OfC4Vyk0zgWw_8_xsd60rj_-Woq3YgghH16_m3LS23lt-Ujdx-Jf8hvhXVmdJ6zln8wroHTacJfjfmQrNMMyHG5JXOE1W7R_1IJK0epNK-i_L_zxoxdinod4P33Rre85QBVaeI4_Q3CulC0uur8VewJFsYGgEn3mU_pbNIwd6srETUImjaU8q_tsBRPa_iytydaujyElId_A8C3ozEnm2jnptp_16i5Hei4Prp8sp18Aj6et1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Y4GAFqWJX4VnmvQMPTC3XKvYzV9RIU9kSAJDYHJLp4Z9xg0XmVPIU0kR9AgfzGgI49jOGs9Y0vpwcc8dYoBK4NhdudIu37-7oIc-OfC4Vyk0zgWw_8_xsd60rj_-Woq3YgghH16_m3LS23lt-Ujdx-Jf8hvhXVmdJ6zln8wroHTacJfjfmQrNMMyHG5JXOE1W7R_1IJK0epNK-i_L_zxoxdinod4P33Rre85QBVaeI4_Q3CulC0uur8VewJFsYGgEn3mU_pbNIwd6srETUImjaU8q_tsBRPa_iytydaujyElId_A8C3ozEnm2jnptp_16i5Hei4Prp8sp18Aj6et1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=vj06PTxRuvG3In0qDWjfbIxwBbbcLnDbC4OLCqT0VKnVTmC_O8Qc2G4-5nISRqvlFPnPEBebFAbot3USzeRMNkhO4slgLgHWt0dya7riEWQn7gVMQ4Uq33WWCV3wDxNWMxKHN-pvzAg_LmYfQxQ4rKDCxFuS9Qgu5kl1gXRcZLikgWKCU1AuCjI57R0dlV2tBnLsOZ80vX9mXiv_S3Bl8krcxQOmpwOqXhU6JCTftx_1sSJRupsST7rTWj5nIPRxXGUeitNZZFWhj1VUUNwJUCuHo2qTubf54OjrLQ8iOUfvOk8O8Cu0SOvNwyzwdnbISBxLnS8dqR8nMkIxmhY8OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=vj06PTxRuvG3In0qDWjfbIxwBbbcLnDbC4OLCqT0VKnVTmC_O8Qc2G4-5nISRqvlFPnPEBebFAbot3USzeRMNkhO4slgLgHWt0dya7riEWQn7gVMQ4Uq33WWCV3wDxNWMxKHN-pvzAg_LmYfQxQ4rKDCxFuS9Qgu5kl1gXRcZLikgWKCU1AuCjI57R0dlV2tBnLsOZ80vX9mXiv_S3Bl8krcxQOmpwOqXhU6JCTftx_1sSJRupsST7rTWj5nIPRxXGUeitNZZFWhj1VUUNwJUCuHo2qTubf54OjrLQ8iOUfvOk8O8Cu0SOvNwyzwdnbISBxLnS8dqR8nMkIxmhY8OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrvXcPBO1SsmJbVfsHIYYjCKAMERKCJVAKLBZMihoo3gOPCy9enT_mR5GPT6JGsX_QT-WCBveZAAVZV1evs5hGZTxb5iziHrxZzg0T7CGTLUlO1wnxqq7QnvV7n4N_69NAHLX8ZRIZE8yb37bXe6yzekDAAzbyTH49I5uvdGHArIULAxO2-KwsJFB4WKtfnUU1DJlL-oj3xW1ohPgGR0wjwEb3br3SCzHTN5KK29Mp9tZxjVaLZQApn_YRLALsyg0983-T3P3kTB7cQlIPqOIXe-TL8Chsw3j_gR7HGnR01xJuDHaARP4bnIbGAlo8Kt2wRYpAmq1WOYHrxlq3axpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTKHvQVuSjxDuv1CT1sr9rPSGCMc0swfh-gQlQBmC2fOP9taXCDTmFnDflr_cf11bgDxnibkGAbfm3y1pVGXp8-rJ54ZfsX9XOw3RlkhLIhx-Ssi9BiTxsosSAH79okwefgNIRFs6ehiEUYPhl8z7_XldpiARABLUrrKlagvVeHBoIP2in1zprAhX7bZl-XAgm7A0URUZTFumFUnSook2EvUBnnnXlNDFJqp_FE9uXvjBlcrOf0Cm70n0c2PkVvQmTH2NeD6dMX_7HJi8jHtNaxx2AFAV17JqDUtN-RGET7RqxUX8rusT-rQusWrxYh_rJnW1q2egkjKOfJmFjUNTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=bgDppbX8hLuH1-RAEyczYvamMwGZXMm4UHtZp5jbRPxh7Xc88gwaB48VaGCdLNQroNewGXIXHscB3mgE3wXmLZuafei1BWmLMgl4ZovYhn07eQke3KKmnlZnESqt22C5hfKg-HV3p3xqhOxTrIopNbPJGs5RUQTJtkYOAY63I0kInouElWZFUC8bCra2ipYYByllFpDClNg3b8IaIPTFxLxkDV_uRlJWZMfYB9rxE_ejltl1Vx__2XPEY5fecIiKhknNOrlT4gzzztNf-YmitYesqCQb62KyY6sDPZoHuXrVjsQoB9um7U2UXclTJrsCSsk4XyeAcApLafcE-dcZFFaXiQ_DRZORFMOhGA79aixXh5oRfr9-Tm78_nDXB_0oY92njLz4-ByK1YtT5UhxyeJej3w-VNENqeESvfQGjWJTOAYcV0suA1h4NXjm448s8FJ3zps9dMmKtyG_YjV-AJ11r7YkINJislfzO6H9FqgLrjnh8Ss9vnvw3vUlF63R_FHmayzwLw30zNivNm3KN2oxBdBVHisAy4OkO4BZECNUuxWjQt6NBJGI2g33Mio_f0PxeN7Uxh0NEUkWTiVPBHXiQcX8u4Uv4AjZxKYhkQVI84_BWGe1Pg0ybBPBHla_cVGY8_FQWsT3kZsYeIvaaMX_1kw3YXXibeJEejw_RJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=bgDppbX8hLuH1-RAEyczYvamMwGZXMm4UHtZp5jbRPxh7Xc88gwaB48VaGCdLNQroNewGXIXHscB3mgE3wXmLZuafei1BWmLMgl4ZovYhn07eQke3KKmnlZnESqt22C5hfKg-HV3p3xqhOxTrIopNbPJGs5RUQTJtkYOAY63I0kInouElWZFUC8bCra2ipYYByllFpDClNg3b8IaIPTFxLxkDV_uRlJWZMfYB9rxE_ejltl1Vx__2XPEY5fecIiKhknNOrlT4gzzztNf-YmitYesqCQb62KyY6sDPZoHuXrVjsQoB9um7U2UXclTJrsCSsk4XyeAcApLafcE-dcZFFaXiQ_DRZORFMOhGA79aixXh5oRfr9-Tm78_nDXB_0oY92njLz4-ByK1YtT5UhxyeJej3w-VNENqeESvfQGjWJTOAYcV0suA1h4NXjm448s8FJ3zps9dMmKtyG_YjV-AJ11r7YkINJislfzO6H9FqgLrjnh8Ss9vnvw3vUlF63R_FHmayzwLw30zNivNm3KN2oxBdBVHisAy4OkO4BZECNUuxWjQt6NBJGI2g33Mio_f0PxeN7Uxh0NEUkWTiVPBHXiQcX8u4Uv4AjZxKYhkQVI84_BWGe1Pg0ybBPBHla_cVGY8_FQWsT3kZsYeIvaaMX_1kw3YXXibeJEejw_RJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwdMDesdfJEJsLACFuUqSQLkkBWX0JsbYKmLK5BQhXuAaUdxsJRlC7CnH2fXmXV_ACFV8u_QcJEWSxOvanr5GtokVFP6d3ULCqXRi46rjcewz8sn_QF-a_rw0zRh3WAmFlYjrIRQHPrWqeR4IqRQQ78InM_J4xrspwC-EFTSj659iRPsFXyYx1ZmxrswRmHCeTG7yTj6RDiMZcw7n41iSuJvUj9j1u_csNsD3ui9vWWjpewoNmah_eKlgrKpwcAbpGIiLQ2g9VcFLuQcMeOgoSs-VvLIxeOUFLWsiVOphbKGAqtY47N0HRP0QEa53iYl4E2JmLMKuq0kZ89JXT955Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNY8lnNJUHtSB6aYQbzIG3B1x-LWQdE_nV5MUpsdSYdMrup0IQPIJuiog_qpziwIv30q1tiFYEzCJbuQvbMj5f5m5d2UTdQ4sCBmbIxx3TpSvslbNtB6elpRJ9kSZlAi9o5pVeW44Ov3KdbJzth3HGHOX1H1_CLPjUYEM7QJf6iAQ_YbzTqZsgyKL0L_8elG6cUT-HxEaYPFe7cCVI3QJeQ0NtTlV5aqr4JfwokRsk6W3G7RpWKw0Ej28Xfip0xYlKyaV-eZJCMI3EE9pEw2Mo9TyP10zj5zf-BG8rWYacsoaYX-s5XU83Jz9Lsyrwz0ywEg0Inufe6OlYYgRoHXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
