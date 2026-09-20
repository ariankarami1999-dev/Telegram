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
<img src="https://cdn4.telesco.pe/file/WkXX0hb1EkrerequuKLBh1TVqyuNAUmcKlhB5_Op_Aelbbv_VGauzVpOiG_xLdFSLs29uEz5Voi50-cMcDpVARKC-_pRDxlu9R5IuKJVGa_Hlj5NNIxgHoA3F-Vhs0mHqdskLlp6YSxOeEGlaS-Oi7yEQaFhdN8n_AnRAOPZ1YzTRYA7jRBzjopHTjShz41hd1SXkigSbg_kPxlXX9B53bTRdZUEjNt6J50qkZcvP3b8Y9ivwVOssrX9WLstHBwkotEl3Wzu6uQ1UKlCUvGdb9Tmww8ftpM5IhgDta8shzkiWZtuq3ybdE2bL1VDAGoWPtgynFR25ZVWRsMOQmeIzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 04:00:47</div>
<hr>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qv9MokZpGj6Ih7pwmBePtjHssBeeuVEi4ZyUS_bPnq4CqfC2TFt0MQ6fMds0B2rD0O1YMXB3mKTU8Ro-FDtJRcpx4-F4MAA56nbnRF1YCFwFhZ7YCs_VzcMciUL8o1h7X9lTCMwcADh6sHQ336sNWbafQ_5pkXjjhr7pKTEjFAj8i8vdEkWw34shPZHcobL6HgeY61BKSiwFBnpIXMzHYFEySzTaRQJqE7-oqaVMMEwnWCslJ4ju_xtpNs_PoXVo61mBZawyR9xllKdOlc__xCwSpZWuBEQy0M52FFaVtTx0O4wtQIFp6vspQOQM5BuyUfXkldoj9dINAQ2pfuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHeF9Lpknido5yebaO7DwZVt9TvoqEi5sJZUq79x7PlQ5YTaPNK9d8pWho-Cxt2jh-flq9y8d5hu1cfTd4Azcgi7p-28NFZ6KzJKEQJUsZJeGSZ_zCcGPo9FZ5BDmvMujUta2IP27y_1nylbdqeesXzUk79eMjhSzGf9El8qpc62Pt2pNZGrdmo4FmikudILr9Zyc86Mu74ulvy6Zx0MZ-caOmOZJ-fVT88YDH2sPd3a5COa_O-0DOUwE13Qg3OeAIIks_RJl23gONtfEAM9gp8xfOGTLEuzrUNe6EaiRp-r1uJn1C8e8e37WOpYQ6TOPuf6zGtKk5xRTLbX0O4EFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3RnrQzdprBeWwWrp3C9MPvEpK8csg5JUc3OO8gLrQNbSQEkj8emqOGUtzcCo7y33RSV5V45DVPJzV-16819tke3RMzyWUOnNbkfcfRjwENAsl_tQolLhDTsf3JBBVK4DO8dqlYARH5q6vVa4XzgiUyWearwMq2gL7e_l3ZY6pYVAHTz1OhHt5hlWgv8JVVJv4mqau2dBtv1-iH52GXqCi1EouRAiW0xYiQ9XE8jtIRjqvTdWSv36mxiPUxYVGZV8_FCdzJygOX0-yiK_H_y050SY2tJHMNg1jtn6W0U1HSnCBs2lK13RTd7MeTg8NJwdsLdpCvEUzczgNVtKPGvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkXvrEMqqCtG4PmE4qVkCmMf2Qr0jBOh_-VKYXOCKcPFNGzoUq8g1NJJAlxoTWXE4Z1VS-E5ZxR7w12sRlbTzLcCLRSbMXVkbv4u17pZ-MnZ6xpxuueZtDtMdz9v1B9ylQGkON6_DRUr-gDMUB2ab8VlikgoXHpF_Ho1kAfyg2HljM6VJT5cRvr9-49tyqivgK-52Gm0YdfOPe5pX9aj7Mlewdh7E5r1HdNP1nGPeXLALMHI6J2lGxMnpxRINZdhejx15uYzmy1LEicqIydfG_xz1BnSLaaoZy6FxPvsmkzd8AdwVSB-1StY0Yn4mvZIBIaonBgtLKv5J0wjKLH49A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7l06Ku3XP_wYV8a79YCG3NlzJ7uA3RuvdQ908XWS4OJDrGiUNUkjP1K5DJx77xHO13Iy4tJeiD3SDtLJmACWqinr_BnAKM7e1q8s3e8Br5KIUQGK9BWzhFRSYPA0qsxT883M1IVFDgFros6dJSylQvzA3kw8QvAkRxecZ9SZ2pGOlsfeKIitoG60fwFWiZDxUGyMgBPYXevQnvUmSS-pVfp_gPcr3n-d7Sj0dk3AvsoBhZd92Dzu2sfFYSMsbwD6T5LAuwx61XkmW93QhLubZZpBLXsufVCPmXmiYs-AurcEE6ey91G6uNhoBtvay9n-cOvvjxlpP_nHoCVKHaQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5wYhcu5gf3RezChzOJlddYmQrZj1E9x275dT7zlc67bTdSABTyqDiixRd41O48Ohi0HOCnoT0dZXQoOlPvawbLkqZA_Zh2Z6e_B7NzICk7Th1cq2nM0YqhMPt6lOv3CAgBXfY67VmSkCutiBYLdOpkxWavKhg2plGXWEx3sgpDqlseWBSdHZ5pVQv_pf-hlv7NAdyF_H47ROo5L3Lgyb8IM1bO3fqZTlD97mFErXE1_eKOf8qePncpgVwWHbRf5miwv86fwmxul0dKSrqJbIYoGShkV8F5uPN6G4LvV4ziL_w8NIiNHmKKMZSCCtzO7lHFSoMvqF-dckyleWNaz1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7cr78q6obd14JX9sItIzR8HYpRG6l2KKTrFdqu0PLIomOtLyDa3b5Y7iXeAHWRZjAekJawYrn3BxeZ-mMHik_G4mm_aul4ec8EAg2kTRAI5BhQSQ98WeHfHueqkRjTl1QRlW1mwBPDcDIRyd1-dL_6F-OJqzsyFgETQpo5CpPuoil0okCJO4g3keYqlp0g_JFK6MD7NciS3ctYZ6do38nrRYXgVMfkkg6_cnHBB0NG1PUvo3AdWZcoFJQvnXp8BzUAx708nhbGn117iPenZ28EEe4hbZ6klhyKPLNtDa_A5gAn0wzN4uZ3D1JF76HMzJ23PFpcQRwo7tBO0thN1Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7BFJVTuUvz3Dq3sEO7cKxO-CcCY8t5nijCTLw4Kn5Wvb7dcPComv4Dz2GIY7qY_BjJHF-UY__ipQPfqdU-6bw_LbD59JAM74eu5vaeUVI0ra7zmNrHJ1gsPINR9_HS87osgf_Ehd4of7B7MVinrKVh0iKMa1PASUjEFASwWjwBCgFjR8qccoeYP99jbaHsmIAZoLYAMU5h97-g10nXdCDMZmPFKJKbCFRNPpBOwbF6sT6m1L9V8GNeEhiU-U6DRi329NUC7Hkn1lXj9IMtLSRVShgS-pNkGh83bqwNSP9fJRzbu_yBoOyvJBpI50obEAV6wReduulXwTOJavQpqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEFUlkVfYiKtZrgLbIfZlXQMes5CVA8xjtlQEA2RI_isR1jLIYev6TGaeltpbI8H0a3O70EiKax9TPSs7TzB_Rhj7YwQpRL1oORhZv0cPQBAmn7hCN3g6u3sE7wHCk50U3PTJTSKI-VWg0dow25tk9zU-bhZA22NbDwetibqE9wVxvOCX8KVZakOUT4Wt7Wjh_VBl1eD6FxXLSlQZ_XMELFvHql_P5VfluMLseOSaNM5vOsK6CiChZFeshFLHSzCtTtcY9E508Au4tsLPFJwYYMb7PnunDH4sjWU7rYDbDOpKsw1MnXH0mi-_-niIuJdKePzuUp2B9jXtft_4XBj-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU2BDBDmdiFUzDPaKvZBVae3uXkOOWQ2epdFbXMEcC-28aT-Vjg1Q0HgdCh_v3kxRdcdRVXLEQK4r0BMvIm-YBGMwB6l-MVX5djGppvZx6qic-eFVZQhsV08xpVU92o4h7tyB80veEbsSctQQCWcnsbbsHcR9s6d2ozUbVpjSx3RUVPVIyJY-1OQxUVcP6ewpajJ-PshMfgwpbvvrDTXLnKCTlLbwjtwct07C0VhlqOlq5-lh6u_5pIgMOxzLVakL0mO6snZ_f4FUAOLm-V1M6Dt8FtnmddOj2JHzybD0bPtcDxqXMn4nA79suCFVy7Tz6ASFxE041WkktXwARqJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=iegn26_zGkOHpD5DSBwXTRTswMbgSildO2uwqtoRNQecb_jOH8DqTxcapy0GFzmJkEtQUlPF3mnT2_xCRKIB8PwF3mYghmp6qwKCWFXyzHt_h2y4c18jfeKYB1ba3E0vTmN9YYEZ-Upyp1CqjgVqbkn7rnqPGgbDgqGOIk-wY5I2JBnlYT0ceVR4dw67eaQHX3fWiHOXWybkPYuyw1Lp0z5L7JtmIgdFx2QOStOZ8D1tBs1LlqI9OJAYTLh-_ent2LG2cBMpkzSBEgNRiKeXN_93qEur1R4Z0YXgNuvivxeQ_X14R-SIwEJYfB-BYTbNrxPSaDZrIWoEZMnJ7bgqSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=iegn26_zGkOHpD5DSBwXTRTswMbgSildO2uwqtoRNQecb_jOH8DqTxcapy0GFzmJkEtQUlPF3mnT2_xCRKIB8PwF3mYghmp6qwKCWFXyzHt_h2y4c18jfeKYB1ba3E0vTmN9YYEZ-Upyp1CqjgVqbkn7rnqPGgbDgqGOIk-wY5I2JBnlYT0ceVR4dw67eaQHX3fWiHOXWybkPYuyw1Lp0z5L7JtmIgdFx2QOStOZ8D1tBs1LlqI9OJAYTLh-_ent2LG2cBMpkzSBEgNRiKeXN_93qEur1R4Z0YXgNuvivxeQ_X14R-SIwEJYfB-BYTbNrxPSaDZrIWoEZMnJ7bgqSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyldCaG_FBG_Zw0nypp7YqeNrou8rrbJIGG2Gs4g2JzV-1VzSAThSlGt7BF0pojx3KWimPBZZGTAoKQi_sbG_BaTCi7pCUeLdiaeHZVHHwUscwl9pMpmEH5yvN7yAxLVDmbxnalJlVHLIpGYqh4z0B5bZPegFESGfrQNvVgltL7-IkA5u7r3oD3V9iqc2jpQiJ-huMg-eVwAOkbrHnyAvBvbFNat6OuKrBPw7V7SB7efDF87t7J61UnGYWOCvt0Xb8oITfBN5E7xnxhh8PnQFVt-BQ7wK-s_FnEFsCYqVEdcM_mQucYGtCIKRKAYbSqVhmqifrg4pZsO_m0WkiXpAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD-AMNHFb2zO8lRtu4PXu9Bg-p1NOKabaGrHOSrp8XUL_2XEushTmPJevPqGlDL_TxYRGZHUz20pmrHk-hMsFzOq7uOMARqRH4MqifVtYeucA79ztUwE7MQazS0MEZXhBghnfLgStM3Q_g5xMzFzX-nUPoqCvt9-NYACqMA_ZB3_IwGYmJ65UFG476ZRbrnkSUrCjBfWcs4aAFUxtLsq-8H7EMQnbiSuzdC5Iu6MsiNvKtaZRsOWy0fkDIFyVXYkJaTqiV_Pq3-92KrRj2Wsvtdl_s5bHKo-kKxt6GO_9cVeXWQQpDrlJzuc1bwgP365WJTFBDSAFTUl9Az9lp6lnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3F0DJvjjzA9DEUiU4cc6h3GfSLZUBsC1UXCtR_Bv9I7h0JmfSb23Ohl_fX1IzfjV6Wt4Vy7APPDAf2jGeWzXtaMPw8RdGSVjYWcccY8WAXNmrOiQ6hYS5xIq-5FJv8jY1zh_CtGmbnxnexY9JT_2sBciiQ0uUuW7L5r5XsKPd0YhrH1ucX-8XtmaI1D-IRKRN86hFYB9WX2m1v7v7JWltZ_KcLqj7BASjGtZm4vaJiePHrVv01C8Ha1EuLIPCENniyayVbYzGVwrHfSER-d-xiVwxMfg_7SsUt3EuzRWatshMYy0RBpKwoqEEo9U8FdN6Y7d3jorzSHvSLTb0SNiB08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3F0DJvjjzA9DEUiU4cc6h3GfSLZUBsC1UXCtR_Bv9I7h0JmfSb23Ohl_fX1IzfjV6Wt4Vy7APPDAf2jGeWzXtaMPw8RdGSVjYWcccY8WAXNmrOiQ6hYS5xIq-5FJv8jY1zh_CtGmbnxnexY9JT_2sBciiQ0uUuW7L5r5XsKPd0YhrH1ucX-8XtmaI1D-IRKRN86hFYB9WX2m1v7v7JWltZ_KcLqj7BASjGtZm4vaJiePHrVv01C8Ha1EuLIPCENniyayVbYzGVwrHfSER-d-xiVwxMfg_7SsUt3EuzRWatshMYy0RBpKwoqEEo9U8FdN6Y7d3jorzSHvSLTb0SNiB08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1_VTEvjXWBuDBDBhESA69HTdiKmPlhV8lzfd61Jm8NPg5mHrxgs-CNOXceVetKkBijZK6y4R9uHq0Ua8uaAz-i3t0DLAiCKdtLZksZ02rddNMn0BPc4lHtf7B3cY-mmasSfTIFdfNynRSWvPTiyiVQtG4B-8OORSTZW14y_m_cLh0aXzlZ2omYd5GqpdytOYKaWAOOqCE-BwQfM0YJMbQGUP0Ovmn4-_lPxVl2Q8tnk5en2LXtVyhpyUSiK2Nbco1lm-zUwCvqAHFk14yrXzqKX7DsOXyQONXuHIapRf_tRlocZer1_9RNJx3NKBmn8JB-QUDc71ukkU3uu-WlrOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7QF2W3wusx98Ki4gwVWIK7o6lo3K0cYg_1W_FykkLbqm23JaIfzyG6vWtlXvkA7MNitaWKSPWvD1nr1MpQy16zExwLdGVphEeooipRK0cB1888rurOB7fbVUbnQ_C2_Im8NX3Ajp6tNPwmZAt0mCDZL_25-DlsbuYiUarOgRIDOqjrquEyExch-fN8yUEgeNXXlX_E_vlhaBUQSohRzpv_sIPL50W_UkVzdXBbtrlgjtO3JHounqX3T8zkK6R7wN9GQ2peQUw1J2pR4pxzUsQsqVkCU7AkLpr95oX8XXIIeRSIqN84ea3ETd_ALcW3oGvTG2TkdMiT4_9jKDow0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=ndO1IwyLvYapv-6erP-ETlbwKj5pzImymQUQvo2tuoSQhg94s8L0T8NsPz3Zwgz6bk4a7j8FCT7nPGVzY4kAiSfhL84VMFrW5YTs7oNCT_aOVPM1ly7szv9D_FsXBWe1sPP7b_aJq0HTwt1agxOBzwCpNcvaeN6DmIvhlUM6yb6jYADdPI0nmh3F-XgiThCbJL0Q5QBBAHnugEFKR7NbAqCBUU6YjRJDOvMtxirch9WgAYJ107JtvJ-iDsYsoBoH6EWuYgFNxlsDkhHf57uSIIg08zbd90TtdgE6UkU4Z17KRlScjxvWcpwqsi24C6Qps7Sd3-k14YP8-nIT5I_FnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=ndO1IwyLvYapv-6erP-ETlbwKj5pzImymQUQvo2tuoSQhg94s8L0T8NsPz3Zwgz6bk4a7j8FCT7nPGVzY4kAiSfhL84VMFrW5YTs7oNCT_aOVPM1ly7szv9D_FsXBWe1sPP7b_aJq0HTwt1agxOBzwCpNcvaeN6DmIvhlUM6yb6jYADdPI0nmh3F-XgiThCbJL0Q5QBBAHnugEFKR7NbAqCBUU6YjRJDOvMtxirch9WgAYJ107JtvJ-iDsYsoBoH6EWuYgFNxlsDkhHf57uSIIg08zbd90TtdgE6UkU4Z17KRlScjxvWcpwqsi24C6Qps7Sd3-k14YP8-nIT5I_FnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=EGTzhDiVfPNTP2BR0bBYxl-nEiNW4E3zadeDK0EQa_cIQ99qWsnHxoCG6BYhwp8zUsL7sFk6KdxNquODt9yc_JVcNNJwNSbMBRWUPDJDMn4itZRgo_bn5VesaGUmZT1qhitjdPuvpfotW2277mzZZfUBZOmic0XNd-MiffLr43h_9ruGuv4gKhP5_0eFRrWTtf8G0b7Xnjsol3kZsONcaZ9Bd9-37QFyUJMVUsAuWGNjMteEWdLPzbf4tLGPIups_WNauNxaMg8DOwETg5L5i30lvpJQ9V4CqvQffE6EEqT6Lyf5wMwIyOyNqgU0BRffVGKuEyjZaYbUjIreHMHyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=EGTzhDiVfPNTP2BR0bBYxl-nEiNW4E3zadeDK0EQa_cIQ99qWsnHxoCG6BYhwp8zUsL7sFk6KdxNquODt9yc_JVcNNJwNSbMBRWUPDJDMn4itZRgo_bn5VesaGUmZT1qhitjdPuvpfotW2277mzZZfUBZOmic0XNd-MiffLr43h_9ruGuv4gKhP5_0eFRrWTtf8G0b7Xnjsol3kZsONcaZ9Bd9-37QFyUJMVUsAuWGNjMteEWdLPzbf4tLGPIups_WNauNxaMg8DOwETg5L5i30lvpJQ9V4CqvQffE6EEqT6Lyf5wMwIyOyNqgU0BRffVGKuEyjZaYbUjIreHMHyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwOfP6fjcNL6VcMwQ1loTxiR60tnxM4ovgSbfjwkht3AI7fGAqArWQzSGuAVEqp5y_SdAL3k1gdtCEGq3Iy9m5stX0RKA33uitYYMdR6JgHMEvH19Hy_uWtR69KHtsMFskX7lMpZXci-rnho_tnwe5Typnke8XB6hY2aWda-MGyrXjTRnSH3dqzmOQJJodCC2Z3SARXuwdbqxbsQrZiNgR1UTizw0tZIw7qfYnq4Uk1yeyvUbX3GmF1cSrkplZtSlS1Z1kxvKQ3-EZEoQtYwiIfZEz9PczveAK5QjLtisGxa6xQ0c-SfOICPkGe-3ClJOWjWLnJrB2pPx2gnrXD6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckJTUg2QIt7rqQJDPkoCKeGteHHRDT7UeHAxYJSlgLptNs0Y4icVRPtaXJg9Ccj8o4HJJrfn_kTj4tJrFaZvoEyWdb-QZNjLzH7oLzC2vuXtXUrBofFk_otHZWyORq3VU2-vZkdKg_4_VkNMorEunkV3sEd4jjHLP9qAi1vAVqGgG1Hsm2YlQnVV1XzJBCPCf3LOPQ034z8OoWQ7ePyM-BFJ4zjFbQtLocjMbJILKffcX4Q4HKOueEHRqOf4R2mhN0a19JL7PuODYLlEQXA0x7ModuOnGRwUxCHA86wyYxMU-HA-T-pyjpP5h-vze_ArFdZJL9YJX05rAs3Pxa1EgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140225" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140224" target="_blank">📅 12:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140223" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140222" target="_blank">📅 11:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140221" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
زنوزی به خداداد عزیزی قول داده که با توجه به روابطی که او دارد، محرومیتی برایش در کار نخواهد بود و از این جهت خیالش راحت باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140220" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McEJA-Lwc3l84yUaJSqpqdG322TiYisf_UNYrCdQzan9N7rpdI3_PU2-rK91e82mYoXaZ5R0pO4rGtoQD7Rs86_psUEDI4iDOaSZU8ovPDE4cWWQBfTyWQU8LWP1r8GFYufF6JHYg1qHwhrsM6enqvoitjPa-RpbaLrlx0qxgJ3v8X3XNKhMBSGwpB-Q5hh6NkZ58M6uoh-AeLgjjxhH6J4xH01jBTR75nNwaxjeErZ_QHQ6uRd2y2rUonDZuEmKUUJBrVjgD8PbsYcxf1CkMcpQkeix40aSd1XWb3zZKHIqvyVn0fre0haOXjxVQ_Gn2D9ZGClj84nvlRNBD842ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140219" target="_blank">📅 10:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140218" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140217" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
با بهبود وضعیت چمن، تمرینات پرسپولیس به زودی به ورزشگاه شهید کاظمی منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140215" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140214" target="_blank">📅 01:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140213" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇮🇷
محسن خلیلی خبر مذاکره مدیریت باشگاه تراکتور با اوستون اورونوف رو تکذیب کرد و اعلام کرد این بازیکن هییییچ آفری ندارد و در جمع شاگردان مهدی تارتار موندنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140212" target="_blank">📅 00:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_L3nGeb6wDx_kawZbkMm_kCY8mr9AkPHj6sEKglHEA36bQA1SskkANH-N3h1-2y8P2cmGDgtMndcjKWWCUrqcjWnNKbkiAjvM4iY13jdHXL3-PJAaORnGKPsMbyQ8vK_WJiiDfG2QXh1V5Ekal3FPQjJU1rMdYDrqBiTOkUSLx4pqZuZkMYsxq2XhUGj0eUia1mdWKN3T_63iTXZYReYWv8-LYgRPbsbXIxzCf59D3pFh60099ZlFiu9auQm9e4LTVrHEn7nz-ssomCw3BpWciqjNT6hwXPD9Vti-brxaQmbNvLEYycxshncizP-mTaCCo4X0ChAptVWfjmO5m9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140211" target="_blank">📅 00:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
🔻
🔻
توضیحات #تکمیلی در مورد پرونده اموال توقیفی باشگاه؛ از صندلی چرخ دار گرفته تا پرینتر و آب سردکن
🔻
🔻
🔻
در دوره علی اکبر طاهری شرکت امین سیمای کیش(۳۰۹۰) اسپانسر پرسپولیس میشه و به جز اون چصه حق اسپانسری که به هزار مکافات به پرسپولیس پرداخت می‌کنند با همکاری…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140210" target="_blank">📅 00:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140209" target="_blank">📅 23:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=FBP7MMw7vwboDOY3ca4lTrESqucyfK7Q9BqwsIJTBtTjrpFuQO5qq7VHxnJ4jdsbVKYgdo1fvxa_44RrYWCt924FbMB1tM2N6zAOz7dX1krYL460IZvycYbOj4COwd2Ka1O3_M7IjuJh7PKFQcRVBiBQ0lVoIsRsN0ReVSSy-ojK9Zuvc1o1iCyxCnxctFe0ncWZo1o7qw3qJItuY_lMFpnlabjC5rCHIGM5hGA45ZBjjTw6REtZk1_CB5-m-vxbA00dyK0B4FzqTjFe54Z-JAWZkkQcqv09xlghe3yK0cMKTRvwZROPAA73xTTmXfv5mMSfp-VgR8Z7xtfVjdm9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=FBP7MMw7vwboDOY3ca4lTrESqucyfK7Q9BqwsIJTBtTjrpFuQO5qq7VHxnJ4jdsbVKYgdo1fvxa_44RrYWCt924FbMB1tM2N6zAOz7dX1krYL460IZvycYbOj4COwd2Ka1O3_M7IjuJh7PKFQcRVBiBQ0lVoIsRsN0ReVSSy-ojK9Zuvc1o1iCyxCnxctFe0ncWZo1o7qw3qJItuY_lMFpnlabjC5rCHIGM5hGA45ZBjjTw6REtZk1_CB5-m-vxbA00dyK0B4FzqTjFe54Z-JAWZkkQcqv09xlghe3yK0cMKTRvwZROPAA73xTTmXfv5mMSfp-VgR8Z7xtfVjdm9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140208" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140205" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxSJ7e8iaGpKJZh0lS8zx0j4dgmDqkWWvx1B3loTXH3jla9JNjrfSwRDyUvuiDSzaRvLk1JGATvr1kfK1d0TG1LRLiGj4HFhuyqjmIkBZFhYbhPUwsbdjzrY4877uziEBgGMrnxLd2oOHnY92sSUuOPXwd-pvLcEPnuchxZ1lYXY6dZOD3TkTs0UwbHgV4kzhk-VXQ9Yfcocc6ph9JSjzzD_fBua-W_QYwLo_t7Im5di2Yv_mUTPs3klBWGvW1-gP_tN2ESc55EDuyRCPZrK9H-Gj-PKEXltTEpgk_yeVMkhMD8yV4CURhUutObVu6r5_ukKnGXzivZKfM7pT2SM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140204" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140203" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=b17rXToe7qqYQDQbu9lyyT8N5Tc2ivb-I75hrtbJaH8mc2pvda7BIq1U2z95utZb_uCEB_3QjsZGm0qdcLYKHuqkA5oQcMj6v3ErnQGOpIw7gzvM9rNRgvq5SDUFFAqajri1tg43dNV1yxTQN8I2LNF9VY19UIb4BEtaMtIKILagrjx-LWDx-3FGI91o0zXhKWsO6-dYHuwddXJLOql1UTaWISBKr-FJaoUPID6JdefmGyb3FoYN-N9en0Fj43dVmVxalQ8JNvgb-FxoV47U1I1D-RToaDPz_XNbmMLNvutwCQUZakD43SHIICNopnl7qf9E4z4cPEQjbUiBHuTztoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=b17rXToe7qqYQDQbu9lyyT8N5Tc2ivb-I75hrtbJaH8mc2pvda7BIq1U2z95utZb_uCEB_3QjsZGm0qdcLYKHuqkA5oQcMj6v3ErnQGOpIw7gzvM9rNRgvq5SDUFFAqajri1tg43dNV1yxTQN8I2LNF9VY19UIb4BEtaMtIKILagrjx-LWDx-3FGI91o0zXhKWsO6-dYHuwddXJLOql1UTaWISBKr-FJaoUPID6JdefmGyb3FoYN-N9en0Fj43dVmVxalQ8JNvgb-FxoV47U1I1D-RToaDPz_XNbmMLNvutwCQUZakD43SHIICNopnl7qf9E4z4cPEQjbUiBHuTztoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140202" target="_blank">📅 21:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140201" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
#فوری | ترامپ: هر اتفاقی ممکن است بیفتد
🔻
تصمیم بزرگی در پیش دارم؛ آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است
🔻
به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140200" target="_blank">📅 21:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1goTy2um_2gp2F8BFN5wqDWBCYk1-IgFu55y5cfIK0q-Pikrp1L55ROVcBX0jheeIdbOUhv37EeB75HglWF1q0ocONIl5JyHE2zB3EFCLlsMt0_KBAfSoWGD3miJXYJ62SoaBNlAp4-tn98mPFoQyPd6728XHdu3Qdu3PYM_eOQJM7v4OfOlaTCmFyLAImC3GDG3yZk25QNkLqVHupjSESiHgZUJ8eKHHYQwIN6riZX6pInx1AaHd1OmTWnzQkdbzeFAH-LpdYPxI46YbSBEejqSFvFYAoPeHFVzBele866J4irru8OAq-rpPUyfiEYtVG6wFHPl4MTB_8QZyeHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
❌
❌
در اقدامی عجیب علیرضا اشرف مدیر رسانه‌ای پرسپولیس اشتباهی عکس لخت خودش و پسرشو فرستاد توچنل‌رسمی پرسپولیس و زود پاکش کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140199" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
