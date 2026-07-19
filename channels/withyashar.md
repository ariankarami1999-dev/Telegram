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
<img src="https://cdn4.telesco.pe/file/RVZYYWzaUqyi82X1EOAybPjls-dKsXvtMnCEMhggy13j9qS7bVEE8TvubgnSF_Y0eKlxGar7kOgXMHjOreL1uPRB8JdEjgu9DgGXLsw-MoPvTJiDdnPhL6MmRCsj8GxNKyVj6vYgXapDjumHZ-uMD3ZEaXNU5dNPXJ9SXF-VxsPLYWYxFO3CDubf79vtWaxxDuHDOrF_qxEqA9UYgPYcLuPertbA0Jc1fAKVRhOE6EEt2h1t_zqaVePMPIJrJOIMsI6vB0-JaEi2BmYvdzlHeO-xz8xko6SuSCo7pQsReNkte2KcSXANCsI_BgT2SulYw1ox2pPrVNY25_TU6aNsfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 413K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 02:54:57</div>
<hr>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کویت زیر حملات
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/18955" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پهپادهای موتور گازی در آسمان شهر سلیمانیه در شمال عراق.
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/18954" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدافند شاهین شهر اصفهان درگیر شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/18953" target="_blank">📅 01:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الان بی بی میاد به جای مسی‌گل میزنه
😂
دقیقه ۱۱۹</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18952" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btlp7ilQVCcCu5siGicc6dKMOAkDZJA2r-d7qSRPI2JYbI2PjiKIfTOPZafQmd1BrqQVgA9P3ijLkMdxdjWw2Q9IY9V5TUuLV7mJF58GARIvFHWdtos8LbVeyPhmOt_s24sPxwZ9F2MM2TX7oFFmXsUJxP4nOAwFIFols1LarphQqOZWL0TFySQ560Tbfari5eeU3mhQIrWVXjDK8Pzp2c9z1xWiTpU1Q5sdx1HoDD65OociI5mW4cfPpCrlclCa7pZIEufXpQjqwJ-H-Tuo51SAMd2fSjSBGLNdeG6dh0hPe54za18guclnvMuwN0mfbrH2D565GrBjHDGexQPyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام و اسپانیا قهرمان شد
🥲
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18951" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلللللللللللللللللللللللل دقیقه 105 برای پرتغال توسط رونالدو توی PS5 @WarRoom
🤯</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18950" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">من اینجا شوخی‌کردم بخدین وای گل اسپانیا واقعا دقیقه ۱۰۵ زده شد
🤯
🤯
🤯</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18949" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گللللللللللل برای اسپانیا
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18948" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیدبان اتاق جنگ : انفجار در سیریک تو دو نوبت یکی بین دو نیمه یکی هم وسط نیمه دوم شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18947" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلللللللللللللللللللللللل
دقیقه 105
برای پرتغال توسط رونالدو توی PS5
@WarRoom
🤯</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18946" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=RfhctD7zMp1MVJD7ODTeJjy_gSHz7n3y5e_PhHLDtOUaSWDoMWwE5LB3gCWN32diOUf6CPMQPTtGeg8-3DdXnirWfzjt03vKFO5zxY36VvAlBzH9kUa4Nlok2STqZSRv9LE3xy8FeD4c9dKlhyo0L5QhA9r_-AzbJEKfReJ8Yjn_k0TwB9jlH-ab4DyGRCQZYWaW39dOoxQBlqScrka-a64eBS6AEWqbA1qw6i0egche24C5c8yHqguVppJ4PQj_fgHzG7TJYxCQO1EX0oz0-FZrbTzPAERHZDEQeXvlOb2xn_wumCzWz9Ol1jBWbfw03cc0Hksd_A0TvZY5BF8qhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=RfhctD7zMp1MVJD7ODTeJjy_gSHz7n3y5e_PhHLDtOUaSWDoMWwE5LB3gCWN32diOUf6CPMQPTtGeg8-3DdXnirWfzjt03vKFO5zxY36VvAlBzH9kUa4Nlok2STqZSRv9LE3xy8FeD4c9dKlhyo0L5QhA9r_-AzbJEKfReJ8Yjn_k0TwB9jlH-ab4DyGRCQZYWaW39dOoxQBlqScrka-a64eBS6AEWqbA1qw6i0egche24C5c8yHqguVppJ4PQj_fgHzG7TJYxCQO1EX0oz0-FZrbTzPAERHZDEQeXvlOb2xn_wumCzWz9Ol1jBWbfw03cc0Hksd_A0TvZY5BF8qhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا چون پرچم پشت دروازه آرژانتین است صدا و سیما نمیتونه سانسور کنه و هی نشون میده
😍
🤣
🇮🇷
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18945" target="_blank">📅 01:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVbaLV-yIMEEWW3lX4xEHMSKZ6_j42FMmySKALGyN5Bnw8skjaFnmPDkNIL8Jf2D_yg9Ag5XppPzQkn14LQeKOO1tT5d25sDHbgdm_AKLc-SKxDxVeuqDAWaKHAbxF8rtX7O3ZU74wvo0L_xkQ0Z4jsffWygegQSgIHOKMGGVyBZjYicq2NhP-3h9MgKyXeGoM1wDpkK9p1B6TxN25ImHqZy52gp3zVu_bxdasadWM9gBrxmrS3mitGHLnqNvC3tkXZEmQj70g2usKTOCc4UL-7gs0--vqSF1bQGU-0wOuYU2oCDm8NT4oQnxqCl0dy3bHwb4GtvQwvjXS8GoH5xeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک همین الان بخش بمانی سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18944" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfNtFoRpzVjSHWufvip0iFJUQrEntqssELbUQscvN5ogTFgdl1jMjq3A9lq58OvoAGnf0qx1hRWj23IC-cggIQrzIM7naoQ7kFhUQ0rdMMBELj2nXS2j9MfK6xfTcY5taXLcI3E2xTsZItI1VHadY7ChHvKb1yk5SCwNkgNQvLdj-ugkTlyCBreWXNt6QCCboCr4owDQCTGcZ8MYaryFmZhzYgrSx_V8SBYnJBpxErGzNg-ujDy2gkXqMW8Q5vQg5kEL2dD20vSTdWY8o93kff-KFxYD4-mZhviF3NG-g5tVMU6e9bPT9Mf-X3yck92_6ZHvsfkMCNWTf8toAJ1Mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از اجرای طاعات و عبادات، هواپیمای E3B آواکس از ریاض عربستان بلند شد و یک سوخترسان هم ، هم اکنون روی باند در حال برخاستن است.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18942" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آرژانتین ۱۰ نفره شد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18941" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آژیرهای هشدار در بحرین به صدا درآمدند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18940" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی، از سرگیری محاصره بنادر ایران، ۶ کشتی تجاری را تغییر مسیر داده و یک فروند دیگر را غیرفعال کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18939" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بازی شموشک نوشهر از این فینال قشنگتره
😁
باور نداری ؟</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18938" target="_blank">📅 00:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd44e5f41.mp4?token=lUOD8T2vjmmUnIsFnrtcrp4ltBw0bLb8Q659xQtbuUHIATfKMFX2TvOr46kbwG1oX9S7zFskFpIf-ULg-S8pO7KBUKH5ZEzhJMZ3wMCcgEXjSd4yqLwAwz6nihi7mcDykhxCKeDhx_9kPnEUSVDghEXe1YV6GzvL05vawL_U-fIUlAW2LMDQ1OPgJlYCD7rbimmstSbokaiDJtyk-Aej6ZHz7f30lyNZh7qA2WS9uy79MQAeaM19girvdolnwBTKL8GoudGRK88KFW2mXzdto7354_zovEkyuOsslqYSiSJWDvCwcru4YvGO4RmY_9_BXb280gPRfCPrhH1dsXgo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd44e5f41.mp4?token=lUOD8T2vjmmUnIsFnrtcrp4ltBw0bLb8Q659xQtbuUHIATfKMFX2TvOr46kbwG1oX9S7zFskFpIf-ULg-S8pO7KBUKH5ZEzhJMZ3wMCcgEXjSd4yqLwAwz6nihi7mcDykhxCKeDhx_9kPnEUSVDghEXe1YV6GzvL05vawL_U-fIUlAW2LMDQ1OPgJlYCD7rbimmstSbokaiDJtyk-Aej6ZHz7f30lyNZh7qA2WS9uy79MQAeaM19girvdolnwBTKL8GoudGRK88KFW2mXzdto7354_zovEkyuOsslqYSiSJWDvCwcru4YvGO4RmY_9_BXb280gPRfCPrhH1dsXgo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای بیژن عزیز در فینال جام جهانی
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18937" target="_blank">📅 00:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پرتاب موشک از ساوه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18936" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شهرک صنعتی ماشین هایی تحت عنوان عود اومدن اینجا با این نوشته eod نمیدانم از کدام سازمان هستن @WarRoom
🚨
🚨
🚨
🚨
یاشار : من میدونم سازمان خنثی سازی مهمات و بمب هست !!!!</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18935" target="_blank">📅 00:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارسالی : درود بر رضا شاه فقید من نگهبان سوله «سانسور شد» تو شهرک صنعتی کاوه هستم  شهرستان ساوه استان مرکزی اینجا یکی از سوله ها دود شدیدی میده متسفانه نمیتونم عکس بگیرم صداش شیشه های کانکس منو شکوند @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18933" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc79a4e2e.mp4?token=mWVCUzeyT_Qe8lBl2lA2pGr7eLZWHlK5C32kmPujvsOM9ftZsgO66JTD0fOptI_7dEPCLyvDug-w780G3k3gi3mYfI0z34wRyexG03SMrQI6CLtqwdPfX3KPLbdLbmhNBGz0H6WazsTGEsPEICATF5d5OhzptxRAwbotRkRUM-8aWjeFP_Mvi1MxxtmlXpCUS1QOKWD9RY3M7VMrAU-1V7MhwHZ_GmwpF84uwABy919pBbnG0eDLjTHsNRaMbuZ0GfIElH4y2XCut_8gIMXgKyo4Mc49Z1_IuY6NTMA2pBpEPIAbtnYio1_5VI1hBwL49jWymHHXK3dNYa6UfA9kaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc79a4e2e.mp4?token=mWVCUzeyT_Qe8lBl2lA2pGr7eLZWHlK5C32kmPujvsOM9ftZsgO66JTD0fOptI_7dEPCLyvDug-w780G3k3gi3mYfI0z34wRyexG03SMrQI6CLtqwdPfX3KPLbdLbmhNBGz0H6WazsTGEsPEICATF5d5OhzptxRAwbotRkRUM-8aWjeFP_Mvi1MxxtmlXpCUS1QOKWD9RY3M7VMrAU-1V7MhwHZ_GmwpF84uwABy919pBbnG0eDLjTHsNRaMbuZ0GfIElH4y2XCut_8gIMXgKyo4Mc49Z1_IuY6NTMA2pBpEPIAbtnYio1_5VI1hBwL49jWymHHXK3dNYa6UfA9kaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از ساوه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18932" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارسالی : درود بر رضا شاه فقید
من نگهبان سوله «سانسور شد» تو شهرک صنعتی کاوه هستم  شهرستان ساوه استان مرکزی اینجا یکی از سوله ها دود شدیدی میده متسفانه نمیتونم عکس بگیرم
صداش شیشه های کانکس منو شکوند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18931" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">از خمین موشک شلیک شد
@warroom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18930" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یاشار جان ما دلیجان هستیم و اولین بار هستش که اینجا صدای انفجار خیلی شدید اومد خونه ها لرزید اما تو شهر نبود فکر کنم جاسب و کوه های فردو که  یک ساعت ازمون فاصله دارن رو زدن
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18929" target="_blank">📅 00:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیشترین گزارش از ساوه و بعد از اراک داشتم الان ساوه خیلی بد لرزیده و همه نظرشون شهرک صنعتی ساوه هست</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18928" target="_blank">📅 00:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خنداب/خمین صدای انفجار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18927" target="_blank">📅 23:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدای انفجار نزدیک به اصفهان
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18926" target="_blank">📅 23:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اراک بددددد  زدن
🚨
🚨
🚨
🚨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18925" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شهرک صنعتی ساوه
🚨
🚨
🚨
🚨
در انتظار تایید هستم …..
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18924" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش انفجار از  اراک و ساوه و…
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18923" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش های زیاد از صدای انفجار از نقاط مختلف ایران
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18922" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18921" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">روزنامه کویتی الجریده: خامنه‌ای (AI)
درخواست ملاقات نخست وزیر عراق را رد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18920" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWq_JAUu6xewJh6DcUKbbtrpRpyrPcF5M01LIPuVXvghp7NMwyW_6SAM3n1X_IbyxqoJjX0khwPeDzuDhVMEbQhppyjxdGDhTuxDGHZ_W90_oT134gOjqQhcuCdwZA5J17S6-qSxJk5vaLOACe04z2igHaJ7kqgVlcVmr3Q_cfjmQU1xZFjfGaE2q2nR10gBbf8FAJjTzz2U-YKBIeffzrfAS6brE-RiBWA9wwJpbxIqUGmpnc5kA6B1FJ1nFUud0EXTEHQizqZrpqCLHTg0-yaX0nEE7jx7TA-mVtmhfG7ibUADVKS_346ywv9xN8qQkN2q53YVB39Em_ectw3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سوخت رسان با فرستنده روشن هم اکنون از تل آویو اسرائیل بلند شدند همچنین فقط یک سوخت رسان با فرستنده روشن در محدوده خلیج فارس تنگه هرمز قابل مشاهده است.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18919" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18918">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارشگر صداوسیما رژیم : خیالتون راحت باشه که تا پایان بازی هیچ تصویری از ترامپ کو،دک کش و جنایتکار پخش نمیشه تا اذیت نشید.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18918" target="_blank">📅 23:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه سنتکام با تایم دیشب حمله را شروع کند حدود ۳ ساعت دیگر و بعد از پایان بازی و مراسم آن میشود …
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18917" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همچنین
سنتکام اعلام کرد
در ادامه حادثه حمله ایران به اردن در دو روز پیش ۱۷ ژوئیه (۲۶ تیر)، که پیش‌تر از کشته شدن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر خبر داده بودیم ، نیروهای آمریکایی پس از جست‌وجوی گسترده احتمالا بقایای پیکر سوم را در محل حادثه پیدا کرده‌اند. به گفته این فرماندهی، هویت این بقایا هنوز تأیید نشده و روند شناسایی و بررسی‌های پزشکی قانونی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18916" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام :
۱۸ ژوئیه (۲۷ تیر)
، یک نظامی آمریکایی در
شمال عراق
هنگام اجرای عملیات انفجار کنترل‌شده مهمات عمل‌نکرده متعلق به یک
پهپاد انتحاری ایرانی
کشته شد. در این حادثه، یک نظامی دیگر نیز زخمی شده و همچنان تحت درمان برای جراحات جزئی قرار دارد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18915" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رسانه های عراقی :کشته شدن یک سرباز آمریکایی در شمال عراق.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18914" target="_blank">📅 22:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فاکس نیوز:با پایان سوت جام جهانی٫ سوت شروع مجدد جنگ علیه ایران آغاز میشود
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18913" target="_blank">📅 22:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec470cd18.mp4?token=h7JnS3q3gSM9EnaYsW2arxAnPBVsnI3xZ7S-I_CDCtR3VGkO69_NiQOcJd2ksLXgZGyJ12nQXbE3lvqJEAZvjHeewycJ66WDHciiw4sqpTwrsvVkr9mgfDq1AM82mBDG9WFNmEd1O4Szuz_BY-du0noHYSNI48cqqWQHO_2b7OZjmMBFZg7_fCfRX3_SlA3ItbbEgiI7avP4OGHT8BsDP0LK5S-5MVYJBZura5umOD127fGmwigNdbCAU0YOv-vHlZi6iRvtOSEc1Cm83rhXYdFnZfYmQ2rStWsNag5RVzNGzN-MeIzScF0AumirqYzP7QlIxTP0KAlgusDuWclPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec470cd18.mp4?token=h7JnS3q3gSM9EnaYsW2arxAnPBVsnI3xZ7S-I_CDCtR3VGkO69_NiQOcJd2ksLXgZGyJ12nQXbE3lvqJEAZvjHeewycJ66WDHciiw4sqpTwrsvVkr9mgfDq1AM82mBDG9WFNmEd1O4Szuz_BY-du0noHYSNI48cqqWQHO_2b7OZjmMBFZg7_fCfRX3_SlA3ItbbEgiI7avP4OGHT8BsDP0LK5S-5MVYJBZura5umOD127fGmwigNdbCAU0YOv-vHlZi6iRvtOSEc1Cm83rhXYdFnZfYmQ2rStWsNag5RVzNGzN-MeIzScF0AumirqYzP7QlIxTP0KAlgusDuWclPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ترامپ به همراه رئیس فیفا و همسرش در جایگاه ویژه استادیوم نیوجرسی برای مشاهده بازی فینال جام جهانی حضور پیدا کرد. آیا او امشب رکورد دیگری را هم جابجا خواهد کرد و در تاریخ ثبت میکند؟ آیا او امشب دستور حمله شب نهم را به سنتکام میدهد؟ خواهیم دید چه خواهد شد. همزمان با بازی فرمان جنگ در ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18912" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: من دوست دارم تقریباً یک ماه را مثل مسی و رونالدو زندگی کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18911" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx30befmObJdreesUqdX4LKvDcGwqgKEVDkAfbSpsT6NsrWHxB-1lM9xt8Th1TLav6NcsWoxwFJkUJrCkINRBoTOtlzU46p0Kx-qWTrM7CCiI3L5appSJiEX_PtFbo9opzGy2C9plgVi2WuiQSnS4nXGcwz1Je4E-RpzplB1JgXBRaZu9QCtLMqGoBKOlTDMgHXW7HTWM2KKLH5cHoxzyHcQRTrSrSoE2_VtLgboafZZBJfXirdxaGr402cPGgoFZcss0v-nkP0IAvCQVX3UE7kBhRJuM2m2eAmf5HPrKiBa0yoKe7cNLUEstzwQR-fuwsxwx_CQ2q-x0FmqCFLf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ضرب الاجل هفتاد و دو ساعته محسن کج بند تمام میشود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18910" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از کشته شدگان جنگ با ایران گفت : آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18909" target="_blank">📅 22:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری CBS: جمهوری اسلامی ایران به حملات در روز دوشنبه ادامه میدهد تا قیمت نفت بیشتر بالا برود و ترامپ تحت فشار قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18908" target="_blank">📅 22:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیویورک‌تایمز
:
دسته جدیدی از جنگنده‌های f-16 و f-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18907" target="_blank">📅 21:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منابع به فاکس نیوز گفتند ، امریکا میخواهد در نبرد زمینی بزرگ ترین جزیره خاورمیانه که «قشم» است را تصرف کند و سپس لارک و هرمز و خارگو ابوموسی را تصرف کند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18906" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18905" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18904" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18903" target="_blank">📅 21:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18902" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش کویت: حملات جدید رژیم ایران تأسیسات متعلق به وزارت برق و آب را هدف قرار داد و باعث آتش‌سوزی و خسارات قابل توجهی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18901" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18900" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری i24 : اسرائیل تنها در صورتی به چرخه کنونی حملات آمریکا و ایران خواهد پیوست که باور داشته باشد ایران قصد حمله دارد، یا اینکه رئیس‌جمهور ترامپ به‌طور رسمی از تل‌آویو درخواست مشارکت کند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18899" target="_blank">📅 21:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شبکه 13 اسرائیل به نقل از یک مقام آمریکایی گزارش داد :  احتمال موافقت ما با این پیشنهاد بسیار کم است. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18898" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شبکه 13 اسرائیل به نقل از یک مقام آمریکایی گزارش داد :
احتمال موافقت ما با این پیشنهاد بسیار کم است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18897" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس۱۰ روزه :
1
- پایان جنگ و برقراری آتش بس
2
- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18896" target="_blank">📅 20:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18895" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایالات متحده به مقامات رسمی کشورهای حاشیه خلیج فارس گفته :صبر کنید. این ماه، ایران دیگر تهدیدی برای کشورهای خلیج فارس و جهان نخواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18894" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال 14 عبری: ایران در تلاش است تا با یک عملیات زمینی، پایگاه‌های آمریکایی در کویت را مورد حمله قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18893" target="_blank">📅 20:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل/سوریه رهگیری کرد. منشأ پرتاب در حال بررسی است. سیگنال‌های هشدار طبق پروتکل صادر شد. @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18892" target="_blank">📅 20:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18891">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل/سوریه رهگیری کرد.
منشأ پرتاب در حال بررسی است.
سیگنال‌های هشدار طبق پروتکل صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18891" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927e9308c6.mp4?token=lxDVSYGxARiHh5WW9O2DkXEIMDgpNC6wH7xq2XW5fRjKlZ2R9thlTC7wGBshTzVMGgGNxVWpn7gn0q31KL8oTGCf54bGL_yAtrFsJLQoUuoMVZBi-mH7HIt9_e6xhmM6pcHPHWxKIX8jqW4fSLhhB3DBnaRKnNWl9CVerR20cLT3AfADOfnFqu5jAbO-i9ajFy27oRthx2VnATfbIZ1nxOSo0yfYIICt2wHgTTRsVY6lSz7OVi7kKv7WOlWgGaVqATQGcDpYYN5S6NPOYp4tlM0ObcecCNpYsi-1TyN-ATJ4zChd3vxALsBc0Qw3EZtQAuXQLLXjSuXYmwUwW4n2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927e9308c6.mp4?token=lxDVSYGxARiHh5WW9O2DkXEIMDgpNC6wH7xq2XW5fRjKlZ2R9thlTC7wGBshTzVMGgGNxVWpn7gn0q31KL8oTGCf54bGL_yAtrFsJLQoUuoMVZBi-mH7HIt9_e6xhmM6pcHPHWxKIX8jqW4fSLhhB3DBnaRKnNWl9CVerR20cLT3AfADOfnFqu5jAbO-i9ajFy27oRthx2VnATfbIZ1nxOSo0yfYIICt2wHgTTRsVY6lSz7OVi7kKv7WOlWgGaVqATQGcDpYYN5S6NPOYp4tlM0ObcecCNpYsi-1TyN-ATJ4zChd3vxALsBc0Qw3EZtQAuXQLLXjSuXYmwUwW4n2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانوک : مدرنیته شوک و اخلاق سگ میخواهد !
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18890" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان از بالا سرمون پهباد شاهد رد شد به سمت کردستان میرفت احتمالن
صدای موتور گازی میده
ما زنجانیم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18888" target="_blank">📅 19:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک نیروگاه برق در کویت هدف قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18887" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
در ادامه شلیک‌هایی که به سمت اردن انجام شد، تعدادی موشک رهگیر به سمت تکه‌های موشک شلیک شدند تا احتمال سقوط ترکش‌ها در خاک اسرائیل منتفی شود.
در نتیجه،
تکه‌های موشک رهگیر در یک منطقه باز نزدیک شهر ایلات سقوط کردند، اما هیچ خسارتی وارد نشد و هیچ مجروحی وجود نداشت.
طبق سیاست‌های جاری، هیچ هشداری صادر نشد و این حادثه به پایان رسید.
هیچ تغییری در دستورالعمل‌های ستاد دفاع غیرنظامی اعمال نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18886" target="_blank">📅 18:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرمانده پلیس آبادان، ایران: صدای انفجار شنیده شده در آبادان مربوط به عملیات نیروهای مسلح ایران است و هیچ گزارشی مبنی بر حمله یا اصابت موشک آمریکایی در این منطقه وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18885" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18884" target="_blank">📅 18:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=EA8-wylOYviwducvavKVliZDCqoOY_6L5k4kmeTeYVtk4ieh31YKglsBBgrosIKSW-BwlgTytN06dl86DKKKGl44gZ-IH6k2AkYAKRIm8XEQt2ij30n3YHbpcObp4jQjfk0XnE1KC7qNG9iKqx1k7QZD6ROzOUQAdEVRZe2g5VBLsPHNUF230h9mSrqlim2MnKnx30jR-JoS146-C8bqohp4m_KE6yWgNTn0q5YXr4CAGpwoVdt4623fIm1WnrCg5K8mZV2Do27N3Wmtf-1ew7d5GPWbOXUtknrifUiGxs7IGrX34QpU9719ykLBjf0C_tPs7mwJBqK7qVu4kpVDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=EA8-wylOYviwducvavKVliZDCqoOY_6L5k4kmeTeYVtk4ieh31YKglsBBgrosIKSW-BwlgTytN06dl86DKKKGl44gZ-IH6k2AkYAKRIm8XEQt2ij30n3YHbpcObp4jQjfk0XnE1KC7qNG9iKqx1k7QZD6ROzOUQAdEVRZe2g5VBLsPHNUF230h9mSrqlim2MnKnx30jR-JoS146-C8bqohp4m_KE6yWgNTn0q5YXr4CAGpwoVdt4623fIm1WnrCg5K8mZV2Do27N3Wmtf-1ew7d5GPWbOXUtknrifUiGxs7IGrX34QpU9719ykLBjf0C_tPs7mwJBqK7qVu4kpVDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه I24NEWS: چند هفته پس از ترور رهبر سابق جمهوری اسلامی ایران، یک گروه تحت فرمان سپاه پاسداران در امریکا، قصد ترور پسر بنیامین نتانیاهو، به نام یایر نتانیاهو را در خانه‌اش در میامی، فلوریدا، داشت.
با این حال شین بت این توطئه را در آخرین لحظه طی درگیری در پارکینگ اپارتمان وی خنثی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18883" target="_blank">📅 18:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو مصاحبه‌ای که قرار بود امروز با شبکه فاکس نیوز داشته باشه رو به دلیل شرایط اضطراری لغو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18882" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=E2xcmdRfwG0rWMiZelz1beMd9sbFrxf6yGXcB9UcfDDI5OoTWFnGX50ZEfBPhYCkYdrtGRsPXQcDO6f65WaZwRUqmg-3mgyqYvLH2LGnurBRTWAfSPioR11KcGF5JqSRY-5vNxhevDZtxNlYoJTSkKKmbHnI0NJKD575f1hj_N6qpcr-oom5ygjgo0yYPxNLckVy1fm98iGUeXGen2bVMi7HdazAsFaGdtlVU55FsPd_6WT3QZye55C_voerf0VN6eHih5sZsGkhCXLW2-OrYEZKJ1cC0rnJn9rlTQulq2M-nKTz6Z1nX2ebrdTBC4Mg7h6rs8xwZbIHz14euTm5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=E2xcmdRfwG0rWMiZelz1beMd9sbFrxf6yGXcB9UcfDDI5OoTWFnGX50ZEfBPhYCkYdrtGRsPXQcDO6f65WaZwRUqmg-3mgyqYvLH2LGnurBRTWAfSPioR11KcGF5JqSRY-5vNxhevDZtxNlYoJTSkKKmbHnI0NJKD575f1hj_N6qpcr-oom5ygjgo0yYPxNLckVy1fm98iGUeXGen2bVMi7HdazAsFaGdtlVU55FsPd_6WT3QZye55C_voerf0VN6eHih5sZsGkhCXLW2-OrYEZKJ1cC0rnJn9rlTQulq2M-nKTz6Z1nX2ebrdTBC4Mg7h6rs8xwZbIHz14euTm5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام
:
ملوانان در حال آماده‌سازی جنگنده‌های پنهان‌کار F-35B نیروی تفنگداران دریایی امریکا برای برخاستن (تیک‌آف) از عرشه کشتی جنگی "یو‌اس‌اس باکسر" (USS Boxer - LHD 4) در حین عبور از دریای عرب هستند.
ناو باکسر، کشتی فرماندهیِ گروه آماده خاکی‌خاکی باکسر  یازدهمین واحد اعزامی تفنگداران دریایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18881" target="_blank">📅 18:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee9644417.mp4?token=sbl1VB2BRhAP7bkhqyncFuggTm855g3U1UhBb8VxsuEHp41DTjIia59jPslkjeewpBbUlbV6V5h0aEeMI0jkpwsB9fEhsRBozUbBinWnqv6ENWNLEA4H3-tiHZoVQQsnSMzwpN2X7cKaNDVRm1f3Z_80m8RFMymZDqiuKz2ngGg_6lA9el1jj5ewfl0v7qIMbLw0NItF2LoR29CDAnWxqY5xqwSplTCyqWEtlOpnoQ37KMny9YvFnkcN5dwba2-e1qDkgFgDcH1UuANoeMw9IXv0s20WykfAz0OBdQUa8OPZgVnP0z8TWRza6bcxdxzWSF5Ix2RxO6Dgr6j-RU--MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee9644417.mp4?token=sbl1VB2BRhAP7bkhqyncFuggTm855g3U1UhBb8VxsuEHp41DTjIia59jPslkjeewpBbUlbV6V5h0aEeMI0jkpwsB9fEhsRBozUbBinWnqv6ENWNLEA4H3-tiHZoVQQsnSMzwpN2X7cKaNDVRm1f3Z_80m8RFMymZDqiuKz2ngGg_6lA9el1jj5ewfl0v7qIMbLw0NItF2LoR29CDAnWxqY5xqwSplTCyqWEtlOpnoQ37KMny9YvFnkcN5dwba2-e1qDkgFgDcH1UuANoeMw9IXv0s20WykfAz0OBdQUa8OPZgVnP0z8TWRza6bcxdxzWSF5Ix2RxO6Dgr6j-RU--MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از سخنگوی قرارگاه کلش آف کلنز منتشر شد:
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18880" target="_blank">📅 18:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مهر:
معاون امنیتی استاندار خوزستان گفت که مکانی نزدیک به شهر آبادان لحظاتی پیش توسط حمله موشکی متعلق به آمریکا هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18879" target="_blank">📅 17:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18877" target="_blank">📅 17:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: حملات حوثی‌ها و ایران به عربستان پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18876" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل  @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18875" target="_blank">📅 17:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حمله جدید اسرائیل به جنوب لبنان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18874" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دو انفجار سنگین بندر عباس
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18873" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSDW8FXHXLZIvuBJiheTSlyC-vf_EuGPkMF2qewGbZoAAfpM90rZNiF2dqbLcFVrocRbPRY1IlAXFMzAtL9bZK-s__iepme-Ztj9zWvSYWYp31k_SeFy0VJehec5jWyjmsFJvu0DKI9oMX8EezHK412qdnxwZqjb1vyg-BEaz1ZN9GwhhS1RnvpPT3t6hPWig9hUmPKAoNVikHbxHeLBI9xcXvhTDEynhS6SeK4uQ_581zJPa-kRmfEqysz-chJjLmCCTEfr9qTv3hCICSCMX1n_k5vYrFjflmC-GRRLFFp2G9NO1Y6H1G4-cR_rUDOydHiwx0JfmF53JeNV5NRbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : وصله‌کاری موشکی؛ نشانه‌های فرسودگی و کمبود در زرادخانه جمهوری اسلامی؛ کفگیر سدمجید به ته دیگ خورده است؟
‏تصاویر منتشرشده از یک موشک و پرتابگر غیرمتعارف، نشانه‌هایی از فشار بر زنجیره تولید موشکی جمهوری اسلامی را آشکار می‌کند. بوستری بدون رنگ‌آمیزی و با ظاهری متفاوت دیده می‌شود که به نظر می‌رسد با کلاهک یا بخش فوقانی موشکی از نمونه‌ای دیگر مونتاژ شده باشد. پرتابگر نیز ساختاری ساده، کارگاهی و به‌مراتب ابتدایی‌تر از لانچرهای استاندارد دارد.
‏
این ترکیب نامتعارف می‌تواند نشانه استفاده اضطراری از قطعات موجود، کمبود بوستر و لانچر، یا مونتاژ ترکیبی برای حفظ توان پرتاب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18872" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPete Hegseth🇺🇲</strong></div>
<div class="tg-text">آبادان صدای یدونه انفجار اومد
خونه ها لرزید</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18871" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش صدای انفجار آبادان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18870" target="_blank">📅 16:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoJ5t4eXadSwZuJ1SXAPHumTaU1OyI_s8z1vwSJ7s2MS6GoKVZWeAA4Icc-a9Qqj_nIBvBzCo1npmbhcMGpiIUndsYnTn6zPeeoDOEMVFsRYgs4TsnpZ_eITYv1FszdEourZXCU24K-h8kKlW3T2YyVGFlLlarkK-7FfJYIHOly-pzwT20W4GxfVAgRX6CBlsGfsV2Pg9lejeEcj88sbQAprINlrufulkRrhKV8Lk7QCYGRJb4RO89qVvU6DzjKTqnY6XEtuYGb1iomUP4ncDKFbDebaAPwJsUOSGCzb_gAita8fClgTpKL0S8bUuVqyWVc3ec0qqpKN_bH4DB_01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشات میگن ، فرندلی فایر شده ، پدافند خودشون  موشک خودشون رو زده یا موشک خودش ترکیده
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18869" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چند فروند بمب‌افکن رادارگریز B-2 آمریکا تو روزهای اخیر در حال جابه‌جایی دیده شدن و به نظر میرسه دارن برای مأموریت‌های احتمالی علیه ایران آماده میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18868" target="_blank">📅 16:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚠️
کرمانشاه صدای‌ انفجار نیست پرتاب موشکه
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18867" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18866" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق گزارش ها،اسرائیل ممکن است در 24 تا 48 ساعت آینده،ارتباطات رادیویی خود را به دلیل تنش قریب‌الوقوع با ایران قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18865" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: تخلیه هواپیماهای سوخت‌رسان آمریکایی از فرودگاه رامون پس از هدف قرار گرفتن عقبه اردن
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18864" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18863" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رادیو ارتش اسرائیل:
سیستم‌های دفاعی آمریکایی دو موشک ایرانی را در منطقه العقبه رهگیری کردند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18862" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQeY5ZtNt6xPt2_eriq3E9Bksut6N2xnL5Lx5_eDlPDhZX_O00otzcla9VhuumJivO0CwO2KXkv5ULBjujY-74Gd-QrfOmE8qHh_pUAxmn5c9zwMUeuEwOp05xQM9viYWlPMXoxWxhQPpyDkX1vVPbrvmPm6VteL9vjr2eOARivWXciXDk-xICxsM-YPge5ADFxAKyzMsVSCHlsB5FQho6-1TyrAwGPa1ZLsuwn5qsXTE7SrxdSf5ECSvbPlE1PWJQsY-6kcQKRdWOgqKMLzkSHga2MtHgr32ntcCz8p4Td7QnfNBVRhfm2qIlqDoeZkIikpIjPsPpS_-AXe9isB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی در انبار گرانول مراغه… @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18861" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcnJzvYKJbl02V58XEWmJXOh6MtIq9p_edKXgYrQXd-RW-4tbCxw8_5Bm-37na-VrnNRT9_OULK3y3nYnavlQlvjqdX-UBEMjTKLPlUhOWNW0IX-K11HSn9iHfmlWD9bspKEI6Y1wVrHLCE7AdUVPvPpZSfdaBPAhPu0DCkb9yffWFraPbjO4MEbQvVfXpSd0BTVD2Baxe9ob6QqrSDYEKfMEuFZpqTj860SfWw3u74-MIQXUG8Y9KyN-GLJYSfvqnhudiPcF4VSoBZ8PsW2LeUwd7YpbNgDIdNEb7Y3hit7JKBDFace6EptbIlA9HY2RAFVcknFOzrSu9Z_nP0pQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کوهدشت ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18860" target="_blank">📅 16:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=FbvT9B184IGe26EmSNfbHNWRX0goxi-K0pEjOZlFyz1z_gEauWXg-zWLZH6VEUmrPK89LI-VYVSj_XduhQCRAkXQwPQdnNzolrj6N5oZL_5ST9sfIXUiJ6Fj9nKrZfmFKklEWPzEVRQwzZ7CL5FJXctw0I8bq7tzPbcmUSt9gyHtdgSkg9ls-Q0Pf6U63wHjIwl4gu3Mo3abVmxviy9Yvj3gxmpn8WOBtvOLPpIX_j_F1N_TCpF4T_rwnWFc5aH_0HRzCsd4stzn2rdlO1YfUq5HKDdnjU3GskBVZ4O6dcj5JpFPPPBreHBO1DgAF5o5QJ-VFkHkbSO6ImqkxRvTJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=FbvT9B184IGe26EmSNfbHNWRX0goxi-K0pEjOZlFyz1z_gEauWXg-zWLZH6VEUmrPK89LI-VYVSj_XduhQCRAkXQwPQdnNzolrj6N5oZL_5ST9sfIXUiJ6Fj9nKrZfmFKklEWPzEVRQwzZ7CL5FJXctw0I8bq7tzPbcmUSt9gyHtdgSkg9ls-Q0Pf6U63wHjIwl4gu3Mo3abVmxviy9Yvj3gxmpn8WOBtvOLPpIX_j_F1N_TCpF4T_rwnWFc5aH_0HRzCsd4stzn2rdlO1YfUq5HKDdnjU3GskBVZ4O6dcj5JpFPPPBreHBO1DgAF5o5QJ-VFkHkbSO6ImqkxRvTJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18859" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G49YsGN9v0-BCbkbPbknecwlSurTl_3n6HS1QUHxGN_9xonVPh9J7U3-2SZXZrFk-uCCnQ7F8IV8z4sIHLbRbksC0FQiZqU-FERlOm1VYDoYudRGZNe7TZMFxmw9cnTSGmZtNwzN6o8l-otX-rMlqvRZTM8JVY_fQZmvCltDlwb4SHqKqsC8wln8Lv2nQc06tkxUdkCThZTMQ26ml-kcU1qKU6lgIaetEBn4Vm621dD8sKs8TDWz12fDUpj19MdVI8DEDYj_jabwkUir_b5mzmG794Y1oreOpVS1vHgAyTvSjwRYc5rNMp9Jutx6a6plXGbcoYeifafYqAWoMZztZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از ایلام ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18858" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ارتش اسرائیل: چند لحظه پیش، ارتش اسرائیل پرتاب موشک‌هایی را از ایران به سمت شهر عقبه در اردن، که مجاور اسرائیل است، شناسایی کرد.
احتمال وجود دارد که در نتیجه این حملات، خساراتی به اراضی اسرائیل نیز وارد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18857" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: آماده‌باش هوایی آمریکا برای تشدید جنگ با ایران آغاز شده است
آمریکا تعداد سوخت‌رسان‌های خود را به سطح مشابه آغاز جنگ خواهد رساند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18856" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRPVUbMtx62HtNqv0pNA82lH9eSFAyqdaxJOYnLaQL6zB5WKrv0GJzNJGEVU3ne292hzKmuLBiN1LczXwhvbWGX8WJgm9AYLbmXh0zbxXgg5-SR1puuIcAvg3o5Xtqx4FVLhORjpcBhgivnFSxdnns8UhCtOUVYh_unLkXBUjUQxs_E1en6Zf9cEcFbH7MKXnuHQCnhNic2stK7zfZQsaykKAXZb3Sbb9z_U2zZscWeKtHX-mzcz__7dxpJMCR_uSXSp5Vl3YBAB3d-17mr1GkTop7vh7is0bH9pZZ2n2VBGcaIp4FPbwhOlPWgU9Ewv1H-r3WX_Cod2bW4zPpizwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این کاری بود که لیندسی می‌خواست انجام دهد و قرار بود اتفاق بیفتد. مهم!!!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18855" target="_blank">📅 15:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770115730a.mp4?token=oQGkwBqdL9x0suE1m_vkFV_kq7Tue2WKEYjPb1BNRnkN-n5NEZjJJ1bybZFM0BJlGSYOhUAQHimJEu_ZZgDnPaySdxlfuA8fEVJzftd9D9mtmIg3t3KjApsTo_l_RXPeREP1aMrD1gRjrDAWrHkbA4gyotCZICa2IyySxLf-82m1PVMM_rtlqaSz0TofOHfmTLQuMMmaNh25fFC5EsKT28opbjZmIqcxCIVl7G6h2hrVOMAnkezS9MdOi65XfXq-vpxRs_KEO5Jct8RfyAK11WSOHv0PNVQjxXEZPsmrNHT0M1imRWc8bctxUhGhIRA8UPD72uTrfExHgiAMKTxLNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770115730a.mp4?token=oQGkwBqdL9x0suE1m_vkFV_kq7Tue2WKEYjPb1BNRnkN-n5NEZjJJ1bybZFM0BJlGSYOhUAQHimJEu_ZZgDnPaySdxlfuA8fEVJzftd9D9mtmIg3t3KjApsTo_l_RXPeREP1aMrD1gRjrDAWrHkbA4gyotCZICa2IyySxLf-82m1PVMM_rtlqaSz0TofOHfmTLQuMMmaNh25fFC5EsKT28opbjZmIqcxCIVl7G6h2hrVOMAnkezS9MdOi65XfXq-vpxRs_KEO5Jct8RfyAK11WSOHv0PNVQjxXEZPsmrNHT0M1imRWc8bctxUhGhIRA8UPD72uTrfExHgiAMKTxLNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
در
انبار گرانول مراغه
…
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18854" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU1EygCVZeA9gAJJGSyTA0CYb3uNZml6GPai5ioeC_NtQ005oVBnKkdjS8h6IEYhNSgZfnvkupI56ezp050zpWoUqjK-4DV5rPd44GTJSH4vah_ctBdEonlsbLzO_-EMWASGLeTwA3kAQRsmB2iHu8nUqrNR8tg68zs2wh_NrVG2NNCf5kLaNAbuhgdldb9AL-0HUjl2EKkJQ4cy9ub6zqrKeFX6ePoCkrKlNSgfarv832bTCJNrfNFka1hQreBX_d3irXOvzgI0YWtmbL7104Kgv5-f9xZsV7w69vA6bsKgXx0BK-AlYn1Af5Ca6Yh-nr3NZPP5FfzyRNxTc-lULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروند ایرانی/آمریکایی ممنوع خروج شده که ترامپ اداعی آزادی و رژیم تکذیب کرد با نام دنا کراری بعد از 566 روز به آمریکا رسید
کراری، ۵۳ ساله ساکن کالیفرنیا، برای دیدار با خانواده به شیراز سفر کرده بود که گذرنامه‌اش توسط مقامات جمهوری اسلامی ضبط و از امکان خروج از کشور محروم شد. به گفته وکیلش، او هرگز رسماً زندانی نشد، اما تحت بازجویی‌های شدید و مکرر توسط سازمان‌های امنیتی قرار گرفت و در چند ماه گذشته تحت شرایط بسیار محدودکننده‌ای قرار گرفت.مقامات امنیتی کراری را به «همکاری با یک کشور متخاصم» و «جاسوسی» متهم کرده‌بودند
وی به عنوان کارمند در شرکت امنیت سایبری پالو آلتو نتورکز کار می‌کرد. او در کنار حرفه فنی خود، بنیانگذار یک سازمان خیریه حمایت از کودکان محروم بنام فرزندان مهر را نیز مدیریت می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18853" target="_blank">📅 15:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie1kcmEj2TWElMzRw12zK8zIpJbkjsRz5W137RPBbkZU_Brr3gvCFFySNwPFn7_upwlXUtWbUYB7GcLoZD63GMaazi6ftdbz_k19fbHtnc2e_JLM2Svbh9s_9iVgNsee7bR6WqYKvh_h7cuh3UPuqjqgxcgLZ4ynuEsQgaPJY6oV81xqyzITHhpGjGkhUrZ-yrBq1yIzRzh-9ZoVlIhoedOhc4P3OI9BQ-daiSQTHFpqvpcBo4vpiUio8KFacak183NdYyGZ_cp-LbPbDZsXmrzmjsvalAWmT80sEPptiPQNJ6SFhIsfdKg9UME6c4BBvYZEUNCzcJgKU0U5byQGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه هسته‌ای شهر دارخوین با نام های(کارون یا استقلال) در استان خوزستان، در ساحل رود کارون و حدود ۷۰ کیلومتری جنوب اهواز، در زمینی حدود
۵۰ هکتار
در حال ساخت است. این نیروگاه یک راکتور آب سبک تحت فشار (PWR) با ظرفیت حدود
۳۰۰ مگاوات
دارد که طراحی آن توسط متخصصان ایرانی انجام شده و ساخت آن توسط
شرکت
انرژی اتمی ایران
با مشارکت
گروه مپنا
و شرکت‌های داخلی دنبال می‌شود. عملیات اجرایی آن از
آذر ۱۴۰۱
آغاز شده، هزینه پروژه حدود
۲ میلیارد دلار
برآورد می‌شود و طبق برنامه قرار بود طی
۸ سال
حدود
سال ۲۰۳۰
تکمیل شود. این سایت زمان شاه نیز قرار بود میزبان دو راکتور ساخت شرکت فرانسوی
Framatome
باشد، اما آن طرح متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18852" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
