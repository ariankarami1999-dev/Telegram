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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyidfyl8IRbkqaAq1M9__Vaze3zlalljbwjKSwbppvPFGqddS6JjaZ1TY_wT7PNKBgb-Q4e7w2K66b1oXFfSLgQbrr6QfS43jg2zI4VQ9HCAxg8DgfHJF2o_Up9o145RpH1ma2lTF1OJs4GvBz7X_yLQf6PgoCiAHk1LEoHeK6zKfyJf67VLRZqDsYgWECdydR24lV3LZP2gUpU7ICU5h0fdl4xxGNUKAcZHLfSsxVdMRG5PILfWKDS0lSINB1sJp5mxiR8LuCClVDpp2IyEHwv15ssQO5srQ9BPvUPfloUicDo5_jWQDd6h2xmJVts5HMw1JbAaiCcUb7gE4GKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBe-n5-XJ7eEpm0cKUvwMvRDINe0BD0DiaVO7qXAVtU5JQPnjMF55kSoTeCVG9B40ZK4LngQK48YBQWpnLEsAUKkGYuyHye48OSgGANvIw9lgpROv11qeyhRGsPgTJLyOxcHl2sTkiPvFYEN3-cUoOrnoCq5TGnirMcRL5R0Aj-gy_w6HZpP3YHQGCJrNduyUIJja5tERIkAQMOZEXEm19z92boLeb01KtYkkMn7FU9lwfLD0vylaWHc0Ej6Y9OvQk9d8-4XXlu5rSZd2VYiMzPcdau-3CkPRVpNSz3rKESct80om2jiL3JoHznzBH6CXrRlkynmMyHkL5rFGoCUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtatJ_urYgV3jA8hrmHntL4B3BGxS4j3kxrrRZP2pcikItiOkE7JHvsLJUhoSq7miSz7FB-_4lmxJPz7GwTajk8sICAm0LX8NW0yqXD2vN0H0O22LwHolNw8xT8wb8lDyw1DVOmhgp5cXD-mTXYWGKC1F5gmDR9y7AQAK6KoUv_LV8sy5-2YJmvXlpouQJmWQXV9xxhIpFpVutdSo9C8W7hJ6ZBJtQ35lcp6tHDwttMqsPo6IN8F9MjeeXBumo6JEopmStVMPHGZmhXeKqyl7YSr57x7w-oeEPIEJ2AKKbVpfREM7LH17c38A0KtBu0JE8_NTGqWPHe9CRMJXU8iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhNQxvXJGp96qQSWVsHq_JCN2Sqi59dUcD787YkK9b0u9usp5v9RiRN7KCa8vQDHYdwfSirN5GBN0f-GAk9U8XMZVFa52hu0Z_XcsAgpBhfeYEoz0jcm0NpxOpfwvhMCVSqRLsyTfcUbySsCKffZp2PlWCNqT7ZnWV4955FubEBgG9-QdT3o2Uz8T3dCZ47U7p_mZ5zQ97j7kG7K-DVPMelDc5qrNuxkMjY0Zd-632wq_HRCoplE4-XdvaQZT4vq4ZuluDyEzW6oAx4ZCn5w3dEKTVEFXrAVtNbCujkVIVF6SI-Gzujww2YiF8lrHVsTvpKMb4-6EhWrakY8YkFVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P32dGYapydeF8T0wd63U16X9S5pQz-lzDzeDEJZq6dEefPDS9WMoLsqIrpUuS5y2VESmyPJcKQ1_9LtsJf0HE8mH_HRs2U6kEYVFLAqROU49jzXs9RCfujqedTr7F62EZMUdwp5d6R_YvC91TeAs1RAikaw8gCyh2KFn-Psn1E7hQMuRygYMII4HhfDE6t58yJ7eMeE8qXLZ8S_0DHunpvclrAweqj6PjMA4H1W8wnPGYgjNr7hwfi0ryZrcWtAZHNUPCQLvXvTD9dZaHTXZpYq2Y8gKIqCaIb1O6aH0VR_NgwLKR8MPTTfOMA6mz0XBP8dAyKjLvWVKxKgQFjBWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugwUAkUHUUU5yWzmKNM8BbxahtiWisAdQaGmEcwxZYzEAMUWr0wHbLadpwCB8PF4sjJ7zP9dsmju6YZwf5RpYZofGOReNBDww1EZje6HHf8IQWyNbh7pTpVPRAEaTIg6igoyOT3J4u6pf4PHfmru4G8yRSRiHdZADRNwnEL2cOzoyt5jO86LShTOjSXS4-AjzRH7k4-TSuKml_n9ex52YVORwGVjFDYMe2kl9dmqAahhNP_zOkKkw7l6c1Gaz3y2b0TBvnvu5SsnwHwFfhitTqG2yga4ulmOZjOHa-MuhUiz0ykjmzGxoOu_SzE0yGi5NgO-mjrJhSm2jykGsBXGMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8Lwlw86tiMaV4nz7MSirlciIiUe-I8DTKmIaVWWR2xgFb_6Lo_1Eb9-W76Fm3xlQrEL0PliWmou7YsOrr9YMNscG-WQg-BF7JGlnuc-vKtpAL_Ba80ju5Y7KynYV5uRNmewLOW93SXbTYuTbcXKktwq2Hv3CbevPrZw9QVENKqaX5WVY570vwPEh_1zZaND3CWREv8NvXnJuA523YbHCJ27eEjASPVbMU_RNySFs_EEsC6Wakhdl_6s2QVqme3Nx3HffnvJv_4NhC1V_ykFQc8aabPTHJbSCgHlLdJmChtzImYXAISQLppiwEKlyizqs5E3PE2ZnDCUe-XUIqvXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=n-9PYxSEIBQtw0DbB6puhTfg9LZlI-RshyEsDY1cyQTMOfJbDOpxAAPPSkf2VrONTLwFLo7TP8g9Y2LgV3rXwR0EbY4netKXIG9ZPQxij10dFkn1k-LhLLamzCfkiRILjFy4YcRnrSY0RnDCDvvVt4lkC9LU0jg0ydxZgr61a4zP2U3jGpWIXw5e7ez-RvQOuSN6-spY7IQLkLyAoYGbRugecvSp6EeVWxdUxd_Zn095aQ0OyWWeI3Xp0q4XxrI4tVm16VXisYm3qLYb0hwcK5Jn-2H7LdQGRfldcz-8lDWr1XCbyWAiAT_QuvR9SY-N0F7urvFU0K9wn0yfjtn8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=n-9PYxSEIBQtw0DbB6puhTfg9LZlI-RshyEsDY1cyQTMOfJbDOpxAAPPSkf2VrONTLwFLo7TP8g9Y2LgV3rXwR0EbY4netKXIG9ZPQxij10dFkn1k-LhLLamzCfkiRILjFy4YcRnrSY0RnDCDvvVt4lkC9LU0jg0ydxZgr61a4zP2U3jGpWIXw5e7ez-RvQOuSN6-spY7IQLkLyAoYGbRugecvSp6EeVWxdUxd_Zn095aQ0OyWWeI3Xp0q4XxrI4tVm16VXisYm3qLYb0hwcK5Jn-2H7LdQGRfldcz-8lDWr1XCbyWAiAT_QuvR9SY-N0F7urvFU0K9wn0yfjtn8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-mlSunkSzP8WE_Q-c1CP6LOuQchWwkByISaCRUVMCheE6Uabr15Z0QCxN9G8IIVIYY2yMiouyydyH6F42BSLOrbuTiW2j11L-4CBGrq6HjmkLWt08uEflNWok11kxN_5oOLo83yaEU1foDib1fGQVMSyl6MXqZnHL7oRWrd4ZDdzZEYuIKEKBZR4V-9t-J94fh9bRVjbW1LMxlny2jSmIJ-argRLWwz3KtYSAd1WfQS4GudalEeyZjUSlr0Qu_5Lxy49ftRUncnNgXsVn4FH5AqYTAKh5mGMWE7PV7kvOhxERdOCqQ7n9sOwVLPLIZNI0-BUhYYwGfvyoaX_wkO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=Zow8_RFjh5WxdmcMfmXgys79nBc71vh1_FzwOGmhcis-tNmgaYEF_4G4r6PpsVwhOvmny_Gi38I6DHX4gjVEWQh2oqpzFuvgPGWERsW1nh-Wyhd2Ah2k3ssUAvrDfvtQhngWPqZEcJ2uqiIrsJbzKaKa9lMcU7ICA_tNaMrDg3mgu2p9q_xZgoKhirP9I_DIViYHPwHOEaMF-wlqsdfY3Ts4TISlPTn4vc84n1XjYj5K3ySK9pFqMwxWDFyhpUS9ZhlmJdyDpmbU2XVzQiFY78qvVqKDCEi9miW3mZDl0bYfzn1ecYTqifOt4YijflW5ZRSW45rQHqVoLEWDNrJ4hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=Zow8_RFjh5WxdmcMfmXgys79nBc71vh1_FzwOGmhcis-tNmgaYEF_4G4r6PpsVwhOvmny_Gi38I6DHX4gjVEWQh2oqpzFuvgPGWERsW1nh-Wyhd2Ah2k3ssUAvrDfvtQhngWPqZEcJ2uqiIrsJbzKaKa9lMcU7ICA_tNaMrDg3mgu2p9q_xZgoKhirP9I_DIViYHPwHOEaMF-wlqsdfY3Ts4TISlPTn4vc84n1XjYj5K3ySK9pFqMwxWDFyhpUS9ZhlmJdyDpmbU2XVzQiFY78qvVqKDCEi9miW3mZDl0bYfzn1ecYTqifOt4YijflW5ZRSW45rQHqVoLEWDNrJ4hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=ijtW_GnMLUYPRxbkicH8Pr6vbWTddpLo9vecE7kn9l46or0c521KE325SLvvRo-1yPowbCW4Zo1BroEqFNPihmUfW2MMOY4xez0UcYudSP6-em89vgKSGeYJrY6KkSU8yzWqmu_VMRwred4aj_-Qn6_hkHBsjFiwBivkFk2PmH4i-dG5QYlf5zRJZoLpj3B8jjYPkevkLvbm2EtnQoESTg4oZHA_1W3kpZDqLP9Dz3sECLR3O7ZMHzcesqCjpIJPdxDW-dVJ3dz2JwXPActCms8psKhbMA8hhe-kULPLXxbtS1XH7mjgLd2ElF54tswBur0YE2pe-uJVxbCxGWU-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=ijtW_GnMLUYPRxbkicH8Pr6vbWTddpLo9vecE7kn9l46or0c521KE325SLvvRo-1yPowbCW4Zo1BroEqFNPihmUfW2MMOY4xez0UcYudSP6-em89vgKSGeYJrY6KkSU8yzWqmu_VMRwred4aj_-Qn6_hkHBsjFiwBivkFk2PmH4i-dG5QYlf5zRJZoLpj3B8jjYPkevkLvbm2EtnQoESTg4oZHA_1W3kpZDqLP9Dz3sECLR3O7ZMHzcesqCjpIJPdxDW-dVJ3dz2JwXPActCms8psKhbMA8hhe-kULPLXxbtS1XH7mjgLd2ElF54tswBur0YE2pe-uJVxbCxGWU-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OtLyyBRI0XhzHHEsqRWS62YWzHuAwgo7GoBIAfObEO9hy6jRaKZuh3W_j7JpYYrHOKio4H8gjCH8UBc-evvit_Tlg3to95l3VvQm3ctEo7tQ_U7JmFSnSpdlAgJtKFkm1pGu1Vc_L47OuLengHuX_W1isfCuHpptJRTs4bpXn96CF3c_r2CrTohUrPnV7cs_z8Q6M4l21C54Y7MgF2ZFszuL69z0qqRZD1b3Hwnk5aCA-3xirLll0Aoko-2bb-XTojXVKtDdrViT9CM9zTTmueAF-6s7Z6m0txkfJEXxqvOwFYbJH-SKmmgG-_o8RAxzwtdjmPaQhJQGUHPDYvv8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Y41qcK_RrANyuZS353JkCwyX6AhWy5teXmjU7zmgCzxtXhD0qwsb3aQk71jEIsecF-Kfed6tQ1ga7FAdinloG1IGnoZugoE-ZGSwgdwEgJOUX8G6rrSnvaRHJQvjaqxFVfKBQ9gQ3PGEmbIgVAu0zMNUAIasMx8K8aQr5W2N10rBpaWVhe_bM0DagjOCgXhJJ-H5A95qadHkYy7L89LD4aLMS3wmE9bzztbcFsBPMLMJNwXQoDJpJmSnJw401u1PtakUY-wTtygbS7bhP70rl-FY4GiCmmfAX7Z2zxn6LpJJlgtlCRRqsOJW_gcNpLeSPOQ8vHnciZ3r342f2kkXVIeXDAonJNL5_4-FItrzJRbSbJvKbiSIraY_6ibt_vS8hDzRpxmg3_t6vC-bNhf0jt9w8zfHAb8EMDBDMHtHJOoZfErMWAhzQpR48YL5H2u5l-vK1cNenRcTuChIsMPii_9oQQL05LMfiAuIfsPbnWxj1s2lwm9FLibYimh8XgmVglmnENF_egvpt6r6_37AFaa-ozZJ_h-9CTPunKKRJWQVDzebvSrU3Z9CcXzdxSVaQRiSDAyp4xcFMWAHGoUyMKCa-tnBs6EitaQH0IRcqpbnrsEp38heVBsi0LeKiSpfCfwq10qdZi3DtZtCcExqKK9ehyfJm9jsp_C3rzWtiyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Y41qcK_RrANyuZS353JkCwyX6AhWy5teXmjU7zmgCzxtXhD0qwsb3aQk71jEIsecF-Kfed6tQ1ga7FAdinloG1IGnoZugoE-ZGSwgdwEgJOUX8G6rrSnvaRHJQvjaqxFVfKBQ9gQ3PGEmbIgVAu0zMNUAIasMx8K8aQr5W2N10rBpaWVhe_bM0DagjOCgXhJJ-H5A95qadHkYy7L89LD4aLMS3wmE9bzztbcFsBPMLMJNwXQoDJpJmSnJw401u1PtakUY-wTtygbS7bhP70rl-FY4GiCmmfAX7Z2zxn6LpJJlgtlCRRqsOJW_gcNpLeSPOQ8vHnciZ3r342f2kkXVIeXDAonJNL5_4-FItrzJRbSbJvKbiSIraY_6ibt_vS8hDzRpxmg3_t6vC-bNhf0jt9w8zfHAb8EMDBDMHtHJOoZfErMWAhzQpR48YL5H2u5l-vK1cNenRcTuChIsMPii_9oQQL05LMfiAuIfsPbnWxj1s2lwm9FLibYimh8XgmVglmnENF_egvpt6r6_37AFaa-ozZJ_h-9CTPunKKRJWQVDzebvSrU3Z9CcXzdxSVaQRiSDAyp4xcFMWAHGoUyMKCa-tnBs6EitaQH0IRcqpbnrsEp38heVBsi0LeKiSpfCfwq10qdZi3DtZtCcExqKK9ehyfJm9jsp_C3rzWtiyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=DpSvzRz4U_1KdXIfOcCJjgLPbiQVKSdbCaMJGqtNZvowNkzEjMvcJhAdY6LRkit5wtBNPbU-eeS4sbuUaNM5LJ4axTWP8CCriiynuX-yAiXs3X3IcutrQE0G0V_b4IIxxWnI3OSuj3uywzaQHkfVx2umN6fbpS9-HRsTkAnAMwev20dBUiLv8JsEvH4KOl5xqMFG4KEGWcndQt5Q1vNa6eKGKoXjaYLoYQi7mmT9nivAUr3EttWMCIpGodckzMSDZTsFIy14qRfxwdu5VE6ONDpAKikcES6LjeQp90gAiqQCxP-XiIcF4YKzAl1bCp3P-iazBlTElCwle4Y7Rv3fMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=DpSvzRz4U_1KdXIfOcCJjgLPbiQVKSdbCaMJGqtNZvowNkzEjMvcJhAdY6LRkit5wtBNPbU-eeS4sbuUaNM5LJ4axTWP8CCriiynuX-yAiXs3X3IcutrQE0G0V_b4IIxxWnI3OSuj3uywzaQHkfVx2umN6fbpS9-HRsTkAnAMwev20dBUiLv8JsEvH4KOl5xqMFG4KEGWcndQt5Q1vNa6eKGKoXjaYLoYQi7mmT9nivAUr3EttWMCIpGodckzMSDZTsFIy14qRfxwdu5VE6ONDpAKikcES6LjeQp90gAiqQCxP-XiIcF4YKzAl1bCp3P-iazBlTElCwle4Y7Rv3fMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=J6XP4gyauyKFUtTeLwt_EYmnDWSFwJHZ9WL-1mgLqY_K_w_rJEvmsMOwH2zEwADYH7jiHsL0v6s05ohxqfvgzGNARDX4l8wkiiecSI4jCIPdUddhlxF0Bs1SlPVkG9OCiTlJxket409RLKiqzukRI34HMmUS1cBCB1VQifQrA_4Zb9uLFfbQSCay8rPmppQ3Kfd9N1TsXdWO_tPvRVjaRts9RK1tt6P6DXFRT3UVHrh5UARBt0rFWtoJZTE_HqR7nQwNTCvZA8HJ0gCsJ2ozfPYk263Afht6-V-1AgTGrrHKXEoRcOIjz3A507hL8FN2ZZ3A5LIj8Ih9HjXn3jr6NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=J6XP4gyauyKFUtTeLwt_EYmnDWSFwJHZ9WL-1mgLqY_K_w_rJEvmsMOwH2zEwADYH7jiHsL0v6s05ohxqfvgzGNARDX4l8wkiiecSI4jCIPdUddhlxF0Bs1SlPVkG9OCiTlJxket409RLKiqzukRI34HMmUS1cBCB1VQifQrA_4Zb9uLFfbQSCay8rPmppQ3Kfd9N1TsXdWO_tPvRVjaRts9RK1tt6P6DXFRT3UVHrh5UARBt0rFWtoJZTE_HqR7nQwNTCvZA8HJ0gCsJ2ozfPYk263Afht6-V-1AgTGrrHKXEoRcOIjz3A507hL8FN2ZZ3A5LIj8Ih9HjXn3jr6NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=q-l38z5iOiGe6y9Fhu4iCKx4E2kRkZDMUwTuzHrd_Bm-8D99GZPTbH5ARFl4HgzabyVX1ClboITTo8_sbzAj3I8pp1dYE5SjwMi2XnvtFYc6s-B0zn0g2zTorAf-eTa6vMmkTKV1fE-S6fhBA3HJSbxlHKzygV6PON3sHdl_nw9UyD33hvzzJBxLoRjpcw34zQJqNOp7qEi4VME5oRmd6JroeS9SrESA0UkXwIlM-jbhpcmvOuzlPaZL4AmyfkaJOeju9drA7hyLAFtYC2P38yXmUACRn2sz9eKFTRGDXB6uR-iYfiayZI2QhZyP7I7wX1mFzBflTkGWXWc12YGHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=q-l38z5iOiGe6y9Fhu4iCKx4E2kRkZDMUwTuzHrd_Bm-8D99GZPTbH5ARFl4HgzabyVX1ClboITTo8_sbzAj3I8pp1dYE5SjwMi2XnvtFYc6s-B0zn0g2zTorAf-eTa6vMmkTKV1fE-S6fhBA3HJSbxlHKzygV6PON3sHdl_nw9UyD33hvzzJBxLoRjpcw34zQJqNOp7qEi4VME5oRmd6JroeS9SrESA0UkXwIlM-jbhpcmvOuzlPaZL4AmyfkaJOeju9drA7hyLAFtYC2P38yXmUACRn2sz9eKFTRGDXB6uR-iYfiayZI2QhZyP7I7wX1mFzBflTkGWXWc12YGHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXpdSj-R0MlH7fy_S6nq_6ZvjNE9Qt-X30Crf0J4ziHwZJFNSiJ7wMRKO93FZP7U7r7N9-Hmvftuw7QL4FB2Tkzx9zvOMWJaGofETFWgFt_Ak4fDgdDOJE7l-0hFjzdzRtNDwslBmjTFnHLF6tpyjbgnhk4lspGXaZju7EpoxubAV-3aUSPpvslqN6eHmaiqo0TY9CzcfSW8SLLZbMXNThNkYZAoyRSyxVhZNE_oBoxofRQpkL47JtgF2mFRS1U1qLKrU-OvJHNnFzyizZUtCEidPtHCoo6JsnLUJJBpfTJruU-A3wubTTbHWJN5lcu5wg_D3bl1MAggYo63SVA8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfaQN4VgytABp_P7vl3j1U6aBG7YYkIZcVa7S16SXMBwHPOCYH0ymH7csfKFgyjwpXqPpoJGcD7_uppCGh3Za9e10xuv9CXKvOyM14encHwGnGYnP6dM2kCsBPY07ajem7whPNHfwkkR7A0PZtxx6HNTv6pWyZvzf4q60uPot1udc25o-Mc5yY10hmr-Bg0bvnPg4Oc_N5vW1oVyrIQYDOQZB-joEOCGC7WD-FNbaAn58FuNsiTfnmhnloYYgkzMQ61KbbZ8uAIODhaNAMKpVvCeLzFzHLn_fvFcndt-T-H-NF2k15RqPOa5FjI_zjJnm2ksLCgSl9xNu4nunfJPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6FSTNAJpBTCyjeOUuAePLoYyaPdwUmylSfFStdCTJYOuTRbZWmSCWvcd89UuimMDazAKSMFm3f8zFJlZg0Nwba_RJYf4lRca97MW2tQnRU6mI_Hc2m7TDEglSwWKpeR0Zs7kN5NBz_JFNz_MjPXtshYu1SF1SwqioNa0Ioo6wNQluO6ViQg5v0U3kYwJLy0G5X-dsIvDzj4HESHMa4hlNvuF-1wKw8rS8QxiSENq7_giW9UlsQywgGtu-b7NcZSbdTpQzCl1Q10YdDuYob51u8XQoOVpp1WMaLher8fsJtXekcnUtWCu6ipPsL52Rm42NdyPrD6lXaUZxA1Gl2Fbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmhRxBN1CcmIaYHQr0jHwJ3bHtFnHabXCq42bN2z-MnP414WW52QOeia-kLFwrqRsnq8NjjEW-KIAjD4sVXgOgChgTGRgPzbKxLVpJDx4ODsz2RMACcgoOPgtQVv1s0tKm05Qf3enCVpMukQn6fcJITHipg9-SHvDAI0ctWkLv35IHZA_B7hqRdlQzRIQmYst2HCcDDprxfqkES56fRwYyntwIVDFWYdWSMrG1TG3dj0QEnu9Fcq2vy62zpUjOdx3Ed4cKWIzW9og5_7o9Jfg1IlC8u44ep_vFUbjyAoITzMQP1O7lGHveDZ1EztUihnOPGRrhOjs7or7x4uBNYrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZIXV0F_fGpmHt06D9ibefe8qs3_Zse7MP8dxctM_fHQt8DlyhTDp-YguUclaZaDkzA08B1VcY2xTevMsT3Uh7itYyTeAuK_PjLhryzoPXUSJrKLlc9016sQG-zLczXOFrlKjth8XneMOoOTKEGpLu77TW829cprwgVjyxQD2n37X0NJAJsHG5jYMCaBV3RdnuLw5DaVKbz06aYStww3wuqtAm01_1UIUO5vC4IxZ5hpPD0LIP2rsvssoir5t1TJGlXRNtaB_HcP9RLAEpiptYADPhsL2VynVypdPZRU3coptD4mBtp2FfkhArZm4EUefX11-CmpvXnoDJ8HCez63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHdOVyuiVCpG1Fw18yBH_qX7ic-LlYifyHbJlcEbygLaQW4ySm0tkZJRmnqTuYfrjQMpQeljdIpk5dY_dsHrOY3IyqdXeHyKViB3vaZRvl9OSAOvrGk60czXV1-KctXx2RnxVePCto5ijUBhPp4rS9y1LhQ8deadtmwCVDGgAuqxJfJXKERVLKnsTMKNf9xvKnPvuYI3oxM0TWF-VGH7gZAprw28zGlScA6UW0DBLqeouzlMXzVI7Ukxn9ZOiHpkyRsn0Grvn0HZxZT6YQp0zZDQVWEr-C6LUpalrbaItHYx4mnR0wa1g0oAzNW9nmMBAxYAck--hAB0Zd5eIvvIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=t-hbKvjVIUEG7asVll_6rqu-XzpqqfYzGFbiwjobBu-rgw8PvfEBZk4r13kTiNIuqVL9heBvSr0mTzXljzzf0wKrImJNnlj-l8veDez46ZaeSEkGP39YJl1-tYS93LY9jQfPx8fNfWlbVVg3W8kN9I4U7b7bFb6DKjiufg1z7xNgmxQktY2saabGE_p9OM1MsWWuN4sAzokhUEiV8a4o14-NpWBZVpi44n-nH0tE0FMzkjJLunebOscbcFuLtRJOwzYp7lmcFxYO92yizm6wpi57JthiCMsJe3y2t8XsUce-NyXwrwCFBIQ-6LQftGaFGi97FrFDGwAzIzXbVDIArQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=t-hbKvjVIUEG7asVll_6rqu-XzpqqfYzGFbiwjobBu-rgw8PvfEBZk4r13kTiNIuqVL9heBvSr0mTzXljzzf0wKrImJNnlj-l8veDez46ZaeSEkGP39YJl1-tYS93LY9jQfPx8fNfWlbVVg3W8kN9I4U7b7bFb6DKjiufg1z7xNgmxQktY2saabGE_p9OM1MsWWuN4sAzokhUEiV8a4o14-NpWBZVpi44n-nH0tE0FMzkjJLunebOscbcFuLtRJOwzYp7lmcFxYO92yizm6wpi57JthiCMsJe3y2t8XsUce-NyXwrwCFBIQ-6LQftGaFGi97FrFDGwAzIzXbVDIArQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/czFNBTqVUsoQQESLr0sjEC0W0jLnw-dethfzSFu2xFEgWPjbDH2b4ta-Tbzm1VgCiUKx1cLo1rmm-JARiCoZYbDGXP3BWym8S-NJjTB_tt_Qh36Wni2usa0nznEojFsas1Y1UCWC0UFQoGKIfzeAdf7Z7mJxPUoH5YgDX6SWdBwmZIUo_U__Xb3Ej1tvp1Dl0zl8TMYS5RYpehOQrFcmfZ-PuNOSCJ9zb3M_hpHkn_ojWMj0OLzZa6_yB5PWPIaXT8MzHq18KtCLjK4Omz38hVDnz89JC6iAXEoszhYPefz_1iC1QMxeYZuvEhbsyQI1eGK4WzyI8B-PiEBqoFDwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=UvgJP7-Y-bT99lnOvkWhfjhwYLTGL8DZBzUKAM9MZC1LlQy9N6wa460tAm9ASdH_HsCtoFs4ov6ne2aT6KkIB3oSgNspmMROs7y_JzW4ZS4_mBgh8eaYdy_PrlUS1m_eZgQ6gWqrm9nbHrgD48hcLxypXHiEXxgcyx_hvMqUy-h93tWqP_r8ABV0zVLuq9hUmiwGHPB6aUXHCdV27pnOMqKiv_Muj2Dlo77Q8W28CvGZvi7m14CZCZ4OTmP10UR7PZrVWBfSFpdxOZHgf51kpewjfpNJR0E96JpwyuKv1MgR1oj6SiTuvMJG7XJc-LEhJuvt8n06Vr32ptcw3_0bJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=UvgJP7-Y-bT99lnOvkWhfjhwYLTGL8DZBzUKAM9MZC1LlQy9N6wa460tAm9ASdH_HsCtoFs4ov6ne2aT6KkIB3oSgNspmMROs7y_JzW4ZS4_mBgh8eaYdy_PrlUS1m_eZgQ6gWqrm9nbHrgD48hcLxypXHiEXxgcyx_hvMqUy-h93tWqP_r8ABV0zVLuq9hUmiwGHPB6aUXHCdV27pnOMqKiv_Muj2Dlo77Q8W28CvGZvi7m14CZCZ4OTmP10UR7PZrVWBfSFpdxOZHgf51kpewjfpNJR0E96JpwyuKv1MgR1oj6SiTuvMJG7XJc-LEhJuvt8n06Vr32ptcw3_0bJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=DZeCtim1Im80nd3l8KjwKu5Kbk6VJzPi7cf1bZxBREnUSBp1aAnWqNcFQdNJlVm2SQncxAKkGOcwqtO-pZPW0o2fhyihXghNpkwy23GXTkGpgBcqyULLUPZe6dLuKV94mPjxJrl0_VJJ3uUlA9t2-xXAwQfSzOqBYk2P_ILuUQB6ym6VvmtweIgjpJ5dwaTTZY8ZZoWB7faLM1IhD5BrvIrqNfc4-GAmxQ_yjS6tgK_HpyMQiclmIdDogBfvn77Kkj932OQvXKDIvUZ1nyzR9W73NWRkRy7P9w69-lMvqJtoysbTvSRvpQnUwTAvNaFl25Ngg5gTSZg9_DwEVgmxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=DZeCtim1Im80nd3l8KjwKu5Kbk6VJzPi7cf1bZxBREnUSBp1aAnWqNcFQdNJlVm2SQncxAKkGOcwqtO-pZPW0o2fhyihXghNpkwy23GXTkGpgBcqyULLUPZe6dLuKV94mPjxJrl0_VJJ3uUlA9t2-xXAwQfSzOqBYk2P_ILuUQB6ym6VvmtweIgjpJ5dwaTTZY8ZZoWB7faLM1IhD5BrvIrqNfc4-GAmxQ_yjS6tgK_HpyMQiclmIdDogBfvn77Kkj932OQvXKDIvUZ1nyzR9W73NWRkRy7P9w69-lMvqJtoysbTvSRvpQnUwTAvNaFl25Ngg5gTSZg9_DwEVgmxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=gCaafFIq7aTvZqyCxbNSPJWdoM8zAZ9lJKrHPOwYw7HKZ7RY-mjOT4s6Hz958wng_iyM1BtnX8Fk8XlBn7jY3x0T74-wtBJOZwSJaTFIBXAE2k7AVNd2g0kOJSzPbo5seHzJ1Ki_wkvGn2hkF-v7GWYU7ntQR7NnYwQA6UVcrfnCRAz98NASlC-tQBtV8P5KRqaqstg6c3LwoCdRa_HeJIX8gnwYBtePrB7oSTpsh0Ylm6kbPiHn0HWvn6iZGrbQ1SKYFlnSeTsOSTL7L-40amyy6KwCu4shwpfZ_rWTalFTvPm1jUE_u2cw2_6Mj7NARen1yQA2VtPdOrIe3qMQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=gCaafFIq7aTvZqyCxbNSPJWdoM8zAZ9lJKrHPOwYw7HKZ7RY-mjOT4s6Hz958wng_iyM1BtnX8Fk8XlBn7jY3x0T74-wtBJOZwSJaTFIBXAE2k7AVNd2g0kOJSzPbo5seHzJ1Ki_wkvGn2hkF-v7GWYU7ntQR7NnYwQA6UVcrfnCRAz98NASlC-tQBtV8P5KRqaqstg6c3LwoCdRa_HeJIX8gnwYBtePrB7oSTpsh0Ylm6kbPiHn0HWvn6iZGrbQ1SKYFlnSeTsOSTL7L-40amyy6KwCu4shwpfZ_rWTalFTvPm1jUE_u2cw2_6Mj7NARen1yQA2VtPdOrIe3qMQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbSo21M5OZXn6mYOP9p_EksbseM0c4kAxAatl2FMgRZcbCVB7PsEaMiCRc1K5mTgZlhHzwwf1cRtbYQKUjg-WJHOTD31ELp-JH48dFByQ5S_d8iTpRuQPEf18dzYuQRzx8DR_JW90MEZkSbXLtPB1GyMZlwTnnBnr52G1LOqCY4TiYa_KD_aVBtak5PKxkaDltICSZ9T21ZArYsxZrzzNmPCEPvk2Lfmj-B4caSpDs7o3IZJNiDfFOWnUhON2NgB4FPW8eddRL1M-jPTMuWy8swM_7r8CPW33SnO3ukHbdRD4WRCCwsI1A9IZikdin6dY1BBL4FsSmrZYY8wEyUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=VIU5U9NfxF4EXEEewAAjRVHK-cYase03f-vvNZDY8r5dgD9NjdOrUqHSzUzrqcqreENg9j72GmrGeW_4ve1x-pdT7TE3s2Qmd6VWkxi3NJUDZ11JsVBlKE6Uq9dvCLoufoQo2FpI42sVGLBPaJII6hViTg2hTPFXUubMH1iTO70arP_u6VbjKxQPQiI7-hJ-zpQpUVQoS9A5rUu7Vz4lG5mAXWq0ZaLsji6PdltFHVbgFh0zoMZYGZq-wt7sOYGmh2-vI35x_JpTHskOJwOU0IZRX6L4CxV2WNiBbBZZOXxWCC1W-MCZUEgiCG53gQTS8j9x_VZ6SsnGZHE7_UdzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=VIU5U9NfxF4EXEEewAAjRVHK-cYase03f-vvNZDY8r5dgD9NjdOrUqHSzUzrqcqreENg9j72GmrGeW_4ve1x-pdT7TE3s2Qmd6VWkxi3NJUDZ11JsVBlKE6Uq9dvCLoufoQo2FpI42sVGLBPaJII6hViTg2hTPFXUubMH1iTO70arP_u6VbjKxQPQiI7-hJ-zpQpUVQoS9A5rUu7Vz4lG5mAXWq0ZaLsji6PdltFHVbgFh0zoMZYGZq-wt7sOYGmh2-vI35x_JpTHskOJwOU0IZRX6L4CxV2WNiBbBZZOXxWCC1W-MCZUEgiCG53gQTS8j9x_VZ6SsnGZHE7_UdzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=J-IoGGWIMOl_TYRTNfEYGIxWIz1GECS3WOcFjER_8NvW_X6JvA7EY9Jn-Irpb3Up-I8JcvxnVRl7b-qdGPJ4QKo0dOijYTDAr5yjMXtu7ArpY1cGZJN2smg3Td-bTgflx8rbelFZeONZFtRxQbfwXGHCaiZ4-tHw3eytRuJE6xc9C074LmQoU0e9cYW7tghEKdOGkMYiKOVXcZm1qFlK0bQLQ0M0UW_lcpFsMLHw5zxsEiUpJziFqLl20Gp3XKHZYhyAdq4lkMSPUrm42om4wxyw7pXDfqs6XAx_RmACRLn_Oq0nvG7OrX73hiUdr98ZSPBZEc0mX-hekBXyy5G-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=J-IoGGWIMOl_TYRTNfEYGIxWIz1GECS3WOcFjER_8NvW_X6JvA7EY9Jn-Irpb3Up-I8JcvxnVRl7b-qdGPJ4QKo0dOijYTDAr5yjMXtu7ArpY1cGZJN2smg3Td-bTgflx8rbelFZeONZFtRxQbfwXGHCaiZ4-tHw3eytRuJE6xc9C074LmQoU0e9cYW7tghEKdOGkMYiKOVXcZm1qFlK0bQLQ0M0UW_lcpFsMLHw5zxsEiUpJziFqLl20Gp3XKHZYhyAdq4lkMSPUrm42om4wxyw7pXDfqs6XAx_RmACRLn_Oq0nvG7OrX73hiUdr98ZSPBZEc0mX-hekBXyy5G-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=oVKAcAkYxstujPMUbWszEAxEfLc5ogoHF1hGu3X8oZfrZ8jw5WOjohLCNWF2Y_e3vMf2ZLy1n3F1dK9hz6eiQqr_RPWheFrguLCCDEg0NT4hcQFcXAiSe-D1AG3bkuaoXsU-FEDHlqU-3uvmj1lrPeFu2NwDLXsgkar0UOUYcfPvUfVfVleSs3IXGnVL7_XFo61GFJFEUCtJJawzkryn-OcRA7nw2XG9WGkpQ_ppLhZYWpLXn7p5rQOvngxol3HegPNpUdZwHKotRlftiLbcqvaiv7uP7gErLL-ZmUF8R8EGp1nREj1zX36qLIkXQwwR6ZGjPYtypvPne2qBqsNAiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=oVKAcAkYxstujPMUbWszEAxEfLc5ogoHF1hGu3X8oZfrZ8jw5WOjohLCNWF2Y_e3vMf2ZLy1n3F1dK9hz6eiQqr_RPWheFrguLCCDEg0NT4hcQFcXAiSe-D1AG3bkuaoXsU-FEDHlqU-3uvmj1lrPeFu2NwDLXsgkar0UOUYcfPvUfVfVleSs3IXGnVL7_XFo61GFJFEUCtJJawzkryn-OcRA7nw2XG9WGkpQ_ppLhZYWpLXn7p5rQOvngxol3HegPNpUdZwHKotRlftiLbcqvaiv7uP7gErLL-ZmUF8R8EGp1nREj1zX36qLIkXQwwR6ZGjPYtypvPne2qBqsNAiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpbuzuGxPaWkbU2KnN4rzX0UWq_XVvMwuN81iSQRHcdm9ao3LZIqske3TVibbmLaBZt6vPFxf2zQjrfVDCTQdd5NR04YkyV_d0w3OQOGASsmnt5l3oGTYv996pn48QI0pDpZ9qleZoLfH_Kg5sryGQ4h9EtdL-RUGtTXHwmtQtbWAHAWhYFxndqhWacpUJses4VA8_6C5d43wj33g4DDMhfU6NNAnltu4SqD4XoyntgKq0WBI45j8JhK5SI7w42mp_n3NNT6j0dGJMv9H3ViKBN5L9itpkihXjeQviXQA8UCreRjuN3y8VifGZJUgSVoMajVG1_hV25Jv9yZFKMvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtoImiNJ2YHus6svGIZ6dXY1R-UcKiWRVCiFgDI0lJHajhI5aqlxfIgpWk4xwalAnprTsx58oOZ1R1vtYSR_d_yNDYjiPW1lL4cZiqIjdJIk0HQJfk5FplkCVqGGj5b1SRS3gtIgUsmK4_f6b5gwWFCM4E21yV56CQMl8-xlIb2ZIETrrnojvPyr3lCxqDmjGBtYofCb_FqJ38uxRAGou67cMl0Mz-FTAV0vdNMJWa59qhAdK_D322rwMMb6r8vW9Utu9D9Lh-i6MgEV6nrMb178nM_D_odov97LCexu5sEP_i-vYH9KKDpqxT4G7-nVBST7VX7TghLVSeL3-LKpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=GrYt4W62k2y4w3LyScVP91Yp7u7V4Hr2K1HPaMRwtM31d3ehrIXs6abj9J3JYzCc4upsd9LzQyvmE-EYVzE-ewbcENr4Trf3UefA1EpwCC8ttqA-rfzgqSJqrjrYuJD2bADJ04ewuv9xkges2j84gSHa99zQ-k5Adr64akAcHFxjAQUE64eEbszYeaUw2GHmQ7mzRCFxjauk2SgPSf4GfneRiyTEoTbb84oldd0nxOD_Hy-a79ijYkgjF7Bq8WDbZxS7J449aGUuj-fy_fAqCcGn76o958P4TrAE3upkxN1e1YZsKof26GCecNfSXWG-VXn-Jxj6UH7F6WBaw_htcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=GrYt4W62k2y4w3LyScVP91Yp7u7V4Hr2K1HPaMRwtM31d3ehrIXs6abj9J3JYzCc4upsd9LzQyvmE-EYVzE-ewbcENr4Trf3UefA1EpwCC8ttqA-rfzgqSJqrjrYuJD2bADJ04ewuv9xkges2j84gSHa99zQ-k5Adr64akAcHFxjAQUE64eEbszYeaUw2GHmQ7mzRCFxjauk2SgPSf4GfneRiyTEoTbb84oldd0nxOD_Hy-a79ijYkgjF7Bq8WDbZxS7J449aGUuj-fy_fAqCcGn76o958P4TrAE3upkxN1e1YZsKof26GCecNfSXWG-VXn-Jxj6UH7F6WBaw_htcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfvD54yAEobbcqzDQ3nH66p2fJYE6XjTmLR4YBiPHK3_yofZ90aDVcrsQTY2iaD0F1TdNNYpCqKSh2e2_hQNAlkvNYcaguQv6h0g41yag_4M6d1BPIoVhQbdhLgHTcA7itHxqu0Jq84wao_NGGHKJtznzZxBwJ0HtHlEz_Rn89PCwJko8z2KF5knTjF_UkCXgPcS3GiFEAjOe6cxedzM8BO3R3_d6xxYfcKCY6tQuWAivFlCa_rxz_1ifOa_OdFlqazaZRa94V8xXUyL_u8VvSr8pNwyj6YrbIy9wnOY03jiHnaN3HC_A4PLMgD2LeACktw6sg2w6CDXS3GdQT13Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=h1AFvsq1jeZ-GuN01md-0gnN3bEvTEHG8z8n0SJetbrID1WdFVbElO8TRCh-mfo0ZHWVoBeRrje2UBTEeIeI64NCojZMqynwa2IIcCREacZ_FTu2UjfdahMjonfm1znCgh9sdoSGOv8oL67y4hKTFiMemv1F6HfVgk23wwS_QLo2vn_iItpmVCzo79IOir-nfkI7BBnijOWcgPtpX8a7GP_2f_tBt8WDgRdLF4yco6GHf4fDOn_48D6VDTb2qsK7rdVHGbH2-WLwOXIdUihZxePmIUtVfmN5rVbFA_CfSwzqDACrfZNxDOkJLN23o0bTCZT4WpTpx7D4as3Tvb5Qpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=h1AFvsq1jeZ-GuN01md-0gnN3bEvTEHG8z8n0SJetbrID1WdFVbElO8TRCh-mfo0ZHWVoBeRrje2UBTEeIeI64NCojZMqynwa2IIcCREacZ_FTu2UjfdahMjonfm1znCgh9sdoSGOv8oL67y4hKTFiMemv1F6HfVgk23wwS_QLo2vn_iItpmVCzo79IOir-nfkI7BBnijOWcgPtpX8a7GP_2f_tBt8WDgRdLF4yco6GHf4fDOn_48D6VDTb2qsK7rdVHGbH2-WLwOXIdUihZxePmIUtVfmN5rVbFA_CfSwzqDACrfZNxDOkJLN23o0bTCZT4WpTpx7D4as3Tvb5Qpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1ZLvel1JvMKCuv3j4-Sb24PBIbg9L5YeWEz7Z8lefxmJe7VsHfTQ6v1pLrisEz6t_bxGiMU4ePEu5P3TQZRt3Mei_xiNXXH9k1s7-GNlCDBYS0Azm_7L1_075LXbNphzdgeSzrmyCDAE5bqu9qKZoEHQgxiG0fc2BMm3u5_ilZnXYRmyHQ1-pwPkwnaP_bs6bOq-_k3ARUPdk0NGisqdMBEofK6gZxOZLXgdArlfIc6rPim2HkpdzCxlg-cgDlMD8ZIVX0fHC7pQ48vAvXNtlmWIEo7RWGE49zswD-Vg7hMb0Hk6ZOy8P5vgsBKdRWLh7zGG09Td7MtSEwCXCP49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=gWqhhYRGN-lSV0sXBxUqSCa8OzB1R3OlbsvpqUy3pSp1dQr50B6-KspG9pxgxn6R0fCJSW36hsG3rrpUyEt_yUGp1e6xulKOPJUmjeLHiMLmxqxL5EeEAn9-6JfupTrkx9JQe_ESIhBkzbiBxGwX4m8oAG29mXIw9MaHDzzyo3RYW4Q3jkfFyMQr1dwmRxyTm7AB_Z5fqwQc8TKzsa0_sWpIdqlSkEtv2duJ6tYjQWD7McfJQNjabw_NcotZyj9Fgblqe_Qv63ycE9c231fzvE__vGdMyjuX6NLLDzNUS6ZbOz0Kavy7fdQBCY_YFG_8ItYnNl51xX8RS2nyJ2OD1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=gWqhhYRGN-lSV0sXBxUqSCa8OzB1R3OlbsvpqUy3pSp1dQr50B6-KspG9pxgxn6R0fCJSW36hsG3rrpUyEt_yUGp1e6xulKOPJUmjeLHiMLmxqxL5EeEAn9-6JfupTrkx9JQe_ESIhBkzbiBxGwX4m8oAG29mXIw9MaHDzzyo3RYW4Q3jkfFyMQr1dwmRxyTm7AB_Z5fqwQc8TKzsa0_sWpIdqlSkEtv2duJ6tYjQWD7McfJQNjabw_NcotZyj9Fgblqe_Qv63ycE9c231fzvE__vGdMyjuX6NLLDzNUS6ZbOz0Kavy7fdQBCY_YFG_8ItYnNl51xX8RS2nyJ2OD1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=D-pBU1NAHtGA5LT17qjJh4NvwpBQwmei-eNgkYKNLauep5P_ayljqJXFQkqjRMW3Qv9GI07qWY9yg5d2gkyLq7B85GQHU07F-kdeHbupPSO8OQG0hWH4J4SmNKyqkTDs69x0s9U_dwcih1P184fz_eNoO6AGqxEE-g9TzIrME0MtYf-flmjDD3JqfO3Ebil6k6pvqyb4BVL6XpwOZdUeQ5MDR4WGEADAz3cUTcjzMuW0i97my1Hoz-N4z2dkYI5a-ZR7itE26ZleDgI_Qcj3TrXa2w5YPzhq8yoqA5VbohD6RS7jppP62y9dXS2q5Jt4eqo6d1NJZhylHTo0O-6V9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=D-pBU1NAHtGA5LT17qjJh4NvwpBQwmei-eNgkYKNLauep5P_ayljqJXFQkqjRMW3Qv9GI07qWY9yg5d2gkyLq7B85GQHU07F-kdeHbupPSO8OQG0hWH4J4SmNKyqkTDs69x0s9U_dwcih1P184fz_eNoO6AGqxEE-g9TzIrME0MtYf-flmjDD3JqfO3Ebil6k6pvqyb4BVL6XpwOZdUeQ5MDR4WGEADAz3cUTcjzMuW0i97my1Hoz-N4z2dkYI5a-ZR7itE26ZleDgI_Qcj3TrXa2w5YPzhq8yoqA5VbohD6RS7jppP62y9dXS2q5Jt4eqo6d1NJZhylHTo0O-6V9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-C6GVg1HfsQyUbH5cp26jxh1M-nsQhPe3GLKPDKSPLU8bl05wFAidrFmU8QNshdDdAh2vMLrEwp19avjjjgMBrYB2v681HHjywBcssvZGX_CkXZdKQFCqv8RbrGiTK4WgNY1L-c51B44J4t8lXiKk6tGWDoH_ZziMe2dIE8568f-SLoA8CFIT_czuLhEHHueAZQskDI_Lg9FDQYQWRYtULu7b96zWQTPBHdQNxmOc6srYgDqxrCmJXDttAsJ7RcWvGGZmbto3-vlbKpu6cMvZzzc1NvovXNyeLltwf0XRiOftFaIu1GHkTmgoAX0lqBi6v4sqnazy21_0YYCrWxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcrt5rnbVVXSnb7P_FOK4MqPgDnhGdAqq0y5NgzfU5lO1JwthbYx9KLxKhggOH8mkjW2JxUnKFamNP0gSw52Qvmkd7_yC4z4QiGt7t6t3IGG2Ho58pEtGfyO1K7fty4jCz-HMl0NQcreiFHxuKQSY_MAhzEeWBgFxLztsCbby2ss4lOuxJiG_YdYPcNpUAyQNOOXGZush7U8kFW-EDeJvaD_v5Hses4iShnU1Ibb0tAXwF6kKJAyV3p0oxfbAC1ebcaX5oHlzO5roR5DdzG8hkq9hFSe6vjSC74BSV0aQBoaafklJzON8b1vqNpfFplCcxI9mynwHx7UYtREiiQdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDLTTVPBH1bb-5LgSx5h0t7LnrjJiRWAZ1qf3n91e8cua_qXQiLeE--cn5buxR60qcPguiQhHeqgqfkMPWpVvNegXK_-AVSDf7r_oFQaiOJWpPtrqPC0jQg3bd4WiDbo1lLY7PMHnDhn4IUUV5H9GueAeo2mogTuShL-eg1Mvna1ZSzl9aBNdVogaS3nunxKZYQCMSEazMtTpOMo9zTKwFYWJBYMXWCRg4Fb_97FCuqI5PN740WibamZaBu3_F11ZzDmggXzYT9NcAoQALzDDb-vBO_1oWa_-ii1xD7SQtASXxHYu7GEWiwz8RDqZx9VsMuxaSbbvzoNI9fKNyyjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=LtRsY8uifVSjPXtslc0bX8EuMi00Ftiz9OK3QgHAOMaCfr29lUCyl0Pbbe26bWvqTVwljSQ5vt7jNcshGWoux0oftdh0M9EwXXu6wUhi3lo-NcMrfFNSnSxmzdAqemhLS-Z6LE9yGM5YoAOHYgBw9q3e-mTQEZaGQRsJ40iMRWgkRRziBroJP9P8NtTSwHztTjs4STfkOjnD3DJjFNp06vpTmLPsAk3eVMjjxUZS-MJH4T_jq_yDAS-O00TdPd9N0cqPWeJVbwp_Ijz0JCtULLhSKi4ZNpEv26NzzoSw3gTipF3QGtEjfiI03pdpNQheDiVsbRwmhoXpJN7i1eQVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=LtRsY8uifVSjPXtslc0bX8EuMi00Ftiz9OK3QgHAOMaCfr29lUCyl0Pbbe26bWvqTVwljSQ5vt7jNcshGWoux0oftdh0M9EwXXu6wUhi3lo-NcMrfFNSnSxmzdAqemhLS-Z6LE9yGM5YoAOHYgBw9q3e-mTQEZaGQRsJ40iMRWgkRRziBroJP9P8NtTSwHztTjs4STfkOjnD3DJjFNp06vpTmLPsAk3eVMjjxUZS-MJH4T_jq_yDAS-O00TdPd9N0cqPWeJVbwp_Ijz0JCtULLhSKi4ZNpEv26NzzoSw3gTipF3QGtEjfiI03pdpNQheDiVsbRwmhoXpJN7i1eQVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=ZEpShNL3OaXx5JqWGh976PielTRGBHCYDEi1tEIoA5ZTd4pTVrGxdgIyVGvUxxt6N88c8HTlmravRFRSyvAuz3klJzbzTTwEs7DW3d3_sYdjDKIaTBL9RYkAWgT5KvC0PJ493do4OGRNYSaN0ZWbxK-e7pFPOwuWrYNrk3EZkItwvY7abaKj6MsASX65GLE-ZjUmCvTed2j5kOB-vSV4_535ciqdR32EYC-U75PvdJu7bklpHJjAWSKYBSVHQ_S6eOwoZjap7BkD2EMaxIZ3E3irzhPQZB0K3iAGjUuHIS3o4YrM0P0VvacpDZ9VM5B1XogOihFqFl54-_HaVtaq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=ZEpShNL3OaXx5JqWGh976PielTRGBHCYDEi1tEIoA5ZTd4pTVrGxdgIyVGvUxxt6N88c8HTlmravRFRSyvAuz3klJzbzTTwEs7DW3d3_sYdjDKIaTBL9RYkAWgT5KvC0PJ493do4OGRNYSaN0ZWbxK-e7pFPOwuWrYNrk3EZkItwvY7abaKj6MsASX65GLE-ZjUmCvTed2j5kOB-vSV4_535ciqdR32EYC-U75PvdJu7bklpHJjAWSKYBSVHQ_S6eOwoZjap7BkD2EMaxIZ3E3irzhPQZB0K3iAGjUuHIS3o4YrM0P0VvacpDZ9VM5B1XogOihFqFl54-_HaVtaq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfyIdyYyBXeqJTs9P-7IVuxSGxck_emlxqpYR2DY9vrQxYfAU7p-_bNb9neCJFWriYawQH6UEXTJbFw-Qbu2_Y8pLku6HuOqMWggfBn9AS8wl5x-A5JZ5JdO9Zmi8dBKDMGQKitxr6DUpdx0nE-hQ8qA7XVLZZ5GfWF8STYZX-Xc0NRAQXktWutKMZzMpu_E3XYpRNlT1NtnkCuLMVVuXfiQ8ahnzoLg8wM4mPwOHyMWCacNuRt5NngYymemNBqWQGd-8LKnygGYoRyne15xktRPh__zmOeTMWNMbOqMw9inoXLmAG8pZ398gg7jVFiIhRTY3uTa7uTSD_pkzOdlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=e50SOfoJVJkQl5wSGf8OT07TQ5owSIN7A3J8kTLyJEH2MmkjK6jjMzWEaUxC95xUibk8h3YHa9GRHNdXvAjRyIcLqHM9-bfVF_ZayTuAjnz8sDLnYuI7N1cl7KSjwNH-BTo5slVXhjMHo8ok64ctoDVWBDOcO2yva_rwSUkNmL45lC600BWn8yEXBZDVhncWFTK2UZ4i0rw92E8duEP-S-Nplmki1bDDUxqc1bMhK-kxUrGCW58zMlcBIIVoF-wSBBj7xQLLVLhbH8E1pM86KeKP-TlwFT6RhjOf2liF9bZD_yax731vVuvEXYU3EdRMcUKcaQrbcYlXG37WcABLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=e50SOfoJVJkQl5wSGf8OT07TQ5owSIN7A3J8kTLyJEH2MmkjK6jjMzWEaUxC95xUibk8h3YHa9GRHNdXvAjRyIcLqHM9-bfVF_ZayTuAjnz8sDLnYuI7N1cl7KSjwNH-BTo5slVXhjMHo8ok64ctoDVWBDOcO2yva_rwSUkNmL45lC600BWn8yEXBZDVhncWFTK2UZ4i0rw92E8duEP-S-Nplmki1bDDUxqc1bMhK-kxUrGCW58zMlcBIIVoF-wSBBj7xQLLVLhbH8E1pM86KeKP-TlwFT6RhjOf2liF9bZD_yax731vVuvEXYU3EdRMcUKcaQrbcYlXG37WcABLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVUSyh5FtyoLhZSiryZepsst6N_H4Y-pTt8bKnznoOAtxI-IBwTmbsxip-LtrwkoO8iaK2XzunH-d7Ayhy5-bZy1wXPXyF1GZf6UQ0Bq3v_MoAEEys2MjtPGXizg9brANhXRZywstRIe49MIyEdDfEDJr4Gz2gpC57K6o2Q45G9a-t4Fw6wWrALnWOu5zY5fXyEut1vsoCwafhH_ITxXv18vvxpKxIVUd7KSlOm2EUxQFfj1xYXyXKAfD5lsjeyL7zl2HggS3Lct5t4BqI7Egd6fH1PnlHjikm58sgzeVMl42oF2_lgQVSkAbun9RqHuZKfhbpw3dq_qydMRsY2yuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n51S14i1M0QPsre4Nd_tpzG22K7NqQVe5bl6SlWRDyhA-daVA-OrR57qLJiUfpncSm936ZdI3M7lK6z0XIrD7i0ILk16J-RcCtDQ3IgE9KXw2o1vbNErdGQTS-19V2WMPFGvW_9bls3a5pxfp2eagLQmgvWOFRKE5nHJ1GNF6X77YB6sgwG7XndjyIrfSmdLBqGxrrjsba1NczeQHOLQZc7eeVAKHMKOVd99TaD_Q2gz898tT1ldFNnWTGS6vViKF79RJBET7f4pS59tPs0-h4d_zGcH9FB1jZ32FKaby6c0YrM38YnzBuI8XePBjhrmpbbRX1Bljq94kM9WT075sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=iiY5dJZrI2ED9egr5FK2pYt8o4-D6L75RipSZ_f03UHopHo3ClEN5FCmMEcJ7WJ-HybIP1_RjOpD38SgoOdd8pZMmMCMVIHuAbhaZ_mCT7NqdVAgKAHKIjCF4jpurPvw7zoCXPx6VWnjGS5LwuOwF27DyHiE6lMm0WPmuoxMzUn1D1cknr5Ca_s01O_ZXjESvh7fT9QvvNpDf9Q2Us7g0x9JYiXiR_t4naOesZDF9hrv2BplGKmTL5HNQ9XQT1tQyO2oc41loodNOOA6rhGRcKzttsMeTuB7jt8FdyENCfuw43R7Fr_p577NFt4zXEFpyPDUEEN4kl7F_ZoFI9sV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=iiY5dJZrI2ED9egr5FK2pYt8o4-D6L75RipSZ_f03UHopHo3ClEN5FCmMEcJ7WJ-HybIP1_RjOpD38SgoOdd8pZMmMCMVIHuAbhaZ_mCT7NqdVAgKAHKIjCF4jpurPvw7zoCXPx6VWnjGS5LwuOwF27DyHiE6lMm0WPmuoxMzUn1D1cknr5Ca_s01O_ZXjESvh7fT9QvvNpDf9Q2Us7g0x9JYiXiR_t4naOesZDF9hrv2BplGKmTL5HNQ9XQT1tQyO2oc41loodNOOA6rhGRcKzttsMeTuB7jt8FdyENCfuw43R7Fr_p577NFt4zXEFpyPDUEEN4kl7F_ZoFI9sV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=f-svTZMgU6Sr40vAJE8w9uLsTjm3jD6qj6FluH7iG6kUr8WhBRYDkZvkPjCTaHHQQaD71xMDgtSoUFAFQMQeL_aBhisvxtK1EVZwyP2Zmn8dHC7axqvhhtH-rQNwORZXUMh7j4mH6bhUR6c4F0jQi8ZBKYcxvg1__3J-yLdVsArfj1fWvxB2G3DrtKv6HG4FlVFtcSU1ctFdU8UeftVP7tCNnQeQepBRHUr__Ax9kOv5PQ_QjG6XnTT1kOH97DB_MYZj2oNo3ddBcobVoUQB7TpPEu3UlKvlCwr5mhDbVt2Tf9xSdTqnxoZepSTZagx2mu8dRRHb82iD-axogyPL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=f-svTZMgU6Sr40vAJE8w9uLsTjm3jD6qj6FluH7iG6kUr8WhBRYDkZvkPjCTaHHQQaD71xMDgtSoUFAFQMQeL_aBhisvxtK1EVZwyP2Zmn8dHC7axqvhhtH-rQNwORZXUMh7j4mH6bhUR6c4F0jQi8ZBKYcxvg1__3J-yLdVsArfj1fWvxB2G3DrtKv6HG4FlVFtcSU1ctFdU8UeftVP7tCNnQeQepBRHUr__Ax9kOv5PQ_QjG6XnTT1kOH97DB_MYZj2oNo3ddBcobVoUQB7TpPEu3UlKvlCwr5mhDbVt2Tf9xSdTqnxoZepSTZagx2mu8dRRHb82iD-axogyPL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=e_1jivuLNue5vJZVtb1KmewWGF0Ay-PErX93hdLJzCULSKS9tCaZIiL2m2_K6AnJJqLcFnwVulIZlpomtVfe7Kn1kfMFYhHOwUNTdXDaOhLqdzlANBu7DtNLRvw9TQsgOe1nJMJRIHPCAVUVjt-ibgB1Cvi3sFwzeqy9S4YalqB_D6awC73M5NID91QDq72UYaTdWABD5B1z-1FOBXitSUPSCnhAdZx6plmgZm5FvDuJQsBqaDHRTFbRwcY8LZEhUh9JoZlvxKR7j5CgjOoGk3Wsu-HbLMZABy4yValiI_6IGIfp6R4OE1N39_xPLETdYhUP1lS2o5bwkHc9H_SVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=e_1jivuLNue5vJZVtb1KmewWGF0Ay-PErX93hdLJzCULSKS9tCaZIiL2m2_K6AnJJqLcFnwVulIZlpomtVfe7Kn1kfMFYhHOwUNTdXDaOhLqdzlANBu7DtNLRvw9TQsgOe1nJMJRIHPCAVUVjt-ibgB1Cvi3sFwzeqy9S4YalqB_D6awC73M5NID91QDq72UYaTdWABD5B1z-1FOBXitSUPSCnhAdZx6plmgZm5FvDuJQsBqaDHRTFbRwcY8LZEhUh9JoZlvxKR7j5CgjOoGk3Wsu-HbLMZABy4yValiI_6IGIfp6R4OE1N39_xPLETdYhUP1lS2o5bwkHc9H_SVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz3A1ttUwHvTgvMnXe9jR3xle96OOYoMJNh55lrc4rVBlqBUoZu6_r6s_PEL4Gb3TcgWAF4pHznSjY2cZgrJaOxhoNvbCND7Q7aktj591vqVhh6JhR0eEOOpIMrW8Sg_LKq8poCbZaUTzXYsSbYkWVhLv4yNVHtaYdFiAAftg8fm5zp9q3UXxo54Yo-ETY1jySh-QBbsIlmyOQoZ_IWHtJlkKwMQUhUpHpmJEr9LpgG4wa7GTT8tyTkn8D7Go2nmLkfMx8hq5LHtKJIuGuJjhGE6IPZFRfBy6yYgv-2rvIZRyd-vBxQCb5TJFA0uGDvnrIEdxceyiDTfbdRXoVOqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvr6PDKWI2FDDaDpTgz4tp5RwrZR_Zm29773JH2cgebCqyg854vHYieaqfMEp0oInGycg-K3VANpxejnS_7Na06lkxDvRj9aRWfh6mvYnffWWho059sKwgm5DyFz9GmvbGzhawXKcPBSuTNXSJkHmnF0ApJe2L6qmoPH3jDB6UShc_lObB-Xcw2cZDO6PuVCB0SWRiz6rNvTWoXJ4Gt9OvQrkT-IGq4_5AmswQNbQkeHIl1cgU6rFqLLvIF7e74_3m7hx2H3Sd90BErsTEH7WLXakzRax8nEfq-S4yXz5G0j1ZrOeATPUxFzP1BiSuP7HgkA3SXe8He81KZZgoJ0yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwhGWKlW1ULfMQ5USn-vocThbGLRKn-RqtcgGWtW70SA8nggp04HPHmYMO34vJFQe6xh66jr3NS8rKiWVqhLIWYK3T6WeBZ0sXSCtCnl2n7rpj_QNQob9YVdNLbFAdgsd5dd2xQQ4WqfxrZpAyKlbMw_rAdv0kTRJ8es2sb6g8v55WQoxmzd5iXKmSBPFVUnHMkACqpsLx90ukFXvf6kVz0ithrqU4mN9oET7hEpu_BZZQgKPPLwJmP9RA2n82u1yCUY7_nkSwmdh5wVE951HT8HOOkPOAHZUPKA_QLIr7zFHMcyXzWA6taGMRsgLmSHNJ4u27QHgvI0ZLrduKN6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=k1oNUPMGKUUT88pdQ5VKuAUrccmtpRPnpm1jGtuQ6Q8N_8ySQfXoLgAQD9ze0yTopCxvBWipKIv5P5-cLaND2j7qKe1VGGOr3MGUCejKiRKwFx2vuVKFLsFR9N--dx9iL1ecoNcRDwYtqC3kHZ9MIiDbiKMCzBX54T9W5dOtEng8ribVjekXDKf6OfRd3bSsoQf02kasZSBHSDatABeolx3S1eTm_bCyfU0U8e6j2w0aOzrq-PMttDoHrx0B7FMDmkZhgxWaxp993i06-cly9Vl95SyNg4_lqA6yYric5JFa8tNvmsZlHmYvjcfa931GAGJ-PgIvAIlGH8ALE6eo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=k1oNUPMGKUUT88pdQ5VKuAUrccmtpRPnpm1jGtuQ6Q8N_8ySQfXoLgAQD9ze0yTopCxvBWipKIv5P5-cLaND2j7qKe1VGGOr3MGUCejKiRKwFx2vuVKFLsFR9N--dx9iL1ecoNcRDwYtqC3kHZ9MIiDbiKMCzBX54T9W5dOtEng8ribVjekXDKf6OfRd3bSsoQf02kasZSBHSDatABeolx3S1eTm_bCyfU0U8e6j2w0aOzrq-PMttDoHrx0B7FMDmkZhgxWaxp993i06-cly9Vl95SyNg4_lqA6yYric5JFa8tNvmsZlHmYvjcfa931GAGJ-PgIvAIlGH8ALE6eo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SeeO9mSY4okGBb-LTv1n2-dtew99uUuFA2polJqSbuDroc_k7YOVwaimxMkF3EgIOlof7cj_vQUoe8FkWZdYKxOOpF2vgq36qtVsEuiqQIiJRJUXzL4MtxJYcmzc5C7x4HIk2vXdEmgBMHdwKtPxQF-uT1B6gUR-k_9su4g1LFjrADi3JtSA-Y1sugq22yLMSXSUA-a2M_HgyzVnbyUaLUc7qqd7k4bRUoQVmIKx3aLwwq6UJf79nDbgtsBRrzK0NYoZoFP2KQCDlfrX4lkcOAdxxcf7y9OKGQa53Ops6hToGavlXY6_4DfFIrE0V27L9eFZwLy8wTIrYm14wuzVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=g6v0EKO-kl_U_VSnhIIK8ZdBNObFjcVytT7JGCIKu889sTHhlyrwu_438ZTYo6ilz1EDVCLp0VfMn3LZ1fMYa5BiQHLuizb59kKNF85kzXkexcgTbmNMmb8qY97vzFrxDRBHh7BFDcaQPM1SW7u7y6OVZUV9XBvil0rrqyd7XnCVfsDthSN9hVhDfulud1vU2uNTRoFYB2Mklhovro3VwnBUYYFInl0Rd26cVd86lExk9HT1PTm5IeY4-HpAPCrVQGTduGEFoaIymaSBtu7Kga_cMx0gTL29pW-SjIoYmj46gfJTkPwfzdJe06J5Uq8sLdt6C1oflnbZv4zPxtDUTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=g6v0EKO-kl_U_VSnhIIK8ZdBNObFjcVytT7JGCIKu889sTHhlyrwu_438ZTYo6ilz1EDVCLp0VfMn3LZ1fMYa5BiQHLuizb59kKNF85kzXkexcgTbmNMmb8qY97vzFrxDRBHh7BFDcaQPM1SW7u7y6OVZUV9XBvil0rrqyd7XnCVfsDthSN9hVhDfulud1vU2uNTRoFYB2Mklhovro3VwnBUYYFInl0Rd26cVd86lExk9HT1PTm5IeY4-HpAPCrVQGTduGEFoaIymaSBtu7Kga_cMx0gTL29pW-SjIoYmj46gfJTkPwfzdJe06J5Uq8sLdt6C1oflnbZv4zPxtDUTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDDWUmoNhDsOraqozB32yniyvYJroKgqY5tReROcMdIyMl1DM9R_dH0Jwkcj8I4NAh4QLKy7DVJg2oTgnRaLJ_r2NTTCiF9bxymqRQXq2hfw6IYExkxTIe3zGoctNu2onzqZLN8Fh1r9vQVPXztCI8NTTCi2vAhj5oVjP5PLsGYnkn8bY3qC7jwXFW4YRySqNWQh0p98nVyk2Cgor7miIQ8KPVWF8gs6t0SQfj0skvf1GW_n4VssptqiM3iT16Jo8rke5sP4lBPEEpJ19GyxOAoJJc5rApE9p7D75Kofih3ZiUM4Z_z8ENaub0i7GNn9eubCpFPu5eQi-dxlLidncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=qx467szd31mOoDvfKypIca3Ut55rOY-8YBRin9dKVRq26XLhUR80w5x1uRKgQJfCHoXBOM-LxPVjqEU7AR_h-C0CEFTQaLlmdDKpBHg27egvGriMe9_jCLPwQ40hBo7Y-_w_lEUB_UWjOLxE1w5zKZ2KXW0M8S5dClJyz-mmTkZLVEh-2lohDihtDz5SagcBV0PF1vXn1m2hVmeokg4gez6DkmPlrLTQU5DsLVUyyM_Bm1dvLJ8m6VD1qMNCVNDJXKkbAHd5LE04HsmUfXqIcmE-8XLal0213byOH4PsI_eliipHggac08MpTxTJJKbUabsREtyCY39_ADzULhC_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=qx467szd31mOoDvfKypIca3Ut55rOY-8YBRin9dKVRq26XLhUR80w5x1uRKgQJfCHoXBOM-LxPVjqEU7AR_h-C0CEFTQaLlmdDKpBHg27egvGriMe9_jCLPwQ40hBo7Y-_w_lEUB_UWjOLxE1w5zKZ2KXW0M8S5dClJyz-mmTkZLVEh-2lohDihtDz5SagcBV0PF1vXn1m2hVmeokg4gez6DkmPlrLTQU5DsLVUyyM_Bm1dvLJ8m6VD1qMNCVNDJXKkbAHd5LE04HsmUfXqIcmE-8XLal0213byOH4PsI_eliipHggac08MpTxTJJKbUabsREtyCY39_ADzULhC_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-q0S7jzCnR86gN5Av_e6E6ywhO9rTT9cyNsRzYOCiQajFzTXtB6Q-QPSfnrrnRaqs5n8-SO8xctf4cQPy1-oPBea5cCJPjaQDIQR2tR6bnqRkZVaEI5dtn-NALnIB8ZQQRMLARzd9mBGnIPv1OVmCNBzS7ShV99OT0Z1exgiMRGfvlieJo1Tdi5y-Da820E9z2N7ZRSPYP2Wm84zwcT7ALjlXLKaeIs4WPCv9hxoT8bC12uyUduMNaFfEJckmZgVY_KV3e46QHy-0aNmWPATYfdlKUew_gCZidaYooQhPmKI4HrJYv_VQQYlI0pO2Wehxd2WE95HDi7AHt5m7E0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMiWyuKEaYgwZomv0RE_xcwKp89FIWbfoiNACdibRMgVllLDyG_eJfsgSfUGHgOsgktawMq0iP6dRoKxpiJfi99p5QBvdXeBd0fCiz7NrWUy7SLbdBTAThJvZ4NeGjF1qIinpzrEaMCzGMpBGe2BWS3AswXQJvRL0DIzmlMwvcRcAkI3gaUjMI3nsmL9hVAXpkuHzUoy2RDhJkcZ6JKpSL9RvwwrrwatLFwiJW1DC4IXFvdxOqPrYvWL6fFtlJIGnZp9eFNHmLZd8TO2ZFcrPhtsdiK7mxcQICHDRMTzfV2H1FNJ0yBRaYUzJMY_VLlfdPOfa3aIwGR7tCnpAetd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMzbWC7PBUu3tqXWs_Jk4GTwyhKkUqFHF5AbYyQ0vqNScSQXxVnwU23KAgzYR0wDluoQpbwBTXPifKGXzJ6nHfgsp5284oIb__WOWsvxtCOWxiCfUtzPv5dZ4oq1lAFVuUm97gLRoE1T3xg6jnJLi53XgUZ-YNIii9_OZ-GAQhmNohazHICpYiRgKCCp-wZ9A8BTlhjvXTOSU7yZoINpkDvzkS8UDtK3_r8uGxS9RnB11vZ6d8oiKrJJyvs7S__s60DgqBvhyTH5bj3UUkTmy8TAtQhO93zKkwmbKM1NIbNM141NXDlXDcoc78YpoA9q060MyMDGQMJm04jDwcx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8Lpewh9GJZ9iTtWau7A2K359m6LRHSwYSWURQL16XSJxCqiWGF3YcLTD6SKTTzEEexdhYDnwLgP4PmLtXZoQ0uYWATskF3YQk-IVvpLA0kmYghroi7oVduhhGzrBgeJ0XHKgjD5e-Ii_EZRda7x-hc7vz7G5uEETd2ciN2QXZVoKXvgX0WVumYsmVz9uVk2gWofiop7qZct-5_BcxpSlOyVpMKac1HnV9xSAECaG0ArkZd28Ro0QpzERD8-PfvoGUtcoiWTdpfkOC_DxtI-AZ7wsA1q5l5Vzlza-lxRFT_kZ9SrLFBn4qrILfK3qJHuAyrbisZg5fScLeJzXn6hRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEVq9DbLWRYkXhGiYF5XMe8r0TnunjQFqbfM3BNVPqOG-GJNBFkx8d38moSTNtClW-OM9ZABpPMnqN9GT4R6VYWe6i5TA6QWpnyhTBj21N-mq9EdEi1ZmXoSlQ_nK-6FNp0vK9C34WmKB3GP7euy-CqRhn7JVy__pAMIb9jsDQ6Agh_2FUMFOTCXaI-srWmm-B8QrTeVTvkO0zJ5eR3NaxYmT8d_n-zCStlGo6idxEM3kPzmBAp3MBflSjzOXXLfJmHJd0XQRswjO0kNC8z58WOOWjdgfGlttkAaltdTwohyHfdyv62EWQlOp-2raAHFzEXOAMvMnGoU-rxHjA6AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=lf68scmqQDIu3WfWUKpXYkaNI5bBW-YomXwUDNctkbpTuR88LIJxRvRJL7Wlk2cn9V1HZUxCteWPMQydZ6yn5OBJBs4aYdif2n-8W2I6HJFDOjeV-gaDjgmdzlk4jPJ-VGTLQOrmdr9JwYVvUeCP6ZW3ndMtGMnAwEAd3BQ_HHA78e2tg8Yls0K71hIkMcZ_qFX2R9AzFV2dWRIklilULcgxfs6Uv_EVC_nl-wUf95UOenhaJ-UKmtKd51mDDSyf80Xs-3gLS3ZukGtPN5IRfZM93zlNB3AKcMgOUirTA9vogtssO8wZXu89-fLi_Vpvt6C6GUHD7NNrcMxNEMzKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=lf68scmqQDIu3WfWUKpXYkaNI5bBW-YomXwUDNctkbpTuR88LIJxRvRJL7Wlk2cn9V1HZUxCteWPMQydZ6yn5OBJBs4aYdif2n-8W2I6HJFDOjeV-gaDjgmdzlk4jPJ-VGTLQOrmdr9JwYVvUeCP6ZW3ndMtGMnAwEAd3BQ_HHA78e2tg8Yls0K71hIkMcZ_qFX2R9AzFV2dWRIklilULcgxfs6Uv_EVC_nl-wUf95UOenhaJ-UKmtKd51mDDSyf80Xs-3gLS3ZukGtPN5IRfZM93zlNB3AKcMgOUirTA9vogtssO8wZXu89-fLi_Vpvt6C6GUHD7NNrcMxNEMzKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=H6QRjJIySdTNE-NpQSmbG160Jrh_fh8letNpXGr56r8n0xQOsP8P9dvUlDqhvCodBfc4nlebFaR6D1XOFIJ-gFsmx41XPOm2ERlq4ANB9zlsvlql2ApibxsR1z5uguI-DrvoC_8oN0jd1gpAe6PlzTTCY8zTVrJdG2vDX8xn3FdJAdIuIzi64W2ke4iBbXKCdJ2MqhV62O7eecmSlwjCoDTy8kf3KnD0nFoc9C9PH1Mt7qvD9WbjDHvU6Fc1chM9rXx_tKAUzt2DA6Q_RMxJUXIJLdWdXQKgrBphaG7XhbzPvvCCBGTdzQuSwvbcn7Q-DY-2hPm7UbIu6_A8cOlGWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=H6QRjJIySdTNE-NpQSmbG160Jrh_fh8letNpXGr56r8n0xQOsP8P9dvUlDqhvCodBfc4nlebFaR6D1XOFIJ-gFsmx41XPOm2ERlq4ANB9zlsvlql2ApibxsR1z5uguI-DrvoC_8oN0jd1gpAe6PlzTTCY8zTVrJdG2vDX8xn3FdJAdIuIzi64W2ke4iBbXKCdJ2MqhV62O7eecmSlwjCoDTy8kf3KnD0nFoc9C9PH1Mt7qvD9WbjDHvU6Fc1chM9rXx_tKAUzt2DA6Q_RMxJUXIJLdWdXQKgrBphaG7XhbzPvvCCBGTdzQuSwvbcn7Q-DY-2hPm7UbIu6_A8cOlGWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=fZncVdd4CG-l79pyR7RDxoQPGI4Djgq3ToDouvWQ71kCUjgFZxHaRn_wqeoFYgn7ekdqXotf0_qSH6_dmFNi3TJD1xHKyg5bHqokMKSW3v1sxpXgr7CjklEx93uk_zhP7syXnfSjqmGTiL7agICsibxWcXKlFXTW4iPpBE2wRshf2eZgskmMdlRYadvnv1eTSmjm0__RWevrh5TzwFLXyWzRx5uoXzeFoFkmXyKePnnR24k6qxeq7CxFs2l5jH2updpafmy1QW9bMLOTQIs7oSAmtvV5ig-2qY2Hrrx_fQ-xXawmpZPpAdDf_OHG_k1P2FdJ6RfXr4p3gP5l4LSMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=fZncVdd4CG-l79pyR7RDxoQPGI4Djgq3ToDouvWQ71kCUjgFZxHaRn_wqeoFYgn7ekdqXotf0_qSH6_dmFNi3TJD1xHKyg5bHqokMKSW3v1sxpXgr7CjklEx93uk_zhP7syXnfSjqmGTiL7agICsibxWcXKlFXTW4iPpBE2wRshf2eZgskmMdlRYadvnv1eTSmjm0__RWevrh5TzwFLXyWzRx5uoXzeFoFkmXyKePnnR24k6qxeq7CxFs2l5jH2updpafmy1QW9bMLOTQIs7oSAmtvV5ig-2qY2Hrrx_fQ-xXawmpZPpAdDf_OHG_k1P2FdJ6RfXr4p3gP5l4LSMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrwrM__py8It7yDrv8IrIp4Z6mtqeoT8CciQrpeyhl2PP2CC-1JLJz_HAybGZzY8SAYBN7JRuMbcsFfXQkWdnFSu2nBFhsgviaBVJL9cX7A9KZu6uq1pKR7Fy98QzgvDzrwhVwq8d7B81VIqErJurQyiAlLiSRVvBxeizIuz-cb_00OsvjH7QC0Y7W781kK8Lge2aTHZE6wbZqTQ_SWRzfGjT77gUMbG6MDBMveALq4Gg1oIWmQYYoRb4Dx9BQCI8Q0ssGEzsOsCC3bsPRb1OpSDv2GRJPXWUBIngqDDp19eoo5QfLvfNbjbejCGYzlYWGN2_2AfoBwXQW3w29GY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dijg-JHAA8we9AEsiGCJRL3aIYKVJwGFpqhE1kL_Ynj16e8r94HQFD7KzcpFXMyCr_JEYJT0mIubXTnNkY7--dDqIgeC5q0gFNyIsej4HoPH2Xa6NEOGKkoXnRUXNG4uI6UNYQ-KzElXR2bBMyMv-_wM7aeVUobY4r1OsnL4-l9oBJ59XaWxLbPR3V-RLLL2IVlKggYhaZL-LfEuT5lQYBl9bVo16W2i0aL_Dnx5eHg8_o8jwcGj11X3A8qCMWnobqNOlLBNsuxcFOajh0BG9ibWq5zSoPgRho5d27IoR3eUgUZVHCBegSZZoKVKARqGbjhVFIOF8c6uwBI-ps-FhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiHIih2pfsbtOGW0djOX3OI-_J0QSEvoSyDzFHB3raLia6SqtSw7GEftKflC-BLC1Py7hmmaaBEzyZE2HMKbnnkV-7VNjmKEAAljVkAWDPvWHNWWJHCWk-8N-zxHcJ_fdNDar-o0g3n3sik8QjtZtqngUSFmE0Qc4t6-gQGaU0gNjhvtBM2bXXCeG01h16TxMDqMtH4S03cJNcgJhjYJMC0ntHWm9cH_zbj_EcB9jEGqwwFQ7f8oqcVoLlZ1IyupzxYI4NcmGxn8mKiuGRLNdJbeg2tze1pUgPRLARDklVUM45b5OPfR237mHei8fW0LH70-PmuQnrzwxYF37pmcpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NQDPJfY7TMqsErl5DMdWhlmlnYnq4XBDVV3JM394mOGE2uB3aa4t80BVF_Uk1kte5xxdJgkIVeQrGlYT5KwJauLpOXNAK36Uv6ulotMKUwVx0iVokoFeoiHNHksuDoxZemgzsjRG5ed9gO3vqKHSH__HioCqYxW625dxedqD2rzgUM2juplSyg4UkqaCrBPKgXSKGxu_sLl1dJ6whbGpmg1ynYA3n8ypd91pZxLnP8yYelAXqLdyDdRtxpWjGFblatPUWSlbs5Rfti2P7LtYDGHDs7-OdNmg6hlcUqG7Hy9I_myvLI8SswFt-JBlLN54Y9TwPlzs-6OllelEXngIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NQDPJfY7TMqsErl5DMdWhlmlnYnq4XBDVV3JM394mOGE2uB3aa4t80BVF_Uk1kte5xxdJgkIVeQrGlYT5KwJauLpOXNAK36Uv6ulotMKUwVx0iVokoFeoiHNHksuDoxZemgzsjRG5ed9gO3vqKHSH__HioCqYxW625dxedqD2rzgUM2juplSyg4UkqaCrBPKgXSKGxu_sLl1dJ6whbGpmg1ynYA3n8ypd91pZxLnP8yYelAXqLdyDdRtxpWjGFblatPUWSlbs5Rfti2P7LtYDGHDs7-OdNmg6hlcUqG7Hy9I_myvLI8SswFt-JBlLN54Y9TwPlzs-6OllelEXngIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=Uc5qNqCtTCt6niuox1mZckDia2g1nnYErx0RekuqdaxgHtplP40DkOwwPETrCBuybQOQ_qmMdOFuBtHX4t04_sRtesKUH-A4bBQlOfhtppbWudyNTEfvw1xROLF3ANDUr7dUY8_1ADE1hhju6r2BAOMRRpjRk7s5is-1zamiHUZQ6LljzphoIlvP-CFT7RoCq_7ZqqMoBP3kC5z_ZtdgkpqFDMPQDDlEts1cOfCWxZV4c1wIFMJuhQMhGKxkDZ9oHtZ7eXUnReoEqbQFDw8-BHAEahZsCJ6_ZSP0iqqXKam7-qHG1vRmmojvBlMJNO3nanXSYBNF6LIBWWIaTZPgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=Uc5qNqCtTCt6niuox1mZckDia2g1nnYErx0RekuqdaxgHtplP40DkOwwPETrCBuybQOQ_qmMdOFuBtHX4t04_sRtesKUH-A4bBQlOfhtppbWudyNTEfvw1xROLF3ANDUr7dUY8_1ADE1hhju6r2BAOMRRpjRk7s5is-1zamiHUZQ6LljzphoIlvP-CFT7RoCq_7ZqqMoBP3kC5z_ZtdgkpqFDMPQDDlEts1cOfCWxZV4c1wIFMJuhQMhGKxkDZ9oHtZ7eXUnReoEqbQFDw8-BHAEahZsCJ6_ZSP0iqqXKam7-qHG1vRmmojvBlMJNO3nanXSYBNF6LIBWWIaTZPgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=er9qAtM9UD0C_Q8i-M2lKzbfxRd8etkhZKQQ8BmJKeiFX2Jym-VSh9wE40jV2OcRsn7033tx5f6KzqR1v55-Jse7sS0KP0pWSP-sOZsG5--6-FDwqXLUg8tIMCYtvnZobR-TXczAlNQCUh_Fgdf8yZWGoPoiAsQ9FGAo6GBJLWcd41rt98aFfBdGHT300QzlBj3qkq-vqWiNTBg4xJk1VvlvZwSPcgpA6prBR28DPO9V_uUDmn4vszJKPolaEAppG6Vu6pYUPiIn8PYwIWZkuqslAhqdDft6OiGAjcTdxHJo5V2cQVJ_Wg95fuMoNuW-kvSIYOSdogbA6z-bOZFcdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=er9qAtM9UD0C_Q8i-M2lKzbfxRd8etkhZKQQ8BmJKeiFX2Jym-VSh9wE40jV2OcRsn7033tx5f6KzqR1v55-Jse7sS0KP0pWSP-sOZsG5--6-FDwqXLUg8tIMCYtvnZobR-TXczAlNQCUh_Fgdf8yZWGoPoiAsQ9FGAo6GBJLWcd41rt98aFfBdGHT300QzlBj3qkq-vqWiNTBg4xJk1VvlvZwSPcgpA6prBR28DPO9V_uUDmn4vszJKPolaEAppG6Vu6pYUPiIn8PYwIWZkuqslAhqdDft6OiGAjcTdxHJo5V2cQVJ_Wg95fuMoNuW-kvSIYOSdogbA6z-bOZFcdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=ayiONgdPyyAQz1CsDGWUO9_O7guepfgK_tcmmtPMC4SuiB2i0PdEH_70Ozvi7CqDjvJIR20SYclbz9Oz8UCW-JnLsA7KeawL6hoYiyGfSuSoJdDKYlvJp1y8Z9NNbL8LFk5XOzrev6dcELifKVrmyElWedZi4SXvMf2Lfo-z0Iybg2L4Jm0I0cfL3cfaWN0U08PzjJdM26eYjcErEztoDYpiCnsYJN6rZQw_YdMJtdXIwyz6MJhwhWUn1E_RpDvFro6RY2ZFvvUMQhA04RoCYmsC8PpOr6XxA8K2bWeyOkR6XidXf3-3b3GghkKoq9E2B75rfVKG2T2JfzXf7Y_9GoiJD5VCU_dxK7INhfnmsWCW2HpoyWTF_J8Z-McSd3C5o9cfF-ZfQdCIKFmbRIJk7Xzu_CxV2wfaK_1OEisELZpyyAYr6_-zgYaM4NzWOY6zofBMMwKqpux4kH50oYZkmm79eX2lB5RDPMbd9oexHFZWslBJWvH26ob-OsAYiM-58y5mpa8lMH2vLUks65L9F7mVIHIMtgr74Th6zvQQ-L-lMzoFjSN8WNrqVzJk3NI-O5F5uUrDkLv_rCr_8EEqIx-bgbwAbmT4w6PQzK8HNOj1hByz3Ga61hYj37_C9z81i8eOsddcEGpH2L-K4swUc1ZdEjyYcqhxWslYO52t-b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=ayiONgdPyyAQz1CsDGWUO9_O7guepfgK_tcmmtPMC4SuiB2i0PdEH_70Ozvi7CqDjvJIR20SYclbz9Oz8UCW-JnLsA7KeawL6hoYiyGfSuSoJdDKYlvJp1y8Z9NNbL8LFk5XOzrev6dcELifKVrmyElWedZi4SXvMf2Lfo-z0Iybg2L4Jm0I0cfL3cfaWN0U08PzjJdM26eYjcErEztoDYpiCnsYJN6rZQw_YdMJtdXIwyz6MJhwhWUn1E_RpDvFro6RY2ZFvvUMQhA04RoCYmsC8PpOr6XxA8K2bWeyOkR6XidXf3-3b3GghkKoq9E2B75rfVKG2T2JfzXf7Y_9GoiJD5VCU_dxK7INhfnmsWCW2HpoyWTF_J8Z-McSd3C5o9cfF-ZfQdCIKFmbRIJk7Xzu_CxV2wfaK_1OEisELZpyyAYr6_-zgYaM4NzWOY6zofBMMwKqpux4kH50oYZkmm79eX2lB5RDPMbd9oexHFZWslBJWvH26ob-OsAYiM-58y5mpa8lMH2vLUks65L9F7mVIHIMtgr74Th6zvQQ-L-lMzoFjSN8WNrqVzJk3NI-O5F5uUrDkLv_rCr_8EEqIx-bgbwAbmT4w6PQzK8HNOj1hByz3Ga61hYj37_C9z81i8eOsddcEGpH2L-K4swUc1ZdEjyYcqhxWslYO52t-b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
