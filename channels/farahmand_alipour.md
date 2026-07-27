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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 22:22:38</div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGrnjk1HjFh0sQjWt1erjgerVUKmQwtCoOrtugTug8iBR0lte3ckwy_LfEktgD47Kdjagkzdmx-lmYYUCUyaTJDEFc_IBlZQxp2Ld0OXLW7o5_A-a8aYLU_IJ7RLpxzD-8EqeGHmIbHo2NaVDcfoUUGcapNMbnNUEKxy23ZrxcvHdUfwNNICL37KwYamjdsdPhHsk2frJx6EE4IfyAe84xk-NeDhA_QpKGJ7eZSDxPerT9CaZ2SLjkGnG2BNoylFVHHXplAVSrs1lC5QsAb4GWJLA1MnUAIj7TIkiuqneBD8y80PDF7UVAZ7O5ZOqY7PwO4ieUgX-z0_HurUmVhdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKZez46Xn4GI-SoA93oRq_kFbqKOx0FhD07p24HU9Yczv9sF3dSWgZP7hsZseQCXO5QKHI-cwbK4-Xhm7GCrz-xiB72zkRArw8zvULvhnW9-fVXA4OGqwPeenPm3cyBEe0sYCqmzzXU0KzjVmkmK_abxp58aZM40lN15bJlnzZlakqpsOXztFmWv8s0ClZj4fk54TycjiPxjeSoJ8Jx_i4Bn_ZRA2KFGKI-YGY5lJJ3FJCSqsc4qVJLZqIQ29vVuzZg9oxrWXawFVWqFkY_-U0KQ0Hl5I5709E_TENYb0Pbe2_NzBpuNA3fmjnYSkkS98oBJoDjtZyxNudnuj5cGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbVM70X_5_B7MbPQQs9gr8NsBiRoMGSEHdTFwlvfMy0y0W4ZStcGrD1IyTaIv3OLMU02GobSzguligzXBg2r0xyOi03HhLJISSbRW1j0XNWh-0n8UPiEqX6cj31FjiEFEHwTUkNHMvmLSEjTbERZqu_GqEpPLhKHfKDZowkYC69DMSQyyzrDtTnsWnUXGjvrOQ5nHP6_THjDyfSUc5cWeccv4Tvb4rz5LJlX73ijolFhRLbDBCYD0wyIOTz-FkwhddfyeCej9xL6NCOe4X6SyWWthLeBuZ0TKMrEBUuEXfOxfJ6F4g0APziCA9_nPaoud2nxPv5AaBM41aFnsJF63Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4WWlBDb9thHJOZ5rWxxAv5kVzhiUHylLLkgG40CFirbzXye2Kb1X9V20QK00aeTRjzLzPPo7Yy2qPkg_NyA_zbZAgE3mj34xN-5pJRKf16NErXIHR7YvmOKwTm-FDlQRQd3gmYZVho9Yl9AeDEa7aXiiZHddLyEqEJpljYq497-mpmF3TBPIBQ9DqWobA1bSyYPO71jvkY5FxcdqVsD0eYOqMIGohcrNOVmqrmbQ-PRGvIhbirKcS9UFuArjIeBWryqel6aCCT5007UcNvhu1CizsNrmW60-w1MD6_JzUxFxBw7LHne-KAR-EXbs5ijoUpiCWVMyW6JR2IBVyZZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wvvz9qBjjstLQ1zSKB262C-I0D2m6ojaT8TOtQpsGJBghETjHzYTV0oskHNMMCGzeliNn3UqxPNN2PNnor8MTur3GNoGjHACuP5xyL7q0k4IoviTVN0T1r59q0mMqgS_tCw908A9L-9GotBCTrQsLhwJK2ZUP8mo8x_rDoV4fhjG12FsfK2Kx6vKHivcsds8rfGj7scmR3Ceb4-erydd8PTSl0Ja9ncaZKUDly8ecg9nzkBbG-8iGbPSSE9Vdo8rqIi_-iffPfQeppkGvAr1F4IlkLOBfPGsjAZ-zyn6psCsVN-giqZ2KRrSvVqzaROGCYNhzby9_tSqA6IZqhdPFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdyvlvYDUpxMbjzXRYuLlBiZL08GylT1waCIeLqC6xdRhaeC6raZHtq7dlWiwJFddhKctWMn-bSkfJjbeCxeMYdXHJ-GTdDVRR8uqdOWAi2_0Z74JHJfCsJRhS3gG2UUsTL3E_ROAOQ6HmVesIGoSlfOZ4jZKgJHccctFOkilggv8rI4iYlNVnDUtHUUceFSLGGp4bRf9rwp-v5ZyN2f7i8A35RqeFqBpTGMiRu76C9elVevsFP296y679vDLd6_IMaPFeVjGPZuEYMdDRlPa72waOfCxbu8Wnk7enRIjBvNIOfn7v2ZZB_6XaDpT_qrVNXrrHUbVG9TP5SiN09tDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=rJl89xyoEuE98qVBYa0G4SBTmv3hiMDhFsm0scb4wDEiXorGW36_DOZjcHs2VcKUgK23YRO4Eym59NIwUAmOlVDqQBM1j8bUnuqkrE8n_c_rDtv9220ip8aSaaUtNvmNqhppRIvPMs-1ESwEEmdC-bUiG-pO-8u6bl2oYPvw5LuzWmuVd2ru-9BU-FYW3qfieFXvK6n2DSKDqJljapbbbAWI94S3PuJm0ltTiYPdr2yvZF5yuDY_VsIn8PS8H0sL9kXeP4gKSaY9YOWiSIKOOnLkaJMTGi7CesLgqgDZuEwFZZs8Oq-zIWnN0FlGw9qJjeEZkf7q69Bca-QJWuCotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=rJl89xyoEuE98qVBYa0G4SBTmv3hiMDhFsm0scb4wDEiXorGW36_DOZjcHs2VcKUgK23YRO4Eym59NIwUAmOlVDqQBM1j8bUnuqkrE8n_c_rDtv9220ip8aSaaUtNvmNqhppRIvPMs-1ESwEEmdC-bUiG-pO-8u6bl2oYPvw5LuzWmuVd2ru-9BU-FYW3qfieFXvK6n2DSKDqJljapbbbAWI94S3PuJm0ltTiYPdr2yvZF5yuDY_VsIn8PS8H0sL9kXeP4gKSaY9YOWiSIKOOnLkaJMTGi7CesLgqgDZuEwFZZs8Oq-zIWnN0FlGw9qJjeEZkf7q69Bca-QJWuCotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip2NawMwbvMYrX9cUPixXCFNJnVf-KWY1kiaNmknoO_qFT6FUGENjIiWjnysrRMVqPFG0-6b8YV_G_jRpIlSpb5aXqED8QpWUbj8KJ_B9-7k2iEmd7GE0IkGjERlJj4597cH1dB4kPeQZVFO0JKZnXPJ-xfyeyXzN0Xa8hw5HzKWD1gLFSgMfc99iZFdB6uwdq2WUV-DJiZEnUOb_YJBijhwlq9MCZ7yzwTQ7GmtmWO-QgfHZq2XesL2DHiZrr0JsWpOutn3Emm5MDLibNcASS1cJSInLPF7xe_gRz5u_4k-tUauRT4Z-73fIibJSPJjdIxij7fvpUOPWfgbdl6Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAkqwGhVgWDd67doVo-rfNRaEzjMUV_JXdFG74qJ6NGzRNwSTuwJMlb9nOEVQFp8WyVuFnX8Nwgrg1F0TbX9wXqrgtTfTOAXIy3RexpQhdPGNVt3fbb4JddzjtS8xqeAM7u3sDMcfxuWrUJO4y2QBCNaQ7xK3Dp_w_xgPz-Ux0xolbgRS42nuAcqvJx9dp3YoSHrw2r7JF73LQNz09-QethmXY3lhQzCnxtcKp2IRb3k6l153-GdnLB3mS0lSEvJYdYMqdxiUSyDVwNg1r2X9NkTgHnK_OErsnQfiyDy-k9xr78XbFHn2zxo8kC2-a7O9eygpTVmT0m4TLXwQmoVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=cHYGgfw2NKY0j9qwGLhQ9H54BhuSOma-VLFkbSltGaEq_7urhpyxwdPPgzBGvxfUj0ClrVTxVD5CqOaQc_CFM7IndSK25MddklllzlAcfXd_Yc2MipUNJs61kVRHzWB7ql-dFZQINfPBJQq0WsuB5wcp4OKsm-txzHCkUoLaHUUHbzdG0Yr_C0WmgEFgcK87AjYk4hGX4jQ3B7KjG7uMSTi1_ibP8klM-zGNchbH9-uTrM6GcpaHxNDe9CViEBD7N1Xs8eavz6qs91GHoZeXr3TlupiPG0mX0um7J3mN_uNf13sm3fh2kBusjdTdxAdDseUdJ2oapvSdy17IyzxuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=cHYGgfw2NKY0j9qwGLhQ9H54BhuSOma-VLFkbSltGaEq_7urhpyxwdPPgzBGvxfUj0ClrVTxVD5CqOaQc_CFM7IndSK25MddklllzlAcfXd_Yc2MipUNJs61kVRHzWB7ql-dFZQINfPBJQq0WsuB5wcp4OKsm-txzHCkUoLaHUUHbzdG0Yr_C0WmgEFgcK87AjYk4hGX4jQ3B7KjG7uMSTi1_ibP8klM-zGNchbH9-uTrM6GcpaHxNDe9CViEBD7N1Xs8eavz6qs91GHoZeXr3TlupiPG0mX0um7J3mN_uNf13sm3fh2kBusjdTdxAdDseUdJ2oapvSdy17IyzxuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvaeB138K-DCSNC9IbNt05wUYOKWkdXRpqmgyBv-Pa-VjKt8sMAUOJjuxtj8zW1FwqkfZxbTGzmJmVqKq7DQK1SyhoRnzxbwFBB1VTW-eKWjowVtMWR5N7yo2OU_NAvIqZCrRFwOLwtoaW_c0XO-KanQrvne2Lf-UqaiZakW_fUOOz-nPSGMlQyr5wqVPBiZMepiv817eXlSEvd4JwyQrYx5mvgkx9bGYSHPwGlznbnbs1mfh2mUhUsZV-8ifyZTckGevarOOAGqorL5Jnpiw7tKQQFqCbJEG1Atq45-e6a9B96mTRtBeVzeF8J5B32oSfhqOfjZZUoIicBHqSCrZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVeez6kEEZ1VLVX3_y7Gsg09bI3HOTe3AFm7vVNk4zxbNPPG2lIbZ-kZbIiWHFjntI3dpvPRo_gFuJ7SNY3BVUyaYPMwoH9FfqGAx2RUwLV3Td3279uvK0NBp8AD_vPAgNNsBssIkD0BUHHL-2kma5XozEGzLt3Fzmw4G6UPb6Hqpp8EM87LYBqrEfRCrxF4-ruK4hsF44KtUY_beIX0q9bRAPKdmirIv9HuU68ge0LN_cZ3Z1K7_6ph3xGZARv75FSH3mzVR10JDaL3sMf1ZsAwKuRXrcEFhq64HyngSO_VTNOhUasyk37uaKfdvO_w-lHkXGkRcjH1ejYsCgOpVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=DDgQPXRfT5Tz38ayXv1ag14vyHxwD8IHtYYBw71mALxbuwG2e0lGklB6r0gsfvzUcIcNaZgQBLfGyW7TaiRajiE0w2uReL4GtLBREeh-KB_rte4t3UsOfqXGoJTJT4n4uFzQI9GGJJLEbeJohJwBa19S5FxzDr18UfCnTGHNzZXwUJ2e8OXJmoCkM_Z-n4HXkXQIaMl-cf8duy6bUizLbYGr151B8UQ-ZTtclTyw3VO_mQR2PxEGYTZrBiF2gpDbi6No88yJqY7QjzjuOiOFJhfS16-tT_rnQ5iLqi08M_EIsCY13y_BXlb54OT1z7euG78Vu57AcjJTiJdkVo-cV7ednn5TUr4O-eY0HOO7GulqFuuMV6evtYR1z93l1ycn-f3o1ZoZ26J3ebgu7cVKBEiq3lJGGCaXorEz7GtXkiluqPv7bNVpFX8CeEXh6zDtq1l2eaW0AyGU0XpfU2ToxeLaz29DOOEQ3buPQZxlIN_ADxpAjyb5RcTjHft2zNnUziC7gHFBoloHjAuUKYU0_XDhmayDjP9at4mhYgHDnhfc4CBmlMyhmL_uGrKW0vN5NotYCsAailQp51LFisdPXp3uF2tbEf0zjhqfGXUVpJITBntbBh7w2Eu6JZ8AQIetDWGW7gEWQYP_fbw5sgnBlNVFfC5YFe_YVaArQMR5JlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=DDgQPXRfT5Tz38ayXv1ag14vyHxwD8IHtYYBw71mALxbuwG2e0lGklB6r0gsfvzUcIcNaZgQBLfGyW7TaiRajiE0w2uReL4GtLBREeh-KB_rte4t3UsOfqXGoJTJT4n4uFzQI9GGJJLEbeJohJwBa19S5FxzDr18UfCnTGHNzZXwUJ2e8OXJmoCkM_Z-n4HXkXQIaMl-cf8duy6bUizLbYGr151B8UQ-ZTtclTyw3VO_mQR2PxEGYTZrBiF2gpDbi6No88yJqY7QjzjuOiOFJhfS16-tT_rnQ5iLqi08M_EIsCY13y_BXlb54OT1z7euG78Vu57AcjJTiJdkVo-cV7ednn5TUr4O-eY0HOO7GulqFuuMV6evtYR1z93l1ycn-f3o1ZoZ26J3ebgu7cVKBEiq3lJGGCaXorEz7GtXkiluqPv7bNVpFX8CeEXh6zDtq1l2eaW0AyGU0XpfU2ToxeLaz29DOOEQ3buPQZxlIN_ADxpAjyb5RcTjHft2zNnUziC7gHFBoloHjAuUKYU0_XDhmayDjP9at4mhYgHDnhfc4CBmlMyhmL_uGrKW0vN5NotYCsAailQp51LFisdPXp3uF2tbEf0zjhqfGXUVpJITBntbBh7w2Eu6JZ8AQIetDWGW7gEWQYP_fbw5sgnBlNVFfC5YFe_YVaArQMR5JlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=LbXX9CQcaLLO1Y8sQIT0GSygoqsZR0qywXzTHiQAuui77KGgBlPyshvISlHqNPd9Bkpe3TbbU5Y2H9L2vQEC_58UOfLVrgA-9SrkF9FaHod9y2KKb12h5DQPcwkFWLi3aEL4n6Z2UDspOIUrHpc28Xwn0mzZxjl3Gx0CIgM-ChoiAqHK8Z5Cwfl5I2UO0ZJTWcKkWUYNcnxQ8voZ4LhAiY7hOG5Y1EOzJMkZfYOAJ4Wq-TBWEOesf87QXn8gWNm-wI4uOr7y-fmAc05odbuWazfk2Gi_nmWlKqpTF-Ya8-YgvdideMkknfj5hwaivy8VFi8XtLZoIMFRttsLBulrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=LbXX9CQcaLLO1Y8sQIT0GSygoqsZR0qywXzTHiQAuui77KGgBlPyshvISlHqNPd9Bkpe3TbbU5Y2H9L2vQEC_58UOfLVrgA-9SrkF9FaHod9y2KKb12h5DQPcwkFWLi3aEL4n6Z2UDspOIUrHpc28Xwn0mzZxjl3Gx0CIgM-ChoiAqHK8Z5Cwfl5I2UO0ZJTWcKkWUYNcnxQ8voZ4LhAiY7hOG5Y1EOzJMkZfYOAJ4Wq-TBWEOesf87QXn8gWNm-wI4uOr7y-fmAc05odbuWazfk2Gi_nmWlKqpTF-Ya8-YgvdideMkknfj5hwaivy8VFi8XtLZoIMFRttsLBulrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9xgfAVVfiCa78qJQC25W4Qdu6xDTmEjQmc2jQNctJZrIrIlV2hxrI8wiS1tFtsQbtmd6e7iYT6s5v6bkfgYRaHT2oiECQ8ogpRONzP0tqU0zmx6ZASGVWPgH7C_YaTb81B9Jnqj5MfLYk-t-oMoU26G0kt7r63ek5Z2A_5-ulK5jVqpWHMGv23ajVG8B_09BSfPee325KVbF-jFlRtLRd9AACSlWN9UzL9bEgtkoDct3ET0VJu-0rKL8FzkNEqNr1F3dN60Q7qg7igYE3BW0-9jc98zjD9R4MO486ZXnXslRwCEwlXx2m4hkNM95f3nABIwmLb0rU3qcgm936eqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=KDzVMSNcqYNTapICCrVYVx10UFtT3z8O8cGnnizsVOM8mH8Yy_k4PX9tWt6LSWedlXgw0cQgcHzDa0Ru1czlb1uACGkTRnNxuD0RQWVdMC1yz9vdI7txcCr4eaEOu-_WhGW7S1RPg-mP6v-r1F_RE2WZ31N27zviTJpae8Z2flq0N7qDiO9IP6gBPOxKef7HTsNWvrOY0sKhYnUAgxm_7UhGJqcIcKsxuqiWHS9WbmmPZExQ10khbQS_UyUXLegZI1l6Ux82SBJxizDUjC0qYuekjOxp2l9k0nFKGniI6bz4lKZXkLnGhZKnMBWY3hapisZl8kueZx_vLO26mESRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=KDzVMSNcqYNTapICCrVYVx10UFtT3z8O8cGnnizsVOM8mH8Yy_k4PX9tWt6LSWedlXgw0cQgcHzDa0Ru1czlb1uACGkTRnNxuD0RQWVdMC1yz9vdI7txcCr4eaEOu-_WhGW7S1RPg-mP6v-r1F_RE2WZ31N27zviTJpae8Z2flq0N7qDiO9IP6gBPOxKef7HTsNWvrOY0sKhYnUAgxm_7UhGJqcIcKsxuqiWHS9WbmmPZExQ10khbQS_UyUXLegZI1l6Ux82SBJxizDUjC0qYuekjOxp2l9k0nFKGniI6bz4lKZXkLnGhZKnMBWY3hapisZl8kueZx_vLO26mESRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG-osX0HcMtH_rObFjXDsD7kWDqkGOc8FaR_9NMGAtPqxz0hEMyoR2TzR18W_YZgGWJ8opc0sBRzNKLw-6tgadCTSSyapKmngPvR9sp-Q0rbC1NIvoUKLQWpwScbaCxRcUIAklYyGPPiHCwb84O4rEsrSJuu_1eaLyfP4lXvV7C2XIFYviwwvxEYt_tVRcrm9ujeIGZohR-pM5sb2X47eBXmgFbBSzro7BAwfumVbQRse6kKxi4Zd3J-ZrETjbO1VH9FlsPnZ6DjbfcDrMa7ygPO8jFMUpzW2i8HTaATWTp7jc9H8IswSLPN21VfuzloucX8ti0KoJLNGioauYTKgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifg-Rb2rR669oLrdSCfEua07xkd0XGOGkxhQd8ovPZN34CTBOFXLHMhMGH3nHThbbJxs9oL-FJL04F6AQ9W4NWXtgvifZvKPwE9Yg6v1dhJo68vS9Mgwtzl2CGQO-y0B61XiTiD7lh2gDx2iONVV-2PniE6S1f_sFZeDq_u7IC58yv1FjBw9EENegWzanPP28AQXnEqg-ZIp7PvXeitpo_JjU3hy6_VtK81VPWqUqZgUSdColwjDAmEz_7ASLaIEbp5zY9xAySXXfG6YIjSO_w9aIrrFV5XYHKt9f_NN8xAdsFbfsqVRxhBlOJaZvXPkw_z-oqJDFh9vre_RjExEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baSHqAAGpnL55j5x0weJS9qldBbnioEjDJmSUQAE68zXD-BkEFfxj7OVr_f_Sza_ZAO_15NQn4cbiDCI-YU8cMnw_Kzs-C-05siHX5o8Ww8nl3T536EHSg-9Bsr4b2Qz-AKNLsyBzLCSmnJJrsBNaqWwfuBdG--o0bp_Od7YAFK5Hl1MjNuHuK-O7OdvjSwrNvaxY9LXooJSEHTrSCgQrTmI3udDNFinbcKZTlMvcOd6r7ag5lHAZI-zSAG2aWEm6oKeS0mXgKx8YrjqVs-teT9ysftFHEgkIrJO44i7Yo8-K45AAHNkihulEPLFBfqHXJs7cbIiUmaGamlslbdjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF3-cJJaVVYu0MjEt9tXCVkdecD8rDRq_vArx8jjbvhSt7rlrCxwbcTpmUie2hlrHS7VMx1LTwKt2n-dOQvYPnMT0Ze3yBfKgDPGhbjVa3G9MzADZbcPf107H4XA4jrTNLQyMX7BldJNHGsgpvTYp_DKEBZ7mumse5M2AGhpOwMRjyOvOOWTu83zQGMFAVUwq5eiDIkODXoebIVxA-3iG7dyM7uyb8oZQ7BXhjTTIXpZa8NOpEx90sQq2kUtakYKzwUCc0QxzRw9egIjHWts5N6Ldk72VmCJ5QLhIIujGlpmlpmyx2xtepGGWnyILlnY2v3aD4zU1b-YL4tVCxj5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifGs-t215D7EbS2AZq_dDFPNgGe-VZ_tkfSX-nytm0pjykOHxhYlntdfw1f4nwRC_bW-sNIUgL3bma5QUJ-MlSuKXq1ojAqwu7fiNM6y0i7Ba9IY0VGAE1Ooft5HHlh7KpXJjUIBy6iSzVEjw6BpMZiiGzygNv6VYXLed_SnlxpKzWizwSez-3_2QB7x3jzFbGV4u01v1qrciz__7NPZC6pJKgOkGDXV5-lT0PCVO-SKuB5El9onlVBMW-0FgIwi2UC9qyeXmWib9bGJocO6DwCu3mez1Ni5Lep3Gwk4Z9ifV26-TmHsdpPmbgfW7WDNVIcz2YrlDHdOZor1_isIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Jop6IlyYT8OK-HG-zPjVr4N0QL0afYyqLAKKNWj7bvFxgHY1kqDS9BCn_MWblhDZmqDh-ybtwTA1c0wUKvnO-KqBshV7Y-Wnpf7zXDjZCw2YBaCDDJYzVNLHXxg4ZSzdEetsY6UmvdQHRqhdQKuaUDee4SWyoogC4gDYHzQ756CK7khFfYK-lPI70I59O2QFnkIfVsnL86bJ9v52Axb9ee0ISdy7ZYAfAh1nCKk17QM2cgeMIBExpR-wkXezzFJDJpwWkW5aFZq3VIAJC2aJ97upDNZOyCcpPSGCMX08boTnrC5rkgLYXlVGlNiSuCn4opJeJS1dA7KQSJ_FG-QWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Jop6IlyYT8OK-HG-zPjVr4N0QL0afYyqLAKKNWj7bvFxgHY1kqDS9BCn_MWblhDZmqDh-ybtwTA1c0wUKvnO-KqBshV7Y-Wnpf7zXDjZCw2YBaCDDJYzVNLHXxg4ZSzdEetsY6UmvdQHRqhdQKuaUDee4SWyoogC4gDYHzQ756CK7khFfYK-lPI70I59O2QFnkIfVsnL86bJ9v52Axb9ee0ISdy7ZYAfAh1nCKk17QM2cgeMIBExpR-wkXezzFJDJpwWkW5aFZq3VIAJC2aJ97upDNZOyCcpPSGCMX08boTnrC5rkgLYXlVGlNiSuCn4opJeJS1dA7KQSJ_FG-QWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhM-oiy8eIKCB-vVUPDGyGn55bTCkA_jJ_6BXB_7HcdVmjx72jtn_TlwgR427PV6hMvHoMhYSEHgyp7v7UnnP8psWkThyWbpgbkH9X5P-bU19tYHbRv5a3XN3PRvnY4HfWLby0TQdCtWPZM4CqOHbzUTWb5v_VHBc_71pnABFXuQ6MZQupQW7uHEv4c9c9pVjnAu-RFe-R9PoGjAwEY8IaV0ZYBDpqtnNEYO39mjEdyL_v6EimHtfapk9_ZMhRTj9TiT9moybc7r32jdgVkZZwEa5dMyzS2eGzj6Ze8GF8WSaMd_dRI_iiuawyb0s7Q10c0tlNoYE3XEfwlzBK5VRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4sdDXo9KTImM4TZChYxFHI3C4YSzhtLWQ7PIVQA2JeRfyL2YuUj-_Xl4NlXCw-3iqujnfS5Q8gbtYn24XNsWrIMJiQBF5kqZ7YsEKnVJkUFmAJInvbmaGA7h8Mkx1efTWVUETKHV50CENVFhfNPfFgCRAW-GLrgslQ7eX8ZBwraA7lviR12aeM0__8DI4S8oJsw1MFp1LVk7obWFj8lNusVVCSOmcJtQ6HbNIxBJxMvjEFjXilx2XKpaifUwOws70ZrQn84NgcUBhL5I7BOFNq_KiEh2cVLlBXct7Cs1jmp24lDoGV5QuT3AtF-V2rV1Gl4ry6mFM0VUenIx-KxjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=bW8S7iRWJCyecwR_bXpa4_JOGSy2JMYLBqfAqYK7IShbPPXE8DOGZ0YkA5lYfQ8lA4LZA3W0_f7U7nx5UH2RsQ9fMioy0qp4D68drNyHZwt3bj5u7Bg5mONWdv7mwvnXT082KcbVboHqaXX-bjn7bbNBmvWZeLtPiHSdFckcqKqRsChmprqu4XbWxiLCYcVArGrFk8ST-WukKXP79AomxkNOVdxunh_LqStfqqiDGU4Gotm0uzshd2OQTRHeAV0DCxb9tuZXza2bJ745BJHHajiLytXj9WLkVKnCguGxrjwOOQNNQaP_Hu02BNQ1iqqxHBJxaSP4Gvo6pfPklVbvlVtxMf9cfTugCkDyySorB5zPvm8f3yTrXJlHM95g2ioQ7Ny-Mpq2BKWWHImhei1LBO7qtiJj2235uXNUD3K8FAqMrV7XSD81YO6uNRns4Jdnw9N_vnfUxYtaOWWjbXzrOOgg5ckCQZMsVu3kLT3AwWXUj6kRNCjkophqIirAodbxtCHCKpeFy-MmTMsrhGcwQpyEECC0CKdXCkkX2MD_DSgeQewCDVdl9lt49J9U7WwiqqvuJTuIUS_fE_FSR1aruUvcsFrrB6nP7Pxkr5GHVe1TfiVwyrLIo8I5H0BO1VwtgWYW9tD5Jrzaj62Q_a-nxv3sfnYUlkh6P8r8QBrCL3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=bW8S7iRWJCyecwR_bXpa4_JOGSy2JMYLBqfAqYK7IShbPPXE8DOGZ0YkA5lYfQ8lA4LZA3W0_f7U7nx5UH2RsQ9fMioy0qp4D68drNyHZwt3bj5u7Bg5mONWdv7mwvnXT082KcbVboHqaXX-bjn7bbNBmvWZeLtPiHSdFckcqKqRsChmprqu4XbWxiLCYcVArGrFk8ST-WukKXP79AomxkNOVdxunh_LqStfqqiDGU4Gotm0uzshd2OQTRHeAV0DCxb9tuZXza2bJ745BJHHajiLytXj9WLkVKnCguGxrjwOOQNNQaP_Hu02BNQ1iqqxHBJxaSP4Gvo6pfPklVbvlVtxMf9cfTugCkDyySorB5zPvm8f3yTrXJlHM95g2ioQ7Ny-Mpq2BKWWHImhei1LBO7qtiJj2235uXNUD3K8FAqMrV7XSD81YO6uNRns4Jdnw9N_vnfUxYtaOWWjbXzrOOgg5ckCQZMsVu3kLT3AwWXUj6kRNCjkophqIirAodbxtCHCKpeFy-MmTMsrhGcwQpyEECC0CKdXCkkX2MD_DSgeQewCDVdl9lt49J9U7WwiqqvuJTuIUS_fE_FSR1aruUvcsFrrB6nP7Pxkr5GHVe1TfiVwyrLIo8I5H0BO1VwtgWYW9tD5Jrzaj62Q_a-nxv3sfnYUlkh6P8r8QBrCL3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=rxN5NaGXjn_tPA--CAuf99VVcwUL5kwABzMMtlCfGsNZxnhq-KW-NyIki7I7Pfe4LbPfYS3lnvIRDfDjhO3hKPlceL2IA68iUbwBVXNZshCwoRCrelU3JgdqTNMYa5FEHA2rmlL4MaDN5Av5GERi4dwRCw0ukB5MUZWp66341WjlDU1rnbSf76nx7hsx1XiiOBNAfK609qgHszgPKAIM0atj1FFZwDahGfSvBIqerSE-QdEJnxlLuh50PUQP5Ht4Q4W0n3pr2Qc-_7PIXeBXXlEKh6vFSKJadIBoEaJ0Lm69HjvIqWDodUHshR0CBWErbSDr9eNhE5xijZZ_Jvyhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=rxN5NaGXjn_tPA--CAuf99VVcwUL5kwABzMMtlCfGsNZxnhq-KW-NyIki7I7Pfe4LbPfYS3lnvIRDfDjhO3hKPlceL2IA68iUbwBVXNZshCwoRCrelU3JgdqTNMYa5FEHA2rmlL4MaDN5Av5GERi4dwRCw0ukB5MUZWp66341WjlDU1rnbSf76nx7hsx1XiiOBNAfK609qgHszgPKAIM0atj1FFZwDahGfSvBIqerSE-QdEJnxlLuh50PUQP5Ht4Q4W0n3pr2Qc-_7PIXeBXXlEKh6vFSKJadIBoEaJ0Lm69HjvIqWDodUHshR0CBWErbSDr9eNhE5xijZZ_Jvyhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KClf7GFNOt302edR-xy74GEFMgAe7jin00ZemqDiLx1rEJrMNyuYpq5ISHqyoGzrKPVWHNZmCrfjc4ZBtG7irwA9BBe0GZAXrwjto9ANvyYPjfVy9xaUijc_b4dFjlF7KVcLde9T6QK4DUR7EW9E8N0wLkyh-Lbk5A7pqtqepxLayiSenGzD8GxuNkSIm5MqhObFt6Yq9gTt7T06romwIylTmxlvYmunNdetG96tv2iH3w0z1TC_hmGFLU_Dda2r2ULfawoGqVfDIp1HkSTYjCNK4nyXA0gFxDtdKeYVEqltyRTK7ynDguQWTDBS2ew9W_eUyJOwX2KOSndgwtjUeLno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KClf7GFNOt302edR-xy74GEFMgAe7jin00ZemqDiLx1rEJrMNyuYpq5ISHqyoGzrKPVWHNZmCrfjc4ZBtG7irwA9BBe0GZAXrwjto9ANvyYPjfVy9xaUijc_b4dFjlF7KVcLde9T6QK4DUR7EW9E8N0wLkyh-Lbk5A7pqtqepxLayiSenGzD8GxuNkSIm5MqhObFt6Yq9gTt7T06romwIylTmxlvYmunNdetG96tv2iH3w0z1TC_hmGFLU_Dda2r2ULfawoGqVfDIp1HkSTYjCNK4nyXA0gFxDtdKeYVEqltyRTK7ynDguQWTDBS2ew9W_eUyJOwX2KOSndgwtjUeLno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLogKLOxvXE3HmoC7HiQPe4CXraDXz6P7eIEMZrQTpvkAibN9j_qhID35UOt7ImFD8kMhFazO8_fZze8X-a-748d7hhd-G3m1qyqbYG5ofBs0Jv4cROdyb1Z7p0pJqNidZ4ERykxYzXja4J29hf5z5NS6WKI7cqSEV8psJtPMLNWyYhUcBhB58dQqYjME4AXqyG-hJyQotrkP-khzSdcza1AC8MfhCfsQshQhbFAPiCTTbxo7CjUhMueO3SWIe9bux8Mg7GUJTs09BCyBXfFoybWRH8LGrWKm5e3CRcpaF-9NJHWHGR9IcxRMFxiytLCy6NgvlNqwtFeriqX3651bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNgUP4J7DFI2xFeVNmOht1aaOlB8B72GA9UzumL5IXMEYQfPibjJQr6Gwv3Da-7j0rFshi5SSDAs-iBqiaVwVusX7N_jKRTiq9irk2yq9MA7wsLudQDoBRw1mW9aePIVSUF45fEO5c34j6zESAcyf_lzphQ7IaOLWopWhXFpBOV8EWIrFFvJ2_NFAoNU0qMfPAmhiPWapoFC5h04B4f4dPWvet-yMmLSsvOl-xdUgBQ97BRrt-J-eC29K0JuwOgLgXNlHGQ6Cisw_wJTHlY1_ml6gJ5Aivp3bLhFcB88mesOpYqpCtrbKY1SkXyrSuMEbwNbjWvQiWMmCJnmGqLu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNchx_0xGez-AwSg9F7ncUlzlgRfr47c7SCnpPtunGyat3jKomfD7xUuLLBm8m-cV0CveQEGIbsKZ7uwcLTAjlZ6pQmHWLYZkzsRazMqKZKHcQadEML6vQ1Z-ozW1EOY1-m3c7bUZo6iuuJAfwAj9xed2vsyWyx0u_-kyxy5yuqAs9ZqzTmZxs9VLbzUe7mClOSdA_I_MJCbI6inYzhRYwGIH_nz0PzFfWSiBeY_Vr-zOEQRRNxYWjbT-SHBMZTYa0NBfqq53TCRAPH0kC5oXu4LkR52egEjruPliXieGNdacJBEXqutasbSJN2sc9JwaRg5_TH6etiDYviLWSwH0Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mH4eKjQrs4BMdh7IHOHgcKYUM6jJCgLXkWv7F6W8ADiEQ23zpO0M5CBnmA2AkM_gZ25oPChaWrNXtZ1S1b7AguY6Eqk4ol1E0oeaeku5UceONWB3qzGHdt3a3ODnh8SMWU_BzpPAatTnQOxT5QyDDWqAbjG-4klhTpX9e-zhTPbfyrCXIWgeMKj_T-OP21JMkFnXqTQh1JK0ArR3pN5W2ky60Zaxc12oe9WdkaZUHKSw80hoallRzjjw1yRQR0liqxoo1Q7rCiOklBSIOMNbiF7DYCKsvZfbZTa03b7AMWTwsKo-xB0GWBHy4o8vnwYtGptD7JSvF1esFnftcnq-OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mH4eKjQrs4BMdh7IHOHgcKYUM6jJCgLXkWv7F6W8ADiEQ23zpO0M5CBnmA2AkM_gZ25oPChaWrNXtZ1S1b7AguY6Eqk4ol1E0oeaeku5UceONWB3qzGHdt3a3ODnh8SMWU_BzpPAatTnQOxT5QyDDWqAbjG-4klhTpX9e-zhTPbfyrCXIWgeMKj_T-OP21JMkFnXqTQh1JK0ArR3pN5W2ky60Zaxc12oe9WdkaZUHKSw80hoallRzjjw1yRQR0liqxoo1Q7rCiOklBSIOMNbiF7DYCKsvZfbZTa03b7AMWTwsKo-xB0GWBHy4o8vnwYtGptD7JSvF1esFnftcnq-OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR4w_wqTNk306lIJJRI7fnTtdMFQMjQoc_Fjc4tNsTYVHyo6mLB3sI2V5nJFRp1-ef_6vOZXADlf0XWAPHgGHEZCeqSVT4GoOVCQ4rUtuDdzRk8daKKWoW2bo8jLeMH4_2oZMoFH2YH1cCNbfBDMzckfxwk_5TV1CZbnwo_gfK0DosYqWayD6pmBmn2hUrVv3no0Oo7WDqcZvKViSRBgQWPI5WZYldlNp5RJaQlpZJqb1hhWiyLhRBzXt5GeJCI8dIQ0UJDfhijE6C_tijBm1l3kzptxraPvWpw4TgUyGVbIYGOi1EHsBO7YrS8rrugahwa2z9lSGsY4OObXmPYpSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/me1AlT36oY3NWj32AMNEwXSz12u-XybDaq2xqOs3wAOI2XJ0BvGDpL97mNdzDcx1METw1wBZDKfa2UYYoJLVgS3pT1XupNziZ97Im-SjNr9zf8T8h5clD_do16q96_WDic2xEUPHvl-c9a4qAPQ759uXj3FX9s0yAAGxc28XvQUovogHA44R1pe49WqzNm6RvJjxDoBNbTHbo0OmM-rhqfvlGAQFUJlqJ3ixFfUT5JXBxMEI0F2smPLMha18Obxvsp3aRDmTzzw-NA4GOa3ev9pdkXM4ig48Yty_Q5ZHgSClVuapWjWiWL7Kl8M32etJev2trOmWyfG7I8sUC-5npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LV5T3tdffbrs6reVrWI-Zls07EZKDn3Nxx5vjRd450S-58-tXRoggSXzDquCig9xp4Wtu6PFi1fId2vIKWSi7aAOkILP1qu7WuKbSlt0XEknjl57PfKkYsi0r97SsfJR8kezc7NUJI1xRBd_qSl5IQBxX5Fmk4ervXHUAGj8UAeesMFiW5k0bvpsALpNPTkBIBO0tkWIm0IBxj1TcVCMqfc4RdjHeMNxtOADhaufzewQzFmxpAzedi43CVxW31O923XxNWNHDFKdW5LuXiOEtaGDcDQ1RgoG1E-ek1G8P-4rvfhbqILgos-s0aerAxaOCr4zq-ITDIdQT09e0rRsUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNEKR-lLkrb_scBwpI3prfhhzB4xE4HCJ61olY26S2-yMPjEiqwBcXmq3PWEZAObk1ru0Aisa2TVTXsCqJX_HWdXiD_LU7hA-Sndg6kGEoD2MIsKy6WXZ6GtBmWjprMLinVMl3JpQesX-tiAkYkYIu73DbO58Y6hCc2Z_n4uGwPdTUrYDpnKrqf3SfsaeTmOkbEqw7NI4zqQH_CqvEiEnjFaClJPtjCmhJs_9-xnsmKrSfZ1wEzKj3eFUxyYOWtZnLhTjB1GfWXJqUk_vxOgDHMyGNR58GJsfeCocyv6LO748UIMGE13qbO0qfKfnHhUlv7TlDA_1wYElRPRj07anQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=GjGqTFh9ipbBf3Ra5QH41paeCGHp3zHE48uTceCiSBFlE4eVq9H1kZ1c7fzcP-776C0NTFxaaxUEgQlwLFxXtxGDr8Tz1azO82k1Ry8YXIViI4cbipeMZCJxmCKh5ssZ8jFkSEa42uPwFaB5iHHBEWkGtM6hBdVqpmcBpW8wJhxqLk8jBqDSG4Fz7csEFAdiEvJhQKwFyWKmYdD0UadJSYHy6JavIJO2O2bkVqVc7vwiMJXeJDskX1VUlthuG48owukwxf85WAauYmFtpNkwXdCO2PjnB9By5SJUNsE1IqFrQ46PNyioSnk1D1kWJmjNeC_0R4uBTTewrC2AgezaRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=GjGqTFh9ipbBf3Ra5QH41paeCGHp3zHE48uTceCiSBFlE4eVq9H1kZ1c7fzcP-776C0NTFxaaxUEgQlwLFxXtxGDr8Tz1azO82k1Ry8YXIViI4cbipeMZCJxmCKh5ssZ8jFkSEa42uPwFaB5iHHBEWkGtM6hBdVqpmcBpW8wJhxqLk8jBqDSG4Fz7csEFAdiEvJhQKwFyWKmYdD0UadJSYHy6JavIJO2O2bkVqVc7vwiMJXeJDskX1VUlthuG48owukwxf85WAauYmFtpNkwXdCO2PjnB9By5SJUNsE1IqFrQ46PNyioSnk1D1kWJmjNeC_0R4uBTTewrC2AgezaRIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=GEOOpA4wPaS5jxkmUrN3wWX7IXHTItz9qiyQWOiO16lxAEcE45MTB_G1hLte7pIqJ0j4d5gKzlbxeMFLyhCUlRcnCL3oVLKbBXsitiLzyYsY86PJApBJFUn13SmQgwXnZtukDX-nLgKTJ_xVk8_ybidkvIb1TnTaoDBYzrYlncir4OI6gKPa8UD_6Yfv8EOl0FCiE6iRKebBhGfh2DIJyEzz2pZ3B6MMuOX72fm5184X3pffiZn2o6e0YdxMjcbinsGQKeV6F8pblkO7GglaE4DUOvSa-QfzO6zVnG3iReFIzGKpZmjrGPrCeKO-7J1Avy16cMNSWmm50nI_dVcUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=GEOOpA4wPaS5jxkmUrN3wWX7IXHTItz9qiyQWOiO16lxAEcE45MTB_G1hLte7pIqJ0j4d5gKzlbxeMFLyhCUlRcnCL3oVLKbBXsitiLzyYsY86PJApBJFUn13SmQgwXnZtukDX-nLgKTJ_xVk8_ybidkvIb1TnTaoDBYzrYlncir4OI6gKPa8UD_6Yfv8EOl0FCiE6iRKebBhGfh2DIJyEzz2pZ3B6MMuOX72fm5184X3pffiZn2o6e0YdxMjcbinsGQKeV6F8pblkO7GglaE4DUOvSa-QfzO6zVnG3iReFIzGKpZmjrGPrCeKO-7J1Avy16cMNSWmm50nI_dVcUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=RjbqvnU3pEIUY92OMildaYWZYnI2Nbh4XdGmWwlh_eBwun66giL7PsAzCsSFDZSl8_us3ztQ11LBqm8zXuHj9qajxDfBjyU5YUUMna3WTyOz8hCqHM-wzhzM70tVob9WMRWv5klWNBcHjDR9ft0SisQn4NPaPMOZF6ShsrTaQXITH_GUtsssAmwbZquPdxylVeNJoRva1dt925owQz6ty7Ge8uSQPmYAasXQcsz1GwMaWLok-AaXcFG0lQQcxTUsbrjdqAtJsL40a3uBQPwaiavNsM3mZd8v9VJtXZ2oUTIUtSyPcDfy3BktaO-eVcvpwO2Sp4GZZvl6bdVq-zNSJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=RjbqvnU3pEIUY92OMildaYWZYnI2Nbh4XdGmWwlh_eBwun66giL7PsAzCsSFDZSl8_us3ztQ11LBqm8zXuHj9qajxDfBjyU5YUUMna3WTyOz8hCqHM-wzhzM70tVob9WMRWv5klWNBcHjDR9ft0SisQn4NPaPMOZF6ShsrTaQXITH_GUtsssAmwbZquPdxylVeNJoRva1dt925owQz6ty7Ge8uSQPmYAasXQcsz1GwMaWLok-AaXcFG0lQQcxTUsbrjdqAtJsL40a3uBQPwaiavNsM3mZd8v9VJtXZ2oUTIUtSyPcDfy3BktaO-eVcvpwO2Sp4GZZvl6bdVq-zNSJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZMXwkNHM_2njwt854zlHj7OHRrveRwOtQKtxKypJWPdz-VZWo7mIYS_DllZ_dOCgzRtew0Ezmz2C8ONnEMFSpRxsoTZmmhIjayabWgZKxkhZcsQDhemEFR62TEDxfylw-Rnt9CZ6jlipufLY9918bFAHe4C7cs40KJdtq_gUMKwyKUzDPir1lTcfASMUoPEbQm4qwMVLo-oEI1Tr0_fQoET_vk3U2XfqFysNt5v5QSAWp2NW7filBjMvy3N9Q0MbarOMjj7LNGrlqlm60LXpg4XK2IX0eZiWXSQEcbbecZvqSkwzRrkatrp3pW6VDs0KW5sHHjtoMkdWN9sqCP4Xg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=njK1r1IpaPC5y7LW0yo4LFBmdaoP-tFjDqfLTFMmKSqobSZ_zT37y25JDol9xpMMYtmsd7aLaaVVwRW1CvQIDb_tzYAxXj_rSbbIvZFC_EOB-Wx6sDxkPWd-RH4ZgCMjrATxYqVG_NCt22Y2MFEc4tf2jKyQHEBzDUM1iayivLf0Lwue4bmhe14kG_QQrwnvwNkjHaxllNPsdn2t7wnS2GmjmzBXaGPykmlUrDsuLO5L99pqb1W8P3FlEJa40IBpxIqZI8R-SlcOHUG_JSKa3sSttIq2DvqVy3gGsxfICLrPpNvRpCRQh4xMTYtdR7q4jAeKtrJd_OONjvuRG7XYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=njK1r1IpaPC5y7LW0yo4LFBmdaoP-tFjDqfLTFMmKSqobSZ_zT37y25JDol9xpMMYtmsd7aLaaVVwRW1CvQIDb_tzYAxXj_rSbbIvZFC_EOB-Wx6sDxkPWd-RH4ZgCMjrATxYqVG_NCt22Y2MFEc4tf2jKyQHEBzDUM1iayivLf0Lwue4bmhe14kG_QQrwnvwNkjHaxllNPsdn2t7wnS2GmjmzBXaGPykmlUrDsuLO5L99pqb1W8P3FlEJa40IBpxIqZI8R-SlcOHUG_JSKa3sSttIq2DvqVy3gGsxfICLrPpNvRpCRQh4xMTYtdR7q4jAeKtrJd_OONjvuRG7XYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KTTO-7IKxqhf7GZwZEDttbNGOBEkAjWiGQQ40jvHaY8EzlFY_aCFx8JaPC0ovxEzyhm1Il0aJ_1rSFpdaZ7InDb8snjqPqpTOYYnM2aqfkycWjVkLW0fKn0kmg4E8WaU16fACIWhvZVUh-_LGXZ69WrILe1D_AwfQybH8pWblhnloWeOY4XfnySuIchq0aRn_K5z7aVTXDZB2iTA0Pi7BS1QcW-Me3W3NqHsgON8Gt4rTckH3kHsddwzKiTwEQm-p2lY9O0KOKgfLrpTWcGrKS7Bj76E-5Y7izbGMEe6Uyvs_Pd1wHxLYO_eyWAyz0WZpdJ4BUze4LY6b2sELOSOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KTTO-7IKxqhf7GZwZEDttbNGOBEkAjWiGQQ40jvHaY8EzlFY_aCFx8JaPC0ovxEzyhm1Il0aJ_1rSFpdaZ7InDb8snjqPqpTOYYnM2aqfkycWjVkLW0fKn0kmg4E8WaU16fACIWhvZVUh-_LGXZ69WrILe1D_AwfQybH8pWblhnloWeOY4XfnySuIchq0aRn_K5z7aVTXDZB2iTA0Pi7BS1QcW-Me3W3NqHsgON8Gt4rTckH3kHsddwzKiTwEQm-p2lY9O0KOKgfLrpTWcGrKS7Bj76E-5Y7izbGMEe6Uyvs_Pd1wHxLYO_eyWAyz0WZpdJ4BUze4LY6b2sELOSOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=aXD3P_PY8CUhA_aS8iPZFqw6NEOB3d6_crCfHe0A_IRxKyGVqsHhF8EjWNU5mf8C_CN5LYma7PJI4aXN-PusByB48kQLM0qYNaANSRf8LcHwrBAI7zv5JwGfsI19yKMpLoUDpyIJHe-W6QdFv5a2qoe49lo4-f_A-wsCj1tjP1x-ZZmSP2L9rTpbroqufgm7PH81MrEW9Toyb5GEyZ0KQpeNqpoF6e_oWnfDmBJIROGq1z_cUJjEEbMXCzSZguGITZKnFnA8xEogy2cC_11hB5D_n-PQTRVLVr4CEkmVdkXoH5prVfL00OT2I2vyRIsHdDexCX5whRS2zXdwCZlaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=aXD3P_PY8CUhA_aS8iPZFqw6NEOB3d6_crCfHe0A_IRxKyGVqsHhF8EjWNU5mf8C_CN5LYma7PJI4aXN-PusByB48kQLM0qYNaANSRf8LcHwrBAI7zv5JwGfsI19yKMpLoUDpyIJHe-W6QdFv5a2qoe49lo4-f_A-wsCj1tjP1x-ZZmSP2L9rTpbroqufgm7PH81MrEW9Toyb5GEyZ0KQpeNqpoF6e_oWnfDmBJIROGq1z_cUJjEEbMXCzSZguGITZKnFnA8xEogy2cC_11hB5D_n-PQTRVLVr4CEkmVdkXoH5prVfL00OT2I2vyRIsHdDexCX5whRS2zXdwCZlaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=rDip1Eym70sIv5gJsZQotzuOqHJFOU34rXydbXwvu5i_MM-Lk7bUmqO7Mp0pC-9_eUjwuq_-xi3c5QipXsnaxrcR9HE5ytPSApA3XJukAhKXzDbLTk9l0aC7p_N3ut71K499Jh_UWfPlNmSuWtDFb0r0mrzJ4Z_gUS4EE78J18jhtxyEAYKdwf_3iQKz8DL6XhuJVBn-5yHy2x1E7klSoav9Q-G7t4HvSE0KqqTnesmf8hRrbcnrZ-gEEnyD1CNNIJ8BtQQ8_vvOXQpCTtmHGdyikm6sF_TC7jfImICFusMQ7lB4j_iytRzhvcXpuzzimjg-N0ev2ooBWiO-E37PwEYf_JLhQ8L9y2nJYqLQFmdYGvbeVQC5JB0ghp4D0OQ89nHGZ_GBj9vIE6lBqJfSnD0oV1RYo5FZQf-zOkcc4rEcsw2wk0MMgA7zy_pEqpFtG_oNZHQyxOjPy0HZdrEk38Vs7WzmPEKgv5pt7IE3zlLDKjZorkyi4lT_RzUALnu-EZJIA3ImtehiExi9AsstHQAImX6EnLEWU7yhTaT4NwxPiNYU3fozQ3ghpxGvz3HZ_zHbJmev3Y3_RobLyFzFkQLyfUIrvDjy6IuI0aO1PjJLuFZykMv2n6BmlDCxLD3jd8dhCNKKQvlROpJ_P7HvU5xJCtj-6tGnHn677oVigJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=rDip1Eym70sIv5gJsZQotzuOqHJFOU34rXydbXwvu5i_MM-Lk7bUmqO7Mp0pC-9_eUjwuq_-xi3c5QipXsnaxrcR9HE5ytPSApA3XJukAhKXzDbLTk9l0aC7p_N3ut71K499Jh_UWfPlNmSuWtDFb0r0mrzJ4Z_gUS4EE78J18jhtxyEAYKdwf_3iQKz8DL6XhuJVBn-5yHy2x1E7klSoav9Q-G7t4HvSE0KqqTnesmf8hRrbcnrZ-gEEnyD1CNNIJ8BtQQ8_vvOXQpCTtmHGdyikm6sF_TC7jfImICFusMQ7lB4j_iytRzhvcXpuzzimjg-N0ev2ooBWiO-E37PwEYf_JLhQ8L9y2nJYqLQFmdYGvbeVQC5JB0ghp4D0OQ89nHGZ_GBj9vIE6lBqJfSnD0oV1RYo5FZQf-zOkcc4rEcsw2wk0MMgA7zy_pEqpFtG_oNZHQyxOjPy0HZdrEk38Vs7WzmPEKgv5pt7IE3zlLDKjZorkyi4lT_RzUALnu-EZJIA3ImtehiExi9AsstHQAImX6EnLEWU7yhTaT4NwxPiNYU3fozQ3ghpxGvz3HZ_zHbJmev3Y3_RobLyFzFkQLyfUIrvDjy6IuI0aO1PjJLuFZykMv2n6BmlDCxLD3jd8dhCNKKQvlROpJ_P7HvU5xJCtj-6tGnHn677oVigJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=k4SK5on3gWhEEOHOac_cvNo2BeDewbGMrwVsv4U2IgN0uCerIFlmZ1av9Qkqg7bTrhVXf_vDCkHk-EdRWoPM-Hgar5-HDtBg8MhVUvB1WBtUYEEYc0x0BiheZcw589sg6eN-7f1Ru-GEhgppxo369fXsv5vXpv7igTH9mob7v6Rr6BXIsdXVHUrwAW93M88kFUVzGEKt8KhUA4UhcTG538wI-nASOaCDNZ4CUR9FoGA0Wr0Kk4kOWkzRg_yRYSw1UViD7PXQTVgQ7SX0TdtNx9E6ybQCCI0wgVG-sxH3z8BdbLx78vwOHDPUupGxxzROlDXidX_QNQRK1wHd6XOesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=k4SK5on3gWhEEOHOac_cvNo2BeDewbGMrwVsv4U2IgN0uCerIFlmZ1av9Qkqg7bTrhVXf_vDCkHk-EdRWoPM-Hgar5-HDtBg8MhVUvB1WBtUYEEYc0x0BiheZcw589sg6eN-7f1Ru-GEhgppxo369fXsv5vXpv7igTH9mob7v6Rr6BXIsdXVHUrwAW93M88kFUVzGEKt8KhUA4UhcTG538wI-nASOaCDNZ4CUR9FoGA0Wr0Kk4kOWkzRg_yRYSw1UViD7PXQTVgQ7SX0TdtNx9E6ybQCCI0wgVG-sxH3z8BdbLx78vwOHDPUupGxxzROlDXidX_QNQRK1wHd6XOesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=n_4AkZrr4PfWDBOMMrHHZmeao6lojzfUYIDYIQExKeBJcqSw9l2AVGmJ9eYeTPzZQTh-LjduOl5uWpYBh5bTAhBX-tx-WyiZ5pA3WimkgtbEXYdUfAqolL4ZJFk56-PaBkxfb39xDB4rX3EbMsl5jN5pkkvpYEdzKBCaQ9sWIs20jTvtrGpCqQzb-0kuWmYwjHLUVrN_p6fZtbo5qvcGMl6uVsttA781I2nQWPfJMQJ_4YE0wOA59ffC-i6Z7OxkFoWPAh1eNzLxwg9MsXn3y335mOsPuVUKQwUSE2zVrTRy5S2cGX0vh9yEVgX3j1xrvK--UxpZzDq8mKPk8AtnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=n_4AkZrr4PfWDBOMMrHHZmeao6lojzfUYIDYIQExKeBJcqSw9l2AVGmJ9eYeTPzZQTh-LjduOl5uWpYBh5bTAhBX-tx-WyiZ5pA3WimkgtbEXYdUfAqolL4ZJFk56-PaBkxfb39xDB4rX3EbMsl5jN5pkkvpYEdzKBCaQ9sWIs20jTvtrGpCqQzb-0kuWmYwjHLUVrN_p6fZtbo5qvcGMl6uVsttA781I2nQWPfJMQJ_4YE0wOA59ffC-i6Z7OxkFoWPAh1eNzLxwg9MsXn3y335mOsPuVUKQwUSE2zVrTRy5S2cGX0vh9yEVgX3j1xrvK--UxpZzDq8mKPk8AtnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HabrIn3GP_U2pRE3wns3rYY0KK8aAkgmunPk32uVZMlqtrWF0NDfgNQWKlbWQUvioyTYjXuADU5CD2-VM8tdpq_nVaTI9KwSPrMPYs-uOUpZ2AcVLSLoCRyUdwmkr56_AnwIzXodMHW-nMpehnDzv-kMl9se5pMl8yDfqIDf4sed_Ms5akWRo5KGYbUxrzjZbLDB3WUqVGlo_d3d14xpLXx_j2m7h8Fn7f1fuVGMPejCBRRBjcoRDTkbirgLIJ-8Gje_kzSrf9WR8bunsdwNS6-o9UIyEuFW_0oopc1ZdMrRjH5M-nXypPRF27ilgTpU1gea0iqmO1Wk1NNaRHw-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uASVC0aKRw7Vx429UMNvqj7pqOfdcj-31fAXXt-sVn3L-Itn6TDGtd9HANyqxapZJJasS2fXRxWv_j7Jy3Nob76W7A_njJAZPXOH2e2Ex2dI6ZVgupkLzhMJiC2sB9Mpsh_skmYbTLadHdATW55cAaQVA2rZlp7q7QsLPGzATRZMo9NebuWYpN4SS0uJDuIyYhwgzgwTSBVk3My4kghDiNZix4LxQ-fqeeCp5Yb_rE82-gNVPr0_zn7yewszrtPxuJeuzEhUvZlw67rMqF5YvJta21_8xEQ43cgk_zCHzBa_092VAyXTpC2llt2MHVKY5GZHLQBSHkndt5mp_7Bngw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=BTuutCtHu39Rg0MpDArLA32rINU0qqEtYJGpbQqOHrI4pZQ9kSoKVshkLB5On4M_hX9C8rdt-0HaFEbyrJndBCK0mOpnARGEeZTZZ07UJbIKkcS0VnK6wYCCpY84hOBSmUhXrSn52nCCgBFyzFGLzK8NMQ3B5-AKYtYQbScGkp9eHUxBXMc6URFfNwN2LvlRF_rMqQZaGI4epBJjv7xdDUKdv2fOi94nKhQJKV6vdOISfKVziKJqVwWQ2_b6O0s1u4cm16Wq_NQuIAcj8o5UKdCKrPEJm6u-cjcNLBMJ92GlMpRPaMDTsYwhLQ6iybTkzm8KGP8g4MElGDRCGjoTS32sKiL6D6XSfwUIF4Sy0fwVTIrk0wC9Sf_QCx-TPzsj4VudQvqJs34nF6arkl4QQJ6ya1lD05nHdb0VSEPQxjoPjsxT7vnDN66Bt82aaZVl7a2mxOSTwtYwoNVJR2Ymrukp5vlusXiCRE8Z3x3wRCZP55EPRQIkapnpJOcJsVsnWfH0BAQsSLv9C0BmbCstm3xrSaBpQ5xNUYxLwyHFwARK--Ovn0C_IgpssGWKwpXtl3WV5NSNENBSN0dCL_YZlw-d7Hbbk_SN50ReU3SPFFKPLB4L1Bgg9jCQkGBEsjDMVswDUIbVvjKdrJn4_dEpsNWwncoKVedqWxA4b7EawuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=BTuutCtHu39Rg0MpDArLA32rINU0qqEtYJGpbQqOHrI4pZQ9kSoKVshkLB5On4M_hX9C8rdt-0HaFEbyrJndBCK0mOpnARGEeZTZZ07UJbIKkcS0VnK6wYCCpY84hOBSmUhXrSn52nCCgBFyzFGLzK8NMQ3B5-AKYtYQbScGkp9eHUxBXMc6URFfNwN2LvlRF_rMqQZaGI4epBJjv7xdDUKdv2fOi94nKhQJKV6vdOISfKVziKJqVwWQ2_b6O0s1u4cm16Wq_NQuIAcj8o5UKdCKrPEJm6u-cjcNLBMJ92GlMpRPaMDTsYwhLQ6iybTkzm8KGP8g4MElGDRCGjoTS32sKiL6D6XSfwUIF4Sy0fwVTIrk0wC9Sf_QCx-TPzsj4VudQvqJs34nF6arkl4QQJ6ya1lD05nHdb0VSEPQxjoPjsxT7vnDN66Bt82aaZVl7a2mxOSTwtYwoNVJR2Ymrukp5vlusXiCRE8Z3x3wRCZP55EPRQIkapnpJOcJsVsnWfH0BAQsSLv9C0BmbCstm3xrSaBpQ5xNUYxLwyHFwARK--Ovn0C_IgpssGWKwpXtl3WV5NSNENBSN0dCL_YZlw-d7Hbbk_SN50ReU3SPFFKPLB4L1Bgg9jCQkGBEsjDMVswDUIbVvjKdrJn4_dEpsNWwncoKVedqWxA4b7EawuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHnrK3X7nuky48UE1f3AOy5Xz6JJtJZaeGC09uRt9liwsBDfN0YXPEyLmhdR3TkxwmV6kAZwesHvqw0YSl3SSZujWCnL8IatUWAR9hkJELsqRI_NKOpD6VZHgA4AVA3osQsr9FywP3NuU9vlH6J8nJVpz7yf5y8DNLefP7iMWtLnjHpiJ8KNv0uyzbBW5zwR5ChCAZJUbKcPAFftSZkTYHolM36RRi_QqwxPMWAbmhBkr9rJfardkFkXg3P4K7TQOYAGIsM9Haqd_bw8-pYf8JjHEi_79Vpbn7yxQvc_KTNevJiUBvTaJx9dAkmQOG0xnyFfyjRrIuE1zXa2SvlN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3zBR7cI2GFSR_OGWDRsyckwEiq8JWn1ueFD9RZB23umRHu_b570YbQfQIs5unc4pz_pPibxGA6fLfNCuUBzJ9ZygD58vOF2FLstGH-xdSCPBHJvm6KiAjo1jTVdqXm-xOtmpi9kyJCMYMoj6l781fU2E66gM5KcoT1oXdxQEt3dwcQZurdt9njtYpK00o97-mFJnXr9hDTBFsJ2DH7etLS-2h0lzZv_53App_2WkMm68Y3VVk4BVFN4Stz6p0ZBNnu5o1itFtCqTNFqjziCVWUfGY0PWgDSmKKHXMX4MMjPNqX1jOXjDfhxhB86HUExlTZQ58sRCWFl92p2_HsQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd5nadmt1AXVfy1Rtr4q-8a-4E4yNTkRbOLxc9RReUjEoTgnZD34rciczdt1FE8Om9QZl29TK_yriQp8kcr1EI8cLx0O0WyqTBJ-iiigTMpSG2xU04zhX4-rNrBLfU9zuJ1wN366kW6wKgLS1fVAT36SeRktM-r7jIPPWmmQKIZnKTgUsuG5hZ392Lc9EecN7YSRGQW_nElsIQ1W4zdRFbV0BzHzUtke2jjeHNhzYysIFY4CfRrBHBvoYUxcyIYmTReLn1d-LQwKXKqmWYFKGl0_xjk20evvD4w8LS30eMIyyZP4hwV1_sO--BWi0bkbw4dMQOAIJwRor8zHd7htRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXCrd08Y0iEviyuEzAWOvqr2TD0-7ylH7u8r2__661g5dwtYpcdOcXf9Cx5cdS14MZ4bKUVnVSSj-0yRTPHe5iKctynfXXvkBNUMVS6vDHKyBc8WNkbdE2ObOviARN9F1utGGOcNB-P9sCcFKoyd9nIvYCStWnQ2-wbb-wERFstVinTzQMyzkJL1c6irKbjpER8TwWTAMUN63lcsTXYOAhKlsmViNz9qe9Kqs-UagazD0lHE93tGPzVYwWeplKpOmo0wjEBj251MI9qUaRK-UMTus-VAVrO_1OIhzeXf10BFiQemROWl1asPDEjcUTVcj0IivEcOrBmcL06E_85gKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=Q5g5MLj3lrkrO3lLSrTp185UJcpi3B6TXEqf_r88X-lMxAVp-_Qv6IpaiegwM1sBLlnXqC5UTX-pPb_LvwMX_AU3FkQP10_U9-mK9BcDhfrUNnCyuSvMNnSB85zXpEL5s7bs6-DdmzLZipB_Vb-DtnDmtWCH_SPcWTXY0FyGo9GbHTK9l9OYqVbeugHvgzJbFLIKGqsFlFdQa_lBM-n8uHt6o9UAOanOAdze57cMpPoqKYOz8MhqvEIMhmaEjCJrXavMCHjF99A7RVXJu1HFclQTxvJBm2vnrt6vdo9VafbKj0DE2VMCfwqwUMt5Smrbq_XsK5HkGy3sZ2NgO7t5znWWRB_RME6Ieh4nnMKdngBR7bx2AhxSEQmTDggorAAAeofHyTMYH_0d-dgHdN4lnEIM2_nC3Q7CXNrx0ydkzvqBfLvpfNOKrMomkMCFxsmiHe43ykR0LAUqslXYbb8Vr313mAfY-fBH5ihVlkkJAAAT_0o_Lv2x6gS1imuHATF_aJmgdNweBpooG8UHKrcfoa0H4KxXy6zlzvs3Elx1wxkELh0A0CkDWGmg4Fqj-1FNtRXraxwEg0Srl0wq5WknMxotMnWVBGlKECD-U4Rx-UEFuH2J3wtO7im3ENclcW2Oz3UPqXdgtcftPv4KjMPHmiXMM9-9xkyDlM7JHEL5i1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=Q5g5MLj3lrkrO3lLSrTp185UJcpi3B6TXEqf_r88X-lMxAVp-_Qv6IpaiegwM1sBLlnXqC5UTX-pPb_LvwMX_AU3FkQP10_U9-mK9BcDhfrUNnCyuSvMNnSB85zXpEL5s7bs6-DdmzLZipB_Vb-DtnDmtWCH_SPcWTXY0FyGo9GbHTK9l9OYqVbeugHvgzJbFLIKGqsFlFdQa_lBM-n8uHt6o9UAOanOAdze57cMpPoqKYOz8MhqvEIMhmaEjCJrXavMCHjF99A7RVXJu1HFclQTxvJBm2vnrt6vdo9VafbKj0DE2VMCfwqwUMt5Smrbq_XsK5HkGy3sZ2NgO7t5znWWRB_RME6Ieh4nnMKdngBR7bx2AhxSEQmTDggorAAAeofHyTMYH_0d-dgHdN4lnEIM2_nC3Q7CXNrx0ydkzvqBfLvpfNOKrMomkMCFxsmiHe43ykR0LAUqslXYbb8Vr313mAfY-fBH5ihVlkkJAAAT_0o_Lv2x6gS1imuHATF_aJmgdNweBpooG8UHKrcfoa0H4KxXy6zlzvs3Elx1wxkELh0A0CkDWGmg4Fqj-1FNtRXraxwEg0Srl0wq5WknMxotMnWVBGlKECD-U4Rx-UEFuH2J3wtO7im3ENclcW2Oz3UPqXdgtcftPv4KjMPHmiXMM9-9xkyDlM7JHEL5i1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
