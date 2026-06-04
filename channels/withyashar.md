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
<img src="https://cdn4.telesco.pe/file/p3vWM1xK7feOaqLbHVAzHegouR5ECJzbnjlpbFbuaYsOusk_oRrLiYUxXju_4Picg_KzHbUtLaLztJ3f4ecdwsxYzVHhVXdwj2w9RSYIGvZc0Gj_l-JJppKWHOvlWzTatzchZZ03Twi4uGikmqj8Go-zkRFr09F4FyljjX-D2h881hjlOgjOOZ6lExzoq04pghcGu6EaWifYXR1fAbU-iTJmsk15KKksncSYMUSFq2WYpsBVrI-2vq905xrN14ZziKZypvosKvC8f6MpETHZYO59JzDjeADgXAiWfCYzQ3uehdPXCE8mzzvYJG3rEYGyNJd2rzi01ofxZRXpTbkxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-13503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">@withyashar
قیصر</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/13503" target="_blank">📅 20:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=eGnj7MLcZETWc5yUd3Uq_fER27dvbfnxI6BYRtA_IzAYhoo1rknfoWJefi1gQZsnbEnwgoPTWw5auBdDsPsU8TtX6Zg4qDsaG-xnhqd2jJ9HdNY1cACTfbiwSH2XRcDiqH7-cPsoBJiN9e_p_AeDf0BsxnF4y6FWE5ChEHwWCJk12t1vssHOq9Dcb-C4sg3osA9uja7WlGHG1bMgxosWWuowsk2wQLRPcxUDtol-zKCLbA5L9KmNCIQm9T8TRwnJMw69Vf3W51uS5Hkqj-11lG1lNeeOO_yLT_EUQjz61tSz2781uzXsF15I2VUx0ZLddU7_UebNyW5Nm-YZVNdkjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=eGnj7MLcZETWc5yUd3Uq_fER27dvbfnxI6BYRtA_IzAYhoo1rknfoWJefi1gQZsnbEnwgoPTWw5auBdDsPsU8TtX6Zg4qDsaG-xnhqd2jJ9HdNY1cACTfbiwSH2XRcDiqH7-cPsoBJiN9e_p_AeDf0BsxnF4y6FWE5ChEHwWCJk12t1vssHOq9Dcb-C4sg3osA9uja7WlGHG1bMgxosWWuowsk2wQLRPcxUDtol-zKCLbA5L9KmNCIQm9T8TRwnJMw69Vf3W51uS5Hkqj-11lG1lNeeOO_yLT_EUQjz61tSz2781uzXsF15I2VUx0ZLddU7_UebNyW5Nm-YZVNdkjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حظور قیصر خواننده
لس آنجلسی در جشن غدیر
🥴
@withyashar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/13502" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/withyashar/13501" target="_blank">📅 19:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">داداش این خاننده دوزاری لس انجلسی که اوردن ایران پشت پردشو تو باید بدونی دستت تو موزیکه
پتشو بریز بیرون این عرزشیا عر عر نکنن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/13500" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد،
زودتر از آنچه فکر می‌کنیم،
سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/withyashar/13499" target="_blank">📅 19:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس با اسرائیل را رد کرد
شبکه المنار حزب‌الله ،گزارش داد که دبیرکل حزب‌الله لبنان گفته است که این گروه از جنوب لبنان عقب‌نشینی نخواهد کرد.
نعیم قاسم در این بیانیه گفته است درخواست این توافق مبنی بر خروج نیروهای حزب‌الله از جنوب لبنان، در شرایطی که این منطقه زیر آتش قرار دارد، به معنای "تسلیم شدن، شکست و تحقق اهداف دشمن" خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/13498" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وای‌نت: موساد در اقدامی با هدف سرنگونی جمهوری اسلامی، سلاح‌های ضبط شده از حماس و حزب‌الله رو به کردهای مخالف جمهوری اسلامی داده بود.
سازمان اطلاعات مرکزی آمریکا، سیا هم در طرح استفاده از نیروهای کرد به‌عنوان بخشی از تلاش گسترده‌تر علیه حکومت ایران مشارکت داشته. این طرح در نهایت پس از فشار رجب طیب اردوغان، رییس‌جمهوری ترکیه، و در پی هشدارها درباره خطر گسترش درگیری منطقه‌ای، از سوی دونالد ترامپ لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/13497" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9fpnspHUKk96FFruDsl0-h62FbYkzAMgpFypdjac7IWqHFVh-4jt4G9fY48VoFIKSBbFIZCWqaDxOD8orVafLnKK9tUfholg5OnJIk3StoVFOFVsiu-i0-6EpOyUOfnEPWArIyTIukGClI3bm0IT9vRvZAYPQ2ygA1bAxiafBYF51iU95U1WUZrQ0DcqH7ndbPTh2eWZLYz26iLGn6szJ_ntoFp3puC3pr3TZMXeUhIyJbePcV-JB7Tx8-qPYrfNeR1k75zhsX9jGhWzFmliqgH6QGW2es7mqenddEnZTBwVlO3VUFYg7sDX5XtjKM2G1uAUaITlcUDyzodpZ30qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای کاتولیک یک جن‌گیر را پس از ارتباط دادن مشاهده‌های یوفو با فعالیت‌های شیطانی برکنار کرد،.
جن‌گیر مشهور و قدیمی کاتولیک، استیون روزتی، گفت به باور شخصی او بسیاری از مشاهده‌های یوفو ممکن است ماهیتی شیطانی داشته باشند ! وی علاوه بر آن روان‌شناس نیز هست. به همین دلیل وقتی او درباره یوفوها صحبت می‌کند، سخنانش بیشتر از یک فرد عادی مورد توجه قرار می‌گیرد
اسقف‌نشین کاتولیک واشینگتن این اظهارات را مغایر با رویکرد رسمی کلیسا دانست و روزتی از سمت جن‌گیر رسمی برکنار شد و همکاری کلیسا با مرکز معنوی او نیز قطع گردید.
روزتی بعداً عذرخواهی کرد و بر تبعیت از آموزه‌های رسمی کلیسا تأکید نمود.
این ماجرا بحث قدیمی درباره ارتباط احتمالی یوفوها، موجودات فرازمینی و پدیده‌های ماورایی را دوباره مطرح کرده است
@withyashar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/withyashar/13496" target="_blank">📅 18:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLMR7J7ZFncY-z2BVXT2qMsbRrSj-qpOZqzM2vXSkyqJ1sc5GawmLa5JNQZd0nZPiKFQp8zCXn8o1KET3H0gEaIYCNIjGiMWOPsVnn-VQ7fzyExdv5zH0g8dG_7Aa60xlJAoc6ampkS9aCZjqx6gz_Pn8bxPNVw4jiDZACRxeX_PNF3nCJbK6ofT7lJd66lJ_JoT3mf4_y_fR6C5bZZHwZ-eJAg6qaNjAW5Ii4Aoo3n_jNYEGK7ehF0wJD2u95CzYocW-RGSujsbndCHQQWX8o52GskOxLauQtafMs3oytg-TmdxGvFLydMB4VR1nN4dD8SOgA84BwpOePmeIKwjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم رو بردن تحویل بدن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/13495" target="_blank">📅 17:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/13494" target="_blank">📅 17:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اصلا جان بر کف و جان فدا برای ما بود اونا گرفتن
😃
🤣
اون عرزشی ها کپی‌کارن زبان فارسی‌هم میراث ما هست نه اونا ، شاهنشاهی هم میراث ما هست لغت شاه هم کل دنیابگین میگن شاه ایران !</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/13493" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مردم به ایلان ماسکم دیسلاک دادن موشک هوا کرد
😁
شما توجه نکنید پیشنهادم به بعضی ها اینه که یک جعبه شیرنی‌بگیرن و با خودشون آشتی کنند</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/13492" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3A0ioUuqxgY12qZzgT5qU_fHHfvXI_4-QQFKEgLdWnGWRSpmzAmUKEVlRkwmB4s0Zz2ejtK6wSpmDA2QftHNARUJk35_EWncHT2H2fC9n5yaCaUZsDPnDF22wxP4AjgRdPEhYVh9uKvcf_30QV6LNePWbZa1-lwwjjydPm1HwP7aWPdi3ErNMiRVh5yp8nBuJy598JMA4Fibq88-sTZNDuQeL2S4RatnhwArMHEzg_ckeOgJAUYqv-RmycankJeY2lnqMs4plDsfrZuUD91lxx0nu5q3EBAvgbhc1AYLzja8ZjrGTqp_UEXEl3MRbhnSlrVbIirv4QW0ipTqUFlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/13491" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌹</strong></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/13490" target="_blank">📅 17:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=EpsraJuwgD76XbCCFbCALKKIyEukVo1QnjEjBOSrECOboWUGR-GCRuFDFLxSwzysKSzGeO9hY-7vgf1tfy5P-nemshfvpkH1ftLE1qiXPaYsjEAiis_nRWZrIUxC81jyvQnSdbYoFJz67P1bsHJpYi6YwKtpSRWfZdw3vhhCIQbFvAT6qwjvfRPzSu4sh4Cejzdl5nLDDXsuQ7Wa3MP43O36RxwBl4p_Gn3CsPPRiSZvwEApksjBJ71JYqqjNhxPST3lPuKh_dRVgPBWWmuSrrUBBozcJbp2PnZ2lD_lobLaTM0Yn7K_LiOfXPX_zkBWDyjJK_oUxZCia_9zahzkGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=EpsraJuwgD76XbCCFbCALKKIyEukVo1QnjEjBOSrECOboWUGR-GCRuFDFLxSwzysKSzGeO9hY-7vgf1tfy5P-nemshfvpkH1ftLE1qiXPaYsjEAiis_nRWZrIUxC81jyvQnSdbYoFJz67P1bsHJpYi6YwKtpSRWfZdw3vhhCIQbFvAT6qwjvfRPzSu4sh4Cejzdl5nLDDXsuQ7Wa3MP43O36RxwBl4p_Gn3CsPPRiSZvwEApksjBJ71JYqqjNhxPST3lPuKh_dRVgPBWWmuSrrUBBozcJbp2PnZ2lD_lobLaTM0Yn7K_LiOfXPX_zkBWDyjJK_oUxZCia_9zahzkGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت شهبازی از کار
😂
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/13489" target="_blank">📅 17:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad Jalilzadeh</strong></div>
<div class="tg-text">اقا ری اکشن کوچکترین تمرین هست برای پذیرش دموکراسی
وقتی یه عده همه ش دنبال کم و زیاد کردن ری اکشن هستن و دنبال اینن که کی چه ری اکشنی زده در آینده ی ایران چطور میخوایم همدیگه رو تحمل بکنیم و باهمدیگه حرف بزنیم؟
همه ری اکشنا باید باز باشه و کاملا مخفی</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/13488" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/13487" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چند گزارش ساعت ۱۵:۵۴ دقیقه محدوده شمال شرق تهران همچنین نیاوران صدا پدافند شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13486" target="_blank">📅 16:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی را در برابر چشم جهانیان قرار دهیم.
@withyashar
وی به این موضوع که ورود پرچم ما به ورزشگاه ممنوع است و چه راهکاری باید داشته باشیم اشاره نکرد.</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/13485" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5xioZNB_GlOtNFgUviNMHek_sFKFA6xmAvurCSLmSUURjeXrJ4cYRs_oUznUoZgZl562kppba5RgTfIK-3kWny94upOQtSy9dtGCV4p_q84NrHO3jfPaDI8XFKcizVQyDORMzzExgBSrCY2M6a5YRR0KQRC70mVzssDnC8W9_CerhOwYugazIo6NnHOilrVqkwdwiakktGmMc-jrqXrOQed1n4CI7grYHpWWj8G4DgJTWjpHRzvtbmuUhuM5xSeW5x0mEmjzQV_8J2-nFsPYZNZQaQEA59lF99lTFzMwNK4CSldX8Fw_GvA4jizlP-qJO1WER1sqgeabLDbPKXW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : سازمان تروریستی حزب‌الله گلوله‌های خمپاره‌ای شلیک کرده که به یک موقعیت نیروهای سازمان ملل اصابت کرده و در نتیجه یک نفر از کارکنان سازمان ملل در جنوب لبنان کشته شده است
شلیک‌های حزب‌الله نیروهای بین‌المللی را در معرض خطر قرار می‌دهد و به کارکنان سازمان ملل که در منطقه فعالیت می‌کنند آسیب می‌زند
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/13484" target="_blank">📅 16:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نعیم قاسم، رهبر حزب الله: نتیجه مذاکرات دولت لبنان با اسرائیل شرم آور و پوچ است و اونو بطور کامل مردود اعلام میکنم.
تا زمانی که تجاوز ادامه داره به هر جایی که تصمیم بگیریم و بتونیم حمله می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/13483" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: در وسط مذاکرات پایانی برای پایان دادن به جنگ هستیم
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/13482" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a60bns9xKNsV_WU1QQWW0c2HJ4gHMrxVh0E2zyCFFBDXH4x0AM_jdveaM9NROnNeS0lspBrgYrUfcPqVSN-Sg_KKdXbSafhv8DFpoAHBCSxSKzAMw26gTwCur-DuYc53jmyX2Miu8S68oiFbdEjyGkxgVHXZ6WxnnlHuQ2E_DLOALPR6XD0ghCZGZIeuM0amxlA_mNdQ6K_IMUVUnBqHDQaYeKmlhng6UsESK4i7r7u4CgqBQKxSxXAYLSVzfQdZiraI5457IBCmaVWQoMdjap9H9-xVpf6xyh6nDJJOmTZiF7B5siHrLls5R521xznfRCqZ-42AwUimQ7c4JZhskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکسی از نشان‌هایی با نماد جمجمه به سبک ترامپ منتشر کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13481" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSvi57SBrv-d2APMDOij5wtMma7VXYtlhWzFotYKyAHh-HLshhQX9g3irSOCxkvq6SsPEU0c9YllZsdJfNUI7Y7EwjyheozXl5KOFvECjOEYpJHtrtv3yVR8gXOGkyhA4tC5d6EiZjZOUsHEpILRB6uMvLu-D0j5qVcie18PUAvgkWRLEZsXr3UCIaEieZ-nEAYLhibFX6RMUR_2TdsfNaWvI1hnkwVMclYiGEWbXjfxZYYSJrqHdUGYA9vECUL7v6F-XT92fUqH_q3JaSUw-R_8jJdIi1713ZfAdFta8JTHYduxwxZJB6lhwcgzUQLLgQ2zVkq6BzVysx2lHGcbvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیروز، در یک رأی‌گیری بی‌اهمیت، مجلس نمایندگان با رأی ۴ جمهوری‌خواه بد و همه دموکرات‌ها، تلاش کرد اختیارات جنگی من را محدود کند؛ درست در میانه آخرین مذاکرات من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آن‌ها می‌دانند وضعیت مذاکرات در چه مرحله‌ای است. دموکرات‌ها با چیزی به نام «سندروم جنون ترامپ» هدایت می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یک پیروزی دیگر از میان پیروزی‌های بسیارم به دست بیاورم. آن چهار جمهوری‌خواه، ماجرای دیگری دارند آن‌ها اهل خودنمایی هستند! باید از کار خود شرمنده باشند.
MAGA!!!
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/13480" target="_blank">📅 14:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد. @withyashar
😟</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/13479" target="_blank">📅 14:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13478" target="_blank">📅 14:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=K2Cah7hF-thfU1--dyqz8X3_znMpaWKv0EpgYDPsJc1P6W8oN9nlPAvPpahXTmgolNN2PKM2dHshx3gXe6Hlw2mO7KyvoDhVNP6z0P7JVGOdduOyiLdczlbIv-84UHsUve4GRfQ0xCzAZRhPI_JmHO-KGWDSSgA1oEzWJHm1UhFB_Ty-N9huMwIEfrhw3KI3N5gwL1KRHhScUbawqjkqlbFDKfWH_qKhKNbaR8OsMFyIG9NuG3EpZlYwRKwOPAj1Mmr4q3C7GMEzYb5TzVzkFM4il6lEIwa2Kx-q90NKiYIg02HFiAwnWUKfMcHncPITyK46smADD2CgSkm0WdPppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=K2Cah7hF-thfU1--dyqz8X3_znMpaWKv0EpgYDPsJc1P6W8oN9nlPAvPpahXTmgolNN2PKM2dHshx3gXe6Hlw2mO7KyvoDhVNP6z0P7JVGOdduOyiLdczlbIv-84UHsUve4GRfQ0xCzAZRhPI_JmHO-KGWDSSgA1oEzWJHm1UhFB_Ty-N9huMwIEfrhw3KI3N5gwL1KRHhScUbawqjkqlbFDKfWH_qKhKNbaR8OsMFyIG9NuG3EpZlYwRKwOPAj1Mmr4q3C7GMEzYb5TzVzkFM4il6lEIwa2Kx-q90NKiYIg02HFiAwnWUKfMcHncPITyK46smADD2CgSkm0WdPppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf4ERZuVaBlX5L_q2itKFSKkkWRo7AY01_XTs4XP4z7W2K-ckHync098xtZDhxYH14tuI5q6GSilkks21-Xi-gAU7BAMqOQE-r8K3lsJxD8YsUq54bvjk7VlxKpAjQRucctk55n3pjr_uS1I8RLkGxgjLPWVk5chrN78sCxw6lORkwNXNNSmJ9yKbxy2QkHh2CmbThHt93ls5hHM6781pLzLdFRHTsSm-gLSxKt5jdJLXy-uJgRpQM3l-JVAtSd3kMcqpLxlcHuDyR6_HklObSYIxNhVMa4LwfERzkXXC5mdt2nkhLgdlQmoo_zBHSD040iTBlfnO7rUPj9Dp8QJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5FwA6jEss-M66xF3omgB1-NK3KjcRIgYFLArFalGKvlHhGEsGPhALcc1Txwd0ocu840hc5Ul551ZO0biWUivJrAoW_njudttIYNV9JKk4WBb_Mqj1nhNsUw0lASEJ8v89H38av9VLVYfNUUDwP1kVXqZ471QLDmnT3Yz4vFlEQZ1_4yeRTJUrnwJIFrm6CWpwgKETpsmXiauLm5b2w5Ag4OzdqqIG_uBXAqizbcEipjXdNWWwHjmV9iK_XcpaZzqY7G3KpcfRc18Ep7Gj5r3-MjftzCTazRylsDBY1_RLCSftbkhKQoAvBbgxB2mIbk6lFImRKzCWMUJZpJCdRwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ED8reIjcJ93tR0cak1Sx-EndFyWkjgc-j9wiSMvX9MHvnhF7cfKMJKRiYEh-JWkQS80Rtt8HWz_FjtCRrXySpNUbVfz7bzkPhXF-4_dn8u2fVKaH3Iq4hXq-How3HNzVs6HbfdPno-BrVg5ax0kulE2PMj3JcUuY6n2GHgCGuSGB_fE02I7B51YeQ8o-qLYbqRQV9I7cmtuxb7KgiL7EGrTd3C97qztzyO61LjV399IsFM2pz5aau0oiv5u5vIiniWdI1Bx7d9ZcxVHIZdxEPaleL177lnP0n8V0IMw0T8w7UQieFHkGaHn6YnpzM4s-WB0SP6FcJImhVsZcQaXwPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ED8reIjcJ93tR0cak1Sx-EndFyWkjgc-j9wiSMvX9MHvnhF7cfKMJKRiYEh-JWkQS80Rtt8HWz_FjtCRrXySpNUbVfz7bzkPhXF-4_dn8u2fVKaH3Iq4hXq-How3HNzVs6HbfdPno-BrVg5ax0kulE2PMj3JcUuY6n2GHgCGuSGB_fE02I7B51YeQ8o-qLYbqRQV9I7cmtuxb7KgiL7EGrTd3C97qztzyO61LjV399IsFM2pz5aau0oiv5u5vIiniWdI1Bx7d9ZcxVHIZdxEPaleL177lnP0n8V0IMw0T8w7UQieFHkGaHn6YnpzM4s-WB0SP6FcJImhVsZcQaXwPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دو منبع مطلع در مذاکرات به i24NEWS عبری:
مذاکرات بین آمریکا و ایران به دلیل اصرار ایرانی‌ها بر آزادسازی پول‌ها، «پول نقد»، از میلیاردهایی که مسدود شده‌اند، حتی در مرحله اول، متوقف شده است .
در روزهای اخیر، میانجی‌ها تلاش کرده‌اند در این موضوع مصالحه کنند اما ایرانی‌ها بر دریافت پول در همان مرحله اول، در چارچوب توافق کلی، قبل از انجام هر اقدام واقعی در میدان، اصرار دارند.
مقامات ارشد آمریکایی تأکید می‌کنند: در ابتدا پولی آزاد نخواهیم کرد مگر اینکه ایران گام مهمی در مسئله هسته‌ای و هرمز بردارد و همچنین توافق کلی بسیار معنادارتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/13456" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBwgB5SxRgA4QZo2Q94cli-yI0SoXB87K0S3N42QNXv_wNoY9BzgQ_okAfZ0rZhTaxE790QzeqhR2K55fTduehMTFa9bPRZX4ypCMNryXFTmcHIuQ5G6AtwEvOoQDcoMMBew9wLcGlZmIBr92WQX9PbB1Igg4UKVt4IuQNVKXrBU2_WXfAkELJeFIOQ8y9fkvmhdy4DAWty_mxsjHuYhNvuUTIW0VBT1zB6XCxY_mgeHEyZ-eCIVK9M66oq51SYARdLft1DZiFr1HuPzJmBK_NIrsH1I1BjaDre1j5yKgyE4MWSaay8bsgCFnXZZhSzK2G4AV_6RLorVPY9dHc5dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکا
جمشید قومی
، شهروند دوتابعیتی ایران و آمریکا و مدیرعامل شرکت «فرار پرداز رایانه» در تهران را به نقض تحریم‌ها متهم کرده‌اند. طبق ادعای دادستانی، او طی بیش از یک دهه تجهیزات شبکه، امنیتی و رمزنگاری ساخت آمریکا را از طریق واسطه‌هایی در دبی به ایران، از جمله سازمان انرژی اتمی و وزارت دفاع، منتقل کرده است. همچنین متهم است حدود ۱۵ میلیون دلار درآمد حاصل از این فعالیت‌ها را به آمریکا منتقل کرده و با آن یک عمارت ۳۵ میلیون دلاری در کالیفرنیا ساخته است. در صورت محکومیت، با حداکثر ۲۰ سال زندان فدرال روبه‌رو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13455" target="_blank">📅 00:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/13454" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ:
ما در واقع برای اولین بار با حزب‌الله صحبت کردیم. نمی‌دانستیم آن‌ها صحبت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13453" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/13452" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان خواهش میکنم دایرکت جای کامنت دادن به مطالب نیست
😟
خدایا به چه زبونی بگم ؟ بفرستید برای دوستون و باهاش‌چت کنید ، به بچه آدمیزاد چند بار میگن</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13451" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرنگار
: شما هفته قبل گفتید آمریکا می‌ره داخل و مواد هسته‌ای دفن‌شده رو در هماهنگی با ایران بیرون می‌کشه. آیا ایران واقعاً با این موافقت کرده؟
ترامپ
: خب، بستگی داره داری درباره کدوم روز حرف می‌زنی. این چیزها خیلی هم بزرگ‌نمایی شده. من خودم هم اون رو یه‌جورایی بزرگ‌تر از واقعیت نشون دادم.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13450" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=k8LL0hlV0MUlep0tn-uOUIVZj6nqAwjMt3xDODXZ4KJ6pLwKdCo5DrdtTP1hi7U7dL2Z5MjGwl8j67ruDFRdSQm01MXjTEqoikPZs73bQuJqXT13nQdTFpacGygivmabXJTFecbXrbAioy9imamXPM_hDcbSrGVGa534MAyO4_dMXfHxbWQEdKNjZ_EtiD16Z9dpK1sJuUXI0XLEt1x-EiYlt4Qjr8AWNdcVLxAczuqeQ-UHsO7jR1KdFdrKe36CMFyttpkaMO1VBdbNGESYpLe64VYaAlLQrhqWKHmlDX4umdZQmEGENQ86Gi9cmmALj_TCL3f9Rp5z0bo8gZw_aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=k8LL0hlV0MUlep0tn-uOUIVZj6nqAwjMt3xDODXZ4KJ6pLwKdCo5DrdtTP1hi7U7dL2Z5MjGwl8j67ruDFRdSQm01MXjTEqoikPZs73bQuJqXT13nQdTFpacGygivmabXJTFecbXrbAioy9imamXPM_hDcbSrGVGa534MAyO4_dMXfHxbWQEdKNjZ_EtiD16Z9dpK1sJuUXI0XLEt1x-EiYlt4Qjr8AWNdcVLxAczuqeQ-UHsO7jR1KdFdrKe36CMFyttpkaMO1VBdbNGESYpLe64VYaAlLQrhqWKHmlDX4umdZQmEGENQ86Gi9cmmALj_TCL3f9Rp5z0bo8gZw_aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=lIt1VnXB0FqW3AL9UpK8uZIq3KkZhUYBeGNBI-iaV4P72n3NWVs5kuWkox0WxkJLtWM8zEXQA5-0DwkyvloYVjoMQgu-Euc5iRlgn4-A5RnoR7BYoi4smBARuhyvNLaCaBWRRZdEvS0WMAZEv2vVugpXbakZmFONufFYjFX0EyDe_EsRJv9bthv52EeY2eFC45L45xyE0dgBoeZ2TPbUW3pMH2IB8VudlDKTzZBmBlmc6uCopFCwggIOveE3x4BIIkW99GbglXA3Rag7es3UYyU6Inu7g2p0H0PxAOgJbIp8Vxg6ZIlL9FxzUtlw_Tg1_3xL7zLO6qoEqXXTOMFbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=lIt1VnXB0FqW3AL9UpK8uZIq3KkZhUYBeGNBI-iaV4P72n3NWVs5kuWkox0WxkJLtWM8zEXQA5-0DwkyvloYVjoMQgu-Euc5iRlgn4-A5RnoR7BYoi4smBARuhyvNLaCaBWRRZdEvS0WMAZEv2vVugpXbakZmFONufFYjFX0EyDe_EsRJv9bthv52EeY2eFC45L45xyE0dgBoeZ2TPbUW3pMH2IB8VudlDKTzZBmBlmc6uCopFCwggIOveE3x4BIIkW99GbglXA3Rag7es3UYyU6Inu7g2p0H0PxAOgJbIp8Vxg6ZIlL9FxzUtlw_Tg1_3xL7zLO6qoEqXXTOMFbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ : مذاکرات عالی پیش میره
می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را نابود کنیم اما ترجیح می‌دهم این کار را نکنم
هر اتفاقی ممکن است برای ایران بیفتد، و رهبری ایران سه بار تغییر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13446" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش انفجار‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13445" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:دیشب و پریشب به ایران حمله کردیم و ضربه سختی به آنها زدیم
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13444" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM_8tFkGUdNXtgeAs3f3P0o85JRGLTH4g9gZ1majmh2-zuCA4K1S08beD1PAzktoVJRCRrkHL423tV7D2eXMYt5I4rCR5aTfnCG18EP8FpS3kHXwrubPscNf-QKLJ5coeQBO1OwCX22D2RnkVtqvQOBgvik2J_zyixLhut1Ai6lwXVCe_duFf0MoPtDrmnCcjRJ8HX2_mP9IZfe6mjFqgv0cA5E9hNGUNGiRCAmSCPlUXthNRu6QrgKqW7XGlRJBY6XlJ4hlfpKrWmJzE6pO_eFreYifAkcNKtRqYLcYlQ98q-G6Z8kwg60uc7feXVuM1_WfRMNFrklfeTnMgJG-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان به زودی به پایان خواهد رسید. به زودی اعلامیه‌ای از سوی ایالات متحده منتشر میشه.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13443" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دفتر بازرس کل وزارت دفاع آمریکا در حال آغاز یک بررسی (بازبینی و تحقیق رسمی) درباره «عملیات خشم حماسی» (Operation Epic Fury) است؛ کارزار نظامی آمریکا علیه ایران که با هدف برچیدن تهدید هسته‌ای تهران انجام شد.
@withyashar
این آغاز یک بررسی یا بازرسی رسمی است، نه لزوماً افشای تخلف یا شکست.
Office of Inspector General (OIG)
نهاد بازرسی داخلی وزارت دفاع آمریکاست و معمولاً پس از عملیات‌های بزرگ نظامی، نحوه برنامه‌ریزی، اجرای عملیات، هزینه‌ها، تلفات، رعایت قوانین و عملکرد فرماندهان را بررسی می‌کند</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13442" target="_blank">📅 23:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پدافند شهریار فعال شد
🚨
@withyashar
اینو دیگه دوستم اونجاست و وارده</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13441" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoJ_FZWrsL2adZitsnfVMwMeuzSfiWdOpdUqhP0T_HI4nPi1RsdCotY4xCWqxgOOuwl38w9S3NleFRaOg8bQDWFDFBTh8bE82Ouzixo63gLitwSPuaLIsdZXoqay9CqtBya6AAL2TfLdyE3z6MGRpzQNoIGvQfJSpEAJqgv1E8lseJRqRCEvpCwVMCrfQLQk0tKGF9Ve9QC9SpZP6uprd0aJiLWsJOlZqtXD3Efrpw0dQLng33fF4QtAb5JsRxIdfL6gecYHskpPK43b6FopflulxbIg3gPJoBhKSYrgMftqKZPk2LMPGfPVDL42ZBlDE3qzQXdnS7yVUbixgP6fng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بلافاصله پس از یکی از سرگرم‌کننده‌ترین شب‌های تاریخ آمریکا، یعنی مسابقات قهرمانی جهان UFC در چمن جنوبی کاخ سفید، به اجلاس گروه ۷ در فرانسه خواهم رفت. سوابق نشان می‌دهد که اگرچه در طول تاریخ طولانی و پرماجرای کاخ سفید، مبارزاتی در سطح بسیار پایین‌تر در این کاخ برگزار شده است، اما هیچ رویدادی حتی نزدیک به این، یعنی بزرگترین مبارزان جهان، قهرمانان جهان، برای مجلس عوام در نظر گرفته نشده است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13440" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13439" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی ساعتی پیش یک ناو جنگی آمریکا را در دریای عمان هدف قرار دادیم @withyashar
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13438" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز: رسانه‌های ایران گزارش دادند که تهران به یک کشتی نظامی آمریکایی که ادعا می‌شود حامل «مرکز فرماندهی و کنترل» بوده، هنگام نزدیک شدن به آب‌های سرزمینی ایران در خلیج عمان حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13436" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=flnUAMUVo0s7tkfmmkMUT_dQGWXnbvEXgVTdoi0kbDO60U0UDRL1eoxYq3SiRNLiXjS0zmMaXgyx5IvjoVCiAj_nB2Jv2gdsQBkm5ijArm5F8DgKTuLzCiyMnID2NKFVpcD8Y_5gy_mnZhaiQKT_LhN4a3Z7AvmaUA-ploAMV-us1_XZqfiAtPqaWm-B8tObDO-JdfIT6YuLqcK0hTqnIG-cSEO5UTXqfEe5awXe408zNwZMLmbjOtRiaJpkB3wy3TI7KC5zc8mGUdMHB2rjHlf9LYXSQNOvyr1OSxvwY7r_91eWkXN_gDNbZ1F9BW00Ta8p00s12SwH0gPqu75zqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=flnUAMUVo0s7tkfmmkMUT_dQGWXnbvEXgVTdoi0kbDO60U0UDRL1eoxYq3SiRNLiXjS0zmMaXgyx5IvjoVCiAj_nB2Jv2gdsQBkm5ijArm5F8DgKTuLzCiyMnID2NKFVpcD8Y_5gy_mnZhaiQKT_LhN4a3Z7AvmaUA-ploAMV-us1_XZqfiAtPqaWm-B8tObDO-JdfIT6YuLqcK0hTqnIG-cSEO5UTXqfEe5awXe408zNwZMLmbjOtRiaJpkB3wy3TI7KC5zc8mGUdMHB2rjHlf9LYXSQNOvyr1OSxvwY7r_91eWkXN_gDNbZ1F9BW00Ta8p00s12SwH0gPqu75zqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی امروز ویدیویی منتشر کرد که نشان می‌دهد ساعاتی پیش موشک‌های ضد کشتی از کنار ساحل به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13435" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الجزیره: ستاد فرماندهی مرکزی ایالات متحده ادعاهای ایران مبنی بر اینکه خسارت به ترمینال مسافربری فرودگاه کویت ناشی از موشک رهگیر آمریکایی بوده، را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13434" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad▪️</strong></div>
<div class="tg-text">سمت منیریه پدافند که داره میزنه
یه صدا انفجار ام اومد ۵دقیقه پیش</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13433" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پدافند تهران فرودگاه مهرآباد فعال شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/13432" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤬</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13431" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند  @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13430" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پدافند پرند فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13429" target="_blank">📅 22:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش هایی از پدافند غرب تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13428" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13427" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
بچه جنگ شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13426" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuMRDRpzlQq6OG3nwq3KlvpcQ02qIW9VJ15YREHByDpEOaFAiR2wHNQ_2Mj58buHPj5IVRxI5U8G1cAKC9tuC15O3PsYa0MIuf6eUXwo6SXCb-ErTo9Fct4_Ut5hcbXr1KOpEirj-2864l81HvSPT0CMOUpJe9PutWZxzpQ9ie_qmgrE4tQOGEJzt58gvrEPHkhogQzte1gaJqrQo4j0NlkfpX9cyyENo1OGsj5zPZ7D9S5lAryznu6DbL-D6OMOKulZaahT9zlf-_ZysYDULbudUXmG4ElM_A6swh-6n6QwHmTe9773ZJH0sw1bcRvs8HPwmtNUNB2plVVkI8AAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های داخلی آخرین عکسی که از حاکمان سلسله مموشیان در ایران کنار هم بودند را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13425" target="_blank">📅 22:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اتاق جنگ با شما : پدافند شیراز ساعت ۲۲:۲۷ دقیقه فعال شد!
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13424" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تسنیم به نقل از عراقی: ایران آمادگی کامل برای ادامه جنگ برای مدت بسیار طولانی را دارد و ما از توانایی‌های نظامی لازم برخورداریم.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13423" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی: در حال حاضر هیچ روشی در مذاکره وجود ندارد، اما پیام هایی با آمریکایی ها رد و بدل می شود
دو روز پیش پیامی به آمریکایی ها مبنی بر لزوم توقف تجاوزات اسرائیل به بیروت فرستادیم
تماس ما با آمریکایی ها قطع نشد اما پیشرفتی در مذاکرات حاصل نشد.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13422" target="_blank">📅 22:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpb3od14Mjhfp_C6khj4lD-JQX7_WZxtZmgcQZjNxW8e4z-iLxBCNrVmldSfVDAwJ_h-DCpOPV9QMrbo_56SHiSH0dmtcNdSGovKdQ0BGXtYnSCLPMiW68huKqDZUSqCxtIDLDLbGsLB7iTnBHVOcqw5uOrUnOFUJ8k_X2L05dpc9e3zI04ylc6LmzpjACDCyRDuQt_yC4-B_dEIY4fEZ0w31EdP1lTcNgKuMqW1KpSYJYonxVhgw05kbmz-ZYYK3QhvN5BeZJqSW45QFNnLf0qoMf4ESjHdNS-gv5SfPruXdT9c106HBTP8T-eGG5fCJ8KwFwHLVeDiHR0abqlh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیل زاده با ارزش نزدیک به ۱۰۰ هزار یورو؛ کم ارزش ترین بازیکن تیم ملی فوتبال ایران و یکی از کم ارزش ترین بازیکنان کل رقابت های جام جهانی فوتبال ۲۰۲۶ خواهد بود.
خلیل زاده همچنین با ۳۷ سال سن پیرترین بازیکن ایران و جز ۱۵ بازیکن پیر کل رقابت های جام جهانی خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13421" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از اعضای تیم مذاکره‌کننده ایران به خبرگزاری فارس: ما هنوز پاسخ خود به پیش‌نویس تفاهم‌نامه را به ایالات متحده ارسال نکرده‌ایم. ما وارد هیچ توافقی که لبنان را نادیده بگیرد، نخواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13420" target="_blank">📅 21:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13419" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی ۳پا : تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است
بررسی و تحقیقات ما در مورد اصابت ترمینال مسافربری کویت نشان می‌دهد، نیروی هوافضای سپاه هیچ شلیکی به سوی این هدف نداشته است و تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13418" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMg13FHTLf_e7Dm0c8H_Mi0IkbOQ0T4xYCXyJkVtTZYX2FiPCopkKcNADImu6bYjd3PquyUDLoz8F4GDUmqQDvnAuOEtchgTSvbr4nQ7y3piwrbaqqaGu3Y9sDI5eklzH7iGHYNqj59OP4p9nQlg5Y2uIUBW6yabf-53gjQP7-UFxRCkLV_R0nWphq5mgmCjXflbBCbNwT0m6booh2aIQHdKp6uCGxwF-uPd6LyFDSG1gjc2m-Z7CFvZhvJmOy4Rc35ZaolxKrigp4z2eb-nhCFiJ0GNb7FrU5J12ll3l9Hz5thC-EAJgnxt2BOdIlF3N1sCC7jNyvEJhrMw14QH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :
شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.
برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13417" target="_blank">📅 21:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای بود
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13416" target="_blank">📅 21:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو:
اسرائیل آماده است. نیروهای آمریکا آماده‌اند.
ایران با آتش بازی می‌کند.
@withyashar
شمام آماده اید ؟
😁</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13415" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13414" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یعنی چی ؟  منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13413" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">یعنی چی ؟
منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13412" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13411" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادعای روبیو، وزیر خارجه آمریکا:
ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13410" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تکذیب شد
😃
🤣
خاک دوباره پس زد</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13409" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13408" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13407" target="_blank">📅 20:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">sample : yourname.warroom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13406" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه ایده جالب دارم ویس میدم …</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13405" target="_blank">📅 20:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">https://www.instagram.com/reel/DZIVRzvuaUf/?comment_id=17892109731481781
به درخواست شما متن برای بانو نور هم کامنت شد</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13404" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدای مشکوک به انفجار از غرب‌ تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/13403" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
