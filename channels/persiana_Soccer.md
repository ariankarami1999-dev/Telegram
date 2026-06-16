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
<img src="https://cdn4.telesco.pe/file/ZST8GQZAuGoKIuxjVOLrbtnEh3uQLdxfuR56-qfImCCcl5kP7H3GM75I_bUzFX45dIVegsX43X38u2d2JKVKRcg9PsMgrhDv62q_X_yrgZfseSj-sJErCUdot1hhgdl8OLl7uFplRqAIE-0JE1mZJRQd7ssKNpVyLNghJv-KloKyDsSEbyndRQLbdGKDR1tGK_XTSU-kPk0xX9Iu-aoVtgWcWIfcvOVuFOBST6-7FWt9lQh2nepth3nZEFLIrZ6Y09LT-V6l82zQk5Y9GTMKO240WoMOxIi9OJYHeUQcFqc_-Lz74Denl17TwXLJiAexc2zS2a6paYGZOC24RAAerg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 301K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 02:30:10</div>
<hr>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=mynE4yJlpGZHxGTwUhL8l_gcOxwGOyeqNPdM7-H6FReHGS3Tu_i8F_SbpghZ04I9FWBjY4mSfQ2K4AUuyEyYN4ENN7uSneTZxDd8kLim0ob0XNnGnaDpYkqhBbV-BaMHq0YOqMOgLGAosQIPzeBKvlMxuadMzqJbP_v3HyZb-lKFAr7jKlIpmJLxLTodL8L8KAtzMlDDxojziR7oe4YALLy_9-cBqvXFObDcH6uR_C3dGfGMYmxI5whjsZ2Fx0yiT9fBqevjk8Ee3Wse149wog0YYbSfQ1wTGB42rid-KyD51RA8RCe43VUxnJoyh8JpAfxPbjonpiqTi720RJFJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=mynE4yJlpGZHxGTwUhL8l_gcOxwGOyeqNPdM7-H6FReHGS3Tu_i8F_SbpghZ04I9FWBjY4mSfQ2K4AUuyEyYN4ENN7uSneTZxDd8kLim0ob0XNnGnaDpYkqhBbV-BaMHq0YOqMOgLGAosQIPzeBKvlMxuadMzqJbP_v3HyZb-lKFAr7jKlIpmJLxLTodL8L8KAtzMlDDxojziR7oe4YALLy_9-cBqvXFObDcH6uR_C3dGfGMYmxI5whjsZ2Fx0yiT9fBqevjk8Ee3Wse149wog0YYbSfQ1wTGB42rid-KyD51RA8RCe43VUxnJoyh8JpAfxPbjonpiqTi720RJFJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRK1xAy0-zfeW5Xf7m7JkJeJp9iEanB49xf53u9Sb4IkjDON7RUIvMa89GCRre4YIoWpnFP5mEQwTX-aaTkrdPyWpgpmcZyiQNi2tj1NKOJL4L0_z1l_ovQpyH0fKdcSkdcNYZzk4TnqB46NUPl-1ESV2cI5V_2FwG35Jmp45uadxc7ERItkCAha0Cw5lx86QYAIHYo_dOSowtkZzHsBdPr3XQsTLcx-36jHiEyNlr0OfJmzOAhXEHcmrLsDYGFwVPphI6a7j7H5_gFuPkqmX8mECsHICB5H40kyZv5Qq9j32p4p52MCGxvm_CG8JhbsoYZOltgSp-idmXSHQUXeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXSYq16g6H9CmVejztVc_58KvbDnjcTuQ2cP0MSz88xMaN7rTkw2VANn-WBCb_WkUsd7D0ZHsVfOOuAnTKXPgcif24ZPgmxqtVGttHxk_HCXcYyOTVpyPEvCe7pjksnH-1qA5wIMJFPNEXZjSWl1G8YR3GfzFrK_vI_xsCsjkjRNNTXp2T1_g2b3VjsHjV_FdcqfA671Du2pZi_g6VFj00GLkJBxjhZUfyCiul2LcGJoom3eJOy1GiyM5kHSV1zOCtEWCBTdbqMAQsvH28ufqMoJxqvlqaKPbXiGFqr8foH8LNRq8r1JIIlxFROhgehVjAkURPhGL7kE-1qc984ULQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPyi4Nc5PBCXqtQbRccMgh8m6ttYW4teYiyAifPbHP_BTLYvfFPqVRZGOOZvfCeTyqTDna8SxtELyJL0FP2lMmDMI_1NY8S36ipGk9_TldsHBZblZtXU-0Gln2u-8NRej70euqzTDKDKgrOKwXE6ojMQGezCkB_Oqt7sHs0MByftzDCeBkvuBSb7AFlaVY-KgHBZt9OKu0xLTrpV1mn9p9j4mIDKGjasSnlCF4NxFBAokBxBZKSqViuQaXCznEzDX6Yd0_hEOTKn2qEi2M3ItaNgRB8bNuLTD4RqVCvKJOA3GIgFuXWJPzVGf6wZeDe6coKiZpi4VFmCfy5K-Z7F-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC0VIWP4cn1gfHwdP2MHLbJNoZjDVs19G7vAbTOk03a_bc52SGqXCJfjBSu44JdMMvEYpy-SUINN4TzLDUYZAHhYZxXsmV0SRQCWap-EtTTqvcElbS02xDFIz8W5lxy0_ZQeZSfDxv8P4QIrN86aNzXwpTwvPmszqd1Sulq3Vtcks_jD7A4xwRqFHVIFmUvEmZjWM6uEssi_Ai6QyLqI7OMb67BNBH-5QvCKKjjlgPx0LeH21mIVhV76L8d0CwDtBh0e52UHZp7zJVTPOdG-ArYMybJDrW_xb0vZwt6IEJ-YkkexXPRc9kAdeh1H5htCYRUnGMBXtbpXYOp1bJljuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای جام جهانی پیش بینی کنی؟!
🔹
پس نیاز داری به یه سایت بین المللی و معتبر
🔹
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت ea26:
👇
✅
https://t.me/+bcynkEgSW2dlYTc0</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/23639" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmsALYl4i53WYrNZireDeVruUZ3Iq11BuzpdEX30O8XG5kuHWO1-spCwtCEmDbczaWBnbqNDsuUW7BpM71WoNgobIQl7Q6hE5TKFq8D39fZdcWjFWlRkOmRgEx0ydGMeMcKgTaj1xfZHdIWmLDr4LzS0xceMTkUVrSv_XTqSKhS1CqSVJK27lu8YZSEOWSZUzZzWkjWcXF1X2l2CKMbl7Tt67OPH9KDRD56phXyIxjQcFc19kKFM5TwYAiB6R6LU1dpFIpVixq1yBpxfLEhFLnEGM0VSbYImJOMWxTPxLBRtebjHK3XaQPsE2X3oNr7OSacrUM62Adso3w0UJfwwlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX1lM4I1Ydk8W12Q3cxvr1EDWr96qlHTT9UqDhBv3r3vtgXM0c_6RzSf63kC-SFVgdegwM8MDe3-qoSp8lsBgdSiRCYdEB7U71eDlmiQz7Pl9UcXJI7214-K78McmNHBs4kPEFxDB9s75pkg5Xatds_ocZlWjcAPHMCN82nmk8og08C5nlGc6YRjAzoeErzA3rRncUKiDE5CskRc3hoZiHuaW1HJSVK5XFdl867lCTSEdvEt3pOYiVz37vqOSIFF-tzrsyfWU-QAvE3YPbgfLqNam8mvP1Ypw5XzZ9tAZzPX6hvME9597IbBlyCIvGqdPMcfiCzNhIuEtZ7FSoZZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU5195ByBIiWY-syxCtVwYFkX1yH6jPY9a_-YTBKopYdbxkY4Ga-g06G8_Xk-47G9sorZ8OImlMZpJ5Mzr0YSw8afOpZVQvZZO_eJu_TkygichMKwM0O1LWzvj_Bsce-qSWK7xPirUPFWwPXg50UN12JQtQoOCGTm-vq6aUJFB2O7iAjv-1cXHcoS9dbwP9sGAqBIvMy9FBKNviVggmkk7BUE6AJj_tbSlmI5LcXC2QXaoT8GiuwmO8L13wjkIg-NW73YS9rO3SW3svlTgXlvWVo8M15IfYa6EXYaaqZ6yur8-Nmtpo2uCL2_Kv3ROCkMfoPhgYm0TVholAIvyn5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxudeaD5fmTteB3Pfok9h4XTBf5vOlwgoySJyH9dkklWJo78RWiFXMw7ciaJbB6q-2lHoQk-o8Awok7eaPgnfrvig_IPuv6JhRkhmX_XhzzAwqEoUKLScrgKJziW4Br0Utw8Pqi16xae4u_302RxmC1UcJ5dyaP8xW5yw6mFtWWNYKmxdb4VETCr51mCogSKKqHIis2SEdGXbgubF53KHuAj5iuO8tlH81ayFuQYnB38INrZO5ghAB4jcwz0mVMwH6hPU5WZAb_inXu4zKCPAW96f1FQixVGdMh50qjoYchmqVPso4Ge_4hxzCTuxO5429wQc807faBfbaC8kQJt-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brpQxMJbbmRB4XkYpd9PuI9WiEMk7xxWMJgZy4OmBwdPT9Rm422L2nWhkw-5rlD3T3vZ2eLms9q0udbHRaWDYUfloRH1l5sKtphQDf4gDMG9BvfVQ928i_b0LQ8nL_FpavnUEFoqyB4WIr_JyP-iDyLJ6q3CYAkU8bF7syDpfiD7Hn7Yh0UTxHFoVHOl71gAAjLSn2Zi4HZB_5X782D6lnVT8nxdwSslm8xo5EAgiMcugpkNz9Mya6q4RF0NH34GuRfJyDWNDzRUT1hFDlSpR2GSBVBGOaXiJDMCR7_5l9xGp81ecK-SnEoAF4uKWeaWuYzKdnBYJ5GS6tVBzk59NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2uQ63QXbRiIVYa_fH6t-MeafEKr51exMCgSb0SXTuzX1xk_T5PnvNzfDdxFm_v_49GXEhXHACLeAgmWeds9FFB9Q8F6z6uM0wWo_tiTzy6oWad2g-QnNZHzmL0KUJdWOngQQe1WFgwpY9abqjsUlaKwJhkUKiozEh0WhdkrRiEas3DOzmSvvu40A02sEao3J-ckfHa-oSHcE0gsJPkqVfeGp8K-SVhMqapnUhQUXZnQ4rGW-Y4JOyDizBIVDuWr9JdDUVXDba8kKxQbXAiBColxc21V_fnRMT-tjSn9NUaRD_K9xsLNZLIxwyDFtaPld9nUTXk7UGhRe8e9cv9APw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsO6Ax1fGHQk6kJm0OuYBe9uDL31YSObZZtSoN0felhs-8d-vBDxsVttKVmCj0SHCGIzCi7VNPoxqFBFWfJ327Z19jnbJZciWcLNyTgZgWLBk_bGP_Eqzcnp6W9YU4864V8nOsJtVpIQZCNa3HOPsCVLisRj6BMTkghXV7s5GDSLzcDYItHzF9nAFHlRSzny8YhIrhUYe255UttDp15v6BpwDzpFRisKNfNW46EQL_ou3R0gWtbgsjfA5u4D3EWM4WnrvmMchL7balYrDvAQ9yOOG8ag-WEcU-7KyaL0upemT7e9w4W0tFghYoSXFG7u9kteWBGXUSLNgW69cvVNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlO60K9M68Zk4PFwZIhLQ7E4ZfatG6n6I3g_uKsZh2KwMY_UT9kzC7D7eX95w0Py4jkERmkC3PJbopRFd3s6kpWTZhb7cMYriHYT9HHXd7ybxcwQbbGWZLf_3LHBmfxYbdsVfdo79Wwxv4382M9mY_3zV00Ne6LwquTnBkfeQtxp-VBGismxKZhQkrO4xfnAWXXYd63caGg_gFS9LqIHUsCKhnBRTeDuTey1gEfbxsHPjWqSlOLQ6N3Hb9r5e61v4V0TpTBsdd4ZFqtjPgtRvjdcd8vvsPV3aVBrh2rdp-1Do6-82p6udRsSyj28QZ14Xqhwsj0N1DWD-Ft1FT6Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=AdxnRpD_dwgifQAHw2Wt8aRRzLvtGITpqczoV-g86Ce6izJ_rlkC5_k_AZMKlC2FocR2nmxjWv278SN9H9VUmREk6x7F33uEppqzHJ_jK_7u_1VwEBp9hm3JfSsWNcKHV_6axSvr9gYmFR5lQspXZV1HAMnma8te0d25QWxre1JNHqsfqP3Ht-tx6kG4amT2sFa-B3ixah_zc98XxxbWs9Z7FRDHnZylbUr59yK1dxuSY3RPwMypPVvS2dpCrQGNzBTjES8iMDq6mpSBFJw4UlUMk74rgQlUuOflzuNCSFJh6p8iUUzdO-Y10Rx593VQSsjO6kEIGBtWMcPC_6tEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=AdxnRpD_dwgifQAHw2Wt8aRRzLvtGITpqczoV-g86Ce6izJ_rlkC5_k_AZMKlC2FocR2nmxjWv278SN9H9VUmREk6x7F33uEppqzHJ_jK_7u_1VwEBp9hm3JfSsWNcKHV_6axSvr9gYmFR5lQspXZV1HAMnma8te0d25QWxre1JNHqsfqP3Ht-tx6kG4amT2sFa-B3ixah_zc98XxxbWs9Z7FRDHnZylbUr59yK1dxuSY3RPwMypPVvS2dpCrQGNzBTjES8iMDq6mpSBFJw4UlUMk74rgQlUuOflzuNCSFJh6p8iUUzdO-Y10Rx593VQSsjO6kEIGBtWMcPC_6tEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftHIMZjzxRW3-zYCe2gYyCwxRAUMBE1c1vUVoyqA-i9ZjcYFhvUJZhN9O_uRWjxvu4DTxMN6SCLrXcuSJH5bJ72e1g6rlNLwLTU-4Q2ABe7biojlCMT7bppcpDlkUbIHOvHVWCCx70D8_e02yB5muGWiltJOsyJxkifJSfPw-zRa5VFVnRW55e8NcU_x09yPae4aqIXzPTg38Bj860anGzLvlP4AgjZgWvWj95_uiIOakBSP6x9SsIJUE3rqP2R9e2o4oO3tCpOhs-s8eGZjeodeyRkK9bJmaND-pD9hw6o0gLs_STkD9Zmmv0kqlzt0pXqlRhsG1zHQgOtR5UNy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdL9tvka0ATga4I3nXl2UPT86EUKKjdMuywjC8NtCcVQPtaklkSrgWVjXtSPs5vld5bUJGEf8PUWELDHRt9nVzFJyi3-YglEhoSPLyK-V5UACbTwb6PPC4BedPNcUlYtrmxoI638sh6eIDTGChtCsDa5o72OYvX8LQUKYzfjPan_8UqSqUsCy83Z2hQEyvInG6UcyIR0jaA_ar6sAouqlMHyqRw-jbBmp8saAMP0LlWVRBkJnx7vQK3KRYsPHwftOCzF0T6SgJUK0YwS3cDRFsGty3gQE6w8nGgIU3_gb5f5_CpiVj-UB4kck5ZL3QpFiwSs3ijUluIKlJaIILRwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeyof_msgX47IyAurvfq511i081sJFa8qiRj8EdSusu342nQqBxi-NIC_q1uJ-KOdRRCq25lEn4RfqDuWwWQOkwD5tjoX_cWQPdWnsA_jw_YUk0CO-SMcm0eDlJQ-ZGS62VH_yJ_ONH_LEiGmZxByXego91exENDS85ZAJM0GmIUH2IElQkscpQU5zXxug1CazE0r18jl7cbSAomNW7n26xjDmPSOwzVMK-0wxvE5yXBrV4vMwzwjX5jT7lZkJ8kAgdVHl5G2xfQTlyDOOtGKDhMmVsxWm4yRhxzke3GmHKzJ5UWK1Mmszq0An03CwFDejuIrQOn2n2uWLZNBsbtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6CALQ49RQhjnI_GxaP3_A0YJ5dr0rH3bL8hiRxtRMp8gga2XMUqxBYdSaMiNK8DolfhA3ntgB5lBhUeURet47jpjH4E46nnEnbGMTCrpzrP4ePkzPzMhfFYaW5gGyeJQMbF--zLfTVOI5L5fYSL69MiojM0uLJfv4l3-nUAxdyPL0Npk3ttprub7KsXaPoy9Dgg9RwUIPeLhrZV3IGOPoDzgUg9Fdaj4N8OeGQWXIyTbgpxciZuSsA9NFFN0XhkwMknKvBTXrGkF-kBKXjLMmqXyuwTLEYPeUOwtdvT-C7DAEzgH_hRZDsFUD-KmUMQGc7ptrRjgHawDrmiBgUOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPJXn4yB1BKOr3qVrxmdWPasl45wLrSj2Z8LMXW9Q0AhNPU702OKn5tsa5xKIn_a01Is7P92bWWlV-g7Np_Rt37rCcLO6anNKlRFlVN-Z5fvIGZtuVN2ONLc2Qt1eWQ8tr3HbXlooYG_CRMxy194eX8kGfQZLxkSzy9ipIxc7nMR2FQlCuO9imNTbNC5NR5-T_ZN--cYFCYA_9Qfwdh2ri1lRBejLtNIn5Bph2vmbLEbNcWkmrXHuH9KiZkh7vc6z7PqLP47TstPziCHbWYuw6u-S-kyZ6KUFTAT2nvM68hwBjdgjLNoIwYuzQZJXbDTVWsjVcj3fsBX07Mt4DVBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5YHMOFPLL_VgRGDgIQ-QJ63MyA2TyUdvh-s5L_oxmFw8yIg08_LdDG7j2wqNk9vxxf2pECfLEfXUfmrk6O7CM9gwbNT0xLGB30bU1Y0DlJnS5ZfhJw-MEbrH8Pd3NdLlO4twD7w3Bykdqp7QjVKFhH_ZaV5J_GoM0IVjfKek1zA2EuKlnTI9PCxoGkxsjgxJT_rbl-_ssrR6kseMUBvCTWPqsYWTVRnGimsfNeq4AkkRyekK-oM36Q-8wFi2ioQ8C-F_fgdssGjbrPDeLD8kHA8X9gJ6IZi88Kv_6tbVEENXrsmd2T4KmrbCFPYHbpkGo8zIvGkNv7WX6Ns15x-1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwUcDN8jEVFXgueHPaPzvA64GAomCIPrjPJr1zbk8WIfKuxSoDgqWvQjcHqwpkXva_1lXLO5xiwYZgyij7x1I3CnfLyfxmpc17pOiqsPp45wlqjFa6QMq8VaWkIOa3QZhmk5vlR4QDRMvKGunt1_2LZaHd3Wv6j1Ytj_MEQ02I1KE-IaH7je5S8rhNvlyXZKpGVhrmc14MY_cUe22b81ulecnP0EMrW-GsUBUZbrm6hoyDN1tRlLmLfRwCzqOfVvAjFv8ucEcFcK2dmXa44_qGPWvVBIAUiL6U44pHCKoJv909zTFNqZWOW5nLa0bvTjt6czVD8ZsGBBBqMbdyVaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2rmGWA_L8nAOt4cHnCqDFoJVFhjZKKgnMGfXFiUcR3mAiyQeGkfHxAO3p2CjkIWjv9TaON2b5NVzCgkbwfaGdNwG87EBtTEUGn-XeAgpCZMl12YAC2AtzklRelGN1S8nT_8fv_FMOBMvDIxQuUvOUvB3kEKklut1WG8Nt19iqsaGwtYxyP2bjkaoH84GLN-JgYzGjkDAGAlctmdxLNqVnxRcQpC05sLcUUzuhZX-vp6fm6FuDUdi_gsjGa-U_XTL4vPDPtjva_net_tNUvTASZN7ngwVLLDHVDb1GLUoNWCEbTwTHlpALbuk2uI4Z1V08YoyAZHSW_i4180H-xMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3B7H9xmk3kekKFAzrFRaeq_8jp1cx8CJBi2PuHQrmQPyUrYpQJibZF4WwRVrJXfl1IOPQFDKjgmS8B9QA0lrahlg1OPz7b_uNjrE7yeRgJCslKjGmswYF3l3d6eNMxZU3wGilcgm1D5VYgNedcsiI-g09DUs_-9Xbv0r4gJNxxvdBhs_ZPOwrE6DrWiTtnEsXooEmAWsYN78P0f1R-OK6s69w9xUs-_yPw7xBfgl9KBztFfFaACOiCi6Meh_eB08N8VEH9yOV0bbstM_FBoP3sWH9f7q7dtwB-9S-wCfItP78jxvveccKhVkf0e5eduDxtITZTRGEwqvNu4plZh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPzmOas3jpESLGJqlYtgoP-K8yE3ldLacMIoepkC2pXWmGKdHHBzVrBiixVfXUl4X4FT5V4gAlNnRcdLEEgE4q6N3sHCiAgBRrE1x3IDqqDhAalg77AMurNrTd4tzhPCabdQ-WQ_zJPh2yUnj6l9ewp65nRqZY2Z92yNHbec_Q_NOXi3xzCTuH_bpKz7cBXQqbrwUh6XnyFfPoDarCamMpEE-3LR52vnIqrXr9m_tWj4WMP-pDDWHhnEft4dp33fgWNJGhTPK-3gWsYqj_AA-eNyI3hCR6N9ZV7LlMeJkn-hx6Ehradc9Q7TyG2OhgPul6OBcWKiCVaTFp06oo4qWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G57ahAZhoEbroXyD0ofi8677z4sjNc2rhLWQVK4T_q8XVRlht5TKhIX6oOjGIFKHrgYv0guUvzjejznoUCO079ErG8arxjAGNoevaSc9ZZjKg0aH2z6PhyE7MJV_evdOfFhnGOW3E8XHLw4xA_q-PQZllNB2ZkeY98xheDjZI-bsRT8Y52mf9LwIge8yEQzFwTzF_HlZ5lGXh2K5aVX4K1EcnINhR3mtoO1t-IzwL9Qrw2lITZf_beeiUUwoPA-OOlhb8qoMqOH2ZACQ-hFzxa81wPplBzUfa-QUPL-83dQkWc-ym426Rf7YpOUCr9qzt8krQRBSNrksx7qDjH5JKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
فرانسه
🟢
سنگال
⭕️
⚽
عراق
🟢
نروژ
💳
حسابتوبرای‌این.بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
26
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23615" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWigVdpuZzF79RSbJQ1o0FN7pr2tqKnEtdg3FtrXho4JRL6iyeoCTvZYBrULmMSClO22SU1s02beGXUt8tZcyAf3GExAPbbfrtzgqTSpGd41lQHAN6hzEYtfT0YfLvDWFyKYVFKo2qDSS_dMkcJQuUB_kZxjlHBMMLjBtsmr30jzAnHMvuu8AcgEAlEo596QCjpmiwbBaJPNyrV0Ct9rOzELCqJ4TD8AXYPXASv0AnM8dl6WTUYJ2-hjGrMTGFn_dBAUmGazOby3aixfHUcVAS5-SgRh7Szrv8wa31ivR9CKWxIXNxTEMWUma-W6kAf_ftgaZb5WNXXorejxMjQ1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw15cSoqqxvH73K5GyDCV4pzqdGBICPvZ8TwQG_EGgqAXRytHZUHk7YylibF_erOxA8P5DbtcPXVL08bxEXcLzcTzCM0irY_LFG7iE8VXAlwTMi7dstjDsWzATNHP7YQdL92psDAYBsU74v67MrHLyX83QXg2c7S7RqctqTMOIGRsNMz9iSAUE7ov9pK-9XEwAsX2HqNaQ30XZiJoPHzvr0u1UD7nwUNqeZURhKr0gtZtgJuvgd8nEL39gworHsXEgkssrbuIwFNfyf5Fjep80MjDxfmei1z4qnKXSQl3K3l3i3PnBqCJ4QM15jygy8F8bWTT6fYFtPZn0LA5Jssqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEgCiO7A8U-NYLa-7jrqnVM1PtJOD6rTPYLczF7ILllfAfRlxT6sp4GwSWINJWEAIWJN8VX-YrN-H6UdbIHe2AXNpntfmCFr0bEjVKkIDsDuHAoIqtUSn1yBES0Gq15EW43Q4eIrpArgc9E-4hUQ4BZeSlcWCic5xijyrhmZvTaCLpPdKy1fdgoYfVJAXpKtQfH9sUcCMMBtKNC0bLRsLYXXBAoX4Bu_oxj2-XOY_2RhG4xVydKzt2LKtH0vFHMcotuZK0g3X_5tD3Td7g-u4gsle8eA-v_2975ATDnjsO7mGq12JWip5DseC1fArL2nbuhGXTFJ7DwkCpSNtek-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1q09hveSwxdW2LCEFtXUgcqXKE36aSYTiZAGsVkH_PxZ-SPBsoW03eHAApQi4uX2MPhETAvBuiASSZgm9YBf34HHFpWjtHhFiPQBJqrWFOQYbDRgPNtcQ5wJqGZVh44KQqrZi-f5BHWiBYF8HsjwGh-z8eAko_p_moKGZc1z2g9WyC8zxICmzzDwFdEJ4XFJvXBuTsCPkI8n5L_Z-g9AWO3FOTYhAFzZsKLlbnYC1qhuwhvsTiH9zGx4q1oT4ALMgvsVkbCcQ98rcNLNQ48bo7vCHwS6v72JCVHzjr-gxs2oCZkJqg_TeWjzavmx3Su45Vu6wy0sHExbENBPMIuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSBYZ38532vsf3p-Pruw_vzFdBSBH5t4xYirl1o1QvHldE-NCGKI10bNsKYz6WN7UX0i2UUwLM0IkSd_u3wYJvdwojW3UaT4IjFRi-S03sCLUqmAToYawc088rtH5H73hpGb6g2YxhiJ6G1ilI-Nq_VIkkViH2Aq741v_lNUdrT9YEAE4JufblXubS67GmGfIyG56Ty3F2IYjHyzBBTQ2m3UStToy2-4o8IePO4VsJGjlQ77_ZeofRFpCTWmIRBXkImO7gR-0D01Liq0BcL1xVqMZd6NOJN8HUtABrDx_4QeObe7vix3cjm36OG8dNjAGa5afRQrd6r4rnXHad8pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-dSBrAFOoUlYPpHv00YcWRVZQUfCj8AYAvEUWD4Nu2_O-EBUSjgPC0ShW_eGf01Kd175UYpq4OknBDPCtlLaz6z5f51vM_pHBf_BNglvGoJau5IBkxO6nNVGZXQKI4U0vcuaix9B3z06_a2mFXDnV8CfeosRbmhXCkEiCwXmo3-7C09_I7uCF60_4UXxJIhlaa8H7NBz__AzHqIsw6vifGLs5LsP_rHddoIFKUhASChnTBQvRXQn4qrgpsWQbjlfDrlzGo23Gen4ynkE-6b4WuWk2megVQevCgeAX6GUbu14cd-41rus9RFG8_f0_ukUn5cjKzXz4pvuBOlXlf9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clSeeqG35B79nIJQTTm4mSx52ncPYLZ1rLptWNK7D8bCwC7to-TRVcU8eG_pmPRnqt2mYRd9f-s-j-ivRfX5bns59y3oJRT4P-5x7UyZsJ10Z_WSaImzbXe8hTty6r8KHQmrPW03Bs_ktD7k6k5aSP65W1RBybm5jjNo6q8GX77GMNQpFJjdKrKne-i0c3_pZSgKYQEH1hdiWLJHT4G7VZbR-kuqANvqGVS7Hl04auLjiZKSg6B83v5RnUKJT-bVCiR9vLwWmmKhT0erfRmLnNQTvsRwAT7fbUtUqmA3NIhggVMYtgOwy3eXl8YpApAPelzenYkKhKkLBAM2CHIVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTH7T12lq9yKzUR6Yj_f7du13UDtN7QqwqlwOxxbEzgNks886RsCbuAGdDQfGFXi4jbBxL6heymrQzydK9x0FOJxIQiKklx5AxvDcZl-JC4cnbppVkudxFpM2Vqc7OSsT5pLVnOodwgeUCjywfEq-TKoPX18OJMulxoXKS8qZhPLlnel4j-9G6VCc3AQKpsrwKvsNa6C8sHqYCqWYnxxcE82Rwg-JjvTHOWA8_d9y98Q8iRtnlyNhtUsTFmGo8EdKHiehNNDyvUBbzbJ3OdtXAvGG_qtbUovZGi8DSXTOxKeCVC5ebcC7ox0MZBu2XN_aSFHJeieXBZqVjFdUC3Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVEQ8Dra7OpspRc_sfnqP9QHylNPiRgLjfAKOCoXhgVcBimLrsD5sAY2PeLk8H3Ekls1sXYEeshYBGIfUIpcxLBygiPBwC-1mfZYIYgXFUaKPy7EalDJCwJ9hasjRRqTfPT8NLo7QytHpMHo3OR7Gif21u803fWn4RzK66C36IwptHU76IG2renzhrUxuqTIFex_EK5V4itOqA_FBdtub9oAfzGzVXfutepfQyCf62un31dgCOyJK6Gz-J2txpgnf3HaIrzEYcj7P4o04ytlF_w07sESqa_8d6kph0_mkS6r7PcPPXtU8wr7Twq30976qOao8jBbhZ6_-1CuKqXqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVbWehCU9jbDtKLWbTiUvN7X_pk-38VdZUOu8rj1x0dkJuTVBx6XYNa5oLLpRR-dKw1EQruLfBhO9_-Ut54M9SFAbHSL2gyvYBoygVEmHd-3uEs4Y3RL2xwvV7xV0bhj_5Miv-pgQSUhaUR8qnLuu9X8Tjd5GSI6U-qn5I3EmtuNYbfcOkzRJFYPqBJ8WUCbwJsrwq96Uyl5mFSiMrb4PhBw4kTt_BUNYm60TpqzMtWhyMIPYMBOBzNzXDHfMGoLRAoh81k5Aq0VdYaJeefNDBpfHKq5WGVXaLtpEvQIo4TBYfRVyTwORqwd1rmU-KkWLl9vy9qj6PDS7wA_ExZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=vK_AW_9_Kyqcqsn3sWPkep6MepmfXHArefk27538Zsn5dTpa0TdMgOolTAl-atrVFGdPJPGea2fyXj62gszw0rl6GVz7O49sLDEO37XaI8vZMVI2rrIO9-Wq8ZWsKSOTTfuwk0vTBMLPYaEQBztxUZQh-EeLm9LQfkMOz4r-6heVzx3lNrNavaumCeQLognbwHkyTCt1mvFK4IkGlWgoz17TVefO570iFHzCbH-m1hrpQzTeeOP8iJxh6OcH4t0vjXUule_sZgeJsgmK_TiwZUL0i1M-ji-Q4RuSrNY0ddlOeR2O9EVZRrkiwof3B7aR_FFE7O03AGS-Whxv55bBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=vK_AW_9_Kyqcqsn3sWPkep6MepmfXHArefk27538Zsn5dTpa0TdMgOolTAl-atrVFGdPJPGea2fyXj62gszw0rl6GVz7O49sLDEO37XaI8vZMVI2rrIO9-Wq8ZWsKSOTTfuwk0vTBMLPYaEQBztxUZQh-EeLm9LQfkMOz4r-6heVzx3lNrNavaumCeQLognbwHkyTCt1mvFK4IkGlWgoz17TVefO570iFHzCbH-m1hrpQzTeeOP8iJxh6OcH4t0vjXUule_sZgeJsgmK_TiwZUL0i1M-ji-Q4RuSrNY0ddlOeR2O9EVZRrkiwof3B7aR_FFE7O03AGS-Whxv55bBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSah-oagIjZSInL1ypV_MUzj4rpr25KfqauEZf-VmdQukPQ4bUYaE-2OMzymME0ndK3LNIapwlj6PANHEPdnfWK2PzOC8OnxxYhiIEknBw1DayYzvQSrxv-tVyDNWqIpMrbDjn1Xxw2fauD7PG8TNz-GlQKz9WULzVLHQnCAYj8C7mMP7UVIXj6Z4u8ON9wa0HLyq2xn9xFt_VbhAYpPfSAPYs16RtFaSsuSADy3ZGV8ASJX9_X7HBl6C-4tjscOzu6g_kaGlfoahHRlkGBWxGGINMcXLX2qVaxPN4EpQPzr4TWXnYVe9RvL735aST6vXJf3qlUZryRbWf5NQqEObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf02u2wFYmQX2ZUW-SrjrKbStBCifojbF7MkYqPSJptW1PZlRFDG83Tk-iBn0v5MzpMkO8nUqF1HLsjJa1RAzVkjudZeWDkt5ccWQXrCufkbAUGHbVVv7gUzZIDKRue7ZIV0XfkUxgq7TuHkr7aJtAmM6X0R9CvDYKTAujOJ9mMFayjyoXn21_I9XPrWzDCfjNIkIDx7IT3XjVvLL5V3dd15ZzehqP-r9PS0AqDf4mZ2V2REAVhGkShhPc-p-X2Ml1-eM860pqY1vq_-8-zkLJtLzWC2uxfcQ99dwMuUcJsgqyczaSxX7J7JPGVr9Q7P4I1pmvOj--alwM17qdIcGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=fumm8TLZId5v_7TKXlZRSkPAYdM34EOCMOTXpP8oTr6N-iNhlg8eiXGjXlamgGUIj3FbZugEPEJ0f99xuuW-WCimtQk5FiZGa9LWiPt7W230cMCTeffnIzIEGlWrqV_ZS_ePYXejBbKKcElhJcLDJCWWplifQrR-fzVczZSsQzmNwJaOoEOlXAnY2o_j22PCoZr4CA1bcLDhpjZv_bv7QtT0qSfCT_NJ_AY1SzviMrv263DOb_bAE4xXRUthjrEgpf4w0ZoN-HV2qW36h8Hmb8aiigdBoS3Gj7UBYc2EQaNyYJDHWTMl99vqEiRtU0F71o-33akxPd65YGgMVuObgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=fumm8TLZId5v_7TKXlZRSkPAYdM34EOCMOTXpP8oTr6N-iNhlg8eiXGjXlamgGUIj3FbZugEPEJ0f99xuuW-WCimtQk5FiZGa9LWiPt7W230cMCTeffnIzIEGlWrqV_ZS_ePYXejBbKKcElhJcLDJCWWplifQrR-fzVczZSsQzmNwJaOoEOlXAnY2o_j22PCoZr4CA1bcLDhpjZv_bv7QtT0qSfCT_NJ_AY1SzviMrv263DOb_bAE4xXRUthjrEgpf4w0ZoN-HV2qW36h8Hmb8aiigdBoS3Gj7UBYc2EQaNyYJDHWTMl99vqEiRtU0F71o-33akxPd65YGgMVuObgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpXB6ttZWna_gNDTvObKtGNpaO0S3Aubk9ZOLgA7HqMU8QeuOhRjqsTQ3AYSP6OeK59kFVWGsjbNEQW6GwQplOuWqZAb8I8ujJAD_c3s_XJpfkIFFyTAvHBQL-oXLMv1XegBWCIyn7VA88FG8YpHQeFZ0g_ZKAprWWPo3z4s78blrhtV7lDZHNTv4KQKB4NLk_z-Mv1iqcsVwi5YQWG--jaTrybvCq3jAvIxC6mmghauIgw8zB6VN7g7THg3mrBnkRefoHgaLIgIi_lOaXWmUzgOSE84MEAaUnY4bVI1sXIqT3BKRo4Ankv4Z8EUTigSKGOVBaRDkLPIMdoq4mrAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz4aj0geGm_vKBUAOLJ0OEiL67MLeBPO17ABUdVHAtY_vDmob8NFZ1QdH7gEPdh0eQBQpoamLM6emELGvnMMAydTcrs3z0AR4-GZUJWWAKyrYC0_PyDyCmPKHj8Gpi0ZKh1YKjigF1oJdkvPnLWMsokgCXTdpngZrCD1BAdffzPemEXotHCs3eJ_shVSEXnwdfpzHIerrV3_GwMgxmXV8TKmoNbsUvIBR6QaidgJJR677iYSmENIFEDPOsrVEAGTMEZXzMQ2Uxvm81rrOYho7A7ecyZkAWMkIMLKcXlGsTQ-NvefQlKBCxrR3ar5irweOiKXX7N7o87P0N4r-2kYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEUaZX5RgpFR8592tCZXWZAc-Mg8jN07xT92ouGDdxSKHx5cTPnyfP3XrjZuSUoCs2M3mVfE1t83nDHcM3yD2Ua0ooxN4cfYcDeoSNQ2RegxSuIEK9eSPNP5aXlzrUeS6IC808guG93KfA16hlFQFl1y9qqEuCzIH80s3k132yb1y22c3oHP0lOH6VdJzctYzmU-bfsFTj7vwDpO6p5r88HMef1zqwxVBe2MbSPu7YrKEuEoguuCFkeg8a4cIWSIe3nZAXVV8EtE_mTJk48WNyZ3lIJk0Elp4OGUkSJ0wLMpUrfUs6nEwr8ebY8xqdNSnUQdwNDqHg5JJNc72PPwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcCf4eahGWesWECbeq_1xLA-982sjlr4i8u3Q2bLSbecsgU2AfVhAyB0mWMBXe8TGjSkZajLOU2ovrF_WwabuyHE0CmlB-Blk8Jm7k7CqaAoCBtL57o0t68mXQKOyFAeCgAKqP5dnCAROnUX-eGW2bFZpEzwR8HYIMqQCOVXugsEYVZfflgn6dZQCNjoeMMGttwmsHtRvxkBByxf4WGXPEN5LlXj8sdj5QGfyj_2DuWVHTR299kjTMUcgVUKycreRhIdyUrr2xoXZv-0SE4KKs8zCOSSnHCObq-9M5eHS8CxW8pNrA9rkGKxwRcBLFGWlQPKajBUWUfCWyrYl6DYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_QjYFDtlW_9CPdejvWo9niMEmnLtjFHbkAzupHDMzFmqkVAwZtQJgvU08f-uoGOXV6vx8fc136De490qSHXgCYGl-xC9Vaj54aJvLbZWqOoomvYG05GsooluLQwkGG6DKcNFVjGLf2ZjJdhHViAHn6v2btmzkVORNhyRWQbei5eJW_gDch25yQD-vrpld3Rbam0t88bB9gtnxDhjx-FY62t-AatZ0y8Vqls-o7eEFGFAKPqvAwjsZn9MZ0Dq44eCmyBvK8KBW5ucBC-ROKxwNvuNoof2hQNJH_hcDkpn-G9W4EaYwltX6D7HRf9muunLY7xSG6oeIDDKD2QnkrwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-tq9ij7eP8QWhvsvkU3_SMgVbqXP_lBQ5_JrQ1c7tnwosmih5YdgbgKYEKn0_NAV6x7lTsR7tgvTPwuKpXwc1avjf3qGAH-ir6Q2OxDWw6BZ2s1Nq23qsuKC4hAu5Yl3E7yP_ePF95SIP76ldKdmUi3bYptW7_W7rVuwwCX-yqyC-TKfyaMqDzdr8Nmq5GiafgISxYh9WtwSi7qWLOCXOeKUiApx2TyS1cq_oCPAeyZ-Y4x-leZQVj-OIWlULhpHfQiSKasy9ev7MQ144pFKzJ8inY3TMfjWC1LHGU42RferaLfL4OfpCwcRoflcn0hdBRTeQ5pLJYyRXnwRXXhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=CmZ-TlHH3Ua4p8DRbihVkz9Bp1XVLxVVj5SpcHNOb6GsXaS7PB_k3uziCkyePAdKS7DdCDLwCAzrVH-r2G6etFCkKMJxVmnvIfxdCwsNDiBbl9iWIOVF2it8G4Op5Axo1g-KCsyE-xtvgX9klZ2tvZ3rnyS0GEOWjVwo1AxM4W4REgNOwuhODRCjE3D0pfcP5B0iRxosKYlJN3aY_WgmFcN7_iYA57H_MHgSOiPvRUgTgPmmYb1XV5cygqI8NUMyPez7v2NkBpqKzUp7LMOBdGbihYnQ1hJNjSMJL_4PwC3mDtMhI13i71NKiLbiKAYlSkBJ1fXOfFDr8-ggJs-cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=CmZ-TlHH3Ua4p8DRbihVkz9Bp1XVLxVVj5SpcHNOb6GsXaS7PB_k3uziCkyePAdKS7DdCDLwCAzrVH-r2G6etFCkKMJxVmnvIfxdCwsNDiBbl9iWIOVF2it8G4Op5Axo1g-KCsyE-xtvgX9klZ2tvZ3rnyS0GEOWjVwo1AxM4W4REgNOwuhODRCjE3D0pfcP5B0iRxosKYlJN3aY_WgmFcN7_iYA57H_MHgSOiPvRUgTgPmmYb1XV5cygqI8NUMyPez7v2NkBpqKzUp7LMOBdGbihYnQ1hJNjSMJL_4PwC3mDtMhI13i71NKiLbiKAYlSkBJ1fXOfFDr8-ggJs-cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzSd2F1uiTjF_ND39pM8yo9lqYh17yJqSUYt0fw1xaa9ZpF8Q7h6HgIQGB3vDIyl1TaEbmBhsSCFoE5tKdb8eblz5sbJ0u3Ybj3pPSD8OPMmDweR4wDI1ILJBTwou2LQr9WP_DNZFruwb71S9NqVfG8Izy1uwJGvxaMjYLGksxnthMSJYA2BdAe18ep6BPwTRt_ZTrMstfTyujEPX3-LfqETbi0f1TOlKz9s9AaxKa3lgJ9Dgsuts9FSZD5Fx4jwDFb0oi3SpuYDd2qX09TN0FCajYwDFTN1W0aqyunPx_tUBMDqhFR9G2Ig57Qoxf2UnWZYk9kEn81ED9mwC8RLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0-Cfw1KI-OkURudRGp5TYb2MqJLdPEN8wUqdYa1ySpswOyLbvHkE68eprd9p0zry62rWGalsjQ2KNT0Tse6V0SDVmZMsPkg4-8StOGm1-P8vQ0JwLhCOGZczerV6_CwDcwMG2S17xuo0-5omUihBSnuLxLXWrL4Izhmy1bbxRaJffUTkFUnTrO69n7a5bEqzu4Outw0MwexDSZBv7G1zKuY_LXet6-T1UTKn7oeWz6HSE3D9raJKlse32rab1FLFpwlF9jgIGuBiMHr0UobKKTrLAfjK7DkE1CsmsqqD9AH80kvhR4RQFKXz-s_GQmf-0M7OTUqAGX6R7goaCOTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5FoU72BtComQBfsXXD9sCLHMfWNnXWmGQiuBBl0GuYHD_ymGjIhYS2rIKcJg_zhGRZak4U0g7b70sHLYsW2-952w1kWjF_23Hd_6-kUa0OKIdeLdlkpt8KwiFx_Ur3q9iUd92r_Wm2XcJ32foGCi68S-dN9qI4DVX5I2Je1JWuZaMMEmow81b9J2lGk9Gj6jtKN1D-oPobtbwYsIts51-HU734zgceeLQekZ4R5IMUuSpWVYZwGkmVFboPHN9cCcgEMuNJaP7KGrw1T9f53Bg3MUzDqiywaomZSXPDZGWyldL50VWB8K7ke-A2thwMChbtclcuI8hk1z7fLtGaX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym-ln0nMe0qLgyA1yL6iBjcmyAXnLSHofRjvLYKWSQoHGWHpu6M3brTkX1sGYidqZky1ooHRJccBd16GfFEvDyYFQFTK4MHAA2Hqj2ogU2lsvuqlusxpFuuSS2AoHqy7t-w0KThQInr8qepVq4jF5Yp8ZgkvJyRkrq24IrS9HHgIgCGY2SYm99XYGr50UJMB-FWELvEyiQFnLyCX0DRtmQnWWuP0L0YgoYqohsclpfzyhKzgr6G0GNEEEwNzIDPr-SE7lsjR36wcfllbjWyi9BzmScfo39tdFn7unJ1YPQ-P-uaE4JOJAdNW9OFES1z7BU3uuNy3xxlCbR4C6YZ-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8ASf4wEoc2ox8On9iNX7GUaqmRF2eqV158GYyJgQfdKFqBnWvZdscjL0RMWHxoqqhtJXCVpwIw7afmETvVFFI_hyEwPrtBWyqMalJHLnYTfe_IZuXnkRKln5kO8j71e8fA-z5fJ-FKUfOLSAgKQIaCU40NHMd6hZdEGd6mEddqJhMo4HUidJJlCbdvOrSgnBBSvLeZeiEEVojG30pLzffr5htT4yic7S0NacOQUgG8zkpoI4XcyOrazpe4uIHTBg1QBJnsKPG1RIzUbh4rfskevqPn0WvgRgjUcQUYpebHAaoP3eVW2LONSnL8LqWDeVZWUrXZy4z9s9ABUCD8XPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXWw7tGVTh2_BLJBVoK9oKuK3fjbEWevpAmzN9jOVt1C07n6Ug6bWNZLEbbn8hTuow4XADdDUUiVkQimR8JXFzDe3J2fVb8wTSCIrEYToC2kpwcjFt-q8k1zx7PNCwG1MuS9f9Lq_mMKGZQBGOgRLZ27zEDrJ0kNWnvUAUfcl10nY4G2fmC7vFKnB11eE5dF5y06h0eSHHQysoW4C7vd-6x1q0W4dFFvxaGreBMMVh5VoBSK3CF20SQKDv9o4GHGlXtvEw8lFLAGaFT_3WObTdMCG19dan98RvV9XYBmVTxvG0IS0Ts9_lsN80PQ2GLHX9bpZXRG7nkdOccCj6LEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBEBsV6kZoHh6z20-sdX-AjzH4x0C1QbxnSRFJ5Kl6UsO5HsDNAXXrAJ-NB7Okozme1TjDM1tBm0lx5D4qWQNcQdvgHGEw4sOZB_w-T4x-95mHzHdrv-CG14OF4z2vtINJVfWmX5XUunzJ0PHqVg9GdFFYEaffFvfWn1nv_hSd0E07b-6P8kpVR9odKJPO08tDC1hj_2_zrWEHsc71I0ekr6Ypd4ZXjm_NGtzbm0e5OEVwN_Uac14ZRdoI5AIsg5J_rDq03K4B75SKMq7yPFZDFnq_8TaQN5UQHAHeyFLzOuqBABGMfEgxywnl-_juqv45YFfGahCsE_hV7aKHBzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwVCDYW33KTX0lyKl54TiD-ZwZ-xfx2pZZmW3iApjy6coFKJZgauXxaIN7wEcwwi27BD9QBaf-E2XhApwma5uQorJbi2StLoskq1VFAC8C2aalFEcvKNX8IhGtOf-DRJmM1waIMAl55ZNyNtGuaVaEnEjhtvM2WDl_06bW6RqTmVO2fulsoQvZjVwtlpQcVxIsX3mZd5dA4xOOa0fmn7-QMEx7A_Ea82OcJtz8Ba8VdtSUY0mlmyt2xJ58mzU83jMTCuFpafRZE4QQkNIqLsveThr_pwH3LsTvpSFYDM5ll5F7g-rA_yuhI-4YAZqjN6dTN1dyQX2TdKvWsxAkldaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=E3_yN8UNlp8KiqC4w3Z5BErU2MVJraKRuBCpwz8oT6vZ0Zn2hTwaLoDBDBSR7cRfbgaaoguWVhBIqpB9iebKeHLjFNvxmfXc-4qhKjJXYfqvf-k6XQn1QDTLwMyOBEkGCEDgE5boVgQ7aYrkOA8t8xcWzKgz3kMroROwujEhZ7_9hVbT6A1PWOcBWUI8QqbLdWwEgDsJcsxxtGeyaLYBY_iXzcx9j-CQC8vrQq1MmxK_Ms2_nkD3Uavkeg6fTBOBPNyT2A2vtLp9E__Elqts_vO1ZEd-8ouhp6VrqLyVpXzqaWwmUFm-qOygk4vJaNabh-Al6f_zfj-Jv91kiDU4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=E3_yN8UNlp8KiqC4w3Z5BErU2MVJraKRuBCpwz8oT6vZ0Zn2hTwaLoDBDBSR7cRfbgaaoguWVhBIqpB9iebKeHLjFNvxmfXc-4qhKjJXYfqvf-k6XQn1QDTLwMyOBEkGCEDgE5boVgQ7aYrkOA8t8xcWzKgz3kMroROwujEhZ7_9hVbT6A1PWOcBWUI8QqbLdWwEgDsJcsxxtGeyaLYBY_iXzcx9j-CQC8vrQq1MmxK_Ms2_nkD3Uavkeg6fTBOBPNyT2A2vtLp9E__Elqts_vO1ZEd-8ouhp6VrqLyVpXzqaWwmUFm-qOygk4vJaNabh-Al6f_zfj-Jv91kiDU4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrRWJ9EIo2UY8g-UP7TpYi1aHqHW9NJgy938NhXCjPwEAOx-Njro8_Vrph4kOYZHNiJ4VrDia3PgiBFSrHfRUXwpc0W_VqXKfO0FDciCKvFmouK1WBEeANGnA0quFlJtk1JTTLOM2QX1ywoY39mNsKWiWmHKGfiA6Fj_gPsSXTtvpG5lwASC1tffBm4spJjEUVVXUVRBg8l2Qy0hkYASrAAS4hgw8xiUUH6e4jKI11MuLlIoO8RTYK9dxEHrWtxK69ncJH1Afy-gak1DH_iaArUd4BifudRCf-xkrzAUQzhwsc2gdsb26UfD3ZTQJjy0Srn7yj64x0CsXTogWz-Gsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FrPWDm-VGl28_a2rNrW5DHSrkueRSof1oVJVhnp3JSfOqVJfiqeIfebSFEj58g31oGcumGN6QYPPM55vMPGRJ16_XO5Uja7VlPBV4NeYg_Za743RSFxD5aOxHJiOIBPHN5H83iG-Na2obYzUvblIjoqBNq7Dn_Gs4KJ3oqVdRF9O4sopbqWfXSK7hKs2lKXigiwzU-sgIP8h8oWq0enLIhwl6Zde_1eGWJtteVuuFupQz0aZJJR2ryD9Wd9ZhoVAQa_AScVXcUpJSIPOBT6AQpRRTHAP8H8v1kABRkTlOolvVC1xLeJHSfeTvzwPU--E0PHt0u048ZqOhEfgcn2BaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FrPWDm-VGl28_a2rNrW5DHSrkueRSof1oVJVhnp3JSfOqVJfiqeIfebSFEj58g31oGcumGN6QYPPM55vMPGRJ16_XO5Uja7VlPBV4NeYg_Za743RSFxD5aOxHJiOIBPHN5H83iG-Na2obYzUvblIjoqBNq7Dn_Gs4KJ3oqVdRF9O4sopbqWfXSK7hKs2lKXigiwzU-sgIP8h8oWq0enLIhwl6Zde_1eGWJtteVuuFupQz0aZJJR2ryD9Wd9ZhoVAQa_AScVXcUpJSIPOBT6AQpRRTHAP8H8v1kABRkTlOolvVC1xLeJHSfeTvzwPU--E0PHt0u048ZqOhEfgcn2BaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaLDzefXwDk6dGauNAUdPYWl9ucmsi-qW2VCEE1yPG5Bc-hw5QNJLUARLKG7IEfDD2BGFr1LEx1tOVB93jOvG0J8dQmeTpj0-ZWLgQ3sQCFNCU78HxA2jKjyhDS7I2OIyao65JuNfbAc7nVpRy1ADH7AnEGz1REx5OV6Pt5UzDO3uwgIAwX1bQCHHndAnCLhC5KZMlnAqkGyIJp6Oiv9YSjIveo7TEgeqpWIrEZcxScOjLx2evSwu3D-_cDu8z0Pb8xLShtu5Bf1v1njonSPL60JSEE9MDc8rYvQzYTeMCHvjS1PqmQ5NApw_CrReUh9v-GB7MQaFBEJ3f9rEwA1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoK8yoh0jzRqJy66tRx-ghMHi7D2tUrxluEaKzZD1NjGoWspkDDH9D1ePHtJsspht65IcvCxQyDUYP71eYKpoQn43JKQvIdLYZ6Abk6B5Qm13H0sFAvJuVPLduZgmI3thPdCInH_Qhqzvy8qNnoCHXRUdZ9UJBphfKsyWXhzdGEGBos_7jqSvv5CeOtwlzas_nq8k3kooWMWcPZ5U0isR5e6_xxpY31h_F1V2LUPAKzmEpmeZI3s7pgEJHYs3jv1jEiaJx9yfSrCNlxg_nvGSLbiWZwZyU96BEy6N3bLnOj7uuKdjlk9xdEFFznMQzhFUqn8o10MuIP7PvFBhgZZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=QSp0msJCFQWcoEjpYHDyOzF-gXa50g7G1lu6JsPCcmlsSDGQN2fDRfhnVX5GpIPU4GBGYtyDsYHL01w4ZsFWn--5RQnCPSRWW7ZKAKbcLJvAqsJ8HAUrrow_psWgG3Ovewom1nAVdDB6COApEF1dXghePQmM23yLNKvxEYIsFU90_ImZmNyfRa5dauVVAlIl4HvjUPDDTiGVyHffZdc9j4_mBEKlvu-T11KuC2TCbTgBugfJ0MdHgRQNURhmwGCeIecI_NclHYECv_p9vNPcZMI8-eX0IVQATaXgnNBrb4SeDp0UQ1xLyBELpp842UUSazQiNDMQ_OBvkySDpZdLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=QSp0msJCFQWcoEjpYHDyOzF-gXa50g7G1lu6JsPCcmlsSDGQN2fDRfhnVX5GpIPU4GBGYtyDsYHL01w4ZsFWn--5RQnCPSRWW7ZKAKbcLJvAqsJ8HAUrrow_psWgG3Ovewom1nAVdDB6COApEF1dXghePQmM23yLNKvxEYIsFU90_ImZmNyfRa5dauVVAlIl4HvjUPDDTiGVyHffZdc9j4_mBEKlvu-T11KuC2TCbTgBugfJ0MdHgRQNURhmwGCeIecI_NclHYECv_p9vNPcZMI8-eX0IVQATaXgnNBrb4SeDp0UQ1xLyBELpp842UUSazQiNDMQ_OBvkySDpZdLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgXPYZoLtQBeBpNGkf7FaGvuJR6BwRX2Ax9iEsFR0L-jm-Q8KxhD55UyqIARgD94AUWjDvyfmZHY9CpZyAwiFZ9IAhlzfMWEBfJ8pzbbO6TKKweJbA7uGiCgeDbDAjmlumz9TDNQ8_yff8aBaNdeZTMPMjs_EfxVmQQzvgmDMxKlRohqxG-hYsJwb2n5FGLjlKVIZKe7pmmDIuVxiptXDLVX6JeXUS9inJZGTgemMarD3yiZrkN1sae22YfvFq5SaNhWvQCTgEVGytB5MmZMt9yj29l8Y0ipb-R-njqZreq-s1pt3PEoUGvuwTw0-u1WomZvIvvp1bd3Lmzr7rBmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHTC6r0r_t45K0ulgM3J4tmjReMz_avheoS1d6T2cfK_RiQwGofKHp0ciSKYH4Ts2YgxvNauNSosx4wf3havfprk1XU1wFzMYm1CgOqBbf-A3UYfFBgwnstojkVGcjRy2KMi0p5hWs0RfUo7b2-p0aFm7SK2n68yYu689cChHZHqGCyylh_-YNt1IV5PHWk3xK_vzYR78hy41aJsC3eCsJGLM1at7EolNQBE2VHH4ZQJWqkWcPtjKhmlhQC1NwDdh_p-ZaICApqxJ74UcQvHNu68VmtdnUU1ooDD_NqHnuoxaSPE3jaW-vMsSZWduSSP0aHcwwmn8WrFKFhUzzL0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=iRn6bOvjIpkakyKKq5xUjCxiqtFJ0_KNDRbVlfU-iu6iwYoEBKCh7PFZ_ezC5pakfrrw_YvYt4FpB03wz9GUaz3AmpOoLwzWWEG75-7Vb3bH92dK2sJEvU3r7VR70qX5zmLZWcqZShEb9cCoLvyNFDiOZ7_Y6-WuIbK1jRHlWXu0L7_nXr0aTtlMlWmyJm1N6f30kMhgdAdnk2BZV0tXfSJugULGdboXiQ5wILhBdKcw43YFtwzEFMEHdKm9gPvcmK-Pjd0_K9bF-03afgT7hoZFCEThvKa1VuYOyJLUcJW2jbXDi22I6N0qU6oF8j-huV1pdOyYjRTfDnenPsNMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=iRn6bOvjIpkakyKKq5xUjCxiqtFJ0_KNDRbVlfU-iu6iwYoEBKCh7PFZ_ezC5pakfrrw_YvYt4FpB03wz9GUaz3AmpOoLwzWWEG75-7Vb3bH92dK2sJEvU3r7VR70qX5zmLZWcqZShEb9cCoLvyNFDiOZ7_Y6-WuIbK1jRHlWXu0L7_nXr0aTtlMlWmyJm1N6f30kMhgdAdnk2BZV0tXfSJugULGdboXiQ5wILhBdKcw43YFtwzEFMEHdKm9gPvcmK-Pjd0_K9bF-03afgT7hoZFCEThvKa1VuYOyJLUcJW2jbXDi22I6N0qU6oF8j-huV1pdOyYjRTfDnenPsNMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JppLs3Kls4h72Y0UczQmWwJTcVR4OS9d-FtzwwX1wBvrulOqeRCY9aNSOUIuda5ZNOZvr2qjY1wvBbIm19PPunNq5u6AfI4mI6Q5SHEjlUfOfudUGkXTI-dgn7RcElcz73ErTqV2AbWPZv2nkNWXPROTXbpWWILljUnkIA7JNDhaZtXK18IRTDogWmi8Af0aSNlaG_5CL2nAALSExwFh6rLsMuRRalK_NAoJBZl3_2zUnE8_kNbCv2X9P_zBWM2J9cQ8fqOd9Bsk_p_mUJ2AjFFO3GlVAEPQi2DhHsKTMTxwdsI1GWAS1i3yTph171YdUCLiugHsqQW7fqSeBJbGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=hMeOxNWy4wRbyh3FlCi_5_e81G_rj_6byBWzNSgD_UDJs9-bbZryMjIRlCwqp1_vXdY_0PUMrIWnoKyVcSFBsRyfsaOwGKiB4Z3P6q4opDQINgR0gErhnZ1UsM7bUYbHZvI4Fdl4xgB3QAWDe1WJBl2jNYsZVQwREDSoe9B9io7chW3GiDcrqsYaHS_9ShYuWvwfffwsHtsboXlU4pMztoP0kjbJHh7zKmx3ULlexTCfNFOLVsm9GXL6Doy06_HTFV4Txndo0erDeerZwEVQvcsKHK4a1cYN1gBsuFfjXE8hi7jg0SnfRnRlKzvi3DLcQzK-P1hd4Ve_wpDIYXZiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=hMeOxNWy4wRbyh3FlCi_5_e81G_rj_6byBWzNSgD_UDJs9-bbZryMjIRlCwqp1_vXdY_0PUMrIWnoKyVcSFBsRyfsaOwGKiB4Z3P6q4opDQINgR0gErhnZ1UsM7bUYbHZvI4Fdl4xgB3QAWDe1WJBl2jNYsZVQwREDSoe9B9io7chW3GiDcrqsYaHS_9ShYuWvwfffwsHtsboXlU4pMztoP0kjbJHh7zKmx3ULlexTCfNFOLVsm9GXL6Doy06_HTFV4Txndo0erDeerZwEVQvcsKHK4a1cYN1gBsuFfjXE8hi7jg0SnfRnRlKzvi3DLcQzK-P1hd4Ve_wpDIYXZiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP6Ln3rZbpGrVTMeGvZMNDlmFUZyPEqUHYncq7c3squMhNf142_mL_ZKL8HqI-NyKm8wd6pnnvkQLrwiLsnwi9MDgk8s8pxxzISQKvxVs41M1FYM4YJ4fhmAxdTAKQBEx4AbZHC2IhcN_j6OT7_qihX2Dnlp-ilRLfnLYJe8r1YlXHdFaoZJQ5Q8nC8f1DiH8e_ddMgq0NpZWGgj0To7gYng-2XpDQECO5PyGt6w12iN-zkGf7shiZuYUl0afsVOuiEifMYNoE3DCx2H2M_85IWaW_OvPHOypSW3BUC9mFXE5XC69edrl3hpQU4aiSJ-4YHRPwL834Slp0vSpL3Niw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALeETKU2NtclIYJO73OJdYWqTqzc8wtgVRCyWEa9NrXGkoXl1gumqG7foDefnSPKt_ych92T2DTsvqmDKVdYP69fhJSayM_N0hBkbX7Pkco49yuvYG0rnbPCjTGeMMHo4cWYa9JzO0tw3cXCbbFKh20iwE7Belp8xnhUFp6m4ndhRRDTfSyIDdFkje8GXH3sq26gKrCCt_uYQfnM7VM1M3z1Pu39dKfLwH4LWLPj0uxzfUtVnvQBv0N4fiS4kxJzOKPS9vXoNuVpCXkWD-bS63UGoDTtYDWF4zzwq8tVGkbLsOtZ0iAjuCemriQnxHHkglLpfs9idEd0jMRbpelsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIoe5qxMCWlaYKJfBGTWZQbwXKNRP2Z29ul_iVO6GQe3BB-63hMjkDiG0R37iuoyhzCYcBTmHf7LnoBWnH_gzmTO1emZApKOdJp-6YfKLBFEkI7XLYL4hZDvGghMFLcWZeIA-aqlUAiu1HzrRQ0cDPji337S-stBo1VRv92TIy8aDd8ykIhuCGefQ162tFN30lE3qgiJGwH0hhZWBJHsdQ-Hoqkq7ZPfRNcE1v4Ag__KKUf7vWTBc4-weRMzlwsfgsFlKCwEtjlzKTgoHDq_72BtIkv7Np7GlPGA-m_W0EYyxn3yYuf534wEuSYTOcLoxS2UTWHkFjXpeeBisXPeMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcapJBWcJYhMHc8Sr9Y-XkRVhLHbQbcFlu9vMGR33q8SE4wZqDSt9XVjAUkGS9ZL1yFuYvdq9cgMqJvFUu8MNk3HOcU7TQavkxmROcfeNUzs2Fbdxfb8IE9T_YeuVpLAkIBAYPf-0tIkLjHnT3qO1goiX6u5kKHlQYhG3EoScYy6tGbNTKpMcDPlH6GW6FOjDRTtUkh64YIUAeKStPPIel6xwhGWN1j7ALDrxsvzcauQwPoI1OaiJge6QzCe5nlFKFnwE1LwDN5xQ8npTmHrnonUxTdlh9P8sN0oErBRueRPhA6qnzVhkkZL-wRszpyq5TtEsyA80iKzvS_pSUDZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=VxW5uqIfkgc0cdv355O6y_s6cWN3PlmL755sOl8LDSaYPCyXAhyph4YcCBIQefPDM6QKUw891MSQO4rdDc8nqs7I5bQF9pt8i-zDjb-LbG2SOkpJXhy1S_cEEjRAbxsoKjrYzCvNvTf5Wfg8YW3WHWHWcs8uNdlc1_I4bJUb7865Vt79JC_pUg7_RX1B4Lg0zV0hBPoVNWVVsa_dOFigZMkUdbB92MZg0KTF1vrZx8OX0iuDqSHwL1d-6zgWq88vRN9N9N_035y1M4VOn4cpcaBCQKQb9oBvyHP5Sy6VumZykrpLmYA-l3mkj--JkDPwtM0mrtPmZZFO3rwmjMwLtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=VxW5uqIfkgc0cdv355O6y_s6cWN3PlmL755sOl8LDSaYPCyXAhyph4YcCBIQefPDM6QKUw891MSQO4rdDc8nqs7I5bQF9pt8i-zDjb-LbG2SOkpJXhy1S_cEEjRAbxsoKjrYzCvNvTf5Wfg8YW3WHWHWcs8uNdlc1_I4bJUb7865Vt79JC_pUg7_RX1B4Lg0zV0hBPoVNWVVsa_dOFigZMkUdbB92MZg0KTF1vrZx8OX0iuDqSHwL1d-6zgWq88vRN9N9N_035y1M4VOn4cpcaBCQKQb9oBvyHP5Sy6VumZykrpLmYA-l3mkj--JkDPwtM0mrtPmZZFO3rwmjMwLtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=oo_qT22BHh-txfNRNweZw60K_ptzdqReH7zvRmAY3IFnLAbEgzIQoAJQsBCQZz2Jqwfp8bBbIF0YKtJfsYDoA8qnurvTUyk2tL5EWIRiTaDRd8nhzr0Aazotq5UHYBQMPMuWMfvv7cjLvjPNtmtSeLis-q709h6lgNcl4KAv_34ehkHs3DftOpiCObgAtdtNQQvjOfiTVkSRcAB0E0pd7oTWFPsaoR8vCoPHEhOEal5TAwo9bfAROjjsDRQQKZYpFfGMs_MYagx7dL5PJoZoiiDVOIWTZlkRxAUbVzd5PNTMIFiI-RhOd2DMgrfJTWukrNVqO4agLYexEjz4DSCDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=oo_qT22BHh-txfNRNweZw60K_ptzdqReH7zvRmAY3IFnLAbEgzIQoAJQsBCQZz2Jqwfp8bBbIF0YKtJfsYDoA8qnurvTUyk2tL5EWIRiTaDRd8nhzr0Aazotq5UHYBQMPMuWMfvv7cjLvjPNtmtSeLis-q709h6lgNcl4KAv_34ehkHs3DftOpiCObgAtdtNQQvjOfiTVkSRcAB0E0pd7oTWFPsaoR8vCoPHEhOEal5TAwo9bfAROjjsDRQQKZYpFfGMs_MYagx7dL5PJoZoiiDVOIWTZlkRxAUbVzd5PNTMIFiI-RhOd2DMgrfJTWukrNVqO4agLYexEjz4DSCDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23562" target="_blank">📅 07:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbVkRpwD8NiA-et9XbkM5idjfrkp_9SdI_exPAXdWQXgQfL7ObrHuvEbbJAAIcG8Kh307tS65up29yHK_8dQKDnNBJPBGaU7LRaqT8LBoDLQHJf4kGu2Fo8J-Vq2fhR-7b3MCRLAP-ccm5YhPPQOzRc59ReSPduSWLfHg8u4H3nbxLxZRUlBCBBF6pXrliFS_a7K5kWym72fgANoJ40qaRmBvb6h2yQw4iPtbAd0UBN9QaUtm8pJgV3YFbOgErKFeQUh4DJev0W7dL2hf3MH340idiwSQVuNVJqHkpKFi9rME3tWyGCwITSJGUyCY0hlMKfaGe1tdRdVCjdvptbuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23561" target="_blank">📅 07:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HklnI7K1biex-H6Mz7x68xDpFmNLAeSiObf3YkvQ-shtEHmmPY68OiLAOe1OBcDU9wcAVdGuKR5oVRUAceDD1H_IWGzG9Rg-MxOmscxSAE9Qpiz_tC1_GU3Kmf4ALu5nrgrY3gTBbboRVcUZ-JRXu9lDlzp9P1j0rPeAWYGfH-IXYcY344QEIZ1GV5xZOf42IXaLl1QYrKeoT902OsR4kSypkQHKT-5sJge67Cuy0_prnKyfQv1hVtDl5tcEFPMpvfOXN7njTj1bf0S0HFZbyV6kurY9hT1_mHzL8v7zzK4-8FcfPZjbp7v5jnPY8D7SGgoRGIiczGJMeEay9nLroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احتمالا فرداعصر ازتیم‌جدیدکسری‌طاهری ستاره 19 ساله فصل گذشته پیکان رونمایی خواهیم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/23560" target="_blank">📅 01:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHn6OJP0JRDJNYx81jHQGUYxPyZhi_HsDGjdyZXcIeoQpIJGNwhfhm7K7wr4JZYwhEP2uxTsnBzYFcKWxNR9W5trZiSQjB4Mjqc1t4THBRDRsPfDbb1p_Hy1LqpN5mEwXRmxZzPh81lKo-WEowEJ6fBdeTGoH_SWS1qb5N6xrInBlYL31jChvnfHJzl-8SPTDdiUqW_D_CFkFBkZTuFDv8ujZIL2k0_4kgb2JHur7aFoRW2xxinjoKwx5h0TfLC2DecNlF5ZFG9Fi5hIXoluU861k-yktJ-4ggiYFFT4KC0Insh4ohh_ZugGyQb_zTsnTyPhFDRVH83YZZUH6gxAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syOplcinBd2eLQZ3EzXD-0lrQuzFz8slzyCt4gDybKPOqvJT_5xZila_1-fUzkcmb0oNTwQmZ3iKWk1mA0ouTmzytHctoFI_ynUOxu24AnmwM5yfFfwzZY3IYK6zmS3YzBhKBPoiU9_Tfiz2y2WRNY2HQQEub9QrgrSdiUmniqVEyJ3ZEnEYaip0zyuP057hGZUQgIs4RLK6RO5s2CkibbECFIGK-_9XM1k7g_9GofGTChLbjJnsaVxjdMWjFQAzR92-xcpHW-Yinp2teE20oc6GbWjVgCdHqe_fFuRiZ5mALdDNz72qUX48nevzyM2EBDX_Hhj_0ebxh13wm1OacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoidANhWSPrqf0ClVFj5wUT3XXZQPo7l79dtCS_IKNqk_CBb8ZmGkWEmAAmjbt4LUGely0CxV-lYkxWrtlMlCyGmP4uQi3r_NNeZgTmhcAZ-S_X1Q47LzxKXEyVzn_HmGO52BrduEO8w_5OSrfg38en81NO3buFRV435m6IWwszrAzjHY_Ud1caobqHeD3eQJAmjsbQKFqOEzKBl-3ZmJLOK38oceuBIxf6xwinBCINOaS4ws6cpr8Me9AcWJ-bZI_Pxayh-MzK57pofZ0GjIG5C6afJ6FhQ8yC6OLT23Vc8QTJmJW-6t6Db_FnwcDLNOJeixpWJR3T_j_LiAfie1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=haKq2H_78bLFVPGNtB7eB-Yzrw60I-hIv77RTNX24Lh-8oj4HxOei1AI_CHtSAus8jC-dYM_i9rDoUR1jp-VjtmJ3yb3Ulmya7M-6CVg0BFLKhJp3_uG8jhAeCcMYgwiNUs46ZAzlCG7cQbLnqHVQLfhwByByhjJ_k8fyKk6UqXsyurr4p0jZ_tu0DcBwXpzNVpj26R1eSpyubrY5BZAdejDW9twy8vfSDszH9Q5L5hQh9Vhj8mj7Phos0ZhfKUN99kARoxFy8z50annLtqUefCj_YCfBQjxLGGA0iAC1iTV_aANupPIPnYC6fay14u40Zsm4SwNKhIvOmd9YBVaMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=haKq2H_78bLFVPGNtB7eB-Yzrw60I-hIv77RTNX24Lh-8oj4HxOei1AI_CHtSAus8jC-dYM_i9rDoUR1jp-VjtmJ3yb3Ulmya7M-6CVg0BFLKhJp3_uG8jhAeCcMYgwiNUs46ZAzlCG7cQbLnqHVQLfhwByByhjJ_k8fyKk6UqXsyurr4p0jZ_tu0DcBwXpzNVpj26R1eSpyubrY5BZAdejDW9twy8vfSDszH9Q5L5hQh9Vhj8mj7Phos0ZhfKUN99kARoxFy8z50annLtqUefCj_YCfBQjxLGGA0iAC1iTV_aANupPIPnYC6fay14u40Zsm4SwNKhIvOmd9YBVaMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=DoT9CUHXJCH4R36EGIjBPLiQ39ene2x_KUjDrxnyZC4eRJ15b7-_fX8RxhYbMrG3aLx00qQ1KkX7xFzrWVcWPq8qbjFt9eZVPLZ9SitMPePgP3MAF9SG0yNc7PBlDWQSbbJvjr7qWITOpYx38HUnMNln6iP4G3_sHbnxyCsroYWgqAHbx2XXBBrNdUToHa-lw18hdnj_yM5lyVpMaWhAQiD-k5YBrQj3TOy_KMKSihu5MbHI0FZ5o5fIKmmafHwBqZ3UmJIuqwqAhXrjt0n-lfsbzYzKEvqnU_81rxPUQHCogmYE07w_4I7MzPSbm-eLCngKjdTrz0VkTUwI1PBYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=DoT9CUHXJCH4R36EGIjBPLiQ39ene2x_KUjDrxnyZC4eRJ15b7-_fX8RxhYbMrG3aLx00qQ1KkX7xFzrWVcWPq8qbjFt9eZVPLZ9SitMPePgP3MAF9SG0yNc7PBlDWQSbbJvjr7qWITOpYx38HUnMNln6iP4G3_sHbnxyCsroYWgqAHbx2XXBBrNdUToHa-lw18hdnj_yM5lyVpMaWhAQiD-k5YBrQj3TOy_KMKSihu5MbHI0FZ5o5fIKmmafHwBqZ3UmJIuqwqAhXrjt0n-lfsbzYzKEvqnU_81rxPUQHCogmYE07w_4I7MzPSbm-eLCngKjdTrz0VkTUwI1PBYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyOleoT8kszz_dpgUf-RSaHzYp32dTEopiHtjceoJldLNf9OO_-7elvlMPXR0qUu2e1rtMOyojWktflvi7LhtMmHxbAuDe62Uw2qYFzcqmKbOwgucsAvHOfMvImP--mpqXJUP3XpqERxOufbyC7SR3mmiWwgENQQHF7vXYiO06bKzuwYfEcmcR3YPLLaKfO2x5RXliguIBRl-w8WcIcCZNQd9WhuMsZBK9-iD_hrWM-Wq8oC2a6KUl0ufF829SSEZtTCcnI2xptGbXxw5vxwLVqkc2rbgOtyHZ93MPPSNy6ednKDn7B2De8_-Dhtq_RoxDvRQkmRGXzpoB90xN0dKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_BDLTzeZUcpDwkLKk8e3PhgTUsW9UIYrV4jTLKEOuuMhLu-AZkA-mSlv_niYXMcbfkp5eU9Fq_roEo5IvdySOMCZ2rFjCFFCUL63ztE6umnzESY4vd4oJ4dlqDEe-4LcoEaT_1iFOKcMMtYyLTpvwLeuRefGX_qVNYfiynV1QtX9fF5-UNVL7zzmcR4VGo3SZdfg4gOTTJ6s0-jtFjMlGzrKvHn94OzQSnUpgZ9nuo91gcYrErBCrxQY-tBFbYxCccLbLQKWJYn4dyk5jGMDok7q3lm6B0PA4vSwBdsr5QIhQDxefXBdIQbHqmxyom3ko_oMiCk7ZEc2fB80Nbu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIa0cKEVVrGUo4X4ZgDeVFZChZ8nzyxRi4ozrlQEUDVZxpKzHXJHZOnrZnzyvcfxiLLJB1keOvQX0Izf8-tyfpymyZvTj__jabql7YLxEtkgMi0engLz3ealXk4lnBiw-TDeTBC1tu9orJEw81cGsQK9nJyYaSCQGif1j3YEXTSLSW093pkV4i_WzPGOjekhnPPKp7yQESEljJsfwLkh4EAV_tyPscq0On4IAk3DS29xnk0Nhd3fkLw9z4vifffeOMt3o-7Y9P05fl5fEEnepzfWUkZYtkuAtts5odwFhMyXO2A53VcpqHC76jTdXp8UKU823McRJ8HcZBgPouTAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ3EDppzU8Q2nspyh6Q3pjsg-VnbHZcYgOYoL2uhL_TdXtyxvhujPA_yE19N1A5x5YfvCthrMQE1bS4v8UcljkcbB_rYAA8_x2Dqv1LuOTLiEdoxnCt4qXs9IIER93sMxjSaOBNUslh57L7bFgUQ6_WrZaimo2j9tL-rKXsx6jnMrGVlqeXrRarri3I85kEG4eCbnenk8oY_u9Y4MmRu8MgBCZqx7vcnGKr1-d18YKHHLQm4S356J5-N_JEK2c5Jx9wkjnCivLiEkduNzKpovX3bcZUlso6b6sR3J83EF8Po5AWbS0ZSUS3_le4yRCc5qAZn-dEYSTbr0ZszD2-ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsA77mbtmTAPqg38nHB-yq56CeuvqIDnl3TwgSW8aEgppm2p7kK7I15HDsLkmPgz3u2ot467I_wnkVQLFtyVW02FHUzjIaor2tMHHXGWpKTBUJj-nEAcpSkkfCEx_aEfcO9kTAramz_11Zf-5PJyVAhRRpCfoYEbmXVpUU6M7Lz8IRew7gyWPn37eXXua7a8MeKAbiW6thMdWG471Rdko6Jsp4sG9JFfO_HNM9-jky_yCUKf6GBgjpHGenDcI_7HGxgRLFl6suiwxOG0iGM1DXqVxQ2TJGGVxmyphiB9-xu5IFa6J7XZlu6pv5mN1_LQRMv6jMzlik2BfnX9PNYSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=fCUfjq7PNJbfCn_BqRIynz8j8xBhwo_dhnBj5F6_VRxZ5LFcp8Kv85YzU4Ksl6eD7Kg6dDUr9LqbEpKDl5yev5cPrLMEJjXOTvh51kBA1HosxXtRA2bKV7foDocQM_Ckds9eLXAEgW-4Pt5HvW5IYOy01MFFGt0Y1FZxmTaJHFurpdMDCNrlG9bA0Z0MGc4Lr74HCG4KSGr4BZsxpyfAPav0Zv8sJmIHmupak8USDL7N-_7bJOUZRFx2pVzLr8-MllBdrIG7xslod71R1LpG9yy8iamPW2GW7J8Bz1JHsrnDxhByRdZWVG6RiPeNjHkyvrc-DiA2mequEMtK08I7fKXuuF_lozzwaAaStpeFmwom4kbKardcC7EcDcpckVp4ICAmKDRIpgK2n_mXgcesy2jIxwFQ-pqx5N3phqFelu24IJza-dVBr6S9QdZek4b6zelhAmu79Pb8jmMUq0TlrRDMGukHh--XaEXZY2qa7QSQtu0e48RNKds_TVGUFrNiJbQRsGpEawtVxW9Miwa8jYqxQKIeZVt3c22gCXZZ_yeksUKqEBinyvLQZ_PIct5qCNjL4CspTkEKD3G1Btw26adtVRtie_eMLELwrnFXvh1vPI1WpUj54aWr97B6R8HM8OJKk8ETHuZRSlpmMPBD8NvS8hDur9DmPT-VUsUf6fM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=fCUfjq7PNJbfCn_BqRIynz8j8xBhwo_dhnBj5F6_VRxZ5LFcp8Kv85YzU4Ksl6eD7Kg6dDUr9LqbEpKDl5yev5cPrLMEJjXOTvh51kBA1HosxXtRA2bKV7foDocQM_Ckds9eLXAEgW-4Pt5HvW5IYOy01MFFGt0Y1FZxmTaJHFurpdMDCNrlG9bA0Z0MGc4Lr74HCG4KSGr4BZsxpyfAPav0Zv8sJmIHmupak8USDL7N-_7bJOUZRFx2pVzLr8-MllBdrIG7xslod71R1LpG9yy8iamPW2GW7J8Bz1JHsrnDxhByRdZWVG6RiPeNjHkyvrc-DiA2mequEMtK08I7fKXuuF_lozzwaAaStpeFmwom4kbKardcC7EcDcpckVp4ICAmKDRIpgK2n_mXgcesy2jIxwFQ-pqx5N3phqFelu24IJza-dVBr6S9QdZek4b6zelhAmu79Pb8jmMUq0TlrRDMGukHh--XaEXZY2qa7QSQtu0e48RNKds_TVGUFrNiJbQRsGpEawtVxW9Miwa8jYqxQKIeZVt3c22gCXZZ_yeksUKqEBinyvLQZ_PIct5qCNjL4CspTkEKD3G1Btw26adtVRtie_eMLELwrnFXvh1vPI1WpUj54aWr97B6R8HM8OJKk8ETHuZRSlpmMPBD8NvS8hDur9DmPT-VUsUf6fM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=XlU4iBZF_F7yNSTqusrxZcnxJQfQciGQnFfl-R-MJ2OYFjZJhHLEOLlatcrA4VkDcrAkPClFpdyjZEU6bJGVT0kt9m-YYXXk3f7lmD5y_ffKfqR-_8OCRgim39h7J-C8_jXaKZOlh90FcLxb_zjdyKqVEbv77L-JFW2YXg-dN5NFA1GigfsPgtj7Jra0Vwxm2qcSd6OnRpS0Y4-VmUShFBaq_ZTIPvaLekC1dTcz5iXVQoJ3SnUnig0XEFWUYMVy_oBcDGzrrzpk3MIl66xec378dDmxtAcj8AK3DiPBjoemB54fYqQRqcfiCXyZ47HwTdT76KwVoGXGNlK0V2602A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=XlU4iBZF_F7yNSTqusrxZcnxJQfQciGQnFfl-R-MJ2OYFjZJhHLEOLlatcrA4VkDcrAkPClFpdyjZEU6bJGVT0kt9m-YYXXk3f7lmD5y_ffKfqR-_8OCRgim39h7J-C8_jXaKZOlh90FcLxb_zjdyKqVEbv77L-JFW2YXg-dN5NFA1GigfsPgtj7Jra0Vwxm2qcSd6OnRpS0Y4-VmUShFBaq_ZTIPvaLekC1dTcz5iXVQoJ3SnUnig0XEFWUYMVy_oBcDGzrrzpk3MIl66xec378dDmxtAcj8AK3DiPBjoemB54fYqQRqcfiCXyZ47HwTdT76KwVoGXGNlK0V2602A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQfqXnVZlhwiyFwAKv712JctOg2Cd0o4VTBd43DFR01xKYE01nSaxJv13aH-_nht6nX8yhM0Oc2QP9B1DmZfOqfJgDXLbTfG8r3BK4SWQajQnBBaZY9UgKZ6gbKmMpl2RtpKYPJ_OQrXjQ86ftGbN9Htv0VQRbTtbYy1oY2IXHOGm7-fgiGeapnSx-U8y4QEG-w83i8KpN_dp4FBwrXDODSeGQZm76CjcqFC0AvKkGSt-qp-_K42VXrWWecbsbko01ggCR8qBBh7m5nMczOXXXhv41O5KfGXxFLc9K-EKFjMtjbkvVEfGH5LFONCy_flv2Q_jF33pLt8jA3b1Tt9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwQteuZ5dlHaDcGTeRfX8QqcAPKno77GzvqC8dfZ7SzsMmDn2sGy3VdDJSth-DCK-MFnMBN7vJZgZu9NfSPi51K5DOsbev4hfDecNWHFASJdkezIp_DuEPdqiyjpst12MxGMvL-iiz9uCy475bfzUhjcbVmlpFc4sm7G0xM0aYBTWorhqeJIOWRkUvlpGtttHHfJGdM1McW4LLRkNqeXUs475_-6AkZraUmSsVa5JPT1vmvzNrN_ymHI6E6cEu-3zyxq9ceOJmcBJ3jTH6RwjpsLJGp5h21Yx4ucekNCeXTT1zFkZ0AiuDyICURiDYzwh9X_rWtE_uFxYPkCGHq75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FARD6TarAlDgn24aNemH624euuPojkExw5iXonEJHh8_tobL_TLUddlbRm-I6Spx16t5lG8hbZ8-xSJPUsqPu7sWIwtG6bJrY1jKDCkWABxOBb-h05mstqbJJZtFuyLQcoH0jO87UyUfmpmFTZVLpjaPgiIPoTnEymK60Hw-fYvMXn4MDEuhFTVoTBe_g44ZhpxtVEqt6ZHA_k5KdfA2Eo4AkBtf6i7rkeFxPIHvSzqfyI5-fUTUmAjhMN1WN3ijqSMLBvn0IipHa-5bzOXfiyPDKCD_s9l74lbnggL0cljWgWKK83AjQVzqnbVoqCZt1c51odTwsRxGukHjr0kAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiEE16Hvx2vc0tC7fn4mcQf8Nm9xzCQzNYQZnKgn9L0OY5E1_jxuQ40pjseE94uI0yYwocanEhRRTm-QNNBh1tJIT-hz_DWwQO3_tAgWtjV2kdrc9IUBNzaP5ATOLnLJa0OEiDMXdGIm8pwhoFmx7Td7vCGIUd6ETwbHotTuZ484XkxkNJYzgstrFb4lFL_5AUZNmc-RoLH243TpLLjrRbWRNR4cAiiyPga_x8x1GwkmJ9gijkqTbovdBe9gcUXWkYBTU_O5Hy-P9bGG1J7A86p_2IOPUd_Uu9P2dQz7AnqFJ0Yy0rpt6xvpp80p6kXM8GzGDig0ZMNWH5qqPC6V7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZbXrPmEOSFcdOBnq_WaS6tQ8OeembIOBLeH08DzXKizCCD9t4WA_DtpLseL7HDmdwoPK-sRdUX5L8a8bk4bQmaRgxcK_GPnXBTieKB1l16f0_eTLJQBEzfjtFULGjebMRNSkwsjWzVms6jqzSMuECwfB1OArNUvn9R2zRqP0j4ofHtEembjCXJpAL7bFR7chYPv9olP6dbZ8CEA6vz19Ec2so9aCgFkfyV9JAqhiZD_KmtNex4IoCX4o8BxMlZTSjx5Zcx5aE3D19lPqFqlKvWcdfH7V8JBtZ7sHg0nEtAJ7r0w3Eo_w7WcT2B9EfZNQJI5RNWSV4tcbUBK4TVBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb3pZDLqsF4X_dXyJ6IRFU4OjsMW7yfYE3kwKB9ieDvaIq6MgI2jLe49JbFRKS3a703bAM7j0LdB-FxAabVxpmfVKEF4mTHf1T4rRLB122TpVmL8h249bLvEJ0LYUAawvAPU110UuUGUgCmuRMu-J3bfP2aIDfPFwBJE5ZOCZIB0VwrC5d4HyuUqu7ccPPKfs4Ran66lQrmgRf98lmeHI86Un18kLCWKNWfXWg3T5EgUsCghc6N4MfGbmfZX0UIP3l1YR3kC6wm77TnN6A-mubCwU_VoeKbNA9fLUEbXv7eYTl66mWw1DSGQ9uNhepuNHdHzeC0my-PaZpThlBWlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJvk2WH6hk_f8EDE0f55Zsy0mllbW_o-63UFK3PTHb9SLszUL9v0dTmt_Tr3eNUgCB-MITM1dYTfcbuLgkt3q5iZJOCssL1OJIs8fqI9TSRGmwjOtnsHmCxtZH_DS0by_XTpoVX12x-VeLOng0rDlwU_NPv5-gOeOXe7dMjUPl1_EA-FP5K-b5E8r4Fn_o5ualaUj-9Ps_tqCBH-IdPbrcZscrzFIpyv7JmhQvO-Plic21YyhncD6m-BzTtdvqCpN8uqZlbeziRY-U5UJyWlkruFGl6gCo8-cwTLrooJmGw2nX6WlFqASpEiN2h6wA7tIFUepg04awqJEvcNXOUCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9O1fShLY8VN0WF2hDGbqXY2iJVUyUYODBKgcp-hiZ4CovVtVWoq0Ul-quLCgwflkkoPHuxN8fm4E_eWTb5lW6ieaCue2O_nB-z6zugCcjJ6pQ2U89uHrsKe3fM9vMhph84_Kr3IQvtIhvLr4hj6EX8iJB7cfSssYga2CESmAb34uTBHpZK7i0l47BSXqfMRPGBjPMHNEkFXPQUlFxXewlmH9QwbjPEZHJ4P9-Z8ZeE0EbCQYWN5cKHRGUa4_xUUadkDsDlk9YqyoVBwqLmqZltxFZtJZ8T6wrJ69Y7vKw1OkGgZ8zuwdePWVoxII19HBHUyhVwG1RO1iGkuYAsQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCjey4FwlUEB7jwCjndM79lCuemq-lp73uj8jA4nuY_xO9UQtpoxQh_lKWJdz14X_Bwg5NwI2t3pXmAyUX5dYax-lvqN-cXR-xKhY1axF1zvqL0qQTI1xJRmzry4EF1euRUBn4gcGuWwlTqXyHlbNPJK0LaG9c8KLEX_rXwrJdONhwoBmYqW4z4eEdQzs8bqCF-CBM0XJ3RoQMUu1ACiRVw_ewnL5_sFCSCzEGm_JelPbqzMImwVK9VmXzxtazjLBb0GoB0VDJfuYG-knDV7Ucbrwm7268rLNyHtEhodKDb-dfjU2IiEqT0o_0bxt6GQlWSwMeAFRwMoJr2OXulj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjMh8LR2QQSnX3vDKmtpG2ssrZjAripaUdIi9aUniYTLi4TOOMWoI2ApMJVPYE_Yd5eoK40nlgb3NvD70cXTh2OZGp2RbojjvNZ7wiIQyQAYU_5dYv98uEuBoHCDoEd26JhlRrV3cM0EZfMfmQoJG4GzMcfN3TTnGQv2zf6QvDZN7UqGHm7IkdI6T2TRM7aEVL6jxZlVlFkPaL4Al037wkKFM-EmRGrRhbqniTggTavooL_dGzay8VGnldAZGVYJjGM4kLkNCVSpbGeoRLpgONV1QKa-UBpbImufjLijUgBo-U-JW6ksk82ayHHT-_eX44GwI5ZEXZ5eZU8mRiSRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=LgjTyXp1T20NoXm2APfXUE7EutQCpMwPn8BMu1dFl-MeNnqWM04jtGXm1fQKcIuuw7w2qyl7Zep9uho8OQ6O2jE-zlpj3FpOj8TkCVp-Mle2r1psWlWzX6KT07BHH5yAfygp7Gv26tp9PuDzS5FS1_Z2v6SJjPH-6f2DclWLWCuiLVsqRnKJyTrEqkv9C2IyeZNawKHqxQK-rSxLGPjdSvJgmPpEOqKUgcWLje0th4w1z_TGYTfYOdBHJ0L4yeQ8wiNfcW06YHggBziojIFmJiamgN6gPqLkBAODXU4bnWw1BUhI41PRXTSyhwbuRErjPMSTqNtV2AACqKrOXneiKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=LgjTyXp1T20NoXm2APfXUE7EutQCpMwPn8BMu1dFl-MeNnqWM04jtGXm1fQKcIuuw7w2qyl7Zep9uho8OQ6O2jE-zlpj3FpOj8TkCVp-Mle2r1psWlWzX6KT07BHH5yAfygp7Gv26tp9PuDzS5FS1_Z2v6SJjPH-6f2DclWLWCuiLVsqRnKJyTrEqkv9C2IyeZNawKHqxQK-rSxLGPjdSvJgmPpEOqKUgcWLje0th4w1z_TGYTfYOdBHJ0L4yeQ8wiNfcW06YHggBziojIFmJiamgN6gPqLkBAODXU4bnWw1BUhI41PRXTSyhwbuRErjPMSTqNtV2AACqKrOXneiKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
