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
<img src="https://cdn4.telesco.pe/file/sL_NSTxe-nqPzoH7vLM9GBFP3DNwJI7KoGl4yCTNWeXLwJdku6FM4oq6C4mFUT44g5zwpcBXVzytTBBE3M6kwjgAjVETGfuHgoRnlul14PjYw2gaVtO0NlIGtsIlUIt1_P0DYnnczzRJSU3SXbQQauYil9hfHRqyVrdwwuIj2P4ynnqPRLwz7tjuZZSTJKC0Vn8zh6LEH84r0r-3jCnLmNzSwa6E6ig1yOOn8q6zFq7x6spK_N0kq5AsEojU00o8MKkSmPFKhoGL1nLH7ax4QNdODgkag31qoqVqwdGpKEMNsvkFJ5sw0rYwlXOuNiiPg1-4IvEauzO0YvjBZIMJeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 01:05:01</div>
<hr>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=K1B6laStYgUurA66nX1rcaxJWEvklWeyAxCfidkgomfsFPEvQEeOYCs7-XbObarLuWv8BiGdsuXkPg8oiSY82D3JY9JoHC8byeTnZzcPjckTpMGYrwDzGxb5qicLltzcErSkujkWJrZ_aK7lmahLJ2nm8gVJX_c5pVjg8zfxQnH4uq0hzDqFoD4AeVaPtFaHxyUFxJAGrxYq9uYloJ141Nqv8p9CKOLmIUPeqN3p2B899pulqeHjlNjF71nlIEYkJ2i_uYp1nwKR9cnOiTbERzdAySrQbHoUALVfdRVnmspfq_Eh32-AuARMNJ1jony-MbLXyUkfcTwzLlK9X0Em0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD3p8nGVBQZKWfT7-W-7YZkbhfFCftZ_3GX640oH_uNJMbZrKgoMMTL0lb8KexQfTLEd1RjPQKJ5LfAP1mzgrPEytBwMC03Xyg4staI8mi2WfeYFvm6lAFy866KngSRTDRxZ1OvLhHOA8S7RDop3sNu4B4z8WvEz_UBhmVEC_DM9PmI2byqJ9GxhREf_JMxDa5GNXS3-keCTcynFXDVNjbw2ISvE0kenlGVpZ4kkUFz750vodKpi73uUArPB3TOfKHyqhLoMNj6CiTtHNLeJT3uxO97Vjz184w6tf2XbLivCK83Ckr4Hno0uDkefnhwpPCvngykqDnH_gq-sAVHt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NslFIUbLzAd-u3LxjhpKY4PaK6e-vK3Aah1hhnPQjBEkpIuHuNIlJAKr5CI87gRDbCIuRupbie-cKK-LgpbY_yyiwhw4uAcc26-I7vhMtxyu0BpOLfmwbQE2O6g2r7tpDZBRB5_b5ngC5xrtYos9-9cDIwPcy2tNcBWqW91_ES3yFptpIGEc4vR4IKXRc9bQv76nGeEFp4dh5rxYVRNleSN6fh_MzNGwf63KW-CJT8qo0FdKs4Xe2clsy4wT_yguk-o2rWHcaL0tqfFhU42jKPcoyC8vEwsqAahqruSB6JEp7CQ930C4yh_fpkOqfYG9ZQojeq8D_PjzOITYtFEx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9OVLQHBYnck8r4an9MLPeSdj0_kEssPky4S7RrX6GQyQiAobeg-_wsLyBuo4Rw1mHS8hqSIo_y2TkNbB_0fDQJRolfGDvfqD7ZCNkTD1ORIAWndlalrOlM4m82X986ClzCLOkPLL4D1xGQGJtidh8n7tCzlYhAz-IlJ2QOLqW01IjqMTUSQcBMPV6h7slDaHcqDaqtme0CBh_vQHCNbSx8kd7XWdMp0k_tl1s50zt56K5b75bBnJXp4lET-iD6awfQPO2ouTCTIz8f7Hq_HWnN4HS5VxudNTDOUbJ_uiaXK2ofcrZeP0rQSoh6_Vj7Z0QhVTtggCy3k6ARn0cTZ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C15ggFdopgf9pTzFRWOymQyWTSgSNZAEsbCsy_QMcqf_DIH9A04ERL7e0NLkbicrAcPCn0k_DLTuzAhjbzFbFdqAF7EZqwPXXNVf9zRh9F-tHS4Dhywh4YNCsRYlIvaH91t-DRhPxsZreOJwcEysCn1hsTLXmlmscem7TLhuBPtHL79i2qFO07vB2wCnUjc-eLyhSiOL-egPMMSvmfXx7ktX4JtPHNRPmo-5OtX7NNAwUBRLc9mNSngJ1kBvFldwFfe437pZphruvHWDjTg42zY0QZw7LzepaddsVS_XM1BbVu91KuLMmeadSUJBc8amSx3XYQvO-J2SUy87gQamTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iF4SQPld7bXK8UA0a_6_tHSsrmH1Ez5D15HIPTK2e5aT1X5HSqfqbYppptLu0Hn1VDBz1CUvRaewA-nvcQqRUYMJneBYYl6MZDtriNbuaJIhDleDe27x7C6XbFHC54dWTYpnsWsSkle1h-pmHY4_JFX4jMcNgbo--narYXLJWxrjDVTJmmDo2ImSDLmYRsuIhCdfY-K7RqJ2PEVBA9V50YhJkQGrxiitigv-mlHCnQ5LrdJrwP4nSf553cnQBTS9o8FEwgUXNHr4GpSj6WKgaONmmbVEI9qEjl3a7Ppt8eJX3h-essUUxp6zENfVxsBh9yK8fRLN4mSnsVVk_rCMIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4WWlBDb9thHJOZ5rWxxAv5kVzhiUHylLLkgG40CFirbzXye2Kb1X9V20QK00aeTRjzLzPPo7Yy2qPkg_NyA_zbZAgE3mj34xN-5pJRKf16NErXIHR7YvmOKwTm-FDlQRQd3gmYZVho9Yl9AeDEa7aXiiZHddLyEqEJpljYq497-mpmF3TBPIBQ9DqWobA1bSyYPO71jvkY5FxcdqVsD0eYOqMIGohcrNOVmqrmbQ-PRGvIhbirKcS9UFuArjIeBWryqel6aCCT5007UcNvhu1CizsNrmW60-w1MD6_JzUxFxBw7LHne-KAR-EXbs5ijoUpiCWVMyW6JR2IBVyZZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaKYP1aUawcBCInMnKvoa_PjURtb3dVm6yWJIyRaC7OSkPXdE_7B9O7-CFAGJLeO4PqumA-htckyVa2IyMDSBe3e_sycikPCcWSxKizs4TPDdLNc2DQcm6_lxwI8wuY9s4isWKDOdHF5HoErQsSNEJfhfFJmLfVdG-J2fg9iKqY5vZW2wtsb5Ksjp4r6I5fLoegn8cNtpTSuXELkiJogSy1rWFYlJ2mvBLDi2rrB142Ri9stVJKhRVh6MhAfyafFyx2kdymSbfiMikOXBhLnXS6h65VN7ibLn40AyBXWLH74WRZbtA117DZxlZkvHtPHGhXP7fGXfVQ_8Kbr5pNNog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9p9BG8bpR0CUmtuaH10BFddMU7pNh1DjLruwzTG9QS_bWE-U4dfE_zuTo7SftH6QidddjRnZooA8q1jHhPBPEkX2fQUCg_q70GBGZqcB2gvINsTJoTmpnxqwBpWGIxx-ue3YaiWhCM9VCd4RfrGeQ0BDOIsXoeedS1xjWPqOAEU_msuFhkPPOUjrsq2Mf_7opAkUFgY1Z8Q7BHV9q46lXle-j58oU-zF6hZMqTQmEkhxpPdxSxvob-amo8NI7g_kuZVfxQTn9j1kRq57UVsdhOikQ0oHjH3dS69VflhysKK1w6CDey0CxAQeEMJ3MKeGmRsmUb6nDjy61eIKm1UxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=lXQfjfj1MRiC9MWQTStogYN6iC4D5WkceXuV_NwU-H7x4UelLhTfqYDyWaRWoT_aLF6zjyJdmm4dGsLwcIRGX8Ad7FKp6FgwiyQBbzNmDOqRfmxiIym9nw_XspJzKyxcnUt4FVWHVl3Pi8oXX-RtGyrxjl-n3d7DsA5YxrJVysQqgv7Tcje2-S3YEXG8Zg73sCT3g7LX15wp17yNi_ra9SViLPJFFF99iqSM4II5Jm94YvW9OVeXWwKVxsI_9GSUGOH5G8fajCxY2nQRsfGeI33WyUSGy3u9Gcw6VCTdCWNL4AKkB9n9qhklrt4jWqa4_myc45H36ufkdca9S4W4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=lXQfjfj1MRiC9MWQTStogYN6iC4D5WkceXuV_NwU-H7x4UelLhTfqYDyWaRWoT_aLF6zjyJdmm4dGsLwcIRGX8Ad7FKp6FgwiyQBbzNmDOqRfmxiIym9nw_XspJzKyxcnUt4FVWHVl3Pi8oXX-RtGyrxjl-n3d7DsA5YxrJVysQqgv7Tcje2-S3YEXG8Zg73sCT3g7LX15wp17yNi_ra9SViLPJFFF99iqSM4II5Jm94YvW9OVeXWwKVxsI_9GSUGOH5G8fajCxY2nQRsfGeI33WyUSGy3u9Gcw6VCTdCWNL4AKkB9n9qhklrt4jWqa4_myc45H36ufkdca9S4W4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip2NawMwbvMYrX9cUPixXCFNJnVf-KWY1kiaNmknoO_qFT6FUGENjIiWjnysrRMVqPFG0-6b8YV_G_jRpIlSpb5aXqED8QpWUbj8KJ_B9-7k2iEmd7GE0IkGjERlJj4597cH1dB4kPeQZVFO0JKZnXPJ-xfyeyXzN0Xa8hw5HzKWD1gLFSgMfc99iZFdB6uwdq2WUV-DJiZEnUOb_YJBijhwlq9MCZ7yzwTQ7GmtmWO-QgfHZq2XesL2DHiZrr0JsWpOutn3Emm5MDLibNcASS1cJSInLPF7xe_gRz5u_4k-tUauRT4Z-73fIibJSPJjdIxij7fvpUOPWfgbdl6Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqIJp_woOsptnyFAnNE0RgvmeKovw5m2BRfPi2F0IYxZYijXI9klbcsr03g7K0EyFXzt_1qGdlkq3LMEozI0mUhbneJmimoW3ECAjEh5cvBI7cMae5avNxgZfD8GGlfpWF-1BhsVfkKtrdFx2OvYZh9k85ZjoHmvDYb3OIiUpzW6p7MejYgbEOla0BNkkcGzdPCVboQZPyCRzc59Bjcb3ENCCBU3Xwio5UjEOvijdfsmuJRvl-Cj70myAFH56AQ5WYIaAg2M-u-wUNTkapMfmQcKrM9lTuuiTOYak5AIIWkvaP00IQ4Mfhs08Yq7v3Gi7Y--3SDY_qreV1bPYj7mCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6DFDY4DnEXw2ENI9M5kcVRlIAZl0HmA7NbtZ6V7_toGxYtrREpQFBp5HCiPulUn-HXk-DWEJS2vUzfK3-dQNWivbIdtCAnZVQ-Px5RmjEigZfayc9AWavTgDKs6B_odjhCc-hnfia60x3vb8E0o5Lrub_NN_xB9Mz2euRPygdK30kn0UZjMaRKa9QR8j6yFRyQQb-ml61waTFinlZa6J1ERfjgFgoL0kpk0gYqrd0-n9Ezg9rRGDkhRQirG6753MZB2Ssh-zq9cEI38aVf-Q6cFBEjgnurDPSddCILWEZoKCahk-IbZWrJv6pOf_SnfW4eY6DcxfnsvlK90pCFbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Detm03xkXslWRbewQOKuYszTURwsj-BIZTz0R7zdHbkHPsNxteo1NIRHykhgvSlTYFlCFq98tE9YlybVS8zYwpg1XNT0x1wMdE58L9hKPirPzM8us1f60V31yVRCjKeB2f7Xs3fe3iYSgc9KZ_Zxf-ZPepHLlgLgIL5nFv2Hu18u06sgtRkz9tLEaplMvlSEC3tbuACZbBbhhTY0d8EiJW7-xWDGsh0_t9yLWBCTD7MngFh5hsEQ6mpG6cOXSkhIqYTdaqUtZx3wAdMfzlAsT7I-vI8CBFW5MrGpBNtnbavaDN4gTG3WYtuRP6mbz_iK1Hwnb4e8RY_O5fwGJ9oLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Detm03xkXslWRbewQOKuYszTURwsj-BIZTz0R7zdHbkHPsNxteo1NIRHykhgvSlTYFlCFq98tE9YlybVS8zYwpg1XNT0x1wMdE58L9hKPirPzM8us1f60V31yVRCjKeB2f7Xs3fe3iYSgc9KZ_Zxf-ZPepHLlgLgIL5nFv2Hu18u06sgtRkz9tLEaplMvlSEC3tbuACZbBbhhTY0d8EiJW7-xWDGsh0_t9yLWBCTD7MngFh5hsEQ6mpG6cOXSkhIqYTdaqUtZx3wAdMfzlAsT7I-vI8CBFW5MrGpBNtnbavaDN4gTG3WYtuRP6mbz_iK1Hwnb4e8RY_O5fwGJ9oLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXRfOVxdKfF318xCnHU6FG8mDvyNZh6HuYs39hSihdXygbtIOirhzirpFUMXHfARyQAbuc2VRkPnOPWF5JAcCSBgHMauP1Fo9fztHRAF8GNpAjiMht-SHYaU9OYD8lL5QnXxSeuqjIfnkXYp9cfWC3mCE6vrMZvk9bYdKpahPcJHMbiH6nbqReGfPJMaytRv_bpbGgR867ROjdupFV461iBkoi38OGTN20JAGiC1v8sxQiEv3pj7Fh28pvT6UloRKjp89LO_4gGhiTWH1fZsQRtLH5hTABS2EViNqHI-BtavEboY5QqG5pSFO5xgUo_10tmqY3LG6g-7MVxWd2s4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=O7Vrb4pWm1LD8_IiarRNBwDXi0jSfinY-hbKJRmuyjpl9jgMW9hb6ltSPgskXmqYV3erFcU0I34L5GFyufe5fDrE2SUH64OBwDKrkA_pBVe1X6wAPhl-R22NSgeU1t-Hr2YwtSKNpe90JqfcRKF05cYeHBU2Lq44y9tWl1eqHztUC286wp_2mFSQNoFSnb1qJYFqIwkempRdBHKCmBwewX2drNZ7RNgEDcd1nNG3tmkmMxDS5hOyfUTHT9SYu0AUykAnSQc089Y1tWCSkLBMoGbJGY12mIB2TFIKu2jvior25t9xZiZB-OapPKmGKV7gHdg6s5TV4xvyBk0EDwj1Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=O7Vrb4pWm1LD8_IiarRNBwDXi0jSfinY-hbKJRmuyjpl9jgMW9hb6ltSPgskXmqYV3erFcU0I34L5GFyufe5fDrE2SUH64OBwDKrkA_pBVe1X6wAPhl-R22NSgeU1t-Hr2YwtSKNpe90JqfcRKF05cYeHBU2Lq44y9tWl1eqHztUC286wp_2mFSQNoFSnb1qJYFqIwkempRdBHKCmBwewX2drNZ7RNgEDcd1nNG3tmkmMxDS5hOyfUTHT9SYu0AUykAnSQc089Y1tWCSkLBMoGbJGY12mIB2TFIKu2jvior25t9xZiZB-OapPKmGKV7gHdg6s5TV4xvyBk0EDwj1Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQNC4ISUyCa4GU5z6yIrlROskuUDXW7riG0Gwhm_0bJMH0CR9R0Jm3o5El_BYJ4Y0Z4WP1jELhpPw-o8PUH1hNQ9E5anD0vGowr5BqezH-Db8LJZrtOos19pvcq8B9K1I_ft_XjgvpcGi7mQ72Q0IrwQvp79U1Je3oddpULOXUq2N0iZi4sqJXoe1YqCtxUXDMq5U-tiKOlE-_5-niClihVzB_TOaRSKYz0WxGl-PlYShq-pEDcDoj-oUmXL-S3O9eUr8d4CYr1-Ybufdv4rLR_8YiZn93l2ZLNPRwpVcgieR-0tjdYKPpjgOeojZKEa1IDpj0f5vtC08oPF2cMXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI2S2Jprx475fJMlcWGt1my7bRDJVoLTBe1ZVgt1CpFJ7HLvLWP2ZitewXTP8tGg5KrSd5tuXWM8MogrzoT_RJBhOzKCScGb9vd4LoADMOZsTS8SyAeppyVCtX5VfxAmn__VGq9-FFxzEJLavxxTmPasKQOAMa1JQJfoKbAMmU-Ik0Hzkvf4xR1mtEyfxbO7SUyTvdzZkc8cb65CVHERTWJmdM3PZ04l8olPKac0yuzcLHAC_3KLcd69U0LyAQpsyj2oYyguIzz0OY1t6E9fuenktCmq91e45kHJjkALtR6f3h4pJ_xu2ZAG5fnBDEFIOfWUuovZs0AUSXIesOzd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=X94W7t4YpmSWfeMCCMnVXzI77iR8o2JI9lRh_vT5zrYvF0QzIMLSBxQ_2p0_zQz7BZkmvvaqjcmDL-MZkNaY_BTY5XXKBmofXCatR0LkjW2de8SIfHvYd__EE2k38QYU2kWkT04T_z4VE1tjfTMhbvBCKWN9f5g24S4XjSNFo6Xy2kZcjNP8M0T_t7Tm3hRv-FYenevT5QmqlDr7rut3_hsCr1vPkUGGDErdX74PUo4ne025Kmu1RV44HJASKLlnb684JJ3dtT_-LrjkYIzp9CCFO0FZeMrdlyhtm8T1IWnLvzR3hDNyKmmB_0F--8F9OdQgQI1lvyIKAWSD6bTAYyybuCa7LhjebXB6bc-uDoQs72gXFSDlHhowKgbg97XPVpa8fwfddwFJwrBpeZ13DjmuZb9N_abQdo-eLCSGbbKlOTUJUrE-Yw_JHT1gt2xwKsbtVXeDTxmo_719tNuX_P5FfGxiKZQo16rCm12x_a7VnaMuFFYgnKEx2wNJ1hUctHctQQGoWyWZdXZoeji68PYIBtUYlE3U-RkrfU3NWx33Lw6DpyNObknAhf9EQhyaTZ2J5qzm1ZRJoCNtc5NIC41c9GKz5w933r8-zswVLzTmsmKTdhXOnxSabawh2Hgf2iYEQvz4Un5lsoUexldJvr8JC5Ngy0qu6FskH1R0O3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=X94W7t4YpmSWfeMCCMnVXzI77iR8o2JI9lRh_vT5zrYvF0QzIMLSBxQ_2p0_zQz7BZkmvvaqjcmDL-MZkNaY_BTY5XXKBmofXCatR0LkjW2de8SIfHvYd__EE2k38QYU2kWkT04T_z4VE1tjfTMhbvBCKWN9f5g24S4XjSNFo6Xy2kZcjNP8M0T_t7Tm3hRv-FYenevT5QmqlDr7rut3_hsCr1vPkUGGDErdX74PUo4ne025Kmu1RV44HJASKLlnb684JJ3dtT_-LrjkYIzp9CCFO0FZeMrdlyhtm8T1IWnLvzR3hDNyKmmB_0F--8F9OdQgQI1lvyIKAWSD6bTAYyybuCa7LhjebXB6bc-uDoQs72gXFSDlHhowKgbg97XPVpa8fwfddwFJwrBpeZ13DjmuZb9N_abQdo-eLCSGbbKlOTUJUrE-Yw_JHT1gt2xwKsbtVXeDTxmo_719tNuX_P5FfGxiKZQo16rCm12x_a7VnaMuFFYgnKEx2wNJ1hUctHctQQGoWyWZdXZoeji68PYIBtUYlE3U-RkrfU3NWx33Lw6DpyNObknAhf9EQhyaTZ2J5qzm1ZRJoCNtc5NIC41c9GKz5w933r8-zswVLzTmsmKTdhXOnxSabawh2Hgf2iYEQvz4Un5lsoUexldJvr8JC5Ngy0qu6FskH1R0O3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=FvQ3-WigqhE698EyJ1BzeviZ7rXBispLzD5U-L0vgRk2CsZObhX7nkBPGMODjoeSR70KuBMUo7qWJrnXqlKTbZ4ZOr6IEQk11JJE_gv4fGINKI9P3gElMGrF3-L9krd2xuZrGDPJO6FFSmFRG-gX9VtXOu4OdEDozn7mkSXjIMQG3XUtG3Dr3EQ_uG84jMZyBPoJcKOCyGdCgxOTw6BWpPqY6ctzpWU_K6PhAp6doNX5I5eBAeC__dUPRBpSgLYg8jTwEDWbHGOMOiFRhyhfGvmKioK3PVwyOd9TEq7DrbjXJcvHQhh7AKFVmfRU8hpXzb42h0lMkgPiFFsr8bN2aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=FvQ3-WigqhE698EyJ1BzeviZ7rXBispLzD5U-L0vgRk2CsZObhX7nkBPGMODjoeSR70KuBMUo7qWJrnXqlKTbZ4ZOr6IEQk11JJE_gv4fGINKI9P3gElMGrF3-L9krd2xuZrGDPJO6FFSmFRG-gX9VtXOu4OdEDozn7mkSXjIMQG3XUtG3Dr3EQ_uG84jMZyBPoJcKOCyGdCgxOTw6BWpPqY6ctzpWU_K6PhAp6doNX5I5eBAeC__dUPRBpSgLYg8jTwEDWbHGOMOiFRhyhfGvmKioK3PVwyOd9TEq7DrbjXJcvHQhh7AKFVmfRU8hpXzb42h0lMkgPiFFsr8bN2aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBosXQHe0-KJ7JZoYvqwMHARDNbfvOePpJYTck-lDJsjUbPnDV8Ik8pQg3NQv8DnYmYYZ9_I1EJAG3LaAmfqfGSyPORYjSD7gzq0F8lrKUffMC1T5gNuhxcHYvuINnHRpUkWjiPLSN2u7sh88eGmDwO4p6cW26lVJskDJXBYQ9AIISx-5fU_exWnZcTtALFS1vwhuAtZbwO6tYyEP9b2GHeCf_LlDyhH3yBghTKDGPaUM6C_-IK8ETGlkMKhLP1h_5AaV0WUPxcTywAfJ19xLPev1Tc_iqSEQ16BnvCctvND-QpXBRgJUqN0tk0RSvxSVDWcMooyZ0k2E0EFVA0EAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=llR2Es1UIRnnhjA77J3QfOQetsgFdqd9q3zvCzK76TlurJQFsDiAvDDALqFszOMRfELyc7pykTpivMWLmxuLzWddCWF6LxSuNz6gTSHciM4wWNOaLSil0fGla3PbSVtNraS35slQ1Ih_lVW9TS0EfBN9sUaYT-qLPskehetwqFzbpoOWU0hsMdaBfhT-lSRJRRT7SwB1iFpqVAPC4WXmrfi2nWK5_VQVDFJ3IPCARP-kH4kWELfKl7ivUBJt28fNK1b2Xo1Tk5SJ165rCbLxWZFRdk7f5lK7dollM0wR-kBHNLKwIexTZnAVouHJLFlau2Ohay1WpRBhaYEOLS_mUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=llR2Es1UIRnnhjA77J3QfOQetsgFdqd9q3zvCzK76TlurJQFsDiAvDDALqFszOMRfELyc7pykTpivMWLmxuLzWddCWF6LxSuNz6gTSHciM4wWNOaLSil0fGla3PbSVtNraS35slQ1Ih_lVW9TS0EfBN9sUaYT-qLPskehetwqFzbpoOWU0hsMdaBfhT-lSRJRRT7SwB1iFpqVAPC4WXmrfi2nWK5_VQVDFJ3IPCARP-kH4kWELfKl7ivUBJt28fNK1b2Xo1Tk5SJ165rCbLxWZFRdk7f5lK7dollM0wR-kBHNLKwIexTZnAVouHJLFlau2Ohay1WpRBhaYEOLS_mUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov42tmhCV-ifFf500Ai4lU3EFhJ6bNoNhrikiyWLLVRXkuA5Ixn4hrXZQEyTl9sP-zjd7ZXLo9LAEF02HZTuoXcfvu8DE07A3OmJWeUM7T4pPepcHCt6DzHC8jQJ3ZeML3EEKP1E90hbXjYuMl93jyax81IXz59rGY8ihSPg7myimFwYPI3JWzFsguq2UUtkY7qs3wYu3YeEHuwXm-81h0McALxv9FqqLciEZnw9eLhiQzFHwux2yo1ytPJJ2rRIvqMKvRw6DU9VXt1BGA3mBVFgsK3OKf7fWUztOsate2UT3gg9BWVUE6TSpBbSJcQntfwPoq3OkeSXtmCORXJKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-slX7yoP5izN-HYoxoVXidKJ2vRo4QlsD3G7C3gPwWqIruSIjGOc2B8FwTqig7E_JE7_vxDeNAeP_5z6niOX_RTJ3Rc-S_ZeKgZsiRWhOYucrIv-V_8zPcCrQsyezWwcOgbuTCT4_nlO20zU6wytse9U84mDW_bIT7tbFYvv1zoOqW2Kib8oivT2b1S4pZ1YBQNF6euUmIDaEcxk2sb28-eF8butSgdura55pWjMeIVn6_hWrVBuwVd2Wgtbjihu5KVdyfGS8PULvgXIAqSDrSu8uhH0H-513kMchk5RHP5Y5JqltjiqoUSkREF3hkzpDS-dOD41LV6uQl5GWZAaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB-mM1ZgfIgE0EBCX_3OhgGB21QKzSdCclrKOOZrQSXrnd5sLqHBkeacUpJGgJ9Sjf4e9tcoqmcl5NX3-mnUoMSrpS929dGU4lVTwh2IyxVmLeB6Hw5gnjIaUE1XiG8qo3awk-AxjxmWWoe_mLw-SpltJaOevuMqENmuuB-GHR2AyR_-lHoIsdI5UXIOAooOzFULf6cyFNlU51n0IqIhSCPo4LXKhvU7pRTUMuTGjvVixe9XxCR6emXaa4mU_26ND40fLAayKv_7I2qXFViqggxNa3ax5gUIboWcraESN_oOR_s5cy70G_1VpWjqPpe0GI_1e2Y0aXPvUFUtBQnPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGJyPqisR_WX8XXDQsTLDjYuO6hn0FyLYWjjUtW_YEt0eN-zQ5YhZKjJglq50H6Cg7sfsv4snYiZtKUmoHU_SFYrPlH-CGjwrvD5p13PM832kdCU7mCGukGaPtPBlGd25As75-5_tNb_0bi9K3qRSoVTGQOQP7YUMssUw7LyETquJfAbf5bzAr6UDZPwGkmi3gF1Q1epb9f-q_xbhdQlhtgt8BzTn92mbLGF4bI4nK5mXulfSsVOrosWlFr_PxsQW59NJ3eVERXugMrVyRKYndg2a0srXRLxurQIUtpCTX5Muflfu3vaYh3ucKwJT8ybDkSWwD9Jwj3cw7RalX4x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUn-1wQzgbPMOkbo84EdNVcfXVMX0FNs5V2pK-ksXMCMxLifQ0TzoZc1fm5yUYiVQHbzcHpC480juHOOCjPqdG5BacAbnEbMfWetD0buf1sUTyW6OD6Yr1OOqMBaPwg37EkW4T0HTUkopJgtFpT6a-NLC0T-3d4p4HAKZ3LHqnMbYU5ZDb-pdElTaIOO21eQJ5f9KFPmSvJyglJ5FTdD5bWEgs9YjHjKUyHiZNaQGG1-15ZvnV-_K0SpPTOh7IX7di-No3LF0wGyqwrQA02-YB1zMZaeRDYRuok44pyfuaAXRjgi1hUuQxy-kRNv0WSJrR676whlvDZfIkgi_z5rtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=MHoTj3NHB1VXC41yxDDtK0Hi50u3jXvd5ITFUPOCpye5Rel7fxI5c31p11bUdSsT5eBjmcNhDMyfNTO-MG0OZoKPM8K7q7XLFRchsXd5Hvx1CMHAbT_GmF6t8VgyM--iCLV8_zOwQ1XdzI_REW1b4tutQV342dY2IIP6_AEX02w0kQRJ35yLA063YR7AwGXjVuyppNT_b9WJuGjj8nd2KAS8-3o6KJ8gX4qINWAAIwAIAjWeQ5GGVXRK6HAr_zzmVYKuc_FLsVR6-D9Yvi3U7BYlDryouWc7sOPQQxDns0ZFFEiWB0Xqn-iYP3mCb4Q98pHXUe9Sg20w-oiJbSN4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=MHoTj3NHB1VXC41yxDDtK0Hi50u3jXvd5ITFUPOCpye5Rel7fxI5c31p11bUdSsT5eBjmcNhDMyfNTO-MG0OZoKPM8K7q7XLFRchsXd5Hvx1CMHAbT_GmF6t8VgyM--iCLV8_zOwQ1XdzI_REW1b4tutQV342dY2IIP6_AEX02w0kQRJ35yLA063YR7AwGXjVuyppNT_b9WJuGjj8nd2KAS8-3o6KJ8gX4qINWAAIwAIAjWeQ5GGVXRK6HAr_zzmVYKuc_FLsVR6-D9Yvi3U7BYlDryouWc7sOPQQxDns0ZFFEiWB0Xqn-iYP3mCb4Q98pHXUe9Sg20w-oiJbSN4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM7uwHwfY8X-57BB4sdXfGQVwqPWdUO-7pIqKbvf6nOxCi658NCr7AMQHqR6YwUU1vZDc7-6I6k9XhepZ1Ik1yrUoW5SMqXbulMT9sxAD3VC4kgkr_7s1l-AlSfQdnuEJOjn4DqMIRXf6Q19JdaZ8s-nL-LpC3Yl05AZMnrOhrFS0km-ua-hJwny7SRhuiQrGFx1HzKrQmFOCQeRsVSjWxu4FRiBv7PbGWu1euKGTPEx0YA5-rxN_scFZ49Mzvkb4Nz1THWri3-lYJVISG-fy9FknQXi4L8pjtXlDuiSVbEbQcwgctISDYcHKHsM3UcCMgXonQEJLJ4W_I-lVMmUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxWB5RSLxE56uRO7Ovxvmz0zrZ_N2C-hFsz6wxGr087yX9rZeHc0u81wTtUYppu8FoTs70Gp6lPcAOdaQvNfDhBhiGLFBLFiouq21EZCllkei8GubRvl5i0O2EWYoBV8Y8vccb3ov0ZrB5HGkAbM2RBpgFCsSAho9kKl6uU7npToD8LYRCZF9UZTvyGztDReYKZlhnQ1zTBqnPSAaIG5_FjZsJTQJWzZYycEOnkvvZHAB1v875ptFp6KwGXPo9wG9YU47-1UJZ0X71bzcPTMHAzbGUT3sFaQFxjuUu1-L4NqA_TNczgDfHIoaeR6pUtdFWpGV7PawA2x_Z1x8BYHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gAWVOvY2XaaRIUGmbBxL731-Bs3kAkMUues3jnLgik7dYHbYGToGcoDLCq8leUAOmHpWAngFNHdpn0rSCa1WSa8ZMwc2-ReMbhEc0dosIppuks0mzwUiNaBF5j8fJ8N9yQFWLcoUndanLVwQ7MvIM58oA8LjJjhNOJVOgRg9ZgX49TkeLSkpmxkeU8gpsMmcPsz2dVXdpRwFWumZ8Na6Ncl-p0FCXZwUJ1fqNT12hQuOmeSFbRMsTb7xOXNt0YMrN1R-kqaSkBdfQ-Gb8BhRhujUu7NW9lj46ftDi_V5J9yUMdfvCOyC37EE_LVLqN8Z1h6WnGPVatojq_YMvOt-wXUwUFbF4-UmSn_3Kme_CU_Wqs9gN_pUq8qA5Yp6HVVKzb3VmEDbmuNz3b6Owfi0gUof_Ne3zTRTbGGtbiNb8Ut0j_YdDOidMCCBjwSRzWUVuS5otLxP0mU5IYxaw_8O-00-_3chUtuw_fCjWzhhoUpF__6PDBuLcHlbzrvLDAD77PiftYCG8GXZAomCtIkIxVjh67PLPtaaidxIz2BC2DLhU2Asaux-T0Jxq503kObxogY4slBYFtNdujyYxB6294TRyNsCAfHmhmRYcyE1cOemQe2_-PDQT9ElZ_g5weFAEv0rM6Pxl4dBqpa_ktjyIZNyvWlUggdzUrmw3H9nM2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gAWVOvY2XaaRIUGmbBxL731-Bs3kAkMUues3jnLgik7dYHbYGToGcoDLCq8leUAOmHpWAngFNHdpn0rSCa1WSa8ZMwc2-ReMbhEc0dosIppuks0mzwUiNaBF5j8fJ8N9yQFWLcoUndanLVwQ7MvIM58oA8LjJjhNOJVOgRg9ZgX49TkeLSkpmxkeU8gpsMmcPsz2dVXdpRwFWumZ8Na6Ncl-p0FCXZwUJ1fqNT12hQuOmeSFbRMsTb7xOXNt0YMrN1R-kqaSkBdfQ-Gb8BhRhujUu7NW9lj46ftDi_V5J9yUMdfvCOyC37EE_LVLqN8Z1h6WnGPVatojq_YMvOt-wXUwUFbF4-UmSn_3Kme_CU_Wqs9gN_pUq8qA5Yp6HVVKzb3VmEDbmuNz3b6Owfi0gUof_Ne3zTRTbGGtbiNb8Ut0j_YdDOidMCCBjwSRzWUVuS5otLxP0mU5IYxaw_8O-00-_3chUtuw_fCjWzhhoUpF__6PDBuLcHlbzrvLDAD77PiftYCG8GXZAomCtIkIxVjh67PLPtaaidxIz2BC2DLhU2Asaux-T0Jxq503kObxogY4slBYFtNdujyYxB6294TRyNsCAfHmhmRYcyE1cOemQe2_-PDQT9ElZ_g5weFAEv0rM6Pxl4dBqpa_ktjyIZNyvWlUggdzUrmw3H9nM2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=jnbRj7NcB657HxABjBDMMK8rGAQlmKxX5shUfdawzhfUm0WeXUSlN97i7FD7M5FOweBE9Ki5q-5slmMYkNBZ8F7UQfQe4295NtbQAOBIhQY-CXsC5SZSDUECyKWMBjm1NQhJ_-pfLfQ1gKT5aCf8tZuPK5G-NW0FWoPiLGWyk91Xu8VhXUrKxvdfyMs90fk9P4DUIE0EM-HIsg3obM2jKsTQaY_GKMpwYUZzod3gl5ONwTPPto0iTsrGwTJIEHWWFg5ZflhsEYd7NjiHuoEH0Zpm8ESgllB9J38X-qtzK7diUUohLC7uT2v3lJyJcc9BYuldR1mh1mIlq7D5WCumfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=jnbRj7NcB657HxABjBDMMK8rGAQlmKxX5shUfdawzhfUm0WeXUSlN97i7FD7M5FOweBE9Ki5q-5slmMYkNBZ8F7UQfQe4295NtbQAOBIhQY-CXsC5SZSDUECyKWMBjm1NQhJ_-pfLfQ1gKT5aCf8tZuPK5G-NW0FWoPiLGWyk91Xu8VhXUrKxvdfyMs90fk9P4DUIE0EM-HIsg3obM2jKsTQaY_GKMpwYUZzod3gl5ONwTPPto0iTsrGwTJIEHWWFg5ZflhsEYd7NjiHuoEH0Zpm8ESgllB9J38X-qtzK7diUUohLC7uT2v3lJyJcc9BYuldR1mh1mIlq7D5WCumfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSpVKNdaZDDNsCbnZBh9lkPRcKSJq622qNxGlml0_CCQJOA_aa-HsTNbBDMhpJg-23h8tS2e5zO2R_J9tZwv_5h0lXAa1oNXd1TKOZpPbx_n-SSvhOtsohceoFmUT5A_q8_NKAbvSfG81ooZFnnFNSou06wWdYPiii09N2AygyK3dq_DeOtjY1CMw-yZajvV_9bUPPYNg-PEE3C0qrH_UhA_pNdZ5HRkuQQ9wq7khSJo3IKA8TJF_NsO9dbgYRby8nGXLySQJj79zZ87l0MnAmoPGMk5VVDnVw6yMA3HFF1MBjUlPl5yswUy5gi1C0ugpNWY2Scda1cx2fFvNvjdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNWyl3FfztpYGvo7iBWBJ1ln9g54Se9_42aCfoFY6tUI8j8bTJR-T7A_UU6Vn8qaHwnibTqigoVT_ZWtO7kiYQtYIyjVm3D5_gCtIOdQyaYu8w6-1uNNd49imMCPZlf9u7BSG7gcOmgLXDorieiWCVsxCHlFNWXSh7UuDZSTLnmjPPCp8VZ-1plGMElP1Iz3bqjMZwsOtexm5eNvJrbQGqwgc9w8OIDEWZxkJvkyuJXAqPzOZXR9u9tEM0xr98regD4p6gWsbv7q5yGMZI4_YbRUwkn-Eo1P2QUC65irKrGPMV9WMaPdh9wyjzzTacKwrcXI0x4W3mGxY9fQkpghFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpgaisX89SMWukby5SY8djooflQvf3Cq8Ozp-hVSMAfeNC9APf8Qu7heTB_uX-N0C91ExpZuPr2CHZlIBduKXfumqP242vwUR01A6O7yddGL4z4xsBTPiLxERznRKZ0U4SQpE4jKenY680luc5PSCSHyPp2BFcm-IFTFQBuTlJfDyG5a56wKYP1xT3j63shHR8xznHntR8Yd6aNRODza4Qw2jtksPXJ286CYPrcQ529ISIoGxYfZ5vZMm4B_eA3ONOEY-JLdyh_eT1vw8yVKR_S62G9VyC5XwbDg5Pa_L-dZr0qOC41AlZcNiCvGThwHnt-5JyOEv5QqwxgtCmqhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=m8Ry7Z7V5DLiQUIao_ZKhx9MCk3mhQJUq8LZ4VreEtqaHsinmiuiLVkJVY0YoZeypcy9HQMSN-KUVQ9ULqe5D6862r-k_vGRFrgHLir_LmO6Rbes3b3sF6d5HpWxJupUVF1v-I5IwUW5CzuRZP-NG7cbuPG1B6CYNmtbnmOd19EUS-mZJ4SZTHaDEW1bolsik0XWOtu7JmjxTU5q2mladQtVQGabwICbKNTqi_Hahmcr2o1bylRjNxGD_FFzhEIuPAHeZJ1PMPaxQqA0TOv7DFq0i6WnbbmE9-6h8dGAkFX3KrhuT7oPQ3RzFfwlUmz0CSIpD7KCghZHnQnDlGD91A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=m8Ry7Z7V5DLiQUIao_ZKhx9MCk3mhQJUq8LZ4VreEtqaHsinmiuiLVkJVY0YoZeypcy9HQMSN-KUVQ9ULqe5D6862r-k_vGRFrgHLir_LmO6Rbes3b3sF6d5HpWxJupUVF1v-I5IwUW5CzuRZP-NG7cbuPG1B6CYNmtbnmOd19EUS-mZJ4SZTHaDEW1bolsik0XWOtu7JmjxTU5q2mladQtVQGabwICbKNTqi_Hahmcr2o1bylRjNxGD_FFzhEIuPAHeZJ1PMPaxQqA0TOv7DFq0i6WnbbmE9-6h8dGAkFX3KrhuT7oPQ3RzFfwlUmz0CSIpD7KCghZHnQnDlGD91A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpYUG7rnoCKSkPFHVG6kE2rn_s_8EwpZ9H3z0jHsjuzGnY7bDoMU-F85uz4XwKboQPqMqyHTSESe8NRM7oWSDYTuc2kf9c__CgQon9x_steac_EgtoP9pjrG150RQ-cCv1K7FEhOXcTGkhdV8CgSYUUREhOYatjB6Bu6jv6oO0FjfI6xArZ5hOCKcLIFaNPWCzaheuPB39D5YJl07ggFQjbmZgEUdHChCzrKPdjHRKBrxtw3HDDczCuia2-mCj6Q8I1eYS5Cn4rfJ0kqvByJ8Yrm7AtqUd8sMDZ0emjkjlyM9p4uBnkO38ZT9-77uMMSVfPHpDCs_FBU8CvdKkgaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6wqaP0itc7VR3KPN1NbG00I62guInuYZzLFiYuPuC4EUPa0PxRmdWxH7Biy4ED1oGRTA8F7Ev1j4O4EtvKKVUtQk_94cFO9hJwuFnJGTPM-7WC7cGfBXTONiAuD6XV-8IIj1svLhIJY8j-eQmx-C_yr1rBl6ug_RyVOfalOh0txnDqg_oriLgKHCqMxg3RczRrxMhFzPE4xBTqyxjbAz_SAAo-d3utA94eWNXv0OXzI8rjuOUgA_gRePzJmcKyIjmQ28o3jN36hqcu6lwX9ts5NqK82akX--13W3FxiyjOBjGnoWwGJJEfF5EeGg_fvxeFXuhL-LCmfaTyTuDsx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJdQqer0jLs7PrQLBaZ5pgUBn53E-MYk71dDiKE3u1PIc4pTiREpdFibLpgx9g5DUunKnTita2zN-R3X0f71ug3yotVnU2HCFjF5F67qJrRXksKUTs9Ev3Ee7RMm4C7yrWIh_M474zYh-KUDX_dVhRhRzkBJF0q1wGKttBbUuoxOUh-E7tdBI0qYVHLnWJPQKnXGL5si2ULjFNKDsQ_ZW_Pax6tDDeIfpvEoCQXBC4dGtQGmGJ-1TSwDAosJe3vskNSvmtnmHvVkC7yh7w_zyEwxNS0tS7eov--pFjprF_2daXLRWuMibHQ9NFPEiHjAZgVleZV0kxLpI512FPvEBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNXaGz9HQmQbJGh3kisaJzWDjVL_J1cYAaPfDCea0Hlu1Ivu8ljPYaSerGIbd7vmwjp-k9S2luCDoWuEwUP52w5hPnWlBsWVrn23Fz4exTGDJ7eHbcSWR_aPfnirBQ5x5xINK-pB0JVXxDqr-0FApsH5-vYjUKbFgz1m3LHUZONwXEdYpa3LUvI-twqJlyy9YsgU4Cq_RlhyzxAERyWRfDEEc831Q82a4cJMC4sciTZHzg5cDlZMbQ5zn03VvSL8gnEAn4N-8p3dkXxaBROyPU1uGzFWXz8xBahowXaYgXgTDqB0UK7jB-H14tRsZ9pkbWXGIpSy4MPN9neKspnZMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=F7XfXGP5adwOTdN24aNaUcbokfdlaMJW_2yrImOQzg7grNZy5SzCu9jve9e72iYza5y--H75pNOJ8azITwFfbv0Of86IFgPi1MO7RyltBGgvtSykMi_GUhwL8JhYnlcahTWMGUdGjdRhcQpW89AtLqxsXrIrAPW3-UwWCkVby1xKlJPBKIfK7PhXhRWlzjTqsroiG97OF3f1lZLPVdVpMNtmMirVQOhQcBhv85-Mj9WSpynzip_gQdvC0BJF8-QoHf96cmP-kz3TFYK-W2YfuZ0uzagR7anICt4ZYWHbjDXCZkyqTI4Cgr8wwpVS9FhYghAhMngvYtZygu8ArgBKUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=F7XfXGP5adwOTdN24aNaUcbokfdlaMJW_2yrImOQzg7grNZy5SzCu9jve9e72iYza5y--H75pNOJ8azITwFfbv0Of86IFgPi1MO7RyltBGgvtSykMi_GUhwL8JhYnlcahTWMGUdGjdRhcQpW89AtLqxsXrIrAPW3-UwWCkVby1xKlJPBKIfK7PhXhRWlzjTqsroiG97OF3f1lZLPVdVpMNtmMirVQOhQcBhv85-Mj9WSpynzip_gQdvC0BJF8-QoHf96cmP-kz3TFYK-W2YfuZ0uzagR7anICt4ZYWHbjDXCZkyqTI4Cgr8wwpVS9FhYghAhMngvYtZygu8ArgBKUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=UJOk68OX-Iy_51jRm-fxvM9vycdFlYhM-pnAlTPMr0LAUfiSjZOdstA0M8wjd4QzhRr-2vb7TNVaMkByyG4J6NjSgeNX_6UVuOKpmP4Zri_XyVwwWvtAC7mGd-8-tdhMEq7VBuoYCnBw7H7L0LVdmmLeWWZ-2uaI9Acrc9u2cpfocANEkfzT8b_G0hiDbEi_9A5-HNtzvYyjNTtt3YnU-78-skE-h79Sm1JToZnw72kkFNbjR6qV9F3-G7i0FffF7jU3oNtADli3mxhnDQxIyGWB0dhEyVdUcrMSeGHer-2d9C84vFm8Ph1XTHbJgS2Idnx8m-V09iElJGpyruv2ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=UJOk68OX-Iy_51jRm-fxvM9vycdFlYhM-pnAlTPMr0LAUfiSjZOdstA0M8wjd4QzhRr-2vb7TNVaMkByyG4J6NjSgeNX_6UVuOKpmP4Zri_XyVwwWvtAC7mGd-8-tdhMEq7VBuoYCnBw7H7L0LVdmmLeWWZ-2uaI9Acrc9u2cpfocANEkfzT8b_G0hiDbEi_9A5-HNtzvYyjNTtt3YnU-78-skE-h79Sm1JToZnw72kkFNbjR6qV9F3-G7i0FffF7jU3oNtADli3mxhnDQxIyGWB0dhEyVdUcrMSeGHer-2d9C84vFm8Ph1XTHbJgS2Idnx8m-V09iElJGpyruv2ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qo0oP9g0dWajXrR7iAAIf5GJCv63YDIDA2sfGCyTa2yMdD81e1A76idqaVYDveEr9cCZtUW_fRcJLJv_diWBGHeUKJ8yCad8ERshjCKb1aZB7Hf8QMOFOb0jRQBXVHrMa2yS5Z325XcvDUJPYi2c7dsNc6AmyzYFVCKREn9cnC7dy-UwVg2cwlZgWrYStD68gXYg4ssCD_IbH3YJAjOnNSE1KghMKu4USyCfqw9k9EWmwwJ4Zjavwh2DTYFyPZFE7BWyK6UhAuexVpc4_yKpRdYu_yc8D2KMIQlYtzZfhZp3CE2BQ_1vpFYeA4kYxjkmRSszpyNqbBG3ICpE2XpyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qo0oP9g0dWajXrR7iAAIf5GJCv63YDIDA2sfGCyTa2yMdD81e1A76idqaVYDveEr9cCZtUW_fRcJLJv_diWBGHeUKJ8yCad8ERshjCKb1aZB7Hf8QMOFOb0jRQBXVHrMa2yS5Z325XcvDUJPYi2c7dsNc6AmyzYFVCKREn9cnC7dy-UwVg2cwlZgWrYStD68gXYg4ssCD_IbH3YJAjOnNSE1KghMKu4USyCfqw9k9EWmwwJ4Zjavwh2DTYFyPZFE7BWyK6UhAuexVpc4_yKpRdYu_yc8D2KMIQlYtzZfhZp3CE2BQ_1vpFYeA4kYxjkmRSszpyNqbBG3ICpE2XpyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAUUHt4UgzJJ1oIJhJr9z8JhTN87nT04L62pE944n4DExw1Ghh1xpqJW2UeQR-BaWYv7W1wIG5DrGJwkgp5gqHoGXTrBgKYnVh6_feubfoEhpItRDtqFTFQgXL86q7o1YyGUUXFHNUvKew_h4TA8c5Bo2Aw37qjIzuRkKjNkMl8diNRcFvnlKsqlPL3g_-R3Uxsd4bTueUTDEwe1XmqE_HDm5P4QuL7fx6Z5ZxW1EXsUkwXU-dZH5town0yA8jkHMahMeynhuw7XoPDtyYqYkxDBcNnKAirgocyeN1NwjOSPjcDJLWWoef886UzPxkkRJBycxM_kHzXFkBoRn4BnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=pIHzSvkZgy0K6FgCUJoaD5FP5rN2L9CzWgpvr9Oc1q7xTtEAHq1gkl6ghPpkLU1U97i3QFM76rhjaKqT1zPfYeTH_KDPPJ5gDEMTeGxa6KfRpV9qeQH8N9zl86DFctgqecGsUQQ4lDWMVWXCwRnPd9fD07IAG-cYmRx6pctjTKvSqMGAIqXu0jHnCXELUtVNdaU88zPstVwHybZ_A68yN6_ZmzsB5Jdy8XVGqD78FGP2iw5fK37jspojuV7xfkLpfmiUYnX3s45tZQLsXou4eIVFpig2HDQNYGUiw09_5GG_zCzspDlPQ5vwmWB8bhL1BmMoROs9Q1iTT6SX7G9YqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=pIHzSvkZgy0K6FgCUJoaD5FP5rN2L9CzWgpvr9Oc1q7xTtEAHq1gkl6ghPpkLU1U97i3QFM76rhjaKqT1zPfYeTH_KDPPJ5gDEMTeGxa6KfRpV9qeQH8N9zl86DFctgqecGsUQQ4lDWMVWXCwRnPd9fD07IAG-cYmRx6pctjTKvSqMGAIqXu0jHnCXELUtVNdaU88zPstVwHybZ_A68yN6_ZmzsB5Jdy8XVGqD78FGP2iw5fK37jspojuV7xfkLpfmiUYnX3s45tZQLsXou4eIVFpig2HDQNYGUiw09_5GG_zCzspDlPQ5vwmWB8bhL1BmMoROs9Q1iTT6SX7G9YqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=OgPD4KgV0xMtmFbjr77OX1Yvbk9nDugowYQpiPIHRM9vELz9f3kc8SUerlsLNyiFKovYsnUE1YZN-fBcPRYlKJpju9GxVtAVK6sQKEF5HCBDUA9phfXvsrUK03ovVmoxv6S7NbZKQoocWwDn2qIc_sxuacKrLvO34qK25AyfwA5Yq0468mRLBvL1uhgHoHjo638WM9lyUVfeo-LD_-HTAvVWhYrqUdXfB9nj9RP91X-TlXG5FwldQRYfX1CZIzznYXDZC65A8ChurUF0QLhAQost1MaOelxIeel1ovBVVf0pwv4i17UzN1YSZZ84VH08MHoF5h9ppTvTdpf3bdpXMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=OgPD4KgV0xMtmFbjr77OX1Yvbk9nDugowYQpiPIHRM9vELz9f3kc8SUerlsLNyiFKovYsnUE1YZN-fBcPRYlKJpju9GxVtAVK6sQKEF5HCBDUA9phfXvsrUK03ovVmoxv6S7NbZKQoocWwDn2qIc_sxuacKrLvO34qK25AyfwA5Yq0468mRLBvL1uhgHoHjo638WM9lyUVfeo-LD_-HTAvVWhYrqUdXfB9nj9RP91X-TlXG5FwldQRYfX1CZIzznYXDZC65A8ChurUF0QLhAQost1MaOelxIeel1ovBVVf0pwv4i17UzN1YSZZ84VH08MHoF5h9ppTvTdpf3bdpXMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=kIsWfaTrdmPcdotnqu5I-O8BaTpH3w4_1odyceYfW_7AlNl2_08pfvA0CQkEsZXfQRYfadL8TS9TS5ZIVpa8Nr1td8NmuOkQjNadJ8BjXKZWE_b9fDlxk9YICFpLM3HqylzayRQyoUfSfqaAUSW5rabO9wg_WxXTB5GHd4DOUrI-JH7cYylOXr8B6efxWtnt2SdFx_gGmCXq2R4-eTSU9DS3H3oT8n7th0vDYBZjXPze4e1CwpjDDZPORyMlFaZLaVQxH1eAqYa610SYzoly49NnOqVbc5fNz-GxAe0Rqxadk_1w4kZ80GQQIH_nHGlidbcREBK_QWOlc-RULZidjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=kIsWfaTrdmPcdotnqu5I-O8BaTpH3w4_1odyceYfW_7AlNl2_08pfvA0CQkEsZXfQRYfadL8TS9TS5ZIVpa8Nr1td8NmuOkQjNadJ8BjXKZWE_b9fDlxk9YICFpLM3HqylzayRQyoUfSfqaAUSW5rabO9wg_WxXTB5GHd4DOUrI-JH7cYylOXr8B6efxWtnt2SdFx_gGmCXq2R4-eTSU9DS3H3oT8n7th0vDYBZjXPze4e1CwpjDDZPORyMlFaZLaVQxH1eAqYa610SYzoly49NnOqVbc5fNz-GxAe0Rqxadk_1w4kZ80GQQIH_nHGlidbcREBK_QWOlc-RULZidjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=bOqixfJNXfwNspP02Eh9pFD7w_bucihbwfpOAOih4J9N3LBtbeOmWVuX8-H1uiPoFLpCTVGCv8OKbRfrCqv4BFWXWcy_t4SNsZ1gy1JmCJT7rUWOfuhNBZUauyJkEaxvrYK_f-h5k6wWFrKjtGaql9Mjji6Uhhqa-_ck2YhAzlA3V_xNvf761iSd9Jjnmb6Ip0FCD10ogmInirbjre90ce4iBfM8GJHc1Evq7oxeIAssT1Rr9ZmG6d5cGbNUJTvwo2taA8mgDuaNAm3aBpfH62Wh-T8D_gf1ylEvAzMXFma__Hv2cRk3oS28asg-rKeZ-2CU-lrqAa6a9LH5gwK03UEEb0NrgiycoiCfIAMLilEOa8GUaydHEjngIgJQ1DcvvOzeCEVwAx80aICRPKH1Qnpo5e0boFD-gwEv8VbTzWVY8RxkQYyb8VBe62mj_HN33F8d-xyf85E3LMIKYNXtpjx8CKvYPI37C_zFGjuA4_2dJb_u66qV3TeVUDsBd9KGDQm7meuzR7J-Z95jJHBagyeksVeAp32QFD1LxKxUzxAqYBOdWAhR5W-40yOnzOpps7Zb6deyq3EO6k-fwiRoXeQT_yFJZDaI8GJGtjlE9W-osxO6-Kvualb3_x-vvHW9905m52-zPIH_ZgBPmqaglWuRYwj43ruEFa9t0eJg8yI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=bOqixfJNXfwNspP02Eh9pFD7w_bucihbwfpOAOih4J9N3LBtbeOmWVuX8-H1uiPoFLpCTVGCv8OKbRfrCqv4BFWXWcy_t4SNsZ1gy1JmCJT7rUWOfuhNBZUauyJkEaxvrYK_f-h5k6wWFrKjtGaql9Mjji6Uhhqa-_ck2YhAzlA3V_xNvf761iSd9Jjnmb6Ip0FCD10ogmInirbjre90ce4iBfM8GJHc1Evq7oxeIAssT1Rr9ZmG6d5cGbNUJTvwo2taA8mgDuaNAm3aBpfH62Wh-T8D_gf1ylEvAzMXFma__Hv2cRk3oS28asg-rKeZ-2CU-lrqAa6a9LH5gwK03UEEb0NrgiycoiCfIAMLilEOa8GUaydHEjngIgJQ1DcvvOzeCEVwAx80aICRPKH1Qnpo5e0boFD-gwEv8VbTzWVY8RxkQYyb8VBe62mj_HN33F8d-xyf85E3LMIKYNXtpjx8CKvYPI37C_zFGjuA4_2dJb_u66qV3TeVUDsBd9KGDQm7meuzR7J-Z95jJHBagyeksVeAp32QFD1LxKxUzxAqYBOdWAhR5W-40yOnzOpps7Zb6deyq3EO6k-fwiRoXeQT_yFJZDaI8GJGtjlE9W-osxO6-Kvualb3_x-vvHW9905m52-zPIH_ZgBPmqaglWuRYwj43ruEFa9t0eJg8yI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Z98XEjFJMsBXyXqf3OJRu2VsDgsT0vO5GIAbOgZtTl4FkEzYwcQ3Upst1RrK56sLWvnTLDnrF_3AlniyTd8AIQgpnEtfFRc2zaF3C4sJdXd1motH4-Yd1azUUA87Bkpxf8koHH0ognIuNeJ3aFD8KImDXSHzX_Vhoo0Ty8WZj8Dgi87NbRMHmBLLgAevAvHBedmGbTOUlHN3Hmh7BoTOm5ygfVRfa6Vr0KlDW4wxjDfrC9aCDUbw_GeqU4QVGy2DgWyM30DGqoku8KGe-gr0BBBlg0Pr3EezLzSaDb8OBu1GDdz7rNS1pFe2OqUJoVpddqwU-0we9fou71ADSyl2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Z98XEjFJMsBXyXqf3OJRu2VsDgsT0vO5GIAbOgZtTl4FkEzYwcQ3Upst1RrK56sLWvnTLDnrF_3AlniyTd8AIQgpnEtfFRc2zaF3C4sJdXd1motH4-Yd1azUUA87Bkpxf8koHH0ognIuNeJ3aFD8KImDXSHzX_Vhoo0Ty8WZj8Dgi87NbRMHmBLLgAevAvHBedmGbTOUlHN3Hmh7BoTOm5ygfVRfa6Vr0KlDW4wxjDfrC9aCDUbw_GeqU4QVGy2DgWyM30DGqoku8KGe-gr0BBBlg0Pr3EezLzSaDb8OBu1GDdz7rNS1pFe2OqUJoVpddqwU-0we9fou71ADSyl2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNeFDjZVt7u2pg-nVwApb4lnoGT6o3EjsVIsNwSIAWbeXTziLj4Zn2IlA3ZXx9LUdaXTQKthPlYNOLEnYgUoQSLpkiTEy9fjMdPTvphaci7I3l2dG_p06ibhx3KvYi4lK_ozadnTIgBFOtLmC-voA2mwe3aPeQlmNi5a60djsGLX4TPpSujj9vIwQKJr-QiU0Z1jInLhlUH4YTKjJYxkj_0-vRWLv---2oPTL8yAeo_d7ftYAFv9lIvb3U-8FHlvhReoFu1Zik3i0gotzgU75vHb8V9woNBfdNATfleM4LC-h5Uo6ag3plMSusPn52kUrpZcu-8DFBX9uRX8HJ_xuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV4EQMBTdFBG1CizKEjAbf6Bg4qIYh5xBB5phmlDHNBDQn17YYibOHYqc7_wWXhd2zFR0QQjDsiXDXug1D4fTJda-rTAnfeTfWpQE5mXm6-p-cFgeo8Gr_JK9jCROa-6pI6ItFmb5lX7e-wIJ3nK3sBUEMMJh57dsM4rDOi-svhpTO5dNzjFiTshRcq6OKmjibEe_E1RUvv1E8DFY4Zd66FDKvZeFGl_hzdgY8_bdngkVTVDbNl2fj0n_YPW-E0L8GX1qlAf639P2sAagG6Krkj6zcXajBahH6x-3r_QmBoFnrbaDtAnHTzKNeDepXyIEOOwmAIQcGfMQgXMIKg3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=r7V9Yt0C1kWLOf_i33DEKkWDHufcs-KJ2oGEhVkEYkizywh96V82un4swTnBYDmsLsAh1cipjzLWaO1vappZyS0EStV2bqU1iEPbwlwQ2-XSYNKTIpPPpupNmXkSFpwbhvsNLPOrtNFLs2Vep_jQ0qrHMDsGIgPa9Z3FZFwid7QHg1hxLfgz5YRixtBvO4jVFnfW9RWnyvNjHrMjHEt6qfoiTKpqFzFqn15iwtjWyDdvDAMOPXrrBzsQVC6Pj4AYvm7BR7wDr-Aj9NxRpcLWDGXRoOmmdCKG3APhgY_o3HDvBslldkgkTQ4SmdJcuIP-p7IFGOA_1ntGRv3MhSkIN75KTnNRC9GKIe_wImXUqWua3AxKphvccoFVsKg7wSZ7lue9vN98TwdtZ5eOZubrswV-S7Afmbyzp1JZC_1INcKgqa_fDVZBaLZvvDfd3ciQNaA16VVjn7jNRAvKL5Ik9iM01eX7fR9AwLcOUANmfvjyrv0SQmXtArrusCTSj0q8lRoNrReu3NAtwYoxWAQtE2OPUJ0iW87hlMal9rGZ8dkUg2xCvEFECPzAQWNaoNA-Q7U-c7BartnUoKGIWv9s-MiU7JS-2jykNYho5a-4zBktHm2CWUaW0yDPG4VoWgw-Og-LILiyljddTlXXl2VpitsdXmyxj8nYuu15ddAZO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=r7V9Yt0C1kWLOf_i33DEKkWDHufcs-KJ2oGEhVkEYkizywh96V82un4swTnBYDmsLsAh1cipjzLWaO1vappZyS0EStV2bqU1iEPbwlwQ2-XSYNKTIpPPpupNmXkSFpwbhvsNLPOrtNFLs2Vep_jQ0qrHMDsGIgPa9Z3FZFwid7QHg1hxLfgz5YRixtBvO4jVFnfW9RWnyvNjHrMjHEt6qfoiTKpqFzFqn15iwtjWyDdvDAMOPXrrBzsQVC6Pj4AYvm7BR7wDr-Aj9NxRpcLWDGXRoOmmdCKG3APhgY_o3HDvBslldkgkTQ4SmdJcuIP-p7IFGOA_1ntGRv3MhSkIN75KTnNRC9GKIe_wImXUqWua3AxKphvccoFVsKg7wSZ7lue9vN98TwdtZ5eOZubrswV-S7Afmbyzp1JZC_1INcKgqa_fDVZBaLZvvDfd3ciQNaA16VVjn7jNRAvKL5Ik9iM01eX7fR9AwLcOUANmfvjyrv0SQmXtArrusCTSj0q8lRoNrReu3NAtwYoxWAQtE2OPUJ0iW87hlMal9rGZ8dkUg2xCvEFECPzAQWNaoNA-Q7U-c7BartnUoKGIWv9s-MiU7JS-2jykNYho5a-4zBktHm2CWUaW0yDPG4VoWgw-Og-LILiyljddTlXXl2VpitsdXmyxj8nYuu15ddAZO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8HNUf5RYg4teVNd7rsITzFt2fdQbvaZduF4dy_B048RcB_FeqnAQIugL3Hjm0PJuNB5mASLDfCxxvH0h--YvX3m_uVki_j6uxxPwDMELB4vM5C01KtRpZvUkhv7Q7ZUWhv888Geq2sdaQwqGbTDbiMOpxSwwhpKo3rA9KiLXrad2ilVn4wWEiK65o1V7zgD84ITMpwQoyjgiQ8NTPMR7MQckIfYJLyWduyP7CEhpT-bhYuLhdgLt30JUDo46DPljr_G0WuXkNQ023Rao25rlC2yy0LhVWt-VpfjKXVjucvcoGTOxE-X1IlRZgtYzwKyFcXyKAFR7iQUD66X7IZIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWVgRlodmno8HRhipyJK0ezfzvG3UFcl_W_KVOoKyMF9ZiXiBRFLL8xRrdcOMTM78joTbHfHalSCxQ6gSorwoWHYzm64W5OEjF5RJXbl-pkW5BiLkLgx7DTMY2mBNZA3ZFwL0wfxpEbo9L3_g8BatS7e_eq-X_zZHIJ18GwmX1jjvijgRTudr0rX56VLJZxigSdvxc59DfWvtE8Cnoy199QNU1jkLdxdvz0vCG__UI6kTBcSPobqDrTeKrQPJU9EPS_4m7ZxcLQmlPZYK5txga7qkPHRCYAiIQj6ozy05fJVAI0Kjw0XYBZIU-QrMeGLixBKhDsb9ojKtsQ9czvMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhbAhFzNaF6a826_2qCEYaOIXbZQMLR3RxVqheiEjlLfWt3N5As24dBvz-spL9-lhjHH0gibuVpxCQm7F2A20T0W8bMbWPesuvR4c3WgVguFLFuXCZwDEm5Fl1r1z43P87LK4T31XiFG_Nap6bBoURyFnFnCX0WoWURu7WMubsndrt2gv3xYgaLvE9g69l370qYbGvRITWweDOezmqyrndBcvW2WWB5c4xQGpf4iEGaVbH39_jvuPyJU8ArIk_Yw7CEFzc5CZuFDqHXiFQ5cKu9mZ3HR92t00epgh7mXB9d5hsG5MR_qCbSkf5FjMO_h6AIpTDBaE_CIOsC09yvp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZNPGaGhTxW-QPfdgKrvG4lwcl_eZ0R7nPbegPdWi1nJBTuCnDvDl4m1RVHBlfVoH4nrk9vDEgH58USL1c7QpNBaetkYWsxueBHgren4hL1rdhTtSIkwoIM1kDB8U7rVLMB2CJToYy7mHsC6b50LFi0dZpjk54QX5mdjZIdeSUxkXbitOZ5L6RCPsfCEadzixttFMO7YPaKO_AKa5YXIOqxYKdkXP2c1-feewkehiD0XquKP2RKy5BX35aXVTNp9lTGc2s5O02v1MWyyj2NaG9chYuGe6rzi0oESNboGTyO0mZUSGoYd7L-ktbvwm3NsnNqs27uJMuMLSjejh9IP4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=FDIdi5OKGZ82obGne3UHiJkYleJt6Nsk4Pf7fTs39GXnV-ZVAmIoWp7LuEsYI2cYWQpSvpGHgT9ERlHK8rFPGdFWGM-2EODNmJ8JWQrtgz69LSH1091CdIzWQ5uyHtYJk27q3iYtVIXNa3Fr1H5G6cvk1cWe455M-OT-wYd1jL9z_Lio7woUrOLaRnh2-8DTXlVJUnepl0PRMB8pq5cR3zPmS2z3stOb-A9Q6JvwModDavkpAHaamU8WYvdjCvkTcG8oMvxK0koANLmNuAJWZcZ4KrNpVUFm3gU0VtduGZQ_gt4jrcpxBhvXvRipvXiwwCcGADvaMW2tLU4NX_JVzKG7CsBgmMc0D7qHOPdWZuyp96y364vmT0W2wLRMJlAt4zOp71gY2z7P39M0fwfi3OMv_5427zYvGECVvNoyW5HO7hb3Lb5FLuRXfATTHJfHRgzD595N8lCQ0TXdY0bQqLTr9frs5ebUVUpCc2dVSYj7Hju0qvZMxDLPOjBrZKp0QQDi5bCuXkvRVmmr46_mOLMpbNuY_xqbsqz_fVXaxN00VaCB8p6VpsPrKzKKliMng6cmlxJjGP-yDJlqRZlst2lc3nYhnQO0135dNH6GOkqe0UqQN89qVUzKS_4roVAjKPrEfCgM_JDD_yl7Ls4Q4ZN90jcVYo6VB-R-7iqfyY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=FDIdi5OKGZ82obGne3UHiJkYleJt6Nsk4Pf7fTs39GXnV-ZVAmIoWp7LuEsYI2cYWQpSvpGHgT9ERlHK8rFPGdFWGM-2EODNmJ8JWQrtgz69LSH1091CdIzWQ5uyHtYJk27q3iYtVIXNa3Fr1H5G6cvk1cWe455M-OT-wYd1jL9z_Lio7woUrOLaRnh2-8DTXlVJUnepl0PRMB8pq5cR3zPmS2z3stOb-A9Q6JvwModDavkpAHaamU8WYvdjCvkTcG8oMvxK0koANLmNuAJWZcZ4KrNpVUFm3gU0VtduGZQ_gt4jrcpxBhvXvRipvXiwwCcGADvaMW2tLU4NX_JVzKG7CsBgmMc0D7qHOPdWZuyp96y364vmT0W2wLRMJlAt4zOp71gY2z7P39M0fwfi3OMv_5427zYvGECVvNoyW5HO7hb3Lb5FLuRXfATTHJfHRgzD595N8lCQ0TXdY0bQqLTr9frs5ebUVUpCc2dVSYj7Hju0qvZMxDLPOjBrZKp0QQDi5bCuXkvRVmmr46_mOLMpbNuY_xqbsqz_fVXaxN00VaCB8p6VpsPrKzKKliMng6cmlxJjGP-yDJlqRZlst2lc3nYhnQO0135dNH6GOkqe0UqQN89qVUzKS_4roVAjKPrEfCgM_JDD_yl7Ls4Q4ZN90jcVYo6VB-R-7iqfyY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
