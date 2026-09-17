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
<img src="https://cdn4.telesco.pe/file/rkdFbq4FaUT-jWbuyhy3PgoAF91wCKLGCzd2_E1MQkPK6EpP5vpqiGAtEnUiq5IRo3eDEjiC_z-jshNY8jh8cVpwBVFXJVFchR9TAhPYgTgGF0t4o4wvVVoLEiUr7hjqHQgSh-dRzj81aCvSJwcJra-dI38CdWxBXWTniS7HdQyV-iFjIfYjORL2C3QqzFrVISmtIat2GAsAF4C9NBx4nEoh19hhuAFRKsxVTSK4-XJlf_RulHDzlyh2GS2SwX3e_b2-RKYFNhAyVw5Btc01vkEH0GRAo8vSpPGyPOLjCTiUTm9Nozds8hvkrqpnhQp7Cyg-pAPgOGdylbsmjQekRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=ghqsWjxT8vke3JGGrv4I4QF7OaxTolHKhtYXbDp-gZVDy8dhXZA7Wg33V_UpeayjXPEUOYNCzTGVAdNnI8awAQXi312pHl2vOdZohn7fIi208qw5QjBKspraVF-3b8k1y26htY7ip5Sx3KOLuAvn_CC5jtCggvALXegw-dcVhhRYwfs5jfvv5Sma1fJ8-k3i5VkFvaVBQXBgvzf9BfKxQnYD1Ty3wFhjBs9n7GZWors-OgOBfFYhvhxlIEMRN4xHgO16lnyVT6Cxs8yoqWbD-MbdiHmY1ro_K5rtjgAUiLHZOxWrPZh1tFwuYOotadKBeVjyCnvS1lttB3IToWPfQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=ghqsWjxT8vke3JGGrv4I4QF7OaxTolHKhtYXbDp-gZVDy8dhXZA7Wg33V_UpeayjXPEUOYNCzTGVAdNnI8awAQXi312pHl2vOdZohn7fIi208qw5QjBKspraVF-3b8k1y26htY7ip5Sx3KOLuAvn_CC5jtCggvALXegw-dcVhhRYwfs5jfvv5Sma1fJ8-k3i5VkFvaVBQXBgvzf9BfKxQnYD1Ty3wFhjBs9n7GZWors-OgOBfFYhvhxlIEMRN4xHgO16lnyVT6Cxs8yoqWbD-MbdiHmY1ro_K5rtjgAUiLHZOxWrPZh1tFwuYOotadKBeVjyCnvS1lttB3IToWPfQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SorkhTimes/140171" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/140170" target="_blank">📅 22:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/140169" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
مدیریت پرسپولیس در حال انجام کارهای تمدید قرارداد ۲ساله سید پیام نیازمند، است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140168" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140167" target="_blank">📅 22:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
👤
مدیرعامل فجر:
📍
انتقال علی بیرو به تیم ما قطعی شد
❌
چون پنجره نقل و انتقالاتی بستس تا نیم فصل باید بشینه سکو
😃
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140166" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0Aekxc56k8nrQUC_6mQb0BHl_hpOWDL4P-U3x_8hgX3dA8uHz_fVg2jxEAKRzgpQVwOrnMqea9vs5xXS4T70McIuy1EyF_aDglbTJzy3ULjMstx-4KRT3q0DPjafD3A7PuEiJE79dKrK8fMLirZoZieyJE1SZDk_mee8TtefzNuOF8joLcl0mguSsZmRbmqlRfRHjOu4kBmggBwZj5SDSvURFrXo8_XERhJDPSCaUrwn0yWpBFwKqGIHNRhRRp7bxdSMIWiNZ5hCSFw9glcYx7rQLY67dh6QcC8TMT61JBzhfeMRX9KiA6buR7SIWCpFom758JcB8Elya9GUYCDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140165" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
❌
باشگاه پرسپولیس کارهای تمدید قرارداد ستارگان خود را آغاز کرده و امیدوار است بتواند آنها را حفظ کند/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140164" target="_blank">📅 20:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
مدیرعامل باشگاه فجر سپاسی؛ انتقال علیرضا بیرانوند دروازه‌بان تیم تراکتور به فجر سپاسی قطعی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140163" target="_blank">📅 20:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M50tCTszq8PyPFuV9URXjkqkbTCAOu5DpBd1AogiCyfQdMrHkzpjRSSLIY_NTSN9RZtyJfBz-a0kmCFb0AAuH0kVw_2qXBHs-PyypmXJE9m1MY9T1sL8pBnIET_fV2YY52fM3P8yBcuUDWgLPnDZTcZv8PtKahp-BhGIcaMwD-V6t1E51LBFLjbdFFPI7plEjEw-DFpGJjtrxdN9V_tHUV1F9UbS2uieebc4oMarE8XWbbDt_QuFnEpIsuuxoaMlmtl8ZHrDCVDswGUEwWCdNqmBfyPLT2IS4ykA7k8ZPU7ciQH8i6cxCkGuuVoy6aK6Ussa8Mnt9ytBw47Yf29lKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سن‌سیرو امشب شاهد تقابل دو تیم بزرگ اروپایی است؛ میلان و بنفیکا در دیداری که می‌تواند از همان دقایق اول با فشار و درگیری زیادی دنبال شود.
[
🔴
AC Milan
Vs
🔴
Benfica
]
⚽️
میلان روی بازی در عرض و نفوذ از کناره‌ها حساب می‌کند و بنفیکا هم با جابه‌جایی سریع بازیکنانش می‌تواند فضاهایی میان خطوط پیدا کند. اگر پرتغالی‌ها بتوانند از پرس میلان عبور کنند، ضدحملاتشان می‌تواند جدی باشد؛ در طرف مقابل، حفظ توپ و صبر در ساخت حمله برای روسونری اهمیت زیادی خواهد داشت.
🟢
امشب چه کسی برنده این نبرد اروپایی خواهد بود؟
📌
میلان و بنفیکا را با وینکوبت دنبال کنید؛ همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140162" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140161" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
النصر هم به طور عجیبی سه گل خورده از العین ..خدا به داد کیسه برسه با این العین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140160" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140159" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140158" target="_blank">📅 18:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
رسانه های عراقی: بشار رسن دنبال اینه برگرده به پرسپولیس
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140156" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140155" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140154" target="_blank">📅 18:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140153" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
شنیده ها: تراکتور نیم‌ فصل برای جذب حسین ابرقویی وارد میشه!
✔️
✔️
گفته میشه تراکتوری‌ها ابرقویی رو زیر نظر دارن و احتمال اقدام برای جذبش در نیم‌فصل وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140152" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
حسین ابرقویی مدافع میانی29ساله پرسپولیس چند پیشنهاد لیگ برتری دریافت کرده و قصد داره توافقی از جمع شاگردان مهدی تارتار جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140151" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_AtpoGF60l9mrr_mfrdxdgGhhjX6YzWN4cZESuwofl2Zzj26RexoWmfcz9yU6AbAkJysVjY5s0ryEeFOS26EhL3bhCirVW6DXmBfIwyoN2oXLfwMxDY1XOAiOLJSLeC33PhA24oumujpxClqR_0aC7nG_g-rwT_iU7S0cqhT4FukZBxD1muueZ0WwgLYdruCHM9t9Tjt4LYRv7pk259A3gKYMIKRF852kB4DzKfY-NuPlfEYdFuG52-BE0RAlSxEt5m99Td51n-EqcQ5iR0COWdo7bhU1tkX3xQJuGhYzcJXGqa_PVpKa2N4liwPIuofgTu-hcVXXTUOXxEJIAK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❤️
ایشون بعد از اردو ترکیه که مصدوم شد حتی تو یک تمرین تیم شرکت نکرده و حتی نمیدونیم مصدومیت‌ش دقیقا چی هست و داره چی کار می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140150" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6afC2rWCwW9sAqWIPMdmbTkyUbB7EZcEMKovIpc916pdqhE1z5HQiCMLefskeEYlV86WZTuCkbTYEdVCk6RnSluEB9zGd7upwprSY9PMPgIU5vYaL6MHJ-8VDqOLmXCgaUOPKXIcqWRBzph2ubOPHOC8zsdeOfI7qg9F4fsiHodklF6slgX6jsNZ4obDSk8W5t5s1bJ2TdTPjh1Tl0XS02DUY9I5rYnXNmLDWeIhlEUbOw972RS52E35m5N5rlvGiIXqi-Ja5KGrRBFcNmsTVO6NkUyLAOw1-lauzag4FQvjWepKxl6F4ppAGcuNQmXe7kAUsh2-GviQvNXPjOW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته میشود باشگاه پرسپولیس دیگر برنامه‌ای برای خرید امتیاز تیم لیگ یکی ندارد و به دنبال خرید تیم لیگ دویی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140149" target="_blank">📅 14:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140148" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOSwi7NwJtIBlkSuznD8W_NpKXXinBkQVwft7HDlG1yTplo2PrHoVcYm2OYpBhJNwi1p0ISQQve61p_QPD-BP1SdWct_xSOhADuQS2cudPWTd3jhtak15L6pu1kBNC2lbn9_S2kwXkGvGmGlz3rugkXdUwGOTvCbHHqndIUsV4qEX-7771hGglkP3Hm4iiQfMshSFMwidslZhmBwKE3InP1LUCKHV58DefZ3Awlvzq1auIXlM-IbyZ5TEeD1KvDx8aOFKkfYZZXP6hzodtDnztgeAD8M6JLU4qxTcZtsPCKFT0XE-3CP0j0pziR8Z4nkMW5OWMwfHfP_7_45OlffqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibSsuLhg4iBKo4TPhY9WQWvZWMuLLmDcggrvZdvsMpD4ceGJYNE_phuas_2Dl4Hd0DV_o4naZ1Smo45-Se4Z9KZ4lN-56j4K_GOYc36IYwrrR3lM9WinHsn9g2_zncJZkl5wc_xL-hjuSB938wFWf0wmCIoIbzkvJ6URQ8dpILd-YvA78DoUwF-Z-JPwBc1sIEsAFqswDiCYQvTuQNf9klmMrTpCTa_RhUQjEcvK9MPUkSI1s4NUUSc08umZu4E-rxr8B2U9Q_4mIIU6posWPFFwJF4zpQsfDnggfix4tNfgMdi5JZs7kNi7qdmgzkxSmk6BZ7ZiMKOOqsrpHBC57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTTy9RdZcNJTVxXcG5Km4-3TPRU8l_MMAucSX_-N-Wfnez0ULb0h28oa-C3YyWazNwFZcpJiCLtzrwkE-OEH0t0V56cxX0-ZPBo_f-QQ1tjdxus7uLgKiAgcqHUCddOyNXC4clv95TE5A02cFxT4NL1WHfJurzSwdivvVfVXxZfjVQCG8K7svLio6CU3fC1VNUdGM1KhV5xgAhYB9gjH2Ksz5SMKxi5cT9TF9QQkFjqVT1Hm47HBwCGfzFN48aGDtHl2BD819IxKuHmyEs66wqDYXmJ7YcsanlAn2kFATrAke8LkQ4nCtyHhwPojgWQuKtgQjFxMJV6uUrr0xgJd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=JM9XeQZUjQmM5b0DZgr0pdWgtFwB3iWTCFAwNQoYWJcM4Fv3XhNfhMELwYoEic8_ItSVVLOpf2Y-ZOOpOgwqVzYzg1-93JItoPnanPEhssjBWCOEMc9o16fMcL5xQDaDndTb1tM7OhofTudN8Qw-T0To9LD5R3wDDzyMhEFXoDs-23wChZOZzIO9x7WWCB-l-mS6FdFUrgtXqPbNyPW-AwcS0To7OMnJZ9Su1tspGoNpC3uI_vgSj1cLKgk2N_tr9i6wV54ldp15WasRk-IBKUU3UjFVQex-GOwPqQ2uT3nOlVJOidKp5rn0C3Pl61TwzIVoS8zyLv28_0glKsyBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=JM9XeQZUjQmM5b0DZgr0pdWgtFwB3iWTCFAwNQoYWJcM4Fv3XhNfhMELwYoEic8_ItSVVLOpf2Y-ZOOpOgwqVzYzg1-93JItoPnanPEhssjBWCOEMc9o16fMcL5xQDaDndTb1tM7OhofTudN8Qw-T0To9LD5R3wDDzyMhEFXoDs-23wChZOZzIO9x7WWCB-l-mS6FdFUrgtXqPbNyPW-AwcS0To7OMnJZ9Su1tspGoNpC3uI_vgSj1cLKgk2N_tr9i6wV54ldp15WasRk-IBKUU3UjFVQex-GOwPqQ2uT3nOlVJOidKp5rn0C3Pl61TwzIVoS8zyLv28_0glKsyBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=PNNMQc7HjrXM7ISbKg0bVB8NBC1XppqVBsgmBJa_AtN-C0pVa3tq-VfLqasN6BBfslIMu5JVsfOa8Jv9Amdby-atuoJ02ioh7iB_vjVuZvXR5awsQkeja8LJmBYUxchKR5761F4S1M_ZKOmduBY1Ci1t1OrkJu7hJSROyshHae56xFd6Ql8vHTkN7k171LEz77oHTgjL-LGfCT2JzshH848SXEheZLryTpxw0e615VKCjp5DYuJNlKogzw2WUtQ4D2QKhg_j5hXazpBvDG57e6afwV7ket0vtjORusdA-bkXQphc2MVn9n8ml3_IQndBsDgi4a2A8Ya6KelPBb8rqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=PNNMQc7HjrXM7ISbKg0bVB8NBC1XppqVBsgmBJa_AtN-C0pVa3tq-VfLqasN6BBfslIMu5JVsfOa8Jv9Amdby-atuoJ02ioh7iB_vjVuZvXR5awsQkeja8LJmBYUxchKR5761F4S1M_ZKOmduBY1Ci1t1OrkJu7hJSROyshHae56xFd6Ql8vHTkN7k171LEz77oHTgjL-LGfCT2JzshH848SXEheZLryTpxw0e615VKCjp5DYuJNlKogzw2WUtQ4D2QKhg_j5hXazpBvDG57e6afwV7ket0vtjORusdA-bkXQphc2MVn9n8ml3_IQndBsDgi4a2A8Ya6KelPBb8rqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=N0k4na-oP9Kj5RS4-ogqXC77SWAkfauKxJqFdaGBorPoaNyimEvb5m9lFqNs5fkijGm9Wl9hyjRRlA_HqNNENpdwRQEJuKiaZPRzMwh-K2J5GcDEs80_N2ho9kHReYekV8G6_xHeVLM8yRXD_MTKcN9De0iUy49JrkmN8JSuJked9Nyf1TFTmzKF_Got7EYBZhnJOOjh_YVLTAXuFzt3hEOwPSE--cgT8wQWzR980nhpoyBjVQ3ccx9ywa7X9ASSijalOX-SIa81SujOrxQKEDq9nasxF6KhjSPaZsha_ttjGmRfEigiayX_zjf_Nh5le_sti_WFYDiK3Tx-uUtL_T2DEuEoNKlhxgHChJ5K6FYbGyJrTk5VV1Q9mFAiLgux9tQgWCZ9l7zhLvo5o1wGsnhDv3aJZ8MDZvrzjpLWIRwDRwTZR9luOH_rtvEdFA2nLAXRLWPJy8E1HL_kl2zwKUV3fUnSAMdaw5lqaFc_51hmBHsqWs7MiEnAkXUMUGixHYw3smzAKRQUBru2Vb9gsR3R_Ubjz7AfIb4bEwiM0caJ-F0fOCs9kQqDRjpIQevSRnJ32NbEaz1Kj7qXKJ_DjNzVcLe4-8i707v8iwpXg2vhs9C1-x7o21YvODxjCgNqIxRwc6ivG2KKL_2nyijrjP6wDwIOaVefGj41dvHVdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=N0k4na-oP9Kj5RS4-ogqXC77SWAkfauKxJqFdaGBorPoaNyimEvb5m9lFqNs5fkijGm9Wl9hyjRRlA_HqNNENpdwRQEJuKiaZPRzMwh-K2J5GcDEs80_N2ho9kHReYekV8G6_xHeVLM8yRXD_MTKcN9De0iUy49JrkmN8JSuJked9Nyf1TFTmzKF_Got7EYBZhnJOOjh_YVLTAXuFzt3hEOwPSE--cgT8wQWzR980nhpoyBjVQ3ccx9ywa7X9ASSijalOX-SIa81SujOrxQKEDq9nasxF6KhjSPaZsha_ttjGmRfEigiayX_zjf_Nh5le_sti_WFYDiK3Tx-uUtL_T2DEuEoNKlhxgHChJ5K6FYbGyJrTk5VV1Q9mFAiLgux9tQgWCZ9l7zhLvo5o1wGsnhDv3aJZ8MDZvrzjpLWIRwDRwTZR9luOH_rtvEdFA2nLAXRLWPJy8E1HL_kl2zwKUV3fUnSAMdaw5lqaFc_51hmBHsqWs7MiEnAkXUMUGixHYw3smzAKRQUBru2Vb9gsR3R_Ubjz7AfIb4bEwiM0caJ-F0fOCs9kQqDRjpIQevSRnJ32NbEaz1Kj7qXKJ_DjNzVcLe4-8i707v8iwpXg2vhs9C1-x7o21YvODxjCgNqIxRwc6ivG2KKL_2nyijrjP6wDwIOaVefGj41dvHVdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIC1-3FJndoJgenn7YDTI2ZLRfynp5TCG6oqTah1ZPJ01XXWZr5fRvTZZcJvG2a2OKVT4BbQzDnXkRPFEI3Ml5tcC9ElZWRFpcwGUMeISubRbVd2LDNp7EwFfMFZFY50oMgFqCJK9icMwaikQxK2sPJRVufnYKToPGIOLD2GAHAOlQ4ruq05TF4Jvv_aq9ATy3P-7v-Qbee20KDyFS0Xy06rRYiqrSec_hJpSypPKte9oDEkIj8s693LD_W7I-xvQJ2QGkq02tKTVZ1qv6MqqNaecMx2W5YPCfj5B1pbuKDlqg751AisRwKBTr8V3AZrRd4l1qrWUOdzOdcXZBBt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMit5tDGJeSuBCbtLf4jOjT79g-yPoTjaCKGjejN2SsbEO8H8q8QJ4ZpHKPFlCVnUZ_ZdxTwpdAKJid6N_Ws9RTIZraw7C-fTZsbPcM4DKNjMZQhvMPAY8GDoMofoPDRwm7Ditq7sPpCXpWX69mkCZLQwkFLdn1Pxddiya7R81xcciPjvpny0aMhdyn-7cxTtUIRIejDNijjpNnimyPnY16JrNVn0SUneNB9DH8wYsEWjVzeykFJTWvLow-LHWmJVKP1L9O7OQeIdvhKhgB1HqH_VapNvXBRxPEN-LQO12HHPOuTdmlOnFdxnWLbGepQOnJLEmns2ksEMgWHC2AY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JxRrv3sidPabs9tpVDWOFT50bzg1U2Fx1wignYq0IFapLEVEZbz6MzsB1X6AnP-G-G4QF6Bq37VsoDyWK5NeNm8au8R6N-bPOdvdWZQkWNCZWy2CL68c0c-uQDhNrXuiu1HRPWdHRtJpBa6i2UVp9Scy0cigeG4LR2tqSkwoupY8UCxrvAAmpOa0mUZPIIvSYqMyi7ZZmtlOmxdIQpS8ngkDvWtimkl2euAIlPdn3aGrPygN07C3CgCaksoQ5YXRPaHBHKA_mwHIsuaJFJPVts6D9m3hkshsfQ2Yyjocc3Nsenbwrsg-zhfanDfdDFGx-J3rGiKxEGEJYnHIHOUkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTjEdHeQvZfYyuZTNyzTziHLfptL9fiHQwECfSdPnXw4rZiP8UgsdBztK2LZXgBAKsPKnYjPcYvJ9OZFqV1_l_CnJUMvGdTvaUS8Zk58XfMpErFU7Or4IEuHqGQtT8U3hILBGz-bNfuVmFni1iDjp6ujt_xkRrVtSz0Vf5ziH3Qm0m5v04J624vVRj5R4w4RayZPo4XNLymdyGUmT_XHS1zWfzHzCLkQ3rV3Trvat9JA3cyruu20Z9Bt8Zgp_qUwTRc371CiYb3OEVpp8xqH8Y0SoLePh4VL-6zPI652BR3W295a_UnyOewRkFjB61W9d_f3nMF3jAlkcHzpD08s7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=eK3SRZwU7RecQhO_6a_w3kMKPnJwaNcn1JMTozqlO6ZaAdV_btoxxOalJI8o9ZoKSIPxr01cRKyTdbvUV_gc3bdPXLLf3W_JI3UMSjPqVN0_KLVzI_z9bTSf2zTNHtxcXZkqi9l_YKhmvdAo8dXiwulqGAxq8YEu2432UPX6DGiRj6sagMLLT9B-3CXk65Xp6gK01Lp4QYDK-hCuONA7B3jYerKRuHfSXjR5hS2XOXQG6UPdNgoyS-sJBt6_xAJ1kZJjnWCsm2U7V0zgTAWuptapzShaIkkEEmt8tytGqmbo4zWXbWDz-fFUxJMRQWHc82XRr1XK2wpxOjissvu6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=eK3SRZwU7RecQhO_6a_w3kMKPnJwaNcn1JMTozqlO6ZaAdV_btoxxOalJI8o9ZoKSIPxr01cRKyTdbvUV_gc3bdPXLLf3W_JI3UMSjPqVN0_KLVzI_z9bTSf2zTNHtxcXZkqi9l_YKhmvdAo8dXiwulqGAxq8YEu2432UPX6DGiRj6sagMLLT9B-3CXk65Xp6gK01Lp4QYDK-hCuONA7B3jYerKRuHfSXjR5hS2XOXQG6UPdNgoyS-sJBt6_xAJ1kZJjnWCsm2U7V0zgTAWuptapzShaIkkEEmt8tytGqmbo4zWXbWDz-fFUxJMRQWHc82XRr1XK2wpxOjissvu6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=OyLzWxgtsq1bxr6EevKcZiV_rj1t5fz3rizn_DqcvUi4GSg48gyfVcM1h-8VQypVXRhjOs4TpIyshMPI0jdb7iMUPfe9D7nbnWxplxpMecuxSZdYCSrfjzYBcKZA8VmqjGUcvrfr8u7N8eOVuJ8aiQJ7Mrps9GRVeFdmnDSOAyrHsNfmFmuU6uJDPkUMJozp8wS8Vi4LM46pkbtnW1uEf92D5U-rJWRKCyRs07235ShYl-iaRnjjM_9wPHHgR01tdsjmuCmbCauE2ghF1g2fuMSQLKqMjpA6mSKHQOrc6LVYanlgQxf9iWFu0D0B1g_B_tyMKKSWYZHpz8cBsLcLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=OyLzWxgtsq1bxr6EevKcZiV_rj1t5fz3rizn_DqcvUi4GSg48gyfVcM1h-8VQypVXRhjOs4TpIyshMPI0jdb7iMUPfe9D7nbnWxplxpMecuxSZdYCSrfjzYBcKZA8VmqjGUcvrfr8u7N8eOVuJ8aiQJ7Mrps9GRVeFdmnDSOAyrHsNfmFmuU6uJDPkUMJozp8wS8Vi4LM46pkbtnW1uEf92D5U-rJWRKCyRs07235ShYl-iaRnjjM_9wPHHgR01tdsjmuCmbCauE2ghF1g2fuMSQLKqMjpA6mSKHQOrc6LVYanlgQxf9iWFu0D0B1g_B_tyMKKSWYZHpz8cBsLcLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=OVrP_NnyQ0cnn4sbzMkOP25mS1eJGUGNap5X_JuC9UwbNSoJHCVTWXzxMVEVxaRsowYPtIf9QyFRMa0RwB3ImP-42_r5c1nApUFfHwbAUGsi5DoeZS5bynES8-1cARjBVDXpdCNvvhVwH3JSoais6dFhjrD0mFRWKHHUYUl_eELihKGF0e54tgghJtmezfWhpQwI_Mp1s0LEkOM9caQvOIls7MFrKroOXEho3MSVDG_F0vyln3rjqQiG8fkEQRMz2MWudCV5t5wcWhUNV-cHbMsT78ulDsozlmE_Llebl9LIngPaYssa9slULQoACbjQgTrMXN5WYfD_wM8wX26zKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=OVrP_NnyQ0cnn4sbzMkOP25mS1eJGUGNap5X_JuC9UwbNSoJHCVTWXzxMVEVxaRsowYPtIf9QyFRMa0RwB3ImP-42_r5c1nApUFfHwbAUGsi5DoeZS5bynES8-1cARjBVDXpdCNvvhVwH3JSoais6dFhjrD0mFRWKHHUYUl_eELihKGF0e54tgghJtmezfWhpQwI_Mp1s0LEkOM9caQvOIls7MFrKroOXEho3MSVDG_F0vyln3rjqQiG8fkEQRMz2MWudCV5t5wcWhUNV-cHbMsT78ulDsozlmE_Llebl9LIngPaYssa9slULQoACbjQgTrMXN5WYfD_wM8wX26zKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=j4LUg8Y0F6jRc70nJB7v5-OUq29pN2hw-tv6p9fXzYqySlfZk4xaux0iKmgONC-PZPpKYSJTHlLU58cDSNMoYq0IyUb_pwJ7IQckWX78IEWqX1HEfwM2NPIals72gJmtUIpEQvwpnPTY6B90It5jD_uag-xE48BqYtidLoTQNmngxPhxyYgUcwe7nZbioW7ZAvXnIH9uQSBxkDGpQ1T5j-Szp_394P3cIQUly0nlSP2nYLkqGjUxkj_OZ6uYKEQgwMMTVnd7blmB1fLTNfC9h96GKvVA26iTCOUFy-oIUb77K8qLXkD-t5ZVoyajipY69kaI8iPyhvebwZjgrSN0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=j4LUg8Y0F6jRc70nJB7v5-OUq29pN2hw-tv6p9fXzYqySlfZk4xaux0iKmgONC-PZPpKYSJTHlLU58cDSNMoYq0IyUb_pwJ7IQckWX78IEWqX1HEfwM2NPIals72gJmtUIpEQvwpnPTY6B90It5jD_uag-xE48BqYtidLoTQNmngxPhxyYgUcwe7nZbioW7ZAvXnIH9uQSBxkDGpQ1T5j-Szp_394P3cIQUly0nlSP2nYLkqGjUxkj_OZ6uYKEQgwMMTVnd7blmB1fLTNfC9h96GKvVA26iTCOUFy-oIUb77K8qLXkD-t5ZVoyajipY69kaI8iPyhvebwZjgrSN0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I0xWS7krQ0blvaK06uMGu7WB4Eha-L8n9j2TsEK24IaaTxRVRANzFo-0hCf-AbO1BSzKgIvM58nruhJoCygban2mSfsAseegpVIGNM5on5IdSqmOKqraNoFbsFkYBthahHTmuAvoH1cU6wbqwB76TF0uhtu6tmhhqs9aANjJyEnd5HqQocnWyQXj7nj-1f-LM5rPFdQrxMYOnWW5zSJDY69soyGVLTGrlZYTeMAuboSc9fXPljbBgCSEf4SUhzyqjqB1WBUp7ztqC6Nyp5AkeaMaBodeFOlTNWNchLN1F73xlNHuoZqy-MKt3MePIh1VO8z_x-u1fa5ZJg61tWMrD4ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I0xWS7krQ0blvaK06uMGu7WB4Eha-L8n9j2TsEK24IaaTxRVRANzFo-0hCf-AbO1BSzKgIvM58nruhJoCygban2mSfsAseegpVIGNM5on5IdSqmOKqraNoFbsFkYBthahHTmuAvoH1cU6wbqwB76TF0uhtu6tmhhqs9aANjJyEnd5HqQocnWyQXj7nj-1f-LM5rPFdQrxMYOnWW5zSJDY69soyGVLTGrlZYTeMAuboSc9fXPljbBgCSEf4SUhzyqjqB1WBUp7ztqC6Nyp5AkeaMaBodeFOlTNWNchLN1F73xlNHuoZqy-MKt3MePIh1VO8z_x-u1fa5ZJg61tWMrD4ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ42_pUPgHs5JF0eXDAhLXApwDIZhq1anp-ZfW5V8t4izb16O054sLVj_h1qPVAqA7CERmq1zUDqOF0Xqg2l3rwgnQrB1mrM_bnbV4JcRC7GjP8opbdkeVKEPMn3lFUTdqhV89R2-d8NxGP1wGFA2dfaBiWf70kAg84MEHF5XFkBH1dvcEFJzHtkuUVimKdRscggUVlv7FdCaZpxrNaonqsWv3EDzM-LZSDhpevoLxMvK-FmJUrKw9MavYgc3osy-QMn7xo0WNeALluvdcMaXYmEsrXXddku32o6kxi3QAepomy1oqpkWfZF_qQnk6-a5mZL8X7pC6pboLbq7JiBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHjdv9VdrKbsKayZ1_CdcVDOQop1FSDw9kh5ZvJYtmijwifbfZlcKgDWH9XB5GJ5_08sFBn5SdzAykD0mhKy-ziFDBdnTc1tZfbwTTuqrvjOJ6r6jp8zD-kb5Tj1bG-hwisela52si2i1RFzplBxxgSaP3Ony8LOcM0Aw015Hz5FBAH-XL3uHLKmct98q2YdiBpb2uGoMJLGTYB4XFNvLYUS5LwziYYrnTHSJKTstF_GlhT726u1QshrGc_HetOqEe2_moeBnivMlO9GPzEY0rasxc-EemT3fPnBOhmEJ4YW_F78l69yCuYnXBCW0BqqWCC03KtBnXm-Fi6b3xas_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwvS82sp7Lmm2zRbUHnvJxs_wX1JXtRw6G6US8XKW_tu8uXYuxwwjTp6hBzW1rGpCYQdiZBwnrQf4WHUCMlX9uQuBIK-jkpMJcRhJXLk91Ym7fMiLsO_dN6FpSllia0_xLiE4DEH0UgTUorcMnLSSYJiX1SQaeeQ2gszDoy3I_zEkLig6w0mGtGluWx-JxKErNJO6UxIEml86JV7Kd-tN78yH0u-sW1Swu6eJRCemLyYs7Bx0FggiefpmFVwqAKIiRucTA_PMj0vwmmiJiwl_FrC1phkJySIP2JXu6N4kwiw8GcpK74aPVtvZnJ3mne5PFu72r8_IpwHZ0yumetcIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9bfVw98RTO_hdfrr9pJf8V6df6pV6q9Gy7xqLzxIeIXgjRv49lplrbTqWOtyAOWCbLpzGXLd4BsUG45ivQaz-cp593y1BLdyb-Jam3N2yHqCtBCteIfMeyJjs3HY9i8jXN9-VU-OhW2Wzi8ipms0p1LCmdwK9e6amGewgs5VlSj2PaYLykBQKXfhC6KjYaW6HK23Z5W4M7QX9D4XzpNVdB8N0-taP5ffsVBC1AOnDGnox27X_tghcOlUKtAITL4VSWF69mu4Ior7Ng5cjvJxna_pVryW2Oew0iuklR1116gl2Qh0P7Mzv9SzSuwWcAZNofmh70F9v8mF-DkQker6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0lWsTyMj5Oe6vsmnJmY5uEb2qC0C5sXsyPMFE3278n1qQHcGS2eexEkrYvhm8mKiC_0_OLlyFIlqGToFdhACpAk5bDpOPOFNFNsAw6BVQD4b_HQxDumrhCjf6LghRLlQQQSUq2ob9gSD8eBCMoPsjCctgrmeV38-N3vEw0BbBVwsZZBKtT0_Eh0bl0htDiof4NrLjo-9T7XSPCrfCV6VsIc2J4p_YD9gQQhc_JEV6uHPxDmVwsLtzzbReNX0fks5HibhYSYlOyCeIMB69VbLFBxX_OBcgwxuu8d0lk7D4kMPgeWsiHDBSRAta9hBaRbvApNdKbtguRteqeSH9v8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=vC5AEFZdNphKtv-PcI8aWfKekc4ukdlaf9AX_aMuIjbk6wJraS3kZzogaHSQnwipFc8pUHIkhChCoCyfHsc2QXoz6vK15C5XuSbBRtWd9B17DenejLi9g_Z6g5mQaGlHYM5j18V2DJEj5xcTdCby5diN2iXyWNNmFKO4zqogO9Px-BBNIQkf0yqJuALBJ7tDqJ4OFi_5TOK6cQ9_X846DCT4riqbCyvCOAibyB_D6pFNQBU-SA87q6DjjpczVtnFD53gvJEdKMFKOOQ5MRiokTpUd52WVSqdySSQiD87R8Z1x-FpWvK1Poo2c9oWZ2z3jBai6m-0ZUNzCjul93qaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=vC5AEFZdNphKtv-PcI8aWfKekc4ukdlaf9AX_aMuIjbk6wJraS3kZzogaHSQnwipFc8pUHIkhChCoCyfHsc2QXoz6vK15C5XuSbBRtWd9B17DenejLi9g_Z6g5mQaGlHYM5j18V2DJEj5xcTdCby5diN2iXyWNNmFKO4zqogO9Px-BBNIQkf0yqJuALBJ7tDqJ4OFi_5TOK6cQ9_X846DCT4riqbCyvCOAibyB_D6pFNQBU-SA87q6DjjpczVtnFD53gvJEdKMFKOOQ5MRiokTpUd52WVSqdySSQiD87R8Z1x-FpWvK1Poo2c9oWZ2z3jBai6m-0ZUNzCjul93qaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140106" target="_blank">📅 16:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140105" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔄
🔄
احد میرزایی، عضو هیات مدیره باشگاه پرسپولیس با جذب محمد قربانی مخالف هست و میگن لازم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140104" target="_blank">📅 16:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyGYb7cDepk7_cvcX2GR8d49bSptiIKXSQu6FanViPm3t1BEue0Ow5r4DZJ7vYr3nV7n36AxdN3f2pRyp0a0ZV3k0yWu4oBYu4YVEmyo81OCqcLDlJ8rpOP_5YqFCOZCw1exbZyGpQyrbP9yEypTzxMtfXTf5eygi3cu9GmK0mqIMiO4r2ZGnI0n_gEtgckLIqARG7xoDjAyHnkVLvwDJSFQ0ViIaXgNFLGs60Y42fqkkYXVQoP76b2LTREPljdcZmEAbC77-gj_fwJX1Sc0MlM70gzxUZ1Isz9McgvJ-LeytWRW85nNMLG0S8Ho1O3HkFb33gTxOjPYybp-4m4ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حامد کاویان پور مدیر آکادمی پرسپولیس شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140103" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
محمد حسین صادقی برای اولین بار در لیست پرسپولیس پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140102" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140101" target="_blank">📅 14:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
عبدی: با ۱۸ بازیکن مقابل امارات قرار می‌گیریم/ بازیکنان استقلال و تراکتور روز بازی می‌رسند
✔️
✔️
زمان حضور رضا غندی پور بازیکن شباب الاهلی امارات؟ ما منتظر تمام نفرات ایست بودیم. مبین دهقان از امارات آمد اما غندی‌پور نیامد و متاسفانه او در تیم باشگاهی‌اش…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140100" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh_Fp39WBABiGrIp0tjShSEp76SfffAlEJK9LscB8TYxan55GGdq-lKqoHTlbhfOgtMiX_2KYVE1WunmcYl-04TFtfLtlgM7EZ2sMCJdenwPm69K-qwa-B4OgK64NDEHMpjD13ytOdjlcb5M4x3XPjF0u7LIvFe1A9AsQ2HIo12BhQIdprNvm1cEDB6DWFw4i-7KHMZftWVtE6832HNC4mqSmg9LPWGtVLqHi8qFxdghmv0I44P63C6lBfgIcalbY9tdhW-7XOlrRr1EY5kE3yyG9wf2gNcaucfHZj82OhToXopvYWVsj57gn3vyusuyiOO02nrIVW2r2TeJJKHSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش،
دنبال جذب مارکو باکیچ
در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140099" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽
امیر عابدینی مدیرعامل اسبق پرسپولیس: مدیران پرسپولیس عملکرد خوبی دارند؛قهرمان جام ملت‌ها نمی‌شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140098" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgPvRvfsA6_mlJnzJ_bToLoZHcNYlToYI_vMr7D8EkqQgsiIr35chE5SKIqyck2rGPga4oEOatnxaWpJiPoWGZfpysl5sz_RWHTpxcjM5zCst2wAzCst8ibdgFQjylWNyGhXwBlQuPFpqfk7SEU4RlmR8hEbA9NSFoUKEyMNTsjmBbjMgZNH71xngYAhq-2mf7SGq1QCqN80BEwIrI73HjRoQazIn6dvTloLMFDjyGy7S1JmmUyUdF0TwxE5HDWVciQ22lD6-oFcwtl5K4SQCpDmOkEyKXM7tv-gNM3HmL4LJNI6zr20blxOG97wRM0Qdf1ZZsEIUvqpAuf8f4Q7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool -
⚪️
Tottenham
⏰
Tonight 22:30
🏟
Anfield
🟢
لیورپول با وجود احتمال چرخش ترکیب، در آنفیلد از نظر کیفیت و عمق تیم دست بالاتر را دارد؛ مخصوصاً مقابل تاتنهامی که در چهار بازی لیگ هنوز گل نزده است.
اسپرز برای جبران فشار فعلی احتمالاً بازی بازتری ارائه می‌دهد و همین موضوع می‌تواند فضاهای مناسبی برای حملات سریع لیورپول ایجاد کند.
کفه ترازو به سمت لیورپول است؛ برد میزبان محتمل‌تر به نظر می‌رسد، اما چرخش ترکیب می‌تواند بازی را از یک‌طرفه شدن دور کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140097" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140096" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140095" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzfKmmmk7MZ0iBvWWiRL7LRnLE_nkiUkQTVgSfNh33-75CgD3FstSPKUETmim0U53bspLJ0D3gKlM7C5ZHFKQWov2YQmHRk9H1KL9uPD0VxGWekUgUZja2HBca7xv_gDQdxZxqSuow-nH1xnucbTvrVo5VBTojPsc2Co7q2q9fqmZk__B2ZJElZSAosacAYzUQRRZGLv48ywMxzbD3eqKjhnwGgRt4hrvLPCo5ZFBnsJxLPU5zltid-9qLAoKjBljLBE7mhJ6qvmg_ijnI0Rs_iDj7B2QZ24vdamhJwMV5GwHlYhzkoHWEUOOKjckdxunB94mJ7IoLsF7Pd5T3eCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس؛ عاشق لیگ فشرده
🔺
اسکواد پرمهره پرسپولیس باعث شده برخلاف رقبا، سرخ‌ها از بازی‌های بیشتر استقبال کنن؛ حتی لغو بازی با خیبر هم با اعتراضشون همراه شد.
🔺
پرسپولیس برای برگزاری جام حذفی هم اصرار داره؛ چون با این تیم، شانس گرفتن جام بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140094" target="_blank">📅 11:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
حسین عبدی: محسن خلیلی همین الان بهم زنگ زد گفت سه تا بازیکن مون برای دربی بهمون قرض بدین منم گفتم با فدراسیون صحبت کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140093" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140092" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjnkQFc9sZAcnNVO9iaxU3L0a8W7urKhm3x-qz4XdyTS3HRQLmqa0qwDgIl-iN-pjeV_SqWD-3eVhIV_A2kEiR6Plm7OLL3Z4B9D0qhlSSgMfCtt9xZIcZHSDUU2zXtwB4K3Tq1Kbwp1gU7O5k2zAo-04Mz5uaJyONzl5r2b2dh5kkZGN6QJ2GErxPfd5nlLhhqwTz9WKasa0GEVQPU9bcx37_ShDOvYZAth1ao8yZgFshPmEWdgEvJRo1HK8ZmKYhyO_5pTxQ46pSlTNpSmgWnHcm6RV5Z4KIsEjju9a_HYUK7eL31-uVLWUO9wgXjYPsfzPE294hDq1QwImJzoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140091" target="_blank">📅 09:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1_SYazuOQBOqY5i3hrp7_7fc6zCBUcA_LakNlZEH-EKdZ-SoyaI63ONn3Y_XkEXgHurjPReA5Fi8dhvk_Svi5P0WZSazz_wrBo0gFgIkNxCZXw2pRjuBz8cMMTcItV0taQznURqgurN4VIkkAho5WrcLcC9KEmhlKTuoITIhR85XVPt1uRpStep9PURtUkalS_cLSTwo8SzPWzUKvpMnhpgu4-0QbvVivcnFXCGX68jxfPDfSfIRB37OCRt6VxgMkS3wfRqetYCWRVMnE7dJwQJIRpt7XRTf1ksBEbhICJY84nkcK23roR41F_t7pa9Nt9yH2yNpqM0Q9wPIU4ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فردا شبِ پرهیجان فوتبال؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین داستان فرق می‌کنه
🔥
⚡️
⚽️
فردا ترکیبی از بازی‌های کم‌ریسک و چند تقابل جذاب برای دنبال‌کردن دارد؛ الهلال روی کاغذ شانس اول برابر الغرافه است و رئال مادرید هم مقابل الچه دست بالاتر را دارد، اما ارزش اصلی در بازی‌های نزدیک‌تر دیده می‌شود. لیورپول با تاتنهام می‌تواند از نظر ریتم و موقعیت‌سازی دیدنی باشد، در حالی که آرسنال مقابل ایپسویچ و فیورنتینا برابر پیزا با توجه به شرایط بازی، گزینه‌های قابل‌توجهی برای بررسی هستند. در مجموع، شب شلوغی پیش روست؛ جایی که تفاوت بین «انتخاب روی کاغذ» و «انتخاب با تحلیل» می‌تواند تعیین‌کننده باشد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/140090" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
حداقل میذاشتین یه سال از حماسه ۷ تایی شدنتون بگذره بعد کری میخوندین نخبه های لعنتی، هر وقت رسیدین فینال آسیا میتونین کری بخونین هفتایی های جوگیر
✔️
✔️
کیسه‌کشا هفته اول آسیا: بریم واسه ستاره سوم
✔️
✔️
کیسه‌کشا بعد حذف: عشق فقط فوتبال اروپا
😂
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140089" target="_blank">📅 00:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8ddAEXKyP_Fj2uLj7OUC9UPRqCBD_Sxi9yo8pb-s9sMCU1IBgk84aq2rmpmAQHZxXokTjQ_83Fem52IAlCSNIg704b7yTSLzVl86rf-05DGze_iYZ15qg3MDC10bEcHRsqa9YoT2AMtqEXgym2_YrE2NCXLJhfDQJG_CZ7a0PB1afNc-W5vmmnwOgiZTzlzriDt5DdpN7UrWPgAXE_Hi6YzhqeBhofV4m-gXS0ZoDesy6X0EzrJxQLA_YD5kUFB0dmrrZWiXe8nsmHTae9PbyD1f4y7baJzjk7aBNIjO8vqvJjWgc3YVFzpxuVh89-iqXP2SUzhjBg9fDUHlVMDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اگه برد تو بازی اول لیگ نخبگان تضمینی برای موفقیت بود که تیم جواد نکونام در فصل آخرش تو استقلال که بازی اول سه هیچ الغرافه رو برد هم ۳ گانه داخلی میزد هم تو آسیا نتیجه میگرفت ولی خب اون سال اخرش هشتم شدید
🔴
اتفاقا جوگیر شدن شون بعد یه برد تو آسیا میتونه به نفع ما باشه و اون اعتماد به نفس کاذبی که بهشون تزریق میشه کار دستشون میده ، حالا خوبه بازی اول بود و هنوز بازی با تیمای اماراتی مثل الوصل و شباب و بقیه مونده حالا که انقدر خوشحالی میکنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/140088" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wAoGiSRXFWrR-lTsogmXlWl3oygo1OnxRIDRbvdiaxNcHHFCyxXSyxEy-NSKQip8jbczqzEwVierJqYRQXa5-5pcPidFn6NT0JydecIP7_3jf7WbMOwuqHexXk95PGBqiEGPzYzLSA4GKL9IVwErkgfQccB6DGVPJ5RcVZVtdtfKsolj7gUMc-xszg9415KOx-GKPF6ddNp5ktwB0-0Fvb0wi9-llX-V7S-1N36SdRyLcE8pRybTsi3QJoG17794-3Vmvoul_WqdYvuiffWYk7lMzEIrvrixk8rFAWBktR3iVjY-TM66oaTvnxe_MkFkMhdnomNu7ssDGRfI2pap6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس با اختلاف بهترین تیم ایران در آسیا طی ۲۰ سال اخیر
❌
علاوه بر دو فینال آسیا و سه نیمه نهایی از نظر مجموع امتیاز هم عملکرد بهتری از بقیه تیم های ایرانی داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140087" target="_blank">📅 00:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140086" target="_blank">📅 00:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140085">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeE7_PGX7dmj0TLwnQ9nxR82dDhflbMC04YYx4A2g87Afh0ZLdnFlpM2z2O-ofwiurTWfx4AEh8CxwM26cqmOLDJGJiW9dBt1wQOILlTY967MtcRSV_KETtQpOjDjEpZRYpEnnvOSLrm3sdpdX1yeVoFapKtRwZtx3kYEn94YMNETwIEI6eXEZFgX0E9J7v8Kla0MzSr-6MX8XdyvKWLuVqftFHwsbti_Qs62DNUkuAO34CCRq_iLId8MkKzrTLbkikG5jCGGncra8lw-T1A6KoB2ebnIxrL7tXJlyCpg0_7pz2j6Dn3bWUeuckbeNsYKHjRqDsTGAhhTzBo9HLB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140085" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140084">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140084" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
السد هم از آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140083" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140082" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140081" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140080" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
باور کنید پیکان هم این تیم السد و میبرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140079" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140078" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140077" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6OysPyRMZWBhkpkabLkq1QaZSJK05FNFmL59K5NU_obzkAuKVklBUUc2x6vtLOycPs7UkROEQIEC282CXHXuC6Ktt5GcslQPVtlOraL0GcjYsPuJ0Hv2zhqaipmStkqaiehTNNGCZ5_vWY4fPk0CxTG2LXW3FwfdNSMZdRefS1pUeuTZ2JJuX34yqfarYK7bCoFq-DzM-ICU7J64wj4MTBPLQYMrGgQKfOiD63ZiJq_YvLQhuoecZEIWRbuYE2b0H9EcFlCkaNmZr6g-x82ahs2g-gppIAifMDA32fuaIbwH4KA5UTjt4EaNHVzeySkRSnmRYaHApxARuQeq_x891G_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6OysPyRMZWBhkpkabLkq1QaZSJK05FNFmL59K5NU_obzkAuKVklBUUc2x6vtLOycPs7UkROEQIEC282CXHXuC6Ktt5GcslQPVtlOraL0GcjYsPuJ0Hv2zhqaipmStkqaiehTNNGCZ5_vWY4fPk0CxTG2LXW3FwfdNSMZdRefS1pUeuTZ2JJuX34yqfarYK7bCoFq-DzM-ICU7J64wj4MTBPLQYMrGgQKfOiD63ZiJq_YvLQhuoecZEIWRbuYE2b0H9EcFlCkaNmZr6g-x82ahs2g-gppIAifMDA32fuaIbwH4KA5UTjt4EaNHVzeySkRSnmRYaHApxARuQeq_x891G_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید دستمزد بیشتر بگیرد؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140076" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140075" target="_blank">📅 23:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140074" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⬅
➡️
⬅
➡️
پرسپولیس در آستانه خرید امتیاز بعثت کرمانشاه و تشکیل «پرسپولیس ب» در لیگ یک قرار گرفته؛ توافقات دو باشگاه خوب پیش رفته و احتمال نهایی شدن این انتقال در روزهای آینده بالاست.
⬅
⬅
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140073" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140072" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
حامد کاویانپور به پرسپولیس بازگشت
🔹
حامد کاویانپور، ستاره سابق پرسپولیس، به عنوان مدیر فنی آکادمی و مسئول بخش استعدادیابی در این باشگاه مشغول به فعالیت شد.
🔹
کاویانپور این سالها مدیر تیم های پایه پیکان بوده که از موفق ترین اکادمی های تهران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140071" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
