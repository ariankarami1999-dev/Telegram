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
<img src="https://cdn4.telesco.pe/file/Z37a9DRXh6UxHrlp9BlJVFK0TS3DPLEaBViAkcr9kkYcWxU5BQYIhiyguRLk8i0jBZ-MjDaKBc1Lr5FS-XXJeOb7iXCid4_C2PKrlXlB4AV6U33Moy7dmCFz8_uK9d19SS5En3mZ3QdKizApCFbNTyCSIv7ALGFjX18PL9gkF9WR1PYKrp1917fSiz-_TRjp03bj9DkPLbO3lES0mEhIpkweZ6f8B1MyB-umZ1pSaLjDw8ej2bLTfKlG0eEnayh0E2lJA-lR3xg8tI86kObMgQOJRbNZ2EjcNUTvq5bEKNtLyL6dBA-LsVon3iqh4NoSwyM4Vm3qPhFV-gFq7xcSgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 376 · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfxOqXzf5gdw5qElWX-dRzzQFgBoxxBuyvllDEOnuNaJhXsSH1DVAd5rSdnW54ob3AzxvZEcUeqsihzK_0kWYmiMPMP0wavBVeJPw6Ng23Qcrn_Bg_Z0S6ugo1Tr0pJVyZS1kuqLYlK1lrMQ0rMA1Owbgjz0lGI4lMA9Szwgqlf8r-6Y0FLKeQ1YfVfsaMFR3i2QrvuFvmYR3yqdDWoPpen472uiUD7xVDG7_BI123Xk6if2Uk2DFa_KLrmJM7eThrYq55Fw-JdbzdpGURMopLwxWRbykPa5OS1G9K4wJSCmR8IJnDVZEOLvE6muumPWGkHndKn5CKg3zCo374K-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 435 · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 745 · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwVy40eDErVQW-ZZQbmJ3aKCR8ZNZPxCMrUtdAlPz2IJCYeN7cs6IvoMOaQCGme6Lv356F_XEzVzLCZOYB9oTLACroQt_KnxRwD4Rbpk4tFhQEbzfIkBVm6qM9prc-NlO5ivgZLHBKTxyKmllHowokBRNC8x5L0ap5QPwH65FV2B6CZ590MgEBXkGKE1EQV2k0ffuTVgaRULgQgOABseLN46ltitZxquQaodJOsm0OlfvBvxAeL5YNDUw0Z76_kO3X8j9zi8qNHNwHQc6T3lGBnIvrwPHouNc2eMNx3_G3lNYUXSYj_ZN_-bKDA3NFiCMDVEJtVGT0kFe_HIKkF_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJ9aNCpAbvr5sFVvv9bkk_JB7Di9YxOxVS49lxA9aoGSfSabgphxLKT1uMC63kWVg3UyqKA7VvLWQBtr0qZRVQe4ER1UVH4m-x7iMFYGWKqXLUIPbjKv4vs-y8r8X5lauLyrRcBHcDEvZ_5dwugWBFkqG7k1shfPGM5ZI1QbazhW1WmsSZHFIyTddE_IQuAIE7HaCH-8BSCJ52nK_4BXi5oenMmoW4GJEpZ3JNnxVoPoqN9hJzZWOoIH12KEJEaNtQqUgq9yuDzLUqjrjvUDhwBb9_3YkiaYM24wauV5grETOEKaQAk6hoOF4o94x79U8qkEPSqSwSaaYrXnQlQ27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4EEEbgAlqcHNjkCVX6N_cmN50quYiJnYSzxgAx1DVRKQDNyA3nzJS8CQBOB1H8Fn7ohrs0ghjMB2MPIHcRuqvLB2U7OVCcKalsfB1BiBEWvy_zitHXR48XZS_Rj9qnU8It4NQmmmF10ANQ7-zedK0_KntzFzYUwwlqoY_dYKMnhnb5WTCSkAAtu7A7WfqS1d15_ivRQR84IZxAtRzAtioplZIciMxCtY8W-_0a_Ri0H_MND8V_XhjWBTN0LmmLOBD2k-ujoWyDuBeLwxPiTvawMaOgB2Btui9OLEgWV83Y_H1i8JBG80rTMqZGAFAVnl_OBSOxMKOgHjZfC3GsdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U13G4b1AVJqAEq7cThbHgAvDXEckcOce214mbOXgDe7ickDqufFnCYNu43tA1GDuHtEhjbR5_GF1WGqRKGBsXWF-QmAueDOuiJbk-r2aX4oTiBgQsrCq1Kg9QhbMsFC2qGqi8ZXV43ec9o15nEUx12p-heP9BXkoZzT6yz3saqZJ1LC6rzOX4f1O4CuBBwWbApV_hl2XffWVxbeODyJhz70qXEag9CSPETYf91v0ITjZj7vfmHm8zJzaEndHhuq8FS8sQv-zIxWT_DIXrpQfz7r1ejZoRh8D44Jt0HjITT8etiGvY9PRSR7g4gKc7kQwPEY45WvMe0uaZYvGOC14DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxmqW4zZ_Vdhy1Mo8WGx3pCJZolq7Ccyo6-eUU55V0l1JGuuQExhGabBqt7G6WKqaYmJF3rviSPQj832cYgVTceWfbsJfEd9Zi1S-_QAVchdm6COVPw43uP-V5hB0HvLqLVX2UOO6jj6_aU_ThDiVn0k9WG4dL6zTThR7fcX0MGN0ziOFQRT8Ma5snzlGYd9aSo5hZj_H33lJe1z7KwvmbR8SJcLTdY_Zh1OejNEA69oheFAAtnf5b2BYh4mll24qfRC5JmKAi2eYF4QFMcCEyIgGcUanvM0FHXYFatj6YPn2csekKxK6mP55FZo3SRC9YEGhihiSWyuePuOvN9zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1jSBM2YaPHnfmUz9ZUxG2pUYZygQZRS23eHFzLLHAea5qzfDK47IXq5qmJ4w5BvCnqPpxYpV4h3vJx_vBSkH9zjxenTLhVeaNuVG0_52PwUWgOUL9zdBHgwSO-lcUZ0rCFvWr8_a3YtFuBiFLRjOVj9iyO3zbOOXLfW5jo70tba_LlfmXx4k3K2Ml6XMihl1hOSHRewDWq3xhDFCFqbdxvNYdmOWfuJ69xbwTeFs0kZ9ydu5zG-RFm_wfrkvaq9VXDjxqniC-v63n3E-MrEgBCUoj9fMVOFOQ2Sonl5biamXa3cSc6fvbY-hBqztdmybY9zWTWg8I-ddJlMd9rEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6BgPBMHShSg3e6Dz-7zK35-OjAO9P9SWogLS0FygrGuoX7ZfpeslapryfRdCkQ3N2Y-L8jAMje-oNM7jN9p2aeHojoRK1QOfUp79-NiZJjUPUsUFQ2equlyOlHID5p1BB-AJwMNExcfqol1ZyIOcO1SiFuz2m6HXQuTUl53aafBpar4GSOyQ96pWxYUOaNhRzkR6g7CnL2ZzjA2gbUXc5xDU-ES-PEpvCgeH99ApjE-LbYRzg971E1YMtYyFLmFbiOuLAibH7y4FkCZc0bFzSQ3qsPTGiHR6dJ2HSRle4gK3OuE4oiIf4tcFfXAXiSceg5oY2zg9dAiCGl_JkS0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or9uiw14GGC2igPcAzDNpBsNKSXHyo44bX2P9n8gjomdCfeqlBL02vBYhuq-kiwLTgPQd7NFxnqGWz4VM8Svhfz2WVyQ7Bi-UI7kHcO7aihPyflVWWHSZecjDAthe-qd7xJ1OxtlYjyBN9cIcbUl5gdTOa2e2cCCrHCm_p5qkYy-K_GCm-hRW9pUL2Aty64JuKEUN4Ifk0nKyf080wpCkC3lOkV1llaKswKWoTbK_QLiHkweK2H3FLert3kdB5LtKxlYaft6rEW0Cw6IuQGpQdEB2vn_AGqABI3a-gco8-cCZHInFB9gM8bLc11Zr3Y4hTIBqA9a5VfhtMU1LAfyPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡
اجرای سریع‌تر و مصرف رم کمتر
•
🛠️
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqGnd-qP9-EqtNSSJS_fjYNg4B3SA0HMbs5qJE1m0-FcBeT7lnFLKTHwymRP_lsnHh5Oq4_sioRsrbZfVAr4L8As8gPcQA48dKvWb-w50XdybkW8bzE72pm-82WkQPagEpHKkfUAsU0DXViPXeKHailcqcE8Gc8snEjvT-FdKgCspgJar6JdBnH7MEZB5_XxU5VSy55EPhXnw4AhiLgHWWMkwVh1iLgRWk5eTAxJV-TlaeyjFRqADFkWisLIFxYFBnzdBZpbUhP_tN1QmmbH6hmPUWDzwF8UK0OAFVCFJ1pXcIAEM9VLJQMt3oor2pKH9L16lxwuOtqP-GnDeprHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuKitqaby5iyJ7YvD2SZ-OkvBdMde8t8kVldo_rmyGavZALgWIKFkHjHgXCNZ_pMC8CQl7Z6zb0m4_azLKoIITojVwP1iVWKRQvPPhsSM_bNfmp4LtX_eDmlicmM0dxHOHUBYC7Lwtbvv4PBCiHnHJBWiB9KaIjc0JKcawDaHx0zyz8VrSYCu4pdXOfIGz-MwN3QZXx3rrFPOvncJlboDbJlrFQxfcUoqR3a_dQMW_xvYT9tk1MV7mPyQ9B2yyRxxVW-fELLKn_6ouARdv_dbrmNfA67-Luj_8aif0Ked9w21cpUCRugPCjl5abHMltrK8kafH504CQFkmrX0vnbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfVOHgPka5BRdgW7Fiu8xu0ZO-UxH4ivUazcVMXzKoqtztgQGi4JlJGsQCDvHMEdTcYdf5rzHRoUsTKQomHYdFQTJYbOW6pLPZfoBQAvchbhZv3osxCUPu8hwHeLa2jQ3dAuwuC4Kt6sIZM63WdkEJa3O8l7hbMQHVdKhmbrj4iPqVKEfLq_5W1Vo683C1_Uo_eiIfAmiZRFScdzaFNAcXFIM1s9JPfjaZ2vv9dR30JpGFOi1FLXef5J5j_U6wSdddtY2BPGvFsZeKY-ZgwdlPIltmkloOpPwfC3jHGfR_d5KESu_Ol3Sg3MYQz5BzbmSX75HcUAoesunQIUBt9AlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXOzvkNUEqitBBNdJiz3nt_4eCRTmqpSxhVSuX752PZjJa721TFghHmyOOsHwqQsIQLDdsn_nc6H1X56x-yZhnVxzGPFunL36FCn7H00kknYKmP1vZbK_HpltoyG8dBbbvmPVLna8WDPH2WFYFm7Zf5EOqNVOKo29-GeFXjtiAMGtnM0GjyTwKE9XItklajz7TFB43lDqF8mvku1zcQF5-xexTtIaxKKBmtoMQnTVFPQ7EvNn9NCkt3jn3ol9xEh11-vU9RqoK5v0t33xwQ603mzoHKgkGvu_inbGb9ZyPnZjNanq8OSGngG5N6FrOgZCzOahDTmMEqU9g-aYR6H_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTznNk85vFWcCOWtG7Utalr1Jh_zK2fHaIlEiheglQdg1ztg2H1iKqTP5LRRx94zIiFAgjw3gCI90p8PfbKx-WgM_Sz7aL-mcsbiJHualSSbAqF2ooTdHFsxltuDxEdoK46EQudJ8FARLs0nzzbJ5gCknZanJGZ_F3vftmU-LeIcGe5DFW8IKr4nYb18eAIxjxCXewtjL46fV07-eRf7F3zeXuyye7SaRfF2Bwlv8RdQTpFqjAFGH9KcxRb1fJkZyEUjtX_6_IyGKZ0-5xUq1UUcl_G-wf8m9-YMPGnGtW7aj0fb2VbKRGsYesE_tz_-X20oOpdUYK_Gs6T7A4-7sqscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTznNk85vFWcCOWtG7Utalr1Jh_zK2fHaIlEiheglQdg1ztg2H1iKqTP5LRRx94zIiFAgjw3gCI90p8PfbKx-WgM_Sz7aL-mcsbiJHualSSbAqF2ooTdHFsxltuDxEdoK46EQudJ8FARLs0nzzbJ5gCknZanJGZ_F3vftmU-LeIcGe5DFW8IKr4nYb18eAIxjxCXewtjL46fV07-eRf7F3zeXuyye7SaRfF2Bwlv8RdQTpFqjAFGH9KcxRb1fJkZyEUjtX_6_IyGKZ0-5xUq1UUcl_G-wf8m9-YMPGnGtW7aj0fb2VbKRGsYesE_tz_-X20oOpdUYK_Gs6T7A4-7sqscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiGj8wSc_wsmiGIPXPcWUoRhWQ_bA-mmIvDaL1chH4ivoOvujIcOxgQU2LpY4Djq2-jo2H8z6qry4fHdFMZDj5UTn0jYZSSzzd5cn5ddj9SB8DO08Y37tDdF_0Vv5mVhY7rviy2JtveOL698_lcRBv1knDxBRJinTLC942N48p8EhpLGnh3-jFNFZf4Zf2bFLRsBRZz7JTdwHc8CArothtzT_ElwyQ8MGDqopeTPLD_q7GsBJ0_I0gVwoXXbL-LlMFxGqrg6yU7Wk0XEn1zq1pkGEsK7Q1iyiny29qivBx3txz3PLvWUfv-FzG76EorRczVbnpLmEVwLGvDN0tBR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtJcpEILPCpiO3XrfVlE6_fRCu2hrQeeaeySdav0BmCvarhdLGb1ZEIDpw1X0IPbFORAuGXDmDhvbm7UCWeP-9IwY0Q7UXl5eGeYi6-fJfmNVR7Ktuk9EwG8E7keVCD9-vDZDgVIgOVi_PFxZJBxvSWomolra7aoCxfslPbwm3V3ZA0CbldH8Pg5WPvM7CVExOaARM6gL5qudo12BU4awGo5T6tmdJdRLfWdLWkKlj274NTEStHqm2mls3Il-vvS6GTj5Prbyf-5xN2Nl3LmDbZ2qRbOYviitB51aA591enKFYI8CpFPngxcb2HoEiHH61xbCdugHRpOA6BPNAoFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9yBlxwtjIO8TWAZUP9FEJgk_L0nlIni-MxgREPnKjAIZF3OXiowhQvsB4uQONxQgeF4L79HqoYIpN5xx-13ZUSY1l8fD2XO2Bpi5KyQs3JQc3UDA0Rjttn-zD_J88oUsWGi_VRfI9L5HD_nHH8PDoLSR7QQWX_cB-99vG56DGps4kdelEKeGIxuGc3o33CmewX1XPCRdwsrcoROA-82dipLLOYykWyWNWsup-nSd6Lc8fgHRbrQgKS61Igu8WoaG6sjIne6Shp_negkuBJOMyQsCVEynQwrxC_fIJkSpDmeQovInjmcF9Ydd51ehGWrIjDNN_kOwFqIUySSYsVpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWZdXPqBYVzirdkzhRONZSqXYjqefr2EDJBWFyaYTIMtXCkBwGyYUVw6RJ2ZYnJGar5X6P5sZ3tzHCm7q_H1dDLKrJ61O2owAogKHDE1ZPOBVwmot3Hqd_9dmZUDMx8scZ1VsZONHlgGJF_WogvhFgP8TwlTHrrBcB5mrVE2POVDbs-LXcpbMZDaxpGk5ckXTjsB3lD4B5lBNCRtWgATFFRH2U3-UEDM-EUMxHHDV8GE6WfCKlBX6eZmUnynudKKalwQ-XGJj1NNCPo_lYHUBZOTlr-hGoJDV196QPm0ssg3UxdNZI6E4WyElKK8r3LWuCeLmYztMtqWFtRzG7GNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbbSLRAa_2xwytipbQKzNQ7yzegA5TgoX2AI76Om5IAUvKbiRLzLpsHNDaXVSLqPMm-TNklN5AT1-NtrTph7RzrCr5l-hagsUixeceLyFi4lxC-naiS2gT1FtAISvy6utTeWvaymGEOqK_QuIFsV4Gpy-dXU1ahLo3vwj0O6BdEC0Ot0ABGnD5A6aKgEm9T3hNjRjyIjV3o0HxyknTVKEJ--3pgUIEWDzYHflM-3kJaL6YtvJW7YKkHpHLaoEayVVaYXrHBe1wqTXr1mc0DwtFWavBZIUaagxc7WAvxWMaTPn6tCato6aJi5lHhKD9acRWNusPQMn_qWeIFW7HCoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPCi2VEWbxga0qELPPSSzoiOxkfW6VKiZG3zhmCEIp9fklmhDuIM4sSNqPizyJn9ygORt5zroN8I-X5qPTKD4dYn8Ek9IHpW_R6fgm2pUxTDdAklijgmXGG5LRj6GGRgFpb9A2YOkexsWsZke3M2GHDRmLh1s9bfPJZOeMaxDYsyhJfvAJB3uuhLOUkagXeAkEJKafKeZhYtVdO0LUa7zL9QvplxZZQPMRamr-W55aIMBxzNTucTnYuv-mKqcYnnR3C-2-b6SwMGZA890a_cAxx9dfh2J7IXolSAg70JDDjwM6eHkYq_Txib-ib-oynLMU4Rj-ER881mEOcnVTGJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUTneJTANTB3SAD_VL5uX9W_V6-9y6lglvxwFesGXpy_l0JF2hfMOCQAzXRp2Sf4rcQ2ZZWJ5NYobiuiKZfbPZpLcG4ZgjtRKhfJOi_koCvCZlctfxR3oDrRZ3K_sNI_nWLjsHkaDComO90ivUNgcRA62YbwYokUo6jflKHweEqCCNZMdlnOmbwdVcJcu8GgRQ_kqAhNp9YXlp_UiGhzpiDOt2lDN7NcwLQJdOetIYmKNQclKGy9-5No0ddwxTYyE5CJdjL_Rk7FG7l42N1q63hL2XzRdfv_eH3NdjLjymlRMg3gml1PqIgMglakwdOxUgbhscCDEZNXK4t47ClPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=BfYnJZgAP0ai6uUsBymY3fekKWc6xTuS9GjAkP_srpMsYgHUB3eOzfOOJ3Ic_suQ-7GlUbVr-4TsWnv-NL5ZpXRvMmbvE2LsQ7dJ9vRGIA47imKTFX4frU0ounWSfAwYKC1aEH369c76neqixSWn9JF6VhN5H77-yIVxDiKTaTS2Ga-qbtJICXaTM-QE71ydJhVMXq83kEc_b60Uxzxgpq-JZtM7_DyKBBJk_fzH-ojMInrB2FdnM0lXDFcA9Tr1BOnx1LZhoPkEGpB2QGmtKqx-_HLgnuzLLEsg_CYsPYDyIzzJON3lMBNBXzTD7CBAJFG3JZLk_UyltTH6qE3A4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=BfYnJZgAP0ai6uUsBymY3fekKWc6xTuS9GjAkP_srpMsYgHUB3eOzfOOJ3Ic_suQ-7GlUbVr-4TsWnv-NL5ZpXRvMmbvE2LsQ7dJ9vRGIA47imKTFX4frU0ounWSfAwYKC1aEH369c76neqixSWn9JF6VhN5H77-yIVxDiKTaTS2Ga-qbtJICXaTM-QE71ydJhVMXq83kEc_b60Uxzxgpq-JZtM7_DyKBBJk_fzH-ojMInrB2FdnM0lXDFcA9Tr1BOnx1LZhoPkEGpB2QGmtKqx-_HLgnuzLLEsg_CYsPYDyIzzJON3lMBNBXzTD7CBAJFG3JZLk_UyltTH6qE3A4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS78IBbwTldhRx5YLveJBeDXwfOw9uCSQC7JExtcIckpzoU8NdOfBZu5zZIgg_nR1iVWAUmZ3Dr2xSOLYY5Fhi0p2Hj7O_7gnDH50YuA9_y5pXTRo3ye4k1crC5ph1Xgw65yZCHeOHpaAnkqEJ1vrRMqnkQqXY7Uz6ngAb8jPvVjf8eqyOJjO0xjxlissI4y1ptrVsXEoGC14yLdZ2UVjsQNGd1rMbUSjdL7lfGz2PA0UyJhCofov2wMfLrUuhpNuq9Ga6MPU2c7cA7KfnqwxWnVm3LIlQq-KR6zZ0oTEch9XkN4j96XFqO8IIwGFdR2qlqtN0g72yvOkykGyPUH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkLbCRK7C1knItE90eTmwFBA9uDUlYTLHKxRYcPCM9DO8MCC594hWtnet99bN4Vf4jRDTUcxduQaUjhEHKSmyOEAYrFJhBtKWywGuM_X2SaOvEYNr8aubzdJs-UUv1wSjItl4nbiIIZj0f2vOxEdIuKZNXwlInsbKeokV116C19aE7wpHs0qBC58Qj_Xg1iCjZiEJ5w3TLVZMwdQR2sOCQgVMdSp1fATghOR5dn_aEiwcadxaTJGHjeLdpjAmfu4WRmTmnl_GcrG9QSdCbfSUZMgqFQMROuNaiL9RotKRE0bSjz6yqRSttCuqIVXPYGalL3MfuWSqiO_tOZ5niAiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUJSZhdfU9txunNO6OvkaP1pIr_I2bAZchCcBcJQt5QuP1mlxL59UvjFQ0sLP4WcgX6a2bYBnjJAUWsKVJ2Vtd4Q7Wzt_6g-cKhzUlZeWUrCNjNSVt4ikprZodD-tjPZ03v1DtynT3MWs2BSqGPIISJJgVSbvpwl5LHyA1Gys1raVfM_fYsyyyJLNG_1r_tpPFX-25LLQHiOoPv8s0j8l14lTrHW_lD8PupjoSgxem8fkKB12R4qtabB6i-B2WcjvRhDcIRoXds4LIGbNu9uTuewlysBb4wgJozfJIpkW3Vntwa6JodYr1A_az5z-IEciLbsXlb0p0s7INWpKTzPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8mRwRFAh2bhFCfut4n37WEP-14jhdUmKPnJg2z69y0MnLOyyy1nibzDzbSRtlhpcOs6di1TXARfcuozhNHi2ZwYO-7SENTDcc0cIxVnorgAKvSJ_1j1ZjUYZkq1AFUskyUXs13f7BXO2RcyrWptPRt-aozHqB8QNSeEAWT9GUfLaDw2sggkW4WAoiaLTp_GpBULXbnsb7ZnPObBTSK8u_z39Mek_9iJfry9umJqxzpLGxZyYC0phnXo0xqg4bxHKf6HbfbQxxHcFG4pOOUai2I1Gif2Q1JY2FqAHjV5T4Lz0Y3Xo_gByLBwEgc4qMZWKFXQXNDzGQQr7j7nLtFxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz__wgmM9YnrjHerOUTgoj2dsV-CE9eLsBhYGDn2-IZKj0zzViZB251Q30l89PWIuy6-9_7XN2Rs8XrK_pJULda46HSvUSKEMGpJrMuTE_ubwwwE0L3AKY9sZPTJSmYDjW5Y1LoS677HvDtliZdMCMR9Ihu-ecYTDRTVQ5lEasCUXSlDpObVtuVHSuRov51UplfIlu8BLCko8qWyEhP_H-T1e0mKJLxycs33p_gh7Q1Xcn11Y1bOr0VRPdq6pUKa8nsgrd-b-Qq1_iMQawvW1fLl2li39xAu1OHmATMDAZN1sZq56D9z__OguOJVf071vqAh6YfFrtVOeNVzdyodPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9NHecfKfHsyFVVHj89b5_xSGyJXtpMBgRZk0v0XHwdsPIihp1AK6lXlGfTXY7BpTg2m8jfRHpxpdCdCdY9uy1UZkuTfrgNOd2MDAV98e7b8mKTXAA6pG5AO-FTjpVG48J5XpnDRYtdberfiuhJ1Mo2HP8TXig-iedaOlC1ufWI749a_BlgFHXOmoJTqKlKSDqcBesYWDX4GqVdiQSwH96T4dIaYQJgHE0QYvsf8UB5QP5GGjKJ-2b0jJQFozFLRsg288tivrwJnwWXa35I-5EuDHtzlpAUSGpuX0kX6C6MoICuROSDEqbbMyc3qJjYNgBdk_P4W99OfkFm1EZwYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEckW9cqp-IJNKroYszqBr1Gymd2baa9v7GHniwD8-GYHeW6_Y8pXFXZQlv2rYohioxQP7BmMH74aEBGTeE-EBZf5ttRIIy9lpzLGB25tc_BJW-TeQulQIdE_2jC5JbmaxkaMjwi7JarXZb9T3nQ1-8JW9kH-k5JMMmNqg1AksW2NpRsDVLh_E_IIDx_aXd6Si0S7qnYoaysQO7wWEHqUvG7yeIILoY_1CE_w59H8_ss92wgjirrg7ixbLaxUfq35vbfcKvID2sf4RPH2hkS7B3AuLGfcnHisK3fmC0BWKCOqOeXJX6iIjmVcT6oflfe1hC9buMam-ipXPCeKv9YXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUlWbL12q2YzWU8t87gc8NHlF3i63Wsz0uPFFsZqpUu2rE9dhurhogvCftKRhNwaK9sT4RQeD40ZDCoreSdcup8yCx4RwK-fIfMAy8cEI6u7gygS4GiBPnwkB8ScnCAEP5nKQtiZJQJ5KUIjm63-v2lBfOKlUZmq7MHy0no1W3saL0tggWsYBXSPWL6DnAWnuGFuB0TXM9bA8i2ynFjws5SJecRDH0S0-0Iwp_B009Ye0XwADyC9dIeOZbcfmvebQiw0jB_ZjGlqIRok301LxYr0ty8UJuCYazOisDdiVhIx6C7efOw7-m7LX8vXrVcxGirHssX17pHTzGiea_TxsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sD8-KHw8z50u9IzsuzM4jxTwLIB0DJU_QFsD1UqElpimDdkBKHpGsAeLy5vJAYYDNzrGRnj3D_nNbzpQDXiWulvf8qya9xT0x15LaaX2QQ2JyvqaUepLQp95-2WvlQXk2ZZIYU84AU9PKjJKgy19CaRb6HsOrJv_EYCK2kljI-W7VgRebVCcS3Yc2v0FZS6Kl7cOc2SNRWsPkSl0muGQ_7HegzS-SiNqt3yA0xd0JhvJZ3dnnja5q9DYB0wg6d90k3iSUYogajRYx8AxB-ZKGFV2FkB7Jb8-mFCjtR9kIByb8F_DW3XKDsuaScJ5fBGAwYNJDrs26OjXzRKtNdJ_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzOp5Nv1Wp5unXHRGQcd3eJDLoG9eBp6Xxgdw_jOj-2P9r_NFV4FFNqQ8dnd-F1nkX-gzgunZuMtk-vtR-M0OI8r_ZCoPhZfRVmg7JK9G_v_RE5LDTSJmRTLHkFTCYwQEGCy61X7pccUrxQBVCCauJio6qDVGJDxXtR-gx4V_Zb_v7NCuSwiIFWYjWQqlGiOTFqkjIzHk-3HInD4OxkRVk6XiAxPzbmKvhX2P4oe8rbGAK4DuceKw8BvAWcNmEC1D7BM-zhW7k9Od1cSGanpX0vP_YX-2KqUUHYbKYutZGhbgC6ID70ArLWWY8bGKCjYPVJz4lFHTdLIIniPlmliaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTwRD5IjsxLhkSHUvr8OMvuhfPc3ReukHvOXHMSImbvIJtfqnfQv_TGPN9PzTFVSjhhrQpzJ7PX6GuoS6i0VsK1jhNAN1VjpOABlp6RHE9C1PDsfyBMe9UBwlhw5cIITZFEd2MBWYIsPJ-RMKXwEeX7GbIoL9o8TpnQq2hEhJVqjFEQoMTYrzBPEYLAngVXlXQovWvvfauhyAmmUhMD3dXFu38JdGfEWXvnh9nRLit66h-vA2Xm7RaphcyDacHYZADSX4y_th6WIEFm_a1blp9VkyS70F_B_CMqxwGYnQZg74lVGDzuwaJl9bvhgLtVUowORFg8jLAss6aiMKdglaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBdMLMssQfxLUAjUGlNlB2mvkd_Yf8CjDa6X__LVh746jElhwJmJ07WSQUgGDJmzRpIWXkoykp1eVI8pMrSENxfbBrYaLudjPWCeSA6rq363Fs2CbF5iiIlvTIoMJdIUx7BlLMpG3upf8idHK_xYnnw9EV9ukM9dnyc5_3sfJ2h6ZrTgvYbxuD2CkbU5iHRy8K4HaDHFwzOM1GgE_1MqozBmQo1of39W27tQ2oxQuRbAzDSwaq9qw2wJ2J-2Fx7gCbJHH4AYsRB4cdAVnDQSL8-CTX2-LLy-Lx3pqLJ4X55EO4FBQwqjAqwcy-hFnYUyZa24hWjTix3QGhCl9WPNpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTtgtecYr3EyjSuYEO-yBx76vrYL5w55qodAGmLNNc0S_EgRXKbHFmNsiDd6kYPkSro9DjYCQhy3tjOr77ed5XI18w56Adfr63QxfXLXhwnrUCHkKmkdeIQ9FVb_wkhXa24cAXimKJubGcAwrzUEYQ33YDcIUGL15CRyZIcjfKfUgvmiPm4Igzq24C0OX-J8FTn_MouFF8ROkM-2fGzjGKciIy8CiFWmi_ltoleK3yKbXsidplteMpG7m1oZQIMfnC4NJx8Az19mNu4_C6Ee2h4HeWPfs5umOPgjoEukY-dseUkXuSBScwDy0IgzP-EtOiClqCwIpak3-Nf05Wm8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n74q-xx2dUYsXPzZI9MuZJHP6atfTQd6R-DEhrWmKNdkQdu-j1L6bItw_NZDmOEFEGP45pKy7mP8Fbc7cbdTAuW0gaBb4KResvjbs5zGJ77He7HmNSxlNzlR4EwXQJDmjZSFAcTjn-RpEdwWeXPn3W-25e2f1j4uT-9GRZmakGdCfzhfmljPAbTH_ZmTIHOQR1U0XfeTKjSE4myYHBddbrZ9oj-O0vMoeRFniP_Be3PYnkGNTEpMBoXooiggVpxq0joYufsaJM1dIeovcvkO_OL_RT8eCpSP2lUfz6YrYVLaozssJZaIrW1Q2yVaq-gG-55o09DWkQYzPrRGU8YACw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=h7O1akJXWWdHo7cQ-MdDxZ3jSPhfP6kyLaVpp2jgRrC-rDAP-b8XCDouzbDQJ_ho1vYhEiSskIGsGfVCSe89CYn_Zi5JCBMVqd9FeN1BRcBZySe5TrJep0Mchdge911VulI7NgLbtvIZCaNRf62Vq37hSxhDIBArKCmXvKxZEimae2Arob2nsfwpsQNuNxfhVizEQlOku7dCktpH7CXgnrPC8j7slyTVhf9wWyy85r94CfMCJQmLip_QRa1bm5BhY3oWJYCaE_EBuhaSDyeXHqQ-vz5E5xsURhMmuzukM2lMJ0xoGyK9TDngwlybC_0xUsNNOSOgL3fqO0-rjcLFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=h7O1akJXWWdHo7cQ-MdDxZ3jSPhfP6kyLaVpp2jgRrC-rDAP-b8XCDouzbDQJ_ho1vYhEiSskIGsGfVCSe89CYn_Zi5JCBMVqd9FeN1BRcBZySe5TrJep0Mchdge911VulI7NgLbtvIZCaNRf62Vq37hSxhDIBArKCmXvKxZEimae2Arob2nsfwpsQNuNxfhVizEQlOku7dCktpH7CXgnrPC8j7slyTVhf9wWyy85r94CfMCJQmLip_QRa1bm5BhY3oWJYCaE_EBuhaSDyeXHqQ-vz5E5xsURhMmuzukM2lMJ0xoGyK9TDngwlybC_0xUsNNOSOgL3fqO0-rjcLFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCowc2RJMH2gctrY3tQWEx6FnWjiKhtj3OLfJEao_HuxVNr50L5d24YyDyW00EsGALOYPmI49H8yxSUuVzJ9be8Y7Xkw2L4N1Pt_sdRMSna6OaM9myRXAYkZzdArzrKtGWisiiOMxhmwG1ZLjc_BfQ2Le66nNRyYKUHMWw_AsD7IB6Qu5CaezqszodCo27GeAALTlPby6paoD6eybT3MGMRAxl_QgAZJUKcH7BhttKdrjgDA6TNn_sWRJr107LCHEKWwUVO_-gNxBi8mMKAjA4C-tH8tvJ96R-LdkwBCB3o4L2-RFlub5lZa03yF7damS15owgetZy5miuPqlJnVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=ZuhU_IDC1MhON8W4PbRqbrt-l8P9CEMcbAR8k9fBZ4enpkanmZCLvrh8nP91CV_h_cLfGQ43ND7pi_t-6kITb4hc92Pdz3m38Az3oJG57H6OGcg9WnsWzvEGepbZ-VF2ESQSQIWYe7NWiMQuMwI3o8cUnGDRP4pz8fH1onoH5G1N3aai5qf8eEWcmYMOkjkQPQiiMbo8kEwBN-kS8w_8AZAoYEEfmd00US73fnyueZvUuL--TqDHzJFSX-yhsID4tlUrJcoQrQnEy9CW0YsMWXdNynWa3ui4SFJcT69EgLssqrBZ67YP5W4O6iGZ3V3FeAOKj4qqIK_lmDiHgbqKUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=ZuhU_IDC1MhON8W4PbRqbrt-l8P9CEMcbAR8k9fBZ4enpkanmZCLvrh8nP91CV_h_cLfGQ43ND7pi_t-6kITb4hc92Pdz3m38Az3oJG57H6OGcg9WnsWzvEGepbZ-VF2ESQSQIWYe7NWiMQuMwI3o8cUnGDRP4pz8fH1onoH5G1N3aai5qf8eEWcmYMOkjkQPQiiMbo8kEwBN-kS8w_8AZAoYEEfmd00US73fnyueZvUuL--TqDHzJFSX-yhsID4tlUrJcoQrQnEy9CW0YsMWXdNynWa3ui4SFJcT69EgLssqrBZ67YP5W4O6iGZ3V3FeAOKj4qqIK_lmDiHgbqKUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDFhCiWhveIVhxwBPxRYlzHr_oI_WPI3QSYd36YrWsZ4WHeL1JRZLGbXaoebEFkZXSMapnloNKY6GtPGdEV1ErVbtbWzX_UI6HxnOyb9HqNn-F1_S8yznDzATmgaXqrU9suA54lFTzX5JSpsxoW4j69tfkXThPn6n0x9WOJ2JJQJR3jMaNa91VfKQfUhTeL8T4LEv0Mr2HLu5fNZh8muo3BYBUr7W-VD4ZjlBQm0NfHOw7WwfyRvTNQ7GX6AtEt0oxXM3Fqev53KtahAxxPtbcd99M4NN_74ZUWTkEZnQAW3CXvRBGRV3cCd8k51i9Ds1pcVFbibrN5iHXigv70urA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bbuhw7Z_zNOyBnNhCBBjooB0fV2AQENF0BpwcZwWsgWOdXDlY7-h4DhOwR6L7iPpMEMSij2UZKSny9O8JONHBo525oeRhRsqB5DHGXBa6TgStDu0RzFljZbXw1MKv9fXxY-4pnWVZMk8zIT3ULg9WKaLdtqo05gG0FgRprjaLy76FWO_u7Zr2hnIvSE3c2u3foOSp3R1nX1bJmNlVztbDDQuKBqsSMWAkET7HUbfEihB24LyDsvsow7H2yZ3_wS5j3V1B8YFMJcy488wrGYs96K5o7YHMMDMVOD_5OQPr6dROMpGkQvzqh1CvEPgr0Dd2bW1VvV_uLXPArvb0EZcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaxtX2pB-2f6nk4WOCYEfVoHxgusuV7H8Cst7-GPbtu3jnOT1ALSu_n8E5tfAodCoOc1jJkJcy1kT9Ce65EGQqsuVvEikmsW7RzIczi5pmUrPKr_8W5rsaMuVoVYa_yGNKWFnmXhQ91k1VUcKd2Zyt4mKNDweyeKnInuYQfdyDu7bIqJ33gl-UY9tgL4STRtA88u1tt9SmMx6RJlk5IjMqphCz4TzSfl0uENM9gPKquBc-exXipQYheE_rM4X-E5hTmXRJz5yRq7Ue9UAHo5CZMcb7JE0QO7J3Wz-BPsbG1lElWRRrwFAplUD12Dj5aRHVmP-apATqUgxX_fSPAyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVq2ehxaEQ8tx2LtJYFOBjzw18eLMfELp66i28Sz5aRiSvANN67IdcYuBKksoUZ3_I9_KzcHHSsqe25HL2-n02SihnWvjnPuj7QdWPWtYlzjxmAo4WTjxdUxbagZo8TUkgwrrQgWlyy5rUKCDvJTajs85KPzzEM_TAaBtjgiPfRX3HLOnqFYNwr7vz_OlEsFCVVFVnl_DA7QQs75Bm5UaFF0RPo7BCcJe22b5G_PikdOw8dsKKTKL4fwzlrVAwRU98dTEiRMiUfmxG-cO3iCRf2vN-8SqJFFfBUwokYOKIOUNC-WkkPdmaWC2pjNJhInwjvWfXzEnam1S4ZNIBPC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBcoTumYn7iwZBwWdLV-rqbEWBUJqi26TVoTnSShWXX2RtVc0JZ3ZndcfGP5oZbrBXyFA3tThcL4qinZLOS6Ot4JNqouXbbTAwKvEQlzMZQkwE19evkVdmfiTmzhqRD1OaJF0Yr63nLn3A-YDKDErxx9h8x8GYhqKLKx6wmKzIayG6dlwuvVfjBJ_lf-YhUJFduJo9OqWBB-iHVDSnUBwMLMEGdEWXELejJKm8tCv9t5Zz-7yMSt-z2wYQJej337EzqVacJ-aURGqQjIcIwKcohkM8hS9RLLLohEjWkofIEw9Kcz2pyMdOHdtyRiNosw_c6UldF6rncd0IS_smXgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0MhVIxC1z9XLx2UT_dHTFojmFOT8eKg4fl3CXAq9zaC_IsbGgfDZEDyxiahlr9aqSPe9TG9COwrk4EHmbhObVsmHYwZORaSnatt56A0BkjE5BNiJZpxtxH6U-8b4YxiKq1wcp9GZcl0Droj2tapbHKNLSCm7ew_OWvv6-VrlDxO-ZL4gtDBHemH86A3_sKB3jGziTbmn3tZ3btTv4a2gjpp-N1mPt5H0DJl1PZIIUqE2aQmo94X6CYqDOcGD0TlwId6iZZyHi2Q09c6wEUsY1VyAFjGhGnFs0NfVHD9wVavAtWQ8HZXGB6raOMC-qPgYPDsVS3LC_I0FNbKs3CRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbeaoev33LJ3OTbd0ShbKhOwfkG-4a0L_hAs1TxFtzPxX6fddheFSMdjdV_X2lKf1Bl2FOK_r6M_YwPDItc7EcL96gS6yRHNydqBfbSdFSh1pDVckjPQ-hQeEpkUFNcWwxQ70MENbnMhGRPTT2_QJIkaaWR8TFM9UZtRsVQge93RpJuPthXgBcWL8yy4-fzd6YZwm8pnXf10zv2Si4n6_GXAs7GGaZMz9GvBrqY94U4dV78M8uf0857Vi8XBHJwZGeRzZjw98c-ECbW24gYJdnGEC3dQcsEnBMv1blknJvV6nBxUcwnE3-cyimXpHn-zWdK1hydKDwa4f6xZp36L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfstWtOj6caJf9cCKQxg80cjsYckgCLC5YG708JWJO4hLdKbAf5ObiOWy79rsN9q1WqCr-kOdMEn0uMEB2JrJrGFdDRjORz-UaFRfGl4cK98r6zyqrdkHaf_G8NHc8MZlTEhskwpYlXJq_sqDrJ5hGlkf9SJ2gXX-O9A7ydQNczWHtriVHxJrZW3xWJx5MtqTf5-MYV6jelu5sQcRG3MUE8SV2s96LJ6Na33eNMl92tcrwpfVjWoFZzW5w9mlXxeWLULRYdhJu0l6Mh7suKcnEMaL6slmmuxLG0MuY8LiE2PrzU4elc66fCEKX7hLQRt8nQwAI9PyNOh5C3PvLdv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV3BXhy85SXoxaOUkDxiX3QhZWuAbqw_ZiBCfT5OiU6iBOoJmvkiET14pr-NMX3qACiezVd5OZdwIriryS5meqbQwM4BWODpbNyY4t5dd61psjLNt_mLc7PtPSBLWi1Mhs7JhtWteC2HiS9Dnq3EskMNtPjrsTZe6OyM7T1K900DbdwnnPnKZXGKozeVQTXJOhm8tAxfm7uIP20aCZkMa4A-5oTdLY_FHUXc06PshQeWM71y0DaRZuh8bIeYa_oKfX7NC4YnrOpFgT8jrpA8LVTEfzdwY5Lf_l1bqbAA268uP7kr3rmpknffzuAvnAT0kTi71MW4nFH0XUc-G5W4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBP5QEdX_PYfeNZMZWiyaMPToA_zUh5DuRDYbyXcOcMp3y_uld6lsvFyQSyHNlp1o_KPK0dk6AZIgUakIPSRD6uWjl-yvLzJbamgq-b-YJEm29vVJIfZDD_tTm9JNlxh7KJPW5PET9iCgueIESJNkIxE8aIYs_VjxPjdrQJ4hhtExCxGrIeaACyUgA5wlRIVG1-I-SbZQJvfUhJaUMPKiyOHYBKc1IY99mw9q_8p1pTMhWV7DsCMn58DzwXiS3v5MzTF75l-vkrV7t7C03SgnCub4lErRfeXVMaIdPieQyX4F2Ji7K8JLhRvbrTYG8CmlrQnrbFsbJcQNruf5zUanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH0kmmulsZGkj7I29crNNj5fHZkbIHY1omVSKHG8O6Fc0S84OxIMRY-MqTtNIRQ8WIejhRxGA1H5QVrU2ItV0A6Bw-QVK8FyJHgq4zqxLe90FThRorUwvuuBeBgw-NmGegV88jIK5eB6UcwWDtv61nwU0p14AtU4EQuJNswqoWrWwDLdq7UMaiOIb8je6BIO2svhRJqU5YFvsVxnOK0Zxm9X8OnQ6HmpJaQxDFS7GnKukbJ77AgZOFjkqpfTPFa719GkezwWPjc5MVnWNMDyhHQbngdBLWtib4sD0UgIUp0wM-fIlJRtWLoJYY1v_R7jB0bMDTVVWh8mOJGAaHUzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=ab1yS_3nsc5AXapGzdACsocdRqpHGoL1TLW8FpLGknLBdlu9yGmK3aznvCV2ph6fsjekm5_iRrBeNPW-phVKIHKkhHCc3A3sQDlYoOWMiK8PifeCCRoxh-B9yIl2CO-q6l_ndRiNK_uHHWtUi-YLkGg5AvcERaMZsDdL7r30GhL2B2hAFFwj5HXMpfIFthbpwGG9gJnbuXFphq9dx3XLyi7qPNPVJNJmoOFoOTWUb8XUqoEHIzTpvT9dNcqFInd0fzyHXbSTbv7iSWFrFD6YKkf-LQFnOKs9pGqjNkzbQbUjB_7g_3JsDPiLBn5znGGcmSPnDXlpuWhTHRShQJhFrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=ab1yS_3nsc5AXapGzdACsocdRqpHGoL1TLW8FpLGknLBdlu9yGmK3aznvCV2ph6fsjekm5_iRrBeNPW-phVKIHKkhHCc3A3sQDlYoOWMiK8PifeCCRoxh-B9yIl2CO-q6l_ndRiNK_uHHWtUi-YLkGg5AvcERaMZsDdL7r30GhL2B2hAFFwj5HXMpfIFthbpwGG9gJnbuXFphq9dx3XLyi7qPNPVJNJmoOFoOTWUb8XUqoEHIzTpvT9dNcqFInd0fzyHXbSTbv7iSWFrFD6YKkf-LQFnOKs9pGqjNkzbQbUjB_7g_3JsDPiLBn5znGGcmSPnDXlpuWhTHRShQJhFrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPgdBX2uvON1FEiNz-TLyaZaloGpaHH34ylOPnnaORkAZskdVDhrTZG5PQr4OSFcga10gaFMJAs9K_2jZFnpQrUfLSeUAfa4jGVDLn_zk-Pjdo2hVIdUXyaRALqnQQZI9btko4ALW4Nn9Anm6bB6A_bPCM6FANqKXwhrXNiC9f_miz8YYqnptA780X497Maf7fzgFSZINCb5-lPNpCvrTXf05_CXJ7HiDyYOblwHh8K7pBEdEhM9er5H9FLC4uFJKf_bOHyMIip13ja0IcBshNWTO7mcn3JjOHqQdoLqG6cYOQmkw5ET5Ed3zDwr52tyqv-aRsdJvk-tbmUWLrlT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0pA8IbdSxRXgpxlHrWu-FWMtSFr0R69IdB-Iiws8C6VFb0h1cr2XDuudGdos8o9VCIVGVUlrU1qtAjitqM7ma3G_GMo5HG3a5UUEVHlVO5ddDJMKy9oqvDscHfEoWqlr5HBlvaRc1AwF0DyEOOVQY_oNRWbFYU12joFEW1dEX5Z0Kw01uzYWXf8MqcWkUxKdf_cnDnoUunuoy72lq3JUFOaj3ytN-wPPgs5CGtrsTvfvouS2LbL-Idrxq6_0g_MRcn0G1FyMFEwMVZQ6sU21QcoFMRHOEU2JzH92pRHiZ6N-GlAn5bSNFJzqy2Kv7_6UnZsQ6c2qf8JVmWkdrO1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=mKlxLTQMObKOKOpTHeHEITYCRrIq8pJnVYooZp2S55uf_HPE8I0hUSjWR9puNmHt1EM1GPB9CzbnB74qsNJiOgJ85_3EOQ3vlAFZoyR8inybl_2TJt6-ANxcUCO0ZYSvY9oGu7C5Th4wYGCAO1wISnGF5dC5MncjHt3HG-q7KyhEvH66g0WXwN2r44z1YADxNvsYCNDBnN8ITJrrHV4bfFPfvMOGVBwF4Omv2hvF43zZ0z2_JJj6asdR-AH2nqDaIq_r597xPNF-qzsMkF3n6wKREJ0E4mCxdV7gnVsfhCcg8vI7C3jE80KPD9fs3_jG4ItUswBSRMb2Js-YYBN02T-B-beiiq6eAaJcZeilqup7CsEQkfXafD2HbjU2Xc6vpU1OYiv8mN9zqpa_iNTcx30Pn0FkHKsE8e6ehotkWMCDWiQOisg4Z9DBTwxNH3qZg4Jh0QF5QNelv0QTTf-34zGWH5ld-3jBRAAxg1VyrV0WaH4sCHPiGFRMTcwSEaM47h1iWxS1KzcBMsWyVAPTIyoxOjNOfR9hICr33CLhVPy6JmjgjRRZww5jtcNBuKosZN4PGtkSOe9rgGZVrROdkRs41-ngrIFrXE9nBEqXGuwzdkP0JizMAza6XafqjwPYvSK2R59bdiC1pKUB6m4how62HFHuC2bT4eOdIa55auY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=mKlxLTQMObKOKOpTHeHEITYCRrIq8pJnVYooZp2S55uf_HPE8I0hUSjWR9puNmHt1EM1GPB9CzbnB74qsNJiOgJ85_3EOQ3vlAFZoyR8inybl_2TJt6-ANxcUCO0ZYSvY9oGu7C5Th4wYGCAO1wISnGF5dC5MncjHt3HG-q7KyhEvH66g0WXwN2r44z1YADxNvsYCNDBnN8ITJrrHV4bfFPfvMOGVBwF4Omv2hvF43zZ0z2_JJj6asdR-AH2nqDaIq_r597xPNF-qzsMkF3n6wKREJ0E4mCxdV7gnVsfhCcg8vI7C3jE80KPD9fs3_jG4ItUswBSRMb2Js-YYBN02T-B-beiiq6eAaJcZeilqup7CsEQkfXafD2HbjU2Xc6vpU1OYiv8mN9zqpa_iNTcx30Pn0FkHKsE8e6ehotkWMCDWiQOisg4Z9DBTwxNH3qZg4Jh0QF5QNelv0QTTf-34zGWH5ld-3jBRAAxg1VyrV0WaH4sCHPiGFRMTcwSEaM47h1iWxS1KzcBMsWyVAPTIyoxOjNOfR9hICr33CLhVPy6JmjgjRRZww5jtcNBuKosZN4PGtkSOe9rgGZVrROdkRs41-ngrIFrXE9nBEqXGuwzdkP0JizMAza6XafqjwPYvSK2R59bdiC1pKUB6m4how62HFHuC2bT4eOdIa55auY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=NTnCHOjVY4QdabFWvI7CX_9_SZGQ-YkixX3FknWZhUETE8EUwoWOgH_YFv28WM19lGirOtMMvE47G_vwt0GdOKtYzwT7pC-LxcHkpLz7LhyDSvvu4BAHOpT09y9IvO8YWDlGH18oW6tddBPXx1aXuj6Ktxu_miqeBtD1QveCvStJtwXaEHlKT9pYrcPeQjb0-gCRdw_CobydOrOWZl9aNbtxuaFPSW_44krFij-fh9YsHBv_uQxcc0qmc-jpqYuOgHdt__84Yl0gGZiLptCaJDpXXiiz9FMTXuDB85_zba-BSrFQr91TNeQIT0I4A1zhmNQ4MRE33WqR-CJZ-xZYlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=NTnCHOjVY4QdabFWvI7CX_9_SZGQ-YkixX3FknWZhUETE8EUwoWOgH_YFv28WM19lGirOtMMvE47G_vwt0GdOKtYzwT7pC-LxcHkpLz7LhyDSvvu4BAHOpT09y9IvO8YWDlGH18oW6tddBPXx1aXuj6Ktxu_miqeBtD1QveCvStJtwXaEHlKT9pYrcPeQjb0-gCRdw_CobydOrOWZl9aNbtxuaFPSW_44krFij-fh9YsHBv_uQxcc0qmc-jpqYuOgHdt__84Yl0gGZiLptCaJDpXXiiz9FMTXuDB85_zba-BSrFQr91TNeQIT0I4A1zhmNQ4MRE33WqR-CJZ-xZYlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWI8DeqFrDqfziuA2PSFtdkQ-v89ddOyYbWMtE5TCtiRroG-WoIC7KtAxs1IfO2fLutHfLrt1kUF1TriLJhO2bhXTZVOb5NX3KpBASuSrBQdDBqXfBIgePTUdss3kDEtRCIrknf7IeVKCGVGRIc8Jw2OoLU_OVfZOWYt4zh4GXxICK_KJNPfETJIBYk_RNlful34_zBuwRGt3LEuOrJqG8V_Zo8WowqmF5n0GdJohFUGtdDYqnXDCGmpNMrbyv4SWNQNSUVg3O5pCqdZoSjVFp0xGOGK6_BfkbRwSaA8FJM6IcpDXFzCqJasIM_j0IjTmt8UB7xZDKI78ALAb-Lccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3C7R31zg7zKpef2PvxuRV2xbFFs8t8u4Y4r5SH9Zy8LGyX6pLwUM7b7G2VTvA439DyXGJEHNUN9rG6vy75ZFVOESz8Rn0buupTwzCoEFB3vq9sZhq0PTfSEOIuFW9K-gsx1ORVYB2GrmM5xDjkzvdVpmDEOcWZfrqFzBOEw1VbiN0mU8EDY_ofCmvkWs_Au4P4iTP5I6PbXcnjQ9qPi84A3dw4wm_ZC4r6x-OQ0d91hjQPi_1AmADoLWmvjGxZtfxFMRrQ9Nq7IWSYrfuXIK7oOZY-W2vH-r5z4iGSpRSOXMkU9ZVgR3ihe2DftqJuXtaNmLKBM8hVZK8V6-_MCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dvba2Isrt_AimehMqhmbzOPOk_oxtBIWk6hZFRMuLB5KNYDPhAf2Ek9v_sOfyYKq4s6Szf-69LHCdLn1MIpi9R9crsCEVe8QMQZnR7lRcC4e4TuaH69Qlfj4RgdKiFMzcg3b61W1KUhKlyF0E978O4nAkR6g_ydGKyqJHZou76NvTzYCSxL0u9YbWFM4eQcbanneIccN-coC2Op3DbJyaI3GimGKmBfrxMKhSeCBGGBxb2Ddj7T2arqlU4l9Plm3dXlUx79qVaVHqUJO-5LBn31LYR3DuiVvd4hYmERGQg3fGpnLc5uoY8iduUJ-kt8FON-wZB-F9I_-j91HVsJYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoGPo6rWuBwh7Eps-WXveqTu8OAFhn4nUKGqvYudm6agRD06231r7HfjZp_Mkpo6VSVsrkVEeplC043U0lJIWWD-qUDpM-SIyrWB48R8NOtMRThCjmLuKHAgFllgab2XgWGLKhh-BAO7wd771tcfc-r20bI3FSnA2djQ0ITBULj1_3uU83WfaCTuRn5NPUthxEGSMG76t1isZrlL0VCCk26cJS62HELJSGaPd4ud0amgh3eFnaSyhOqtpZE-uKFj0ljUzgKg8jS_UhD2ctrm7lYo957qTf6xhrzLT9cOxZTyQv-8zLXTLAyJ0kY3gk4_QwItwOoGSlmVVzWw5oWauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWuW-z6tWns9ZkPA2d2I-Lob3nOp96QHKMI1HdKADZ3JUDbOZ6eyOn2ARD_Fs7Jepg9rtg7HS1Jtd8MPw3tAPdcl6VXICFKIZp5BNYjeLuTGGphXctoWAuU3xw1P48pdLo6lhfW0nfNvhmNwDfHNBV0uQfjU-fI-1_NrPvj4olS55y1opFHqd0JozQsp-4eoJSKvfCd7ngRcMa_b_J8lrOtjAXdyDSnGXLpAG3_Dq543yFJdVcdXfuPxFxt0aSUjBWdWyStZW4aAfM7ETLND_2qzvGXHA0_fZJtHPn3LvV4LE_zM1k122CNzUpLmphz1rTJBWj3IF07Th2O4kMUjVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxZRgVhYEzaFCoRjNzLqF-qoUe0GiobCA6wM3qm75sLICMmzT6AMCKALUNhU2KFNuq0uyZpAWOwla6r0lZyS04Aqb7RfyrJvwbBJYqi6FQgRtgElGo3dZECJx_tgYjrG7ngjzacqIHYM8QzrGa2X7KAddZQrYyyn5U3CJy1DnC7i843yLrgahvi1FUedeWQICuMTU6bjDAIsOgzwKjDbxfXu0rMF0EoeyWgzxL_yRb9IeGeje4TORh5Ze1IOQEMJsYgsA143WQbYOnEHV8v7MQ_3gYHVnIMsIgLL48EKKwow_rQkHkH5OPTlAn_DhNtzKZFicxGrMKvrDHxTRLTSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4v-abBVKzz7vbFVRikpUBREKcJrPKxenNpIE2LFzUo2a0oFYN5CyAzg5OLdythQBPCV6BobWzJKaA_3n5m46ew02GteWYvyFJRixpSq2cX-AY9Zg0nUX1ilNPTVfD1o8jBuAEEr_mIgmjqM00mZSd2KCnt9qpQ2orErS7AX_-vff2k0zo3BYjX4vCfQ9_EhApYOu6Ypa3EmZXZSCmKEzo2bj0HPJde7IXtir65dbBSSi9FewRJVZScvY966ssslR2ZlV22LhmYzKNDDWP9pLr1IUKR-OM2O_daDv6r5PqlkMrbgtBrf8cpQA_i-H9h2er9TxXR9NCrD2MY7ORyPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmuB1MdVOOWBBsO5b9CnHYX6PiOTHk-juV3iTmaEoVq9aCVS9J5fIN_trr_Y_hqxnEjirEo_SQE81AFzmf_N2vnF25Fkhi3k3raWGpnXKapYhbPt74gsie5bvdh4EEwSjM8B1w9OXM-dUy3obGrJ7olcNgZqc_XHpv11b9bKfAoQMfjYmcZJcZ0uhPFqk3QHkyuco8sW1c5tx9gP9jjhLom88CoJ4TIQhATIAPSGsFOAcuiYivOMkVeaJkoFKc87JL_isRHx6S94_DzB00WIEKZRP13-8VWuirWvwmboKGW66TzOTMqI9aMJGI10opYGM7K8emfspUbR6N7X9L2ctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfXby2aiiIf9LDbyv5txLA4u9CgrcPqTrQNnQFkGCwdlCeTHyNktolMRbRuMddIdTU7V7AOa8VKfiWaGyH8tvxTAErdWOPmtCZx_2lnO2uLBJgJGpp2zZJ7Xb9S7bvF2Cag67qdDD8VJgTLJmpC_NYRd5woREnwN4vbtAVGcWvqUpBVfJpffsEPGj6BmVBO09GkvFYKSE5yaQnXsy9tnCYL6aPmCD_fPZzddWatRpMeu-qe3JnTA_LnPVd7IOyvtb9mZ8RGhEsgCnbTQn1oT_nl14tayuLFb2DCTrtCp2YaS67OxFnv_OEquG1_SWjtKz8-0gJJr--2LR5GYRbRN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
