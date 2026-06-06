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
<img src="https://cdn4.telesco.pe/file/r6u_8RasiwYfhoNpalzUBkas70Ylq0DdGiW-m6Kybp1gl_q4efC3TTu133h89EPz5qjhrMliufREqzOTetOGxBWeyd0wJmaJqE-xYlItFzPql5y_Q0U6zSMtjvWK8_MRgIW1_FGLX9Fmwubf109pKXq_F_Rww2pdmF-VOxye76zFcBnRdgy_jxQCV1iNU3-G1GDS-DJ1A7LqMmG1Hx48U8UKKYgZQHWYTQBW7NWtg6-x_rHN7f0TNzpd6B8JtbwnC8PbpXKWy5UX2j_kFMznjyvPSDIIfHU8OXiGvn5VaWASCcaKF0LjSjl8Ct4qsujz6-dlSQQyPA-RhJQZ7YkGWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.3K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P21LAa-Zlv9mCGqBlPd52MVYjJoRsDxBOJamEUTcBNSgThPe0ZCXUy5M2X1-Fvm9lZgb6Mwp8L-qc638_HkbQIX6LG_3ylCVZGFFUN1Zkd4WBOUYH6P9kW2FT571xpZEwpo9mzCd0hCRjYxrhqRydwQWeam9uWyTR0H1wgmSpMlhp2LAv5BHqOquOhiDQpu4cku2z8hJjTG67_UnK5H1P3ioespnRhydV2hOIXVpapdMYUjPGjaJUizlGDN5xLa565DzOMJdkzc-57WbY08p7DUGnRU4BfKvQbypJXZiN5w1fYWe1hCpy42_5-g7YeXxehNi8a-afguUd2GswbzSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📄
✨
آپدیت جدید UPDF منتشر شد!
اگر زیاد با فایل‌های PDF سروکار دارید، نسخه جدید UPDF چند قابلیت جذاب مبتنی بر هوش مصنوعی دریافت کرده که می‌تواند حسابی در زمانتان صرفه‌جویی کند.
🚀
🆕
امکانات جدید:
🤖
AI Copilot
تبدیل، فشرده‌سازی، محافظت و مدیریت PDF فقط با نوشتن یک دستور ساده.
🔍
جستجوی معنایی هوشمند
فقط دنبال کلمات نمی‌گردد؛ مفهوم موردنظر شما را در اسناد پیدا می‌کند.
📑
AI Bookmark Agent
ساخت خودکار بوکمارک و فهرست برای فایل‌های PDF طولانی و چندصدصفحه‌ای.
✍️
AI Editor Toolkit
بازنویسی، خلاصه‌سازی، گسترش متن و اصلاح محتوا مستقیماً داخل PDF.
🎨
AI Creative Studio
ساخت استیکر، مهر، واترمارک و پس‌زمینه‌های اختصاصی با هوش مصنوعی.
📋
AI Page Management
شناسایی خودکار صفحات خالی، چرخیده یا دارای مشکل تنها با یک کلیک
⚡️
برنامه UPDF کم‌کم در حال تبدیل شدن از یک PDF Reader ساده به یک دستیار کامل مبتنی بر هوش مصنوعی برای مدیریت اسناد است.
updf.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 365 · <a href="https://t.me/archivetell/6082" target="_blank">📅 19:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=owRX6NX_aCCN9av0c63mMuZAsranlo-WVb3O75LgSDQcpw5COMx6gn4x_fVivt8iT5LTgrQ8ZIGzvHfkiPTPZKEdZIJ5-APqkCMlDR8_phJuSaUN6o-Sv548YBUuPGIM8SXYkx12XlxP9yus8WIItjfbB2kpCrmou3HeH3tztEhtd8kggVJiui2-WdJf6HiNVyLcWE-W5xOv6SQHD9DDdyIiOynRp_gLqpXFW8fRPgmPwZFqRO_cfS5aQ46bVKBNNm0b9RpEHzrWX7AnBH7aVjRzm0qmtqK0K5URhICa3juYNa1wJmYTkmmasR3S5nWiB7mtS-rA8iOOrdKTtossxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc7ad03ba.mp4?token=owRX6NX_aCCN9av0c63mMuZAsranlo-WVb3O75LgSDQcpw5COMx6gn4x_fVivt8iT5LTgrQ8ZIGzvHfkiPTPZKEdZIJ5-APqkCMlDR8_phJuSaUN6o-Sv548YBUuPGIM8SXYkx12XlxP9yus8WIItjfbB2kpCrmou3HeH3tztEhtd8kggVJiui2-WdJf6HiNVyLcWE-W5xOv6SQHD9DDdyIiOynRp_gLqpXFW8fRPgmPwZFqRO_cfS5aQ46bVKBNNm0b9RpEHzrWX7AnBH7aVjRzm0qmtqK0K5URhICa3juYNa1wJmYTkmmasR3S5nWiB7mtS-rA8iOOrdKTtossxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
🤖
گوگل یک مدل رایگان برای ساخت موسیقی منتشر کرد!
Magenta RealTime 2 (MRT2)
ابزاری جدید از گوگل است که می‌تواند کامپیوتر شما را به یک ساز موسیقی هوشمند تبدیل کند.
🎹
⚡️
✨
قابلیت‌ها:
🎼
پشتیبانی از ده‌ها سبک و ژانر موسیقی
🎹
اجرای زنده با پیانوی مجازی
⌨️
کنترل و تولید موسیقی با دستورات متنی
🖱️
واکنش به حرکات و تعاملات کاربر
🎷
شبیه‌سازی انواع سازها و صداها
⚡
تولید موسیقی در لحظه (Real-Time)
🎯
مناسب برای آهنگسازان، تولیدکنندگان محتوا، بازی‌سازها و هرکسی که می‌خواهد بدون دانش تخصصی موسیقی ایده‌هایش را به صدا تبدیل کند.
🔗
امتحان کنید:
https://magenta.withgoogle.com/mrt2
🎶
آینده ساخت موسیقی هر روز بیشتر به هوش مصنوعی گره می‌خورد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 787 · <a href="https://t.me/archivetell/6078" target="_blank">📅 18:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ6BuDykToP7CsALGd5D3hm0h-vS2NhRi1LCsYlAC_IIzQ6_dimslXAK_WmXDULrAjII4wg3SYQn54FMXu8iVg3qBgqxfIiJWrFSPlqYOVbO5oZVvFjAKSOjyUFCF6b5isr3MUJSWQtkNu5YMlK_UPI3CNIvgNPjOApbbmXbjS9zdR0o3yOaRbYVbQ0h6mvxollWzfDqAUxvrUcKcLumuzachdomhQe2HOjbEmZaxgIclE2NcZDZ_mdBHqGWvhtc2-FKmfFY9wVtiRQdtBjX-0FDGCfJdgEHSCpJPbnJ6oGHFX8LTithFiyZzgZXNxKFDZYPmbhjZVoGRPFsl2s0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی پلتفرمی توسط OpenAI با نمونه‌های کاربردی ChatGPT
🔥
در این پلتفرم حرفه‌ای‌ها از حوزه‌های مختلف تجربیات خود در کار با ChatGPT را به اشتراک می‌گذارند. آنها توضیح می‌دهند که چگونه شبکه‌های عصبی کارهایشان را ساده‌تر کرده‌اند و دقیقاً در چه زمینه‌هایی کمک کرده‌اند
⚡️
🔗
https://chatgptpro.substack.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/archivetell/6077" target="_blank">📅 18:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زمان : نامحدود
حجم : ۱۰۰ گیگ
متصل رو همه اپراتور ها
✅
vless://d601f422-a626-4533-a3d9-8fddf16517b5@171.22.136.84:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#100gb</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6076" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
80GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 80 / 80
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6075" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✨
اطلاعات عمومی
[5/23/26 3:48 AM] ᴍᴍᴅ: ثنایی یا صنایی یا سنایی
[5/23/26 3:49 AM] XrayUI Group:
ث</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6074" target="_blank">📅 14:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpJWnVBRzJ3d0RkaWJMV2R1VkZ6YmVY@45.95.233.55:443#%40MohrazServer%20-%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6073" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانفیگ مخصوص کلاینت happ
زمان : 40 روز
حجم : ۱ ترابات
لینک دانلود
Google play :
https://play.google.com/store/apps/details?id=com.happproxy
Github :
https://github.com/Happ-proxy/happ-android/releases/tag/3.22.1
happ://crypt4/vfb1onL0njkmd47DHXNPUKKEEPQNrpfahCf5vmgczvqBX6IcP0JkObKmWDw+hAZ2VwZ21pi6REi4WyyLXGQxIbppw+LrTNA2hI/+0Mv4HBgFZV3AEzeh1kgwD0yr9nppZJsSGofePhJLN2CcRV095i4udLU52HxgvaCcMSlW+MxM5BQyQycn0iznnAt+/d3fjhtJbMsGGPwC3VAK25ERXDg4IQVlPdk1K7QOfMqddVfnbPKHx6cYrLbYlh0jQS1ya2pgxEDHAHnKBapy6ldkGRojSL5NkZ0hDNhagnbvlB6EG+7WXfXLGBG4HTDv18z8kKwMcd8SqxlQs7xoZnsmUaMDLdiy7WLZ1feY8Z0upkOTj72B1Iwj1TIShiG1ZNyvKn9pPLCrNhntsChX3ckLrAMCI8U3iIRjoTgfW3WftxxTLfTN45xFAYGkektT1C1z/v1Bs+E5FZujJdzi/rCA+RoFpO8p7CvIbbCizV+dYY5deDml/Y0aBtTcy5J/Haukal2Wsx3Rrhcb8V1+L9FM6PfN0aKuZyzZ6cEZ2BCJTSEG4CAv0PSOwqQHts5lpfRLDdE6M5em9jkYuS5sdwxU2PULK4QDUn2a4LmkW5NMWQq/QOYuNTaiPsN1QqLKsTi0eXaGC9sJNHRLFOXahzwCgnKKr+ios8lIK98MoQ0KoUU=
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6072" target="_blank">📅 13:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqkVBbJH3Imr34mytmqVkbxtxeAr-Cf-tzX21bDHBG9TP2dvPpFUllffSv4V3WQD3Bzf6PPvydxPaLYJtaJLF6urleTgiGi-jmqBFdbjJUrZ99T9BL_WAa7aq9Dl0HQphFrPBKyw_dfYDJc9RpFbqD4x6MS-RxSVynjM-6O3oWnPmx_8YHqegdoPsF8A-tbOb9nJ-LQVuVIbMLbIoLiFIrG8k4RyKMrNMzjhDDVoUc-C9XEEgdJTPusGswNW7Xw4B0oeTLINR69Ku08UyTRcvzslPbEa-pU1GRVct_Mc0G_F5q5mJg0SBfH8jusJg-OAPAL6kt6yCcJa4YwOW5JyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب پریمیوم و بدون تبلیغات
https://morphe.software/
قابلیت ها :
اوپن سورس
دانلود با کیفیت دلخواه خودتان
امکان تماشای ویدئو در پس‌زمینه و با صفحه خاموش
امکان تنظیم دقیق پلیر به دلخواه خودتان
گیت هاب پروژه :
https://github.com/MorpheApp
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6071" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6070" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔥
آپدیت جدید NipoVPN منتشر شد!
‌ابزار NipoVPN یک ابزار متن‌باز برای عبور از محدودیت‌های اینترنتی است که با مخفی‌سازی ترافیک واقعی داخل درخواست‌های عادی HTTP، سعی می‌کند اتصال پایدارتری فراهم کند.
⚡️
🆕
مهم‌ترین تغییر نسخه v1.1.54:
🔹
اضافه شدن پشتیبانی از پروتکل SOCKS5
🔹
امکان انتخاب بین HTTP و SOCKS5 از سمت کلاینت
🔹
بدون نیاز به تغییر تنظیمات سرور
💻
پشتیبانی از:
• Android
• Windows
• Linux
• Termux
📥
دانلود:
https://github.com/MortezaBashsiz/nipovpn/releases/tag/v1.1.54
🎁
همچنین توسعه‌دهنده
چند کانفیگ رایگان
برای تست و استفاده منتشر کرده که بعد از آپدیت برنامه می‌توانید از آن‌ها استفاده کنید.
⚠️
قبل از استفاده حتماً برنامه را به آخرین نسخه بروزرسانی کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6069" target="_blank">📅 11:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBUUtCkkcijKrZHtqQE35TsbrylnjZzO6inpg_e423boH6JI3R682U_kbEpaxuoP0p89UdxjRBBimG_ucQODB8iXLWfD80AMSdgT3yQSFQsZsMHYYyVvSu-JoF9QrfGw2wfvU2xK5hRxf-xF8tiq0RyMDZ-1C1zieaY1rzJQjeyDgx7HRC3jonPoAfPZt7Cadn2aJHSpd1JUwXGANlRnmY6MvpTY-YpkLuFFGRWdlA5QxDyVvpBasBVTIcjpGFIkGIkKKMBppbANhkW2mAj08Xuc7dfi7WKyGxo47Pmj1lmdYAQ8DHGnpv55dXYnSHSwj0MDglPCY4I7z2ELFvU1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف سانسور مدل های محلی هوش مصنوعی مانند Qwen , Gemma , Llama و ... با یک فرمان ساده
https://github.com/p-e-w/heretic
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6068" target="_blank">📅 11:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=kBOZzUA5PlsLhKuKJlJQ1p3uxzAktxYj0u6RxC2u8KLMa9DFLWAWYn5yBqxtkCsC0rBQ5D00CAmucwh3texoXAbMsliJjJ4NuILMTspXWrSc0luu7Dh31mSW066MH-F2UmEJZ04Qf1rYEOu1cvuKN7jZV5g-o06woTSVTpi3WmaauIIGYRwwMa8D50eP4AoieOhdyF14tG1v-P3QKbUqRf5sX3eJJ9gU6aA8LAHPVyhSKl71k3m0l58U8yZkG7V_0oWqlsRuDx7jR7Vop35ofdouK1FqeyD8qR5IxDKysF34rttINdZPvNMC5BdyrucFfHuLATZhzBySQkSfJLXOfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602b4fbe6.mp4?token=kBOZzUA5PlsLhKuKJlJQ1p3uxzAktxYj0u6RxC2u8KLMa9DFLWAWYn5yBqxtkCsC0rBQ5D00CAmucwh3texoXAbMsliJjJ4NuILMTspXWrSc0luu7Dh31mSW066MH-F2UmEJZ04Qf1rYEOu1cvuKN7jZV5g-o06woTSVTpi3WmaauIIGYRwwMa8D50eP4AoieOhdyF14tG1v-P3QKbUqRf5sX3eJJ9gU6aA8LAHPVyhSKl71k3m0l58U8yZkG7V_0oWqlsRuDx7jR7Vop35ofdouK1FqeyD8qR5IxDKysF34rttINdZPvNMC5BdyrucFfHuLATZhzBySQkSfJLXOfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🤖
آیفونت را به کنترلر مدل‌های هوش مصنوعی تبدیل کن!
تیم LM Studio ابزار جدیدی منتشر کرده که به شما اجازه می‌دهد مدل‌های هوش مصنوعی اجراشده روی کامپیوتر را مستقیماً از طریق گوشی کنترل کنید.
⚡️
🛠
نحوه راه‌اندازی:
🖥
LM Studio را روی کامپیوتر اجرا کنید.
🔗
کامپیوتر و گوشی را با LM Link به هم متصل کنید.
📱
اپلیکیشن Locally را روی آیفون نصب کنید.
✅
با دنبال کردن مراحل داخل برنامه، آیفون را به LM Link اضافه کنید.
بعد از اتصال می‌توانید مدل‌های مختلف را مستقیماً از روی گوشی مدیریت و استفاده کنید:
🦙
Llama
💎
Gemma
🌊
DeepSeek
🔮
Qwen
🪨
Granite
🐬
Dolphin
🧠
Nous Hermes
و ده‌ها مدل دیگر برای برنامه‌نویسی، تولید محتوا، ترجمه، تحلیل و...
🔥
یعنی بدون نیاز به سرویس‌های ابری، مدل‌های محلی اجراشده روی کامپیوتر را از هرجای خانه با گوشی کنترل می‌کنید.
📖
اطلاعات بیشتر:
https://lmstudio.ai/blog/locally-lm-link
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6067" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
سایت های تولید رایگان ویدئو
⚡️
Dreamina
— تبدیل درخواست‌های متنی به تصاویر و ویدئوها. هر روز چند تولید رایگان ارائه می‌دهد و برای پروژه‌های تجاری مناسب است.
🔥
Pika
— یکی از دوستانه‌ترین تولیدکننده‌ها برای مبتدیان. حداقل تنظیمات، شروع سریع و محدودیت روزانه تولید رایگان.
🧠
Runway
— یک ابزار جامع برای کار با محتوا. ویدئو، تصویر، صدا تولید و ویرایش می‌کند.
🦾
Wan
—  می‌توان آن را به صورت محلی اجرا کرد. ویدئوهای با کیفیت می‌سازد و نیاز به سخت‌افزار قوی ندارد
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6066" target="_blank">📅 09:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: 184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 87 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6065" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foCPiuESDzy4vYEuHASeICS5sUKPLx42nTtsPZI-Kuv7Ewc3GlhznaEG1-PifvSZqAOavGTs4HX_QYsqiKJr-WR38R__lveuF6peUpvwMtdjYmwZD4BB60MNYF8yNdtaJ3R-y620sjAFiaQ56zyItT96GHA_gXJT41Up_VjZ4MVZ56mzYgIIvRGEr00BVXXcyVs9hsAScsUY3s6F3faJRzBA1VO8FVbLQ7ldvClLl-OYMXC7d4O14AVacsQ8FzTxMFhoG7X7dE4kzASe5UccY9mjMGDbEYzAbuxKEGvd1hY4reDEotZdp_qomO7LxT8j8vYUONMjPRjUzyk11whI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفر 91 روزه F Secure Vpn
🔑
ابتدا شما به یک ip سوئد
🇸🇪
نیاز دارید ( حالا هر vpn )
برای ایمیل هم میتونین از
@TempMail_org_bot
استفاده کنین
📩
وارد لینک زیر بشید و ثبت نام کنین
✌
link
حالا رو add subscription code بزنین و کد زیر رو وارد کنین :
BNAUH-EFCTO-EQOCZ-RXHES
و در آخر ایمیل رو تایید کنین و تمام
🤝
دانلود F secure vpn برای اندروید
🕹
دانلود F secure vpn برای ios
🌐
اگر اروری دریافت کردید حین ثبت کد مشکل از آی پی شماست دوباره امتحان کنین
❤️‍🔥
تا تموم نشده بزنین
🩵
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6064" target="_blank">📅 04:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
184
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 87 / 184
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6063" target="_blank">📅 03:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6061" target="_blank">📅 02:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پروکسی
🔥
https://t.me/proxy?server=channel.t.me.tradeip.store&port=8443&secret=dd7fe6d9803aafad7823ee9eecbf31886a
tg://proxy?server=channel.t.me.tradeip.store&port=443&secret=dd9c214385c44ee56c5f8d0a0f07475c3f
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6060" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی
وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان
GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen 3.6 • GLM 5.1
🎨
ساخت تصاویر حرفه‌ای و خلاقانه
از عکس‌های واقعی تا لوگو، بنر و طرح‌های هنری خیره‌کننده
🎙️
ویس چت هوشمند + تبدیل صدا به متن
صحبت کن، وگا می‌شنوه، می‌فهمه و پاسخ می‌ده
🔊
تبدیل متن به صدای طبیعی
ساخت پادکست و فایل صوتی با صدای مرد و زن
🌐
مترجم هوشمند چندزبانه
ترجمه دقیق متن و ویس به زبان‌های مختلف دنیا
📊
قیمت لحظه‌ای ارز دیجیتال، دلار و طلا
فقط کافیه بنویسی چی‌میخوای
مثال : «چک تتر»
👥
مناسب گروه‌های تلگرام
با قابلیت AI Agent برای تعامل هوشمند داخل گروه‌ها
🚀
همین حالا وگا رو امتحان کن:
🤖
@T_Vegabot
📢
VegaEnter
-
ArchiveTel</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6059" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLdqiUPOHqVOq0b_cLDMcZ0YXbYESaUq0aBkj4wcBZwIrriDBuIMBD3s3_1Xn87NGuqxjEumq5lO1A_14A4iTylolgw1g-im891G_VbQ5gpxLbJgBU00VI4WD1BC-33jeBWFR10Iv6SipRpjfMsBC7_8t_tXEJPXOHaxptcbYrWiGn0lD3FU7GMoMBmtRYE0jFfgoiAVYY6yNFqyjBiGxyJckPOWFYwBV2g8HEn5y6wuFQ7oNV4c-CPz9qDs_CwgGdT4BZgIqbdS4Q6lp-GEru1jtqVyroDZKVv08MqqhI6Guns4wziGKN-II4HbJjMCuFq7jU0sM0P6tpTYVskKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➡️
Atomic Chat
دانلود و اجرا کنندهٔ هوش‌مصنوعی در موبایل‌ها، بدون اینترنت، کاملا آفلاین
🔹
Android
🔹
iOS
❄️
atomic.chat
💬
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6058" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6057" target="_blank">📅 23:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی اپلیکیشن AzadiTunnel برای کاربران iOS (آیفون و آیپد)
خبر خوب برای کاربران اپل! اپلیکیشن
AzadiTunnel
منتشر شد.
این برنامه تمامی قابلیت‌های کلاینت محبوب «شیر و خورشید» اندروید را به آیفون می‌آورد و دقیقاً از همان هسته قدرتمند سایفون (شیر و خورشید) استفاده می‌کند.
🔹
ویژگی‌ها و امکانات:
✨
اتصال امن و سریع تنها با یک کلیک
📊
نمایش لحظه‌ای وضعیت اتصال، سرعت و ترافیک مصرفی
🛠
دارای بخش عیب‌یابی (Diagnostics) و تنظیمات پیشرفته انتقال (Transport)
🛡
کاملاً متن‌باز (Open-Source)، امن و مبتنی بر حریم خصوصی رابط کاربری بسیار ساده و تمیز
⚙️
آموزش و نکات استفاده:
تنظیمات این اپلیکیشن مشابه نسخه اندروید است. در حال حاضر بهترین تنظیماتی که خوب جواب می‌دهد، استفاده از پروتکل
CDN Fronting
است.
همچنین اگر IP و SNI خاصی در کانال‌ها پیدا کردید، می‌توانید به صورت دستی وارد کنید.
اگر کادرها را خالی بگذارید
، خود برنامه شروع به اسکن می‌کند (ممکن است در اتصال اول کمی طول بکشد، پس صبور باشید!).
📌
پیش‌نیاز:
قابل نصب روی iOS 15 به بالا
📥
لینک دانلود مستقیم از اپ استور:
🔗
🔍
(همچنین می‌توانید کلمه
AzadiTunnel
را در اپ‌استور سرچ کنید)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6056" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
800
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 75 / 800
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6055" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ZwzlUiHdEvfd7m5JFprCtubLyJbtQAO83eAy31FmFfDEHyMd_Zln5gc7crt1RRGplrnSKBg_B2Zu-KPHQgnLH2ykKm6__z2N100JIxx0WOHJ_Qnl8YzQtocF8ojrTfEDRdATEzAU-UwzhXGSSogNJWiueXc5Ulf8QzVBZvfGqrfPQhudWLcSTUFNimK5dg09kXS0SiSZb41rcnOmhgioUhYgyJIZU4qMcDh2VPRjjGblhtfGm4TYsqeLaklQniGJy83fMN5HPOn0NHrTY9vYCa24OyMiwCYL9ce3vw9iEYBTqbaapg4180Ua6yYjDP3mD8CkbUtnrLs0gR2V1dzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرشیو تل؛ مرجع محتوای ناب و کاربردی
🔥
گلچینی از بهترین مطالب که نباید از دست بدهید
❤️‍🔥
به همراه پخش کانفیگ رایگان
🎁
عضویت در کانال:
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6054" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0aAuOXMW1o5xgBW6C3BlBxigfEe9QW_ojF8NJ6uHDS7GT02HP_gTBUTTIfWxX22NAeUqUsKJXR8SWOje3iwxEuHKFOypIAowam_byyMWkAh6iSbcwzyEeKQzEgR145vUknbLAf90ipp4E29ptCmrkxeSLT1qhxWUndRa35sDEAmPP2J0S_8YUrpYJBRUtpQl6SyYIHtP0Tet0en-WwBD1Ma_F_YL68AaUAnLRF3A2hpNKl9ZvciFt0biMVQ6UdI07KknwBvg8OuDW-QRec2v0VnE99YuLswbVN4ytt4PybzBMl7wR37BTue4tI91nX0VYjLFbcfQpevQcyrBZYVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید ویدئوی هوش مصنوعی از متن یا تصویر با کیفیت 1080p با Seedance 2.0
با ثبت نام 10 تا credit میده
https://seedance2aivideo.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6052" target="_blank">📅 17:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6051" target="_blank">📅 16:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6050" target="_blank">📅 16:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6049">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sorrow of Sophia</div>
  <div class="tg-doc-extra">Draconian</div>
