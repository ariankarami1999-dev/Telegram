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
<img src="https://cdn4.telesco.pe/file/evxyKxp_Rdk8RQ7MVdv85MZb9QEASaCZxHR7ZcisCvwiTlfRXr068rKazIzXPxCtu4rVH5RI_rOz9uFCiPuFNXBjee-2pyljm6EQnJ_FB-pVWD8vDBLbP7TouIRRAjz1JaRECXyvwl2lsVybPLkCM80QnLGLIur3h6e-ki7fSP0jAbD2kS-F66iajV5tTdylyX7-wqjLmdhYfP2AnXc3ABi7fm2mnNK4QY2eNXZnqnnZ4g5Jbl9kIptPYPjxm0pJuKhRVhIyVmTYEPu7-86F0g8-Bx52V2YzHxO3UatHZgG3zGH5OIAEf7qNWh1iNQHevKI7HcFTQ0aOGUu4hWU6cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-135806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
گل‌های پرسپولیس در دیدار تدارکاتی مقابل شهدای رزکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/SorkhTimes/135806" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
جونم اسپانیا گل دوم هم زد و در آستانه رفتن به فیناله ..فرانسه در آستانه باخت و رفتن به بازی رده بندی ...کیا میگفتن فرانسه اسپانیا رو میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/135805" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
گل اول اسپانیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/135804" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
مرکز مشترک اطلاعات دریایی به رهبری نیروی دریایی آمریکا :  محاصره آمریکا شامل همه کشتی‌ها، بدون توجه به پرچم اون‌ها می‌شه
🔴
🔴
محاصره، کل سواحل ایران رو شامل می‌شه، از جمله بنادر و پایانه‌های نفتی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/135803" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/135801" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/135800" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/135799" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
ساعت 22/30 بازی حساس و دیدنی اسپانیا و فرانسه ...پیش بینی شما چیه ..کی می‌ره فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/135798" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/135797" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=W9L6z3q8aAWLBjpKBzak_zn2uDoI1X0lMtbD1rHWhZTjvPv0SqvwMk5Jx_QlvwNQG4snMtUqOjQXFeotvyZ7dolXpQtskQQfInL2ldGGedy3UwDdTJimCR5ntokc1efP_5-CDDIArIN6EaX36V8N5QrZ5htzoRswUj7g4xTiVSuj0a1LoRHV4QGv6bL8SNT3kM4ywVNgLMOLj3eeUdn07NrB4e1ULPfge4X_xQVqHIMbkr1xkfe3VPo5e7d7hAGKBNneTdKDYIluCkra0IpGofTLaQLHWduC5IFka_RsKe0dfH5mWEJ8CL9wUamUC71JQoDwRNPSRLTIlkjd-BbP2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e06b7b2.mp4?token=W9L6z3q8aAWLBjpKBzak_zn2uDoI1X0lMtbD1rHWhZTjvPv0SqvwMk5Jx_QlvwNQG4snMtUqOjQXFeotvyZ7dolXpQtskQQfInL2ldGGedy3UwDdTJimCR5ntokc1efP_5-CDDIArIN6EaX36V8N5QrZ5htzoRswUj7g4xTiVSuj0a1LoRHV4QGv6bL8SNT3kM4ywVNgLMOLj3eeUdn07NrB4e1ULPfge4X_xQVqHIMbkr1xkfe3VPo5e7d7hAGKBNneTdKDYIluCkra0IpGofTLaQLHWduC5IFka_RsKe0dfH5mWEJ8CL9wUamUC71JQoDwRNPSRLTIlkjd-BbP2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابوالفضل جلالی: وحید امیری خیلی به ما می‌تواند کمک کند
🔻
فعلا در تیم، هم‌پستی‌ام وحید امیری است!
🔻
آقا وحید یک بازیکن حرفه‌ای است و از لحاظ ادب حرف ندارد.
🔻
با وحید امیری، حسین کنعانی‌زادگان و محمد خدابنده‌لو در تیم صمیمی هستم.
🔻
بدن وحید امیری آماده است و او زودتر از ما سر تمرینات می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/135796" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
جااااااااااان کیسه سوزی باشه؟
😂
✅
جلالی : دربی حذفی خیلی اذیت شدیم و گل عالیشاه خیلی قشنگ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135795" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/135794" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
خلیلی :
🔴
دیگر مهاجم جذب نمی‌کنیم و با سرگیف، شهرآبادی و علیپور ادامه خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/135793" target="_blank">📅 21:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/135792" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=HYPv3eYLLOY3_ANQOXXuK7DeNSnSz_CUB43LbGA4PTokKYVpEgfzjzUJ8HRML9_Bph3Sq6XuxNHdVuyu3IUYrdQ2Evc9S7hFiynjfWjhPCwG6zowiTapI7Y1kgi_V5LaI-4Fgd5QlORzQ87owTm4IsTqrgevv1VM5RRlelfiQA10SXY35A9kbx4yzSeCtlYtdzI5RhmFVLggTIUGGJqjCK4rfdVa3eUnwzC7N3MNUU1EamQCgIDOBJCWOEu8yyNMjOyl41UQzS1JcwVfhRxKIg83Xlj18pzhJEVDu3pOlKwRnXtJSrQGvkyE6cr9iP3CJ_1iZdvU1uevbKINM-Q2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4138202b6c.mp4?token=HYPv3eYLLOY3_ANQOXXuK7DeNSnSz_CUB43LbGA4PTokKYVpEgfzjzUJ8HRML9_Bph3Sq6XuxNHdVuyu3IUYrdQ2Evc9S7hFiynjfWjhPCwG6zowiTapI7Y1kgi_V5LaI-4Fgd5QlORzQ87owTm4IsTqrgevv1VM5RRlelfiQA10SXY35A9kbx4yzSeCtlYtdzI5RhmFVLggTIUGGJqjCK4rfdVa3eUnwzC7N3MNUU1EamQCgIDOBJCWOEu8yyNMjOyl41UQzS1JcwVfhRxKIg83Xlj18pzhJEVDu3pOlKwRnXtJSrQGvkyE6cr9iP3CJ_1iZdvU1uevbKINM-Q2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: با قلبم به باشگاه بزرگ پرسپولیس آمدم و این تیم را انتخاب کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/135791" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=OzD-a9PJ9dHyteuzSHoo2ndyJFn2RLopZc6UTMoWFTLPsY97lEeHhJKZNQxqi6fxmVimQUS0Ah25L98O9hDoiksGtz4gun-37l0yMolcgf3mEnh3H96qniTVBFiA6RcBsXRTppot0swrrjnaEXRDIaiOnWyxkey8LbLT2nVTi8Oj_3CDR-SHfI63zJEtmglVz-A9eaejhDfIOGCuWPNjrm7i3w3HaRk4WjnToZkXx7_4-IxBIjk_NgrCjve9-gfT1RHhQLDJrj3reP-67sQYWo6DdKigMpf0zop0-yxAUkcmGigGB5q5lQOTMhRYgt7ffCPg4S3VccwjLaRv9563iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e350a78f3.mp4?token=OzD-a9PJ9dHyteuzSHoo2ndyJFn2RLopZc6UTMoWFTLPsY97lEeHhJKZNQxqi6fxmVimQUS0Ah25L98O9hDoiksGtz4gun-37l0yMolcgf3mEnh3H96qniTVBFiA6RcBsXRTppot0swrrjnaEXRDIaiOnWyxkey8LbLT2nVTi8Oj_3CDR-SHfI63zJEtmglVz-A9eaejhDfIOGCuWPNjrm7i3w3HaRk4WjnToZkXx7_4-IxBIjk_NgrCjve9-gfT1RHhQLDJrj3reP-67sQYWo6DdKigMpf0zop0-yxAUkcmGigGB5q5lQOTMhRYgt7ffCPg4S3VccwjLaRv9563iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوالفضل جلالی بازیکن پرسپولیس: امیدوارم امسال بتوانم دل هواداران پرسپولیس را شاد کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/135790" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46267f8866.mp4?token=GkmJeIgR8CDFTmfijJvHfuqwbViHdR3nBRO0MqxAHf3uxXq6J9MIwERCDfFrCbbhei-DOoholwJm-UH1I8hVT-_8Lv31vdKPzi0YOOsTRJYdSUfAKeJSjGadDeR3havqfedqapOFAak36vnrinjEU5uHnJIliZgmfnYcvPnD59iFLtR-_L9aH6_cGR7DS4oZpj8PlkLxcdC2R-53l_YsTqeA9opti_NRcoAyeFY57R4TN-kTu_GE2fd8IZYZqOu_cfoOCTXe0RPTPw74KZxoTtzagiteoQyplK_Isbm9lSnLyBrrFMvYdedBnc6kxpmSv5grqo_l12k-fRuZNxA7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46267f8866.mp4?token=GkmJeIgR8CDFTmfijJvHfuqwbViHdR3nBRO0MqxAHf3uxXq6J9MIwERCDfFrCbbhei-DOoholwJm-UH1I8hVT-_8Lv31vdKPzi0YOOsTRJYdSUfAKeJSjGadDeR3havqfedqapOFAak36vnrinjEU5uHnJIliZgmfnYcvPnD59iFLtR-_L9aH6_cGR7DS4oZpj8PlkLxcdC2R-53l_YsTqeA9opti_NRcoAyeFY57R4TN-kTu_GE2fd8IZYZqOu_cfoOCTXe0RPTPw74KZxoTtzagiteoQyplK_Isbm9lSnLyBrrFMvYdedBnc6kxpmSv5grqo_l12k-fRuZNxA7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی سرپرست پرسپولیس: برای جذب کسری طاهری باید 200 میلیارد خرج می کردیم که به این نتیجه رسیدیم که قید این بازیکن را بزنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/135789" target="_blank">📅 21:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135788" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/135787" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
خلیلی: ما اصلا کسری طاهری رو نمیخواستیم و از لیست خریدمون خیلی وقته خارج شده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135786" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
محسن خلیلی با کسری طاهری تماس گرفته تا در تمرین امروز پرسپولیس شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135785" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
بیفوما به‌خاطر کشیدگی کشاله هنوز تمرین نمی‌کنه. بعد از اینکه برگرده، تارتار کیفیتش رو بررسی می‌کنه و اگه راضی نباشه، توی لیست فروش قرار می‌گیره.
✍
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/135784" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/135783" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
برگام
😐
🚨
علی نعمتی هنوز با لوسیل امضا نکرده و پرسپولیس زنگ زده بهش تا بره مذاکره حضوری کنن/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/135782" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
به خیر گذشت
🔴
فوری:علی نعمتی راهی قطر شد!
🇶🇦
✅
علی نعمتی، مدافع فولاد، با امضای قراردادی به لوسیل قطر، تیم تازه‌صعودکرده به لیگ ستارگان، پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/135781" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/135780" target="_blank">📅 20:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/135779" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135778" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJrIlS7FWpJlQhT5JiRYC2x0JKnV-n43MwVFW7XNR0GxP1L0Ke-xmrUjzWckWBt4LjFFJJ2KTgurlbm4kPL9WURSWnhxPI5nMICKXxnuVLHranvEnn2D4diwHyTZHS4fxLzkkDQJ0Z5lkpGPs3jEoLnoFB0xNdoc_Md_7m-2w8YDKTn_gAVzQZBv8-_V6ZtF7HsP7LSOATfm6Vu6DeUenqnlvHUbnn3bws1HqcjgJoMRJGnIXuM3JTwFNw4j-uTMULIET4Ownrm_2m_AOWAMdUITfVtmJAYMcioGhyfa7ZLF7eg9bfkRf_tZTNSNHBfC1Un1X3JtdrEljLqNzYFmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135777" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/135776" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJIIUNSo-a3c37w1gaNDfKRZH03PCmY8_HlCtfRXZGZmECwMIbS33KzaOp5U5kwDyw_pbX4QG78slM5zVSOhDJ_cRhXaNlggXExL5FYiMxy5FmzelywswgraLDaHclwrfiCj16G7ZH4od07WzzGFYLih35_d_iz282plhgeVUxpWPW9sniTmtCstUf__MGcLB4qZYV3X3RbIs0bEXWo-gxsiT1tLuPy9zzlYFC2dxioixWQCEFMSbechYw_7yqmO5sggp-EHukEmOsBo1hANFQs6vpSUfPcDqyTWy4yqIFTrdkPyUeIClZcn2yYfQOsj62OtbPCd2YINzK-dHbmRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/135775" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=rOQmOZofMvc5-qSWCdUJBLPZIho6emgtRxuJ0U5gwyar1A1JkBY_nvFhiyhHf945pundJmfuHxHHysxZV1xB3SVYuNXyZuKPB78kH8Apv2DoHcks6hP38heklAHM2NoP1Gx8WNh0Wc0YuTWmoAn_foeSnvGXheMapHf5VjLyghcQ5dNkxXgKl7_wo9Pk6gOl2cmSXP3ybdzUsNEMpvLfAHfUnERZKDjlXItg6KsJ9nAAi5mRd6QK0OLlOAaWLvIk5jH7b0HxuoBcXJW4_gxsixKLHeIyO3q35sdK2SicyCYIEVOznWztFohxf5ccg_thoeJJs_TFyzg8rgpfcmn04ZfZt5MSiHoQFJxNMBJQIpibqFEw0L8o-VRXbKcEu4J_2DFa6Dx88qm_xqeD8ADb9m3FDFLXUm4sUAbrpxGzpfavj3ELmkHyYjcG1KEJKRNU7ejji-jTccFD9-CpuyCmbuUxJh9XPGX6IBbg91fHr3asIu6zVIp_4R7yGKrYNGRrP-rfQC_jcI7YhFjXZLxozisx9IsJatOSn4GrRfO9TDILdJ8XrMi_DZuyygUir6AK2QO9tbrnf0MLyk7VS27egjuHmpHBAz6BIEUi_oHA5Tg32-54PNtOQ5CSEFTeD4vaZudQdmI51BnczACD0_n940ufZT2XkQcKhULKpfbe6h8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb37226cd2.mp4?token=rOQmOZofMvc5-qSWCdUJBLPZIho6emgtRxuJ0U5gwyar1A1JkBY_nvFhiyhHf945pundJmfuHxHHysxZV1xB3SVYuNXyZuKPB78kH8Apv2DoHcks6hP38heklAHM2NoP1Gx8WNh0Wc0YuTWmoAn_foeSnvGXheMapHf5VjLyghcQ5dNkxXgKl7_wo9Pk6gOl2cmSXP3ybdzUsNEMpvLfAHfUnERZKDjlXItg6KsJ9nAAi5mRd6QK0OLlOAaWLvIk5jH7b0HxuoBcXJW4_gxsixKLHeIyO3q35sdK2SicyCYIEVOznWztFohxf5ccg_thoeJJs_TFyzg8rgpfcmn04ZfZt5MSiHoQFJxNMBJQIpibqFEw0L8o-VRXbKcEu4J_2DFa6Dx88qm_xqeD8ADb9m3FDFLXUm4sUAbrpxGzpfavj3ELmkHyYjcG1KEJKRNU7ejji-jTccFD9-CpuyCmbuUxJh9XPGX6IBbg91fHr3asIu6zVIp_4R7yGKrYNGRrP-rfQC_jcI7YhFjXZLxozisx9IsJatOSn4GrRfO9TDILdJ8XrMi_DZuyygUir6AK2QO9tbrnf0MLyk7VS27egjuHmpHBAz6BIEUi_oHA5Tg32-54PNtOQ5CSEFTeD4vaZudQdmI51BnczACD0_n940ufZT2XkQcKhULKpfbe6h8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شهاب زندی: برای فروش ایری قرار است هیات مدیره تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/135773" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135772" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/135771" target="_blank">📅 18:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW_Cg1X5DQre0HUr7ZKpThW_wdJeQxa71IohLpba6vkYqXKESHUkrmqU5G4XTPxiUolSctILjsdAj1ANjkpFB_7rQ7NVX-WtnW_RhgWRVnFMph6yiY6FvF6dlaX8hAyAqJMmymVzhnSvhI_wVYBYecVh8o53w91V9vF97oP0G2gBWDGsxQcO5x9FYVHL1nuhFE5hXmC1puc-8likTYzLESxQ-B93TAxnrxZURryaB9b2SKxE_zp1cM-511fy21L06qDcs_6p8EE-9LL1kW0sZUlmt_azK8wIUYzX-Qw0ezdS__VZD_tjsPNHtnUJk4EBlQuSPGUSiFXqusolAbXRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از خبرورزشی
📊
📊
📊
علیرضا جهانبخش کاپیتان تیم ملی فوتبال، بمب نقل و انتقالات مدیران پرسپولیس و بانک شهر برای هواداران این تیم است!
⚽
⚽
⚽
⚽
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135770" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=vGIaoMEv3N_O6r4ypuEkiz4U3jusDUDJJDX-SV9cjpzOjxY6HQhTwgnm8G-Ed69cG58tPwDV5XOFWBWWzydqpxgYkhdDHrPwzkvMrpB5BbckTEYx9jIrDHIkPhmsPJ5I2-B2097JzaSJvvZytwdXdQNhwTFL9QJ_cFdSMulnhnxYtHk-uMPA5N-HfVZriZWnAT6yELXwvpbYxls2VEuAmNsrZckWqRfdy5lhmSK0zxA19JDmpEvP9j6XUkzNiFzon66izEMXspkgk7sHeNoQ2_qat33ybhowfEFGvUaMnMOJR58vXHbiCsOVkTyAnqDJNArSLPlULp92nr0agxVstA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de17a51b64.mp4?token=vGIaoMEv3N_O6r4ypuEkiz4U3jusDUDJJDX-SV9cjpzOjxY6HQhTwgnm8G-Ed69cG58tPwDV5XOFWBWWzydqpxgYkhdDHrPwzkvMrpB5BbckTEYx9jIrDHIkPhmsPJ5I2-B2097JzaSJvvZytwdXdQNhwTFL9QJ_cFdSMulnhnxYtHk-uMPA5N-HfVZriZWnAT6yELXwvpbYxls2VEuAmNsrZckWqRfdy5lhmSK0zxA19JDmpEvP9j6XUkzNiFzon66izEMXspkgk7sHeNoQ2_qat33ybhowfEFGvUaMnMOJR58vXHbiCsOVkTyAnqDJNArSLPlULp92nr0agxVstA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بیژن طاهری، سرپرست کیسه، بعد اینکه یاسر آسانی به فرودگاه رفته و ایران رو ترک کرده، رفته راننده رو مثل سگ کتک زده و گفته چرا بدون هماهنگی باشگاه بازیکن رو بردی فرودگاه!
😳
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135769" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
شایعات؛ جهانبخش عصر امروز با مدیرای پرسپولیس جلسه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/135768" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135767" target="_blank">📅 16:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
فووووووووووووری
✅
قرارداد برای میلاد محمدی ارسال شده و تا ساعات آینده ممکنه اعلام بشه/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135766" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=rcxD0XHnb6xw-9t2QFoRfKXXKz4evj_SIaPRDpcZWq-b0AN6_FZyoWoOLoP6fNQOss98KhzvdiRb9AFyJsfg79YvhoQwFPHrZtDRKTxX32PR6zZhER47MdiboFSiXt8al6CSfhzxjCB0bF_K2JBLuzv0yM_TuClUNUF20I24F2lSRlEeU5YpvtItW7drn4XiYH2wqNHzO6DYsF7_suLF23QUdlreTZHuPY2YBIRo5iC5ooDRqMrTJdxTdrqfeQKXgWNyy8Iy07WktDyl0VKZ60uVp9Glz90cq7QzVYNtOKXV_ADr1z_c9h_vb1n7NeOzLyD4a7rcxS2kyUsvhyIkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b882d31c48.mp4?token=rcxD0XHnb6xw-9t2QFoRfKXXKz4evj_SIaPRDpcZWq-b0AN6_FZyoWoOLoP6fNQOss98KhzvdiRb9AFyJsfg79YvhoQwFPHrZtDRKTxX32PR6zZhER47MdiboFSiXt8al6CSfhzxjCB0bF_K2JBLuzv0yM_TuClUNUF20I24F2lSRlEeU5YpvtItW7drn4XiYH2wqNHzO6DYsF7_suLF23QUdlreTZHuPY2YBIRo5iC5ooDRqMrTJdxTdrqfeQKXgWNyy8Iy07WktDyl0VKZ60uVp9Glz90cq7QzVYNtOKXV_ADr1z_c9h_vb1n7NeOzLyD4a7rcxS2kyUsvhyIkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
این چیه برا نیمه نهایی ساختین آخه ناموسا
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135765" target="_blank">📅 16:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
#منهای‌پرسپولیس
🔹
سینا اسدبیگی و محمدرضا سلیمانی با عقد قراردادی یکساله به دهوک عراق پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135764" target="_blank">📅 16:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtGCR-HCoPnhmOAk7x2OGnd42rEvlbIYAcJ7HbgIZZ8HDqZZ663nQhYwu92k56ehrIXdiEjxfNIHnJd-yMSG_VbudQNXMWaYTDHjk-haYbtgZmSLKj8kNzbUQ8xURgYA0dsjQba_GSymo9qUgMAJVhxL9sg7PhHeFB27GL2dsQXX-mXy4UqIm4a_xkcdHWY3Nd7yIEY1jFWuyWrsbsklvQ3vghBrhD4ltL43DBqzIzoC2oTiv7XPuDEdzzzY_gmgnOcS0Mjz0XHYGnl4ReOq5y5AiuZhcl2PaMUwcKSG50rz9jHgB-fM6XC2F2NfEuwYdpbSvY9N2do2ZDuCWTr8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیروز تو بازی دوستانه امیررضا رفیعی بازی نکرده و گندمی جوون نیمه دوم به میدون رفته
🔴
به نظر جدایی رفیعی قطعی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135763" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135762" target="_blank">📅 16:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان حدادی به عنوان مدیرعامل باشگاه پرسپولیس معرفی گردید؛ از سوی باشگاه به عنوان رئیس هیات مدیره سرخ‌پوشان معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135761" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFSQowpPns9UbWHJ4GoA-jZ3NN5yLyXcBUoiQPdw1RenlXsMEAnbknd3KiFdSygxDpt9Tl5XAtq0Mh8f4J5dMYnDq1HSSOQu_W2kW4kJJQ-oIiy4qotcI18p9QB-f1FK3yx7TZYaVB9fjc17E0DH-OSlDkmhpGVJns8wOgnnNWi5GXRe1HUrFWe4EdzRmSjxNiIEgH39cxkDuOfsNIp1-wV2X6m7HIY_1E6M34pMdtHPXS8TxBdGiahTAuUUbcKu0NRNuT4FtxJNQg4FYPkX0IWiRwC6EM-8SnOiEzX1mXsdCfO8eVpbz8CxegHSENclt4ehxO2FDKp4Oo5a8ECRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
❤️
فوووووووری
پرسپولیس دارک تا دقایقی دیگه از ستاره استقلال که خواهان حضور در پرسپولیسه رونمایی میکنه
🔹
👇
🔹
@PersDark
🔹
🔹
@PersDark
🔹</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135760" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
تسنیم : رضا جباری با مسئولان باشگاه پرسپولیس جلسه داشته که ؛دو طرف در این جلسه به توافق نهایی دست یافته‌اند و گفته می‌شود جباری به زودی در تمرینات پرسپولیس حضور پیدا می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135759" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
🎙
علیرضا جهانبخش: می‌دونم که بین پرسپولیس و استقلال لباس کدوم تیم رو می‌پوشم اما الان نمیگم. پدر و مادرم طرفدار یه تیم هستن و هرجا اونا بگن، میرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135758" target="_blank">📅 15:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
فوری :پرسپولیس برای جذب رضا غندی پور اقدام کرد /خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135757" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apT5qsoOy4gr_sX7_O8EacTXci1owKy9wXxz3oEz9bTTtrjrgeRSsHRHqYWRMgeFlpU7Pv7L0YpVZBmVnSSuhv9HF4trVXr0pMQilJzsBHqp5pB_VZT9SxesPduWppEOGK3kLRyONzmRkCErIf_4QvFvNX8n4wNVaJlBXQySz1NGntC1CtCtE16ZgQqrq_Xk22iO3h-ynwnhOlZNGJrDHTUDxDbp1NukkQ3Z1rsDKCwmL94cvQtzxjXnLpuxXTnNLHVHpG3bTnAD2C78MzUDpPU5mCxA2n958H57qXiiJzqf57YSqhKcv4up85Zeia3R-29JadzuKCVB1fPAHUCJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه فدراسیون از رفتار قلعه‌نویی حسابی شاکی شده و قصد داره این مربی رو برکنار کنه مگر اینکه تاج مانع بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135756" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🚨
قرارداد میلاد محمدی با پرسپولیس تمدید شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135755" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
ورزش سه :
🔴
بالاخره پرسپولیس و میلاد محمدی  روی برخی نقاط به اشتراک رسیده‌اند و به این ترتیب احتمال دارد در روزها و حتی شاید ساعات آینده قرارداد مدافع چپ ملی‌پوش پرسپولیس تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135754" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
تاخیر ۷ تا ۱۰ روزه لیگ ۲۶؛ فصل جدید فوتبال اواخر مرداد شروع می‌شود
🔴
🔴
براساس اعلام سازمان لیگ، در شرایطی که قرار بود فصل جدید لیگ برتر فوتبال از ۱۶ مرداد شروع شود، این مسابقات با تأخیر  یک هفته‌ تا ۱۰ روزه از ۲۶ یا ۲۷ مرداد شروع می‌شود. گفته می‌شود علت…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135753" target="_blank">📅 14:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABn5QB3yEjNAHnyH-naPMxfnYreMldNLoOJ_M-9EL8oHLNhj8a9e6JvQTh4nla3b4aJwxLxtkp4XburK4MFKihTE8diZ_9iYiobBzJQqRGPgsnaGZ4lLu5g_yMdEGas7-eGfNmmiZWfsU3S2914U35PO4P_dYChp6n3A0ie2PREc8H9M28-7NWBv4fUF5oIBVFRx31MILIGVoiaJfj1udUiHWct9ZtFEzN7APAY1ke9aH8HxK5WQTK2VOvVsdN3py17cmKN3bS9PMqhIMX-wJcLuos7eGXTLhGhi2kWLi6pWli7fHHUVHGMLbLG88lQ9gytM-YocOogum2TIBhMS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135752" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
میلاد محمدی نتونست تیمی از اروپا پیدا کنه و احتمال زیاد تمدید میکنه / طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135751" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🟡
علی کریمی با عقد قراردادی رسمی به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135750" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
فوری؛ با اعلام سازمان لیگ، برگزاری لیگ برتر در اواسط مردادماه لغو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135749" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
کسری طاهری مهاجم جدید نساجی: من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135748" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135747" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
💢
احتمالا علیرضا جهانبخش جانشین امید عالیشاه در پرسپولیس می شود!
🚨
جهانبخش جدا از عنوان یک بازیکن برای پرسپولیس قرار است سفیر تبلیغاتی بانک شهر هم باشه و پول خیلی خوبی قراره بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135746" target="_blank">📅 12:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135745" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVe5XVf9jad7R-uzg85sAq-xmXxZ-h30en5m38h7luQwcG4ueUDZ0EjLRu-CupOop67cefaFl1rdZhaOADD-DYR5-4ktvTnW1LaoORX3V6oggxXlBR0VoAo6ox0rYYCgvJG98BlFhaCZ3V0uPMt1FYvBWzQXPibGtPDqXPey2yFyDw33EDuKxE-y64sWEBsOW3Fxo4V9qZBJUKYJxEiQNBnP06Q6HH1UFeew6xs29bhHdi7YpD2VD4XZGSmp-IFqDvmVSUmi5PHgITbLLZNMzvH29FUklJdncM6vLWdW903wbig6TaWRVzmURt1CVFWwWRUQpvyeS7Ct4XQNs65rBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135744" target="_blank">📅 12:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
جذب ایری برای پرسپولیس در یک صورت ممکنه که نساجی بدون دریافت یک ریال این بازیکن و به پرسپولیس قرض بده که احتمالش صفره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135743" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=GD6LGlHjw-59i66rPGwSpRsuLeKc-vZk-VXKRG5sjhCQXaaQ9rh5RetovZFN9yPDsmgEdDHLC4L_kafqPY1bhmhYIvelXMlbWXuPgEUbdTyCvxMahY_4p4xVDZGww2k7QdjjqBknLcqAPbB5-PgyXxrG4QisiLkqjMK8U6m-c3_HM_vOayQIUwB3WA4523gCcZoJdg23-PxG-7CI_NkGWCRULeEs47nytIVI2MrLX0I0BkMRHlx0NR6p04n8yEg3vH94wxFkrCsBKfFFkzcnXI_SMPRDVi-owun0lfmXnAGDiztxPAVxbqikDJk621FUHLU4ha8nvw7oxDUKBPvLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=GD6LGlHjw-59i66rPGwSpRsuLeKc-vZk-VXKRG5sjhCQXaaQ9rh5RetovZFN9yPDsmgEdDHLC4L_kafqPY1bhmhYIvelXMlbWXuPgEUbdTyCvxMahY_4p4xVDZGww2k7QdjjqBknLcqAPbB5-PgyXxrG4QisiLkqjMK8U6m-c3_HM_vOayQIUwB3WA4523gCcZoJdg23-PxG-7CI_NkGWCRULeEs47nytIVI2MrLX0I0BkMRHlx0NR6p04n8yEg3vH94wxFkrCsBKfFFkzcnXI_SMPRDVi-owun0lfmXnAGDiztxPAVxbqikDJk621FUHLU4ha8nvw7oxDUKBPvLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برای طارمی چیکار کردی ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135742" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135741" target="_blank">📅 12:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135740" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGqlOV3gmDFXNdpZMt8GxAxOuM_WLxzql4QAm4J53UiFI-cFBrbVVx8PE2T7SkDi4aMcPevudR4oArUphXezZ2ALGqqrlnVsAI9_Ykyr88UoemMAUYXlLc-FtpHob0ekygU2Ia0zrzgSSjNkXJQaWCBki4AqrCZH8kdMi6sO7gHWuCkZNCi75iO0ZYq_83ZBqExh-TnpyoOhv5ou43cXGpPZ3eNI8snP5usN6dIKZpDlanaHJn8g-HHVP0iGe0k6nIeub_r4Ayfw_D76ZZX8gvXrVXTGQwVhfFeU7Iro8wfxUOEyq9ZLzlzLzPEEYgez4RfazXnxD1A_biMrahTOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135739" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135738" target="_blank">📅 11:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=tLDaY06hcvAlUv8ZHPMIH9XDbvgKR-ftmIjImnuJ73zvyc_Yf6fptR_v9r0P9sJ3d75fkfupRI357jlptshz__3o3juMOPtt7yPUM38EcfuAheEoyJaa7ttE02hpHC8WL_bqDmrOnBbh4zN7YtvdQajJjQ_YRwy7aMLeU86DdURiWKAgQvlxCMQYDa8FOwIAQp8K5-BrBJnp9CCSsGOStXcfr6N7v4zGydqW-Pr_LvuW8NsovUWmax16wsZyKDGk423kE5lAZ_VSsEJMZO52ubiwbxjcglK9l6ta9t0kJePQjCjdCJUcyMRaPzX4bkkvGb_Es7coTJoMkxT9ROzy5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=tLDaY06hcvAlUv8ZHPMIH9XDbvgKR-ftmIjImnuJ73zvyc_Yf6fptR_v9r0P9sJ3d75fkfupRI357jlptshz__3o3juMOPtt7yPUM38EcfuAheEoyJaa7ttE02hpHC8WL_bqDmrOnBbh4zN7YtvdQajJjQ_YRwy7aMLeU86DdURiWKAgQvlxCMQYDa8FOwIAQp8K5-BrBJnp9CCSsGOStXcfr6N7v4zGydqW-Pr_LvuW8NsovUWmax16wsZyKDGk423kE5lAZ_VSsEJMZO52ubiwbxjcglK9l6ta9t0kJePQjCjdCJUcyMRaPzX4bkkvGb_Es7coTJoMkxT9ROzy5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135737" target="_blank">📅 10:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135736" target="_blank">📅 10:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
استوری جدید فرشید حقیری در مورد احمد نور: قراره شده احمد خودش بره رضایت نامه بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135735" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=m6O8MhurF5sLYgAbls11rOOPUUSYVit-nFX8AZDqMLZLGHujGmlPA91st6zfhj_sPWolYCWHWHf3mzAM90rVGGa-gzdcCweTLQ065nyMs5zAjCJwUEmfFI9RQ3_V_kshhX3M9r_RMGSSNswo_xy5P8UsemTkyjZXKBtwdEM1Ystw3ew5zdk7sqH7c5hLyeaE-U3XPFvJW7SPT_zGpEoMnD5PfiooAIVFo1_ek2zFOs8hAldNzKvq9NPMWPNWh3ZmIa3X2WbOSot1goo_tr_HthVTLqolfMt2Ce0YVk1pSI8L_xcyCAOOQPxwFni4HlqyWghDsf6YDAfYoA4soInfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=m6O8MhurF5sLYgAbls11rOOPUUSYVit-nFX8AZDqMLZLGHujGmlPA91st6zfhj_sPWolYCWHWHf3mzAM90rVGGa-gzdcCweTLQ065nyMs5zAjCJwUEmfFI9RQ3_V_kshhX3M9r_RMGSSNswo_xy5P8UsemTkyjZXKBtwdEM1Ystw3ew5zdk7sqH7c5hLyeaE-U3XPFvJW7SPT_zGpEoMnD5PfiooAIVFo1_ek2zFOs8hAldNzKvq9NPMWPNWh3ZmIa3X2WbOSot1goo_tr_HthVTLqolfMt2Ce0YVk1pSI8L_xcyCAOOQPxwFni4HlqyWghDsf6YDAfYoA4soInfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135734" target="_blank">📅 10:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135733" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135732" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
جهانبخش :با تیم های پرطرفدار تهرانی صحبت کردم و شاید امسال برگردم ایران ...دارم فکر میکنم ..نمیگم کدوم تیمه .....ولی احتمالش زیاده بیام ایران چون می‌خوام بازی کنم   پ.ن یعنی میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135731" target="_blank">📅 09:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-9YZyI9Pyj_Pq4e2e3g4I5JKqPYg9nOvnbEPfa-fr4H2Lw9JddiXYS7kEKZxicR1NuUHXgi3_UJ3DCS6AYocMhJ0KeUbJbZPqH1EqpxkJMveg7X8Gz0ATn7WP9ez4H6jT1N5pVIwQrRDKfy61FXLeVzSUevDdgB9DkCbU-6XuqpixX6NM2jvs9sp8mMZMlFkeduU1BwLbsUCWU_KooHLktdEbZ0Y3mk-v0GLcoDr6YCOw-NSatxvmovEgX-fX690vM5vCiT_NzaKBKhCpEZk6dpcu5U1AjYROnxKHjVrUioHGl-cxrh5Xv60_XPqfEDUsIi6ILDaV5mZAJpBmmRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135730" target="_blank">📅 08:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
ظرفیت باقی‌مانده: فقط ۴۷ نفر!
فرم میکس ضریب بالای بازی‌های امشب جام جهانی بالاخره آپلود شد. روی پیام ریپلای‌شده بزن، عضو شو و فرم رو دانلود کن تا بازی‌ها شروع نشدن
👇
👇
https://t.me/+ThBeycRt0x1lZWU0</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135729" target="_blank">📅 02:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs7ZfHRGLyd-QLBqW_v_UgRtY3jlgWPSw5AJQc0F0tDtgllbC7RKnLVc2L9XRbCCjdBVVi5-nCRnMr8jPf7UQUAU87oDMI5FfiAeIVjgTR2X1As5pnf6lw65C1vcL0fEiZTSwINrxR1t2rWj63MNFG8FYxpMe7iaW-iSLd2dG9GbHAjWdr3myJKgI9VDdouB3S4zAeRWAKCfXfUo89x1fTM_uvgTuZVmF206Ftrx6r2ruy6Bg5M3RTkoYryMH6Xi8jEpxMWGtrEl6jaeQRw02_KDJ0js2rf03eWFR4fss8CnWS3Jqcncfz7cw3vC_m3kcF_7CCV_qWDvZ0cq5yM74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ رو به کیف پولت وصل کن!
💸
دلت می‌خواد بازی‌های جام جهانی رو تماشا کنی و هم‌زمان ازش درآمد داشته باشی؟
دیگه نیازی نیست شانسی شرط‌بندی کنی و سرمایه‌ات رو هدر بدی!
توی کانال ما هر روز:
✅
آنالیز دقیق و کاملاً رایگان تک‌تک بازی‌های جام جهانی
✅
معرفی گزینه‌های امن (تعداد گل‌ها، کرنرها و کارت‌ها) با ریسک پایین
✅
فرم‌های میکس پیشنهادی با ضرایب جذاب
📊
میانگین وین‌ریت (نرخ برد) ما در ماه گذشته: بالای ۸۲٪
فرم بازی‌های امشب آماده شده و به صورت رایگان توی کانال قرار گرفت. روی لینک زیر بزن و فرم امشب رو بردار
👇
👇
🔗
https://t.me/+ThBeycRt0x1lZWU0</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135728" target="_blank">📅 02:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135727" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135726" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135725">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
خبری تکان‌دهنده برای همه باشگاه‌های جهان؛ علیرضا جهانبخش بازیکن آزاد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/SorkhTimes/135725" target="_blank">📅 00:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135724">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
دنیل گرا و ایگور سرگیف دو بازیکن خارجی پرسپولیس به تمرینات این تیم برگشتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/135724" target="_blank">📅 00:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135723">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
🚨
🇺🇸
مجری: به نظرت وقت این رسیده که مردم ایران دوباره بیان بیرون؟
❌
ترامپ: نه! اونا اسلحه ندارن و هر چقدرم بیان بیرون باز کشته میشن، رژیم بالای ساختمون ها تک تیرانداز می‌ذاره و با اسلحه مردم رو به قتل می‌رسونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/135723" target="_blank">📅 00:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135722">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
☹️
ترامپ:امشب، تأسیسات هسته‌ای ایران را در کوه "فأس" (کرکس) نابود خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135722" target="_blank">📅 00:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
☹️
ترامپ: عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135721" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اوستون اورونوف چهارشنبه‌ وارد ایران خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135720" target="_blank">📅 00:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135719" target="_blank">📅 23:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
فوری / نیویورک تایمز با استناد به نامه‌ای که بررسی کرده است: ترامپ رسماً کنگره را از شروع مجدد جنگ در ایران مطلع کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135718" target="_blank">📅 23:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135717" target="_blank">📅 23:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq-P0T5sgGOUxib0xOjgngwRXb4oO6OTF4ajNVJHJy6WIM-GoG9QTfrv0b-CljTkGleN0xHEucMVyHWDXoxEPY2C7wZDtsih3g_kojRaNX97zYmyWVKQ7ZsSCW1S28b_9ZIsdul_7VNbiWKErq6CUv1LdftQF2V-8WKK1tGnI4PAWKRJrMwpjDNOaER6f35bPkBkzLomlk-89pOq_STGPp5htbNXEf7K_i3CfRxBwJ-Zj1JG0lT7CQFqjxWfJaexWXQ_s12ysah3ZYDWZmAne7jgd02TUbP7rTPqYAWrUBIx5m3CJnxejian72K0vVoRDXMhD7Aimr0P3GbVwMGSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135716" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135715" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
🔴
🔴
میساکی: اسکوچیچ سرمربی فصل بعد پرسپولیس است
🔴
قرارداد اسکوچیچ با پرسپولیس ۲ ساله است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135714" target="_blank">📅 23:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
باشگاه پرسپولیس با تصمیم مهدی تارتار به دنبال خرید مهدی ترابی است. اگرچه ترانسفر مارکت این بازیکن را آزاد و بدون قرارداد اعلام کرده اما باشگاه تراکتور با اطمینان اعلام می‌کند که او قرارداد طولانی مدتی با این باشگاه دارد.
✍
ورزش سه
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135713" target="_blank">📅 23:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135712" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6uqDTH33ylxyFeprerydwif7dj_s2oxkeuV516MVkb0HunyYWR85gX1CplhxD__-7pDqIeRcnmmkYHNASUIIJlM742YLo815fztDRdzbDp1dazvKVVvgNWkfuVuyCxGQNUDLrMuuKfLae_m4XZSh9VQ3j0nuijCGZNGGUhHof_ZvmNom54VPg9rLjL-TS5aTVfKQGOa34Q_fQTA46-81qVTJ3Ry2iZwNOEds5-Wxad-8QLc3iwwv-2w2kM6t3qw0AcXvtWTHoIaJ1t2rb5pVvKfG8lKec23RsFBqTKez53MGkqoAEq-2zuo8jTKTxUGoUJcxNxQKUa1FpOhqCCaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135711" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
احتمالأ پوریا پورعلی امشب رونمایی میشه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135710" target="_blank">📅 22:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135709" target="_blank">📅 21:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135708" target="_blank">📅 21:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135707" target="_blank">📅 21:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135706">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
فوری ترامپ:
❌
امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135706" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135705">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
علی علیپور و میلاد محمدی امروز هم برای تمدید قرارداد خبری به باشگاه پرسپولیس ندادن. پیمان حدادی دیشب گفت که این دو بازیکن فقط تا امروز وقت دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135705" target="_blank">📅 21:27 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
