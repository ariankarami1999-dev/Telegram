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
<img src="https://cdn4.telesco.pe/file/XE2AfZ8KAxP7vqgjTayhmFRWqLjdWD9nRNgRLwBLTBoIedyZgpvCkusoZrXF4kqInZCHa7QRI_a6nmWpwxWN8HcPti74WFRmr4BWnNzWlRsADHruuJB0DyMcpxGEukTzdODVErV88f6f9bmmeRpEJ76qru0EmsEtdyus7Ferz6LIufagy7M-wFIrAyaC7dgcP0tRM41Sauv-dTxp51XnR9v89-NxH_Bqw3Vm2lut0YY1jWYfhwjclvaCzEIU-av2UXv2WEZd8udyMSIRKR74OvNp08K6iir7DEHo9mWFWXhcQwDcDl6TbxZFtYcGTnVdPVP0I_OJQEZhFEAvvwh1Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 22:22:38</div>
<hr>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به كشاورز زمين داد، چريك شد
به زن هويت داد، آنارشيست شد
به كارگر سهام داد، كمونيست شد
به هنرمند اعتبار داد، توده اى شد
به مسلمان حرمت داد، تروريست شد
به دانشجو بورسيه داد، ماركسيست شد
به اقليت حقوق برابر داد، جدايى طلب شد
@WarRoom
نسل ۵۷</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/19841" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEEDKkqBCN4Ra8ItQdhCGfejJTItAN971W8WMmIycsoCq8C0Kflwct0epZz3s3X2RZb894ku2dHXqrIHzLvYYg_7KY-78YUogOk5TSEs1A44VpAigfJfMMrFLCCv_JX2okaz70weY0eJg9axcE-ua5IuDDItoe0v1fWD5EuZJcB9SFfLtHvJxe8vw9oxhR-OzCCWKlUK1zQ37_YeuEQ7yePdW21Z3dUWkED_QV1AihwN6PPRQP4wJU0IayUEF0c08-gMVDSkQamQD4eN9YiVRGDwELJ72ru9cMPCbM_ktrzkI1KOh29hfRLfYD5bexVftiSNR19IbVuEW5okXqWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عمو لیندزی بخاطر ما تا مونیخ اومد، حالا وقتشه ما بخاطرش تا واشنگتن بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/19840" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏در برنامه دیشب مارک لوین پیشنهاد داده شد که یک دولت قانونی در تبعید با رهبری شاهزاده رضا پهلوی تشکیل داده بشه. مارک لوین این رو یک ایده فوق‌العاده خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/19839" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۵ عبری: نتانیاهو در دیدار خود با ترامپ، تحت فشار زیادی قرار خواهد گرفت در مورد مسائل مختلف، از جمله سوریه، غزه و لبنان. این دیدار بسیار مهم است و امیدواریم که مقدمه‌ای برای یک عملیات مشترک بین اسرائیل و آمریکا علیه ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/19838" target="_blank">📅 21:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار: آیا نتانیاهو از شما می‌خواهد که با ایران به توافق برسید، یا از شما می‌خواهد که به حملات خود ادامه دهید؟
ترامپ: عملکرد بیبی عالی بود. ما در کنار هم عالی هستیم ، نمیخوام بگم ولی ایران اکنون ۸ درصد او چیزی هست که چهار ماه پیش بوده
@WarRoom</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/19837" target="_blank">📅 20:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: از پوتین درباره ارائه کردن تصاویر ماهواره‌ای روسیه به ایران، سؤال خواهم کرد. با اسرائیل در مورد ایران مواضع بسیار نزدیکی داریم. ذخایر مهمات زیادی داریم و مایلم که مهمات بیشتری فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/19836" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/19835" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار: آیا شما و نتانیاهو در مورد ایران با هم موافق هستید؟
ترامپ: یک اختلاف جزئی وجود دارد، اما ما بسیار به هم نزدیک هستیم، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/19834" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: من زمان زیادی را با ایران سپری می‌کنم و فرصتی وجود دارد که اتفاقات خوبی رخ دهد.
ایران در طول چهارده روز گذشته، ضربه بزرگی دریافت کرده است.
آنها به ما با لحنی بسیار مؤدبانه درخواست کردند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
احتمال رسیدن به توافق وجود دارد.
اگر اقداماتی که ما انجام دادیم، صورت نگرفته بود، آن‌ها اکنون آمادگی مذاکره با ما را نداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/19833" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار: آیا از وزیر دفاع، پیتر هیگز، به خاطر توصیه‌هایی که در ابتدای جنگ با ایران به شما ارائه کرد و نتایجی که در پی آن حاصل شد، احساس خشم یا ناامیدی کردید؟
ترامپ: نه، ایشان وظیفه‌اش را به بهترین نحو انجام داد. ما ارتش ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/19832" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm57G2puJ4T3gVWarWLF3_nh0FTydVzUH1Q6nR3FS0VMbKOfKuPHpmkHUXcVC4KBOdSTRnM1EBKUXfPME9_8_PbenLXN4b0z0fb3SbGrokhf1p8T5kgaTHR5D74PuaO2hE0tdEVzc_JXbdL660M4mopMiPSVPmNKmjTW9P6U5_7Yjj_naExcbjSRPTxbvWn6WJ0giFa8dYulqBiKbOB2TYaCrd3vjqqk8-xIN7xDFCw1toe4pgw5L2_PfP3a3PqBWhgSUoJ78JHfc8GkeasXp-fAL3iGlI6HVLr-vjWmlbIh0wlq9l_MAM_NMT6EbHQoOslV6qgOKs74clUtFax4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/19831" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
@WarRoom</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/19830" target="_blank">📅 19:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند. جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند. @WarRoom</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/19829" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0bHap6RRtIEi3NTzgqEFqK0mvahqFDi_8ycgaoOXFeD5By9thu9D96jsTsCG8BL_1tUep03HAGPEazvELvDqn4n4Rw0x-Fy0_rFeqeKGps42Ts04gBiqQq53NtfQJbX1qWH82LfyfNr9CdXUx8kLzK0YeHCEmjxYCXDbxDnggbKMS9HG8xGqrTyYQAQhXTQVN8f4MuORpPp-M_2ibLm55yMFqEHb_YGMFgCfLGWR8nx3sEmI7cbY-N5b3vF_Iy7McGoph7L_0PrZ5WTk7lHF5l1aJQzqkd-FMdN37zEKhT5uJrsdov4pnf6k6yp4D-NmzD4zE8enyNaHL9qdSYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک ملوان آمریکایی در حال گشت‌زنی در دریای عرب توسط ناو هواپیمابر یو اس اس فرانک ای. پترسن جونیور (DDG 121) است که از محاصره دریایی ایران توسط آمریکا حمایت می‌کند. سنتکام ۱۷ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است تا از رعایت این تحریم‌ها اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/19828" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هم اکنون
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
@WarRoom</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/19827" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تامیز اسرائیل : بنیامین نتانیاهو در دیدار پیش‌رو با دونالد ترامپ در کاخ سفید قصد دارد اطلاعاتی جدید و حساسی درباره روند بازسازی برنامه‌های نظامی و هسته‌ای ایران ارائه کند. به گفته منابع اسرائیلی، این اطلاعات شامل ارزیابی‌هایی است که نشان می‌دهد ایران تلاش‌های خود را برای بازیابی توان نظامی و پیشبرد برنامه هسته‌ای افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/19826" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19825">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار:علت پذیرش درخواست میانجی‌ها برای توقف آتش توسط شما چی بود؟
ترامپ:چیزی برای از دست دادن یا به دست آوردن نبود ‏
@WarRoom</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/19825" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19824">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqC3zp5acTqCcFYKyXEf_hPclD3xmQaRdH6akETclGn9xt8LxULTA1ky6-4V_-LYtu1DpTOIPmqNPApsGhlr1ASyyJWRBihE5eyuMFzU4CH0HbCcVPNfWsrV_8Ag_rMbOOUZZCX343YwjlP1nJaLN3hntIx8S4hzsuGi7ejPTinsUUkq0KUtYeznJwHKwz8a83bayvTE89XGYkApiull9oR5KNCkEA5T6y57Xlrrw_Oi7hbtulsqbb4qSR0UAen_242gddE1WKlNvqOCfsk_SFrZ5Z_Q-9s7O-Vj_9lOcMDB24QfEAotTWcIEgpIjfWUpmRDJLbSVTFNozTGXQQ-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/19824" target="_blank">📅 18:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU7Rv_XYlLcqq9QO_z_VyL5iNf2g7v9_4kT8UiMBsbOcJ_4h_A93Lt2PrWdXbt8pPlYlpIQFVo-DV_hUyxFrYntz6tWAMAKp22AclPnslQEUmA-w-TvWCLe8z9vBdUOCg4ady2WLDDIq2D_cmi5phwqAnYsPXze9jmb2EqPSiVvmvqC7evd4zbrkkF50q2hqRFZdFv2wt4AjRH8FDXgfOkP2SDuXt0DruIkOvZoSMR-DjLLqjvT0Enl8ZeBlA8-n2myZscuvxLWdXQWVgV5ulCeDWLBBhfollo5ao5r5Kr0In3UwJQYggXZpCPsGD3PB9zyWiA-ik-DBdjgf9-roDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyr-RRt-PiXNdSbF7KI5mIZmJxUsqe5VnRA4S97N5t8zOo-J_55BW29IocGadC9UXJGlooj4LmXs_vH_cWkGmSa_lOzkBLPhj81ImZh-8dq79HwQxlZA2xlD7ws5PU_J3As_msA0XDEBueGeL3GiWND--lBnAfyePCYCc3DN6HGx7bQ9WpXJk-YjRG3NSrAKFuabesS2LhW8Z88wiI3QGRqWbbAZy2WEih2RFxfIFE26F7A_9F0tyXBRA5E3EqL_Y5kcun2WN-47wEO-iJ0UmQRWFBv2q4knfxDM3XITqgBzhwWDc5gNFZ4Tppqs_UV7Vv-Faz0jn69kzZxqEAh5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI38umdr4LCmYvF2p60GCkdhuMtDEFuViK8xEh1xYQrkSWYTpzTJfO5QMWJrTbPfotaWt39m9RlEU4rInU1Kwx7aKRJfRBjRq7QHedmYplC39EYQTeRRGsctZQb_OCNIgLBvwxqKiqCURzZ_uEqiEtinsSghqHMhwbP83sTydbS6SfozTi3Gxd4811OlERPBZIe1Z-NFwDcFpXv-o2pymn06Ro-PL-MZmlbWycfdvHwB3Od1biiVHvVeY1jZjWUUdfQ1Qzxq5myAFOEL8SVkQd1DthTSjg0rl_X7YEMi6_f2iJtByJT9uva5YR9qJnk9R14UQBOLVq6Q6YRZHwabhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19811" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=ruMP7pWuvgRwFYGs-r9zyJDfW-y-JRRFLipTLFM1RqI-IckhimE6-Tm4E1mr6zRE0ZgPiL9oyd7qEAtDtWkkx1lB10UXW7Il9GT_aOjwbcC9Sx_bvdNkUvPNRcnOoeRToWo7uQxufBvRALxcIe4OP8xKfFFRIaNpzf-Wjy6sYzUfUo9vmbKMWRHbyM3GQquPiN1wEZnwd6x-4gNbLjdMigiXeJLUi6q2llnxnmgr3Rfwg5sbut9ghUT0a7YMVOeX4o7-L1d4YDuxw8ebHOWEgABAX8VvqhwrbpYW-v-w5oYihm4TvHZE6wA0l61uPvSsB7l8y07a9FhywB5ijFTWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=ruMP7pWuvgRwFYGs-r9zyJDfW-y-JRRFLipTLFM1RqI-IckhimE6-Tm4E1mr6zRE0ZgPiL9oyd7qEAtDtWkkx1lB10UXW7Il9GT_aOjwbcC9Sx_bvdNkUvPNRcnOoeRToWo7uQxufBvRALxcIe4OP8xKfFFRIaNpzf-Wjy6sYzUfUo9vmbKMWRHbyM3GQquPiN1wEZnwd6x-4gNbLjdMigiXeJLUi6q2llnxnmgr3Rfwg5sbut9ghUT0a7YMVOeX4o7-L1d4YDuxw8ebHOWEgABAX8VvqhwrbpYW-v-w5oYihm4TvHZE6wA0l61uPvSsB7l8y07a9FhywB5ijFTWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19810" target="_blank">📅 13:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc-ksY_7LKG_n30z6bh7Wq5d7AnYWldORkBpZHugiWIoKIiFsVh-5SokqjrGOMhWr5eHLF2qXfCTnWWKNZmiXmgywS8mrjKO3_mh0OlMewbDTOaDgF9LeYPuBYt3W6uk5GHWFla4ij7MY96OwohMuGB4rBkMw37cs4kDYvGd-CfVpzPuBA2g8ZyxXEsjoA7PQMmE0AaH525nROzdxxVr0rWV_-aZTmkg8zYCfOKolcnCsmslPJVFEa6zzX7s2WwWT9EGJw9D6c8mzOWyxXR2039K_AwlxcAeNuN_lo4h4lt2hlKCp5F-VNsljr_ih_Umlir79eaYLiCNJDGPciYc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19809" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19808" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی اسرائیل گفت: «باید کارهای بیشتری انجام شود. من امیدوارم که دونالد ترامپ، رئیس جمهور آمریکا، متقاعد شود که ساده‌لوحی خود را متوقف کند. او یک تاجر است و در مورد مسئله ایران بسیار ساده‌لوح است. هیچ دیپلماسی با این افراد وجود ندارد، هیچ چیزی برای صحبت با آنها وجود ندارد. باید با ایرانی‌ها از طریق دوربین صحبت کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19807" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19806" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19805" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jimHdjDWThb19yJ_bRI99jI4dkJFdeRImt9e3GIMIfbCVLj5eovaLzKCn-gZCR0LTpCYyLoJi1xGaBrJF_AD1fq5L5b6hqvoVRj-gUy0WdLKu_XCSBzLpZxxHqgEBoc9A5qyBWNAM4jaKpdODTzF2fNXjtC4MeXifiX9bWsbbu3yP4e7Vvuv8HQbHU2jQcL1VfMilUnawGBvWMgs0c30lFLn7gTUyhnBNCleWNggqoNR-l031K36Ns-FLxFnSWmi4ULm_T13LaUU7ZaPzmXkEkBx0DQQcO9L2x-oRKKlaY0puZIEUIM4grBr4w8-8dtXSEgXHGOn9shfifiWR3nrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اطلاعات ۴ مرداد ۱۳۵۶. دقیقا سال پنجاه و شش هم همین موقع ها، هتل هیلتون آتش گرفته بود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19804" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19803" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=Lae0n2FVqwuKwCFjzp1tQL3Tg2rEXpaNqgj78ftg3pFIr3tWgaXbS1g6tUQ-90t0dDnpHFkOGxg6E_cJ_oCHPMxa0UJ1IA5cOPansZYk5pCESFgQTRBsZqjpm0b8BRSfX7zTsegqMsasAN4sJG0w3hy2u3iW3BoY5UKoypdL2Bwz65pplZ7bhYbPEsJn8oEQrnKILjHKOxUXxXVyKuekNUYw_IP_FoET7NBuiJf1LfYYvRDP_8VFyr4KrnzfS8rZP-TdUfLbwaeM9T92vR9-2KoiuRUNktXWDXBkoqHD6ucZkNm5XCQkXJR-YUs1dIRLZf60ODbfIseaRKQqcb65Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=Lae0n2FVqwuKwCFjzp1tQL3Tg2rEXpaNqgj78ftg3pFIr3tWgaXbS1g6tUQ-90t0dDnpHFkOGxg6E_cJ_oCHPMxa0UJ1IA5cOPansZYk5pCESFgQTRBsZqjpm0b8BRSfX7zTsegqMsasAN4sJG0w3hy2u3iW3BoY5UKoypdL2Bwz65pplZ7bhYbPEsJn8oEQrnKILjHKOxUXxXVyKuekNUYw_IP_FoET7NBuiJf1LfYYvRDP_8VFyr4KrnzfS8rZP-TdUfLbwaeM9T92vR9-2KoiuRUNktXWDXBkoqHD6ucZkNm5XCQkXJR-YUs1dIRLZf60ODbfIseaRKQqcb65Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتل در حال تخلیه است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19802" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5G9RPyINcBo75svDWC3cbI5Wco7uOq2qA0s_Cnd40mZNgLlIV6Rnr5ckMId_VR_MQVlZTs3etVSgcp0B1MpHBEMNvAIZ0gyOH5kac3U9VVec-R9zJlpTgj05_p4k8eGPMhwc4amTzAaqBR0h_fY6Ks5SS1pyhdZRgssDrzt-F2lZoP2ZXOK9H4Q8Vl31WdCO_E1n29JtYkiKLaUwtHQVge7Oln56kM6_r1RItyhDsvBskJU-wZHyPaY4S3pd73c_7s2ucUjGu3mfF5MPIGZ7HIe_6PNScnMmI-OwR4L2uVhgh9OvPNigC4MYiY1bBu89nU9jHr6T5EF0A0vr9lBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی ساختمان هتل هیلتون
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19801" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جمهوری اسلامی  : تنگه بسته است
سخنگوی وزارت امور خارجه ایران گفت تهران به واشنگتن اجازه نخواهد داد شرایط پایان جنگ را دیکته کند و هشدار داد که تنگه هرمز همچنان بسته است. او همچنین اوکراین را به دلیل حمله ادعایی به یک کشتی ایرانی تهدید به تلافی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19800" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=PLP411kNbgyyNIlllCLgbfyc7DWm2waQe0-KjFeZVwtZsEzGJuZq6QjmwJPCesk7GcfP8TDkoCbKTBCsl_N4LM7eU9rrxWdHFSngbD8B87tdNw8lcc-yS2U8yjeDWxr01Jxv8jCrUxhS4ub8XO3IYvVgi_a1UFL5WphmFonYHLPlLRe5jkjs8m-F90iE1jZbxk_RH2I_h-vdJ3UBpd7SvmO9Worcg5QcEgCtCok5b666nNfly7u4gDke63mR4I7Pe_wv09HqVtPM5XAPjF4krFT6TmIU2A7gP6f-ur3ymNDe2EmylrRcDIttb_QnJqQypx2A1yl4M3RZuCVjAOW5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=PLP411kNbgyyNIlllCLgbfyc7DWm2waQe0-KjFeZVwtZsEzGJuZq6QjmwJPCesk7GcfP8TDkoCbKTBCsl_N4LM7eU9rrxWdHFSngbD8B87tdNw8lcc-yS2U8yjeDWxr01Jxv8jCrUxhS4ub8XO3IYvVgi_a1UFL5WphmFonYHLPlLRe5jkjs8m-F90iE1jZbxk_RH2I_h-vdJ3UBpd7SvmO9Worcg5QcEgCtCok5b666nNfly7u4gDke63mR4I7Pe_wv09HqVtPM5XAPjF4krFT6TmIU2A7gP6f-ur3ymNDe2EmylrRcDIttb_QnJqQypx2A1yl4M3RZuCVjAOW5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در
۲۰ و ۲۱ بهمن ۱۳۵۷
در پادگان‌هایی مانند
دوشان‌تپه، عشرت‌آباد، حشمتیه، لویزان و مراکز دیگر
مردم برای تصرف اسلحه وارد پادگان‌ها شدند و تعدادی افسر، درجه‌دار و سرباز را کشتند !
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19799" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیدار نتانیاهو و زلنسکی با ترامپ
گزارش ها از سفر قریب‌الوقوع و ناگهانی زلنسکی، رئیس جمهور اوکراین به آمریکا همزمان با سفر نتانیاهو به آمریکا
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19798" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkMa2tjEuVtwXScgeMEcsccMbonOibuaTJR_9xALs0BubIzCdhrEseWLgUgOsvjAXRqSK8TLgtV-xSup-MU4bTexlvg80vTZPHL12tjZ6yckcXFr88aHm-7II1PuJEQ8pHcUxah7UWmg6X5m8081heViEyKrpzO6712PSDWn8BP8yJ2Yj9-lHDLPpTL60M2lSadqGrdP631X0MRyKb9fAj5MQwvVZDbArlKIt77XKrPk2G7NiOqsZ4fCPBh3HPhXbYp_pFM5-dZuAYOOAUzaYREi15tgnHiM5X1Wlhi2_53QdCMJQHRAj957_nhtaF-R_INLQ_N-Y08PK54PXFL89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=MCSmpeO_1qFq395tQgZwQykrFwYO9CCaB0kdv8RFItuW-YzoY-JDGcJB-aniVhFjO24UJgb_LvNtplXwVS0ZCSscCR9Ufj_coxatFmCa06Hq4drVdt3qmfuiQji7PTOR4JxJmmxIrJcPhVOmrssw4Vyd45-GNNOq6h1v3lJ_G7Td2mCmnlD0WkFMo2ccfKirHiGCHbdsjO3KCtNsP2svBij0yZfXNmBW4jcRhgQJP5JLmI9VQh6doVEvNWEvH_UBKmOr_fmDYTsFeEKK-aoITORK3JwKyFNIpbna_C3Y9TUCc3tM5bRHRoTMs_ztvp8AQUerGaizfFHeXmv8ZhltUTqmnbCKjkEXeGIZT8OAwmR5cgZtRUoU2ZL4m7jJ7GMmCb6g6DAH78P4Nk2cCZDiSDNgSkXkNSm25GJRxaamFQAUWfBo06TOYyLfHtx_gulXUsDXhYvHbKXzhUfiLkKmnVhbtObvL3clmsmGnxYarghS2V08UzfJeqI7VXeb-NKZm1qW4LhUtE5OEuIeIoUbemtZgrS8uElDsTy55ghTRpFwwGdgX5p0smHU8NYKvs2gcy8wF6AR6uG33UmdWKK7gkedhTNv-NSStbLb_p3QnJoGGZdf5a-gijjkujxyqT8DHEvoJ3RiQ41RVxVCheRSlugZXqlFiO0stEOq7jMMUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=MCSmpeO_1qFq395tQgZwQykrFwYO9CCaB0kdv8RFItuW-YzoY-JDGcJB-aniVhFjO24UJgb_LvNtplXwVS0ZCSscCR9Ufj_coxatFmCa06Hq4drVdt3qmfuiQji7PTOR4JxJmmxIrJcPhVOmrssw4Vyd45-GNNOq6h1v3lJ_G7Td2mCmnlD0WkFMo2ccfKirHiGCHbdsjO3KCtNsP2svBij0yZfXNmBW4jcRhgQJP5JLmI9VQh6doVEvNWEvH_UBKmOr_fmDYTsFeEKK-aoITORK3JwKyFNIpbna_C3Y9TUCc3tM5bRHRoTMs_ztvp8AQUerGaizfFHeXmv8ZhltUTqmnbCKjkEXeGIZT8OAwmR5cgZtRUoU2ZL4m7jJ7GMmCb6g6DAH78P4Nk2cCZDiSDNgSkXkNSm25GJRxaamFQAUWfBo06TOYyLfHtx_gulXUsDXhYvHbKXzhUfiLkKmnVhbtObvL3clmsmGnxYarghS2V08UzfJeqI7VXeb-NKZm1qW4LhUtE5OEuIeIoUbemtZgrS8uElDsTy55ghTRpFwwGdgX5p0smHU8NYKvs2gcy8wF6AR6uG33UmdWKK7gkedhTNv-NSStbLb_p3QnJoGGZdf5a-gijjkujxyqT8DHEvoJ3RiQ41RVxVCheRSlugZXqlFiO0stEOq7jMMUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Eyk09zfifDhN3auzk4ss0LYsfS4nNv5ER8uzRVSd6QdH3VAyq4v9IiUEZbsIJQd4Z0FAw1YPFo7CkH5tmm8lQs_JFv8IOPbKLVmhasVL9NJmRejSuButAeDczEKWUD-zBKvVgvw8MBFdSxBQSqrno5N-ye6ErperQHrkfGXuNgv-JwEV1N_Ork9NTQOMyUKycqWn1SxomKdvL5IAiCEXsoa4EKyuN9Z1iLtzRA6hyvUBhiP9VCHyJf6oIOD56Ld2WNo0zVjGyCwXPJnUP4PD5guUdccziCHJVfYP1-zOb8aGQj1zzmfNA6zFvAmU7nyb9Lq23-EbNUjr23lpvk7d8ZUvCCzittQthSFD9HLtvoRpBsUrfOomFa23r6AqwvKNIUN6CDXvI4Ul3yeWuuewOsCjvvtXJtMq_UbiAY-KaIHCCwPwb74uS9bBRzETpltM-0HsLLkIMRlExLRXrWrwjKo_p7wZDfAubF1VAdEjwyVy7Y9YCge3l5SSi_GDdxOntLgCMZKQJl6_hRlhOfe0_QILWPPYLxqysGCRFfmALfuMEh0HIAOLn8s4SDzNxED5qKkJSQoz8hXYHhJTjt4CYE_QVjbMxlDfKsvN78803HE-H4tvXJGqzKoOOw9OEd5aeDAUpoaAdtZ3AI_TAWAAu3a84YUPff8YN8ys1tJjU9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=Eyk09zfifDhN3auzk4ss0LYsfS4nNv5ER8uzRVSd6QdH3VAyq4v9IiUEZbsIJQd4Z0FAw1YPFo7CkH5tmm8lQs_JFv8IOPbKLVmhasVL9NJmRejSuButAeDczEKWUD-zBKvVgvw8MBFdSxBQSqrno5N-ye6ErperQHrkfGXuNgv-JwEV1N_Ork9NTQOMyUKycqWn1SxomKdvL5IAiCEXsoa4EKyuN9Z1iLtzRA6hyvUBhiP9VCHyJf6oIOD56Ld2WNo0zVjGyCwXPJnUP4PD5guUdccziCHJVfYP1-zOb8aGQj1zzmfNA6zFvAmU7nyb9Lq23-EbNUjr23lpvk7d8ZUvCCzittQthSFD9HLtvoRpBsUrfOomFa23r6AqwvKNIUN6CDXvI4Ul3yeWuuewOsCjvvtXJtMq_UbiAY-KaIHCCwPwb74uS9bBRzETpltM-0HsLLkIMRlExLRXrWrwjKo_p7wZDfAubF1VAdEjwyVy7Y9YCge3l5SSi_GDdxOntLgCMZKQJl6_hRlhOfe0_QILWPPYLxqysGCRFfmALfuMEh0HIAOLn8s4SDzNxED5qKkJSQoz8hXYHhJTjt4CYE_QVjbMxlDfKsvN78803HE-H4tvXJGqzKoOOw9OEd5aeDAUpoaAdtZ3AI_TAWAAu3a84YUPff8YN8ys1tJjU9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیغام های زیاد گزارش انفجار در‌ اهواز
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19783" target="_blank">📅 02:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19782" target="_blank">📅 01:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjKHNxktWCokqGThByZdKw9bB3SsLOWaGi5eIqMjZaMm72lecrDIXcIIwMI-8ws2GHwtvaQsGKo5LIK-nTQKHiEXKLF_EmXFdN2j6c_VyL-EECcA1xMLuR36neTDIVSY-R3Zb9__ppNasPE-Ml66wKH9V_1ge-cDOkrEd3TRHiUILx_sEGpIqhS-tCCvuqsOsZbwVMYBYDQ757mGzJCQl0nM40mdJcLjy1n7e7bouKLG8kFbl8xSBoI6ifIte7X5SMVrzMnhgmbTws1T1DwcibzgsSbNni4HFEakhEnUvFKAcT1B6DSPCMHP_Ykck2gW2p8-eU6-EY6W1NwE4sSHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سایت خبری روسی مبنی بر کنترل مافیای لوازم آرایشی توسط حسن روحانی
رسانه‌های روسی در چند ساعت گذشته با انتشار خبری جنجالی از یکی از بزرگ‌ترین پرونده های قاچاق سازمان‌یافته آرایشی-بهداشتی در غرب آسیا پرده برداشتند.  طبق ادعای این سایت، حلقه اصلی این مافیا حسن روحانی؛ دیپلمات‌ سفارت فرانسه و فردی به نام مهدی‌زاده بوده‌ است.   طبق گفته این سایت اخیرا و در طول جنگ ایران و آمریکا دو کشتی محصولات قاچاق آرایشی تولید کره جنوبی، متعلق به وی توسط دستگاه های امنیتی ایران کشف شده است. این در حالی است که چند کشتی تجاری نیز در سال گذشته توسط دستگاه های امنیتی جمهوری اسلامی کشف شده که با دخالت سفارت کره جنوبی و پیگیری وزیرخارجه کره، این موضوع رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19781" target="_blank">📅 01:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه های نظامی اوکراینی ادعا کردند: در صورت پاسخ نظامی ایران به اوکراین،ارتش اوکراین حملات پهپادی دور برد به شهر های ایران انجام خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19780" target="_blank">📅 01:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19779" target="_blank">📅 00:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جولانی: حزب‌الله به مدت 14 سال، رژیم سرکوبگر سابق را در جنگ وحشیانه‌اش علیه مردم سوریه همراهی کرد و باعث آوارگی و کشته شدن تعداد زیادی از افراد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19778" target="_blank">📅 00:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19777" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19776" target="_blank">📅 00:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSG1wYhdC7tdkzlusLmvXqYhDQWNwbxJRmD-Qf0axosebRTPizFW7rk-GnLjZy3ZuSxJyfq_WcTRaY-4os9joekTKynWsO9bk5GeTze4Kk9qQuWlCYFoiqGeJZ8e856SnW-vhveNg0F3JKJt70J70aw4c9o8VHme32Rmmm6qwOX8yfzq3WPGU9kNiIlJrAWuW_hpriWjspntx7LLzYbkSWhxn_vPW5m3tY3X_7MWrntdx71V6U52hoJvCuyKmIyy5b4LYrYj1qiGX9COvak_7WkeBrvotx95Xaii2wuZJDxUI7WpSs029u-AzznIpPO3hWMsVv1MSEYny96EFSSzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19775" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh5ElmZDwYsesA_kBPOJ91qPk2AxwQOUIBEITH9Q7ctRQkQSKymRuybQvSU0cqX_uWXZBX1oxmviPk7jTSaaRGWb_cCC8i2wDMkw8lPnosDPamx85Y67ueC1durcPLmxBCDvXOmItsP3nKkMIfnnflcLcONTD4nuRpezsv-ZZeUXT03hSXUxX8cHZCL_niN-vyctsxElBK0gujLjacs8hl_FpA0zehLBJJYTd4gypguNxBim2jWMgxlJV_n6fZMXVsv72HJsp_fergu3YUMOoI6SLvf-qSkvpNLXckAwMwOt5zBzKQ_yyxqV_wVt_qi4WngAfQmJLF882s18fZTDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19774" target="_blank">📅 00:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plk8wWN8Ie7M9SW64DBnvVW_HLN8KoMMXsdGfVW5vgzoMixH1UM9_Q4-A3jW4QFmxtbebE8SnlMq_RcRJDXKabdU3GF1-ayLabT80sZMRfxmTWgc-uuP5WSsLQAVNMnkkoXsTa8CirZhQxByjcT_A7jI6tqVEAwSQuXHWf6WXwrGRAxhTP0DUcnhk4tUqcaLVRwQLvEgKQTw8r9OuVfQ3F6CrMDFaH75Ywum31GQkBWFXA4dS0NrWuMEU0PqciGPlYe28ncQzWIuotOr8uoDE4an-P4oR83X5OFD2pv9tjmJg2MSyJCi49iDtwuM4OJqwgLh8nQ2-UpUsV19KqKveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : فرشتگان نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19773" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=lYmHU3y2d-H4NO7eoDC0LzKaI3lQV9D0SO3Y3OGf_nzisOD09ZmPWny6JnosQVwps_SIr_rOIKv2TmprCjzepn3rM5eYzbqoMoH8RSC0sEw0L9Dcaox3BR8Psf-eE92MEB1bRvFPGdgdsytlMaum0khCkjyOmryrUpVowkXYiMo5sZpy59Vf8toj6MFM0UdfI-xLRwtqSkluWvIK8ZJhcvf_8WDRZKPf6saNedQO6GdOo2NN_QG5skD2tUcHGmY90Q7ZTxcUa6qIMBH37gchXjaHEghKiBaWTO4w5uk4Xnv9EJ7Pcbl59axRz5zUmyetxa2D4oUI_dvbynLxr6dZZp2KHseBJio8OKI-EiCGrbGfL22vSfdIJiav_rp3Q7j2qDbpHhuYxcIRu-AgDWgHe1zpiYMoEpqsdwRcKvYcCXedx40ni9e89wA7bjJizoPK-POFNedZiz7so2uhxL_tnJknvgoHAqC9Dw_s7Hwrv8Au05DKmGX6cuEWepCTkAln4XuDdiRNTfnqa-jBnTOwlEDl0NfCJLXX4dCa0NhEtkYvbl3bjV1VI87bfhY5tg2EGytEql_pHetJ9fmYi3vekmhE5j1Nc2t0eZ5Y5hURHckdloiPD_Xm6aZLllQCJAOr01DHXY5forFy5N1k6Ic1pjvWvdRT_uN7Vp1riKOg0NY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=lYmHU3y2d-H4NO7eoDC0LzKaI3lQV9D0SO3Y3OGf_nzisOD09ZmPWny6JnosQVwps_SIr_rOIKv2TmprCjzepn3rM5eYzbqoMoH8RSC0sEw0L9Dcaox3BR8Psf-eE92MEB1bRvFPGdgdsytlMaum0khCkjyOmryrUpVowkXYiMo5sZpy59Vf8toj6MFM0UdfI-xLRwtqSkluWvIK8ZJhcvf_8WDRZKPf6saNedQO6GdOo2NN_QG5skD2tUcHGmY90Q7ZTxcUa6qIMBH37gchXjaHEghKiBaWTO4w5uk4Xnv9EJ7Pcbl59axRz5zUmyetxa2D4oUI_dvbynLxr6dZZp2KHseBJio8OKI-EiCGrbGfL22vSfdIJiav_rp3Q7j2qDbpHhuYxcIRu-AgDWgHe1zpiYMoEpqsdwRcKvYcCXedx40ni9e89wA7bjJizoPK-POFNedZiz7so2uhxL_tnJknvgoHAqC9Dw_s7Hwrv8Au05DKmGX6cuEWepCTkAln4XuDdiRNTfnqa-jBnTOwlEDl0NfCJLXX4dCa0NhEtkYvbl3bjV1VI87bfhY5tg2EGytEql_pHetJ9fmYi3vekmhE5j1Nc2t0eZ5Y5hURHckdloiPD_Xm6aZLllQCJAOr01DHXY5forFy5N1k6Ic1pjvWvdRT_uN7Vp1riKOg0NY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش دیگری از‌مستند او قصد داشته در اوایل ماه مارس به فلوریدا سفر کند تا از دونالد ترامپ، رئیس جمهور آمریکا، بخواهد در بمباران حزب الله لبنان به اسرائیل بپیوندد.با این حال، بنیامین نتانیاهو، نخست وزیر اسرائیل، قبل از این سفر، توصیه کرد که درگیری گسترش نیابد و گفت که اسرائیل باید بر ایران متمرکز بماند و هشدار داد که حمله به حزب الله می‌تواند باعث یک جنگ منطقه‌ای گسترده‌تر شود.
نتانیاهو در این تماس تلفنی به گراهام گفت: «ما در حال حاضر بر ایران تمرکز داریم.» گراهام موافقت کرد و پاسخ داد: «این واقعاً توصیه خوبی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19772" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=FpqpcXKwdzN4Ds1B34AABUgeI4oQ7nIiU4Xv1U2zGDmZ5H-duVkDfle7NQlTR6KcYLC9YmrRqPtGQZqwaaUXAekP-E7O9vjgiUqRfINiFW4hjbAc-xwzOxbpNmIaZ63ixQnQm9X57MncCC67-n8UMjyXE7M1G8f80gpPtguxkMvG0PzPrfxYfDgHhw1WJc7KAKVYD4i6ZFTzP3p884h0vVAoKKoH0oFZyghYpDpgilYzOlSb-0hDy81NyAdUYnljHRtY7PSAkVFOdgnLfmlY2sXN4uVYh0xBo6giSC7fh32PNq3XF84uN2retOJpAiWn6q8T03STeHPayfcPs9SIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=FpqpcXKwdzN4Ds1B34AABUgeI4oQ7nIiU4Xv1U2zGDmZ5H-duVkDfle7NQlTR6KcYLC9YmrRqPtGQZqwaaUXAekP-E7O9vjgiUqRfINiFW4hjbAc-xwzOxbpNmIaZ63ixQnQm9X57MncCC67-n8UMjyXE7M1G8f80gpPtguxkMvG0PzPrfxYfDgHhw1WJc7KAKVYD4i6ZFTzP3p884h0vVAoKKoH0oFZyghYpDpgilYzOlSb-0hDy81NyAdUYnljHRtY7PSAkVFOdgnLfmlY2sXN4uVYh0xBo6giSC7fh32PNq3XF84uN2retOJpAiWn6q8T03STeHPayfcPs9SIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر مستند منتشر نشده نشان می‌دهد که سناتور فقید لیندسی گراهام در اوایل ماه مارس پیش‌بینی کرده بود که دولت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «حرکتی تقریباً برگشت‌ناپذیر» ایجاد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19771" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وال استریت ژورنال
: ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه پس از دستور ترامپ آغاز خواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19770" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کامنت جدید زیر پست بی بی  : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRKUnvs_mq/?comment_id=18097108343207051
ترجمه : بی‌بی، مردم ایران بسیار دلتنگ شما هستند. لطفاً به هر روشی که صلاح می‌دانید، این بار پس از وحیدی، کاری کنید که روحانیون تندرو نیز یکی‌یکی از این دنیا بروند و ریشه کن شوند . هدف قرار دادن زیرساخت‌ها و سربازان وظیفهٔ عادی، که خودشان نیز قربانی این حکومت هستند، فقط رنج و درد مردم ایران را بیشتر می‌کند.
ما شما را بسیار دوست داریم و از همه تلاش‌ها و زحمات شما صمیمانه سپاسگزاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19769" target="_blank">📅 23:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کامنت جدید زیر پست ترامپ : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRJwPPBPaP/?comment_id=18108319289002859
ترجمه : لطفاً به‌جای هدف قرار دادن زیرساخت‌ها، که تخریب آن‌ها تنها موجب رنج و سختی بیشتر مردم عادی می‌شود، و همچنین به‌جای سربازان وظیفه که بسیاری از آن‌ها خود قربانی این شرایط هستند، تمرکز خود را بر سران حکومت، به‌ویژه رهبران مذهبی تندرو، قرار دهید.
از تلاش‌های خستگی‌ناپذیر و شبانه‌روزی شما صمیمانه سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19768" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSEpK81stmw94wI7Si9tydF5k2cQeea_eB7fInIY-kujOzFgtaTPA0tSxJVyYTyQD51T6vrJUX7mY1uURNbzPQbEG6tkLemLu8lLs16MK9IMUDHX6gCrLQyl8io0GUyKuoqhzGnEbu_ViqVjFafEOXnzsvEz1Tsr2BLTkVUy1G1iFb7rjhGVaBZ_l_qLQqDBBFM_g92iMzhhuYm33ONjw-Gn6QndRljvMu3avZ9kin7UWQ87kDou5Lvd77tguDtPNx1JUnuwMohufAQN1o2MqIpQbB1sgLRr4rySh5A9ja8zWWlELcJQCjtuy4KrNKvwIEnwscm4KLAaTGjWW8NUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : الان دیگه نفتکش ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDZwKUI1NSr_MlmLMRQDvXOa6EAfljf7CjwbDU0zvoEf6PbSJctx2MQ81GUA6k38ZZyZnkA9JczGLlWUtg2V6xNaSJhYUQIndkgJlpZ2n6uWlHfQ6nSPANW6i1mP7KXvcYynHScDW20j6_NOMcuJMMPgsGXJkMlumDC639vy8PbAHYtjAOmK61yDBUFq2a7jH8VFTWI9ldsBeVyV0-qKB-gWaXskEOrmy7QhQ4Kkc49xyozjGPyYsJgv20Bl60F4YpPTDUzDSLjEw3uGmznkXCoLAEVqxmskKSBnYjSFVpD7cZSTQKeSStSawhaJVigI93dSkp0tJdty9Rn8YIoyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حمله هوایی به جزیره خارک
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19766" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19765">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=QxAwdN5axtQTNwI546ISO7bcDcSfnbBe4APpkE9tXLGfy1NnUXtGmD6vGZflgNqhsfdXWAbvVMWmMThoVxCZkUcYM232BClKxD9DT7Z9aPzvh4AhEqyEofGedspNBVjXijhUoIX0ThILlSW8prrNddIENQkHoMu1uzG8sdNOKPDUpxJIg55EIRwiLwTGiKbaYdA65I8GPXx2treHX_CU4BRwCC0aWf67Y9S7gzPb5xNmJCxl0DN_1Gg0weloGwXF8kSI37OYK_fIFcA8q-PLAqeuhJeAzGXfzvnMhqG9lsAJ7mQAYvkZ7MvFkKIbiPGncKRNmMgY6gy2znFzhJAdrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=QxAwdN5axtQTNwI546ISO7bcDcSfnbBe4APpkE9tXLGfy1NnUXtGmD6vGZflgNqhsfdXWAbvVMWmMThoVxCZkUcYM232BClKxD9DT7Z9aPzvh4AhEqyEofGedspNBVjXijhUoIX0ThILlSW8prrNddIENQkHoMu1uzG8sdNOKPDUpxJIg55EIRwiLwTGiKbaYdA65I8GPXx2treHX_CU4BRwCC0aWf67Y9S7gzPb5xNmJCxl0DN_1Gg0weloGwXF8kSI37OYK_fIFcA8q-PLAqeuhJeAzGXfzvnMhqG9lsAJ7mQAYvkZ7MvFkKIbiPGncKRNmMgY6gy2znFzhJAdrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏واکنش من به تحلیل‌های احساسی مردم:
💥
«ترامپ از رژیم ترسیده.»
‏
💥
«ترامپ با رژیم ساخته.»
‏
💥
«مهماتشون تموم شده.»
‏
💥
«ترامپ ارباب نتانیاهوعه.»
‏
💥
«همه‌چی از قبل هماهنگ شده بود.»
‏
💥
«اینم یه جنگ نمایشی بود.»
‏
💥
«فلانی با یه مقام امنیتی در ارتباطه.»
‏
💥
«چین آخرش همه رو غافلگیر می‌کنه.»….
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19765" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19764">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f4990448.mp4?token=jhN5VGVEiSMsxflKSyvuWSt8gLFmBv7eH3-3MH13cpMWZEbgx-qAkEB40JUHjbKU0HOwn8RjvaX9ZlQE8sp2lvxhdNxQC1gSQIbMx_fcWzgweKizbUgWAFcnGH4PUL-ExkGqjn8oWHb7RmE1J-eLZpVWVUxj5cvBZkF2fw462izOneEe18ljbvSdYQJV1RHaOflynfxcnvt4wKt1-VpoAhfNJGbZzQF_S5BiQCzf-6YxU9LH6VC-wbmTkm_n6_tJ4TOJuNvrDxzR15JtAimAvxs7FW3duwA_hVruDu9KqPogWjZmnL-IHISqrZNSdCwDF-pxpzhrXyBA2Rx2M7X19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f4990448.mp4?token=jhN5VGVEiSMsxflKSyvuWSt8gLFmBv7eH3-3MH13cpMWZEbgx-qAkEB40JUHjbKU0HOwn8RjvaX9ZlQE8sp2lvxhdNxQC1gSQIbMx_fcWzgweKizbUgWAFcnGH4PUL-ExkGqjn8oWHb7RmE1J-eLZpVWVUxj5cvBZkF2fw462izOneEe18ljbvSdYQJV1RHaOflynfxcnvt4wKt1-VpoAhfNJGbZzQF_S5BiQCzf-6YxU9LH6VC-wbmTkm_n6_tJ4TOJuNvrDxzR15JtAimAvxs7FW3duwA_hVruDu9KqPogWjZmnL-IHISqrZNSdCwDF-pxpzhrXyBA2Rx2M7X19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار: آقای رئیس جمهور، امشب کجا را بزنیم؟
ترامپ:
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19764" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19763">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoEsHhsQzRKkQ3tFmyYlGT9hRlNty3n4BnLUIdkuuOKevbYypP9G0Yusu3aJjGaRUobC9y6m5uIg5n1NXBeanajIY3kl38b6pzULyQ3KGStp8sCyyWnaVx2idxOc6a8WTDvnapU13EZeaX7yDhzqf7H9yy-Go2jzGkqVyIKeLj29om1GdvXHfhOHDbLU8OlWGXyGOzmSx4xaEbX8spkSwagLVeWjabeu9hLyfIq8NcMU06AFYt1X1JjdDYAcWHMxmAv3DpRBNabFjZbgzN_UK5zUxdISVC0oKSda1pd9Zqgk_4nfyal0IkBWXqRCZlZESjzBOlj01iDJTvouQ2NGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آگاه : اوکراین را ادب میکنیم
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19763" target="_blank">📅 22:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19761">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk4t0vkg8k39_1Sw4Lhb551wecUT1z1zKTJ1I8YQxwBq_M5De39-ZfSDGTipdT8DsQhVBEQufES9w3-vvKT78teQRbRlz42LT2OvR1pX1QEwfVrBtScRqshw1Cnd6MJa8GYSPfRn66SSEzsQ5wqlE9qASXaAGAab2v5WI4SxjcadovkJ8Yqx3OYvRKN3sENW6cyMkxAPr0CUwOfXbNZ75CqN3vgh5z1OKvAv0ShyfYp0bA0aXiw3wv2O_L88fj87jJNP99vEE9-ZGmHbkyJbMRVbqsyc7GXr1RiPghygUgHSPgbOf6wkk2unf0lPKKM0eCtIJdRXe53OAvROTmHa9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضای به شدت شلوغ و عرفانی حاکم بر منطقه و یک دسته حوری جدید که از اسرائیل به سمت خلیج فارس میآیند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19761" target="_blank">📅 22:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19760">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراقچی: تو عراق به من میگن عباس قهرمان
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19760" target="_blank">📅 21:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجتبی خامنه ای: ایران حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز اسرائیل را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکا قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19759" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19758" target="_blank">📅 20:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سی‌بی‌اس
:
بسیاری از آمریکایی ها احساس می کنند که جنگ با ایران به خوبی پیش میره
این احساسات به طول جنگ، ارتباط در مورد آن و تأثیر آن بر اقتصاد مربوط میشه
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19757" target="_blank">📅 20:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">العربیه:ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است،
هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19756" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش CNN: عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز را داده است، مشابه مدلی که در تنگه مالاکا استفاده می‌شود.
پیشنهاد عمان شامل یک مکانیسم پرداخت داوطلبانه برای خدمات ارائه شده در تنگه هرمز است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19755" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سی‌بی‌اس:حملات آمریکا به ایران به دلیل سفر مقامات عمانی به تهران در روز جمعه برای انجام مذاکرات، متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19754" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در ابتکاری خوب برای کاستن حاشیه‌ها، شاهزاده رضا پهلوی تمام فالوینگهای اینستاگرام خود را آنفالو و فقط خانواده و پیجهای رسمی را نگهداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19753" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سفیر ایالات متحده در سازمان ملل متحد به شبکه ان‌بی‌سی گفت: مذاکرات با ایران در سطوح مختلف ادامه دارد، با وجود اختلافات موجود در داخل رژیم ایران
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19752" target="_blank">📅 19:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=p3ZXYdK248Z8hdkN_DM4sgUwwro3SZF8sEDGTBT4Lq9_TlUPotsPR6GlyG6RUQ1K-ALVPnzhDLXnVt59CsWTLjDoubHSoNRiw2dkOyXJLd1EcKc6EQyuTryoKaaTxyq1xLstTofUJInu5PRZRiD8hjEjsSAQxvAK9K83bkI6j9Bla3aC5ihS6reZNv-X-V5a27gVqnqVDg0vQkMzklKXe5jhEF1T0XuXSNGbBHDrgrw4di4ocPolCDmyHREC7APfEuMVN8VvNkMrKo8DlpydEGUrZaX_Yb1ZEgKdpART34I3kQ6-bpUKmQAa_Nk0X83hlEIjMYCufkCUfKGsUJoAzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=p3ZXYdK248Z8hdkN_DM4sgUwwro3SZF8sEDGTBT4Lq9_TlUPotsPR6GlyG6RUQ1K-ALVPnzhDLXnVt59CsWTLjDoubHSoNRiw2dkOyXJLd1EcKc6EQyuTryoKaaTxyq1xLstTofUJInu5PRZRiD8hjEjsSAQxvAK9K83bkI6j9Bla3aC5ihS6reZNv-X-V5a27gVqnqVDg0vQkMzklKXe5jhEF1T0XuXSNGbBHDrgrw4di4ocPolCDmyHREC7APfEuMVN8VvNkMrKo8DlpydEGUrZaX_Yb1ZEgKdpART34I3kQ6-bpUKmQAa_Nk0X83hlEIjMYCufkCUfKGsUJoAzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین قاتل، اشتباه وحشتناکی مرتکب خواهد شد.
زیرا پاسخ ما، پاسخ اسرائیل بسیار بسیار قاطع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19751" target="_blank">📅 18:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مجری فاکس: در مورد هرگونه اطلاعات جدیدی که ممکن است در مورد برنامه هسته‌ای داشته باشید و قرار است به ترامپ ارائه دهید، چه می‌توانید به ما بگویید؟
نتانیاهو: قرار نیست من اطلاعات جدیدی ارائه دهم؛ فکر می‌کنم خوب است که فرصتی برای نشستن با دوست خوبمان، رئیس جمهور ترامپ، و شنیدن آنچه در ذهن دارد، داشته باشیم، زیرا فکر می‌کنم از بسیاری جهات، این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19750" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بنیامین نتانیاهو در گفت‌وگو با فاکس نیوز: برنامه هسته‌ای ایران باید به هر شکل ممکن پایان یابد؛ چه از طریق توافق و چه بدون توافق.
این جنگ زمانی پایان خواهد یافت که یا نظام ایران سقوط کند، یا آن‌قدر تضعیف شود که به این نتیجه برسد که باید برنامه هسته‌ای خود را متوقف کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19749" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مطابق گزارش رویترز، به نقل از یک مقام ارشد ایرانی، در تهران، میزان تردید و بدبینی نسبت به تصمیم ایالات متحده برای توقف عملیات نظامی، بیشتر از خوش‌بینی است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19748" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19747">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت دفاع اسرائیل اعلام کرده سامانه لیزری پرتو آهنین پس از آزمایش‌های گسترده، در مرحله تحویل/ادغام عملیاتی با ارتش قرار گرفته و به‌عنوان لایه مکمل در کنار گنبد آهنین استفاده می‌شود. این سامانه توانسته در آزمایش‌ها راکت، خمپاره و پهپاد را رهگیری کند و هدفش کاهش شدید هزینه دفاع در برابر تهدیدات ارزان‌قیمت است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19747" target="_blank">📅 17:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۴ اسرائیل:داماد خامنه‌ای سکوت خود را در مورد انزوای مجتبی شکست
رئیس سابق مجلس ایران فاش کرد که مجتبی خامنه‌ای «به دلایل خاصی» تمام تماس‌های خود را قطع کرده و در بحبوحه سوالات مربوط به غیبت طولانی مدت رهبر جدید از انظار عمومی، تنها با احتیاط گفته است «امیدوارم سالم باشد».
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19746" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19745" target="_blank">📅 17:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک منبع بلندپایه به الحدث:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه
«آن را به تعلیق درآورده است»
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19744" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الکساندر دوبریندت، وزیر کشور آلمان، در بیانیه‌ای در محل حمله به رژه همجنسگرایان برلین گفت: «همه چیز نشان می‌دهد که ما با یک حمله تروریستی اسلامی روبرو هستیم.» این وزیر افزود که مهاجم مظنون به استفاده از قمه است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19743" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شبکه سی‌بی‌اس نیوز به نقل از منابع: مذاکرات بین سلطنت عمان و ایران درباره بازگشایی تنگه هرمز، پیشرفت‌هایی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19742" target="_blank">📅 16:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19741" target="_blank">📅 16:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدا و سیما
:
جمهوری اسلامی بارها هشدار داده است که هرگونه عواقبی که ناشی از انحراف کشتی‌ها از مسیر اعلام‌شده توسط ایران باشد، مسئولیت آن بر عهده‌ی آن کشتی‌ها خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19740" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
