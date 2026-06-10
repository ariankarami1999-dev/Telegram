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
<img src="https://cdn4.telesco.pe/file/dS6vHYsGDyfg8pavuCK7fg8NQ1tWp-euV6hrptJD9ta2EJ_PC5ehFCf_6QFyvapZpao35851s4_qx698UEYEw7YHVdaGj2_PRWjaxqhB-s8ucY_O1PPeiKbFbrerDF-87SeP-Oa8qhZJoTxyK55VEJH7hOtVnqFItX30NS5A7wHXTKUSafQ8bePM0BPKzBCBsZXcJWtJ1t-ykZtVjmd5REXycfPju6NvIcyDqh4IMDg8wkOUe0TJ8joEdqkTPKnBF7cvzKT6rqGc03uvmWWDbaAQBbdv-95z5KxOQE_hGdFWlkwQbmxCATsVWBKyq2OJQwMOm_Lmkqaekv_vam9etg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-133223">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⁉️
💢
صداوسیما: برخلاف اخبار منتشره، تاکنون خبر هدف قرار گرفتن منطقه پالایشگاهی عسلویه تایید نمی‌شود
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/133223" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133222">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=K5XvjnWzRI9ndOn6nwuhMTYgXQseXZ0RLXeRC2eVFx8ZnoOggtN78coF2Eih7ScZWvFQ1aRiQJK4CLYzH4FcCkqyLEsAIex_U8G73dt_TuDHfQYcWyGmw-3NLCL9p0DsBEoaUb7vUaYObFDuLSnrFHgeTV_J11GrJdBeW6MXsGlIMr59t7IcM2KT5EiBGd5AqVlAkJHCMgYxNKuhU5lbrjJNhvrL4pQlUM_UQJbx4xaJ9gmKfEXATGPEcsocSUZC123cZ5sZEez2P3CpJY8U-Y3Pq7_wybq-cL1Mu7tIsuC2FSQSx9xzWmFx7jzD3TSjz0CGVv3yL3UsoxfmH-9aeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=K5XvjnWzRI9ndOn6nwuhMTYgXQseXZ0RLXeRC2eVFx8ZnoOggtN78coF2Eih7ScZWvFQ1aRiQJK4CLYzH4FcCkqyLEsAIex_U8G73dt_TuDHfQYcWyGmw-3NLCL9p0DsBEoaUb7vUaYObFDuLSnrFHgeTV_J11GrJdBeW6MXsGlIMr59t7IcM2KT5EiBGd5AqVlAkJHCMgYxNKuhU5lbrjJNhvrL4pQlUM_UQJbx4xaJ9gmKfEXATGPEcsocSUZC123cZ5sZEez2P3CpJY8U-Y3Pq7_wybq-cL1Mu7tIsuC2FSQSx9xzWmFx7jzD3TSjz0CGVv3yL3UsoxfmH-9aeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/133222" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133221">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
حمله آمریکا به جزیره هنگام
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/133221" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133220">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز:
هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/133220" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/133217" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/133216" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| منابع عبری: تحرکات موشکی در ایران رصد شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133215" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
پیت هگست
: امشب شب شلوغی خواهد بود،
سنتکام تاسیسات ایران را بمباران خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133214" target="_blank">📅 00:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/SorkhTimes/133213" target="_blank">📅 00:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
🔹
سردار آزمون: نامردی در رسم رفاقت من نیست، من با این بچه‌ها نون و نمک خوردم. دوست دارم اگر روزی مُردم با عزت بمیرم افتخار می‌کنم ایرانی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/133212" target="_blank">📅 23:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
سردار آزمون از لیست بلند مدت ایران هم خط خورد و رسما دیگه به جام جهانی دعوت نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/133211" target="_blank">📅 23:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
#فوری | ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/133210" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/049d690382.mp4?token=jS7H3xZl2Vfp63BabfityQ5PNH8cW3s-_WweAqYrdCzJCuAn9snsg7dJ8OGb85mBVQ4EXh-vOtSrkigILak5gCxwaLT4Z7iqKvZTXGy_WRHACIuBzb6Zx3n-ppjg1jHzuSUvYeJWSWDFjNZYmxkfu6tqOUXdf8V5WUT5qxvQ_QCiCEvfLVI2CEgAMYaqj34GF5t__oJW-nMeZhNSOpM2xtqljkZLa7giOey3kDx9mZ5-CcRy-O-GRL5GI3TBSA80Xa8b6QxkQTDbDUYVhESxDvFH1ogxDzD8f1yTHL6funlkd5NKhKJhqfgFzDitScdg8t-sY_Ov3wYq5ooH5YUnwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/049d690382.mp4?token=jS7H3xZl2Vfp63BabfityQ5PNH8cW3s-_WweAqYrdCzJCuAn9snsg7dJ8OGb85mBVQ4EXh-vOtSrkigILak5gCxwaLT4Z7iqKvZTXGy_WRHACIuBzb6Zx3n-ppjg1jHzuSUvYeJWSWDFjNZYmxkfu6tqOUXdf8V5WUT5qxvQ_QCiCEvfLVI2CEgAMYaqj34GF5t__oJW-nMeZhNSOpM2xtqljkZLa7giOey3kDx9mZ5-CcRy-O-GRL5GI3TBSA80Xa8b6QxkQTDbDUYVhESxDvFH1ogxDzD8f1yTHL6funlkd5NKhKJhqfgFzDitScdg8t-sY_Ov3wYq5ooH5YUnwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133209" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوتبالی: مذاکرات پرسپولیس و هوادار برای انتقال امتیاز به مراحل نهایی رسیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133208" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_5IqqEgRVtC8hbfO-tpUk1O7-x1DObf4gkG84SVScs2pT9ltnsssBmv4yZ04o7LrGRZTbwbkFQTF9VKvpWqA3vPlGB0L2t6KRbNZ6egTEBOFseoFDB8Yl7ZSsBHxjaejZrH0ujrXwHi-rq5NTNBIsmXBQkvziL1UJKFjhKjT8IIuKr9WPyBRTHNYI81vSUykOoKt3-xUqoXctXAvDBZX9MImUBUwM4thmi_EqbrlI1sildlbhOsziWD_ibqRgwpfgCuG2fRaxZJiPwc61lQewI2eE2RtSI4gUW_WV2ujB0_T6aFG0rhGHRfRScgwBvLReRu9MwIR8QvOHr8J2aFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امید فهمی، وینگر سابق پرسپولیس و فعلی نساجی: در ۲۰ سالگی به پرسپولیس رفتم و قهرمان هم شدم. واقعیت این است که چیزی که در ذهنم باقی مانده، بازی کردن برای پرسپولیس است و هنوز حسرتش را دارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/133207" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
قول ویژه به علیپور برای ماندن در پرسپولیس:   امسال کاپیتانی!
🔴
#فرهیختگان:  مسئولان باشگاه پرسپولیس برای اینکه علیپور را راحت از دست ندهند در تماس با او پیشنهاد مالی خوبی را برای تمدید قرارداد مطرح کرده‌اند و حتی به علیپور قول بستن بازوبند کاپیتانی هم داده…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/133206" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤩
اوسمار دو سه روز از باشگاه زمان خواسته تا بتونه خانوادش رو برای برگشت قانع کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133205" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
اوسمار بامداد شنبه به تهران میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/133204" target="_blank">📅 22:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚽️
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/133203" target="_blank">📅 22:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb3041a14.mp4?token=qU7odVBrl_Nm1II0yt0FWXCd_bozNbWPjDXK-BkR4Nva6qIgRrBIpzhi5DFJahn_Vm1_Dovfw52icoy_V_3ozj8dRCnqkhBBklpS06QaOp6PpBRfzg1T1mJp91e-48vh84a2_Hv8yo5stER9oI--kLyNWcKId9dDbGMtkbZax5NJGKQ5nZO1ZCXH1TOzoj_juRzF_G81IDRRoKN089BSTbwB5V-VvAfI_erVSEZoh_q6jYaA2Cw2oi9Jj_VzpqOthzZTRZVl6TR2POx4LO_oM-AB6RaO2f0DMAb51qaqBxSNRuPHa2lXHpt6aD3egQnrkQBj_DqL30H_HNMiqR3QrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb3041a14.mp4?token=qU7odVBrl_Nm1II0yt0FWXCd_bozNbWPjDXK-BkR4Nva6qIgRrBIpzhi5DFJahn_Vm1_Dovfw52icoy_V_3ozj8dRCnqkhBBklpS06QaOp6PpBRfzg1T1mJp91e-48vh84a2_Hv8yo5stER9oI--kLyNWcKId9dDbGMtkbZax5NJGKQ5nZO1ZCXH1TOzoj_juRzF_G81IDRRoKN089BSTbwB5V-VvAfI_erVSEZoh_q6jYaA2Cw2oi9Jj_VzpqOthzZTRZVl6TR2POx4LO_oM-AB6RaO2f0DMAb51qaqBxSNRuPHa2lXHpt6aD3egQnrkQBj_DqL30H_HNMiqR3QrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
🎙
امیر قلعه نویی سرمربی تیم ملی: برخی بدون مطالعه می گویند جام جهانی با ۴۸ تیم آسان تر شده است اما به نظر من اتفاقا سخت تر هم شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/133202" target="_blank">📅 22:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133201">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiJvdde999Pnb_QH-SfB7LXYqC6RyBk7kNPHG2YwMnipBSuJ59_Ek7J1yFGM9WnvWcflUFtG3twLZX9P0i6pmA5YlYILPvl2d4rjCkQIoCuGEthaHIyNE8jIF0QCGasjTfCH8_COUM_gcVpf4MP9MRogzfuds4WOrCpSWXny4zYjLJADRcMUuo_eeuHH-vmV0iANyTt4cw7RCH3swgavk88Hhp2kNbW635xp3TQTelTleSZZxjo2D6eZGwzJtF420mIUZFZq913yBQKs6guJ8z6zLxQQCUgiv_5xhCGEPkOvg2bqxGrZjY2FotL3tzKXBuA0YlLKxOofAjOkvvdkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جواد خیابانی از صدا و سیما خداحافظی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133201" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133200">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13HU14EUlamKefoC0LiP9hUn4GnX7KH_CdB28noUk8dY1Pt9cq8Yqh0YcYwO314IQIKu9rAaYlxrRO6DoIQaiZOYy1o2jhqOLxPrDyzhLk_GLWgPEuZPJMy--N03i81-N_kZ7qy2mVCb4BvzwIj-rrqOzVePC0bmKI2AgH_Rwkk0RhAo_p223Faql6sksTFiiHHAIY97g6_tM-Kq4VKeTZYSHBqStxIIHOaok8FM4zGNgHc7naizkZUHrSSE6YWIRtSwW4FNv29YOpI4HVuanghpKom4ucL62b4hYoKcUJs8EWOCRa6V8UDtbKzX7e-AWZUjoAhmtXWVrTEz-Qglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133200" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
ترامپ: ما با بمب‌افکن‌های B-۲ به ایران حمله می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133198" target="_blank">📅 20:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133197" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
🔴
غایبان پرسپولیس در تورنمنت کسب سهمیه آسیا، پیام نیازمند، حسین کنعانی، میلاد محمدی، امیرحسین محمودی، علی علیپور، سرگیف و اورونوف هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/133196" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
ترامپ به فاکس نیوز : فرصت اینو داشتند توافق رو امضا کنند و زنده بمونن
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133195" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
شایعات؛ به باشگاه گفتن رای بازی گلگهر و چادرملو برمیگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133194" target="_blank">📅 20:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
دنیل گرا به ایران بازگشت  این بازیکن خارجی پس از حضور در تهران، خود را به کادر فنی پرسپولیس معرفی خواهد کرد و عصر امروز با حضور در محل تمرین، در اختیار کریم باقری قرار می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133193" target="_blank">📅 18:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
مراسم معارفه رضا جباری امروز در ورزشگاه درفشی فر تهران برگزار شد و او رسماً کارش را به عنوان استعداد یاب شروع کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133192" target="_blank">📅 18:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It8gupWyMWkRG4BWbeyPaw2EKLE1sQ_99sjoO4hp6MXyoXkzB46dzG8Q8ZS4u_TM3har2GzbVG77zV8as_lyhffiK3xqdSwBDoiCkvtg3Hw9yDST0Ppvj2MjE4WlVrmIMhPIOtKsNPZLEKC487aLCC8h-vZeK1dAOGb-nw9LRfOy0IZpcqve9jBvlaQnWMVJ8QonJBKd4NKDhXNIimO7LC0hLuW-tMz7yy2yRWAoPcI_GCqHx7cvW4pY_TOsXBoXnAgaolDy7ukEwPZjUaBbm6jEecdljxu7WCgKNep6VLCMUPJqCkdcK9p0bBN7rLMU_MtamA8wNMAIzW4Tn3OMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل از ایران به خاطر استفاده از نمادهای سیاسی تو فوتبال شکایت کرد.
❗️
168 تعداد شهادی مدرسه مینابه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133191" target="_blank">📅 18:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133190">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
دستیار اوسمار به تهران رسید
◽️
جولیانو والیم، مربی بدنساز اهل برزیل که قصد داشت راهی تهران شود و روز گذشته از عمان برای پرواز به تهران اقدام کرده بود در نهایت امروز وارد تهران شد.
◽️
این مربی از فردا در تمرینات سرخپوشان شرکت می کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133190" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIQQOGVHK0W8NZmlEPYb-6Y6vCZ_cq_GAOeJVkxWpK6Kb4FovtVxuMdnBiJ1CpdH6GahfxbM1AIj6sPoRb2i3EnhuSTD5jqmi0vhZhQ1thrZWEuHpSk-eTFY7_cs2kf-yoEhRoaM_YVkC-SPNZ7t2ZcyXWdDefsU-gK5gqnXg_Pj6kpIwDhMmF-jFn8nXbU3bQ4QnN0WWyp_-G_5GX8PzQCt_uJkju7VLfyXyC-pGt4Z9H8sO4aK5IXjEgOPzu6oLcH1fbVlcvFL0HGCW4D7qX3lsp3fhj0N3MNaokcH-XHQqBhoRKocZtTj7t4que0hKZfp4ULHjxQiOuxjtgydjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
💙
وکیل یاسر آسانی اعلام کرد در صورتی که باشگاه استقلال تا ۷ روز آینده مطالبات این بازیکن را پرداخت نکند، قرارداد فسخ خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/133189" target="_blank">📅 18:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
فرهیختگان: پرسپولیس دنبال درخشش اورونوف برای فروشش با رقم سنگین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133188" target="_blank">📅 17:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133187" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
🚨
اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده!
🚫
ترامپ بعد از سقوط بالگرد و حملات دیشب ایران بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133185" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133184" target="_blank">📅 16:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚡️
⚡️
حدادی: دفاع راست اولویت علیجانوف بود صحبت کردیم گفتن 800 هزار تا 650 هزار دلار پایین آوردیم یه سری اتفاقات افتاد بنده قرار بود برم ازبکستان گفتن تردید داریم باشگاه بتونه کل پول رو برا همین خواستم برم ازبکستان که پولو بهشون بدم قبول کردن پاختاکور گفت چون…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133183" target="_blank">📅 15:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
#فوری | به ادعاهای رسانه های عبری تصمیم ترامپ برای حمله به پل ها و زیرساخت ایران قطعی است./انصار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133182" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133181" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlQIglvOmnBxjnMCOou332LgEbA1pAJPI94yDGySWTPgrfqSc4Q1j4a6W7zyMyu6MU1baBjlqVhnYX4mrMcZ0WuTLrBDcwerzgy8SsPcrxiXTHT4FI3Wv79nMvIQUdMTYPWzTfl6c__LZtiZS3YpuS0n8IsggqkvLoMynnfd6UpUk0HvGBkyLOrID5CM14TCI1CE3buNyCu1jcuIFfq3XuB9G4miBA0BPJjrteVyKH9RMx5jhMulVJQO6zIw_Sr06W1XC1kODgRUUp9BthfbJjpK7LhBuF9JINtMZcoMKQy4hDigzGMdaxpEuEisW0HTKnv3HdRBtv2kIf7EMSEL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133180" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133179" target="_blank">📅 14:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
اسمار ویرا سرمربی پرسپولیس بامداد شنبه به ایران می‌رسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133178" target="_blank">📅 14:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyFHjaUHrf9o5SGAyCW_Q131QAWrLDt7NpcrBDCYxEOCqnZEzJRpAipHXAGYJTZ6NZGa4yfx_gAxshsi67XObiHjVlyCr6wupDh6cOWlABTlJ33LWQGeaASSGSK3UNCyh-WnxXdb5rYPRB_TDX2FIr8aJN_1se_V5lLlw-oWqsdppTCGvfZ7wcBtGmbioylTv6qsEHjUA8sCaHYfkNph_Av0HjCrhzhNozUGoiggru-d-GYHnXVKEPuMsxA8HLBdT2N0BpeJ8ZqK0wD68MUfTFd48pxAZa3uOfOuMnl8JfC_G1G8EqMdbIm3SFdOltPHZKqqSXc_CAQ0H5YxtsET-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133177" target="_blank">📅 13:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133176" target="_blank">📅 13:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
وجود اعلام AFC، پرسپولیس، چادرملو و گل گهر برای آسیایی شدن همچنان شانس دارند/ معرفی سومین نماینده ایران تا ۹ تیرماه
⚪️
در شرایطی که کنفدراسیون فوتبال آسیا دقایقی پیش اعلام کرد که تیم فوتبال گل گهر سیرجان سویمن نماینده ایران در فصل اینده مسابقات آسیایی  است…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133175" target="_blank">📅 13:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133174" target="_blank">📅 12:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-d4UHCee8mUd5BNgmb1tcuBu9ve7NdrINNL_8qRWDDO9Muk5eGRB6rMF9OLqJIvvqUTUIudoZ_XsRDBcdy7do6DtdpWsxezeofwH4ncelXICM2ag6CW0O-01umzxR6wQJ5NdKUNcPsAfPUwtY0zWr2WBUFIcN6It4beIrwqT9X-xE_9EKxykO_NgDy-xK1_b-cKelsyXYxXD9Tivq50RqptXbQ-89h0s7jGMFwTBmB36TweHgryvxvAZ3lyZ-GyH8wu7-lWNbCOflifkLuKKt5FzbH8TkxrwojtSBWP_gdWzdsjQc-GRTMPUBJdEdZ54P5qreY_om-yHMg1biVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خاورمیانه واقعا عجیبه
‼️
🔴
افغانستان و پاکستان که دیشب باهم جنگ داشتن، امروز بازی دوستانه دارن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133173" target="_blank">📅 11:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdMK0ddI3NaeBmsspm0iHw9Sl0_z8KMF1CW3w-A4tE-EuToG3CFk4Pmz1DxwFr8dH-OBuMX8BNhELZe2p9JhBBKu7g14MCVBX5KxSJF4FSMw59BXCimZBi5scHWCLVBP3mJEoL_JeWTi7F51Z0STtBHl2R3fs8oT7TA-1aB9T5BBt8vmd5LJFRok1Ra1qfmfm6sHBD-vq2qeVyICjnhCz7c7NGX0t5wFqJMucGBmhAw_x3-X07FweY36g1IWeNo07frndY6GK05KuZJEuTupndDmhEeVvQCtLaYHd_TSdefyq1NQz1WuS9YX5zPF4zChrV50Mm1JyN6H7g-udPLpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133172" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133171" target="_blank">📅 11:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133170" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
اینترنت بین الملل در آستانه بازگشت به وضعیت پیش از جنگ؟
❗️
رشیدی کوچی: اینترنت این هفته به حالت قبل بر می‌گردد، یا ۴۸ ساعت آینده یا تا پایان هفته!
🔴
جلال رشیدی کوچی در واکنش به زمزمه های اتصال دوباره اینترنت بین‌الملل طی ساعت‌های آینده:
🔹
من فکر می‌کنم در…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133169" target="_blank">📅 11:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133168" target="_blank">📅 11:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133167" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYThtLiS4sAj4UOtil5I4G4iCR7vGLS9Q1MCUzYLjAPGDFuZIb7O_4dmePhfiEZTKjNheD6tq3LCA_tRF5SSqFTjB65fweDCCebsPy-S2s_n5XQ9k2qOV0MCpr34BW1kly1B8YvskDqH7C308BeIvCk5yCFjesAVOGVzb-635tkINR-K4DJCZ7K2ceS39jPPXVLDy8kQN_lTR_uLXlZ6ypgZG_qRb3Z0yjn7XnDWHdOrk7sX5BkwLLKCGb6NMK8_mDScTLAJZ__fe3Znx96kVpmy4KmRBb0P6wvaWfTH-dvitL-dZVTyw97Ten4Dj7gk5VmqT5VclAh0RtE7TjtT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووری؛ پیام صادقیان بازیکن سابق پرسپولیس که به ترکیه پناهنده شده بود به ایران بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133166" target="_blank">📅 10:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133165" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133164" target="_blank">📅 10:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmZYSQX2KhprWoouVrVa9VWgwygoAB_IVnDwaIYTivIcm_SAcWtRQNXx2UwjiRp5IEmaIJt8qDbbXA2e2tffOaH8x7poGdWInkaA0GHwhjQuizAo6OqPSiS0ddP6vUet6ohxqmHmcWC7P08V3kV81Nh8XlR6XypvraJ2R01QZmu0Jj5RUFUsY9XXrq3KFLmNuO1wim58VCPsLzxYNK5uRDBY66Ty48Xl2jgRSgfXBZFbe4og627fKM_R0GbhlNSHQQjsmRVZdGg2AgKUROuTLrjIRnmE6xVfk45oKMMlkfcmp39OZoEPE6M7OaSDQ9oMWr6KA7j5tXKq2UBEValOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهروز رهبری‌فرد: درست است که همسن و سال‌های من به تیم ملی دعوت شدند ولی با ۷ امتیاز صعود می‌کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133163" target="_blank">📅 10:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
#فوری؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133162" target="_blank">📅 09:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMsdxdM0U9B6H9A830h-FH19bL_UaZSc1XzieHXGubzzNwtQkTHiRvG9yo7T1juC_06BqR9TuHptMFqwoMfgC461Hc7p7TvtKHy1WjpX3SUhD0fR0AGa7siDha6nMLxMz1x5VNERx7goE6Fb2-h3_pQrUUKAyqYGsvS0M5rDRRGaKSfmgPnuIuUm99dKR98ccjY3XDAF2fSv6QemD-cjBHfwcHGR0AzNReEKVqDlHsKZfugpL9RCSiDJMvUn8WJvQR4M8NxAF0qM-BeGtu7rVAPaemVS0YLZQP3YjdRj0n9KPh-pAFjRLQdJduKO-_CjtEcGqYgv0V1yF9RRQDB7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133161" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIRX5Q5__jkFePu1KXlKc280xuw4I650A9-83Evs9Yf7yWi-AFLFfDnKL-D6eTZMyXLZ7HpzsiFC3jVSpn9TPwpM1hlIS7Vom_gwcVY60lw7_0le2MQ2ljcD-1r5EX_7NAFQ8VgbiKEmqF-JtwTP_-oDfYEUo33fHU-BydMa8xMMD70u7XeOzv0lAsWNj4-iOVrEUUNzNeQBmv8SAgZqAHZvNl0wEAOhCtNoCby8E7z3CgP_6yQgWNELjh-IpyAqDXvic_H3n-U98Q5f0i1ISrBIrGODGv5w3sGSpmz3BY4CmrXDrUESNICa3lUDGSXELjQh9K1akAck65jknG3M_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133160" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| پهپادهای ایرانی در حریم هوایی عراق به سمت اهداف خود در حرکت هستند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133159" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
#فوری
| مقام آمریکایی:
🔻
هدف از حملات آمریکا ارسال پیام هشدار به ایران است
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133158" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
#فوری
| گزارش‌ها از انفجار در بحرین
‼️
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133157" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
#فوری | حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133156" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
#فوری
| آکسیوس به نقل از یک مقام آمریکایی:
❌
نیروهای آمریکایی به چندین سامانه پدافند هوایی و راداری ایران در مجاورت تنگه هرمز حمله کردند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133155" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
#فوری
| حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133154" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
شایعات،فهرست اولیه اهداف آمریکا:
– پایگاه دریایی راهبر سیریک
– پایگاه دریایی ولایت جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133153" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=QtWUkbIDDbQ2i1rS3T5q7regQ7H-B612iSHefo8dQSmrnNtkVRXXH3XpFjXNbqgBErvo5RBEdqYYN5ahvFl5hC9AgaRAwZvvbLo15go3hZ1_4SPScxPbdl1aurd2d1dbiMFD0k_mqnTFC2d9ou4FnOm4BIaC0pt0nyQG1PFqfdabQpvOjMEEP1MyKh2XsHNOxxQAHpcD6RlKwfFihqUYGXZYaGW89ZvAUqM9Vs5V5sFFLSXjbUj1l_Dx2RGxRx2_eyrqfCGX-ZrtvJsHBPZHIn-ihDaYsNG5x1vvGZy-7N6w6B63AAJ8p-XQoayR8WFiIuSLNILDg5VRsFIm-u4k-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=QtWUkbIDDbQ2i1rS3T5q7regQ7H-B612iSHefo8dQSmrnNtkVRXXH3XpFjXNbqgBErvo5RBEdqYYN5ahvFl5hC9AgaRAwZvvbLo15go3hZ1_4SPScxPbdl1aurd2d1dbiMFD0k_mqnTFC2d9ou4FnOm4BIaC0pt0nyQG1PFqfdabQpvOjMEEP1MyKh2XsHNOxxQAHpcD6RlKwfFihqUYGXZYaGW89ZvAUqM9Vs5V5sFFLSXjbUj1l_Dx2RGxRx2_eyrqfCGX-ZrtvJsHBPZHIn-ihDaYsNG5x1vvGZy-7N6w6B63AAJ8p-XQoayR8WFiIuSLNILDg5VRsFIm-u4k-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
سوپر گل کریس رونالدو به الخلیج برنده جایزه بهترین گل فصل لیگ عربستان شد
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133152" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133151" target="_blank">📅 23:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
🚨
#فوری | پیر دوسی، خبرنگار ارشد فاکس نیوز در کاخ سفید: ترامپ در حال برنامه‌ریزی چیزی بزرگ و مهم تو ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133150" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133149" target="_blank">📅 23:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133148" target="_blank">📅 23:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJfd6nLT1EMmagWkon1OBfBdePC4PQMvveFxEzUhElCp9qJPK4qdA5gH3hD-qdV7QrM_M7mdlxOsC5Xa7HMdxTnzp1Ts2HipQLDmZMJLJpkobHXcOj-AeaTUz-LnUSGF43CNLSduPxzP_TT3FhhQ80YSJIbm4LMxjrz0iRtz3QAsD6m8DJnJr58Mga-AvG2qY9ZjyfEcPIOsZ7vlhFHdeijIdgXgU91I4PRlWNzFhTRF4sajIjDR6EuhlGn9uaeVbJbW502d-49KIqBOaIgPsiH9qeQnpbCof_wEtll-iXSOYUyVhH1Zx-7qf5umprcgOE5R7yiUvCe7i0sEA7Lkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا
/
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133147" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
فاکس نیوز: ترامپ می‌خواهد دستور انفجاری بزرگ در ایران را بدهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133146" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlbHw4ww7errI6pFihU-xCIFLu5w3HJ9lghC4m_vz-A7fzF-DU96xP5ZH1xIgJueoJW3TQnXdnMLkgdybKej9NfQqvlnkcSee6236wQt9Q_Np7DEIjhOEVMFFqwhkIGkXfOVU80wdONHab1c_8X4lcZQuDPJj-dkA5OiBCNRC2ZNrog32U83wJt_BiIqmZ8v46G0KLO4Spx1xFol7Lu8sM8xLvAFopcSjegqr8AfGpNKmHoTcy64M0T1WU3G1omA3p_E9lr681c-ekPXWPFdi7ZNPieVXwXIIT_wInG8V9UtNyhLRn5iVKkUKg79FaEhI65BqJSIF3lw-8F6cyyOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
|  پیت هگست، وزیرجنگ آمریکا هم پست ترامپ رو داخل صفحه خودش منتشر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133145" target="_blank">📅 23:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133143" target="_blank">📅 22:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133142" target="_blank">📅 22:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
رسانه‌ "چمپیونات ازبکستان" در گزارشی اعلام کرد، جلال الدین ماشاریپوف که در بهمن زانوی خودرا جراحی کرد و تلاش زیادی کرد به جام‌ جهانی برسد به‌دلیل عدم‌ آمادگی این رقابت‌ ها را از دست داد و یک بازیکن دیگر جای او را در لیست ازبکستان خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133141" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA-T3KZBgrIXduo89O532Iid78UNjXu4Gr-QXPTc_38Y9pO2qm6fsuduAeF5lcGHUTx0HH8aKn-OxubKed5bAHdIwyZdkx_w7rFmzrMpeoEzXyUoyOgqUE0LxwmSUXsR_byAFiyij6XR09DRXneKt-lYenvedHTkv6wOif50SQMUV3rI-Ge1Nphk-JCe2CEFoxYYZF7x8rdLjKbE5Cai0GJNfVrVZ7e532Q2LptA5cnQjTCatuvquy-0cTuvYJvS77LdAZ_skwe6VtO--dzDL0pIv9974V25ObXYUSLufah0LWfxVd5T8L-xYY-Bb0IHsqQRikZXkMDd1WwPpeZIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان: بالگرد آپاچی توسط پهپاد شاهد پرپر شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133140" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔵
⚪️
افسری(سرپرست گل‌گهر)
:
◻️
ما نماینده‌ی ایران در آسیاییم و توی هیچ تورنومنتی هم شرکت نمیکنیم و اگر هم غیر این بشه ، شکایت میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133138" target="_blank">📅 20:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcbUVU8FXl9n3GF2lErvm-hNaR1BBa6X-G5P31Sn2NgXO7vmk-UuezxbpgCQGx1gM1ggka_bv0FB_D_CvqwyXdScodAzjToI0Yglfpur4pTXTdeS_Ismi9-YhuiFYD_WdDhhf6lzeCY0I8S2tFiXfbpixyiM0aMjp2bP4PP9HsQFlgM49CNNptXoj3N-kPuBQbq6OlSpEgn2OpEjnxzP9vQCdYVKrVFeOMmkVHxDJjsssh2tPeU87Ilikvrdi-v3RI7IkeyW-T-MvklsEe1tsuzWi8YNii9hMnFI65QWCBTws-mBBm726lvvvynqPZdxJ3beGb6EUKhgK_VMe_R8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
تنها ۲ روز تا شروع بزرگترین تورنومنت فوتبال باقی مانده، رقابت‌های جام‌جهانی ۲۰۲۶ رو در سایت معتبر
اسپورت نود
با بیشترین آپشن و بالاترین ضرایب، همین حالا پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133137" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_2ytRIC_UJgVqriL9MCcFde4gi6EgkpyX6_48W7l-ioILXOuN08sQ7Ac1KNOyTLW70eXpFgmModTKWHb-RVIjIuQwBpDAeEY6mQEnxjY_BLHKrSYwY5KnP0Xz2lG9obXyTbHyCM-yj1e3ORlTVApG25-PY0ZdgWms9pyuamBDE6nNQUgmz6DaZKav-_BfevhGaWhgZiZSbrbaJyNU_OjNauVDzuXLo4HB0PFa4i9Q_E2UBfzhx4nDbTZjV976jryM6IAAafmj-oBLZaY6bApJUuiYLoxhS21UMSiz2Q2rxb7Z8_34HgaAfrVfO9nXnkJQliL7h6Iyuo3dE2xRTOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133136" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rn6lGa7NY4wHus3fxOjy2AgLeArUutFH6FyTwux2u0S8OGEof71Y63bCIPpGPndXcJN21PYYEuCjRDnROvAGyJaobrAJCiJx-ff4ebkKiQSb6YHk_NlLEDwudSCPRrcs6FL4EhYgv_h9VahoNgueG3uXWrQBJzrs3GZPE8P_YEqsQwoEoeXHoqFrqek-Rw8H1d0sTOIYi5wIUponUlDMwpLAD0OKttM63GUZL2JNcbEBEw71iMKk9XV7HznQgXIdqjBZvitmIPJSBMdBZC1_xsQkHKWa0W6wmcA8Qg5PNaVTcnPHATwQhjpdKiz9k5H9b_5mg-lFl4kX9hFLcKZTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال افزایش سهم بانک شهر در مالکیت پرسپولیس
◻️
بانک شهر پس از واگذاری باشگاه پرسپولیس، با دریافت امانی سهام ۳ بانک دیگر (اقتصاد نوین، رفاه و صادرات) سهمش را از ۳۰٪ به ۴۵٪ رساند و سهام‌دار اصلی شد. حالا خبرهایی منتشر شده که این بانک قصد دارد سهام بیشتری از اعضای کنسرسیوم، از جمله ۵٪ سهام بانک صادرات، را خریداری کند تا کنترل و نقش تصمیم‌گیری‌اش در پرسپولیس بیشتر شود. با این حال، هنوز هیچ تأیید رسمی درباره این تغییرات منتشر نشده است
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133135" target="_blank">📅 20:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133133" target="_blank">📅 18:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8YdD52NOfFt13Es9HaHZUeA1ooPM7Jg76oQYCEyERoBDxQop7OBfiKliKmNbqFABWDJHIZ8EkrZ-X09DDEdyumJkuCQG0hPWn2Wl5IgWb8DvjtfcAVsPCokj0EWf3LjQed0VUH0Gf-ruDg567fwj5-pCqedSasRFiDGwNLf-UGd26j5Eo53sEka057pVcYOELjq36YRicFp0u4TdAmiaFfZ0Hyk4U2Tti_u6P2qUOv_qHQK_6yArVG_z3bOlrrA468KfKi74K3B4ZTOKX_6o6kHlFajtsgkzQTQVffq03YZ6c6PiJ3G7bR0kZUqoJTVX-Je17aNKbsYz4sx_THezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133132" target="_blank">📅 18:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
💢
مدیرای باشگاه هنوز نتونستن با سروش برای اوردنش به تمرینات ارتباط برقرار کنن.
🔴
این درحالیه که سروش بیشتر مبلغ قراردادشو دریافت کرده و کلا 10 درصد طلب داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133131" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
مطرح‌ترین غایبین لیست تیم ملی: سردار آزمون، احمد نوراللهی، الهیار صیادمنش، علی قلیزاده و محمدجواد حسین‌نژاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133130" target="_blank">📅 18:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
🖍
غایبان احتمالی پرسپولیس در صورت برگزاری تورنمنت سه جانبه برای کسب سهمیه سطح دو آسیا
▪️
ارونوف
▪️
سرگیف
▪️
علیپور
▪️
کنعانی
▪️
محمودی
▪️
سروش رفیعی
▪️
میلاد محمدی
▪️
پیام نیازمند
▪️
دنیل گرا
▪️
تیوی بیفوما
▪️
مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133129" target="_blank">📅 18:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#شفاف_سازی
❌
از بیخ و بن این خبر غلطه تاکید میکنم پیمان حدادی هیچگونه جلسه ای چه در رابطه با سرپرستی و چه در خصوص تبلیغات از این دست موارد با خداداد عزیزی نداشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133128" target="_blank">📅 18:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133127" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133126" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/133125" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133124" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDBVBgfp6BFjVVLKrtfGn57L5M-fwRYWZ6e5_auT0z4y01M5WSRkgE82FuM2E1SMujq1E76SihrYKv5WJWAs0Wmp5KHiVUjenVPzc9yIaB0MwpfXNHD1kRaoLecz13Z8Qo1O6QrHgmNmvyf-eZkudrXKkZkYqBDyjKC6wLEHkXduBdQYuYNNQ8s8cOHKhJLLVPhsfB80j1ezYuPdBcukEeJFfC8CUY_wOXLUA8VI_AM-TpnzbStwJni49AI5S5jkTRHFEGV4jFCNk4IDegGBxziY3q5F9v9bD36jExZeauAcVvbCfT_5b8s-LuInMTA_jJW9vpxV0fV4y6tGi--g4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133123" target="_blank">📅 16:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با تایید مسئولان باشگاه پرسپولیس کسری طاهری مورد توجه باشگاه پرسپولیس قراره گرفته است مکاتباتی هم با باشگاه روبین کازان انجام شده؛ و قرار است در هفته های آتی جلساتی با ایجنت کسری طاهری برگزار بشود!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133122" target="_blank">📅 16:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
یاسین سلمانی با عذرخواهی از هواداران به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133121" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب تر هم بهتر بازی کنیم یک فصل جدید و نوین باید رقم بزنیم و دیگر نمیشود با بازیکنان سن بالا مسیر را ادامه داد...
♦️
اگر بخواهیم قوی تر ظاهر بشویم نیاز به یک رنسانس بسیار مهم داریم که باید مدیریت و سرمربی تیم روی این قضیه حساس باشند و مسیر از فرتوت شدن به جوان شدن تغییر بدهند موضوعی که خیلی ضروری میباشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133119" target="_blank">📅 16:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhvVrMmZ6r9-nz5JfdpBSKVN06PEabzJvsQ861v6MYu1J4O637wXs3XM8i_oDymviEVtLFlOBu9MsIM7mx16IVgyvjqUByCFuMBY11Ay-KbBk7Xtx6TdMy1KssfYmK9p450NixoJnOw_L9TKH9X0hBBFsVFkl7ezYZn2pkFZdf69KXDaASbK63305dOlQjyLQQgxEFOjrrsoAhV7p7L-25i6gooY5Y6pQjtq8RlKgQpQ8KeJSTXTP2mkGS0CG_P7lRIxtrtYEJKe8njOhscxABTvEvWkDNTVvYgFez0XvDJYnMv_uAp8TyRMOHJjlAZPFaah7_90ioU1Y8weRjM-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دستیار اوسمار به تهران رسید
◽️
جولیانو والیم، مربی بدنساز اهل برزیل که قصد داشت راهی تهران شود و روز گذشته از عمان برای پرواز به تهران اقدام کرده بود در نهایت امروز وارد تهران شد.
◽️
این مربی از فردا در تمرینات سرخپوشان شرکت می کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133118" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8C8S6AtJ15X97tE3WHPwBBfdizTiKnnbPd0uo8BGtNS0rNqxJqdM5L40Jg4CcRzidvTUmPGL--xRXhEwh0K3iGgk7PFkZuXnHMlv_5Gux2WnEzakSODZmSHk3_te0QV8n3C12QibcYAOZp5xDuy0dB2ynXIjtxHzQHYbqPGewXSAGKwlEnlB_H2hQSTy-6GjXPOCGFT3TXHMfMmQFiooZMsyFYxYaa8y30zJenW01XWG6tQ7WLDz3iLjNPTfhWEyZrP66eUUb9PWFeTeiiGNf3EmDZsKqeWc-GZ4QnqgDD0THkglc0PIl3RyslUJPFNMbqwlFHKxQutBsu9q8qANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133117" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
فوری : یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس: وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ ، رفع فیلتر یوتیوب  هم در دستور کار بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133116" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
