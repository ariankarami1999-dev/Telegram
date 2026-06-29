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
<img src="https://cdn4.telesco.pe/file/ScsA2RLzqkdg0Ukbwbc2p5wktukSj2G_Hu--yP4s7hqCFXmyXXZgujRqG1rw6CIJ73SmC6Ci2vT8Eofx7d1BC1ialLvY1xpIpPI_AxczicRtXn1nXEvBiVW3HBkammJx8uN89kLrOIEPOP-bSyk8CJjn3b29AF7BWaWxbAyI0Z15yajaISBkq1SoGXbynhEmhgAHZIUBqyUfgDpYqYBHfP2tBEm6cYukX9IEgo3fgpqHGZv_DqDgOg6j8h2XD2BHkQ1VPqfj99zKeDspC50YoS61Z6Rn55xj00mjIJcjsg_G10jg7EjmYsCwNkeMR_T4L3BcJYAcrYegHSvmHiJ_KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px3hG0PNMQdjepNkBAxjA6if9ayTBuK_PKorBMehwUcnK4gvAdzlq9OHI2hXvrMezZY00WQOyTw2JWnoEu3_SpeRXCyeh-HX3Lr0pFnD1jS0-wzTgtrt5J3nigSbeK3tFBWBKowJRjlg0wRBUQzaPHwcgQz9s9yQN2iLR-Wcz0SXdS9giN1AnK3C8ZNi1uP2Wgkk0yeXKoYOzYLfMaq1dQRSKN3b6n41JTXM6KngXOqtRkYWBXm-4qB8fQQGA8gRwZgxp10goulaIaV6rzNEuQiYxLxOfjC3GeAu4yVH2JEy799sbxPUGexYPo6WqdxGh56zMWDkzjyNrVlRyCGXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=onTtqdEacw1W3Gz9LH6SPZrFCSC89X-GOv8zPzPIoya1NC99NiDmhHRHKi5v-Om9kB10kGl9ZeBwNG3NMi5UdhP3JxbJGBimQ0xZ0_V3fywzjOdrbmyFhGc1GZW_Eyasp5cHLck5uNIiefr6u53Op1ZvRTQN50ySGoFt2IO-CSCARYEgLL2BT-XEnQ4EQGp51cf17EVxtPsko_n6MezdvOHyIhNJ9mqFc_EBVl91pdeDTmU9ruk3gH4wWqSTKyjX7biZMy8GuOeEar5zvE5qrR0MbT_pB9OKQzhgeG4fM63V8iM5esMjxMJnHroUqIasnP_t0TfEjBtY2p_0NENVoWlid0w3dS83-M1Fr4HF9-srYqpcgdwRRl0RT-GdxP4u01M9Sf1iby-dAb8mNwP2YjG5JgIeTUmRZflvWyX_Sabo1y-9EUnoLwL34j6ZH-f-02J2fWig92RXH0juGvaE03GSqU2kGjErr-yKDXd45grJwprB0eg4OcwFdUwcYHcU01--E1X1zpBOcdiEqTVpZL3SgdhWTnHB5LqV_rMJJroJC-ztsyqnyc4GqyPayAPgrq6TRsXnQxjXDz0-y7PUuXm0_JqZ85QFTAaWh6n6L_vHPInoU9qthZ3cSdpzpQcchLHjbE9-TDlu4SjCTVE-ktS3LwLAorEJDLzqMgO6BZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=onTtqdEacw1W3Gz9LH6SPZrFCSC89X-GOv8zPzPIoya1NC99NiDmhHRHKi5v-Om9kB10kGl9ZeBwNG3NMi5UdhP3JxbJGBimQ0xZ0_V3fywzjOdrbmyFhGc1GZW_Eyasp5cHLck5uNIiefr6u53Op1ZvRTQN50ySGoFt2IO-CSCARYEgLL2BT-XEnQ4EQGp51cf17EVxtPsko_n6MezdvOHyIhNJ9mqFc_EBVl91pdeDTmU9ruk3gH4wWqSTKyjX7biZMy8GuOeEar5zvE5qrR0MbT_pB9OKQzhgeG4fM63V8iM5esMjxMJnHroUqIasnP_t0TfEjBtY2p_0NENVoWlid0w3dS83-M1Fr4HF9-srYqpcgdwRRl0RT-GdxP4u01M9Sf1iby-dAb8mNwP2YjG5JgIeTUmRZflvWyX_Sabo1y-9EUnoLwL34j6ZH-f-02J2fWig92RXH0juGvaE03GSqU2kGjErr-yKDXd45grJwprB0eg4OcwFdUwcYHcU01--E1X1zpBOcdiEqTVpZL3SgdhWTnHB5LqV_rMJJroJC-ztsyqnyc4GqyPayAPgrq6TRsXnQxjXDz0-y7PUuXm0_JqZ85QFTAaWh6n6L_vHPInoU9qthZ3cSdpzpQcchLHjbE9-TDlu4SjCTVE-ktS3LwLAorEJDLzqMgO6BZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxppZXaxKWsrNyX4DGriBV9IercHCKqgbS9BCHpA_pzD63aZU5mYIUSQnY8w7B_jb-iLTBf5kl8YzNa2SnZvz3GqejQecc0T9Ux9AO6Ydc4UljWc4wLNu71RGBpFbCDu4fv4RcL81eEtMsvvr-bwpglZmLIBpdKjEhAj3Z7eHfl4FRfWwO2wN_pqKqUF5F951B6_q5QfGf6LIfLUMPIUfUIgKHwaO9bgbAX25NOTXWtwbCGgoZc-xQVOSrL5u1YYzIrrVsYw_f2H_5ifROZ5to3T3EImT9hshMLJHvnWFQlJzRI9LkXrorJxMVObYRQwcTBjG-6pVZbz_ZO_MqPUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xlwi-QuKmi4pCI_lVnmeLaGH4r9MjUMH6_GHzE4KXPzfGQ9s8ItdYWdqU2EzGstK1fGWFUMkVgc2-8zrXQ9zRFYffmpcDCNS5Jo1LjnL9TGHqvwJaBkoC0syb7p7BZTcN6hEeHmqzO5Oz0ZYZj-j8JlnPij7CgiJeZqHLH_B0tWp7AHvOK0IEjSodUS_jp32VvjfXB7H6UWJhiqo4BAk77tfWtTd0VoaVvL3TgP3xMFTmwHTf8WNhVN5YgfERgvgv_FwGInx1Ex-wvGXGh0AaiFoyStoY6TUeXYpbMF5JcvujGmSVuoKBeK7S6xr88fbGjCsWfrKeB7eUgW_DNAqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAqKjKHKW_7uX7tLWBE82cwt3W8wcsPtrMLhI4xp4OQVz8GG6nmpWf2ZfxpbHQoIfMcLg6_pGQLKe9E8qczgnGw3kveZfL7_VOUHJSr2Rkhe29ewv6IvVnHwV5pRf4uj2Y5tqP7YUnuDcmZ7hoWW180RNEtNDClcigHrroVDoxAtJ5RQlEzjLMhI6NkzXpBpVDRo94s-Jkd8VUYaZGiQrAY4u2_4Cc6j3LIWAEFpRJ7sTg6iRA1ZIp9JW3B-MUSQa9PKwNYfoTQNZ45j86u3KWMp9YoaxmCledU6H053Veto_EAaHC6JNs99CcMqIsbE7IG8fEjWoNm1TTJ5WUH8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Z3MdUJEzOl8LK_dgoUdAjz5Nn3tvSLWRFRwa5gLKAEKB3ZPenJv5XP0ATekEgKOo_w42ouXgvBI8-7JzmKyeL5jWzxL2gTCoYENOUCoOlNctTy9In_WcuHfukFPq-V1pn87TvPkP53asD1hbgbxhw7nlxzhErknv4z-fPKPKYmnnqGmh3Qlaehvfk-seYYc00WYohKo1vhJI2_zm7T-r8prrYHP6HgetxIZbMhemenZBOXas5egZFCs0AZmOIa7dPieIs6bH4vNzSMW1I7VPrHLvceA1Ln76lS2LoeH-sBEPE9TXVWckKe3OuHdPsoKsQUlRMLjv75LTz4vWRQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Vc8FiwcRQnxgNMP67nA5boTJaOHfNj53CO0aAciJlsDABnTJ1mbSF7aks3xLcML91laRZ2PWhcGT9QLoZVMv34DG3aoFmZYyM1gqUwTVYVus8CpMAjtEyZcYZbZesLr3UxnIIw-itbZ6qXPg0WZoyzTOfFS9Kook7dmYPbG7aDwzjv1Jel76dQHBFbH1gEJdbmzPILS-p5eoloMWLv1gzBtAyy4flJ1n_tQMr0bplh223slMhrOqZSvyommbA0JaILUj0cIZe-zsvkHsdb039ivCglpWpRnPPfOMgugEMXE8Mm1ddprvuL6Bqh-EfE1KOyK8CxZ-ruHAbM2cgPjdGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Vc8FiwcRQnxgNMP67nA5boTJaOHfNj53CO0aAciJlsDABnTJ1mbSF7aks3xLcML91laRZ2PWhcGT9QLoZVMv34DG3aoFmZYyM1gqUwTVYVus8CpMAjtEyZcYZbZesLr3UxnIIw-itbZ6qXPg0WZoyzTOfFS9Kook7dmYPbG7aDwzjv1Jel76dQHBFbH1gEJdbmzPILS-p5eoloMWLv1gzBtAyy4flJ1n_tQMr0bplh223slMhrOqZSvyommbA0JaILUj0cIZe-zsvkHsdb039ivCglpWpRnPPfOMgugEMXE8Mm1ddprvuL6Bqh-EfE1KOyK8CxZ-ruHAbM2cgPjdGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=MfG20tKcV3DujV69UqaUamxPhoQC3EGM2dv4YNHk1QQnB9RatL0NZKyrTyTWMw0-8frLHUX_ltgPaDQfh0rPFKcSo-1Hb-I_QXk8wmAY5jERHFTUpezRoiKI8Muy9ctikpQXxtZanOfwy4XkBO7ZMXYpqWzEzc7Oyz_5aqAF_AKL1ERkjP4rrWRFAXe3XorImSpVFhbbe2b4xVYtE-yUasvo1ocsyeLGQTPqstCc-iwXQ25C7xIXWgpqaWrDDm7PG3Dqec5n-ad84oRBkzWTilbs5gSSRk89JjJ85Xl_RHJfCUMtljZUCrVcM7AbdjSItE6nV4oVWvT2GjkJ4oMngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=MfG20tKcV3DujV69UqaUamxPhoQC3EGM2dv4YNHk1QQnB9RatL0NZKyrTyTWMw0-8frLHUX_ltgPaDQfh0rPFKcSo-1Hb-I_QXk8wmAY5jERHFTUpezRoiKI8Muy9ctikpQXxtZanOfwy4XkBO7ZMXYpqWzEzc7Oyz_5aqAF_AKL1ERkjP4rrWRFAXe3XorImSpVFhbbe2b4xVYtE-yUasvo1ocsyeLGQTPqstCc-iwXQ25C7xIXWgpqaWrDDm7PG3Dqec5n-ad84oRBkzWTilbs5gSSRk89JjJ85Xl_RHJfCUMtljZUCrVcM7AbdjSItE6nV4oVWvT2GjkJ4oMngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqaLB1lG2RELuFD__irigajZG72UviHujTyJP19Ir7IdBrTKx2ujRtJzUwiFCZEDs1f2Drv4oajkD0CmkSue_NZM4fbnjXukYc0UAxMCloCWqT9wMOjXTMBpB6kagR3u2wWGEOyd5Q2p7nkqNrD_Hr0nmVZQxyGp9wRnXeBpSJlVYzTjUrY7s06Eqf6T8HVkjKbm0cMnOfNRHxG2v7uQiJb5CzTNZ_eUK0JzjqvQHPqEvpEUZ19MuOXDiS_KqzCBIeYkMu7x94idgdB7xScBq4Z7UjuH4HyrqmN6phBXn9haHRVVyqHiXWEsxrjQ4i8q4orF-28IEAgsPM66tld9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAl2yvkB2jEfzeHKrIOCfP_xt_fMKEKrFHBOONzDozAx_KLpj-Bx3qzrAE1fndMsa7Qi-5iCLDOktAQXv6nxF_Et94KvInGfWlCv-Az1B9_QPjzqNRtARHClQcqpPW1fxtYI-8A24YpLP4-qbJnTW-h_SbaYZQGK7TMV1juDoan8QPkn1x83ZKpRDdXlvqV7YTRiSC89z3QbLSmo8Iqt9Y3Tnr7fro8tI_ht7J17wIT9E4VJ8wvfZTjXdLbvqj02zni4bnkhbz5x4bPJxx8gH0MgOe2xvaCZ5cMNa8D2Q8rWCxsjMe-jVIugg6KZBj2HLfaVIy3LBm4GSqPT-up9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me-objVy3Mh4pHX5iqH9WvQ0KU1qYIaCBR7YVE-DYcnALaRk1_4PRmR9sbaH_WJzMyjnH0ZowaJIGkX6SpFc89vz_zMyGuJ6BolxVKgL_tJo9hJd9yJ2RQJFBcD3-sf_-lX0wc85QPq1vXg24s6X_U99Z6npJNf_2sTxb6vwMUwpJ64t_tqO6iUmV8c2SmyATNR5clU58tVpeIULxZ5Mn0zjCFbxkDAmMYpEGr35Ds_ptVCCiTJO8VPdenJBKg417neliNnWH1qza71uMcW-luRC1XmrRw9bys9tjS4-yL6LTlFQV3uc0X1hdnR8jkj6WduoQEsYOF90sJg9mb9nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVdCx1HX6m-XF1BNRtlNXq2jh5_0c64TI5CaQ9YjHCWcwmI6a6hCmxNgtDXbsxr9OFI5NrfFMj3QOjyp5wJhKAdE3Y9Uz-dsyHzZdE5d-DUr0zUrsMaF8ctC_Y_AVymBLPjjiPOR9YSByOnjE7pFRmyOEXyXITxjmtQRAHj3aqYSfMHONpafmxPaK2XHoszJNrIg_a32Gj0JM2lSK9G9olRhTtHRN6XTI6JV8ATFnKRvu20ei2J3854aWrVcqjjQ-eNHF2IiZgmWsFcHaZ2Jbqp7FwvD1aCe7ur6LVSW5p9NXUbMVFTVFrP8x9JzdRjSpqh851mS14wmu4eCaXs53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um7IOoxlaTUhp_78vwIwmTO_x1Fvti6eVYnxma8oE0115IewTRIlWsMexqsOdSwBL1zzrSVoYB5uCRjQ1bAUk-U7jVaN3PsJiw54snriyTgX-zYfJQQkYi0zljLHYWNyJ1V8bnvxOvJCK62WV_AxH6LYcodcyzIvdpz8XxyWemAPtNlEcEOitvdPYhp94i4gJK-XFM_NgbHDXMBiPoVBirkS92Eo2hv-npZpb88MyRCcpK3nzaxySIVmJgHCrsPGnDrC98ZnijikFAZg-At8wPeJ41-fWITPSOFHfCKI6JmiW_2-PYGwQNOUmkgoFY4_XK3mtW9XX517qY22rKMBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdGLpLE5VVqzJlODfFvpqJOPZFpQ0xxrnVLUrgTlZZDbwTSlxj2hEnUL3zMA_4HICryYOfHKdy2NpvwAyn1A2R6EodJe4ADgjnK8UCNoCrlCKu8KSORU7BP87vzG3f9LvsFTOc8X4qD_4JUfc-oRgmlkHUfA8PQIThOUaN0NOB0Qr-CnBzwWa0ooiQ1fRshRH72e9op86cbAiFdeEO3moOe16U-zLBEGn1MmTQHDWI2NNTchgZUo6S8uOyXGq16DCP-pMteDBW3Uv7njncMRh3NKbXBUuiV9I2xm-lK2YgOgkLHQh4VZnr_LJj85B6_wFa9ayFyDy_kSOq_RHqDOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYJC--BOgCn2Rn0x7HsuWZqNbhH6kMvuDc6FpSC00aayGTt_WxOFm3PMmfAgyZ5mpwWagLyjQo1GlMaYrgpR7R4KZKOZ91tTtMXVhrKf3uwRfx2Lt0oCq6BPF_UH5iLq0ye2kgws0P0KQWriQNEKcNCioWLCcyzKjsBkI-R-8Z8uyTvxFZCDt0MawCiCN-0dNZxXW4VAYq5JL9SbCI6U5hXPec2E3ieHU8JXSRQ1XWC5J90kCFKdxMKvad54u5sf3cC7uDUCrZnMNPX1cw58rIn2tIvihiGBfws-psAb4XImrVWRpUFcI43YBmZgHDoVaXwDehPAfKfHEv0h0c761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=r7UIb0Rg51rBm82D85ds8Oofl33NCzBdUoH-avFnCuNxufQAEf1QDIwm6iqfLYLw5X8nXggDQ7786LdY21Yp7gBMwf4vvpqka6cz7rFhJopb8h0UZZ4iwIs2-HKboFfpbajZYq7hdsBQetQWv5zSF3zBmdDYCalQZPj2WvG-34mNsCdmF8bvlVlTjFkSrIKFTzT1KwtFffRa6WdpZhd-sHCHDbF3YrAHzFJ8zbem3TzhxrpY93T3cNjsalOXO5Tem1RgSX1CyAcVHwQcggO0kDcDwMbHiKtZZdj2rJpR4vmW2Ph8zttE-SGwUR6K6GFVaZo2EwXLgZgrcgCFldshKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=r7UIb0Rg51rBm82D85ds8Oofl33NCzBdUoH-avFnCuNxufQAEf1QDIwm6iqfLYLw5X8nXggDQ7786LdY21Yp7gBMwf4vvpqka6cz7rFhJopb8h0UZZ4iwIs2-HKboFfpbajZYq7hdsBQetQWv5zSF3zBmdDYCalQZPj2WvG-34mNsCdmF8bvlVlTjFkSrIKFTzT1KwtFffRa6WdpZhd-sHCHDbF3YrAHzFJ8zbem3TzhxrpY93T3cNjsalOXO5Tem1RgSX1CyAcVHwQcggO0kDcDwMbHiKtZZdj2rJpR4vmW2Ph8zttE-SGwUR6K6GFVaZo2EwXLgZgrcgCFldshKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LufC2j6t78KHrxChD9WhdwRnWZFWzqxt8QXiOTKFf4rFHQD2OCp36OzMqhmOxssnk-6JOYVivztSNwJzV8hvr1YSAlgALcj3z2pmxTbmR6WwzqfoQGN05lLVDAiO1S9G6xkeJThrWWyvdgAVKyv973RzfcMl8-PvIqIfQylseHQ1anZQy1Z0aZOKtUUoEKQTUYSjuI5X5KV-b1gTWpgttsxgAA5kkLwjzYYGJ6i5QCRcWV9Hp1ZDd_kcGxPx-uvVQOxv1QdW1n5vOvvW3stUc6uf7eWT-YA3xR-tYl7Vw_0dHWbCX99i-d0M7WJglkkNfTOzebNgkN_MRbjEZ4EsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2pfOLpO_dUzAMm6clx-DzxbZsmNzqpCMDWgLqjX9anTV9GvxBIwz42MHtcGggkfYzBO58QUEfFVvUbwwKNxWpxM6kP8345vK26VFH6P1bDFk3_AFZts0y7MHHhSFWaeCKr17lVR_VWSd1i3Y_fdNMjQlwb_jR9U0j8FqXiaDz6xmf7_-_SCs33nC55ENaHES3MJ5WQWgRdRWrnDzuW7TJTuBxl-1wsjqIdraLFDzIHTuXajRBck4_dC0ZI-ifxoFBqE6SVxSuz5mqRjYe2YapP-IIYAifxuKCPLViY9SSdnbh6WFtUsx99c7WqUfH5PpAUIyE0g20eDIAjTkGjGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh09pBWCzQPT-z_kJPTc5MZn_J7bqOjsLyx-O5YovkubjdE1Jac0rB7M9IFfLMfSUYts6sdMjqQcpU9Y2L0nQvJEZjWOKFKZAYrtPGqhgZmBFlmXCpdjuD2bQatplIa8MZpWZWXlsz6UGAL3K2I1XjSL9ehusbdxFU2ARA-Uu1bPSI_bIZJwl7Vjx02KqsszE3JOktkTjGrK3gsB-cRVQV9oJ0sEIFI2IwVCt7nBed_rgUTseMn2RCqsf1-FzOibzNut9attFE_gOpyMX4oAd8CBGvJRHnN9r45k7G_jJbaR9pzVQPFl8E6eCOUFe_gCkkeuOdS5x0HZGBbo7U327A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIsq4PykoOKOXbd7iGub6yMWs_trjVdNDXLdZIjC-i4Aa6wFexgowAielxOzBaS6Zs5Y62LGSSCHQcGiBryf-flIcBVGggkro-YAcATrZ1mbwmArP82JuwNBK81JhDt6QRobNDAT2UlBQEz0x613b5DGA0erFPIzvUuWz2SWUZMF4upSjJfJ1Alh45gYiUm5LnCMpXpeV-K1mHaLptLvWieeftflrRooBJyVmLqKzprmr6-g4-D6JjZSD1aV_ebwyXfB4dRnK7eRP8hYbezPhWV-VqC8bSjz4f3YYal6Hzvo4Lmqn8i2C7OR1E3kAJobftPiOtnHkpoJrrqJ5XPKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBMbQNHbg3XDXdiHa031FZcC_pnJNWNzi1Bia2MsCRNSgPKdbmOdl5wscxGJTYbo8at9PDcHgnVRSK7ylW-TsrvkWYHEfkZifxinAfcKZg-pbCzBqQtWGTV1JGEmU9IrzkPtaB_GZRyss5AHsaIEnZNkFj6KNYhm4eBNgR20bXsC8YB9jFScMpZQulaKFtcs-JJXuwww91BFhOjQ_8fzImDuLz0M4tUV8Mu0t7yIPSUVZb1fKnDlegK80GnDQyLM6SFK0LdvBPemG_Oo5eu0E8ZYe8s5TLMFctq3DAhOzH-7JsfzicARn4wrk1KykGcUT6h7jnyzeLwbhbBcPa_hQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYV8-vqPq8ZY7XNqrVyRIyP4aSPT0VDk34BNAMFrTuxuHguP_aBv1DyEE2zcT9TNvFpMCDt2FysihSNP9nD9PpmS7sqPC0gyQul1yOgEO-cZOteFrPr484mYmLpT6ddiF9uKnaRolG9Swhj7f5glMAPIb_HBe08REIRZaN9prIyIdXnwtg2yw-ie1OPAl7qMRiOygrmmIofY2Z-DQUrdotYbKXqvvS0BraaF52CkeyrY8Ffs-DF9TcY8MeNHHNHjllyqFpSZ_DJAbSeKZRIRSX9jI9XeLp8wrrwrtSNmgTeGAX41DjD4jO--nA-I1AdVCxBjUPSmDu7mO7gcAQ_7Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqFz0Q_f2OnggnsiCxiHNTE-NjRreCJC4Bp9Q49VEpg0QzKNy8dhhhmdpe_tTDUI-bjR9mN38RSH1z_78KsRxFxu8EOoWDIn_Iy4MHPzErVA_XBgvr9bOsbJwbYy9o6GRMeW5r160vZF9YrS0CHlV1lItEr9sOybMvREBgJj-KLm7-v9MF4gqlihQEbYNehDRbcY5GyIIxgOQNf4lmAzM5r5MAp1MkvYftuQywXMhGR90lWjNxkaezMfbvHS6_S2L3PHiEa0pdhAamJYoLfbdwhS1ADTsCHLViTRhbTRfuSKZBFBbYcWz6A051hlNL59cGCy8sQqzYPswnNABe2Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=Ftd2n9OCq1dDi5YxuxbfRc-Vyk0ZFo4Or1whc6pWIZplilobqUjfJReJzYKY1pi7YXQoV8OQKktJz9ihokAUmkDzoxlOOlDM2XJohb3UbpNUDMWOEtvlgzqjuRW7Vcw-LwkFBmhO4MicDqKdf5IXGfeluDv4rxN_QYFwk539SNX7lUoDunpiI_u_z-qlokHDElgFxJmik4Pj2fLWB8h2PEyeH3a4gwOiK8KAShaqgMMDU6Z7hbnRfnZvNVqvIk_PaUwL6Ubji7So-DoF8swngWJE37e3u1hMxRHoPaln0UhqMBzfosfXU3_05JPRPqG97MJT2Ox-DYLFIhdk57ylzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=Ftd2n9OCq1dDi5YxuxbfRc-Vyk0ZFo4Or1whc6pWIZplilobqUjfJReJzYKY1pi7YXQoV8OQKktJz9ihokAUmkDzoxlOOlDM2XJohb3UbpNUDMWOEtvlgzqjuRW7Vcw-LwkFBmhO4MicDqKdf5IXGfeluDv4rxN_QYFwk539SNX7lUoDunpiI_u_z-qlokHDElgFxJmik4Pj2fLWB8h2PEyeH3a4gwOiK8KAShaqgMMDU6Z7hbnRfnZvNVqvIk_PaUwL6Ubji7So-DoF8swngWJE37e3u1hMxRHoPaln0UhqMBzfosfXU3_05JPRPqG97MJT2Ox-DYLFIhdk57ylzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bw05VPKvgHqyftdo9gfaZpZJrtXzLs1wSa-gM01Whl7jWnooSmKgLilDbK4Y4jhv9wK7CUTfqcaLypU1HXeOOvhu_RP-VJssJzvhA4gMPteLoddhG5lMgoxrF6oS5zgBT-aS9o5hEdgHGTM49YOzQHEPEB2LHBHOy8tBmW8WUkTGfmnw5UyKFii76GZIakm9TWadP5njTRzROby_V5EL6yjkW2Jnyszxb9_rq5ZVMfj3CpjIIaEzRe1VHbe2l72GTD68HyCsvgE6NautsnKH4QXvayy8C844tHkJc4UuwmIHlLiJqfEkprGHt3jNYTlUF8VQr6ARWlRsJRzifOYrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrE7w85EhrCn6K3xMnP0a8VL5lDatNn9hfwWmQx-ckCvv_6_Ua15UxNJkJcLScCtjEIfilHu8a3O8WfjFtVcLSzwXei7KpL1m7Tzkgsbrybu_VifHIAW4vlFChZdlcBLuePK2ox16DELuzVhJUmXxS9VcffKJtNau03GV6Xc19OiPd5568tARAYamtesCCfNYJfnYs6IMOOAqcP3M1Ud5nACWpLyzYPMeGay8OB7yKminOuU9ehk6F1wnuPnEOzjOuX1soOk8HcZqVmkB9WZIFwKGEa0y9sSKwLhwJtGSLk9KiRr3QDU-xRyte_rPlfRNnBW5c-1K0Jb5lozCsXx0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_MaP5uVzgZQ0JhhWCZmAHDIkdJKIcbLfzUq1lH6vOBkCNaNCQlLL_e8xFXChcPBAquqTmEY7qjCgu1Q8hKSrFM6HhVZ_eM06JQ5GS4iMpJbYmzgJBEr99EJjBUXv1nsVOMg7I0gVQ6AU5PDxOXvZQPko3RJPg1-in5iBVXUsG8KNfjlg7R0_wDLSFL1qrkLBRC_FuyIIs3Crt8jepcCx-tl2RXGs3vQmDI3kmhzEBF1H8Xp3_XZ9MSuzbjHjksOWp4gtS0hDI-dgvYyI-bpFRj0md5kx3k3XoKzVJLFkp0IXi-d63EFBhMxX_3KzcT7iwlMZ-Gy0MFaBYy2nifuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSTaYm8skgSXj4bhEaEm5N28y6w_qu2sh9OJIId97QiLjn4douG838szjous2jcS6IiozNUiwtazWq7WTHbuOh0tMQyoqLREXbqk-KJ2t1OSf0JTbuUoJL5dzaZJzPO3wn3KnGFAzCUH2IQvfbsFjxavlCWpa0jSHSylaQlOmGdd-9teeF4UOItYBAWX7qnFy8VgrS-lO9P0YQg0IOq_x0Cpj2mx5v2GwDi6k-Q041Y_UpGFj7yuTdqkezw22_C-sylQo1SM2p6cSRD8ISK0FqxunokOqKXxiUdP7LD2Jxv7mh5Be390nsW1cBgS_VPVoWcGeBEiFLKHfdXXNlxEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-nVpagYnpqGmYdNOH2suznKF25tzNpDJ0mZ4ECqmQmy4Y49cKjHhIjFZhDwBCCkPuRBtR-sbdqrCS0UMpXmgge1uDlMCU-Wj-umCP9zrkQ-S2O26VnIk8zgkdm24czVXxM_iKC2WseZdsCbD-f_m_QFiF646clQ7fNI20Aa2sld2jWzXHNwbvpfpw8ANPvUE-56bxZm7rFxRjK83WafGNHzDMz3FvfmC3eAufq25IpXnx3AL9_j9VbWg_6H1vYAj5DX6nLT1CmppeAzwEgSfZsruqdrsWixnAyHrRKbDbDYmNuhycSHZCwJB6DReGl6V7JR_A6sPLlbrFerMCXPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt9roEk-WQRDSvZccenJXLmow75W7WthQ0gpdzonMjtYh9sSWwj-aUNY5BgooxmGhtqmXkF5hCZyi74PV4QlBbc5qu_21SXRxFfPneKwHkJ54pExBgWqwpp1ogsD1WbV_-HazHeOBR9X0kVTW47C64xlPOGD16VCtLe3w5WADPUJlLAfS-CtQN-z0ZGXdIkMRxRRC_eYYj4dSLVnVmDjRJdvy8Fz8WlmQ17BmFg0f_dWGv0Pm1I_gr6zCZILaK8lEp79XIsj4p7n3ZhKGY8qktnkOCX0SHPfuR0Zd6sEqNlf3zLlX8U5hhDtqV12JG1NMSppLPDloGhXe71KNbtPGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=YoAREfKp9ozJzCSqjIMqw7pxI8rJn8i1Yqa5XqPLEomu4fExiqp8JemoY7YqOt7VtGYHR_vKkqAvardxLDwP9-iytu1_w6hYkBeTG1jBVQNpCgobk711_XuT_biJtfHHJjJrm67BtoMg4hTOwFCJSK-iLXHki6Oi-Coa-fmJyO0PdfUq-6BAJj2v5ODH8wTNuQwSdoWv4Xhy8KdLU9lQCtF97RSHYt0yjMtFb_0ywIyrmMtxFzoKNjePDOydfyZgpwe0GIPir0jcFmp6ehks4AMzOMgE-52hvC_Pl_pXEQWCDoHkQcvHLpJN1J6-h7UKY-uNU0SaQIBqD9gPDMEazDkbLGUyzQ3BNbnst11DRiSAavkRcQSV3gvMHkGEUF2Ynbn28U3HST0tItxd_37q2Oa4irce2dnE-tZ5m9PQaTyA8H4HFu92J9bwoCa4bf4Fw32KiSgsyJTnT6iCD6Z7FugendI9bCYhuHHfvqpczHxTK6QHARD5uRXfx056F53giqXKVy-BwosiYCPtCDf_PEj2yI4czUuIqskJv3tNY2UslZfBV6Kfvhj0OnAGgfJ-UIwggC3X2h9hF221Os-0GeXu-EnuBLQt5_Axx4GzvdJtqDuiffwpWG69Wl1Bz-ilulIOtfrD713kJBLHMaudjKRZemipyvGhcHrKCSF8Uxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=YoAREfKp9ozJzCSqjIMqw7pxI8rJn8i1Yqa5XqPLEomu4fExiqp8JemoY7YqOt7VtGYHR_vKkqAvardxLDwP9-iytu1_w6hYkBeTG1jBVQNpCgobk711_XuT_biJtfHHJjJrm67BtoMg4hTOwFCJSK-iLXHki6Oi-Coa-fmJyO0PdfUq-6BAJj2v5ODH8wTNuQwSdoWv4Xhy8KdLU9lQCtF97RSHYt0yjMtFb_0ywIyrmMtxFzoKNjePDOydfyZgpwe0GIPir0jcFmp6ehks4AMzOMgE-52hvC_Pl_pXEQWCDoHkQcvHLpJN1J6-h7UKY-uNU0SaQIBqD9gPDMEazDkbLGUyzQ3BNbnst11DRiSAavkRcQSV3gvMHkGEUF2Ynbn28U3HST0tItxd_37q2Oa4irce2dnE-tZ5m9PQaTyA8H4HFu92J9bwoCa4bf4Fw32KiSgsyJTnT6iCD6Z7FugendI9bCYhuHHfvqpczHxTK6QHARD5uRXfx056F53giqXKVy-BwosiYCPtCDf_PEj2yI4czUuIqskJv3tNY2UslZfBV6Kfvhj0OnAGgfJ-UIwggC3X2h9hF221Os-0GeXu-EnuBLQt5_Axx4GzvdJtqDuiffwpWG69Wl1Bz-ilulIOtfrD713kJBLHMaudjKRZemipyvGhcHrKCSF8Uxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=ko_R0yySnmU6Gm3HlnfjUuZ1d9JmVbq0rC6hTzqGuqjYWt7VlxhEuTiu4G7E6QbGOHyUy372jmED8yRmZ_iaM0Oh_rRR9abkigLLPLMLldboeuCbWdzvDDPuzADPtxITEkQSuu5AqjEp_R1j14IcwUpnn2Pu-t9WEQSXhLZrkROsSJ7jQknpjHag_j5Wi16jUj1UpcNCSaBqXN5SBsxiPzKWuZQw2ICjarvZE7DevPeBjtVlQ9yk5urv1KpLdAHeeoqoPz1C0X7ZOlRMmXNQvUGUztKZkABHQVauy9Jov-Adpidij4KhB2oGnpOBGMrIlaGQeP7wsHkakkD90Aezfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=ko_R0yySnmU6Gm3HlnfjUuZ1d9JmVbq0rC6hTzqGuqjYWt7VlxhEuTiu4G7E6QbGOHyUy372jmED8yRmZ_iaM0Oh_rRR9abkigLLPLMLldboeuCbWdzvDDPuzADPtxITEkQSuu5AqjEp_R1j14IcwUpnn2Pu-t9WEQSXhLZrkROsSJ7jQknpjHag_j5Wi16jUj1UpcNCSaBqXN5SBsxiPzKWuZQw2ICjarvZE7DevPeBjtVlQ9yk5urv1KpLdAHeeoqoPz1C0X7ZOlRMmXNQvUGUztKZkABHQVauy9Jov-Adpidij4KhB2oGnpOBGMrIlaGQeP7wsHkakkD90Aezfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1_m76Rif-oy_peAJsyLGlqfiWkD1TvYzWuXNn2xlJdCxLeWt6WfGM5JyNyDqFCzCZzHtD46qjxMu2Rg6PYmxhfXJxWJVw9_1owg6P5lDEENLNc_FkoBltiWC7N9X4W6Ron2uUu_nEqf_-Ce1hK3vCJ2LiGYboFEbYRv1G2iUThLNq8T6do_d4gFCcoGddb1Gr5oZ9umX65nUofXffntJGDigoMjROs7BiM4yDKf9pS9uk7ZpuVO6A66CMSsxH5lKpOkwxnIxCtiEBlivc2vmDo_jzswXtceAE2jqCgj9XgSP1J7tQBbmd1CnaTMwUcf3vQ8CP8NUXHOYcmV3IncIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=ICQM8CyFA9yqubpAdlGhZLjOjSsdyeFqNkdUSKWqgm7yeohfa9dQRaaeWl460hvgskRf1qK_d-we6H-s-_7Rn3Q7lD6Oy679tUegj97xR2upjz8Tf12NE6tF090ZDz-eBu93SyubGxy6792CbXzRIVwm_I9JYovcwUpKRCs1pLy7XiIheWmCg6O3yXMqEstHnxmCF4S5lGpmP0A3F1EOvFiLYMbbPu8sycRCNA1N8XC6DQyDPAg-EeljL5FZThoI03HphY5QKI6BwHcHJ3i9QKTJoMLKdmKs2ewYdfERwTUPrr01dStzXpeQ0F4MbdRsLx-PLxL7MYi1GnOrvdOWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=ICQM8CyFA9yqubpAdlGhZLjOjSsdyeFqNkdUSKWqgm7yeohfa9dQRaaeWl460hvgskRf1qK_d-we6H-s-_7Rn3Q7lD6Oy679tUegj97xR2upjz8Tf12NE6tF090ZDz-eBu93SyubGxy6792CbXzRIVwm_I9JYovcwUpKRCs1pLy7XiIheWmCg6O3yXMqEstHnxmCF4S5lGpmP0A3F1EOvFiLYMbbPu8sycRCNA1N8XC6DQyDPAg-EeljL5FZThoI03HphY5QKI6BwHcHJ3i9QKTJoMLKdmKs2ewYdfERwTUPrr01dStzXpeQ0F4MbdRsLx-PLxL7MYi1GnOrvdOWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
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
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
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
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=lskXoMht8BI2XgpgGdXglo8-pwsEO40W9EW3Mf7IVwKYk4WswfCAmQKlachRjryx_dEWzKwtNIwnoqObZQ6Iq8aZ09v4NZtALe3kVXZrb3-DTo9xuThshAJQgiiBNY4LQEE4R_UR8gkmjRpHh0g9c3xB3k1xZ8Bxp9wu-ntDkrA5M0YOEVYiVU7HhmppwzNKpwHpwrQyr_Qa9uCEk0FjgQRkdKd7ED5_IsV-SX0HLeSbvdT4Q9xQwm9Y1PmmPro0MXf9xoedMRFO8vVdjbSmJd6ldYrFNezVBtkk1xPYubneGR6KpiYhNKPrKWgJ6uBSC9PD-jUtUOEpi298E59DUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=lskXoMht8BI2XgpgGdXglo8-pwsEO40W9EW3Mf7IVwKYk4WswfCAmQKlachRjryx_dEWzKwtNIwnoqObZQ6Iq8aZ09v4NZtALe3kVXZrb3-DTo9xuThshAJQgiiBNY4LQEE4R_UR8gkmjRpHh0g9c3xB3k1xZ8Bxp9wu-ntDkrA5M0YOEVYiVU7HhmppwzNKpwHpwrQyr_Qa9uCEk0FjgQRkdKd7ED5_IsV-SX0HLeSbvdT4Q9xQwm9Y1PmmPro0MXf9xoedMRFO8vVdjbSmJd6ldYrFNezVBtkk1xPYubneGR6KpiYhNKPrKWgJ6uBSC9PD-jUtUOEpi298E59DUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6eOrtybTpFm7XprrLZpWGpkToy2ZbDB12-fe0LazykzXZlyF-ovvaVOr53UURR1tNvJfIklswifcb75SBIgDXaSnbwRJ0Oiz7EUyfutm1PDEzMmBtDMvNDpnu3UQn6S9BUruWOJ5GkBKTBKEZMt1FKDvmfsAlj6s7Ono8lcV24ktkaD9nNdu9I7neUrJ466w3o_Y44S2N4no53Gah1iA7cUsIaQmWBDCvK-qeNdTvNMtlfUyj_Vpt1H6BOz0Zh8KG5nwxNTbiL5LBDoK4M69JQXYJcZ_fMlhZsX98hqG5MqErTyfQwE4Um_RtP8yconfIMwSvmbthHXtyvjWSqu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlSeqBondL3hFssRTmnPLafrJcYq4ilAXFrJa4fiXxoL19ytNwANxogbM3XPSkfS40dgg_XX4KJhpDeB_gQXq7TTOdiEr9ldPF4UNBvhcPmkot0bZ0heOw_ovJjYKdgYenkWYIhLoX72LZ-gw-_eRi7oRxn-mYvKWzMgQ4MLWgZeUAWTcZCUGQxdIEEobqHNrn01B8jalTQIN978dIJoLQF-GOlQykKTK-nfKE-1l7bMumq5v0SeQp0gmEeVYavyI2ZcAC1TmkoGuivbR5DZGsuky7RP6SSz7sefGdQ5QNRA9IeEMRRhMA3hEA0tred3G5F3fH86sOE59TovY8Um1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoJWX-_-Ux5B_5xOC3CzYIGvgpfRt2EathcOCMWSX5_sjtHj6ycEukXiyt3waB2fU86x-D2EILAWBzdTdWDdFfW4LLGr2EgWOM0tP1atZ1wE1U4GUc-VBzT-U1hjh-W-ejWeFbHPDpSNQ7xda8UB8We-qEjX9xRpQdqLj6Z7F5d3CcYSnf_eCigvTyJjXfDNYFBubAnWpfcBhA8YKkraiAL1K9DGKDpveL1lA1T-CKxvrotFQrraqYEtjza3KM7nvqWkH1g9OZl_2OW1VxoJtn8A0Z8jYiHBtZDy8vmsh0z_eNfIzTBQD07cgxVYcBviWl4NmRJeqNnoCcqPjj3xVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=jQOwHFaOLYEFK2UIkBrMLdLjJK-LDo81nfj55LLwvyxNpiz4w5N-YXL3WROqdFy4--QB-Ehij5Kny3kGXBGCyt06ZUISk0Ihzw-3PuUEv-AVOTzWJI31Lwu0okosMrAFLdxEp-ABcsMOqZLn4dILOTDhlHo5_Ujaamj4yS5pJF9pRB9mP2LKKWvTvk9RoQGe7iMVMqwe7AV0jCsZQCDqpwIaNya0PBZIF3098XCkkJ7_v3Lw9lqYfrhv-MjZwb2Mx89Kp9IhhT87g7BPpCZ0aDM9oBg10dIwfqy62v4reJMDHUmIYpVZyz_YccEqbdW1j-dnd12glRV8MBjrd8vdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=jQOwHFaOLYEFK2UIkBrMLdLjJK-LDo81nfj55LLwvyxNpiz4w5N-YXL3WROqdFy4--QB-Ehij5Kny3kGXBGCyt06ZUISk0Ihzw-3PuUEv-AVOTzWJI31Lwu0okosMrAFLdxEp-ABcsMOqZLn4dILOTDhlHo5_Ujaamj4yS5pJF9pRB9mP2LKKWvTvk9RoQGe7iMVMqwe7AV0jCsZQCDqpwIaNya0PBZIF3098XCkkJ7_v3Lw9lqYfrhv-MjZwb2Mx89Kp9IhhT87g7BPpCZ0aDM9oBg10dIwfqy62v4reJMDHUmIYpVZyz_YccEqbdW1j-dnd12glRV8MBjrd8vdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=KCAF3mIygkQqsF1NBTGPiX-os020onZ9_JxFlfUTiPW0SQASy3XjcIrIL8QqfzU5rnzparJa5fZgybehJBFqYNPo7H3NKS5OLslfrGhX3nj7Wl4Nqo5Vrjy0MOb-zKBrVh3-i4jQzRRShgpkewbtLXt_BFb64jrY2ZKhPfVHMVJx8PLrkatsWeJ0-sRnEMJrQFrGnJBfzVXggIbENdo3iCKGncCILi8_WltM3yGyHgIfIBMsEL87khQcrU6kG6eq15oMUWjnnzc5jccj7H2eMOQlitCW-PxqzunNH1WS3ZzIw4hMl7GqspVJvPy_pg32I-CiLxUksagGHBBnGGDAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=KCAF3mIygkQqsF1NBTGPiX-os020onZ9_JxFlfUTiPW0SQASy3XjcIrIL8QqfzU5rnzparJa5fZgybehJBFqYNPo7H3NKS5OLslfrGhX3nj7Wl4Nqo5Vrjy0MOb-zKBrVh3-i4jQzRRShgpkewbtLXt_BFb64jrY2ZKhPfVHMVJx8PLrkatsWeJ0-sRnEMJrQFrGnJBfzVXggIbENdo3iCKGncCILi8_WltM3yGyHgIfIBMsEL87khQcrU6kG6eq15oMUWjnnzc5jccj7H2eMOQlitCW-PxqzunNH1WS3ZzIw4hMl7GqspVJvPy_pg32I-CiLxUksagGHBBnGGDAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3GljmvI4hpY3dgSAIOmhwvbhX2iFZUr5eVjeBhj2AX2z6-GjHviltV9FYOv3eDZHnzfytHxChGgPXBThGywYKcooaeFAGyfi2IvwZlAlvNQcSWZ0cwrO2qlBlXkUX93vUjnTuuIS5H94uiDldYxGL1xAVn0S-KPfwraOyIOIxkoRufA3LUJ91mFo-65csnAMUIGqKJ1TMhIK9h--SHutR6mIen-Xykkb5pXGQIeI0fNZcmCT0qBAfNmCX0caiY31JF5hlBTZgCmPmPaxL893VjmmnBMvD7D9syI2ZLdS8h3POW31UhM85hX926HRFCGU4JiMEiYv7brBPpgrvq_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrkBiEFvz-kG4UHBDDyuIzl5zSg-MfhUjjVvaESlENFiUSEWEenEXxYIVtBshv4TM-fUVMAdXT5hD8gpsrMSEMojkJBDoiLrDluCCJ1OcwzOyckoCFofYN0uiIaKNHq6MWNtNydMALeI_2W7WECfZhQLzgpDsK0Tm-2-4VpTRLaJnKVautFnsziHf76DlMZS7Myzxi9xkVwrj9LOFQQ9F3oyKG3IeZtoQ5oc3KpdX2RtnJTDuMXcZvN0TZjAkBoql8AsbQx6MkAM8Hi2kOCB545b5EmTywBjGTV_Fb7ZBcDTJEBssp_QovbKpKmgqlqbS39mMt2sOKrRGtETujR1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvhSr0CKgQQu0GlRQJUPgXueBhaXgwRhLvPsISxcKSGday8pMHqbLlXcPkQSBuBp0Nr_u9Hx0rfoeScS4MLU4Hox99_5SqoSB8jC8E2QhneNVjGY9WD5V6cwa-4nuB8_ZHoCvH4oSrGC72YU5rCjVlTdcMFYESezJ-1RPQG-xlDXSCDVzP8noCPeX5pRMgfcAdXekGTuExC-61UGD_l4hly5Nkdc6i5nEhIiMWmp4EIKotjt2JnMRI9-saXbGsemiKyrjnfh2B0RKoO-_v5iQlBd5uWmJ3IA1M7lVUbP9cOL-T2mWsTX-WIDrGOPK5j3nqFJPBOuwhWPenGRUaI-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOhsrfImEBLA8rRCSpzrCspofzKQe0oO-mDcVR8fJx0KQ7bzL3y8iTdNMdoUI3GFV6Y9enzfDHdui_ClgR00SNAEOUMy9X5qk8qPovyThxDnowuwqjUXqZNOQPEMCgGtxZPbuBmjm1kVkFi3oy3vXIe1plYYCVk3W85Oe1SfzTlCPzrnnGybKCEjFUr9kEbhKu84A_56qMO4uvQBBs8FcFhr1NLWCt35wLobEpFraeWSfR_F08K3SiRLjJ_wTr-uwJaYiEVf3YBVzXm7T7eG3o4YUZT-srMi_acZgD4hQ1oHAMdOaNsZu-TkfZ291DDQ9xU9zUqCPFpWs-4PWvCzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzMdrpRbvY_TO7E1ywJYOSF40PTokcfqhPj06XR0LA4gGEpTumPY1rH6zGL4FxGJ4z77rcMk5Fs57DO-i3FacbF5ASjhRnRwLgYA_jCaWEVZv0OUCQTM1CqESK29D1HB69K3Brlkgpy0Jw2PTU_X-Bw0UvM_hQhNOLRhGCig-sGc7sdhJjXb50_fp3bhiNnG6GOwZuKmrz_l5vTXwhUplSmHQUvjN7W7NSOG9yGccJXDPX6zksmGFYv5eYav-wWKie2VuLaeefnLbjh1j00IiFi6tX5y2gYDyKHQGflrWN9C_mPPK83eUSzRa3dOvp6cAd9oQP33vTnpGx0_1XF0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wjs7fhUdW_WBaEd4pNjQBlpS1Pa2QEHj26_plCWbVjCcVp1LKzJIbDvnUf984FawomT_ORIXWcgdJtPsd5b39fUkujKqzEebSdVqbRBUZTmZKQbz_ud_NILjVnGlTO-ZOZub3PBeWKnPnCDx2L88EvyrejoIDwmVv2mb_xt53ibr9oGWRtmIx4c1BQmcC1vOOS_FZ0anbP6JdlGe8U3b9HvHQRBBZ5SiXRo3foGjRXZAghH4jJJLQKvlN7iUJBVWY3YmTfxMIOheXnxC8BcaxYV61CKgzmnr2_qxL1fqEGZCsCST9FuN3EqVF9hbVk6sGj9c3BW5sCKdz9uuy6jIew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cboyBcOihFaSCYPR0KYSRsLseO4j8WU395DMeFG198artSGuACSJARj_jf4LCljYtLFI2Q85V0kiaVamx3WP-zIbO-geVeoCywPS_B3w3vaK0SsQmzQGcbHk5dedRH8wtMvbgn7NzsF0l373YlpB7XlgMv1p2diTsYVcfCoyAvF3-oogyHY-jRvqWukXjSaZt4Re47Z38kgYUfYuKP3h1Ozj2i56YBy987ATnw0d7304bymGvvtmaDrFeRfO_qtpQ0qxwP95peWx9siftX0INwxPkvXGMov3N_VrtZkWZCy3I1CtMvA9cU3riedv22GTzh0XBe8oMEWsis9Cs-y63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3xOpSVl3o6ojKb2fo2-K8Gd5cPcF8z2lAGNM-tQn1jLxzkbSp9IpYYvrFKyO7jXKSS_ThRHrj3QkSLAfqbkk7IQy0XmJjuDzoTfg1QcNeyZ9d0y0EuCD0bvrNkXvO9bga-e7-6K27OksiZ7l3Do3Lq-qUz5tbgmFAlTCmuFciiqhQcb27slEJT2QLAzzV8SChuIIzpieuKCLu-iaWlatfQ_LJ_Uq7yZgofIOTlXHbDfPXQQsUZEROhlAkYGfzBQ7zR80Jwxr0cPCW5iKVi7vZt2JlrKCr96dYc3mftv-CZ8dOq5w1xpLHISMKVye6XibidxDrhk-dZkieYR-5Ba_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdsW3iGGtrySoB929jDehL8o5TsHfJFfM4TmpqPyDPhbV5b7U5wS6Gr2Be-w9BCwHySTqGxyX_aIxjuc3aTDfA6oDjBSg3DEq_qZKVrCfNo-FEudP3lxbNSG2grjOCM7gaE5fGgKutHI43AQLN-A_L0fu0UeU9by4gko5OlQOcx8i1idVq1Qp6lE9LxY8GmXZ6lCss22o2RbsNriV3st94zlpAp23_oPnkP0ewDOp7Q6oSW5N8vGdgKPDZtF0ORdLJdfAr4Pl1zo3jQtUh0QU1W5s8pJGI0D8eQilXp2PamsFte3L91itmzKmyeY62jCb_Ldw0fNj2Sfun9obzBOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJmEcc9EcL_Kt5QotSDsRv1FKrZHmZGLabBbLPvvNAqQD59D8qJlB1MxfA2qRLI86wmeuTEv2CueJYe1Al6shERUwKc0L53XGirfSD9ZQIbLZ8BrmK-Qhp9YHoHq7VsdI_yeLCUN-T4Gxqt1WSJilT2NrIoYrRHrR2QXXUO0-z9vq9PVp9MJytL_KpY0Jr28dBMQ0gOmi_XwMUqPSSWFrTbMEz2-jn0mBeeJTR7Ha0Y5Pbb69nIVlsq39EDkNgT7ESxi5LsHop-C_RwETxQcWqAyjaVqi9w5tuvSSAnOyQ2ekOWV9HlNXEQBPdJmf3TQAuG1g1Ndpe1mqQflll2FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G28vcZmTVVPnNpO_d1W1X4bcDbjNE5X4MnRK3RtwyVusQdB1Bedgq06kVeFTpC2Cs3orA5HlcGHuALwt1egWCn4g2CxUEVIFSaznkidfIVKTDZrfT9TFC-mcLWGZeHgmflr_8-vi2FiIWjSf_xu4lye5TpELk5zZkJmgWuXG7Vp4x3ooXlBKobvwntU0OLx5aHSQOK4efFIywy57vQ0_jeqm2eeIUXnsAT3PC5np2DIYAjHEqTy-YPj4SRbpsGrkCsKFXU0K0-Hy_Cm8fw8B2Cj-wbTyPbpObSsqrm-Zp_o9R7Aihd0p4iUtHugBphw9oNY01yefEJGogSb01R83Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmwNmlF8vk5diFiSGspk79DUpySAQfzEV5-vbb9tde9fPo8pydnTFteNpHxOR-KJXXte1M4BeA_CkVk8Nk6PF5SjKlwwVqg3p_1eztD6Sm2J-hnbGfcIqgaPYjxwt73z-3K72esyjif79bxUn8MtFJ9JUQDOVFv6fmuJgdP-hRZ9siWYtpd9RMtbyznQgz9ULLsb6K_Rw53xUO5py96ym1Skcu9oUzgsF9F0l9wXDAYfcslCzvZ888jeYftJfLqmbgbomi4MVkE4869Twc7ejwDH3T-vrDCdXnr1SH5pSkeiEu-Ypx37vO5llGA2qJE-Vmt88dDJ_gj8qwntGpnccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_22uooKtghVuZaC7B-Mj8QzHttPNpquTe-OPB2wF9co-Mxj0KwEx1cAnmnNSC44rrsK5jRER0a2UcCCujj1-Q8X4sZMNzxwmcHo1rmC7Xs5epBF2_I6K7L5daZJLuKwXREQnyXis3xRVgGGWTA7WLgx7GW2fMAE1n-AUxTkVCWBIf9k5agkYPmQkvMwBN9R130wMUV2UeHBGPKqlnO3Uuii200DkZWBo1-S7UfYm3xv2o05GnNVU4G4OJFquw5G88HMAH7AtXqFCOldd6pHLkZUtbFrH-TpZut_dch7FtRX3UpRqoNE1D7rn5TcGNtL7m0wWRi48e_fOUNx8wfeKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voMHpoXt9ObRfwPUWigyI2T2ScaMwsHO8_ot2uRzlMQC-lICIUIdgIutJWdENI3-b4d45tvG6E1TXm_ZCTESrCb0sziZHCXXxKIXSHq9om06f1ZYSDIAE4zF36MnGC5YDVVm-5rVjzkci9aCqLDJECUfGy1dqfGxZsdTMS1o3Qcssvse56DqMdh25-QMFcYZyMe-lGLcevhmm4W2QqWMThdELb0ucBY5Hf2-CVErs-Qd6uzQVFk2Kj0oULvHU4iXqgu1munNIz35MPLn9KHo_PcaU4pyE0OsKMMduMNyuzW7sk2FBfFONqHCwVHjZK6gNjD-_YqfoOooe7uHA3in4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=HOSj6J6mdRIFGz2mECFPYxzzqdQSsrJ0Lr_QnMZCCZ2pD-xQYEEdWlXaRq7dWOCW1pGYxTvGCgfFqEdw6dmh-RwPu7s-_-m7TazGYRZMKEAB1MZBySBodazaes0VDuU5uOH6SONF2dPartki0QiqSgb73WDmJk4-TFEzdrDq24YfPi8DX0oFmVZvEgMqc0c2ikEAPe1112l9OnXxnauZCyWFmoTMaNNVD9vKzaVQcxDi7lye5mscfYmx5gGvOh7C8KhRQ0Dc0Vam68k0HZlKofzwErf75diNUE1RAfbrqtgUH-V8vKLzd15yIavRdzAGdUgPI-aKwFPOypbVlfn-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=HOSj6J6mdRIFGz2mECFPYxzzqdQSsrJ0Lr_QnMZCCZ2pD-xQYEEdWlXaRq7dWOCW1pGYxTvGCgfFqEdw6dmh-RwPu7s-_-m7TazGYRZMKEAB1MZBySBodazaes0VDuU5uOH6SONF2dPartki0QiqSgb73WDmJk4-TFEzdrDq24YfPi8DX0oFmVZvEgMqc0c2ikEAPe1112l9OnXxnauZCyWFmoTMaNNVD9vKzaVQcxDi7lye5mscfYmx5gGvOh7C8KhRQ0Dc0Vam68k0HZlKofzwErf75diNUE1RAfbrqtgUH-V8vKLzd15yIavRdzAGdUgPI-aKwFPOypbVlfn-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHB407KBurwWFMQSJW3MXOLCVJNc0tssIUUAFpHpkyx1l11KpBDVN2MYVd52MwJFmMfskq89LcP_xtT2ldXsa5vB_IS9FP4i-kTywox1liY4L53hTD2dQ99vGZ2OymXwpLwigBNemTpO-8OzsORYIsutOaqr1N8_ZtjhfhAi6cmRzfcC7rXXlHmX_JD44flFfRhL9RXupd_cpv0vAgxWFS9btl0TXMQ_xzC0dvKFXHrHtfDodHC_T5SEkv2PJPkQzDGnPeSoi-8treKhsrHKWaV7trode8seX9C66IwNe1ZpOsjcKs3ZZr6kr7tmNHK_wGkvhL6o1nQAUdTJ0Nm0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M84sLcsDM0YEdMuN2e_nnUjWNnIagWT5sZZ9-fZlkvYiHmDUWMUwNr2Rh1iqRCN51Jose8s3vGe9KRuAGho1tt_344LRk4afsUZmokFjbhBDjmo6weMa_mcVO4Z-uIWh9HbBwic3colwuFcx0NVtpyYyJv169bZqwr-QyLf_TtukCY0uJ_AyGn8FloQrQkl-ps9V3eRrh_3wUcAh59lRtVLad7Pcyz6Cgd9Q8Pkg2wEH2-BLDkQq5zQYFlA25YUd8HLR8Q3T_sFDZixlcsdpXRtAjiZuZJ-U-NZiCEVs9FbbUJevVvJ-9O9qLjZfNOvpc8HSoh7c2mKUBSQ6t2AQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3wCtY1OU_8s5RGDXggR-XraJlcMnpNwCe9hzHqC2ErbXlzha8xdzh32JrPNPi0I5Fd19jd7CnhrYn0wtw1S0lVWKMia-Zawq2axLR_dcMFrC_FsUPIFeOHnHWin7xN74K5ujF16G4qxTGzKBgZaXrR1KJFaemw0EUZqLSguj5nWGVAhDgu9ILvHOBgq0bis4WTLM6CjgGctEiU-0DEZA1_MByOhfo5CZ5Ed673NvKdvFnRyUtBd8P7Z7WtZs739vGLHd1-qN4WkpcNhdZhkx8knL7G374Vr8JycKUQRU4q1_i1kzlMdTRpm1a6cYAexjddnBvqIaSBbXoGGmPpEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMAEl94lqDJhFRGjln1bAgKXBCiUH_oRwtW-ruH6T9wP7wa7tw7GlRyKULKf4szHv46eJjhGCGvm_ET7DCdeYYOuQ_WiMMjhy2C2bNKkhHRn2FIwGg2I-f1VUkCRpzosm341rauH1fXuHaT1H63W2kNK4VJtmQHISj5ix3pcb07vDuGBM1DwaujdKPe6H_Uva11RyRYrnee5NaBMz_3GYGRSikcPzLDs_Bmzma9u-6RXmnsC8Wy98odSlPWEKNSr8UhsvJxLYLfc1wwzkFPSXy6XacGUnyEr9Cwl9Nn2BD24WYkipzySyFYNJKWTIhtVl5f6BhZfWPmvgkXx87Q2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=orhmuDHzXJtmiMCG_2uoEOqYW6UOLL921mLtY29o2Ktt89sVo19HDARupSHHsq55P0vDTlHMxTLRrYUcoQQ-xu0cQo7-VVdS0UA3OEDyBcQzzV7d2Tnxo6ahMdK0bCL0dy14ADC6Q387tNNjmUcoSHIhNWyOLtVZFn4Qk5zFGLozUp2vWxnLHWc3Q090jL22QkGbo1cud_mgqTCd6WZYnL94mch3IbSOzC8m9qhxwGfxMF_5JJ5PjeCFJ3xlZMBqN_igwjdVz2GfNkn0GboB-bRdlfRT5mdxmci0lgCd1WokR0eM0H4lUCSKWIQ4qiAvoQqZE0cK2TNeoUvbqx303A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=orhmuDHzXJtmiMCG_2uoEOqYW6UOLL921mLtY29o2Ktt89sVo19HDARupSHHsq55P0vDTlHMxTLRrYUcoQQ-xu0cQo7-VVdS0UA3OEDyBcQzzV7d2Tnxo6ahMdK0bCL0dy14ADC6Q387tNNjmUcoSHIhNWyOLtVZFn4Qk5zFGLozUp2vWxnLHWc3Q090jL22QkGbo1cud_mgqTCd6WZYnL94mch3IbSOzC8m9qhxwGfxMF_5JJ5PjeCFJ3xlZMBqN_igwjdVz2GfNkn0GboB-bRdlfRT5mdxmci0lgCd1WokR0eM0H4lUCSKWIQ4qiAvoQqZE0cK2TNeoUvbqx303A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Iq_nEH-BpGFMTB0ZbsxIXtBUGx5a4ElXG2QsOHKPK_yaK6t0NmMGjOdB2ahyJlX5eoSNYXyHUMOW4ZsxBBn7ybNeLfV5qc5IGhRPOCYo3Huq4kcG2BgvFnuRK3PxuGt20z71xwYu96n5zp1RTtZjFm9FvdiH4hjZCJHGbpHtR-Dqit_9UkhrHvYe8WNpKkcGPK291RioXuJIQdvbwskGbMjBQbMP4v7JAgSVF9o60HNw9GpsJ7fYVF-LhXvaZQfUbDbV_cdOeaF98sEYD0w6aUqx-EyD_3mE2DLJrFJDTblB44h3j-6YOJaEHx9cteopc1ojsEb5vwK16OKk-Xj4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Iq_nEH-BpGFMTB0ZbsxIXtBUGx5a4ElXG2QsOHKPK_yaK6t0NmMGjOdB2ahyJlX5eoSNYXyHUMOW4ZsxBBn7ybNeLfV5qc5IGhRPOCYo3Huq4kcG2BgvFnuRK3PxuGt20z71xwYu96n5zp1RTtZjFm9FvdiH4hjZCJHGbpHtR-Dqit_9UkhrHvYe8WNpKkcGPK291RioXuJIQdvbwskGbMjBQbMP4v7JAgSVF9o60HNw9GpsJ7fYVF-LhXvaZQfUbDbV_cdOeaF98sEYD0w6aUqx-EyD_3mE2DLJrFJDTblB44h3j-6YOJaEHx9cteopc1ojsEb5vwK16OKk-Xj4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djFYB0FSCXHXAbz0kklbOpTvKDeMwVQHgqBwB-hdFmkYictBImcKqNeMf1SvWTpJnNh8VDaNtqGfMPPv2iyGCka7iNeENCQ17qXrUcXWqgF3mO-ydsVhpyDIJ_U6HW8AKHhaEkxxoI20jI2xNAV_1XED_fNQZpjk8ncl68fOnbFNBuKeWqpgQlJjfO3zAt5H-y7CumzSxf2PBIanvBB6TUJXJdpn3C9du6d2EbRYqzrOyPnpI-9Dj2HrYKosVeUj0Z_tTsLwGWEmsdKNT2zM3jHgz1MmhvP-4IsVbha0jlei0XHorycGZtfA-KcDjY5U1J6r5eHodAa4pJ4EOpFDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=SImTqFmSW-oEVY7bo4fqDiSgw01_T0W3LymMS5aZ0Fj-wFRQuvF0siwPvJvaznBIZDUHuj9i2AgbDODCSjpx5DuIqHWaVqv0bhRr_B2xkP9Es6CYV29bMY6j7ZiaKKWzEqbnar0MXj_ehwcyQ_qlKzEl2f1N2zfaEpOIPScvUhihaurnaVmvrynetkZk5cRO-E8Mc1i8PPHAdBkjkRcCMVM-I9qp6UqwyJnymYGW-YrBRXGYHz-0G_xVUBs2tGQARYYIAxEopchm9mAk9Uj8KFgJwWeylqtjg8l_pyCHQcz2nlmv0Bx3ma0-EMrAiASg5TrNmQdL6tfwEqzn6u2_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=SImTqFmSW-oEVY7bo4fqDiSgw01_T0W3LymMS5aZ0Fj-wFRQuvF0siwPvJvaznBIZDUHuj9i2AgbDODCSjpx5DuIqHWaVqv0bhRr_B2xkP9Es6CYV29bMY6j7ZiaKKWzEqbnar0MXj_ehwcyQ_qlKzEl2f1N2zfaEpOIPScvUhihaurnaVmvrynetkZk5cRO-E8Mc1i8PPHAdBkjkRcCMVM-I9qp6UqwyJnymYGW-YrBRXGYHz-0G_xVUBs2tGQARYYIAxEopchm9mAk9Uj8KFgJwWeylqtjg8l_pyCHQcz2nlmv0Bx3ma0-EMrAiASg5TrNmQdL6tfwEqzn6u2_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFESB_iqeKKOamTEIAoMFDz63o7f_sIt0SwPxkO5b8Z6rtcIf5PVEuZ9LZhtN_Zas4eWvYhlO8NuII9pNbDS7jEU62W8cGJ1r_t0mfHNJkuioAJS7oKMLL6msxKIvFlN6CWdr_PGeK9a7JA-lqwWlBZZNpS8wD3zFB8X9R6_QF9fYVGYfuxjsSLgBOviRgBgPFOzyeqrKulhxJDxDTSzx4vl2csYtnu18NpfISdxbIJCvbV6j-c7rmQqoS20Cqpf1mH8GDO4Bv8igjb7pNptFEfBtQHICLcOFgMSta_p-JyXoMFpQIyogeeTGJ4rPh2u5yXoANj7vT08qLc2W9aEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJXwZBF5vi2B0usGRZQr-giNpoaCqFqtLDPXpFypjc3UAOpwp7H3xCExD-zGZWHgxIKZwZVcHhVLQrnq9J97LHlvJQZ46zxZPNcL-UcwvYoU9J6twCTzdccseRQWV4V-CRACOF6EsFzYAMYy_dPzb-msyLA8hYsk3VmBeZ3j6VVaG9ASM2gq7sWhpdWIwQcl83wiR8jfTN3XHsqMrPlPnFiWGoodC5YRz_Eg5vnzh5Ki83292ZhPaLaajmyqghRqNBii5IIuDbufpZ4Z5TqTlBm8mfjiCjvGoZ-es9Mb03hWnTe1TGmO73uAO7Ko2Xu1ukJmkmcvwrcAxMTpxblSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpalJZMQmbEzurAg-OSGTtSz97y5cocmt6i5JTg_iN2NP03AlsXO4fhg-U7IORA-G60kN5TCAEHtbxGpI62Hd8DxAI-Tpt-Pm8hiT-hhCZC-w3PfNzp2Uo9ziNY8rDvNVgJeb2oJ_2usyQ3egqcFNUn5Jj_wy_WP-DsWEmEMzfmc_VM79RfUvHw-WXVfct2Vb39VJlOmxfbYzY6XmznnfEheX-_JfqKcfY-ji3Wysz4InynuB6eJVUmB88gixdHcyghFumhz-4xMnoAkH8ZfmP5DIA6p5kWRma5Wa9bFubn8l6JEtMIvICwkATlW5rD6eL22_HvCblqAEhrQlrKP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
