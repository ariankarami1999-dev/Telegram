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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 354K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCVE6HlAWxg1NzjucKpHQrHg5zHGdtpSg22err0LnLIxi0YaICPHPJOFadFO5BhIQdoVoZ2m2fipH-jbgS010ley82XeXQqdpajpq_zcTiBaH0mCRAF72qhMqOMF_k3e_S_zs7sAXlKwlDjSn-GXgp70UakuJ4goy8KlSkVF29El3dyndnXC4Iw5S53IiqBSZbrgfMi6l2u99VCmzgOn30ehE9bJfHi0rCYLDZJs_o0LZ1NvfRDRzs0o7AbjL0pavXcrK6GYq5UWhesHZLCaOJM3DCutFIJenNUxUWm4_NSzeFpBZat57OBkrKNQouwH4ALZzQYyhd9WV33pzFlb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7pbdCQVrLc1N1lqIiyUJ7FtyXPhSdjngbOwwKdDZj2Lqx2OkWzQZRXsSsIm1_YBp9yJxLenD8zvkHSmM5mV6wXhUkPqQnbgDppKdVr6KccSRx7jxCf9F1cNxm7GRIZ5Q_7f6FcPu7Z2owN1oLF39aOpBnQMj9KZLYGBrW4gShQneROTFjaEZCxNOmeTsc9VUjlyfq5BsdwsFZb7UTgOcJQtHX7iJRgtXFHiYO2elcpi9fRGJGPyhTBT2JY_NJ2X97A3KYsKA1AD5MaiUCMBCV6S4zJOt5-wu2ItzyDlOFkqjSoioIkUBRlN9t-JAvaIWL02e0g-3VlrajldVPhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTKWkkTwTjGE2_jXoAZzvfkW9JBHMgyzx4mj4QECP9TE6AZE4lpz7SctNHmgzu50PguQFzOk7QtO-FO7bhiyfffH0Qc46ON6fWzlLPMZ8CVwA9gR5dveXliJ4Rj8RIUcJWdFDJXn9tBoAI4dCD4UfALe6ZO6k0j_meCUqScEQI9kHxHgmVod6PPmOQ2tcDv6LJVVMv75tkKrse4LwFgjDBCWKwVsvuOwxrQBKMf4fTWsXBiSFxOtcQo7c0D6-MFwsL-oero8cwXVRF-y_mi6AeYyXWLIOwYVOrtHjlZmLDHgotD35MVraTz2hD-Z_W5Ynxv8jT316TDHuggLZOhLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مسابقات جام جهانی 2026
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
10
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPZ0ECAd-KglmWEFVZY1mDBiPdFXafp0Kb0bPrOVXvHIOOQ0OhvlEKQyPk5Ib78EiUKsSQfb_rEO98nUSCw3cnrP0o9qsi25V-JljK4dWwGc1d-GGvN2X__OqcqTIJL13uj6SstEUA2w84xQYdmcmvJb2A_Gv1Zt6hAEaXXjiq7xPL1mpUnAjIXBaB3qwc0hCwV31vRXJ96Idnar49Hu7na0Bh38FWhIfnpS3qyZ8eKUVFxdnuF5ruuW6JGW9pG6mzIm_ZPjpAP9kqnmO3XLMNVH5E9LkyQivuvQxKg8McpVofUp8M0ZZaDP83tb43u-I2bw3vA2TC757TmxaAKhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5L20TwjVN4Kg-WsEnjGXvp7AK45ZTP1HRIX_SSLF6MAH45BbPjDsYSjsLVlNtnPgU3zAHnprYJtfjsGfBdfWFxZVaE-df0H9ClOfSUw2tCLkfHvamR5xBcOgYv9rXSSwSLaU3e1Zwmnxti0ewKTAd1LZxwrPqh8vj2UXuOyCoORa2HvfwMl7J6FHZrEqG3fJX2hzwTeKDawFGgr-PZ_-f6F229s-KbCrhug3yrvvNyuJDMiW5OjjkTniICeL7kSvEz3wUV6o7p_ZN0lqPmsAr6CAHs75beWRKKztKVRe6mYFHW0jEQhcafVK_i_PHWGAfz89RKOdrab4N_h7DA0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkTiw9gGANDHHg-HQJq__aCJ-bKJTUrvWBXDLJ-1fNnzpiETHU7cF2AeQBYNUUiqj_IrJj9qUslvpS15A80D_PBOmCPHcawKlWeU_erbIgfTf1yGclrb1wD5enNwS_2SSjm1g7FZh7MO8PdWfHeyxcovQlT6FxdfgUOQOWc3fTPq6NYv-wOHRfeBaSg4fKahPwmzfNXDY5oDY6zhCyVKlf_DT_adcQTPDcpGZUojyQ3cllI9QwWhHITfV6Q42USpALXjAbDe77uKz1ReMsfMVQ85Q_7WwU1137W5GPFCZRhF9FKLB-H_LdUUqtwicr0c7C2vXJfT8SWWQsuD_BxYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRq2fCDXZuftFze_hnX_ozeAyhB30sAiQlJX-RcIRziXO1ddeeFSKqvzqLk7jGIWg6G5qJ0a-oiWIzhTXYQh6n-w7JQdB65yQsSjD4kxsOt9BgOhkI4PVoJcuptmbuSJCkoBHdaZDywMzRmTfnDzHshtMPbRuDa4oy4jQ6oyNnr-jrK5ih2nSe-xat3iR_S3NOt3FpqhQXhA4OhbeYvIblMoBNrbLcQ0rlDiTb3u49Q24A6OVdo60-7QymQFSkh_l3rm-aF5YMcM9hbSqBryTq2L2Y9LLQ50f2GM6i-nPDXJXuCEYxKdlumU_ueFwPnbNnppCa1mUsWTdFOxRuZ0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRnw_GU1CytL86oa5O7CG0tOlyL69GvoDfJehcNntEwngaPuomeDvaHP9Y14RhoamHHkOoGKvsvQH0BA0ooyY-0xP-Zf5ahHMD34oIOjVxH1kyyar5hVCbYw6rEFg3KOlvMWlvtsIrmP7mZFdp-o1jseskgjopA3o6_78Rm5rfjfrK_XYVJRGYM2WFUJtPJDmpYduic4qeBk-8bWyMHAw4_y33irZf1ybed6NdSkASsX3PryfwRNv_LbPZxn0MnkQEtEh1it3TMg9yPIDovlfnBsgdauRPji6j7011_s91APQfPXFAf5ZzcY1kxawlStE2A_q3y4zNRDybaMov_OTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhtbR9qeh9prcM24m5ScxjAF1n0l4_ZVTIbjGZ-84A9hwA6D8b9YD98npou6_wsgJachA0_4ePHNL9TeE7F1UQpen3QOfWGnTMvlQr0D53dDbPBboRbK0a5ukgc0tXCj6aHWnpicQ6aOYS9zc79YZKJQ5JY8I3Y9UphLs8DkP_Bt6zDcl60Vr1ZnoIQb98BcR8DywdU9woqdrMRqyd60MG0OGYqX28LZogwM4Zy65Bf8i-ivJDSQPshAT9aPenb_siYTfDmIqWKXHwpoPmrzsLtu78rJ6Qf68srxce6EwnvXcMvzRYwiZGUFG6c7QwW0NxCqB3UWH4kC_nZx6vnpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsXn43jIztpHSZgNdu2NvMZ2F27R86l2uIOIJanMRpBU-Cj74m2myE_yV4qV1eaU8G3fS7jDx0EZJYKFfxCQJms60UIdd-hwCPVxfCv9jH0OVsnx3_rIbAh9JK1ucgOjfwxogQFVi59fDJTB8Rii-D14Xsts_MlP9TqmIm5zt4r5Oql4gND0EwoGp8WHrlxk9QyRMeRqNMguJGFC3rVA1Ja6YYQnlZ3LqOoivhY9xtFk26ZfRrUtphLK2OP_blKzr20OyDvPy7e5CCkyMywh0CSJtLvmT2dGZWaGaCO86_QlmLAK3QkHyXabOUaaG6LBpA03WTDxu9g0MrlxuhqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB-hH--4xNvW6DXy_FryZMXSay6XXmVnArwoRRdSx5Dk0R3AMtupTVEEeL4Nb_m5THZljkldfsPeeXSAnvsuitl0VeAcKiaICvcnOV43n1_5ApDVRNpBSC-FW3ua9g5L6DQSqBUivHT9f8qlKk7NohIWs7-il03jnq6uftU_EJfrA8UMEA7BybMZ2cxUXV00rRMYIq6Yx0qFtPdZsTyy2bf9HMOgyKs3g91VrULrWuMakHg64nPErNrKULxecqtD5t1cusq8fbcge4MiM44bnq1eRlXyeBsFlaRM6mBn3mL-AGC3_rgF65yh3-3wEmAeNEXiCSucw6-SVijkFhRm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPre9ioh-hKOJgI44WR59pZv5Vsm_kptPaO42V2FF79ueg0rai5VtSMMCG3FTJ_9lTsNb6-EJzmo3dv8xuIya2kbu0n2RVrjVyC8t1FGcOsjUO0fiW2WOA-AGzYpjp3CI8iM5iPLnUsCfqaxDweq_-S1QfvW6XBv4fLOY83muluyfPJeJ_4Hjhgby0BKIleA9Zm5wKaDRoB1ysoZxPcsv38PsNWiW2UXjY32LcAZSdPPHwG--ZStkShDg6gGM5E52H1XeLgdia5XghbPJHa21w8QwNdRMABxijX8LN8FqnilL2MDY9eA1DAZAObgbmwscpuFYwbi1IaQvPVLOpG-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob746JB0WeVNTF3h6qcimO651er4NBPIHgDyApgrv3U40JdzSBK7i--sOXFOmMfJIPfa_oNaDgT8DJqZxxijeCuIP3oacWYxMfedKwsuWNZM4LfTWU2ECWtx09XsWjVgrD8vlewJes0AzojFJLsajKIu4k8PxCIGWqXbLwuJE-GL7df3yvb-XTm0c9hzcoHg1zmvgDts0PHHS285xLW0mruDaRQCQNi4OYz4sB0hrMSgnQ0q7OXIr24DZx0cCBpc-f4jh96LK0HyrwYp_YurlVNtMO78A5xttMODAPAAtLGp1tHQjh1jx_wK8pxYTxNoSN4AJGESy3T4D0R-O1AG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz4eyzebVm5kHOPACGjyRJiAoKLCpVgh62rBG8K7d85g0RBNVbARhpnm-Oni1CQxKu2l0XYFJMdHhNwI4mvAk8dYJLXqLn8neAlVMRZnKAPyAbRfhfCLS1BaL7UZ23q2H2gRKWQlb-uX9CquuQtgezDDjcS_5UJ7NuqhDXhUtgpmlruDShL8KHQT8Aw5-lmb87GbhA8z5h4tcUsMcEawTVuTgA6PaOdszHy__NqjR46Kuh7Sfew79ht-Letja7TtKqo4emCcgEboy2EOswlbPimGVUaVU1FHdaBy_j7J27tr3Z7Acnbr-5XLCQ9r88VWEYLAMIsirzXaIMNEdVI1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwyRuQIirGdXgfndOOwf2a1XJtJ_E7fAXhzyvesTkPDmhMb7ZnZpomFL7C0Z2g_JLAYJytqw95sNictfJNQfPXu7rlgglg2053fshV24D5S5SWYyvxZOsuV1jyyHVRWtgMW9DzBJphdQyo8Jm1lNftq6aD0-vkHArJIiKgwdutrxJXLUkJgjoMfBfDcnzMgwgLNb-4COCtaDIyMIWUPXpC8fuOhPYf0EpoxuSB8Zd_E3Wtu2QtxjIF73HWUuINsmtqzCIf52Mw2Gew5YLyawuFFqWHKe9Id8cv8Pe6Zm-0LRY0rgKIJpYRORu9ZfKWCxIS5xWqiNP0q8MzmEcFjX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLFMIRWy2Bbn9kltYxkND_ifcuVQMmXg9wIJNmXtzZkH2GH3HgOvnmY_zIaiLCgeubrbOra94Z-FeYIBrliROz3Xt-0mdNfQ8HV1mT-h_1yobRThjCNy2w8raGt4csO7VQBg2406RuEHf_PyztPGS1AkD1kREysLZNjSndL-Vg78YdSa3FQigiyacq7i5rEkErfXaTjeOsYxCTd03iKhYfX8xwr_Vm-QsWCTooIl5sDXne3f2l-IAL9HUr6GOMS24SYCM1JcqVXf29HDwbldQhbjbBa6XT6MvG9Bg3DzW4b-9PPPbdW04UKERzKSw4Ok0RsLO8uTujENT9i8RZ-F4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH6rLnek8DnlVvk34aChGWtOLCjcll5Djr3kxiIz-EygLwARQVjJ_ejU6-a16mp0WMaFJW18eowrXq1-nr2TSUDf3mVzP2BUCedGgh4eYHK7rp_KPKD-QgwqfsXaUIxTbuhvMtQ11Do3zTNGiqmIhBqqXBjyOFqTRSo4XH7Aa9mynrz694oKLOPSfdHhnBgCjkVZkBOV1sLINeGFalzrUlGDrbnASZGtkO5rJsTXR797qKPZMKAdUOdz198GK7o6KyZZT53WJ1sTAbbALh9NM5P38wC6MJJhcopbeDpt2CO0SZb05JD2hDM5vv_dJkGePiu5oFSitJ8V2Xzk20phsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMNjOy7JyPNaw0OlhsSlfWlT6jqYFMpmD8pijK2px76_zAowHX4Yg7slLILazNUq_v1AbYwuMNr_MEgYlsiNQgcACIGaWFIS16k7GXK7MuLOj--ZIw-eyktyARzlx-JadecfZbD69Kc9XyPtuAxaR72MMcHWy9rY9se7KDuyb3pmtx0hgghYN1GbYhIst7huiYWqL_UVS5VfrYWhFeEreFEWcroJLjlZJ37n_m8VYON3SL9w2YPhO0gh-otzJDWdduUdRJ_mv2GzVC8pc08FjbKEtBu1XxPpck5mfudALL_QzfkujfJj5c-9o8Z0RKNTIH0K5fYwtYCZE_xOpr0-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=UPTzjxwLU7qilqtk5wDYT7RzsPMCdbq7TYAjY6vKCqJokfv6lccQDlVDaPsJNWAfdtiGsiEO17ka86jlEqmLg_mlgZpyaYe1cfZUYF4ejLwuPACOdPugb3cUP-_hEeRSxReYj4hldA8i_45atyWtgyb6jcR3cSvYIBex5R1DiQOYjj4WRJggfvOojW1qZ5NfnDMXNtpZ1fT3AaSeEIhLyB7aXVEC_l2cUpTaOCmibPOqOb7Kd1T5otzQm3KBXCl7B3vEDLwRWd-u4-bC4cl8rlAn0ZeblfUSlQ7HPOOTV1fzr7DyasuBZCREuHN8QxoRApAyUO_SDLz2GJkV8Sh4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=UPTzjxwLU7qilqtk5wDYT7RzsPMCdbq7TYAjY6vKCqJokfv6lccQDlVDaPsJNWAfdtiGsiEO17ka86jlEqmLg_mlgZpyaYe1cfZUYF4ejLwuPACOdPugb3cUP-_hEeRSxReYj4hldA8i_45atyWtgyb6jcR3cSvYIBex5R1DiQOYjj4WRJggfvOojW1qZ5NfnDMXNtpZ1fT3AaSeEIhLyB7aXVEC_l2cUpTaOCmibPOqOb7Kd1T5otzQm3KBXCl7B3vEDLwRWd-u4-bC4cl8rlAn0ZeblfUSlQ7HPOOTV1fzr7DyasuBZCREuHN8QxoRApAyUO_SDLz2GJkV8Sh4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=q8ns6Il2aVwkOGdLcgZVoR-Z5WIw2_6IwBK76h1DQRPZDwkLXdd7vcaErP2B_RKXVpxJhBmMZYwhv4A4_LY991N2OczbVcp_Sx5jE3sufX4BHkncaZmprusPuHPG5ld2DPbhGD68_PK1KU43MbV3u7gYqclWPNxtVeqCU2ZOpsvYLXpLzXnPt8pe2EgtKvLDJg-g8SqcjQgkYcLdPHIklz0ODxeAgKi1YbiwxP3oe-Sl-vNT5sECc-ZtZMj5etd5gr-AiIPiAHpV6O6u0aDLPkXysh5TYodqLDF163oOcxnPArmrxEayD123AO676X0oUMZ5IP3S-RILAnsS80o-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=q8ns6Il2aVwkOGdLcgZVoR-Z5WIw2_6IwBK76h1DQRPZDwkLXdd7vcaErP2B_RKXVpxJhBmMZYwhv4A4_LY991N2OczbVcp_Sx5jE3sufX4BHkncaZmprusPuHPG5ld2DPbhGD68_PK1KU43MbV3u7gYqclWPNxtVeqCU2ZOpsvYLXpLzXnPt8pe2EgtKvLDJg-g8SqcjQgkYcLdPHIklz0ODxeAgKi1YbiwxP3oe-Sl-vNT5sECc-ZtZMj5etd5gr-AiIPiAHpV6O6u0aDLPkXysh5TYodqLDF163oOcxnPArmrxEayD123AO676X0oUMZ5IP3S-RILAnsS80o-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdVErKM_7oWOpbETd_4a_M5PLM_ArYAmW0tX5TUnajZaPU3aHb9MF46m-C_I-fpSVHDnmKyJA7dhdpua1VztbU-DTGG-0WTerY1_WriyhDk2OyIKrsMyQzm5gXQSzmhmUmGOQbNKxq_fVH136ecc15tjvBOYPNFAzqMeP53CO8S4KK3iP3x05XU6ys6uUnKmbuO7upA6a2gnDEPlUDmCAr7d4ZPhKCX6RZma6KAofS9ee-nUI61HUUjq5wtTLc7qdvOq7vGzmcseu-dulEd8_7N8PvlhZRU21FRtxnJbekoSuV_VUFcFDScCbff5guF_Hypa9tvxGnqHblaEDLF1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUiqZJqcialoEropZXFSDzf1PWe-IIcSiJhM1LPT2lUMizcEqEBULPS-mFBDdemP7WZN4Re7YwGld74w7EQxQkt4GZhTMlimxK1e_msSloqXKei3nVpIT65fyKWV8ZvsBBwqmcmagMXYAO0Erfkpphtzaq5RLuoOrAOzBiBHmO-9wcLnXY9DAF5dfo6j__hIWT8lhULZEgNRu6kmxtEyH72Wg7JYKeYpoaSMUDLDiBsKQ6XEf2Fd1BIvkSrJgdHbBIPTWQvSBufShs22tJIiHJ7pGZyD2TGxVe4trgOJQDumdlCj6CGtljeVvPvwyN9FsT6SYKt7AijE74ZX29w6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=CF-4-ggnUtqL62Z7H_fpmnfVLPpdqMicBdT0t5AJmg3a2G95XrlzfVKyDJCE2Y5RQTAQR2HNrM17d5g3njyVeRZ1ufGsDdZks2SMScqoawMl3KA4E3ktJqToqVVo_zBDxJ8L5GfXekxsLP5WcMuSa8f57_zP2SzcqIvRDQDiI9dRFLMyqft16om3s7T3wJ7646dM7_ILF64XWdI-KXWTJbOpLcYAJLyOCQYfHeKi3Ypdo-Q8c186XkmAJ_MsjDsMvK2i84suZB_-3TMFbWc8HZwJCaLFx-QSYTgAQm4PuF4j_HoIW-mB5aDY0700d3qsbbs8fT-QZ6NZWWSFdmAY3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=CF-4-ggnUtqL62Z7H_fpmnfVLPpdqMicBdT0t5AJmg3a2G95XrlzfVKyDJCE2Y5RQTAQR2HNrM17d5g3njyVeRZ1ufGsDdZks2SMScqoawMl3KA4E3ktJqToqVVo_zBDxJ8L5GfXekxsLP5WcMuSa8f57_zP2SzcqIvRDQDiI9dRFLMyqft16om3s7T3wJ7646dM7_ILF64XWdI-KXWTJbOpLcYAJLyOCQYfHeKi3Ypdo-Q8c186XkmAJ_MsjDsMvK2i84suZB_-3TMFbWc8HZwJCaLFx-QSYTgAQm4PuF4j_HoIW-mB5aDY0700d3qsbbs8fT-QZ6NZWWSFdmAY3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=FNF6uPQFwxtG8fT2pwtMnWHLKd1lDJ63FGvliaqI83Ix1AL3Oonwshe0RZnhDWpD2MZJZLK5xucbTqGSksuPZLhDgOqzOsfdW9RPz5jgilkMAdHjWT-ipr_Mk9KTSIABppqofkZ4esNX24MaRsv0NNClqN7j258GSJ9IT6agOpVCoXLPEEPkuyyu2x8CEtme2cSS-u56S6f_wydg4mDRBHzz9ZrhHz1jZP4BXjbRNIw7ed-SGAQupoF1RV0LZk30jm8phk6gePvZ3jxqRYDjE6p4r8va4LED3H-a907LQxWeGQbC8WWTjJj-PodrZKPwp3aZ597c_BA-pfGMpyjvyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=FNF6uPQFwxtG8fT2pwtMnWHLKd1lDJ63FGvliaqI83Ix1AL3Oonwshe0RZnhDWpD2MZJZLK5xucbTqGSksuPZLhDgOqzOsfdW9RPz5jgilkMAdHjWT-ipr_Mk9KTSIABppqofkZ4esNX24MaRsv0NNClqN7j258GSJ9IT6agOpVCoXLPEEPkuyyu2x8CEtme2cSS-u56S6f_wydg4mDRBHzz9ZrhHz1jZP4BXjbRNIw7ed-SGAQupoF1RV0LZk30jm8phk6gePvZ3jxqRYDjE6p4r8va4LED3H-a907LQxWeGQbC8WWTjJj-PodrZKPwp3aZ597c_BA-pfGMpyjvyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnH3nDljWomOta-rpCNarkIwZSpHuCbl37lHw4ylsJOyuL_QEGf6o9AYblr7KK_aeGfUrmjR5Pzz3QdpB3RPhs0vrv89ckB4sYY82wKQ1erBs9npHzEzedcMFk4nAx7oOfaxdfEQ0MQmpqj9OIpTuv5wyyKB5ZQQOw-lBUBUyosuRg0j3jspnrQ_sWOJPgjbKA-Ren-dGJ5r0TnHUx2smQhGtsrnumCihTsO4aYacE5pZGNxHAFuagh4QA77qFQdfXc47TCgcKd9lTadJYVSdqh5TKVZeMzz4df0JpbeyQB1Nsd0Fdeaz6FXbTmBWWZATg1xXbrEiIgj4ZB9kqtCZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqF2Npq2bWd_1pnOPu_QblcJjHR-Ao_1_STn3H5xGaqNwDKvVxPVh5nPGgM-rntGxGXlKseRrIegqIjHFO8HQYq_afG-NPZ1-J3-X5MrdKkv4KMwHubD8NCu7cDMAP4fkUEealK4pKPdhRLH9Whwj9EyMi2o8xkrFImnGfjxUrKnrZQ_Bq7Z0cRJT7-moywpMxKTM6brhiOjr8c0dKYoeJqrfNXAolyrr2GzUYrvLoL0fYkb6_Et87NdYOx3FO9RireCa9b17JuSL_AMqTkfb9InzKDQa6YlMOnlQryhlHD-Jed52P-4AvJRslgkMSQXXPmnUkaF_8ZUgOimmlYAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2kl_Lo8OK-DQawo_WwoyAwsZCO5pac-owvNgGylzgfeAVwqjmx2TzHBmyG5hKQRIIIwZBQn7zNRooo4FkA-lCj0qR7SPzHrIhtdPkdzZa8Yof85929Wf-uNJIP2t4t9A1QBLHnSGmzmRbb-pIMeRfTUrcfKWV8brTPBy_whWQwwg_2hYdNlF2xGsSI1gXCEHv55dIGYMNifaKLiXbEJOqUSEFciY1pm8q0gw_zlaPWf_v-S38cJrzUk8EDl8BhJ4ukvESycWAfLzY6ksUoqYFtziER1ZRR3ijxWBCF6HkChIoVKx1VobdpW8_HkFh--ecxXg_ks5OPkGxqxQ-HADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXCb8wY3NZMHal7rCCRtk0WHZRorO_VUcB2kFbOXI7LJNFwNo9kcHk3Xkqgi7rkl73lA7AkS3H6Gf0SNGLc2T2XH9W0f1jada9nhvsjxtm16X_nSCUyq_hgBZSfubNr39z0lzW6jYSf0nBQpRcg0lu6Hjy_Ep0942MU-3wXGjogy8f0DBUGmtxuQF2l5SngHYo-xTGzVL9cLa_eZ1NGdGmB_RaCH8w4oUtEhr8MSixDXu2UeCoX3P-t8rpfG1dIqyd40pFKjBjEbGtdrSCAkrUbH-l9L05_4piyPLc9FMtISePr-yO_oZB-rLn-gNdYl8-alJiMEeU4HNezbx1zPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=cbGzNG2Uq6Zy_nOp-7TVgwSAGOvFlz0MLTd0XaLthXkm0NuE8i8Qwms0GnsfDJTsg3GOqmeZwmAm89C_NWcgYxcv8zfuXturUTWsjQCo-46I80o44pa_8fx6wqN_vUD90qvomLkc-xF3hByqaWHq-zKKcrNU6dGfzvVFjp7zjph322E5ZsC0UtNVXGG5DFfh8Z1LeB5J8444rWIbHUUBMAXPciaTR1y0ee9WZ_nX68YAIov5AuuOfHRe8e7n73zWtJ87sDeFGbV47B189-rFYhMVBLVStjzdO1LPc4lwWFWpqgiTHDso8gQOnzRqMB6zvkOdGdY6E2GVNRiTAiPAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=cbGzNG2Uq6Zy_nOp-7TVgwSAGOvFlz0MLTd0XaLthXkm0NuE8i8Qwms0GnsfDJTsg3GOqmeZwmAm89C_NWcgYxcv8zfuXturUTWsjQCo-46I80o44pa_8fx6wqN_vUD90qvomLkc-xF3hByqaWHq-zKKcrNU6dGfzvVFjp7zjph322E5ZsC0UtNVXGG5DFfh8Z1LeB5J8444rWIbHUUBMAXPciaTR1y0ee9WZ_nX68YAIov5AuuOfHRe8e7n73zWtJ87sDeFGbV47B189-rFYhMVBLVStjzdO1LPc4lwWFWpqgiTHDso8gQOnzRqMB6zvkOdGdY6E2GVNRiTAiPAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGilw-Fu1Uy7L1BjxB0OQ0OV--cgMtafEtC4PqHrb-yzRyGQtqqeehzFz-vvWywkymPis2QJ6jy1GYgWM3FWWmNW_O8tMaY98PWyo437ex2FWx4bD3eDoLd3iec7G5vA--9TixQJ93owjDek8C5_e14nbGIxEPTMXIqx_reP-gAQtwpS7lRIZtHfuRPRO6Ist6r8Eq_5KoGWbnB7NnF6cskpOqiEO3CBs5R9Zrf5rxcBYHL1ml5KZWwZYWLRhIgs9lY-WvuKxps8gjbqJdEbMsaz4uFVwcS6sEg8w2P5tck13FKZc2S9IDZWzzarsPefswJV_vuVI31ytxUAN1CvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=pTBx9FZVNKIs_j5qucgHj-HqTLA9chFkylT6kATHf9pO-Ti-6ufRAr4iXxN6N_kuJT5QqrAH5BYF-kP9DWl-RGsVPwRBX03RieVXuwfn9AZq7ccdPIEiIdZNCuvibkfbKyp4tcx7yhBCzZbAUq1eFYGolMZCHyZiQK6I_tAV-2WljBPSK830yrB_s-WFyGNpxXxow2pXkgiQLZSz3sVv9tSYrbhT55qEJi2sMp9rDu9i7jYDcTU4_4eASQGiB4xJsJoCAuAVg-Jrn33_tpmQ0mIAgvnSsIcGyQhSKBE7wYOQcV60wAZKjIxH0no8CGvpuAaRuos7awR8X_6L7mW-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=pTBx9FZVNKIs_j5qucgHj-HqTLA9chFkylT6kATHf9pO-Ti-6ufRAr4iXxN6N_kuJT5QqrAH5BYF-kP9DWl-RGsVPwRBX03RieVXuwfn9AZq7ccdPIEiIdZNCuvibkfbKyp4tcx7yhBCzZbAUq1eFYGolMZCHyZiQK6I_tAV-2WljBPSK830yrB_s-WFyGNpxXxow2pXkgiQLZSz3sVv9tSYrbhT55qEJi2sMp9rDu9i7jYDcTU4_4eASQGiB4xJsJoCAuAVg-Jrn33_tpmQ0mIAgvnSsIcGyQhSKBE7wYOQcV60wAZKjIxH0no8CGvpuAaRuos7awR8X_6L7mW-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkIKVo2fNb_v8HTMG3JwjMQgU9gUquSXYgwMvG5NyOru39uLmMelyZtCC0rRVN9TmyUgB9L_V-Ic8kzaH3Prk_RhfvivAcUofydn3WKp02J70AtksxpnOCD7u2xuzQxtYjupNTzi3-IatdnXK73u8IXqHcVIEOyq_f6uzcsDvOMNcs95Qm3LqFGiaPf1vVkNY4ikruE83iU2vr34afgqBOmKcNKXR_9R36fJqjczuA-Biek4D8DCDhLl6_0oX34DjHIJdve1AGEaxp2kfi3IULQLGV0xXF5IljVR-lbE27MYXPDANSW6df_qU878ren26pqQEDJL-Pt1Bz3uKJSaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC8_5IvZnZy2gKnzHMHlJxxJQE-p-FCFn_umhyBCF1Duv-9DR3iHr50bSiIJ2ZZWVeyp3acImqc22Z4_oEwwd1y6a-mB_YhxWLrRrGfzzrqsHA7HIW9TsUtEb8B6o_x5bnyLa-jgkhHlCD4U7ItdiK7dqQQB_k8tLSxZgwn7uVu-76tm37vb4JsTWnwr9_0GZJuNEMTbdajI6nALAV-sWj5HpwnLS-EkFe4IT4_xti7Sxl2yKrAUzIUKDXGJSOEVopD5L3WE0WTDaLzPqb1y1I7JsmpGULbWWLPpipawm8SISwrQElDSSvv2ez95lENOPAgrjAFj0PJMX05siGRf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXqMCjW3RxdOCkBeOONfD-R2XbnrotxAs3RyPrh0vTCAOu9VDu6kubxXnjUAf9ldBRFh71Xi9AzFNVnIp-jQJb-kdl3wxBX5FbtVLf7HbwmJORgebgWdMqt5SyfJb4uuTybrWKYtpq7XNEWew-3X9mOmFfvACKTtuh1KcPQhIddF8OCkdBxFCaPJkW3ZuaykSioUAkLIpkNWtn8jlpovVSg-Rvwe3v0fm_bZ7g3t8HKgeJkG4RQjqA8LhFQWC8kHAs3IAzJm8WoNnG9TEgzwvtdWS-ugVo5mtP17tWtZbm3uMfNQekP28R79Ly0JajjQmE54qEoPFsH-5T9b6fYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ci0NLZawVYVOjNlM87pdcF_qAAFkZA7Ycxmh6EMX2JHpokcHK-QTBy2niG6wfqLBMbS9G1Sy7XdajIcc7D5pBomOOJ9QGQhTLCogEbVBcDt82lFn1a31f4IRjmJl3_FCa5i77NqaeFa3old6hd5S6OYSe9IWjYp-PirZFdk98SIUtKIQ1jVY6tr2g1IrB4JVXpxliZQYiGAq_l-39JE6tmUP32U0KCi4JudmDPyyXIDBW7gmqW7nyZ5DcfCwk3KldDcEYiP86IBNJqcXE6Tk0vtc6yMRJUeVIirz3r6KhfUgpNFif455alnMwYO8WdKVbKtUWQTL07YfgKnxqq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkiSbltfcAvEH3apk_FMvpBzw0bHDCwr1KSITX7KQdUXhwrTytbKlYpf1f2AbTBscrLRoj44xC-WXjxLDRufqCwJGvU6R-hdEUJvjuHQH5rTuTVIwf-KsRO-LLkKwqwT6FhrxGfMK77dv2j3vS_kX-BF-mzgbU1o5DcFcwAE7BFP8Lggs9WcZW0RC-wg4rKvYbsQ7NPpZDTnYMUU6AoerJWhR2NQubqGkOdFAxPEdhzvzTX7qco5R3-nSc0zSB9pLtPj06s9e0g8VjOQ0J1ObCGS8oGbaUWqEkwve_X1J65e1OjRIG_XEV3iEqwc_6_eyTaU_IbfOhbco7m-srIjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmzo2OnRnFyFOZVzF8KdnAOvh4mFO2Ob75twI06QMkb8X5ZnxRv87--37H5QTChjgpcUHqrl_lqbiJg_-2PmHq0z-UjdkWeSz24Oqg-pKeQg1HSlZUu8Pxy6qNhCMvTpI4VseHyVa6fn1u5ui9Qi3ZRPCQoSWGlZKHJQJP6ugjFipmk2LtHbhZ5xq-Bwi85tB9wMTR0lkjTKgs0ksi4TkbKMVR12FyiCun1GpdkbwwohA6_ldE6c99OaMqhiIYtOUw8mghZfToWvECWtttxEOgBAGzCQDKZc2o1IpxtQX-CboN7IagwbTm2M0lzllnRY2M3rL42Viahv-2-Q8J0XmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIyUVyg-9WpFAKlVXEQ7wpXpP_qEmmL8v8JfKLErJ-2O-Glsw_xj83Y0hZunhuAUrmOZlsi-SJ-KOOXBW2EjTTnoPyKvyatCbM-KfN0QX4VI9y-0VMGZiUbsi8AZ_CkbJhalGipHcVsrBmoMumK17kS6DjhEjXfd7dEMwU1X10cFw3Mfcb8bcKcTFOjzCxFJWpTZOTPS6UXUdqbzzyTLyY0TzbUERQ40ntxbDa5sesp3hqOV8UZTdHHmKBre5wgGMDZAnIW1pT3EbaJXhBWIyRoZwTv1QiR4hw_RuJS5J0BvF_YCZzPd4GVAwJAIkS0LUjYK_FqZxnXCSOzzx9Mn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0V1RUBq9SZuxxi5gpnal76mtSXcJrT56KjzRfA3FiTyi29UmKCSlYhcJ_6DeWXggjzh9-yfcre6s3m3pxhccx69k5F9MEZ34oAsCu2sqi0QFvCbQmbzHAxmQ-M_zbeBn_aeqrXGFiXHEBz55R3burjyJWNXj0a8cr9boJm8qC7-k9Z7QWLfTpy84YbkTAuAPJgCvPnwGyMdQx5a_mjpqpDwoUcKv6y6twjbmDNFP4A9iHZ9JZauSCxfurkc5NuRWBVCKPi6L7xSGuiOCgqAYJsS9qPOWQzhM7gom48baX2iQV5eZjELamxDxngrcOPD64qxxKuw5_5OzW4Dhtwltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgYKdOq5TWZRP7Fe2tBsG-Jn9pC2qy3Bc7sqhd-9kfTPYDhQiiOtP5MicqnTuzlOgowcDZyxqP2gSX0_1NoqlRp3m2-whCpODYA_Lsv7-MIYeKLQBcVshNBPZTDJRM2iUu0HwS9A19WxIwyDMlXgRJjYKJxwfuAh7lWhxdd0TJVwcZiMHPEFHsD6M7HVO3IqC_YBCSKCGH3uBwzDNVqgpuMQcKmJ1FSAMlout3JcMB56-H79dTNxiKE1KEarY5fxiM90AbBvQe2bnMNTFZV9BBOusFyQFhafMI8h27mm2nYLlxAQ3NRTycFNWz6Zxq4JZj07NQ0qrkJHN8u9S8huIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDAVydu5Dj_aE0r_DzYNo3H4NvtTh3Y-whlGYgPQa1T6c3RQymXwZUU3qcVXLQfjQLZL4l8FJFZjYu2rjsUKvI6UsdPwY40cMsA7w1iNoGEyFXO8ReUBPPRgbgwy8nF4-r9jR8C4FQ1rYKcxoGVXCbR4g9dJRZPEB7WVlS7rBOplSgZyzGHH5zRaiRlmRXutYxHayB3Gf2Gpj8v-LBhCEYfh-7BQzZRN1uAYOdKagv1SzqLTxpuwbzQqLhP5BA9JHH3U6vB_cIVNKF_7T1L1VyK1ria1OkitsEIzIiitNKBw3YXOZZUSN-Uqk2Z4KA1LYPC9KJ1cab1cCSvwBnTDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm5BgLc7QBAC8qMGPoH7TGnqlFqVuu9jVRauT3yMa2vmcB0KJvQTRAgQrDIgXuTyBKXlFpQfsFMc-ABJIS0Oq6noxO9UP3fcrwvf7SncCf39y0_d6j_brgFHB_CU772Rl3QNa_lRkf-E9PPilGlAVGDMlbFgwi7f6Pgy0mk4fR5fvRxe2MDwqKiMKLlG5eHmo7eklpL-mR0sOH9heAoiHy4nTm2-AQfnEu3sUeCpyloaNwhJzKnkiw5J8x-s3qtjUZvRGBUhxfEfFnkqyesGdzwqoKY7Dtpijr9Bren6vSkjprUll2gkN47nH3lqwHJWwQzu3cJK-JpCr_eHHHFY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boarFH4_-3djHeqXIr6YJ6YMZHW7tETmbvEm1lZxfmdueuIPK5nm9FlIQJEMaifXlIg_RD_C1EaYZposDNu4PCziGQ4JF8aOJkJz0KordBILqNj92cBuiA6OzEC5ykB8QX9TtSnztSZn9038fS9TgI5XkVz-e1CITRj2VB4QIzxqMhjBsjwPAePSvA9PuiddHCrB0nu0T6jN0VmbeZby_mj_93b8JyY_53ExmXVD5hsH4dIW9K3sPePH8Y_ioAfeqNC2lvFxvc0-enLLuKo9IvYOVkkO1XBOodHpSoP2sBpZCw4YBbhck2WwAOXU1jpOg1ZaY1mThXHjab3brYP_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WABpR-YQxghTfNfsmHWvZoMfoYTnDZGnQELVStHoNkK5rIcqqqXtTnk4-QlXpkGF8xS5OJA6caGKX5OMKgtsuae55VwbVVwPJmllDuRPS9DTtEBkEO5M8Olg2FAGou87vMybuI8vGWBw8PJlBe1vbSE1Nuz0nLZD5dP09_35pTMlHuQ48HMynghxWG2hrYyAOJQSLN1ZyCO6KikGDEDD5MHfcdNq5VToWBDYF6PPGcBTvm0UPNyshCm0bEHJKH61CGpxmndTVGltl7vsn-98wiVmXAFKE6-6EUQCmEFGbY05ryb0p56r0woVWnh8sDTRCQ3OXE8986yQjXyb2x7D3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNYlH4ROWrZj2pzZbnEL2rqAvxV_EsCWt_LU41wxuMU-h8NaXW2CVWF0m-qbGVSpBCKa2VMc6IxNp6-18tYdgO1rDBP7wHb7OxIm9rDPsLAHYP8JF2bOJz3DzwGutHyZP5r7tqxrsxa9PEdcePuiJKd6bDzOXjiqCeCeyPkNWwA-mG0WEPMBcvwvBDXdaL_jvqgX1aZUMu7Dv4i04G4PJYpr67-spVGkjXMadNVNYdvvxB9orct1AFsIBSO4l_MXIfS-qdCxtu4I2URTDJgS5h0MItOow-TN1FE7b3uuTtmznJbZJiFMmvakXtUH-_lTpPIdiPfMZPODIyF_HxUXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUonPHtWPf1ODl6wpLiBK9PbCZCm1KY44y58Tsuraj6rxMDrXoITItnaaH3lcTh9Bb20U4spijMG6nqhoQpB_6xrTLLCHs6A8d5GHj3rHS25Y5WKFBkWNbVU8TXRD9uL6KSAU0xXqdwQ6wUdqdk3YaAEGFzq85L8Fd-XHSuMctr9qSy7hkC-VuV6LVNIwgH6NPITKBRqXaFQzV9J7MMJ3Uwg6tkLO_WB7M_WmWxmYHiI27Su9xCoyuNRqmIBZLA705tP369MCx7RfoBE3X1JBGYt7qZHBEk2q2C_vb_Uv5uol3-hmQlbFeyue2xoZIxxeDdS-Ar9d5lY5Zy1eIj-2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEpI562Flbaa-mFzWLkZXz4Te9ARse4VNFVLsohURaUQHy0v1P3afa-PE0RVMLgfPAtTjw6bw8ZJTAhoD9qfNXMim4Wtom27ItdKsC-dJs_CdzY37-v7awnu7EFaSbp_3VXCBLiP-9Jo-70gxJdzJKQSgpDq3YBPDp-rZosFLAmhs8MtFHdYbutekopIZV9OuN1GJqRWbwlG2W_k9bSNvEnf9wsP82Oq-14BfYrj-zj89eIbUPEK4-zhnlJm59xwsOOof0Ko_qQM8bXe9AoG3X3bgpGs-kwY1-qVCgheKDj00WUVUDupJfVjcWsN8xM5tQ9YUxIrXcS30KJpHmm5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa3zoDrePaR4SCIIzm5bGrPhhPcj8lNym_9wsMwg8OLCt_MEiBQb0aPYI8esUyPV-iIJDFQFcLzbW26wZE_Bcac2UnC1h8NuF4JmwFJZOicq8OnTsSTFSrG6bkw2J47WmPOI06t84Vk1EIJKhNsF5bXVJadZjehTKEvbBsFTPSPy6n2WiTq1I9HqnQpkZ-_2EIcetuO5wqQvJl9rO2vv_Kkgt1cJEDH6I4NHuwDgR2oMchfzdsR2YwEDFl4-lw92kbDEqy4Rn8MgMC0Q_qOlEXLipkaxUhxIjsQQ8wIu-Vs9cV6Lilnt6CVmXIczbVktKjQl-l2BMb1f6qjVycY7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_1Cog8Udyf0pBVb3iVkGxo6WkMu_GOquMUMhnH1a38y6kqhcCpmKFmwJTvATBGptYjahGU2xuDD8CgXekVFhHUpcn3Nue_umWaUpvD2jODfM_0hVcllsHQXv6ZnlGc2FM8UPzygdo4ET05D-d0w5qBrRiz96YjKOVdZLEEWokaRoEx-Oe4avi23ZPp0pN1WpsnumvIlPqHcWcT4CBzzxHBM0qUEZLQUp4XccCFKG6j2WHyTm2Sc0XxOY8TmvRtXz_41z5q7h0Q7Kkgii37FkeX6GuoNu4D9fiQnV2deMAzuBi2MSjipU4Dt5cSxvZtD0m2VCNoM64MRQO2eZdnQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWjwICenQ7VsnRAdIIX4rfVHrRPvzwLrFJFgW9bXhFCGckTLMae3qd59U_dRHPYBaSPNVZmoXQ_RiveJUXu_4W0jYKtVDhFEivenk0arnyJbpAeOJsWNltgdHqjBY68zq0Zw3D8gfw_XmtX0eRURMrX8VJ27KqByU7_r32qsB-WTkxcx80FdasC5hbNJLOqEmI_i0hV1jyVI2PO-qJI73bp3vxq6aFdLaV6ki9DLnK8lU2YF88TahKelTKOo1UQVFwuFTSxJRTNvNC76OWgzmLY8qSwVHJ_udctg-co8fMkvpdXg7VfEoEdliOr2UD3Knr092Ycc5qOxMQHQecjn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7cHXHTjNGKC-rFZ2LtfoxESYPaXZPiLpdCNUMc3V3yotC8HfH0aegXuGMZqatVAiS5Tq-i-0_rV9UfJxVKdzXwJyg2LSZ6YuqBt0bF8bxpzt24P4ueiCs658AYSzK4XLEZ90yFI6rINilE8a2D2nQQePMaJdgmCFryliJRG8OHQrjAkrIbpeYRHF-De4_MXj-gircgmYKRW5s4r5hyMriCQ4Q23ETrtQxAxZljTFj-UsuQjjGfbAJAmXqtWhIEjxLRrMji-PIvPy8-uqvHgGRojndBnZi28pU26roATSHdVzSQ1y938nknTdX4Sa99usBaXnnjJgtQUc5CUxMjpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=jFq5pK34W6KmTGPc97SGFVykquLUzyXS-6Pr-tCpDb6fyEQz5262zdh2DLhtB-pfYpFzuIKRfZGAN2c8B_T1VTVw7AUxISywUk6rUI-Et_HWdFChFPKGpUdjpISeZXsxmwe6HS5noPgBPh1IDjQDF_KnzlGoKYstP9CJENtgmatpHR-489nZ7yu7_zCDeAUADJIwD9I2rNmaW0bfZKUd5uTe0TGli3BZhYWH9SRiICHTurmXZipoJYE5QRoEoC0WCTUo1mKdC4GYPlNbRxoUVYVQybVRkgQOL1sYsL4GxpZ8e0i3XsUOlbchdAE2oj137b7_Iz6nn068Xi9dAof6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=jFq5pK34W6KmTGPc97SGFVykquLUzyXS-6Pr-tCpDb6fyEQz5262zdh2DLhtB-pfYpFzuIKRfZGAN2c8B_T1VTVw7AUxISywUk6rUI-Et_HWdFChFPKGpUdjpISeZXsxmwe6HS5noPgBPh1IDjQDF_KnzlGoKYstP9CJENtgmatpHR-489nZ7yu7_zCDeAUADJIwD9I2rNmaW0bfZKUd5uTe0TGli3BZhYWH9SRiICHTurmXZipoJYE5QRoEoC0WCTUo1mKdC4GYPlNbRxoUVYVQybVRkgQOL1sYsL4GxpZ8e0i3XsUOlbchdAE2oj137b7_Iz6nn068Xi9dAof6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfzaIX3304yZAsJ2tNfkG-_5vkrvZ8psfq8hMcu-KH_9SuH_a7JIOWKnYrNDOJbjpMZTHhIKuEjyQ6jj0dR562NZEKQImC4YAm0X08fq-TogP18ix0BpCiD9Et0sg3uCGFL2sl7UQ7AeM7c6VDdPwtpz2_gCf12Ct2J4sC8oNnzFxsDRpyQg4JbKy4H20pU0_MRKvlZP9rQkzu-iKI_KXi5QFOx_KGbK3n_-hHI873m2jrw8zPC06geHaaN558I3uZviJs9U5rnqAPG-9s9Q6wPGpJlMMJaMdyxVDyeX2iBwLo-P3i-OzWRqcUh-YJszrQeJ4jDnH7dB1jxtT33-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=O5OiIi9R3pv7lYLmtlESHiHr4fF0lyCbbCp4rZWqmMTbgrvyiOBBcoYG42haIoE5RriOpwkDUsQB0Ty1Wq76xX6c5Z8t3vvmuTBHMAxFyW8gSbYHHEdwqeXfEBllXUBdZ_lDkLZPXgHxyWXlsmNjlp4MyP3_WWyET9uC-CrLT9O4iu-RxA-wOPxJruIlvHPXYI2hQ1gKzW2YcJumLeqHnonRO1CeSWAHQi8-wTY0SVahUcvRB-zqcM9w5RR8FrnFsIxQqijHZGOyn03_FoA2Tf5wa_MwnrxSxzQFlz8DoKG9ycjW-Vncr_1cMpBGNjeKwOaTK79Crirj6Ofx0OmIng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=O5OiIi9R3pv7lYLmtlESHiHr4fF0lyCbbCp4rZWqmMTbgrvyiOBBcoYG42haIoE5RriOpwkDUsQB0Ty1Wq76xX6c5Z8t3vvmuTBHMAxFyW8gSbYHHEdwqeXfEBllXUBdZ_lDkLZPXgHxyWXlsmNjlp4MyP3_WWyET9uC-CrLT9O4iu-RxA-wOPxJruIlvHPXYI2hQ1gKzW2YcJumLeqHnonRO1CeSWAHQi8-wTY0SVahUcvRB-zqcM9w5RR8FrnFsIxQqijHZGOyn03_FoA2Tf5wa_MwnrxSxzQFlz8DoKG9ycjW-Vncr_1cMpBGNjeKwOaTK79Crirj6Ofx0OmIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=MPlgXjLWCvwWbuwBHAZYOMtJaZ_RvhPhE7gWrrwcHe6RC2Hu7mGY0MXaVPGX3LqnzKMdnwFjN49i2EBboiamaOI5YuvJg11b3ffAo75Cc-wAeSW_vjJsPwdU2hEDM-gKyF-L9hZeIPcQj6jFalu8_rxmHWYvGgV-9lePpCto5iiwV-31O9QlKBkmCikRsKPdE6OZn8zCipRe_mZfsc0auiMi8Ruq1zS3-bOqy1vOu83AEmeT0XjcNF2qoOzTT1OlpF88ox_ycpthe4W2uswoTwZ5YvGbNqVanBNeXtjMX9DlbbaJytPzih91_AzK5gyl9aJRJaTeNcKpHRanN30mTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=MPlgXjLWCvwWbuwBHAZYOMtJaZ_RvhPhE7gWrrwcHe6RC2Hu7mGY0MXaVPGX3LqnzKMdnwFjN49i2EBboiamaOI5YuvJg11b3ffAo75Cc-wAeSW_vjJsPwdU2hEDM-gKyF-L9hZeIPcQj6jFalu8_rxmHWYvGgV-9lePpCto5iiwV-31O9QlKBkmCikRsKPdE6OZn8zCipRe_mZfsc0auiMi8Ruq1zS3-bOqy1vOu83AEmeT0XjcNF2qoOzTT1OlpF88ox_ycpthe4W2uswoTwZ5YvGbNqVanBNeXtjMX9DlbbaJytPzih91_AzK5gyl9aJRJaTeNcKpHRanN30mTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iscK7Gz86AXR7Ok8OVs-VZLI-k1XgmGHFBOqA2m2N7BxMAmj2jQPomNpwuykDULPyKy0CugVn3vWBY_LLUnU_gzXy9Hlzz_IwaK1M29KEK9Q7QS2tLVFVMvTtns90OYVhwCiDAYtgBz5S4DhVBH6nur_s53R5ZPJuQPlN9JDH1hXTAYV5ceU-CF50ZLJ87zDTtHXDgTk0HGKDyRdxn9Tl9r35wz_nGEQQsH7A6At7FVcwjLmceB_tzQu7CxFzlqTbe5wCbw6oyvQMjC-LL74CqIUfWf-kg8wI35OrKNFS5PaTAg_IfIizI8-Qw1W8MCdtcBBw_KqDK0u40U9sLxaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muMwrR26wKIWTI6vE82kKLqZ2iZmCC8buf2zSTBo-YNrVuy8WqsBFmY6O4DQaza5u_juf-qo0Gn3DaiCmjxZRD3FoFWC_UHlpyPYaSPIvDqLIIbEpHPzhuk0hb4fXPKCb7ty6FuCmHKOkGPX9IvbMBfZp1lYxVirmciCfuedN7-5Tx1tUEndiZF3adbnPMyWSJFZydv43d9hy6818-4ZOoZNP4BIW6Xfwa3L3c_7FPird1j4_7rzKnh_anZz2LnlWvoq9H-RI5dgbuYKDIlL-KIlYUGMQCKOv6teLSvpie2RW9wExgS2YRsmvUBk0nQ33erKjH8fdxs--SXvHzuC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txVS_P3SZ9_ArNiEUWEEaNS6sCiS9Jaw3o3NB0r4ynbDRn1uVhqLwCeL8Cg6XKqlLaZgO48BUg4GawB8q-c3keoytQ3POBfx5ZPeWCnB2jussxxdyMdZPocG3DN6ucRI6JHTipYGipUhq1rNKHeFzykcrLCZmgay5j54ro3w2kR6CYJb39GA34hRFqTIFNPRv8FzoID1xUhFMaDkYRYWt7yJxTuzZhwniWHuS6Y0cuQU2CPRlbXYnRzU_xz48AWviX5VpLgC1bvTP1ck4NUXjZkBl2TWKpSXpGu1hecGLlCQ-9qpa75EOI5ZdFDMgRclAu1QuYx2VAUg5NQ7-1tzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z42G0Cguk5YFYnKGWtCLVLNiltdVqmvldDGDGcdQeo8Vl-qa_yItU-GwaY-X7YtxDFmtm8zTNu-PrmqjFfxAw9AywAtbfq4XhOmtmPS4BefsdTfmjZNqo3qTdvHxN_9u4YpvuLN9pczkePzPz30JUAq5mONMY8aYTFIomXN3_NfJglxxhQt_RscHKomQw8zZBm0Lw-fV0t69RgyoD_BoSRuRh7-ouGNjvpjWsDweklu_y9TiORdc6BpDXAPxGrx_LFclPuvBFs4vJTVsP_adIjO7XhCZacNbzZxNEXdmtUzpUkdOlObvXYbHFVF9JMDa6hUPxiSYtnKN-4uam-q3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP15VR2z1T4CdBP7mCUuDlQe9rZ2JAcpuSTH9XSGzCa5eSBgMyIsZAuK1m7UEuXDBWL5eG1GzP62ouBcccSqrZjx8eJ-8fodamPJdObW-nHZ_cw9qga7gCSKtIkGE31546d0S0IxqweSWSono0sbqG-syCDiRsp0FuKHPLZjclmovHsVChzeeG2fuBCk4kfcuOSpLRUvMvbgSqoUnwRPyG9Aum57Ho6ALy9DSJnZkwG50qmPDdraPG2VVW_wBBlVG36wDGwYwzsVGSuhVe5s7ZqgETCMDlduDu-UY9D9Utp6SF0Ubk1XroNaSnhhOOX5ZjNjPR2wKzLgUj0bVk7aJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=j8Yy1h8h1EptfCPDwgn-63a55EFLdey3tlnj1bxqD-7vb1rIvwG2pdPXZDOt6fQcC8X8iHttBtu3I3YCvdJ74-j3BjirglxzYL49ncAWgnCUcpuJGGTepEZrnBhyqKyfyVGnRMrXF451XWTW2lQRC_pII9i0kZeC-FszKooXdxXheLN9rW_EdwoqJyEnBgkfoB9Y8320YYtezCQBZQHHtpLybfd122n7e0sWBp5nOK0uM7E8rqUfeBvJfMUEFBlQMzeYCtusKuMmlUKgCMQqNuF0A8OS5CECoSJAmwLIAw1KdaJvdnbvyL4S-g3lLMXgjjRjB_YZbY6Q0HBExYWMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=j8Yy1h8h1EptfCPDwgn-63a55EFLdey3tlnj1bxqD-7vb1rIvwG2pdPXZDOt6fQcC8X8iHttBtu3I3YCvdJ74-j3BjirglxzYL49ncAWgnCUcpuJGGTepEZrnBhyqKyfyVGnRMrXF451XWTW2lQRC_pII9i0kZeC-FszKooXdxXheLN9rW_EdwoqJyEnBgkfoB9Y8320YYtezCQBZQHHtpLybfd122n7e0sWBp5nOK0uM7E8rqUfeBvJfMUEFBlQMzeYCtusKuMmlUKgCMQqNuF0A8OS5CECoSJAmwLIAw1KdaJvdnbvyL4S-g3lLMXgjjRjB_YZbY6Q0HBExYWMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=OFu1rAAJOY91fW1RUSZ55ST5PE6BXx-723eRoGkJXMKCJtWNaNFIdPxF0aoTAqfRVL5jFbhT2WDt3Oy_bio4_oYwqlWsa0A4EJNFt58S8Edc5WEOpVH3SpuYRRC_SIlJw6AyLCoMyE4X_-jbA6WV2v1rUBfYyNZq3WZ2wPhcKP5theP8OMjifTt3aGAf4DVx4Q0cRSR4Iqqu4jTDlW4gNbbNHyjV606K8V9F1J8cGurrp7MsA1Ez-PBK18YV3be5vq3urpPVJDPPpVIejRgXUfekprtbNi3nDQMucG-K7Pgjm826ELMp-ULgMA5im73A5liEJv2L8q31pUi1BDIjsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=OFu1rAAJOY91fW1RUSZ55ST5PE6BXx-723eRoGkJXMKCJtWNaNFIdPxF0aoTAqfRVL5jFbhT2WDt3Oy_bio4_oYwqlWsa0A4EJNFt58S8Edc5WEOpVH3SpuYRRC_SIlJw6AyLCoMyE4X_-jbA6WV2v1rUBfYyNZq3WZ2wPhcKP5theP8OMjifTt3aGAf4DVx4Q0cRSR4Iqqu4jTDlW4gNbbNHyjV606K8V9F1J8cGurrp7MsA1Ez-PBK18YV3be5vq3urpPVJDPPpVIejRgXUfekprtbNi3nDQMucG-K7Pgjm826ELMp-ULgMA5im73A5liEJv2L8q31pUi1BDIjsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwkUyBJLI-uBTclmk5J9FmqGpFZzTm3S6wVUBEtLurw32eHXusSh0NCWHLUeOhgfdY7TmJIRf7lc7o0bwyaqevo8aqLtx48DbA8wvkhaGGFl41kaIrI44EKiPNZE0bK2j3nCV_rR1I7cu_eAoYnpqkt_VevSOQ-Sm82SFrMmpiUoFVisCh7mox5bg6KeDI__hL9Wx-Qm9rd4G5zl6cZmez2q7pX7VphBebyUdZpGzMhW1x5NpQ5f3VIE7t3trSfxSgS3HKLAL9JcPjjcwzgCHPijo1CPgnMLv-z-9rHsHSl5fD2Ke24-msAI0LhTbSeANHSYV3tzoSyu3t5oz_0TyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggwx-Z7gU4DA2uFz75xIk8xBO03dl69Dz0qjZCLo_RxB7x3vzoe9wJoUF3vZI3MO0bMiD6seKv3DMca54yNTK6fq7z-gdmeYIKY97P69UmG3iqYc8NuOz45LiBwUpLxxJGnfRVoJT6ptwVNb-KsrUpiNGD1Q5A1YdsrziabeL7wfOiYj1I35vZFyYFdBn9fAufWsKnNQwuipH6mq71zXFq5UulO8HhIT-oPqg6IdlldukKVL5v_HA8PN0wpZRtboqTYmgYAR692tTULXVX_kgRElSExJUyq-ftJU5RogCTOaQcYbj6USC4KeTEtrIq-mp6A-Kd0kpPS9dcTtVfs6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTEqYXZO4WcklbV_crirn6FM5N2vF6l0SPCBxlsj9p9Uu7AE8kacsoDHQ_2xXb8WLKP_O4H2G45xL7SoB_1Q0Lffw8vy6Fvrc3Bk_l2xhIweCx1I9XoxVdsKdXIdECFcNJaoi3lh6UxISkLwaP6zQOMVh9N2OwKYE-xmpai8ka8yVKeoJOjggswfsT5pORLLAUWX5dMMYpozRbx7OiWvbhhB21yD1pg0NpfyhW76GhsqsJxB-KZYk5OLC1btCuhlscYS022DRwBROY9F2aa3o-lzF8hYP4vtj1BU4j8KtLcYF7mluj6NzNq-aOYJSNA57HU_Q4IncmNwWwnxdBXIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=iuDsPSuoAFOoey1IU46nRXkOk5Kchemn7pTuACSVcYtdQuVsxON6lLBkN8_N5JU9-vFR9MJR03hlESprSEI5smzROiJBDuZDVPP1g7bFMneRAZCtGPz6ur1yV08ZfpHenx_sB_QmlgnGq1JgURPSqF3lNIzjbMgDmWiOKa8RX__VAqo_YNYUCChSPIA5PIfv-prDWzP6axW7kpBv6zE2IrId5YnbtxzMjZ3j_m_UDOc34CMP0HkoeDIkEboaQmCSC-wuhzQRG2Fz2eAogkmAS70jnZWzogpP7S3L2d4gKNuSXYmgfHjCD5ytzRcYzOlyXphNULNKJXgdS5mJPklkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=iuDsPSuoAFOoey1IU46nRXkOk5Kchemn7pTuACSVcYtdQuVsxON6lLBkN8_N5JU9-vFR9MJR03hlESprSEI5smzROiJBDuZDVPP1g7bFMneRAZCtGPz6ur1yV08ZfpHenx_sB_QmlgnGq1JgURPSqF3lNIzjbMgDmWiOKa8RX__VAqo_YNYUCChSPIA5PIfv-prDWzP6axW7kpBv6zE2IrId5YnbtxzMjZ3j_m_UDOc34CMP0HkoeDIkEboaQmCSC-wuhzQRG2Fz2eAogkmAS70jnZWzogpP7S3L2d4gKNuSXYmgfHjCD5ytzRcYzOlyXphNULNKJXgdS5mJPklkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikM6TuRMF57gQ7uRoqfsjDnpVgIAmBUqAANO9av4MmR1YJBirKASMGBeml5pMbHl8GbMqUhxsN4XfBx-PJ3nY6VzrJpchhweSptDU8Y3mI7lPKLG8Bj14buPt9o_XGlH1nDDsH_-e0E7nPEcmsqetZRCYcU_AhqxdfGb_MtdHC1_mQw9VJAe_evZvgRSXmEfdfjamX3fKNJVYeIDVvu-XfbrPALsMn7l8y7STDoWLUZrVfUvFHVamNWQLv340_IrmYI6hwWizccHC-a8WhFtUy02D_DW160fxY1yF2DiecZs6CZKJx8mEtmtvI9Yx1NvrLt0OkZhDIV0gpD9bKxSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlLVzBSI9XUHwUCsjcclPVtWS1hZrMd760Zwh743apv80XeOzNtKTzTQE2cy8X6q98VjNg42MSi_kyd3NXPokPZus-S-CireinjszsE48y0_0XZbbxEaLGPnA3hYY59b1pjKd51GCNcU1NTpF1QfXfpbK8p1nzilNY3yYspPP5M3Uh5yU0C1_IvthP_cVcFt7FqvWILClRUY-1E5LfxBsuyT9jKtv36Tva5c2KE2_wdMcj2ZqP537g51WAd9GVx0-RAFcI-ARFgKHAxgwHU0LWLenTAo0sVNr28Q4VawiooAQ8GsgXLaKhimPte6e9poatgXJ1ICi_RI6Zg9hTf9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ7crvx3dW1a1-k5scUez5MvJemLljQMsxcf6JJuv40uzkUzUNNosyxbt_PtKEwvwYZJN1kSP3FC62yitX-M1QqOolUR6d8jmnP6z55gZfTp12BaD3Sj_wIQPlGEyXeExrQ-vtcXYze_dm-pRr5JMm1CXTT0gm8udLSiAK9pEMSo8lXuiqRR3sUvaaoe6cLs9XKKeVD_0Qa7fMHGwsdhGR8e_dIvmovTuNg58j_sUAVqWAIP-cG8oNABiI5_ct4qIZYTWMzeTswCww4nB0tAtbQ_56Afb_a1ucBvJqD7Lr85pqV1vWGK_I5_v0QfYwpW2vkqaaO4Y0NmrHnfufF4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsusydR_v8svFOXfTzKLmIXxut9Jl9Vyd5mrhZFYXRkWQeffQ730OefawRu6OXRANewmYHFGEvX9tbCY4lQao_vvdF3YzdFl5YjdevfPGQts7siLJWGHB3lI55ILOsk9g2RGvnbp_5N1_0h6LiYlAxKFa7EPnzNajeq3dHsVTUzNogArvskXC1lK3cXHaYkzNLzeKTCzrpL6g1WKKLdxAHjvfqajqhDDEQxwO-1Y-VVvzI8iwHNW9HOWTeSB_RU8tWlpLDJk2n0xy65ISqgnI4lmEY_z5Aptm91ksW7yjda3kw8Ayn_Ul-2sQan8oNCAsB_gkG4JV1HcglKreFzyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu_NqQbm-rs84T_TQjQ2XLKj3ef6ryIbnZ15hW8rvvl2Bg5v64RQ4FRAFHGT6lKDAA7uGEI2THgZU0v4Cz4WyALoxyNtwtaFNLPuow3d4PMa2ZMKkVfTcvqHkz8cRw6nqR7HZeFAZCo2CACvOwWkI4vIcQu1McE21XIAsM90TEv7yNFtudwRwehrUaq1TNyuXvogB9k_44YF_RLW1bI-BL2ezy4PplzaNSU-oUzAZew5xi1iAoJjD58aMqb9OiDvKCeqUr7Z6OzC7nSIM09FfV53pYQrg7BOyzTXQ7aXU2gPe7XMEJhqE15eH1QxOw6VsOp3W227SKUzRY_hwA6IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV8AhARu2ITHH3OmHSLEJLSTTL_oo9sQXHNhngElALFetoa188AP6BHlH59o0V2UDOq2VyHCH7U6qz4e_YCkNqNG3Z09NBNd5jTCBWU-I_534KYc0HXNNRL7xMBv9RyS2RnM7jKcMFyxgACZcsRMmia53wpKMX5Yk5HHBBFYJey9r45d8kb6iKPoqU7N3Oqq7ysQ9a9IlgstZX2URv7O7Z6JnkKl-cu8nJbEm1iYDSScPHc_KTvnjYa_tQJtEf0yWQov59egD6u53O74hX65VhS5xPJpHIDtY4r5JxKNegFD9byGthac_x4y8YuAPntCcm69BAfSMHEzJ5AlMtKWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHFFdW2h_4RAPelAatXEPGrhljyt2-EmggGicckL-PR_BYInQ2y38pHqvUCOqPrwvV_kLKegyEuTLAw2SxB0SHYMQnkImy1lk3TlRkH_DW3CG_xYMSw6xgImy7-pT8kSNWq_2ql9872MJPbRUPiBtVm1HtCoPFP5Ydva0y7VoYSRFApB2RoBb9ql2SHjJkCf9wEucs6pFx-XJs_Hxpli13UiyFeK5nzAbLUTUVeom86eKoMWFy_vc1XrTS1Nidrl1hFAI3jsxEAIPVdKTaoDVDI-ghwOB4_niRXMG981-B1sz2gc0d3MqJmjh_RsmIQUF-DbcdZah6NV97VZbnx60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwtbeUQnZKCF93GioUFIrnsFeXa8O4S81I8i9mcWdzeK_8gL7HctOnR6oI3lt99T7IcdLG3pq01VgeawnffYqzfTL2KErsxT4xAH_d2kr2BE1Ef_cB0CXw9P7vMML_No2_H2pItkLytqhi_LuPjQRdulLVMR9ReIBKYUYntgMuMWF80kt46YYxUxY9p2sezbWYktiHg9SbPRKQbvFoFgpLwteZm-8VJBwLqwb4-UAo_XCKq5XLxn18gLzg513uAiwf9GKPHJhcBjuE0vZj7n19eEqtFJMwbWEKsKYziUcMaIMxkD0l_jSfRIjBjHhID6LU-5G-26wZxsHpEeeqn-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=v5K-AeryZC-cikTpPGi6PrrqRRiU80O7rr9l5vFoCWEnjJib9E6gqe0MaQ-Tbqw4scvAep-DPWxm8j6IpiMzeHqF0vBlzJnuNpjbJVpdbI9mTmeNwZpsUEZo6euR34Qvh-Gvfkr7dLHKU3jOPal8020qEPpv9ftWLFYY1NdairluGeKul_YxqYfFOEDYgjeV4oooMHk_cc_7zJQ4E_ERmi1TwlNbhnLpGbSXWvxrFrciowW5P1WEzu5HQQHKcR0jfIFrttaDaq07tXgNWou2TudVAkE6mdX-IdRJL1b-nIOAtF-DQLMOJNCgHszt2ibEK6-0FJD_DZgR7qJRhmMq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=v5K-AeryZC-cikTpPGi6PrrqRRiU80O7rr9l5vFoCWEnjJib9E6gqe0MaQ-Tbqw4scvAep-DPWxm8j6IpiMzeHqF0vBlzJnuNpjbJVpdbI9mTmeNwZpsUEZo6euR34Qvh-Gvfkr7dLHKU3jOPal8020qEPpv9ftWLFYY1NdairluGeKul_YxqYfFOEDYgjeV4oooMHk_cc_7zJQ4E_ERmi1TwlNbhnLpGbSXWvxrFrciowW5P1WEzu5HQQHKcR0jfIFrttaDaq07tXgNWou2TudVAkE6mdX-IdRJL1b-nIOAtF-DQLMOJNCgHszt2ibEK6-0FJD_DZgR7qJRhmMq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIQFtcvgmAF2UHyP7JDhcrttYIv1bIMrHMf13fYcjlZwlJJa0HucURn2LO-qRBi5rOCCK7pOCGp0GP_ccfY3t5GhUzxpn4rdFYHyi-YwUTbQJ4U5TDuUoay0CXtFXMj4XPZfWJ506tTxxvVNx4p4TJxViUoJOjQVgWTlhJQZT978zHwgxaJaEV_ReZpEbnOBH-5Y5FYLJxCapT1_HeDjBmqOswg2t-M0Fv2NjE7srIcR4IarwOXBTpfrioy6ckZssRC_EGzsLo2HN8_KKoSx6hUwv0J1jgxQAd8PvYsOgtAL4J8jpJmzs8Pz6kCovXC2lFaNudV4_3P_M4opgziaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-7630Vh4tq1W_FwlapNUlyHs3zE9sx8RjKQ8N_9VNHkkqsMMGQ6qq78TwNF9YFqpaunJx0Y783d2yDrZLNs0X8y5fMSWBspIeXRxQZ-CjTmgKEKIuLaRI6RuKA-Ujab6SIQTnjKL5WEvXZCGPSETr9TIlzoUgFmfKIGpT27RXBJpZmn2Ctdm_U_rcaYQ8bKijOlkroK5NsR8US9DmIHvZ13c9NObAb8JRuaU5bvFYzSBqASiAgxz651NVPB7tDLyhz6cLMMAra9-lWpwHzoghYQKv6mx9giIRgp_xKUn5bW3qtEDlcsN5JjUcIHHCZTxIZEunpEd7Gacczws8QiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=U7hfedBVL3iM9g5Ae5VOnn2s6qvuNEh4pCDvKv9Joo_SPqZhMOUGXaBxjaN3uYHgyhcYtfXYGiV8Rr-tlCft00NaXfc95wTZOaJ27bAL8T7u7XzII0SVuVJpqxhy1WL7FLJ0h4lflbJkoW_9K5zv0Sfg7fhjYOHWv3yS4Tl5ZhysGyCIvtzoFxTbFoRsKA-9Qem_3LHU6G5Si-hGNEsDX2rBDYK6VZe-v-M8u6ybJ-m_O9Crc2JKpH6Qjp0NZdT9qvfxOjuUw86wsRA_ikjMQs6s5x9zxD8-gqtNeFgXx_DEX3QPQftLDTY6PRrj6shm-0HJ-VDcaS1HlcD9iBnR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=U7hfedBVL3iM9g5Ae5VOnn2s6qvuNEh4pCDvKv9Joo_SPqZhMOUGXaBxjaN3uYHgyhcYtfXYGiV8Rr-tlCft00NaXfc95wTZOaJ27bAL8T7u7XzII0SVuVJpqxhy1WL7FLJ0h4lflbJkoW_9K5zv0Sfg7fhjYOHWv3yS4Tl5ZhysGyCIvtzoFxTbFoRsKA-9Qem_3LHU6G5Si-hGNEsDX2rBDYK6VZe-v-M8u6ybJ-m_O9Crc2JKpH6Qjp0NZdT9qvfxOjuUw86wsRA_ikjMQs6s5x9zxD8-gqtNeFgXx_DEX3QPQftLDTY6PRrj6shm-0HJ-VDcaS1HlcD9iBnR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=hu9qAPa_-MGm9_2oA5r9wjNZcrFoF1BbA8lPvXyZaeMz08i_5Map12SyOv6VgdDK5PpRTlT-5xJRuyPdn6DxiBJOYzCHwy2_MfY0lgt19QMCYsaYBIErRlG08c5U6Zs-pCmCOeHZeoercVue0qF_bjd0b-xeIKz3BheZ0w3dva07i3glhA-qUrHemMMBA43nCSzi7uI8zeZEEQAHXE-I184PGRYNgUdTNDrg_JqVHn1ZTsNmgVwlQLQIjVYOWswhAKr-ri7vaRY-oOoWi5itphrXPSInTzTmyQPv6njirawKr-yT-Q358FIc7jl7XoMUKqnlDro0br2Py7iQZ9971w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=hu9qAPa_-MGm9_2oA5r9wjNZcrFoF1BbA8lPvXyZaeMz08i_5Map12SyOv6VgdDK5PpRTlT-5xJRuyPdn6DxiBJOYzCHwy2_MfY0lgt19QMCYsaYBIErRlG08c5U6Zs-pCmCOeHZeoercVue0qF_bjd0b-xeIKz3BheZ0w3dva07i3glhA-qUrHemMMBA43nCSzi7uI8zeZEEQAHXE-I184PGRYNgUdTNDrg_JqVHn1ZTsNmgVwlQLQIjVYOWswhAKr-ri7vaRY-oOoWi5itphrXPSInTzTmyQPv6njirawKr-yT-Q358FIc7jl7XoMUKqnlDro0br2Py7iQZ9971w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=O0CdB2513z0_b0KT9Xj5Al1Q4vYoC9nmUaBx5-vp_YPHseoV26-UmmXF18RefnMJNW8BLNrnRz0xXvxLZI6rKmcMLgsD4mkQS3mopAzB6TARHeHcckNn8rHXPWzKtJMTRGfTScJyW8_FVSlX8ztNjtK0zR5erU-NW1MqnMn3x1aqJJ-5Aiag3DQLLG4nXsr_HQN1nhDAh1pg4KVh00GFjCGXKrbeQ_ccnetgSnEFsqc44hZVEYmalOarCZa9Vc0GFAFzi4bjpxUREF6wuf68fbKNnMYKiRPiXuFBqnS53S-fcSPvuGCwudRC7_iK-iocZRtp-WWfpSRjCHO1bRbrWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=O0CdB2513z0_b0KT9Xj5Al1Q4vYoC9nmUaBx5-vp_YPHseoV26-UmmXF18RefnMJNW8BLNrnRz0xXvxLZI6rKmcMLgsD4mkQS3mopAzB6TARHeHcckNn8rHXPWzKtJMTRGfTScJyW8_FVSlX8ztNjtK0zR5erU-NW1MqnMn3x1aqJJ-5Aiag3DQLLG4nXsr_HQN1nhDAh1pg4KVh00GFjCGXKrbeQ_ccnetgSnEFsqc44hZVEYmalOarCZa9Vc0GFAFzi4bjpxUREF6wuf68fbKNnMYKiRPiXuFBqnS53S-fcSPvuGCwudRC7_iK-iocZRtp-WWfpSRjCHO1bRbrWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMfDoS3rsEmuBcVC2w59szROU6M2pxef60pznV2FdRmhmx74UmJ6_CKX793SiZjGCVDkD-l99gnPd4PWTaGqw2pJvOVTCQncCIIhF4Y1os60_5DhP-RNt0JdjIt-VhN2L5bEh7swOZ6uRyLBx-UWy6vGDhbe2zgtuhXPFoQDUcGmgc3QLM79tbVPk7BQsfJFxTr3MqQHgdIzyBFclBoUiSYhB1iBW8Uil-7rPU3UWsq0sLcfj1YkCFHfGg7g1un2A7GT4DRTG04uHEqolq8xji0SpJek7RIGkVsYS-wKX6EuFPW5eGqHgDTrHA97S2uHRnAUqA42JiO-BBUeLclU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkvvs0dJDoFNY7j6pDBbS2rZtElqYJc3A3gqxk845A9v3yRCAbD4o8MDsFF400CvDHKWm6jvYWKHRzXKXVyr3XwOlc8fg9IAn9oBpXHRKX1C7jzqCkP6FbeQjRZVz5IGbJCZak6PyL_-2xA7wr7ueewrtlCm_C-6VatdxY190NBHH6so4CIIxqj-x0yOe3a4n2dmkFVdxaaSxoL5QHeGPeqrKu5s_41L9PUodJ6UEus0s5fsHHEAmBWUhgZ1_ASl72nt9554LLoj9J4CMxRYmtiy5nMDUta1MFBXy1nHJWDZ_z2yx5T2FzR3ygr5_bMefhwrIez7f0hkkk9BZjEOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nik1J4Mgk2lY-8g2-vuog8t6KldZvTMVqioIxACY6m4zfqtqq4kMFEuNZbTzGfwFhZ3R7j5h2VkYnBTVymFzl5y0B0uH8xoQKCNygz7slTyJNEw3TMkC03QADsYLkDjARyWxN1sDgNh9mkwe0cDLf3KXZi6Ct3fh4P5EYDt-YcREi9HAgrWo-W_qHya5icIo67bX9JwVJjqkIyMxEhLAwmlEI2LG746IwDHOHsnxjrlL2WOerHrnMbePSE81sAnuSJ20bckPkiF2skvFQcNvEhP1-jfmWgSgiV1LKypTjG40NTWuV8GsAvgMeNpm_WcDrok78njxaovZ03hysD-AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=eqBXjXgyymOhmA-ZueFqp5ulvAMABo_p3rTl4txDxbH2uiT5riQdJH-Uf5HF_bJCzT_rpyKB7d1AfaL1ijodZCthDPJrtuuDbZcWOc9bgcS-AKQpx9EJFROxAhPRK06fk2jTTwmdqVLHASCUx_8yxf4Vh8dhC1r1ajgHVXmRYSGYyM7NisE_TKYfj8qdit5bbcEItqBPMJCgw88AyZ-eimq6g432wlxVfV5KL273U_WYwwOVn5NpwFHQu9Dt3HxgSXLZAOVNhN2cXckFtK0g_RgPVvIXDxtS1Xy5-TM-e190aMeINsPLnkneszRlsKJu0AUB4cm-fZ5Mi7byQhbOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=eqBXjXgyymOhmA-ZueFqp5ulvAMABo_p3rTl4txDxbH2uiT5riQdJH-Uf5HF_bJCzT_rpyKB7d1AfaL1ijodZCthDPJrtuuDbZcWOc9bgcS-AKQpx9EJFROxAhPRK06fk2jTTwmdqVLHASCUx_8yxf4Vh8dhC1r1ajgHVXmRYSGYyM7NisE_TKYfj8qdit5bbcEItqBPMJCgw88AyZ-eimq6g432wlxVfV5KL273U_WYwwOVn5NpwFHQu9Dt3HxgSXLZAOVNhN2cXckFtK0g_RgPVvIXDxtS1Xy5-TM-e190aMeINsPLnkneszRlsKJu0AUB4cm-fZ5Mi7byQhbOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0fbPML-WvG02wH9DuVVXj7QGVZtnkJryth_gvljHKw8oNwwWcjuHhF5RLjdvOW5FpzfPMkG6Be3TNpQ5CREIWrhJYlXhJNgN6UfoFp-sz7NjLI0vm1m-3zt3xxpHAM9hllpoVqQ3RilBRCw-R_NM8Y9muKB7iyklJdfgLft8qtfd7WhUK4mO4RfSX-_tOIBkg_CT8TGHtdb30nQaPc0q4zkUN5SBxb3oWcE4qalgXONFAhtqTCE_dyL5JAgNjQG9BF0YoZ7709s61CLpdKsjo-F3LTOtU0IdJl1zXy2vf2SgRsT5B98KYmT9Yn52PxAhsPPotk_yyA7hwdojfLZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2L2eHTHV0o4rujphP0lrah7NakASqHTYzcHrA9-T1NNFzipwx5rjLjBML8QXl-ZQjtVJcO3NYCUq1_2UlpCnMkJkWGSgJUigwTsKfEuKr9eu0sNDp16DLJbPZU9pHYWbAI4WcSa4105hkRvXyhQS2ttQ76S58Kc3h66Qmiuryy7XKAn5u7Drunj5GbFTTSuzvZzugdKJBk4swv-xAtLzkf0_OY5YOG5zNmFfFQvSknIXvF6P0QihwHm_lYJ5RiGrKfB9UecNXR_JyPUxTQAE3JJSccbQVXRqhFHG5H6_atLjKeCF4rHObHnVo1BIG0S8H8wjpHprt8LRWB__nJPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mR_TPyoCQohdhZSxy_EZA4EcDW7R3jlZDNAORN3sbxNJmXeLY_zdGI8UKangWG9lwmDnqa37ve-b9RaOvNtVX3VUuwgJJZ4T6Ky58KpXpmGZQZzKZYfKw1tak7g4rO2dxgar2fWHIWIstd1FtOkMwZ5kN2Tt-N-jFJapjyuKvWCAXy7n08BcQhNALukbIWLw6aykDtTkJPnqI-aLN-hYVfnux1x_tZW-EWT3jGrm2yS4E2w6xoYIgETX-Qzwi0XWl_6D4BxKQR111168Cvjr1PRWKraIVM26BKn0DQ8ZtgCrJbCvdRwqz8v57pBq54ST2jJhZvZpH7BLsNR1I_kWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V8x5W9LEVMEfc_T4eyxvesw4UY_pmJgDYLqLVq_E6J2KZ3anHrpLOYoOmGo8ePtKDPwjI0KTvGpLNsENMG8-2GO_l1t4c_7b5aJXdvuSa1Z9TDjFixn7UN86EgmeKTOIDXKbmorG5uoaDHKIDE8kZVVagoC-RxjnX6LUy-cPi2eQiC5F_FEZKanvhleIM3v3YDpy164juxd3XeaVaqdchPZwGbg9mztX8_WteoAD1s2aXooCNEQYQx5m2iiCCxN_2OZo__07h3TDDJFK2TAoNqOLepKFFJsqS8SxJD-JDHaKexiKtjvgv7WLJCNXYIG0ABo_EGqHILHEH5rLxRBH3c7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V8x5W9LEVMEfc_T4eyxvesw4UY_pmJgDYLqLVq_E6J2KZ3anHrpLOYoOmGo8ePtKDPwjI0KTvGpLNsENMG8-2GO_l1t4c_7b5aJXdvuSa1Z9TDjFixn7UN86EgmeKTOIDXKbmorG5uoaDHKIDE8kZVVagoC-RxjnX6LUy-cPi2eQiC5F_FEZKanvhleIM3v3YDpy164juxd3XeaVaqdchPZwGbg9mztX8_WteoAD1s2aXooCNEQYQx5m2iiCCxN_2OZo__07h3TDDJFK2TAoNqOLepKFFJsqS8SxJD-JDHaKexiKtjvgv7WLJCNXYIG0ABo_EGqHILHEH5rLxRBH3c7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=N4fqGrn2UHpu0YXY02jnFn6vmcON8CcD6PYzq8N2yLvAhMUHXkLe9cge5rfXrJ5WZo5BV4LM90ctdLHcpzerLMSESzRQkfcQyeWwbFpW3oO2NirEasOFMVi9yfWxTqoDMgVp26uzQMkOdDO2i3RFSpBA8czn6OXlhKnKB2pNANzcEw4nmghynzLW3BS_GRxOOFeH73TGfOSy8ERbkPhKuzUBx-1LIyQRnYWHlEDk3-TMog65GheUSFhv1_Uu1p9vcZO-ge4G-KhFGzVmuUc1Gr7bd0LeNF-CIgjdIOtcjua0Y644gpcIrA89VNo-IE4aQds9c6z226PrUjjLbpMF8rN0kBeHfwoU1UpRaURgkLN-9LnCppxqLMYvuAWHiHQ0DGiTmrgLRhAmwJ-DaxDJoWmvOZm4cc1spj4JHSWP3Dgid5_VpK3pJtBKWAmV5PZ24L0fM7ZoEwD4-L_wNofb7WLSxIrLWDP6IyM6YsTU5arRkdci2j3UYop6kmyu0ZOLfhe7waZmmauo54c25Cx_DhDVRF-1X7Qb5JD1RnENWW9b6GV1u7Ux81s5a4zk_gHsiG_hY5SJFn21o0KvTRwqMPRtrrrHUQNcr56OIB9g3s6cG4_-a6lFy6d5JEaP6K1_BIChVXpXwuUSjw8DlLfW3Pyzd1X7rJckMygAjNcogxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=N4fqGrn2UHpu0YXY02jnFn6vmcON8CcD6PYzq8N2yLvAhMUHXkLe9cge5rfXrJ5WZo5BV4LM90ctdLHcpzerLMSESzRQkfcQyeWwbFpW3oO2NirEasOFMVi9yfWxTqoDMgVp26uzQMkOdDO2i3RFSpBA8czn6OXlhKnKB2pNANzcEw4nmghynzLW3BS_GRxOOFeH73TGfOSy8ERbkPhKuzUBx-1LIyQRnYWHlEDk3-TMog65GheUSFhv1_Uu1p9vcZO-ge4G-KhFGzVmuUc1Gr7bd0LeNF-CIgjdIOtcjua0Y644gpcIrA89VNo-IE4aQds9c6z226PrUjjLbpMF8rN0kBeHfwoU1UpRaURgkLN-9LnCppxqLMYvuAWHiHQ0DGiTmrgLRhAmwJ-DaxDJoWmvOZm4cc1spj4JHSWP3Dgid5_VpK3pJtBKWAmV5PZ24L0fM7ZoEwD4-L_wNofb7WLSxIrLWDP6IyM6YsTU5arRkdci2j3UYop6kmyu0ZOLfhe7waZmmauo54c25Cx_DhDVRF-1X7Qb5JD1RnENWW9b6GV1u7Ux81s5a4zk_gHsiG_hY5SJFn21o0KvTRwqMPRtrrrHUQNcr56OIB9g3s6cG4_-a6lFy6d5JEaP6K1_BIChVXpXwuUSjw8DlLfW3Pyzd1X7rJckMygAjNcogxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh59sxTrC1QSrmeiRkHZ5yO5cKxn6RcYhZSLeYU6MQhu49FpyqxSrdY1uVA782022WXA1QjLCUD6FAbhbjuxirdU0H6ThElrF38d8u6C2_WimrxuaG4xhOLJXbaFvfm5Xf40JSqhyh6Cd0unyuHKCkyXvJCNZoQx4XQZ_cUgE_5lNdUcje9YCx9TRbgY4KT5g5PKZ86V-eP8-sOntf1GeRzSuFitr8iGhy5FyX93CExqJvLmLr0JSMtd_H_GyCefUpgBMEvdoVtRTZYquEH7B5Vj5bId2-q9-1-5QylLMi5ZXAtdpeU8cnyUbNyLOAcbMqY55iraxYumpzwgqgkSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=HaWeLQABnSOYBGP3PD_vu7ZqtkoeuBUwbl6s5mvDUWpRrtSm6zXD_lpn5tJug5hrXUATHyjFWlVNmq9cTXadR4WPxRho7zC3jLM4ZCDHN3PooLLQzQwx53NAztRh83PEMKQhLH1OZYhw4QDkGmDso8WqoVMp38xTf-EIfDTMH9rpldX0d3UbRAePSnXjhfI6hW-Qtp9xYnfQCsUn955nAi3mkEskqTNTDvzqe5Fhw3dbBa58Pwe7_778b5GJaydZ1J6NRJJ2stz1fzDhioK3fJxvzSACQQFys3ETEJU6UA3MtQgyI2PFLo7O7JGd9MLPm9a9PFc0obvwoGbOsRAgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=HaWeLQABnSOYBGP3PD_vu7ZqtkoeuBUwbl6s5mvDUWpRrtSm6zXD_lpn5tJug5hrXUATHyjFWlVNmq9cTXadR4WPxRho7zC3jLM4ZCDHN3PooLLQzQwx53NAztRh83PEMKQhLH1OZYhw4QDkGmDso8WqoVMp38xTf-EIfDTMH9rpldX0d3UbRAePSnXjhfI6hW-Qtp9xYnfQCsUn955nAi3mkEskqTNTDvzqe5Fhw3dbBa58Pwe7_778b5GJaydZ1J6NRJJ2stz1fzDhioK3fJxvzSACQQFys3ETEJU6UA3MtQgyI2PFLo7O7JGd9MLPm9a9PFc0obvwoGbOsRAgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
