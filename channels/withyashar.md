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
<img src="https://cdn4.telesco.pe/file/m6FbA8ifwlRRa5Zx9CVjJsLbwE8CKWrQvkRHjOzAct5NTYKwVKqpje030MpqtmxgmibQP7x7pyeCaHhnQBEnjXIU1gOvSaAtd5y3vqrEAAonw5vg6YfvyxZ7pA2UOfmYvpk0GwodTQvBiJKwmlwNGbLBRcZjI0wlYlIh3HoJsJ3_sGvh3k76MmZvE4A8vRknE647BFi6djNdtyHs7cn_SRbN9BOSV5QprlZnPxMDmOZ0XZ-9r2VnqTB5DyNb1igRCE_3oPiOD5lYhrTbX60FvSTA7_KAEXUO2MapvIGYcqCAIDlmHAcQbah2D5O3MUXR03ZXQA2FlB_ImRjCrJroYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 268K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 10:11:43</div>
<hr>

<div class="tg-post" id="msg-11921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سفارت پاکستان در تهران اعلام کرد، وزیر کشور پاکستان بار دیگر با عباس عراقچی وزیر خارجه ایران دیدار کرد تا پیشنهادات برای حل اختلافات در مذاکرات با آمریکا را بررسی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/withyashar/11921" target="_blank">📅 09:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رأی‌گیری درباره اختیارات جنگی ترامپ، به دست جمهوری‌خواهان به تعویق افتاد.
@withyashar</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/withyashar/11920" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/11919" target="_blank">📅 06:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/11918" target="_blank">📅 05:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">تو خواب نداری یاشار؟!
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/11916" target="_blank">📅 05:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زمانی بدتر میشه که پاسخ با پارازیت میاد و بعد با پارازیت جواب داده میشه ، کلا دو دکل اصلی میرن کنار پارازیت ها میوفتن به جون هم و تصویر کاملا از دست میره و برفکی میشه !
@withyashar</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/withyashar/11915" target="_blank">📅 05:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11913">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خیلی ساده است یکی یه سیگنالی میده برای یک جوابی بعد تمام پارازیت ها میان رو موج!   خوب بزارید پیغامش درست برسه و جواب بگیره !</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/withyashar/11913" target="_blank">📅 05:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11912">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خدا نکنه یکی یه انتقادی کنه همه مافیا ها میان تو بازی خودشونو سفید کنند
🤣
به هر حال ما وارد موج نمیشیم و فقط خبر ، تحلیل و فرهنگ سازی رو ادامه میدیم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/11912" target="_blank">📅 05:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11911">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak Mosaferi</strong></div>
<div class="tg-text">یاشار چرا همه به جون هم افتادن
کی درست میگه
چیکار میشه کرد</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/11911" target="_blank">📅 05:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11910">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وبسایت خبری «ددلاین» گزارش داد شرکت فیلمسازی «یونیورسال پیکچرز» با همراهی مایکل بی، کارگردان آمریکایی، در حال تهیه یک فیلم سینمایی درباره نجات دو خلبان آمریکایی است که پس از سرنگونی جنگنده «اف۱۵-ای» در عملیات «خشم حماسی» در داخل خاک ایران گرفتار شده بودند.
بر اساس این گزارش، این فیلم بر پایه کتابی در دست انتشار از «میچل زوکاف» ساخته می‌شود که انتشارات «هارپرکالینز» قرار است آن را در سال ۲۰۲۷ منتشر کند.
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/11910" target="_blank">📅 04:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11909">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/withyashar/11909" target="_blank">📅 03:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا حتماً داره آخرین اولتیماتوم رو میده….
@withyashar</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/withyashar/11908" target="_blank">📅 03:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11907">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اتاق جنگ با شما : سیریک جنگنده اومد ارتفاع پاین تو شهر مانور داد الان
@withyashar</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/11907" target="_blank">📅 03:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11906">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-</strong></div>
<div class="tg-text">درود ياشار جان
سيريك الان نزديك صبحه و يهو صدا جنگنده اومد،رسما ا بالا سرمون رد شد،و چند ديقه بعد پنجره ها لرزيد</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/11906" target="_blank">📅 03:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11905">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d5cbcf6a.mp4?token=MPUNkeD_gbqCNbDR6FEBVS7izqGVgQqsAOoIiU9eCkA4GmhcgNABbqggQf2Di2DwLSNlL9Po1i5aVl8AR7ghQBvZIeVnbEb1Jt6vHl-zfnCr3DkxG-vPTuajFAuN2s83skpSvovWfsrHGmjo6FLY3XQp4NKOOoo7iHATasmJ3ULhNRsp2d7AL6y5FPREVxEzoMmWvwa-cMUkHZ_m7ShLlSryPGHX_jI9iYUOC2ernAUgcCY0G8nnG_eZf0g1IhcfJN3UEOchYw64ZHi5VjayYlrZ7NUXE_uDuxo-Z0WBVFInL8ko2Kqre4ZaHHm9iD-fUO76v0gU-ceNvamU1CFZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d5cbcf6a.mp4?token=MPUNkeD_gbqCNbDR6FEBVS7izqGVgQqsAOoIiU9eCkA4GmhcgNABbqggQf2Di2DwLSNlL9Po1i5aVl8AR7ghQBvZIeVnbEb1Jt6vHl-zfnCr3DkxG-vPTuajFAuN2s83skpSvovWfsrHGmjo6FLY3XQp4NKOOoo7iHATasmJ3ULhNRsp2d7AL6y5FPREVxEzoMmWvwa-cMUkHZ_m7ShLlSryPGHX_jI9iYUOC2ernAUgcCY0G8nnG_eZf0g1IhcfJN3UEOchYw64ZHi5VjayYlrZ7NUXE_uDuxo-Z0WBVFInL8ko2Kqre4ZaHHm9iD-fUO76v0gU-ceNvamU1CFZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : یه خبرایی هست …
@withyashar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/11905" target="_blank">📅 03:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Martik (t.me/withyashar) – Parandeh (IG @yashar)</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/withyashar/11903" target="_blank">📅 03:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11902" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/11902" target="_blank">📅 03:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/11901" target="_blank">📅 02:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11900">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐏ـٍٍٍٍٍٍٍٍؔؑؒـٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍِِِِِِِِِِِِِِِِِِِِِِِِؔؑؐد</strong></div>
<div class="tg-text">عروسیه ولی بزا بگو درگیری بین نیرو های سپاه و اسراییل
🤣
🤣</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/11900" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐏ـٍٍٍٍٍٍٍٍؔؑؒـٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍٍِِِِِِِِِِِِِِِِِِِِِِِِؔؑؐد</strong></div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/11899" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رسانه‌های ایرانی: تبادل پیام‌های میان آمریکا و ایران از طریق پاکستان ادامه دارد. وزیر کشور پاکستان با ادامه مذاکرات روز جمعه در ایران خواهد ماند. عاصم منیر، فرمانده ارتش پاکستان در صورت دست‌یابی به «چارچوب توافق» به تهران سفر خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/11898" target="_blank">📅 01:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">النصر با کریستیانو رونالدو قهرمان لیگ عربستان شد.
@withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/11897" target="_blank">📅 01:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدای پدافند در تهران
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/11896" target="_blank">📅 01:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با شما : سلام همچنان صدای پدافند میاد اصفهان.
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11895" target="_blank">📅 01:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با شما : درود خسته نباشی برادر به نظرم درگیری هست بین بندرعباس و سیریک تو دریا داخل تنگه مدام صدای بمب میاد
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/11894" target="_blank">📅 01:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صدای انفجار یا پدافند شدید در قشم
@withyashar</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/11893" target="_blank">📅 01:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لیندزی گراهام: ترامپ تاکید کرده است بدون توانایی غنی‌سازی، مسیری برای دستیابی به سلاح هسته‌ای وجود ندارد و به دلیل سابقه «تقلب» جمهوری اسلامی، تهران نباید اجازه ادامه غنی‌سازی را داشته باشد.
این موضوع، همراه با هدف اعلام‌شده برای اطمینان از اینکه ایران نتواند از گروه‌های نیابتی تروریستی حمایت کند، از نظر من خطوط قرمز مذاکرات هستند و دلایل محکمی هم دارند.
زمان مشخص خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/11892" target="_blank">📅 01:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل به جنوب لبنان
منابع لبنانی از آغاز دور دیگر حملات جنوبی لبنان خبر دادند.
تا این لحظه شهرک‌های زوطر، کفرا و شوکین هدف این حملات قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11891" target="_blank">📅 01:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۸ سوخت رسان در آسمان منطقه !!!!
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/11890" target="_blank">📅 01:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11889">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11889" target="_blank">📅 01:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پدافند اصفهان فعال شده</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11888" target="_blank">📅 01:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">درود به اقا یاشار گل  داداش من با این حرفت که میگی پادشاهی خوبه چون مردم میترسن حساب میبرن مخالفم  چون بلاخره راه در رو برای دور زدن اون موضوع رو پیدا میکنن ولی اگه قبولش داشته باشن و بهش اعتماد داشته باشن بدون نیاز به ترسوندن دستور رو اجرا میکنن</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11887" target="_blank">📅 00:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKarvan Ghvami</strong></div>
<div class="tg-text">درود به اقا یاشار گل
داداش من با این حرفت که میگی پادشاهی خوبه چون مردم میترسن حساب میبرن مخالفم
چون بلاخره راه در رو برای دور زدن اون موضوع رو پیدا میکنن
ولی اگه قبولش داشته باشن و بهش اعتماد داشته باشن بدون نیاز به ترسوندن دستور رو اجرا میکنن</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11886" target="_blank">📅 00:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">@withyashar
eXtrime weekend</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11885" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehryar</strong></div>
<div class="tg-text">درود به شرفت مرد
حرف دلمونو زدی
❤️
🔥</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11883" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خیلی حال کردم با دایرکتها ، حال اتاق جنگ ندارم ولی اینجا ویس میدم  تحلیل رو</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11882" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خصوصیات پادشاه مورد قبول ایرانیان
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11881" target="_blank">📅 00:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ما یکی لازم داریم همه مثل سگ ازش بترسند ! و اول از همه مثل سنگاپور و چین باید فساد رو ریشه‌کن کنه و فتیله پیچ کنه، چون اگه نکنه، اولیگارکهای مافیایی شکل می‌گیرن دوباره!!!</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11880" target="_blank">📅 00:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرهنگ سازی این مملکت فقط یه رضا شاه کبیر میخواد ! حتی محمد رضاشاه هم کارش نیست ! جدی‌میگیم … دموکراسی رو فراموش کنید که در انتها بد تر از اخوندا میشه
😂
🙌🏾
مینویسم امضا میکنم من اینجا رو یه کلونی کوچیک تمام تست های روانپزشکی رو انجام دادم فقط دیکتاتوری ولی مدرن بدون محدود کردن تفریح و استعداد ها !</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11879" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11878" target="_blank">📅 23:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العربیه: پیش‌نویس نهایی توافق‌نامه ایالات متحده و ایران با میانجیگری پاکستان دست یافته است که قرار است ظرف چند ساعت آینده اعلام شود.  ۱. این پیش‌نویس شامل آتش‌بس فوری و جامع در تمامی جبهه‌ها است. ۲. طرفین متعهد می‌شوند به‌صورت متقابل از هدف قرار دادن زیرساخت‌ها…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11877" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11876" target="_blank">📅 23:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11875" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مخبر: هیچ‌وقت باور نکردم که حادثهٔ سقوط بالگرد شهید رئیسی یک اتفاق عادی باشد.
@withyashar
😃</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11874" target="_blank">📅 23:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک مقام کاخ سفید گفت : فردا کوین وارش به عنوان رئیس جدید فدرال رزرو سوگند یاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11873" target="_blank">📅 23:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca046287c.mp4?token=XwGm1qVRKrqyBCGsrZq5IP7PwDWmJOTUNEOFY5j84v2MuoyUUYEqMG3qQv_d9KmsvjYRtd4l2g9CsTHTg_2BrlUbPWdU7f507DOOWkfiDgnrS1o9kKgrGBgp8P4jbtj-FP0Q5-1zYx8FsMWvAqjMVdzGgetSk_PZUVG-9ktwyfPQVqSvOow2XXc63ImqPlMowujv6URz18b2xf9gqA0v-7eJbLmegSdHI0V8WdyHB5cDcdRnxlZoBOH7RiFxMH_lo2EHAhdmLZarj7Fz9FM6lY26TkEGKiN8KOVim8nkNq7a5z8Ymfzj5ktltkWfbPGXB0z5_r9ckMdSvrmuWfapnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca046287c.mp4?token=XwGm1qVRKrqyBCGsrZq5IP7PwDWmJOTUNEOFY5j84v2MuoyUUYEqMG3qQv_d9KmsvjYRtd4l2g9CsTHTg_2BrlUbPWdU7f507DOOWkfiDgnrS1o9kKgrGBgp8P4jbtj-FP0Q5-1zYx8FsMWvAqjMVdzGgetSk_PZUVG-9ktwyfPQVqSvOow2XXc63ImqPlMowujv6URz18b2xf9gqA0v-7eJbLmegSdHI0V8WdyHB5cDcdRnxlZoBOH7RiFxMH_lo2EHAhdmLZarj7Fz9FM6lY26TkEGKiN8KOVim8nkNq7a5z8Ymfzj5ktltkWfbPGXB0z5_r9ckMdSvrmuWfapnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم :
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11872" target="_blank">📅 23:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الحدث به نقل از یک منبع دیپلماتیک بلندپایه پاکستانی: فرمانده ارتش پاکستان امشب به تهران سفر نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11871" target="_blank">📅 22:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11870" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال‌استریت ژورنال: کویت بر اثر جنگ ایران منزوی شده؛ با بسته شدن تنگه هرمز، صادرات ۲ میلیون بشکه نفتی روزانه این کشور متوقف شده و واردات مایحتاج از مسیر زمینی عربستان، ۶ برابر هزینه حمل دریایی تمام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11869" target="_blank">📅 22:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
منبع ایرانی نزدیک به تیم مذاکره‌کننده:
اصرار آمریکا بر مذاکرات هسته‌ای باعث بن‌بست در گفتگوها شده است،
تهران تمایل کمی به ادامه مذاکرات نشان می‌دهد،
احتمال شروع درگیری در هر لحظه وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11868" target="_blank">📅 21:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏شاهزاده رضا پهلوی:
ما برای مطالبه آزادی‌مان عذرخواهی نمی‌کنیم. جهان باید بابت نادیده گرفتن مردم ایران از آنها عذرخواهی کند که ۴۷ سال با این رژیم مماشات کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11867" target="_blank">📅 21:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت امور خارجه آمریکا : ‏استیون میلر، معاون رئیس دفتر در امور سیاستگذاری کاخ سفید:
‏«ایران دو انتخاب پیش رو دارد: یا با سندی که مورد رضایت ایالات متحده باشد موافقت می‌کند، یا با مجازاتی از سوی ارتش ما روبه‌رو خواهد شد که مشابه آن در تاریخ معاصر دیده نشده است. این انتخابی است که پیش روی آنها قرار دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11866" target="_blank">📅 21:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علی کریمی : ‏اگر نتوانیم بگوييم اشتباه ،اشتباه است؛
‏يعنى به پايين‌ترين مرحله بردگى رسيديم!!!
‏فعلا يكسرى هاتون جولان بدهید  تا اينترنت مردم داخل ايران  وصل بشه!!
‏آنوقت مردم داخل ايران قضاوت  خواهند كرد
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11865" target="_blank">📅 21:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دولت فرانسه معتقد است بحران خاورمیانه طولانی‌تر از آنچه سایر کشورها تصور می‌کنند، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11864" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام اطلاعات سپاه به آمریکا: زمان به نفع شما نیست
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11863" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">العربیه: پیش‌نویس نهایی توافق‌نامه ایالات متحده و ایران با میانجیگری پاکستان دست یافته است که قرار است ظرف چند ساعت آینده اعلام شود.
۱. این پیش‌نویس شامل آتش‌بس فوری و جامع در تمامی جبهه‌ها است.
۲. طرفین متعهد می‌شوند به‌صورت متقابل از هدف قرار دادن زیرساخت‌ها خودداری کنند.
۳. آزادی کشتیرانی در خلیج فارس و تنگه هرمز تحت یک سازوکار نظارتی مشترک تضمین می‌شود.
۴. تحریم‌ها در برابر پایبندی ایران به مفاد توافق، به‌تدریج لغو خواهد شد.
۵. مذاکرات درباره مسائل معوقه حداکثر ظرف هفت روز آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11862" target="_blank">📅 21:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : آرامش قبل از طوفان
🌪️
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11861" target="_blank">📅 21:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e3625918.mp4?token=WXlM2K-KL15JPD96tgELT4z-0WlUJTyNGiiUpLqqFZXqg5ruwAMgaMNYej_dyHx6QUuNcxTKZ5-Ws-cFByFM5zeiMshGZ_89lvskThQBkAF3Hbk3nI6PtUr854GJUqFVGyHlBBBRCPswhC6u4a-VqqrfTYaLSdWS0BW28wSddp0NzLdpmqQjdK--JZ5pulCIyTnkpvkC3yZFtLq1oGDFgvZQluxxV1ll8DwUINxRFUwdZkmHsIulrB3nRJkQqRyyEc5WYcRZ7_zwwpTJ1s3-E1DQMycZKrX4_4ttyyHkwNf7PjWAXy64Pb-ZqzKTYrFEKNa0I4GA5Xj1NOy0ltZ_LCKuWfDe2thWwEIQ70DUvoRS4wunyM3kMwOdkjAx3xA_M943IJ6LY29oJ-2wNvprziZ9tbJJN-LbmCzrGKcfpp76DmIYABESxXmiR1gdCGLiPxM36UckD-S4LwynisbkrQlE-LxPtTtQlssGVTyyixbZ7CpuY2a9CD7wTPhybDkqdt5niaTdCgpFKBSU68FPk_ow5vGR7TSlHqBi1BJwDno2glD3hq-vVVNCMXldgWSsXyelKeyeYBd3eDmzXKUeYywZ8r6J18gBLvEVvMyJ2I5e_fw_CKxOA_4CVuHbQdQQdXjY5Dywf6G6rCpMZId34vphWYExDN2xY_qrigwtqX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e3625918.mp4?token=WXlM2K-KL15JPD96tgELT4z-0WlUJTyNGiiUpLqqFZXqg5ruwAMgaMNYej_dyHx6QUuNcxTKZ5-Ws-cFByFM5zeiMshGZ_89lvskThQBkAF3Hbk3nI6PtUr854GJUqFVGyHlBBBRCPswhC6u4a-VqqrfTYaLSdWS0BW28wSddp0NzLdpmqQjdK--JZ5pulCIyTnkpvkC3yZFtLq1oGDFgvZQluxxV1ll8DwUINxRFUwdZkmHsIulrB3nRJkQqRyyEc5WYcRZ7_zwwpTJ1s3-E1DQMycZKrX4_4ttyyHkwNf7PjWAXy64Pb-ZqzKTYrFEKNa0I4GA5Xj1NOy0ltZ_LCKuWfDe2thWwEIQ70DUvoRS4wunyM3kMwOdkjAx3xA_M943IJ6LY29oJ-2wNvprziZ9tbJJN-LbmCzrGKcfpp76DmIYABESxXmiR1gdCGLiPxM36UckD-S4LwynisbkrQlE-LxPtTtQlssGVTyyixbZ7CpuY2a9CD7wTPhybDkqdt5niaTdCgpFKBSU68FPk_ow5vGR7TSlHqBi1BJwDno2glD3hq-vVVNCMXldgWSsXyelKeyeYBd3eDmzXKUeYywZ8r6J18gBLvEVvMyJ2I5e_fw_CKxOA_4CVuHbQdQQdXjY5Dywf6G6rCpMZId34vphWYExDN2xY_qrigwtqX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس هایی از فیلم کمدی تهران۵۷ و باز سازی عکس معروف ترامپ در تهران…
😂
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11860" target="_blank">📅 20:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ : پس از پایان جنگ با ایران، قیمت بنزین در آمریکا به سطح ۱.۸۵ دلار سقوط خواهد کرد
«این وضعیت خیلی زود، خیلی زود تمام خواهد شد. و وقتی تمام شود، قیمت بنزین شما پایین‌تر از قبل خواهد آمد. می‌دانید، چند ماه پیش از آیووا رفتم و قیمت بنزین ۱.۸۵ دلار در هر گالن بود.»
«و ما دوباره به چنین ارقامی خواهیم رسید. اما به‌هرحال به شکلی بسیار بهتر به آن خواهیم رسید. ما به آن اعداد برمی‌گردیم و در عین حال کشوری خواهیم داشت که سلاح هسته‌ای نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11859" target="_blank">📅 20:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456925e365.mp4?token=YADQqcUYRU8SvBhgCbQIUG9oCK9-KAMfsfcavykcn4Yi0rAoXqfrmvQKrpqo8SKwgXDYrw2QTuuoaCseLvVQcvB2FNCBEw8lXFdF4AODx7Bj4pL9S2b-j6lIBX87DmZts8Jij91d6kMbWNaeiILIyN5GWKJeDlLy_KACrJG9-BAAaE1GkNh2R9R50qRuiwtjW5Tbwcf45FVCk05Dh4AHbzWAgE_5GLjv8Yusy12jiD0pVcZHqeQEtSGPB3vT5xah_P9n-4qt6_SpMbLPD9FtTUljTxWuivnEt8g-GiBKGY3TTKI-_grxcM1-Bn9f1zdwRRSbfFew7_yKbD4UDEKkmKyRgw_636_nlc9_qNSseNEjbmpHF6isEunL9hYlKJkPWC8_ZI-pqbY1i2gJh4g58KptePm_eST8yFRapx7cTJzqcY5qBkdwXew2hQyXPpcJHO9emHpwK-IY5pe7mVDETKr9cxAgwWhSvp8FbHlhAqYcktC5FtXaS4s39MDVvRkY498VnCTSRv1_lMgVkhTr_-uqajoiLlw2A27Ei9pqgnbP1q5_MBWzgeOuyPp-hRnu-bDwFoMyIcvzcsWWS5EMM1AtF0VgS4Bd--rwgqXSo4UH0yfQpo_PHZDc0jeZn8S8_hAvUB-PNT-9xa8pHOrK9y-WFz2w3pbGzHMHtg6W-Hk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456925e365.mp4?token=YADQqcUYRU8SvBhgCbQIUG9oCK9-KAMfsfcavykcn4Yi0rAoXqfrmvQKrpqo8SKwgXDYrw2QTuuoaCseLvVQcvB2FNCBEw8lXFdF4AODx7Bj4pL9S2b-j6lIBX87DmZts8Jij91d6kMbWNaeiILIyN5GWKJeDlLy_KACrJG9-BAAaE1GkNh2R9R50qRuiwtjW5Tbwcf45FVCk05Dh4AHbzWAgE_5GLjv8Yusy12jiD0pVcZHqeQEtSGPB3vT5xah_P9n-4qt6_SpMbLPD9FtTUljTxWuivnEt8g-GiBKGY3TTKI-_grxcM1-Bn9f1zdwRRSbfFew7_yKbD4UDEKkmKyRgw_636_nlc9_qNSseNEjbmpHF6isEunL9hYlKJkPWC8_ZI-pqbY1i2gJh4g58KptePm_eST8yFRapx7cTJzqcY5qBkdwXew2hQyXPpcJHO9emHpwK-IY5pe7mVDETKr9cxAgwWhSvp8FbHlhAqYcktC5FtXaS4s39MDVvRkY498VnCTSRv1_lMgVkhTr_-uqajoiLlw2A27Ei9pqgnbP1q5_MBWzgeOuyPp-hRnu-bDwFoMyIcvzcsWWS5EMM1AtF0VgS4Bd--rwgqXSo4UH0yfQpo_PHZDc0jeZn8S8_hAvUB-PNT-9xa8pHOrK9y-WFz2w3pbGzHMHtg6W-Hk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: «رگ حیاتی تهران»
ژنرال جک کین هشدار می‌دهد که یک توافق جدید ممکن است ایران را زخمی اما همچنان پابرجا باقی بگذارد و این تصور را در ذهن حکومت ایجاد کند که آمریکا را وادار به عقب‌نشینی کرده است.
او می‌گوید:
«مشکل من با این توافق این است که ما ایران را زخمی اما همچنان سرپا باقی می‌گذاریم، و آن‌ها از اینجا خارج می‌شوند و خودشان را قانع می‌کنند که آمریکا را مجبور به عقب‌نشینی کرده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11858" target="_blank">📅 20:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6961194543.mp4?token=OyJK0te5ZI-567uOsKWjtA-9eBuBcH0_BOLMmhViKRpz3F3V_3fKTG7oZolagNYM2QnF0u9kAqKj3o1ddd7eSkpWY2jtF83gMz6c3xonqnSKRWaBwApMc1PpPdnbU74IwQ0SBPUAw28wcDV1eSgIbTjOkTucPfcRrgo600hp9kcOkPxxFrpi8fEt0CoPB0BujriXteZxzbcLB3VO2WoIQAqrl7_hF9XB5wbluH-rE-3Cza2Wn_U9ZWHLenYSBD1P5szJRmO0MY52L-NoimYbM1UZpGQRAw8C3gdMp5CW_re6hq5-C7boHkEC6gERcXZnXCj8PUqGP7M_ioai5mFZgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6961194543.mp4?token=OyJK0te5ZI-567uOsKWjtA-9eBuBcH0_BOLMmhViKRpz3F3V_3fKTG7oZolagNYM2QnF0u9kAqKj3o1ddd7eSkpWY2jtF83gMz6c3xonqnSKRWaBwApMc1PpPdnbU74IwQ0SBPUAw28wcDV1eSgIbTjOkTucPfcRrgo600hp9kcOkPxxFrpi8fEt0CoPB0BujriXteZxzbcLB3VO2WoIQAqrl7_hF9XB5wbluH-rE-3Cza2Wn_U9ZWHLenYSBD1P5szJRmO0MY52L-NoimYbM1UZpGQRAw8C3gdMp5CW_re6hq5-C7boHkEC6gERcXZnXCj8PUqGP7M_ioai5mFZgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : تیم رئیس‌جمهور ترامپ شروط ایران برای دسترسی و کنترل تنگهٔ هرمز را رد کرده است.
خوب است! فقط شرایط «اول آمریکا» پذیرفته می‌شود.
«ایران نقشه‌ای منتشر کرده که آن را “منطقهٔ دریایی تحت کنترل” می‌نامد. تهران می‌گوید متعهد است تنگه را برای کشورهایی که با شروط آن موافقت کنند دوباره باز کند؛ شروطی که به‌احتمال زیاد شامل دریافت هزینه برای عبور از این تنگه خواهد بود.»
و واشنگتن، در واکنش به این موضوع، اعلام کرده که این اقدام کاملاً غیرقابل قبول است
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11857" target="_blank">📅 20:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار: آیا دارید کنترل سنا رو از دست می‌دهید؟
ترامپ: نمیدونم، واقعاً نمیدونم، من فقط کاری رو میکنم که درسته.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11856" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: ما در حال مذاکره با ایران هستیم
هدفمون رو هر طور شده محقق میکنیم.
ما فناوری پیشرفته پهپادی برای حمله به ایران داریم.
ایالات متحده اورانیوم ایران رو میگیره و احتمالاً اون رو نابود میکنه
ما عوارض‌گیری در تنگه هرمز را قبول نداریم
درگیری با ایران خیلی زود پایان خواهد یافت
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/11855" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a280dc1be8.mp4?token=T6rcbt0VazPc8IEij-FIfi9iY_cddsenhouZvodFDB2n97n3XLiyS8y21hQIQZ875Ne_8BKGtZpbRC67mYzDPjCa1KleBxo3dIwCjrPTpjxsKtMGCVUi9K_bLO_JpKV-ZxSTaPRwAsp6tTDa_wI3PkKpxtmauRIgGNGeJQWEusy1xLkI9ocdpiAraYO611pIcVIbczt7nhXGiwwimUXCCXvCkNf8Zceh16OajFlDsl3JckEQPddWGyuWmIUesiH3uM6eCYLjTHfpGxSGxBH9M3B7w37q6vgFdEBbn9ocw1gOujcrnGZCsm46G0OO59FeOWYLdIxPKyvzKMwdAFMQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a280dc1be8.mp4?token=T6rcbt0VazPc8IEij-FIfi9iY_cddsenhouZvodFDB2n97n3XLiyS8y21hQIQZ875Ne_8BKGtZpbRC67mYzDPjCa1KleBxo3dIwCjrPTpjxsKtMGCVUi9K_bLO_JpKV-ZxSTaPRwAsp6tTDa_wI3PkKpxtmauRIgGNGeJQWEusy1xLkI9ocdpiAraYO611pIcVIbczt7nhXGiwwimUXCCXvCkNf8Zceh16OajFlDsl3JckEQPddWGyuWmIUesiH3uM6eCYLjTHfpGxSGxBH9M3B7w37q6vgFdEBbn9ocw1gOujcrnGZCsm46G0OO59FeOWYLdIxPKyvzKMwdAFMQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران نمی‌تواند اورانیوم غنی‌شده با غنای بالا را نگه دارد. وقتی به آن برسیم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11854" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30025bd687.mp4?token=D7PTq9taCeyg1EurgC_hgYONcw4K3EcB8o0x-fyDVSoqKKkgw8qsfiHw4m0uFnj7MKVFFT3KMVakEY8nDl61CQvP0c1sSWIBKNbJaPujXWIODVRil-OsF5s6ei0o623dwogaxThO8RUiWckOFO9bnJCmvZmHnMNssHhUEpsRBVXCLYHmF_nLw95qdC-aw31FO-4mF3_NGH_b8r0NoxnxEhg2tuhsSAV--FK8uBXPUdkJ5uDcY7JRb-L3ucPEab0tH39DBbyLk6TH3XwMxXGdd9QvMGZvXajcBomMmduoeDRj1A8p_8T6jr1RFYdcyTyXUsy6A-90UVU5K-BYeYJs_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30025bd687.mp4?token=D7PTq9taCeyg1EurgC_hgYONcw4K3EcB8o0x-fyDVSoqKKkgw8qsfiHw4m0uFnj7MKVFFT3KMVakEY8nDl61CQvP0c1sSWIBKNbJaPujXWIODVRil-OsF5s6ei0o623dwogaxThO8RUiWckOFO9bnJCmvZmHnMNssHhUEpsRBVXCLYHmF_nLw95qdC-aw31FO-4mF3_NGH_b8r0NoxnxEhg2tuhsSAV--FK8uBXPUdkJ5uDcY7JRb-L3ucPEab0tH39DBbyLk6TH3XwMxXGdd9QvMGZvXajcBomMmduoeDRj1A8p_8T6jr1RFYdcyTyXUsy6A-90UVU5K-BYeYJs_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما کنترل کامل تنگه هرمز را در دست داریم.
@withyashar
ترامپ: مذاکرات با ایران ادامه دارد</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/11853" target="_blank">📅 19:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مارکو روبیو : اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن می‌کند.
«در مذاکرات مقداری پیشرفت داشته‌ایم، اما روشن است با سیستمی روبه‌رو هستیم که خود
تا حدی دچار شکاف است؛ یعنی ساختار حاکم در ایران.»
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11852" target="_blank">📅 19:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۴ اسرائیل : سپاه پاسداران در تلاش است زیرساخت دیجیتال تنگهٔ هرمز را به یک ابزار فشار و تسلیحاتی تبدیل کند و این موضوع فقط دربارهٔ پول نیست.
طرح پیشنهادیِ دریافت «عوارض عبور» از کابل‌های فیبر نوری زیردریایی می‌تواند شرکت‌های بزرگ فناوری آمریکا را مجبور کند از قوانین ایران تبعیت کنند؛ اقدامی که خطر ایجاد یک «شوک دوگانه» در نظام‌های جهانی انرژی و مالی را به همراه دارد.
این اقدام، هدفی را نشانه گرفته که شامل حدود ۱۰ تریلیون دلار تراکنش روزانه و ۹۹٪ از ترافیک اینترنتی است که از این منطقه عبور می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11851" target="_blank">📅 18:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر خارجه آمریکا: مقامات پاکستانی امروز به تهران سفر خواهند کرد؛ نشانه‌های مثبتی وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11850" target="_blank">📅 18:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سی‌ان‌ان: یک منبع گفت که در سطوح بالای دولت اسرائیل، تمایل شدیدی برای اقدام نظامی مجدد وجود دارد و کلافگی فزاینده‌ای از اینکه ترامپ همچنان به آنچه که آنها وقت‌کشی دیپلماتیک ایران می‌گویند اجازه می‌دهد، دیده میشود.
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11849" target="_blank">📅 18:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام : «تا تاریخ ۲۱ مه، نیروهای سنتکام (فرماندهی مرکزی آمریکا) ۹۴ فروند کشتی تجاری را تغییر مسیر داده و ۴ فروند را از کار انداخته‌اند، در حالی که در حال اجرای محاصره برای جلوگیری از جریان تجارت به داخل و خارج از بنادر ایران هستند.»
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11848" target="_blank">📅 18:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلومبرگ: ایران در حال مذاکره با عمان درباره نحوه ایجاد نوعی سیستم عوارض دائمی است که کنترل این کشور بر ترافیک دریایی از طریق تنگه هرمز رو رسمیت میده.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11847" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایلان ماسک :
انسان‌ها به زودی تراشه‌های سایبرنتیک کاشتنی خواهند داشت که قدرت‌های خداگونه را ممکن می‌سازند
این فناوری می‌تونه انسان کور رو بینا کنه ، افراد فلج دوباره بتونن راه برن و ناشنوا ها هم بتونن بشنوند.
ایلان این تراشه‌ها رو به عنوان «معجزاتی در سطح عیسی» توصیف میکنه
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11846" target="_blank">📅 17:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11845" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11844" target="_blank">📅 17:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شاهزاده رضا پهلوی: جمهوری اسلامی از روز اول ایران برایش مطرح نبود. رژیمی که به جای پرداختن به مشکلات اقتصادی ایران، میلیون‌ها دلار صرف حزب‌الله و حماس می‌کند. در بیروت بیمارستان برایشان می‌سازد. در حالی که مردم پشت در بیمارستان‌ها در ایران از بین می‌روند.
غیر ممکن است از چنین نظامی انتظار داشته باشید که از دید منافع ملی کشور به قضیه نگاه بکند. این رژیم از روز اول در جهت «مصلحت نظام» عمل کرده. نه به نفع منافع ملی
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11843" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1663101b52.mp4?token=djJFTjVVmFI-5DqfTmCNB-ep7pUtQCtjHRfd3psGSBCsfs3nCBksGIug9IJaGyNKud1Nld2bgghswI9KUVMG0SzNv__wi0hiQrocc8lzeeDsd6znjh5TqK0X5KhfyKK0Jwjl9F_OtE5KSGLdO_vD-6fi-dFmsECURLR_JHlY4_5oLVJUz_Q1URc-VSX_54A39joA9tKtN14rL6Vkw_PcI5WeCLu0-_4Qn2kObBYOkZZlF26Ygca4Cg-fw9qmrjCbq5cfAfe1MjwWEpTXP2hwSHLLWBkhnbQee8WVdoz52KNuyCfyyndBWEAbdNOl74udUuvGnyvoA8TxDkGEYWbIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1663101b52.mp4?token=djJFTjVVmFI-5DqfTmCNB-ep7pUtQCtjHRfd3psGSBCsfs3nCBksGIug9IJaGyNKud1Nld2bgghswI9KUVMG0SzNv__wi0hiQrocc8lzeeDsd6znjh5TqK0X5KhfyKK0Jwjl9F_OtE5KSGLdO_vD-6fi-dFmsECURLR_JHlY4_5oLVJUz_Q1URc-VSX_54A39joA9tKtN14rL6Vkw_PcI5WeCLu0-_4Qn2kObBYOkZZlF26Ygca4Cg-fw9qmrjCbq5cfAfe1MjwWEpTXP2hwSHLLWBkhnbQee8WVdoz52KNuyCfyyndBWEAbdNOl74udUuvGnyvoA8TxDkGEYWbIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترسناکترین سناریو جام جهانی
😂
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11842" target="_blank">📅 16:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رویترز:  رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند @withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11841" target="_blank">📅 16:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در تروث: مقاله نیویورک پست را انتشار داد با عنوان «چگونه تهران را در سه حرکت درهم بشکنیم»
۱-
ادامهٔ محاصره و جنگ اقتصادی
آمریکا باید با محاصرهٔ دریایی، تحریم و بستن راه‌های دور زدن تحریم‌ها، اقتصاد ایران را تحت فشار شدیدتر قرار دهد تا حکومت از نظر مالی ضعیف شود.
۲-
تقویت برتری انرژی آمریکا
با افزایش نفوذ انرژی آمریکا در جهان، هم اثر افزایش قیمت نفت کنترل می‌شود و هم نفوذ چین تضعیف خواهد شد.
۳-
کنترل تنگهٔ هرمز با قدرت نظامی
نویسنده پیشنهاد می‌دهد ارتش آمریکا با عملیات دریایی و هوایی مسیر تنگهٔ هرمز را تحت کنترل بگیرد و آزادی عبور کشتی‌ها را تضمین کند؛ اقدامی که به گفتهٔ او باید همراه با تهدید جدی ایران در صورت نقض آتش‌بس باشد
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11840" target="_blank">📅 16:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استوری علی کریمی : "اولين راه براى فهميدن ميزان هوش يك حاكم، نگاه كردن به آدم هايى ست كه اطراف او هستند."
"نيكولو ماكياولى"
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11839" target="_blank">📅 16:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار:
پیام شما به خانواده‌های آمریکایی که از گسترش هوش مصنوعی نگران هستن چیه؟ اونا می‌ترسن که بچه‌هاشون تو آینده نتونن شغلی داشته باشن...
ترامپ:
ایران نباید سلاح هسته‌ای داشته باشه.
😬
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11838" target="_blank">📅 16:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بر اساس تازه‌ترین نظرسنجی فاکس نیوز، ۶۵ درصد رأی‌دهندگان معتقدند آمریکا در جنگ با ایران در حال پیروزی است.
این در حالی است که وزارت خارجهٔ ایران در حال بررسی آخرین پیشنهاد صلح آمریکا است و هم‌زمان میانجی‌های پاکستانی برای پیشبرد توافق به تهران سفر کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11837" target="_blank">📅 16:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرنگار فاکس‌نیوز در تل‌آویو: ترامپ و نتانیاهو، در یک تماس تلفنی حساس، درباره گام‌های بعدی در خاورمیانه گفتگو کردند.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11836" target="_blank">📅 16:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع اسرائیلی به رویترز:
ترامپ به اسرائیل قول داد که اورانیوم غنی‌شده از ایران خارج شود و هر توافق احتمالی شامل این بند خواهد بود
!
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11835" target="_blank">📅 15:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یزدی خواه: اینترنت جهانی فعلاً بازگشایی نمی‌شود/ دسترسی ویژه برای گروه‌های موردنیاز برقرار است
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11834" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11833" target="_blank">📅 14:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز:  رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11832" target="_blank">📅 14:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای اندیشکده آمریکایی: طبق ارزیابی کارشناسان، وحیدی و اعضای حلقه نزدیک او کنترل نه‌تنها پاسخ نظامی ایران در این درگیری، بلکه سیاست‌های مذاکراتی تهران را نیز در دست گرفته‌اند.
@withyashar
من دو هفته پیش در این ویدیو به این مسئله اشاره کردم
https://www.instagram.com/reel/DYIY6lnxd_R/?igsh=bjlqYWRvcDZ5NHIz</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11831" target="_blank">📅 14:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر کشور پاکستان با احمد وحیدی، فرمانده سپاه پاسداران در تهران دیدار کرد. @withyashar یکی اینو آخرش از سولاخ کشید بیرون دیگه مابقی با موساده
😅</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11830" target="_blank">📅 14:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تایمز اسرائیل:  ایران در جریان آتش‌بس از فرصت برای جابه‌جایی لانچرهای موشکی و آماده‌سازی برای دور جدید درگیری استفاده کرده
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/11829" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">روسیه: ایران به تنهایی باید در مورد سرنوشت ذخایر اورانیوم خود تصمیم بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11828" target="_blank">📅 13:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش های تایید نشده از ۳ انفجار در بندر عباس و قشم
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11827" target="_blank">📅 13:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همکنون زلزله در بندر عباس
@withyashar
مرحله بعدی زامبی و گودزیلا است</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11826" target="_blank">📅 13:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏علی قلهکی : آمریکایی‌ها پس از دریافت نظراتِ ایران، پیشنهاد کرده‌اند که «پایانِ جنگ در تمامیِ جبهه‌ها»، «رفع محاصره تنگه هرمز توسط آمریکا»، «بازشدن تنگه هرمز توسط ایران با تعرفه و مسیر دریایی مدنظر ایران»، «آزادسازی ۲۵٪ از اموال بلوکه شده ایران _حدود ۲۵ میلیارد دلار»، «معافیتِ فروشِ نفت ایران به مدت ۳۰روز» و فازِ اصلیِ مذاکره یعنی «خروجِ ۴۰۰ کیلو اورانیوم از ایران _در بهترین حالت ارسال به کشور ثالث_» و «قبولِ حقِ غنی‌سازی ۳.۶۷ ٪ برای ایران (بعید است در فاز نهایی آمریکا آن را بپذیرد)» و «تعطیلی مراکز هسته‌ای _منهای راکتورِ تهران صرفا با کاربرد پزشکی) به طور یکجا توسط ایران امضا شود!
‏ایران می‌گوید تمام فازهای پیشنهادی آمریکا  برای راستی‌آزمایی به مدت ۳۰ روز انجام شود تا هم ایران نفت خود را بفروشد و هم‌مُجاب شود در بحث هسته‌ای مذاکره را انجام دهد!
‏پی‌نوشت: ۱. اختلاف جدی بَر سَرِ مباحث هسته‌ای است؛ «۴۰۰ کیلو اورانیوم» خط قرمزِ دیکته‌ای اسرائیل برای آمریکاست! ایران ۴۰۰کیلو اورانیوم را نمی‌دهد، غنی‌سازی را هم حتما می‌خواهد و ۲۰ سال آن را تعلیق نمی‌کند. ایران با ارسال ۴۰۰ کیلو اورانیوم به کشور ثالث _چین و روسیه_ موافقت نکرده، آمریکا هم همینطور و خودش آن را می‌خواهد. نقطه‌ی جدی شکستِ توافق اینجاست. ایران مذاکره بر سر «پرونده‌ی هسته‌ای» را جُدای از «پرونده بازگشایی تنگه هرمز» و «اتمامِ جنگ» می‌داند!
‏۲. ایران و آمریکا سر فاز بندی توافق اختلاف دارند؛ ایران یکجا توافق نمی‌کند و آمریکا دنبالِ توافق یکجاست!
‏۳. آمریکا متعهد به متون و محورهای ارسالی نیست؛ محورهای ذکر شده با اینکه فاصله جدی با شروط ایران دارد ولی همین‌ها هم توسط آمریکا به مرحله اجرا در نمی‌آید!
‏۴. آمریکا تحریمی را لغو نمی‌کند؛ شاید تعلیقِ مدت‌دار در بهترین حالت، قسمتِ ایران در توافق شود.
‏۵. بر فرض توافق با آمریکا، هیچ تضمینی برای جلوگیری از ترور سطح بالا توسط اسرائیل نیست!
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11825" target="_blank">📅 13:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f70e8f6f5.mp4?token=kf3-QPd5Ebxl4zuPhRUJc189GWayaxOSBlzbnFltd1AzLKMEGaaFMXOrlHCBUXpzIjuIMF81f9QCcI5jRwaevs_ZIbrj9oC3bW663FZeIPv9Zz9WTV5YEJnkqo_tU55b4hvD3GefMQdUj6j-dpX05JaPNhTU0XwEfNdmA0OVQ8yFGo0JREuCmtLKomrOXlZgukQ9qUpPPrMF50upAnnESB2UAD7UL16I_DdmPjSZv3JrfETWB6MvAvIPGbixgCqgiMEzzW39TsUD6F5N9UFrvQ_DxmhNeg-evcpLzaMo1hcK1fEdL425lXSctEm2A5WsJz69JLlEmZtIyOyv-jWkSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f70e8f6f5.mp4?token=kf3-QPd5Ebxl4zuPhRUJc189GWayaxOSBlzbnFltd1AzLKMEGaaFMXOrlHCBUXpzIjuIMF81f9QCcI5jRwaevs_ZIbrj9oC3bW663FZeIPv9Zz9WTV5YEJnkqo_tU55b4hvD3GefMQdUj6j-dpX05JaPNhTU0XwEfNdmA0OVQ8yFGo0JREuCmtLKomrOXlZgukQ9qUpPPrMF50upAnnESB2UAD7UL16I_DdmPjSZv3JrfETWB6MvAvIPGbixgCqgiMEzzW39TsUD6F5N9UFrvQ_DxmhNeg-evcpLzaMo1hcK1fEdL425lXSctEm2A5WsJz69JLlEmZtIyOyv-jWkSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای تیم ملی فوتبال ایران برای درخواست ویزا به سفارت آمریکا در آنکارا مراجعه کردند
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11824" target="_blank">📅 12:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الجزیره به نقل از یک منبع پاکستانی:
مقامات ایرانی از پاکستان خواسته‌اند تا مهلتی برای ارزیابی و بررسی معیارهای آمریکایی برای مذاکره دریافت کند.
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
ژنرال منیر هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11823" target="_blank">📅 12:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGMGBn9BmtZ00nRkZP-19JO4UvmclDX0yqMVk4ERTEw7Q1gslUZE1MAPMR84hl1HzSRbWbwYgNiMnWIGSzCVxMLwouVVLR2Ps2Je6nSuRmK_gBOnjQ159SVm4cUgu7yIZzZQpjlCY_RDjZJworQrR6ATWYEB82ab6u8AKZFnPBBgYODBFS2RmflFXdephVKkqIBa8WiCSFOVp8iCpXC587irbVtB3Y91JbFX8IpEigQQ9SKqRrc6KACl8pMy0mHuJ_4wFTnRKOBVvY_RA211mPhbflvXnkEgiQ7FSOBbm_ObWYL6axG52YBgpLodgU7HRQB3iqzgPNmGUi5jMcgTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما :
تا عید غدیر مجسمه‌ای ۱۵ متری از مشت علی خامنه‌ای در میدان انقلاب تهران نصب میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11822" target="_blank">📅 12:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فاکس نیوز در گزارشی به نقل از عمر محمد، کارشناس مبارزه با تروریسم، نوشت سبک زندگی مجتبی خامنه‌ای به سطحی از ناپدید شدن رسیده که اسامه بن لادن سال‌ها در ایبت‌آباد تجربه می‌کرد؛ زندگی بدون ارتباط مخابراتی و با اتکا به پیک‌های مورد اعتماد.
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11821" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۲۰ ملوان ایرانی به کشور بازگشتند
سفیر ایران در پاکستان از بازگشت ۲۰ ملوان ایرانی که به‌دلیل توقیف کشتی‌شان در آب‌های سنگاپور گرفتار شده بودند، به ایران خبر داد.
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل و ساعاتی پیش به میهن بازگشتند.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11820" target="_blank">📅 12:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ایران در حال پاسخ به متن ارسال شده از سوی آمریکا است
ایران در حال گفت و گو‌ بر سر چارچوب کلان، برخی جزییات و اقدامات اعتمادساز به عنوان تضمین است.
متن ارسالی به میزانی شکاف‌ها را کم کرده است
اما کمتر شدن شکاف‌ها نیازمند پایان یافتن وسوسه جنگ در سمت واشنگتن است.
ورود ژنرال عاصم منیر به تهران، به منظور کم کردن این شکاف‌ها و رسیدن به لحظه اعلام رسمی پذیرش یادداشت تفاهم است.
/ ایسنا
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11819" target="_blank">📅 12:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش CNN: حکومت ایران در طول آتش‌بس بخشی از تولید پهپادهای خود را از سر گرفته است، که نشان می‌دهد در حال سریعاً بازسازی برخی توانایی‌های نظامی است که در حملات آسیب دیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11817" target="_blank">📅 11:58 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
