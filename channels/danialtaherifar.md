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
<img src="https://cdn4.telesco.pe/file/DfCVtTC-EkH9ftKSVx8-diEae3i4M2wo-Saht_iPia-2c578ZS5mUSuOQnzSekdGEwBNrIztAHhhwrns8q0JoPcDVlhl-AfkDyK5A9uTLh96ar8hQWnJJBL9gsRboVyLGbUQ-2Ab4ACBkBrCX-eVsqok_LTxD0_H9kVedpfKp6XTXbXQYmXGsamtEucxMucEtFw2QJ794mp9i7eXVpYqRuatzobSXDAl5Bcl_f-Ed2aTPQ_B_mCu94SV7yAZ-JVR9FL8vCnmT62K7oHnr9jwEqVV5tiX_BjijLqtXG1IkBbcnoJt4zbT3doZOMXBtyVD4xIJhkrbPt85j0yj-GLUJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 282 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 471 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 493 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dsQyR0rx423hr6DegCG-dNeWKcfOZRXvn0hglom5N9G-zvBa9QdNroY7xgU7NgKfUQQ2_43rQMxfO2r8nBHyX-dSGXXXR8FJJSfrSfT-bVUmiB1OI10fF5W6ip_Lrx_TO4E7sqiV_HoITJYnGnOJ2_sdhDc8WvMy1dZVlW_ptHUoI1xekazUx9ZPCO6_EdIbme9DsUgNT-5XPwMaNkIy3Xdg5UEApGHkO1P0_-kFXJLVQxIH24IZNCH5NJx_mQH5VjiISsOwAVaDZumUYLt89Ic18tWIdEvh7SrEmqksIRhSUzYcO-VeRje224FvKUxloiuWR8Rt-Cp4CWa8694VYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dsQyR0rx423hr6DegCG-dNeWKcfOZRXvn0hglom5N9G-zvBa9QdNroY7xgU7NgKfUQQ2_43rQMxfO2r8nBHyX-dSGXXXR8FJJSfrSfT-bVUmiB1OI10fF5W6ip_Lrx_TO4E7sqiV_HoITJYnGnOJ2_sdhDc8WvMy1dZVlW_ptHUoI1xekazUx9ZPCO6_EdIbme9DsUgNT-5XPwMaNkIy3Xdg5UEApGHkO1P0_-kFXJLVQxIH24IZNCH5NJx_mQH5VjiISsOwAVaDZumUYLt89Ic18tWIdEvh7SrEmqksIRhSUzYcO-VeRje224FvKUxloiuWR8Rt-Cp4CWa8694VYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 536 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOdi1NAY_Ui6LAfABfCkNhMFxl0ui1G5aazOJ31Gng-29MWOXzgwFGiyPPUTtqSDczpToVTiwphcAy2otdK3nHIkjhhthBUaEAEB7s1KzZDZbXTqJVVwN4_QKZrkSuNlZJQjfjr79sDJPyLxuvdFpc-cqngC5D1Wuh2RHirPctZ3tYEZZnPG3qDe92asHW_AmWRp2ZWy3g67KYLwQ4gLJEGqv8zIVEczOEyeEEONXbguD5x5YLg_w69XlTKYzwOXHYz383v8jf1F0eGRCsAC4d_tem8gFySiAZKmy2NRYob-qLRH39-kW3qLOaGUA-YalJ_q0KvzmNm_tg43fkjA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 562 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 764 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvZ7i_xJmF03rh9mUewp5osyFdLfx51PB9h0gFtjqDiQlvuvACo9CExqwa79G-BDNSKhVhz-nadbsrSg-iSbNa3ly-LcecL0DOKeyAlMpyYpzFSsmeqdB6sxhYbk_JmajbgzlI9NH6UGi_VSHzvYN_C2X1GodN8E-oWrM9XOhL31VloRHWy5co4JsD5_8fBzGiIcHaCWgJVC8_2gKKMpp4GeRYcgd5-sKzXHz0mvOE1cCziXq10Dq_rW2cYaMARDx9WWVI14LEsWav0hfF1VlBTqTvNuPwqjVS2I5SCVcuIwWN6LXTNzCT2_yvIEG7cxHVV5k5qOskfoLKZ4CiWoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5W5pv-CrvOEW7vnXzYPvSxyiq2r3rr00TApHW1ruNcBj0ZECIVsVVZY9kpCamUY30l4NRilwHNH-5zKGw8iHohcz6CXKoxMm22W0fM3L0_mhKI4t-0PrmW-NZvjTMTw7XpiNawFiucb8VmJwENY2R5cSf_Mgtux9Z8ag3rOmf1K-LGcQC3j4uEteQhCVWMAGF04MzSjF4TS7pSoVLrZMnvzkN3cnlzJWjcydoDNttViAUZg90Z1nENygx27lobN1vzH5PMbKPBIy2B5jypXpYOIENlaByAvzKqUgD_ANEXmb0hOnTGCgoaMZZDokODFxwk-Wbg9tYFvbskPtNvsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq9cOPI0yx9bHVGtYS2zouFDRWcSgoz9jGuYKb2NobxRlDWggVSsfwgnH4ZrECPmpif2lI84X7mXfMkklJQGSxa1P5ZFww0ip_J_2wuW4lK2Jaopf6lwu_Cq-zAhNfKt1B7h-X_zYu2D3e633H8RwFu6NnNyB7tKrF1RTwfL8_uQG1Usjn7fDUlh_eXpQ7WYkpt-BsbBiF2PcLwnaHQ4veK9RJeOabi0M1jVCRt4bAaKNDHhmgBCU8XzH790EWh2HnpkBMsRs4Ka0BiKbqkdNSUVaH1TVtgTTpLtahCZE6cRyghGhInieTcDETsACFBphRm-2DgKazO3XvHR7N9sXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGSjjOBePgoKm_MJwewN0Fdq-Plcb2WMJ1r6VANM-mZVnVl-IhcpPnhR46bSnuEFC-rd_ASabBevbh8Ky6rGd-s-bjc7C69ugDh7MVPlopFAkb8Iymz697k21Gan446YrctTHA2Beo4khnhkH2RPv5cP13mwxS87WyVvRdvvFceDaywOtqnxEfg7Kxn96Baf73pqkV9Iy0vn5frAM-YlsYirYRWjEmGxR9w7XA-vMOeIdm2CECyYmfjZc_4KDlfjfoOqEZKc_VFaZNDoJ8QQhilNrsig7YXo089egCNWBmBbEBKao_kjrriji9T9r63AUw9qkZq3fVPBXG4aHL9DxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw-DF2W2mnWMDC_NVix8cI9iJf4CflyvRvFUmvlUPrxRMBUzcCfueI0cczPpQYxZIJNEnV1t_yMz-h0jCWLWxlH3kK_mQE_4LnACTzOooUG-l2GM2xouWm5U-CWIO_9RcMpwf2kuBrQxcg7xOq1XXYwATqcW4bxb6dD0tJlbMQPV3Lg7elk5VLECeNQo2G4LLEfkymkK6mOu_h-pKTI0iLD9jx4_ROtOQn9bPvLwx0CNvl6ifSPVUBCd89d5JQm6UBTngz4KrFBw6HX8vatrMuK0g9xNn06Cda2fzt_Zy6D2p7L-6y3RUCWWFTP0hEht-cpeTmeM1OgSHUyDPWhHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnkK08qqxtzs0PvXSVVbTvaQ_Z6naJ-HIfbxm7r5p6z7Pbu7A9D0vehVgjPSuazRp3n7KkwVZo5bCKv4VALKjR01XnICJTa_unF4_gjtgKBUGfPaPjpoEiiANK1MYoBfB9L-WW-ZgyZplRGQpot3PYytVDYH7o65FAZ8iJbocbItjst__J0CFGlRxd1GN9bDwRqyKqoFVAelImPO6kBeP-gaKElnwP4hiVYf2zUnhq8630dUJNYB4imXe6m-F7fhGv3-WLM4LBfRiQM0-fHxGxs50h9NZ8yZZVE2KbObSaBqSlAHOT2WbyZlPGBWyG9i6O84pj-iyGaU3c66E6zTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAmpWwZwaQsjC5uAMYu8hnIOLAB8jjUwlXL8YgYiLeHIJ-sH1Q2yJ9BH4EyP5LPbehdKhyQQYfG8rB2vUq0H9sv2C-WZ8EuDjj8XCfdLMwUoKzN7SezzsYuiRuEYt26MucOKbCh_6OE1b7bYPf0K9kdA53EubbUZVW3P1tgfneOfYQpy5eXThITMP4-QQU1V0Fjk2LijXgTdC3PkD2eO9pSNeF9w55uiHaK2rIuppzmaII-p3b0fjnphBHKON-tiMPYzacpkP7EjTeYnhATjKPB6dMHRqV_fE7Bhtfo3Jpvy7NB_SRe0LpfK2r__7rs0wW5bZiTTcqpuDg5QfBDb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pf9QXg5o92n-vL5trDAFn0ZvfApUTPnUVNJkCVjxmT7GvhnvRzSyy0k2qReITRIk3WoSJ1QMau_VNHFw6OmstyFSa7XSI0oMBQLHztjrGzX2sWYJ-WriwlaiMDHeX82jKTKLeHBT6QU-5vEBTqu_gwqonkYbyq3AdCqaf4ag7s3n4RzBt0Ne1zmC2-SSwaOmzqcO3_F5SGHtEFvuSBvDJGpUYvGkpFA409vw6lY63A6yt3nuLhCtFXADNBQVL3QdO3ARIY_nQ6NiJmMY7FZ_0Q2h4weIuJ1v0LgrDNfn9wLCEoG1ixByyWbOwzqdGDFYZCWfE72b53kqJe8W-JsD7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5AEE8d3kLhbPtQDnAVvi-fTkPiY6Xd_LTgEV8XYZcUMpCAREgKtgBI5pYJx-YFyzWVfOLKKHR-rpvCRG3zuyO5HbxUVcek5Jhpk1n8wsinfQ9MXDAHahSSWHkEf3S-xUV2V9MuYWZuOataYpHx5pGZV1AdC38nSFIDKdjOwXGYbMJgmgtr-AxZBFdKzo9HaGsgcOOp4kcpnfCaHtd5wpOUaYMw1fJpuqJhQ3tkzWJkv_1m2LWPbcxGClhWnKwxu37_5OeTFpOHOSeiugBe3m1UXLz2yudYXB7gI8deMUQxu_lgSnpctp32FUzCbDvQNvO6HJ1hTjv8f_ks7l703YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwxYyQ_93SQUhl0dslVc1AP7gmPYGyhU1u8A-tcoXke_HwVOioKvNvRtYljKMoqt6LcIffubb8S4w3hGDe-rjF5A_QCVU7QsZyEotA8jnFFs_eZ6FAYcYkEvsjxBEsiTDYeKepRcgu8ZAurtjyKRe7HMMdaKNQd3WGu-AsOdambJMmuUW_82baMCcvLckva5NLVjiS-OsjK3n3FzhIMgaVXGEt-xW3nKR6NpooP4b6XZJ19n84r5VCcKBDN3yAuh59JLWbe_XeqKktktJWNlpEPwc6U0-mo6Yjl0uzXx7ymVQSXEYIK7_vz5wAs5UiNXRSJanXfaA-2u73KUMCoqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYhTyir2uLrj0w5sF_eXt9gwSptrh8c3MdtJ7Cx_xouUucv85zfXprageIwFYZ8w0YeV6YFNIfsYpFdRzoe3vKzZFWKq3FDOrlmA6qUTtacOjaaClMt3nBJu0Zct0hCI9m-phoIpP1xnTk1SlsX88RJhkFCbnz-ztvukhAXcXTlg_exVLN4hUoWgtuSAzMvuKg4MFhtuv_HPwDir73mSGZ0NXmhGouX9VWP01luguHFFzdsUyzKN1i7lkyaMMZ-HrJpvIs-dH-OjGGRoVYPnKhNhVvIDN2w2Q67nVzbNSYGHPWmAk0TDTnsQiJ6BMsG2XSmgbrKEOF1t2KM2NX6h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUGvjierqKFTwfTa6pzY5GKhWDVOwOfAgZ5J8aueeOSqjp8umqkAVzkf5FTAWL5MLNqL5yse608qV32tEAW7UgOOMscMNh7aA99hLYsFLi5NZ002ZznweaO9JhIiOOMhwbVxpgXDen_a1tikV2nij-3nnyHqtlGYzH0hnxoTYleWFloZACAgrC3JIt7sGhNa_aSFphsPUB9q-Ut6Y8ENejQj351bxFuxzducwAaaNf7BddYRLrvrIElh58BrEEt4eHeL9dwHH6Cf6WcgS6vFdeyV77TSW5MS-VBSjZv9ga5H8DpJfav3vPJM4vc_BxPIJhIslaO6m-4JAIdKvplRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5CXv_OUeTDxE69_4XZUIuXRiR3jJr62kUm4gb8keQsspteeeR36JxEluSq6wWwYB6hwQoR8ucaC5m9l49N8KysqXqqgfJ0wHdYiBgpB24aqJ9OKrWOgjVZHuZS363xVK6RcqRwjiFq_zfHI74QB5YU_AwkUVxlHkrfCa82ZEwodqwBkVpAUoskL4VMMr--EHXxMeLCvuySA_GqZR6c6o6MCER3Ip2s6sGtOTPJFZfsGDHVBps8vAZchw5OkP0evwdIE5fYKa84iGLnzyGPJOTc5JKOdAGoSZa1LAi67W8dVL63AyW_DE3fH-0gMEP-0xz2Z_iKj54_OA9Vl4nW2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxtWociXgZJjMGSEC5TnBeeHkMQxO7MDdbd_Pn_yLXvKkHSTyWHAHpT5I-g_lciT9zTv-ubTkNGWsVYziqxrnfmMsfut0KShHlf0K_pHhhQWDpCS6nW-IvX0b5eYjXbI5nS4uENWVR-IrXRtQ09S1Se2-hYNgBk6A02QJjf1S_6o0IKg1XI-jxAtXSg5T1CNtqTvevPKV0yKVes3yMC4hL-jX3h2JL0EEzHArlw1iJm7GRp3iFCeVAa-MR-Ga2-JOPuZ7fil4OMvjEy-Gu5txDKCxpQQRd0KB0ybXKEZ0mXxadSaRhZzoqyN4ThgW_-fETcFleiPJu04ctaX_l7VvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4kO7y658yvXzQ91ZuAauJWsF8bNYDpncN9YMguBERKtwhWEXwr3Lc1y43oqjYTj082MC3gnkHa5phLPDNAvTvgsAwsEmXCUvlLZPtAkJw6cqctpyPSFdW2po1vXDL3sA8lGzkmXJn-lAG_4Ft7wTnnd1CVDzRDzYtrCyReuo0oCxOP2BMasrblbVQorANxgqDpBLztWegD7WAVYjl8M9QYenc2XJESjFd5Hm8Mgv2hUpoZ958FnshAsq8sZPQbQZJvZiUThD0cnYbDtEm8zAYjM242UvifcQvSIrlOObQAO6mJ0cEhpINBJnS5DvJsLs9CCIbmANVwsYpDyvilSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVxFqH-fnXqQ7ccft21v4nif1Jr9QTjtpwwASg2-R2I1xV7t5GKQeZUQWich2pc0J4Y1RXtNA9PS9dLzVBC4hw_3Mi-cjfnflDFDbupZAvb6isiGAG-5ySq63bpdifhfG30tDaNNJiLabNmRTY5RhODqXvypmzkQQceFeGIfynx8x42wEO1l-7bBBPDZYiKuXC-8sYoS11Fg3b2GvSRWsBpWkCCeAmx0tnvZt8c9EK1UkYGoYNcBknStKToDdFfjcUUrJOPjuxx2d1XalZQdb_6ZeN_69eoHgmW1aLXchG0q4ta2zG-2jYhzT80dnTdcZ6rH7H07oY5tIq4pqDX4mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qedEu8gck84moQcrk9I-fooNjyvVJI2XYOjzDL21vPTxJ-wOeNVGoEKXOdp3sBBGPeeLKML7OvcZT93rvU4ARjgl6QBymW3mSPszh1VJxGeDn6W4RZT1WCyS14PEsJAjruyXhKZKtl6HyEtDXXngod0A82eZJCpOL1MENPXL3iZ9xJ4cNvug22AVuVd6KCo1T5KYfluEwFHvsRdnTirNFghLTpLS-AbgwY2-1O8a8pL6vxAG5A5R0e2Jgj_Dz2Ie0HXICNbh0ZlUDTcnpf_O3VwOl6N2TJY_vuNmxF_ruByT_vN60qFML9wks2004P5ipl0MzfTfnlrnFixAKRlMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=B-uJnz0105Kb-6sbAVhoyrG1wWoHbAX0Zrw5dXP3dg8HCHl7QjxwL9bIg9K_8r5h7uz5-JYyk5JVqnsyHW5sZdq-Uw12tw2HI62fULiubjn4hp7z6rGrCapMdlTpIcPUt6bOsq-ohShNjnM64A6VTYja6HV-lrica7SrZL_HynGPNs9etaw66YMRlgqyAJIv0zjra7RltqquYrJ1ASo6vdC1F0LjfO3RNTrGfiU_PGRSPeqBrttRu9JBoUMxFWz9yW5Y_UXYUV4MgXkD3ek2EVYZ_EfZUnbRpVRl4BmVPYiAQ1Fh2i0v1GQkg9JxmO22eUTIr0MBpkU1rm8cJAGXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=B-uJnz0105Kb-6sbAVhoyrG1wWoHbAX0Zrw5dXP3dg8HCHl7QjxwL9bIg9K_8r5h7uz5-JYyk5JVqnsyHW5sZdq-Uw12tw2HI62fULiubjn4hp7z6rGrCapMdlTpIcPUt6bOsq-ohShNjnM64A6VTYja6HV-lrica7SrZL_HynGPNs9etaw66YMRlgqyAJIv0zjra7RltqquYrJ1ASo6vdC1F0LjfO3RNTrGfiU_PGRSPeqBrttRu9JBoUMxFWz9yW5Y_UXYUV4MgXkD3ek2EVYZ_EfZUnbRpVRl4BmVPYiAQ1Fh2i0v1GQkg9JxmO22eUTIr0MBpkU1rm8cJAGXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0s7tDPiBKwjpxorpbY9fpyp9lqi82ENXJdvbFr9hrwgKSqGgObfblPmVNk39J8KRGPoZpHaHS3gzqB5XkdxHOslvAyTTI3OM-u3zUtc98xumRt-KFFBZhQ97QUShu22UI_CLJJYFTj6rxTgClyBfMFifh0jMwD4YUTEil9MlUfeVJmMPYZYOmB_aDQ5vXbIL4KhLU8Hx59OUp_ZvjRSabVV3L7-VI-gMOGC4G1llHSu9_azbFa1i6rjQlmoCL1yN7ScE79eqDQ7kgbJ93c_90nwehy0m_mr97E1vjqKtMmXy1qDPO8-WvgsYyjx-2CGuf2DXJlinzd5yF-EUyCyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt4_bMCWbx3pouaqh92f9etqhdHfZSWYKyi1_i1MbSEzKpSYnDK6pYO1P191a-KNxCKTj2aB3POkCU_ytvtXJTYHfd7nkTXcC3Eu49dfFvp54Lw7jn_qe3HifEkAYPPLenP3XDtkC8wkavgb3LP9jBb0URVQN1g1r9Zxr4XEY9unq5FkesaYgKe3aSYVpupwTbyvfwGUj3HmQL1ZA7Jl0vU06T2ye3xjI0-WCb7a9xQRSmi0LR0byFty34JHQmh8CvPF3DC-AzCmDURRNVy_Fw6-s_EpjuWPsF7LBlW2FgwdZsMi_cYiren6o5SZ5icUOrSCRr8xf87l0FRHk1cBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4lq84O_q7ylq9cgTqfAD2z0yrZcoZ4vPTN06culzLzCmBKpv76CYZ3jx0Z0pb5Ygd9maYjrYcfAG8WWG41nYpVa6PNmONogIULv-81zOgBBwHJu5Sq6M2sAI05QzAMIzvzBKwyEq8I7iYxW_dy7isXuKxNJG6v3iSF4jPHvTC-xf6DTXeH7-mGm2zEO3VD4G6epz0b4eo9yH44BXyrWs4mvfeGM9CJinXpg0JYlFhFL8xNEpCSM7-Ho0KU335Q-S6pj_zkwXit8vtfIzIz-SgGNb994eWzGSpyLMsLNSIkii-CK0UbBy8hGeub2ft41HqUonuonBUF6rX-V-qdKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi2_hYsC8wSThfgv-xhkMHUYZic7ReAHdlRTTQ7o5oNFE90JQ39Mw0hgay9NX5riQM2gYwqXAcOkHFLRnyb9POJFXccJUjN0t_0nUTShH7NGo0DyomjPg--MszRX8azrfe-e4BXf_L-EEcouUw_f8VApz7kvulN4kPVMC2qzxv7zqY0XcoeXHdod2L5VbUo2-fNy2VM6dxvWgratsApYPGctMIW20eDuXG89nuT30mWVMsvjWn598d7zc9CU9BLyjkmlEwy1jAZFbbvw0F2JSMUGMZc0saA9wPLHECYpIH5Ik886hbGKLJxI8oDFlIkAK8eJz5EIDsOrRD56L73BKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NleMMdaSoFbMZbZOsp5MCFR6RJefHcvQ0VwLp24GTQFv89h8b8if4_JhLUQ4raURQzKbHEmDLhKpX6a3KEZCYPSMMUJMDYyUcU9tFcx73eqpLWZ5_Q7QNf1wlxvPSCCr284ZTD_TN0jqb63CiTx1qwxmrtJcTCsYB5GEj9SXiUefdfrYSDHEG6H_gyjEQ57R81nHX0yXPwpAd_19Ez2AE3ntbWUZE8R6LjmhJ8qCZ1G5-zAgrdkdnPSlGWu7iH6f7N2DNzaFQiqj6E-Zmrr4oIgs41eaC2e4Qp2g55H7H2uX8NSFp5mywieXkjnQ3wNgc1USvfbE4CZ4RE7cGxk9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps3ZLaqx0UmfzjrzGL-VMHliSBB99xiEoDU1H1yywVa5TZtDuvZKgtuZ0VrglZWSxzh6zInM8gHlVuSKWNuAjvlV9NoEgwRto8mXIqUWvai94NqqkaCjFEMWeLkBtxrf2PlkK99uo0YlVZQvJpQFdXfOiGXPpAdxIScKxaLIDN8RTPKxQDm1Rg2vlF4DO5z-gOTBIkt2G9B929hOki3weAMe-SnQfXQoFrrCHaDMNMV7fCxuDCMFmQ76_9UIQ9z8qmA2_M6qliBjnyqR88Qu-PCOjcpz3r3gE08TsXbHeCgg1V77SA0Gcn5zVCh3d-tLJjDkqlh4YMUNBBJJ0rmmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRrvPDZduhkPCUl4h40o0tLG3vj9n1y7-qJjpp7rnfk-nOmuEEDhonBMO13FvJ5MtiMnixfG9cBSFRmE3mWJYh_s1RmTxQty2dEVia7pLUWqhxhLgbiqVLDtcm65bwsapl5-N4J3AKfBW5Apgu-mV-c8WXyubJZToa9aA3ukNAdTNmUUcR_oo0AO_nwQuRcX3Febsm6YDSrfZyD08reDc-JA6pVjmSc9WKB7AK2iNpLszl9kPvoGa4Av2JEDnI1H7daccSCXzGQsAuBn3NyqouCooqh1ckoy2oeSfz0bTymW81bYO9OMTbi-wiiwGiKA6DFvp1VEozr9a0Felk-vjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qk8HFn_V0atm-x-leTmdActluN7v7-MVNK_iqj5PUyOJ4kYG2EuwR1ve6CxdSf9FIzCcq4S_cS2-jA7qxHamQEVuHx3G-zTBv6e102g7aHSQg44RRGBCKag-S9YXpsa-XkOO3n-axmD83sxMcEgah-KAEq8qjZHjwA3kku-LHg8RmI2_4v90Bw-iNukF2ggp5BJUqSl-eu9Ouv62FoIG3C3AdlFyMjZd4Z_95wCEs3F5L5FExN0v-ye3jcAuo3TFKyxaj4-kbXtD4E-mAaxkoZBK_T16s2Gd5ZisEEQbLIPt1DgGJbLIJ6brJDCN40qNSHoEweumUvFEK1OhkDyeyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUCZUhEJSgP4Qxk-_y8N2H60Dr_XhYIPJe8pV8AqUDiGf6rKZJdFHqMeVffkY15EmCB3PtW5wl0fOmGu0yHDWZrJ9NrJk4UAKmbiaJIS84Jj2dyumKK_NOFkCAw86tQZFmwpZOl27RgUdeRqHUEGnIKc9tXCQSwe5bp9wKGtlefHA9HE8V3b2nfsXxi712Mt8AMzhL1Q7Yr1oXcezAR-GtdmzPddXpnCaR3UKWxSK7on5uIAwh0LNrFktJg3BiSsY3YEVyfI3GfAvTAxo9Lpf1KyAa9SOqxJBCj-ubgwUtwMY-EQDOTOmnc64Nlun7vzA3gW_aLnOQWx_gKZ1tjsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um2WQFCNIUlUClLTWw5vG_ECeT03KA8UrJ2uAiYSv2AP_p4nPB7xkmDf7aNlE3x-jwnqWve3tzT7Hyd-jHIUyUc40DM119TsEhcdAs6WFAQl7lfnEq1ep9TYCj4Em_vqfkfg5JUkAV46Of6fC5GamFRrG5ihmv7pLTH5o2eQ9ITz8RvBxwOFe1NUTTSbP6NpA9KXvckFtjDlCNp93boBoyo0esJIRFvN8FaQZk0pc7ll5pRjYYGVmuxIuKQ3J9wg_IWpWiunjT71ppf7AR4fo4Qhj0q3f4Fc-kPuhw03a1tq0hrtbaoWG7AuZVOw4aCMeh0__X_perOFO6c1lFx4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuwntxin2g-7so3k5w8Dfqyk4Na-BoW_oqf5iQWQ7Zc0Y8-4b1Li8Kcer-FVh-AorWKIhlYQavm4LDLgH-BSlcwCqQ4vmUaxCl08XxDe_zx1lobQ5tU-hrlokoxAXvb75VeX2DUU2nzqfAj0Nad3UzCAkietoFyZlY3KEXNpxhEM0u7jBBwAVQkETH9CDIVEzejKd2h_iZEtFhGdzF7s6od0wtR_fuOQ79Abo76IhFlJUN5DFSBa_SLXdAcfSTRj6UZ2GWTDYdQrTlo6VzsbV9MzlAvuw8YayhLe9_C0U3IpANAFqTP3gI9OggNqJ5ch4x7lCR4_EHc04qFJPUMAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtIS09ju_3OA0QNxQLe5qk8r10tGqXLxuIo0q1ZPTiS6Kmm3A1FY-sQABZW96RagMTMZFlF2h3OF1ZQvYtPyhI2xdW8XtU-1N_4xq4WNyQFRxZv4YvG1i8K5DjhX894mdlCFgpwFUA0qfxoQ-IV-1D5qhDuw9MeKYjZJPpfBk84hBVOsPQ_7TLM_1F55SlkNQWy2GeV8kEH0Y7Jij2qzSrb2_VWUOGRfGlRWOfUPt9iqBXJyddazW78Ww7CYCP4AwovNMnd_PPcn0AVnK3rkqX0_W598Hku35EDEvRu6JdJM1VfalpvVeYgdeizbCc9O3tpC233ms9FOoHhDwAMTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvS4NDDaUaWtisk95F-8koi3Au_HbGAutX43QOv9dY-e7XWqMtGeTxrNBAnZE8BI_HfIkh-ZwLX5PB4GKt27eRGysFpNcBQomDQFB3KFJk9VOQCilezqtidEdCQuMqzh2liWRPA0YC7JZD56CZ_qPg4KbqVMHerd5mjtP4dQb9UXayaD0hhXxk8AyaJMrqzSqIHRZ5JjiV9ajTOmlD6pV2wGbsH3NUbctmatDbkfuh_84kNlz5jjDYHwNqrCmof1Pm2PqNIOjhOvq6PRDEB0r3ZzapYkyhpIN3CK367sMHOIYB3kCvJD1X6mPDD22xktrIQ1tgZDFiIWP3HMtEzXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXKCk5jeCejo97iZeendGYulY0PPe21tTzGVwNWks2NZkGxLpfYo009es_Oe9ZQwbXUrdTn216LgxrNU28cU9u5vpqHvOeXltOwRrgTPOw9eLunrELdhC9S-RS5N7b2VVanTncbBv0pTgJk8sVc83ocFDnRndp0QRnVaca9sfbsTyUGy2eY1zAdiwJ8jYK26SavZU7Ht0o4Nj9TNL0AmtXF-DwvaoaIBA6AjTqDxaIxzYrOytjdP_wPeXLKXh6ifBw8qU-8A0P5MXX5E_BSz-Fo3Ae5R8qh6NsDAZ_ALfY9A2kdO4_9_z9fIven-VLxj-iyhE9btvFoUu-r5pYyeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfvycTNNk3KHBe2N2fHzfZXcv41fsfBcS34c_p5nQ9FDCx5xfm0awyNm-8tCKIlAHc01yMybOOpgc0H9uv___ycj08mSX-3pgiUtugDcibcaSyy5WtFaQjIQlSmiVQsukAETtTcbT6fk18OuoQbEYsykQIbcARYUnQtcfMzq03sgh8Oy6Wb4orFrkXj3L0sHogx_xz6yqutCaCXxIm2UhQQAnYkW8enmBmPVkob5NsLftGGOyhBIj4eejTtZXh_7hhf9dWuZiM1hKvbrWc8NvfMclJPu2vyc0mTxz7y_jiXiPwml44NCgjoy0Vbu3Ut0gH0yHG2ZDL8HhlPc5wuQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dy6lhJ6Jog7g_MQU7WOtR9N0EM8DRBUjnyFFY3UrY_zl6w3xg_1XS6DNBiuITJQWyjG5i97jslttiMx1Wao4Ecm-lLu-BJBabSJs3vucrA4siwj1Ocww3PlY_cNSrUqNiZHAKGEkuv53TUfe1_ldLd1Wrdj7sS1IAJWHr9njTPATY1POxiq8GoAorZlcWEqbXCqEtjcJE2zXiAFSW-n-8iCS6th0hz9zpvK8fffuC249fOIi2UowpYWW7Zt2qEyKvDXeKk3qPFHa3fobvQlnq6mOnLUQ2iWijF0TfL1N_wC3gBckw4jmbY3fIu-kwOYHJtyTCniaTfqTXZf9v7oqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sin69t6LRfaPFC76GYKcMZuJJj1ljCfO_P9OUftb-U8oWRy3T7iBLyA0I5F9n2yWYi1bN-_7HCRqX4TsM7C6JIOo5b0lBIlUkPvtOsfEfPqfuzFGmUYkDRWuG-5wZ8ktxlGMN7JsiVWPm3sBUdMcpvcVYL-CBYWhU5omxs5DBjmvxHVNV8R6Wr9emSPxldWKrECBVXWTstwDBx4aPutvOzKehGxCdS6DMkaXTsMiytGyShTU82k-o8KHCGuzi_bfWRrXvcK6otdY_voao1cQ5hUYu0Wd3rOYLixpXOkD2uCWar4uyQqv0XxlaEsQGDVzMIfkK8Hykd9Ma6vx5ndAjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVrZn8_JLB8xKsvR5lx8Eh7G0ipl-aO8J_-8GugIe59s-2FcNRkEKLDb1N_l_VGCSBf5JH92AnJj_6z3YJHcdfT3dT5wyq_sg1IwO9U_i-lmaYKiUMyHOD9PWhgiGU0437mAYV9rxaJGvnpve_jQcaOK16eoVAX3G3dbn60RrU2fFtGfbcs7nBrmv8a7Azb0lFqZym9b21zBEEwuMq6jRObO6VSNWQjwEhwB5JNq_PBtU8y7ioYlWKgBAz5MYyjghErCF-tsfJNXHFV968sMMH205eVrG4R73d-0xAOiPc6HV5dl1q6JlhrnMlJQQe0PfnPTvUIvHygCn3JIc1N90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXHWoCngnHn_BcR-i22YCZa70XH3H3yEOy6gpK9zl0joGmJ1uea208r1-v_AHP8PVJTfiTAWNsaO4mxm9kxBXProiCnuHvGnLjJl753Pj3-ZyTiRuMsHageHjVVhKWpknFD5sbXeURcfJjTbGKgHUWcax3vMbSx8XqkIUGltwUMG2EzVPuSlxE3h-_BivaZqNJzHkxQgXEM3s2C9YmUs-wDZDTmfmlpBNnD4Yk1fhMrS3-eIsBdgYYMo0OsRvvy4tyuUTTDoXgcVAJqMRqeLuUd1I5Nm6_kWWP5HjkqoHtJQPmS7N0ZJz6daW-Q7H7UwZEmS1sweiI9aze5MxzXpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgaK5To0fXmwrGIIeZ4gI4gypAHJNgpIR-6Vdzcco9tmn_sZA1Ia0pA9MYZ3sMXFBzSj5wYU-_1LPR1CXoY1hjW9DQUuJjYl1MdNYc7CBy40QHNonZeBB7vxUl2MonIAysP6hw7iHE68ZTgFryyJJOuxS2heyFTWCrwEaoe9R4l0X-_BH_Pq9CEQoPulUoE94v2qR34r-MTWkLrxdLHGMhWG3PAvjSa-H5S9m3ZYbClu27qYReuZw673dq78WZ4Xix9_CGE537uRS_JTV7tiBc_mlXhb5q1-R8FFXwq4Yyu78R_FEWDDCeTxi1WPKQui6_X7LIf6Wa9EXaRRGqobjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6nZrn5taHMmahkIaygu5GNJlWOsl_I0a_WCnbEWVIxCMr0EXnOzJUOK5j9BbrmVqCCeBzvtD5ShD5yP6ZKN0_GXBzbhYOhI5F4oeoR3eKBgaPk5nxrNhXVIgudS2WHpG0ru3Vw5FV1AlJLS-yzzVajCmLPxUEb9HhDgTcDcsAkId1bk2m2UHXphxYC-KTbgJVrf3PW5_EX0jXShgrbFcEzoI6vdfFp1a565aajdwVxVsjX-fZIVqCcFDLACxqupsKcI2eoZh90k_9DgZLItdHm-3241Gr7Ol_B49iLa83z_XsqAIbpwdPluaPGC3aXXCQ23rSVWz_DNguOGEFHMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmFrCD9bzSWCP3AkmxY30K255i6Y4Ew3kJEsvAb6Ka4LV2-MVC78u5f9mkMMDzlz2xib9KoKXRewak7R2Pjt0hgg4m2qfnC0FA_KYJDt5jYaQw5mJ7eFCycjsTIEjaXDA_Cs1iKCPSxdF1t5BmphmPleO2AEWC1eucJVxLrDWU6MuQtd4MxG7lAgI8VUKWcC4gV44veMCIpQBU8cOqWNKJOmIJSQ_qmbpBHoxRh3nUgFgOfSEDWWlvPoER-WRVKMEUZpH-Mc2p_phoxow9atbCmcNIjy_LM4NX2K-1Hq2tmSPJ3NV3mt_dD9I44uj2kugnz13VNumXCHT5UTPiox7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5u0CDUbXduTv4nwEWG89F9i9O8KCi8JVxzYi2STGRYyDblFqLnn73JqPqige0w8C821jDmRMl4Chp-5tT0VvJEXe7C7MMPme3VeCwDC7O_l6clOMEe6tdolw95ZgxFE9NsLZeDS6KDWUilwJ3c4Qjjw_xBtu-SfbUMG6D8KtnL8kG4Zpy06Uhlqz9v4d7JanyWJfHYaHZTb8xM-0CEa67xavLsTiV3la6I33xIb2vd6fbpBlPWpMc6VQLkqq7EBbnc1_4dtngXrcOqxWRs1WTWoWZs924dMgr8ZtTlB4-_6a9hBWodWAZpX-yWrJmQxpf-UthtW7g64KNxHev2e5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au9_ccOE65Xfrg-QRLqutKYq4HerOJ5V-Fpyj3Xd8tfYDRk6xGBdsXSgK_tYThK-XMJAcUFUPVtp6uIZxUzzvbb450OikCXPl4woGERgHLdutwlJ--FBmQs2BhA3ZSccL1dGrGc2KsyP8ci1H6BzfHFYwjFmnoCTl87Uh3l_vRABuR5OSheXz_RypRvzKeFt4do_MAtaAAkoMzacwfkY2prIwnISh-KBS05i0Ftatev0D9rDE3jfeGrGNl69VEkjW4e0yIln82TLnVXgAaSaoC4wTx8dHJh7rMkVAvfuJJvVdUGIqUcgzAvQ52dYyyrwHxDcQedmXl-LWEP3SMwQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lc4nkMLBi9jQGF4ztO5-ufs1MUfofNqbeifVFkx3y4WhwzyFE1Gkf1MmilGs-K7j7ajOCemIOkuJaJAy6LR8iwRhRJ1urt6l1_ckaejS3lh3UWJYUBaTjf5gUiYHx_pxi-K8J0aCq9Qzru2tNM6lrpW79t0PCjC19-cr_c-2UfbC42Ezd0FiwPtO3zFDpX8P8bjCzq39mpjhB3pfRhOMjeYUcfuVg-t4VYHEyEFseDXBWyhQzZT1RzbbMZaxmqJc_kHzPz7HDRp2GE0YYIYWxYkjR-uOJ5qDucSIaeZcAPFFDDHzI2CmTU_e6b9eDjxWGnidxMQGG-aMPDoMZ2L2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4CjpE-JjSCrJz3r20Y3bS66PZhPdoD6ehxwYiHW7rp1RsKy58w_gSuVFTtYX1k2sfDtyi4dmvk-UCz9Nb9TJxhALPrv8co8H6AtIVKJ7sFUBkPI_MbPTmfeurn7-k0IE8Y3m9u5xAu1BMiefALRuEiXV2Ec40DGvwgXCny2ocN3zp32XYF900ej7EdA_2pHv1KdKASPgH65sfqcUocwiBTKWIiUKz4dU1IrQpEGxWNgnaMmY5trhLVtXs2xaCV7cUjeMISAK2fvufmJlqEBc-2YkPYID-oRlO0pZDmQbXSzfL1cxZohH0Babmkg32PjOhfn2knrnGsFq1upwd0cfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMNs7SzbCSLEG8f_lbDXOm643txPW1sCyql8xsH7pOM7j0nce_Rxt8WFvsc7xQUN9bspLIEH6ggxeiFaNOGf7VEg3jEfuFVXCVQOLn0mhrz6UJ6nFFg5qLvWFQK9wMBpfTJguAtfb-0L-cp7JhxGVpKfQrVPBJZuMbZ5asAHxSeTUe7DpWZalWlEhBVyOPvytn54Mzai2Q_vVZG8ghB7_9qMasHMBwFZAhM8rg6gCisNn399gORUu0XJTT8kIHiEW6FPmyPsirMSF5YnGzWDMAjm0ntb3TT4otX8X8mSvr7K4cN48LPFPS5phySJr1f0uG3F8dZMHYOx2a-FluxK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhBLbbmy5845E74PrFBvzEyT8Nxnqb1gTNCnFHeG-wJg0XZjxHP7Ux2PXz53zwetBll6Q1XaEFnjhLccEryvMl2ymjRKf1aR9rLoRnCU1E3zgGsJGfZS58yJDrXznHFVuMnc4X8ofnr7jAWkMsZCnEl70dE896F6GQsJlnI3yGV7BIXBEL4BKYQ5tboLCD3OUSJnQFGcUcAtAF1f8bK9CpNYbHuFyKBapO6jMV72u4u9fxzc3yhMLUjXc4L77n1es6V2znU6xEubgCfO0hCOxiFpszV1upJ6p7D3atInbq9oLToK97gOXmVQKB07NQuywD2mhOKxZkceCzYDMk3TEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0NCmOR-GOpKqGTfccqZKKdwNPQFew_4TlZLIFCi0j9c-1kaGh720EJzQSqme4GGScqAu8Lq8bie2UmL7RVOcJdZB5v1z00aIlV8f6tbM2Rbscpd6xKUcfnYVwyc3PV55pRI6c80NLBxxq3QIJmVLbmGeWMUpxeDT5MsUoWWP5kc7E1oNTntQUaGYwlyV73IOyDAraPJgJgLI0TNIp_q8_j4CHC_Z210XWMLG4IDrB0Xt8t18vLGHvxvxucUK-DLCasfsXEHTGbMHmn7iKG-F9bJPNsTxyoIPSQWl8kKv4MvuZe3_7rXHqswWuo1VxuxdZQ29g9INGudQNJxw5oXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfGk7pnuXyEH44Xa4F_t7mD1b52zWnFWxPkrTJBqVzSTDfjlYWbtXcm-gJp_F1PNSHJ3b9VW-kS4OvKWZz2onb_QooUaPdGVQdQ0HWg8TvPPocb8ocu5flnKiWxyZpZ08mZPC9s04H_YUb0s9LNzWCxpMGu3oiUJnHZPg4fkja6rbHRRuTI6FkT_UQLwxCe_cB3nYSg2WTJG_cwnyv9FPi83Bg060JlR4aw8EifZbDH5NN0o77_ZdZOcTxhQQXC9GdQVLXSgBlkd4_rwAFXv2a4_eHLL1Sv5yj4R-L5qNO3-0ZrT4yUKi9N1YjqisQKBamVt_HHafK5wXWBRU6OQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mC3GHpGe-FE1FmuDIzx7JriUacMLI4JD8jyFVfMwePb7ifVoQ5wUxWZC7h-JjN0GT0ZUXL5cpfiKCaj7FY5A6cltI8QuFUJXxDM7-5wQcaJnmUurhDVCZDIPJzGgne8IKoU1UnjZh3Q82Fxj4J-uQYAm-gM9G8LQuyvrj06R5G3kyVGHkKgiml1k8iO0RrDTBJGNUEsPVbHG-X7C5f99HsxM8RHXbS3KEWOA-HABhaMsSTlEFkQLD_FS0ESQKjEv3zShQthuAR4_w09rwy0m7la4kbTr6L627wb-SmyO2OTmvQUTTzfLFDRHcneY2uOgrAtRJmkPnI955_wYW9ET8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOb3OG62ecf0GSVbbYh7rxoz0zroaB2Lntif9KGmHKiG6-0gMi1q7Z_Sc75nMWKazXIeSvlTgRgO2kRhGdahYsEnkibE38Zw6yPcwxgkBzKtg81cUb322f0SysyqdqKVdG7fmC77qnyDa5MnWHU9bHsY6CcKECVEIh13TazEXqFrXLhDRFiSKmTZ3L8uhzEkNkWxNqnCZbH76QfpcARIKK89lO6PUXPXutSc95Rm2e7Qy317rVVVjtiE8RVxZQs5h9EV6C3T412IjWKjOcBQjMHb3GzVAIrhyXOQFHgATVUTDzaqoTRVPoQ-cLBDrkugKxM9e_nOeJfQSLkCs5OOxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI75emub2Zu7AX3D2grw6BZf2xC9IdwuUa0jQEOoEqpdbHVY9gulrwvf3f8UIIp8rQySOkhaZmem17xW6aQ5pwkWvBP8N4bDPjOzpi_QpnkFKl2V4tAIsj8rzsOKQ9Eq5Jxx9zbCldqIP7LJLgopGWuwajUJjizLl5E6jwCy5C8C4J3vane14byM2eQxtPhUdCDVjjviR3isliktKZ1cff1ipJZ0qhLH0qSuxTdctvv4v-Ys5EzrpGModEO4Xjb7zURpA4ohIuGZO3COvAi221UQ2S8KRnH-n5-iuH7YgYlEyHKy9uX-g_Ixz3mUqtgNsIefh8X3J1nbokP2hmxSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW2crFB4--hUdZTDl2xmssyxDSnW1U1KVSvcfIPWiRFA0qp7N_Dl3aePGSBhjtCTQUemakda3RtDlCCIYo47-mqIR18_cD9PQtFzYMb26vGvJA7gFYveqIeYuH_tR-hKJwE1UYtmZFuRvA1Y4EgdCpizCdVL8F00tuDNRaoo9hNi6VzuUOphxSv526utrDeL6gZ4cyN3ukQSn6oURsVvdzzTG4R6zfo5sZkbtpNT8tRw1qtinxZKpei0M_3Bc4_1xKe5muo4H64TdnjD0c0rJGW3S8tfSvaLzdnkGEpAxjywMgO2MUffnzjA-CxHJbNp-_JkXt5cI9mtrurUc1vgRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv0qQLpztcr1lXbN3IFnVS2VdKz00bykr4HVY2T-qIQWSd2rKFBR04UARbZnIM4a0w7Y6t2rVwPAuxsuctWO87xMVAzYTLTFHOKwR7UlU8imdMWZ3_6i5_8uqRIafYy4ljuPVyuAUESO0pUMoNxb4-c7GYikR9WHYRaLh4BWsmMw51-xzqK4SSxa7riSHGSkQvnomWedMzjfogUwN_MTgpE9_T4Ct9IEQgENVWIGp1SlkgoTd4nHT7y1CYM_R7WbpJRR35vYFqP-YIlxmbeTjx_v_guVKdsYfPZ4tJv8SAzsPTghU4iqwUDQrFIvFewKhi1XTjQwjfTVcmzNo7cIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8sVqxM2HnCxiobbUObphRWRg5FIz0sIuH7YqvTycoSnlYmE0HvE9D-xzalI2yXhpwvm87QPZNdnK886OG_UF0xiFjwzfEWdmognlUlU940-zqj7Es0wIkIXeq01wvoXSP4jAlF6nJFXj7uP7_3JAnNsf1y6aiQDR9O4JKOnJdvYWcGVr0HAzKq-pzIY6khE1umfiJSlIvHj8XeJsEWfIzdV3-H2ZjwNyltTlcdkpuirf1kiovGRlh85Xdz0rsM9UU5btI4krU0Qs0-moSTUTVt30czPQR7057QTI4fhcHz2wfoYpDwNxWcPI-YY-xCZB1zca4q5SA2S4lkUubNfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUK0tabLcoODWMwVea7aV6g_12HJzMnXU6dzWjDRgZImVjjND6O-r_V71ySwYz02l5iOCQG51wbwKckkPmFd3xlLZxvs3Dy0xkD6-p_jox-86iFGs3OTe8AAQf0vFMp_ISxHYFE-VTgKepcPmxIcK2ithTTXY4MyD6P8N3W0zJOIR7f3k2OuRRQyfsY2t7IaOyBULU9fCWM2ID1I5pw9w-P12IwqkrVsNIOUCXAVA1p-tSnHiRd6fk9YZiak5MCQI2skoXFgJGTNrgj_YB-1qXLT3_iuauL9Hdb1aPD1aaUMsyFHOVED-XNUA1EsoBG15WuLXIGjS1Z6Ss8YzKq2Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0iDiOewvUnJDJDZuZURONtMbcbDhZCrNmLeTaY8QYyrztyWdarqYnSi_MNwwsv51_0cXbr3zHaV39itr0igBJJvAGWnmC_vSLExM3nFoPOYMeDNwAI5gk6QzB5ixk9NFhibhehKM6sgDNdGBmv_GJ5RrJw7AU40ZBs_9Z_t_XtxZm85jKvtV8Mb_2aVqDYNIpMIZYycw5NGJnM0N7KO1_x-UlF6HL9g8nnbIdKA1tRegNCaglMXbRImlBG6yZ0DQOWnZtv-DwR1OMVBG38_bde5AsVa7cPJRFFqrVPDGpQBwAO6Ui5EnbUra7KsWTxPXmXvlabi_0GwLsBazbUBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q95kIRjSAboQs6nMKfRe-B6mO2dhEvb6dVh6KZzdcIFze6-esqhSLkBtz1t2yEYvuXjE1pySTQU78ZtoRV_MsOiADXAjV02aZv8PrpZQN45zw6uivsJWa3gIqQcn3bix9x82Sp0tgvcX29OPuj96bhVdpaj7iPch-Fit4mu-S0JoiiaJFoj4Uq0fNktvIaesVegjp9tJ6yMBzhrqy1ENMTPcG5dGcU6eFBunnMam6o31SxrOJyXMYysjnguzGgVFrio0Qq8bz3Xc-i4n45S1pR5O-HbXRFncIMZJAS1x-uemePLug8M2mrQxl_QWxJlYDyAWZFJJrjUxrAcDSwFyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqsTWZgeuawyUZvCNJp8SqTAwReYDS8VFlIFuGppNl--kNL6JLH0Q_xH-GvEXKvYuEbOKr5EcCh7bK7ws-f5BNvZLwrVSgZ1pgGa4dH7gH9Njj2uniP3nWT8qN6jBT2ZvbI8w3WgM0VkyYF3plCBNjvavWMk_gDcRGOTg43uXoXWQVitoCJxDrVdrFq-X-syOdQDKiFVlA9uMU9LePjRG24wna2gXXrRWuxKcN1H_MqeD6la_sbHr6t6chQq5sKW7gTkv-jUKOx6rkyO9_fI5ARmgKdMnTrJ24SMSNkRPxhqE3iwa5At6IEcZTBipsSGIOJr0_Tomx3Z1gAq86WzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEUlzZiHKmkRaSgKwWUVAXPL3zSFz_lgFSrhLxhvGkiEfQRBDO4zr3tI1wkgE0g2tUam2QJJRWGvE28euzE8oN7VSlu_dn4nbPgyZrGxvGYdKBlzg2zLqhRCGtvyK8BcfdRz2koTq99tW1wTwYWaHOgY1ZI6i8HAgmXLhg7ayZUGeO6MaIkrKKTsiYGPGhEdPFVNQd_X6otl2ziQhC6NoRGjsgsgPQg_QGDIRQo0T9B_t2cxQ3O3T2rBmQ4iVgteuRaui-0g9whhdu9tZCqVvngZm3jjBnfD-D5BxGLQHi-qS3s15Vh21KTm2WMtySSq35b79deoQjtUR25GYmdbKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxQkzKFmzTT42BahWiknBm0BjdlHoc2cKFixRWrEzlcMGn2x2WHxSukfUQO21CT9hUnavs4mw3Qqbmg1sMfcL3tK1LVrHOM97JhIpwdiw2K2pmaWdTlCIMAKT1v_8mIU_gKh94G9d0q-_BR2DojmYuubxp6-8z2JkGr2v-qhY42jbrY4ZePa9Oxc4-VxfNdvMRLdJc4105QaGT9kQ1g5LCNE0dOfiPfo1in6ddtES7MOSTPnDIZ6G2bjhCGUSAcd0EPYM-8pZifRbJi6RdgxIPxhHx4rmkG1PFx2TyKrFFiUC-8lGSbGbP-hBQhFPMxKLeruRGROTAA5raMIu5pg5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh7Lyc0JnkKfHO_jRhhUWQ1r80R9V_47DTWcnWEUxyMi-Q-s3MC8Rg8ir55vA4-PxA7MH_9uD6gq2sdD3M8djaLrHmSUcQ_4NDv_dK_WeWcrJ8Y8h_W5hYFO7NZyTRUuYz2Qt_qQiY5jyKbW_SAr-oUZwLD7UtGkJ5QaW1DUjQ4tgw_SOMZwNcTAtFNvhOoY4mSxY_z-mfNKpMv8iTho2LDqy8ExKEoamxGvWCyyirD4K0-J8l6viNUNRUSkXZiMutT5wO7nj8ncIo5_V5dR4OTZrCeF6sEQBZ5P0uqPgczdKPH9P9M_K9a1srso2QoDlBfOE0m-k-tFZjGVlzdddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKeQk6Q9qxDoZq1_hKcNlZ2QVbdXZ7WuaGFbVNSmSZSDxXg__U_qpUzkSxZ67u76gg3mPbgsjBlzrXaXoy2MVaiQujsggYoIsAJkqSDgGSyU_-IIuzf3ZgnkMy_rHUz2dQfuAQUqrZiVYJPImDixXxaEwxV00kYqSeD8k0YTC2i1hQU540AyplzhP8i5ktIFEY6zrt_HrqYjxA1VlejF94FZmMrK4O-k_wfpA4PiXAVsv0UgOasgrEznmhwiDPsT7rsFqYn03BOFrJUHxy71CxcMFxMF_tpPrMs3Oi3qmEGUtGrqIPacHlzlMX4GD62ihZ13HFzg_XMa4qMkweyLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwak084CAJZjdXqtoFebGKJozDcZPhCtvnpIRbAUlRuirCOYgtC1RxnkdLmiXr3JXZkCYdI1bsjCerWFBCxw1R4E2KAAYTE-zvwCVbUJi3dRySJTu2T_XrWKO4aI7hhMXqPOTP3r4Osy-yEucqBBcuGmztUIAXf3naifRN2FRAr_SeKU7uZ2BMgxqqF-r1JUSoRALRaN-8KCe0FaJZdN4IkekMHweMkLom4fxxHjX9QgZHF8XL0yqMWWudvl8JiZ29rI4-pSA9aVYm_VTXcFHKS2MusSRYX6D-gNNNNkPyPyaoQABVPZm255LohdpELSjJVZyg1fa3xBX170Z9npsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfNl9d3-iUIn4gy5nwMo60DTuupl7IqOLHftkmys9K0BQMShuW7w4-3tOdPumbSlKZxXPeMBVlMMlEF3H_mlp27ppbg7wOQvfkp7vCV5MXds21n4WmX3KEC30zufBpFGaWQbk8Z1F8DU2heT_qfKjKKzF46Hb0wMAlHA3IgIH6atsGBV0WwCRtcJYgksf1cJ9sShEXfjZoSWsigHPr8FoqC9v-hslSCj9i2RAaEb6sgm_n6wHMCgPwvUnxCdiWQgocVkujE8IuCgVamRNYTuwJmggi2kNrfBjnIdGVI9jqbjFcKaCTW5zDCixau1DPb9CBqgftVykZigK1TcdxN_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sHoAw65qnXoGvvxyjx7jXY5jmtS0M_y35H5bau0szSz7qR7eePJFl5rTWG16QxZFSgelQEQ5EkwLyZ6PEbzQM2jnCPx8KwAPkw3gt4GLFb8Ngq9lsAGdSDu60Ql6POL45HLr4WmrG5MLudfa2XB96AbsOXfdhyJee0f9ZjflUS5ftqOXD37wqrK3EumrvfQKW7KU3_CWls928dGqSo7xAvqgK5kYpJE2NR7LEgyGM-F9ySa9g2m2uFjS1cqadxWZIH_gBSbiFtpoqCEfveZFOGXhd9wejWzx5iT0sGcS51o73VIg-LkXBW0lWvbNSJmBpMEAPFUqf3ySdKI4oKmioA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sHoAw65qnXoGvvxyjx7jXY5jmtS0M_y35H5bau0szSz7qR7eePJFl5rTWG16QxZFSgelQEQ5EkwLyZ6PEbzQM2jnCPx8KwAPkw3gt4GLFb8Ngq9lsAGdSDu60Ql6POL45HLr4WmrG5MLudfa2XB96AbsOXfdhyJee0f9ZjflUS5ftqOXD37wqrK3EumrvfQKW7KU3_CWls928dGqSo7xAvqgK5kYpJE2NR7LEgyGM-F9ySa9g2m2uFjS1cqadxWZIH_gBSbiFtpoqCEfveZFOGXhd9wejWzx5iT0sGcS51o73VIg-LkXBW0lWvbNSJmBpMEAPFUqf3ySdKI4oKmioA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I34-SYtzKN6WO9teeqbfow-JuPDO25b8PDTd9ZZ0btgkNJR_6raUKw2PFMW5hTliuQsfOiobpU1NAnucYHZd3uqYS01WfQtRD7NoMonXbj3rvUGP_Q7wR2VQObEglrXRyMwi_ce9ZLV-7QgTENGR_b4zLCu1Wb07Q1KKlfOHXyQuu9jkzWEoP-qne4-Dgin04AbzJVsxMba-dcl1TUlyJcKOaESSYu4rYJG_x4knglGrTJq5VkyjiADV7HeouZGA6vUC5iOZ_8_xf5ei5wKP9iVGcQ7wCuUmBQUJ4gDF_31uRIRiztJQb2_1bVRnan4vF6cIqNbwhYoF_DdUBPACNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxWKDJPVao_pvzfPZ-MvfsR3cjJEPU7EsC2J2y6iDPiyRGvNHllx1QKdzk7ImVRBa3dACklJN9PiKOOndKPg0G6KgX8RyEh7d55iexkE8__MI-wIiWRLavVVcQvcDZro3r4MKKtilwuyq82mmzOzy7ydrcxaLUmEWCW8ClcZToTCRhpqNffE5QTgBtdmArKd9HNhMhUkxheRzI8wiCaOCWDygHlsc1pQMwMN58AUrm_reZPI9IRQp-KUOUEwQInELOmvw8eMM0M-cAhp4MQtqtANhM-GSOnCpNxPddhh9toMcHy0jx6jLLv4njbMessgWIRNT0tw2tnEkRCtgrnxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1g41Udf9FOap8RWLxmSQuN_I1xqsUZ9LZp88RO6A0JFKgKQlcwgfI_HJ9N--ku9pgjpR2d8iluoNaC6gBZQvUr8BFAtF8gf41go6RWrYKIpfBYNJGie4I_J-4nG9GgZ9juErx5eCb3t3DM1gfcQvN-fmn3to2vhTawlyulRTv0E87VpSw5ViSlBCMQe13ZTQggoOr1w9-rI3nsJmcWJeb4pcggPXviHHAmlBOQg8pR8WdRKgJqIEmkZcQSE8whXbaaWauXty9zkSX4A0_Ly_AQX_QU7DhWkFL4o2aKOS_qm2sh1783av358sbRzyhhJ9M1GzMzZVYcnZglkWjpBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjWQeLrA1QKsnhfpmdxbhnN53LAq_efd3c3YolxiTQPOg5qBvllSyDvVVgiucNYAXy4ax7aW-irXOe3OLXC8Gg9p82nVleuqWs2OjSGokyEeQiDZgihntZWNxtg2GmVEngfZuFLiqvn9meBE3-KXZCEFFi-rB9GyYTdEbG2nS5Fd1zHhDPMUzHF5VQPTiyvZY_a6HhZ7Vl8rLKW5ZY4qSnv7avkjkYh7A1bZwMgjbz6LuWZ57Wk_VuUtRNkn4vXy7wI7CZl1VOdJRQdyAWt1a73g5lTaybxoznBvYEeJxfVqUIyUZ8XUF9m3gG1ZjbHoAzqL4mA-8JsRvQLQac7unA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad8x270T7WnZE0oo62hdTYzRuKt580ysU64eQmBxY2VaKJ3mhBWo7n3vBkXZfwLB3q5wmPwfMw72A8UusM8pk4dytBc2xsWdZ36iHqn9xQp8YfCes_gMHUiAkg78Uz29_v_PEYTCJZaUc5F9MkeKTOQaQJulxDaAigUGo63EL_D6tvQ0L-lf3UveOCH3mRzXk5MCf6GC-FyAJ5QcFNKTlY6VyUO3lrA2ODqxnh3vhZmgH8n7jVtHTFq_zAjyW28guyTzKQquzuOHM1EwZw2WAlw-ENh3FHEl52lKUzlSB0LMOkjrn0KQNDJbke14WdmdNPazCAKN8zAt2PNNEZWdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-PoS3WMaoHsYf-t0WpaMaZQXMRWTd3NwhweMtahPKC4oBLXTNCR4NhRFuphEjidXQ_0pfyN34B5D2YTOUVXyZtcNNmz4W4g5nZ0vnS3VBlbKSMv4U-uymJF1MMbiLbax6sY4ltBp50q4zB468gWVArUoLQjcEaRtprz9slenLoWOdhcuusNlJx8ZHz_y5wP21rCh9EAG8CVne83t3oP0xGeLUAq15few3EBVyIUnhMid20Vn7-8zAbSi8vmAy6DCnZE140UODgtq6pNbAsy_v-LkMS1Ij0VPGHbZc07e3soexb_Rkz5gXYWh_shjR_rSJ3tmEN-N6_bG3iru3-1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7gA69ULid13oOQrEm9D6FA7TBe6kw111APJfc5byBgDP2J3BfZ2JFb9unoRddtsP6SW4MjuI1s5e3cLK_YS-OXZ4Hjqc9cIyHIlBKSRoIgxkF5L_GCRah0F2sKo9LXhMJQ_TN78n_SPSUrsEtfO-rEp5nsJ4HMRX4hGT0NmRyESMG4Mww9J8lLnmz6z2oZOgL2SmufVDghUbvyXvfX4iTt9YZBmrwnfmBdx_qyV7IAAtnWpwU1ykagNPLrtFtt23RE5kKnFfhc3-Gm0DKBbhvXuoe4jwK-pVyrHOUKo3vv6hhIAJtadBN4rmMPZOcs_JS53_c79iDbZfcAKCsQg4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NtpvX9xVJkTrBRnXxJR19d3qj8nq2l-u40owpK9ap4oMLA6YqoTv0u64OJg9eBuDFS5aDP0_3_XgvijMzLWaUu0orsIIds-QB-JEXe4E3y3BEXMnZ1xSQcxwbb6uvWXrbjTa37gNJBsT6sZ7rN8b7-i2qfBFojOWAkm6PtMiWCY-kU92NfgZ-FQUJuQyewQ3mHpBb2HKbVo6gfb7vq8FHq9V7mpLFd8YWJEM0ZxLdTjAMReuiKw4ziaqjDIHl4ykdGymy4zi6upgVLMEryfEYacgx8pRkIIvphBAsLkjpQRBc4nWVeUGeg4fDFgttz-gClNs_csZVAJ5tEPac7v9klthynChw7lzkGT1lDb_U7LndsVMyjXa4_ChfEU5BMt3pG5fzOeasdH3mzIpUq93rwYlPrn7Z7TExmkIzTLk1-ATZiMjDsgvwlk0fFLYB8Wzw0Zo3OcRslb6ayTZqe47fvuKQluKfnxp8-eFcS6Hg4aWCtqntH-LA-0vOsJZXllDZsTRKj0nndnnT6IQbnDJ08Akn0cbrBCZYZl_ExiUjgGg9cvRqp5bRYyA-euIORjfSNmhUmV0Mt7O8I9LIoOLEiC0st92Z4IrdQiB-NkwweDQTM794PMI2F9Y9dIfZ0f41qXUPjJCS2eWUX3yg8ggJt3YOwOjiUdVAeSThLuv7Fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NtpvX9xVJkTrBRnXxJR19d3qj8nq2l-u40owpK9ap4oMLA6YqoTv0u64OJg9eBuDFS5aDP0_3_XgvijMzLWaUu0orsIIds-QB-JEXe4E3y3BEXMnZ1xSQcxwbb6uvWXrbjTa37gNJBsT6sZ7rN8b7-i2qfBFojOWAkm6PtMiWCY-kU92NfgZ-FQUJuQyewQ3mHpBb2HKbVo6gfb7vq8FHq9V7mpLFd8YWJEM0ZxLdTjAMReuiKw4ziaqjDIHl4ykdGymy4zi6upgVLMEryfEYacgx8pRkIIvphBAsLkjpQRBc4nWVeUGeg4fDFgttz-gClNs_csZVAJ5tEPac7v9klthynChw7lzkGT1lDb_U7LndsVMyjXa4_ChfEU5BMt3pG5fzOeasdH3mzIpUq93rwYlPrn7Z7TExmkIzTLk1-ATZiMjDsgvwlk0fFLYB8Wzw0Zo3OcRslb6ayTZqe47fvuKQluKfnxp8-eFcS6Hg4aWCtqntH-LA-0vOsJZXllDZsTRKj0nndnnT6IQbnDJ08Akn0cbrBCZYZl_ExiUjgGg9cvRqp5bRYyA-euIORjfSNmhUmV0Mt7O8I9LIoOLEiC0st92Z4IrdQiB-NkwweDQTM794PMI2F9Y9dIfZ0f41qXUPjJCS2eWUX3yg8ggJt3YOwOjiUdVAeSThLuv7Fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlvThhvFoT0wWHvN3a2PHUewXYxElY0YEb9NxwuTvcTH6BCk31LQOLEtghD713zxYBc2NHRIGDRhpII8IOhAiR9JOPHnR9VMBfB0EmVU0QuesFW4MkmeIFZgxhbJmGzDozPm5mWs4kRcc0nweW2HqNafTEgp3EjswMZGvdGV5uDLUxmLhkTqZhKCfRog-ER5tcfTyZrap6e3YcDUv7gQ_GKq930CyQh10sJtK53KsI27JfyCv4IHWzGxYr8g2LwH78bfomN8wcVBIMl3QwAOSid1pYrVXb5qWHm_BEnvsGnQTEKZ-mN01EOK2gZg2CAATuN6o1w6bKrmxMymCH6bYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyINXh5Pm92vKF0XWVAUDUogStHpfckFzCkjS8UPysGc0Do2YgEermd78E720KB_HK14Tn8nhIFleWZ_5oR9QzNDhBn5VTVz67u0oolIDbNzbISreKI_w2PrWeCHom19z2GzVFM6CcyJqiCxSxoAaxCacwUh6h2R5ndPFoDEg-EqUzSHCKf4Tk4n05Ro0eVIvivARiCyDSIvxNFqs-gNy4wY-_DWWD6TnuGNcyZAKQR6voggvUsD0HTndmT3S3iV2gWvcQMMgXLJMcPTxslDbmPOyHyNnGwRZC_hFYEAuJZ19AYPSjEHU0wADVbv5-3-iEWfZasTw4PNvtBV7IiA7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esX8-JLbjRQ8J7-hhJ8fQdkaNErQ-WaMPajSZ1kBn-e9uDuOeRDoEVxNFXiucfEbuEDa2NgRUe7fJZyBRxBYs-Obts0J1Qiaf8Vx-5NCO-Khv87e7VP4v2HV7Nwtsk0PSSgsSVucj3l7vDrbo1q6JcJ1WbHuNRWIl_VuOPWh37SCjBQW728lGgp7SYjgufXoIowYhT6LQCaLujqe9f9FCFpaec5GN1C9A2CqP-KnwhPTwhVRKkKlGwBzWJbIt6bzq1C4thyqpomn9Dy77AUatDONYj48kBXvm1hOtltxvTp3kfVdtSFf0L8kAlTTiFp7r8dyIv5N9NWmFuiGhreRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNQtx2MaG50sNTJnR6X89nERmcXKd4NWePgSNXgH3PVWgIVd3vbwOnQJE_ytrkUx-oGY0p9k7j4F1R7yrj3OyyhcwTC7RKD45fi7Uw56sSKtc5LNVwOad0SiUPWQSIBVsJUS6QgIINknuCJy2CLi22r9VHYSxW-1dVKVcqkJiop0fLE-8MHpBOY7aCMTbJl2IMl7br1aLNqJ6YgEbMMzb8E0Cyr7FbDmn9Bn-yY26VqNM3COcYaZkxwD71WQVcYVDXtZC98R5kjh0vSvMWZmvyzQJZ9Nz21DCpQWA4c3RGxVP4zPpQjjc8i3tKZhwnPbidBe70T6-jcLPG8Yda2XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD5GrmG9Lny2bPp6h7bW0EFYWdBiis4T1QA6ACz0AJFb8JfGr9N3dd85Q0c7wZciYFjKjVU7x4__KHcZ9i2lyBoKwYOUjwQImQh0s52aP6TLSAtI5kHCrK1w-BNIcATpmP2hNqbjeTmOMENBk4BZdww3tySzHg5tqaF0rJiRrCzI541RmVbIuHtHIPXPGXMvN_A-UBKjKe_H0NfWMi2KsYoRIauQ_mi5YhphdVbVqEEWIaLu76TWqHhw_snsVJEBCYJmGgSTpqMquPTXzUTHlJKZoTjytd3k4eyffO-9vgL_qRnUwF-2XGHWlVGDtLyRcQ9j9T-XxJ7zubuBnekaLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUaB0Ucoc00PMxV7ZwO8KsnBsI0salwacFPBGC1aYBVbb2AJkYQJqWszrPlFTlacl4GhAoH39VoRl8leL4Ze7FcVVM67D65yXB1IhX2KSjoBQY9ExJN03-YdCPZoZ0q7gy5gOGZYZkYf1Be0ZRaT8N52sSb7YDNqZEnQfIlZwI7IQ4mU-9wgMjGog7bI2c64FzaKY88O1nbZ_Dld-AeEoaT20zeABMlbCiYNkk1MZpF8peqTi4G989hJ1QkbdWzgIO5AM_cM12vcBw83Kb6VoYKeXOpVm0pUl8R1olhg8tjJCxvHhNOeLdMUGTmjLIcpOdI_nrcAxQM6HwfoiIA7mjE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUaB0Ucoc00PMxV7ZwO8KsnBsI0salwacFPBGC1aYBVbb2AJkYQJqWszrPlFTlacl4GhAoH39VoRl8leL4Ze7FcVVM67D65yXB1IhX2KSjoBQY9ExJN03-YdCPZoZ0q7gy5gOGZYZkYf1Be0ZRaT8N52sSb7YDNqZEnQfIlZwI7IQ4mU-9wgMjGog7bI2c64FzaKY88O1nbZ_Dld-AeEoaT20zeABMlbCiYNkk1MZpF8peqTi4G989hJ1QkbdWzgIO5AM_cM12vcBw83Kb6VoYKeXOpVm0pUl8R1olhg8tjJCxvHhNOeLdMUGTmjLIcpOdI_nrcAxQM6HwfoiIA7mjE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaRwSaA1PiE_3fmfO4S2sK1wh5n_dlMdEHWI0D06MUQf3Ipf7ce_HFKFEYFq8R-Gvfc-Kj0x7c2kYUH_QQ0b_sMi8a8zv9pUy4j0ySbhx8s9FgU4FiVDcVThEVBJXdeLjK5HfBlu1KvoHkesPbxVqDKjjGN66OTydkmflJzSndWOydnqzmp0DmS5RGFb6s1dT9m4yb0cHtQu-hsTR0XGbdjiESIplDCbJHryL0w4MctE0sZEmXtyPta7QDpw5m9docxzmYSiJmR9G9hl3NKM0TFwOY3n5uLO0ARoxfkwGTTuI932oqjmo_4mS3VwoB7RFBV14AWZOgNdcj5c2ij7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrPY7oSzsySbMHlY_5UL53GU15Z0NgT4X5n25rkrYtXdetzMsxCbf1HuepcY3YDRyYPBb-NMjxSVYtzSioPBOOTrN1dresK2GH5KvsCItDTI61G1Kx0z-6mcw_DEHIc4xr6026IE4vCIfOk-ZpDLl5lQdj-jVJ2kbJ581h8AkeFUlTe4zZY4n2_lwmC-AIFxhZVpyDbI-ZB-5OuiZ9CV4PSTwodKABlDsxAXtTAUNWKQF_TXSpE6tNSU4O9ZqumDmsZ8siYesw3BXPDi6WCBxEypznKt3XIHSnoYmQaPLvwLF3vfRYaCBpFqx_l6oh68ZAUOi9zBNIP0vd5otMeHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
