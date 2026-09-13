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
<img src="https://cdn1.telesco.pe/file/XbDwSblYMuQQsjKKg31NrzBsbg3eWU498qYi9u7ZkJu-_BHMYoz4LvfwSEi2OtE2fVh3QDAiIh3FFlhfwlc2PVy5Y6TYzNNmXmtL2yWNxHpe1e0NmoN1b6412VcUiJbW4N0CYDDLR-GkfR6RJ1EQX0sCxuhxcDsvqyhtuDIqcvEDLY6q8iH4bScDZrG9qIF8tc31O9FNIOHWtxg_zdSaf15ItXJe6056hTwt8TJqK9IyN7VpNnghKNekmDSJFKJ18wnaeAPLNxpnBL-f3skwSpbwawEcWP9v-c_kglARMQDoJeWkSVZWg1MCS3vtBhXNfG-nTl9lR5MSG2hdG9j1Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S8G5iIfMdYThEZLlm5VXheBGKTpbkjmWqqgOq4H1RPW2G9jq7_ejyFJSRS9AxDzHxHB9JMnAPV_27--CoE9mC-S_Pwbf2aaTpCnsj5FAFjvrs6JXvwv5kNVJbA2XCrg0JwfL9utGbLBd1OfT1F8g4Embay4eBjRP92yedkhq7dydpNEV82D3pplFAQ-d82sgxqC896x_hJboQhYOGRy6m9zi1lI6xyjGouqYYXYtShP_bmfjEX_DIttt_mfUhOhEwIV6Z7LAl4pKNo-lj6gjKGtcmHpB7JWVY5rnybz8bYKOkbpZAnaHV3fQ5gWAIXrhLWpaIvNLgzA0v5j2-kdIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rY8DR9fAZebremYHqubkgN0QhXoA3gGqquIrTNqFYGjvXgkSzi5_R5HYGfPpiYo-oR5kPgad1rslbY9qsCLHAXX8BxX8TNiJ_6dlgQ5ZY13LGslCvYrCM0mQQMXEkcGOdhJREDBUH8LH0KTAt9VnL0Y6AqLuf1o3d04pA3mtCyy7YtGRXPDHBtVwpW4E-uC6aE9UH8qGZk6GKg03S2FyeXQ7vAvqstmS4rahobMZbSDUD_JI-k_P7CgQyXVnP6pV9-Oh2d9SkZUXXJgpUkdYIdOueJcmZbNdanR__kCdQW4YALcuXfWDx903MnSV0qwcnRb1WWVlWDDD8B7C5yttmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3xTi_g2JulnvIzFahKMRXcWTUhqRz2H0qaa3W8gthqxrVkCGvqCmh3MQECIKipR6gca7MtOX7xLAqtGzWvHGjWAqb7O2SVJwrVICioJpX0qaEFsEhvRrU8uYLQzEFQGcRNdK_PCPQIpFib2RWIgO6-0y7bTZkt33g2lhbcHXdDDq-V4jVOraFwZDmlzsxb6B5fTdCLOHAVrBm4lQ0YnYK3P4G5aGzXU9Djf2P7PvaOE8z3aRXSJkmPEfmBBZjf7ao5maVXOQtc6mlzmyw3GVHqPAQqGn8Y_18QZfIFTtNCfxJz_Es0ngAyw9rxNUgW1m_xXGMjzcy1r_aA7BDNVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKVvnWZAq_3RjhXE1GqLFZZXvIq2xZy5FGt2Cf8fR-8xHXb7jIpPxhLFMSp7Xf4BjTzLczNkZqdpFm_AqlPZM_0ZzqJW87ZVxGR2G5fdDqaFL7XaTx6ZnjNVRhptQn98THOzezNkfpQJp_VgHkDA9pBRLILvLmy-D62v545_OYnrkMe02OEjKj4ppwUjW_fnP8dud7ettjXTjzsnxSaf3uDjwRza3MgGu_90lWqM_T-pbSqrXJbIyiTivlQ5qPcBieURkgvyPb5IYb-aVeSAEcPVoAJmGxxwr4vzze32jsKlQergemYdbc4_8_J5rSZQmoSBh47PS-qmuhPH23ihEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OA9yBev-DNel6slUHSmFg3e4tJjCW-qaLWk8Wx4NbXr80pbjIiHor9LASTDDCDDAGFTsFVxWRhQ5jklismtCZULslM5XlgRXP1LJWOba2gm20RlvyNuaiGqao_COJS9pyGlS3G4FknzMGU0Ryuevd9nyB-gBkO1-9cucLWs1DJHEdAFGz0XBbGiIX-HN7MOeQU5_hOX-QwDWlzY0Xybst2Segsj5shFduerz1xgEEX9Oyrd8MRngxKxObL9KC5RLNN-v-fOa1vfOM8ODsT7wI0AuNLxR5ntXCz44mVmPtjmLqkjviavSenwlLR4IUzNKg-7B6bKownsPPkr3gBo3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOTzTJphpDpp1csdtTm5QmY3FW9sjdQhxDnUne8zkl0xPI8e1NtaOf_VA5MWIeD_YCx3BpJqKV24SMPC9z9NxICyhwTp94z3XOkdxg-Ql8Z_D0RPIeq6uVnx5HZNZCcTb9LaA2VRExt1TjxOJqnAMd7A96gfRftUh5_WwS5HGM1RyasFkP7ALhChnO9UgwjoFBuv8S6OBv4aBNGTyAeIB84CbrDak0WBPcXAU_-UkiqSLac-uUnep7a8Yoxoq8q3kUOvrn3Z9JQ_Y1_n4UoOOFw3Wk33WuaCPvHSSLREDOUIuwcrDa1CTHqfEoqaBZkfcGoKOsT9tigIXn_Bj05dUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVI8MG5oOlw3zuTTkNuMpdM0mEuHdUZCBF428M4QXXkJdixuQahg8ZYYt-UgFMkxHwwLpZLY_kvT_Hr_prK4GgmCSs6zbMA3HpBR8mBnY_5Rl1PAlF9ol6IHER_-lE8DZTnJzEB3CgOZ9llMkhhZJ1DgWM-cJNbLk04KCc_DyuzXWk545Jfl0SPajs34-eRgiYE0xD3uBq9-TI1WbckzDdDmWSKfxsZg11zO4JM8JEkqF6MWqmDVGPpiB9Ky0OBh3LyLI9HDVLHIZeUEXn3_B0BbRjZUqI7O5z-EZQKThxSedF27Hu6HtqbN3G-QH-E-z7-sljBjeUBT2SZFpCKF0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvQIeBfJGo6iZRVE9OupL4sMb_MaIAGC7Id--cO748CaIZHFn3Hp7Q1GakzVXwZKQBtA7Q2Pyk_XeO2aUVM2SwS0wgZYB6hKH5nq8ACKEM42I0yRZSkbOuiYiT_PMUGnkPOH0I-QIf7aJqK0aAY5ukJZ80bE5YVerNL8AiJG6VO8NBlc7axPoXGKgBfkjzyusipNeV0asWygy5FgzvRrhiWvew_h_K2yRgfTy6LiStksfq0Frt5txKvleLK-6mrTacTOTFiyA0UnQhSrBLneRZZebbDpWcaJ4wX_F1bmtDUmmAb0UDqu38myqDyqHKDaBCOCBypvmfoMHKvib1fTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oinJtYUscymjAeBygxWHIRKE-0IFFL5m56i4cydV2Fb0TXsgA6pBNln0F6v9OYbKycWjs0wDYXbVuZIP6Z-_oee50Ubf8AVMf5sClnNiOI2ukQ9YSvFDjN6frQo-j_AbFWgdDKdFfn3zjiSNTs8b4ejW1IJhcHQdjIemQr4KXN0lOBlss7xFxeghtJEluiOqZzHvLy91DAw1da1FuPqE48YUr4FMWwxfrROrNJikGeyN8H_zngDvdTT_sbSY6PjeOGmprlKZKxnv3XHZmEdy5t72FYmagrZ-Zcdos-8fyoZvxqsTAQKkLp7nDH9KGHnRq9Pm3S7nrs0i60Ys9Q-2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dg38aIu7f7pLjrOV3S-aakKoStRijSHeSRs8pNpnn3jgGCcHDwG_8h-Rtnk5SD_t1X7ZRLl6Px1e3ySYCa7MBCt6GPaG93XyC2crAXiE8c1Zl2_jxC97b9Z8jx8oBpwsAVmnLBJo1j1sC-Z6HrU4qaPNjUtQq17dmh47nU3paa16E6_x2Y0f9V2czI6M701THql9d-nQj0xhl2XN417a_vgK1pTDYGox2KJo07zyCcdEoGQZIKojADZqnu4lO6PlKa-WOJUNHfO1IfqVvMCndRuOkWLPT3R6jSZxyirw2aPSeVWLCuHyCDl3b2JCHFjaqDU59RediGhtD0VyHVBsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8g331xKwW6yEFQKZgTG2xwBlltpRnMFx2hv888ST67Y3l0gjS0oS3lJmZvR8IQf6mRaB9wPyZgtq3Ex7CkOPGxCIcrFQlkHrLq5TSWV9Vmk-tQGxX7zmMwfysq3IblLljq4mIGl0BpZn2Aa3QGFa4b2JYbQsgOXQaJlHGuNHX3jUQbvMYG2XWAVDgjEyU4b9a4seVTSsM01boJuXXsxN5aD8fmfI-tCBmQkJD0FMeHIPMsapZI9_jlNcPH-nUSiccvrnN3jXYjyj7A1Qt8hd3jcf7seKkIMgz5WD7ZUHVBvWl3GEmoi-orJEAelvJ9mBM8uS9eV9EnMCU-vONNZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N63_LgTAec2jZ3itC12zbFCbkfnPx_-tek-BdkegUAsT54wgDrFBvIJVkWjoSa0fz4ASxCz6GOyWGqGQiL4wIgrU0wEI0uq3gHVqlPFs0HNM_9vGCa2K1DYHRIGlfJThVgBOdUlFXZdOMjlZ7Tmci8Vvk8_TrD6LfYpMZ0vKZrydbVMHAIiHzk4aEaoCpXFqSor3Z2IBxNA4igXDwwIu5qWIJqVqaR-d_m-_s8PqGI6y_s_Re3_d_-uU7GoZb2ZofB3KFMh03nHtaLf5EMpx0z1UZ7KyHxHPVV88MeD6cKhB6rZQaUtiDh_VdoPicobKKrCxWpsyeItdRGZvgmFfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDTQHTcDr3YoIZx62HVwOSV3_WY9C5SIXdu_6Ycs1ZP5fbKmwawzxUw2FYyq_ztjxDezwoDKRGfjbeNpD7ZMcDMNWDE9FnPcbbR6EM6OzFKL2lKZA8t9Sjxlkj41qkQWoPA3WLL0ZhtTh6Y7avW6WylEtAJgoqGq2u4iYzHEWIqgfoBDfte3ECeuGUYhJtF3AI_aoOlwHBNuAsbplryxFhJsKQNzdZhqg_P26wN5NYlqyyQthSRkFMvlhp2d1bN5O_L16KNIEZ9oLaV7ZWEAlDfEImKHfRk8COiYeVuxzA6CZtSFu7dgfeMdtCpZ-UrGpm8PdXgZAmGpXdxdu8GAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dDIn8gbFu-gaIFzNs2WQ7Fxz8PCLg1HOgzfTjOJJk_yPQuHubMMUN_eMv8LCB-MFpjoXWUgKdvbL6SF0-i12y4S-5THE1uAwRnsOK7JWQlNtk0qDCjmTvD_CykswsU9yH0Js8PNXZK1GvpD-xwo31IMefoEH9vd-FlssuP2h7Qe9Medl5qOToXqGKsnAGCFug9fNVNs7HIlZpJFOnycRf4uzVY1w98uykHMrn4CBqMksn-GtiIChKEpVjRrM31QZq_lnvRLK8-RMIdaXdsM2tU6ZS0MbJRZkuey2LpLg0zdKL0rqbe33rp6NwmjXh36G88VP1agzWziftc1eMP2W1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KCzrXr-dgEDItbgXdWmog3ELnwGq2W34DzRTyjJcx91bAzXdLj-BmooiIwiZOSwX9EMN3powE8mUthDkpvy_So4D8yZdLPMOrX-1TqKcB6Vzz5kZXsNxxsyvcyo5__qtN-max7_ITDkJuviYxXe4wvDZm9OwXVuLvegfVke2gIj4RPgzwSmGoNoM-dDhzI5z_5ffY-DGTDLK1ZfsExVEXej6GKUoQaP3gEQCSvwHe0ZHHT27d8x0AQ72pQ9JKmkH2xwKqGeSxWi08SP-2uE8eweoU2j1oS8DnAmaoJ9AlhIkesuN7JnaDua2Gv-cGtllFEsjksYg2yrpqG-M4hgNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vag2wSV9HyDZrwxkLs7PzyLGPqFBR3cgTXS0HolyZxIzMqKA9SbCcflg6pGRMfZexLprra_zmMyVYjb6gXKrpbBoi94tb7kLwgcb3L_qyL3S0-ocsgJjNpwSG5ylETajpBBZzAPEVnZ-Sun0b93N50QOUnLZ1tJl24xlDjSauvExlMSSmvyJn2HzO0NRtlI4LywY3qkOboCuZrUeX_olVZtVHf-KQWWnogIAeFKqUGm3xo0K7e1AQ6e7fxiYqvbDe7vlMfDHYn6NfDCXMisQ1TjS-tzV4ge4XguCr9b2TBrRDWpLlunb9l_UKOt3q_iwgOHjomPpOHgr796Ilhk0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nx0ujRtR7nrqEBsZPm2OzBFMXhV2NQ9HaVSIjRmmful9tql1Y4-9Grfcjln9eEzrlVUCdlXEM2yBFfMw50O57QTFBqWhJLniCOziEWC616FXQ427ocoEc-y-Pt9e_-oPipR34VDFUo2NkzHuDIuEXzU1qehxMxc09-Tq-YidXlwJZVD2ZAbw78QychmY2XyRz278ePBN0CVo1AhF49fGiUz0YgBcutMdoPB01ghrO4donquvjbEM2Z-Gg1PvbPlUCQNTLfgNti__XUOoZSmJrAzaVTXqNSVNTXkN8Fsiq7PU2kwxagm0fS8zIuvfqh1enR9164khFLCg6BbSITdSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRMl7NN2YruD1c_Q9NVcRkeOtqbQ9GW2uEm4V48lpBiJeWWPja7RZ2zQreG4MJfgAqFfrqljz1ahBUIhhrQOUv-vzwB4LCpC6aP0zB5oIAG9RU3V6u3N3jsWxg2Ynwk84T84_JwMDjfNQQJQQz2saPg2nyJwzA9nEgiPIldu5OK4zIu3GO14apq79pURLxU8k2PSNQj6-a7iPJKFH8aGGsOzYrZIMOYP0O_VKQpUGG0eWnIIvP2h0jjg6J5G3x_R5V9bLpblgVYf2kFg4hzP540hy-JfOsruzlcotjw3a_tdX0QsDbNYTxKjqt8a3ZO9vksPSy8A1h1PV44QhsCZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYLY_PgECSDqHSIe6_tmtc1KLEU_iQPDYNkJEcbbVS1oLi3GfakggQBSe_a9-un67v4lThxhVuqRtwddEzpXvYkalZHT5cA9w6hYDLUpwkE13h3l5wUPU8Mq6_g9LMDhjOgiDo8uih_Ci3tpl6LM9v25j3YgDVjsQco5XnkQRqJqG4h8vtQCqyBOLDQbGG9ULe2_gJtFFLgMefoLtTUbj1O3Loucp0ml1mow1bFLBY7fKm-T4Wdi70AHYH15IbT_VAqG51tiF7AUUADes_idlETtwasuCLtyUEzDk61SDcrfN0fb2rlj60e7jMvqkhdCK_B1sNjRKpOqJYyBBeSRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iN1yWBSFweZ259PuCyItZG-mgMIEiSbOBITDL9q4JSZKevSL0yE5agaxLRUVvpVsQX_Jb29JYUisLV22nEdnstfjWIRONhDHBvdRxkvRQYzYCojs2_053thaRmtzvVNzqNn80OJtrXLoA3IDyUbq2F0xqcoHMFcQ_CtnakSG6vxfrz-5__SjjvWJUYp7jtnc3kR8fRXa5xDvKcsOoy34LISPzRwd_mcHjbl4PwqauIN7rPeI9g-CKZNrnlNt2ENDKt0YhWlQ9WgmZ28rQb6nZtK42hra94FB8dz7lVARNZE1Z5iZaoI2lPOzulsPJNJ4wu6FO_bbnFRhrJwSy1aopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdIUu_XVdcbOFsF-dsbuvTAhn9uBBPqcM23EG81Amoxm15kRj81Z-OpZQaHyFx6wU9Nh111W53UfVSUoHOuBmq7jvUUc3oLXgbDxA0UMx97BB63V1d7-ZBLJZCkP7AD5rMD_3lHj_TwX0S9Qy_Ni0EGLEaXWYTExc0EAGAZ8KFUQKyVxFJ1GEuO31bh_3sSFGQqVY-dS5DDBVEzAwsg6HtXTYJ5MoUBuBdNhdGjGybz3ejr2Gy2Z_vSfGozMqgnpExki56LRHlmiVcUqMBrlVODGSptlFGz-x_SCZrcKzYCPFLGUSnXFJVtEkqvF2hwfog9QNlsT3DHhnXel3V6Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Om3NLHmsG8vdahRkPqaTDRa09zcmqEnVtfu6ZNMWKqxc5wwULBgp1aWIyc4DHqI0v8iucaDxAcjHfDl92IWSxclvTaFUDYE58OnJoq4muvrQ2xytp1VwBUkzYOKmksRm_FRmsgUZ5JH9okb-EmESx4xEV8O37rFeJqgY5TKsH4e5hV9LPFnMaN04aW2uGu0ln2JUfoPX6A1ZU7Hmaix7b5BXNB2qcdfIQk1mNs6OtonZ-wqTNbWW9F5ZqI0VAm7kHcNK86XUSJdjI6bM0llFPNbxtuVahwzorh7tEbjNmJUYyvvLDR6PakLoKzU6v7G7y9udPVymtHIKzwLCHEWHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbmv7WQl5mHW49lzXSJY3ZSdnl8mwBby8lYhrhndSyWkXcFks83LT9EcFIqKymjRwYbCLDhnwtmRIWs_RCgYBSe8ZLtjT6Dr1YhNL4qyRoptTkGdQtpcC5DoiUCcFKf0bIlCWkBZLTyc-p3B13nDPlsYRx8-Vff9tr14zgEuLc-Gw8UCJ4EOdRQxnzUv1xgdH0aScyO5GcfXw69z_A4LLAjul0fxOkgiGg8xWRY-nHxEs8VI2wTHBn6oAFX6Fw-o0CzKkvNeCt2crv5vUwBD_LRdOYv_Lo31LgN-22Yg4WRoSE-BlPz34Xy-wansz473DOFZfET5Dik0TwpTZzxVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V9R285MHBU2hfwWzqra5yeHgQvRoXJEToKlE2xOXf4St6mSPGF64mtiyUVNzVur2q7ukmzX_EbAJgElN58r2BD_a5kcd-pOvcDnMI8wacqRT2MMzyJKHEL-09sFxzkkwQWqZowV0nzxtpuK1e9YMXSZJLyxmIXsph-C6VeC78WAF71dtfnVowvkEMkIo3eNcidBEmnq39gIZqVqBmJRnuW5NtAaoj8gFQkvasuvcEGJVFxMfVzWc6YkZ2-fG3g3LEARUtxDXH3omXPoII9qTvfi1VTALY7A4ZluRauLqVh7iOPAcqC01GPDcCUYsL9zhLtwF7TmCZ8bUw0qtXitoXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQI2EfCJizO0GdjYon5vLghKaXrTrYqQ04wrfh6q1kdyGXUltw52skX1vfLXnWsezV6K3EbapBYJd2E0sjz98VP-Z-pg_VSgjaVcIIF3o13qduKtZFe0Jq2Xb23tOE7UbIVs2x_J-Iv45tuic_mCslcJVnrLFDuYWK6rHNpe24KsSmV88jSrWTWzegFEIo_FTB8_NT0rbvt1nqCBdB6hodPcHss6vhwoDR5t_zn0w-hFqnRwFRpysW8OmhddRsvmmz_R2deRhrSU2tBT-VdBDI5304dQrHBRnDj5zXntzIscNZKmsQpVuqm721aHdjbcJzoOzqeHfc9BLkFKm6Il6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HG13WOy28cDF5f6D6VzFSiXfZtD5V3DrsaNs7R_Kk4PqrZJGZm7R5qpkKBAB-7OtVdsDN-h4ZgqP7NIswddsKPB073SQVa5SBawepTTMPjGMbrEubU-5JH4vga91ZShw3HAiLK6cB5SUqA_geGBGYkK_l3R1kioe8oIG-tziauXLfqonbFFOt9gBKQtGPTLW1yLqJUED5tcxJ6yCeG2b3V2tgzT4EgM0yjmaWKms-xzZWYqDYcjGJ5620w_mS4MqH0-xcmI8OmuB6lc3MYmwYDFbqdZ8Fk-iw18o2vdtMiEIwgz-9LdYWsA19Si_2OzNxTrugoJwL0BEn9J_fyeeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXOKVwYIGsWP2dv1D01It4m9Un8xzZMHW5Soe3D8mxlysz9SOr2ePJ_RMsuT97XWTd0nU7bxE5P-JoXZkBig3-urWyTsVjVWFeSblTcJffqksO_MQSOVsbCrnpFnHeiptahLAWJb6fq0mAMnCivq5ryBFWtM93H8hoolZxJ4Wwrwo4dV8YvPsBtWvNOSRl97Y2fwysA80JD6OqxZVY9roykQkeuCzF6SVfeVOaiybjjDtABGCyBLdWelRgg1Z8RT3_166g2WgBiwF_qtHAzn6u5Nps5qCEQ579Yo4x-JtXGx7Lglr7RFhVyBdLw7jBdlH_6vj5de3gTFvWgvSu_tgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vqia2tMLw9iZgPCQJD2pjXlNJIzdUVNNiVhqAxdaTQYaHfsDbQR4obYY5V-gQCbcMFRlfhtLV6veLO5-_Vz8MS8wb5_wxhpy8wid6zcAYO6TDzgHjx6cMdJNeNd7fCyNAP5oV5qKO_f4uX8oFg6SvxrzU9Wnwi85Q5CERJRD3n75ztN9rnnuqhjiElPodj4D-3iFEIEShOv2nPZu9n1Q9yjFoI8VuJ5AUA_aj5xAQIr9Vz_23rK7ojrVuccfyvReXgQlVu5AkqMA9BBD6ssKjD-jSpxpkoUM8wmEyJuLAtJ37-0xNcemsi-Jq2_1KdiWTi2aiSiHrJbYOvg395dYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSMHBUuMu-g4Xr9DGGZ-K1ZvwlfKaTGCisBe47Cf6LJkRUy0VyZI7-ZyG_-KW0jLVlj-M-YjUhIcY4Xvs_A0Z762-h2FbicfButiqKyZEZHKzJJzs1vQx_pMuQAYm58iOkmoAlfRbQEMCD1p0LnvT6VY-vbjmh2ZiUWg62_QBaJlvcxpYS_pMsRJftrYEiaUfEGY63YvQFNrnbiyPJvFYYcmtOMLVsWwiQ71zF_yM1lqaoM5gBnSG6yRKKDFpMCDTQ9jbb8m-I74SK-mcZXY0QXWqH32WjroMCzJmBkdZ9hQmJGuGEtIzy8Xm0l4TYSHy7kkUIVLOKs4sYWaRXOZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFB9BqM0F9svD3FDMUVCYpjIeq632OmcJtXx6X0NQ73QY8LHftD0OXET1vCSb3dP40ftmUvq3V8M-elvgY4o-athHtJW9OVZ5OdXvifaN8trJGImV5S2Vfdqa7TXc1PLTUWbhpuhcPSV8rJTJ8m-qnlr4GLubvcRshTsI7IfqkaGXJPmpQgKuiuMtFoznpzHxCwxrvHXTJljrNcDNobnDPvBLvD9dBvtl93bwxpNRB1n1XYwMyqGKPhRoT4zgDxjkSaDyqOQ52qiRdqgbwi_W9BQhJZMSSnEzfBMzDrkRddkPuZxdx8Z7he0tsAWnIfiBoWgqlNzcWO3bn8jQppdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IO-N6vX0ABHrZlLLMWIxCy0vHsU3aXPV3JZG1k6L8l58OcYJUS8OAv4SMroIRNsXSjaeGJba4_D17iufJKFvY4DJgJ2ZOrP-X2vzDu-qbHY50O6jOWtQpiyyqfFuaTQFRLu_V20B-8Z3QmENiX_cMY4HW6bREQlTeoZA8Ncz_PmFKhHjb55WD8MMVnKIH2jRwnXw6CjVzePGs2gXsazv5zsfF2-mAXtCMbbiFOciTrpLlcwOfRpDC2UeuXviPYEcOW_qI0KRTzXJ_ozpR1DMQtxS64Eqv5gq-5Ob9iPwmhfYHEGl3We8llUdN5hJN_ORFgduhfLEJlt7K39khWAE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SY18jxyE7yvfyjyZ0QzABjO75FMhFOv2dMSR9O7xj76Sa6kdjDbYiz0Jn2lxIObx_MngOlkp2sZ07c2vnBqI7DfbkeItXCZYrDZVywxYhYKHBOozGEZEki3B2lagMAUjAzqcwE6qcMFD083anCWIzxcYQkYly9r55coZ-aCP9Ph87urJMt0wkONqJl4rrG4av4suEEip9emQTemCMjWblB-WQoqLgGxETzucZFvtbmY5vorKBIsnDycHqxc_zOXSb4VIZBqJJCEtthEnuQDOsAWe5yu6NVTSNEE7wANDKoz43wzre5Lc4n2lWSdkvtZW7gW6r7KCk7SdzMebiyuEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEG5-LcX8ZJVCJFowo2AKMS_qIhLO7BBAriLkTX1Qnlig4V6k85rU6dO8iNXArqo9frpwt_n_ezCloiqjbXvuzAMjy1LBJnWEvZnOnuF9seazv7lZTae1TJxXOT9lvIBdftm0jEYcQb-whUaNPgrFeNB76fnnvYETxTUCJVfcSh5VV6a9UQx8Lxet7fRNXVfpeqNwnioLUfRtL6tvr5KG4Hue2ZnRo1-paRb3Adzhq8UqQsJGYGImxZ8qnw3h2ktei91gw7FgwxIEZ0Gt0Q5x4whUeagiKt5d3LnWgoEwS-zbKd8sOfVq4T3GaFiI4HYOqFwNWdl5yjV4LolmHkndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSokJ9_jEueU6_yOIX8rmjO1VcIZrynNS18blCJ4AqY5dH_rdxHC3JUXjMMWooKplUGIFBvS_p9SG4EEYY7e34_fYuH3OgmUZtm6YX4OUrQ96wt-Pk42-jo6aqZvK2zy4Eo-GGQ2w7MyTrbg33a10x7Q-m-RdeQoHj5fHGO10tkgeMshSNNkU1M8pH1k0Gra6S8nuaCvfRYLj-vvCnzZpY272u7HkO1gf2b2GFX74RgYo_6XtV65iwWM2e7LcYFu9BWirW4VNI3pbdunEUa1kW_nYgSUiG9i8_VP3nIeQ1BsjmhzYS_6cbiU7sdUcZq2M3-9iIG6OU2LuvvkVgBt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/luRCI77icBO6tavt_BfO7ttU9zDPIvKGEyheK68NFWisiWS0EZSI0-_-BpsZzMDTvRvUpY0DD046o7pYtyGyRUSLvoI6T0vsAAE52LclErZaiTPwCNUhDb7Zm2pVgRTNGvDq86K7aU9TwcVPtCV4TKzhBH-XQuMon76QrI_mkNwayKZ9GxrOsqzwr4ZHf25rmP1PPF6tjGLU4bBAWxqhkUfhMBEkaK0OTIS8rJ5vA4l2G_PbzVHBTwQGkiwHieod5h2VaF8D9vfhBslx8ZtW-ghJ5P6yG7CLdL-YVvBCMbNu3eu-Avx0bq4LX8RvPOy-80oTZa7EbvuKTNx6ck0tyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F6Kx2TqVjBhAkpU9JWW55-paxreKH6hrXqOqB-_PZ0eGxhXIJiFUjInHqlen0YFFLNLdr_KyUTnfen8bhYulJPyWqEPUGIGfsKBhFYMqYNcdHWU9GCneKZ8esbuJ_Xd5Uz192n09a2vPr6LnjBQfgD4lqZ7JOBjUkn5MbD_d6TRv0cZx8h9WaV2cz8gxkjI6oYVI63B2rO-XRJFTr5PZ3p6elLczdptOTV4WJlULf2DDSSGDVMStSV46JoVv0H729-sTmpI5QOEK9ACnKvHzogFZ-POGMdNvxHiTsblzY086uZxEnScndXee7n-F53jQpQCO7siZNI0aeUwbkdJQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=AdymU5JBm9M2qd5hpEDw8hI33u---KTLBACe2bPYF5GHgvW0XU61PtWy0A6trNbIcP4S1DYZrHteQJHnP6T6tnsu9vk-AWywzOzFTijKUNuc4XSuMofYRJUwnxhFKDy_dAxTJb9CnoVC74r1bXAh_NCqYrfRo84Su2yE2bzLKFAzwDf6_9LVC0R6eox456jrGZAkifHGt3_xQwzM3RFJBx7v-zY_06c2gEenIwPPolb7Ev76JMKzALjbYWUgq5Zs9LnIcWhpDx-lA6mN-WYVnT0R_C_TQw-n2pUHbPFv7598J5MtIWopyMECffFUMg8-kCJLrxp7FBgIw_e4RVG_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=AdymU5JBm9M2qd5hpEDw8hI33u---KTLBACe2bPYF5GHgvW0XU61PtWy0A6trNbIcP4S1DYZrHteQJHnP6T6tnsu9vk-AWywzOzFTijKUNuc4XSuMofYRJUwnxhFKDy_dAxTJb9CnoVC74r1bXAh_NCqYrfRo84Su2yE2bzLKFAzwDf6_9LVC0R6eox456jrGZAkifHGt3_xQwzM3RFJBx7v-zY_06c2gEenIwPPolb7Ev76JMKzALjbYWUgq5Zs9LnIcWhpDx-lA6mN-WYVnT0R_C_TQw-n2pUHbPFv7598J5MtIWopyMECffFUMg8-kCJLrxp7FBgIw_e4RVG_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WiLOk1_R299QwWENGdtuEBXwG5Z7PbFrR_EyeGWo0_Yf6gBsT2T5rUYj7GLt3gfSAeD3_5Hy7VhVRLC_M5lQEQ6jkqSq-gRnKF2ojXfSA74aXxnLM7gTe2SWyXtiDbvd_IQUsiDViVKTSXXiPbbyWs32I1pE_NhfMrBAD_vFYvcBBKZQ1jtYVZC639EVo4jsw4nY_vksY_L-T9-Y0pOOCLABq6VpGW9py27MzS9KZgPC-FSW0o52yjtkaLSGyi6AjnDus9cyg9mQ4ZzeT0rR0QVIWeV9UkzkfoZOD72FroAevN5bhYvv1wvKrlXVTU0pEQpqeRgxNoT2y5bgvDI5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/otpVeXbEiyp14fEa6_kY8fyICGuOVvJaw4x-svhA7z_hQ7XHocTARZsUEoXKzLOzGHrWw9cv7xjGRn3OOqaO1aVv-3Dg2RHgnvCpXRXntH_ajMQ3w1EKIwMwU1Ft3OXqZNdIRmqE-B69f4Mey6pGSYb5H1uAeF0nFuqxvIrYEDvDqWlBIbV6KCwu1bTtghNa9S3lQRiAgfWQZ2_MUMfjzOXMt-NaBKLSOn96ksCD9jTEJo9tmUuuujt-nrmz0UIFz6vzlOXTDmp16w4dOVHAAtQMpJOwdQ6ZACrp_2NsFCeslTa0fPTh9ORrGL5eq84iKM_KlE6JXDw_AenTzD4Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSl5QNcgv6YQqP7L0UCsnZDG5tKEA0ynYbHInfNT5d5G1uJqGksQvsNLNF0GaY10EY5KiUXuj4Eri1ixc2QBA3yu6sqTWHK9TmdXSrM9vcFPCdIHR-6pnLW87kdt7nCvQJZF-8SgBdHqPo7KOCGvdBEDqZwbBC0tOJY-k-WrU-quUuJ-xB1N5P0qDJl5cBkycU0bmWdQXWawj1M_0L350BcAv0erC0TaVR-mfB2dlzcx8_2N3sN5kJt9PJt7Xf0Lh2OmfbGdq4KOE5Nn3T6vzsIzFRep1gZU6wePJc83MV_7dvXAP_gKEmRjNNwOuqecXeeG15ozcPMdRt2YkiQbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSP-YhJEkWtDrALra84FUC4dp2DTEE8_bIKTiZPN0rmojEkE8eYDVq7UaLWLZ8YnTw2p0i3Y-DzsywBoJo4xIYoEZyD-061gkU6m0L7inHPQV11VnSUzO1kQkcRig52WApre9hVxBUSNhKwr2lKJR7fGEy4kTKAHK1GEh2B-EsbepFzscnLAWxaABLCz-bKGVCkl1CoQQQi3nH8qo0eqa72r4uzfRNaLf_YpMGLXrkX1XPQRku4Bih6989BbJ3egOfW9jqQb3Hk7wU1oY2xDc2Y7lSq-4hLWphcnhOz7ru5PmeOQ5-yY9T5rSqWw0wIE0-mC16WFUbZ9Ken-rJJ7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCRLsDwFEQgT9xWXzqsKvC6r_cinR2f_h-Dz7OtZz6thaFsSaX5LbPaB3alaPjhlenWRhv_TBJ7R59NyXF88GO8U0cbEvsNygBO8mOqCU7tBA9yLujg3Brq3o9dy5OMy0mQS7UNtqwT88K8ZFZxnePFGrM4w_t7nCJEBxq1OBchfPYhMXeZtPTw_P8s0w07sUV9nw2AJKKk7cSxeM34sHLNovoDGVpB-vURMvJlozK4TyiF8i-uXvcq3YNneNxmFK--zsXzOtFiIZ-6BeerXseYSgIuOGqW-zHcHzNTUJ--UJQz7tDVjzJHbk_-cz8JMBIuHLhVAoKSMqhVAnepJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-rfNlBewgHUvA7wu-1sfPKyDtXgeYKMOlvCasDkpzGjYCBk9-3lefI1mNLRRQmv2pv7fRIWNtI4wfBCUAtdnh19Ux1u_EwKNtIVFwvO_chKug483TC3gUGWIIXaVcMot6aVHlilMHieuyCASTepeduh9SyJwAb8faoa1O2X8_iNdwEzY3ReBjrpgpWsN1VbznhGT05UUbbBhF0Gi9mr-BIVKf9-xMfkZaeWpb-hGwY9iTkHGuVBgCK3qjAdCcVCSQv88HE_phQ3Yt5BmPJfHrLIla1XVtL3BZnspByyMn_wvXesu_YYHPEaqagmgrCPJX8k7ypHnDVy7IFW-YGqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJN-CKFrdRy1ABU6VFcRSQ8fv9tbpuqY4-9SlmJURTV8EgjoQFdrTvWDeeFYtuCSM7-gQHPj06S7qQEXYv-E1t0BxIhJ2WegKGSKvayvaWamydY4sh5VEPW5mt-hiOVzGGxvAUp_K6ZHkMw7HHF2PakCdWAbd944b_sMFJw-i4FVwkAs-TxBwDA2W6fE5NvUD-dECbLcSSs4eP29h0azWAIzbbXkXYHW4bGQ968FvzOMhJUhRctTBZFApvAru-GswTedLsZorKXlJj1c_WNqt1w6r-Etwxw-I5IcraJzG-fLHHBF9OyZRzlPCwUaCAynkyiCz95fIccLqvP6Rl2r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCp9zXn5X7kNtSdLn8fnaMNr4okR0wb8YaLuHYAfuAoFI2HwHwHmjAIL62UicGfJWnWTbJYYsCjEANF5qd5KDsfr0hBHx7t3KDhCJ-rLX_t_KaKcn9rF5C0gbFIME9KrU0mKAcMpTwA2osu7DJBCv0SspJHeD-lkEyAK0q4NTUtE2U8-k6Pov8d4VIjQVKQtxn-qmuIOFIsi39oatyvAFJfaZ1Hb1_s-lDeKAoWJ-P-QWWBd7IL9HoIwHqVjj4XVt02UyhaO2aTJKoppdtwu6Zb5jMQwS9C3-BjaM2_Cnkdy6hUQY1-4ygUFH93I8M9VVn0qlx5grdw06a1-zn44RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UAxG-nS-MFr-ZGsAkgwZh6jwz0zKVVmJtQCjgZXa627DuB_3sdmJmUukX46FP8yRDMY2JfzjeP6HeIjwD1cBX9-f685BwRX9IJFWkgGNnHnjjOCFv7eJf6r1Mw1oykWf-CmwGyS87t3kwDeLys2fsPCEdY7ECC9KeXJYkvcx_1Me20VyNu7gl1aLp6EO2yZNgPxRllZsjR5uBpDwZ6hru8xiNb5ioTYE1MHw0UqsxLszi_s7KA690Tja_6yv8HmbToXmLIKuPfWGbaBcVDwiUpoCB0SaGMs0sTrJOb_DzDyxwYbY8r8y9US8KZgeMAqIREt3Gy5IsZoLW-msi63y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v06f0QjEcVCIIBQCZhwxkMWs2UgW-1pOStFJl5n5MbFm3uZETbCHE-iTZXSdmneTS1KIyeeahJreezMNLklG-tn6Qq9PLhpoK0tluB9vkotO723Uh_u8V58KXeZokbGvHYSUwSRDJ2Bt6oCeLKFN_A90wUPzpaqi7_-_p8P0jvoZsuRQLQbmoWC1bJs17pcIHio7hruhjhYuaGbMzaNpI6YIRUyXObNOLCxwaGwqGNBa71KOCvwpkOoojd2sJ9NFIQxhJGMT-jJNqa8hbtU_QmCBiUoOsLOnmJ1CewWyyYylGfMtvzcn6T71KYbfZAQFZ0XggJ6cnY5xcigZn84HKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QiHj0ffcnUWX4_zrA8EJ8EOnQm-AtsLSwu6XLx_fHIRB3-KJp1_R7_ayi49dEQ8bBeNOSLgIx8b9BQrkC4cszhy0xmYHM4jaTh8my2as77gTGFCslatWp0rHf7k2vwbND6TNy7W1_TuAY7PAUYLvPQI_kWP_h-BsCphurPfmGqpymVYzxIwB6QbrbarSEevNOif30SmA4UwXT0UGUGy-xAYPBkVtDf1vJGVca7vbcWrLv22FFTqoLRI_SABBnlEbWq7pRXB1PAw3maU0EKazJpTq_0-cm7XDo0UF5oHJ-O__zpIMDO11oZpwd4lI59p3WvP92EVs_E8--A8pznhX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aqzyRpHEmpi4GE7xnk71axDu79v-CcLO-665KBdtQnOre_NeCZVOIjlyzvNm1wc7CrwySBIUR2Gj2ZYSnO93Zk5IlGQ2QpX5_YJCa7mPdC5JQ84YJP9uPCqcj1Co2Xsd22Fv_s0KTfs9YRUzEo6rHVBDIV4mwd1vvRPSyuk2JkFoHhpXFM9t8I9pJqjAuWT0AdbAop4VY2ZPASn8LXeBIhKQHEZwywb8RTWNhIdc1ogj_v_1RBROAIE8BKfbuLWZo2rJb2upilSkIB-citzWHpZMQ1Vn06JZmAHXqzRSwKNXe57QmaJPXLsiVFAOS2yR-QqO7zt4gMRWA47THVbUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPKt_V6eKZx7IyaF2d6TXCm8xaBhqM4xtkGmAbKL8-oEiHssywoY6muHVkL4iu4LMVl6kOnYW7uKVO2uWOKyn459KIpGrmUo4zT7D4flns8F1cAkg-oKLIOyCBIDsRgFWOOpuAnDCYnLU-kKfx3l2u11igEU9Y1dPsuj7LxmYCbAZBxSFhChwyJDwXJF1zOAyDXztveC1pp2iIDrrIgr2mYdp5oyclBXvDScKGgA_bEjCzaIbEcSKsis5QhAJrOBjiMhgxLBhROZT-S_SRVjLw7z6ydluEWKZmNZtWf0bAIHUu4ws6OoWdrxWNnBBzusxoKXXbD__JJGQVS9G7gScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9QxonBfvmfFznrDkElAq5EEV4vXlwVM4mSaikS7rLTRAy7NRYvnKN4ujVgRujcwLAE9HlvDjilLJg57SohPi8N7QrR0asHpq0pwnDZzPnIoC6LjLHXei-aADLrgV5jJyB49av-6BuXIVzogPG_y8sbPhadGeO0MHEx5O66YXgfgmUJGxC9vtaa6Sm2QAyfYqwdXaRCwZo3900Ocie07RIYMBG578G6R6eEqTlC_6CTs0Gyjh79aI2o2pAdI0IoK6Jz6H9n2FbXVHG7mQNB39EH2Kziyf45qKBFLxQ5EOzBv8vgUosx4k4_JjQERkuWIy2e4wasrCE3wdZRjnsUN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHVxETwmcFMEtTIekX0rzhLf59thy2y7NEv6DBhvJhjNqsErv-o5J1XMJ-vAjjEx96jqeUvQbMF0U2lMqm1ZeDeHuzN44pXsSYiibp6CKKtqQhQKZyHhFkCufl6kV8cDH8ASyxcNWZ7w9FlHlHTY8krc-SEfJ0iQlhPdXa_cW41ssXsAL2UqFX_G4dPE4Uaq8mf-ktzEP7LzPVpG1MO6pSupyvEtuF7HjhYON_cuciMoMB1jQOem_sbi8udT0u1bG7Pp7wCTVN_FZPdoPEt4TtUHKuD10-AvshTwlWdfezEbRFTH5jPhULero63lGUl2B8C5jaLstymjFq9kPl5dfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhsb_JujQYDYhm56TxeHlRucbRTv1JEQNmLHQcP4Y_EIEz3AYeHf3_H4q-ducHYHdS3Iq6AW70sNXZGlX774mXrHRpsFUWYWIxB1LACESl6V4r6joC45kk6Pevi40CWUCXKTkr9Z0Pzvkp2mMQs_0kJOPpCbwU7dzAJ3zTXuBLbvG6g0IlncrCXjq1toy-k0IZ5ti4b0qVzW16oSv_yn_8tFQN7A5aSuNqiMRiatbadDMHCzC2WOBR8AWFZaBTbpuReflU6Z_1XRIyMynIz-_cqMQPOuYF2zQVT3SfyLhed9e2hkxrNCv9kQauzFHRToeyr4ai4__tQAOJWvIIaYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5gg1ogxcmsBFddvXuu3TJ891Bj5QFTzO8p8Zxy-x74vlQtFq5EY27wTOS8GhHZY07R7C8cZcRKxW97yDgIxdcaaIkGstw7ADSHx5EES-eqHxQ5QrgYaQcoVrzHTl0RR0wZYohWpAKk8Q8DwxvAgzKZqNaBPghGr5ieFAVaHA9BlOZxAVR7XXnxMdKtZOX1KUeE0WOVpO9QQbxMv3s2D8TvuaVjaaayCBOidtPGKJeVv4zggymr074C_vUvUJtoIM0-qKhdQvyl_58AWTHHbkuhhpTuWMD8nJlaM80Uy3mimoJ5U-9lUcwKo-Ng9Wsv7XVihHM7acMqcwkH9S6De9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYu7u8wIJVGtOHEOpqRv9tXSTQ1Qpxf1lO6-Lv2HhfLZS5m5Kbdj7TuolO6mvL-bGhGN5m8PlUL4yBzKlu9Qz2B5si3q5VE0RtMgZLg0q56tqpO9YJxoDlQi7DyvVh7WfF73q5NAss6pDBetenogiqdLmMiUowl3r3rY5YH68LW2mLCjY9TdDqfUrHpUp3BAN4gni3cjq1jeTX3En7FFiCrDePiQqFWyUFrZ7G9uAVr67NUUstJZOxXri2Ejb9qOSbPGPihC2YM-WQGSHQQIfa-F95b_0PKQfGvMXC6YXQ2BwBgAptf__2xTb1kKrejs5Cn89fcxF6m8IOdmvODuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFyBaizB32VvbFXZamjRFXZFTK9OdJM6DDf13QxxV07lHonF_WI_jaeMvYMD-WMY_n7zHo8gwSabsHcttf8zOxn7Oi8gFYFxXepfT1NLPsyZ1zS-QCQn7520pjDjl3oS3H21l11NZ4gwfp1xS64tk3xA731HLiE3ZfXGaihbXoRMhPLYoTeGbYsY7Gsec_MHhugyi3RScSOyafUj4LhE_SpDWQCYIDniq4SfczIxyV45P9ODq4tSreAID4CmpABvYfSOhkBiXn1hwPO0iF37ermBWI_QNzsvkof8OFByXIcloPc0VBRG-zJyVlSaLA_Qh_BRhm1kR_msGEZAQRt8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h8KkTUJsx7Yg8vfexneBnyJzeoQaXafGNbFtxh8FsBegdBC93Jt-gxNdsAvYZyYFWgIXFhqFcL9enDNqlMTaQVXcw-f_-W62dAyvgTS57g_fzpHgbqZf2rldcDEtfQG8TIn8Hh9VaQKM9QOn0KJyQrx6c6VdNgAaeLVh9n0VDqVUboW_DBBxcnhJDABWj6PHFkt8U79SQr4FQOxeEPEgFwjwBMOLl4H2FDcnPzHeaO4u7WwFxZrHavpxFuyNjVeZIUVuby3lMqa8LSmOTeQzhDNDDkwpwNkqPsvCq8d5aSOh_PpzEKLHVC-jvSLgleWxHTJLSTTlVZq3cgbYEZfkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_ynqvmH7pav-86rkWPX5k7kcQpzX3GjFkoRL8mm6npyMGfPiSYZ2vE_OAa4fxIJWq0VBlZg3ksu87OaHMe8_PrUpGz6czFZhOekCo3oOj2uC7Q6CmNTkR32NpBwEmTmfSCvvgWp3IRmKcv7OXiFkBrrRBTNxtFivBObl39d5oMPsNo5pdTBm7pJXs5ajPwYTCq62LzM6weKdsr86-pouYqQn2Qajwsi9HSEdPxRjm8rKG3w1xX5ctQ1UmZ2ZJDFs7gL0bDQA5akEgC9P1C4Qr4mctdEnF0cSRZW802qccaaVD72bbFLHCyiBRYs0c0XcSOEalwvrTsH8hEZZjYgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWzRNnpCV0fjxuOvoyI6LnW1P5RgR4-3WaocXMORuHmKScKc0TiSMpk_-uggYE0b3sBTrjnrJH1qJIRUS7sAlSvZntbVXAuyYUUkeJ1z2d0Agu9ntNxkZx4fE-A2VyPAuu9dBGRgq84QSSezFEjXywk0iuMm6XiX50J7OgNCwdhO3Vnph6nRP1dqeifWOh616oZyl126l1u21Q45owAoVF0YXTqVH8IIxkJdrbuo9jR777LJjZRrR2GXso74doLrn5-LU8ia4NVgXD_HpqmEL6ROYbqdjH30Qlyf5AxkTS9lM2OAjqUDvn9TKYgq6QyBgjO3DChDI8t9GN0ZJUxRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAVMrzR21EA2cNmUY6pRByaT1Y8xwAoeLhGS8YhgR48qEoRh2t5yIa2BKyuhl5FSaJRGwf7q_OnXtWqZhN5dcZAyECs6bKTp-ZPqqS-ixHxNqxtdgasz2UlUQPde3BU32oOZS0xGegstyTgBVumUeSpGuUmL7nNg17cSczMUMAXul8wiLq1YVOfp9S7UD3MtGQfHO9B33IqYs3YhbCYLBQ4dioEwi5UzRno7MG9ALOvfU_GS1_AirCENMCPytEVrPDUZDxMzZdF_Sd_S7Lic8yKooYF6e3Xw5HNu-4bH4pOOWog9HemodHjDMfw60bljAzLPFX8rraV5sS9zxbXomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbDpyHPqELlQ21Asmriwf8D0JXT8nsEuT5FP8kNlKCKTqglVFOcF4lJUi2v3_i6BTfsPibxT5s4r0rzQWto-Y6JIe_l4Kw1kKWxFiFpQ3Yimm722Gvc2Sl4wr7QXpFfld6C_-vR4sHynCJF3FWOk2frlkHmnwlqhc1lRwVrg0LI8ecCcAMYHg8HWLyQLHVaS0SAXBgPG7DPrIVDzVlplMHQbdYEsvIOn_Q-e-AHuoSgDTqRmYE3uACDJip0ZGfdQyPvE1uCglkr51xU2yDr3RO5JjmRMll54BhzUsdk8f1LiVFNTeO6eQsyC6wS7AUjgan4GTmX5SG5dO-Lvrl1pcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxCp6GnxhHpzKmnNCtF_g-Rjgh9MnSGj1MW4eYHH9J43usy-aF9o9ofpjPUPdynDbMqBR2nP3288Zgs5-cgxogLTanIAIUYZ6BSio8kx_zvjxQw8n2FYiJ7vexP0wUbG9rWBAufrIM1HX7xj9HcK8vFFXsTbIXVmPAzj4OMrKElDz_Jp1R_Sqmy83lXGeqO74INX2kOdR-UzffhMCxJYQ_5WQIEU8b_I7rYj0rjvAyqaQIl7tk577LGV-s1sEVKK0UXGow_F4TeBlFiWUzyNuBo6E_ttDPZY1C1LLt-pIOZHfewIHxDdlGk-FNk_RQ7E-C13km8N8kQlXFN1uq7MHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBcxSQWOTGJO495qmtpyppQImTFaFxgzqc-xusP6baaJvkqKtsORcjIdk6Ah7SZK9VuBqzLeaqFs8GXjXMM71zeAJvr1nuwpmazYpuMA_hOabZn1tjQM9Fqdh9cPmHafT84nCxXuT9jPWhYyPQXN7h_yj3NB4OvOmpY0X8Pnh-30PhYyFWNUqRQI8Sooy9T-3QA_8DbEC2wkMttQZ9hzI2RpynVRBbBZWTHGpjnGf9n47cNWT6yteNIGVLTKCe7zC8I3eL9I0FyTTqVpK6g14kg_C4Gv6DEi8xKArtDGyW1tqdMDaMzdwFhfjGZFoT7cA-rJrl9HpTDbDmVetoIKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psf23f-2DSOjNOa8XLb_HvxFrXs3y9pgdi5fOb4t_4EXR5yK9m2QURDEW4xRGAtDo_qNGMFbj5LiOgXrgFES-QyiitKYg-2rOUYK-AI4_KjhkG08dm1dpIGqHAGswbmJ30d8kq7dRUTh9uMXGRyz10w50hJwugJZNUAN5lHFTRAfOe3h7fDYLIDFfLRo4_EyYMuRIbDNFZX-epdO_a5WXy7isvFBNTQ9BINqwsg6J2mzmxHjCFGmLqLxMdsPiT0PbJQLUSprzDTcKWSzW0KOSDoTCO-e4bPA61KNM9tLO4a8nTb0VDuwl7Qx6VQZFhiACQuavUnMI8F-g84vbUhJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNlXu0qyTNcsl0cwSh1uCvfaGONmW3N33DK_kh-mPZeyU6aIqVff60XvSV0qjD-orEaQeTCFS5f384XiOHYggU5JCVXokLO57QewO-CV2cWEhTs-RcERL2MvucNXrJfzIDmgCT1UiY54wVWqpp2T7CVnnA3j6bRuzO-_AC8YJnQpllOx8fpAZpnTEKXUqoSz4GuNmYZpM6W-4lZM3RBryAK_M_M6-0htfLFurCos0vOkh31FjjbwJYJ2XE75KXnDBS1ngZBqVID7U7WdMMpMbr6Rxe1C2eE7Y7WeHywpOsepcitGjYcRrBppGOjqY3Meeuh6ZZ_rbFTEkELixkdwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwThptWRh99L3mdKQsknzAYD1mlpC7dPdIIBg1A9VHtcQsaDP1iD5qI_5KX2oYnGmMlbyjpvgbvR2lstqHs664UKoYjxRJnFfbOMazZoPeDYs1tqMmi2FdWZapE4JkPpOf9x0DaBaLO8OroEWdpgJBbnny6yCe41e3ytlQJGIGHwhplvTCGn5c0L-rTbKZcwwo8feTXf2ZAeUo2b_23h4YV31sptuc8djg3CqvePPcapO1A7rxyG9M5oUdRLaED45933KBvvQkI3gFPdetutarsw-hKau1ViShbgbIhBi6R0nhNRDni1iP8ZQAY4cDkHJInSPcHhMbSxO_cetlyAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTgMcVWL5e0WTK8EENAfOIWcdSK3DU30pjs9-GZx16c8EQKc40rRccXWreBf9cFAJlitPjylMtLaxHMYFEVU3CWjZhkgoWZBax6bJwuDMIZ6AkzpiGrxmRgFPaf-tIfxm1BLkguwJOHz1kLJ0xYKIj-TtbzLqBFwc64dY-X_sUctk8pwpyzlsUW5z2vkEswCOpX9i0HzxgafYskOzLwXqcopAJylThEvblW3vRX_UQt0mgu1jCUKkZtB8xFDSh5VbPGg9SWudHzGz5wfv7e95ocZ43wj_C2zda_y0i3XtUKSF_vUck9ATsNyoUFBADNieG7K3gO15Hsuho4SkpGUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMI67XTUtQuDZ0gXyaFajzIueXOqE2SDtOxpjFdEFuPe-aD1rVm2lz2cDNeGcpNxsG7Tq2mzuVt5_nTdfo8_Rnd9LCxL2gaegHfRme1Oa8gOqmL5HQSbl2tah8_yUMCpbAtmyG8FGw98fQz6ApofP7a5S8gRcCMqXfK3rbGYF4v2V-Jf6209zYFgY3Axr6Mm_7Szdk-NptH-H2YGSkW-KstMif3Vf81EUBa5kuLGZNuHoiGQuXTZJ01Z_T8U1iST3PsJOGrqWWXZqfsZa6EcQ8CwL4ao9tbqwXtcLz49bA1gEz6xKuMlEIfG00i7SI4dVkyTL0fUeviLCR2KiDCKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUneWWuZyiHK6LA2aaw_X0T2cHCy2FGgKoGWDH35-chUkbABK-5rNBlEQXze-GbP1XphN2Hxmc3IQ_1ka2oHfvtIHuXuzjUKyniyVlmBv8aJ7MiZkYOPfptYM3-jmTXZjCXsu22xhUzmHk5u-aA_q3gekJAVq9G5D9q_jw5QnzyEtf76lo6aVE2PY3s9i3Tp8koHKiAb9irOZIFRiUkAmpeNJDste9xag0g8q1iWaRzwsVx3Gg8QPV2Gsu5wG_W65YCV3Cl8zYczZhiBUBMyevDOceHRBt7q2JQCXHz34fFnOHfKNVXptgJmTX3Ma4-L1wGMgONe6c7xD0VElC-Uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FdnP3P-SLN8sAZKf5YoS1kcUL5F7RNmmeFN-0gJphcKK5J-w1xQCt2KkilQD1OUZy8Wp8BhnrfnrEEGZf493xk5ILdz8WMflY1A068hVowTfZgWfO2ovtOpdxuhVfafID8B4Gj1dGwwzJ2iVqsVLcOOzM0BLrNPIKBOL7AYWJ0lg9p9E-rDNo7dOGf2GUvkpqf5E80H1LEqrQNoaEw0NqweUQ23bEhKkd5ZayZqKk_OOiAQgWvchi10v3p6kRheWDCyFn7esW_mYh3fnKXGwi2xRn1gnuf8xXo3DGAzT7MQ_rCKIQne-wvU1zkVwPcVfqOStbRorNGDIVCJz6dUXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-Mf2bKdzL-rSrN6k-tcGIczJvQAafITfWhBwhKXqpbjK4xwpvdMI8AEWWbAK9mgOqHpvO5JV7PBR3m_TvPOAYdCL9ZSZ1JJSvCWaBk1Tx0lHQiMqLgRopRrtOcJYcikITT09RXE2laKS2eg5AGm8d6JdGp3AlvoqNaRXXZ9GCB9esLzozKaRGadjJXHWkbJXTSrO-Vj7gmlViK5gLgO2p7S4TP75qhj61AyiGmVlaxgHQ5NpWWk9Fv0HHnhkBIribLdS6AEizi6T70hWQTz73MKKbKSGWkp2F3htxUjjjjiAorGRKFw9zqvs-uyjRaY9kaQtch9QafixU9G4xS73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QoXgPlt0SH2X8hM8zMdS4y5CZ9Ps6f7S8nH5KDOXCjIEOTxoiXfYk77bDMwOCXyYLMujBrl7CWq1a03smL5INucW8avB3Gdv-N58qYKKYKEm2ka__7IoCYYeNe_xPqLqdNkM1zjJ-fsGV3x1BLNWOvvWplBOXOA2byrCyQLks0c1yWDcCAFv9JmIDt6akAnCATVngy3TqYW8oLz9UsdFlOD4fGTdWEam9wghZXmjc91XbjAwRp02S2VTjLngv7coluSlfcfSit2ptOsEMegQdYwyjuTPLn0Mo4iALo4OQM4TwTW7yRe1NLi8vOlRmZQvsT1RHaVFdKndVcHVAd3j-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhIwXqOppfJdcpLPy-5cMto458hp55S-PSVM_8uuIX4uzq85-qjFuHVyDgLn-6iipYsDtjX6OSr0L3gTYBUy2TTG_Aqx9-G85Qxfcef9asfIRFMdm32nTO8_ovFloKUC6PWSQgTZzj7AQmK0fQeZmp7HgVVMW92xp6zvpUibHuBbvuQXp2TRO1txFtNkUc2e-Xr2hV3RNPRhwPFd5TMaEJ-ftQN30k_1BoUrQZSo8cjqFvYO_g3aeIQEaVw4DTXzWTxwZxYjiAbEJPq47XgyBuuFOsGT6qRSRCSeeORxQj1JLYN6zF3lMESvsu9896Cb3Ly2X_l6zwu5LBHmStBqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpRrmSTKsEgbOtrbYSzn3Jn1OdoLa6vj4DkmkghMUsc7dX741vBA-RkLv-BUV7wXJsiQWUnSpB_A4c_8NxTDdHmzASGWqhKwWZ83CFsuIY3DHknUfdzIaKwdwqkQIG1mvHxC7F73Mcme5BvIMvSN8GHIo8gw0dVVsygIuJuBM5OKFqcEP2-WTmOQ1L5VMEMbeS_epnxF5n6YZrd8HTOM72krvUxI0HOwEe15RMGoiCgH5sfNJshpRv3aGTienshzduZ9bnRBQjVzmMRtQoY9xn07RFKSx_pdbJhVTWGmIhuDxZBMxVOQcPVPWqU_z64Q_zwcceijvlRnEJsx4QYxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LoOwRCKoQc9yDjmOeWbe1NZwvJO8YbnsfRbKmqzRtwIQejdTDETCv0tw_gFKH5A8YdW7jQWsfEgArp9TstRqT7WBEngvLxeG8r4j5Eru4edxGofPBAUqT6QHst3UESe8OsijGYeDAPHqrfqHYBN88lZ7IuIqUzAMKyQNTm4nE-Bv0rkvo81TByqB1vNCeJqIZwTt21OiGEJCntoMy_PKSGKYyDcS_ZTtX_iDmRHIqkBtQx-JXFOdL2vF662lGhTTHWi_f6kUH0Sxnjg08P2y5iHY0M6YJ0OxR2vPxWAP1Zz6FLAOgHyT6vv58kxYMPatcN6n59SVUeJsG1zU89V21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFSzBfD2rbMrbRcVH9aWKJnfd_y-_psp7rPoNRm95XOPm9t7p8-UuXWi1CIjh4Iz8yO8KFjzrlEoKFW_jdKsgQf9XdgQJFmSN1Tzi9is2K9PSORjSy5Z0K2pVWlLE6giLCdzRKKn1b9N_4ANdEXTNGXuvaBtgJL2k2kCQ1BSDGAgbxlyXQ5tIonNfPePA1bBaIPQ7cFNpGZkoxp4WcDbHu_lSrBhG0VAZ5mRPDv82oDrMlkpdlteZdsMxzivLmoUfANeLH2KZ2ey0813kUo59X8YEhWe4y2WbLKYULBy99LSA2dYE3wEALCkBQknd2BNZEy3NgHgnnZHRyMlYDitmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
