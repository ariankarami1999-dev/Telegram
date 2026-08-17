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
<img src="https://cdn1.telesco.pe/file/bPR7OHYvHtgDquQjmRLYE2HVkSWTyGtgM61BXzLkIZiX7vlzL4aq1rZBiy5pewhcUyf-2GSGev-Ret1qs78mvy_vuImB_Xf3gbtVUhbV2edhvnPs3sMyJCn0Es9kXziU16GiiQcRhCpgwHp7qu_jahTAeoY9pONjfJtgL6_WOP6ITJk8-RgXKHRhAAMTDiazPoCCWjVxzpnXkgRo0vgGAFXvUmZrnVQl0Z6Beh_lFRm-UpRuqZeGmZLw54-DZcTn0RKoqa1k5mjRIf-kiOq9P9LFZGXU26bKLwcSZoCpbTaVcuLhDPS8vcU0vZG6tO73BErqqhkCLM18k6DTayT2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 03:13:51</div>
<hr>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbUmWi6FBIcwR0cCdVncLJ5SjeaXDIZuv96UJ_bqFHsAUwRZnGfbTyIYw5jq2pR1y3roKzCSEgF-h6eDxlix0krgC2Kf7XLVYKqA_M8U1Fc6FwAqwOvzAqbKY-1DWn8fyWPaxKZqYvSY5IOJro3dS-wVpkkVwB6xe122dvXq1r29r4WfNikrDxEZRNhq9qwqUupDBtxz-MrqJ1MN7WUrw3JfDY90QC8IcvJV1yYhk0fcW3cERQTD8pOSVQf7v6YEUPtvulpVWBZDxBZ3Af6hhZ66I0yw0gB_i_bfzABo90YBB36rfjs7wKdRVZTDKqaP5YQ_3JNGqPk4crwsKy4eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hssPo9VPqHlXrS_yrhFDseWB2CsKTk3VJzTJjeVm3xD6Sv28YodYX3bPiUl6pOl91z7Cz4KCMWkvwXm9C5oHyIBUfLI36Ateq2xq-78FuyCGEtKLfJNgEPm_FrSO60NNCM8KVuYbauPS2liZx2YzvBU3Tcz1sO9QZ9NmTfWPKZUdR3-FB0r4b9THu03jvz1hmmyN3eSPfFCuQUNwzZW5cu9c1H1l-beEpfGxSdEiDybiXz_uWBu1VofCfnAxX5zpwJtEowt-pDUH9KCTPl64SKj6_Rq8PCqE00DCX20uNibK-ztJQvlModwb_bVvPmGgPoEc7vCNUvfccoyMLd6b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DX-Xadc_t0fwDyYbNAjkzNGk1yIWpnuA82CXQnxNZXCW3SeVSVm3lGy5JmBssKjbZUm78zaMQa0Aq7CISREZEK1tHpnH0JzAV7WgwSwyBSMWWDdpv4dx0qMguEFBQlnYkMWwVRWWoeUyLGvSDrsGQodHpjKGTjvSy3YkM0J_zrU9GvxryEWgm5qutrMOhUFmmz33uBdpnRDXAxcBwBZUlLfX7HKtLQARWcW6KOzepf8yukm02DZ0Ed1oBO6v0vHZ3UOQ8UguAv2PRlvGEydh3E_E81oUBriboKMNY-iYyNqL_M2J2dQm6d4hmpRk5x9CGW1mZiUZRGKXPKDz2srr3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pe67zZ5A7R_p5ks2Fb_OLKnEd-wdMmBaMd_F0j2BZaUkEW7Y_w1Pc-tfHXniyRSuCA0QU93LeTMAlqBqdy_BH7Hjg9cdajVsX2DsvJ8PMZJFfaS_qNs9XWelkrkCy7c2_62xEtzDZhcrPSJTCMcg0_2pgvTjRuoegLDL_8RnkspK_X2MrVX0rGadDNkdKxICkGyR4A46edy9SBmFxqeEkkNkIocUQMerTqtE4yS3Vc6Gm5bYheWVAawb_9JTMRJXJc3SlLzIK_VwILeairLTzuhPBsbUaGflEY_6zQautrgA_jr2ZBlsGtpk3jfLXNxie_mYers4FPaqKPKmHS_KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_0y3VoObKaTkGgzCPvY1DZV9AtFpdkdXhBGlFP1EOaXLjeFT1AkeD-50WlhdQXjc0j-Ej5OGVgf9bQ_oQKUtrSLWjKrl9yGUc3dKSGcv0CPNS8b27UWEzreaHGOXviyKlss-1f2q0KY2FLsWOAZABnY9VJg549_UGB9JPfx19EUcpV1FZ43hJCy2xkmQdvi89QdwOAS1pCEQNDwT-lqLJTSPMvTAW6m7He0RCRdwQtjEfaVDTCQCZSvQv0pJTMugOqk8zD_FwXHJ0BqZWDlCUF94HaFNf1tA5hcF5ghGNFlNc7VyyiWRFp1CFQW6TfF8lhdjRDmd4ftuQxHuZxqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDNJm_bYh0JxFyHhfSQuGy3yv4V3IBpHLxhx3j1TrQbbt47neJ7weT04FcpaDjnON_W8NoWO1AVWB3m_Dip3Afm5tiogk1c_zZ1VYkXmZ3W-tiQYPC6_35Pda11XtbhT3oEF4skdOwZHmK2w1KiaGbKKWHTRzeQCQsmmGdqao9ghc8diL4a-Py_GxMCPrLb19j-IWEvAFUZAJYZSTQ0UD_t8_EPiIP-yYuEtsnizsSGkrcLX3IyDJYHz5XJLtGLXSAf_jg81lV0NX0NKtA6G1s1gDc_706IkkpZnsjxlEpdlHSyaiSJTEosGfX66_ObQTsQp4fLv5KjqEVWakcyJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p3CoMQx8_KnLEZbxcOOMMuQfHX84UGi5eTAy12QgOh2KNhxJOdXrkChDET3ETypYpkTPsBmJc2NQ1gq66aj2RRwc0VWCY0UuXaREcbsvzToAD4y6QXMTAOBwxVZ_QFsHnB4UoIzJh9nHLMy5QoJ8C4RhI905L9LaKp-t1rq-LluVkDgKH_-sdSTwxJJcB9U3u97L2J2upewrfp5QeCOt4On2t30o-QVsMb1-Q5WdKLMCEAcKhD_1msrbpPvnEVYD-cHcw_Eyd6lT5k7k4bqZZr7-Vwne_iTaMbUa6WXJgJCKGJVMEaRRXqO9sWoyV61a8fMMAOr1wQeJgKwhtMORyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U0ySbzmYuOy2O8xTGGtEt4NZ2PMGubhpyTKDBMJeMzrNcWmV07SDMrcNvZ6KSgxPb_OCgdaoJQbLgZJIYpVWGH4zbss6slzhkZ5SBhBLlZ_l3PmHH8DUAUfzLKeFNa9DdyewWn6tUMf3X7mA04Cv8IT5CuViKkIbKv7cq2T6r8By7Smc3__ZAeCNcG-hfX9eVp7XERL_hOUmvdDUZp9RSiAtAN9A2JcIEjIMTL1xBKi7CXnqZ1KqjA_qd8GO6jqmFpThZRCdcQiSXFGLGwaRrPLOXu1Vt-rNJV0qQY_KTEQLQt9CFGF9tQZDMIJiK_T-bNCoRKD5aYslm0X5yo-1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gEUhO-3euqnRLfYkNS02ZGcHdf0aj_WHe_7HUpuCnoMLwfeWBqHJm6lENeN91_H08dYJcf_EgAwyXPMWpkcRvh5uSoze4MGrg5J9tYS4JN0Aig8tTZv4Op7OwJiur5JJSlH_m-wJY-PDyy4djlCQ6JNWO4LQOE6psQ_zxFjykyWqqfwIkhp-D8BqlnAZM2cNVBJLaofdHuAX-goSehGWt5fFQTMuzAIKbRPwxrvNF4PvtmgmIHFCiFezhe_gO8RzMbbOQadSgYg4cZhmSTrsDZw9a4VrRZZ1XoHla5plrLYfC1VEah-0Yfsav1t4YnhJDkK6EXzMJuGdJWg1hyyZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kpwmkfjp5eDxs_JtEG_w8bzfWlpk4lLI_uHja7DVw88RubXUlQIxKEy8lz4C7IBvGiBpyx2qRpkIR5CYTwFlwNOYIOl8qedtrz5bjBfatmPvJr8wuVetj9Gv-fp1uLCVzsjdhRxAxgcpgQ4S7QR7BhzJjqpdjQEeraRizl94qSWkbXS6Xao-lYl3nzblnEHSoAej6LHTMAcnUHE3SMsiSrTYbA7Ye-6k9Jstwu1RB7a8S3aYk9T5FLdBMqaA1g-iy-17aMKSOzPoPdctbOGMuRhkLHlp-LTFTrTpazLB9JScHkwaz4YMiwbhovp5eeNIA1XK1O2bXwnJbvhpi7B_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWYHfb5hHv9Iah8RMSLndNuMckjeFr9zI23Dxcgu-l4dMmcSAN1pRWugVBCGBCEamubjnvcCDabiP3pnYj0RaYGijn4fKGkte0T1lCmnFLcAKrepdUfW39mGqjqS2U83z3XUzk1VF6ejJdYqqSs4p0GO1Hqs9bm6taRv_ajayYhI21_6IEJrwXNiAw8E7zjUpS1KT0ZXXKXESGHlXydjfGGtZBURxpBbY5qgNkBoj9Q7mJWzipWHVWSUQiQ2VwLzQUjZZE00H3_36DlHspihxEbiSsKAIcf7kr29Ud1Kq9yoHUAPHcHk_yuT0vbDuSnEoXNqBSxd5N-93ZOhBcjAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=G6I6Zua7oTXnSY5GhghpeF8xAkQDZSMy47_16ddHOjuLVm7jBiNzkiGd7nAvlBAmxn0EAW6LokLV30mBY2abNQpYs2t8OTVVn9Dc7DAEpxGJxf45Nw5o7kSVpwbrfKo901ZOgwudvi6GPt0iNCNXbXYw5EozmDZGZjcnyprJoEFlhHiK9vaJ2sGfh0A6vFn5oLtci3GTAASIDll4saytJcknRM3FPCU0x7ltDbKWmCheguMR5ge61wvFR5CijtQfwMf2kVdDhmsnOr0ArlJfr4_pEiNVsjjkOCyIysiN4qilz1fZf5Qxp_koaCUc_DKhRxDL-KJ-A94VrmgowsLPVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=G6I6Zua7oTXnSY5GhghpeF8xAkQDZSMy47_16ddHOjuLVm7jBiNzkiGd7nAvlBAmxn0EAW6LokLV30mBY2abNQpYs2t8OTVVn9Dc7DAEpxGJxf45Nw5o7kSVpwbrfKo901ZOgwudvi6GPt0iNCNXbXYw5EozmDZGZjcnyprJoEFlhHiK9vaJ2sGfh0A6vFn5oLtci3GTAASIDll4saytJcknRM3FPCU0x7ltDbKWmCheguMR5ge61wvFR5CijtQfwMf2kVdDhmsnOr0ArlJfr4_pEiNVsjjkOCyIysiN4qilz1fZf5Qxp_koaCUc_DKhRxDL-KJ-A94VrmgowsLPVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np5fwcXVRHFs-0MoNGpS_kU94AvDWJI_UzaEGPcYBCTn8OKLXAQ3bxrNCaqDq3kLqKfCCXuRV8pHzIql3X5XwN6f5kdEjkjjd17b0sJo2RZpVMpS91biiTOTddrcxqdQndorZ03a7-AvEi8BGMnCSkmGbp4CQsswHYT_cF9nWDSFntVcHQX24JnZJAOclQGspjKRoP6K9rgWi-YHB6AB3rtvGyBmCkwXmMu3SQSJ6GnMX_ortyldqe2LI5XaHXL8GYksabniA33Qpdz4gPs7EHStFlITGbdy9obOZtdQm615qMy-eoVxCIqEX4QLmYdtpOjYR0IdP58IPL35F-3EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EoqzjokP5PuqBxqJ-QZo-_qdAQNwqQnjXPBeu3xXgRCF4-LmazraHtCXWTtc51aCFWypS6upcAaD1uT6rtJ1AkRzjSTGXTtChRconFAUvx6eC5pU_2S1eZ9sHFtgL8aurlLKZNMC7t0Ur6rsBHYPQCwy2au0Bu8NzlxyYVTq3L6TfGDX7zS1rq-9EPthKQ0FIZaW50sfUGj3seS3ggiDBg8YBI2eTISqsiXP23LMOY7GoOn6dTljkTAnLaIYF-a3fCtRG3Wu6RoBuFHQbbf7WOfBhPbk5d_1_qdCOKQt_mKrK5oWMgJMjMd7MUg_vD0hrnESBfyNiiqjryMGKTEMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FaqPAiWeMUCucE2C90Ka3LGN9VE2IBIDKAtmN97JpXY4mXrnQ247nem4wCWx6242O8bvvTpF0gJqF0EqrS0NcsdJbz3dDD9nAgovk8QgEusEZS0WLOsIXrGOEkh7bUUfjAWxfuxdST0xMKXdfveWV-CCUKX4alT0JPutUWQSurqNXVAth_hK9UgsbjxcPL7797r3YdzQ0cIqwmEwbiFTxY73tmEs6Cy66IAi40zLbEo940sSEC_srWbo6aYjhh_VkZHkLtwIK4cGanMYIRmdHne6g-NGCghMN92mFczvSQuigL9vqNciVJpSEz_m07JnAkiR7azYnNNfCbcx9Y5jtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KiHBfnBSztqNqAy_Lnf3rp3ZSLoyF0r_x9s2AquM8DuMqxLpmWi7aH9Ew4F1ceGKlNB3kMsVuv2kxys0yGZyJU0eI96kpgfcbQehW9neV1UZop6FQ2aqN71dXNf3ceCWeDJAUPSF4ubDexY93QVTzbt_yd1ahP1_PArWR-89z8ZbdvzuIw3Nr6ryVKLP7nG4YkqaXbS7kx463xzUXDMQPpYXQfi3TBnKl0rrQWCVtbYEXbFBbH05HtON7D8E0lzgSsT6CDsolqsmQgF58iISDGIzxOHbjfj-1d8Cb9ucw10WNUVpQQLQIPzQrjk8JWSeAE3JQK0jqrnLXTg7ldlloQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKcK2Mkfv9CnDAwgL_168fiWYdhsalGgGZ3ZuvJ6xBqHU78MF6MjswKEYFnqrHcgXooZesaQMnAmZ2DhahlFH7xDrHrcudY3KCv-LBGgnCzU4mlBReHRd1Juyts73zmhi-O9UZ-7erFeH7e8fISRzj7pfMB4B5La2BEBr1GQxIJoBipQZETv6Pi2F7BgIBij3Ti8cW1axehK35fXoqXOOfFnXTchg7U4CC-2WrPccNTK1R2o03I4AU7c_PNcHsSrrRqa-lVPmuuP9Dvf99OziVAUKJkht0eBFGUBZHqj483XS7_XDLTnThSJKR8-g9_3x_LWhtDXjET49aenq0LjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AwJPglnaZHZxvExavJUdJGegZys6zzuNuGIz1NyDZp3fHsJoAlZe3HDmTPTq3jFxzI2tnaWQBdtGWP994gVQtRvPYdljDosFuNSfqPR2-qKVJwrXNTf9eEKBiHabx8_cl3jIR9SKXKvUiLUB9j8yeSjXE-7jxYSLILrL7jImiT2uj31EuADTJ9BwF9aUgoXSznZIoni6KHvRNwKxyZfNncA-fJwTi1zH6CwhNXzj0naZLqjYj5J3jLS-csmqc-XJ6NUZWx2zHQJRfPkL499ajE2gGVLRIBL6pe74Kxt9AsjnFsf3YKey2uN1V0uKNTIF1OdxSIw3uQZFIN_LZl5KtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KQO2Gx6IxDasnsrd63iQYDgiYPZympQNqDGtIlsjA9LIXXjfjmLLgR5N46FS_-yvwyDuVZtd9qZw1_46_eAt5sYXoqbaoC1xIBS2ARJu-7r7RcRjpncyExM-VtmpQtlhUv4ErRnUz3dOsNXGqjNJChMaIXfH6r64vcH97TgMXWUjtvMOTzWDrg5iQSOxtKJiU0IEPpRorTUP7E7FGk46XNNh-2hWlsVSPojswDceGHq7M2SwwyGfMncALO3Q5LHsa6AHM8qUvkkLDVNEamRClJbkHmAksNiF54oaje_jdQlpQLhMOq4JUo8CK41opOt9q76wP1H3jz3T0Xrnwrjgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SaIGKw97OVTXOzp1bhU-Cj2VD_bmI7g1VHx6amjoocYLF_tmin3G4IZAJFD37bmSOmwOJl8b2GOjiieS9ALv2Lw0phl7Uomb_gkc2WSHPqk2yan1jkl6XdrMbAEi2LMhRjcKd0Rua6YLr6Ma0amxjeaFwbLPJhL8dmBxakwOIBXkYeMpUG-cuRKAnf3MnzdiWqzr-CmEa-Yz0mSMgHLYdXibl_86IwE2cRq79ZCx_B15i1VjMFlL1O_3bMwOUrKwa0z2HgpEprDTut0TnBTNgv49wtGBgrA3x8yvswCFFnJRNnpysoAe1oCdvDoMa704NuzUlKVLhb-b5CPzeYDscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmQakZkbvv0Af9VoYE1JwEkfILhV1lSvsrTQ9WOnrulDB9D6__EQ03RBw-orleWRXU49ap646ubPUTZE-MU-NzWxGWDwMytkF3ItVk-2V-r8sLyZeIa6wOfXXTVnOcp7SiTHJkhODKFwEuISkPIvj8HKhJCx390vjujnPkDBE6VZRvTZQk_pd9zC-e-jyoM86dYB7sBXQb6TIXXUQq9EmYsEhxJ_z4qvB62uVeyQxDIenLe9jyBrOiP5Rsfkq7gySKfZea-JVxDT3S9FzkMYl2B8EksR6hdP0N1fHWfWdPsPaTBC6g224Z2nLnxREIXd_W37irzkyTqRjx2ENi_BtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aAblJbXmRvVHh2JgF255Y07hwVEXzrN72wc2xUStBaPVSup-dP4fxZnDzDCgFg6IOQkM-TKPYITKhZ8nA6RqgW_v9p3Y8ZNmVOClfBqb3bqoO1VAGuDENs1kFY0kf10NfahTzXOXyLOKDfo-91wU7FoA5lwqMPHrZn5BfapDW8pBeODFNh2h7HjLkXcixu92ShTH7LcfWhAhAGzU9y2oq1xEXsObdMwok6pF-SsWADKYlJ_tpvyAQ0h7fCDAM4uj5acsp9WdNhGqNXDwlk4wYQskuaM1H76yh01IaDYK62jVJ0g8u1hrHYQf2a-rS5ukUZhYGSteq9Yro5bY-nysRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4dPXDLfxdlBI8i12ngbuVw7Z908IClJ10ElkxH0-9H2A2ecMoheKMJ5sFQBkux1bcmT8Y46FRnoRo2LUp0z0DLEF_2rBxl46grLessKrOtDCIU--lG4LFo9Y1StRu3nZYLNih_JRAGCHLE_Dy30_oLFucd4aJj2DNNOCt3wQBA_2U-4AVxSQ9QEBMkFsSRUl7lda-iXeAe7MMMbNmDr8I-T8LeMinHT31FlHo_PJJ2JL-EETiAdO5e79x8ZEZRFAMgsgHwB7EUUo9Zg_POg87Q0v4T-3tFUwbJJCYJXCRXituIcGM8h2re1Dmlw0CE7xxS5BXLF0hsLH2U2d7EcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GagcNUWerXttW9notFszGlE9bIH6ZNiGxmNTaE7U7JuBnZ9Esbq4TLXBWTT8N_dLGD2DciZ3r6X_6GFDUZdoIVoln1xYk4A5QBoCGtzbNl30JF67jndm9J4Occf6KoFgqbqxA8o3yZbkx2K6vQ4IV_wbHCA4zNPWoQF21nwMptGEPK64Ks0v-6O5c2bkX1N8ljdRjBX5yVbGr6tt_HS_ldwmvswjs_iKftUJxlD5MTjSWfWs2On4trbfGKGws_QH687MhOkXV8K-KSXYMucXU9IynFtTb8_neEpTZqDVudzZa--ZGb5jDS6FXi-ovj1U37KAzHAkx1ZodjGprdfmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmlXJCFdLZhMTwpA8JiLTcHB_Ni-toAdUhfBFpdQ0cLeEhBH3gPPomMEWNAjWCEkKGINIgwDe4ir4Grw3kC3taO1WHEb56U5babZkOSsG-AvxBzfxcF56tloi33lc4PNnHezq4oravi0N3yz9TPT31uAJKUUdXDk4m4DpDBAACuiGHc5TMEqledUsdsK2VNABJ6Fv6aLsgloUZW4p9munOUo7DEax_K1grsqbj9v8XLAIKD3N98z_AP6GgbmVE2QKSljTZIVHLHfTBHDwcVqs4vOhtzOeNTHnxBxzK3qMTp7JuSVbkG9ngj_OQPjAnGt8Puxop4AfC8ccOa5b_m97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUwscg9ISQH7R8x5AY4cNfEhW3pQtQAMNStHArpMKL_od8bNm17yH67PFPvzkw4l9awEZYt0JGu07ULY_w9NSRiqFiwxO39nbTrex0FXlp4q21nGDc3VST7Vrsf8xZ2vg9G3KwuTa79SieW82xVnbyN4ornAMNZYSm5skD7uisU0-KZgXxpe1z9k52Km1jaYWwVGErCgqxqHM4j5LLaXEez-Gc1RrcBVXLqg_E3pnfjIq4bsaKG1fpvQc981gD9JGbQEmhuj2JpVRy_MSuudtRXMB14c72E3i6Ndd8G2vgNtQJg-SXxAv2a8G1uYHIFjq6ORaE3xXehh7T0zZZfJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAK-e4nZuUn1UCpcFeSyuWRQF8AL4fTzmtMhY7vGZMKJJGOwSwlQmeLdiwJweP8ErI4bdn_lmbrKodBWDJ2E-Esgfi3KqsyoDCe4F894HpMJDls0_0xvuNpr_xpaLpG8C93CphB3v0FfrBXDpmOzvzCdhPJpxEpnNfy9aN5UWNkQxEEoHr8JuvdSw6Vy8K4QrZvYJe9ouP5NQp0mRnlW87_JJIBV7s7NIarEWp-8FtR2t0oqUCQZR3QfuDXHwn2pHnZjfYLKs7MR5oqmhpYMTSFGvqfLZNEd4RnwO1N5Lso4W25NRH2ZQ5Jdqb0qE6e2XfnOc-Kk-lGs7jP4wxlkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7LnMlt24DecrEP76JUQxkFFmn1skX0iK5tFPZIw1zdHVEaXzUlyvXVh1KU-ZDnHtmRx8ajmPjY0LArYCILaqmLgFCa_B9Ugdb1Kh4EvPFDDCaOZDc-1Z1r3bnXDtwgCf6iGMGTb1Rm6JdANZNz0R-BKXirVXEr4yLdlpruSECQ_qn0dQAMvggUFsYn4Em5_IVDwZEO356DOcn01E7-K3O5nDSyVXG3Wxuy9aIM0m33FAy6hjx4t6dowvkmnDza11bJ1xq-kYjkvTaY-wOwzh6neVUbAuJQYdQJgivpuHHcTjspudWoubh4hh5zwzcLPpYXaOMUoDvCJYSXxUW78xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTr0V5ahouBJA9UY-N3w0En7VpEXpuCo3u0Eo0Rk0O6yFfqhhqTISDagqrocUY5JXgufREHLNL6WX6MuOjjTjUo358xLHFifi64zKzD2b6LcGv7IVbQcrQoj-nZ8xHyv9F7llJj6OgRVE18PIA_9L8-SWTMohTNOvmSNvdeHHqUuuWWHUpMhaq5j4wRWhjPlFURzylHbsYfJJbv5vXhNOAggD489WGgF6oZVfKcwyZwo_uf6MeRW-HgpULEKLglKIbGL4VWUGDUYNIKabQXX5Xc8iVG_L1l8aUJwExetbr5fbOAUrIlXzE7o0zcUvL0gGiX2xTzAkmdL2KF8whifTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SEY3pYzmrXmAauLwR7TmLiSH-zCBQTItMpJ6bVuR1teKEvGg3rr_dFnzXDtttlCjwAxXgI0krpOByfxmMzitctp0wQS4ViqYNXnYAd6_bihbpyRcGwPuMFbX6FAOWLG6C7XwRkB1FGc0KY4SbNlPJ6o1OO5H1a7phA5w_WrR1E1vfP9t5CkgpSrw3XuQ1GaNpyh3QFE5sV9Q5XqhzRJclVoW-sI3z2KD5zaI7VDDlD5YG2oEsn4e0HemG652TZcxZNMeOtAk4Xt7qiGVMiVrxi-juhnUWhHsT4hIrpnKT1bNEppAB-QTxyEXLIWkIgDPujj-i7E_AIvXTRCv6ZCk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KrMA5Da4qcaYj-oIfG8tR5XERSzIwKcDbSWecJ5MQVbW4dp7PikgZCamWGTVsSwlhht_9Bqv0tc2XDTMZkzIrodG3oroa3IeBstJ-72f_tGYBnM_oeUFoG2GKK5lGNs3klr4T2Xjndp2ULLOW564eOOKUgTaiZIBiyd60qyeYEpNyicIgIbVfmlFCNYX-DYCZxkIE_VNGExdYn1sj-2eYaynw_xc0YQoN1RbbIYSt38BeDsLIrMiyrmtdrlfZaLkG9wkQeTM7mlk3WBXettGsoK6pZ9MLWQlrFbyFaFXh_PtUl8ux7GkNn7jkwviD3nXNlStyrAWl-UCOZ-5evSuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NblZ9tQyDIw1hC4AueLIPcKCkPxvdt4u_43e5ixpIfY-lWScUpwE7jp_GpTSqK1-yrlDpRjgCv0DRGCI6s8alpNFLIkybGpZPJRNBcKx1iT5dUuqvbgs6rvyyws-mmQ-Om7MZCUgVw-zNOF0mJqpERjX5kYll5AYbqauuvIoyu_k_pGsEatq4qeSeo4rx_qt18a5beN7p3ZBUbikohs3YNdYc0aIfE7Emx77ougEDhizW1z24t8RfaM4tfZEIqtYmnNKV-qwwx0mRi9I_HoEapoQ5cUV_gycPEW80BmiqlWfxLrmYh__OvfMyGfnP83pxVhO8gqJKRrn4LTEZyvuiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9OkqaMZFhA0t-1DdD5wTDAOUWeaOTKB58ZhAtXiZnLbde3MhWY8mKQ3PS1qJs2qe3axhjKZetZBOcl3YIMaKSrHcreom0QtjFta1K9SxyazBZY2l1XCqDAcQaKoqjmh0vmbpjgd-xfoeP9l5uezr6oJxC50tDypd9HCKRiaBAub1tZbj_9FTMVHVhJTDGY5uSbdvfG36Q-tTWL5xys_-wnnhB8hpTc6dgOSxr7WMkP_PHflth67B4wrO4W5ljFmuoJ8kyRVeq0hA_xTjjVi0Jhcfvw1E6HExu_mKHaeDwM78hjpBNLPekF_I9xmmKvd8_5jWYMiLMt0dXHk4e2Okg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jhs_ziCgp9Mku3FIFM9imu-Rok3ow-i14Ymwi8PAHIrwRWittO7fRrM3VKb82H5tainEYSbwkrlXlwyczCz2GxhDmqK68VA2mrBXzuyXOGKbhzyluwjJ4AAV5uFdlIuVtpoPzlYDw2r2OicYDoAEPJpvJTRFOIHbztKpP0i83qELULtl6wOvyymvTDTn54c2D1R_ELmNhmlNmAzEc25aD5all9QRGgQag0_aSRvJ_jaPL7JExumpGguP1WIfXQ7Ks_bthdrXsMi-0OxbNo_n32Pnv0vlF5OPosxU7QlUHG8XLlOdqJ2XBGsed1fDaVZeexRaTvEMc3hYeWtqARlsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bIBp82D-ZZ76p-yg_jrzvv5dPIVaPyjsLt6ub2RzklpuS1pb1Ovphlc3nQQYx6rGifu_lExwaxs6xv5i15cgdyjDYR3J6HSydKcKpva_-bgQaqDMAePTkJZf0o20jsukSxVqhdbwr85MreVxgTSrYEYi1-lnLBG6pge0BsHoNyFHQtI6FsTiesIzpK2zrYs2NJY5vAaSYQP--QzkmIaZZEZw-tGpxMd1ZlujM5jZzijG-meucr7mr_hr5dMt7dLKZYaDmpXbtdp09UplGOXLEqthQngMup6dp5EmF2SrKysMFp8sxJjq0wzsCEW0EXf99Zpdf1bhgC06xJL97_YhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpjkaVtNrnH4uMaqSxLBVm_2nXQXtMpM1GF7IBDLYRfiJ3z02U4sW1X4M0rdISsEcpceI5hBLLe0qTdN8Hr4X8gAFn2QMyELgZ586-ks8TMFjE0LPC09aGvyk3UlqiieCTr4SOLgKxIp8z9AmBk7bp06bznZAbo5zvvxsBcrFUuTec2N3oT4dK_etAGWC1VjeovTwrEAMrxVez0Og_0WFr9e8zbLJfMqxE4ve4K79ZDCCu67UTadjSNCcPvp8P_pjYN-bA8gmeDWFmEPvfl1-DUWApZt0noogNLyaPVAimsh5o2IzrStF4grqwMt26zVuIVnN3lMGqfEqhOP3G8hNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucgZ7UFG1j20U7RpShy93H4kaqctsnBk8Q_LUJbmSPcLP9qIjDjeerwL8U3jdPERaBMcgJpR7LZcm-qvo1LbQTeJXkkMiq-VX3-zBFi8WrdElcGOCluo16eEn65kW-Mu8mrhgsZzBZO7Wnpsrc6xZfbK2du-vtaH4pe_WZp560aWZkoO9hUu6yRr8H4RkSVgsVxsm1FOI9axAcSc97IMqTUdxagbtayQNc3NxfdNsz7U2X0D_pFtbZUNp6DKm88yXKY2HEEO2NHpXGmw0ku2KDbiCwH1BXhMLRYBIEBUWg3Yb1KsV9zf0Y0EHTAtxf0f9A0SKxYlEYWLZkQ56uOXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNOrccbg9qLyqUsojRwaSqF5AKL_hsCKoMgTfnrDwWdFfrw3h9NGp__r3Tw_ic7wz_Sy20ARAMBBc37L-M_BhSBfBqSarGcb2_d6NTpx0vohMvXK0wdGk8-_l5Bz63OPIx7xIcbCjE8PY2PICfDx5f3rHlnwFOJQj6WFCDhUvPwE4mQ8vtA9MnHFu2HuBcsVJUmnLTgW-BhwQryeQ6W0VMdD4lKxW7IjJCPsShuG8iRBXlPI74LfI5fCyyZ-4ZAQ5LdTWZUV5yMLtp_Z4qtyAZsbeogKCU-ZAjTXlPs7EIQSTU9nnpqr0GUTAje66B388IYLPny_aQA8w1Gd2HAqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nSDnY29qrXb11u_salylf-MFsOJMeibgNaF_LKbaUDy1aIOpnUfY2AbZTo3VaDttQX2nnsJ1TxAc3BBt63DRDAbuDrhGbLYbHtlkdIJEotjjPJTDl2729ssJ7vlZZz7gqq6_hPZwhhhXresFg-DOdMNj4MfymjiyXMx7d-4bNHy2n3_vj1BAJly_xJaX8N1CIYFQA8zIBUlG_K8rDs16Dgo1fLhZeRozfEFZEpMe4bKOTEhEA98hbm66Z3Ned7iRiTQGjZvYKyGHV4t_tKar3SCp1NmZhYjvzybG9WBZ534t-9ndbH-SoJGI9raL5fL7i52Lw1uTxlxY4JZSyeLVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmRIzhYz7RNgTLV91IQLq6p1zUs4XziZghla2B3QRQWDWAw0jz6LTAOl-tasu7JBv7KjrFxzg-6sZHE7w8jxQp0Ev8rF1YdzkqDIiNKp0kWgDXx-ZBfjr_DAEX4P2troUyGPFHo0uf3s1A6QGci5PCcBeB0B8m-9FRpxl7Ibm7TC3NXGNSClbG3K3Dta-xGqDM6Xoo_3NFR1FZeu3rUffAkaUV8NuHYd32AhrDZ0q-1NKPj_rESu3x8KtrvW0kxXgb07y-OBpOcoCgO7H0vdPqL1oMMi1g5Iz6uHD9RhdplKtp_6UO3EaPdUDzhUfAt-t1UJthndIkAo011Il4-r6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZcSmf-a8eJjCA8T85Lg9zoyu0CWosILldRvIpCCdZEr1iZRZI-nOjOWaVC7fzqNr8o2HmRQd_OQcNqFs8n10eLZWURwfIOmTmNndWVpSOq4STWS6xaOqgxp3Bam8ZwAuEyqiiCTvUfOy9HgefytXPrPybEafB2OHYuuY1-yIYmTfuGMka1EZnVUtb0EFrt5PImoWBLX-5XTe0-h2v2_32YKql7e_oaGZ5_mPnWmYCSjZf0MzanxwGotuBVsGzAvC80bL9u8dfzkUgm1LhentwCBLFqL1AQEWDDQJHkutarwHpiXMcidPZ29muKtiklrC0t3rve9GFeUTva7GT75Nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=R0UdWY5W60pb6wUh1RjY9th5lP4RwTV29r9TvQQWMeEoxd_uhwV42ZcrqNlJBEup9DFGXaZXFl3--w1RpHbRAKrukOqPAhHV9-wiBUtB29kjvaZcuM0QcbGlCiKDaWFFT5r3K51yDQ3RCh8H4BQydbXoF9BfxybA3IXjkhx42r3XGA8HM8-QQKjrfoJdDWHIqqqw5qowCY3dkyePQ1L_0koF0FJjCqyQTxxUTSFl1CTXmEW67I__CM_GAKsrAuM2derfhoT-raPvXlU65sXoXlFkutn_d5kV3LfdiDwWqiyG4HAR2SDoHSgtMudNjDlw0KOI1jYMkpbXgjxgLr2eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=R0UdWY5W60pb6wUh1RjY9th5lP4RwTV29r9TvQQWMeEoxd_uhwV42ZcrqNlJBEup9DFGXaZXFl3--w1RpHbRAKrukOqPAhHV9-wiBUtB29kjvaZcuM0QcbGlCiKDaWFFT5r3K51yDQ3RCh8H4BQydbXoF9BfxybA3IXjkhx42r3XGA8HM8-QQKjrfoJdDWHIqqqw5qowCY3dkyePQ1L_0koF0FJjCqyQTxxUTSFl1CTXmEW67I__CM_GAKsrAuM2derfhoT-raPvXlU65sXoXlFkutn_d5kV3LfdiDwWqiyG4HAR2SDoHSgtMudNjDlw0KOI1jYMkpbXgjxgLr2eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BsXwT64Z1438uu34bno_qxqBy49yeHQidz7D-KiCf_gCoDzHVAH9LgZDwunUG2thvgJ2eT-WdS4WVo45ZrziHqCXMmG5Xwj5HYviBKWpTuAENCrQMvr4O7D5tmP4oqzchUSj2LEcfC10gX5lZoxpH3VR9XN-h6Twz3bikvPFXmDLJxaANHc7V8o1ZSxn19bByiwOTmiLrY6sybCORPlpaAyC87i3c8YzUc6I0BFq4RDWD4ASkQVth7RLLg1uTdmW21LvcqTIFITxGeGpxBQQYQ82iQgm5uwsKym9ZF8nJ-CqGeRgQRNOT39Q0oQoMyPfflOHrX_mg26FkS555uTv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/thizGF79xB86Ov9TPxYOhNiFHYBfud-ANV5VdF2Fha45E_9zMpoHTfEjS2c825napSJ039xmk5mNYU4NfRVXXaoBA__pzyTiEWAmj2u3mkglej9ju6zQ9BRCU8Tm0A1k2rNYJcnilO2rz7NnEukBvrPROqF0xq9wfOsEwAqQn62uRbCCV7D8fi-i3asGb0eNiMW9ehrO5OtceZR7gyKfw4rga_G1FEdxaqI0O8svkETcW3gUPlvdYJfk1ekR0wogoDIxtP-0sB5asC8utgUoAimhP78FrEtB9h1UXJMtki5gHx9j3eME11O7AaIpf-AwCFlTEjjfik3qbfXeBpSnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnnJh_YOMg0-vagQW25EB0UxRGMRwu6_DeUApqyifuhbbwbgwzkYpqqOs7K1RO5gRUFv-PhdM5I86V25QAd8pLgsZ3jabdGayIOBYyGbTaITZ0Q6ymmUl1IxQchnJSpwZq7mbzW3FME9LGw64aBOhwgqBShkROOE6__FVuQaXmUDuCLDjkvLKoWp3Hx2PUlCwAsKz6FFn3jA00bSJ2_Bus6zKiCHVeVylWw3Ei-X0uv1i8r611YSRHtReKvbj4t27Q7iOlVdJXt8OT7cFqTQepdD5JLnq2BaoiG6cFv_TUNgvcMyv6AjW2GJtgjMGaYpDJovfcFc6ptg7l8jnsR_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gcp-c01x9DMhigPqSG54sJoLUXhnCC64RONLHpcxEH3Tf3KT06ZrmUshnbtSyIC9MViKkOskhFByfPjWE3NmiQXJdWcSYPQQ0Mch6EPRW_6c5uVhnqNxE42I_ujgleQXpUBQ3A7FSrqbw3DTMdUDNF6oUbxhnkIb4kQxbEUw-EJdX1SSQ-asA5NJPGW4rNS-MdZ3ggsTl83IskWgd_Vvj7SFWO7JisnxHTPgkJSTnKqkzWM8wNX3PbmeSwjjnJ_g9p5Vy4lrGdUkOShVC8J3pPBMMZXhax2Co3cUhuD4VcpeLaKaeDpiD_KCBhscMKH_b3lVaPaxiRUK2Uy2cIhk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mg_o5KUFXmKYguYvoGeGybzIe62Gfb3Vs1Lpu7e2QS1VmV_cyGG-rvfw39j2PYF2xK84UT2B6UQRQbNPj2FW2lXvmzP3N-nkCl1g-Ak6XOQhgRQgwgRlAenRKLQyJA_w9znL-gM90ySu7sb6-YvOAJzW75EkAg88ybQNboGjIAA85dgwUEa8vLnTgFnUPOcooCVeoOCUcH4t2Kwvw-CKriMvFkKhVV8m2PjQDw9ly547p0ncgz7u3EhQP6yHWDI8XdJs0k5NhKXukzIfirWNmMrSyESOdswlU6vJm522Sn-2Jek46Hv2m-Bmf4JdElxQFFO8RkFfBemiH3xHpjG5-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOLYlZI6tMdKolzPACXg-GeBvxhocKhBQeZyI2bY38PVrdQyX8vek4PXZsWdRDpHDxg6S3L-JJcsn-6p3wXIPph6XJcwamuYAkgr3G8a97vHmP33MEA1JX8K_U5gROjxuc_2tMOWjOoYzvEOCyUEsPKFntH3DTSmR3vYjC0xLICWKinyqWG0KJuzijYMnPR_zvI10-W4CBlvgiGzPJ-GdA9iF-ulQIrLqjoDy-ly_KzeyaP8WqwvhUChvcL3iOEwyFcV_rjwNDkSwqkYUHleiHPqJ04asKgEZMXvC3YezcL73E75e37Tpc145m6ok3BfN1z_fP57tL1S8U_hREzUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
