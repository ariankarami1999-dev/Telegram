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
<img src="https://cdn4.telesco.pe/file/DglKu2MKBPRGxrPo1lOlfAsttA1y2jDYXKZOTmWm1AyQMc6b-GU9AnS_IFJXz0jPoEJEA_xJp07d9YueqW_Fw-KuIKMeg3AGgd8xjSNAfR8imPqCYmQzVvrK9Ta2WrfcjWF-KdBDBQAllJbre9ibXT8iI7kjHSoCFdH79MNeygau35F3qWtddf3aJUfSVh-o1l4KsnRmtPEAkioBP9VMJEpCFUwG7yVQcKIvO5_w7eTykrVBlBRRZsvAJBstjg7RLOpyl4GBJE8M17Cr6tH4sXfPXo11USI_RVrZ8j9ZCl7FNoPH3VaQmbTaW401V272latSiU-OxC3tagkasKvMHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 17:28:38</div>
<hr>

<div class="tg-post" id="msg-681990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تمایل به تردد از مسیر ایرانی در تنگه هرمز بیشتر است
مارین ترافیک:
🔹
تردد دریایی در روزهای گذشته در دو نقطه بحرانی کلیدی به دو مسیر تقسیم شد.
🔹
عبور از تنگه هرمز ۱۹.۵ درصد کاهش یافت و به ۹۵ رسید در حالی که قبلاً ۱۱۸ بود، و تردد روزانه از اوج ۱۹ عبور در ۱۱ اوت به تنها سه عبور در ۱۶ اوت سقوط کرد.
🔹
از کل عبورها، ۵۱ عبور از مسیر ایران استفاده کردند و ۴۴ مورد مسیر نامشخص بودند؛ عبور از باب‌المندب ۶.۷ درصد افزایش یافت و به ۲۵۴ رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/681990" target="_blank">📅 17:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fac94c09.mp4?token=lIwnJa1Tc9y7jPZ0zWYJLrSEDMxrQWY7lD4SfR61sg3M0fiwQcjAYrT6uRg4kX29BXuA69IkPhKo6ZXUP3PZbKdklnmzBDUUR3arut2zczch78xCUBPL_dioo2J6AMqCzFpN7ma6fmoY_s9z4U_WMLQF29OQXJ625BuSHa_-tqb2dNoo6dIttlNR5vAvlLKCq1F2FXH75EeAlbjlo4xUsvl-4n1thLaBttB8ODYwpusBaRaWgxaqUCXKiGbmQXXq5mSv4M3JDPxp_Sdq9ZSWvq8qPpe7pTy1cpwT6gBcQFQVe8ezTRlyviW78kBwqnfqGFsMXsLEafV4KLKzrsDirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای سربازهای آمریکایی در آمده است
‌سرباز آمریکایی:
🔹
ما وارد جنگی شدیم که هیچ‌کس آنرا نمی‌خواست، جنگ با کشوری که تهدیدی برای ایالات متحده نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/akhbarefori/681988" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b10a7b718.mp4?token=YUcDmyMfATkk-wJvGhgmLlG1Vy0T24XMFmILvzLyrLca51ttMlSym8QdFUL-knFeaatfycKwIOgvQ4Mrv-BIH-Y1ygsKxwk0C18Bm7bej0qa59DMXtde7xeBn0_jksZ2h21DN5mDfnculvIN-yPifyfSkZymoaqGyv8-cXLX6EytGoW2OTHVaMRsZJKOHbr475E1Y3-Ui3qIvAUSVbWL2WZG9CKHzEvV4OVQc8RSR23KD31Q_aSiIwxoLrjp9YkilIDpSAvZ1Y-AjuJBG9Ia1bGCWILIot3-XAnQG2AozA0hJ8i7oEHN3mNZj3WblujJrnECXxmiPM0SFmkhw4CjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ترفند حتما به‌کارت میاد؛ برش دادن چسب‌های پهن بدون قیچی
✌️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/akhbarefori/681987" target="_blank">📅 17:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681986">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رویترز: تنگه هرمز قابل جایگزینی نیست
🔹
جایگزینی مسیر تنگه هرمز با خطوط لوله در کوتاه‌مدت بعید است؛ خط لوله پیشنهادی عراق از مسیر سوریه حداقل ۱۵ میلیارد دلار هزینه و حدود ۴ سال زمان نیاز دارد و سایر خطوط نیز با چالش‌های جدی مواجه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/681986" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681985">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قیمت نفت افزایش یافت
سی‌ان‌ان:
🔹
برنت با ۰.۳۸ درصد افزایش به ۸۸.۸۵ دلار و نفت وست‌تگزاس اینترمدیت به ۸۲.۴۲ دلار در هر بشکه رسید؛ همزمان با پایان پنجره ۶۰ روزه مذاکرات بدون توافق پایدار.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/681985" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681984">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سرگردانی ۴ روزه ناوشکن آمریکایی در دریای چین جنوبی
🔹
ناوشکن آمریکایی «بنفولد» به‌دلیل نقص سیستم برق، چهار روز بدون تهویه، آشپزخانه و سرویس بهداشتی ماند و توان حرکت مستقل خود را از دست داد؛ در نهایت با یدک‌کش به فیلیپین منتقل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/681984" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7e5ed0fa.mp4?token=fO3sZA6URjgocisFwAssox7CqFvglIJnoeT16ml6t-OUvwm7GJyqvAycSKBxqCQRPAjjO2XIs0cyDz87BPqGO3vCgga0HT31Aa5_RK1_4DH620rwn5PluXgmYU_EasOdO9KLG4meJErImF7hAWJ2t2UccwRmq5EOd7nuroqk8Rrp0gaVYlxMwOeYpQQJGrm6mVlhLak4t0KlHRDnujNZnknkCZaRqv9lvGvGbQvYy5Kjhfg6KgYqlu8AWakQlfH4bIfoIhywbZAXOlQcYgCHL7hx-dvDNVH3NNxG-E4mUDANrARGm1A4yRlMVe3kkBVuwaqRxKlS8RUyXxs5sBmU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل ورسک، مازندران
🇮🇷
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681983" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681982">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoJbQpDZjB-3RI08IZvEnNgS5U0SLqcotfNfCqJRoyh3FdsRQeAJje4SakpYfQdFnA4NvhpLcHHzDBN0a0m8XCgLV9QHVTSniVGZCH95Ot6wPJ8xLiTNUW4p2MNlckEnJxsjqEX_lVCvKycY0BDp5Xdpv4OCfM2nV9XCmFfhclnPwfce8LyyoVLgsib-s_TJ7mtluWTkZgXUOwnWL_JA6-cBS2ZEz0i_yapNZhaxTQdtSUfGlFDdoXWDUyDZaYxEWiGALHvycBA0CW0EB9MsUnLxG3tpfamAjsBIOVD5iJX2jkWvdry3TuQ2L4Bg3apXxuFstNZfL0aVgyJh3VDJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه امنیتی برای یک کشتی در سواحل سومالی
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک کشتی فله‌بر در نزدیکی سواحل سومالی خبر داد.
🔹
این سازمان در بیانیه‌ای گفت که ۸ فرد مسلح وارد این کشتی در فاصله حدود ۷ کیلومتری بندر «ماریئو» در شرق سومالی شدند و کنترل آن را به دست گرفتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/681982" target="_blank">📅 16:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: ایران برای گسترش جنگ آماده می‌شود
🔹
ایران در دوره اخیر، ضمن افزایش تولید موشک و پهپاد، نیروهای سپاه را برای هماهنگی با گروه‌های همسو در یمن، عراق و لبنان اعزام کرده تا برای احتمال گسترش درگیری در منطقه آماده شوند.
🔹
این روزنامه همچنین از تقویت ساختار فرماندهی نظامی ایران و آمادگی تهران برای یک درگیری طولانی‌تر خبر داده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681981" target="_blank">📅 16:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b64e1686.mp4?token=Rdeqx72AAMZvxYhKZTYgQkl8fBTCmLQppyvBstCDbZmMSyU1MmX3Z3XaWNbSBIhrDe2XyGIq2skL6MTDCE10TcNuPee-pGDSGKk32fQfrUrSQYfs1LVhIBsjsT16drqvUph3FORsQy-_bKiPoAhn1G4EqmW-ZoKFEBeMO_g8Vt-XU90IsoN4miOpEIprMYs3l32PDcQ0hAIeGvKOBUBwn9zKu8tI_rVqGcQjYhSeCC4V0VVhUg8vV47dgDJPwgn916bzjhW3n7LUFDFAUH-LSaiyaYo7elvMrNel5bqZI_eBhn8iMSMOZkpNEE71s3ntucd-0tX8VgMdx3cmJ-E-BIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b64e1686.mp4?token=Rdeqx72AAMZvxYhKZTYgQkl8fBTCmLQppyvBstCDbZmMSyU1MmX3Z3XaWNbSBIhrDe2XyGIq2skL6MTDCE10TcNuPee-pGDSGKk32fQfrUrSQYfs1LVhIBsjsT16drqvUph3FORsQy-_bKiPoAhn1G4EqmW-ZoKFEBeMO_g8Vt-XU90IsoN4miOpEIprMYs3l32PDcQ0hAIeGvKOBUBwn9zKu8tI_rVqGcQjYhSeCC4V0VVhUg8vV47dgDJPwgn916bzjhW3n7LUFDFAUH-LSaiyaYo7elvMrNel5bqZI_eBhn8iMSMOZkpNEE71s3ntucd-0tX8VgMdx3cmJ-E-BIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعویض پرچم های عزا به مناسبت اول ربیع در حرم حضرت زینب(س)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681980" target="_blank">📅 16:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtkpTgTt2sH6ESXtD9dPOXJY0UE6Z6xOioh-2uexGnfeVg0JDh1h8RydvxTfTZol5RlIfmLq4rXrs1l4z1xea3cQ6HOrjVQCgeuuciFPoVuS7NJ4bHj06njpBgqWFabsCkoHPGLPbxaFq_RCL0bH8DCgM4a9uCZ2CK_tHNuRe6r1akyhrfKMwDO129xz4r8t6GVZ7po0iYSm9QKvW6CqL6AiGXiy7Yfqjn5SueU-ToMDZerdK5KvyZ22jbnWC-ZqqqyX8tIrmoFYtqZX-TYdaGToSgyBPHd_JemADLqivPJli_iATN3GGfiiyLHVuRSUDTB9dWrqE8ENAjh8N65BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگراف: پنتاگون از نظامی‌ها خواست راهکار خلاقانه برای مجازات ایران بدهند
ادعای تلگراف:
🔹
پنتاگون درخواست تلگرافی غیرمعمولی برای تحلیلگران نظامی ارسال کرده و از آنها ایده‌های «خلاقانه» برای مجازات ایران خواسته است.
🔹
این درخواست پنتاگون نشان می‌دهد که چگونه گزینه‌های ترامپ طی ماه‌های گذشته نتوانسته تهران را مجبور به تسلیم کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681979" target="_blank">📅 16:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/681978" target="_blank">📅 16:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
نظرسنجی بنزینی سقاب‌اصفهانی در توئیتر!
🔹
رئیس سازمان بهینه‌سازی در آستانهٔ تصمیم دولت دربارهٔ آیندهٔ بنزین، ۳ راهکار پیشنهادی را در شبکهٔ اجتماعی ایکس به نظرسنجی گذاشت.
🔹
این نظرسنجی پس‌ از ۱۰ ساعت تنها حدود ۱۱ هزار مشارکت داشت که در مقایسه با جمعیت ایران…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681977" target="_blank">📅 16:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سپاه: پاسداران انقلاب اسلامی هرگونه تهدید و تعرض را با قاطعیت تمام در هم خواهند کوبید
🔹
معاون اول رئیس‌جمهور: پزشکیان تصمیم گرفته پرونده فیلترینگ بسته شود.
🔹
رئیس‌جمهور لبنان: رابطه با ایران باید براساس احترام متقابل باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/681976" target="_blank">📅 16:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9bf50f4e.mp4?token=OFbwdI3gMrFiFz-Ioxbbb4DRlGN3wUs5nkoqeqnP49S26Z4Mje07LktQ2jKOkL0r6fcU6HoWMAS3tfNWAcCxLbrOCrEaxT-bHOWbcyKWt6XQwg7vgQ_cjbye7ogUwta3GDFQedVH0dRGc2ZVLJemA5ZgdnV7vWPjeX1AYb8zNYlEj-KG3h0pU3SNB0YayRr-MtigzYDD-ezJafvx3mnGrswGd-vVHG-G3nWrLcY56dYkZ3vxOD0v715RkflHQ4A1ulrDzLbnloSPxjUmu58m66cXUle0lcyjIr_cs4N7ZIGZyTFZsPhwfptGsc6tqvbrBLa4x0bBcOQFmeJ7ZjDzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفری فراتر از زمان؛ ایده‌ای جذاب سفر در تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/681975" target="_blank">📅 16:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای رویترز: ایران تصمیم گرفته است سیاست خود را از حالت دفاعی به حالت کاملاً تهاجمی تغییر دهد
ادعای رویترز به نقل از یک مقام ارشد ایرانی:
🔹
فشار بر آمریکا یا تکیه بر میانجی‌ها برای رسیدن به یک توافق دائمی واقع‌بینانه نیست.
🔹
تهران ضرب‌الاجل چند هفته‌ای برای آمریکا تعیین کرده تا یادداشت تفاهم را به طور کامل اجرا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/681974" target="_blank">📅 16:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
المیادین: صدها کشتی در جنوب تنگه هرمز منتظر صدور تأییدیه نیروی دریایی سپاه پاسداران انقلاب اسلامی برای عبور از این آبراه هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/681973" target="_blank">📅 16:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/681972" target="_blank">📅 16:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0633a32c.mp4?token=YZ4pGqqqv3zW3MdMF-X1Zi_52wWaD2C6ySEveIvVicSIV9_tLq8pkev95NXggpoR1a3L3DdnDuHhNgKpMKxtBJUFhlcF5Ir9YwAYXPDFJ3Wm8c9hj3HRzt3ezN0PQrv-R0yjzXjXX93RaiWRJD5ptIZMAvPgYKBiCtPUrOqPATpOjIt6bm8l3_tbOvNN-T9YFQG3ifJz-jUp3kAqLldR_j35-XecKe0CFoveFdf7qWiXEAE76V46txOtM_llUo8GmWfn0TRMyjKxhW1ZZ8CWtsyrG5clIlcvfDRgcbYefPG-7r_G1xb5QeRUYgZrEndYGQuNDupidElNsJqKsGKiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این چند عادت، ناخواسته‌ شما رو پولدارتر می‌کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/681971" target="_blank">📅 16:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpO-U-yL0h_pZT2Cql_o2Y8Oui23hCQbgmeaM67LWfo8VNTHxKciDc71By0JWmBx--YjmY7zKRitkbp_qnWkF91bY2Rvpolk9ZeRy1vj4V6cN4ed24IsQrw3WsSxtpIHgXivjWVzgeHNOdN_rfkp6PdbxpjlYoVwxQMXRnptjT7CWAOae9c-obPBvW95vEP9X4UuvfH3G175xguAoRnYqJml4y0T4xjxtDmXE3JOQPgM43bZ9IroscbUty8cF5L_By_TKQdpVfa2j2coFfw2QQDtlYfdYMgrL2rGHqpNKyke3BAVYvoo7XbqpdYVQVqT1fmv17fcKzLj4Uj98g218A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر جنگ رمضان بر افزایش جهانی قیمت گازوئیل
🔹
پس از آغاز جنگ رمضان و بسته شدن تنگه هرمز، نگرانی از اختلال در عرضه نفت باعث جهش قیمت گازوئیل در بسیاری از کشورهای جهان شد.
🔹
بیشترین افزایش قیمت در کشورهای واردکننده سوخت علی‌الخصوص کشورهای جنوب شرق آسیا دیده شد.
🔹
این جهش قیمت، هزینه حمل‌ونقل و در نتیجه هزینه تولید و توزیع کالاها را افزایش می‌دهد و می‌تواند به موج جدیدی از تورم در اقتصادهای وابسته به واردات سوخت منجر شود.
@amarfact</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/681970" target="_blank">📅 15:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون اول رئیس‌جمهور: دولت بنا ندارد اقدامی را بدون اطلاع مردم انجام دهد.
🔹
جانشین فرمانده سپاه: با یک‌صدم هزینه‌های نظامی دشمن، در جنگ اخیر بر آنها غلبه کردیم.
🔹
مسئول سیاست خارجی اتحادیه اروپا: جهان بهای سنگینی را برای بسته شدن تنگه هرمز می‌پردازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/681969" target="_blank">📅 15:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f238b08db4.mp4?token=Gyo8hFSfz-RJNlA7hSSkWiuCjYJpMTJwUg9X1xNTy1T6QG3V2y1Po4VyHhp3Y0Eb1dVu2W3ZPUQllDqN_kGgSoXC5qspaNCq7cdoLwA9GkWWpaBtaBvA_JG-_AmlCoQmvMmbNIyII3GSXCsyDce1hxM9GwILHYI2loxy4wueW-RX18hwfXxz376hVP-G5a8ZBcOmlnvkp-8AIH4SjkCE0L8nd_wCCXwWn1Hf3XZjr-pRrx4PDY42YPS1jBBTyVxIDi-Q666xvJgFHKyLyzMYSQppJtvPFj4DoOQVANbhe4o3pgJUfwoQqQBN6OROQvvFET1aMYN7gh8SFCUYyTtf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش پوست ماهی‌ها رو راحت‌تر بکن
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/681968" target="_blank">📅 15:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: مدیریت عبور کشتی‌ها از تنگه هرمز به ایران واگذار شد
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در آخرین توافق با عمان قرار شد عبور و مرور کشتی‌ها از تنگه هرمز با مدیریت ایران انجام شود و عمان فقط نظاره‌گر باشد، همچنین قرار شده عبور کشتی‌ها از ضلع جنوبی تنگه انجام نشود و مسیر عبور را صرفاً ایران تعیین کند.
🔹
تصمیم‌گیری برای مبلغ دریافتی از کشتی‌ها به عنوان عوارض عبور از تنگه، درحال انجام است که مدیریت این طرح بر عهده ستاد کل نیروهای مسلح است و وزارتخانه‌هایی مانند وزارت خارجه نیز با ستاد کل همکاری خواهند کرد.
🔹
عمان نیز از این عوارض دریافتی، بهره می‌برد اما سهم ایران از عمان بیشتر خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/681967" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آرزوی تکراری‏ ترامپ قمارباز: ایران باید پرچم سفید را بالا ببرد! ‎#Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/681966" target="_blank">📅 15:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تصویری از کشتی هدف‌گرفته‌شده در تنگه باب‌المندب؛ این کشتی متعلق به مزدوران سعودی بوده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681965" target="_blank">📅 15:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079fc18e6e.mp4?token=DJseTqY0Mf9kg2lhAcAITMrKOgUC4v-7q1kxzkXA4e5cDf9Hrzx_jKmyTbsrPW5FZPV9ns-Qj5svgRPDR8KtzlqLMqhw7Wc0MXkz96zVnshs1SyTcFjcSL5x703NDLjYd0Mu67cnL0AZXYF4MKOCs8ZuhJS6j9FRnUgqgZKLTnQCqj-szxCj9OY7ohUCR3XKrLHaJ1cxQ9RmyXMP2TrRPNbYbs83LgQBHRuv3OTpsQr9BDuYErtWywmwYWZX8UdMR_QUzfu5QO3qwjkjmv-9H5fvzcBNLAldjc7QX8XfITT4LzLqA6f4zowIIdOAW77pCayDj6DKoYQGhjBy8a6CjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران حسی عمیق، شبیه افتخار، شبیه دلتنگی، شبیه دوست داشتنِ وطنی که هر گوشه‌اش، بخشی از جان ماست
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/681964" target="_blank">📅 15:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مدیرکل حقوقی وزارت امور خارجه: احیای تفاهم اسلام‌آباد به آمریکا بستگی دارد
🔹
نقض تفاهم‌نامه اسلام آباد به معنای فروپاشی آن نیست و امکان احیای آن وجود دارد.
🔹
این اتفاق زمانی رخ می‌دهد که آمریکا عادت خود به نقض تفاهمات و اعتیادش به وضع تحریم‌های یک‌جانبه را کنار بگذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/681963" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/681962" target="_blank">📅 15:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جزئیات طرح اسقاط موتور سیکلت‌ها و خودروهای فرسوده  مدیر ستاد نوسازی ناوگان و اسقاط خودرو فرسوده
🔹
تسهیلات این طرح از ۴۰۰ میلیون تا ۱.۲ میلیارد تومان با نرخ سود ۴ درصد به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/681961" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa44eb4ce9.mp4?token=FHVWm7f4_N6Bp0aof2C7EQsmxY7B6sPIzYgk8cS0gc5qXtRZljw_ZQWomkaw0JAJbSM2_5Lszjw1X72_rcN5OJHOtJy-rDaGqlWXVAxlee9p9IsUDYC4Bx1d6IQy2byj500s3OvZDLwLMFLnlxxFjiH4WbtSmZqfQGkKUKSK2rszx69hAQadScGNzCIKVptfECXOIJ0mWuZFE70JtEphrQIT82zoOG0hJrN4GJHhrk5BRYgqed9RuigYk2DWYAlXjtvrW2F1MjHzWipz4m5_ltB5vqDnudp8Cvfs7fcZY6lUfRWbX1-keu3ZiaCWjyu9glXNsPwD8KKu3Dy8NWQ7WXlEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید عده‌ای به‌خاطر بازار فیلترشکن بر تداوم فیلترینگ اصرار دارند
نخعی، نماینده مجلس:
🔹
بسیاری از مشکلات فرهنگی حاصل مسائلی است که پلتفرم‌هایی مثل اینستاگرام ایجاد کرده‌اند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/681960" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmQ9nd2ARcOZkcIaEW90Fkajvph3Y-njgPKseiI4nMtBM9NwO5OrSNiizLPTZsupI1QPhCeQhDvdvNEDXExfG5etkfctjD8-pA2-dlSgqII_zkDT6olyFEW_6IZtnt3v6FtxsP0MsdggVN9KVna0BlRoPC1MtLt1rnsFb_P4TLTVNYj0z53s_VtkDZrYpm67wMdSrsO0fiV_zeXftbSRwxZ37iC73IVlPP3nencW0lfCCrDCC4RBx-6TBDjcX3H_01TVkL6cEjLCVKxXeVS6w-LBHKtLNUbW8PnNNE25bkcPvXdf9w3JVAg61y_LnxqdKAEq1aHwE_KB8953Nwp0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نیروهای مسلح یمن در یک عملیات موشکی بندرالمخا را مورد هدف قراردادن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/681959" target="_blank">📅 15:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuD7qrWYbRiS2vSAHyGYSI1KfNZQd5whnrKOHkEJCDg5RzpS20Q-fXcACMbB2FWoDYdNlXYyNwLqZqnzKbykVZK8XKAvhSoBpDwBgEx2f27_Nrx0P053brJAH7ufXfbsDMru2azKoxuNc2w2220H7Ly_3cDrp4e6TSiCZB_Bx1OMAzMfBn9hLTvE_OHFS9VYfM8giKX2NaU7XmVxdOK-75hwa0O0HIyzYUzEWhzcQNHkHdmws1NsI5fe4qB8BDVye8ET5txkvf2T0K41lC_znO40ac2Wms6pjCYazVW9xV0Djf2bfKMXPcElIZeJew-dqsuV8iPSnDPuslRzq2M_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خرید اعتباری آهن‌آلات با LC تا ۶ ماه
⚡️
مزایای خرید با LC از آهنگر:
* تأمین انواع آهن‌آلات موردنیاز پروژه
* امکان خرید اعتباری از طریق LC
* مناسب پروژه‌های ساختمانی، صنعتی و عمرانی
* تأمین از منابع معتبر بازار
* پشتیبانی از استعلام تا تأمین و تحویل بار
برای دریافت شرایط فروش LC، سقف اعتبار و استعلام قیمت وارد لینک زیر شوید و فرم را پر کنید.
🌐
ثبت درخواست</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/681958" target="_blank">📅 15:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a0d5787d.mp4?token=Aprie9L-kaam4iHXFUa43vFfIfD7ZQaIejBtaI1y479AYqDw-FvGpO0B_WkGZ4SVMnPgHmxDpYzFrTIvX_Ju0FR2ILxvfV9Un27zbFbTE2jaXgbapt8wCmHrlIGKbSDfVnxOYZVZnYZzd6JtQJWw2JgQmTq2V-9UN-UBpZKI_CHsDYEuSHcGaN3EiWNCalzCZ4iGe6OjEVvvblqSElr2vuErAKR73_6D4He_TMGV7Uk6JWCZrKgZSnYECFYqyKP9KMtOT7YLLhPt_lNrx3on26JRo9-RIrhrKPyda5o84aCjQNIDu1AktJwFvzgl2Q_yZe8rlKZQUJoTUX7tIUBXvk3PSEtCYSC1r0lg6XF5OJUpGHqB4tcwbkneCUmJLDlqRpi_P97T8jJOfJ9xWtMnZVz8fGikzYvCIO9geJsmQP4tJ8oucAlqMk9o3evhEziJvtA0u53N7sZKjcxiQStmKHglNmoHgxzrfR2u-fhN8_cKTY-cwy4myYpqqOuwSIc24gR95YHiR5bwzP9f--R1ArqQ9iBDg01O6d2dOgj_paNj_JtX4DwHYyVlMMSvP8AkxSayVdxavkmEQatdPXLKGqaSVhboR_jNE6VTfUqsjjPhab3NPDiyeot84bsTfuLJL0ByMNVQ67_YZRbZtp7ujdgeWGfDFfFfUblFIqgBz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گوییم یک نفر ADHD دارد به چه معناست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/681957" target="_blank">📅 15:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP5C1dBHwfEyyDMx-7VTmxciwpheH1pmTNvUbfyN8MoR3dOvrmfWdKpHiJQj1p1xLXqCOlnx3eaCB2BJcko9gDVVYewGWquIdMWfnuhhdflxdvC9QSApOBnYnjERicZF1MVCdrAVpPb9EGpAjLrXbAPnFrktkatgb01ULHiVhHmaUftKo7AcXpGYKJ77rbjfJ-gupqy6pbof-bUV7GsKMhbk4M2lTnFYuH7osN9o2u4rnfQSyJ3j88iVMs7yYdweF9qm7mUGeJ-JOn1QsDCC3Vd20s5wSuc6YR0_Q9cvXdFZ4i4LZnGoxiL16iZl7V9GbJD1NXHb6Kt3rWjTd6RNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۵۵ درصدی ارزبری بازار تلفن همراه
🔸
قیمت موبایل در سال ۱۴۰۵ بین ۳۰ تا ۸۰ درصد افزایش یافته و ادامه وضعیت فعلی، اشتغال مستقیم ۲۰ هزار نفر را تهدید می‌کند.
🔸
ارزبری بازار موبایل از ۴ میلیارد دلار در سال ۱۴۰۰ به ۱.۸ میلیارد دلار در سال ۱۴۰۳ کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/681956" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=IuCqHIYZXIt5dXslSVHhZfZoaKJ887kcZkLE2a-6utahSlfC0KI9gu1u8AZKHJi-zdA6lhrObE4jby0B_ULnHWamC6Re1fWV_JYZxzf3ZQyCx9Et1NYxQsLpRe9GDLkOa886YTKkKMrk4V7WgCOxVDCVkatcC1zvZ753GpsDz5ZuFUs3rENfg76655yQiPpV_J8Q2kvv4wZMPTGn87Hhkg1N8oUtRLTjXHXFbKNJ26kNF61eTBfZeRg_uan_x_M6fwicYR-zGbiPtyXthKBsmSX9BMkGOByuCNyz-tNKT2uDGOCGrGZZyf37xg5vBtyd8t6HdDAxpx7aZGBJnQOVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما مستقیما با مقامات سپاه در ایران صحبت می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681955" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ درباره انتخابات اسرائیل: فکر می‌کنم مناسب‌ترین کار برای من این است که از انتخابات اسرائیل دور بمانم، اما ممکن است از یکی از نامزدها حمایت کنم  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/681954" target="_blank">📅 14:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ترامپ متوهم: آنچه تاکنون از آن (مهمات) استفاده کرده‌ایم، در مقایسه با کل ظرفیت، بسیار ناچیز است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/681953" target="_blank">📅 14:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/681952" target="_blank">📅 14:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8966be94.mp4?token=XmNWRVPwoNocZnbd-LnY4ZeCQP4DvZwFf5T-LTqb1duXQjggptpkD0g3H5XOH_wA6sM2-j2XKW4oXZ3C1Ro43tO8AbMURdeWQHTlyADkAoJmBPrl1DsHi2ANWyUkZrwnnsyCdTKUp7m4yaZ8LQ3Kil5XzmBMNxknzNu-n9dyE3T4nyf1egAYHZIdD1IxgA8ODHDXmB36ZBJiuFthVohLvsjC0lHfBlgmvo9wWqAWHN1IrEGD7clQTLwzpQ6wC6lPNu5VeLwC_gAGVsDMZTENZuWJqFZTF-JtkgzIYwiP4EaMOTNGtNWdyxjgirLbQfADdDySHJNtm4pFv5Y-8NEJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفت بخیه ساده، یک پاپیون دوست‌داشتنی؛ هنر گلدوزی در چند دقیقه
🎀
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681951" target="_blank">📅 14:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
چند خزانه، یک واقعیت: انحصار خزانه در بازار آنلاین طلا تمام نشده است
🔹
بانک مرکزی سرانجام امکان استفاده از چند خزانه برای سکوهای آنلاین طلا را پذیرفته و بانک‌های ملت و سامان مجوز خزانه‌داری گرفته‌اند؛ صادرات و کارآفرین هم در صف‌اند.
🔹
اما مسئله اصلی هنوز حل نشده: سکوها فعلاً امکان استفاده عملی از این خزانه‌های جدید را ندارند.
🔹
یعنی روی کاغذ انحصار بانک کارگشایی شکسته شده، اما در عمل پلتفرم‌ها همچنان با همان ساختار قبلی کار می‌کنند.
🔹
گرفتن مجوز خزانه یک مرحله است؛ اتصال به سامانه ناظر، ایجاد زیرساخت فنی و امنیتی و فراهم شدن امکان قرارداد و انتقال واقعی طلا، حلقه‌های بعدی این زنجیره‌اند./ پیوست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681950" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681949" target="_blank">📅 14:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
افزایش تمایل بانک‌های مرکزی به طلا
🔹
گزارش جدید شورای جهانی طلا نشان می‌دهد ۷۴٪ بانک‌های مرکزی انتظار دارند سهم دلار آمریکا در ذخایر جهانی طی پنج سال آینده کاهش یابد؛ در مقابل، ۴۵٪ قصد دارند ذخایر طلای خود را افزایش دهند که رکوردی تاریخی است.
🔹
همچنین ۸۹٪ بانک‌های مرکزی انتظار دارند ذخایر طلای بانک‌های مرکزی جهان طی ۱۲ ماه آینده افزایش یابد. میانگین خرید سالانه طلا در چهار سال اخیر نیز به حدود ۱۰۰۰ تن رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/681948" target="_blank">📅 14:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d621b4d8d1.mp4?token=jPspYxMjPzl67-gomILyO8njKTovF1zoh_X1bHanCZsSNJY1OEFWOWTuyDlovyPfCY92nLhsLF8W6WyTsgiRbvliS9l43nIBooPFYmyFB3DIn7KfYBgIHldz9etLWvzQ9o_cu9wT26Rj-bOUzXPSrhhASwJmyJYjhB9hCQAuIIgx9HUUD4vvKTACne8_l3-VhmN_4rrZpkaeaTXnugsG9MiG49qqaHUwG1q2Fd-19mGqJYPrWKcO_VF1zVAJTQ3J671Q_aZTKTP__7ONbakp6NNjb-ddsMpPrYy4m1_SEnCJkA6ufRjbd59XTHxc66rjdN6x0IYi7acJ02o_R6HFloWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشکسالی بی‌سابقه در هلند؛ راین به پایین‌ترین سطح تاریخی رسید
🔹
دبی رود راین در هلند به ۶۱۵ مترمکعب بر ثانیه رسیده؛ کمترین میزان ثبت‌شده در این کشور که منابع آب و حمل‌ونقل رودخانه‌ای را تحت تأثیر قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/681947" target="_blank">📅 14:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای العربیه: خبرهایی از موافقت با تمدید مهلت ۶۰ روزه میان ایران و آمریکا منتشر شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681946" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uClQ72cj9dAx8rOzIVOXcGQ3SzxfgphTyx_vVNvCPc0ITaSiiGZM5WUEMyIoclFhvUCRB8Lf6pAEA5AUTJj6gINW5Thk6k-0xo_sFr1OusT4dsY4qL_FN3U7sM6lFYadlyEDAjmLt6gPhf2jOpX9taCdhAoykuyTD6vavKFdB0EmHyzB3ZitTlsbXKrM8b2EXSKkRH77iQtt_7uvhYN4UOJjPSTq-UwlIFuEJgSGBDoLPCcC7iDn1ZihPeLU6cPxk0-GUi9sv6Z7_Y6l_3XRaoss1kPbDBSC0mSSWYDaQ97q37lAC5wskesgvnM9GIy7mROozafO00PCWYFPWipDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش توییتری بازیگر مشهور نسبت به سکوت در برابر نسل‌کشی غزه
لیام کانینگهام، بازیگر مطرح سریال "گیم آف ترونز":
🔹
اگر از خودت می‌پرسی چرا دنیا برای متوقف کردن نسل‌کشی در غزه کاری نمی‌کند، اما خودت تا الان در این باره حرفی نزده‌ای، بدان که سکوت تو را به‌منزله تأیید تلقی می‌کنند. فرقی نمی‌کند دو فالوور داشته باشی یا دو میلیون؛ حرفت را بزن، لعنتی! سکوت یعنی همدستی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681945" target="_blank">📅 14:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کارگروه ملی احیای دریاچه ارومیه: آب دریاچه ارومیه ۷.۶ برابر مدت مشابه پارسال شده است.
🔹
کوشنر با نتانیاهو درباره غزه دیدار و گفتگو کرد.
🔹
نمایندگان حزب‌الله: دولت لبنان دست خود را از مذاکرات ننگین با رژیم صهیونیستی بیرون بکشد.
🔹
نیروهای مسلح یمن در یک عملیات موشکی بندرالمخا را مورد هدف قراردادن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/681944" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7399b39d67.mp4?token=NP-YToJkVMValSmliS1lSceHck3jDHNyXO_trNXKTESSX7BCyOkhpOml4vRx0rBcP2UGySZ4e0yyBjjmZz6nAoX7no-tYOEiJ5AacEiLd2-2PiyuzQk3lRPMZw_Gj-uy6Jj-wXQFeOzfzqHGctPZWsS6AU9-a70KtgikwPF_9-Juxz0h6-ucENVXvAD_9iUbkcYgEgCvUtgrbzt7tp509psV1g4J-EIscBc3AssORja_0RWiwXgyx6Vx8202lMgX5D37UP8WrT7omeTAQU8t6G_4PyCSztc2OCogpd2yjljP_ckHjW_C1VnwpM41dShuiSGxYp2cYNBIBP2pFyfDXgYAc2oh231J2VEFtTqG3dItMIPfnU0LnC5KW-mlRf9wyvBNYuoQrOIExHSl81ul-xuKTTBhlOWfIfjKxCGt81_jUYlexrqrJkijWz4s6Bwi0kpQ27ZJax94WVePrp1xNmXOd_IWc2gNXO2wimEqT6AC_KECQ_m4GU74pCqNWQ3bRei9vkH7jg5vrUdF3K3v8L1FpNUnDn8aIEc1xl8KGHzSdluWon3n72Ri2W-sMPgeqTl0TKUwlwFjG-e6p3uEQe3zxhFv6EB-z_6U53yAatAt9XQbx8LYVKqqLrUQRcULcMkb_2YNR_4kgXX7p4IEznW9jttSQ33msLeml1WpzgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوکیا N93؛ یکی از گوشی‌های پیشرفته زمان خود
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681943" target="_blank">📅 13:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXF2ZBVlz2LOHtbGO2HOobKeir_ukCtyHGqOhkaxHWfD5RQDeGaOdRCEMd5qCYHHVRjl8e3tT8gFowALrLKJZjFP0EGltJoeWatYcEY6aJ4oklqHWnZHgg9ilBw9cchfcyccpxcP3YxyrG4PA0jyavpN_HFcNYJVaj5ldDQwa2EKfsUpOzMPIhHE2TIQLr8C4dE38tf7bypxhqz4VprizphFnWyuYSzH5XwPDWRAVD5ukBFgCq_fdCS7-kbGVwVXUfnIhgHszZRP0mgiWE7YerF0sL1kxE3h91yL4PZAllHvQyMkEWbDssdndVpYCWjehCu0NkB34KBDzBeFpgmaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز: هدف شماره یک، و همواره هدف شماره یک، این است که ایران به هیچ وجه، تحت هیچ شرایطی و به هیچ شکلی نتواند به سلاح هسته‌ای دست پیدا کند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681942" target="_blank">📅 13:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681940">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f17673114.mp4?token=qiefUymhhDeifHw9GVj-gC-iuDBwSUNUE0ao662NoymezxFoNPB7FMyql6xK35gSPzipK7ZKXeTqgMt9MJlB3pI7FG_T7Bhl96IsGhyn4iYKZ7HMtbKrxGETNIqsxPffAMoskv59kGsvkowDqbd9SOU836_gKvuxnkY9MEEUgDn9ivUxOmYG91iibmmw1N0wXRyPkvrJRx2keuALKlTH4_YL7TYZO0ajhOz-W-vpEDPFYsb6p529m0mmoWkVaYsh2J00v3wJ2mqSt9wV24ezwWvuhnI12yeOqbnfAlOfW0eqgM46deqjBKSrKOXa0iqjBE02-iU1kP6OK94APO1SzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن اولین عبادت یک دختر ایرانی؛ ویدیویی که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/681940" target="_blank">📅 13:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681939">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF9o7FaWC_98v7zRVnGoyvnOmPLUAER1Bou6Tpfd50PPUNpbsOra4_9AfYvJH9sJMOGZz_XKW4YKmiCK6MeC94aBQ7Fn09Gf9UnzDX8JACMbgp3TKzpJH2sW0YAqStkCib8Rdi7xvytyFS-CVOznHKXl8lvOda7SeWW0H5xWqQjoF6TYKYW76ybgZ--nUgcpb3bIzXcBLxEjOH_OuhfMNQF1qhUhNN4ZTl-KA_lOqhQ_IR9vGdUEvDkN3bQsrXb-tes3LvyLHSzGEFVJNMXc9ifrNAWrwDzIkA2-q10VSyv54m5QAElGz7-bTMr77fVsWHrLw_wQejVPz0zok7tpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی که یک ملوان آمریکایی از کشتی جورج واشنگتن به اشتراک گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681939" target="_blank">📅 13:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681938">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سرلشکر ایزدی: در جنگ اخیر بیش از ۲۰۰ هواگرد دشمن ساقط شد
جانشین فرمانده‌کل سپاه:
🔹
در جنگ اخیر نه تنها ایران اسلامی تجزیه نشد و خدشه‌ای به نظام اسلامی وارد نشد بلکه خود را قوی‌تر و استوارتر به دنیا نشان داد
🔹
در عملیات مهیار اصفهان چیزی مثل طبس اتفاق افتاد و ما نصرت الهی را دیدیم. بنیان ممتاز فکری ایران مبتنی‌بر نظریۀ ولایت فقیه است
🔹
حماسه‌ای که رزمندگان لبنانی در مقابل ۶ لشکر رژیم صهیونیستی داشتند یک حرکت عاشورایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681938" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681937">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf402f74e.mp4?token=B016RPaOguSIKoULvcQwivYXo1EufZa8OVkGLNbqPVoX6tz9g-_v20H-VBHiq5vx97uCNIFlgLlkqvyDGEDq7f2RvMSaztdjGBofWjMNzrjXqZni6qVoJb4hkjpZ28rcbphMCqGRTUguFrhNrSRfPUcvV3B3eKp6Pum5kwG3iiipqx-U42sUJWIaZi1BH_iV5eYdDu43RbLX4FIB3Oaw52_uBb3yrwIswUPyI-WKje1no5xrgtiB0vjxuuKv_-vCS_R31meXxEW4PWs83xz55cMjSiOHQTdq7uty0BwOaZXJIafJ1ekEKxR-7wlQTH3FBZb3sDLyXFtqqYgYFXSvDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«چند روز مانده به کنکور؛ بخوانیم یا استراحت کنیم؟»
محبی، روانشناس:
🔹
راهِ درست در روزهای پایانی منتهی به کنکور، یک جمع‌بندیِ هوشمندانه است: حلِ یکی‌ دو آزمونِ جامع، مرورِ مطالبِ مسلط، و تمرکز بر مدیریتِ استرس، تمرکز، حافظه و تکنیکِ آزمون./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/681937" target="_blank">📅 13:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681936">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde605370a.mp4?token=HL7MK49qhmIR-1JpIVRam4jYWPSuFKATohiO6DKLf5uxPhegD03oACBnzbkUWswbZvc0u9lTAhA5opYG00x1rheU9oUofsGt-DB7QDRe4_wfgifsHBgXUcG8rvXLldXpMIhhWv-TXrqPMUDE93MRYo81DKehhxZxWw9d8v_9QMIGmdHMZvHsMej17ULFcsoAmeTVLe_3v-Miv8tkuRJ-JzOzR70au_ZDXkEYmepQuENuHqULl6EoqpPOuznbHdTtEYc9poSUxw2prTIvIkKnXAloROT8WBzF5dlCEA8DUzi_7ZFoxf8kAA9tD-7KThtjzlSU6uWinbkknA5HeAjzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز ناتمام یک مسافر صهیونیست
🔹
یک شرکت هواپیمایی آمریکایی یک مسافر اسرائیلی را به دلیل اظهارات نامناسب درباره غزه از پرواز خود اخراج کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681936" target="_blank">📅 13:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe61f8ddb.mp4?token=S5aFDMU8BLSJ1Wf1JWWOZcmCr6MBHVKpEDJssCOYF7EYOaD63bo_pJHQuOs8isW1GBC2ceK2fKns0CYTv2ZPkXJ13RXNZP_0UlFYVSd2am9JdkLUW7ppp5dOAAUjeAv3irTbtromOPif4f5-sbOsX-jpYyI30r_WJkjbx_r6SMmTuastqWJGHUz-uBz82ehLDbIseXWGls9fELQuTkk5keG8a58ensMkwCyDERMD3x-dIOKQGeqBSpC3Mpa-iisGmTFXPpM35x-pgxCfUAPMhyOn9_YgXTDos3hbFKzgSff_DEP9akTw1p8p_KxXoKi91iQ9L0FbqybRWA7xn46I6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی پربازدید از تلاش یک خرگوش برای نجات دوستش
🐰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681935" target="_blank">📅 13:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681934">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پلیس راهور فراجا: حتی یک خودروی تولید داخل در مرکز آزمون تصادف، تست نشده است
🔹
رئیس قوه قضاییه: تغییر و جابجایی برخی مسئولان قضائی در راه است
🔹
مدیرعامل شرکت ملی نفت ایران: تولید و توزیع سوخت در جنگ بدون وقفه ادامه یافت
🔹
آتلانتیک: ترامپ پس از ناکامی در برابر ایران، کره‌جنوبی را برای پرداخت هزینه شکست خود هدف گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/681934" target="_blank">📅 13:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI9jx4yGPcsX_lUWKs0IyQiEtO22kv4g2mZvvH7910C7zbdb0ZpnCyVuut80cbHl27L7KpxgeI489W66hFZe95XfQKotLIQtCRuZFkTnppwmbiXh1t0_MZ7PpYeUcEqYjZafBjtZYyfjZNGrikKAVq82rmQDFwMTa2HueG0K8oq2Y_H4100Ug0A1HuwiEsGjO78h_o1YFmrh4X_-3fsci8_89ojLxDpPQuSWxMnWIGPGmjyJ3IGfmLkvbOzy55pdwGhihmqtDfUDARKF0LpBlYsR8LUQ2fd7khP82D7fXS_LDDOSxVD7Y8VE8gSMFktGS5Af4IOmpgAnoVOVYfELKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رئیس اقلیم کردستان عراق: دفترم هدف حمله پهپادی ایران قرار گرفت
🔹
مسرور بارزانی، رئیس دولت اقلیم کردستان، مدعی شد دفتر شخصی او در حملات پهپادی ایران هدف قرار گرفته است. مقر رئیس سازمان امنیت اقلیم کردستان نیز هدف این حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/681933" target="_blank">📅 13:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnK3nmba4pgJQM5IoCiZj075u4u1_NnrpOqSnW-6Xd5pKM3K9KR80yEwqLGRkqaMZ1JeS9JMQ4pLEwe5tsyzeIc7MW6TQ8PFGHjoQHj3VscvIMSzIr2ByfduxKmtW3pxfAjEvsAdq6mbf4LLFdNYtp2-o0zh77L5xKt1cBYzRrouztQmx1SV-7CtksrisGTWX5dFdg8zjl-YAQbnTkdwSHGjdAuApnsXc_AcxtSno2k2leeqbpGZMUzbLzV4zlIi3ViIZUN747HE2_j5ou5-QP9RENL6j6T06IOsFFRbkz11HirPRTVTi8j1_kYQP13bvDtZTlHUsp7DnTxr0AJ60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: امروز خانواده آمریکایی، هزینه قمار سردمدارانش را نقداً می‌دهد
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/681932" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch8y43Nge8g36iVmrpOKCukFyLDAvnT2a3KaKZgJdeLjsx0StXQBobdTdD5iCHoOX0p5f8-64LhGf_m9hD1mbyLEllAV7i8S7_vg8g_S5P3_-ptJwnGYccKvpJysTanuxQk2LzGmg1dvBr5cC-0um_N8jKjebezPiRFs250mBV_24ecxxJorFnzCc72HDaVYMhlYGwTjgv7dU9mtDDyEIjfJl8vKiY-BAoIjaJ6x7fASEfqkhyL8rluev8P7rbWGh2-5tTPQ5S2Ew484zlPzh-BqFkhuI7exSlvPF37BE_xxZNaX3NtYo6pjmHSgLKnqf3z3iJheN7_slxAWFNJmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۶ مرداد ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز بدون تغییر روی ۱۸۶ هزار تومان ماند و پایان آتش‌بس ۶۰ روزه ایران و آمریکا هم واکنشی در بازار ایجاد نکرد.
🔹
تحلیلگران این بی‌تفاوتی را نتیجه آن می‌دانند که در دوران آتش‌بس نیز درگیری‌ها کاملاً متوقف نشده بود و عملاً آتش‌بس واقعی برقرار نبود؛ به همین دلیل پایان آن هم نتوانست نگاه معامله‌گران را تغییر دهد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681931" target="_blank">📅 12:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پخت کنسرو خانگی آمیش‌ها؛ روشی از سال ۱۹۳۴ برای روزهای سخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/681930" target="_blank">📅 12:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPvKLtTAWSn-edE4E6o4InOlcsPjpDu7V1c9H0qH7Sxo5PpXAthKJeXCf98BV-RwjEMpvVzSGzR5rb8KyMp1pcRiEcuCzIK10rSQ4vfM8NOv3xadAmloK5hLz0bSxcpGoJzSOjOrwm6cA513RuwnrK1qZHxHkmIMN6NPcOhgYzaKQY6G-pdKMKuFEBmbyyD58BGslKtn2Cnou2lEFgQ3vYuv2amZRQLBU1A0l2r2_cErVA1uygN15UTl1vY6YfNYES_QpCLllypuB3pmR2_2z0UgI7Im5jOMf1TCB1TIcMgHfScOsFg1p009MfQdZOmjf_ovh7YBAQNuvJPpQf4ZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد جدید بورس در مرز ۵ میلیون و ۹۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۲ هزار واحدی به ۵ میلیون و ۸۹۸ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681929" target="_blank">📅 12:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeNjQv60XlKuEcEGIFwShpSe2WdiwsK1aFyORnNMTNFAXxxiAqhBGX2zqD5juEDznXf-eNN8Lu7fvGVy0-ADv6RXEFb5Jfv803zs5ssCoiarfPNKET8rdRLE1xnx4X-ykwsshpWY1b9bI4Meij1mRHM2sbGbLqBfjU5Pu3POOXKLfJcYItv4NqatK_zgvwBa29On28aU88WtjE7ZideNekyTdLuXsZ5zClu1ZE4ipPz08ohhHkM8vp02_wfv8by4BvbUQQF3K-11WxWa9SNLzFzXfkBAPFhf8Zux4PXhsvaAtU1ZNYHpCsrcw1OK3rv5OKfLulTAb7oopImmRnwEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراحل ثبت شکایت در خطاهای پزشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681928" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین به ترامپ جنایتکار؛ مستقیم از فاکس‌نیوز
🔹
نماینده دموکرات ایالت ماساچوست و نظامی سابق تفنگداران دریایی آمریکا، در گفتگویی با فاکس‌نیوز حمله‌ای تند به ترامپ به دلیل عملکرد دولت او در جنگ با ایران داشت.
🔹
ترامپ فاکس را تماشا می‌کند، بنابراین اینجا مستقیماً به او می‌گویم: آقای ترامپ، تو تنها رئیس‌جمهور تاریخ آمریکا هستی که یک جنگ را خودت آغاز کردی و خودت هم باختی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681927" target="_blank">📅 12:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681926" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی MSI؛ گران‌ترین کارت گرافیک RTX ۵۰۹۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681925" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7885178bb9.mp4?token=T4KozM7gTj4lJv6d8sHz6MmCso45dU4rmDeILVwe3eZTqyYfTl1YoMe5XToaaiFej7qfz6dpgQJvsCub3y8x0uaycQ3-kE3L8JM35ZmwhcXLP-ZslT3iFKmS0GPoXkul_1dyvktZlCU78LtW33F0FBftnbb3KgCClfZwoasuUnEMqMgd5IY-4vnMxTeSL2WUda2XbmdOJiUwDD55D7oQm1EXLGSWgb4qC_VNNq_VpZg0G8Akr_HZIJZzNllOhrZHOwLwruqsljPM6jIIlAHGuExTEEeX0tpk1GyDBtH7awWRBzq70-qpvmwwQLKjmAXgTMUApivQyYmdcYQ0F_iYWYoiwyF08lACPEBiKFE1OHr7rwTT-YKPkqmwEBGIUckkI-ipD4VBZmC4jjSNtUtU2V5HtAjpy4mSh9yB7mWH8iwkoisJGPN1_RskGX9cijfS4IIlBvaE3nHX9xWsuf8z4scEtH9MXGOGpgGz_96avxN-XWgMVXWmZ53zUvtszvjmj1h3ymglSJMbGlh1OdSMzaUc9YTrD3mrsiOy__10TOkTLlr_gHUxrwkjDIhoNr42E8NwcMQSu4mXllvcc8c0IisSyUP_pdh0vF8S-tg2x8EVpcxLSpP5vMDZp38W3TiiaseUzrcxt_BFxawNdLAKv5j7r6UsdCwcpUUNUU2S2bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7885178bb9.mp4?token=T4KozM7gTj4lJv6d8sHz6MmCso45dU4rmDeILVwe3eZTqyYfTl1YoMe5XToaaiFej7qfz6dpgQJvsCub3y8x0uaycQ3-kE3L8JM35ZmwhcXLP-ZslT3iFKmS0GPoXkul_1dyvktZlCU78LtW33F0FBftnbb3KgCClfZwoasuUnEMqMgd5IY-4vnMxTeSL2WUda2XbmdOJiUwDD55D7oQm1EXLGSWgb4qC_VNNq_VpZg0G8Akr_HZIJZzNllOhrZHOwLwruqsljPM6jIIlAHGuExTEEeX0tpk1GyDBtH7awWRBzq70-qpvmwwQLKjmAXgTMUApivQyYmdcYQ0F_iYWYoiwyF08lACPEBiKFE1OHr7rwTT-YKPkqmwEBGIUckkI-ipD4VBZmC4jjSNtUtU2V5HtAjpy4mSh9yB7mWH8iwkoisJGPN1_RskGX9cijfS4IIlBvaE3nHX9xWsuf8z4scEtH9MXGOGpgGz_96avxN-XWgMVXWmZ53zUvtszvjmj1h3ymglSJMbGlh1OdSMzaUc9YTrD3mrsiOy__10TOkTLlr_gHUxrwkjDIhoNr42E8NwcMQSu4mXllvcc8c0IisSyUP_pdh0vF8S-tg2x8EVpcxLSpP5vMDZp38W3TiiaseUzrcxt_BFxawNdLAKv5j7r6UsdCwcpUUNUU2S2bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: خسارت هایی که به محیط زیست و دریای عمان وارد شده مربوط به دوره اخیر نبوده است بلکه به دلیل حضور نظامی ۵ دهه گذشته بوده است
🔹
بقائی: آسیب زیست محیطی فقط متوجه به ایران نیست بلکه همه کشورهای همسایه جنوبی ما را درگیر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681924" target="_blank">📅 12:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681923" target="_blank">📅 12:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیمه گمشده واقعا وجود داره؟  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/681922" target="_blank">📅 12:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm3sAKeXz7lYEUpouhRTSP9yHXgLcdrnAyEYhj4bZ-FiA6wI_9ApoFAPvr3bBLTgbynuQDlpwUtcMN5LoxgBa0Wux1rfNKfXlCNvDX8YnK_m1JfiRz9sjQVx5Ut93E8CW7bALjkCoVjieu29CYS1l7uS-N8RsSvNWH-VQCfr-a7SgSsDz5g4kDLqBKalxcbfowwv68p9NaS_CfeA_GyXvASouZgzN6lBA-Kfx2TpvjSRYHx6s__H82abbIa3F4YjyAM0AOVrGbPsbvQx4GcazShp7pVVqi2THeB6fcsJwY6iGC2JPGDrAaxgw3z-dOZWhx5E3X2fzrixh77N3pGmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
کلینیک ایران نوین قدیمی‌ترین و بزرگ‌ترین مرکز کاشت مو
کاشت مو (Nanograft) با ۵۰٪ تخفیف جشنواره تابستان
💰
قیمت نهایی: از ۳۷.۵ تا ۴۷.۵ میلیون تومان (متناسب با وسط طاسی)
شرایط پرداخت:
۱۲.۵ میلیون پیش‌پرداخت + ۵ قسط ۵ میلیونی (اقساط بدون سود)
⚠️
ظرفیت این جشنواره بسیار محدود است!
اینجا کلیک کن
👇
@clinic_irannovin</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/681921" target="_blank">📅 12:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شگفت‌انگیز پرواز کفشدوزک؛ تصویری جذاب از دنیای حشرات
🐞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681920" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdcloPhs4OEN5OuQMXkqxV94pK3Z_QrOkvS9H040qfb12X83vcETs5In2GzCgmApGiO2t46_JJBdbaTPIvR4srSuKgKHn1ySMffl_aposZ0iEFklsIPeL0YfIuFPuZJompf8VlYcCRpsMKA6qm1xj2f3zGLB2mSX2gDb5hVfQT3tn94qCIz_xc_qZv_yZl1ZC7cbc8m5uOTm_yRBHhz7TMxrBy4q4spIcIMj28Jm10fRJid_zGKNxxE4LjNs7xbOsfI4DQ5WMJSnc_-JpBxiusgBZK9LcVtcDUsDOKfZeWEXRRoJXyQiDlWWRtXe5K-fN_KBaugwLFJK9v7JLmLjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: توقف مذاکرات با ایران، تردد در هرمز را به‌شدت کاهش داد و ریسک نفت را بالا برد
🔹
رویترز گزارش داد با متوقف ماندن مذاکرات ایران و آمریکا، عبور کشتی‌های تجاری از تنگه هرمز به‌شدت افت کرده؛ به‌طوری‌ که طبق داده‌های کپلر، شنبه فقط ۵ کشتی کالایی عبور کرده و یکشنبه هیچ عبوری ثبت نشده است.
🔹
این رسانه افزود تهران بازگشت عادی کشتیرانی را به تحقق شروط خود از سوی واشنگتن گره زده و همین مسئله دوباره «ریسک ژئوپلیتیکی» را به بازار نفت برگردانده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/681919" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/681916" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
واکنش ایران به تهدید آمریکا برای تحریم‌های جدید   بقایی:
🔹
از مدتها قبل ارزیابی‌هایی داشتیم پیش‌بینی‌های لازم در خصوص اقدامات آمریکا انجام شده و ایران از تمام ظرفیت‌های خود برای ناکام گذاشتن شرارت‌های جدید استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/681915" target="_blank">📅 11:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmi3eAmRAbhqsanypqnj8sowvqQSUt3MY7Ze13Kx34dtYVJjwGsSasKQjbJriKjx31DoGHqHtOyRncw7cTgky-yH3hcb1Ovs_9jjFFsXFUWzwDq7Mc-aGaMVMAzVnhj6-plGRaR1cVkES8iY0DRJetMleajNt-nRQxcE42vtVxZn6Ar46v5g95errN57jcAWYptdAnBAyVjz6coSvr-7v8ZNqygxZUlQkpt8GzZIhILlO9nKcv12XHcBspnL5f79D7w164hnpC34vhCoodUJsrFVFt4Y8lz53Ho0w2kSeyTpmYix_os5qAYQOY4gwwe901xiAAig5RLL-izDRUPZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/681914" target="_blank">📅 11:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681912">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33947fa495.mp4?token=UUW5s3uqoe7BI4s23hLIFvBhRE-wl0hndfTrD0Jqvc1rURxrUWibl_1trHmkS7mqpmUzh_utzbkx8jFRlfZ7qpYVT4mKFYQ4bjN_VL1_Cg8vKyTzfk6wQqzReLgrJe-HUflN5LCVTTYY0aukZuO56h-2pmcZzd50KvFiljV34Z5-OAkUvGsvPRFCHQSHnYywnaBFbV2qWBu0FB7UiH7rYMlST8FBbGL4hXYRUVGklaNKRU5kqLHtttbPBogKIndAkBnPhHgXZs4Cx4sPpQeFVZb-TyUaV6RqF0kbQZ0Nn9t9CJDmB2NUTd5tPkuoIZmTvBTtr4cI-0ofryb0vx5G_nkrihVuRKCNZ-CiieRIoPAMv6XrihBNzgFnWR3V8ThoVltzUjXnNV1C1HKblsIPyE2XRkBolHHr488thdjFnba065eBPl1s4DuQleWkE03l7e_cKkD_L_Z7HGlemcfsOhY08SuhCSKi1FherhPmXdMWBqjCGb7kaGhJWoIG6xtef9RaRtG9sn5lUA6uVWKfzCphQ8v9Pe19Op4YAkR-5P_69wExICEi63-OloEGeTAKV6S_uVbVa-eO8KHRq0kuPQWb9ntt7oRF0jLl68xTXGM7DzqJQrm0Wl4lCsPcwhHufXDhkj4yqOoisz2rRl6KX0OArcnNFhmIsOqVAI2HkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33947fa495.mp4?token=UUW5s3uqoe7BI4s23hLIFvBhRE-wl0hndfTrD0Jqvc1rURxrUWibl_1trHmkS7mqpmUzh_utzbkx8jFRlfZ7qpYVT4mKFYQ4bjN_VL1_Cg8vKyTzfk6wQqzReLgrJe-HUflN5LCVTTYY0aukZuO56h-2pmcZzd50KvFiljV34Z5-OAkUvGsvPRFCHQSHnYywnaBFbV2qWBu0FB7UiH7rYMlST8FBbGL4hXYRUVGklaNKRU5kqLHtttbPBogKIndAkBnPhHgXZs4Cx4sPpQeFVZb-TyUaV6RqF0kbQZ0Nn9t9CJDmB2NUTd5tPkuoIZmTvBTtr4cI-0ofryb0vx5G_nkrihVuRKCNZ-CiieRIoPAMv6XrihBNzgFnWR3V8ThoVltzUjXnNV1C1HKblsIPyE2XRkBolHHr488thdjFnba065eBPl1s4DuQleWkE03l7e_cKkD_L_Z7HGlemcfsOhY08SuhCSKi1FherhPmXdMWBqjCGb7kaGhJWoIG6xtef9RaRtG9sn5lUA6uVWKfzCphQ8v9Pe19Op4YAkR-5P_69wExICEi63-OloEGeTAKV6S_uVbVa-eO8KHRq0kuPQWb9ntt7oRF0jLl68xTXGM7DzqJQrm0Wl4lCsPcwhHufXDhkj4yqOoisz2rRl6KX0OArcnNFhmIsOqVAI2HkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ناوشکن موشک‌انداز آمریکا منطقه را ترک کرد
🔹
ناوشکن موشک‌انداز یو‌اس‌اس مک‌فال دریای عرب را به مقصد پایگاه دریایی نورفولک ترک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681912" target="_blank">📅 11:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSm2uZanxW2Tg81W7UuJX7fReHcLR2ukPnw2NnD_zr6w_QlNNkulOc1hbrVAOBBM0qK6UpfyMOtemoeSUIJoujzDbB2DzNenRoOyKYodGNRbj6w-Ik1OnhIckcSdKXgz1GMDAn25MEh0UsUSxLmIzxmBqcvRW5tgbz6pelocUa8HKcPlQs45BgjC4lAyc_JxsAPQ3CZoN3YLYykZtNOdvLH9N99b7p9jlkf_kL1T4M20YwER_k5ExXQpkkTCzQnRltu3j5G0zngwXcF1IpbN15Nk2_lAAEUIQrvkznK3X6xbbi2dTK3EIAmcnP1EboSx35QxgR4O-6V_Ry5r2UhwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارسیان ورق را برگرداند/ اعداد ۱۴۰۵ چه می‌گویند؟
🔹
آخرین صورت‌های مالی بانک پارسیان نشان می‌دهد در شرایطی که درآمد تسهیلات ۸۸ درصد، درآمد عملیاتی ۸۳ درصد و سود خالص بیش از ۳۷ برابر شده و همزمان سود ناخالص بانک نیز از زیان به سود رسیده و منابع سپرده‌ای، سود انباشته و حقوق مالکانه نیز افزایش یافته‌اند، یعنی شاهد تداوم تغییر مسیر در درآمدزایی و سودآوری بانک پارسیان در سال ۱۴۰۵ هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681911" target="_blank">📅 11:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681910" target="_blank">📅 11:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681907">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168b84c809.mp4?token=Q2YRmiinE2KH9V4qTejvSH5zUQQ_SxX6MJqwl0tDiVcqmjDIWAh9RMfqbuiDMODwpNjHNGRvhwcHyEtWlcanFKlVtFMcc-TsI92tJ8culz4nwmqMQO6tKejHTRBO3rO-Fgr7aIEwwYAqtx-3wvEbd0P-ADAsWEdyXaYKSb8xY6Fnm3ZOxlmtFwASLW3I4Sz2b4vQArNoRREtDSmeoS20ZXa6GxyW5OYgUtvwIp32HYkyP1ZlE7Kfd5XttvrPtn-HnuycYG0vqZDKrrqGJ4v7gd2OQLtW36fy-tMJ1jDZnUYVvTgwZ6c-Kuz5-yoZW8Vp7eY7NjkBK6gnRDUD04xf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168b84c809.mp4?token=Q2YRmiinE2KH9V4qTejvSH5zUQQ_SxX6MJqwl0tDiVcqmjDIWAh9RMfqbuiDMODwpNjHNGRvhwcHyEtWlcanFKlVtFMcc-TsI92tJ8culz4nwmqMQO6tKejHTRBO3rO-Fgr7aIEwwYAqtx-3wvEbd0P-ADAsWEdyXaYKSb8xY6Fnm3ZOxlmtFwASLW3I4Sz2b4vQArNoRREtDSmeoS20ZXa6GxyW5OYgUtvwIp32HYkyP1ZlE7Kfd5XttvrPtn-HnuycYG0vqZDKrrqGJ4v7gd2OQLtW36fy-tMJ1jDZnUYVvTgwZ6c-Kuz5-yoZW8Vp7eY7NjkBK6gnRDUD04xf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش ایران به تهدید آمریکا برای تحریم‌های جدید
بقایی:
🔹
از مدتها قبل ارزیابی‌هایی داشتیم پیش‌بینی‌های لازم در خصوص اقدامات آمریکا انجام شده و ایران از تمام ظرفیت‌های خود برای ناکام گذاشتن شرارت‌های جدید استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681907" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681905">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشکان خطیبی: نمی‌دانم تا سه ماه آینده بتوانم اجاره خانه‌ام را بپردازم یا نه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681905" target="_blank">📅 11:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f63dfbc1.mp4?token=a_jmeclXayUcX-_I43PVF1ADT9vlVrneQ-LiAUTz4ygV86NFhRc4toUvzU3GT4jJ_vwvw3o0uXIdmIRdQwufJzqPlNFcWRhRVniOrY5aSi8MyQtaFwmk04i5AGrIqONh-LoeeLgNuweozfiHDk7I8eefKKut42fkC2uk75zMiAWU7igV3UX3Do1X4Mr0Hz-zKMlvAL239RTgDnt6JS2VSY5-rmmcXpsJAaN6bR_Nmx2SBLR8w3kkGYeh8PtKMQ8jqU_RUNKOkFnGd3GzMiQ_9F-k-xRqDNSppw_6D4q8WdXfupHvhekKsBj-kGpmaHrNxfiIyDFHRfS-aYMxkeIYPRyOkxwoLclEq2zaFfIeJalKjT66iPUSAVDk4OFEP24kr3wYWRyIM9Euvk5OWRReVBFnGYB7TJJrSoR1fv-HhZwUIM4n5Nn1FKBoMs8qV6sxTxLlTH-DTJImsVDIaHtT95nbM3urffQNL5hpUE5sshWlG_s0fp8GoSrq4y-p_E0pfq6-XIH5A8qL6PWxUJCPU2nOp8c1AotHDU71dk1wtFchanuRzDE6vERMbcM7PFSljcdlgWf221P07gKA_EuLHR-lVMoyp9kSFLBPUbfoqrOcmZBmyh_2yWgQQYekJz97sJ3ky1ADm98xx3MCiSXskZG5Jva44ivhsrqGB0IUmH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f63dfbc1.mp4?token=a_jmeclXayUcX-_I43PVF1ADT9vlVrneQ-LiAUTz4ygV86NFhRc4toUvzU3GT4jJ_vwvw3o0uXIdmIRdQwufJzqPlNFcWRhRVniOrY5aSi8MyQtaFwmk04i5AGrIqONh-LoeeLgNuweozfiHDk7I8eefKKut42fkC2uk75zMiAWU7igV3UX3Do1X4Mr0Hz-zKMlvAL239RTgDnt6JS2VSY5-rmmcXpsJAaN6bR_Nmx2SBLR8w3kkGYeh8PtKMQ8jqU_RUNKOkFnGd3GzMiQ_9F-k-xRqDNSppw_6D4q8WdXfupHvhekKsBj-kGpmaHrNxfiIyDFHRfS-aYMxkeIYPRyOkxwoLclEq2zaFfIeJalKjT66iPUSAVDk4OFEP24kr3wYWRyIM9Euvk5OWRReVBFnGYB7TJJrSoR1fv-HhZwUIM4n5Nn1FKBoMs8qV6sxTxLlTH-DTJImsVDIaHtT95nbM3urffQNL5hpUE5sshWlG_s0fp8GoSrq4y-p_E0pfq6-XIH5A8qL6PWxUJCPU2nOp8c1AotHDU71dk1wtFchanuRzDE6vERMbcM7PFSljcdlgWf221P07gKA_EuLHR-lVMoyp9kSFLBPUbfoqrOcmZBmyh_2yWgQQYekJz97sJ3ky1ADm98xx3MCiSXskZG5Jva44ivhsrqGB0IUmH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا توافق ایران و عمان درباره تنگه هرمز طولانی شده است؟
🔹
قرار بود تفاهم خرداد شروعی برای کاهش تنش باشد که آمریکا با پیمان‌شکنی جلوی آن را گرفت. گفت‌وگوها با عمان برای رسیدن به بیانیهٔ مشترک دربارهٔ سازوکار ادارهٔ تنگهٔ هرمز ادامه دارد.
🔹
نامه‌ای با منشاء وزارت امور خارجه خطاب به مجلس برای مسکوت گذاشتن طرح اعمال مدیریت ایران بر تنگه هرمز وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/681904" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a987f247.mp4?token=ezI1QT2AOm5uuDjMte3u8zuvA-cAxMriov0tuxd1lHG6OtC0IL104lpOtoIvhjLs5OQJ6TDvFHk13pu8_UDKqSdzA1n8FXYstAUUU4sdMGzocJQRLdbwmRyguqB283Q6lboSs_tMSOUMu_ULrxU7OtFflCzoKxUmPbHn0bEeEy3zI22Inq9bC7bORi5hi7CY--drLTZO3jYKpugFbj4Ap8kP0YQj2sSa61fZDThqEjPnA2ysBF_Rug5y_ox0G7JY02B_o835K2uEkU3thtAO8zCZyb_cVu4YscirjDv_9_jmen9q2UG8_8M6Y19Ycc7rLAObzUYYxyZEOo3VsO9RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a987f247.mp4?token=ezI1QT2AOm5uuDjMte3u8zuvA-cAxMriov0tuxd1lHG6OtC0IL104lpOtoIvhjLs5OQJ6TDvFHk13pu8_UDKqSdzA1n8FXYstAUUU4sdMGzocJQRLdbwmRyguqB283Q6lboSs_tMSOUMu_ULrxU7OtFflCzoKxUmPbHn0bEeEy3zI22Inq9bC7bORi5hi7CY--drLTZO3jYKpugFbj4Ap8kP0YQj2sSa61fZDThqEjPnA2ysBF_Rug5y_ox0G7JY02B_o835K2uEkU3thtAO8zCZyb_cVu4YscirjDv_9_jmen9q2UG8_8M6Y19Ycc7rLAObzUYYxyZEOo3VsO9RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: میانجی موضوعات ایران و آمریکا، پاکستان و قطر هستند
🔹
ما میانجی جدیدی میان مذاکرات با آمریکا نداریم.
🔹
دیدار مخفی بین آمریکا و ایران در اربیل عراق انجام نشده است و این خبر ساختگی است/ تیم مذاکره‌کننده مورد تایید همه ارکان نظام علی‌الخصوص بخش دفاعی کشور است
🔹
نقشه مسیر تردد دریایی با عمان با جدیت در حال تدوین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/681903" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivSbWcdT-gTylUljp1xHcZloIy04RpxynxP6fPGjUB4_Z485zkYAgEaPNNwjUnx7jZHitnVjvbHa0NdHgHvGwK6qPoVvm1L0RyeJSq704QQQ7HMhMSMwPDJtF83bfMn-2se-sWcZxC8ppyTv0McnXBuWvP5XcZx4R_rfMA6Klu2aATZq_6y-E_GH1BKyB41xK7m1g2Tu1hkM_hq55qE9S34FDbO1i2RZc7eceWexh6ug-N-26Op3Xn8EyrrvwyxjY8udvRWYqmZveqkyvcXHkHpk6fqEvsX5gN2PItMZHt2pkmLv5K3TTroMoI0QmVe9cVn84jihzjSataIag7aAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681902" target="_blank">📅 11:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681897">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وجود هرگونه مهلت ۶۰ روزه در تفاهم‌نامه را رد ‌می‌کند
/
نقض فاحش تفاهم‌نامه از سوی آمریکا گفتگوها را متوقف کرد
🔹
ایران حقوق حاکمیتی خود در خلیج‌فارس را با جدیت پیگیری می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681897" target="_blank">📅 11:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند
سخنگوی وزارت امور خارجه:
🔹
از روز اول که مطلع وضعیت خلبانان شدیم پیگیر آنها هستیم. ۲۵ اسفند اولین مکاتبه با صلیب سرخ در خصوص پیگیری خلبانان را انجام دادیم
🔹
مطالبه روشن کردن وضعیت خلبانان ایرانی بسیار جدی است. مادامی که وضعیت سه خلبان ما روشن نشده، به معنای این است که به اسارت درآمده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681895" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaxDGG-OG4NA17uUWBJSmzkkLuDQu1TC3053Hjqi8PqIHJxFROFl2-pe3qMfv7i7p7BLNOlD_6wX18W2xHINS9hpZHXDhuIQQZS9qW61cQHVtpJAbBUVwNBw8wjHNDYangzkdv5iaM8lYOWmDUcwDGio2OBKkPBcTjGSwKZkdO7xgDfgJdXQ1lu_xZmfnkSt0yhH9Rftw9SPw3XBHLGLU1vErdffFuWLyZG1JMzwaMGnqC0okH2MD4C2ZKeTF2AZ3gAnySc0_dxl02aQQ80ucWtdA4fJM75CUDeHfv2wbH-mE-i-e7RoUGxRG2DLDIwOlsBgzYnGFVlMT3yTAUHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/fast/37832/180124/</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681894" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تصاویری از بقایای جنگنده اف۱۵ و پهپادهای منهدم شده آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681893" target="_blank">📅 10:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbS3lri4guEmNg8Ki7BFvWreUtGryf8cHnHNc_85VIoO7eSdGenaMsg5VahaLFu__CQdwMJh50o7vmlPZdPHy8iWATTz04kca20LS9jDwkblHv2zR8_tQGUg5PEm-Ix7ECCmdemuNNEK9axGAp_JpX9pSaNPckH1qBbS4muvDTi6zXreKo-Dh0GzdSY4-kNjWBqU11a3DhY8_42B8d96zcraTte25qAFqeJSZU3Mu_oT6420fOqKbkt0a1rbsR8LSO565NzPQldBcwrCk1hOyyqoaxWbUtHGszzDwQXJA7n-HikVKqVJeT3bVno9YEAIe0IRRqOPtCONgN2yX8EDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و رژیم صهیونیستی در جنگ شناختی، به دنبال ایجاد «ناامیدی» و «درماندگی» با تزریق اخبار منفی، بزرگ‌نمایی مشکلات و القای این حس که «هیچ راه حلی وجود ندارد» هستند. در برابر این ماجرا دو راهکار فوق گره‌گشاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681890" target="_blank">📅 10:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=oUBFKdMjvqD40wNbbGkwrd6Q-2YF7Sqa4jElZ0uEoB4mPNMxUfjqZ0E8jqgeXCuVpv1efFofBPeTGlDi45NB9vTb2ErFmBNPFowMPrfiPSOmb9wMITraIJgbSN1dj24EM6nG560Y79OuvwzsMjTNJ5jIq0RYauo9NQG5RLjZowZSuxl4HjjD3q403kpnq12PUk-SJunfoyPwc-l_gbwLx8omoVv1yGikE54S8nT3K97nkC4HwqqQTJZ4mqTiwP4ZoZlw-dYEA-Tcinq2beYsi4KHpsjwL07-MewVRxlJ131kqaHFk5P7UFNWYv78qvVFR1C6nC7SqDxBxwCV0uOAF0ke10BGe4_Dgn42tcDAIIX6ucYy0M2TxfrF0htcD8ME5VTM3gebSBkmYatlyJFr8Q41IxRbwY46NWoEvhClrkVTs73VqpOpeRkcFtEpcXbVJwAb3vYqgcsL4X33nTb5QznCQpFvNPQLEDfNcK07iOQ5Mey0oSAytWhbAled6dVADLtzAyuiBKFphdD5_hDtImVDiD2xVOX-NRvMREF6HtB3paGyOSHHbq0SXqNVqgPJFqoSrbTOz9opKDSd6I5dVascFdKJKQBGr2I5kDt13QOrXbxSJD3TNkS_d3e-n01qCeClAYs56VKG0Mc6SlCwZOwKSY86ZtLzQsaPt-SeFuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=oUBFKdMjvqD40wNbbGkwrd6Q-2YF7Sqa4jElZ0uEoB4mPNMxUfjqZ0E8jqgeXCuVpv1efFofBPeTGlDi45NB9vTb2ErFmBNPFowMPrfiPSOmb9wMITraIJgbSN1dj24EM6nG560Y79OuvwzsMjTNJ5jIq0RYauo9NQG5RLjZowZSuxl4HjjD3q403kpnq12PUk-SJunfoyPwc-l_gbwLx8omoVv1yGikE54S8nT3K97nkC4HwqqQTJZ4mqTiwP4ZoZlw-dYEA-Tcinq2beYsi4KHpsjwL07-MewVRxlJ131kqaHFk5P7UFNWYv78qvVFR1C6nC7SqDxBxwCV0uOAF0ke10BGe4_Dgn42tcDAIIX6ucYy0M2TxfrF0htcD8ME5VTM3gebSBkmYatlyJFr8Q41IxRbwY46NWoEvhClrkVTs73VqpOpeRkcFtEpcXbVJwAb3vYqgcsL4X33nTb5QznCQpFvNPQLEDfNcK07iOQ5Mey0oSAytWhbAled6dVADLtzAyuiBKFphdD5_hDtImVDiD2xVOX-NRvMREF6HtB3paGyOSHHbq0SXqNVqgPJFqoSrbTOz9opKDSd6I5dVascFdKJKQBGr2I5kDt13QOrXbxSJD3TNkS_d3e-n01qCeClAYs56VKG0Mc6SlCwZOwKSY86ZtLzQsaPt-SeFuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است
🔹
مرغ سال گذشته ۱۴۰ هزار تومان بود الان بیش از ۳۷۰ هزار تومان است که دلایل خود را دارد.
🔹
جنگ روی افزایش قیمت‌ها تاثیر گذاشته و قیمت‌های جهانی ۱۰ تا ۲۰ درصد افزایش پیدا کرده و کرایه‌های حمل بین‌المللی ۱۲۰ تا ۲۰۰ درصد افزایش پیدا کرده است.
🔹
نان پرمصرف‌ترین ماده غذایی در کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681889" target="_blank">📅 10:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681886">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41942480a7.mp4?token=gwmWNWKt4CZalXsg8fhHVOjzfj-iuzwJTybdgFMzvAay0GvULhzotWQytEPdgfDTlcnxp8FGeujhzygJjwkOgqwXgvMRlE9LlaGQ6NvDPGk1tZfFtYAdZfV5spD9tHyu5dM65vIBhmKA6zDhyEwO91FJZbn47-YyEwwynKbPGYkltvrd76CZQLoXG9u8aQVcoTa4_9c2ePnvm8FH4gNxCOusuuOdok2lWT8rKPrOU4XoxRo1uV5eZ3aRW-f9ad5WYRWnDRZ74NjbGAphaCBv0sVokP2SUoaEDF2SePIFpe0x1HABpyM94-A1ioyScilecxhDOWUhm_2bx5sjzNBhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41942480a7.mp4?token=gwmWNWKt4CZalXsg8fhHVOjzfj-iuzwJTybdgFMzvAay0GvULhzotWQytEPdgfDTlcnxp8FGeujhzygJjwkOgqwXgvMRlE9LlaGQ6NvDPGk1tZfFtYAdZfV5spD9tHyu5dM65vIBhmKA6zDhyEwO91FJZbn47-YyEwwynKbPGYkltvrd76CZQLoXG9u8aQVcoTa4_9c2ePnvm8FH4gNxCOusuuOdok2lWT8rKPrOU4XoxRo1uV5eZ3aRW-f9ad5WYRWnDRZ74NjbGAphaCBv0sVokP2SUoaEDF2SePIFpe0x1HABpyM94-A1ioyScilecxhDOWUhm_2bx5sjzNBhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«سردار جوانی» معاون سیاسی سپاه: تنگه هرمز زمانی باز می‌شود که آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد عمل کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681886" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681885">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من چطوری می‌تونم پرچم وطنم رو پاره کنم؟!
🔹
۲۶ مرداد، سالروز درگذشت عزت‌الله انتظامی. او از حاجی واشنگتن و سکانسی می‌گوید که باید به پرچم ایران بی‌حرمتی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/681885" target="_blank">📅 10:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصلش تموم نشده حتما این دسر لایه‌ای‌ انبه رو درست کنید که خیلی خوشمزست
🥭
مواد لازم:
🔹
انبه دو عدد
🔹
خامه صبحانه: ۳۰۰ گرم (یک پاکت و نصف)
🔹
پنیر ۱۵۰ گرم
🔹
بیسکوییت پتی بور دو بسته
🔹
پودر قند ۶ قاشق غذا خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/681882" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZm7XL63E8xsTMFRG705eRnD7VE4E1Pa053x-NkB2qErlWalSLuG5vkdJ1Qz_Arc0dmCa2yGDvb9hMo7LvB-2Z4Uz5ZFErcQK8OHD-bBZQ7AjwF2rpZTuiGkGDUZwbpgoyQsifzojH3ioBecdHN74tsZHMjjUi7DbFQZSyrYo8vGPOWsG3j6nGZDuVPMr93N2RVc-VPQaIWeI1GfWxplW5xQ0s0Ffkq8MuVbcvBqrHT4DVv3tM5WdBjn8Du2qyD2SFmeAq_vCWBCB0hLzMqZPWmtaBQ5ERY5bkoJTft-Szv9BM3l6QMplY-ROgN6LkReARt4telbE5kSIh391sZznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه در حال ایجاد پایگاه‌های پهپادی مخفی در نزدیکی خاک ناتو است
ادعای تلگراف:
🔹
روسیه حداقل ۱۰ پایگاه جدید پهپادی با ۵۹ ریل پرتاب در مرز بلاروس و اوکراین ساخته است
🔹
پهپادهای دوربرد پیشرفته، قابلیت رسیدن به لهستان را دارند، نگرانی از تهدید زیرساخت‌های ناتو در درگیری‌های آینده./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/681881" target="_blank">📅 09:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
وزیر جهادکشاورزی: به خاطر محاصره دریایی، جنگ با شدت ادامه دارد
🔹
در امنیت غذایی کشور و موجودی کالاها مشکلی نداریم؛ اما قبول دارم به خاطر جنگ و محاصره دریایی هزینه‌ها بالا رفته است
🔹
دولت طی دو سال گذشته هیچ روز آرامی نداشته و هر لحظه درگیر یک حادثه بوده است/ از همه چالش‌ها عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/681880" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681876" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqlrsmm46evoSyyirpmgDme5mJ8h6u-oUBeWCytJTduWmoxa7H9Bgtm1HAinALtyPE3KwmayU1z95eLDOA0d257sv3qr0A8SLp2YyvHvJaHTXzyCrqddgu4yan-LTocGdozzgXFYN1CydtWCiFT280HcSjAQlJZ1LZZmVL6DHEMCP4GhP4ukEkJ2qz9DdGUsWTm5b0Un9vzTemQCHZc2EvuY8RFeJ_a_mPQTxmQDl6cbYjAmvzism5EkUzgaDp1HfLg8aFnRaIut5DdnjhmPiu6eJPp5g-FWgGp_1Ta-0DT35aHTrxQeel7LItYnW59lnT47qEi4LJAFFY7PmpP1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت با انقضای تفاهم اسلام‌آباد گران شد؛ هر بشکه برنت ۸۹.۴۰ دلار
🔹
توقف تردد در تنگه هرمز و بن‌بست مذاکرات، قیمت را بالا برد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681875" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaYcH-7AjisJUHn6mLTVupuFO7taZLDoQmwlJH0t0ilON6zBHtroxnH7UR9IZSLSDC__L3U86amtq8PVRRh-w8Aoio9TsCDlWGXpXibmvUH8anXE43lbzvxKDiUtWPh1fQRDGXL2UWSuXVw8lVmqnwsEqIpgKblvSV3rbQA0qRgzgm4mZW2I4GxsgSGDKTBiMWC4N-3vXlnN2oLaYYrp4J6WsZu9Ogot-xPkfUIJWn39j7Go38TsyAkOgqLizkHJhvnyMfJQkrmBbP8XKPjOgUKGFWIGxbzk9DFB5D2K-_lZwkS5bC59iEOl-uCXNvcvUVQH4UBmKvvnegzuTkF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681872" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH37QUxeXoCk5V4iFGjiXkS9VnxeYgAjswyBpZYsQA4VB95APxQPPFYvkpUs0A5CWnRnb9K4Wxyv0HYak4r1m976bbkBT2s26tfAqC1TH_I_JvhesPgivMvEbstXnivRxFyfxmCx_jgBY3G2ijIK4Zg2sd3hPbnvVD3CzFAW8XgNwL9z-RO5roLlJ1XvNGeXSG1gvzeJ-b5SuWp0d-z13JM29o0633I1ioIs2j-tc-aPb7UY6acx1a8Bu28l4Cv-FDGEfL3DqJUzBC8T5cGl2oo0TsD6_gMG3pJLkixtNDDQgsJyGX7apPoXvYVpnCGNtgPSoIobnLLqmomZL7183g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی المپیاد جغرافیای ایران اول جهان شد
🔹
برای نخستین بار در رقابت‌های جهانی؛ تیم ملی المپیاد جغرافیای ایران در بخش Poster جایگاه اول را کسب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/681871" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شمارش معکوس برای پایان آتش‌بس ایران و آمریکا/ جنگ به «جنگ اقتصادی» تبدیل شد
نیویورک تایمز به نقل از منابع آگاه:
🔹
مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
🔹
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681869" target="_blank">📅 08:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: هرمز باید بدون عوارض و هزینه قابل تردد باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/681868" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعمال قدرت ایران در بحرین!
کارشناسان آمریکایی:
🔹
حمله ایران به پایگاهی آمریکایی در بحرین به یکی از هاب‌های اصلی پشتیبانی و لجستیک ناو لینکلن آسیب زد و کار به جایی رسیده که برای مثال یک ملوان در پیامی به همسر خود گفته فشار شرایط دارد مرا از پا درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/681867" target="_blank">📅 08:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نقل قول دکتر لیلاز از شهید لاریجانی هم از جهت تشخیص و پیش‌بینی اوضاع هم تلاش نظام برای جلوگیری از جنگ بسیار حائز اهمیت است.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681866" target="_blank">📅 08:26 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
