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
<img src="https://cdn4.telesco.pe/file/aUDxuNq4EGBwIAirNS-CCpdZScajWlRR6nuT2a34AQnQ0N4SPbmJ1WVbVyXLpYYq6qPx-zHBbGAejeepd2az8uz-lyQ9XCApneZDzVsFWdXT6Ck3r1MKNQfSrF572CTKPtHZ16MuzMgj6WVbIfkCZwSQQPPXteCmqmhq-pbmhHCYk_bTnkQS2Dg1XgY38uw5IJaD8040ytKPaBInqY2btE2Mw8_1GMuQzexc3Hvx1rWSkpZfpOmw_Ef5ar16_bSxOGfEj2vT4xrKFZF6kbWXMNbGcIOh436auEZzdxYndwKyVG9W3wz7xdeMCZeJlxN57xyhd59_6xA5UFCv7KeycA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EU87ErMB0X_jXMCoW_oblEGmYXVu-51ZZ4kS5tshza6w2BLxGnF1_rLzV9Bsc0Vb1U07-nyvyNzEP2LX_OXifk-vBfSr8BZL6zNK8pfj596iOUckwyeaqr6zACJqAORlZDTfbX4vfcUL82p0_YnxwnCzRzh_lbGjdSrFn_puCAhwTGDin1ZSQa-mPOV8jskZhdcsdI57vAhJss6CXBTl8OWdWDveZNmvbGPCgiReNYrcH8U2mey9mfNALyd3VIlxcDMCNyfiW6C0NU5y22v7-t5iHpw1mt0EGUgYHCGKFB0VpQ0A80KjKli9nUIa2hfaF-R_R0_-r64l5GkKChnGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4FJIGGAjyP6Uu_L7d5-43AJT7Ky9kzkj_XNouSjXl2xAc_5vs8hpZUfZtr48cCNKrWS-pHae3GfAMa3_lTEqxhNDxM0XNkRrQ0xzmR20eCWgwdweNhVAvFqxvJ16zLjzlVJOpWpXlhhepdsEMzQWqySSGHrtJY8qyKB9dubnVRqBhl2Ckfu2T5vEqpaMGOaMmwAoxkTURC3rp9Ojtogo9Iw8Kmpd73Z18TTVZNgQYqcmFbAmaklHZw_Sq2wmXlPoa6V04BmAORQrUroB1gQK1XTr-4IxVBt0q3OLgPsW8Av_SBQv5iGQpW1f-NhG6lttKgqtgaww-qVKx7Hiy10JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAnbvwry5uLpeKfqmtsVpwazs-S78kQjOjX7wjQVTL7vSWGkwC8cX3NVxDlEUyeG2auaj3JDBtUdbDaH6NJWLEZ4tOPTVbwYVrnDZ6otL_su467xeoebtRoheAwA_0G_nKeNllvlko58bcRcGTQ0LU95GpqKr7q8TmD5fegmzCTt2U86N3ul_ZRTx44OMO6KDOTisy0522p3RwcCrUOonN5fY_x0FTJEXWjipARPQlq18-J0b7isoPcSrOw1M83jcsMsaNkvy6d2BMDYT6Mmw0aTcEBe9dWWo7dH-Csec6bREV8PZ9jEguJLoki9Ycp8xll8d361v6_FshgMp3cnMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=PRzLMxMfC0TmDN1thswtj2G277Pg_Xs3Dht43msxyUU2XlsTTPZ-hmEb3rcjkOOqp1q-jxsYsybXkNF_rX6uSrDJkcNKIYBtVdUNGzlWzpEVpTeEQQZWVv4PAWSrVdqlNNCw_KXH9mTYflUwYEs3iD9gyt3LzsF_TgYjKLS0zi3r1z4SU6LuiQtPWcLdkO2T0z1JzBBLwOZOq9BdSLzNudlAQsGiScZleRUgVDJFDtlQdu6Q3LCQeN-RYcM7VS2-uHJEBfD8Pecd9nMLihveE2XWLTWkv_CTRQBq_V1r0wZ74xuMCy84NVkP5CTCOoyLkDB5kWNa_o5XaCMvh7YW6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=PRzLMxMfC0TmDN1thswtj2G277Pg_Xs3Dht43msxyUU2XlsTTPZ-hmEb3rcjkOOqp1q-jxsYsybXkNF_rX6uSrDJkcNKIYBtVdUNGzlWzpEVpTeEQQZWVv4PAWSrVdqlNNCw_KXH9mTYflUwYEs3iD9gyt3LzsF_TgYjKLS0zi3r1z4SU6LuiQtPWcLdkO2T0z1JzBBLwOZOq9BdSLzNudlAQsGiScZleRUgVDJFDtlQdu6Q3LCQeN-RYcM7VS2-uHJEBfD8Pecd9nMLihveE2XWLTWkv_CTRQBq_V1r0wZ74xuMCy84NVkP5CTCOoyLkDB5kWNa_o5XaCMvh7YW6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
Arrow 2؛ قدرتمندترین مولد تصاویر وکتور!
🎨
‏مدل
Arrow 2
اومده که کار طراحان و تصویرسازها رو خیلی راحت می‌کنه و ساخت وکتور رو به شدت سرعت میده.
‏
🤔
کاربرد متنوع:
ساخت انواع آیکون، لوگو و اتودهای گرافیکی با دقت بالا
🎯
‏
🤔
خروجی حرفه‌ای:
تبدیل پرامپت‌ها به طرح‌های برداری تمیز و قابل ویرایش
📐
‏
🤔
تست رایگان:
دسترسی به دو هفته
trial
برای شروع کار با ابزار
⏳
‏این ابزار خوراک بچه‌های طراح و گیک‌های گرافیکه
🔗
لینک دسترسی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBgVrhjuVGG5ORDuWaXCnHBWn2CAJwFgQyAUMnyYMpEwGQ8jFzMhcf7Ny1sIJEEzUxohzs1C3Cgek91y9b__oQ-gjdvswFzKw1GuzjxRW8PtDAIkRr1UrtAedM7ICAWezoDrHmDPOhjW-4ULQDNg91kGag__Iogwxi1bCqEBOVwDugYD8Dp1FcJodjfuxU_ukfJFOGloFbl93peIu300afw64q284pmLbR_VfsP5GYyA2f0Y3_DwMAUNTtMmpAu6uu_qyyv8BhEsA3KxROLNj2CV2oubf11zCpPKRYIkLmiOm0Hj9OXIQL4qB-iA6yz-VZxggLDANsqZBqtP15XKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏
Union Alpha
امروز روی
OpenRouter
و
OpenCode
در دسترس قرار گرفت
✨
‏
چیزایی که داره:
‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)
‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام هم می‌فهمه)
‏
✅
Tool calling و structured output
‏
✅
بهینه‌شده برای کارهای agentic و کدنویسی خودکار
‏
✅
داده‌هات برای آموزش مدل استفاده نمی‌شه
‏فعلاً کاملاً رایگانه
🆓
‏
🔗
لینک مستقیم:
‏
https://openrouter.ai/stealth/union-alpha
نظراتتون رو بگید
👇
🔹
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">😎
یک میلیارد توکن Muse 1.3 به صورت رایگان
به کاربران جدید، تا یک میلیارد توکن در Muse 1.3 ارائه می‌شود.
(این توکن‌ها از طریق API ارائه نمی‌شوند، بلکه از طریق وب‌سایت توزیع می‌شوند.)
اینجا
ثبت‌نام کنید (از VPN آمریکا استفاده کنید)
بعد از ثبت‌نام، در تنظیمات، کد تخفیف زیر را وارد کنید:
LYA0IL
+ در opencode، این مدل به صورت رایگان ارائه می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
بدون یک خط کدنویسی، برنامه‌نویس شو
😱
(جادوی Vibe Coding)
دیگه لازم نیست ماه‌ها وقت بذارید کدنویسی یاد بگیرید.
الان فقط کافیه با زبون آدمیزاد (فارسی یا انگلیسی) به هوش مصنوعی دستور بدید تا براتون برنامه بسازه! به این کار میگن
Vibe Coding
(برنامه‌نویسایی که میگن الکیه کیفیت خوبی نمیده، حتی اونام از این استفاده میکنن
😂
)
برای اینکه مثل یک حرفه‌ای خفن‌ترین پروژه‌ها رو بالا بیارید، این ۴ قدم رو پیش برید (پست رو سیو کنید که به کارتون میاد):
۱. اول نقشه بکش (Deep Research)
همون اول نگید "فلان اپلیکیشن رو بساز". اول بهش بگید:
💬
"ایده‌م فلان چیزه. بهترین روش پیاده‌سازیش چیه؟ چالش‌هاش چیه؟ برام یه دیپ‌ریسرچ (Deep Research) انجام بده."
۲. گیرِ تله‌ی پایتون نیفت!
🪤
هوش مصنوعی عاشق پایتونه، ولی همیشه بهترین و بهینه‌ترین گزینه نیست! بهش بگید:
💬
"سبک‌ترین و بهترین زبان برای این پروژه چیه که اجرای اون دردسر نداشته باشه؟"
(مثلاً خیلی وقتا یه فایل HTML ساده که تو مرورگر باز میشه، کارتون رو راه میندازه).
۳. لقمه‌لقمه پیش برو (توسعه ماژولار)
🧩
بهش نگید "یه فروشگاه برام بساز" چون قاطی می‌کنه! تیکه‌تیکه پیش برید:
۱.
"اول ظاهر صفحه رو بساز."
۲.
"حالا کاری کن دکمه‌ها کار کنن."
۳.
"حالا اطلاعات رو ذخیره کن."
۴. ارور دادی؟ فدای سرت!
🐛
کد رو زدی و ارور داد؟ اصلا نترس! تو وایب کدینگ، ارورها بهترین دوست شما هستن. متن ارور رو کپی کن و بهش بگو:
💬
"این ارور رو داد، مشکل کجاست؟"
خودش باگ رو پیدا و حل می‌کنه.
🔥
با چی این کارا رو بکنیم؟
با همین مدل های زبانی هم میشه انجام داد ولی ایجنت های حرفه ای مثل Claude code و Google Antigravity هم میشه استفاده کرد.
👇
تا حالا با هوش مصنوعی چیزی ساختی؟ تو کامنت‌ها
معرفی کن رایگان تو چنل بزاریم
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پروژه bkup یک پروژه اوپن‌سورس برای اینه که فرایند بکاپ‌گیری و بازیابی پنل‌ها، ساده، متمرکز و قابل مدیریت باشه.
🎉
نسخه 1.2.0 منتشر شد.
⚙️
تغییرات این نسخه:
اضافه شدن
Restore
برای بازیابی مستقیم بکاپ روی سرور از طریق
SSH
پشتیبانی از
3x-ui، HM Panel، PasarGuard, Rebecca
برای Restore
پشتیبانی از بکاپ‌های حجیم و چندبخشی
➕
امکانات کلی bkup:
بکاپ‌گیری زمان‌بندی‌شده، ارسال مستقیم بکاپ‌ها به
Telegram
، پشتیبانی از بکاپ‌های حجیم و چندبخشی، مدیریت بکاپ‌ها، تاریخچه و لاگ‌ها،
Reassemble
فایل‌های چندبخشی و
Restore مستقیم بکاپ روی سرور از طریق SSH
.
همچنین امکان نصب خودکار پنل در زمان Restore، خروجی گرفتن از تنظیمات و انتقال آن‌ها به سرور دیگر و اجرای پنل به‌صورت
PWA
هم اضافه شد.
⭐️
اگر bkup براتون مفید بوده حتی یک STAR
روی GitHub می‌تونه بزرگ‌ترین حمایت برای ادامه  توسعه پروژه باشه.
🔗
github.com/AliRezaC-xrol/bkup
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7764" target="_blank">📅 16:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq3RUSuAgrIOkh60U0M-HfTeKP4we4CfnejaLG2xneDSTqGneaIaqgX675odcM7NDUN9TN7dhWEkJpurJlfldXzwn0iHhensL7S_RgHMYNvdQHIsQHzCQlxKmBRZhsuXuOKcVAajNVWat69HkHn0pBE6Edi71fD7hXxBnuVYJl5OXv4pzA2LN0cokSkrEqcJ8L46v7Atg_gZS5YZx3PnRX7l2UDM0jXkKfGNtqhJZwGc2cQ9y6XJFAZoLPzM67KGnGVFBL7wh8V9VCIefh5m5IgyOMMIWm4_AicxkkPEQaAI2oocMgDp6UvPSE5AuAseea6Tz-AFgW0A5GhG02OJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⌨️
آدرس‌های ایمیل رایگان برای استفاده‌های مختلف در سال 2026: یک فهرست کامل - بیش از 60 سرویس
▫️
تکنیک "نقطه" در Gmail - اساس همه چیز
username+anything@gmail.com
→ همه ایمیل‌ها در یک صندوق اصلی. استفاده از IMAP از طریق App Password. هزاران نام کاربری فرعی. محدودیت: سیستم ضد تقلب گوگل - حداکثر 20-30 ثبت نام در ساعت، تغییر IP. سرویس‌های Oracle/Webshare، نام‌های کاربری فرعی را در مرحله اعتبارسنجی مسدود می‌کنند.
؛ SmailPro - آدرس‌های
واقعی
جیمیل ایجاد می‌کند، با بیش از 5000 آدرس در دسترس. تحویل در کمتر از 10 ثانیه. از تست‌های تشخیص ایمیل‌های یک‌بارمصرف عبور می‌کند، زیرا یک جیمیل واقعی است.
▫️
تقریباً همه جا کار می‌کند
؛ SimpleLogin —
نام‌های کاربری فرعی نامحدود
(در اکوسیستم Proton)، فوروارد و پاسخ با استفاده از نام کاربری فرعی. متن باز. نسخه رایگان: 10 نام کاربری فرعی
؛
addy.io
— قبلاً AnonAddy،
رایگان‌ترین سرویس
: نام‌های کاربری فرعی استاندارد نامحدود، متن باز، امکان میزبانی شخصی
؛ Cloudflare Email Routing
*
@your
domain.com
→ فوروارد به هر جایی. رایگان، بدون نیاز به سرور. ایده‌آل با دامنه .pp.ua
؛ ImprovMX — فوروارد رایگان برای دامنه شما، 25 نام کاربری فرعی
؛
33mail.com
— نام‌های کاربری فرعی + پاسخ‌های ناشناس
؛
spamgourmet.com
— نام‌های کاربری فرعی خود تخریبی
؛
erine.email
— فورواردینگ خصوصی
▫️
ارائه‌دهندگان ایمیل IMAP (غیر موقت، در همه جا کار می‌کنند)
-
mail.ru
-
rambler.ru
-
yandex.ru
-
aol.com
-
gmx.com
▫️
ایمیل‌های موقت با API (قابل اسکریپت‌نویسی)
-
mail.tm
-
1secmail.com
-
guerrillamail.com
-
temp-mail.org
-
mail7.io
-
anonaddy.com
▫️
ایمیل‌های موقت بدون API (وب)
yopmail.com
·
temp-mail.io
·
dropmail.me
·
emailfake.com
·
emailnator.com
·
mohmal.com
·
tempail.com
·
getnada.com
·
inboxkitten.com
·
mailinator.com
·
burnermail.io
·
fakemail.net
·
tempmail.plus
·
mail.td
·
mailpoof.com
·
trash-mail.com
·
temp-mails.com
·
emaildrop.io
·
temporarymail.com
·
generator.email
·
mailsac.com
·
tempr.email
·
atomicmail.io
·
emailondeck.com
·
crazymailing.com
·
tempmail100.com
·
tempmail.ninja
·
boomlify.com
·
tempmail.dev
·
internxt.com
·
adguard.com/temp-mail
·
webmail.raoshahzaib.site
▫️
بات‌های تلگرام برای ایمیل‌های موقت
@e2tgPM_bot
·
@mailtemprobot
·
@hidemail_bot
·
@TapMailBBot
·
@botmail_io_bot
·
@temp_mail_bot
·
@fakemailbot
·
@etlgr_bot
·
@DropmailBot
·
@tmpmailbot
·
@TempMail_org_bot
·
@TempMailer_bot
·
@smtpbot
·
@SenthyBot
·
@TempMailBot
@telegaemail_bot
·
@hs_temp_mail_bot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">😎
دسترسی رایگان به FABLE 5، OPUS 5 و GPT-6 ASTRA
مبلغی معادل 1 دلار به عنوان سرمایه اولیه ارائه می‌دهد، اما با توجه به ضرایب، این مبلغ به موارد زیر تبدیل می‌شود:
🤔
Fable 5 → تقریباً 7 دلار
🤔
GPT-6 Astra → تقریباً 18 دلار
🤔
Opus 5 → تقریباً 20 دلار
استفاده از چند حساب کاربری (Multi-accounting) امکان‌پذیر است.
————————————
📝
نحوه کار:
1. به
وب‌سایت
مراجعه کنید و از طریق حساب Google خود وارد شوید.
2. یک کلید API ایجاد کنید.
3. آدرس پایه (Base URL):
https://www.rsiai.net/v1
4. برای مشاهده مدل‌ها، به وب‌سایت مراجعه کنید.
————————————
💻
نحوه اتصال:
Claude Desktop (Code):
- Help → Troubleshooting → Enable Developer Mode
- Developer → Configure third-party interface
- مقادیر زیر را وارد کنید: baseURL، api-key، model-id
————————————
♾️
دسترسی نامحدود:
1. یک پروفایل جدید در یک مرورگر ضد تشخیص (anti-detect browser) ایجاد کنید و موقعیت مکانی خود را تغییر دهید.
2. یک حساب کاربری جدید ایجاد و کلید را دریافت کنید.
3. کلید API را در کلاینت خود جایگزین کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/bUqxqsYNTnfm6sospqLvNnKyHBwXTcoeavxPpG1lkE27203Y-ttU61tBvIfRLr_J7V9Mkei6xHZoKA147A7fOesYRAuAMvirOa0fVKwfsx0pdvA67NTK25s2jThk1rB5grvXedUQXLDyE4Q0XdjDEowJ-9i-xicHlEarAIh1z0t3CRJd4uow-DxRIEqxEc_evpdIm6lgiG1B5rQcY-EtHNXWqREqZr3XS92KnShqcwS9zLJySn_MVPz_rx0GipBFgMWsHCeuXTz6Pa5kgbiRHjpP1oKspXgcYrP1htxc8DVqVCBaXjBdgo6L1Ne1jGMWMs4wcPKLHi6_kVBMeG3J0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/TFXdinW7R48_R0bWvlz1dJ050pr-0G39MFYSV5z-CQNF3livODLEE5KM3yDHrhjKydsytvZxAdjrBac7UBZ-4KwqvDRavKr9TH6qOoJDKcpC2naPFw7NlO6QbsrX1XmIibJR8xJ8oK5luNXVkOFU3LLO1ZUOXHcwMnm57hXQLNv-Zl_uCFHEtMwyfDL8ZwewgNPOAuN2UUlpTM6lr6Tbw5_7JxMMLICdZ_irDT0kQ0KRXWpbpFyhs3b3Ff04qllz2Ext5j2kl5ajy-XcFZM11VeWKbEQiKQVarYRj_KpW47MUtLZJG1AScwNar3r7AHjYaY2HTUUPW9qQ2lVQ9YZZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/GU7U5_Fmwn29TlG-IBd7BYFWTHlHtlBIPgAc3HBZnwYc3L1_MTrOo3ecslwM1Eoqbs-pDasCi4i8NfEzr0ihroSUrtSfAS2_uyncvql_hBgZSbU03Z0vxaAxOZQN4FyL8GETZResNwCC811XiHKgLcKxmC0H97aNGKV632Y0p-knwEDlxbYo7lYvzqIpxcqOtt-t22tRYDK9S6efFxVt7n1DbvQvkMmwbSGat3_4zJ2Wr98QUiA_66sIekXK5-UlTVDG1SzwdNW5NhwB7kaMt-9buTXsOkj7uGT1aTKxGqIGKGKjciAHRqQI_h6I7zcLfAoxXsvzR1BjMuDu4Ag36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ucJleJGUxAjdmlNPU_gVhtQ9HAjzLn70ah9yT10oSTz-iwQG_wAyJQUoyr1g3fgFeuCDXGx2XgZqLqo77nIKW50ugm45d2Xc3aEp4clFCUOr2XnXhC-CkIEKe9V7OeaTpZZ_pDF2EKQrWc6xUqmqdgDRdcBs1caF9Tfwmzdu5ZalzQq1eD1MK2OB8OQI8JvInfdqXLb6ukrz6VN4iVi0KqvZpsgIUrJpxjd3_-iISDh0HqHcTymEa9EzT4QF96bONWuYvEyp3gTBTFeOoLLz5eRsIZUtZRLssSq-r_SXGNl-md5sfu2LbX1jNu-da-P1Xj7Rugmf1FOs1WeipIaKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/uF5A023tUoWbCiX8pWdvUvBlYvGrxPUAgdDu-zhqudY18YpYyRGYCxESsM86CVv9aPmTWXKykvuu2-fxvBxGkG0FBceYkzWhl7I7W5RbFVgRj5M_ymXMh6i6r3Yw2Jq3Gw2CXyAm0GgxlvTwrAFYlGyzY8WHEGAMDeIztJ9MFOCXqhLx4HF7Mz0cw8YR3lH3QPx7H4IUnGVFYwMMQIjXwpykIGk2M3NUnRCF_7CEC7dhCIwEVNsC7IU7iL3mRWcvZtrJL2dx2TlV0x0TimcQ33Fqm2yv04POOv9QdE5TY_daeDyX_IlosbQ_bP7Ipm6C8o4n6GnxUjFl0rsmW1PaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/furAFfa5XwQYUUvCPZ8cEDu4SvL74_ZXFNOSssQIuQqEBDS4xZNuErsCAr3QuvIycwVO61d-WTHPE9ORNH76gUnMuK2tnc7RCbmAUE33X7kCUB9Zdm8rJFM5_odB843rLSzYddqVUFTSx_gXevrBlLxP2nl2TRQaTokjSHfnQM6kRkbU6Ur0ScrE9Y3Tr-mObz5GYiho6ohh3WLabMC3oN6pM_5g9-M4CO89UHwuPo5deBC-IkdgtJKmLi14EnGvSGFa7kHCUu6Uodbl8tCaZPUogM876Mdlb_G1Shjyh-sq4I9fkMVXnUIC1w9A_Ep047gBHHyxxK50Ry1ww8DcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/coXmydI3wMZOviZJQy2moUgfGtM8TQasMLg7MmwNsdUZQxg1k2kkRDurf2YOTD9SIIV4UBqZeJvEXpEnGWDlA7C7XRQy6cElPy_HchFUpVDZZBDe_rwkGomtzY0EE855_P0ZyXLN3s1YYa-aBlbOBRz2HHeXhWwA9rE4c0rv4ZtSdZz7QFm_sm3YvCOLaLF89QkP8BhqAA7laD7XCg9pdqTL_9gZyMGtY9NyrxAmuTd-TTPelfSxtzOsIzr3UQJpB7C_0wUmEif4gjVYonQ3OV4O9aeAeDoxdLg440m6wkYSgSEoDheiyp-1Fw5sTH_glCKtbX1TGDvxyCI9IV_FZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BL7HSd9pQE_9maCf-MLfC0X1DNVEdXLlspREQvsrabkyLjqnS9mr04kpNJTr12nGC5F0Cc-XDJoKcHaukcjSJr3_GcfuY6s5QDHaZjfmLflRtvZ1ffNxggFX8u_i3xkwX1Ns2sQgu_VK2IGFJQ1yDREiEFsIKK-Ng719_suG1Yq21DtquCkAP9MVdPiHAnUgPWaPYmGx_SnUlcUYT_zJs4u9giSGvZyADKejNYC88eNs5a49puhQTPu1xI_TBuOzJJfLBZb0lg9Dq0Bj-JWnSSXLS5O4cnN4D-vol5Lotancnwtppeb6cJgK3bGlHJAS3Ks99ZPpCbePQ2mYAH1Vew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6sSEkOO2dUGzVK6bLAXDlP8rYqtOlcmB1FPF92D5pSpU1SLCkG20mXOxNTwq96CQnCdbKHrPFDE3rQajJxMTLsX7kHNXDC-ViW14oka1wBZlJIOGTcqqVsi00bSE-pCboUASsQNQt4xEb9M_7z0ytatVC_5q_-pj1uLJtoDBEFnvoxfYi0IIw6NDGDWfnmqjNaNPKwwF5qdq9ne8uYS3ke4DQHfCzKBdp6bJLOtuf_27m32SqXHvymnxCHm1IPoHBJAegRUyN2ahWZECu7QvVNmtIqYH2lOn0gniOp8OO9gKzgYK7Vehzq53D75wEZM4AD3wxhO4Qv_UDe-Wz2HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/elvbzg3ouzIXQyD7E-qpx5DNgtzPvsyrVPig-RgNVS1_GVRQNXUziSoUck-7lI-weJuXwdb85cgts4OveK_mPhyFnasVsob-v8dXreGe0YMNz-E1ET7ToRCQnSM3ZN5Bc4Kop8hOqCCBJDySbzVfSHorgGvK3GqaY_WOjbZefB4dyJls0mT5CcDcIuWyIy0wtSPvNnfwRVsSD2Obg4quzL95uGBZuQ0mhHFJvVpuFgF_w7inKV8BJTuCkY1WswWRgu9zyBNavosNQ5KxSDK4ZgeNyHAzLkmkENLJg0_vKJgdNJzP7_Y8WFSbPxWylKr3BOSnVrdo2ZV7T9qbR7y_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/v99gQ5_uegVaTBCVCNdevUDCknu1CclMAjf6XIDorHQocwijn3LPbaohewcHQWhm0_NS4136lqXF7PEvXFZWSZkimIfGhhUIxZDZphp-XI2uBB4B1pDDGNY8zfKGQWpNTLIry9HUx2I9i5EloXMl1sCiD02GnMMqawMlWw4gh3kZM7kwP7iPjsOAZbYny1xFZClWLwRFVzoAxCBATj3Ey6XAqBlpOnJfK_0odmX7ks-0kRxMwP9WocA3Y6UQtkGB2IqqOYNxDMuSNuQjLehpbwdBTddxS5jT4ES6CFSD7lnb6Hy_I1sPA19OAGCBg0L2U12U0IOIGjmHX0-aD9EFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6yhnyZAaC7Yl8tlL2ReQh10nuK8xGiVqb-JLtIWYfzRWihNI5WBAgrx5XfPS27iWLVwDkCEtowMLGMQ2WkGLFlRBvPPGREvdu2qUhY_CIiYJLDLg0RCArwz8mZHMJqRNhjZ707oiZBMx6VhE3XfM1YJ8MkyY89KVpksQ-iaqDdwVj1AuQcYCK0Xv_Wn-V_fi-qGl0Nv_iIA4WFQDJNH2yd_qyalsKxduyJCFa9wvLJMEGiS5oqb7Nhbbc9UAnGfa5Yz2fVpgfAN6NsXHG6JCzyX49dChDpl9Aj9WYN1gtPmpklw8Fn_rEjfg2_srPpucuY3YemJV-hq0H_sxmYUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3dfZYBE4SH1afkgL4eShKn1voYJ45RpysZQMTxdYki8nWoWtAXUbu2Kj-HikSZg_jXu378IVQHnNvOq3Vt82mET2DqzMimL7DBRe7AUK_XcTsTEdbTHwmEEEP6lKcvFZI31SCatoNrZ4TL2K40Qd4QeD-ewReOKD7E1cKVydE-PVlWwTsBQ1MQXIP8Tx3if8_f2WtojhVXE_oTmXNpmD3VcqAQBjB6AW4oCVOd6ir3jlvx7i6Xc56yWilIzQPlNslxnIdlD27-qeST11Dzs2wGKEaAXEgL7cEL8A43ViqKyhcIa32CjB6kZXWfJBRggqqw5_y7EqgqQUpGZqsKDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWOyZUJd1ejEzCRofdnZrECTVmbBmhuOxt_1l7TtNGtMeyyerBmewlKiPqLke5noGX3uncJm_Oywp2TXRkrt7ONlPNrDyKE_y0S4FHM26FasQ_7EdA6FdoCxgB61PIF3xP2u5C8clLKeeUIZbUbzqHQ5_T2tb27DcNn-vxpWEKRFKtnvTDUQF1goWlmJCbpbG4sCPemoRpBh7t55nboz8j4GBa02e00Wf5EaBG-DTfEngW2ddh2OhbGUZz2A1XqRwHN5D-VGTUZxC4lzRUzZO09NAolaultH9OvjYTXjqUt-mj4wdgpW9mtTgGnZpJQQ467a59f07NECCMvfgX_WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mzVhdiVSmhi2meHjH3zSCEVdvF3i6Yl6SQVo32Dsx46Lflu8WTmApgrO933nnhZ8HbQ7v46dnzG7110RWoMnO3GER4N6hP9Wtc0vRQRtrPrKrFYH776ipgG-nlaprawteY52QEzZAzR0lminN62SGUB-VOuhdyLITzTeWu_4DtBK6s7LC_YrBxu1S9CquFdU3yRiN069MoKug_tK_dfNyyvhDXRok6ZF7Vo7BQbhpL5588WWtolDrZDVgCc1268_pE5S3alunGSrXhCl-0dmsDV5ScYMnVfeZTb-ZWPHzZeXoUuLcZo3Ibahm6huy3cGliGIdgB8DSdp67t9Viiwpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mzVhdiVSmhi2meHjH3zSCEVdvF3i6Yl6SQVo32Dsx46Lflu8WTmApgrO933nnhZ8HbQ7v46dnzG7110RWoMnO3GER4N6hP9Wtc0vRQRtrPrKrFYH776ipgG-nlaprawteY52QEzZAzR0lminN62SGUB-VOuhdyLITzTeWu_4DtBK6s7LC_YrBxu1S9CquFdU3yRiN069MoKug_tK_dfNyyvhDXRok6ZF7Vo7BQbhpL5588WWtolDrZDVgCc1268_pE5S3alunGSrXhCl-0dmsDV5ScYMnVfeZTb-ZWPHzZeXoUuLcZo3Ibahm6huy3cGliGIdgB8DSdp67t9Viiwpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4zAXWbcS5u6jqN_g26q9ywHMGumdPC9XBN_vB1MqqJNUmuRhgiCI4Q4OKxInKdRUE-T164HFR8KksFD3zYbwXy0IfZMgCqMKffG6zowzAwabO1iWcrunPmpPuyD3I0tIrcgSV1a0CPslRzqCvtUcg5yrpFejtBKwnDtHnbkX4B8_ziWtORYxM6vCPSe-vilheSMQKICNhBkqfhSWFzgZcKKHBjuB_vjd7PrsamTH-oZ-8ojLxnxhHJ0NRCQA9jVvlA_FhAojMlJW-hC3uX4s_0GMMTcwUFEKpjuywmH2_kl-vNOxezBfYEv-iifcAPpZ29b7K7mXqWZ5kKTEhBzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8yu6D3eJEmf6zWn9GVrooygZnbzjrOveNk3tBAmI9TxJsB5ODBLu7IL8K7dAVLcoCUI3FSdITO2BNZbM5FrICjISUqKa4wOc_ADhvpskY2eQ9iTIanScfdkkTuzlnA3JyZkLVzJXFyWxJNqrnlnvBjKTr0tgbSFc62Y2eK8awDBuGKHiZK6qd-10ST2UGFcIkfCII5hOgL1eKQGm_rMF8wAZ0vb1-2pua7BOdVOk0W12vGI4cVI4QmLvVDYbFyZ_TQw-wLdx09Mlkb_UN1YN1O7mAqhNjncWRyk-tKrVrPv90erJHtxJlyxY0j0l0peUAGuT2XHUmjfD_WaSBptzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXRVYgPAHQzTf-sj0WpW1I5Z4mcOGikc5pZ6RtV6TKZjZKGkpnzbIKZgSkvRTUXCJui9yy48SuDNa7TS7FnnXolEo7fUrFJLgyZ9w5442Ahera2Xdbw3b4G0Ks3-BebnqQlXGoVb5gktGTmlNZCtHsymcsYzMHX5fu9uRHIuAR8wzfN4AeO_mMZpfufOkyb21XSAJHfXQAS4SkVbO76GKr1uAzQ2xD29uYgzCy41GTI_90WsFq_2APFLvz7YjdwCOeIbYW5jHdHqzsMa2ktWxPMH30N9NA6AOlpWN06nFeK9U9vxdBR733jFbddRxoamltcpVEPV3ulxOZJpOX_iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk7vuGSLA6v2k7zHbZeUhh-IoZctWnMWOWtWrdxisFj44Aw9_A6W-pUTeZciiTEO3UT9_cm7BLZoTE9m7q_0yfIzg_0EjLCIPh2xL9jO-SBoC6dvrDjhF8n9aWICo0MdPieg3HQ9A6m9Ywtu0-6lSfZiTl4pUz35lkH0Kiaxvt9SnZ7oFGZH5XKTJbrRwrJxKMnEABr2_60fpzeO12ak3m5OMVJmZurUvBHGtuVjB8FDqRIHWxaRy3uaNYrBsjG3yFnEjC00JO-avSuoSWJdtlfwTofHfQXVgSQORH2y1C5DTMoLQcynNeMWZ8bfhbxznc7FbiEGAzgvoZfV1Y-WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWzonDykuvORZJIntf2LDlxnsghcPWZkjKOghwpHzFjEw45ClALCfs5CVyIy_WRqWuiiZnSa0NNSfLac8pADErXmAS8J75l34IfxAO5wGZ3tq2QbIQycw1Gi1Jy1RJoDVQieKJ5sj6GjaNiNsDdrTXMIHtIChsRARkz8yQvL9Xq9TJ_Tt_8meFo7bBdGzQ1ddusc5SNRpH1SvzB__C6xDzdGOeymiUsQts7nsOY9p9Qu6MiQySreEEB20TySzT-9D911RHRC2l0eGDF4h5ttrNiP_EPPV7fa5G00ouYDbyU1dyciKolQuajKCFj0OqI-V8JksawSXsT2c7wN5h-2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/erP44u2XN9n7JbaawxcoEwqESI6YuZcrNx5fE2cHbcXDhYPzG9bxWJvUinBg-wKlJGviVRr1IqRRZ_rz6h0TSunQ8_UtDKcnxpcvwxBws3Ta-xvU7_b0fX3VZAgmRUSzV0MMKXxx5bs_7P--Vml72uAGIyukA6pVYI0-ArAfaYGMDMcvzf_gtPFc_aUVZT1A8KUv-zZkUMLIuNRnXnEZypeWjFWRFzp6b54RoIOSJF9ljc9c7VJ6VLw_6XCSL8l6lgILkfi23j28GhycHfqVPehd2NDyYMc0JTjYxXW0y-DQX7DaWQv5kUuSBVwdH8WZ8A-NSQzKazgTAFvaJv3keQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbYSI4zl1xtn7rinM9zPKNrInHyJ0kqeypPCKhcOsN8cXeD1PXyYkHJ-28on6C_HfQHiPseElj5SirASdNTrH2RT8pxgBw_8l7dsGUxrDeZgka9pLX0MMXAk1AeFpT_IhDNfxmfuuxxYhLwr1ZnwM-SOUrrvIKYE2g-MW9ETPthP4yOFmtDHd3C20YFpIAxpfY15hVYXeE6ynXvVKGJvmsz6Ia1NzpJ0lgm6U4Lr8zw5A1G7bkcm_9nqImCxkVS6oFlOBqpeT5B18H1kSzJnajF7b4v3ipomnIzJQj6vA-Cf5c6RQGQXt93Oe4fLKk4y0xYglxvsHqWtArSX8A6pXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8VF3vYYZt6TLzMdElep90TngOyeZpg056IewCcwn58uNeeMk1V2Ir2hsojRQ-nZDDbgfDovj3W-2AIADjZRHU1cqZBak5hWe8iv8sqrNWkicjL4fCoNjTQo65zbtc2bnwBGg7EyzPg8gN299rGAeT9ox_eVBFXGNnS06MdzaGPWDQHvTgCw-QV3W_GKipq4T6OAd5uvDI0v3C5flLDvqWg_hqKJ-JUQTI9RF2EC6gqI8xRipnkTGFgA8JmLub89T1KHp_PquERThYQltR80aOn8QEwaGFriTgniKv8QYNXXI2ZUtutnaE1l7O3Kms3Iocp8yQoazGFn27CsRwCo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGHMP5OKZ87EKPeEeqMdyibUhPqWsEwr72OkMdRnBHbgsgQzgAPHcaVyk0Oa28PYkeAUGx63FiR3vR26Re5P8wSgQhOnwP5jSd66VwGX3E-6mUTGEp06-X7fB2prYNGq6Q8sKZcsEqMcIdFupnXSrccWc4i32mZsxZOTg9Q38rRnSeE3rO8FxwYmsAUxsHGy_35ovpmzut8PH-VocSNHVyrBdiLavykKCiDxhxxz4gocYaGDFhR35-76L-El02X3bByCdYp03hXQyapLGZJcvBdywIArjbT9xmvcLac88hFJHasE0LTehUzq11hb3sZUhDXx5wfY9-83EH6ykFkBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PenwPTJh3ENi3A7OdD0r_maeuB_X-23PbKP3eUT6IBIc-n9cboLUaj7_NbyWN34DCyT2NCC0EW9lCb3UI30qYO3WLtT7b6CNbM9LGFfHY_FTW68_vhyiKDyzN7mAkqsXYiQYyBZHHaycDosjTF_apc0xwSvMMwcUamYSjZ-0_BMYsMgi8zi2-Xg7t_37785K02uVKAfvvn1ACDwxcTEMn-awwKL5PBBtk1LCvjFN7TvSgPH6LmgPyR5zrbilJDjFf91MT7OTp1Oy20pB1sCfIKbzJJh_bahwlkKsgcOp6_CYolCjnJwPH262jrDmSe8DdWxkQZ__PzPKU7j5G5zf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn_PBb7DQiKPLV7HfOmSJmGDk9cMKHPExLvnNNDpxNNc3I5ayS1AHLZdkAiMnyGyp3yXAaWsCYzbYGJL4FEdUJu21W_DOgQn4VzwlIoYKgA3ySsfYG-H5U85nRqwaz3Cv0ZO3ZF2p1xirPGzP6Wn5INJiY0YEpzRhMtqoiu2R6qxFmW8MzdJBhyfSEwUdFPFXNS3SxfCRMFmUmcfOcJvB--5pR60V2Cd0Zdyuipf5xviyXVkP_2q0ejKE8C_sQIaJP1TJMdvp0Gis9FsFC9Cqv3roatNoyMmaaLW0LWoXtBOEB25KIgu7uZcy8zM7fG09grnTkHiM7A0gGI9yz4VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8_dDrADzIhuE1-ytOh7ng4maN9jAvsqu-dMMpFic7fA0V2dv5PNU6KHru9rEdKZGQpGuKc2UasFhkyUO6FvzxEq_TlJDoanSsIbsrrcj7q7Im9Rt2V4gy37eYLgBzdfs312ioqX26yoI23BjZaC4I3VY2ibGU65qgUzZUxmfJmDX1Raaxz5tFYGs6T8aMHBcHDH8p4HuJWJ8bQdtjyY72d556jtqU3iAwAgG2jn5X4NQ2AEPmcTPQbJR4_T542n5_EFp3-T_7_ZTtWZCATxHJsgK5IAQk8S6Eq3AP7UoIcUvGgohlPx3YNY2XnKw4-irmOh0DrlJ2Dt5Ojlw6lWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z18gMkOOpCx6qXfJz8MOGEtdXMn7o9i86WgJDVPZWLoy9rEkQ-X_V3GBrgk0Q0EhOQGEwYl1qZa5IKRxm8USawNdp322AFPAGncWRQShznDWdX7TKChMC9iOKeKzU1kyPC9o97HxJz5nzYrAkzqw_ubbAj6GXYSHfW9vsqJYirAyMHDezXAYmCiXQQpiLZeSbJWN0k3PlvOzTEI-_1yL4VJb5Eymg9SVktcj1ZZA02el1INjL8KlS6yr958tv3emV5m7rETkPCK0gEy4AOmqT_hDihBFiQnnj5JY_3YA5EJQIk1xo42eNXUYruutFwGS9mV6LjQ8V9yVMYdu1_WUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAasv3nQ7X5-m5c-wWFwOT-B6zSVzVn-mxtLJ2PGq0BwyoW0VExfYjzK6-i1OqR45_Px5wotM7h2GM2Q8-LJt2Clm-r_kt9jBRG6XNbmOyKmOxdahWx6wXF-8gY6QhiI76VK_ZDB96dIbXxWOrILrDmlnT0Bc_MySuKnblXL7nvrAKBR3f6QegY_afd9Rv1f_LewI34r1quFegrF1Q6De33812IcAcndQbaKrBjW4R6oX_gBD004raK7ErqKeWInK4TLq3L7cPl7kzdiiMJNDa4TutQn7pUm3bDlP4dG0FLo1w_ZXjGcBcxiCQVajlfNQC62mmo_a4mVyrd2rKe0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvBeHLRo1LyWThwxA9V43Hz4twvfgKn04JjVuRDVvXVNBdlC-uVYrbTkgtzFtHK1s1sW1UYhD-q0W9c5Z_JZLFq3EQdIlW_N_qxJSdsN9KNrFaDFuwTBCXt1jByXdRQUSxOGYG9q_rLPzRUc2t845cx1a0qF9HGFhqj1DMMOfrdaECpHKBRJDpuEuQnG8xW-xbI4RmYxubpg5TYaqb4qg8bqeBw4fsTbFO9taUng1_VBTPOgL53w43PmN1qNjPICQyDrvdK5oyPYUC_BY6t3EXzRQN1M78tsQVKkMJc_G8aJHnTZiqBY614JIIhh-CNqEp2foeXfWxTxiwiRMrHOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOYhZ0iQwHVaFMhSTZnY3_BV5WSiddEdn8Hv2SJOaxg9_OgnqD3AfY8nOdhpdFS13jKA2vEoavUTyP4fes4K6wbR-2-pPwJiTn0BOUMZewHqcRfUpqT8j7lxS7jZRTMOUUgK2HNoiezSDkhPOT_gLn-y4q_H82FXhdnySI_eZPPyV7tEt90TaFeJOyDwuEo_4RcKteLM1Zw9I4raW_IysnC1F24o4baOhsCBELuo92xP9-QrjDWa-mMFUS0Rv4NXNYtAYztL3be96juidHAlDxhxiYWcXgRi1ctQGTguMYUOgZ40sQUIou9VMNthl9TL-Xf4Pzji4O-fH2x6-MbLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFc6AVLHLDR8QhpDCEyQyfa7smSC9ixNC7f4WOzPMVWKHiHs6tzCmc4g0M_X9F9naohfPWvYF1_PyeQ56PkEq6L893WmX_ToiHqy0s67PToRd3pbkIG82cuQrQTTOZVBNOG18h6mofzdRYYD7czc2-w0M4waoYvOlCVCFgk8ruxzsOSh3GdpQu7yH5Ute65boapKGH0XrWgihLVpok13dvkcg0gVqedAAcpljaVyvqUcLCHxE3XHIB9Pw2_LvNWmZ3mjb61Lhcr4AxQiLYSHtokZ__OmqIVQ1GxIo3U6oawBH-j528MO3NYFh25V-REJC3Ydyf_Z6rv9nT9RxyTTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W74evXKn0Bmg7SO_LDaV5FOyymTjErchkutixX20gIIwPIq7XhlUbKB_R4FNAQJL49B0dU7_5k5QLyoIgBTdRIvm6kBgh_caN-l8QzXzzUuryErmsv64wQU7LIb34XkMJmhrga0IMmmFhbEsbZqKuKO-0SGQy-yYB_HIqO1lbIEhC7NSLn5cQY33ZUALBtOipXoC0w-ENtMmxcgTpjuK2poUnEEApcsWeSGf6KoEJ_d995iSfwjWGJdmVt_D5n5ITCvSzzlg1eEK5b0gBP0bOQKf9eaS_z6USg0YUH_WS1dcagn88I-XOFvt37vR1R9yrKm0gGVYi3DcjeOrQOq-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XniQREeRWVjigt0WXmHjHuybx6A9MqsI0XlQXhp7ORg2eq0nAQNdMoncffVGUDnLHFyYSMYxrrnB1AOXWsB95iEdc9FwpgX8YXPf_dbirUKgKqJ5sztaQwgbM_fqHjcVxnMzCuBIhUlOrpLsvWVPtOzLf3ApI2nON2ys1T4l1lURYcfvog9F6oSwYyuUbTyu2JSnW67PgWnSWi7xcz0H8ylJk999QQqn7t41SbZof_A6kkF_mKrVA8SCBGaPU-j6Fj5lXkm_mTV02avNhlbI7g472b7ZVQYjBKMLeI3r8aiKW6vBQqNXqnHgFPgqFwT4O_gR8ivzgf4DmcDC1e15bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec8yCLFnrwnwSXvGHEpbFHoEac8xOG1ElDHxA7GgWhJLFpZn03hIQwfvZlzMmtloSYO89JWGQaKmlrZjH5fWEmFhWG57hiFl4uo5_soZDaG0hLthnog2bH9-xSZMdpLDeTD8dz9vR-cMGEuOtkNR8k27L6ckwnOlcXNo5bAuhBuVMahPcnBWJVwVqvvziZxiHLmvIIkUtdazZDb_pCJBL1LzaJO6Dv1DbElvhx1TRS1j5aG3wUVG1BI4ehovbdoL3aYknFR9_a3MdgRC6PcW338c4YWA-xBLfi0r5f0zs-YoPubTShCR-iesS68y16O7a8FfwaOUGp_0xRYVJOx-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Z-_6b9qOw5-KxMxWUfzoOTbDOO34Z4ysDe8APwa__7ngIRHbcgSajwaTWjLqrqI68cEOYDu9qO6rZKCyPlzWnjy5XI76RDv-hXk19_z_76pC_4Zq_d8AWUWJptQq4T3B7cw3Pe36nKAwqQv2_EAMl94wp2NGQIbsFCOKi5BmzhNxPSBpKwReKrP-ovUnoDFxUD7_9GIgmrJN0kgFrQVY4CLJoDcDPFcwt8Ti1_bBFvevAD8m1fnL9qVHJxCx7FZAj4mIiGNJTxFlN8b6tPq9npY7OkNKtA98a0IXltorAfZ-pnl89bpvYCY-l7O5HQ9_Rdf2Pe0He3RLYDphgKNZKYvYEIgqu0vy2PrV8I8q6orQbfiDvp9XZeAxP9pZ9DMOjPRfDOquzdmWV3egIxLcMOeImwAGvIbo_WRVIVBUb3pM2PJMvvWLdM56pNTkozwoawCMWoYB7nezkEynZOvWqjF092T3gY1Jokb_xUmlVs6XeaAVWoze4CUM-Px36VLSyrU0AuPW-ZNRii6mYKBc2jZ5FkQ0tIAwgJgWw7BNZWmXj4K1Rm-93ASQ7V-4wtNzgp_Ic7mPrXExv6hXlEKrdw5V1U0YKzxyIWQZ9dBxqZP9DEjqybeE_GmJAhgJeBb5xbtN2n38ZBKaufxTil4VK6Gpe60f-4oZ8t-Tqk4OIhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Z-_6b9qOw5-KxMxWUfzoOTbDOO34Z4ysDe8APwa__7ngIRHbcgSajwaTWjLqrqI68cEOYDu9qO6rZKCyPlzWnjy5XI76RDv-hXk19_z_76pC_4Zq_d8AWUWJptQq4T3B7cw3Pe36nKAwqQv2_EAMl94wp2NGQIbsFCOKi5BmzhNxPSBpKwReKrP-ovUnoDFxUD7_9GIgmrJN0kgFrQVY4CLJoDcDPFcwt8Ti1_bBFvevAD8m1fnL9qVHJxCx7FZAj4mIiGNJTxFlN8b6tPq9npY7OkNKtA98a0IXltorAfZ-pnl89bpvYCY-l7O5HQ9_Rdf2Pe0He3RLYDphgKNZKYvYEIgqu0vy2PrV8I8q6orQbfiDvp9XZeAxP9pZ9DMOjPRfDOquzdmWV3egIxLcMOeImwAGvIbo_WRVIVBUb3pM2PJMvvWLdM56pNTkozwoawCMWoYB7nezkEynZOvWqjF092T3gY1Jokb_xUmlVs6XeaAVWoze4CUM-Px36VLSyrU0AuPW-ZNRii6mYKBc2jZ5FkQ0tIAwgJgWw7BNZWmXj4K1Rm-93ASQ7V-4wtNzgp_Ic7mPrXExv6hXlEKrdw5V1U0YKzxyIWQZ9dBxqZP9DEjqybeE_GmJAhgJeBb5xbtN2n38ZBKaufxTil4VK6Gpe60f-4oZ8t-Tqk4OIhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=jnkrBIBayUlT-F7OyOGWXpWdkKYuh-EHYl88C4Rls37OGT_1QlGXg-nTIhno2maYWF7uo6LgeWMnpq_YMfvQcCbfg3zPKqOayr2dXrRabH7DmcTrDN3C7AIF9u8b2OM1RyfuFjSt86WHFKYNM-R3tOZ5_n8WGxWq_gRg7j3vbe-ONTZsU3-plUwYS4nYPjlArMGLdtPbXMcuvCgEJz8_rrKqfmYZ_GXJ_KaFJXUzuxDrpaXCfVUDDnCPuCHdamPV2gv8QcPWzwlKdW6kPF2M7ExID2GOOuUG3MQC2MijfPtS2J0jnqE1tHJKnfol5pSF79xuWAz1b6KPBHS97DQOd0n6eCbrCr7adl0dpBn1YzsA0PkXCdp9NAJZpgd_ueQq3Sb-rzAIAwVDcqGUG-wo_OADUKkLfa_9thrrFJ4Qw8HmpMCpFriT8mTHmUINiQa1fXk74WdmBz82atG79WkxJYDyh_dF2R7VpbGdxsqx_jEubRhnAiWkS4uAjlIfZJoVxZeQj3CkvAwCT5GbJ2DFdg1-NaQow2M7lPIk5RsWVRpJ_KIO_U4tHx285eRu5Us24IE8sxpaJVeNrb8CGYxG4v_JILBdADe8i62ljIbBZW6flCCMPOyQXxxlKe52tHLXVBgvzA594-K94Rucq9X-V_O1w2qGhPyfiRAxBylxMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=jnkrBIBayUlT-F7OyOGWXpWdkKYuh-EHYl88C4Rls37OGT_1QlGXg-nTIhno2maYWF7uo6LgeWMnpq_YMfvQcCbfg3zPKqOayr2dXrRabH7DmcTrDN3C7AIF9u8b2OM1RyfuFjSt86WHFKYNM-R3tOZ5_n8WGxWq_gRg7j3vbe-ONTZsU3-plUwYS4nYPjlArMGLdtPbXMcuvCgEJz8_rrKqfmYZ_GXJ_KaFJXUzuxDrpaXCfVUDDnCPuCHdamPV2gv8QcPWzwlKdW6kPF2M7ExID2GOOuUG3MQC2MijfPtS2J0jnqE1tHJKnfol5pSF79xuWAz1b6KPBHS97DQOd0n6eCbrCr7adl0dpBn1YzsA0PkXCdp9NAJZpgd_ueQq3Sb-rzAIAwVDcqGUG-wo_OADUKkLfa_9thrrFJ4Qw8HmpMCpFriT8mTHmUINiQa1fXk74WdmBz82atG79WkxJYDyh_dF2R7VpbGdxsqx_jEubRhnAiWkS4uAjlIfZJoVxZeQj3CkvAwCT5GbJ2DFdg1-NaQow2M7lPIk5RsWVRpJ_KIO_U4tHx285eRu5Us24IE8sxpaJVeNrb8CGYxG4v_JILBdADe8i62ljIbBZW6flCCMPOyQXxxlKe52tHLXVBgvzA594-K94Rucq9X-V_O1w2qGhPyfiRAxBylxMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9U1GEa4a-4Foi-APJfHwbfCu-kVgO6mWri4mtrz04OCF-RD-BPl-sK5DLMDzKZ0pEQopXgo-RQYuK3Un0EbPNo5S1PsZeTpgubTG-3HcQpkkJq8COZZIcs1wXzeaFKPeERiQFJ9o6ZrAX3On_JFJWcGxaSewPCAVwPQiwmHF39X1Qe5OcOJ2rrY3QOF_k7EGSyWvpoEMNhaMJUyOqoDnRZl8phofxTVloGvS-0sg72mZZwl47OBH4cXgRIHJxRKBEBQKFRDJNVbShTuyjROp2dbjn4hMC_a7dRyu_NWTqE3HkmTqvyZh-Wqb8QHz5NODMCGREXFIhig8vI6bWXmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=j-slugurG57FsylaWYCfsvCiXS2l584t8-iDGqG32FHkQjDW7qgYfPemQp_vntj9tip8dR4S-U9GKRmfbEL-1vpUZxZEweavswVxobf--OoJKp0PL0mRJvOfFPnKxQzlaRMjp2Mh7kSIuzeYueCWQthJYqAJr-wrWI_GTSkVaA0ygShIe6uiLLviKAgfmHv47G15k8abQlpQHhv-XI1rxkZ79D2RO3ItBmRnJBVhPLATbzbKuanWcMn3v3TjzJVOBro9KWN23Rxzp_OBX1MxDuA63EKiI_3nRaKDwdI-M2pbjQ3YCeRmbCUxTM3zsN4eu9JEZGHRFXFngw-KyJLRVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=j-slugurG57FsylaWYCfsvCiXS2l584t8-iDGqG32FHkQjDW7qgYfPemQp_vntj9tip8dR4S-U9GKRmfbEL-1vpUZxZEweavswVxobf--OoJKp0PL0mRJvOfFPnKxQzlaRMjp2Mh7kSIuzeYueCWQthJYqAJr-wrWI_GTSkVaA0ygShIe6uiLLviKAgfmHv47G15k8abQlpQHhv-XI1rxkZ79D2RO3ItBmRnJBVhPLATbzbKuanWcMn3v3TjzJVOBro9KWN23Rxzp_OBX1MxDuA63EKiI_3nRaKDwdI-M2pbjQ3YCeRmbCUxTM3zsN4eu9JEZGHRFXFngw-KyJLRVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85QMWFejBfi-7iZKQKuDE1J-ScDuHYmvq1vYdFY9n-gmST2_uWrljFdEJpwkAwvd88Kou-9ar9CHEqzVZ2Hit9e2gar4N_VVSRjLoLrv9NTBbMmpVzkI-0eAd6XahWt765OCoUTSfV_ep2ylgTUhj8lTD_BOFZM9ZBm80Oa9hsQ0L_o3TneOnwSA_-nNh_b3g_MRvfwQ7nqYLn6UM5H5Ai2wJR6EoK0l5TOiby3f7x_Mlmo2NF1X8ptT6EWrxmAdt-myLSYVROW7HzfLCbHHgcfmS_ygM_g4lFli4BLsW4N8SRgGPmhNCuq2zAuX36_-ZMQhwW_uE8toIQk2h7AVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=mDgZKg2Z52SoJnnVFgTB_BvDec-bIqf65JaE3LGoXbKOamP8gfn8-A47a0VwzpUAEfSZmoFf64VQcBz1x7voEUjkSGmQLJ6FwwghXlKz0brKw5ECg5SyDn7NR7B2MchVeQXDnFF7U83XKOnpauYuwZyBXAeowaKOlFmep9sIXTcC63Vc24YO2iWgCkTaayqho5pPuYr6fZioPSSMNO8qiF1GHg17ctJ_nnUJGn-VCiMznYldinYAhkolGkjeMqyq2PcSQEwuZPeexi4t1LO2tDJBfEiGeGKRiUOGvVbzXH1TzkWTEgYWz30azeZmdsBiCsRziLVHnom4f6JuQDWXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=mDgZKg2Z52SoJnnVFgTB_BvDec-bIqf65JaE3LGoXbKOamP8gfn8-A47a0VwzpUAEfSZmoFf64VQcBz1x7voEUjkSGmQLJ6FwwghXlKz0brKw5ECg5SyDn7NR7B2MchVeQXDnFF7U83XKOnpauYuwZyBXAeowaKOlFmep9sIXTcC63Vc24YO2iWgCkTaayqho5pPuYr6fZioPSSMNO8qiF1GHg17ctJ_nnUJGn-VCiMznYldinYAhkolGkjeMqyq2PcSQEwuZPeexi4t1LO2tDJBfEiGeGKRiUOGvVbzXH1TzkWTEgYWz30azeZmdsBiCsRziLVHnom4f6JuQDWXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp9JMyYdtL1HOAYFeZpYh41nOGKNL5XNIZbiOzgLa45_SlDDBqjNhJRP87JQpP8G_w8YzTvWyLi3BBCrOS_ii4zOsFmDzLxhx33TVXXL850Us8nS285fuxhNGjAKF3MuFuV5tQem8U2czC1rQM4-4XmeTaDhd8IdxPbgyonoyaSJhkpxzUiA0qGfyvGZOvmhm6xcpHy0aH9tx8vZG36TkbzmnV9wSQnmU1UbvdXweZyWsKxNATy5_gtv9gl9_tHZGSHanq0Y5boTZFL0OT4Ngl9zBpWEpmdM9xYlfweGcGDm40FjsQqazoEnYN1X612IP-eAnkp9tsU7fiRwQFUh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyZKpa5gbceT_oEIICd8HU3ppSJDhH3SuArOaP1OBu0DuRIsTupZNzk7PGwAZpL5tFMz3CMuwlE3kGqPIvJCAGx9ch-33UyyBry_BQzEWf_a5w4MRkbpI80DeaDIAtgyGjIefrYPG8hiysLYO8gbkk2nShGZR_kWIK4cmP87xrCXRZ2kaRaY1XyhjciWFYnqUWg6fx80msklFhipPYo_fEfzAW9n47QDdSW3hJkXtOH8mZ5MmJEl9dWTYAUT9SvCxOAsUUTzgAcxGfDAeHZIyzr8AUoaDkqwQu_cIdnk5HlZOV_QrR7BdThzxukeUKEqlxgIwkqVOf4Vn0RUhzRQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VglUDc3iBGpKPjsY8cG9M-Sfr74nrpYw_spNDwbFRjayWQUegaMMoTVX3c1S9Mc2trWesyOWtOg4N7HI7_SjcH2CJ6DYs_LgstOBSu5RnEhJYDiAaBJMW-xtDGYYL5BqkJ-G_wkMro5u2x88XITGzXPhIms7rnbgm0u-DabqK024aU6qIT1MIXa0RZv98row35R3rYMaqTwm9jkZnH7_R3RgzbpOquJ8Y8pckttcusYAOXea9bpgvDvPiOK68r-KSoKjiSgTcB5rM2xX6Cyl_imaEayzFJI-bFCvQdzQI_pWMYRa6UQIdEzZRj95z5ddkorLDDM90ogDzvlNOURmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny6_ehGyupkiLmP5umfOBFthBatSduRuX5VvYQEY9rJJv8SM3WBoBkDgINsbjyrcKWS-aKZZ38OKiok_IwUEnRNTE_YfbZMbE2Xt6O3cD-g9tCx1gOxY3ObA3WX5Xp3RwUhpyXRmHAiSz9AQO7IZyvgiw9gyx7POO6r6nhZVtck5tP4Tgg4aZuoyVp7tCpJK_UmPRktXQz1LIaf8YpA6_jFo5jCtWvUWMOWWAKxcpvFmPgCgY5wSjzhvJY7XCM53fCsUmF17zIOFnw8XRyr9l2jr4jwY2EifYlPWsrN5LAFkKSKy9a3m0NvhL7EMQFUF5Aza8qM3_uLFc1bnGvgn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uj7qt6HUYau-YLlZwrOiMcPML8UBjgzxOmjP6J-Z1y2Jmf7C3ubhQwLwowpaexmShwgYJd3cmla36Anq4i2uZUdM0NDTnxO3wCSb_-CjvR-MH98poIpKDZKGLnAeZ1b7SlI7aMRQooFwlQ8NHdatcFrmQhNymERW9E3_HWiLBhsXRs9Jkf0o2vL4Py4suhEJtgd8gAIgCR1sio4o3n5ZoH1EDV4sjXmLNRuBHPSzSondbTBx35E8xovq5uvIIeWBo5erSNfnb_ljz1dml6ROL9GH0Y1_46_jykhl_7IR5ou7w03qM9zI0xE-0dxRKEwJq5CypAO5HN3UCetE-8IGtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy5XID6aKT8spOGyosJITuWb3IA-XJJozaeC_KEJnGkcUnrNcQGjCrs6X0E_-usBEU7xiJQhKCHPjX6FJXkhkLvOimnYY0SXAzZx-gWf1mbx_-q14-igoJoFDMIBVvLuk9DhQni0kIdn8u4TxHjgHCWEPNTTOijLzUYt3dEjbkewHJJ32g4K38Imy4L_Tub9fJUYimiL-JL1AUNdZSXkVt09XnCtjjcgce18M85zWGf1NDUJPm99c0IjEGLgk_Jsqol02id9MsuqkMUyhMP_6uzUXNBHSYyNQQbpOs7hU3eYEPAwSzSdvpNwxdo4KOCT6nybGY9DE6OtZRi7Ni0PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=BEhW9bsz8cesGoEsa7etV0t40hlmHxhrxCosJ_JuP-EIYxksK_fZW0oj6hBUvgmoNCEUQliXNQhbptqpYlbMQbFNaIDlOZH_3uSOk7PR52FBjF8WGERbpue30oKw0GYz8dxirWlQhjVVh2nHKpNP5iU3RblitMhPV8az1xX_0sfzRqkFETxKGxGfd2VTAP-pYt70_0lqUNRKaq9WfX02ZWkyZIILV_DZergHBbJ3LL2gjKn98IhPaD00zGBtLkJuULK0SWY2zqlhDiatojJFbFow3tXYoXhbC915pCNc6MSpuN7iR4K0XKFJri20DtQJ_d3QO0-SEzoMtgITobLT5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=BEhW9bsz8cesGoEsa7etV0t40hlmHxhrxCosJ_JuP-EIYxksK_fZW0oj6hBUvgmoNCEUQliXNQhbptqpYlbMQbFNaIDlOZH_3uSOk7PR52FBjF8WGERbpue30oKw0GYz8dxirWlQhjVVh2nHKpNP5iU3RblitMhPV8az1xX_0sfzRqkFETxKGxGfd2VTAP-pYt70_0lqUNRKaq9WfX02ZWkyZIILV_DZergHBbJ3LL2gjKn98IhPaD00zGBtLkJuULK0SWY2zqlhDiatojJFbFow3tXYoXhbC915pCNc6MSpuN7iR4K0XKFJri20DtQJ_d3QO0-SEzoMtgITobLT5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9GEb7Ps4pXjHTpnNzzcHCkzRyjHIXcQCjoseqIOFCKYszrGnoTehAYVwsELuuSfdWrEPwgivEbshc6p9NbdjNR4jV6vDE0aWe4uhf9S-0nQ8LHUqPYvlJnmRypH5NU33FuGzylbDKeWa3l_99QBsIuXzdDZetdbTwuN2t0WBteKOWmcfGb1unRr3HB5bf-0VaSja2eEizCrzWCTuj10Th2R7Bb-ZAJxRFWqCDFarEomd0bYbqct4sYGOppXDZCNZRgISn6bJRKirTC1QLh9Rd1kCCL_w8rB5uamdj0joxD9t5ql2d5PJoONFWjcQbNrnkYDR3hWY1_MXxvV-KgeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMh_kcVCD96WKnltBzu-0gQmw59QRBpntYgravuNxGz3_6CVPRKazx08EYSO59MsAmXpdSUmljsRyDo0ZTisGbmcWF4iZxrFdbPEjTekGpS75uhYdei5XXUFyJWIjZAyiZmVYlYSbEwrHmyjdAyePmH_IFQOjGiL2rTs3I0W31j14dUkLD5HMUfI6-C-zPrx7w83ye_ojX-TxWtAMQ_3gmTf2pLpureNO6QoWeuLiLbgUWX0aiNmy-sTjQ-UsV6v_PLS4vDGYRRo2QzPTluoc6N6Ku6L3Nnjl7YGLm3Pu3L47hV_NWcFFjOCxSvzgV16WEo9jx0XiOGF16FimraNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lERW3y__8GBXpl4SZ7O9D5f44V7nL1uA-53bH5MrhM6o0Fa2uxGNwu280PuDpIx3ON1bEKUS2MHFGePuDBZWq95kGhKuy7u1omzqP_bjIyFR_KbFyzlt3hl88lQlta6ZkuB3jriW2n2p5geVLd8wyxNt9EqNjG5o2usL6K9vBOrPHek7D_Br642gwWaxX_XGQN3l5C58DYdfSbwn4__ciEA9a7AxH8U_nqvdJfsPs0Ux_NqXnCf9FE_haeyayNx64H-CXbNj2MRK9SckuLS3mzNumGI_1vEQQzZlJsZS5_zsD5N3lJiWVTa1QCIunXy792DN4h9BzhiPM4AawgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePtbIM4y79iaz-j8DliYJ1RZ-VNpujJMgwJQYbcY7qrlQ12_VC0kNz6s6Qfvq0adCKKucuUWg6oOKqcgc7GXGHvda9UdzLBPReICec90jDIYVphuKUxhvTA_IpfB4ihUxh2tQvsH1JUbRRCbpq0Y53MY1FfD_DYdaagthn4Ln7_xKmYD7E8bQudAq_Pn0ZfUWP7ozqEwaRuwPKAKYcsWxAlc3b77beiDNGhfldJHjKMn4QsjrKtDepyIZGmtF-DcuTloS0PqaNZup1bHojRU7WewX3miwxY0Pb93lBlGpQuXqkm0PUv3VaNGMUGT8DZmiNrxSP6IbAtHklzIgy4tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roRw8J5Zwp2Q7RvWc6kZhcDvr9JBwTP5StDHdH-ufg-aVQjV5UqL-BzDZGsoGP87Y6YdZiJW06VcB3n9kO3d3ihB0F3qmRk79Y8L4JPkR-eShSqRrf5BctUS6rkiylLBZqnwluS-oooXrQt1wQ_g-eac2ZpiKN66cxzhWYbqZgMuYyVe1tO3rTem4p7v4y7fnKsmechgKhI-PLoJct6E-R73uoncY48YK4_RP43VgDB5LwHGSPucJpPFfx8Fbkt7OHCw5iiBemeHebu0Fv8uCD7ht5LdcL0L4CYwK3ba9gLVXfdUcZJlYVi79pZ_MmDXkoI59er6haVgCBW0l6qooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekeV8p5rw4mriISS8wL3RGqQ9nuKyHvdQTM-i-FM-oin0YfCi4KMm-XM2cfuQ9R0cSfcY6u1TDmPe9O2C7fBPyT7-7d1-TTEFDYBA3097KM3TKTVviPMtAl6h03JCeFV6yZI3hw6_XOZcOHXXtRoxdcjUZPEs4iTCOptYgT-3p64jSH11kKCBWQDWYZqKcYT8DsqfTJ0ecKitrbA-FQBCMlNFa32yaBHZXx5PyUjN-UkWZx5EqpcjzesATuOcODzBN3T5XsKX_eIj8RA5TJFvGuAdFraDKA0l0oldX94zky_5ayVj-fuLmyuadMeUsG1hezPBIk2OTewzkvksZXsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAOFAwY9s0K-ER9XA0S4lUBRys3WLBPEVX-0zX4rQtiaY9U701Ezx53plyb_9awen_VeuMpxweu-as8oFBPvoKn-URyiJ6qVjT5-snaUXBRdqKayCfRHf2SvnaSXEWlXz0YZtFD8L26ZSA00dsZdCs70vGbISmzSKYTPYLHWQYmG7KUG4-VwSHtA3t0pD2ATWwI5qWtlHZDg6L9D3S3QnmvHh-m3S54t6bZeHiHqxS82SzCIJys8an9Q2Yf0jwqLzdXmaIJ74ydPia92dI-VWqfKUV8qYu0ecTgxEnWTP8ffjjskhvUdGmbz03UoZO0x_HsZwYTAFGLw-EFS733VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7QjiWvBC-_RTIGlKuZWkB3LulBS9r4XoeoJjjOLrVWlzeBHX39ABHAb0S44Ynn7-ey0U_IPzQzIQOm0Y-PznfjrE_Eq_huynIiL_pzTGkQgDDp1HYSR9tKaE1RNVs-e4E8OcI2jdYWenA3AYgmspE76ZZBmD8s6JlneA-JmnIDjROQHrHmhUecycAdj-A_Athh3qmRQlgBFncrlWnYkXwq-EnWZ6zCAxd1WvX7OO_m7np-9I3fttINKZVZ3evJlA_VHKd2uFQGX8Rm964DdE3J1qmQErgdBcFQJ1ryHqhfw4a2nB6o44-WqeZXrgW7pS1IKVKFs0EpGHwFjmdGsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brROGP-VS0dNrITnjgw6ygnGflF3JSNq8WQRxW4UJ4s-PsVf-ilvweAKwfiP1gBnGvIgnh1AV0IVoYks7Peck53CQJDdfT4x3MgHs2fcgkbENxmTVP-VZdBZ0gFbrXY-gIF7kK3sOcFeIZlnqAic6u7203MYVP44xjFXv7rTZEB5vI2jEtd2fdrb1rociuJlg09tKoInEbO5cnpsCMkCyWhzZ5q9eV1jh1-vh0dOmTrJfd1XUSUlJ64QKmM6_ZMxHjJ4dm7u2-vPRnFMFxHhsK3GuAwN9elfPUHjCnbxiz5bqcAsHvi8RnKldROWOEfQwf7kU1Ch3Bh4LZYQQYK8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da_Np8onFsu6WXZdofMCifIsmep9-1iCx5YdvLagxR7oOPyuDTHLb_rITrGpWgszEg06HbucOmc5kiz1Jy6ANqGOEypUZ4n1zx43-LMyJ0Ex5wU7O3WCRx8KhpcL9GNoW3Z6lsHdod0cHePggel9eygDeVjuhQW1Yx1Ee24oMQHxG8A865MTyLmuFSvEzTlWbuklUWVRRVwA7fxY9sVZ4tG9AurN8lHt4oc282xC5AWEEXUFVbiwORDA8tzVk4Pfj7Ob-COOzx4Pgjw7ihrF0AA6HmdTfhuG2l5Yf04oBAIMkFlAHwlZDsVTKJzNsT5SYrK41rR7beGfdlFi1-AhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orFmUM2ygPKvWxE66Z28upcLLD682WR47DLzITSOT5MKcAKAIAGOSWLyn3cLXhfnp1nz6KLMeVuuRGgOQ2kdU9poxlygHRYHcZpOwQF6W8p3QgPycSEXUoZVnpnwp4Uody5xCTLHW0aqr2HrF9XKdX71T_RWr7y4-f_bxUv05fgGcpjWrd8p1f43GWNLSHz2W2Hyh5tLYDEb86uRFAI_PgJrdeRCmDMPrkyPmvfdqt10-CqFwCzfjiLXndEeARLbIdZluvIwes4RvvB_vmonMaFLNR9hFX7tix7E5b_JpAD9dRZAcEXqSIDkEkuNm_RxKpzR0CfhhsKHWwA-2H4jjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdzSfyZrYBWB5Zs4rlFN9ssjW6oTY5dSZcP1uP9j3gchyLWPBrTZaeNFQp8YyvKK0SSe2Rp2RH9v7t-wkJXgqogF31m9th6LNFrThp2P5hEPJ8089j0enJRhwHrQwm_p8lHz-IUvkUXmFLavHnkDSe49_4pLr39RSMVmjf7Y1RaCsaAojOZliaC1Tn2_vNMPKpdEza6Q5eGa7bvtMOnVoRJOgwRgozahtq9OLHUEowuf9cL4NTKapS__OttM5D8av80rAB1UoZ0lnUwvXoXGuNZVumEODugt9fn3fOGS9ELESdc697Yn2ON3XP_v7YygBaFDHBl2j9N-rceyn39noA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nptAlbylYylGU3Qnmc55Nm-yFCIlEMBRawOQeCy6q-VjzmefJ4UeNzpI2L7szlvGvUBg93C-KuSaSPSVdogmQEyPPODZSRht_HlZulFxNQDFyjCsHQThVy4hySeVz9xtfdClLhpP7zIcVwymEK4ue2G5-Q2wz0KcuutFi8OQRSFn-fLHsgFC38AW2mk41vpw8VL8X2iCoR1NXFysNt4hn2Fo9QmGQsQqEHN9RDp2XqYdZ-2fnbKHVpMgJvhp-SxUacsar9odZHevXTNXJ2eG7rSfGbc22tdxacr98sMeTF2cabJAqusf34nf-wQNPNwNeK8lSp2lFY8I8m8xZw8CEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
