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
<img src="https://cdn4.telesco.pe/file/hWV4OsRIDT73jXn9pV8uRHeN8fLNdlSkujKgBDV0kOz2afg5Fxp3CtQPZnUXMxGEcuQJrSw38TRZ3bkEQRFoXLxLz612hU-bqRnDgzm1-UomoYl3Q_Dys6EwBF1sRErRPpjWj7XPEpioTiXu33ei1aiZTRd7EsH0QmGdOF81O65GTJ9ajWGLunFobda_rcYqAS7YVpEJ_tHCYEPgUA-4iRh4tKARKn6RIgombdQksn-Sgv88CpxdG9FBm4VUtTGdQOcJJJcbWOO9YW-z7efg5_7X-6P1rc7wcDH8orqAmOFwE_f_zw0494aPrGksT_znazmziS_-CEOgaFR2tquHPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 276K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-12720">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/12720" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12719">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/withyashar/12719" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12718">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSG</strong></div>
<div class="tg-text">ماجرا ری اکشن پر قرمز چیه دیگه ؟؟همه دارن میزنن
😂</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/withyashar/12718" target="_blank">📅 21:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12717">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1s8mjW1WX-4Dc8OrLnxRJNAloAo3Plk88AN6raRLSKDk30rWliCl8hTTr3bUwo-rJGgS-m20MyiJ7TPu9tish135FPP4a0-ecf-j23IWfz7APGN4tOwzqz7U2VU3rO6rDsYK2PfHJvrgBHghncb33XFnYVag1jkwoyVg3RBVqfmfQ1_yI7HW7mME1FN0eocPpTudztHQPRm5zr5ITjXan8MqQseWjumqCf3pUslYsJbRIv0LOd9rvGXrwMmDySxsZq7Ux70be8pKA3xN5ttJDMjT_17x6mrkV-_Eei7oxWrdF5z079pnpBx22BemjBZNNWkQz_RmP6KNgLBUTX-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی رد لغو تحریم‌های ایران از سوی دونالد ترامپ، بازار سهام ایالات متحده در عرض تنها ۲۰ دقیقه، ۲۳۰ میلیارد دلار از ارزش خود را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/12717" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12716">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/12716" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12715">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار : هیچوقت انقدر مشتاق نبودم حجاج هر چه سریعتر سلامت برگردن خونه هاشون
😅</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/12715" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/12714" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">داداش دقیقاً داره حرف تو پیش میره موج مکزیکی
😂</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/withyashar/12713" target="_blank">📅 20:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: دارن کم‌کم شروع می‌کنن چیزهایی رو که باید بهمون بدن، تحویل بدن. اگه این کار رو بکنن، خیلی خوبه.
اگه نکنن، هگست کارشون رو تموم می‌کنه.
ما درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول صحبت نمی‌کنیم.
وقتی اونا درست رفتار کنن و کار درستو بکنن بهشون جازه می‌دیم به پولشون برسن
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/12712" target="_blank">📅 20:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار: آیا با این موضوع راحت خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ: نه(زیر دلم درد میگیره)
@withyashar
🤣</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/withyashar/12711" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ :
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/withyashar/12710" target="_blank">📅 20:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12709">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/12709" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhesam | امیرحسام</strong></div>
<div class="tg-text">داداشی امشب ردبول و میزنی یا نه؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/withyashar/12708" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12707">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیت هگست درباره ایران:
آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند.
آنها آمدند و التماس کردند تا صحبت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/withyashar/12707" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12706">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHQy9giUvB_vxmaGBvnO0IIR0XWPQdKsvu7w-qyQLrZYB3VOaYkPlNiVVGE7UsWDBle8I2mS6y9kmAh1RTuvDzm6zZsFmFkrJuuDa1HUYVnez44JI9h5sMTwiQ8cF1-WiuoU_LvTzOgwYNBRG26oseEDUr4W6ZL-WXrXz0tg8mjY2NhNkUWxeLYWFkm_qd_WOjwkPXIhoZedScuVK21_dA9d5rG2WXFsKvstgRNkmwBjj6tXbdOS9wHIomFNkBZSm2Y-tc90maGVpk_ndAedudkb7WJ9x7CQSAPaA90qySunFmkYiwDN2feGlwLn-1GRz7y9vVSpJmg9b40d5ligvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️رئیس روس اتم می‌گوید روسیه تصمیم  گرفته است بازگشت کارکنان خود به نیروگاه هسته‌ای بوشهر در ایران را به تعویق بیندازد!
@withyashar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/withyashar/12706" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12705">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مارکو روبیو :اگر ایران توافق قابل قبولی مارو امضا نکند جنگ را شروع خواهیم کرد این‌خواسته ترامپ است
@withyashar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/withyashar/12705" target="_blank">📅 20:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12704">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
@withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/12704" target="_blank">📅 20:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12703">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره مذاکرات ایران:
آقای رئیس‌جمهور، اگر این کار جواب نداد، گزینه‌های دیگری در اختیار دارید.
@withyashar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/12703" target="_blank">📅 20:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12702">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روبیو : ما با جمهوری اسلامی پیشرفت‌هایی داشتیم اما در روزهای آینده میزان اون رو خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/12702" target="_blank">📅 20:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12701">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/12701" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12700">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KXbXfIkSbl0lpkIZmVAAlj9pMzwvL4K5_KtyUs7uKw-3t8RtelJRUsc7ppLsQ9hiaZohiZF_T-p8PfYI7iM79loDJXFNmcN_A3WN13GNcAiQ4NAl573SnEd2WGtBIohY6Bh7rzkQNZfZjkGUbIrFX22dYfeEKiCyGJ3SDmjubQxzfflKeit45i98dzuH6GpKK2OAQXsYEGMPqDf1nawA-muaXIT8iQkt_ndOieTLKbYu3rysaLDMUeww3pQqqpR9XzhQbWT-sYM0EFmgqmJsL_fWBak4jRs__zOeUagwwAPH1BtXNSLDfk5Y9gz0qsklOGHVd1ngbFrcePgqP1aBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06481c5d63.mp4?token=KXbXfIkSbl0lpkIZmVAAlj9pMzwvL4K5_KtyUs7uKw-3t8RtelJRUsc7ppLsQ9hiaZohiZF_T-p8PfYI7iM79loDJXFNmcN_A3WN13GNcAiQ4NAl573SnEd2WGtBIohY6Bh7rzkQNZfZjkGUbIrFX22dYfeEKiCyGJ3SDmjubQxzfflKeit45i98dzuH6GpKK2OAQXsYEGMPqDf1nawA-muaXIT8iQkt_ndOieTLKbYu3rysaLDMUeww3pQqqpR9XzhQbWT-sYM0EFmgqmJsL_fWBak4jRs__zOeUagwwAPH1BtXNSLDfk5Y9gz0qsklOGHVd1ngbFrcePgqP1aBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران :
ایران خیلی دنبال توافقه. هنوز به نتیجه نرسیدیم و راضی نیستیم، ولی یا توافق میشه یا مجبور میشیم کار رو تموم کنیم.
اونا دارن از روی استیصال مذاکره می‌کنن.
اونا دیگه نیروی دریایی و هوایی ندارن و رهبرانشونم هم رفتن.
ایران فکر می‌کرد میتونه صبر کنه تا منو خسته کنه
به انتخابات میان دوره اهمیتی نمیدهم اونا گزینه دیگه ایی جز توافق ندارن
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/12700" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12699">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینترنشنال باز خل شده ؟ چرا ترامپ رو انقدر میکوبه ؟!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/12699" target="_blank">📅 19:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12698">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم @withyashar</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/12698" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12697">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx66A-tzAe8khLKKDri2XmqGGe46mwT1grZvLGqo_dHgIMkvohWNwB4fmWJ4DVZ9Z51pOaVnmeVEKY-5Ay1Yfp2k-Dxd9rKDIIIY5d_YwBQ9NanQS56XgMdPbw4u20d0DwAssdVogKVyp6P7cNa91JesWoTq52cN_E0K9MmEYxrkfyorbLIYuzOUjVlPzHJ-YRBMKjk5QSV92XO0CDqZLjfvHJf4rU14OyQyWP0WeQ-YSc-l_9OFEqigJdHJdO8xv0rc88MnjrecvyvHD3_JcLIrft-qeniJKRzsvYchZVpfedJcw35a0Bllvpi2joFVM_39yRKQGfnAVOFotEX4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایرانی‌ها فکر می‌کنند من به‌خاطر انتخابات میان‌دوره‌ای جنگ را تمام می‌کنم اما من اهمیتی نمی‌دهم
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/12697" target="_blank">📅 19:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12696">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q71IlAWWn07iSBQjVcjdBTRidHSV1nQ4OM2NA63fjsc_0WNRLRseRTyBZSI55zbkjq6X-ylTpbjcBHh8DlxN_BZTIq9Bx5ImtB6XvVVcxhfWN0cQudn1xSGZImOWGVeRdG0-htsgXsSnHFyUVD4EiNHvqgpY7qFZN9IC4ALRtw4wwqSNL12u88P2N5wYeeHL9GmKPiDwoVVDTz912e6ijO3OdPZbraJn6dDsK_IZ0RqxM1dq8Xbp1P7kJPGMYU8l8DtRU40zcw_PT_AYx9vfITmLesrzmdd_9k-PifIl8T9Itn961VCiOm_elZrMBD9YfP3fy4jhf8h9sqVJfD7ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها می‌باشد.
میزان اختلالات در شبکه از دیروز بسیار بیشتر شده است، بسیاری از سرویس‌های گوگل و کلودفلر بسته شده اند و حتی قابلیت استفاده از گوگل پلی و اپ استور نیز وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12696" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12695">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">یاشار جان من دندونپزشکم، دو سال سرباز بودم، صبح‌ها تو کلینیک ارتش یه شهرستان دورافتاده کار می‌کردم، بعدظهر هم تا شب تو کلینیک خیریه کار می‌کردم، از نظر مالی هیچ سودی برام نداشت فقط دلم می‌خواست دوران سربازی یه کار مفیدی هم برا اقشار ضعیف انجام بدم واقعاً از دلو جون مایه میذاشتم
اما اون دو سال، از آدمای قدرنشناس  و پر توقع رفتارای زیادی دیدم که باعث شد بفهمم خیلی از هم‌وطنا وقتی برا خدمتت هزینه‌ای پرداخت نمی‌کنن قدر خودت و کارتو نمی‌دونن انگار وظیفت بوده بشون خدمت کنی
همین تجربه‌ باعث شد دیگه سمت خیریه نرم
خیلی از مردم ما واقعا قدرنشناسن
وقت و انرژیتو بدون سود و فقط از روی عشق به کشورت صرف کاری می‌کنی بعد یه عده‌ پیدا میشن که  برن رو مخت و پشیمونت کنن</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/12695" target="_blank">📅 19:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12694">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB40eFNTVf-ufV3AUcZYz7CL_RRooEJAEn-pCwHL-ew3CDrsaMJ4c5EmEp7k0cowueagiaf_mvUSR6KgUYI1mdtRfjuK-xElR2GIIalijkES6GgdzDymqxp6Y98Q2WIn0441kCJWHUnbRDvTxVIIfqbMagZ30l3ekYE2rbFnCSk3WZjxVtJvjrE6b24laQq1gVzZmRowG8ZHpI-rkjirA4ybBhTlsgcdTfJhvrDzN-BLwepGGS4J2nayYC_wSCi5zCqGDcaR0kxk4qCW9qEXIIbqYEVmkNxnngKokAsKksXptodiq3QRLJRkZmJb7OD0oFHIesD8kPiBYV5Q5fM8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به PBS گفت که ایران در ازای کنار گذاشتن اورانیوم بسیار غنی‌ شده خود، از تحریم‌ها معاف نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12694" target="_blank">📅 19:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12693">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlXs3XZW84RWdxe5SN1NBmIzWthl-9T2OlDeBOnD6nslak-6nQxhDGUfSLhDcnVKwnfUhHC_WE_nNNGZhYk8hAQ1w_boloVdgNzIp0zj1fmD78Cdo200iqpf4TM9l1mEWyyz1jGGgexyr4mPrHkYFr4QNL-CGuYKIq7uuHmBslquZFi_6MllkAyOK1QBp_3Mdyy82bD5SX6J4mCe9WFwe6yDwN6oSTuUhuQdxF8SpS4CXkVJ3kUZcIJkAhQ_Rx-P3OaYhCDkMXnwDNuuAloxnuDBuLgXT7QzQLjrb_1CjjWq0XAwHctOqoRiVmPVjwDjyBzhbDJ0uIvXnrwuEqFAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار برج چیتگر پامچال چهار از طبقه ۸ به بالا آتیش گرفته
این دقیقاً روبروی همون برجیه که تو جنگ دوازده روزه طبقه ۱۵ رو زدن بعد گفتن نشت گاز
@withyashar</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/withyashar/12693" target="_blank">📅 19:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری فارس: به عقیده ما احتمال دارد ترامپ در ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است
@withyashar
یاشار : عقایدتون رو …
🤣</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/12692" target="_blank">📅 19:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzqXjBDSTZ13RDLbhgilXULI7EEbj4ey_oBdYNuvL_1ASaosXcG0X-Nu_i8_ht7DoLFVga4ursM8n0IMz42n_EQAPFMy9nlSJeaHvSbTUXkYoGPUPN71VlLqFdQtU704G09HAbP0nuSqP0YhV37jzDoqs58_CcSzHvUbIs84qXjueKVikCzIB3BTXqtIb3uU31UFatt5sJE1-Lc2K-mLphAtydCFwN7OZE1I4XClyMtrviFgL8lV4sUDJCm3hk8P810-JtlN-245DdZIm5J9TYgm-KZERYfDgSRX0WRsJU12urFEnLIcoX3m2_fjrcBIVaSCVAFz4HoDuxMP1W97Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
عوامل موساد باعث بازگشایی اینترنت شدن.
@withyashar
یاشار : شاید باورتون نشه ولی درست میگه اینبار
🤣</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/12691" target="_blank">📅 18:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR8l6koMScmFUHEFLVlDAxQNTe5H0QV3lfpiENU5w2ZgTcOY-_tMw-uwMiYRmCNFUpKwxEtNYsr_wz2aSnDaJGCGRiztnNQPK0WCU7FUxvgFzFaztcJ1S5-MzIdLyg_9heDlOUZUpfrftujqVv8pILCZo7I_JXrlLNqYLHf950iC1uUviIT_Z-j0Dw6uyVgroXMbJ68dXfEZSTGtV8eYNmSMJglUrmSSDx_vrdX0SOmINmBJORbTDmFiitZD65Q82hUFEBc4Igok5Ykx0pC1QGhQq-3EUkCp1DdtW9iTbK4Z133G6po_FYY7zfmuzDIXlDCJNHQVIIGxB2qxXBAWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از پایگاه هوایی رامشتاین در آلمان، ده‌ها فروند هواپیمای ترابری C-17A و C-5M نیروی هوایی ایالات متحده، چندین فروند هواپیمای ترابری C-130 و حداقل 10 فروند تانکر KC-135R را نشان می‌دهد که در آنجا مستقر شده‌اند.
در اتاق جنگ گفتم که رامشتاین مهم‌ترین پایگاه ایالات متحده در اروپا برای جنگ ایران است و به عنوان یک قطب لجستیکی کلیدی عمل می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12690" target="_blank">📅 18:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پست جدید یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/12689" target="_blank">📅 18:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کاخ سفید گزارش‌های مربوط به تفاهم‌نامه ایران را کاملاً ساختگی خواند.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/12688" target="_blank">📅 18:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پست جدید
یه یا موسی کامنت کنین بی بی و پسرش و زنش رو تگ کنین امشب بزنه
🤣
💥
💥
🌶️
🌶️
https://www.instagram.com/reel/DY2Hk4hoW2r/?igsh=MXYyMDlxdjY5b3QwZg==</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/12687" target="_blank">📅 18:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل در اقدامی فوری دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراففش رو صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/12686" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زلنسکی در پیامی به ترامپ:
اوکراین برای رهگیری موشک‌های بالستیک روسیه تقریباً به طور انحصاری به ایالات متحده متکی است.
سرعت فعلی تحویل موشک‌ها به اوکراین دیگر با تحولات هماهنگ نیست.
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/12685" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر دفاع ترکیه
یاشار گولر
:
ترکیه حقوقش در دریای اژه، مدیترانه شرقی و قبرس بر اساس قانون و تاریخ است و با هر اقدامی که بخواهد وضعیت موجود را به نفع برخی کشورها تغییر دهد یا جزایر غیرنظامی را نظامی کند مخالف است.
همچنین هشدار می‌دهد که نسبت به تهدید علیه منافع و امنیتش در دریاها بی‌تفاوت نخواهد بود و ارتش ترکیه توان مقابله با هر تهدیدی را دارد.
در مورد قبرس هم تأکید می‌کند که از ترک‌های قبرس حمایت می‌کند و به‌عنوان کشور ضامن از حقوق و امنیت آن‌ها دفاع خواهد کرد.
@withyashar
ترکیه با یونان و قبرس بر سر , مرزهای دریایی , منابع گاز طبیعی در مدیترانه شرقی و حق حفاری در آب‌های مورد مناقشه اختلاف جدی دارد.</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/12684" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به گزارش فارس نیوز، آواربرداری، تعمیرات و بازسازی تمام واحدهای پتروشیمی آسیب‌دیده تنها در ۵۰ روز به پایان رسیده است و اکنون تمام تأسیسات قادر به تولید با ظرفیت قبل از جنگ هستند.
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/12683" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مهر:
یک ساختمان اداری در فرودگاه امام خمینی آتش گرفت
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی دچار حریق شده است.
این حریق در یک ساختمان اداری گمرک شهر فرودگاهی به وقوع پیوسته است.
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12682" target="_blank">📅 17:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/12681" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین</strong></div>
<div class="tg-text">واقعا این ملت باید به دیکتاتور وطن پرست بالا سرشون باشه . ملتی که جمهوری اسلامی پرورش داده جز دزدی بی فکری پاچه خوار تو اوج بیسوادی ولی ادعای دانشمند بودن میکنن آدم فروشی ...... اینا با دموکراسی درست نمیشن فقط باید یه دیکتاتور بالا سرشون باشه مثل رضا خان بزرگ . این جماعت تو هر لحظه رنگ عوض میکنن در این حد احمق حالا یه عده میگن توهین میکنی با کلمه احمق ولی توهین نیس واقعیته یه واقعیت تلخ . حکومت هر کشوری طبق لیاقت مردمش اداره و اجرا میشه واقعا متاسفم پاسوز یه عده جوگیر احمق شدیم</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/12680" target="_blank">📅 16:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12679" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad Farahmand 🐾</strong></div>
<div class="tg-text">درووود بهت یاشار عزیز،همین که توی حاشیه اصلا حرکت نمیکنی یعنی کارت درسته.فقط(( هدف ))مهمه تمام.</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12678" target="_blank">📅 16:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لیندسی گراهام:«مدت‌هاست برایم روشن شده که پاکستان به‌عنوان یک میانجی، فراتر از حدِ مشکل‌ساز است. دشمنی آن‌ها با اسرائیل، ریشه‌دار و دیرینه است.
این حقیقت را نمی‌توان انکار کرد که هواپیماهای نظامی ایران در پایگاه‌های هوایی پاکستان نگهداری می‌شوند؛ و همچنین مواضع و سخنان گذشتهٔ بلندپایه‌ترین مقام‌های پاکستانی علیه اسرائیل نیز نگران‌کننده است.»
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/12677" target="_blank">📅 16:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/12676" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOzGP5ig1KTQzc0EsI-q0MFUmeyAfDhkC765UgB4vfjI2Qob0n8IBOwJI5qeQur7Bb20xrN6A2SGLWPGJJ-obCikzEp7sSFU0cBgg0xkjPiTcLqDuJmNoMTee822JwCGbTqH9TEQGn1Edv5x2En0TfQtnpgmF7UWa7eMAXQ-j_Qew1jB_WJs2mRctqYfI2xhjaHQkHAVmnEr3EGMCzkZtZRzNMXi8TiFV5j1GiqN6CJN8x-aQv7JsEXc2tREMiVenCqFoA3x1iGQUr7KMkjHSlWkOSfXgLlCkMADJKL7tP0qJV1XEVBdt_RZSyC6fw3EZ3aOuIhyXoF4Zl8yb12FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث از جروزالم پست :
آزار و اذیت جنسی در زندان‌های ایران در دوران آتش‌بس به‌شدت افزایش یافته است
جروزالم پست
آزار و اذیت جنسی در زندان‌های ایران در دوره آتش‌بس به‌طور چشمگیری افزایش پیدا کرده است.
یکی از معترضان به مدیا لاین گفته که هنگام بازجویی با باتوم به او تجاوز شده است.
مرد دیگری پس از آن‌که مأموران ادعا کردند به پیکر همسرش بی‌حرمتی کرده‌اند، اقدام به خودکشی کرده است.
گروه‌های حقوق بشری می‌گویند از زمان شروع جنگ، دست‌کم ۳۶۴۶ ایرانی بازداشت شده‌اند و قطع اینترنت باعث شده ابعاد واقعی ماجرا پنهان بماند.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/12675" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK3jSkJh9OEscCnLLYD2cz1g-cXafNbwtlO6CCmNLmuxS7e6TRAllvXBVWEd3Tm9WnX6AEUC_v0i3Nj-lWUJmtpFEW6M3DjFFrnIstHeAOiab_qWx7X9HCUzGI679Vy68iHRmLuvLlT4B2sPaXExjmxgOIzbsSxKc_YJ7MA4BzZlUAcW_Ntm2uQvniJ7niBqtF2yUEvImK6N7g7xbwC3-CakQM9znX6f4exmqYrm1DDngQ-Ju8j6XeyPRGBrCskURrtSNg3iKvmq5RBMQliFwV6ld0M0oVitjAlNhZWyTMpl9YK6LnCzvnNqzdKqi1_uQxS2rdRiRuSATUywQ7oebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای سوخت‌رسانی جدید نیروی هوایی اسرائیل، KC-46A Pegasus "Gideon" (301)، اندکی پیش در اسرائیل فرود آمد و ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در مراسم استقبال حضور داشت. این هواپیما اولین فروند از شش فروند سفارش داده شده است و امکان سفارش دو فروند دیگر نیز وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/12674" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8b7f9a5a.mp4?token=Exj7AVmap0mmdB_KbTQRycieL8DXNgKJkVBjluEmTqcRJnNKqP0CjsbUXkgjKnsv5-YYqQZmmLZh_4rtEPOtADDQLNgSNHXY1z1NvNZD1DT3O9gENoCwFGD2nfCCTUoCJH2QpK82wW9pX-qhyucjeFjC6hvnJiucVYfaY6YQcWuSgOyTgYlWEkLgb41nqde3AKX9SN-ulw7wvnlJxbetQC8vIZpYGcnCmPh07CNutdb9S5QFfbSnAKGTCRqVG8brIEqihpbaOBU4j2kL_HboGvK4hn1x07Va-N3i_CT-7XQVPAidliuIP1GeR_FcACGw1k1Lf35i1JmD_nTjzIsHow8UVdcbPw0O1sXJ-bMCeDMN_jgI2Ntn_lPlnhS5CzLA7J4ftW1b2_yI_ZUic_nMjjiMB8VrU-VYkkKTFANQ3N465UCOPlCLXt3EJlUrVechFLxQ_dXCiFTFV14WboeV4m9_kXDFTrdSRybdX5dlfjWVGvOfWlEOY0gE3mml62G7YiXHV6XNsW0ZZ0owZetxcO2C17CipKJd-aNaah_kXvSn1Ew9H9THC_aK9LmK5e9axnl7dAK2Qdyaft1RRmKDP23ncUnJZCipQEzDu9BxbJ7tfmwcIPHt4fN94eDVgIT6VkOSonOb_fgBXMJe6Sd_9ttec7S0jhyeSXZuJOzo1uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8b7f9a5a.mp4?token=Exj7AVmap0mmdB_KbTQRycieL8DXNgKJkVBjluEmTqcRJnNKqP0CjsbUXkgjKnsv5-YYqQZmmLZh_4rtEPOtADDQLNgSNHXY1z1NvNZD1DT3O9gENoCwFGD2nfCCTUoCJH2QpK82wW9pX-qhyucjeFjC6hvnJiucVYfaY6YQcWuSgOyTgYlWEkLgb41nqde3AKX9SN-ulw7wvnlJxbetQC8vIZpYGcnCmPh07CNutdb9S5QFfbSnAKGTCRqVG8brIEqihpbaOBU4j2kL_HboGvK4hn1x07Va-N3i_CT-7XQVPAidliuIP1GeR_FcACGw1k1Lf35i1JmD_nTjzIsHow8UVdcbPw0O1sXJ-bMCeDMN_jgI2Ntn_lPlnhS5CzLA7J4ftW1b2_yI_ZUic_nMjjiMB8VrU-VYkkKTFANQ3N465UCOPlCLXt3EJlUrVechFLxQ_dXCiFTFV14WboeV4m9_kXDFTrdSRybdX5dlfjWVGvOfWlEOY0gE3mml62G7YiXHV6XNsW0ZZ0owZetxcO2C17CipKJd-aNaah_kXvSn1Ew9H9THC_aK9LmK5e9axnl7dAK2Qdyaft1RRmKDP23ncUnJZCipQEzDu9BxbJ7tfmwcIPHt4fN94eDVgIT6VkOSonOb_fgBXMJe6Sd_9ttec7S0jhyeSXZuJOzo1uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیمان بستم و شب و روز بیدارم
👑
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/12673" target="_blank">📅 15:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/12672" target="_blank">📅 15:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12669">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c0f02fec.mp4?token=eJ-qUtz3NKHuCtCVKcBge5oneNjpFF8JRQIq1R257G9ZArSaX4yv8OWOVEHUk2psgF4TOp7XW7ipLam-2DYMKeFUXXsntFv2HUYAti-KsoIbKTkayTMQP3SgnnyYU28ehhJjI9zhW6h9euvZ1RF63wLWMCuEDHIl8p4hr5ZbwZUzX4_0J2G888_iXtWrIKufQCen7bv55pwgmsrpsikg2vP-GeVjXr2gx2nRdzq1Ap1aIyxMmNCiiigEyhIxq2S9M-BGmERzZm-0q4Gl2sD4bcU58In7sW4CJI3GlgJpxUqiZXWPI_wP6jGGgHAkZwMbhzF8WgZpOfQEVmSQAXC8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c0f02fec.mp4?token=eJ-qUtz3NKHuCtCVKcBge5oneNjpFF8JRQIq1R257G9ZArSaX4yv8OWOVEHUk2psgF4TOp7XW7ipLam-2DYMKeFUXXsntFv2HUYAti-KsoIbKTkayTMQP3SgnnyYU28ehhJjI9zhW6h9euvZ1RF63wLWMCuEDHIl8p4hr5ZbwZUzX4_0J2G888_iXtWrIKufQCen7bv55pwgmsrpsikg2vP-GeVjXr2gx2nRdzq1Ap1aIyxMmNCiiigEyhIxq2S9M-BGmERzZm-0q4Gl2sD4bcU58In7sW4CJI3GlgJpxUqiZXWPI_wP6jGGgHAkZwMbhzF8WgZpOfQEVmSQAXC8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت داخلی اسرائیل:
توافق ترامپ و ایران یک توافق بد است که می‌تواند به اسرائیل آسیب برساند. ما اجازه نخواهیم داد این اتفاق بیفتد!
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/12669" target="_blank">📅 14:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12668">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه 12 اسرائیل:ناوگان هوایی آمریکا ظرف 72 ساعت به پایگاه‌های خود در اروپا منتقل خواهد شد و در صورت از سرگیری درگیری با ایران، هواپیماها در حالت آماده‌باش برای بازگشت به فرودگاه بن گوریون قرار خواهند گرفت
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/12668" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12667">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید! حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/12667" target="_blank">📅 14:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12666">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بگو یادتون رفته پزشکیان همونی بود که ۳ ماه پیش جز شورایی بود که دستور کشتن ۵۰ هزار تا از بچه هامون رو داد واسه یه اینترنت شد ادم خوبه کاش وصل نمیشد همون
😡
😡
😔
😔</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/12666" target="_blank">📅 14:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12665">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommet</strong></div>
<div class="tg-text">بگو یادتون رفته پزشکیان همونی بود که ۳ ماه پیش جز شورایی بود که دستور کشتن ۵۰ هزار تا از بچه هامون رو داد واسه یه اینترنت شد ادم خوبه کاش وصل نمیشد همون
😡
😡
😔
😔</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12665" target="_blank">📅 14:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12664">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حالا بدیش اینه که این کند ذهن این مدت نت هم داشته و پیگیر کانال هم بوده و همش پیغام میداده زر زر
😡
اخطار هم داده بودم و گفته بودم دیگه دایرکت نده کلا ، دیشب گفتم بعضی ها میخوان مغذشوت پلمپ باشه ! مگه یه معجزه اتفاق بیوفته
🪄</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/12664" target="_blank">📅 14:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12663">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">واقعا فک نمیکنی تو شرایط فعلی درست نیست فعلا پزشکتان خراب کنی ؟ این همه ادم دیوث هست تو اینا یکی ک داره جلو سپاه وایمیسه رو چت نزن روش</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/12663" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12662">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">واقعا فک نمیکنی تو شرایط فعلی درست نیست فعلا پزشکتان خراب کنی ؟ این همه ادم دیوث هست تو اینا یکی ک داره جلو سپاه وایمیسه رو چت نزن روش</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/12662" target="_blank">📅 14:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a0b3327.mp4?token=C7dTtL2-FhoIrk6fuShatApsj0W2hsse39WOThXXdvPjzFQR5FnCg0xgkIdPUxcB-ZZkO9tOMoWYj4P677acfHMm6FBEFsP-XaMm5llVb65LruwIZZqLfSqk4KWfQUSvY8M92Xue1ZvuqwrEOk_J2Ezn1gzTfeBrgVZ4RQqB0CW33PxxjxzIT_WKjnwNpTmLE3tRzwHEZ-MmRfTMKHG3r8DayatlDpJNlNQaEXYnxLj-biHkynVxmrt6T5C-quFczV6ZHWRSY2rumdh5m5mi6DO0ZJZsJimEKpfx97PUhkS-HhrqQNN6QYqTVWpF_mfkYiMLFAkmG5ZhZGrN54845w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a0b3327.mp4?token=C7dTtL2-FhoIrk6fuShatApsj0W2hsse39WOThXXdvPjzFQR5FnCg0xgkIdPUxcB-ZZkO9tOMoWYj4P677acfHMm6FBEFsP-XaMm5llVb65LruwIZZqLfSqk4KWfQUSvY8M92Xue1ZvuqwrEOk_J2Ezn1gzTfeBrgVZ4RQqB0CW33PxxjxzIT_WKjnwNpTmLE3tRzwHEZ-MmRfTMKHG3r8DayatlDpJNlNQaEXYnxLj-biHkynVxmrt6T5C-quFczV6ZHWRSY2rumdh5m5mi6DO0ZJZsJimEKpfx97PUhkS-HhrqQNN6QYqTVWpF_mfkYiMLFAkmG5ZhZGrN54845w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو شورای اطلاع رسانی دولت :
چرا رسانه‌های ضدحکومت دچار سردرگمی و بی‌برنامگی شدند؟
@withyashar
یاشار: چرتو پرتاشو کات کردم ولی اگه ویس های دیشبم رو گوش‌کرده باشید این قسمت حرفش درسته ! ما باید تغییر‌تاکتیکی‌بدیم یا منتظر همون معجزه باشیم که منم گفتم !!! ادب ازکه آموختی از بی ادبان !</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/12661" target="_blank">📅 13:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رسانه I24 NEWS: نیروهای دفاعی اسرائیل (IDF) و فرماندهی مرکزی ارتش آمریکا (سنتکام) در حالت آماده‌باش بالا باقی مانده‌اند، در شرایطی که احتمال شکست مذاکرات میان واشنگتن و تهران و صدور دستور اقدام نظامی از سوی رئیس‌جمهور دونالد ترامپ وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/12660" target="_blank">📅 13:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الان نزدیک مجتمع صنایع فولاد مبارکه @withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/12659" target="_blank">📅 13:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/12658" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fc7b1751.mp4?token=opxEDO92-y1aFfCf_Mp8Q5qWG-G3dww4U94n1JtqhZxIDR7MgvGy8o_n1k3Dv9ykij4LSnFq2ZbFTR9bf6gjWfB881i1BUgb7BvfaU8e0JJb2gV225MPZNyphIKyxvirkymoeu_2mLBrFQ-2kVj5WpRqWNB71hkMQARUYMi5lWYNhRKsJypr9jrYYamR-y2XtjgaYI7EZuXYuHbNeYMiyGPe1ADMz6_WmkLdygIJ03uTxpozxPp1IgnZGoThlceEUUEIncoMX0Dn7fDJk-tHLtJCcY4eA_HM1bz7PXLEv-DIyFBWLHqwix4ZBSmc_5BEbDuyk18qE2FSq0R_bizm2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fc7b1751.mp4?token=opxEDO92-y1aFfCf_Mp8Q5qWG-G3dww4U94n1JtqhZxIDR7MgvGy8o_n1k3Dv9ykij4LSnFq2ZbFTR9bf6gjWfB881i1BUgb7BvfaU8e0JJb2gV225MPZNyphIKyxvirkymoeu_2mLBrFQ-2kVj5WpRqWNB71hkMQARUYMi5lWYNhRKsJypr9jrYYamR-y2XtjgaYI7EZuXYuHbNeYMiyGPe1ADMz6_WmkLdygIJ03uTxpozxPp1IgnZGoThlceEUUEIncoMX0Dn7fDJk-tHLtJCcY4eA_HM1bz7PXLEv-DIyFBWLHqwix4ZBSmc_5BEbDuyk18qE2FSq0R_bizm2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان نزدیک مجتمع صنایع فولاد مبارکه
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12657" target="_blank">📅 13:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/12656" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079db554c9.mp4?token=WZroYBPdoHLgD96XWnQr49dWVXt5tXoPgDG0IfRal36FEUMlXH0GgTjT91KJWHT0d-DeO5iYJJwD7fCz8PJvo2zMwOBUqQw-AKkzs7D2WGrXEUq4b5RWs60H1Ag6-aL7UAglCFdrm--EEvF8MrYK1nFzmkHbgP5uSVrxB87RLgFWtXLest9obnAwMhGYZnJfRv4gGvddOZ04M8i5AOjgbQlpdqNjp8KjRztU2NODaLQh7EiOqbMdVIn23U01Y5YQR_zeTgM13dHZYn9aTZai6--8tAOFKAnDNvukK7RkpaYywZwwCc-MraOoDVHaq7aA7kCrvNicqB7lQ6SEQGWuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079db554c9.mp4?token=WZroYBPdoHLgD96XWnQr49dWVXt5tXoPgDG0IfRal36FEUMlXH0GgTjT91KJWHT0d-DeO5iYJJwD7fCz8PJvo2zMwOBUqQw-AKkzs7D2WGrXEUq4b5RWs60H1Ag6-aL7UAglCFdrm--EEvF8MrYK1nFzmkHbgP5uSVrxB87RLgFWtXLest9obnAwMhGYZnJfRv4gGvddOZ04M8i5AOjgbQlpdqNjp8KjRztU2NODaLQh7EiOqbMdVIn23U01Y5YQR_zeTgM13dHZYn9aTZai6--8tAOFKAnDNvukK7RkpaYywZwwCc-MraOoDVHaq7aA7kCrvNicqB7lQ6SEQGWuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
مخصوص‌ پیرمردا</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12655" target="_blank">📅 13:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/12654" target="_blank">📅 13:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12653" target="_blank">📅 13:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Fatehi</strong></div>
<div class="tg-text">یاشار جان
اینترنشنالیا دارن میتوپن به ترامپ که بزدله و به ج ا باج داره میده و عقب نشینی کرده
تقریبا رسانه ها شدن این.
ولی من هنوز یادمه که میگفتی ترامپ فوتبالی بازی میکنه که توپشو نمیشه دید
هنوز این جملات و حرفاتو یادمه
بگو، خواهش میکنم بگو، که این رسانه ها همه دارن اشتباه می‌کنن و هنوز  ما اتاق جنگی های قدیمی دارین درست میریم به سمت قاهره.
مرسی ازت
❤️
#دیکتاتور_مهربون
❤️</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/12652" target="_blank">📅 13:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال‌استریت‌ژورنال: دولت ترامپ در حال کاهش نیروهاییه که در صورت بحران به اروپا اعزام میشن؛ اقدامی تازه در راستای کاهش حمایت نظامی آمریکا از متحدان ناتو.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/12651" target="_blank">📅 12:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEflaeAjNzU1T6V9_89u3GqlwCrqNSLSvNc96MarnSY3Pz1gfexcC4LbUVJF1pHZLc5rm0OBH5x-n__lN4NkhM7bqdpj8fguvx4nQlwwUATt8UZ459euOT9FvJZpyD8kHrqQ2zDtBpDEXyvDMfgksn7hDDJ4hLF_VXEhmcFydF_SNLpB5bM0i7RnIbF3_wzPOv-gh9L8sScRQ_V2OCQgPAmLiFXavExI7Qwe8rPvih9MOc-9k8fopIo2-p2_zNh-jUZGTSL3zg6hYz4sugWx6fWQHHqVggFo4xJ9VGS80V5ZuhfEDfVXEirWdssuHHq9rvN4Hj5bxZXKEJwK-WxyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان ، تهران شوش @withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/12650" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزارت اطلاعات ایران: دشمن برای دامن زدن به اختلافات ملی و فرقه‌ای و انجام عملیات تروریستی در کشور تلاش خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/12649" target="_blank">📅 12:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">باقری:
ذخایر اورانیوم غنی‌شده ایران در دستورکار مذاکرات نیست
ریانووستی به نقل از معاون دبیر شورای عالی امنیت ملی ایران:
ایران و ایالات متحده هنوز در مورد
رفع انسداد تنگه هرمز
به توافق
نرسیده‌اند
.
ایران و عمان
در حال مذاکره درباره
رویه جدید عبور کشتی‌ها از تنگه هرمز
هستند.
تماس‌های
غیرمستقیم
میان ایران و آمریکا ادامه دارد.
ذخایر اورانیوم غنی‌شده
ایران در دستور کار مذاکرات
نیست
.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/12648" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-NrdQAKZvpl4e34BymmFsoYywbgNN1qpgLTppS1YRypVgjqXDY0Yl1WqqB5wFLdfB-y_JQt2I-q0_wXwuK0ExjiswO6wiJ2dLTM3Er7ANUMnI-s35iWn7Q2V3la9OWfPPgu33Qb55tG3rjSdDLJgr687wjCpYsIuqUp_SzOk1Fd6F-3x-uxldgKzcXJU3yBfvj6WLwwFnijeofUkb_Vad_Gu4KCfOWtXT_hOaLbtGpgzAhtXtzMmyz-WKMo8tV6FGgPGuxfe8QcwU7UIc9qSoSw-GeWZlWfhVZNxRTxJ5t5Vw7yU66Fedr1YablO0dyi72PKIYnKc5_GiZPdChVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان ، تهران شوش
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12647" target="_blank">📅 12:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : تو نهاد امنیتی، هلاکت محمد عودة تأیید شد @withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12646" target="_blank">📅 12:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درود یا منظورت حمله اس یا که اب و هوایه سطح کشور مثل تهران اصفهان هوا خوبه یه بررسی بکن ممنون ازت</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12644" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙒𝙕</strong></div>
<div class="tg-text">درود یا منظورت حمله اس یا که اب و هوایه سطح کشور مثل تهران اصفهان هوا خوبه یه بررسی بکن ممنون ازت</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12643" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12642" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار : کمربند ها رو ببندید
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/12641" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارزیابی‌های اطلاعاتی حاکی از آن است که برنامه حمله به ایران از دستور کار خارج شده است
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12640" target="_blank">📅 12:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شبکه NBC News به نقل از معاون رئیس‌جمهور آمریکا ، ونس: «من خوش‌بین هستم که ایران در هر توافقی، با عدم توسعه سلاح‌های هسته‌ای موافقت خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12639" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6wSpJY_a-wZOp3HEPHRGLPMo-ise9HHw_eefOeCXDco3RzaOAEe2XWuKLAfzTMA3umF90N0IJFsqfIpWbchIv2NQfY4fOn2Fe5q_uaXibAysS8UGsGngWWEEFhAwrnUT2h-yfyoXXVGb-flAFQ7d5H45Re6-A-b-T95d1d2320afSI-SyL43DwyQSzbOxBWZ6D19YXBnvwAMjh11SH2UvXhO26e3mUu76TDFALIYjKGMiXSPp9WVuCVyAd7A66RvK-URcqaUbpXPAVDTU1oplr86ruBEQuRTSmNcJxlC3JNMlLeyy_ShIGNNZi0lzPKC0u_lzA3Zd3dzRVZ0m3pmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد +۱۰۰کا ویو یک پست رو زدیم اونم در ۱۱ ساعت !!!
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/12638" target="_blank">📅 12:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLteKfr-IU3ixL42VVyIqhrMe_xXYpLlqhehoT_EHQcpNAvo0-fust8CazDMXv_vcx5dZvkqCLypXtFGiz-W1GpkaiI57MzQZqlIuhQODm5RIomsqrxEzEzkR8NtumS_x0a_KscpN-qzgmSKNrxncpwKbEpZYbW3I3cwiEVWHbq8znh61WBBNldQ8ZP7D6KTHzdFEDFTWclvWweJUrYrKzsyojw0HT4y9GrmV_vpidtwTesKA4MCEaHcA1x4r3oOfT8QL043cPltuy-RUl-oo1CHo0LV9FMwYJkmo5_52DQEL1pAwK8EJHHMndYilRbp3M6yvzlwPKZRdKc6tJ4zxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کاخ سفید، : مامویت سادست؛ صلح از طریق قدرت
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12637" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : پروژه قهرمان سازی زرشکیان رو متوقف کنید !!!
😡
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12636" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گروه تروریستی سپاه پاسداران:
احتمال وقوع جنگ کم است، اما نیروهای ما آماده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/12635" target="_blank">📅 11:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12634" target="_blank">📅 11:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗠𝗶𝗻𝗮</strong></div>
<div class="tg-text">یاشار برای ماهایی که تازه وصل شدیم اکانت اینستا تو میدی</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/12633" target="_blank">📅 11:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در حال برسی اینم که امروز‌ خودمو نشون بدم و با یه ویدیو بیام به یوتیوب !
⏳
https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12632" target="_blank">📅 11:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسرائیل هیوم: پالس‌هایی از احتمال حمله آمریکا به گوش میرسد
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12631" target="_blank">📅 11:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید!
حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !
یاشار : دقیقا مشخص نیست چه کسی بوده است. صحبت ها درمورد تولسی گابارد و ونس هست ، ونس و تولسی از نظر فکری به هم نزدیک دیده می‌شوند؛ هر دو در جناحی قرار می‌گیرند که نسبت به جنگ مستقیم با ایران محتاط‌ترند.
بعد از استعفای جنجالی تولسی، چند روز پیش موجی از تحلیل‌ها راه افتاد که می‌گفت «ونس در حال منزوی شدن در دولت است».
اگه ونس باشه اوضاع خیلی پیچیده میشه
از اونجایی که تنها عضو کابینه هست که رئیس جمهور قدرت عزلش رو نداره و با رأی بالا اومده
تحلیلگران معتقدند درون دولت ترامپ اکنون دو بلوک شکل گرفته:
بلوک hawkish (تندتر علیه ایران)
بلوک restraint/non-intervention (محتاط‌تر)
و چون ونس چهره مهم جناح دوم محسوب می‌شود، هر اتفاق امنیتی فوراً او را وارد شایعات می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/12630" target="_blank">📅 11:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">روزنامه «فایننشال تایمز» گزارش داد صندوق مالی شورای صلح در غزه از زمان تاسیس خود تاکنون هیچ بودجه‌ای دریافت نکرده است.
@withyashar
این همون شورایی است که ترامپ تمام سران رو جمع کرد که پول بزارن</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/12629" target="_blank">📅 10:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مجلس سوئد ازدواج فامیلی رو ممنوع کرد؛
طبق این مصوبه، از اول ژوئیه 2026 دیگه ازدواج بین بچه‌های "عمو، دایی، عمه و خاله" تو سوئد ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/12628" target="_blank">📅 10:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a45d6ab.mp4?token=dGnSTEMxy7w6kRhW_ozKvF7rmmDVcX_qcln9nCWVZHHLxFOMjYENZF0haQCCBT5VPRZ6tR5YqlGqLK_hkPkTP9Ymu9m32XWen1k6H7BUzQHOZmCxPQRy8npKfM6G4Z7Jmt2l2lpWzBMMjAC3ZyokP-E0f__lyvoxDb2cu9wpjFwo-5YNAAF3rBGIU5T0cHd25DbPll2AawOLW41RQwE6kdQ9vENoarY8BUhPaAHvEYD0T5aNlgqD75x-yVChQSyJMRjeY4_0VBO_qGGyEQG_XtfgnCvgi4iKHSPKmH0FJJGWAFdHuI-PbifWVmVs8fnm62rzrRiOXbvOSVef-rJbfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a45d6ab.mp4?token=dGnSTEMxy7w6kRhW_ozKvF7rmmDVcX_qcln9nCWVZHHLxFOMjYENZF0haQCCBT5VPRZ6tR5YqlGqLK_hkPkTP9Ymu9m32XWen1k6H7BUzQHOZmCxPQRy8npKfM6G4Z7Jmt2l2lpWzBMMjAC3ZyokP-E0f__lyvoxDb2cu9wpjFwo-5YNAAF3rBGIU5T0cHd25DbPll2AawOLW41RQwE6kdQ9vENoarY8BUhPaAHvEYD0T5aNlgqD75x-yVChQSyJMRjeY4_0VBO_qGGyEQG_XtfgnCvgi4iKHSPKmH0FJJGWAFdHuI-PbifWVmVs8fnm62rzrRiOXbvOSVef-rJbfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان:ان‌شاءالله این ظالم به نام نتانیاهو، درسی که شایسته‌اش است را از مسلمانان جهان خواهد گرفت
@withyashar
یاشار : به قول تحلیلگر ترک، ترکیه هیچوقت مثل ایران نمیشه، بلکه بدتر از ایران میشه.</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/12627" target="_blank">📅 10:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارسالی : اینکه شب عید قربان نت وصل کردن، حس گوسفندی رو دارم که قبل ذبح بهش آب میدن.
😂
🤣
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12626" target="_blank">📅 10:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">زنگنه، نماینده مجلس
:
آمریکا حق غنی‌سازی، حاکمیت ایران بر تنگه هرمز و رفع تحریم‌ها را پذیرفت
@withyashar
🤣</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/12625" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گویا موشلی رو جمعه در تهران و شنبه در مشهد تشیع میکنند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/12624" target="_blank">📅 03:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/12623" target="_blank">📅 03:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12622" target="_blank">📅 02:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12621" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/12620" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/12619" target="_blank">📅 01:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/12618" target="_blank">📅 01:52 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
