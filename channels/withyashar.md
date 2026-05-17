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
<img src="https://cdn4.telesco.pe/file/Djkz2xaIjtNyBioPz-ZWNDJkWkjdX3d8rdmuTscYXyct0K2YbsoTfD9H_vYgrL0Rhe_PIY6S_37F4KbP5g43-DNE-YBa7aGy_DrIbYi3ilDI_yBEo7jCD2N-CNA95E_6WZZqz5LoGHDnyDnv8UUNoPoZzAKhTyhI3FGN_216FCzu1LKHfwaRthuHbZD4ZVLL9YpkywMElIdI2PuA7AiJS3Qc92o2GCbe7kIstCM8_8xPglzFFQ4Zfotah8J76VfT15n6Bd1q6kNQ_yITTCWx2RpRiB1n16fM9HLZoEiAZRWS8yZT7r7z_9-P3Wufo-W1MSMDuCAXZ-FiUPgLNA8vmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 263K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 20:17:40</div>
<hr>

<div class="tg-post" id="msg-11495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c29a07582.webm?token=FgxDmoroBdaLCikvMFtZReiI3lcsSWaiJ14xvdCJg9qBll_wVdVzvqBmFS1Bk-TTyahWIdzL3DF10mXb8Y6JmdqHd4ga3f4ULDjhNhR7aWvq7j4pmzGOYnKTNTmrH10U6DDqBCXKuLofN_8rP1VuUdrkWCSgYWgEw_eUXA2_4A4gDhfCQ88atpngJN8NuBgvqf6eWmX27rPIvbFIaAb5fO98PQdrjwEmi9B8LAz4CkNGYb4wvNdPWsywMgsSZ16IiiCVUZfz-95W7JpzxJKiPTJuYJlvBW73lLlqKcUpfNeuUjYgljJBTSAL8RhJUa6uTqh2sId8aW0aaeJCCy6x5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c29a07582.webm?token=FgxDmoroBdaLCikvMFtZReiI3lcsSWaiJ14xvdCJg9qBll_wVdVzvqBmFS1Bk-TTyahWIdzL3DF10mXb8Y6JmdqHd4ga3f4ULDjhNhR7aWvq7j4pmzGOYnKTNTmrH10U6DDqBCXKuLofN_8rP1VuUdrkWCSgYWgEw_eUXA2_4A4gDhfCQ88atpngJN8NuBgvqf6eWmX27rPIvbFIaAb5fO98PQdrjwEmi9B8LAz4CkNGYb4wvNdPWsywMgsSZ16IiiCVUZfz-95W7JpzxJKiPTJuYJlvBW73lLlqKcUpfNeuUjYgljJBTSAL8RhJUa6uTqh2sId8aW0aaeJCCy6x5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/withyashar/11495" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتحاد باید شکل بگیره ! حتی بچه هیئتی ! تغییر رژیم شکل میگیره ولی تغییر عقیده کار یک شبه نیست و باید هر دو سمت شل کنند ! من خودم کافرم ولی تیم باید تکمیل باشه ! آس پیک شخص شاهزاده رضا پهلوی تنها هستش ! ترامپم مارو میره قاهره شک نکنید !</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/withyashar/11494" target="_blank">📅 20:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محمد پروین دوست خوبمه امیدوارم با تغییر جهت به سمت مردم برگردند</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/withyashar/11493" target="_blank">📅 20:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72df07c21c.webm?token=sqJplB3ulBqg-5d8SU7T9vsM16vg6FeuG8uXAmMtC39nrtWpKOe6jXFA-pp98vVIrOc5vOvnAfqewaCdFv3mxVhOOWv96jjByYfOndxTaJv4hdscuVZjeI9lL23lLXorGG9iwDAn5NxlSWr9A-qhwCkia-fom2-wzPWBxtOCck7SYhgN70X2u9f_RtGT2GAdgQ8yfTApvQqEWjWoDC3sRRIgEAvNRFiD78D3zjMWej8hChWCMVSuQp-6qnCTF5d-WuhSf8bg7vhb4ToaW5mlwi-TzqYocvuteLc14rGwgPMVuZ7DT6Dnrcu-TZ7Sb2ZXnFe09_vI_NpXuP2CRYakgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72df07c21c.webm?token=sqJplB3ulBqg-5d8SU7T9vsM16vg6FeuG8uXAmMtC39nrtWpKOe6jXFA-pp98vVIrOc5vOvnAfqewaCdFv3mxVhOOWv96jjByYfOndxTaJv4hdscuVZjeI9lL23lLXorGG9iwDAn5NxlSWr9A-qhwCkia-fom2-wzPWBxtOCck7SYhgN70X2u9f_RtGT2GAdgQ8yfTApvQqEWjWoDC3sRRIgEAvNRFiD78D3zjMWej8hChWCMVSuQp-6qnCTF5d-WuhSf8bg7vhb4ToaW5mlwi-TzqYocvuteLc14rGwgPMVuZ7DT6Dnrcu-TZ7Sb2ZXnFe09_vI_NpXuP2CRYakgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد  علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.  پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/withyashar/11492" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد
علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.
پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده از بیمارستان مرخص می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/withyashar/11491" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شبکه عبری کان: نتانیاهو و ترامپ، بیش از نیم ساعت با یکدیگر تلفنی گفت‌وگو کردند و در مورد امکان از سرگیری درگیری‌ها در ایران و همچنین سفر ترامپ به چین بحث و تبادل نظر نمودند
@withyashar</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/11490" target="_blank">📅 19:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕭.𝕽</strong></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/withyashar/11489" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWsC3t1yhAqe6iMznKxtm-kKjAHG60gZkxIkFGQUonRKhdHYUOJ0Zl4KYu6IlVB47XKLN8mUVRLFeR79sdnvBWGGQzLRbxNo9GGXjVZvPJUt3C4hlUxYhmyVmvUq4LsZgZrelRbSQI60acb5PL-TScT4Dwwgb8PFWF8B0TZD0ZYx8M8ztJtZgJSP9WA3V6bztj44XVdDPlOeQe8lA71ylm9_ObyW8YI5iD4yovjXNKAiUATuzHp10umMMwVLjVIbdqnkC5LSoypoZOK_pRh36GD4wEhdSDTDt1xLiVPQbzKxrZY2vESPW7S3fcPs0Iyysa0OiPPKKOUjoqxysFNkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/withyashar/11488" target="_blank">📅 19:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زیرنویس شبکه العربیه:
قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده صادر کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/withyashar/11487" target="_blank">📅 19:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زیرنویس
شبکه خبر: هشدار درباره عملیات غیرموجه علیه کشورهای منطقه و انتساب آن به ایران
یک مقام آگاه نظامی: ایران همه کشورهای منطقه را از افتادن در این دام رژیم صهیونیستی برحذر می‌دارد.
@withyashar</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/withyashar/11486" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سناتور لیندسی گراهام در مورد ایران:
طبق تحلیل من، هیچ نشانه‌ای وجود ندارد که افراد مسئول فعلی با گذشته تفاوتی داشته باشند - آنها هنوز می‌خواهند جهان را به وحشت بیندازند، اسرائیل را نابود کنند و به دنبال ما بیایند.
بنابراین شما آنها را بیشتر تضعیف می‌کنید. کاری که رئیس جمهور ترامپ انجام داده از نظر نظامی شگفت‌انگیز بوده است. زیرساخت‌های انرژی، نقطه ضعف آنهاست. برگردیم به بحث جنگ، من انرژی را در صدر فهرست قرار می‌دهم.
من خواستار آسیب رساندن به این رژیم هستم. بیشتر به آنها آسیب بزنید، شاید آنها به توافق برسند. اما در حال حاضر فکر می‌کنم آنها سعی می‌کنند منتظر بمانند و بازی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/withyashar/11485" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کیهان لندن : آماده باشید که احتمالا آمریکا و اسرائیل به زودی حمله می‌کنن
@withyashat</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/11484" target="_blank">📅 18:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حریق در یک ساختمان تجاری در خیابان جمهوری تهران
سخنگوی سازمان آتش‌نشان:
ساعت ۱۷:۱۴ دقیقه یک مورد حادثه آتش سوزی در یک ساختمان تجاری به آدرس خیابان جمهوری بعد از خیابان شیخ هادی به سامانه ۱۲۵ اعلام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/11483" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mehmooni (iG @yashar)</div>
  <div class="tg-doc-extra">Amir Tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11482" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/withyashar/11482" target="_blank">📅 18:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=RlmY1yipUYtQD7U4Ygoppo6STOW5GSNWajTw90Zn4PXCsyTOEaA1fltxvFxR-Z_2XWggdbTsMpDxmz4VvWM3RqxyapC5AIh8IxClGri_K7_VHJ3vLW8lUTKx79M85BK4NgeizuXHyQME5mcFrjBIZ_wzTr10b98a4y7Owb0ZFwjje69DOWrZEPifhtvw_mF_k0DVyTUrmCNjABE3quP3SysuqJSckvVbdySu-2ghMPAfudceh1fhguGTI_OZHogoFbOi0FFGUAV5C3zGUICVVNUFW003HIpEyLzRBYzTlEsIILAOQzpxlNGVwNLIPXx-qxrVqLJkMf0t47WH2dR5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=RlmY1yipUYtQD7U4Ygoppo6STOW5GSNWajTw90Zn4PXCsyTOEaA1fltxvFxR-Z_2XWggdbTsMpDxmz4VvWM3RqxyapC5AIh8IxClGri_K7_VHJ3vLW8lUTKx79M85BK4NgeizuXHyQME5mcFrjBIZ_wzTr10b98a4y7Owb0ZFwjje69DOWrZEPifhtvw_mF_k0DVyTUrmCNjABE3quP3SysuqJSckvVbdySu-2ghMPAfudceh1fhguGTI_OZHogoFbOi0FFGUAV5C3zGUICVVNUFW003HIpEyLzRBYzTlEsIILAOQzpxlNGVwNLIPXx-qxrVqLJkMf0t47WH2dR5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/11481" target="_blank">📅 18:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم  نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/11480" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA i</strong></div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم
نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/11479" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی را نمی‌توان تغییر داد همانگونه که یک گرگ را نمیتوان تبدیل به میش کرد
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11478" target="_blank">📅 15:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=CX3gfTylUMTdQmrcgL-ZX7149OTNiIra5G0KpMqjKI8r2a1htn-1I4KPnB3jqBF8whZbTSIVbGszCv2-61tZUzXqQhKeK0Xg4KTQGtdMUi3MqiFqoQA6bU_epwMNCuWS8ZCkMSpK66YmL2Vd4l4W0qftIKksJBoXNY7E-PPWQemgoHUNtDaGxZzi8bnHtuO_WBTU5bRyEioHLdQGC1gX_G3oROWHxhu3bTbAtdzxsLkTaWi75vBhWC488ooanq_S4WFCboBwYTvBakzeKy2MZZ9L9Ztt0bNFNGuG2-YCzZC4Q61Ch3M8twh3kYHsb1urTCbt9tE2j3umfZjKdSDvWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=CX3gfTylUMTdQmrcgL-ZX7149OTNiIra5G0KpMqjKI8r2a1htn-1I4KPnB3jqBF8whZbTSIVbGszCv2-61tZUzXqQhKeK0Xg4KTQGtdMUi3MqiFqoQA6bU_epwMNCuWS8ZCkMSpK66YmL2Vd4l4W0qftIKksJBoXNY7E-PPWQemgoHUNtDaGxZzi8bnHtuO_WBTU5bRyEioHLdQGC1gX_G3oROWHxhu3bTbAtdzxsLkTaWi75vBhWC488ooanq_S4WFCboBwYTvBakzeKy2MZZ9L9Ztt0bNFNGuG2-YCzZC4Q61Ch3M8twh3kYHsb1urTCbt9tE2j3umfZjKdSDvWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:   با اعلام مدیر کل آموزش و پرورش تهران؛ دانش آموزان پایه های هفتم تا دهم دیگه امتحان خرداد ندارن و با توجه به عملکرد علمی یکساله سنجیده میشن.
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11477" target="_blank">📅 15:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک‌تایمز:  آمریکا به عراق دستور داده بود که طی دو عملیات داخل ایران، سیستم‌های راداری خود را خاموش کند و عراق این کار را انجام داد
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11476" target="_blank">📅 15:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: امروز با رئیس‌جمهور ترامپ حرف میزنم،چشممون روی ایران بازه، برای هر موقعیتی آماده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11475" target="_blank">📅 15:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFpyYxYfNgx5Ea81epOvADl3EKzFKiJgM0N8P1rZeop4H-IRfbBa_8oav7XmhRDhMj1hmEIPs8BwSVi2M847oj_0xCrCApHi40n3ZhGviyRrFPxeJ8bmVbXsTmESN1qMTpU_n9XYXtzoYeibaJqlQ3NBpTgLYFXKyaCrDUxVVvHsjvjWhNgLLq1BpcXZu_JKHqMWI1FZlAwybRyg4VsDbOcAdW09gHhdB3ZzWWq3dEgW_i9Y3IcIBlWl3y1cAD-5P1R285H8tdLkW0pFfJZXxvu3a6mIqB2BdknqrqBPhADqJOlsCJypL6tqQD6iXbU4Gp7_1t0l__vzoii3EQ30Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: یه کشتی اسرائیلی تو خلیج فارس توقیف کردیم که خدمه‌ش عکس علی خامنه‌ای و مجتبی خامنه‌ای رو روی دیواراش نصب کرده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11474" target="_blank">📅 15:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو: ما در غزه اکنون چیزی را در اختیار داریم، دیگر ۵۰٪ نیست... اکنون ۶۰٪ است. این وضعیت امروز است.
ماموریت ما یکی است: اطمینان حاصل کنیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
ما محدودیت بودجه نداریم. هر چقدر هزینه داشته باشد مهم نیست، شک ندارم که اسرائیل اولین کشوری خواهد بود که راه‌حلی کامل برای حملات پهپادی ارائه می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11473" target="_blank">📅 14:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو با ترامپ تلفنی گفتگو می‌کند
رسانه‌های عبری: نتانیاهو امروز با توجه به تحولات و تنش‌های منطقه با ترامپ صحبت خواهد کرد.
@withyashar
امروز همچنین اسرائیل جلسه امنیتی برگزار میکند</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11472" target="_blank">📅 14:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تایمز:  انگلیس برای جنگ آماده می‌شود
این رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11471" target="_blank">📅 14:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مشاور سابق پنتاگون:تحرکات سطح بالای نیروی هوایی آمریکا در خاورمیانه شدت گرفته آماده باشید
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11470" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دارم میرم یات تولد ، شاید دایرکت ها رو درست نبینم کم اختلال داریم ولی من هستم
😬
🙌🏾</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11469" target="_blank">📅 12:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11468" target="_blank">📅 12:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11467" target="_blank">📅 12:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">داداش شما رئیس سواک میشی شک نکن</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11466" target="_blank">📅 12:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کنم ساواک روزی که برگرده باید اول به من بگه دادچ آرشیوتو بیار
🤣</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11465" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=Zc9bnsqwzxM8SCODszsA0xcIXuV8VFwBoPalRJzAzrQd0uCBd0SV-X6pYBDW70dsRhl8TvmpXrCkL_A4QMukKoIWNu8PNXtjgx9uhYebNvrUfLV8iMhHV5cq9XI94D2fge0kxrGQ9qbCsGheQuTk1GyZdQ5muLEcD4SbnS8hAz663jJ0-3Ds_otQAmk0KzbJ7gwL0sD0p8H2dTADnlmEfmf4hU0_L47x2g7oJhznSR9pD8cU6qN0WAka3pv_zso5i1ORlbmuMvxHAyQL39QI4PqIm-rsQ3s776nkXsUUM1jpcNxxTetMQ4GmcvkRgWDOP9B2L_Ftr3ywuUMzDtVt6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=Zc9bnsqwzxM8SCODszsA0xcIXuV8VFwBoPalRJzAzrQd0uCBd0SV-X6pYBDW70dsRhl8TvmpXrCkL_A4QMukKoIWNu8PNXtjgx9uhYebNvrUfLV8iMhHV5cq9XI94D2fge0kxrGQ9qbCsGheQuTk1GyZdQ5muLEcD4SbnS8hAz663jJ0-3Ds_otQAmk0KzbJ7gwL0sD0p8H2dTADnlmEfmf4hU0_L47x2g7oJhznSR9pD8cU6qN0WAka3pv_zso5i1ORlbmuMvxHAyQL39QI4PqIm-rsQ3s776nkXsUUM1jpcNxxTetMQ4GmcvkRgWDOP9B2L_Ftr3ywuUMzDtVt6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان بحث داغه دیدن این ویدیو شاهین نجفی هم که در اوایل شروع ‌به کارش برام فرستاد خالی از‌ لطف نیست ، من امید وارم همه با هم متحد باشن و مشکلات تموم بشه
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11464" target="_blank">📅 12:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=Ra7U7wnm-Comh8MEt4VwLczbWGJYmXgjc58c2j17RMk3092r2mA5E2IkO04LqXtAggQZiL4Gc4nuFKCOtnPdhlwy6DZbWgmklsQyaKYA1CBvdZEEDH6En95RJFGrsHDgYdB8TPpFLGP6r4BPIQXjMMFau4yDitIIERU__Jo08C-19-12daNrvXc2qeFf6Ed0txmzScu3r2yZpyHdyHyv2mCfb4z4NfMGqXUL75Sc_OhdBjk6LaCnlUjhWIeAKBf22MZ0-09Hdx1LY5XWXFkQvCQikNBxm9V0fgKR0rC_OfG9QnEIHQaptLVDQCFOxQ_46mAmT_3n07cfkkWK4Q7oMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=Ra7U7wnm-Comh8MEt4VwLczbWGJYmXgjc58c2j17RMk3092r2mA5E2IkO04LqXtAggQZiL4Gc4nuFKCOtnPdhlwy6DZbWgmklsQyaKYA1CBvdZEEDH6En95RJFGrsHDgYdB8TPpFLGP6r4BPIQXjMMFau4yDitIIERU__Jo08C-19-12daNrvXc2qeFf6Ed0txmzScu3r2yZpyHdyHyv2mCfb4z4NfMGqXUL75Sc_OhdBjk6LaCnlUjhWIeAKBf22MZ0-09Hdx1LY5XWXFkQvCQikNBxm9V0fgKR0rC_OfG9QnEIHQaptLVDQCFOxQ_46mAmT_3n07cfkkWK4Q7oMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش به تاریخ پیوست…
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11463" target="_blank">📅 11:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11462" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عباس عراقچی، اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11461" target="_blank">📅 11:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/11460" target="_blank">📅 11:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.A</strong></div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه
اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/11459" target="_blank">📅 11:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11458" target="_blank">📅 11:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11457" target="_blank">📅 10:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11456" target="_blank">📅 10:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11455" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11454" target="_blank">📅 10:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEu9aRip1OZW1_pHaRHYTiSAjwc92IsM3buNmkZs2s1tm4R-j-I3PIytlWAUVM0200Lvu6hBJ1K3FwgF5rzx7rjq1RF0yd8UgBXrL5KCmumeUyRwMNdm69n_8uWQ6OwvkfVN5Hmx0Mhb5cb-WqL9bKN_qCeZ3w8Xr167FvsFJ0Sd-CV4Hj4TwZmCIgDG0N4DGoi6B3rdEGu_RK807k2xGXZHbvISgqntq3CB-DJm3ic1gx9lOQ7N247PE0la4URVRwYK2NpHAe-k5ehygg5cmF5K6-D3xqwu_ciOni_5wL5Nkfj19DGS-bLEwF-Cq6rviyADC5NpdSVwzp95M2CQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11453" target="_blank">📅 10:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11452" target="_blank">📅 10:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11451" target="_blank">📅 10:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11450" target="_blank">📅 10:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYas</strong></div>
<div class="tg-text">عجب جمله ای: اهدافت رو از ملی به مالی تغییر میده. رحمت به شیری که تو خوردی یاشار
🙏
💪
💚
🤍
❤️</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11449" target="_blank">📅 10:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">این لحنم نبود
🤣
🤣
🤣
🤣
بد گذاشتی ک</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11448" target="_blank">📅 10:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولت براچی گذاشتی تو</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/11447" target="_blank">📅 10:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">ولت براچی گذاشتی تو</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11446" target="_blank">📅 10:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11445" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پدرم در اومد رسیدم تلگرام چرا روبیکا خبر نمیزاری یاشار</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11444" target="_blank">📅 10:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms.r.s</strong></div>
<div class="tg-text">پدرم در اومد رسیدم تلگرام چرا روبیکا خبر نمیزاری یاشار</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11443" target="_blank">📅 10:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاون وزیر خارجه روسیه دقایقی پیش از قریب‌الوقوع بودن حمله آمریکا و اسرائیل به ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/11442" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تاج: فیفا برای هر ۱۰ شرط ما برای حضور در جام جهانی راه‌حل ارائه داده
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11441" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11440" target="_blank">📅 10:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAhmadreza</strong></div>
<div class="tg-text">نظرت راجب فرستاده پاکستان چیه؟ بنظرت احتمالش هست بتونه کانکت کنه و جنگ مجدد درصدش کم بشه ؟</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11439" target="_blank">📅 10:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11438" target="_blank">📅 10:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEnrique Batista</strong></div>
<div class="tg-text">داداش یاشار
خیلی از کانالا دارن میگن که هواپیماهای c17 آمریکا دارن خاورمیانه رو ترک میکنن .
این یعنی چی؟</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11437" target="_blank">📅 09:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سلام وقتت بخیر با توجه به اینکه این اتاق‌ جنگ اسرائیل تیک زرد داره هنوزم فیکه؟  چون تیک زرد خریدنی نیست تا جایی که من خوندم</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11436" target="_blank">📅 09:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdyar</strong></div>
<div class="tg-text">سلام وقتت بخیر
با توجه به اینکه این اتاق‌ جنگ اسرائیل تیک زرد داره هنوزم فیکه؟
چون تیک زرد خریدنی نیست تا جایی که من خوندم</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11435" target="_blank">📅 09:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باز این اتاق جنگ فیک اسراییل توییت گذاشت الان همه میفرستن میگن یا خدا
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11434" target="_blank">📅 09:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af61de15c.mp4?token=SBPmzutnOlL6iV0aZJW1te9bcEg15zpCALrFO51IDIRAP2PW4Yo_1r7xnSIjhvYqUeTlrZm0NiZ2qCnnMMl5AJKF0WrutVLa2lq0sI4AgL3QLskVEa84GuQaqOxDVauE0VY4WKiumcThLI2ImUrKthpb4bf72IHrUwLuS7TTD-2Mq6ZZN8e-bTzQVeu0HpWi3gtF0kwR36yQlAMXm2hUBPJfCAJY_iqAvdm3051ZdgTtStEO4ZxPpT_lhvGSCeQQ5Sp6QWH4MYmJ5k9JBOSp0iZAGU1QAzViydDbXkIteMNt6VmtJQzJHpS5YNa2wZDeJrUd9f431cLWQ6KKv-dnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af61de15c.mp4?token=SBPmzutnOlL6iV0aZJW1te9bcEg15zpCALrFO51IDIRAP2PW4Yo_1r7xnSIjhvYqUeTlrZm0NiZ2qCnnMMl5AJKF0WrutVLa2lq0sI4AgL3QLskVEa84GuQaqOxDVauE0VY4WKiumcThLI2ImUrKthpb4bf72IHrUwLuS7TTD-2Mq6ZZN8e-bTzQVeu0HpWi3gtF0kwR36yQlAMXm2hUBPJfCAJY_iqAvdm3051ZdgTtStEO4ZxPpT_lhvGSCeQQ5Sp6QWH4MYmJ5k9JBOSp0iZAGU1QAzViydDbXkIteMNt6VmtJQzJHpS5YNa2wZDeJrUd9f431cLWQ6KKv-dnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنته هرکسی که توخالی باشد بالاخره معلوم میشود
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11433" target="_blank">📅 02:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11432" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران به عبری ی توییت زد ک  پیام روشن بود لفاظی نکنید... המסר היה ברור: אל תהיו רטוריים... یعنی کار ایران بوده؟ مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/11431" target="_blank">📅 01:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoul</strong></div>
<div class="tg-text">ایران به عبری ی توییت زد ک
پیام روشن بود لفاظی نکنید...
המסר היה ברור: אל תהיו רטוריים...
یعنی کار ایران بوده؟
مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/11430" target="_blank">📅 01:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر جرالد فورد به خانه بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/11429" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سنگین در بیت شمش اسرائیل و دیده شدن ابر قارچی گزارش شده که در کارخانه شرکت تومر رخ داد. این شرکت موتورهای موشک سنگین و سبک، از جمله موتورهای پیشران موشک‌های ارو ۲ و ارو ۳، موتور موشک هدف سیلور انکر، موتورهای ماهواره هورایزن و موتورهای موشک باراک ۸ و باراک ام‌ایکس را توسعه و تولید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/11428" target="_blank">📅 01:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/11427" target="_blank">📅 01:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Lcjls6ZHH89NtjRz6MEYfAimeiRRmsPSyJw9Llb_mzg0a5A0k0Bx9nkCxZHticm3NWeiou_xu0uUu-IGLN9a8HkD7M6QVr3JiL9yYWdYXCRQJyt6Fy-eziRQ9BTB5r1CaSQpYwbr99pl0F2jqIP7p6DYToVYu6eCo0U6ruEK_3CL0fyLUSHBTiHCAuLjK0ucvv2iR8MoHisP-EjrqLefPgWdrw6b9ouCMSR4ZwwHi2NSvDaJ3qaG8el5sUCZ1BbMLGErpb0oM9nXnoTyIObdEZsqQ6ZpT6bKtda49-Odgebpbrh-kiiVBB6I0tYvJEzIdrrTu1238T_h4fzmMWp-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Lcjls6ZHH89NtjRz6MEYfAimeiRRmsPSyJw9Llb_mzg0a5A0k0Bx9nkCxZHticm3NWeiou_xu0uUu-IGLN9a8HkD7M6QVr3JiL9yYWdYXCRQJyt6Fy-eziRQ9BTB5r1CaSQpYwbr99pl0F2jqIP7p6DYToVYu6eCo0U6ruEK_3CL0fyLUSHBTiHCAuLjK0ucvv2iR8MoHisP-EjrqLefPgWdrw6b9ouCMSR4ZwwHi2NSvDaJ3qaG8el5sUCZ1BbMLGErpb0oM9nXnoTyIObdEZsqQ6ZpT6bKtda49-Odgebpbrh-kiiVBB6I0tYvJEzIdrrTu1238T_h4fzmMWp-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب بیداریم !
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/11426" target="_blank">📅 00:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏ جیمی دیمون، مدیرعامل جی‌پی‌مورگان چیس، درباره ایران:
‏آنها ۴۷ سال است که تجاوز، قتل و کشتار می‌کنند. دنیای غرب اجازه جنگ‌های نیابتی را داد.
‏ما درس عبرت گرفتیم - باید سال‌ها پیش به سراغ سر مار می‌رفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/11424" target="_blank">📅 00:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXFqG_9ZtE0VexMbKRXGK_ZkOyW_XENgnaQ5GVFLXYsLKUmnDBiFmREPiYocYM43h9PvSrx6tOTNGJolrz5vl0elW1wEqZh7dsouWrheaXPrXOb7Fa2-B3R306tSR5Q05aiZeTRkPpVN-Pl-rssFCXArZR4vrgxjhnEybedPe_zHZi80Dh6kkbZsK-8EX5IXgnmtcYwMQuiCTWrff4nWQljHP-fx-IgjBg2lkGyv6DCjLd5OHCExJjdAJrxfh01b6ynDX_6pGF77Q93bNKT0YtQPMX8oHHC4Wq1tr6P5aLYJEEpa4kr19rYkx7vfrnqeVG6nuy86aCvEia0X0yhKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امین صابرکار، دانش‌آموز ۱۷ ساله بسیجی بوشهری،‌ حین انجام تمرینات تیراندازی اشتباها با آتش خودی(فرندلی فایر
😬
) کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/11423" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@withyashar
فرهنگ ما همیشه غالب میشه</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/11422" target="_blank">📅 00:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=JsRDz7xlV2A8YjTk8Z-ObY5TrxCU_fl2w3BNOFeqKYQTCrC6CsRjMtPgXUYlpULnDR60lMrKOHBqzVBO4NuXsQctlzYy9mtHVy4sH02-G2nkKG6F2QXGmUN_y3vmQiHXo5zpMO28PVHEDbIgXTvjBixZCEahzmK5OcYDG2EixMZu4eOELaXJ-IgSXWSLKN3CIGP5fK9Ndni2ylbSNyd0HJeWT53L2sCHyDgo8vHQbNEijkhGktkbZ-1Opd7CwW4XV3vFmLLqat1c4MxK63llWrGtMTjB60PkigYM2t91gTDHby6qdyAxTQi-2A6ZMjCermF7BjoIHpH9Q7IZwM2FyxgEFZb0I37KrvaEkNhJdRNITFm2FCqyn_I2o3OEcnwzJaxdqXiXMXzslG7BnIQGBAQ7dxgP51LiKcHktD0ZMxuomvvytjgOPvRIb7KrSOhJ2mh27guOLfVUBD8gumHp7jU6MPpaFlU9m-Dl-ya4P-SM_TQoGMjGxSEe2a3f15pU-wfOTtImySC0k0K3VBCqqjLoN2EBGmi8xv3rMxWjPLWrQ1ligg-JQRJG1BHH6RgON-4IGpZCgqd__KHTvh3KSVyHhEjQUAtqzwVlHVvmzCvMZL8kRasgAYynODdoDKrFKGsr1mc8bxl9UzbNnRuDUnnOwcWNLTvNL118kHuThN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=JsRDz7xlV2A8YjTk8Z-ObY5TrxCU_fl2w3BNOFeqKYQTCrC6CsRjMtPgXUYlpULnDR60lMrKOHBqzVBO4NuXsQctlzYy9mtHVy4sH02-G2nkKG6F2QXGmUN_y3vmQiHXo5zpMO28PVHEDbIgXTvjBixZCEahzmK5OcYDG2EixMZu4eOELaXJ-IgSXWSLKN3CIGP5fK9Ndni2ylbSNyd0HJeWT53L2sCHyDgo8vHQbNEijkhGktkbZ-1Opd7CwW4XV3vFmLLqat1c4MxK63llWrGtMTjB60PkigYM2t91gTDHby6qdyAxTQi-2A6ZMjCermF7BjoIHpH9Q7IZwM2FyxgEFZb0I37KrvaEkNhJdRNITFm2FCqyn_I2o3OEcnwzJaxdqXiXMXzslG7BnIQGBAQ7dxgP51LiKcHktD0ZMxuomvvytjgOPvRIb7KrSOhJ2mh27guOLfVUBD8gumHp7jU6MPpaFlU9m-Dl-ya4P-SM_TQoGMjGxSEe2a3f15pU-wfOTtImySC0k0K3VBCqqjLoN2EBGmi8xv3rMxWjPLWrQ1ligg-JQRJG1BHH6RgON-4IGpZCgqd__KHTvh3KSVyHhEjQUAtqzwVlHVvmzCvMZL8kRasgAYynODdoDKrFKGsr1mc8bxl9UzbNnRuDUnnOwcWNLTvNL118kHuThN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوش جان میسپریم به فریدون عزیز تا من موتورم رو گرم کنم ویس بزارم
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/11421" target="_blank">📅 23:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZm-WAsBthphr3bFduDdjYgRpRdHcMsbJJ-F1tynGrhGtkqbPNLGioOn3F8xbd8Sv5oHia_KD_P2d2PEDO3e9d5wYkxoVFaPVTdz_DIyFMDYd6SUATZX10WJZeDK4649yN_gicJQUjbPEjsiSqF8Sj9upcQg_XuJvBz9iyId9mt3G4pn_RVWOD0mD1yY2haOy9LSnoDdz-4UTfRIU5rAQU1FBzd2dWyIky6DVecSG7MS9wJgSANJqgdwVN1k6gk6l4Q3suFFR84vfwE7Xj_oJzX3KzQ7YnC8vc0AeQ8TFZbwhnmGCsqMbaAyMZ4O_X7M1RufdiwBdJ5_Gj07o0ZP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آرامش فبل از طوفان
قایق تندرو با پرچم جمهوری اسلامی دیده میشود …
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/11420" target="_blank">📅 23:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/11419" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJdBKQ74rjfcEJPXudL5Hh2F7Clw4p2hL1JeQDWhdHZxA8oklWdWHat67ts1GElTmbg_5v0y-vrxT-2uPXGx7r-ACZGXqKfGYJp4wH9Yvvjf6nSQ6YeqIslyEqDjy3sjJ-9PhIBDUB-9HF5d7dx2ilp6ytJzT1Anv5acm_fVFA1PQHWXmWFQGM4wZnO26B86QZvRmQKQ12qA3EWQRPBoaNgeuq-Nv_yBBkLUFUp5-7LRgrdO7ASzEibQa8E5lVzWKcs7W8y_Q66Vxqe3OYjkvnQAcmeCdgzuNGTQrCKAx6UomgSWd5TvllwTOKPVBl3rm8EBAJuI3psCLKFAEyX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاورین شاهزاده (امیر اعتمادی و سعید قاسمینژاد) ، علی کریمی‌ رو به علت واکنش ‌به کنسرت و آهنگ شاهین نجفی آنفالو کردند  @withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11418" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست آینده تکنولوژی در ایران:
ایران می‌تونه به کره جنوبی تبدیل بشه، اما به دلیل وضعیت سیاسی کنونی به سمت الگویی شبیه کره شمالی سوق داده شده؛ جمهوری اسلامی در ذات خودش قابل تغییر نیست.
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/11417" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در بالاترین سطح هشدار برای احتمال از سرگیری جنگ با ایران است.  در صورت از سرگیری جنگ با ایران، احتمال دارد ایران در روزهای نخست ده‌ها موشک به سمت اسرائیل شلیک کند.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/11416" target="_blank">📅 22:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قلعه نویی در لیست نهایی جام جهانی آزمونو خط زد و گفت باشرف هارو دعوت کردم.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/11415" target="_blank">📅 22:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال استریت ژورنال : ایران و آمریکا بر سر یک موضوع توافق دارند در حالی که بن‌بست دیپلماتیک بین تهران و واشنگتن ادامه دارد, هر دو طرف می‌گویند که در حال حاضر درباره سرنوشت ذخایر اورانیوم غنی‌شده ایران بحث نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11414" target="_blank">📅 21:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو : اگه آمریکا دوباره بخواد عملیات نظامی علیه ایران رو شروع کنه، اسرائیل آماده‌ست
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/11413" target="_blank">📅 21:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFapo1414</strong></div>
<div class="tg-text">داداش ناموسا من اونجا بودم داد میزدم به شاهزاده میگفتم حتما با یاشار ملاقات حضوری بکن</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/11412" target="_blank">📅 21:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hy4MG0Xs0crPl-bdKMTxSKtOtSGeLF7DuOiGwQYlVR_emiUhUl8ur6rXwGeJ8GlvnNKkoaCogPgkvzddFWddnT5VEaVY4nPZ9N9KkTZtYT6cPTB2b5Q7VxNirE5OejYHgRDMLUrunu_UyuPzQYD7o4GI75mNWRELKa2_usw6jJaKXFqbnhqWyIEiRl2fACbX-VjGGXrH2QzdQdXoTHYf787Eu0LEHWNyUPWZbo0Sv0M5p5HSegScKfRYFC24BYrlXF4g13q3-F0pNBA-hbqXsb8RRJdX6VtueRPpBJQhoGJpRDwq1o2AOyRhMznjw-iqxJ7cpYZcaVQXBdu_jiMMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سخت ترین شرایط بهمون روحیه دادی، تو جلسه ی بچه های تکنولوژی با شاهزاده به یادت بودیم!
❤️</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/11411" target="_blank">📅 21:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرهاد مجیدی با البطائح به دسته دو امارات سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/11410" target="_blank">📅 21:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/11409" target="_blank">📅 21:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH.E</strong></div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11408" target="_blank">📅 21:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkk9VjPAGNuIHMLlMlS1fZGwCzD-L8oGMG0plfxK9E_1Pr-PQBqUbmO7vSSV6twCcja133KPKObNbBu3XhUrsbo37rvIIntvlok41uxkfxD3ROYEG49O1Kq_kA_UhKj9YWnC35d61FtN-VJtEYCtSfENK_pp-B_HNnlojd90R1lUS5DjNg5pElchVcQP7gJ60KD4GJ7B_NOUbKQLZ4ZjsVJkZK612QVlqTmjLbxZPA8U8uCGpjJiqcDZGbX8DAJW4j9YpCcRokfm5jiQ3nSeqtt3B86hm8ehq7QRFbLOtIhW9wkE9B6bQyoxBexNOrbUp2NDd12AB44zv-Ea7zkI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناوگروه  آبراهام لینکلن با سه اسکورت با سرعت به سمت دریای عمان می‌ روند  ، ۲۶ اردیبهشت. (مکان 260 کیلومتری چابهار)
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/11407" target="_blank">📅 21:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شبکه 13 اسرائیل: هم اکنون ارزیابی‌ها در اسرائیل بر این است که جنگ با ایران در روز های آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/11406" target="_blank">📅 21:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: اگه به آمریکایی‌ها آسیب بزنید، یا در حال برنامه‌ریزی برای آسیب زدن به آمریکایی‌ها باشید، ما شما رو پیدا خواهیم کرد و خواهیم کشت.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/11405" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ در گفت‌وگوی تلفنی با شبکه فرانسوی «بی‌اف‌ام‌تی‌وی»:
آینده مذاکرات نامشخص است اما اگر توافقی حاصل نشود ایران روزهای بسیار سختی در پیش خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/11404" target="_blank">📅 20:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">العربیه: طبق گفته منابع آگاه پاکستانی، در بحث تنگه هرمز، پیشرفت‌هایی حاصل شده است
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/11403" target="_blank">📅 18:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a350642e.mp4?token=VmUGKtYyXkHW6knxxW_M7-u6aeLn0SSeKtc_KrZH1iw_3HNUkX-GLbXGd_rpn81JdSiSO2uOo7mWbRPymtF_viS_AWx_lJ4UB-uu2o1MC1DyqCwPaKcODCzbZeKeZLJk_P9NfHXwCseLDwihrL9V-b0-nt3UK50Ff1QFwR_PJ-sZkuvn4SHdpyJ1uG2vN6SDv-d1jKn3ycVlMcmQXjUrYJnr-CI45GlrNonRVU3cdnjxjIoAiulL8DlF2yNrbJfZuVqjX2OAkFsyk1V-U0ttae7cuP_fapgd2l7owGDudfWTQKkkpA9V4VI-q1cjjwxcXyXWuNa2aVgXials8XJkgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a350642e.mp4?token=VmUGKtYyXkHW6knxxW_M7-u6aeLn0SSeKtc_KrZH1iw_3HNUkX-GLbXGd_rpn81JdSiSO2uOo7mWbRPymtF_viS_AWx_lJ4UB-uu2o1MC1DyqCwPaKcODCzbZeKeZLJk_P9NfHXwCseLDwihrL9V-b0-nt3UK50Ff1QFwR_PJ-sZkuvn4SHdpyJ1uG2vN6SDv-d1jKn3ycVlMcmQXjUrYJnr-CI45GlrNonRVU3cdnjxjIoAiulL8DlF2yNrbJfZuVqjX2OAkFsyk1V-U0ttae7cuP_fapgd2l7owGDudfWTQKkkpA9V4VI-q1cjjwxcXyXWuNa2aVgXials8XJkgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوئل نهایی ، وضعیت الان!
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11402" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTm bzx</strong></div>
<div class="tg-text">عرزشی ها اومدن که خبر مرگ بابای سپاهیشون رو زودتر تو چنلت ببینن
اخه از رسانه های دیگه ۱ ساعت حداقل جلوتری ستون
😂
🔥</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/11401" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpAKo19kfFiuk6LYOpnrOSbgbhaqSVS8nkq6GbXEgugjgbcPykusRgXv_2GxLhkIKAgjQLnZQGjZw0M4buLtHEM8oNM0MYpWL-Oz-7G_qaU_Zgs71vZFCqvPMrvcsFC-yYz2UIneviKhiF4hns0PloK0Py6ChkWL_SXKLoaz2hUY16fcZqFTCqNIWo0YGwf9oxOrLJLaY7Uy0fi5O3f0mxW7GBJtVaWZdRXNikNSemjEpXZ0vFSeAkeaF0K3q2Uip6lQUdaQ7Zzw7SpCiLzHNeuGuOA_kjCbc5t0_9mbasboG8fLWASYDBIUxSTGJw0TY0B2Zc9adKLXhT4j7cZHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ :
شوخی نداریم!!!
ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/11400" target="_blank">📅 17:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سقوط یک شهر پاکستان به دست جدایی‌طلبان
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/11399" target="_blank">📅 17:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فقط برای یک پست که نمیشه ببندم مهندس ! کلا ببندمم که یعنی میگی خنده رو از روی لب چندین هزار نفر بگیرم به خاطر ده نفر. ما اینجا هدف اصلیمون مبارزه با اخبار سمیه و روحیه دادن به مردم. اجازه بدید در عرزشی سوزترین رسانه ایرانی بسوزند و حرص بخورند</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/11398" target="_blank">📅 17:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from➖</strong></div>
<div class="tg-text">میتونی ری‌اکشن رو هم ببندی داداش!</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/11397" target="_blank">📅 17:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/11396" target="_blank">📅 17:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐝𝐢</strong></div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/11395" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
