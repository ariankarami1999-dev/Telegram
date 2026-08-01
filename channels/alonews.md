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
<img src="https://cdn4.telesco.pe/file/GPKg24XXa2wmqLwmi5fNgrEi-pVT83114BbcAyoLh7HZKJ8aVCSz2j0EY3VXAGrp53MJqDGSEiQr2DX8HV66MYe01mRg8WrBDu_bIrUKr6ZaG-RY6nh7SoYHZETvQMfyGy8TA4jsJ6zljki5flxExCKkFBEBh12BTSqAyFMCmbdxaPKFgpWiFQRTDHUQkWpwGwtbOddPqMmx-wN3dNxEJvzf-C-j2EkaaMV-q33xEPIL5WSb1gMe4ReGLq4b6EdWjiXK7k0E0iB7a1Of8mPmGwnNkAxPDHVkprfzLKvol_X-LT7cXKxvXfrvpifJv55dwCxpoaMTZtDh0Gk5NPTTcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 15:08:29</div>
<hr>

<div class="tg-post" id="msg-139104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بلومبرگ: کاهش ذخایر، بحران سوخت در ایالات متحده را تشدید می‌کند؛ آمریکایی‌ها با موج جدیدی از افزایش قیمت‌ها مواجه هستند، بدون اینکه از بازپرداخت مالیات فدرال که در دوره افزایش قبلی بار را کاهش داده بود، بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/139104" target="_blank">📅 15:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139103">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287ba1985f.mp4?token=YtrY7aRP1NPgUp99zUzdM1yYRQzRF0-z3yRRKyUnbyY3IUqmxjZw6jPT2qsnM5hKFytmqQgXEAX8udmf8HGXu-cu4Z-fTgIU9FyzxVp1EZJb-h8ruZYbWE4lKkaE4hHUE0FttMN5Bl6zIl7s4sMPyVfcwyG2JVkXe3LYe5abtKPcO4lv7xqhn9eGTfwnXRIySXQXrgo5323PcoYdVc_oRwpXxmqTlOgJv2AORoVRWU8WxTJl04VtItTWOOHg494F7IJJTuwTujqaq8WQLGMl1107qqcTT3w6NnXsRZBLy6_Vmx0h2KDBhw1I8XooDecDU_-699ieR6BW6_YYptTYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و قبرس عملیات گسترده‌ای را برای مختل کردن سیستم موقعیت‌یابی جهانی (GPS) در سراسر هر دو کشور آغاز کرده‌اند که دامنه این عملیات‌ها به لبنان و سوریه نیز کشیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139103" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139102">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال: ترامپ، در ساعات پایانی حضورش در باشگاه گلف خود در نیوجرسی، طرح‌های جدید حمله را که به او ارائه شده بود، تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/139102" target="_blank">📅 14:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139101">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / سفارت آمریکا در اسرائیل: آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139101" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139100">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سفارت آمریکا در عراق: به شهروندان خود در عراق توصیه می‌کنیم هوشیار باشند و از دستورالعمل‌های مقامات محلی پیروی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139100" target="_blank">📅 14:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139099">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139099" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139098">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه امارات و انگلیس درباره کاهش تنش‌ها در خاورمیانه و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139098" target="_blank">📅 14:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اداره کل هواشناسی استان تهران نسبت به بارش باران، وزش باد شدید موقتی و گاهی رگبار و رعد و برق در مناطق شمالی استان تهران هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/139097" target="_blank">📅 14:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قیمت دلار به ۱۹۴.۲۰۰ تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139096" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139095" target="_blank">📅 13:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1VQzmnKm63z0sHI0ZeZXWv151duACtLxQo6dFbs8lamFQUyngCZVUBd0jsDpfFt5SSKCzCq_bKMnCMf4T6BP0H8d3uFYlke55Qws5_mamDkrwsC6UBb8s4Yp7FMPqvaW0ZJL4jlTBheY8wW3N_jKz56fHF5FkiSei_itTXs2bhGB8fQ9TL_HTGMsDvVmndSCteMZD0i6TyOmH7CGhT-SVDnTQ12m7PyWNRzlLiIO8n2zh-lF2D5Ldnrbox9tZXQ1_w0yQuwOnB6V-_DL4HdM2cndKy3zyB0MQHKQEHkS_nrDTqO16UJQcfYDCX83lLbH0B2LTtuG_LlAMdq2fnnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: اگر به ایران ضربه‌ای زده شود، کل منطقه و تاسیسات آن را به عصر حجر برمی‌گردانیم؛ به نفعتان هست که حماقت نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139094" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/139093" target="_blank">📅 13:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=fAw0uks55jvVsm9c8SjH6ic-UPz2RuIy7GzFp3pDZgzlEu-m_YVw-38d4GzuPxMdSjzfqCeg3bPP8Vyx6CY7_UYddPMn-m_MK_ei0zKcYM-VJ7fjP2_m_vZd71ksQsgUjYreApq6Yl9aGT8OOGh6VcL6Ag2HwrPvNfrBmjwRVUqcTmtnlb4uWfNE8JGGMoIh0dH9rRzA1OQVNQ8LCi7jfBmHYN_Mm0ECWi6o81PJwtZPHq7vyhJHSygIrsQmHCYrbpIYQj5s3NY5cl0rE8PRRfNof4PKS0qJdGxj1JERhX_wxCqg7GhURzU0M3VE-7BOtzTGZ8plzARfMduk8FEpeaN-l0oawhE0WOQaOtPO4X-6D4d9rP4vVHD5DltxvB1nqnB7vt6ction8DN1i4SYT24Snq-dXrzKHLeAWYgXv8uMH-fQ8gi25BVT6-l5eyCcj2vL99nu4WB9Jwrnyi0WQdBvnnPhHDmm_uibJ92uhDSR47jrBQIJs8eYgxYcaZAsQDZcofJRWYqrNXtybENEXHPEcvD-zWCPhtYcEypdq5VlIRf1-A_O7kPCkWKHW7OoQuoSjIZfaajftVVHI-BglnFApzfRV1ffXbPK5sYeeWKEdlp9SsrrzAT5kZMhQm7jMMtX9nTAftUFUwpnZAN6pORZ-CRQ-hY9PUmPj5SGCC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139092" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر کشور اسپانیا: شمار پناهجویان [مراکشی] کشته شده در حوادث منطقه سئوتا، به ۶۷ نفر افزایش یافته
🔴
کسانی که به صورت غیر مجاز وارد سئوتا شده‌اند، هرگز اقامت قانونی نخواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139091" target="_blank">📅 13:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / پاکستان به ائتلاف دریایی عربستان پیوست/مقر این ائتلاف در عربستان سعودی خواهد بود و کشورهای عضو اولیه آن شامل عربستان، پاکستان، کویت، بحرین، قطر، ترکیه، مصر، اردن، یمن، بنگلادش، نیجریه، سودان، جیبوتی و سومالی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139090" target="_blank">📅 13:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139089">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
درگیری دو باربر در بازار تهران بر سر جابه‌جایی یک بار، به قتل یکی از آن‌ها منجر شد. مردی حدود ۴۵ ساله پس از مشاجره با همکارش، بر اثر ضربات چوب جان باخت.
‏
🔴
کارآگاهان پلیس آگاهی تهران اعلام کردند عامل جنایت بلافاصله پس از حادثه از محل گریخته و تحقیقات برای شناسایی مخفیگاه و دستگیری وی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139089" target="_blank">📅 13:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc1_TyUfdxvQaTQDieRKvXcUu23b6UmPi0HURQ-PwQMqOre66szHCu-mRjxZGXzIMwrWLcZgwyuBi3ZTm8HrTA6zqjnWMsjMnxRqEp-6hTyWHzQcQWxdhjK656PoAQZ2DhuU7vFvCkVHCTO9sPUupXaNc8bs36QSDhllM6UcbIHA52AaSfKJsNV21PTTTJKjzeYv02QqDZmX7byjCFG8uuWJW6EFvMKGL-k2TUyKJWYVBoQ8JBJWJqbDILNcoDzuaEdOwEZyd-ZfiirTGbjg9sFXss00CJs7rmZ3GnCWjUHlfmw1XzU7WU7K8-KfXIYXE-RTltrCBYyM-9ix9EiEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / مجلس با رأی اکثریت، وزیر آموزش و پرورش را به استیضاح دعوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139088" target="_blank">📅 13:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دو کافه دیگر در تهران پلمب شدند؛ مراسم بزرگداشت شاملو نیز لغو شد
🔴
دو کافه عمارت منشأ در خیابان نوفل‌لوشاتو و کاما در تقاطع سهروردی و عباس‌آباد پلمب شدند.
🔴
همچنین، مراسمی که قرار بود به مناسبت صدمین سالروز تولد احمد شاملو و هم‌زمان با انتشار مجموعه جدید آثار او از سوی نشر چشمه برگزار شود، بنا به اعلام برگزارکنندگان، «به دستور مقامات» لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139087" target="_blank">📅 13:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUV5sTXuG-tMYXiWTerKO9qeP6Q85meK8vOzbHo2cC9pNMztMYrKa4ndIQbXRx4yG21s_TY0MJo5_J0N4QPlP-f0lfw0fO3g4tBHhB4YYYSdFaaa041yH5O6dk52NsehcGl1J173D8nbD-b8AuhX_baeI0HIBRvcpyyRyeYtKWv8q26mkKU4_YffyDEjaXvP4WmOL210MLyFTPvrR8NOhpGmlVKw6tucgbDJnsBtCp-ASrl-1wM1jBfa0103sgyC_O-txVVRyQynkd5SWCFqXqZqZmMxLj9E7i_QpO7zIFQB8r7HkbsDmDBI5_GG4WZ4vhETWxyf0rwa9G3CAd7TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون سابق بازرسی قرارگاه مرکزی خاتم الانبیا در واکنش به تهدید های ترامپ:
اگر به ما تعرض کنید، سیلی محکمی دریافت خواهید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/139086" target="_blank">📅 13:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا از استقرار راهبردی ۴۰۰ نیروی هوایی خود در عربستان، کویت و بحرین خبر داد؛ این نیروها از ماه مارس برای تقویت پدافند هوایی، افزایش توان هشدار زودهنگام و حفاظت از زیرساخت‌های راهبردی کشورهای حاشیه خلیج فارس مستقر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139085" target="_blank">📅 12:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بلومبرگ: بعد از تهدیدهای حوثی‌ها
دست‌کم ۶ نفتکش عربستان به‌جای عبور از دریای سرخ، از دورِ آفریقا می‌رند
🔴
این مسیر حدود دو هفته طولانی‌تره و نشون می‌ده
🔴
نگرانی‌های امنیتی و اختلال در حمل‌ونقل نفت توی منطقه داره بیشتر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139084" target="_blank">📅 12:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ذخایر استراتژیک نفت آمریکا (SPR) هفته گذشته با کاهش ۳.۸ میلیون بشکه‌ای به ۳۰۸ میلیون بشکه رسید که پایین‌ترین میزان از مارس ۱۹۸۳ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139083" target="_blank">📅 12:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اکونومیست: رئیس‌جمهور آمریکا در موقعیت دشواری قرار گرفته است
🔴
تشدید جنگ، اقدامی پرریسک خواهد بود و پذیرفتن کنترل ایران بر تنگه هرمز نیز در داخل آمریکا برای او شرم‌آور و در برابر متحدانش در خلیج فارس غیرقابل‌قبول است.
🔴
به‌نظر می‌رسد فعلاً ترجیح داده است برای خریدن زمان، دست به تعلل بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139082" target="_blank">📅 12:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آژیرهای خطر در کی‌یف، پایتخت اوکراین به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139081" target="_blank">📅 12:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efghBcsxBMAtbfjvpwOCwKVpR38JQ_08OhbDx4OkCK3LojxpwGiz_i9LtnibQ4LxUAdiPtUFjKlHtZG1wahcq7qLQ9N7DLaJ15-KjDK53S9gW_prrEnnNzHrmGv2_FF15j-pp3eoNg_1z7VwBseiksUCvv0BMsS6DMPuEx-nblvcUb5IjLMLyHsttEIxznUlVXRK4D5QwlM-U7s-GaoITbK6lKPtS1h6PmqYQdCLEg6z4XcPJHA4-HkIN0-hwk3gSGrrb_5X5Ecjbyw1iXHBelUS4AR-9wBZ_Fh6N33N7j8VR7CMZwRJ2Y7Yqie0zfjeVDBz9N6VaBKn1kXxcVe6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده نزدیک به جلیلی: باید برای ما مسئولان پناهگاه‌های امن تو کوه‌ها ساخته بشه تا تو بمبارون آسیب نبینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139080" target="_blank">📅 12:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم : هر کشوری که خود را سپر دفاعی آمریکا قرار دهد، در آتش جنگ خواهد سوخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139079" target="_blank">📅 12:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سفارت آمریکا در اردن از شهروندان این کشور در خاورمیانه خواست با توجه به احتمال تشدید تنش‌ها، خروج از منطقه را در نظر بگیرند یا برای ترک فوری منطقه آماده باشند.
🔴
این سفارتخانه هشدار داد افزایش تنش‌ها ممکن است به لغو پروازها، بسته شدن حریم‌های هوایی و ایجاد اختلال در سفرهای منطقه‌ای منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139078" target="_blank">📅 12:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139077">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3f1b61e.mp4?token=I47piY-i9VNqbMm_QfEPYz4IelK0tLWLGs5U3JHNaplswGtPlnKqUvY0lCCHt45RyIKKUQnzCK8pbPxi8QOmzG10smSYVJY_f4rgOMf01iz4n4tSehqSSv1RMd1cNjFLoUYK2XiuW6vOb8jAYPRyiCTXSB_KmddS0pGbIpGzilwbAXJzgIfKZfb6fbHH5kdELmKr5-J1EU1l-R-7eNkelZTT1ndw0ZwHGbtDiP2cya5gzbOaBa_Yq4SXgxrUSpACujbWJtO-G4n5w3RIwT8HHS_G-76elMd_D4flAJvtRXo73WrCfXN6JawNumz3flR098wAmfMztxkSKSulxPjEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3f1b61e.mp4?token=I47piY-i9VNqbMm_QfEPYz4IelK0tLWLGs5U3JHNaplswGtPlnKqUvY0lCCHt45RyIKKUQnzCK8pbPxi8QOmzG10smSYVJY_f4rgOMf01iz4n4tSehqSSv1RMd1cNjFLoUYK2XiuW6vOb8jAYPRyiCTXSB_KmddS0pGbIpGzilwbAXJzgIfKZfb6fbHH5kdELmKr5-J1EU1l-R-7eNkelZTT1ndw0ZwHGbtDiP2cya5gzbOaBa_Yq4SXgxrUSpACujbWJtO-G4n5w3RIwT8HHS_G-76elMd_D4flAJvtRXo73WrCfXN6JawNumz3flR098wAmfMztxkSKSulxPjEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه دستگیری سارقان مسلح منازل چهاربا
غ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139077" target="_blank">📅 12:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e157b43618.mp4?token=ZLb5IgR7LQW5n4EynIEdebzq9UcKCz8jOwc7GqiMZFOQy5Vx2q0yAVHcuaLRd_43q17fWmsHtqzazJPBVY1V_Xe_TcyPVeFbrkqDI9qFNIpj8rYYPAzrEs7Z9faq62ScJyKMlrLyTi8FguUlZaSCQ0Hx6P0tYEeTsCKQ4jxHCRN19ov7rj5IOsShsRqvw2RK3kxI9RhHRhIgU0hcgsmuy214SmB2IRBJPUUTFjN_RXh2JN2Smbxxd3gw37H5WrZoP1rXQMboV5xKB9whK8LAPhWZtEHRC5nt6SaNZkabOsbuJNZsrV4NYU0Bp4uywTgfXFP9je71vAJ7GDra7JVLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e157b43618.mp4?token=ZLb5IgR7LQW5n4EynIEdebzq9UcKCz8jOwc7GqiMZFOQy5Vx2q0yAVHcuaLRd_43q17fWmsHtqzazJPBVY1V_Xe_TcyPVeFbrkqDI9qFNIpj8rYYPAzrEs7Z9faq62ScJyKMlrLyTi8FguUlZaSCQ0Hx6P0tYEeTsCKQ4jxHCRN19ov7rj5IOsShsRqvw2RK3kxI9RhHRhIgU0hcgsmuy214SmB2IRBJPUUTFjN_RXh2JN2Smbxxd3gw37H5WrZoP1rXQMboV5xKB9whK8LAPhWZtEHRC5nt6SaNZkabOsbuJNZsrV4NYU0Bp4uywTgfXFP9je71vAJ7GDra7JVLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔴
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔴
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم گرینلند می‌خواهند کاری انجام شود؛ گرینلند از دیدگاه ما مهم است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139076" target="_blank">📅 11:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5hnx50ipo616zIr1xEAbZfIV-Q1_cEmxIKkWia6EGcnHDi4qo7gHQmG7IsmyIX6ph7RWAVY2MI9IyjNz3MhO1EAlq3cw2k8o6HhdWEk3RjbKXXTqdFIncldfvAw6qfcdIPp9_mb77o9BHge-n20WlY6aifJhLqKSgnlgIJJqvFzFQS_kPbBISqOIIHRPTYEHhv2u8QPxfpklOmyV-VYUhG3itekJ5wz3XRbnLwnN2orcAvfk0hP_yvxCiR4nBwQVy74LIKTA_TedBZzaeI7hkuHtYNsKd3-aL4GJRC1BoFcWpC3Vf7FfI1vEA4CFkEFQzc3OEMsLyL1RqjUz51bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTQXgF4mvg8Whl-N0297JjrIEHr2hvkfyDndqgn0HeqECqBfvTdT05B9Fv0gBH-5Czr4t_ySbRnAS59PPD9yBqJSGulPOS-TBJyzl53dM8ZbELKXLGqe5gWIlxMHhkWyJOVo-G4tFs5BEAY7H3HGmZSxI2qL-dGvce5vc0oqsod5qPpTYkn0ucMBRTWpA6gxgrT19UddxWXe7M8qgnDed2p_ZRtEwRCvOQ88OnBDJ8jwLZDZIy026gNPrcCa7nEPTOQAsO3uNfZWqzRD1u3up2_AovE_12w-5KIdMwOccYh7P0RvYbxMTsL40gxG_dDpI4mHp21yByLC2SrSe9NZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uugs0FMCh8ELZZeNGquCIzFrzvBDavZSjwZSay7zbTwAG7qJ0j-JAbKoi6MSQ3HlWHvRTFfkGy1bT9cABgfHVAiFJnOXrY66mNI0drxwNZKCmezICrNfy-EskXzT-ZTT7RLgwU0FLfiglzDPkdkS2i5_u1ZkWM4ge8pAi-18z-JvCnSm-7SZ8sN3srrBDN9MdkxWr5833_NgVJlzE9E-QSjQWPGaCn9IYvF2omIVfn-0ltJ3YpHmCokWkPnxltP5DuleCehXOUamud5KwezwaWL7OBQmoNumebNqZV2hAsmrJRmj_SeClApOD47tVxSDI4LvuQoZZrDxOPqCqT9VBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrZGH9Nc4h8X9iJK9suS9uRMroqx5QZUAItnT9tGSzSJL6MMfDsBWeHRdW7Bfm817FLFSH6FcOVzhpAt_7txon5bC90yV3coYCyLbuqrsx-GYxZJdmvlAJhnvoaPtN6NJlp_mNmO3egwYIRDek2tHQHeRlNvudZnteRH3Yt7CjRM9JkRMvBKAhlT2pdZDUj0L9NytdxU0XYeG142O_EdsTcZ9VHXyDouZvxZ39NPicI5wZcZlSqtuqNHowZyvMiTq53XZvtieezsmILrxp8kz_GoZxgmJHW6i8PDNU4O3n384Zin9FN9hsAOav-qDZWii72oQuBCrBfHAyXpiWyRiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از حمله‌های دیشب روسیه به کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139072" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
حسین یکتا:  ما قرار نیست قصاص و خون‌خواهی رهبر را به ظهور موکول کنیم ما خون خواهی و قصاص را مقدمه ظهور می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139071" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=cQDZa6NPAjXU7kj8nI0dS_AqgJfPhgro_WHJXtUyulPa8SPdKo7a2WGUbDjWoeGp3EBWFp3HWjauNea_XQD4lbNDrgKp7KNRoJPof7KDaIb5t-7O8PdAhpIq26FkWg-oG18eOYHPSwJ8yNSUSOps07RLaLDslCg-f6TjRTC6B0zYCFjqCYIaEBM9qIWflS5uziFSAcEzmT9BctfmpF_MogaDubn5dikaQckjxHFpXvDCDl2WaZNwlVbfelkwuzVTJNlYi3GpD4jvDQDms1qg_Gfo97FQyK_U9i_2cvYYOYInKRWCgUUkEElnVw8BzdpIsl0JeWpyNYR7s37VCTDVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=cQDZa6NPAjXU7kj8nI0dS_AqgJfPhgro_WHJXtUyulPa8SPdKo7a2WGUbDjWoeGp3EBWFp3HWjauNea_XQD4lbNDrgKp7KNRoJPof7KDaIb5t-7O8PdAhpIq26FkWg-oG18eOYHPSwJ8yNSUSOps07RLaLDslCg-f6TjRTC6B0zYCFjqCYIaEBM9qIWflS5uziFSAcEzmT9BctfmpF_MogaDubn5dikaQckjxHFpXvDCDl2WaZNwlVbfelkwuzVTJNlYi3GpD4jvDQDms1qg_Gfo97FQyK_U9i_2cvYYOYInKRWCgUUkEElnVw8BzdpIsl0JeWpyNYR7s37VCTDVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: آمریکا و اسرائیل برای شدیدترین بمبارون علیه ایران، طی روزهای شنبه و یکشنبه [امروز و فردا]  آماده شدن و ترامپ دستور حمله رو صادر کرده
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139070" target="_blank">📅 11:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرنگار نظامی وب‌سایت "والاه" اسرائیلی:نشانه‌ای دیگر از تشدید قریب‌الوقوع تنش‌ها در خاورمیانه... ایالات متحده خواستار احتیاط و هوشیاری بیشتر شده و از آمادگی برای احتمال لغو پروازها و بستن فضای هوایی، از جمله اختلال در ترددها، خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139069" target="_blank">📅 11:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله پهپادی اسرائیل محله شیخ رضوان در شهر غزه را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139068" target="_blank">📅 11:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3328847f69.mp4?token=gG8bQ_wB_DfLMAbjt7LbwmwVZ5aVxcksZ2-KzmQe2ZObQ8ptbOy_LcwuHEIGtr2sOuza9U4Tm6u1QJEEJccJrreMq81PLgyB8JQnRyiqH4xtHqEHFULVALOqgxEZRXJ7av_mrhqfg594_s2ZkzGl_IrTFDPf7WEaZOTG13FcH66m5nnSyjl4mlO20TIBIRs6FwHcirOYtzK-6fvvD_Q5JkKv4rC8CT4KiSif73OHvBUREt1HHSTz8TtQt_PGikXOiF46MWpx6t3OG8uKMGBciYRbLbFTsyLc1fevqT_K1MjiWTVTZMSMOfP6yyXsStFaOaJn8X_YxWceapJGE4B1VI3NwLswau7T1O36399U3bIFi6V2lyA2loo7zSjD3PHl4-USvTwvjxf4C4lVe03lawFhCkIjdoTeQt1tKyoPrKJ8c12PYDLpOg99B2fUbB7i06sbTZfDU6sx-fNxePnjIuwMl9MFzelQj6lpUymv9SC4RwaP7LhxRYKn0SdV5jNh-8FO2B51eSMMtz3Nop_dZK2vrequJbWIVvbgLUbS29D1QrJe176yoP3ShvDDzpSkjW73k1KL-FN7iGl3XJnwfHkoshNbVQyZWJoKoDcs71uX8xybFRFZY_j2fVHL6UTl5jzv2ESo5LSrMPeB11k84DP_jU_3FKE1fuOaZgao--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورش زندانیان ترک در زندان یونان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139067" target="_blank">📅 11:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW5ltn4dP5mAje2eu01Bt5ctLkWS4yKuQ70vDmVT0GQjejn1s7pxPw6awfhGCGIVM_ThE-fR-ZPhQT_oS0pDkGOPLcqEl2Z9VEJPVMTDo_qty6KAOMRnW7GBnkPAUqB4_QZfysxJmlYHbKJyky-yvP9u9IEO6mMEz0qtJM6BDtuy74jcJ6fr67pgct5WcQe-aJthz_QoEcKslhlRg-GUbvxPWY0UVRftq37T2hK-TkD9B-kCRlVjMnWOVvtXzqAH8DaH8K_Xwwpl8_jdHw1YtC0YQ21CfoXKj0xzYfuFdkApsRqiodDkEe5_BAvAzK269eeDIuOIpwx5li-Y4tkX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت اتاق جنگ اسرائیل :
⌛️
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139066" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مارکو روبیو : طی هفته‌های آینده تلاش می‌کنیم
🔴
ببینیم می‌شه مذاکرات بین روسیه و اوکراین دوباره شروع بشه و این جنگ بالاخره تموم بشه
🔴
البته می‌دونیم هر دو طرف روی یه‌سری مسائل خط قرمزهای جدی دارن و تا وقتی این اختلاف‌ها کمتر نشه
🔴
رسیدن به توافق خیلی سخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139065" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn8y8XDuEqSn21RbGiqhEAspVuq3trRG_jBcf5A56LmU-LWWvPL2NQct-GqZcSNVTOJ6E-fWjYpoVmU60zOkKy0Lq7QUYyXpAMNXA5WnAkeKeuDt1-e7do4egZCvuUHAiHESzv3A0RfPICM6XSmgMxSD1qBuoG-1eXhQGDp_97CQvP7JlSVq3_3MneNO6Luo3vvCKTL1E-YdDPIm_DFQHuzry0lj9qDU-e6ElH3uHJnpVn46eyp1GUqJ2k4enmX_GLsjTVTPg3lyRFuBpJRpzGHJ7Q2N9kWc6FhGJlEBjqIazlQK3-rbZgR9GqTxcDtq0IbvVtacl4jeqXLdwBAN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نیویورک تایمز: بمبی که دو روز قبل بر روی یک خانه در قشم پرتاب شده است حامل یک تن ماده منفجره بوده است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139064" target="_blank">📅 11:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو موفق شد ترامپ را متقاعد کند تا حملاتی را علیه بخش های انرژی ایران آغاز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139063" target="_blank">📅 10:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سی بی اس به نقل از یک مقام ارشد اسرائیلی:  ترامپ و نتانیاهو سه گزینه برای جنگ، از جمله حملات نظامی متمرکز بر مسیرهای زمینی تدارکات، را مورد بحث قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139062" target="_blank">📅 10:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBjTLfOG2kvTlDPBvh9GDQV_h8Q61MPD5YwOnS2sJ126-FsaCuz4OecaSeTFttdDK_6bDH_bNHFWFS4ki6Z8oWwYZKCT0QeOUTgMK8UbgwTDxidaYvh3ayBg9IGUuFezIRpX2YFe_n6taX_glihtFImmTkKXEpmVbKCR9XiDV0SHYPEgxs1jQfIgclf3b78M9tso1pQ6JfUXmSyJ1jxNNJqh_uPwcsWqdr9G6k5IyeeARX4nqS3CWaYehl5rI2fF2PfjwqkdTDdkKqYSazgg8G-ItWUNTq--3BMmodac5oUtXk_33-unmrR6iTxggKC1T50YEZPg0kszJqy0OpXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران با کاهش ۳۰ هزار واحدی در کف کانال ۵ میلیون واحد ایستاد این لحاظ که شاخص هم وزن ۸۰۰۰ واحد رشد مثبت داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139061" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bbc3a7e0.mp4?token=Lq1_qDLF77GL-84wvElJb38z_6bxC2mc95qq0p6SvFznFhGpdYHUhC5XItCmvPWBhZJR3zGn6YrOKFMQLgh3GvV9zSJOpXzUOQTr6mVdH8tUPdu6OYqjJNUKVxokYuXHbHFmoeGH9dYqZm30PBqLL4J75G1dsHPg-f8oouUrvJBGsJoXnCYdc9m8u7MIpvsc3h1lU8gpVzNwIZ-ogmTZxytFbcoVCHC5TZOErWOmpuyAOvwvU9NRlloMBl9QvgDfUC6TMvTDTCqlk1-LmJgeRoODuSFBMy-kG2ELsrDLKYYy0GlVyuchCh9_-3m5XMCPPPIZps_qXXP7tO3j38DGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:  تنگه هرمز متعلق به ایران است
🔴
ما به ورود آمریکا در تنگه هرمز مشکوکیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139060" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=aBqBRY8-67pyPdXoSmHT1Jb0RGuVqFx2BL_SntA2agPipEAZFj803aqTEsDqBxHzLCcmuay_j0-KB-9KKXrwqUgMW3hVAv6HaveCzErgW28lyx8JDUdOjXyXH0tnm6tJcBihUnCRz0qkOJ_Qbjn5ULWakoRpOQgcDXiundm2GQM3iZVJiYVCoyzyYgcoJJou8K4gbBAX3TRNFCl6dx0SpAexIa4Uad7I2DvjY8tlbkOkA2jKHTgKp--5SfbQstZpy32YS8Sp-_R1DCwSY8xKrZqyoBP3h_DY-3jmGWExj4QPvTK-a0FchD7DJXA4-AlCA-gBHrhQozHBUB9ZY2-fhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139059" target="_blank">📅 10:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: ترامپ به‌طور جدی در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است.
‏
🔴
این حملات همچنین ممکن است برای نخستین بار طی چندین هفته، شامل مشارکت ارتش اسرائیل نیز باشد؛ و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139058" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
زلزله ۳.۸ ریشتری بویین‌زهرا را لرزاند
🔴
این زمین‌لرزه ساعت ۷:۱۱ دقیقه صبح امروز در حوالی بویین‌زهرا به وقوع پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139057" target="_blank">📅 10:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4mBrYvyJS889asiVxN0bCfZXl4ncQH-7m6_hK13HlYD5z9n8ol94AOztToHB1BDuhwvN6DTLaTdIzAbbkfbmBV-yEOFSxxhyN8rFbyY70cFnYeofScjD6Jb_74qIrLrbC3YGtZANi1e6yOqCOUxqYnc7axthjnxNfTFUVXbicAHmTy4VbIE2PSU1GQoLOZSm39ji5zP5bt4HLximTsPEHejoKdQsglkyBYd9vBnVDLlTILux7XNbV4Onfv7x7r32CO8Ei7MCNLhRqHbAAI3Xb4f7pqDY-MvoqpxhuXrO55TYjD9gKkNGzmB8977IAFfWdzSi9QwV4DT9o8YY57jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد فرماندهی نیروهای مسلح کویت اعلام کرده است که سامانه‌های پدافند هوایی این کشور در حال حاضر به تهدیدات ناشی از پهپادهای ایران واکنش نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139056" target="_blank">📅 10:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dffd6f0fab.mp4?token=t2hZs6koE28Uwis-lEzs9j2dV3AGy_9AHsqfEZDCvmufkSPmh7fg0hQezdQxNU_Qv2anKugE2_CAD1C51o3adFSKtjWUFLtDZzc5HqQBj3ivT49Aek4EMHjW2RvtyOXathmVtIM5SsAJX1QmwmsHqGuNabRI18R4Zc6O3A_sjZyQ63TiyeDmHIw7y1Tgvohr_E8LBl4jtAMnhGDz2aNSyLbujwfNpKbMIbo0aUWLKhQ8Z2bEECC_RpfnvDA8mktR-t0YZVKoK-8lIcp6lVe5s53Hz5vfkbnip_zengfmfU_GwkKgl_A2LPG_fLtuIXvve-S5Zud6bviJAA48RhEw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف:ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139055" target="_blank">📅 10:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ارتش کویت از درگیری پدافند این کشور با پهپادهای «متخاصم» خبر داد
🔴
حساب رسمی ستاد کل ارتش کویت در شبکه اجتماعی ایکس دقایقی پیش اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/139054" target="_blank">📅 10:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1d389880.mp4?token=p3FgqN7bE5HWXPY-hiFZoLN0bs2EByZYGbaC0A_aDdYBQ23segJvQ2O5q0wiVqeODHwYSvqUxPKevlwzid2ufVSrPW2iWGa6FHA0h3vAmgzSXTWVGE3NWJMRzWsL4czL95kQJrUfKWsVDkL9yD4yF1spk28e0LFL1Suyeld32SKguJnEZCKyKjaGo2rec_kiAbS9_Z3pCONY2AxoKrek4BSe9rRiTORFBp8dj2R4nAd64R96nzloyBo0vxIXYO5OlW6aYl33R7WbNXEQQ22FiXy6CHpfEGjIj_IwkCUBgN_8nrZlwe3FfvEqvdUBX5g2JK1dCsUZiDykmtruDpyFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه ۴.۷ ریشتری جنوب ایتالیا را لرزاند
🔴
زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر شامگاه جمعه منطقه «کامپی فلگری» در نزدیکی شهر ناپل در جنوب ایتالیا را لرزاند و دست‌کم ۱۰ نفر را زخمی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139053" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfTCJD3nUnM9p1Xxm9EMGLdO5KCG84Bgr8m5GwWzNfQOuZrhcYF77B3vh1rr9LD5jC_QMBq66NOOH7A0C0P51-yPIWsTzBszJ3iS74l-G87R2YHJwrCwroDz1WYishUz3uJnvK4OFxJU_fFamgQgXIi57mUbo_xKR4W4yLLeFVwD2qMENFk37lSuLdPjYcXhKAl-K01Mg7QGDF_kPNdYYz9CUl0gZqRyu1EHsR7BDnsUnn4VvkPOLBMkyP-Hc14yH3lTdyXiy5iysF66F_1cWebjOJv-CWDdxGZEekb-iVfEB5EOKu_sVLOaQ8slDTt73-YjiKF-2wXeDft9uOTF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: مشکل اصلی ایران و آمریکا مربوط به حوزه هسته ای و ۴۰۰ کیلوگرم اورانیوم است و بعید است با بمباران زیرساخت انرژی و هسته ای، سیاست های تهران تغییری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/139052" target="_blank">📅 08:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فاکس نیوز: موجودی موشک‌های «تاد» آمریکا به کمتر از ۲۷۸ موشک کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/139051" target="_blank">📅 08:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی کاخ سفید در واکنش به گزارش‌های ادعایی درباره احتمال حملات به ایران در پی نشست کابینه آمریکا در کمپ دیوید ادعا کرد: دونالد ترامپ، رئیس‌جمهوری آمریکا، همچنان به راه‌حل دیپلماتیک متعهد است، اما به پاسخ دادن به حملات ایران ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/139050" target="_blank">📅 08:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-DFyD9k6dZLTCLfVWadqoJAsaciS_KQgJl8uwHDsITJarS51RhvZFslwM0ng3YzHjDNqAuopex6fq_1UQJg7Uo4bj6aQnLH8UmMYCamL8-JQ3ANOvbx4cuQR8fVkpNy9b3cy0c6IoHSDDLvQibxIrzfumzp5JapV6w4DEm3tY_2ZYNaEvAgTEksx_IIDAzt1ce7qoK2rm6YzYHDW5YvkK9rFXCUsHYftQNNqPX4Ff_bC-DN8cLOcchuYQAcc-8pNOwDvNK2fOw3kgHkOSD4YkD1fFOCdMLL-DVNS-pRsmHCMV8oTW75bEFz0FLImFS6zsprBqz00rcjH31rw35eOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: آنچه که در اسپانیا اتفاق می‌افتد، با ده‌ها هزار مهاجر غیرقانونی که به آن حمله کرده‌اند، در ایالات متحده در دوران دولت خواب‌آلود جو بایدن اتفاق افتاد، و اگر دموکرات‌ها دوباره به قدرت برسند، دوباره اتفاق خواهد افتاد، حتی بدتر.نگذارید کشورمان نابود شود. به جمهوری‌خواهان رأی دهید و به ایالات متحده افتخار کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139049" target="_blank">📅 08:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=A3ePidRubFV6p97oKgy7tU7dOjVvwK8wU-xJ4plRnHBTArwRPfmad6eDkPVEo-q_B1wwTso1pwnax2foE7POPKlGFS9ZIeIFYvIkyzktQhSrwg1Y9QvnfyI5-d5u9XfNTPMFryuN7tzJWprR7xxP13a2b4-RjJ9BwlFyi9FR7Mo3AyjYAGbEEUVfG8IT6gabbz5UB44OFACMcDQIfmGm8M6nCewBYnS9-ln6gvM3xyS9H8U6pfY6uG0Ym5cAlYYzs9hhAoqS8Vp4gjU30ROuIeC7rh4jPSlNRVPtW2DgkEOQTWtJUtBUUlOvMkyfIR5tw7q97I81TCL9LDKGTCxCuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658c5b0c9d.mp4?token=A3ePidRubFV6p97oKgy7tU7dOjVvwK8wU-xJ4plRnHBTArwRPfmad6eDkPVEo-q_B1wwTso1pwnax2foE7POPKlGFS9ZIeIFYvIkyzktQhSrwg1Y9QvnfyI5-d5u9XfNTPMFryuN7tzJWprR7xxP13a2b4-RjJ9BwlFyi9FR7Mo3AyjYAGbEEUVfG8IT6gabbz5UB44OFACMcDQIfmGm8M6nCewBYnS9-ln6gvM3xyS9H8U6pfY6uG0Ym5cAlYYzs9hhAoqS8Vp4gjU30ROuIeC7rh4jPSlNRVPtW2DgkEOQTWtJUtBUUlOvMkyfIR5tw7q97I81TCL9LDKGTCxCuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، با هشدار نسبت به پیامدهای هرگونه درگیری میان واشنگتن و پکن، گفت جنگ میان دو کشور «فاجعه‌بار» خواهد بود.
🔴
وی تأکید کرد وزارت خارجه آمریکا در حال انجام «کار دشوار دیپلماسی» برای جلوگیری از بروز هرگونه تقابل اقتصادی یا نظامی با چین است.
🔴
روبیو همچنین تصریح کرد که وقوع جنگ میان آمریکا و چین سناریویی است که «خدا نکند» هرگز رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/139048" target="_blank">📅 08:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فارس: مارو از زیرساخت زدن میترسونن ولی مهم ترین زیرساخت های انرژی دنیا در تیررس ما قرار دارن و اگه بزنن میزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/139047" target="_blank">📅 08:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/alonews/139046" target="_blank">📅 02:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYkzXT18xjYkpYZXzzxtuwOsXeNQEfYW5y6LkhPJ_SJvhMC5Ola7Atn2vtpvvnllgxSSmIr0QwuWCeeXkY4kNcpWcfCauJ2iiqM05AwI0WSW1bqm6ItSTFMMjspRWCAsevFMC8iDLgv_XkE6HH0Vt6g6T_ZRoGaHvngvGeSW4Uyy7R5zJZkR8ebCJFZtOod6MwCTg9L9b-qIQ600vQhQE1HnbFXLBvwztqhIZSphM07w9u42gI9ps4Hb7oZ8AkJR3UOF-31kon0jQ3FDbJ9eD9sY-LNueIyzGJd-gPPpS06AAiLSL9ZIvg6-2CpEH7zTAUY_LzZ23giQH3PPfRKuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقال تجهیزات ضدهوایی به جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/139045" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قشر تندرو واقعا احمقن، میگن اگه زیر ساخت مارو بزنن ماهم زیر ساخت منطقه میزنیم خب بر فرض شما زیرساخت بحرین و کویت و ... رو زدی. خب اونا پول میدن آمریکا بازم براشون میسازه و آمریکا سود میکنه، ما چه کنیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/139044" target="_blank">📅 02:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/139043" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سی‌ان‌ان: ارتش آمریکا مقدمات لازم را برای انجام مجموعه‌ای از حملات علیه زیرساخت‌های هسته‌ای ایران، از جمله کوه کلنگ، فراهم کرده است؛ هرچند این حملات صرفاً محدود به این سایت نخواهد بود.
🔴
مقام‌ها گفتند که این آمادگی‌ها طی چند روز گذشته شتاب بیشتری گرفته است.…</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/139042" target="_blank">📅 01:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان: دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/alonews/139041" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان:
دامنه دقیق حملات علیه ایران و اهداف احتمالی که آمریکا ممکن است آنها را هدف قرار دهد، مشخص نیست و دو مقام گفتند که این حملات ممکن است لغو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/139040" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
طبق گزارشات به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ اینترنت سراسری قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/139039" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
👈
آکسیوس به نقل از مقام آمریکایی :
رئیس جمهور ترامپ به طور جدی در حال بررسی حملات علیه اهداف انرژی در ایران در چند روز آینده است، اما هنوز دستور نهایی برای انجام این کار را صادر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/139038" target="_blank">📅 01:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طبق گزارشات ترامپ یک فرصت دیگه به تهران داده اما فقط ۲۴الی ۴۸ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/139037" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کاخ سفید: تهران تفاهم نامه را نقض کرده است، بنابراین رئیس جمهور ترامپ بیکار نمی ماند و پاسخ حملات و اقدامات ایران را می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/139036" target="_blank">📅 01:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بازارهای جهانی هم اکنون بسته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/139035" target="_blank">📅 01:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/139034" target="_blank">📅 01:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رسانه i24News: ترامپ صبرش رو از دست داده و حمله به زیرساخت‌های انرژی ایران میتونه آسیب‌پذیرترین نقطه جمهوری اسلامی رو هدف قرار بده؛ تصمیم نهایی در آخرین لحظه گرفته خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/139033" target="_blank">📅 01:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/139032" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/سخنگوی پنتاگون: وزارت دفاع آماده است تا در هر لحظه دستورات رئیس‌جمهور ترامپ را اجرا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/139031" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
✅
‏ ️فوری/هم اکنون پرواز گسترده جنگنده‌های آمریکایی در آسمان منطقه
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/139030" target="_blank">📅 01:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139029">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال: ترامپ در جلسه امروز تیم امنیت ملی خود، دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/139029" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139028">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال:
ترامپ در جلسه امروز تیم امنیت ملی خود،
دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/139028" target="_blank">📅 00:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139027">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/139027" target="_blank">📅 00:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139026">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/139026" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سی‌ان‌ان: به گفته مقام‌های آمریکایی، ترامپ از عدم تمایل تهران به پذیرش خواسته‌هایش خشمگین شده و این موضوع باعث جلسات عصبی پشت درهای بسته و تماس‌های تلفنی پر از ناسزا با متحدانش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/139025" target="_blank">📅 00:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139024">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
گزارش شبکه سی‌بی‌اس: ایالات متحده و اسرائیل در حال آماده‌سازی برای بمباران اهداف مرتبط با انرژی در ایران هستند، و این عملیات ممکن است همین آخر هفته آغاز شود
🔴
طبق گفته چندین مقام رسمی آمریکایی، اسرائیل در جریان برنامه‌ها قرار گرفته و با ایالات متحده هماهنگی لازم را انجام داده است. با این حال، رئیس جمهور ترامپ هنوز مجوز نهایی را برای این اقدام صادر نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/139024" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52236384f.mp4?token=oDZKhFAZtOaIKyaXXCaCQvyuQi0qYNL6QKCCnE_h-dLYW7cDbMVG43Cxa6ZQjRiYg05IrAWNiFZaO3DgJpuyUyOYDJejiIScB36CSvYn94MHNalrU7TO9lojaZCmeVpVZtZytv4mxLUWWcAN_ce0Jc24OsJr6XUJwWox8EcqzgWtyUmi8SreyHOBPlgiW1jk-biTMOefZrMsdESrHB7PgQVTJdaZw5u_r9KQkO2ZO0WNcBBRgg9XW9y38yEQu_w_j7gajEzIiYYn-Rw28ZGMmY1hPhwmZ7-_tYC6xBkCv5i22yvK5JuTqcM_wwSCdhGojXuzzrPGz8DlwuME7K8Mhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52236384f.mp4?token=oDZKhFAZtOaIKyaXXCaCQvyuQi0qYNL6QKCCnE_h-dLYW7cDbMVG43Cxa6ZQjRiYg05IrAWNiFZaO3DgJpuyUyOYDJejiIScB36CSvYn94MHNalrU7TO9lojaZCmeVpVZtZytv4mxLUWWcAN_ce0Jc24OsJr6XUJwWox8EcqzgWtyUmi8SreyHOBPlgiW1jk-biTMOefZrMsdESrHB7PgQVTJdaZw5u_r9KQkO2ZO0WNcBBRgg9XW9y38yEQu_w_j7gajEzIiYYn-Rw28ZGMmY1hPhwmZ7-_tYC6xBkCv5i22yvK5JuTqcM_wwSCdhGojXuzzrPGz8DlwuME7K8Mhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی:
برخی می‌گویند ذخایر اورانیوم ۶۰ درصدی باعث شد به ایران، حمله هسته‌ای نشود؛ این مغلطه است؛ خب اگر استدلالتان این است، چرا این را نمی‌گویی که اورانیوم ۶۰ درصد سبب حمله شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/139023" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره بنادر ایران، مسیر ۳۰ کشتی را تغییر داده و مانع حرکت دو کشتی شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/139021" target="_blank">📅 00:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر من برجام را فسخ نمی‌کردم، ایران ۶-۷ سال پیش سلاح هسته‌ای تولید می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/139020" target="_blank">📅 00:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1579fcf7a3.mp4?token=ej2QQX9jR7XqbjPAedsagJgFJRal3VNG-xGlGrHi_YMTMBaWSDyC529w_h0mQYEJ-A2rUkZ5xlDahBJa07Zn13uDyU_JESrKTSBBwKhRWOpVK7JgGsTut4wgYyO9iZbgqgBkhOdZdTEE6Ym4ZOPhu65C4FqzH9BT6efUoZ-ayYNHVTyij_kVTSxaFmp22GTL8ata7fJ3gFELu4MlRvhxfjRRorZtpszYBVxT2kU40ynGbwJpnsyfD5Zi4O65CF9flqKLmrhjXu3BWEIRouswUCorQVOJsRUTSZIm2450y_dvLODk8UjTg3NWT2KIYuVvPGfS-32TQ5BpMWPOVt22gSsxEKcG2WZlFyN4U1M5meLF33zBPLJh6w9y3akbP-0xcf-86TBnb3YRx3n5AhlzsEVOcemEUFBw_36LFmJiwAJHB8Fepd27zpvGxoYx-xqSN14Q8Xaqx_fFMWidGQi7ahGzP8zGrniMsvgoX-1r7JK-kWpuOgFEKa5sFhDxmhyJ4f2BdM7-xzFSfVtIJd84_fG8CbW5NNq_oY9cBWhnN-6yvm3hgkzEFCkYsAM2YMRFrWhICg2-qqrhkT2wcGcND1eJBH7smommrQBWnUxgpL6QX79osRXwDjdVblqPFkwEOS1lx29RDlOZlCDJeGfL2V787vm7-I23IBpK8OmrowE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1579fcf7a3.mp4?token=ej2QQX9jR7XqbjPAedsagJgFJRal3VNG-xGlGrHi_YMTMBaWSDyC529w_h0mQYEJ-A2rUkZ5xlDahBJa07Zn13uDyU_JESrKTSBBwKhRWOpVK7JgGsTut4wgYyO9iZbgqgBkhOdZdTEE6Ym4ZOPhu65C4FqzH9BT6efUoZ-ayYNHVTyij_kVTSxaFmp22GTL8ata7fJ3gFELu4MlRvhxfjRRorZtpszYBVxT2kU40ynGbwJpnsyfD5Zi4O65CF9flqKLmrhjXu3BWEIRouswUCorQVOJsRUTSZIm2450y_dvLODk8UjTg3NWT2KIYuVvPGfS-32TQ5BpMWPOVt22gSsxEKcG2WZlFyN4U1M5meLF33zBPLJh6w9y3akbP-0xcf-86TBnb3YRx3n5AhlzsEVOcemEUFBw_36LFmJiwAJHB8Fepd27zpvGxoYx-xqSN14Q8Xaqx_fFMWidGQi7ahGzP8zGrniMsvgoX-1r7JK-kWpuOgFEKa5sFhDxmhyJ4f2BdM7-xzFSfVtIJd84_fG8CbW5NNq_oY9cBWhnN-6yvm3hgkzEFCkYsAM2YMRFrWhICg2-qqrhkT2wcGcND1eJBH7smommrQBWnUxgpL6QX79osRXwDjdVblqPFkwEOS1lx29RDlOZlCDJeGfL2V787vm7-I23IBpK8OmrowE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟
🔴
ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/139019" target="_blank">📅 00:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab4670a68.mp4?token=iYeJ7sqyJd95S3ovxZTjEyZeThPPuZjooASubGVTTxX_iAxuLJaS1Bd4Hz5Y3Y3iHOoJHjsPAvkQcN6tkVRlM0HvsUz4CfHtyaM1YkdKyP6PF4xhoAaOGc1Qsd4hBvOULWCmwU5k-TnLe6PDSnUdrmp1JiR3yKOir1COlgxk0YU02DcTCPUmY1S7SD1T1aj5uC7Hnn2DhUcKWDWYjuSLSfPOp60TbkfPncigFVivnJOfmWRqpt28Lg-5gz2GfB69UMwOnB45DelsawL6Fwh5K8NsgqqmOcrLp5wSpFzV5U_M3V1Wr23sJNlWhNGUl74PRRu9weKzKmqd_aM22hRUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab4670a68.mp4?token=iYeJ7sqyJd95S3ovxZTjEyZeThPPuZjooASubGVTTxX_iAxuLJaS1Bd4Hz5Y3Y3iHOoJHjsPAvkQcN6tkVRlM0HvsUz4CfHtyaM1YkdKyP6PF4xhoAaOGc1Qsd4hBvOULWCmwU5k-TnLe6PDSnUdrmp1JiR3yKOir1COlgxk0YU02DcTCPUmY1S7SD1T1aj5uC7Hnn2DhUcKWDWYjuSLSfPOp60TbkfPncigFVivnJOfmWRqpt28Lg-5gz2GfB69UMwOnB45DelsawL6Fwh5K8NsgqqmOcrLp5wSpFzV5U_M3V1Wr23sJNlWhNGUl74PRRu9weKzKmqd_aM22hRUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
قیمت‌ها، به‌جز قیمت نفت، به‌شدت کاهش یافته‌اند. وقتی دو هفته پیش تصور می‌شد که به توافق رسیده‌ایم، قیمت‌ها مثل سنگ سقوط کردند.
🔴
اما ما به‌دنبال یک توافق واقعی هستیم؛ من توافق صوری و ساختگی نمی‌خواهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/139018" target="_blank">📅 00:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: من دوست دارم که فرد بعدی باشم که در این سمت فعالیت می‌کند.
فرد بعدی که در این سمت خواهد بود، مانند یک نابغه به نظر خواهد رسید، زیرا تمام این کارخانه‌ها دوباره راه‌اندازی خواهند شد.
این کشور دوباره ساخته خواهد شد و او به خاطر این دستاورد مورد تقدیر قرار خواهد گرفت.
🔴
مک‌کینلی کشور ما را احتمالاً به ثروتمندترین حالت خود رساند. بعد روزولت آمد، پول‌ها را گرفت و خرج کرد.
مک‌کینلی هرگز آن‌طور که شایسته بود، اعتبار دریافت نکرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/139017" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ در مورد ایران:
می‌خواهید همه چیز سریع تمام شود؟ به دیوانه‌ها سلاح هسته‌ای بدهید.
🔴
خیلی سریع تمام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/139016" target="_blank">📅 00:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=mizndD5UazzK4XazZxe3nlOMHRmLnC0mHD5Y-ZTt8J28jLwcOYAnJ_a4_e9QZzJgAVr9zFS1uAFjAB3Zm3HOQc6zCn5w7LpJ3nbIneDYMQeACaONh6lJ-mbCsXMYkEUh0QGGKOJ38Vum_lld-FAl35d0GtphSuAmJilRRDdSjQZAcX3FJ6gRA4ntUQZi4IVauoeeQmTNFNlt1f5_XD4cQSmmpUjH7-X2TaeCtSPuaig-bR05MU8jym5EYYfmvOuzRhdaWDHZUeEdvlVvUCF_E2h3wVVlcqv6ir3TFzjywc5okePykWC6lGplrvsbR0kiXF5Jakt64nnv0Y59GB7jjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=mizndD5UazzK4XazZxe3nlOMHRmLnC0mHD5Y-ZTt8J28jLwcOYAnJ_a4_e9QZzJgAVr9zFS1uAFjAB3Zm3HOQc6zCn5w7LpJ3nbIneDYMQeACaONh6lJ-mbCsXMYkEUh0QGGKOJ38Vum_lld-FAl35d0GtphSuAmJilRRDdSjQZAcX3FJ6gRA4ntUQZi4IVauoeeQmTNFNlt1f5_XD4cQSmmpUjH7-X2TaeCtSPuaig-bR05MU8jym5EYYfmvOuzRhdaWDHZUeEdvlVvUCF_E2h3wVVlcqv6ir3TFzjywc5okePykWC6lGplrvsbR0kiXF5Jakt64nnv0Y59GB7jjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران
:
من در حال انجام کاری بسیار بزرگ‌تر از چیزی هستم که گفته بودم انجام خواهم داد.قرار بود وارد شویم، توان نظامی آن‌ها را از بین ببریم و بعد خارج شویم.
🔴
اما بعد متوجه شدم اگر این کار را انجام دهیم، باید نوعی حضور و نظارت مستمر وجود داشته باشد؛ وگرنه آن‌ها دوباره همه‌چیز را بازسازی خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/139015" target="_blank">📅 23:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران نباید سلاح هسته‌ای داشته باشد. آن‌ها قطعا از آن استفاده می‌کردند.
🔴
اگر من نبودم، اسرائیل امروز وجود نداشت. آن‌ها وجود نداشتند.
🔴
آن‌ها دو هفته با داشتن سلاح هسته‌ای فاصله داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/139014" target="_blank">📅 23:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9a8262b2.mp4?token=UydCKV1dvahsrZgtew1f9iyDXT3jyqheH83AcyuhXTnzrqmWucX5m2w6ibLIyuCze-IV5tkw85iUeacW7e9uQJTw04GEoJx__RA6yp-S5Eg53XqBeKmfDUEPwAc8h3uxoQNggpt4j8Ipol5Bpxo-DFaBs0rADrER4A1zYsOBqoUs4WJ2CVL0rlNM8eXu6ygrRIftxoJxwrxIcqWgnxlETgvDX9e9EGrFEhu1NL8ULqHQMkK8574_kXj7Ihi9grTr-xHJoy06XpRukh8LpimmTF_FHII9Yoks6OpUXEBgZuz0r5Z0M5ozhiB4-OyDIK7diwQo9HYgpR0ylgorGtmeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9a8262b2.mp4?token=UydCKV1dvahsrZgtew1f9iyDXT3jyqheH83AcyuhXTnzrqmWucX5m2w6ibLIyuCze-IV5tkw85iUeacW7e9uQJTw04GEoJx__RA6yp-S5Eg53XqBeKmfDUEPwAc8h3uxoQNggpt4j8Ipol5Bpxo-DFaBs0rADrER4A1zYsOBqoUs4WJ2CVL0rlNM8eXu6ygrRIftxoJxwrxIcqWgnxlETgvDX9e9EGrFEhu1NL8ULqHQMkK8574_kXj7Ihi9grTr-xHJoy06XpRukh8LpimmTF_FHII9Yoks6OpUXEBgZuz0r5Z0M5ozhiB4-OyDIK7diwQo9HYgpR0ylgorGtmeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:همان کسانی که آمریکا را ۲۱ سال در جنگ ویتنام نگه داشتند، امروز درباره ایران انتقاد می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/139013" target="_blank">📅 23:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895aff4f9a.mp4?token=Ac3BeaFG3wCf_OHP0GMn86nzdPGBC6oFFfQbMf4Ng7bo-SGPXIUwWgB2HK8_CeNTaaF4d4dMBJc8CVcygbkZRYxoZJR2o5GTqopcgJPCM4Jil6MdzUDfB0oMqjr53Otkz7ciE0REWyqzcarGbYvJs0lEcZfT5QCll6IveqVU9ts0f8KfD-4Aw5uokLsYV2q1l0sv8o7GGhHX9wdl4ElPEVaj76LZCXjN7427uDsPrycr2bmB0vBhfXrSX7r-e4f7-Xu451MepU0oPLdBoKqMmwYQqSqXz33XwwNjOyGypvQLRSW8I2RDSesDfL2TL72aZrCsYi1GYVH9GnPm9YBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895aff4f9a.mp4?token=Ac3BeaFG3wCf_OHP0GMn86nzdPGBC6oFFfQbMf4Ng7bo-SGPXIUwWgB2HK8_CeNTaaF4d4dMBJc8CVcygbkZRYxoZJR2o5GTqopcgJPCM4Jil6MdzUDfB0oMqjr53Otkz7ciE0REWyqzcarGbYvJs0lEcZfT5QCll6IveqVU9ts0f8KfD-4Aw5uokLsYV2q1l0sv8o7GGhHX9wdl4ElPEVaj76LZCXjN7427uDsPrycr2bmB0vBhfXrSX7r-e4f7-Xu451MepU0oPLdBoKqMmwYQqSqXz33XwwNjOyGypvQLRSW8I2RDSesDfL2TL72aZrCsYi1GYVH9GnPm9YBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تعدادسربازان کشته شده درجنگ با ایران:در ماجرای ایران، بسته به اینکه معیار محاسبه چه باشد، ما بین ۱۶ تا ۱۸ نفر را از دست دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/139011" target="_blank">📅 23:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1gghoVT4QUQJIfVSTlRvOtDAS0_3ilmIIE_2dC84iIWW79mAktxqrVQXB95iZrhlxBVXSTVftgr5LSEfUZ3aHrShBkwkMCPEf_c3vhTR4iMmV7UHwTf5KGT3VlBPiFUKDidLYlHP-CgFzzRnSVgmsXg41D36X5s_7P6dT9MZR1G-OuKtRhYY6tmRf4rIRDNx2qjtyYa-vRcp7RKh7TwBD8VNcgD9rh9h5qPaaYno7Bv955iaP9BvzFHHGvmCFvGoRBtwn_Gt5ZsUQuyYjSZDxYA4ysjiSH7ifWUc9HtsPyx5QCEqTURkdR024fajV6Oz5OvmH-u56VBhfyWpwpdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج فروند هواپیمای تانکر سوخت‌رسان آمریکایی در آسمان خاورمیانه و در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/139010" target="_blank">📅 23:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/139009" target="_blank">📅 23:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: جمهوری خواهان می خواهند ماگا باشند، در واقع همه‌ی جمهوری خواهان الان ماگا هستند.
🔴
ماگا یا MAGA همون آمریکا را دوباره به عظمتش برگردانیمه که شعار ترامپه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139008" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8qxT4CLlW1LFI1MVKrdyI5egvjXb8YiaUp_57VAUdA8td5ETTB3ohf4cetduhPs7LUEe_EknTIOhAGXJpmfnby0miIt0FvM8hzO0kmIe_VE6kTWyU79Zj6hUHuhcUD0T-X7jBenSx-uR5zSbkYYfYVdYpssgRedK6fGiAyj3hYTPv_rqYJC4ruhAEYGxvmYpz0laaU00pwuAnYL2S0x2wyo6KtKk0MVmP2SwRnaUjOUIb_V3oUsHaBU7ki3D2uJ0uyuyTrQcR74-HIeqo4N_nqRKgiqRpMavmVvoguZWW264goC4_OLd9yIFnk2cwCrQjGLL4m3TY5Gwy2a4G0IMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل پس از غزه، اکنون به سراغ لبنان رفته و با حملات توپخانه‌ای، شهر صور در جنوب لبنان را بمباران کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/139007" target="_blank">📅 23:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک پست: فرمانده سنتکام یک کارزار بمباران گسترده دو هفته‌ای به ترامپ ارائه داده که در آن خبری از حملات محدود شبانه نیست و روز و شب و به طور مداوم و گسترده و در همه‌ی مناطق، ایران بمباران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/139006" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت امنیت داخلی آمریکا اعلام کرد که ایالات متحده واردات از ۴۳ شرکت چینی دیگر را به اتهام استفاده از کار اجباری ممنوع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/139005" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قطر از توافق حمایت کرد و از حماس خواست به مسیر توافق پایبند بمونه
🔴
همزمان گفته باید روی اسرائیل فشار وارد بشه تا این توافق اجرا بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139004" target="_blank">📅 23:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الجزیره: قراردادهای آتی نفت خام برنت ۱.۲۲ درصد افزایش یافت و در زمان تسویه به ۹۰.۱۲ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/139003" target="_blank">📅 23:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فاکس نیوز: پنتاگون پس از ماه‌ها درگیری در ایران با واقعیتی فزاینده روبرو است. ذخایر موشک‌های رهگیر دفاعی آمریکا تا حدی در حال کاهش است که برنامه‌ریزان نظامی در حال بررسی این موضوع هستند که آیا می‌توانند به روند فعلی حملات تلافی‌جویانه محدود ادامه دهند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/139002" target="_blank">📅 23:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c9e5e82d.mp4?token=nICArpr_mTe-fsgHKMHyhirTnksVwKCiJRm5xboLs1vIsc4YO0AYpWDxs8F1w_As51KYJ79xcvD0tgk0E4OOef_C3ryJmxxzv0BywvP-cbDWik2VeM8By5PvRaHDKPLcMsTcAAszQUx78_fwQQtwqXXFaAO5U-5MtAOqukl0pnWFxe0MWtWC6XhE5nQCfV2brfGwpj6Ahj5nXsqCR7B0Dxo6XgVEeZxCwwrHtoWV8IhRt-6aoTkw9tOPojFi_VoY-05fkIAY7oe894OT6JUTF_7hhFi19C-x-SXYYPc0m8bfb7NpUP0esqOMKwW5bDRPa_Hj6IkWWN7U7yRA5vzQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c9e5e82d.mp4?token=nICArpr_mTe-fsgHKMHyhirTnksVwKCiJRm5xboLs1vIsc4YO0AYpWDxs8F1w_As51KYJ79xcvD0tgk0E4OOef_C3ryJmxxzv0BywvP-cbDWik2VeM8By5PvRaHDKPLcMsTcAAszQUx78_fwQQtwqXXFaAO5U-5MtAOqukl0pnWFxe0MWtWC6XhE5nQCfV2brfGwpj6Ahj5nXsqCR7B0Dxo6XgVEeZxCwwrHtoWV8IhRt-6aoTkw9tOPojFi_VoY-05fkIAY7oe894OT6JUTF_7hhFi19C-x-SXYYPc0m8bfb7NpUP0esqOMKwW5bDRPa_Hj6IkWWN7U7yRA5vzQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تظاهرات(کودتای آمریکایی صهیونی) مردم اسپانیا در مادرید جلوی سفارت مراکش
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/139001" target="_blank">📅 23:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b78ee674.mp4?token=VGJYUKcEQDxNjlQO3lZZYqHh45wsQUpP75zOL2-MkkPsEi_JivbWJFjkG6hR05DzWrl6H2h9amK0cKqlafrjHCik_xurO09ajfZqOi1fgubGHkE7HD7h0aRtIx2Yo6r77wZuie2HlxRqQy1iAufY1g538sjluTpuPcjCg7x5dYF5Jwjz682ad9yVn-fVQsA06aQI_6uUBQ8YCCISuzZVSaoPIlsptzGSFx7C0uJTLw8w7QbWKgf4C880eIMMMmSGhRffudraFlOwTFOzWbU1ihdNrZ_4xkvZOldH6Sn5BplZCttK3TiBFxBuq4zSqxFdCfmxYhBMohOha1Dajx1VZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b78ee674.mp4?token=VGJYUKcEQDxNjlQO3lZZYqHh45wsQUpP75zOL2-MkkPsEi_JivbWJFjkG6hR05DzWrl6H2h9amK0cKqlafrjHCik_xurO09ajfZqOi1fgubGHkE7HD7h0aRtIx2Yo6r77wZuie2HlxRqQy1iAufY1g538sjluTpuPcjCg7x5dYF5Jwjz682ad9yVn-fVQsA06aQI_6uUBQ8YCCISuzZVSaoPIlsptzGSFx7C0uJTLw8w7QbWKgf4C880eIMMMmSGhRffudraFlOwTFOzWbU1ihdNrZ_4xkvZOldH6Sn5BplZCttK3TiBFxBuq4zSqxFdCfmxYhBMohOha1Dajx1VZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پناهیان بعد یه بَست: آقا مجتبی پدر جهان هست و قالیباف هم برادر بزرگ جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/139000" target="_blank">📅 23:05 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
