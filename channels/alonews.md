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
<img src="https://cdn4.telesco.pe/file/IhvyOaqUacOi1_M3f_487NVX9KJCyfcXHPI3fho1Hw93Em7lMDlKgYpBoSxp89C0m9LPi82cTTyaxXey7gY9GrWvahBtJoy8mDUBd2yx8E4_1ZtqQ3fW8rh64eC4SOcjFgPkU1eVPZnm_EGoXMkwMgokZRTEzjxWYhIclf5QLAkuSOC00Ob5t0b73fS5lKcNYrqJBwDI8jWhR63hd0ovL2yryW8CObHqhuIS4W3M9Z_TbLzgTQr-DStuA9QXQNkGxVWhMQAKw3Rmv7Hq4kff1jm3KtelyHkGyew2pMJHeqI_yB2FXh3lC5uJqZVmKE6G2TlAuttLJKAF6cqABbrN9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-122970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نخست‌وزیر قطر در تماس‌های جداگانه با مقامات عربستان، اردن، مصر و امارات، راه‌های هماهنگی منطقه‌ای برای پشتیبانی از میانجی‌گری پاکستان میان تهران و واشنگتن را بررسی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/122970" target="_blank">📅 09:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/122969" target="_blank">📅 09:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122968">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
هاآرتص: عربستان سعودی و قطر نسبت به درخواست ترامپ برای پیوستن به توافق‌های ابراهیم محتاط هستند؛ این موضوع نیازمند تعهد به تشکیل دولت فلسطین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/alonews/122968" target="_blank">📅 09:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122967">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در مذاکرات با ایالات متحده، ایران می‌خواهد کنترل بخشی از حدود ۱۰۰ میلیارد دلار دارایی‌های مسدودشده توسط غرب را دوباره به دست بگیرد و همچنین به بازارهای جهانی نفت دسترسی پیدا کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/122967" target="_blank">📅 09:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122966">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
طی روز‌های اخیر حدود ۱۰۰ اداره و بانک به‌دلیل رعایت نکردن الگوی مصرف، مشمول محدودیت برق شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/122966" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122965">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مخزن مواد شیمیایی در ایالت واشنگتن
🔴
در پی وقوع حادثه‌ای صنعتی در ایالت واشنگتن آمریکا، دست‌کم 1 نفر جان باخت و 9 کارگر دیگر همچنان مفقود هستند.
🔴
این حادثه چهارشنبه در یک کارخانه تولید کاغذ و بسته‌بندی رخ داد و نگرانی‌هایی درباره نشت مواد خطرناک شیمیایی به وجود آورده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/122965" target="_blank">📅 08:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122964">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASNj97kw99xjFnxVunrygYD5wHCUNoB5W1TjWDnv12YBaY9o8U7frV-0TTBtIBddoaD1r2-x6jv_22C04X630ipfzPV9qcaEP5a_6lN4ACNyzBSn0EKIoTy43bIGqaFMZ5h7MTwtV0ZIoegNmi7_ir4Sm52hHhyi_31Bi5AQg7r_zvqi_o9g_ocHkpnl5-uHJFv_Rn7_brEH5Q17M_Sp1J2Ufw15VSZyXO49pl2tMIiZ58FWwJUwbkLEJ6WIY6QX6ddCS5edIlHyN92FkQb6OG1916gkD5oYrlo4m6k1B0ditq6qX-R31DoFZ5usnBu6Gg-Kri0XG7tjX7tiSzjBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی پایگاه هوایی تگانرونگ در روسیه را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/122964" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122963">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G30aN265ZppTrFr23-EJ1CS5vcLMl9bJwq7EAKk-LgfvfspwK3tMQcyBPlcfmYaTxhFgET6HC5zi6Qxu2Szk6mig_xRjQZ7UA2N-_q7cWc-xgekxExPgVYJ2bdKcKQTnmBzo8E_jQRh55KaiOrn5pyef3yjbx9QdwsE71uMNz3qHeR9sTGK12GrueJL8z0vggdahC2z3UhR26ne5ZR2WyIpP-76dtHCOIuvue6-87Cx5yqCioz3wHCPrJ0QLAnUjK9S2-1qKlrqkGcthdt_rV9Q1ifosyizEY67tkMUjogXNXUNaEdsxNsjfmL6BWvUdbNkNM3fVZ3N4a0opX3SNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر روز رویترز از کشتی های پهلو گرفته در نزدیکی تنگه هرمز، سمت ساحل عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/122963" target="_blank">📅 08:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122962">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فرودگاه بین‌المللی تبریز بازگشایی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122962" target="_blank">📅 08:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122961">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فارس: بیش از ۲۰۰ فروند کشتی در یک هفته گذشته از تنگه هرمز عبور کرده‌اند
🔴
اولویت عبور برای کشتی‌های فله‌بر و حامل کود است، اما برخی تردد‌های مجوزدار را به‌نوعی آزادسازی عبورو مرور از این آبراه تلقی می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/122961" target="_blank">📅 08:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122960">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
زنگنه، نماینده مجلس: آمریکا حق غنی‌سازی، حاکمیت ایران بر تنگه هرمز و رفع تحریم‌ها را پذیرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122960" target="_blank">📅 08:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122959">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مدیر عامل شرکت برق: برق 100 اداره در تهران رو به‌دلیل عدم‌رعایت الگوی مصرف قطع کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122959" target="_blank">📅 08:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122958">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7664471564.mp4?token=d5dOBDFK3puoYjz26JQ0A8sYtlGscK7s7-lpEUNeXgFz9L9_tb14ZpIcMnlzmpm_lm94qqpVSDI2XsrOYkelQp2MXc4Wvt_0Ix3D7NFuk4SZHuK7YIS7kwigj312c93d2GyBiC0RtOgdpPF7Np7xunw3Fmf4ewZDX0MSNJrP9TrRL_BsByKNwWzyiE3Tex-8gd_PvL7J7F4jAQYb2SLjjJ5V1N3n8m37IwMiN9eoiW9zzDPhqA2I9fMy_2MtqynIAJp00PxNVXGGxsMYisWMCazJxnRmFWnNbwfDCMsUgdsrfNVaAs9BlbMYxA0S3ZjB5z3ZOBgU-hUmTWHuw7HDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7664471564.mp4?token=d5dOBDFK3puoYjz26JQ0A8sYtlGscK7s7-lpEUNeXgFz9L9_tb14ZpIcMnlzmpm_lm94qqpVSDI2XsrOYkelQp2MXc4Wvt_0Ix3D7NFuk4SZHuK7YIS7kwigj312c93d2GyBiC0RtOgdpPF7Np7xunw3Fmf4ewZDX0MSNJrP9TrRL_BsByKNwWzyiE3Tex-8gd_PvL7J7F4jAQYb2SLjjJ5V1N3n8m37IwMiN9eoiW9zzDPhqA2I9fMy_2MtqynIAJp00PxNVXGGxsMYisWMCazJxnRmFWnNbwfDCMsUgdsrfNVaAs9BlbMYxA0S3ZjB5z3ZOBgU-hUmTWHuw7HDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به سُهمور در دره بقاع در لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/122958" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122957">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کی‌سی‌ان‌ای، رسانه دولتی کره شمالی: کره شمالی آزمایشی از سیستم پرتاب موشک چندمنظوره جدید انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/122957" target="_blank">📅 02:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122956">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رسایی: بازکردن اینترنت اشتباست و خیانت به رهبر شهیدمونه.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/122956" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122955">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-O4m3tGPvmoUJzZsmYWr63O_5ydtAiHo9dhPmU5jyexPlbbw4qMG__H-GGRrJ9AcL6uPe77twX_tXFv6xspyu4aL1O4YSk4QGwYiPTgeIjeipHSqGSCY2G0CwWf8MPVzkMfDIhraqts-zWtUEUwSPlX9-l8kNG-9VLYk_uTZLHNKD4Gqy4LZ91abJ54ySKlprb8mq6Bn0iURjgoal7CfPbkeOS0JGQc3hZ83vIiZw3sjc_iUxT5bR7sp9JTBxr-8kr8hvnureE9JUxy9w29ZuPXj5zEsetSFePDR2d05cH6B_03Pfi-t0DxwUp3z8i26qYarVBM7jKmnUAF_VAeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: بازکردن اینترنت اشتباست و خیانت به رهبر شهیدمونه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/122955" target="_blank">📅 01:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122954">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
چین: توافق پایان جنگ ایران و آمریکا باید به شورای امنیت ارائه شود
🔴
وانگ یی، وزیر خارجه چین گفت که پکن معتقد است توافق پایان جنگ آمریکا و اسرائیل علیه ایران باید به شورای امنیت سازمان ملل ارائه شود. وانگ گفت پکن امیدوار است طرف‌های مربوطه بتوانند به دنبال کردن آتش‌بس متعهد بمانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/122954" target="_blank">📅 01:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122953">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3n9tO1yG0gtIdRc2QWKdtJeiSQOzxVouNWMwsuZDUKJHx06f2ORuD-WBMr1bTraM0TH0FixnpsLMQMHrxhBaQuAYwAwTnGscZ6uaC1aRl2NFgcvsX9gErcVJT7VcAEsZcB464VIo3DjIbEIm1uNwCgvRrs7wBetMnVRJZdaHHkyHKF1Bjs0B6laxqKnKBUMDyqpUBVuk9GHabR95-6mBcuh7ar7DYn-ZVDoEgB7eidKUCvVqxJ32Neir9dqp9sU3LUpHOfvTvDnasGPW2yNrk4a04KPwXnBK_aIqrJN7jSzeu5kG8CZcfUYgdUwhRRKfP8PUzu22525PBaeJM4KUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته شده برای حضور تیم ملی ایران تو خاک آمریکا ویزای ساعتی صادر میشه یعنی اعتبارش تا پایان یک بازیه بعد بازی دوباره باید ویزا بگیرن
😐
🤣
@AloSport</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/122953" target="_blank">📅 01:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122952">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgNVe9DujAoGO-TnrIYttj5SuRWwDtBZQQ_SMDdeHBtA9my7U14p8j8yImGIbQ-DhITfPvtXlZdKtOHZg0HeV2GMRuy8usINh05wGbN-_mISiWaMMiq5wR0cbZDpUdSQdVvj-WTmyvcM2h-pwS4e7TjAZ7BbHWL9nUnJd65rsW_wJdu-PkxmgueyFN8cjqEBu3FoVCR71LbQ_la9LtuCukEk7FaGK3bqAmr_FlxuBu8P-GpJ8y3jkzk_Bs9R8udLfXIx0M7qKCSBgvQO0p82Qqw703Zr5K63jYFVzSdHXqScbe1cJE6vlz5kbGdpyR3dak7U_7Bk66zZtJ03ELkO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
و کسایی که دیگه هیچوقت آنلاین نشدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/122952" target="_blank">📅 01:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122951">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/122951" target="_blank">📅 01:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122950">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411f1a7cb7.mp4?token=iGki1A6C6q7JsUQEM2MTSQdbU77LLaYxnAmuxE3uBdvQKL5DtcvmlxjjYudE4RSHNOQ7OgppAxMnhPJyujuTBQjrL1dHMXevqJkhsvXGWOYhWlBdjvCYe8LCRPorGzzeVJLhMQTB_f38Wa1nCrM3wmEQMC3QjVp6nz_QAiQ-bze-DChcnE5NxPkC60LUpGBnPKre_ghbLpwyH9TmPC8vWC2a9sq9LecavGktFchQnlDJesQoyLCskqJPCnnEcNKBNWckejtLljZN0avyruNKyVx89SXKMfv2olxvksQQ28ed9SXZL3IU4a-cttJHXQP0Vd8gjZjF2OuobxevMPEs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411f1a7cb7.mp4?token=iGki1A6C6q7JsUQEM2MTSQdbU77LLaYxnAmuxE3uBdvQKL5DtcvmlxjjYudE4RSHNOQ7OgppAxMnhPJyujuTBQjrL1dHMXevqJkhsvXGWOYhWlBdjvCYe8LCRPorGzzeVJLhMQTB_f38Wa1nCrM3wmEQMC3QjVp6nz_QAiQ-bze-DChcnE5NxPkC60LUpGBnPKre_ghbLpwyH9TmPC8vWC2a9sq9LecavGktFchQnlDJesQoyLCskqJPCnnEcNKBNWckejtLljZN0avyruNKyVx89SXKMfv2olxvksQQ28ed9SXZL3IU4a-cttJHXQP0Vd8gjZjF2OuobxevMPEs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساخت و ساز برای رویداد UFC Freedom 250 که در ۱۴ ژوئن برگزار می‌شود، در چمنزار جنوبی کاخ سفید آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/122950" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122949">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTe8ajRK1W2NSbUPQ92aTC8raDzjS-eUWS0rQ55y2WZhqI60RQrumtH9-8H2xR--7zYvLM00PXcPjoIo5nJSBfMeZN8eeJQd32NvtkH5HsyZmu-4PyL93IXspffZXxzFx3SfSaEkQ4uiPkf4J0fXShYa7zqkTO1CNVHwJnMmjlRpnK6sYcxexC6-J4cDHhuuNLlZHtcxMkvx_91alZO-fThHMHzTTtsvkaPAImnKERfJLHWanuHo-hEZHNU1P6Osh3tlH29Jk3109W3XWranE4mjHS7_48uIp3eHxPL1KDXCA236kvDzEPrmOHobDq11Y_aVz3BlfgsKx6oA_-6DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس سازمان بهزیستی:
بیش از یک میلیون کودک بازمانده از تحصیل در کشور داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/122949" target="_blank">📅 01:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122948">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBelLeUH4WXGSt_AZawupCaAs4BOTmbAHpfiYnZfH0yOdGFLQwkBGbld2C9hVdCz4nnfubzY6QHSA24CgehfhY9GQLpXseLVDwY55gUd5aVo7fYQtaHzhx1qbRtEuIWwKuINlBNVdrm41n8wFPr1t_TTqOWs_pvLzYvmo1fWSb3kx33X8sW30BEuitXAkHn1AR94d_ZRWQmAsyFoElADgxWedoPhG4tqXHgnMll5tlZFlkGKx6C45crUnkBATmCEDXaVfn5jaORGMu4_OUFGkfDkkOrMTWE2UMziv0p8C3iFsyUHsB8fUmzxg_rwV_y4S-Pv43fWney7eD15UpKp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
اقدامات تقویت شده دفاع از آسمان در عربستان سعودی فعال است تا زیارت حج را در برابر تهدیدات ایرانی محافظت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/122948" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122947">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vil3WSfTu1yvWeAt_Sq9bXYPftPiKyceyKndypBEPAAkhlgzDL1YbqV1emKAfG1V-7KMtGqNW9P5pNqBW_hRNS6Ou6Ray-JZCzu-AsYQnhqLfw0Cpv1VDsBxMCpp7ftX9gn9n3Xe4Hg6wVzM22s2CacWOx9Q9x2StARNAqX0ZPgcElIl9FfVK0_YqPIYfOYKHHZ0ZdVd_KjM7mJNckYVEHswl_vkBvst3IbhLRPfXrXn_NyHue-HpPgmInMhEIagdKhK1xrrxasAl9U5Sb3m8DgziUgj8ylbq3IiBllQPzxV8pxgLmdVk9iHNZ4uMvgth4kv2Zjfs5XN7Eexj1nthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیج فیک متعلق به انقلاب شیر و خورشید
🔴
رفتار سایبری ها رو بهتر بشناسید.
🤔
پایگاه مقداد مقیم خارج نتونست جلوی خودش را نگه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/122947" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: همه چیز انجام شده، چیزی باقی نمانده جز [امضای توافق]
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122946" target="_blank">📅 00:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4r_mhS4mNGOam0GsNyRG1M5uKs8XDmzka3YC2KpEixasAdCyYUg9Jlrwha2PT6y1enZkVc4jeSs5WELIas1iUgXfZQHqKXGZArGTCenA7OWQEbf3KFZ4bRQ-8zvWldfdGANDZYRheZEhEIs09QrdBWDA_vNPM8ZnpIoAqHkoev1OVfj9oZiFDOhD_x_sPB_o-_fGDgOXu1LQxz_N0Ign6wHP68-MpjDkgZD9M6Dv6pBBd4OA6oKo1ITx-fa3nnM5M6160Eq6NLDa72Dqf48aG6V2P2f6rLE8ZHhUtyYaB-ylMC9VzjixxHwSDmzaN89seNjzrL9M5J_TiyRgNPaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه آمریکا :
- عملیات «خشم حماسی» هیچ توجیهی برای حملات بی‌دلیل ایران به نیروهای آمریکایی تو منطقه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/122945" target="_blank">📅 00:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLPPIUlAHDDqms6xNwjaBtHsF7MH3kvXDKGDzAqXpJ9_tjnY8_AbO6nOTVNx4qwYvmLoQ2g-Qxz9hVaONtHowRx47S1sI8yzIlbe-sHBSWBg7gScQZRMUKLhSrasUNO5cToaXwCERGRyyTqnorJyDFpN4pJc2bj6Y5z5gLfEjgviHuaTE-Rb_w1wgXbxSdGrx-7Ba_bEWS4CFupASGB-SQFamvLp6fICXVVyVXAb8XnH8MksyAElrn7AJ9TUZUIHEyHa3lrgYkONNG4UFttUknr3qGNfMVsuWvUhpRV5DWD2VZscG0yIJBgWB3Oa4iBUD60u8042FJmsR7skK5X21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق الحسینی: رئیس‌جمهور مملکت حتی برای باز کردن اینترنت بعد از چند ماه هم اختیارات کافی ندارد! این چه وضع حکمرانی است؟! ‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/122944" target="_blank">📅 00:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاش ما هم مثل اینترنت به وضعیت قبل دی ماه برمیگشتیم.  [@AloTweet]</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/122943" target="_blank">📅 00:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6b923b91.mp4?token=a8Clft5TsDXPiYGAz2tbzFpfCeLfKjyvscFh7tDxtqDO4LnSu4oAqJDcl-JTL_79fcg3ahWpIwKqITWyqdb2WIHJHHbcKvaPSZcbNN--7CHdnCC43rGum5iXZsUbxScuAskFcmWr0aMln2mCDDoVNOQhcW1ASoJKjZtHzgbYiTkwKW6YNrIo9F698TNUZQjVYza1Dt-XWBiMLgq7aLcC7gKwb9mJ-F6Q3W0GKn749HXGkrsO_U4MDBrIy5DVj-xAH8U7kvPMsMnueLslMqZw5yhoCF9jQ_en0c5ugbTRaBSAlA3MFVO-LP-ZZRD8d3QbHM4_ZVQqGEn32-kZzdsQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6b923b91.mp4?token=a8Clft5TsDXPiYGAz2tbzFpfCeLfKjyvscFh7tDxtqDO4LnSu4oAqJDcl-JTL_79fcg3ahWpIwKqITWyqdb2WIHJHHbcKvaPSZcbNN--7CHdnCC43rGum5iXZsUbxScuAskFcmWr0aMln2mCDDoVNOQhcW1ASoJKjZtHzgbYiTkwKW6YNrIo9F698TNUZQjVYza1Dt-XWBiMLgq7aLcC7gKwb9mJ-F6Q3W0GKn749HXGkrsO_U4MDBrIy5DVj-xAH8U7kvPMsMnueLslMqZw5yhoCF9jQ_en0c5ugbTRaBSAlA3MFVO-LP-ZZRD8d3QbHM4_ZVQqGEn32-kZzdsQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:
جمهوری اسلامی درخواست ۲۴ میلیارد دلار برای هر توافقی با آمریکا کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/122942" target="_blank">📅 00:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حزب الله امروز تصاویری منتشر کرد که نشان می دهد یک Fpv به طور مستقیم به یک وسیله نقلیه نظامی اسرائیلی که سربازان ارتش اسرائیل را در بنت جبیل ، جنوب لبنان حمل می کند ، حمله کرده است.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/122941" target="_blank">📅 00:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
جمهوری اسلامی چقدر مردم رو فقیر و بدبخت نگه داشته که بخاطر یدونه مرغ صدقه‌ای اینجوری صف کشیدن.
🔴
کشوری که روی بزرگترین منابع طبیعی قرار داره.
🔴
خمینی: شمارا به مقام انسانیت می‌رسانیم.
🤔
ویدیو یه نکته‌ داره ببینیم میتونید پیدا کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/122940" target="_blank">📅 00:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEgSX2YlvPxtp7PNMo4dIuj3lJpQF7tE9smtxc73GKltcMVVE2XpNZYjU-4Q4AghP1VreX5nfiH7UXUpza500F_M85MqLLcpoxBGW8AIvcqGGH9n9wY4InHxr8rzUMyyBXyi32iSFhKlCRMKRnPOHI-zCHNzNG1SPobfI9NewqAg_x56cCPBmm1cG68gb_zrNX0ezu4QNpEhjafaJrbVL-660Cea-22PzawEwAB2UnWe76d9OoodJcVNKQq-A9TarROiycz2TvBqJj7i70IbAnFsf2063BeYIIZAB4o4rSQmrZ4UconAO9XVfJt4XPTb-iFVi1QM0fDMUns_MR1qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : فردا جلسه کابینه تو کاخ سفید برگزار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/122939" target="_blank">📅 00:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWIb1mVMu0-kVLR5rFFozjJNG82MFqDbNqMkIj9-TQ8gxfu88TXtmsHadDkbmeT0tscSul5IELDurDd4IWjclj3V33uLPPnKxEQNHCULpIi8Yj2X4lQBBOxlZNc0I4Xw5F7uiq8w10W20L653idh6IQkuewryqfcRDvmb68JRdEUtTFbNHTXnlVxX5JeqCtNZAPNDnbViSVxc4SoAzjT-9yN4Qr4_qSUa6MSFSt_4IhfEedCuY0xe93TR3PzUGA8iY3Wn3gJzARbLwC6iDCLpX8eSszF_AVGLqmqQ2IlDjz7mpffkjRqz91A7GDH5MHUToWInlnf0L2Dpyla2PQavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: از افراد درون این عکس(فرماندهان حماس) هیچکس زنده نمانده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/122938" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJ6KfJuYLk1ujbhWL7Taj05ap82i_OvDueHKw2YnXVwzW9f7JOdRB5YSZ0hYc2PQg16RqjzZIelq-o0TJgVUvMcbVnSeS0uPOEVtxOhaCFqm_UkPOL9TUBP5lg4iLx26Bs1xS5FtJnOufWFzI7dHzgzXkIJXWixtSCTCrgDlaYETyjR8FFJQpavqTq_8uz4gsWc8V2pZKtBjlt3kr-AP5gBOU8mq5XHwcmsAv-GvYxRJqmMkFx0BQitagWjsxLdKt4z_KO142vLiaFslEukHjzfE-ojqm6mhg1LtBAhbxFcKoDvkDsSPAXU18LEM9CZ8WKak4EmZkFbUXZvA7Yv7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از محمد عوده، فرمانده شاخه نظامی حماس که ساعاتی قبل در غزه ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/122937" target="_blank">📅 00:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZfv2sCpcx5ILSG0peu6TuAj7M3xLsSwnKh7CiOWIeS427eKhAiKOE9tChiQO3FMqvG94AqF0HB7Knnh_IaQh7TwZI0y6cQcVFR1ospboj5a3XsAeS-6iwd6zzVMA0qQl7YJPQXR-p1-B78b5yRVcq59g4YDaiwEXDz6klH0gO8YoJ2E1a_gCFmt-qk5Ac7IFm7SNEpBaH--H4jJfSpiJwSS2YDqlRSXc0pjupdWXO3HO4Fowi_Ej4O4Nny732QDOn6aJeA7nqNQIEu7X3TTigQ2gTGSNV5U8xJ9e6Sp2RfHBgbdJpgC98LeUO-cohp743eZUs7tLOdF6UTutOxKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: میتونیم بمب اتم درست کنیم و بجای اینکه بزنیم تو شهرها، بزنیم تو پایگاه‌های آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/122936" target="_blank">📅 00:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
حالا مردم خودشون آنلاین شدن و دارن می‌بینن این حرام زاده های «سیم‌کارت سفید» تو این سه ماه چه مزخرفات و چرندیاتی رو به اسم مردم ایران جعل کردن و نشر دادن تو رسانه ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122935" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1005c8d36a.mp4?token=Dcmyht1WdKnJngCoLwjd_Eutz9FvoRJBE3mPUYUH_b3vyaJf24xkKY7FM4BlZyNTqk3oFDb-xE1fJ7NPxDrlIJN9lxnj4cQ3-Kuq064QYSBrAWtkRIyNlI9QezOeWmqWZYwZB71viIYgAWd3u4zNkbWwaDKgury1CKRfpR2otpnszUnnF5patW_kmC6ffK4D3wT47QKpTh-peZS-Ubu_PG_CyJVNGFgETxndPfygJ18YOSoYAKmwQxDpRH3suxNtrWIWanTI-99WDuxxXeT_RFo-pWqubKTCXtVr_Y2sBXHeY_p0csdGAtxxBYGHmrHpfyofe1lcIVMU3bUxp6rvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1005c8d36a.mp4?token=Dcmyht1WdKnJngCoLwjd_Eutz9FvoRJBE3mPUYUH_b3vyaJf24xkKY7FM4BlZyNTqk3oFDb-xE1fJ7NPxDrlIJN9lxnj4cQ3-Kuq064QYSBrAWtkRIyNlI9QezOeWmqWZYwZB71viIYgAWd3u4zNkbWwaDKgury1CKRfpR2otpnszUnnF5patW_kmC6ffK4D3wT47QKpTh-peZS-Ubu_PG_CyJVNGFgETxndPfygJ18YOSoYAKmwQxDpRH3suxNtrWIWanTI-99WDuxxXeT_RFo-pWqubKTCXtVr_Y2sBXHeY_p0csdGAtxxBYGHmrHpfyofe1lcIVMU3bUxp6rvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از کسایی که تو تجمعات شبانه شرکت کردن دارن میپرسن نظرتون با قطع دائم اینستاگرام چیه؟
🔴
و اما جواب حامیان حکومت:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/122934" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: ایران به دنبال توافقی است که بدون واگذاری پیروزی به ترامپ، موجب آرامش اقتصادی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/122933" target="_blank">📅 00:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f4740d27.mp4?token=mF7QbHyVMudaKmTd9APKqEO4PL6EyU-Wzh_p6PicTajGGRjQVEY-RebbFXNcG5UeB1JRdXmsRwvTCKZPvNWKaNyg1n6SFE3d_aDexWB4eAuVHw85IywU76aWYXSv4YOD-oPSeiWYCB6f6InLnj86XJMI1N6KeRQmYOiqBgwTJxkjG0pAVSHUnEshjo2YsYeviHj_ZlsgXnChGnIMFmftX4ZG4niLq5rXxa362Ufz_0oUflln_mKk0IlFMIHy-ao49RhjHk76iI677uGzbWtMe_9s-R62upc2A9q1u4DKvgBAshuD_nMNLZxIpSXHsURHzzfGPCO9eC5z-jGA8f-8nnp9N75X-O5fGAx0w8etME7M_BEqR2JNH0bfw31IM5k6Y8T9TuAE_BL_fJUKGuz6vWuj85v7OL34M3KOCTYPFodHG0SQxoFsUmIN2d6W2eE6_TM2a2Yf03J1zboweHqZ7Z9d3mbdpdf4EsjSdugDb1Q2bSCUCYMr7tyHG7ytOuBF51EXSjBfPW8Pdh-JtUgLynvWVhAADWHzg0YXsU7n9fTHrTBIAc4rUUYTanZx6FTLWmHBXBIv2_emKoPG2X4KBjnKcj5NZV5awSwcRnuxS2TgoOBIgCT-15xJZIPOFgW16M8t8qRiURCuTXiVVSucxm8uZBBl0gX0V23Mp3BEQPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f4740d27.mp4?token=mF7QbHyVMudaKmTd9APKqEO4PL6EyU-Wzh_p6PicTajGGRjQVEY-RebbFXNcG5UeB1JRdXmsRwvTCKZPvNWKaNyg1n6SFE3d_aDexWB4eAuVHw85IywU76aWYXSv4YOD-oPSeiWYCB6f6InLnj86XJMI1N6KeRQmYOiqBgwTJxkjG0pAVSHUnEshjo2YsYeviHj_ZlsgXnChGnIMFmftX4ZG4niLq5rXxa362Ufz_0oUflln_mKk0IlFMIHy-ao49RhjHk76iI677uGzbWtMe_9s-R62upc2A9q1u4DKvgBAshuD_nMNLZxIpSXHsURHzzfGPCO9eC5z-jGA8f-8nnp9N75X-O5fGAx0w8etME7M_BEqR2JNH0bfw31IM5k6Y8T9TuAE_BL_fJUKGuz6vWuj85v7OL34M3KOCTYPFodHG0SQxoFsUmIN2d6W2eE6_TM2a2Yf03J1zboweHqZ7Z9d3mbdpdf4EsjSdugDb1Q2bSCUCYMr7tyHG7ytOuBF51EXSjBfPW8Pdh-JtUgLynvWVhAADWHzg0YXsU7n9fTHrTBIAc4rUUYTanZx6FTLWmHBXBIv2_emKoPG2X4KBjnKcj5NZV5awSwcRnuxS2TgoOBIgCT-15xJZIPOFgW16M8t8qRiURCuTXiVVSucxm8uZBBl0gX0V23Mp3BEQPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده شهری در فیلیپین را درنوردید و 489 خانواده را تحت تأثیر قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122930" target="_blank">📅 00:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmJTf0HvHjsHS_xdNhKS6ZxheGHVTYvQhEFlcYyyLZwOllTrkUotqVr75pJBHt4on2awpz_zxPMntm32cAgE3YZx9E9JULt8z5PJvoV8XWFKHbFa7l9QeDwW2Q6FpnioDlNFcmTUn9OONMy-2pxCdQxOQ4V9kijhCh0fjnRysw0zTGBThcJon6o8b1dznOdr85_5mZvJllLr3w1QnWoUbtEYM9Z-wwbwen8d8z-8B5IFlqD0D4QDlBiDdkyIUE9pP2W2TdMnyfxFF00fI4o2yrM_Sm0tfE8IltkfcYtBsGUyT8c0aCw8wp8yVRB8HYdWr5zdA2KUv_IASRuIDmlcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت زمین و مسکن در ژاپن همچنان از سقف تاریخی خودش در اوایل دهه ۱۹۹۰ کمتر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/122929" target="_blank">📅 00:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUrqIBOjbL1hhSnNktIhdSBFbATvnUyRAg786IBdAJ33vJUXRNy4qtn0eqMYFgmPBNdJZveaUvuEhMVHCEmHVdwy5digo5FwlK5LljDdqI7zI_236Ix5CGgGOAPvplL7LH2jAJz6zuUH3id37frhZugKYIIBBJ2AmUkDVK5lKfEFhw-2buXN5B7ewpIeAAXWZ-ljNICHu1srhSrWCOJciJKBhqvpEvX6yT8dcWJEFxY9eu7vuQ9wNxumwRzeqJ5msGMV3TiV_kyMY1Z4FaJqF5ESyhfFRwJN2SvSnPfYYdae2XXsLeLe88U9ui7Q_1EgdbKPhs6eJyrXp85iFnVUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/122928" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122926">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pitM1C4LTTcP5aXgq-dPYrS1e4xgYxSXyqrm_yjHcvNX9UrNRrKXpL-XDA-pZniFNwSOaVJ9X46y5rYGq-cJC36qtTVCNfxtTd_NYNWjDXHcNwlQ3Z3zYG-ERTJmqOoEBB6S-JvjsOqFsk9mf_Qi9QJVsyD7GyUlYKG5pGGIhcOkNiW4q9cR_HWojkv--4udAgbLjBEXFcXncEuP4T_DuYrwVZF_tWezWHWsTcYFOWP0-65Of2d_2g7Mij8_JJyKWrsDU_SoDQ3uONfh4W5f8Zl174DwYaeRwjt0DkBeXkWou1XfwV6ekumh0sQ73dsbZFPnIoB1pZS3ce170K5Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-5tsOrpRhcrf888Y815SdTcdLnRN5kjsbvz7aFs9TXKZDasuVfFAGbHyACeGhKnSLElFqy76kyLTkanitPfMTHWbaZaSCA3229m5vGwxl9-ywUIWB8YJpbkB4Lo0Cg05Y8Enc6Qw1hT0RZZmmWV2E1hTlWcvL17XgtcdKpDzCNB0PDRv1iBo_X44EOo6YAbF7J4kBJiibKV0Y0dL-HOKFmZH9wBlfmoiSRdJpbhPYi6Nav5VDtkyE8J_kn2ZUJIF-TK23nrOx5EyOBZXqmqNJ_gxWm1_QSp-NQwuZaqlXxNzHo8l_8sJaDvi1BCg6a6dRocRiGWR0xoJZ9jhxhYkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
همچنان در جهان ۲.۱ میلیارد نفر دسترسی به آب شیرین ندراند و مجمع جهانی اقتصاد تخمین می‌زند که نیاز جهانی به سرمایه‌گذاری کل تجمعی تا سال ۲۰۴۰ در زیرساخت‌های آب ۱۱.۴ تریلیون یورو است که ۶.۵ تریلیون یورو بیشتر از سطح سرمایه‌گذاری فعلی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/122926" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3695a24bdc.mp4?token=j3i7OQycnHWRvDr1B_LSMGOJtEU1HtyiyJL-o4ObwHeIdKSIclXRwkB8Awj2O-sYSMSfIQqE0YoKh9EoD3wv8SXAKx39dwKIIdhke5oKUHetyBN7wbyyf80soFWgC7ixp-axPsoQbwRAe2Dwm-fjoo2cG5wh9VnGoduTxAfEz2TRtXRZl9ZKRUSq_PHUQLk8eAzoUG6fXqL-SYyLf2Qz2Te2_Aji1Px0c-gxJ-ZVkCbKghMSDPJSet_kox5jE21r8I2rUB92wiT03J58_0Iyr_C9hvMroDbVTWfabYxFqnyhX3g0VuDh4Z0CerbQGTLUU6BisvfniUhg_a6OikT1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3695a24bdc.mp4?token=j3i7OQycnHWRvDr1B_LSMGOJtEU1HtyiyJL-o4ObwHeIdKSIclXRwkB8Awj2O-sYSMSfIQqE0YoKh9EoD3wv8SXAKx39dwKIIdhke5oKUHetyBN7wbyyf80soFWgC7ixp-axPsoQbwRAe2Dwm-fjoo2cG5wh9VnGoduTxAfEz2TRtXRZl9ZKRUSq_PHUQLk8eAzoUG6fXqL-SYyLf2Qz2Te2_Aji1Px0c-gxJ-ZVkCbKghMSDPJSet_kox5jE21r8I2rUB92wiT03J58_0Iyr_C9hvMroDbVTWfabYxFqnyhX3g0VuDh4Z0CerbQGTLUU6BisvfniUhg_a6OikT1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیوی تازه‌ای از پیکر جوانان جان‌باخته در دی‌ماه ۱۴۰۴ منتشر شده؛ تصاویری از سردخانه‌ای در خرم‌آباد، همراه با فریاد دردناک مردی که می گوید: « دو برادرم رو از ما گرفتند.»
🔴
این تصاویر فقط روایتِ درد نیست؛ یادآور بهایی‌ست که جوانان این سرزمین برای آزادی پرداختند.
🤔
صدای یک ملت خاموش نمی‌شود. راهی که با امید و ایستادگی آغاز شده، با آزادی و پیروزی به پایان خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/122925" target="_blank">📅 00:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
طبق رسانه‌های عبری، ساختار امنیتی اسرائیل از کشته شدن محمد عوده، رئیس ستاد تیپ‌های عزالدین قسام، اطمینان دارد.
🔴
هنوز هیچ تاییدیه رسمی منتشر نشده است، اما انتظار می‌رود که منتشر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/122924" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOuF_PVc82UDluMoQigyCbBsBxuodDqZCx4zEjPMAgkHk27WBXxeFnT7LmmFY0783GM613g_OqmSvIMQ0lR-mFUujo_7Xx4eENdzJdTzAVuDUn_ezNiEwEmkDT5bCKIRyROc12VuiPeJzTd8JRH5PbuwWstfw2wDg7MOgjQjBVv3d6qi2Rzi8eZZMqm3eO5mkg1rVEp9wqjshoC94HiwNLHJao6XIn0GmH5KbIMUCWRCH0WKzf0K5sBZQTNul6lQQlBFZZpqzwbzRTkYmmB2_1JNoFpb4FB1Pr6AVHD0scL16vZ-iulJszWaoYXqX-cMSnWIpxME13jI0vskPb4z2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: جهان اکنون به‌شدت محتاج توافق میان آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/122923" target="_blank">📅 23:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : تو نهاد امنیتی، ترور محمد عودة تأیید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/122922" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
چین توافق پایان جنگ ایران و‌آمریکا برای تأیید به شورای امنیت سازمان ملل ارائه خواهد کرد
🔴
چین: معتقدیم که پس از دستیابی به توافق، برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد تا مشروعیت و اقتدار داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/122921" target="_blank">📅 23:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Cz-qUx4lej7BOQ-S8XTrw9dfefzF4dKFfkxSDZB0oBQrofv_6rhOp1-o7WnRFUuWLueIHlwUesCRi6xntHa7dSLCDn1ArN5kelnkPkgJ1BIea_HEdQmZzsQ9o4xYIbv95fIXewmu-rfCQ2Iw8C0K7LQYuy7nAtxNlWLCDYeQVszIVVFA8K3w0Ad41SoBk6NNycodLnDYu7TbFseZFQvQLmJZta6o6c6qkIKJbw6aRYJuBk_XYM7Jw8WsdX63NLj67ws8555CLR9oJrcacIRUXR53QF8ltRyu1m-ku-po5gbRV96e5pO1bzlwc9uz4D1-5iQfHo5gzkTDWMZFG4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه آرتی: وزیر نفت هند می‌گوید پالایشگاه‌های این کشور متحمل زیان‌های روزانه می‌شوند و در صورت ادامه اختلالات مرتبط با جنگ ایران، افزایش بیشتر قیمت‌ها محتمل خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/122920" target="_blank">📅 23:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فعالیت ۱۰ فرودگاه مهم کشور (از جمله مهرآباد و امام خمینی ) و ۳ فرودگاه دیگر برای پروازهای حج، با هدف تسهیل خدمات هوانوردی شبانه‌روزی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/122919" target="_blank">📅 23:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اسکای نیوز:گفتگوهای صلح باعث «کلافگی‌ هایی» در درون کاخ سفید شده، اگرچه ممکن است توافق نزدیک باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/122918" target="_blank">📅 23:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-FttNRjsnp55qgxfVfxJ3yodozzsC5Q4pTjRfzhRZ8t4_0Owd53LTpsXTBJuY225RVGuH7Cl25MFmVfHpnX4kmJh3-JZxyEnsD1MInsCHBKhMmbUz6PdXCPs1DuPjpj4yV8OB-ec-l04i_224qM15Kv_GgsVuHVAk0jVY5AOJMjpTC8lScQW5yB-wuR1y0uk8i3ceuqmj7hkS3O7xN1OZMlyPTgs24PAI76wd5hR3QhYq9UjXKELTaqhUB2f_5HM8yRloDPqB9VsU-W1Ivqr4Mg2YCsZsuY36gAjyI1wbi4TmWHnU-RMuPqJv5_O6wvT7IausFQ_43ZpJgozQWSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر کل رهبری باقی‌مانده‌شان تمام «اسناد تسلیم» لازم را امضا کند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های فاسد و رو به زوال نیویورک تایمز، وال استریت ژورنال (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود.
🔴
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/122917" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122916">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : آزادسازی ۱۲ میلیارد دلار از شروط ابتدایی ایران در مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/122916" target="_blank">📅 22:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122915">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کلودفلر:  ترافیک اینترنت ایران به بالای ۹۰ درصد رسید. واتساپ و ویکی‌پدیا در دسترس قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122915" target="_blank">📅 22:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bd2e3ff.mp4?token=PDSi9zkQRfhgHgBZGWWU1Qooo_QpyYHU84NjHHZtSN6QYdkDXDFirTwzUiCaWJBMEmclmj5olkhmzJaJYvUN__VJvc61GjlXDBR3XiGMLIsICp0zPkLYeVi-J1a2mVet42-6_Rk_zENoNI_Ia0sQnir8QYBQRq_D7RJeXDITIoTtTSQ4VHJouTI1JuSvXiyqc00NMT74YM4jtZOx3NBlOnjzXh8xwWVYkZOMhzGGuZr0QWl_yzt8FAGj7q2K8syvmqACB7p0rzrVGWIEhhKRbtWJJbI3gnhOEVuwGfqKZva3ylAROe21mOgSxrAPcXpNBob2xb6CQx0SXFUWlcmD7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bd2e3ff.mp4?token=PDSi9zkQRfhgHgBZGWWU1Qooo_QpyYHU84NjHHZtSN6QYdkDXDFirTwzUiCaWJBMEmclmj5olkhmzJaJYvUN__VJvc61GjlXDBR3XiGMLIsICp0zPkLYeVi-J1a2mVet42-6_Rk_zENoNI_Ia0sQnir8QYBQRq_D7RJeXDITIoTtTSQ4VHJouTI1JuSvXiyqc00NMT74YM4jtZOx3NBlOnjzXh8xwWVYkZOMhzGGuZr0QWl_yzt8FAGj7q2K8syvmqACB7p0rzrVGWIEhhKRbtWJJbI3gnhOEVuwGfqKZva3ylAROe21mOgSxrAPcXpNBob2xb6CQx0SXFUWlcmD7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه : فیلمی منتشر کرده که نشان می‌دهد پدافند هوایی ایران یک پهپاد آمریکایی MQ-9 ریپر را در خلیج فارس در سپیده‌دم امروز سرنگون کرده است.
🔴
مقامات آمریکایی این سرنگونی را تکذیب کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/122914" target="_blank">📅 22:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122913">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoU78z374SnXI5RG2Ekf4QOp93ciX7_BqkT2SLKT5t7SxF2LbarsSFjfiPg3fdj74ABEAGUqkeOpR755p6VN8O1IHOblZrZuodeBIQxtFXehMrcRtuhWI3Zt7r9_ufBkGrnlSlDOFf0nXXIhkn46kIIBHiPnGZZIhg4M5E1svenXd23qolbdfFm4870vq5Xld0h4C1nSDTjCaTNZn8v-wOIBLDF7DXau0USlGmjNfCM2o9o5Ta-_UQ6HZl85JOFkzqhBsAZVoPH43MqEoYVpjfG0fG-a1m-looUs6AnMNqJzOykeV7bdDWrn9rfh703hK4T4tzDGR9exo5AleT7l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/122913" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سایت
پورن هاب
به دلیل هجوم کاربران دقایقی قبل از دسترس خارج شد  [@AloTweet]</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/122912" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نتانیاهو، و ترامپ در حال حاضر در تماس تلفنی هستند، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122911" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ایلان ماسک : وقتشه یه پایگاه بزرگ روی ماه ساخته بشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/122910" target="_blank">📅 22:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/risSiAVuL_4Aav8SVmfKaYTeeBCaK-Fpy1z1Li48mMyhkUm1Ba0BZ7xihFiYxIHvPSB0gh_lKOUWAOnuvcNid1d4wiQWEsW25H0zQ8ZH7cc5_Q2TI3lwMt9X40pFW9ZB1IdYTbOus1yZ4Vvt6GlhVypWQEk9sPxdwycCTGL820AjE0rEpkvosxp0P61Vlx6_AYtG_CvGttBkGnzZhOqLeC-or2ailPM2R7JEmnRI4mouYrr39EnB9IwRX7A4lH2N8QlC9UxIIkrwzmsOKgPcd5gZ3V8WT7U0g6u4q0GCMNIZABhLYSTKSb6TrSZQucG6arogRyRz-WSV73OHGw9BvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نت بلاکس در صفحه خودش: خوش برگشتی
ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/122909" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو، و ترامپ در حال حاضر در تماس تلفنی هستند، طبق گزارش کانال ۱۲ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/122908" target="_blank">📅 22:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR5XlOHaRzXaH9vMyBkiZYt8yefryrLdIMxTr3mE5GS7aqVhjjvhbBzdyI93E_7cEOZ9GfW5TajnOnv-uR22Pt7hRfcIAa12gjkY1VEjHZ8VWcjm-erO6k548MkF5BQnwLfCoeefbrhJgpknQgTW1bdDh8ejA721OcDrFEmR4SjwvFXSiVup27fCgYOhEkb_IcyBZPRJIsp7NgrW6IXDaCagtsGEXglsXil7By6Kv46yyD51YRkwCdfa-3cWPsR9tBP_-iCxk7XyEawwer7eggAHVBBr0XSoWuWacKj7XnIZvD4KrFgZ9wU96V9MTzLKkP_a236cSJbJzL9rpq_6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار سامانه پدافند هوایی بومی «
مجید
» ایران تو اختیار نیروهای مسلح ارمنستان دیده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/122907" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اتاق اصناف ایران: فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122906" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122905">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس: تا الان بالای ۹۰ درصد مردم اینترنتشون وصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122905" target="_blank">📅 22:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان: کشورهای منطقه فهمیده‌اند که اگر میزبان پایگاه‌های آمریکا باشند به‌شدت صدمه می‌بینند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122904" target="_blank">📅 22:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نیروی دریایی سپاه: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/122903" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6143492ae9.mp4?token=o-7xDHO4IJBW6vdqC6Rsf99RJFsRUCHkR7nNQwDWU_ml5UrXZBZ3xmStgTI0MRXlVkK7_DFqmdPCKLdzD3x4yXLDd9amrAYt9VWQXlhrZovkjJAUmLQyMgE20kI9ub2BADvaEhoIf2NK9QyvIosy2WeMTnBW-sAXDaRdhexUe9NfuESTOLbOWJv1WuY-3RDXnwni6unrJvdfGQZoivhIpSIjlqf9ifo8b4w6amAxJ56Q9yNHhoFSJa8GQqX9fTYaLNrTkyQBTb-o2J4oQ5hWqXLJ3eFcrZAS6PLFBAn1FUffrw1ni14udCP7YCFepJml7gME55w7JAqa3fnincoZMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6143492ae9.mp4?token=o-7xDHO4IJBW6vdqC6Rsf99RJFsRUCHkR7nNQwDWU_ml5UrXZBZ3xmStgTI0MRXlVkK7_DFqmdPCKLdzD3x4yXLDd9amrAYt9VWQXlhrZovkjJAUmLQyMgE20kI9ub2BADvaEhoIf2NK9QyvIosy2WeMTnBW-sAXDaRdhexUe9NfuESTOLbOWJv1WuY-3RDXnwni6unrJvdfGQZoivhIpSIjlqf9ifo8b4w6amAxJ56Q9yNHhoFSJa8GQqX9fTYaLNrTkyQBTb-o2J4oQ5hWqXLJ3eFcrZAS6PLFBAn1FUffrw1ni14udCP7YCFepJml7gME55w7JAqa3fnincoZMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: همه باید به تقلب اهمیت بدهند. همه باید به ریشه‌کن کردن تقلب اهمیت بدهند. همه باید به صرفه‌جویی در پول مالیات‌دهندگان آمریکایی اهمیت بدهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/122902" target="_blank">📅 21:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بیانیه مشترک نتانیاهو و کاتز: ارتش ،محمد عوده، فرمانده جدید القسام را در غزه هدف قرار داد و ترور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/122901" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سپاه: طی شبانه روز گذشته ۲۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/122900" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvHtGaWHL6WeFdrYMf2976GZ1yIERr-ZSPr9MRK31gOeNACaXS136cxBYNwrHZcZq-90S58sgaRPgm1ooagzNL5oUz9eat3A4SH-POtMNyS-N33WQ_FzZiq9xL0zXOukazgMFmKmCtIa4gcEgdbCOU52n0UmVBb7Roil0-0bCbdhgCdJB_qoC7QdsVG6_FBd41UxtGaTkQ2FIeiq70lQhTOOr2NG-bIn36kkCLrjqrlra8P8ESKzfKa9GRO__rbCMprOGjg63uDDytNi_P0hOjkPatRo049SRFQHp3D7eYbx3RE40fDVtwFvD_zzhKnIU2n1T3EDm6PW5sOv7wAnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXqL_1E-sVHbvuo8_v0nXX0pfVN5nm1d5hCxN-EOC1MCCNMtnQb6_wnCFU7CE6XlZB4wpdhkemQGb5FTdX0UXQ0Lhv7vp9djwXBDh9s6xr3OEnTdwvBmjI_8-T0BZyXQ9TUSH2xEqfNysNGsP6ZDNnkkn3B7MJ3ctGFF5hOKZOxc5vw-tqrvszR8M2lQgVdDlJx84LTB1zmrzdA_HGufgBtYh6jwC5nV740P3lrUvEEjfbsUtIU_1hjxPhUG2uxWGrnxYbjECpQxZVPFfbhNtEWnwzNBbAGkEwmoa9o_ocCYNp3ZLkIeWiE5Esb5g8OFHL0422CyPtL-QRv0SH_QuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97b34ffba.mp4?token=bYkUZcz4JwQGVu8MkVouLbk9hfXubRGVeFYzgzYl51s45RmlaTZn1Iz0orlrt8N4Nv9wwmkPHFqal4bcKdNcWJT4trAkVf1p9_kPy_FQOcbS99KEZC0UlM01VhXKvRModdxY1uo-aOddZ81VbtanI0LwtPkMr35uQb1vnklE1K3KmGtQvpSSkqsmeMMkNS4tJAfveXnMIg9zZH2W6Vc5SF7MmcBj-Y1WMVHctgSX52cLnc3iBkgHtGiguCb5EiaYO25q3n-BTl_HZ8U1jS44G0Dki-u3zL6O2Inlglb1kE7Ju0qDcJfpf1Njo_scQDKXpe776wXlEv5Vu9YuO4uo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97b34ffba.mp4?token=bYkUZcz4JwQGVu8MkVouLbk9hfXubRGVeFYzgzYl51s45RmlaTZn1Iz0orlrt8N4Nv9wwmkPHFqal4bcKdNcWJT4trAkVf1p9_kPy_FQOcbS99KEZC0UlM01VhXKvRModdxY1uo-aOddZ81VbtanI0LwtPkMr35uQb1vnklE1K3KmGtQvpSSkqsmeMMkNS4tJAfveXnMIg9zZH2W6Vc5SF7MmcBj-Y1WMVHctgSX52cLnc3iBkgHtGiguCb5EiaYO25q3n-BTl_HZ8U1jS44G0Dki-u3zL6O2Inlglb1kE7Ju0qDcJfpf1Njo_scQDKXpe776wXlEv5Vu9YuO4uo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل حمله‌ای ترور را علیه فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل شهر غزه انجام داده است.
🔴
در حال حاضر مشخص نیست که این حمله موفقیت‌آمیز بوده یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/122896" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWRMvOXbJukVBVMoASxVhHdkA5OO-NzJqWrJrcQ_H2orm0YOdGcrORlFmNS-8niyXJEzXFyPXThnPPrXkrYXlIlxqloz9j9TuVK0RtfCUboTjUeNN8gk-PRy7YpFwHk46yRYUtrTFTUbruuJaEX2uEYnl2vYBDZzQUmkqMVeVAiMBv3UluezNHkGRj7oc-yxCSZnFIDSJW5hwDf9Sksrs_fZxrqbaCxrSSREIM8Nvs9d9eqIVDBEW3JM2N9hpy3Pl-DNvvDm0eWmyXMyOawRVoUvmNjF4LEt8DwWC67sqEIFgb3zdpg9q8u2NzFJWl32Lkjbpo4ey9_dfcsESw3DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاآرتص:توافق ترامپ با ایران؛ رؤیایی که نتانیاهو در ۲۰۱۸ داشت، حالا به کابوس جهان در ۲۰۲۶ تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/122895" target="_blank">📅 21:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دولت ترامپ در حال پیشبرد طرحی است که بر اساس آن، پلوتونیوم درجه تسلیحاتی دوران جنگ سرد از کلاهک‌های هسته‌ای منهدم شده را به شرکت‌های خصوصی که قصد تبدیل آن به سوخت برای راکتورهای هسته‌ای را دارند، ارائه دهد، گزارش نیویورک تایمز.
🔴
اگر نهایی شود، این نخستین بار خواهد بود که وزارت انرژی پلوتونیوم مازاد تسلیحاتی را در اختیار شرکت‌های خصوصی قرار می‌دهد. این وزارتخانه در حال حاضر بیش از ۵۰ تن پلوتونیوم اضافی دارد که قبلاً برای رقیق‌سازی و دفن برنامه‌ریزی شده بود.
🔴
حامیان این طرح، از جمله اوکلو و نیوکلیو، استدلال می‌کنند که تبدیل این ماده به سوخت راکتور، راه‌حلی کوتاه‌مدت برای کمبود سوخت فراهم می‌کند، در حالی که ایالات متحده به دنبال گسترش ظرفیت انرژی هسته‌ای است.
🔴
این پیشنهاد نگرانی‌هایی را در میان کارشناسان عدم اشاعه ایجاد کرده و جزئیات مربوط به امنیت، انتقال و ترتیبات دست‌کاری هنوز در حال مذاکره است.
🔴
شرکت‌هایی که برای مذاکرات پیشرفته تحت برنامه استفاده از پلوتونیوم مازاد انتخاب شده‌اند شامل اوکلو، استاندارد نوکلیر، اگزودیس انرژی، شاین تکنولوژیز و فلیب انرژی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/122894" target="_blank">📅 21:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122893">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: در گفت‌وگو با رهبران ۸ کشور مسلمان اظهار امیدواری کردم که خداوند قلوب ما مسلمانان را به‌هم نزدیک‌تر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/122893" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اتحادیه اروپا و کشورهای آلمان، نروژ و هلند روز سه‌شنبه پس از تشدید حملات روسیه به اوکراین، سفرای روس را احضار کردند.
🔴
به گزارش رویترز، سفارت روسیه در آلمان اعتراض اتحادیه اروپا به این وضعیت را رد کرد و گفت که مسکو در حال انجام «حملات دقیق» به اهداف نظامی در اوکراین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/122892" target="_blank">📅 21:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نیویورک تایمز: ایران با چندین پهپاد انتحاری به چند ناو آمریکایی که از سمت دریای عمان، قصد ورود به تتگه هرمز را داشتند حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/122891" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1ZBF-8BM069CtELh47je4mngO0xEDMRVEFTVQYpxCdCvBI0n-VELtQ0U7HkdFzyy99h1eIwoYrmcJeVH0zxn-dqKbkoXHaaS2-vB-_iDJ2qwqV0ZN1YpjhkklbHFUl1wLYBUorTSyNGkqcGKUzk8l7IQmhaPTetdkRLKI2cQ-0aa7e3sQmgaqzl4hvMpRq-MDn0JI-Yljn-TkVFHpVPwguzgjKZgdVCKEmCcSomj5LZfkBT11JV_GAhbuKprTo8MnFyn6hd8ZS9qW7WvWTkuRwunb4ddN6I26jATCERFZZEcoS11FXwSp7NuqGQIkgZckIp6EDBleytkXNhtp-qYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/122890" target="_blank">📅 21:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یه مقام اسرائیلی به شبکه ۱۴ اسرائیل :
آمریکا فعلاً جلوی ترورهای هدفمند تو بیروت رو نگرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/122889" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">طبق رصد اطلاعاتی واحدهای SIGINT و CYBINT جمهوری اسلامی ایران، حجم عظیمی از ترافیک داده از سمت ایران به سوی سرزمین‌های اشغالی رصد شده.
ظاهرا نیروهای داخلی موساد پس از وصل شدن اینترنت به سرعت درحال آپلود اطلاعات جمع‌آوری شده خود برای موساد هستند؛ طبق این گزارش، افسران موساد تا این لحظه به دلیل قطع بودن اینترنت توان چنین کاری را نداشته و ۲۰۰ هزار نیز پول ته جیبشان نبوده کانفیگ بخرند و امنیت ملی را تهدید کنند.
از این تریبون خواهان قطع شدن مجدد نت و برقراری امنیت ملی هستیم تا یوقت نکند دشمن روی ما اشراف پیدا کند...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/122888" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqP__aEnA9hVCRSIftW0cyMd6hAckaMD3kLepkBnNn3BqH-1KcYd8a8fRIQoDR5ypAPmzgeIe1xGPU-1zQcFbzTZBqYlsZT9AtRPbIyAgYwQojHY_rHo3xFIugekd9Dwed42By8qqvtU_sG6J7XZPZsPNlaqg5a4UTi1-tZKcWk-q7MwGOHZJ8lVB1sut4s9nu7pebiCtoH6LhD5QAg_OsDrWz8XnVsnm8eW1K8I5DWHbqxv-H3oUH6TOL26sCVYuul5pqM0GH0LH5rdJUinJR3gmOG6r131szi17_nPcr5XY7q5wDMz0jrBDD0n_elyBERhnRgjpcbDWYbK5wpa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما شروع کرده به صورت رگباری داره گزارش میده که اینترنت نباید وصل می‌شده و اشتباهه
🔴
حتی به عارف که گفته بود به‌خاطر یه راننده نباید اتوبان رو بست تیکه انداخت و گفت اتوبان قبلش باید ساماندهی بشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/122887" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی در گفتگو با کانال ۱۴: حمله به ایران پس از دریافت «پیام مشخصی» از ایالات متحده، در این مرحله از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/122886" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صدا و سیما شروع کرده به صورت رگباری داره گزارش میده که اینترنت نباید وصل می‌شده و اشتباهه
🔴
حتی به عارف که گفته بود به‌خاطر یه راننده نباید اتوبان رو بست تیکه انداخت و گفت اتوبان قبلش باید ساماندهی بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/122885" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل دستورهای جدید تخلیه اجباری برای چندین شهر در سراسر جنوب لبنان صادر کرده‌اند:
🔴
— خیرابت سلم
🔴
— بیر السناسیل، قابریخا
🔴
— مجدل سلم
🔴
— قالاویه
🔴
— کفر دونین
🔴
— تولین
🔴
— ساوانا
🔴
— صلعا (صور)
🔴
— برج قالاویه
🔴
— جبیشیت
🔴
— القصیبہ (نبطیه)
🔴
— فرون
🔴
— ابیا
🔴
— دیر کیفه
🔴
— کفر سعیر
🔴
— صریفا
🔴
— الغندوریه
🔴
— النفخیه
🔴
— ققیات الجسر
🔴
— عدشیت الشقیف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/122884" target="_blank">📅 20:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH6sm4C2ciDLxid-CVYiRZ6u4jkL4YlcLE1QJHfc2QhgLORvPKJyFMVIFXfN7TjebF8SIt-Z6bqlTk1BiGQxgeL01T8SYAdhxZs0JYOi2XAoK_qILYUsrClNtCIL3I1Ngcq56ZgzVJqlPZdeVtqo2sPjMO6tQhxCqAdRJd2bhtxWIzbM9fuo69A_29dIBYFp4Xe8o2RaKb3aPiTJGvnfGpHgAuFJFNWZDr1LDVCItWtYZDPUUuPBqcUUUoKHGKl_fXbpQljVwYcn462FxjgZVx2xI_a7bLY5wisezKQ9XO6vV_t-ntoyqzmvra1wRWlgrrdhGRyANCcH_d30TB5hUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا وقتی می‌نويسن خوشحالیم که همتون وصل شدین
❤️
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/122883" target="_blank">📅 20:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ادعای عبدالخالق عبدالله مشاور سابق بن زاید و از چهره‌های بانفوذ امارات: امارات گام‌هایی محتاطانه و حساب‌شده را برای کاهش تنش با ایران برداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/122882" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QD-bwU8qvlYEv9mwA9CA4pBYJikj6bzLLW1q8varqcKXxFk_r4WRPHf4bjKA0nTC9CIU27BCxKgJdLTuenuV4SjQvf0p1PTH1mxlkcVLwDxKwUQ1NHTENw0s44aWemLj7tLnRrVO6khFaBqUuovDVoCamZrYj0wfKqOnZiEX1vwgaS3TVSd581__ZePu_w5ht1dAgj9bzF5T2JubY8_GnGg-RdoiV-tmFthCfqvMo7NwoRax64xT5fjPb1Vx1rUPueyRL0UxxMVegkK_uWCsC1XyEJ8SJT77jZQqqaCc-n0nq8Z2EK6Yflxz3RtHGCQT4YnKGJXrO6SEuX7eNCO5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ViJvvab1nYl9X2z4405-pKRDOiF07_pCVlbqW0K1aCVS_VD0S0DJBWOCkF4qcesTULhSaWgfY8-pHm2j3En4vmqMBmHt-BYxROIuLCCAd8AtXSZNujgH6y8d_prKkQDXbM769jPOL1Seuvw8zhAV-o2ib3TPUGvKuIAh75DkQMgdN9egjL5QesTjpobrn1QZFT43ynszbILX-B7WEWsqcP3DdaqqnIpwzhOjgb8PCDsT0nye6exIPxhv4Z8KdhpdeI4OgP7e6dEcO6dmkuip1xVyjxT8M44h8COxumUNSJQX0rTayRJjyQqJYtk01M2Fj0oYM3STwCvHFHsSGjt9_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعتی پیش بورس آمریکا و بازار کریپتو به صورت غیرطبیعی با ریزش شدیدی رو به رو شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/122880" target="_blank">📅 20:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کانال ۱۴ عبری: برآوردهایی در اسرائیل وجود دارد که توافق با ایران تقریباً به طور حتم لبنان را نیز در بر خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/122879" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا به اسرائیل نسبت به حمله به هر شکل به بیروت هشدار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/122878" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خوش آمد میگم به رفقایی که تازه وصل شدن</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/122877" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/122876" target="_blank">📅 20:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/122875" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دفتر امیری قطر: امیر قطر در تماس با رئیس‌جمهور ایران درباره تلاش‌ها برای کاهش تنش و حفظ امنیت منطقه گفت‌وگو کرد
🔴
امیر قطر بر لزوم دور نگه داشتن منطقه از پیامدهای تنش و اهمیت راهکارهای مسالمت‌آمیز تأکید کرد.
🔴
امیر قطر بر موضع ثابت خود مبنی بر اولویت دادن به راهکارهای سیاسی و دیپلماتیک تأکید نمود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/122874" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
معاون وزیر ارتباطات: سيستم عامل، مرورگر، آنتی‌ویروس، اپلیکیشن‌های بانکی و ابزارهای امنیتی خود را بروزرسانی کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/122873" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به الحدث گفت:
ایران در طول دوره مذاکرات خواستار آزادسازی دارایی‌های مسدود شده خود که حدود ۲۴ میلیارد دلار تخمین زده می‌شود، شد.
🔴
ایران اصرار داشت که نیمی دیگر از دارایی‌های مسدود شده خود را ظرف ۶۰ روز دریافت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/122872" target="_blank">📅 20:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما عملیات خود را در لبنان تشدید می‌کنیم. نیروهای دفاعی اسرائیل با نیروهای زمینی قابل توجهی فعالیت می‌کنند و موقعیت‌های استراتژیک را تأمین می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/122871" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKJVh1zd24r3NhF9Nhyuw6Vd-JRaK5BN_F5EdzSHne2UbWJOTOKClbvtOt_nKHp-ZVpI8cE4xXIPN4c64JFCyYynmKl_qo37hl1w_qUay3sxl1GsrtLpgNsPLqCxwhP5Ev7yXMvHi5SjIdIkHPX9d8OJQdiU6cpkIp1e0B9wbA1yN6_o4u24qTgPsQ1Ao-E_y4_Mq4zCEAKiJ_mRlFmyvNBEKpPCXbaAESLPoRhfYo5OyERKRihGPrg4cZqc2EviQRwY88RycnG-m_k8UwFWGnpYfIWHeti5VxL9A3JB9BonYF0XK2KMyiZ67hdyJTglVJOPxuv3b9ayr69xhoD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
تازه معاینه ۶ ماهه‌ام را در مرکز پزشکی نظامی والتر رید تمام کردم. همه چیز کاملاً عالی بود.
🔴
از پزشکان و کارکنان عالی تشکر می‌کنم! به سمت کاخ سفید برمی‌گردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/122870" target="_blank">📅 20:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122869">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKSJaUBTPxg2kc-MuodO3QEie6Whs7fy1S9lQdJ8qIAqJ0DCIfUSkltVeIcX4Dt5gdsbCwFoZ1rdsiMBXVNkTP75ZJRCx1PTFG3A7VAzC44mvC5XW7mG_2-u2rbRW9rct-w8svRPLMD_F9hd8BzwNLC_eJ8N9SzYP1aJ55bFbD5rNki4Jsx7tuEF78QmNTsjjE-Rhp4tG2axwGDnEo3gOqlWaOlHCSNXtZcLgS193GxW78TLgexeVMzD4MKaqH1Jdw6qZk6V1n7ZKlMGT6OOmKYjdxOrbs48cAvIuSHT9Fmr3EywZkraoaQY8ubhpZwJxQOcUPwNjKSmekExBRbrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : پروژه «آزادی» از سر گرفته نشده و نیروهای آمریکا فعلاً هیچ کشتی تجاری‌ای رو از تنگه هرمز اسکورت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/122869" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122868">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره به نقل از یک مقام آمریکایی:
گزارش‌ها درباره ازسرگیری اسکورت کشتی‌های تجاری در تنگه هرمز توسط نیروهای آمریکایی دقیق نیست
🔴
نیروهای آمریکایی در حال حاضر با محموله‌های دریایی تجاری در تنگه هرمز همراهی نمی‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/122868" target="_blank">📅 20:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/122867" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
واکنش سخنگوی دولت به اتصال اینترنت بین‌الملل
🔴
تفاوت نگاه‌ها، در بزنگاه تصمیم‌ها روشن‌تر از همیشه دیده می‌شود.
🔴
با دستور رئیس‌جمهور محترم، روند بازگشایی و تسهیل دسترسی به اینترنت آغاز شد؛ اقدامی در جهت پاسخ به مطالبات مردم، حمایت از کسب‌وکارهای دیجیتال و توسعه خدمات هوشمند؛ مسیری که دولت چهاردهم از ابتدا بر آن تأکید داشته و دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/122866" target="_blank">📅 19:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رابرت اف کندی، وزیر بهداشت آمریکا، ویدیویی تو اینستاگرام منتشر کرده که توش با دست خالی دو
مار سیاه
رو می‌گیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/122865" target="_blank">📅 19:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحشت در فرودگاه بین‌المللی کمپگودا؛ خروج اضطراری مسافران هواپیما
🔴
پس از آنکه مشاهده دود در هواپیمای ایندیگو در هند، وحشت برای مدتی کوتاه فرودگاه بین‌المللی کمپگودا در بنگلور را فرا گرفت.
🔴
مسافران هواپیمای شرکت ایندیگو بلافاصله به صورت اضطراری از هواپیما خارج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/122864" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
