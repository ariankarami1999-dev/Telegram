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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
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
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPQyGH8jpYnRAL9R48M-KPomIqwFEfm8xxGE9NouHKF0COHm2ICGgQ8C4eiCdYFdwt5KtgomwtKDoRLKVt4UNpc_lE20roMAft3OAY45d1Mii7JSdNAAedLmKO1B-P-V6wmMEaqU3SGNE_Puf0er93daERFYGOqI4GXSYh0k7YCaoBQg1xH6tFKFT6RafB23MgOda7OUbvRg1Bo-OVdfsGUd2QkGvELMgFtfBD7ir-7B5Lmx8rZj3UnHEgp-UzfDQpOX4DJgZCd7-Zl6R6O7JxaiHV59Ys9lXth8lfL4hOH9AEFsrlrk8OzUmhqd3Mz6WTczlW1Cj29q4qAKzWpbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOG_oRMQpDHWHMeFU4q2aBzdwqo_O2F2L5UnlyuA78XAzmXZTPhOYfT79kxFTfOlW8KUCpU_RZ18CcVhnZ5K1Nsgp_NQ9RD5RnL4TjbqPg9hy267BrTfUYjdWTF59_1Sfbexevruz_EOm9Hhw3En3wNucv8LQLqLSMOpSV6IquHkQYnlZvVskeJmmpQ-rwsWAGH9J3Xkxhyc9LgPP49RwJ5VsQ4H6OW00zU0Qny9NlWdXOIFVTn1zYK970g5jyh5qQO3HpMiY8JMHoM0Ld2EaM3-7kbhJJXRyRJYZMMdCckDQbvCO4fwKTw8r6WX23IW1WuTu5TMASpYJ2dyacNTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W52eMj46vnisE2tG_PXu2a24hZ4mrhBYyoif1FJY2L69a7-AGl0-cXByYEHa4SY8UGHvsz3552w83E3IMcpyxGojY0PymDLa45np9KNVQmoIJgKk0UPyROdZ-Hv9lM6QD31HtqaVJ1v4i7t5n6N8cE8EnROCRX6yYHq05R7p0oL6hnU5j9K5sr_B1KVUkIcC5tpvVuQMvBNJ6cauDHkI8F1QLzOPXtsT-FYF4i8xYJHIL8zX-8-XtOXafw4uUaYSf6KxsPXHiaMQzJbOErX53DMfWiSkBLymusIA2uscC2knWkDi1EjcHlmu_zLI-zhlG7e_-5TyeNKwwspszFMEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqhy41eOK0R74DQxLLuIDXTFH7NZE6NbR4P1rON8utB_lMYKP4dlHEZNptZvWMJ4GljuJgvvJNC2dNw4WkUnyLvDAt1Jls5vJq6AvRKzJDZU8012c8c3eOIrWU0b1sny2S_OnCPUjwENi8H3XSwaeTAHOfCTSsYYWsodx3PNJgmupxQvMX9QaxkBobKcPN0Fxml1r6TMFEvud1ovBWvRxKuddWH7Oo4jGEsEZfzHfpge6hVWfdpK_QRH7b7a9Oe2NtX6D8aFQ2N2gdoJXMh__gdvmQ0P5emsSThpCN72moa9wF-FXFf5jfaMbBnwdllJJNlI0_CWyRwWE_Uvo8dw8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1h1g02NvM4DwOVL73PhKzn9jGlHk8n8mpyKVt_8U7j10dN3HldkldIxFjowDRIJUxPI5_peB2Si_fM-4UbzbBuKf-iNMmJnolPa37sw3aV0vngevtULtfSaDUrqPBoG77NPnw02BpeFvQW2dM9AdMZUTZUDGO0xtMOX9cUinGh9wX90RRW_2GxIpyzS6V4obnHNovsVrxkNr39W_hsHwWVTAY7TH1MK6APsvblZAVJk2yjT0TAWFIKI2yrXAp9Vvk9ZiNTDAJFZS4DcFZDgwcaDIQQXT27zhkIEA0dYctNzXCqw5f1nVupU5PC7_ctxNAg-kbJtaVbj9QuNSqU87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFhqNuPl04Ah_5bb73Y9yf-vfRt7Y--LoUnfmbQXvuAq_Lbv6JQnTmzP20EUsU80TUCIwXOKeLhxpRQKWM84LoyxKiAJEba-5mJUB-Z8Acj3Lk0i60yuw-msq-olehxi-GkBLb7y-krtqSa_FurvvRbFa1YrAf-z0nR0Id5J44_mb32dXmkNsk8nAUGZb1yyJD5QVum5ZE6TBKplaIMqOEPiDH5YhrfT1C8zlTyGmZPiduBNKs-k6-5TrM0_i7xvJXQNFUOz5t5N3k0CsSaRPnpehlDgD9NP9m8w6MWyNRcyEOyKuAOlPfZS0AVk7RwKMt6zQwbZYQOi9y-C_eRRZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox1lveio0Sf4Iz7NBktJM0lQgOv4u2tE-domLY_CpEtAU6ZhZ5TnBeD4ae0Y3UVZ-edkhPizHJKUSY00XWzN_Jc0Hs9-gj8IXZG5BFdSiFbAUaZ1QiC9dIAV4FJymZ5PWfkLJQBxVDRpXyCo_KzlI-WfyyNYBCr2gkC3g1UHn0NKyebPD9vNz6ZUZQw-s2t5heD-SUj3UuTD2cfI93pXaT5WYRW3id9-kp4-iq9x1-G1MAOPnpoxrIkp3xUkiELTd2nk9gneE1Qg9AwpId3e1u4tDLAYy-dpI_jxODa-7psZmNgRnbM9Ls43SLnSaKElYFnVwtmRXa3iyJame50dCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qciRBBu8Ou-b-LphRA_QiKiLVfSwqw5hcyy1e1dHiVGPg7JOX2hV6F18eS0pZF0mkhmtrdbkp2Rt7if3nwZEdVDdthsu-lUeWFLBGAUzk74rRLI0F8V4Qqw4YRFTxWjrUEAGTQaSNF56pnI3EIN28i86qgwcy8ra52rXzgHNFS1vPAbG0QuPAyctPpkArMUUIEDv2pX6iae6BUAsZ5AXwvkXlqC3vCYt5bhFOyq3XQ5R0wCwNSPZV3NVqXh303M3zG3_0qsc03I5MY5wvwXaPGNTzbuU8CiAkrZrcKirBqklXxFuZw1KbeTsUE5QHj2s2lULE9miwIVNvtFMSyANRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=qciRBBu8Ou-b-LphRA_QiKiLVfSwqw5hcyy1e1dHiVGPg7JOX2hV6F18eS0pZF0mkhmtrdbkp2Rt7if3nwZEdVDdthsu-lUeWFLBGAUzk74rRLI0F8V4Qqw4YRFTxWjrUEAGTQaSNF56pnI3EIN28i86qgwcy8ra52rXzgHNFS1vPAbG0QuPAyctPpkArMUUIEDv2pX6iae6BUAsZ5AXwvkXlqC3vCYt5bhFOyq3XQ5R0wCwNSPZV3NVqXh303M3zG3_0qsc03I5MY5wvwXaPGNTzbuU8CiAkrZrcKirBqklXxFuZw1KbeTsUE5QHj2s2lULE9miwIVNvtFMSyANRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImJZyGoU6GOOze4F3l73fl4ZQBgVXLwWv4LfXuerC-ojZMzTPR4x5B-jF1xjgKwpPgKjTbTr5NbW4XInGv448vYKq3InI1xMA3IpQt5KxUKp00ol2plKHqKrK3ZClu24D_ZFZ-W4xBpUO3i4pzmZz5mgKaTl-NJVbuC5-cQXA3PCEVfNt83UTSwucxY_WvXLCULwvTgmwG9jREBf6eWTTAM5eH7V2LwNEBfmyt6D90nszoEKOmzPnrhPxMW49y8DxT2CHx-EihLYbJQD24A_0ZkYQWNLUui8X5HJdNIuL01k9Z0KGS0L4vwlVCKuc51Lenmz43G6r-40PCuk0C9DGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CloxDlupjzPa9fE5beu9wp9KakEttAGgwsqC02c1D2-BFRecY7-P8U9WwwLpToncadz8IzuByPLJ4xAAah3tJtPWlCMBgAct1XSMDjhcGztaofuNzBQ62BYhmYqKt4JHFonzx7kGJ6ToVtYa1iMnQ5iGM2NeLhP1-DxP3f5pNKmPodxGbk1yBNK72nZuecSMQOYbXY2Ux2z2--MUO-Z23EzzA5SxivjerQ-TEcK1qeqb6v2KNBz31X0bFalNWvwpiUOUaXsdlWPcoILlPo5Ewurr4dcPnch0dX2o0MOhskr4yKdG8moQB2HJ07yu_vYmCnNToJcSG1pV6en9RxpoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZY1ZU16Y2BeBif6s2NFLXQ-T_Pl0cUMOGb3VLzeHVK70o27RvOboVtDJkTWhMSa4r5uAxZgquf37btNQ4_EDfEVyx0Es0pMtP9SlMlnJDRnMEvcYw_XkViHwUPCh7ob1QkbX6E-RGjxo2tos43MH6ixNjFhetV6EV5vnoyic0-XiubW3cc7WVP0Jxtoe2mUV68P_x6C1ZGAuE52wZDpet9SbQ6IF5iTXDasCDTFD0RrZXIVqdecVdhNFLje0XOv_IdrUtmQurqUnDuoJj1Omu4abl2noECY5QZ5UL0B9-ee1DiOA78yhLkOjnn-zsEfiS-6YeKeOwZXdfxKup-87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=DhHau8UXfnqLFlGX89kMvVA6TQu0WH9tOtW-1NmjQI_d1spDh6xTo4X9U6J-86vwQ7N_liZxTrj8Q_imWvczqracszPPOiSOTp0MPhkRIAi5hiG5uPeWU93GYJR2s7Yl6JgtYmPje2fgV1cZKgYTAvXMo7K_ig1KGZWRNXJUdrTMNnasVBnNiiJSO362uo2W7xIOnYkmj6emI-wUorBy28vGO6J_VJM7DxRdExBrzQstCffIXPC1vkQWW1uw0-4bL-mEp7gmnQl5pvZlH52VUJP69ivGzKDwxdd5bdpQuP7A_Jfki-QzkCY2uZEdcOgWguNh6DJqKHh11MBt2BPP9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=DhHau8UXfnqLFlGX89kMvVA6TQu0WH9tOtW-1NmjQI_d1spDh6xTo4X9U6J-86vwQ7N_liZxTrj8Q_imWvczqracszPPOiSOTp0MPhkRIAi5hiG5uPeWU93GYJR2s7Yl6JgtYmPje2fgV1cZKgYTAvXMo7K_ig1KGZWRNXJUdrTMNnasVBnNiiJSO362uo2W7xIOnYkmj6emI-wUorBy28vGO6J_VJM7DxRdExBrzQstCffIXPC1vkQWW1uw0-4bL-mEp7gmnQl5pvZlH52VUJP69ivGzKDwxdd5bdpQuP7A_Jfki-QzkCY2uZEdcOgWguNh6DJqKHh11MBt2BPP9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_xx7Z1gg2D6Zo3QFNZ9zoxPiDVRj2LNtzIqBnDAMvYhLtDQTtoYpLphdgY2roD_Qdmh4rQmD5UDoUpkP1WEQnCXcY_69Co5OO4uZ4Z7LuISl0EZH3jOb8gCUfdvTKXOBIqFObff0_Pi4PddTTQ2SrCfo-b4LVHYgtzqVV7yNeCtSee6OZ2nbZxqWYcgYuFl81_RdRdeTtAaUj5IzeM4aortUIYZuagRocrwOz6F5MNc9ohgjur91sMsiLPja-eEBgg4Ln_NZOEFgBNcBGDjVxHW_ciaxpLQx-Fc5lXO6p-vF9BUN49afPW2_DzsA9jRb2JsZtOcgIvdCsGXVxxhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=HmUA6yoLPeqrr0sF6v4qXJHs1utt56S1COdRX5sjShWpUhlON2KyrEmwgtAPRv1Ku6yymymZgXUwzrGchH-6jM7Cl5BRGY_sFeuPTCPD_1wt-LE0qpW_PsMCqgalnHlIwMSFUlvtatCfmtnWwA8CxxVa4yubBSt5x2U1De1r0tv_0zvUtstlMQVxvKrsAY5KFNKus-Z8_fjeXykxJeTgY5sULs8dNWn-AZ3e7LBX7UDXQSO3reC6ZyWhg-cKnZ8WRFXIE1UDbhTzeommvzM61pOODhlV_G-KLRGhWYw-Goxx53T1vGwPxkEcZwhqfUzBZKAyUaaBJlrd4x47iREitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=HmUA6yoLPeqrr0sF6v4qXJHs1utt56S1COdRX5sjShWpUhlON2KyrEmwgtAPRv1Ku6yymymZgXUwzrGchH-6jM7Cl5BRGY_sFeuPTCPD_1wt-LE0qpW_PsMCqgalnHlIwMSFUlvtatCfmtnWwA8CxxVa4yubBSt5x2U1De1r0tv_0zvUtstlMQVxvKrsAY5KFNKus-Z8_fjeXykxJeTgY5sULs8dNWn-AZ3e7LBX7UDXQSO3reC6ZyWhg-cKnZ8WRFXIE1UDbhTzeommvzM61pOODhlV_G-KLRGhWYw-Goxx53T1vGwPxkEcZwhqfUzBZKAyUaaBJlrd4x47iREitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqRRxGxqf1WKZeAMTjo3P8opZ6__cH0GfSYKwOGqmmS_JKvPtnQNby2DzvQTwtJNNbGynDDl3u2nnVQ4pz2h4_nsFLRB8dQuMa25Kr3rfUOYCJT49PqIjDtu3Pq7KM7E_J7pf3FkcM9hGBJWzeONZTXQge36P2AhKeb_s-pBTEihLbawU_ZsQdq1IBqeIcTaOuyWpk9kg4U4SgEC2DsLs1lOzO6RemdYAX-yY0ubO_-4H60L4n7578XtPGtQYXFNR8_GkE_24cJRuw66hMUOiIWxHEUFDdPMjtn9-OVS_uAtvW2HoldgSF9pGAhnTQO9Sjrufxdz1gKIzMcxCLS2FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhUaj3ae3MshQqYHTfQMLUULby20YVnu0CvrRE3u6ADUoiwtxb3zdkSt9s0bqg1TxDA7ORMtGt46-lfPR4dH6MeBt_1UNl4i18SHQFWF-OGt5dysvLIG_DTjoS-qgwSe9i5HajC_1uOAcEVzjeZeJN5QbFumuNL6rISTheI6dy8m8aKjoDypRLkZLNjtE7_Qpmi8g_F6Rtf8kGn81BJhhbJZU0wv8EszobCNEy3Kjq5wi2Oa3m-l0QmGOR9Ma5XwlifwYgZm7jA5hGRYJJpiep4om9fmEXcMO9otPPnZpY1Jc5DBVcTQ7l-5l1y0Vs8tlztMDnc0p2LbD77rOldUoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=hu9wwNy0FLhNjoW6HpWkoZ4Vk7XcinN7hiV1q4XIB--GgXTrw1K84RObH6y6k5mZZy_AQAI4s9JbzI0ipzZdSkQNFty7ie7477G0CU3lebl4gjcGi4t3eqWsEicUyNx6ycxKxC-G7I1yjJ_1IXXTXQxF8Nyo3kdUySv0k52DP_lhiRLgbZLboRuIQ1jqKzZxqXA6peL7x2khgJ1fRuHt_vx64KY8wvi9hOWcBs2B_Ul9AygLaBgrM9OUuQOYWj-d_Tx-fGdUudTxIsiTGOkc9GMfVAEFvejrJsVnmhOCfpAo-7d0NZdDL75uIMH8v8Img7zMUEesyKr19q9F4rR33FrIk4bkXFlneFbNesHq9Ng_g1cGWaYZ4Y9nVYvBWDI6L79hUJljYqlJuk9wVWIxAOZb01XhznIYSvRCTJt2hSkyMfx_vk-CJq4hpAwHNVn2887j0PO7yyHzslPe6dldKCAtkagxnGeM80sopOVljj_3QD5OLPmLqQBocE_l1bxsrzKJGAD6jkTJ3iBEQu-d4pNmq9J3zGTs8bJRHorOifghRvXGtiKkG65YCaEu5uP5Mu6L_KFwEJXBwDio_Y51VTiVm14uaXt76ElGgAwlzp5yWUSkqxWPg9Lf3kr60Nqd3JkAnND5F58s4ViXO95wqqSaUDeDamM9OfOswLb8z60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=hu9wwNy0FLhNjoW6HpWkoZ4Vk7XcinN7hiV1q4XIB--GgXTrw1K84RObH6y6k5mZZy_AQAI4s9JbzI0ipzZdSkQNFty7ie7477G0CU3lebl4gjcGi4t3eqWsEicUyNx6ycxKxC-G7I1yjJ_1IXXTXQxF8Nyo3kdUySv0k52DP_lhiRLgbZLboRuIQ1jqKzZxqXA6peL7x2khgJ1fRuHt_vx64KY8wvi9hOWcBs2B_Ul9AygLaBgrM9OUuQOYWj-d_Tx-fGdUudTxIsiTGOkc9GMfVAEFvejrJsVnmhOCfpAo-7d0NZdDL75uIMH8v8Img7zMUEesyKr19q9F4rR33FrIk4bkXFlneFbNesHq9Ng_g1cGWaYZ4Y9nVYvBWDI6L79hUJljYqlJuk9wVWIxAOZb01XhznIYSvRCTJt2hSkyMfx_vk-CJq4hpAwHNVn2887j0PO7yyHzslPe6dldKCAtkagxnGeM80sopOVljj_3QD5OLPmLqQBocE_l1bxsrzKJGAD6jkTJ3iBEQu-d4pNmq9J3zGTs8bJRHorOifghRvXGtiKkG65YCaEu5uP5Mu6L_KFwEJXBwDio_Y51VTiVm14uaXt76ElGgAwlzp5yWUSkqxWPg9Lf3kr60Nqd3JkAnND5F58s4ViXO95wqqSaUDeDamM9OfOswLb8z60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=cPbdCU_oANQTaNNZ3yTPxniPDVnx2FCC53noLd7uDKs8bB3tpElpT60voaLQBvoBLTnYponZ_k06-zZ04TpfUUknsoP1krpZ3K6AhI1cT4xi7YAC7PKgpIlmoK_5UMQl8xNdxX74wAqCTGmwYdkCNYbKy4YAj2_zXZxDvEt-IKkR6V8RcQQMzQ5yYzHcg4lOzGlLqaILsttPWo9cNhiBqWboMotyE_tVzUS3XT-xqxQfQIaiK6FlFvX5J2WwvCapahSqgwwVPblJc-gwz-DdlQNfool9JoP5BVRpEJnInL23qJHjtyy944RLpXsUcXh4Ed-xQORQWRiLTaae_hvZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=cPbdCU_oANQTaNNZ3yTPxniPDVnx2FCC53noLd7uDKs8bB3tpElpT60voaLQBvoBLTnYponZ_k06-zZ04TpfUUknsoP1krpZ3K6AhI1cT4xi7YAC7PKgpIlmoK_5UMQl8xNdxX74wAqCTGmwYdkCNYbKy4YAj2_zXZxDvEt-IKkR6V8RcQQMzQ5yYzHcg4lOzGlLqaILsttPWo9cNhiBqWboMotyE_tVzUS3XT-xqxQfQIaiK6FlFvX5J2WwvCapahSqgwwVPblJc-gwz-DdlQNfool9JoP5BVRpEJnInL23qJHjtyy944RLpXsUcXh4Ed-xQORQWRiLTaae_hvZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG2dp_PUOjnZuIxmbCK-qXJx35bLyMKGt3b3ep3I6u22EQVQhFOQS4iABaIoIei1DUuNoRwFh6hv7WNRpF0cZdTMKTmnZRrUV-jV1enSyFgK6qVuAbPuQnNuJApKeklWhctKcx1VvBarwxM5lE2W9teXHH9maJbT_5wb28v7oJ8Akxl7lJxa8f4E6pURURVuwLKA6tuSYTqLqUhFH_BOE9JzeyDNadjUFWtjZ6kJG6quij0KqNrw2sdyWs-FDctt1GhN4pQ28OL5Ut8XX8h5WOezHReXfLvdVLWixzwxwLLUhb-3PoHFOHYcgXB0wm27cEPBRAdYQlFOTCjsJf2ebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=dQyP9yUVzbseXlDPLNrP8S5q_MuNtRH38N99p8kqcjdCbToxzFUFUTLcpZua6BnoyXVx_dcmCXmukdI4zxYCk3WXWlVT6rfKTYtjcAdz2gKH1OYTk7KfUjHN-MWREasWQtfqz1nrydRbRSpHiKQFC1c0QxJ1REQJ-24NGli7xWRrXsGODJt1GxAhN2wknKRFqWxx21-AjvC2J3tlgPsEMvYjnNSr71GDuh5vuGJZBQumHKqCWANxR8z4rxxT2dLYjIvb1KekGBLynP6Rfzb7pcUErZBvRkWshyb7YaFUdR98lL7BgDS_nSLHmX8V8vpYgs3nhnLY-0Wn1FpoUN9Y-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=dQyP9yUVzbseXlDPLNrP8S5q_MuNtRH38N99p8kqcjdCbToxzFUFUTLcpZua6BnoyXVx_dcmCXmukdI4zxYCk3WXWlVT6rfKTYtjcAdz2gKH1OYTk7KfUjHN-MWREasWQtfqz1nrydRbRSpHiKQFC1c0QxJ1REQJ-24NGli7xWRrXsGODJt1GxAhN2wknKRFqWxx21-AjvC2J3tlgPsEMvYjnNSr71GDuh5vuGJZBQumHKqCWANxR8z4rxxT2dLYjIvb1KekGBLynP6Rfzb7pcUErZBvRkWshyb7YaFUdR98lL7BgDS_nSLHmX8V8vpYgs3nhnLY-0Wn1FpoUN9Y-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftDBgKmooz5aUVs6Niwqhets16wPmpdpG4sZbC2uGXqU7C4VNuCO4JyTGXH_sSIHjzulaywfZcn2By9FbWH9bOKyCELnDDy7UxF3ZXk_EDUwR-MLZcxljVc__AHBhh6DbtFOHD-VX22Ol7dSlyvCURaUcvq1S-inbsmAgGNgWQBiuJMzPOMWQPcvJuqhzLIy9RmAPjMG-9Fp7duhhUfyULbpX_sMx_VWTG9SaoD82UdaFYoQDUCItDa-UqO26bMrxlkby9ukzyWhkf-lyGnwG7y4pgo5RI1PKxZ710tl9ozsfYxRw9m7EPTNxpq1JTsHGZg0flOq44bQM9698ahZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf5-s5dKCYU_SG9mZdKxqVpWj1Wbx7n4mjGmCegXy1a6GPGa7W3uhWEW0Rnku2VrdoVbJFMqxgaFYY9a8sR4NBfeEqqwGMcKWNBZ1W8xq08fHDgaYMP277D_8mXDVhtcB-KBZQtQQuwzLzpqyO3OEWmTPr-tQxsRBha73Z4QjFQWcd9cox_CR61hO9c8PXfqNSWQUKeu8QBM-fFL0ahg4XkvcrNLrRlw65lsS4xrZXVB9sF77TExtzts2A_MGE6aueGwHPU8PdzYdi508VPJv0w0Dfpfkj39J8aedmpxd6JiJWaeCZAVLv7gsSpiQ7amwDMPAru2OxXQxbcJwWbaqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbxtyFSMGQxz1H4EkZwTS7YfN7bze9NSxy1dFEantzlv83mNSyQn9-D_D-tLP3nreFpEGK7WSH_iduHEHTRVLs6QCFzD0V9TdMkr_tIPL6wE_bLVzTqS8xbAWGY1y01if8BaiEeq3MuozPD77bcDqGgKUYggJ2JDTyglcYC13huKVL2XYjQtbM_pG3CWThrpiWIgEYG9z_G1u57z8Pt4TH6VbFee35zGcgXVWtkPjaegD7GImtl1L9wYgkgFCIHt4_w-OWWDByWGErx9lsL1MfBujoJOpfVAU0wNtfmZK4aNgVQRp4L7bCqJEngW_mhPvLQIArwJ6ovfgceampKBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY6VG92KustoNL-4ECZcraNbsz-pPbmrgu4N1nx3UjAC9WlQEIRDPE-EP8DlvV4vWLoAGmj6lnTRfyk0_UTi4zrJl6nkIzYH1SU6z0lw3Xq-nUBXDL0s0U5prKwNTMr7bx75oiZLnzI0MMyX4v4uy9GnmCdRznENe2KaUEB3rfP5iH_my3vifFwDUuF6N0Wy7cvOXtofB6C7nQv6AZzDd--0DlugHUYeyfKxl84ZuNEOUoloIVtbJUf1vnYX87oO6JMWl2_5F28vv9W7aIQz7wENQ9zLoKWzQLiBCdKHRXxO6WsVA5m5ZwR3STHe6E2Yd4lyd5aUzaIduoIjxskKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrOdEffr2DZ1r3x_uNIlshyJCw7y3s3I3BavtSrFWdCEDP_FwJbuckC-6ph9VpjeBUYCwR8vK_2NaNT4Zrev6H6O0wX3JAg4O9CuNR3lKW41G1oQFf2s1L312wxBAFOqnlCP_dXt6S3qmIqo8gkiPnDbwi7v6SDQPOKvAuGFqLoAvnCC53QvQ6s1KIY0kuW2osBgt8jKHLt8jfIQ9PEIEJ8JeoMoNOWC4bgoCU3vbGh-TZWaOk3IihtDT2wNRQ0xkR5qYeqLw1m9GZ5ZC5D-xKzCD9FgkzgX_L-lBt7uXwt9fawsEOWNtqb2D4armUbpHIei76Op2wGnzH1udFCYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Dpwu5pIgEdLf2xw_tA43QRGkj9s7Idg4PdsxqG5Q7UOYNMln-kHIb0evqepzyjT7uS0bEb7InUEcOVpecGcD6itQ2bBM1cu9Y1YQqi4myrf0kl8b61Cxq-0z-V64X2uhEkbK7FBOE4hPBvRVAopqPPs8YyD3upryf73xs-jQmvedS6nJJOWhEnGLPj1cB6Am3GFhPW6hBTXkdopiR0WBMMVHGpbmwHUlhTgo0kLxBzSmva-Mwg6dlAF_3ZbpIfWNrhW7ZzWZi-nLOI6TPLV3SD2yBSunD_gUpOfq8U9D3fsJsJIMF4GZzmqG0GwCRG38H5FeXMqf1YiWqAeL7pfuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Dpwu5pIgEdLf2xw_tA43QRGkj9s7Idg4PdsxqG5Q7UOYNMln-kHIb0evqepzyjT7uS0bEb7InUEcOVpecGcD6itQ2bBM1cu9Y1YQqi4myrf0kl8b61Cxq-0z-V64X2uhEkbK7FBOE4hPBvRVAopqPPs8YyD3upryf73xs-jQmvedS6nJJOWhEnGLPj1cB6Am3GFhPW6hBTXkdopiR0WBMMVHGpbmwHUlhTgo0kLxBzSmva-Mwg6dlAF_3ZbpIfWNrhW7ZzWZi-nLOI6TPLV3SD2yBSunD_gUpOfq8U9D3fsJsJIMF4GZzmqG0GwCRG38H5FeXMqf1YiWqAeL7pfuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6_cIDwXZJZxSMiw6icf9UTUMuWCmLv-eOvX9ZHpgkhZNUfdXwsYY8hTGYEgw1ieSIXPozvnEq9quUIRucLcJDYxHv_22cjH83SQI9xL8KftnBQkhOayFk2SDoAZpfaCfJSUgSDeDBb5vAKNOmL8YRxDM-3FIFnX3_slGxyGcAobDpADuS7BihPAM0GckYefuJU4roh9KRouD3cgJ6VzvixVEYjVfCvjYK6a9QlXglgSV136HYL-2wRvNIJ0iLPHlOKQHbyw_u36fU-q8PZ6iX2BJwxZSaINiDnlxN7Q14ygffkzo4GlP8KxVHbsWR_MXh9FykslCHqoK-rlYjz3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWrzY1Z7CiDKpR-pmbahNtCA8q86K_dQt7EkRG7yOxElDLCUr_0zP8BfK97Mwj9vj3gnT915YbLU9BY35lVX5N-YYxs_qsAbxHakeGJwXfxCF74_0BiVOE9__Of-f7KTNNHZ9D5EBSYoVpjw2lXYnKP1vVjwRLs1v8F_NUwjZlFynQr8Fa5eGjL0QiY2SeIqRtkibAAwyA4HEmGVorsU5l_McXbEeIcMUGVeved0jkm-FdMc3yxtrb2ieKxpIlohi7k0tYiwqP2SbyKDN7we7iaXTvaLLnEG12ZZ9Xb2UDLFUNiDS8uMGsMq4ajJ7ZFKpRsD5A5xJZ2HyAkNeSTZjg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=tBvhmBWN8SFWGBZCq2WEU5-G2DBqhwMiwv1jTI-iIJ9h4mmZcFySW3L5a0zVwblEgFPQkDZnn1yW2whOt3qyZ8p7SWheDUeo0ZO-zIyKG4Gy3ZgB9NPS36f4jV_8SgFZDCuJvkV7F8wDtQHSqhIoQdEK0LQxRw_ZuHUc0NvUC-jXkyJY0DFQ1j7Ly4slaIiqS_VlO0-OiiTtEe-ejvaP7Lv9d9lWN-9BQrJsUfDlL0MKp2nt39TRoiTBVeBjXS0NvEIbTgMvrY7Rfga9hzIXdK62ec7SzHOLkeQu_4eJWWe85JFM-HZb2JT2YkeTTJX818Ixcc7lcDs6p0hiU5NdIYWNdYbZqTJxAb6jHN7nUQc_lCs-IlJbNoS8IN42Ya28lwCLUyuq9n6-ZWzY2KyLogdud8V7unG0d1Pm0EDUN3pUjzf8D4S1H8QBAnX9CGc3FCmOUC4KIdPAg2Fqpg3r-wFAMWlkVYO1l9jIekE8xFFVtPdmB_BT39yVorldfmA7VJn1jDlC1IEaShm_FznLUyuoPt4KOoCHnfeZnNm2Cz62dsossaGkBuOXL0AD7NNbfaKF-AC8-b5qY1Hm8spzPy9iriC9hE46tFAUt7eAlYxJ-I0rNlNsHptYHIYk81MvNxTHhGW7zKVokWtI8gdPSqhW43I6shGiUazrXHlR5O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=tBvhmBWN8SFWGBZCq2WEU5-G2DBqhwMiwv1jTI-iIJ9h4mmZcFySW3L5a0zVwblEgFPQkDZnn1yW2whOt3qyZ8p7SWheDUeo0ZO-zIyKG4Gy3ZgB9NPS36f4jV_8SgFZDCuJvkV7F8wDtQHSqhIoQdEK0LQxRw_ZuHUc0NvUC-jXkyJY0DFQ1j7Ly4slaIiqS_VlO0-OiiTtEe-ejvaP7Lv9d9lWN-9BQrJsUfDlL0MKp2nt39TRoiTBVeBjXS0NvEIbTgMvrY7Rfga9hzIXdK62ec7SzHOLkeQu_4eJWWe85JFM-HZb2JT2YkeTTJX818Ixcc7lcDs6p0hiU5NdIYWNdYbZqTJxAb6jHN7nUQc_lCs-IlJbNoS8IN42Ya28lwCLUyuq9n6-ZWzY2KyLogdud8V7unG0d1Pm0EDUN3pUjzf8D4S1H8QBAnX9CGc3FCmOUC4KIdPAg2Fqpg3r-wFAMWlkVYO1l9jIekE8xFFVtPdmB_BT39yVorldfmA7VJn1jDlC1IEaShm_FznLUyuoPt4KOoCHnfeZnNm2Cz62dsossaGkBuOXL0AD7NNbfaKF-AC8-b5qY1Hm8spzPy9iriC9hE46tFAUt7eAlYxJ-I0rNlNsHptYHIYk81MvNxTHhGW7zKVokWtI8gdPSqhW43I6shGiUazrXHlR5O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=NvgXVyjVrgau-hITugDKMKcwlaWTn_9q61jlB9-A6f4Nb-ghSsTPi0OGCNwoV2KvyqdRpgZvPVHHl0VSpf4OeQsGq49RqoeJpxVyBiLngCTCtq8hb8phwAMOPtk0DKLTHiiFGH-IALHWJH0FHf-ev15sFd4WRIRcKMLdM5Jz1A9xExo5Fxaz6ZjL9v7DLsQqPJy16E9tX3u-E0M1A-Cqbg2ZsBKS8FmRlsW0CdUFvLSBFdgl1KUfgeqTB6x6xPzW6N3D8BE4alxDnehIvIl3Nix_qSfcuilwXPwCW__quE3orbj3bOvEZn67Xdn6aKZmwENjTPflnedSUgyVdi0eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=NvgXVyjVrgau-hITugDKMKcwlaWTn_9q61jlB9-A6f4Nb-ghSsTPi0OGCNwoV2KvyqdRpgZvPVHHl0VSpf4OeQsGq49RqoeJpxVyBiLngCTCtq8hb8phwAMOPtk0DKLTHiiFGH-IALHWJH0FHf-ev15sFd4WRIRcKMLdM5Jz1A9xExo5Fxaz6ZjL9v7DLsQqPJy16E9tX3u-E0M1A-Cqbg2ZsBKS8FmRlsW0CdUFvLSBFdgl1KUfgeqTB6x6xPzW6N3D8BE4alxDnehIvIl3Nix_qSfcuilwXPwCW__quE3orbj3bOvEZn67Xdn6aKZmwENjTPflnedSUgyVdi0eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIqUzqvDrEionQs2LAmcNkDYt1Y79guas0fGG9pjis8yzi7r4LEFR_BiProcSi0fa7eTjMRh0SL6k3oRlFyfXuRwgugdGREDQpL_S3ZdNeSmUBSwMLJ9DuXx4Rg2XdOeOZdFAj_VJ2QCSoyRaEoiD84se3OOUJvaRtxNLMx4M7KFlSVkQP935uTW6m384JmxlDOWTr5z-93gfoLWmNoKVSVpPkUyA_20Z1CYpb62w_hvaj3ASfhdMzWZWvOK2pH1DzvIaZtorj5l8Lcbk-HzVhCwPK0aNdnJdLT7JkUwjONY6zLxkuc85dvZzlMhBDxWeHNnbAszhFo47q2SMdmNHF_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIqUzqvDrEionQs2LAmcNkDYt1Y79guas0fGG9pjis8yzi7r4LEFR_BiProcSi0fa7eTjMRh0SL6k3oRlFyfXuRwgugdGREDQpL_S3ZdNeSmUBSwMLJ9DuXx4Rg2XdOeOZdFAj_VJ2QCSoyRaEoiD84se3OOUJvaRtxNLMx4M7KFlSVkQP935uTW6m384JmxlDOWTr5z-93gfoLWmNoKVSVpPkUyA_20Z1CYpb62w_hvaj3ASfhdMzWZWvOK2pH1DzvIaZtorj5l8Lcbk-HzVhCwPK0aNdnJdLT7JkUwjONY6zLxkuc85dvZzlMhBDxWeHNnbAszhFo47q2SMdmNHF_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UST9EMcEnDnULlVw2XKvX5ndRacBCUu8v_WkqSW3XcInxLFvJTByVM9uI-jQfXP5jd-zlGgdbXznMI65ZBFBBuSpkqdtYI3P0R4cbPiRzUdGdVd_7qewtJ25jeQTh2Zq3wckJZ42eiiZiY9CgRYhuJid9pcDIUx5RnaVBNx7_8l541VcozdumKkwe_chU8ZAD9Yaba1XTr2lTN-6slSHJELOj76kGpPPi-GM2HuGEipDk4ffC1TeGjLY9nXpWSQHVYEPrjJWuoBqGvjwG7ZUL9ZEDp1uUtYHW0hKlJUQQaPjVlSzSdIlIIECohoCK-0fTvOVbaR-OHn6IAnnAhtGMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su9uA5OwjAs_dLIzpk4Z4UNcct4poQVFLYwMFDcQA83l40MfSiOWHJ-DLpUD4c_iQ5lXWiEykSUemto8WlM6z7u-jO_rF4_o3aln-nDt43FzAW81Lh_cUWiQ97W--oATM26jCICy6Mrmy89F7N0KBwXenswPt0bMkO8vFNhvhSSmKLLmYJilm0c96gtJJqOAgIKdOucC45VpcYz6it212mYOatJ9RnVwvXP26ykU0Qeyl1Iozm415zdZudpx-ilzoHYG2D2tib3clgkwEUXdEAAcLTYvBjyj1_zv4wdbpH-QPrBf9bjU8ACHCNN9qM1dnwqPtO04uWKNXdjVLjlQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmSEBxX4GBxhsW-ijYkRikJPDRZAH3gYWngiq19QWaXva4_ELbabiR7oP3CC33Aj9EWkkyF7oe2jhc7x2MSfTi_QTVEMPPL-Cf4ezgpr1RCxH33pkfZD4-keLkpStwz1HSWALRVA90NcTfqTyhTHkM9b_pNAYl858andoiUvWyb-4iBeoJsM4nzJMyxso9LH1SOHpyhsxYzyxE1Omp1GQXOWAVrNiSRbTi5hlikYlSlz6QLCYDM43JVRcN4N_jWjEx-UuhBevwISbBXALsGnWSbLSjdJF4xuS4DsmVSqxdik8L1JkncnOrNIwHlGvh7czaUsMoBj69-LPq76q0Xk_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=TY21ognYdwubHgEtMBKPoOM_pWUTC_UiL6d9PB92OaGsoFmjMxTWW-gOcAhNt-KkN6EPoHWojWsxN-U81E4EBoqUBWyFLPm5Pnoz1HJ781JNaxjskgC8ZMThZtOiZR-hP3RTrQ0-fEvP6sQZcdJl_H_lpkQsMG-S4g6NZUJBlaqNvULCksQfvw4npG7PSG4SL9Ch-FygXTcaSCA43xUdiVp8LKvXvBYB0zLyfMgDXHCVhRpOAstD0sfYJUh3OnxyGIFq2GDqNFzMoN6xboOIMtMUptvVW_3Ua1WqQQnjGRA7xOGVq_Sd2Dbg3e0f-qfIlRm8KzUE3uLnYc2X3l8WKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=TY21ognYdwubHgEtMBKPoOM_pWUTC_UiL6d9PB92OaGsoFmjMxTWW-gOcAhNt-KkN6EPoHWojWsxN-U81E4EBoqUBWyFLPm5Pnoz1HJ781JNaxjskgC8ZMThZtOiZR-hP3RTrQ0-fEvP6sQZcdJl_H_lpkQsMG-S4g6NZUJBlaqNvULCksQfvw4npG7PSG4SL9Ch-FygXTcaSCA43xUdiVp8LKvXvBYB0zLyfMgDXHCVhRpOAstD0sfYJUh3OnxyGIFq2GDqNFzMoN6xboOIMtMUptvVW_3Ua1WqQQnjGRA7xOGVq_Sd2Dbg3e0f-qfIlRm8KzUE3uLnYc2X3l8WKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoMasQ_moaVIyUN4brBMn3F1C9FwAFHbWO80eAnmLMQToCWy4TG0--kJtlDRQpj9ljMc9LWZWlDE8ozktmLIf2MC1qyHQSlnS7xsdNggb9cKA1kM0Y-D8b112AK2smdSZ1Al4BdGXPMlZVaQ0FlFIXu9Y2qZzPcG67HKN91kbAIxvmyDjGSvoIwyhr8It6nHhcGYfHYXk03BA7-yIGWGzPDhRp4xfiCGJe6CUUwvjd-4-fSUncXnJCP3B6by-2IItkzqX3epSk8wi7AVjrboJ3P8VgXZDJxffP-R5Db4W4mn2ddX3pqwQJIxTLpxL4CQV4vHCY0x0lPFlyO7mSvKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f634sH48DsJefSt2VWT0hBWrmLUwZnfqnkNAsyyfw0-GbZjaPDRJjFJ-c0sMsc68YQfcvyPeySpOug2gZfnZyk7I-6zxD9K5Kw-B71exUUaQLgB4K4PtlSpE_9VhTWFv-gRkuatMtsPVX492BnP8pwNYnT0_GNXYAS5JlYq4rBXWUvAOdRWBxOeS2sgIYgWd2jZALZwVEgPLMGJyk7uqRhtipV25bjoBw7fa7Mv__kc6IjfhihHFdIedB3xmufTnYOvbuRoRm0q4T2Qze5Oisochghh6gAtnhJ5F0VtTfJxLjp2Ux3xYSgI1I9Gz2e6RaUDdksFxWFekP2Y-xKS2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqRqlEkIIT3IVAShD9ODoC9h5JPH9WZ4JCd9tZZuXML5M1aTXahdutx-3vTfgzq_ZH-9hXQSo_OCIs3R6N2zDCoFZ1q7OI4-EWsrpb-dAp4j3boeye61mSZbYHqaD-c7FYIY4DQvgc0IRhs5YjQPRjVuZ3UrIMqss9gwo5cKXnjEafN8ydXhPPb-Yys0milSfFlC8aK3YlHEQSmKtlW8FisnP9MVWWbJ3fh3TWW87b4FS6bgQ4MmvvKpgE8R9yxhch7mQXf7DSfXEWQAnEEYHw8YP5vCSejqYcE8713ZmrqCyFwfirG2aG1EKcUb0iOie1uiE87GxJcDadhy_X8_5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBOnTjyza36zH1ycVcrq0BKzftw14vsEYuqdjRl540wHaCXrTRIWow9bg6JTEM2l5sb6a8Oc5VlksOlMduW4x5IifEMpf7dEeRI-9kekRd_ZDN3Cg0vz913W8W6JaG3PM0Tb8zaOnAuxuHml3g_b4bfS_aPOhe62OC2uz5rvJ1UxKMJtiS2A7hmS-ntO-geRlO4yDtUPC26Syt4wl8cNb0FVLEnipGD3zhPOJRfNQjXtZHois3aDyEYezxLuDwB9U89nO0DIVLPxlJX3k2VSncJy3dk5LL7wv4qL8c7XFF_yqXhrK_nKxY58ToGtjmcGRww2maYUI728_1qmTbYqmg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Jt-tt5S5wECbjM7UL80OvKyDL2OfixJwimF32GhvRMdbM_JFNiqhBk74Iq_tAkWSfruoih_pwLB29h3QMbOEU9WrCgBiZGHUhT9WDlYWuUJCpINJeURx3SZs7LW2HyE9xJOMmrEhKcVZ75rRKREPiYkiIrQaAld74fib-zqnZLQCZrjF3Ib5EAhH1wBcdwzxtkyeUGV_fkDI9EAP-PbZ5UHhNBfT3j2DLPB7BkPTXTR3s3Wsc2E8b6_vrvG14Mg1zLo91jmpxV8N63MBzNybwQjPYL30LPNdZzrO6gcEmTDhmLTCorsTZAvNAMa9gQXFlu5X_iyEKkwQgn8zq1oxvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Jt-tt5S5wECbjM7UL80OvKyDL2OfixJwimF32GhvRMdbM_JFNiqhBk74Iq_tAkWSfruoih_pwLB29h3QMbOEU9WrCgBiZGHUhT9WDlYWuUJCpINJeURx3SZs7LW2HyE9xJOMmrEhKcVZ75rRKREPiYkiIrQaAld74fib-zqnZLQCZrjF3Ib5EAhH1wBcdwzxtkyeUGV_fkDI9EAP-PbZ5UHhNBfT3j2DLPB7BkPTXTR3s3Wsc2E8b6_vrvG14Mg1zLo91jmpxV8N63MBzNybwQjPYL30LPNdZzrO6gcEmTDhmLTCorsTZAvNAMa9gQXFlu5X_iyEKkwQgn8zq1oxvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=t2LFcGXsrKA1L2_bVtNAKkiXsDfJipZ1szJnkpYC1NKG9H8JxA7yYMKSgWPNNQUiqsbK7RL_Dff_J01ty8o1m8WJIZfEVSeCe2p47Yr6uatupxsqfEuulNOeoRA2yDquZPfTHh__Tm27bJNusl9HV3QFLROJhnbLDz9Y5AGp0-hl6msxmw-Ju2-UYQOoPm5fGyOem6ZDHmB7V0l1A8dl2cBPgipYwdIHNKAEr49pSMVEpZi1J5eLuHhMMhoEEaHd509Iggm7bHwjiog1rJbliwTHdXeDuOtKnTmKqAYgJEXwBH9HZfugWloIBocD1mMkiS0_im7CbHj4PS5mzOBhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=t2LFcGXsrKA1L2_bVtNAKkiXsDfJipZ1szJnkpYC1NKG9H8JxA7yYMKSgWPNNQUiqsbK7RL_Dff_J01ty8o1m8WJIZfEVSeCe2p47Yr6uatupxsqfEuulNOeoRA2yDquZPfTHh__Tm27bJNusl9HV3QFLROJhnbLDz9Y5AGp0-hl6msxmw-Ju2-UYQOoPm5fGyOem6ZDHmB7V0l1A8dl2cBPgipYwdIHNKAEr49pSMVEpZi1J5eLuHhMMhoEEaHd509Iggm7bHwjiog1rJbliwTHdXeDuOtKnTmKqAYgJEXwBH9HZfugWloIBocD1mMkiS0_im7CbHj4PS5mzOBhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ObH2yxVBp9m-Gyd9rIb10La9Xwr-8AktL6XUQNO9GJRAm7va1Pw-fumUHAJAy3C_P0fHvRhrFhrTP-wtdgVHrRFj1GwEr6DuMhUuHnUzpBU8s0fJYNKyQBC9oJMFVJ5BkUDY33gd-U-7f88r6rI-YusNKFJe9W9VfCgLsipc2OQ_b2qzPsNeozNtrCxkMHe8_TmrR02jR5IMVvA9OZ0vOuJJBUd1o_C_poE5s2u5MQUmRN_KAKlNuh3hSgTvC4HVi71dLc7Ys3eo2r6T239dRC47373h1cqNBuG4sRJmsybY08T1zOF6fRR6qpwne0Y9cBQZT8sd6YPAJ2fUue1cHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ObH2yxVBp9m-Gyd9rIb10La9Xwr-8AktL6XUQNO9GJRAm7va1Pw-fumUHAJAy3C_P0fHvRhrFhrTP-wtdgVHrRFj1GwEr6DuMhUuHnUzpBU8s0fJYNKyQBC9oJMFVJ5BkUDY33gd-U-7f88r6rI-YusNKFJe9W9VfCgLsipc2OQ_b2qzPsNeozNtrCxkMHe8_TmrR02jR5IMVvA9OZ0vOuJJBUd1o_C_poE5s2u5MQUmRN_KAKlNuh3hSgTvC4HVi71dLc7Ys3eo2r6T239dRC47373h1cqNBuG4sRJmsybY08T1zOF6fRR6qpwne0Y9cBQZT8sd6YPAJ2fUue1cHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emsMNe1r0215YqXLPt_-UmO-flPkA2qWeHF7uE9v3q0vHaWB6BQh3R-6IQ9ahRB6uU-HOeT8vu7HBvhxoQDptJBCgjBU7Ji8smDYQQRO4emuO47Bt9skiFsCW-cRHWaOLmkswNWqlzRUIYA5-JIGrn_s3WB08sQEmyUMZDP4MwkGUVGBqZfT5N6DHGJ6tEf_KD_fmqCKTXchuIKJl7YFRpXPp3oIjgRFh68rb6EOKh_Cbbn6ePNokfJI-Kjr8mQaVxlo9HL8nWmUopMjLWMHEbkth8XuKSoRkMtGzjBQE2pVcwOdKIcxIrX--AV7NJmJb1Ry53zUo_jh6TUg2JSr1g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=I1ozGbJo1o6WYgEZwHFaHZ3o31Cp5CKHuAAYJQgJcIhhlOB_uEbfIUTUV1RRDLEu3wU3WUokJpMesOvXXAoyqdfOxs9u84Nw3VtkwhEFkFGYwdav494PwKmNzE5shZhDsQNdPJo0KcnWVOLyYE7uHhJX6OeyMN5_LsxyUCbU5OxRR9Bnb71r_1HEz5B78m4yP-_LpdsJr6gRE5DQ7Ol89LWu5E341yLk3TE37RY3m3kfJhCtRSZTRGUHNrKmMoX9rVlxX2BFKSB5UaQlqs-zoaiIZxAVIewMSvxtnBwDyMDjYk5vTqcbgA6qQIach7ydvGLSpQQTQSwfIudKM6NbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=I1ozGbJo1o6WYgEZwHFaHZ3o31Cp5CKHuAAYJQgJcIhhlOB_uEbfIUTUV1RRDLEu3wU3WUokJpMesOvXXAoyqdfOxs9u84Nw3VtkwhEFkFGYwdav494PwKmNzE5shZhDsQNdPJo0KcnWVOLyYE7uHhJX6OeyMN5_LsxyUCbU5OxRR9Bnb71r_1HEz5B78m4yP-_LpdsJr6gRE5DQ7Ol89LWu5E341yLk3TE37RY3m3kfJhCtRSZTRGUHNrKmMoX9rVlxX2BFKSB5UaQlqs-zoaiIZxAVIewMSvxtnBwDyMDjYk5vTqcbgA6qQIach7ydvGLSpQQTQSwfIudKM6NbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=nTBoqyAY8T0ODXhV5XuTmrVTdGDbWrNiCozHhWYR8e6dtEwQAoeKdWYHmRt38zTkrPBezoiS06a-R1l6IDDuLa5Qfw8_5jt96-NoU9ds4G22FqttjljPWoHML015DORNFr7Oj8wUoYeey0xxzvY0sDgB2jz8I8N-X5jNglOvYv5SczEqGDDEC_iCioQYdyYRGgtOAc9IriRvG97ML_HPvvPTt1o8SZb0l40MNFHRE3ar176Lfz499QwKr-IZCp6RoLzcPXpTuWxurhIlCsRujJHof_-ZBCw8rJRFHDZcQHk9C4Z9jGYc8OhDO-T09rjXpbrwHwz7okVn1gfDw0tlrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=nTBoqyAY8T0ODXhV5XuTmrVTdGDbWrNiCozHhWYR8e6dtEwQAoeKdWYHmRt38zTkrPBezoiS06a-R1l6IDDuLa5Qfw8_5jt96-NoU9ds4G22FqttjljPWoHML015DORNFr7Oj8wUoYeey0xxzvY0sDgB2jz8I8N-X5jNglOvYv5SczEqGDDEC_iCioQYdyYRGgtOAc9IriRvG97ML_HPvvPTt1o8SZb0l40MNFHRE3ar176Lfz499QwKr-IZCp6RoLzcPXpTuWxurhIlCsRujJHof_-ZBCw8rJRFHDZcQHk9C4Z9jGYc8OhDO-T09rjXpbrwHwz7okVn1gfDw0tlrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=XKcsBbrJW38Ui0P7ITzd3GneL0XaiagSifxriYBKfiUYfU5uYOb_tiFlBM5jQxu-KMBWOioms7iEwDJ7FwU96vIf9H1gY9lSogtnyIgfnS0wRj2A6jp9_6zWoj2Par2y6bo7-oK_pWIBh799eTyFQ9_MIUJY3bIGbPvO8B4ylw7RyLx1L7JFOIk4jrXzyUCtDUhhP6DFlt5ATIhguelgqR7GpiK4-ak763F92R7M-Cy3ZtfRb1mBm1k3aRJ65VDICQWh4DNGUqMwfvQcIIwcACVU2ZEJE0r0TwFfZ2U4x-iKddnUAoATX8ZcCT8q7BPCdG8P60PMDy2wTDP5Jw7ClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=XKcsBbrJW38Ui0P7ITzd3GneL0XaiagSifxriYBKfiUYfU5uYOb_tiFlBM5jQxu-KMBWOioms7iEwDJ7FwU96vIf9H1gY9lSogtnyIgfnS0wRj2A6jp9_6zWoj2Par2y6bo7-oK_pWIBh799eTyFQ9_MIUJY3bIGbPvO8B4ylw7RyLx1L7JFOIk4jrXzyUCtDUhhP6DFlt5ATIhguelgqR7GpiK4-ak763F92R7M-Cy3ZtfRb1mBm1k3aRJ65VDICQWh4DNGUqMwfvQcIIwcACVU2ZEJE0r0TwFfZ2U4x-iKddnUAoATX8ZcCT8q7BPCdG8P60PMDy2wTDP5Jw7ClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=sKOweSWmkqIMXtO7EWoWAOtYmlQYRVwozboUvxZ0VI4B8H-8azvDstWKilPsnMzgXx1uhwQnqp-K2gOeXRRzKLex5q5AqpFo6xgf7lQO59xkmWo2qz3h6sAT7FIxPdcXn3OBvUXJOSun3PcnorVXbCbCFJgtGrNLc-_zhfN0pukvdBJaZxyOUxrr9Fpr6aWN-kiaB3Ba-qpb0yPSoWb3iRRNszjZEjfPCr9x0ohGLI8EhArsPOK0V16m62xAW36v194w8aotuHeK10GVHjvvZZBKDlnzgo6gb1Lr7o0hl2IZHRQ5iqTSOToI1QPyGD_p-G-OWBHY0F97nix5n_DpunSeUBJqb6_8f7iQvTMZyo9pkCvzL2G2HdenI5m-Jcol7SEW13dpi4fSzkFsRN02fSu6W7TYZXXRBlcXFqV39hflQvqQVxrhjgOBHORcswVEhLumSC0QsxBS7BGRnosDGzjEzKWvHeEx-07RDyuq9AMagoEH77N0w7NfLFM3QYm8kYnzHt4tyhVmIdaa79RdnNFCvvAQAY5fnlWdjWyiW7TW0a9SCqhCqeovwDSk4YhXDzRwhhHMt6O4oh3xZgC_GyHnR4SrD0Xt8SRdW9Y3U58N5_aPd4W__VFCHzePk-4n0obt02TSJ3NXZJO_SpYj8FNN9sJf8U8EQysYSmrGKM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=sKOweSWmkqIMXtO7EWoWAOtYmlQYRVwozboUvxZ0VI4B8H-8azvDstWKilPsnMzgXx1uhwQnqp-K2gOeXRRzKLex5q5AqpFo6xgf7lQO59xkmWo2qz3h6sAT7FIxPdcXn3OBvUXJOSun3PcnorVXbCbCFJgtGrNLc-_zhfN0pukvdBJaZxyOUxrr9Fpr6aWN-kiaB3Ba-qpb0yPSoWb3iRRNszjZEjfPCr9x0ohGLI8EhArsPOK0V16m62xAW36v194w8aotuHeK10GVHjvvZZBKDlnzgo6gb1Lr7o0hl2IZHRQ5iqTSOToI1QPyGD_p-G-OWBHY0F97nix5n_DpunSeUBJqb6_8f7iQvTMZyo9pkCvzL2G2HdenI5m-Jcol7SEW13dpi4fSzkFsRN02fSu6W7TYZXXRBlcXFqV39hflQvqQVxrhjgOBHORcswVEhLumSC0QsxBS7BGRnosDGzjEzKWvHeEx-07RDyuq9AMagoEH77N0w7NfLFM3QYm8kYnzHt4tyhVmIdaa79RdnNFCvvAQAY5fnlWdjWyiW7TW0a9SCqhCqeovwDSk4YhXDzRwhhHMt6O4oh3xZgC_GyHnR4SrD0Xt8SRdW9Y3U58N5_aPd4W__VFCHzePk-4n0obt02TSJ3NXZJO_SpYj8FNN9sJf8U8EQysYSmrGKM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Z2IC9sew9ieYmnoFDSRovwnfiLAdRnR6A4B1PI3CujBtLF6EANz9C5tUmPb_Z_CnpQYFEtQwKPGK2fz2Omy80wpg1F59jWsp88rZ9Bc1buKFuhbI2H4BD-lbJFx-JCwKxqjnd3lCCFgy2tpDfb9bnmthouAx7vt0p2OG6l4tr1C1qmVFuqCslhHwOApyiqiwNHwBJX2U0W6ZgyxMiOBMUWKh3yg2tMeDD83A8ppCLlQ4qeyitHjrYh28Y-X_4A_mG-hIPviphY-MzhSCciC7no2ZLl2LyvdkzmXlcypYAu288Mig5Eta-shCNilueHqY0tsLrihbgM6v0uHAHWLBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Z2IC9sew9ieYmnoFDSRovwnfiLAdRnR6A4B1PI3CujBtLF6EANz9C5tUmPb_Z_CnpQYFEtQwKPGK2fz2Omy80wpg1F59jWsp88rZ9Bc1buKFuhbI2H4BD-lbJFx-JCwKxqjnd3lCCFgy2tpDfb9bnmthouAx7vt0p2OG6l4tr1C1qmVFuqCslhHwOApyiqiwNHwBJX2U0W6ZgyxMiOBMUWKh3yg2tMeDD83A8ppCLlQ4qeyitHjrYh28Y-X_4A_mG-hIPviphY-MzhSCciC7no2ZLl2LyvdkzmXlcypYAu288Mig5Eta-shCNilueHqY0tsLrihbgM6v0uHAHWLBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=pTccA_eddpNSQH9txQKkwB6ObyeutQQq9kBVw3VhkLlZhqu77CACsuwSPb_Bt2rG_j2sfnLXNuWbUmw2Qosch_ILMbGON46YkotxngMLc6kUj1y_AW_JrTw-3w0LLYfh1WM_9K6Cq3tz_gkbAZLRIqTldFp3lD8aYwOZMz9i6fgrm9Gqjd4H_o35Nfnuc5HO2GAIfmha3Gdj7-LRG-TK6z7gXmEzL_FAIxQAQmbo4eyin6clk6SJgErw53HCrE5O00quqNzLEuiivx7K7IFnfQx3ph07QLOn0-8G001RA85uiyKgpoCB6gdMNh41E8ReZ8wIJuSNNOs8cvbq4MVwyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=pTccA_eddpNSQH9txQKkwB6ObyeutQQq9kBVw3VhkLlZhqu77CACsuwSPb_Bt2rG_j2sfnLXNuWbUmw2Qosch_ILMbGON46YkotxngMLc6kUj1y_AW_JrTw-3w0LLYfh1WM_9K6Cq3tz_gkbAZLRIqTldFp3lD8aYwOZMz9i6fgrm9Gqjd4H_o35Nfnuc5HO2GAIfmha3Gdj7-LRG-TK6z7gXmEzL_FAIxQAQmbo4eyin6clk6SJgErw53HCrE5O00quqNzLEuiivx7K7IFnfQx3ph07QLOn0-8G001RA85uiyKgpoCB6gdMNh41E8ReZ8wIJuSNNOs8cvbq4MVwyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJL9pwm3GXckoqncdAbz4L0JBYet-S9Tt0E4r_N9-2d_GNFzpkMJziVGcwSoIfIgyJ4uXZXwBwxawpITquPKCLYE_oImQB72zv_V22-XXoDoyUlsZwi31fBo2jsE6iSabKCUQfZWDoZKMpjI7u8yUZyF3939zk23Kv_rdz0wFs1szHdLdn_IFJYCokyLCDvB8KLLLKztXaaY4ff-s5jOscKOrZbONXtVTyebQQ0VSZydOG-wvG4jqG5ig3DLGMO26uzxBxYYaHHOxUsLOH8Hlhegxgo_cumyly8TRWSYG_5eLg15MIwSWak5oA9qW7bpYGmjhbu--ZIQ1fL4wyxekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ZOZ77Xoqu9XUYz9pvlluFAbNyE3LYDOiCmpFWJwYcmFhLMWS9EjSLtY5PMwcPuatEzvNy_fPvQJcSI8HOynZMmvem3-jCeBo6EWaLQmSi0mUXqtz3O6mgrr48U1eJHpTz176dV4FPW0FBAg-5P_y6VIwKubEjO43jn3BQt95FhLTrYSOnIl2GpGrU0nK5gEGD7ZsbOAPSuizmbth2-IKKv9Nl1xPvP_VeYwbXVzJeYHD9PffQlkAuKqp2Txm1WvPDhcQrubIHcP4E6LKCfuRUohrX2Qv7zhaHDUhxSezRi5v-Jl5VAnw1vjdU7DhB35MT9UbS8OurC1_J9-wZCWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eF0d8VGtzmGm5pne313g6N49PqYkF1uvCdma34717RndRJISZ_PQwKLjkf56IfmHIJOBnkFpxHqcLht4GfrSo3jXReugx-KOKQLmvV98Sfs4cekTn8If6XoBvQOe8wC8V2Y-4967WjqWWIDjs1J5oKny7hNNHqOEAlFWSWPI65JCZd5wwrkB0D18D0XFDbwWirvIR6JgTw2bD0Id6iAjbZUUzCBMp67Cy3_l2kfT6KK7DXeE0_QnmJE5GgLpOUaYx6O3Lm2E9__2JbPm1DDEoEErphD4oT_UNru0J4RKoD8en5AhjGPTaqCAgxBVdExsO17Co4SFoWs_K7F7TE4dUnF0RLPZe0r5GpLHF4zsdLieqXSa2Esc2MuD9GIsMH1y9KyG4VonSW5-g6HcOODY8o_eLssNSKdxncNmszoF2oXwOtfXVY7TcgUtxiINS7xQvOjsC8fkm76WGabf0CSZptuzfr1eP1lmWdQv3hej6QEnm7D2JXpTQh96M6vKtQbPwShUYA-bLtAuwjS8KegDt6dJhw4zyndEGooKb2yuBDY4XvMf5j9yurkfZ4hgVI6QZE3krnrvVb2KiXabG6hulNvlIGHJhCIAX4kslFG1rJM_oDmTGFTQ29Y_zgBqAqK5OQOP_hoqViNa6ia_NXJUpezU92rDlvAGk8AV1_A_Vn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=eF0d8VGtzmGm5pne313g6N49PqYkF1uvCdma34717RndRJISZ_PQwKLjkf56IfmHIJOBnkFpxHqcLht4GfrSo3jXReugx-KOKQLmvV98Sfs4cekTn8If6XoBvQOe8wC8V2Y-4967WjqWWIDjs1J5oKny7hNNHqOEAlFWSWPI65JCZd5wwrkB0D18D0XFDbwWirvIR6JgTw2bD0Id6iAjbZUUzCBMp67Cy3_l2kfT6KK7DXeE0_QnmJE5GgLpOUaYx6O3Lm2E9__2JbPm1DDEoEErphD4oT_UNru0J4RKoD8en5AhjGPTaqCAgxBVdExsO17Co4SFoWs_K7F7TE4dUnF0RLPZe0r5GpLHF4zsdLieqXSa2Esc2MuD9GIsMH1y9KyG4VonSW5-g6HcOODY8o_eLssNSKdxncNmszoF2oXwOtfXVY7TcgUtxiINS7xQvOjsC8fkm76WGabf0CSZptuzfr1eP1lmWdQv3hej6QEnm7D2JXpTQh96M6vKtQbPwShUYA-bLtAuwjS8KegDt6dJhw4zyndEGooKb2yuBDY4XvMf5j9yurkfZ4hgVI6QZE3krnrvVb2KiXabG6hulNvlIGHJhCIAX4kslFG1rJM_oDmTGFTQ29Y_zgBqAqK5OQOP_hoqViNa6ia_NXJUpezU92rDlvAGk8AV1_A_Vn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEsArw--82EUzjlMigakxOlHRRIjLEwizbI9G_oOubKF5JzNxscH17vrXo2e4fi9iXWP4ArjTNQP5p2As5LvI0bVa9Wntu1I-lrirlRZraX5CckDRAUJP3H5Y6P2OS8EwetXkqt0fiPoIkRTdkiocH4RhddPuAm8qibFSCskpqpywKcbOH8ZoaGtslIGqS9fproukeGinf6KufPVZGbJvu7AMbnL0cITl-KJ9785e-ww-nTD2clUWTHKmqwhzuNQC0gHoyofYWBQtXhtz5eOR4frgqoWCbKntio0-hy1vlY-FR9cDWYOGes2LkhUV32oFnoHOmsOOnDbCKrfn0QQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOFtSyA8q2NladVEWmo3u_upP3pmLP4GIRUYyXvJQhMap8Mx0Gp_zR3ma0LAXkAd1GKf-ESYf3zAecR86eFigMvvobhwQ-1HsW5f2EXoB1tiWkNGG6l7g0dG2JsQvqRI50O7Pa3_2bVA2S2rCxdli12H_blKS_6CTv8nykDYUtPI6Cw0FT0z4Hy0YhEIDIwJiPioePSCrxYWgSJfvgLUwirLQabiMb1k51BTkNSHovKRXSsG_8jKW6Fyotz1ymNz7XRGTtgQBZCv8IadM2OoaFyPlpAp34wnn7vtK4Ubw4gW21RcVjxft46Id4NgsMKK7qqINc04bM3ehWhFJJuR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7y4ktW1YqeeLoF-tJ8FpNS_qaZAFZMh5vuW0ryEPnRCbt4B0uWQAY6e7l5kZJEw0N4roerGvPhg5avFasBcs6ecPycMuMScxgl774MfIu6AaIm8dxQznD2n0M4QNUPTqifE2oB8vNR6kuapdnLBiNhQBre-eEI4FZfXdtIlf3nyTrEKj_2t5ZERwlCGrW0MC_BZNYimWvuG-ElGv1bCuTADMsz95Kwk_A_nqpZtEKNJOfpPtZNK47cdht3uEdYVW5e5IwykDWc8L9nf94eQludVSBolj7NkvCmhcKNMiPagsvqckCt8N2d8oJUYe6LRTdaiY5mH8-LXhMRM8bTbtA.jpg" alt="photo" loading="lazy"/></div>
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
