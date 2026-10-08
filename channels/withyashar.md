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
<img src="https://cdn4.telesco.pe/file/hgceMWAT122iPwAdIOtCRGVtVs7losBDqiqgP5xPJ8YosinKnAHbZEbbnwvSZX8_4YP8CksmxwuM9arcAYgHRYdyqxsgtpJrMK6YNf81evqxdCNsmhfj-e4uXZnqHc8UNIFqy7hsOQgaAFAK79xmNIwWGSRVCBYDzwJdwB7e7xL3HQDItrN3w_cmqqApcpJ1BqhrWbaQ81yG6R2TtikLvQXYxK1t98y_iYf6UZdqTNKsu6TSOUi_OT3KjC6cRABUlIGluyMgza3pbe3TUX_MZIAFYl2swIiHVetGRCXXbRl5Ne8J1RZMez7Ha9Ki19YQCgH4GzrifqCSQsXKTHA3fQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله مسلحانه به مینی‌بوس حامل کارکنان نزاجا در بلوچستان
روابط عمومی لشکر ۸۸ زرهی نزاجا:
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، در محدوده شهرستان نیکشهر مورد حمله مسلحانه قرار گرفت.
متأسفانه در این درگیری یک نفر به نام «محمدرضا اوکاتی» به شهادت رسید و ۳ نفر مجروح شدند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/25167" target="_blank">📅 12:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=DoUf_NNhBQfKBRhT-SlF-Pr7kdx0ANyp70pXLE1HylSq-DC8fHT5BlzNKXl7HyEsHSTQxUtWbleup3cEtyGBYJfr0P2LBZPnyu7_-FTPEwad8USDHyueUIGtbeh2yjaC4FoCzLKq_0RS-YwnRX3bruhiw1xFLAQGbAAJmnfled9b1g39cQYa_myUDN1ypniigxLsWbNGDJUhaY-EG_ghVVlo1qzpghEbHFOgFuLD_VX3I3h-A87jW4VeViEvIUB-IOmOM3VJxrGZ9_M-__o_HuCOCL0bCcGvNfpPtsAjO_h5-suGeItNtH4gOzMBBY0vp-8QK1bQPlzaYemrb7AwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6614110b.mp4?token=DoUf_NNhBQfKBRhT-SlF-Pr7kdx0ANyp70pXLE1HylSq-DC8fHT5BlzNKXl7HyEsHSTQxUtWbleup3cEtyGBYJfr0P2LBZPnyu7_-FTPEwad8USDHyueUIGtbeh2yjaC4FoCzLKq_0RS-YwnRX3bruhiw1xFLAQGbAAJmnfled9b1g39cQYa_myUDN1ypniigxLsWbNGDJUhaY-EG_ghVVlo1qzpghEbHFOgFuLD_VX3I3h-A87jW4VeViEvIUB-IOmOM3VJxrGZ9_M-__o_HuCOCL0bCcGvNfpPtsAjO_h5-suGeItNtH4gOzMBBY0vp-8QK1bQPlzaYemrb7AwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : زنم بهم گفت یه لطفی بکن، کلمه vegan رو درست تلفظ کن!
‏من میگفتم “وِیگن”! از کجا باید بدونم چطوری تلفظ میشه؟! من استیک دوس دارم!”
@WarRoom
😂</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/25166" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز: ایران ماه گذشته ۲۰۰ میلیون دلار به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود ۵۰ هزار خانواده که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/25165" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز:
بیت‌کوین فقط امروز ۱.۳ درصد افت کرد و به حدود ۸۲٬۲۶۵ دلار رسید
و اتریوم نیز ۰.۸ درصد کاهش یافت. رشد دلار، بازده اوراق و قیمت نفت مهم‌ترین فشارهای کلان بر بازار رمزارزها هستند. حدود
۵۵۰ میلیون دلار معاملات اهرمی
در بازار کریپتو لیکویید شده که بخش عمده آن مربوط به معامله‌گرانی بوده که روی رشد قیمت شرط بسته بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/25164" target="_blank">📅 11:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اکسیوس: پنتاگون برای احتمال ازسرگیری عملیات گسترده علیه ایران آماده می‌شود
منابع آمریکایی و اسرائیلی می‌گویند در صورت آغاز عملیات، حملات می‌تواند تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران را دربر بگیرد. این موضوع پس از نشست چندساعته تیم امنیت ملی ترامپ در کمپ‌دیوید و تماس‌های اخیر او با نتانیاهو مطرح شده است. یک مقام پنتاگون به اکسیوس گفت:
«وظیفه این وزارتخانه، توسعه گزینه‌های نظامی و ارائه آنها به رئیس‌جمهور است.»
یک مقام کاخ سفید نیز گفت ترامپ در هر زمان همه گزینه‌ها را در اختیار دارد و آمریکا به‌دلیل کنترل تنگه هرمز و وضعیت اقتصادی ایران، در موقعیت قدرتمندی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25163" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
پنتاگون به
فرماندهی مرکزی آمریکا(سنتکام)
دستور داده است آماده‌سازی‌ها برای احتمال
ازسرگیری عملیات‌های گسترده نظامی علیه ایران
را تکمیل کند.
بر اساس این گزارش، حملات ممکن است
پیش از انتخابات اسرائیل و آمریکا
آغاز شوند؛ با این حال،
دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده
و
هیچ تاریخی نیز تعیین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25162" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبکه NBC به نقل از یک مقام آمریکایی، یک مقام خاورمیانه‌ای و یک مقام ایرانی گزارش داد که
ایران و آمریکا در ماه جاری میلادی در نیویورک، از طریق میانجی‌ها درباره برنامه هسته‌ای ایران گفت‌وگو کرده‌اند.
واشنگتن می‌گوید هر توافقی باید موضوع هسته‌ای ایران را نیز شامل شود و ایران میگوید خط قرمز است و اصلا
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25161" target="_blank">📅 10:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تنش جدید اسرائیل و بریتانیا
اسرائیل در واکنش به تحریم‌های بریتانیا علیه شهرک‌های اسرائیلی در کرانه باختری، دستور تعطیلی
کنسولگری بریتانیا در شرق اورشلیم
را صادر کرد. گیدئون ساعر، وزیر خارجه اسرائیل، این اقدام را واکنشی به سیاست‌های «خصمانه» بریتانیا دانست. اد میلیبند، وزیر خارجه بریتانیا، گفت لندن حق اسرائیل برای بستن کنسولگری را به رسمیت نمی‌شناسد و بر سابقه نزدیک به ۲۰۰ ساله این نمایندگی تأکید کرد. امروز تابلوهای کنسولگری پایین آورده شد، اما یک تیم محدود بریتانیایی همچنان اجازه فعالیت در ساختمان را دارد.
سفارت بریتانیا در تل‌آویو همچنان فعال است.
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25160" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: ایرانی‌ها آماده‌اند هر کاری را برای ما انجام دهند تا از آنچه در حال وقوع است جلوگیری کنند، با این حال، توافق با آنها واقعاً گزینه‌ای نیست که من ترجیح بدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25159" target="_blank">📅 10:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1LkfiNs_7v34w59Sp0mG88rAJT0QrDFyJX7uxEe0iTKWColD680i3U1FsuIvxWYY5cMGhM4ReAJztNijbptJa-iAZqacvKGQrF0krBNSmpU6y_3pwaEqlY2PEDhP0qwLW09E8-tPa7qLbrPVq3vK2VphanOy9f2i_U7-6zymGYyZcQCy4auq_14pVfRmZ6BeJEmUuf-XAL2Z0eaobw4cTQmWxosMRTZDb9rbpUjCQ0Psn2vzNld0OuCNOCQoUOG7W0chbJNybdQcuxC3B-3vdc4pw3lRnQo1JlqY0567vzQgRtd8uyRyRCUorSpj2tZkJwQa04AScUSyLvjgVkgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «انتقال نفت به سطح پیش از جنگ بازگشت!»
@WarRoom
حجم انتقال نفت خام از منطقه خلیج فارس :
قبل از مارس: جریان نفت در سطح میانگین و طبیعی خود (حدود ۲۴ تا ۲۵ میلیون بشکه در روز) قرار داشته است.
ماه مارس: با بسته شدن و انسداد تنگه هرمز در پی تنش‌ها و آغاز درگیری، حجم انتقال نفت افت چشمگیری پیدا کرده و به کمتر از ۱۰ میلیون بشکه در روز سقوط می‌کند.
ماه‌های بعد تا سپتامبر و اکتبر: جریان صادرات نفت به‌واسطه استفاده از خطوط لوله جایگزین زمینی، مسیرهای دوربرگردان و پشتیبانی ترانزیتی روندی صعودی به خود گرفته و مجدداً به سطح میانگین پیش از جنگ (تراز ۱۰۰ درصدی سال ۲۰۲۵) بازگشته است.
@WarRoom
یاشار: چنل های بی سواد همه اینو زدن قیمت نفت
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/25158" target="_blank">📅 10:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjwrKd-ufVq11Kg-fvLMI5zjFsT44DRHZDwcKtoHJ7Jc02XGrHk8g_XZmYmtvJ5PWqm63pcp0l2fTLocCwvWNHHNxE8y0mYvsHDNaEuFvs0Iaq4fzfeLzW-xof-sP28L1E6eLOM7IV7JkLVe-bdCjaskHMrCP9XdpyeemmVB98O9tl5SDryfs22n1pn_FTKOlrc-pAwo_vUyIr49t1bA-q0rpxBOpCYQhf2N1Olq_0h-kFZyk-KtDmO6DYDqME0MfwbugVNodqxDGv4oUfrijmkwep24oSMPEgyOojCmgSvBT-B67YvLW-7XTDyKhK3yIUckfK4s7fvDilEYKvG_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد … @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/25157" target="_blank">📅 10:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بندرعباس ۳۰ دقیقه‌ پیش صدای‌ انفجار‌ شدیدی‌ اومد …
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/25156" target="_blank">📅 10:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71094a656.mp4?token=l5pRLwZ7Cv8K8peru3cR-EIhGDKJg-Y_lTj1MpNZadPO-DyYAUV6_Xqy3T76gFvgveZ2K4FaiX8gzXt6jo90IYlAYHoJVx0E84_L0hqh3Ps0ptqVvLJwOKSSZravtn-w5zN3MxB47M8N9KfE2dw3x-Ju0WssHuSeOjvpzhroQfKMFIC5VeVdZbiyr2E8Ayn8aiPYFQsQDTl__lQrTzsUayoI-Gl_q17PnOI9CGGT0pFlLrBqKqTmP4VT8WxY2X1wRkm-HfVi_zTWEDdghiVRYzoTJ9vcaiKJwO8X_lUM8jh6D5BxTpZFC9KIyq5AMGii3md9B9_mJ1mn8VWw_5kGzhTP8rM8iBPzGkB7uWCeHgStDuHEd-WoGtNeWlNlgPG5oFrmZ0taExriTVPihhfL_cqapW9hBHsc0nBC9rruUcmsALhaqUur9wSHOyXSCo9ZqRIJxSTp23hrJNgCDb20wqUTpQCRJVwKU9g3R6ctiGEeT9qgdrtgd0SZu1CwHXS5Ac-DbFL4_GeFVMl3ZROQ3Cw-pmfsUcgjIrR43kJ4EO-Oh1Bu_BkOrrayXNXOjWhUUsZ_0U_c6D2wNWHACcrfw2HzTo8-hp_VUSM_AZMgeMONXTQ8-ebcRKZjCqcq8t4myjE936IQq5LWh4blo6dLd5ES38emKM_4hJwvIQoHoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71094a656.mp4?token=l5pRLwZ7Cv8K8peru3cR-EIhGDKJg-Y_lTj1MpNZadPO-DyYAUV6_Xqy3T76gFvgveZ2K4FaiX8gzXt6jo90IYlAYHoJVx0E84_L0hqh3Ps0ptqVvLJwOKSSZravtn-w5zN3MxB47M8N9KfE2dw3x-Ju0WssHuSeOjvpzhroQfKMFIC5VeVdZbiyr2E8Ayn8aiPYFQsQDTl__lQrTzsUayoI-Gl_q17PnOI9CGGT0pFlLrBqKqTmP4VT8WxY2X1wRkm-HfVi_zTWEDdghiVRYzoTJ9vcaiKJwO8X_lUM8jh6D5BxTpZFC9KIyq5AMGii3md9B9_mJ1mn8VWw_5kGzhTP8rM8iBPzGkB7uWCeHgStDuHEd-WoGtNeWlNlgPG5oFrmZ0taExriTVPihhfL_cqapW9hBHsc0nBC9rruUcmsALhaqUur9wSHOyXSCo9ZqRIJxSTp23hrJNgCDb20wqUTpQCRJVwKU9g3R6ctiGEeT9qgdrtgd0SZu1CwHXS5Ac-DbFL4_GeFVMl3ZROQ3Cw-pmfsUcgjIrR43kJ4EO-Oh1Bu_BkOrrayXNXOjWhUUsZ_0U_c6D2wNWHACcrfw2HzTo8-hp_VUSM_AZMgeMONXTQ8-ebcRKZjCqcq8t4myjE936IQq5LWh4blo6dLd5ES38emKM_4hJwvIQoHoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره ایران:
«همان‌طور که قول داده بودم، اطمینان حاصل می‌کنم که ایران هرگز به سلاح هسته‌ای دست پیدا نکند. آنها این را می‌دانند.
ما به‌زودی از آنجا خارج خواهیم شد و خواهید دید که قیمت نفت مثل سنگ سقوط خواهد کرد و قیمت همه‌چیز نیز پایین خواهد آمد.
این عملیات بزرگی بود که روسای‌جمهور قبلی باید طی سال‌های گذشته انجام می‌دادند. باید انجام می‌شد، اما هیچ‌کس حاضر نبود مسئولیت آن را بر عهده بگیرد. ما چاره‌ای نداشتیم، چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/25155" target="_blank">📅 09:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=XgR2KttOkxh6PlREEj2WOxp2rmTgYo6pHYC6dkXcE7AZ5xTeulk63vnSwQfdNQHqR7tliZep1O5KAqgl7WtSkp8ke3Sy8EMMd0aOA46mXBIHwFuXyal52wKDIKkCnDj0kDehcCvxx8bjzSNDfqYwxGko7DG2pWXpnADtBG2xOli1SvqhmOzs6vJ2c01s_aGBTTBdiNQH_rGXe-a06jeJwP88N1p8r_iA4U5KKMNjCKvppKHZoJk7euHui3j47eLlQD5ZpLECtUlXzuQupNvVxypcITxp3KU2iH9c6A3qvYWj1K1p9XJVqQuPBZmsNavS6zDqV9q1uUarUtOQw0Ce_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7d98ccb1.mp4?token=XgR2KttOkxh6PlREEj2WOxp2rmTgYo6pHYC6dkXcE7AZ5xTeulk63vnSwQfdNQHqR7tliZep1O5KAqgl7WtSkp8ke3Sy8EMMd0aOA46mXBIHwFuXyal52wKDIKkCnDj0kDehcCvxx8bjzSNDfqYwxGko7DG2pWXpnADtBG2xOli1SvqhmOzs6vJ2c01s_aGBTTBdiNQH_rGXe-a06jeJwP88N1p8r_iA4U5KKMNjCKvppKHZoJk7euHui3j47eLlQD5ZpLECtUlXzuQupNvVxypcITxp3KU2iH9c6A3qvYWj1K1p9XJVqQuPBZmsNavS6zDqV9q1uUarUtOQw0Ce_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : استیو ویتکاف در حال کار روی توافق با ایران است و عملکرد بسیار خوبی دارد
فکر می‌کنم این توافق واقعاً چیزی نیست که من بخواهم انجام دهم، اما آنها حاضرند هر چیزی به ما پیشنهاد دهند تا این درگیری متوقف شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25154" target="_blank">📅 09:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=FSlaDAweOdTLQ82ohnplQWO00HPS_RgoTZEggn3FxVpU0PnoNAL4FG2dUEeEKwdiVeIe1PalH77zQm8YurROjqbS42zsLdtEMU17xmwrGrel__R7xaMRN3DmHhZ8OV52VxzCnZbFT2wH0L3uC5GKvPW9R9_80Pptvum9HzUDwrhMUjBq9S90pAccavkcM4oHVLkQWVn4TBtRPahnzbLLz5h-8SfOy3V0kqaQ17JnBMc6692R2CTGnbi56Y64Kbki9tS9IFgnZDRKz5XzN15GkhWRG7qwafJKjTQg2QzSTAdNHjPOISNOp2CHlC3oq0eXdhzEwXUxvyc7hHdR5TDBMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfd30d3c3.mp4?token=FSlaDAweOdTLQ82ohnplQWO00HPS_RgoTZEggn3FxVpU0PnoNAL4FG2dUEeEKwdiVeIe1PalH77zQm8YurROjqbS42zsLdtEMU17xmwrGrel__R7xaMRN3DmHhZ8OV52VxzCnZbFT2wH0L3uC5GKvPW9R9_80Pptvum9HzUDwrhMUjBq9S90pAccavkcM4oHVLkQWVn4TBtRPahnzbLLz5h-8SfOy3V0kqaQ17JnBMc6692R2CTGnbi56Y64Kbki9tS9IFgnZDRKz5XzN15GkhWRG7qwafJKjTQg2QzSTAdNHjPOISNOp2CHlC3oq0eXdhzEwXUxvyc7hHdR5TDBMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«می‌خواهید تروما و مشکلات را ببینید؟ بگذارید آنها در مسیر، یک موشک به سمت سن‌دیگو یا لس‌آنجلس شلیک کنند.
می‌خواهید صحنه‌ای وحشتناک ببینید؟ می‌خواهید مشکلات را ببینید؟ بگذارید سن‌دیگو یا لس‌آنجلس را هدف قرار دهند.
ما اجازه نخواهیم داد چنین اتفاقی بیفتد. ما از شهرهایمان و کشورمان محافظت می‌کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/25153" target="_blank">📅 09:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=MIaM7kK4FPLK_XvKtpnh7C9iYWn2wpy3d9OTiTBIAnGIhwbgcSqISumzccK6R-IE2wlA_bDkMXEw6YDgtlHwJQ3LZQ_igAVD2vc0E-JNemEZUQJmchRGS8bvGg3eFaCg_58suTfk3nW0RBITzl0H4jBPmRTdSF7MsRcAj8WBv8aG9NfI0--MJfHnL1SLKPUHARlb_o1ikslPwGM1XYyxKCD-vDjYrNHUeDZa1h4gvAiZiTXeiewkJwOb-hf3vYmWaz9bmfTcjilWjil9IdNS4SXMkx37GQnqXHA-oH0afUJ-HvBFKRHuLMmMDuodpmS65TS0kFAe_NmquotPGKP34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c79099a6.mp4?token=MIaM7kK4FPLK_XvKtpnh7C9iYWn2wpy3d9OTiTBIAnGIhwbgcSqISumzccK6R-IE2wlA_bDkMXEw6YDgtlHwJQ3LZQ_igAVD2vc0E-JNemEZUQJmchRGS8bvGg3eFaCg_58suTfk3nW0RBITzl0H4jBPmRTdSF7MsRcAj8WBv8aG9NfI0--MJfHnL1SLKPUHARlb_o1ikslPwGM1XYyxKCD-vDjYrNHUeDZa1h4gvAiZiTXeiewkJwOb-hf3vYmWaz9bmfTcjilWjil9IdNS4SXMkx37GQnqXHA-oH0afUJ-HvBFKRHuLMmMDuodpmS65TS0kFAe_NmquotPGKP34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ : در سه شب گذشته، ما بیش از هر مقطع دیگری در تاریخ تنگه هرمز، نفت بیشتری از این تنگه خارج کرده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/25152" target="_blank">📅 09:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=vLpQ7VXRjlhHt2QeLn8re-B8zLbewU0vR18YtkJFs1QpKyttSJotVP1oohaop4E9usUFH068EuuNAqZSO9u-Ges_3IY81mWlJP44TJNZzJp1r2-qPEFHG_o10FnHdmYpmCd-FrgyJQs82kIMcAbjA2cCc9Tb4tsrggJ7g4dqhaDtYwaJ2iIWTpLtW_SrpQFZQe2Le8w4chr4mhWGIFtNCYiH91Wcw070lGenmwZAOV-70zRjuKqXvv9KaqhA0GYyt7X8pMMQqlvam_v_4mMRtLl6Vf6nzPFCjt9akpMGYsTA-Qu7xwxc_5uBxwNhd7OV_bHAWkwDTLGqZk3YN_7YzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef85cb34d.mp4?token=vLpQ7VXRjlhHt2QeLn8re-B8zLbewU0vR18YtkJFs1QpKyttSJotVP1oohaop4E9usUFH068EuuNAqZSO9u-Ges_3IY81mWlJP44TJNZzJp1r2-qPEFHG_o10FnHdmYpmCd-FrgyJQs82kIMcAbjA2cCc9Tb4tsrggJ7g4dqhaDtYwaJ2iIWTpLtW_SrpQFZQe2Le8w4chr4mhWGIFtNCYiH91Wcw070lGenmwZAOV-70zRjuKqXvv9KaqhA0GYyt7X8pMMQqlvam_v_4mMRtLl6Vf6nzPFCjt9akpMGYsTA-Qu7xwxc_5uBxwNhd7OV_bHAWkwDTLGqZk3YN_7YzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«جنگ خیلی زود به پایان می‌رسد. آنها کشوری شکست‌خورده هستند.
هنوز کمی روحیه و جسارت برایشان باقی مانده، اما زیاد نیست؛ اصلاً زیاد نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/25151" target="_blank">📅 09:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی کاخ سفید : رئیس جمهور ترامپ از روند فروپاشی اجتناب‌ناپذیر ایران راضی است.
ترامپ اجازه نخواهد داد که رژیم ایران مانند آنچه با روسای جمهور سابق اتفاق افتاد، او را مچل کنند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/25150" target="_blank">📅 02:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن: ایران هیچ‌وقت نتوانسته راهی برای عبور از آبراهام لینکلن پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما…</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/25149" target="_blank">📅 02:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=GP1TQgqa3K8UrMlwUWySr-awv-WeeMcJ3Mbd7xg4pFbhSx_nzTfjUYd1EpN_pGCVIN2D9sKRXUwe3d2FWjMIeunObOTIZYGn1zqBC6bqwkbr5dqBeyrfFHXYCPvinSjxPmoBLdOd8zUTdgiCnLvLeGv16xkp0ge-bINUrcJSX_kfINVTQrXDx4sgh0Jbl9eTAzCrHrdbtZqC6PMxFoYdB44Eq0XCNIcvjvNRmi265ZdB-J1a5y5evkZx6HbeH-8tuN0sizCPix9JtyidK92nK_a20aG7-4Iu3o7NRJBzgykI0lar60j-k0-fohZzbEB6whHz_QefUahf6U0xNa9aCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14526f5af7.mp4?token=GP1TQgqa3K8UrMlwUWySr-awv-WeeMcJ3Mbd7xg4pFbhSx_nzTfjUYd1EpN_pGCVIN2D9sKRXUwe3d2FWjMIeunObOTIZYGn1zqBC6bqwkbr5dqBeyrfFHXYCPvinSjxPmoBLdOd8zUTdgiCnLvLeGv16xkp0ge-bINUrcJSX_kfINVTQrXDx4sgh0Jbl9eTAzCrHrdbtZqC6PMxFoYdB44Eq0XCNIcvjvNRmi265ZdB-J1a5y5evkZx6HbeH-8tuN0sizCPix9JtyidK92nK_a20aG7-4Iu3o7NRJBzgykI0lar60j-k0-fohZzbEB6whHz_QefUahf6U0xNa9aCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، روی ناو یو‌اس‌اس آبراهام لینکلن:
ایران هیچ‌وقت نتوانسته راهی برای عبور از
آبراهام لینکلن
پیدا کند و طبیعتاً هم همین‌طور باید باشد. خیلی خوب بود که ناوگروه شما از ابتدای این مأموریت با نیروی دریایی ایران به یک توافق رسید؛ توافق شما این است که
اقیانوس را با هم تقسیم می‌کنیم، اما نیروی دریایی ایران سهمش کف اقیانوس است و آبراهام لینکلن سطح اقیانوس را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25148" target="_blank">📅 02:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knj0c-B8HsyCxRdSv3JKkSBgIGOqkVWwQrZXTQEeaSq7Zb3v82SX2RNVrH0IkTgxv2hCvElWiNGev2YyIoKfk_Cm2Cuwxw1pTkXkTjA_S4e1zHsX-QYnjx5qLSjv3_j5mB8Mgjs2boPKDWvhxdLrnBduzpJ0y1xT3hUXXRc-AGrjk0uhWM_5qK7AWQ5i223I7uCZz07_BMTgynAj5xfHKNNMVWsaDpRl1a6l_deFxNb2-Xnj7bPMqTFkDzuRcUyK3sOtkAyE532NHAhIVexarWVCNh8FV3cbo4V1ijHMtw9jdB4zEIfL0x3YXmo9jvV5uOr5ayEbBJ1sN8_XX-1q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت‌یاب سنتکام :
ادعا:
امروز یکی از ژنرال‌های سپاه پاسداران در گزارش‌های رسانه‌ای مدعی شد که «تنگه هرمز بسته است» و ایران «کنترل کامل آن را در اختیار دارد». این ادعا
نادرست است
.
واقعیت:
در حال حاضر تردد از تنگه هرمز ادامه دارد و کشتی‌های تجاری حامل کالا و محموله‌های انرژی، از جمله
حدود ۲۰ میلیون بشکه نفت خام
، در حال عبور هستند.
ایالات متحده و شرکای منطقه‌ای آن کنترل آشکار تنگه را در اختیار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25147" target="_blank">📅 01:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آکسیوس به نقل از سه مقام ارشد آمریکایی:
عربستان سعودی و سوریه در حال بررسی
اعزام نیروهای ارتش سوریه به یمن برای مقابله با حوثی‌ها
هستند. چندین یگان سوری برای این مأموریت در نظر گرفته شده و شمار نیروها می‌تواند به
۱۰ تا ۲۰ هزار نفر
برسد. این موضوع در دیدار اخیر
احمد الشرع و محمد بن سلمان
در ریاض مطرح شده و هدف عربستان، تقویت نیروهای دولت یمن و فراهم کردن امکان عملیات زمینی علیه حوثی‌هاست. با این حال، هنوز تصمیم نهایی برای اعزام نیروهای سوری گرفته نشده و مذاکرات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25146" target="_blank">📅 01:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ در تروث: سه سال پیش در چنین روزی، یعنی ۷ اکتبر، جهان شاهد یکی از تاریک‌ترین و شرورانه‌ترین روزها در تاریخ اسرائیل بود. مردان، زنان و کودکان بی‌گناه به دست تروریست‌های حماس به قتل رسیدند، ربوده شدند و متحمل وحشت‌هایی غیرقابل‌تصور گشتند. امروز، ما یاد تمام جان‌های بی‌گناهی را که از دست رفتند گرامی می‌داریم، به بازماندگان و خانواده‌هایشان ادای احترام می‌کنیم و به یاد گروگان‌هایی هستیم که رنج‌هایی غیرقابل‌تصور را تاب آوردند. من بی‌وقفه جنگیدم تا گروگان‌ها را به خانه بازگردانم و آن‌ها را به عزیزانشان برسانم؛ و این کار را انجام دادم، چه برای آنان که زنده بودند و چه برای آنان که جان باخته بودند! ما هرگز ۷ اکتبر را فراموش نخواهیم کرد. ما هرگز قربانیان را فراموش نخواهیم کرد. و همواره در برابر نیروهای ترور و شرارت خواهیم ایستاد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25145" target="_blank">📅 01:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=QzW9t7Ow3By6knr3WCuy-0J0ztjrA6f9Tm1GESxJocwfLDSUnKKMB8fHeoAa-btE9nZgxvg9eVjlvBvg3iB2-EFa8WUGFlMqQZtO3O3HJ5IpMHJCX_eqkMluKFtfBJp0Iifs3CKVzSGZv6SbddNdrSvvcsDrAMi5eDnvtd8joPUMa6mInXl6g3bzTU8XKyCdqN0PUVpuZP8v7VfXzZEIc3Kyvh6s_aU2zXfCbnpjTSkHriKgv-yC8820rr1ed5l3cHwttq2HFgRFvl7Q_u2hqvd6ghF2hnv2JmxjiRPb3h1ADzmsfxrTriPt93TS3J3CUP2z-WUW951LsZ_X7Mh4bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0adcb3b11.mp4?token=QzW9t7Ow3By6knr3WCuy-0J0ztjrA6f9Tm1GESxJocwfLDSUnKKMB8fHeoAa-btE9nZgxvg9eVjlvBvg3iB2-EFa8WUGFlMqQZtO3O3HJ5IpMHJCX_eqkMluKFtfBJp0Iifs3CKVzSGZv6SbddNdrSvvcsDrAMi5eDnvtd8joPUMa6mInXl6g3bzTU8XKyCdqN0PUVpuZP8v7VfXzZEIc3Kyvh6s_aU2zXfCbnpjTSkHriKgv-yC8820rr1ed5l3cHwttq2HFgRFvl7Q_u2hqvd6ghF2hnv2JmxjiRPb3h1ADzmsfxrTriPt93TS3J3CUP2z-WUW951LsZ_X7Mh4bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25144" target="_blank">📅 00:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران اعلام کرد که پاسخ ایران به پیشنهادات مطرح‌شده توسط آمریکا از طریق واسطه‌ها به طرف مقابل منتقل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25143" target="_blank">📅 00:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: مشاوره‌های ما با عمان با موفقیت انجام شد و بر سر هماهنگی‌های مربوط به مسیرهای امن به توافق رسیدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25142" target="_blank">📅 00:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: ما 82 هدف نظامی متعلق به شبه‌نظامیان حوثی را در استان‌های صعده، الحدیده، الجوف و مأرب منهدم کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25141" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به قول شاعر نایس پرفیوم
😼</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25140" target="_blank">📅 00:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=dnhC_1mr19yB8-_vaxj7ffnWKT-PKTrf6ssP4qJ19b3JZ6ojDKM-pDehDkoiP1CIUyWhu-uhs7mTLm0XKrBcmfqPiPMn-HzXRftoIfuTpoGgHHes_6dbUxSEEqpo1iG7SiMjyouiceyerYxGnEYWhEGM4HPjRArj-LV_LHdMyOFAD6yuwRqt3BhEjZBNU1hkCx-4CseLvu6HdEUg0ICUZ-B1m3oTftidL0GuTEN9pEbhgJEue6RcANESgbyLoZC1tQyt6kXko0u7WrivHPg3S-o3tYpfpVzort0r0yjrBZe1vz0tDq9x0UXOaSZOn8H_IYT3k6baLjEqlIdFl7JKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af54a6283.mp4?token=dnhC_1mr19yB8-_vaxj7ffnWKT-PKTrf6ssP4qJ19b3JZ6ojDKM-pDehDkoiP1CIUyWhu-uhs7mTLm0XKrBcmfqPiPMn-HzXRftoIfuTpoGgHHes_6dbUxSEEqpo1iG7SiMjyouiceyerYxGnEYWhEGM4HPjRArj-LV_LHdMyOFAD6yuwRqt3BhEjZBNU1hkCx-4CseLvu6HdEUg0ICUZ-B1m3oTftidL0GuTEN9pEbhgJEue6RcANESgbyLoZC1tQyt6kXko0u7WrivHPg3S-o3tYpfpVzort0r0yjrBZe1vz0tDq9x0UXOaSZOn8H_IYT3k6baLjEqlIdFl7JKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25139" target="_blank">📅 00:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25138" target="_blank">📅 00:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25137" target="_blank">📅 00:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=pvfd7BrkacDuAJANlmOR7Qk-rGO2ITdXnnjnar0DkO370zn0IQDlGYoe9EMiKRzfGCH6JhUUy5FBH35d4YyIr_sZYO5jpcyWQQIfxYCZJirL1kKS3lRqHH3TkPp3qvRKdnwM2iBsfIwDJu61_fzRHGhB7ifwoZSLhTVFPMw1xG6hqK7mUoVeUTI2i0FN88WcledL2z2AvSSg9B3KiYxmCHmToS1ARaLXw8cq2Hd0uq79NilopbK-kk2svuImmHIubEMn9-DstAcf7AMp7tjnqAkowzOZ9kcdagf-hG0QyNs3dP1RkFOa4LP9YZMKeKMWsNBjcpSIFdQMleyos06r4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df53d80fe4.mp4?token=pvfd7BrkacDuAJANlmOR7Qk-rGO2ITdXnnjnar0DkO370zn0IQDlGYoe9EMiKRzfGCH6JhUUy5FBH35d4YyIr_sZYO5jpcyWQQIfxYCZJirL1kKS3lRqHH3TkPp3qvRKdnwM2iBsfIwDJu61_fzRHGhB7ifwoZSLhTVFPMw1xG6hqK7mUoVeUTI2i0FN88WcledL2z2AvSSg9B3KiYxmCHmToS1ARaLXw8cq2Hd0uq79NilopbK-kk2svuImmHIubEMn9-DstAcf7AMp7tjnqAkowzOZ9kcdagf-hG0QyNs3dP1RkFOa4LP9YZMKeKMWsNBjcpSIFdQMleyos06r4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلانتری گلشن تبدیل به گوهشن شده , درگیری ادامه داره
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25136" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سیستان و بلوچستان درگیری های شدید گزارش میشه ، همه هم شکل و لباس هستند و حکومت درمونده شده ، نمیفهمه از ‌کجا و کی میخوره
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25135" target="_blank">📅 00:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه خون دماغ شده دکمه پرتاب آبگرمکن از بندر عباس رو هی میزنه ، تنگه صدای ناله های شهید عججی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25134" target="_blank">📅 00:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25133" target="_blank">📅 00:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25132" target="_blank">📅 00:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن  بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25131" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvcXt6zb9ZAyJ6Y0I8NLr1vy0ihUJ3UReA7Q6nVHwloPANKVgDqWX2WC_gDLf4Zeg5VcFwJiylaWR603S0OlyoVTubK9bwEqIvfdFPCyYi30EYrahf9Q-_p6V8zyBVkA02-EWIH1_9oLyBH2h0W5n3Y-VE78HWfUvfUWZq52vvtN-le4qvd9d31Y03fSqeGwe3nPWD0IyMrEUOX_p7Y1-BhrEyo1Oxj4whFZK5J_1NdrQr_isXqhugwcoh97oRw_rjpd3GD3euQteslM5Q1s7HlWVWmHWf1zRjhcr16QAy2UDg9q4Z1SzL1LRW7HThGlPnXFwzg5TpfnHBCxONvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع یک حادثه در فاصله ۵۱ مایل دریایی شمال «مدینة الشمال» در قطر دریافت کرده است.یک نفتکش گزارش داده است که هدف اصابت چندین پرتابه قرار گرفته است.
گزارش‌هایی از تلفات انسانی منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25130" target="_blank">📅 23:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOa6djIq-Qtc80paSC9Egc8iHcWy4wpF2S2Vmjg3PSLFH243e9BgbaEC6Z2nFU6w9OK42uZIoDAy2EZBP_iphhmEcb5W0ApIIrHnrPeHWSNz55jLnu_7vYtiudZ2R0t_kvqIhylLy0pNCSa94G-49v9RCye9tt3JVn_pgQ36B8PDrqDU91X7ApB51sGN8WUvdk_Cl6zKmaiyBMk7CK7gx1P8FyU7H8EYV31iNKUL-JvRernThUR4OBV0SeaB6ddAwx-pTwLSCApBHfowOhnjZu4lJVHv5ImqG4at_WHG7q-vzFeie2k1IN9gow_jeKZauirVjUF1-EryriWzHWfT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون نظام وظیفه: اگه لازم باشه برا جذب سربازای ۶۰ ساله هم فراخوان میدیم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25129" target="_blank">📅 23:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25128" target="_blank">📅 23:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال 15 عبری: ایران در روزهای اخیر شلیک به سمت کشتی‌ها در تنگه هرمز را از سر گرفته است. ارزیابی این است که حمله‌ای از سوی آمریکا انجام خواهد شد و بنابراین ممکن است آنها بخواهند ابتدا حمله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25127" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=qd478cWIGI7aSIJimNb8WHKgjFl25k98SlhWNVWdgDpdkVZ2pDD2VD3iXkUDDIK_3DqFKvQD2f5mRpAG4Mh7ZzIQpKaWuL6tHi1M31vhHUzOpp-IXZ-6349HscpMB241kBcjJwtqFhG_XkAUGgnHNy7YW0QaqGc79uDdwUH2fBIWRtI5V_ULqnRt9w4ciUWJrzcXysvp7Tqm4ihOuXAurwkiGjPkI1sMJyz7JanAw8kB3L5hbzX8QNqqjHgcfYPrxM1zZQ6HGvMi-fVurzHFHPCj2sCUJCmi0QFScBm1cuitAo-wW8x9p1ig8ohyGCNXOOxvRSCOtu0WomxxJNd16g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c43a91ec.mp4?token=qd478cWIGI7aSIJimNb8WHKgjFl25k98SlhWNVWdgDpdkVZ2pDD2VD3iXkUDDIK_3DqFKvQD2f5mRpAG4Mh7ZzIQpKaWuL6tHi1M31vhHUzOpp-IXZ-6349HscpMB241kBcjJwtqFhG_XkAUGgnHNy7YW0QaqGc79uDdwUH2fBIWRtI5V_ULqnRt9w4ciUWJrzcXysvp7Tqm4ihOuXAurwkiGjPkI1sMJyz7JanAw8kB3L5hbzX8QNqqjHgcfYPrxM1zZQ6HGvMi-fVurzHFHPCj2sCUJCmi0QFScBm1cuitAo-wW8x9p1ig8ohyGCNXOOxvRSCOtu0WomxxJNd16g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
فکر می‌کنم داریم خیلی خوب پیش می‌ریم. داریم ایران رو خیلی بد می‌زنیم.
اون‌ها هیچ‌وقت سلاح هسته‌ای نخواهند داشت، و این خیلی مهمه.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25126" target="_blank">📅 22:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amd4_RXCyzOHCMyyzx6FKVeaE4KCHhxB_RW_3_nSM5LLjiu99kqkFLhbcpJs9voOWIqCyLhfRSV-_32Lm2GTF_gYOdpaX0a0wLb7koyasq7rkhIDg_aHU5i2e4zbxo7YGxlmV-Vk525e5uP_-_dQ8jnmAIhi3ErjRrEObbVGFbJo-vtnFc_7ywa7saaPgNooZT15jktVoS2ILHxu2N-Xdqqfz16_vrCc27DD-Jo0_Ao2S1ySwxOe0SqjMg6OEoGrEAG8zaKuoVcBlhcCo7desUaZQMyqjWMCOmxGQiWKiaZA1K3q9_w5TeyaICPQtghnSQtQF1S_ucpZgUS8yQKW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
این هفته، گروهبان ارشد تفنگداران دریایی آمریکا از نزدیک شاهد نحوه تجهیز نیروهای مستقر در خاورمیانه به
قابلیت‌های پیشرفته پهپادی
توسط سنتکام بود.
تفنگداران دریایی به
کارلوس ای. رویز
، گروهبان ارشد تفنگداران دریایی، درباره استفاده تاریخی سنتکام از
سامانه‌های پهپادی تهاجمی یک‌طرفه کم‌هزینه
(نمونه آمریکایی شاهد) توضیح دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25125" target="_blank">📅 22:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دو منبع دیپلماتیک منطقه‌ای به i24 نیوز: احتمال دارد تهران یک حمله پیش‌دستانه را آغاز کند، به دلیل نگرانی از یک حمله آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25124" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آتلانتیک:
احتمال دارد که ترامپ قبل از انتخابات میان‌دوره‌ای، دستور حمله دیگری به ایران را صادر کند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25123" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فاکس نیوز : خنثی شدن طرح تیراندازی در «مال آو آمریکا»
مقام‌های فدرال آمریکا اعلام کردند یک
طرح تیراندازی جمعی با الهام از داعش
که قرار بود مرکز خرید «مال آو آمریکا» در مینه‌سوتا را هدف قرار دهد، پیش از اجرا خنثی شد.
شیخدون عبداللهی محمد، ۱۸ ساله
، به گفته دادستان‌ها با داعش بیعت کرده و ابتدا قصد سفر به خارج از آمریکا برای پیوستن به این گروه را داشته است. بر اساس اسناد دادگاه، او قصد داشت در یک رویداد در
۲۴ اکتبر
تیراندازی کند و هدفش کشتن
۳۰ تا ۶۰ نفر
بود. اف‌بی‌آی پس از آن او را بازداشت کرد که طبق اسناد، وی از یک مأمور مخفی(آندر کاور)
یک قبضه AK-47 و ۲۰۰ گلوله
خریداری کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25122" target="_blank">📅 21:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری صدا‌وسیما : حمله مسلحانه به مقر انتظامی در گلشن
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن سیستان و بلوچستان مورد حمله مسلحانه قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25121" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ درباره اینکه چرا شایسته دریافت جایزه نوبل صلح است:
من شاید جلوی
نابودی کامل جهان
را گرفته باشم، چون ایران هرگز سلاح هسته‌ای نخواهد داشت. اوباما این جایزه را گرفت، در حالی که هیچ کاری انجام نداد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25120" target="_blank">📅 21:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=NtXtSAhRrtlbIN98Y3vcF-eGKvuHvoYWEBRQv1mdsm6RWnTqqS6ueHdFttnCNkPdPza07zkXbSl11ufunrnnnLJF64FN5FuxTfeOOlIEMZ5uWIL7jZKL74ZEzgr-QNb8B3Szwyjm4UUg4ww9WQVR4bzT1rWqA5FV8czIQ5xRHCTDJJDVb2GTiziJoTFQJeH0gAnY5_83KnfJk6bi8wkdThBAduYDSAFn1Umq03eKOcJSVLoM_yh-D-Z03FL820CZtYp2r6uMGZ2LqLt9faN0J5xSV5JdnUoSgHM1ff2qttigYDJW2Gs0Z2jwuwn4v8B82nUD12wXGB4-dYsRy1U7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b83a25ca.mp4?token=NtXtSAhRrtlbIN98Y3vcF-eGKvuHvoYWEBRQv1mdsm6RWnTqqS6ueHdFttnCNkPdPza07zkXbSl11ufunrnnnLJF64FN5FuxTfeOOlIEMZ5uWIL7jZKL74ZEzgr-QNb8B3Szwyjm4UUg4ww9WQVR4bzT1rWqA5FV8czIQ5xRHCTDJJDVb2GTiziJoTFQJeH0gAnY5_83KnfJk6bi8wkdThBAduYDSAFn1Umq03eKOcJSVLoM_yh-D-Z03FL820CZtYp2r6uMGZ2LqLt9faN0J5xSV5JdnUoSgHM1ff2qttigYDJW2Gs0Z2jwuwn4v8B82nUD12wXGB4-dYsRy1U7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
پیتر دوسی از فاکس نیوز: آیا همین حال و هوایی را که در آغاز کووید از چین داشتید، اکنون از روسیه در مورد طاعون هم حس می‌کنید؟
ترامپ: خب، چین زیاد چیزی نگفت و روسیه هم زیاد چیزی نمی‌گوید، اما آن‌ها می‌گویند که کنترل آن را به شدت در دست دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25119" target="_blank">📅 21:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333de74250.mp4?token=XTwsaRfWGv9ZO2q00ZtvyfR4OHKeszeMp9AmpcIkt4XcMLexHS0TsBaYwIVU30IiyxaJhxI9DGbROxXgB23auxljLHZurkFVfdHsgr3QOmAaSLHyRT8SQIkik3jsBuJ-zTWc3RdAy3KDYH2dW3DisF9y-73KmX7TplLUVgUjlIFQFpmfSpcigBMf23CkAbViSM0HmSOO6xRUuMNIDmIloZFwW7Vi0Q9Cos18cEq-1yoFulY1-HzCUArxFiOEMjzAyMstDXrmtMNhaIAOkNPlDvSC5HdPqhGDh6WpTZ2H5FsQWyP6zP8oTV6sTjD4r-BUL9HS-nYdmNeu3NYpMTpWxD04mhKNQ3bfBOUBZZVkVU0dfvzNJ1bMqon53u3dSeZ26uqZVuWwGjNcI1xHVrIvkUkPQRYZhGINdY8RTe1u58anT5cBcxZPtY2hvro7Hj3TOv6Gr89VV4rSXJs-dI2HPWbJ7MjSwPIPHGyrwhtfGpmvZ3SzbZaGHJrnGl4RICtYWUGAivBZX89DVfV-1tnYFetrwgwm06Hwj3Z0G9IOKzOXJ-W2tUPNF5b7XbQmX16iQGFvGWEfbWuqEH3rrsvb4Y94GX7K6RPMm3K7nvP0RNZ3R-eeHffgjGPE67AA1tSevIrENg7o7CnCZL3EOmR_-cEWiOqJWtP5YtHlwCUTQ1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333de74250.mp4?token=XTwsaRfWGv9ZO2q00ZtvyfR4OHKeszeMp9AmpcIkt4XcMLexHS0TsBaYwIVU30IiyxaJhxI9DGbROxXgB23auxljLHZurkFVfdHsgr3QOmAaSLHyRT8SQIkik3jsBuJ-zTWc3RdAy3KDYH2dW3DisF9y-73KmX7TplLUVgUjlIFQFpmfSpcigBMf23CkAbViSM0HmSOO6xRUuMNIDmIloZFwW7Vi0Q9Cos18cEq-1yoFulY1-HzCUArxFiOEMjzAyMstDXrmtMNhaIAOkNPlDvSC5HdPqhGDh6WpTZ2H5FsQWyP6zP8oTV6sTjD4r-BUL9HS-nYdmNeu3NYpMTpWxD04mhKNQ3bfBOUBZZVkVU0dfvzNJ1bMqon53u3dSeZ26uqZVuWwGjNcI1xHVrIvkUkPQRYZhGINdY8RTe1u58anT5cBcxZPtY2hvro7Hj3TOv6Gr89VV4rSXJs-dI2HPWbJ7MjSwPIPHGyrwhtfGpmvZ3SzbZaGHJrnGl4RICtYWUGAivBZX89DVfV-1tnYFetrwgwm06Hwj3Z0G9IOKzOXJ-W2tUPNF5b7XbQmX16iQGFvGWEfbWuqEH3rrsvb4Y94GX7K6RPMm3K7nvP0RNZ3R-eeHffgjGPE67AA1tSevIrENg7o7CnCZL3EOmR_-cEWiOqJWtP5YtHlwCUTQ1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: حماس همچنان از بیمارستان‌ها برای فعالیت‌های تروریستی سوءاستفاده می‌کند:دو عضو حماس که از
بیمارستان کمال عدوان
در شمال نوار غزه خارج شده بودند، بامداد چهارشنبه شناسایی و کشته شدند. به گفته ارتش اسرائیل، یکی از آنها در حال
کارگذاری بمب‌هایی بود که از داخل بیمارستان به منطقه خط زرد منتقل شده بود
. فرد دوم،
محمد طموس
، تک‌تیرانداز شاخه نظامی حماس بود که هم‌زمان به‌عنوان
کارمند امداد و نجات
فعالیت می‌کرد. ارتش اسرائیل مدعی است حماس در هفته‌های اخیر از بیمارستان کمال عدوان برای فعالیت‌های نظامی و بازسازی توانمندی‌های خود استفاده کرده و این اقدامات را
نقض توافق آتش‌بس
می‌داند. تصاویر عملیات نیز توسط ارتش اسرائیل منتشر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25118" target="_blank">📅 20:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای انفجار در حیفا همه را ترسانده. ولی هیچ آژیری فعال نشده. در نتیجه نظر من این است که از آنجا که حملات سنگینی در جنوب لبنان در حال انجام است، به قدری که جنوب لبنان را بد زدند، صداش حیفا همه ترسیدن یا سونیک بوم خود جنگنده ها بوده
@WarRoom
این خبر بروزرسانی میشود</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25117" target="_blank">📅 20:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز: آژانس بین‌المللی انرژی اتمی می‌گوید پیش از حملات، ایران
۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد
در اختیار داشت. پس از حملات، ایران میزان و محل ذخیره باقی‌مانده را به آژانس اعلام نکرده و بازرسان نیز هنوز به سایت‌های هسته‌ای بمباران‌شده دسترسی کامل ندارند. آژانس برآورد می‌کند
بیش از ۲۰۰ کیلوگرم از این ذخیره همچنان در مجتمع تونلی اصفهان باقی مانده باشد
و بخشی دیگر نیز در نطنز بوده است. رویترز تأکید می‌کند که
مقدار دقیق اورانیوم باقی‌مانده مشخص نیست
و بخشی از ذخیره نیز ممکن است در حملات نابود شده باشد؛ بنابراین نمی‌توان گفت مابقیِ ۴۴۰.۹ کیلوگرم حتماً از بین رفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25116" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توییت جدید
🚨
🚨
🚨
🚨
https://x.com/yasharrapfa/status/2107855000521293885?s=46</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25115" target="_blank">📅 18:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رویترز: ایران ماه گذشته
۲۰۰ میلیون دلار
به حزب‌الله لبنان داد تا این گروه به خانواده‌های لبنانیِ آواره‌شده در جنگ با اسرائیل کمک مالی کند.حدود
۵۰ هزار خانواده
که خانه‌هایشان تخریب شده یا امکان بازگشت ندارند، در اولویت قرار می‌گیرند و به هر خانواده در مرحله نخست حدود
۳ هزار دلار
پرداخت می‌شود.این نخستین کمک مالی قابل‌توجه حزب‌الله به پایگاه اجتماعی خود از زمان آغاز جنگ در ماه مارس عنوان شده است. انتقال پول از طریق واسطه‌ها انجام شده و این واسطه‌ها حدود
۲۰ درصد کارمزد
دریافت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25114" target="_blank">📅 18:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای درد و دل تنگسیری و سلیمانی‌ از تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25113" target="_blank">📅 18:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBTvNauCcBPV7RJObc3x9kJsGepor6tO7kdQIWwSeBk7CmbSakQgS8SCyH2Tcg9aytTaDXL6WI2V-BwN9Hn5loLHnLFE9HztgvlJmpuT3SSbgmvtzp5Klwa_dXo6ooy6V-uHrLnAMTeRlKr-RaqutVvcNgcxJ6tMOg9F8P2CkQS3pt6B3KQR1UITvrcHXavjMWpsaaBCboKkBFqOzsurReYugNwyQbZXFSZsR1Idg3mJm2Dq19aH_YdAoxe-ZnfO5Ff1KzGMJPxnFFGbgGFA6OMNF2i6ZwPnq2d9ulADzx9E7zfZymKiRo3n09t_ToiYLDnBIyXWw0TKMH44NvxcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد نیویورک پست از عکس تروریست های حماس که یک دختر بی گناه اسرائیلی را که در فستیوال موزیک بود کش‌ته و حمل می کنند
نیویورک پست : تا همین چند وقت پیش، اگر به آن‌ها می‌گفتید “یهودستیز”، برای توصیف این بیماری روانی‌شان کاملاً کافی بود؛ اما در سه سال گذشته، امثال آن‌ها آن‌قدر از خط قرمز رد شده‌اند که این کلمه دیگر اصلاً نمی‌تواند عمق لجن و پستی آن‌ها را نشان دهد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25112" target="_blank">📅 18:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317b1bb05e.mp4?token=sJH1AaP1ue5DjLpy4VW4lrjBkx7dmEvUuS5_ZCFzs2zrXMrxJBJ97ffukkhnuVR0_WpV2h7Nm8OqiAFmaWS6MEspGoUl3rNmyykNVf1umaNBkShL5Qcf_XHZ2s1nXlZdD0oxFfNZbdTq1y3JULnThawVkW9L4Wx8SttjG1ULks0OwHUHnmrnn8zCKU0XNaDaizUf0bP05zbR2iUlaHqHpYdn7T7pK1dunrY4HpkkpvT5JZpysMOfnVOobGRoZ3dxK7GwJ3bv_1vp0YCHR1uozAweHOCb670M0JcSei_F3SfJUUSXuyb-vRLceead7ofOudKU4S-OtRkKJdp2o7qzKxstoFt3naeqLucN81gEBumDxUkX3eISZ6sMjK7VSGWCY8Ij37MURHfolwtOHss9JrZeoVlfTMCo8pqdIIzfKHXOUSQQ9pCu3GhVLogz4mW-5x6sVZuR1wZMBc3kruCZsywWMIJSek5YufjJURafwBkqIj5GPVSKKX7FgUktWdQ8Mw7yEVOw6jPHnrLtVnuK7YLQSvYEgGDukJsvlUpSlAG-6qJJvmANaxwkHuJy6w3H73f1n8J3Y_EtWhzhUfLyz0iRVoJbVKHFLyIYBn1syXMIa2rgXvjbmV8IsJB8dQWEDpaP_Ge-9dPwxiD4aI7ZORfrGCQct_W6B29X8MoquJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317b1bb05e.mp4?token=sJH1AaP1ue5DjLpy4VW4lrjBkx7dmEvUuS5_ZCFzs2zrXMrxJBJ97ffukkhnuVR0_WpV2h7Nm8OqiAFmaWS6MEspGoUl3rNmyykNVf1umaNBkShL5Qcf_XHZ2s1nXlZdD0oxFfNZbdTq1y3JULnThawVkW9L4Wx8SttjG1ULks0OwHUHnmrnn8zCKU0XNaDaizUf0bP05zbR2iUlaHqHpYdn7T7pK1dunrY4HpkkpvT5JZpysMOfnVOobGRoZ3dxK7GwJ3bv_1vp0YCHR1uozAweHOCb670M0JcSei_F3SfJUUSXuyb-vRLceead7ofOudKU4S-OtRkKJdp2o7qzKxstoFt3naeqLucN81gEBumDxUkX3eISZ6sMjK7VSGWCY8Ij37MURHfolwtOHss9JrZeoVlfTMCo8pqdIIzfKHXOUSQQ9pCu3GhVLogz4mW-5x6sVZuR1wZMBc3kruCZsywWMIJSek5YufjJURafwBkqIj5GPVSKKX7FgUktWdQ8Mw7yEVOw6jPHnrLtVnuK7YLQSvYEgGDukJsvlUpSlAG-6qJJvmANaxwkHuJy6w3H73f1n8J3Y_EtWhzhUfLyz0iRVoJbVKHFLyIYBn1syXMIa2rgXvjbmV8IsJB8dQWEDpaP_Ge-9dPwxiD4aI7ZORfrGCQct_W6B29X8MoquJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوش بدروسیان: شما در سازمان ملل گفتین روزی که خیلی هم دور نیست، مردم ایران آزاد خواهند شد. منظورتون چی بود؟
نتانیاهو: «دقیقاً همون چیزی که گفتم؛ جمهوری اسلامی سقوط خواهد کرد.»
شوش بدروسیان: می‌تونین زمانی براش مشخص کنین؟
نتانیاهو: «بله، می‌تونم؛ ولی ترجیح می‌دم علناً زمانی اعلام نکنم. مردم ایران در زمان درست و وقتی شرایط مهیا باشه، بلند میشن و این نظام رو سرنگون می‌کنن.»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25111" target="_blank">📅 17:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ممباقر ، رئیس مجلس ایران:
«برنامه دشمن بر انجام اقدامات خشونت‌آمیز در داخل کشور متمرکز است.این برنامه و راهبرد دشمن نشان می‌دهد که اولویت اصلی ما نیز باید تقویت تاب‌آوری اقتصادی و تأمین امنیت داخلی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25110" target="_blank">📅 17:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مرد خردمند ، مارک لوین در‌ اکس : من طرفدار پروپاقرص رضا پهلوی هستم. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25109" target="_blank">📅 16:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25108" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSh</strong></div>
<div class="tg-text">اقا یاشار این مرد خردمند که اول اسم ایشون همیشه مینویسید  چیه</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25107" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25106">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شاهزاده رضا پهلوی: به مردم اسرائیل: در سومین سالگرد ۷ اکتبر، در غم، یادبود و همبستگی در کنار شما ایستاده‌ام. ما هرگز کسانی را که به قتل رسیدند، رنج خانواده‌هایشان و بازماندگان این جنایت را فراموش نخواهیم کرد. جمهوری اسلامی که حماس را مسلح و حمایت کرد، همان…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25106" target="_blank">📅 16:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار | تحلیل بازار: برخلاف برداشتی که ممکن است از حرکت امروز بازار ایجاد شود، ریال ایران فعلاً وارد یک روند پایدارِ تقویت نشده است و آنچه در بازار دیده می‌شود بیشتر می‌تواند ناشی از دخالت ارزی، عرضه دلار و اصلاح موقت پس از جهش اخیر باشد. هم‌زمان،…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25105" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرگزاری فرانسه:
همزمان با نگرانی‌ها درباره مرگ یک کارمند  آزمایشگاه تحقیقات طاعون در روسیه و پیغام آمریکا برای کمک ، مسکو نیز در جواب اعلام کرد آماده کمک به آمریکا برای مقابله با شیوع بیماری‌
سرخک
است. سازمان نظارت بر بهداشت روسیه اعلام کرد این کشور می‌تواند متخصصان، تجهیزات آزمایشگاهی و ابزارهای تشخیص و پیشگیری در اختیار آمریکا قرار دهد. این نهاد همچنین از تشدید وضعیت سرخک در چند ایالت آمریکا خبر داده است. در همین حال، مقام‌های روسیه می‌گویند تاکنون هیچ مورد تأییدشده‌ای از طاعون در میان افراد در تماس با کارمند جان‌باخته پیدا نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25104" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQa9RsXHOqAIqxlMmZUYgw_FZWrlw0A2JZzFMuBXGzlwaFysESGS3wgTLBggUSjZuacKu5lj55tBNTP8sMIoumCaLr1M7mkDgzzgzDwY9_VzuV1Mnv_JXYge7MmHY89Zt5JS-dqJB4Awqqpfgacu5Q2HXgU5aSOmgbgWouSz0_7KjWSU2xf7cHyeZrajfQ0GZOvUs-kYF4jaXHbKfuJlThCQOFRGgk1Qwx3jzzJYWZ-fEDxl_YaXi2QFeOsVFFXAJZmzon4DSHgs9bWnx5-GoRjiW33_zGuvV_wapOm4OPVqpa_4SSUxshRnumG4jb1aw7-Z8x8itN8GINLKBVIMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:
تالار «کهکشان غدیر» در قم پس از حضور علی دایی و همسرش در یک همایش خصوصی و آنچه «عدم رعایت حجاب» و «هنجارشکنی» عنوان شده، با دستور دادستان قم توسط پلیس اماکن پلمب شد. طبق اعلام قرارگاه امنیتی سجاد، حضور افراد بدون رعایت ضوابط در این مراسم موجب اعتراض‌هایی شده و برای عوامل برگزارکننده نیز
پرونده قضایی تشکیل شده است
. دادستان قم نیز تأکید کرده با موارد مشابه، به‌دلیل «شأن و منزلت شهر قم»، برخورد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25103" target="_blank">📅 15:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایران‌آنلاین:
مسعود پزشکیان در تماس تلفنی با ولادیمیر پوتین، زادروز رئیس‌جمهور روسیه را تبریک گفت و برای دولت و مردم این کشور آرزوی سربلندی و شکوفایی کرد. دو طرف بر
تداوم و تقویت همکاری‌های دوجانبه و راهبردی تهران و مسکو
تأکید کردند. پوتین نیز ضمن تشکر از پزشکیان، بر ادامه همکاری‌ها در چارچوب
معاهده همکاری جامع راهبردی
تأکید کرد و گفت روسیه آماده کمک به تلاش‌های دیپلماتیک برای کاهش تنش‌های منطقه‌ای است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25102" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسکای‌نیوز عربی به نقل از یک منبع نظامی اسرائیلی:
اسرائیل فعلاً قصد عقب‌نشینی از جنوب لبنان را ندارد و بازگشت ساکنان مناطق موردنظر نیز ممکن است سال‌ها طول بکشد. این منبع مدعی شد در بخش‌هایی از جنوب لبنان، در جنوب «خط زرد»، همچنان زیرساخت‌های حزب‌الله وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25101" target="_blank">📅 15:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏دوستان و همشهریان ⁧ عليرضا سپاهى ⁩ بخاطرش ماشینهاشون رو گل زدن و کاروان جشن دامادی راه انداختند و با سوگ می‌رقصن…  @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25100" target="_blank">📅 15:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی
:
هیچ مذاکره‌ای میان ایران و آمریکا
درباره برنامه هسته‌ای تهران
در جریان نیست
.
آمریکا ابتدا باید شروط ایران را بپذیرد
تا مذاکرات هسته‌ای امکان‌پذیر شود.
به‌رسمیت‌شناختن حق غنی‌سازی ایران از سوی آمریکا خط قرمز تهران است.
ایران هرگز از حق خود برای غنی‌سازی صرف‌نظر نخواهد کرد، اما جزئیات و نحوه غنی‌سازی می‌تواند در ادامه مورد بحث قرار گیرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25099" target="_blank">📅 15:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70eabff49d.mp4?token=WkEDypRAKJbj_Ndp3bmz8qf3dslpaPrRVEO16pBONpaCUfOn8U4hRghiXQxEE50BxiRqn5SqjYZPrnDV7OI2ArZc1GufDQ0WfG4weCP-4mMUrb7uMY2rWwNXP428pqW6L8jph1ZGd_tUgJzqE2LquN1vCXX9irHylk-IICI9nlCoCLwcjRUQaIv8bgjj5I_diL5FIKEydbH6ADqBRsqpIT5ROoQYye7zku5L2hfnQdIXl406OqBeoecZiO-s3OOV1P3WH6a9w3l-EIuWd-PcXzfpLOvh0dfWMMUsQBdgEkZlB2WiYoadXgMijoxvTuLUmSNyhzL7mqdTtm9-PrZBZqq0PDZFyb9eNCdFGtVOsIHyDQabcAA2DsifVS3SWmyVr1Go5c0PT2QwLq2de83Bx7ZTeZ6-K3m6-Rx7xbR4lm2iSwnQQ7kqlvus7LPX6ghSdnhUBK1enxXkYnPkltRwr5CKHT94miC7PkIDI1x5bfo9e3MbFa6jW4cN87kiaehqHyBR_JUA7nvZnEQjsiDzxZ-S4vCRk2isG15tNKIbo3UQ0Sk9mNmcVx0oket1IbZWGUHbNCifENtJBiq9ShoXca0JmrSlorAStCU_Dkg5b2GKMUpe-JGOB-Yk_fM_1_kRUTf8dn3h0jMTg9VENyXD9zD7xxT6DjRgnEmwEIOOLHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70eabff49d.mp4?token=WkEDypRAKJbj_Ndp3bmz8qf3dslpaPrRVEO16pBONpaCUfOn8U4hRghiXQxEE50BxiRqn5SqjYZPrnDV7OI2ArZc1GufDQ0WfG4weCP-4mMUrb7uMY2rWwNXP428pqW6L8jph1ZGd_tUgJzqE2LquN1vCXX9irHylk-IICI9nlCoCLwcjRUQaIv8bgjj5I_diL5FIKEydbH6ADqBRsqpIT5ROoQYye7zku5L2hfnQdIXl406OqBeoecZiO-s3OOV1P3WH6a9w3l-EIuWd-PcXzfpLOvh0dfWMMUsQBdgEkZlB2WiYoadXgMijoxvTuLUmSNyhzL7mqdTtm9-PrZBZqq0PDZFyb9eNCdFGtVOsIHyDQabcAA2DsifVS3SWmyVr1Go5c0PT2QwLq2de83Bx7ZTeZ6-K3m6-Rx7xbR4lm2iSwnQQ7kqlvus7LPX6ghSdnhUBK1enxXkYnPkltRwr5CKHT94miC7PkIDI1x5bfo9e3MbFa6jW4cN87kiaehqHyBR_JUA7nvZnEQjsiDzxZ-S4vCRk2isG15tNKIbo3UQ0Sk9mNmcVx0oket1IbZWGUHbNCifENtJBiq9ShoXca0JmrSlorAStCU_Dkg5b2GKMUpe-JGOB-Yk_fM_1_kRUTf8dn3h0jMTg9VENyXD9zD7xxT6DjRgnEmwEIOOLHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس امنیت دولتی گرجستان: یک شهروند گرجی به دلیل
نگهداری غیرقانونی مواد هسته‌ای
و تلاش برای فروش اورانیوم-۲۳۸ بازداشت شد. به گفته این سرویس، فرد بازداشت‌شده قصد داشت اورانیوم را به یک
تبعه خارجی
به قیمت
۷۰۰ هزار دلار
بفروشد. مأموران امنیتی پس از دریافت اطلاعات درباره این معامله، تحقیقات را آغاز و این فرد را بازداشت کردند. مقام‌های گرجستان ملیت تبعه خارجی را اعلام نکرده‌اند و تحقیقات درباره پرونده ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25098" target="_blank">📅 15:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/25097" target="_blank">📅 15:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">در پی انتشار ادعاهایی درباره آزادی یا عفو امیرحسین مقصودلو (تتلو)، پیگیری ها از وکلای وی نشان می‌دهد تا این لحظه هیچ ابلاغ یا سند مکتوبی درباره آزادی، عفو یا تغییر وضعیت قضایی تتلو به وکلای او ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25096" target="_blank">📅 14:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز به نقل از مقامات: ترکیه، کمک‌های دفاعی و فنی به عربستان سعودی ارسال کرده است تا به آن در جنگ علیه حوثی‌ها کمک کند. این کمک‌ها شامل سامانه‌های پدافند هوایی، اپراتورهای هواپیماهای بدون سرنشین، و همچنین اطلاعات، نظارت و شناسایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25095" target="_blank">📅 14:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1nZ25V_wsy5Keu7fNyYgnWTeock9_793A0b2gEzt85Jnt-1-TX9kJlNfpgHqrFL_NhynJD4mBKs3suwxmbzJy2RF0zwzaVbvAkUFIBRbmC8V6g7bIxOezM6TPh1Y1ZJT81oSggQ1C8lE1pKUDUIvR_wT25K0UOPLUgX3y1vQzjs6kcbEtqCECHGsygdAPQzC3oxXacnNEJuXLVWpwlNhejW1-UVTDd-E2EoKzWbMSsZ8x2dA29kRZGL7igvuhPh9LblIW3lhJuiiYjFRJWqalbfBlxUuYFZgc_2uC7jImXaAiAUFawz7SoJjX26CZ2R4mpMtkH_3IR4q4b3ExKUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند جنگنده F-35B Lightning II متعلق به تفنگداران دریایی ایالات متحده، هم‌زمان با حرکت ناو USS Boxer (LHD 4) در منطقه خاورمیانه، از عرشه پروازی این ناو به هوا برمی‌خیزد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25094" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏دوستان و همشهریان ⁧ عليرضا سپاهى ⁩ بخاطرش ماشینهاشون رو گل زدن و کاروان جشن دامادی راه انداختند و با سوگ می‌رقصن…
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25093" target="_blank">📅 14:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا: «
ایران تا زمانی که دونالد ترامپ رئیس‌جمهور آمریکاست، هرگز سلاح هسته‌ای نخواهد داشت؛ نقطه. پایان داستان
» روبیو گفت این موضوع
خط قرمز روشن آمریکا
است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25092" target="_blank">📅 14:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401e25df0a.mp4?token=siTxfGdck6JMg49gz3Ae6-eYf_FoPMAzikwCzJC0LR_kuIMPuZ5WbjB0Q-k7s4KUt9j_y8htxnVHtNjnlutaDP3vHmM2bRwLUFk_ruFIMLHagmEa_H1LA2jaGF9V6M3bXhzbUYnRPWmQm9BL4_1B1EdxMwUCcQ4WehxoCH0TNjv6iQB6Pp6RInAjvTMsdYuDLuGLR8dlctiyYEQFjuVoMV00XYAnoSd1N6BF97_IJO0KWTevqdD2rfRRYnS0ft9Tzcqt4P36zCJiycUWK8fA52AXBfDFjyHKfc5HOTdxZNlWdRBY3MJOsBrQiWnncHM0hMmtEymrGyzKieOyfks-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401e25df0a.mp4?token=siTxfGdck6JMg49gz3Ae6-eYf_FoPMAzikwCzJC0LR_kuIMPuZ5WbjB0Q-k7s4KUt9j_y8htxnVHtNjnlutaDP3vHmM2bRwLUFk_ruFIMLHagmEa_H1LA2jaGF9V6M3bXhzbUYnRPWmQm9BL4_1B1EdxMwUCcQ4WehxoCH0TNjv6iQB6Pp6RInAjvTMsdYuDLuGLR8dlctiyYEQFjuVoMV00XYAnoSd1N6BF97_IJO0KWTevqdD2rfRRYnS0ft9Tzcqt4P36zCJiycUWK8fA52AXBfDFjyHKfc5HOTdxZNlWdRBY3MJOsBrQiWnncHM0hMmtEymrGyzKieOyfks-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
«حتی کشورهایی که
به‌طور پنهانی به ما می تازند
، در خفا می‌گویند: «آنها (جمهوری اسلامی ) باید سقوط کنند؛
آنها همه ما را به ستوه آورده‌اند.
»
«ما اطمینان حاصل خواهیم کرد که
آنها سقوط کنند
… و
آنها سقوط خواهند کرد.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25091" target="_blank">📅 13:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da597a552.mp4?token=ugORIw_AXmPDrOjzK-7ofPkX2tG4J6HeWH5BK3ihzHwwCFE1egqcO_HvyqpkpChE2eSHERv1JTQRfmYMUOlSUu-Cs0yLmgHLZptknMTRlHds-ey31iDWFU-XkZ2R0ja7gl-NsaPckcPGNf5pkDzhz4vZdo7lOhh_vFZ--kEzaRtOT3SEnxtWtJomw_VMoZmZHVEEtk3O6SUzd3f8j0I7X0JCKM-csnIlu0wA_W63WmzNHTwyjqncvqxQgR49lEjScy6vN5ymjlBRn9a6adkc5ybe3gzPsWQp33F120d4dG3v44x0N-f_pmTGo_DJLRkM2AcHds6d3eUxyLLJA-XUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da597a552.mp4?token=ugORIw_AXmPDrOjzK-7ofPkX2tG4J6HeWH5BK3ihzHwwCFE1egqcO_HvyqpkpChE2eSHERv1JTQRfmYMUOlSUu-Cs0yLmgHLZptknMTRlHds-ey31iDWFU-XkZ2R0ja7gl-NsaPckcPGNf5pkDzhz4vZdo7lOhh_vFZ--kEzaRtOT3SEnxtWtJomw_VMoZmZHVEEtk3O6SUzd3f8j0I7X0JCKM-csnIlu0wA_W63WmzNHTwyjqncvqxQgR49lEjScy6vN5ymjlBRn9a6adkc5ybe3gzPsWQp33F120d4dG3v44x0N-f_pmTGo_DJLRkM2AcHds6d3eUxyLLJA-XUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
«اگر ما اقدام نکرده بودیم، بمب‌های اتمی ۱۰ میلیون اسرائیلی را نابود می‌کردند. ما دود می‌شدیم و از بین می‌رفتیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25090" target="_blank">📅 13:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی ارتش ایران:
«اگر لازم باشد، بزودی عملیات‌های پیش‌دستانه را آغاز خواهیم کرد تا دشمن را از هرگونه تجاوز بازداریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25089" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وال‌استریت ژورنال:
رادیوی دریایی به خط اصلی ارتباط میان ایران، آمریکا و کشتی‌های تجاری در تنگه هرمز تبدیل شده است. بر اساس ده‌ها فایل صوتی بررسی‌شده توسط این روزنامه، در برخی موارد خدمه کشتی‌ها از نیروهای ایرانی و آمریکایی می‌خواهند به آنها شلیک نکنند. از سوی دیگر، نیروهای آمریکایی از طریق رادیو به برخی شناورها هشدار می‌دهند که در صورت ادامه حرکت، هدف قرار خواهند گرفت. این فایل‌های صوتی همچنین نشان می‌دهد
اختلاف زبان، سردرگمی خدمه کشتی‌ها و هشدارهای نظامی در تنگه هرمز، فضای بسیار پرتنشی ایجاد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25088" target="_blank">📅 13:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاهزاده رضا پهلوی: به مردم اسرائیل: در سومین سالگرد ۷ اکتبر، در غم، یادبود و همبستگی در کنار شما ایستاده‌ام. ما هرگز کسانی را که به قتل رسیدند، رنج خانواده‌هایشان و بازماندگان این جنایت را فراموش نخواهیم کرد. جمهوری اسلامی که حماس را مسلح و حمایت کرد، همان…</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/25087" target="_blank">📅 13:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای تابناک:
امارات ۴ زندانی ایرانی را به اسرائیل تحویل داد. یک منبع آگاه مدعی شده است که امارات از طریق ابوظبی، ۴ نفر از ایرانیانی را که در این کشور بازداشت بودند، به اسرائیل تحویل داده است. تاکنون جزئیات بیشتری درباره هویت این افراد یا علت بازداشت آنها منتشر نشده است.
این خبر فعلاً از سوی امارات یا هیچ رسانه دیگری تأیید و منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25086" target="_blank">📅 13:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پرتاب دو دستگاه آبگرمکن گازوئیلی پر صدا از کرمانشاه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25085" target="_blank">📅 13:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار | تحلیل بازار: برخلاف برداشتی که ممکن است از حرکت امروز بازار ایجاد شود، ریال ایران فعلاً وارد یک روند پایدارِ تقویت نشده است و آنچه در بازار دیده می‌شود بیشتر می‌تواند ناشی از دخالت ارزی، عرضه دلار و اصلاح موقت پس از جهش اخیر باشد. هم‌زمان،…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25084" target="_blank">📅 13:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اتاق جنگ با یاشار | تحلیل بازار:
برخلاف برداشتی که ممکن است از حرکت امروز بازار ایجاد شود،
ریال ایران فعلاً وارد یک روند پایدارِ تقویت نشده است
و آنچه در بازار دیده می‌شود بیشتر می‌تواند ناشی از
دخالت ارزی، عرضه دلار و اصلاح موقت پس از جهش اخیر
باشد. هم‌زمان،
افزایش قیمت نفت، تقویت دلار و رشد بازده اوراق آمریکا
به دارایی‌های پرریسک مانند بیت‌کوین فشار آورده و حتی طلا نیز تحت فشار قرار گرفته است. بنابراین حرکت امروز بازارها بیشتر با یک موج
ریسک‌گریزی و تغییر انتظارات نرخ بهره
سازگار است تا تغییر بنیادی در ارزش ریال. در چنین شرایطی،
کاهش موقت نرخ دلار را نباید به‌تنهایی نشانه تغییر روند بلندمدت تلقی کرد
؛ اگر عوامل بنیادی فشار بر ریال تغییر نکنند، بازگشت دلار به سطوح بالاتر همچنان یک سناریوی حتمی است. بنابراین فروش دلار صرفاً به امید اینکه این کاهش کوتاه‌مدت به یک روند پایدار تبدیل شود، تصمیمی اشتباه است هیچ رونق اقتصادی صورت نگرفته و نمیگیرد و اوضاع به سمت جنگ میرود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25083" target="_blank">📅 13:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به یاد قربانیان بی‌گناه حمله تروریستی ۷ اکتبر @WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25082" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91c52f407.mp4?token=TdORjYTrI9TWr-vlqHgmswNMykiWBcuv4CCKfjHN9uJ4oNUIcQMZnjtZ3a0OspLlYkl_vsgzQ2gfJ-cMThDgaeRMlPqXwERRdU7UlehRXRuZ-GXRWA1XqaMPp5eqLo4_ae2KWy_Twdx7Qx6Ah0tSbjnDUsApujMpdQQeJYUb2Yny4vwMIbT_w2tTYGJNye2N-PWZNOSV7jkpPnPkKVGUvt5S-9K30LaJFzB1IjZrDdDZ6ahflXy7Tk3bnv_MaSSlbJL9E4FDlT7A0LX_oq_SFqkCyKH3Vr0SzKJ4USXQyzRakVHvQ4mXEKaGJJzSYhnyI0cTgOjOay4HQt3HKG8M4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91c52f407.mp4?token=TdORjYTrI9TWr-vlqHgmswNMykiWBcuv4CCKfjHN9uJ4oNUIcQMZnjtZ3a0OspLlYkl_vsgzQ2gfJ-cMThDgaeRMlPqXwERRdU7UlehRXRuZ-GXRWA1XqaMPp5eqLo4_ae2KWy_Twdx7Qx6Ah0tSbjnDUsApujMpdQQeJYUb2Yny4vwMIbT_w2tTYGJNye2N-PWZNOSV7jkpPnPkKVGUvt5S-9K30LaJFzB1IjZrDdDZ6ahflXy7Tk3bnv_MaSSlbJL9E4FDlT7A0LX_oq_SFqkCyKH3Vr0SzKJ4USXQyzRakVHvQ4mXEKaGJJzSYhnyI0cTgOjOay4HQt3HKG8M4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو، وزیر امورخارجه: اقتصاد ایران در آستانه رسیدن به وضعیتی قرار دارد که تعداد بسیار کمی از کشورهای جهان تاکنون از نظر شدت وخامت اقتصادی تجربه کرده‌اند آنها مردم ایران را در شرایطی قرار داده‌اند که اکنون در آن به سر می‌برند
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25081" target="_blank">📅 12:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارک لوین درباره خبر (نکشتن ده نفر برای اداره آیندهی ایران توسط سیا) : «نگرانم که سیا حتی بیش از حد محتاط و ریسک‌گریز باشد و همچنین با مسلح کردن مردم ایران مخالفت کند. این موضوع بسیار نگران‌کننده است.» @WarRoom.</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25080" target="_blank">📅 12:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">العربیه: نیروی هوایی یمن بامداد چهارشنبه ۱۵ مهر، در پنج حمله
انبارهای موشک‌های بالستیک، پایگاه شلیک موشک و مخفیگاه‌های سلاح حوثی‌ها
را در اردوگاه ماس و اطراف آن در شمال مأرب هدف قرار داد. در منطقه مفرق الجوف نیز تجهیزات نظامی و یک نفربر حوثی‌ها که از صنعا برای تقویت جبهه‌های الجوف در حرکت بود، هدف قرار گرفت. هم‌زمان درگیری‌های شدیدی میان نیروهای دولتی یمن و حوثی‌ها در جنوب‌غرب تعز ادامه دارد و نیروهای دولتی چند ارتفاع راهبردی را تصرف کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25079" target="_blank">📅 12:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">روبیو، وزیر خارجه آمریکا: ایران فرصت‌های متعددی برای توافق درباره برنامه هسته‌ای خود را از دست داده است. ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ترامپ اجازه نخواهد داد ایران با تلاش برای خروج نیروهای آمریکا از منطقه به این هدف برسد. نمی‌توان پذیرفت یک کشور به‌تنهایی کنترل یک مسیر مهم دریایی را در اختیار داشته باشد؛ باید منابع و مسیرهای متنوعی برای تأمین انرژی وجود داشته باشد. تنگه هرمز باز است و حجم نفت عبوری از آن اکنون دقیقاً برابر با میزان پیش از بسته‌شدن تنگه است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25078" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز: بیت‌کوین امروز حدود ۱.۷۶ درصد کاهش یافت و به محدوده ۸۴ هزار دلار رسید؛ اتریوم نیز حدود ۳.۳ درصد افت کرد و به محدوده ۲۶۱۰ دلار رسید. تقویت دلار، افزایش بازده اوراق خزانه آمریکا و نگرانی‌های ناشی از تشدید تنش‌های ایران و خاورمیانه از عوامل فشار بر بازار رمزارزها هستند.
بیش از
۴۰۰ میلیون دلار موقعیت لانگ
در بازار کریپتو لیکویید شد و بیت‌کوین در فاصله حدود ۲۰ دقیقه نزدیک ۲ هزار دلار از ارزش خود را از دست داد. مجموع لیکوییدیشن‌های ۲۴ساعته بازار به بیش از
نیم میلیارد دلار
رسید.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25077" target="_blank">📅 11:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbFwuYEFr5AgovsE1PXGzmG9mFjgNoS6X8P5eXUuQNT6_xw9ZFH6DwZqPimLROfZzjvxVI12W93Er_WT-nd6uOTRsi9o9gwAtCxf5T5Z5SlFpurgvIz6nQl5aJGnh1DlABC6y3dqNemsMIyYvBp7lt2ofvHbQYFX8SnmJQJoRNLc6_PCKH_saEBWptGWfMaTVz__aCUFvh6GPJr0UInkMpzNfJpobS52Q27pOvswYjKqGcHxY4ntlzxBLHOyOKa3CIlGChXvO29t5WhZ-hcf6ojeUmYk0-fgvXfSUSSOYIEeO1HVWnKRevzXReM4Z2lsCl3X2SIzPcwpQtWxbGkwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جروزالم پست:
تصاویر ماهواره‌ای از سایت هسته‌ای «تأسیسات اتمی لویزان» (معروف به تأسیسات مژده) افزایش رفت‌وآمد و عملیات عمرانی را نشان می‌دهد؛ این سایت از سوی اسرائیل به فعالیت‌های مرتبط با
توسعه تسلیحات هسته‌ای ایران
مرتبط دانسته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25076" target="_blank">📅 10:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع هندی اعلام کردند یک کشتی تجاری با پرچم پاناما امروز، ۶ اکتبر, ۱۴ مهر هنگام عبور از نزدیکی تنگه هرمز و سواحل عمان هدف یک پرتابه ناشناس قرار گرفته و ۱۱ خدمه هندی زخمی شده‌اند. تاکنون هویت عامل حمله به‌طور رسمی اعلام نشده ولی این حمله به سپاه نسبت داده…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25075" target="_blank">📅 10:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25074">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فایننشال تایمز:
به دلیل خطر عبور از تنگه هرمز، ناخدای نفتکش‌ها اکنون تا
۱۰۰ هزار دلار در ماه
و حدود ۵۰ هزار دلار پاداش برای هر عبور دریافت می‌کنند؛ نرخ بیمه خطر جنگ برای برخی نفتکش‌ها نیز به حدود
۲۰ میلیون دلار در هر سفر
رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25074" target="_blank">📅 10:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079c75e928.mp4?token=pfB_dmojMpV6wqJAaN5P9JsGXaCS0bQvncJuOj_7l2MSPWLExe_e4CSpa5gdwOoMm5lnNKexCDY3itb7xRYGWk5DOl-0JbUkbWXbK_3UeZHlFIFGIvGmnRgrocvkSpJ3CxOVuiNQsXEJ8Nu5F-uxgk2Q945U05XDpnpVITrV0OVW4xthQ21yJt7TE2t0M769hXC_VCY0sfM_PFJ15xMegEPWE_MohvAQ6_vw2BQ2mzxCJaflsdhWgmH6YW4nt0v2-unwllX8OABdEZqfIUmSh2hvJ8FTb_28rMatkL77JiJSieMYc7GZ7eBP-lw1nD2o2aNDBDXtnuyAAxO_yIY87w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079c75e928.mp4?token=pfB_dmojMpV6wqJAaN5P9JsGXaCS0bQvncJuOj_7l2MSPWLExe_e4CSpa5gdwOoMm5lnNKexCDY3itb7xRYGWk5DOl-0JbUkbWXbK_3UeZHlFIFGIvGmnRgrocvkSpJ3CxOVuiNQsXEJ8Nu5F-uxgk2Q945U05XDpnpVITrV0OVW4xthQ21yJt7TE2t0M769hXC_VCY0sfM_PFJ15xMegEPWE_MohvAQ6_vw2BQ2mzxCJaflsdhWgmH6YW4nt0v2-unwllX8OABdEZqfIUmSh2hvJ8FTb_28rMatkL77JiJSieMYc7GZ7eBP-lw1nD2o2aNDBDXtnuyAAxO_yIY87w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد
قربانیان بی‌گناه حمله تروریستی ۷ اکتبر
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25073" target="_blank">📅 10:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بر اساس گزارش جدید منابع حقوق بشری، جمهوری اسلامی از زمان اعتراضات ژانویه(دی) به‌طور میانگین
نزدیک به دو نفر در هفته
را در پرونده‌های سیاسی و امنیتی اعدام کرده و ۱۹۴ نفر دیگر با حکم اعدام روبه‌رو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25072" target="_blank">📅 09:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایرنا:
تهران به بحرین و دیگر کشورهای منطقه هشدار داد اجازه استفاده از خاک یا حریم هوایی خود برای حمله به ایران را ندهند؛ ایران تهدید کرده در صورت تکرار چنین اقدامی پاسخ خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25071" target="_blank">📅 09:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbvQ4ZaDWwb5nIM_mi_-T_5hSTAOC3wEfwnfm2gZdnF8mRt5BN4TV4dQpSVefysTKjy5WqyCA3nMzDPTKk17gz49JLAzqy1neIvSQ6m_u8uCJEocF2ewl0tmUE8qPYisY9vt8EhYlrxU5G85tKsvwU0VfsP_81hbfJ4QO2OXj_nNxLve0oyDb2r8nQwnjxheSwEBSmiij3w6zZrHHKIkP5HoR4ySE-37lXAHe3xrau7jKNmt2SgMC_XHP2wxJKSIIeJdTWK8cdLAxTjx3AqLtG_awmsQCcF4gjk2V-ZoraalFfpdAhMoCAhh9magMHXmlz6PsWCcyC2Ibf-canpHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع نظامی اسرائیلی تأیید کرده‌اند که نیروی هوایی و فضایی اسرائیل یک رزمایش بر فراز ایران انجام داده است.
در این رزمایش، جنگنده‌های پنهانکار
F-35I آدیر
شرکت داشتند و یکی از تانکرهای سوخت‌رسان جدید
KC-46A
اسرائیل، در حریم هوایی عراق به آنها سوخت‌رسانی کرده است.
این نخستین گزارش از استفاده عملیاتی از تانکرهای جدید KC-46A اسرائیل برای پشتیبانی از F-35I در یک مأموریت دوربرد بر فراز ایران است. پیشتر رژیم حتی تایید کرده بود که جنگنده های دشمن تست ورود به ایران را انجام داده‌اند و پروازها هم کنسل شدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25070" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25069" target="_blank">📅 09:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZq7HIbxeVa8OmCkVU40mdA9xmt9y0dqotdo1A6xoBBjAM53yoXYqlArzXnnwwngsP2RUwRUmupkR0MGyocjoYqRd6_qeOTAoiDDqN3xuDSYXXGJN8ODDFbJcLTOFPHvk2H5eotFgNAxDHRvDlKuaLWSPmqtIus-STfNP_RZDBuVWCVFp2_nF8LI9t-EanSa2_S5-zC7_FFyoH8vRcG1r3iY5Zf5nXF03eDGbiIfZwNcZsJF8SStQ3h8G6RkgXmBy1jW3jlMAIcgVNBkABTiss0LvCEgwryZz-tAWmAJVz1AjZHo7bPM-zvcco6OOjGK_UnadgT9BTCQFpEsPW6PWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل : سازمان سیا فهرستی از حدود ده مقام ارشد ایرانی را که نباید هدف ترور قرار گیرند، به اسرائیل ارائه کرده ، چهره‌هایی که واشنگتن معتقد است «می‌توانند نقش‌های کلیدی در دولت آینده ایران ایفا کنند». @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25068" target="_blank">📅 09:19 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
