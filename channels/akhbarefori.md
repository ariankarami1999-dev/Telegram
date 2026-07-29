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
<img src="https://cdn4.telesco.pe/file/dabobywK6JZYNhfYNRlQ1cviccLjfC2NQVQQOaI0Z4NZWE7DuWQ4Lq4_oFXEvycRg02-3T2k1yxuqI0UprOLScTa-W6MHS5mcpVmGP9yZW8H3zv2LmV4ChmbPGUeBY47vDwVJfEEmeAKAOjRAq1dOQR-ZQlhdZWQ6jz3rCdZrGAauob5MIcdz6u59dOBfNsGCUNZRSPoHKbrJ3iZToo1nAfISH4ESIttcPyNXh5A8XSFlwFpfUAN5tz4JcdZSs54-jh4AAnuhWpglwVzlqDX5uKMO-lQcsWALvwwMlIWvpPuvxksyJ4hd_7cjL-KZbd4yUizdS-NoBstsTmvmWczpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-676292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ورود معترضان به هتل نتانیاهو در واشنگتن
🔹
گروهی از معترضان به نسل‌کشی اسرائیل در غزه وارد هتل محل اقامت نتانیاهو شدند و علیه او شعار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/676292" target="_blank">📅 11:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82f8a748f.mp4?token=aptQa-_5IRZifBBamw9Fm4QWGJkeOTGCLXH5AXpQ6t1m00gsPsq0Up5kBAEp2sje5ixNzEMI4fGvPOTXUElRfvS0UI04BtFp3h05FpBDXPC23vGBhv8WFNQD7hjpcuIjjl9X4-Oh7l4Z2Hd_UF3O1Y_jC6K6aEwFARuTJ9iF4krX1kwkA41f_WJfZibByW9ZADP6cjCw7PY_UVEGUu_-p01U7EMFQdORvZA9zlEBO37o3qyc9eSX0mhQsckZ94s1gSDU6lLQPwt3rLxorss2AHDzS-poWfT8owPUV-dSDCKqQS3I6jAonn3uQdbiIJSGTbLtPZnbfalmCB-mjB5RAW6Ah5pg4FiZ9PeERW4W9peI8OPiJEWxKn3nnB0XU2_L2CyRmye4uW62M2yKnIeOcvQS9Gp-_BiBIV7ZOATY1UwOKOPzU3jLFf-Fwt6GH5sN-dmmiCum1WKmp6LAdwYassNtzaw8Pcmi9PYTHup27i6MEMlLnugfFT29H5jnhq6ioy9Ji0HRzoqBEzwJAyzcy2BNcnQvgJ3F2eCWmDx_t1zcbZzPjl_tyJCo62CicncRvfxKZLpafrtmFJLniApKjlhJ5tK-WeRyEkiELOMF-qL8O0jMCCBFAmF98v4hn-stPzOxP3W16B2T9EL3rH6lZrrNPtF2DBksvQ7333kMYeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82f8a748f.mp4?token=aptQa-_5IRZifBBamw9Fm4QWGJkeOTGCLXH5AXpQ6t1m00gsPsq0Up5kBAEp2sje5ixNzEMI4fGvPOTXUElRfvS0UI04BtFp3h05FpBDXPC23vGBhv8WFNQD7hjpcuIjjl9X4-Oh7l4Z2Hd_UF3O1Y_jC6K6aEwFARuTJ9iF4krX1kwkA41f_WJfZibByW9ZADP6cjCw7PY_UVEGUu_-p01U7EMFQdORvZA9zlEBO37o3qyc9eSX0mhQsckZ94s1gSDU6lLQPwt3rLxorss2AHDzS-poWfT8owPUV-dSDCKqQS3I6jAonn3uQdbiIJSGTbLtPZnbfalmCB-mjB5RAW6Ah5pg4FiZ9PeERW4W9peI8OPiJEWxKn3nnB0XU2_L2CyRmye4uW62M2yKnIeOcvQS9Gp-_BiBIV7ZOATY1UwOKOPzU3jLFf-Fwt6GH5sN-dmmiCum1WKmp6LAdwYassNtzaw8Pcmi9PYTHup27i6MEMlLnugfFT29H5jnhq6ioy9Ji0HRzoqBEzwJAyzcy2BNcnQvgJ3F2eCWmDx_t1zcbZzPjl_tyJCo62CicncRvfxKZLpafrtmFJLniApKjlhJ5tK-WeRyEkiELOMF-qL8O0jMCCBFAmF98v4hn-stPzOxP3W16B2T9EL3rH6lZrrNPtF2DBksvQ7333kMYeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتضی سیمیاری،کارشناس مسائل منطقه: جامعه اطلاعاتی آمریکا، نتانیاهو را «پیک دروغگو» می‌داند و سفرهایش به واشنگتن را منشأ دردسر برای کاخ سفید توصیف می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/676291" target="_blank">📅 11:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ویدئویی دیگر از جنایت آمریکا و عربستان علیه حشد شعبی در نینوا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/676290" target="_blank">📅 11:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd8931bae.mp4?token=ThskGIJe7FGuNi_n_JcB59A2oIVmGZW_C5bKhcaQTmiB3G8APvywzekzANDJdYbVwqYmphwjFqJeHIl012xeP5F336Vs7O1ppyXDnHvoa7VLwE0UX38nuHrvFp88owa6l4iNLh2g1MrHHWmV1zmx94O6Twr2AWLSwl_4w4kAub0yOmomuIX_xLaXTV8qh_V1Aoj4A9w9YiYwm1s6xtPMT7AGGt79qMrNotwWAJwmLKdvhLp-iyMkQ_iquNxyu1FpRyBBfHCisvbSPeftylo4e6UcHJIj2wL0X2CV9ms0ylR8Nuq3QYtdwVdyCb8Qfr-QUHUrke8cGdzPPsIKOeTofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd8931bae.mp4?token=ThskGIJe7FGuNi_n_JcB59A2oIVmGZW_C5bKhcaQTmiB3G8APvywzekzANDJdYbVwqYmphwjFqJeHIl012xeP5F336Vs7O1ppyXDnHvoa7VLwE0UX38nuHrvFp88owa6l4iNLh2g1MrHHWmV1zmx94O6Twr2AWLSwl_4w4kAub0yOmomuIX_xLaXTV8qh_V1Aoj4A9w9YiYwm1s6xtPMT7AGGt79qMrNotwWAJwmLKdvhLp-iyMkQ_iquNxyu1FpRyBBfHCisvbSPeftylo4e6UcHJIj2wL0X2CV9ms0ylR8Nuq3QYtdwVdyCb8Qfr-QUHUrke8cGdzPPsIKOeTofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه: ۲ کشتی اوکراینی را هدف قرار دادیم
وزارت دفاع روسیه:
🔹
دست‌کم ۲ شناور اوکراینی، از جمله یک کشتی حامل محموله نظامی را در دریای سیاه و یک شناور دیگر را در بندر میکولائیف هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/676289" target="_blank">📅 11:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ماجرای دستور فرماندار کاشان برای ازدواج فوری کارکنان
راعی، فرماندار کاشان در
#گفتگو
با خبرفوری:
🔹
ما برای بحث آموزش آمار می‌خواهیم برنامه‌ریزی کنیم و ببینیم آمار مجردها در ادارات ما چقدر است تا تسهیلاتی برای ازدواج جوانان فراهم کنیم.
🔹
همچنین آسیب‌شناسی کنیم به منظور شناسایی علتی که تا این لحظه نتوانسته‌اند ازدواج کنند و آموزش‌های پیش از ازدواج برای انتخاب آگاهانه را داشته باشیم.
🔹
برای اینکه پاسخ نهایی شود به ادارات اعلام کردیم یک هفته دیگر فرصت دارید این اتفاق بیافتد وگرنه قبلا مکاتبه شده بود.
🔹
فرماندار کاشان پیش از این دستور داده بود که ادارات باید ظرف یک هفته آمار کارکنان مجرد خود را احصا و برای تسهیل ازدواج آنان برنامه‌ریزی کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/676288" target="_blank">📅 11:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676287">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تلاش دیپلماتیک مانع از حمله تلافی‌جوئی ایران به بنادر اوکراین شد
🔹
به‌گفته مقامات ایرانی و غربی، در پی حمله به کشتی ایرانی، تهران در ابتدا حمله موشکی بالستیک به یکی از بنادر اوکراین را در دستور کار داشت، اما تحرکات دیپلماتیک اخیر موقتاً مانع از اجرای این حمله تلافی‌جویانه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676287" target="_blank">📅 11:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676286">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
قلعه لک‌لک‌ها و کوه‌های رنگی ماهنشان زنجان؛ از بی‌نظیرترین و زیباترین نقاط ایران
🇮🇷
#ایران_زیبا
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676286" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676285">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf3d7fe7b.mp4?token=UJLw02e4PMwgIAjkrB7Tm0SzlZbzNTuuyaa69CqiQy0l8SsqGpkoiR4xbyl-LxeWpJdS3nS16u1uvCTknMolpLzFzjchTMwBzIISmfabwOocKYBRjc5Qo6pzIgsR51rKPJU5Q44YsKkPf-UBth5YuZzvVgBWo7Smibbz70S27tuHTJa7-Z_U2E7lvrYrGdNfoNoMnlqKRPCuVBd8iWrcvsDY_XxoWfhBPGvaiqhDzQUEa1dWn0xzGRsTZFtGC9qcVJQRIRrKHxYhFJpFY0qSm-BY_yd1kUNC2UqSzvIYtWwEDv4KKYRFTEVAmQrJKTabbxesMcT30dOu7fVSLriL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf3d7fe7b.mp4?token=UJLw02e4PMwgIAjkrB7Tm0SzlZbzNTuuyaa69CqiQy0l8SsqGpkoiR4xbyl-LxeWpJdS3nS16u1uvCTknMolpLzFzjchTMwBzIISmfabwOocKYBRjc5Qo6pzIgsR51rKPJU5Q44YsKkPf-UBth5YuZzvVgBWo7Smibbz70S27tuHTJa7-Z_U2E7lvrYrGdNfoNoMnlqKRPCuVBd8iWrcvsDY_XxoWfhBPGvaiqhDzQUEa1dWn0xzGRsTZFtGC9qcVJQRIRrKHxYhFJpFY0qSm-BY_yd1kUNC2UqSzvIYtWwEDv4KKYRFTEVAmQrJKTabbxesMcT30dOu7fVSLriL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش شهدای حشدالشعبی به ۲۰ نفر
🔹
حشد الشعبی در بیانیه‌ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر شهید و ۳۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/676285" target="_blank">📅 11:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هشدار امنیتی در اسرائیل؛ دستور شاباک به تغییر سبک زندگی مقامات
🔹
در پی هشدار درباره حملات انتقامی ایران، سازمان امنیت داخلی اسرائیل (شاباک) حفاظت از مقامات فعلی و سابق صهیونیست را تشدید کرد و به آن‌ها دستور داد برای امنیت خود، روال عادی روزمره را تغییر دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/676283" target="_blank">📅 10:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.
🔹
جنگنده‌های ایرانی در مسیر بازگشت مورد اصابت پدافند دشمن قرار گرفتند که با تأیید آزمایش DNA، پیکر خلبان سرتیپ دوم مجید کاظمی به کشور بازگشت؛ سرنوشت ۳ خلبان دیگر همچنان در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/676282" target="_blank">📅 10:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676281">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
افزایش شمار شهدای حشد شعبی به ۱۰ نفر   حشد شعبی:
🔹
شمار شهدای ناشی از تجاوز سعودی- آمریکایی به استان نینوی به ۱۰ شهید و ۶ زخمی افزایش یافته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/676281" target="_blank">📅 10:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676279">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfUGOXgYoEj0sAMafutXLi7G6ejLICAbxiVaw52b-JH16rE-CL67OuVJvyBRsU65YBb0bRMOvowS_s73NZ9cfDxfCL1eTlfsuezn1RDDOMiWY74NpGpw54ZEB3zmUqGz1C35QY59sNEYK7hKOxaGLjdLIakBAKAdHYPzNuJkMht736ofcwkLrk50tLV5gjyvRhFrHNudAIOyW56mp0mi6pCUi1tBewzR6w45-VQ6sGk0wjgh1MAkqogjCAmsI90rb2WWtin1WTRFxF6077bdG2ywZZMojxGMHZ4x6r3UcRbJKQ7leKbRSdpEiYvf2l_sP0FyTbse2wINg-B48cPcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
می‌دونستید طیفای رنگ بنفش چند تا اسم مختلف دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/676279" target="_blank">📅 10:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc587e9bbf.mp4?token=ARisnuazcYEK7gWIgULmjXFIoZebv5LOVLUSaLIQFi4_GoxghO0yGY9wwgxnhZswUqSkhnirtJw7VGyDC8gxQ9w9BGeVuM0ZtYi6KmLAS9DpLdEhCQfwfU-jkjuJN6DsNeDMV_R4Z8HlU6ValhH8TKL0dJrG8imBwDGD3lkwoP1fjuPXqXtasuuIWUxIY44sMJf9wdndo-rAIPOwhs-g-o67E9KK_fdsOSbo5gvwa5ZU-BXVX_oKOjlWy3dpteVBsvxlaLo9_BRGX7NWp6LX6iF4f47IOo7FnUSneBH4thh2Hc4isVqfOrGPrfl4ypJbSxJJYSKCQ0ovx7sSTWFK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc587e9bbf.mp4?token=ARisnuazcYEK7gWIgULmjXFIoZebv5LOVLUSaLIQFi4_GoxghO0yGY9wwgxnhZswUqSkhnirtJw7VGyDC8gxQ9w9BGeVuM0ZtYi6KmLAS9DpLdEhCQfwfU-jkjuJN6DsNeDMV_R4Z8HlU6ValhH8TKL0dJrG8imBwDGD3lkwoP1fjuPXqXtasuuIWUxIY44sMJf9wdndo-rAIPOwhs-g-o67E9KK_fdsOSbo5gvwa5ZU-BXVX_oKOjlWy3dpteVBsvxlaLo9_BRGX7NWp6LX6iF4f47IOo7FnUSneBH4thh2Hc4isVqfOrGPrfl4ypJbSxJJYSKCQ0ovx7sSTWFK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی بدون گوشت و مرغ نمی‌شه یه کتلت خوشمزه و پرپروتئین درست کرد، این ویدیو رو از دست نده
😍
مواد لازم:
🔹
عدس
🔹
هویج
🔹
سیب‌زمینی
🔹
پیاز
🔹
آرد سوخاری
🔹
نمک، فلفل سیاه، زردچوبه، پاپریکا و ادویه دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/676277" target="_blank">📅 10:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ونزوئلا سفیر ایران را احضار کرد
ادعای خبرگزاری فرانسه:
🔹
وزارت امور خارجه ونزوئلا در بیانیه‌ای اعلام کرد که این کشور سفیر ایران، متحد دیرینه خود، را احضار کرد تا به اظهاراتی که «تحقیرآمیز و نامناسب» تلقی شده بود، اعتراض کند.
🔹
مقامات ونزوئلا، مشخص نکردند که به چه اظهاراتی اشاره دارند، اما ویدئویی که به صورت آنلاین در حال پخش است نشان می‌دهد که عباس عراقچی، اخیراً گفته است که ایران در مورد مذاکره با آمریکا «ونزوئلا نیست»./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/676275" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران پیشنهاد عمان را رد کرد
ادعای وال‌استریت‌ژورنال:
🔹
ایران پیشنهاد عمان برای تقسیم تنگه هرمز را رد کرد و خواستار کنترل بیشتر شد.
🔹
عمان که در آن سوی تنگه و روبروی ایران قرار دارد، یک طرح موقت برای ایجاد خطوط کنترل مساوی پیشنهاد کرده بود. اما تهران رد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/676274" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676273">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxpDq11L7v8NPAIpHSIZ17ee_pIBovzp2tmkF46BkrGbrImNPj7oXUT0k6FjAKeq-P723jbP42ih7KfBBybSvFUoV4SUiIc970xQ9-dD_QeXMlhjQOCHJi14fX_H1_XPoiE6qdL8C_TJhMowHkmUiFgJwSJPIhd10uqrp1Y6YPpimBI-UMD8UqXHMuBEywnicOUeD-msHBe80YkTpam-SJ-jxxYmUbrgVtMHpPTufafc3807xbkyPVGLq4WkOvai4q_XFaKjksV-OGuPSflvnqpMgkvswi8SaQ1WAcR5OVfZAP96Csl9NQXVfG1w-Vfn6JTw_OSrm2rHsXWluGh9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز سلامتی در یک فنجان چای ترش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/676273" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار پلیس فتا به زائران اربعین: برای جلوگیری از هک شدن اطلاعات گوشی، روی لینک‌های مشکوک وام اربعین، بلیت و اسکان کلیک نکنید و از وای‌فای‌های مسیر استفاده نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/676271" target="_blank">📅 09:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsJKEwoE90engAUU7pG8Ar2sPPeRs4yUI9MCE0-baWJqHSr0pV0cweZ1VswB6GA-modhnGeSyZKcEu_u6dKdKMrimtfi30F1Cwn71WWjCOFPlrkoKtbbub4ALR3aIgsFlF-rkGTa_9Xlil74EABjFC11sKF0t2GSPPCgDEXwdPBG72LmApnb2RoCR5_Wy2hmIyGwK69CDKyHmQEkPYLkraZu3DxW7zm0AQS5F3pfqLDnPZ2AYBCuYrmwaxsTA9Nvj4-Y2KcZjuX6RWsCQEOB6cJ35d8BoohcSx00dmmeNY8OcPtE0jR8Qj5DHb2AHeIvnSCrKKd2NxHjIOUZoKqY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش شمار شهدای حشد شعبی به ۱۰ نفر   حشد شعبی:
🔹
شمار شهدای ناشی از تجاوز سعودی- آمریکایی به استان نینوی به ۱۰ شهید و ۶ زخمی افزایش یافته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/676270" target="_blank">📅 09:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59d89d7bb.mp4?token=WRhL0vR7MhCWKqjwYmybUBDRzvtnZQoFNdifqwzQ1VvCrOgy3IAXTle4Dc3bdyvCe-RTxNf4otvX5sRrfiu8Biaa4SWx-wzEgt5pbf0pnStL2edkEeb3sG2Y2vfCYdokvPP0mJH0akARO8HkFOUwiBegDD5oUBdrIGFDdjXGvlSO7Enw5ChHN0JZNq2z2BWML-ThFGVpmzVVZGUGZz_45I1qt3sAgbre7vFtXR-KfxW2losyP-Fc0MpnPKEsEUexYoDE_320y_n5dMpse3lY2DVphVZ_zNdsOlC9wBfFZYWmxIP7T4DeFUCdbhYBHaSV6ooZpmkYZBObFAaG6t5voQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59d89d7bb.mp4?token=WRhL0vR7MhCWKqjwYmybUBDRzvtnZQoFNdifqwzQ1VvCrOgy3IAXTle4Dc3bdyvCe-RTxNf4otvX5sRrfiu8Biaa4SWx-wzEgt5pbf0pnStL2edkEeb3sG2Y2vfCYdokvPP0mJH0akARO8HkFOUwiBegDD5oUBdrIGFDdjXGvlSO7Enw5ChHN0JZNq2z2BWML-ThFGVpmzVVZGUGZz_45I1qt3sAgbre7vFtXR-KfxW2losyP-Fc0MpnPKEsEUexYoDE_320y_n5dMpse3lY2DVphVZ_zNdsOlC9wBfFZYWmxIP7T4DeFUCdbhYBHaSV6ooZpmkYZBObFAaG6t5voQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از شدت زمین لرزه دیروز در ژاپن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/676269" target="_blank">📅 09:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
منابع عراقی: در حمله دشمن آمریکایی سعودی به مواضع حشدالشعبی در استان نینوا ۸ نفر شهید و ۴ تن زخمی شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676267" target="_blank">📅 09:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad8f4b979.mp4?token=IOdhQ3BXDGJYT-nF_H9ka-RQGLXWcZUs7ay1FB7jBOlIPNCxiGMHcDIorTDhbB25XOIe4z2IEAqwlvlnq6pk1xK0-uZOkWeX7e1EPyYc7wh399JjRNegnfFE44XUY6bLN1y0Tz0cV_ENWQtyw6tCzZ_kr8iitoEGUe6FA5yAytL-hf3tI2spN856Z52ZXjtwuRkNvZuI7Idw9Db486AnMaQBrr80LhkBwuGe4U6tD-H5hkc7YvF9XaKsycqyajSuuyAjinVQwM9WQQMjH7gP0FOXOnvX23GxG8H74rt7znJ_diBvh2fEdjpzFeEUkTBGy5sJPegH3A90zPvZxei6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad8f4b979.mp4?token=IOdhQ3BXDGJYT-nF_H9ka-RQGLXWcZUs7ay1FB7jBOlIPNCxiGMHcDIorTDhbB25XOIe4z2IEAqwlvlnq6pk1xK0-uZOkWeX7e1EPyYc7wh399JjRNegnfFE44XUY6bLN1y0Tz0cV_ENWQtyw6tCzZ_kr8iitoEGUe6FA5yAytL-hf3tI2spN856Z52ZXjtwuRkNvZuI7Idw9Db486AnMaQBrr80LhkBwuGe4U6tD-H5hkc7YvF9XaKsycqyajSuuyAjinVQwM9WQQMjH7gP0FOXOnvX23GxG8H74rt7znJ_diBvh2fEdjpzFeEUkTBGy5sJPegH3A90zPvZxei6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالت‌های رنگی اینگونه ساخته می‌شوند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676266" target="_blank">📅 09:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b0a8dc2d.mp4?token=G3vGTYmPIzVJAHeXNktC8NmchvneOtiLoxGjzhnMus0knHDSB4bf7AD7zCvEi32xRonJ8V9RgFq1t_h-8aIhp4Y5TYB8Jrj2o6RcvSJ8BQX1aHV8Dr6x15NV8Ah5TxQwHovd9kp6ax8QEN4oVx3udFQDbVId079GYNa4KpSjdNs-FCWjVf8v8pQTdW73OTN-M8VS6KyL2cUA9ExEAsGOFouu2-ptTqCvSuAaFFy7eNoSBLRnLPuB6n4ne7qdee_Edc4wKCDgcbs1QsudUajrp8ff3g9DJTBxABu_twWKWwMqbcTelcSNKF7ViI-q2_wlVbIWFnEm5YP1BU8M9HQVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b0a8dc2d.mp4?token=G3vGTYmPIzVJAHeXNktC8NmchvneOtiLoxGjzhnMus0knHDSB4bf7AD7zCvEi32xRonJ8V9RgFq1t_h-8aIhp4Y5TYB8Jrj2o6RcvSJ8BQX1aHV8Dr6x15NV8Ah5TxQwHovd9kp6ax8QEN4oVx3udFQDbVId079GYNa4KpSjdNs-FCWjVf8v8pQTdW73OTN-M8VS6KyL2cUA9ExEAsGOFouu2-ptTqCvSuAaFFy7eNoSBLRnLPuB6n4ne7qdee_Edc4wKCDgcbs1QsudUajrp8ff3g9DJTBxABu_twWKWwMqbcTelcSNKF7ViI-q2_wlVbIWFnEm5YP1BU8M9HQVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله
🔹
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/676262" target="_blank">📅 08:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bb771389f.mp4?token=GHln63m8kBWpBphSWRE1NeUN_3hWwWJfhX83CkZFYQsF4YdyhEQeIND5saEb45mnhE87ayPgTY5_iXpLyXkF0CFylJP2mONBARwBTtgTyu6rTmPun4w074t76UYv51IExiNugS-fTjGAVpwPZwzfc7O3191eEUuiXpb34cQZZpsa5rsCSeYm_B4zznj6qr_KrJUhewsp32srRWzYDcGM3NcSNJ1R8t_stfmyryUc4Rt7q5gv2jOR67jjyySkwcyb_np4t5-mDS1PkCrur4Bi4lQQN0R-xDfqI0MP4cqFvOffUJdiMQFGWlggYzYFJKjoCSzhTu8MAwTLUGQL2_bO-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bb771389f.mp4?token=GHln63m8kBWpBphSWRE1NeUN_3hWwWJfhX83CkZFYQsF4YdyhEQeIND5saEb45mnhE87ayPgTY5_iXpLyXkF0CFylJP2mONBARwBTtgTyu6rTmPun4w074t76UYv51IExiNugS-fTjGAVpwPZwzfc7O3191eEUuiXpb34cQZZpsa5rsCSeYm_B4zznj6qr_KrJUhewsp32srRWzYDcGM3NcSNJ1R8t_stfmyryUc4Rt7q5gv2jOR67jjyySkwcyb_np4t5-mDS1PkCrur4Bi4lQQN0R-xDfqI0MP4cqFvOffUJdiMQFGWlggYzYFJKjoCSzhTu8MAwTLUGQL2_bO-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپیس‌ایکس ویدیو فوق‌العاده‌ای از اولین فرود نرم و سالم استارشیپ روی آب در هفته گذشته منتشر کرد
🔹
این ویدیو توسط پهپادها گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/676261" target="_blank">📅 08:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شهاب‌های آتشین در راه‌اند؛ بهترین زمان تماشای آسمان فرا رسید
🔹
همزمان با اوج‌گیری دو بارش شهابی نادر «دلتا آکوارید» و «آلفا کپریکورنید» در بامداد ۸ و ۹ مرداد، آسمان صحنه عبور شهاب‌های آتشین خواهد شد.
🔹
رویدادی کم‌نظیر که با وجود نور شدید ماه، نوید یکی از جذاب‌ترین شب‌های رصدی سال را می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/676260" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31262d9f8e.mp4?token=RYQ4HYUhIxM7wu9Mz-_XkHhVmQeCT8Pzh0XS3s_7IIzAQi8DIaYBF4xCJB_bq_mBqFINmN9ipMZuT1j3o6wzlddvjFZwv0rX3lQCrnt03HVw4zMWW2iOEVFKT5GP26uo0mH0un3_L6FBFu7_CvR6szFkraY61ntzqrg_o-iqcTKO-52Av3Hv34wDk8FcXA1qMfvRejh8WUsdX8CP4CO_d9ieUJwB0T23dmGw4W-90dgXbXszdauZOQZkwOPC17TZOa3A5ekOzqrAxfCvezAqTTfSNZ08m6UJo9pryZCCUHKKQaaWrxeyRvOmZ06bQo41KJQ6ewyZb8RknSwky8BpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31262d9f8e.mp4?token=RYQ4HYUhIxM7wu9Mz-_XkHhVmQeCT8Pzh0XS3s_7IIzAQi8DIaYBF4xCJB_bq_mBqFINmN9ipMZuT1j3o6wzlddvjFZwv0rX3lQCrnt03HVw4zMWW2iOEVFKT5GP26uo0mH0un3_L6FBFu7_CvR6szFkraY61ntzqrg_o-iqcTKO-52Av3Hv34wDk8FcXA1qMfvRejh8WUsdX8CP4CO_d9ieUJwB0T23dmGw4W-90dgXbXszdauZOQZkwOPC17TZOa3A5ekOzqrAxfCvezAqTTfSNZ08m6UJo9pryZCCUHKKQaaWrxeyRvOmZ06bQo41KJQ6ewyZb8RknSwky8BpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ حرکت ساده روی تخت که می‌تونه به بهبود گردش خون پاها کمک کنه
🔹
اگر احساس سنگینی پا، خستگی یا علائم اولیه واریس داری، این ۳ حرکت رو هر روز چند دقیقه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676257" target="_blank">📅 08:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نتانیاهو به فاکس نیوز: من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
🔹
هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.
🔹
موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/676256" target="_blank">📅 07:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwq9XLuhOZc3uk-9pniJFB-MutSO-fGJWhbTgnRuheptzSPhf_kJev9CzR6OoybpCF_Uq35IY8obo73glXhFZjk27bQEyP5S2uMw7aXxf9U-zmdBXC1ho-6j6NEZeS37BvYpv6NXbsOW-LowL0Npjb6flO4XCtRFtxi_04KXWDcyQXSJXsLv2frCs4BNQwcBLZfIN7JezG1t-4DpwMgBptIpxHxsSB3u7oHcwiOUjFVjuNPkcvyXOB2rNQC2LxKSwmf_EYrdJZepzgXcjakXLOdDCr4i6vYHxvNbI7tFdhQNjAD_WGj825PRbAQNzrZqW-cyvfvhnSW9e9pEgvKVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۷ مرداد ماه
۱۴ صفر ۱۴۴۸
۲۹ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/676254" target="_blank">📅 07:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXLc-pnJrGCrW285JaKu1qJnjI102peDYXzYl6RugWLNUFYkSxlUThNl93UmAJP6HjnBeNBA3GS_Ft__oXceCTBKAXvOwyvtyhVXXAlSHAWIPgCjN_1CVAxK2fSQrNaQlIEzfwM1bqnqzEJtjF7tbWpCa3FSvIaTKM4SpTZG4lPujykuoYkbJfTEMiJKdqf8DuUuLhXnZ9tktvTpy_Ypb_DPVwxExaLaBFrJZJ6iSm456sqbHKJNoAa9tXZYZgSUNfYq-pD2a6CcErS6SsrlgzyngOgy8GdjMqEtvp1BHAHTN9dM4K9iyqI09kqwVlBtRnAKL229gnF6eZS0JPEYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyY2IvGzogpgNqoOqg4MG187i2QQsrj252iO6naCFKZApYjQfGpScs5HvlJsCs5hXFl4W6ZsY0kXSyQFDAa7wkb1_qd2fe-3D-UduXAZS2KKEDAvZ5nG4YV5REwGNj46K9RBJp7mJFMl4kRbD2L8PKVY9BkfmHIm9ESwJf258HJVWdeQxOGLEF7X6iyo6pZGAafT8pgkb6BnY8tSZe-eGNKTy0V9FrB_oRwzBL8datwa74-VSn7UzgQ1Im9Dvmw_P2JVNPM5uClg8pO-W5pHttpVw7Xiexzbs4wytmjWsp3Gfliw03o5fUeP209EccWX7yTyrmDuk7knW12WZJpyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIpxsgWXXLQgAGP9VWDJD6TmOZmbjHxN_XTeD_dB9g7lugjDkOiQjWIoxiVZ8Mbr26zUU2HIFU9va0wSxFWYgrpoJ3a1SCLCQxdJzPhjdFhQLLDvh2IuZ1wGJn-pPAR_IFBmjJ6CEJJmFO8r_s0EMKTLSmlaXlp8XIbxLnBb545DkODuX53GZxNx3E8qaceH4mIPqhCljYOnnYeOqF_DLFqaoL12HqEz8KbGSUXaXxk-hpX-svItpfa5eZK6SSGXbUFmqbrzpRwVRfXGZE-mYnmmLraOVNwRAecbQ-J_1EXgGcKm5euDYUUDNlmjDSmZQVaJzd0Ey9iq5Y7Fv9MAEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احراز شهادت یکی از قهرمانان سوخو ۲۴ ارتش/ ورود پیکر مطهر شهید امیر سرتیپ دوم خلبان کاظمی به کشور تا ساعاتی دیگر
روابط عمومی ارتش:
🔹
این شهید عزیز خلبان یکی از جنگنده‌های سوخو ۲۴ ایرانی بود که در جریان حمله ۱۱ اسفند سال گذشته، خسارات سنگینی را به پایگاه العدید آمریکا در کشور قطر وارد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/676250" target="_blank">📅 06:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اولین واکنش الحشدالشعبی به حملات هوایی آمریکا و عربستان سعودی
الحشدالشعبی در بیانیه رسمی اعلام کرد:
🔹
صبح امروز چند پایگاه رسمی سازمان الحشد الشعبی در نقاط مختلف عراق، هدف حملات تروریستی نیروهای آمریکایی و عربستانی قرار گرفت. بر اساس اطلاعات اولیه، این حملات منجر به شهادت و مجروح شدن چندین تن و همچنین وارد آمدن خسارات مادی به برخی ساختمان‌ها و اموال متناوب به این سازمان شده است.
🔹
ما این حملات را تنش‌آفرینی بسیار خطرناک، نقض آشکار تمامیت ارضی عراق و هدف قرار دادن نهادهای امنیتی رسمی کشور می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/676249" target="_blank">📅 06:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
منابع عراقی: در حمله دشمن آمریکایی سعودی به مواضع حشدالشعبی در استان نینوا ۸ نفر شهید و ۴ تن زخمی شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/676248" target="_blank">📅 06:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676247">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۲/ پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت    فرماندهی نیروی هوافضای سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به اقدامات تجاوزکارانه ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه،…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/676247" target="_blank">📅 05:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۲/ پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت
فرماندهی نیروی هوافضای سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به اقدامات تجاوزکارانه ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه، پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن را با چند فروند موشک بالستیک هدف قرار دادند.
🔹
تا زمانی که تهدیدات علیه جمهوری اسلامی ایران ادامه دارد و اقدامات غیر قانونی و شرارت آمیز نیروهای آمریکایی علیه منافع ما در جریان است، مقاومت هم ادامه دارد. تهدیدات مقامات آمریکایی و مداخلات غیرقانونی علیه منافع ما باید متوقف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/676245" target="_blank">📅 05:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76e22916a.mp4?token=fgHrraenjUCHAAGZoQKYx0U-hed3EyJxZ2HDnOjtkAW7Si43NX7q6JMWlfELqFeTymRM2gMrxC-N8kUersfGCEiuDTGB1qnT_a_VNKbZAgLXvp1RJ7GrqYnsKi9w9PPnBGe9-Z-eF7zks4R4BeuLvbaL5McE3pf5qqUPKpOXFqFYSoejle2G1h2C3RrOiu3_2CafnlSGzMP-FAP1qO0IyUOCVcRJPAZsWoFLfyBQb5Wk4Lzm6jnnY_yUZ2MDitekvJevUb110G_H4xeaWnTB0aehj3Rem9r1FVHwHtWx08T7C2smVxEdez15DMKjaitrcSkx94zB3YWXNbfmcHHsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76e22916a.mp4?token=fgHrraenjUCHAAGZoQKYx0U-hed3EyJxZ2HDnOjtkAW7Si43NX7q6JMWlfELqFeTymRM2gMrxC-N8kUersfGCEiuDTGB1qnT_a_VNKbZAgLXvp1RJ7GrqYnsKi9w9PPnBGe9-Z-eF7zks4R4BeuLvbaL5McE3pf5qqUPKpOXFqFYSoejle2G1h2C3RrOiu3_2CafnlSGzMP-FAP1qO0IyUOCVcRJPAZsWoFLfyBQb5Wk4Lzm6jnnY_yUZ2MDitekvJevUb110G_H4xeaWnTB0aehj3Rem9r1FVHwHtWx08T7C2smVxEdez15DMKjaitrcSkx94zB3YWXNbfmcHHsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی-سعودی به پایگاه تیپ ۳۰ حشدالشعبی در استان نینوای عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676243" target="_blank">📅 04:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عراقی: هواپیماهای جنگی دشمن سعودی-آمریکایی همچنان بر فراز شهرهای کربلا، بابل و نجف در حال پرواز هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/676242" target="_blank">📅 04:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c0612bb1.mp4?token=mB5X4XANX5Icd_yy3AQBOutOyj9cyQBllqNAmdS95Z8WUz2ib9MLtbNLFfcIPgxfj78e_tmyaLJ6aFHFQDlqIGbfffrObv4SxoCwMUFlRqcmvrqRQOejzcGzsQURaJgkV_v8pDT1xnmo36VEN92FePPpCxw-HiNc0jFlxqowEAR7H4kfeiq0qTujGLMQRqd7_7ehAzh1NTOlgjZZrJWq9CSG7U_Ja-XLy09-bCNnsZRxDZrFt8ABm7ILzJvyee-EFCImRWTbs95iJVhjLn6lxDvWk7Jd1_J7EXcSYI_ldl7QTd-cnL62cQNrxEsBGwoNUCPuzgZ4SoD7uqgqgTdqMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c0612bb1.mp4?token=mB5X4XANX5Icd_yy3AQBOutOyj9cyQBllqNAmdS95Z8WUz2ib9MLtbNLFfcIPgxfj78e_tmyaLJ6aFHFQDlqIGbfffrObv4SxoCwMUFlRqcmvrqRQOejzcGzsQURaJgkV_v8pDT1xnmo36VEN92FePPpCxw-HiNc0jFlxqowEAR7H4kfeiq0qTujGLMQRqd7_7ehAzh1NTOlgjZZrJWq9CSG7U_Ja-XLy09-bCNnsZRxDZrFt8ABm7ILzJvyee-EFCImRWTbs95iJVhjLn6lxDvWk7Jd1_J7EXcSYI_ldl7QTd-cnL62cQNrxEsBGwoNUCPuzgZ4SoD7uqgqgTdqMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی می‌گویند که پایگاه‌های «الحشد الشعبی» در استان‌های کربلا و نینوا نیز هدف حملات سعودی-آمریکایی قرار گرفته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/676241" target="_blank">📅 04:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
رسانه‌های عراقی: حملات موشکی و توپخانه‌ای موکب‌های حسینی و زائران را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/676240" target="_blank">📅 04:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آمریکا: به همراه سعودی به عراق حملاتی انجام دادیم
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که به همراه ارتش عربستان سعودی، حملاتی را علیه پایگاه‌های مقاومت در عراق انجام داده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/676239" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
آمریکا: به همراه سعودی به عراق حملاتی انجام دادیم
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که به همراه ارتش عربستان سعودی، حملاتی را علیه پایگاه‌های مقاومت در عراق انجام داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/676238" target="_blank">📅 03:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109dca722c.mp4?token=Ivxbu5coZyDNcApHYB0K7aZjWutdCauklql1GnYeYCwXS37mO77ktivHpK7tPYaHPCA3hyMmVj1_VT5t0x0oUa7QIUztiYC6K4i9UoCjUkSDrG_fSmkKzVxClUK0Zabaalk5YdpVSRkT1j05w0IygY6_6frWA4xs09kVJdPKOm8erovcjBFgxlXsnp_0NWAXVMQjMiNtwvAlNkSMJcCMLG5bV1YbZTk3D9d4tFzeIZ0EClawG5WcGOhfRcFIbIheITWWhOGwbiR8iXCJ71rLXZByw7jN_6DbSTIE9PFgC3h-GhqI54lgr4j5kgswSJTyVHkcJHlOx9P0xtteMtHzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109dca722c.mp4?token=Ivxbu5coZyDNcApHYB0K7aZjWutdCauklql1GnYeYCwXS37mO77ktivHpK7tPYaHPCA3hyMmVj1_VT5t0x0oUa7QIUztiYC6K4i9UoCjUkSDrG_fSmkKzVxClUK0Zabaalk5YdpVSRkT1j05w0IygY6_6frWA4xs09kVJdPKOm8erovcjBFgxlXsnp_0NWAXVMQjMiNtwvAlNkSMJcCMLG5bV1YbZTk3D9d4tFzeIZ0EClawG5WcGOhfRcFIbIheITWWhOGwbiR8iXCJ71rLXZByw7jN_6DbSTIE9PFgC3h-GhqI54lgr4j5kgswSJTyVHkcJHlOx9P0xtteMtHzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی: عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676236" target="_blank">📅 03:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منابع عراقی: عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/676235" target="_blank">📅 03:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
العربیه: همه پروازهای شرکت هواپیمایی امریکن ایرلاینز به دلیل یک نقص فنی (اختلال در سیستم فناوری اطلاعات) در سراسر ایالات متحده متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/676234" target="_blank">📅 03:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7a73c822.mp4?token=DfXCmuAFswpT40L17ICh0MMnyHDbSpG_r7F1-JdIwTsm74fyzz6gTBu5io35pbHmcgKKsB5Cer3ISIXeFSuYJ9ZrbI83cJeYDTOjvb4xTAiydpcdhvaqRuqXrxw64menfClHx-xLUO8g3mUKEAZKPmeaI-DmjEt0T90-geJ-mEpClriz9IiEt9kW4mZaOjC0cDS5KJn1gN7Scw4cwLowAf0yfN_0f7SOjC5Aql4I9QwhyI6oOlcj30jF62zKgTfvgO-vvNswJX182aQju4osxZQxSJOzenHmcb7OcgqoJLJqrmmDOpoM2qSnF3z_TRxeiVwLmgatWR5yCt-fjWAr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7a73c822.mp4?token=DfXCmuAFswpT40L17ICh0MMnyHDbSpG_r7F1-JdIwTsm74fyzz6gTBu5io35pbHmcgKKsB5Cer3ISIXeFSuYJ9ZrbI83cJeYDTOjvb4xTAiydpcdhvaqRuqXrxw64menfClHx-xLUO8g3mUKEAZKPmeaI-DmjEt0T90-geJ-mEpClriz9IiEt9kW4mZaOjC0cDS5KJn1gN7Scw4cwLowAf0yfN_0f7SOjC5Aql4I9QwhyI6oOlcj30jF62zKgTfvgO-vvNswJX182aQju4osxZQxSJOzenHmcb7OcgqoJLJqrmmDOpoM2qSnF3z_TRxeiVwLmgatWR5yCt-fjWAr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع چندین انفجار در انبار مهمات یک مقر نظامی در استان بصرۀ عراق خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/676233" target="_blank">📅 02:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676231">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnWjgnjftx2oN6-q986QckfqO9zy-YfbyiLIgYZx0wM3JOFrheoa3c5c2VrkTU9srSK_q1i2TEYGCpIaawfzRRv9FrRMD7INnwhgh3VUwHm5ch5_JWFhWFqv0VPxIq-nR1swJqn5aKUV1DfoMJvQSX2nLBXZse9KVCgFTgX0kdt4_PuEzEx8CO6MXxYdBWWG6XLw-PyeApQJfUkDNV1D6E05FaQVnNQdLlNtp2-SOio9I4Cu9Jk2sMaWk0Kyf2wXXFntuzm_kHDRARgn-8nbrFqe41dGXezIP68W5_zVko2qFbdjja1MUhb4fBr0uga3jOUWdvFZJh6UluIO5mHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت پس از حمله ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/676231" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676229">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای سنتکام: ساعت ۱۷:۴۵ به وقت شرق آمریکا امروز، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از خاک ایران به قصد حملهٔ غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه پرتاب کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری و منهدم شدند. نیروهای آمریکایی همچنان در حالت آماده‌باش کامل و هوشیاری بالا به سر می‌برند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/676229" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676228">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF0eadyl864duK7SdSuZjLgySfZNFqPH48ZiqRnu2VR0pJgnCicc-ZN0oeKnsRQnZ_25F9WPDZiee8g23Q55_OpqSuHbCkHp-_7SIY0gZNSvG_L3LoP9UOB9ASJga_y9892IIlYY8z8GShDQgzBZ5pK4YmLnRcnCP2FnHpt1oaJOKpCHxTotPQcJ3l4Cv_Jrj4A-aHcClrCmMzFQ7T4N6dZMAvFT46z09ON4GgCkIJUFnVv2LCGjAGygL3dtA0c15S_cx-wvMerAkUYVw8rZgXGIMUhMMupiLA8UPutvuL4kQhV3MNHYuvtX9FHECxBQh-EbIY4VeX7miBsBqg9E7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعطیلی تأسیسات گازی در شمال قطر
🔹
در پی وقوع یک حادثۀ نامشخص در تأسیسات گاز و میعانات رأس‌لفان، فعالیت و صادرات این مجموعه به‌صورت کامل متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/676228" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676227">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای یک منبع آمریکایی در گفت‌وگو با  i24NEWS: ایران حداقل ۴ فروند موشک بالستیک را به سوی یک پایگاه نظامی ایالات متحده در اردن شلیک کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/676227" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTRRzBKOHKrbtsofcv77MrqF0a_-KPm0sFQ49KzJt-RUzCZ--07c40p9BDRN3XKbmzcOk96KZ78TotdAlNEwKaZSMpnt3DKvijGRSssfwFhmHjMt25rpocQtKypghK1VjbFGqNKG0BWnhvwC_vPQcDuy0Dk7CkGuzc_NXlei-EMJXh7zphOUx5KnB-kW_e_v3EFjzaW4PVIs4uuWYM-i54zZy2y9_hzafkaa6eYYiWYZv6pzx5ONgjaaAn5NQlZX2wmp1lVE-ErX34vYc81SHfobGjL8aA4QWcmU_dDcJ1yRWIVqTDdJW3O84myFh2IchDIOHEEL5LDF7ggjJFznEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db00447bba.mp4?token=Qjm6Ym8eamxt1KtkGGSsITtpKriL8sMQJQDVmGqlVbzyw36bBGjLfxA0xE59d6nWxw7xsas6jBUdSpw_kVJnRvZj69DnJIHiXCEa5sw27loJ_1mzbpfs9tb_FpfxXYm5kXmMWnFtx4QGeLgTLVEw2YsEa8R40VSoQ70EqI79btDhYGKhMv96hf51p1zImGZXwDFj1yaELl6IHgrFyjrkHcF8x6pSVhd_AmYIMaoEfjVT_GFhEpWMKD3m2DBAcTd2NW517MW42gkYUr4rq0X84x8H4G1e4vAvkoOdn5pXms3KI7wRlBttwmhsjMOabL8RUv5cOeREY5eQRMTch7Dp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db00447bba.mp4?token=Qjm6Ym8eamxt1KtkGGSsITtpKriL8sMQJQDVmGqlVbzyw36bBGjLfxA0xE59d6nWxw7xsas6jBUdSpw_kVJnRvZj69DnJIHiXCEa5sw27loJ_1mzbpfs9tb_FpfxXYm5kXmMWnFtx4QGeLgTLVEw2YsEa8R40VSoQ70EqI79btDhYGKhMv96hf51p1zImGZXwDFj1yaELl6IHgrFyjrkHcF8x6pSVhd_AmYIMaoEfjVT_GFhEpWMKD3m2DBAcTd2NW517MW42gkYUr4rq0X84x8H4G1e4vAvkoOdn5pXms3KI7wRlBttwmhsjMOabL8RUv5cOeREY5eQRMTch7Dp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایرانی به پایگاه هوایی «موفق السلطی» در منطقه الازرق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/676225" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
یک مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/676224" target="_blank">📅 01:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac506c8b95.mp4?token=DYlw5H1vx7sdYrICXDWdrfMd7PhdIxNfBzETkGNGj7lUJYak8i5_d8lvsMPcljjd17jdMJN3xxz5ZmK9lxL2es0gw6GQ9t-4oSQdMkUB-OrgC_DmZ07IppF0LRxhiFCdg6HUYlpQtBoeJij4Kv79DiPXiExml6fyR5z9fj0TIZfNLip30rRdmiNlhhwcQV0oVhdwiWgoZcrQWOeiS8TMN18x5NyZCKUuJipxaC51byKqkRjn_bqkPrcRNhneoES2PafgTlfzDHaL0hprJsRTykCAjs7ZyNUwPRPQs9YopoqCv_6WnGR5mPo9ej-YJ1-Fx5M4HkPsWeRtskE0UsKqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac506c8b95.mp4?token=DYlw5H1vx7sdYrICXDWdrfMd7PhdIxNfBzETkGNGj7lUJYak8i5_d8lvsMPcljjd17jdMJN3xxz5ZmK9lxL2es0gw6GQ9t-4oSQdMkUB-OrgC_DmZ07IppF0LRxhiFCdg6HUYlpQtBoeJij4Kv79DiPXiExml6fyR5z9fj0TIZfNLip30rRdmiNlhhwcQV0oVhdwiWgoZcrQWOeiS8TMN18x5NyZCKUuJipxaC51byKqkRjn_bqkPrcRNhneoES2PafgTlfzDHaL0hprJsRTykCAjs7ZyNUwPRPQs9YopoqCv_6WnGR5mPo9ej-YJ1-Fx5M4HkPsWeRtskE0UsKqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی در آسمان اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/676221" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f64ca23e6.mp4?token=jyPdm-Cwd59JwbvkqClg9DP8igvdJPzYoLCRuYm857XvA0jxbd25yPtU-FwTsQulsDYc8A3jbhqH8iDYs4vVoxZ4hEcKvYVFHMp_r78cc_uOIfm84dzbLACITP-sja0Asg7Flkf2BnLwsmEbsVNw-mNYM4_VZzo5sJowc0KxGmrPdPACB-JJft_G_zsIigPbm7-tCLCfwzSDe9DfBw-gOyT6m61qtLTQ71DBpd1F-JGPX1q2CxD8VkxHVQ63Zf7VtWDzyeMlM8xsnZn3n9-UCLjqn6kSjPMkoEmIDWF7PxSk4Y5Tzx8_ZQqgSKDf5E56jFxA6AJVceN1YIRoxApYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f64ca23e6.mp4?token=jyPdm-Cwd59JwbvkqClg9DP8igvdJPzYoLCRuYm857XvA0jxbd25yPtU-FwTsQulsDYc8A3jbhqH8iDYs4vVoxZ4hEcKvYVFHMp_r78cc_uOIfm84dzbLACITP-sja0Asg7Flkf2BnLwsmEbsVNw-mNYM4_VZzo5sJowc0KxGmrPdPACB-JJft_G_zsIigPbm7-tCLCfwzSDe9DfBw-gOyT6m61qtLTQ71DBpd1F-JGPX1q2CxD8VkxHVQ63Zf7VtWDzyeMlM8xsnZn3n9-UCLjqn6kSjPMkoEmIDWF7PxSk4Y5Tzx8_ZQqgSKDf5E56jFxA6AJVceN1YIRoxApYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت شدید پدافند اردن هم اکنون
/
برخی منابع می‌گویند پایگاه آمریکا در اردن هدف قرار گرفته شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/676220" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676216">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjFAgZW0RCf_vb-S1WTiSj9-0Af9NWkdKObTTfz7YzfLfleTXSuAWzjqt7X2DgTHAqJ4jPpyUBMom0uZR_dmlYpuY2eunXFsM2UvZpHlcGjCygySdTTv7fRvyFfuZ9SXSTDZ8pYOhsEbNdBt1DEUbhTlZra6PxfGpWqOAjtwb-UpGQ5Ng62m6hiMpAKgbf0-HKfsi7Q84fSKwcn2J_K7QO223_GmHcnqK5SmvQtaPywa8xm3-I8AY1NEXCLYFT-6G5TNfV9BgEnrOwng1fXGao52Ok3miTCPDyPsPzPMmLRi_TkIYhwebOHEu2nVzGLjeDqjhGFlVzBvcROLzcKKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYSldc6O0VK8SR-fj8ZL88aqFzuzO0iagWpCKkhlTFDn90ZDbOd6rWDKkWvoDbm34rfZYODs7MP-UWqUnhDjr9_UCnLTNUSsZjJfNJQyKTat0iNx3xA_aSmSNsaW_yWZDn53-sw9NXYoXJD9UPUGqunzbM410_lSPIYzjeyLRqNl9kphYDFtkzfsWrakMhsVjbW-Bf4TzpjGCKdQj_tafteAs5VR11am3Ne3apBpz_Qxx7NM-uY7AuxA7RDW9tYLgbeURwATTLQISWhlZDrsQWH3oNUWPs9VTFeU_9nKhspadlh-aAyu_Tud1U5txWogp810OmO-Bj16-yAiBibhYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=kWyHkqnmpinTvQlA_O0Q_gs1lCvi39mAf6r7wlE5LzS5SLBG5_OWyKz1Nvh0xLLxsqftIXyZuWchOawHYsaxLKytgXPEQXbEUWyPQ5GhNSAcFYPLubpBg7s5W-zNgX-FhpEu2VipbnpVKhJAZ2ucq3EHHR0LxyFGxNzIwLP9w02ie0iZ79s-V5r5CTGaJgNjOX8RakN8kLLirVuvn7lq6dPMsbK7ZidBS-r7mZtjroG7Z-qEXz24dke-9ZZxANUGY3q1LctvpM-ZNVqnJhoyS55IuXSgCTlLV35j9C5L_cAkL4ieqvOh2MyjhgdAnAX4flIazybcBgq-khsxrnuQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=kWyHkqnmpinTvQlA_O0Q_gs1lCvi39mAf6r7wlE5LzS5SLBG5_OWyKz1Nvh0xLLxsqftIXyZuWchOawHYsaxLKytgXPEQXbEUWyPQ5GhNSAcFYPLubpBg7s5W-zNgX-FhpEu2VipbnpVKhJAZ2ucq3EHHR0LxyFGxNzIwLP9w02ie0iZ79s-V5r5CTGaJgNjOX8RakN8kLLirVuvn7lq6dPMsbK7ZidBS-r7mZtjroG7Z-qEXz24dke-9ZZxANUGY3q1LctvpM-ZNVqnJhoyS55IuXSgCTlLV35j9C5L_cAkL4ieqvOh2MyjhgdAnAX4flIazybcBgq-khsxrnuQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که از آسمان اردن در منابع عربی منتشر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/676216" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676215">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5hNIRZUQnMZp70oo0sNCywKCeFLrUxByF_voIi6EPaCIOfLtgQWgefd6mPcoiTRUlKH7iMj4OdXwYnkABM_s3ykk6X1qPLfnYUcpbZuYlhCwarbJB2bVlEygf2pWeY5iEZzD8MPSwk6pD_tZiAAIBs84o0ISW0OknAYcv5uqAs5USQ16wNVV5ZkEDaVNMYGI1JtzTi8BvuHW6W-jGdZOn2nHxLbBc3rBL8pnhDpDJJc9sSY4voRQzxH7W_2jJLLaBzijrf3RniVStcA6VHbqJb1IxcdcVhGfyXC149ok-a5wNw-6fmeOqRtJwVi1n9viOwCagg3-uOHbRc2bCQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجارهای شدیدی در اردن رخ داد، همزمان  پدافند هوایی پاتریوت اردن فعال شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/676215" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676214">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه آمریکا در اردن
🔹
رسانه عراقی بامداد چهارشنبه گزارش داد که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است./ فارس به نقل از صابرین‌نیوز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/676214" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676213">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
روسیه به دو کشتی اوکراینی حمله کرد
🔹
روسیه دو کشتی اوکراینی شامل یک کشتی فله‌بر با محموله نظامی در دریای سیاه و یک کشتی دیگر در بندر میکولایف را هدف قرار داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان روسی دنبال کنید
👇
@AkhbareFori_RU</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676213" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7906f25da6.mp4?token=OPZ6XxiTxzmWdox293rn1bAL7A3umXUosW-rJEVUxh7yPOX-jgKLl4Ci9whZtuR4cjDXp02DiX6xJ_H03J1AdAmZNuG-muzxRKyWXL-UPoqsnfEGh6YSgxaFo5CUh24vK5KZPO6-mjl-seoKEe1BVDLBbdc48y5-MCcqtmR8e2CoEDK_bX0-i8o9LEAI-lp68R5F0QVIgGkzwq9lPS9DGaZXO2rWVtgf7Tq0avgvyoexfHdfq9nBIAvMQiiOQp11nObWaffOOj_EUSCGU7IJzqi9CM59u8_x23UBH7C_gujdJ5BIOYgPTgrCtRSvKPvWbnSKVJq6_6hx3E1w-l9obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7906f25da6.mp4?token=OPZ6XxiTxzmWdox293rn1bAL7A3umXUosW-rJEVUxh7yPOX-jgKLl4Ci9whZtuR4cjDXp02DiX6xJ_H03J1AdAmZNuG-muzxRKyWXL-UPoqsnfEGh6YSgxaFo5CUh24vK5KZPO6-mjl-seoKEe1BVDLBbdc48y5-MCcqtmR8e2CoEDK_bX0-i8o9LEAI-lp68R5F0QVIgGkzwq9lPS9DGaZXO2rWVtgf7Tq0avgvyoexfHdfq9nBIAvMQiiOQp11nObWaffOOj_EUSCGU7IJzqi9CM59u8_x23UBH7C_gujdJ5BIOYgPTgrCtRSvKPvWbnSKVJq6_6hx3E1w-l9obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر فقط ۳۰ روز قبل از خواب گوشی رو کنار بذارید چه اتفاقی می‌افته؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/676211" target="_blank">📅 00:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0ae10294.mp4?token=MClRjqp04HNBmrAhQGw-FpkBA3lCyhHXYiMerMRGsj_Lelajs52_IiXS64nSMx9KRcbDHNQa8hJZaZpM6PLXwz8BykqUBkHpOEWgO6D3AsWdQ-rCq6miLhYJDiHX34Kc1GDqj2whqetY7QpRmxSpIDG8nJVol-6cU3_FGLsNTtgvMRe9F5x_IUKlGC1Ws1kipNgQsFC3ZbJsXlFUulMw61-mNOj3fODnz7NKfLV-yb3Yg5R0X5mNMMqXWZqFUKMPdDzBO6Z6knGJWk8SPQcyAhl59yMhtDGr8giOsyn_xePJMYwOJReTnyNt75Nt8yjZuL5V7KQNyulgALE8ZCSFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0ae10294.mp4?token=MClRjqp04HNBmrAhQGw-FpkBA3lCyhHXYiMerMRGsj_Lelajs52_IiXS64nSMx9KRcbDHNQa8hJZaZpM6PLXwz8BykqUBkHpOEWgO6D3AsWdQ-rCq6miLhYJDiHX34Kc1GDqj2whqetY7QpRmxSpIDG8nJVol-6cU3_FGLsNTtgvMRe9F5x_IUKlGC1Ws1kipNgQsFC3ZbJsXlFUulMw61-mNOj3fODnz7NKfLV-yb3Yg5R0X5mNMMqXWZqFUKMPdDzBO6Z6knGJWk8SPQcyAhl59yMhtDGr8giOsyn_xePJMYwOJReTnyNt75Nt8yjZuL5V7KQNyulgALE8ZCSFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم منتشر شده از دفتر لیندسی گراهام در روز حمله به ایران #Trash
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676210" target="_blank">📅 00:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc7b46a21.mp4?token=dvqa_JpnGl4O0UWQI11_7RPMV88h8-ALkQ1ppxtBSku-8U3zSuKOBBmuTagHwL7zp22r6ie2usMEWwOU71vk0h99bRn-5wT9K0QhYwlo8-9xnGpHIKRKbEzTvtHQRx5utspSJk6dT40i4PE42U2Z34j1IqA7ZvIpBOwNxN3Mvcfz0VMFSEkXkFD9O4MIunvLjVb2KeciXP4EK052At49kmsoJkCrfxBdKLwOzzamKZEZuQgdrJAYIxXcD_XhHPUqu4xxgulmd4xW6KABZCZBi1Ov23uvptVNwF3eYeBUwQFkQljHJywxdxDlxbOqD6516lGGGVHCg2x7NYGI-esNMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc7b46a21.mp4?token=dvqa_JpnGl4O0UWQI11_7RPMV88h8-ALkQ1ppxtBSku-8U3zSuKOBBmuTagHwL7zp22r6ie2usMEWwOU71vk0h99bRn-5wT9K0QhYwlo8-9xnGpHIKRKbEzTvtHQRx5utspSJk6dT40i4PE42U2Z34j1IqA7ZvIpBOwNxN3Mvcfz0VMFSEkXkFD9O4MIunvLjVb2KeciXP4EK052At49kmsoJkCrfxBdKLwOzzamKZEZuQgdrJAYIxXcD_XhHPUqu4xxgulmd4xW6KABZCZBi1Ov23uvptVNwF3eYeBUwQFkQljHJywxdxDlxbOqD6516lGGGVHCg2x7NYGI-esNMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/676209" target="_blank">📅 00:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm8MRxRwYMsROOEeh5ykdPDPHXvKQphx7iOfH4qAFIbsvrkyhttJf8JXP7-JMpi-690qlCdgcqaf6Y0Q140HeoCJMFh7w-XiBgBvKyXr9ESGTYsPvOeID9-fG8y-Tu2i0p9pSeBnG47a48z4XLBpEMiI_gaByGJ-kMYTXxHtKyWiRvWgSCPK1utZHz6Eci5BTohLRBqMvhmK7-9EXm-gZCX2QUYpOvFwevN7Tr9-cd_O7F6XsZ4D5VHAA4CuaYQ7oyLWWgoi--OYKU3tyud2vbRheN1D2MjlBkcnsWLIFxbb0zyJbPzOwk8fRhQ362dTFRZA4POIrOlP0V-OnWm3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان رسانه‌ای خبرفوری در مسیر کربلا
🔹
کاروان رسانه‌ای خبرفوری روز گذشته وارد نجف اشرف شد و پس از زیارت بارگاه نورانی امیرالمؤمنین (ع) پیاده‌روی خود را در مسیر نجف به کربلا آغاز کرد.
🔹
اعضای این کاروان این روزها همگام با میلیون‌ها زائر، در مسیر عاشقی قدم برمی‌دارند و به‌زودی به کربلای معلی خواهند رسید تا در آستانه اربعین حسینی، به خیل دلدادگان حضرت اباعبدالله‌الحسین (ع) بپیوندند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/676208" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTu7ZOlf4BCRZGjWf3GyygHg2XvVnZn9a-c56eHOsbT7D-jVA4NJWytJw-YJDdT9BlamI9PTQSRocNJVtUq2oiLZ7uOv2qY0w7BHSOMpWeVooji2Ev4uNkJlclmLJ7uiStGbec8Z8crBrW7tk3BPAuKXLqhHnyWinFYtxRvy00HinHM2wlcFRbj8dtp6bVnKLzbkVvzcarI6sikUrG1u32SWgYpnLF5TjdotZN4A5CsTBWnuihdso63nUOXTmKuWUkiqFhhfZANGiPCsgHLnZaYjKtlcQLdxY77rOMzfio7NVYBhjm7FP7Cw6t4KC_eDg0_BRRT6dEobmZ8rwgY4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ اوکراین و ایران چگونه خواهد بود؟ / مقایسه توان نظامی تهران و کی‌یف؛ در جنگ فرضی کدام یک پیروز خواهد شد؟
🔹
بدون شک توان موشکی ایران به ‌مراتب از اوکراین بیشتر، متنوع ‌تر و راهبردی ‌تر است. ایران یکی از قدرتمندترین قدرت‌ های موشکی جهان و منطقه است، در حالی که اوکراین در این حوزه یک بازیگر نوپا و وابسته به کمک‌ های خارجی محسوب می‌ شود.
گزارش خبرفوری را اینجا بخولنید
👇
khabarfoori.com/fa/tiny/news-3233826</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/676207" target="_blank">📅 00:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJrsjnzQGOizezEeNrqW6RO-99i_GrGOqhb9-fioGxhv_uaBVl8aWvQ_dIf9UXEOIs-Ed5JV1urhU88lFCHBAKSo-3My13clkl3rwa8AYRMZTSuqQX4eGqWopc4wFSg08mOY-8rFbpMgghPeHmpgQlllsahHmBS7FfK1_T1kobSfJhzsoQYijXAmqi0gqTQXd8ZZgryvn37KTb1wrjtFGpsEaPaWpIpvMRpZivXXx0fO8h5v0FtdvwsSVpLXOHCGBwGTBOSH38oD91xiq491DC4GokRrQtjpJ1OXY3luvU8xDcxQjNe3WLltOTsayEa1bTG68nIEh08RN3iAifTr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676206" target="_blank">📅 00:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فنی‌وحرفه‌ای موظف شد بیکاران جنگ را با آموزش به اشتغال برگرداند
غلامحسین محمدی، رئیس سازمان آموزش فنی‌وحرفه‌ای کشور در
#گفتگو
با خبرفوری:
🔹
سازمان آموزش فنی‌وحرفه‌ای طبق قانون بیمه بیکاری، موظف است کارجویان و افرادی را که به دلایلی از جمله جنگ بیکار شده‌اند، از طریق آموزش به اشتغال بازگرداند.
🔹
سایت سازمان فعال است و هر فردی که برای بیمه بیکاری درخواست دهد، به دوره‌های آموزشی معرفی می‌شود و امکان شرکت در این دوره‌ها را دارد.
🔹
این آموزش‌ها با توجه به نیاز بیکاران و کارجویان و همچنین نیاز معاونت روابط کار و سازمان تأمین اجتماعی، در سراسر کشور در دسترس است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676204" target="_blank">📅 23:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d58dc1ad.mp4?token=PgA7OzT1d5cCsHuHUgNWVVWx0MPYKpNCQZA4s1FQLhiGASDswzaOecjp_0_LQewGGNeEzVG8xbWbnIcYoUIlcNauaEh-0fk6ifX1I0WcLI88RbjvVYoXyMtb-uxPiBr3Rc31OBsIfqQOAZTn5tT9H8odlfK4XTzgFNzG2CGFYtS-R16QaW9Lt_6nfN7h7ptfuJbBS1u_UyZoMOoa0JoAyM6pFXUWq2li_Wq3y0LP20muN8WYSZJKO6eBABuHvS1RzuKlpwNnAtWKqyNzhw1hNMzL4R1YIEpbI6jjOvey8y9LMcffze7iKp4G7rC_L-uuDzAmriYtcT1TK2Or4BB2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d58dc1ad.mp4?token=PgA7OzT1d5cCsHuHUgNWVVWx0MPYKpNCQZA4s1FQLhiGASDswzaOecjp_0_LQewGGNeEzVG8xbWbnIcYoUIlcNauaEh-0fk6ifX1I0WcLI88RbjvVYoXyMtb-uxPiBr3Rc31OBsIfqQOAZTn5tT9H8odlfK4XTzgFNzG2CGFYtS-R16QaW9Lt_6nfN7h7ptfuJbBS1u_UyZoMOoa0JoAyM6pFXUWq2li_Wq3y0LP20muN8WYSZJKO6eBABuHvS1RzuKlpwNnAtWKqyNzhw1hNMzL4R1YIEpbI6jjOvey8y9LMcffze7iKp4G7rC_L-uuDzAmriYtcT1TK2Or4BB2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انقلاب رباتیک در چین؛ پیک‌های دونده رباتیک با سرعت ۵۰ کیلومتر بر ساعت از راه رسید
🔹
برخی از پیک‌های تحویل کالا از تجهیزات حرکتی مجهز به نیروی کمکی استفاده می‌کنند که می‌تواند سرعت جابه‌جایی آن‌ها را به‌طور چشمگیری افزایش دهد؛ به‌طوری‌که برخی از این سیستم‌ها بنابر گزارش ها قادرند به سرعتی تا ۵۰ کیلومتر بر ساعت برسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/676203" target="_blank">📅 23:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQfuaiDGlZdeNY2f7dMRgI8swqGGrEDbBBSFgNXKTHGguoGeAwWgVAtnl4Wrbw8D-o8sG9c84jJr1wwjD8Da6w2EI8b64bqjXUCegUZ5Pz4dIO51BKmtMqKX4RS2YuIazFkQVk9Pgvedl4Jgf-RV0bV6ydEYAX_0kWJaRlzWzFSLGfIfjiAeeoJjXv1IgGBbL8HzhXJNy0txLSpkenfEUbjcvndwWbXOkwNGX5RSoI4uVhAtJ4cdPsewA_VGmAxeHITYSyumOquQnhHIbHpvwS7ylehy2cspexQ6SO_LcGg5EWKGYhA-yO9pMti8xFwWGCQp-qCeuZM2OvrHrmJAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlIy5Zw-k5yqNtzhRBin73qRrQVQ084D68PSnjOIQRmBdzmncArhEPV9upB2f85GdyerDpax-eE0yipxKiLmQ50jLwS6fE69sYXQJPIjakY-ohy5DIEBckk_jCCAXhNhbrVU0clXhSsXvfCCTTa1FVI2SysgffLcGI9E7qfEHG2SLNDl7iD0Qoh8jXJEl8MsIaAXGoBpe80ps0uNrkoaJSU1_4NBzJJe8DETQDdkDzlFA9byMcjbpmn2vXmyNFMkqDumaPx1gDsfYhcvNfei_COWfvysTYY3UUsNOPWGbSmO-nyhZ6bTo8xwpBl-Atwh2WrssB1a4Y4DX6Xv2hHWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS9qXMK-3kBbl_md1yAUMvdqZ9Xw4hnna-erDsDXTHW4UcdolznIdJX8F5lxNtGHHa21qwR36pCHxIBG0q5orF_LonuGdMWXSNcWL636jTxAMKLg3_BK8qYUAGd-uzI9CW8HieBq6Gps-4QshEU-qXSNN2tFWypK15BNwTGqAuH7QKENUxgb_LLN-M273nehHv6848MDHQ9Zhby_whJaTAJa4bb3YkMRyCmJ8UJ29GJmq1oz4lufOHbpPgd5nU0GxzKzncSWV7-fS-zhiXfcCCdeSiaozLCtdLHidFD26QV3rViqhgpL4LFzi9eEnC9xGjcnvvQkt5XnOLmdguIHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yrj-BaksP7HAlnt1Gw_6HKysYchIGXPSF2VZCfhdYeLmGBYO15a0ieUl6fDsAkJXkKkXL7KdNKkmYfcrrlnoT2yqDTYQvm-2-978FjxvEClqu5npDwCeHS7Wwug6k4vhVl2jHDafpocjUMrH_o2UIKd6HJiZelE__1OTrhOAIE8Ri96VB9bBHMuxgWenu1iuH-Pp4RU2cRoZz46GjppiZ34r1Adyps5IEQrg_alYfoN2dCSxXr6k3KyBaHUMXFd-su9496m0DgDcTPncSPV2KkhNJysKyFIMM7DMvV-AcUKWatGpz_QVg8jTvub5A__3F1NCuiJlFleaJfhrRJgjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u--32MYhMtm5n8Qq9b9sUf61rTDeKr70yFK5_vMhseaqCXJUCyXd-_XF8CTRJ62xBHeg1Ig05GtZ1lYSIcvx2SyFQcwBh8bZpzo0GCk_8w1bgOmM6r6aDE0EovdyzPW2zsZ0wOURtedsXapHEOIAuD5SRhJcJnMDPBNXr-0ax3LxZakD2oOzyMbPELQP1wEoZ-xHIbv3na09XrVLKtTc-40KBDdrtt7n9ppGReaSvjIOk0Tg2dI1yl4xPNSOL_u96YFpDdUgjuDG3dJZi3gS7gqxlaRaUrgjfzkQErkjG665NHj6LEUD9ONk89J9c4i0P_clckMNl0-m52DIg5Eb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKSPWipy90pZsKa-Ha7kYVOEyJahbc0OQWGbiutWAnCZZYrhJMehagJmAXSA6RXS_lCQH7yI-P4u6mzJEtfAsbat2XGHt4t3Ka77WMrEY7ZJqLvY9pKCTrVvtKcYHf_KxB-PitlA2S5ssc-QzBoitkSwYQ9jP5ssMrDME2pGpmr7BL8PEuxS4DsKwkGoDNgTEPtHFOQBQLL8NRKHduakv5sZnfs9gB0aIJOe38ddH5g8jKDrEmAhnXdcaoaI10mQOyesiS4VnZTmznvCK1vf3XCbU6u5q75qYb2gBc3lx5uaHWp_u9a5Hm5-FXcJTTy3jB_S7v-Ms5rssSxvxxNtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4_Mz132qZ12Tgy46fXEvyggKoYd3mBuMCZ7YNlQ2VXlzeOewj5jep00063dZLY6PKYYTKmD0lPAUSzKG-Is5eFQtMGThB_EiPXAG22b7nx0Yua2_3m8I5N4jrILZNYJDJjAcrw6nK03Y0CwvUIQT9q2Sgg6eXji70gFz2qDusudJcPqNKYRf6qHYxMnV_uYZ51Bix4OK1MUGbvmO0rcScLaTJ7XbnY4qkWA9iHNlg0MlU5Hm4eDwU2MaaICm-73wHv82kkPVl4QKLOwPKtyabUJCIWT1Z9Mvmr7v-zpnddgoTHzCuhJc-eJgqXaERVVagd8ir3Y36LeNlw46rxgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ08rSmzwJM0skIsexKPzQPDd0w_SSL5FbPTcEo37i6WQR-nRyydmwxeGv088MT0EA2djfdzYpYExVvB_j9E6ewPFodCULyvfebFNCX6bzUwo5Z1xVL9A4VbLECD35oA2J8bhCN_UegJkhGwVKyUUtzuzRydD4k8MDKtqMRu2NwtCuzh84DJ_f0rAZt6z3EbytSgXpyJT5HhJHKn40uwrmFewZBWjX9wD3Tyw1bOUlRVg4D7AgoLWoQp1czzGvgvOF-t7Ub_sTh9IKfNcD2fdN82E6Qoug2SEGaayHc4giZ0gqB3zmpxigqdPU6ZgKvOx924ibzAqDvg0X1DVG5LZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4a94nhl4hgvlAekqV5y9XHPlyKE7uaZ1g5Q5lvERstZp20SUHnZF1lyMTmNxFGSYJDecsG-fzfZHgb61JTPeB8hLOKroE6w1aAHtaKGYZaSaRbwYfLyRfAyqC1iWK3nUNOW9W_eC7Uz5TMRZVCL7pxrYekAEM32WtrXXehAJdnJq6gOI5NmJUNT-XfqQCe39cJa3njN9hn1ZgYVWzai2t9S3b6oGxlPZG52Onvt4qDCV5piOvpDz8MEFPXHe2bpZamZreMYKgvTqAywxherySfT_j1ir8OB1mapM2GB6Y81Eu10K_6IvCpcH7U4fTv1WqkxZu1KuklTIcWqGZJZZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش تصویری روز اول حضور کاروان اهالی هنر و رسانه به نیابت از رهبر شهید در اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/676193" target="_blank">📅 23:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJv0vqrMDauRI0iTOb0xIMQvsE8QEIPDKHNQ-8Wcw30b3pvz50YKaYzE5-HBTT0rdE3gd5iqZ1yMQyf1wBWISerVqxTqi_Wzd8u50zwyM1U1WCu0t9AUIbgCynJyChSS3Hwohi9S144aHrvFPaUrHHtQmerq7z5UvEDp1Su61jf34kANHw1jfYfJQlWWQS6pR-tP_bGLhAH_cRsVs_FMNGihLv7uE9Kij_oDu2jgV4X6SRoWg_lEvb1WX46LYMHdyjDWNeSThOWtG_Da82-ajj3FyQkueEXkZtTGVDBKllN3Wsf7KPXgzNN2jpIV7jw5t7Ajuhgmcc5Yro7vfY_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
خدا را چه دیدی! شاید همین برداشتن یک زباله کوچک از زمین ما را بهشتی کند
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/676191" target="_blank">📅 23:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
جزئیات دیدار نتانیاهو و ترامپ/ احتمال حمله به تاسیسات هسته‌ای بالا گرفت؟
👇
khabarfoori.com/fa/tiny/news-3233883
🔹
جزئیات جدید از اعدامی های امروز اصفهان
👇
khabarfoori.com/fa/tiny/news-3233879
🔹
حیله ترامپ بگیرد، ناتو هم به جنگ ایران ورود می‌کند
👇
khabarfoori.com/fa/tiny/news-3233738
🔹
خواننده مشهور دختر 14 ساله را کشت و تکه تکه کرد/ عکس
👇
khabarfoori.com/fa/tiny/news-3233863
🔹
تصویری از دریانورد ایرانی شهید شده در حمله اوکراین در دریای خزر
👇
khabarfoori.com/fa/tiny/news-3233697
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/676189" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-myQ_lBbo7ETsqLCybe5IGPMIN9DryDZNR-0um_NV5DXsy_Pt9ttqd7yyjzCEHxJmbP-7VQRaweNikctCiHcD-QXeiss1Crrd6jhI8OUmoYFnm4F-PlRvsk_lf3HvErN23HsIkpcEoJk-nHUZjqUvyVsq1huccCwGLs2NprOoxMUF2U0Q5NhMIgy4yk0oIGTeUUVlsLmhfuxfJYixCN0EDolgn-5X1H5-QsSVLLLPXZXUReEwzMjkuGdCCsfP25UMd41HX2Kr8r-ynUtrDggHtmD7VsP1JslNfC2IPE5RLqPPekk0hUlKoaoQ50weN6A7Qpdv2dmgZApCKaXaIKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j26fseNpZoQYwV4r0akapk0WcyQW9zqIi5Yb58NQxXobO1z_DlDVHLtN4kJyzUfBO7bUVuGK0kH5GNWSlVYZBGNok5ujX5hk22v68PHrArB2bs_5C_XB6aI8Vo2tpt3nfPBDWysekZiTf1eLduxFziI7bp3oIgAt4T9oU3k5gABDz7G2F0kO2LHhTBoeJwohlaO-IiMJd9Pr5cp3PDxtLVVDpTTxTYaf2EaBBrWwe2os1Yvo-H4TwnGdHBIemSljM3Y0MBSKDOI3Cujhi5hiRQ5MWt2FD-yVMcSETxkuuS8ixHPH14QTLgjyhRoWacHeUIz4rSXz7JLGmtaKP0VZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFxD0VpPm1zFjjD8ZOK8oQ2memVOD4rhNvab_aOPbwgdK_sZgZs1Jf1EBhN7kWD7yIMJlnH2La3CP-bM9-I0qazhEmBXAqeI2elvWM9OBizcyIq2-TF6ikZePFkQiQjArKBZAHzwY4awPfHIfD9yvSWgTYwyp1AYsejPUmM7x__is-1i-pYfdgplnktyWorDrj69wyhhsPnIEoJWvwHM11DYMGxHGVn_bVaIEl2I2KeODyf0CVjaRWr7OrTuKCaFTS01_o7gyN7ky_IkwdPGkEaMbHa4pgc9svXrK_V-8PbdxaNjc4B8vrQ6Tchqm02-fthZkiC1JR4jwZ-ExDbrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtHWv8Gk4Q3Z5CK2uz-S2kH6Pgz0TUQEbrh88oaeE_w9XaR4QrJzh_OV0Q1DBJ9dEXT8rHRoq43v7G-6VY_waJb2oRIM3u0CttQHHNcq9003pHDCggeDPXlnmyskQx8xtJ4Y0LLMdzlfumkw3koLNqu1blSa4sP-0iI82thR3BAs326ySX6EbuqE_DKGlUno8pERl-vPC0ZIVbeG3IKoTvjMZAqqGgDx93XmDOxuzu79ofp3YmL8lj2Yen9QLg2YA17NGVAnfab3K_T8CgQYyqvnw20xp62Cl0cEzuhGCpmi_5sit2xKCss2u0IiEZeLxkyXYzsid-Wk85A3ZPuEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpYHUFHp8_tkGvshEr7cK-VLf7HKgOoqXUi94K8rUFRG-1BN7vCZ2i2JT9gK_hf9mqcGjEY_DmoebzBP1Z5ErULzHpcAHtBKb0ZH9w42QArsoJV2dYVrm3b5RO-26s900KOitOe56YGQFGuhtodHU0CenOpEbr-uJK53kWYG3Q5umrjJdgZL86yj0nl0KVfwus9Ug-caa2Xwj3a97s0HV5VTdzjlPZ6y9qwJdVWlwdc0VNqlTcW7pCvXVo_YmbTbFQCUGZIILE47GLHNsaghB1MUMIUXd3kjPs-FJtadKPLo_741RulaTmvqECy_e-AHjDGsYnotSxaUvIdo9vl6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T73ySCQ5CAYwRq8aKRQHuajIs-pSpboi06RWyCteijp1WUPi9VbIUMvlydEIAdfcWeqDedEx0naZcVMeIS_4oQ7GqAn_bwbO_n4Hms9iHLFrluqKj2glVTFWOjrf4xSrHNlicn74AaOdWO2A1GyZKg7PSd7g_N0UHExZyG51m6WL9_rRDdOejMOcZf68Q_auFyQso1iIx6C9GdLE7w1ZjTqwZ_O2F39Z-geoLp2SHYUsbwADh1J-CaXYG-j0qLhPMfQ-UaWhBfQOz7GPVWO1FAa12iUZJ8VaQk-3FLnmY3TsIffeQvycMz_DRf4M8V_01Lj6WIAl5uSyq-xPmLT0rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ نوع کولفی خوشمزه مناسب تابستان
🍦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/676183" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=mz3tFwAC8xmtUCXbVbH9D1PmsineibONjUCMQz4pcFlMrNVKXcIMAVv_ulCFVLJxd13FKchE_LmrMn_UEmbDcViqKhyfuiTyIG0ipARJlSRk5Y_4b-I-o1wammjWyjF_k7UYFDM_fyB-FaWAENxK8ujbJNTDEOzO-l1nvCtJ97HzmrW2KH7FLpgX7yB1-KOffAxQoYBtTMfwXwaFvsoqStRNv9rphOJ_uCdJjYQ2QZLbN55g4gIJMD9EcuX3GLMCKRIz5Ticvkwpw-0YNfbC2W9dICI5uSe3KlxYElKneoU-mx2Xh2ONVANFBwp8wiQatbyNtekms0SzzsDAi8Ubgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=mz3tFwAC8xmtUCXbVbH9D1PmsineibONjUCMQz4pcFlMrNVKXcIMAVv_ulCFVLJxd13FKchE_LmrMn_UEmbDcViqKhyfuiTyIG0ipARJlSRk5Y_4b-I-o1wammjWyjF_k7UYFDM_fyB-FaWAENxK8ujbJNTDEOzO-l1nvCtJ97HzmrW2KH7FLpgX7yB1-KOffAxQoYBtTMfwXwaFvsoqStRNv9rphOJ_uCdJjYQ2QZLbN55g4gIJMD9EcuX3GLMCKRIz5Ticvkwpw-0YNfbC2W9dICI5uSe3KlxYElKneoU-mx2Xh2ONVANFBwp8wiQatbyNtekms0SzzsDAi8Ubgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرهٔ فرزند شهید سیدحسن نصرالله از اولین دیدار با رهبر شهید انقلاب
🔹
ایران و حزب‌الله برادران واقعی هستند
🔹
آقا گفتند درجات سیدحسن هر روز در بهشت بالاتر میرود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/676180" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef69034a0a.mp4?token=SICLPDbchzbmtyu9C1DLbtjBaTQZgAi1ohgbvi9MdaKm3NACalrBfed8_erd-4dEbnR5zW9vBADyanstyZNiOiJl5PZV8kVfjhk1TO9LvUHPmPxxonbQ1y4U2JIbF5IiGv-2OQDrro9Bi_hPU_5ZJRr2_ZJuPAROL7bSAEOpS-_tpOR4bnJCFexiQqBvSAPBCNEWnMBFfAVhpfIRDDo5tOKrBdGoarR_0l352ae7aZbOVqrvR758Wug73l30UoReFuLwTHqMidqGa6r51NFttb-oZNtzINLc2A5iwKEm2Ne2qY5JaXtE2iRCMuOHglKZXUj2YOkWPpJizVr19WF951D7NeKbHCi7wvvZlK5OKNPnDfdsU19HaM5MPtU1ZbxiSklbEQc5VCL0f_fNiQnuJztyzof-3730fE8QIndFnEdpBF0NA0vPbxAs3JtKCZa4Tz1-UrbrscXwcOfBh2wtPzMavcdPF1ZFyMUSNHn4xA1sDFDVzpqSEX6_J6ooIyB_i04_AyicnCTO-H_kprM03pS02nIJ02ifqm6o7sY6LWzrS22nj5Cn7aUmdVZgOruo4vb5BWHj8w_zYa6PTJV4Vy4nCEKy6_6qZpkLsoIBpPxUbGBUE2Eqts6cZjDGtt2dQB4MseeiYJ3texJU4oM6yVzQmx1unnn3lRvqh6afxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef69034a0a.mp4?token=SICLPDbchzbmtyu9C1DLbtjBaTQZgAi1ohgbvi9MdaKm3NACalrBfed8_erd-4dEbnR5zW9vBADyanstyZNiOiJl5PZV8kVfjhk1TO9LvUHPmPxxonbQ1y4U2JIbF5IiGv-2OQDrro9Bi_hPU_5ZJRr2_ZJuPAROL7bSAEOpS-_tpOR4bnJCFexiQqBvSAPBCNEWnMBFfAVhpfIRDDo5tOKrBdGoarR_0l352ae7aZbOVqrvR758Wug73l30UoReFuLwTHqMidqGa6r51NFttb-oZNtzINLc2A5iwKEm2Ne2qY5JaXtE2iRCMuOHglKZXUj2YOkWPpJizVr19WF951D7NeKbHCi7wvvZlK5OKNPnDfdsU19HaM5MPtU1ZbxiSklbEQc5VCL0f_fNiQnuJztyzof-3730fE8QIndFnEdpBF0NA0vPbxAs3JtKCZa4Tz1-UrbrscXwcOfBh2wtPzMavcdPF1ZFyMUSNHn4xA1sDFDVzpqSEX6_J6ooIyB_i04_AyicnCTO-H_kprM03pS02nIJ02ifqm6o7sY6LWzrS22nj5Cn7aUmdVZgOruo4vb5BWHj8w_zYa6PTJV4Vy4nCEKy6_6qZpkLsoIBpPxUbGBUE2Eqts6cZjDGtt2dQB4MseeiYJ3texJU4oM6yVzQmx1unnn3lRvqh6afxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو رو قطعا بیشتر از یکبار نگاه می‌کنید
🔹
حال و هوای گلزار شهدای میناب پس از دفن قطعات به تازگی شناسایی و دفن شده دانش‌آموزان شهید مدرسه شجره طیبه/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/676179" target="_blank">📅 23:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZeaicmuMNpcQMsg4toHCOVGxkkyvOXCuxnuc1LSH3gwytaRQj1YE_MHcwtltKpEIi0WKLEE_xhEB3HzYERhSIOx22NxYRodj4OyIh3a8CTuA1ra7Zd4Xsm-JzDA36_NOGWvm2kRu9jkOCJUbceJbYFZhBjm5CYVQuFj6SsIz7oCBPyQgbQcv38fAN0K4p30K7NeOzPbRplMZHM2aXwhcDbUvVr8UjrH22oMEUB5sn5DiWaKGS6esw7xzZn1syqbAN0yi42RDRhUCP4ah6wixSIwY7eZH3yWBJQgN0YTW9HxfCF7ayPHzQZpZnvk5vKR24fx6bcWALD6vZmqv-JsKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdbCKuu45EwRF1-NCSRXL-bbz6KjINWrZHZJ06SlM5pf9oOkikVCl4QfocIcNQ4GzblgsjvLJiG3nUDol93cwlfno0argj8FrxkvqJ0-288mFdeWd9YbwFq575R9m7zZ1Tqu0YpoYbfX5lAz27tudM0_OoppTWIrPVu-pTfwGR6UPo5SrMJEhGcCenmLi9o-3FOHSPlIzteHQcuMoKEikVk-9vfH8fO583uZsZ9MtJSK4qmJ3M-mkZMOpZ5MRdShqBJ2IkZ4-h16h7laYFqK_k4f3jN6MUrPcw7UKkGrBT7t8_OJ2IONCuAKFnpfgf3tAFJC4C2AhCHeG3N-cI9luA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMQqoltqTIUlsKkOh9ulp4vGGRRfs0aVSwUg1eucJI2S8VZ9hTy7oq6HaXAEfjvPtai7HkjNKhRMGfW6Ava78MthgLPIrk-I355R2k0SNgHiQWKpPMmOK3eNeiTTIZWPiDzIugXB6GNHFoXDJ1xUYvKIrw2eP8Iqfq6kVr6Je8T6V8MM4_HfBxAxJkkJJqxbqQxcW9CVQDKBgb2v9d-Te-LGpyVRWEdljZAlslqsJ0m2wmSp5cyctMKgxl_KuZDaI5M3lpRis-F2DwzUWJs6rXBHtPMingAeul_Sqjv2wSVhPFc5_2ZAUK_Bwhy6o6MFBZcUKrZvKU5MjtEXtmiBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZADzJ1VF9DFWGy3qZu71niDuiaVxuRdSXUucPzR5XFpV_SXN62y7-RZydre8yqAazt7NPpguge2Qcsyz7W9V9rsO_hb7iFKItfG4lNNS1lONNtSgAHXMNNXWCWL4x0P2M38C288oSF2cdBFk1wgrOL0UFTvtwgLA9uvlNLFw7rFpPJWgEjapdXx1-AKOBjADkTfbjlDhctGJJ-L217jsBMF3_99AOAfH2WXE-RZ5hyoF7T88i2bKASd9kYEUGCdWxXRvVR2SBDhaFNaBV7qx0rr7LrSpkBkFj8YEjlzHVTUfI2RgxbbCXP8VS97b5_L3XzTgrcVay19ohjAtj-DSRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac68f6bd9.mp4?token=SdCVO73_jQkoWwr127t99LTeFHB2Kj-9Tg0DK6EVyT1qRgdiJ48VX2mqglEQsdTAe3VaKvtW8rLDH8pi-699SdMYufMoDkjgSgqJp1fcuG6kuomnsBac4WuiyNZES_puZeTSPEaGrrXnZBx9svXsa7AIxDcYY2WSKp32b_Z2LAGgnjKwIxZ0bbwmjdVZxTx7hiQBMPm2idHlf1Ih9gzGGvQGpobsZ5RhvkxRDHT72ggGbpJPOUQ3Ev_j7k3rdnTi5UYxudqDcNUDXQyDSRaJVB3zJ4BnV1z0Sap5APLEeVPbpgGg-S_Xk9lW86lDmjycLFuJnZ4_Ji_ztbp58c3XxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac68f6bd9.mp4?token=SdCVO73_jQkoWwr127t99LTeFHB2Kj-9Tg0DK6EVyT1qRgdiJ48VX2mqglEQsdTAe3VaKvtW8rLDH8pi-699SdMYufMoDkjgSgqJp1fcuG6kuomnsBac4WuiyNZES_puZeTSPEaGrrXnZBx9svXsa7AIxDcYY2WSKp32b_Z2LAGgnjKwIxZ0bbwmjdVZxTx7hiQBMPm2idHlf1Ih9gzGGvQGpobsZ5RhvkxRDHT72ggGbpJPOUQ3Ev_j7k3rdnTi5UYxudqDcNUDXQyDSRaJVB3zJ4BnV1z0Sap5APLEeVPbpgGg-S_Xk9lW86lDmjycLFuJnZ4_Ji_ztbp58c3XxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه خونین در جاده کاشمر به کوهسرخ
رییس اداره آتش نشانی کاشمر :
🔹
عصر امروز در جاده کاشمر به کوهسرخ، یک مینی‌بوس حامل مسافران به درون دره‌ای عمیق سقوط کرد.
🔹
این حادثه منجر به جان باختن ۶ نفر و مصدومیت ۲۳ تن دیگر شده است.
🔹
مینی‌بوس در کیلومتر ۱۸، با تپه‌ای خاکی برخورد و به درون دره سقوط کرد.
🔹
در این حادثه، تعداد زیادی از سرنشینان مینی‌بوس در داخل خودرو محبوس شدند تمامی سرنشینان این خودرو از زنان شهرستان گناباد بودند که در حال تردد در این مسیر بودند./ صدای خراسان
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/676173" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c462fed8.mp4?token=uprrWAdxLv5ZJESI1h3dYe9boIMN3jggUZSJeTudQGxcDx7_DY8999EKLmIoGo6cUBo_QUJd3WXzlG6gYF0aN1JNcfQHb4BkWxm6fIH7b1q1HMDJZl0QKCpcxBMYlV9qnntBp50h0tWtvgeL2Kf8nXGd7V6TxVhQVxiPXDVskmyq1hQm3xo3DldYMaypEx33xzFIKJrdsKMM49QREJ_UeWemgkPMPlfGEuEJaZ-ZQPI9imbVi_vzGYkLHI1p5RvO3O0MsXwBAvcfHoEqbtsDf5EhD0Nc6YKi-u1X-kozEjqAVorAoPm43K-7qGafJHXmKs-_z3JuIkVaEUEWsNOqrYDBTEMbZl75MHgdAntMvXQDsK7eAduVzT33M_Mc76xxtXfgsFLi1znNV6RnM7AG1j5nsgbxQMm0wl38CHcuSG-TQcvQS3gS_BGa6Q0FylcoyqHt7eRiWlPyF-6-GCNO54iBQqazK4-cInvD0ITvCBwizEv9lfH7Lx5QfZVEPTomIKrYVUzydKa2aOqt8Vm48SkVmmQbyL66dE33Fj777TcTxzplUUqOns3iWr9LVdhFePW-w2EJn6xLekKWiPFpum1YKelnbnWAz1Mdi6nKCEvCNbpR6wHMc0vRJZa7VPOO43tNcCeDGfLJWv1eqLgWxxAg70PQ4XsbKoLwKeHFfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c462fed8.mp4?token=uprrWAdxLv5ZJESI1h3dYe9boIMN3jggUZSJeTudQGxcDx7_DY8999EKLmIoGo6cUBo_QUJd3WXzlG6gYF0aN1JNcfQHb4BkWxm6fIH7b1q1HMDJZl0QKCpcxBMYlV9qnntBp50h0tWtvgeL2Kf8nXGd7V6TxVhQVxiPXDVskmyq1hQm3xo3DldYMaypEx33xzFIKJrdsKMM49QREJ_UeWemgkPMPlfGEuEJaZ-ZQPI9imbVi_vzGYkLHI1p5RvO3O0MsXwBAvcfHoEqbtsDf5EhD0Nc6YKi-u1X-kozEjqAVorAoPm43K-7qGafJHXmKs-_z3JuIkVaEUEWsNOqrYDBTEMbZl75MHgdAntMvXQDsK7eAduVzT33M_Mc76xxtXfgsFLi1znNV6RnM7AG1j5nsgbxQMm0wl38CHcuSG-TQcvQS3gS_BGa6Q0FylcoyqHt7eRiWlPyF-6-GCNO54iBQqazK4-cInvD0ITvCBwizEv9lfH7Lx5QfZVEPTomIKrYVUzydKa2aOqt8Vm48SkVmmQbyL66dE33Fj777TcTxzplUUqOns3iWr9LVdhFePW-w2EJn6xLekKWiPFpum1YKelnbnWAz1Mdi6nKCEvCNbpR6wHMc0vRJZa7VPOO43tNcCeDGfLJWv1eqLgWxxAg70PQ4XsbKoLwKeHFfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری کوتاه بر آنچه در مجمع پتروشیمی امیرکبیر رخ داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/676169" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-NNOrOi81rEely7g2VAWbsBc3U0qt2GHjnpczJMbnGs3pCCimIAKMeWxQsMIcnb2gUZC_VuX5Iaf17ZvMXvlDkjszKXimniOLstlMlCCdjMlxQZVkbi8lm5FwV3V_U7xLn931h3Eh5O-b1KVKSnCtwTjeKvZKPz2r3PxQgTlAoJTxUl398Tev9WBZJqeBfGKUjlcCS0EBfHWH8sW29W5LexGZ7DfJ--M_qGjZ9nQmO-S4uRRW4AJQyrF72xZAc5W4sV7Z8gEXemwe7p1Fq_mCTS3eOC4LQ8eoNUJVthhHTotC4CzE4Vbj7L_h-AKnUDNh6xO284WF9nsgLMZ9uK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در عربستان پول پارو کرد!
🔹
کریستیانو رونالدو در کمتر از ۴ سال در النصر ۶۲۵ میلیون یورو درآمد داشته که بالاترین قرارداد تاریخ فوتبال است.
🔹
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🔹
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🔹
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🔹
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🔹
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/676163" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMLfgo_YYEWaJvzo1y4LdVHfsVp3vA9Jy-t5qLi87sliFj9rAjETV1l_1lRPJyQup22aNjwuchM4W-d0yTnwrEmE2WV31l2NQLsqJCXQH6rC7L81E2sd7ZRPdpXAhY2mLc_sy2RoSJ2f8pZwYqcuVkGyOJESyAgjFtcBM_qktEPELsowwcvFVEhhjv3AaENtY3x0csLFT9D0dW4heOTEF_MdVNqKQUi-6wBzZVC8-gyQNt7VwwU2l--wwfYd-b76l3zEezQTH70HQaq20o8vB7rKo40oK18nDwlyxA3J1U-lRK1FzN0nMVJyhFASZyd9NC4rj-I9qwFZmBN-uoyjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار محرمانه پنتاگون؛ آمریکا روز بعد از شهادت لاریجانی ۷۰ زخمی داد
وب‌سایت آمریکایی Raw Story:
🔹
دا‌ده‌های پنهان پنتاگون از تلفات و زخمی‌شدن ۷۰ سرباز آمریکایی در یک روز از جنگ ترامپ با ایران خبر می‌دهد.
🔹
گروه «وار هورس» این سوابق را از طریق درخواست قانون آزادی اطلاعات مبنی بر درخواست اسناد دولتی  که شش هفته اول جنگ، از ۲۸ فوریه تا ۸ آوریل را پوشش می‌دهد  به دست آورد.
🔹
بزرگترین روز تلفات در این داده‌ها، در ۱۸ مارس، تقریباً ۲۴ ساعت پس از حمله هوایی آمریکا و اسرائیل که منجر به ترور علی لاریجانی شد رخ داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/676162" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def029722a.mp4?token=YYomkrAZ09WODRlP59eGVPmTZYRwgS70IRG8r4OAuDUmpRjymDmKBBvpaU5DawBcB844DphjkPtYLNe_FxFnIk_4GBSDRJTlhQ5DzPoEn80BKA7nB6PsultULuG8Hn576omfxDqS75eTh1-QDRTrKL_C4kio1OByFNVPk7ZX9kCYOVgsaStejAnN5QodEkhvlxyfrkEa64Iq4gt3crAoOIQWsfeBes9qG9o8gTmeOINvUfS2E2yvIR7o524y0YLbfXR881zbdFuTuXcx7qyrizxNNVmbAPTrbaKA-O1Ai940AEsYdZqEYCEFCsU42X6FmuLKo1LT4XDXcQap7PwLfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def029722a.mp4?token=YYomkrAZ09WODRlP59eGVPmTZYRwgS70IRG8r4OAuDUmpRjymDmKBBvpaU5DawBcB844DphjkPtYLNe_FxFnIk_4GBSDRJTlhQ5DzPoEn80BKA7nB6PsultULuG8Hn576omfxDqS75eTh1-QDRTrKL_C4kio1OByFNVPk7ZX9kCYOVgsaStejAnN5QodEkhvlxyfrkEa64Iq4gt3crAoOIQWsfeBes9qG9o8gTmeOINvUfS2E2yvIR7o524y0YLbfXR881zbdFuTuXcx7qyrizxNNVmbAPTrbaKA-O1Ai940AEsYdZqEYCEFCsU42X6FmuLKo1LT4XDXcQap7PwLfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران است؛ سرزمین مردمی که می‌ایستند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/676160" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e595e00fab.mp4?token=X8FX8RnS5jB8C6p3jkrnpqCpB1-GqR9B_suQ5tsySgHVSmQ8t_B1li3brAZXJ18PaWUokGB9N9uZZ05tnONK_Z-raiTpdYoQ8BtuBAzsFB-3uICthn3UrDi8Qoxjbh9HmKJ8xkuQL8fezRiLBMbHBfMnqme73o0UFmHsvdPAxTdoY7bslyeMbzvgvJFT030OAux4yVjd_GSEYHsi4HdaStvLAFKjWIJHSvt-UTmB4JbB6HakWhP1cyWsfn7CMsSBZbZdSeGkMgzVY2NMCq8eVBRgoJ8BHYTS4C3H-goUWuLmC_aYb-d3-G2bNYKItmyu-8o8SMc7vf2McMXok9eEySvSmptNZj8yChCjySn1MfqpV38roJIFZpJIHb7Dmgwtbfgd3d1SVpjRipvUkdxEqJYVNTg5O_OxyxcFg8ks3MX5CQWcYIu36-gcIKTZ5keMNQyILrqVk8gCb8MwQTDAUEvyeMFi7JMaSoxwdhkNKOAas6o9MR9YYqh_d3s7paoZjnj3mdZJcNu1tFQDc3LVObtWFkRueG0kNsSn8Ey6wQQ-Y8NqaX_ZR2CAHONnA6nQCCNrLEsu-Ve9nKiMFk8Eb-7nQk_7WMjmJlWNYHFglgUyssFSlbXQ-9SdsqHNjVcB4turMWctIBxAfmadhyDWVQw6Gv_wbaaa-WeY1ZFP5lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e595e00fab.mp4?token=X8FX8RnS5jB8C6p3jkrnpqCpB1-GqR9B_suQ5tsySgHVSmQ8t_B1li3brAZXJ18PaWUokGB9N9uZZ05tnONK_Z-raiTpdYoQ8BtuBAzsFB-3uICthn3UrDi8Qoxjbh9HmKJ8xkuQL8fezRiLBMbHBfMnqme73o0UFmHsvdPAxTdoY7bslyeMbzvgvJFT030OAux4yVjd_GSEYHsi4HdaStvLAFKjWIJHSvt-UTmB4JbB6HakWhP1cyWsfn7CMsSBZbZdSeGkMgzVY2NMCq8eVBRgoJ8BHYTS4C3H-goUWuLmC_aYb-d3-G2bNYKItmyu-8o8SMc7vf2McMXok9eEySvSmptNZj8yChCjySn1MfqpV38roJIFZpJIHb7Dmgwtbfgd3d1SVpjRipvUkdxEqJYVNTg5O_OxyxcFg8ks3MX5CQWcYIu36-gcIKTZ5keMNQyILrqVk8gCb8MwQTDAUEvyeMFi7JMaSoxwdhkNKOAas6o9MR9YYqh_d3s7paoZjnj3mdZJcNu1tFQDc3LVObtWFkRueG0kNsSn8Ey6wQQ-Y8NqaX_ZR2CAHONnA6nQCCNrLEsu-Ve9nKiMFk8Eb-7nQk_7WMjmJlWNYHFglgUyssFSlbXQ-9SdsqHNjVcB4turMWctIBxAfmadhyDWVQw6Gv_wbaaa-WeY1ZFP5lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت از آب شیرین‌کن جاسک بعد از حمله ناجوانمردانه آمریکای جنایتکار
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/676159" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676158">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg_b9OEhf1VIxyKsPcRPKn9l5jap3JTbI2dDMeJmB1Nlr4_-BKFrk7oilo9eTYFDyQpHPo8OXaI40JlVR4eNg4PEHIXHHcbD0pUT51SCsxN96db1qpn0aD6hO-j0P4ONmC1XOQdfQjpbwCqZtLg-Y1Xz36BTdjCR9WLK--agwPb09m1yq7b1TIzW4aPBgkQ4yYR4LyT8VqrWcYPcgUCMZ6527EY9tU-rmyZzfs0q7H5d7pVFoUgwnUGKlJninIa8Vzt7INDczxjqDOCDu1HWpEOgVaO0upJsc-QlxeBobljl8rQJs1PCil-ruv4QugY3ZsHSnhpTuB3R-LlpGICL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اوکراین اطمینان داد حمله به کشتی ایرانی غیرعمدی بوده است
🔹
سید عباس عراقچی با اشاره به گفت‌وگو با همتای اوکراینی خود اعلام کرد کی‌یف تأکید کرده که حمله به کشتی ایرانی غیرعمدی بوده و به‌دنبال تنش نیست.
🔹
وزیر خارجه ایران افزود تهران نیز به‌دنبال تشدید تنش نیست، اما بر غیرقابل‌قبول بودن حمله به منافع ایران و لزوم جبران خسارت‌ها تأکید کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/676158" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آقای من (:</div>
  <div class="tg-doc-extra">حسین‌طاهری.. قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/676154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
