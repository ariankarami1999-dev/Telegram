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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 02:23:05</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BibzHv2igOFaxVYk-us7sv0gDzzbjC76V8wXDfiwCcbuRxx_WifS1v6vcqrpxYayXwU2PAJ8Z9hhXBfUW_WaiXrGeW2A7mGqway0pW4psG2sLIlBjFrREuVTqAjSh09dz00SN36y3MEJ2qv1iCr4fOprtaMJVl4F1G8k05ov9x03Lo3i-lXvowt5WRJ3nPGeKSpUwGp_NmtunAZLqVgVWr8JX0JQO7BMM7hSc62-qJbS6czRvkqx4ueHqY1dzuQHzxmXCWwTQOZLCXJmdriPXoXnN3HFiVqxqc8raJT8Ds1srGCxQ9cXIZ_NYTHHCMD2IgF-ECx-FmfN3yj1QguYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=HgDkSvZWaY0XWwY1PU4zrfVc8vOyLrpaE-AVIjnLkDH0SyUBonE3WksqWQl9y94kz-D_oGRen7GZUye8XekBvJhTnk2nUbZWOASlYU0CTGA_KSUnDA58eKQXMF9OcAShHlrsIgwA8VplMdrClmdobF89eGOucA_ZFzMan_vtb5adeO5Hkl2eZ2w-0uHVFe0emSHN10Teb-tD4X_9daTGQmOFTbFZuegpj4w1SIOedbjBYoDUGarrsiID2KZj_zzDx3MzWCOo7bwbdYKLpBQTjNk13nrNprsQo847Im6TZeejNEuT9YuMaijP2d2kLn20uudehIwwoBaMlVehYFAKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=HgDkSvZWaY0XWwY1PU4zrfVc8vOyLrpaE-AVIjnLkDH0SyUBonE3WksqWQl9y94kz-D_oGRen7GZUye8XekBvJhTnk2nUbZWOASlYU0CTGA_KSUnDA58eKQXMF9OcAShHlrsIgwA8VplMdrClmdobF89eGOucA_ZFzMan_vtb5adeO5Hkl2eZ2w-0uHVFe0emSHN10Teb-tD4X_9daTGQmOFTbFZuegpj4w1SIOedbjBYoDUGarrsiID2KZj_zzDx3MzWCOo7bwbdYKLpBQTjNk13nrNprsQo847Im6TZeejNEuT9YuMaijP2d2kLn20uudehIwwoBaMlVehYFAKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip2NawMwbvMYrX9cUPixXCFNJnVf-KWY1kiaNmknoO_qFT6FUGENjIiWjnysrRMVqPFG0-6b8YV_G_jRpIlSpb5aXqED8QpWUbj8KJ_B9-7k2iEmd7GE0IkGjERlJj4597cH1dB4kPeQZVFO0JKZnXPJ-xfyeyXzN0Xa8hw5HzKWD1gLFSgMfc99iZFdB6uwdq2WUV-DJiZEnUOb_YJBijhwlq9MCZ7yzwTQ7GmtmWO-QgfHZq2XesL2DHiZrr0JsWpOutn3Emm5MDLibNcASS1cJSInLPF7xe_gRz5u_4k-tUauRT4Z-73fIibJSPJjdIxij7fvpUOPWfgbdl6Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTNMsdPDcbUHa9IfnJM41v4GfodmobirC5pEFdus59kaczyea4clSty1Q9rFehaEh7_KihzRGFdekhZulJYj_GtCKw02UnuPaj-y2G4zB5pOaia9SiBrDR4lCPjaVY1GhQ0m2FEFMbU8jZTbLwPrA_A_KE9Bt4819EnNvzGVszJBLjQhMi7htnIV0-_sL1GkRbeR9mN1FwswMPgSEIvd2-AkLl7MbulBfhWmrmUXxpJMXAT7OKfmrCXbOJWUP7UrMARPOa1oY3A6itfj7ur2sXGpknU7AYF-ZAzDF36AhlDXJUdPgk1jKhDa8rb2c04Jn5JKTRvnHLc_JjMqK7m78g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=V2zzjfFkyu-y5ZG1nsSE6-3WAyteFsIIcmIjHy3HN9-IhV4qkSS8Ej2QbZdbe7LXJIN3ByYks0hW8GlYkiF6TfLmaFqgT2xFAi0puoe69uXhEUp2pbgyrPIAN_06a-f446uAp19_amdig4jk5PoEGRZx-uHcLE95Tk3ZAZUUmOFu1e4429V9AYGRZBDz5YUfHCrRDBy1DMkj1iSf5m2H1RqEhRwDvIXYaMKbvonn6ombZgWg-iJ04mq_gzhGPq4hGpHZJfotDqUB4Y1M9RvlAYVP8MQ--7fCTQpnYE24qFUcaBMjtmAunNNQWaAGfab3tik6Mw5uOtMB0fFm_OvxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=V2zzjfFkyu-y5ZG1nsSE6-3WAyteFsIIcmIjHy3HN9-IhV4qkSS8Ej2QbZdbe7LXJIN3ByYks0hW8GlYkiF6TfLmaFqgT2xFAi0puoe69uXhEUp2pbgyrPIAN_06a-f446uAp19_amdig4jk5PoEGRZx-uHcLE95Tk3ZAZUUmOFu1e4429V9AYGRZBDz5YUfHCrRDBy1DMkj1iSf5m2H1RqEhRwDvIXYaMKbvonn6ombZgWg-iJ04mq_gzhGPq4hGpHZJfotDqUB4Y1M9RvlAYVP8MQ--7fCTQpnYE24qFUcaBMjtmAunNNQWaAGfab3tik6Mw5uOtMB0fFm_OvxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdkJJqz-78zY8U_30Dfglcta7K9tdIA_mBej6S4HzwiQfXhpphY49CqwhU9Srp1Rj2lBb8zy7DTC00qa4REi7hy5pltFQeKQeghT-2JtvGrxjTMwFU_CRytV9pAnqUglfuFogTVj1NVI-O_qbAfA4s4WQBKXqQ6PwvPzxIK6Yiqk7zsrjRlgPzpwlI0OzEjoVwVKBIwvw7Gng2eSCjUOrE-WsgWUuV7IXQMcFIqKYv2jMBgBdW8EOGplM01yykrTtgY6O1FbkVn6MkBUYpeWP4C1C0Edpt4wlZQ7U8qY17dFBaL5q00cp7GnuHAaYE2-6mgxLhS1TeI7Ij1GqwUlaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9X_iPcn-yQqE7zlHk-GlhvmUEUlVjaV2QAyeIfMfwVq82_PzgG_4wJIuEeeJLxWNHYILwBOlwtEHjwahuG2isFTFzL473xgYjxh54CL0nxz1U_e033a6i_QW-nAdvMamiBePsQWW-bI_LFSpjTicaKWrbvNbTYjRN7oy1KUTk9-4Y5qwjhPdH116DAy0b9DSIfineWwAW7PBpm7NRswOzPTclBj9zzB2VpgIJs1J-Rm5CD7q4KpIklZtl_zOMCrWGLToDb--2xlzhawE0yP-x1W2Qzm2vWEj2y11D2MG7seUueq5L8GzjoDZ9Y1bOHNEm5V1a2DXB3K38YPdT0Rag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=aEPBhGenhlBdZBp9jjy8jsrI2XqMBXwD7xD5FVMw8b6nn0yxNqyMjJhE2pnRcm9prZzBkuOAPdLMmtYlT9NNg6XMbAG0cLzW_Dbu_tlBasN8EWKDqd7jL4MRlE7oAfjqnuIh_2IQghzHOXOCq8VTvEUOGmTIoYk-oukCzXzdrWe31MHOGLHlwhYbwZr-rS1xK6Ly_1_-pOtxiGXkZ71QtN1Fc7DYgqM1W6oCIh8i_pgabGLR4UNx_hgHT5gt_dTkcFfLjTmk8sFuVtbCR2N_jy5HXiIq07pSVl6pkI3NEeEE6ZPbMFOJ4DX6Dnu-GQ4wp7E216S85imUlGUJQ0T1TZAK0N7HDG0BmbEKhpx3EmIR4uywNgCy7b_Hk0C85YavalG5pXFHkrTDa5TUeeAYIHM2LPs5jdxwW_Wv2qZMAn2a-PRyor5ty1vX1TQiLQCS1BBqAKRm61Lz-E64P8__rA157dckDXWSZhcgVQK2KtluA6Al2p4R2vr-Nrdk33yuMlSdIdRtBZ3DxdvcpZGSo9yVlJOsVTu2cgnhoB311x6LG533kwyBQ3oOf96ERfbPFAAjMlHtCaJkGyFmNC1l2g711CeOpmYwgknGxTnaSolZA_w33FRJJSdwnabRPZTpfqG0ux2_qzJdlbh22D_-0UIeTLoLH2tkQ6okcv7VdE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=aEPBhGenhlBdZBp9jjy8jsrI2XqMBXwD7xD5FVMw8b6nn0yxNqyMjJhE2pnRcm9prZzBkuOAPdLMmtYlT9NNg6XMbAG0cLzW_Dbu_tlBasN8EWKDqd7jL4MRlE7oAfjqnuIh_2IQghzHOXOCq8VTvEUOGmTIoYk-oukCzXzdrWe31MHOGLHlwhYbwZr-rS1xK6Ly_1_-pOtxiGXkZ71QtN1Fc7DYgqM1W6oCIh8i_pgabGLR4UNx_hgHT5gt_dTkcFfLjTmk8sFuVtbCR2N_jy5HXiIq07pSVl6pkI3NEeEE6ZPbMFOJ4DX6Dnu-GQ4wp7E216S85imUlGUJQ0T1TZAK0N7HDG0BmbEKhpx3EmIR4uywNgCy7b_Hk0C85YavalG5pXFHkrTDa5TUeeAYIHM2LPs5jdxwW_Wv2qZMAn2a-PRyor5ty1vX1TQiLQCS1BBqAKRm61Lz-E64P8__rA157dckDXWSZhcgVQK2KtluA6Al2p4R2vr-Nrdk33yuMlSdIdRtBZ3DxdvcpZGSo9yVlJOsVTu2cgnhoB311x6LG533kwyBQ3oOf96ERfbPFAAjMlHtCaJkGyFmNC1l2g711CeOpmYwgknGxTnaSolZA_w33FRJJSdwnabRPZTpfqG0ux2_qzJdlbh22D_-0UIeTLoLH2tkQ6okcv7VdE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Vk_NP36G7ckcYJu5C6AQVF61O0SmgwyY7tzjrE1VtdsiEeC5E4aI7LUWgvlciGqR0nir-RetafsTYg03jMxTM7LFKfQKgNIGEtsfVyove-EBES7e3QFpPRtJ7yjspTkiIObIDufN2fKSBisD9HY62n5hCKV801ZZhLz9tS-jyQ1dRdWuEVnf6imPr-uB3CqRnTKKMRzTXg6nRtWw5URHDBvNSRhKJglUjJrFv4mF75o7iDSbC7-qDXb1gnIdxGYsyeQBdvXBFuHKPQkRZlzZBQlgedBZ6LS_9ycTyvM8vcHk5Y3VoYlqar734q-dFcWJilJUtcoPB4VImDhfGmKPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Vk_NP36G7ckcYJu5C6AQVF61O0SmgwyY7tzjrE1VtdsiEeC5E4aI7LUWgvlciGqR0nir-RetafsTYg03jMxTM7LFKfQKgNIGEtsfVyove-EBES7e3QFpPRtJ7yjspTkiIObIDufN2fKSBisD9HY62n5hCKV801ZZhLz9tS-jyQ1dRdWuEVnf6imPr-uB3CqRnTKKMRzTXg6nRtWw5URHDBvNSRhKJglUjJrFv4mF75o7iDSbC7-qDXb1gnIdxGYsyeQBdvXBFuHKPQkRZlzZBQlgedBZ6LS_9ycTyvM8vcHk5Y3VoYlqar734q-dFcWJilJUtcoPB4VImDhfGmKPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZQ4j0a27fSOIpeLL6ZC1TmCg5VQLV5GqHjI6rZKKTyRpfUeIqZ0jAxGX6jjPkA7gpy1NhvlRt_UFEgS5575jX8DaFiNqqHdE0Q0_jR9CX7bXJQUV7mzVkaxng21XptNSLEF7VuewvTcxFjv3bmWCQ4ZsZXKmAAlhBQXrdEs-e9zTAw3kz2ilUEj_uQa0DGH-7OkSuX2aVV-aYuXNpEWieVOipMXqeDmB4EZgHKZVWpZJb4rFGralFcotBOJF_k-psAZSIhsw0zVXPgzFkyv1Q3Ci36v3TYS7-ke1lpLj3HDDMfR1tRmbmaGENpKIiBg5lx6Gey9JAuoCpNAs6hMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=sNop3_yls5HbJQSR8XA7NhKmOvamf6pakpFzmctXoMqCiZMaj6FVj2tmwMWc7mIJ8oRmRtnGAkWMnHS413gRso0h08PB4zxEXwneUEQqPqEyLDYqtvy1VR46xZfweUxpGMELlTJsOutwcORH9YMoxbo4Mw1c6a57hpxe6EG6juIUMLG4_7qiwbVpbZ608LL9E2ladbEHR0joRFU4AtqbyKGgE93PjBcTwmUbW51dg0nSobWqc2nfly8af0Id8bNLC9VtbT4ApKEEaQZQgeQUTV-cC2n1dUO_P9jXiTbkd61Lxm7u7_k7cF66vq5FMiN8bYOdbvxVRbDvy3GOk7b8GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=sNop3_yls5HbJQSR8XA7NhKmOvamf6pakpFzmctXoMqCiZMaj6FVj2tmwMWc7mIJ8oRmRtnGAkWMnHS413gRso0h08PB4zxEXwneUEQqPqEyLDYqtvy1VR46xZfweUxpGMELlTJsOutwcORH9YMoxbo4Mw1c6a57hpxe6EG6juIUMLG4_7qiwbVpbZ608LL9E2ladbEHR0joRFU4AtqbyKGgE93PjBcTwmUbW51dg0nSobWqc2nfly8af0Id8bNLC9VtbT4ApKEEaQZQgeQUTV-cC2n1dUO_P9jXiTbkd61Lxm7u7_k7cF66vq5FMiN8bYOdbvxVRbDvy3GOk7b8GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuKZHWNUuuZRrSewIU0u-b3axRqADDmsH6Yo5qWLiPPpF0a5pgUaFN7-SvrHgGaU2fmJLZQT1-zPELlArzVYB40ntinL75ilzBY6Set_zYIPcmHKWE-5mJO2ZWXwgiMapiRqm3L5nnN2FsZLXA2d19Mtp7GFP5i4oksAP-9b85ehPEwaXOFTd-EAcrJI4Pp_mZ2JpSokAqZ76yhDX000294ln96kg5WFV2YgWigWfR3MTi6NWNa4iRKUgGAh803TPSM_FqdZLYBhv63pxnSCirBp0U-hssE68w2oTbgmqrYl8lau-5fCBTxee42NNxBy08c8sIZUZ_w16S4wpkj4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU-0AxOOs_pmoo2mBBXsfgWIi8wNXjpXiAhHFok0PQ-EQ1G4cAl3dXIT6fUP-O9ml0OPaK02jNJ7kr65TRq4kIHc9suaIJwiRRh67eRuZK0y49NUwW2dKrNhVxzEMlhND2s9OTPuHsjxVyZ1WCaKPxWXhHaOsiFJAQaTxi0OZNiCfRhp3JzbyxZ0cLjxz3Ra-YPRI_pl8KT-5aQyh7fVyhnKnviC2sabFUhWwE-kpz7FL_NADrppahAGcjwKua-FSOy-zkhDfQk1_GOfK-7flLt4_u10j7d6m2zIgzpcOmVt97Mq8fIfEHVc9w-CX7cbAl0mD7ta5K8ys3NmkCdX_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elJKQikAJMIu6K_NDA6Ji9u6G1ZqQpC_ecC9x3QFLU78HB02jfmnklI9wJ1lsgOLC8um5HSCPd0nTocF3Qtb7RgE-1_3r9IQGcz0Gb7hj5ZFkVVeUQG5gCwlJCjOk_n1-XPsn_LIJ6NrvEzVPXvsmTsfSR0zSRDwotVyQAl8GOi7G_Fi_3jaMCa3kUR_m-fFcL1K10YHNnvYtoKUQTjVijbUa3MsY7T9cGJRtpqewjsapq6-uS29QXC4G4TSe9QhHyTl7qZQVMWnrYSXOqSwPM-SrtdzU2vXJGjmfDH_lBUPOtTH27tVOUYVwtGpJQ9aiA8MYJzmO_dnAXbqdphplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL-QEpgOchUIQdkX_x9IV7IiHRWubidjZiNxxgS4duBR1cdBFBNVkG3HJ1gn1ovFjfwZSF3Jh-Hq14XY1jL7NtEKAA0kx3_8diyzrnr6O3BbprO_8dP4507f61Zq9kN8l5L_oCQrtOI2x_kbAjcIVVqAnXYKiQEmi8kfKsp1k5_Jxw4XRnDQhNUm3GAI10_oytUSwUVaKqAzDq09xyMuGoJBFFfoLeEi4Ys5R-R2oEF6OFscEZ-Eh8Q4YdLTMHE-R3lpX0pA085OqE16-B2c9aPWfmSe-s0tRQ_XWQJgD-mc06C90sKuorMN922PiHYezW8eDeOgGauTqJcTHnz-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2KwkKhn8VGDATtIOCcLgEm-mnW4ho6Vrwi1gjCVxqRvHrqXPD_cKEJLF7G9VF5wYoMGQfcQ5ikruS4sRcwVAHiJKKMK1bc0_fE3JVWOkHvL7UAlouCBE_WF_yqKa8fjhG-zTufduYrVEvhaElK8ZmzDQDfH8KbeweWNrvALFiqVZJGrzL0WW8b99nYol2o_3IWpHhyyrl-uTTh4rT-tR8x2LwO5Dp9GqsDidIxrRKf6xFscoBN6HOer2mHhPxiM7UxJP3JlSz-dYtQ6tZrc0rNpGqnQlMt-ye3AC6lAyIzd8Axp8G9YvSEXq1yeEdKyEvRAAoWSTQTeXTgohWXitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=LNHawr7uClABeTOwCyWpqLgSVi5vgUyuaEJJ5f6Aezgmwvwc4GbYP81Z-aupgZXNk-78LKzsK7N_cCLLMrMK6qUvdOb2kchD6WTUiEM2nrBmCCxHLO_Lp3ugPxiULHac8JVmFUjVuGJItT-ZZJWU6TH7mWn7KWn_kdyVnCvrftBrWRW7KWxXKVRS_d5Wl2cWWFBZWDYml0lOZwTXs0HLE2NCwB7n52shoKIER9pXBrChC2K-z6gwFafn5xEuto304lteeP-KrJQ-rbDuliUmT74erGnmE7JFYEJ7lWUuMRNZAbO3DUDJGglfQc_fTshRyaixnIGKWdosxwj5IaZppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=LNHawr7uClABeTOwCyWpqLgSVi5vgUyuaEJJ5f6Aezgmwvwc4GbYP81Z-aupgZXNk-78LKzsK7N_cCLLMrMK6qUvdOb2kchD6WTUiEM2nrBmCCxHLO_Lp3ugPxiULHac8JVmFUjVuGJItT-ZZJWU6TH7mWn7KWn_kdyVnCvrftBrWRW7KWxXKVRS_d5Wl2cWWFBZWDYml0lOZwTXs0HLE2NCwB7n52shoKIER9pXBrChC2K-z6gwFafn5xEuto304lteeP-KrJQ-rbDuliUmT74erGnmE7JFYEJ7lWUuMRNZAbO3DUDJGglfQc_fTshRyaixnIGKWdosxwj5IaZppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YidZm0ThWxBe8TEU2JhidksaXcCjtq22BHZ_TtoyCOnVq9G9wQAs8_MiUz79m__vidMeMveN1nJdfsTE5O7NJW0dunHON983QHSWN1mjcsH8ptU05Po2CXkEmj9pEXc4AWZFWW9ygLu2ceFBENYvFXxWwkEVUieERSCWpB1MNUtyTTFdDcO9-P8xg7_cUJgoLB2sp42etChKVgurGea-lvMT7xi2j6UkhJI_-2ldGzCTwvNsUGGrMeNzmO7rxJYFAALYmPZfQziBUH2ssPvsDvT6KAVoPGmZr-B7vKgVSLAy2irgt7QC_PXMFQETXii9m1ZO93DOCK7b3x_VnMuEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP5G_bnBGbWZPpdygTAug6XA9ngPELVxQVqHoPCQ0qlvsWZbhHzAFxZRfm-M5UlDx7qc_4qtZiuboD-mnN8mLugFHu9D6Q4s4BBv48BQvmvTMgI8MyxTwhomPmf1EWQbBPk4yQJyIzQm_Z3X4zgwkZTYAeQoSqAh55WJHodrVw_DJ7V0Soskw79Ei7Cy_zUjUPjWtSnzRR9f3oOlpFoJDnwLhX04Zbivix-pM9PCqu7wCzDqdLtUQWPAWX1vsCPSrvjF8owDDQGpMh1Bu8pr0QVE0BjqvJC_rTyAJZdgl0VtuF0CHhSiwhlinrRm_sAFTwd-AHGyA-jySBHKVwaGgw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=qPfcLBXCIImGxwTGwdgj4hWeXTlRwDy95yu_3cWmXnUMAsaS75VC6E30KiaOyKRucMfhVTs3aArjo3dhNmLrUNGtk8FN6y8gSeUmui0tIHnebCW81nHdq_MmtXmKZ0qb91ktAkoKUWIaxSxdloJpdh3YKTosuLwRUOTNUZVLwF4r4zyZv9swI-AeQ2F4EqAcN_D5y_FmimUSCYW2oOEGCXdoslTP_i4euB7_X5AlhAfUXvy7p1pui-fCN6e4b5u-X4uJgRCGNaUjAgC4lvMDnTSXRJH7yuJNV-s9CkLKgu45V5KC4dlaIBK2MEpM2UxoBd-F6-x50Q9I9Pk-jYuzt37O_qJM5KFCN5UQvcpgPQAXoA2brGoKH47mWoetEIMFAMTbArG9D-G3mqxUcABhzsX5fPXJRvfXeCbUWWvF36P5AjQ5Z8Ok2gVkYoFzYkQgZbjZ5PdE97KNYptnc-c9LGLynnWC6uTvMzRgrKQk92j43gINBrLPR2nN9zMOjEupAmU6braoQU7xqQbjwRisasUqOJ9rg4C0fPlkQVKCSNIZ-nURqCZlEMsoWaSQ5kb_rTbaUiz1QCTf1zuzBbCR9ewu_t0cSV3SPA5Iqhojh6b9DoCwkzGSxOUTlatMs6GBf4mB8el0UpROwlyu1qf_GUrAcptmCDM8pGw7brtnuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=qPfcLBXCIImGxwTGwdgj4hWeXTlRwDy95yu_3cWmXnUMAsaS75VC6E30KiaOyKRucMfhVTs3aArjo3dhNmLrUNGtk8FN6y8gSeUmui0tIHnebCW81nHdq_MmtXmKZ0qb91ktAkoKUWIaxSxdloJpdh3YKTosuLwRUOTNUZVLwF4r4zyZv9swI-AeQ2F4EqAcN_D5y_FmimUSCYW2oOEGCXdoslTP_i4euB7_X5AlhAfUXvy7p1pui-fCN6e4b5u-X4uJgRCGNaUjAgC4lvMDnTSXRJH7yuJNV-s9CkLKgu45V5KC4dlaIBK2MEpM2UxoBd-F6-x50Q9I9Pk-jYuzt37O_qJM5KFCN5UQvcpgPQAXoA2brGoKH47mWoetEIMFAMTbArG9D-G3mqxUcABhzsX5fPXJRvfXeCbUWWvF36P5AjQ5Z8Ok2gVkYoFzYkQgZbjZ5PdE97KNYptnc-c9LGLynnWC6uTvMzRgrKQk92j43gINBrLPR2nN9zMOjEupAmU6braoQU7xqQbjwRisasUqOJ9rg4C0fPlkQVKCSNIZ-nURqCZlEMsoWaSQ5kb_rTbaUiz1QCTf1zuzBbCR9ewu_t0cSV3SPA5Iqhojh6b9DoCwkzGSxOUTlatMs6GBf4mB8el0UpROwlyu1qf_GUrAcptmCDM8pGw7brtnuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=DJhxP-QDN-hswyVi0yDUMo72CaMdSE-prp9KtX5Nd5eQXjsCfppJ7-qcciJkDqVfbNZCpkOzEj33p0LT9vnjM-I2O6NjRH747sOBzWaVS1ee2BbWgcsu5uGU6xI_1K2ZOfAm9WeH8uxPOG4cvrxFjnw5B1BmcNthOExBtLipPUTeNE4F_w-5YNaWIYjMhWR5Cdu3R-bGSYS4sC3puImOB_jQ-6bohoBjzho101Q7ZU3PpJoggaR7Ro0R_yncGOIGlDwdydQfDw74G-0Y9-aPHWMOWQlQrZyaxvOozOHJ8_98O3A2qL_1qMPiQQ276-Mv1p-D1CYRlz-fLurW4xLHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=DJhxP-QDN-hswyVi0yDUMo72CaMdSE-prp9KtX5Nd5eQXjsCfppJ7-qcciJkDqVfbNZCpkOzEj33p0LT9vnjM-I2O6NjRH747sOBzWaVS1ee2BbWgcsu5uGU6xI_1K2ZOfAm9WeH8uxPOG4cvrxFjnw5B1BmcNthOExBtLipPUTeNE4F_w-5YNaWIYjMhWR5Cdu3R-bGSYS4sC3puImOB_jQ-6bohoBjzho101Q7ZU3PpJoggaR7Ro0R_yncGOIGlDwdydQfDw74G-0Y9-aPHWMOWQlQrZyaxvOozOHJ8_98O3A2qL_1qMPiQQ276-Mv1p-D1CYRlz-fLurW4xLHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut1OLtQd0TbbooLqPWI4SWzMOJOBRh1JoQNqXDrsp-4pB3HDoTXRMyyM3E_CmKfd1hHggUsQB97vYoiGjCxDuEVcb0srjYhMq0HbGZDIhuY0TAIcXPFv6b9F6NgLpPxiTD1Pn__CAICIPm7ki_kKResH1Z1g3HYbsObPs_a03mfViHCXy3B-DE0UTZ7IDVJoIKRIALQJqxqS8qshK_PQBvy4Jd_LZIxTxLhxM21T5vbpjGav-MH_JEFcnUZycTkQWTL1dDeb74rXc0JetnjCgisbuPTvCI-0F9TikZF5rNBjT-PdwsyEEMC77ReqR04ViRf0E-3ohhwp3CCX_GTFQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ysTFxkg8s7Qlp7SAeOsTNXsRRKpVpAKy4p_U0YcgrZ1B_7eN5wsnjHBLcQLJO77Wh_v1r4s2DDycCkGjNPo0bfKOaXb0581p1JD5uQRN1KpCEFemWh6Csj9AoDwkydfxGFNj4k52lcgnSOgIMLoGpQd7Z5UVU7Vd_yitTsMJWQZTndyub1sBJSP4tveUAAaSpcBa7NHdaHDSrvKwFTmJDAhoCnE8nAPSxE7BX_j22cjnXtwCYzaON3DYDD5UOkvs7uutxRfcoPnosxtRGntNewhsGaASZdQWhE8ZhlDci34GohNhwljGxtCgfXgQo9uFGzo8HBY1KsRlb2kvhO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUIz7_2rtq_bRuoXdGZ0Ml9W8ogGdxRhZ2qZx8R1bJtpCvo9IbvAPItcMgNaW3Qhy9vuKDRHNuhGum2h9ii9T4lS9wC32w6TaWV7xu5IfF81TiO7l1hz5AXz9abJJMbXf6vPpmTXHOdosL_La6II0EQjuWigiOn5jsB-PqJ0D4eOyWsCQYqsPMJH-IiJp21FkWxCVYAorHZTdQn1nbHgfyvJo7zlVA0u7jpJ-yWxTnV8oZMYTjRWUA2l_uZsUJGYGiBganLfIYSzQ4yaw1FENljN7ylSuPm9vOyKcelaKYNMkr3WNUslnp_qfDisqZs14o2o6UNsyJH2mc4PeWXhtA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=tms4cdTwYOw8zw4PbdgMncMLscYGYRe1EZsJiH68p1cinuDE--gIxugIRLn8BazmCrmEnHNhg3ZqUPLUEbJfvz-2FjKOg-MgY1FRNU55KGA_FkyUcQqmigxr8UgzkAHaLFuw8y2IvJROotxJOQYH-lV9DXjLS1HSRMgtuW1rnr-DhLzsi9tKCZcMJ5u7dBzRfEJ733wvq8r--1CRJAdaw4HDNdkaLDYOUatCCd4srsgyFksncAKY-IzFfIP4QJ_Uf1OHJXFOzIwmEQhXqFBy1B8E8nJwvznEnWj4mz4wnXNHB_r8Icd2Wp8vlnqavfWZxfUwds4N1rODbLMBUUzjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=tms4cdTwYOw8zw4PbdgMncMLscYGYRe1EZsJiH68p1cinuDE--gIxugIRLn8BazmCrmEnHNhg3ZqUPLUEbJfvz-2FjKOg-MgY1FRNU55KGA_FkyUcQqmigxr8UgzkAHaLFuw8y2IvJROotxJOQYH-lV9DXjLS1HSRMgtuW1rnr-DhLzsi9tKCZcMJ5u7dBzRfEJ733wvq8r--1CRJAdaw4HDNdkaLDYOUatCCd4srsgyFksncAKY-IzFfIP4QJ_Uf1OHJXFOzIwmEQhXqFBy1B8E8nJwvznEnWj4mz4wnXNHB_r8Icd2Wp8vlnqavfWZxfUwds4N1rODbLMBUUzjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMOxajjKQmC0BzD2m2gsikd7TojP9QZS0FfinmGMBQa9WJhV0wj6HQyF2PDR-E5Ebibqii1nOZAlIr7LdDNLcls94mS5jTkPNOdR0RTE8Ns4Bh5WH55ftwQ2cFVOtPOALiu37b8dv8T5qwCGjBeZXokpZIeeqNqCjZ2NMo69vMMbXKtoP8yQFMKCYk-C70UhwXcJfzi3YrWyX312lXE_eD8Ag4h1pWHEtExutroLiP1laPp_14HCxNVCsb147nWS67Q4XWW0q4It_OvXTtpABZnqtNoFZKr47d94U7SMRqMhdOP2EBWuwo0SoUulBLYLtZekl08_9aOZHymvyJIorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9h2HqPKMtCW948Bek9CL301qGUSPPddoOB2CJJMA2aJ73sTioDT1GXTA_7RvHrvoQvIH2T9shDs1wy0p-pFc20YQlTz4zxwT6r0-VL5LLyKw0AWyyUxhPIqoDVWbFhIq2iUZacqXsJJCfh1xyprYhA0ToCJDbM8eW7mNKMQrJuLCx2xHX1VVLkucNww5n7GaShg8u9ncJBF-yqhwa820uFyq8hEOsYWJu2mEb9w-oUjBy7oYZCV3ZHBGAWQ-Zlj4_PPFkcxBrHeralp3wrMv0atO3QN4RXul9-3CSB-r7jD0PRtMZ6LoPsGC0V9mDKHFiiLsaZjSz7Pap0b7c1s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrvkzKH0npeWGJcOIL3UXKu0rFHP14YjQbj4z6lZV8ryBk6mJJ-09AFEGay6S1Mvt29W9PuzIu-U0cuy0-lIBhmYVorjSDcDEYm2_Iz3YFbyaDAI0tZZDMCprkomtEq1z6YO6pnst4Dca5XbR6JwwKVkgK9I3eAQ9aK66EKACtxmEyyX_uXk5QBOd2hx4PhdJG8RE1z365Dl8Lg9R5gtklUlFk1aFtx0ZyFmsA9iyVOg8kQVSJUjUPIe3RJIJUUSnqEenytAUGcM7G5-1Tefpa2KRw5mxS2fee3OtUpsDveKPLgkLIB98QO1qdzNIsUzGSsSG6kqMQIvsFtQGyXyFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfzmbbw6dNdJqr0wyuhkulPNWJkVoEp7cXIXQoX8XsEsBs8aw00eG3ikAueCA0YE-9WE91n1u1hc-y2R0Cunf6fOArsN7SCPWDD81XpeLXaoqXpWU5Ru37gwU2zPoizYcr0tiMF4IfYCHUtrtJfSfIOL2olxiZz9T0DgmY2fAm9KroZKhgpNr1cbE4rEejDFCjK8GT2JU00KdodyyDYQWndPUpKcGBLRDkpw47lF5YhtZqVFwIs1neQnilrrfwLWqw73veb_I6FqOAtCyJChKMhFK91hrD0CLu20Tbnj_NGgbhfokoNWARzEZ6CiOPz21uzVigl20E6ynP7w2m0iKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=YQaQnyfWa5z6UlCuHla8Ui9AQnZ1SUMMqYLyc-nsaNtvw_pjyPmD161YTo63bFnXWCDuPjvbCx4W3OE1dHJrMmVv241Njp5FS3ewfQDV5UD0tDOTvrDQVzMe_j_BaQ2NSflISzii2yg9q6REM0ReZFEXtZ3XCFxuRh_n6Fw57-VWFsOefSWgXkkI7GCTSP03JH8C9bUYuZzsAYCYjFyYuPaTEznw5Ej-8ZaZ2cc9uvC2cCp0M9AthOnKWYLAVz_vdf_DuMQuwG-2vL8Pm4Ca4ef2jh2cePyH6MUWPpxkcrq6XmSBf4f5-GGbQimLU2I1XUzZeJyZ4TvDEJhFx5lt5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=YQaQnyfWa5z6UlCuHla8Ui9AQnZ1SUMMqYLyc-nsaNtvw_pjyPmD161YTo63bFnXWCDuPjvbCx4W3OE1dHJrMmVv241Njp5FS3ewfQDV5UD0tDOTvrDQVzMe_j_BaQ2NSflISzii2yg9q6REM0ReZFEXtZ3XCFxuRh_n6Fw57-VWFsOefSWgXkkI7GCTSP03JH8C9bUYuZzsAYCYjFyYuPaTEznw5Ej-8ZaZ2cc9uvC2cCp0M9AthOnKWYLAVz_vdf_DuMQuwG-2vL8Pm4Ca4ef2jh2cePyH6MUWPpxkcrq6XmSBf4f5-GGbQimLU2I1XUzZeJyZ4TvDEJhFx5lt5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Btc9tB_u7lsOSVbQgGU-HIdTMbkNJOHGStbXVh4KYma4htfe5f3CYbQxYo3nSpDNEH3DxmTDNzao18j-Wn_GON4cTSUCzQ5iYxcmksNDlA_cAK4R8R0_lejOnNd2nE58_-E5kXVQfkqbyphrmNv4N8Kep04fAbm4ae8e65n_dc9NFRi0ZO1UnfLI_KoS12P0qAKS5a1VAlAavnPNO6eQx8AppskKCcqJNxhe5ru3UU30zJLOx43wZDXq7FGd2TjioQlj0PqNpTfaEpuXsVJ_lgR3cL6jYJhvwC5OMIj1cx6k2rdRmiUTkK5djeI--xK3mS1esLDcUHC5GWuJtbmb3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Btc9tB_u7lsOSVbQgGU-HIdTMbkNJOHGStbXVh4KYma4htfe5f3CYbQxYo3nSpDNEH3DxmTDNzao18j-Wn_GON4cTSUCzQ5iYxcmksNDlA_cAK4R8R0_lejOnNd2nE58_-E5kXVQfkqbyphrmNv4N8Kep04fAbm4ae8e65n_dc9NFRi0ZO1UnfLI_KoS12P0qAKS5a1VAlAavnPNO6eQx8AppskKCcqJNxhe5ru3UU30zJLOx43wZDXq7FGd2TjioQlj0PqNpTfaEpuXsVJ_lgR3cL6jYJhvwC5OMIj1cx6k2rdRmiUTkK5djeI--xK3mS1esLDcUHC5GWuJtbmb3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=H__Jwufp2RcRC9_1AjmX24k1SJ7t2KqZT0EuXC7njvu31YR_z9s_8rmJdVXAGM_PsqPjGPsSLepR1gpzDpFjtz3iC_qSV2dZcEikaUKav1by_YsVFCeXGunXnItaotHjT7SqVSRAio-eM7IEXLCJdIKAiMPKGS-7nijxljdAapBzih_nSK3Cylrxz8rlo18n_iY-a1FvRdSly8JGcUy8Zr_Z55eOilXyS8c_EgpvlPV0S62UtRxsVI0PerncXG-3jtJ0nRdDAHDc1ry-TJezVaUD9VaJWBdBF9RCUTgLj5Ve69alRWmQ5HEOFklsy6D8kURh3jc_pbop6FZY7fufFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=H__Jwufp2RcRC9_1AjmX24k1SJ7t2KqZT0EuXC7njvu31YR_z9s_8rmJdVXAGM_PsqPjGPsSLepR1gpzDpFjtz3iC_qSV2dZcEikaUKav1by_YsVFCeXGunXnItaotHjT7SqVSRAio-eM7IEXLCJdIKAiMPKGS-7nijxljdAapBzih_nSK3Cylrxz8rlo18n_iY-a1FvRdSly8JGcUy8Zr_Z55eOilXyS8c_EgpvlPV0S62UtRxsVI0PerncXG-3jtJ0nRdDAHDc1ry-TJezVaUD9VaJWBdBF9RCUTgLj5Ve69alRWmQ5HEOFklsy6D8kURh3jc_pbop6FZY7fufFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=RwNHtjvRxVS1nfKLp9UH77J-COeYok4qHLrc3cUMBRUCbOaSZXuibGBj7ENkDtc6QM4hqiGhO76MKi0X0PRNhOrefiJYOnys2GylKMv6Bv2Ly3qLh-VBGjUZkf6L0h8i2jb1XuoxHv8-pt1-rGkDcWsuTqE4OxFBl2k0jFxF0Y58KfPjCFmBWqIW-ZBJnvoZXWGVwybpuqYVpUujsDbvVsrX3zP5ACYqesMuo2Sv79IhK_AQODy26daiP8cFRSohyRUJMzoOX6oE3DxrdaEOxlPCiTKtrjxudeAu6kcdk7L7rYYJIgHRAjIHRQcAJxumwpPqbG-a9RiOs96LPI844g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=RwNHtjvRxVS1nfKLp9UH77J-COeYok4qHLrc3cUMBRUCbOaSZXuibGBj7ENkDtc6QM4hqiGhO76MKi0X0PRNhOrefiJYOnys2GylKMv6Bv2Ly3qLh-VBGjUZkf6L0h8i2jb1XuoxHv8-pt1-rGkDcWsuTqE4OxFBl2k0jFxF0Y58KfPjCFmBWqIW-ZBJnvoZXWGVwybpuqYVpUujsDbvVsrX3zP5ACYqesMuo2Sv79IhK_AQODy26daiP8cFRSohyRUJMzoOX6oE3DxrdaEOxlPCiTKtrjxudeAu6kcdk7L7rYYJIgHRAjIHRQcAJxumwpPqbG-a9RiOs96LPI844g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ig-XZHIgKQQPl1B5qqc8rlzwy0Lk18nJuny9bSjosqOdHhcmDvXslxscqLNvnowVLGwlIZynjg2CqLGqtmKNmtl9ixysd7AryzYj40dGLcCc_PRzbh0FOtpzTDWMyLUZrYg_EUC-M-O3sdklKSAm5FtmnJOAYWimlt_pwjmn02hQ9CdcoEH_9CaM-4ODQaioe1xe_jIjS5IGUUnqFP6zfhe1S6cbNrW2kTUn3KWKkhSxT9y1j4kJAJbfUE-cEmaXxo-FJh09rHMEBW9Pk1o-6QjI8AlQL4MrxndVMOcsHzMdNhs2alE83iuhZyq44NIRhVAVjgHorn7Js1kIJyDk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ig-XZHIgKQQPl1B5qqc8rlzwy0Lk18nJuny9bSjosqOdHhcmDvXslxscqLNvnowVLGwlIZynjg2CqLGqtmKNmtl9ixysd7AryzYj40dGLcCc_PRzbh0FOtpzTDWMyLUZrYg_EUC-M-O3sdklKSAm5FtmnJOAYWimlt_pwjmn02hQ9CdcoEH_9CaM-4ODQaioe1xe_jIjS5IGUUnqFP6zfhe1S6cbNrW2kTUn3KWKkhSxT9y1j4kJAJbfUE-cEmaXxo-FJh09rHMEBW9Pk1o-6QjI8AlQL4MrxndVMOcsHzMdNhs2alE83iuhZyq44NIRhVAVjgHorn7Js1kIJyDk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ybr35IB-Q7WqIpATlu1HmG6h_JlW127getfwM2Op4qCLPD-9j67E1OI_EyrtXrujoRTuepEPrzzm_rR1ivPfeLgAGKIkgeyGnyVmItxFt0xv9sgacQ6zhv1PNcwohXeKA4rfJt0L5vjTARsUnWTX2Z4R2-2GBS1tF5N_h4BofOPbRvIGrORX1SEMOpn8lObY9gn9Iwe3F6EsoUOlbjdnYUEposamuR1MHLbn8G4Qq4uYNxri-mBXi4E4t_gSFjPhpLRGAcCjDtJh_BhOxYjpzm5nB1bkdquui8RLp024uG2B3B_v94crlb5mEYbY6f5M5oyHH-5QDGsLRtcY4qa0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ybr35IB-Q7WqIpATlu1HmG6h_JlW127getfwM2Op4qCLPD-9j67E1OI_EyrtXrujoRTuepEPrzzm_rR1ivPfeLgAGKIkgeyGnyVmItxFt0xv9sgacQ6zhv1PNcwohXeKA4rfJt0L5vjTARsUnWTX2Z4R2-2GBS1tF5N_h4BofOPbRvIGrORX1SEMOpn8lObY9gn9Iwe3F6EsoUOlbjdnYUEposamuR1MHLbn8G4Qq4uYNxri-mBXi4E4t_gSFjPhpLRGAcCjDtJh_BhOxYjpzm5nB1bkdquui8RLp024uG2B3B_v94crlb5mEYbY6f5M5oyHH-5QDGsLRtcY4qa0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=FxWiW8Pb3c9LJE2IGz3v6lj3EUOsvxfBPSCEMZQD0nbdasncgnm1fipZf2DUIuz-zi4mFH0amaz4j-pYLxQl2mgqbj4gK1xSavO65C9e9isLJYJdDyCxouLkPbwnJ3PEu53p_4orUJD_1cADyH1BDUzQvqWr7Kk6yzBhMktQWw72B2AVH8KF6fxzPrGY0qjSqPIQ3_kU3uZ3qJnVHqDz4MuthqPxKry3XC0DOB15DS80YQqC0qf5c7Yt8F-fY2NqTyG-5EsgF63s1rZ93Rutszd4iuB_lc3gTKdA0O01sV6-y6Dzn4Y5TlPB1yJB-Cm4axvVMhMYYXX-4JbuMZ72YmxK36MJMFmRqLrPLPU0MO_JcoWt5sDPxA9Gcyno5SqyJDe484ZHe4cenR4FtHezecWGTWp6ItfZXCaSK5viGu0_UhPMJSDqB_MsyMt-5R-SWvujHNhuiw2Zuh2EDTHNSo3D0_J2MkwtavjQqw4sHEs0O-DktwqYWAtXIjSnFAmi0He9cCGm9II3z_0reK0Olyhh4zqs-pYPt-cQv5lFaFCCDQ64dh3gu029LVKYUNciF9xs7evKO8h-oRdAlr0EDDn_YGG1dtVQl-O_IAZJRnQKwQ1Eqi9Sbkj9qjPPJGrH0YgMoJ8f_onWrMGtH3XNK2WVk2kuUhaRffgHtWv3eCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=FxWiW8Pb3c9LJE2IGz3v6lj3EUOsvxfBPSCEMZQD0nbdasncgnm1fipZf2DUIuz-zi4mFH0amaz4j-pYLxQl2mgqbj4gK1xSavO65C9e9isLJYJdDyCxouLkPbwnJ3PEu53p_4orUJD_1cADyH1BDUzQvqWr7Kk6yzBhMktQWw72B2AVH8KF6fxzPrGY0qjSqPIQ3_kU3uZ3qJnVHqDz4MuthqPxKry3XC0DOB15DS80YQqC0qf5c7Yt8F-fY2NqTyG-5EsgF63s1rZ93Rutszd4iuB_lc3gTKdA0O01sV6-y6Dzn4Y5TlPB1yJB-Cm4axvVMhMYYXX-4JbuMZ72YmxK36MJMFmRqLrPLPU0MO_JcoWt5sDPxA9Gcyno5SqyJDe484ZHe4cenR4FtHezecWGTWp6ItfZXCaSK5viGu0_UhPMJSDqB_MsyMt-5R-SWvujHNhuiw2Zuh2EDTHNSo3D0_J2MkwtavjQqw4sHEs0O-DktwqYWAtXIjSnFAmi0He9cCGm9II3z_0reK0Olyhh4zqs-pYPt-cQv5lFaFCCDQ64dh3gu029LVKYUNciF9xs7evKO8h-oRdAlr0EDDn_YGG1dtVQl-O_IAZJRnQKwQ1Eqi9Sbkj9qjPPJGrH0YgMoJ8f_onWrMGtH3XNK2WVk2kuUhaRffgHtWv3eCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=EEIXIPwx_oqRsaVO1QmAOO60KvZs_Ho9ZC0aUx08d1xsWNwyo9K38oUueILAPPXSHJHzj8cPF3OwhzsSR0318JKMST-vnWT2muJxItvY7suYTH4ULFoHDmep_KfTF8mFLXHRknMixG5yrgmliNeWmoUAVZ9KnLYlw6NgEIFd0MDZBBK7ab3RCsrlEhplcJzkYpe1KeqjfqbPE5e1TKfxNhfo5LOT2fNenEeDPDSoTxIU-q6qZylAO6hbFgJx5_nHr0mXL9lVQSunfKt8CkncfFTgUvoGJ8s2PFm5gWibu7d1kSLDg2Je5urBGViSn7_cpshFDucjAwFBq_3le2a7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=EEIXIPwx_oqRsaVO1QmAOO60KvZs_Ho9ZC0aUx08d1xsWNwyo9K38oUueILAPPXSHJHzj8cPF3OwhzsSR0318JKMST-vnWT2muJxItvY7suYTH4ULFoHDmep_KfTF8mFLXHRknMixG5yrgmliNeWmoUAVZ9KnLYlw6NgEIFd0MDZBBK7ab3RCsrlEhplcJzkYpe1KeqjfqbPE5e1TKfxNhfo5LOT2fNenEeDPDSoTxIU-q6qZylAO6hbFgJx5_nHr0mXL9lVQSunfKt8CkncfFTgUvoGJ8s2PFm5gWibu7d1kSLDg2Je5urBGViSn7_cpshFDucjAwFBq_3le2a7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEQFSDdso4uGoo51CsdFFVxZDd_wYZ8bRUPvBTieO39kZakYyMTE4izMt_mk4oj6DX_T25ySihCjDsv84f2650O-nt9OqDEaC9SY1J-9VMtkDJbRLM7lCu2lO1GQnopiz7O8adtqxy8E8N6FGUaMG1GdoRW7rBwzPK3qkAKLY_KTqUXRPjovy_PraNPjK7MDui8se9MP_FBlGUwRLgxLZ0zgmz8HqtEY3Qm6MDPMBQMHUc4o7chfqn2923Js9Pr5KoEJCYD6lxWnHDW_qkNixIff7y2TF564pnb9yWEkLrdowC4UvrpF9qo4BbOS2dzNGqwyaY8aJEBuaPj7TyYZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6L_FpCBqtJ0ZJ5M7na5dx6WwTf0-LiqTxLmo_0iu3m5ZjfhVNoMIKVcmWdMMYoOM8DVmwWiu9n7kxvQ42OMpdkA2ba8OJ-TjbqS4PewVlCKJwqSr3agaHZNRP8LR_CWDRj-5kzD3mwaxiOPWzcfWP4QzDO7crp7ZluEAwb8Vdm3qIjjoZyMW1lvOZrW0kxOPQkZlS_hHohwijDpdJbmUNWcluBfTThMinOcny3LgbET1xD7qGYSnR-vavXUsuEMjwUYFIqPIlpTkJD5lGZ9HU185tQEbLF0YYHUUgZSRS7FMRVIpu7aD2SexaCHQyrJpS0QvnRdNWAUArYg-W3DVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xm6r9aYBVi_xu5FbzBkem8tbVuyydpp0woNog98M7lQ5LDsUmnbzmLjSD3MB1irR9EIO-yRCVlimkjyMazUw-D0PZkdW0dUA-jyMomiOGQ003mY1G3eBfgZPdCx6LVNnPnBULERwIl0d9G7tFwoJQuU-T_CCpNaru3flORLkxF41X_Vk7g0XGQAOKw4MWCKrCgiiDsGmV9WA3qSgoAdFK3shBWNmnFh-IQN53FllaIuxdJB1sm-1RatUs0JRdfL62XjBgbhqXF90KDzpONtaGGTGA8UJCCk4-kkudHZ6HV_0J2vhik7Ub00t9vKQ-dr4nBmGqxWoKmW1vWP_UrGsKAbE-4XDW0y3SyLhMHBYdDC3TxrFIUNs3iQjGMg_IEskBzMSQ4TUsUQMZhlTPz6yC72rnj1HbaP6ckBimmDiiYlN4mJXTSvAi3X1Nww79mzT3hO5IGwda4GOsTXBSuVfwuyUcTp4EfUKnH4Y0W9-ZJQ5UMce6qnIBYPrABjW_PhbkzzlC6tqYJeLlG4RlNlQaLBMltAiJtzHh6KvgOzkOxu6VSnYUA_EpWFV19Zx_qByAt_v5bUoJpQ2Rg7hf26O7dsh2v12pE35YQiGd1QLs2t1exuPDkLSLJyiocxpRmqN2TA2nGPuwSxJTM-JORrsp4FEhuBmkIt83DD9K0IxFus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xm6r9aYBVi_xu5FbzBkem8tbVuyydpp0woNog98M7lQ5LDsUmnbzmLjSD3MB1irR9EIO-yRCVlimkjyMazUw-D0PZkdW0dUA-jyMomiOGQ003mY1G3eBfgZPdCx6LVNnPnBULERwIl0d9G7tFwoJQuU-T_CCpNaru3flORLkxF41X_Vk7g0XGQAOKw4MWCKrCgiiDsGmV9WA3qSgoAdFK3shBWNmnFh-IQN53FllaIuxdJB1sm-1RatUs0JRdfL62XjBgbhqXF90KDzpONtaGGTGA8UJCCk4-kkudHZ6HV_0J2vhik7Ub00t9vKQ-dr4nBmGqxWoKmW1vWP_UrGsKAbE-4XDW0y3SyLhMHBYdDC3TxrFIUNs3iQjGMg_IEskBzMSQ4TUsUQMZhlTPz6yC72rnj1HbaP6ckBimmDiiYlN4mJXTSvAi3X1Nww79mzT3hO5IGwda4GOsTXBSuVfwuyUcTp4EfUKnH4Y0W9-ZJQ5UMce6qnIBYPrABjW_PhbkzzlC6tqYJeLlG4RlNlQaLBMltAiJtzHh6KvgOzkOxu6VSnYUA_EpWFV19Zx_qByAt_v5bUoJpQ2Rg7hf26O7dsh2v12pE35YQiGd1QLs2t1exuPDkLSLJyiocxpRmqN2TA2nGPuwSxJTM-JORrsp4FEhuBmkIt83DD9K0IxFus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TotUdZ71pu6TmjQOAIQxq4kTK4jiMNNGytuhsOU8JDqTgLWRkEGdSKm1fBZFCOpBK1r13BXK67dipRoWLRkpiJZt0gig6cNEF3odt4TLSpEI0qMCdW_I9jY2uv85nPKx0Jhc0eMXmOl3DDY57ltCvkZgLhGbIwbPsyS0VAndq2uDoI1M2EAzWt5GUEab66PL3RLH2DCAp-M6sMaO5coljtL2-3FBdyrRGBC3C8ExBHWhRRrPHAyIXpgcezPHi37-w0Q25dumprc4HuLVMoZtByIQyrvpnrOS68ruQDqT8-hKBCmPtkVs18wedLmFOyaga_315hx3Iu5tDegmzX4mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dacugvN8zheMdaAd4T4p6wc00OwFgV2RWdzPwtcKn0u22GBqCLgMCzc5YlN8qK1WxVrT-L5Fn3oFxPrEd9IZvgzozoiKudGDudJt5mz-q3tm_SpCO0NKsfaCRK77Rfkeu9SBEkvOlETutW9SmorrSviXR3ASLTVGkxTjdGAtkOnvQUafcPYTB4B6orCDcT1HtsEbyZjkB4b-UzUriZZWgJZ7uDOJjnzFkGuh5xWCXr5cY4lcunTyPoPPtyXJBoMz_GWwsaMTZm2uCuEd4vGmBSrd2qmsVCS6o9nGczdsP9S_pcotqzfVSIu3ThvDjsUwtX2BCIJGPlrnY3KBCnOoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAH7XV989kHmBSDSqDeI1uEf-b08ka2UbdCbFT001PGRoSTZvJTWAIactm2d5t-RnyHwdDdCmD5S_7aVuli_WTGSnrcszqOWAQdSkUOvpxHaX86o8y2ftOLIqyCYcIGNtoOVnWHkh37espFib_hWjAwosVSIrtwFBDgHVI5ldTaSsKMDln-HtIV1U-xM0zh0bSwkWRf8nannCN70WtRuAjbP4yI1jhDVcUPFOsif8n_TyhUAOckA5EUS4LS53G6xh0pQkkUAYQ5NArEfPYdR8ZMrwl5p4je4OIJIMC5FRkKbPne9zQQTAdY4pM9KMnDiLGrgbVVpthSc-VlcRgShrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT2p1iPsLQReqnI57bovoxJKYUVrQm3VCtux3AGWQ5jPGnatdAbfnFtO0nFiQeJ27nIIYxg4oCdCcRTEBzneIgIWYGhyo7OaHxXW_z3Pu9NeZ7fa7i27hTgYij_9UVlUeFHmr7dEiKEGlboAYncuSdShukhR8OJ_n8X3i-NLyT3T5vhWOi6nWycaN4Wg8EmlkQybo9_2Ark0RaqXSO35-EgUIyd6R9cu4bFTaqAuMOq1T6R3gx7Zey7_2uJtYQa9DKJqlFe6Uul_sivmai7mXk_LfjC-JPu6tvwzqui1aZu8UN3bCZXjhO-oU04qekfjstTF6u4cfLScXl4Y3I2WnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HBkgbNAlhwnAYMsNf6Q263hNrO6Yu3xAJIjXIcY-W_EwX6nIB4dpCNWN3gENfJMUmFM52z7y1zU8h4_vZXz2kgn1ugQtj1FZYy_hOROAppOwG32zcA2mmZpEdBv7xrYVLOLGNO5NcLAOlDisUpZCqYsJzP7HF-CaxySDJwvEQs1wkKVdPoDsX77QPJnyfKxZZxb_V7lGGjme1fisfs5UF9d5IfyXGTZtxwI_gTuDVRa3ad5_3kX9eaaSSuL4vmaYi4RlPccbKC_GAtHcdH4PS_pO3XzQ3sy7AVksrj0ZAKvHgeoaCUo9tk6A-ZcKaq466dKsGlkEtH8B8Qw_Xg3uMQ5Ol-MUlN3cqWsN2ZCwHjnIfkQqeuVBQC388TNBp2I5uQG7MA2tb9Wi1sWxH8SwI5QdqQ3zYpQjSiPULjZhf2Z_ycSKoWeG2rLohNGNyTuzy9BIOSQnG0p5vaUSGW0c_NCETfBrUn1p7R2W92V9Y9ESCRIyhqsKRJXr_kVoW8hX1W0rR-eOGHOoYt__tDQC3EIZUo8Wq-qBNy9P5dQ2j0SPOZxmUyFsM1mq9tbvE2NMh_etdQCGbZ2AxmhrWwvL82Q5qac22nOXaAaP70Ad7UaJiKj-fYLUq0V86kQvsFfOv-B4d_6XxhhkwVyt8yl_b6XxAKYzK_Uy7rFZmv1gLVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HBkgbNAlhwnAYMsNf6Q263hNrO6Yu3xAJIjXIcY-W_EwX6nIB4dpCNWN3gENfJMUmFM52z7y1zU8h4_vZXz2kgn1ugQtj1FZYy_hOROAppOwG32zcA2mmZpEdBv7xrYVLOLGNO5NcLAOlDisUpZCqYsJzP7HF-CaxySDJwvEQs1wkKVdPoDsX77QPJnyfKxZZxb_V7lGGjme1fisfs5UF9d5IfyXGTZtxwI_gTuDVRa3ad5_3kX9eaaSSuL4vmaYi4RlPccbKC_GAtHcdH4PS_pO3XzQ3sy7AVksrj0ZAKvHgeoaCUo9tk6A-ZcKaq466dKsGlkEtH8B8Qw_Xg3uMQ5Ol-MUlN3cqWsN2ZCwHjnIfkQqeuVBQC388TNBp2I5uQG7MA2tb9Wi1sWxH8SwI5QdqQ3zYpQjSiPULjZhf2Z_ycSKoWeG2rLohNGNyTuzy9BIOSQnG0p5vaUSGW0c_NCETfBrUn1p7R2W92V9Y9ESCRIyhqsKRJXr_kVoW8hX1W0rR-eOGHOoYt__tDQC3EIZUo8Wq-qBNy9P5dQ2j0SPOZxmUyFsM1mq9tbvE2NMh_etdQCGbZ2AxmhrWwvL82Q5qac22nOXaAaP70Ad7UaJiKj-fYLUq0V86kQvsFfOv-B4d_6XxhhkwVyt8yl_b6XxAKYzK_Uy7rFZmv1gLVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
