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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3p8nGVBQZKWfT7-W-7YZkbhfFCftZ_3GX640oH_uNJMbZrKgoMMTL0lb8KexQfTLEd1RjPQKJ5LfAP1mzgrPEytBwMC03Xyg4staI8mi2WfeYFvm6lAFy866KngSRTDRxZ1OvLhHOA8S7RDop3sNu4B4z8WvEz_UBhmVEC_DM9PmI2byqJ9GxhREf_JMxDa5GNXS3-keCTcynFXDVNjbw2ISvE0kenlGVpZ4kkUFz750vodKpi73uUArPB3TOfKHyqhLoMNj6CiTtHNLeJT3uxO97Vjz184w6tf2XbLivCK83Ckr4Hno0uDkefnhwpPCvngykqDnH_gq-sAVHt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NslFIUbLzAd-u3LxjhpKY4PaK6e-vK3Aah1hhnPQjBEkpIuHuNIlJAKr5CI87gRDbCIuRupbie-cKK-LgpbY_yyiwhw4uAcc26-I7vhMtxyu0BpOLfmwbQE2O6g2r7tpDZBRB5_b5ngC5xrtYos9-9cDIwPcy2tNcBWqW91_ES3yFptpIGEc4vR4IKXRc9bQv76nGeEFp4dh5rxYVRNleSN6fh_MzNGwf63KW-CJT8qo0FdKs4Xe2clsy4wT_yguk-o2rWHcaL0tqfFhU42jKPcoyC8vEwsqAahqruSB6JEp7CQ930C4yh_fpkOqfYG9ZQojeq8D_PjzOITYtFEx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9OVLQHBYnck8r4an9MLPeSdj0_kEssPky4S7RrX6GQyQiAobeg-_wsLyBuo4Rw1mHS8hqSIo_y2TkNbB_0fDQJRolfGDvfqD7ZCNkTD1ORIAWndlalrOlM4m82X986ClzCLOkPLL4D1xGQGJtidh8n7tCzlYhAz-IlJ2QOLqW01IjqMTUSQcBMPV6h7slDaHcqDaqtme0CBh_vQHCNbSx8kd7XWdMp0k_tl1s50zt56K5b75bBnJXp4lET-iD6awfQPO2ouTCTIz8f7Hq_HWnN4HS5VxudNTDOUbJ_uiaXK2ofcrZeP0rQSoh6_Vj7Z0QhVTtggCy3k6ARn0cTZ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5y4Ua6aUe7oWLDp1H1yPD6RcoyYoM3Yjldw2UB29O0NAvFL29pVZGtdVi6TOHyymZuBAYPzLCsGZGa0AZokFP-eEG_2jXIMJLFEzBB7TkgjkCzRgUuKjEBZMb0tvKzwN7DmdHZs0PC9Y_BCD_p_nGwxT5NvZeee7NFd3QULqThBvyJhPb4nnQZqsJWrMZTz8E5y9oOv_w9sBYQCN6QJ8lE4VAIKxJn7Mk6mNH3HpuISp60YznKcJWf1qqmjnTq6B1uxonB5oK2lL-j7YKaAQTZ8y3QMVHDBpzqDUjGxm2cM4Jg5dMR8XkR1Q41xTivg0z1K6pt9vEZccE293xHB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akYabXVNSFGIHeMgTbtpQBHEK6vH7DP2HNKR0ViU7vZ_dItLxhop4AgiDe97nRPgOgecu7bxNc9Gs8rR5fH3A1xquJ-OtfyE6TnGHYkhALZgknFfyoiqPLq-GR1m9eY9fb9M4llqMuoIv9282y4HsyB-ZCJUOHjzOAnNC6Ee_ZVra8kFeeUPhMMbROix3coTrUWZHlXjrlFT1O4DDUAPDEplO9B38LXD-bfGI2ZxjSMn3qW47i_0wvbFbAdKorYkJOV_Wsp07NwfEbgVLsxylmo7jl0KUJnY_DCv-Y0oHlbr64Xg5Ju8yi6Nnq7lRBy_GxzEkT10SgfzNSM4zKASfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbmZs2euICu6Mh7wPG64WkuhuZvJ3VGaVOibTaMDj7luwlD8MY4IfAaE-HuCnxW7lpVqrBxO8waNSq-md9w9UJrle077rhyAX3u6UOjkqculgNS0Av2njxI_taLcIXzPzmO5refSRWTKjLWLqSY41GYh-FsUktyCWca4Tjb_K4nh_SZtPzTDCi1f4qNaZe_bBPMZVBhWw7RBhwSOhLGiL72v4pKY1b_FdzHISTS_vAIqXNYclHOH_p8rTuvREYZq9pJsb-5UjUzVMTNXQtvG6nxvg5xLemonOeS72Von-hckN4bZ6Z16FVLdlGmY2IJ_85zPZ2xnZpGSdNniC8IBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unP8SpwX9kw3Uhe6V8xmOT4627xDMU-TWafKHtxc39uBfncf51Gystch3cPQYwyGdF3Eu2SZaC-qkYxU7pOMu-3nAa-oZN1zX_60KXMoGXUh6AdOnduog8iTyrVn-6lAn7-D1gYLPgoasPxaE7iif1DpUaAiLS5h15NyrESojLkBqgcaYIc3knHoO5k5KVlTXD7My33K-r0MZTGeObAPcanGBOmvkKcJKpaD6vhF8xYQnyd4W4VfyPoujXU2SZOUFDrMYQcgLqrDZ7TF8QBzykza6BEF7tFL9e26eGoX6lluUwmjbaaMmswUUY5lOWUo3yUVNWFRaqMmS6dQgpNxpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2G0-ah1cUdXK3Nh3TL6v5d24RjpVlZCxFnQa9PJN-Z2DLpICrWSOuBfqsgoZIZ8SgZY6YqToTGVFwa3ds32Fx6bnfXHOU03vwrWJ2Ma5B7hT-uNCKLCTlLjAYG9CCAMOd3Jnot7eewk-lSiAVOao2z-Bn_wLdfAp-k_OCDEBGoWVGgUkjj-N7PaZevMbOlY5SQ7xcxgriVRFy8whMjKOq41d1AI_TPSeTdSpgVw0LdX2eHhpz-BC4PoQaNOPCTleI8dnnY07nkEu7nZTnmFR59m0hXVMHjqLEgUp_-lCUTM0kj0IZwxYDvUjga67B4z7PEWQoeNbNOG7qFc1xutwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=AEo461K2DzynhmQI0e8BfzeMK_hF-DBAQeNpFnFS_tRSipx7VXYpcl25CIoyYCvhYu-yGtqBVb3BVm9_Lz9kZM37_0HbOcesvk1ndw7H6ZS-nN3p1MmrdfEelb_icjlwgBUNorWzxylHbfBimN0zN403gxRpvspqYjfNsVKeBYi0Jhd5hvxqHZdTlzTjOdkodzTgmyf7KBlv5zGZcLADP92dSd6Tms9MH0j_f8chp_HYNgPiw3-Z7RlkE7WuIWyOOcg0TXCgdcJK6a9wOxjdvE71ZAbbcN7QkC1R7K37O-MqvCLRp_TrmxM_vhu3ZZEe3BD4nRRUrQhu7H3-QuNwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=AEo461K2DzynhmQI0e8BfzeMK_hF-DBAQeNpFnFS_tRSipx7VXYpcl25CIoyYCvhYu-yGtqBVb3BVm9_Lz9kZM37_0HbOcesvk1ndw7H6ZS-nN3p1MmrdfEelb_icjlwgBUNorWzxylHbfBimN0zN403gxRpvspqYjfNsVKeBYi0Jhd5hvxqHZdTlzTjOdkodzTgmyf7KBlv5zGZcLADP92dSd6Tms9MH0j_f8chp_HYNgPiw3-Z7RlkE7WuIWyOOcg0TXCgdcJK6a9wOxjdvE71ZAbbcN7QkC1R7K37O-MqvCLRp_TrmxM_vhu3ZZEe3BD4nRRUrQhu7H3-QuNwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEn03-8MAtuRbnOeidA4Gsc-_G1jueXrDLDYFi_bFXWCDCXIQgcUZBu9KZ-OQBrG60fubYgZX1sPKr_TN1Orjhj_z3iAq5w5qMXPCVc6W6YdkAM2tXJ-5v9VdvwzY5-9MoTJ7V96jNdiruLAViGmwD8Yjo1blhJ0sueEAQzTo6XleoAuFpKWZtAKIBtBcQ3C4X2ShCQ7ZlJpekQksTeR1N_kRnDM9pi2N446TvDccQTvwid3d7Q3Pe0QMKfzqHwjawBon0LuKmTTTIPPUkwfeh0JBcwie5AWX0liYvSUmBrwzkxRrPL2j6riX1KV2UjSYywR0aO9dtlU0JlenHiKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2XUr_hKD7rbsXcACJJ40Epsf5cZRfZ0SoOOrFmH29IrNfGAB_FiXZkvn3G_obZDQ43S9obvJVKXlMlYU201MAnUOaz7Tix-k2lMa1-H48CQF11emqVNGLzbmPWcFeHOSjPLW1mrV9HUDB3dpZCIYSPDxfbizT5w51OQk1N53SzM9NLArkpZWUN-SFbDSwt3F4hRNbT3S42alJjNIHH9oK97Yx0_t9F7epqfgGKa4dGaaU12DS_A6Aha962EbuX5eSOZGB8VHWU_nrZrcvxq-IpcaHT7c0pUAIH8MqOEDRhTQP0ZqGgXCErzQRAtp-iy6MwVQMiwskpA1ciksHyVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZw2FQfmrWkKpu7hTSTjxI3rmzEOdeoEQzv1uBy60hHZIULz0xnLCLk8ntVReC-1HUz_le89ov8yM3L_FLtFmGxMKCI-qy4TjFZEnh9PowteLPt35ftjMA3BmGyXbTSR5ntU8hPvGp4ufJbgmk9NGcdBUZ1uovFP0FpIiuAAxs978ZylyFzDstBCwL_nr7UzWwFBoOhrwycetONa1Rs_0oY_Ezq_ueHL4r28VujgJNTJmbnuMiGOkrvhbq2wCqSqVwgY2iXA4qlwpoaLKtap1OIwLg19aUvLTIfpSkG4Jg0BKv7VZKZYFS2SVswP-Z1sc27qlSh4LcXXKrpTVMBN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=LD3stiD70CEy8o4TH9D5Wr3OzmJ-fuNm1XsXqgqfBz40JwQscGTOPZ1m9zCxNJKKUmgNS1VjezLBDTGeYNZ5VHNZBkSlp60rT71jSoJxZiyGoE6geFn9UmuDOQQan67tkjFUPyBCTnwal0hBHhQdujelLGtx8WY6UMxam7YLbpFHq3tv5-CENzBxlh0LiL1zkclUBd_QkVA34mdAWB8XhraQqkjqrQuqD6ObnPMKJfazZDtiNE-sErkS_HdChsuCfYuSAL0TQBfeyWI8Wa3nHmn_pxEz-OgUgqEp-33MVl8nZMdRRGLsEgz2fyV7CdLyjXaNzWxfW7t5Gd4--gp_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=LD3stiD70CEy8o4TH9D5Wr3OzmJ-fuNm1XsXqgqfBz40JwQscGTOPZ1m9zCxNJKKUmgNS1VjezLBDTGeYNZ5VHNZBkSlp60rT71jSoJxZiyGoE6geFn9UmuDOQQan67tkjFUPyBCTnwal0hBHhQdujelLGtx8WY6UMxam7YLbpFHq3tv5-CENzBxlh0LiL1zkclUBd_QkVA34mdAWB8XhraQqkjqrQuqD6ObnPMKJfazZDtiNE-sErkS_HdChsuCfYuSAL0TQBfeyWI8Wa3nHmn_pxEz-OgUgqEp-33MVl8nZMdRRGLsEgz2fyV7CdLyjXaNzWxfW7t5Gd4--gp_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SODr8hg2EXcoMgT6HUac3qffXiF2zXh7Tg6AnpRdbeR1j7s4YWD_TBSLZYML2rZ3xwLZcnxA3l3UQGpSjeEU2xkZhGzdHv6f_djG6lGDmJfqrJQAn1ln-qDr5_e5Py6ylmGrPAWp9tgNCsh4RO5FVYGppRXEQpbgNzqrrfzldZMSEulmg-RVuH1GTXO0zgD9w8Re5yFJQUzLy9YnfgMKCqvwVemx-SDeETk9xdwTfNmYkC94apzL1TzTP_9X9Bqx4LYE1jmpuJIKBVdhn1oJUPQqBU-lwmc_zcoozCLnyAIK2ShyTe9FlfiM5b2hF_9Pl6rvhSDGWTVgit1xKgYnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=F-aWWOmGtXDzeQ-yRZ_Ua_gL_Os5S54dGiRsf_AQG_-qMSmvyE3SX6Tah2NJc8WBAWRaiM3QcCwouJf0SOJ0tBzpo3DUB1eBODkp-0est2jwhAO6NKAzsDdcmN958151exgTa51L5NYxvFyDE-5crWooqWjiv5X4kQz5NB6V4S1udgpaPTsasUDJsD-ufDXki-hvuISS5b5smITz4fS_ameyorgWMefUd6YhcrptzdPfcJX6T2JntNV3ksi-nRx7ynjoRM0Gte4Qj0-prNzhzsP7Op1pQppSD_xVcZGQ_GVYnVx_jTlntw3nqPNdifAHQyFLbABLBlTlqoskI8qXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=F-aWWOmGtXDzeQ-yRZ_Ua_gL_Os5S54dGiRsf_AQG_-qMSmvyE3SX6Tah2NJc8WBAWRaiM3QcCwouJf0SOJ0tBzpo3DUB1eBODkp-0est2jwhAO6NKAzsDdcmN958151exgTa51L5NYxvFyDE-5crWooqWjiv5X4kQz5NB6V4S1udgpaPTsasUDJsD-ufDXki-hvuISS5b5smITz4fS_ameyorgWMefUd6YhcrptzdPfcJX6T2JntNV3ksi-nRx7ynjoRM0Gte4Qj0-prNzhzsP7Op1pQppSD_xVcZGQ_GVYnVx_jTlntw3nqPNdifAHQyFLbABLBlTlqoskI8qXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVXDyHXBVlNcgt4WdUW2tYdQ6FKjpCfXPEW2x3m9kn4LA5E_4l4eKss9ZZl6QVA-jYj26xfnJy8WrzcF1zbKx6RP8uAO1uFgfdKrsaqKFhwkFyZCnFnfNjkgOFBqoI3Ravw9Xz1QKCke8tjsBhoBio6CUjAiB3kHY73PQoMEfWnheOBvYINsX9IVKhdUl5Tx7PROZCxoInx8kF__MSt5ab02nA8f9uoDBfiIcRMkMMZNQBZ-NWqZVtB--fKtf7KSWphZQyj0_ElhpI2whZGlZ0bf0Ld4syAdNNJ__7gSUb8NU7FkpWfi9rHxLVi5t_yDh34D-IjHlsOMpNCoObW34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ14PqUQQsDUZxAc5UhGh_Eg-LwJcmlgOuzefwAU9rx7uPAWu6eadrbIBcZLoL6fPPg0hvYBD44WkqQEds-W19vD5HzTirC95foPczVM9BglaX4ZTEqIuNVWAbeibHTTlFA6RRVKjoeGEggTp3rg1rPomUgEGjzY-j38F8zsQw1N5qv9AgB2Njp8WE-SzOOS0Aho2you5wnJvr6grTXW-4A_Pl7oHsGO1kmCu3FpwezT_ZzOzdnka4pKvVsygaKBIdM0EMmZUUV5G0YcZZgKJXE9sVqeusprFRDLQIUa1Bsx6eIY6cgFB-WHB2Voj_UCqHcgL0BEUNIkEkG1yeLIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=kjGM1MKg66tfvGw0Jig9mSBhyD3ElG0DZPC5kfiMpIgxcHRsdgsDnNcZUSD-JruSwnkUtGtTZ_65kt3Md66ZmtDVNrrGLBFXNuTTx_pcU-zKIhP9PFM9kVKRZ4gQqWf4MEu-OKSujzFaVQRv7QbDy6g-PWnF48ACCDXZyS2H6eFnejoM27xy9Jze1HWzYAd7kjPfkwmqd-SffxnSUPX_iH-BelWS9L0KxrDiEHB4x5OdTPzbGdcuzp1ThL_msIx-JqL3ZX2X7V5SIIuC_aPJp9v1l4q8IsxM57FePzpvBMUnAehNCi4XOzxN5OSPeXWCuHp9N8mT3y-9rWISOvh0ImGx3nAZ1LE5Ql3pmPG6zQ3dDfrrdpbKPAFQsrGK3lGoCJVrtyuNVxtTUi--r7YZ2hcWpXm9LPmMjvA90wcykfnoJ_ZNmZVSrwmu96D0nEZGkCHp_OniS_pF7foxXz20J-3ZHHfDMk75K8NLA2eG-odQCspf8_u_hGRjB7J6_9YmHqFKKLOF0tv8imrbCXku9TcsBcyaLCpSHddaA9VF_bFlBpch9lHAwEkW3JwJJlJ942XeFwSDrmi6PtiBK9T6M7BkLxuQliTdJFnwpqzAoD96y_19Fx2imr8FzxHYcGri8I3Fd6A0IthF23is9AbChJ9gotbN9TsqW8JcAgARQpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=kjGM1MKg66tfvGw0Jig9mSBhyD3ElG0DZPC5kfiMpIgxcHRsdgsDnNcZUSD-JruSwnkUtGtTZ_65kt3Md66ZmtDVNrrGLBFXNuTTx_pcU-zKIhP9PFM9kVKRZ4gQqWf4MEu-OKSujzFaVQRv7QbDy6g-PWnF48ACCDXZyS2H6eFnejoM27xy9Jze1HWzYAd7kjPfkwmqd-SffxnSUPX_iH-BelWS9L0KxrDiEHB4x5OdTPzbGdcuzp1ThL_msIx-JqL3ZX2X7V5SIIuC_aPJp9v1l4q8IsxM57FePzpvBMUnAehNCi4XOzxN5OSPeXWCuHp9N8mT3y-9rWISOvh0ImGx3nAZ1LE5Ql3pmPG6zQ3dDfrrdpbKPAFQsrGK3lGoCJVrtyuNVxtTUi--r7YZ2hcWpXm9LPmMjvA90wcykfnoJ_ZNmZVSrwmu96D0nEZGkCHp_OniS_pF7foxXz20J-3ZHHfDMk75K8NLA2eG-odQCspf8_u_hGRjB7J6_9YmHqFKKLOF0tv8imrbCXku9TcsBcyaLCpSHddaA9VF_bFlBpch9lHAwEkW3JwJJlJ942XeFwSDrmi6PtiBK9T6M7BkLxuQliTdJFnwpqzAoD96y_19Fx2imr8FzxHYcGri8I3Fd6A0IthF23is9AbChJ9gotbN9TsqW8JcAgARQpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=SBu-yCaB5rHDWofeZpOIIC4zqsGdP5zB_vJHmCOp9aWNxt3WQuS0piJg2pAGstsmULyw0M0-iAFo4PTzC8fqY7_zVZBJJCWBhdmKnD9CAJ6CyYA-OfX575PLCu1bmm3IPeTYLcsFgwG2cYG9UmXsW2C21sMkXybETfgeVIiBvP8HK1UJGspVhTE3u9au0o18eGcO42pATKLJLX4IPXTuQ4coRYpgzx315K1lKAs-jRZdjfmwQ2Oswe48xJDhyOuPmSTXAwa75v4Z40Kg9SBGVQVqt_0_wzqzHzpXE2kzTZRsVDW81ZbFsx0HmMIWy1VCh2WGVAvAW5KQWs-h28L_jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=SBu-yCaB5rHDWofeZpOIIC4zqsGdP5zB_vJHmCOp9aWNxt3WQuS0piJg2pAGstsmULyw0M0-iAFo4PTzC8fqY7_zVZBJJCWBhdmKnD9CAJ6CyYA-OfX575PLCu1bmm3IPeTYLcsFgwG2cYG9UmXsW2C21sMkXybETfgeVIiBvP8HK1UJGspVhTE3u9au0o18eGcO42pATKLJLX4IPXTuQ4coRYpgzx315K1lKAs-jRZdjfmwQ2Oswe48xJDhyOuPmSTXAwa75v4Z40Kg9SBGVQVqt_0_wzqzHzpXE2kzTZRsVDW81ZbFsx0HmMIWy1VCh2WGVAvAW5KQWs-h28L_jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW_FwGNtl1Zy-P3i-0c2CkKzdY6NWOxlJYBKW0HKSNj046LbzGnEeDxTKNU3bhGR07nsY1nVuXE41-PENQ8yOFIaAuUEfl8uGHPEmJVMY2084wspuAc1OvBTZzVPmFBNyw_m1dWmOnIw7XDLjJ4X_Ril2gn8NbgXlxTTeNXMsmxelNzLNG0_lYT4CFhja11V7xRXXbFxybHaEOKHlcilQT8Z8uowFuvTY5SFctWK6VKlb3_OQEpye7T6GXT8HOzUYqA63t4q0IWE1CknohRMlc0ftKF6MeOgMtHBCgQVAzoI40kO9DXPMIiASwMm7aiUUxN84xKpJpEQzuCj0TU_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=gvoXYAK0OxhBjytCVX415xkWEx5802iWPsaF6NmxCpTpETb9YCov_yGKF53VsDdMM6V1j1WQtqb4eUPf_AP_S9Rru2IckjdSBCmFE7mp3JILdIV9075fF8Rd7RTD37bGLFVdkAolVeqzhx1hxXEjDng8T8G0yAZBGFjqgqMOSAYek_iqg3paR236C0GKbR2cE_-Oy7ruQCxParjeqk31Xce-WBuHI40UEOoy8qr4wvRfQtlBHh3yT6Uynzhk0RscZnuJy14Xt-n7nFFSAKAFZDjYwpStL1OYF80JCduH-WBGyfleb5-wfmEO61krCJVDriN8aZQarJ8FbmpHv88cLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=gvoXYAK0OxhBjytCVX415xkWEx5802iWPsaF6NmxCpTpETb9YCov_yGKF53VsDdMM6V1j1WQtqb4eUPf_AP_S9Rru2IckjdSBCmFE7mp3JILdIV9075fF8Rd7RTD37bGLFVdkAolVeqzhx1hxXEjDng8T8G0yAZBGFjqgqMOSAYek_iqg3paR236C0GKbR2cE_-Oy7ruQCxParjeqk31Xce-WBuHI40UEOoy8qr4wvRfQtlBHh3yT6Uynzhk0RscZnuJy14Xt-n7nFFSAKAFZDjYwpStL1OYF80JCduH-WBGyfleb5-wfmEO61krCJVDriN8aZQarJ8FbmpHv88cLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn6tV415M4fxbdcxjUI5oDKKPTeOLbJ9qjeYHsBILd0vGBD8Wd81E2rKZausMzfxHO8heKDWJ-eVeHyVmsPsLVWyew43arfu2Lt7UEFz2ZTkFkIxX8F3IASw7VoTECHU-20EY3xAQoFEGKCdc37USXOX2TSFeErFCdcACCI5LwlS9dEzNImV0dCKfv-V7nxbYHDMF5mOi7SR4RH8gsdr6PtoItvV7YwlJDJQyxJen5EQe6NnyKsgM-hTXmOfxd5_mvoDI7NjTHyijGNKbM8cb6HX2Lo9_DMj2m4jHHkDtL1m0dr59ymVouZmdqZdtxFwwLKkkHWLmHC1kiO_jhcyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt1tkyrOvjul63_tEuUYL3h5zN8KeBcDKoR18WLol9brj0JIOMKR8Kz2iSvakujrPzjZ3kD_W7eaKp-O1y_xdSMutOaZsXXswuRc5qXtDfkyJFPYr98-LhjeqSRUeNxLHjbYjL6tzb49APXPiZxb_11eLA6tiiCzpvpEsXTWJw1ljnZcODr19XFMoLi6ZFhLqph6Yu-PpX9_1CvY7vY5Rv3RX_C0RXEJSwSNdT2AfF_kjnMehMyu_MKYYkaydhz1MvK5ZNspV52fsHLJNPN45_dMXc2cPAX0rHle1qcX7X3wzH7SxO2rxrdHDlvTAu9pmBlQO7AHBvFay_9ocmzHkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDlxRQ6UGNxwRoSOtD8hCSOXhWkwk75Hvt9FgNMFRr7Qi7g_2ZjJMSFwqM1OgUjoW0L3NUhXA_cGNbiWlU2JelOPofQNHmYhrQ4JFzxbmRtlF4oJTGnFFNjqWZ5Uf10Uv22mUq9RND0skMXfSTVJ_sd5R_LT-SuQPmtQ5s659lPlAcJA8-rsl-wyA7jlH1JqxzncbAg_1Xft1PBBtJO0KP1p-8rixEOfkltxg1dXRY0bKCCWX5M3tKQUGz01LINAzwK_nBSqw4BVMzuPMjJjar7j5Fyg_kR3ilC-StlOwT6rUw5bsEdC4x0vhGjl-ohsrX6YsWUQWuXv4gRTtITpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxcsIBIRUqx2A9BVYeiBSc3aYyySTV7r1teP5zI1r-iUwS9VuUOA6Ie4W8ifrM49xOmaY3z_WMY5PHqi5zx9k8CQKRFIMv64sjlofi0WbRxv2GtvgitciE-vinbxyIpcbU0hejhtjvmwc7fImdrxqCuL-nnjVRZuVzp7EpgP-B-7ZFsj3QKi0Z44-WwsaslZBRMmO23mNhtmoJLSAtRr5aLFzOaAkFQv7fDrJxVO4JCn6mygcqUJ2C5_tbBSmr-LPOnAMpHT1YUD_5xltbMSVBgi4seVvbyoS8G5M0b8hclpXvxSVV7XYaBLydKtwAqMWQyfgvdKCDU2RFPoLZGDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEsJQDF_m_ZItE4rWwmyLjbxiLGY8vsgNp8BKZaAVgTbaDjwc0KTTL9drX0KluTc8tOISrEt06fSFT1VS3MuciowZCObFXX6c47QCapxU9gMO9oxLw1UFs02tfXZW8zQncEC3M8jjBnfBxNLPCugX5Px2C2xCxQqLXtYW0Va161P2YFzr4QOwEDIcA5ZuXzk-5t444DtVjaGpLPWzF9k3GcnQjHeRouLSLoDCsIL6XoHIzn7S_6frKiFxhgWyjIklorTC5newxgp2m-do52TuRLrMwPF3s79Ljij_5iSVS2w5B5tkbgpG2zwroItkX_srbDNKsKlRi534E_GzJxCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=VXHNTdrtLkfVi4MdkZBZHK_hFf1ZIniaqJ8D50YlywZOTVNLtNVgIFKPaxMZeeFxnqX9Zv-cSRwqZpQ9ervQz_FKrF6cVnFsG8BQGIWlQcxN8T76BXiktfsiGgh7yMNRR1RT_agsW1yeS93szsh1wboU_OoJpjQQbwKkYxX19V7DWKxPJVPWngbIU4hvGWpFpRMte1eZW-md7TxKwil3IlLqz4s_zPIVcQejn3yraGHux2ex524fRoFMpohA2u_Jxs19ntliVzS_zzbTU15R7K9tR8jBNycxr6KAVK8ItzYvX3nTgCkYP3aSNfQ39_tUwfM53GfwlXvqvpHTlighxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=VXHNTdrtLkfVi4MdkZBZHK_hFf1ZIniaqJ8D50YlywZOTVNLtNVgIFKPaxMZeeFxnqX9Zv-cSRwqZpQ9ervQz_FKrF6cVnFsG8BQGIWlQcxN8T76BXiktfsiGgh7yMNRR1RT_agsW1yeS93szsh1wboU_OoJpjQQbwKkYxX19V7DWKxPJVPWngbIU4hvGWpFpRMte1eZW-md7TxKwil3IlLqz4s_zPIVcQejn3yraGHux2ex524fRoFMpohA2u_Jxs19ntliVzS_zzbTU15R7K9tR8jBNycxr6KAVK8ItzYvX3nTgCkYP3aSNfQ39_tUwfM53GfwlXvqvpHTlighxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX3H3ipWgjWdhZ3Po02w1hqigSPBTB--_85v3FcWPUUir1L6BT4MjtKLH7VZL8lYLCemJiPk_aZZXqPeko5CasS8oqyxZMKJgeTP1XkG-bcjtK9mwN_cV6I9jXalrKVfBUBISwA8ztjUP2IvRcec_cIgqD2dW0-uWOjFSMLOd3XTc7yzDxhzgWkdQ2HtaM9jNqXHJjqF-nw2AIHJz1qj1DyN_k-1RGUEnT1bFNdTBdD2MK-94wJFUA53nLVQr5G3qNK2Xz_G3Oms1TyNi4XLCLL_JuwJ9_s6f4gbow8cGRr9dbLAhb5wHcpormKJvwizYIdd3IDxFHsE_eK__psJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OelpcMtAHig0tJj14rwfMOH1f_2FYY45SnbQY7BxoRflGFZwAaI3BzyTkmBJo9XhMTs1tXYiTSKduDSulxzpzkvvfUnwvaynx_q9tFUK_9_OaJjpdaSQbUW8MAg7DhyFxBPhTld4raLALCa8RDfHcO5CUSHcNy59Rnzc4TG2EHg-IAKL7x0B9JncKGWvgEhx5dzTVczfr7zRLYcGkX9jKrTRLGZ0EpN41byO3cLXBk4370k3rI3rs2zNAfK2CZ24PrXOLRmls2H7Om9cjUt-gUH3U6bxLNbbHQokV_kJWJSgXcHMonnfTMglRroz0sfKQzRs6UepvGo_9NK6ZkQORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=P7_5aWcD3jqyYXvmd_ss3Mqjhg8lH0oLgRJN7ROZhU8m15XdFmpN4YqUarzfXo-waMW8EA9tl0_fSVSickTRY9ZXII5uzJQE8vuHur1ByQRKjRM7cz5X0fA-PEZGI7B2ovoyynxQYrZEWfh3o7-6riXrEZ5p-mb3wLk6GBzfKOcPPNCsXCygrzr-dIm18S5rm8_MmwICZOXXGFLa3fiZUKjr872M-m3l34OCARTRGsogW6cRWBMViVsewL2hx5SoIuTD5C-H0RksEAbkpVzWJDuxut5qHWuLHZrV7sz4bHAky5dfVh2EURCrVU2_7l7f64FghwHec-XlRrqvOpbVWUeQCr-V0OJ0eluUqg0ZrTVaPeHg9BE6soYB19fILa7UO6hf4h7m8fGqFyWMtDdMLW9epfrC60LadJdzkKNBGfyLnbjNt-iYHRLgd04Bw648A3Om9XKlJpEc-aV4SFe9cJZE03ovJkG7yC2cMTodIhIQEk3ppUgKY4ZqTlDnTW3nHdL-1LMfrMjC2-QpBE3SYI-1yaX1ke2rEU-umufegyMdfN-4tUW0fWfAijhlFWXsM0_uOrUb_40iZW-tBwpa1I4TP7XjuGHgfQ9o_xzmwfEoT0914ZlSA0A1f_ID7rVC1VyVxLXD-1D1R6TAr25OpHS4OH03d1ppLg6eJ3B8Y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=P7_5aWcD3jqyYXvmd_ss3Mqjhg8lH0oLgRJN7ROZhU8m15XdFmpN4YqUarzfXo-waMW8EA9tl0_fSVSickTRY9ZXII5uzJQE8vuHur1ByQRKjRM7cz5X0fA-PEZGI7B2ovoyynxQYrZEWfh3o7-6riXrEZ5p-mb3wLk6GBzfKOcPPNCsXCygrzr-dIm18S5rm8_MmwICZOXXGFLa3fiZUKjr872M-m3l34OCARTRGsogW6cRWBMViVsewL2hx5SoIuTD5C-H0RksEAbkpVzWJDuxut5qHWuLHZrV7sz4bHAky5dfVh2EURCrVU2_7l7f64FghwHec-XlRrqvOpbVWUeQCr-V0OJ0eluUqg0ZrTVaPeHg9BE6soYB19fILa7UO6hf4h7m8fGqFyWMtDdMLW9epfrC60LadJdzkKNBGfyLnbjNt-iYHRLgd04Bw648A3Om9XKlJpEc-aV4SFe9cJZE03ovJkG7yC2cMTodIhIQEk3ppUgKY4ZqTlDnTW3nHdL-1LMfrMjC2-QpBE3SYI-1yaX1ke2rEU-umufegyMdfN-4tUW0fWfAijhlFWXsM0_uOrUb_40iZW-tBwpa1I4TP7XjuGHgfQ9o_xzmwfEoT0914ZlSA0A1f_ID7rVC1VyVxLXD-1D1R6TAr25OpHS4OH03d1ppLg6eJ3B8Y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=OpQMhnyR7CzdgLnmFHW_-elkNSJSH6hqdghwKdg1hlY28-Bl8HvPbacpzLUioRVkPmTc9alK-bsAd1EoOW0y2c-qLtzEJvS2mfAeWCWLAT4v2sa38cW_n19GhUIS82dnmEyWZvyG0x5mF4Zp89Hs9-R-3gL0LdUTpV5Xfwo8r25RrPlHEyDPoc9n4ZIpJSA7dm7Z5D4AibIruJh6f07WhOIOhow_vJamt_o0DPajo4H0JEbr8gwzOxDDMmMuin9wvkIk4sPP72U1p0s9W4v14Rtn05oidduFKHj8fOmTwx31f5pP1RCzgKWgWg0EkaJkiY2m54oEqlXwB3kM8Llueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=OpQMhnyR7CzdgLnmFHW_-elkNSJSH6hqdghwKdg1hlY28-Bl8HvPbacpzLUioRVkPmTc9alK-bsAd1EoOW0y2c-qLtzEJvS2mfAeWCWLAT4v2sa38cW_n19GhUIS82dnmEyWZvyG0x5mF4Zp89Hs9-R-3gL0LdUTpV5Xfwo8r25RrPlHEyDPoc9n4ZIpJSA7dm7Z5D4AibIruJh6f07WhOIOhow_vJamt_o0DPajo4H0JEbr8gwzOxDDMmMuin9wvkIk4sPP72U1p0s9W4v14Rtn05oidduFKHj8fOmTwx31f5pP1RCzgKWgWg0EkaJkiY2m54oEqlXwB3kM8Llueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RAKAPDho0Vgw3pYhaEIxZ7WPUC0oL_xmCtKcM7wR2hYUHUCXdJdm2bnMYmE8GMqqBSYHLyx5jSWonXLeueaqAPJpxhh0T4FTkf3BeHKfOyqHop2ge50OGuBXQMODEsubdMKN8eH8Wol3bX_aapgL5Dgiz9VtNwPeraERxZqr0q_kom38_2lE5T5eASZX-kvuMRZMua7kSk8wHbr5peSMdGlaU1t_KJZrqwwHH84GJ0gCcWOtVgSRPoj0f9YUeeReMxaee3foB---PV4y3bU0QfPtlWHGBiAHUiD6UqjqVviJUXX_c4Rz4is5EiFh7WBTHs8NhFOmo4IX16rsJF2pBKd0rFs_W2BVDoQ6_WPg7iCzZ58DwiHTePW6Yx-jjXemuB3W21MnG3Zg0UD55f_9nnEshYbo8XmXlCUQRbaTQj0EQV9dIkuy_cAgXXIDbWMNXEVt0xo0lTp9o7SvP09KKdNn2-PQxrsd6iOtMYr0YuvfLBFJ4-8lv8TIDaAzf7buS390A3stoLGd5bFxXs-Xbm-m7H_6hhvkiZ4PaWyBsfACA-fcF-C7yf7jC-v9_o0cR0hKFdcupFe2T4Ya5MYPn1YgJFdEl5KN1kQPzwlxLETPIebfJj6wnT8vWYLW5JIj-Xa0Hskr0izFUWpRs4Imi48Da_5JUt5Vb001jyrhmro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RAKAPDho0Vgw3pYhaEIxZ7WPUC0oL_xmCtKcM7wR2hYUHUCXdJdm2bnMYmE8GMqqBSYHLyx5jSWonXLeueaqAPJpxhh0T4FTkf3BeHKfOyqHop2ge50OGuBXQMODEsubdMKN8eH8Wol3bX_aapgL5Dgiz9VtNwPeraERxZqr0q_kom38_2lE5T5eASZX-kvuMRZMua7kSk8wHbr5peSMdGlaU1t_KJZrqwwHH84GJ0gCcWOtVgSRPoj0f9YUeeReMxaee3foB---PV4y3bU0QfPtlWHGBiAHUiD6UqjqVviJUXX_c4Rz4is5EiFh7WBTHs8NhFOmo4IX16rsJF2pBKd0rFs_W2BVDoQ6_WPg7iCzZ58DwiHTePW6Yx-jjXemuB3W21MnG3Zg0UD55f_9nnEshYbo8XmXlCUQRbaTQj0EQV9dIkuy_cAgXXIDbWMNXEVt0xo0lTp9o7SvP09KKdNn2-PQxrsd6iOtMYr0YuvfLBFJ4-8lv8TIDaAzf7buS390A3stoLGd5bFxXs-Xbm-m7H_6hhvkiZ4PaWyBsfACA-fcF-C7yf7jC-v9_o0cR0hKFdcupFe2T4Ya5MYPn1YgJFdEl5KN1kQPzwlxLETPIebfJj6wnT8vWYLW5JIj-Xa0Hskr0izFUWpRs4Imi48Da_5JUt5Vb001jyrhmro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th1mvu_8C5n-z2LcSH4b7-HkdJvCR9jgXw6upjh8MRjJYGv9EMiAE3JgjzshaLLT04--Os7wrusqPgZnK62iZEwsIsdMbVoxACxasQn-2M2PvilPpmmU6IpZljw7uxZpKu1_Dr6R1X_9RHr0-SknjrOcmJw1Yf3TwVKm1mWwhbBxclFM5bh7pPyO-6XQWTINkNSPcPpm4Hfv3zHfvrx-IGTJ6K4HoMJ1nJzbmdGsHshyMX1S323bDq-jcUil_bUdrca01nYh5XgMBqzHzeyAKnH5FfgXKUbWECgYVuGXg8FtrmMjlsO7bVCWpbVvtDfMiYMnmkPQHA_uHbGKL0KnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm951FdEMoHSS90jKxjTIDKkpYursSQqB-GqNVP9X3XRU9uDHoeYJ90BGsAqSOyIuxNSmymmHHhqwbKJnP8J4qYb8v3Jccm5vgjdw_zA0h05kf4JG5BNL3YkVSV0ELdYkrOG4UH_Mnqu-WZq0Dgic2-Zxt0dlnMXRZl90Od6PTnZfPHmHihj_ICK4-JDNT9OYeTn8Mi4MIMJTl8TsTXPwl8PKY8P4ZTre-3yeIsge1VH1YLTRfbphyQoAepJxIm0ihvjdMi3ZbbZ1WfXCrqpd8C-sqMr4dyu3D0RBJe_4j2zYxn-OpOR9kx1GeLZKBo5faC-PHuaqUcwfoAe80Y_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc5Sn6__n5xGc5ExcO5JUd5FKayNKZ8dyp801I1nFdnvo9uFfC28kTYn_9ir-A1-HUkkK-0PJui7g8etcuuYJZqCBU96LZu3eFIDgCzLZtfWceuJyI6rYv5Xae0G76h8ifuTgCrXmW7hkv-2NVq5unP-1wyZ5PzBbLTHlRieAsMFD9DWerNcJqg4eMsS8YRPycFmJOScMzOo2-4ooZMSlihYv2VYVHrQ8p2DQ7p8DyDpyyOfpwQ4jpJs4o2XRwZrin4Roi-kx5rtu8RXP2EakwNO3M19iQwIo5iflovMOh7mZZducFZzgHy_R6_BwR7utkmSXhLwkWZGKRv-aOLMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=qtlnbSa2xB2uW8U579x_20MwZf9P85Ck0C5zigGKbTdC7E3sIzVqe97yuwxNM8-iitdlcllWrLPT6xkWMTbywUUESKsKagnBE4GV8KFpFr1KaHzq9rS3cxr0NhqU4hq9K1bd8qQMCAulKv5LLXMZrTjIEngZgC8IU5eUQqcllwYZ654wFhnoIVGp9w3XuQN4gx9hNRjy1BO77qGeUzZRw1Sfje95vaWQyuQ_IZv31IEBHz0TK4yqG5hlVnR7AiJnBthFKSXmuke0EVkuvwUGs_xz1Ww1BPTxbb9mSr4ajQkoiIQOIUy5BiVxlqEczm0Iu-W0cpHiiUg9xgFVt0deHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=qtlnbSa2xB2uW8U579x_20MwZf9P85Ck0C5zigGKbTdC7E3sIzVqe97yuwxNM8-iitdlcllWrLPT6xkWMTbywUUESKsKagnBE4GV8KFpFr1KaHzq9rS3cxr0NhqU4hq9K1bd8qQMCAulKv5LLXMZrTjIEngZgC8IU5eUQqcllwYZ654wFhnoIVGp9w3XuQN4gx9hNRjy1BO77qGeUzZRw1Sfje95vaWQyuQ_IZv31IEBHz0TK4yqG5hlVnR7AiJnBthFKSXmuke0EVkuvwUGs_xz1Ww1BPTxbb9mSr4ajQkoiIQOIUy5BiVxlqEczm0Iu-W0cpHiiUg9xgFVt0deHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZToeHTeDZnvrF7UGic_IWwtDqIHPE_7IauK9YcrVw6nUB7AeIq_TgQiDbJ_8u8T3FdAya0-n_7w_BXaHqBz_2xHRERauoJ2kKGLmZDNCG95Xq-Cgk9NHmYcMDA3U0QchWMxRzvAa3k0lreyj5wrBeRYaVDtUTuQKv8n9eR1amfEcccCCeHPxk57MS5N-10xIRCTtSSD6wkXcli1v4czLwMo3AonWT_OmCQkkCrHzFRNsH8m8BijES8P956EbAE_3plxtL6OXP6w1zcDymbbqaFhLnlObXNFkjpFMfNJ7tlNI8CcDhiL6nXTdQa4RxSUEMi9CggXHymbfKl4hlrVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVxmT1D0qSyFfPHC1vmyTAmaWPhgCjs6UXwbEF9P6MjTTvi-wiRSEKNeHOb86G_cNqg4ow95C1PDXzjXN2HNY2-oGO4gy2_xDOtM6hi4BLTWF67dJ9tWDnZsEfiPnk6Uioz-O78OCVpHaSn5EYASUVn02wUQvlo40Mpg5oygltEZU6OwjFZJPlLhFUPXckjfWlPyClc6agR47UEGl1_tVv1IrIiFF_ea3ejzu1zjfOrJV1jAREvQubIKnTvWANbdsrLSCHQnTNw8X9WuKKq8kA1weGvgwsDiWVfZMo1nudFBY8g2mbfkJSYRyCSAKFh18N1VrFThYq11fqLoZE5nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOoqwChsSQeWDCcIRvKFdmorT18mgKyvSWY8kDPqg6IMS6u_MgkJV7Hd_v8Q9nlcj0OCttaId5c5mI2ej-wDciHj5a-VMhb7zRJOJpXE0IepA0u-7CQ2o64lH4NmeLZ5KnM7SIM1k-wF81NDMz-QAmrwElqcusZS9BWFfDTx1pjSe4ls0m6PWG3WqiV312fXqU0i7n6zJaCGA3DMlu8uEAYNb8Y2ApbZeyzCWrnNms7MR5nHM6UiwLmiP4Bto52kyNPBoUJ0qYQvP76UxZJp-8NDuuXEbXJNqhBZdOk9C2_vuCQGi3IikZsnKJWjVjVILwssp-ppjljQQjIJMXcsZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnrM5t3s3gwpaZnPYtNHHS0UzZeyc9uc_Ck8Kb5oSf-tqdRpTjTGuKnxV2k20_Lv-tsNrt0grENF9XU8wXXelcbZ4zGBVMoiLjZY5f8hPmVt0zkqjOGKmfw5fpDZVY3FcjbUbIUZZ53Yl1JlQz5kvabD-n0KTQPrw4GsIu54i9CjOLsLfeeaXkRJV6_pyjkSxox49MVEm0Le4J00x2gGyxmo9z3WyDSZXvgDrj651-qrnaPqe2CC_10byJ53ZdwseoAeqvb9_U7UxHDHX15733T2UszPXPlXcSb852pUTA_SJqnENDE35HhDEWOLAo2mYFtGfEiGUGMs1YIN_3tsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=n1tWKCGiU7RewMroTCEity9G0rLFLURWDwI7dDom-nkjKjblZ_fN6sg6mw04RVlstATBmuSqky07YC7SWxw2Sb0vrsUOlvsAyqKUHvuzBS-ubboRvcjPngZsT6Nztz8GXV9nysaTZXodZXx4vm3OH6thkMu0N-4W1qy2_YlZnf-6r1VTzgGOwS-6B_4TIY4rXq-VqxZKy7_wIeztom9K09iILvRUaJy__xMlLCo5J37cllt9CKod5fuVvTRONCkn3xIzT8trvfHbfa7ZtUgv2Poy6gI0ha855_cKaZyrfYfBBBboVxELs5jjWbRzNAyFjmK_vBzk0IoH6bH3q-KlUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=n1tWKCGiU7RewMroTCEity9G0rLFLURWDwI7dDom-nkjKjblZ_fN6sg6mw04RVlstATBmuSqky07YC7SWxw2Sb0vrsUOlvsAyqKUHvuzBS-ubboRvcjPngZsT6Nztz8GXV9nysaTZXodZXx4vm3OH6thkMu0N-4W1qy2_YlZnf-6r1VTzgGOwS-6B_4TIY4rXq-VqxZKy7_wIeztom9K09iILvRUaJy__xMlLCo5J37cllt9CKod5fuVvTRONCkn3xIzT8trvfHbfa7ZtUgv2Poy6gI0ha855_cKaZyrfYfBBBboVxELs5jjWbRzNAyFjmK_vBzk0IoH6bH3q-KlUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=m13nyeXXRNBVPQy8tQtQBeL3k6LBIrPXzm6YzSj9ZqA3f2D1JPxmeoUZNlIV61kZSm1cAYagizQGoGDkb-hEuxFxea0g6HaII_NWKvbGsSJOX4LcCmyP1_E6ElYne6o_hXN_wt2izLWAAR8_iXGhHsxggiHikMuhQdbMdkwmUvVRI68WGEos-d-PIeR8tatWXx2q__wA4rJ0wnE0MoA8kbJoKxLCtXrbtGYSaEuEI76Js6v-DWq-2oDedHuPwSVuXN2S33ptIrKXG4DxbdOyULGFFdHwrm83oZwZT71Fyh9LVREopV5KGrqLoN23SNy617fmn3h-inMP3A-jXgcreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=m13nyeXXRNBVPQy8tQtQBeL3k6LBIrPXzm6YzSj9ZqA3f2D1JPxmeoUZNlIV61kZSm1cAYagizQGoGDkb-hEuxFxea0g6HaII_NWKvbGsSJOX4LcCmyP1_E6ElYne6o_hXN_wt2izLWAAR8_iXGhHsxggiHikMuhQdbMdkwmUvVRI68WGEos-d-PIeR8tatWXx2q__wA4rJ0wnE0MoA8kbJoKxLCtXrbtGYSaEuEI76Js6v-DWq-2oDedHuPwSVuXN2S33ptIrKXG4DxbdOyULGFFdHwrm83oZwZT71Fyh9LVREopV5KGrqLoN23SNy617fmn3h-inMP3A-jXgcreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ShPb2BmFvqpUlGB9oyQYij5Fhh0EX7KzWj9uCwpLefSz-hmdd1iPWFB0YaxkF7ZIFhIzdZ9j_C2hTkjfE3RC63ssWESSIwx6jOJwJUditMqPCl__-sfVFJHcff2XMoVWR0wZe998bBsqaOYuo3py_gt3t-wrTLEXAHlBUE87jPpAhfRnykTIlYwnhuSCxiyJg7F2D8ASrPe2sm93bIs3x6bqRpP9ye9uoOKT7KpE6GZGlGVEPIkfVfQuqkSe-e6uY3pe-aQV-QAngpnS_GJUVm05YeZauRe3xga0Sc9ZzWDo4OmA5u_JKvEp_j4uWgTqd4Pf1GQHeMeVdb8Yfz1Amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ShPb2BmFvqpUlGB9oyQYij5Fhh0EX7KzWj9uCwpLefSz-hmdd1iPWFB0YaxkF7ZIFhIzdZ9j_C2hTkjfE3RC63ssWESSIwx6jOJwJUditMqPCl__-sfVFJHcff2XMoVWR0wZe998bBsqaOYuo3py_gt3t-wrTLEXAHlBUE87jPpAhfRnykTIlYwnhuSCxiyJg7F2D8ASrPe2sm93bIs3x6bqRpP9ye9uoOKT7KpE6GZGlGVEPIkfVfQuqkSe-e6uY3pe-aQV-QAngpnS_GJUVm05YeZauRe3xga0Sc9ZzWDo4OmA5u_JKvEp_j4uWgTqd4Pf1GQHeMeVdb8Yfz1Amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW6ORZzLS3fX_NvaF-lRSKUXCTmqHHdK5EAlEZuG_R3xPja9PTsf8JSLSXL5E6TErbrSX3t7aHgQLYCJpRjVJWrJ2pGSdm8CECZ1jHtZxXeb--QHZNxyS8C_XuimH-E-8-FgZ1SAeO2LEAVHr7uKj3d_KKW6wPkHm1nOlslec9zDUGq1XC4Z1QH4pkLCQDnDAxS2ErpsBw5dJJsH4ua3w5Sp1DtCdKkSq0LWupU_g2TI1zOcTFK340f9-2YQ66_baiXTtoxc3OlnCSz-8sBhfhyjILglgliGoGPOCw6vanzCDLE5z3N1_Y5mqwyfr3Ch70FXwUcDeFej_1xydTyrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QzZnvapOF2LtFPtI-_-1RAzMO4UB_2BV3TirEp6c_Zez3Eag3Pmzk9fIoDGh0tyFwcz6N4HFzI7Tvhvy8EakwkjvD0I4M6-UNexdoyBsB6bDlPbidkREgQ-yK5eCt3M5ydHzfvCSglusbOS4rbB1Zo_Ec8Mu4BnmrUpGa_K8vTox-6lvAbl8IyvvjwVc17_9oVcyBSuJpSKm4vygGYFypG4NQkMPCjFi1hx1MRX8w8_aot778QiHLh44iv-N_tB4JldQErG6NvWYWak7vS-a-uKA_kETn3qACjrHDf5HNen2Pk5XApj0kjqodgtNGuyEXavelUNCusf0Lc5nu_oKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=QzZnvapOF2LtFPtI-_-1RAzMO4UB_2BV3TirEp6c_Zez3Eag3Pmzk9fIoDGh0tyFwcz6N4HFzI7Tvhvy8EakwkjvD0I4M6-UNexdoyBsB6bDlPbidkREgQ-yK5eCt3M5ydHzfvCSglusbOS4rbB1Zo_Ec8Mu4BnmrUpGa_K8vTox-6lvAbl8IyvvjwVc17_9oVcyBSuJpSKm4vygGYFypG4NQkMPCjFi1hx1MRX8w8_aot778QiHLh44iv-N_tB4JldQErG6NvWYWak7vS-a-uKA_kETn3qACjrHDf5HNen2Pk5XApj0kjqodgtNGuyEXavelUNCusf0Lc5nu_oKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=oG2JitHGlemGXNv0iXeyr8xBIa0aTdOxdE3iLO8UmWELR6w8FddRFKycyoScE7OPD0xaim2b3gpJFlIX0D16p1zjM2pfI3YMtaJhDlysi6Jt2zZVn3frHCcy16e9qBf6GGBfc1Wyzx8H7cxt8Qkas-1WImBhxu3eaBOgSawStHS-kIUVE6jvu2j3i9CUDkbkofCkNWDeXMUu5A9-3bcXQtXCaJY-Q5UZvAjS-q4LY-QcmmlCJyBsXTQPFybC23Chl2dus4cj09gD1PnpOHRZ9MX75GrZLXvuTTeiWf7AmGuUHJTWsxpbeN7i_j9TUGjlYvSJp_ZmCBm64t7aXgfl1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=oG2JitHGlemGXNv0iXeyr8xBIa0aTdOxdE3iLO8UmWELR6w8FddRFKycyoScE7OPD0xaim2b3gpJFlIX0D16p1zjM2pfI3YMtaJhDlysi6Jt2zZVn3frHCcy16e9qBf6GGBfc1Wyzx8H7cxt8Qkas-1WImBhxu3eaBOgSawStHS-kIUVE6jvu2j3i9CUDkbkofCkNWDeXMUu5A9-3bcXQtXCaJY-Q5UZvAjS-q4LY-QcmmlCJyBsXTQPFybC23Chl2dus4cj09gD1PnpOHRZ9MX75GrZLXvuTTeiWf7AmGuUHJTWsxpbeN7i_j9TUGjlYvSJp_ZmCBm64t7aXgfl1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=fEuoW0mOIN90vI-QIY48bqe3j34Cs1ytSV-n7Ubtorvvse2bcP8eV73kA-THrAtXy7F0DTitQnwwg_r2f6FaXUaHnEW7HqEtHnbeJehQJevYeNjj8jtFHkrO_iWj2uNQOJVJCKCRgw8XpWF4J2kPc2ukKTfzKTB6Ietw2_TJQCsWJ6AVaw-EVwgOEpyI65YM81FK90FhVlqhwj0m9y40bEZutnB0mnue6Um7bI3aSXajg9PHUmv01VM-uJxhmtveB4l5HIyZf1JgG64QPRpmQd0CosgVY5CWsrXZ12-TgGG3ak2kubbMc_xHqGNYyZzDZ7QC_e1iYFgIcu4sker_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=fEuoW0mOIN90vI-QIY48bqe3j34Cs1ytSV-n7Ubtorvvse2bcP8eV73kA-THrAtXy7F0DTitQnwwg_r2f6FaXUaHnEW7HqEtHnbeJehQJevYeNjj8jtFHkrO_iWj2uNQOJVJCKCRgw8XpWF4J2kPc2ukKTfzKTB6Ietw2_TJQCsWJ6AVaw-EVwgOEpyI65YM81FK90FhVlqhwj0m9y40bEZutnB0mnue6Um7bI3aSXajg9PHUmv01VM-uJxhmtveB4l5HIyZf1JgG64QPRpmQd0CosgVY5CWsrXZ12-TgGG3ak2kubbMc_xHqGNYyZzDZ7QC_e1iYFgIcu4sker_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Xd4iX-6iHaZAJfp0qvpo5gfHTsDFKys53Fet6aqSg1pB4RdsEJIuO1sDAXosfk2cH7R3Bpgx2KnGwdNkAaimiBFdR05TqmAQdcBCycBkqHoX-J6ZKjpJbXFZXxxaekyfnJ5OvMxfhIOUHZDngZjsf2A1Py3YJ_7YLx6HzHqehWOspNSdPs7VEz7lhbfMwG7S0hKUZKV2U3ncWNcIlL9WwkCI7iY9sStmXaTYhTZtMYzcruLiFcX6eU2tfxtPudsFefdfJMJ_v6sOTZ4a3ePvlXBZQ35Ma2pZIgaTNuNEH8aniLZOkya8O-uzXzJevS8mDaajLJz8kQ1M0dKeRiEFywKppONL33kCv7icN5-CMiJeAa5g0k16B5z1pwJ-JJGY3t98E7BqnAzIuu9lkEHhnSpiINnZ-4DwJzL2VnpB7Ov73aa-Qz84WgpwtQnZyvGc0H8p_DBsurlcPHtNEs7MRFIro_j8hu5M-EWj3gYPybXLjQKvAE9f8edy92YhsXM_XkfXJEVpcjRvZ2LniQTYG5kqCiAuDAw3jVxZUBfcFlD8Ptrz4RMz_bd97ECdIEJ79bahjNcQvI2ybvPxaY24XEU0NA7u-47zBoggBsjIBMcIFOSLe4GnavbZTUM311cH_BtgddPkr_ZsBgZ4oJVe8Qj2B7pD_nUy6u6fX3l7nTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Xd4iX-6iHaZAJfp0qvpo5gfHTsDFKys53Fet6aqSg1pB4RdsEJIuO1sDAXosfk2cH7R3Bpgx2KnGwdNkAaimiBFdR05TqmAQdcBCycBkqHoX-J6ZKjpJbXFZXxxaekyfnJ5OvMxfhIOUHZDngZjsf2A1Py3YJ_7YLx6HzHqehWOspNSdPs7VEz7lhbfMwG7S0hKUZKV2U3ncWNcIlL9WwkCI7iY9sStmXaTYhTZtMYzcruLiFcX6eU2tfxtPudsFefdfJMJ_v6sOTZ4a3ePvlXBZQ35Ma2pZIgaTNuNEH8aniLZOkya8O-uzXzJevS8mDaajLJz8kQ1M0dKeRiEFywKppONL33kCv7icN5-CMiJeAa5g0k16B5z1pwJ-JJGY3t98E7BqnAzIuu9lkEHhnSpiINnZ-4DwJzL2VnpB7Ov73aa-Qz84WgpwtQnZyvGc0H8p_DBsurlcPHtNEs7MRFIro_j8hu5M-EWj3gYPybXLjQKvAE9f8edy92YhsXM_XkfXJEVpcjRvZ2LniQTYG5kqCiAuDAw3jVxZUBfcFlD8Ptrz4RMz_bd97ECdIEJ79bahjNcQvI2ybvPxaY24XEU0NA7u-47zBoggBsjIBMcIFOSLe4GnavbZTUM311cH_BtgddPkr_ZsBgZ4oJVe8Qj2B7pD_nUy6u6fX3l7nTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=YZQy7LwZAuNchXEEpIwK__g23Lk-y9o5aYMOnsaA9GNjcSXuiyAPz_SkFcsKPJYCauKcEfO_0igJVd6Nlfa2XH882qJ7Kqh1Mg0uCcHuyfPDIpHbjAESB80iqskB7g8EdczRKGqFZnqySIj6e1UUGWjX1y2oWpRRDQe3HtMvZqwEXPknBM7eFbvh1o_cCSX9d31ELmQOk9czprNwuSfHWv8dc4IAsVS1l033XJowFRXlDGGBebQ2uynO7yQWWkHcYFOm_yG3Gkot0iKTGWdNl6FNBkU53LzPz0c6NJGqYSo5t6TOx8PjLA1i5X7h3TE9PzqYgQZWfuKNEW6zku9hew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=YZQy7LwZAuNchXEEpIwK__g23Lk-y9o5aYMOnsaA9GNjcSXuiyAPz_SkFcsKPJYCauKcEfO_0igJVd6Nlfa2XH882qJ7Kqh1Mg0uCcHuyfPDIpHbjAESB80iqskB7g8EdczRKGqFZnqySIj6e1UUGWjX1y2oWpRRDQe3HtMvZqwEXPknBM7eFbvh1o_cCSX9d31ELmQOk9czprNwuSfHWv8dc4IAsVS1l033XJowFRXlDGGBebQ2uynO7yQWWkHcYFOm_yG3Gkot0iKTGWdNl6FNBkU53LzPz0c6NJGqYSo5t6TOx8PjLA1i5X7h3TE9PzqYgQZWfuKNEW6zku9hew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MAU9Ba-KcDEy5fQw_5xFLbkJxOQn1v1Z2S1WpRviDeQ3DNjZ7fL9uV0D7iyZm8LpoS0zHKgR7bcYHSxYe_cAgl800Ex1sJDnRv29u69toFe4fzNyC4QS02CWzQ3SB8whGTQWgPHggOx1ClDxG46C2SNpAPLpCjp3PM-nwhtD7yQG1xrcuNSBn2JqPXKgCbD0HZl7X5XWUzK9E8Y9Q7RvJAxINpemOzT6MOgqDdtQpCF3OhzSlEpl_p99m8S9BbdEeDcIg8rIpN8sSFdQpmsgNhVy49oNwzrAibmay_DA1OUW8VLdb9qmHVR6_2M9lnhM0N-0TtpNzUIIS7ZTByU16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MAU9Ba-KcDEy5fQw_5xFLbkJxOQn1v1Z2S1WpRviDeQ3DNjZ7fL9uV0D7iyZm8LpoS0zHKgR7bcYHSxYe_cAgl800Ex1sJDnRv29u69toFe4fzNyC4QS02CWzQ3SB8whGTQWgPHggOx1ClDxG46C2SNpAPLpCjp3PM-nwhtD7yQG1xrcuNSBn2JqPXKgCbD0HZl7X5XWUzK9E8Y9Q7RvJAxINpemOzT6MOgqDdtQpCF3OhzSlEpl_p99m8S9BbdEeDcIg8rIpN8sSFdQpmsgNhVy49oNwzrAibmay_DA1OUW8VLdb9qmHVR6_2M9lnhM0N-0TtpNzUIIS7ZTByU16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoP-tPwhnhX6TsLYCfzWtE0kbS-GWGFYMOP9HnziHzTAp2Sl-seeRNOljfgscrNKsd8AStfinE77VarKwyuYG6FUadwZQvrFxldMDnuSpB0mCpJwdGuBqDptlAhDk2dyS4sgtQxCW1vOOoQ-BR7u3JjjiDsivbVyIQVAQrgBHhe8RPujkvxynD29JsTIiz5ehFO3VIaXmONiEmHoi4JSvTJYheQsNwaSceejsI1YVrIyH3l2k93XCvUR9dUdZICJkpd4fWRuXYBNb2siJuXsoG79G5JQ4QVi2N7wC4CAbjgDl8KUtnPpNCCfH21pmIGJzaMSBtErDxaVxkmgFm_GDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai8nN9on8M8rPKphirR9Bi9Slffy0dOIFINN6iEgQ_VhW133TWI_b-iPGgXetnYUoGOkFCpWz4HJY-Z27bf0HBXW0_ea7oSz69csZokWOobYSrUIRHmbaYlmeooIBjkLrKucxkyPtzN8txT-iF4DHx0vew63jnbrgMFoQtR4t-EfNzGUNC96DFAjFZL1zhX06feBVeSGo97MtLNMOn_-EqRRKbVd3dauuBzTNEWFqLf7h51Hrp9ePHpJIkxvcrB4CZAOc991boDqgsWQI3oJ6eFwm90ET56LsYOab6U3yZ09e075XdeC3y7NSawJyAxYr6UrcSirDG6WeiM5AT064Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=okagI0OEInUI895wBYK4pH4-H_QqstZtov3Yf1jp18bFna1wa2wVet7nNCQ2bX6oTT1yu595ldZYjeHnC_I-6Fut5PElxGlWH6c64w8lngW7JMbVE7bjWDIUyvi1s1neGeuLlcabUy9oJ_s3RGrIRLK433MTDI4j4kZarulGoTt8rUEzGDTAAJctZzCDGzss6qVysabsXBovUL4wTH6PJI_9-57oAtd6RL5DgkAvhZauZFaxOdwV5txaJfmpb7jUqJEUBHJxLATkz3zq-mOqksw3f58gYUMOwgwcK55Tnpm2itic4tG2Ism1Nc_wLiQpMnJBfRycJBX-0eiwMR88lKlqmW_WLQprsOHGgvdoewAXVWgf0-Mt5s5wyMpAPa8bvkTr2Wx212QRKny8wkHpNf9GvRq6wXqVDaeQ7I8aTMU1BVLZa5CDkGWYWatE4w5i8c2yMZBNM4QO40pM3T-nO3McpxC0oijDCNlNR6rFr17x5BsG0bB9rF3kc2eaalB12nSFehkMLDuHmNbMV_VA05bkmIAnaQmpjKibpOTnDQgjUnHsrRJ_ThqjNflP1sGAiiRelPdV2QIbIW_2IAw9vXke4LkK03lWD_3Tu1c5s4hY-mKZDGEGDWzT23QjziDgsPganO-7JHy8kQJ5MAeOwt7aymevDgIQSVkoo4k7wls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=okagI0OEInUI895wBYK4pH4-H_QqstZtov3Yf1jp18bFna1wa2wVet7nNCQ2bX6oTT1yu595ldZYjeHnC_I-6Fut5PElxGlWH6c64w8lngW7JMbVE7bjWDIUyvi1s1neGeuLlcabUy9oJ_s3RGrIRLK433MTDI4j4kZarulGoTt8rUEzGDTAAJctZzCDGzss6qVysabsXBovUL4wTH6PJI_9-57oAtd6RL5DgkAvhZauZFaxOdwV5txaJfmpb7jUqJEUBHJxLATkz3zq-mOqksw3f58gYUMOwgwcK55Tnpm2itic4tG2Ism1Nc_wLiQpMnJBfRycJBX-0eiwMR88lKlqmW_WLQprsOHGgvdoewAXVWgf0-Mt5s5wyMpAPa8bvkTr2Wx212QRKny8wkHpNf9GvRq6wXqVDaeQ7I8aTMU1BVLZa5CDkGWYWatE4w5i8c2yMZBNM4QO40pM3T-nO3McpxC0oijDCNlNR6rFr17x5BsG0bB9rF3kc2eaalB12nSFehkMLDuHmNbMV_VA05bkmIAnaQmpjKibpOTnDQgjUnHsrRJ_ThqjNflP1sGAiiRelPdV2QIbIW_2IAw9vXke4LkK03lWD_3Tu1c5s4hY-mKZDGEGDWzT23QjziDgsPganO-7JHy8kQJ5MAeOwt7aymevDgIQSVkoo4k7wls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKsrKSY1m-4fZtHKAmdji-hwnK440wEsTWzrH4PKGOpdIoJHC7Uc7sFF-YeKLrSFGcLziCBQ4C-_js8hAURRqBH4W5Hi-8Mqn-LZhBZDpqU1MfB6wl7jAUTgHsNCbnSyZwDVgCWhPEzfk5iFc4rHM4ZKxxAe4IXgf67fnRXtsWEB8VaTFQdviSi4O45LkyqknY9SNWMRVvSn1VcgWz3zckoJkJDI6HknnZrEEqhmqUqgwE3QZZfOmE4gNCpAu0TKjdrXRZYjXSqtbWuVHoI_3DJ8I6YOpo46LEPbL0P2PlFKJfEt8QBvDt2sjP31mBt3O7jJI8Nyy6V0Th1KGAxGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSp1I1oz2pQ1CZZslFazNoVzS11Jj1L8pfccC7JZfE4aTT1Qu8xUw4plmxrklfyXPOHmM_C-hwo3ltzrNTSiZqCuhxSanYNT5LovcQd5gVO1VLokjFWxo2KLekrPZNqTsGk2hZAeKau4KghKj4C_qzkqYeirOmXM40WQBNS9M-AlQjhPuyB3KNUYl61PcFUbrEoOf_D7kb7R77oT1uDBw6rK4UrpWd6PbktGnlJfLlLigvTgGW_FzGeawGyDo974sBOk-0h85sjT20U37U-V6zyaHrIwRVtSIC30klKtCcMOlFEwNc3wFu9FIaJMoiH0DlcUGl_rdpn1lNQxEtQYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkFA-oFS9REZ4KBqCWnYmCQSCBIzFklDVO20zsNGE_d4MKDoTvZPU5tV3fD6dSgwXIDzoxIHeFtzYvDoV4hZwSwrBQ9j_fLbwVcgu8SXoGP1x0_TTwMPoSIOU2jPu_v0P6lcUEgjgjGAt0iaMPV6PJJpLUJeYW5HTOIyP7IN6qZ8jmd7SguHWOTuzcTeJLREylMni7JMwbk6Jzoc4XOcDLANxMDr0NZJjSbl0s0U9x7JxgKdxIkHczaftL6JiJgrmMWTqf8M0SjqiZRwVKrO3EDcwfwsztqCdZDDiKqGX6PkykjFIDDImBDsL5BcCbI8HCseOB92k3qCdG0Y4I7E1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ior2cFfWlUEnbtan5U-A3cbJqlxrimADdCFkXrbhKQc8KAbvxUQ7VmSaZ4GqZvJU4TVzKroK9vROtnAxbLrZYy1FpBepz7PaV44djTAtC5Exgc2VApQz9rE3MeUimY3KpYGee_Jz1Xe-yQHZnAn2XMckbXfupRup1vRCcYXGmVB2KtsSvWhMeKrvokcx5ejVZAPwtAv8PnpvPuWt786CVfXGpKZKeKchMKI0L08JtTUBR1qMBb0_3nwRQxjW6r2Q8Z4blxlzQcRYmfSHukNLR-x52HknpBmJc4QwGp7GWwVzV2kjDPW0eWh7Q0cth4x93dlWK-uk1ZysX-nYJwOKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=SvPkunhoJ1UJYfj5U1FjkaNLG8EptxWXSh_TEamax8b8BRif5WySnzyFqWljy8Z7v4kWFJdsLF7Iadol6RJrzifiTIDe6t0h_sD7xil0pDGZyAVx1WXvq8bEXDZQ1xaltWZWUM_YR9z2uG0tH0R1hBVx5fIfTA2ixlb3y0olb7S6VJQNTzODkS34dmQOCTyU6oO-1U3Jv2MWJI-vqS5wRpybiJ2W4EJcv_tVLhVOXofSWrf8uMZWOj-hvx3okT3LvFnvPh17xHkdZV4CevhpnDDTKdfoPmDoU6YxkU4lr8ZyResO7r-MqxquIRngxalVoaT5kiAuwQn-OzpCT3T88Cxm2uTdvyXs9Y9UjNzRMnfBQYmx2oACJzf898OBhYwSXhYEnMqxp44Kij4gr1kA7DQzrWbJuM-LQ4iZWGflvtLpBgjrJpZG6hQBQuvjgPYMMsmNvJGByjDiVi-S_GT3goLWxglvx64LBysg3JFpYhjYTQYQY0-VH4sjjRBuNqPOFZlxPX1azE-WOORXlucIM_JnzSg07E0LIKkEcr6FOBnQFf-vQ1q8popJ4IXD4BKnB9WC3QEoUXWo-h093zL1oNU-EE85xEqOO2UgiJsF2nicGgNbZmWai9j4q93KF6vnDK-Ne9ZWTQieDy4hjnvAtqjNraRzZ2mEbr8BN72tZO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=SvPkunhoJ1UJYfj5U1FjkaNLG8EptxWXSh_TEamax8b8BRif5WySnzyFqWljy8Z7v4kWFJdsLF7Iadol6RJrzifiTIDe6t0h_sD7xil0pDGZyAVx1WXvq8bEXDZQ1xaltWZWUM_YR9z2uG0tH0R1hBVx5fIfTA2ixlb3y0olb7S6VJQNTzODkS34dmQOCTyU6oO-1U3Jv2MWJI-vqS5wRpybiJ2W4EJcv_tVLhVOXofSWrf8uMZWOj-hvx3okT3LvFnvPh17xHkdZV4CevhpnDDTKdfoPmDoU6YxkU4lr8ZyResO7r-MqxquIRngxalVoaT5kiAuwQn-OzpCT3T88Cxm2uTdvyXs9Y9UjNzRMnfBQYmx2oACJzf898OBhYwSXhYEnMqxp44Kij4gr1kA7DQzrWbJuM-LQ4iZWGflvtLpBgjrJpZG6hQBQuvjgPYMMsmNvJGByjDiVi-S_GT3goLWxglvx64LBysg3JFpYhjYTQYQY0-VH4sjjRBuNqPOFZlxPX1azE-WOORXlucIM_JnzSg07E0LIKkEcr6FOBnQFf-vQ1q8popJ4IXD4BKnB9WC3QEoUXWo-h093zL1oNU-EE85xEqOO2UgiJsF2nicGgNbZmWai9j4q93KF6vnDK-Ne9ZWTQieDy4hjnvAtqjNraRzZ2mEbr8BN72tZO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
