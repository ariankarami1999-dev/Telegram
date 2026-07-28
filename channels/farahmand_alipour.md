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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWyg1VhTgWmTIzlpZgFOXFJHBEdd6VjHQ603nKY_f5JhX6Vrt34C_kFgvZbTAuVF8xBhpE6gC1karqH1jTpZfkTrmV1XQfEMleLJufVQtB8G5H0DRQ916rUPSorYvGhf5klhOPgQy1MrBlmz6CtoD5cgWfNQLP0z17ARg3gwWESc4r-0dqNp4p9dy1sy5Qf__jxWJNB_GHv76-l3367-bHth2Y2dvWvCjCZhfZgLOKjiHRuh5Gv23guLWpzbg5BrFDaMJncsW-qLh7f8MxpcOaVB59-qVI8m0Jcchvp0Ro5jC0ns_yjnIAdC4UE4RTBxDjUOzm6mORG6cc56u4yL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgvBgUHGpvK9Rf11Q_NuvtBzRr_H532gywy207qbMLqu6mJbhmnBXLU3xr_sz4ysa4jLqgdmtFSY8Ia1KzVHRWOKa6yzjwpsB5AkDBgqTcJd3w_R79DK26nhP6qaut4-6ndebXTF-v4kSMSo9VbkdwQEAlSU1j2hsiIdMqYBwlY9FAA4eiKwS5dcH7vaCCoUq1nm1FBfSgMOWt1yTC7RjLAhH6IZiXa_VsLPx5ZD954un1_ZQx2VLxSac1olL1kTYqJclRqYdLIQw9MbTjAxdckQ4l6hNz65NtBpKzdSdaGANiGJ_m1UghB_3kHS8NA999cRuOLq3R-J1blAobhPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzBzM7s4c6mn7vCSuTFM4qEOxVoyYcza69o0OyJxbi1Jy34qMYKKxZS8PvLZl9kSisey-Z8b2oZ7B4oaOeR2Gmgm42tZnc1T-NHjqjm--FKdoX2tT29XEzSTt6v52-pa1u1B9m0D6TrCltJGZa8NxhU_-4O3jHXJO64Hi3pSB1j5D9I6Mfc7H7676JW7BzKQDmxjflw7BM8mbwXwduQXeq4p9SJ-kb5AWuSZ7YAT8mqz_gOF2VsNAjiPJ7Itm_p9EpeqtRHU9b-BZjNFWpz_FYul3EoBCfEpVAmBvkIY7o_uMMvfnVyYXr-Ixa1qEz6JhsC1ssJ-bmU7qcW6LNegyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjLjq0GMnsA5L40w-oksXt8hOaY3ckwoDW6X4Bqn5oXCkjTeS9yjxX11gEc8PrHCSBTAJf1wo2He7khowI1VxAO5HhFy9hxBjnJGUgGS6ORtsjVLod4fbi2qgr0KuFKbWoyMIAvaeMTho-AGs0guZNtUaYnyL3HDyCBfctwSOvhTT9ZR9P3XmjnoxikSwTer3_wjMvtIlpC50ZdrcOtI0b7kN_ObEpsijFQegRBusCiCDokoxO2fM3SmppuTSbS1NZSfw19-31Ec0cbI9RWJKOHGVVIZZrPqH3GB_Oce11_H1SYoXuyc-Ru8mo6kcFDkoPGm6PnTlzh2xTz6N17xwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mzzda3gLwp3j5DYpCN13FkacrLGw0HVcbDAyNToydQ_RXOoTIqfJGAXTANxWEVyMyEjj8EIJKlkqTBvqYl1kMy8std8K852fa_CZlspp93zOC4ItCRMRYXlaPuOsmaRvVSke14H-xLrZhjvY-_x_-pJCyz628jKZCDYwq4E3zI2b8X-bAVjOzXxp9svsWM1f8KnqmwaNtyi-2ekhBZSo_YF-anWbdQVR8KASKxC20hwnv7GMaVWRenVugjJiaT8Ubs0m4J3RH1u12PRvZQLpgrGc68EE4uNOw_QI47hMn5SHGkfWlVUVK6K6d5WhrTUaw4PB5Ad64SJatOZ9zncCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBe8ROW7Mo31X96BUWw-xpo55qIGNQkDtaP1C4ouOfa8rPbPRDOGYmyZ-yecfmIKrCNDuSbZFk5k86cnV7MEStqhCeFeaAYqPb2egubXMAMyS77ztQmoizzv-AckakTVwuoL5vLB-pYd1ScHrRWX9PLDgZ0kR2V_C0KKZE950sXWn6f8mggYv1Wv5OY2W49ZGBCchy57WyQ1fn87sB0TKfiZ55pza9PW8C4YkXscjYezBUVGzL27yPn6XadVMoosG22gQUhhGkieGLoJSdWI26OhMW7e7INpU5kgh12vsfH1snPn8xOs9OA1VpBjZAg38d6hcaeK-xrPdzY_Jh3NRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf1vioj1W8leHW4Fp7zU1FdkFbuJO9BvuDcSRMvSVktYVysJysp8dHCkmfAn7ItM0KoD1saVNBL22Sjt9Jwwrfa5OPU3_JagLEW7oM5bSi-jtUez9ICbfRh7c6OTixAWylMk9oFIxLeXpYq6Pgm1z9iVveORnwELhEsJ-HRpmiA_LIwUf5ERxu99qiEs8a8652m1NKXSaG37jEOZdS6Er8fYaHBNNNW2GsGZN0YJ9CZSey1-OYZuNM16VnFE55vdPyo0jXak0kcRqmBwnSkYBVQslHafIK0dY9eURAK8Na1GQLzSlgzyzuRnkRd4oU0JsZpQeHcMvNxvY7A4IYgSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5ENxRLn8v8GizkW9LAGZH2tlYrGpVk3bhvAaJQDYxgfvyO7Zz1zv2uD8vHofQoKYbDsIaIywyBXm_WkEsIb16m69GzDrZZkAepf7Uz8oByYHEdxORpvCQfWM1zw0QItm6LGJVDXlUH8oL4GUKc6ua6TLP1ek4OJMXCZi_aqy_tkYLIcIec0QaG3gtGei05n0eO5HbzgcIPNOkEs1pcc9K1alrsaBrlDOdwk9f11R2KHQVBJAbG-M50MZzKLnKhNYNGRz4hPXa5DV0sYCEljLqQyO5QCHWbL00pa_Jb66kFV2UfJjxgKiOwWI9y9DgMvO-WccuvcIMDu_Gk3sd1ekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N139iy5nC0flp2WXQnrmPTXFzVRxf6UHMIYVn8tQmHDXRZgLj_OcoewP6vZmZWonf02CmDryvGryOuYxuDwCo7-DdFl5Au8RXZ3gYQSBzZjwAB9mAazGnzKhLdyATLmiWUT3Vieuq3BlvJmI4cfduCiddNWFUk4gjFOF7q09e6CYRelaqrNpJ-a-LpvDSlnnuoLocUTbvuZIWs6b7XqaAQ_GYqw5KYIbHZY7cJJ3rFEOIyDAMEqAr71qkBGDvbEJ4m9LxLy5l_K39Q0aIWpUtXYtxo32zpHi0UBNHBDlPW81kxnuiReTmLyY9ZapUm2HehPJr1nR0fLWQLgc5TR9ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJArJwSEoDtGVw-vvKPznrdTsRHqRXc9NRWYwzn8vPyiV78v-XumftCn-IZ5UB2yMzCDZeExRojMzTarNaSjtOUMgwC-rOXKqYaspbN3lmMfE8jtnKYWjgVN12Kn_UrYy5zGKrAq84dVTKWKh9LBTnGXbJrmiqtKHsOLMj5s0XE-mcX57MezCkjjPivce4LIZuFTH-Jb0r4z-FbDCWXUQGRtMoeCmrdGdEhB7f0zkOf14WjjZNLEbGjqvrlse5DuS5b8WHgsAVnLKE9KrYBFULIYvNutyFch9sOnRQDGvIS2BIgf2ThahNRA5Z3H5ZvehO-_D_25we41r8dZu4dfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clrJlNJdBwqb1VjxMfY17dpuFIeJoAJD2OHfc6zVEQhdLNGb9m_FRLDjXx9G7Jf9QmcilzJO7m-ybyzeZObU7bV9Q8s5QG0Z9kv5kwqJmkV5HJIxQeIfAybXKutOkr-HlC6_YvsZL0e7xbzD6FQq3pNZbMSymnvAAUB4fHfjL-E6dHFlQlCHWoFFGPZgeyCtGnrDXTGumMZykk_kgaSTRnIL0Ysfce4JSHi3FLI9kQG02d8jHsnzEDyQnSn-6rsgErNUo6tXZ1tVj_YqYoLywnbYdA_QtUwsCUGxCFBny2JntiMnKylzdk7ODxd3_3FO5j6sgC8eJBV80nR8iPorrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vV_IbIVe7-gaBIrkMSzrFw3Pc2QJddxgp24bB8SaXZloSbXmKAx3cArWbADWVZWjSpnTg3qx9tTuvyrkuwEMPseLQQq6HznyFdat9oU_6VSS-hcSF6Go5rU-sbL42siBAKYnkuN_4hSmJr-9u1wscotO1Jt82L12IVgIJ2hP6M1fDKunc3fOfj_8drkF16uqHiF3KHtbvQ1DUeRI3iP2r53vTbMKRgqWKAAk1Q6Yd_WilR8t_uBSWCMMM8pbuS5lVEgOVaOU0XwM_5TZmVG87ompIZsAjpeC1nR9mi_Au-goh-CxHkDHNWRQVTA9mwI97cgyn0xA65g093GJ05_fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy7ylRAY3IwOPQZYA9nZ284rOplnCWvJfReK8xG7XnnIj9_wciMn7_bxGE72pf3TdAJgXqHHS7GimzGGB_z-Jd8Z4m8wm7eljRXCqsFF5VuWhHCJFGh-Byapv4rpzrxgZPGv9nc65EPoigvHkwiQGTNzXlciiOdJMpdJ4cppwtQWEd9USL_2iP-J-_wmD9LvlLQOli9zfQXht3vWjdIK-njNkZheebMg0Eo9czpIseuR6joOOUCSQzVvGK5-xt7T4m5KJeQpxzyshxCmh9a1SCLx0ebsl6j8y17aZFTt2wrleoCxYy45c-FOuW5JGJBSKwJZxABnLDwX-Ts652LO8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKYK5c7if6orSD3KRoLgQq_hdtkFCAc4j_coi1d0AYfIbYJpMflVqWsGGcDoy2AA0pc7jZXDA-Fj_6Nzkb7qCf6ZVtP9kGg0VGBvk-CHTkzmYh_wk1hNwOIuNemWW0aO9rpNxW60NtKOS6zX6fnIyFy_oztDIUr0POU56A9BHfk6S930cNmAbBeWAwMY8APJGQy596q3_WGTOW5Tb60cPN4Fff5EvAaBUz_viu_X2Jg4FcEqhMSYXgz4xPlC1ZUQLy-NfELqDvzRXxKuqn0H3QGfhhu8GLjJdkXgG0ePXz0YEKY1CkASdVBHSnhTpGMYzKsq5zAgBFTZbZLtkPzyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-REBatygYj5SXdFQEXhn66CrDKe2ZeN1Tdo7k_accvMF4cJj9jRbGiIlYiNooOIYFyqjWu8TzldtfBUgnkW6WU1ZnakPY8piFEK00z4zSOMTxduxxSRn_-v1X9voKV50CMTykIW1_PAC6KGxN0XsSNXAA2YfnjYxvfEEwzISGqqrPiq_YSl2dmMgRIdf07NekzCrasuGy2y-yLVy_RalcJ_LtIm9D7Yyvxs0WO6_u6XfnTZofk8yZWUREkojsotKVJA8iuwcgVv0i8Lh-50u91z0f26m2NYvXTh6fYFjHLggmYGYOpbmg32lZpCZTIcc_T2EYfif-KQDVF1cvpDTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3RVbUWH_bUtF0xQEraFdF8jO10bZLuwrxCmsL3arGU-uHsi6s4UDchNvzZn_h2rmvmcfxs_-Ms3uA3TOK6AeeXn1U8ubH0gGW8pLfEMtpAVEieGJLh-fhMMZ_sDLEVOO1KWMuz5rjGnvyZSWlBHgVqDw5LJ8v1-QfzEnWqfkGfNi4bVz0zeA5kEMe7F7ZVI88b6_G4Je1gr6N7YmcBXNP6aD0kOA8FcUTIINNPnuJx625U8e0qiMqn9VPeySN0TDLAkfIiMkW0gjaI-1c7Yy7lJe2q3FiV-4JlZeg7GNJVHxkLLyM9xyIw5586dC1fAvzDyQheqioyZgbo8YkU0cA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=FodxwU7UldiN0W_Fho_LiyhEnLB0iKTH0JrJkFgmja1fXLYcrK2cmgaRLgZqTXi7d5C5N95vGkaEuAxMj5iYYw7NnpOlppb4i3FmlZMOvz2WJ7D6WGnVC0vIgGF1UFjQNP9Ta9BIvGZf5VK3_c9oDOZwI9rItX75Y3TGC1hueVjvNkgFgHJXZr23MVJFvR79RzNw8zzwrrOLM-bGhnIWcRHf3LwS-KAqQcRgEXFZDp-I_9cHET8QdER_CPG7blYf8LQgXdzcWtGWwNJVMShJEcydA6ukJY1fESb7s4KIIeyaDTAJcPQI51rWSPh1-rQSV1xJnv-6sOZNA9n3aHHqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=FodxwU7UldiN0W_Fho_LiyhEnLB0iKTH0JrJkFgmja1fXLYcrK2cmgaRLgZqTXi7d5C5N95vGkaEuAxMj5iYYw7NnpOlppb4i3FmlZMOvz2WJ7D6WGnVC0vIgGF1UFjQNP9Ta9BIvGZf5VK3_c9oDOZwI9rItX75Y3TGC1hueVjvNkgFgHJXZr23MVJFvR79RzNw8zzwrrOLM-bGhnIWcRHf3LwS-KAqQcRgEXFZDp-I_9cHET8QdER_CPG7blYf8LQgXdzcWtGWwNJVMShJEcydA6ukJY1fESb7s4KIIeyaDTAJcPQI51rWSPh1-rQSV1xJnv-6sOZNA9n3aHHqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm64NvJlF_5Q4zQypJSjmpUgsGNGIKcEmEDF177uXXIqg-rOzCqJw6_M4j5qqrKGB0FqWjz3PYpp_11EDMNb0xd1KUdyB_tYSWIJK8Fk4A0VIXm42NFsXCAcw-L08ZVUGKaoVyQJ6lmne7nCzZ5TwivRsZ3cFD-uyjsQmAFGWsgC2lMgplTW8a-ysD5zNPSP3OAQkc8eTgooFDL82dPMnZ0jOX9sEJZrGAsAooNbzFazDISlKoo7e3kJJCTvPNesGtJ4H4UCdnhSoKL_KMcRbPAG7EztafPSV-WOzDUoOTZ4l56a3hxfGmbhS8c15X7mH3G3FmHJoG8Lhyd1oBGUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smQhQ_O3NEg3TgYCC47A5afu0RZEy8vIddBIlmPot5hT6jGDl8OIFhuh0MYCPLi4qdHyeZxTZPHvxETFlGwex3bUABJwaoUGtwsO6ILVbDfOxtb9VJrUUxapGWOR-5S0V9mxfsWn3PaBLVZk6jk4dtBn5TYTZlSvNA5bhbPm351eL-W9_tTcMHIGp8nckqh5dHZyfL0cTJ_8s5aLhUUsENWXOBVi-TCjKNiIFgBxxiSiPz89RAcrWoUnHxW2axYID2nK1DhDXD0ulXD0SAqpl_CAbvrQN25chDpMRZ9MQFHhr0SCQsV5qbDeU6siBftmaTb3b15OU-yO40B2ASPNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RubAu4WGvL63klW6GcQ7etvVnt-Y_-HErh86BMoyM9_D16jH4W4OYltYval7OfdOwhBnS42VWw65YV5W8rg-pZOBTjYttNyR7-UT2zuXTX39HijU3CqvDcruEyD5pobkT06aYivPEgP7uKGK_nZ7UzaFZwsQpYxzjLZiovAQLZEuNKBDbt7iNiPtfCjMc8HhDC6DKJoj9nm8V1qE2hIBM8aJ3bzV6g-5zmcmRlydRXesgqNutnJupdEBKc5cuolETSn4jnXJhdnBt4Pa6vk-sl3nIWT4Lj-A907bTzcUMU4OHCNKp8-HYmHjT0lpKaO_W---pBUZvqrmxlK8JwGTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=WUQJpuUFo0PGcqb3diePH_4acJNusRJABx7VGeFS295jLJ9b_7AtnBgaVjUeqLpWqq9f0uuUSJYZxN0a4FEoOc_qTc6AQbM0mokoSVxBoDsEfye4ZBVeocH1ar_og5wwPEH40JWdPsOAJiRbTcySeo-o3m4yTt_VQFeLOjut_vmERh_pnSFwAhWXwBjbgU__DWIpSKJmBu-XCwKWS3KXuv0lU5BKrZ7sMPYX3z0w5phlSxTi4yZVLpYuIzOaIWXwXWc-krjLWVMLtDh05yaIi90nivsi0WLtTt20e7nqbQEEgRSfWzBU-xZaCDsKMOJ3cpakoVsg-rQXXcy3K61T-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=WUQJpuUFo0PGcqb3diePH_4acJNusRJABx7VGeFS295jLJ9b_7AtnBgaVjUeqLpWqq9f0uuUSJYZxN0a4FEoOc_qTc6AQbM0mokoSVxBoDsEfye4ZBVeocH1ar_og5wwPEH40JWdPsOAJiRbTcySeo-o3m4yTt_VQFeLOjut_vmERh_pnSFwAhWXwBjbgU__DWIpSKJmBu-XCwKWS3KXuv0lU5BKrZ7sMPYX3z0w5phlSxTi4yZVLpYuIzOaIWXwXWc-krjLWVMLtDh05yaIi90nivsi0WLtTt20e7nqbQEEgRSfWzBU-xZaCDsKMOJ3cpakoVsg-rQXXcy3K61T-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0BstJlE0JU2_sDVpwzIAdcnVzJ_KzdGb9MGeu-YW5c2tErf9GlrJvpg57BQfzlDf9O6SzKs1e8jAkkG_6TAvb5oOqkYmGCVQZSqjA1P_Aa-SWHVPgOs_iKc5Pa9Mb0x7WALK4vWKXUQaWvBpMTPw9JDwkx5y5Epon8tUCfIQqd53PtS9pyg64Fx9ijJOuufHbNrMA0Pkdv90U2a-oo5kpPIvNyt1D1-zsAtomYUkZk6JbRYppvNp6xwsgCst588EVgcXHGPYOpzMC4KqnhDE2yggFW1AEH7BGD3LR7foJ4HXSfYSL0EQbgqfRaHTgL3mrQ7nm15ZAV4wnybwb45FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=M-WHSd9TJz0TUzx0D8GhNbRNEKSuvq5zC6c7AyMuV0WwPeozmpuZuiowsFGM6LPs0qaajL42BircykrG-N5pW1OxuvSNa_5FR1R6wHw1YXyBzl694C6r32qe_shP1AJptuRNNBR2tHtxhxntkzjDGTcqnswlSDR6r74Bj-lH9-9DnYSMCF-PIOisDKdkbJM68ur1yzUDBn1BeSAOoUDlSv83uHcErWEisY3l8tqiMwxvuMShROL5AEFa_gQXGODIMPzgpLJSxf0g02GcNEgAbYLXRxEIZkfL132c-2mUo3MRVqgNpSVl_Y9h7vFnsJv7qyHvSUmh75hLvl5zbIp7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=M-WHSd9TJz0TUzx0D8GhNbRNEKSuvq5zC6c7AyMuV0WwPeozmpuZuiowsFGM6LPs0qaajL42BircykrG-N5pW1OxuvSNa_5FR1R6wHw1YXyBzl694C6r32qe_shP1AJptuRNNBR2tHtxhxntkzjDGTcqnswlSDR6r74Bj-lH9-9DnYSMCF-PIOisDKdkbJM68ur1yzUDBn1BeSAOoUDlSv83uHcErWEisY3l8tqiMwxvuMShROL5AEFa_gQXGODIMPzgpLJSxf0g02GcNEgAbYLXRxEIZkfL132c-2mUo3MRVqgNpSVl_Y9h7vFnsJv7qyHvSUmh75hLvl5zbIp7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR7DKwb5oJ4YkBbdnjNRdObaH8W8EgfiJbOByHFwAW3sjIlm0XXdIeT8e5pKHR06ke-n8IxHqjIdXgotmBaXN6rIhODE8aqTq_1o7yjcPArxSUR6mMhfGR2PCVNYDUV4WKOF2oPD07ILEtOvd9mD6-7x7ishNHLRET_8JRIuBZSvMvyWbMRnOWjSlErE3jBfQwwTmhr1hb-zdTsmmrwOF6ggRRipCqpmDOV5vDED3uGIPNcMWFdIUuyrRtoOvW5Ix1pIvhUl6H3V0hOCujzKDdAXCxoWVJ4EVCye2wHpoHfsc0KWmaeZoSjU9_gyilNBmB3C3r_frQGoXd5YNp7IpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stQsxdXZ5a3FOZtySkGIE8Jj3mkFNnsuBnARUtbFX7-2cSaFQhcZ1W6-yFygOaanwAwJuvHOX6Xamd5ApGg0OOePyxNmENN0k9_SRCtFXL5fGysGaJsVMfU8_BlUa_bpyG9_MXozifyxp62zEHiUyiIoE_nYN5uD4pYTQ0rIWE7TGGECU730EaFpM8a5sd-J5UI8vTOjQgoVggUlVnmEl0mvZYuAXQsTuZIP56Bk9RJ4oKEQ2US649VL-U4EJ0SbM6rEgAnIS8tzxPjYLS-sPJv2RLZkPL9_cTuHViyRQKoawZB0KVe1ujoCBu7fTanP0HuWbaXGC_gR3SS5jiAOnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=jX2m2rTb7DSuGt5cGFpa6DBCzARzEwzzsHRXPNjv5LauprjzWBJf2opQ_eGP9PFwonp90Lvqh10KvBM4FLdfeOfy-I7SDmbVwiqsmwsTDysix0GOOlopLPs0SXD5wqhEkxOdSinTKN7toiwboZkW7d7cDE2ZldJNmab3xRZefGRw532kMNGKZ4tIFAE9KzcX6m2OxrbN0u9EUXrTrgYIsIL8195EiDnK5gm-mqpL0IUutvNLtjBWf030Gqdi5yYdREGq7arw9guZS-X4koH7NDdQeUFyYV605WCaurpDLnyaWSVHX-4Xck6X9BEdozPmzanvgHw2GW3pdIXrF7BWgoOQAHDcPfZKniLq6VVfEPXXmYJTTed2_IBwczCYM34ZDw29dablYNEMP9UP7xmbgk5raD6alMlhP17hlXOCyyIui5Xj85BUho04nLDOkPQTCAJJmGewJNfLZzkuMThcMQ6riFWPKiBnem-Cc1WZ65wwkB8mggZSnIrqpFWnJzc7F_sKb-kbSwN2tHRpLpMVFQhtx_2A3q3YlWNNaLtv6kj75j9CDJiDGbF6FSnlUfkWwZhZkhtfp1SjsyXW1fmyAj9rt7V5jsKtnXW0SnB99I2lCATIXrWbUFr5db4REydloEf1ofA3ptM1ZWW4H0of9qM-Pj3aQlK9ewZ6IYmB27c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=jX2m2rTb7DSuGt5cGFpa6DBCzARzEwzzsHRXPNjv5LauprjzWBJf2opQ_eGP9PFwonp90Lvqh10KvBM4FLdfeOfy-I7SDmbVwiqsmwsTDysix0GOOlopLPs0SXD5wqhEkxOdSinTKN7toiwboZkW7d7cDE2ZldJNmab3xRZefGRw532kMNGKZ4tIFAE9KzcX6m2OxrbN0u9EUXrTrgYIsIL8195EiDnK5gm-mqpL0IUutvNLtjBWf030Gqdi5yYdREGq7arw9guZS-X4koH7NDdQeUFyYV605WCaurpDLnyaWSVHX-4Xck6X9BEdozPmzanvgHw2GW3pdIXrF7BWgoOQAHDcPfZKniLq6VVfEPXXmYJTTed2_IBwczCYM34ZDw29dablYNEMP9UP7xmbgk5raD6alMlhP17hlXOCyyIui5Xj85BUho04nLDOkPQTCAJJmGewJNfLZzkuMThcMQ6riFWPKiBnem-Cc1WZ65wwkB8mggZSnIrqpFWnJzc7F_sKb-kbSwN2tHRpLpMVFQhtx_2A3q3YlWNNaLtv6kj75j9CDJiDGbF6FSnlUfkWwZhZkhtfp1SjsyXW1fmyAj9rt7V5jsKtnXW0SnB99I2lCATIXrWbUFr5db4REydloEf1ofA3ptM1ZWW4H0of9qM-Pj3aQlK9ewZ6IYmB27c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bHNkVMtmgjnAVVuGL8cfVGbbKgLDpg7swuQ4WFhMX1Uh83KOJjVH6wVU0EVSXZq6VosdJ4Za6p9ExuXIbnXfja1qv--nDu9zcoL7M5RGbZXXFv48dMJpNlRafdYSkbDK0j8ae77VWgx5Aingx-BAIfjMULEWaEjggIqtDkbYy7-wF2DApDgJ2pD_Dq71j079yGUDUFzGk2bq75RuXeG1vg1WudhgsBG0jeRsxQKY6z5-M_0P8Bd7l1biwpwXctmdr3hUVNpeXOWTqEMQIGXvIFid790VRlDydMDzEO_q-jCmqru23yAc6Iu2IptDEAia66RcRgibjpA_csUsXZtCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bHNkVMtmgjnAVVuGL8cfVGbbKgLDpg7swuQ4WFhMX1Uh83KOJjVH6wVU0EVSXZq6VosdJ4Za6p9ExuXIbnXfja1qv--nDu9zcoL7M5RGbZXXFv48dMJpNlRafdYSkbDK0j8ae77VWgx5Aingx-BAIfjMULEWaEjggIqtDkbYy7-wF2DApDgJ2pD_Dq71j079yGUDUFzGk2bq75RuXeG1vg1WudhgsBG0jeRsxQKY6z5-M_0P8Bd7l1biwpwXctmdr3hUVNpeXOWTqEMQIGXvIFid790VRlDydMDzEO_q-jCmqru23yAc6Iu2IptDEAia66RcRgibjpA_csUsXZtCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPEOExwB_sVPBzzpXb-5eWWZjBMgzmT4omQMnRp8nXbklLofu1fQb9Fh37ICxj5M5RuY-cBakmJ8kaj4oQbI3sIYMZCQT21KFf9VbdrTwgYXZb42N3vq-UCGMqeAmQwx6LYxHF0X-f6lMCOuk33_hRu1vKW-03OUJ296r4lK1KCXxcJaLqHMu6p4_dVLQT3l3PcHNs3A7Q1GVj_vVu9cISJbryYfSXP5rgvb5H3boOb-eeyzxOSH1nj9JsJtkfcE5NjNjZ8R-6zBnNwWE7FArXO7vF4tu_D_JBqopfiFP_Kj6KNHVycJuUyQyGZB7CmQQ7lXiYYj8RYmF48KfqKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=RsV3yLFHPeOOIjpBqDtK0w3TiEpKMdoTbTN086iTf-kRpDIbIyH_vMdw8pJ9IuM4uFkmRpCmYx6J7TjnpEGJ9-o2N1KQVQi7ZHr16oydDw4I6GbhxHuHUmpkE6BLVWpD8iTyR5f03Ypv2zBwlXL2bXfIuC-4qRrRgGRjYohvqy7XWvDp2U9mlzFQVSb9l4XSIWz6SXyDv-Z4sEqBYhHHAQBshBqeMRQe-vujizkkkU8CbZAH80NMX3INSqfaB-bI9npuH4-e2g8VEQhXqkJ7fGjJU-yw0ov4GGuBXTQuuVLocXsq5EIxoZJMbsocUqLkRUTpZQYnVgkx_yJfDKjavTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=RsV3yLFHPeOOIjpBqDtK0w3TiEpKMdoTbTN086iTf-kRpDIbIyH_vMdw8pJ9IuM4uFkmRpCmYx6J7TjnpEGJ9-o2N1KQVQi7ZHr16oydDw4I6GbhxHuHUmpkE6BLVWpD8iTyR5f03Ypv2zBwlXL2bXfIuC-4qRrRgGRjYohvqy7XWvDp2U9mlzFQVSb9l4XSIWz6SXyDv-Z4sEqBYhHHAQBshBqeMRQe-vujizkkkU8CbZAH80NMX3INSqfaB-bI9npuH4-e2g8VEQhXqkJ7fGjJU-yw0ov4GGuBXTQuuVLocXsq5EIxoZJMbsocUqLkRUTpZQYnVgkx_yJfDKjavTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kahO1D1ZURnUlS645QkCDvYFZDHfnilWMW7xVVMw6qjIgWWx5A95PJyL_sic7p8Eyk_WM3GP-QlWdemoSv4p_GDVK9zeFM91I92nnsZNb2YBL9ytlTOQ-kfQrorJWcCo8qShYhT1NNTHWK-DnBrUqnuvWcKtlR2eER1FqQgGW17UPSOaIqXKSEpLd5z-V8jzmhn43PJxikHmdus25VKR5n5DromtGCPq-gohBf6niAdrKoyIAlI7PT4CUKI43aOesKyqqDO8NXyAvwKp1HclIO2mB24lk_AwAyDCo4Z74B-e6lwSrikh7oZCGQxMaOwXVwrHlYLfKKfb83va88Xgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_sJn7z9rZfDaHKB44cyLxindcs-jUNyaH79KovQwZLxeDIalFfq0NrnWBPA8GVPU-rFpv7LUaTD0lXe05rOQECjfEXyM79guj9vL0iyFKHpODXyQ6WpFOVKt04YryHCsGAvArMqcbclzYnj2eywwG9JWRt8tz9VQAn7Ai6kxJ3W8M-g-tA08h01IMUpQwOceGFj6NTu5K0szoWVW47NBj1WRlIzSVTqJ53fL1vHF059r_T-81SdRIZvCX7NrBF6YOdfChWkFu2wy82j73aFUfrMUmU6ICxcq7oe3pK0nxXbvCtlvRcdgZrpzHwoLdLxkgG5LNqvtw41i05eopoJiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBosCurQmzpr7wG80YWUhMWH_d1uNwQXkCAEuyQJk8YQU9OZAZj5ngRdONeBGPyZMR4cQgdCIkuUarB_7ApPUvV-X-G_I9qT8Sbb7ZDBXfI_yvnNdvm_sFiNUYBbIwiFW33cgtTxrr1DzMp8OID9iyJiCbNIa2ngov3GpRBSBT8yTZ_w1EtDwORy_5kUs6RovUFp_MI9dBWXmVbzRLcXl7TsRk4Cun2vgLMh93vDEkyAcp4A186b0Df8bXPRpz28UPLTwfD5-KCZkTE0DAB0a8G_-aIFz1B5loyxs0V4zBkgC2HH35ibkTRvvLhmlR8_4E0J_qJPoHzC5DG0TcDv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihum9FlcFyQ9hCJzxR9HEUOwRMwOIcKt2zB1jWbplx2BZxU3WTWl2ycRCLLFjmrWZC4BZqCYd97SLc1jEfePsmMvVBxDtkxlwFj2hKU2ajx2O3bFpeUzOZv8P1YY6Mv8ddStuqcSw6TW21iSEpXGP34XhT8BBeaYvUZILBerdSwxMTRlgM1V7-FitUUkqeTylievQmrXDEX1ikuICwNwTjLAhZVhkiE5YdXNIuczlOOE9JHyahafN97nEYOcGj2sXzJyaTnsoW9gJVTV4DgG95IRRsc95afWnk7sZcRMz1k9djIs5m9aCEwD-WtAlB9dESPC0OOiNG95Drp6qcUVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzBdQffaSnRmlV9mbZLisOhCfdo4eudht64YCX_Hun7Cj1dkwTYnPNyVyZQ6ag1CrMqfcyLaI-vIfG-PzscYFDl4OOw8CJe_rz_ZPR90tbK5QRZPoX3H5JJ4eChqIuqt27nv-p3Q4mlt6epSQbOdDNug-qzGsl50bmvu0lwiIBiV7y4N7Q13E3e42BjTpLKiexmrdlUYNFLmfc5vRq_S5dKn36Ue_GjuHFZ4mXFuX0hWC_oZ3wQZYeCj3XEuQy0AyvNpQSt5PDKsffptcm8TlyUDexX65bnaT4Xa7oAtfnbbFRvSJoq4n8IoMH84xuBWxd22BFSWW7UBXq2bOk7FgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=tZYDHIz--y90eNXmy8WdS0WpTCyA64nacyhR4I1atPhQbW_4s_AlsZXRIuG0KiYXy_pldCxPYxURJNMKyZ6Oxyah1w1pgLgjiAq3Yw_jKbKp27h6DRYSIAxESe81BhU0n5e5BlASOQxkZcqWvUONqjJwoTbW9Ve9X4iNpft6zKfYiyJry5UEDjTCXbNVkBwUEKVDW_O5am9rVnHXSutUvfPherbvRL9yNryDNauqDhdw8yq-rK4YlXtsaE96pjpagtSDrOy4ye2A3BQLIN8u7OZJVqUvyQmLdprgo806iajlXFyqY_Gr4DSeQNeDNN60X0yTp9R99MYk34zUdOKXtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=tZYDHIz--y90eNXmy8WdS0WpTCyA64nacyhR4I1atPhQbW_4s_AlsZXRIuG0KiYXy_pldCxPYxURJNMKyZ6Oxyah1w1pgLgjiAq3Yw_jKbKp27h6DRYSIAxESe81BhU0n5e5BlASOQxkZcqWvUONqjJwoTbW9Ve9X4iNpft6zKfYiyJry5UEDjTCXbNVkBwUEKVDW_O5am9rVnHXSutUvfPherbvRL9yNryDNauqDhdw8yq-rK4YlXtsaE96pjpagtSDrOy4ye2A3BQLIN8u7OZJVqUvyQmLdprgo806iajlXFyqY_Gr4DSeQNeDNN60X0yTp9R99MYk34zUdOKXtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9MM349YvgB7cyhjJd78X06Wahc-p1mnldC9K1BN2Dnzz1qMe4lr4JcWb0yqOlpTSNVy3IgfwbX7FYB94bgJ-c61H3651D6rSIrIHw1ma-NaVXCk8h82zySc3tKlKzw2h-PV3Rq_B-ctiaAbJ5fISuEX5VH1iIXUirD8ckIiGKa8dromSgtzG8fBoLE-3xjWQdRfXv2vScA2G2QJhXiA6pu7jIWUa_Zsz4OMCnJXI_VMabVBKG2nXrqs008ARVzvAnsvTmGhsrUACN4acuZH7MNr9WfEiaqQLT1N6W-1h1CdNKTciNnKFL6koeDt_4sIseTwSX6eWKfXAfFv8SHFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fs92vnt8psE18uw0wjFxX7wNtK00Hsfejm7d25w2aUlXoI0dbf4aGBYgghKuSqKna3oV5-yb8Z7SoRUy8o3SW3EihxzhudZ7p1Cl5Z-CAkkcQ8-lYtyDvNbtChbdjjaqApG3d10Q3ZscbEC_kLBQQoHTQ1ex9OcjdzoVzB1C8jA8Myyz0naVKVOStDBpKpPTLOsbRdZC1W6QbZ-ZZ0VXTGW-0r9SnWN6hz0phjk4k4Zly4ZQKFIyuE1Kt2DHNXOxV1j-vZgzNmQ1W7fykWfdGgXJWsszXvJKn8pMsuclGEzCckbLl2iBdMXPAAH_WJ9ave9-WYm9ogC_HipSUQgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vKKKotc0ZP-DeFC97wu8PZMAoyNVAZXr0aqzURL6tWX6A-_hKRnr5rlFZKt4es3OcBz0OpBv2qic55rvdeWKjQ3UWVBPF5e8--rcq1h7q2Mf-nD5IsFni3TEJRod8ptfuH5EAdXnO8D7w63EypuiXarWZlUWweLs_-Tr4-XRuN4OCS6RelhS1FQ4-dCCS4lHcA6O7HmsxGTmv8XO3Pp0KPS1NxPiQ4QK-AF7IzUn5aVCwtLyjAHdGocrlSuUJxLyoVbpQzKLc2CG6QWNMHhd8Del1GMkOK7UCBPXkiiqCCjQUQI1OGVmTbNWTKnBQcVyFt0wOghFoPqXxVqfSlXCNWOUQG_vLV4GxqUF_7COwDM38n4ypvEPi0J4tGqpiZU_vhxOZTHQINXV9WJYKaiPIO51icjNEV6vz5RJgb34IQWmjgVnclX6xhWTMSpDMdgS-f5PeRiIKgvaUv0KzWibnHPrwgyrCxpSCeqpwyypGkRtbBZAPsQe1D76MAMBbjF46dx81c6JEDL1CGZPYJ4TpHizFgWyyuXsRLlv9NQg1wL6xRRxE4pNm87gW8HTRGfroUAkGERogQtkeNQasfV4oPqsnY1-TXnBlOsZx30I-JegB3le67BO7yUVxjTDQ7X1ahcSwameCDUpZbAWMsYfPXpDwSqTLUw3W9jTwKMdVRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vKKKotc0ZP-DeFC97wu8PZMAoyNVAZXr0aqzURL6tWX6A-_hKRnr5rlFZKt4es3OcBz0OpBv2qic55rvdeWKjQ3UWVBPF5e8--rcq1h7q2Mf-nD5IsFni3TEJRod8ptfuH5EAdXnO8D7w63EypuiXarWZlUWweLs_-Tr4-XRuN4OCS6RelhS1FQ4-dCCS4lHcA6O7HmsxGTmv8XO3Pp0KPS1NxPiQ4QK-AF7IzUn5aVCwtLyjAHdGocrlSuUJxLyoVbpQzKLc2CG6QWNMHhd8Del1GMkOK7UCBPXkiiqCCjQUQI1OGVmTbNWTKnBQcVyFt0wOghFoPqXxVqfSlXCNWOUQG_vLV4GxqUF_7COwDM38n4ypvEPi0J4tGqpiZU_vhxOZTHQINXV9WJYKaiPIO51icjNEV6vz5RJgb34IQWmjgVnclX6xhWTMSpDMdgS-f5PeRiIKgvaUv0KzWibnHPrwgyrCxpSCeqpwyypGkRtbBZAPsQe1D76MAMBbjF46dx81c6JEDL1CGZPYJ4TpHizFgWyyuXsRLlv9NQg1wL6xRRxE4pNm87gW8HTRGfroUAkGERogQtkeNQasfV4oPqsnY1-TXnBlOsZx30I-JegB3le67BO7yUVxjTDQ7X1ahcSwameCDUpZbAWMsYfPXpDwSqTLUw3W9jTwKMdVRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=h14dCSeGbtMf65y_TOUNyknvwnGsgpDfuuOLwBfRZJOcKQhVfNtT129_FDjPW3HRoni6kksEZQPKlDkbpJ4wywgvzE6icItUwYrTnpoMT24ylNqc1R6JSbYIOc_wvrjalgRfGRwyuZXtSR1ySBlr7u5OuSvjxXSfQmDfyGb-li8QFgp36a9_4Nx6Ft7K7iNOiz1zQEFdXmyTR9ZXpBzQw0jUSAI5u1tYceWUuwBC00bVI9nvjZSiEm4HyDrWfadbP6dqv5iBjdPT8LvDC8w50MG00LbYSfPepwVTUe1s78ck4s6Hc-h8YKBuBvourcOcaoBc7gqH0zGUjGQJmjGkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=h14dCSeGbtMf65y_TOUNyknvwnGsgpDfuuOLwBfRZJOcKQhVfNtT129_FDjPW3HRoni6kksEZQPKlDkbpJ4wywgvzE6icItUwYrTnpoMT24ylNqc1R6JSbYIOc_wvrjalgRfGRwyuZXtSR1ySBlr7u5OuSvjxXSfQmDfyGb-li8QFgp36a9_4Nx6Ft7K7iNOiz1zQEFdXmyTR9ZXpBzQw0jUSAI5u1tYceWUuwBC00bVI9nvjZSiEm4HyDrWfadbP6dqv5iBjdPT8LvDC8w50MG00LbYSfPepwVTUe1s78ck4s6Hc-h8YKBuBvourcOcaoBc7gqH0zGUjGQJmjGkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCluUf0Yp7SVYySaiz_FlwyBV5SiQLLu23zERKOdwuFc_NTY7GPWShl_juxNv6xScm_buKyBpzwP8j9P8gsL1lBDR-QclPdJDq_BObwEdfznuoyVuixRNVl2h_RzqtsZIi4Qxto8n-q8i2wxx3dLqhLB6ThvVMWitiORJcReUpAyy_oDsewkgKml6HYTjf1qphi4DKCRP5yAhVbaAjO3vB_a4yQuS41A0Oaa12gC-9TWJYpPJGjgruRsPt709_fXUleLjPo9JAGrSe09ITQ81G1hTvvXkSX5Os1N79fIsMJGgD9u0dYttwd2xkhaqahieeVjRwfHQYwL2FKnAfMF1NDM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCluUf0Yp7SVYySaiz_FlwyBV5SiQLLu23zERKOdwuFc_NTY7GPWShl_juxNv6xScm_buKyBpzwP8j9P8gsL1lBDR-QclPdJDq_BObwEdfznuoyVuixRNVl2h_RzqtsZIi4Qxto8n-q8i2wxx3dLqhLB6ThvVMWitiORJcReUpAyy_oDsewkgKml6HYTjf1qphi4DKCRP5yAhVbaAjO3vB_a4yQuS41A0Oaa12gC-9TWJYpPJGjgruRsPt709_fXUleLjPo9JAGrSe09ITQ81G1hTvvXkSX5Os1N79fIsMJGgD9u0dYttwd2xkhaqahieeVjRwfHQYwL2FKnAfMF1NDM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPEzOT9JeSZ0lS3jhaF_i8G4jY8CiEvtE-QFA1rUCCD8oMyc-qkyQCRQfmtF8MZrO-q-GVIGYvuqaeBvI-IGLThwCGsZn4AAbkz09pmrtdrKKGsdiBnfoUtMqRj8eSeiy0NpcFWPVYhdrr5l8Q3_6Ic6udm0Y6-NuvF6ZdjYJut4GwRNQRSYgVxQ2x82xqesPjD1g-n8XtVzJY_Hi29WSxStNDUOIbm35fsZzuYAuJo9STOffcFXLRHAYw-IF6MmJwUwKNa0CAGXXbxaQ1PljTmYRnTE6RcMMFxXVAS0tRwq-IDCdwI335Ts0jhWRg0ai7mrOeomSvy2hfeWwWf6GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQFHBGQfc242rr4h-x1ZLv67tGqGl8hPCSRK-5wdNaBoWMCP6E1tkJQBc47rRWVRxFrD6FuvscrzIFjRlKEEcBL7fSxOZCLk7XdHLNXkV4cW5rx9-blkX_zIr6hQDPDiaI6cuYZ-tsxb-4dMXpMOR0cOS7SSJOlIc8mcG5Cz-sq-pj3OLkC_-5RYD9YAf9DNcZmDgN9_XtV1YgwogkF-W5xMzgZhC7UqZtlFbB4uedekz2_BzpyLtgv5ikPS4CUz6zO5PNM5FbMViHF7Dz7Rtp5sp8-2u5TNDCPVMjTWL_pBDW3pGIxP6Sp6yCQd_2ZkhfI9Mabp-1frZ5JoKSnKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGVQc9Pk4jwo2oDLf_TjmNxzpriBDUsHI8XTAbqfX8KWba1ppBtLrJr8Ly-BAu-iMuglW_agO9rWPvJ_vxKBmOwNwsic3cjKPuOrYSio6DpDR6z3-8vTc75vkP2UGJJU6DYBqfKjsVkR2r0IGelq5ZvV-f_JJigwY7wHAuLZwBUBCaP0yR94D3pwFhCVKfguOWYIhwfJWa2x2UtazudDRZREhHhmSg_9GncBpCs0mbrfr6D3MO_QL2zgZbqxjibthvi-4RyMV93XWXRNJZ7goJyC08-141DdeFxkJN_N9k-5y1yMqUNuBF-tNKZx1YTQe5FtO4uU2udKxB5az4Mmbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nM7Wm-pj4TPqt8FaY04ZnAG8vYuR3ySWHoQLQnqwHeQoggaspxJNlUUDg_chHzzD4WyIp8t6jOitk-bRw4fSTPRSGjKofbLFpz97eEC9OGTMQp0SL4Z6hiQg4Npr1nKDZqg4o15kAsUfwD0X5JZQibmoM6KWMetJQAPmOe7a3UgCGwLZDvL55cNGZUSF-jw2YEzlShQmsONVzR1KmMzDYa5HHkEM0tiMsMZ4QlZEGNKHOZMkAPJkRlgmTi737rxKFGmNSNdgVV6_elBVN6_J3P_bGKdv2xKzIfV17qMzTpAxKhy8H1MTo_R5bq7-o7Mdvg4aLnxvlGn2NrOsdzbf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nM7Wm-pj4TPqt8FaY04ZnAG8vYuR3ySWHoQLQnqwHeQoggaspxJNlUUDg_chHzzD4WyIp8t6jOitk-bRw4fSTPRSGjKofbLFpz97eEC9OGTMQp0SL4Z6hiQg4Npr1nKDZqg4o15kAsUfwD0X5JZQibmoM6KWMetJQAPmOe7a3UgCGwLZDvL55cNGZUSF-jw2YEzlShQmsONVzR1KmMzDYa5HHkEM0tiMsMZ4QlZEGNKHOZMkAPJkRlgmTi737rxKFGmNSNdgVV6_elBVN6_J3P_bGKdv2xKzIfV17qMzTpAxKhy8H1MTo_R5bq7-o7Mdvg4aLnxvlGn2NrOsdzbf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX4k_4TeAd8JIYG8yCcDyG4HdS19N2r4XdM26sBnRNj4w20GZJlmiiZ84e2n89V0OU_ZPZGDpOAds0tt_jBt6MEEuD_ZPwS325S-_pdIYYFJfTN9oZfNcA8ig_25rUQd5oVfpm8Ge7GWYLSqtlrBA0JScV0F4MhsIbLk1hyfKm8uR0kH9Gcw_5YvuIW3oacC7XS_SCsAYIJKZK7AyKCutaeBvl1Sz_vyWqmeZnKcC85d6EbyGDhflEMuzQgzgH95zbyJOatM4gzAQkc29XMfj62hsn19cF_0KGmGXVxJL6r-Ymvww9FlJsMwGV4Yulbx1V31Qs6sSp-cARFca45qFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mH753k6Yrtu90PiH662twJcJb-alnOXX_c0i2lHXt2AbeuiPbqDFVoNOefHRyJdLZZcwuWF3npKQK7xk-Q5pZrSDSKuHECHFR-nL9m2RuBFmNhvNGbxgBmmtlE6wMTD8f19ucHea8CnnvrpbsM6TnqVmJg2OY6RHfU4XRwUa6-pQtAKMN8BY6Q7Y47Pq2uzyNenBpMXi4RjpghGN01os0TWfqQYxpQA2-Yrde4fSnB3-zCzAOSa5OxECgj47f4kguGGX6MfOSC8HuYwEpnsVIP3cks3NplGXf671p8krot2srAZ9ImW2dE8rnqmQ64oahWjI0a8XbycLFfgndt4OVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/es-IjJamKtdL2kpbcCbm19jUyXjBnop5-ic_10IE4yltwizfstqBWpC4U9vsX82qvtgOVx_ngWHMaIb0EvSyisJEcJR60jblu4yhZTuNEyLowRoLA7JPBjZghssVxBuDzHhfsxBaMcKWOv2XUnnlEIAEwQ-fE3U9LROTcR5zuNsVgtqaQH7VQN1mzMgw7QvdGgKGaeMKRMx5FuZX2XcKwW3mTFaEzkEfPx6VW7djjqH9qGIdbqzACZwqxapfsdaIy-JFNs1ipj3RACTrxYlLg9ifTowPd1NRvheDqi18wZJNXfl7OSQQ6h7IFaHca5QlaksvGbgK65c4jf0-Bhmuzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHg2pE0hwfWm60trygE0uehtoZdsaFWSONjohvNRLAN7cLaZ6rZS6ZUU1Om2gRYa7Rud-n6IuPr6pIXlnpNFhOUWxet__HKy7fZBHhd-_LOei66RLASZu4hnrqcdsg4mMwBoYL-c8qPvNRY5Q-81PgM_2Iv7x4YCxaTTSiTcI0l31HTK--0nz6oKhccwwczuB5XE4kmDlTblyG2sKMeJ8d6mDwHtGs72JXsI5r2auQ4QLMby7-AfVWEitC5Hqtnz7QPNeduWiyzarqbPi4ngY-JbWtYm97ANu--M16IqpPkeeY2DN2b0E1G2ceoYBv4qTEFBZPJE8jelG8uhMOeIUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=DG8Tdo51x45vBtNFU2RMvojJemLvC3BGUwh2yMGOFiZ7iPRbA9K4dEQ1iqHq3r6zuDvkpPNp0iufzU7-jCk11C5H9E_tBO8n1q7H_wdKwrJUOq2d3Y_0e6m3xlvwcmgOODqg0PjpCguk0H_re5vgEYDPaQxm8DgwRA9LFDSymrBpEOUN7kSoFVSdvI8SK-tGF6l1Nbm5hVEfXn9F3nWQlH8uXnEz6UNz2IL6EEIHMvgBZli8FM_kLY8137UYi6nu-znHPUASP61xlgoBnW61-9JtORJzYMJ1Vo0hzWdJIqSdnaFBXhPhBBCKor1Z3q1YgjLXMDhDBW5jfUEp88h8gzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=DG8Tdo51x45vBtNFU2RMvojJemLvC3BGUwh2yMGOFiZ7iPRbA9K4dEQ1iqHq3r6zuDvkpPNp0iufzU7-jCk11C5H9E_tBO8n1q7H_wdKwrJUOq2d3Y_0e6m3xlvwcmgOODqg0PjpCguk0H_re5vgEYDPaQxm8DgwRA9LFDSymrBpEOUN7kSoFVSdvI8SK-tGF6l1Nbm5hVEfXn9F3nWQlH8uXnEz6UNz2IL6EEIHMvgBZli8FM_kLY8137UYi6nu-znHPUASP61xlgoBnW61-9JtORJzYMJ1Vo0hzWdJIqSdnaFBXhPhBBCKor1Z3q1YgjLXMDhDBW5jfUEp88h8gzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ZhP5-N42CdiqGeuZ3Cv9a6T0aFplUKHikhCH4Lp_kejw6DRlU14z3llmR7k6sTa8lAZm9MsjDyVna6a98HOknBpznjctihrCWnXsOBnWjaqHrxWj8cP92kJzjQrdosXfI5703sfgK-ORHUWUl3Ouz5SNxv6dneMkjL5xGJz5wcFIJbqo6jZP6SPkUtSVE4B8M9tTFLRl1iSFwU9Pi70SBTmH3Jq0y-EyW9ipHGK8anAIcMjzV5a9JtzxQh2XyaIHU3Dokrd5GQWUcurjj1x8czQNoN12SWwYj1VGSMohdGu2m0pCHtcqKNZqXIcMKINbuCVRCh8izWgwCCZ44nMEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ZhP5-N42CdiqGeuZ3Cv9a6T0aFplUKHikhCH4Lp_kejw6DRlU14z3llmR7k6sTa8lAZm9MsjDyVna6a98HOknBpznjctihrCWnXsOBnWjaqHrxWj8cP92kJzjQrdosXfI5703sfgK-ORHUWUl3Ouz5SNxv6dneMkjL5xGJz5wcFIJbqo6jZP6SPkUtSVE4B8M9tTFLRl1iSFwU9Pi70SBTmH3Jq0y-EyW9ipHGK8anAIcMjzV5a9JtzxQh2XyaIHU3Dokrd5GQWUcurjj1x8czQNoN12SWwYj1VGSMohdGu2m0pCHtcqKNZqXIcMKINbuCVRCh8izWgwCCZ44nMEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=nzfYKs0dHEOW6FqGhX_bdzd1IMSXMNmxnqyhz79LF4q0kg18-BaEn-fzSh6-KfzEMMPriDiEPWJW8Aoqw_7VgYezXxoeLG0NRhvKyOlVK-gQ5h_ooCCDc8eTCi5zHdhUY0iw7XsEfY9a5QMr8_4hbl4li138nkOaiCaK4er-G7brekrt0-CdcGxZSzuRBf_a1Et0OaN2CjQPbQ-djiaxnennjffthZ5DCZyt4aRs9GWsGJZGsH_gWIjGlqS5S8O3yok2dnKTU64fCpjqyTET1NOOuUTrf-Q5KH5uizeXbyKnPyzkOGskNOiWZhp8tXaTgFnuJ3zYYCEKtnlp2NuttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=nzfYKs0dHEOW6FqGhX_bdzd1IMSXMNmxnqyhz79LF4q0kg18-BaEn-fzSh6-KfzEMMPriDiEPWJW8Aoqw_7VgYezXxoeLG0NRhvKyOlVK-gQ5h_ooCCDc8eTCi5zHdhUY0iw7XsEfY9a5QMr8_4hbl4li138nkOaiCaK4er-G7brekrt0-CdcGxZSzuRBf_a1Et0OaN2CjQPbQ-djiaxnennjffthZ5DCZyt4aRs9GWsGJZGsH_gWIjGlqS5S8O3yok2dnKTU64fCpjqyTET1NOOuUTrf-Q5KH5uizeXbyKnPyzkOGskNOiWZhp8tXaTgFnuJ3zYYCEKtnlp2NuttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZIUoB1WvgMJfB-ExFUSTqmstmU2RI3KpxTvVLk1mftgstxVb9wjXhL4gkgPanzYVbGTAEr4Uyah7MgkxeOBdXoVHT5uKMZsXHWWg5r9Fd-Vlc9qwb71ShT6_rVIoIRQZrtr_mA3zh1mNZ-199c5XATNk1JKMsZtf1ShTleNGTbSR3ZZ8eq0nxWHuTUfF25DOIewga9_-iSEnCwwxRpA4c2dP8ZdG5C_rK8iOK4Wif_RUAOyO0lCxpPYsEV_7nJLqkOG4r4Mg1g_fHetdwoYV0jvn8As3LK6Eh30IrVgAfvNfq_tLOi6sKQUHpudKCwDbEgld1SuS2z8V3qK0bJv2Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=hofW_dAdFq833Ta5M5RguLSl5hrtLKZpr-J2RoEBr_BtWGhStl0ceRACkTvzOBGbuKlSn8Ip9OMMr_NIFN7OtA82PAHd3ZDEb2VPX78u9T8k1w9BxIp9oKUuO4yzmJykHmdf_W9e_0LToadMyAEieLjeeopTmBJ4nsz5xfcI8IMSQXlJS981l_p2W_YvqDUOpOS_5XLrhdHGR15RcscSnhcSc1aqy05fGH9TihCQ1QgVqbT6kIqQtZTLxBurgpPiDZZIfX5LaGIcW5I65cwF1Ovs04a1JZVxDxzBD7aKbMtZ322vAweYL8XFgv44aWd_LSEigBrjlsR-IjpZsVGDcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=hofW_dAdFq833Ta5M5RguLSl5hrtLKZpr-J2RoEBr_BtWGhStl0ceRACkTvzOBGbuKlSn8Ip9OMMr_NIFN7OtA82PAHd3ZDEb2VPX78u9T8k1w9BxIp9oKUuO4yzmJykHmdf_W9e_0LToadMyAEieLjeeopTmBJ4nsz5xfcI8IMSQXlJS981l_p2W_YvqDUOpOS_5XLrhdHGR15RcscSnhcSc1aqy05fGH9TihCQ1QgVqbT6kIqQtZTLxBurgpPiDZZIfX5LaGIcW5I65cwF1Ovs04a1JZVxDxzBD7aKbMtZ322vAweYL8XFgv44aWd_LSEigBrjlsR-IjpZsVGDcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=hsx0436Gl9Z86wWI08DaL0DhvmBTzWtawssMrb6sHVJq_AsciN1yt_CIqtbljS2mltbH-wiXgZXl3IhWO1WrhOfNRhoq0GJI_D5mpd4u1_NQEYLpZhqJEc6sF0bL7cE65HYnAZfQvRWH5Qiz1wUzZEyH-0fgdvRgs5dZT6l7A18GonG8eJwkR-5htxchbS8gC68y62MT50uq2esLDWEQq0utIVQ9vtZObB17V9lFFH80yetHKact7_ejcgPWbb6Zdwj6NXiO7oY_q6SMqECxWlklF517nfesDMpHARE0mN4U4QXAOMdJfwJF7bf317osclqWPLqA4e6buZoaUzQLuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=hsx0436Gl9Z86wWI08DaL0DhvmBTzWtawssMrb6sHVJq_AsciN1yt_CIqtbljS2mltbH-wiXgZXl3IhWO1WrhOfNRhoq0GJI_D5mpd4u1_NQEYLpZhqJEc6sF0bL7cE65HYnAZfQvRWH5Qiz1wUzZEyH-0fgdvRgs5dZT6l7A18GonG8eJwkR-5htxchbS8gC68y62MT50uq2esLDWEQq0utIVQ9vtZObB17V9lFFH80yetHKact7_ejcgPWbb6Zdwj6NXiO7oY_q6SMqECxWlklF517nfesDMpHARE0mN4U4QXAOMdJfwJF7bf317osclqWPLqA4e6buZoaUzQLuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=rsUL5wOqna0reYmI4Oa3xNaLbf-kLDpAKwtxNI6OWJEKK5RYi7_SwKSI7XwJ2nwhVCB8g5x1ybkmIcKDL8fN5vSTEnwHUD58zTTo-g8oMZMxtXTru7Wi2TCLOO35aYeaCHJmFkhm1dFNGqCDB7qE-2YfA_gz992COlgXs3LUEQp1L0iz0lPkbjgvRI6i1_bPg06aZ08OOjuoxKjVCsaFhC3aLOIOEGIYl9CQYSb3-gI9TVv_EO7lWjjzIk2ON_q01NFazIgMobIZx6EnITa5e6JIQx_ruOaY2bvf6okzIJNiB4RRgnxYoKnNRBd8Wv-XLcxXD8L329NtsHvxp_pPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=rsUL5wOqna0reYmI4Oa3xNaLbf-kLDpAKwtxNI6OWJEKK5RYi7_SwKSI7XwJ2nwhVCB8g5x1ybkmIcKDL8fN5vSTEnwHUD58zTTo-g8oMZMxtXTru7Wi2TCLOO35aYeaCHJmFkhm1dFNGqCDB7qE-2YfA_gz992COlgXs3LUEQp1L0iz0lPkbjgvRI6i1_bPg06aZ08OOjuoxKjVCsaFhC3aLOIOEGIYl9CQYSb3-gI9TVv_EO7lWjjzIk2ON_q01NFazIgMobIZx6EnITa5e6JIQx_ruOaY2bvf6okzIJNiB4RRgnxYoKnNRBd8Wv-XLcxXD8L329NtsHvxp_pPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=lMxP6dbBS7W9hEe5EdHZmDfvbjgX5gyu_SoLzPrCrv5fpSKe7Ym7hvUBNp7jJeKxg0EqzhFFl9IEXIZzc81MQTOz87Lsj2DHOJSEvLed4Yq2FwwYpVmpAOdzvJhkArEgXeGAAKvWmIFUADTi92z1-M9MfiBbFqpsu-7brGpGChNGTgoUlDSjAZFpilm-7SIWPEvJU7RtH_zcX_t4gRW34MGiEnWQet0YoY7TW8iNDSak5GNiFUVFeClLh9xBY77wHL3T-r7wIaIknh-00X6ylbK_ZGYcxel-KMxL7dR3ZRuFC0eYc3dXoidMdHln0W6OSlh4vumOz6n1S_myND3oh7Ax-M_sEmwiLE-Fs8ahnRAwuyKEcaLXozlBC_ND7oDLNP5zxmR-xr6HgSoRRhUppjxkYkcAhbJlsEa_1ceBHMlwN7QLwbt2-lRmau_r3mFfMdoN72NiMR-q4Z-Ep0XHswqS7zl2WxAzPMzFmQsBEUEkuOWiUxC10gwQs_e-8F654zgVx1wN9FcGFN_p4EKPqyBQDFCEpVNdeHsHCk47qyBEw9_LcGPhR3tM707heLJpNZwEqT4XlcUCkqGg767tuMrOONte7ISvG-WBJhyyuxVd1cYY4Kp03gHaviJ7D6q6Jn7i0Wee9FaB_1qdXLvB6SybKmVU86dbFt-5hNoCDjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=lMxP6dbBS7W9hEe5EdHZmDfvbjgX5gyu_SoLzPrCrv5fpSKe7Ym7hvUBNp7jJeKxg0EqzhFFl9IEXIZzc81MQTOz87Lsj2DHOJSEvLed4Yq2FwwYpVmpAOdzvJhkArEgXeGAAKvWmIFUADTi92z1-M9MfiBbFqpsu-7brGpGChNGTgoUlDSjAZFpilm-7SIWPEvJU7RtH_zcX_t4gRW34MGiEnWQet0YoY7TW8iNDSak5GNiFUVFeClLh9xBY77wHL3T-r7wIaIknh-00X6ylbK_ZGYcxel-KMxL7dR3ZRuFC0eYc3dXoidMdHln0W6OSlh4vumOz6n1S_myND3oh7Ax-M_sEmwiLE-Fs8ahnRAwuyKEcaLXozlBC_ND7oDLNP5zxmR-xr6HgSoRRhUppjxkYkcAhbJlsEa_1ceBHMlwN7QLwbt2-lRmau_r3mFfMdoN72NiMR-q4Z-Ep0XHswqS7zl2WxAzPMzFmQsBEUEkuOWiUxC10gwQs_e-8F654zgVx1wN9FcGFN_p4EKPqyBQDFCEpVNdeHsHCk47qyBEw9_LcGPhR3tM707heLJpNZwEqT4XlcUCkqGg767tuMrOONte7ISvG-WBJhyyuxVd1cYY4Kp03gHaviJ7D6q6Jn7i0Wee9FaB_1qdXLvB6SybKmVU86dbFt-5hNoCDjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=G0wbEY7LUddFfYy2t8pCyjpZW2Djz4GHtV_0EU5HvT1BKc4jyrbtOz8ytjlnIdMbzyQifLmHU16XBrqmIH6YRPblyb1JaodzR0iBoNfcew_ZhQDtCpOhpcADKkBQ-MWN_6BufMw91iVaJuajxVjiXFgyRElt8dO3Sy4WbJX5z3rjpUhPs94KIvDsZi9SMqwNV1hM2WiBF9u0P90Up6H33gIuHX_ZnR9QJ8m5tnQX8b4EgtT51fSztZSv2aUhNrW8Gmo8UrW2dPffL-hVDo7CYCdpbsPS3fNO8q-7isAfhMGhzXnXgq3BGHxHHMV3qS2caFX9ZTvfNXX_w9cnDE3GKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=G0wbEY7LUddFfYy2t8pCyjpZW2Djz4GHtV_0EU5HvT1BKc4jyrbtOz8ytjlnIdMbzyQifLmHU16XBrqmIH6YRPblyb1JaodzR0iBoNfcew_ZhQDtCpOhpcADKkBQ-MWN_6BufMw91iVaJuajxVjiXFgyRElt8dO3Sy4WbJX5z3rjpUhPs94KIvDsZi9SMqwNV1hM2WiBF9u0P90Up6H33gIuHX_ZnR9QJ8m5tnQX8b4EgtT51fSztZSv2aUhNrW8Gmo8UrW2dPffL-hVDo7CYCdpbsPS3fNO8q-7isAfhMGhzXnXgq3BGHxHHMV3qS2caFX9ZTvfNXX_w9cnDE3GKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=DIVycWVIWsHL0_zmrxgaBc6pMlCpKLIBmuOX7XI595ZthJzBTzeuhqgilb9KrKGgUOWIPYmvY89f7Aq2chyxDgV67bnKe6rPwBlScE7ugyMN8vr1NqvLIFyxZ994JpWveMr2N71QuyzFCd3ojf0r78pT3EfUH4OLCM8ojD5XlRgFP6a6NvhkfBppRm0RQGaiX9BLpmjpiu7F9jmVpVc9Jg-aRm6Kg-ypGvRXs6nMTxIx6avzBQbxCI6xf8Gz24uEXY2v8uX0koCAYeIpgq7GM18QrtjEy6BoY3j5vjfNwRIa23uQPVpgYKvTYb_fhZKq10MLP4cLo-Qw7qsauF2aYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=DIVycWVIWsHL0_zmrxgaBc6pMlCpKLIBmuOX7XI595ZthJzBTzeuhqgilb9KrKGgUOWIPYmvY89f7Aq2chyxDgV67bnKe6rPwBlScE7ugyMN8vr1NqvLIFyxZ994JpWveMr2N71QuyzFCd3ojf0r78pT3EfUH4OLCM8ojD5XlRgFP6a6NvhkfBppRm0RQGaiX9BLpmjpiu7F9jmVpVc9Jg-aRm6Kg-ypGvRXs6nMTxIx6avzBQbxCI6xf8Gz24uEXY2v8uX0koCAYeIpgq7GM18QrtjEy6BoY3j5vjfNwRIa23uQPVpgYKvTYb_fhZKq10MLP4cLo-Qw7qsauF2aYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSKvIboQqUO_OxayA94WW9LDRqXkItBG9EjOfU_gOJwKl2Cx1phX-b-r5IPJ5WbE_LD-j1OVNbvnoblSdZqrhYHM2wVxFi1hzo3TZs--OCmHqmTscLoMmTywc2OKyRRW1MdyvhA2nwnGmPgyVjK18cmxBjj1sbWTYVw1iUp1nxE6rCXRJ1qAwuFPXJ2swFGnYzq85N96MIrxIDDC3N2HAgMKUladVYjTPHEfyD62s5XuSNMAJIhe0yYmTb8qfO0ULdLFVMlS3r9F-u-uWVYV85gEyfZxmq0oC0iyCV8VfrSJo5gFhWllDXQs0Cpg1EFWH0qkJy88Vt7nv_LH1AM2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc-1hbQTQ4bpXypJfdjv6ECIWFH_xqTEUxOkj24mPqMK0LT4qMbGijli9Q_KOQOYstMAFZlNEGmo86jU4qIc2Hx_BYSiDCEOfdMCxY6FVtBm3NtJ7YXvc4uhC1GlqXJaWv6c0Si6-rC3dOus_gVU8sWXr5Gv_fzCmLyGixXMsiHWWa0UBQGIXrR6UUoEcg66-etQyojRNxM1RElFG3Z9X6DqV4xZ_Od_C3hhvQTCCho2l1ledqPOnqOzYJr3dtM2-TPk8PR-PJW28-esFSYpVQDEtZbhoTJDggvDIE-40zlTXn76CLxl61gKGkm2jgHACYgIys2YTsRmQuaeAfgzng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kyc50X9Fhb13I9xZ6W7lGzlup2NXRINpv6lZllzDDnVK30_B1AO6otYipXLSVqV8d8dlMslsZweRmioUh4SQ98yyebL5bEeqzP5IpDSVgPZEnu6uj8F2Z4eQ1WTh-BOFT8dx5wrM6bggEDnj-vxhcyj19oEw2ghgUrXrUJBdpkJnc9G2GD7AaYw6VJDelRt2qPTXNxRLsrdazGdGW6PeZVWtuRqDB8kSSUBtK8xl9Ba7C1w2mgmbnhx4BzVNZOqoxxKWVcdXn4xfnC8NttLGFEl3ySlLJ0jt7lRyhHFJqeWfczE8u2Fu4ptDAOv26WTKIKELQNzWkOhNebewTZ1iaDza_wEqNePYjXKxeH5FLag7OPBp7P1D1GKLB-giZ2n3Vj4za8YO2599is5KrWD9WQsc5KPcj3pzWNN49JqhR4zPi0hp2PAEztffmCrZvKo6hbeOZcOyOPixY7D10KODln2n_mitIlvxNECODxvIEiMx9pwJlHRiL2XnJKVlBbPecCVUWkfjSvLBHzXMZ4To1Q9FfSXRXk8eR4GBoXMECJ0QTjdT62JAB5UsJqdgezIv9gefLN_o4uLP8lfNfmsWIPfYNKRGSIUV0T3QXAf1S0CT6wrHpFbt5KAWDr-S9KJtdIvxZ_RPqh3Me1YyaOHzlY_JgQhE3CRUA7dFOrtZfvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kyc50X9Fhb13I9xZ6W7lGzlup2NXRINpv6lZllzDDnVK30_B1AO6otYipXLSVqV8d8dlMslsZweRmioUh4SQ98yyebL5bEeqzP5IpDSVgPZEnu6uj8F2Z4eQ1WTh-BOFT8dx5wrM6bggEDnj-vxhcyj19oEw2ghgUrXrUJBdpkJnc9G2GD7AaYw6VJDelRt2qPTXNxRLsrdazGdGW6PeZVWtuRqDB8kSSUBtK8xl9Ba7C1w2mgmbnhx4BzVNZOqoxxKWVcdXn4xfnC8NttLGFEl3ySlLJ0jt7lRyhHFJqeWfczE8u2Fu4ptDAOv26WTKIKELQNzWkOhNebewTZ1iaDza_wEqNePYjXKxeH5FLag7OPBp7P1D1GKLB-giZ2n3Vj4za8YO2599is5KrWD9WQsc5KPcj3pzWNN49JqhR4zPi0hp2PAEztffmCrZvKo6hbeOZcOyOPixY7D10KODln2n_mitIlvxNECODxvIEiMx9pwJlHRiL2XnJKVlBbPecCVUWkfjSvLBHzXMZ4To1Q9FfSXRXk8eR4GBoXMECJ0QTjdT62JAB5UsJqdgezIv9gefLN_o4uLP8lfNfmsWIPfYNKRGSIUV0T3QXAf1S0CT6wrHpFbt5KAWDr-S9KJtdIvxZ_RPqh3Me1YyaOHzlY_JgQhE3CRUA7dFOrtZfvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcmNWGN7As1kE6DShPKULqg9fX5Qxm4wjGHQV9Kw7wMVcEFW0Mlf674UwDa8rfVdBngrdHejwCGMIuVqXjGOXpCSARY8TK82oTOUXI4cIonVtOhNjSzyvEQ8P6HwMyFCvbPhXN_VBfmyMKE5YEC2e0kI5OAYb3_bFARefJofKeejhyR1bxGWkp7dIO1YhigeETlnZYuSPMcfkeRfbTa2xH-X7JxDm0JuYBO_9xiaP4iDJXsA1X_Mevb_A31Q6Pb_XLSIuWiDTsVX9jtSoFwKwC5v2maVTL2dysmZEBh1O4p6qer5mmAMr5VHrtHZauX1IFmPOZt-NxQJz5at5wtrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8h0Cymkefz4Rno9wZxgBiAtjjliHWI57ktprFE3F8nqZAttdg9jwgHaeDqotBdZ1gqzzvqTIeJ1yutgwyBdySqD8QyhDnWRAXzCDmTnHakcooGdNlwsA0MRNMTrXp9yhZkA0kQkOxN1xPopEp54Ru4ftXiBk08cwOZXNPF5b1brXkXX6zPaJBdN1pZ1v0MRKxemndsFi4gOA3PasniDQxDH-l9i2rdW34utgcLayboFumt32Lwgauh-8Dh4IqustbTV0sHgS0NLz5rmvM5HcI7nC43e-RgPC7wzvaOhorvgmU166NANPVTjIHq_p9ezOPdEYHhS8e_RyPaD9TZeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
