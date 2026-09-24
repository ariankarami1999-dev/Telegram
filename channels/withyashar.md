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
<img src="https://cdn4.telesco.pe/file/rtbdCo-gNqR4sOL2Pe9UoA8kpMqEMj7061mvch9EhJTsc_MKNd0OjDzYwtQgs9USShPYdq11DYvs09ui_JGUFqPhwnrSSUP1neE6vwmIKbiFyRoZGMmcnnLJuQCFTErEUMuwSSZ_7v6te4ciFbGM9vQtGAfd7XVYOK_TjG-S9_v6ZNqqzV7VvlRLV9o_hvdd3vNSNiC8StPeexkEB5WJHnDjDljRSfQseRfL4o9sgJVsrXxR3cryz65_RGvLNyiVmQ8fIaRR8BOAb6lhU1OpXxEjllyk15am-BQWXwjKdkhWaBbeTYSE5ribcgGJQQEDYEl2BFhhfwOaRnDP-Vtg6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 456K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 09:10:22</div>
<hr>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ژاپن:
نخست‌وزیر ژاپن، سانائه تاکائیچی، خواستار آن شده که مذاکرات درباره هرمز فقط میان ایران و آمریکا نباشد و کشورهای وابسته به این مسیر و سازمان بین‌المللی دریانوردی نیز در آن حضور داشته باشند. ژاپن می‌گوید حدود ۹۳ درصد نفت وارداتی‌اش در شرایط عادی از مسیر هرمز عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/23957" target="_blank">📅 09:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدای انفجار سیریک(میناب) مربوط بود به یه موشک/پهپاد که پرتاب شده بود و رو هوا رهگیری کردن آمریکایی‌ها و زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23956" target="_blank">📅 00:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1iUvXijEt7kGaee-FRXJBG8DOV-n1OT0YmBahwxFf4WWgGWhj7D-VfybQfZcn7w4xX_CMU7fSz_7FjRSQTORx2uJcTZqCIU5VwA02_s2ksXCTNKXQYpR-7SHwsc6s-jfaKZcl5lWXxc5Edwv3wc6RKmE_O5UWZZJpft6YwdV7Y9leuAMba-EssglmlvkAwm9u4wEiAwaLldgLzDQKB4iuf7qy_E_TSYLfDbkg-fR-feCASc2tJF0f3wBgZ5_fcCeftkufQZLZIR77W0G5QCXOkZLJz0FNmLuRcTt_19E5OMXszyAwcynKnm_sr_5RrWYIlvjzu_xmLMnMPEsQDSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوخترسان از اسرائیل بلند شدن به سمت منطقه  ، ۴ سوخترسان بر روی تنگه هرمز / خلیج فارس
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23955" target="_blank">📅 00:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای جنگنده نطنز
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23954" target="_blank">📅 00:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش صدای انفجار‌ خارگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23953" target="_blank">📅 00:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش صدای انفجار‌ و لرزش شدید میناب
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23952" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رگباری گزارش میاد از انفجار در بندر عباس
@WarRoom
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23951" target="_blank">📅 00:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23950" target="_blank">📅 00:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a2badc4b.mp4?token=AZ9TZVM27pQkvBD9zn7w7GGmySnHVoSJwiQ583HsRv1i01SOy6dGLRMkX1gSRYy9lPxxc79npoHtKz6xIx0SUjB7qjDDF-8GzBBSrZGh90Z1H1JMethIME8Lj4XQl_RQHlrT-gKvWueMHZipApRjVN-VBhIrrWxgOxRHaA0FFFQ9toducB1H4W07BBKnc9aaqDf5LdRNr-D3OWv8RYCXwWULHG6wvwfFtklhSJxYhql691WJtDoUQQozqrOodm7P_vA8xNf5lp1P2whdnWtiYpm_eL-1qg0vw7TtRr7ygkmU33AquEfJ9OU3fEGjyVCQ3Pjn5aNXFqoAzubQDKLq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a2badc4b.mp4?token=AZ9TZVM27pQkvBD9zn7w7GGmySnHVoSJwiQ583HsRv1i01SOy6dGLRMkX1gSRYy9lPxxc79npoHtKz6xIx0SUjB7qjDDF-8GzBBSrZGh90Z1H1JMethIME8Lj4XQl_RQHlrT-gKvWueMHZipApRjVN-VBhIrrWxgOxRHaA0FFFQ9toducB1H4W07BBKnc9aaqDf5LdRNr-D3OWv8RYCXwWULHG6wvwfFtklhSJxYhql691WJtDoUQQozqrOodm7P_vA8xNf5lp1P2whdnWtiYpm_eL-1qg0vw7TtRr7ygkmU33AquEfJ9OU3fEGjyVCQ3Pjn5aNXFqoAzubQDKLq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی از خبرنگار خارجی میپرسه نظرت درباره تیم ملی ایران تو جام جهانی چه بود؟
خبرنگار خارجی‌ میگه : جالب بودید، مخصوصا اون عینک شجاع خلیل زاده
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23949" target="_blank">📅 23:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏حالا من کاری ندارم ولی این یارو «باصر بهرام نژاد» که محافظ موشعلی بی گور  بوده و تو جنگ اخیر سقط شده ، بیشتر بهش میخوره بابای نوه های خامنه ای بوده باشه تا محافظش @withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23948" target="_blank">📅 23:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تنگه صدای  بادیگاردهای خامنه‌ای میاد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23947" target="_blank">📅 23:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرگزاری The National
: طبق اطلاعات منابع منطقه‌ای، طرح ایران شامل
آتش‌بس منطقه‌ای تا ۶۰ روز، بازگشایی مرحله‌ای هرمز، پایان محاصره آمریکا و تعیین یک جدول زمانی برای مذاکرات جامع
بوده است. این منابع می‌گویند
ترامپ فعلاً حاضر نیست محاصره را پیش از مشاهده «اقدامات اعتمادساز» از سوی ایران لغو کند
.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23946" target="_blank">📅 23:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارتش اسرائیل در عملیات گسترده ۲۳۰ فرد را بازداشت کرد و یک آزمایشگاه بمب را کشف و منهدم کرد.
تیپ ناحال ارتش اسرائیل طی ماه‌های اخیر در مناطق یهودیه و سامریه (کرانه باختری) بیش از
۱۲۰۰ مکان
را بازرسی کرده، حدود
۱۰۰۰ مظنون
را مورد بازجویی قرار داده و بیش از
۱۰۰ قبضه سلاح
کشف و ضبط کرده است. به گفته ارتش اسرائیل، نیروها همچنین یک آزمایشگاه تولید مواد منفجره را شناسایی و منهدم کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23945" target="_blank">📅 23:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2od5axPQiIDfrdYKqz7geX2I_gz0_wLExWb9ycgCHl6gqPCqM7kP8rv9nMKMiQSe4TtPAs5hxAW6ucwg39-lVErP4G07IuYOR_tCIPITgqX3e2bFjFTbk29AAvGFJAEApfawp2wJd0r8ZQ6BIP3Qrds4ZHWyedAAHGsGLxnMH_SjPA8SHHKKfLoqNHp5QV-yp6HoEWyIfN6ZcuvTQVtf5PAzOXzlpOggSrHUjz6iqtKW2ls5QnsCcN8xnBQWxZbfYJqEHAB3VoISMz9HSCGYrtZ5P3AjXgA2mtLo9-n6EVCSftOYkLPIRX4KGfowT2muhqmCEq816wye89nymp7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز امنیت دریایی عمان اعلام کرد کشتی تجاری
CAPE DAO
در نزدیکی استان مسندم و در فاصله ۲.۵ مایل دریایی از ساحل هدف قرار گرفته و در پی حمله، موتورخانه کشتی آتش گرفته است.
۲۷ خدمه تخلیه شدند و یک خدمه، که یک شهروند هندی بود، جان باخت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23944" target="_blank">📅 23:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پزشکیان در نیویورک در هتل مستقر نشده است؛
رئیس‌جمهور ایران به‌جای هتل، در
محل اقامت نماینده ایران در سازمان ملل (رزیدانس)
مستقر شده است. فارس دلیل این اقدام را کاهش هزینه‌های سفر عنوان کرده و گفته این اقدام برای نخستین‌بار توسط یکی از روسای‌جمهور ایران انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23943" target="_blank">📅 22:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز : ایران تهدید به فلج کردن فرودگاه‌های کشورهای همسایه کرد:
محسن رضایی، دبیر شورای عالی امنیت ملی ایران، گفت اگر کشورهای همسایه در همکاری با آمریکا پروازهای ایرانی را متوقف کنند، ایران کاری خواهد کرد که فرودگاه‌های آنها دیگر قادر به فعالیت نباشند. این تهدید در پی اعمال فشارها و تحریم‌های جدید آمریکا علیه شرکت‌های هواپیمایی ایران مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23941" target="_blank">📅 22:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چقد زرنگین‌ برای پست نتانیاهو ریکشن خنده رو میبندی</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23940" target="_blank">📅 22:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBI DO?</strong></div>
<div class="tg-text">چقد زرنگین‌
برای پست نتانیاهو ریکشن خنده رو میبندی</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23939" target="_blank">📅 22:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانادا: امروز پنج فرد و پنج نهاد ایرانی را تحریم کرد.
وزیر امور خارجه کانادا اعلام کرد این تحریم‌ها تحت مقررات اقدامات ویژه اقتصادی علیه ایران اعمال شده و دلیل آن، از نگاه دولت کانادا، نقش این افراد و نهادها در
نقض حقوق بشر، سانسور، سرکوب و استفاده از خشونت غیرقانونی
عنوان شده است. در میان افراد تحریم‌شده
اسکندر مومنی، وزیر کشور ایران، داوود معظمی گودرزی، رئیس پلیس فتا تهران بزرگ، رسول جلیلی، محسن فتحی‌زاده و روح‌الله مومن‌نسب
قرار دارند. پنج نهاد نیز شامل
ساترا، کارگروه تعیین مصادیق محتوای مجرمانه، گروه دوران، شرکت یافتار پژوهان پیشتاز رایانش و سازمان فضای مجازی سراج
هستند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23938" target="_blank">📅 22:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPxBakvUK48399bG_TLfuJ5AgEn1IoMKf5Q5-XRyAWBHfQOLSUE6be049UYl73wOIVP5HsrZty5hVHcpE1iUb6IsR6v_zdjk4mWrls7hz7qOaK4z_K1RL6t3We9LaZQoEA2QqVW_eh55LXQGaCybgTHRNJjup-Z89upR7c-o1QzP6QnC8BcSLPjUkz4emuDr-we9C5LcKSwo-qZjdnJlVmKYj-8PvD62YRssiVNF4Wjd1nnqA9fhzymrivJkDj2bChrnEaaOfcMxwaZopYAeoDgsXmWOnvWSppbpkG34C5LuOqngz433xvj80fQtbgXccsArEbrtJRGCxa3b4Y2BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت به 103.52 دلار برای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23937" target="_blank">📅 22:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الجزیره ,جزئیات مذاکرات ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل:
ایران از طریق میانجی قطری شروط خود را به آمریکا منتقل کرد که شامل
پایان جنگ در همه جبهه‌ها، توقف اقدامات نظامی آمریکا، رفع محاصره دریایی، پایان جنگ اقتصادی و آزادسازی دارایی‌های ایران
است. اسماعیل بقایی، سخنگوی وزارت خارجه ایران، این شروط را اعلام کرده است. در همین حال، استیو ویتکاف، فرستاده ویژه آمریکا، گفت دو طرف از طریق میانجی‌ها مذاکرات طولانی و فشرده‌ای داشته‌اند و این گفت‌وگوها را «سازنده و امیدوارکننده» توصیف کرد. تهران بازگشایی تنگه هرمز را نیز به کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران مشروط کرده و گفته است در صورت تحقق این شروط، امکان بازگشایی هرمز ظرف هفت روز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23936" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e07f1b30d.mp4?token=szfVlLYPB-luud3CxIcJtfe0aVvv2rlfS0K5ruPVN7i4w7fgumUQlNvqhwWfEHhH_612IJQsCUu3mif1khTDtyGHU1FVav6E4A_r1nDYXOKd_hPULxij6tDDV6eWT5dCqQCw9FP2YGBbcAHR4mmJyn9Jveg0yLDv4cZnk-sCcgJznq_C6ogwH6kdpFx6nrQ4YCFVUiEv-8JZpVMEXhcnZ-J_MO8fvAkKV7Mz8__XuHtxC4JMYw_WBwrtCpRb69C_Wvlioag6vUqS-TaC7XfiX5Dgw10wt-pN91C3u8iHyllFlQtUK0WDD9Dk8F-jQk0qmNN6lwSQBtxz8Dh3KcHcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e07f1b30d.mp4?token=szfVlLYPB-luud3CxIcJtfe0aVvv2rlfS0K5ruPVN7i4w7fgumUQlNvqhwWfEHhH_612IJQsCUu3mif1khTDtyGHU1FVav6E4A_r1nDYXOKd_hPULxij6tDDV6eWT5dCqQCw9FP2YGBbcAHR4mmJyn9Jveg0yLDv4cZnk-sCcgJznq_C6ogwH6kdpFx6nrQ4YCFVUiEv-8JZpVMEXhcnZ-J_MO8fvAkKV7Mz8__XuHtxC4JMYw_WBwrtCpRb69C_Wvlioag6vUqS-TaC7XfiX5Dgw10wt-pN91C3u8iHyllFlQtUK0WDD9Dk8F-jQk0qmNN6lwSQBtxz8Dh3KcHcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : تا امروز ۲۳ سپتامبر، ۱۱۵ کشتی تجاری برای اجرای محاصره «دیوار فولادی» آمریکا تغییر مسیر داده‌اند.
از آخرین بروز رسانی‌ دیروز ،
پنج کشتی جدید تجاری دیگر جلویشان گرفته شده و بازگردانده شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23935" target="_blank">📅 22:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تایمز اسرائیل : بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امشب عازم نیویورک می‌شود و صبح پنجشنبه ۲۴ سپتامبر وارد آمریکا خواهد شد. او قرار است ساعت ۲ بعدازظهر به وقت نیویورک در مجمع عمومی سازمان ملل سخنرانی کند و همان شب، بدون حتی یک شب اقامت در نیویورک، به اسرائیل بازگردد. این سفر به‌شدت کوتاه شده و گزارش‌ها از ملاحظات امنیتی و نگرانی‌های مربوط به اعتراضات و شرایط منطقه‌ای به‌عنوان عوامل این تصمیم خبر می‌دهند. نتانیاهو نیز گفته است که در سخنرانی فردا «غافلگیری‌هایی» خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23934" target="_blank">📅 21:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23932">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695a72d7e.mp4?token=BMAfHK8FGOnu9o7KIZ_CTD31N07X6E_1BAs0w32tsSd5Ac5065gI9KD6PdkRCUQO98huDhtBSADmf_0wRHC6rABh5txN_L9VVJcp4r773Ud-PjhZaqxVHdAH05vV5284yMmBBIB1FBOKj2AOvFlbzUsX7h1pl1hzhaNjC-0G6hRxWM2GhiB_lc0DvaYk7kmeIQM2MIfh9WHZocuP_5iqWG5dtzYJpIiCVv_gTL0Ebm46Nzu7BGMqOUjKvo7SDHmWWik8t_PHdDT9AmCRb_p7fr6uBEdPYxSWbrbLnkxT48DQgHzFrhy4vTqYnHbHwQ9L-dHzn46utYt8pVI8-_lhaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695a72d7e.mp4?token=BMAfHK8FGOnu9o7KIZ_CTD31N07X6E_1BAs0w32tsSd5Ac5065gI9KD6PdkRCUQO98huDhtBSADmf_0wRHC6rABh5txN_L9VVJcp4r773Ud-PjhZaqxVHdAH05vV5284yMmBBIB1FBOKj2AOvFlbzUsX7h1pl1hzhaNjC-0G6hRxWM2GhiB_lc0DvaYk7kmeIQM2MIfh9WHZocuP_5iqWG5dtzYJpIiCVv_gTL0Ebm46Nzu7BGMqOUjKvo7SDHmWWik8t_PHdDT9AmCRb_p7fr6uBEdPYxSWbrbLnkxT48DQgHzFrhy4vTqYnHbHwQ9L-dHzn46utYt8pVI8-_lhaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:ما برای وقوع معجزه‌ای دعا می‌کنیم که جان پسر سفیر اسرائیل در آمریکا را نجات دهد. او در جریان یک حادثه تصادف در کرانه باختری مجروح شده است. @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23932" target="_blank">📅 21:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در آخرین درگیری امروز قرارگاه قدس نیروی زمینی سپاه و مهاجمان در منطقه سراوان ‌فرمانده قرارگاه عملیاتی سجاد ، حسین ظریفی ‌کشته شد @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23931" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rox9q3mpJny5Mf_2Q2kD4uxKppQT_wNjVNkNr9HLy2OFYeCvISofI-33fCZDQ6uq0MD3KzcUMdcbkZ2j8d2Pugg7R2pLVjy9wJVxZ4EAAUBPyRcb-FUjabOLRTeVkwFW3C1O4Zek-uR9X6GOLlzkkRMhzM5j47juLmkMyz0mKMuKVbDUabgCqjk52dWrj9CsjXxDy3Vp_dBaW-6J_Ig-O-PjwAvFmI_WJTumf58o2Um5pUGqydxmnW6ipoK99f8mNWbseYRWSATK4QiEGHe9JSfpAwzvjXCykTeICPQDPuqcxEYSWdmSOZ7PtivvIu2iuSNQwgmNPpM-sqhlksTWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری شدید نیروهای مزدور رژیم با گروهای مسلح در سراوان همین الان ! @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23928" target="_blank">📅 20:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو:ما برای وقوع معجزه‌ای دعا می‌کنیم که جان پسر سفیر اسرائیل در آمریکا را نجات دهد. او در جریان یک حادثه تصادف در کرانه باختری مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23927" target="_blank">📅 20:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEB2rQrp_M_hC0tmvlw2jE067BWaMJmQB5ath0OZ-at6Jinfwh4FFDKCQLcypymItuf2Cuw2bry-pJMhUFuO47DxVWl7tyY68MVtw6qQrA58ggFd2Hqn0byS90IOJPxQIwxegg52gi5WVLHjc_omL0Kq3q3JRu9izAhmh475oL_uQFM96-XZLbGKlCz99zZWIkeZ-fAV_fH1wNY6wwyjJ8bJffvp1sPFowJxxfoGZ3ozQAv8LZoAdX4ew-ZAyKcqoaV6Zcb6q2h--9I1u-lGvnhNS5rEHrCgnkIgZpaSyQ9D0LtWMzWz67OBuIJGT9Gb9GZIVg9hnZFQcJKSPkXakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر و داماد پزشکیان در سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23926" target="_blank">📅 20:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز:
چین پیش‌تر از ایران خواسته بود برای مهار حوثی‌ها اقدام کند؛ این درخواست پس از افزایش سریع نفوذ نظامی حوثی‌ها و نگرانی عربستان از تهدید باب‌المندب مطرح شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23925" target="_blank">📅 20:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد. این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23924" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ایران:
مذاکره بس است.
عمل کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23923" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506767e20.mp4?token=eahukq0xu6m1X3q5R1Ciymie-Lq9X_FMYMkwXVNt3dVYh7Cs2I1yyEuiAWQ-Xj-Sm2bZMIzUYdmHPw31Cva9SfLSl2WlynkNxmr0b6pscT5Xo11ZmWplZ3thfyUuFSfTriDnF4rGDVLkrVyhZRw1l3IcmIx4eBR6pwA9CTZSYumoecO9EB3-29LOE6VWIibrZR5MsRwyr4nwPH6HhLNj13yd-V_XGG8h5Xch1aUNWV2707_dJh-_2M36F-AXCwTsanLCUw_l4RpSKam1_YdLhTBM2ZsZTuJQbetNOFh-b-waj5txNAwrg2aQQsdnGQnvsKxiQ5XXmDn2AkoYL1LdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506767e20.mp4?token=eahukq0xu6m1X3q5R1Ciymie-Lq9X_FMYMkwXVNt3dVYh7Cs2I1yyEuiAWQ-Xj-Sm2bZMIzUYdmHPw31Cva9SfLSl2WlynkNxmr0b6pscT5Xo11ZmWplZ3thfyUuFSfTriDnF4rGDVLkrVyhZRw1l3IcmIx4eBR6pwA9CTZSYumoecO9EB3-29LOE6VWIibrZR5MsRwyr4nwPH6HhLNj13yd-V_XGG8h5Xch1aUNWV2707_dJh-_2M36F-AXCwTsanLCUw_l4RpSKam1_YdLhTBM2ZsZTuJQbetNOFh-b-waj5txNAwrg2aQQsdnGQnvsKxiQ5XXmDn2AkoYL1LdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در سخنرانی مجمع سازمان ملل به جای لغت سانتری‌فیوژ گفت سانتیری فوژ
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23922" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26cd367cad.mp4?token=NzYPAibpTiPoWlUJS4ORW2UhLW1gYNi3uyBb69GVAxRa6fcUxNgDdhIkLEjGlQC7WhITF6MIXDvHxN5G8P8canFDtU_LjqbqIsypmxvBg09E-ngiYjTjeJjwLpwhUSIkJs5WzbHz8o97lmfEAl1XvORREfDxrMSty54pI2Hvi-UH9NLoOhga9prPtGQ_R5FjrcGPJwTez4al0-9QGw-hOajmKOF6wEg2GLUJWee3Bg8gVQQMHdLpsaTJrJP0YdDMvPlf_kOEsxpx8koI3ee0S8lhGcy6mJ3yQ55UoLALNnP8keHP6jt8oMAlaVRE_bT84oRgGTo-Cr8n2uAi8nY9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26cd367cad.mp4?token=NzYPAibpTiPoWlUJS4ORW2UhLW1gYNi3uyBb69GVAxRa6fcUxNgDdhIkLEjGlQC7WhITF6MIXDvHxN5G8P8canFDtU_LjqbqIsypmxvBg09E-ngiYjTjeJjwLpwhUSIkJs5WzbHz8o97lmfEAl1XvORREfDxrMSty54pI2Hvi-UH9NLoOhga9prPtGQ_R5FjrcGPJwTez4al0-9QGw-hOajmKOF6wEg2GLUJWee3Bg8gVQQMHdLpsaTJrJP0YdDMvPlf_kOEsxpx8koI3ee0S8lhGcy6mJ3yQ55UoLALNnP8keHP6jt8oMAlaVRE_bT84oRgGTo-Cr8n2uAi8nY9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو، درباره مهمات جنگ با ایران : ما مهمات کافی برای دستیابی به اهداف خودمان در صورت ایران داریم، اما تنها در ایران نیستیم.
ما تعهداتی در منطقه هند-اقیانوس آرام داریم. ما تعهدات فزاینده‌ای در فرماندهی جنوبی داریم. ما تعهدات و متعهد بودن‌هایی به ناتو و شرکایمان در آنجا داریم. هر بخشی از جهان که بروید و به آن‌ها بگویید که پنج سرباز آمریکایی کمتر و دو هواپیما کمتر خواهد بود، همه وحشت‌زده می‌شوند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23921" target="_blank">📅 19:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، شروط رژیم را اعلام کرد: در حاشیه نشست مجمع عمومی سازمان ملل، در ادامه گفت‌وگوهای میانجی‌گرانه بین ایران و آمریکا،
از طریق میانجی قطری میان دو طرف پیام‌هایی ردوبدل شد
. این روند حدود دو ساعت ادامه داشت و شروط ایران برای احیای دیپلماسی به‌گونه‌ای مطرح شد که
هیچ شک و شبهه و بهانه‌ای برای طرف آمریکایی باقی نماند
.
بقایی افزود:
شروط ایران روشن و شفاف است
؛
توقف اقدامات تجاوزکارانه آمریکا، از جمله حمله محاصره دریایی و تروریسم اقتصادی، پایان جنگ در همه جبهه‌ها، آزادی اموال مسدودشده یا محدودشده ایران و پذیرش مسیر امن کشتیرانی مطابق توافق میان دو دولت ساحلی
…
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23920" target="_blank">📅 19:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f84599d5.mp4?token=BOtoqd2Lc9pXUs3fJB4msujAo_BKg2cJYzE9k7oEoAaoayD0m-pFmgUeS1CpZULXzxwTQjCUOZnFuKon8YzgsdJ66rern0zSztHsIq6WpFRJlZlolFoQhHaw0hubBRqgQJtrup7Y9Smek0fR0b2gW_E6inyD8Fv5waFc4-Hn5Jp9J5TvcPqveO-Nl6AdlbgdT51GDuWFVRx0ciC8tSr-puvNaNHBuEkjD0h0CxAeMPMZHqas4CcKDg7Ha2acKwWzHaQx4tsA2Z721DnvqhWSqg_o2VemkJgJ6Up_oe6kD06bk1IsCPeAkdqh5t-5vPdLW8jPyu7uPzLH7rlIAHTkhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f84599d5.mp4?token=BOtoqd2Lc9pXUs3fJB4msujAo_BKg2cJYzE9k7oEoAaoayD0m-pFmgUeS1CpZULXzxwTQjCUOZnFuKon8YzgsdJ66rern0zSztHsIq6WpFRJlZlolFoQhHaw0hubBRqgQJtrup7Y9Smek0fR0b2gW_E6inyD8Fv5waFc4-Hn5Jp9J5TvcPqveO-Nl6AdlbgdT51GDuWFVRx0ciC8tSr-puvNaNHBuEkjD0h0CxAeMPMZHqas4CcKDg7Ha2acKwWzHaQx4tsA2Z721DnvqhWSqg_o2VemkJgJ6Up_oe6kD06bk1IsCPeAkdqh5t-5vPdLW8jPyu7uPzLH7rlIAHTkhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: من نمی‌خواهم مذاکرات دیروز را به‌عنوان یک پیشرفت بزرگ توصیف کنم، اما در عین حال فکر می‌کنم مهم بود که دست‌کم یک گفت‌وگو صورت گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23919" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f1d757e.mp4?token=X6xOu3UuWuEuf0vfQQqLViJ3B9TLAlbiniq4Yoe31a-iCawtNVCbj--M5aVXR8ie7_aMASGK3L9mzwjGsn2XhfB6sSvgLJ4Zz8f4quYsFrpPWqWyvSkdQI7tL2sBRFY-vsFpUnDKWrr-I0mpVQ_hOtYu4b0-QIGzETmukdBcy6C2HR7N7qV_c7HzYnmaVyiCKfrF7eToua_kXGyoz95RqzOI4nLR6LTjCQmkylPCRoGNHJO7Vfz83edGNzmx7i042KTam46X6Oh86lwkiJzyng3eCl-UPNOJA9fpbaoytIMbik0ogICqg6Iuu-XEt1Qh9qm-0yXMnASgMDHw38PQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f1d757e.mp4?token=X6xOu3UuWuEuf0vfQQqLViJ3B9TLAlbiniq4Yoe31a-iCawtNVCbj--M5aVXR8ie7_aMASGK3L9mzwjGsn2XhfB6sSvgLJ4Zz8f4quYsFrpPWqWyvSkdQI7tL2sBRFY-vsFpUnDKWrr-I0mpVQ_hOtYu4b0-QIGzETmukdBcy6C2HR7N7qV_c7HzYnmaVyiCKfrF7eToua_kXGyoz95RqzOI4nLR6LTjCQmkylPCRoGNHJO7Vfz83edGNzmx7i042KTam46X6Oh86lwkiJzyng3eCl-UPNOJA9fpbaoytIMbik0ogICqg6Iuu-XEt1Qh9qm-0yXMnASgMDHw38PQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنگام سخنرانی مسعود پزشکیان در مجمع عمومی سازمان ملل، نمایندگان آمریکا، بریتانیا، آلمان، فرانسه، اسرائیل، سوریه، لبنان، عربستان سعودی، مصر، امارات متحده عربی، الجزایر، لهستان، سوئد، دانمارک، کانادا، ژاپن، جمهوری آذربایجان، مالزی، نیوزیلند، استرالیا، کنگو، اکوادور، قبرس، ایسلند، مکزیک، کویت، بحرین، اردن و آرژانتین سالن را ترک کردند.
در مجموع ۳۰ کشور.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23918" target="_blank">📅 19:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز بانک مرکزی امارات متحده عربی درپی تحریم آمریکا بانک ملی ایران را از فعالیت در این کشور منع کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23917" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تایمز اسرائیل :
مارکو روبیو، وزیر خارجه آمریکا
گفت امشب جلسه دیگری با ایرانی‌ها برگزار خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23916" target="_blank">📅 18:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abc111212.mp4?token=nk-9Y2ZtI64uj-7CRNuev2PiAlAlBe0b34RaM2sNiadfWIU3ahYq5R83CK4-xl3Dm3HrmEasuLFpiVuBiuy1wHyEP6URNs7LDW6Xee4wkEJr6Ui1IPgNIDcpn9NQ1PZclUgFkiUxztlPux9myGKpTarafo0WJMGoo1iza6tG0s6Bq60XhNmD6-FzlQSmisIVmVYtl55AFUmiLaplr_g-Ms3PTG3MXDWyZK15yEWBQ8ItMxeT6LlVetfI6ds6v1Nfpi7MeNlG-CGsCMOFboUZWMMMa4lGhisk4yMUt4Pd6LfAk2I6ddbGwsuEdU2fd2_eE8e-Fj54VloBfEhvKXyv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abc111212.mp4?token=nk-9Y2ZtI64uj-7CRNuev2PiAlAlBe0b34RaM2sNiadfWIU3ahYq5R83CK4-xl3Dm3HrmEasuLFpiVuBiuy1wHyEP6URNs7LDW6Xee4wkEJr6Ui1IPgNIDcpn9NQ1PZclUgFkiUxztlPux9myGKpTarafo0WJMGoo1iza6tG0s6Bq60XhNmD6-FzlQSmisIVmVYtl55AFUmiLaplr_g-Ms3PTG3MXDWyZK15yEWBQ8ItMxeT6LlVetfI6ds6v1Nfpi7MeNlG-CGsCMOFboUZWMMMa4lGhisk4yMUt4Pd6LfAk2I6ddbGwsuEdU2fd2_eE8e-Fj54VloBfEhvKXyv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه اراجیف پزشکیان در سازمان ملل: پزشکیان با اشاره به جنگ ایران و آمریکا و اسرائیل، حملات به ایران را محکوم کرد و گفت ایران قربانی تروریسم و تجاوز شده است؛ او در اقدامی قابل‌توجه تصویر علی خامنه‌ای را در مجمع عمومی بالا برد و گفت رهبر ایران بدون دلیل ترور…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23915" target="_blank">📅 18:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23914">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766b749308.mp4?token=hCiQGiKSjJtKtTEuFhce850J5KuA5fKGWCWEFCjYFaHs0XAgjif3YnGDd-fngSKtZqPwsbSSp56y60gc3KbxnzLaUtxbf9EoVP1icimacOZqyOaWersnqqdJMeZLdT-ZyVyGrafjlGmBrzmDExI1O4i7ABlJrrreXZQ8znXyR9d1WaTZMBr1qxMlk_PR1b_dc_6iZGLsKItImH-qdcSBWJiLqK0FUi4Xf7ZDjAiSwNSzXDCBpj_dfDj1kv9SYPFBiPMH8fIVAT27BL1CrYmyquOOBd3MfIa0f2__6S_LoznP5ThTlpnWxhYqAMbeByToZgEGW_GeuL9BPFq_HT5ZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766b749308.mp4?token=hCiQGiKSjJtKtTEuFhce850J5KuA5fKGWCWEFCjYFaHs0XAgjif3YnGDd-fngSKtZqPwsbSSp56y60gc3KbxnzLaUtxbf9EoVP1icimacOZqyOaWersnqqdJMeZLdT-ZyVyGrafjlGmBrzmDExI1O4i7ABlJrrreXZQ8znXyR9d1WaTZMBr1qxMlk_PR1b_dc_6iZGLsKItImH-qdcSBWJiLqK0FUi4Xf7ZDjAiSwNSzXDCBpj_dfDj1kv9SYPFBiPMH8fIVAT27BL1CrYmyquOOBd3MfIa0f2__6S_LoznP5ThTlpnWxhYqAMbeByToZgEGW_GeuL9BPFq_HT5ZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه اراجیف
پزشکیان
در سازمان ملل:
پزشکیان با اشاره به جنگ ایران و آمریکا و اسرائیل، حملات به ایران را محکوم کرد و گفت
ایران قربانی تروریسم و تجاوز شده است
؛ او در اقدامی قابل‌توجه
تصویر علی خامنه‌ای
را در مجمع عمومی بالا برد و گفت رهبر ایران بدون دلیل ترور شده است. پزشکیان همچنین تصاویر
کودکان و دانش‌آموزان کشته‌شده در حمله به مدرسه میناب
را نشان داد و حمله به غیرنظامیان و کودکان غزه را محکوم کرد  و گفت صلح پایدار در غرب آسیا بدون عدالت برای فلسطین غیرممکن است. او درباره برنامه هسته‌ای گفت
ایران به دنبال ساخت سلاح هسته‌ای نیست
و انرژی هسته‌ای صلح‌آمیز را حق ایران دانست، اما هم‌زمان به وجود زرادخانه هسته‌ای اسرائیل اعتراض کرد. او آمریکا و اسرائیل را عامل حملات و تشدید بحران منطقه معرفی کرد، از عملکرد سازمان ملل و شورای امنیت انتقاد کرد و گفت ایران در برابر تهدید و فشار تسلیم نخواهد شد. او همچنین قدرت نظامی ایران را
دفاعی
توصیف کرد و درباره تنگه هرمز بر مواضع ایران تأکید کرد. در عین حال، گفت
ایران راه مذاکره و دیپلماسی را کاملاً نبسته است
و در صورت احترام به حاکمیت و حقوق ایران، امکان رسیدن به راه‌حل سیاسی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23914" target="_blank">📅 18:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23913" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23912" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23911" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba6328511d.mp4?token=Mre_WmnXshh9JGh8EC99AZNBXJJA9B66nRs0GfnISjykENgfFr_MChhSlha6EjvE2BSCnrXWtrZtc8OJNa5-eYE23dkCvwhHsVtJjg12hfS1qQcFQYhdGswCNSLc2Tt8KxPr_-kIO4KyyXeg6mupBdaYKytK10Xt2rfGoqjVNjsLW_m7hIz7ZHhlk01TWQ46yhSLosC-NmB11VHbp3yrP7shZmT7IcdzmnmvFg2uL23M93LlEhPBtP8dItKCiLTRs_gbmXA267utXghPuDd21HaZVHoRHehC2rjjji6OXKKTkIkACMEpaPLrRAvgebvsQCidKLSMmPOf-z5pzFUOgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba6328511d.mp4?token=Mre_WmnXshh9JGh8EC99AZNBXJJA9B66nRs0GfnISjykENgfFr_MChhSlha6EjvE2BSCnrXWtrZtc8OJNa5-eYE23dkCvwhHsVtJjg12hfS1qQcFQYhdGswCNSLc2Tt8KxPr_-kIO4KyyXeg6mupBdaYKytK10Xt2rfGoqjVNjsLW_m7hIz7ZHhlk01TWQ46yhSLosC-NmB11VHbp3yrP7shZmT7IcdzmnmvFg2uL23M93LlEhPBtP8dItKCiLTRs_gbmXA267utXghPuDd21HaZVHoRHehC2rjjji6OXKKTkIkACMEpaPLrRAvgebvsQCidKLSMmPOf-z5pzFUOgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده آمریکا در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخن می‌گفت، مجمع را ترک کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23910" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مارکت دار قرمز میشه
⚠️
@WarRoom
🔻</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23908" target="_blank">📅 17:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB-CJgVWHodQijeKApbT1TiukkTIVZy1BOwebNlOmCgxgkkBJQxtCm1nvJMYVi0eSdv-Atm1CA0cg11ru43729m6vKtoHxKY-UhrVniwcgn2bAEPEHEvDZH0-oZbvYb8PRYcPPdb1Twb-Ob_w76BRiin_Nlbfgf1Gbh_e4RVb30n1zoOBU1QqXoWRg7sOr261BxTmkuBWNnJtXgwRi0ay1MBe39_V0YkxAAZRk2hXidBI3QvZQlSeD2hHZyl0VxlVq8awBDrWRPgz9_k8heDh_IoVUsuj-rZEOimSEf3U4kjyQrPN38HSJ_LjZG5QTEqPZLqPCnNcGwE1ZcCw2Ue5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا: یک کشتی باری در تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت که منجر به زخمی شدن دو نفر در کشتی شد. خدمه تخلیه شده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23907" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پزشکیان چرک هم اکنون وارد سازمان ملل شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23906" target="_blank">📅 17:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">غوغای دانیال ایوازی از بازماندگان سرکوب اعتراضات ایران دیروز ۳۱ شهریور ۱۴۰۵ در مجمع عمومی سازمان ملل در نیویورک، وی در اعتراضات ایران هنگام تلاش برای کمک به یک معترض، هدف گلوله نیروهای جمهوری اسلامی قرار گرفته و زخمی شده بود. سخنان کوبنده  او علیه جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23905" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274a2e46ed.mp4?token=dJAio0kKYOSUpQ8yE0mkfTsW43A7zEfqchEDn4BPCxug6GtDtLky_KginBXG-16_2iaX3skypMdBlYWsO3pI4lx6OVjJ5x_v2QRWqIJ6FmdlvgYSk0uKI_yoJp3BJH3VX7rGUWj_vZv0DBuXLayIY5JR_op3JWo2V_gE2JLoaJy5xcysyNlRecOZocsDt4uIfyAA1HY2g1oSCeecfVJU51NXexwxnDbQSOzsaMh8RGCecvEyrGmiissZAJAaz9FcQjQMtXdLvVteviIEBLGmaH_z_WEilD_tftCdd9UEj8NSQnn5xEv2TWGXsFd9V1GdxSm_m2zNjm1o95beqf6N1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274a2e46ed.mp4?token=dJAio0kKYOSUpQ8yE0mkfTsW43A7zEfqchEDn4BPCxug6GtDtLky_KginBXG-16_2iaX3skypMdBlYWsO3pI4lx6OVjJ5x_v2QRWqIJ6FmdlvgYSk0uKI_yoJp3BJH3VX7rGUWj_vZv0DBuXLayIY5JR_op3JWo2V_gE2JLoaJy5xcysyNlRecOZocsDt4uIfyAA1HY2g1oSCeecfVJU51NXexwxnDbQSOzsaMh8RGCecvEyrGmiissZAJAaz9FcQjQMtXdLvVteviIEBLGmaH_z_WEilD_tftCdd9UEj8NSQnn5xEv2TWGXsFd9V1GdxSm_m2zNjm1o95beqf6N1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری شدید نیروهای مزدور رژیم با گروهای مسلح در سراوان همین الان !
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23904" target="_blank">📅 16:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvWMBcXb2HGFfHS1SsRHdWccA_enXDTTLN1PgHIiqFyzo70XY7zLf7H8icyojnoIaib9FC6lIKahr50VFyzdO7IHXw75Le9EPAuuK_9muV1ZnyvYNE1VRxFSJkt6pUxxTJJRizK48CEIe0CtYAvcgnNpUtaGfdj4rnAhqDa_oVRxmLFkomHkeTxfO8beUOX6k_pUW1Vm8YjrFMQY2yiEnDwoJwOJy2plywf51JTV1ZGDURMFx4Q-NbITMNZNkF3wxRdPTWKoT_oqzkNcBYq6vFygsPwm5p7NcNrZ9i6urrrzSKgsI3RHZs1uCHsw8iUD5LsjzHHf_HwTW9Pn1UBcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج نفتکش غول‌پیکر (VLCC) حامل نفت خام، بامداد دیروز در حالی مشاهده شدند که مسیر شرقی خود را از تنگه هرمز به پایان می‌رساندند. این نفتکش‌ها در مختصات ۲۵.۹۵۸۰، ۵۶.۵۵۸۱ ثبت شده‌اند. این مسیر راحت و بدون خطر نبوده و کشتی‌ها در شرایطی خطرناک و زیر آتش از تنگه عبور کرده‌اند. همچنین آثار باریک و کشیده‌ای از سوخت در دریا اطراف یکی از کشتی‌هایی که مورد اصابت ایران قرار گرفته، مشاهده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23903" target="_blank">📅 16:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری فارس:عراقچی اجازه دیدار با ویتکاف را نداشت و باید عذرخواهی کند.
گویا چپقچی مجوز شعام رو نداشته ، حالا هی سپاه موشک میزنه نفت بره بالا  این میره مذاکرات قیمت رو میاره پایین
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23902" target="_blank">📅 16:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOhJGbij147rY04ge1pn5nyRcM476FGl9KbIOTNZY36QYVsp-HhQ-xdRcSwbnmf2jplem_2kko01qHZf87KxQ-bixQ3axk7IF2dG9BF2eWIcqABs30OQ0pvR1_tU-hdHwWWVIkt9-6x2_C43LZo1TwWOcKEjTcGUCi4_aCs3Dwtnw88Nb9mhSCIvVJN1QRkPvVP8iz8f936jpj2J3Z0tiSwjAinJtcVlEO2rp-U5l21P067miRnCLM8J4a04VsTjRzUYk79SuBqfoF5hJZYH-ou7bNHHUSrz_ggrnF6mrloaZwUx4GqOtGS7SqY4WFSyR3I5P23mHg4ffmYWn9DIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا:
یک کشتی باری در تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت که منجر به زخمی شدن دو نفر در کشتی شد. خدمه تخلیه شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23901" target="_blank">📅 15:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پنتاگون، پایگاه داده مربوط به سربازان کشته شده خود را به‌روزرسانی کرد ، این لیست نشان میدهد که یک سرباز زن آمریکایی در عربستان سعودی بر اثر "یک حادثه پزشکی" جان خود را از دست داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23900" target="_blank">📅 15:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003e77a4ac.mp4?token=DLFRv2Hv3dS7dOGgYgK2tg5p8RTUwoQruZ6KUQXkPF_39IKD8p2ljME9Pa3O0LjAmxPbxhDvzePqXq3zRYefyO1E5qPH8Y6Db5_Wht_MNc9QTiisM1hE4OURBixlgpeabvH2Ic10VtXvmMHDY-IcgRvuPk8B_aJhML9up1nr-tNrRwwzZ3nC9EQnp5lH3wNkYrU6vIVnQvFJrB-X1emAYnIuRv5WhycLiGj-vikL6htiAVLfi4OrRzV1XTJorjq6Vb-v0uoj-MMlO9if7Uwc7mEmuexifRrremYDc3zo8ecwqWWDQB8lsMKL1K223btXmBugZl8J_7gUulVOK2JJyai1i7-wjgW1pR1yrHsajBXoR6AwJs0vb6G9N8Y_R7hMSapkMJBax8pEbepsedH20fgC4B0_LBnLWMtAWS7RikQJMztIDBPYB0zPHK7_oKkDPtOhbIya_kO4HBS6n1JzSVRXUAOwwtJ_2B3TtRc0zmEEWjH0VaYPFnPabkrBtyMAvfmn0fGy2UXKBmrsmTa4sR7-JjrXdUk6N9n7piJ944l2upOjdsBOWcuGUAnxN6LC4HH4J4d1TlEnIiH5BN2WAHZ9bHBdNJ_NDFg5gH77fPmijn1YwrxA-N1lmAA6B1susN9VUwbELKuVm7BrseQ8uXo3VRGuJDI0Y-06PVVRFHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003e77a4ac.mp4?token=DLFRv2Hv3dS7dOGgYgK2tg5p8RTUwoQruZ6KUQXkPF_39IKD8p2ljME9Pa3O0LjAmxPbxhDvzePqXq3zRYefyO1E5qPH8Y6Db5_Wht_MNc9QTiisM1hE4OURBixlgpeabvH2Ic10VtXvmMHDY-IcgRvuPk8B_aJhML9up1nr-tNrRwwzZ3nC9EQnp5lH3wNkYrU6vIVnQvFJrB-X1emAYnIuRv5WhycLiGj-vikL6htiAVLfi4OrRzV1XTJorjq6Vb-v0uoj-MMlO9if7Uwc7mEmuexifRrremYDc3zo8ecwqWWDQB8lsMKL1K223btXmBugZl8J_7gUulVOK2JJyai1i7-wjgW1pR1yrHsajBXoR6AwJs0vb6G9N8Y_R7hMSapkMJBax8pEbepsedH20fgC4B0_LBnLWMtAWS7RikQJMztIDBPYB0zPHK7_oKkDPtOhbIya_kO4HBS6n1JzSVRXUAOwwtJ_2B3TtRc0zmEEWjH0VaYPFnPabkrBtyMAvfmn0fGy2UXKBmrsmTa4sR7-JjrXdUk6N9n7piJ944l2upOjdsBOWcuGUAnxN6LC4HH4J4d1TlEnIiH5BN2WAHZ9bHBdNJ_NDFg5gH77fPmijn1YwrxA-N1lmAA6B1susN9VUwbELKuVm7BrseQ8uXo3VRGuJDI0Y-06PVVRFHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک کارنی، نخست‌وزیر کانادا، درباره ایران:
«
تهدید ایران
یکی از بزرگ‌ترین تهدیدها در جهان و در دنیای مدرن است. برای مثال، همچنان
تهدیدی موجودیتی علیه اسرائیل
از سوی ایران و متحدانش وجود دارد. این تهدید همچنان وجود دارد؛
قابل قبول نیست و هیچ‌گاه قابل قبول نبوده است.
»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23899" target="_blank">📅 15:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69c03421a.mp4?token=DhnNCN4cV5TPtRaKtsbSq5QL_4eo1O3dCjjCS61ErEMV83Cw2LieaBGprfqjnFgkkLGYGRT_lqfHbw24A6GiRaK9hg4I8FqcnRLChxK0QXj5msHPgy3u8n7smhyU5CVGZ_XkSG8oZSNNZr3hEWCTYdVTuleWZ9xZdx_-KU3CmR72NCpNHbridb4JPQPjp1r7dsJyezsk_4ku-zIdR1YfeN1TZS-WcMrAvVjZGaoh3r8LqdypRB-hMwP80YMALXqW91Bk_XwN28T3Vl7WIS-8NsEjXRZOvL7IyDEJzK2WXP37MP37IWUOcfVVJOsskTCxwVvCTuUIoVDbNhLyeOCd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69c03421a.mp4?token=DhnNCN4cV5TPtRaKtsbSq5QL_4eo1O3dCjjCS61ErEMV83Cw2LieaBGprfqjnFgkkLGYGRT_lqfHbw24A6GiRaK9hg4I8FqcnRLChxK0QXj5msHPgy3u8n7smhyU5CVGZ_XkSG8oZSNNZr3hEWCTYdVTuleWZ9xZdx_-KU3CmR72NCpNHbridb4JPQPjp1r7dsJyezsk_4ku-zIdR1YfeN1TZS-WcMrAvVjZGaoh3r8LqdypRB-hMwP80YMALXqW91Bk_XwN28T3Vl7WIS-8NsEjXRZOvL7IyDEJzK2WXP37MP37IWUOcfVVJOsskTCxwVvCTuUIoVDbNhLyeOCd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
«آیا فکر می‌کنید ترامپ با بیان اینکه در حال بررسی گزینه
نابودی کامل ایران
است، زیاده‌روی می‌کند؟ آیا چنین اظهاراتی به روند صلح کمک می‌کند؟»
مارک کارنی:
«اکنون جنگ در جریان است. او با
زبان جنگ
صحبت می‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23898" target="_blank">📅 15:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">غوغای دانیال ایوازی
از بازماندگان سرکوب اعتراضات ایران دیروز ۳۱ شهریور ۱۴۰۵ در مجمع عمومی سازمان ملل در نیویورک، وی در اعتراضات ایران هنگام تلاش برای کمک به یک معترض، هدف گلوله نیروهای جمهوری اسلامی قرار گرفته و زخمی شده بود. سخنان کوبنده  او علیه جمهوری اسلامی و در حمایت از مردم ایران با اعتراض شدید هیئت جمهوری اسلامی روبه‌رو شد، اما اعتراض آنها پذیرفته نشد و
رئیس جلسه اجازه داد ایوازی به صحبت‌های خود ادامه دهد.
این حضور با حمایت
دیده‌بان سازمان ملل (UN Watch)
انجام شد و
هیلل نوئر، مدیر اجرایی این سازمان،
ویدئوی شهادت ایوازی را منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23897" target="_blank">📅 14:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس کنکوردیا:
من معتقدم ایران آینده باید یک کشور سکولار و دموکراتیک(حکومت مردمی، مبتنی بر رأی مردم و جدایی دین از حکومت) باشد؛ کشوری که در آن حقوق برابر برای همه وجود داشته باشد و ایران با همسایگان خود در صلح باشد و با آمریکا و سایر کشورهای دموکراتیک روابط دوستانه داشته باشد.
تغییر در نهایت از سوی مردم ایران اتفاق خواهد افتاد
. نقش جامعه بین‌المللی این است که به مردم ایران کمک کند تا بتوانند این تغییر را انجام دهند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23896" target="_blank">📅 14:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اورشلیم پست:
ایران اعلام کرده حدود
۵۰ درصد ظرفیت تولید آسیب‌دیده میدان گازی پارس جنوبی
بازسازی شده است. این گزارش به نقل از رویترز منتشر شده و مقام‌های ایرانی درباره روند بازگشت تولید توضیح داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23895" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ژاپن‌تایمز:
حوثی‌ها,  عربستان را به انجام حملات هوایی مرگبار متهم کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23894" target="_blank">📅 14:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آسوشیتدپرس:
گزارش تازه‌ای درباره پیشروی سریع حوثی‌ها در سواحل دریای سرخ منتشر کرده و به نقل از منابع خود نوشته است که
مشاوران ایرانی در خطوط مقدم
به حوثی‌ها در این عملیات کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23893" target="_blank">📅 14:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فایننشال تایمز: هزینه اجاره نفتکش‌های غول‌پیکر در مسیر خاورمیانه به آسیا برای نخستین‌بار از
۱.۲ میلیون دلار در روز
عبور کرده و به رکورد تاریخی رسیده است. به گفته شرکت کشتیرانی کلارکسونز، حدود
۱۵ درصد از کل ناوگان نفتکش‌های جهان
اکنون در نزدیکی سواحل عمان منتظر بارگیری یا انتقال محموله هستند. افزایش زمان سفر، کمبود نفتکش و اختلال در تردد از تنگه هرمز از عوامل اصلی جهش بی‌سابقه هزینه حمل نفت عنوان شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23892" target="_blank">📅 14:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه کانال خبری فقط خبر درست و غلطشو  می‌زاره داداش جناحشو اعلام نمیکنه و دشمنی شو جار نمیزنه</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23891" target="_blank">📅 13:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMorteza</strong></div>
<div class="tg-text">یه کانال خبری فقط خبر درست و غلطشو  می‌زاره داداش جناحشو اعلام نمیکنه و دشمنی شو جار نمیزنه</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23890" target="_blank">📅 13:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5523a29a.mp4?token=iWgv76PTl3VYq4wMNfPyPisBjau5As0vlc0tB29bMU_cOeDHlMsgP8sA8bigsacMD-xpo0IGFR9TNSqyCzOpLB4UzesjXgo0tYe26uOyA61QziuBd3zi57XptZBa-K_AA8BUTkUE70YKDroXkLdNXapmXZiO3IWIW2o1_kHs2okPNHnl9OL3BBlcuSb-huSVwfmiGvoD_nzecbnEnCRTjk4CxjkQwV11zziEyyKzF96fdWD0jjqyhkjoMEfRxFIP3k8UQdHshJxhcoasDS9vNmaG6PUPqijMshDjRQ0e2L7HEgzzqQ8FLuYqrq_8GPM4MLBXZNzKrtKJQu8R0SZTuAU8JPzkFZDvGg5SdhdQYkvNWFrG37UkFLRazS6VdPBloj3QP-KpkDX1mxrCn5UHTQWDIVwCes9OPhYSU0b0nYItEizY5GY-ORpaHxsMoQTIf3dPo8xyax2mBdGzJe3ZwfVRVP_1FJlmxWVQHL7AH7Kwq_UCWz_6FGW5Q5LVrKyvkLaWM2Ri3VHkyT1Vd6dih6xeA9Dy6fOM8x9DjXe7oCQSzliOgqVRT8SmdNhLPHYWrm04VWcMPGmfQ6WOUesFNMzLsvazjUVcf_EkB6CGLacok_WRyw2TRdTYcp9GJSr1-tOtiAYE1TNvrJzek9waQiW9KPVUjjDDXVJ0GrhaqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5523a29a.mp4?token=iWgv76PTl3VYq4wMNfPyPisBjau5As0vlc0tB29bMU_cOeDHlMsgP8sA8bigsacMD-xpo0IGFR9TNSqyCzOpLB4UzesjXgo0tYe26uOyA61QziuBd3zi57XptZBa-K_AA8BUTkUE70YKDroXkLdNXapmXZiO3IWIW2o1_kHs2okPNHnl9OL3BBlcuSb-huSVwfmiGvoD_nzecbnEnCRTjk4CxjkQwV11zziEyyKzF96fdWD0jjqyhkjoMEfRxFIP3k8UQdHshJxhcoasDS9vNmaG6PUPqijMshDjRQ0e2L7HEgzzqQ8FLuYqrq_8GPM4MLBXZNzKrtKJQu8R0SZTuAU8JPzkFZDvGg5SdhdQYkvNWFrG37UkFLRazS6VdPBloj3QP-KpkDX1mxrCn5UHTQWDIVwCes9OPhYSU0b0nYItEizY5GY-ORpaHxsMoQTIf3dPo8xyax2mBdGzJe3ZwfVRVP_1FJlmxWVQHL7AH7Kwq_UCWz_6FGW5Q5LVrKyvkLaWM2Ri3VHkyT1Vd6dih6xeA9Dy6fOM8x9DjXe7oCQSzliOgqVRT8SmdNhLPHYWrm04VWcMPGmfQ6WOUesFNMzLsvazjUVcf_EkB6CGLacok_WRyw2TRdTYcp9GJSr1-tOtiAYE1TNvrJzek9waQiW9KPVUjjDDXVJ0GrhaqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت یه کلاس درس تو سیستان و بلوچستان امروز  @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23889" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGqiOOkW2_ci7gPgoavGwGgBFvrm2lcDU68c3QY9GEcByY82iwrt5Sq03zQz-_ZbiTEXRXx13F7AEzuktjFxHjKYvFM00VQM-sB-CK2GXA_okuHWWMLsFMpJv_67beA6u8O0j8tMSDeP7Q9YQR12kAS0jle94RHP4bNXMMdKgN8aKMQeITge7fUK9AqtB05kY7iKaor53fHrKcl3x3EqRCB4-kEsKYScUy7uIJUxGGYGPPNJac3jKBmSZe1cyw1aqLDwoanf1rEnYt_vUCXbREWULRwy2PCyXNyvj98OVLUvmflqE1yjHXI0E_6JXpLmrIdH_3YkUVHHB5lBFiiykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت یه کلاس درس تو سیستان و بلوچستان امروز
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23888" target="_blank">📅 13:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پزشکیان فرا رسیدن روز ملی عربستان را تبریک گفت
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23887" target="_blank">📅 12:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کرملین:
«
ولادیمیر پوتین
آماده دیدار با
دونالد ترامپ
است، اما برگزاری یک
نشست بدون انجام هماهنگی و آماده‌سازی‌های قبلی
، اتلاف وقت خواهد بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23886" target="_blank">📅 12:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس: کمیته موسوم به «کمیته صلح ترامپ» از طرح بازسازی نوار غزه به ارزش ۲.۴۵ میلیارد دلار پرده برداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23885" target="_blank">📅 12:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_se-nkbG3MgpzHci2NRe93pbAS2xYiNGGamBXViCNfy22pK77gLuoafBDZfiOdQMNh3zS5aVmDhpZt6waKWO6LYtK075RrlUwp2J-WEkaN3ti3KPmjJkYJyIpI6cUkN5sbCtzVPSURBUuh-Nrz_Rx9h31iFI98QZb7zuZH4y7jb9KBWdJYqrs5LsrOwyjhBjN7vVQaBkrEhi6r1F8AGqlAnbwxM-_NmjgVt9Kvp2SNprb9ONC1ElTnOR7laizuDz3RCxz3DOFGyHW1kS0eH6mPiatE8e9J2bipMRM54yprlY1CzuqtOkJC5Dq2uIXLRCLAUnCkHyGmAfHfQBJmFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : تحرکات زیاد شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23884" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOSs9LEL7dGzL1qxzpBD86kgZRCMvyLDrdtk2XsuDyKd3iCRGvaJVDA4CzqAOVIdD9_bxPU8kSfis5NkrhlNC_P_jQTmwbGPgrCrIyZLTF2Yo39ibi_j_c2jcA8PStJ_4uX5q-WLhL-m2j__mQafBDEvmvePQA-vZbDi0PMg_4fI-tn436Lays9a5OFqMwGxc6xoQ5hKeSY8hke7_nHBi_-KuL9qI8EbK8uy7MM15oi-RV1F8pSV1mTFRxceXkGAhJsnneI-DFuKwEfdol0MiOB7PcTdTTE6-lDACLjGVbjONEMYWPBEBusct6sxFXoVIH2VTn3TH3jDgccAc49YSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خبر نیوزمکس: ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23883" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری فرانسه: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد.
@WarRoom
یجور میگه چین فرود اومد انگار شاخ به شاخ زده به ساختمان پنتاگن</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23882" target="_blank">📅 12:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آخوند زنجانی ریقش در رفته  و امروز دولت عزای عمومی اعلام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23881" target="_blank">📅 12:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تنگه صدای فرماندهان پیشین قرارگاه خاتم میاد @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23880" target="_blank">📅 11:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تنگه صدای فرماندهان پیشین قرارگاه خاتم میاد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23879" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروهای دولتی یمن: ما به سلاح‌ها و تجهیزات گروه حوثی در جبهه کهبوب حمله کردیم، که این امر منجر به تلفات در صفوف آن‌ها شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23877" target="_blank">📅 11:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نشریه آمریکایی نیویورکر
فاش کرد که طی یک مکالمه محرمانه میان جرد کوشنر داماد ترامپ و محمد بن سلمان ولی‌عهد عربستان نقشه وی برای کنار زدن
محمد بن نایف، پسر عمویش، از ولایت‌عهدی در سال ۲۰۱۷
بررسی شد. در این گزارش به نقل از یک مسئول اطلاعاتی سابق در منطقه آمده است که کوشنر به بن سلمان ابلاغ کرده
همه در دولت آمریکا به جز سرویس‌های اطلاعاتی از وی حمایت می‌کنند.
این پیام به مثابه
چراغ سبز واشنگتن خطاب به بن سلمان برای اقدام علیه محمد بن نایف
تلقی می‌شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23876" target="_blank">📅 11:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش‌صدای انفجار در قشم @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23875" target="_blank">📅 10:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دونالد ترامپ پس از پایان سفرش در نیویورک برای شرکت در مجمع عمومی سازمان ملل، بامداد امروز با «مارین وان» به کاخ سفید بازگشت. رویترز زمان فرود او در چمن جنوبی کاخ سفید را
ساعت ۸:۴۱ صبح به وقت تهران
ثبت کرده است.
طبق برنامه عمومی کاخ سفید، ساعت
۱۱:۰۰ صبح به وقت واشنگتن ساعت ۱۸:۳۰ به وقت تهران
یک
جلسه سیاست‌گذاری
در کاخ سفید دارد.
و طبق برنامه رسمی، شی امروز وارد آمریکا می‌شود و ترامپ در
پایگاه هوایی اندروز
از او و همسرش استقبال می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23874" target="_blank">📅 10:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مستندی برگرفته از اسناد محرمانه ی ایالات متحده درباره ی رخدادهای شب بیست و ششم شهریور سال ۱۳۵۵.  به همراه مکالمات رادیویی واقعی از گفتگوی خلبان های نیروی هوایی ارتش ایران با برج مراقبت و مرکز فرماندهی.ماجرا از این قرار است که شبی آرام در اواخر شهریور ماه حوالی…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23873" target="_blank">📅 10:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8175c0276e.mp4?token=phdon1655OuaxKLZ_cq7dseeHijuwgVqoaMGt8T1pHHGC-vwY9dJxhCxgTYZ5FK4hWg6TeYnathu-xGanK8fkWzIRdcmGSIaQHLmVX-Fy8XxjGs-ImxGe5S2cBOnkWpzIJ56KJIsVttMMIFkn3rAHTfk1j-Upaa8mxchvpZQd3fVabnPVJQuCcRC8obsEY0nHRTIEmqy76O5VOP6oAoj7C7IjghvLSxxJ7KH86EPPwvcGLFq-txoMzKF379OO8S91HovKefIcDlir1iKUZaBvc8Dl0o-iIl9at8V7P89-ZWrD2FcmRjHI05lKBRupdGQBWA2Bl13GtFAy6IzGpQ9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8175c0276e.mp4?token=phdon1655OuaxKLZ_cq7dseeHijuwgVqoaMGt8T1pHHGC-vwY9dJxhCxgTYZ5FK4hWg6TeYnathu-xGanK8fkWzIRdcmGSIaQHLmVX-Fy8XxjGs-ImxGe5S2cBOnkWpzIJ56KJIsVttMMIFkn3rAHTfk1j-Upaa8mxchvpZQd3fVabnPVJQuCcRC8obsEY0nHRTIEmqy76O5VOP6oAoj7C7IjghvLSxxJ7KH86EPPwvcGLFq-txoMzKF379OO8S91HovKefIcDlir1iKUZaBvc8Dl0o-iIl9at8V7P89-ZWrD2FcmRjHI05lKBRupdGQBWA2Bl13GtFAy6IzGpQ9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : همین الان (ساعت: ۰۹:۲۷) شیراز، تحرکات سنگین نظامی
یاشار : هواپیمای هرکولس سی ۱۳۰ جمهوری اسلامی که در زمان جنگ در پاکستان مخفی شده بود با چنگال تیز دیدبان اتاق جنگ شکار شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23872" target="_blank">📅 10:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاهزاده رضا پهلوی : مردم ⁧ ایران ⁩ را با منابع مالی بلوکه شده مسلح کنید . (ویدیو کامل مصاحبه حدود ۱۱ دقیقه) @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23871" target="_blank">📅 09:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاهزاده رضا پهلوی : مردم ⁧ ایران ⁩ را با منابع مالی بلوکه شده مسلح کنید .
(ویدیو کامل مصاحبه حدود ۱۱ دقیقه)
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23870" target="_blank">📅 09:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef7b629ee.mp4?token=l9-EP2dJN3Sz6vB981eR0H01CSliI_C0wV_yvACqINTKyrfo29MjKu2Ms8EZwrfYMcq1C3r3HD57djHTbLg2kwTrIb9VQcqrsaQN00rfyp828j1KmzTO-pupzUBuFioSfX3E0M85Am5pbfTKlkN0bqDvur3qUWPfdNre4ZJMt3DhWJ8_TyL4a4Obv23aNY7s0lrdKL738Y9ho1rh6NCLQRrdGhgQw-ZgL8FTGbSX9v3QD0NBDGktWcAij9YwX-xyfQmRGFNmyMHP9InmxGEHkf1-ckDy967QySuUkVqHcRtHUOlE4xHFU8b9At0zuwSAijzOlLbpON_3rIA86uOKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef7b629ee.mp4?token=l9-EP2dJN3Sz6vB981eR0H01CSliI_C0wV_yvACqINTKyrfo29MjKu2Ms8EZwrfYMcq1C3r3HD57djHTbLg2kwTrIb9VQcqrsaQN00rfyp828j1KmzTO-pupzUBuFioSfX3E0M85Am5pbfTKlkN0bqDvur3qUWPfdNre4ZJMt3DhWJ8_TyL4a4Obv23aNY7s0lrdKL738Y9ho1rh6NCLQRrdGhgQw-ZgL8FTGbSX9v3QD0NBDGktWcAij9YwX-xyfQmRGFNmyMHP9InmxGEHkf1-ckDy967QySuUkVqHcRtHUOlE4xHFU8b9At0zuwSAijzOlLbpON_3rIA86uOKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون، رئیس‌جمهور فرانسه، درباره ایران:
«این درست است که ما در این جنگ حضور نداشتیم؛ نه به این دلیل که با آمریکا همراه نیستیم. ما برای آمریکا احترام قائلیم و فکر می‌کنم متحدان خوبی هستیم. اما وقتی می‌خواهید وارد درگیری شوید، باید با متحدان خود درباره راهبرد هماهنگ کنید و پیش از آغاز جنگ از آنها نظر بخواهید. ما تصمیم گرفتیم به این جنگ نپیوندیم، چون معتقد بودیم ــ و من همچنان معتقدم ــ این گزینه درستی نبود.»
«فکر می‌کنم پس از آغاز جنگ در اواخر فوریه، اهمیت تنگه هرمز احتمالاً دست‌کم گرفته شد و امروز باید این مسئله را حل کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23869" target="_blank">📅 09:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de2b4f18b.mp4?token=IOqOKvEM0aEN6CCC15xJbJfmt75xkzztXQbZlnzWp98mPv05Y0vMXvQ_FoLB0-aCCqiBKJnNwiJnD-aFREXyH6ZifFHZJYRAxHDpvpXXIuqSVMmxF_vlisl8KNVAw421TExoXOXWE7dG5csdPV-BUrZwzhtOUU92O7toZ5CSgAVdxat9a3ihdw5v_YPX-6vUcUH5Pjb-Fg_I_LRWDQ-woaeCK5iPl9jYBBUXYHSIUkrl2TX56xVq1SSztOrX-Ld6OxXzA-o-Gw5clx6shCn2Vj5AMgXR9oyLFGC3pdnZi6KT_3ljcK-R3I3dyO64Q4bZVf1yrMu303NiK-uPG3h4qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de2b4f18b.mp4?token=IOqOKvEM0aEN6CCC15xJbJfmt75xkzztXQbZlnzWp98mPv05Y0vMXvQ_FoLB0-aCCqiBKJnNwiJnD-aFREXyH6ZifFHZJYRAxHDpvpXXIuqSVMmxF_vlisl8KNVAw421TExoXOXWE7dG5csdPV-BUrZwzhtOUU92O7toZ5CSgAVdxat9a3ihdw5v_YPX-6vUcUH5Pjb-Fg_I_LRWDQ-woaeCK5iPl9jYBBUXYHSIUkrl2TX56xVq1SSztOrX-Ld6OxXzA-o-Gw5clx6shCn2Vj5AMgXR9oyLFGC3pdnZi6KT_3ljcK-R3I3dyO64Q4bZVf1yrMu303NiK-uPG3h4qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون، رئیس‌جمهور فرانسه، درباره ایران:
«اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، برای همه ما بسیار مهم است. بنابراین، برای من این هدف اصلی است. تغییر یک حکومت از طریق بمباران یک کشور، چیزی نیست که آن را عملی بدانم و از نظر من گزینه خوبی هم نیست، چون نتیجه نمی‌دهد و ما در دهه‌های گذشته چندین بار این اشتباه را تکرار کرده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23868" target="_blank">📅 09:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=Yi5zOP_mteVMGJgkjpipll3QxFFOvnm6piTrgia1-ssC6-BvfXovcHWz1xTM-od0kn4a-OL5szBtIbwe-KWeK_Xb_SXSgQB0VZZwJvGd0hausBE3a3Vf_R0Sn_shueLYe-dXtX_bP6QBDYsR1U3YYY3jwBtbD5Z0RC6Y_scTeUO3kH_GCRz45MR7L0xc0TgqICeWd8WQ0_sI8u3dAj1rfVcsG55dAmVoq0brw1s084cmHnoq0GiCaq01noASDoA2bkxWKUgxl450Q1Axbk_t9vrqdBKtJ2KGEgPp15FYtfYYBoA5KWxsFCauTG_2hJS-Lp3KfrSmGOux-NMR24chbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=Yi5zOP_mteVMGJgkjpipll3QxFFOvnm6piTrgia1-ssC6-BvfXovcHWz1xTM-od0kn4a-OL5szBtIbwe-KWeK_Xb_SXSgQB0VZZwJvGd0hausBE3a3Vf_R0Sn_shueLYe-dXtX_bP6QBDYsR1U3YYY3jwBtbD5Z0RC6Y_scTeUO3kH_GCRz45MR7L0xc0TgqICeWd8WQ0_sI8u3dAj1rfVcsG55dAmVoq0brw1s084cmHnoq0GiCaq01noASDoA2bkxWKUgxl450Q1Axbk_t9vrqdBKtJ2KGEgPp15FYtfYYBoA5KWxsFCauTG_2hJS-Lp3KfrSmGOux-NMR24chbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: «اگر آنها حاضر باشند مردم خودشان را قتل‌عام کنند، فکر می‌کنید با ما چه خواهند کرد؟ با اسرائیل چه خواهند کرد؟ یا با همسایگان سنی خود؟»
روبیو افزود: «همه بر این باورند که ایران نباید سلاح هسته‌ای داشته باشد. تنها چیزی که تغییر کرده این است که ما رئیس‌جمهوری داریم که حاضر است در این زمینه اقدام کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23867" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=EVrZId4ayXkJzLmCOJPgvsqB85omSn2aPOXBcKpwzazWyY5W_-U0gF-WYDDVC7IJtp9GKWw4_omKcC2weCu9w3x8ZLvg0taHqIQ6MHL8YSPXqCD7f9LCetXjyyq6QcaF_nhF3LUhz_M2Cstv9rfu04_3sbqgvtFuxpfwaJ8IiAX4CEY6LPv2i0UOqSTLnVYfefRktlpBH9PB1zc4qhToKFPp23mvLuRtS-yze9n3oqhqZ4s8fql88Kdeb8A1-E8iuWxInCWNrh0JsApCU0qKub224Mj8BJtyGlLvQ87EA9YdUdWw2pSW1qaFO0vIhfQ4FRtZSb3v8jFGAi6fr00PKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=EVrZId4ayXkJzLmCOJPgvsqB85omSn2aPOXBcKpwzazWyY5W_-U0gF-WYDDVC7IJtp9GKWw4_omKcC2weCu9w3x8ZLvg0taHqIQ6MHL8YSPXqCD7f9LCetXjyyq6QcaF_nhF3LUhz_M2Cstv9rfu04_3sbqgvtFuxpfwaJ8IiAX4CEY6LPv2i0UOqSTLnVYfefRktlpBH9PB1zc4qhToKFPp23mvLuRtS-yze9n3oqhqZ4s8fql88Kdeb8A1-E8iuWxInCWNrh0JsApCU0qKub224Mj8BJtyGlLvQ87EA9YdUdWw2pSW1qaFO0vIhfQ4FRtZSb3v8jFGAi6fr00PKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: ناگهان مارکسیست‌ها و اسلام‌گراها با یکدیگر متحد و همکاری کردند و دوران افراط‌گرایی و رادیکالیسم اسلامی را به وجود آوردند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23866" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=FlOIFhuwUu_jwwKczEmB-If-SdrS3umjBCqNFNHOb7Nf8p0Kqa0GASZHm1Sbn4ZCtqmbJFrfSoVvDoxkjOEMRdXNbzYUWw-8YJ_g8H71GZyRupnHFMNXAeRefhcE_vtO5OPm9w1ziMea8DlHVCRxyMQxrHvQoWnT1T1x2vHSPVUg4np8YlASlcSYO1ioOXIzjH_QQTxpjuuCfIb2v-3u8pbHI_zzCz2tQCXOwDJJsmC4BS3H44yd_ufO_8QtNVKOSSDINRdk4fcwjI6mcuXxu_TUN4m9xw2oKyH3cBr0_YabTd4Z_4dDgC83sEXzRT2QD2V1i-yFdqGQheBolRED2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=FlOIFhuwUu_jwwKczEmB-If-SdrS3umjBCqNFNHOb7Nf8p0Kqa0GASZHm1Sbn4ZCtqmbJFrfSoVvDoxkjOEMRdXNbzYUWw-8YJ_g8H71GZyRupnHFMNXAeRefhcE_vtO5OPm9w1ziMea8DlHVCRxyMQxrHvQoWnT1T1x2vHSPVUg4np8YlASlcSYO1ioOXIzjH_QQTxpjuuCfIb2v-3u8pbHI_zzCz2tQCXOwDJJsmC4BS3H44yd_ufO_8QtNVKOSSDINRdk4fcwjI6mcuXxu_TUN4m9xw2oKyH3cBr0_YabTd4Z_4dDgC83sEXzRT2QD2V1i-yFdqGQheBolRED2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: پیش از انقلاب اسلامی، هر روز پروازهایی از تل‌آویو به تهران داشتیم؛ نه اینکه مانند امروز، هر روز موشک‌هایی به سمت تل‌آویو شلیک شود.</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23865" target="_blank">📅 08:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با یاشار: اجلاس کنکوردیا یک نشست غیردولتی و غیرحزبی است که هم‌زمان با هفته مجمع عمومی سازمان ملل در نیویورک برگزار می‌شود و محل حضور مقام‌های فعلی و سابق، کارشناسان و چهره‌های سیاسی و اقتصادی است. از چهره‌های مطرح حاضر می‌توان به شاهزاده رضا پهلوی ، ژنرال دیوید پترائوس، فرمانده پیشین سنتکام و رئیس پیشین سیا، نیکول پاشینیان، نخست‌وزیر ارمنستان، لیندا توماس-گرینفیلد، سفیر پیشین آمریکا در سازمان ملل، و ترزا می، نخست‌وزیر پیشین بریتانیا، اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23864" target="_blank">📅 08:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=QNCo_oFNkrG1U3s23f9Pw1sZwoua9gbqRXyvBAp-04idCSoO-VN27SAf4TKNOafaEYY6K-CqB0QXdRl2kq5Nt_N1dH06qKkJOX5KSkUDHLYJDn3hmRlNJlpYBX0Mz42Vs4J91F1_u6ki4JoxTXJ-2PsY6gc36RD0G6_0t548iUdoV73c-O_ZCNw-O5VIPsxfZhD-hWY5avq_UVQXQA2_x23vkNgWWv1yksTLsu5p1RzfOGDIyolqFjBIe-6w8yb7f4M8VnMtqLs-p7xsV8g5didKgvD6tCtSnsfe2-1udigiauMHzrE-xg4mchA2OAK5NE60lFxl_fLel_87PDyQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=QNCo_oFNkrG1U3s23f9Pw1sZwoua9gbqRXyvBAp-04idCSoO-VN27SAf4TKNOafaEYY6K-CqB0QXdRl2kq5Nt_N1dH06qKkJOX5KSkUDHLYJDn3hmRlNJlpYBX0Mz42Vs4J91F1_u6ki4JoxTXJ-2PsY6gc36RD0G6_0t548iUdoV73c-O_ZCNw-O5VIPsxfZhD-hWY5avq_UVQXQA2_x23vkNgWWv1yksTLsu5p1RzfOGDIyolqFjBIe-6w8yb7f4M8VnMtqLs-p7xsV8g5didKgvD6tCtSnsfe2-1udigiauMHzrE-xg4mchA2OAK5NE60lFxl_fLel_87PDyQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود؛ امروز تولید ناخالص داخلی کره جنوبی پنج برابر ایران است. وضعیت اقتصاد ایران قابل دوام نیست؛ پایدار نیست و در نهایت منفجر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23863" target="_blank">📅 08:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c403db85.mp4?token=pRA_J8rh9Q6tUgxHc5GNNO7SbD9CftbRnOOUfu7Q-4V-9h3U2FT--DFyiGDz8tKmDryEX76P_w4qLsC-mkEpQ11V0-41xl0-b9trnhELw_-YbZLYNhCCRmTn7oqVRhZOmXQkNobwqCek_NM6_WL8LtiAz66DECktfULYRWijmuNStAvagBhRjVFCwtLKmAOQ9kiQ58tfonK2wXpVOufFpUG0y-OUhZTdTfHXNa2XnP3HFcZ8vbV6BPx-2sAgI2N9BPoRUfIeI_eOMHQv_i2wgqwHRwdyA9JYWjLEl9xmZ1HpSi8MW42EsQJ5jPe9yfGlmbhHg0TYvJ1t1yBGCZfNrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c403db85.mp4?token=pRA_J8rh9Q6tUgxHc5GNNO7SbD9CftbRnOOUfu7Q-4V-9h3U2FT--DFyiGDz8tKmDryEX76P_w4qLsC-mkEpQ11V0-41xl0-b9trnhELw_-YbZLYNhCCRmTn7oqVRhZOmXQkNobwqCek_NM6_WL8LtiAz66DECktfULYRWijmuNStAvagBhRjVFCwtLKmAOQ9kiQ58tfonK2wXpVOufFpUG0y-OUhZTdTfHXNa2XnP3HFcZ8vbV6BPx-2sAgI2N9BPoRUfIeI_eOMHQv_i2wgqwHRwdyA9JYWjLEl9xmZ1HpSi8MW42EsQJ5jPe9yfGlmbhHg0TYvJ1t1yBGCZfNrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که پروازهای شرکت‌های هواپیمایی ایران در پی «عملیات طرد اقتصادی» در چندین کشور لغو شده‌اند، پزشکیان، رئیس‌جمهور رژیم ایران، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شده و به‌سرعت به حومه شهر منتقل شده است.
سخنرانی او امروز حدود ساعت ۳-۴ به وقت تهران است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23862" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش‌ صدای انفجار‌ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/23861" target="_blank">📅 01:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش‌صدای انفجار در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/23860" target="_blank">📅 01:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیوی نیویورک فاکس نیوز:
میلیون‌ها ایرانی در ۳۱ استان، در پاسخ به فراخوان من، به خیابان‌ها آمدند و در حمایت از پایان این رژیم شعار دادند.
آنها از اقوام، ادیان و اقشار مختلف جامعه ایران بودند و این نشان‌دهنده وحدت در عین تنوع است. پهلوی گفت
این رژیم عامل ایجاد اختلاف و تفرقه در ایران است
و ایرانیان قرن‌ها فارغ از قومیت و مذهب در کنار یکدیگر در صلح زندگی کرده‌اند و پس از آزادی نیز می‌توانند دوباره متحد شوند. او در پایان گفت:
«انقلاب شیر و خورشید در راه است.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23859" target="_blank">📅 01:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرتاب موشک از بندر کنگ
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/23858" target="_blank">📅 00:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل در واکنش به اظهارات امانوئل مکرون اعلام کرد: «پوچی و تناقض فاحش اظهارات امانوئل مکرون تکان‌دهنده است. تنها دو روز پیش، در آستانه یوم‌کیپور، نتانل شوکرون،
شهروند فرانسوی و پدر شش فرزند
، در خودروی خود در یهودیه و سامریه توسط یک تروریست حماس کشته شد. او در آخرین لحظات زندگی‌اش به پسرش گفت فرار کند. تروریست‌های حماس تقریباً هر روز علیه یهودیان حمله انجام می‌دهند و شمار زیادی از غیرنظامیان اسرائیلی را در یهودیه و سامریه کشته‌اند. ناآگاهی،
هیچ عذری برای نادیده گرفتن خون قربانیان نیست.
»
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23857" target="_blank">📅 00:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تتر و دلار دارن میکشن پایین
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/23856" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیویورک‌پست:
جمهوری اسلامی ایران در چارچوب یک طرح وابسته به سپاه،
حداقل سن جذب نیرو را به ۱۲ سال کاهش داده است
. یک مقام سپاه در تهران اعلام کرده بود نوجوانان ۱۲ و ۱۳ ساله می‌توانند برای حضور در گشت‌های اطلاعاتی و عملیاتی ثبت‌نام کنند. گزارش‌های بی‌بی‌سی و عفو بین‌الملل نیز از حضور کودکان در ایست‌های بازرسی و مواردی از حمل سلاح توسط آنها خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23855" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ:
ما به دنبال تغییر رژیم یا جایگزین کردن حکومت ایران نیستیم؛ هدف آمریکا این است که
ایران به سلاح هسته‌ای دست پیدا نکند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/23854" target="_blank">📅 00:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فاکس‌نیوز:
دونالد ترامپ اخیراً با امضای حکمی،
مارکو روبیو، وزیر خارجه آمریکا، را به‌طور رسمی و دائمی به‌عنوان مشاور امنیت ملی کاخ سفید منصوب کرد.
روبیو از مه ۲۰۲۵ پس از برکناری مایکل والتز، به‌صورت موقت این سمت را بر عهده داشت و اکنون انتصاب او دائمی شده است. روبیو همچنان وزیر خارجه آمریکا نیز خواهد بود و همزمان مدیریت روند شورای امنیت ملی و نقش مشاور مستقیم رئیس‌جمهور در مسائل امنیتی را بر عهده خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23853" target="_blank">📅 23:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری i24news : ‏اکسپلور گردی« احمد الشرع » وسط سخنرانی اردوغان در سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23852" target="_blank">📅 23:54 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
