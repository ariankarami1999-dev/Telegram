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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
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
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOttC31beuRBNYKwwAeiWtXbZFmOAaeELiXnOgQIWvNdB4UZYVEXylpoeEGM6VhnX3ob8hNBEgN5Igi9wyPISjArPyjh_36Uouogc1kbehGth1meUvr0zCRsVJiLwUg2c1t-o7f78OEA6genUgbe9iF8Fewmhj63MGSAvbEe0NDSWMibo1kb96XKlmnlIcKKLlOBMIBmqtXI6a84qzgbAeGgiT2QnxDtFHle1iCC7pJLXcSj-A28tIosT0A39o0Yq1z5AzOB7sqsG0JKEZaHuqqGpdhFS7aD7mXVBfEByAV8VWbaHEBb-RW1XkXQufg9HydTNwBn6axnwRHPRdhEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdyvlvYDUpxMbjzXRYuLlBiZL08GylT1waCIeLqC6xdRhaeC6raZHtq7dlWiwJFddhKctWMn-bSkfJjbeCxeMYdXHJ-GTdDVRR8uqdOWAi2_0Z74JHJfCsJRhS3gG2UUsTL3E_ROAOQ6HmVesIGoSlfOZ4jZKgJHccctFOkilggv8rI4iYlNVnDUtHUUceFSLGGp4bRf9rwp-v5ZyN2f7i8A35RqeFqBpTGMiRu76C9elVevsFP296y679vDLd6_IMaPFeVjGPZuEYMdDRlPa72waOfCxbu8Wnk7enRIjBvNIOfn7v2ZZB_6XaDpT_qrVNXrrHUbVG9TP5SiN09tDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDPALiIKV8Ige5xlUVbQl2XrdHAfhJtmMuIo0S9m-f6nLnLZWCtyQkEXvsTuwiPtTRhfob2Ohkmr06WBqYn6ot4dUEFndT-NG9f-5SHHRnxLf7rKMltYLdKDDfGYhoJeF6SuBPa3XuufkThvPQrRm7GL3UMfoblliALJR_SCjMKZeQQ6BVqSdkEA6YqgRGZN-zJEytWetBIBEzEOuP4kmXPyjX6BOnnDaH0aMw0piYji_BgA627Pw8vWUXP6GbxAY-ogxybFCzgsMUc4kEhVG0sQz9h1XLf8lA-C5PLWHjbtfKGUUiXv1MnwyeCMRmUOfu0ZxpKOmDWGEYrM205Zfw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=vPZkMNznXFrkfYGWQa04Ozpl0gMVt0RRQwIlmYeznU4mhNZQ-J0tOkWDNZOkCnrKdvBO5Qr9VnrcVRWZzBxfXs_qSiegbgLqzFiuqB2a6UCJdpZJSZ6d5AD15Kt0mDjm4WXproSEpjhg8cP_563O5wYtq55X7Ddt3_ATFFCVXrZbBPJuGeSwaojiJZORJ22o81XSsV6rHZ7mfxJHPbn8zfZnj6FzWOUimztcoWbMfqpKs4jfhEN2n_ngp1QTjh8S90rtj2yIhVOP6pUE1J2muRd7FcmNxWzVlarWGsQHacgeLWkO6RKtqmBkWmAw6pCTDUL-96PihvF63HpxHa1EhyfQIPcbQvmVow-DHQOlBQL_0qwVRf4xApLtH0bWNQSmF0QfPyJuxbM2H8wwpSnxcmZOEDlIImbgAHdhEoiQRQmO0aLU9vxgqf8-sa6T_8_GASYuVOlLImFOYn3GdqMifBE-SpFxpr-kDNJ0M6mU6DqiAFtESnw2H4wywOetaabox2p3EikjUCOb4gz6hHifmbSSc0fNL1xnkyQY9bnVdb0H3Ma-LtLGKwCCZhYlT0y8TmfuU59BGSeid4uYIxeKUpa_ODXcaNOovHCX9y5Cn5uFN97a3aLP5J8_0xlDkqy-GRJr1tK3udXpi0002l5ywgpiHdpIT1n0YyVT4uf_6zM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=vPZkMNznXFrkfYGWQa04Ozpl0gMVt0RRQwIlmYeznU4mhNZQ-J0tOkWDNZOkCnrKdvBO5Qr9VnrcVRWZzBxfXs_qSiegbgLqzFiuqB2a6UCJdpZJSZ6d5AD15Kt0mDjm4WXproSEpjhg8cP_563O5wYtq55X7Ddt3_ATFFCVXrZbBPJuGeSwaojiJZORJ22o81XSsV6rHZ7mfxJHPbn8zfZnj6FzWOUimztcoWbMfqpKs4jfhEN2n_ngp1QTjh8S90rtj2yIhVOP6pUE1J2muRd7FcmNxWzVlarWGsQHacgeLWkO6RKtqmBkWmAw6pCTDUL-96PihvF63HpxHa1EhyfQIPcbQvmVow-DHQOlBQL_0qwVRf4xApLtH0bWNQSmF0QfPyJuxbM2H8wwpSnxcmZOEDlIImbgAHdhEoiQRQmO0aLU9vxgqf8-sa6T_8_GASYuVOlLImFOYn3GdqMifBE-SpFxpr-kDNJ0M6mU6DqiAFtESnw2H4wywOetaabox2p3EikjUCOb4gz6hHifmbSSc0fNL1xnkyQY9bnVdb0H3Ma-LtLGKwCCZhYlT0y8TmfuU59BGSeid4uYIxeKUpa_ODXcaNOovHCX9y5Cn5uFN97a3aLP5J8_0xlDkqy-GRJr1tK3udXpi0002l5ywgpiHdpIT1n0YyVT4uf_6zM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=mvNWKfUfJZGOGxfMNinXusbHP4yyOff0z_3wyO8NWnf9wUi5K9H2i_UDDM_MCIJvCbxebi8I_2WC9BqLqdqMRXl8pTmm9YdhXthaf52EQPH9xhzzicOWr876X0gmGXPs3Rk5-CmNkUw0PEgsQoM97FN_CRwecDpjVTV0OB2BbuHe0VsVbVKB2MeBK9tBkqHC7xHA1ek2ESkDnTTHh1Eea2w--GmaQt9-OsyMZ5Iufbq92uWDxVWbw77VLXJ0HZ5Gz4ujy1ZWkch9WAci27HcFbje_IxHP82oVcmvw5drulupU2EQEhPueaihujucsPCc4cqIedN673Jm68p3aS9n8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=mvNWKfUfJZGOGxfMNinXusbHP4yyOff0z_3wyO8NWnf9wUi5K9H2i_UDDM_MCIJvCbxebi8I_2WC9BqLqdqMRXl8pTmm9YdhXthaf52EQPH9xhzzicOWr876X0gmGXPs3Rk5-CmNkUw0PEgsQoM97FN_CRwecDpjVTV0OB2BbuHe0VsVbVKB2MeBK9tBkqHC7xHA1ek2ESkDnTTHh1Eea2w--GmaQt9-OsyMZ5Iufbq92uWDxVWbw77VLXJ0HZ5Gz4ujy1ZWkch9WAci27HcFbje_IxHP82oVcmvw5drulupU2EQEhPueaihujucsPCc4cqIedN673Jm68p3aS9n8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZseqhqBei5iOAlkvaMSaSfqHC4nyBjt6OSe-Vy4LmOFZP30qSPkyvWXF1e3VzGut8WAlJvRJbdtu2qtxKsCFCVqkR7HW-07M4xfzvOUm-78gZjsqXkRDxWkHy2ip1kR3hFu2poT7EpJWZ74MYxSWpl5EntbX62_lZfLIq9Ee0_BTueoRFuJ2wojhCa_Y1ifZ-L3cH-9xNm9YLhw61nU23HMABcywgsNgYtnArWj2XfHklrsYPBD_iyMV4HyBD_WcERXLvHC0MkqSCE_MI23jxqckr4UJVjtvB7nfC6oZuQR-sFO4VUfRj4RgTjTw5anWeS9R2QqD4FBHttsclnwvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Lot2GYJTC-XSfab1kTzUiRprajenZI_rOAPYOSNZEC0IZb1OTrvrY1ls_jjIoX8870F-KEMhUrOlnfH_X_xT_i_2ug-k6Cf2XOl8GwRrgFuQjvBcaMH_6kgbo6_Ge_6qJVX6Boi-PM5NwMzY-80kT1GLNYsunTOIfnCuvfJ_9liwnbQMsnQ6tAuk0HablkzY9LAg2zeDyceJbWBqHWGBFDuHd80c50OmVEqr0-xeaLKgNYVDzXDrvzqmD8jcJZEhneySqv5QBKOtpP120sxPyHtN3Et7l2aOwfgkZc5J4eRXCOWKGQojvcDzvNOuZx8pd2gNXRy1dXnBdG0g916_tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Lot2GYJTC-XSfab1kTzUiRprajenZI_rOAPYOSNZEC0IZb1OTrvrY1ls_jjIoX8870F-KEMhUrOlnfH_X_xT_i_2ug-k6Cf2XOl8GwRrgFuQjvBcaMH_6kgbo6_Ge_6qJVX6Boi-PM5NwMzY-80kT1GLNYsunTOIfnCuvfJ_9liwnbQMsnQ6tAuk0HablkzY9LAg2zeDyceJbWBqHWGBFDuHd80c50OmVEqr0-xeaLKgNYVDzXDrvzqmD8jcJZEhneySqv5QBKOtpP120sxPyHtN3Et7l2aOwfgkZc5J4eRXCOWKGQojvcDzvNOuZx8pd2gNXRy1dXnBdG0g916_tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q680xC1kHzHb-jYdtwyWLC5fJN07cH8lVfPQZhzKn_Auxd7YtByFewC-hMJVIpjXnV35lWsTUP_pi64UG4aw2hZ3Ljnd6neiSv3dCEaCLk-av6r_xhumeW2lb4QwNHygBgMqZCQPAPUEF-mQDffhxmX6v2kuiA0mt4BNY9qXKMankUbupp2rOoViAihEqG_W-cNFLbwyUaVFrNPPWhH6A6lUh_Gx1WLYninhds4wpZgs_ldUdU8kG_YZq1__3cONEv3vfA3ftgvFNsS7a3O4mFxbf5XSGRxusakald32jnZpUpCLIJBamk5yk47X6sQDcqV6HoJbQZO_-32cqsvOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqkdOUt0GuoAchMQA46zin48OpNXNfOJA1s9jmWcnokSg3dGo7tLkAwqEGUnPcWKyJS0-doDu6vxKPthB4IG47IU09SuD0DuCK_5UvBAMikynASj7aEyQRfVGehSlpNTMOAlXksP0KIU8fkNmgCv5aGHP3T5vf1StHE-IilwcTTL52Cg28f-UTPnDA5Fs-qGnMPQRQ-3AG0sWL9hxeUs6r1660Og7afExRfay1Wt4OfcmqivPQmZFNj8oUxjErWwqn4QBdqz9c0V0q8tXCOfr_nQ7eHBOMnYMtNInJh5v8pzw1rP2HbVdhYje07flZBEz1Lq5wTKnsf0sYAi7Ia3bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcImUoj4c575drQ-ZiHhgG2BkPSAT_sQ0H1PjPDE-ivoULDajXhFN0ER-FIPq9e9yJsP2HhZhK5VHvvE_nU-pN3PktiVC5Npu5AR0eeqGXr78o5_JvSivHMYoYhbYqjlqIdFXrKsoGlJ5cI_pEOKrPkcBYZz5kuPKczKBpcOiEtvQH2K1dNU67TrbFWJxlla9tGlB1H_c7XtFvBKSC1Ujr1L1N1u8KKuFMKWutL-bQSj5Pus_Y1Be_RpW6CwFkAd_E-F3KedbwDAf8IZ3-Pz6C7YzE6JzyX4kD21osYAt8eiQZZ9o6cUapCfLOpFXbm3kROq66ShKrE-wUMda6QLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmSmRYAUAlYxUmln_JtnOk22CKqFhqVRQR2Q1WR_D3fycvrcMqjx7uMO0Q9pxNutoH6S55QJS4398hlzRfPQVNO8qKLxWC_MrXK2cHRgDRG7hnX9k6yAxCKsuBHPR8wT5OKMyMEjEiOfqaE8bHA9LyaH-0X37ew_ErDYZVcy1_vN0yR6hIYlitojwQmM2rF2m_BP3LhOlbfOuR8RpP2qMEXozPmCcj-4XCNF68ItUqkv3qyi9Me_O1t4_mGUi3f6sY6N_XAEomt-4k3fHepEHFNx7LTZB-v6WFAoYyCT38EArTN2K9wBlb-xenT-MJ_2D8sb4VyLLY2TSH9rZVCl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGgjOgICRvj7xMfPlAsHrZakHoYxkLedNnEtUm6MBck3qBxiDWDaJfz21iJ25AlXxAM9QMPsFBDJpa42Wtp6E-em7T-5ub1sFCrKR3gf_7lc9yHpbUoRsuOazFCwt1nekYA_0W_g8iR7lp5m9UWNSARQiDFDGft_qNBeqgXR9El8_Qi0FyKudLnwpqNTHvyYTewadQvn_kOXHK0VsAc2lZ4Vox7cb3HSIg8-ecBgBkyiFw_QhHxEQXVhNdbiEubWP6yGVtUsbiUYl54ECoNOFvd2tOASRGvFr8qu8DFbd09Y1OKnV88D-oGjGQ4iTFT3IzVJFkHF070lMBU86JNibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lBWkbfNrAiqsoWlmlUrSwX3S0-pU2DGQKQWynDxJbUqci7Fj52GSVQHJr63_vWeQtuyGicUL6qUaY5KGkwWhAF7965plhDgQawIQOXmuPwL9vb69i6r30jpoezK47LwK9fedrbuA4TNpGnN1AgCLcboZ10JyGFd1ctVBT-5TP0ODA4Fgf_v3Tnvjo3gNHhhwZQJgM_ssjGH_t9xYRsQy23o4vAwYCIuXAIlW-mKQdFOmGBusJuYknvfJm7-9u1pD5g9MkevmU2AsUo1-x7FofZzBxg3dtW215FTF4hYPrAjcVCIXigSMfhhKOPySbhpx37uV4wOhU3nB3qPaWqbPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lBWkbfNrAiqsoWlmlUrSwX3S0-pU2DGQKQWynDxJbUqci7Fj52GSVQHJr63_vWeQtuyGicUL6qUaY5KGkwWhAF7965plhDgQawIQOXmuPwL9vb69i6r30jpoezK47LwK9fedrbuA4TNpGnN1AgCLcboZ10JyGFd1ctVBT-5TP0ODA4Fgf_v3Tnvjo3gNHhhwZQJgM_ssjGH_t9xYRsQy23o4vAwYCIuXAIlW-mKQdFOmGBusJuYknvfJm7-9u1pD5g9MkevmU2AsUo1-x7FofZzBxg3dtW215FTF4hYPrAjcVCIXigSMfhhKOPySbhpx37uV4wOhU3nB3qPaWqbPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7J3zhK9mOTplxzqjGMaBaePBkqeBJ_Uv2vYjxgxY1GdzSQEP4WDiTeBeQ_bMfirENVc24Kv0ZmMP1AFc6AYxSNQDRJqL0NRMcgOxNLvynkk0h8BlEtGmPwSph7adg46TIUCATeHq-qwnsXLgFQLlCx0hTXMj7snPuEysZsOc171HfjlaV6H8DAA9Fh1XuAMcSBGbtY2aAmqUg31fRf0vbNZ6Yig12WYWKWVsfTI_hCpQ3-pN55ySguRIXi-u9OyQacjhqpz0yD8uzDdT94DwSYCxdOq14JCC6ywYZ6zINX99fSTE3sZiT9eu1R_afMC8urRZUYAf-ICJ7NEnbHYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL0LsnRF1MHvpVk_BKnPCss9cq8EGNu6TXnfACOWPtAFTCHagS9cIavt0b-rtBViulZSdCtIWnocQaqMHi0y8x8Lu0btvMQaGfQshjjmv9ddrfs_izzNgP0ya4A10_lcLc4WLPujQaEYIlCL2IFvWbwJMagBYk3EnFgkMmYfdraWPMm6kLukrIlMfGKhu62vtGdR0YlW8HJqxm7HCtspxbZJ6h4e6a9h9OwS2ee_uIHpMFElouJ9BnAMRtDfhkgoTfOwCU4ZupUmUc2YEOHaYvmE46PH1xiqqZmM55SLz5dwsYYnudeAyTkL_AwfSlQJ2b56kYgdrw4yTyUmYn9ZWA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=F21eqWgCjb9NRFWmyStGSf-M2uNRRxqGSfhdg7Vg1-LhzNPQwO86cqGlgKj_reDE5YjolhkQXVkRs_Q4PUtpFobuJfT1n_BeCS6UU6WzehCWUthiQgjCGhT6RDFFWPqYRVLDt9m3ZOni_tAskD4kaxIt8XjtgnYboDUH2b0hMXzW-0OECGauWL5nnnGIiEBlSFvLqVHohUKMVU8h-iz8vNY8yzDZirwUdK1Ks8gwKeHGZYiJqBSV9TgfXBjAuuQFsC8jnMZj3ot4BYXy5hhJXXlYA7b2rtjApnmUcsKagU64In8aPMvUMkjFt31-p9u_SfVU4eSXnzTNZlvluOfNGYBY_AJ5-VQpGyFx3xVI0oCGshQ6zEp8onAWywKEis6tZSDNBzTD848cGgDiywGE2faJXRSSrTo3JAVES_Yop1oFVfNwrcc_3MJ0XkrdayMgnTXAA5zEfFzcokjwTxj5T2Pc03Ir9YZJaTRtb47QhuV7e1gw6eMMmIT2YLPMlvl6cg8BFpfBsxKbnN9_wwM7FOgbipjC6-pYw9otITLppPYWb29ze_4-kcX75UlwRkSH59Y41zjZjwMyC9ZmeIzkkmOTLRCAnABaCCxfhrf_GWYQvQz2IJReLg6pJwhT_B0aV48OCO_oYthKDv_Jcd_rZWFblPfFAgmc0ahqVqXl-T8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=F21eqWgCjb9NRFWmyStGSf-M2uNRRxqGSfhdg7Vg1-LhzNPQwO86cqGlgKj_reDE5YjolhkQXVkRs_Q4PUtpFobuJfT1n_BeCS6UU6WzehCWUthiQgjCGhT6RDFFWPqYRVLDt9m3ZOni_tAskD4kaxIt8XjtgnYboDUH2b0hMXzW-0OECGauWL5nnnGIiEBlSFvLqVHohUKMVU8h-iz8vNY8yzDZirwUdK1Ks8gwKeHGZYiJqBSV9TgfXBjAuuQFsC8jnMZj3ot4BYXy5hhJXXlYA7b2rtjApnmUcsKagU64In8aPMvUMkjFt31-p9u_SfVU4eSXnzTNZlvluOfNGYBY_AJ5-VQpGyFx3xVI0oCGshQ6zEp8onAWywKEis6tZSDNBzTD848cGgDiywGE2faJXRSSrTo3JAVES_Yop1oFVfNwrcc_3MJ0XkrdayMgnTXAA5zEfFzcokjwTxj5T2Pc03Ir9YZJaTRtb47QhuV7e1gw6eMMmIT2YLPMlvl6cg8BFpfBsxKbnN9_wwM7FOgbipjC6-pYw9otITLppPYWb29ze_4-kcX75UlwRkSH59Y41zjZjwMyC9ZmeIzkkmOTLRCAnABaCCxfhrf_GWYQvQz2IJReLg6pJwhT_B0aV48OCO_oYthKDv_Jcd_rZWFblPfFAgmc0ahqVqXl-T8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=FoOvvJ5I7qhuk4ZQhRDDA6FgvKGnjP6pv8PQm09xAKj59MdDETIjW4LhyWvS4w4TS4-7WZ3y_c-TIjRh8JBwSdxDewQidZryJ3FXGRkMUSa7ZHxVX_MEazd4dogPb_BmI2f89a-cKVrTqB3AMXzaBjSitOedUd_FUAAi4lvfySDng_TwP2qQbqf5x-VDxy2Et9gRAI3HGpv1B_eNeke0RkqjR8pWw5AxyVqMGWkL7OVadq5oFrEJCmw3ND_bzfMAnsjQQVCpYNtcLycsfzOkkpnp5C2tEumTJZ4ZxuKcxK5pb3v4EdGiaUhHLJr1ddJcEvtVh5yId5rP8IY6pZ6YSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=FoOvvJ5I7qhuk4ZQhRDDA6FgvKGnjP6pv8PQm09xAKj59MdDETIjW4LhyWvS4w4TS4-7WZ3y_c-TIjRh8JBwSdxDewQidZryJ3FXGRkMUSa7ZHxVX_MEazd4dogPb_BmI2f89a-cKVrTqB3AMXzaBjSitOedUd_FUAAi4lvfySDng_TwP2qQbqf5x-VDxy2Et9gRAI3HGpv1B_eNeke0RkqjR8pWw5AxyVqMGWkL7OVadq5oFrEJCmw3ND_bzfMAnsjQQVCpYNtcLycsfzOkkpnp5C2tEumTJZ4ZxuKcxK5pb3v4EdGiaUhHLJr1ddJcEvtVh5yId5rP8IY6pZ6YSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrvIianHS9xn11A6rjO61FZfMYsDIgogsCgsC7GUHGICW_WILry5cfH--j4_ZT6Qi1ZCBkmcmfMwSlXSUfWyYMFZTLPlR0ttkt6RpNMBzFj3IspBFKe-gvb-mkOOQ590K2hlhzUSnnQKhRwZ1lvi6oUZNjDuVrgXcXMScwHAq_Vc0UuQrLtmEVVfZen-WmZQgMy81oby1ZF8_m7ENVHrE5vHg1KK1MY9E7iQOCjsH-6BtSrGzFbEcfc9zMu6wJYjqKPxEgaYVYVn04LB0nwXiauvy2xfXqXjHRLkOF3wac7ce5XJJlmdvYqhmma_Lflvf-1qtShagueB1p7XFyXLxoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrvIianHS9xn11A6rjO61FZfMYsDIgogsCgsC7GUHGICW_WILry5cfH--j4_ZT6Qi1ZCBkmcmfMwSlXSUfWyYMFZTLPlR0ttkt6RpNMBzFj3IspBFKe-gvb-mkOOQ590K2hlhzUSnnQKhRwZ1lvi6oUZNjDuVrgXcXMScwHAq_Vc0UuQrLtmEVVfZen-WmZQgMy81oby1ZF8_m7ENVHrE5vHg1KK1MY9E7iQOCjsH-6BtSrGzFbEcfc9zMu6wJYjqKPxEgaYVYVn04LB0nwXiauvy2xfXqXjHRLkOF3wac7ce5XJJlmdvYqhmma_Lflvf-1qtShagueB1p7XFyXLxoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7WRiZjNGpkdDg-w-u54PRe7fwsV0GCFBNmrJ7-4NP9rSlMk5mW-sSeKeCJV6_8Sbgx9dY4Eb2eQsI17AmOl9-5i19qCcdDCk2kH9D6VF7EwsTuKaxjr2RauvrN8k_GGIXmIF0h_ZYmqW2cajo1qjLNgh2p1We2S2Cyfpbk1RA5Tu2K1O4qS3riAekWXtxVlEhM9CJwg75ADs4eZ-o6YXJnFma8oTvqXptTPdv6Ov0F0fnH4UPYqgEyrEuD8ocTN4i6Z1x-a73VL0Oivp9a4vIszEv9HYn516YteEADR6N7eoURZv7tAInSqKioUaEAnpahWwAWAhs6jOYxlbmomzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn6v3hQzF9cOy9BCAWDg0R53iQhFIOuPsainyjhNb0uo-wtCzHNi8Ix_ln9ooEf0S2EWIewhAOImbrjKmuUWk30BRO0W74BzvZXQrr3ccL9tpURQJCP6W8hfSsCOm-NoJ6hMkP7d0cz3tiIVwwoAQyQCGTZWYZxdxAYSpcbbIsCc-sPpKGPlWObJjgj9r344uBavd-GTOjwRzec_jOGlm0Ewi4ZL-gqd47i-tfWZHDN2MZo8sf9Ls1j88CnvxT0rUpZFC2MGsJpv2gA1exN3qdoaEZ8ZH4RqR9I1yAYHdpzMnw58V4KTJSonETKPF6IpeRVvQqKRCmqofQoveJqbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK8bJ8TgwWOATpPaHEGPkfGdG8TRt4LeFLPYXUILhxCiUwR66nodcOG5RqxaDBL1NyhfV45NZoJJqE5o21TLWrVJztSXSaSSTCLIV21y79X7Ua7ITS0iwVZbnUL-LVW-8J-AleDngEGp82ocsfwtVL4PDqP_NKkk3H5pUuaHKzuSZPqoJHFNHQ2VJi8OBkmG8HR4wlpegR85qZWPBG6RvDIi_xGQF5nAENm_AvbwQYXnI0c2hJSFxWI7f7wsGAieAMw-VQI5mKW5Tt3ODEEYI1cbLnZ7ApgN25HYEccP-_YTv-mBjwrbx3BHh8GM4_FnEzxyMRlDsP9jPJJauHmtMA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QfhhXnqU9bN7iB5gcNJylxAbpTf6Y1TJiTkVvkS4AFyp55ZYPNVSNVxcIXuR63tjlC_gFf0CnirBIIM9z_FQeUMOFKImuztZcmaqKsIDlrFNXT8gktsDmXTPqWkYVHaGjvSKXVWkWzYTTKodXjk6A9WdRTuv7Gt_zGzV9RNL0pL-64dtNS4b_Jq3BRBCO85h1YDgx-95JfhXuLT6vOMhmfKbCVyFkYsOUD-5g7KzHx3k0S5_RlkTW_o_hkPcz2nP9cjbdqV6w1RV-M0ZcJeID5wNcjQqLUOORtLvz3ijaDnBXpWTGCvzeEyEu13coguRozemJFrg2Z6i8LS8c-26zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QfhhXnqU9bN7iB5gcNJylxAbpTf6Y1TJiTkVvkS4AFyp55ZYPNVSNVxcIXuR63tjlC_gFf0CnirBIIM9z_FQeUMOFKImuztZcmaqKsIDlrFNXT8gktsDmXTPqWkYVHaGjvSKXVWkWzYTTKodXjk6A9WdRTuv7Gt_zGzV9RNL0pL-64dtNS4b_Jq3BRBCO85h1YDgx-95JfhXuLT6vOMhmfKbCVyFkYsOUD-5g7KzHx3k0S5_RlkTW_o_hkPcz2nP9cjbdqV6w1RV-M0ZcJeID5wNcjQqLUOORtLvz3ijaDnBXpWTGCvzeEyEu13coguRozemJFrg2Z6i8LS8c-26zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8VWF2_ArUsOw7zdLx-EVf0kJnc3t7fv_yUoPI9yvntsNivQlUZyhh70_BaJ0-9kgeKs_s-GsDkmRJ5885wQFoqKDW8qEdfxCkTpUkTXUEQ2pX9_OS9pLDSaAy9yqJdGDhB2_vHVj3cw5sr_MROZxYg4-YlthlA9iTuzrc1wq6LfenODBIKRGUisYFcNj5NP7_Z2AOWHhI5bZXYUabwvsj8YGXsZueiO4lQaAxNpfQ0hmW6uv3IGszomJjQzeB8jgy4ANdK_3eXnMUZcBD5fam0uCcH2Hn2R-v4XCbhQeyUdDLlfqrfZNC1bUajp5aEeZ8xrVYpAiSGP3ySDiF-2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijwb6hvGCoT6eJxr37Q3AD7b0BRK8Zp6AJDNhQXAjHZ7tpVJ9zH35L_IDuZZGRdMLxcKkdWcbKCMZGHMcvpcb4khiAL5IsojbsFKuMnc9w0NVV_3Q5DkpO5nGZ4-S7pxr_7IvEOctbg33sAxcEn1NuNVt88koeS6TYtdyTvWZPkoTeTHf-ujimXGMGr66QVB1On8Mq3AaxUI_qawuIJaQ-XmED3kV8rT3s97FKHz-S7zYog7f4iV2DpTUxMYtg7VIzIh0ep5tNsMEKm01CtxwFK9cpSgAJA9CCKJFONZNNeH5hme4GxLzQmM8j6Eki74qtYvYyRQiRRHX_cUh__a3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoDU7ptcYHuexMlpbgJstU4hmMeea7Dw-Z5uLv4SDW-vaB_nkq6ruT7LZLebeC4x6wiQZyIQUSapbtbEGW3y1sVQ7GjhXTPhU-0fZnFqxiNfpKscwbnGLlZF4_zYuCJCB2NBVCjbAG3KIywp4JiIjg3Zq78emZDBJ0ygtob3pEjpMRH8iZ1WpI9Ui_U5EHhK9ZZ5pCdUYXs8ueCe9uUK8VF9nVKy3kNMfIjK0BsHxbiwJOYhEvC66Nu2y9g-WLvz-e7H5Z-yW8-JN8zYELvsAkqvcipPy7rhjaYfE4luj1uC-UIn20_fGagXVBLHFCYptT0pWAo57M5RwLy8JcwKQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFKMl5pVZLqbHcDvBMWLUwljH7doudlTfJjXvUDqHwSQBHqRGxkvGB3QvP9pKElO9eqoxNlWzTYJazvVgVdwFz3k7wFmXes0PlcS5tVfzI6yhehT4_C8D0NITtTrrorJMTPIOfkvUDUANv8L5hMWDLuk2uxH-URYeJAFOdN7p2GfMOuuvLdwzBJwIJzt4CtvBIzKTHCPXi829UsCFKTwoLcPDk0fwBWXX6G36WXFN3pE2G61Zyxt2ggnd_N8f26OYqogXRvdQGlT31_sHV1Mp2h4epTWPCO98w7mLMDjeAZ0p-_XaO6gL6yvLtlRK0Aj4IxVSl9e6AtTLoLFFrD9lA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=SYTpIvk8iU8BN81nDWhOUu4f57ofF3rckdk0c3I2bu1K6_9sO3-8zfSOwcd-ZBwWDBeYzEs_Egm9Yr7SbKGUyemC33dQ68URKHOGJjhtjXOkyCm8iF5JymdHJA5PYFWk0_3TFGwRWvRhqXCm-RVanhmvufS70JtqULilYn7pMl2czsfTGAGprxIHyMZJ_lgsiIAEgPju4vUuDN3davrV8jMAXry5p_mAGjJALjZiLBjzGAxysCyRPPcbTGkV7Obx6CGC2Qztgc0zFe77X-Oanman_q-4oL7KcRuIhX29GO8g3pAmx1edKDuX7AkTQYdn4UzrzSlOfEahaRTA-fFkGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=SYTpIvk8iU8BN81nDWhOUu4f57ofF3rckdk0c3I2bu1K6_9sO3-8zfSOwcd-ZBwWDBeYzEs_Egm9Yr7SbKGUyemC33dQ68URKHOGJjhtjXOkyCm8iF5JymdHJA5PYFWk0_3TFGwRWvRhqXCm-RVanhmvufS70JtqULilYn7pMl2czsfTGAGprxIHyMZJ_lgsiIAEgPju4vUuDN3davrV8jMAXry5p_mAGjJALjZiLBjzGAxysCyRPPcbTGkV7Obx6CGC2Qztgc0zFe77X-Oanman_q-4oL7KcRuIhX29GO8g3pAmx1edKDuX7AkTQYdn4UzrzSlOfEahaRTA-fFkGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=obC7OrRxY1gX82LISp3txmyROmiN36B7nSvEUDOnHrvWJC7JKNEvCiTk1Aj6Bu8B9RO4GTmr47wUCZ_AYcfdUwB9bwP1lo5QfwLYHqX1Ejazvk4_J65OdSmm677Gtxaius6nDq96R2GfIDGNjhlzWqlHYaaLc8qQ9YpQdZawQW7wip3kzRF_sbqNlx8gxM3twwJhamQ4EX2KlvZ6i1T-t00mrdQCzY3pJzmW6QCwfHKpJknyNWs6M6Y67OkDM2LE8JGlP781ELMzoX15lfAKTNGcTZFob5YEyxV5vdLXEpig7p_uL3hl5qDZE_VuJAeyF_yS9NAA8IYoac5JBhdwUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=obC7OrRxY1gX82LISp3txmyROmiN36B7nSvEUDOnHrvWJC7JKNEvCiTk1Aj6Bu8B9RO4GTmr47wUCZ_AYcfdUwB9bwP1lo5QfwLYHqX1Ejazvk4_J65OdSmm677Gtxaius6nDq96R2GfIDGNjhlzWqlHYaaLc8qQ9YpQdZawQW7wip3kzRF_sbqNlx8gxM3twwJhamQ4EX2KlvZ6i1T-t00mrdQCzY3pJzmW6QCwfHKpJknyNWs6M6Y67OkDM2LE8JGlP781ELMzoX15lfAKTNGcTZFob5YEyxV5vdLXEpig7p_uL3hl5qDZE_VuJAeyF_yS9NAA8IYoac5JBhdwUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=nFg7Amjp2wHIjEfjegZVTI3gP4QEsxUY8nYXU2or8zGoO894AsBQJSvPpUQ6OExdbULxgsURup8N2iAgoMsO0kNS5aQDZv8z8h2Gmc8sZWxY5uKtH537gpiiQOLsi80j3zyMMokDk-AiqHGqPZt3fYphGuESubT0pJcnKc7MwWC_51GdeVuWu2XKtbWPvPPAj_QGZigthEqo9YwwwgNjDilAotTliUjILaj9jJZ6vo8pcQIR3DjtdTvcvLzQ1xJ05J7gjyIbQQd7tgDaba1fwngbnvyAALzPocAXXey3Pgt0w6HAaxmH5eFJPmjD-aeNPmG-5tjGb56Bwp1lyEPKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=nFg7Amjp2wHIjEfjegZVTI3gP4QEsxUY8nYXU2or8zGoO894AsBQJSvPpUQ6OExdbULxgsURup8N2iAgoMsO0kNS5aQDZv8z8h2Gmc8sZWxY5uKtH537gpiiQOLsi80j3zyMMokDk-AiqHGqPZt3fYphGuESubT0pJcnKc7MwWC_51GdeVuWu2XKtbWPvPPAj_QGZigthEqo9YwwwgNjDilAotTliUjILaj9jJZ6vo8pcQIR3DjtdTvcvLzQ1xJ05J7gjyIbQQd7tgDaba1fwngbnvyAALzPocAXXey3Pgt0w6HAaxmH5eFJPmjD-aeNPmG-5tjGb56Bwp1lyEPKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyYvrCEX0kUAKKKA-tyjpWbXtpZZcRhOR-kVMu2DHmUqUyJ5ZH8xlvLiUza7sGJq41VUnaCGu04g5WG0VJx3n5TyWKyVosheu--1Nms5GUxj6t0x86vpmTZRHGZAwjy11b35IXShpAXUDe_6MkAh4ylG3NV3UWWxKYEVVj7KtoWoSixGb9FYkTWJB8z1mWqbQvFIiSvQV6tAfy0gOXutJkkQAW6F5egNkcC1HBTF1vfboTV-6z8iO3PAAUr4zOyHwm81bB2LrZ7FOZvDoY9E-olE22XHaZDulDKVNnNlwAkhcM-Ql_Tbx6H6HQUzmCGAsfRjHlHuV62nN6Ibo-ReVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=UgWpYViuQ-Lm7qf4BtJ4EJrvmduQGKOEqy0iY7DduAeaJm12DXw7QKg8UwBd2NeJWED1IhHGCEKa34iSZxUA8Qp5l4aPh4Vb6dmkqKCqSWW1pMoLNXBzu5rWnmPWvsOvPCxK7xPUol5Vw1Z47x3GFabZb03-Y2MzQfsbdnUGEOujphQGoNmP7bRkgbsA_rlZZZGt5JJ4xuNWVwq7ngrLVXS_VFj4JIU1BWPRVnxd-LUeREtJnq1x8i8xKkXIODV45QBs9194Be6fxzAnzuFOFlmvHCoZOD-1Y6brv50ohmuZgpoJ59V00nj2ziw13u278b4b3WkOV3MvWYHNrMd5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=UgWpYViuQ-Lm7qf4BtJ4EJrvmduQGKOEqy0iY7DduAeaJm12DXw7QKg8UwBd2NeJWED1IhHGCEKa34iSZxUA8Qp5l4aPh4Vb6dmkqKCqSWW1pMoLNXBzu5rWnmPWvsOvPCxK7xPUol5Vw1Z47x3GFabZb03-Y2MzQfsbdnUGEOujphQGoNmP7bRkgbsA_rlZZZGt5JJ4xuNWVwq7ngrLVXS_VFj4JIU1BWPRVnxd-LUeREtJnq1x8i8xKkXIODV45QBs9194Be6fxzAnzuFOFlmvHCoZOD-1Y6brv50ohmuZgpoJ59V00nj2ziw13u278b4b3WkOV3MvWYHNrMd5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=YRLJvyr5Y_Xqx9PK18gEkfQRu2S6oIe-zvPmi0mnfuMlQU_Gy0DHMox_LAcOkzvesTbvp5ESxaovz9ySwcBrsqWWCauRvQHAzaB0jhlJbsnaKAbHqKDGugm7ldbsI0sAwr-fnnwR_75YlrtjN01Wo0Ea1c5DAcK37pmYX1uIQyWfdWgejHGJU8kbrVyhg-etiFpbTz1FPbKKA4QXpfCoNLhR4tKzB_HJPhKEUaM46mJsajNMvO5k1SP-FNQIXCLeZxdmlcecVhXeDp1BBBZJgTNTepZhUgaLztlEzRoaTFwHA4ieaOaMd--sBvqaGzbeUAmnfEeXQfXASenZay_dzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=YRLJvyr5Y_Xqx9PK18gEkfQRu2S6oIe-zvPmi0mnfuMlQU_Gy0DHMox_LAcOkzvesTbvp5ESxaovz9ySwcBrsqWWCauRvQHAzaB0jhlJbsnaKAbHqKDGugm7ldbsI0sAwr-fnnwR_75YlrtjN01Wo0Ea1c5DAcK37pmYX1uIQyWfdWgejHGJU8kbrVyhg-etiFpbTz1FPbKKA4QXpfCoNLhR4tKzB_HJPhKEUaM46mJsajNMvO5k1SP-FNQIXCLeZxdmlcecVhXeDp1BBBZJgTNTepZhUgaLztlEzRoaTFwHA4ieaOaMd--sBvqaGzbeUAmnfEeXQfXASenZay_dzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=utUC6uivixRiS26PuyaCAH4__8IxqENUHmirlfqY5kwKDn4oO3aF4eMKTCjfd6DvwW-Cab8kF74iM5mwECFeCf80AvJO-yYpmmEo62KqXZy5bfitA1iqj6Ofs3Osr9-7XpGNLbpASHd5JMEP4QGY-O_8KNV7mEPKfGFM4UVgOPVds-3U09XPLEPgzWv0tdwcEaaNBKut9Lw0SNsfDqw0rEB_4KCEw9DOUYV9LpHSi4l6FmohXA5tRfmrBuWrOUF2e1HJHC8OgafQwg_ONw1d5QbRWheR6c3X4lampTba7SvSntBxxYU63rAiL7tMeKj7ZQx-PlzSA9oVeflaaP71ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=utUC6uivixRiS26PuyaCAH4__8IxqENUHmirlfqY5kwKDn4oO3aF4eMKTCjfd6DvwW-Cab8kF74iM5mwECFeCf80AvJO-yYpmmEo62KqXZy5bfitA1iqj6Ofs3Osr9-7XpGNLbpASHd5JMEP4QGY-O_8KNV7mEPKfGFM4UVgOPVds-3U09XPLEPgzWv0tdwcEaaNBKut9Lw0SNsfDqw0rEB_4KCEw9DOUYV9LpHSi4l6FmohXA5tRfmrBuWrOUF2e1HJHC8OgafQwg_ONw1d5QbRWheR6c3X4lampTba7SvSntBxxYU63rAiL7tMeKj7ZQx-PlzSA9oVeflaaP71ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=dceuiii3HME_VneMhvZyKMc_4d8EFWH8WA7vTZ8fKFvAiF0Hzdt76NisT2WIZUAoTS0NlKxaNdbl8iaq-wc1jXIoJtT-TwGglxmgCy2xQlxlwwRlEos9ciW5w1Thnb09ASK7ZlpQoh6-9KsMbsHnANpiWIw2J4hKifHpbXJtlqblMZOur2oGkPZ6Y6Rx3UNjrZ9HR5CMbVRcKthmgr-gYNlUUvCCXtqhqIdF9ELktx69zrQIpWvhDWKCQ_3AO5r-ATVwGpjizqG_Qt9NHiI_47PXULnL5gpYv8XwBb9XA_Be69jLmLjEygZ3R_b3ix0Y1fDEOeetY0Bx7kFTIiF-CgxC6qvuHTaEZc1hl5sinnhBHuph-v94bcodMVHxyqeLqGzF_hrqTIR52mv5InxZHUP9ShDyv-X153Uk_EA487uz6cWXSrGR2J3hHsNwFjXBoVFknu7O5fbs6hECtphLuJLrXMKIMlUOEagZ36PQtNt9s0Tn3s7OFT5SrmzP_iAhOkwauLUYVCKnKO3YN28TdBkv04UhSNcZ5Kd4Ol4h0tE-dtWegd23J92OLg06T7-01Y9_LRPs8EVEGvs3NKRfGdojdwzhUY-mmv2yFcAPXboyv_FIw42Dg4wu7wn6M4NLhYNaGucpI5EyXj5YB0Y-3GWgOEYc0gWDxhzYI5ELZiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=dceuiii3HME_VneMhvZyKMc_4d8EFWH8WA7vTZ8fKFvAiF0Hzdt76NisT2WIZUAoTS0NlKxaNdbl8iaq-wc1jXIoJtT-TwGglxmgCy2xQlxlwwRlEos9ciW5w1Thnb09ASK7ZlpQoh6-9KsMbsHnANpiWIw2J4hKifHpbXJtlqblMZOur2oGkPZ6Y6Rx3UNjrZ9HR5CMbVRcKthmgr-gYNlUUvCCXtqhqIdF9ELktx69zrQIpWvhDWKCQ_3AO5r-ATVwGpjizqG_Qt9NHiI_47PXULnL5gpYv8XwBb9XA_Be69jLmLjEygZ3R_b3ix0Y1fDEOeetY0Bx7kFTIiF-CgxC6qvuHTaEZc1hl5sinnhBHuph-v94bcodMVHxyqeLqGzF_hrqTIR52mv5InxZHUP9ShDyv-X153Uk_EA487uz6cWXSrGR2J3hHsNwFjXBoVFknu7O5fbs6hECtphLuJLrXMKIMlUOEagZ36PQtNt9s0Tn3s7OFT5SrmzP_iAhOkwauLUYVCKnKO3YN28TdBkv04UhSNcZ5Kd4Ol4h0tE-dtWegd23J92OLg06T7-01Y9_LRPs8EVEGvs3NKRfGdojdwzhUY-mmv2yFcAPXboyv_FIw42Dg4wu7wn6M4NLhYNaGucpI5EyXj5YB0Y-3GWgOEYc0gWDxhzYI5ELZiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=u1MXBv5K_c7DNGL5oG67IeQga5U1Vjb6qh2REE5ir4rJWnTnFy8VxPftX6skB6wUGJIcamOyALU45yUwNNorGttVnIHv-iLViodtNdIEfCIqrMSUY-LXx5zFmCKq4M-_GNJutKjpcN3nRI_vb3Z_ayKonjMjnzRvLMnCDCOm05SCKrpJ1w70NDryPfeR83h4VPabVB8MSii6y0qBPjXKxG3BsvF-jaql9-nZb799rplkpGv_JcxuWnvcDn668xSi7uqwXKVNoz8Tpt6jH1q967-hHuqGMFDbPRculaYxOLJZjAQ7yoStR3b2rX2I9F4r1DPvJO7-zQCXE-bWfGctCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=u1MXBv5K_c7DNGL5oG67IeQga5U1Vjb6qh2REE5ir4rJWnTnFy8VxPftX6skB6wUGJIcamOyALU45yUwNNorGttVnIHv-iLViodtNdIEfCIqrMSUY-LXx5zFmCKq4M-_GNJutKjpcN3nRI_vb3Z_ayKonjMjnzRvLMnCDCOm05SCKrpJ1w70NDryPfeR83h4VPabVB8MSii6y0qBPjXKxG3BsvF-jaql9-nZb799rplkpGv_JcxuWnvcDn668xSi7uqwXKVNoz8Tpt6jH1q967-hHuqGMFDbPRculaYxOLJZjAQ7yoStR3b2rX2I9F4r1DPvJO7-zQCXE-bWfGctCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Z2y77gE4IJ0BEMpXqnpHEBwxHsyAp5hVKq50wjwSdGe9MEu_vXKy1FHiin6n3ZYxxRG6pXv6_gOemtFUzdy_724dyS70qeCgUxPQVLUC9Ba8wz8jXknPFuqdvPO-LiFmjz3H03etJdDUw9Dq-S8vHYxGWo7ymftupKUKOeZjw4rCvhVjKtuOZW7wY9bhI6uTANuhEv991z3GOA4ZxW_UYp_2OeCpNvRNb7GHT9gARYs0zbXIP1dvdlvmWB7otZaJkKZyam4w0T40nGwsVxMVNJNWPUir3KMCbq0Cw_5W6Razo8fod7zpZhCawYvyJ0BWY9izyAGoM-Gscg6xfqyAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Z2y77gE4IJ0BEMpXqnpHEBwxHsyAp5hVKq50wjwSdGe9MEu_vXKy1FHiin6n3ZYxxRG6pXv6_gOemtFUzdy_724dyS70qeCgUxPQVLUC9Ba8wz8jXknPFuqdvPO-LiFmjz3H03etJdDUw9Dq-S8vHYxGWo7ymftupKUKOeZjw4rCvhVjKtuOZW7wY9bhI6uTANuhEv991z3GOA4ZxW_UYp_2OeCpNvRNb7GHT9gARYs0zbXIP1dvdlvmWB7otZaJkKZyam4w0T40nGwsVxMVNJNWPUir3KMCbq0Cw_5W6Razo8fod7zpZhCawYvyJ0BWY9izyAGoM-Gscg6xfqyAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd4mJuacDHZoSpI3V-ECoHqlHPEvbehngPhDETqhg4AUnITJajprVFF0fBBxK-Cibw5zpevIpO7x_ki5i0Dl4IXVhCTVjVQSVhCpxzygqBClTN7nWhFFiIgSttWuqmUZ7hfHS6UFSAKUtusJrNt0Bdj0dR7CtoYimpX-iD4p6ICbgo1hCWMG19UtturRbApTx6HtoNvJasVWRREl_b63P6QHrWoJbOHAUxvmQzkVlheHmdtXJS0yqpe6nbL_A3t-Hjv6w513RdbsITsi74O2YFObDhFXI-x7wEw237x4YCRM-c24LFvtK6lM4k-WQmBRlwkczdax2Woz-P5K4rEWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYNORaYdTSq7D5vqGAgXklw8SahgJ_CkDGRuOmtG40oaycVVqus7Tr2ij2jsq9POlEv-I27gZvqLXFijaVGxyxN6Oc_gCxgfa85cLYFM7MIw_hn7TUvmbdjP5MzQTmCpYz1RPnLhbqi9UpCBIc66q0N6Sfl5Lu-Z7TVSQmRqX7wgvvUzYY5rLPmUts0ooTuMPxx9bnHx0MejohZTGXnxUuPtO2noDXY0LKi8RZh8ZqjyFrrizrjuggWgikzQorfJ9WMPWQcNBFWYlUdoKdPetCcZbmpilIhEL6AvrE_uKIMBR5ewXlOxIml_0iQhxrXSFqRXNDVEt9SPvC-1-fmbiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=QYk-IJ9xcVbOazeubIiz40PUdZiM3QsFl12ff71ZXN07_-qHIqqn1AboM7ln1NExzwZpsxkyaOT4cvFTcbCLuToZwk_e4M6ugJDcUg-WDGkAmamUQ9wNRvTFokfRr9prwXNUK3KlHZL3wHnsGghv5IQziTLOw1YNpmMpmvdJwvU34DbfQwu5e7YNaiM8hQmS8_2rzhgF2LWD4riabqA2Tv7kqgPIcF1GGML9HzM-OgUv41eDtjp_LFKv77dmseJ0shj6B8IvXoDUdlt2XTFkeKWrOcXQIlg9Y6HdIbYqQ3N4Iv_0r2lSDbRMajeX5FYyOZprZreW7wTZIAupSoO2PYL4tbHfRXaGw9Z2NlWyGn0QBLOAXhr3rJT64nxEqTpdcJ_VCAAE6mqNNKGBjRqElMswFS9LDxsyp7VZDBHuGtIScYybEOu3P8KGLWjXIswybPln3n0l7eaS1Zs3Sa30-aiUQDz7LHOg_1NqpDAshTieuNLEEtPxJhyFTzF4FadOtEmq0A6-VpmhK_vWjYbOIfMFVYPLQL0iGO7ucX17nWjNWk6MjAHMEM0TS8ZbvyrXBjdc-z2MZdGYqhcUnvYqZGblN1dFK8q6pQWNtK3k3CyfLqHn4z4AoV8fuEBJgjwLq4qohlcZDi3YVFIkuG8_3s3tIgxZZRQMsKlFGwfuceo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=QYk-IJ9xcVbOazeubIiz40PUdZiM3QsFl12ff71ZXN07_-qHIqqn1AboM7ln1NExzwZpsxkyaOT4cvFTcbCLuToZwk_e4M6ugJDcUg-WDGkAmamUQ9wNRvTFokfRr9prwXNUK3KlHZL3wHnsGghv5IQziTLOw1YNpmMpmvdJwvU34DbfQwu5e7YNaiM8hQmS8_2rzhgF2LWD4riabqA2Tv7kqgPIcF1GGML9HzM-OgUv41eDtjp_LFKv77dmseJ0shj6B8IvXoDUdlt2XTFkeKWrOcXQIlg9Y6HdIbYqQ3N4Iv_0r2lSDbRMajeX5FYyOZprZreW7wTZIAupSoO2PYL4tbHfRXaGw9Z2NlWyGn0QBLOAXhr3rJT64nxEqTpdcJ_VCAAE6mqNNKGBjRqElMswFS9LDxsyp7VZDBHuGtIScYybEOu3P8KGLWjXIswybPln3n0l7eaS1Zs3Sa30-aiUQDz7LHOg_1NqpDAshTieuNLEEtPxJhyFTzF4FadOtEmq0A6-VpmhK_vWjYbOIfMFVYPLQL0iGO7ucX17nWjNWk6MjAHMEM0TS8ZbvyrXBjdc-z2MZdGYqhcUnvYqZGblN1dFK8q6pQWNtK3k3CyfLqHn4z4AoV8fuEBJgjwLq4qohlcZDi3YVFIkuG8_3s3tIgxZZRQMsKlFGwfuceo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1N_P8cq9ImKyEKqJPolC3cRrj-pFayQ_Gp9YG6C7DE8R0ievI40xODRMuq0nN71jUNquiJXRwrEUkUKS9pE3up3MvKzXCR3zJsFbMmWOyC8zRa-hWHc5_ZAhxG_4DEtnn_4kPVN9gc3IAh475cs1QrCPNr-33cvgj-u4DFFR1X_J8OwLXZxV1Ivix-b4E6wsgJw4TCQ7QQaaSXzMi6R_0zv03nwto8XFVNjBOjFXlXRa9aCPFO-SuUgiLJcpuI0_WBkPk-r_fl_YL5oympMuGkqpoipZWHR7ImR0vQxmnUm1DNRygDDHOwF68IHljZcIbn9lDsoJ_xmasBNeVX3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-eILYitKtJnTgQjrmq8hSuAwf8dhztwRrE6zgKmYearNRsKFaV39WgpIeMRRjYd9-m0NGgst-ZXfDlzTgQMhLcZvnXq1MDHPiBt_KqgOZrlCgXqE7_Ko9LaATM0_HdNTHPc9ojjpgFDi200k01qhrWLvCU5s6U7pHx68M9vTkAj6EH5xrOqziaSqaBD8mRSSEfV1fRy6-omKFlBSpezoIxGEHNPYBwdLE5O1BSWWKX73f9JM14iuaKqD8IFCr3_-pj5gsCh98_aFIMPrI_lqlCALIF2AmxcZnF9LFhhK6Pthy6qJdcm3AWSpbXI2V8sqgTnR1VE4TpoK6ZJGsFQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V70ttz8IZCeN8Id-vt3XyuZTpQUIZRNNAdZjYiOWH3PQX5w6JNEqWRuMVvkTIb3945Tow557sSX6977_PwdWhefpBxSa2SP0AghLkOp1-7iiOdE7OP0bmmCu2XwbRxVnxfRARN_EFGwZw18-G5w6xweIhqSxTML0lkvH92L-nlQH80Ym__6dWf7t89OPeSti7GY1R3GfvbrqLePI-u1WTHjUMyg7kCyV3oaw_91MwkfRrBuSIpGieRzFU0IoGIZQsW-FY1t1S22PDHs69jp7itgjbCTZSaej-0Zhe0cjbohrVb95geQ5cWmsDuQ0FzVJU-2hDQUDZkeYAevYiCYvRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDG0pV85yf5o5sHj_rWpOBaD4ASVuWuJcxr71r7OAWlncnVyjJ3lwspVimDzGt1PJDsSiI4zzacVHesIUwJ7RnZWxgdplAtPYr4QUK2Ond7VWPX_g__dKASxNPBX5_LoYgOrNThn690GnsY7zBmPE-r9_LgpYdIvg9xih_2iP21dPMY0Yu-8TQKY_sNw7dPynnUaEDVHaa4pLgKoMGkQBoKnEyq76LkDOBd-hz6JtlBXxu5g3XaEmOXZKxWgH9SLufsDtsyU9Vu1LTJPSTLx9OnC2HU9kkmowjB79Pe7Q0Mgoq3ndQdj-Ek7epa4rABjhDFwHF6O-RqBvyK018pGqw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=DK6l45EAJhJcrLu7Fw1vBl8P5_xlF8kPpL4PSV7FBqiiC7vNWoTDsMBAk5Z5C5NLsF2wVQZ3t_1SRHybWK1NhFUKdjBonecpFRApXmoLCe0N0oUErjob5h8yoC1IEUZEgWZGzIotYuo0WQyFymuk99cr4_ZlkB0cGHb5YHwPyqVtuH0ifgCfvIMn9Hoxd08L-86AAIxS5B55_kNAxTtYV5cCSc74ShUIehlQbkEdGz8hyQh7GKNnBz_HmhVmut4ZIPARy9V3FwUF93ZQ4BA65hFvdB30KQ6UwljK1ybdvQfwGt-SBqaSoBAQ3k9Cz96fj4aRxHn_kpQrXlvzJHuJ86EQrJBBTlLKHlBlkdKDXv8OuoUxqG034VEh2sjQgkvXyPzgJIwB-WJmXzmruBDLFDh05G9502RSkRVFNDIfYpRF4r2V7IlMBa6Qxefq67N8tJZM_Ejx-tJVPXRsXFPvfqmMW07uO02Z45-3gS69EsmXXAesxdC9r2mjlrBIKVR7LHQ6u7pQ812L_9Lkkv80FRpqm_Uqfz0zN0NYb_t3YuGgCVeLjydIrDn7lPxiJFrDvOrc8SfYI_QhxIQyf7gTvTgl7Xh7VKdWVkQEXkvD19xzAYMj3XlmZg7sJZLwJSpLVgQEY9IeQkUTojlvLMkKRQfdB2ayjD0Px3mosCmmK-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=DK6l45EAJhJcrLu7Fw1vBl8P5_xlF8kPpL4PSV7FBqiiC7vNWoTDsMBAk5Z5C5NLsF2wVQZ3t_1SRHybWK1NhFUKdjBonecpFRApXmoLCe0N0oUErjob5h8yoC1IEUZEgWZGzIotYuo0WQyFymuk99cr4_ZlkB0cGHb5YHwPyqVtuH0ifgCfvIMn9Hoxd08L-86AAIxS5B55_kNAxTtYV5cCSc74ShUIehlQbkEdGz8hyQh7GKNnBz_HmhVmut4ZIPARy9V3FwUF93ZQ4BA65hFvdB30KQ6UwljK1ybdvQfwGt-SBqaSoBAQ3k9Cz96fj4aRxHn_kpQrXlvzJHuJ86EQrJBBTlLKHlBlkdKDXv8OuoUxqG034VEh2sjQgkvXyPzgJIwB-WJmXzmruBDLFDh05G9502RSkRVFNDIfYpRF4r2V7IlMBa6Qxefq67N8tJZM_Ejx-tJVPXRsXFPvfqmMW07uO02Z45-3gS69EsmXXAesxdC9r2mjlrBIKVR7LHQ6u7pQ812L_9Lkkv80FRpqm_Uqfz0zN0NYb_t3YuGgCVeLjydIrDn7lPxiJFrDvOrc8SfYI_QhxIQyf7gTvTgl7Xh7VKdWVkQEXkvD19xzAYMj3XlmZg7sJZLwJSpLVgQEY9IeQkUTojlvLMkKRQfdB2ayjD0Px3mosCmmK-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
