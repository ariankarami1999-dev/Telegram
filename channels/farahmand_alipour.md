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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 554 · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3p8nGVBQZKWfT7-W-7YZkbhfFCftZ_3GX640oH_uNJMbZrKgoMMTL0lb8KexQfTLEd1RjPQKJ5LfAP1mzgrPEytBwMC03Xyg4staI8mi2WfeYFvm6lAFy866KngSRTDRxZ1OvLhHOA8S7RDop3sNu4B4z8WvEz_UBhmVEC_DM9PmI2byqJ9GxhREf_JMxDa5GNXS3-keCTcynFXDVNjbw2ISvE0kenlGVpZ4kkUFz750vodKpi73uUArPB3TOfKHyqhLoMNj6CiTtHNLeJT3uxO97Vjz184w6tf2XbLivCK83Ckr4Hno0uDkefnhwpPCvngykqDnH_gq-sAVHt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NslFIUbLzAd-u3LxjhpKY4PaK6e-vK3Aah1hhnPQjBEkpIuHuNIlJAKr5CI87gRDbCIuRupbie-cKK-LgpbY_yyiwhw4uAcc26-I7vhMtxyu0BpOLfmwbQE2O6g2r7tpDZBRB5_b5ngC5xrtYos9-9cDIwPcy2tNcBWqW91_ES3yFptpIGEc4vR4IKXRc9bQv76nGeEFp4dh5rxYVRNleSN6fh_MzNGwf63KW-CJT8qo0FdKs4Xe2clsy4wT_yguk-o2rWHcaL0tqfFhU42jKPcoyC8vEwsqAahqruSB6JEp7CQ930C4yh_fpkOqfYG9ZQojeq8D_PjzOITYtFEx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9OVLQHBYnck8r4an9MLPeSdj0_kEssPky4S7RrX6GQyQiAobeg-_wsLyBuo4Rw1mHS8hqSIo_y2TkNbB_0fDQJRolfGDvfqD7ZCNkTD1ORIAWndlalrOlM4m82X986ClzCLOkPLL4D1xGQGJtidh8n7tCzlYhAz-IlJ2QOLqW01IjqMTUSQcBMPV6h7slDaHcqDaqtme0CBh_vQHCNbSx8kd7XWdMp0k_tl1s50zt56K5b75bBnJXp4lET-iD6awfQPO2ouTCTIz8f7Hq_HWnN4HS5VxudNTDOUbJ_uiaXK2ofcrZeP0rQSoh6_Vj7Z0QhVTtggCy3k6ARn0cTZ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPQyGH8jpYnRAL9R48M-KPomIqwFEfm8xxGE9NouHKF0COHm2ICGgQ8C4eiCdYFdwt5KtgomwtKDoRLKVt4UNpc_lE20roMAft3OAY45d1Mii7JSdNAAedLmKO1B-P-V6wmMEaqU3SGNE_Puf0er93daERFYGOqI4GXSYh0k7YCaoBQg1xH6tFKFT6RafB23MgOda7OUbvRg1Bo-OVdfsGUd2QkGvELMgFtfBD7ir-7B5Lmx8rZj3UnHEgp-UzfDQpOX4DJgZCd7-Zl6R6O7JxaiHV59Ys9lXth8lfL4hOH9AEFsrlrk8OzUmhqd3Mz6WTczlW1Cj29q4qAKzWpbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOG_oRMQpDHWHMeFU4q2aBzdwqo_O2F2L5UnlyuA78XAzmXZTPhOYfT79kxFTfOlW8KUCpU_RZ18CcVhnZ5K1Nsgp_NQ9RD5RnL4TjbqPg9hy267BrTfUYjdWTF59_1Sfbexevruz_EOm9Hhw3En3wNucv8LQLqLSMOpSV6IquHkQYnlZvVskeJmmpQ-rwsWAGH9J3Xkxhyc9LgPP49RwJ5VsQ4H6OW00zU0Qny9NlWdXOIFVTn1zYK970g5jyh5qQO3HpMiY8JMHoM0Ld2EaM3-7kbhJJXRyRJYZMMdCckDQbvCO4fwKTw8r6WX23IW1WuTu5TMASpYJ2dyacNTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox1lveio0Sf4Iz7NBktJM0lQgOv4u2tE-domLY_CpEtAU6ZhZ5TnBeD4ae0Y3UVZ-edkhPizHJKUSY00XWzN_Jc0Hs9-gj8IXZG5BFdSiFbAUaZ1QiC9dIAV4FJymZ5PWfkLJQBxVDRpXyCo_KzlI-WfyyNYBCr2gkC3g1UHn0NKyebPD9vNz6ZUZQw-s2t5heD-SUj3UuTD2cfI93pXaT5WYRW3id9-kp4-iq9x1-G1MAOPnpoxrIkp3xUkiELTd2nk9gneE1Qg9AwpId3e1u4tDLAYy-dpI_jxODa-7psZmNgRnbM9Ls43SLnSaKElYFnVwtmRXa3iyJame50dCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImJZyGoU6GOOze4F3l73fl4ZQBgVXLwWv4LfXuerC-ojZMzTPR4x5B-jF1xjgKwpPgKjTbTr5NbW4XInGv448vYKq3InI1xMA3IpQt5KxUKp00ol2plKHqKrK3ZClu24D_ZFZ-W4xBpUO3i4pzmZz5mgKaTl-NJVbuC5-cQXA3PCEVfNt83UTSwucxY_WvXLCULwvTgmwG9jREBf6eWTTAM5eH7V2LwNEBfmyt6D90nszoEKOmzPnrhPxMW49y8DxT2CHx-EihLYbJQD24A_0ZkYQWNLUui8X5HJdNIuL01k9Z0KGS0L4vwlVCKuc51Lenmz43G6r-40PCuk0C9DGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIOU3l4960z48kcp3Oi-x84C4YqNFzctkwSs62D87VuI5FdlXkqBCYg-E9yrf9r9ykJFovl-lQ6RhOE7bVPDD7INoI4HOAf1v2h_pNQdf5dqrIsq1yK-4IZv3ns5tbHaIJUcKR8-eSAYAiLGl3H_D9LhE5ZSmlfNTp6Jt71Q4-ggMYfPLpK5rN9TzKYTkQAQldt-v4N4jNa3rnI8GOmFrLifRsGExtxnfxztLuwtAeH3xBkL7nsgVuRRuJFGkzB3A5LwYA6cn5mlz28cVDGuTHqN0o4wly1Io0ViHJE5Xi1OvD-yT3Pqwala7v-exHkgDu0VSJtm236CR7aPQKi4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQEMwhMTIFrUEJJnui_E8IVqCPVAGpaU9Uxwfc9d7GQpaLnxquVfMLUNWkoQQDQKIjxvbqtl9PDCohA-lCGdUgcsbuXQSbsweJxonsOT5IpFDpEG2OPIsdoC17k2DxGw5ZEDBmpXRmgXep7UqoPE36lf5rttjLRCtgLdhO0dPRB7HkQOP57ZwYVkwTlR434x-zh2U_MZXajyb5NxPuKGY8LfKS3Ohq-jv92uBq0KLZ60wgwtCuCuvlPcJ7ms1YvyXrpqVZRhqz3M27jJQaUjQa5xOVEpK7ogCvBT7ESpNLW4lOBj5sa88Ek2SNL6SX3ZJdBCBCKBDlq7BS3qb5KrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=UY3cckazEV1a2pMKzpgSFXlIAznQ14_fct0hFKLWgAPazls_ycbj9p-aRsaDPFwcrqSwE7sCiMJuloFzSCq6rFYQSRqFwJGgHnSfS34shAxOAj-D3JUsxZ8LKfQOY4Mr-77r_6NhTFSSNiRaJie6G4XFP_vNbrzuPE9WTCgBcZM6psJs_bdhjIqcwAnSKiIk0kGEeAuQau8sC0r9T1DDIbOpeuG5lxCbOsv7aHzl798wTnwuyUkoORKmY58Fo2SYbSSb1af2nQT_qkjrUVVuPDN9RCdfcFPSBIIRmRGlknOVdJeT8fjydWVMyimEuZ1lC27JoM2Iao2yCNnJHM4_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=UY3cckazEV1a2pMKzpgSFXlIAznQ14_fct0hFKLWgAPazls_ycbj9p-aRsaDPFwcrqSwE7sCiMJuloFzSCq6rFYQSRqFwJGgHnSfS34shAxOAj-D3JUsxZ8LKfQOY4Mr-77r_6NhTFSSNiRaJie6G4XFP_vNbrzuPE9WTCgBcZM6psJs_bdhjIqcwAnSKiIk0kGEeAuQau8sC0r9T1DDIbOpeuG5lxCbOsv7aHzl798wTnwuyUkoORKmY58Fo2SYbSSb1af2nQT_qkjrUVVuPDN9RCdfcFPSBIIRmRGlknOVdJeT8fjydWVMyimEuZ1lC27JoM2Iao2yCNnJHM4_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDe3mCS42uVlKIxyG_SC0pkU7AHQwATHfp9BV19-lT91pKXw4_1Mu6CHmwVAvlPDRm8vEZmhmqd4eNYX6uMfH36viROQVSd_rqRPUfsJGsnuCvrCkFwndzRPIzwFeSYcOwNdlLUgAfxFxHw5OP4q2ToJ9vZXB1vqBr-3uxKXDWz0N-5E3T-1cviWBm0HtVaH1jEjeu4gFGVwgevEpuROFwt7rvDhEw6rdr6veFS-ZW_W7gS5mKQzOFIOcvYxYLKsweXiABokQOJFGYR1-rhxf581eRZw7lmXYttk6HJv4IfSbsIYNvGM7BSbG1QDlaB_OOcjul7bCd6-btJV9rvhcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=cXEW0-kkqQ32Lpp484bgHkLFYEbXIrIdLh8DDpR1l6Gaazstuk_XTNDebTU3VGgQ4VzoEsbjFlFRh0yMtTA9cU0xs3Zsnx-YhANe3P9PuS-yq_jO2-vbE2HziIfkNVTfDKqvLdupsRcaHgPMFYXPyzPTzwvK-3Iibn69vwGW0k_vuvTLH7LmsNkxq6AH2ie2g1av_HawJLfTRQWQkkV-FEIWzlXDM-ypEXZKmHD7QdbHRKmQexREpaZWjt8gVYHt0RYAnvc3i-Uq4qKwVLdAMkeYYrsO6CmxnoOGZHD01S5_HMcOJC9S34n-sLu0ehkrHzfyyZ3R-V9apFrttV6cDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=cXEW0-kkqQ32Lpp484bgHkLFYEbXIrIdLh8DDpR1l6Gaazstuk_XTNDebTU3VGgQ4VzoEsbjFlFRh0yMtTA9cU0xs3Zsnx-YhANe3P9PuS-yq_jO2-vbE2HziIfkNVTfDKqvLdupsRcaHgPMFYXPyzPTzwvK-3Iibn69vwGW0k_vuvTLH7LmsNkxq6AH2ie2g1av_HawJLfTRQWQkkV-FEIWzlXDM-ypEXZKmHD7QdbHRKmQexREpaZWjt8gVYHt0RYAnvc3i-Uq4qKwVLdAMkeYYrsO6CmxnoOGZHD01S5_HMcOJC9S34n-sLu0ehkrHzfyyZ3R-V9apFrttV6cDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYgXKWPf5rknV23I7TLw-aBIaC86cbZCOtavf76w9k5_D_jaBs_-0GITOkQl7lScjgRcqIVXDU7s_hf7cYqDQCCl0MqzrhlwnhTI2agNw60pddTzQeH9KYDsE2ojq3pdttupANP8fW-XDcZZ5IBnc8I-oHU9SrS7j6o9Z05ol_I7AUARzTbKuM2COFf3pQ6TtHCwCNlGA75_dXt5oP-2VGxrd_eV0QPmwnQKRRMkQH9gRlzQY_RE_XLPTXMACB2S8ZcU8ip6ShOzJtPjbXW8kQGWwfi1H9Wptnt8z5iiV5JxYjO_CCrVWHUirqCe35Id-Qpo5UbpCUcBSL0JITrytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjzZuGZjr0eQyu8_WftJUf_cRmJhVSNbRtsWkv-FQ4c5ASF38ky9xZWoa9jBCS2i8tWazNZfc7_lnp6Q3DkdcBSEuWpgGQukrLklUwGvWT_FiLCJL15W3-sHskCQdQ9PluDWTGIE8R1tAO9KenY4PQUbcb_NFK9ia1Ac3TMsfR6o-UNim1wNBZdMBLEoqsuuVFg3a3SM49JnL2Wry4IZ-SzlxgxaWBxmlXA2c6LnYQKNgRnZEOzr5IoCqcRyp4ogX-XpZzHEftKiAzbk_FTES1uH_vRfM3CqT0BCI4S0YsWCdvS5tGDnOyILOxFbiIvgvVKvu4xqNRhGJecNPmPm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bYEUHmYSx36Yn4F0VkyktWfMtfl61oAXPbx2wij_8XZM2GmocfkwnryO1Zbl0-rm8h56W9WtnBtNRMaIUxoc1nDbuGU9MzG9nJYRUKPjYK634AMCDfiFvunr0V97gN5R2UI5Mfwo8IqzSmGU2Oi1eNhW873zudoQB5LLVTAtR2slyzNk3C6kp2wx7MXSrfQEb0RpxQdpBWexKozGFupz5-BmUQVeJEdX12OFpNsTL1AsvkNBzAn7vgZ6kHdV187MD9h6mID32SvEJ1XS5kGSg7_t6iJUNDJLXh6N0oXr9IvrBNiL-zVXPxwZJ-7Zm3DTAOG480lSjrtKU9KTelYWSJT3Zm7G4AIoGEVsxziIy-tjgApdWQeFUjvJpFz61Cr8eD0ynIrAhdIdLeZxyMKNi48e0dKNpkJzzNi4piMjNcgE0NyUXAcErerYl06Cy2Mx64xbuJ0__-MDD_0ZCEmSkGGdvXK7ib5GayRtoZ1zHrNJ1X-U2lmlKZb9xxpvFT_n05Wx1-bain614-oZwnIn9IWzzm7ZEtJFRRIiRaljgnRVJ54WKP1_XGhsXUXxfb_mkWaOfLTTjAZwY8B7uM0Ix6mvkpfZd6WDUeE6Opc1YIw9ApGTEuBuPaLhhlk6Q_HrvVUZcokqizRuH8oemcHaj5bnU3HA52sK8wSMFRHEavo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bYEUHmYSx36Yn4F0VkyktWfMtfl61oAXPbx2wij_8XZM2GmocfkwnryO1Zbl0-rm8h56W9WtnBtNRMaIUxoc1nDbuGU9MzG9nJYRUKPjYK634AMCDfiFvunr0V97gN5R2UI5Mfwo8IqzSmGU2Oi1eNhW873zudoQB5LLVTAtR2slyzNk3C6kp2wx7MXSrfQEb0RpxQdpBWexKozGFupz5-BmUQVeJEdX12OFpNsTL1AsvkNBzAn7vgZ6kHdV187MD9h6mID32SvEJ1XS5kGSg7_t6iJUNDJLXh6N0oXr9IvrBNiL-zVXPxwZJ-7Zm3DTAOG480lSjrtKU9KTelYWSJT3Zm7G4AIoGEVsxziIy-tjgApdWQeFUjvJpFz61Cr8eD0ynIrAhdIdLeZxyMKNi48e0dKNpkJzzNi4piMjNcgE0NyUXAcErerYl06Cy2Mx64xbuJ0__-MDD_0ZCEmSkGGdvXK7ib5GayRtoZ1zHrNJ1X-U2lmlKZb9xxpvFT_n05Wx1-bain614-oZwnIn9IWzzm7ZEtJFRRIiRaljgnRVJ54WKP1_XGhsXUXxfb_mkWaOfLTTjAZwY8B7uM0Ix6mvkpfZd6WDUeE6Opc1YIw9ApGTEuBuPaLhhlk6Q_HrvVUZcokqizRuH8oemcHaj5bnU3HA52sK8wSMFRHEavo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=R4HPG3u9sLtB8Mt8V5_KKTUc8Vc_uotmoCwEIQYvy6dvkbC-BfbrV7KVDrAFDeyp9A4bRvb6LEEC0zVDCfTs4KQcfuMFKBzX_107FI1P6WNLghEZfffP3_qQahWtrPvgEssjkZCTGAuY-ejskyCyaoCaukL5ywjWeCfd9Akd_J3cMZApFXRZmvfRGAx56rNCNs996hp1rs9NEDjU5wL__7uPT6QjAru-Nu2I6kiarXRBXrLdnPZNUzW-O3JbudVjo2K2OpaLDE1UhpdXP8gGEp_fj0DoXOdiTepA1ucK-0kj8CRK42uCUrcFlWJ9GcjDlRrE5iWOQD7VawrIsWWmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=R4HPG3u9sLtB8Mt8V5_KKTUc8Vc_uotmoCwEIQYvy6dvkbC-BfbrV7KVDrAFDeyp9A4bRvb6LEEC0zVDCfTs4KQcfuMFKBzX_107FI1P6WNLghEZfffP3_qQahWtrPvgEssjkZCTGAuY-ejskyCyaoCaukL5ywjWeCfd9Akd_J3cMZApFXRZmvfRGAx56rNCNs996hp1rs9NEDjU5wL__7uPT6QjAru-Nu2I6kiarXRBXrLdnPZNUzW-O3JbudVjo2K2OpaLDE1UhpdXP8gGEp_fj0DoXOdiTepA1ucK-0kj8CRK42uCUrcFlWJ9GcjDlRrE5iWOQD7VawrIsWWmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMNHhq5zUeBcK2034VP5wqFWajciRsGZBCZ_-DesViXBjTC9aKvS7tf15_q93B3oZxG18-tHAxZ0f2Jm62oMWskRvls2esJ15jd31bX_9naXG7o_2u39sW2nUKqHobGEqsFcNylbdj5pCwokiqK4f-5w9-jRqiVR-NF4dpFRhmkwNwDsDsTAmhgsV__MXrggsg7nVA-jQyepbdxONDhaHwplqtaJ6XBBSSZ_RrsHXu2ij7PFfCECBfb-vK0oc6EeO7DLzD4UaIA5m3CjCq2SuhCCFNTDb-DJuNe0zj4KgVRmLIF9vFYh6NHRGeqjdcsHXYeYRC5jr1zVtREJdISYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Ha9UQ-RvQqMFPvnCqunHJ8io_nAFVOoNOMe0CnPveSSyNKUGxZDqMKB7TKr9jPgm3llR7JPosB_RIjhewLdv5X2m1dEWjh66En_xH8t0okXnNbcT-V_s4w4AQusjqooo5K0gb29aol_CejOIc9rPN55_01ZVqYWadA65uomiJ9ixVo4rG7MJFL62pEhE1DtXWtIbEXHt0o3ynbrsVbEKbWuIJqG5eekAOmzvxxLmC_HBgut6uwvpD-1b_5phMxEnhVaJzoP6f0tMqp8hlTM-1Q8bYn5zYxsfLa69ilQUq85blVcQo_yyudYiyJ3wI-FIFluxBovsnr1-fv-YreFl-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Ha9UQ-RvQqMFPvnCqunHJ8io_nAFVOoNOMe0CnPveSSyNKUGxZDqMKB7TKr9jPgm3llR7JPosB_RIjhewLdv5X2m1dEWjh66En_xH8t0okXnNbcT-V_s4w4AQusjqooo5K0gb29aol_CejOIc9rPN55_01ZVqYWadA65uomiJ9ixVo4rG7MJFL62pEhE1DtXWtIbEXHt0o3ynbrsVbEKbWuIJqG5eekAOmzvxxLmC_HBgut6uwvpD-1b_5phMxEnhVaJzoP6f0tMqp8hlTM-1Q8bYn5zYxsfLa69ilQUq85blVcQo_yyudYiyJ3wI-FIFluxBovsnr1-fv-YreFl-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWnti013oxbHoC42vs7djCYp4wzeG7H-iEpkLdqI71PCi5dslXESnZjo8icqKCf7GTYknTSsdJrEdMpS5C0EllnkeLp9CoCe4oh9BorZAb-_W6ErhVKpfKWX1o9UV2VVHU5YTiUtC8lb9gwetGGnO3TLYnJOTAX8T3Gz6VNNi2e8BtLnd0os71lnfO3ri8ckWzKGVHlpcQhjViyeNQJgoAGvK4Wg5A9_UpRA_CHLJecvVRWVOm40zO5XRsWk0R8jv2Cwr_XDqJ2pLPIwNnFRmmGBesV4eEEbApOuFrb3pBq2sV8ogD0ZpsdYH3vlJqsnCvTTeW9gEFiEsDFGCI5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgFpWY5OsOKb3FSDQSiOoapCt0cLNJV9facv-6hbzoTV8QVaaVsVsIlP4P_Xo4NpZeUA78SYaQ8T7YcP7TJKn57SpUJMVaBB2csI4uNeDSNCBHQASl3WZFeKN-xTpn-J-pRwhDWpEquMEj0Y1D6B7jhnayMsQmz6p12bTSHgr4YRBt-rdXUjTZGxxKN6Mm7oIacoUQCkmS_xYHzxityiFy3xTtL2hls3StEntFNs6Ep3BGkEm5LcVSwVOSBYeCAw64O1md-DD0D1e5VW-qSHW_pcrDuN_uOjXdXnuYegjc0OpD2wvQQMWpERuxvldGYdeaHTY3F7GVkIz1YR4SWe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2oj4ycB8ixtR-SSgpBppLnPx7wtwSMg0LTiFmmht9eg_mr1YGUkqhCEgKIebsBJucqDG5kN4_BQIWR4w1qouut5iSItmxSDYNXM6u0hmc7ATUqoPcXdVCdHYT5YQI8FOlBqqEdkq4aV3BixByge6asDkjAEyRlfuAlhLFFVdyFwTmj2CjNBWIFVaxhP2_8tvRoHRzD-MeZgkMIchXjWgIbLWALbziGYQVYr7sHRP_7QCkoOzx1QixDDwfRxQivQSiNM_LwuumQwWD9fL-ks5L-nd78EYClf0nej6PQ2coPqlpV6wJpIMAkS6PVXhxNGB0ybDf8K7h02_-3903ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHry99YENGpWwwRpFAf-eWxcjSMLH91hrr6qj6mm145BifTKJC5vwg65qUoIVPec9DmfrDWiHK4ieDLLWVON2OSAbcAA2pSwKimz0fCz6figoWIrgr83T2-rcKqrDhQttQQGwXAsn_Mzmk0Rr9Gi7zcdBnoTwlyecgoe0RS60K7KxP0SukIfOhIZx85cXEJIkO4OIIblCtHKWgEeuYDnJxBPrZ7g7kk_rdR8XDV7rMVhVdxv9KyWbXVK8EZrjXhyrN1RkW5ME42eG_7BHjIRaQTiv6EgKcrak_PgNEhi34CC3wMTpW3OwZF86XeEfst1YpdMZeZ2ni0nkc2YM4n1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ402ap_RT0eYZBAGI8p-FCCRT9qUw2ftA6hB-Oi65YYitdOcYxHSLCZtEkK2jfvzJPmL7wHqWyMzTYBNalHKhVRfCg5TqPJHXiWHJui1Uw224QNcRQV4fDhiOV806yVD0tGiDA0HJ9VZU4LHqa_s6M_8Vb040v3Y5iUukYpuGreViXAWa1Oe1zKy279Y7vuAdTXeOE7Zj8_X1YeKFaxZgDREiV8sTm4UW12A8vIdBBj5XPBrzFr62OEvu_ieXnlAnJoLkcE78Yrrmt9B3nvf-tqMxJ9dZyasdOSOTm9E-n82yhJKHENYJkcN8YNe_JbTuX-ya3dJ6NlgW9TnL-sqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=bq6B5jiSW8jfzgV6XC_VNqH7Y7_LCFjowSjKQ0lqwyGFgK03hs90w2JbN9f0OqZ9NjW6mDF03uO8qObxgfurTU0QA5LJGXME-wEoXgGgnBjMo0CU2PMtTSZAIBOE2uO4cuwqXtlKqPBNxlz_Pt0ORwwNuKN-GsAyaPidDVPxXUIwTz_DuPIltHKE8fyuAxa6Bk_Pbe-XsnWr6NGYal3bFRxSea34KxwE8inpOS65ktI4sqayNE9EGBOYfeY2aiQyCeasKzF_n3OdNxVsrhyB97h18R_PUmykqK0nT3zz0M3aBlCGuhTyugsMbA5A3hDR6iqZQjVTk2Y4qEjPqvzHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=bq6B5jiSW8jfzgV6XC_VNqH7Y7_LCFjowSjKQ0lqwyGFgK03hs90w2JbN9f0OqZ9NjW6mDF03uO8qObxgfurTU0QA5LJGXME-wEoXgGgnBjMo0CU2PMtTSZAIBOE2uO4cuwqXtlKqPBNxlz_Pt0ORwwNuKN-GsAyaPidDVPxXUIwTz_DuPIltHKE8fyuAxa6Bk_Pbe-XsnWr6NGYal3bFRxSea34KxwE8inpOS65ktI4sqayNE9EGBOYfeY2aiQyCeasKzF_n3OdNxVsrhyB97h18R_PUmykqK0nT3zz0M3aBlCGuhTyugsMbA5A3hDR6iqZQjVTk2Y4qEjPqvzHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8HSXLu_uu_4huM2d0m9mXT0qMvddPh8PVthfQE-fe8O1DYDbPc8PH8VxihCfVtVA_F-sGMZobV0BbmMe3-BkEkHWaUyNiXX_5loEALXZvvqMXIyaxRKA9Vtdt4Fi3RhU4sImVHITOstI2pAhHgyNAws5v1J87nZypKKwUfpow3wAzuec-dw8nN5TiQYWQZJca-bK-lm6Fq55BDEZe4tBDzj213XQ6MNKWBipcY1FmQNTQwVWJ3S4oI3F9oeT3gfBed9n2b5Qdaz8bxmAENeJ3KcbPPi3q5oF45qhCmnoXZ9uF2_YBG0C4MTtPKXpLCcMrvFSCD4mTJ7oM6O5oXDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6gXM5URFPCcPJrJJ1nzKXbbEK8AG2eJZMrg4IJ3sKpROqW55vpVXu8xtAu8zrhXOBgEQYlR-R0jKtRdTvE8vzVZXtyMeW0luXCMHArtQ-pwpg7ac7Ba-bT2Ro1CXpdJD97ACwoNAXA3pG-7nf2eO0Xo00fpIhYNVskgVvIPRTe7il_BOQx0stHyx1lgyjlugHdZiRAhSOHD-qXYJUGfjYUS1ggr1Jes6ngFa4bvvBbilq6WTTxqOtT_wNin7yRf9T2-ehXswMLfr773yDf_XbrBQdhI8AmFU_YRUhWCpUKkiqeeE650oPW4eTHL2MvDgiqpM8YbsXV6NARK83TtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=og10MZDyMiAGKyZOhJeZXFGhAznVgnxLWETpWOvoCoSu-ZESMSwl5EhMG3wHIDVEhINWZt6JmCH1ZcoCQomN-DAZ8oJfvmwIQnH_QP2-oZ7bGj5oHrOFOIQK3VYqDa1KSeB_f_Zvq6cFHR5nzNDWPXhduu6p--Ob4dsdpkYnUHrwti77f9VP93yalkgEQhffhU9pUdnMP6uUU6kTzp0XSCv1UUNSDuuiUYaWUJR3QxOJ0sv35sV8wSPjqMwEMwS6qgnPRMGURWQb7VFfqZOjtJ5LNhXYpq24oBQPB--rxwe3kFkkrFnZx3JHGMI6czt83s6YkboopcZVhmdUCMwsQ7uxbhzVe5mfNfPrOgh4HhoqJJ5AIwA3-3oA7T-Aap532mgLsg9lOGf3LNQB6J1hsMKwMmjRO1epPAymUOsfrr-LDAoydRLeM1orzbe-fkfBa-sBW8VSFMJMwrHGTJFhf9nAskUdYP32KnwlNPkPLMk7T021-jl24uLt3tB-adOSkjKHNG-NrWbDtp5oUKbIzZ2EP6XFeycuti9c2npUu2scHqBE3bsXFeG8fQn4yj4ylCvnRMpdcES0knA-TWcoQUjWoiaFgxeQGoIjsZlghho9_BFpt-8PSZ_f9sX_74_eeHgYqG47EaCpyG67ck0glQgIeEhg7-GHXVlsvrF6g5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=og10MZDyMiAGKyZOhJeZXFGhAznVgnxLWETpWOvoCoSu-ZESMSwl5EhMG3wHIDVEhINWZt6JmCH1ZcoCQomN-DAZ8oJfvmwIQnH_QP2-oZ7bGj5oHrOFOIQK3VYqDa1KSeB_f_Zvq6cFHR5nzNDWPXhduu6p--Ob4dsdpkYnUHrwti77f9VP93yalkgEQhffhU9pUdnMP6uUU6kTzp0XSCv1UUNSDuuiUYaWUJR3QxOJ0sv35sV8wSPjqMwEMwS6qgnPRMGURWQb7VFfqZOjtJ5LNhXYpq24oBQPB--rxwe3kFkkrFnZx3JHGMI6czt83s6YkboopcZVhmdUCMwsQ7uxbhzVe5mfNfPrOgh4HhoqJJ5AIwA3-3oA7T-Aap532mgLsg9lOGf3LNQB6J1hsMKwMmjRO1epPAymUOsfrr-LDAoydRLeM1orzbe-fkfBa-sBW8VSFMJMwrHGTJFhf9nAskUdYP32KnwlNPkPLMk7T021-jl24uLt3tB-adOSkjKHNG-NrWbDtp5oUKbIzZ2EP6XFeycuti9c2npUu2scHqBE3bsXFeG8fQn4yj4ylCvnRMpdcES0knA-TWcoQUjWoiaFgxeQGoIjsZlghho9_BFpt-8PSZ_f9sX_74_eeHgYqG47EaCpyG67ck0glQgIeEhg7-GHXVlsvrF6g5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ovr0hDST1TCGLrLwUqF5VQjE7mCa4JS6Y1PT_x28HXUEb26UfFB38HZT1DcQ_Q1WhZgEvBaVrn5lkzT-qkMk3tICpfcGZx5LnTPHbqbLHGoKRlA5in2SWr5gKvye_KrXsZF9ZsP7kUuHAQpbQAOmjPrycXQ5IzpykBizZ8kCp0rnKy03_GwEPCHWjxA0rxSd2QzLKGBy9jUUAvssRNccbI7uspIKmnPKGhz9AHlkfewl64AajYtWQQdoaYQ1IrZCqigZUqBUVAI0E1Mbw_vmUvRTzz7z4XeAzQDtQp9kKuNOmwYhx6bRSMAsS3PH7jgvtM1d0xZItxakMWnFgN8K3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ovr0hDST1TCGLrLwUqF5VQjE7mCa4JS6Y1PT_x28HXUEb26UfFB38HZT1DcQ_Q1WhZgEvBaVrn5lkzT-qkMk3tICpfcGZx5LnTPHbqbLHGoKRlA5in2SWr5gKvye_KrXsZF9ZsP7kUuHAQpbQAOmjPrycXQ5IzpykBizZ8kCp0rnKy03_GwEPCHWjxA0rxSd2QzLKGBy9jUUAvssRNccbI7uspIKmnPKGhz9AHlkfewl64AajYtWQQdoaYQ1IrZCqigZUqBUVAI0E1Mbw_vmUvRTzz7z4XeAzQDtQp9kKuNOmwYhx6bRSMAsS3PH7jgvtM1d0xZItxakMWnFgN8K3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RAKAPDho0Vgw3pYhaEIxZ7WPUC0oL_xmCtKcM7wR2hYUHUCXdJdm2bnMYmE8GMqqBSYHLyx5jSWonXLeueaqAPJpxhh0T4FTkf3BeHKfOyqHop2ge50OGuBXQMODEsubdMKN8eH8Wol3bX_aapgL5Dgiz9VtNwPeraERxZqr0q_kom38_2lE5T5eASZX-kvuMRZMua7kSk8wHbr5peSMdGlaU1t_KJZrqwwHH84GJ0gCcWOtVgSRPoj0f9YUeeReMxaee3foB---PV4y3bU0QfPtlWHGBiAHUiD6UqjqVviJUXX_c4Rz4is5EiFh7WBTHs8NhFOmo4IX16rsJF2pBAd0ZEQODp5uy-MySRAv5HTh7x6YXsI7ekvlpLRADvFc55V9_4gDfQn4w1noj18mgKuzZ7MhdoSwM2egzkLaKIsgtzriRmZ6M4fT6iXxn-09ykP3mJs56Me2Z-SKqtBKZpk60kmd1gBAnBaxwjlu87T6kyeUy7qKz38M-qpYsim6qOIQlkzLPiBVDD8eyLoaLDVSMkMIRZvE4RlLaq3GCI14QftWEoRMNLLBz_TmZ7U6FD--7IFdiv5I6pZoZgoUwdA9yQkrQAeN54Jj6P0aSmKHhD55FVrVg3NHsNJipCWhxQS_4Inmu9WAftTGhjJTkFj4-0g3e97StQLgD2eRUFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RAKAPDho0Vgw3pYhaEIxZ7WPUC0oL_xmCtKcM7wR2hYUHUCXdJdm2bnMYmE8GMqqBSYHLyx5jSWonXLeueaqAPJpxhh0T4FTkf3BeHKfOyqHop2ge50OGuBXQMODEsubdMKN8eH8Wol3bX_aapgL5Dgiz9VtNwPeraERxZqr0q_kom38_2lE5T5eASZX-kvuMRZMua7kSk8wHbr5peSMdGlaU1t_KJZrqwwHH84GJ0gCcWOtVgSRPoj0f9YUeeReMxaee3foB---PV4y3bU0QfPtlWHGBiAHUiD6UqjqVviJUXX_c4Rz4is5EiFh7WBTHs8NhFOmo4IX16rsJF2pBAd0ZEQODp5uy-MySRAv5HTh7x6YXsI7ekvlpLRADvFc55V9_4gDfQn4w1noj18mgKuzZ7MhdoSwM2egzkLaKIsgtzriRmZ6M4fT6iXxn-09ykP3mJs56Me2Z-SKqtBKZpk60kmd1gBAnBaxwjlu87T6kyeUy7qKz38M-qpYsim6qOIQlkzLPiBVDD8eyLoaLDVSMkMIRZvE4RlLaq3GCI14QftWEoRMNLLBz_TmZ7U6FD--7IFdiv5I6pZoZgoUwdA9yQkrQAeN54Jj6P0aSmKHhD55FVrVg3NHsNJipCWhxQS_4Inmu9WAftTGhjJTkFj4-0g3e97StQLgD2eRUFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkKf_FHM-mJYCj_aWkoRRiwTcdFZE_NMBz8rltZ53SIWhIG0ilJLZW9lnI-KrKzw-LNq2re3qkQEfmEx5XwbX4rgoLwglWLFfATNrdAGhlgzEnGOCBicntKyAsM9tldBOcn64vnLHvdkdKSEUUVQ3jD4b_9YnA3o7P2Tiffjou63x_v5Kpcj5WPK3TJOYJf4VaVf8g_Uu8JbVjMPlk12r1Tz0fFftPuWS7jz6983BVpcvxI4mJOXCJJbNcPOVF13lA25Q6-VkRAnWjEHR_fszFvIKulHPuyM6MJpnokGtJfTeR-7u-oJVq-WKQMD7hUdU2KsOZt_uq3cnacvGLq1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reOPAou4ldEmspTCMCoVDwb_xPSAkjDuQyV__G0MTbS3CrQHrn9rVIzxEqDI1sjQJjuhvZyhZ-vWyOZgC24fgdLM7bSLVkaxsZcds3hmZji3PSTFz42t4RB2A0TdF-RrbzGYoTEf7J9f42_fEml1cgRW3b0cZgG_6m05k2v_tNYvzj7ZPSkgqqOiZIRsLyhn64KejF8KrDPGEnIBfuQyuOYpck2yZmC0O7lfhkORzH_mjwOsTudKG8pfw1o0OugYdIJDhkK3Upl6yBGPkLcGL8OTnO_rbczDOdLTB1cgjThyxecV9OwHwyFySZRaP4PPJ0lF7W4GD2WX8xDINi1c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkMMkQBjwJVBvbKSby9cM9BpSxf0V4MImhAy2-nvWADnjsZ5DxXFPqfkRK5p6tf0MnOs542TWknHbvvNcfAgTVjksn3YcBguFF_ScgmZdmbW4-vo4g5hcaaS2lsOwb9yy8J5G0fMBgGJEzdkCuDkvCoF2EqZlR3yLO4fToX5-bBD4i5-akHbR9G7wRJHwEVvIU7FebSK5g1r9U3SwvxdK7rDoTMbhPrCqxS_YgxZ305i2g8ETK0qNLdjtdiIpUnScY_ggSnh4PhGbsG_6tbISUsy_tc-xwHXLOBIWjuySk3m8V4hLOJokF0PufuKCfjulPgTdM8XH16tGHJAlNZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=UVCST5Ca-W-h_76PE9jauSr-u-DJ6SAcFIJKbRLBzAHLMd52VJRapkuIwY3Autr2PW14WgS3fJjLb2lcqlMkYlLRkedzgRCbpGt8x3ZGSxOE3U4d8zQzGNbnmuFABc9c4ySHni-_zaSBucsaffU4YPZ69HiCUcWNLQjSQEW7hSC6MX82J8ppq40PuQQiehkd8FPzfFSWZhbGczacHOjon13tYfB_CYiRT78Ak3mfk50bPfPIM39ozVsOh-pTXatjBf2cjFNjq65CBhcVxmzK8sbNz9SUJuSidsFqAFUB3hxethowSdIZSQSMHbwfrxh1Scd0pweIDwIaXRquIE74cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=UVCST5Ca-W-h_76PE9jauSr-u-DJ6SAcFIJKbRLBzAHLMd52VJRapkuIwY3Autr2PW14WgS3fJjLb2lcqlMkYlLRkedzgRCbpGt8x3ZGSxOE3U4d8zQzGNbnmuFABc9c4ySHni-_zaSBucsaffU4YPZ69HiCUcWNLQjSQEW7hSC6MX82J8ppq40PuQQiehkd8FPzfFSWZhbGczacHOjon13tYfB_CYiRT78Ak3mfk50bPfPIM39ozVsOh-pTXatjBf2cjFNjq65CBhcVxmzK8sbNz9SUJuSidsFqAFUB3hxethowSdIZSQSMHbwfrxh1Scd0pweIDwIaXRquIE74cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X908xp82LNP6XZtvXFRBa5Db3doecAEegaf54LtxjtB3ZibJdM2EcOl1CRgCO7Fut1ZgQ8-FZtU0BqkBFrTgtf4vAqo0iMqamGu3I1vqRtneRDmEvdmc-hkWmgeVwxaMsmfDL77VXwR741NcmM2e6tmQEn52bSQbouWQryXks81ZcaU2Iy-kW7VQ1fqObpAijEN0o9mHc1dvLuKbuzT9_5XhDIFDjDR_vQ58SGCI9bOG79JhEuNI7qWCRsUaYGew38BPyJjUSVSDoxJDLUbPZ39Inw4AEAmSivHnJ24ixzH5s4dL0jqU05fuWscaivzhjnuiDc1KO7V_FZiUad3gxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCIFSHkxlwAXv0B5ABPU7SpWWNteqdDVwMz1mLLY9O54-8jftNffOdWVQuo8SP883y5MHD8xiimErL1uPtMeR_n1ORx7JSp1_h29dqEsU2R69UD37_cdPZy9ESKwXNjW40iHkL7bPm5ghNNZQ2lgXdqhQ6bg15I6r1cYFMlazBEuYCZdfji_v_NCihCvTu1jc34Kbdu8o397iD0yaOnu3F8ICt1jXUePaf99QdpwepN7__h56SmdzU4FphYk4Liw0xp_7Wc8-XoYTjFU88EY7VbNgt337Ywl8iMP2lgIous3C9_B2-ZWkcGD1g51_9vfLNE4D-aY-q6X-mtOKo9X2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6TVAMK8xv2yJrbkeQngUSKqC_2vdadvj6y8Bsz6tp59HuqzYUYSv4jdVZCvloPEeZLKzL3BFcbFhhf73FS29-AT6UQnQQLJ66hDruegK7f2_YNMQyXnXQfNrbBPYiu5i8y1S-rkQ4FAl9ulHQGGXPeZRb9mN6g92n09Zjc380o34MHO-TXVsGu_SYBq55rrV0euzBwGCcN4PtZ9B40FoLf5esplCGe7Hl9QsbwPYXwXUv6h0EzyzS41F5fo4AQSQ_mhSjzdoo6BpXwLrATkIyGg22CKAYnfBGcRk_objjkTM2TB8nb31ut1lzyZ1pwO0HW2iZFc1CnWulUsiVPPrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaBbslsjYwSykWfdZ0gSIHGky1QCrcHy8xUWBM7XuYcRXg1s9gx2ecdhmpnZ3NwhGmKycx0vilZwfVxXvkk2BjnzyUVrJ1JCKaYdu-Fgyg0qoAXt9vnEWqJoNHNTEOlmneUXECHKnScws4m8tTzkpwzY_3K6i4oE7xJR9XZFcb3caPBCOLfMk9rOY5HS8T_Cp4EFbP2P4_VEh_SDXOjashM3NFoqyxwp6DpMsTLinvm9Y72NKdsYfWbFHH1ADLBEPeYTjMjffZEvFId4xINvvuTeLPVZ2d0ocYNOlz3VeTllrYuzLcKHJbAY9rdtpAEo9P23LJ1sMUb0mVipGXrwcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=N1qPtTwJqOt6ZM1GG-FlHeF9rvoEksEZwG9ZRrw_6i5B9FLd2upyjM6u8VtyvyZmsvDScF5XuqSLLRnpw1_wx7knqkhMDVqpKRts4L1H9v6l-2mwksKRoV6QF8zsoKR_D5wUeD2Af5Bwb2i1WNbkafNBtOBQ1gY0p8sQO49a0SUoKDwMweZNckulS_RCYic-0AVrHrlOIu0RIrUrtLJVfWScNos8diQY7eNyARs_sAVEdavbac-GBnU8T5s30343wloKJcXG4txTxrJSg1iCVpsOQb7qBgZ5VSS5wpb4OR7CIhz6S2c2u1fp8f1II2zrNtNtP3idxdwqu5YfrMv8CzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=N1qPtTwJqOt6ZM1GG-FlHeF9rvoEksEZwG9ZRrw_6i5B9FLd2upyjM6u8VtyvyZmsvDScF5XuqSLLRnpw1_wx7knqkhMDVqpKRts4L1H9v6l-2mwksKRoV6QF8zsoKR_D5wUeD2Af5Bwb2i1WNbkafNBtOBQ1gY0p8sQO49a0SUoKDwMweZNckulS_RCYic-0AVrHrlOIu0RIrUrtLJVfWScNos8diQY7eNyARs_sAVEdavbac-GBnU8T5s30343wloKJcXG4txTxrJSg1iCVpsOQb7qBgZ5VSS5wpb4OR7CIhz6S2c2u1fp8f1II2zrNtNtP3idxdwqu5YfrMv8CzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=cqBZRVNMLs0H5hLA_0MOgHDIFGDUzGKssLI-RPvWypRtrDoHPmSTZ7xRVc70_J1jjy720dvarQVvuW2cxz-tiFxa0jXohp30gzWhS9c9yO-wbm02eIvKlcFRPFOA0VMYZxO56e1LUE2LUo1g_KkLtDLMoU2BZ1aPxU_tzGW1O3Iqu8JdtGrf01M2fmcQHsCjpX2SlEgx0p2Xz6mtJevVRe2OR7mKTVRfH2n9FyC9Npk1qbroRolxME9rVnkO7Bd314LNdZ84o48CkQmkrNAf3Wdd6x0hhAGHWlpqJPlbwmJYzZE-HeMx-EBZvlDmaIMzkxb9-AQSVTY29qcJ81xybA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=cqBZRVNMLs0H5hLA_0MOgHDIFGDUzGKssLI-RPvWypRtrDoHPmSTZ7xRVc70_J1jjy720dvarQVvuW2cxz-tiFxa0jXohp30gzWhS9c9yO-wbm02eIvKlcFRPFOA0VMYZxO56e1LUE2LUo1g_KkLtDLMoU2BZ1aPxU_tzGW1O3Iqu8JdtGrf01M2fmcQHsCjpX2SlEgx0p2Xz6mtJevVRe2OR7mKTVRfH2n9FyC9Npk1qbroRolxME9rVnkO7Bd314LNdZ84o48CkQmkrNAf3Wdd6x0hhAGHWlpqJPlbwmJYzZE-HeMx-EBZvlDmaIMzkxb9-AQSVTY29qcJ81xybA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qY-8nMI34cWmDgIaOsmgAxGqgcYyczuqPINLhnmbQiEVrY39WKLIkwb30lqYLzzlhJ_jJdhoxhsItfd_cF1wSxD4VRKy22M7HbXc_klZY_l5rPR8ZJmGNapxtT1BmZqjjOorSroULeCv617FO2OLQv9U7wHoakVdoma3WB-1ArJwoxhT-Od2aBFCfUA5k8FJlwR8GkrIgZ9_mIEbbMD4-Sn6G4GHgBxyzYcTHAlUAKRwCLHsRcR69PsuxCEatGxSWOOr7RCpdgxJRUdqSfh-C2-cOAJ_pPBePGBA2TMEvOStbgLxFfGvG7q8bp5wzDxFEbXcJi4TINoRxprobyvkeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qY-8nMI34cWmDgIaOsmgAxGqgcYyczuqPINLhnmbQiEVrY39WKLIkwb30lqYLzzlhJ_jJdhoxhsItfd_cF1wSxD4VRKy22M7HbXc_klZY_l5rPR8ZJmGNapxtT1BmZqjjOorSroULeCv617FO2OLQv9U7wHoakVdoma3WB-1ArJwoxhT-Od2aBFCfUA5k8FJlwR8GkrIgZ9_mIEbbMD4-Sn6G4GHgBxyzYcTHAlUAKRwCLHsRcR69PsuxCEatGxSWOOr7RCpdgxJRUdqSfh-C2-cOAJ_pPBePGBA2TMEvOStbgLxFfGvG7q8bp5wzDxFEbXcJi4TINoRxprobyvkeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSwLmCbFCrWcmWgsUa9he3OKQgmUjkOU83fTKMQrWCzul1YCAYkSJ3GXemZJKcyj_84iaY6VD3ysjZ9-gG1lIL3WqAQnHnIaYNWnGVCs_XVA910d_qyPXuHQ63t5d9r9_vqSrMC65wFfSP1SqKVXgwl6Npgw2OQZeb5ulbezWCxvlLtrMpFpHIFlpDpeJhLFJpm-4jV1rqr2axcdziaoLKyMNdblLsvIrhdIbJtPd_k7CfrPamyuI4-woVjHYCGk_YEjM_D4v_Vff5GUQ8fa0hepMcNri-o5CGRlbd7LQ0xm_urg9N5E25yVwfnwr3CZuto-yoOnNmaalj0nmsQIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=KKXwUtYLMCjSm4gODzipcPq5GhWeAEWC_MV3q5MDWzwtyoSp3cAmMw79j9bu_lRdPN0eSMO0Ls2bosmKm2YEdTw5QtYeTqv_JV7YQo4jswvINTdb930zsTgAx1DppdXIwYtoGOXTVUnxJln2tHN4vbqcYZeobwVqtcluRERYI6gZzq0klyasiZ-vEvbu7pEVY9ypnMyUW7oe9vJwP8-xyZmde1zfiongHDRUZrXRUUoS32QIn1oJ4c0xlJrWIrp_Ff7B2xXN1Z13_GZzINP8ORw6VE_aVMN7DFLQwoVLR-iE0YALtmwhwYbsf1Y3XW7i7HfvsGI6UnE59GaYQ9ZG1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=KKXwUtYLMCjSm4gODzipcPq5GhWeAEWC_MV3q5MDWzwtyoSp3cAmMw79j9bu_lRdPN0eSMO0Ls2bosmKm2YEdTw5QtYeTqv_JV7YQo4jswvINTdb930zsTgAx1DppdXIwYtoGOXTVUnxJln2tHN4vbqcYZeobwVqtcluRERYI6gZzq0klyasiZ-vEvbu7pEVY9ypnMyUW7oe9vJwP8-xyZmde1zfiongHDRUZrXRUUoS32QIn1oJ4c0xlJrWIrp_Ff7B2xXN1Z13_GZzINP8ORw6VE_aVMN7DFLQwoVLR-iE0YALtmwhwYbsf1Y3XW7i7HfvsGI6UnE59GaYQ9ZG1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=TmGO-pKUIF5jJjSrMPD0DKB_B8kQs5107JNffrkUkV8JtDYccbwL_k3VTzJklPez_EjjTxc0h92JFMcjTVpgYkicOFxCgdYILda7GwuyP0rc_hB_XUqObNLbjQ_-CrMnFIqIUHdTqsxmf90aYYdQ923ijCg8V_qGYDHCpEQYOBHsdA5i0OqN6rQPWStEtCvteW9eorkWt-eUzNH-8cIwK10vx-yGNboX0nN6pcRfwvRmhXTNlvWY0TEGnBsSkPofHgWicNkXgOKwm7keXY-btXjaHmh6Z9Lo1yRAWCUo5me2-j5hakWF46CdsUjxu8skuNMr5lVx_oO4h5_8_5pCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=TmGO-pKUIF5jJjSrMPD0DKB_B8kQs5107JNffrkUkV8JtDYccbwL_k3VTzJklPez_EjjTxc0h92JFMcjTVpgYkicOFxCgdYILda7GwuyP0rc_hB_XUqObNLbjQ_-CrMnFIqIUHdTqsxmf90aYYdQ923ijCg8V_qGYDHCpEQYOBHsdA5i0OqN6rQPWStEtCvteW9eorkWt-eUzNH-8cIwK10vx-yGNboX0nN6pcRfwvRmhXTNlvWY0TEGnBsSkPofHgWicNkXgOKwm7keXY-btXjaHmh6Z9Lo1yRAWCUo5me2-j5hakWF46CdsUjxu8skuNMr5lVx_oO4h5_8_5pCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CI78234pZdBhiz5N7M73aGuzbQIVz5qrkfFzT4q2B4XJGhP6P2cr_ZNSmZEQJkbef-rdlOA8iAdRBdMKXHGsDu737-RtuWtzRlJAowseu9Ee_BMVQsryX9W59AUk1rnO-j9XNayHbwYTh7PSoFnYGUMPKhQeLRfBF9MF-tHQ0mt-rTFpG5Fy78yQO5lB9tnRZqp9L3Iynb4btV-fFXEvPsF6yAuIDPVb6zTjwX-sZGfgpQ5iHtxw7t6D0MCbcwbp4Elw5qbYpB6FwI04zIEb8CppKtvf8t27sq1bjaC_uLW_wL9Lvhd26wPozchdvMugfsICrcNMBJRnD1lZlphTpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CI78234pZdBhiz5N7M73aGuzbQIVz5qrkfFzT4q2B4XJGhP6P2cr_ZNSmZEQJkbef-rdlOA8iAdRBdMKXHGsDu737-RtuWtzRlJAowseu9Ee_BMVQsryX9W59AUk1rnO-j9XNayHbwYTh7PSoFnYGUMPKhQeLRfBF9MF-tHQ0mt-rTFpG5Fy78yQO5lB9tnRZqp9L3Iynb4btV-fFXEvPsF6yAuIDPVb6zTjwX-sZGfgpQ5iHtxw7t6D0MCbcwbp4Elw5qbYpB6FwI04zIEb8CppKtvf8t27sq1bjaC_uLW_wL9Lvhd26wPozchdvMugfsICrcNMBJRnD1lZlphTpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=uJQ2AqRH6RNn9j2bEI6CEZMHhXMUthxLbskn8-oqCXndXTdfw-1spKHQ1jCZKf3G2eNCUCED_s-ss5Xmm2fP231k01Ji7p_jkco8XFWePBQUxsawyCPipLmPWP_JEhhJ17pvGX-_Fs7taaMc-hcKmIO1bhMnleJ_vuoFNYoQP5mJoUj7fLmXXfXjUt-xqnNk_ECPdQ8Q_EgNf6fxjrSBveUrY2goU-3b1n5r0YudNg5GoAFuiZxEUvE3uAqDHpmiRBKXz2WCeHhkWFUYEfVp7Hqd7-l8Qus49Bf4nfsKCZAx3t_3ki913GCH9IwIuZbeWKUfOEXaePkkP_joj98WVbT-vf6QZIUGu0QbtNhCHG12OA6-J4KGxzqI9qUju5cp6s8ceQ9yYkyH_uMkLV36MLlWIm2A2rnvtifK74b93jGq7ciRdC0me_UOOLIhUzNklZwTmjiUci-3EuKjOmJmclC_BSGyhvoQ_zY7IFqe05A5siZvYg6QAwtBjbQZWPcPq7QRADJOBsx6Z2X9ZPyuARuC8pRsBC1uaIhKfAs5lTVZi6REyJ4DIPe7VczIwWIOhMZT1xuHLZMnFGvztHgJLXAKUuIK2ZpBQBfPclP_x0rv-INDK6ymNWYM6E_YtkA0Mr5bwymNIZochz8ShTY3BnuOzx9gMs36JV3uQN7Nkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=uJQ2AqRH6RNn9j2bEI6CEZMHhXMUthxLbskn8-oqCXndXTdfw-1spKHQ1jCZKf3G2eNCUCED_s-ss5Xmm2fP231k01Ji7p_jkco8XFWePBQUxsawyCPipLmPWP_JEhhJ17pvGX-_Fs7taaMc-hcKmIO1bhMnleJ_vuoFNYoQP5mJoUj7fLmXXfXjUt-xqnNk_ECPdQ8Q_EgNf6fxjrSBveUrY2goU-3b1n5r0YudNg5GoAFuiZxEUvE3uAqDHpmiRBKXz2WCeHhkWFUYEfVp7Hqd7-l8Qus49Bf4nfsKCZAx3t_3ki913GCH9IwIuZbeWKUfOEXaePkkP_joj98WVbT-vf6QZIUGu0QbtNhCHG12OA6-J4KGxzqI9qUju5cp6s8ceQ9yYkyH_uMkLV36MLlWIm2A2rnvtifK74b93jGq7ciRdC0me_UOOLIhUzNklZwTmjiUci-3EuKjOmJmclC_BSGyhvoQ_zY7IFqe05A5siZvYg6QAwtBjbQZWPcPq7QRADJOBsx6Z2X9ZPyuARuC8pRsBC1uaIhKfAs5lTVZi6REyJ4DIPe7VczIwWIOhMZT1xuHLZMnFGvztHgJLXAKUuIK2ZpBQBfPclP_x0rv-INDK6ymNWYM6E_YtkA0Mr5bwymNIZochz8ShTY3BnuOzx9gMs36JV3uQN7Nkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=J5ZQwotXDaSC-Y-A8VsGnIzxGZgEDnjH2XPEoHotESHYUiHE0w3kKXsOuY5RSjfETkvM3_QBEbatHUiJMLP0kUbLaiNh9E1HcJ9uPYs1DZ7BeM3CVeN9gUmfRw9W3XC0-cj4IDS0dB07HlkbRB0-ouTgLmyifHQqeOP9vpxgCiilZEB68nSpprZPKNrfbAcN8DXWnHXf8Wxa_EKcyWrKiD4ZvTIs7mCPRKr_yteMBAT6Jk3b-S8Of9NQrS6ZFGk8Rz4AEIpcurCH4g4k0cQ-VtabslrR0Q7VtpaQcpE3rC6xjTsz0X9eX4wbsPXXv2D3FtGkpJ4XsnznckY-lGo7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=J5ZQwotXDaSC-Y-A8VsGnIzxGZgEDnjH2XPEoHotESHYUiHE0w3kKXsOuY5RSjfETkvM3_QBEbatHUiJMLP0kUbLaiNh9E1HcJ9uPYs1DZ7BeM3CVeN9gUmfRw9W3XC0-cj4IDS0dB07HlkbRB0-ouTgLmyifHQqeOP9vpxgCiilZEB68nSpprZPKNrfbAcN8DXWnHXf8Wxa_EKcyWrKiD4ZvTIs7mCPRKr_yteMBAT6Jk3b-S8Of9NQrS6ZFGk8Rz4AEIpcurCH4g4k0cQ-VtabslrR0Q7VtpaQcpE3rC6xjTsz0X9eX4wbsPXXv2D3FtGkpJ4XsnznckY-lGo7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=d3gJshPUgV5_v2DWD-CxHZVeuP3EoP1_hwD4M4xxLgyI74jyIU-uPlO4zVntKIIwwjFWVIE7WlJ_GjG8VgX1RwWCGyx3Z2B0kZGI5L33XEqrUAVzh9b7WT4zHnBSVJ56fpJEEY0hCF1jeHpNhoG2u1FiXeVbqrnRwA3IgaDdsMvMV7KA8INjHcmURoaK1FlkDzbSQAAqVUq2qW1HAexZZexWG11I0JdDr_AXFhNdg-5g6UIAyWTgfc9DNUAGal7dhc0vOTcKvfm-zIesIopHUoOH4GMSfOIUVxy7sqJy5Q1qICDqMQhuRFJ_c8K9A0XkTOB0opNP38acb-Swzg4qrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=d3gJshPUgV5_v2DWD-CxHZVeuP3EoP1_hwD4M4xxLgyI74jyIU-uPlO4zVntKIIwwjFWVIE7WlJ_GjG8VgX1RwWCGyx3Z2B0kZGI5L33XEqrUAVzh9b7WT4zHnBSVJ56fpJEEY0hCF1jeHpNhoG2u1FiXeVbqrnRwA3IgaDdsMvMV7KA8INjHcmURoaK1FlkDzbSQAAqVUq2qW1HAexZZexWG11I0JdDr_AXFhNdg-5g6UIAyWTgfc9DNUAGal7dhc0vOTcKvfm-zIesIopHUoOH4GMSfOIUVxy7sqJy5Q1qICDqMQhuRFJ_c8K9A0XkTOB0opNP38acb-Swzg4qrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVdGYe71UaxBCphSQdHokyIwEttOclcozJh6H-Li06D1Y3bq9LmlINgVbo97njnfVhtojlL_Q1IbkjakRueX9Kp9fls6eBPkN3pV0UAqsb37-3uFUJbw_xM4nMxJfGwVUvSWjshLe_OYiDbSTMEwCESiFJKjqFRUslTDgbvCwXPFNqY1i7wQRG4KEfwmFCWluGOOOKkwr8w9T3jqnxJTGy2A2Tpa2Ycx0hW8H_X1bVBJc66rxUW-sLPGaEXix66vxPJdVCPaaOn3Brfa_I_uZRf8UNZ16iSR8n8a1H7OWqCXUoqHJNYoP99Ud7wFjkHaZw9gstKKtai-D7TskMVdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ2ZxQhLKF6QgKxGA2OF4jNeoqFIcdbToUPdhAd07pf-zKfDOpieO6MdqbMk9o95Bit_a97ZauZMeMeX0xmWx7VnoKAKJYRvZRKl9WhpR5ki0rCoMFkzTtsOVTk9dNfsrcik_uyD8OLbItcBPcylK-rD6k3AYRWVfNACliqE6vknmejhT3uRaufoVYfnMXFGnXDZAPq1kCnvyRDmVieW6BXIWIgYUcBlhX8IkdnlvRXQ_lKEYB-s4CG3CXCrBTbekUWmyzHi8SFZqqNsSlZvcIiQHHp5uQUV6e0oa__zXJUvEEWN6Xv-VyPAef6AQ6YXDjUcYqP9Q5DeoHR8IY4cWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=juTxBUZ-Dy9x4gcie_Gw408KoKbwYwHVZqnzdH68vEzX8M709tWXRy0Mtcj8klGWtbQZwdB70xxT8VtY6holft0Ud0p3LVn50oGFgbt7b55PQ6NL-kTnZ4Dx-hJKdcugjmYpxWFzByTPS7UWUj0YjFQNo45LrAh2P5nVP237aohcG3SObx2j6ifSXmcX1Dvy3c_ukNMImFeNNbaGXy8nGvesbSFXeC_HgbI86c0v6RPBpSonV9F15ahpvCl7JOMai3qi7ZLtaJyUNeMuw84yKt04NnFPuC-3RxENtcytH8S-lVTXvQm8az6xNj0iUK1_nPqcRCITuPlWw7F12If8zmt6S7PB4XLLKq8DSdR5max4Aa3uxl--WkMqNHErTNK1kKLpMve6p8EtIkXYW2nMEc4ZAVjN1AEcLa7xFF7RW4UKb498zTJBQ9-Xs07z-FQaouZYDKhn4BbKluNWHninqTvbXOEZKVLJhdQ_Am_DGcRSVDcspkt3xKTN-IWkJyZ0MUpXI9KdnLS1YTZWcUh1vXuycUNWf53JUdcg8keCEH1KrvguvgHCKJ7mjhtH2u2UWOlj3jCQKbYiGS7SqqYUiSSvEGyrxywfNtja9cIfIKEt8D0-otiGpG0PmZzwzp_4e8ii0srTp8mGQ15wfMtH9xL9q7YqV6QzVT0zonKsuxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=juTxBUZ-Dy9x4gcie_Gw408KoKbwYwHVZqnzdH68vEzX8M709tWXRy0Mtcj8klGWtbQZwdB70xxT8VtY6holft0Ud0p3LVn50oGFgbt7b55PQ6NL-kTnZ4Dx-hJKdcugjmYpxWFzByTPS7UWUj0YjFQNo45LrAh2P5nVP237aohcG3SObx2j6ifSXmcX1Dvy3c_ukNMImFeNNbaGXy8nGvesbSFXeC_HgbI86c0v6RPBpSonV9F15ahpvCl7JOMai3qi7ZLtaJyUNeMuw84yKt04NnFPuC-3RxENtcytH8S-lVTXvQm8az6xNj0iUK1_nPqcRCITuPlWw7F12If8zmt6S7PB4XLLKq8DSdR5max4Aa3uxl--WkMqNHErTNK1kKLpMve6p8EtIkXYW2nMEc4ZAVjN1AEcLa7xFF7RW4UKb498zTJBQ9-Xs07z-FQaouZYDKhn4BbKluNWHninqTvbXOEZKVLJhdQ_Am_DGcRSVDcspkt3xKTN-IWkJyZ0MUpXI9KdnLS1YTZWcUh1vXuycUNWf53JUdcg8keCEH1KrvguvgHCKJ7mjhtH2u2UWOlj3jCQKbYiGS7SqqYUiSSvEGyrxywfNtja9cIfIKEt8D0-otiGpG0PmZzwzp_4e8ii0srTp8mGQ15wfMtH9xL9q7YqV6QzVT0zonKsuxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3qz9n0No3P0vPCDcA_p3NQ4CuDtduG-iDjYG1qRRnL5GsKAJFGpSn4LSCTnShdRIlIRcdjSDBOhIX2K4lXrGO-dU5tKTzH_LOW5sKuKTv9qk_hvyMIZXbxX8TfyNDHNs-D3uirJlQoFLjMlJOmMLUxUwj2ln-ypyR0uykt32fXxzjeZE7C-dVGngWcM07h26QGFfx7c9Ap2mD67ew-4KnsM7jh8L-5BAiGPXiS7NJSvR0ZBlzHM-5cfEtDhBnSdycvYkU13tt2CsqWX8klinWxUMPDvX2lcqpm3RTutlqLaMPtkCBUw7XuFcVbLYivwvzFVifmaFL2eu9sN1ZJ01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjcbdeC27Q9-UZkJSVaolikIIIhF85DqRr9LOSdhwGGY-5CQxYOenymkzWu-z1ItQrevZwwrKcojm25k5PHaK8P5W85pPbrkloVjenQfLcdldmTOgGhfrfrfzUZsnD6T-Y5ZBu_yuBCZMjhx0EzE8KlEWGwj9rA04ATU0XPiGZuSb8-fOAr7AeMpmZ3YJe668YXWDO_eUuOzBkQIJ1YKnTjnYp6fRzfZkQmdl_4KxebnGA5jwR0axKVwbZK0XcAStgZcSK0UB_mNBaDUJ9azRURHYWH2DpGKFWvZIxe56vv3a51BNdrB33ZmA6RxLLcNJf6FuML75qKrjy3_6O71aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiF7FrUgKYDXESp6C3uoxEH57pWvyBVZGn_gX1YIpZQxS_ggHTpmsio62YHHNBaTcj8YkAptK9Eqk17Rs5qEFdySAq45TxcAeXrd4RKjm47T-7ndL86fpPtQa_6XYGqemIhwrv1HnFDtrliloNusoEon2nNC8OKkupmf_ojihiNyWxSm-1zez2FW8_RaBuGqsYcjphN2twpJzqMsHktmNr6Ykz48646TDWi41ujdeQJFVW67u_vqarCQ83pElcLkTQgL3Gu5-aQ2KIxdtqGgTQWf041T02h3_L9laA6KmfMcF7i_jTgE7Jp_n4HCEWbFQZhA15tRk28qRGToRuIMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
