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
<img src="https://cdn4.telesco.pe/file/nt0QD6r4PMY3f9C8KgJSoDVGyCNedM2O3oaS8GUg_FCunRK_2YTmprsmGLK-zY_Tpb4H9Z-KsQPaVua3X7aob48tq1AwA_YdlSPVHz1Dt11NNmJG4V2TwQMSGEvaM0cM_WKedHFwfh5_8gS6IHj6sJjxK5Sf0U1ws20mp2Uk-zjag_jF0cITtqLzFXhTyC2ciUjmKwQDf7Cs4FH9iYyGWgQkPZv1XkLYxN4J7OciVehMzDz1RnAi-zooXMLnlMz7aQfIskXozYiA6Tr_dysKM2DZOanfi0F_12wKH1Wy5hyOgAex_-PuHAKzdSOaC1_mjl_7YnhnQFsFz0RCAGEudA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdPvNrkQ0TYrIrKVNn06NanZNVy6HgJ24L_6hFxg0bq2lXcxOgXz0Ih2VnpMMfmkysLyfrHeTGfx1Nfo7UYq6vZwzX9nlpmU4iRQf9cQSRLPOe3DGdivqj4avzvb_ZTZZO3HpjlGO4fRE3p-2kFiMBA_cctAYHs0TuqHMNaqQf1ohCqrBJgzLfyF5NgAY9QjK265Ta5jKSEtVPitPx4-hyRUi9wtUyQ9oIwVWOROPaUsVPJVIJCU-i0ECMxEaqfnrFdPc9pDOU8Y69hdXhFKLRe_jLEcUNiFV6IdkwE0fw6lmK3acln2aMQTEZZoXF5pyjJznW9fs6taPDljFPdGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqUD2ndD7sFwSXOgEzcznV7mqKZARVxgGgTqz8K1O3JVXYDNsDiCgorvvbXwT2eCf-2rTAZKeElFvS7V65AdQAjwJovWCkGaGOKJDfcymdHwEmjZE4XFwZsvNn4iR1Ceylq-u06jGsEEuLvMMixdUKZUxxx6sWhUfgFsZ5rg9gR6Nh8Aw-zpJh-4ERleHV-YjYQnu0tQ1fl9b9JY2hPo_44GZLDbpp7w9wLxjGXLSxen2TC15Vd9UVg7k34wAlVqiJJTGqc8TbKTtBiAiZ-Yj_QfxkEhV72GVfpx9f-z7O8WZTgzN5ewHzQvvvN5YvWKZ5rUm6_5JAgLuzXr0xlUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCCa6YmageUjgQ11s9uKPYfRPCKq52xIJph_INt9SIJ3p9F3nFoO2z6X5ZKzQgeSlja1FJzB6kXLE_KMfdqpGF9zYsmFYbFsg0pF-XJ_i1Kyve6dhbTXXanUYB2_pTaeXU6ppVtllccK6-xGlUUUUIG0D5XsB0jNcxmQiiTSEspWdvwNx8cURbafEWxwBM_An06FDOwP4riDAOJ5A7LyoXKZE3sUoub9Sy6ZBeXc1zwSOU_DvfYis4QmnFsmhH3EUTUfoWWbZ2DSpNtoCxt-ZghJcdbGt2Wp15CE1ALsE7qu5qR2lHKn9hLXaUgXUjXHIj4iQ8XnCBb2ZDaUbyNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qv9MokZpGj6Ih7pwmBePtjHssBeeuVEi4ZyUS_bPnq4CqfC2TFt0MQ6fMds0B2rD0O1YMXB3mKTU8Ro-FDtJRcpx4-F4MAA56nbnRF1YCFwFhZ7YCs_VzcMciUL8o1h7X9lTCMwcADh6sHQ336sNWbafQ_5pkXjjhr7pKTEjFAj8i8vdEkWw34shPZHcobL6HgeY61BKSiwFBnpIXMzHYFEySzTaRQJqE7-oqaVMMEwnWCslJ4ju_xtpNs_PoXVo61mBZawyR9xllKdOlc__xCwSpZWuBEQy0M52FFaVtTx0O4wtQIFp6vspQOQM5BuyUfXkldoj9dINAQ2pfuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHeF9Lpknido5yebaO7DwZVt9TvoqEi5sJZUq79x7PlQ5YTaPNK9d8pWho-Cxt2jh-flq9y8d5hu1cfTd4Azcgi7p-28NFZ6KzJKEQJUsZJeGSZ_zCcGPo9FZ5BDmvMujUta2IP27y_1nylbdqeesXzUk79eMjhSzGf9El8qpc62Pt2pNZGrdmo4FmikudILr9Zyc86Mu74ulvy6Zx0MZ-caOmOZJ-fVT88YDH2sPd3a5COa_O-0DOUwE13Qg3OeAIIks_RJl23gONtfEAM9gp8xfOGTLEuzrUNe6EaiRp-r1uJn1C8e8e37WOpYQ6TOPuf6zGtKk5xRTLbX0O4EFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4EKl7Z0ZATDRQU76OgtOrjn0Vd3jdMht3SqN-qLp2jioBExuqg_uQTlH4ngV9FblAOCMekRJvipFAoExYEWxc9d0b64AtHsIzjSTDXtTsKq-x-RIz03u5tBzyjHzmFNpIssxh5m0wDaXdSLH5GN9NJEbbjCN_buQG16mJZ_5p5oAUz_sDX6IvU2oK6mw0zAJxbLTSEU1DNGDaJaH5_OBBn1WluD0peIEEn4jKTspBYdA8nOgeN0EdmLcTYbpLVxttaHdcTCFW34tjElLF2lIX5hPKq9icBfaX7SJkz8a33z0qgwJXGwNcbP7qadNE9BoXc0vc3oZ3lytKJU8MW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6gGz_uLLRfIFc2fY7EP1HUOQX2Qu1sKBges6Pntu9bCy0Cdav68xhY6s-YlnfQtGX_ewygCovBlScM4GzbmckkJue0QZp-oROa51d2MQPCRDJqbg2-2VhD6NhBjO-4n0sKxWJv6YAFPbAJOQXqQlZtQVwm5fXtRfalh7kj8e7m3wOjrjc5SARn2aEz_Tn4MljjJ34z2PrrqYupFuRh19GIC6Md6nP-xcFcFsZl0k5XCOkxRW5ZzuxvCIUfvV0a4QxqfCVsH8q4q4YIdwLSfuAaKx7imPMDDnlBgETLyDwHVxL9xsETLupUBe46MuKl2hpiBe-qH9ysxY8AjerOdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcjEGJoK0mwhPuN3y2FN04WJIF8RbL69KEUJubju0V2yZdrCbAFZrO6rL2cefG83-zb3tNyImW0BXQy-c58NQ8jPIdRry5TC8z4Q-IIPtxkmb-UWamrCylz2r57jbm5YMw8SpHgn54R8T5dWb83Bh6h_RARfsNW7OUPiEbw0Ivpbd7cL3QcwoKBmPQOkuK5fCIMEpSjaLS4NiKw8cfRDnes-zAJ_ALCmaa6sPBcwyGh8ShHeBXPrg_mKnDzKTho_CmLZsaxBtre51-FkynwVNEGKVMbrhwxkGiqi9deDcYx7a_zd02dz-PWx0VHsyFNSdrekdkjPnwfs3k23HumOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkVve1VrtwkeGkrLeDC0PWATGZlWKx8-PA4521r4JuAMl3DZ8ZJd6iNlZqDUopb6C7FXciidn8FsNgWtfYTzSo4tXOR4WsfgQuc6fW1dfIEXkiVRrMmC0Sg9P2yxrdSgrB91GGstmAzLcfLbiKeBtWjdeS8bEH4JfxmDl2oWGkbiTEm1oGIIyciFx6DiT8C3poBEVmKAOhPVyL7PLF1c6uA72tudmXqeU_k0lb5YSg9BUvzdrb9Bn2t0FvzqAzny2ozbqnQ8WBNp82tETl1lRA7trvjhl24jBP8VQK-9AKpCbLcLBKj0vFNIOUuM3h2wVYDd3_FABWBPp4wtaAExqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LznLkvV6Mm73oyHF0LzxzDqwkI_j0vJwwPf3txhrYVVppox-HUb743dugCK-r7SRg-9ak5xblZX7X9UM0v7IXgKZKnax2xpb-eY7rs7Vhg3ROpA4k0GXKShX9DdOw4TzKtXg7WLEu1k3slVIuzwZ5KkZ4PoLRmTkbydHIOvaLMUy8AypINGIi2sjS83wh1GdKV6jih4IegANzq-jFGoT0UElRYy72ujKceEDiIUQE7UStpniwhpddHH7fjy9eV2H06vnXmVQfZ6II6TAL7o1L1KK1r4uhYpwIf5jRdMc7H-6uqir1N6jWKk50Skym28upWJLwsRnV0zyW-JY5CRRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcagy6K3oh8t6mV6BOWUB4ZLAQ2lLpk5qWz9bEWHmeshrybC0nl5zI4eY4YgO9tIVBEOw2NbZFdqfe0R7o0smxgpLpy7c8u6bmeQpZUaRUd0deIsfzyiSDp_cYZcF72OCMd5nrtluwDv2Rs_nYxv0kIrYK12cu1u-YqL7lIHL9_UQLCv0rrVhhnQ5Dh2mpp1lcPclAWVVYCnHGX6bD2TVhN-OaEduT24UF_g1XxKhx4a-e42QJyjQA1hKJQOfsSQ_uKUhFGSgOG0O2MzhJlGZl-J6fNcBBJIfPK_dmv0ardNvgE7Mely2YD2mNA-7bx8QQjKkPGJVvQ7A8eLavv-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=bj-NoleEN9uOCnN7OIXKOnV-7q_VVNfUrqOPqd22Z-7OhPKod-YB3xb7YCHxjRM5tj9ioIfAPPDmUG8O6nMD_n0n2rI0vKrDHE05zZaRy1TP7cDgIZq3tURzECsLCAa7P_8B5Dw16ORaacDVxeZHsoXAjN2WDr0RJ7X_Cyu71AfPHicGAKmbbdXW_vGqwgf2fXs7PEHT_-9G82amwtdWQOxg9ObDnkIGzST4UCJOwlqLpAr4nayZgRXDLNZLbM-NDavdY6iaL9DHM6dSyt2bcJve_IPNfSYpIgI-xyB3aht4ONSd-fHzfvpF_joU_1SqFEmZ-8zBsPsnR0a4kvY2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=bj-NoleEN9uOCnN7OIXKOnV-7q_VVNfUrqOPqd22Z-7OhPKod-YB3xb7YCHxjRM5tj9ioIfAPPDmUG8O6nMD_n0n2rI0vKrDHE05zZaRy1TP7cDgIZq3tURzECsLCAa7P_8B5Dw16ORaacDVxeZHsoXAjN2WDr0RJ7X_Cyu71AfPHicGAKmbbdXW_vGqwgf2fXs7PEHT_-9G82amwtdWQOxg9ObDnkIGzST4UCJOwlqLpAr4nayZgRXDLNZLbM-NDavdY6iaL9DHM6dSyt2bcJve_IPNfSYpIgI-xyB3aht4ONSd-fHzfvpF_joU_1SqFEmZ-8zBsPsnR0a4kvY2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2XVGQpkzG9W9_fLHVVeT8Clz3Jgqmhpj12Zc2cypmweC2eQYhKoQ79B7DIQn-Wj-l_gIKuZsrGQvPmrj-UGi6qmeHOUJ_HF3owBQuSplTOx29yqfUphdVUWPPaHpy0wGunyr6Uub-cyEyuLjySQ2sZ47w1jwyZfzBvghYn-qcLDgcJnLfoEgCoOpkNZodu3I1gEqxaOLIhVr-F8-x5iE7-qEjCNw_xFXh9jLVBtCMOJdAjIP2COnCmxdXeldBOEk8M2UbA-qbhrApAgvwu7xhltGhUiAuXaHnE3yuCmlzo3rQld2CO5O3UmzMoGqqOQsR5PmG-YpcIc8b8_DRVkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVpB3bTuNY6RGlCzOnxvJrbykwv1DRjnr1Gs3jkuadbrCWpe4zUemvpFIujX3w81y2cNxTyfOhrJ5RasgUu8qD49-SNwWTX0AQngEFEbQkQj1Zun-Umg2MmIUzlj9ePgMl-bYGnsp1L2gYjMNtDN8lscAbe2fzmWR8CdyfuNJzThbpnKo6G8ziRF8YfnRR74BaevlkX6pZwdBksN95rKm6yMq8ztuoocaEYnj1Xm0tZldw606iQAAY9ZbM7DrPxv0FUGC4iqLhjsBw92LRlF7u1Xt2msolehW2At_IKCA5o_IpsvF9p4gOGPKQXtg6hstGDbww-yqbN2pIc3LsZ7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=SkNEur5Ewgfgo9U6gRv2aO-uI9BfiNsKSaB7Zb5F3cZvBDjtIIOD7dXgWRHk8v1rfSYaAafn-RoYpsFljAsOlNFWVWOkO323GlOD1E0aju4c1C8RT5o7Y9FizG8pyQfNT0YfhM4GR_JU7g-X2P10gkmk8XxYWBA9wnAzFzq3xPLntgSPmdNvD0ifKY9xYM2i6DnyOJqfUxcQ3O5NLDsGuu7Ge2hwABrYLA0wlPF5CV5dtsdFgcJRiYtwvqrjNQ6xIrr0oaE1t3dgAtrrO97IcQfbUrcghdQfPWhVc8QwGk8DffWPsPMHaeyYbw8idZjVpoOGTmaSx2HaFGfnZCvSUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=SkNEur5Ewgfgo9U6gRv2aO-uI9BfiNsKSaB7Zb5F3cZvBDjtIIOD7dXgWRHk8v1rfSYaAafn-RoYpsFljAsOlNFWVWOkO323GlOD1E0aju4c1C8RT5o7Y9FizG8pyQfNT0YfhM4GR_JU7g-X2P10gkmk8XxYWBA9wnAzFzq3xPLntgSPmdNvD0ifKY9xYM2i6DnyOJqfUxcQ3O5NLDsGuu7Ge2hwABrYLA0wlPF5CV5dtsdFgcJRiYtwvqrjNQ6xIrr0oaE1t3dgAtrrO97IcQfbUrcghdQfPWhVc8QwGk8DffWPsPMHaeyYbw8idZjVpoOGTmaSx2HaFGfnZCvSUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cov-Z8cBg0khiH0cO1R_UbxDdYPQJIrYtKVu5vNU2uzH6zmndgER8GLbF2PqjMwh2mXLSPvJOX-ZwCeceIcgMrzo3qnpan5IYfmAYHNNzeN7y-F-LWP3F8CmmQb2sqrZDvOxpPIy4bMAnXEpnLNXxe2Xx6NQQIyU7M3B-lE7Lde4xXdqraZNQfya7YaG7oVdH70NMqzUWSbM4zOvcxTN1G-eExMpT0ah626WsAz-OuJX5kJYzETTnw64jQBuIH6cqKvzqfi1TnlnBbjU7DicBGk_K106w04j9tMLBR1D1KlpQPV3yGFE2p_g34bL0_dt3OSm5A6UotOe1bumn0oBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=SB29ByrRHxsXyGBwHyyl_eRz-JaCtRldPvV4T2AQjhNvx2kIQ_S1laqW3TYLWs0K27JrZfRkSgZm6ZQmA3JLp8Ei9WZlNSqqy6s_0xfaZnPPNmJiBGbSgay3EHZQ84vdkjEXSzFeQNkZ8gAaB0Qo5i-6pr0fkz3TacOF0oPGvG2hcFLadAOD1B0MmGccqj9S6TpJ281daO42llI-GFfBDvUpf9Z0ofhqZwXxmiK3ZoX2qK36mX-Vg9mcKEhNynL0Z5fbVNTwrsDk7G7E5kVkWB1zTS34VwcFDoNHtnEaUm_nb5Ahr144jeqXg2wmG_ST0D0lAjDG3i1wxgApRjuh-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=SB29ByrRHxsXyGBwHyyl_eRz-JaCtRldPvV4T2AQjhNvx2kIQ_S1laqW3TYLWs0K27JrZfRkSgZm6ZQmA3JLp8Ei9WZlNSqqy6s_0xfaZnPPNmJiBGbSgay3EHZQ84vdkjEXSzFeQNkZ8gAaB0Qo5i-6pr0fkz3TacOF0oPGvG2hcFLadAOD1B0MmGccqj9S6TpJ281daO42llI-GFfBDvUpf9Z0ofhqZwXxmiK3ZoX2qK36mX-Vg9mcKEhNynL0Z5fbVNTwrsDk7G7E5kVkWB1zTS34VwcFDoNHtnEaUm_nb5Ahr144jeqXg2wmG_ST0D0lAjDG3i1wxgApRjuh-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMkP0rcMHWfSMEmmsTfByEuaquq8VW5pIQzheO2r3ItFLKvEvPhSc3aldMeWjTIiZ_AtWFCCZEH8ghxvuvcncTynk9PC1f5S8T_Up13vNQ9106JGvaMSnxFLl_tfQSYNxYAqpo-y4nKULuj-bqid2H5MHuAYlEgyWwRYWHMiXNWy-Qr1MmI5hR7fuT1gEBrE7VTRpVOKsygz6bGfTNNTdNWEmA8V5tjqsxpSMKH-3Qse3bcnmx4rykZZNhidlO0nxSanrKzYmbz6_7CIs6fUEfQ21rQyxfTFidqpB-NuN_YMKW4HLupoKs_7dUBAykpybKDbkId2hdVrFgk2e_f5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3AVBHZj_x9qbgbOelh9edy7ybb34Rc-2B2GsUXd9ZaqnTyF2DRVdOMRhvEBw1LSaXdtV4PyiphlBp0f2hotHlHnJe0_kO1SjdBCkySaW2NbcX9F4PtHEGPIV-VC38IbFlY_HNeXWXNJDKY-uuhpd8r2kXtfjAniLwuEkn7AFUAxQuJks1zoIevzMPMA9LmF2_UR4g9fB7pPx4zZVCm31ns5sJu_URisOU66A708UN8ifIOYNsf2qy6ceeiaIcTZPo2tj4d-we2g5Vh2qs_MiGBL-vr6Yfae__CJ7OXO5CNbzRfdzh3SiHidefvpCw_cjG1QraJK-sdRMsL0VH7IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFB-IiXGuWhdwRq5nQyjlcRG1M4qpf2zS-oRLVfiFyhaS8TRFBzOUOBjeIlFh-Yy9yfYkOLaHrNxdNSkaLnJiSq4NzsgOxq0TDuRFfZTBbhVCMglIYyp_dbRomlxvio9IUklzXoj6lzrhVVdpP7gNACZfQlzYfLDG5B8duhSWN2PkU8KzEODI4RxR8QRgJRDZlSmFoeldJQu6bFbJXxW0IEIkLZrK5DNNoUJGKwUL8IHHboKtTY4Ow944rPNIpz37MeXzLa-4hlHG3NFz_5L3X1_j3kQYuDpViS5ZHRMXJEaKxGWcqijxY2zNUzX335XjEGTKsadSsrYNSCLC4vdc-Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFB-IiXGuWhdwRq5nQyjlcRG1M4qpf2zS-oRLVfiFyhaS8TRFBzOUOBjeIlFh-Yy9yfYkOLaHrNxdNSkaLnJiSq4NzsgOxq0TDuRFfZTBbhVCMglIYyp_dbRomlxvio9IUklzXoj6lzrhVVdpP7gNACZfQlzYfLDG5B8duhSWN2PkU8KzEODI4RxR8QRgJRDZlSmFoeldJQu6bFbJXxW0IEIkLZrK5DNNoUJGKwUL8IHHboKtTY4Ow944rPNIpz37MeXzLa-4hlHG3NFz_5L3X1_j3kQYuDpViS5ZHRMXJEaKxGWcqijxY2zNUzX335XjEGTKsadSsrYNSCLC4vdc-Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=LlM4U56BSwoFKe2erJOagUDpvk9rGjI7rUuOP0fhcJykYPolbjOmSotOEToghYOAkTVjBJQUIh7ANmZxWVVMd_3-1c0gMgueTou3Bk23O3EEpQfL5Ki1C4IFtDfLSCxFuQJ7saAyG0RjtWPY6BnlHIT20YuxZeQdBI778E6unbnqYGBfNLQQ14cryEipea6whAJItIkfbToOMId6Z5a-4kJBdEVnLT8e5rhL2SoR1tCtoSvkSD41bPsr-UueDPQdQgQVugrHXdSNYff7IpgCz7z5buSiPJ2oXF3WUC1V6JcfkrPWmc0-irY_jitoUTGm6LLuWjLjmcwfzVsOvUmgdXV4GWjnd7KHi8g6vvWSqQCpt7pqG3iCv2D4sy-erBHUf7YMSyXvdKhDlrLFsx53XgL6KOdRDfzkzw9byqfBQPqVxlqdkAyljW6b2R8ONu7tGHQj-8BfnSLSLat8MA21XjKaYLt17noMUx2w7UU2V0kWXXiHDQoB85vyurGlaAEpS1v8W9ssucwW-sdypIwDET_95kSEbjil7H0DqERxvOng_cWo_7f4oi6a7AietaqWJGsrL2ObuJFrMiOmg39o8rlGjFDeyyAybTb63mSzngey_kcXT152LBuCKV4ibe5ymHZdQCir32NDEg7ll4US32NCeZo82zgrG0SH81Ky_5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=LlM4U56BSwoFKe2erJOagUDpvk9rGjI7rUuOP0fhcJykYPolbjOmSotOEToghYOAkTVjBJQUIh7ANmZxWVVMd_3-1c0gMgueTou3Bk23O3EEpQfL5Ki1C4IFtDfLSCxFuQJ7saAyG0RjtWPY6BnlHIT20YuxZeQdBI778E6unbnqYGBfNLQQ14cryEipea6whAJItIkfbToOMId6Z5a-4kJBdEVnLT8e5rhL2SoR1tCtoSvkSD41bPsr-UueDPQdQgQVugrHXdSNYff7IpgCz7z5buSiPJ2oXF3WUC1V6JcfkrPWmc0-irY_jitoUTGm6LLuWjLjmcwfzVsOvUmgdXV4GWjnd7KHi8g6vvWSqQCpt7pqG3iCv2D4sy-erBHUf7YMSyXvdKhDlrLFsx53XgL6KOdRDfzkzw9byqfBQPqVxlqdkAyljW6b2R8ONu7tGHQj-8BfnSLSLat8MA21XjKaYLt17noMUx2w7UU2V0kWXXiHDQoB85vyurGlaAEpS1v8W9ssucwW-sdypIwDET_95kSEbjil7H0DqERxvOng_cWo_7f4oi6a7AietaqWJGsrL2ObuJFrMiOmg39o8rlGjFDeyyAybTb63mSzngey_kcXT152LBuCKV4ibe5ymHZdQCir32NDEg7ll4US32NCeZo82zgrG0SH81Ky_5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbKhVw5JYKsCpKVQYTOdnP_WngG6_NUJH5RuvmrESGjxTrkkS4DSwJt3ylTExl1KLH0LJ2sL9sUL-ocCXSphAGg9vTiXaNVQZvnYKjV45FRqsvYzIuYHGQruukJxnILzTVvwMO4qmGiKY21rxX-sDM5cm100G8g1YFmW-M8TPhlw_JnCq6H1wosdMAVkOfEU_XnsnkE83kyq5r6YxCiU_w-UdzuJwTuBF-H6SSNCMHzmlnX1c0AfkVCo44f99a2GaXIrrXv_dqIvrXGJIAbaWmI3IGNJ5tFnmPJWMVDBf0ZgP_qSsW5x3n3ZaHFfSOJnScD6m8BqcFiEeGXUlgh21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7QF2W3wusx98Ki4gwVWIK7o6lo3K0cYg_1W_FykkLbqm23JaIfzyG6vWtlXvkA7MNitaWKSPWvD1nr1MpQy16zExwLdGVphEeooipRK0cB1888rurOB7fbVUbnQ_C2_Im8NX3Ajp6tNPwmZAt0mCDZL_25-DlsbuYiUarOgRIDOqjrquEyExch-fN8yUEgeNXXlX_E_vlhaBUQSohRzpv_sIPL50W_UkVzdXBbtrlgjtO3JHounqX3T8zkK6R7wN9GQ2peQUw1J2pR4pxzUsQsqVkCU7AkLpr95oX8XXIIeRSIqN84ea3ETd_ALcW3oGvTG2TkdMiT4_9jKDow0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLkAQ7OcPSao6uAaNeZVSmixXTf_ajpnqO2WDXVF6JBVY4lMUMcSoyvcBHJBS6YjjjoA3fKs9Th8f0IoM19k6BbgC761wA4jzcJpCXcXxGE0fmu_ECnwB5h7QCBPyTZRLimolrcnrQEOPw-Sn1xaZVm7fb_gQyw_D5CwC2m_xQRYvKxStV4XOdtcFEv-Dr_35hXEuqRmreIeGoLj-3sVzPfdjiQRoVQMOU-zfRXJcmpg08jbF6pYOe_vLwARpCKFJaKwH7NO1_SonGBXA9rG0poVkA2pVfZwVPX8UOvn_iKZi88Dz8jSTwQ6t6y68BRXsMgEXNwSo7jw5l_W8U7jrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Brentford -
🔵
Chelsea
⏰
Tonight 22:30
🏟
Gtech Community
🟣
برنتفورد مقابل چلسی؛ جدالی که برنتفورد با فشار و بازی مستقیم می‌تواند برای آبی‌ها دردسرساز شود. چلسی از نظر کیفیت فردی دست بالاتر را دارد، اما در بازی‌های خارج از خانه باید مقابل انتقال‌های سریع برنتفورد مراقب باشد. با توجه به سبک دو تیم، انتظار دیداری نزدیک و موقعیت‌ساز از هر دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=e0EUyMdKHfgt_kYPNiUauEGROPQOrZL8br2Z2bDeM5Nfw8hCgzc-npmo-KGzjIdh8RB1XPLbcXI7VHfEWnO8r-MHH2qomUNynzqT2Y9sKtTfCSj-m9UDK27UlK7uO3AtLPKxt3vKyanwxiqOLSHKQxQcztmxZjGYrmZTcf_fhHIp08Am8Etmz8ScyRAo_h_8hBh_73MXqQrASFuIb_WtD51J7GIqVwpsHAGG-sRdc4pqlo0SY_FQhCuam4dSfaAubapQIbGulWeN8P60mq5JQwgmSkN6b6HMvFGfQcyk0XsYS68T5gIal-kFgAb1panGDLGBKhOTxbbuGzrE7fNeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=e0EUyMdKHfgt_kYPNiUauEGROPQOrZL8br2Z2bDeM5Nfw8hCgzc-npmo-KGzjIdh8RB1XPLbcXI7VHfEWnO8r-MHH2qomUNynzqT2Y9sKtTfCSj-m9UDK27UlK7uO3AtLPKxt3vKyanwxiqOLSHKQxQcztmxZjGYrmZTcf_fhHIp08Am8Etmz8ScyRAo_h_8hBh_73MXqQrASFuIb_WtD51J7GIqVwpsHAGG-sRdc4pqlo0SY_FQhCuam4dSfaAubapQIbGulWeN8P60mq5JQwgmSkN6b6HMvFGfQcyk0XsYS68T5gIal-kFgAb1panGDLGBKhOTxbbuGzrE7fNeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvaWuyM_Cmab_uNyRaZtjeheRg2LgZ1N0m84LoXo24RGgvrG4vHpnXKci13yOzMxB7gR6mkVPCq0xAZccnyOP8XBhyadPCqwcKSBQGvAsO8CiuMoxQ-0_POP4QW1rh86uVtiwmnwN736fpQJD-k9xDnTr9z-TwDz5L6bbZOvONPf2O_ktqutQLdTTeOmZBME7jMDpS-pRLU7FSTlRc1ttUH8Vmlfu_a82jzBmpWHIHuVVPo1YMelGy4KytY8PTlhCI0i_gPw-g0O8Jl1qozZSyuzhFv4q7ytKHyBS2OpInWdzaOdPrjWe2OoSSjEfTmC1hc0PjxEAVoz1wDjHVwwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=cYyajcw9L9-9kERCZbC8oH7kFVb5vfYaSOpcmGBweyrY2kF16XIiimizdEzzavpq_TgUMYJ6oUjrr7UPZosC0qBcjqxfN9-uQz8bFz4Vtk83rYX19dkRguJw9NikATGiMZqJ6GUphmbXz86nJ_MgiNyxqp_OXF3Uejk_-allJEzxPk-rx06PB4oQXVz6nrevR77TSB9VFwSGhJacXpJEQM7ZeaFygDx8TuAkUgJPyxntyEFtv7oXRHu7mjjVdRTTHjIlmspYnpGGqho3kgQMF4gEhLjMrW8jeq_EGjQTBn8rsPGKWM4wc0qn_niRLpqQwVR0Hqa36yPTqL-41fSAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=cYyajcw9L9-9kERCZbC8oH7kFVb5vfYaSOpcmGBweyrY2kF16XIiimizdEzzavpq_TgUMYJ6oUjrr7UPZosC0qBcjqxfN9-uQz8bFz4Vtk83rYX19dkRguJw9NikATGiMZqJ6GUphmbXz86nJ_MgiNyxqp_OXF3Uejk_-allJEzxPk-rx06PB4oQXVz6nrevR77TSB9VFwSGhJacXpJEQM7ZeaFygDx8TuAkUgJPyxntyEFtv7oXRHu7mjjVdRTTHjIlmspYnpGGqho3kgQMF4gEhLjMrW8jeq_EGjQTBn8rsPGKWM4wc0qn_niRLpqQwVR0Hqa36yPTqL-41fSAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=mYsXfrsvETMaauiu3vby8_6tD-DaPcL7srNwfBNMsTiyYr1LiR65RUc1nGYxCx64gVNXEat5vIWwMEUb3L2XA4EPHJQuB1zlQrE38vc7RQ9xBHqfjnz3pN_m-pgK6HWYkULAEnAgpThWGy0lzcW6P3LpiZFzwQT2-o64FcjNlhEp5MmoeD88rLtSi0VdDI1dQOo7uQ1FMgz0UOg3aWl84IwHMm9D1eQxHdd_50FSEecwGD50SxOgvkvX_hpQuBDRvWNw99hojazmkcZIn93DWwFcXyfxkS-Vlej1_d2nqO_Okt4AebaROESAuV0UUcOXwqtt-Dg2OLSc3nzBH3N52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=mYsXfrsvETMaauiu3vby8_6tD-DaPcL7srNwfBNMsTiyYr1LiR65RUc1nGYxCx64gVNXEat5vIWwMEUb3L2XA4EPHJQuB1zlQrE38vc7RQ9xBHqfjnz3pN_m-pgK6HWYkULAEnAgpThWGy0lzcW6P3LpiZFzwQT2-o64FcjNlhEp5MmoeD88rLtSi0VdDI1dQOo7uQ1FMgz0UOg3aWl84IwHMm9D1eQxHdd_50FSEecwGD50SxOgvkvX_hpQuBDRvWNw99hojazmkcZIn93DWwFcXyfxkS-Vlej1_d2nqO_Okt4AebaROESAuV0UUcOXwqtt-Dg2OLSc3nzBH3N52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQwA0s_4AB1NBVgxrZEIk_Wn4oaDvjYdeOGVfm1rHrx5hpLhcVgFxVyikw9whKuroEGBgGMISufY-vjJOSvtFLQDTXOn69Oou30RHFHFeSZsSriA0Gft54RGkNYHrm0fVLJRgNy6vAhZR22g7PTnw1h11oPhDsgD3hv5XBMJb-tLJDvLJGgd_Htxn6LbbR2b6SofzcjkFB94A7Oe4vs0M6yRJjlD2IcyklwrrGp-jSoYxK5nXRsHTxeqsvPcXReiEfy4MoN6b_B3chK3U_JJKw6ViREN0EH-hqqjvpGum8BD1kzkC4FZ6xeaPpG7Jvr2yabReKZSxgHELOVyas4ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M50b1AbWsz7eX1uHTdIr885v1GITrRZp8XHcxFNZ0uAwV2eB7YrKfebb_5W_Hc4cNzHvBg1ybZpaJ2pmFYKmjiInnOSL_VSJLllc4bZoaXSf3HOYvVnzjEltoZj6ZmqSVqOy4utALJ1SJq3iAx0_GI35LNgR-Spx4wavH6cViZPlgM42er1f-XmaXevHHGkcCD8YIWebD8_iiUFrm9Rgblm9RWi2ZckU0tMILSSZuGrJK7sDYC20Angp4ts5_5N4r9VPcDMPDMhZcD_pHPxnrkNif_rX_P8l-zTrwDP1sstT-7puTRZRPBbTROI4kteLlU4axGHw-I-i4QlcS7WGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن در خانه؛ جایی برای لغزش مقابل یونیون نیست!
[
بایرن‌مونیخ
🔴
🆚
🔴
یونیون‌برلین
]
⚽️
بایرن‌مونیخ با مالکیت و فشار بالا، احتمالاً از همان ابتدا بازی را در زمین یونیون دنبال می‌کند. یونیون برای دوام آوردن، روی فشردگی دفاعی و ضدحملات حساب خواهد کرد و فضای کمی به بایرن می‌دهد. با این حال، کیفیت هجومی بایرن می‌تواند در طول بازی اختلاف را رقم بزند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140225" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140224" target="_blank">📅 12:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140223" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140222" target="_blank">📅 11:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140221" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
زنوزی به خداداد عزیزی قول داده که با توجه به روابطی که او دارد، محرومیتی برایش در کار نخواهد بود و از این جهت خیالش راحت باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140220" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3HwzZGRQgsW8cA8y1FyzWsED1VbBSYwYVJHi8suQ56E-esKNSpBN-30Qlfz0pZDBI5TDExIvs3mN7kT79i6Z1W26PM9vvgWgAh6baeTNxv7F92SFYFi255KI3lOuRDwa9htl4N3poLhQM3yGPlOB2NL3fO8-xm3BzTf_mD_A682ZokDums2fT9Mqfombk6wBsTnLuv4TatOCUj8eFdVQwUIu4hHjFwg29JDr2TBXdxTlSQjHQJbdo1SP5vwKCtlgnEJy6k6XWPtKG3FR70X159nwHcZF-rHBtHC70Ic7tD9oXWAvG_-N2BWHQGjGbBmNws8KGvFZMbclB6U6xFs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140219" target="_blank">📅 10:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140218" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140217" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
با بهبود وضعیت چمن، تمرینات پرسپولیس به زودی به ورزشگاه شهید کاظمی منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140215" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140214" target="_blank">📅 01:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140213" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
🇮🇷
محسن خلیلی خبر مذاکره مدیریت باشگاه تراکتور با اوستون اورونوف رو تکذیب کرد و اعلام کرد این بازیکن هییییچ آفری ندارد و در جمع شاگردان مهدی تارتار موندنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140212" target="_blank">📅 00:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QyHem-P5rGZcTyU0QxIf_VPLwveGZ-sYusqutD8vRU1gBVM4P33Ae_CiL7_fl44PloYOj1oXtR2nwHfo-oBppXhPEt8Vg3vU5hq7wiTeNQBuUeNWCCSXXVnr6xx7HntOFAsYFRk__e_b3dXI_gZ77_pWk5voryNCV4IRiStFcYW_LKxXkLSa9FRfKDdA0lO0lo2z8DsLnOgRoa6q710T04A18hF8_pSQuE-bxu-1YCW4rAqLetkTf3JHJaJyT9_9JdTzGAXc1yQjtC4Ha84gblWjhG-jXnhHIImNQdlNu6ZNpBbVCe5YIELdk_tbBpsHtyrktJ_AHq5s4Pf8r0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140211" target="_blank">📅 00:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
🔻
🔻
توضیحات #تکمیلی در مورد پرونده اموال توقیفی باشگاه؛ از صندلی چرخ دار گرفته تا پرینتر و آب سردکن
🔻
🔻
🔻
در دوره علی اکبر طاهری شرکت امین سیمای کیش(۳۰۹۰) اسپانسر پرسپولیس میشه و به جز اون چصه حق اسپانسری که به هزار مکافات به پرسپولیس پرداخت می‌کنند با همکاری…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140210" target="_blank">📅 00:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140209" target="_blank">📅 23:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=eNaSrE78nTrYO4Kvq9Ed9fpMxhbQnHXtEkHn2cOxGhR3l0IQBn-uJX6ZKNV9i1yOwe38m379e8s_nn-JH-7fLiBZ0ixA2sZTQ6YDK3-pmwL-S5Y_sQXU1Qyvi2VMAW7On5IgI9AqFNshWsfq3cwPY3cJPCyKQbVz5aOVwT5BdlNGJRFwIAIF1-pOx8FrRZaz9ll0hpmFlavFD58jShIkB8MXU7uOItbLPZ0gbffkF-kBJYF5f8VYiwaQYdZw2MpCdooUznFVctkAE3AWq0_OmAWvEm4n-nHjc4WMgg-I3JAlR5kVEscocD3Qes74a_ChBlWefu0QEXOHYyBV01J7ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=eNaSrE78nTrYO4Kvq9Ed9fpMxhbQnHXtEkHn2cOxGhR3l0IQBn-uJX6ZKNV9i1yOwe38m379e8s_nn-JH-7fLiBZ0ixA2sZTQ6YDK3-pmwL-S5Y_sQXU1Qyvi2VMAW7On5IgI9AqFNshWsfq3cwPY3cJPCyKQbVz5aOVwT5BdlNGJRFwIAIF1-pOx8FrRZaz9ll0hpmFlavFD58jShIkB8MXU7uOItbLPZ0gbffkF-kBJYF5f8VYiwaQYdZw2MpCdooUznFVctkAE3AWq0_OmAWvEm4n-nHjc4WMgg-I3JAlR5kVEscocD3Qes74a_ChBlWefu0QEXOHYyBV01J7ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/140208" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
