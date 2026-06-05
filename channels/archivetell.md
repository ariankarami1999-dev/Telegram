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
<img src="https://cdn4.telesco.pe/file/t8omcVpZiqBNxLhDmlZkctYo98Zb0TsmiYb4uHXGKNJqyEUL6UQrR83fKM8wwRyvJ9oHUJdf9c2zmgKeP1WCkRE-g_ORiU3elJjB5izGlufunRMHn48VjAniw8erLpu6Ifk8hS28vE3cMOVAryHIFbyG91g3-Dj8ePEv3H8QkwSMaI3x1iSjEoRgxT2KLe6sbnphN8u5CyrV0QnkLS_KAK5GBxYwD5_27QthSUWJhxdaHw79-XzV1bMBstCEqIPV1d11uLfdZZfVOw7oHX0NjtTC0MQxGCkjXpTWXcpCAR557sk_LMPzMpCIJBD_crIRzauH8qENfcffXKvDXWzWQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.03K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 03:29:29</div>
<hr>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 68 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 257 · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E62AK6-OTpyHrVviRdxp4oYRQHYCZI0Qawd_eZ8I0ZJXhsHvEXh1IBiPm9tWDSS7KbxzeUDHhW-HTaH7sGBhsE1O_8sxtUtuTEU5jvD-ItBfvzFbtYJRClKMGLRWToL-HokPlsk24UTxlxxDp2ltR39s1mfvmSE2WZj0OEYMtgpKuR3KaqV4WbFSICuaGvstBkHXmo2Bk0BZdaxEm9wN6F8dyrUVQBLmWEjsP4UCIEvh3YAEQPVYwl4C94G2d_5rv_fZwA-mA9k1hu_uH5UeyXOit3sZL1he9j2y6E5HJMnMoa66a6ZsEtle5a-hXeAUtr942WfRQ6bj0UdbY4vj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
UAC SNI Spoofer Android
ابزار متن‌باز اندرویدی برای اجرای کانفیگ‌های VLESS و Trojan همراه با Xray داخلی و قابلیت SNI Spoofing.
✨
امکانات:
•
🌐
اسکن خودکار SNI از لیست دامنه‌ها
•
⚡
انتخاب بهترین کانفیگ بر اساس پینگ و اتصال
•
🔒
پشتیبانی از VLESS و Trojan
•
📱
آپشن Split Tunneling برای انتخاب اپلیکیشن‌های عبوری از تونل
•
🌙
حالت تاریک و روشن
•
📊
نمایش لاگ زنده Xray، VPN و خطاها
•
🛡️
مدیریت VPN محلی با tun2socks
🧑‍💻
پروژه کاملاً متن‌باز بوده و با Java توسعه داده شده است.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
#Android
#VPN
#Xray
#VLESS
#Trojan
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🤖
Private Link Bot | اشتراک‌گذاری فایل با لینک خصوصی در تلگرام
دنبال راهی هستی که فایل‌هات رو سریع با بقیه به اشتراک بذاری؟ این ربات بعد از ارسال فایل، یک لینک اختصاصی برای دانلود می‌سازه.
🔗
✨
امکانات:
•
📁
تبدیل فایل به لینک دانلود
•
⏰
تعیین زمان انقضای لینک
•
👥
محدود کردن تعداد دانلود
•
🔐
رمزگذاری روی لینک‌ها
•
⚙️
ذخیره تنظیمات پیش‌فرض
📌
مناسب برای اشتراک‌گذاری موقت فایل‌ها، اما توجه داشته باشید که فایل‌ها از طریق خود تلگرام و ربات مدیریت می‌شوند و لینک دانلود مستقیم خارجی (Direct Link) ارائه نمی‌شود.
🛠
دستورات:
•
/settings
— تنظیمات پیش‌فرض
•
/help
— راهنما
🤖
ربات:
@Private_URL_Robot
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WLYqsNMsZ_tNF7L35VFz7-QejfmEWsCJmfHv_npPcWcp2-6WksHGNdlpzTPE-c_9Q05NSwTPIhiUkbBzFUaLDfvaYsFd2N0qm-TTSOwv0ZIa5vZ26flO6YQ_KN7HLkafte-eMPxHp0ybu4LWhqa7s9Tn10efqUb-Rh2CP-fyXyZJM_0PRgXCU9iX2RFxPBPgNu-fsioeFl6GIgvuXy-J24wZP5_xuw-4o4RGx9GhmrXfvJW1XhRg8a3SE-U42naItuRqmP5T1Du8L3DPs60Il4URsIaa6fscTouGQqAlIwa2zF4nv2_djoa7XwadQQzjJFhHGZni_xjrIebB1hc8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6025" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50
🧭
شرط دریافت: کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 49 / 49
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 49 / 49
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6023" target="_blank">📅 20:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im7TP5zgpZKcxgOsTvezDdl1Kxh5rCFbHhKMxuxY_aUENsTc6yr5pjQ4sqFnUbDK_1EMzWjzkiTkuaEFBdkkMi4pUYjT4Jv9Fsn8iM3DrgqO8Lc_EMJ_ftcqSqOUgmbobSsc2j3aGa3Eynr--nMkfhjBDOJPk3WY_vjMmG6MojOqOAL4P5rUg97wTLu0viAxD3P2gbuF8oeWPrLBBecq-K3VJaBtpgpqiia9eOCvJ2emM3so9MjKxoMWVlnv97pmcLF7qiHn7tbhOhEs1AO1aT6YtuH9sx6mFSdsymJemvsUvg2_cORW8khtboFBgYk3s1FzaMAsG9StoXSxa9xDAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXqZw0SSNy4v5uNcvGvt9bv9Bgag67l0K4wuZ0NhhYhsz2Xir-_1n0sIRFqFU1Eohpl2pDbERnc5OwV4Tx_VzNcAwNGkPb35ewCpkslS2zhqL_0wa4WDjrFX5zesJ6TEUmizU4vw9gChnzg8gBLUgGft8uVNruqDcZNb7wL0WNnIFFWzsgIrGEen3cghM22w5g6ZlIollSLe6cGM7kHyJE0niDJvq04dQl4wl1Sgkhl5V_avg5WoaLihGURk06CcnnoypWVw-FIK_uaid3OIzD2mBHpF20P6HUesLanwE1L4Ud_Diq-wBO5_vNEsW0jACEHgXI7QHVVZTCrF3qOGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJXUKABpWo6V9hkUD7ObYc15067MrswMALjkuft0LEFFOE-TyX_nyOJsFWtifW1tUvqWPiQ-NFQuAQZl1RJJjdCUe552I4zxb2r6C53YxpobRcuyRDwHLK35PNhAhQwenKakBDZ6546YN3viUX7Fbf_JxbTtU3ZkreqXkbwA5LvXz1olW4173u-ZyaTTr3gowKBxbgIrYC5U7xab4iKGR_C77ilBaBQaznQFRL1X34tZVTqV7ZOsvAl_Erb56U9LFVXWaflrL3xVGQITJn-7BMianiaIkKmE0lqLmSzk-JwwEKIn3zdseRnkh8QbLneJpKe1OQUrAJOCDbVstAD97g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
ابزار V2RayEz — ابزار متن‌باز عبور از فیلترینگ مبتنی بر DPI
ابزار V2RayEz یک پنل وب محلی و تک‌فایلی است که مجموعه‌ای از ابزارهای شبکه را در یک رابط کاربری مدرن ارائه می‌کند. کافی است فایل اجرایی را اجرا کنید تا داشبورد مدیریتی در مرورگر باز شود.
✨
امکانات کلیدی:
• پشتیبانی از Xray و Sing-box
• تونل SNI با قابلیت‌های ضد DPI
• دامین-فرانتینگ سمت کلاینت
• کتابخانه مدیریت کانفیگ‌های V2Ray
• اسکنرهای CDN، SNI و IP
• پشتیبانی از Psiphon و Cloudflare Worker
• رابط کاربری فارسی و انگلیسی
• بدون نصب‌کننده و بدون تله‌متری
🔧
فناوری‌ها:
• توسعه‌یافته با Go
• پنل وب داخلی
• قابل اجرا روی Windows، Linux و macOS
• متن‌باز تحت مجوز MIT
گیت هابش:
https://github.com/macan-dev/EasySNI
آموزشش تو یوتیوب:
https://www.youtube.com/watch?v=Y3tVfMqgys4&t=28s
#OpenSource
#GoLang
#V2Ray
#Xray
#SingBox
#Networking
#GitHub
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان
دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:
1. وارد سایت
cursor.com/students
شوید.
2. با ایمیل دانشگاهی (.edu) ثبت‌نام کنید.
3. فرایند تأیید دانشجویی را تکمیل کنید.
4. اشتراک Cursor Pro برای شما فعال می‌شود.
⚠️
داشتن ایمیل دانشگاهی (.edu) الزامی است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وایرگارد...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knrBAAmXBkZKBvel6aNT-ACP_EaYOhmop__fFOv1kUHiTgkZCfuOTi_HYUS1PYkVZhjl20rGO999fMfN696i4YqNz-gzk4Hq7rUJUgOYc-6yBqCtOsuAe6BT1Ih1OfB3jG7EhgIje726UyWxZPr1A1SwO_3rS3IdBpUYXTR_RthMhwJd-sAf_RHgh4dQB6cTYVS6pQCQKA11RPX98RulrzSouYp_7JLpPwZu3xPjfkT8IKZkzL8tcJyQ3AApNS112ohYirOjimuhOqpPnR6GtvWEZJfhX9G6UIDW6sA6Byf7RkOioA9Jyaco31lDiEsEMZz4TEjlvzTyH4s6QYuaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUvSEVIx6ONYQtOQtGoMwRvF36o1Qb2LM36jJCYNhWdxMX3kv3zGjgQWfphkhNJR1laESHxeY1703gNi7Ef0M15655EGRBGclmol2gOUHWOcRdesjiryDeCVEF6iyCQDf3aiwKhl3WwECgP2bw1QmbUoY6aRkpQJlu0Gcmx5GrWPagj-quhKm-w3T5PYYaRSr4BQc4MFfnO4vVhSOXhAD5nw2dfcw6OYGIXrTGQsnK7Gt0xcfLTkOflu6vcoC-ZGEBgHT1RiW9fxTpJHfGuS-PiHNAvuTDeL5Yu1ggy1hk0n4M5esxAaCWF9rKtz06xdpUXPA5E690tgcKuk_AXahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2GVQudLlMZGjyrYEbceFQr3pKpfRwWNZvYQsBg9MJKzoxiDPrjEVYIEJqCoE2n9zeIPco5eoyqZweXSvYhIxbsL-Z7dPO74iN8fQrDmjvx9XIqOx8dMqXxiy34De4CEpG87tnq_weXrT0qAnRcPVHSLePA2c1mZEW5y0hE7-rwDbIHzHrCcWV36VtIRmoHaoLuCGgF6kxeLUjiXsQfG6GQrhU2MdZyl3KgukhV-YeXkXTtGl8-YatWDws_haIIGRvyotDiU55oN4JL_geantLFG7Q4tL4_Omc5F5m49KIvo1vYlBUJ13c5A2u7Hz_ThhqH-v29tJO7BLp9BeTLYaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک استارتاپ به تازگی ابزاری برای تصویرسازی با هوش مصنوعی ساخته است که در جهان رتبه دوم را کسب کرده است - بالاتر از گوگل و Midjourney.
👀
🎨
نام آن Reve 2.0 است و همین حالا منتشر شده.
آنچه این ابزار را واقعاً متفاوت می‌کند، نحوه عملکرد آن در پشت صحنه است. هر تصویر به صورت کد نمایش داده می‌شود - به این معنی که هر عنصر به طور کامل قابل ویرایش، قابل دسترسی و تحت کنترل شماست.
بهترین دقت متن روی تصویر در میان تمام ابزارهای هوش مصنوعی فعلی.
رایگان با محدودیت های روزانه
این ابزار در رتبه دوم جدول رده‌بندی Image Arena قرار گرفته و از Nano Banana 2 گوگل پیشی گرفته است -
🔗
https://reve.art
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetell.npvt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/archivetell/5986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پخشش با شما
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=ZZOv9qZAsywqCU9gY4ApJ5855WYrb-i_gYjN1FZ64q5q-Ge8SWTfC9gduGj39IxLOcvt5_Kc-Wn0kmEAwu0XnjkcyzL3VH_t3alqv5c_pmoit063_-i6KzuTYSKLSShqot4WpU1_d7ryYxYBQGOIsxxqPrn0ua_WAaJrxK905vlb59Bsiv20Ky-offi1IhPF7f_o2-dHxxyLhnkOjD3muNC478YIFbNVZfbZ6qTTqWEJcqV09HNPLDVPRHv6Pgo88_CXBucnSso_Xzx1ZKXO-1Y8GKcTb4fIVDRT1cbTqz5wlERSuMMjyKwbent4itqgP7j9BEQSYytukcVU0HdqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=ZZOv9qZAsywqCU9gY4ApJ5855WYrb-i_gYjN1FZ64q5q-Ge8SWTfC9gduGj39IxLOcvt5_Kc-Wn0kmEAwu0XnjkcyzL3VH_t3alqv5c_pmoit063_-i6KzuTYSKLSShqot4WpU1_d7ryYxYBQGOIsxxqPrn0ua_WAaJrxK905vlb59Bsiv20Ky-offi1IhPF7f_o2-dHxxyLhnkOjD3muNC478YIFbNVZfbZ6qTTqWEJcqV09HNPLDVPRHv6Pgo88_CXBucnSso_Xzx1ZKXO-1Y8GKcTb4fIVDRT1cbTqz5wlERSuMMjyKwbent4itqgP7j9BEQSYytukcVU0HdqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
اجرای مستقیم بازی‌های کلاسیک و نوستالژیک در مرورگر
اگر به بازی‌های قدیمی کنسول‌هایی مثل سگا، پلی‌استیشن ۱، گیم‌بوی و NES علاقه دارید، وب‌سایت
gam.onl
یک آرشیو کامل و کاربردی برای شماست.
مزیت اصلی این سرویس این است که برای اجرای بازی‌ها نیازی به دانلود فایل، نصب شبیه‌ساز (Emulator) یا درگیری با تنظیمات پیچیده ندارید؛ همه‌چیز مستقیماً روی مرورگر شما پردازش و اجرا می‌شود.
📌
ویژگی‌های این وب‌سایت:
*
بدون نیاز به نصب:
اجرای سریع بازی‌ها در خود مرورگر.
*
آرشیو جامع:
پشتیبانی از کنسول‌های نوستالژیک و پرطرفدار قدیمی.
*
سازگاری بالا:
قابل اجرا روی مرورگرهای موبایل، تبلت و دسکتاپ.
*
کاربری ساده:
فقط کافیست وارد سایت شوید، کنسول مورد نظر را انتخاب کرده و بازی را شروع کنید.
🌐
لینک سایت:
https://gam.onl
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu3VtdRwhaQKCp3_AYRHo7dqKQqy-ppHHJUII_KCP2wxj2mKv4bT4yhPWewR_rvley4FJRyighf1Q0QbbpKuxyKnGPPrHg521Nbk3tgccToC-AxF-PhxWS_MzVMDJX5yt0OlHUVm0WoneUFOEY3XIkVeLh-GewEHwz6ROaTXLnzT9zWUjQvpF2eHRRMQVj-lvWlpwdGve4SDti0b_7auCs3yHh7SDd3B7xqst2kHnmfwvPaZBou4waCPeH_BNwTUB2ENtIcC8PjaooqgArVSeK9AeZpeQJn8fLOu9c7jcZ-jCDPBJMSKNu5h-SLFwS_xnpSX8ZZpLjy7GlsPPRopMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
در حالی که اکثر افراد به صورت دستی گیت‌هاب را زیر نظر دارند، Trendshift به طور خودکار پروژه‌هایی را که همین حالا در حال محبوب شدن هستند، شناسایی می‌کند.
1️⃣
رتبه‌بندی مخازن ترند در بازه‌های روزانه، هفتگی و ماهانه.
2️⃣
جریان انتشارها از توسعه‌دهندگان و سازندگان پروژه‌ها.
3️⃣
جستجوی هوشمند بر اساس حوزه‌های فناوری و دسته‌بندی‌ها.
4️⃣
فهرست‌های جداگانه بهترین عوامل هوش مصنوعی، دستیارهای کد و سایر راه‌حل‌های محبوب.
یک روش عالی برای دست داشتن بر نبض گیت‌هاب و از دست ندادن نسخه‌های واقعاً جالب.
https://trendshift.io/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معرفی ابزار AutoWorker؛ راه‌اندازی خودکار پروکسی روی کلادفلر
سلام دوستان
🌹
همان‌طور که می‌دانید، پیکربندی پروکسی‌های مبتنی بر کلادفلر ورکر (مانند پروژه‌های خانواده Nova) معمولاً نیازمند طی کردن مراحل مختلفی به صورت دستی است؛ مراحلی مثل ساخت فضاهای KV، جایگذاری کدها، پیدا کردن Proxy IP سالم و تنظیم پنل.
ابزار
AutoWorker
توسعه داده شده تا تمام این فرآیندها را ساده و کاملاً خودکار (Automated) کند.
📌
قابلیت‌های اصلی AutoWorker:
*
بدون نیاز به پیش‌نیاز:
برای اجرای این ابزار نیازی به نصب Node.js، پایتون یا محیط‌های برنامه‌نویسی ندارید.
*
روند کاملاً خودکار:
از ساخت ورکر تا اعمال تنظیمات پنل و دریافت آی‌پی تمیز، بدون نیاز به دخالت کاربر انجام می‌شود.
*
حفظ امنیت اکانت:
این ابزار پسورد شما را دریافت نمی‌کند، بلکه از طریق پروتکل OAuth 2.0 یک توکن دسترسی موقت برای اعمال تغییرات می‌گیرد.
*
پشتیبانی از پلتفرم‌ها:
فایل اجرایی مستقل برای ویندوز، لینوکس و مک در دسترس است.
🛠
نحوه استفاده:
۱. فایل برنامه را متناسب با سیستم‌عامل خود از گیت‌هاب دانلود کنید.
۲.
نکته بسیار مهم:
پیش از اجرای برنامه،
فیلترشکن خود را کاملاً خاموش کنید.
روشن بودن فیلترشکن در روند اسکن و دریافت Proxy IP اختلال ایجاد می‌کند.
۳. برنامه را اجرا کنید. مرورگر شما باز می‌شود تا ورود به اکانت کلادفلر را تایید کنید.
۴. پس از تایید، به ترمینال (محیط برنامه) برگردید و منتظر بمانید تا مراحل تکمیل شود. در نهایت، اطلاعات ورود به پنل و
لینک سابسکریپشن (Sub)
برای استفاده در کلاینت (مثل v2rayNG) به شما نمایش داده می‌شود.
📥
لینک دانلود فایل‌های اجرایی از گیت‌هاب رسمی پروژه:
[لینک صفحه Releases در گیت‌هاب AutoWorker]
https://github.com/marketnoobtrader/autoworker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN-Z1SRaS5671cIoFkx-vUx7ryhb1M18r73t6TEw6X6lFHxmDWmt2khCchx-sJQUVb6gL1T6jX9hb3sKrdU_F7QqBd7U5fVDznWiwgUYYztK3zjzynUrTiroBxntRODel3TCKsCo3gbgNW5IYqOacUggI3YTSksDiOOvDAFawc6jGFeXRm-It8pn-Rfv2We9CUnbrhu8LU0SznXFe-o0zIIG-7J7TgeczDwLqOXztptecdKyKQ3PSR37dMgX9EoU7KILDWnluJoG9P4UfgkV-SToYBuGD-s-2Pg2D5DXAm0rX02uTp2qg0hNkyC3fjPxgvWf7i1t53MgFX5OLKOTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
متن‌های هوش مصنوعی را کمتر کلیشه‌ای و طبیعی‌تر می‌کنیم — اپلیکیشن AI-Text-Humanizer نوشته‌های شبکه عصبی را به سبکی زنده‌تر و خواناتر تبدیل می‌کند.
🕤
افزودن انتقال‌ها و ارتباطات بین افکار، با حفظ معنا و ساختار.
🕤
جایگزینی کلمات ساده با کلمات تخصصی‌تر.
🕤
کمک به دور زدن شناسایی‌کننده‌ها و بررسی‌های هوش مصنوعی.
🕤
نصب با چند دستور ساده — بدون نیاز به برنامه‌ها و اشتراک‌های اضافی.
https://github.com/DadaNanjesha/AI-Text-Humanizer-App
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=Z-hIRRFfwKEKm325SNbvAzpwc0i6zRetsH5Ue6snjWAMT1yWldgIK29XywKtOC0c8tQwxWQ5QHcqxjJfSN2oCRStqtFqnczb7HicEuZhgeFk4soKwGlaMvAqcSUqI3MsfT_e5pF3uUPf3mV4ck1gTDtRmO31FTTSF7Tq2dY91mmaUgrBwIcC8pfsj74TBi0r2nIW9u49gRFcf1lkqaIOkSsPqqVl4kZBL7Q7Y5y2EmjorHNB8ctdDqFpUOgrtSktTRn76sV4O_eHH7xmpTOUWN6Lgr3lN6nN1XHN3FO5T5fcdTJSgdd6jzKk4pXuY9Gr-XDSa454qfxvzfeQSATdmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=Z-hIRRFfwKEKm325SNbvAzpwc0i6zRetsH5Ue6snjWAMT1yWldgIK29XywKtOC0c8tQwxWQ5QHcqxjJfSN2oCRStqtFqnczb7HicEuZhgeFk4soKwGlaMvAqcSUqI3MsfT_e5pF3uUPf3mV4ck1gTDtRmO31FTTSF7Tq2dY91mmaUgrBwIcC8pfsj74TBi0r2nIW9u49gRFcf1lkqaIOkSsPqqVl4kZBL7Q7Y5y2EmjorHNB8ctdDqFpUOgrtSktTRn76sV4O_eHH7xmpTOUWN6Lgr3lN6nN1XHN3FO5T5fcdTJSgdd6jzKk4pXuY9Gr-XDSa454qfxvzfeQSATdmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY4Yx9o_yNjkduBiMu_chTwJPE5tjhzTuJCA8Q3bt5F7dYCYkgLY82JWBYb5YnioB22xqJV_yHys9-U14J0tC7k6PIfRYf_LQ0HFq1zddOWJWWxmWJw9VcNcAXDmMn-Ozs1FrFC-Gpl4U1G5j_dZtdkfVKjir1gggrYgVfajbHEVEFex74Qfs2dU2I7B7sgpSygKuW2mxGCENAYT75TCNTwv2AiTN7-RjmQ96XZTzhe6uclC4oMEGEulKW1M2mLDm-QwonkCc3RPj24EokOQOE4lQZpywomaoZ7i6L-yHE5G_woLw0nqzWE1M3qPttWrJ8c16PgDZs8uw0XWQFZP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎬
🔥
ساخت ویدیو با هوش مصنوعی Seedance 2.0 رایگان شد!
مدل جدید Seedance 2.0 که توسط ByteDance توسعه داده شده، حالا از طریق Dreamina در دسترس قرار گرفته و امکانات جالبی برای تولید ویدیو ارائه می‌دهد.
🤖
✨
🚀
قابلیت‌ها:
🎥
تبدیل متن، عکس و ویدیو به کلیپ‌های 1080p
🖼
پشتیبانی همزمان از چندین تصویر، ویدیو و فایل صوتی
🎭
حفظ چهره و شخصیت در تمام صحنه‌ها
🎙
پشتیبانی از صدا، دوبله و لیپ‌سینک
🎬
انتقال استایل و افکت‌های سینمایی به ویدیوهای جدید
📱
مناسب برای ساخت محتوا، تبلیغات، انیمیشن و شبکه‌های اجتماعی
💡
فقط کافیست متن یا تصاویر مرجع را وارد کنید تا AI بقیه کار را انجام دهد.
🌐
لینک:
https://dreamina.capcut.com
@ArchiveTell
🍷
Bachelor</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=jRPgvwSzshiRDNpJCQWWfPU9bGjKbhFaogMI2s4Kid2P80u1YkLCQ4pAaGiHCrByN3Z3M7TbsSy7q4QwoKbSqhItQnHXyafOb-g7e4YQmVJBqcbIil1kxbCW8MaEhjBnQNhTctUhSFWu_tgjwHGv3NAzI8IUtQcjJoBP3AyyHxNf_XNeLNTDvl0SwAnr8KdasIJCy2FklmeX8jZBQmnFeI1qMYpnLYKfQu_aopzIWcRJJC9mMo-DPSoqG6qjqWmqPWHPUO9bY2y9OGnKi_bVMvuF4zNMYqSOwis_1BGcA1pXUW5F-DhpGlm3wMJa0rxePOlgA1R0YRL9wWe2FCSAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=jRPgvwSzshiRDNpJCQWWfPU9bGjKbhFaogMI2s4Kid2P80u1YkLCQ4pAaGiHCrByN3Z3M7TbsSy7q4QwoKbSqhItQnHXyafOb-g7e4YQmVJBqcbIil1kxbCW8MaEhjBnQNhTctUhSFWu_tgjwHGv3NAzI8IUtQcjJoBP3AyyHxNf_XNeLNTDvl0SwAnr8KdasIJCy2FklmeX8jZBQmnFeI1qMYpnLYKfQu_aopzIWcRJJC9mMo-DPSoqG6qjqWmqPWHPUO9bY2y9OGnKi_bVMvuF4zNMYqSOwis_1BGcA1pXUW5F-DhpGlm3wMJa0rxePOlgA1R0YRL9wWe2FCSAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔎
افزونه SwitchSearch — جابه‌جایی بین موتورهای جستجو با یک کلیک
اگر از محدود شدن به یک موتور جستجو خسته شده‌اید، SwitchSearch یک افزونه متن‌باز مرورگر است که امکان جستجوی سریع در چندین موتور مختلف را فراهم می‌کند.
✨
امکانات:
• پشتیبانی از Google، Brave، DuckDuckGo، Perplexity، ChatGPT، Wiby، Marginalia و Yandex
• امکان افزودن موتورهای جستجوی دلخواه
• جستجوی معکوس تصویر با Google و Yandex از طریق منوی راست‌کلیک
• باز کردن نتایج در تب جدید یا چند موتور به‌صورت هم‌زمان
• کاملاً متن‌باز و قابل شخصی‌سازی
🎯
مناسب برای:
• پژوهشگران و دانشجویان
• کاربران علاقه‌مند به حریم خصوصی
• افرادی که می‌خواهند از «حباب اطلاعاتی» موتورهای جستجو خارج شوند
• جستجو در منابع کمتر شناخته‌شده وب
https://github.com/thedmdim/switchsearch
#OpenSource
#SearchEngine
#BrowserExtension
#Privacy
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEEtnvVPKwsa7QnvoupTMrUEp0XP-3a9bXG1bCIfhBeyS_zVDbWADGGf90lNaywee6YU71L2WZo653pc61wMQ2FFlNkruoNYJHXYiofPlj7vwLAweP0q7yhhsGRart04mHlglVAt5N1xFlVZH8VDO2h-A67Yugf1GaLCD8VjH5-xLkBJWv1CSvxyOdTbF-8E-EtC04MnMJOU-HtjmkVCN4nl8WfdxeUyRJDSzjNIBvWjUtouykP9zuFIpPhg__rAvq1Amrn6edGShWQyER56F388eZJSHVemcTNqnZ-lUZLDvArcGmYcSC4_nJVIIxM5NiQCmjDcrDMg2S24WxVdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5967" target="_blank">📅 19:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5966" target="_blank">📅 18:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.  کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5965" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.
کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5964" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">vless://c2b6a323-19ec-4e4f-a95c-8b0e99aa7660@109.120.138.95:443?security=none&encryption=none&headerType=none&type=tcp#%40archivetell
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTRjYjU3NS0xNWJkLTQ2NjQtYjk0ZC0yZTZhNmI0Y2NkYTg%3D@109.120.138.95:28655#%40archivetell
عشقا تست بزنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5961" target="_blank">📅 18:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD_75rOM9B7VjDMops6sfYj-ivRSlFeQpZoV3XTxVLCzKF9TzSfy3h4RTb4dz5gAhI0635H_vc27SZSgM2iEaq5uByix4hF5VnKr2D_7_Tq-rZjkCElTRaY9Zi5WeaMBHZ-HnyWZgTsTCbKny6vR8-xCFjUlLe08ImxqZn1O4dLvCDkadat4TulYnk_uVpkbxDE3uhoyNYXU5Aoq1RWc48s8IjwfomcHlrWcjyvMNthx_iBoecQKxparkJpwmtpu6kUCCZjVcKM07ixcfTxHBvHhQFIXKo93jVVJCzfZ7O74wCTjHhhykVDfV9IhBG1E4vY_lTLiIHmxWoCnHiDOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اجرای شبکه‌های عصبی عظیم روی سخت‌افزار قدیمی — کتابخانه AirLLM اجازه می‌دهد مدل‌های سنگین حتی روی کارت‌های گرافیک با ۴ گیگابایت حافظه اجرا شوند.
🕤
به جای فشرده‌سازی ساده فایل‌ها، پارامترهای مدل را بهینه می‌کند و به طور چشمگیری نیازهای سخت‌افزاری را کاهش می‌دهد.
🕤
می‌تواند حتی در جایی که کارت گرافیک قدرتمندی وجود ندارد کار کند.
🕤
از بارگذاری مدل‌ها مستقیماً از Hugging Face پشتیبانی می‌کند.
🕤
سازگار با LLMهای محبوب: مدل‌های OCR، تولیدکننده‌های تصویر و سایر ابزارهای هوش مصنوعی.
https://github.com/lyogavin/airllm
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5960" target="_blank">📅 17:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0krO3OWaqzCQxUZENLnohAN1PbUmWcnU2Si0tzt60ZOd4_If3dUt_hiqWMWFV-nEBBuUln2BRy-gaGaAm5FyUELTQLGdIJf9veJwBijunGdciX-t-_YQWBhswjU7g_dPgK2ab9OHPMItrsyrruUNCExh0Emx3rIRg0UxOw-f_SojMet6l_eykOEt469fQAjPanxqPZ3BVy-sBb5n9_SZrr6xtTeF-YZ3rNcqkd0s9c4OY1kYE4jMmB9K2WhBOlSHqiL6Bm-M_GEOAFqUtzlsJCOIqmtVhTubOgq5lm208ZxzLQxj0phARbnx9DOay_dI8FkK2FojcntDPH_d6oNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujBhP8nZ6O8AXn2uB1GHxTVykBewpxIl9jCPbl_G-S5iLx0hQvOzsXRq1lGPF4QJ6RZei3bXDE-PqsXZk_XvElh5jd6-B0WBraAtqP9r_qnk_f4fs1Hmgr35l6Oqr0HH-TL4BZrc1M_g_yP6HECekS3V9HIb9uEUCS-0Fc4BXZ5Brfd-FL-7ad8DAWoKnI8V9LkYkYq0dsEcoW5j_VYcWiULYeBg9MjRLKKAsKpnhTHxOP-nnxOcQA5R0ykX4mIaspVXNH80RMs_GtGBXQsVKpBQa2gKeAzpqCMvy7gLiuB2Emg9GH1npQamRETIbF90urcBgHRVzRxBvNzt8Kjtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
WakeUpBroo — ساعت زنگ‌دار که شما را مجبور به بیدار شدن می‌کند
برنامه‌ای منتشر شده است بدون دکمه‌های «تعویق» و «خاموش کردن». برای قطع صدا باید کدی را از سایت وارد کنید — تا زمانی که به کامپیوتر برسید، خواب کاملاً از بین می‌رود.
چگونه کار می‌کند:
🔹
هیچ مصالحه‌ای وجود ندارد — فقط بلند می‌شوید و به سمت کامپیوتر می‌روید
🔹
کد برای قطع صدا در سایت تولید می‌شود — گوشی هوشمند کمکی نمی‌کند.
عالی برای کسانی که همیشه ساعت زنگ‌دار را عقب می‌اندازند.
لینک:
https://www.wakeupbroo.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=tmqJCHDHFbWCcl9OOlZvoBNu_d5_3lkorRQqmNBvW_2JlVA_kjFw55MkYOXBzu5FrfoQO1swV8b2MAo760IS_rz-8TZLBrq2zcM9XyVrrzfavTXjPUIxKADqiDjmamgfapop20D5gBmiGzz68XETYYGLCGTAnk1GbvT4PLBf8Df-Hm_RBY4VF9twDrAQlR_HuDbnO4G-G97mxhlQGMAoZ_YjNJR63rZMjCZrqrOMMGc4siF_ulU_MU75qDPYz72bG9zVPHgmApu-Ad8fh_EIkydaIujQI3uwkyqnve9-u9paY708-OVKbCdndoFuEj3Km3rRqbsmOKBwSZTn8a4JpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=tmqJCHDHFbWCcl9OOlZvoBNu_d5_3lkorRQqmNBvW_2JlVA_kjFw55MkYOXBzu5FrfoQO1swV8b2MAo760IS_rz-8TZLBrq2zcM9XyVrrzfavTXjPUIxKADqiDjmamgfapop20D5gBmiGzz68XETYYGLCGTAnk1GbvT4PLBf8Df-Hm_RBY4VF9twDrAQlR_HuDbnO4G-G97mxhlQGMAoZ_YjNJR63rZMjCZrqrOMMGc4siF_ulU_MU75qDPYz72bG9zVPHgmApu-Ad8fh_EIkydaIujQI3uwkyqnve9-u9paY708-OVKbCdndoFuEj3Km3rRqbsmOKBwSZTn8a4JpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کردمش یه ترا
تا جا داره بزنین</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCd-fg0CKvdxzlnTAXEkMJXNFQvvIHemtFQ29pD3GOjXhu6P1kwdHtaX3ZDUjgWG8EVoo9nd4qWN7U3Q0B7GU572EAFTscphwaoaO_JvotoJwcj_QjinB9SkbUrsdkrRvxI6nUCQRhlkuCgcZyacQfjfBQ6jhedY-2ZFC3_XQ7l0UA3WLWxNAj6FzPZKHVBu4gooV5wGp1FQc-WUhur_jHjzb8LYmWUB_yCVo4UzHrPO6WT71yVNSzVfd9u3_bYEwcsMWFK9JGBisEStj5HSpSdOFdcktA8zQY1-ZwWbw2erBb6SSNAoau-tUR7UNAf6VRMK52bCohqPIQrrbun5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪗
می‌توانید اسپاتیفای را فراموش کنید — پلیر موبایل رایگان Metrolist را پیدا کرده‌ایم که دسترسی به موسیقی را بدون اشتراک و بدون تبلیغات فراهم می‌کند.
Metrolist چه کارهایی انجام می‌دهد:
🕤
موسیقی و کلیپ‌ را با کیفیت خوب پخش می‌کند.
🕤
موسیقی و لیست‌های پخش را برای گوش دادن بدون اینترنت ذخیره می‌کند.
🕤
بدون نیاز به احراز هویت اجباری کار می‌کند.
🕤
متن آهنگ‌ها را مستقیماً داخل برنامه ترجمه می‌کند.
🕤
امکان گوش دادن به موسیقی همراه با دوستان را فراهم می‌کند.
https://metrolist.cc/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYNNvbKAWctCZ7CUoZOvPjQyINVK1zHGwwz12WhnYv8xMeuYHUMGqdeC4IbylqXrnW4pieCzyK_nKBnPy0EywVl4CuGgLNMKxAHbd8iPRaVAX1IMDOXDiT2S_3dLeRO9FagSzjFs5VxGzcjtvigU48khcaAGsnEGwwy3KmDQ8CvqgA3gEbTopUUTUPc6kVHyiVyoyAoZtbcvK3sC-BL2hPdtdTv6IBkjDeqXldgNAcNZxCAJqYvJv4nYS8w4q-O8D9rGATXP71mRT0UzX_CI26IM10nTChj_2dAcOLPLixA_Jtih5z28G_KHIFEmOmDZkiffRDX1h2wkPGJLsn0XpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJV91RN7RKS0eoUPjTs4W1ey9CNU6Fe-z_aJjRX2WVHDu2uZAfSaoXzrA_bYYGGtVHuH00GVsjjskpDPN1-_7E5y3h_ZQRfmrtdVwzw7SX2JrS3g7QQ4CKKhMuyMdDLIJk90LGRaA_XekmveWv0GuSmuVkQXHKwJ5aDEe4wjMtRvOw7pgnb0I3DS94BN8VVcNggRdJ4hcdygy-4LYy4EaD03pSa4q_cPq_2eHDst9UXbuJwaq6MXNIPgG2fynw321_9kdICq7_RfXdm4MW9xAlCdmR6yUkC-6ZnXUzrIjwuahTgHPBtDwiX_gmDM7tiXUmmqxQltn8dRWG47AXNlrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">GoFly VPN
سامانتل و آپتل
✅
(اول با vpn برید سرورها بیان بالا )
https://play.google.com/store/apps/details?id=com.ambrose.overwall
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5944" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5943" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeU47K69yATnOJQ9d8M43masUoKQDw5ybv_wuJf-oRR-tWZgFWTfHu8evNM0Yx7d9tJFs6L0oZcG1qZi55mWMZ4JV8WUOYyAJD9wWzah7qgV1NNIb7ZXoF67xy-aCENptnK4kH3YRUu44IiLdDTYkNUs9RMkb1d-_FBacUXLYLISucl-w3hMN9wKfYcq1i6BdBPUfpzg5ZzpzyYefvznF5QuP80ErI4FJHZo0HQcBUr9L1RId8IDo3nrDLdSH2nC_TS_UPbxzRQLB5wjwKL2erzWpil70nGdck7rx_ShLqDj4A1hWBIv4bsJ148sN_bP3yQSA0UxEQzfvTlwxOKxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cybear vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.bear.vpn.super.fast.unlimited.connect
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5942" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ3YzCqWPMnd61pyQC-kpfNl-sBh4BKEH9s8MC0z3vdNSor4_Qu2y0ilscKnaPbsaOMrYpFLEqPl_cJXLDhq9J8Zf8Y97w3vZqQa5PLzkbUX_mebCUI_C9VbITpRAmaP_OAN9YRnEcY9igl4nq3GAqX4jQJUkzOMqvLs5QatQcsn57MfMRtx2ZXm58bI1ow0NXMgMpkIpHBccC6DHvab_Vs4L7gVefyfYmd-1fJDJHRQLdOLQYGMea4kN5IQps9MrVfNSOyaJ6dPhGvC7Gaqmbtjla7HPMgyqbkUyDMb4RaFldvzTZCLPM4_tjYg8oIXJWrLvfsDSy5PB5MBFAfr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Soren vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.provpn.soren
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5941" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coH_HpkqmNTa5CVa4eqdofdjVMz3NhehB56ROcjBi6xsjNM6ZjVDpFMTi4XDvaJ3AVz1S_HdgYcTpxQeyyyEC_Guz7Ff6VhyLWY2L004pOlwILgfp9AEO8rN_E9Zkyt20QKs-qukwKX66t1Vd5LBGjtvs8mW_jdw9E_ZZia_u82TXr6IfXxwG_J50-oPeOPJa5P2-rHF_9U3wdhRcoOhh_Fnr6Xy0InkioncqlWZfUrONU5lF2S-0ZJvLaj-UYL9PIKp_uspsyFqYy5fDdLC9P1Umx_X9L_4BqOfOjS85iJkPQnWlryIPAszyGL3HoVsukG4aFztQSsmKR7TGrUb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥷
۱۳۸۷ تجزیه‌گر OSINT جمع‌آوری شده‌اند - یک کتابخانه جهانی برای تشخیص نشت، تجزیه و تحلیل شبکه و دستکاری داده‌ها.
🕤
شبکه‌های اجتماعی ، تلگرام و فراداده‌ ها.
🕤
جستجوی داخلی ابزارها.
🕤
به‌روزرسانی‌های مداوم.
🕤
دسترسی رایگان.
OSINT Tools
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5940" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">https://hjfisher.github.io/SNISPF-HJ-Configurator/
انتشار configurator مخصوص SNISPF-HJ
تمامی تنظیمات رو می تونید اعمال کنید بدون هیچ سختی و خروجی بگیرید و استفاده کنید توی برنامه
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5939" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🛡
معرفی SNISPF-HJ — نسخه پیشرفته‌تر SNISPF
🔗
لینک پروژه:
https://github.com/hjfisher/SNISPF-HJ
━━━━━━━━━━━━━━━━━━━━
⚡️
چه چیزی اضافه شده؟
━━━━━━━━━━━━━━━━━━━━
✅
پشتیبانی از چندین IP و چندین SNI به‌صورت همزمان
در نسخه اصلی فقط یه IP و یه SNI ثابت می‌شد تعریف کرد. اینجا می‌تونید لیست کامل بدید تا ابزار خودش بهترین ترکیب رو پیدا کنه.
✅
Health Check خودکار
هر ۳۰ ثانیه تمام ترکیب‌های (IP, SNI) تست می‌شن و اگه یه مسیر ضعیف یا مرده شد، اتوماتیک جایگزین می‌شه — بدون قطعی.
✅
انتخاب هوشمند مسیر (Weighted-Random)
به جای انتخاب تصادفی، ترکیب‌هایی که packet loss کمتری دارن شانس بیشتری برای انتخاب دارن.
✅
Graceful Rotation
وقتی یه مسیر ضعیف می‌شه، کانکشن‌های فعال قطع نمی‌شن — اول کارشون تموم می‌شه، بعد مسیر عوض می‌شه.
✅
همه قابلیت‌های نسخه اصلی حفظ شده
Fragment، Fake SNI، Combined، TTL Trick و Domain Checker همه دست‌نخورده‌ان.
━━━━━━━━━━━━━━━━━━━━
💻
نصب روی ویندوز
━━━━━━━━━━━━━━━━━━━━
۱. Python 3.8 یا بالاتر نصب کنید:
https://python.org/downloads
(تیک «Add Python to PATH» رو حتماً بزنید)
۲. در CMD یا PowerShell:
pip install git+https://github.com/hjfisher/SNISPF-HJ.git
۳. اجرا با کانفیگ پیش‌فرض:
snispf-hj --config config.json
یا برای دانلود کامل سورس:
git clone
https://github.com/hjfisher/SNISPF-HJ.git
cd SNISPF-HJ
pip install .
snispf-hj --info
━━━━━━━━━━━━━━━━━━━━
📌
نکته
بعد از اجرا، آدرس
127.0.0.1:40443
رو به عنوان پروکسی در v2ray، Xray یا هر کلاینت دیگه‌ای تنظیم کنید.
⭐️
اگه مفید بود، به پروژه ستاره بدید!
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5938" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5937" target="_blank">📅 08:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">100 گیگ مولتی لوکیشن
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=c4cb37f029af5828#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@crope.top:443?security=reality&encryption=none&pbk=Xgq8hNKvlfsBVHeJtXwjytbB5Fv2Tnu7vXJdZOgS8ig&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=crope.top&sid=b5af336756f77990#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@birch.gouher.one:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&host=stream.greenfield.lol&fp=random&type=xhttp&sni=birch.gouher.one&sid=28e92c6d545c9c26#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@meadow.pinevalley.top:443?security=reality&encryption=none&pbk=JfUgtIVRM26EKkksroAENXLWNJp9n28mSG-z-8CDAHc&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=meadow.pinevalley.top&sid=e86995a2ccab9364#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@rouze.click:443?mode=gun&security=reality&encryption=none&authority=rouze.click&pbk=PqunTCzbpHjmqH97ZpXHL0RBMyHaFzjJAO8i3uHr-XE&fp=chrome&type=grpc&serviceName=grpc&sni=rouze.click&sid=7fcb3d98608f93b6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@berry.riverpath.live:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&fp=qq&type=xhttp&sni=berry.riverpath.live&sid=bdf09e70262b409c#%F0%9F%87%A7%F0%9F%87%AABelgium
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@road.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=road.oakvalley.digital&sid=54aafe829679e92f#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@stone.quietgrove.forum:443?mode=gun&security=reality&encryption=none&authority=stone.quietgrove.forum&pbk=MchbHn3bpJaqAX-oqnNXYiXrbUTN0n-K203T8YGr8D4&fp=chrome&type=grpc&serviceName=grpc&sni=stone.quietgrove.forum&sid=0ae20b3e5e2c0bc2#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@flame.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=flame.quietgarden.live&sid=06d7e21ecb57367a#%F0%9F%87%A9%F0%9F%87%AAGermany
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@ember.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=ember.quietgarden.live&sid=fd488ee90cc0b9eb#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@valley.syrniki-iz-samokata.live:443?mode=gun&security=reality&encryption=none&pbk=euMfJzUx3qAGiaXwcvAXqXiqglBQKPOqxkTdSqwnqEw&fp=qq&type=grpc&serviceName=grpc&sni=valley.syrniki-iz-samokata.live&sid=c6046d150f597d04#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@field.wildgarden.digital:443?mode=gun&security=reality&encryption=none&pbk=dtxZ0lFLHE0IGfg45g2t1t7WwHWHuDW4xbfww3zKhDQ&fp=random&type=grpc&serviceName=grpc-bridge&sni=field.wildgarden.digital&sid=bbbbe9607d343bb6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@bridge.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=bridge.oakvalley.digital&sid=5278abf8d6d75483#%F0%9F%87%B9%F0%9F%87%B7Turkey
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@eveningwalk.sunnyside.city:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=eveningwalk.sunnyside.city&sid=54aafe829679e92f#%F0%9F%87%BA%F0%9F%87%B8USA</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5926" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@areal1.greewebservices.ir:2425?encryption=none&fp=chrome&pbk=xQnXh5EfPDhcEBB7rRiLca33GYrMEeUa35domLL_yA8&security=reality&sid=9b60d3&sni=yahoo.com&type=tcp#@ArchiveTell%20%F0%9F%87%A9%F0%9F%87%AA
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5921" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کدام مدل‌های هوش مصنوعی روی دستگاه شما قابل اجرا هستند؟
یک ابزار آنلاین که به کاربران کمک می‌کند بر اساس مدل GPU به سرعت بررسی کنند کدام مدل‌های هوش مصنوعی را می‌توانند به صورت محلی اجرا کنند.
https://www.canirun.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5920" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۲۰ گیگ
⚡️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5919" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5gwwrnaizOUWY7ao_aRwSGPrOW0Fj0sP5rib38-gxm1MfTu2X3Tdwoi79aTH3vAqntREFCsgL1f4MSw6c-kHWlNZnhCwxDFoncs6qNcw1pG2arRfu15jgu7YVNClUcyAMEOycSfaalITdxM5rNuw6IBpNTj3CfRMd39plJMlOW9zqPRV0YlsEq-61kC6YhV-YqOIXfSVZwnNclooE3KqYuQKgE2gixHMvu3raEaVUB7WWc_saW-icZ1pvJ7xETNwSTjERNOMCv2vhTWqFNyXYs2sBW9FTCAxJkzPAg7FzVnmuIMTl7vumjTSz09nta4dELwBXS60uE-pGV5INnGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚒️
۱۳۰ ابزار که جایگزین تمام نرم‌افزارهای اداری می‌شوند: آفیس، ورد و پاورپوینت. همه چیز مستقیماً در مرورگر کار می‌کند، بدون نیاز به نصب و محدودیت.
در مجموعه:
🕤
ویرایشگرهای تصاویر.
🕤
ابزارهایی برای PDF، ZIP، CSV، Excel و فرمت‌های دیگر.
🕤
تبدیل فایل‌ها بین ده‌ها پسوند.
🕤
فشرده‌سازی تصاویر.
🕤
فرمت‌بندی و پردازش کد.
🕤
کار با صدا و فایل‌های صوتی.
🕤
ضبط صفحه نمایش.
🕤
ابزارهای متنی.
🕤
برنامه‌ها و چت‌های هوش مصنوعی.
🕤
ابزارهای ریاضی، فنی و داده‌ای.
https://github.com/aghyad97/browserytools#-features
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5917" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">VideoNote: ابزار یادداشت‌برداری و قالب‌بندی محتوای ویدئویی
یک ابزار یادداشت‌برداری ویدئویی کاملاً محلی که می‌تواند محتوای ویدئو را خلاصه کرده و یادداشت‌ها را قالب‌بندی کند.
https://github.com/xiaokeaijqx/VideoNote
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5915" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5qbolnnOav9PiDTRfCbgsu46Vl0vLHVkIKpnIK7WvjiM9nlSmJ_nIuREdwPEXDfFMHtfV-dPvTT6gTuox5X9I-Rg2LN-mFrzzAmljLA0XieUq9NdV2ItWAvJxzlqTY6H3joJ48Hy-mRxqTwRYZYzUqhlhCHr0hQL6pudq8MX3Czvo9gzNFljU916yjn7AO4x-7BaWGOUOxuvTpG6UYC0PiLJdLAaeClTpFxMBp9AaL4IKmQKzpDScMcQoZjHhZJO09VtPm0i8dJPz90rD9S4phzdM561HlHG7uNqvqqS0-kkFlL2APu2UWmu9xC_fEUJgq-NjkDkVD_ouBd8jSrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOdRATfpnY1-5cXFUJgSaRTKCDdBW3U-izw5wZoQCSkAnWfIkNaSNqMAzyGQm-5lfw1Tcin6DNS9pcs_aHWmCtgqkre3zR5_ZpP94Tq0mznzIGsiHhAmKoONcdEa4Cg6FudStId1sEtCIYSnzE0kwuZWpfwP_SZxTfJjV25U-LDnpYHzuC0OIjswKlY2rm_qoDNePuIrMC7_V5aBdVTXb6g3sxJLXpj4T9NlbiGkDMfdo1qeM4JnZRJkMU9ztf5OFNYbYrHvoB98WKiZsGtcWJ81ixZkpAskhF2JCcYi1D7K6iIfDQcC9N4UlN80nJnVuQyKN_HuBQjwwbgUjgfkAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت عکس و ویدئو رایگان
https://www.mindvideo.ai/creative-studio/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5913" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://t.me/proxy?server=47.86.102.135&port=443&secret=dd887aa96cd9b760d42f62217afdcc6bc5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5912" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFRxqNpC-ffbcG27yNvGiap73Chb1IMCv9vI5ZJHtrkXrjHIYvdt65SQRVbimGiOVf-ypair_5jJ-jCpRBEfy6N2sDdj4NNNHgYBZXG7Hn_BoAlKSdPNclUfzlbJoiFk3gFgTljiNPncgtXNP5Im3e8d8DbFEUwLeQcfpvXZ2D3JnD_-IV4sc7g7XshnKX_HpNGJoQdrbPwE8wXsV5byfDrg7I3xDU7eNd78r5Ux0Fan9OKOi8d9h1lXoBLAktJ_1EewPtf9BWlmwaE-XXf-NbnN0a_h7BCw5_dLeuQSWnAaZE5Z5XZCF_NdN1q3e0JkPi_2Q9_tLop8LM9A1giLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ویندوز 11 را تا حداکثر توان ارتقا می‌دهیم
1️⃣
بهترین نسخه‌های ویندوز 11.
🕤
Flibustier 25H2
ایده‌آل برای استفاده روزمره.
🕤
Revision Group 25H2
حداکثر FPS ، مناسب گیم.
🕤
Ghost Spectre 25H2
فوق‌العاده سبک که حداکثر بهره را از سخت‌افزار می‌گیرد.
2️⃣
حذف زباله‌ها و قابلیت‌های اضافی.
🕤
Remove Windows AI
حذف هوش مصنوعی که منابع را مصرف می‌کند.
🕤
Win11 Debloat
حذف برنامه‌های پیش‌فرض.
🕤
Ultimate Tweaker
بیشتر از ۲۰۰ تغییر در یک ابزار کوچک.
🕤
Open Hardware Monitor
کنترل کامل بر سخت‌افزار
3️⃣
نرم‌افزاری که بدون آن ویندوز 11 دردسر است
🕤
WizTree
— بالاخره می‌بینیم فضای دیسک کجا می‌رود.
🕤
Revo Uninstaller
— برنامه‌ها را بدون باقی‌ماندن رد حذف می‌کند.
🕤
TaskExplorer
— مدیر وظیفه با قدرت بیشتر.
🕤
Explorer++
— مرورگری که واقعاً راحت است.
4️⃣
ظاهر و راحتی استفاده
🕤
Windhawk
—
مدهایی برای بازی ها
🕤
Jax Core
— پک‌های بصری و ویجت‌ها.
🕤
Seelen UI
— سفارشی‌سازی عمیق  رابط کاربری.
🕤
Cursor Mania
— هزاران نشانگر موس برای هر سلیقه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5911" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال: @ArchiveTell https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5910" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال:
@ArchiveTell
https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5909" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=26a4&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://104.167.199.23:2096/sub/ugqvbxg55h1u87rw
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5907" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch2LzJX7aaM9szZNXfDK3bZiQjFVPtbgJi-MQTJsj-R1nHSeUCpYl0pDrh68VQmUVW4TYbCnqEc4CC8fvQH-cG0aSPXbJ6So2SJHqw0yFsSKK0Ndx5gGyNyNc1s8fHDC7IZipHv561tW0Wugz0kNSQTW89VLHPrK-g0OcmAu_MmMsSKaAjvb5nOtRX9k8NACqMC-g9lsUwn4W7XXAkufImKF-MUZIyL6euoAlYjDh5JixOBklMLY5dAkQbJMMRP29I9Ypu0B3Q5vzxWL4Lc3hmwwZfQYXmwjBK3h4Ztca3AoqFMJFglvtkkaNfttwxPLQLu_QB2fS4tZj6nVqeQrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه ها قبلا ی چاره دیگری هم اندیشیده بودن پرایوسی سکسی</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5904" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">https://obito.96s.ir:2096/sub/cqx44nj2vnu1mebr
لینک ساب 50 گیگ ...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5903" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.  آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5902" target="_blank">📅 18:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW_DQiC_-VTnbOu47K1TctD37XSWFsmdIKMmLonveh6oaVukEySFul60UWMveLHIbDRIMRB3g2cgt2-WLEHwxuJWbPZcbzPpkGxjavxRO1vO739uuquEp8VGAjI4hf54MPaAssowCBNNFzlaBAjvBCIG02KkdzaKxvuAbF8pNURYaYUtbIWGk5-SVvs-k4n47YQu1mOE3jTCmY_pdz7kjMmgLkK481k7wucLYOOWGHLKHPcrIRaLBEJ3-aSSZWl56Gq_47agwLZiMo93X6CXVCKPNJmEvIcii3Dq6enrp9vkOSGzytLj0A7R4kFgP_senLhtbfth_Ab29iHqz50feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.
آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر برنامه‌های داخلی.
🕤
اکثر درایورها (فقط ضروری‌ترین آنها باقی مانده‌اند).
🕤
Microsoft Edge و Internet Explorer.
http://github.com/ntdevlabs/nano11
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5901" target="_blank">📅 18:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تولیدکننده ویدئوی تصویری هوش مصنوعی
ابزار آنلاین برای تبدیل تصاویر محصول، پرتره، پوستر و سایر تصاویر ثابت به ویدئوهای کوتاه، پشتیبانی از چندین جریان کاری و کنترل دوربین، مناسب برای صفحات محصول، تبلیغات و تولید محتوای شبکه‌های اجتماعی.
https://image-to-video-ai.best/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5900" target="_blank">📅 17:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">https://185.211.101.214:2096/sub/2f6ve5e7v0qim80w
سابلینک 50 گیگ ....
با نت های مختلف تست کنید...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5899" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S62jswY6HZrZgdcekEWQgwiK3C3WP6bGMLrY1wOcfxVhHkCkS84lRCp9Sz1UvOR4AjqkGpqsraFSD1sHdbJZ4W9OzJFzY1CyvOXRh65BBRSSmEI7i90dnlQpkH0v0gQNtkPhE72PEV2j0fBZKopC5gvatlbQrYF7ISgq-ljP8Po15EvILLfD4RQlsD5nsHmrmrCe2kSovlqmWWyx1OeVoS28Pcs4xUohHMvWxeba6_Fk5u7LI9YSLeXa7-S3neF86AzFPflZ0YQn4vrVvAsZmPxrAXBRWxwTbVi0qP_aM6U8HN_12dsa78lItTydkwsUo3ejUSuq2D0zr9GmIDzc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpkNCYOt5P_x8oeB15_suRudowT3XGKy7LxtUaDP6ZliCi_wUNrxuZGSInAtTo-CVuyYxSJ0xt8VkhQmSl7sCU6NvGvTHSAprAvvUGbAuGTpOcNgTeWQRAAfr8wfY_qpnTufzuwPHbmBq3cq5ScO_j1V86Ua91paV0wX98pMw8ERfLfMdSKfbDPwPTu_zeGHKQ971yjQsRZlm5BDigaw9cVckXcuk5Ldk3HtmPJDAGbYMeLoffi_ikOjeRfnV56sfqKnuiVuvvKcnnTlIxBawDyKqeZ9Bq_5m-MR5HVbAitZrzWkU_6ljF0uKlOuq-jqf1fCaTSakRVQf-kZaITRSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">https://khan.shompolexy.shop:2096/sub/tvhnms3g1zjuotay
سابلینک ۱۰۰ گیگ اینترنت
با همراه اول هم وصله..
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5897" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
