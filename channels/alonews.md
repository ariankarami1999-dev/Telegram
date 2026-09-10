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
<img src="https://cdn4.telesco.pe/file/CzkjVa6VyTe59Ds_gIgwgwN8Udr1tguE2C38FUVeLAl3eM77rBwC9jSvlSnBZeY21cj-jeKASVcd1wzT10UVHfw2dCSQSOgpTMIkqIUXjaZIemVAshxTJmn054mIuI9UJ4Qmq-Ru-jpZeW3r7oCo85M7liR0meUnNexH9ak2piffYKmn94OvX93Q3qaNkYlKVQpC0WiFA-AKmy6FhaDjDHnAfvR1Tjpn1Kne9qpZ1Lq4hDkwtKtKd2SqHtu5d9W7Fnm2PqBQ9y6qnHtr7kh0VAy3xWdVcuhRNAleDVWiu5MkW4yfjZ4Yl4d7ldSD8-C4vaH2AJZxVnj6GU25dz4P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-146757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/alonews/146757" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB3vvhKMP3Hd8gI5Ex081YcPcr52f98mlz37QrblTvfikLUh71L8u9DhN-x1AmJ9w8sdRlc5IaEpwrtl5D-xs-LX1zOMFMSYQx6CH6mcw9QC9znbTBkCdkPypHavm4fV5jfRpr2dm9nm97MQ7QBzh-fvObIM_q-V11GrSYnmw-GoWKN7tLpJ-yKpmUPpOUdGhe5RrFuDAYgNwwJTGGU3Itelh9kesDoeP3c4Qu7fE0UpM4QHCxoYO_ItOGmEoQXbqBh_Jiu3PwM7VhhkL8HpHd9-4OJsWp4p_FIWkRuAXdoDDANZtWcI3rceBw63XUq9qP0aVdD3yJLSRpx197m3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مصطفی نجفی: به نظر می رسد حمله سنگینی علیه تاسیسات هسته ای در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/146756" target="_blank">📅 22:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/نتانیاهو: نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146755" target="_blank">📅 22:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69ef09a20.mp4?token=eHdhy4a1WE7b5UQ3alT4c4bZr_-sndzumWrO_GcbFS-01-qbh5tQrKi6o_bT-l784E9IHU4-flvLnV8c55cCGhQKHbSrKBEtrVCGuFSpGhTqMhqEWyz1RqM4qcwWsNK5vW_YJ0jTdl0FmrWxBn9JnNQRi1xuo0QTSO6ZOZ-IKN2IDploAodMDK_OfweiiRfvXU3OrzXSBGtamWqleEYe0e-U4H2QJqXugradb5DA7YlejErzgeIwp0-T6HJdcENxRwWdbY9tT7-J-0wnnUT46iHIDIJosvui-AEpSpIGdKEIarwWGnn35sEyPDDrXgkPuQnnDw0Fhubaqfba_TKRVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69ef09a20.mp4?token=eHdhy4a1WE7b5UQ3alT4c4bZr_-sndzumWrO_GcbFS-01-qbh5tQrKi6o_bT-l784E9IHU4-flvLnV8c55cCGhQKHbSrKBEtrVCGuFSpGhTqMhqEWyz1RqM4qcwWsNK5vW_YJ0jTdl0FmrWxBn9JnNQRi1xuo0QTSO6ZOZ-IKN2IDploAodMDK_OfweiiRfvXU3OrzXSBGtamWqleEYe0e-U4H2QJqXugradb5DA7YlejErzgeIwp0-T6HJdcENxRwWdbY9tT7-J-0wnnUT46iHIDIJosvui-AEpSpIGdKEIarwWGnn35sEyPDDrXgkPuQnnDw0Fhubaqfba_TKRVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/146754" target="_blank">📅 22:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=BwWFcZ8Jly5W0geahYfUQySWN6jR2Uys7Ack5MLYrouL9zzNp8sZkFO4Hq55jqkppr7_rNMY_VMHL3y7_CYmUA6fEFRlhGMEdpwmmlKlzCVSc9k7Q3yXADfpj0B0LzteE9NoqQdSwzs80Sx8CPC8-Mos9EJEngNvLf_DAs8wZeVvZd6rcHxSa7EkUQ9mRU--AfwUSdv0b2muXqOcGf3KE0rQhvv7bnJj42vF97BAvjE2M0ec0_hufpAg_6KqxtleQlpo-d8R0dMM-jqUlMKne-swRFxTUBZ6y4To2wtTdtp8XyDIpWdhIK4tv8NQOiuxd-YsYwg_gwmonQQ-429_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=BwWFcZ8Jly5W0geahYfUQySWN6jR2Uys7Ack5MLYrouL9zzNp8sZkFO4Hq55jqkppr7_rNMY_VMHL3y7_CYmUA6fEFRlhGMEdpwmmlKlzCVSc9k7Q3yXADfpj0B0LzteE9NoqQdSwzs80Sx8CPC8-Mos9EJEngNvLf_DAs8wZeVvZd6rcHxSa7EkUQ9mRU--AfwUSdv0b2muXqOcGf3KE0rQhvv7bnJj42vF97BAvjE2M0ec0_hufpAg_6KqxtleQlpo-d8R0dMM-jqUlMKne-swRFxTUBZ6y4To2wtTdtp8XyDIpWdhIK4tv8NQOiuxd-YsYwg_gwmonQQ-429_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / تصاویری نشان می‌دهد که نیروهای اسرائیلی چند لحظه پیش تونل‌های زیر کوه "علی الطاهر" در جنوب لبنان را منفجر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/146752" target="_blank">📅 21:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پزشکیان فردا به هند می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146751" target="_blank">📅 21:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146750">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری بیا اینجا بهت میگه دلار و طلا رو کی بخری و بفروشی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146750" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-bprtzMkeCIj3QYPU9SmwnYWp_Qh4cGDTZY9gCwqr7niuiWZHcNAYGKZb1YgjLV95n-785ZA09dZF2RtmxorMAF0vJ-K1atkimpcNCTxpRVAO26xGLrdHlnK9RHxPXWH9Hr4dczfypZ1hDfhCyKDld3HL6mZ6QI9ZEqujOuSBpVQRRqmwqQtPkRdl6tpSsPY-oUAQV1POqUx7MAR3Keqn0Ro21myVAgEYoWhK-EWLlso_kLWd-WCmigjjSl7oue00lE_ryfocI0ogz7r1Twm3fu7LyISbIqgPu1mXnUYEh6AFlHEw8dNHt6ffyTL6IiV2ffdCxzMBxkBxTaI1kcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید شاکری (مشاور سابق اقتصادی قالیباف): فروش نفت ایران رکورد سال قبل و همچنین کشورهای همسایه را زده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/146749" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
در آستانه بیست‌وپنجمین سالگرد حملات 11 سپتامبر، 2977 پهپاد نورافکن شامگاه چهارشنبه بر فراز بندر نیویورک به پرواز درآمده و با شکل‌گیری تدریجی در آسمان و نمایش نور تصویری از برج‌های دوقلوی مرکز تجارت جهانی را در خاطره‌ها بازسازی کردند.
🔴
هر نور نمادی از یکی از قربانیان حملات سال 2001 بود.
🔴
در حملات 11 سپتامبر 2001، 2977 نفر از 90 کشور جان خود را از دست دادند. از این میان 2753 نفر در نیویورک، 184 نفر در پنتاگون و 40 نفر در پرواز شماره 93 کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146748" target="_blank">📅 21:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر نیرو: در حال حاضر اتصال شبکه برق ایران به کشور‌های پاکستان، افغانستان، ترکمنستان، آذربایجان، ارمنستان، ترکیه و عراق با موفقیت برقرار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146747" target="_blank">📅 21:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/ترامپ به نیوزنیشن:
اتش بس با این رژیم برای من تمام شده انها آشغال و تفاله هستند
🔴
پایان رژیم ایران نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146746" target="_blank">📅 21:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فیلد مارشال رضایی:  اقدامات سیاسی و مخرب آژانس بین‌المللی انرژی اتمی، کشورها را به‌سمت خروج از NPT سوق خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146745" target="_blank">📅 21:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آخرین قیمت نفت: ۱۰۷.۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/146744" target="_blank">📅 21:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=nQ-xSUQwlPqwK7C8jT6T7sMP8imqORy26pkIvzvBFaJq3PBhb_3Re7A9HhgvMdvMtYzPiOGkbE_aJ-z9AXsxZwAKqXoTWPZKGdnLRGaSG96ER-G01xU19sCtkNeC3on2MjBiNRCyMeNTaS5R6nx3tWvyvKFF04-8RpsUDEhZNZYYXo2YHDoCIsCJiqpFodIcwS8alDYxRYSAtnEmiA4YCWjeKUCDiVUSUal1zTftk8v7msnSJZoY7lc_uFB84OYombws3wo6hGXGGjukzKYvejSt4b8xpQAzO7d1P0PVFYmwFP6Ey1dzrnC0ei530jvDBgAtk_iC4qHhYP9osv902w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=nQ-xSUQwlPqwK7C8jT6T7sMP8imqORy26pkIvzvBFaJq3PBhb_3Re7A9HhgvMdvMtYzPiOGkbE_aJ-z9AXsxZwAKqXoTWPZKGdnLRGaSG96ER-G01xU19sCtkNeC3on2MjBiNRCyMeNTaS5R6nx3tWvyvKFF04-8RpsUDEhZNZYYXo2YHDoCIsCJiqpFodIcwS8alDYxRYSAtnEmiA4YCWjeKUCDiVUSUal1zTftk8v7msnSJZoY7lc_uFB84OYombws3wo6hGXGGjukzKYvejSt4b8xpQAzO7d1P0PVFYmwFP6Ey1dzrnC0ei530jvDBgAtk_iC4qHhYP9osv902w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: رئیس‌جمهور ترامپ امشب اعلام کرد که ایران در حال تسلیح مجدد خود با سلاح‌های هسته‌ای است. این درست است.
🔴
پس از آنکه توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را ویران کردیم، دوباره در حال تلاش هستند.
🔴
من اینجا، در کنار دیوار غربی، پیش از ریش هاشانا به شما اطمینان می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران سلاح هسته‌ای نخواهد داشت.
🔴
همزمان، ما به محور ایران ضربه می‌زنیم؛ نه تنها به شدت در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات بوفورت را ویران کردیم و اکنون با ارتفاعات علی طاهر در حال مقابله هستیم.
🔴
چیزهای بیشتری در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146743" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146742">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: ایران و چین با یک سازوکار پنهان تحریم‌ها را دور می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/146742" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146741">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) تصاویری را منتشر کرد که بقایای یک پهپاد شناسایی و رزمی ساخت عربستان سعودی را نشان می‌دهد که امروز صبح بر فراز استان حجه سرنگون شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146741" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146740">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه تلویزیونی ۱۳ اسرائیل گفت: ایران در حال برنامه‌ریزی برای یک "حمله بزرگ" است که اسرائیل را نیز در بر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146740" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146739">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: هیچ هواپیمای نظامی آمریکایی در حمله ایران به پایگاه هوایی در اردن آسیب ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146739" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146738">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سپاه: تنگۀ هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146738" target="_blank">📅 20:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146737">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
جابه‌جایی بالگردهای آسیب دیده آمریکایی در اردن
🔴
فیلمی از چهار بالگرد آسیب‌دیده بلک هاوک که از پایگاه هوایی موقر السلطی منتقل می‌شوند، در اردن در حال پخش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146737" target="_blank">📅 20:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIL8qlb4L4IhwQud_V6MftcOdBJZd2fOA_vbXbMEWWPAs9M9JFBc_w0Zb0_bmanvmRqVpgNwKSRefVNGhwoPFtvZ5RclNRT7Bn-MoHg8acMJKeJ072OI4zuDUeMA1Q9Ohr-84w37O_KoP5xUE6RzroIxYjWvaJYSIXlmlfWnoDyPsR80jvfJmsHu-1uUHzFUHXdeq7-Y0YCnDHN1IXzNiUxnajamdYYAVgctY3475_46smh4bg5QNR3o6Xyh_wlbIhnui1BR9_0BEyyksf0St6zHEBKtHHhQKBD2hha0jQqPvCr0nJ1SDEaLdmgiJ7NAQK3iit-E0-YOMOQ0A-Dd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c03d5ceb.mp4?token=aCsrPC6Ru5TgWV1FAkIdrlNjgHguVLRVv0yyZfn8CJbNzU6eBBrvPq3VvaTthAZW0O_JoShODvj_bGpcR7yB09qsc3xBAUTBAjYotq5Jbt8x6r46COZcBecLa4ALeYqDkHqpXm32REuNo-C8RGp0iSG-heMa8Heu-bYI0-T1R0ORePF16zwTOEq6f6lQlMQkFpqk3p6WMRGvg1NUy_WiTvgv4moVdB4VLaLpGaEsmB3csbRgdh2Zy0eWOMXcZeR1GtTH1czjggVBqxts0nhwl6hmUT2Pi9jZxIFpwtc6q8TJ2b-_1Yuuu7cx8UCKVlS_dPre_K2aWZsXxS4R76MxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c03d5ceb.mp4?token=aCsrPC6Ru5TgWV1FAkIdrlNjgHguVLRVv0yyZfn8CJbNzU6eBBrvPq3VvaTthAZW0O_JoShODvj_bGpcR7yB09qsc3xBAUTBAjYotq5Jbt8x6r46COZcBecLa4ALeYqDkHqpXm32REuNo-C8RGp0iSG-heMa8Heu-bYI0-T1R0ORePF16zwTOEq6f6lQlMQkFpqk3p6WMRGvg1NUy_WiTvgv4moVdB4VLaLpGaEsmB3csbRgdh2Zy0eWOMXcZeR1GtTH1czjggVBqxts0nhwl6hmUT2Pi9jZxIFpwtc6q8TJ2b-_1Yuuu7cx8UCKVlS_dPre_K2aWZsXxS4R76MxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انهدام شمپاد ارتش آمریکا در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146735" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رمضانی، مدیر توزیع نیرو: مردم کرسی بخرن، شاید به قطعی گاز بخوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146734" target="_blank">📅 20:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGYKuuBT2rvfBxaO4I6D1IVWvJLiDY1Lw-QrFR1Bi8fVkWrYcpe_IjPUlcyFG4j0cgI-BGj8kRDFKjMywJIKSgDP2RCwsFSzpQkP3pOzXQI5npoL4KK_2uo3oLxXvGmyqAClNRI9A1iar7RvfMn8LwHh3NY1gCdugRq1lN-RVqPgWyWv5Am3eR6g-tEtZ_cgIhMW_3fK704JHsjLPnCiDxj4ewHkT7JBszV7Zlo6zlxmzEYBgCXNawXaENFkEFrOeLk4dh25JlTvL4M8Y1Lljb80LzyNHuAozsmv_RdUxAJx2Oc9xs4QT7MrGCY7VaIbGEpfvqju0wBzNe6M_aYAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به تونلی در شهر حاریس در لبنان حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/146733" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال‌استریت ژورنال: جنگ با ایران ممکن است تا پایان دوره ترامپ ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146732" target="_blank">📅 20:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران بار دیگر تولید موشک‌های بالستیک را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146731" target="_blank">📅 20:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نفت ۱۰۷ دلار هم رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146730" target="_blank">📅 20:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e2184c3e.mp4?token=a66_Cw_CF3mPNta7g0YEclmlMtstQ11-n9XyH0nTf8rt1pRD9PdDand1jpID9AogjNSXcM1_mEEBBQzeRL6YAiJ1wq6h8uTu8lGq9I-ROMxV5dAw_BeQDuIuwoWrmWpFMQ0ITOccJFK34osl5EjRZCAarLPz9EClZF-eVJrJRrl7YwrIDm4lsEqivYKXxpWGqxSNS2nrZAbNoeuT_jUO_gFx54EZOpAZ5omOr8r-N2SEBaWL6mvCf_QhJFiz4drTS8rjFHXeZBc2b0A4vVcJduwYYXlQmVXqJBZOk6ETffrKWvYTuMsdeM5uyQ_bnBj187hpxSFJlx-_j9E0pQIGsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e2184c3e.mp4?token=a66_Cw_CF3mPNta7g0YEclmlMtstQ11-n9XyH0nTf8rt1pRD9PdDand1jpID9AogjNSXcM1_mEEBBQzeRL6YAiJ1wq6h8uTu8lGq9I-ROMxV5dAw_BeQDuIuwoWrmWpFMQ0ITOccJFK34osl5EjRZCAarLPz9EClZF-eVJrJRrl7YwrIDm4lsEqivYKXxpWGqxSNS2nrZAbNoeuT_jUO_gFx54EZOpAZ5omOr8r-N2SEBaWL6mvCf_QhJFiz4drTS8rjFHXeZBc2b0A4vVcJduwYYXlQmVXqJBZOk6ETffrKWvYTuMsdeM5uyQ_bnBj187hpxSFJlx-_j9E0pQIGsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگنده F-15J ژاپنی پس از بروز یک مشکل فنی، در پایگاه هوایی ناهای واقع در جزیره اوکیناوا فرود اضطراری انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146729" target="_blank">📅 20:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/146728" target="_blank">📅 19:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کاظمی: نمیزاریم دشمن مدارس رو غیر حضوری کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/146727" target="_blank">📅 19:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که نیروی هوایی سلطنتی عربستان سعودی در ۲۴ ساعت گذشته، ۶۴ حمله هوایی را در مناطق تایز، حدیده، مریب و الجوف انجام داده است. در این حملات از جنگنده‌های F-15 و تایفون استفاده شده که از پایگاه‌های هوایی شاه فهد و شاه خالد عملیات خود را آغاز کرده‌اند.
🔴
آنها همچنین اعلام کردند که نیروهایشان یک گروه از جنگنده‌های سعودی را در آسمان تایز با استفاده از موشک‌های پدافند هوایی تولید داخل رهگیری کرده و مجبور به عقب‌نشینی آن‌ها کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146726" target="_blank">📅 19:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146725">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی مسیر ۹۷ کشتی تجاری را برای اعمال محاصره بنادر ایران تغییر داده‌اند، در حالی که به بیش از ۵۰ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/146725" target="_blank">📅 19:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBPh5uIH_skxMiNl3jDTSRBe3P6juJRMY08TWOH3zTK2RY6Kq1Bd05y9v3dbMwm0GZjve09r-nrjPgkKhZGdGQVLoQKW8dee-HBzvf4V11QNePTdKl5N8EcnHAah4twYPc7CJd_fYP_pb_5u79ZSRrDTHHGlrEn0T4SArgxmsMA1RjKkigeLuALscv00C9C-FeNcm8BRHlfwYns2ZIdWHWQtNeYoBIOToTOZbEICk1I1kTyOX28zza94GOthv-WU7LVPMZR7eox8ChfJ7uC9oaUo25rSJ2Fp3oFARjJ7s7k-vxTnzPa7w78PQduTRK5JzcT_zIFMMm_PnCWyGkhSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به 106 دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146724" target="_blank">📅 19:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6QXIecbH_DdEDYegfMH9V1S_1JtbQUgyuaU0ftpHAZRNccdNGxz3SKJmc1Gkjn6D-gy6859zXXvzLfEwBF1ogJUpWe-5J0U8mE5qLO3b3IrKRpp0uFmWq-_8lT5IUx8VZSA2RJ9sxlGBrmhWW7_ZRjK6pqqhN8sPmd_6jdtNdfuPBpGQGGRZ1QSWrd9rekCAUHluXoYiVbEiDh7Qgjxgm11yuU7uVEbbeDseZ1NaD3ZSPVyMvzGHJ3iW8C2nj7r6G1fNYdu2zcPbebwdO6bQFBDA2JrvHdw7mq3j0iczN7EXANmtVJJi419JqQkYxAebGykfUyulnY4GPU-5xVDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه سعودی الحدث نیز اعتراف کرد جزیره استراتژیک پریم به کنترل انصارالله درآمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146723" target="_blank">📅 19:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146722">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت دفاع: به زودی گوشه‌ای از کوه‌ یخ صنایع دفاعی ایران را می‌بینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/146722" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هیلاری کلینتون درباره اسرائیل:
من اسرائیل را دوست دارم و از دولت و سیاست‌های نتانیاهو متنفرم. من آمریکا را دوست دارم و از دولت و سیاست‌های ترامپ متنفرم...
🔴
این خبر تکان‌دهنده در رسانه‌های اسرائیلی منتشر شد، جایی که نتانیاهو به طور مستقیم از سوی محمد بن زاید آل نهیان از امارات متحده عربی تماس گرفته شده بود و به او هشدار داده شده بود که حماس در حال برنامه‌ریزی برای انجام عملیاتی است [چند روز قبل از ۷ اکتبر]. و یا او به این هشدار توجه نکرد، یا می‌خواست ببیند که آن‌ها چه برنامه‌ای دارند تا بعداً بتواند به شدت واکنش نشان دهد و این امر موقعیت او را تقویت کند.
🔴
این یک شکست در رهبری بود.
🔴
اگر مردم اسرائیل بخواهند دوباره به این [دولت] رای دهند، به نظر من ایالات متحده باید موضع بسیار قاطعی اتخاذ کند. من فکر می‌کنم که می‌توانیم با یک دولت جدید همکاری کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/146721" target="_blank">📅 19:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146720">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: درگیری در خاورمیانه باید از طریق گفت‌وگو متوقف شود.
🔴
باید به اجرای تفاهم‌نامه میان واشنگتن و تهران بازگشت
🔴
ایالات متحده باید استفاده از زور را متوقف کرده و به مسیر دیپلماسی با ایران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146720" target="_blank">📅 19:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146719">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/55de3b7b3f.mp4?token=LfgpN_A478OnRXj_gwkaV7KqCiLsFKhTiBQQTMTxtaHM-ZspOP3a15tXuZrDTfzIiZ0A2NAYj4vXWNZXp-J7K6iJFkpGrFwakM-D-ImPMcgoqgBtkdO-dLbJtgOziAM5Wba-1ssilP8sImaeqbMCtn5izmEL8D-e0xwljuSXOEmPW5ugRxjrHsuEhsJiuEsHxxg4eMvRekiB8xFGtOrGB0kEPM-2RFNPQLU2vXLP6Gf5Xp-KmCJkiun35n2Ys3Nx7Lhs-gN-XEFgoftXXTHI-yJjuj1hlKhmX7GAh7B_pCtFtxOhstoBKHuuvzaCW05suj7lK6nqxxHVayR30REeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/55de3b7b3f.mp4?token=LfgpN_A478OnRXj_gwkaV7KqCiLsFKhTiBQQTMTxtaHM-ZspOP3a15tXuZrDTfzIiZ0A2NAYj4vXWNZXp-J7K6iJFkpGrFwakM-D-ImPMcgoqgBtkdO-dLbJtgOziAM5Wba-1ssilP8sImaeqbMCtn5izmEL8D-e0xwljuSXOEmPW5ugRxjrHsuEhsJiuEsHxxg4eMvRekiB8xFGtOrGB0kEPM-2RFNPQLU2vXLP6Gf5Xp-KmCJkiun35n2Ys3Nx7Lhs-gN-XEFgoftXXTHI-yJjuj1hlKhmX7GAh7B_pCtFtxOhstoBKHuuvzaCW05suj7lK6nqxxHVayR30REeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده دانمارک در نشست شورای امنیت سازمان ملل با موضوع ایران: ایران باید به‌طور کامل از قطعنامه‌های شورای امنیت تبعیت کند، از حمله به کشورهای منطقه خودداری کرده و از هر اقدامی که آزادی کشتیرانی را تضعیف می‌کند، پرهیز کند.
🔴
وضعیت تنگه هرمز تنها یک چالش منطقه‌ای نیست، بلکه مسیرهای حیاتی جهانی را نیز تحت تأثیر قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146719" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146718">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابعی گزارش داد، از آنجایی که جنگ علیه ایران توانایی قطر را در تأمین گاز مشتریانش به شدت محدود کرده است، دوحه در حال مذاکره برای عقد قراردادهای بلندمدت خرید گاز طبیعی مایع از تأمین‌کنندگان آمریکایی است
🔴
طبق گزارش این رسانه آمریکایی، شرکت دولتی «قطر انرژی» به دریافت محموله از پایانه‌های صادراتی فعال و در حال ساخت آمریکا علاقه‌مند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146718" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146717">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون: ما باید به خطرات بالقوه خود توجه کنیم، به ویژه به این که شی جین‌پینگ چه فکری می‌کند: می‌دانید، "آنها دیگر نمی‌توانند از کسی محافظت کنند، زیرا توانایی دفاع از خود را ندارند. شاید بتوانیم تایوان را وادار کنیم که به سادگی تسلیم شود، زیرا هیچ حمایتی وجود نخواهد داشت."
🔴
منظورم این است که اگر به نقشه جهان نگاه کنید، وضعیت برای ایالات متحده مناسب نیست، و من معتقدم که این تا حد زیادی به دلیل تصمیمات بسیار اشتباهی است که توسط این دولت گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146717" target="_blank">📅 18:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146716">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نماینده پاکستان: دیپلماسی و گفت‌وگو باید اصول راهنما برای حل موضوع هسته‌ای ایران باقی بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146716" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146715" target="_blank">📅 18:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای ائتلاف "جنوب غول" همچنان دسترسی به شهر عدن را مسدود کرده‌اند و نیروهای مورد حمایت عربستان سعودی را در جاده‌ها به دام انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146714" target="_blank">📅 18:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الحدث: روسیه و چین مخالفت خود را با بررسی تحریم‌های ایران در شورای امنیت اعلام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146713" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔴
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146712" target="_blank">📅 18:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
تسنیم: تنگه باب‌المندب به تسخیر رزمندگان یمن درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146711" target="_blank">📅 18:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: برنامه هسته‌ای ایران منبع نگرانی و تهدیدی برای امنیت بین‌المللی است. ایران تشدید تنش را انتخاب کرده، برنامه هسته‌ای خود را گسترش داده و بیش از 400 کیلوگرم اورانیوم در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146710" target="_blank">📅 18:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npKPVLgZVbplRBqOP4-1yaXM0q20_c7MkD4_vHT07sEyK6A4wTV0Xmxic_R3frC25ptNoee5gdbmVBmHrnE8v13ODXR4mCGKGmNbn-8EI8FXf6q98HSeKlk7UEOTSa_JXPGylYghBPTIVdEfKF8Nm4F3weSeGIzFml9PMioHcsu4gAAleNAuDe7o2h6A9sv9p9te5eV3-IKAQY60FB9SNit051VoVCxPql4qn1E6Z4KlzbryYwsHqI_7mndcpX7n8n1lu50QXkflNz0-8Jrqz-Na4BJRDv52pdmN_f71TP1vw_Ue7CyIKaMf9xA4QOKUTg6TlDbfdIxw36z0pTCnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین تصویر از جنتی که امروز منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146709" target="_blank">📅 18:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: ایران با آژانس بین‌المللی انرژی اتمی همکاری نکرده است.
🔴
نماینده یونان در شوراى امنيت: از ایران می‌خواهیم در مورد برنامه هسته‌ای خود با آژانس بین‌المللی انرژی اتمی همکاری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146708" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=aIbl8f18I0HtWSOhnFR_M33N-vq87xTrACcd3BKJGC9bTGHJmOt7JKmJv9etTbfCGX4h4Pw4EMrS2Osq2Q9JcSVOKAf9FRf1cSKY0wIi-4-FNLsDBtFymACH02rdY3Cm8L7dGGQxrdJD7tKjpsdUXZM0jIkQAnnhQVpumQTXgpY-ZE-oziABnXM-UU49UYxM37ZUabr952qO5RkIA6z2H9dx5HEiS5KJHLKq2uUsphTgbhbDop3ceDtpjotZVLxjkegNRsIhOF4g8UCvQUnjL0NfJW7DDE-Fpp1wYzjYFeJYipRk1PDkFoE0QUl_7atDJ6Fq9wH_loWcJY1Ntbm1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=aIbl8f18I0HtWSOhnFR_M33N-vq87xTrACcd3BKJGC9bTGHJmOt7JKmJv9etTbfCGX4h4Pw4EMrS2Osq2Q9JcSVOKAf9FRf1cSKY0wIi-4-FNLsDBtFymACH02rdY3Cm8L7dGGQxrdJD7tKjpsdUXZM0jIkQAnnhQVpumQTXgpY-ZE-oziABnXM-UU49UYxM37ZUabr952qO5RkIA6z2H9dx5HEiS5KJHLKq2uUsphTgbhbDop3ceDtpjotZVLxjkegNRsIhOF4g8UCvQUnjL0NfJW7DDE-Fpp1wYzjYFeJYipRk1PDkFoE0QUl_7atDJ6Fq9wH_loWcJY1Ntbm1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده بحرین در نشست شورای امنیت سازمان ملل با موضوع ایران: حملات اخیر ایران به ما و کشورهای منطقه نشان‌دهنده عدم پایبندی این کشور به قوانین و حقوق بین‌الملل است و باید در برابر آن ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146707" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=dPuCapazRLBDa0G48uysK3Op0tUB1Pd07olGh4HKECuG9NIAXVYG814QClpM4ON1Nbi-SxUeAlrUsjLlUURrDpHyOt18NtLIEGzmyFH71HYxS9vHihUN9uK56Z2gmxvjUnwATOxvl5AotmUEwx53rp2EGVuS63ghN2ATPKcZkZjxwBriaSbUF2msQ0iKm_A001_n8umzAJ_irbHbqzxrlcQew5gX9hTDhPFr8M6ueMBJhmxwUOHZWL5fU9G7usD7ne-_WMCELk5jgjcmk72sjwfo81rP6DCny0TaNAdQr_RAL2bBun_lc23BY-NMu4obmDD5AWFSV0llWqRl588waA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=dPuCapazRLBDa0G48uysK3Op0tUB1Pd07olGh4HKECuG9NIAXVYG814QClpM4ON1Nbi-SxUeAlrUsjLlUURrDpHyOt18NtLIEGzmyFH71HYxS9vHihUN9uK56Z2gmxvjUnwATOxvl5AotmUEwx53rp2EGVuS63ghN2ATPKcZkZjxwBriaSbUF2msQ0iKm_A001_n8umzAJ_irbHbqzxrlcQew5gX9hTDhPFr8M6ueMBJhmxwUOHZWL5fU9G7usD7ne-_WMCELk5jgjcmk72sjwfo81rP6DCny0TaNAdQr_RAL2bBun_lc23BY-NMu4obmDD5AWFSV0llWqRl588waA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔴
11 تایید
🔴
2 مخالف (روسیه و چین)
🔴
2 ممتنع
🔴
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس قطعنامه نبود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146706" target="_blank">📅 18:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146705" target="_blank">📅 18:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20260b4433.mp4?token=BxBvna7PH0841GoT5zaT-75-IUgacBXOymFFZDWN9EfY5o6_aI3TilIjgtQp2NqQY83n8bMDRG35nF6A0ys68wrNYnk4lA05h0ffWlmHVG9z3IVK_WESjL_6X2e_qv11syuHAbYRxHM9HakpWb-4BHcDCVg_S9WU6qLTow21oZoSkr60eMRo_-cT1KvCZuMQH5dQ3Hz6CIXK4ptzmFFn9U1fNdkVZ_t6COnvwo55BkKhqdxf74FPtlzvsKMKdDcXtaCoB1_AbxgSr8moMpMDt5esj4chqdIM6ZQ41gx5bdWFOueAd0TSQs7Cucqj5VT3dBF6kEybMlcx-OlzQTYwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20260b4433.mp4?token=BxBvna7PH0841GoT5zaT-75-IUgacBXOymFFZDWN9EfY5o6_aI3TilIjgtQp2NqQY83n8bMDRG35nF6A0ys68wrNYnk4lA05h0ffWlmHVG9z3IVK_WESjL_6X2e_qv11syuHAbYRxHM9HakpWb-4BHcDCVg_S9WU6qLTow21oZoSkr60eMRo_-cT1KvCZuMQH5dQ3Hz6CIXK4ptzmFFn9U1fNdkVZ_t6COnvwo55BkKhqdxf74FPtlzvsKMKdDcXtaCoB1_AbxgSr8moMpMDt5esj4chqdIM6ZQ41gx5bdWFOueAd0TSQs7Cucqj5VT3dBF6kEybMlcx-OlzQTYwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از سر بگیرد.
🔴
امروز باید گزارش ۹۰ روزه ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است.
🔴
روسیه و چین می‌خواهند قطعنامه‌ها را نادیده بگیرند و با وتو کردن آنها از ایران دفاع کنند؛ آنها در حال نادیده گرفتن اصول بنیادی سازمان ملل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146704" target="_blank">📅 18:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=jZxD4Nh174yN5lMdM0oGYMOfUxap7zJR_LumSk_Z22JYoVrD5_FoTK7sKO4ErCnBIzN3I9pq9bBSu58yWS7rkjRJrAXrdfgqWZ0635QS9JDlY4nd4l2CFm0-DZLhjD0uQCYt0bNgtFpqEPMAKmsu3DFaVNyn88QpfyamBQqP3fU8kH5DCHiEJCedqfFRl8olQm3eGTZq3kTRZVL9qgcJYmgwyad_fqUEODpkV4K2KqjelEm9gcw6jeCrrhIx0GWjHsKz-oBlX6makb3AYk7ggngBYoR788NekjQNHoXNF5kKd1BWGGdh_kSeySmNcpYQuyIZ5IBjjbS_s5tM2Che5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=jZxD4Nh174yN5lMdM0oGYMOfUxap7zJR_LumSk_Z22JYoVrD5_FoTK7sKO4ErCnBIzN3I9pq9bBSu58yWS7rkjRJrAXrdfgqWZ0635QS9JDlY4nd4l2CFm0-DZLhjD0uQCYt0bNgtFpqEPMAKmsu3DFaVNyn88QpfyamBQqP3fU8kH5DCHiEJCedqfFRl8olQm3eGTZq3kTRZVL9qgcJYmgwyad_fqUEODpkV4K2KqjelEm9gcw6jeCrrhIx0GWjHsKz-oBlX6makb3AYk7ggngBYoR788NekjQNHoXNF5kKd1BWGGdh_kSeySmNcpYQuyIZ5IBjjbS_s5tM2Che5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون درباره ایران
:
ما کسانی هستیم که ایران را تقویت می‌کنیم. آیا ما از آنچه در ۲۵ سال گذشته انجام داده‌ایم، هیچ چیز آموخته‌ایم؟
🔴
و من فکر می‌کنم ایران، نه فقط با تشویق بلکه با کمک هر دو چین و روسیه، بازی بسیار هوشمندانه‌ای برای کاهش توانایی ما در دفاع از خود و متحدانمان انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146703" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اسکات بسنت: ایران در حال حاضر به‌دلیل محاصره دونالد ترامپ و تحریم‌های فلج‌کننده خزانه داری آمریکا با پیامدهای سنگینی مواجه است
🔴
آمریکا کنترل کامل تنگه هرمز را در دست دارد، صادرات نفت ایران رو به کاهش است، صف‌های طولانی مقابل جایگاه‌های سوخت شکل گرفته و اوضاع هر روز بدتر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146702" target="_blank">📅 18:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
هم اکنون جلسه شورای امنیت سازمان ملل درباره برنامه هسته‌ای ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/146701" target="_blank">📅 17:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
👈
طرق گزارش مسافران: فرودگاه‌های ترکیه پذیرش محموله و باری که مقصد نهایی‌اش ایران اعلام شده را متوقف کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146700" target="_blank">📅 17:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گروسی: نمی‌دانیم در کوه کلنگ چه می‌گذرد
🔴
مدیرکل آژانس بین‌المللی انرژی اتمی می‌گه از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ گزلا رو زیر نظر دارن، اما نمی‌دونن دقیقاً چه خبره.
🔴
از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ‌گزلا رو زیر نظر داریم ولی نمی‌دونیم چه چیزی داره رخ میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/146699" target="_blank">📅 17:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/بلومبرگ:
آژانس انرژی اتمی وجود فعالیت هسته ای در سایت کوه کلنگ ایران را تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146698" target="_blank">📅 17:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع نظامی دولتی: حوثی‌های یمن به جزایر حنیش بزرگ و کوچک در دریای سرخ رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146697" target="_blank">📅 17:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس سابق سازمان جاسوسی بریتانیا:
فکر میکنم وضعیت کنونی با ایران چند ماه دیگر نیز ادامه یابد، اما فشارهای اقتصادی از مقطعی به بعد، آثار خود را بر ایران نشان خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146696" target="_blank">📅 17:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرماندهی جبهه داخلی اسرائیل: از سال نو لذت ببرید، اما برای هرگونه تشدید ناگهانی و غیرمنتظره وضعیت، آماده بمانید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146695" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
در حال حاضر ۶ فروند هواپیمای سوخت‌رسان و یک فروند P-8A Poseidon در منطقه در حال پرواز هستند. شمار اعلام‌شده هواپیماهای سوخت‌رسان، شامل هواپیماهایی که در حال بازگشت از مأموریت‌های خود هستند نمی‌شود.
🔴
۵ فروند از هواپیماهای سوخت‌رسان متعلق به اسرائیل و یک فروند متعلق به قطر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146694" target="_blank">📅 16:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=hg7gjFxXLVdoriWXhV2_bMMQosGHhGPiMdOpSRVLfnJYFs_OLTXQudDJbmadQ59Jg_gczCCw54cLH-hXgY4tfZs3akKFQIlSr4OBLcXgeEp5S6Nk_rPYVTCoa612_dTqbe4NfbuS800znqrCM4VrdYBxVPoll3fyEaZIDpcNleNxs4jVsPh892eSpq8l3lyq0yqfdg2tquNnJj5ZCQyrJZF_MCLpdb-0L5qM_eiEmM1yupDz8PISJn5g1WdbyrxU27SScUHbjHHwYltqmkPxUftV40tScxKAegipvFE8i4sOFnUVGO5Rfs42_VLtohPMpX06wffQiu1sh4zaSXCzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=hg7gjFxXLVdoriWXhV2_bMMQosGHhGPiMdOpSRVLfnJYFs_OLTXQudDJbmadQ59Jg_gczCCw54cLH-hXgY4tfZs3akKFQIlSr4OBLcXgeEp5S6Nk_rPYVTCoa612_dTqbe4NfbuS800znqrCM4VrdYBxVPoll3fyEaZIDpcNleNxs4jVsPh892eSpq8l3lyq0yqfdg2tquNnJj5ZCQyrJZF_MCLpdb-0L5qM_eiEmM1yupDz8PISJn5g1WdbyrxU27SScUHbjHHwYltqmkPxUftV40tScxKAegipvFE8i4sOFnUVGO5Rfs42_VLtohPMpX06wffQiu1sh4zaSXCzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها، پس از تصرف بندر المخا، تجهیزات نظامی متعلق به عربستان سعودی و امارات متحده عربی را به غنیمت گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/146693" target="_blank">📅 16:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=Er1sJiesDujF7FT6HwzDl2YmB4z7iOHKpSBdd8Xz9mqbQjiCZEsuy5iI9UpnhZkpMie8m-h1TVlx8T9AZKm2d1M-g7-CgbK60yXDtjem6FHLchkM0NXGu3JQz9R7icaQu9_VA1fOHusKCBe2r7r8lMCdYR1rGfoESefV38hdQZV0qK1KL2-iSO3qXwpExNGrkFQi1aECjiU0eUIcEg4kU4MwosoTf4EASWXtO0HedAY8uBu69VYk1TBkrn9f7MU24N6y_SZICLOYZBuemjS1UXImRNREuWo5GANLDdZcLG_evgQqY5-7B2kmbu6_g-RXfV1cieqlZzxQRnu7L7bDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=Er1sJiesDujF7FT6HwzDl2YmB4z7iOHKpSBdd8Xz9mqbQjiCZEsuy5iI9UpnhZkpMie8m-h1TVlx8T9AZKm2d1M-g7-CgbK60yXDtjem6FHLchkM0NXGu3JQz9R7icaQu9_VA1fOHusKCBe2r7r8lMCdYR1rGfoESefV38hdQZV0qK1KL2-iSO3qXwpExNGrkFQi1aECjiU0eUIcEg4kU4MwosoTf4EASWXtO0HedAY8uBu69VYk1TBkrn9f7MU24N6y_SZICLOYZBuemjS1UXImRNREuWo5GANLDdZcLG_evgQqY5-7B2kmbu6_g-RXfV1cieqlZzxQRnu7L7bDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو مربوط به آتیش گرفتن موتور یه پیک هست و یکی اون وسط داره بلندبلند شماره کارت پیک موتوری رو می‌خونه و مردم گوشی به‌دست دارن شماره رو می‌زنن که بهش کمک کنند موتور جدید بخره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146692" target="_blank">📅 16:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آیا پاییز و زمستان قطعی برق خواهیم داشت؟
🔴
وزیر نیرو: از الان نمیشه پیش‌بینی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146691" target="_blank">📅 16:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0yoV7RgCDejVpsu6zZCza1-NKTa4iIhCAJFlahwUtRH3TZAwkFEhyAjQV3WRIy05E4tV5AetmwBoDRXwFmwJJ_leL_mU_IR3Qt0Vx71hJSRCFsmFb0ICphNhj0VPCSOONjbQh42VyBtSyyRMZ3p9sjV_FnmRd4WI1KXJMpkV9lyZHJ3qWk0ZLd5So0AhRYT1HYTLb59sbJyPV61m4M-6rfnuTAqCfAYtbVWgLfvIBEGLlAeA46vYWoI1zKoF2kWsuzu1vXZD2aufR3BEkMlxJ_gPItkMEuIKwJDdQlw7K8pPgrnT04etQSiwK0VDC8dRJ13DhixpIIRofzfym_C_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه حمله هوایی اسرائیل
نبطیه الفوقا
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146690" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9EAuqcaTNpSGt8qATsWEccp0mjeDCNUaH-BosGsnS7dkEMeYehclzuWwTBlmpiSUU1Q-DYRn4Q87YReLOGa-g25tIT0452tdP1ySjaUVfvf6jYEwOblQnfzG1ocP-H4CurlvTdKenB04bxoaoU9LU-QM81hnk_p_C-JJAl-m0u8cGB7Xk9sC9ihhWcW2Leovix-J1nyRjQaL0pvIJOw1QIfesUCvXzqbjVoTp_VJSnxom5WDmcUkADh-O0uPZLaNTbhhfB2c17S8pg5F5NQn-iN4RY11cN1iWWumeIX7F0hRq9cAaPqUpIXGK027UTYba5Vt05U45n-8CLMuAZr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۴.۲۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146689" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrKV-LpDhed66tbOCzk3JPr5aULnIJ7Yt__vMY3gsJg7fIYEvwaOJhZ0AWjVK8YcZUYK1gatdOPMeojmX2r0flxGbu2EsbmOlpgnCGrj2HyyoB9pWcvpiYcEn5ELn_OulAh0M2nZMTTYhDITeweogtKPhChyCP_RfB2rxG1gyLk-ZCPoFKLTAhfL6V-suHOy5x-7UrEJR8ymsXJGo3Qoh-mTpWVJ8iXbNvAtAy9DYbEUJlB6r20uOTlXEyWwtLGC2DnnO9CJFeM8Ok-Pk52y7gcVP-friKwAY5csftx8j0jpXpDSrE84GOF6LQxmOBZbsK7_jA1RS17ueJ-pdiqdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت «۱۰۰۰ دلار تتر» کاملاً بصورت رایگان
🌟
این پاداش بزرگ تونیکس است
💎
🔺
بدون سرمایه‌گذاری
🔺
بدون پرداخت هزینه و کاملا رایگان
🔺
بدون بازی و فعالیت سخت و زمان‌بر
📍
فقط کیف پول خود را وصل کنید و پاداش خود را آنی دریافت کنید.
توکن های دریافتی از همین لحظه قابل معامله و استفاده هستند
💯
فرصت و تعداد توکن ها محدود است همین الان اقدام کنید !
⬇️
⬇️
https://t.me/+jtexLpNX-fNlYjcx</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146688" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه قطر و عربستان درباره آخرین تحولات منطقه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146687" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نیروهای انصارالله، تمام جزایر دریای سرخ، از جمله جزایر ابو علی، هانیش کبیر، هانیش صغیر، سویول هانیش، الممالح و جبل زوقار را به تصرف خود درآورده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146686" target="_blank">📅 15:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxJSfoKN87tKF2zkvMR6VmwF4JjlsqPufsuHl6677_mFnMvhrrtogbDdQMrggYOkkn9JJxGDSWKquZRjLFMGNnSkNuMddQYpTRys39tfr1XtsnSyLu2QwZVW-ATetSu2vwL9k1tAMjcbblQHd6200tLUqKOtl_3t1sFhneCSICBMjX4NsFIfsvLB-hjfpCrpEoB9RZL_sxin8gyajNTSyNAHDQxw8d8uvL3Fpn5o14XrfIl28okdWha25DYrFknb__XchzRaF2ehHB_1hf3SLLJoAsxvEyean4qc1-zJRVw7MQi2LsvY9pQTx49lalnv8HDX7zubhIhPGxZjOSjDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای انصارالله، تمام جزایر دریای سرخ، از جمله جزایر ابو علی، هانیش کبیر، هانیش صغیر، سویول هانیش، الممالح و جبل زوقار را به تصرف خود درآورده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146685" target="_blank">📅 15:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoNv2jdL62OJtUNdthhT_iUcDuZyZwoZ-WzL4Cn9msZyNUokuprQVq2x083xSEQb5y3hAlqAC3aJ_HpWlVwk_vDmmGEh3x61QcZGTMfHsupfD8GmjnYYLosRV_UvzM77HnbqHqPHX-8FXtFInXPQAGggria5wVxKRi0LZH_OAu41mfBlYI55PzTVLodvwkiMcLkDOnPwzT6me75tGEaHlW7TlFuAd9HE1GhhNk82k7MoEv2FIl7rLv6-VK2Vx9Fix3b_bt1t8pGF7s0s9TaD57QOxP5IDqcK4Klsm2Y-qYHGjrdtHCEKrCMT79gx55FrC-7pR3gtzJS2RBGNLmWaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلار هم اکنون 236,750 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146684" target="_blank">📅 15:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0abdca06.mp4?token=t5x_DvH-dyEXW5tIlwSLuzhfsM8vf4j3BubkItzp4AE-eLiLE00VS1ZAalIANxTMJYaFimz8vj3bvM7Zte6VrQ11sb3Kyyk6R5JEIiM47EwRJ96wqxvBSxh5mO0eQrx2_qkI588c9uz5nHt_iDmJ6L2L1we6Lb96ZxbCkEExeljmSH_ELYoAOcbxW00HICQIN5YKXfExJkY-mBpMlt2cbylBMy3IL_noOai0iLfwqSps3Mx6LGjZhdsQVNhKQr9EjfI0PYNY5PGeUMJ8llmU9yFF7-g8jq9X3q3A5C5d227ZkcL_vojaFBp2qMJ1X-iKrvsS29acfwgYyaw0n4-BnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0abdca06.mp4?token=t5x_DvH-dyEXW5tIlwSLuzhfsM8vf4j3BubkItzp4AE-eLiLE00VS1ZAalIANxTMJYaFimz8vj3bvM7Zte6VrQ11sb3Kyyk6R5JEIiM47EwRJ96wqxvBSxh5mO0eQrx2_qkI588c9uz5nHt_iDmJ6L2L1we6Lb96ZxbCkEExeljmSH_ELYoAOcbxW00HICQIN5YKXfExJkY-mBpMlt2cbylBMy3IL_noOai0iLfwqSps3Mx6LGjZhdsQVNhKQr9EjfI0PYNY5PGeUMJ8llmU9yFF7-g8jq9X3q3A5C5d227ZkcL_vojaFBp2qMJ1X-iKrvsS29acfwgYyaw0n4-BnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حادثه مرگبار برای کشتی خارجی در چین
🔴
خبرگزاری «شینهوا» خبر داد که یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🔴
به گفته مقامات چین، در نتیجه آتش گرفتن این کشتی در چینگدائو استان شاندونگ در شرق این کشور، ۲۰ نفر جان خود را از دست دادند و ۵ تن دیگر مفقود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/146683" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز: «سجاد حیدر خان»، سخنگوی وزارت امور خارجه پاکستان، گفت این کشور در حال حاضر بررسی حمله به حوثی‌ها در چارچوب توافق امنیتی مکه نیست.
🔴
او افزود: «در حال حاضر چنین موضوعی مطرح نیست… وقتی زمانش فرا برسد، طبق این توافق عمل خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146682" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نیروهای انصارالله پس از رسیدن به اردوگاه عُمری دریافتند که این اردوگاه از پیش تخلیه شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146681" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بلومبرگ: ایران توانمندی‌های موشکی خود را بازسازی کرده و مشاوران کاخ سفید هشدار داده‌اند که جنگ ممکن است تا سال ۲۰۲۹ ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146680" target="_blank">📅 15:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWs2-rdACB5T_fFCLORPzOuSmmSrlJQpbkBNmZamZnR_uEsL8tx0eXnIFmY9pUhBNaTtHAbwBXLM9Zb9WQ9-_Bur3qBjqB7lPkGCeGr2DJ6CPjsiTDOVlWt3NmhlABpxRfK3RF4x9dl_4GoWG5ozTTUpwS9EdeYODPXaWxK1UF4TnoPc7m-Pefko07EaoCR_ULbQdqb-74r14b7PKab8UkIhssvNl82GkX81onLNByb9LVzxz3C4Bj0qGKwupW7l_53-xmRSW3--MOKfrICIDfS3WHPnBb9HvtUYa_BXbpECWGEc9iJBPWcCGGBq-mrIkBbCl22JC3LFMQZewZoMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت دیروز سفارت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146679" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: الجزایر تصمیم به قطع روابط دیپلماتیک با امارات متحده عربی گرفته است.
🔴
تلویزیون دولتی الجزایر اعلام کرد تمامی تلاش‌ها برای حفظ روابط دوجانبه به پایان رسیده، اما دلیل دقیق این تصمیم هنوز مشخص نیست
🔴
رسانه‌های الجزایری پیش‌تر امارات را به تلاش برای…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146678" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c171ce10fb.mp4?token=CfwAikPxftsdsWIt2IENUt0mZ7NN7kbI7e3wOJYTcNGmHSKvVPRVD8fqsrZZ7n4qFumsB1vIHTsY00I4TvtbzCtbsqMsfS-gqxUNsm2Xqr0pGvM5u1osoQIh0go2zQPVQ-evL4ij-3TgGhXHViBG76KwbInw4NCTp4ivKOIQThAJQyW224snovpuU5AA3DiHIvuli0GNc__UenekNJfq1bOzZvdVX8hWZk5QeU50MKydUXINzcIxJ2PWh1JlGd7-CYMfb5Eb__OWPKFGUdloFNAaT4VaMzAwQ27a-T2G-LHJFCYdSuE5OKxb__08GGcNcX9mRVTk6nXpmXqGupFkDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c171ce10fb.mp4?token=CfwAikPxftsdsWIt2IENUt0mZ7NN7kbI7e3wOJYTcNGmHSKvVPRVD8fqsrZZ7n4qFumsB1vIHTsY00I4TvtbzCtbsqMsfS-gqxUNsm2Xqr0pGvM5u1osoQIh0go2zQPVQ-evL4ij-3TgGhXHViBG76KwbInw4NCTp4ivKOIQThAJQyW224snovpuU5AA3DiHIvuli0GNc__UenekNJfq1bOzZvdVX8hWZk5QeU50MKydUXINzcIxJ2PWh1JlGd7-CYMfb5Eb__OWPKFGUdloFNAaT4VaMzAwQ27a-T2G-LHJFCYdSuE5OKxb__08GGcNcX9mRVTk6nXpmXqGupFkDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران گسترده زیرساخت‌های حزب‌الله توسط نیروی هوایی اسرائیل در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146677" target="_blank">📅 15:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jjqi4rCHzZSY8npIVoDVB1GnXVoPtwZlYKs58yLDuiljun9Ejron195oZItMH85XC6NaJ0OO-Zxp2yuCw59aEOan-X9bqmc70riUB3T181fgJYBBpVmyKTYrJB9nUxEuSRzA1Pj1kYcMDBIs90V8OebH7yjxzAelnMdDycs-aAQIXjIRtyI58CligmVZl8ZIhHaPa7lHfyL52wbAUMFhzDNXhLv9cjhPHpWmA17E115WgaivvdcmmC3ac2DaD4WF6X4swFIlzukbYr3VY2qzTwAxk0tJf9c-VYr-jeaYC1Y2mVuCP9ZUprMb_T9_tltO7DeEg3ARzvkDch4QRl8rdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c62ff9ff.mp4?token=qQJAOMIkKNP-ofv-jgEPuzVkVktEdiFueO04YBKXyKisM89B73wkqAiEeuYv-oX10t1owH5RyN2_GYkDhT3FPKTvvZ81HRjItfax1cf8BYGC-yZqjnegdQNubDqX2fE4wixaSDbaSa2bVWBnFLbAEih_IVvwg1utHsDlju4axjoCt19dof2a98tUW9IispcGhhnqbJqHM6ND-v5FsZiwpGDnNAfQZ2Y2uEfQ3IRl5Vl86VgsV3DKfLXnDHESVyQNDSQYq8B-pxY8pF9-JLOtIsvDgtA_3OL1FDZ93vsPeHb03XPV2B8OTbpfLRo9XerobgjlGXHzJSKTRuKMmE92qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c62ff9ff.mp4?token=qQJAOMIkKNP-ofv-jgEPuzVkVktEdiFueO04YBKXyKisM89B73wkqAiEeuYv-oX10t1owH5RyN2_GYkDhT3FPKTvvZ81HRjItfax1cf8BYGC-yZqjnegdQNubDqX2fE4wixaSDbaSa2bVWBnFLbAEih_IVvwg1utHsDlju4axjoCt19dof2a98tUW9IispcGhhnqbJqHM6ND-v5FsZiwpGDnNAfQZ2Y2uEfQ3IRl5Vl86VgsV3DKfLXnDHESVyQNDSQYq8B-pxY8pF9-JLOtIsvDgtA_3OL1FDZ93vsPeHb03XPV2B8OTbpfLRo9XerobgjlGXHzJSKTRuKMmE92qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای بیشتری که تخریب سه مخزن نفتی در منطقه جازان عربستان سعودی را پس از حمله اخیر یمن تأیید می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146675" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLZbYKaO2laHd7FzE1u1X_Z848i5R_mFK188CwpiSkEu7lP53TaD0EhZS5EUTwCCo1Ox2n785-qt5aixpt8nDkHC5eSMAjTBgm-0T4oCu1UbX7bCoSQr3naDjgu-yrypfkbSa4idturzB-vrJoxnMeMzrV4-z89wRBxb5cKKF9J2HlZClslTZOt3gt14DoCr0u-6fmYS9fXfRsqiAfB0FeWmgMe99aZZQpmJTyGoEM494-XBVPiFADssqftXEXvE4fYbYoIVl11HShTdZBG3swtd3x_AU270NOLxl-0fwOxCzXNqvsSK0_lagoFXuUhBhYV8EVH8Ttvw3nqLYkuYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
مقامات اصلا نمیدونن جنگ سر چیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146674" target="_blank">📅 15:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
پزشکیان: سالن‌های همایش و استخرهای متعلق به دولت ادغام می‌شوند
🔴
در مدیریت فرایند اصلاح الگوی مصرف، دولت پیشگام است و شخصاً بر جزئیات این روند در مجموعه‌ای که مستقر هستیم، نظارت دارم.
🔴
به‌منظور افزایش بهره‌وری و صرفه‌جویی در مصرف سوخت، بیشتر سالن‌های همایش، استخرها و ساختمان‌های متعلق به دولت برای عبور از بحران تعطیل یا ادغام خواهند شد.
🔴
همچنین توسعه و تسریع در نصب پنل‌های خورشیدی سقفی در واحدهای دولتی همچون استانداری‌ها در دستور کار قرار گرفته است.
🔴
از سوی دیگر سیستم روشنایی و گرمایشی هر نهاد دولتی در فصل سرما با الگوی کاهشی کنترل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146673" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851878f527.mp4?token=ecFlQ4x_gNm58KL4iN5F8cg_6Eo0GT_uCnb_DskmoZQHNZTgC2gukysQR43bayLyz8kyKmSF1f003UdhBdmkuTUiyOwb4Aq1Oce_jmfze9qZEOcY7K4mxrolxnFgccDGqvPNsufAdRE9n2sG-9s-e2NIH3E3iLIjQT6nwFa2350x0euyLJMqa0z-01FUQh9XoyMi9kkXjVzAkZeRKNRnMkffyEd1uE8lzDPfTgge9lRPOjDD4eYgDCkxPIYenBxN-Tgt3OlPMtfv-pRWptGncbzujtMzPTM_DUEBcEu4PlhfhT5SwGINqzkhxVfO_VRpf8YWf23J_2ht3GfiJgF50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851878f527.mp4?token=ecFlQ4x_gNm58KL4iN5F8cg_6Eo0GT_uCnb_DskmoZQHNZTgC2gukysQR43bayLyz8kyKmSF1f003UdhBdmkuTUiyOwb4Aq1Oce_jmfze9qZEOcY7K4mxrolxnFgccDGqvPNsufAdRE9n2sG-9s-e2NIH3E3iLIjQT6nwFa2350x0euyLJMqa0z-01FUQh9XoyMi9kkXjVzAkZeRKNRnMkffyEd1uE8lzDPfTgge9lRPOjDD4eYgDCkxPIYenBxN-Tgt3OlPMtfv-pRWptGncbzujtMzPTM_DUEBcEu4PlhfhT5SwGINqzkhxVfO_VRpf8YWf23J_2ht3GfiJgF50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: آلمان با استقرار دائمی یک تیپ زرهی جدید در لیتوانی، به امنیت متحدان کمک می‌کند.
🔴
سپاه یکم آلمان-هلند نیز مسئولیت فرماندهی جدیدی را در جناح شرقی ناتو بر عهده گرفته است.
🔴
آلمان برنامه دارد تا سال ۲۰۲۹، معادل ۳.۵ درصد از تولید ناخالص داخلی خود را صرف هزینه‌های اصلی دفاعی کند؛ یعنی بسیار زودتر از مهلت تعیین‌شده تا سال ۲۰۳۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146672" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=kW8wTR7hzpCaMVnnn8qDNMv0-Cpkl69oXMszriSVsCsVu8hkPLVNPakzZ_z062sN_wlO-WuKEeRpdnosvyzcWwfpx7tSC9lfJBtx1r8rbZEFD9VvD4I0ONZXDJHWuRgLgqZYnxYmBhFuPg9tVeZyu10P-Ym6UI3mfQuerYvcQduBp8DZbRaz-_hdt41z_biGq0V_l92DcoVvLPHIlMXitNIzE6m0BT1Kr3Iefoea4kBMRcmoDz5_m6I4VzIVslaLFB74-vFDsns47UH7z2AOCCjwWc_BvA_7iV-9fOyrN-ehVPB_2cum6S5L66FmQKAC4jencZ0dHaeXMV05JoVUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=kW8wTR7hzpCaMVnnn8qDNMv0-Cpkl69oXMszriSVsCsVu8hkPLVNPakzZ_z062sN_wlO-WuKEeRpdnosvyzcWwfpx7tSC9lfJBtx1r8rbZEFD9VvD4I0ONZXDJHWuRgLgqZYnxYmBhFuPg9tVeZyu10P-Ym6UI3mfQuerYvcQduBp8DZbRaz-_hdt41z_biGq0V_l92DcoVvLPHIlMXitNIzE6m0BT1Kr3Iefoea4kBMRcmoDz5_m6I4VzIVslaLFB74-vFDsns47UH7z2AOCCjwWc_BvA_7iV-9fOyrN-ehVPB_2cum6S5L66FmQKAC4jencZ0dHaeXMV05JoVUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: «همه برای یکی و یکی برای همه؛ این همان شیوه‌ای است که ناتو عمل می‌کند. روسیه می‌خواهد ما را از هم جدا کند، اما ما متحد هستیم.
🔴
روسیه می‌خواهد مانع کمک ما به اوکراین شود، اما ما کمک بیشتری به اوکراین خواهیم کرد. روسیه می‌خواهد قدرتمند به نظر برسد، اما ما قوی‌تریم.
🔴
اقدامات روسیه نشانه ضعف و نشانه شکست این کشور در رسیدن به اهدافش در اوکراین است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146671" target="_blank">📅 14:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146670" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز
:
الجزایر تصمیم به قطع روابط دیپلماتیک با امارات متحده عربی گرفته است.
🔴
تلویزیون دولتی الجزایر اعلام کرد تمامی تلاش‌ها برای حفظ روابط دوجانبه به پایان رسیده، اما دلیل دقیق این تصمیم هنوز مشخص نیست
🔴
رسانه‌های الجزایری پیش‌تر امارات را به تلاش برای افزایش تنش‌های منطقه‌ای متهم کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146669" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146668" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ایرباس ممکن است برای کنترل بیشتر بر تأمین قطعات، مالکیت یا کنترل مستقیم برخی شرکت‌های تأمین‌کننده را در دست بگیرد.
🔴
این تصمیم پس از سال‌ها گلوگاه در زنجیره تأمین و صنعت پیمانکاری مطرح شده؛ مشکلاتی که باعث تأخیر در تولید و عقب‌ماندن ایرباس از اهداف تحویل هواپیما شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146667" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rafQxr1f52L8jlW89pq4jEWkHlVVF0mkt8-s2lt6s3GXGKILAoZyfSfBR38m5Y1C_4dORjrMp3U6pfbHVVHnSlyl-jrXxWdswEaCalMhU5XTVoFIHzf5BsT51a_fTwNm2GizhhTX337BW2H4BwzB-ILuM9VYIKy7EClKMqsWhupoGndOg1RDQ6i9MKabLpc8Sxy4EL_A81li8RAnRejV07XfCrjuzi6ppOMpjgx7b2jpMDF3rLlWJrYefDkmxAkDQit9nY7h7Hc3A317gsUIcVYRMPD2yy_QIO0hMZVsd4qiYBiUgjRmfHeiTiPTUeLMNeJW9fPUvOUnTmfc2Y7d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به‌روزرسانی نقشه کنترل و درگیری‌ها؛ فاصله ۶۰ کیلومتری ارتش یمن تا باب‌المندب پس از تصرف المخا
🔴
بر اساس نقشه‌های جدید کنترل میدانی، پس از تسلط نیروهای ارتش یمن بر شهر بندری المخا، هم‌اکنون فاصله این نیروها تا تنگه راهبردی باب‌المندب به حدود ۶۰ کیلومتر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146666" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیروهای جنوبی وابسته به امارات، از ورود عناصر مرتبط با عربستان سعودی به شهرهای جنوبی جلوگیری کردند، این اقدام پس از فرار این عناصر در برابر پیشروی ارتش یمن صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146665" target="_blank">📅 14:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: ممکن است در برخی جا‌ها با کاهش سوخت‌رسانی مواجه شویم، لذا باید سوخت و تجهیزات گرمایشی جایگزین به آن مناطق برسند
🔴
جهت عبور از بحران، بیشتر سالن‌های همایش، استخر‌ها و ساختمان‌های متعلق به دولت تعطیل یا ادغام خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146663" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس گزارش داده در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق‌السلطی» در اردن، یک هواپیمای تهاجمی A-10C نیروی هوایی آمریکا یکی از بال‌های خود را از دست داده است.
🔴
بر اساس این گزارش، حدود ۸ فروند جنگنده F-15E نیز به‌صورت جزئی آسیب دیده‌اند.
🔴
سی‌بی‌اس افزوده جنگنده‌های F-15E آسیب‌دیده پس از بررسی و تعمیر، دوباره به خدمت بازگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146662" target="_blank">📅 13:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی خطاب به تندرو ها: انتقام رهبر رو امام زمان که ظهور کنه میگیره
🔴
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146661" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=BeD1wL27YWS9Rvx5TFLk8EEpRbv9lR1a_y5ocsHC_Lt0z1i55IpWst4OAHwdVFRIt8ouNii9l-ncI2YShghv-mwUtk0igAYzNFFaYDLQhTpgeKsQCdjeUmeRdHLCMifRuF8NunmhwCEDi0JLPEVVEzf9lXyFGnhC4B_Ha9wBOSSrJvgTJdkb_9q8RIGtejZKQObrhEMta5iyTueNKi3T1I0DFezJcF8SzVUNWfKfWO6o1YT6FL_7qckQBF-hs-JcsU2MRYLYqRxZC4d2F8una-UAWaT2030R2-rUbK_mn4x1Am42NkUSnIwZY44olvUGNfwK0z1sUe2U9FSWLT_A3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=BeD1wL27YWS9Rvx5TFLk8EEpRbv9lR1a_y5ocsHC_Lt0z1i55IpWst4OAHwdVFRIt8ouNii9l-ncI2YShghv-mwUtk0igAYzNFFaYDLQhTpgeKsQCdjeUmeRdHLCMifRuF8NunmhwCEDi0JLPEVVEzf9lXyFGnhC4B_Ha9wBOSSrJvgTJdkb_9q8RIGtejZKQObrhEMta5iyTueNKi3T1I0DFezJcF8SzVUNWfKfWO6o1YT6FL_7qckQBF-hs-JcsU2MRYLYqRxZC4d2F8una-UAWaT2030R2-rUbK_mn4x1Am42NkUSnIwZY44olvUGNfwK0z1sUe2U9FSWLT_A3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما بعد از زدن بست نابی: بانک مرکزی کشورمان ۵۰۰ میلیون تن طلا دارد
🔴
طلای موجود در بازار ایران و منازل مردم ۵۰۰ میلیون تن است!!
🔴
این درحالی است که کل طلای موجود در جهان حدود ۲۰۰ هزار تن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146660" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
👈
مخابرات اعلام کرد از ۲۰ شهریور، تعرفه خدماتش رو ۴۵ درصد گرون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146659" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وضعیت این روزای ایران خیلیامون رو به بن بست کشونده
درآمد 95 درصد مردم الان ریالیه اما قیمت همه چی به دلاره
اگر بخوایم از زندگی عقب نمونیم
و جزو اون 95 درصد مردم نباشیم چاره ای نداریم جز اینکه درآمدمون دلاری باشه
همه وارد کانال زیر بشید لینکشو گذاشتم  همه رو به درآمد دلاری میرسونه لینک کانالشو میزارم عضوش بشید
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146658" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل ،کاتز :هرگونه حمله به اسرائیل از سوی ایران، به هر دلیلی و از هر مکانی، با پاسخی قوی و بی‌سابقه مواجه خواهد شد.
🔴
پاسخ به ایران شامل تأسیسات اصلی انرژی آن خواهد بود.
🔴
این حمله‌، ایران را دهه‌ها به عقب بازمی‌گرداند و آن را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146657" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRUBARChDvbQiA7wwyHxty_7cco75GpzFBqerfBAFGW-hA6u-0JeK-pZ7Q621SBPVRcAv3_23yO4WamyJV0tI_BObJ_CCBXLYGdA6yk9J91Diw5U1X5KR7bk41CbYDWArc7jDSdpXmNqL-iYbanqhAYLDXshUdL7souBS2sj_AnaU6jhSrHBasUe6JmFlvly8ZRy39csM0mEDxgFdhFrtFHqAatDmy07cEkjduDHup1LjT-Bak7atDn_ySyO1oZFeLqqHA63RymAcJ5iiTgSVm2RAE_BSTQTVu1iFlTU-YmebzKVEXbgYccoZ2quBorAq6gax6VSXie9owokdnnCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید صادق حسینی، خبرنگار: در روزهایی که کشور درگیر جنگ و محاصره است هنوز کسانی هستند که مسئله‌شان حجاب، قطع اینترنت و تعطیلی کافه‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146656" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp2_cuQBE-sA-w_h5USdf-QZr285iCPPWrac40nGxWMsR1sKwwsiNQBgjQV0-s-rD36jF3uN8-INrduHD5tlEMfzsOovuOf5SDt1bRUD2TvZRcx8Uwb1fQSePWslRiDTha8f0MFJNyDg7YLK3r5NdJu2CpfPlxWXmEo1JPfGOrZP49npKvDRekFGZADXbiTVWl2K0gjrzcYT3y9KC1o2lJDKnUP4ISRIZ908cRY7ApjlChAUgwgH8y25EBktF2dnHHLBmirf-25oiXVLgIJewiC2fC32WbZ7uN9jYN34tJFuQdc5-L8cryjf9qWy-p5J5NAooduzdn90notKyIUV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۲.۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146655" target="_blank">📅 13:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شرکت مخابرات ایران در اطلاعیه‌ای، از افزایش ۴۵ درصدی تعرفه برخی خدمات ارتباطی از ۲۰ شهریور ۱۴۰۵ خبر داد.
🔴
بر اساس ابلاغ وزارت صنعت، تعرفه مکالمه تلفن ثابت با تلفن همراه، تماس‌های همراه با همراه و پیامک تلفن همراه تعدیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146654" target="_blank">📅 13:21 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
