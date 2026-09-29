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
<img src="https://cdn1.telesco.pe/file/E2K-c0os9-UHJpv4ynaJUeSZ36tCo_BzDR_FNVfkgyJR_psJr8o3ldBo5ZGZ6fNV5gtzY_EOrY0v5COI0qDUnnKwPeMlP9lreuHlNmO1Yl3BaSIDTgNX5TG1WosxzbSY1kDTPcuTjWOKRlnbMPqW0M-LFv-yh5WFxX_yXuJhRLHj2xw_WSjJseGnHZSwWGw6NpzgWFxtESQU7xxfQMrSmAJoBv3GMZ4smhPgXEcanys843W4j7I62D7ADNn8ydEiUKbnAnKStbr8FtBIJLCuFJgCq0auv9zfNOTDg5GKGK3pdx2dq5cYcg2eh3XYY9_wLQtOwVvUFyaBorMK8xpQWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsBnhEZnfph9vAGmly47iHFFSHokCRuR4Niza4Dk2SxmrkH8Y4FSlgkkR9E-jzOvvrwMCukixmErEfI-58y0d2q7-v9oWKZEKPJOpppgtqc9Sj_yHiOzQjzkdrIujaWScRgajT5vdUPUt9SI3GPCUdilB021USFUH04h3ny7tEzDadCgUYQ5NGg6Fc3Yk8saWESPgjh7-TCg6lj16bIa6go5zwN4Pr6oMqwl8S9M2OVUsQxTI3CrYXZMKuObyJsQO7N4P8oNZ8tm8o9qzpaRarTu4rsXO4IkIJQKF71JQJSvPARSSCf0y9cdcWQMZnTPiqpDnpif5gRLr5HM-cWTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GN9xd0A0cMNL66OBq-PZ0lVUhFBddqZk0H4gapvEAtx1vvk4V253-zgLmgOHqHOZeh6GZJ4n3jaWMTQXh0EcS91e5nvUD7qUkAGXQ9snPlEY5U3z5jFNb3PNZhs_DLJBCel8LNOSOGZinShBkHSZ50k6bhL1SIRgC5S8t0SDRZDvCOcmpBf4ps3piXSRK4FOgfwVTWCoS6YBz7GFMDHxfgtWe92uNq6lX2huTs6F44HzR3fRc3NTFxahc8Dn4j-DCWBrDuwOggxFGNkQ002uLPbVJ_16OLI7GqJnfAXfF1L7oytqvzFUdIHuRUG3JvAqFFfT1E6P4AtLyVDle25nUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GN9xd0A0cMNL66OBq-PZ0lVUhFBddqZk0H4gapvEAtx1vvk4V253-zgLmgOHqHOZeh6GZJ4n3jaWMTQXh0EcS91e5nvUD7qUkAGXQ9snPlEY5U3z5jFNb3PNZhs_DLJBCel8LNOSOGZinShBkHSZ50k6bhL1SIRgC5S8t0SDRZDvCOcmpBf4ps3piXSRK4FOgfwVTWCoS6YBz7GFMDHxfgtWe92uNq6lX2huTs6F44HzR3fRc3NTFxahc8Dn4j-DCWBrDuwOggxFGNkQ002uLPbVJ_16OLI7GqJnfAXfF1L7oytqvzFUdIHuRUG3JvAqFFfT1E6P4AtLyVDle25nUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=n5GrdEeYEFpg9nNJ1VC16h_IF7mWZpoqQ-7OeobXCc2ZTewXs2XOm1Cp2LLf_qETBq96J9LylLyAU7VLXj8-f8mAbGKKkTYker-kRGopM4FJE28tdFUlTV-CDYgFFl4qKGozVDJqxZOaQlZq7ekZN7tkrQvn8zJFOwOlX7SdjNNte8pEPGl2tUwph35VLJztg0AWgRFt5FMv_S60K2NevlpI-3fs7bC54cTtKGyfGG4krHHyMOvpPNLjfMhT_e95B-wYpL1bKaQbmy6BxIMg6lUsncLyFc8YOvz5QmiJP_emBTe34yc4MOTvLskVYy97F4MV6SNBkDKHTp3FVXW8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=n5GrdEeYEFpg9nNJ1VC16h_IF7mWZpoqQ-7OeobXCc2ZTewXs2XOm1Cp2LLf_qETBq96J9LylLyAU7VLXj8-f8mAbGKKkTYker-kRGopM4FJE28tdFUlTV-CDYgFFl4qKGozVDJqxZOaQlZq7ekZN7tkrQvn8zJFOwOlX7SdjNNte8pEPGl2tUwph35VLJztg0AWgRFt5FMv_S60K2NevlpI-3fs7bC54cTtKGyfGG4krHHyMOvpPNLjfMhT_e95B-wYpL1bKaQbmy6BxIMg6lUsncLyFc8YOvz5QmiJP_emBTe34yc4MOTvLskVYy97F4MV6SNBkDKHTp3FVXW8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FKARJN8IWTc8Dm-K6br9hJfs5luFlE7TlcvGcmoY2-ueiy1brVRWxkozbd_cbnZuYg8V-YkZpYiuZ4mEVes8qISTz-os7MVtDh4IzEOpQnVl3EMTECi-F4m2kgFz8ruWhYJ392Qz_lCYQ9jpxWmIdPGe8hsFeyIVgucCy-2MChg_57T0ApYnnt49hRztIlSufUzSHbSdMhlJKVQ5Wo-uwsoroCntZLYPm7i1izCCx5P3gYWzZ3jPfQVmuGfQZ1b0lfmv2WONuQG6aKmnY42_cDLtQenZx9q39BCOy4j-SkXv2bQlVCJChrQZmxytVRxewdg7_RrX0wiCLN-sMmKwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-0aZcqFpNhiw1Wlkmpa7Se4gLWBkdKo7OtlYGyCGwdEpT4HhT9ZbXcxVP5ADBqjGqDGnERihQEQi_I3-XaL7AYWy4BG2whUlcRGIJB_tsudeyNJV9ZwoObR2udBjTVVcFShrKRqIhkd50cpQEJTl55VdyMFPn4m8U2fhQ-UjqxS2GE6RkZJZZTZa1ZGb6Wkxsa4NkHorfr9BGYXSdxyUQydk2zKUcf0ngZ3z7l0mXAY5lX1u9RUDd26yESY4oesMYalVW4vZkziusPn3WFTbF2qR_vyt35c_yWghNHUp3TL_yniUN_VNxzMGlnZLBQJ-TGkjEHJVjZj7YSWSPNG_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fvYV9B3Sz1yB2wnwjj8ZYKrqu8-WjmtJxjYJdOuLo_1QC_sxKX_N2-XEWUR0AHMzgaTUijv6NiRYr2d7ejGgRdnc-OGPEdXijQtyfYxKQYBfSA_quLjhyCidmlwjha1gOO933C2HTEY5c2TicsMkxSQ2-PJFxPifa-fUGxc4_jpJYI0O0mEet8ExWe2C8jRuDqesWrtmto5UUAqvYRXyophgj055i2Ti7_55AGh3GOUQfMrreg39al7X8aeWTO4J38XQ0uwLkAf-DwR1UyZas_d3kzIAhtys6ZnHV48Ep5KFqp5ZlyuELEieMwYDWmsxL7ftktClmov2DbgATxhfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFBoVNvp9ascrxFhx-9uXl5xBlQZ1O_OKByUfYIvGQzt49Y5AiZbp6slI0NSTEynlb-fVXaQUHMHIPKjuz8dHCXxfX0YXPKnTNokqyjCnH1jWOR02iKPL0W0UH1aXEex5RAsnIl9IhV5OTbSoB3BokJ6G0k9UktDjpQ9frIOf_VPznM7C5kipGnkP-lbPet5-RaOXDOyrljOlSIeoXiYqzzbEwbpqsIRRF25mpwRwQFBglJ1KUAw1LymvvayRA_oUEiKXQafgCf2pe4EXR8_Ii9B01rO_RYtqLjlPP_EuSldg53Ed7JkDUU-9uTMxCmtzU40YPlec_nzs08xSghoaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pEIj7u4_eN8Rdk4ReW5z_DSD3a-7ALm1zbfdy8bzhT5YsWQQv6SCCHsNNiQG6zzy0KSGBCYzyGVyzodmu7YWgN1KmtqjevMK0XKygWHrMcwnO7n0KL_vTvYPd95eL-fpGaScZ1mQ-BRV0UQx7M1RoMw89p2iqI4pEG3g_YkKlThxpZOyfLFidiIawWxhefHEYPb9F0iJKQLSs0FapzZjBAR5TNxV8iNIx8HQWJOtxIGZWpfwSUhhwlCCMdFdwJWRNFtYAn81gqQ67F4KlHGqZPzIJ_o_u0UyksAXkgap89v1yVa9Sx41CwcezvFQhX4J_SUQN0ke41B5FErmdzgZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JU6Tm93GeGtdhkjGRBwZ64GVQF9ckLa_WYW9BU1fFwp9nz_qgHggifdGhU1zpCBLkOYordaj2edfsGU2jCzsew4BCEaGjN_QPuhTchGs3T4Cnw_z25Q5yDpEjVcgWOFul7diD-fmeovsF5q-VkMv4h96TkcXgyTLrptvZOR7yhwfrU4cpYaXJOMubmGUzmBVT4h1RULb_HD1zQYrc1-ewlMpUNppiWNZ9xrDZLomPSXxL5gemQ47f5xJov1PdcVRTejg7Vw___zXxIU-anpGX2FmNI0ZbjgFuOczLkolpdIac0fF9ZMWD0O6fM4gU4MouuyN_KrKvGgpx-YfHtX0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WL_LaFZ4MkQpuLnWHMInJFpZYuBwThlUN5Uj7-shMUasPuDb1k_Ax1dRhTlVxQXMKBQ4vjFeETMincwbc19_-2OMgywHkFwLUyTXako4UM7kJzCekyFtRw4VjlwirZtJxhFABrCQukY7uIWP0a2Zy9xBcooLZ7251HjH1w8YXu94BVO-0cYf2T5yV8Aa9v2HsDb7eoPyGFO8KhtSr3OYVUiK_ydBbvqSoz8zjWayHDeDHr_4T-dOdxyTzsj38Hvq1z_hw2jojHmKXv7CDuUidhxg7MfazKFtrsI4Oc1lNh8RL4M9WIYWYlTl4XT4Te0rgRXXzwgKv_8aqdqBPP3OmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FW9PZHwFve1TH6p6mgnjQkjiKVByWBZKM8fwXIgtUvziT6VTIKkIKueERLCkT1vmaDG_cXSkwZNLHsnXjFWAogptu6NuwAW_DdTnNz2ZqQFQEYq6zYwaBelKtzvMi172Hx4jW4QnW7Ub9WBCG2i88lyw_MkV3cazIsuliAE5gBKMPFZb-rRXwidgXOpT5Yd9j7a3DkPXtmPbs63V07R_6i2-J8EhiUQjtVb5Pl_q2S1PK_h-IY_7nQCDBvwmHxMBL_-nJUlhWHh4AFeqM2Ug6domhMFaE1o8Nm5sL2TJUFueVdQdd2yPojXu0i-QDIfCZ3emuy5z6m-2N4ADULRWNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=KtBQP70suXlNGUHbWbFdC5IDH9Ri6iuMKsY9xuXbXXLs4JnwkXTqZQ5VqgwUrJdbKl8JmhWzAh-A5tg9VB7Hlj3zQcF_0W66sQIOVyz74xq-OoSuzrYr_2O5S4czn6cVcR0MAfBHGiOKQ6KTIRPJYbYvwC_l2IKrPlmS9nqtCC_O7toFlVgzo7aShP57zMCSc6H41p0q23b7fIJYOHPmStgmVpbZ0XYmtRcBbz5jmukXJczJXpn7_4fT28UM8shNtbqMqL46H6ehiY0YQ0kor32uo6u7Ye2-I4m7rRCC-HaQ1r-HznJszSF_OltfOsLpGTQgG0hwbJz_mxoJ5iCrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=KtBQP70suXlNGUHbWbFdC5IDH9Ri6iuMKsY9xuXbXXLs4JnwkXTqZQ5VqgwUrJdbKl8JmhWzAh-A5tg9VB7Hlj3zQcF_0W66sQIOVyz74xq-OoSuzrYr_2O5S4czn6cVcR0MAfBHGiOKQ6KTIRPJYbYvwC_l2IKrPlmS9nqtCC_O7toFlVgzo7aShP57zMCSc6H41p0q23b7fIJYOHPmStgmVpbZ0XYmtRcBbz5jmukXJczJXpn7_4fT28UM8shNtbqMqL46H6ehiY0YQ0kor32uo6u7Ye2-I4m7rRCC-HaQ1r-HznJszSF_OltfOsLpGTQgG0hwbJz_mxoJ5iCrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeliG7kcDH7BvIFtkArRoNWAGVATRx1FLSVJIYBeB2ZOyJkxVqhE32HVITMGxhLQwh5SR4qLZ0UC9rrMrnMH-o-vvbOetHKD6bX46tHVcjUtyy2tVX0VxnzSro7o2ZVQpfwDbQOaPWOeBgGvQzufRaauPHUm1nYAdR-6dNC_0_Spox69HFjN6661vAQOde1IUpzjW44eJB3epcPBn2bGNk-bWajvXHQxctyRTZLsOkhq8yjTo4cNZEU9Ic3lN-byJFGW2xrMnFkDbl1-8002ezsx9--rJ-9ciyZu8I_x5GcL-XbNVZK7vX7dvuWvo6ia4_jHUz05lfo6QnJYaMNI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J91qO1WaFstp4io1pw3yh8fUr6O-OsV7U-aLt-PkS6bsVjuAbkwwhpdCOofx09-UIUS7NGmvpp38rzRgkD2SdRjkzJY0ucJxz_DG36H-sjwLhZ3eSioQ4fpJXQr_uoxLKnHZypIi_XI_glespROBcuv8dyfrz2j-VnGbW-99PTMNyxAgu_wGuYCfpBBfPu4JNVpvmjwv2bJgxNJPc5HTcue6aBoo58wpbdExHRriDDefY-ppMm-t8LpbqWq_pm77ohCxgVuXtsW_kjuvfDMJ8UWVU-A0Zl3FkNaatzuTCJxdDHMyYVQQqMjkOEKpnLpPD_NR0OtnccaRdfuFNx816Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rCTB8wfQb7fpY6Em5yBBdMdp4UuDgX3irYPg3QsR63ZTjGKerw4p25Me-MUZeKgdgSWkq7efnxxNMJY-ndD535iZAZPthodl9Wm1woN6cjNfYwH-cOwsMgT4TqWMkULOHqLf7h3SqCofyIDR2KTiGh6HtpiC6i1sniLMwSevawAo6oKGyMKFzJ2vpETM3DnotWX9F3uX9sPHFcGy7hRNxYqXZ02T00tK5Ba37gH_WHiwfCQ1IvOyvEyl2X1LW0KMUe_-8R5iSXsA77Od814f-j7rOPf9NN7PbwXGNbsz7660wdTFsX2IBNpjRuZVnvgHDP3M68CFKOWbQBwQoa-cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FrngnS7G0namm9T1GM2OOczWcz_JcewPMgXOlgg5opREPVy-VwRha8jz9GAFUuWp4ZXU_LWZEL4kiKnCrBfDLHOl9qD2-0oT1EyAkfLSxiERiA_7S4oLdQO1wvkAi0ifuXYmNVdkJ1C75UY-E7AkjtVYCjOUDOMvmh1v17Ai7tcZNmgTMZOgPCnPyUnsdNjdx9cVFUSvDYlh6q4nY7DURbuxYeL6aIKjbzMj_UpvxuUbOWVl71YSNrAlT6p_zUDfTL7j1DTDEjj9LZ03HwayB4st9o4st_h3lObZ9Mkt2XLT6Z1pzNnZ6EkNszC85E4C08AEYBI8Qc3IRAgeaH4d5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hHxLcMry5m6wFKzv1ubuQCQhdsOqykg3CDvGtsztHUP2lJ762O37vitn5o_fFfQLUsQJa9282G564cAYpKlpC6_Cecd0e54lTYgastV1OW-wgx5MakcvZJ-xtpWXIlaXoe6p_RjToGNiZWYy7hqEGAijHbMeDsXBAv8QFvoVFb-H1xrQhXIMI5ApHPOJPSqRxgoikcm-imXkgw6QGS3y2pYNhpTtMIB3f8y0Xkw6f9acUOOVlNZr08EJsNjUzvIOs2oROAPaoRWDy0vGgqcVmxqLGAtD-V1HSjpVx-MLB9YdSv5siZpfynvA64RzSur1z3Ht5z8J9VusEVQeDFPieA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nozS5XDZ6yPFAPVTlwBGU0DGu-dAghghlibOvPgI2rOTazuD_OSI4iygbUjzeE-v_lWuKHWus2w2oI2IzmMC7UGoraGoZXO_pUcHzC_QE4s6v6MogVO3-xtKvgba-3FAjlgecVPoh5Ei0dmJs_R7y9M35m7mB34k3ammMV8ic2bzyY1MjM1gMIELG55euCy_J1BXsmAeBXZ6-nhov6jDr09UACud_hXELw6V2ICt_75j0JQIadfXPiB-X6PSq3Twt2rQi_YkOYpmgp8TiOU2vwp0wjbdxsO9LtIbBMMVIl-Jjc0NiaPUgjxzkwqWJD60oAao5hNQWAeVWUMjMKj5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R76qZt4WR6qrOieLJBaelixU1Pzf06Yq6FWhHbDhe3QNHF6b5PYH_g5PxuVpSeO2oXqVmER3fi80dgzQIJPe_D56hoEHqAQHSXCZvSVqogBr-3yuYkWBW5oHzmvduADZKvVoGdOmfn001-syF0jMIIpKZF02RoZRiNOyRnnyLpBKTCjKlb701MzPrLSCLO0Uzq7YGDTAjKximTJD_MVuyB_9JjcPHA45STPWin74EnaeHUoLJ84P58fKaMRKIWonpsFqfqhIq-9WZhJFaSXpIczIBklaAx8prasxPmrgiUIBGeICpcP6dyMCk-2iO5-I8nCxhA_QcrZ_gYrLw39grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeVKaBlQp5gYt7O-1Y4GueMpzlojaUwMyV65I_az07UbIHIwYPpvTR-GMVUPylDDDaw1iH1K290y8N5km2rx4MVoJNZSBKxv7R0XKCJPKitHhCQ5BTTiKDoZIXqYh4ZBok7nQUKNAvTTV4lIgjGJJLA-7m_M3XbkYKufd1AdzhGjy5Y9uPKSXbeHlfKbkPDPonyEJV_PYBu3wRbdYnf4tX8fxHplee_rzkZ9Xv1c0ZvmEQnwBbkQIOuIPopIPfOpHOdjekVa0a-_loPUbPkpz0TCmUkVRAYwakQWGMkLehnv3yLfvFCbo4QR8Kq7MOSL4dqy9nZ8Zhxa_M6i7QIEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZEitaGN_Dpm54vaNnCPdpFcEvM7u_LWYzMESeyWYnOP3E0r8wgojVbysQSCb7xMExJ-NuvdxfErHs5IHPyuBRmCCDF3HnHw-Ztz8t8MEAfQ9D2Gq6HCsnb-0E8I2yVd72XfGLJ4-fa2HYv-7oyh_ushMwCrXM748RAOhhuUHmsBgbJQuVn1767ZlTjQK1ofv943JpuRDuBSEyB1H1t71SP9SQjhb1vsjG6YjHO6OLrMRnLq9NFrOFTnfaMO-JGQJu8VhLJ1_9IxyKW5jPRF9jBYTJT6Sb7lqs9S649nTB6wThUzFGhpbAiNRnxNlRbelMaV-9XHCAgTBHEBFFsUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUwuoq8LFKsDFDmZsjDH4wTu4vv13w-OpbZADPMIJZpwXmboksp81hGB20J6otNU5Bc2HiIpdyUPFenxwqfrUxAmFY3mzQBRZp4o-gxMzajZdEmTONzXgy_gHiiJ-aBsQm4dVLj0UvpQZDm4h0FK7ZhDpzMp7_Z2w0dNWi3pNBBhyzrQnUs_YgNEgZxGbAFVS6PCtD0ECt2lQHAFGj4MEDH9Y8t-jG5yvm0b5Xqwluy9sNPxpy7Zy_kyFVpnvnft5Qlk_N1L1Fq-bNI6SV5WwLOkMYoLTC0ZEyt-OJLzMios9eYLaSPpMdPJaOMOS-qqO0W-2LwnOVaAzH-9wNhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=CnROdKyOVSmyrKeOffqy-lGW1u-GTtAB0V_6Mmkgotyf4f4Ns-vhg--wWOS7Bysd-fmI-lbck2yxgGJ-pdb-ePi2f4CpV-tBMwJw1VXYDQKff6IH57GFOtbrtuAElFBnji7Pt6GaDWiC6KepyUB-f7YJhjukgj_0vwUxP5_KEtUDfRH-7o9BPj86Q7qj6Mcd8xA4zTVXZZl_rtvYRZJxytqkCAicHdnKQgL1RkvrDM6Z2VOLoz9efn5lAuCifY_qcHPii4ivM8_lW4YkhTTrdY7oob7uhId8NQX1n0TZzAWwBerYXLlHz4jOfZSJU5dTYi7DknrRPe4tFdE8YRjjjRqEhEjRQinQQHdjCGoVsgrGyc2fuF78vZeCR2Sf97YZWuH65qqIx6SdoHRVzq9eJtqzBgk8K-pCQVRNkFDVzndb7m3dcJvqdlO9OsedPtsJ6-ZyO0qPyRHvZaXMBevx-HHCwUqsjeUa-M1KV6TMCBylOdPpPdfQysjX-BMOrEIR2hY2VOy3MxrDms1TpQCME8jiY9_rLLdhhQs8aytv3_NOVA-iZ8fZzSrbjUvoYEPcc_NJQNbuMfQqhrSVPidu9YhXlDBfvCl02GWA2WdjtpocdlG38eC79F5Wk_yWkWSDKpJQXnz_LhkIzf4GYQAXntPDGBZF9fJL3xDX0wEQkkI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=CnROdKyOVSmyrKeOffqy-lGW1u-GTtAB0V_6Mmkgotyf4f4Ns-vhg--wWOS7Bysd-fmI-lbck2yxgGJ-pdb-ePi2f4CpV-tBMwJw1VXYDQKff6IH57GFOtbrtuAElFBnji7Pt6GaDWiC6KepyUB-f7YJhjukgj_0vwUxP5_KEtUDfRH-7o9BPj86Q7qj6Mcd8xA4zTVXZZl_rtvYRZJxytqkCAicHdnKQgL1RkvrDM6Z2VOLoz9efn5lAuCifY_qcHPii4ivM8_lW4YkhTTrdY7oob7uhId8NQX1n0TZzAWwBerYXLlHz4jOfZSJU5dTYi7DknrRPe4tFdE8YRjjjRqEhEjRQinQQHdjCGoVsgrGyc2fuF78vZeCR2Sf97YZWuH65qqIx6SdoHRVzq9eJtqzBgk8K-pCQVRNkFDVzndb7m3dcJvqdlO9OsedPtsJ6-ZyO0qPyRHvZaXMBevx-HHCwUqsjeUa-M1KV6TMCBylOdPpPdfQysjX-BMOrEIR2hY2VOy3MxrDms1TpQCME8jiY9_rLLdhhQs8aytv3_NOVA-iZ8fZzSrbjUvoYEPcc_NJQNbuMfQqhrSVPidu9YhXlDBfvCl02GWA2WdjtpocdlG38eC79F5Wk_yWkWSDKpJQXnz_LhkIzf4GYQAXntPDGBZF9fJL3xDX0wEQkkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5MWiDxEG0I9ytTed16BTBScaDKoMPbmNztdYrE-KrSHlPjXcy_7_kVdjLccUOral_VMHlp6HDj2Yv37oUwUuyXpCqtbxH5yx1Ay6ZUKxdgbAnL-ar1WoXjOjwx-P1X6ujhp_Pp-OObqZx8v9KOtAkQkXR5F-7OlJ_02Kv-y0YEfaahs0S-ygo7IUhlqeiyfBUblWlNZX-c7Jk4k_-NXV6s6yh1zBRdnDuNZX4PiwEdmKlszPf_rDoFG7opkfAFev8bTmEhQuyT9b5uc75QrktYHTfOOYP4yLdf8EyIT-QdC4dfw0DE7A7A61CeVzG1XM7_dzi74NhVKn7xtJRsukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULGYEqPxBAfPMOM5imtD2VeqFuYWq5Kl5in9WsrGEcLwxBsxEwoaWA2uVPcK968OEU75gvQUY4-P9hGFmg2mG2vBQdKDjtv_vLAWSjWCQh0LQhNtZ3yiwoKCpmkaYJr0h_JYSYx0C0JPpbQ0X8o7EdpCv5zK38yvNUrBc5MqN2W2n9n_welAdF6jT6aWd_FcFry0IX1pEuUUvo-xyAYVr4Vr617TszgCXdvyie6pUakWWgqdnsBdRqOQvgvU63bXSe3_XP0KReMARQxzlxeccGlKhKg6oGDWWmDkIx9t9-CiIRSzgEgnTjnmnlXJ65HYYFcGfIUnnsErFLjTJsiyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pAVPLn_7cYWTrJ-7d4PfS7FI94_zcfwKC-YGp7F9t-6rmCYDJJD35Ot8Hi0D4sg4pwrYDhQqnM6p9s03eITCviO06UJ921q_JiEzQrmjf9k2qg61-BWzPWKc-8vNVRVQ4BsQQm6JFES8kfVAbmQ7u4Peq7hLBEXIzU5rXBjEz-IJpaD3dIM1CbirUeoRBtn6XcVJRecmx2m-XeY8EMiRKGd5dTHw9UvDawLEBocm77cvKfqfEDZxL_w8OA3Z-aalt86aDWiSDFOqDAB9iRXavb3cWd6GgjC3FcSbVYdT1mEM_F5wu1IYJoBaGp1fPueswEMBoQV89ZsZ-pQfL_11NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjjfapcewmQeA2TfKAy87dZ1KJEFlmSezV1QabMn_F3cu07zePaWCwVUQbMgqN6CO_7nAoeaoi-HkM4kF7ohTEEvA0NZZmEDV4h9x3eZDnwcyA00FC7_8FRbgo9w-LzDnvs_0OhrvDUZ7BZvSqqIsYkmqEZ6acSuRN5DcOudJbHopXnVh01Ylktwzxel0ItvtZC5GktlGSR74HhOuus8uLpYL5qB7wMROTnuncY-l8kgSoNWWjRF9KD_1jyFfAELsjxaLxQ-QqPWQ2dZ6lLIXWXBOwnExA7a_7YpYz2QL9Jyc-jgP-6I7jkcZzCkH37wb6c9c5HdnC-xRl-GzzCXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXw18fMFxAx6K5gwM-sDsxv-H1_ha_WkR6d8mLc3A38S-n_UBNTEPKQI86F34TsWTMZYBK8lARhGMybTyeS1Siu-LlxNukMzm_PFR8wqWaajRy4IcONXmgna-Wy-3xj5RwpYbB9Qqd1_k82GlbP-mC4OClp9_Jl1tDanHLu5ajrVLY0lPMBzCiVpbE_jgvJZdeJshGOwYwhVI9y-AAbfX-KCLls53q2ueeFqMYGkwIm-XOW5zJZESIjo_2K8QDeLtDOGAsTpcVQL7cuLtHSaQGp-UZxiY8M7XXfj0hEPGXWFT-2lMZ0J1-4R5msTDoJVyGdTaVJRP2bl_LkRv5-fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XkYcpB0U-cs7SXmTfQJG_fnEIgLQqfik3VkS7laGfoV_hbG9qfdomfeBCw6Edv6X8_sZmkh9FISSVp6KfCBRqfqvUImkIbv8FdwspHlFZjLuo_EW5rFEFsrDmMBdrXPZ2O-sNqMvtSxlCHemNl40YAYyR7pgd7BCeNgN5EABwI5z-mmex_GrBVQGar8dPZI-DHq9Hcn1Vw2Qtiov1tu1Z15oADzaol_j-t5KfZlhf4djqFoBXFMYNkS3CD_1_VDiO8kNP5B3_3_ArxPnup34JYGQ3RWbbTtwec8UB3mftC9oR8-DJE6dXa9cdIMMVCMhwTNpUPeEKT70_42te8cPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=UDmli2rCStJuka1fM3nr13CZE-8sdK9eiR8ZWZcjWWR_pcF1J6obGOds9hKo1ISssqA_uP8ehdznzS4fxda7AkEYGOQ-gGeGA6E6RyHfGOFxT4uxwOzJnatDG0iw7vtuqXt1u-vuWKzKUJ7ZJs9doNnL1-Uy3F4GU6V4jtzud6uvIuTmKcQ2or1JUzGStvtqWv4oQwiB4p4ZCW4ASFtLyZFQHDYOaBdjw4Y02A3NdpecUA5yboaaNuFqmjEth5USqbzM3ShiGJ2y_PhWxYU1j3uKTIWps1tQ8nEXl_UHD1aWl3PuarTvPaZmcXZgpZhhRd5pxwnGTacpWbkmHhlP9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=UDmli2rCStJuka1fM3nr13CZE-8sdK9eiR8ZWZcjWWR_pcF1J6obGOds9hKo1ISssqA_uP8ehdznzS4fxda7AkEYGOQ-gGeGA6E6RyHfGOFxT4uxwOzJnatDG0iw7vtuqXt1u-vuWKzKUJ7ZJs9doNnL1-Uy3F4GU6V4jtzud6uvIuTmKcQ2or1JUzGStvtqWv4oQwiB4p4ZCW4ASFtLyZFQHDYOaBdjw4Y02A3NdpecUA5yboaaNuFqmjEth5USqbzM3ShiGJ2y_PhWxYU1j3uKTIWps1tQ8nEXl_UHD1aWl3PuarTvPaZmcXZgpZhhRd5pxwnGTacpWbkmHhlP9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/patOCTR0HFconjktv_KWMEuvlZ6hMyLa9GAeMxF5goe3y2gRhNJz2wODS6Bg5BQZ1qHPt2ju5b6SmYvY4sA5CkxX5wdhY0ionV6sXthXuggwRQO1Os-xpUqqQz3d-ds0JZ3-rKoTis7pxG-beD2ryTYF1Twfs74UOnOnJvgpweL7HScyop5JRJFgAHtvva70IiYeNQ5GAcE5C7ORgQ_tUxfOlB1aFUKgYS8kQJsFC3j5kOXEyG6PpODyLeMVkmEKSISltw6Uv6NAgYfRKuZXtWyMZeQYqSBsWSsPe_s6mFxQe_kKhBlwQdxMmfOUT8NA-cOThcyygrEopQfAqdsfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BhMR_1jdsOTYnKcEhIyyTugUUxzYSdeWB1Kcl_gcriLRgbuEEzu2Qd3wGYXMo82gtQ2j02cy0fQLfxcoZRov0DDf5BDM4s_gNbgo_pGajdrDl5BPUZV3IKW1dhcx_-GI6SJWDieKByHxliMzlBNEFYkotyLzwxWR8dnG87BuYJcwc72Ez1WrI8Sq37KxYFjLp0rBpRm-lEGEVeBAHUyA9M6wlQ91HpwcT7Ogm1cqD4V9g09LcsrQV3G_OKhzG3nEEDcXZmRknNSHa2WAjRqyAXKYxQQkG6bBUsJ9APUUBtem_TpLXpzOT2pN4OQqKY6Czj5XmjL2AhV2-oAMOj_HWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3htc6n3tYPMfhRjkSFooglPvcJRvqbCxvp0V7wGc-VXgxxj7pscS5utzoxLDOAyKeVLcMnOTvVMLNZ6CVkqn-66KhiQJK9V8qufxctsC1X4H2hT9l-vTcvEGEzqAjBKBow03Kssk9Wn1umaAS2zG9gku-B7Ma3GVseB1EfH_Eed1g1MTXTTu-hSg7uYkgKk-XynEsxajgpzMoIXkr43V4f3bbKxAaaMjNM6QT_VNQAhTBjRvbPn0CjLHW8FN2IayqTbM8rGQ2eef-1kYAqgZmEq1iz_Xu6ToZ9J7WYJuKQEuZS4qCgnD-R4YTLYh2MMH_t5MX63BPcpuidExxJOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HYmsxHYiltbJaqfilKFUbyWCUwP3nYOKjZ4zNgVUygRpr4Rp9YsQpADedvgvMVTHgGNwtBvXnYfBDcDBFIQo0Akq3F9_oni-ZHHvvlJR4grRntZaPRWj7WniMf1XSdLbCx7U0gcggjvK6AJN2hbLJNasuLxuvbgku1MP0WTko0g_4HllxtqnIl4lFRTrZtB-hob_TN8b_SJo1If8Q_WY_3ZDztHPFUoEdomA2vIkdgEbV9W-fG_lSN1jqC1B-Y-KXZaqlvIcm9Ays2m-fGWYcbqvajAVDGPwN0f_XG0uatoOUltLuNpIVoPUgJBZaIQ4b7BpHT_G2OjOdCYsqlWEow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWUjnvdHDgqd0vPE0CXveINd4gCYQSIyxJ1ZYwciPeKkGSvAykS-n3Jexop-LR_V8g7kAjp6AQ-zrLJNUy9nQ9bZE5vIyOXov3swbnkDFGfn7aLHLulfu75d14WqdMNIUNUzqoq1lxQBre02OA3y8u8012Bn_89n7p9xVGRXCsu8KiOC4yLtfumEyHXofANGPvHTmqsGIpdcjWyxQ-XbFCxBUXVifo1mT4QHRl1Tz4IhhUdK0VQd0soDS8nvjSjkI_pLomlKJjGejqK7RbbEiJlpLpjMCVjpMVfWXOYCJNAqYxenpOhntbjTpRyvoMDboRVHT1GDiWS8pVH8EKU-HVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWUjnvdHDgqd0vPE0CXveINd4gCYQSIyxJ1ZYwciPeKkGSvAykS-n3Jexop-LR_V8g7kAjp6AQ-zrLJNUy9nQ9bZE5vIyOXov3swbnkDFGfn7aLHLulfu75d14WqdMNIUNUzqoq1lxQBre02OA3y8u8012Bn_89n7p9xVGRXCsu8KiOC4yLtfumEyHXofANGPvHTmqsGIpdcjWyxQ-XbFCxBUXVifo1mT4QHRl1Tz4IhhUdK0VQd0soDS8nvjSjkI_pLomlKJjGejqK7RbbEiJlpLpjMCVjpMVfWXOYCJNAqYxenpOhntbjTpRyvoMDboRVHT1GDiWS8pVH8EKU-HVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=NWT9AQiZGX6JoTQc2B1v9D-BFcjOfjR70mzica4d4VXmTzmI8PTGuEXjrn_L_hc7YaCMFe6gx6dHHhtsXv20E-WA55PGHCBwDUb3-vkgaescszC4j8eW3A-vq84Inbx2_sgwA9dfCqXnHWLiP-tv6n0YnjXqmZ93PnElGaFAdqp1PpZPkyqgM5ZM5anLruBDnN5fV4fDq7Rbc9-kkbwMVWEkKRlXGphlf8thb7hLynwBLXeuJau8Y6coRTiIhz0gbTh-6EXO7V-ByL4PxP2rHfFOfyMW4fufyDcvOp9zn21z14D_hY6EIPLhFaG6CExphKwN8SmtDAxCs--QLRcEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=NWT9AQiZGX6JoTQc2B1v9D-BFcjOfjR70mzica4d4VXmTzmI8PTGuEXjrn_L_hc7YaCMFe6gx6dHHhtsXv20E-WA55PGHCBwDUb3-vkgaescszC4j8eW3A-vq84Inbx2_sgwA9dfCqXnHWLiP-tv6n0YnjXqmZ93PnElGaFAdqp1PpZPkyqgM5ZM5anLruBDnN5fV4fDq7Rbc9-kkbwMVWEkKRlXGphlf8thb7hLynwBLXeuJau8Y6coRTiIhz0gbTh-6EXO7V-ByL4PxP2rHfFOfyMW4fufyDcvOp9zn21z14D_hY6EIPLhFaG6CExphKwN8SmtDAxCs--QLRcEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rs3Mt2NazBvB3Gt_KIpnoX6BCCgnD4uw8Mxji9klhrPYeSfopDFbcjLorxhTkJxfpV3hqA6hiIvmYsC3Yzgbs0NsmkWzGxFgiNfEqhD9piw5_h2P0ScGAEjgK6ejZei1qxMqDMK2ylKp1JpT-bu0zWu9wviC5Nltzuykw6j4wfbsHjLM1aO7O7qA7wVKRnk2OUdsLf6pXWN_FjHzYZbwSmXqK_pxUZfZu-16eVWfHaJwqQilD5vqI10Ob5hZBaL56vLdiujLZ7nbg6iaP4EYlMDBjwMOpj95hxUTMyXr60OIcnIbwK7uWi6FIA2AgwJDwUtbvoADzBhgm0GAO1ZPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/haeGPFYWvy4fhRPYi2qcFvSZnoz9b2V_3mChxGcYvRa6-LtiPOAByp8MMSQ-72sOoNsSRT3fcPD61QZHjIF0RE6xuyw5EGGKufsIwO9gtKwXkfVn1tgtmSXyDzyGVYnPDcNOOLockuN4hg3kFBYjSVIj9EqA6zqeLNIWiMm8eWO9ZWoM2qRX_GGkrQQjRcjs8ZtBzkpOSIH5GL7nPCKlAyx4pTRfHX7uuDMR93d2aP53-VuEg7dc7SkJYGrUNTAkmOemhJriOT2mhsHpSgrTU8akKjXFHNEnQRlIn-KWv2BaoHCwHPdSMYzmxiBNYpfo0QfPVFo7pX1ODdzPMbGYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT6MfEF_YkPUfL2sSdYfCHxHLYc8mZZ0CGu_gKTzEHDiXf-bZSoEsR8_efAiUHDcUFm15jxi89Gl41jvolat-zWwQOrdhlBDtbX6fqB2dav0PLQZ62T76xduQ0CV7jpfWmu9tonbhkCv2bmEr_Tvc0t74giOqY7A0qUXTpWnsSJbhr5cri3bZitAjOPCoO61u-VtvPjIwdOxyFEYurPRitc7IFQA4YHC-5DQU1WRl8Ax-pEr8xgdwAdvu-jG_JoZMGtroHdl_r8r8j8QGK5GZHvu0fo9xNWOQt0-86eS2OPDzWCKx14DJ1CVM_d1EuAr7JXXDiL5pgt-sxCg5prdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsCjIkSS9eIE6u3zU1PqcsuG8FS80uW68iHndOv20TnsD-yhu07l5XVZRQ6R_b_ulcicuYXS1MIcBz-4ERpxzZCaS5WybBvXM4F0BYG789WZAQnJb22KEJKFWPFHsNOUSNe6xIK0es6tVOB7dVBJWGMX_1jDzzy_YgVQ4JB0oFZPxpc1od8n2Cxp6M6Aq65Oh1ATvsizuGNDkFZ8m3WhkwQcQ7aIIhhAy44wmjibwQz_oJSsEP8BdV1N3zgdRTENg7QvRlEs_KTZ3W_Kh70pu7r4wQ4PZZ_VZegO1VUgI6rL8fEZBManwthjZxA3B-XmC1hbRfsGlCDM7kAX48aCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRja30mmLeI29Tm79T99gKn11nvFra_Q2uqwA4QzPVOEv_qGQaYiJwaaDzMs4GjowklhbKAwWt2G-NDV0Il2iT-ryvgCVwbemqTJBpg5HRdm9-hj6r2I83r0__PLEdVI0_1O6BlgWODLzAbwWQnRCHdv2Wes6UDMjplbgFB7Rc6UtT0CN-T6P3D0jPjxDwHXsb2xfzgjmqKjTwYQfgBKFVPdGYJRRo4kGeyAQ9Cqkzs8qsvZqpDH57KkCkU57aEc84IduS6lJ9VimyMde0pacRQRwVI1gbILTkOBDtp7xAYcGizZduLzsabna1j-zBVzkQkBebjvwCB-fxQuaD_HfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKIBOJJuC7cz75QcDrIptQ3ec3KaKVSJmSubiFj-BME-MVD6UWZGNfeEE9TnhMR8QfGJL8kjfC_JNiLqhhJtxfYJNjACT06O_Rbue9CeYgK7_6y3RnVJH6j6rN_1Orxl1NhxEeBPLZOMW03-4hWQ0E4PEY3BQmcUs1P_CO261NIVuZi1Kgl3P5REjoh_p9RcMj4w_SFBIzh5ByOdm66GX0o9UFkNlbBKe8kTi1Yw62f4ewtG39koCGNl6P3S6jZVU6-OyGA6CXiXf9EAru7Wimmv2o04dF5Cb4krKtS-nfMpYBztb64Pqu-KMW3jatZzw7VeOXtLhFF3K52Poj8wXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbqsOG0ScoxSwJuKJqPCK6Sqg7rXai9yDmi1QyCGyvMWgvN5cMPcwFuGhL9OwrIalkQUP0Q2zOc_dhB2T5cVsuTeH6cbe4lS6KPdGYAJCHBiu4hpyiBeIthF4NpJvFSE0FUu9BrpXBX4Wv-8eSVyS9XxqtYXTlpw_6cb5D1LF3ISZ-TptHO4j_j-_312FPb4C3halPWdaZy8HaUIVT5k66pp-qzIgOIo3_hxiPLsrinEUjBlE9Y_juAOdsf3x7leo0LnqJkFZr6kjC1wwqjVVKu-ez8PXqvkf4yRjSpPw4w7nJTVmkXlLcGANmvru0b9p4mGWBAbAdyMd4svS7Ba_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOx0TzuQeJLoI010prgdBEBFeL0TmE1uHVZustKNuCOlYV5iQoDcpVhc6vBoQaI8o4Dwe-6Cc44G8DCJhoJnugggfvQNgctJwdnrDKCh5etnPaRh-0GAze2UEYfGLpmiOkpTJu42_6OHQAJAG6LhXOEarEvzs_3quWGkykHzMcwUOsW9cy1IPoUKSRNmyT9T0t38O2c6RQEyz64er9LoKha6XwH7CIoIN1BqEVqorAi0j4QkSiHKOMHx8L3ZRjWzj5t0kZ-kY7s04RNmeRUMs2loOsFqy2r79jfb8AsfNP7IkxogJDT6Vd_H2gu37-oPHn1mjKYnEeSe_9kJoXG8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=AOzgagmTL5Gf01HNnolfsjfUxa_QVbZ72u1lhgddCLpRxEdM4PmeCiTZtP8ueM4s-J6IsI0-xt1iIXfxT3wIbYPjTQQpwL6ArsriiDqxoNiMqr2NH1icqm5172R6mPXgyvSz96K9nzM3aU_nHHJfVf0uSFEp0y7GSTmheDWpiAY1le6RkRo-6fBLfNsgpfrXLhvAMuHu-PJpgCS5WdK0HU_hjIL6dBmqOXA-pa01MRyWuQmkUynS-Lr05dNNurcam6Cq0kyka1TvLcXu6LFv6G0e8z-wADuJRTIFBjry1W5O7xESG_eNJ7-Sr_EmJ8PA7jrp08nf_rRbsAbCjGqZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=AOzgagmTL5Gf01HNnolfsjfUxa_QVbZ72u1lhgddCLpRxEdM4PmeCiTZtP8ueM4s-J6IsI0-xt1iIXfxT3wIbYPjTQQpwL6ArsriiDqxoNiMqr2NH1icqm5172R6mPXgyvSz96K9nzM3aU_nHHJfVf0uSFEp0y7GSTmheDWpiAY1le6RkRo-6fBLfNsgpfrXLhvAMuHu-PJpgCS5WdK0HU_hjIL6dBmqOXA-pa01MRyWuQmkUynS-Lr05dNNurcam6Cq0kyka1TvLcXu6LFv6G0e8z-wADuJRTIFBjry1W5O7xESG_eNJ7-Sr_EmJ8PA7jrp08nf_rRbsAbCjGqZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZCnJyKgdyFmzYiPcxxZ4VKqo6EBgFficdnGruPCn3YDkdVwd9HUP5tvWfkulOcQVIos_gzZFBGBDqwg2tQtlobzXwUO8y41hqq35lGF0BW9eVLX3Zlh3N0YCMJ4LOYEI-Guh0cxnXMqCS8UXwmcuYp-0H9Yj8jRApXhPo9WlQD0BsaozUhOpHoBi0XY1EtG4n2SDrY7mYSbBhmWrh9AyZjwUcWF-jD8-StOjft_AiIS40bKL5L2VCJ9dukLmdmR8XNnmUD9zxu1lIBkZRmMqW1qH9aWRAmnqffvb31kN1uWG9q0p3DWY6d8DY4y5h7nI3b2YUkWY3Z2NxLXdzGXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IjvGMMvo-qMnx9t2gRBt8tmY8yoi5QWQ4UfoJBoiVZFBpOBXI-4YF_RR_81T8sHJ7Ez2ByJjd0F6_jwdimyDKqWAhVsi6CQ0rGpe30NHaXzgZfsJFSJZknBqkA14nKNdx5llbSV1J7sm_nDY9kJpUCfEOs0iKbrMUldhDZZ3OUxCpRZKLWUkUUCHHGIx9ur7_FCW0gCN_-WzTi-l7Wt9bGj0KygTQnPK_mZgzcluEDd9jTLuWRrO1vnoE1YU_39MC9lBcOmQFv6dDqozKdWgZRIL1HMEINWNszG-eSWh4Z5CKsWFvvdIwRmtmU-gFL4U0vg0Rms6tab2I_DDwK28hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iln8XruCYG_kEqFNRzXMugBc4ckQhNYpWU3TrBvt13e-sinY-B3bhinInI6vN1xjv3aZsqWiKNEp97xBsRqQlp0VnpOv2dNrgGC_JdeK2NiBp_65nZthwKHk4NL5ZMr8VCcF795nwXBGI-zlgl-GRiF9FnahKK2x_A2mYYR5ttquePOgavC9fNvAb_S2cPveRMOjDW60LVUZlVAeV_-poz-3EWiIjwCaGcBICYMeXWR9jJMiT8M5G09EV8QQdevpket8T9tQTnDKmfMn0BIpUIK3rRvkHRPjLWUhwVYZYlRm-v6MRzmQ4oo8aScyX3Ar5u8kKeDlBH7d4xWumE263w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4NNfRLv80Q0Sd9f-fedQNovAJKHWVGQc7Qhq6L-VXyJFuq5IAwm6LrAbas7jzEZz8dBvsDIcQr850rbfB5oa2FE-FEOPAuNOVT7ooz0Lto7lfMWizKw0MVPrYqfPC_L_m5EXO4kBSl6JliuWjNumLAMv3jdiRJU0nGaMHG7CpFLO9NokgXNPnScdTDEXn5Pu7DtvQOGbWsve4D6RNA6b8kOW2xmRvj4EoeScH40jCilT6t3wUWzd1RtS6kR51eOp5iQF1jv9lE2Irr0BiVZX5CQ_aMgbmSx5b738wiw2kZqbN2I30bnzUUdA9H1RWc8iB4EYHZ04juwOTBcv0mVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=AeykM6h6diHNGr7cq1cDuyhdnzR4s7HC9uBdFDqzpLIGb20TOOF8GGdtkHBqgt_vwhIm3MEqwHO1Vo6RywaUv0fLbU1_umzzwGtS41zJJF4_C7RKBP6Kewg7pvazdrR75Jv0M8HrN9flUCSCGFdGGoYpLc8HKftPb_ydNhz65p-UJ4eq4tEISn6w2imU-X7ESSvCmgwQk75kRnu50IbhfI1GdmepqSVE42qQtqD-cAp8ttengMEiX5e-I0cOwLgUWVgw5ca51WS1mR5_qpgVyOlSzNbPW0unlbqsq20ppmLHDTuS62ovJEqxIvwYXsGjJHosSTWGq_xqN76KetIrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=AeykM6h6diHNGr7cq1cDuyhdnzR4s7HC9uBdFDqzpLIGb20TOOF8GGdtkHBqgt_vwhIm3MEqwHO1Vo6RywaUv0fLbU1_umzzwGtS41zJJF4_C7RKBP6Kewg7pvazdrR75Jv0M8HrN9flUCSCGFdGGoYpLc8HKftPb_ydNhz65p-UJ4eq4tEISn6w2imU-X7ESSvCmgwQk75kRnu50IbhfI1GdmepqSVE42qQtqD-cAp8ttengMEiX5e-I0cOwLgUWVgw5ca51WS1mR5_qpgVyOlSzNbPW0unlbqsq20ppmLHDTuS62ovJEqxIvwYXsGjJHosSTWGq_xqN76KetIrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk9tb4wB1ucvvTkuIIJ77fG6H_AkFUScbS4zYTJ-nWLm_zmcKUNHvdE2EHFML-uul-HPZnVU9acmSVg10G58z2506Vy5E02yKMhtjw3ULUjINWsmV-kNqyxwsP3Y1PISUl6iOB7Bz9bDTo-oE35VMIUpReJnTWSjTQZLPYYovEd94nWJeXhewGQSqEdeZhx6cwr511YXu9Yk7qdk01RfNhOU42kANr9zveb5C5uWse1fL42C2bY9AqDseWrVeUhNjY4UQJnV3lbu7wZNk2oMpD-G4s3mKCkopL-sxZ7lEuhtHZJKx8SX--jq8HETV0CqWZaLS1sS3vDn5jZGmecrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=JANrzzRd4BUXIgyc6f3ZvPL1bRILafK7z6FdcthFmjOAurukmqUlMJKTiqpSBHD7yuSz1tA7Vgk7P_PSuHLT0EbiOtfj3XUSGhD_cLdZ248-AOPKgdFKxNzQBsdiY7p-je-s-HAq2JGxpnbBDX79-IPxlzDR52mSHWbCSK4b6GOMUqdZV7wDUgdgD0StuL8dtrjbq2l0J8ncQghcBZwI180S1OGAQAlCYiuOViA7MMbcyq0eHUqbc9zwDnHpyIthRZeG5-fM8psAu45GsB9foBurOz2vhWs97m6OscO_EjonoDyKDZooLy3-GMmvh6B26WAhjLhXqm0TYJbeCwnPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=JANrzzRd4BUXIgyc6f3ZvPL1bRILafK7z6FdcthFmjOAurukmqUlMJKTiqpSBHD7yuSz1tA7Vgk7P_PSuHLT0EbiOtfj3XUSGhD_cLdZ248-AOPKgdFKxNzQBsdiY7p-je-s-HAq2JGxpnbBDX79-IPxlzDR52mSHWbCSK4b6GOMUqdZV7wDUgdgD0StuL8dtrjbq2l0J8ncQghcBZwI180S1OGAQAlCYiuOViA7MMbcyq0eHUqbc9zwDnHpyIthRZeG5-fM8psAu45GsB9foBurOz2vhWs97m6OscO_EjonoDyKDZooLy3-GMmvh6B26WAhjLhXqm0TYJbeCwnPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AzDdIjB7dro4EPOuwk23YXGbPzEHaOm4d22T1FcFFtmNGo_AIRniBQXe5CTjwZjSkO9QjMc5EtBGg6eEgSPQGjl7cVJZi5R1q4SiH-ApcERHSvxBMKuA8fi61QhWfBF-_S-jbYvL9HMNBtocN4Wvpkcvh6Vb5_ZKoPVrM9LiGoi1AAd-iQeNljDIIdoJEQyIqC3qHA1gEN9BgcVZLPZfwK8lkcvQ-GjZaFZPq0uMga-6351De-mioLsTjzlH77X89IR_OrlkIY5mzikJ0FsEoZqPTjMfyfoe0z61cUTJHgvuMRgSxjveW1OdZTn_eLtQl4GwPaF_hxzwSQXI4NV40g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StFv2pTR1AMMsVTw7fqDmBG5TfxRODmph_Uxfnlj7soBzjP9qyB4PfXpklx9ahnxZ_pFkLjL2jU29z6mVhm9mBAfJEKuZjlmK5AbBgrCRmR18duQlhL9moyz5mPro2giVF_DF7-tFeuPhoM6zokwGaL6Dp52LLJ-3uQLL9ATq_cfm0rBL2vqihZ6bP4K2Ua6SgowDh5GmqXK1QB8pnSLrCWAC0WierQzuzDk2DFQeBXXdrf7J0y-DhqIHKKDVvb2tNW4plzYX_Imj3ycxj0HJByTjqbt3s7J_rjLeGxx35ikKjlC-fvD6HY1PXC_y-WhkKfv2hX_aynQy7sAstSxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j6UrpntaGq1fHmGpxXW1pvWBxwuY-IcgewuLbsu34zgPORP_AJ_S8vufA9wDZ3m1kTaQ2q83viNrtG3-xxfcdomXQ5LHYerZV9ozqhvK8E4RTxz31tQ0sg2_FsZuGcOQ_UmoJ3POgJFPRXOt45be8u6AvSEn9w3SOs8ZnEnMgmzeoHN-rCVjO4DunQldvT56tMemuyfvelcq3bBv_LACI-I5r_Ps4pcYTIy-23SddFzOssFmThpfRm6MI5AO-2lvJs1hn3cBIylhZhcASQroylaQHlQgKrgcqANx5sWBEGUFBpbyL9mws6RX2fuRDmI2DwLQ1ZtJZrm0Prr7Ky6K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mETqBF76yz-qv5iGHpdHweGwK_rU-miTJ-V-Yt9mMvW_p9LZhYgk0DcVp0BkXQ20Vhomzd9mlmYMPt_V3bpjNoziL6DnILNVH6PbwlRfCrh0ooMOgcurmPlAzReBeO2MClTU-_GJ5rqs3vszJ09ONTz536p0aXTRQYlNCRFOrH333ZZ9zuRK15yHorUX3fNyuVQqWIfx8p6cjnEnJOkQBi1SpT0qpvep_jeW7LvkXgHLIeWpNVUFAKSC__A9OHxxnl00Pi5vfrar7NgiCVJsT9X-AzIjn7I56w-eTX8QXVUkRFiFTOoEc27ulxQd_eecTksgqgjD4OOmeKLN9RsXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jpEspWEuwGOnxRO41ovbLTlkNlIIpOFK_5OIMqFTwYVrNsZejje5rTXGZQPeO9zMP-9eCumiQv6ewWuZPwzsj5J4Dp-KNxSFTW3aT_Zfp0E1Zc5qJ5A5qRMhtjLHqkunw6c8khuzL_dXw6SqTQsxE0QQtbk-Nlqb2-TzHNLIZchdFmMH_jNLBeuVYO_swdTP7ZWyv3L0XLT1cS_5Wl4rJqUk0Jh1ydG6ipD3vI0aYbYRamJutSrvDm7OUgd8Pg956wpOhKh9bmruz--9gKNPasu_S4N42IAMYoE5_rlBE_wTIiNEfBZIGmaLz9j6uagVSLDTUoQgJua9YnXf0JLFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6CZpgpcMhAgkg3tqAVQYrcb8YgE3Hicv8WlsGlP83iku4uo3EUaSGueh8yMV2DaB-wotmRkx6dwky1Jch4TEqGgge7dzNck5Sbd-8Rfa_QstqG-8g45BWr40w9xMMGRmjAgW87i-czYtqbaF2NRWEZBBFBkjTzJstVlLN1nR8cWDOuNrdj_CZ_6FbfeGIQrWj7QSa6kHngfVIWYqccgECtqivZWjYzwso09yxvX61myjL5KknQW_eqFAV_C9VMynVahQIw4bY8t9-5V1fjJsIgs-NXTnnkzE77nwL_OjoNNkSVoYPqFUaRhz-NDTYo4CkAjWepGCIKctHQwR3Ua1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YeXjRfctVzl8QwDjw7PByvT4WxLwZrH1XcaVcDn0DHdoQA4f2IkiB9yynslocc2dXV8ci8EYq6T_xlxxCp_FKFSZqW3ztMhtTbp6fHFa3f4--YnU0CQpmf7ISocIGYNCTfAywS2QbNXSU3ayTebJ6a5dFY_e_YtRbgx7vKRpLzU0NSNYs9Mv5_ygFqTiRIEaPJOuVu4gdFcN3Tpv_CtPJTMmZ_dtoeoYN9mDrCIX-hqRcRj6UGIZ0kmAjkhzfYizW8HmXky2eODGvT5N9rzXUUCMv8ZVc-Vrp_PALK0ZXLiTNrv-2HMm5Rhz1TIuJNsDamKvArLqqM4ekehAKwgA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qeZJosMX3mk8FuHziLZ5wJCOUBRwP9omTk4A8A89hXLWMr_a0O4x2Jbz_694H3q-V0gfaO0WRXIYZhz7-epQA9zb0qLFHfykRAThTyMYacPEayg_zLif5NBkTtofEpXVyJfy5Bi9JNoyBLlNv5Tf32-wc4NiPZQ9dXWnab6wPLUz6ZPnbwmINyfkuGfE5cp1ddJfjWVxgWdPcxjHmGVLpj4t8Zgbg0ReyZz1V9QVAW1Y4Bt1T_SwVJLyVz93dTT9I7WiJZ0bj3aOLhxF6OnC2KcHuu5XkTwStXuPinLF0fK_vvJ9woglOkddBgdfTUY7UAWmE9Xk5ho-blNgITBUiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDebcoi2T5lmeG6hEF3xOLvxAH8COhzYcrjSsOgPECkq7HVetK0Z5xBlgv5wpUKPaSfyunDoC2STXmAraOGSvrzXFYreAMybwpu8g-5ccL3JtMMiPyp4yzDHO5vbnjB5OyjnZW0VwdeEgzrJ0kyZVbyR9Q3exWwKSRgNczHUAAjf6Ovnzqf9GrqKUOmai4wP7-GvB2VrUFdzJjFceF47HOmPuE5_znwRsCqRT7UvXskHQ4be6x7qgj6LuHKvkOve0D5ef6VX5WDC-uRZH6tQEAgC6N7cZPf6Rbe7YsRvbrRNJ_eTh9QggGiK-ea3tDtJ7sYP1oLiE7Iop4ceIeOzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uy0qdRsm4hAM-dMNg5YgZl9EagaLOw1iE9Lhbjz9oZ2wK9butdGMmSYpgGM48SXFXhoJGT1gfeBSeFKvln-JiSASG9eoJ87TU9A_H6RziB6njFZ6WKjMRIiR_EmrFPaNrtp93Ar3t7X0I2bscH9m2R5j75PBg3uxMwks10DH-Cyzzm0ZUvH1IfE0PvYY6LU4isxZ7-JHsqxwofX5OU_kBQwgoRkvp4GrtpR3PxwIJ43X6IAb4xonu4CxxYVGJnux2jYtdGAL21Nf0iWblriLL03n2Idi_RfXfXkJr2S1UX-EIyojMmw2K0uk7Wg5tfHl_hQ1HoprdCHhcE401i1ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dnhN4PFFAvgA5d8TFurcknxu7vpx9lHcFmDlUQeqWXcbQIeYLrr2vmNC5EwrharN9ax219ss6b2pmwC8rKXiBufNx2jqA0EoFNUOHyVx5CxyIrdmqBO_8b6iNeEFw2EQdfYP5GWHNYqiritMx89n-sEDQsHPAuASfb9iIFF8BM8dl0O8BTIldcWPpwVoLtb_zfa6Owg978qLfw28xKyIWdgYMYMX-sIiV_2w5yLHtEL7X9jbL1N32rhz_mcMrILJ89DyxyBeRtEc2JIGKvp_05ph64RnRCqdMZI8raN9P448bQzYnsIaP5Z-pEqdn0gEvHaphzdUFpk477p_lPryhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/wBY2Nw4-eF-OOidjkIeGXdqKTFmEZv72tLM0S9GVThZHgkJvIe1J8-5VnrKvW27YuL3S1gZyC0IW9-dKSQmlZ3AloUpbpkPOsHNhknSIO6ZVMNnG4WMzPXzRz2OY6dtgoHoZAz3CF0rvUqSCRdFKL5p8cjqOzCOvG7NNHQI3Z5QeCpJ9YboGOLsww1POga8ajTc4IcpF0UmkQjAw9DJ8dpXz7yOO2ouVBo40txiekxDWb3I_WiBB_9JCF7hjibSL7cXiAd2x3t54PS1aIApsdC1SlENWDk48QNUV6r5gkadbjwOBA6r8sdHn78-hnLWzGHeB7NRUAMvJGTvkVOkDJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYrI4ZqSqWn71-A-InOSgcC9Vf6gEnedisIJyAMYpQ7FBC30edDtz4rvHDCvd6Ml3faNDx2ioEHyiVzYoUOiwTJF7dQlZuSH0agU8xLZy16cIqLDCuqE-PfPCInJFWGYTxRbwHJOAatUabEXUU6SvNnubbgX16Oi11858auT-98fag4ntSn4eqVoD7IWD7fSrUKip1OEtI7AgE278Ym1FedASMjnmZSoUgbZvdUnQsaMHY_HSaYQB8RTiumvXUlmbnCTvDTv9pnZ4l5-He3JS2i1UVhGtTs4xtzY6HglOE2mqC0AfxG6NJVxJZRRCHaEdMlpqJeDmj7Hb4GZ6KhoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-inkyOxXw4VIS5O0SNpUEtuyKkYMFa5tFjq15GSr4_3codQi9m3gWo8UprAbSRqJLz1L-hztxn6uSuDVeXC1qf68v4BRS2HogE_hJKLQKqI72JzeOZITfG_suQI1uvc_vlCuUnp7kz99365LEY80h5KUYcR0oYhLKFU8M2TDlDzpN4xanY25rc7CRQe74WEeMkYtXr-K_KXUoiCaelnG4Is8uBFXuQ-cZ70DUV1WDEoaI2se_bE1GKBmB7yejsqsClEg6a8vSopQSro6Vv8aNkBYiA8J3AHah1TRU9iJSr_F2Se5EH3Qj_s2apTtYwGo3Rd80V7VvSMyVp1k627Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