بسته‌ی
#مداحی
#هیئت_قرار
ویژه
#اربعین
شماره ۲
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/676154" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc360cad4.mp4?token=MOJGabTqb_XPuCuXMsuJK-0GpCGsM6KtAl92SfI8SacqalTAAfRgrbRW31H0EnfdlkAAZZzYTuX3-JAGu0s3wvkH312NCDP-2ZPwxUSvszPPC0Y350okq_c78cuATbH-syQXE0WQxpje_4mFk9n0ioup_e2GgHJRoJKlf3MQHhqAIDoGaL0SSbe-5rcvZbwUeLPH7WKqlaWXFIzCprdsBspnMA4DX-Rpd-CcrmNo6PAwlUC6KqdtK_J4TeFuWUoe66Jb-L4t2s8iAi1etXAic_fAzGxk5SHM4hNqTY4oNMrd8Gl0J3MxoTeZhgEvn2_HQGM6YPatAl3Tpw2pZkmAYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc360cad4.mp4?token=MOJGabTqb_XPuCuXMsuJK-0GpCGsM6KtAl92SfI8SacqalTAAfRgrbRW31H0EnfdlkAAZZzYTuX3-JAGu0s3wvkH312NCDP-2ZPwxUSvszPPC0Y350okq_c78cuATbH-syQXE0WQxpje_4mFk9n0ioup_e2GgHJRoJKlf3MQHhqAIDoGaL0SSbe-5rcvZbwUeLPH7WKqlaWXFIzCprdsBspnMA4DX-Rpd-CcrmNo6PAwlUC6KqdtK_J4TeFuWUoe66Jb-L4t2s8iAi1etXAic_fAzGxk5SHM4hNqTY4oNMrd8Gl0J3MxoTeZhgEvn2_HQGM6YPatAl3Tpw2pZkmAYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی بود؛ هنوز هم هست
🔹
در مراسم رونمایی از طرح مهرورزی هنوز هم یاد عزیز از دست رفته برای خانواده‌های جان‌بخش زنده بود و در هر گوشه‌ای از مراسم برخی اعضای خانواده جان‌بخش قاب عکس را در آغوش گرفته و امیدوار بودند با اهدای عضو مادران و پدران دیگری شاد شده باشند؛ با این شعار که یکی بود و هنوز هم هست./اخبار تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/676152" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPAOJz423tvsmV4jI57HFSXybncsTMTxjf2kwdlnJt77-AWpX_gj18-_OFs2am9bvqmS9QtXRJT-WMWiGJpemGVSEslOwvXnEa_mBsUy5fMDvdIxBl7ogfizxU9CN5kPDCXK7H9-kCW5TOHpzRrBC-j14vIbBVc_One_6SC6E0m7Dsd9ds0_agpI3mT3hnB7LMJRi7I57bF4GSF82wP_PBTC8xlfO0zR96gw1BZSwk_yr39FQzHlM36dEI0Q6SsZD3suecDaBqAX3x8FrWkB97x0A7Zqr0M0LlWnXeCGAXkcUndgNENFTqUnY6f38ZF-STx6GO61WHMTDuPImvjHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد زلنسکی برای ترامپ: اوکراین، اسرائیل اروپا شود
پایگاه خبری Responsible Statecraft:
🔹
اوکراین از آن نوع شرکایی است که وقتی دیگران اقدامی نمی‌کنند، دست به اقدام می‌زند. هدف زلنسکی متقاعد کردن ترامپ برای پذیرفتن اوکراین به عنوان شریکی از نوع اسرائیل برای آمریکا در اروپای شرقی است.
🔹
جایی که می‌تواند در مقابله با تجاوز روسیه، مهار توسعه‌طلبی روسیه و محافظت از اروپا و ناتو مفید باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/676150" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMTXAGevufCad6iX-VN1WrV_ffNos31HaZaFovMylxeKRoy2xlu33loI42SJjWGI_Zppk11d7dIzO1VCiE0hRz1KtVbcuCfCTZR65t7mvHrIGgFKjd2RgUaVFJ25e7SnjVOOcogF43jqo-D1DimlH2u-_PFxc5odjflPQsLaiG3QQkBv8hceXC_CUbnPf0D9rqicQoj91hQZCap0sU-usVIzbthHDtyrrCYrSOeqvpc1cVNSEpiKer_DOlbHjyQz01bibL21JaR9R4OTNTIXv9owTqkILIkC4xxCgXBLekrKyqHljYgYQfvbAl0Irp5H8WGVMk0V-30L-kpMmsMQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌹
یک قدم تا زیارت کربلا…
با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و فرصت خود را برای برنده شدن یکی از ۱۰۰۱ سفر زیارتی کربلا امتحان کنید.
✨
این سفر معنوی به همت هیئت قرار برگزار می‌شود؛ شاید نام شما یکی از زائران این کاروان نور باشد…
📲
همین حالا عدد ۲ را ارسال کنید و در این پویش حسینی همراه شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/676149" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اطمینان‌خاطر به مردم؛ تا آخر سال تمام انبارها پر است
پیمان فلسفی، عضو کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از جنگ دوازده روزه ما کمبودهایی در حوزه نهاده‌ها داشتیم؛ با تاکیدات رهبر شهید و مدیریت دولت، چند برابر نیاز کشور دپو انجام دادیم و تا پایان سال ۱۴۰۵ هیچ کمبودی نداریم.
🔹
طبق پیگیری‌های مجلس، وزارت راه و خانم وزیر قول داده‌اند اقدامات لازم را برای حمایت از ناوگان جاده‌ای انجام دهند تا جهش قیمتی رخ ندهد. همچنین وزارت راه و شهرسازی متعهد شده است تا کیفیت جاده‌های مواصلاتی و ناوگان ریلی را بهتر کنند تا جوابگوی بسته شدن بنادر باشند.
🔹
در خصوص خرید تضمینی محصولات استراتژیک مانند گندم، دولت همیشه چه امسال و چه سال‌های قبل با تاخیر پرداخت‌ها را انجام می‌داد. پرداخت‌های این بخش معمولا از درآمدهای نفتی تامین می‌شد که با توجه به شرایط فعلی ما از دولت مطالبه کردیم تا راه‌های تامین مالی جایگزین را پیدا کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/676147" target="_blank">📅 21:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f8d58e31.mp4?token=ZJJ874nPBFZYY5GTsgz9wS73br-VsIXqN5igFIyPP_lKpLajyCA0oG_KzlAaFpiSGpkJooTmCgzfH1paIjnXACmfYvn0M1m2uDSD2gLQg41xleLpC7sP8JuCy8xcQq07cXlYBPw9mKzyIFbE0TRKNHcp7IvaXkfqSYp8a9Wwqt1LjjkQ8e9fEE78LCVjtSfzVWAXAyRfthQlARvUTVHG6ms6M7ynWw3eZS2rcV4JlXLUpt5FtA1WgwUD_6-ERqEl3iDEAVNN1QDyMPCgtQIs8siw5EdlnTkQQCM1fFyoTHL0XwoGAi48gze2r7pEKjk_fnrSj_ocLDHE8B2SDpYEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f8d58e31.mp4?token=ZJJ874nPBFZYY5GTsgz9wS73br-VsIXqN5igFIyPP_lKpLajyCA0oG_KzlAaFpiSGpkJooTmCgzfH1paIjnXACmfYvn0M1m2uDSD2gLQg41xleLpC7sP8JuCy8xcQq07cXlYBPw9mKzyIFbE0TRKNHcp7IvaXkfqSYp8a9Wwqt1LjjkQ8e9fEE78LCVjtSfzVWAXAyRfthQlARvUTVHG6ms6M7ynWw3eZS2rcV4JlXLUpt5FtA1WgwUD_6-ERqEl3iDEAVNN1QDyMPCgtQIs8siw5EdlnTkQQCM1fFyoTHL0XwoGAi48gze2r7pEKjk_fnrSj_ocLDHE8B2SDpYEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: طرف مقابل فکرنکند که ایران مادام‌العمر عضو NPT خواهد ماند؛ همۀ گزینه‌ها روی میز است
🔹
ما با بحث دربارۀ خروج از NPT مخالفتی نداریم. جنگ و زدن تاسیسات هسته‌ای کشور فرصت مناسبی برای بررسی موضوع داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/676145" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
غریب‌آبادی: طرف مقابل فکرنکند که ایران مادام‌العمر عضو NPT خواهد ماند؛ همۀ گزینه‌ها روی میز است
🔹
ما با بحث دربارۀ خروج از NPT مخالفتی نداریم. جنگ و زدن تاسیسات هسته‌ای کشور فرصت مناسبی برای بررسی موضوع داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/676144" target="_blank">📅 21:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش و ترامپ قمارباز در کاخ سفید دیدار کردند  نتانیاهو کودک‌کش پس از دیدار با ترامپ:
🔹
درباره جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگوی خوبی داشته و بر هماهنگی کامل دو طرف تأکید کرد. #Demon #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/676143" target="_blank">📅 21:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8946dc2c80.mp4?token=G_v3i8YH_vCtxBvbhuPU81KAlzYPjdsKUAfhJw-tf61djIk1PkaqElght4iHQ_TL8H8-668_IOrnMnKlonzhlB_LF-Yc2l6UJ7vREkKZn6wdhFEKTWBTzmotxHoKE1m-6dnNvrsn-XTSMCvVqXK3hperMgpQ7b-niVcXsatfaUf2gqPilP6SFgMGz4FBCDpzGu7GXzShEOnhjlfrsrgOWTtyN4ZQGV8K9LKuydVHUBvHyw7Z9dkw3vPyv3yMiwseJ0hhZ9Oe1uYdvCvFazVxCCW-K2QJrD5J7pr4YcPBK1hjNQdQd5Ap7q7QLcA9sOfuVc5iclI2MpBI8H3jnl3zUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8946dc2c80.mp4?token=G_v3i8YH_vCtxBvbhuPU81KAlzYPjdsKUAfhJw-tf61djIk1PkaqElght4iHQ_TL8H8-668_IOrnMnKlonzhlB_LF-Yc2l6UJ7vREkKZn6wdhFEKTWBTzmotxHoKE1m-6dnNvrsn-XTSMCvVqXK3hperMgpQ7b-niVcXsatfaUf2gqPilP6SFgMGz4FBCDpzGu7GXzShEOnhjlfrsrgOWTtyN4ZQGV8K9LKuydVHUBvHyw7Z9dkw3vPyv3yMiwseJ0hhZ9Oe1uYdvCvFazVxCCW-K2QJrD5J7pr4YcPBK1hjNQdQd5Ap7q7QLcA9sOfuVc5iclI2MpBI8H3jnl3zUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمک‌های ترامپ به مردم جاسک/ در پی حمله آمریکا به بندر جاسک، بیش از ۳۰ لنج صیادی مردم جاسک در آتش تجاوز آمریکا از بین رفته است و همین موضوع باعث نابودی معیشت ده‌ها خانواده شده است
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/676142" target="_blank">📅 21:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پشت‌پرده رسوب خودروهای وارداتی در گمرک/ پای شرکت‌های تراستی در میان است؟/ کنایه دادفر به روندهای دست و پاگیری اداری
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری:
🔹
از زمان ثبت سفارش تا ورود خودرو به کشور، به طور متوسط حدود ۶ ماه زمان لازم است. خودروهای بسیاری وارد کشور شده‌اند که به دلیل صادر نشدن کد ساتا، همچنان امکان ترخیص و شماره‌گذاری ندارند.
🔹
بسیاری از این خودروها با منابع ارزی خود و دیگران تأمین شده‌اند، اما همچنان با بهانه محدودیت‌های ارزی و موانع اداری روبه‌رو هستند. این روند زمینه‌ساز رانت و فساد شده و شرکت‌های تراستی نیز در این میان نقش دارند.
🔹
در دوره جنگ، روند خروج کالا از گمرکات روان‌تر شد؛ موضوعی که نشان می‌دهد تسهیل فرآیندها امکان‌پذیر است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/676139" target="_blank">📅 21:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd11c18a66.mp4?token=Nqbte164H0a_nAF-XHmbwjcc88lRxP1qKOvJvp3FW8mxiLRe57evcTAkKOwP8184UuVn2M-pHM_fj2HG0iHceuGHNRDnOCdndFy04dJXIM-HihoHmoXt3n9c_-WnXEogapZo08SP6A4nFXz6AtgQBl6JcB5LM0QP2arE7qXeim2-EvAXn0ouSaqs53gK0l4C32yy1yGbZT2WzIDRTSXoZpIQ7TsCoZX0Rt8_8axwHXCoLEcOz25IYW2hywsY_5JSPkMBUk5yr4hx6656fkEy60hxSvriHZ6yPZ7vdoAloGMjkJKE9GuyPVundJk8miaGUkk-HTYxEpgfWQVc8_822w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd11c18a66.mp4?token=Nqbte164H0a_nAF-XHmbwjcc88lRxP1qKOvJvp3FW8mxiLRe57evcTAkKOwP8184UuVn2M-pHM_fj2HG0iHceuGHNRDnOCdndFy04dJXIM-HihoHmoXt3n9c_-WnXEogapZo08SP6A4nFXz6AtgQBl6JcB5LM0QP2arE7qXeim2-EvAXn0ouSaqs53gK0l4C32yy1yGbZT2WzIDRTSXoZpIQ7TsCoZX0Rt8_8axwHXCoLEcOz25IYW2hywsY_5JSPkMBUk5yr4hx6656fkEy60hxSvriHZ6yPZ7vdoAloGMjkJKE9GuyPVundJk8miaGUkk-HTYxEpgfWQVc8_822w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواص آبمیوه های مختلف از زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/676133" target="_blank">📅 21:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgxV-eomqDNTJggvnJUMDwqb6sCbqjPjVKtvDybevviTEE4vfVEMuQX-hgrx7YawDKl9k1q-hhSqrBGD-weV-jtQi5ZtJSq8n5dOiMLY7VWJx4Yo_p5VjoNmUJj9lyi5U__N3K1KAiOY-uNKiA1EpT8eo-RFTZUjyH_i_pTT52CT4Ikg-1NuENlC6nqMoPuD4rS6E5j-_xeUYkG_trw9tfzNeaDR64T3aiIaSzKjjfFCaTtZpIFolrvNiVQS4IZioXZ1zPY9bfDbJqL4XwK2cjor1Zkm7_OHbQBNXvRzVheZ4tnecYbrAp4sTuMyq7SRTSrFB4VEHjqTD6dqdjVY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاروان اهالی هنر و رسانه به کربلا رسید؛ زیارت به نیایت از رهبر شهید
🔹
کاروان اهالی هنر و رسانه به میزبانی ستاد اربعین شهرداری تهران روز گذشته دوشنبه ۵ مرداد ابتدا عازم نجف و سپس کربلا شد.
🔹
هنرمندان، سینماگران، کارگردانان و مجریان تلویزیونی در این سفر همراه شدند که از جمله آنها می توان به مهدی فرجی، منوچهر محمدی، دانش اقباشاوی، سیدعلی احمدی، محمود کریمی، محمدرضا شفیعی، سعید پروینی، جواد شمقدری، حسین شمقدری، وحید رونقی، احسان مهدی، حامد مدرس، علی صدری نیا، حبیب والی نژاد، محسن اسلام زاده، بشیر حسینی، هادی نائیجی، فاطمه افشاریان، محیا اسناوندی، راحله امینیان، فضه سادات حسینی، شهره پیرانی، محمدرضا باقری و همچنین چهره هایی چون حجت الاسلام شهاب مرادی اشاره کرد.
🔹
این سفر که به دعوت ستاد اربعین شهرداری تهران انجام شده، قرار است نوعی قدردانی از مردم عراق بابت اقدامات میزبانی همه ساله اربعین و برگزاری آئین تشییع باشکوه رهبر شهید و جنگ رمضان باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/676132" target="_blank">📅 21:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676130">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ6UaHZV3ZtMEqKlQVNXYPP-gqSRgQkIuwaqOyEEEP1vjvL-93pFgrJlGy3xB-WfY7SxLpycrvqngKOYW9H6CW-4IRcMMI5tkGzyw15KMFHCdlr-QCkJFMc2ZIKkjlUSbJfic6k2n_oj70TlHrkj3sBgDtly_Ad_8Ac6c8Mm_DQLCfScBu_CKmtdFsngczMNhJN8Ufne7ILIFQ3x4yGwjFWLxTZwEFAR_GNFchq0vYiOxZSs68P4Y3-GYgm1XqUgVvRJDmk59eabzEzJHJHBa9gzg8oR06pbHdScDncqLkgyRIVtYFLqD8bEE0Tmtfd4sAG5_nxiJM0ldhyNZi-YqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، هر جا باشی بیمه‌ای!
فرقی نمی‌کنه
کجای شهری
؛ پشت میز کاری، توی خونه‌ای یا حتی در حال سفری.
✅
با
بیمه‌بازار
برای خرید بیمه
لازم نیست جایی بری
...
کافیه وارد
سایت بشی
، بیمه‌ها رو
مقایسه کنی
و فقط در
چند دقیقه
بیمه‌ات رو بخری.
👈
برای مقایسه بیمه ها وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/676130" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676129">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
کی‌یف به تهران: قصدی برای تنش‌افزایی نداریم
وزیر خارجه اوکراین در گفتگوی تلفنی با عراقچی:
🔹
هدف این کشور تنها دفاع در برابر روسیه است و کی‌یف هیچ‌گونه قصدی برای هدف قرار دادن کشتی‌های غیرنظامی یا تنش‌افزایی با ایران ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/676129" target="_blank">📅 20:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DttBGIiEQ1Ep1RfQ4mVCw5K6HRsLM2KXOosvGa1RnK2sUL_UoBo_YPd_vW9j8cuJd9nAZW3QUBukqGkmJraFjvE8SIapU9icxS6sZPgG8IRApkmggwR4r642kmjhWgTj1ouHj1QDnD8H3r4kV6jcFPT4QmQJFL_P5eXMOQBNOanXhilJbbJFi7Av-qWGM4TTf8EmJMalosIsYRp4oijNFAGBcWkd0yqfPFjrQYnWua0P496TL9RuEbbLFgr-jJMoi6tHRcB8gFMWJAxIN5Nl81thy3hjanhGOscypaYHVFMo85zb5jY8hQgnwcm6DX_jmf_y_Dr8h1r8Dxa6p1uqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1KV-qCC2Eizal5dAEOYfCslB6c-Mved_vyN9ChwujTYM3qrMqZI64nxpJ-595NCOSR_6ZYpeSROkHlBYqJyRuM5MWT3hWi4QpdqsjB6y4R2h6c1PuxZ_n-yj2VByi21MIG-GDAqKjc2WC32nCKvx_o7SFgVXXWn-tLhiGYw1xY5RIqRpKdL05RSJQkFS6cPTbmhdFYOoBqp0mQryc8uPc1NWaJtpgXn8Rmk2mUhCkaVL5XUl5-8Oy66F7Nd597KbVlp1DAGQYeBZpUPWVE5oaZ5dMsTy-1lH2kP8--9OWI89GpovliCBDp3SlxvSuNVFMTF793NUO_yGEDZptIWGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از هر چهار جوان ایرانی، یک نفر نه شاغل است و نه در حال آموزش
🔸
بر اساس آخرین آمار، بیش‌از ۲۴ درصد از جوانان ۱۵ تا ۲۴ ساله ایران در گروه NEET قرار دارند؛ یعنی نه شاغل هستند، نه تحصیل می‌کنند و نه در دوره‌های آموزشی حضور دارند.
🔸
این نرخ از میانگین جهانی ۲۰ درصد بالاتر است، اما نسبت به کشورهایی مانند هند، عمان، اردن، عراق، تاجیکستان و افغانستان پایین‌تر است.
🔸
کمترین نرخ جوانان NEET نیز به ژاپن، سنگاپور، روسیه، سوئیس و امارات تعلق دارد؛ کشورهایی که بخش بزرگی از جوانان آن‌ها یا در حال تحصیل‌اند یا وارد بازار کار شده‌اند.
📊
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676127" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
غریب‌آبادی: مسیر موقت تنگه هرمز باید تحت کنترل ایران باشد
🔹
ایران با پیشنهاد مسیر مشترک ۵۰-۵۰ با عمان موافق نیست و تأکید کرد مسیر ورود باید کامل در اختیار ایران باشد و بخشی از مسیر خروج هم به ایران واگذار شود.
🔹
اگر با عمان به تفاهم نرسیم، مسیرمان در مورد تنگه را ادامه می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/676126" target="_blank">📅 20:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از برزخ؛ از آب روان تا عذاب مال حرام
🔹
00:10:00 احساس حضور حضرت ابالفضل با نوشیدن آب از دست بانو
🔹
00:19:40 بسته بودن دست‌های کسی که او را نبخشیده بودم
🔹
00:33:00 طلب مرگ حتمی از خداوند به خاطر گریه و ناراحتی عزیزانم
🔹
00:45:30 رؤیت عذاب انسانی با چهره قورباغه و داشتن ظرفی پر از لجن
🔹
00:48:35 قطع شدن زبان شخص نمازگزار و متدین
🔹
00:53:00 در اتاقی پر از گل‌های زیبا، لباسی از طلا برای من دوخته می‌شد
🔹
01:00:45  بازگشت به جسم با روسری که توسط بانویی بر سر من گذاشته شد
🔹
قسمت سیزدهم (حق)، فصل پنجم
🔹
#تجربه‌گر
: نرجس اربابی
🔹
قسمت قبلی
🔹
قسمت بعدی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/676122" target="_blank">📅 20:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676118">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxCOBL83jmEJPpMS-wwar6P7X7F6ZYZslTfmXFaimyBughax2BIsCRNTkQBe8Mz5GMZMpLzy4J4hNSGY9yE_TYAPaHTbfxPAm8ZJxBnQQjF3rE-Kv-hrO3zRx2P2KaQ1JcHa-8VWXZV0bWI9J0gMDYpp8ZENRagSwsts44LcoLneVpG1Vmq_stZbXQQwhWdHFWFjHyktR8ZpCYAGMR8h8bK86bFby9Jc0zoekdqsQRjgTS9O7cqinLz6dKDVNvdXEabZ8S4-I1FwCmarS9Yxq1_py7W_zX1jdaffJCCyrXDIXCD5xVXgGjqv7mhtwy6aBu6xhO8Xzji0MzAkKWLJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/676118" target="_blank">📅 20:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676115">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifebb-k4WOuYe3Z-W2W8zhJEGnytl5X7SO6vO5K4U42QMkOJQGLHAXsFIyoXiRc-GQdSI0SwMaGuK_3NbFmNXx7HCKLV0OZ_7f7xYOu8FKWZnmelyll3oCnP0rGeXHizkGlfdu0wn0HAYlXLWNT4Sae6BPUYKWTjDd9TRv7ScfzyuwlUEP7WTk2Qq3Jq0QonFWjlPOBL4Vp1cB3kVG_SYqor0jUh9VVfvyaRtCKkLqfFtUCudTHdlxdzKgchWri8uEhctgnAzrxsY8R8exqA7ejE8mxpvDvdANX13sUFYtdrfDDD_UySBMZm2hoNtp8ZoD_JvYfGxE2DvqHH7qhmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مثلث شوم
🔹
هم‌زمانی سفر نتانیاهو و زلنسکی به واشنگتن، آن هم پس از تنش‌های اخیر، گمانه‌زنی‌ها درباره شکل‌گیری هماهنگی‌های جدید علیه ایران را افزایش داده است. برخی ناظران معتقدند این تحرکات دیپلماتیک، به‌ویژه با توجه به حمله اخیر اوکراین به یک کشتی ایرانی در دریای خزر، می‌تواند نقشه‌ای برای افزایش فشارها بر تهران باشد. سوابق سفرهای گذشته نتانیاهو به آمریکا که با تحولات مهمی همراه بوده، موجب شده برخی تحلیلگران از احتمال شکل‌گیری یک «مثلث شوم» میان آمریکا، اسرائیل و اوکراین علیه ایران سخن بگویند.
🔹
هشتصدوبیست‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/676115" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa27eb9b0f.mp4?token=NlmoxEAkgTZZTw9yoPDQtocqW__O5gTG59puWXg3B4Fkj-x3lwlUourpL7HhIFHHnsfoClGSYVUkOk0sv5FLq3oRoYbVvVP5XZdYMUgQmbZ63VM2fz0w9z88RrOMwsEUHfFJ7MopDZkFz102nLAC9I7M5hpw-7dwgDkMNuHKZAVPk5QpQXggQlesO9oN3UsxmJyOapjvrNermmhC52g1KOL0fj6Y58_JkW8u-T8jIiaaWapNCImf8zz2OqTvTNb2wL3IWr5NSdb5OboHHvsJ4e2an2sEFYGkLI0w0K5Xh8pxNWu0IduzJU2I1wwhk72vOb2-8Y9oUPx2Rt97zre7blFUBu6GIIg8E1QRyGYgzI0E8urClHa0yxz35lY-XlynpAMCAXFiyWNyJfcFQ7EA81h1N_7g0aBN0NOkRx3RdirSnGhjQV4NnlPcmti6oDfFnzkDZ1Ycvde35gPqnlF2bNYH30cXOtllRo7oMQlOnQ8-lo8SSSad7TK0UNwhUDsDJxeNQMDDR5dagNu18bdiySxbjEz1-jFbqOdCY151VqCrfOWHRnoyMHR2dvJxkhxX4IFBsSO_uSGhBML4TM3PGfj_cKKEZab_e187bQTsNuSF0jxgOCGS_GJu2v4KCnTsE1gsaZYDhHoDYqKn2bxZ3cnZJCbR3n1ndIa16KBLQqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa27eb9b0f.mp4?token=NlmoxEAkgTZZTw9yoPDQtocqW__O5gTG59puWXg3B4Fkj-x3lwlUourpL7HhIFHHnsfoClGSYVUkOk0sv5FLq3oRoYbVvVP5XZdYMUgQmbZ63VM2fz0w9z88RrOMwsEUHfFJ7MopDZkFz102nLAC9I7M5hpw-7dwgDkMNuHKZAVPk5QpQXggQlesO9oN3UsxmJyOapjvrNermmhC52g1KOL0fj6Y58_JkW8u-T8jIiaaWapNCImf8zz2OqTvTNb2wL3IWr5NSdb5OboHHvsJ4e2an2sEFYGkLI0w0K5Xh8pxNWu0IduzJU2I1wwhk72vOb2-8Y9oUPx2Rt97zre7blFUBu6GIIg8E1QRyGYgzI0E8urClHa0yxz35lY-XlynpAMCAXFiyWNyJfcFQ7EA81h1N_7g0aBN0NOkRx3RdirSnGhjQV4NnlPcmti6oDfFnzkDZ1Ycvde35gPqnlF2bNYH30cXOtllRo7oMQlOnQ8-lo8SSSad7TK0UNwhUDsDJxeNQMDDR5dagNu18bdiySxbjEz1-jFbqOdCY151VqCrfOWHRnoyMHR2dvJxkhxX4IFBsSO_uSGhBML4TM3PGfj_cKKEZab_e187bQTsNuSF0jxgOCGS_GJu2v4KCnTsE1gsaZYDhHoDYqKn2bxZ3cnZJCbR3n1ndIa16KBLQqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی یک فعال صنعت دارو از نفوذ مافیای دارو به مطب پزشکان: به اسم تجویز مکمل، مردمی که به نان شب‌شان محتاج هستند را سرکیسه می‌کنند!!!
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
▫️
https://aparat.com/v/uov38ts
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/676112" target="_blank">📅 20:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSNKwQ0ePWAlpszfFwL5JWm67o-YvZOIbQE63gkYcmrTp7q0AaYzdT1fnMZwpI2kDhl9qSSDjX7AsULPaESn_tKpaW4j-1f4inBJIsyGzU-b_bTJreSPGUrwDhAYHRqgX6M9L755lHWFWmN6D0AIew0O1uqQ4duuST25R8UWCCdAbrYCzN9Ij7pIk18adH0tD_mVomUyzMJoDB0pQWQiMPlEVHwltMcMeLTJC2--ccywkvyQZ7eg3nk8UiqGjEKxt0AuOsR93hXCe4J_H8u3BzTU28I7ZjPb6vJhwoPVLVuXSLOk7qIAEVDwJfm4-qON7mTiBwFNM9viNY_xTJikdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش و ترامپ قمارباز در کاخ سفید دیدار کردند
نتانیاهو کودک‌کش پس از دیدار با ترامپ:
🔹
درباره جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگوی خوبی داشته و بر هماهنگی کامل دو طرف تأکید کرد.
#Demon
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/676105" target="_blank">📅 19:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک کارشناس سیاسی: می‌توانیم با جولانی هم کار کنیم
الله‌کرم مشتاقی، دیپلمات ایرانی و کارشناس غرب آسیا در
#گفتگو
با خبرفوری:
🔹
ما می‌توانیم با نزدیک شدن به طیف میانه‌روتر در سوریه با دولت فعلی سوریه و جولانی هم کار کنیم. جنگ‌های خونین ما و سران فعلی حکومت سوریه باعث سخت شدن ارتباط برقرار کردن بین دو کشور می‌شود اما مردم سوریه هنوز حضور جمهوری اسلامی در سوریه را از یاد نبرده‌اند.
🔹
ایران تنها کشوری بود که هیچگاه سوریه را غارت نکرد. دولت جولانی نیز پالس‌های مثبتی به ایران میفرستد. مثل مصادره نکردن اموال ایران در سوریه و تعطیل نکردن حوزه‌های علمی شیعه در سوریه. به نظر می‌رسد دولت جولانی بدش نمی‌آید که ده هزار مسافر ایرانی به سوریه سفر کنند هم برای زیارت و هم برای تفریح.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/676104" target="_blank">📅 19:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52551de2f4.mp4?token=ZjsZ0LdQfGur1TUcEBRpTrVoWVBANBaamof6OT7OMhpJ2gFNJrFMTbnjs8HHGmrDiGllFmF8wrXcr4G2-7XcQPc90eppyhmJyX5P71pi8naQADgxDVOog6SY5Awld9e-x-o76XhFXfrqVy1iOTUhvB9XXg5slUWMTAiPqyEu53lwy2wpILCrt9jaamptQ0-hMut7nKaomp-1NmWH9uf39lyVsOK3s2o8FdoI4Ax2f7zEUcr9boh6PnyLAvvzR2rVCKBgxlxpWqpgWqyvlFj6QP74TAlYrc6pMVtqXjUhbkvC9rLvdfBmmF43EIlwCuNwh07P990IKqooJW8MRL870A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52551de2f4.mp4?token=ZjsZ0LdQfGur1TUcEBRpTrVoWVBANBaamof6OT7OMhpJ2gFNJrFMTbnjs8HHGmrDiGllFmF8wrXcr4G2-7XcQPc90eppyhmJyX5P71pi8naQADgxDVOog6SY5Awld9e-x-o76XhFXfrqVy1iOTUhvB9XXg5slUWMTAiPqyEu53lwy2wpILCrt9jaamptQ0-hMut7nKaomp-1NmWH9uf39lyVsOK3s2o8FdoI4Ax2f7zEUcr9boh6PnyLAvvzR2rVCKBgxlxpWqpgWqyvlFj6QP74TAlYrc6pMVtqXjUhbkvC9rLvdfBmmF43EIlwCuNwh07P990IKqooJW8MRL870A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند راحت قارچ‌هات رو با سلیقه خورد کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/676101" target="_blank">📅 18:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676097">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های متناقض از وزارت صمت و انجمن واردکنندگان خودرو؛ ثبت سفارش خودروهای وارداتی متوقف شد؟
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری
:
🔹
از ابتدای سال ۱۴۰۵ تا امروز، هیچ ثبت سفارش جدیدی برای واردکنندگان انجام نشده است. اگر وزارت صمت نظر دیگری دارد، می‌تواند مستندات خود را ارائه کند.
🔹
در حال حاضر فقط ویرایش و تمدید ثبت سفارش‌های قبلی امکان‌پذیر است. ویرایش ثبت سفارش‌ها نیز پس از سه ماه پیگیری و جنگ امکان‌پذیر شده است. شنیده می‌شود به دلیل شرایط موجود، امتیاز ثبت سفارش‌های پیشین در حال خرید و فروش است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/676097" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676096">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تصاویری از نعش لیندزی گراهام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/676096" target="_blank">📅 18:24 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
