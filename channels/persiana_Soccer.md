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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtXdUlHgGWLPaMMav53mBaOzEh6LVMfYFMv4-UsV45MjDUaFIArMQPFU_PtKxNd23SnGNVAGAIYD1q2tOHbMqLRvJr2erR-WorI_RYY6dCDXAZB-oVpHN29GZR8LEv-JEaJPfHeVq-u2BcIb4mKbRnMCk5FHxCI4M6152FT6w7U_B_Ysp002lQ07bNKRYksjDOrCO3skheQpPUcsTUENAA2gpTYlRO3Fj5-YBCxZTRMbnxUjGyCpmab81rPRdIthAVMegX2SUC18xRIEwvF_lAa5phmA2vD4UIhIUIPm-fmGbLfjUAZCNKio4BjKge91wN0ObA6UDajfQvj-TJID_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEwL5_OZhQQbpGr4gsiCVIHgUtuJSbG-AFljFlerMuWfN3JbSb5rIeFNQHDpOZfPVQzdydI1AxthCLW1qeBjxx-2GbbZ61yM6yjTLyXNgw9gMOXb8lDGaZaBJiUVY9hz_8fAOgQ6bw73IJSnQY-Q6QgqurBUm2SiKFQL0D_giPyalEFoPk98OEmmUQxkn9t7uBYYXFOez9lOpBl4XVIVsDpPc4ZOv7xT8Ro4RHVgchkrjSWAyw_alECLXr0IIale7l3UVTpr4K6NSJgWGlM81x-90c_6uBkUA-ypGyHUwQo9vVxF77wRU6e8NUkkXbTe80fSA4NVjlA9S-uFRzGkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGOQ_LVlCT-tmReaDAfXPAwJTkey-3XxTc1esIs7kMVvRY_f5047n1SVttLjSV72SIGu8yIQIEPZLZJt1dOkHT4-rcaCEXEzsojT5j5uBd-szCGlveWomlBckz3ni7lJhKLaRTIzeJ1lGnRC1hZpQIwFZ_olJyN-fHVuwpRS8gvYw9KgXx7uwKVhH7OkouquC2YBC9i6W451GLJCAh-vqRYpMxIJFxXPjE27wxmHv9s5gENzc-FqAieKych6gPWjSgNzkClX2SI3QoZcIWe7yo4jDlx7sjcbo8dez6rMjK76kxauJSRE86ryRsqRWwOABffAmqNW9ah4kncN0KpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDB7hX2nlnFlXLk7p2N6Xl22BDXB3kUQd-Db-smW8daFEHc5DoVE3lAqlsDnzQ4nUzfJqw6WzxkzkYfBjxekr4iCjzo0zymey5KkGtrDF5GJBv4pfgVWXdXZVM50ItpMgj19RG8dg1sWbeVzKDQhynFFY-fl2btbpgQIlfvW7Q0SlQxHiyP8MMP_sryII09c2ZvL_yXlsslJpINfU7ESqJcK8vM542YxdhGOUnJX44A0nHJtnAotIeo83IfH-Th72pLpsDgwTAV_69f1tUFhDEDuqYN0vt7dogTVYWo5BuJgmXQNT40i-xoscL4PcIpFA1VDK_LiRmFs6W07NSOA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT-BMpZ4cmEZIqMzLwLUSCIpjYTJvpu9sLkB8qAulSxfbmuSIV3Rab1uUEwgVMnjhR2rjUKjfr7g1Nl-0iv4WJxBOV7R0KFLM1Jb20rSLof3nW92JhEz0ZwAStVUJzNsnw3kgEm3rDa2Aw2AQNYte8Lkr_KsE6bHco5fJ8jCHIjpLYW9uNahizVDbgREsViYhBVz079wMZn-ovl8dUptqLOvAwal8I5EcjmgumcAi_QoW97MlWwwtBB8Cw7O9QJsOGJ8muAks6Ut9YMMfz1OyYrP0A28j2iGtbnVWFfrcD1kReOMtO1-Oq1AJY4IdReM_fXz1KJkDl5gYnDZreJ8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm4BeTBYPis8zU-uNYauhHAhdRPUnpbNENkme0Lz5N3NXHpHYBdmlsFocTIAgxPI-iv-EHtcEPnu9CDWdIj6xW2JO1wiuLCs7qooavWP5JaGLKlCtNjH1ej18UHPMv7mHJ5xpkxSIZTUHXZaZDLUvjJPpR2qCxmkY_MmJGmaLhZAqPsVsQGMSzsQ7jE4mtBOMGvn2s5YLbyjXNjAwVRkgxqq15qbisKrzyOLPRuEa2dCbiDfOOclikIUYNFA2j1VVjUSMCoVcQr9oRC1EoP3K1_UPnWAwcVoEn0cNvlcsRO-agD3R0W2c5jOfOSrr0MU8Rgcclse5KMWYApcmPscLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiKiD0krFPcIHUqL_OlcI84w0zGC7hXkJtKr15k3iPI9b8D0SnJmnCl_Yg9WsHaXmzJOU0j-FagB24mKp4zW7Y2UhqLxtbDYmmCgpBS-RU2yGPw6m5eRKFYdI-jfsHVuaP6pHIzg__x44MnnasIi8u_MDoGvkfzu2AeGaA6yKvjCn--euIQm-ZzPvWl0A9AWc21ZPFbbY2iNrChym-Wp_DnfqbVcM7VvWwJFGG8WY5221KgJsVuCoWznevXIvVh2TvdwieJKFufUxzxlgq0CN8s19QV64vHXR_x4o7nREZ9TzzjuFZ03D5bKLYkWqd-03eISPOLrdcozkyhNatjUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTVYDX99X501HNSVkFHPrUpU_D2kthoqRlDsT3sQZxDKpjxj10lK17HsCVFfJPn7IIvA5AasB7azk8HFfRRFnQ9t4kJomv_qNivlFIU0DIbrUQQ0ScRh52T1qUr3BhF9lauAX3yPptpJlnHzXhcnDVqDUubBJ-MBA1eTfU0ncxUsra4PXa4J1rf0DcHCdFPx-SxK3SXa2hb7wL4Iq7CZkv89Dlln-HAUJ23Cly-uvf1NcIdJy6Mrf7FlGjI3VkNU72OczqbqxVcW0nWny9E7gGnszGuDiXsGNsc_BCcA4OcBWRlm1q8VcUStsLBoO5GVoyboSVfjNKk7Y3WUvhiIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T46FztdUoL0Odatjm-DOFmvpNH2OxFs_hJ7jEy2RnwhKru0FT7k_MVZ2lQD_dlHtdVENsU2sQ75Jri6K3SBSGEKHCS4k0OgMkA5AzBIZ2B7iBlK_bcL0DVAKp7R5PXLeCBPkxoD1uQ_fFCqPCYey0L9khuz6ZgRO1ksYSAZkj8lYoUO8Q4mSCW-xa8Vhf4WHOUkBemOKdPbYEhgCaSc2VAvZ4SxgM50huoNvtk-R9TD0QyT2E7StRJmqcZXD_-fc3c6qvHSxuNY2jgHrhRhgTvT17aw3_qQmrlM1VwpLiwVIlg45Q8ZCP0aS5m3C-Xjw7LKAeYMEx7S-hrTu5uJfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPHEbU21JNmElTL8Ynw2u3kYQ08iB5AMGgBAjkBFu7ojmrYNKsASukOJaBtet9UDjPlV0RSrKBJ8DhbbtvJv8wNU6wtpbnfW31MoRcD-dKL9QnSbt3O9MkJeerbQT_KGAU6DJNsjQcIq2lP2lsYqRKM_GAy-ADuKZ7AJOJGKt3TgNwmTkh1lkreNmeAD1QC21PVgKsThfS5R8QEx1iZhjv_IcRqnovTpaFdIGZngfos4LfcyvInK0V6h717O-bI0x1ldyULriUHNKg2fSIhsBJMDg6WLlVK7Ly5GnpEfEEhzqVmhE1myyke24dUOukR9hHbolMO2Cg7tdXETGAtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPNZYKXKA0GkLOWRy4r76it5hHQ_vr3WERNoREjKWn-uKZzro7fhGKZvPZeqZc0_2oK9ifTEC0BjbkUVkdh9ijLV9sJ9hqtRWBcfcLE1zzO9JRkgOOVejo0M0j438hpTHoaEVIzxC1C9rMd3TOPAMC-dIFX_MlHWNN-Pxxmias1rlekNUKYtC0zf64h_sYwKCGbAkRXpKkbOzs7pW2BEe9cBCg54U_K3NxwXyblRRhT37a53ZJIMRWE0yMQmV3Z4T2SuoNUw58ilQ6PjgGlQnXosc4riGDGiTp7AdwXOMcOX99vvEam7GqO3o9HwYT1pn5Z-E0eVS2obvlcY7wVbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRmue3ezV0H_lt0jaCePynL0DTsmbrgczETEKvy77wOhsqPKRlgf9eNl9U_qE0KhDUj01Gucf2dsU_5nyeiIooe44Zn9oBGcFrHXO8gBIniDRLBmdtjYjX4_Gmlu9Vrnl7U0SXN8VvF2C2NAThDwFF5PozPcZKFycxgOGbb5BmrA0CQnlTrPvFjZ3rWASvnm--hKUwTfz_qnLos4PDJcKVnEDzkKYiO_6p_TYaWdcoyK7mL7Myv57NcRHycp0XJjfD4KFTRXrxQbY0kQEz24GZbt6BwZr9y8cTQSwXiUosf5DHKbSklOQT-TG_3zfXRux6VjTPwMHn7ubeluXt3LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLEzzkzq8n1FBJ3LaUOZWUi9YkwFuIbwoE-2eZzNL2LtHD29pPL1uLpMQdena0xU5bR2ED2PNHNY9flO2NLXDBRgg6shpaU7lfipgllRoXHvSJ-NckpgAN28yIMBO8g0K8cevk1dpSZYzbcO50unwgXDMPRAmemP1EHAyRFJJdVfwhCRJrVafI41wBx2iK4SbNk_TP3CtC-b3_Zv1KaVeRHRvm5UmThvPEmNKwzlLXW3Su4RCyHGRDHyGMW-DYloWKkGcZU5hLlDTCT-9RxyD3LZhBRalce20S6FW0Yos8TG-em7Jubbf0PrCHyZPV6e35oASuLPoaQsdxqlPgODoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD8xhcYW0wwCmHRz2kGD1GWpwR7HbjaEHjH3J3543VnR8iDk42SiU8b6Pn4dwpNvskaJcbPLruZnWFG9tty6WEekpplXg_tCsq6CC9fNrmDGnMK90EzaCpY-15UrQUBO3LHQ6FmRicYIKYL_RnjDURaYlIMfxdtWLzEinDrHjzln6tpEnbNCY3APl78Ml-n4noC10Vj19BxDgpr44Buf5NcKW6o1J_w_dSOX2qR_JRBhWLxQ-wzXnuIkDB6Atvlj22z6B5Pn0AcNhwLJzDdyzwAgQsnxBgAR9o123y517fPHsbN36phB7BE6kXx1q8uk613iQx5yajxEZP2keTsLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJK-WH8X-mfdjcf9Gg_ORvUnlz2ao9mInKqAFisapR3IvQE4SrA6denfZEhjDUsiMRMxVU09-sQZkGo8COjKMjMxrK4xFdoNUHYBOrdKZVPlmnCvJmklb5S6h6zNagHgtedv9jI1QYBifSA9hfBzMFnag9UeobOJuTRkJDzxP7bSvMOBi_dWuvS5LqNo1LX7xNvvkqbX2Aok7N_nyGas6113wynYY8kiFmT1xjrFoaqutZa04bPkMxvJx8H2b8KXmlVE7Tgo00Q3TWDEZlHIMVBVCFqRlnm7z4axDpQgsD24g4DbngkMXfWhHLEXSn-HJ6UfP3fJ71Y38-i1vgT9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4rll5Ya9PTX1EMWgBLc4hdKilq4vuK2HmEnIDHFZlMj9RvYSYcRvK6fZy7hl3BZej-KYe32DSdiNbZSI7QOef8050pov3UJumH88jyQyhhL4u-kAv03mChSnMTWyqYORUWb6x151qvGZtc9E8CxvqMS-LE9Az-KZdpT8VXppt4xEeP7O0yRyPCwz6OT4lpKq2NeLgEgblDYya79OfEPsEag3mFv2obKiwwvEVT42D2Y_VKcXIMYI4yWcqrNjh8NzmQaE-W6CwyomfNEB-WOhVb3oHafG8e8aqE0xuC2QkIxRg1zhdfn3eo_ysUD9FbrPfkwr7aX6aaPUsLJ8UJK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNXlNh1dD4NLkritqJaEUVRvRN0QJfpLZORCt5dKP_OCtY6NRAPa7G6POf8k3IbCSgL3ndvkIkiWo3pzb8p0xKWlbLeN9dhbmChwUjy-4RgCgADeZQz_WlLJiA2tReJKdbmLfFLLc-_puaaaESGKHlJHm8CYTVI7yYCLCh-86goe_cJet-azriJf5XXcF7jDnv2AA2Hxfz6Wrc5hdloaKWNK8mlaVbBDdwrGGWv0sRDiJ0tl_cJnP5YGCjSYpp7RKRC3anITAfjPPPBgF68Eb9LIA8guXOHWElAz2qXKqUMTHkOJk3KFPxJpcoc5ntSbW7TWDShSxmdE9JRNsQBT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkJhygFqcptDhwlfyX--eb-SS9TUjnkBNZcm7Soewo2OZ4deC4eamZ1Prvev8zkbTqLnmMJEWVCOQa-frOXCg0slhePPdiSlWLedNoNPiKfb5fLi-p5Za30xjeJ2DTZ4n2c-ip-wFbz8yXzDAkfbOIuZaoJ8qKmdhLCuZLIgdI3TEZCoVFI6pISErJ6DeRr8CIDKkjtSq1zIqEyLL0B8VppcR08QPX0aimrzJJnJTTD60103gAMhLOewpethLlMnxWQfb9gQKrLgtB0RxyJpdDOx69Hl0r8ymye36TQzni7dJo6DMgqFoTYL67mpJ_3BuZ7u883MjMZiXKQjw__i-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=MQOxkKC3qIQkYdE4vwFfSWQl1psT7UB9CPbnGi4CXB6TUrxXpHPR-SIMxBwX647aW9CsDT1R9pr8KElVBrjEn8-SK-CYHX1r32Vlu2ZaWLQfis667vSHGLulW7BecweCOu7EDFZ3dECARvFxhZsbRxeHE2J1m7VfvF1ZXejIwv6uYC2hIPhVxtgvCmvDWc7jky8qxfHeEKXgqZZ2iAuT1sGm9MmGha5MsN_7RU3S_jm8pAm-st8lfucdbHQFYi4XaC8gUszdnBkkPFCkMdpWqgWxBTXsstyP3s84p_qS8i9oD4XWRImsS1_1aNvNyfgI3NIjSny2DHA4U8w9B6ftDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=MQOxkKC3qIQkYdE4vwFfSWQl1psT7UB9CPbnGi4CXB6TUrxXpHPR-SIMxBwX647aW9CsDT1R9pr8KElVBrjEn8-SK-CYHX1r32Vlu2ZaWLQfis667vSHGLulW7BecweCOu7EDFZ3dECARvFxhZsbRxeHE2J1m7VfvF1ZXejIwv6uYC2hIPhVxtgvCmvDWc7jky8qxfHeEKXgqZZ2iAuT1sGm9MmGha5MsN_7RU3S_jm8pAm-st8lfucdbHQFYi4XaC8gUszdnBkkPFCkMdpWqgWxBTXsstyP3s84p_qS8i9oD4XWRImsS1_1aNvNyfgI3NIjSny2DHA4U8w9B6ftDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=NMWvin1FhTxON5xPmllB8uwlAHe8TnMrJU64n0XcKcRUAdQ6YZQOvQoPE8tiviKW6_Lvnz4bj4WYWM0xzac7bfEsZCEXNXSj8QYlBriVb1nHsmhTBuNSunwbxe5738UXDiq6QnVENrVlCXcPiRgUtOyGDt-b0XniSccU6mO03AC-IvqTmDo5DxjlmDBIUraklPABnQ1dNQqUGrt10jUZlJZL04MHrqp3y0V9JGiB2LMf4svivSQDKIFQ2RaYc8OcbDHQKESlVeGBEE1CfZW-hpuaYea6jBW2WTy6YhXJiCePuQB3W0p2I0hwmwoZxSTxd9_W4mF7mF1mUvoNxOTqbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=NMWvin1FhTxON5xPmllB8uwlAHe8TnMrJU64n0XcKcRUAdQ6YZQOvQoPE8tiviKW6_Lvnz4bj4WYWM0xzac7bfEsZCEXNXSj8QYlBriVb1nHsmhTBuNSunwbxe5738UXDiq6QnVENrVlCXcPiRgUtOyGDt-b0XniSccU6mO03AC-IvqTmDo5DxjlmDBIUraklPABnQ1dNQqUGrt10jUZlJZL04MHrqp3y0V9JGiB2LMf4svivSQDKIFQ2RaYc8OcbDHQKESlVeGBEE1CfZW-hpuaYea6jBW2WTy6YhXJiCePuQB3W0p2I0hwmwoZxSTxd9_W4mF7mF1mUvoNxOTqbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8viuKE0xgnaPA5O3651BdcdzQE9svFOkepcqUiha09TuLXBKiC8nDbphNxa_SwaAI7AKQpOtJ4bEu7resJvdHsjIHtXclAAHEjHoG1Ln9FxGnRpWVC2GRsu-twjx6bha4TbuNqg2e2_Oz2O_EnOb1B9__M5l8p18JD0VkrYM9UONQFWkVvMO0I9REbbMyEtbCLUqxy7aAKXgSySnqM2K5C6ZLUjbiBJrPV6Ex4qul9Racm6j84Az-pYUD7Ey1QH4tBi3HNVfr2fargA8YT2HzXZMszi9FS6IxiCTd-EFcKrvuR-9I2WoL_Gze3C58jxiEqkrk3KYfASskfvRhcokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuVZJ6c21EDKTbc8pWZ8wXb8yYS984fBPSp9fpYcRClLEvNyMj3YsxSK4Ymr1mNyNBhKVlgBPHs_SLM1U1Ma6TQAHbELDn4RenFl_tjP5xa4E_AUD3CZpqg-8H1xAbUj3CmRnZcimnLe9qyXeiUonttX5Bva-UI5IFjz_nM6_htoWgd6KL4sBbLMxf2Jox7NUrn9fJjSaQAnovUTbnTPCYIVYL_lawL6n64rAzhs4UVdntNRT-gWNjUrZTv0jdGZ8hUoe54hnE1pKyeo44wcGMv--SPk_t-lQzg7rP4W_vEo7st3RySiHHiEGlbHfTNM9UkU9GjbE3pewCMq6QMeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=XrA4iS0h_eN4owrNaTccQO1oQVMmkc06_M2ScD4IvbtKwZZNkoFDXRm7fdQWCD7VfhIO4CGcZFJnTsFNCgKShRgMi4UQC2bixCWBrszz9qwvxlF3HctXy0NKY1voBjJJcd9kiF6h2ZKHskO-pSBfFbB42rVueB4v_gaqewrmEg95bX-ogO49r_264jdLTaFi9Wn1nOnrOyWtBqH8oRg6cdu6MLZkS3uWsC5vApyoi8JfkMyVpsBELMNhpyHVguyTGJE_7Gv2el2Lhqn0UNw3qfteHQMb_9fX-NzHBa2uDbB2WMlnrxEHAahEl27lAHz5HyCEflEUybe-xQdwyKimyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=XrA4iS0h_eN4owrNaTccQO1oQVMmkc06_M2ScD4IvbtKwZZNkoFDXRm7fdQWCD7VfhIO4CGcZFJnTsFNCgKShRgMi4UQC2bixCWBrszz9qwvxlF3HctXy0NKY1voBjJJcd9kiF6h2ZKHskO-pSBfFbB42rVueB4v_gaqewrmEg95bX-ogO49r_264jdLTaFi9Wn1nOnrOyWtBqH8oRg6cdu6MLZkS3uWsC5vApyoi8JfkMyVpsBELMNhpyHVguyTGJE_7Gv2el2Lhqn0UNw3qfteHQMb_9fX-NzHBa2uDbB2WMlnrxEHAahEl27lAHz5HyCEflEUybe-xQdwyKimyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfrACnS2qYu7nF3QMATSnPVSHw_hhZLwyYvJ3QslZzGb1EK2faUGjkL0aC2tezIzXUddDESfLeNvjO92VNhNK5LuhOXKXa6K8fuqA_Pfa911okug3105CrMIRd3ZMLZhEs2iP1DAUW6-RjYwXmnqbnzvVjvSMNHjZfbRb8q7s_OpSIwA8-Ezb4AOQL_xLSwc1-8XL_-VevMtuz8Qlwn2RtC2jRlK0dRtwxLnDWWvNARGFv3deGDvGgiV_r2MqnToBYvbidubfK_zRGkwKLuJ6PwOqefhmj8i_KVK1eCQc2UQgntlFT6cVIsz4ZQvJwz7LERjtF0p4Etly2AO9zxOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2wSLr90Jllp-MOvSWVHef9ZWo1FmzQ983_VsKYHFpyAYapNj0AJy_AKhoU7XNNQcVD3MYYTmnPg0EWB3wXDTrZprmrLoAzaek3Rzztsfd57cu6Sz5mWTpe-xjHFtj8MBUNbtJhwSlA63oX98iGgErjYKyFkKVMvHBVfdycj4DWRfpSF4dKDqu282ZH5PyP1E6NiImusDZZJMkctFeduqiDW8xCkl2CBolBayVnPPvA2Yj4Fjit4m4o2AnLSgDLCgJfShtlTA9_oPyO0njyz6d1FHilyz7Km5Dld_pIjTes0VmtuDHDawZ_O4ZPIO0KKOWwAX3jvg9P9oWbgDuD9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=t3Y-4YYc0Se3MqhmBYDvTnIwnsDcW0hgWDIRPOgDoI-804eZuY49YQgHDKA2hs8B0jpJ9fL9kmc8g034WGGAbYAlS9JPP3sVhraiAa4OTgP3E40jyXxbv2TVShaEgYJWcNAUpK5XUXk7i_26p2BUGYSrEz-28gG2a0N9Zu7iLyg_LIGjMpLeZM6itlwwHwpapFMvYMfqIWgCedmRolRaKuuT6rc6gZcTD5BWJmQcKxdUJkjPrUgB5Qd_Wk4TRGjbZmFz7hciU6olHpUuHsugLXFsf2g1zRensLPE6yRWdHB1hgkR_9sJXxIUR6MzFQ45tgGteiEdgTKvD8ANoH2gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=t3Y-4YYc0Se3MqhmBYDvTnIwnsDcW0hgWDIRPOgDoI-804eZuY49YQgHDKA2hs8B0jpJ9fL9kmc8g034WGGAbYAlS9JPP3sVhraiAa4OTgP3E40jyXxbv2TVShaEgYJWcNAUpK5XUXk7i_26p2BUGYSrEz-28gG2a0N9Zu7iLyg_LIGjMpLeZM6itlwwHwpapFMvYMfqIWgCedmRolRaKuuT6rc6gZcTD5BWJmQcKxdUJkjPrUgB5Qd_Wk4TRGjbZmFz7hciU6olHpUuHsugLXFsf2g1zRensLPE6yRWdHB1hgkR_9sJXxIUR6MzFQ45tgGteiEdgTKvD8ANoH2gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLGtnegb7-ipwG5gNon4js2U3Ku32NRjuZIfI7HWz0XgsEsmcxc2s-2RckNLPYWhKx4l65xdezqGY90peQ4pqZPI9nDJaDOrRIgsP63V18kvcbD5xJ05qW7HRcJHTDoc9j5bceuiYDWSks9h-D7uizPTswIuZHy_jzsR8MuGvS6MpofMo426Ed_P17dpqftaue8t4ZNvAUx8TsCR-eIwaACTJpOuJANyoPJpEXUkUHYW34tXRgNkFArGdbl5SqryVy2Hv28PUTw5sVovBHhN5D5zJthb3NT9CuKtLuJsttsXpJglHD_O0AH0y4FfN6TfkBbq3eVteVIhT0IFGDp5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=HDl_893gX6ekxX18anhuliWndCZbe12Hja8kDDK_Z9a72dxIWrPsmyGcIYxhkm2CwZyixN58qin7EnglJj5yTZTnQw-FbTK0qVO8035IBcPs1tAzl6EvA8HLtDEkpvpR8HQW4f_uYUKyohLB69lgsOTsd_DRKdkKapwkrsOv77vNDEqSgG22HdqtbofVbFTx-n2m9nZEwEc8OOLc2gQmNtifWWiyiKhNMr-Kb7HJEtc33bb2-rxu2_alyyeHDC96pU3z4VKR6kARS5YVlvT3Fn3HbNltdhir92w8MB68LI-nvue12Da7aFz9Cm53BSOeiY6odI22LlPBntoI6B8t0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=HDl_893gX6ekxX18anhuliWndCZbe12Hja8kDDK_Z9a72dxIWrPsmyGcIYxhkm2CwZyixN58qin7EnglJj5yTZTnQw-FbTK0qVO8035IBcPs1tAzl6EvA8HLtDEkpvpR8HQW4f_uYUKyohLB69lgsOTsd_DRKdkKapwkrsOv77vNDEqSgG22HdqtbofVbFTx-n2m9nZEwEc8OOLc2gQmNtifWWiyiKhNMr-Kb7HJEtc33bb2-rxu2_alyyeHDC96pU3z4VKR6kARS5YVlvT3Fn3HbNltdhir92w8MB68LI-nvue12Da7aFz9Cm53BSOeiY6odI22LlPBntoI6B8t0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb8Eh6KW_jMoF8BDnRE9weVDUWrNyJQNRWsQ8Ws7vQuN11t6ewbb9HcP4UoUiOO2qFkIeqh_-kLF6wLKwB9GQtn6OBXRfSJo0qkq4JGF_2binYwRaTWu6SqXxsTBIYQ2zJrZxg_gW5ute7L1VXTEDvP36Ub4E4PmD3B9lV571T1HyGpmRhje4hXiZrSQqgvEWdsVZ8lvrVeRzO0P58JYKnB9FG41eIaqK7aPudxXrOFKK9bXYrQB9ar8tbbL68BqbymAAGB11ICM0aX9a2iBWfmvLj5MgpT5ZObvKpFXggCCjHL0Kp8haje-dw1LGLdE0b3QaxDeL4ng-xbt3LpdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRoJ_G4eQBc3kz6sTe3FtWclqf9b7A_omFNHkBEW4zh0ppPMCf-DK7ObEk_pCMsMFHwaG3JXPJD9BuGT5lJBCLvdkTW1pdOVzwVmL--8MjUhUiXTuB7TgVUjCsdrrCYgyOzKd0GbB1F1JepgE-q80T-TgvGbl4AteWzOo_6ZZomPKRNTU1iCGujUtSVCGaXhEPq9ZAEDPrTgeaI6VX3DWLMFHcqZC8W9mHGcQEWrQQ9PtvM3PxCL-vk_8BmG2bqapwrYdtHfG9eu0g38FXzXCGroVJDdeT1WO2C7P-JbDmnYV3LxLoDc9kHXSN4wfFM89FqC56Xwm2Koq7VhSMDcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLHMKAPWgVBEumvOit-5YdhKdSBmnStmdw5X69K_gRFxW5Jge_UWnnnM_8ticPWHdI93BA8qc7fTEgpJ8K22hUJvD7NXAGfWYodAJWNjSbZbzRveavWFsWYnPB0nar5CP4NHuaIRerA5OGbteItftmcKoMDV7T6OeWtqvgO6lktwZ7RLUNggBjAf10HhWvhS93OPeVWhuNTvlPa-TfCtWvQWQdVj6CMFYjDt8lpgdNV_emheRikCFmKqrZ5tWDpIvceGeN6inYg602v95ZMeTb0OGrVdviWa9YgxIuFGIU22BBoPY-vpXgYw4Y1QQRIfPg4hZ12agMGlOm8T-34M9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1OdnEjjs_CeRoWK88JxvA2TqQqLL7jtUDh6wDXA0QpANyOja5yMCE6u8ARYiO1HcrkBH2DIuvrSXS5b5BA-b9_WbhHewYO5tn2XKTuxvYJB-85SMwbSKVV1nOHbWHMa4R39CiaAN2FRAfcotKBAYlQEQVTNYauR-GI0hDhz0CQU22fFSxhD7hLpyjWER1f1B51ACh3ROhU6TBhWVvSL41nxUg2UsZ3GQ7DT2-TSY9seAFJ-14K_Ip-bEn9MGSF__PbWzKTg0LOLb2GEAKj6OktBvzvC8StdFfvLdHh3sOoEnr_EtrJ0LouG3UJy6Hh8e44fQSjT8F4X3J5_STUg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhE1WtVcBwRPKF1oJP-Thq120nzNTxvpn8HbYQ_1H_CpOGs5NiKbGkTEP9fe_Oqzlf22kdrylR5sF_WMXeWGRVT3l3VOoHK5LLGn3MMORAY1xoA2GU0EvDY43-Rsukw67JCtX2_0bWDViOG1OlRMnwH0ar7fYPPCzaCLnr6PKMYUrxxoVqnBuJxsxO7OXv-Z3gzuE2cCcPT-s2t3Cp4pLl8ScvCgIey7rXsV9XRen9_FIc6soRe-nQeXtVenOc70AgFn8RpEHcoIfwCnUJboTduMZ7_4-oifEREDH2e62f-IVpLQnbV-I9SAO5l6_mTfi9Z2bhdlcs363kIWX0_GDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtFCmolxBqPCLJtFn1ZvVI8Dn4qD1u5ogo9iH9rNHCDqrOo8ilNHiSYbjiRyRsaf-paOvZTU9KWs30W4Pv5Zuc6F4nvaKv8WQjNQf2UBxde12Ynp9g8x7hGh8GOy-wSiWTYsHOaxp-cFq2I7QaNlk50zmJMcmts4X783T6ahxO1LPwXSghCYUJRHOeGL4NdDKpMJfRv8_hm-rkTmuX18moRWVNJkcnJPPiDmkoHrAzt8Z3zZLNu_xdfI2LY_qC5m-b-JDS6x5mgto_Y2qQ-cpawMpVJa1Yae2pEmBEov6c2lQeeaxDjoEFYTKglRpGVDO9zD0TDuZp7EdYCjaBoztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djrhefqugOxqMm8Ez8PxukvP5l-5F_0UA_pOvqpXoZVvPCQeA3jJ0xg14QXJ0eK86HggX-uWuiZPaHUwoEzcWWh7j8omC_Gqg1qhc_8HOVdtebq9NP6pAv9mc9ilYy3uilcIGJxOiPOpSpsoah0LJxOJokXIEXU0-B6BvjACfOUuSdisyl3BdtaRiYl1FqUNK820QCPaiOWRrafo4rEqbqB4toLudRKPQqgxvf4oaiRo_MeV1MlpvxJCJfZ0pPh6h62TAwaMNUvwzoMWC1s8-XwFrnSLakITQxrNroLfA8QiXg7iwKptB6Dlk52Y6O6V3WeIGiLifzsYSMWW-JHHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=FEiZeb5b1zH9BjjVUr-P8MhTQs-M87vsdj_hFhXKoGmvKIhgvji2cgNAVOjZs72vOOaMrFwPCnaJMP6YuR_k9aHe1bQtGCaN3z3_FCAQbwV2IHEFjv_-7SMH8fylZlvFRGAGa5QgcdO2EG_T-IfS2Hq5T5XKGUge-_wBHZIYP6NAzEK7W11lprvO2J7fBo2p3DLiCb9mUYJAAdOr5WQtjA26cI-B2nBDw8Oi1rqje9ZxseMomGNhadshxXbALkDzUH1IuPNgfVnSfMoQf3h9Sudgigj_QUcljTDTCNprVMgyFYOoaSrbk8fsXuo9HQ31TbK19tQ8RC0GA7um0cvgsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=FEiZeb5b1zH9BjjVUr-P8MhTQs-M87vsdj_hFhXKoGmvKIhgvji2cgNAVOjZs72vOOaMrFwPCnaJMP6YuR_k9aHe1bQtGCaN3z3_FCAQbwV2IHEFjv_-7SMH8fylZlvFRGAGa5QgcdO2EG_T-IfS2Hq5T5XKGUge-_wBHZIYP6NAzEK7W11lprvO2J7fBo2p3DLiCb9mUYJAAdOr5WQtjA26cI-B2nBDw8Oi1rqje9ZxseMomGNhadshxXbALkDzUH1IuPNgfVnSfMoQf3h9Sudgigj_QUcljTDTCNprVMgyFYOoaSrbk8fsXuo9HQ31TbK19tQ8RC0GA7um0cvgsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v12hgBRjoW0dR_eX-foyEi9-EVy5vrgNmqQPraLW0dsNizTWRIZjaW-nX8Dh6bnbyLOjcRcKFy2qE0nlX1Gz1rw783ipl-JofTrNevn9dlw9gqMrbSY4mQikb-dwlPlN0k_NIkAXmswR4EGMUdiKFNv3HgWmQDKqq9PZOKEKCyxHPqKwAcMdl1-o2FRh0yDMqy-CQnDjR2ZRfpgLsUygnM6FrYEqk5dvspOf3e0WJv8PTBRsQm8V7AosBxUqaUSMnzmq1GDlH_3oU9tcA0XTlzOzAlS68TDfNKHN-0uY7UuNMgn3lnoePi2EIAnhH_HpJxMX60ahB8AMb2W-Tm_t-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veb3VO0ziJ9FToFqNJjPKBsVN-Wzxn0gcR9muWNu8wOFBKEf6MLDG2R9MyQNvGlnre5rnecnS4LmjmTbWcTBv6cvW3jEAKRs973fW-0JUHYJC_yybW91voB8iweiJDmF42cPL6OJethy6fr-09bpTWEoyMIuR3A6mtCwrMAR1P-p_B2rA98btYYj4yCEPK75Tb46eNaeWXWsWpVKmgms8-uxysTBWiMHydu6lyFqn5AArUaZLd8TknbEq0r3DFNUzfSGollvBoM4aVOn9u_ibmIGHI1eX2gcdcT0wi254FKx4NJNXunSOAy1lfHJ7sV2e5XYWxBz739IIHC9BygEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1gm61naO4xrra9oN3AXTi-CUyjjiO8n60wgypn436CdjZD2s1tR0nVwbXryAOY5Z6AktQLbEuaclXZE3M-7in2kHdoyfwl6gZ2OBZUGlxKqFQO859QN5c7iSEhaMIGzw3NrMxFCAK7mKU_RtjQmZizJVivpikGOcaZh5norkremP0wZZ1j8AGKDVYybeXVmFtpKQUGNJVQOwSAr2P4MqsHBIQBrHDJgpFufrlZ39RLP6GvUZwGW6_4mMhKsVd7xiAS6zEaFkgNbYYyKnVYcuGbHzVWFRq3EBt5XLyYIFV31SWTnJx3S53xhJOELJlJy3wetFSeiJRUXkxCBNZ-U-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7eni8OQFUMfyi9fp3KdG5wn2RpvaSbR312aQmaH_fbqqN4vHYdkGmlc3oU2wukma-6nZ0KjOPexKHwB1aStwPWfig0jrHSKuDoHvSsECVczM3vgvP5skQTMtctj0hXD4UXjdatSy_GrWcC3OLMNf0GgQdJzLHF9LRvwlQ_dNrfXXA8y7A2-xRfifJjo-fb-qicUHtwQg_zn8vQJUx7wMrY1qbxyp3pfVn7IH8kelWEphOMvko84aXjPIVpr97JSD5TBtgrVNDHGwmw_rfmi20qxTKK9Qw01p3IRkNO4caUo8IryOZMX9fSZ8_8rGCkh2vKgbgsKIS908YeTsHEhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts8hdtnYZCWX9RBpFuSSrcwS1CFai_tAwmKQ-E1X4W0Q5pkyrZSZrm1azYuyi7-HHlOkJFOfRyFe7fGlwRg3XtBDKx4p3QFjuCl7O9hfFcle2Xj50XCJqWQoFbzr4HvCiAFUEN7-Pdmg6urrz6Qrs2b8RbPQCc57Wf9xhVObR4ZMOu8GMBJZS5ExbOoYWlp9SF4SHgNiBNful2G0DE-Dt4g8sEQ5s1ddHzdiCCSZYhm4tLaJjt3076VhhM1qG8b_hzJaub-wC0ykB6QkOYFMrPHkVtj2po7g8LeHuBNQBQw0n27BYx6OTVeX9HSTYOLvxz44t-fduY0wI6Ixd8sSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMlFGF0vN07095PPf9HH1LOCuEO84oUj0q15UnwcBjfepnQ7B42k1H6RLL3UQ5SFIvS0tLFS5XJDvz6xw9lIqYwKVYn6tw9fj56VXZghTPQPlSS-r5nA48AomcqQqSXdbS-ZbSRwtCc3-x0RvHTFTQjbKTj8K1uAgtc5XqOiPZFP0ttzh7dH-nK15It0AgZ6fPjYc6SyZKeFmrGNSNEXRJ0eKzXpqbzDUR73ATRsQewyNGtCImjbqugn0SxKdDZqbADFi8oaFfrUc5bxlqHhVWepTeK1gUcxrfv605nvTYAHiD6VwVoZ8imQc3d7Da91qhaZeoHttCfS2FMKj5pdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2FfoIdoQB0BtPZ-diC610S-hVChed5ore66x9FOwa1y_6zrfNdyy4sT2NGfjPF4hSvr469i0iGy79T0U2ttUecVoDYSjArMpiHhtjg70kizk9q6tyR0nmNJHw3jgRy1voLna9E7zSotnlWTQCcdDBJkf9nVayIl5F0PeEdcpLD2apDDNw6d_xUqMaoZFRtlzctUo65imYTgQbs13HRArVCXn2mudBA7akYo0SKhR6REa48KUiAJdh9IMedLcMeAhI5iVg84E2JkA47NUNmSUtd0OfhQV9zTm4mIUFY3cOJPuTdFnGuowpapmoXvQXw4hXMNIZWZGH-7whZPPhNd1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpuVI_9_-kkaIWtDXXID7HIyshMmjO2-W-ej8gpoDfh-49lB2iXof5YMSH5qy1ybhK9F7ssf_FGG5cSpEcslengnWywrGEXAF3v2KWEDYC0zY26hPVv0LLzpSmUoDKKKVTT3D5NKU2DELffnbbFTBdJvKCFH3QHDeSl91XyUmBFGs767wqxS03gMpGkT1wI0amL3hZ_aK9wAQCP4T3TWw023ApKS7t8wXWkohq-dE20WGf0aifD31k2WELDZo7A_Z3K4F7sSZZISd_knBskt9KZNXMIdUatc8MhikO_idisDyt6KmvXo3yDQIwBkXBC698Vy7nZdWMI1zPTVzDNh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXKLDo8V7OlFaOpvwktcaO6prE9GlYlz-gz7ZCjSzBwaVDzNRN4Lzpwqjh_ZVCyZLefOO6F9_iLbfyno1FhHxz2JegN6ok1_n_cdVLdxL5hv80dE6paDB2IfGqQnN2hgDt9rkRqTSiT3FuIyRZBWftVFqlmALUfXV8wPa_4S5-Os55SybNIyVdAXIU7WTZBXgRQ4-XnHXw1ZcFRbFdorWOjIVgLhgwle0047AIm2T62wGsI4S_JjM4UkgBhyHSnPpnTCbLmrAdn0xMhD1KlK45y8kGWpy47npiidTc8TncO895V5zEPGEHoaqVx2PZjwSeA6o9XMqyqxaUxD4Hj3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGUqR4IDgiYpD4h3FtsATzLYsgfoXf8Pq07UBYvgzb1Sj3PjqCoY24EQjXD9uWe3XjPjPkvM_8pLUSEMSSLBAkJQ9uvTGb2kI4x4T601ASTBFH9-kE05yezMKjPMk0AGJkF02l02CV5jEtP-tWzmyKVcKGKGNPme-JEYTUZYqtkS2j2iwR0DUYRN87_0sBuvi43PmOgxDXL9fLB1OWeKbnB-MQqKm0QvSpyS8bot2ubF8oreu6mk4nZxWDJSONY2MX3tbUh0oJwktjke3laUkdyJNpR5uJMuq6n4WUyvHj0BEk6EnW2DEmELacM6Wh4PC36Y4T1s35eui309aGtHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t86qSBFaLWNG4jZoov6qxyHNuy3U3vZ3-ucP-EPEem5buRidoj-9DIPa_EWsdJk28ksV10jt5jAsUrUOkdP3AhSFLVOrJLzdoqQvyAbFzKWSwIpS80VuPwGsesntAw3iZOSEYqCoWXVgwlAkxTtViroyNKAGwWpbWQUjSaaE_MIGniPAH-MmxI5QoqGx-K07LZz8XGqvDMHxmb7VbBIDkjk373wAtz5QQyGIhYGGxQlxy_RRKbQOxSIV3CW2iZEY3WKha_RJIJt143FVsXcKHPRJKGQq9vQqtXmcf-Bu_0WILXB1jaDRy05koXLQv3WXex1WK4vmYFKDuyHuOgxynJNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t86qSBFaLWNG4jZoov6qxyHNuy3U3vZ3-ucP-EPEem5buRidoj-9DIPa_EWsdJk28ksV10jt5jAsUrUOkdP3AhSFLVOrJLzdoqQvyAbFzKWSwIpS80VuPwGsesntAw3iZOSEYqCoWXVgwlAkxTtViroyNKAGwWpbWQUjSaaE_MIGniPAH-MmxI5QoqGx-K07LZz8XGqvDMHxmb7VbBIDkjk373wAtz5QQyGIhYGGxQlxy_RRKbQOxSIV3CW2iZEY3WKha_RJIJt143FVsXcKHPRJKGQq9vQqtXmcf-Bu_0WILXB1jaDRy05koXLQv3WXex1WK4vmYFKDuyHuOgxynJNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMof62worl4Ch3HPvDgwnEHY1xut1mBb41wiRi4hR6-pQYce5YD46iabEjX6k_10a-fsonYsXw7V7AqzUV_EDSJgxwpbqPh68yRufaHUaP51F8n7rX_tPQgmq_YWwW-CZsLJrijZUAFNVGkWN4OhMYxalp1ZF7wdIa52kwBme0WiTLtJBQXAl118xHnEkN5WV06XbVxfUmEK6X5_DGLg1daSdaP5k5Zt2zuUcxNkHQe8beCezBhy4KUBG339DosDc26Du3uj1tBxtq1NS-STfdFsPwz4i2tiJQmXv3bxssyVVB0EeIzsfV8OmfqByHT00rQwPMl1AJC7hPr9c-fITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMEtUEbxyi2xeoD_duqY8_99crhfmVaK39BEKbf4D5HBRDdEczmmooUEBAccyq6LmSFiTJimimpX1mQ5uHF3njhtKCqyN6Fjvzgv2V_7D9L-PY6f1jJWe4fjerezFUk-O8fDWNcQrRkn7I6-SQrXAqAoViYshnJHG6jPXrseDNpVFM3C40LETwJL27Fn_aZ4JkO7X1_-ehuvXpELlnsm7IPytdFD4YuKgI5jYp4Wg2VUrqR-9Bk5KTHAmmJL_urwEM3ecitPmEtFeWXXmAIJ98oRwNCleWFeMUak5PSqj2Wwus7k8BYvYMyoMTjayVFumTgQ2QLESbQDRacqyDyiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujJuRJgpID-OZpcAENnxUDXu1ObnZx5Ogqfd7b-sa-MJ1-M4z3qUWiFj-ljKfclXK4CabtBS0dOpUCxyMruUs4DeeKGocH-fBpg9-c-JAoh3DbXxbUWI0eQSgh3RU7pgyK6ZQnB2ezBlum3kaTyYyrK7lk4tyz-FhEMUgzh6Kfz5y5aKnxq0zpRPh-v-qVVGJRbQCrrsJIEkTvefZhpu0VDHXH0XzOt8I45O9iYC9RPvLR2ZsEg6VRW1PPhcb4G63SDTmqppE4gJKgUG8rFiYhB1oPCMwKHAWdxG4MfU_Z029r4qnoOZkr2XEgQpnNVDKjTIwcR7ev7q4yWUr8L6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be_Kaz4nURz-fzwqErtMpEJ3oXK5Zj4JkNkRlOhU4-4dDbLK4ZEXE61lOdoBpE-Ir4r4Kt3LEP3aVt0zpzyro9lsxzNOl_57gdNrEQTivuv7ZLoaR_7rfbNr4g5mLmjAMGBliHvUD6OU9QUU6xP9ZVWSqBx9p2PpApXFl3FKvbKHw7vrSq1Kavqi06iqEqjy9ZQxSKTpseulbK2JQBw6GQWzy_BqH1d9ImKRiJoPY6Kb3kYLht2GeP3gxbtsdbIWnBJdIgfLX_d60gvMt13lQ4WTmeG9s5xpZ6lAVVxA-S5x5vvwNLqs1x5aJjS6iLbyfl19AfK3-VMBYJX8QIHrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9_GdpIiO177NdBc_qV81pd8vYHfB10koVMy50T5Tas7JRcKiD8Ynfb1c2CUpPOoRJ46fphYvPFWQQvtev_7TdoTe66Kg85CTKgbuXDeoxECJtdvbundjC--Omk0dCqG85VCc3k5oNjrcSKm8U9_K6N-ftRv6OJKkfdv7hkB9KLfZN78mgSTiA4DvmhnlbagwfAPTldLrLF27RXyJqg7ntFVlX3WohpD4tqaZowLSnPZ_L1vAdWUVH_-ZkRom0zioYg84Jxo5d0xIlcA5ISX-gJQi9B12camz2hmbw5e6NdDIl2_mNJScgyAZ4ObVjeN_3hTJZUVxHL3Rlm39YFVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2u8vVPQnN_nCLSZON36DnoeUDsjix7NrFvFHfi-_hIF5kOhWaYPAc3dEcUFmk0cmMMSpk999HFbKBy8D9UfDgeWdo8WOavFsQZJARZBJLjZW_nQn4YqMEcYfyDOtWMvT_YsM-vic-2DyhCM9yO9lrKDC0TTAzjoZ2kFZxUZ0dNGWjVINmpo0Q_XDnRgXICkw2GybEasp8E1z3AV6n9An78lISQC7Gd-9ciGiGK9QC1J91_Q--tm0Kw2dI62ARTni8h5_jDxO_2wbIxGEyFbTk8k4JQOKSa7iX_Ijf83puFxt7fEG30559hGEIpXxiRqT_E3VSyQgOEglYf2IwxnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0iYfBH0mCoqwQHo0GPFMda_ZMUM21cW8QyxPt4RbBEhbhUl4tfsuJHL05EqezZT0lXnd8ZsEJRsYDt06x0sjMAvd_9Ssa7y-Otyi1XtcJA0X5o4Dl0lmfOFLVDuhCM6KBjxAmz8Ol_2_9YVFGgSRV8jt_CafW56yGBfpPcshDI_cRuIAz8y9shkw6-XRvA1mSm6RKACuumuLhkHjYBgiOiJvfLNMySSvx_sKcjSkmz4nhzeo2debE7F7uVmnmp5LFr0tmgghWR56fNFFzF_9Yr7xgAuKesEVv5JfdRERgbjGmnrluo3jJX37I4tRvTr0IfmUNhHUjW8R61eC0uciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsdFBBgE-oHjdir6O7fUxm7M2_Zkq-7TVdoM2JAkIVDc1YNEs6QpOHoU0k_FjNoYvfHcT0-l0SAc8GUIv2lifNLS2Rl5DJHpgDaO2voTAA5aE9ndkTfQZPWeRQXpcTb87nTVlf01MmhnvZ-SMlHoWaQdQyxrz2C7FRInWziMvhaJPrdSSWeGMd61Yyr3SbcuoAFNCsxyKMmKj_ivLTlrasON06zsPCckgRou4xW4fAE3iA-CjH_EI7UcxeFK2sYWhpfYYQgpsE9ydWKgPA7LZpQeXh8KZsRqrtjwEZhsd6Jb0_Bgty_PGM4XntpjlE17bn_7CaKdoK0bEbQ2qysUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuZ5j0swRs0XyJPYyFSuNDWvPAyegibglDeAPH3-5_TMK-dwhjnoS14SvdotktnxTyvKDSf8NFaXr0UDxg7_agY8DZxLp6fMx3B2va5Ja8EjMqm1LsoXZsNHtABRn15KY7q3-U1KCowgQ3-bHGEV0-BkF6Sn8NqVregHNYpcExIWfwZVgloQDiy_PdFG5tpgZfR_4RoCq-UBRv2vur3u9TxC75a8d8ZZ6sopLc1RxbbxkKnbHgw4Qi3YivtJf1tUN9-PwaCYX5k-KhluW6CgNVq1sHiXPUuPQqfcg6QpCvN3BbpNx8fEqVpBPg2jdRwF3h7x42ZP7su9uu-wmFPoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSjgligU-l4eHdb2j3wvcDbI5PvA45Tsb3aNBpUTQ11mXwm6MSEGlCwaMvOa_r-de4rZPrUJJmRjooJ48cxqc_2SFnzm2t4xW65j33zHPZgvkiPNkjj5Uy66-b5Nb6JeVUjGrnyGSeP-8iu7IOWijEz7MWCacu0wHNwmU0fSDmiDonGf_LYip4YSG-2ToE3JXCsouehHavIbU_t5dQLV6kzpPJho9dSyYSIWo16kiKR0WwABvIglI8XudLYHzGdTSf3LYqxl6CfAqJvQCiYkmVLSAKxHeqAu8b2qDikTYlUl49CGZZMQuIVp6Bf8Qa28hj1dFBCxe7N_cBxtnH38GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6R0Y6M_MWcXa7DNbI_PXp_VKY3PUi6tqMK3ZDq_47uaDxc09FZqJP4iFhkRo7a587JFZnBnH41BzwIi9m858HoQeGT-P1RG3AXaCqwV15fAcCUEk998p3styOOoohfiZNitUptiuaV9S8apB5UdjlErGiJT-Q5whD_3J9EvTeUcr7XEPv_PFgJXT17fJS4-OrNwrTKRiGuBDrvVrhZbeyaZvwB3FxgypkNcwy7xod58CWMAhSOT2Bv9MqUkoFDsIZGIh0Asf_WPRXeTRNJD8DOCCbZ3q-9P7fBqIuv_17nkqjs0TNVuqkW1AP43SosdKNIQ-xFI_Bo4_aTOaTBhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=cRVupk5mhQXGSb7Hufnm6OY0VYqYw6S5bJNfC5B52U2CkkpBEogm9KTvYG7oehMTVprrIQGZNn72wA_Onmp7yMtDX1XW7Ewjd2CED8RZYwt6vCLnw5IEWKotfrj8fxzA_nRU3Y48ZEe2Ip_6fOrVPVrxpmP_vbc-6wGSIDMr_HPCZHCalkKFcCXBiPzuYNqzItW7G0HoWz-64RRQwu1xve_IIQLhS65gr8uc5sCPEqITmVKEc8cYrRx6kyYF3ol2wsVF9q-USL037ScxzrZotntu5sFGPEHNPukEZMO3V4MXvmZmTCucR1GSfy6lWkyoHlwTpJwD9M-VpCS_l8DKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=cRVupk5mhQXGSb7Hufnm6OY0VYqYw6S5bJNfC5B52U2CkkpBEogm9KTvYG7oehMTVprrIQGZNn72wA_Onmp7yMtDX1XW7Ewjd2CED8RZYwt6vCLnw5IEWKotfrj8fxzA_nRU3Y48ZEe2Ip_6fOrVPVrxpmP_vbc-6wGSIDMr_HPCZHCalkKFcCXBiPzuYNqzItW7G0HoWz-64RRQwu1xve_IIQLhS65gr8uc5sCPEqITmVKEc8cYrRx6kyYF3ol2wsVF9q-USL037ScxzrZotntu5sFGPEHNPukEZMO3V4MXvmZmTCucR1GSfy6lWkyoHlwTpJwD9M-VpCS_l8DKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKEty3w1s2yIOneuAFZ_82qLKeiWMmdzKIyzJwjb5P82AXzuYKOHxINSE6DtN10Dq8M7VyOZchIkGSziRfsbc-gZd9mNo0x4smdA0_XdoM07-HCuzALjOOiNKwUUmyfETLK1Rcpz-cczQnrAByAWfyJnzhonJfpnDEDx8f-tIcw1i_E5V9fk5bYNMAIF8bbqyMuvtVB-lqJfYpP5SS_WJk23mKtBcYo0KUFg15MaJG8qx37NXkeINCBsMQaYgeIL0l4J7Pqq0EQBE7S-6Ruau-Q0oxqRRmdeHUqxnENm931W2TWULQ7M9EFtM8X1Z7mP8WGyR19PFFFLsU9I_PrW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN-UI4OlpJTH0aPMWSUrPrtHEFMKZ31DQ5eQ5yV_a-fV14vJx0drnIvgbLREhVI07TRIEypyZHJJC5lEUDWgL_Zt8BWzL3e3I0o6YeloURR5gpw0mrbpXkuB7heFLElExSyMqCjKJ-g9ym5VdPAdI_0Vy0IRnkLoplVApPN5xcsmUIqPEvEDNozmCH2X7JvaCmPSn3bbKw1K2dD_p680ixt8U5ua0mKSZQ5lQ2nSjb1pHZd7cmjNr6DL0Aaoe5DohPCSCSihvCzObOeRE4uSia-1rpN0v-fPPx_252x-sJSfUeusIuhmN-El2QCMbjP8MflhSmECrcqyFntRcCOOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRhXJ8suRfROYN2-k-9uh6meC69lnaB4SKIP3AzFqwzpvllHz3OLTREcnPnZvEqnQKzrRI0cMawGP388M8-1hUDKGHqQ75zkDkpLLN7bA5Aq1tflyFg-Ndyq9sD4TwbgZZS-eFyJGaCllYl7crDc8VlM8CDl7sbH14_nrRd9iYo3xJ1zHSYBICM2zIEgmy8txujzJVXa9hV3sBRVmC1HFC9pUD_EQAzBueUo8ail71AcYxZveLZ1-46-FD0MpwQ9p4g6FibrJ2IanB1_-6ZsGwZb_ZE6PWpBYEzWGr875mZYlgZEsgXmhdoOk99la07zH_Mb-44QgUpPGfLJvT_Xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=h8kM6zEpXAjAb31tsmoxCKQ_wNFeSsELJFNOXeLWuyGLFPmzsoc00L6kqZkjDQntGZv0v8lhje8_W53lJujRs8bVLUV-InCEiGkebQLOLGxiRIR_mGUmpKrh9ywkcgE3w-Q_6FxT6VAWmO8YeWiFbE2L58lJdDZjYo8PIgka83Q-mdgiS_ApN322WYb-7iS7nW5qCAUwpgEnQrlGHZ9NdjelJHGNSiTOehTIma0cc-ABrmQdzE7OH1R4BeQsWknuBtuiuxrf-slHtipth91twqYINRhq5cc2Nu7cyLtxg_Iee9mg22XPzinlYeezL-Cn4RAxah8DVR2C-Pig9J_yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=h8kM6zEpXAjAb31tsmoxCKQ_wNFeSsELJFNOXeLWuyGLFPmzsoc00L6kqZkjDQntGZv0v8lhje8_W53lJujRs8bVLUV-InCEiGkebQLOLGxiRIR_mGUmpKrh9ywkcgE3w-Q_6FxT6VAWmO8YeWiFbE2L58lJdDZjYo8PIgka83Q-mdgiS_ApN322WYb-7iS7nW5qCAUwpgEnQrlGHZ9NdjelJHGNSiTOehTIma0cc-ABrmQdzE7OH1R4BeQsWknuBtuiuxrf-slHtipth91twqYINRhq5cc2Nu7cyLtxg_Iee9mg22XPzinlYeezL-Cn4RAxah8DVR2C-Pig9J_yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_ROrt-SHX3KBB-bvtABzoilxrFTr-FHLI9OSkh7MZjxVsg7SwxHvo2yg7wGjsnR3tJYfW1j55Qlgiq7E74DcybBumds4Pkp1OW2soGj1yB7T0sRKOvZdXnP7iniLNusXABmdz3WjPkvOoc-kCkFOf6MVVYf4Ni8HavINp3Kg7Ewhn4xpGTx-EydSY0PWQlmTlDd3RnEVXpeiXbC90CtTaWd0pfLd1YvZlGIC_mmffP2_9efgypr8Rk-qZOKQAxGpPLY64TQ1G_tzWhLPxEuK-OAhS5y4Cm4EPK0UJ5DVtL0L8J0RkCp3NlAFxlZFLUJZQAt8nMDkPswhrgJUCQEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgbgyj5B3kY-1X6wYRmxaqp5ZBqBUH4wznzf-601p1aMRdgkKJPAdPs1mv2Oy7ZstwoDYID_NmmS2zdMWBv9X-5Lc1kWrxLB2WVjyw5qHp6vqYcpkupSmexlaqCkmKjSnxKeaMJL7wJ1XVAl5D6uwq7fJz2pBJ7bhNkGoc57Tiia6GIgRce-UeZpk1cHT_tF1BOWx3JTD_poV-AyO3jYeZvbDjovwSTmzRnsEIT04O6LQ2Upl4eVcT6KUCtlQEan5eYVxoD6Ce3elxwbEu-QUqdWH1E5n2iA3D6o24uxQacffNRunSp_48_sIkea_kV1yDA8Ut78Tq4fqDhofjR0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np47xsubcjz0Edlwbw7AtulTL-afH4g7KP_U4nmFzhKnO_6TuyV7okYQ__rpkdoV3dnuLEPRsavuksILiHs1aVWxXU3oV3lOJZN4R9o0vlcrsQc2RD30WGnoC87DVh0dqNHxJeXA7IxWKvDKQB2xn5gkTTGLjElQvrONdz-OYKKEpWoJb2QceZuat2f1eHbzps59pb-U_ZHFkjj3iKmzWkuN5Xz_h6Jsm7-ai4x2rFwJ0wdvBIuQngThb1e5kYHVH3gs2OkUL2jHpSexmbs7AY_dTumPxFS0L7rnls9yd4M-1Sh2jOkv0B30op1FUIUU6YtSWOl1Z2pLsH6oLw7ozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=ADrlq_bm5zd-DBMOfHGOGCTR2YyEDz8a1ROLibQs_-XaRbvXO3shw8ZUnePVwOlHpN2rYyBEMsHlYd7cFWi313WPEImJ-7LMpM93Zcd2e1Bnhi-ByUvYcIo0bihi4IeORUgH8YWiBb0wj_4uvlFhv-E8h4xzBxy0yK-IfToAt6ZCbjrh-7iBAJV8ogjPS8JI-hwjDy-W93VqEemgwHUzuk8ejZZcfvU9vPeH4ZstH6XGaKKfc6CVgmMLUtYAhGp1MzjgzFdcsRJgPQDKCuNk384Ev0YYMm_-8zd6MQFHL3a84VG3sIXMQL5pp1H-6tLifxJpJ3uV4vfzCvVE4izMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=ADrlq_bm5zd-DBMOfHGOGCTR2YyEDz8a1ROLibQs_-XaRbvXO3shw8ZUnePVwOlHpN2rYyBEMsHlYd7cFWi313WPEImJ-7LMpM93Zcd2e1Bnhi-ByUvYcIo0bihi4IeORUgH8YWiBb0wj_4uvlFhv-E8h4xzBxy0yK-IfToAt6ZCbjrh-7iBAJV8ogjPS8JI-hwjDy-W93VqEemgwHUzuk8ejZZcfvU9vPeH4ZstH6XGaKKfc6CVgmMLUtYAhGp1MzjgzFdcsRJgPQDKCuNk384Ev0YYMm_-8zd6MQFHL3a84VG3sIXMQL5pp1H-6tLifxJpJ3uV4vfzCvVE4izMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-9nRx5uGjLWarVrsiv-AKBFaOjKCVSrTVdEdL6ajV73YC4el-N8ksiDop6mqppHVNtBkKWZBVH9dWhYvJBOORcblURcnAAAfF1khe1LoukgzkVngVkc8GVbULCJRrVLGR_RiWrBJRVnjWTaws0UwjmvoCBGKIbdqRbjLaMI4bhwzOKHAB_GSotDo9rToveLT7RDyHAhsX2F6BNTMWJD_A_oPUonSCjxDX1R1CwucRZ4S9lpJ7CTrNqbtbqsUiZbqdYcsRTrIPNXiPZvhtOaqQiuvUzeTZ1bUVkz-tY0XOG-FL3gdxLore7uvP2nNY5812_4V_tv3i2VkSIPyJLzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=mhCdA4lc6c5IsLr49rrD94Fs4nah-LrNlAWZ7YVrlzkx1VNZLkbVbGD9LFOScF0W10T_0WgshlyV-5HexENASUagW2G33boLN4_3SHtig1lehzoRz65D-xMQU5zKX4jXS52RGbiUOHZiU8z8TGnnkY4v5-4yxyJECMMEOlRKUmkPVzppCu3OJ45EJY0zwIOdgN_lRjjhVgfNkMNqEBHPynp3RZWOeo9T0_AtY0gDvkKZxkUuQajP8CP3BV8FRJj4J39ZFixcQG6xStg-vaWUsD7KIu5O7zEw9Kr-hyqWDqBNGPlwO_69m_24pzWNGz6DfB5nfA1GcPPWdLtHHj9i4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=mhCdA4lc6c5IsLr49rrD94Fs4nah-LrNlAWZ7YVrlzkx1VNZLkbVbGD9LFOScF0W10T_0WgshlyV-5HexENASUagW2G33boLN4_3SHtig1lehzoRz65D-xMQU5zKX4jXS52RGbiUOHZiU8z8TGnnkY4v5-4yxyJECMMEOlRKUmkPVzppCu3OJ45EJY0zwIOdgN_lRjjhVgfNkMNqEBHPynp3RZWOeo9T0_AtY0gDvkKZxkUuQajP8CP3BV8FRJj4J39ZFixcQG6xStg-vaWUsD7KIu5O7zEw9Kr-hyqWDqBNGPlwO_69m_24pzWNGz6DfB5nfA1GcPPWdLtHHj9i4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQviP83RVZjcJ7R_U7PDZmgJxsoz7HV3uCtZf2WuAnYgUOruiSXjRUkhwZmt9DyX8zMvOb0K0oAwwdngzVFSck1_9dblWEmnQOSAxRhM4GZGL66sz1vvMZknW8E9u0C1cr3RtYJbkiUs2X26q3_VpLeHSKNOQie2uyOB7rD-tmZ-z1mcUAgn3SdglXEYDOY2XwmOW1QkqX8efT6WdcLIP84VeSaB6wnBDNrnKKZz01Y75X4XJmuEQgv0PgTDFwJ3nmKIhOL7BbY5YhvYqUELoGl8yvDrqpR5cBAnEAJTfEmlpuEtBH0NPFrd4V2KxmzabmR7z6h_WmPjBtnM-1yjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQVBPvx4bzT3kaBkT-SzB1Dy7zso6fn3QxnFV8ipoSdWl_X9T3zMsjrGkfKIlcNDTGGvb3WdMblTMmjal0chYu4SEJPTvMKxwAU6oxGCIegiPeFbBYmXGigJBEIGE6XbNSn89Fd-45Fg3xWxB9ZhnhiZS40jF0VXRxm0oC2paTk_rfg02M86wo3QYxkPvY6-deARMVv8lq4frP5-6ovGfxBXaq7bccnSycaL8q6uWp38lg1FudXlAXWySZ-vUYpPOJXNxrGyShK4c7MLqZqMf8bwAkvtdb0-cSJk63xtC2OmmZCrV0rfSAY9vgrBy9JlCMh9gDTlmCTEkdLT4b4slQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=jZh88b0kz96r1TbMVbcG67-Omo0sE4YUaV7kqntZC0aTSxV4woIWpsdXNm7P1c_fCnO6fqg41R1tJa50AtF4l6cx5MfRpBZtX9DnIRU_hCV9EuCKLrizb7PYoYHAjSEzwWUiSahxc22U_fiHTpYHXWQwPJZieWzydyV-Z_LJgpJe1RWGbt---Ma9YBjwzKAeotr9hMGBbgJC65_MGq0ufZpIBHR2ZWnY_bB0FbRI6xf_t3doxCwAVZ6Y4U248rAepHJPAhFiEhzzRWuJL8evKx1DN3o3ZJD1LXAeK9U0TbA-vtXnNmhstMmXcAgVtIUUmLzYp4WcNGLXQfrQNgIDow-RwssqqoWUPWhDnua4b-zHJsZ3sjCCRdFUTbe6EfuWdETTupckbpa2Ee1Va-1cDE0w2LHendwmV05aNk1bPHCcjaW3D6bC_rGcYWJn27ebyyiscDu7nKW7NmbEqSbzrU1D7SzPHmVlnYHw9pLpDBPcwzd4wLWqqHoVL8daPkCAetUAD70z0YL3gkNBU7s0YLn0kZrHpmrmVjiWXPIgWaMAR2KaFkePuqAB8E2SaP5m0gRzQaTVgRyfniSc0d8c-o-K2n6YVO2ZkZZQQC8UkcqSZrMQVPHgEzg_8LI3_AddAZ0Lsp4btY9g_QNQoVPdpsV0CBJ2cyKCHK1gAnbX6D8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=jZh88b0kz96r1TbMVbcG67-Omo0sE4YUaV7kqntZC0aTSxV4woIWpsdXNm7P1c_fCnO6fqg41R1tJa50AtF4l6cx5MfRpBZtX9DnIRU_hCV9EuCKLrizb7PYoYHAjSEzwWUiSahxc22U_fiHTpYHXWQwPJZieWzydyV-Z_LJgpJe1RWGbt---Ma9YBjwzKAeotr9hMGBbgJC65_MGq0ufZpIBHR2ZWnY_bB0FbRI6xf_t3doxCwAVZ6Y4U248rAepHJPAhFiEhzzRWuJL8evKx1DN3o3ZJD1LXAeK9U0TbA-vtXnNmhstMmXcAgVtIUUmLzYp4WcNGLXQfrQNgIDow-RwssqqoWUPWhDnua4b-zHJsZ3sjCCRdFUTbe6EfuWdETTupckbpa2Ee1Va-1cDE0w2LHendwmV05aNk1bPHCcjaW3D6bC_rGcYWJn27ebyyiscDu7nKW7NmbEqSbzrU1D7SzPHmVlnYHw9pLpDBPcwzd4wLWqqHoVL8daPkCAetUAD70z0YL3gkNBU7s0YLn0kZrHpmrmVjiWXPIgWaMAR2KaFkePuqAB8E2SaP5m0gRzQaTVgRyfniSc0d8c-o-K2n6YVO2ZkZZQQC8UkcqSZrMQVPHgEzg_8LI3_AddAZ0Lsp4btY9g_QNQoVPdpsV0CBJ2cyKCHK1gAnbX6D8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Zu0AlNgblHo-RHI0TY9HT4Bej0By25WA91TLNbn78FzmHkKIhJyyWl9AeoieO4i9MqAm1x9rkShg8qmi4ldoihi-zWD8HB1K8KcsgIH61fe5pT1VEJL4uH49C8ErKN5tTDva_IPgS-9H5HPWLHbi77-glQ8VCA8NIL1_-RpCv1iQ2z84FKAsI9yG6808Uh4S1ZBJEa8WMMxFFQGdWJlkGI8vp6PlkfeK8wvgqeW1B0so-A0SOqmcHw8OotUJOU3xCST6sKueGLlJ5zLpqDRoRVNzmOKcJQSN3NAwLMzsGXfBIRlh8sIWYapaS07XvDBj-lX83_R0YFm_4Nxj12mB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Zu0AlNgblHo-RHI0TY9HT4Bej0By25WA91TLNbn78FzmHkKIhJyyWl9AeoieO4i9MqAm1x9rkShg8qmi4ldoihi-zWD8HB1K8KcsgIH61fe5pT1VEJL4uH49C8ErKN5tTDva_IPgS-9H5HPWLHbi77-glQ8VCA8NIL1_-RpCv1iQ2z84FKAsI9yG6808Uh4S1ZBJEa8WMMxFFQGdWJlkGI8vp6PlkfeK8wvgqeW1B0so-A0SOqmcHw8OotUJOU3xCST6sKueGLlJ5zLpqDRoRVNzmOKcJQSN3NAwLMzsGXfBIRlh8sIWYapaS07XvDBj-lX83_R0YFm_4Nxj12mB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXLqs4EY0iKw38EsKBIuA76qFSjHL8yXKMlv5MWv4kc2gIf8cy7Hbc937jVmT6YipH7020RAjdGQn45b4KyGuI7VqD2rcvi_8T_S9nPvL3DtqCEGEysvzDBjQ2rRvFS0j-5bhh57nOXqXMGR_dRmEBxRi_8qp5dZjfgcKInx57P1Bhf7bzAsEdBy82yhvg5UTAADKVjVYOgBHSCMynqxvWel4ya-RsPbGEv2viHNoGbM9gsaI-9SHft1o7qIUuFGQ3Sam-6fpIc3nFV5cSx0hXXQ0B0TZW4Oo8xeceKvUu730V-F-mOomuHYoIOZ9RXU4yR_fp6KYWAhInzoaL0ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZXdUjwoGrLagoG65iiL5Zen7fhB8TTMO7Rc3FkYYd-PBqX8oqLZKtsA4fVCHQjgpNgpldMJp5rrX1EgY4QAXqnxTyIFE3ybUO9Tr9pZyPpzU6DkL-D-exJeUpbh7vExA-t3bUYs_8D82YHF4E45Ov_pj_CaanO-UGFMggOfZGW6cF5wSnBZj-GWm8iJLXpYJfFRpQm-74YjwUJzB8ZFLVcP2_LOh9qS6QXgtbgUdBXolKBF2HLU3YLEpCuKcIIsr25roG-2-mEk_mC2-SyqtI1sw1swKAJsuNs-8xgx48XcNjFt3gdJQXU-j74eyxurtvXTwEJqdG9H5WEnC6oHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFSP3qNYtH_Rrm09tvw6-igUN8sFfePoFHJ16NcHMGOs2H79E5tb-ZM65Ln94q8pmWtxUtJnFDIUKGQejd9c0RK8nDcW59wRGH8Zrwa4YnnVAFBGdkAv_M8xHWGMqSNdS6izxIvLXN0WWybapUExvt89-Atgn4MXZ7h1MgozU7qE_Qf3UkcfTJRQ1pC9uz7LaNX1SGx1qZrkfP1PyhcH3neMxpfPaI33_P3OMx13Xv7ohnI5jiAxEH4Ln7uf6njBmND8uWU4UZh5sRmPWxGYDvTT4RMvyFGXY5xR_IKpZgD8lk3xxHb5_xYOFyPnTsR7Zl1rqJ0asM0NmUbGfJA8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlA5_qVhVlb7BEAThL4J5DToEj1vC_mbYiIgfrwPoQM1UEWaW0lePYlDeBZLxq2czkrVMwMG4viUzT5ZPJ5kenevMRPBSqUPRp0rOWmkmcdyQzY9a-ALSstKlZyo2twqoFtFkgiuDhMdR_UqFx3bYuZucWNoct0Y66HlWoD__4tQPeCJoxxTQ1vvty0opMB6jBGcTcZWRyGw2rFegOu8sDqR6aNA3CMMAPQE1epuTOW7cycM04HzCnVif_tgVegUkyIk14utBkK90bmCqTl8sk_nDObFqUBfhPSwjkwnTclqmUIW5sgA6DimnGioyevGzLHODEOpoN-q1Bwu4tNjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUGmBZurJpEOCYy2JMw2aPiJpJOhSzFbKsu7KgYfzu829Z2AfzHtwMZoXDTMafkLDSgsmw4A4F0LYV7bWh7Z0kV4UwJhkVlSPXbm0SbdUQBLHhF-VrgBU-1doxm0hcWl8JD6EfsB8aipPny18yTMW-Eb1KHUgi-9K87hIwC7LV-sBgwc_ta-GWDRuo3D3YSKMeY8ZT_p6h8KeaDSOENHlq4lTu7ptIZ4N-ZeggnWiMEzl1rz4VSvi1-OEf-BlDT5VKnoxnebwEPR8Okiiyf6V7kcdO5xK8qap_F3mIB0Cfk-z4HSsYxzPMUuhsA3NGRYGDdhbS4AtZXk36WdEHy8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
