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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 08:43:33</div>
<hr>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=X_ZO9bb6Y-QeRFRaBte_vumpN2agvo9YEGs10kO2duRGOkn-RwKHfRxCaQFAi4lADcGK4Zws9ARr4QfQ0OOHWM-QrZERZwvkS32fCmnZm4OvagX_aOs49Mx3xa5H3gyRux_yf7SZgy9CYW3JWEwgAsxc8vh56qvX_1fTrL1gpTtgp4R2F9IkMG-vMzSmTQvK4pw03ITdr_MklShGKqn6VCKmzXTpabzoeWRLlmgUPyI3Ybq9uPwsyjBORa4vQ4QBaBAqC7p2GX0RKGi50UZjgJ0-FKXz5qTbcGUwa_98S5XdmBDAX9PGw-q9YbXXpXUqqMiIJWds37vLh0xArz9eajU66FywxZmjc-mAtpOE-KfdOjFl0KfVzKpjDMAMPDAWBlgVyuwGDoBQad3DV7BGmn5lbKSZMn1kkEJyyURH4J0b803iVhZ3FkgH5-9MN1V_EjWjzNu1FHdrebXvgh1vJ0c90jk1LmtNmCT5-d6Q15GefVEnVt6XdR6e9gjvCTTzWRSRI2Gmjw4lbPCBr-lIlBsiEWOhOGZISFsWK3WnBMmHblQBjicDhZbfDrDMGDd6mymcEBvsBALYjWrOUorTc1cYGjB2miOI4TJXLSFht5rJ9MC8KjviyGRFDm3SGc5uOO8WNqzXCyL6gjv9j1Y6Sp0VEiypZJ71ksuFdBjY38o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=X_ZO9bb6Y-QeRFRaBte_vumpN2agvo9YEGs10kO2duRGOkn-RwKHfRxCaQFAi4lADcGK4Zws9ARr4QfQ0OOHWM-QrZERZwvkS32fCmnZm4OvagX_aOs49Mx3xa5H3gyRux_yf7SZgy9CYW3JWEwgAsxc8vh56qvX_1fTrL1gpTtgp4R2F9IkMG-vMzSmTQvK4pw03ITdr_MklShGKqn6VCKmzXTpabzoeWRLlmgUPyI3Ybq9uPwsyjBORa4vQ4QBaBAqC7p2GX0RKGi50UZjgJ0-FKXz5qTbcGUwa_98S5XdmBDAX9PGw-q9YbXXpXUqqMiIJWds37vLh0xArz9eajU66FywxZmjc-mAtpOE-KfdOjFl0KfVzKpjDMAMPDAWBlgVyuwGDoBQad3DV7BGmn5lbKSZMn1kkEJyyURH4J0b803iVhZ3FkgH5-9MN1V_EjWjzNu1FHdrebXvgh1vJ0c90jk1LmtNmCT5-d6Q15GefVEnVt6XdR6e9gjvCTTzWRSRI2Gmjw4lbPCBr-lIlBsiEWOhOGZISFsWK3WnBMmHblQBjicDhZbfDrDMGDd6mymcEBvsBALYjWrOUorTc1cYGjB2miOI4TJXLSFht5rJ9MC8KjviyGRFDm3SGc5uOO8WNqzXCyL6gjv9j1Y6Sp0VEiypZJ71ksuFdBjY38o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-M2LMFjxvyfiOsVJHRlzGxSUedjq3dtWN1yKgaI_oZgVo3qrpDiUm4r1SWP2wmTS23npBgKIEdA7dm4y46gZRcZxqLyn5LEt6cTjbSiR830qImoO9Wb_E2W-nyKEFn9GpwluBizUK6WeYmy0oyuTZRdLx92-heqCqK_RwRq_usKeYhd5LMwWQmR8xvIhED7ZSXKFQl3Y-xtmuJN2MHVLVxy4zl31F3YmAVkfSQlA8nJIAUq4kTmbeaFbOmRfKouVGC_KING_DpQWjnwHlSvUBx4LHU484u6NIoWmC4wn32C0m1nxHvzIkqxClFKMITlbN-Nki_u3YmYfqFYsm--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3p8nGVBQZKWfT7-W-7YZkbhfFCftZ_3GX640oH_uNJMbZrKgoMMTL0lb8KexQfTLEd1RjPQKJ5LfAP1mzgrPEytBwMC03Xyg4staI8mi2WfeYFvm6lAFy866KngSRTDRxZ1OvLhHOA8S7RDop3sNu4B4z8WvEz_UBhmVEC_DM9PmI2byqJ9GxhREf_JMxDa5GNXS3-keCTcynFXDVNjbw2ISvE0kenlGVpZ4kkUFz750vodKpi73uUArPB3TOfKHyqhLoMNj6CiTtHNLeJT3uxO97Vjz184w6tf2XbLivCK83Ckr4Hno0uDkefnhwpPCvngykqDnH_gq-sAVHt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NslFIUbLzAd-u3LxjhpKY4PaK6e-vK3Aah1hhnPQjBEkpIuHuNIlJAKr5CI87gRDbCIuRupbie-cKK-LgpbY_yyiwhw4uAcc26-I7vhMtxyu0BpOLfmwbQE2O6g2r7tpDZBRB5_b5ngC5xrtYos9-9cDIwPcy2tNcBWqW91_ES3yFptpIGEc4vR4IKXRc9bQv76nGeEFp4dh5rxYVRNleSN6fh_MzNGwf63KW-CJT8qo0FdKs4Xe2clsy4wT_yguk-o2rWHcaL0tqfFhU42jKPcoyC8vEwsqAahqruSB6JEp7CQ930C4yh_fpkOqfYG9ZQojeq8D_PjzOITYtFEx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9OVLQHBYnck8r4an9MLPeSdj0_kEssPky4S7RrX6GQyQiAobeg-_wsLyBuo4Rw1mHS8hqSIo_y2TkNbB_0fDQJRolfGDvfqD7ZCNkTD1ORIAWndlalrOlM4m82X986ClzCLOkPLL4D1xGQGJtidh8n7tCzlYhAz-IlJ2QOLqW01IjqMTUSQcBMPV6h7slDaHcqDaqtme0CBh_vQHCNbSx8kd7XWdMp0k_tl1s50zt56K5b75bBnJXp4lET-iD6awfQPO2ouTCTIz8f7Hq_HWnN4HS5VxudNTDOUbJ_uiaXK2ofcrZeP0rQSoh6_Vj7Z0QhVTtggCy3k6ARn0cTZ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbmZs2euICu6Mh7wPG64WkuhuZvJ3VGaVOibTaMDj7luwlD8MY4IfAaE-HuCnxW7lpVqrBxO8waNSq-md9w9UJrle077rhyAX3u6UOjkqculgNS0Av2njxI_taLcIXzPzmO5refSRWTKjLWLqSY41GYh-FsUktyCWca4Tjb_K4nh_SZtPzTDCi1f4qNaZe_bBPMZVBhWw7RBhwSOhLGiL72v4pKY1b_FdzHISTS_vAIqXNYclHOH_p8rTuvREYZq9pJsb-5UjUzVMTNXQtvG6nxvg5xLemonOeS72Von-hckN4bZ6Z16FVLdlGmY2IJ_85zPZ2xnZpGSdNniC8IBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMIhZtC3if3vWW_0UGkZTvvXX-B31DsMvkeX7ElkT525_loUyBhLnsIopiYShMteHuhBFagi4csnutRZ8hRDLIXJBohq4DmtB8OrZy7IMRkfQWYxQX1yZ-JSMm_Mi_IccvZkyEmAm7lr6JRVQFXAiFHf-JoszeA6YfrixMIAG-0-njW00QZO_ll0c8cIuLLNu6Ah-I5C0hSgOdZfi4m1YbJ2T5f10-0UxrWq_gfGVsh9WbhFBR34E0oN2golcPQ1G6wIaezqz_IxMXDstH3TIjJgZhklqze3ofewNQCc1j0FGhp6QPJniZdlGD0BziH1VH5bHqHrr0OKaGXPn59cug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7j-uGgZJLd7Z9QHPvgyTLP80FId7eDRCpBsBLqgs9UQSYKtBrp50QY3XIyTzCtRiH0GmYAkPwRh4OndhTqus36PRIVDeJdbxY0dgWwoPYTXWejJNrx-VDKp4QjFUf1QT3myIbgR38M-V_hVKUzZ7gzq_E8QFQxWHGStQA51Go0cdkTxJnIzgQw2RnSsN-B1BSpB4gTuO7tIj7DCQ4RRhnWRhfjK-aXQgFQZvrCygKdcTvuTR-5h41T0dvXBp9C62qKZLPOMVShiu2m0Dsu3rXQqLt0eUdsaFXzsqeghf1aF8olGNbsNbu_DGVtRNpedyNKLtpVRshxk_MjWQnQaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=tlImCP9f5eJuzIkq7aj8OkczSjwALyg1mVPBeFGxzpEhBHkDOO3SvPnRHQDZhMeib0BF6oHcZ63PZVzMspKRRQSvO0VCuT3NPkxjW7-1ssildL34a2RLo7LGmpnkISQM47n7AlJeUoOtULPc6XjKiqKch7hBfhlUwz8xTriEZRHopX_l60jcF_EiiTtPd9sTOUGAk9PfWdY3B_sV-2mg77yky8zusL0wH7-Vt6KaQzgQex7mJiG-vj99fPOwhXOp_jFQBwQnVD3DMmliQtH9As0ypRYSIN9Yjceo90tlHTWgeLF64zgY5AePoWEC08WS6Nj09K34D0vCf4k2y8skZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=tlImCP9f5eJuzIkq7aj8OkczSjwALyg1mVPBeFGxzpEhBHkDOO3SvPnRHQDZhMeib0BF6oHcZ63PZVzMspKRRQSvO0VCuT3NPkxjW7-1ssildL34a2RLo7LGmpnkISQM47n7AlJeUoOtULPc6XjKiqKch7hBfhlUwz8xTriEZRHopX_l60jcF_EiiTtPd9sTOUGAk9PfWdY3B_sV-2mg77yky8zusL0wH7-Vt6KaQzgQex7mJiG-vj99fPOwhXOp_jFQBwQnVD3DMmliQtH9As0ypRYSIN9Yjceo90tlHTWgeLF64zgY5AePoWEC08WS6Nj09K34D0vCf4k2y8skZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxBeYD8-HSdxkkR2_TvT6MgUDbGDfzqzUyeW8RnGALhkvPKzLe123q-lT1wzoI7swI1tlTXCf644n1hCoOp-Ro7F2x9hPR_CTrlUMCQJgUS7RcdU4ReNZe8O2YqJlH07LqBN_yhRLv0NXAYH1Uu_oiOP5E_X6cI5mGOc15ujqqMMO-qmUmxE6pbZ45x8kFAWzBKSAirTGLtDBd9Vm_6qdSNOlqdy_iYJn_FZ0ZTnEvpyctY6oXuUfz3re-utz1cAoimwbmmT6cg0p__6Kr_iDNycxWRdpcrpi3q7MtVZNNT0_lWxFDnKPkBncTTE4aP8gf6jWc12PtGaaGsX8Q_srg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxeDHm2-qdgotv-EId4rizMKFvawtCDKUyEGtazFUx5IOX_FO5UWPLexDjE3HtLOx77wTUoq19_6E00A-t1p4JVTcc0rMCOrivjOB_qmWPVfaLrVAAJ56haTP0StiO2iL0DRfeLpDNyqh8OJ88cU_13Srbsol40mVACqeYKz5Bygnzuj0KbuM6lSD6H2IOcTinnMT7_x8MfjZYqJliGonnaVN0ggNpsi1xbUbu1k6_UsAQOwFVdyqPDnEITsifV8sIHF3dTGyTTFyt7zQcMOxAUQhCy7QnF-QQl15BjSrchkP9U-ZnvRUdMAnVWeAUi2HCCXut6IW-TOp4JcjwLX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsSFq12UaT4-m3T875ymXDEj9vP3Bwawl0APZ6irjL7vvyqij3oZGwHWun98UE0xC3pV8MMOZTmadN1pdhv32vnglRaBDFpLarmpogNttwQKYsC0oTRI5r_ryw9P3ct05q1DCL5uWVCfJsFy8fKL92JdxpEDT8U182zqEhpVrsUQ7-bgfEe0U6JUPYSZ6Dj-YXjBsZiL2Wn3Olbyd_h5Gj6dTYnLuiaJckM4IdsZm-XdzQtdUkZx7J0aktMu03kV61tNTzHxif3oY_q2ul8EO6dWrEVC5chTVQxI3eSzpi5Od3RxG3CUWWBn9pByGFVhmiMx3Lovf7F2ISBk7b3xSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=MYia_dlCo3QmLO2SOPzNBtVJ2KyU-OiZz-mzZG2WzatBhDQnVlbzHwK9DptBb8TLFho1SQ6okAXDpEZgI5_dSNUgpTORubnJXiWWS_8re8GSeKYES7Xu9BDSdTakxzdAZ71i3EVsamtUnlGsTU45dEO14xp_pfMop7jF2vjPAqLRg9lc4kMaXy1g-FmyFwZDQJTXBE-5II_miL7lEg-0jRw5g7aK2GsFmyWTOMScbDohOWzwfbdKZMsuWs5K6EQO3tHnr2YVHs2nshbopZwQt-d5Zqo18ujCv-wL2nGDlH7PzelOi8aJ4KiVKUxD_8SRYa9mzKvzFpz1Cis-79cg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=MYia_dlCo3QmLO2SOPzNBtVJ2KyU-OiZz-mzZG2WzatBhDQnVlbzHwK9DptBb8TLFho1SQ6okAXDpEZgI5_dSNUgpTORubnJXiWWS_8re8GSeKYES7Xu9BDSdTakxzdAZ71i3EVsamtUnlGsTU45dEO14xp_pfMop7jF2vjPAqLRg9lc4kMaXy1g-FmyFwZDQJTXBE-5II_miL7lEg-0jRw5g7aK2GsFmyWTOMScbDohOWzwfbdKZMsuWs5K6EQO3tHnr2YVHs2nshbopZwQt-d5Zqo18ujCv-wL2nGDlH7PzelOi8aJ4KiVKUxD_8SRYa9mzKvzFpz1Cis-79cg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC-hyK-YzkeiFx4iXjuaualBUcb7BQP4hSt5veWXxuQqZ5s3VYjFFV3AmIl2MTCGV3zORSky8ZoZtUqVaJBCL1mf69ZPo7GuEn8DSsiGSCmbZfFxdalGiVF7hsi1SPZeLqiuKwx1ujMC4Q9j3-L4Gm4TNC3oMmpgrXXzNdweSb5KWT-O5NqTatxaAmslNydH_S56Q5L2ng7FoQPDYq4m-ugMIMwdQnL9r-TRSW7Gzs9Fydh82gaXSHkCRiFiZJOnC15AT8dTXagSBDZoNlp2ItEMlW2Pyi82INYDNmrsmBp-hC2b71ulsEd_NOZc-wLueRk5r1CAdeYf_U3BW-i7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LzrDjYckKR8xow5EVt5QAu_GTUuBEFjJzBqjRs8kuD40Kbz5dOm0-E66sy01eA-4AackhrxmNa1NyIplrdzKB5kLq7dO9-ndsonvRfn3uX9kYWEvHIc7DQlZwvFNRtdCuJo5_oXYMWrJM_ntz_pLbTYNm18tk06SOAU37q0cWIukLuHgej-zmnsCqMWsXpTzXDJAWh_FPnNMP45grShJ8AUosLOBtUdgZLqri6LVGb8-H9UkhgLf7KeDiunF_dkA-RU76xFx1C30R2U5kimsDuklhQiyY3Y7AXrbk8J-0iNYdVjSDg3Gekm-CZhxWo43ZYR93butDnfMubfICOuKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LzrDjYckKR8xow5EVt5QAu_GTUuBEFjJzBqjRs8kuD40Kbz5dOm0-E66sy01eA-4AackhrxmNa1NyIplrdzKB5kLq7dO9-ndsonvRfn3uX9kYWEvHIc7DQlZwvFNRtdCuJo5_oXYMWrJM_ntz_pLbTYNm18tk06SOAU37q0cWIukLuHgej-zmnsCqMWsXpTzXDJAWh_FPnNMP45grShJ8AUosLOBtUdgZLqri6LVGb8-H9UkhgLf7KeDiunF_dkA-RU76xFx1C30R2U5kimsDuklhQiyY3Y7AXrbk8J-0iNYdVjSDg3Gekm-CZhxWo43ZYR93butDnfMubfICOuKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkcFg6XjPF9AKEyIq0DBa2G0Xds_DG7Wm9wAQlI4nrL0q1nhI7cR5iOgHushhEO0Kz_z9ihxCJTOwqOhs3m23tYPRZlqwcvUJIKzo-tH-3Ffi0CvWPhYk9OQ5U8fTVs5K2hBTjjw5vI4FhqVecvYzeZp-AojAWAKanhFv8GvIDZofZS_BBxHgVQXVGYcIZB6D8j-Vqz-d27djfwJSO60T3FzfkdqWmWn9hZqyUrFkwu4tJPKW1uF6Km5W-X187P8P-N2MsV7ObESLb2BWYbkM1x2b7z2YcwaXAMzWnAP6C5mhx3IthFBwkckQfWOrz0fVf0VhdZndlxGEtS2E13tMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVRxfvFC3wa0O5fyer7w5D0N9u1NOYNSAqpolPvMtDTAF7O-Z3vk_9KCMDFsjSVe_MjusN4q40or9ii71c1Py91RU9BD3A7pEFgEvE6j_hujGPTycp6Cy3yC3eypx-EY0ofa5rsc7Yj7a_LIV4yMfE9sWg1bLqcVUMe4CnemrRx4YsU58ColUdhkMaZvQc0hiLHUlRXdGDhRca8RyDoQViQds_K6MzHJG3xZQL6akvU9QOD4yz2YKfAj-HseC7QgePU5PYW9s4X-6zqZxiyVYLAGyxNpQxCOVZnhDummPi5YdM902CzqghPH14mpckleqdLcyhXe_K_etdx0GkUj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=vG2kTfaMcq-owk-CSJSDtLhX8AsK6ihHBy4RQ-YwHTZJAFh4kS6I2hFUh3Xj2MEjGOYeSUrEPBUkU7WcYg4XD5Yn2V25wo-490W0GXPFsahGa3o0oa-30-dopJ3yk41bVZvB1kfnRqmePGxEIg-Sr-dmTj-pWJGw_IoDNaZopzrGkcZVzeSUiwcKPYOLIeP_IsGck7tCQm_qhPkzhCYuET5cgR8Qb2iSaQow-LJKlOEIDxc_QKwrKiWGj_6veGGrpe1d7vFUPOaQ-deLMn9vDW5yqx6mBWvGns8aM6cNqLPMRF59VJVidec_4ifUwHQRZBC-Vv_65VqQpss0bUAV1zr8t2zyzVKG_sxAwNSguwgD6YG3ZLX58LvVGxOJdLoPrBFiQOYsEjKWwmImYABg0l3nPSrjvIzp_RWGK8mfL55xJRTTVl50anUzRMiK_ZSCu84fI2K_ZFbJR9lLBttOs3X4l2kedcB95Rs_ptven4rlr3DD0jFfM_OTkKEhu8EgVrMIDHk0L7hoEkdtB3pB-S5Lb4r9Z6WDKjtzTxXB3pM-XqVIbvZb3GdMOxm2nrUFcHTnsG1-x1mumpKo9ZetPh54T0ziKUNem45q_MC-AgY3R-9q4GS3BblTuLAOnLGz0VfrrvqYm0K1lvfBXal3Ql4TtZfT8_h305T5M27XD0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=vG2kTfaMcq-owk-CSJSDtLhX8AsK6ihHBy4RQ-YwHTZJAFh4kS6I2hFUh3Xj2MEjGOYeSUrEPBUkU7WcYg4XD5Yn2V25wo-490W0GXPFsahGa3o0oa-30-dopJ3yk41bVZvB1kfnRqmePGxEIg-Sr-dmTj-pWJGw_IoDNaZopzrGkcZVzeSUiwcKPYOLIeP_IsGck7tCQm_qhPkzhCYuET5cgR8Qb2iSaQow-LJKlOEIDxc_QKwrKiWGj_6veGGrpe1d7vFUPOaQ-deLMn9vDW5yqx6mBWvGns8aM6cNqLPMRF59VJVidec_4ifUwHQRZBC-Vv_65VqQpss0bUAV1zr8t2zyzVKG_sxAwNSguwgD6YG3ZLX58LvVGxOJdLoPrBFiQOYsEjKWwmImYABg0l3nPSrjvIzp_RWGK8mfL55xJRTTVl50anUzRMiK_ZSCu84fI2K_ZFbJR9lLBttOs3X4l2kedcB95Rs_ptven4rlr3DD0jFfM_OTkKEhu8EgVrMIDHk0L7hoEkdtB3pB-S5Lb4r9Z6WDKjtzTxXB3pM-XqVIbvZb3GdMOxm2nrUFcHTnsG1-x1mumpKo9ZetPh54T0ziKUNem45q_MC-AgY3R-9q4GS3BblTuLAOnLGz0VfrrvqYm0K1lvfBXal3Ql4TtZfT8_h305T5M27XD0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Ei4AXTIsbtNOuFQieDOX8tL-eeQiS413wZ4fK5faPDFnFBljoKOlSOZbgfLNcxlkQj9o5Ed-nkKVYfSg6uevyLmMZWw8oAJX5Q_GYWz0E8xC1x8j_l0r5KBqadChbPoPxNLQOmF7bFibN8vZLE7cP5xeIF9noFow4qWdkLBPuy8S1vD5w4e2n21WPrFx6qeNH2mUvx2t5xC3Yc3Sz37wrDqxm3dx87QBcNJwOQ_bjmqchkzObbJ_comY4vplvkKvAcGqjHmJq5vaVAthA9ZwltiZPgBtrfwmd1TkiJbQVMpAjnuCqbQ1kwW-B8O7G6KCbelnHO5gCOn4A8nbTVkyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Ei4AXTIsbtNOuFQieDOX8tL-eeQiS413wZ4fK5faPDFnFBljoKOlSOZbgfLNcxlkQj9o5Ed-nkKVYfSg6uevyLmMZWw8oAJX5Q_GYWz0E8xC1x8j_l0r5KBqadChbPoPxNLQOmF7bFibN8vZLE7cP5xeIF9noFow4qWdkLBPuy8S1vD5w4e2n21WPrFx6qeNH2mUvx2t5xC3Yc3Sz37wrDqxm3dx87QBcNJwOQ_bjmqchkzObbJ_comY4vplvkKvAcGqjHmJq5vaVAthA9ZwltiZPgBtrfwmd1TkiJbQVMpAjnuCqbQ1kwW-B8O7G6KCbelnHO5gCOn4A8nbTVkyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5fmpN1RPiyQdQNGKd89ZHj_eSXgBPcR6nUYV1u1xCf0tzE3KC0Y29QFXud4Tg2fs_NMoz5Cr_qf8_lyJL37d3vBi7q1QTd4E1EhRc0G-kr_G4_BdUSjj0mJJMG7y7S3O185Syx0yjZIfFaHgGEe8iXhrv7uEYpAdi8h8_e6exYuHSupPAXYG4JfE0hXbc7LnGCUUc82pXsx5_HDEjHW5QaMiHoHC0dodoFVKKgj7Yk9SGPFVBiYnZMKUxrpjc6MJ5mGLRbmJ6emaxUo1wBxGpqaTxB9h3s0XZ-_FEisAOiwYqQxFOPuD03ecsgvb3H88Jm3bbHZsQtgZwUVHq3_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Fcbl1gsOS9vsG4dqfCQuRV4t1PNGmddSs669kMiQmESZPE6uy79VWRfksW50JxT2x_mnUGbsJihWV_iMMom3j_o_WPkilEjH_mfVK5mPn_G_wHJaC8x2sCPx469VviTFc-7YXM3OaoT9qBV5cVw0t2mH7UoWymzfQa0WhG4nTPRVEFUO3d4V22YlkzyuLdfEf7nFisJvAccLiTfQLLSk-ZehZDKVJYx3uheCbKQUaP4dqkzsRiuqQ2W0Nr7mjzYgb1ZE5IuBbiKDrCUavwfCwnZ1n0TnR4wU1segdib9bCi-tdSzSRQXmmHClUJYBuHYZmE-W-jce7ejFHmB3PMGnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Fcbl1gsOS9vsG4dqfCQuRV4t1PNGmddSs669kMiQmESZPE6uy79VWRfksW50JxT2x_mnUGbsJihWV_iMMom3j_o_WPkilEjH_mfVK5mPn_G_wHJaC8x2sCPx469VviTFc-7YXM3OaoT9qBV5cVw0t2mH7UoWymzfQa0WhG4nTPRVEFUO3d4V22YlkzyuLdfEf7nFisJvAccLiTfQLLSk-ZehZDKVJYx3uheCbKQUaP4dqkzsRiuqQ2W0Nr7mjzYgb1ZE5IuBbiKDrCUavwfCwnZ1n0TnR4wU1segdib9bCi-tdSzSRQXmmHClUJYBuHYZmE-W-jce7ejFHmB3PMGnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l08wbpW2xUsc9ZVablahol4wg1gmL0upbudZWaYgt836ldNYD4kkwLGCJi0y5HETrIt6I0xzEL_fyy11dP2xjp67l0OoSaLkx5EOQOzT7Oruj2VxnZQB0KF3H-jekzB27PN1xI7U8OP9FfHHw5vHgoIAcZTfIMcKAql_U0V3OC82vfmVcgP_78Li8V6tI29Wp8aLuqQlwkTfSXLzHGHG9kNh9zio9YmSaMYGyyjsPpavs07gONYlxWsLsk8-gOo0Ag8urCxiwWcm_oHkUP2Y2pRN0XWG2fVrhT_Uq7ycQ2tPI86vbm9tnNdok-XWu9hr1aCs0_J_Bf5RsquA-Ek67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZMr3Xak5poB9XHm4-u12dbV3qti49fGlWV8LyfnNCpUgEryiDAI2f_C_vpV6W4AWvZwObFyRvE3Hz2dUUkpRvSNeD8JKqBjKqeX2HsHAi8lW0Twg3paS6YStY_JvoIqt60ar8z-LfPhPtQL8hSJJVtz-m11_w1gRrS36Ao24SNWpd8YfWszaKgBUHudmAdYMQ-aVHmD8qybzpNr0Q3Vs5F11LHrW7b_gRnXGx9fSi1x1d-oiTx0aApX75hvwhySP2afkKA1NWUE4mmTM5DnJagX62qyMrBHF45L8s3KqA1RByZ4a5-U8VBPEkVbxMJokaKx8tDtaE4pPOocsPOQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VovAc690i5zdon36seI2LDaiEbCgpdt78EAhuKNRszT4QHuI1MuVjwhxJiPg2l-YFwukNeV2wNwicpGUVFqxTJI2kTssZX-QLqHIVdCRipm5rfE4es_kG5kOxlcvFMEn_etPiDW4QGCC7EesuUr12oo3nlEdX7dhRBdL7vh7VwJVc_sSYXt0DQSibgFEIO3GSbfsOBWhMa4AvOnOF8W5kbC9n0PLjrjvSIJLQbaA6pOUlNe6Yd_9F8T53WskIRotSSsbIyZw_jVYNy-e8ACnM_3UgLfsmhDLB41a9vR9EiUbjQDwZa4XldkKoF4V2RhZV0tsghawV0DVqZbPAmA5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQwjwc4tTu90AL90P3uO-wp6aaSW4rEb6HdnAnRS2mwcnV6OD5nPQHpb9YTDjKqB2mv1Xvqpo8T_anQPzBI7v0hYpxVZQotWZ5Cuqvqdzjq9Vr4nJpySJ-wpSdJKT7vOXSuWh6XAa0zzs5ZeAR5mSeXZV8Ru2JZvBWSm1jnWxCxJHQK6hILFdt2y8XInAG6TQD6FhyDns5Ftkp3pRbXzfI8rhBQX5lrzcuw2W-uLy7rQOtvgItjt4Hnnz70PTxjtap_wgm_XhMZihWACDQHuvUhUfD-pecQq7I5YtKy7tLga66TB-TSeZ_vKULpzs8f4rN4S2BWKMtVLc14d1WRkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb6s77cSdZSSnVoEGkP2Ntu_QH49KZedzaTqdZ1FlszMkhPjOn6D1wiBYj7sM3mO03biT92vRvSJ76uIMg31sVZJ5zmzmWN_EX3HsV3aWRR734Q3QIPTpps5_gW2d6Ho5hX-0wmfoOPD_BHVuuXOifgNML4lSve_w0fLtvX7mWoAIyCi1fsXmxokRdEMA8sBjlOfb-I1uTDerh-wKUELDsxK8rP4-tXxF_bRmD4d1aeZfGF6ZQR8kVN32_YLlHSFa2xaW7bP58y6vKptrNcQK2SMRFoROnqbE--WH0F42gsDOuzGbjB8IKsgoIjTXyJJIn6Lp1NfsZfYhrHdhYrcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=L2yxIzI_IYKxZbJh-stoegHCYn87VzW2w4W3kCEdBPi11WRUkCG3Bzp9Ld5wye48AFHaIsBeKm5O7laClm42FPRXx3LSwh6n-_biPWgknw9nm2kDjUgEtYcdkrrFdf89AWJTmmlJhK3NqmjkWDiXjSEFwgSA6EHlwuipPO9gHEohlWKyCF1rECqe5PqZ81QQu5Ffrn59sH-Av0YZ-HnL2mQUAHvhr9zTgDYK3NDW37TopBg9T2U89KbVdtGCkrRbN6DVByBg-quiuIHRu96ipu0ToclHZukr7WYGPB7zrb7VIB716dZqLwGoghhTepKoRRVO8-ibROKEjufdJneaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=L2yxIzI_IYKxZbJh-stoegHCYn87VzW2w4W3kCEdBPi11WRUkCG3Bzp9Ld5wye48AFHaIsBeKm5O7laClm42FPRXx3LSwh6n-_biPWgknw9nm2kDjUgEtYcdkrrFdf89AWJTmmlJhK3NqmjkWDiXjSEFwgSA6EHlwuipPO9gHEohlWKyCF1rECqe5PqZ81QQu5Ffrn59sH-Av0YZ-HnL2mQUAHvhr9zTgDYK3NDW37TopBg9T2U89KbVdtGCkrRbN6DVByBg-quiuIHRu96ipu0ToclHZukr7WYGPB7zrb7VIB716dZqLwGoghhTepKoRRVO8-ibROKEjufdJneaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzIA16k03oF-09K2Gjfn8wMnvoydRP7TqXMK_3AXh55mfthCtfqRxds0OyjmkbbKTmFv3SBDCOecpZr6bCa7L12dxG12gQ0nAQXx8_FiibZAlJmRhPVAWmCfY0jtD_24Tw6WjfJECSCQefZ0LMHd23gfBK5rsu_XTSEFKdYrccUyC_3zpkmnPxZtBB3yipzorqC3e4diGSMX0sycYuBca1zX3UyXfLday7cl459SdgSuhpXJ_AetAbayfKsXPzSXQMpiKFQbFYzTFXZkFiMUBVyjRgF5HOa1W5JB1ww0JFWc-5NssXQMrVwVVqctPW2nFRsnrZrFVWGpkYkNoQzifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpzBHrmf8Asj6Un6ggp881c5dlSEFfj2p7frjJkArvdkDKQWDptF5NbRPdZ2HLyBDvTZo3Qj812eV6fau5JTCVi2fcwlSqNs8_j81Bp8Dz1ZKgtNH_K0-0GlywKLp1T3KJag_-EniXgFr-1TkSxAcy7dF4EPYmdjWTleHTwp_9ZFVoIUGEszLoHwZ3gIjC-P0sPxsuDLCpm4k8Yb-4vKlwuchH7Z13r3AravG4NODi3FNQrYWR8sJ4p1pSTppcY7VS9IsCGMyIYMFTtHc9-h3jDCHeG6jreqTt0q-wsZHTFzQVHDkOGwIAYa1qyLXF0prD6g_lBqIvjwUuFvRZ6RTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OWrAXIRGgp8r4aKu7YLb4tTcZU6UuKqwKsWZsiZ6qp5E-E2oLvl-FX7mypiqAJOFBg7kNcjl66NTZ-p3QJbuCS3PE3ZOa2IsbRur-WnxMyfuxXx8p1N9YPa83MPWlJq9gU-MIiJ8LzQJeXgI6N0VGJySGGTH_ihcojxR5xMubvZWnPEp7Ab1EkW2yn2-6nArLTdA3L6YIS_weaKBh34ltF0l6C2wvdUOHNKrV7oBXJaAnsCF28wQtf0DvJ17n74N1Mz-S5RzTE1xyzWxCDPjmiAELSLtO75DO7nMwsHao4ENb61howqujYQh3UeJ6MiCXFFaYCs4tyokHP95FoKZhxmfp3K_BOUYCE6JwSwl9mWhgZaEol2TcSW0Eh6Yv5Cheptng_2J72ErZ9YO41n9EMI3oJod4F8-Oq_ZSXPu5v-5Vtt8ZOh2juFVaAeIL_5V4qnnLh1lSiygWTITjNAeuE9Rk5kma8AujaCjwrnKJOuTtdP8zL943mj4BOuosLM-_pyQnxFxf6J4VtfNIQfd1_2A5QMedl2Rlvt3hlgbpxgfdjmSF8AvhYqjwzhbvMa9xOGJ2euBJZHB_o0Ja8PkQs8kYbuPgPr_jvTxzsp0rvjUVLlu849oxbz9g1KYAXPXDj2sMnEDyWSgmTr36FtfgStb6_ng92Nx-MwvFsP08mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OWrAXIRGgp8r4aKu7YLb4tTcZU6UuKqwKsWZsiZ6qp5E-E2oLvl-FX7mypiqAJOFBg7kNcjl66NTZ-p3QJbuCS3PE3ZOa2IsbRur-WnxMyfuxXx8p1N9YPa83MPWlJq9gU-MIiJ8LzQJeXgI6N0VGJySGGTH_ihcojxR5xMubvZWnPEp7Ab1EkW2yn2-6nArLTdA3L6YIS_weaKBh34ltF0l6C2wvdUOHNKrV7oBXJaAnsCF28wQtf0DvJ17n74N1Mz-S5RzTE1xyzWxCDPjmiAELSLtO75DO7nMwsHao4ENb61howqujYQh3UeJ6MiCXFFaYCs4tyokHP95FoKZhxmfp3K_BOUYCE6JwSwl9mWhgZaEol2TcSW0Eh6Yv5Cheptng_2J72ErZ9YO41n9EMI3oJod4F8-Oq_ZSXPu5v-5Vtt8ZOh2juFVaAeIL_5V4qnnLh1lSiygWTITjNAeuE9Rk5kma8AujaCjwrnKJOuTtdP8zL943mj4BOuosLM-_pyQnxFxf6J4VtfNIQfd1_2A5QMedl2Rlvt3hlgbpxgfdjmSF8AvhYqjwzhbvMa9xOGJ2euBJZHB_o0Ja8PkQs8kYbuPgPr_jvTxzsp0rvjUVLlu849oxbz9g1KYAXPXDj2sMnEDyWSgmTr36FtfgStb6_ng92Nx-MwvFsP08mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=pX_bmgIg6uwQ6c51WFzdP0bx8NxeP_Fe8Kbg4SuWVt3roOXuCBgw4YeyMcy-FRLX4xTQRHj2fx5vP7UsSu3nBa0QclS6IEXiC640yl9xE12X8jCga4KB46DJQJ_a2VCp0dM45nLJI13IKFiIUBhQtras-g5PHqIz8NrnFs5EkquZa_-vZc7FlTaVF27CZoGK8M2jcxNmhh1JNR-8akI0rtEKPk8v7i7obqZxvH5ihBYjy3ajuGhQkBzFnhc6FWFKqXYnxn_sIZz72somN2wDBN14V8SvxRBc8zigyC0ASQA5JVELC6DXcWwN_yWBWz8iH-1BJRFpQRUJMnDlyOIv3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=pX_bmgIg6uwQ6c51WFzdP0bx8NxeP_Fe8Kbg4SuWVt3roOXuCBgw4YeyMcy-FRLX4xTQRHj2fx5vP7UsSu3nBa0QclS6IEXiC640yl9xE12X8jCga4KB46DJQJ_a2VCp0dM45nLJI13IKFiIUBhQtras-g5PHqIz8NrnFs5EkquZa_-vZc7FlTaVF27CZoGK8M2jcxNmhh1JNR-8akI0rtEKPk8v7i7obqZxvH5ihBYjy3ajuGhQkBzFnhc6FWFKqXYnxn_sIZz72somN2wDBN14V8SvxRBc8zigyC0ASQA5JVELC6DXcWwN_yWBWz8iH-1BJRFpQRUJMnDlyOIv3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCks45maBFbB33p8vrMFWbYWNRQV1CkRhm1PY-LgN9WTPfPw4DWolpUqn2j2mIkFlozo_AK4wozs_nONqDX6qreXUxLXorHizKFHuUKWhgnFcTDQ4jD-3PgWemsWBGV5v0YhYe5ctkLV10Xg1M101NGDMI_-thx5A6RZbq8yr3oavWmPCwv32IjKig-2Id_78KzkzHe1MeaY-eCx0NVBKey-yb13x1ng81KLu-VQW1PtlclbapCa7MYxIcRD_3yc8JmMOIok7zuW3l0gb5pNIRti1NXFkdlHDMxnLDpmnTXcdtgFKjtdhsA3UqBB55qx9ocq9KSvDW8g83x6WWUorkDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCks45maBFbB33p8vrMFWbYWNRQV1CkRhm1PY-LgN9WTPfPw4DWolpUqn2j2mIkFlozo_AK4wozs_nONqDX6qreXUxLXorHizKFHuUKWhgnFcTDQ4jD-3PgWemsWBGV5v0YhYe5ctkLV10Xg1M101NGDMI_-thx5A6RZbq8yr3oavWmPCwv32IjKig-2Id_78KzkzHe1MeaY-eCx0NVBKey-yb13x1ng81KLu-VQW1PtlclbapCa7MYxIcRD_3yc8JmMOIok7zuW3l0gb5pNIRti1NXFkdlHDMxnLDpmnTXcdtgFKjtdhsA3UqBB55qx9ocq9KSvDW8g83x6WWUorkDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNWCMi3rekHhpaBoeJjBPXQkiPAB_VqnR43ZsNzGx5jQ1Ruq-v4c3bD1IMQf1bSN_jpBvYDqeWEZXje81QqkPagNcnNH6mtJNUkg9mkhq3lAKl3QMLEH_-3e6W7ZQKmgPPsTKgUe9Jjwp28UBRx06fkk2dxvPicwUuJDPUZNVwXchkAaYEaV6cnYYZdk7d9UnDSw_CX11-RZbpmsxZpx7JsuVrFJaAfjoEGhwXE_scSyEbznZWDpu8qAOFTWo47Fk3VNFyItdGRCp9cfnBsELD-rzILBe9Q0PAWSaIlKL_WrCLa64BqaOraJcyP-8cuVtPwReiGD-0lofXUdiLr7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNrVq8K9mfYp7Rzta5i1zY7FMZRykjzsPDPO35ge3Rx_t6Ptyl103h1A22XyFSmdZcT_Eqh4-nHkCfnsvQMS9MLSuIH1DA7lswIC85ysD64uVuhVIXAZOrKb_dIS6ePUqQnQu1CHEVWtdcbcYm1RHSdmqahqBFDB7eCQuG3miebWmFuOpph3COUapK815_QnXt3EJ4ndBI0AsOl1b89px8qxNsnYc4cKqUd2phRJ7m8EAikTpIRzuJ44aa7_DIdZhulrgFzZKq_pWv0MjZGkW3osR4wGlnqZYCrD295nesnOuMaSBjmfn4_YamMm1dCFamEcsr0jQaX_YGZKk5pg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvGimK6ou5iMzyfRWEvzvOxyMF5nieNqFE9abX1P3Z3cx3fgYR-IDGHwDTPWWuLB_C9M-arE1IM2-ZZ4u2GLS1X4Rfqy4u_K1zUkTqRkRPfi2awmG32-C0WrU7M_R_j3Iq-KQq9lsCRWvpRyNtI5H-JtDWiePxjrwyYmK4zHqAfBL1gO1008jjJUYOvzd-pdYrVZrzPuuDfFXN6FXsckpQvvtvbkcm2eGNloREigE6PAsNBCAKYwhVEWZqavxOAf-A9DzNEnDfwLwcG27PDEGuBt_GSGSZYAqyhpGLc99wnhoZw9-0KzyiaGJyMrTWz-6bkPnVx74CDkd5K3ijA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=lA2SGb0J-WoQTTxWjkM0987D0sq4KxEZVnHdq212Yhn1J8dYNfXZb0WWEQJjQHlSwkj7EUsGP-hiu2zPgphAwCUY4MVw95IPR0tKBWpXdgRdggwqjrnihuKYGXfH0fS_sULWQLJzywkh6mQU8ABdNovlv82O3LspOOtSUOzV1ataCEdWe9E_pAiAX9rIu2jyPsFZZyJElv8aFU6kfaxi0C0j1jNn8BHe9Zmw1eZnM0zWk7mQKe2OpN9oLgUYTjOA-IatIZcnsCHJ2uBIZkuV_qqLk8KTVC-lA5wcYmGNUcByq105aTli-5Q4YKL__iqYL9jQrWRVPgCp5V6fcWOPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=lA2SGb0J-WoQTTxWjkM0987D0sq4KxEZVnHdq212Yhn1J8dYNfXZb0WWEQJjQHlSwkj7EUsGP-hiu2zPgphAwCUY4MVw95IPR0tKBWpXdgRdggwqjrnihuKYGXfH0fS_sULWQLJzywkh6mQU8ABdNovlv82O3LspOOtSUOzV1ataCEdWe9E_pAiAX9rIu2jyPsFZZyJElv8aFU6kfaxi0C0j1jNn8BHe9Zmw1eZnM0zWk7mQKe2OpN9oLgUYTjOA-IatIZcnsCHJ2uBIZkuV_qqLk8KTVC-lA5wcYmGNUcByq105aTli-5Q4YKL__iqYL9jQrWRVPgCp5V6fcWOPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fji5g0DY2n_wwWQIBQX0bzNaurkpmSDeRg8PyYsnBMFDvQ0SA16CbaKIqWUGwRNlLf1uBcBuBIQLrHSpFowuuAWrgaGJEcmlXW1Dqw7IjtkbE4Xpc60e8N58ui17_A6GD-dMKmfrLMrThy0Z0Qz7ny8j-nUgGJy0OzqDR19dUZ-iNd7x_KyyfThORdQSHbl4LS0LIfixzrThhxV9oS2r3iJD2-nzZlSOqqbsuXm4_izQz_kOCSJm_dPx5-vpVHgnl4a6eimzevcfHAjdkwQXaAA-7fqfYpFEumTIGwyjn0H4gnlmWgYlNQOqgeeJR2UMAbBdIPBk9eoCQNVq-TWiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLflAQ-4t19j-UAua2dVXf9cr3pmRdmqZlviiUWnxm_KIY1FE4LJBTMAAD9cw14_deXAum9FNim6t3P9mUlMYSV-8L0l9Qm9xed45gDQzoWQjr_LYvVJemLbMkC-lhZ3kp0fnFmQnt7OiiJodm5IEH5I005cLG_xgaFgZA74s-EUyE2J6NHTbsgtCU3tS7eik9GJQ5vTQhbZU1r3b1o_QAVQC_DdevaJehBAtuWPa6ltskiftUojOZ_E56DkuksH-zDv0w423cYSYYy3UNwOWz2P1AI2g7uUgvZVdN82MQtarHVIQod4d-jV6uZfph6_sOQn8onUB6qjKzs8S0QEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMVANvpxExLxKQPiNP4HOMo1LsGiyv1gVThW47Vx7azFKxtq_Y4mqFx-nXGLmVkEZxltggn6PZYdqS9RHTPh2DKNSYl271VDDWwJN0VxcxqStVbtWoWcZG2aLNZ4HQoV3JyP_sxMffHH4BU3OPcoVhn5ugnwCTW6wDXyZ3dGm90BnfahVsCGGthApRmI97YwaktMVEeDQiA-nz5r04Sq2P2SEMtNkPVkzbfd226vgj5bQ0u79EN13Q0YN3BqM8pLvXSti8S1g5FrJeR62pHiQheXMP9DGbEX-2Es1AhuVgUUuJmuEyXt9cEF7ulE2O8Pjc49VgcEcQcGuI31dadlAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4kngiA87gSLYZYqiNPxZwT27KbgDVjCWI4VdGxWIlFnIfKcUN6uUuHBYOZSKr0oUlXSFhyhfgKcagDTNtLr0SlhRiLPf1SiU44hn1PuKwMTCbGQEqFyn9UgfX868ySorHYl7l5RvgL72B5pP5_1I2f2WkbAJ5g4T6DGAvZbcbACtpzwjXgwIbK1HX7s3AXs84NdB9S3b2bHhuinWEp6NPXSlmKCjxtyL1mA1vqG-68UX8rwdL42VanIBOmBDzeFvq8asSFS_9e4SvBeGbtGvWc1mpqrm3c-vjujfh-wwOSnSzDkPu5ZR4pQWIbT5Waui39BXyNbav1ykegWuDgEQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=DYUnSrbsJLiDahyYnSWdq_7UCFuMejverdH_qmUByoWfjGFG8cp68llglmuVFuO-EX38PTIfe4IynSrQMrklmQn0mFrgk3zB21W8tvxPKCj4OlZi36k7hiUPbtMwyA16-wmdmVGeGpS6trrPJJq4QCo1CJlYkE-wyGz8CBOsoPo45XzxCgAABEjLUyP_xcdn6smjdo1hTyAc24yrjjw_FNCx-uPvkGF1hE_GwHW_vPAvFCMB_8hcoST4_owwiEgMem0LmA69G7Uvvjdj4v6zlFnTUV3FuULajiqtAJo3U2JDkJQ4iNMJAJJvihoymU0GKbzWkj6EKl95MY87V5j_ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=DYUnSrbsJLiDahyYnSWdq_7UCFuMejverdH_qmUByoWfjGFG8cp68llglmuVFuO-EX38PTIfe4IynSrQMrklmQn0mFrgk3zB21W8tvxPKCj4OlZi36k7hiUPbtMwyA16-wmdmVGeGpS6trrPJJq4QCo1CJlYkE-wyGz8CBOsoPo45XzxCgAABEjLUyP_xcdn6smjdo1hTyAc24yrjjw_FNCx-uPvkGF1hE_GwHW_vPAvFCMB_8hcoST4_owwiEgMem0LmA69G7Uvvjdj4v6zlFnTUV3FuULajiqtAJo3U2JDkJQ4iNMJAJJvihoymU0GKbzWkj6EKl95MY87V5j_ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=KXxvNasVUSxwGxD4K9eaet-7SIctvYePNaDjy_ReSwrWbRs9KAItsuQQlwQ_81WR2aFuPU1Z8AmASCwHwOjPK_cpbfKzEsBBOHJrRZNijqodid_GK2gcc0AnjZEv687jp0uTyAxOy5O9fxg-Qt65LDAy4rz1oT6H0_R7OfV62DNacufA_R8nJ5DP5A4BnV_moNfB3Of6DIbYjvPU3xtyZCnwwipRv7gFLKzGExm3m-qSTx10fMrwmeaAK6gDxTHJj8aB2Imr9a3uYIBQ6KhfPJF5uEzFMyf0Kuzf7djekO8vp_0zqIuYUKcfrd_UZSynEiIWHhUh7jPEdX9NfI8qSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=KXxvNasVUSxwGxD4K9eaet-7SIctvYePNaDjy_ReSwrWbRs9KAItsuQQlwQ_81WR2aFuPU1Z8AmASCwHwOjPK_cpbfKzEsBBOHJrRZNijqodid_GK2gcc0AnjZEv687jp0uTyAxOy5O9fxg-Qt65LDAy4rz1oT6H0_R7OfV62DNacufA_R8nJ5DP5A4BnV_moNfB3Of6DIbYjvPU3xtyZCnwwipRv7gFLKzGExm3m-qSTx10fMrwmeaAK6gDxTHJj8aB2Imr9a3uYIBQ6KhfPJF5uEzFMyf0Kuzf7djekO8vp_0zqIuYUKcfrd_UZSynEiIWHhUh7jPEdX9NfI8qSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=m_j5x-NQ3J5Q1z7vRtpOWhmJmsw1Amv4FtDS25TB6ccgJv6c7brtcBgYaf-r4WVxLxmISOfgBM3X4tmP2jrNVkyIDOGXAex3MFy6hk-2TJRO7gl8kscUxyrMIX_d2kU_Wngpu5X5rKUSzekYeJbUDf5nqv4QimR6abXw1S6L3NPxEbwSNYWNI1NIngunL3oUdddVDRVe169cKA7XGH3bYWm_KGSHvchfsMUgEtfqgsn0X5__AUPKYA74UVGgLI_APrGtu61qYBTInU3_hFangpYKc1f75CVxBZneRbVUhMenL9fIiGRkFn0XzKCg1Kw8K7yUkZ63foY8PffIjwuaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=m_j5x-NQ3J5Q1z7vRtpOWhmJmsw1Amv4FtDS25TB6ccgJv6c7brtcBgYaf-r4WVxLxmISOfgBM3X4tmP2jrNVkyIDOGXAex3MFy6hk-2TJRO7gl8kscUxyrMIX_d2kU_Wngpu5X5rKUSzekYeJbUDf5nqv4QimR6abXw1S6L3NPxEbwSNYWNI1NIngunL3oUdddVDRVe169cKA7XGH3bYWm_KGSHvchfsMUgEtfqgsn0X5__AUPKYA74UVGgLI_APrGtu61qYBTInU3_hFangpYKc1f75CVxBZneRbVUhMenL9fIiGRkFn0XzKCg1Kw8K7yUkZ63foY8PffIjwuaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAUUHt4UgzJJ1oIJhJr9z8JhTN87nT04L62pE944n4DExw1Ghh1xpqJW2UeQR-BaWYv7W1wIG5DrGJwkgp5gqHoGXTrBgKYnVh6_feubfoEhpItRDtqFTFQgXL86q7o1YyGUUXFHNUvKew_h4TA8c5Bo2Aw37qjIzuRkKjNkMl8diNRcFvnlKsqlPL3g_-R3Uxsd4bTueUTDEwe1XmqE_HDm5P4QuL7fx6Z5ZxW1EXsUkwXU-dZH5town0yA8jkHMahMeynhuw7XoPDtyYqYkxDBcNnKAirgocyeN1NwjOSPjcDJLWWoef886UzPxkkRJBycxM_kHzXFkBoRn4BnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=TiTqSeFVrfKjIJvE9h14nOWGdc_1ZRYDKEdf_BRmrEGA1GQHGlbewfEymRJQ-PzzJx7v7WICmNk5wOyovCR-1NIzybgbpwjpcnvbzS1tewwyYU9Lzu_6mAAVvwRBSlZ1z02r0w9V88KC68mmhqpQ1Gl3aRZOQBnqCO68F2X0VU2FOlhNxp7jVgUe_JayfNVL9a2Y7N0cGBDEljrtoRKlOPVE_HWdZtR4c2RYnDdsA1B9x-WmCG0hpZiaHR0GYuPQb2n6bcrFxD6a2a_qc-QybjbOv1cLi5_x9W3WnHNdaKBbCBRjF36x_oIiIRv0whaOJHKUzkNJe2UqXR_LL8s58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=TiTqSeFVrfKjIJvE9h14nOWGdc_1ZRYDKEdf_BRmrEGA1GQHGlbewfEymRJQ-PzzJx7v7WICmNk5wOyovCR-1NIzybgbpwjpcnvbzS1tewwyYU9Lzu_6mAAVvwRBSlZ1z02r0w9V88KC68mmhqpQ1Gl3aRZOQBnqCO68F2X0VU2FOlhNxp7jVgUe_JayfNVL9a2Y7N0cGBDEljrtoRKlOPVE_HWdZtR4c2RYnDdsA1B9x-WmCG0hpZiaHR0GYuPQb2n6bcrFxD6a2a_qc-QybjbOv1cLi5_x9W3WnHNdaKBbCBRjF36x_oIiIRv0whaOJHKUzkNJe2UqXR_LL8s58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=lFXDM_QLFeEcANZR0BG0SHixDxLes5TN3iOulVpJ2H_9CT0bowVzwEoQJtUhiOZ08HDt32rrKS_nC8bv5WUXK7CEwUg9-NG7fNqJu8CL4uN9gSfPoRqpZgkcQhCss16yqzFX0BXvUhZxRKXM5_1QhsV7LWkO1yEOvIW_CubKHJQO5LvRBHINjutYwFa90Eo3XErLvkLTcJBPmYW9n3O8PYVtrJgh2ZQHmYUpkM6eenECb5xELeYPGaYcgFGMxGAMzD0xBXRmWtKAK1vtjiITPSMS4aKC3fBmbxUj3j3fEHIsd9_OGAGVBHOik4arM82y-1DOTJNXGD2L5P-4a1AO1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=lFXDM_QLFeEcANZR0BG0SHixDxLes5TN3iOulVpJ2H_9CT0bowVzwEoQJtUhiOZ08HDt32rrKS_nC8bv5WUXK7CEwUg9-NG7fNqJu8CL4uN9gSfPoRqpZgkcQhCss16yqzFX0BXvUhZxRKXM5_1QhsV7LWkO1yEOvIW_CubKHJQO5LvRBHINjutYwFa90Eo3XErLvkLTcJBPmYW9n3O8PYVtrJgh2ZQHmYUpkM6eenECb5xELeYPGaYcgFGMxGAMzD0xBXRmWtKAK1vtjiITPSMS4aKC3fBmbxUj3j3fEHIsd9_OGAGVBHOik4arM82y-1DOTJNXGD2L5P-4a1AO1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=uBWsCJsyT9mAH6HAKcJWFNNZUayI6cQSYLnWcHz8h6lgWGrBLyNy0gp5-POne2gUH2z2Rc_5bxAd22Y9j1Wqzj8lpwf3shDMA3xPywDrcaSth78uZQ5YxQLMjGWd-XeXdpSlCJyqY4Of3FuuM5ZNxYU_yeXjghJSWrb8s8mMtWPUJSqkO_dRkAnnQmHweBawc2f3yPW3V8bNyUfWu8ljEexK2dv5b6w9_zGAZtsLwBqG5VJLo93MVZinxKVAgKv9FbMkmYVkFTdsWZ_sdrTMqSv0helqKHgH2p6Q_5F_WN8hICzPpYdxqzOGjGh3cuu8gQifyYH9-7eEZqFuPlcSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=uBWsCJsyT9mAH6HAKcJWFNNZUayI6cQSYLnWcHz8h6lgWGrBLyNy0gp5-POne2gUH2z2Rc_5bxAd22Y9j1Wqzj8lpwf3shDMA3xPywDrcaSth78uZQ5YxQLMjGWd-XeXdpSlCJyqY4Of3FuuM5ZNxYU_yeXjghJSWrb8s8mMtWPUJSqkO_dRkAnnQmHweBawc2f3yPW3V8bNyUfWu8ljEexK2dv5b6w9_zGAZtsLwBqG5VJLo93MVZinxKVAgKv9FbMkmYVkFTdsWZ_sdrTMqSv0helqKHgH2p6Q_5F_WN8hICzPpYdxqzOGjGh3cuu8gQifyYH9-7eEZqFuPlcSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Do2v__JojJLH76FGWqFtNmRFk8dczJU1ebx13MYTk911Sw7a_1ao1qmEb0zZTiUnFInu4XMs1Q7jQHP8a9bi0ABDcbR6Mv4jZVMnX3y8yiUnKUZiLsk0mcrWlaZq68-Sicu_sX_BI0lNjTqlHwxOXKHuiD1lW0VtLQBoeNSFbad8030KQ90xRst3So9rmCgMAuaEaOsSAWNZZFmoEqbNRqazZGsZaHKzS2CC0BU5UDHpqZ5rSxDuwgEjeuMr3PwEXxyUm9so9qHN8joYCbGht5Fdj8vmustAgGbHO6LReL5Yxg_NugbL6bP573fC9iBmU3BRIjuyVOlN6QYztvc67Jd1rxLcXXJjR8d1WGo7a5WMhRxjIppB84JA0xxEq_vKtvx8YETEtWsSBFIRc00Ia04KAYXVsRNKTodeY8TLq8cTn7Tm7AzccVFl2XWYLBqPOjxvhoHT1BzMAVSIukST5RlDK9Gk3Iv8XlxJcM_pTW_SpdiyhmTfkP84zQoFShYYISt5dxZ3LlCbhB1d5NEuXKMqqn4R0SmhSgEFzphB0vJyeKSKZR--KjAW2BeaFVJ6F08zIfCWpdg7Rq7Iq6wd_qlawwTTsdxx-Pe-WfhSR7araTytujpkRM6gO8EKjBuO2P7ptkeKMVSSfKqM1Jmo3V4jGNWpFLQ8f-Nz576eHV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Do2v__JojJLH76FGWqFtNmRFk8dczJU1ebx13MYTk911Sw7a_1ao1qmEb0zZTiUnFInu4XMs1Q7jQHP8a9bi0ABDcbR6Mv4jZVMnX3y8yiUnKUZiLsk0mcrWlaZq68-Sicu_sX_BI0lNjTqlHwxOXKHuiD1lW0VtLQBoeNSFbad8030KQ90xRst3So9rmCgMAuaEaOsSAWNZZFmoEqbNRqazZGsZaHKzS2CC0BU5UDHpqZ5rSxDuwgEjeuMr3PwEXxyUm9so9qHN8joYCbGht5Fdj8vmustAgGbHO6LReL5Yxg_NugbL6bP573fC9iBmU3BRIjuyVOlN6QYztvc67Jd1rxLcXXJjR8d1WGo7a5WMhRxjIppB84JA0xxEq_vKtvx8YETEtWsSBFIRc00Ia04KAYXVsRNKTodeY8TLq8cTn7Tm7AzccVFl2XWYLBqPOjxvhoHT1BzMAVSIukST5RlDK9Gk3Iv8XlxJcM_pTW_SpdiyhmTfkP84zQoFShYYISt5dxZ3LlCbhB1d5NEuXKMqqn4R0SmhSgEFzphB0vJyeKSKZR--KjAW2BeaFVJ6F08zIfCWpdg7Rq7Iq6wd_qlawwTTsdxx-Pe-WfhSR7araTytujpkRM6gO8EKjBuO2P7ptkeKMVSSfKqM1Jmo3V4jGNWpFLQ8f-Nz576eHV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=oRqWFzFcw3AH02GtBrpsQhlOv5DXIADUHWZK0VJcQH7RyVetoVf3ry8ATLukr9Er86V2wc2v8qGrjY1wPcMnhj189-Oe-Qi_NTI9WikQuUUY2W7P27ecux4be70a-tBWXUgd9NeinSetsPY0T4blqUNIBLKCwIxipqj-xd0TRBJFWd3c_QGVGwBfo229-C0EoOSpjzngPvrsoljtukX1ryYRqjQCaYflETdI6e9UUXx-1OzCDzfGyJ67sTB0AplIVhjCYo57BbBB12nuw_EfYIx05Ft9jLDPXzuiW0AxYSDVl65FnnIDLJFeZhrEaXCK6KzbmtdVloAly-zr9mZkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=oRqWFzFcw3AH02GtBrpsQhlOv5DXIADUHWZK0VJcQH7RyVetoVf3ry8ATLukr9Er86V2wc2v8qGrjY1wPcMnhj189-Oe-Qi_NTI9WikQuUUY2W7P27ecux4be70a-tBWXUgd9NeinSetsPY0T4blqUNIBLKCwIxipqj-xd0TRBJFWd3c_QGVGwBfo229-C0EoOSpjzngPvrsoljtukX1ryYRqjQCaYflETdI6e9UUXx-1OzCDzfGyJ67sTB0AplIVhjCYo57BbBB12nuw_EfYIx05Ft9jLDPXzuiW0AxYSDVl65FnnIDLJFeZhrEaXCK6KzbmtdVloAly-zr9mZkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=AZGcDkZT9EQBqvo-gcTgGDf1FVBGdKQGWVQNlnZbjuV1txdRd_TzD_ezzJI49yFzN-k8eBoRBDEtIAaY5baxkKF-cISMUaR_erBbuhRu_n9CNVqBcziRXlEsGXyd-fp7ylHuKHBOQWmt6tNedDFG0FsuBfR6g5JUarUAWtkA9MN9yRH7DRFST9qYnbh_dKBqsGLIGuzOB2jj9vJ2yoKLiGXxrVH_8ZErsWz_mAm8PZZgruNvk26FGBSNF5GxrqqLzzeE7jvgbeDkfuxnMZvkHzaVdMCWEQMCpu6_Mti7q9ftxQu27qweBLmVTiU8Ig_7iUo3LDf0KUZfst7mwjimfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=AZGcDkZT9EQBqvo-gcTgGDf1FVBGdKQGWVQNlnZbjuV1txdRd_TzD_ezzJI49yFzN-k8eBoRBDEtIAaY5baxkKF-cISMUaR_erBbuhRu_n9CNVqBcziRXlEsGXyd-fp7ylHuKHBOQWmt6tNedDFG0FsuBfR6g5JUarUAWtkA9MN9yRH7DRFST9qYnbh_dKBqsGLIGuzOB2jj9vJ2yoKLiGXxrVH_8ZErsWz_mAm8PZZgruNvk26FGBSNF5GxrqqLzzeE7jvgbeDkfuxnMZvkHzaVdMCWEQMCpu6_Mti7q9ftxQu27qweBLmVTiU8Ig_7iUo3LDf0KUZfst7mwjimfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBgbZ49xthmTsXOokBVXsYCcw8h-WvlicOV5Ixmg1iObhasbyUER6v4aetiwNjI7ZSMu_2OIW3PAj5QLeDHRsrpUgm7mMSfa8i11LgzFb0WuBRBQrWwr9-sj0BvH_9Uz8NI_6o1LJaB7Ql0yBOhm4J_VgSbZ5uxHUk0FtDMM88HtZZOdaOPVefkbzAy1rqUznGguIBbSXj1lfvp8Tqml1sqEoBHQEBUeNHFEmHJhwytmDY8zc3cadjotzwjQYp69LqgRapBth1Mf3cpUcWr-5cdj1-XzPQaO0aYhNsr4sTY3HcHCLDewoxhd4nO90uRdp7XOt4LeE5aQ1dLS0v8hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBIvjz9--Oao0j6cKuDVTNW1SCMAC0tmxT9jAPejQNtarJYWb7FJjhQeEca9C_E1Ob7DehXUB4ESrlUyBHJvKo1gr4CyvF-72WOZJeL_WcFQ9SFWJ3mdvXd8rxz-N8KljTF8KIVmjXSonXg5V4_fsFQ7vJuDSGdIbtIddqpcyiK-UzVXfAPZlryX10N5ZNGwGHreykLREjKvS-GuPsLp6CYpprC9UvEvGTNnuCtcSEEW8px7qQXSNB6qEVvgTg5LmfaKe1jmpEPkGPIMChRd6eumCdawE4AFjC7XJ-8jNuk9enqvn0aHElEWXrcRGCaa7tZpiGJa1-eAeiWVbUOJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WVyIFQtyb-dwaGlxw5TlkfZ9psHA8lMxp1ojCF5-W9b6SyuWwYPQo_mM3i7I959PJqHHS8cIe8866T4hvXhr21RiYXiu5FICe6iACCWXY9nA64Qfydpwn6FObu-i8cCv0iNQGEjno_IEIp10ckhF2ad_UgSiGzJw3rNDmXsFgMysDX1UGs0_P-QB2mXxyeg6IyaKD5OYjzwqleSfljAxUhpOfNIv2UgdNDiTxylpS1b26wvlz_E-9V9dAoYjPqywXGNyB3gCBsN4ARSy0PMydOns5dzJNo3XT5zEFlBK6nk0Co6zrurdyhAdAUPN1e370Iv9BQHUF-IXTenL37BOPR4moT_C5s157ueUuTlBgOIlwANZCgpNYWHc5hM30h5OSuuCiXAI0qCzlYcmiMxD_onw58wkk3W38XTkYB0Y50t8mVeK9UIeHOxR-Tc8dSxoNeMBeqXgsOIyQ_aLN6MxnhV1qoVzlXqoHirXziN87U4aYxyDTrpoJL1uwRcp8v-hLpeEq66MHxXkQmjLo9jB1p8X6Eiv2uYzrD_3UGtto6OJSbjZER4yG5xhRhtLHr9LZcmspbPR1l7rAAG5E2o6nkm6zkp5xv48Khs-LeAi3QjKI_f424EQ402PTYovbp3She4_FNdQU31vVLgHTwWmQ-Ap0SVV9hGr6wUxYkAo4D0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WVyIFQtyb-dwaGlxw5TlkfZ9psHA8lMxp1ojCF5-W9b6SyuWwYPQo_mM3i7I959PJqHHS8cIe8866T4hvXhr21RiYXiu5FICe6iACCWXY9nA64Qfydpwn6FObu-i8cCv0iNQGEjno_IEIp10ckhF2ad_UgSiGzJw3rNDmXsFgMysDX1UGs0_P-QB2mXxyeg6IyaKD5OYjzwqleSfljAxUhpOfNIv2UgdNDiTxylpS1b26wvlz_E-9V9dAoYjPqywXGNyB3gCBsN4ARSy0PMydOns5dzJNo3XT5zEFlBK6nk0Co6zrurdyhAdAUPN1e370Iv9BQHUF-IXTenL37BOPR4moT_C5s157ueUuTlBgOIlwANZCgpNYWHc5hM30h5OSuuCiXAI0qCzlYcmiMxD_onw58wkk3W38XTkYB0Y50t8mVeK9UIeHOxR-Tc8dSxoNeMBeqXgsOIyQ_aLN6MxnhV1qoVzlXqoHirXziN87U4aYxyDTrpoJL1uwRcp8v-hLpeEq66MHxXkQmjLo9jB1p8X6Eiv2uYzrD_3UGtto6OJSbjZER4yG5xhRhtLHr9LZcmspbPR1l7rAAG5E2o6nkm6zkp5xv48Khs-LeAi3QjKI_f424EQ402PTYovbp3She4_FNdQU31vVLgHTwWmQ-Ap0SVV9hGr6wUxYkAo4D0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rryRkFTLzwJw9C_dlnWZWtwrORmB8UCs-FRlhhN5RWeP2oYWvcjm_KvPpGYjugPJVdThmAr-UmfDZpW4MRD_cecUv36jhZOm69GZU-ARvaEHPZda0hOezZNa4C3nQWWoaFJQeS3EWq27pgLXK3--S4OA39Ff9NqQ4F78FFLTmuH22lCUmUHIDaGfSmNuhDBtKDCm0zAR0W406VBfg8JQJgjotuCFr97ejXTOCV0NGj-1zDnH51qQSTjxyCxk5ZNVYQ2MNaFZsRObF1YMuIc7cLsQTklFpWK0mzv7ceLanftlZmZEXZstYJAKHd9tlpvfz550BiFMS9zUzwKmctkE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N45Z9-DHQWtbx2s-LNGmfy_4PHAzJa9pcsJdlciGWKdpgRcu9c6aDCsMMfCqo4VJW5t8haThVT057ZtXygtRsKlWENfzKYD8Rea-WlhDlBju8egs1V5kGW8IWtR_RWPwGnHs6SeUfP0JAfeVqdLoTdquKAEgpHL5sn_LI6Cm-8nd_B0cpLKMwryyvZvud3D8Iqb5KxQ2Z3oap-ooYtI7Xjea-nJ9yEZCgE1dTBq7s-7TEvqnbMYz4PApoDjzZ1y9AJ2gZ7YmgT_coqhW8W17EL0E3p8qFz9x8ced9yoBQOZuTggp8N3scPp1XyZ7SybSYtn0jBnIcEjNbxUNnI5YoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw_Nmowe5rAd8-Jy_qeSET7GXwW4_Uc2j1-pJVOAJcSh9BgozFFVf6Eb-6PcZypvnxd7bzed304snlkE4WGPrsNj-Pok5gcsfOASRgOL2bl3FnU4GbnXbK72rpADXLZhAau14h0NT4HT-pt3alVE-XgTsDr-mZtabpzz4nSuIEJNGGcP54wc4nHKHdITRLdjhTKuvSzfVwOAdbVdu2mbeBBFVWJP_NxtTssDEMeiGUV8FJGGNanKfWT2vVA2pXeHl57n3cCrHUkgnEJUwq9pfNAYlEHYwdZlyACelrF1x5UsNGmkIbLyljWIrbiLdwOtLjMCFEPID31_tfJ_OWYrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjX5ozbYkBSg1usMkEIUAUobDVRetPNEQHuDq4eTPqm9Au2j05P48MH8jJyNejH88--B6DAubU1qxuC-jwTJa_kbWCkBeASBl87M2G4mE5sEYdH51m2A2yHVgTUcVUb0YlcSCGFVOzmpsUbjxrbuY3WoU5zMLjj5ZpSkGYANNc4MWij7P7SypaUWFyMUiwD7Xc_XNWTqmeuceyReTY2Lj5jrWqyIkLYwVl6O0RyaFgOP2KUcU7sWbbBzBzqLyxn4qAtGdr2hcVGLcybz280oJMiaDHZhSf1Gx21rrRp3vaAVc16j2FRDzujasaRtymA1IX24EEuu-i8CK7ps9JnX3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HdsFv8CcjWaM6jJKMJ7_mY_jOxr83ZuaSrDLisRtsMeOp_knjfr4lcUY9o6OerMYPF4LQYM2_n3PYbio8knEuAH6t9eHfqKsUakOPjGXwF6H6wBbDvpwM2cfZrR8bYYr8JMJTDISgcwY9sBOSmVVdpjfPSjjR6-HmrF-LItGDMsdykwo9VDKFXTKUwVQPEph4twBIGPzC3onknevG0jIvM9n8UZRiMze6uYYC07ibOcmsAg2cnvVPoV8foD5zaWpWgb9Diy0MZuGXps1gWwYZKL2eI3oYopDX2Z3PosiwlU1rin0pKCRYN-_0VneEG2C_PM11RJMfCtYS7co-fNa6nL9AbdDo8thH6YVr0y4Rrfg01aso08vkk7Sf8WzTKxrnYh4iqbVABADC4RBkvUc2tvb1m9HUE56CtTeLiJZ_sIqlODNfEllpotfcCo4Ea4uKKLmd5tc9C1fXjDPVdDqt2_Ftkn00Ar5I0qAL30gtrw83KFdN8pCKVDyE5byeDmagnCLLI5DtWOn-VCOPnnZAbS4x03Nc9M7ebynJgh92IhracgSr03s1HNo90tbJk6wsjn5GXs_IPAZOfyvKitY40vpFkHFU_6XcDsrtewaoMMnVWcWlM7mupmLx7Vc47nRxwD_OxM1QIuypdR_NE4rm1GAIAEm-oQSUAwgrqrtt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HdsFv8CcjWaM6jJKMJ7_mY_jOxr83ZuaSrDLisRtsMeOp_knjfr4lcUY9o6OerMYPF4LQYM2_n3PYbio8knEuAH6t9eHfqKsUakOPjGXwF6H6wBbDvpwM2cfZrR8bYYr8JMJTDISgcwY9sBOSmVVdpjfPSjjR6-HmrF-LItGDMsdykwo9VDKFXTKUwVQPEph4twBIGPzC3onknevG0jIvM9n8UZRiMze6uYYC07ibOcmsAg2cnvVPoV8foD5zaWpWgb9Diy0MZuGXps1gWwYZKL2eI3oYopDX2Z3PosiwlU1rin0pKCRYN-_0VneEG2C_PM11RJMfCtYS7co-fNa6nL9AbdDo8thH6YVr0y4Rrfg01aso08vkk7Sf8WzTKxrnYh4iqbVABADC4RBkvUc2tvb1m9HUE56CtTeLiJZ_sIqlODNfEllpotfcCo4Ea4uKKLmd5tc9C1fXjDPVdDqt2_Ftkn00Ar5I0qAL30gtrw83KFdN8pCKVDyE5byeDmagnCLLI5DtWOn-VCOPnnZAbS4x03Nc9M7ebynJgh92IhracgSr03s1HNo90tbJk6wsjn5GXs_IPAZOfyvKitY40vpFkHFU_6XcDsrtewaoMMnVWcWlM7mupmLx7Vc47nRxwD_OxM1QIuypdR_NE4rm1GAIAEm-oQSUAwgrqrtt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
