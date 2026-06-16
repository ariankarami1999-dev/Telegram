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
<img src="https://cdn4.telesco.pe/file/USLCfCqYskCIF0SMud0ZToiq01ZvpGn6N52cTUldo3xByn2iKXOFd1a78P2ncF2tZJYCgB1_tIjLmytkKhPJExaKTw2sfzgBiUIwrEYjioPirLwDmdIXxCV8ndtHGHCbJNz1ez1uhdJaPRomvb_xrSzLUWwcnejQvnpLNoBoPeWLxVY6P5tDctnzsxKl9T5wmdTnZiezxVwgGc3uWVOTFl3Kdfb7FgmfRYLnhfU_h272UnvOTqUbVOE5VHMKU9D5Byb6ttiwePi-zLcy1SB4VhZU43lNbg5V2uIKs8oXMWiMokxGWxQV_aW5pzloPFr7N4uD1Hu-ofKQk-oQPFj0yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری مهر : شنیده شدن صدای سه انفجار در قشم</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/17616" target="_blank">📅 01:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
ایران باید تأمین مالی سازمان‌ های تروریستی خشونت‌ آمیز و عوامل بی‌ثبات کننده در منطقه را متوقف کند! نمی‌توان با اطمینان ۱۰۰٪ گفت که ایران به تمام تعهدات خود پایبند خواهد ماند.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/17615" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تسنیم :
رفع محاصره دریایی عملیاتی شد</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/17614" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/17613" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4237e85c2.mp4?token=Ez35u3Rncr8abvOo7L6oFuDfkzeUJUqLf7DippxlsMZU3ubHA0WlpZwa6km4Of0Fu2fd2CagHLC2mgR-ZrTZuwzwG70QMT0nIOtRkZNfE-N3eGOTHDHpwZCImRi93dhHBHVu9LbXbquXwiUBJtA8IPrRuo-3kOPHOwiEX2YqiRf8vvqAfxuCKImKdZYIZ-J2iKOiwYTFoy3xis6HBZqPIoNWpUeU_zUKZb4rUNpyZqHmg9t_OUMpfwNI80jRol9f2gga3pegEGzq-iK0Ad0pPKrig02qKCulDN_NPuSqJABxjVzSQ0NQWydVAIec23uHcPiWmngrDaXCXn4hsvCFFiSTVMED1pIZD5aqNROwbRVG0qegr_ojRRdgkKWlwbg1uZMhGjMz0uMQk9l89S-SUhb2mUXGfRycA-aOTXXMi3BH7kLM8hfVRCcqtu9IGb8SmqHvokR932iljkVSkc47I2x2-Bi8ZKyNZs_yXvfK6cxTr7oNRbq-hqDurwxNeBwTxIPdvvktQtjaXwOlAMgd9Q8RMFfbbDWNgzSlMCh14M5G5pw09k2cqV57UOdol0uJEIC975KYDE7-2_MkR3C6Keve9sGcjkdegJa9R9OqDn3JrZhJu8P_wzuwiPURy0rnr4S_IU9waRy9wp2iiscjclfEc5nM-AFbAZD5MZ-YLT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4237e85c2.mp4?token=Ez35u3Rncr8abvOo7L6oFuDfkzeUJUqLf7DippxlsMZU3ubHA0WlpZwa6km4Of0Fu2fd2CagHLC2mgR-ZrTZuwzwG70QMT0nIOtRkZNfE-N3eGOTHDHpwZCImRi93dhHBHVu9LbXbquXwiUBJtA8IPrRuo-3kOPHOwiEX2YqiRf8vvqAfxuCKImKdZYIZ-J2iKOiwYTFoy3xis6HBZqPIoNWpUeU_zUKZb4rUNpyZqHmg9t_OUMpfwNI80jRol9f2gga3pegEGzq-iK0Ad0pPKrig02qKCulDN_NPuSqJABxjVzSQ0NQWydVAIec23uHcPiWmngrDaXCXn4hsvCFFiSTVMED1pIZD5aqNROwbRVG0qegr_ojRRdgkKWlwbg1uZMhGjMz0uMQk9l89S-SUhb2mUXGfRycA-aOTXXMi3BH7kLM8hfVRCcqtu9IGb8SmqHvokR932iljkVSkc47I2x2-Bi8ZKyNZs_yXvfK6cxTr7oNRbq-hqDurwxNeBwTxIPdvvktQtjaXwOlAMgd9Q8RMFfbbDWNgzSlMCh14M5G5pw09k2cqV57UOdol0uJEIC975KYDE7-2_MkR3C6Keve9sGcjkdegJa9R9OqDn3JrZhJu8P_wzuwiPURy0rnr4S_IU9waRy9wp2iiscjclfEc5nM-AFbAZD5MZ-YLT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسیب دیدن خبرنگار Press TV هنگام حمله پهپادی اسرائیل در لبنان</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/17612" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرمانده نیروی قدس سپاه پاسداران: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و در صورت لزوم، برگ‌های دیگری نیز بازی خواهد شد. - صدا و سیما.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/17611" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآذری‌ها |Azariha</strong></div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است
یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.
ایتان لاسری بر این باور است که اسراییل و ترکیه وارد مرحله‌ای از رقابت استراتژیک فزاینده شده‌اند که ممکن است ویژگی‌های خاورمیانه را در سال‌های آینده شکل دهد. وی اشاره کرد که تنش بین دو طرف به بالاترین سطح خود در دهه‌های اخیر رسیده است، اما هنوز از سطح رویارویی نظامی مستقیم فاصله دارد.
کارشناس اسرائیلی ایتان لاسری به ۸ کانون تنش بین اسرائیل و ترکیه اشاره کرده و معتقد است رقابت استراتژیک آن‌ها ممکن است ویژگی‌های منطقه را تعیین کند. مسائلی مانند غزه، سوریه، لبنان، انرژی در مدیترانه، ناوگان‌های رفع محاصره غزه، تقویت ساختارهای دفاعی ترکیه، و نقش آمریکا در تعادل منطقه از جمله این کانون‌ها هستند. لاسری همچنین احتمال جنگ سرد بین دو کشور را در سال‌های آینده بیشتر از جنگ نظامی می‌داند
https://telegra.ph/%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3-%D8%A7%D8%B3%D8%B1%D8%A7%DB%8C%DB%8C%D9%84%DB%8C-%D8%AA%D8%B4%D8%B1%DB%8C%D8%AD-%DA%A9%D8%B1%D8%AF-%DB%B8-%DA%A9%D8%A7%D9%86%D9%88%D9%86-%D8%AA%D9%86%D8%B4-%D8%A8%DB%8C%D9%86-%D8%AA%D8%B1%DA%A9%DB%8C%D9%87-%D9%88-%D8%A7%D8%B3%D8%B1%D8%A7%DB%8C%DB%8C%D9%84-%D8%AA%D8%B1%DA%A9%DB%8C%D9%87-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%AC%D8%AF%DB%8C%D8%AF-%D8%A7%D8%B3%D8%AA-06-15
🆔️
@Ir_Azariha</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17610" target="_blank">📅 23:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17609" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فوری | نتانیاهو: ما در حال کار برای حفظ آزادی عمل نظامی و ادامه بهره‌مندی از آن هستیم. توافق با ایران توسط ترامپ انجام شد و این تصمیم او بود. ما منافع خودمان را داریم.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/17608" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو: گاهی اوقات من و ترامپ هم‌نظر نیستیم.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17607" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو: گاهی اوقات من و ترامپ هم‌نظر نیستیم.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17606" target="_blank">📅 21:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع ایالات متحده نیست و ما کشوری مستقل و دارای حاکمیت هستیم! ما شریک این توافق نیستیم که امنیت ما را تضمین نمی‌کند و به هیچ وجه ما را ملزم نمی‌سازد.  نباید در هیچ چیزی کمتر از انحلال…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17605" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsnLFBv0llwpBlncQnS0ZP1h3L2RHE1H-D7XJOGetQR8_iNHpzsDgFm4wh4SOg6dp_xsgbnjufCg8dhrn2xorQbHuIdv8U7Czd2tX2NIBIZ-ulyA5MyNEsTzk3CF0RqIzTakBl_jsF8dwJTlxiYJt2iMqlXUWtgmnKrwuMUE457a0Q2oZqoiVoqHWCDJA3vUM0mzex2VRKaTfOjD-B4CTJ5vr6sdmYgtPRf7Bh3redLO61W3oKTZySzA8DZObZntYiML5PizZx7GeoKvTSZmcDFbJ_CayQPOBMBbjefh2f_oLhkm3N3rvZXjChP3TqZCbCs3QWH3uuVnH8LkxWjfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  به نظر دستکم 30 درصد دیگر ریزش داشته باشد.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17604" target="_blank">📅 20:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Kke2YAZyPd3ikhp8Mh-95xUZZu90j_qsBsxPQP3JaBrLKBezLUQbzmU-DbQWOe9uM9l4-txYcDDAmOlhtI8rJeUt-LjudlaDd5emg-4POo2MLNPcsCAkulB9leRygL7Z1gZkXtQzMYyjD4PxDteaEnSJFdQyD0YSpcqm319JfrT1Q8WEZ60D9O-TZ_hApT4YvRD5fxysU4zma2f2MQnCrvyKXB0J_nIwc9ip9ujOna4o-N4NJd0QBBuEBKtuKutD1d6wClhfFnQPnqckjvr9ZiqgsrZ2PmJU9toUEr9vUEJtgdnFeiE6ZuHTozezv087SfuHPkpehcLrgV71nP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17603" target="_blank">📅 20:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17602">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک مقام آمریکایی به رویترز می‌گوید که خروج اسرائیل از جنوب لبنان شرط توافق آمریکا و ایران نیست. اسرائیل حق پاسخ به هر حمله‌ای را حفظ می‌کند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17602" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار از ترامپ می‌پرسد آیا تحریم‌ها علیه ایران قبل از اجرایی شدن تفاهم‌نامه برداشته می‌شود: آقای رئیس‌جمهور، آیا این توافق شامل رفع زودهنگام تحریم‌ها برای ایران می‌شود؟ این موضوع کی اجرایی خواهد شد؟  ترامپ: خیر، اینطور نیست. این واقعاً یک مسئله رفتاری است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17601" target="_blank">📅 20:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار از ترامپ می‌پرسد آیا تحریم‌ها علیه ایران قبل از اجرایی شدن تفاهم‌نامه برداشته می‌شود:
آقای رئیس‌جمهور، آیا این توافق شامل رفع زودهنگام تحریم‌ها برای ایران می‌شود؟ این موضوع کی اجرایی خواهد شد؟
ترامپ:
خیر، اینطور نیست. این واقعاً یک مسئله رفتاری است.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17600" target="_blank">📅 20:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17599" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17598" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لاپید از رهبران اپوزیسیون اسراییل:
هیچ شکست دیپلماتیکی بد‌تری از شکست نتانیاهو در جبهه ایران وجود نداشته است</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17597" target="_blank">📅 18:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یاد فلیم اخراجی ها افتادم که امین حیایی آن پسره برادر کمند امیرسلیمانی را اسکل کرده بود!  یک تاس به او داده بود میگفت بریز اگر 1 تا 5 آمد بازنده ای و باید پول بدهی و اگر 6 آمد برنده ای. بعد امیرسلیمانی پرسید اگر برنده شدم چی؟!   امین حیایی گفت اگر برنده شدی…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17596" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: این توافق به آمریکا قدرت نظارت بر برنامه هسته‌ای ایران را اعطا می‌کند</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17595" target="_blank">📅 16:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17594" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: انتظار داریم تنگه هرمز در بلندمدت بدون عوارض باز باشد</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17593" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده. طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17592" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گویا لازم است یکی دو فایل اپستین دیگر منتشر بشود.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17591" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwAvJKwLAjw0CvA_OJ7tKSSrM9KaUfQNArT_BDy6wxuBlEXY2uh1eBqFO2znhCwaNTPTsG9jCT840O95mec4t9xi5VnmZ96gCrRQ6lDKW2QdsXpMNmvPArI3JVvtnSoWWySQpAMDOejXFF6yAURMEG1qGReAKWjmTynHQo8P-InDRxxSTLNmVEb10m9T-gAKHxJbLQfr9OWckweC87j_yyWtutQy5AHZnsrylIwRKA8q63zy1WO52dAdWVx3hJcJefR5DcajvVYtQ9DfrTKYNgHwAEVBxFaEsSMlDyfc0ilCJPlcC2whbeHTiaNlLptBBiXHsUMkirRJKal6SupGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17590" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تحلیل خانعلی زاده — از اعضای نزدیک به پایداری — از شرایط توافق  میگوید از 10 شرط رهبری 8 شرط رعایت نشده و 2 شرطی هم که هست به صورت مبهم آمده است.  در ضمن بند مربوط به لبنان (بند اول) هم شدیداً ابهام دارد و بعید است اساساً اجرایی بشود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17589" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در حال حاضر تندروها هم در ایران و هم در اسرائیل با این توافق مخالف هستند.
با این تفاوت که در ایران میانه روها با این توافق همراه هستند اما در اسرائیل حتی میانه روها هم با این توافق سر ستیز دارند.
نتیجه:
دست نتانیاهو برای ادامه حملات در لبنان باز باز است و حتی می توان گفت که اساساً چاره ای به جز این نیز ندارد چرا که هم تندروها و هم میانه روها خواهان ادامه جنگ با حزب الله هستند.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17588" target="_blank">📅 12:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع ایالات متحده نیست و ما کشوری مستقل و دارای حاکمیت هستیم! ما شریک این توافق نیستیم که امنیت ما را تضمین نمی‌کند و به هیچ وجه ما را ملزم نمی‌سازد.  نباید در هیچ چیزی کمتر از انحلال…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17587" target="_blank">📅 12:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تقریباً با شما موافقم، فقط اینکه از دید من آمریکا به مراتب دستاورد کمتری نسبت به اسرائیل داشت (و بهتر است بگوییم اساساً دستاوردی نداشت).</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17586" target="_blank">📅 12:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر دفاع اسرائیل:  نخست‌وزیر نتانیاهو و من سیاستی روشن را پیش می‌بریم. ارتش اسرائیل در مناطق امنیتی لبنان، سوریه و غزه باقی می‌ماند. این مناطق از ساکنان محلی پاک‌سازی می‌شوند و تمام زیرساخت‌های «تروریستی»، از جمله خانه‌ها در روستاهای تماس، نابود خواهند شد.…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17585" target="_blank">📅 12:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-poll">
<h4>📊 از دید شما پیروز جنگ:</h4>
<ul>
<li>✓ ایران</li>
<li>✓ آمریکا</li>
<li>✓ اسرائیل</li>
<li>✓ طرف پیروزی وجود نداشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17584" target="_blank">📅 12:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده.
طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات دریایی" یعنی تثبیت دریافت هزینه برای ایران توسط آمریکا خواهد بود. این اصل در جای دیگری از متن هم تکرار شده؛ به این شکل که ایران فقط برای ۶۰ روز عبور بدون هزینه کشتی‌ها را خواهد پذیرفت.  اما پس از این ۶۰ روز، جمهوری اسلامی ایران بنا دارد با ارائه خدمات ایمنی، دریانوردی، محیط‌زیست و بیمه از عواید مالی حاصل از تردد کشتی‌های تجاری در این تنگه بهره‌مند شود.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17583" target="_blank">📅 12:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رسانه لبنانی:   امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17582" target="_blank">📅 12:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه لبنانی:
امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17581" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=ZOXyYUaGsFpcJAJPEZeuF8hPG_hjr2EKGeyt68JNGJv5PGE9yEOJ_mabjwfhSKHGRNQEkP1p3EUnGCUxjfo39vvBGl2Oe7uqwthM3im78pkz4FKr-oOLRTS09eG08fF7tBKOXI0BChKp7estoTHlTSlaY_cu9KrL3T9QlK9ZtnlI51YQMefqz-hDaG7JwFCzSygZCC46aMJ3EECQXU0z3qs82vJFEgf-2rjPt-0Sqps9-QQlCBxGNhjN_54PwtbsE2imG8Zg1bP1UZGvqsk_NZ4ekwYFSGmEpOm8iKIpqkYEaV3zPQxS0HxCbBQJJGJwUcTdSRPqaONDd24yR9fpPDPv0w7qREqPXZ1bxFiEDMFuSVskYFWHh-Hq1tARXJRGH5AEJUOswM87gxA2CFNxt2d1hujbpyHyB0eiHJp-ve61bZ_TRiRNzb-bo2hQ6edstr638Oko3TXb79Z0cOlkIzFkmd-CqOlImsmH0bYpcztphthZozoQ3IhuTXzsYYY_dXqJIPMn1A756Kdz-1wLvy0QRQZpMVPNXRzTBbjIEOWXID0H4iZyQSw2nWGswfxzlbUKxyMUkRfVXbbG-NzvGr6lrUW5bBZiX5tfalauq8uKDKuBdYi8BiT834hoDlG1wdoAj-bj8PlFxkZbjBILHt6IIPVpjv77T7F_ockGXYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=ZOXyYUaGsFpcJAJPEZeuF8hPG_hjr2EKGeyt68JNGJv5PGE9yEOJ_mabjwfhSKHGRNQEkP1p3EUnGCUxjfo39vvBGl2Oe7uqwthM3im78pkz4FKr-oOLRTS09eG08fF7tBKOXI0BChKp7estoTHlTSlaY_cu9KrL3T9QlK9ZtnlI51YQMefqz-hDaG7JwFCzSygZCC46aMJ3EECQXU0z3qs82vJFEgf-2rjPt-0Sqps9-QQlCBxGNhjN_54PwtbsE2imG8Zg1bP1UZGvqsk_NZ4ekwYFSGmEpOm8iKIpqkYEaV3zPQxS0HxCbBQJJGJwUcTdSRPqaONDd24yR9fpPDPv0w7qREqPXZ1bxFiEDMFuSVskYFWHh-Hq1tARXJRGH5AEJUOswM87gxA2CFNxt2d1hujbpyHyB0eiHJp-ve61bZ_TRiRNzb-bo2hQ6edstr638Oko3TXb79Z0cOlkIzFkmd-CqOlImsmH0bYpcztphthZozoQ3IhuTXzsYYY_dXqJIPMn1A756Kdz-1wLvy0QRQZpMVPNXRzTBbjIEOWXID0H4iZyQSw2nWGswfxzlbUKxyMUkRfVXbbG-NzvGr6lrUW5bBZiX5tfalauq8uKDKuBdYi8BiT834hoDlG1wdoAj-bj8PlFxkZbjBILHt6IIPVpjv77T7F_ockGXYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:  توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟  امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17580" target="_blank">📅 12:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:
توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟
امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های دشمن محقق خواهد شد.
تمرکز برای برگزاری آرام جام جهانی نیز هدف دیگر امریکا از این توافق بود که به آن رسید و آنچه قطعی است، سناریوی دشمن برای ادامه ترورها و حملات غافلگیرکننده به ایران خواهد بود، ضمن آنکه رژیم صهیونیستی نه تنها جنگ در لبنان را تمام نکرده بلکه رسما گفته هیچ پایبندی به توقف جنگ ندارد.
در هر حال این توافق عجولانه و ضعیف که ناقض خطوط قرمز رهبرانقلاب است، بیش از هر چیز ریشه در همان موضوعی دارد که ایشان در آخرین پیام‌شان به ملت اعلام کردند؛ "خطای محاسباتی مسئولان". خطاهای محاسباتی عمیقی که پیش از این نیز راه جلوگیری از جنگ را مذاکره میدانست.
واقعیت این است که این توافق حاصل "برآیند توان و فهم مسئولان ارشد کشور" در شرایط فعلی بود نه ناشی از رضایت رهبرانقلاب. وقتی تاب آوری مسئولان از مردم مبعوث شده کمتر باشد، خروجی آن تکرار خطاهای محاسباتی قدیمی و دل بستن به توافق با امریکایی میشود که هدف آن نابودی ایران است.
و اما حرف آخر؛ این توافق نه گشایش اقتصادی خواهد آورد و نه امنیت کشور را تضمین می‌کند. روزهای بسیار پر فراز و نشیبی در راه است...
✍️
امیرحسین ثابتی
‌</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17579" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQM89exEyHDp2oJNhwd-NimIeXETTOydrbhyQzK8-edzGuogP567ZiuBLhQOBgyr3OYziNK56EujU9Dwh5a_Kg_gz0YSEvX-LF9X5HIyTBdSn57ExX8L4lZkp4VV0UMO_RXqCyM5eaUlWjnLL9QoYZSIGnj41ICJH4R48wnn9jypJLgf5EIPmtTfA74hYv-__EIGSTVpz21LSqAHDap8-eavF7SIPJsRlQFCJZmaLrBvBfEzB6RT_ZHjKCrB7AU29KpbpLlaMkTO_Wt4ry8WqU8rq8kLtHMCLeK_CQ6ic5ijypNFgW8FPG0kCjWTJydRre9ItoLNMH8fXuO4Ng9-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17578" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هدف حمله، علی موسی دقدوق یکی از چهره‌های کلیدی و تأثیرگذار در حزب الله و مسئول پرونده جولان بوده که کشته شده</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17577" target="_blank">📅 10:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17576" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17575" target="_blank">📅 10:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17574" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر امنیت اسرائیل، بن گوییر:  توافق ترامپ ما را به هیچ وجه ملزم نمی‌کند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17573" target="_blank">📅 10:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تحلیل همین است.
این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.
پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17572" target="_blank">📅 09:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">- به گزارش معاریو ، بنیامین نتانیاهو، نخست وزیر اسرائیل، به دونالد ترامپ اطلاع داده است که نیروهای اسرائیلی از لبنان خارج نخواهند شد و اسرائیل خود را ملزم به رعایت بند مربوط به لبنان در تفاهم‌نامه ایالات متحده و ایران نمی‌داند.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17571" target="_blank">📅 09:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17570" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:  معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17569" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Qwyf-UjWAxEbnluNd6hpl7kCxcb5AbMZyPznIIPxCzNsi6YlfxhfIVMMhnxQjucCn9LLRRRZfGr-OxJGO52p-G8hWwi3Paagt_M5BQPEBKq1iEqQuxIW8eCCps9R1WxAelxMxDAQaKAscPHnMkjm2skPGIMbNewp835nhd7Y-jgSrrd5YZ114A3vECmZHY-nBp8rqPkU0bcb3Cl4swjWK-TNycvAjT8DiU3l0nZADT_GM0hdxfjWB2fIxXlIKgEwlaycccLRBQC3rihbKpHHFdOzpmT8agZsj5t7LYsRaolnRM3dM8TxKoSFQ7g0wIbBKCz213J61FBB3lGqOlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه:
لغو تمام تحریم های ایالات متحده و قطعنامه های سازمان ملل جزو دستورکار مذاکرات ۶۰ روزه خواهد بود</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17568" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نایب رئیس وزارت خارجه ایران: پایان فوری و دائمی جنگ و اقدامات نظامی در جبهه‌های متعدد، از جمله لبنان، باید از امشب اعلام شود|</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17567" target="_blank">📅 01:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آخرش هم گفته بچرخ تا بچرخیم!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17566" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فعلا که خبری نیست. فکر کنم آقای دکتر لانچر خودشان را فقط آماده کرده اند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17565" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ
:
معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان نفت آغاز شود! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17564" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDGLWxuKVoAUaEBx9GvMykHIGEZRSUozUUKhIRviVC-313tPYhwj8MHVqo-iystk5fQ05yfnqY3U2ZPxhlXoCQxApf62qZxv2zXTLbSp11XdxjCG2FXj73YmAQvhEbEq8nq5uBit7BMPhU9qLDBUFWmkgO2GY4seOP6-MN1jMDvMbFbZ9b-PXLRcxIplixoaw8j9oLTubmgnsew53bovKhRHgAdUwPhITMe4e-n4oGByYIsbJBfSwv_hL2u_kloE-_dr9Zad9xU2t9qcbN3iDHkh8jOXjOqjnQLP5Oh2KhaxYR_VjLCxYlXlRSEqwWkElh5T3NZz4Vd1gAY3qz0TGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام نخست وزیر پاکستان، توافقنامه پایان جنگ جمعه ۱۹ ژوئن در ژنو امضا می شود</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17563" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ
:
بعد از ترور رهبران رده اول و دوم در ایران، رهبران رده سوم فعلی منطقی‌ترین افراد در برخورد با ما هستند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17562" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17561" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: ایران در توافق پولی دریافت نخواهد کرد، اما ممکن است تحریم‌ها تسهیل شوند - WS</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17560" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17559" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش روزنامه‌نگار اسرائیلی رونن برگمن از ی‌نت:
پس از حمله ارتش اسرائیل به ضاحیه و تهدیدهای ایران مبنی بر پاسخ موشکی، به نظر می‌رسد تهران در حال بررسی به تعویق انداختن پرتاب موشک است تا به ترامپ فرصت دهد که توافق‌نامه چارچوب را امشب نهایی کند.
به عنوان بخشی از مشوق‌های این توافق، به نظر می‌رسد ترامپ در حال بررسی لغو فوری — نه تدریجی — محاصره دریایی ایران و تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17558" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کله زرد :
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17557" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17556" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باز معلوم نیست این فاکستانی ها چه غلطی کرده اند !
احتمالا دوباره نسخه ای که به ایرانی ها داده اند با نسخه ای که به آمریکایی ها داده اند متفاوت است</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17555" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این فاکستانی ها چه موجوداتی هستند که نه آمریکایی ها به آنها اعتماد دارند نه ایرانی ها!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17554" target="_blank">📅 00:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOPz6Vq-sziHx5LWhR2kXOzfbdWGl8vdLdWFknqomeFIqBVBdf7Igp6A8rUJaXq_xUIDNrqJPrBykZVvUUQkWQbAZk71swaQUl8THRGflsxWvNjVl1LIOO6Ri1aUyvKOoQoR7Nt66ujalz8Jfn6YfEk2N6O8_pUhUblhLjZdPd6oyf9bJV3YhAGOWKdonl_eZVDsplCJJpu9Sl9zEAopI-ygeOGJF3mv8ilePxdNg9pSb5ybDyhXLplM_01OLRmxunGZpUAKYE4-N2xMcLNAj0uTxVFYfCw1rRCo24-4CTEjYI5pqJVxuOHWh-QUnbbX3Asfcq1K-uKYZUYNvPDhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.
دو مورد که مدنظر من است:
— همون همیشگی (حمله به اربیل)
و|یا
— سپردن کار به بچه های نقطه زن یمن
در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه باشید.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17553" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17552" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علی اکبر ولایتی:
یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17551" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ونسِ ترنس در بحبوحه تنش‌های فزاینده با ایران به کاخ سفید شتافت!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17550" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:   هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.  نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17549" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:
هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17548" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ینت اسرائیل:
دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17547" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قالیباف:   آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17546" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف:
آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17545" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17544" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نمیدانم که میزنیم یا نه اما میدانم اگر بزنیم آنها هم میزنند و بد هم میزنند</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17543" target="_blank">📅 22:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خداوکیلی از دیوار هم صدا درمیاید از رییس جمهور مملکت نه!
بلند شو یک چیزی بگو مرد!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17542" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوری | محمد مخبر، مشاور رهبر ایران: به متجاوزان درسی خواهیم داد که پشیمان شوند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17541" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-poll">
<h4>📊 امشب:</h4>
<ul>
<li>✓ میزنیم!</li>
<li>✓ نمیزنیم!</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17540" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17539" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17538" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این مقر موساد در اربیل مثل درهای بهشت است
هیچ وقت تمام نمی شود</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17537" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقر موساد در اربیل؟!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17536" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محمدباقر ذوالقدر: لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد
پاسخ رزمندگان اسلام در پیش است. وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17535" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FihpIyvaN1BiMCRlBOfguguIPYvYls_iKjDdFt2NPPqVDN5lpQ94fJwgBLe-IvuyQhbd5AuAkD2kcYFT29WNbkNjBh1T7vEQ7cEA6nUQIQfx9hWtzGtwnfziNSw1BjVnCTblPjyITUNVzYLUd-HWbWy0G30E1Ace8sz6UhmE6pW4jIsLEc5wzUoGpYEfb18bu8A9f14k6iz3qKilr3Ze9im-WRhyBJ9IHC1Oa_q2ni583igk2BgoKzUF3WM48bpPfSFcQx5xFkq46gcSY08F2NZ0NkiWN2uVK2-oP0H2ZVXcpG5TQd9FQPeIMTw35IiZNZWCqcbB9dO0DXIu0zPR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17534" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">«کانال ۱۳»: ترامپ با کلمات تند از جمله برخی ناسزاها به نتانیاهو حمله کرد</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17533" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17532" target="_blank">📅 20:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):
«انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.
ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17531" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اصابت موشک حزب‌الله به شهرک کریات شمونه
منابع خبری متعلق به شهرک‌نشینان اسراییلی از اصابت حداقل یک فروند موشک به شهرک کریات شمونه در شمال اسراییل خبر دادند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17530" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17529" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17528" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.  ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.  — شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17527" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.
ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.
— شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17526" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آماده‌سازی حمله گسترده ایران به اسرائیل
اینتل واچ: یگان‌های هوافضا و دریایی جمهوری اسلامی ایران در حال آماده‌سازی یک حمله گسترده به اسرائیل هستند. بر اساس این اطلاعات، فرماندهان ایرانی از یک عملیات پنج‌مرحله‌ای با روندی تشدیدشونده سخن می‌گویند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17525" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:  «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود،…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17524" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
«حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود، مجروح یا کشته نشده بود، و نباید این روند مهم را مختل کند.
ما بسیار به توافقی نزدیک هستیم که صلح را به منطقه از جمله لبنان خواهد آورد و همه طرف‌ها باید از اقدام خودداری کنند.
نباید حملات بیشتری از سوی اسرائیل در هیچ‌کجای لبنان انجام شود، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری از جمله حزب‌الله علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد، بیایید آن را خراب نکنیم</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17523" target="_blank">📅 18:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
