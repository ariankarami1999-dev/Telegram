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
<img src="https://cdn1.telesco.pe/file/acn1yKUn9-mWn7q_5SV0YkGza0r2z8nQpN4nTTwBxhl9ULHCwVvtz0XQ3vfBBKX8d4WG-C1DavZSq_d60XOXm3UFZ6-cp9WyB5ef6o4DHxGk_gWLyT4vvPHSGXIAtt6n3ORnoBLDUuQ_UaofCqEMOhYr148yehUj7zGpH6-Ts_wn1Z8AZ7zIAxux4XaMVu9y7EYXU-JO1W5pLDxrgkMz0k7M4-UYSSuYRRkGGI9dFsnIBbJvyx0suElmP103mp-a7MlTZZ_ynIJd8oNVloLzPmEEXOEuez6S4hacARoMFrENuiq8XK4DyNwG2d6H73HXLW1Qbe5trwvVIeNrZftSxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRziAWqh8tQFaxZ_jVpp-TW_0SCTpm_AuOYm1lKKgkA6O3os21snPWGbCvA-nGBcWXvOP-4BDWRPy3REbzryEGR5y6O7E0ezeaI2UsH2na2wfJsfefFbW7AGJeU1OjeUTOW9tfJrNXedKrFrARlzCQDyTinnJmydgok8dul2jFAlw82GABZ0OOAB2JwhqUI8fo9YSwqpKlDtsynudctVgBB89XFuwze8jEqj2FUk7D2eU9xVkO63JMOPxNhyV0mwKS_c55kVC096YB7MWR5MxRPxeYl_2UWoYNRLvXwyX2l2fvdrcvCBVayIO2EtB_3sy-T7PDqW2hq32jcNKxmuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ES-5x7Vy5tlNuXs8yIUpmAoE8FtX9cK_yP2uAYFzI7dSqWGFzrtc5ZlfC0bHf4DYGApVa2IqPbdyvn8RiiY9YlruwCnefKfMXMVUZfNVIFQRhfT6pA5mI9SwTJ9mW3qHKN1w_ffr43SYSgbftnJNNmwz48Eu1yAQxDazvbF0Kpfx4hq6cE9uxCuu-tWUZVeuA4HKKDzTzMcW2GKs9hLukDkF5Hx8OuhyXuisW50SzSijgKvYLbPS_e1HQSx4mLZ7tqGW_Z7MExAGh5g2frD8KQXrVaXgqjKjyWyK1H0OIylpCEMKThVa6g_ngPgyqV5OVindhsLeD5KBqHzz4B8gWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nnh1pb4z5ieEJyIqGLSmtO93zgX43ic6GtDFzdrFqrnvjCqbjxax_enFOf0BMLh_WMUE4TAS0TUix3CJk3s-ENclFE3dad3DOOQ3hCsXp_5Rc18sD2Vcaz0706-r7XeCVKp2zRK1FAbjg2tjGtsrIObuQkLh0lDqaMsCk0XZzxP_QmHPgrHPTfeVxrx-LG719xl-Ou36qz_5xIUqhqnvHI7JhGz_1tkI7PhE2RYTUK5mUZjo3BpN61tX41eya8raz7YhXC3OrIG03LVelmm1hOIcSriuDGt9Vq_g7DwjJkUGNFkb84BaAvHSfmkmnYUkMlFtPHUWP6MUjMUQKXVC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/efXD1ylDIvzxFFGgTl-cki17m9rqKYsLhTf7W1ngBG7sLqZhenoc7Zrtj4fKCk9qQujxQqeRh4o94h0yUpN0Rz-CcMJYaYQlhhGkcH7QVhjQypejDQcYDWtgABbjqm5eJgBZ9g-F3MZGq0n6qIWifJMpFCoX4FyM1tSqh_cMMzNAzQ8MNqjGMW9mpdlkczUSDG0ilDHfPVP-cm8hGMfvJp6BaZP_bIWGjxJ8v32c1xgj_2-ATnbTpout4BB0azZFpxEZcU3_5mHG-7MioFuiM06z_HIdvJGjQsK99XI8JeR61JRV1gozUogmX5L22QwoS63J0UfPGdZEisdNnWhfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bFxSBAGjDlNWTYqJ-4nOJp5_jmkYY7OziSwAqguRE8BM8hC4k1VSbREELoc5vRwZZXmz0QZpJGuDDJsfK3okAsfumEApGKNBAn1h_Fm6yV3t6dL9Lhs6QbOeVFJaeqknJcTXfdTxjDAJgwaTdy5zcXW_K_lZRp0hofVxaO-7xS8m7LsvIfexoAi9HDq3tt8-T2wI8ytu3077H5OSAfj4kVikhRCEOk9m_eOQ_504cu2o-niOl0VxzQhlNSiDN8RMNcmCE8WCrEYvhByP1zG2YrDIifW5LRFwLkWnzcgBDujrgsTWPiBvluMO4JZJrl3KjQoaZE2cys2VU-7TzHi1kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TLtuonlPDbzXKB9VmqG9ucQ_5JZ4s6Wj3tuUpsAKSZqNnhAj0w65o6tB75UMKhYsa0yOPjnqntngB-2ICkEroDxq_M6XHmpNfwTE7m3otHdKDcwVyKNhMBOtXsbbaqQLFK1Gba_hzwvKFtjeYqk-ViASEn3MGULdjvYw-SOSGPRCR6mWFOLqdrd5146lE59Uj-x8aDc8WUeBdcvfJPxFyfKWMCEK_Q136-_oUiwIrV0oh_6CbSziIvNSCrqA9bgm6MHEzr89r3yztvuO_xRbTy0coaMQv8J99ti8Cf1yyd5HeyDR2hrp_anprIl_GE_Fe8Nz5Ht4PXWTiVpo4pMYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHOuikU5M7RdaPdjzHJKXyk5BCWDwFK8E2cFwRcZweKFXq-DBPb4QvQ3Vm-q4y6vVriz6h6j7QXCrsl0QPceGg4WExopk0nYr_ptb-n46JLauwE1GyNnkGV21X0U_jcgmHDW0IRPYzaH5cjch9yElS1t_XDDw_eKFpHtXeR1j3ERmW8wCyLMfBkxc36Hv_lvJX-oqPK0pfTsND-wymW6FHPDbA8GJFFsJ40XEDsR1ZZUKtganehOJjV5cOxGrGSY4bvX-uKdSXjZXSGiIkS1BHcJpU4cdeJ7t7tzsZCu0ZhWZsU5WOehkFVUSjAD7jHdRDyysWmlYjQTb7H2TQgFbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcHLZNo5_FnbioyqWjh8hbN1CrgW4A9jCroM2tGjTJIi4f3YWQ_ipzIrKTxJwEpj7-6gt4jdR8v4kwLGNuqLrmGVoG3KbcFNyR8f4pTHdmd17bfb5OQN1yevXlqkuN-HkyUNjxCfgvHQM1altXACoGqt1tbNheTD8wpyA-1FS3pSUEopmNaC1L2GmM6XLfIst41Dp7CgAPBuIWFMEuuwjA4al8OCoAInz2ch_nZ6M5NFK_71aT9Ff9wxQ3ISPbzx3WhHP2ll8y76TOkbfNRmx8kVF0yKG-vg6pdKd2BeP7gn02Q7wTBZBWKD8M3X0MnY_24bmY1SINJyMl7BSjFuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuZTwHtmlBveyGUR10gAen6eDGD9soWo_9qP4MFiWpzrjTg9Cs47Phlmr1y9t6NYQzWhNuHc8rc_4OAhJTOPctytyC-i5xJf1EagoQtZOw-h97fAPgXn8Lf6pp0dKH1bQBa3EZe5RDz8COo_-eyTH1m_32uzHCo86S0oTaf6N34hFu2nu5ag234yx6RuxUBApOOxt0tQdzU082sjXYLxHntvFzJSfLqAGdQzH9SsDsG1yD_6Hk8LT_eaVcuPAqj_-UpnyT5YmfOHqg-9Lg5--IAYwNC3OXQhylzPtVu1kX1yheobBjhNkHrZ8TqeXfvNW5pu618nus74sOmlFp9a0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ0PPOoRyz_2DR1a6RLRJWP3FACzs3TzBp2bhi-IqyyktgCLBYgH_MoADNNJJ-C_HWrxNtPhJ0xi5t-2-WQmihdt-LD9ILKIN2er_Uac03-6lLOzqtUtS2n7agSeNFVgAIA4Md-G1AO9rRsh5Bp0XrFfzfWUJiVeCrRDIxkCburN0OML7Nfee4ZWhVLBsTHyIp6HPzuwguq1-aDqnGAMvgusmAFWUVq7Xv1IKRF6ugXPzqtH-ZmNJZ84E1RXnXGgd8_QI66v-P5OcYggbGvwpAw3b0KcfD_uj1Baku8exCcqmjtTX7n3oFLQvhbxZ5-Rkfx_1kyarC-t1-AhmD1Pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2Oalzj-10cHoEOhwBeuDjvhwK6uGzCBxOQTBkl7Nxr34r3Q3tzJid28CEZP-uoQ3WvfdttZfE-krb9barcsCaaf9XbuGzjou0wIPvkg_mFyVvp5okrsdEwt5t9k4ondAqh3-kHTYKisPeDkk2ADwJnZyKgbfgo7YNiwDDhMEPv2yfwFfBuHsDbh232xJOYnJXpQOpPYdiPbE7hBelIvvl7nvq_WQUmdfpgDm81GMhvw17UYaXg4X3zlBVbPhA8mHugEDjM1Mw8VBEG_9TOlotOonp0CxHjMaPjD1tJUAs_Y9Rf3TZjY0xUDLAlIoiCmUvq-8xqXwQYIkv8mKA-9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfiaxpbaOWjWYSqVtzctp1vvT3fH9ENxGOZUAf0wl4ij2s-gFHDmA0ntkYutCo46ci2F4ecFfZXWczdVRXH0LHHNV34jgesVqTGB-oUIautrQh5ogtrEAz8ZaFOPM766nHlLcAQFWm1RQd4NlHeV-V5rqPn8KCKWSk7bhXA2Eql-JYwq9G7UN67wjZ6oPcDWiV7mJIrH5GVGWAkX9lssUc31felAFT46tmNVCx89nHh4iNZGEmji-F80vaAzLaVhZFFRcYUAkuZJZ45qjSY13lvJBaNb6FIQmY_JyTyxd8K4Lj3Z6ghGf1KpFvbI3YHioVJlAB6U9KaaQ2X-DMazsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F3gw5OwekYyL1Ud2f1Meu4am66V3k77pKMWmL1RQ-9e0ri1W6HFimRD3XNngUxpsHa73J0vWIIz3UMTRHDBRhdh8YLfV4xXgglMyEuJJK8Z1NnTwjUmHFKkhc2D3UqUqfFnYSKsIzypz9RYWsEDMgku-ooE5MtV0jUmetHoVb0zwReLh23HQ6HpWHJ2QB0XpoXC58ZaiFDGKKTt9ARwgpVH_qCiPurOoSRfNd1eT65C6wt8WD7gHzlCBCLTx4u2F79ek-P3CsnIM-BA1yHWMdpFaUCJRsJa5wXPEt9pHwXKyBl3v3ZOuL12qm1H0obNJEw9F87A-xmCNDluAirsZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s06qr5VH5dOHaPgYuByob-e9MVQRI7_ZfpOPEp0_eUsKlJ6T00Hfx_Hcx96bppVXKfKbCdAksZR_NxELCItYJWq4a4_VeX-2qS4Ue0fo9MjXHNAHDIxr-YLvuT3l7cMa0AQ9cxCB5-mF60d5KVsMcqIG5-_Vu2hQwJvV4OJFpZSXFeYCFjh2QHTBE57aeo9L9CdxEI4M2fjHfGBOESb8cJGUhh8ku4ghEx5uwGL_3GhYIM8CQtJVvsHd_bGphJ3oIDP_PfqJHGYbQk5XaiWWgODnU1eZY6bwGXNV8j2YqMX-rbueoUy6xDw1lFqAz6w0hEzj49CpSfDcAaDXJSQbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hcoL3blCfv3zHeZU3sWEu4uGtwkQfG2_qqJ0VZi3KY_CIyY1vyfvQIIPrJZANlyv2nexTnOoNFYDU_qCUscocKO0y-ogyfUNowt8qMqkxdzM_ZjtxUs-47X9d2mXJFw05dmCk1XxmpaRHKltxV25u9hWXvlAoWGsjyKnDzP_cQqLaNzculY9nDxIEtAkNUL5788vp9CDTbXtrKEPn3x7FBqyu4mJGP2oQ9BkA5_5RLLwW8LkmyV0Yscgh_vnW8-8Qia0c2eFygw_t6ubeJk3mJtwVducik8F5_UyU2dMqeUOLG7Cl1z83fKg50EczrFz4f4414k0ViZkQv0Ga9Nc5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUPfkOUA5F9Q5BNoF2-gQ8RdBrDxXtVXFMmFdzjZ1hbBTDhzwog7mPaBpR_1JLozMqRuyoUx9IRlJg6H_c2DkhCGfeRDiRE24Sc-t_ZV1x9f-G0PBcaVJ1ranDjf3kygWDIbwI9_3mFR0DXfiqhmEBnt4zdJmzQnv9wQ9WhXT92pqOsSPmNDQgRFu5XFpP2Gro1M_l7L_fCrUq4_C_Yb9hB3AOl4zsPTuf_1oL5Yuj6P5CjbTT7Ud-RdqzJKsSrfV0EyM2y_zrsv7UypP0SrP-2NKD5Q9KwqMSudPD2u2vdlYzS2N5C3dmeJPbZKYdyn07HwDqdnLqdygHNCjsO1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WdBQGptnrnmGydaSKFHqdrLFAglZokbGLGh2GsnWckPASRtMPFS4FdZ1XWIcg-5H9Qg7yXy-A-UkP69ECZqEldMossnTCRfe0qyQBtMpTZDh4onaxe1otIntrRIIDFTBQCYOYpkut_Ikel0OJY-eDTdJZ_Nlz23-40jpl6d4zvKqdnAjKEcPgCm77xbKXnh6PTNIagHB8zf562wLhTmXAjTTwJizCsb-ENFwRHIAAAIm2CQSsNawFIvLp4BSllXp2x1FfcGjTvodgtUzDH1jM0_pdnY5L4Uj6MkakWKW2JjFkZHlsDSJIwPMu4IuZaOG5Ks_ZpyQW1vK_NkpELs0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4AH1qMjMJEVWYRWqjamfjJ96daAGd6KDlAiFOpH2teVJ6N06b3ZlXyTMM72WfunhbM9ti6D1GK4_g-bXRbeVnbZBQelg36gbJABIeu988gryYmPLh2qyZAYh3hVeLgxXhywf6og78wp-XtzP_h_9f_BrTTGFqa1c5y_QHYm7pD6P_-h8aXQHuvWansgLx2Y8EK-JorFuRfQeDN2Xs9gZ0CUfr25Jvw5j9A1BKwuovtLzrzo5df9CI6r698n3dQqoeTMQzfzeysgUFmTCehF64hzvQJzPeuEpXUeq8QYNzW7cI4HkAU-PUO8-nbUgXq9C76uVS4o5b-WnIC74Jq-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8vOtAR-fwwdwfiIUqBr_K1XNPmCMJtwHcoc4hpGuLkHxAW7wGUNjITn7Yg1u0vXbpC6lEJaSDihgDaUmpxHyX-gGjvDftljEEODPpZC44PatGqU59uxPhyDTS5svbsRluoSitkCV-v6CUvRLJG2vHUlKhQopFqEFV2gMM1AJSH89WAZDs1-NXs_HaKCvcrbIrBWZO462jDj-vDVlWutKzDJvgA5jdluG0AXo7WbNunQuhyvyqKo2VOg_9A7bz1ZsUi3WM0mA7jWhA5u_oFXCUw9uD7Oy8C4fFFbMlsevXVmeNb1vOtZf5IYuhBuJxiL5yY1b4io9UZYMEM0cfyOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEZXK49JxwK0LU56x9xnWx-7vg6Nae1qP6qnlc3epbKNRZU9K1V4fOdzUrLRl9FvOFXJGauqkDwviA2DIyE5nYz2WQJ0tZxI3KEtiQUnGqoMIulVztao2ucMyK2FFyuqwyLZzSxeJF59KJxAUfQo3VvtsI3mECiR7sEY_wP3aCkJyoxIYbEs_L8pIShfmKEo09mTs_Gq185IGF6c1UvPMQgBi6q5d40XgkxyL34sbVb_Z9YF-yv1V-ZgehvJTJnPlckxW0Ix7ogRg0qL-ym38PWvCQ67aDtre-2k0mR7CO-BUoClqgDR0KmSa1QuBvV8yI3gIK5PSStVRd7n0e9J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_W_O082osMbMYcvkEHHIxLiyH_uZ-rztnOxY2LRdj_rbJtlV--fywS9-rlSsnQ4Fc0NptLOirmZ_6mdoQS4kbSVLHzfYe2KyiWqNgtr3hHQO1_UEi2Gv3yD4zWJnO0BduvpXRptpvapIboVpnnfZB0VT19iWdNLPCE4o_0Hxl0VOwsjQmZoOx0sZEvO5gXVlN9yzGvoHv5y5hNQVw4AxZ5RygtUM8UetrvT1U8mRHytWGR8djHUNF0X1wbIv3E6rW0xRJP55HiKaTEXez7V_x2BeS6gL9HrZYgr-Dgd1bi-giqSIR8LtbXc3o3O15_tlphLKiaFGiNhhxmPI2nh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZGTf5R-nz9lbbkZkUzT0TM096CK1WNOyTp7OU8tBwhwo92R8iB5kNvxLA_DUBPmeYryxYaykn5k4-2kB6NgemfZNYNZiyH5Jsyr8LThU7xxLTppRvr9dRmf7DneRO2YYY8QHmaZwktwlNv4iAMMaJnmgbcfKRsViUyqJIAiJnJr-Lm4-f3Zubd_ZgddQN7XuyXoNMcpqiXFrRynOEIdD8UcfM3anz3TwRxjQoKCp6Z7zCXgonM9y7k4i_rklWfwQuW6wYGlXSb0suOWq4-OgatTMRrthqWXY8Diax_Fr2-Yy9aJWUm8tqMwXz6UedKiWN-zEioRT-8bSDA07iExXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LjRjdAn6Pws_pREpqiGAmrCe4N4MH8UAPVSF28yklZhLJ7J3ScIWdCqDAiSG17hhdgvTtXBwWPn2w8AMTir7hEj0U1wFYwVLwcoFIjVSLbFOC_pBWYPUnagseEV7VQCA-U6yhOry84xUZdYsOesuy-uOMDCEqgdwBMwk-5tRSR2Zz6kuEC7aj9heWi3IX2GCUeAtZ4uCj5of0jK-bmfl9nLNdCH8GDSQJUmlSPcMTqPACE8HlYIXiGgY_5jTjsMYMDVRr4sPs06d4q6vHdytkuk-IjYLw4FeLxVh9ycqSJiJTOGx9X8hzLSrzL1bLQWDPnM_uHPQRLra8LJvxS3v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=i5MbvBWatH6LD11NndCEb718eb7Scr5jGiJkBXqnYLJAKJwQw9qnb3LbDSUAR9nogwhzRWXywaab53uuoSYgw5ZP7QBAo9evGXHyLUAfyFEcr__E6keeSpng3pIggPI6sWzvtNKXbLsjwmKsGQRNdHc8gHTVcCAKCS01ZO1T_R8mZBvqNL_Rst12aBxMJl5sgK32bOFD02xu3xHmvvFRKzzi_ehJxeTilO4erdCjVTsjDtECjV7kn8erYfgzbOfOCDj4xJbfioTanrA270XUBj5WVrdm_l2d6Wjsb_59VUfTE4i4Uy9Y1qgz5eH4a0D0S6mbDK-D_f5mG9ncbGHuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=i5MbvBWatH6LD11NndCEb718eb7Scr5jGiJkBXqnYLJAKJwQw9qnb3LbDSUAR9nogwhzRWXywaab53uuoSYgw5ZP7QBAo9evGXHyLUAfyFEcr__E6keeSpng3pIggPI6sWzvtNKXbLsjwmKsGQRNdHc8gHTVcCAKCS01ZO1T_R8mZBvqNL_Rst12aBxMJl5sgK32bOFD02xu3xHmvvFRKzzi_ehJxeTilO4erdCjVTsjDtECjV7kn8erYfgzbOfOCDj4xJbfioTanrA270XUBj5WVrdm_l2d6Wjsb_59VUfTE4i4Uy9Y1qgz5eH4a0D0S6mbDK-D_f5mG9ncbGHuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkZdbesV5DSOzBnZ82r6oTmru-vkZsZRfbgosHJAL-P2pfdNeU_yuOFH8O8s2ouH_EMg5eIOgTvZATcIyWGagd0rqjci-9HpjmJgwowjMjQaxRCt21BlG_SUvtuUC1vILZmy8byQNnU-F6RDUPG_Pj6GWfDV0TsdN0umI1k7h53s5oB9q0sDxXQt0DBgezWLeAg-kvHJR-6ifCohJz10ay-8mi55iGUm-Yy_SjL0lD49ln6nA8ncGy7DBsR0IMc2x5YI2QrKa7WL2rN46wBhWDISe9czltORzcPvAFYymJ1Y4w2BZUGXqMpfmN5jKHV5hW85m9OALS9RQAENhrhQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=mTBhjnuyLCuYBkrikPPP0OkEmT4ScpXWdaL7bca1cBclZOR3dUB9R0r_jL3JGCJrsmj5jjwDCNLpxAPrBkdyeVfgm80_IET0S2Dtw-yJQIlOpgEvdm3IX8XfenGQeWchhoLFB-rYtNplNhTpJzLeiLaYPVgDh5T2e3p3GkxE0VIOwM67ylOhxza30DkgmO8BproX4fWLg19by9Erq7e5_whAeevuxBgGupjAU6VeQKS2F14kxiK_MvEJTS_scjdyEwaXXJeJ6lFsxeHf-IjWMGuOEQL21j_Jn38ZHkDlowD7ERHumNrJHXzUW_GbAG8DUwGQAGGp5LqJaY4afatV8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=mTBhjnuyLCuYBkrikPPP0OkEmT4ScpXWdaL7bca1cBclZOR3dUB9R0r_jL3JGCJrsmj5jjwDCNLpxAPrBkdyeVfgm80_IET0S2Dtw-yJQIlOpgEvdm3IX8XfenGQeWchhoLFB-rYtNplNhTpJzLeiLaYPVgDh5T2e3p3GkxE0VIOwM67ylOhxza30DkgmO8BproX4fWLg19by9Erq7e5_whAeevuxBgGupjAU6VeQKS2F14kxiK_MvEJTS_scjdyEwaXXJeJ6lFsxeHf-IjWMGuOEQL21j_Jn38ZHkDlowD7ERHumNrJHXzUW_GbAG8DUwGQAGGp5LqJaY4afatV8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=gMuubm4cOvIeuvduO4RHb2cOV8u0FbbJbvM3MRRCPVIH5PljvMDu2IMQn9cfq7V7gkARnx7SxAqIgEw0wYEZRc2OFEbtBvml2nsxU3mndm-GEEUSa1L9s7BXoprAZct0K1kp0QN0C-U2LfUIUepwrLCz7fmwSIz1GZ59AkdQLxm7vBgFYVsc1jDrdMjzJM6CebGgsBMNOuR8s4ROKKUqFTilk2eV5WdUK5Sew-jzTOgimYSm_PRORD5B1HAvlqKu_vLHNcJzHnF1FdZMEV21jffw7fWN3DqjwnJZDTMLcmM_su7Cqehs5MvI9xqp3SvPWI_GZJJaFI09gYtkrxzbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=gMuubm4cOvIeuvduO4RHb2cOV8u0FbbJbvM3MRRCPVIH5PljvMDu2IMQn9cfq7V7gkARnx7SxAqIgEw0wYEZRc2OFEbtBvml2nsxU3mndm-GEEUSa1L9s7BXoprAZct0K1kp0QN0C-U2LfUIUepwrLCz7fmwSIz1GZ59AkdQLxm7vBgFYVsc1jDrdMjzJM6CebGgsBMNOuR8s4ROKKUqFTilk2eV5WdUK5Sew-jzTOgimYSm_PRORD5B1HAvlqKu_vLHNcJzHnF1FdZMEV21jffw7fWN3DqjwnJZDTMLcmM_su7Cqehs5MvI9xqp3SvPWI_GZJJaFI09gYtkrxzbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QcYdbE6bCQW4snJiYriTHRr79iZPz0sCapLIzamSRMc7_WRmz-YdtbmctUwBdKqoHcMjm0z5Pa9sG6eLkwtejWZlY8EoXTHkm5LpaeBmxOgq5K6d3YSQrJBfjsrikIGKNRJHK4MzEmwC7aoauzuiTCeWyyJGb9U0DthATC9wZwtsSu1reYtBCOezj-be66OYKDQw3PynXNskPyKFGLqq19xDjKXkfU0GTXPTmaxKoMkiR-f-HghB79pr0r7dnPWvkJc4aR5ZuJNKpmrqT7xAmpMocQF1Aq-lAIBuXMNlhU7QoxkXLNChzHOwQ6gslaEx9RdY-iYY6iFXVPr-jGt2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/by2K6VPud_j3zmfIi47V-rfq3QXQuWSIRqUPNeZ1q_TO6LxCMoT3jc7Grs9IWOYLP24HbV-ucC1nhDJmPhx71Xb3zFrDCxrB90WK6hrj9rIE7zgLcBCoFsMrGdNDRhLYfp0iYhEW8dTAPv_hsB1VAXl60VoNhjSTcybLMtLqamespEzH497yBV90xWVqoFPPcznLiCED3Asmea8M9qti7nUaTTvYbs7sWs5_mQyz85kgNc2Fmj0wfq7Wb-YKgVZNURZ8esL5PJur03e9UsC76_FaExuWm7CpykP0SjXEbRa2YtSI5Y9Zg7JQUJeAcbwbMajp6zf0cC5xIqVb0n0Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoFD0fhlscMapNiWitdQwVJDziEsNwIJ8wFaEtWschzQCSPXEOA1QkpSF9XZFhnL-q7NgkANI36KYPz1Y-LMdJC7aHEjZ4zGefW-5NLPi71WqkN9I_wNV2XRY4mBOs9ZbgDl0BIBk2zJLWvFGnkR4SaPsn1QikUWo1ScTfTfHHC0lqk6zyCp5hkC7pBYfHZRHl52t_MZjuWuLjETlUv4DpYrU7CSsikWm5fUWydUPabfLbDz1FtZu4OCerqjQtxOHxaAuwMp2b6Sq0cZKjN1L4xN9pt8mo2MC2Ujrhd75ZZJ1jr1_QCFqJp5w-abII4KC7zxwdVX7jUGiksvyo8zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsqrnYjhXfhKPbuV1WXNctP0ssUTyTlRhy_CpOlkwFXAl8vPIzt3dsSArNCaZBXd9Yr56oxvonHN6ya5A5rg1En79hHNKRGWMO2bngOJwhT1eUGTGFEOinKtojthV32l4gcD-R2l3LdvCScq9HjU_qdE_bqZ2IOepHkx_L8M48FEbqzggnyoO2iX3OZ9pi2GSa4nxTE2Y4eaY190GnRx4iKoYlKZt9boyJAazDlbFV6LENh8jvmU01H8YREeftR3Jt-MrjkYum3Nb5f-k19kbD3KvYHw9Z4mpHqERWiryPvwW750A9Ge8E78t6W9tUM1JKrWf68KqrBfWSctSpzv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIdfIClbCjUdCg0vvyxnsnJbEb9hPNYaG4TQrVdisiBqiIV8u_44i1wzjbkU57gUa_1vyqincwME0uXFfDSaoUzOAEi4FgLG7hHcL2GgrVQCONiU81bq7MKDEeVEfc7OSHfsd3KgAGs_gZDrUTFnvvFYpH6g3aqHHu2VQnv4JGNHs0OHr-X32cYeE1MG-pMm5tmZzmsgpRMo6SCUZYCf62qv5HvEE8va93qKf9NKNDLGhgX1tDmmNP9KwRj85OdSCKLKSG9n7h_zMopKp9BVAgCIHt2nfIZv9yMqzqudXBT8GPvG6yWlSXOYm2iY9bdgzOafJLMki6Nor0DMTZemxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZASuWWBrDSZ5-_ulYxVJ5pV1AECBabDs5-edsK_Eo3MH3AxA5WUhK3YeKx6btsYBq_P9H3il2v8WbkhQFeoGTyVtjwa-uEtpnLyNgYOkO11EcUAA49r2RScpXxzUI5youvDMKH3dy9waeIVs_kx1_KmK0fPh05wU-NigufgvSoUUWOdZYbJ1sYsVtV4luzz-GQHI6AtM4FjgmhW3irq11sgOQok9S7ClVWHxvskwL7os-G5wwE3PifFArPWZhaolbMsZT0WeUQxTMJZ9YeuCnGFySDYjziqM16PBnsNrRCiZK5SjKmfBHU9qhTLdXy9xmyk8VUZP8aLO_XXmpBA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RV1FWlI3eN1HNWENpgij44sQ_bFDlnolZ5R0UdqRBk0eIvnKxUu-tgfUdO2JKDh1DdZE1APU0f85TY6C1TxtiKUqEyBSyvcCb1Bk3rMDVt9ma1QxRunmMh6cKD2mLIrZQk4k5Ed0gUVPFhR2LElMASBvhInfgpjAeeXeQQMwpRiKloAX4Cyx63z8oSF1NSvXggZRfhD84F-0_FtGyeReKVFRxo7yp1HwLoN4Aumd2y_3g-a5lIGdmxdw-xmIVp9yURBAotpBy9zXWA48-fqYvAfyRuSaaTjAQzzITr0T27wK2d_RcnelQYTPCOR-akAoxGf2XV3XWk1kvjMFkZ2zmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RV1FWlI3eN1HNWENpgij44sQ_bFDlnolZ5R0UdqRBk0eIvnKxUu-tgfUdO2JKDh1DdZE1APU0f85TY6C1TxtiKUqEyBSyvcCb1Bk3rMDVt9ma1QxRunmMh6cKD2mLIrZQk4k5Ed0gUVPFhR2LElMASBvhInfgpjAeeXeQQMwpRiKloAX4Cyx63z8oSF1NSvXggZRfhD84F-0_FtGyeReKVFRxo7yp1HwLoN4Aumd2y_3g-a5lIGdmxdw-xmIVp9yURBAotpBy9zXWA48-fqYvAfyRuSaaTjAQzzITr0T27wK2d_RcnelQYTPCOR-akAoxGf2XV3XWk1kvjMFkZ2zmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhR6evmPwlkheJGlSueXvDhwvOqY96Nua54xuVCSBocW5O-6kcAUstbH4K7n_1mcQqdD8eaxIC2n0sVGga5hM4MBaaWKbmEfrxMZkPbnkgx1SlcGS8LQPLNO41WrOfHZASBnUvIWDuoPTDcQTSV8T-nFyVwDT0-q_XEDPUyyfVn5EkWzyEYqGYKUOPKyy_QBVqklOwpdW28wtjttsVMnw_G1z9bOQ-kBa_7UCYCrxpz7n8b4CpvlL6Gp4DUvHcq6qwqZzLqZ7C6mF5RW-1Fj5-ju3p1SkaxL86_-hlFrL7qnDT7-2bvDpb9GrxHQYPSXpdd5s1SWMcpm8PbayI_RWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QdnT4x8CPG9vTbv7SLQ_2ts7IUnFyTJJjT_Z9Mnndm-_QKydWIxRj--JaYU2EobPUCEf8eT5oV5JOuDH4V0yRzRc6h_rdvzeKZrLlpRq1hST9N_3A4NIcrgO9FsvTa91QmifYrc9CHKDziAu0CMbc8pJSW4XwrNa87tlSGyeH3dLAAlDTWJvyru1-m7VxJvpvNfeufFs3pGO7lLApNRlmH0tqVQdO9qi43LgJLb5Ntepk-uwl8c8i5tQpvacsK0j4rwVcq8ji0ebf2CwTBl8cGzpycxFl5Hverw6p7odHo7tj6eHr0jhv3DWnchyreLV2eTBiM_rlXqdGv7jXxI1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mh2YmV0QP9MRv8CbTXO4LhyuqaoXWuNTQTnWrXFNZ6aCGpZKOaz9elAwTICqYQxeHwEd2VKXuGxbz2XUs3ueiovF3MPD1o9vcEV_lw90vRq-k3VqqAHKCzjqEMJn3ybJWmkOxgrGX0BbdVBSgvFLPnGkTTLu1IVnRrd1NElHBEFb82nJOY3sz2poKlNB4svYLE-VG4wSXX8xU2mY97VQ530Tn3XoXVdyilN2tveXzhjUYE5WAVRg80l35kT-DSI4W9EeJ35UPsC-NzBA23a2xi7ztDh_d3clgGNUcEOjhB6C2tXeqLKc_b3G9D6btBACw2yb9tT_d8LN2eN5GMrsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dj5q1VzqQa04fBNvuCPM9FiRTevezNL_osFPxRRyd7NoZGo6O1SQzjc6a1cOgAvysM-yPG3TbSiZIGWM3JrXkxu7Dl-VP_jwioDSLVITdE1Ri--SsuK5n6GSUTUjEXHhj2P-S_XM4i9tDh3YF9HV1yuRwm4NepU4dhq76rPIoUm52cHL67wtHsvHqCRAh3Wp4-QNtcOAiqvDj1pzkKmPuGQnhkdHDAgzJgYSZe8yNMVRNb9kJbjiF40TpEJYr_KCut94VMvgnt96N4UXv6rmPbxUGJtT1wjy5wHeXj6F9PcEjkj-rbFwyYWOJs4ZJfFIBKI9HOfx3J2xyaZ4WETQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJygiJacWxF_614ZfqNff9EjtB_0wCXlHcUwW6SFi6nYdjlSt5cLZWlrHed7WGI5RSosTz9IlQsPFdRrFbPkG5DO5wG438lasV8mb73mC6aCBuR0TtvEg5Sxk70rMASVB4-0gwFzezxStgo21bThNZIDEVHC7qjd36y8BDGpmPveYD-OEjPOw5Lk3l_d3EiMjAGuNWB7ARIi_cib8J4sSXEliJcQZ1dlyeKwye2h-kl7KdcQQil0uxixsVNWodX_7jkLHLL9kTCCLTeHfrnIvGicTHh3pxsCYsTJq6JctFENSGKH59NmSsDwy2lugTO8uDVb1bR18_DWiCWi4y_5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gQEPRINMhCRN4A2nWnRe1EOI8mFgcxLLq_wghbRhcdzaC0jl5TEOTCkNEplCSkRvhL9c5-SWdomU9d-gL9db5Dz92qpU_mM0g20DjItryy2aI5JfSSq9TOJILYPzc-YLk6ERJjY2pAXdiXCsQ3PqeAKvbdydAnEcBllY7R7oxP9vh2w2BbYR3SNd1fp8QZMvkU7XuzkQW6CvahboV1h4mfOAuJ9YNIhnKwpbLl1QS615Nhs1fhH3DCWsi1qGk3kd1k2yngz3Iwyp9ORjVhVnYqdnIID-zvpn7a5guzr4Sz_I0A_2dD7Sn0VaU-qxyN3PlI0WBDuNenOF9eAYSfulSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpPaxESiPC0joU4r7DjzSNi2vflzdT3yjWeLk5ptZoamps71cyo70JADcV2TVqq8Ce2IX3zuv2nyMDMIcIt99lDDWHMPhvbPRKcBV1wl5eISfwqSq_zL45A9okfexph6kUa9I-yGbwf0famFv3RwW2FU3Aarq_4k_Ux8L3m5AgZfFBPl4BwBVDsyfaanKFWorcJBCMR0PwRs7b4HW36BVCFOfCQk5kYZ4v6AOMOkooNu0KLh9yBQug4eFNhle2w9scZYYa2VwYAV2YsyhJbgslrhI6v1lvL8lLhwh38TlqxMhxTzcezzyl6UU9Eg_BB9ogWtix1qsUxIwI4dSFUSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=ZIgMK9UegvIqUeQcpCV8BlgYCuwjLeV4mdlEqEhtOPL4jOlJhbH-C7e2ixkO02dAgC5TFGwjjv8zeGqFcmKlrmGtPMtwuFKYmi6lMeWy3zPMSln7loW8p02dYb-cI-v7XdljwE5v9_QfLYrKgQfrestdorCfNe4Hge3SGxEOr8LaivskFcFkC80rFnwMiJN3I-Zb363jsi-e0t15gJaUECvFLXqfAqpe7ziQq38JFXVa8m_52WZr2bT8wP4T_EB14AbdH8q_mzL_jdMmn-1BtSYo-wTTxMyfSfrrgRABmasQgCkWOimWcLjjPbilXJasPbvjk3hlaxvOD9n5kiV_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=ZIgMK9UegvIqUeQcpCV8BlgYCuwjLeV4mdlEqEhtOPL4jOlJhbH-C7e2ixkO02dAgC5TFGwjjv8zeGqFcmKlrmGtPMtwuFKYmi6lMeWy3zPMSln7loW8p02dYb-cI-v7XdljwE5v9_QfLYrKgQfrestdorCfNe4Hge3SGxEOr8LaivskFcFkC80rFnwMiJN3I-Zb363jsi-e0t15gJaUECvFLXqfAqpe7ziQq38JFXVa8m_52WZr2bT8wP4T_EB14AbdH8q_mzL_jdMmn-1BtSYo-wTTxMyfSfrrgRABmasQgCkWOimWcLjjPbilXJasPbvjk3hlaxvOD9n5kiV_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccHR39oSxsse_-5hT03lgORYWQ9WtWxW1OaGB6KpZTmoxojJ1oQUaA_FCzSp5rkgpdtUseS5sV7lmK97jpb_ED4H8vLZHIk-oXDHm0Ii-eSNVQ8anGU0FraSJJoREXxdyZmUtu8G48fh2YJM8sT7B-c-N8Aeu_8-e-MYYai1eVhPll3LghDVQMwwc7rjzLXIVpXTvUgeBfnZsD9MRGoP5dfUdw0WBVuN3A2F5mjLrpGmTLgpm3kDBJAERNqVxZmXfCssTCQ9ML8PFDbl9oiWIIQqBHesEacSc2OyGLfdH67oG-6JZK9_5FGrG6UEVpqKCplqwIZ4djHvJkr2KP_3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GHYJzPQO82fyLDhMtOHsp2GCqMAhVXfd5mqiNjD68ngXFyFKGPTlDfKnPepALokad9igjMMi1gEHxJDD9onjyAgd6MiPn34GU8Z4Ig38MXmujyuwOFFkw3uWA21hO8DhSZrS8J9MtpT9mpVpLrp4muLVtBQHWYdHGbuOfE-JgkGaWqWWVleKXbhbHul2f0-mQzVyR9hwllyS_OlD88mfE7MRwPifudFq0S2Hvk2nEYbUrRcFjahGuCXLCCSLdSm4kQ8fHbjqj24EagOg3z9Q-69jX542gMWonfESPATxc0wi71-54frv30CJSvn4MzWiK7TWPJ_QiHPOaFQZ03ByEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dlP3B5npJxp9t74WW1bCToTHq-XUDjjb8Dat3A5Z77JJPMAvtbMaUfrymu_f6Isw0PN0q2vBHU-MfkiSsGlksOrGDIuoxQjGiY8RdrsfcKZAlMgbKi1kASSlaUQ8c0KpGBCulyBEwreFfisqfKwrv8ol7sxTLTSuQhR1bmUASH_SJjW1aKCPoXkzb76oZW9ZLJ-68tQAe2kctvWjG2jKDRSOAk8EaHwzfPYv-ql-BcJgAJcsVg3KEG-WbdhcKDUwET4z4X8o76Vp161GC81aBoJcOgmdfps828RgkzCnZ3FfzSj46pWa6-DFpEM978pPNp83UVaZzxA1QZtTivObdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qa7Sv5uTYVVJf2KH58gb8RgnH0j2Cd2kz_ecbxCQ2ylClyMDnenWczFnrXrMQ7N9QRrhndEsxP5D6QclRJirTzNR98TsaMHHq-d9K62vjqsOfROlJiiDiH1jJDyJ8UYu0P0piB2eKLX85af8Im__ffrDIJfI55n4P9Fr5Lwvq1z7_TCJVdY7WL2dlXV4IaozUQSUDXb9_y-iVRLySa0rIIv-f4QrfQc6C2-pMgdA0iC8Aql0POTF4PDdNvi3A3Rm9P2by7f9SEIaj4K8y5dQYXgqlMbkXQgO2tpJ3ocWLZZAXBrxPi00X4EvuRKQLsT0iLHNqVRcF0H1FCCcbiAj3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8lITfBSrO7W09IXTuf1PReTqQslXD_bSP2cdpwHxWUmUOvvmFzZaCEMMyyYmRPaF8c3-zJQSngjRQHdF3x0LtJOZWXRpJ0NRPbNAz2fpoOgyyc0am2hFeDntMZQPz1oWqgdofW2Nvew6tyhrwGGXl2zL1Kix-UVjgL0bO6MsY1oZNCEzVGfPdUgTbRq6BIvzs2bDDeW1dT2ZPyjbGF15FuT6g6QA7Sjw6xmMSPARbHDxQ9CcCdliYSPdGjDOixwGS44Py-Itqrl6f-RWJlZn71aJ8vRf-7U6ZlIBO45mA3UifOgRm6V8Lgv_ljvUIUALxadHTFMnAc47w5WP_7J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
