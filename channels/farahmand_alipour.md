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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3p8nGVBQZKWfT7-W-7YZkbhfFCftZ_3GX640oH_uNJMbZrKgoMMTL0lb8KexQfTLEd1RjPQKJ5LfAP1mzgrPEytBwMC03Xyg4staI8mi2WfeYFvm6lAFy866KngSRTDRxZ1OvLhHOA8S7RDop3sNu4B4z8WvEz_UBhmVEC_DM9PmI2byqJ9GxhREf_JMxDa5GNXS3-keCTcynFXDVNjbw2ISvE0kenlGVpZ4kkUFz750vodKpi73uUArPB3TOfKHyqhLoMNj6CiTtHNLeJT3uxO97Vjz184w6tf2XbLivCK83Ckr4Hno0uDkefnhwpPCvngykqDnH_gq-sAVHt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NslFIUbLzAd-u3LxjhpKY4PaK6e-vK3Aah1hhnPQjBEkpIuHuNIlJAKr5CI87gRDbCIuRupbie-cKK-LgpbY_yyiwhw4uAcc26-I7vhMtxyu0BpOLfmwbQE2O6g2r7tpDZBRB5_b5ngC5xrtYos9-9cDIwPcy2tNcBWqW91_ES3yFptpIGEc4vR4IKXRc9bQv76nGeEFp4dh5rxYVRNleSN6fh_MzNGwf63KW-CJT8qo0FdKs4Xe2clsy4wT_yguk-o2rWHcaL0tqfFhU42jKPcoyC8vEwsqAahqruSB6JEp7CQ930C4yh_fpkOqfYG9ZQojeq8D_PjzOITYtFEx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9OVLQHBYnck8r4an9MLPeSdj0_kEssPky4S7RrX6GQyQiAobeg-_wsLyBuo4Rw1mHS8hqSIo_y2TkNbB_0fDQJRolfGDvfqD7ZCNkTD1ORIAWndlalrOlM4m82X986ClzCLOkPLL4D1xGQGJtidh8n7tCzlYhAz-IlJ2QOLqW01IjqMTUSQcBMPV6h7slDaHcqDaqtme0CBh_vQHCNbSx8kd7XWdMp0k_tl1s50zt56K5b75bBnJXp4lET-iD6awfQPO2ouTCTIz8f7Hq_HWnN4HS5VxudNTDOUbJ_uiaXK2ofcrZeP0rQSoh6_Vj7Z0QhVTtggCy3k6ARn0cTZ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfs641kOYZZ0-S9F4rac_1Fq6igM125vIJaXiSLbjKSl3UND_rB1vapxcKln2I1VoLCiuInnc3vVCSohSeYrYQJkj2cSN1E6D1X0M6XfmCQ-MwaLXuzYReQZB07Dz8086sBBIN3LR0zodoJDLbzMYGmvQGhG_uUI-nUPHDk1BQzyPnsgnbu1Tu8RpCgR_QyESSewn3Z7HR52NgztjytgeSxm4vT3vA_YIegGocfEV-SQKQL7Knvm7Md21pBZLO8gs8pYBuL2RucWbMykftauELnVvTRfI8SUWFcyBhxAH_NuoDKXkd9cgaFTdirndwpKF4fScJ_uCnfoN0HH_iSjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ml60gaU0n_HDmqwDRghKaln0QJTgs1lFTo2RrVmBrCM-MnVIQw0MNonopleWA8DLcRem0ao9XYZYOWEIyQtkdr65cj_tp0TupP8DYQHxBCpyX5_6GeH7Eo1ZiDINnyXzMRlbXHOKJ0KuRxuUkboq44qWuUciEzjk9xNPDpppJwg5shQMRj4Mgwrsgnnia4nj4nHocAeOAFAVYEckGGbiNfQtJhLgltkprRMZqTi06A2d7fq4hbzaCZP48Hp9MM8Zgi3rZtjz19oCPSi5cYyfDmGHwZxD6Y8b_jdsXyLyuzDEX9n8OxQHK1h2wa-vHnutoHTd8uJd29mfy6PrQCYPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxnDl4wX4pzj4iHEERAnDz2SavVv1yTDHUDQ3Xq5zBRXZ4nQqymIF4dVQGfZOsJ2lIN9KlO6K0V_fVNiUf3dZ1Wqbc9P3p6PnN1CKhMqgy8iOfX-rOvj1U0Sbymarsx2PX-pZ_CAB95mZ9aUGFRWobUDKcp7VmTVq8u39Z_yrQtKWMtZZ-1rwjhpn5F4YVxsZ1jDey8CzJyHLFuvXmXx8eoFNG6V3Tk8RL88GWXK1tZSXidIYELOxk8zNMyHfUuM_3oOwZIwc8WCDvH8NJgw92BhYalehs4NLssLu6rxng4Z7yOoeWyJWa4sEZ46XWx8EAL9SZWY92WIa-lhdoInQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9IHTkE-c7IaZFrvpQCuJyIU8li-XKNRh8I0nA2nabvw9l28qVXoj9d9PdapKg5hxpKInb9aH8SNBIWjGlVU3WhbaMdtbCvUJxSQsFO987GtD10-IqNXgYkPJCyMtmDyMX4BwlJ8nGRZUUAyLKjRAjfRwH0qhGq7_apAduoo0H4TPyVQ4Yz8WM2pC65xYUiyszr3BqlMRBxAESrKcy7U5YsjVQxV8Tj8PJfZxXOtheNos9Lh2mcTfps8nZUbcn1KlnRl-EDjn0pl4kQz3H7f0NYxUSLpEJmYt2FNoOhPccoOOKOdqbmihyFDUw600vwCTL90Gjurd1z6bpsAej6r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVa5vdQgQ4XRKaeyhaN5gU1VCPMIdROCv5URaJRg_OPoDbwDAsy_ArRwfG0MWJJboVipwx9MAM9Bv746YAbXxB7R7mHKoMC17z8FMu8KKuXWLPDpBic0akBqyv-ch9GCIvSbLXB4RwcAsYui1Z4IEQmMBeK-vvc-iG5kDXUHvbhDObePzcJgzFaDDcpZOrUYJd3JiV0dagC0PaeRv3tc0T8Ct2JKmlv1kGXfErXWvwnWMFQcuVR2PG_81t7eg2eZ5UIkr9DUOhXZNLD6D2l-Ki0TH63ycwepLWqpyO2m9RKUOLrYQEI3MYMJplS2d_brMXvOg7FupUDsSgFLUjc_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzGhyyfRy0hugQ6ye-clpky4VPM7Z_ThSpbMssb0TBklhXI1KQpTAPCRKrul5A78DfqE-RkFFUQ9kOqQQf_WxCNLBb4925SB67WxqM1sIG2hD9QamYCForNJ_VIV1uf99IrIwpsxiOC47j3HKUsstI0Xe-jxAiKGQUk6yECnv3yD2sQi-r4wUfHA7iq5duw9w8ZHk6r7uIochfS2Jv2B-iwz7N2k32NkQsAo8JZF0niJzAlfE_cTLCOJfJlqteIb993fzLVK1NxiWGS-_IFzmXax-sVvi2zF0b2-b4nP1KufGXBRhLh-xLLUZfIWxqg167CAZVJu8SviXl_x8GUJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgexaOcEKvx959xmdFE0gWk1rMhngg-ddOZLKgb1QJmUB3kb0MSsc_iVHyrNv8-Fc3s5AhAk1eWOvQmVABgQfR80renDRhFHCZtoHBR8aNCYZ_Ci2Icbu_7_LNnd3lU2QlVKvQLdNCyIECGAC1ROqB0EGImH16Ehz_fobmjpfnzEpcoDOF-_ji5lb5XIqSUp4MCiMHo2Kp4K7V5X0FVC7--VJ--S61AP2ZfRzXcqeV142xcudqI5zz-nECctowgE0bF9-OYRs_jMW25CUoKp4h250tsVwePKKQGDShqzsM5AIEjcytE7r9KcT9yppiOHjea9DhEEQDnVlWIURGx8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf8NPpSXWdGNlK-3J9fFrSfOYB26H5PiOtFgmekmcD2hLq3jmqg0Pjt5HPW6mgrsgL5_GQQTHF2D95xH5u0W8BgJS04zYNn_K1duDQDDx5dfNklpH732ufzXlDzqSaQDrDnH_GZ9Od2Zh4Rh5-ppIxgO66HD28UmukCxT00a_Gj_u8pP2EmHEjbeu5O189AEPPidvXpUeI7ts9ltU5Jk9Ah0DsQCeqjo8-HNNH2GKgSeydOeuviX436uQja1HfBuoKWmE5RpxH9S5t2jCRyEXP--iKJZ8oZB97UXuUd_00N-e7FJzyAh7PZDJ-scE58RaMK-ZFOO_Vb9XrkQrfuvHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaspM46Lu53pbqtnbj5yCydFVzBRpfcOP5re9K30meBpKIYR0zi5TLPvC1x946v8Hhvdh3sk_WxuZrZ7Wk-JswrCXisjcfIQczKxCp0tEq8nuMX33reNYGWaioPucdNYycUM-qa7lGtvoE_7tK2F-bqZ10sKvmB2QIn2LHaJ6nXjOFw3Owg6bVR7of8Cc2L9MhSfH4gQdXDTyuKavuJU4FyeRtivkjOeOcHrHFwyBVufLdGaDi4Sz8J6V6JcMuFFADQyl8ahL_GgIilIIPVqWFa2d7CNHM36z6TYyN3oW9UEXCNFiv-8CChw0iOlxA_EdWPvOC1C3JOJtwqjRaLLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKjZtz8OW7nESSg7V2KEyVdLU8q6Nq8E7RKwXIDTaUubSW9S-VN6AZ4sydRdFUc9lN3SxC0Uez5GIxXGhOveSaSBgLWNYDoFXZgZfVsacitsprjmrwOui3El6WdDRLCGRTWPZApGQcsMKbdHAvaYwXHtrNv1_5oMbR4XDUDcMtssV8mv6-dxSIdlt3ziox90MC1E2c5UlYf90zyN6Q0lakhedlp0JSv8HPMW-zhX0eXt4moUDZEyKt6apnCZT8sbFd2OdD2h1z8QVa5x59tIhkRpsgCnasUY9MzkyhhTwosBg2VdEDOvPlHyndegiFtgVE191OX-fjFR5SlOkBHAkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLTz5PvAGaTzH3ZcuouBCEjP91BnGrJJ5oHlK4YZmjDa4HezRCaP8NJkpuTvmlC0acmWWpmfn4IAdbaAmOwUO8814_KPoXeljJXX0OX1ADPjOFjshgBEFvJbpBz6i4gvrraYMkSMUTo0t5cZkobltyJLuXiEu45Vn-WPhnyfA2J4JcJNZnaGK2ygmvjA_W-E5HN_jlO3Fi0X09jc3QUlUjENqjqL_xsumddigP2MSRW-PIZD2E2j4BOoAZeibP1i4xD_IobLxSaUJe1tTMP-V1Bb0LuFuLXnqdcXLPvmWp65JT6bsq0DUIQi6zZODzuDskA-IBj28lgpCi8QyWen9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=X-1rcXSe2SN9n6oxhjvRNysV2pw_hztACNiFEyHf5DV84UHs01TS48Yalg9wxWSVoD_P-Y_eR8F0wIaxNmhMI9DQ5TDKw2FAQrFKSNWPWEIaZKu1JRnrwQT0X16Nozjn4MHWYJ7ZpQGtPIGUU9Sat1Jzt_Q8tEVl3uk4vv3-gEAZHiEPmPhJNW3aliqfEyby6fXc05nmO_33AGUyleMY_Zm-dg8Fdosp133kovroO2mRRKvRDt6-PJ6CS25mzVh3SasjFS8g74qJ0ocDgHYtE0A_ffhKBwPOMMO6IZduX3Rc9JG9tnjnjluFpgV8VqS0d_1VbHZUZtprd-a05IdTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=X-1rcXSe2SN9n6oxhjvRNysV2pw_hztACNiFEyHf5DV84UHs01TS48Yalg9wxWSVoD_P-Y_eR8F0wIaxNmhMI9DQ5TDKw2FAQrFKSNWPWEIaZKu1JRnrwQT0X16Nozjn4MHWYJ7ZpQGtPIGUU9Sat1Jzt_Q8tEVl3uk4vv3-gEAZHiEPmPhJNW3aliqfEyby6fXc05nmO_33AGUyleMY_Zm-dg8Fdosp133kovroO2mRRKvRDt6-PJ6CS25mzVh3SasjFS8g74qJ0ocDgHYtE0A_ffhKBwPOMMO6IZduX3Rc9JG9tnjnjluFpgV8VqS0d_1VbHZUZtprd-a05IdTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsqWVQTly40x_9_mmIuVqDjqa8fdu5GZBUvdY8WCHR05lgbzVcn6F29rdJojCT_XZJG0bjJV6JVe_zcBdZwSlmJMCq7Jw6QlnkYQQkRtnVcK3Nw2TBt2c0r9dXaO6yTiSSP_WYGSlG8YS-Tqu1HZvCdl47Wzl1eLelnuRRdtqKUHUKAho4BJEE6Xy52dNcN3L3o7CDyZHIk8KvxqUfPzywV-wcuGZY-4OaPbJ0daGiy4riPYSpGXe8xum1mEDPEQljSL4Xr3nmyAMwk_ybCpIKiS93ar9kCIATetYkaJvU9ZVEc-XbHQPy1UJs3nbBApmCwCXvBQDqiRUVzD6-8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3gK3kZlrrFw_Eat7ftLnvBapLMSi1X347FxQTyxuGPwKvJUNfOryLMkML7xRyvSMJUkXH_ha8UTpAZiOIYdOUGslVCBO4f5ZVrmwXcQXlor1RuEcBb9vIi2ERMNrPb5sIEVcnhL0lwBElq3QEuBWXcTpdr7pK-l0De9CEEnWeRuP3eA1x2L_zqnJr6oGSVj-38pe8hp9_pYPa7OL-zksC7e4Fz06Nj3Q9WJau1qQwLdvl3dJ-bWLaisY5y6EnFlCNuWYtA8SVmTG2-IVq7QiAs5uT0dsfs_M6csVXRq2yEBh1aIO-qN4X_Ltc9PhPvuCWVkyaF_5gJWZbiqLTO7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng7SF6BkFGqfY6485h-fGc-mFB4uEqsSIb4GWPTipQdV1SQCxLguz5VvfRe98SrF3snJ-a8OON5k00d6Ku2cyE--fVogr8von_TeX9GDdeD_9YEC0Tu6lNeBYLqvjqAXXD8ee295xpxR2Vam9phj8C0axXqc-IW2HIYeosLoDhpAhKFVEpPQTOuxT2ftghtrMPljDMsbKN1KuO-eRDpf4jqlDILsnNgK2vTRsqdlQNDYu8thKAQnu0v4Xf8Di2E57UPT9pqQ2hcmORYuXHCWR1QYHEJ7HNiHXv5uBH71gpB8pJdvSXHP82WWB6i-4Fwwsn9onofo6U5tqhVumIzvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=ZyHPytVzcUGW8RL2zQ1q4bNtv1hMQJzTqnUWZbD_Igbwss1HP0tuczWakla8-WVuhctWhoBdl1pjumPtQq6NblzVwjQi41uLB2KRiMFIuL5nPgyf1JDPA0ZZqpB4h-_VO2iS2JR9AZncQ0pTvs042Cx-OqViCOMOxsRkcWJpbRnnXN799EadH_p2ywD7G7GyZg5dg8IUlQXir3RHpgw27--lSjg9R02KNF_S5tRtbOejvvosSxD5yD0nGOVecZI91FsHzMdulZ6khQieutyj8roD1VuPhvmiYeg7s0mMp3fhIrf6LHu4fLm0sMsT1PNeFEZvJtadbmzUjBi07_dE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=ZyHPytVzcUGW8RL2zQ1q4bNtv1hMQJzTqnUWZbD_Igbwss1HP0tuczWakla8-WVuhctWhoBdl1pjumPtQq6NblzVwjQi41uLB2KRiMFIuL5nPgyf1JDPA0ZZqpB4h-_VO2iS2JR9AZncQ0pTvs042Cx-OqViCOMOxsRkcWJpbRnnXN799EadH_p2ywD7G7GyZg5dg8IUlQXir3RHpgw27--lSjg9R02KNF_S5tRtbOejvvosSxD5yD0nGOVecZI91FsHzMdulZ6khQieutyj8roD1VuPhvmiYeg7s0mMp3fhIrf6LHu4fLm0sMsT1PNeFEZvJtadbmzUjBi07_dE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njn5y4jSEShk8wDdyyGviTUn28dLG_jchcdphlV6bC3iySMcW0R-zLq_GffcG8WiIZf5y5-bgJQ_3h-biZPLZYAImbFLAjvDKbUDeToDoaVmbdRXnFbx3hy3e_9JI2TijS90UqNQPJ-7NDTZAvErY2N8VlyxQh8FaDiSZXGkhrAET2NzbHDgXQjw9Aea-P0n0tFegS8gbIloig4Ncq4N8Ki1Fwnxj3SzjZq8hupTw79UtenqLPEACVQtVNMBkVmJkyK-rYFpwofH_F0z6LmrZ86NcMm6WZQb5gc474hl_qZ-BTb86ZPtHFt5T3GStLrS9RGSCMpGuTDS-kSQFyMsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=mjUbv1_LgpnHonaXEwzZ0ErZDbZpQwUnP2iiug6eIFxEe0epCETuHf3pstzRC-dqLVEccVaV8g4jttplFZxU2b2xOW9Ct9vx0HtxpMBEJj0BbIw3LWhmG3TeZeung9BBqEB98J08ffHvnzOgXSt6nkKzqDw2Cilv66OQJPVCwcIgrxsR84z2PjriywSqqxQ7QoEzTbqs6aYuxZP9en8PFKpBw0L6l7a0PnbtYVhoSufwYmYA4hOPSavCgty3anT8cuxnf6-0QNnejElf_2xA12rbb3KctNb-9QYWqnXuWJR7fNG4fsU_r_Hd-eG725cGn7xm7pnXJyOukUkz6nfs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=mjUbv1_LgpnHonaXEwzZ0ErZDbZpQwUnP2iiug6eIFxEe0epCETuHf3pstzRC-dqLVEccVaV8g4jttplFZxU2b2xOW9Ct9vx0HtxpMBEJj0BbIw3LWhmG3TeZeung9BBqEB98J08ffHvnzOgXSt6nkKzqDw2Cilv66OQJPVCwcIgrxsR84z2PjriywSqqxQ7QoEzTbqs6aYuxZP9en8PFKpBw0L6l7a0PnbtYVhoSufwYmYA4hOPSavCgty3anT8cuxnf6-0QNnejElf_2xA12rbb3KctNb-9QYWqnXuWJR7fNG4fsU_r_Hd-eG725cGn7xm7pnXJyOukUkz6nfs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzgXLb6sh4sF-hMfeda1KT-wlOS2rVLeVHfXyvEglOtSITXnYC7-g9aFK_Xvqz8JoliWfFr4ddbr8K34yqB_yJcoEyniO9Tt6FbKQbD6WJu-Mol_puWu9k4JUmzdNPYyuBTZqqjhVy4YxAZSYNeNt7p6SKDMAA4xJhk6JM36tkds_UQREc2eQMKL-1_uQP4eWGHbgV2AAjcQZmi8Z4PsTTxfrM4NVFpUVMVnZBicUc-QnYG2I0MVqwyzW051bT3PTzdM1bjW_oWlFOOZ3gS9LcOQPn_hmvhyw8goRzS-NsLNAsMYH0FlvxilT-bhhnITMkuFIXrF_kRoxU5xfYQAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uE3hPMpeQyjWHATTU3HEw-yYshR0uhVplPddkFMPkGu2h4ACEB40B-llLEVp_ujtmCCSb7Ehj1QECpFNViTrTNvDcR1KUFP3xu6pPUJ9JF-J68I9rro_7-ucR8Z9kXRbqRzNSOregxNcOpkg76o-VN9CNyP4eCFqkn_7N3EbpCaiCQ8qff-sum24yQ6FYPS3tVBJh5EOYkBHWOJeBR4JTDR3pYtT31Vct7CDD-jjelKwIWgUvAbKu6wMLUqnYq0pgmoyO_1E_q7vkb7H4sjD1TAorJV_jsIwhnDZVEe8Z1IApSVvcc9xE1SLCeWh39xRhRa1bE9crYle4NffouPYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=mXLpmgxF_jPGbYpCk6Fk43St_lk1iMMuEYVMN0KFdezzqLteHK2E0Zgn2HxxK3Ie-ttxFYl5SiNptxVUmAWwW6agH8qAyo4PRpF537L4-5FZvcZadkTN61S6mdE0TvEEUS1ffkOfARCiBkJZprJgi5uIHBkGHJtK5YVcJr28BGW8PMlXldrlA4Ix5Q_U6JUZva2lOnNPTtkuBEVb09uUAYmkxZMvNEr86au5uyXJ9w7rFyuv59eaV5GJoeI-G-rtan37UUPd9wnTRarEwdi2l7yDF6_6j3fWiAQn2GDgi5C0iJOqPTTCTLmkOFxayYesq3JiiFB2Ya8PtNy8_5JzhVHZI6sxNn03FZAraYBqcnzwFTrSmVSly0CT_nbaZymB1gJtGhsOaNW8jFXfT89tgnMV-LI9PUAsjw8hs1OvrPXrZdviqLiVLR5hx5FbU6_fcUYzft3r14OWU-pj7L5j48BgcbL-fMr383VPbCRLAkxSjja2JwrZKR34b7s8MB-bXpc4udFC5Y3GWjJMv7_8XAE6u0DEltm0MYGq1MQp9QLq231uBxCOdO_m0JNpvz90bSapuKI9w9Ect2LNZnvSJQBsPrTMgeiLb30mmcQ4-jxqiG7LLrOncfX8o20LqqcgCJsU71nYZem_ua3BXroI5DDixXc5JCVeDfgPFzZa-w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=mXLpmgxF_jPGbYpCk6Fk43St_lk1iMMuEYVMN0KFdezzqLteHK2E0Zgn2HxxK3Ie-ttxFYl5SiNptxVUmAWwW6agH8qAyo4PRpF537L4-5FZvcZadkTN61S6mdE0TvEEUS1ffkOfARCiBkJZprJgi5uIHBkGHJtK5YVcJr28BGW8PMlXldrlA4Ix5Q_U6JUZva2lOnNPTtkuBEVb09uUAYmkxZMvNEr86au5uyXJ9w7rFyuv59eaV5GJoeI-G-rtan37UUPd9wnTRarEwdi2l7yDF6_6j3fWiAQn2GDgi5C0iJOqPTTCTLmkOFxayYesq3JiiFB2Ya8PtNy8_5JzhVHZI6sxNn03FZAraYBqcnzwFTrSmVSly0CT_nbaZymB1gJtGhsOaNW8jFXfT89tgnMV-LI9PUAsjw8hs1OvrPXrZdviqLiVLR5hx5FbU6_fcUYzft3r14OWU-pj7L5j48BgcbL-fMr383VPbCRLAkxSjja2JwrZKR34b7s8MB-bXpc4udFC5Y3GWjJMv7_8XAE6u0DEltm0MYGq1MQp9QLq231uBxCOdO_m0JNpvz90bSapuKI9w9Ect2LNZnvSJQBsPrTMgeiLb30mmcQ4-jxqiG7LLrOncfX8o20LqqcgCJsU71nYZem_ua3BXroI5DDixXc5JCVeDfgPFzZa-w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bD9PB1zpoEOtY4H90Oh0kcOrebi63HMhrQxuKHWIUp4vgyf_hLp4ZRInej-M-q-EdTozc0RPde3l5foG1qxIKiF7xGDEYjs6-4kp14YtRGOnSD7T93WBnbnRl4hGtC_bV0ihrbqPU-Nknf_rj_rgBdQ4QUtBuZb5Kdfy6voIeoNxCV025kjT4VWlWVZXUKq5XiTG3SCdo20fVgw47bscOTDRQq1zGnaf8TTYU5O4NpzW7NxpmSMyWKY14GaUPZ1B7oAz6QLe8xWJ-qO8yCjNGYVoVaSlWVIuaBPNYG9D9PgvDNOYRhPg6TDWaULr2E3NJOOWccP1PK16fEX624rWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=bD9PB1zpoEOtY4H90Oh0kcOrebi63HMhrQxuKHWIUp4vgyf_hLp4ZRInej-M-q-EdTozc0RPde3l5foG1qxIKiF7xGDEYjs6-4kp14YtRGOnSD7T93WBnbnRl4hGtC_bV0ihrbqPU-Nknf_rj_rgBdQ4QUtBuZb5Kdfy6voIeoNxCV025kjT4VWlWVZXUKq5XiTG3SCdo20fVgw47bscOTDRQq1zGnaf8TTYU5O4NpzW7NxpmSMyWKY14GaUPZ1B7oAz6QLe8xWJ-qO8yCjNGYVoVaSlWVIuaBPNYG9D9PgvDNOYRhPg6TDWaULr2E3NJOOWccP1PK16fEX624rWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D53xYjIowDlJIyjMl_rm0s8cXY-iVFSjmBrNizIOpAAYJvF2II7cKGWfo8oi-6eQKjF_nqrVb8KmxVPZSHstQuCG7Qqcgkp_3mJlGTvAooSaaDYKZHJzQfexAcJloXXGJarMMsT_8KbC9xns3ZL7MC7YM9s_Siis0sO6_MNQNlfrabFYQ9LsG-cbkpX36ENjQZ55Sf73wbNdfRycT8QR3RsYm9CfqT8Brikp1Zt3zM7ZMwlblah6sFqucd39MarST3UKDqisNRrdpxe2qAOacNqBsvQPMosGHUcv2C2XCIWULzxlGnxUu1NlbJIzvEFivsVaNxuUYA89EFE6ZBZafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EEnE7SKn4J6k1UgSWwA_ZlS4T4IJIlkCIuhrYvt11eQWsh4RyXl-kVtnMAsR7S0L3uNldi00_CACD0pXMwb0yME66o0Azx2wxvgF8F6hvHFj0-enfqBjPLSptRQALA6Jk7l8b6NQiPdgETwpvq3ZRdJhW4RlS5ngbvEJ5ZXBgzXDqmw8l7uK3N3N6qJ5lLeUOyK8YWwElQ1NMhp-pzfA6WeQ76k5krm0s0A1LBGZVeWUpBdgm_Eh_v_njmoSZEvgdCuLtgTRU6lgJFpf4H4EnH5-95M8rcc7x9rbqxfuJ3Kd10m2Eru9v7w8h9tMpdp-UrgAtTEFT44CwPEzk2rIDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EEnE7SKn4J6k1UgSWwA_ZlS4T4IJIlkCIuhrYvt11eQWsh4RyXl-kVtnMAsR7S0L3uNldi00_CACD0pXMwb0yME66o0Azx2wxvgF8F6hvHFj0-enfqBjPLSptRQALA6Jk7l8b6NQiPdgETwpvq3ZRdJhW4RlS5ngbvEJ5ZXBgzXDqmw8l7uK3N3N6qJ5lLeUOyK8YWwElQ1NMhp-pzfA6WeQ76k5krm0s0A1LBGZVeWUpBdgm_Eh_v_njmoSZEvgdCuLtgTRU6lgJFpf4H4EnH5-95M8rcc7x9rbqxfuJ3Kd10m2Eru9v7w8h9tMpdp-UrgAtTEFT44CwPEzk2rIDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqnyVmo8Os46mDb-JKGtl_e5Mxsji0eeL7pdJ-ImtJuFEHQUuiRli-Gdl6FdDo6YyPB6_WYwV0ZGzC7xKKgCr_s7Nh5CW9WmICjwml_PgZXdm5XJ0jH1sPZL9Z-CVOs8NrF5sm5Z69nsBJhU4LzL-NUUbmpP3LQYapMwTees0ybfLlDdnqzLm_FDk4Z2igwrA-SyUCd15HyKFsmyvquPmgD0X2EBG60lWevMvKvB0lOp2nSFupnhj-UFj5CoR7gFEyLGk9ylscxYxojAzbUvr0H3MMRldLODUOLIb_x-1VaHl5GJPDy9SQyw1gUsYQBzRsnhLH2ZJjNX6S5PZ2oaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZqAB4oox-89zL08IRXUT5YrOhVfICwqi6YzDLf-rv_oPhYCUtpHwsJwQSvlGfvrVaWUuFwfFZIJEfY4xuprIG2T0nMFAg9gPg9c5lWNNeZGGjx2m2_EwYL60HCAG_R7Iz0IC-gH9-5vg6y2HvzsHq2CI0aUt8EYaU0ZYm9x9pTAO84wk6NSCJqJJeGve68WXwD7j7Xco-0iXc6FZ2hEWtEtjlJAqYv8u_U5dAfZw4xAjfIEWT6kDA1x9xTf30BUAAvgxEkBlwBmTIdahL_W9l1NZeYzb4zqRdZtZ0xqnQuysHxFAfBJ-hx3Mu75AePuGGmCSU-KEG6A0GOM25eExw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7rs0K7ouJHUX9vRyGx7o4mQJAL-WkU2OO3BPwcHBc4xFhCaLvlCNUr4pFeRiT99ghFZ3b5DD1R9L6BR_EEJn7Hllf8xuISPc23B01bx5f-o6sKx_d-C7PgLejjGhSnyt3p5Zg5VHN0Loq7xNeCczlnZQt6mgNAFsnYGb8xGM7KhVjEK7JYSRO3Mnd0mEw7S0YAyFmTkmJejIwA6KmTCbF8ScXyxAGk-9tHns95GDu4hOQ0I4SkJC39vvCec2qnc8mMrYdzzlEPdpMDJAKVVT9l2HME1uICOhQCongZyhRqsHD2FkZwIZa9sVxzOygJ8Md96GVMkZ-fZjkKAbr-J5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt4zk2FhwLvC-R17S6MfKmmoIoxAE-6KChV_bOR20hOxKD7ELb-wTnIZHc0g6uZOMKB3m6dH8PlastjPWfm_fye6Dj5YnCp17vi3nHZ7dfjfRFCHtR1JuNCjEeNjg3D5iwXyTR34sNlLx_K1EnjdE53BDVTXj9VjiWnfsxFczL4ZZHsWkOmkXsKji8jpiYdR2opI6MKFT1bLcMa8kPD2H5tAuc8r72MJoM2eUClfuC7kTcUjuPyGHmcLt6K89leKK8QFYYQlrM-RwB1xwMpDxnVgeVU_QofA87FQikxjs1JM8ezQYBPFHx9MKXynGCNFedXm11q_o0dYvu512WisIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaIb2yQM1STgOThX3lS8rH8UJwatoUAzO5AENNbssUNs9EzAp9WXhMsyMu194OHhesOS2CypnK3rqzvwCok7yFUWe8I8WT8JXKnS1M7MB0dUpGDu521kJkK721rnF7Xgk2kyICuud4uFQWdNFRx6C8v_3nRWyG48z-Sm1WT0DlcZ7K6abDyteQGPj_4mOvLSyVRCar8NPIK3B_2r-C8Dv2u9YM3SZi4RNCamcPk17kgRjb9oH5Xg1g6Fh-8UVppMg6lV8cTpjMmlCLFeeOiWfCoPFF5fFYwlG8nIspxntZxqx5VFlE2MzzHM6q53voYgPuVEsBZASi7xVJhGzHqhow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=t4hb9UZ0AUmT9GnCLjDLoUuMwvgSB2efCZIO3subdSrj6NI_38Bihu0b9uCqyB2wGBbXfniMqfD_YPzVd7fOt6XRTcuPKbPdDUomzdXXVI_p-XB_mTH3kX2nF1nLNajtlX5MDiOuJIroz0XStMS3-5YdYV-6W49B-be1iIuQK1cpeEt4RByRx888EkEC02TSP8xHdD5A85a9N03ByRwKLz7cQpOuBaz8r0u75DBze2oZanIK0Gz_BQj1Oj5tC0pZtYoPGYn30UnesAXW6DYYSDNAnQGkKwQjPbXOCjT89TXGt7jXGcLTMx7c5fWAAWNkxDPEMGyIfx2uMYaXM0R4sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=t4hb9UZ0AUmT9GnCLjDLoUuMwvgSB2efCZIO3subdSrj6NI_38Bihu0b9uCqyB2wGBbXfniMqfD_YPzVd7fOt6XRTcuPKbPdDUomzdXXVI_p-XB_mTH3kX2nF1nLNajtlX5MDiOuJIroz0XStMS3-5YdYV-6W49B-be1iIuQK1cpeEt4RByRx888EkEC02TSP8xHdD5A85a9N03ByRwKLz7cQpOuBaz8r0u75DBze2oZanIK0Gz_BQj1Oj5tC0pZtYoPGYn30UnesAXW6DYYSDNAnQGkKwQjPbXOCjT89TXGt7jXGcLTMx7c5fWAAWNkxDPEMGyIfx2uMYaXM0R4sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB6A2yI7bKNrTSbkFIvg8xPvDoz9-GcyJngnVeyiO6CT4q-8v5kq2uRPSEAypZZBRnEgGjryuZqJdmj1FFcDZHjyHwGUDmClK282ESJ9nxaiZ_zb-QS407kRtcuzh3xQ92HKhV8Ec5cdNCo0dzHvJMVpMOcHLdbbsRymcxSrP9EGp6BSjBruiJAPyWf4I31wTYXMNYjv1v7YD8ebS1RkphyGcL2YVWQmax5JH_bDzCNUC14ahIy0ChjQsTkDAlG--C1cNQT8WnMZsXA5GOo2u4uIJxFHY_RzGTzxYZ2LWPISdcuuObYoaCisL4XYVXStcWOBCc1aLQ2fY92lcHMfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdJKjEkvpU6xWdl0VuWZKv6YYZkebJt3G_KPu6Y0nrSYzuhetJeNW1UIJFpnTDszFmnYIUhaOkG8VunpGR-dt0_WNMPro_Nd5DOaIwc1Yi1cnQtDao2ywdYmY57QY86HKJirtI6sYRclxFmjAnsnGMA2YW7Md7suvHk41YjxWQgIcas03yQYCddsrIN1JdxCigRdHhY-uHgxqvDXAJF1NYeVYj8pl1AdtS1sdipWYpUNHwmJVHxtGru9dQ5zL64dPxqLMN85onD1BvAJfs6iKkcmOBNemqSfEpflsgaLFJHx7RtNal9VFEDzw2PBKWC76ZLyzv9AaovT9z0DkKQQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=aKb5UGXZbag9Kmd7JjRD0Dd0_XtJJ-3Kf-DIieyTb-_NGQZPt0T46lwT443T0j4SlnyForJvV8u1M8ngS-DCgw7XIaQlO2kd-6XTMUnhCtkMKmA7HrNS_Fi-OJwvsQg0AQBxfrKnc-UKfgUq8Qns5F3W5AkxOABAuAK_auvx_UpT5r10b_BBlCrwTcI3ozWHVpS20mn3qXZ-OZqThA_kRm8AI4YV2wtM2hwOZDlndgvqq-JDp5GKGVi-773kEJ884u0G7lEqY_f0W9YavF1VPYV_J6alLs9oMSi_ZhH9UR5ZwV9JQ9Jd04hKVh291j5PQLhtpydTXSn62zB0GWnGBrYDE8QGqiYhU31_Auh7ZDtKOhrXQ_ftxPmztAX5oIAbUWJ-s87k2NeJi22lg2haBnpT4EMTIKgYhHqC9DhG-45-QzY6ZPE-UaBoD7HNSNAkTMLJA0axN6GLXxTrvL-2OLsuRU1K7bTWQQBbc6d5OJPsaogxRfvMt3QE3DJHpLBm4BHC0D1n6P-SRPhjbKkQKP7qH1yurYCzS9Cayu4hiQ-E_7DXVD2gkC92PBXpnuN2xVQ5DO6nuAWt2kP0GC9qFICpjYzBuQnA29NYtQSLYvxBYrpLeyQwk16UB6ktBdGRKdmQYiV-vx6D37782tk50hwkVSzWkCb8GNKFTda6DZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=aKb5UGXZbag9Kmd7JjRD0Dd0_XtJJ-3Kf-DIieyTb-_NGQZPt0T46lwT443T0j4SlnyForJvV8u1M8ngS-DCgw7XIaQlO2kd-6XTMUnhCtkMKmA7HrNS_Fi-OJwvsQg0AQBxfrKnc-UKfgUq8Qns5F3W5AkxOABAuAK_auvx_UpT5r10b_BBlCrwTcI3ozWHVpS20mn3qXZ-OZqThA_kRm8AI4YV2wtM2hwOZDlndgvqq-JDp5GKGVi-773kEJ884u0G7lEqY_f0W9YavF1VPYV_J6alLs9oMSi_ZhH9UR5ZwV9JQ9Jd04hKVh291j5PQLhtpydTXSn62zB0GWnGBrYDE8QGqiYhU31_Auh7ZDtKOhrXQ_ftxPmztAX5oIAbUWJ-s87k2NeJi22lg2haBnpT4EMTIKgYhHqC9DhG-45-QzY6ZPE-UaBoD7HNSNAkTMLJA0axN6GLXxTrvL-2OLsuRU1K7bTWQQBbc6d5OJPsaogxRfvMt3QE3DJHpLBm4BHC0D1n6P-SRPhjbKkQKP7qH1yurYCzS9Cayu4hiQ-E_7DXVD2gkC92PBXpnuN2xVQ5DO6nuAWt2kP0GC9qFICpjYzBuQnA29NYtQSLYvxBYrpLeyQwk16UB6ktBdGRKdmQYiV-vx6D37782tk50hwkVSzWkCb8GNKFTda6DZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=vVJqGwga-MyVlRzwhpVi3PnJdJooEWPWvN9Ov4ZoJrHfRSML2bKYAHIwJmzTE_xzn9ttE-KJcqRI6Owk_LCLPecy9djcTABS7HgkO74F5Bp_qxOXaAqLIRpcnmegLKyXrGc_CodpY4tC9UsjVqNGGnOgIPvJtX3c1AD_owjEYcXW7029tMkp3Hi5RrX9VndF_BFLTZ3FIxZKJHJkvAqnNwyD-vipQrxL3a3WjEI4LBD0vi7bkP-AXlEZF3LN4-TC2ygsMV7xRE-Z6siZmTVDoObeVRiHZxDamnPK63XJtGxJSAtYKjttygvLXOtfYnQC-GrxlmGFHgNN9NxEviobLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=vVJqGwga-MyVlRzwhpVi3PnJdJooEWPWvN9Ov4ZoJrHfRSML2bKYAHIwJmzTE_xzn9ttE-KJcqRI6Owk_LCLPecy9djcTABS7HgkO74F5Bp_qxOXaAqLIRpcnmegLKyXrGc_CodpY4tC9UsjVqNGGnOgIPvJtX3c1AD_owjEYcXW7029tMkp3Hi5RrX9VndF_BFLTZ3FIxZKJHJkvAqnNwyD-vipQrxL3a3WjEI4LBD0vi7bkP-AXlEZF3LN4-TC2ygsMV7xRE-Z6siZmTVDoObeVRiHZxDamnPK63XJtGxJSAtYKjttygvLXOtfYnQC-GrxlmGFHgNN9NxEviobLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjQ2VkwCOVZxZsp4KWM9_kismtpgm4lz0t-UslQaBz8Mu6eqZXEmskz27LwhGCXXpnmD2cW16qcuzi2B5egdIGzpFLgtvOyov_-u7WBfq4-9FYHzhHrE-iXCP7ewR6YstG_Eqn_LX57FDJOz-nIXyj6Ocsr8gtuqJQnM5gjEf_sieT3vJmVqpvAv364L-Jj99sMPggsZC1FCWUNp-R6xd0I5vb37Hr-sGxwxd5o6V1zFwOiY4O7ul1uXKO1w2ywwmKkd2pv52_03w97HHHwsIy0UzU2H32T_aDHwvYuk_Izdw9A3QJK6otXMF3TG-lDh1wj17XYNB9rNp441JGAX08Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjQ2VkwCOVZxZsp4KWM9_kismtpgm4lz0t-UslQaBz8Mu6eqZXEmskz27LwhGCXXpnmD2cW16qcuzi2B5egdIGzpFLgtvOyov_-u7WBfq4-9FYHzhHrE-iXCP7ewR6YstG_Eqn_LX57FDJOz-nIXyj6Ocsr8gtuqJQnM5gjEf_sieT3vJmVqpvAv364L-Jj99sMPggsZC1FCWUNp-R6xd0I5vb37Hr-sGxwxd5o6V1zFwOiY4O7ul1uXKO1w2ywwmKkd2pv52_03w97HHHwsIy0UzU2H32T_aDHwvYuk_Izdw9A3QJK6otXMF3TG-lDh1wj17XYNB9rNp441JGAX08Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGRarAbOrAJFBWAefIQonw-AN5bLXC-DtFdF2Cmn9jvjS-Ors5CGmOYcYtf6QzM-y9Tsafgr_cn3t3dQnfeBgRVX1_aE-Q1Dan8owA4je-hlXjNZgU5WPJ7vhmvevXemnbF3-dljoNITFk8rJ8EUScUKBYNWOyJAbfyA9CqcxakLfbVbrJ2Am4tbiOM0ZrIIpi1WjljGlMaMrcvIHrw718YnV2X9WgMTPiXoGCCoyc2Pc8yk71lwIPyRYA9YFXMlA7dgX7R3_rhyutdAS171E_1sXITFaOHgxynyYvM8jLyle5anT7uBgOItYbSR27lAaMd6LcD-0pzpw7QufJ_CWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyks2isoaSD2p3vPFgzfZ2vJmvlhJcj7plDHppQcRl6bqyo9Ttm5bEw3UgbV7WBzxK2Xu-9WKBZF-I-LstTIOe_YigNqTxWTgGQxyIJwpYZ41pMKHgSliQ-NzK0cj_jE_ASm4jyFsC3gzP_J5B8WF6byJ-E2Tx9ObujQm1DjIzL7ndzZ9o9KXxQ0LW--vMWWxAhecxb5OEK4auW4kDblSLA8NFBR_6nqL8PVOS0Zy0bdhqIhLtxwkRPzPRSb0ArERUlt6ZZnKPHLWpS9HDxt3YHKGeGmw22oI3KPAMhqXKMNwpoRoNvZq_tv4DnHrnujF5t6CFo1D6buh29e7lQphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwyRiwFnD4rbLUYdm7AJm38ZUIFfLs3UQS9IJ3bF3oePWVlAAi63eQblRuYPg7p2nRqhO_Q1UY5DPzCZcp13MI4-ddw-YfXWM0D4WQd1rhAtDJl8NDKmUzIBIkJgCewV8bKo2kx2wu4s-tndVwc4do5ECq9nuzTLAlJAPwGa996kswmS0vaHI4PZ-sNzT0q_weGJMSPV5YbgJEiSMnSKC0_BvG5cq8mmN8DdZ5sYtNV58QQ_hRYIyXoK81STfgS_UCuDZBNwtpBpKQ6JofmHiOxDwP8t55kT_bNq-yuwXoiF7H5poPcPP0Lw4E29RUrYtIWKKSSUgs0KZlXnmnqpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=n_KSgjB_D0PgK0QmFLcVGEUg76zrzNsbT195vnxfxJNo79jboEpRdxGj7FpAzF2HQow9bnJ6zDEmihZjBJbWypoaSuArS9wNk9w8unHLQd2RRNhemmzv6a9bUoINCzSMWzh2XQiB_MaF3O7d_QlK2sIAZ0_Qciksyxig5UiYyokuSZDnECYRbPX_giJOw7zfXvxJNgQ9gILvL2gZTa4Ct9m2osElySdycZ6VrzPYRtMb_J3UIr-6iK51wEAFdaFEvZrFwYAMwdLiOLudqIc8A8_zBCFZkRZDsoa4YkNQdBRu_jMFfzeHeqoqlxTmq46Rm1QZ-nYyxDZayPnPP0OHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=n_KSgjB_D0PgK0QmFLcVGEUg76zrzNsbT195vnxfxJNo79jboEpRdxGj7FpAzF2HQow9bnJ6zDEmihZjBJbWypoaSuArS9wNk9w8unHLQd2RRNhemmzv6a9bUoINCzSMWzh2XQiB_MaF3O7d_QlK2sIAZ0_Qciksyxig5UiYyokuSZDnECYRbPX_giJOw7zfXvxJNgQ9gILvL2gZTa4Ct9m2osElySdycZ6VrzPYRtMb_J3UIr-6iK51wEAFdaFEvZrFwYAMwdLiOLudqIc8A8_zBCFZkRZDsoa4YkNQdBRu_jMFfzeHeqoqlxTmq46Rm1QZ-nYyxDZayPnPP0OHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2pFKmFkX-N7ZM_LQGE9V9rStvhxXKVCc5O-eGtTH9LOQTSr_D9phOI8IGd8SxJZnOvn5U02Xva8ZXDhvZXqYy30uIYU9b7ujKDfqEiwJlSrtohbGuKPN4j99FufukMdbhcwnxzNbzn9t3tZ-rll8ue1w7OD1NCwavBNNBd7cWzgoSgfZIT9ZDwW_Jgl7z2imX_Ni5nMh35bZL-G3jPxfkcXH0EbEUgTb4jzwmCaI_aObC_3DGG_RIdD5GOWHsAlK2KI1GB1-v995w6S0n6zAb7DbkZOoBpOuEc_PQm2c7xXA1EvNQvzPInFpLO7cqLv8f28EMj3YhuvuWrjUnZGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOyu8b6iTo0SGsS26zotfXiQkAUd3erEUOXo-znq9-ozqNONpU7_Yiyft5SMJD-Pu-bk8cKOvy-qpUIFglczW0gpU3c04a93xFFdGFGnaBUzTf2kaI8WBbKrewtYFenBDH8aiPZ7GOnn5VweRQOMQB2Rkgw1MV_Fznbf9PMokziVyf6dz_oqQSOV1hORUM0pJ2JvudJtfDAyRM9Y7LPAO8NR0v8xMTRwSoEOAVMoHNXqFNudOGmsJ2TD6ZTcXNhyI-eQ6r_Ll7WWL93FvD8IXUYj3PCSLTCR_uNcYv7H45ug9i9TSC7obQLqFnmUeroZVJqa5O7l9h78gSuvCiMuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dzihi224g6zqXTBFVUX0e62jJM06OZfHxsMVt2GsH85yfCSIlPCkDNVJa2lorVO_lvrsFNmfA92i1z0ijWtclmH1B8ZvvaS-V7G8MSx0OtrVVCnYoBgPXGjX_V6_QIPFGq_BjqxSdLNbU2X1-8CTfqqKYUD7XXIHN_x-vdayxFqbl2bG36XbF5NKablD0sP3Y0bQe644cxh6z1YqsnAE4NdZ1010PB2uRbjjWqlSqVuaJOAZXDqH8TYT9ccjBR-SjTSwSB-Esg4eQwfLKB_1GjVxxx1RXfmpnZ3tHCGhjD68C3jPHxWDD5H4M9Xt5WFKdgLSiViGxB04u18kbA8L6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ixesw9JqKUq0vTq27B2rXOTuw7rDlXUhp1e9Wfef_HZ1E_lkHl1xSIqdhTKTojemTdashvVWivLWVaVsNV02Qe6Mr3WqoHO_3GCbmvHkOmBgYcsMRgbXnSHO6EB5CvxRIltzCsdz1X8LI1p1n-FmCIMsAZxUxXXW9v22WkQ6ah1BllZItWYGKzyRt2a-Fk7j2FiUGNjvjJi8zQQipmJSWY16P-ZiREgQVuKeQybr7eQd8dwbIzdiiRoqyT8vI-9tamcfkd7_EYfRwVOLvDvEQNt-E75JV0vBy7jlsjCeugp7He_ouoYjGnSb21pJy9NuvrYqn38hv17C1g_vzR024Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=BGfA-DboLOjaHv0lXNcPxrSnAREwu6z3AQQ0xKD26cjkiQTdkhFTD9qPGYlrTbB9_FfD6-Raz64jbk0w_NI8WCP2IaG3QRGo1B_UE5OGUGXq590JjZR0sHBPvQD3OwYGXS12EoZ2HsuKTOnMGOcnYktumwaOr43cY53JWllEU_fhCL326grSe0tWd_c-CWGF7BbmdSK-2EzZlw78b7kvXkyRfne_E_vmHEaGqdUSgU7TcP224XdMCAfLYsiiMe9TqV-4ujAoVvC4RcaoXgE034lwWS-JyiN-8muY7jDYK4pWHKhyew2FKp3Tiy1HQE0fIWJbqdJkflY-CuceA8__FIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=BGfA-DboLOjaHv0lXNcPxrSnAREwu6z3AQQ0xKD26cjkiQTdkhFTD9qPGYlrTbB9_FfD6-Raz64jbk0w_NI8WCP2IaG3QRGo1B_UE5OGUGXq590JjZR0sHBPvQD3OwYGXS12EoZ2HsuKTOnMGOcnYktumwaOr43cY53JWllEU_fhCL326grSe0tWd_c-CWGF7BbmdSK-2EzZlw78b7kvXkyRfne_E_vmHEaGqdUSgU7TcP224XdMCAfLYsiiMe9TqV-4ujAoVvC4RcaoXgE034lwWS-JyiN-8muY7jDYK4pWHKhyew2FKp3Tiy1HQE0fIWJbqdJkflY-CuceA8__FIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=IO73-IkBAEZ67HCPtH9ZiERevk8L2bGrN22ca0kK1306JNkho5DPvgRV7RM72mGWJ7wSlK0yKLTD1lQotWt_l-A9k49rYJAT_19OHSYyeEXQEHmX7ynSpc5H5EHc_-KmN5aZi41vASzwNBjUXhd9td38kJOhXgX79cQpRFpBNAlJjhKKC6B3zYxy6lFx1iC-OmYj1Zg18T1IJnb01OOqMiZws-_lW4aC7nBnU0Hby-5TTMrebQk--N9aqGxtwDxzD_ikRk6GayjJ9Js08AgMjVu4Pbp_0alURP5782yCsozzHCbVUSC_K2hWn0E0fuNttNOAxb_MLbD4WzHJQu6GXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=IO73-IkBAEZ67HCPtH9ZiERevk8L2bGrN22ca0kK1306JNkho5DPvgRV7RM72mGWJ7wSlK0yKLTD1lQotWt_l-A9k49rYJAT_19OHSYyeEXQEHmX7ynSpc5H5EHc_-KmN5aZi41vASzwNBjUXhd9td38kJOhXgX79cQpRFpBNAlJjhKKC6B3zYxy6lFx1iC-OmYj1Zg18T1IJnb01OOqMiZws-_lW4aC7nBnU0Hby-5TTMrebQk--N9aqGxtwDxzD_ikRk6GayjJ9Js08AgMjVu4Pbp_0alURP5782yCsozzHCbVUSC_K2hWn0E0fuNttNOAxb_MLbD4WzHJQu6GXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qiBAWz4qiId9idt6mw11Hw0jAcwASmgv9fPInks0LAMsES73mEI8aAh-JNyBJB1p83VFWbi0CdXb7uqLAb58nIxvBeT3PTZU34A4-BrNAgtN7mB-PibFxcxhbtqGi-66d-dw78NwAPjUOYZ-QYcE7PgTJkCHps9VRmoPu3ooVYLAFfiZPtUtLpiiBNK91pJYGpZrVc1Y1kqe4uPJ75xYfazsFeGHGUcdqQjn144Ygr-O4uBmwriu9zRLVYXpepI1Hf6YHFdQqWnk12iZ8gYf4zy5bJNVi6Lf9g3dA_tX63-OYVjJE6J-4J7WgTHfi_Fg6kVQBavGOD0BEbC6xCyuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qiBAWz4qiId9idt6mw11Hw0jAcwASmgv9fPInks0LAMsES73mEI8aAh-JNyBJB1p83VFWbi0CdXb7uqLAb58nIxvBeT3PTZU34A4-BrNAgtN7mB-PibFxcxhbtqGi-66d-dw78NwAPjUOYZ-QYcE7PgTJkCHps9VRmoPu3ooVYLAFfiZPtUtLpiiBNK91pJYGpZrVc1Y1kqe4uPJ75xYfazsFeGHGUcdqQjn144Ygr-O4uBmwriu9zRLVYXpepI1Hf6YHFdQqWnk12iZ8gYf4zy5bJNVi6Lf9g3dA_tX63-OYVjJE6J-4J7WgTHfi_Fg6kVQBavGOD0BEbC6xCyuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl46TQEBOtJ890Z_N7_y-mzpgjWZ0Zzk20cFSDONMyIK9K9I-UVV3JoYwuQB-wY5jHvDnU_WHeDPXAoMGI_DQl9FeXekRxoQWv0hodkrX4kkJ34wkfSMHOxAmI81uLZpzCnma27E1TTLX04gmJMwYjeDEc-p0pjlkVHJASP8siucsfhY5yyx_MzFti5YRpSzq05zOTeElLzP_C7E-YJr3Fs1IHZdum9bqZCKcziRHNX2cFjtncwovoS7FxzUo4PPDHgAzneuvb40CmWPYBmeGob6vg38iwbtU5Xi8gjlWyDEpzKCVTsoEnL8YX2Dg23GCOJbHFU2lHT6C264KIzXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=tIXJTHSLi4lhlEaFQeZdG5tv5T6eZVaatFxCMH9TcGH8SgaLi-TN1QpcZHn_qNUc6L_nrwmcojqFLZI-NhGSYrHt-G6oectgaA4NezN-YYJlzeKfJYX8XIMq0ARIMwPtUUZFLmr_WyzzQbHPOpkIq_CILPAxrlwOOLB3MMa6dhDw2-TY6HDjo-_aX_Zvj2yc6W1xUT8Nvfi6rxVM9jf9AFW6QbBi-EPeGIsHMy7R2T7HkT8ldvJUZzY2CcucNamsPqzv4ufirbXniKXkMollDxoMnM_G2xHAUQBQkfKUYinAWu5WzzV8jCMUOIjDHcMcGmZxo_RkAn2umXOL1m4kLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=tIXJTHSLi4lhlEaFQeZdG5tv5T6eZVaatFxCMH9TcGH8SgaLi-TN1QpcZHn_qNUc6L_nrwmcojqFLZI-NhGSYrHt-G6oectgaA4NezN-YYJlzeKfJYX8XIMq0ARIMwPtUUZFLmr_WyzzQbHPOpkIq_CILPAxrlwOOLB3MMa6dhDw2-TY6HDjo-_aX_Zvj2yc6W1xUT8Nvfi6rxVM9jf9AFW6QbBi-EPeGIsHMy7R2T7HkT8ldvJUZzY2CcucNamsPqzv4ufirbXniKXkMollDxoMnM_G2xHAUQBQkfKUYinAWu5WzzV8jCMUOIjDHcMcGmZxo_RkAn2umXOL1m4kLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Qt84TyfFHAOFpcFSbYmMAj3nBMeMyoVzYNb4_ouf6WhI4T_KdyGsUg-L4qjWRUu71AvG4DmYKB8Zi_L4WuFaa_wx62v7vQJzQQMRf5XrxShZ_jy2Z2rwd11PzIH3d1sRVVr0LUpsWl9N2LTQ9CAX0pBdcOIAhIZkI5QLAwDHh1J0lqqe1tpkY50WrsXP3kVNge0IRWpobeglx7d6m0I92TtW4dXARIot-5y8tcDEdXmXx9n4nDSzv0wVL1O7yaBQzvcJhmrZraZn-RUmaI_Kylr9AG_zoKsdQ0PjTGmKNP5pmQIWiePpb8eU_jeP1ZDBTvDnC4BRMwdmtpT_sO-7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Qt84TyfFHAOFpcFSbYmMAj3nBMeMyoVzYNb4_ouf6WhI4T_KdyGsUg-L4qjWRUu71AvG4DmYKB8Zi_L4WuFaa_wx62v7vQJzQQMRf5XrxShZ_jy2Z2rwd11PzIH3d1sRVVr0LUpsWl9N2LTQ9CAX0pBdcOIAhIZkI5QLAwDHh1J0lqqe1tpkY50WrsXP3kVNge0IRWpobeglx7d6m0I92TtW4dXARIot-5y8tcDEdXmXx9n4nDSzv0wVL1O7yaBQzvcJhmrZraZn-RUmaI_Kylr9AG_zoKsdQ0PjTGmKNP5pmQIWiePpb8eU_jeP1ZDBTvDnC4BRMwdmtpT_sO-7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=I3cVBwB6JR3r-pTxdBVJGtscXytCjskAvR8M1iRhGYL8JlZYdBSbTooLzXRPvxQumyEtN2gaTYM_QJk1LTTyCnoz3eU_0B3Z6RDdjSefgCMGlZRy1co_aE_o58fRSedPvw3py3mbsYvc4rEjIeaoZUn-p9wAfgKxGONFS_qi88lwI7nF0mn1jR3bZ1_bczV6dhTFMHdHbFTC0oJCW-P56H0mxsaBfdxD0IKECYrOAh3NWqeLc5VyUKILcu3wbP8rJIFjaMH7fYU9EPKdMxhlpEtVsiyoMbJm8oiSyaXaxFYi-_YclPkzxncTTK0JGf3Tg0fU2v5bXkA0zPcjQjKAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=I3cVBwB6JR3r-pTxdBVJGtscXytCjskAvR8M1iRhGYL8JlZYdBSbTooLzXRPvxQumyEtN2gaTYM_QJk1LTTyCnoz3eU_0B3Z6RDdjSefgCMGlZRy1co_aE_o58fRSedPvw3py3mbsYvc4rEjIeaoZUn-p9wAfgKxGONFS_qi88lwI7nF0mn1jR3bZ1_bczV6dhTFMHdHbFTC0oJCW-P56H0mxsaBfdxD0IKECYrOAh3NWqeLc5VyUKILcu3wbP8rJIFjaMH7fYU9EPKdMxhlpEtVsiyoMbJm8oiSyaXaxFYi-_YclPkzxncTTK0JGf3Tg0fU2v5bXkA0zPcjQjKAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gtb58qKgDhCIrwS_-ZSAO6c1BzsnrI1JCf6u3yXzfY4l7JsykOTmErmxdiSVplZDaqZNE1tKz4Ll1u7GuHJiBo-SPYGpfh3mGooT9XL2pn-GMUM8wsUoNrkLVWPu_WuUXWojd_v1kj7SLxDtt7jW3VHez8z95KDW6w0ah0aOycSOaPNWqF5jE4qCg5b7f5XY5aBrA2VZjTP76DBSOrCpG8bIoMhzg5gbLNfzUwgsKk9veg55_52nSmve0OMWc5ymofrttQ9qFFBrITVB6h4kxJ6_KdW67c-uPqgcWQg119Svo9FzuUQup2VUEk6OhkqlgSkIif-N-xKwOYBBvmeksHQrBqIFNi1NEV6dt3dN2pLFJ4UeXe1CKlf4BpdD8jtfiFjhavvxUdJKD5Y_oI1vH45a_FKyxhHLLhB9aPTdxGTiYVYZT58XrMm73tdFcE9kkaj0-uXGpY3_71s1ckJlBB5-HZIBkdhLM6QlW0rXM9mEFezd1VLviZmvy9ldYg92w_HU6UJMSfKnPRgE2_1D0L5G50D5z0ihz33xVzszprj13xT6LdEBV3ms9Y2qzGbimAmYwYuuem5eT93QwMpx8abh1oIUs5ZQuvHYnvU8KqmCeV4H8NJ7UG0Jg_RRjtc6Fs3NQrtPt1Jfio8Tf36H3tZDprhLxO9RPY-d2gVQE3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gtb58qKgDhCIrwS_-ZSAO6c1BzsnrI1JCf6u3yXzfY4l7JsykOTmErmxdiSVplZDaqZNE1tKz4Ll1u7GuHJiBo-SPYGpfh3mGooT9XL2pn-GMUM8wsUoNrkLVWPu_WuUXWojd_v1kj7SLxDtt7jW3VHez8z95KDW6w0ah0aOycSOaPNWqF5jE4qCg5b7f5XY5aBrA2VZjTP76DBSOrCpG8bIoMhzg5gbLNfzUwgsKk9veg55_52nSmve0OMWc5ymofrttQ9qFFBrITVB6h4kxJ6_KdW67c-uPqgcWQg119Svo9FzuUQup2VUEk6OhkqlgSkIif-N-xKwOYBBvmeksHQrBqIFNi1NEV6dt3dN2pLFJ4UeXe1CKlf4BpdD8jtfiFjhavvxUdJKD5Y_oI1vH45a_FKyxhHLLhB9aPTdxGTiYVYZT58XrMm73tdFcE9kkaj0-uXGpY3_71s1ckJlBB5-HZIBkdhLM6QlW0rXM9mEFezd1VLviZmvy9ldYg92w_HU6UJMSfKnPRgE2_1D0L5G50D5z0ihz33xVzszprj13xT6LdEBV3ms9Y2qzGbimAmYwYuuem5eT93QwMpx8abh1oIUs5ZQuvHYnvU8KqmCeV4H8NJ7UG0Jg_RRjtc6Fs3NQrtPt1Jfio8Tf36H3tZDprhLxO9RPY-d2gVQE3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=EIzFloTJM5nXWaG7XN4HwMD46fmK0BfWavzdv_WIIgQKJ5KXo30qHDClZO0KjsEXu3FuEL1LSNSYbQcc4shkYH2sL1OUqyBa43g5oPlfEYctKTQ5EEVEFo7FMw8dFegblFq5XopvNnPCkealG_tW84IbMRcO0wL0kPMYZ0GwfmjLgi-JKxmvQzwxaHlPqOvlkY1HdHQ2ICo6GTrlEKxpwmevfplAGbbAk8y6cABLMOEtnDH_KGKsXbZnrjlDMBtV6OT4JyNVb8xWC5okRAWtrYRtV13XN2CPVB5g32pv9ZHCBXP3K7Eyp3dQQngBXJC_ebGh8NQAw1QTyClXOsbB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=EIzFloTJM5nXWaG7XN4HwMD46fmK0BfWavzdv_WIIgQKJ5KXo30qHDClZO0KjsEXu3FuEL1LSNSYbQcc4shkYH2sL1OUqyBa43g5oPlfEYctKTQ5EEVEFo7FMw8dFegblFq5XopvNnPCkealG_tW84IbMRcO0wL0kPMYZ0GwfmjLgi-JKxmvQzwxaHlPqOvlkY1HdHQ2ICo6GTrlEKxpwmevfplAGbbAk8y6cABLMOEtnDH_KGKsXbZnrjlDMBtV6OT4JyNVb8xWC5okRAWtrYRtV13XN2CPVB5g32pv9ZHCBXP3K7Eyp3dQQngBXJC_ebGh8NQAw1QTyClXOsbB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Fz_isu_NCro5KqiN8i4H7F1Sp-MK8z-ALnNgZdseo8xRuPwFQun_Zf6C-Q9wazJA5V4Nu3lKZhDb0er2mud4H0LRa6KXL-5f2tWK5FnlDPOexCLNgfGlDyjktkrNa89eyifOm5iPwCyPyEqmmr1xZTaGkXhgoVKvlLsyF1KMrBQd6WCXU06ThxyJge953RMbydyjzKJnPojFUozPbBDMd-_a6EIGH8TnbF9AC55ZzV4aAFM8ETXo0IoYrt84uUHAQkR6WMgPS60VKDaqe4MJla1Ve5Q4PMHwkDy8x-aanXLbVswODva2xE35ct_wiFZ_V1fDNzMHdGrK7V1fZTg-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Fz_isu_NCro5KqiN8i4H7F1Sp-MK8z-ALnNgZdseo8xRuPwFQun_Zf6C-Q9wazJA5V4Nu3lKZhDb0er2mud4H0LRa6KXL-5f2tWK5FnlDPOexCLNgfGlDyjktkrNa89eyifOm5iPwCyPyEqmmr1xZTaGkXhgoVKvlLsyF1KMrBQd6WCXU06ThxyJge953RMbydyjzKJnPojFUozPbBDMd-_a6EIGH8TnbF9AC55ZzV4aAFM8ETXo0IoYrt84uUHAQkR6WMgPS60VKDaqe4MJla1Ve5Q4PMHwkDy8x-aanXLbVswODva2xE35ct_wiFZ_V1fDNzMHdGrK7V1fZTg-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbZndCKv1sMXLX7yAv1ArrL-yXTzs4itUdDQ08MOrYM62Z96BhRUyugDYHj1JyqJo7WgfHcctAvxPaW6VL832sLHXRHBjE_eYtictI3S9ImhgiJwHySCM841wjHSzFq2NirzP9tJY1knG1WVlT_X7prO8wGJqdto7AO6EAVrcDuABz8lV3aI7dHghgV1cMUCFlDWu34sNZGWaQWyGbwHiYSiZ1A3ZFeAU1dP2TpHuklSFbi4nCAnuEIELAp3qK25z1JT4WzYPVsdzKiZfP9lwg3PwpwGmQDVAU2pYDYSTrlRAOJyZ1i3tHbT59fUHogOdVEc_R3kYBYpDw-ZLHzSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVqqZ4KwEKSDd2XgLPLgjLvbweWGwfBGXRtsfNVZhKiWUHG75MPYHjk-cCaMkL4lMdUKpL6YW7944ZqSl7NmwiD4QqiAYGv16zEXxnDWdiDSKBnWKUdaVipht4lGf553UOXPZnMFPCnVh8bxHDkSNcWWKIZMCFudGPP86Nls940GMt_jp6_zmR0B0x6kLDQJEcMdvm0p20eMhP3WEgFEOXGlSmkdb7STxn6gchbb9kyrIN75AAGQcJIxE8FDJDgb-hoqX9c2M6OASl3EiBMBFMeVZN5t2Tk7cGiuD7OJ0-FktQ-Cdeb4xVi4SK7gJZ1XAGt1_F00o1kUx1ClZMBzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=g662LBlTn0_EC95TX-QPHW20NY3PChZvaTOBimB_xxp0EpjHQOdkNKfX98QyZcoD_A2hCnGGWHQ_FMt2QgkPstTBMCqOBYifIH2JYXga2NwvKe_fjPNiAUKkOLrk9YFpwX9lPCvcJ87dH7eMB776mA7PNyRnJfx9_euWCGBEUJtJXl1YWz1Qhjqbaizmi2NXnGy6pqP_P81qom7uV0x4RsHPelX3Ybdyj2eVvkVNJnXNVUbGiZmAlESrq72reGU09qIoTAM8WdPwLjjmcb3nJCDY946PQY_8Q6pl0d0PYen5r9xpWvq1w2nWJ8A6f-7Mk7V4oZEcX9KsooN_uhB49G7sPI0u0vv_9mjesA-m0xewKOkhD14s8ZduwSs561HOsxcX-sQxp7ncdCgAbXpPcihuj5Inc2YWXHl7ed5zxFdatX90yrO4qugj8qq9Ftwj9OGrZUXTTip4m9uw_t6epa3aLcQXiKdggqZAaYXjbWYds900yKzV7AGK10H8niGOJtl48oJ3dc8iCFAw2zq5795_Ui8UO3r06PS_RGJ9Doxuuys6O-u7TVrHVjxmb24AB_uIY58FJVMtx74_A-sQ_XhAg_VE5uW8lAPceWj1b4v53Bv6exao4i3k1BisUZo-mlcvDz0TofFo7pvVgKIpkMrR3gxqH5-kE1rZyyJoIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=g662LBlTn0_EC95TX-QPHW20NY3PChZvaTOBimB_xxp0EpjHQOdkNKfX98QyZcoD_A2hCnGGWHQ_FMt2QgkPstTBMCqOBYifIH2JYXga2NwvKe_fjPNiAUKkOLrk9YFpwX9lPCvcJ87dH7eMB776mA7PNyRnJfx9_euWCGBEUJtJXl1YWz1Qhjqbaizmi2NXnGy6pqP_P81qom7uV0x4RsHPelX3Ybdyj2eVvkVNJnXNVUbGiZmAlESrq72reGU09qIoTAM8WdPwLjjmcb3nJCDY946PQY_8Q6pl0d0PYen5r9xpWvq1w2nWJ8A6f-7Mk7V4oZEcX9KsooN_uhB49G7sPI0u0vv_9mjesA-m0xewKOkhD14s8ZduwSs561HOsxcX-sQxp7ncdCgAbXpPcihuj5Inc2YWXHl7ed5zxFdatX90yrO4qugj8qq9Ftwj9OGrZUXTTip4m9uw_t6epa3aLcQXiKdggqZAaYXjbWYds900yKzV7AGK10H8niGOJtl48oJ3dc8iCFAw2zq5795_Ui8UO3r06PS_RGJ9Doxuuys6O-u7TVrHVjxmb24AB_uIY58FJVMtx74_A-sQ_XhAg_VE5uW8lAPceWj1b4v53Bv6exao4i3k1BisUZo-mlcvDz0TofFo7pvVgKIpkMrR3gxqH5-kE1rZyyJoIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms7cqLLgvXoSqdLGVaswbKAMARZKJkib2wVKP7fttOKLrCic_i3q1DXPrSR1erS2TFs52utl3PGstGQvUcnRqSu6fJWdqkuquOIeiV3-hSzFF76YQ8Fmub45zySGIwRvF1x96bvYGsSjkl2j8k_WM0VEvzRKtDAJigA_aXfoAUQ9z0h1kyZZd9PoO_JURixPe0BRBMP8P_LGjdLFiseQEF4h1yTxyR5jiFF5KehiIB7VDf8n5O201FQwk02cenp8Ka-DOd7aVx8zdPCBA4xjhaYPTGbWGBUKbHUjPH1kkwEs-pHY6ENTnFkzvepsDWNC7-7lOXvo9VGXLRUgO3qQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTzyqLXSYaH7ylhgoMe5WA_YLO2jkUniqvNoJ6hZrE0KBuf5RFWZ9i6NX8tnC-5pCJ79aExU1CQu50lpfsGBm46ySr5mM0jQapaHkuIRDv-YYIU6OG2YMnp5cQmow6G1SH0TmM9Fyr7G9zlhDm2dIFBo-S-FPfJIRfrIsYdeIhynd0fWME48oz7lrXFFQCcAtUdyFDTFmRzO-pctc_JCqxOew3MeMx12GQNDYml5BDwem8UoV4W4-3E-tlrHOZ31jdSFFmT5CL5aE5o98pylHOTZ6U7EhIgxdz7LVqRglxaVzVXCHcGdeh7JlledNQignQ-AaccEOtortHGYNrYLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJj_K0hXk09MaVyUzqf8b_X-cLetLfIAlJhN_oZEqYAKCTqniZ5DkwnYR4uwT2XrSPJuu5TImu3GaOvoCl81dLKr9hD5Rpfm0q_S54rdcdr-yBoUwFp1HqPHxp1lLLggfKcjjY2hRxbG4EmHV67HQ7VmaniCcN_C6CrEtj-sYaQb6Wa7lQ7BMHTLF6H5f_9xdv9Xexd5GSl_OvbeD7gFWihc4EnVUJugf-Imvm0m43bIM-vPsfRzBtDfQLyg0xhHDw-JjXQmHmHtzr4p6pkgnPNnJPziggrpVKEIq-j82HIjcniZ72_hjF1zUBgJoerJqwkR-AD4wZk__sAmeH1FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
