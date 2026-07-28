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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
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
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0lCcbE_hdZTWgj6kJVfGOKPdahpYon1kuntesK4pNBmaCryBSWd_bWxto8r-HuUPLtod9HdbtR0L-jfGZf9S92sKNHBKQAdaSmHNB3E90pvl0ST3-sq0OYvTCoJDi1KHTeIwEu9Wq2GDwmawBSKyN9kBUr-NvZNINFyj0ShYbMQWy7n0FH2e_Ukd00vhCuFuxgFIOzcdKoss6_zrsksvjbzUrHYomd6I9BUIngIlX9Dz_eJe9hMgm0IGoxq6SRaIrtm9PJT0coHWGRfRSZ8Brp3hOM_QA24y4vy6is33QXuvoQt_4ULdzwnpH2Q7wqZsQQe1OvXNW3LbfjeDxjGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJS5e3UOIiHiXf6TvpKnaVk-xCfT1iwmdic7Hv3R6EFYA6TGLyDHx-lPFbjl-Jy122XK6zIonTuWezuKeC8ESG25WDDOSRM0hDCIS9UXmCS9NxFAzo8hbGJRHt1YeFvWJ2iy-aE2o_j--5khUWyxCWInTScd_AlDsYQo-oL7hWzZPXjGYfoo-nS71mbxkvPYeiM50fYqo_l1AwpPfFFJdlxzj9c_9CZRPnrBmI_2pnayxJU-Fo8xWCuzwgz97LZsaiNNjq4s3PNplhDYE0A7oebtQC4xJSZC9RD54QDojmXLusaFz71HyTZkr0PZ5CZjkBu6ySUfSA9qaiachKllMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJkYzUTySBqCWpZKpl04EMKSDvIP3_fhhu8Kp_Z87OXR3-IpyZvbuEFieNScvFJw48qPbld0VIbJTy0A3S2BwGzZBgN_KV0PGqwaySqD78iVNRje8dk7GyxBHbWCBiWnbAJjAPLzCP9qzWEqX2GtRtbgeWTnJUAA3Rvt91k_MnxVpOO1ZrbaOHGmbzG9oI4f53Cfv1HlOWDJ2zOK3jr7jYqpi3oGJ2uwSY_VotHxPkLsInayta3Tal7hNr0faWMpIcvCwc7oVWn1zknP3G2mbxHL4bzrAorvqbvpBu7UecZUEf_709P4rwXl-irYBZB38tsj5K-bKrNEHfXff5JDCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=u2a0Ih9JrA4DHhmn2jyqP5ANawaFHNpmcL0G9pc8JIgRS53NLCPU9L6VAtw0gchfmXCqjSKc_ocdDPKI-fM2W4FKeIENy9aDPVDjMZVIzX0-7bvLKxICXurGSJ_rXCaPh41CeKyK4Yywbw2EwrFdx-txoKqu_5aQJRnPXKakEdbZYyfDjOUtYwI5shpKtYKlLivzDyE7JaEut8UfUUiuJx541oNq6G3DWc2mHvRKRm3ICMUBuu3zxinGrySXPLlAFt-M3O-wIIQQMr__ujZjn3vNCgch5Q3_cBdKef4rjCpqHM_A80-k7n9JUhqY2TL2cjIdzOn7gtpUgf9u-iv0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=u2a0Ih9JrA4DHhmn2jyqP5ANawaFHNpmcL0G9pc8JIgRS53NLCPU9L6VAtw0gchfmXCqjSKc_ocdDPKI-fM2W4FKeIENy9aDPVDjMZVIzX0-7bvLKxICXurGSJ_rXCaPh41CeKyK4Yywbw2EwrFdx-txoKqu_5aQJRnPXKakEdbZYyfDjOUtYwI5shpKtYKlLivzDyE7JaEut8UfUUiuJx541oNq6G3DWc2mHvRKRm3ICMUBuu3zxinGrySXPLlAFt-M3O-wIIQQMr__ujZjn3vNCgch5Q3_cBdKef4rjCpqHM_A80-k7n9JUhqY2TL2cjIdzOn7gtpUgf9u-iv0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICyT2lcI2j9HyNjlo002UEBBw4HklPXVsEgo-hCXEtvDDxHHbmV5IvHwwWenx3jzjMjsJACJERs1QpQR5eoUgU4a0epxYma9Te_ufbY1l4XszIWSB5RSIC90wZKmjrA8hy3ujc8i2jdWRrOEPNOuwi28Y7cC1U1r4ErwMiqfa0XWUkCrfqnlTGUB49mClM_3bpMxZU6s98L9hIMHdY088yWhhwVkCHgxm-PyhtitZK5NInbNM88DtDYitHfdHWY_Uz9lvQ8LMJprCcvQMprVJo2J1z1toyNUKjD5VleQqtsFgGIlac6BC1-8H48ctSOp4VzzrBBIYMJJE5o6SFQq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGAQpzaCgkSJoktO_p569a4cGWF9sRVsD1QBfDfWXJ05eeiEUI1VUD-yaaL84rS5dVA3LcurGDd7bFnMFN-SadL3eo5fPcZmWCLRaiiEDmacaSqG7IZLyEvzG_LiDA476Dw0Xsm18qcHka-vuJinnQE7yXj6v3oZ3MbZIR3Xdi8bbeBTr-r_VTnJI9tKIhnhd5_dLPVpo6rI9nl_zUbn1j8o6EjxxIPoN10P6Or7JuvQTC7utPgyuM7VVB6ZSeViKnN01nSXW5_UuY72VmoOmQR3m5JafKBbZ5PuLMnHfqbvLOYiq75bJoi3grJoraVL2ZF0thHeVd2_gWhknVEbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZV-uBzF8djLVJc8wAQWll6-SfWW5sqpwuOXNv6AEGgKdr1D8bxkGqj2jqJMCJV4xzOJQlASdzAIfdE4v-xYUZbgYAjV3th8HhSdZcul_e0fpfx8_lXN3fnAFbCSYZ-CiDxmZynluId8roi8qD-KY-ikco98zGUMo6hAVYt7MlaeVpKp1fE-P-yu7McxhH7-xgc3_-4qwyLxg2NlZYXxDn8qb3co5cQzVSRSPVCJAIccCXrjFo8DtWMSuQR0_ac_3X2tLhyu2DrxftLXd6higG1KgXhI0tSrPHxEQpbn_JR9GohMShFGxiNBumqHn_i6IBuYKzqb4TgC2VVS_wUsoQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=GMY6W-K8M6_geoCGbL_59g7FvV_KZG-3OduwEUNwCyhnEeo7enEhwwjVWntJEeznkVMFHv7yIFeArAPgy-SDnLMf5yM2IKpcusy5ld1lYwpDzAc58h2BiHtvEOFBh-n64nuqJUMO7p3r39uGf3SqdNdZdfK-PmfEOVM-HMezC1lOujyUMyhAQkXwvxH3CaP7v9gM3T2HSaa6MWd9FYGI5DzE9xdiaOZTiGbUo5YjbOMgRkS-Txh79O6ASF8DTVNDPRcwIBR-skZuUc-GnUAFHQ_8lPhXebtmENxaBPkuIZMuWprvN4KePMPNa8cBb6bdrGlBKitXbwxXceRGdf-TEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=GMY6W-K8M6_geoCGbL_59g7FvV_KZG-3OduwEUNwCyhnEeo7enEhwwjVWntJEeznkVMFHv7yIFeArAPgy-SDnLMf5yM2IKpcusy5ld1lYwpDzAc58h2BiHtvEOFBh-n64nuqJUMO7p3r39uGf3SqdNdZdfK-PmfEOVM-HMezC1lOujyUMyhAQkXwvxH3CaP7v9gM3T2HSaa6MWd9FYGI5DzE9xdiaOZTiGbUo5YjbOMgRkS-Txh79O6ASF8DTVNDPRcwIBR-skZuUc-GnUAFHQ_8lPhXebtmENxaBPkuIZMuWprvN4KePMPNa8cBb6bdrGlBKitXbwxXceRGdf-TEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4gUEUcN3yQQLg_iKlkkhxVYz-6LhmXpyut9VzjlsSOH-g6q5axbZxW_vBOQ0UZ_TahBC07bS49zW5HWz5kJiN1iY6fsNWjiRJz-_bkW1W6Nu_nopF4mky1PDL7Jmtl1QLBE7QkYKxAB5PDVsqU-2mCEQ_TkObzBJtL8d-iHXJqnY2uDqgllqFInJdqJgSvCoI7WlWV_i4PNWyDlF5vLKMI592Hw0DTyATFx6R4sDsrOvBQDjgZ5NrwBSgauIegizgDq5JEx774LKdFEkgaos2rrAFTFU7jOHzqS6swFk1e722x7EOjHsGXuqt7m2Ye-0ixzQ1jy2c4ZyKOM3lkEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=vhwUrZqY27eefF4SVjpYNlIVo9fGzR1jzzA08IAh_NDzhKSF4c8L-qXIz9sSOCebgaAf1cKQCdGo_d1ZT39U1NJGychCznUI7se2XVAxuOecGANggo6tLpT4dU5goh5G5OskYZ3qXd6juUeo8rw2mtcoiJYn6Kh0TrIjseMCiMUNMk1cXxHrlewUNeLz4CyI8rpPefieFW1tLZF48lgyRyFlrjhZOEkR5uqhMm6QTROwkZs1l9VRhya2Dly2njL1ZlDErCc8ejxLV4RX4R5F1TjwGSux4ELE1cn_iIlRJBhtlIfjiVaP7qOwcAllkpmrTGERNZckC-YkOnA-bZKZ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=vhwUrZqY27eefF4SVjpYNlIVo9fGzR1jzzA08IAh_NDzhKSF4c8L-qXIz9sSOCebgaAf1cKQCdGo_d1ZT39U1NJGychCznUI7se2XVAxuOecGANggo6tLpT4dU5goh5G5OskYZ3qXd6juUeo8rw2mtcoiJYn6Kh0TrIjseMCiMUNMk1cXxHrlewUNeLz4CyI8rpPefieFW1tLZF48lgyRyFlrjhZOEkR5uqhMm6QTROwkZs1l9VRhya2Dly2njL1ZlDErCc8ejxLV4RX4R5F1TjwGSux4ELE1cn_iIlRJBhtlIfjiVaP7qOwcAllkpmrTGERNZckC-YkOnA-bZKZ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reqC4guQElchOWD8X5TpmKEm6xHBZ0K1RS-mMdMxBf8eGpJcIjDnKTV7AKr1Z8Q6mFezC9s5xJtdrO7A4AV5r1rlP-KMKPQn-2AN6NX7oikoiPJ_flYBiD9tBHUrUFaFceUtVQ2mxS9LTVGgG_aeuHk96HbdydXJRKjFz-p7Cijd5LBgsv2CF0eDw1LA56HfFvEqfVB_o5yPx8HHrofPF79yWE6V-V_f2SQ3hsVW03nGYnMaYRbpIOZeJooZLA4-LOMAIG8A9-3ayYb0D_YSJuY-LlK1PaJNCmDkvtlMDK_NsXty_A00KlDYbe53dwRBSBxYyKvADfqIFveRZL9K7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU9BSgdnLsB2TA7wAO68HwQvfutFe_cDLGWbp2Umg6q6KnoLMI41Va44BZDiChPXElZus1gcLS6KcAGqjnFo2oauNXJS6D1D5TZ7sphudtYkd7MC-4R6udFI7tFobdyQ8H7i2GKQM3Ztg0xksJSQ5-WhVi3t7hgXUImyTG34YRQ9gKuWX_cDbAEn50HszDenP-0ioOKYTlUBX99DEI8uxqfFSfaR9g1_uPZ51AphwCTIhWiSdkNcvaBvp4SlqhCNSE-bjSEC_tqMQnAMG3FFz3oClQU18boKKrH2GbXNaGR1AVQXATIpOmVQvsd7IiLEpBEdx99RZdtPEWSH2YAmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=VhpokVMbVZj3JkWwb25TTap6levwy1qnJ3I7IDyGM5TPYcKY6CJd4YNngyCG8m6t6DhQKooJlZjHBt2o_uiUGUp-oa1j3B6zTVLM-36SjsycpQgFrD5QzxK5LpgLyFfSDRt2cnxTVjmtFjMLJDbCHdyGXAqE5DD2c2e4bmEoVHjZv7fp9mA-1cfFNxlamdQYPLov89rnGpDzu-iFwr0F5ipSDIDHMn804tQPC2sTjd2DCog6HZPYdp9Rr8vIyKrDFjJ7Zq0nPt1ebZYSiO58HtLxvs2RJxQM5TH6hii0c7xI3igWYuck85WicbwO0NPRAPVggmPt7P68jOtOfhDd1r1srNYVeoCvoQCe0eYTl3fXQPWh9_yPZTAp-kOubFiyl1oxmUI4mBnEQUrmAJNLa1BC-v0JDDfFhiHrTjZ0m0G3MFtIaxQBvZeI8GARdX9xqlRCjjnJZnJSYAx8jsGucaIBiyA6nFs5dHeIzjegZarc8oUBfbClevkOxg0bmkJDkiN4fTzt5z7R1auiVJ_GzvA1BT_HVxibG62whKaTVvUQvt8cKIrN9suhcTTxpfiYYO4acJ_Dn8KAfE5XzjMn0i0gJY0jgOCb7aLr3RzIKuAszcR8laFXFVCgalOo9UETcdz0qwz4vX5lmt9CFyDnu-yuLFz7377A962yadlOLMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=VhpokVMbVZj3JkWwb25TTap6levwy1qnJ3I7IDyGM5TPYcKY6CJd4YNngyCG8m6t6DhQKooJlZjHBt2o_uiUGUp-oa1j3B6zTVLM-36SjsycpQgFrD5QzxK5LpgLyFfSDRt2cnxTVjmtFjMLJDbCHdyGXAqE5DD2c2e4bmEoVHjZv7fp9mA-1cfFNxlamdQYPLov89rnGpDzu-iFwr0F5ipSDIDHMn804tQPC2sTjd2DCog6HZPYdp9Rr8vIyKrDFjJ7Zq0nPt1ebZYSiO58HtLxvs2RJxQM5TH6hii0c7xI3igWYuck85WicbwO0NPRAPVggmPt7P68jOtOfhDd1r1srNYVeoCvoQCe0eYTl3fXQPWh9_yPZTAp-kOubFiyl1oxmUI4mBnEQUrmAJNLa1BC-v0JDDfFhiHrTjZ0m0G3MFtIaxQBvZeI8GARdX9xqlRCjjnJZnJSYAx8jsGucaIBiyA6nFs5dHeIzjegZarc8oUBfbClevkOxg0bmkJDkiN4fTzt5z7R1auiVJ_GzvA1BT_HVxibG62whKaTVvUQvt8cKIrN9suhcTTxpfiYYO4acJ_Dn8KAfE5XzjMn0i0gJY0jgOCb7aLr3RzIKuAszcR8laFXFVCgalOo9UETcdz0qwz4vX5lmt9CFyDnu-yuLFz7377A962yadlOLMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=hNcRE9QywIL9DX3C55FzzBQpHm0VWz__Ml5YLCpSOD9CV-2iuT63YpP1AhDLTzch_-V7mA8gOcCn9l-2VjaboblN76-_6bvwNBOF6bz-EDKBd2BhUoeBYg-DNmzRFbjRAX0nhSGnir9_j0OWz1AcSa8aZMMylJ7OnEiNWYMvUKY1XpW7_4U_EIFJlgIXBnG9SmRXldbgenCgr0gySOqwbbNJcqDe1mQz_QTFI_ycb7-p8L_bg0EUjRNH-49GhJTVBc8A559KfNrEdIVfR2H9jNL8VasJEyD-fVR_slAC_OSLGiZ_sqWdAcj0orP_XD_qoVtwIFh1jDYyWjSg10miag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=hNcRE9QywIL9DX3C55FzzBQpHm0VWz__Ml5YLCpSOD9CV-2iuT63YpP1AhDLTzch_-V7mA8gOcCn9l-2VjaboblN76-_6bvwNBOF6bz-EDKBd2BhUoeBYg-DNmzRFbjRAX0nhSGnir9_j0OWz1AcSa8aZMMylJ7OnEiNWYMvUKY1XpW7_4U_EIFJlgIXBnG9SmRXldbgenCgr0gySOqwbbNJcqDe1mQz_QTFI_ycb7-p8L_bg0EUjRNH-49GhJTVBc8A559KfNrEdIVfR2H9jNL8VasJEyD-fVR_slAC_OSLGiZ_sqWdAcj0orP_XD_qoVtwIFh1jDYyWjSg10miag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA1QV87gByRM_q3NrXMYrM9CT8qaCD_33fbDJOrDnBB3RyLAjAE44IUlZukLzq4IPUaDEyxWAvZj99KB8s0SarONyCqtQNjQ-wvgCoxQOG79zeutkrTCEn0OPlyEOHH-K54aT5ebCUWSAgbM0XI0vWwntJERIu15C1T4Lcoe2RA4aNKWZbE74wvQ3LHVvpm6zrAC8Wx0TnV2mVnpFW3zpVvQzuFbnYb-3xqEV28My8SmtAhVOY0RPvFMstBGM14PMhxUADfotGlVKM69WMAgaYApvt6zjji-YB7nz3GjD3BaP4IzmVnyymh_bUxJHwAGlAJlu2u8Kn0qrFQ_103HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=kdzlA_cyWaGzPDqLiU3gseGF27tsqyoqLtQfDwwpxqbRzMjrlnXvw8toL6re03kdq6pzXVAr9_wCGmJA4rs_FgccXhWYKm-atK6PbW4R8Tz0YsL0yHd56qUm696bf2eecgAytjV9n3fm2c7OKyJOi3Ux1G1EOJUteYcUeGO7xATsHD3WWcHRSvx0v60ZswH1ekVerL-AOHK7UEhSXJzFwEUVSMvnjJGrhea2sl0lJD8z1J0WlTuYSi7L7CB_L0m6sZWbY3nD3Yys4ByFVAz664jRdvdx4lRP_vsa87tbutkK2tpWaxTVObH2R5srmgG3t641P1i3cqbPsYit7_eFGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=kdzlA_cyWaGzPDqLiU3gseGF27tsqyoqLtQfDwwpxqbRzMjrlnXvw8toL6re03kdq6pzXVAr9_wCGmJA4rs_FgccXhWYKm-atK6PbW4R8Tz0YsL0yHd56qUm696bf2eecgAytjV9n3fm2c7OKyJOi3Ux1G1EOJUteYcUeGO7xATsHD3WWcHRSvx0v60ZswH1ekVerL-AOHK7UEhSXJzFwEUVSMvnjJGrhea2sl0lJD8z1J0WlTuYSi7L7CB_L0m6sZWbY3nD3Yys4ByFVAz664jRdvdx4lRP_vsa87tbutkK2tpWaxTVObH2R5srmgG3t641P1i3cqbPsYit7_eFGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-4crWtFwt-ELWp9dvoU0ICQHgFIZAPKQOUM_hLaP0o_QHM9e4ztIiL29_Ks2Dj7mq9VRc_x69rSCXKMnFLkE4xwX_qMxftPaWnlkp9ksMLLpMq8-qiQ--h0eQGl-4emD5RH4jYPYl_yXQuQOVVd6wBrO0v7YiBCxe2q19SfMNHGbM6-aKVwOOj6vVosZAWJpgGj8fyrUCssMpr7fq8vUHB-X-NYoMtICmJ3MFP3Osc6tz4gQqmLIQG8SNBEBRZufdMrry51ZVGtwysKLpZFdo9jNv01S-h_TNNTvYtz2cj2xXhy1QXxR8Nt5O-BBjIo1Bp0WJBJOpM0sZsyVwi9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcYFN_pmZgyTNFnsIXQYUsaP_zlOfZtC0jzfH0wg9T8mQSPm3K4O0aSZID1uwUaGVQNVNg2We9nsMz18uLfGB6RNg1Ox4Ip0-JNEP2exrG3ZOV3apL1J2jXaMqeTEUIGgiV48UqpWEZfkplPWaTW7oG-Ckaa53RQfsUVVbYc8w3nlD1p5ksX4Y4J4Aqc-jX9HRZdqE8LD9wCBssWNJqJ1jDwW1LaSA8FvXoICyjMAGiXcql2DqTOnUFGl0XMb0JmjZeIVlbsuQ6qWC-EZ7CvmLgYhfJ-9Ioag41eC5u00nDWI5rjtnG8Tjkv7kZ4tsXKPSkIwb3oFhiY2FY4VgYb8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k98a3wLGgKNQkRgGCm1eCK_ALZhKrAKu-G9nzrPaUaZh4dcpZTU1f9EiBJy82sTAgCXumGLUbu4FscVnBPs7C_jYtdxL9O-9fkw8GH2MDzSxZWvFXvznLIqvtTZnBwJmDJsdfwTWgOc5EumoFCNViCzMOVmJ3R46kFCKCIc4TclxMmmog8PqNZ11Ix_AvYuVoJmoHAueTQ4JajDMaxlCMAtqn6iE2M6CpTHBqXI85F7cYTsfHzngScXtuMr_DcqGVTfspmfvomt-MaX4t-52kouZmdnSgoenODVpQkb7-zwlTPYjEG5pHddnASt4ISKWDTlf8Zu5UmZBL0701PK8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmO3VVU36CEkRUmPp-Z9svZ8l1KmCcqSuIzT-yrSn3UJO6gcBZivncM78A1uiw9j7kSEUif7edrGcZWEUNA8keh0CZzcUJX0Cl3JaQHLymhBm7FVWPl0REQXMDJoOqqhPCJYChr0i_IbheuzZett1iiY3ENAz5ViO18l_JfukM8JDdqqNhm7AHJEuSV_q_jTgZZnbryW6LTGtGbPjxz3C7v0o3v5vqFA0HifGvAGyzHKLJ23am6Gu4tBTg12mXKQluTd3KU2f4n42G-J5KN2kMzF7mhXS1EIQnHNAYoBQ_6fMK_Gg5fSJzx7oeoOsxEtCyprXUOJxXoLRHSOP8ZAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee41bfpTRx6xeZDUb_5JtdkG-0rcidnmx9KENkcxCNL-9PNkJCVRKbsErjZN5QQB-7Bv_jgrfQjN_8yoHSMsVmmaxxGvJLCN6fZ0WmyWWYzd9PkR1unWVjlXKJwlVmcMioZZab8cNDBG08lulMC2SuvgM5Mpx77fYMHu6wv1hd6N2yGOGsDn3EtTXO_-MIQv8N004SFOxJrLH_Ak1wa9fEyhKkgfam_wj98ShvDjwVjQpzdlhSFe0ZcTz4fBLH1EuaCtoR1jOAK0ilvxYes0Ld2suHnJBqwdB91skb4lgl5nqS1eR4GZlSrpAnt3HKefKBwntbmxPldZPlmYHkM1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Er2d6obTVj3KtkdYhx-C7x1wL-xtNn0S5mysWvxm9E21Slj5SxRcNdk69V2CAqlq3-dMwIunpTI4yuyKrmyPDZPPBSOYQJkm9mru4hzj8DdxG0l-bOIY_jwaPrfQoFsOAnjqSI9WcAVTTIaCRCVBiVHI3JcZ92Py7MH1WWXxsmEnaJ0XA4nBa08oMbij_Hd5v2NK3OFwoHIvLI1TqloaweUFY0iB_g8yjpDX_HEuQ7cB1oV3tlwd7_LauEEat42rW8qaExvTz17o0qCs70BZKNj-paZP_y4kw6xHiVZCWeivMN1dNWWTgOw4hbuBYER0IjVHIG-iqoddoWzdD19TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Er2d6obTVj3KtkdYhx-C7x1wL-xtNn0S5mysWvxm9E21Slj5SxRcNdk69V2CAqlq3-dMwIunpTI4yuyKrmyPDZPPBSOYQJkm9mru4hzj8DdxG0l-bOIY_jwaPrfQoFsOAnjqSI9WcAVTTIaCRCVBiVHI3JcZ92Py7MH1WWXxsmEnaJ0XA4nBa08oMbij_Hd5v2NK3OFwoHIvLI1TqloaweUFY0iB_g8yjpDX_HEuQ7cB1oV3tlwd7_LauEEat42rW8qaExvTz17o0qCs70BZKNj-paZP_y4kw6xHiVZCWeivMN1dNWWTgOw4hbuBYER0IjVHIG-iqoddoWzdD19TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhCuAVvLVP9r0l5Tupcm86gwZ14n04jx9g_-ejRzbcZ0uxVpIe6idulVEviMq2mGS6TAtiFFptZOmEk3v7pWEeT10WJ0GTJJ_MFwfEwySzotOP8aPGV5gzQpuFpdS_jk730m56sBuKIM9GMRnsLyyHPPHi74pFLmoj3v4vjZlLnmByGNVcc05IsOeUn2jHwV5-ceK_7KvSgM6UXtGKwI4s_6QpeAcNGVUxQd5rcdq0lIjdN0vqZpS_POWoEpZTT7ibRayTL9I19D2o9b_aGPQiiQPs3qpTuI_XcvSSgZ8cwKQ8ZClcpoFtPeZnhlYP14mlll1tnJir77E1fAPygzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deqbGmX5SiJuGdTB1gF1nWmPj-5aT8EENnM_uZlAvwTirl0sfs6cEkJKd_uirRE9jtv9VXn7sn7AymwxW1wT1Z3RhbYfp6qKQP8YJMpOa7PoPCFH0kiSp_tHpTgQqC_PFrEGvfYIR9WjfT3Ybq-PmY6LccffUCd03kAEn-I_Nq98UXOZsMr5096UuZaxAzhCWQMWPnIg9sA-J5slbK2GzCWq3MtoqJm6xKJMZEiQ7NdsqZtW5BfSAvVlscchlGLkjdxczf_3mBhkwd8CdiNMPzpGQuimZzpiNVqhcE1BXpydtI8UA_Do3afwvSbf9kBa9WWxED3tVMGRZ17HV-FPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=t7VbH2dVtAQ4txLY072EDx0Bo1Jh7zmA7CHLAdFRYhqSxgZ-e8QGMGvPDGxrDJluZyEqkGhu5M_--3h-Onhfu9tV-PFFQlW_kuZZ81OdvfDsH78N_jKWBpmfEJ_EvQfUi9pvzHHOJoatlLy-v7LUGcmvmcxebhIfer_iIg9UZiL_8dzU0QtbpcNcbMaGtsIjv7w5Omm3kjH7knRX9-_2zr1M3qGNA8jUxJKOOLERCTsYaj8-EIXe73PAmJLaQmUcJU321AQJ1SJzWDwnd2DOSwByIF3OSxPlFKZhNuJRZOAxHE6zQjGU9r2Ox-5M7Z9MuRLk185YFKPcde26Fz9u2jRPh2MqMS6QHBNBD0J-_FiHMv0KEEXb0Aj5WtY-x_Sf0pb_3qXq9AykP4Jx7PhG-BfXWFuXyvkC-LB0t9ClTmgEOw0oSOeNg7WpwbowRt9hKX07MmftlQo_1nW3tWZwg2lRC2XossOUCzKOG2FLb2uCxqnUNJkCyNjQ2Omn9PcTUZWAe-RRpGa-aBwmA9TefY8ILtdOHLiLKyoJE7kH1wkrIyjOjkxVLxmqpflJjwHxGcruwVP1u36ciknjgjapUR8PjN0Em7VHKa-_7gxuaImukFXUqAE6PqbNorQS1ve3vAF-m_bZxPfOF9blFquj2uuQHObDgD9AoeZv9R8KNGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=t7VbH2dVtAQ4txLY072EDx0Bo1Jh7zmA7CHLAdFRYhqSxgZ-e8QGMGvPDGxrDJluZyEqkGhu5M_--3h-Onhfu9tV-PFFQlW_kuZZ81OdvfDsH78N_jKWBpmfEJ_EvQfUi9pvzHHOJoatlLy-v7LUGcmvmcxebhIfer_iIg9UZiL_8dzU0QtbpcNcbMaGtsIjv7w5Omm3kjH7knRX9-_2zr1M3qGNA8jUxJKOOLERCTsYaj8-EIXe73PAmJLaQmUcJU321AQJ1SJzWDwnd2DOSwByIF3OSxPlFKZhNuJRZOAxHE6zQjGU9r2Ox-5M7Z9MuRLk185YFKPcde26Fz9u2jRPh2MqMS6QHBNBD0J-_FiHMv0KEEXb0Aj5WtY-x_Sf0pb_3qXq9AykP4Jx7PhG-BfXWFuXyvkC-LB0t9ClTmgEOw0oSOeNg7WpwbowRt9hKX07MmftlQo_1nW3tWZwg2lRC2XossOUCzKOG2FLb2uCxqnUNJkCyNjQ2Omn9PcTUZWAe-RRpGa-aBwmA9TefY8ILtdOHLiLKyoJE7kH1wkrIyjOjkxVLxmqpflJjwHxGcruwVP1u36ciknjgjapUR8PjN0Em7VHKa-_7gxuaImukFXUqAE6PqbNorQS1ve3vAF-m_bZxPfOF9blFquj2uuQHObDgD9AoeZv9R8KNGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=VF525fHieESn_nQjekXC7ubYJnM-KiQhMiMmAMKgwOSHONFXUFOyrwSCfrvFWFLb9JlPygeuTXZAfH5ObE8ILxZNJmE4iLGKiGUZkn44zGYI2yeWOZyXXGcfp-De2o0w4vT2PPXdqRy6D1nG-yoEMX8BKHr1qdawGTDsHLVzByzfeqGO173EZnvf3nX8dx06f8qa21iu3aRcXWmDEw_x5LfJVIMqQEtMlxptLE1G7sOZTraS96qGd4D5km5McXNHQGHAkvZXREPhEukaJG16oE98vu5q76wgmq5L6HjmJPP7EIW1VrhOglVwRSqlouRMvMY3CA-8ORXqtTnRmYyoFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=VF525fHieESn_nQjekXC7ubYJnM-KiQhMiMmAMKgwOSHONFXUFOyrwSCfrvFWFLb9JlPygeuTXZAfH5ObE8ILxZNJmE4iLGKiGUZkn44zGYI2yeWOZyXXGcfp-De2o0w4vT2PPXdqRy6D1nG-yoEMX8BKHr1qdawGTDsHLVzByzfeqGO173EZnvf3nX8dx06f8qa21iu3aRcXWmDEw_x5LfJVIMqQEtMlxptLE1G7sOZTraS96qGd4D5km5McXNHQGHAkvZXREPhEukaJG16oE98vu5q76wgmq5L6HjmJPP7EIW1VrhOglVwRSqlouRMvMY3CA-8ORXqtTnRmYyoFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIgsmHK_fqaok_1L1P_jPkiDI-FV5V-DJNngTG7UjyL9a7ARZaIq_tbUbofyef9bloTCEGQ2JigsedoK-cvKbn2QpPOXTltMr6aaHjn0y9g76t33lX3FPCvxJ72ayMdYCamsu2CYT2BwckB0_ve0KiSBknPwVx3IPauGQbfBwlngGlyrzlsxe3PPYJJLb5W33gu4dvE-sFUlykhCK7mSX_SUovEWwpIrgB-zx0SQPHK32tAxpyRbhD9eW4A5poL0JpZB2ql1cymZziG-n2PRjOge9Maizwa7795gXXMcA4-IjFzSH5uPCc0PqhDHnMWReeUP_nQ16lxTRYygVvD2UjEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIgsmHK_fqaok_1L1P_jPkiDI-FV5V-DJNngTG7UjyL9a7ARZaIq_tbUbofyef9bloTCEGQ2JigsedoK-cvKbn2QpPOXTltMr6aaHjn0y9g76t33lX3FPCvxJ72ayMdYCamsu2CYT2BwckB0_ve0KiSBknPwVx3IPauGQbfBwlngGlyrzlsxe3PPYJJLb5W33gu4dvE-sFUlykhCK7mSX_SUovEWwpIrgB-zx0SQPHK32tAxpyRbhD9eW4A5poL0JpZB2ql1cymZziG-n2PRjOge9Maizwa7795gXXMcA4-IjFzSH5uPCc0PqhDHnMWReeUP_nQ16lxTRYygVvD2UjEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBeq0YDPdVL4hKCDPTZzH9G-IF93wtvydXv0zbMxbo0oQyk82sIofDpdvjgZ3rCpSkEzTQyT5tJaCFYSd-y4DUCeTjFWX7oXZLNxEtBk7pCs15oxOLgpnrgey2soBOvjYfs8JqGA74jAAORmMpHUzB4ZZyPmk55whMz4V0QJCLR10Tu36dZooenyalvGl_VDdhN5tQWJImyjo6-OKQj5gtK2ORRWjU6Ol56qhOVHr90urKVRKW-qVcAI01hY1R8UWncYj8JiXI791Nra2_ghfhzsY4ybQAb4ENy61Y2Je-uJknavqtxmwcB4vb_rlGvwD3602m6kMRGWjhBADXoxnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGCyShpd8v_mWUMC3y-4KuGoNp7CHeKcgrweuxVVMl6hSjAoReLOz9DU9KkHQSo7NGmf-ljv6hBadOp6TzsHfIJ7ooiBMXbpZFFscRLPs8htcivug-iYNFoRtF7tsg6yBDjzEM1N-jqa9Euqe_oj3xIdYpDfs58zHho5fIAOLknN_lmlnIxmn6nlLZd0qVEM8uSfsCW9N-0cPSsjy3u_U-ou17HMUTXpeOy1xehj51BERTJfyAAF3Ft1kRR4POZk-kiKsyE41i2BQY23XCDvLJAPMdmSeP315GizaUCcMvBagNWXWs9QlbpeTipdr0LjfzRW8iRbah1EwZ_Cutw4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uswx0CLdXd1XqyzyQsOXt7nNqqkj108-bEPxlJb4XPz7ZjWSXhQMQAlAEr9d2eXbcwlQQLQ6mjA1NpE_47X4nmqKPaRhgArA6DvrmxTlwLMVeuF1XXVpAbkC4kYWFlSqCKFodbJII5o0gJqQeejHyB76n52rXmgGyR-vxfNE2Ix9dv9g0Rx-t11dT7YokvWVvwrKJeoQZQFZpKeni7wGHyRNjMD15ye6Kr8RwXt9houE0CzQFDfT06_v66iWgo_GHjDgydlDpanIQb1RjogtOeZ1LS81r8zu_Ts-I_-oHg93iNHCfsACGV7zdMoWDCVAwd6qD7zvfsrrOqaJzkBlUg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=T_UC2cD-hj12rnGK11qcT2cK4FdTlC2r-hwLmgdgiFN7lfjgT-67joDc39iqWaUYh8CHGXHppGXBxl_2Po1DQ9JYw7_URJJLIu_cxvezpOHEZVURyAmKhB_mRE2gP7_2krUXr2fXA6WE81P6_rhOlJ70vgIyrRfMBEJfWMVxKx3WLvockLykEQPEcCwRZSrRfeOLX9hxRlcERZ7LYeXYSL26E4CR6Vw9aq_smE07mJnQuBs-xJpY3YIzXIDlNXEA9b2qp9TS4fajVz_VS-Kt4RebOjtCThBf1Gpi9hX5lSVqphaq-ycnBMV71Mto3Dweko-RPgs0f4875FiGIvhp7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=T_UC2cD-hj12rnGK11qcT2cK4FdTlC2r-hwLmgdgiFN7lfjgT-67joDc39iqWaUYh8CHGXHppGXBxl_2Po1DQ9JYw7_URJJLIu_cxvezpOHEZVURyAmKhB_mRE2gP7_2krUXr2fXA6WE81P6_rhOlJ70vgIyrRfMBEJfWMVxKx3WLvockLykEQPEcCwRZSrRfeOLX9hxRlcERZ7LYeXYSL26E4CR6Vw9aq_smE07mJnQuBs-xJpY3YIzXIDlNXEA9b2qp9TS4fajVz_VS-Kt4RebOjtCThBf1Gpi9hX5lSVqphaq-ycnBMV71Mto3Dweko-RPgs0f4875FiGIvhp7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBRGdhg4awbVHQHGxKA3fRmUsTxIB0Yyf773XL2GnKXsxSizL1XCgEdB-_UjoRNhrjB15L4OXy9JlxuyJ9S0AUeisvDo4wZw9VVaRq4GxfMC_Bj-jk2k6wg1bGyvBK19oDhcgJ6L5NpX99b7FnOyvdzLsfyKO4ntN5yeAweCdO0HX7h7c9PFII0TH6yVGhlweAntM3cQ5c4E1xulfADFzgcyY8TFDvFq8PCSLNjPZ8S8zVA8fMzWcd3laz6NviVektjRj5NmEyM0_II_jth7-CpaAYJiGqKFwbuc_r-90y1UW7zSRNb4IlnI_8GUAc_UF2hC8xCADiVAaLQs77x3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvLLI5xVYUqdE6AhEtLo5dd-6wnZy4jg82wapWOSl4iil-fct5MA6RdbBf01EsCQ1asVjYEEyax6rrwPUZSsPLMwgJT09xqQejWhP_Z3glvOS_eMNlp4Iig-FK1qPY9E8mRgZ5iHIcPeJhq1rUQjILRQrJmbIuPIIzQCjk_cW7qAyohaeeJwvLIcbY8GpcfSzwzkX1UlgC7LHK29KmjzEFSBsKGDvtTyXJLEDgpQcEwAtjuvteztrBZllKkQvOtfDbBeIIJnBWyOYmF3GvPVf8JEsD9wnwkjQIxo-hcKdny-AxZopp1tLXgbJDqnAaemtEzy89uj0Md6dE8pDPgTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTVfYjgadFI7jWTVFITXZfcAEFGRWYvi4F4KzC0MK6rXRBY8MYGbaTK1u65DEtoKCtNPXFeaYWxsu3mi7ZdUi6x66kVFM1djVheUIxqsg2qVj2qNnzOC8R7OJB8_qrM0Miz7I9vfrrVWeAA0AtaxDmi3dUYuC6L9OOQGmmRNI32GoO6K_jxbiISy9o7vefPELtHkvE0pO4JQ50X2go16K3FtTYwglMy3HmM4ahW1DRlDe8HjPV7gAZCitFx_S54etdNArl4_P1-cw-O2QpjlcwF6Hj3bkXwtZKiFb_2gQEXKSfd4XCTYuozDFvJb0Z8giEfgvEtqpVp0jvv6OI8CqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXqD3t2dxbDfIP-Q_jVKmbloIj5SUjpgVwf2zQr_G7q2L0xvCjDgbyWihiZiWKNX4ipelOyvE0LuxEwgbByezam1BKVleeuxAjBvRovOrfiU-t9a41OTlzMOUTbGvlZoCAqMnHBpRby7xGWCHPXJdAalsp8ReRilUrbITDSVZOpyGXzlskEvuMzwQYv-RFnwYBaJRKdhhEgcXfrYV8DCtulWZ8dtDzt_3iDrJTifNnLHf6-c_2y61Hjgq_mIRAx404-l9VlNJXpoUWS0eh5GhB9hP9k_NtGsES_58ozU33Z8fSY1tuwc-9WaJ-dbnGIg7BhUDC6uo2rqgVL2kA7BMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cabPBCbE4fFnI9UjKmtmvd6vvLhFtZwj6Y4xoKcLzR1Wzu_IjnHxuqE88L3qSHBOIS_ve2Bahnq6b5sl6qLeeagT5KbPe70Hdngjp2x6Welb_Cnoh5i9YOa2oyT-fHnBqfVteVfumKUmCJ675n57wl9GgCDDKMlTgpdeLesaFlZJmT0y5qqa8hV8J9xEQHgtJZ5_9OCv5OUnz36uMJMg0hhY7UijfSNyEF8kJ_EgJQFWXSowhGpx7NLhodQ8l7E_zclQn3rh8HooryvLwy-KBLllMMsrAPMQnpMzTquiKcL9A4Z87DNbPAn5wsNwF-wEGtr-G14408UlQ8WUAblNjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cabPBCbE4fFnI9UjKmtmvd6vvLhFtZwj6Y4xoKcLzR1Wzu_IjnHxuqE88L3qSHBOIS_ve2Bahnq6b5sl6qLeeagT5KbPe70Hdngjp2x6Welb_Cnoh5i9YOa2oyT-fHnBqfVteVfumKUmCJ675n57wl9GgCDDKMlTgpdeLesaFlZJmT0y5qqa8hV8J9xEQHgtJZ5_9OCv5OUnz36uMJMg0hhY7UijfSNyEF8kJ_EgJQFWXSowhGpx7NLhodQ8l7E_zclQn3rh8HooryvLwy-KBLllMMsrAPMQnpMzTquiKcL9A4Z87DNbPAn5wsNwF-wEGtr-G14408UlQ8WUAblNjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=U_BJMkl3YqKH1IUEUjY2ZqdrOQSP0nGeQJ-BD05NkIgok4hferenNPFon_jGe6xWuLAbLe6BzlU2V02fJuoIJF9mk_ObqIlk460Uha5RDgvxwCxU0iu1Mejo8zfEE3nocn5bNzQpjmxoavmTqvis1piQPmvR11Z22FMurtV1yQcbGJJuzhlxMvxdEvK0p3cLjiF8SWRMf0L3y6pxR9UElVolQHTmjtvGw0cRbFtcIgddZ2b_DVIuBwL66JcoYTtFjcgSig2DPf5gFLHKuLEfAx3ls3TIDw9y8Tixlzpy2tKNSIWCjDLsPeFSh1d-HLuisVTAyrEJWKbFawvrIS6S8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=U_BJMkl3YqKH1IUEUjY2ZqdrOQSP0nGeQJ-BD05NkIgok4hferenNPFon_jGe6xWuLAbLe6BzlU2V02fJuoIJF9mk_ObqIlk460Uha5RDgvxwCxU0iu1Mejo8zfEE3nocn5bNzQpjmxoavmTqvis1piQPmvR11Z22FMurtV1yQcbGJJuzhlxMvxdEvK0p3cLjiF8SWRMf0L3y6pxR9UElVolQHTmjtvGw0cRbFtcIgddZ2b_DVIuBwL66JcoYTtFjcgSig2DPf5gFLHKuLEfAx3ls3TIDw9y8Tixlzpy2tKNSIWCjDLsPeFSh1d-HLuisVTAyrEJWKbFawvrIS6S8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pztRSlHu66QKpllDsK_jxjH-zUxEN_9jo8ejFEMb8D3b6e1K8nH9PF_KGtnQ7PCBuZdy3gyclBo1xzpC465MCzYhbcKqStrv0ixsU-vH_pHgebzgpfIiMrSTF7YIT2EpOOQFUetH-51tgp2LVrWYdCm4osvang7SC1mKxKwelPS_bAdokQUpo9C3YHKQy-0ECbm8CMRRuP--K9X_BoBh_RNQMNYgBUM5cotPiTkIyWbZhJgRuoTNvCNm5_O3iRvmGgv-sPmR3vTI0FixXXpxzwqA_y9Lq-PYbJbIRDwBlEUrzG--ttlY3iTy4qw0SSUpBeLOuQkijbV8gV_XhDIYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pztRSlHu66QKpllDsK_jxjH-zUxEN_9jo8ejFEMb8D3b6e1K8nH9PF_KGtnQ7PCBuZdy3gyclBo1xzpC465MCzYhbcKqStrv0ixsU-vH_pHgebzgpfIiMrSTF7YIT2EpOOQFUetH-51tgp2LVrWYdCm4osvang7SC1mKxKwelPS_bAdokQUpo9C3YHKQy-0ECbm8CMRRuP--K9X_BoBh_RNQMNYgBUM5cotPiTkIyWbZhJgRuoTNvCNm5_O3iRvmGgv-sPmR3vTI0FixXXpxzwqA_y9Lq-PYbJbIRDwBlEUrzG--ttlY3iTy4qw0SSUpBeLOuQkijbV8gV_XhDIYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USSgMRqgD_FGEuI78UYoX_iUOYl39q1vSQh2xsHDYmPkbhK5zs-yVaurX1fvdlJqPuQ4PcCCL1TCQukf0hOae24aybY_Wtz1rucfNefPPYSAHT53hVbxcHhd7IR9rAc-cTg6QBhkZtYavqDLpoxwu8Ht-oi9x9Sx_YmFJPWT4i_sOo-cWvZSigXMKRkd3VLBhUwI4G-Tqr2CjwGc5mqY0ZSpzmv5TiyjVgVpYYYIliLuOqeNRaBISN28lTVLGl2fVD-Hy0_piz3ablwbBLRIMHPQSxqPYuKCQmE_FHcZoZ1X-m5OESgIlhjaqD9-lfb1kKtU1rKmbIgaXQLzYZdjVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=XDpzxzo3hwedTIWqshg-a8s0KzvRTk3izabxTWRbhd12pj5l8PzOxNflM_DCowExgALouo1BQEwClV6yIqEPB6JkLGYQLDk9MQ21fWA4ll7UnocHlHk9_4_9YoTMtBT58dqf3wViWK8X8P8ke2gTxVlG83W0lt8_U3EiGACgdxDX98Y3YkCH3r727qTGBJdh5gYFW1v1Bf2OC-h1gSAVspz0i4hK3J5MopfUTs0q1J60o0Kie_fKdb2fSdr_z-NudL3aHEZMEo2z49l1iIOwfcvDCHZi7pgHrPstv7kcWLClhRoWlz_UjiSbaqphoGcF-W-QwDAgLVC29ZHGmhgefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=XDpzxzo3hwedTIWqshg-a8s0KzvRTk3izabxTWRbhd12pj5l8PzOxNflM_DCowExgALouo1BQEwClV6yIqEPB6JkLGYQLDk9MQ21fWA4ll7UnocHlHk9_4_9YoTMtBT58dqf3wViWK8X8P8ke2gTxVlG83W0lt8_U3EiGACgdxDX98Y3YkCH3r727qTGBJdh5gYFW1v1Bf2OC-h1gSAVspz0i4hK3J5MopfUTs0q1J60o0Kie_fKdb2fSdr_z-NudL3aHEZMEo2z49l1iIOwfcvDCHZi7pgHrPstv7kcWLClhRoWlz_UjiSbaqphoGcF-W-QwDAgLVC29ZHGmhgefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=mTFonIBDkDiXPokZISBjrQQX0CzEhfvvrXEqKj6XQo7e--VgBjVQaklRk5DXIzPCcuSc0PTlul5hKxP__uHnOudZZYJrx1kwYUfCAycKQYzZzM0JtA4JltY1XBXRFAaPQHmn-Vgr_o2LpKU45DEL2bCLFb3jjNLXlK9qgAr4N_0xLwnXmoGPPGt7Iv5cBHPp2i24xkGY3WYExtMX4nhw1-1ssy8X0x6xeIS8VRzbARxTr7-P3G1otR0yPAeWWLerbaOV4edBchzk7VJqCqa0nyB8-Ad0iJjEuyfRfq3KAA2IbUd-43N-U-x9r6OpUcodP9QD6OO1b7gCNLWOQO_fUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=mTFonIBDkDiXPokZISBjrQQX0CzEhfvvrXEqKj6XQo7e--VgBjVQaklRk5DXIzPCcuSc0PTlul5hKxP__uHnOudZZYJrx1kwYUfCAycKQYzZzM0JtA4JltY1XBXRFAaPQHmn-Vgr_o2LpKU45DEL2bCLFb3jjNLXlK9qgAr4N_0xLwnXmoGPPGt7Iv5cBHPp2i24xkGY3WYExtMX4nhw1-1ssy8X0x6xeIS8VRzbARxTr7-P3G1otR0yPAeWWLerbaOV4edBchzk7VJqCqa0nyB8-Ad0iJjEuyfRfq3KAA2IbUd-43N-U-x9r6OpUcodP9QD6OO1b7gCNLWOQO_fUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=FYfG8WwNBBdCptdi_gWaeKzK8-g58LOHiucNUErCuNjOXTt4q3Er-TFZd1iiaUlHMRpNJuexpGa4L0NAkMKzAr_IWlCY1pNRNWXYt4J41rpQdy0K9E-DcL-sPnI-dpLKWbyJAzy4xo1iF-2IsSV-AsBL69PypwyAlRzrQY4A1qAgtS1klHn0n9_3Xi-gxf8QqTabjc3_gZ06RaKdVqaDvXUm3UhYCQ3rTTgs_z8gJOcyMhN8zyEo8y4LMlAw8kNP0wkGhj6vtld29y46ueg3y3NNJTxqKL1uDH2t-DwwQw6JfArRd529aHtYw7VQKLEjlD1vk-lL9vj4xtC7hn48yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=FYfG8WwNBBdCptdi_gWaeKzK8-g58LOHiucNUErCuNjOXTt4q3Er-TFZd1iiaUlHMRpNJuexpGa4L0NAkMKzAr_IWlCY1pNRNWXYt4J41rpQdy0K9E-DcL-sPnI-dpLKWbyJAzy4xo1iF-2IsSV-AsBL69PypwyAlRzrQY4A1qAgtS1klHn0n9_3Xi-gxf8QqTabjc3_gZ06RaKdVqaDvXUm3UhYCQ3rTTgs_z8gJOcyMhN8zyEo8y4LMlAw8kNP0wkGhj6vtld29y46ueg3y3NNJTxqKL1uDH2t-DwwQw6JfArRd529aHtYw7VQKLEjlD1vk-lL9vj4xtC7hn48yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Rv04Pri02Hcv76vkq5lGOruJpxgbOJoAfv91KuSQsc7Z11R6jJVouaW5O8LSWbfGDW3L9GD5x6lmH68ekxUQ1Ha3_zbpuqSmo5bZbyb2anBnlUKJhGRE3LDxNg76ClZwsd93BpGboHuM3oIhY8U5j2QpDa4hspMXaAHNRd8iiYCY-QfPNEKDWVDVk2jZlA__VYp1o7uXaPlEs9fBz8B5VLs9PJ5ea4DOblSQRbKBaCcvNBZA00K6kibyiCBT7cCsykBLUKx8BV_Fk5wkFAMW_XRe9nCxAy1Yvs-c-xcHJqBOWvreHoMfeJp16tAurqhVB0eUz7dvf9MC73zYCGxvSSSsORNCV1J2QsvcuQ3wbbEcPhrs4h3PugGv8rzTQzSAfRomyEnc_NWnYAF20pcg1GW8mdGXjX9qJEoc3MQMlHZ-NuL5Fsu8yVfGUhevFp8eiku_ph_ejGQwA2-BfwcpjefEsWGFjdjDgXXc_owkXlNrKAHS9PYGeS1PzgIfr9UzDw9AqNlvl5JhinCWyRcnYpp5dI7yOZeEZ9GvXGy8aHSljd8uNuvShpiXc1zQubv_C0PlTg1UcwOmXc32JpXmvriBWqFU8yE2Wy4kgnzvth4zcCkvyBcoHa6VhiD7xO3Wr_hzXgifNqsODhhelDjuTTBNxAYVXfm49hOcMs7Sl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Rv04Pri02Hcv76vkq5lGOruJpxgbOJoAfv91KuSQsc7Z11R6jJVouaW5O8LSWbfGDW3L9GD5x6lmH68ekxUQ1Ha3_zbpuqSmo5bZbyb2anBnlUKJhGRE3LDxNg76ClZwsd93BpGboHuM3oIhY8U5j2QpDa4hspMXaAHNRd8iiYCY-QfPNEKDWVDVk2jZlA__VYp1o7uXaPlEs9fBz8B5VLs9PJ5ea4DOblSQRbKBaCcvNBZA00K6kibyiCBT7cCsykBLUKx8BV_Fk5wkFAMW_XRe9nCxAy1Yvs-c-xcHJqBOWvreHoMfeJp16tAurqhVB0eUz7dvf9MC73zYCGxvSSSsORNCV1J2QsvcuQ3wbbEcPhrs4h3PugGv8rzTQzSAfRomyEnc_NWnYAF20pcg1GW8mdGXjX9qJEoc3MQMlHZ-NuL5Fsu8yVfGUhevFp8eiku_ph_ejGQwA2-BfwcpjefEsWGFjdjDgXXc_owkXlNrKAHS9PYGeS1PzgIfr9UzDw9AqNlvl5JhinCWyRcnYpp5dI7yOZeEZ9GvXGy8aHSljd8uNuvShpiXc1zQubv_C0PlTg1UcwOmXc32JpXmvriBWqFU8yE2Wy4kgnzvth4zcCkvyBcoHa6VhiD7xO3Wr_hzXgifNqsODhhelDjuTTBNxAYVXfm49hOcMs7Sl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=ADZh9fvzFsde3ora8R1HVE4acTVFVAgBWR7ywhFptbwKJjWO19tyMosOTMc-Wp86hyFknSdGBslqyplV_lfQGmbzoNRvLiSOMhg0luccE34lcbymwkPqTwk1DkX8pLBMhBv6Of5CxOe1vSeEo6f5VkVaDv6d5VIyYBw0p_QdDXPu7lNqjgxIDwdqW-777eZKXTVJ0eR68VNdNAel1B7XgzrBS3V2VzJFCxzV2gYJnVL7Qgl6tgTvuY6UWUg11OiTNVwQm-3Kqjw264MMqSYmQ5SV_LybAKJAS6y9Gn--yPYdMu-Y8H7lSeoFCY7LmIxtqTVrRDwNzBWtEwI-3DVtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=ADZh9fvzFsde3ora8R1HVE4acTVFVAgBWR7ywhFptbwKJjWO19tyMosOTMc-Wp86hyFknSdGBslqyplV_lfQGmbzoNRvLiSOMhg0luccE34lcbymwkPqTwk1DkX8pLBMhBv6Of5CxOe1vSeEo6f5VkVaDv6d5VIyYBw0p_QdDXPu7lNqjgxIDwdqW-777eZKXTVJ0eR68VNdNAel1B7XgzrBS3V2VzJFCxzV2gYJnVL7Qgl6tgTvuY6UWUg11OiTNVwQm-3Kqjw264MMqSYmQ5SV_LybAKJAS6y9Gn--yPYdMu-Y8H7lSeoFCY7LmIxtqTVrRDwNzBWtEwI-3DVtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=FMb-wPq3B9nBpmjQFzgh_7UttRocV3uIVo4EOSC3SSjf49d4Et7mPkeZwZeWiqnnjMlrhC5YUjVI9QpryAVhOuHC-WBohYhdoKtHFHW4HKxgNc8pni0b9C9kjD68D7d1-bm4BTmaDAxYWJFp2NENBr3EQVinVxEOYFd4xNMFSgYqlxlrwaxI-o5pNSfyn8v44jBCpm19VGY90MGDXb2ysFCDPqPwlcZN0D16pBlJtCsMkRJJWz10lHlHeKIHU8VNwp8GnB1BFohFIpRIZreXhx8zTf-7uytj0DE7ERBJZs3ZJNLldgb6e2YL13LHYBl7sOtJ52LJODUycY15S04yew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=FMb-wPq3B9nBpmjQFzgh_7UttRocV3uIVo4EOSC3SSjf49d4Et7mPkeZwZeWiqnnjMlrhC5YUjVI9QpryAVhOuHC-WBohYhdoKtHFHW4HKxgNc8pni0b9C9kjD68D7d1-bm4BTmaDAxYWJFp2NENBr3EQVinVxEOYFd4xNMFSgYqlxlrwaxI-o5pNSfyn8v44jBCpm19VGY90MGDXb2ysFCDPqPwlcZN0D16pBlJtCsMkRJJWz10lHlHeKIHU8VNwp8GnB1BFohFIpRIZreXhx8zTf-7uytj0DE7ERBJZs3ZJNLldgb6e2YL13LHYBl7sOtJ52LJODUycY15S04yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqkfHVxhcrwCrfFuusncEZTTbU5sj70ppaDA7wL58rPtPBIQDpbbncHC7SyQ78Nr-RG5Vv8Fy9F4xaqyllyj53SE64yYY8yilOa2kisW0YobtqNhuMSqRyNe4CGcx_W2SeqAiqnbOJPvgkV3gS56llSAr6UxTIRw-cxyA4v0giqB1qtk8r_GXscOVQsVqcCKquh9YVYWKHU9m7rOG9xy79xpPpsTSpTOJHRrMElMjbIlM-HQFIZcoyyo1tGBK80qgwoA0aaoj__LdOlHj9khLzvZbqBAEHs-3Vv8b4D6VhN7D0W8Ualj7qc3E6R416xQ8GdNB27bR45JPNIOdztglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv_XWEjRglmRQICClA_DmQETBSCjNVPkp4vTWJbatGztUgLxB08yX_YsMWDtkNtlNosUERim8LAihybeyAR3DagC1u8iK1StyTgqPIhcgEzQPD1USzO7xNYpuHx_k7dys2NjSxGCtKHT10FfCDt3y9ahm4ucNbWp21ScrxaUviceWHCpnsn3aZq2iJHBGwY85BrvYKW1YVlMRnCP0N77cvo7U2gy7g107q9QdQULPBdtqVYDEKi8JBwSfTvg2KDAC8v23VoP18k9wQDTLfQRTcri93EzaHb3hzmBWa-QbNmPz3mOJyy3xxZB74sEAnjsQ_b6PMz-tDs19nygcTgufQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=KadFLNdhYcgqToVgvQdCmUaGnF32nHG2-8PPLhWehw69yY8EkOMxTxnxiRyVbSCl5IeOGV5-SmMZDX415hbnXaPKKX4lEGuKrKrye5LVDZARNXwyBnX3vV4Bth_MkfTZbNLcC8jbw8LnE1RsFG033qC7MozmMRqK8lp6TMUbWwgWyO8IazZ1p9DrlinaKN3EG43Rsb2IFTI0IUiwuCFT57VYQd30wxBufmeECAxLuTh3uWmHkP_eweSa5YR5zGg71xxu4cXESF7sWiqN8f4KRJGmU6rfibrf7dQLV7R8bdYWSiOyD0qh9w4rzC78EQDApPE6gF7q-MSz8cQJmvQC_41JbEBZ8FdLkeOT6zdt7xH7M9-YUYMPiAWny-wXb7e1ZfsvtAWi75-12aroZHezHzo8oBMXDb5ZIjemKLvl7zBdPPxOoSmrl7RP6n0bJ-wdQXWw0k_NquG8GxufHSQczhCTNk5q6EPDtpxvlphXn2ZC68y0BiDEAL671PyCORAJ4_bdNjogb2JfITbHBlY7Xly3RRLro9WN2HnoyGe9br3trUIX3ctRjlCNWTdJTlDs8Mo3VHNHMuOyBridBmEMWfBzmQro7RoWS5yD3sgPlYkVtiLsTzJJSAqpESNsVx4FPd0trDUbD38rMeeG_JChlGuyalLI7O1SjlCwm8_Kld0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=KadFLNdhYcgqToVgvQdCmUaGnF32nHG2-8PPLhWehw69yY8EkOMxTxnxiRyVbSCl5IeOGV5-SmMZDX415hbnXaPKKX4lEGuKrKrye5LVDZARNXwyBnX3vV4Bth_MkfTZbNLcC8jbw8LnE1RsFG033qC7MozmMRqK8lp6TMUbWwgWyO8IazZ1p9DrlinaKN3EG43Rsb2IFTI0IUiwuCFT57VYQd30wxBufmeECAxLuTh3uWmHkP_eweSa5YR5zGg71xxu4cXESF7sWiqN8f4KRJGmU6rfibrf7dQLV7R8bdYWSiOyD0qh9w4rzC78EQDApPE6gF7q-MSz8cQJmvQC_41JbEBZ8FdLkeOT6zdt7xH7M9-YUYMPiAWny-wXb7e1ZfsvtAWi75-12aroZHezHzo8oBMXDb5ZIjemKLvl7zBdPPxOoSmrl7RP6n0bJ-wdQXWw0k_NquG8GxufHSQczhCTNk5q6EPDtpxvlphXn2ZC68y0BiDEAL671PyCORAJ4_bdNjogb2JfITbHBlY7Xly3RRLro9WN2HnoyGe9br3trUIX3ctRjlCNWTdJTlDs8Mo3VHNHMuOyBridBmEMWfBzmQro7RoWS5yD3sgPlYkVtiLsTzJJSAqpESNsVx4FPd0trDUbD38rMeeG_JChlGuyalLI7O1SjlCwm8_Kld0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miQA1aRIev5AWy9qlvNqDB_7WWzFvd4MIwVDwkI684az-sqz9_nGbslw10n8HD2RKgLw19mL4nC288H48o5I28X1XD0hKqdRdB_Q3JRiSfOQNHx06VVDD1HPfHekgzrGOR-t_ksjvT1gIo-Oq6AHgMcy9hkHxSP22PAxwzDubTATGva3nnTMZTqn1X4n9PohUg1-u0zJ11UXoP0ro4yiwPxngtDBuMzsAcvlw0MzyK-TxPgldY_cHZUSqWvUu1nPYhlqMC3jfl3_rFPHfmdmPL3AMg-1EUlU0dMd_kxNamVwkDtmBNMlOXhOAH1m__T1a_yFwIMJdSmv_JfZxAaADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onZxxqLoaDjyW9FPcuWQ_LQyRhVE3i1aa8bIuzGaj7GXJ4wmHJp-nWPv3s9t2XD9ILlH7Vnnbw7w9MPxAHJ1Lp-m_NWopHJFZDZdW3i3QeNMU4vdzRrMEZEcwL5znllAiRhttW5RkadeAKrHxR2NUELJBGrT2LhOkMmIPK9ZpXnIGBfw6zU33w-5I6nIY68008YfX_gA1PYU3-OSX0g-LSyX8h1Vc4JdKBJJ9HueGfZNX0k-qSUxt511dcSqpu8cUxGWsr9Zb-SQL8FL6yH2308huCO5VhbnBpConWJ-mVcO8RVg0SH0E8-8js6yXkdVEZhk-3Q1ibEXNBsnGDeZuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgx9ml6LvVKr2rJnRUMuIv4fIndIZeWWWyzdX_Z71aMc5qWyBW6RNlg6NrTcMzKaxX7ib5e-gO13o5W7nn0z0G6oTArujrTcJPEn_4Sa9Wz3w4m3ytzptCgosicxivZ9fgzATw9UfXOoLfA0zNVgLA-Tq5VV1TRJ3sOjOPeoqStH7PFNFqZDhSUyfKVIDczFq-zNeh70vNceABOk_99Bf07wCuYfaY2BfBgQxqwUH48xraHuQF7cSqx35DugniOz2QDypJbQ5v1rb1WEhAe-OuDpgBG9WZKznFO5cMjmxecbRnEyZ5ucfjT5kKF9cU0Y2UYAdXuATsBoGKCLAGxXew.jpg" alt="photo" loading="lazy"/></div>
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
