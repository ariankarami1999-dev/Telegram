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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 208K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 21:27:15</div>
<hr>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyidfyl8IRbkqaAq1M9__Vaze3zlalljbwjKSwbppvPFGqddS6JjaZ1TY_wT7PNKBgb-Q4e7w2K66b1oXFfSLgQbrr6QfS43jg2zI4VQ9HCAxg8DgfHJF2o_Up9o145RpH1ma2lTF1OJs4GvBz7X_yLQf6PgoCiAHk1LEoHeK6zKfyJf67VLRZqDsYgWECdydR24lV3LZP2gUpU7ICU5h0fdl4xxGNUKAcZHLfSsxVdMRG5PILfWKDS0lSINB1sJp5mxiR8LuCClVDpp2IyEHwv15ssQO5srQ9BPvUPfloUicDo5_jWQDd6h2xmJVts5HMw1JbAaiCcUb7gE4GKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBe-n5-XJ7eEpm0cKUvwMvRDINe0BD0DiaVO7qXAVtU5JQPnjMF55kSoTeCVG9B40ZK4LngQK48YBQWpnLEsAUKkGYuyHye48OSgGANvIw9lgpROv11qeyhRGsPgTJLyOxcHl2sTkiPvFYEN3-cUoOrnoCq5TGnirMcRL5R0Aj-gy_w6HZpP3YHQGCJrNduyUIJja5tERIkAQMOZEXEm19z92boLeb01KtYkkMn7FU9lwfLD0vylaWHc0Ej6Y9OvQk9d8-4XXlu5rSZd2VYiMzPcdau-3CkPRVpNSz3rKESct80om2jiL3JoHznzBH6CXrRlkynmMyHkL5rFGoCUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtatJ_urYgV3jA8hrmHntL4B3BGxS4j3kxrrRZP2pcikItiOkE7JHvsLJUhoSq7miSz7FB-_4lmxJPz7GwTajk8sICAm0LX8NW0yqXD2vN0H0O22LwHolNw8xT8wb8lDyw1DVOmhgp5cXD-mTXYWGKC1F5gmDR9y7AQAK6KoUv_LV8sy5-2YJmvXlpouQJmWQXV9xxhIpFpVutdSo9C8W7hJ6ZBJtQ35lcp6tHDwttMqsPo6IN8F9MjeeXBumo6JEopmStVMPHGZmhXeKqyl7YSr57x7w-oeEPIEJ2AKKbVpfREM7LH17c38A0KtBu0JE8_NTGqWPHe9CRMJXU8iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4uks0s2zIVQQxXW699xzRqEv254JCxDX8v1oXz6EeHET-fdEUTVkQEF9MDnvBZVIZ2S5FkSv54CSz5wSXel_7u8X2FA3JAIasdfUfWUKXCiRqL5l1f5ZIVYklj1zmAz5PSgYNIN5O46175NnQOKZ_XchNnG5fZEuxD6ximpI3N6Qlm0fzuM_buZqSqwU82LPgPZtc0Zwur3T2OpuYpbqrTTDd9AMe5qBXsMLyGfw2b8LQBgwZuIoKAJvdIUZ5EhVfz860B5BMqbHrAmyCgrhmCxtnbbQtwcmRodEIv-8Wa8G91kDV29lvXTh-vHw7fKqIRlCbpDrcAagCUX9autA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhNQxvXJGp96qQSWVsHq_JCN2Sqi59dUcD787YkK9b0u9usp5v9RiRN7KCa8vQDHYdwfSirN5GBN0f-GAk9U8XMZVFa52hu0Z_XcsAgpBhfeYEoz0jcm0NpxOpfwvhMCVSqRLsyTfcUbySsCKffZp2PlWCNqT7ZnWV4955FubEBgG9-QdT3o2Uz8T3dCZ47U7p_mZ5zQ97j7kG7K-DVPMelDc5qrNuxkMjY0Zd-632wq_HRCoplE4-XdvaQZT4vq4ZuluDyEzW6oAx4ZCn5w3dEKTVEFXrAVtNbCujkVIVF6SI-Gzujww2YiF8lrHVsTvpKMb4-6EhWrakY8YkFVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P32dGYapydeF8T0wd63U16X9S5pQz-lzDzeDEJZq6dEefPDS9WMoLsqIrpUuS5y2VESmyPJcKQ1_9LtsJf0HE8mH_HRs2U6kEYVFLAqROU49jzXs9RCfujqedTr7F62EZMUdwp5d6R_YvC91TeAs1RAikaw8gCyh2KFn-Psn1E7hQMuRygYMII4HhfDE6t58yJ7eMeE8qXLZ8S_0DHunpvclrAweqj6PjMA4H1W8wnPGYgjNr7hwfi0ryZrcWtAZHNUPCQLvXvTD9dZaHTXZpYq2Y8gKIqCaIb1O6aH0VR_NgwLKR8MPTTfOMA6mz0XBP8dAyKjLvWVKxKgQFjBWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0B2YH9flLjdZ_146yiq3Wu0HWds5iZkNxFCgENccArUHKTbyr1wOgVE_MTG-tnIQVCL9GFn5w6L3cZaswBSu81l22MuU9V3-SSxbs15ts0xdgzwHWcslaXwf7VxL_7b7d8K5SKazPkrNBfwKysGY8ajtjylZ2pk1OZmeW1zu_x1F_Kd9-avtByPr4Dx2ggSuMGRgaxzI-Tj9QwFanJeq72DMcpx9ZbLj8iDKOxLt8jC5LDRKS4aAUnANF0LLI7Aqj5UH51v7h_kd6mP3TYPrP1GO_s3R3BCMPb3c4H2G0_OPeDwQyjmQjWfsy39PqWD9x-QEJd12p-d9bxDBDm5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6-d_7sjQtSjaJbjAwgK192HMan55eY65mziUAErcSMXzTxOQ0p_XsYKX3IQnKxO5bHYDgoULkXRuQlUd2tqoH5fdi8hW6uolGwSoQLe3o0NlfGA5bEexbFS7FdTohMkz_RWz8epEWEqWyyPqBiQaGK29xY5GlPhci3TqfntiKCHGIHQ0fwxH64T005do1Otu4Iggi9NspbPvMmKxtqOLNXh-W-ZEw4ZD-R9_ORAK2CulsE89W1_AH9gp8thH5_j4pUgfT0nMxwjxj4W2UTyI2npoq70SA8_uv9vBaqrlmNnvsY4MdHsO7c3HPH-7WW5co6aWp6mnDeNrtaewFwVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=c-VqMxYHk8bAx_XSiq5GPuLKk8E2VnINdxfWVAKLxXLNfg5BwEKEx4Pvx2s7ma_19qW4HIgsmaNXJ9GpiuFkPqmSyQYqDYaNy9rkoZy4Ysei1lBqNjWDDDw7c6x-S0xZil8pIlGXfA6hWzsopB8SFKX7nokEdEI8NX4I7wiXIAiNtFVWQ8TZLMy5exT6sglIYSUYzEAQzQ8A-l6lr_UtlH5OQO52NKX4eulVmNoJK_bU1DijD2AiLdR3sCyNz-8xB_0xDkXXKQkUgwo3UfjwDgYgsgoTdKZZ_S-ZMpJcCCmiIr-jfkH3T1wot6ntZcY0FLS7HWpS92I363XauRsP_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=c-VqMxYHk8bAx_XSiq5GPuLKk8E2VnINdxfWVAKLxXLNfg5BwEKEx4Pvx2s7ma_19qW4HIgsmaNXJ9GpiuFkPqmSyQYqDYaNy9rkoZy4Ysei1lBqNjWDDDw7c6x-S0xZil8pIlGXfA6hWzsopB8SFKX7nokEdEI8NX4I7wiXIAiNtFVWQ8TZLMy5exT6sglIYSUYzEAQzQ8A-l6lr_UtlH5OQO52NKX4eulVmNoJK_bU1DijD2AiLdR3sCyNz-8xB_0xDkXXKQkUgwo3UfjwDgYgsgoTdKZZ_S-ZMpJcCCmiIr-jfkH3T1wot6ntZcY0FLS7HWpS92I363XauRsP_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eak7R0FXUkNxsieiZlmub8hdxKF_A3KYB1vRwxeZkK3y46AdcXL3iB0ByRa5z-EeZ2ZN2GZpesVv9qbivqGdeoCZp6gtWimWF4R0BM-mDfk9kGdAAaEosKoRp6XxyWWHiqdyF_617gsfd6C3aiNojYWWTvWA4KgkQfxLiUXvxweUh7-fUFM6qezDrJ7q31sHR-bNn8VhhhT_zjuvvfwJ-Tcv7vvniolgsbZIrgkaohomG0UzFzY-ASXnP_WsJQ50aT8cdzobSt3q-TBlivSMVw1aYPoYQLLvcUZ6eFKAOd_xrA8DrVBYJ99NgzTb5eGFycJpucRE9dqmWu68hMHPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6T4xuzwHyquX2gmfs4tUJjFv9pQ0j59wrnpon7yybAdAL8bO9_YwfR4BPNVr1zObVntL4vI7jqwJkrWsI_RM4Oy7X3SXL47bsUsBjAhLHB5_kghJ-ZnALCCtdXcCxljbQ7wvmnJ9nrE3y7gls6zU9DW54qRiRV3-V6imkepMBXuDFjdHSAX6vVvTyCSvfuPXGrJomKyYgdN6RzMkylrrjX97uDgIjUZymar7c4S6DHvpyFZHX6MesUhu4ho9zyiO2_0eX8QAeHcK1OrKGrc_BRZJz0oglJTWCq9Xw6Eldom4-gHFourw6N2Twp9wYxg7K_Ce7IGTpp9OfFrYB7KOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=k8-YPDDvFaOoWCYMXWLEYD9SOfshbCz0Z9EjbB112U8wsgbpkzaLp6V1uTcHi0Cp3LmGeqxKM5Th3QWter3PL-AHYKQ11rW6eeG9y0Gk3WzMabdar332wGPazbEDeemr6Igw9X6VXu8es2npaU0D7Kuj-wybltgZoSG7VHtpbPYCHyi7Z_6iLI9NWOVNH_zgVlPwSh9QehptXwikYce7zyk2paY0_r33yHBa0pAaPFLAgWCHRUKhSlJRUkd-DuZXfs4iS3PI5tOGF7JkoytvDr0gaAg7XR2FCJeHTO05bN2cRzCWFNhqWeiB2wyKTxRb9qfTCnQ54UogzaXonHMVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=k8-YPDDvFaOoWCYMXWLEYD9SOfshbCz0Z9EjbB112U8wsgbpkzaLp6V1uTcHi0Cp3LmGeqxKM5Th3QWter3PL-AHYKQ11rW6eeG9y0Gk3WzMabdar332wGPazbEDeemr6Igw9X6VXu8es2npaU0D7Kuj-wybltgZoSG7VHtpbPYCHyi7Z_6iLI9NWOVNH_zgVlPwSh9QehptXwikYce7zyk2paY0_r33yHBa0pAaPFLAgWCHRUKhSlJRUkd-DuZXfs4iS3PI5tOGF7JkoytvDr0gaAg7XR2FCJeHTO05bN2cRzCWFNhqWeiB2wyKTxRb9qfTCnQ54UogzaXonHMVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCn-WWRBeE6Y7XJ8uhTH4HdLyaAMriKWoEYnXvw0NIIWiZ1yTUp59SJKERutOeFNPDVzh8UP4CH47pjr8AO53Z9yY2M0u00Ca6HxwfElW5kRPAPbg4uWd5Gq-zJ-fPC6_aoNBQMLXvzLS6A-wSwEoMMvAjCiYBj_MM7dhZ5epOs3yPvU41MMdf15H4oKKT-M5zR2iN_gHD4c232bHRTzfPgYIepBzlqj3rvSbudPcfxKsF4yVxDlUyKJBoJu-3EleBtukYS1FHy39oPhxy3e-4dbDzs2EYdECYnWFtROL1BTx1VsMkNj-dV1OBe_JlkAk3ey7M9Zya4mexAsHNAxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=XOZNgOZFrSAvvoW94rN_YhitpzKCfuabieV5PY08mXiBgKIPE7Sonr1LJfTQfTbzowaOy14tnJwSKkqbtDLMlratbZr5RsGBIlVQp4hEwqm2DepvYbtp8nQ-ZA5MW2l3SVZqr2278NSzRv8CySn9ckK_kniJzNWNlCXD8KMHJo0Z3cAVBlsaR6ICfG23G-2POdJNBxC5AQjk-llxouR-NnvBsQnZfdZ5BcXGt-Tj6R0zlKmmzbI3oS77YcpGHFOptYrZJIHatuu9oZqwotHTw61Xich5MTCuJ0mDKm0GulMRxmeevOYJXRd-wbDD9dDwDE_EGQplNZSVdozp2vx0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=XOZNgOZFrSAvvoW94rN_YhitpzKCfuabieV5PY08mXiBgKIPE7Sonr1LJfTQfTbzowaOy14tnJwSKkqbtDLMlratbZr5RsGBIlVQp4hEwqm2DepvYbtp8nQ-ZA5MW2l3SVZqr2278NSzRv8CySn9ckK_kniJzNWNlCXD8KMHJo0Z3cAVBlsaR6ICfG23G-2POdJNBxC5AQjk-llxouR-NnvBsQnZfdZ5BcXGt-Tj6R0zlKmmzbI3oS77YcpGHFOptYrZJIHatuu9oZqwotHTw61Xich5MTCuJ0mDKm0GulMRxmeevOYJXRd-wbDD9dDwDE_EGQplNZSVdozp2vx0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=pl-iC-PItwC4oIIzas0Ajjv7Jlioaz3j9JJDIBPgNJA-gSSm8mM8wPSpm4Dhrxcz3KAvj7JmbniQ2OMqXPKjZje1uOxtzklrIbEZvLEDtD-Gjnk2wFn1BbjlMLvfaBs7upuIwK1fmIsxpJcLXv8AZecQXOUa9Iiy-vsgarXMc-pK0W677cnXE5KrKAGJSjcHu1xYbMKklIrQuHgyP_yb8NCOfQjhrlJR7Op_u0t9XiUIlO2hoGKeOiXv7mXCOoExdylRByXpQSHKatJ9NrckHtJ6gE61Ss8Pjew7t7lZpXf2vV3hKMKjAZ7pkvP7cBjJGkUgCprRgk8yYH4a41Expw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=pl-iC-PItwC4oIIzas0Ajjv7Jlioaz3j9JJDIBPgNJA-gSSm8mM8wPSpm4Dhrxcz3KAvj7JmbniQ2OMqXPKjZje1uOxtzklrIbEZvLEDtD-Gjnk2wFn1BbjlMLvfaBs7upuIwK1fmIsxpJcLXv8AZecQXOUa9Iiy-vsgarXMc-pK0W677cnXE5KrKAGJSjcHu1xYbMKklIrQuHgyP_yb8NCOfQjhrlJR7Op_u0t9XiUIlO2hoGKeOiXv7mXCOoExdylRByXpQSHKatJ9NrckHtJ6gE61Ss8Pjew7t7lZpXf2vV3hKMKjAZ7pkvP7cBjJGkUgCprRgk8yYH4a41Expw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=uv5iWYkStHwjOYuu7H9LO-wpf14oE62VboJwWYVFFdQpG9tm1LMZpjkBqfnyft0Rubz-uzl9wTgrqo9b2ITt1vdyiiHle_6KcG9XTQN5cHmU7HwcNj06LpDpCCG34zjL1ynmXvZ-bCUFplM7vxJ_3VRKcbbkBRFj0dShiqGcLTQCelixEMa2x9OncWioN4RRZsG_G22gnrhynpVOqvLsKh8vRPgrgSQjS4kOpXifdAK7uSLHk6PHTL_IfQv338Q0rTZnGEQbgMTmrJSPhovIik2LgesJ7kD3yVjCnSbsX9HBqmm7kbI8qZR4Fx_SS6UeHGwQ8P27iw4czDkqE-GksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=uv5iWYkStHwjOYuu7H9LO-wpf14oE62VboJwWYVFFdQpG9tm1LMZpjkBqfnyft0Rubz-uzl9wTgrqo9b2ITt1vdyiiHle_6KcG9XTQN5cHmU7HwcNj06LpDpCCG34zjL1ynmXvZ-bCUFplM7vxJ_3VRKcbbkBRFj0dShiqGcLTQCelixEMa2x9OncWioN4RRZsG_G22gnrhynpVOqvLsKh8vRPgrgSQjS4kOpXifdAK7uSLHk6PHTL_IfQv338Q0rTZnGEQbgMTmrJSPhovIik2LgesJ7kD3yVjCnSbsX9HBqmm7kbI8qZR4Fx_SS6UeHGwQ8P27iw4czDkqE-GksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=vjnL6rQSmmKXZWF0mm4phur1Y5DcF_Jr1hhXVV-anSFm3nRF9EOkYEERCmGJA5JzLk4m-WtjWJO_IAhrltex9akHkqQh8bqQs45EAkmYHWupHy4lCbhe1OUOFqppjl_IM2POHaaa_JdcE4_dm50bTuTr3mXYBjkf6gIKzeNZHpUpsx1BncX1kmw2vxeS08S74LuclmoR9WhtYi7Jz6F5uciqp7TNhNWtwMNYktk697jITRfhI57j0x7JOzucAzhXEXt7YrOwqwZw9QbWowJv-ckW0WIedRgl-bv7svOnWllL5djTPnW9mCw7YLJReWIZeIGC17-GPpCQemkjcJV5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=vjnL6rQSmmKXZWF0mm4phur1Y5DcF_Jr1hhXVV-anSFm3nRF9EOkYEERCmGJA5JzLk4m-WtjWJO_IAhrltex9akHkqQh8bqQs45EAkmYHWupHy4lCbhe1OUOFqppjl_IM2POHaaa_JdcE4_dm50bTuTr3mXYBjkf6gIKzeNZHpUpsx1BncX1kmw2vxeS08S74LuclmoR9WhtYi7Jz6F5uciqp7TNhNWtwMNYktk697jITRfhI57j0x7JOzucAzhXEXt7YrOwqwZw9QbWowJv-ckW0WIedRgl-bv7svOnWllL5djTPnW9mCw7YLJReWIZeIGC17-GPpCQemkjcJV5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=QcBfHvx8gv2oErGk24iv1hYpVH69PJ39k7KREIwahiUZhZgJfAYIPDNuFaCblfH69HtaOdpfXI-UnlKsWv29q4UJUPVmMfMOm4o7Mfp3cGfBzJI5rWrs9qYKl598rrH2OLGx5Os0_0gY9Z4cMpVMo1EFIYWXbnWPZgVyPcqzody0OQmA3oKreqqjvJgT_VFUjkJHj_TQfgrSU8-oOwfgWgoKM8W1_fp77XV4py9XTQnWhqECjawF3k1P-VuZN8sQy25XtlWeWZ3Ko4fWAIPFG2zL2Xec5HwTKQQp30XtYJOdJpfkNWaJvHYgwICp7BGssAQQLatjmCDWw-TzgIPwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=QcBfHvx8gv2oErGk24iv1hYpVH69PJ39k7KREIwahiUZhZgJfAYIPDNuFaCblfH69HtaOdpfXI-UnlKsWv29q4UJUPVmMfMOm4o7Mfp3cGfBzJI5rWrs9qYKl598rrH2OLGx5Os0_0gY9Z4cMpVMo1EFIYWXbnWPZgVyPcqzody0OQmA3oKreqqjvJgT_VFUjkJHj_TQfgrSU8-oOwfgWgoKM8W1_fp77XV4py9XTQnWhqECjawF3k1P-VuZN8sQy25XtlWeWZ3Ko4fWAIPFG2zL2Xec5HwTKQQp30XtYJOdJpfkNWaJvHYgwICp7BGssAQQLatjmCDWw-TzgIPwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=W--Cbo77Wn6lr1GllAofellvHyaEGzANqtdYiXtljcKC5i_Rg2WNPN7WFdG51SjMFpCXnvYlF-CbOBMf7YtkkmyNY4xmTrgMDE81WEpiTu2x1Oi6VSUSfuiUle544pwashdk1wFDd1AjOLjsQNtf0fgKYzHo-Sv45u_Z1tZhfuHXae-YhMAKQJ6dFnIYBlY74DLZJAgUAgsYGJHKNOQQifLUEYvGIJntWGLuIqKh4wzwPvdV3jOpiK3GgO7L92dmhdO2xQ5RqsvxKsU8vq7jnv8hq4PFKpb3hHvmt1OEdPkX5N3fRWKuajHJvAQlRk-8NfHQQ5rdV6Xzq0Pms5Wdlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=W--Cbo77Wn6lr1GllAofellvHyaEGzANqtdYiXtljcKC5i_Rg2WNPN7WFdG51SjMFpCXnvYlF-CbOBMf7YtkkmyNY4xmTrgMDE81WEpiTu2x1Oi6VSUSfuiUle544pwashdk1wFDd1AjOLjsQNtf0fgKYzHo-Sv45u_Z1tZhfuHXae-YhMAKQJ6dFnIYBlY74DLZJAgUAgsYGJHKNOQQifLUEYvGIJntWGLuIqKh4wzwPvdV3jOpiK3GgO7L92dmhdO2xQ5RqsvxKsU8vq7jnv8hq4PFKpb3hHvmt1OEdPkX5N3fRWKuajHJvAQlRk-8NfHQQ5rdV6Xzq0Pms5Wdlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OutxxGle3mtfwXHEwXsCxTgSY1EirC9nRYihqiP8e8LnPZFPmciOEympaVs1ZvwHb9sryBRA7N-Eo4FUsJ3Eg9lNcSSFGN8ff4IYCetMiXf3W_yCd6XjkaA64BKkaLKxiAw4RA81y3vhl0rYcmvBZBKQFn1Ra1YC_KIKws3BH6gSqcQB6Cdn0QEf9lwcG-VuqYVuqmv7MNE-7cvKs2Np4xj_VRXRSLgxq6J-cyYM58cDePxpIGtLXwE-xRooqCuFyCxJA8g-hOAVW6un45Ci5p3INDv9mRFlPXGvweMIoB9tBgAfNiauj8qcIDk9EihpJfxdQuHyDnpLWQLJD9zwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s4OJMwiPFSUkgmVPuwUX_He6jGrhSWueb_lVOiMivorDlHEy06EvqzmuOhglndhDXym-eM049zBzsYQ74OeRUF5GK5RC1NzQTE6rE06YXkoyDI2GiqAWxEFz82gKwAYm7OELjDsmL81IMMHghnMhBw6V6FVyZ7mN5swnIRWyfRKiSUL86sNQSQh61pdIFIjXyfoFpXKYDv1FkaYfI4TUouKzerVZ8Wq91sABgkdLZSbIyXRAlFzg-auxc5Z1YVun5V6XjI0mFcjAfVll7oOcb8JpBzNVf_J9kUeeY4W_y36R1s5qRZGc_TdVNnVy0u5Csoi8jpGainh0frz8VqgzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Uf7vLI7XxCIMDSZ76T53S7eI1i3N7Jjqd-Ww8F3j0TzOITuwDtqHLmHOSPVel8CvLV4XMXEYFKEvQpBG7jmuMxgGvMd_9iWWS-B6Te-4t-Le8UoQpclJSP1QxwcHOiPIfz16NtuUi-dhPM75x3xQOCymdxrUbCYawieUHzlsR5hVPAqAQIapZ5VMDr59O3IR4cfYUaoXJTWx9pZP7pEQuaDNVDEtYLrdnfM-N_ng5GDHq8UPPzqvNkmfhyXV10o1Y0DFY8gO65OdVzcbtAgYYJ2eYprSrEqn1FUFxeNfYGF878ip32v4nKjyfEb2qbkPeGl8rjGcU5q0Eel7P4ADYrBwyvlLXsqtwJiPUQgpy_MCYh7RDU-RLThF6ZgOxyirTRZw3kKP8b7tMPdwCrvqQRYnVuqUDl0_XIlvM_9J6DSS4QGg9U2EvBqaeaq0CR0ssdWoRU4LTRjdoVx1ca3DPq9DbU_sPB1gqL42S-Qzu-uIvCLJ9BFHnezoGWPLN000MmBZI6weyyX3jMEyfEXmk6WkX_F_QjcjmJWLKopenT33JmcEsXOvwD2eHAVcwqHByJNHAhOYMWffvfZgSAF27X1HCtsp9YPhPflBnmUymIrBlZAhi_kSRSwN-9o1GFdi1aXZE-QqI4WPi6CIYeO871O95Xwk69Xo2JIsp9TfHZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Uf7vLI7XxCIMDSZ76T53S7eI1i3N7Jjqd-Ww8F3j0TzOITuwDtqHLmHOSPVel8CvLV4XMXEYFKEvQpBG7jmuMxgGvMd_9iWWS-B6Te-4t-Le8UoQpclJSP1QxwcHOiPIfz16NtuUi-dhPM75x3xQOCymdxrUbCYawieUHzlsR5hVPAqAQIapZ5VMDr59O3IR4cfYUaoXJTWx9pZP7pEQuaDNVDEtYLrdnfM-N_ng5GDHq8UPPzqvNkmfhyXV10o1Y0DFY8gO65OdVzcbtAgYYJ2eYprSrEqn1FUFxeNfYGF878ip32v4nKjyfEb2qbkPeGl8rjGcU5q0Eel7P4ADYrBwyvlLXsqtwJiPUQgpy_MCYh7RDU-RLThF6ZgOxyirTRZw3kKP8b7tMPdwCrvqQRYnVuqUDl0_XIlvM_9J6DSS4QGg9U2EvBqaeaq0CR0ssdWoRU4LTRjdoVx1ca3DPq9DbU_sPB1gqL42S-Qzu-uIvCLJ9BFHnezoGWPLN000MmBZI6weyyX3jMEyfEXmk6WkX_F_QjcjmJWLKopenT33JmcEsXOvwD2eHAVcwqHByJNHAhOYMWffvfZgSAF27X1HCtsp9YPhPflBnmUymIrBlZAhi_kSRSwN-9o1GFdi1aXZE-QqI4WPi6CIYeO871O95Xwk69Xo2JIsp9TfHZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=ENN5PEUQL188Pc6R3SdfYMQ1mzCZhxIUfUyZmqBhoQ_GgqQEgZJNTwS3U294EmznUx5MLh-7Jr5Tx-gX_zn6sbfAt272g5yzJQC4Z8zSomaFDD19jegrG_d8sznrcL_wbWJe8ugYEWXbKRJSAmYSQ3X6NOR1oh2a-487AiRUkICdiNW7j9Y5H0TL2Pa3Q5bf5v3ibNFMqgN3hC4CSP2iECIxrwwxKkfdBXiVOv0cusLwBo5RHgl476MEAeHQdgad191O1t0xHa_5JM8vzqPuQl1QNkxt2WD_Z-YiP3rWswax7Tl_C9WA8zaV7VEYtvVG9nDIy2QyB9STf57ysm1vrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=ENN5PEUQL188Pc6R3SdfYMQ1mzCZhxIUfUyZmqBhoQ_GgqQEgZJNTwS3U294EmznUx5MLh-7Jr5Tx-gX_zn6sbfAt272g5yzJQC4Z8zSomaFDD19jegrG_d8sznrcL_wbWJe8ugYEWXbKRJSAmYSQ3X6NOR1oh2a-487AiRUkICdiNW7j9Y5H0TL2Pa3Q5bf5v3ibNFMqgN3hC4CSP2iECIxrwwxKkfdBXiVOv0cusLwBo5RHgl476MEAeHQdgad191O1t0xHa_5JM8vzqPuQl1QNkxt2WD_Z-YiP3rWswax7Tl_C9WA8zaV7VEYtvVG9nDIy2QyB9STf57ysm1vrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=PnUJHfSUoEO_qQgHm5UzYz3eZlDbYK2OdZf_8v72UaSMTTkS58up3wdBwLcJ0NLY71KY_HL6SPBx_vo1YrZapC3jRsXeZer1eilxXr_A5iANcM7J9ConV4z3-nzuyyq-x637APCsjLXpk2iEJo6sEABYncTgaqiCDNu4CJAb52qnoVW6q-InGdQav_8dscPLUzSLgoOIXWxxa-l_oxWCClnx9vQFT_-JlmYEAAUwWbiME6MC0U5KSVuQ0Jaz-hF_LAqLFO8YkgDDRYnC3ZrAYDcBviVa4hCu75mndlawZAp1KGwm6UvjxrLFRzdwnD94SjSTIkTj4ee4dR-4BccZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=PnUJHfSUoEO_qQgHm5UzYz3eZlDbYK2OdZf_8v72UaSMTTkS58up3wdBwLcJ0NLY71KY_HL6SPBx_vo1YrZapC3jRsXeZer1eilxXr_A5iANcM7J9ConV4z3-nzuyyq-x637APCsjLXpk2iEJo6sEABYncTgaqiCDNu4CJAb52qnoVW6q-InGdQav_8dscPLUzSLgoOIXWxxa-l_oxWCClnx9vQFT_-JlmYEAAUwWbiME6MC0U5KSVuQ0Jaz-hF_LAqLFO8YkgDDRYnC3ZrAYDcBviVa4hCu75mndlawZAp1KGwm6UvjxrLFRzdwnD94SjSTIkTj4ee4dR-4BccZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=mmlAr7p0lMGBQ1uR9qC4g_XDvcNUoSfZlNz5mkJN753Jlf89ApQwPnrjyBNVuS6laLREYGmdqta2EIawjFnWhSnAT1ibECvFgwmfQvYf1ao8h8Br0gEgzYFs3BhnuhEge15D0P08KYNRpN9yBykER7kHd6KOVaXWi4pEUzJsGOr_VGfa7zKFYCgXXmiQrSALo-2OZ--eOx0dbMV5Hcs9TzEYMh3W_MzriobylUiVrp5QumLrPN5kUdoC8jepyvfYrOKCtT9kDOgyz5gXauFcw8K0pHWgKdAe6afZCGbi8JoxK415xKXDO22A8gzcv75layVH2nAbnk4wULgqQ4NTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=mmlAr7p0lMGBQ1uR9qC4g_XDvcNUoSfZlNz5mkJN753Jlf89ApQwPnrjyBNVuS6laLREYGmdqta2EIawjFnWhSnAT1ibECvFgwmfQvYf1ao8h8Br0gEgzYFs3BhnuhEge15D0P08KYNRpN9yBykER7kHd6KOVaXWi4pEUzJsGOr_VGfa7zKFYCgXXmiQrSALo-2OZ--eOx0dbMV5Hcs9TzEYMh3W_MzriobylUiVrp5QumLrPN5kUdoC8jepyvfYrOKCtT9kDOgyz5gXauFcw8K0pHWgKdAe6afZCGbi8JoxK415xKXDO22A8gzcv75layVH2nAbnk4wULgqQ4NTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=mZOTVv0G89bYfJAOr2W60SnwNHfDDUpNYAAEztAM5ON41ZwBMa73SqK6mFQjWoSfAWD5B1bhqx2xfk5UlXvmnBDUWMrN2iL11Ubx7LtGAQy6rhLeyEMS-hcA0MXMNT-xjeKsUtcnLAC0rij8alhscqFRch0FqrvSZjfxD4b9jKKiNBr7Zx32Ktp69BS4-Yr9h6aSPVV3qVa3UUkUCcy1TJcWUfaZjyKJLK-GQVX0JtN5l-r4A0p9IisAZcP_3i9jOlTunfOLBAjHFIVhdVA_VYpwfzimXfAv2WM7zwAW__Mr-BSIFIMTS4BdktiUbYuKVnGwBTojgCPl6NRuX9PD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=mZOTVv0G89bYfJAOr2W60SnwNHfDDUpNYAAEztAM5ON41ZwBMa73SqK6mFQjWoSfAWD5B1bhqx2xfk5UlXvmnBDUWMrN2iL11Ubx7LtGAQy6rhLeyEMS-hcA0MXMNT-xjeKsUtcnLAC0rij8alhscqFRch0FqrvSZjfxD4b9jKKiNBr7Zx32Ktp69BS4-Yr9h6aSPVV3qVa3UUkUCcy1TJcWUfaZjyKJLK-GQVX0JtN5l-r4A0p9IisAZcP_3i9jOlTunfOLBAjHFIVhdVA_VYpwfzimXfAv2WM7zwAW__Mr-BSIFIMTS4BdktiUbYuKVnGwBTojgCPl6NRuX9PD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNSQYUce6_reYFgkKx4Kfh_ZKPRPVoYxibTZl4K2z2X8S1v2trLznvUkRq2K2Bhpcv3zHF0qnIuEXYjQ03qHymITI8tpIAMC5ij_imHmIOGEew0UajjbKkAPYK59xZbymhVfQcIkxYF1Aw3YADEOCqzvX9OkCKs398nAgxQKpLhcKgRqeO95P7rBGYh0Ojq7kLhAir5h3c5SX6l0QC5Uygh1zxJ4TOzFyIVOL7LIenmdXqEuKufUaXgDPomPcXCpZ8g4KozSlLZ-t4F17Tphn8dfVA9Rthuzl7UXnrFqQjr6lyVQiz6_T1JAuWQeY_zsFULQ0badCqy9YRRzaWQU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mky0Cs_Hv3xGieS0jlkQaZgr7h_zLe51HKdQWv0ds9cqDcN1UdQtgIALiGLw52X6KWuG9gpxY3sWcqNjVj6U-gecENsL82mHdAV73txU2qO1HWcDnGk_Qkc_f2VuH8f3PII_G2guC94m7gIId3Evl2vFwvgMc_SOuHcduRpdxS9P398bAdRlNKR1Pbo2JcbunuPD4ahmjqjFDP17IqxP2hB9fZqhe5vKX3JTI74bolb25mwMBg82T2_ac2_x5InXNrmC3Mpej4WGuWbRhgCurh48enmZhNq-IxwU16l7sl4bXz8jjiN7ZYaJC24MT8UnSKSeYosxL2-YenpKbHGMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nynw1NZmtKzQ8xgVHUXvtKAX2a8LSm5ZgA2vuy5Xm_1GZpmzizLxPlk6a6h9ZuJmTvAfoW8sG9A2_Hcm2h1jVb0x0dI3Ps-5kwsYrOLV9wHWePmNknkINwvAvELcUt2un_Yq1EJvzRaeM18LAy9a5Lyr7lr71ZiI-cI5uE84kfI6Jt84E-rmOyp7URPA9rflwHuldX6WXQPe2w6p5bl8ADiRrEXR8i9LDlrGrmUSPd4wf-u1kgLwtQ1_oMotEgZ2vDBveVkmXvqY5CFE5mNyDNDBmUp9ikElyZf-PmJJ4V71xOVWzL7V4kRqaQVgDVseHfObFsXZLKTHGCU4wpNHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Pho_qQQMe0PNc6ShdBZDG596iXX0PkgnzhNj204PBrrNRvuM1UhHhwwX_stgz4sZVdZgU993MGFkTLGleh0wbPXmqAkppzkDEjZ_xU9G8nWn6Xb6pl7CaicatfT2T2B6EydrFM5xSn4upioRGk-GIRhfS35WQ4ureR1rPZkw7dqLkFer3cA5BR0AywdUzUNBem_ggE4odpv0FDoWM9ti8ra-_AavjkyOP1U3WI_J0REiCRbCMzZaeTmlfc7HrFerD_-W-5OpisbTn7Qvwxvn8xdUd7O-U_XojwpFFJ7PU9cY8IRL15mgylXm10oh7CvbUKYTTKpQz6gsduHSXBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZIXV0F_fGpmHt06D9ibefe8qs3_Zse7MP8dxctM_fHQt8DlyhTDp-YguUclaZaDkzA08B1VcY2xTevMsT3Uh7itYyTeAuK_PjLhryzoPXUSJrKLlc9016sQG-zLczXOFrlKjth8XneMOoOTKEGpLu77TW829cprwgVjyxQD2n37X0NJAJsHG5jYMCaBV3RdnuLw5DaVKbz06aYStww3wuqtAm01_1UIUO5vC4IxZ5hpPD0LIP2rsvssoir5t1TJGlXRNtaB_HcP9RLAEpiptYADPhsL2VynVypdPZRU3coptD4mBtp2FfkhArZm4EUefX11-CmpvXnoDJ8HCez63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXSkQJN4Wju7QG8NS6W3Y3Qn7sm9uTjaQHR4tLYfjS92agsCwVJlDroKOybGj9oZi_F0aFQDaUf59Kac17aXQM01ARICJzeDnNCo8FPGZFc5hQUVNWzTxb99PjgOlbcRnVrP4YeijO4VK-Q1afqDgj8cdAOc_hw-pSWO8K5hldA1vj6omZotQ_7ICcWI739WxGJ2W2vr1CUcPGmA7th1Va4Nu7p8wXREziU4EEGZvH-H-_mtTu5uMlsgBSVo2MGygayqvFQ2_d9MT38sNJfPUjFdOhfx_Ruk4mg-amBZ1rLD_laMSGMLO2LBJdnheUf-pvev_Cf0KdoSBne1HbRZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=NRINrdN8CySbUBSo5rXzMCBytD7bKlm7AjOnZDZWtUS2pkLMt7xToB1fFcf9L_0xSGg2QR0Xk8ozC1Jo9OjMOmPTD9lLYPFLGUKihLeAVwKMSea7GfEMeju25hXvsZjT7S9WD39ktOYwJYmRngrsqHSpz9eMLAllKKX1i9Sarpz5-OHpJ-ZACtxgO3mK9lcpCeLouIj_JsxbptdYZvQpyJ0u5x-920QGbQxtEd4c4BIqkoLw_uqDoAupz5-pdm4f-pWsos7qAI1Mj38SQWQHm3zvupSsP5Jp4LaE_7kexFTiPm9rqoQjIjUR_loFiNrOl2eMCkxWxi8u-YaS1lJiyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=NRINrdN8CySbUBSo5rXzMCBytD7bKlm7AjOnZDZWtUS2pkLMt7xToB1fFcf9L_0xSGg2QR0Xk8ozC1Jo9OjMOmPTD9lLYPFLGUKihLeAVwKMSea7GfEMeju25hXvsZjT7S9WD39ktOYwJYmRngrsqHSpz9eMLAllKKX1i9Sarpz5-OHpJ-ZACtxgO3mK9lcpCeLouIj_JsxbptdYZvQpyJ0u5x-920QGbQxtEd4c4BIqkoLw_uqDoAupz5-pdm4f-pWsos7qAI1Mj38SQWQHm3zvupSsP5Jp4LaE_7kexFTiPm9rqoQjIjUR_loFiNrOl2eMCkxWxi8u-YaS1lJiyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BcVbkHcaGBYSLrsPLwwsYxoqGw5-RPy6gAuIGUkL7xxm5XFh5veKvZ4OE7TuiIIAuDZB-lMfRkoXc-CL7rdzT25t4rFD2XfwytJGza7Y4UAai3-ZNHdjWaLgcdH37v1Wjk0s4Abc6l5gaC_XP0sH71ssEjEDTyxa6jS4pzQkiXDxl0Ui6tHnjLOR6E27FCR7dFNsLH-kyqX-xo9xZZvAimHSSqeWm2CL4UEiGKNZYNFTqBisSXm4eHkZpWx0DadKRvHGCNtdHJ5rF8vug35sMl5zKR82TC6CyNTova_zvUr3ieOgcDFLV6Y41HXijHKTHAg88j9pG8bUdIi6VsTIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=UsHvciBNSJt0WWx7JWcrb15m39ZIizFzmxxDI9v9OkfJICNPL6CWeuLWT_49GO04KczSb0vAs1jxzvFAK9EIH-OBV0vD_Yp-ea9S8oXBmyZNQ4ft3cgJj4bInKeO1hyztFECBRG94lnmkzyNSx5YPennb7DseGAlJINAS9xk463Ad5TOrXkoE1fxLIhHikQSEBRZI2HMmfqCJhCYST3vhH9WL-OY0momSJNxP2ryiqGrm8kAtzB7Mr9TE7O19qnw_2HZwM4uv1RzuhiJK7cgMQcSqjp2pRf2XhK3vyvAVMJTaqYO7pyQdxwIKJIrh9CUB8ySYtSa-JIubIt7dmgmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=UsHvciBNSJt0WWx7JWcrb15m39ZIizFzmxxDI9v9OkfJICNPL6CWeuLWT_49GO04KczSb0vAs1jxzvFAK9EIH-OBV0vD_Yp-ea9S8oXBmyZNQ4ft3cgJj4bInKeO1hyztFECBRG94lnmkzyNSx5YPennb7DseGAlJINAS9xk463Ad5TOrXkoE1fxLIhHikQSEBRZI2HMmfqCJhCYST3vhH9WL-OY0momSJNxP2ryiqGrm8kAtzB7Mr9TE7O19qnw_2HZwM4uv1RzuhiJK7cgMQcSqjp2pRf2XhK3vyvAVMJTaqYO7pyQdxwIKJIrh9CUB8ySYtSa-JIubIt7dmgmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=jrZnDUC97wlzaL1wvJ5XcoldjCe0-96kgweKGMI7xd8zt7asBo2O3J4jSX-skTUOClx8AcEn_7isa8bR6RpHZOnZ2G5cBameyH1zl5atJhForE0nLbeZSISwigMvz9vTJGek60jKUagAwkkQ1SS_rzgqyBKOCFvhXUNgqDaso8aQHfOGZN-lU0mrcyieZD5j0o7dc4jcCDaFB_3gXXs-35GtYw-rFo0aDntzYN3BWz3ray02u2SWmdOZaAv1ZiajCRvDfaAGlSDYSdJEz_szUmTW1EehBfPOf39edoJ5eA_e6qBDc-UvjtKUJjD6FjGymSrNGT7lehQ4Y-FtFYMr2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=jrZnDUC97wlzaL1wvJ5XcoldjCe0-96kgweKGMI7xd8zt7asBo2O3J4jSX-skTUOClx8AcEn_7isa8bR6RpHZOnZ2G5cBameyH1zl5atJhForE0nLbeZSISwigMvz9vTJGek60jKUagAwkkQ1SS_rzgqyBKOCFvhXUNgqDaso8aQHfOGZN-lU0mrcyieZD5j0o7dc4jcCDaFB_3gXXs-35GtYw-rFo0aDntzYN3BWz3ray02u2SWmdOZaAv1ZiajCRvDfaAGlSDYSdJEz_szUmTW1EehBfPOf39edoJ5eA_e6qBDc-UvjtKUJjD6FjGymSrNGT7lehQ4Y-FtFYMr2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=dPtv68OMwohgJRZEIViNWrSr1h4XAKPzTJJRpphNM0PyhhIsZFSM607HapsnBBqyzv1ptMlxnsKvj7MDMJ77fZXhPxipxcY3oYOYwtYrw9duwK2gAE6mkVMF3FM1-_oGdIoGYM_TsEgOqdfE4yOKquwnf_b35I_Xlx3P3Ul5kC3hJtrbDRLARre18k_MLUk3HDwNEHjVP8EjvxFhXMin51RQP-0DHBY07FBzmzc6FDzYjNj-b5yUAeeKFsDRbPpvpWHtnnG97YzFpir90engKU0rRxLX7FltbzO6Pc4H62QMvmg5M80ZtC9-9i4B-EPNnP49omKlafjUfA5SjoMbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=dPtv68OMwohgJRZEIViNWrSr1h4XAKPzTJJRpphNM0PyhhIsZFSM607HapsnBBqyzv1ptMlxnsKvj7MDMJ77fZXhPxipxcY3oYOYwtYrw9duwK2gAE6mkVMF3FM1-_oGdIoGYM_TsEgOqdfE4yOKquwnf_b35I_Xlx3P3Ul5kC3hJtrbDRLARre18k_MLUk3HDwNEHjVP8EjvxFhXMin51RQP-0DHBY07FBzmzc6FDzYjNj-b5yUAeeKFsDRbPpvpWHtnnG97YzFpir90engKU0rRxLX7FltbzO6Pc4H62QMvmg5M80ZtC9-9i4B-EPNnP49omKlafjUfA5SjoMbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItD7CcGek8V1Ht-sDmn1SJOjnEzAgck32mG4xFKiHZA5y8s_W4k9b5TtEXYqPc84O-xBXbGUsglk4VruMRm6uLiCYVbwJ4JKxFlsoU2Cria-VDf6WyByKkw41sLf5yG8kSt17djvlE-N3BA5At1fYswFY4rWkgkS6WGOt8ymXWzg5rqGJLHy6PzzpfGqLSrfxWfwCVybMFVoJQlG8bfqQ95KLOdQIhgBTLsJChr2Br-7CyoMsuuxO_PlbZNZptd0Imdk1sClrwsa-Lh3lgJm3KWbaOi6498MGUxazRxjkROCpGWNwuiKS1TlRDiwTG_dog8EQSDtT6xuYa9upUNifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=eOXyYnPvoxrv9ukeek2f3JE2-rHDU1gzHAAZDtoA5UHuUJsnuQZLbL4d872-mu983ZYYf-iRESldf5ghBaVNGWdItKZS-ROtgS0bixtf612ecFrJqqprfT6ubDzRhqB7b9U3jurVNLXYkdHwoe2R9noDsSsmRsgBpbefjzRUN01e4qPqGtXfnQmlmKz14pnjbUUk5YDFbOwSOzdTsQelMzO-o_dV5ukwW_WR73vXGZEqsakl6Qdh78g249nBqJLX2vfGKsw9MAIhnsatgk9gqytknD7xYrzw6F3a73QM30xRwDCCpJXwvXkB2qT0UcjEvKVznAJJ6deUgpV6kYLKig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=eOXyYnPvoxrv9ukeek2f3JE2-rHDU1gzHAAZDtoA5UHuUJsnuQZLbL4d872-mu983ZYYf-iRESldf5ghBaVNGWdItKZS-ROtgS0bixtf612ecFrJqqprfT6ubDzRhqB7b9U3jurVNLXYkdHwoe2R9noDsSsmRsgBpbefjzRUN01e4qPqGtXfnQmlmKz14pnjbUUk5YDFbOwSOzdTsQelMzO-o_dV5ukwW_WR73vXGZEqsakl6Qdh78g249nBqJLX2vfGKsw9MAIhnsatgk9gqytknD7xYrzw6F3a73QM30xRwDCCpJXwvXkB2qT0UcjEvKVznAJJ6deUgpV6kYLKig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=WlDwwRJM5EUpxIlsHGP6nMmIWh7Dcdb5-BFKnXIGzTc5gDFrPb9EXODwmF5S_lNLNjn91jE0jfMPM2U9Ne_ech4AY1ECKH2ZDdsqpTKpPNIxGJ0GRfP9W6VzcPemFKObnXQFZ5LTc6lsZFp1TYc-QjRmFybV0j-Z1hOOGiJInt0ovo4bDHaj5Pw6lhHky-NABI6L8vEyOz0wCNz3M9ilB_jvP08LGIbnUHfAYQDzIUJ2U1WKTjAebvCKnR7x7-ZPnWGzKfosLSxK8w7UaEgzK6fJlevHMc1NjDMR8sZ9-hHUF-d9VVDhj7ULZSc-NT6UWGCPVeWos8qLpK7_z8i4og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=WlDwwRJM5EUpxIlsHGP6nMmIWh7Dcdb5-BFKnXIGzTc5gDFrPb9EXODwmF5S_lNLNjn91jE0jfMPM2U9Ne_ech4AY1ECKH2ZDdsqpTKpPNIxGJ0GRfP9W6VzcPemFKObnXQFZ5LTc6lsZFp1TYc-QjRmFybV0j-Z1hOOGiJInt0ovo4bDHaj5Pw6lhHky-NABI6L8vEyOz0wCNz3M9ilB_jvP08LGIbnUHfAYQDzIUJ2U1WKTjAebvCKnR7x7-ZPnWGzKfosLSxK8w7UaEgzK6fJlevHMc1NjDMR8sZ9-hHUF-d9VVDhj7ULZSc-NT6UWGCPVeWos8qLpK7_z8i4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=lQyQqG6Zk0r990dKIcoLJ5-F8iMgh8zhODlKndk5bLoktrf7s6qsDFG28rwewn2PF0riJ9WsUiSk0JOF_1XHXEOWHE_HB5LrYIgOHIKGq46VNce53L6Pj6A9Mhdv1NebbNeJdjrSTwYdjhh7ijU95e_v6zsRDuXF8_UoXwGUJr75BLyIL0KmU55STuHWR3BeEVxZkjGzXdtrWHbtWct9Jz7E-a_DTn2yZ_8t-3QmFFZkyUwloG65Z0-665H5Vxe_tE3EFLdrxXsfM57gQ7pKRLhuvs_8e-NeQN74OAMUpPzDAmqO36-J72dkaQNsNVzDLGgiTZrrDOL0eyt3-FcM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=lQyQqG6Zk0r990dKIcoLJ5-F8iMgh8zhODlKndk5bLoktrf7s6qsDFG28rwewn2PF0riJ9WsUiSk0JOF_1XHXEOWHE_HB5LrYIgOHIKGq46VNce53L6Pj6A9Mhdv1NebbNeJdjrSTwYdjhh7ijU95e_v6zsRDuXF8_UoXwGUJr75BLyIL0KmU55STuHWR3BeEVxZkjGzXdtrWHbtWct9Jz7E-a_DTn2yZ_8t-3QmFFZkyUwloG65Z0-665H5Vxe_tE3EFLdrxXsfM57gQ7pKRLhuvs_8e-NeQN74OAMUpPzDAmqO36-J72dkaQNsNVzDLGgiTZrrDOL0eyt3-FcM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMlN7Sva0Eq1L0GGlpDAhDuX7BCMwMHEG9ZPfDIfIBPsAts8uOfblEr-1K9HGwA1hL6K6T0r8_da11pR8k7i8XdPAAmishmvmE83EA8pBMmb4PSEeNozFbwHBn1qjEnnestDjiDSw3PKtzilZtH3hHwsR4iWR5jueB3E516aqWwNGyeieqdBnPQK9NPrym3ivsYOlLMme2W_NvvV2kODqqIXDDxeKGJk976-TOVNloDrNb9hZqyq61hUmYPE9CfAIJxNsfe2X4hNOoyLO2_syX2oxy4g9e_lv4WBMrEcO1g2J446Q6b4hoVwvGMLKF-RT53qRsYC2FucdwBclE_bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPJyEZSu_14ZGZXiCXCyuZd953zmUTqX3tmY__qe9gKz9e4ezTUY-Ox-1f5kgr_PsLJPIv3bKlLIzuCVAaiMecxhqLeg1Pdb-vM4NSuBWcwgNwFZDarL5mCtxfpQbB5ybAT2LnA-e06ORx8xWY59S2wnIrpfKXHB98hqcpvXlvfj1l3ZX_R5izbqajz6uA0nOInLLludlO6LaOP63TC4mOZJJMTht5ZCyxlNJlM-qBxu8eB70qcCQdQmGpqqFXUAucpEePI3MtenbrwsQFl6uJMnYnvQAJ-oOgEzKtsdj131pXwpV7aqM2uzH53wEubWkSwbSCROAznT7jNP61ifxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=JWcJ_A4x1DKcvwtNYRMIb-wwQOr9jK5mQAG69CilkC6XNPYWZdZfIY32aswg-zkhEeA60ov-KXrZI55RmXEiLhPJ-V5PHNGj8ylEKHmON22kVv-v09XLSuH-5s68wWmvRwalNkpTg3Zsm6ShCa2UC5J4nmobkB5_D9QPDJHo_VXAlHo5dQwvybTqOVuhcGlIZOM7iT3NmIi7piW3AIx6_b1UyHY8yJZVgM9BprQqPxCp9wTyZlh1ZN8zeos4WYCjiwjD22QuhGMhUBXNhpqY5FEBXQQNA_7l-i7GPq5D5ouvVa1XH3SDxP7hFV3pKv511IMhjyVB9bxmsDmRCsuXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=JWcJ_A4x1DKcvwtNYRMIb-wwQOr9jK5mQAG69CilkC6XNPYWZdZfIY32aswg-zkhEeA60ov-KXrZI55RmXEiLhPJ-V5PHNGj8ylEKHmON22kVv-v09XLSuH-5s68wWmvRwalNkpTg3Zsm6ShCa2UC5J4nmobkB5_D9QPDJHo_VXAlHo5dQwvybTqOVuhcGlIZOM7iT3NmIi7piW3AIx6_b1UyHY8yJZVgM9BprQqPxCp9wTyZlh1ZN8zeos4WYCjiwjD22QuhGMhUBXNhpqY5FEBXQQNA_7l-i7GPq5D5ouvVa1XH3SDxP7hFV3pKv511IMhjyVB9bxmsDmRCsuXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QKtLyiB3t2V6I8EmwhAtwoe5HmcTm3-24VdChH1SLbhOTakOz2zjRdbLcdWaW-plv6fyTwywUkSFKoVCkLeqjKFsa651GQBP5NPfO1rLfuyXkfUdYGhnVQc_E_LtUD67Ydx95awtqdXTLvrVAU6Ifo17Pqb76xnFwHPvOJDXibKYzIG2GgZA3C5D8C-GZ_nVlqGcRcB_HkeJL42Inanq_DPMtujy_EzAarayaYg5e-cSllpwvTux4Y3tbXGYqIlgUxgo6EDfdwa_3nrx2GGVBifvTiEiKKYrAjOqCkY_JhTvxUdDQQzxc5GLqUpcbAtJA2ecd92Vandzt7IhgDVPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=d7rYNkqh_8924wrPK7p4BZsILlkPqasAYcRlBObHYXRBR9l_cbeYdyV2aCY0ycIU8nfr9HI6NoqnJhkrAavegeQ-Y_i0_Rylh5_CkqGWIutV36tnmGATNaGlMm-f2g7szGsrs6vBPhyIWvOw_34awJ6FVqVfff2glKWtcTzaEG22_DL06a5Dz_nnbYs60nDQhn-gplZ84xf3mjs44m0a3yxNPFZ1wG6T2M3O6CHVjkfXBPxgLA8WK3YKDf5OZa3c7VstwKxd3sHfao2gwmrHvrlsjDyP8dVvKowtIo16Ex-7Mr5CNaErpwAkyZD-HlmE2LebYrPZ7Y78y-HkYFXe9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=d7rYNkqh_8924wrPK7p4BZsILlkPqasAYcRlBObHYXRBR9l_cbeYdyV2aCY0ycIU8nfr9HI6NoqnJhkrAavegeQ-Y_i0_Rylh5_CkqGWIutV36tnmGATNaGlMm-f2g7szGsrs6vBPhyIWvOw_34awJ6FVqVfff2glKWtcTzaEG22_DL06a5Dz_nnbYs60nDQhn-gplZ84xf3mjs44m0a3yxNPFZ1wG6T2M3O6CHVjkfXBPxgLA8WK3YKDf5OZa3c7VstwKxd3sHfao2gwmrHvrlsjDyP8dVvKowtIo16Ex-7Mr5CNaErpwAkyZD-HlmE2LebYrPZ7Y78y-HkYFXe9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln_3BRQvDFSks21r5heug6LIBg1bMg7Jwz_95GJj2VDEnbwfGpZoZ6gd5kKFPCH2A1koUlQwHfPt78DmESt77DrtZOUXON7j5d6Tt1of70GpjlrtMekIjkKK5tmFNzAINYUDA-6mVuJ2LO38sd-IN49sx4WpZxg0sUYfbWWKmx0Q6a8Clx5a__j3U2Qxg2n30dbR0FiwFy6RhQ7rkpdbowz9NYn-206Xl89qbJduAKDJ1XUn51GavcJduzq3D_R2y8VsPbZtUjtAJO_wZVW4ymnVZM5hLOJb5MuG68WJsw_WvcvZ8mSoLmxQmL10HdTZNzfvtHcTxHXwSwqFdH5s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=M6hh27miP2udTw_HT_In6VGOcjxrY0qwZBSFAS4F7La1JkKZ0Z4nyhMraFo3D8edWfobRv5TFaI3-rWApaPNylE4tC94O0mvBQ-1VKGRp7ZE8rs1MbmoYtKzvQqQOBbKufBwNrOAvuEL7GE2HtCshUbAX-kT5gkivC9OeJerX5UyWZ3NLEEPrtUCy__zTfls6DQBSVeZEqdNMYEFKCrG3VexXEqCn--0ejAT5wHlCl3ourBS11l8QxxtV7NW0kykIauPC7KlQn9NApip-RPr5VJS257GixTCRIaZCPN3ZGQFBNEl7WA7ARUwYwixZD7n4lCHcq9Nt9dQuivfSwByVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=M6hh27miP2udTw_HT_In6VGOcjxrY0qwZBSFAS4F7La1JkKZ0Z4nyhMraFo3D8edWfobRv5TFaI3-rWApaPNylE4tC94O0mvBQ-1VKGRp7ZE8rs1MbmoYtKzvQqQOBbKufBwNrOAvuEL7GE2HtCshUbAX-kT5gkivC9OeJerX5UyWZ3NLEEPrtUCy__zTfls6DQBSVeZEqdNMYEFKCrG3VexXEqCn--0ejAT5wHlCl3ourBS11l8QxxtV7NW0kykIauPC7KlQn9NApip-RPr5VJS257GixTCRIaZCPN3ZGQFBNEl7WA7ARUwYwixZD7n4lCHcq9Nt9dQuivfSwByVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=aCQF6Z0kMI1n-ulDcwwtRutJiVnorH-2xfGPzfwA2VaTe7y-omax02UkXkEUQqlO35cp5DWH4PXgFEKhEyV5JJAGuJpVcGKbStB1O1nCxBe1T4Xq2-lSbuKVgsxsndL9XYI_1fh7PnTgwvvv3zSaYUiAVTZkYb41NuuT-_QfvRasPny2C1Su6eR8qUw9YUArTrtpiBnOHVzOJqw9d2VDyUcLZmkCsrhU9ASJFDOL1j5J_rkwin-VS3QU_hqf_p5-H6s-CIxCjwzdvcSRsN5S3Rou579XiffoV8F0Lrhx2ACpRedK72kxOM1msbzkB4YjcN815rcGP2nztVGeXYOW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=aCQF6Z0kMI1n-ulDcwwtRutJiVnorH-2xfGPzfwA2VaTe7y-omax02UkXkEUQqlO35cp5DWH4PXgFEKhEyV5JJAGuJpVcGKbStB1O1nCxBe1T4Xq2-lSbuKVgsxsndL9XYI_1fh7PnTgwvvv3zSaYUiAVTZkYb41NuuT-_QfvRasPny2C1Su6eR8qUw9YUArTrtpiBnOHVzOJqw9d2VDyUcLZmkCsrhU9ASJFDOL1j5J_rkwin-VS3QU_hqf_p5-H6s-CIxCjwzdvcSRsN5S3Rou579XiffoV8F0Lrhx2ACpRedK72kxOM1msbzkB4YjcN815rcGP2nztVGeXYOW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH5Kp5hl1YRzv7bAxi1HOIMir7w6CBOGyB1qYgdg3GOPkrQPk1bMc3BAfm_3uCsyJPH8sOqpgnB7wDVTTF5uSxOUv_b9Q7_QcagKc0fyrV3CdRvxJXMGfpUbRBI2Z3Nq9rM5ACbcS67zaRkatIOH4GBdixYHmkpgjGSLu5DK2iCFOwPfTnDYzpTEF-5ZCBJziMntXy7N_FEVD30I9jhkh7kFc7fHQbKauaioYjLNT0eHuiWVI8ll5fk2FHgaG3NhST-gMJkPo57uwtrH4qXBSOHDP6n0CaGA4HMAJe-pXarRzRrP8GsLvjPKAe9CoPLQI1frRwPE6Bwn0wmolZj4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvEQl61n8nEQnBIieoi9xER2baSYre7t8sbqRj8xbnhmTU9J6x5f-g5OX50kE3O8JHJC64bSR9DDVWet9nJW0NPq7gS6tyGDdRsfsBNv_HB7pWfM0g7tbPy4r-7Fd6AeGghHhOfAV1ls3mKOi5QABsU2syMIcwAH8M0ZXd_nwbhSCYzdKCZ2dmUshANs2WJqKG3pmxSDo8Bl-ugmGREaxKJGqENpAwlVqcESDMtIc2Ci76K-ya_YWECdEXqY2kjz1-V9QhvHaBgPzO5C5XU65EE0nTUmelga5swDHVsFrhLxani1eSQkGwqK1WT4jbXf6n0w29IlJed6ZGS82UZxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6_G_SuPcq6ChqADr_Tgb5XQqCYQ6pO4_jMso8SV3BPrTzRf_KC6_y5G9L4ZvUVa6lmGEzqLpPIJff-2sDWywgK5BOVeQtkLzaIgbGhzZNoWljfG0Hji2aDoJPOTl9WyE5nzwy3_l9YYwGugzbm3BnbovFcsPXAEgPaAh8H8fucRnDjIlelvPvkytZpVh4LKBbcE0Lh-10myGIYnzxUSShxXaQQpPLWHzq4uvyYOqilyaUyML9wzhyUJTOm2ITyt5zGQbn9vsaUDEAyIKdytjMc2W_Lc0ZRvNGc5l0xeJSmx0QIQMp7fHJ8VaRGa-t0nZbwB2r9Cnx4Amjn4Z2aXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=p3j4EbNg0hfK-tMCwjUsLXzMuZAXN2Auo1g-kXyXL_EQbAzd_FvATIXEh4naL1KBdHOVGZhrHyJ67gBufzmr-9PVZmNWrHsKvmSArHnsk1gonEQ7nZGz-4EJJ7Cy3KEjcanepf7-W0n0xCMI4MZ_35UbkfhVzFgQaYzjvdxr4RRKJtuHxLlAgfUMVuduvggi1pn6pGAaL-qTbEzBL3oWM6kd97wRVrzlsgbHS9fPTFYkxx67hhhFnQSd_0I05LZVrKM2oYqr6NvhVU9Ay8t6gRe3wN-nsKj9ZdA5wE-GVLrZx4oQ8U4ZtA499tp3N8amSHPwfKFElai93dHmqBi40w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=p3j4EbNg0hfK-tMCwjUsLXzMuZAXN2Auo1g-kXyXL_EQbAzd_FvATIXEh4naL1KBdHOVGZhrHyJ67gBufzmr-9PVZmNWrHsKvmSArHnsk1gonEQ7nZGz-4EJJ7Cy3KEjcanepf7-W0n0xCMI4MZ_35UbkfhVzFgQaYzjvdxr4RRKJtuHxLlAgfUMVuduvggi1pn6pGAaL-qTbEzBL3oWM6kd97wRVrzlsgbHS9fPTFYkxx67hhhFnQSd_0I05LZVrKM2oYqr6NvhVU9Ay8t6gRe3wN-nsKj9ZdA5wE-GVLrZx4oQ8U4ZtA499tp3N8amSHPwfKFElai93dHmqBi40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=phlbi029XMsyD6fBySb1o8YGh47k48kLHaHLUoTcFOwHifIoIlUO54dlkRSTAqFDSgHIpqrgx987rU6L4orFtVWKs4xOIezU1CQ5sdAVVm3e2hNnzqcpMC0gf3gcyUxmNY3fywyrrJ5N5m-4OMDW7CYMZbcBjFb6qizq8RVhp1DukXZ_83rSGDUT6JkdBchbqyI_Bluofb7zi-AyTRSlNqhXlSAsQMhfIg86gEbaIUGxOizUGz3hewsVxeZutFcV_ZP-QCWKb5rqVtBsgME0Gnf65D-KljUIzxWqfeG2BLkxjyUEUhwWmucjU6_EztWJbG3Ok531ZGM6HdjX41-pug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=phlbi029XMsyD6fBySb1o8YGh47k48kLHaHLUoTcFOwHifIoIlUO54dlkRSTAqFDSgHIpqrgx987rU6L4orFtVWKs4xOIezU1CQ5sdAVVm3e2hNnzqcpMC0gf3gcyUxmNY3fywyrrJ5N5m-4OMDW7CYMZbcBjFb6qizq8RVhp1DukXZ_83rSGDUT6JkdBchbqyI_Bluofb7zi-AyTRSlNqhXlSAsQMhfIg86gEbaIUGxOizUGz3hewsVxeZutFcV_ZP-QCWKb5rqVtBsgME0Gnf65D-KljUIzxWqfeG2BLkxjyUEUhwWmucjU6_EztWJbG3Ok531ZGM6HdjX41-pug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdJUC8HoGN8QBAdILcKlaCmd0fM9Rz71TObwF6yA2PEI7bRCTdvsnrgOItVoPWKu8lk9nDPU7f7iu8_iwXMk9-ZR8OQt1KuyH1P1aGvxbOzmQ3ypVogU8MjWyAsixXRb8ZGWBrx7WEGTI_XeY1qWfkBumshCL-ztLcov06nsssfbKxKVIGyEKEYGfKR6Nr04XH6hITwPdTPbwT8h9BIanI3oSYgKE-4H3Q1EjwwiV2rkn9tvOZUpwaxUC6dykAg3neTAzQzYvLQljnFcn_iUmrSgWtrbYjIR1uOkQT1GsIHh8vkyYfPjJn4pnmv6o9gCcYtT6UjubW_eizW37nNRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=QB4jlabQDvUin0dVquLtt_bWNheCO0m_T6MGH6lbDWII43Npsx1uRaznf73FUEbqy9GkU5ZXdEXg5gH_Ful0GhmfstkJgitV4wMWr6WJyJNouxMOltrJ-kGHNAk1Z8SQcTdHST6tZnlE58tB9TsU4zSHGDpvERfaSHTBwNVvJVj5SJDohjJs4WojGH7EirFDzZtP1EBs-ZFJNG1D_IDSpiYCwwI_VdC65em7ZJUuqUibFv1lnYU-FZ6Hs-rD-RsIpgRSal7F8NdF2PvzEfXdtLC1ZrZT1vL_CdfIAZFytoNieBS81fK3Xsb79MgtebqM5y0T7SAstqsUhSL6-wNj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=QB4jlabQDvUin0dVquLtt_bWNheCO0m_T6MGH6lbDWII43Npsx1uRaznf73FUEbqy9GkU5ZXdEXg5gH_Ful0GhmfstkJgitV4wMWr6WJyJNouxMOltrJ-kGHNAk1Z8SQcTdHST6tZnlE58tB9TsU4zSHGDpvERfaSHTBwNVvJVj5SJDohjJs4WojGH7EirFDzZtP1EBs-ZFJNG1D_IDSpiYCwwI_VdC65em7ZJUuqUibFv1lnYU-FZ6Hs-rD-RsIpgRSal7F8NdF2PvzEfXdtLC1ZrZT1vL_CdfIAZFytoNieBS81fK3Xsb79MgtebqM5y0T7SAstqsUhSL6-wNj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1oQ5BXTJMNVd6C0opMkQilFHhE3K2lCnT0qF9JkzRHPvqEFMeiuo8DRxdfjfuvAANvJoT4NmNMSynrZ-RbLD7t61vuIYnLVaXHelydNdWx25rfCRXbFjSUr37ctxY_smgSjQH0BHbepRGCYpjzhUCGnRDPiPxXiO14Z09VgnJcnxzGr-v1dA0GhgA3rnUieg6twQAgDPOR2d2YeLhUuiU5WDMpFGph4Y6zmfMnipWYs165_Qr8yPhKXQALbbuYBVazNQJzZz21QgmHsPmbvFYcDuKZFdKsH_hIyAGrFCAqrMquCdBrvxV9FB94Em4TzH1cBjmXOgFC6UuK4obWKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=Hx-kkTiYKWOObK1kJ780ZiptuWQTAiozNuyTYqufR1iSrI74DQ1dxWDPUlYKRhzC16xoMN7sxw_PoxXEe7trzGLCs2OEqz9uzz2f1iwVVJ5xeLCKZaYHi2h3bqEx1H2d2yVRDZOxr42z8IxgjBZ7YW-vvqONkDaUS5ugqesPt0KrU49J6bQxlzylj4lGBHLeeD74u4esdzb8S7i0SJbf73v93AfOrdi_o_XvlJPDeexfSF9dumkHRsKuPxk89OVSZIUJ3y9HzZxOIjpGL3DhncUjw3MdgQir8sNo7WQas4xoG9sXn9eDkOl0v4jHB4sWTNUa-8NElbQA1lHyetv_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=Hx-kkTiYKWOObK1kJ780ZiptuWQTAiozNuyTYqufR1iSrI74DQ1dxWDPUlYKRhzC16xoMN7sxw_PoxXEe7trzGLCs2OEqz9uzz2f1iwVVJ5xeLCKZaYHi2h3bqEx1H2d2yVRDZOxr42z8IxgjBZ7YW-vvqONkDaUS5ugqesPt0KrU49J6bQxlzylj4lGBHLeeD74u4esdzb8S7i0SJbf73v93AfOrdi_o_XvlJPDeexfSF9dumkHRsKuPxk89OVSZIUJ3y9HzZxOIjpGL3DhncUjw3MdgQir8sNo7WQas4xoG9sXn9eDkOl0v4jHB4sWTNUa-8NElbQA1lHyetv_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcx4BIVZLzZ7qvFkZb9Ny6lkNLDmtSjjuGANoQ6iQdjlD780MFSUXmxE1vAIYYJy3MioLMPyIwBBx55mK709hNXePBZdC5DLp5GD439Fd9P2OL3FkukIoNhwkIcJtElZiEuq2YH_ri_KUOcPlYTykBDECVI3JD1E1eU-N5QTeJb_rODE8L00vkaPXb427Tsn1VXYRxu72p3ELCOOU-6ULxx4gTa7vVRbCaiC6k5gI7vr0CQ3SkU356JgknTRMqRgdipSPcgZZ0mSgNudCuLsX5_KtPBNcC1u2QyS8WEbcJnXMgCefxNlhbm15485sZiGYPMgGW0yGBj74rKpTCts9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=tIxTHitvXj7lDwfQond_WcmBn91t23agBzmvQW-QscKpJi_3Zt23FBFdMkuk35LwvHcJKtsVO3H1h7T9qXHz3sKslSKRXo0XySrOnrFc6lp3odUCxvccaumi8XbFSEaB2qK5YBaGDX4vkGyda_Ced_9IkZA9K91jgUXij2RReR3dhgbw4L8jDRmyXaCV3C62nWhwp-27wKUCqgSIuewk6vSA0mnDEXO4Eb-6bcli2TiLbN7paNcqmiG-X8Dt7LyCScAS4VTcUkmxFVq72YAQEwGTBsQpUCZtrTR0WNb2XyNGbuVYD5i2hm0KIH_5ezMubxXV_3So1utXp4zdNO78rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=tIxTHitvXj7lDwfQond_WcmBn91t23agBzmvQW-QscKpJi_3Zt23FBFdMkuk35LwvHcJKtsVO3H1h7T9qXHz3sKslSKRXo0XySrOnrFc6lp3odUCxvccaumi8XbFSEaB2qK5YBaGDX4vkGyda_Ced_9IkZA9K91jgUXij2RReR3dhgbw4L8jDRmyXaCV3C62nWhwp-27wKUCqgSIuewk6vSA0mnDEXO4Eb-6bcli2TiLbN7paNcqmiG-X8Dt7LyCScAS4VTcUkmxFVq72YAQEwGTBsQpUCZtrTR0WNb2XyNGbuVYD5i2hm0KIH_5ezMubxXV_3So1utXp4zdNO78rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=EAuJ78xZtDcolt_dkCPg4KzpoKZeFI9p9fb2q3w7s1q5XraaVfEp4LOJVsh0qVmqWX9TtmLRhtx7qa7U874rD25Qmw-RSW7yO4L7keSXuKSX5brpfqsz_MYjztf1tyt3AfNpkptJvuIkJrw5am9J7rMMOTWJNw5TdFOvWtpZ-Q34eQLRQAgYL6jvKnbVuxRWxSn7Q3Pv_HCV2-cjIDDWqRS8aNKPoZ4SwVEwNXfKAxHt6IDZ2OtuwV5r-88DQw-qOMMGks_qiGNqaOUEJ0FV_recV3VlVY2wzG7fg_X5j0aJSUKeuqw2q96rslLVr-8UKekE66a0caVyJwZgagc94w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=EAuJ78xZtDcolt_dkCPg4KzpoKZeFI9p9fb2q3w7s1q5XraaVfEp4LOJVsh0qVmqWX9TtmLRhtx7qa7U874rD25Qmw-RSW7yO4L7keSXuKSX5brpfqsz_MYjztf1tyt3AfNpkptJvuIkJrw5am9J7rMMOTWJNw5TdFOvWtpZ-Q34eQLRQAgYL6jvKnbVuxRWxSn7Q3Pv_HCV2-cjIDDWqRS8aNKPoZ4SwVEwNXfKAxHt6IDZ2OtuwV5r-88DQw-qOMMGks_qiGNqaOUEJ0FV_recV3VlVY2wzG7fg_X5j0aJSUKeuqw2q96rslLVr-8UKekE66a0caVyJwZgagc94w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=K_0Lh_pU2-DNmMPklbEGoM-1b8BCIrupMn0lCwlfrNpC7z8ekeF8uRVJP_CSh7wRKTK75hwv_d-PGDseu4RQCSgNoiPR-FKjovQ08H2aRCU5Br0TXTn4Cw1euJxBqK1tOEcNtsqfrQt-Foh5b2lnSkX8gf5Nt9zp6U1xUWiQsU2Pyo_RFAsOtAgTLB4hlD6ZQdG5RbMMlqCV_5o3DfLTFyBMY70U3Oeb7SfUZmLTkZEq9on2VLA2HQHtxY0tvm57OfF1hR2Lu-seQWLURsXc5K1rpImaaHFDc3fs2A3bfPwoa9Z9_J8PdFzH6CYBr7OmQZN_RDtSM80PliAC3uzCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=K_0Lh_pU2-DNmMPklbEGoM-1b8BCIrupMn0lCwlfrNpC7z8ekeF8uRVJP_CSh7wRKTK75hwv_d-PGDseu4RQCSgNoiPR-FKjovQ08H2aRCU5Br0TXTn4Cw1euJxBqK1tOEcNtsqfrQt-Foh5b2lnSkX8gf5Nt9zp6U1xUWiQsU2Pyo_RFAsOtAgTLB4hlD6ZQdG5RbMMlqCV_5o3DfLTFyBMY70U3Oeb7SfUZmLTkZEq9on2VLA2HQHtxY0tvm57OfF1hR2Lu-seQWLURsXc5K1rpImaaHFDc3fs2A3bfPwoa9Z9_J8PdFzH6CYBr7OmQZN_RDtSM80PliAC3uzCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMVqd3zfg6ZBn7J2_FeZ3XJpw2wHUY6UYCsfCevUlQbnHBc3BcWZnB95Zrl291TbinHC003ccGcTlMXiSZAs3W7c3v7dEv0UsSE_4B067EtBtEZg3NPP76sHN20yNZkBBrKNiQyPcBFtkznqHuRy5nOTRzByHJZ7ng7CxRpSThurp6Uv_M-HCCxRKPDGLbtPDmjaLf3rUv77NWxBnuX2kNmbmlQzP9rtwAfzpETPHDLrAwPio32MeWnwjF5Ttvy01M6fCJPpV8YZ9KwPyRYh0X08tWBU3PTwHD055FrJ1Ir4m1ToUWVTnybMAoZTmrXZYdRRVzyGkyJI6w_k0TXBnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io57hGDY3TQlbQmF8vOCoT5mHC4pyC6VsY5ZFVoqX1e1s1W0WFeR5e0nt_BHv4lk4UaCCGZFilzcsT3TNBVHZaq7X1Jvt6Q21fyAWqVLtTyPbNvG9YcMDgsz6yfJzLT5objmmloZ3ODhI7joQ1rfLITsPQU63Ho4nJXaPUM5gbvNL1QcSmEtwWyF09QAovHEbHY6DM6QIF3K50DV0LSuoLBO2m5dWDw_hL5h-mp_5tjZuFHt6vfK1XY8T12gpMQeBTH6GxNIqFUjAGlHu9tKRnpVMs-tqBBn_Rm_5PIJgA1xE6b3d2_iWIzmTOdbqmnhBHfE5N-eBaV8o4T-8tCEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usWGzZL-e6OfQ5829AQOcUtlvSGn5GWWIdwC8W6TNl29WYTRyfG51tE1i6ZdEjHy2GhdVQFdkw3Een5lAcdeN0sIm0C1KXIl0fjThi5Qek-k5NbvSQBQTE9EZg50vgOK_qKlm57d83xK6k5DT0HAHOjpSAxpkiVDqOPVchynyehjYPudFZb0Crx_Ke3lpCRfz-2EgH6y_mofdzD22dSsxINUwn4WRrPz6iUWD855pJMnYWxNESJGohIYX1FyHwfGo3w8wQme_h9U4xKw0u6lW1DUziL-UNPhxUNzzIeDKQewadJRO2f1fxfNWfqX6GVQbxqGAvW1Gvn2zNBPmHXEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Db5XqNMWteAuL5e32T4FQHo38qNA1gkSQbVqzzeZIHNsfUx3ibxsU-kwnSOOpY2EAIJ2g0fx90cgAEgGWeorD8Ze5SlrwQdNR93v3t-CUiUVcvdxuwtJeqgtY1AagsMH4PRPzqs3B-Hb9hibVUni69TALjcD2h7_uuShodnzA7JVbdRWfXYvNaeVlM9AT0abEfRYRAN7VkjK95z7mE5Kf7rUf5RMLnQ5DPtBg-4gB-uZhhPccswk33haXP7EXGklbm5kqY1TpQaC-FxnQUtWSVKVOTLD7384l-olo_Sauc9loUQv9-2LEprlcqlGsyiHcdKll-_eOkjODfeofGHfMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Db5XqNMWteAuL5e32T4FQHo38qNA1gkSQbVqzzeZIHNsfUx3ibxsU-kwnSOOpY2EAIJ2g0fx90cgAEgGWeorD8Ze5SlrwQdNR93v3t-CUiUVcvdxuwtJeqgtY1AagsMH4PRPzqs3B-Hb9hibVUni69TALjcD2h7_uuShodnzA7JVbdRWfXYvNaeVlM9AT0abEfRYRAN7VkjK95z7mE5Kf7rUf5RMLnQ5DPtBg-4gB-uZhhPccswk33haXP7EXGklbm5kqY1TpQaC-FxnQUtWSVKVOTLD7384l-olo_Sauc9loUQv9-2LEprlcqlGsyiHcdKll-_eOkjODfeofGHfMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OuHCa6mfoEOSXrXsMR8ImysuefGNSEJry7PeNXsMqCWJOQQhbhjrzCCMJNJAkaiYY0UHISf5Q4gTpWRdrfUozCzhi2m6rw3uWZTkbUDnjH8HxAdrFlUqORQ1gLvVGD8aRmVaLymkaxZv7lVza8lwUf7WJZy4IhDKwwHjjQy2grXEqtyD5xK0fEXd9KANCbkT1k76J_VQdW5M65iXSh1JFgCtLlzrmA-FJZiDUaXDy8_j45427JOpQfewJhE0ow9j3B-BHGyr7Kn1DJ2RaFXcL66kt_iv-uUKG-9vxe2qACbjqDKIXu6iOB585dvkIDTtHPlxSl5RYiqC8pdAM-9SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=myksyFRTzTbWB8GrWybgDi3rbreGt6FH3a9GW-oFUf_DIhOQWlgxQ-OGzANf-qOnP4e2oOXYaY09ByCPcbGICTFhVtYehRVsBL3Dn10rOFzftcBmEmhL9j0IFHvplomlTeUuRO96WBXlc2ldMxzGi6T4PqV7FMzEOqWfwGNAolKugkDhBb-ikaIWkd0M-Y58TCE19zC35cVCRkkP-Tfb99cBy6LqslFx9E_j1_UIKMRjE4nhv4CYoH7J1nA5X-Z9j2W8_MY2aSPqC2WSeoiO1EIuwKseOEveOrtj0nEDjWX9Y6M9aEZSdDuzEPiQQhgpfVhObuRrM8GMUXo8U03l7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=myksyFRTzTbWB8GrWybgDi3rbreGt6FH3a9GW-oFUf_DIhOQWlgxQ-OGzANf-qOnP4e2oOXYaY09ByCPcbGICTFhVtYehRVsBL3Dn10rOFzftcBmEmhL9j0IFHvplomlTeUuRO96WBXlc2ldMxzGi6T4PqV7FMzEOqWfwGNAolKugkDhBb-ikaIWkd0M-Y58TCE19zC35cVCRkkP-Tfb99cBy6LqslFx9E_j1_UIKMRjE4nhv4CYoH7J1nA5X-Z9j2W8_MY2aSPqC2WSeoiO1EIuwKseOEveOrtj0nEDjWX9Y6M9aEZSdDuzEPiQQhgpfVhObuRrM8GMUXo8U03l7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLk278BEyEuoHMIibnBdSiTDkiqdK0W6YahA1SFdnveHRHKlZf68-NLnQH7EmPYmqsYsdN8Yg1Nn4bNu6cHPaBVblnEBFQpj497b6_LoK0Iajf2CwvEiV4KBkjvQoOfBM6JklTaSo2pYIn4tvBMWTV6EsczS3z7CrU0ah3ReQXwwCYE7yB8d-y7oEgdaY_Xu600z3NTKGdFT0B6FHosagzcFfxqAmbNtELZXmMm2tYUqjAD87M_nuf8QhE8Yv6Mf5mD3qnitg6zzexqmnBYT-K9OLZvmf4HtsC7TkuRlY13mPt7WL22vLIyRyrDgw1EAT8P-YRCDKZwna4C2ydU31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=Z0-wUAGqMeQJ9fGZN-4OVOAbAPcta5VIyXwcCyDIy0NNPj4-PVZE3vbMVexa34KmIMjADy2SnmAcp0i6LCI3PP6oD-R_QWvxulu_ialI_WllkDS6256WmHIysyfUqq0Lozn384SpKkpLNeSdIWiM-AcSN9_i_uCUzJGnB2q8UOEJOJac38YoUKIGZK0gforq6JB6_auEFZfSIJaowVj6R43zg9lQBqBKmlmZcWRjtm5P5Hgg8T1DcZ5FeDS5QG5PGb0Q5kkrTptIlMqatfehCwm71idS6oPooMg_Jb3T0EDQLc01slcvMeSUDArqvS6atf2TLuvTPoMd8-KBgTbn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=Z0-wUAGqMeQJ9fGZN-4OVOAbAPcta5VIyXwcCyDIy0NNPj4-PVZE3vbMVexa34KmIMjADy2SnmAcp0i6LCI3PP6oD-R_QWvxulu_ialI_WllkDS6256WmHIysyfUqq0Lozn384SpKkpLNeSdIWiM-AcSN9_i_uCUzJGnB2q8UOEJOJac38YoUKIGZK0gforq6JB6_auEFZfSIJaowVj6R43zg9lQBqBKmlmZcWRjtm5P5Hgg8T1DcZ5FeDS5QG5PGb0Q5kkrTptIlMqatfehCwm71idS6oPooMg_Jb3T0EDQLc01slcvMeSUDArqvS6atf2TLuvTPoMd8-KBgTbn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-q0S7jzCnR86gN5Av_e6E6ywhO9rTT9cyNsRzYOCiQajFzTXtB6Q-QPSfnrrnRaqs5n8-SO8xctf4cQPy1-oPBea5cCJPjaQDIQR2tR6bnqRkZVaEI5dtn-NALnIB8ZQQRMLARzd9mBGnIPv1OVmCNBzS7ShV99OT0Z1exgiMRGfvlieJo1Tdi5y-Da820E9z2N7ZRSPYP2Wm84zwcT7ALjlXLKaeIs4WPCv9hxoT8bC12uyUduMNaFfEJckmZgVY_KV3e46QHy-0aNmWPATYfdlKUew_gCZidaYooQhPmKI4HrJYv_VQQYlI0pO2Wehxd2WE95HDi7AHt5m7E0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0XZ02fhsxB3p75O5DDuvHIxhxF90hIqAskQKeuPtWOyqF00OOdD9x4_B1sWvmVH_nSGOUHDCufGBi3AzyubMyZg98z5SbwSVrT8kjC7tWsEqUgzb99ZSkeL7L6wl2tzr4ycPHM1tSHa6Oa4mnxxJEKo1U3DcSoCtJJ0d4e8pyle4BEgU2dtFvY7IUMlsp3S7RKOdsCJ7HhN-P3kOLSTzlqLEsCEnTahwwpHy3cdqEqf-vFF2rAb9-uM9BiaCNW4O5uH4iVFQezLb6EVh0be-5R8VyyLtWdDJlI2XCBw96tCwC09ghoPbozUASwp0scEyW48eWknil18zXVWZXOR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU-At93qPSTaD6Dw5x0gP2iDgfDZsm0YkYmR7dt5FaGL1bIm-efIF5ejkNQxCaQNX_jULY8TU0pbXTw61zk_OZ-5MHBzQ2AwMh8OjQ37-v-o_He9_POumDc46XYkmVqw8ExjRAT7iJTTlJvrNeMVwYL46QM9Aye5bkAMCtGC0qIf3tREKExKo3GspVv-CX9DPSSeF1lsmrXjaRZpZLGSF11-LhVFW-R_tTMFKa8Dht7auH__lnsNliu8YeoVRueKzM8wh6uoMpdaYMg4mAbHsdqqGJVJSCMMM1odigYJCSQDSDebsybxniua3czSmMJ1paQyLpxHZOh4f6b11-nWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8Lpewh9GJZ9iTtWau7A2K359m6LRHSwYSWURQL16XSJxCqiWGF3YcLTD6SKTTzEEexdhYDnwLgP4PmLtXZoQ0uYWATskF3YQk-IVvpLA0kmYghroi7oVduhhGzrBgeJ0XHKgjD5e-Ii_EZRda7x-hc7vz7G5uEETd2ciN2QXZVoKXvgX0WVumYsmVz9uVk2gWofiop7qZct-5_BcxpSlOyVpMKac1HnV9xSAECaG0ArkZd28Ro0QpzERD8-PfvoGUtcoiWTdpfkOC_DxtI-AZ7wsA1q5l5Vzlza-lxRFT_kZ9SrLFBn4qrILfK3qJHuAyrbisZg5fScLeJzXn6hRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPafOZayeKZLnQcQmwT8bTM5OsnK2GanxtwRVbyPJBDT1HEk-2xVx3o3roRbv2qFiLCaPdwSS1tUZNm1fbqXLHuI1i7DcjoQP2LNMjN7aiXpJ6rFdK91pijQhhx-VvynfaZ7DoRveEVKL9lwPnxBFNFzxekf7G0XQYbXtdafHxtg38rOxZu91jpGkvH_vxMaUz4a3Coe3ntXlyFpKNuquHO_R9QKOiYF6s_11IImP6iSZIkIzJvhRlctYuHajl52Ddcohvv3wIYCfn2yn4NVeNIgXSOZh09H1neNz60dj8a1SDzh5MTCi1Cq9_t36_j8kYJmpUYMhlY0_fL5Yo4BfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=LvknR318FtlxNB3XgGnb2Up40ziHBdrY6d88zzlscndYtNXLZ2QBqJCDt5c-p1cvzCBM32-cG7leSvexivYQ5iVxVWsgRHu2u-N4tIpN6DVXzcQLP3Piv7FydBFGcHQD-g23L1uOT2pEocfwDsbB1Sml_5nE-t3Wl9CJ8qeG4qzisGRI1sybtf6Z-zW_t7oi1JNSMvVe4iv5pAkXALg7tQP4_Zx1Hk12hwwPE-WGVA68EvNCXx-OXUiaz5E3kfbsmpOUk99eLH8RFx85N3y-SzJdLqlpl8Tjjw7a0I-zZXDXAaHWQvAI7blMd2Wrzus2LMLE03Ukro3PU4UhvFVmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=LvknR318FtlxNB3XgGnb2Up40ziHBdrY6d88zzlscndYtNXLZ2QBqJCDt5c-p1cvzCBM32-cG7leSvexivYQ5iVxVWsgRHu2u-N4tIpN6DVXzcQLP3Piv7FydBFGcHQD-g23L1uOT2pEocfwDsbB1Sml_5nE-t3Wl9CJ8qeG4qzisGRI1sybtf6Z-zW_t7oi1JNSMvVe4iv5pAkXALg7tQP4_Zx1Hk12hwwPE-WGVA68EvNCXx-OXUiaz5E3kfbsmpOUk99eLH8RFx85N3y-SzJdLqlpl8Tjjw7a0I-zZXDXAaHWQvAI7blMd2Wrzus2LMLE03Ukro3PU4UhvFVmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=dyQc2cdTEorSMRaunVLfHhf5xiHuhMxO5h84q0xur3y2PiIRfmVRAYan4M9N5gYtX_BPmIgm6VcbJPmS8IRfVxlVN-TS_QzO_ScuV1fv-sjoNr6s-0WTzK4J6PXrMD5WFvFbzsPk9kDh4ocY-zZROg0SY7KEl5MFOMJS9CXutF0mZPMlwPhC1dWkl3jP1yk2dtnX7WAi63fSF5JeKtlOOy8cxf_txjPf0DY2_g0XPZpoDf_L2-d5S4IC654-naSDWQmpim4xH0Ohg3FZh6Coe9tQlleHQL7rGqHCb23JnJF5ObTHKlT5Y0RaNLU0ObzNnxdPvksGa9RkhROvouhURA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=dyQc2cdTEorSMRaunVLfHhf5xiHuhMxO5h84q0xur3y2PiIRfmVRAYan4M9N5gYtX_BPmIgm6VcbJPmS8IRfVxlVN-TS_QzO_ScuV1fv-sjoNr6s-0WTzK4J6PXrMD5WFvFbzsPk9kDh4ocY-zZROg0SY7KEl5MFOMJS9CXutF0mZPMlwPhC1dWkl3jP1yk2dtnX7WAi63fSF5JeKtlOOy8cxf_txjPf0DY2_g0XPZpoDf_L2-d5S4IC654-naSDWQmpim4xH0Ohg3FZh6Coe9tQlleHQL7rGqHCb23JnJF5ObTHKlT5Y0RaNLU0ObzNnxdPvksGa9RkhROvouhURA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=tDjywSCsDzxydGGE3RPxFnHfLl8S5nabojpKtAuFz4QtNpqMEe2z7_J6jUazmqMUNHgVytwXieZUpHSD5KIfceM61yL2kEFa_4azveEggnS2XZl3WBU59Qh9mhmvzLY2j-b9o7qCU_y_pbz9uFalLJaSd_InaWZdP8e_SYSEH7On828lja8bWD6eRJfNvpWY5PHxwLE9dM-V3CuITmp7L4V2a4S8KouGqeNNo2-MvYPFKrY7fzxQ2eVw9vcSYIAumRP6yt0qYiQC5WRBo-D-VZbYmvfydY0bTnQtcQlUnTb1lwxnnmbjR1Ka4T9_QqjU9118tjw7ADlrRNlTbFGM6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=tDjywSCsDzxydGGE3RPxFnHfLl8S5nabojpKtAuFz4QtNpqMEe2z7_J6jUazmqMUNHgVytwXieZUpHSD5KIfceM61yL2kEFa_4azveEggnS2XZl3WBU59Qh9mhmvzLY2j-b9o7qCU_y_pbz9uFalLJaSd_InaWZdP8e_SYSEH7On828lja8bWD6eRJfNvpWY5PHxwLE9dM-V3CuITmp7L4V2a4S8KouGqeNNo2-MvYPFKrY7fzxQ2eVw9vcSYIAumRP6yt0qYiQC5WRBo-D-VZbYmvfydY0bTnQtcQlUnTb1lwxnnmbjR1Ka4T9_QqjU9118tjw7ADlrRNlTbFGM6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmpneZVciqjEcijlCCRBl8WOe7Zjr59pyAGp9NKCb0rK_wApQfpySF9fS3rq3gSNpy9wi3bhymGMfHs7yrRZZ2Q9W5KhK60OCyVIW0NNEoYD6DkmzfLYEGzFY7dWs4GRVbKZWCokZE09KBwrBkEAz6o55B1nqUEvq9v8YdJfOgZcI_eNCCaBuaVmp2KUO9_UlUN8LJR1Qe1ZO75yZtvPabRLfoQGnLRilWAFSamNUOCL6R-zdMGsum-i9yxwCQJASy-GwVDEZXMkFuTEv5gLEXxUeYD8pMTfWo3smGZM_uvEuHM3jjRvZNbrH7XJcxI0-Wk2xd7--hG3p9k6jZrbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVY5_i63uRfK3MJ9LUFrs5EyBBE6zWOw_pneoX419ke45d2H_UksK1FjphQntjV7TigT8UMhz_XQhfIbt1at3AuUtHR8q2JqRFt-zAe0aWV43wJROTbbweml7BNWsUQVOzfWjbAfsVHrga5wu2aa4WzsUZadfXdYLSBr6VZIyuZwW80i1SMOGcKf_DZSVANGCppBAnnDcafuKJiFUgCVS8fzv-RLYIKpmp4v1zqmzy6I5yfAFMfiMWRdwVx6bCjNyQTXEQ3rIhj_7q8SE-eEjeVrSfNNq7ArFXRWlZEgeATTL9YDK_fCVn8o8-rlxiiJue62UOC6eZEombCPaeC_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xeq0vS010W-L3rPxIqbdgV79bB9wCiN3Vb1BolJ_xQV6JQ-Nv6R0S3nZAPinxNNox7EMkuywKDiYpgOSDnPHdQoJrEsbV0lwRCQHhp2UOE4VtF4XBl7GjxnThEGccQWzGf3rAgmpJx3nChrlUBiC4ErOl49js6O_lkNezLCD06dlUMqZdFe54CUr16YwPKs7dG3SE_zoioS_n0kct3R2Naj_z6GqH4w3lmOjVyiPYD64v5qyHKAziPUD7h1WM0m-Q2H8-gmQ3A4TwGsOUS4TIG78Wc7wiFNN2b1sDeqndk_dJzXUmyi-yh4_h_tSnHLSxqSEpcoDikSbY-Oxy69MgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=tVRJY65Jr1Y-bM21lPEewAaIb9vSd_ThucBupoG1WeIlL4VWXUHElIX1RhXqosI-nx6p52-SFsfsLEd0lKmteZCb2dlXW7cXxyf6k1UwHQWR29gnoqsrkOdjcf5jHuHf4Lz_GrgtWczXzUKnvHFZahzrkaWj-5us32Z6U1CCIoBBbkxevVO4Rrb1d1iT5H1IjvMfHe3kdlcbD2zUVQ-jj8gsE1koW3ZCVssuZUPNai8robmV6T0U5xcI8SDHIe5RIJbnecpJJb7sfng3lfDeRVJxdhPSI9Ph6BNbS-grvsFau03N6BY3YdCRbLS0Y7XNd8817TdartXk6D4-sVbbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=tVRJY65Jr1Y-bM21lPEewAaIb9vSd_ThucBupoG1WeIlL4VWXUHElIX1RhXqosI-nx6p52-SFsfsLEd0lKmteZCb2dlXW7cXxyf6k1UwHQWR29gnoqsrkOdjcf5jHuHf4Lz_GrgtWczXzUKnvHFZahzrkaWj-5us32Z6U1CCIoBBbkxevVO4Rrb1d1iT5H1IjvMfHe3kdlcbD2zUVQ-jj8gsE1koW3ZCVssuZUPNai8robmV6T0U5xcI8SDHIe5RIJbnecpJJb7sfng3lfDeRVJxdhPSI9Ph6BNbS-grvsFau03N6BY3YdCRbLS0Y7XNd8817TdartXk6D4-sVbbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=rCK1FkI3j1wpe6gRv6zY7RDKmeXn8ZF05QFwIBrgf6r656GgErK0D74RGkOMix6YJwPyjmiHKR809OaJsZ-RRZEHvP7kOaY7tznYA_LO3Kl3omLTvzmLOx6v_RYnb6fk2K99sKrJAmRm4juOx4nZ61rfjYloosHrDZbaM-oJY27a-0lwZ7VK_Nqi_8zyVqWmYPIlT8OPrIeJhI8rCEM-3Nw2RiMqOifBB6fMpZQv94KAJYYA-WcOYPc6z0mV7NYSS_UHvY1mn7gX07L4xYj5rHb-01bkSrRNNka57kxJ0STkXyL3fGRG19FHTJP4EGzfLWUWhag-6zM4XpBF8EEoLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=rCK1FkI3j1wpe6gRv6zY7RDKmeXn8ZF05QFwIBrgf6r656GgErK0D74RGkOMix6YJwPyjmiHKR809OaJsZ-RRZEHvP7kOaY7tznYA_LO3Kl3omLTvzmLOx6v_RYnb6fk2K99sKrJAmRm4juOx4nZ61rfjYloosHrDZbaM-oJY27a-0lwZ7VK_Nqi_8zyVqWmYPIlT8OPrIeJhI8rCEM-3Nw2RiMqOifBB6fMpZQv94KAJYYA-WcOYPc6z0mV7NYSS_UHvY1mn7gX07L4xYj5rHb-01bkSrRNNka57kxJ0STkXyL3fGRG19FHTJP4EGzfLWUWhag-6zM4XpBF8EEoLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Sm-ysT1R6S2H-sokw5dh3D7pILqjX4sbs-2mTlO3wb1Gv2POUI9CB87Xhp4vNab6TkcAQkk0AFf1K5uBUjxO_e1FSTYP3Jt8aPYzFuyRhxaKabEsa8uFqdWuEP7yt4BGd1frCVX-RKhznhtnnVbn_mn24bAWI-tNYAkJ2KcW-M5PpX2Vh0sjVkqJMQPXx-5DTp4sfaT4a6h2zVW6T2uyJnPc9xGPGpTHPBqo-urIVqyiknuJ2t1zA-11ebM_VWiCaot408D-3PBqFWi1heV0n6LnKwdB_jkvUw7jwlMsIdAcACqxjsNQdoD1FjQS44s9o5a8EUsrtuekWbMIJLoG-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Sm-ysT1R6S2H-sokw5dh3D7pILqjX4sbs-2mTlO3wb1Gv2POUI9CB87Xhp4vNab6TkcAQkk0AFf1K5uBUjxO_e1FSTYP3Jt8aPYzFuyRhxaKabEsa8uFqdWuEP7yt4BGd1frCVX-RKhznhtnnVbn_mn24bAWI-tNYAkJ2KcW-M5PpX2Vh0sjVkqJMQPXx-5DTp4sfaT4a6h2zVW6T2uyJnPc9xGPGpTHPBqo-urIVqyiknuJ2t1zA-11ebM_VWiCaot408D-3PBqFWi1heV0n6LnKwdB_jkvUw7jwlMsIdAcACqxjsNQdoD1FjQS44s9o5a8EUsrtuekWbMIJLoG-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=IxV6CoDV1oDn6GGXgzwMksIXc4ZDC3BiyAPYeyHQTttbLnnwDd5T4qMQKGCaDGl_oZFCsaSmvJqUCVgnVT4qazkasV1yBMc-tSVzGNkdl1W4Zz7z6hMdIu6GoanQ7pGfoSS6BWxjwJpVD1DJL6T9poQpZ3x_s0WDwBwSEDbZ8wA7RQtg03F0KwBqPlrS8COcyvc6l_CvMnCU7AflADiFgMZhjX--ed_QN_Hm0XwTP4je-bz7PZVE7PLbELT7idvl9u5X5SAB1GOKcMpnj5R3msNmfL2sFH8NlSU-y7JA0C78xPCCqs_Fxq3E6KW7mVfBl6tgpUX_nfYpIjwURfAs4YbMPphZ0uACUrpo2_2rDc8GRsGiVLDOp-e86b41_xfWQ3e2bgJ4_COMK13iMgZMIICYZYdTlBqaxDKA1FmPVMkcVDjmccLU_z3nzJcGh7GC0QETV1jJm8kQs0fNn3TOQXoaJPnFPOfs-13pj0JftURaJzZ4LAvD43wcMYBqqxo9IzhXq2nzNrq40FZbBhbKK9UKNwbmaKcI8UxLgZlkNpcq0OP7_aTbciN7D_iEJfJu_EXy4sA1_FfNOYZV85N3Bpa4yXLjU-KcQi07GtIVX8rrqJkEX6tyNBZ2YSbg_gNTyfMebMsGAs4IvaaeoRDipFkTTNL5ymBYQm4ZCeatknk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=IxV6CoDV1oDn6GGXgzwMksIXc4ZDC3BiyAPYeyHQTttbLnnwDd5T4qMQKGCaDGl_oZFCsaSmvJqUCVgnVT4qazkasV1yBMc-tSVzGNkdl1W4Zz7z6hMdIu6GoanQ7pGfoSS6BWxjwJpVD1DJL6T9poQpZ3x_s0WDwBwSEDbZ8wA7RQtg03F0KwBqPlrS8COcyvc6l_CvMnCU7AflADiFgMZhjX--ed_QN_Hm0XwTP4je-bz7PZVE7PLbELT7idvl9u5X5SAB1GOKcMpnj5R3msNmfL2sFH8NlSU-y7JA0C78xPCCqs_Fxq3E6KW7mVfBl6tgpUX_nfYpIjwURfAs4YbMPphZ0uACUrpo2_2rDc8GRsGiVLDOp-e86b41_xfWQ3e2bgJ4_COMK13iMgZMIICYZYdTlBqaxDKA1FmPVMkcVDjmccLU_z3nzJcGh7GC0QETV1jJm8kQs0fNn3TOQXoaJPnFPOfs-13pj0JftURaJzZ4LAvD43wcMYBqqxo9IzhXq2nzNrq40FZbBhbKK9UKNwbmaKcI8UxLgZlkNpcq0OP7_aTbciN7D_iEJfJu_EXy4sA1_FfNOYZV85N3Bpa4yXLjU-KcQi07GtIVX8rrqJkEX6tyNBZ2YSbg_gNTyfMebMsGAs4IvaaeoRDipFkTTNL5ymBYQm4ZCeatknk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=NFupYUPQrlRJZpEZiAtUGUbcxKAm90tAaOg_pK9vu8qn6b65y-VC1nJbyhQM7NQ30vqora4nXek0Cnquo2eBunfORwiE_lkFbh4ZNNuzrsjEwOLHdnXuINgSNDN_bV4wZW2cZ7ndbHKFcZNQa0yDElN4zG6JCUHddQWIqliN_x3k2FVVFBUUYcjcjAVs-Rg-hZ6ahYC-RuRNTt3dlU5ir2cfZnW0AK9UWkHTsJatY-dR71Ssd159btkEpvy_f6ze9Xbhl-ewwdBjCMqEGV3ZXe9L-ifrkFw55keR89azGxFALtPIbFOi-hJMWvfCNO6KOo1GwxgArEMX3BCAFDOZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=NFupYUPQrlRJZpEZiAtUGUbcxKAm90tAaOg_pK9vu8qn6b65y-VC1nJbyhQM7NQ30vqora4nXek0Cnquo2eBunfORwiE_lkFbh4ZNNuzrsjEwOLHdnXuINgSNDN_bV4wZW2cZ7ndbHKFcZNQa0yDElN4zG6JCUHddQWIqliN_x3k2FVVFBUUYcjcjAVs-Rg-hZ6ahYC-RuRNTt3dlU5ir2cfZnW0AK9UWkHTsJatY-dR71Ssd159btkEpvy_f6ze9Xbhl-ewwdBjCMqEGV3ZXe9L-ifrkFw55keR89azGxFALtPIbFOi-hJMWvfCNO6KOo1GwxgArEMX3BCAFDOZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
