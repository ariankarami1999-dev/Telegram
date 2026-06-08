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
<img src="https://cdn4.telesco.pe/file/BHz2rOn3dNwbhVZO33DX8ri94Fc-n1txl5Va6dOPTB_LGCTp2BMYGuglrR9_R370npXe0YoPVhJ3h7S-Q-ILsymc42LD_o34x6f4HDh4lJkIS2QkS2PWHMvBfshOXvutBiicdb29TVJl87-QR9-11umtpov5LzcZJpfIb-Xp1c7PtXgOVSueLg8qihBlmDDGKEmQaJ0mR970RXyuAAfS9ho7p8b78vN9IJPmNSygaRTDOqH50RhuQbXRGJ8Z7YaqIVg9cyAqFKuj3r6Vc0oxVIijg0G-3_-1Yw0HRpL3UzSUHp6_lF8yzoN4Eha3CaYStRCCrG2-ZN7yVGI3b-elwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 303K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-14028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/14028" target="_blank">📅 16:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=bRPekXh2J6tz6U7myPSkE6XKr9V_8hfu6FRbLy9hrWui1S-kgqcnViJUDD4uETrENb_6jaQWk_cjwZ4Xvbdk8X6FNnNYjErYi8LVkAtaVf2goSvE46H0rAtUwixxZZ1sWuYZgZKUM2J_sNfXoIyhQIQ_Dbak8vNbUe6UiM3PM6N6NKKxqCHJKBDyHv3NE5IvDldR_c1zcqMojUnvXRM8f3pS2jdZlzJ_wuqjvcA3P6cE2TXC1RgFysPojg2l003zKMszi6Rf_wR5HybA9dy8RGaYwUwDoPESdjJyRmqhhgJk0iuEcGqvpw_dvn-ujvCLKzvz9cc5U48miLd-u6CaEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=bRPekXh2J6tz6U7myPSkE6XKr9V_8hfu6FRbLy9hrWui1S-kgqcnViJUDD4uETrENb_6jaQWk_cjwZ4Xvbdk8X6FNnNYjErYi8LVkAtaVf2goSvE46H0rAtUwixxZZ1sWuYZgZKUM2J_sNfXoIyhQIQ_Dbak8vNbUe6UiM3PM6N6NKKxqCHJKBDyHv3NE5IvDldR_c1zcqMojUnvXRM8f3pS2jdZlzJ_wuqjvcA3P6cE2TXC1RgFysPojg2l003zKMszi6Rf_wR5HybA9dy8RGaYwUwDoPESdjJyRmqhhgJk0iuEcGqvpw_dvn-ujvCLKzvz9cc5U48miLd-u6CaEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر
⚠️
اگه ناراحتی قلبی دارید نبینید
🤣
بی اختیاری ادرار میاره
این ویدئو رو صدا و سیما خودشون پخش کرد!
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی برای تنگه هرکز
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/14027" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بریتانیا هشدار تخلیه به شهروندانش از اسراییل رو صادر کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/14026" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUtHQQUT9NVVRuTP5Ec_l5mNGEuMzCmPRzy5-7EERQrFJwkCtGNYDqhY3-r-0MmikWgp4_x-ggiMQ-qhWoR6ak0VhdpW-gXU6xFURcBBmtsN7AOClxENlg-6lLhPM_WEYooNO34TdHklqS0FIKGtQVq9VTN7XflE9TWw3CZSkT7aGNKIwuZWLOgDGbSWVGKH-h5V2F2gg0fbgHU-p0WtEsDSZAnbHYcCtARHdJWg9-PAyz-tcmkrge1vcLEVNEsWPFMusyBxcCyr2cNm8dWf5_Vpvo_SerAIUxiuZ0tqvJf9sr0vrmLakDq7FSv4SeIQ9pFQGuh225PKZTuaVC1rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هم داره جنوب لبنان رو خیلی شیک و مجلسی هوایی میزنه.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/14025" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/14024" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترافیک سنگین در محورهای چالوس و هراز
@withyashar
خوش بگذره به هم وطنام
❤️‍🩹
جای‌منو خالی کنید</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/14023" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14022" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9eAXmbs87hMtPl30hgkclBjwSAXpq1iIq7Y3s6jvtqIYjz8C20jsg1j8490aaIgUIy9968BOwgirtpuZyL72pSvt5EXZawe5z6IjCgcn-ndiODt7QoBfYCx-ONvHzskLz4LPE-71-mPnRVWKYypooOzixHJZU-1iS4HYreb3CzU29_hIK7PBWBFKl0P9gSyV1SdTHbe-Zr0bM86Jn2W25W2DrWbU1JRzuZwxv2WPlShha75wicDLTmQ-Fawe7ZB8oey2Ou1NLWvDU44avOTWGL03339wk2zlZkgDnjopeC3OjHeLFtNpTFS5aTdEqvx4PkQ6LhNNP4wGD8HLQ3cCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/14021" target="_blank">📅 16:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14020" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حزب‌الله هم حمله موشکی کرد به سمت اسرائیل و آژیرها فعال شد.
اسرائیل : 5 موشک رهگیری شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14019" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
تماس تلفنی ترامپ با نتانیاهو «مودبانه» بوده، اما نتانیاهو با درخواست ترامپ برای توقف اقدامات بیشتر مخالفت کرده.
به نتانیاهو صراحتا گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت نکرد و از آنها حمایت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14018" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراق از بازگشایی حریم هوایی خود خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14017" target="_blank">📅 15:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال 12 اسرائیل: ترامپ و نتانیاهو دقایقی پیش صحبت کردن.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14016" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هم اکنون اسرائیل به لبنان حملهِ کرد
@withyashar
😁</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14015" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدا و سیما:جنگ پس از شکست دشمن به پایان رسید و زندگی به روال عادی بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14014" target="_blank">📅 15:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تحلیل کمی دیگه در‌اینستاگرام پست میشه</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14013" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14012" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=KeEEuVwzqDennR11slOvCQUPxmTTvm5g_zW8iAychaefUNEr_D877aYl469riho_jL-rP-FIDO-axxK2UbvXuB_iWyjVhrXCcvzkHjwTkfM_RRY0txp-HUzeCCqfh4HWRYyWwKmKzEUxctq1wUKKf0-nHPOTIxZXJ9TN9GRcoAjtAk6TtdF0KfgJ6AUecikZFHZsIdpZLoXNbfEmE44X-UKMkwmZtAdB-QSq91Py6wuZPxm4AbqZRwc-S7NjvIKr3q_23s0JD8I3PKsXEUMMDl5XGrO8K2btCXqTYMh1UTPzDFXKi87wFQNugcwg1StweP6jjdWF-lt6dGLFAFrBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=KeEEuVwzqDennR11slOvCQUPxmTTvm5g_zW8iAychaefUNEr_D877aYl469riho_jL-rP-FIDO-axxK2UbvXuB_iWyjVhrXCcvzkHjwTkfM_RRY0txp-HUzeCCqfh4HWRYyWwKmKzEUxctq1wUKKf0-nHPOTIxZXJ9TN9GRcoAjtAk6TtdF0KfgJ6AUecikZFHZsIdpZLoXNbfEmE44X-UKMkwmZtAdB-QSq91Py6wuZPxm4AbqZRwc-S7NjvIKr3q_23s0JD8I3PKsXEUMMDl5XGrO8K2btCXqTYMh1UTPzDFXKi87wFQNugcwg1StweP6jjdWF-lt6dGLFAFrBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14011" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14010" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیهش نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14008" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل : ما سیستم‌های پدافند هوایی رژیم تروریستی جمهوری اسلامی در غرب و مرکز ایران را نابود کردیم
‏پس از حمله، انفجارهای ثانویه‌ای شناسایی شد که نشان می‌داد موشک‌ها در پرتابگر بوده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14007" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان کرج سمت میدان استاندارد و فردیس
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14006" target="_blank">📅 14:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14005" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر آموزش و پرورش اسرائیل: تعطیلی مدارس فردا سه‌شنبه نیز ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14004" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار I24News خطاب به پست رئیس جمهور ترامپ:
من واقعاً نمی‌دانم این مذاکره درباره چیست
این مذاکرات به مدت یک هفته و نیم به دلیل لجاجت ایرانی‌ها متوقف شده است. پیام‌های ترامپ هر روز خجالت‌آورتر می‌شوند
و تا جایی که می‌دانم، اسرائیل خواستار آتش‌بس فوری نیست
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14003" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcEJyyrNmcse30ytnETLJR8U2LJucwAee-xMAJS8DhrU4Fw7vBG4aMfgKNkZlbcsMHcOCV5PJpH-dG1mWLQ7e1VaNRU3I2ulfgMva8VUxyt3zOnaQntrzQv0y70PXbVRLcULMnLlHA9-X4cED--1t3M43oHPXNkZOJfU0gTay0I29pemygOKeqwrVOC__I4TZqm5syCkTWFddRCSDcpbX6Vi8hnFVg6Abf0O5nSqIhtdmWWvVFzbRit0SlioPKy3XnGXu6HBsqzCfbUvgQnf__ZlTik2yO74_kXT5El3WCAKw9Ay1JuiG_SRd2AXqCph8AvwC0iPpaepIZhPMiQH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14001" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8r3D60-kghPLzPWiOE-rlaH7V03yMJyPuAnbMYO_PHg4DXXZ1h90EeZ8eB-54j4MnYklEXN7fF7jQIbMFVyOfF0lxK6Ra_eDKlDJLFsZ9GY9tTfjzeXzDzfci7KNb8dZLSNsx_C_Le1XmH_A-7jdgGeSoOB4KTCTGs2CRF6Mx3_Q122d8dpvTJLCW0424ybDKVFGgnKC58oTn2w4ygFpHC8EYHReJp2Ocs7IeI-YFFwROcpKkI7DiYhQV2d4ZE-205q7M6UkshFPruIvSJPJ_CzOnCGlmQvqLpq7YQBhiOVpa7ZUzbOHG2INXPy5QiBbrAp-BrZMKgzBGkwVXNS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود از انفجار در شیراز، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14000" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانه های رژیم : پدافند یزد فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13999" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13998" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلیه
@withyashar
🥴</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/13997" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب ساعت 9 به وقت اسرائیل تشکیل جلسه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13996" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرپرست سرکنسولگری ایران در کربلا: هماهنگی‌های لازم با عراق جهت انتقال حجاج انجام شده است
@withyashar
حجاجی که نیومده بودن باید برن عراق زمینی‌ بیان</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13995" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13994" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034343a08d.mp4?token=TQulKsovpCHnZG0K8JwVO6t0BcxYegk2Bi_xVQYMZRcIehv1b6V32IlMtfR_TQNkx-10cl2YVCAAr-f7EsUVf5Xnh_996B8lmt-MbijFAeLELuQpm9SVcIIBR3OzUS1LtRsNXG3C4ZZmILAabII-3_yL4sXRqMMrST5Vo-KNFAWlXROXtPSB3sNDd4W9a00iUiKJHSRZJjBEfvnSR4_jkiWxf_CxEvWxJW9bxOT2PL7Fc7vCBT_0sImMboFBxI1UcjwT634W7MAnc2PqMu-l0TboCgaO8OXXxdPorVQxlmPakfo-iJgP1WIrcmRoAP3enswrEeBv2RVeHVfts3nVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034343a08d.mp4?token=TQulKsovpCHnZG0K8JwVO6t0BcxYegk2Bi_xVQYMZRcIehv1b6V32IlMtfR_TQNkx-10cl2YVCAAr-f7EsUVf5Xnh_996B8lmt-MbijFAeLELuQpm9SVcIIBR3OzUS1LtRsNXG3C4ZZmILAabII-3_yL4sXRqMMrST5Vo-KNFAWlXROXtPSB3sNDd4W9a00iUiKJHSRZJjBEfvnSR4_jkiWxf_CxEvWxJW9bxOT2PL7Fc7vCBT_0sImMboFBxI1UcjwT634W7MAnc2PqMu-l0TboCgaO8OXXxdPorVQxlmPakfo-iJgP1WIrcmRoAP3enswrEeBv2RVeHVfts3nVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش السیسی محموت احمدی‌نژاد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13993" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYihxtfY8hIB7CCL_5btaQYLqnRclSTCqkDFCusxTLq0fQm51gYVWTjrixoY4m0eD2Z9-fxVUbQnqyKNWlXnyP8cHGZT1UVcOOacSNLAH_9tIiEM7QxojrMSZqPd9FAu5pEXx2O0g17rWQACHwk7sQxkm2vkpey0b5MwOjDC1qfloozaiPoXg19NDah5Klqgqda_H8ff14FJV7dwW2q-tG6f7ENUUtt0bWRxDeRoFeADCu37p2jwC25VUfw2wF32ExUlfVwmG7rQBNrsq3rK6XI1YgYg2zbGv6nBE80th3H2eH2aoulOgQTRIRMzGuuRTN-PP_HZkGSjmDL9yxAIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به سایت موشکی تنگه کنشت کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13992" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13991">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13991" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه های عبری: درگیری ها تا ساعات آینده گسترده و سنگین‌تر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13990" target="_blank">📅 13:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنقلات خود را آماده کنید</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13989" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک منبع ارشد نظامی در ایران: حزب‌الله  روزهای آینده نشان خواهد داد که محاسبات اسرائیلی‌ها و آمریکایی‌ها همیشه اشتباه است، و ایران ثابت کرده که دوستان خود را رها نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13988" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس: تو غرب تهران پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13987" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ با لهجه استانبلی
🤣
:
📿
الله لله</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13986" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13985" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13984" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسافران محترم قاهره لطفا آرامش خود را حفظ کنید دایرکت جای  فحش‌به ترامپ نیست از مسیر لذت ببرید
🙌🏾
😁
مدیریت حمام اتاق جنگ</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13983" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">همکنون دو تا از رادار های بیدگنه رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13982" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnlinbLapf5E_CP0oS2MJCgHqkbPaq4Xi2G3OV0AuyJJVLffTu8aH2pO8TQPM54NuGxCgCtPr9zHeGk-hDqCINfawAOueWd5gv8WF6K6HfLVHOM-EDy0e_E6stdSd9TA_bKoNTWgIpFWVuuvuM8-a2xWLDRqe75IZbR2nXqD7Oh_ORq1tNW1s5glNFfn6sAiB_T7NZs2gnq2ClBzyUJxktMA9LHiNwIwOYILPaaKMNFOxyX9yvBZ8O_eqFaSU-094DIfOxMK8omvAPh42Ccown0BQySS3HU-8sTv2BVXNe3gI0dev05OW73iRvYbGEm9qmesQ9rdGT3Dv0MC2oj9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13981" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کابینه امنیتی اسرائیل ساعت یازده و نیم پیش‌ازظهر دوشنبه به ریاست بنیامین نتانیاهو تشکیل جلسه می‌دهد.
این مقامات همچنین گفته‌اند هر حمله موشکی ایران به اسرائیل «با حمله در ضاحیه» در لبنان نیز روبه‌رو خواهد شد.
وزیران راستگرای افراطی در دولت نتانیاهو به او گفته بودند در پاسخ به حمله موشکی ایران به اسرائیل، «تهران باید بسوزد».
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13980" target="_blank">📅 13:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش اسرائیل: برای احتمال شلیک موشک از سوی حزب‌الله به خاک اسرائیل آماده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13979" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک منبع آگاه در حوزه ارتباطات به سیتنا اعلام کرد که تاکنون هیچ دستور، ابلاغ یا تصمیمی درباره قطع یا محدودسازی اینترنت بین‌الملل به دستگاه‌های مسئول اعلام نشده است، در همین حال شب گذشته پیک ترافیک اینترنت بعد از قطعی‌ها زده شد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13978" target="_blank">📅 13:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان ملل از شرایط موجود ابراز نگرانی کرد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13977" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال 12 اسرائیل: ارتش اسرائیل در حال آماده شدن برای احتمال جنگ طولانی با ایران در حالی که عملیات "غرش شیران" ادامه دارد همچنین در حال حاضر اهداف جدیدی نیز مشخص شده است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13976" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تاکنون، ایران بین ۲۲ تا ۲۴ موشک به سمت اسرائیل شلیک کرده است
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13975" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13974" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رادیو ارتش اسرائیل: در حمله به حومه جنوبی بیروت تردید نخواهیم کرد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13973" target="_blank">📅 12:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فوری رئیس ستاد مشترک کانفیگ فروشان به ادمیرال یاشار رئیس اتاق جنگ گفت :
آماده‌ایم تا به هرگونه قطعی اینترنت پاسخ‌ کوبنده بدهیم
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13972" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینترنشنال با استناد به ارتباطات زیرپوستیش : ارتباط مقامات و فرماندهان با مجتبی خامنه ای دچار اختلال شده.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13971" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldS3M0YejUfWpX-u-M57TNMR3Gdzr817xT4TZVSCsNKD2xrUB1wzQ9rDhCVZ2z-vYFWPc0AO6MItFSLO_dS5kbupGFJf5RZzZslKM8uxLSOq5OzTb5p9IHtAM19aU4Y6Dhhk6-2G5xQLqhVe60skYz_YMK64FJHzWOyr9JQDtOi9qPsrnOEkIcJ7NsIM2GzimYoLcCC8ZOt81RipsCeGG_9T0aCEsxx0MDsXv5vC1lody2C5weZWFZkzsEeylVRixVr3hK1Q3qLMn_cZ-911G2q0Hca1qJjZyYv1aSkIOnUY7UVLcXlct_D4ao_blwMhdBqQuWVv29FFE6L0C-Pr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش ایران موشک به سمت اسرائیل پرتاب کرد که گویا وسط دریا خورده
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13970" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگه تازه بیدار شدی بدون که آتش بس آمریکا و ایران همچنان پا برجا است
🥴
🤣
@withyashar
ترامپ هم کابل رو گرفته و پستهای انتخابات میزاره…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13969" target="_blank">📅 12:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تن و بدن عرزشیها داره تو دایرکتها میلرزه و چرتو پرته که مینویسن
😁
. اینها به هیچ وجه فکر نمیکردن که دوباره حمله شکل بگیره.
@withyashar
با عرزشی سوز ترین رسانه نسل شیک پاسارگادی با شما هستم.
✌🏾</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13968" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ارتش اسرائیل گزارش می‌دهد که حملات به ایران تنها توسط اسرائیل انجام شده است و هیچ مشارکتی از سوی آمریکا نبوده است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13967" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دایرکت پر شده از مسیج‌هایی که چرا نمیشه تو چنل عضو شد. من اون سمت توی گوشی شما نیستم این علت رو بدونم ولی محتمل‌ترین حالت لیمیت شدن شما به علت استفاده از فیلتر شکنه ، اگر IP تون رو یا ساده بگم فیلتر شکنتون رو عوض کنین این مشکل حتماً حل میشود.</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13966" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسانه های رژیم: خبر ترور فرماندهان یا مسئولان کذب است؛ هیچ تروری تاکنون انجام نشده است
@withyashar
یاشار : حالا نیس اینا خیلی گردنم میگیرن !
🤣
اول همیشه اسرائیل اعلام کرده</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13965" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روسیا الیوم نوشت: ترامپ به پیاده کردن نیروهای ویژه در ایران تهدید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13964" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرهایی پخش شده از حمله به ایست بازرسی ولی هیچ گزارش مردمی در این رابطه به دستم نرسیده. به نظر من این خبر فیک برای توجه یا امید واهی است، فعلاً! ولی حتماً شروع و انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13963" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صدای جنگنده مرکز تهران
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13962" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13961">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13961" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13960">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=ZaSzdI6dpWlezAWY1ZdUo0CJdBoD96E2UJY-l_6GjFAb43tmXF7RVVvYC9EHJq502IF5P050Ml5SZlWqoY4axcS7_Jl0YJ5SG_kpsiW-62KdG6wLldCStd6eB8EYejql4ap070sERIR2SWp9kNLKMP-k4Fm2KNn8E5f93xlGRM7qvSKVk80xTc5jISrj4dlEkSU5n7xMyVTd7EkIbUwk29pDDEErzfJW_6dmoLmvXDq2Rm5e40cBXT4_cmVT64lE8_lC218iyMg9pcQYPVV0y5eOF90XLB35BsfUVKxCzlUirAA3x4ollk_KJAYvCCDxg0at1u7V-pBkpArXfLc1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=ZaSzdI6dpWlezAWY1ZdUo0CJdBoD96E2UJY-l_6GjFAb43tmXF7RVVvYC9EHJq502IF5P050Ml5SZlWqoY4axcS7_Jl0YJ5SG_kpsiW-62KdG6wLldCStd6eB8EYejql4ap070sERIR2SWp9kNLKMP-k4Fm2KNn8E5f93xlGRM7qvSKVk80xTc5jISrj4dlEkSU5n7xMyVTd7EkIbUwk29pDDEErzfJW_6dmoLmvXDq2Rm5e40cBXT4_cmVT64lE8_lC218iyMg9pcQYPVV0y5eOF90XLB35BsfUVKxCzlUirAA3x4ollk_KJAYvCCDxg0at1u7V-pBkpArXfLc1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پایگاه عظیم کوه معروف یزد الان شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13960" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه سر برم بیت رهبری الان میام
🥴
🙌🏾</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13959" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13958">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شهرداری تهران جنگ بیخ داره و داریم پارکینگ‌های زیرسطحیو برای استفاده به عنوان پناهگاه آماده میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13958" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13957">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfjmF6bqjcceSCzvqU7rjUDDfFIJeAKBk53np6GNEYaKv7khsNtVg1DcBZwaA4ujtAJnBiOxHyhKQqvT8gIazPziq-NlprqJ_1m8N3QkZJXOaUYDdvd0F5e77aWtVQHbf0gerAEHWJbxCm7rf2KRop0dgPbZByr2tdnh9A0cEdj49e4_C-iLPpa2zD7aoaISAX5K6JQlClRn5XQNoptaX-HnR7isUH-nb-mCO08w7iSWONC4_-46jVFtKQMPq8psML1JSwSr46qxU9uOF6_XPxdmOcvmVJ-RgtV85xLJ-Oe0cOKF6pWdKHy5yAjVWQFWuYCcXXGGZO9mYUHWyt5PyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰،۰۰۰ امین نفر کانال خانوم پی ام
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13957" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13956">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
گزارشهای از یک تررور هدفمند در تهران
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/13956" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJLlmqJd5OGJIDvz0cOX7vnvSrBsdTAGKol2AQcQfbYns1zc1AoVqvohIYgb5Fivd39r6OiCDcLqSylNss7hUGk0fdqiy9lmuDfkmHRyGAPKFVh5rawptdm7PysPlVHKbdu-WZA5qfKwm250f5yi6ErLkkVXc-zKN2VpxM8XRvYVdWgPi_LoegAaTCO2fwTFxIc0fn1w8pP5fREjQOCIf4RY5InsiFjDThxQ_6NAWfcBg14o86DqnUwfy-sqhg0lKDTI2FsLJl0PjG6RZ2r4tjS2YgDO92kOPCDBD9OFEBDivkgaCNUw1RIjVWpcKWMe87eY9361CUWXPbNIH9hicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دود از شرق تهران
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13955" target="_blank">📅 12:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفارت هند در تهران از شهروندان خود می‌خواهد فوراً ایران را ترک کنن
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13954" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رادیو اسرائیل: همکنون نتانیاهو ریاست جلسه‌ای کوچک از هیئت وزیران را بر عهده دارد تا درباره مسائل امنیتی و سیاسی در تمامی جبهه‌ها بحث و بررسی کند.»
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13953" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش چند انفجار در جنوب تهران
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13952" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13951">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کان نیوز عبری: نیروی هوایی درحال انجام عملیات در ایران است
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13951" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13950">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فارس: موج جدید حملات موشکی در راهه.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13950" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13949">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvUNRUUxCU4VGLL2OmQ1HC4kfOXE8LXHzocaS8tjMATvSODozjo-HTON95DSk1kmYCYJdiS7HawX7uvdvoZukb6I36HIRRHU9SEquaatUoF1hZ2Mow36N7qo2bNMo1EreHcrZXIeNnzVwSU1-8cAgIYrPKoGpJzDubavoxflOr0N3gQ4gkwaHGDj8is11QOAA69bPzSo8akiOgWelVTtU9B33vxnyXXIwlVo7wK3hBOBCm4r5HouzK_PF31fuWdKvm89XV_caLX7Ekbl-rwvNxeb3dtbDqZ8zCBQKVzzSRraNZ6uxCmtuVKHIBVGr0S8Hn9-8r7zOFxmxR8Dyy01dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان الان
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13949" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشات از انفجار در فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13948" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13947">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh_TNQzlc_rmmfbzseQhBGpXUTsdIalrL1r8f6y6VCoNbllZm0TG74QmgD0QTt0v0EdgCNBFmLvNRTjr-x21VYH4DfJojmDWbQ0Zswlx7jYy2KbYf73FEtpBKxeeDA_YSZvcjctHTMEv6le0fNiHMjWSK0yKacxH30F--ZflWOnCxL1MklaIUZqO_L3wvWGpc1r_a0_jL9gZlvEk9Lzx_xMuFVbd8kdK9_4wTbGOb4oON90vhkTBw4AJBJEJm4MmmbMaeBFYe87ScYx-FLq8HhNR1n7iHek4SKSc6UnrMg8KJ1rDxuOf3DpKGyPt5d3i0_myNOsKQMZF8ct6CEP2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران الان
@withyashar
این تصویر گویا مال راند قبلی جنگ بوده تکذیب شد</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13947" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13946">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b742c26d9a.mp4?token=hIVgkjorLaXy5s8Q6Ex87kcse-NmqKw-o8egQrIx59bDyk64TDJZZo2EPCvhkiTYdD9toja4k2puwAyBfjDKbX_Xumnu820KjLMJK3s6cHJpsvcZcRd2gI6KPqA0WqxytZQ_hemXTCahwbAvRqW2dGOBqREf0YWxXVk8VRad1_-EtX-ZtYzZ-DyETyZLNg2Lkur9oiw4y2RBxRu6hw5dda3dOuX_t1QyIYjZyAEXtD49IZSH1qPxjSSZXLJtoj3VZs6QprlFkMu6BOz8nqyrx2TA-h-_FRjDqi0UYM1rRJ6zkWCyvaoCPnkIFO55gjzNEVFgkUEF0Y8jYGDJeTRFxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b742c26d9a.mp4?token=hIVgkjorLaXy5s8Q6Ex87kcse-NmqKw-o8egQrIx59bDyk64TDJZZo2EPCvhkiTYdD9toja4k2puwAyBfjDKbX_Xumnu820KjLMJK3s6cHJpsvcZcRd2gI6KPqA0WqxytZQ_hemXTCahwbAvRqW2dGOBqREf0YWxXVk8VRad1_-EtX-ZtYzZ-DyETyZLNg2Lkur9oiw4y2RBxRu6hw5dda3dOuX_t1QyIYjZyAEXtD49IZSH1qPxjSSZXLJtoj3VZs6QprlFkMu6BOz8nqyrx2TA-h-_FRjDqi0UYM1rRJ6zkWCyvaoCPnkIFO55gjzNEVFgkUEF0Y8jYGDJeTRFxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : ما یک حمله گسترده علیه سامانه‌های پدافندی راهبردی رژیم تروریستی ایران را تکمیل کردیم
در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، در چارچوب تلاش رژیم برای بازسازی توانایی‌های شناسایی و دفاعی خود که در عملیات «غرش شیران» آسیب دیده بودند — این حمله منجر به انهدام این سامانه‌ها شد.
در عملیات «غرش شیران»، ارتش اسرائیل به‌طور عمیق به سامانه‌های پدافندی رژیم تروریستی ایران آسیب وارد کرد. حملات تکمیل‌شده به تعمیق بیشتر آزادی عمل نیروی هوایی در آسمان ایران کمک می‌کنند.
@withyashat</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13946" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13945">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pha0pCCDS0rFgyGebe6SD_tC5HJYxjmtwtcOYOALP_NgzdWP_YWOCGXZqMBkiOT5jwEj9XFCXZoCrI5ZYBvbms9tYr--A3fEEuz0_OqUBawxSNwbkpbujqgrq6fvN9cXQSAUYKaoD1fF4lIwkZ9hOPraJY2ZmRMjrYAp-R9IRSQgaQcYfcCHpbvVKpHHgKn-QfBw2ZgtYTS4ldW7l2Vt6bRDOkIm8KUeyLwxDR-rKZ6CMLMd4UOlti5fysfch437bTqkiNqP2phFzBJb4xcCqGdFwXyKNGLT9cLjHVucJnnay2juMomfA0uDMrsHFDglOzC9QbzK8XW1PjNei4MokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمس آباد تهران
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/13945" target="_blank">📅 11:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13944">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دانشگاه هوا فضای عاشورا رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13944" target="_blank">📅 11:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13943">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1fyPmIIOKa70eN5GQ63QWGmqCoVIfMnIogt2-T8pEMGuiXHRL5vuBJg4kfqLirumnt-kechhnqSgNo7CoWeiqKAOYyQ20HrHtKeK_e9QnpRNU9VP-SguyWee5Ow3Gouq7plJ6-HwtdLhk-spx-bbrTyQvkJ-7Ztp9v8ZuR8qkaPhCmE6dMALj9-nYZT4bJJtIPSVON-DTb73FU5PEU6ea6JITGOIH9FqDKPaf0DJkVr5J89jTwRiV8ZRIul_f1IPgDYMXcRg4AhQxxtWYfOCzKnmkiQN1uizyJEkj0971Wy09v-XIycYDSaA73ejnJoCUUTz1K0SSKYnYq2MzhCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار شهرری صدا انفجار اومد ۵ مین پیش فکر کنم پالایشگاه زدن ستون دود دیده میشه @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13943" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13942">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">غرب تهران مثل مرز  بوسنی و هرزوگبین شده یاشارررررر
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13942" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13941">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تبریز رو بد زدن یاشار
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13941" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یاشار اصفهان رو زدنننننن لشگر ۸ زرهی
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13940" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🥲
انرژی‌من به انگشت شما بنده</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13939" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یاشار شهرری صدا انفجار اومد ۵ مین پیش فکر کنم پالایشگاه زدن ستون دود دیده میشه
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13938" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فارس: شنیده‌شدن صدای انفجار در غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13937" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پدافند فردوسی و شرق تهران فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13936" target="_blank">📅 11:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کرج سمت بیدگنه صدای انفجار شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13935" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجار در اصفهان شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13934" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آغاز موج جدیدی از حملات هوایی به تهران
حمله به دانشگاه هوا فضای عاشورا
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13933" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار در کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13932" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13931">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13931" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13930">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پدافند تهران فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13930" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صدای انفجار در تهران و کرج شنیده شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13929" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گویا دیتاسنتر آسیاتک قطع شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13928" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