</div>
<a href="https://t.me/archivetell/6049" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6049" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orIq0VrzoJxpsVNp_aqf0HoOg_63LirPFH5--cSjY8GHu_P0whdHAP7JhKb8NxrGa6b_r0Tfj9yrzP7JQqCHvFNn8oD7XBuIFKj343gQlNOE6gj7-M_RR7fAATc0KW2Z0FtXci3c76ztUFj49_AIr_--JIYGRMHrj5I4cjyvkgo9JQifZwELs4byz8BgZFHk1h7-URLq-AvGZOJKa3dAN6A2_NjEu71HzfXhXm9BtqhqBGhKgtb8onpLA6gTmXdDG1_Y6gVg0afPotpqQF-0HTP01308HIh9pT55IYKl-ALrn8nAySwkapQDTyp_JeomDvRoJPyTTMYOuQva77wjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
⚡️
FileShare v1.3 منتشر شد!  اگر برای انتقال فایل بین گوشی، لپ‌تاپ یا کامپیوتر دنبال یک راهکار ساده و بدون دردسر هستید، FileShare می‌تواند گزینه جالبی باشد.
🚀
🆕
قابلیت جدید نسخه 1.3:
📱
اضافه شدن QR Code به پنل برنامه و صفحه وب
🔗
اتصال سریع دستگاه‌ها بدون…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6048" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNVE4Exfa5F4IoF-d1uq1FsoHxGEjsqVrU5PF8pgATRuznprKZV_eXIj9l_kqpGVipt7DwYQX0ZpxCg6k6ZDByE-PvWJ36aE8dY3bGhToBSAhQN3e7UbVwAPP-Bb7lSQco5TU0kiD-0tNrl1TG5K530Owl4wMLMnNQVNmBBskNt74XcIbPfYkfIJBA0QhvG35hPmqa8AoSWGo58muoayAmQGn6FT9CHSQvUFl5ruoHYKYltiw-Jo68s0Gibczoel3NxEIbkMROmolHKtxjYYRp9_nj1if2Eh79GZl6q0MzE6Joa9kRGp_sU4q2ksc0GSPux-7HaHfLR2rov7a80R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">FileShare.exe</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6047" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6046" target="_blank">📅 15:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6045" target="_blank">📅 15:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎬
دانلودر یوتیوب در تلگرام
دیگه نیازی به سایت‌های دانلود و تبلیغات آزاردهنده نیست!
😎
فقط لینک ویدیوی یوتیوب رو برای ربات بفرستید تا:
✨
ویدیو را مستقیم در تلگرام استریم کنید
🎵
فایل صوتی را با کیفیت اصلی دریافت کنید
📥
ویدیو را دانلود کنید
🗜
ویدیوهای حجیم را به‌صورت هوشمند فشرده کنید
❤️
بدون عضویت اجباری در چنلی
⚡️
سریع، ساده و کاملاً داخل تلگرام
🤖
Bot:
@youtubedownload12bot
👨‍💻
Dev:
@Bachedev
#Telegram
#YouTube
#Bot
#Downloader
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6044" target="_blank">📅 15:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
کمپین جدید
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 62 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6043" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همراه اول Happ
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 187 / 600
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6042" target="_blank">📅 13:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFxLqvsPtVf0dD_ItBO1OT42ZWaxiOGCdsnq96YjOfg1b_dMcWAX9cwKcQd_deUIT_5czlID5q9DKXPNfLrqU5NMvW_CYXt0M_JukufbPcidBGXPQENDVLfV2tR1BcYT3gcotkd8I-sNVXgsxEsNy_U1TqF6LJFZlbxSDK1Hc_8X_RmU2KNEH-ouuj9ROotST_lX4PCfElVJRWzI8a6N9t19rfwaDe27aYfyR2VVE7-ws6mVw_SZXza3RnzYe1aC9fIVYY1jgPj0gJ1twGlbkCwtn7y3p0hWdi6vJDnKvX8m8fF885_ag4pursKG6slUeQVZn9uZR4C4Imbkx9EUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ابزاری که مصرف توکن‌ها را بدون از دست دادن زمینه به طور قابل توجهی کاهش می‌دهد.
به جای اینکه فایل‌های عظیم، لاگ‌ها و تاریخچه چت‌ها را به مدل بدهیم، Headroom ابتدا آن‌ها را بهینه‌سازی می‌کند و سپس برای پردازش ارسال می‌کند.
این چه فایده‌ای دارد:
🕤
قبل از پردازش زمینه را فشرده می‌کند و مصرف توکن‌ها را ۶۰ تا ۹۵ درصد کاهش می‌دهد.
🕤
در صورت نیاز امکان بازیابی فوری داده‌های اصلی بدون از دست دادن جزئیات را فراهم می‌کند.
🕤
کمک می‌کند تا با پروژه‌های بزرگ و جلسات طولانی کار کنیم.
🕤
از Claude Code، Codex و Cursor پشتیبانی می‌کند.
https://github.com/chopratejas/headroom
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6041" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=R6ERikv1UVEkdLASwKEzvvQxYnr2vyMuLMgXoWWFbgwtF4ie5g-i_yQgZyCb_K0RmqD04DOSys87hKaIjl5pB5f844vALOmhyUWAeIEgvTlWk5s_Ns1aYughAOU7ysDlc0zNymXowFF8pJa6A_9XVIguzRb3-JdW_C1pYIhMYaWBFh1KXSQT_H-a7xVTIO0CERB7vFksMTJr0jeQZ07dUaN_ik7RPQqDdzYOErIvnoMAlXt9fmy-Asf0kARRfSnrwTLE9mS_5fyxqNINIhsMPJyXAS5_v2lbbTT0fXtHutsGi-tF9FvYW3NdHMVphStznTJWuwZDH-SCE5YC2Gzi5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=R6ERikv1UVEkdLASwKEzvvQxYnr2vyMuLMgXoWWFbgwtF4ie5g-i_yQgZyCb_K0RmqD04DOSys87hKaIjl5pB5f844vALOmhyUWAeIEgvTlWk5s_Ns1aYughAOU7ysDlc0zNymXowFF8pJa6A_9XVIguzRb3-JdW_C1pYIhMYaWBFh1KXSQT_H-a7xVTIO0CERB7vFksMTJr0jeQZ07dUaN_ik7RPQqDdzYOErIvnoMAlXt9fmy-Asf0kARRfSnrwTLE9mS_5fyxqNINIhsMPJyXAS5_v2lbbTT0fXtHutsGi-tF9FvYW3NdHMVphStznTJWuwZDH-SCE5YC2Gzi5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗂
ارسال فایل‌ها به هر کجا و به هر کسی — ابزاری که همه چیز را فوراً ارسال می‌کند.
می‌توانید سرویس‌های ابری را فراموش کنید:
🕤
پشتیبانی از هر نوع داده‌ای: اسناد، عکس، ویدئو، موسیقی، آرشیوها و پوشه‌های کامل.
🕤
نامحدود مطلق: هیچ محدودیتی در اندازه وجود ندارد، حتی ده‌ها ترابایت.
🕤
انتقال مستقیماً بین دستگاه‌ها انجام می‌شود، بدون سرورهای واسطه.
🕤
رمزگذاری در سمت فرستنده انجام می‌شود.
🕤
رایگان و بدون نیاز به ثبت‌نام اجباری.
https://github.com/tonyantony300/alt-sendme
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6040" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWue4ca6VSnvo-Tvh1UN-F8WT36cn-HabVw2OpzE6BwBNW7lz3u56NJCp2GYimlrVtMPdcQKI5KAC60RSbvg_bSMCIceZmzgUriV_qIeKAYQ2tT9TCS0opOMygXnqSI513PlN2G2mCj_SrT9t5PLKz3oc9EFrMfpae1FyTGEvD9gQxELtzSij3mib3BLUTWFq-kc3UJHOGPP-QcMlI3F-Cg4xgiU8rPexeKpU8LxvGzGgNKHX9Hde4_v78eqJIOKhk_gAzN0tnrfmM5jy1YUcxqq2lutwj2SNP3ZdpGOVz65WvN7OC3sADV3AEuMq_Fhy1XIggdnIrwM_Gze5iyeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان پس‌زمینه تصاویر با هوش مصنوعی
پشتیبانی از فرمت‌های مختلف، پردازش در مرورگر به صورت محلی، حفاظت ۱۰۰٪ از حریم خصوصی.
https://quickbgcut.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6039" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1pxx5Wybw5WN7L4ueRNr1wyUrvbstUYFTcexu-70Yf-QWj1X0Z2I8V7505cu8Bak_fihfiJnayJ8t92w7cBMfist6z8j0CtteORmLaXEPvhKtAiZQUAE6JSMpttcJRV0AGCuLbdtR2xF1Thbsuc-0ZkQP5aATDLXivMnrEv8vscwXvEGnIWQ1WaNej3Bw1bRTNniUCzHTRa28h4qkNAKv7GebMXfUiCKOd-sTlQPoEAUGpRGa4rWh8J9dCQpPrXqSFJb9PCBV8sUlJe9pl5WLSyn4CzRgp6q1iGA2Yl98Rifak83gGlDIQeQP1o97gLs8xIJ5knWE6YAnsoo_8csw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
✨
حجم پروژه Node.js رو با یک دستور کم کن!
اگر از Docker، Vercel یا Heroku استفاده می‌کنید، ابزار
untracked
می‌تواند فایل‌های غیرضروری را به‌صورت خودکار از خروجی پروژه حذف کند و حجم نهایی Deploy را کاهش دهد.
🚀
⚡
قابلیت‌ها:
🧹
حذف README، LICENSE، CHANGELOG و مستندات اضافی
🗺
حذف Source Mapها و فایل‌های توسعه
🧪
حذف فایل‌های تست، نمونه‌ها و پوشه‌های غیرضروری
🐳
ساخت خودکار فایل
.dockerignore
▲ پشتیبانی از
.vercelignore
🚀
سازگار با Docker، Vercel، Heroku و Yarn
💻
استفاده:
npx untracked
برای ساخت خودکار
.dockerignore
:
npx untracked > .dockerignore
🎯
مناسب برای توسعه‌دهندگانی که می‌خواهند حجم Imageها، Bundleها و زمان Deploy را تا حد امکان کاهش دهند.
🔗
GitHub:
https://github.com/Kikobeats/untracked
#GitHub
#NodeJS
#Docker
#Vercel
#DevOps
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6038" target="_blank">📅 13:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 291 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kih9D-B_bQAdzk_bQlJDxoyhSI2TY8KO3UWTghjcSpeQYwbfOy-fuJzRlg1GnGD5Y6Xdh9sr6r8okRqV1ePsRTaCFPRbYlmj1nJGYORdIvh0U4YBe_yQM3iMQe1jUOG4g2Kkue5Tv_elYwmmHK6VUorpUNO4iW3f2MoL9vpcr1qFa68oGRGA0FOJRqAm2JPNOyfkHxwBCXczvkrl78qaIbaC6-IX78GBkInsR7zZ37kaKiaCDYNX5eVvY_od40t7O5_4JWeAewu5qyPdOmp5Ng41YbnHscvkxfJ4yRRergn08g8MPiISRtKEubThtIDSRTNWsRit0jx-TSPKnf6Ucw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNJeW60jJKjxWJFxe3Y3iGFUOF25onZJ5xt2fqvzbYvqTF6Y01uvvB8MCbLEyi9yl7s0Wy9e3afNILEdAHpwYTecgF1LBxjh-Jj5IA7wn3pl25smIv8t8S5IaRLIjRn13xDnRo4CJ_PW7DN-StHCcpBgNa5x9qOLlzcWLrqSkd_oPlthOHXZUcrzR2nI8OWlXuVESXQhuW4VrnF-e49azl0yfFlcBKdUC-YLHqh97LIyQOD2APFD-hko2ZswJVWtqq7jsXFesiDQ6lFVHPeBA6sL0rBK0qqwTS77ndYACdm5ab0gG6kw_0F-5uMtAo2M-vlRfMgNhTcdJxR1zC2h1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6025" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6023" target="_blank">📅 20:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORXlnrfUqbyBLtfdjgDrdw6uA5T8depslkI67zzpH_rx_YYwq9dBzjBZo_bqtp_nb6-cKIF5adPV5JOcmMBRaa9g0bWgpOF1o95el3psegsV9FUUhtNiNTIp477v6GFjGYaCnu4jCgdA3HGpfZvmHvh9AIcuz_AvLxFje_6INsONKpJ7Rl-gi5IlBFKT6Jf7qOPKzWRMTpHk1eoXKiTl_GK1XqOYGHyqcf2KMpS0R7RVfXftn0yDni6HDXHUQbw5U5ZyYgCD5c1s57LBKrBkDejPpKvOFeTU4aZ3EEZzCfpdaW9EN5Da9gQoGHMAENKhRXxKHo1GFbRjYXMPyEXBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgbKCKiSsV_kxFQ_LBhiA9WBthpgv7GwX4_Esop_l-gr-nqt47SdKUOTpZc1CiXcHiwf4pwXBRynHVd1U_UEMSMaJmvJtTxy_teENgQiGCU67jccg3pV3swh7DYX4v9wUFt_t8vekNXXFJD5yZOlns25JVhmzgNnMWa_sWB_CzAwcCmWEoHYaPRgLQTxR7iMcOJB8QKqvYsRp94DzIhrUvx5Fd-3jR_mQYPigkaGXsaiVWlWfOPSp3DzlIXfebwzFYHSGwe7iQ5ZFZ6AR64XbwimO-tBj-DRTpwrCFkQHiDd5zf6BGTVx7d-Hk8j6bn0jaAEOBWDkaxGviORI1ps-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vs2SGfyj1Y_g_CcRehPsvQ3ttSaFn-54ohwxXXSVuLA2rgzyjHW6TsIJgrZwBqSz6-nbRrvRUNcfZxvMe2YboUcnOh2eojV82O9VJAkvqha0YnLv8yiLCQHEN__TFMBgWrDy7hxfF3sBx_QlZFMRBdCMCWjb1H_XAji03JE5ksTi6nzAs3edHJzRkT9gfnhycza3tMmXjDSSToH4Y6f0fp0kv5DUia5sWVyx43BIW0v5QRcJd2JcvFxMPZAK_6uPlmamf5me_p7mdoTBDlHzK6lCj-4MJAIWat0HQbdZCkW9UKw8gbRetvQHlvoKY1KkUmSjuzYvFdO1mP8cMKPjWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBVtYrAi39rhMZk0tY-kuM5sfpV3imh_53Azi1n9LDg2LYs8lGTmqxReXQIi6tjKXQZsbyt2LotiAX57Ia48_oGgaPM2h9E1lXg9bXDLnsVzSXIffqPm2qQNilvKbHc3sD3YlhZUKdyMqvW5YhoiiE910s9mGUc50via5gi2LjdG3j5JGK_ESxS7p8pmKZ3MMoX66_YBEK1zirlvBlw0lb1atNZezKd6_BQBiCvEohZrJz12MYrR5jSi2Y068NOQJ0f224pUTZgTt-d19NEEPeevm2WHcEY1grPteA36GQF4jb_dPJWmuilr4VG-eLSm0VHKeslCcI-Eu07Xb_czhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZEZHz5EmxSdXdH4rwlg_OOvlj0Dl17rX5wskMN3wqLDHifHEqZtXWBteRhn0Y9LybB5_Zi6pUoxIhfo2UJ5xNQHWugLCsLpPdGFAr7vNoQw_sigTab5ExmmkYCKKbPZuDhZCecEvcaG8gU0rxVu8TCMizyEMDtLv2ZE5i7rKzlLjehG_Ci9WmRWSBsqwa1zW5O-TcrDoRpUQfbWx7KEBPrMG0bDs16akvUJjtOJ0IKKPGl6EMlGiWwj5dOdinvHjDX7SxOwpNcliJGrmqPiLhTJc-8HlnMIAmG_GCUG55IolSaBEKnevnU1rzxOmDJ2zFnbgmux-IiTlN0qqUJiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5FEFj8eKbVs9KbfhQ0FPwhoW3pRZSJLTvJTZDfMIskQ8xvkK4rLCBZHnnlpcj5JPaHfkcgbmAOUd7ux6s8s4Z2_-nBz7vfX4v8KpcEvslfSLS64zNQZcM9Gxd4kAr1ds3dc7JY2y8zeH9S2sWQ4NqjvwS66yN9CzUedzVXvlTecNJOieOpaQkoYq1XHV0vXZ7-cR9rWa3ErGldJ5sF8Gz9dccWuu0cvwyNTXWoxgSJTTHQdu91uQLUSL-NgQtm0WL2_IxxkqutPjAtGugh6Ob4BvjNXRo0_tsadp_vhVBWuGrLgoJ3ACBf4cmbvoDOQRVOAEIC4kD4doWZclZnmAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=eJ0TqwmMVwqCJBizKCJDfEdzafUIdJc2I4EiLr95job_3m8J20bAVS3RmKcdHySUe8BMLAgpbOHXP7nfCNAumyA_xvgZskm-RgqJeKcctbf8rPBnjYgFSt-YCGc73uIEK8DyCMAxVSbW6PXvoOX1QdRR8say84653hkGUfeQmPsGqrO3lGQeO9FYNKdZfFrvm2g8gpYAgtXEsfbG8c0joKCvSuZyvxVQKfxZgXKJmV3qR8LqQPip1Rl_05RY0Ku85BnXAqqvNrMvsHBZb5trkc3VEkpCWa5-DKwQ7cNi1Tvezx1vvOPBmWTWVLw9grkAOx6TSqi4c5qKwr9ZHplO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=eJ0TqwmMVwqCJBizKCJDfEdzafUIdJc2I4EiLr95job_3m8J20bAVS3RmKcdHySUe8BMLAgpbOHXP7nfCNAumyA_xvgZskm-RgqJeKcctbf8rPBnjYgFSt-YCGc73uIEK8DyCMAxVSbW6PXvoOX1QdRR8say84653hkGUfeQmPsGqrO3lGQeO9FYNKdZfFrvm2g8gpYAgtXEsfbG8c0joKCvSuZyvxVQKfxZgXKJmV3qR8LqQPip1Rl_05RY0Ku85BnXAqqvNrMvsHBZb5trkc3VEkpCWa5-DKwQ7cNi1Tvezx1vvOPBmWTWVLw9grkAOx6TSqi4c5qKwr9ZHplO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay0vZm8s1QUraVIhkXagRlRc-Rpb6y4dgHKQkUiJRBpZBbDQp4iuzM26WfoUda0vV1aOKRZMyQHEH_UInNZwJ2v7RMimjMgHVWmeBXRukViw0dSXp6PlBC97GKkObGkqktOtJtQ2XMzAPfN7vHiGuAQHsl1WTKaBjaurAOzQqCU08q-kIiJZt7mbDG5gqkTzy89kAyTyo0o5bJHR5ONQP2rpoWtrS4zpsvF93gZdOBGtM_psX4f03H6kluAi3hnCs6gfc9C26p_uAF_yYP0bAaGNCZjuH0wHkXkDkEw7sZ0T746sn-pdo54fJ9yCjjPgk6_kDwu_sV7HnOmp3As-cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC5OG47w9KeXD0lDkBFUKD0ZFGYJHJEw_JJDQyEaI4Cv_Cm4cp0bKGvBuj2BRbx1dxskeDVL0fsUZreOdUhCTnLU4qNBieVfKBlTfpyw9WIstoylJ17vL4nIVrOudfwYHPfPVsDQM4ycL1d95oRdWsMq-UkAwmuRn-eNsKwLuJOXXK82o83EbM1p9ETSpS_9rkLPYoYmiAEz_c1SB2ewsxmvZ5NVzTv7kwSUavXalg78DnBRdVMJSIO2aM1mfZs57WLkL0n1FA1BI2F2BGB_Gy-X1SQwcytEW-4uiwNyONvyIcSAReOawEieVjFReof96BomoJBTHj4NDRHof7FjKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=MjmJ8BQVsmGHOFXwe9y0ZxkP-XbhiEooRtptZJRFwZ4Mop0V0m88AYHSpb3ubQSLyQbPvvmR8kmciEXhsYy-igN5M1baE0NnWXbmaKZ_MQmA_UVjUBLPowIDrlVdOXlu-rZjjlYCq0HkOLbgWKuNRDR0phfyO3z4UYsNughEb8TFuDGNV58iYKOWz2YAdgqSUuP3urOTGBO1v09IopUdV79O1FBrz2aXd5ITVj8RDgTgl-l_YxuPvsikq9DiWyt8FXNWSX8__6wwZIjBLj5rv-2PFTmkhNR0utuKQSBT1h_wZNNzr0SI5Q_9x0XEaXicxo3n8TiCrRTC58jxI4aKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=MjmJ8BQVsmGHOFXwe9y0ZxkP-XbhiEooRtptZJRFwZ4Mop0V0m88AYHSpb3ubQSLyQbPvvmR8kmciEXhsYy-igN5M1baE0NnWXbmaKZ_MQmA_UVjUBLPowIDrlVdOXlu-rZjjlYCq0HkOLbgWKuNRDR0phfyO3z4UYsNughEb8TFuDGNV58iYKOWz2YAdgqSUuP3urOTGBO1v09IopUdV79O1FBrz2aXd5ITVj8RDgTgl-l_YxuPvsikq9DiWyt8FXNWSX8__6wwZIjBLj5rv-2PFTmkhNR0utuKQSBT1h_wZNNzr0SI5Q_9x0XEaXicxo3n8TiCrRTC58jxI4aKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMHEecwVscwhF6NyQMZnG4BW9gpUwdSjEB-qIuNGnd3rttH6__JxTwleRhr4nWdBk5ql4m24AGyDpjT0XRai71tuXeFwRQtQuzaHWPRM9XL-p6lIADIDOfWYsLEhTmFmM3-Vpuo1gpaKQcSSvskbEEL_iduTuMZ_zceqogftaDYpnjxLChUPYZAm2m94K5jZVDufpxn7AxhI1JgQxe2uTFVE4mBBXDWwjk0v9KHjZRa4ntBCj2d1WsxIVP11qE77zc-acrAimEk55yDPEVT8O5nynlYNGY6hEjGkc0LSc_VsT_t9JNPPzu0MfKKdxcXlbQ_WAAIwAv69ioEJg1Ikew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=LjF2gQ46cue2uIXe1LFIMaFFvMahF-cZ41mDOcaDbMcsSqfsWIPSzONuzK-JFndBOlMVhMuAzDn6cHpSmsN2ioLwDHD5ws5CywkE7Tn4U6QMdRErvCquFptT_VwAI3-M781a9UZz7kJ-GACpEYRQaWmyrhd5EBFtqavNOTEElZrxUFr8-QUxXp07jxSchYwPmc4fmcqHsjJheh0cXVtjsfqQ9-W4fw9lM4FAXIACT6O7y7wnPqlh__9F9sJa08vQ5ak8Tb4e1p4o5giSxTqoqleleegBciRuCAOaUXkaYEGYKrCI-5KKO3RBcFskULi3ykIpyly6mrUTJ9xjrmVuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=LjF2gQ46cue2uIXe1LFIMaFFvMahF-cZ41mDOcaDbMcsSqfsWIPSzONuzK-JFndBOlMVhMuAzDn6cHpSmsN2ioLwDHD5ws5CywkE7Tn4U6QMdRErvCquFptT_VwAI3-M781a9UZz7kJ-GACpEYRQaWmyrhd5EBFtqavNOTEElZrxUFr8-QUxXp07jxSchYwPmc4fmcqHsjJheh0cXVtjsfqQ9-W4fw9lM4FAXIACT6O7y7wnPqlh__9F9sJa08vQ5ak8Tb4e1p4o5giSxTqoqleleegBciRuCAOaUXkaYEGYKrCI-5KKO3RBcFskULi3ykIpyly6mrUTJ9xjrmVuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idg8WUX39p2kkNtBpuK1pWmkheD8wTrq3muOklycWiVEu56FtfrkvNHxImEfnXx6OI_ErBE--kq3JAnD-M5iNKsrlmQHhXhEeTDV3QSHlNQWBBO38kKMzo4X4BtFGFh0sOI2fG9T6yMcPFRoZhglOpzlUsuJneUuubt__OED0aJEODUR4YJXhbyPmfPfbDGrWrKL-457LB5YRzAGmdYn5RZF5NBTwimNWDBy2jAk42j_P7btQkpj4IsFXRVXjkK1YnpI1iY95ixS0EJgzmALT70vwvee9CAB1V3Zw-PUoHmbv4GNIausB25pjjIdpH8p89gL7iXhN7es-v5L7Q7zhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5967" target="_blank">📅 19:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5966" target="_blank">📅 18:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.  کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5965" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.
کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5964" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">vless://c2b6a323-19ec-4e4f-a95c-8b0e99aa7660@109.120.138.95:443?security=none&encryption=none&headerType=none&type=tcp#%40archivetell
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTRjYjU3NS0xNWJkLTQ2NjQtYjk0ZC0yZTZhNmI0Y2NkYTg%3D@109.120.138.95:28655#%40archivetell
عشقا تست بزنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5961" target="_blank">📅 18:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2DcKVLsrCOun7_NhyVbopD8qp-o_N_DV0g2pXBNi8ijOVX529FHoyQRET4EqTpn7yZ1lYA85aL2xkKSN0IEZa2KDGsw09ny5tenak5SKMrN1bG324E4M9y69l5rtIHb4XwYDqbXtnprZFIPJR8--NsOdMf7UimnsV7ofsFzzC0vPOb67RVzl2WPZmGJGE8Cu7i6XDy9hF-XFpRuxmkx4DYO28eX5bYTeowEn7HitEM1kc92rXIE5OC-lo_m6zBVe4s_f6bJCEnqIwsIZz-h-26FODSd32BjEuAeU1N4lsYlt_viiryiV4PhfmTZbxutZd6DzwtHDG_mWmiPfjlsiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5960" target="_blank">📅 17:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNewXwslrE85xFWC0xfgDBxygluhO4HDwN3cRTlRwnjK6Qpe79La4R_NzVollWUeuLagRer82cyg5dAC-xttSaR5SwbzLM-B4jSAbKcjNbkistRPiWk-m9wscFdyM7sgMZq8gvDPX1YPr3nDSXirHNrHdFh0Cfe_y7SDsa417WSnDdOQPXLzAtA-6MV5ILgLvfuPTCWbTMQUt3u7F-hVLS78mlyTpPsrYrU1Ye_pA9oFHZyJDS5NpLtplxmicYzvsloZ4DL-yBKFGVhfazK7vzO62neoEchlLoV0Ox2wNzbKw6KmQZn06avM28gNwZf6K_8gvyNcZEGu2cRku-sYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_rzrHxgpUQjPp8255KyJNtkOHkLhK_LdxwpxGiKJGE5fyqi1rj07KibgaRYdULHdBOJR-QNmS6ydVLZyKsPtnDYrZAp8tyswa8a0aRAIVnaoMRbS5hIkkZfEqN0nD7xtgupeSHfypvRt-gzxaKqNRIpJvj-7NIK4WyrK3AOaxMfjutSYb-lUOHJwvmVKV--xwnmfk8f2ckd_L2GkLTVb_-ha9nld937QMCrmG89H-tg1WSI9LMxqFeII2AVKBmjDencWMPBVZZrtNra6Hu1BDWemtqGNtM3VI_89vAKHgJx2NG2EqF6zeovJKi5sjL8qVITMHTa_qTYpdVjRmfsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=O45ZZXRPDZQk6SFFz8wmndtqvqbTygZ50OhySIcz37ri7kovxhlvkXrbsGROlPSPtomXXV1RIgR6o1sr-UY5sSBUExcU_5rxCRQ5g1wInB50qiNMThqWnpRVSOgkqFHpQcxY_gXqLSto_nSuVj3hRwpgbC-J56mHCeq1EKzoXVSMtG01aO8CVaqpJfzAzAi13HmVBZvzYAVFxbELbQf5TWAb1gZPIXVyuO11hzDEL_UVm3g6J8Or_bu0htKKx8NoQ6QCvYpEbQsOvPT_PRDmrLX8x-9cSgbA6D_uaozybqSqLyNojcRKer1AkiJ9IinsFESL0EY4eXP44r_XekjWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=O45ZZXRPDZQk6SFFz8wmndtqvqbTygZ50OhySIcz37ri7kovxhlvkXrbsGROlPSPtomXXV1RIgR6o1sr-UY5sSBUExcU_5rxCRQ5g1wInB50qiNMThqWnpRVSOgkqFHpQcxY_gXqLSto_nSuVj3hRwpgbC-J56mHCeq1EKzoXVSMtG01aO8CVaqpJfzAzAi13HmVBZvzYAVFxbELbQf5TWAb1gZPIXVyuO11hzDEL_UVm3g6J8Or_bu0htKKx8NoQ6QCvYpEbQsOvPT_PRDmrLX8x-9cSgbA6D_uaozybqSqLyNojcRKer1AkiJ9IinsFESL0EY4eXP44r_XekjWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=vPxEOjqReuvqr3SzzdUPfXQ0XlBcVkI7PbkNl0PuLWrLNJKEZY2SxmpUF-yZ9pCjkzftrdHG7lNJxkJc-AOoxE5cmyfRXX_rGYtKMrcj-USV79iN4YcvRRqHXNdrCI0OnmZ7ZQeVqcAiph4NhQZJo_XuAAVl8yR5rC-ZYw-70qxHtiZexZfZSvnwLsYYi8ruur45BROilNsmtXAppJRLEytKhDZSnSRz2OY_OoB6n0GZAy8YHYGYN3yp8qdBNDhC5Pcre_KBp2NwgeZNGfZVdU4aIFZ6Z93pWOFm5bDcVvD-KYYhwz1QQ9MUjwk6Htyu3O1c1c_pmRPLx0p3ueMoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=vPxEOjqReuvqr3SzzdUPfXQ0XlBcVkI7PbkNl0PuLWrLNJKEZY2SxmpUF-yZ9pCjkzftrdHG7lNJxkJc-AOoxE5cmyfRXX_rGYtKMrcj-USV79iN4YcvRRqHXNdrCI0OnmZ7ZQeVqcAiph4NhQZJo_XuAAVl8yR5rC-ZYw-70qxHtiZexZfZSvnwLsYYi8ruur45BROilNsmtXAppJRLEytKhDZSnSRz2OY_OoB6n0GZAy8YHYGYN3yp8qdBNDhC5Pcre_KBp2NwgeZNGfZVdU4aIFZ6Z93pWOFm5bDcVvD-KYYhwz1QQ9MUjwk6Htyu3O1c1c_pmRPLx0p3ueMoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کردمش یه ترا
تا جا داره بزنین</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNEb2wvPCv1KkDhK1zUMjbzhWh8JkfXxFCuZoMXIbK2-SmIVDJXffejFrd1cc0GkhEb8K0GD4GUcMwOcdJzFfFFWNJf4mcn-62N_c6BQbCIKUxAMyiUGs5FKkVYr80KB5Vny_3pQR6-RemEcHkKI70KQ-mnZWy7cZDIo7DJsPkzQom5xhI_oZ4DksC2C62ZWD99MQ5e3y1-fuMadupZDpbUAjXFeq1vzgfzxo6KW7TUTSXsNhos4FIGE5Inbe6u-lihwqLHmhDIOiCzLVP4VWgH2uWekjTJ6Y8SZfNi5NqyQE_sqj0tRBZnFuCyw_3RbsuU-y9XyMSDKX3DN7EZoNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqDPxQlUXeqRnvBK8mOg1EGR-u0asrgAfof3OPYITigovfy_f7OpKnmEfrk0ZwFwmt-o1eJ8UZ290OHYKxVLyJsmHpeMAeF8XeSVNLv0hLIiNIfswchll1xiEBUhbtH92IN93A8StgR09TVsRXnXOmyN9IP3WHe7HvGeTX4HeEVsWYdeZvXUuHLlxGLYwd1HAUiT7F9g-__PZUJtwcLQMRerHk3J3GJ2MAY--ujVn2UHaMAUcaWJwA0X9LtKO8SRVDmvp3e_lBscvEvvpJaRIn2bbzoJJ7C6hoTxCJ3X4qLtpnc7A9LmksAuq_0ZMVQS2I3IVdSLFbYnbPmOkBgY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjySge1g0KLolyKZ_1T_e_XjDz9ywEtnR-Sqk7lsl32p-RXC4yx9-8PzlHxJPQ2MPjzIVXto46SM_k_VDyoU2Fw5FWUt7LNUx6DqR4ENaxzMN8SqkL7Z8gLVAQw4e749_1Mxk_C6fIpkt5QMbMWEwd-Wumv4gelJXbDfSfiqrQ25_yX6mDhEmF98NapzSNP804aWx5KWo2o8VjVS0-H-L0snzPTeFq2HQ6x98Gz4sadLqV9dnbPc5JF2h1ljgOB1C_1DrUI5xT2gUsAJAGRbBP2LCQsDza1F9cMpKs__-c70NT9Sw5Ejeyazyp6WtsXHOyDnEfWesKn5TUEKlbVlvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
