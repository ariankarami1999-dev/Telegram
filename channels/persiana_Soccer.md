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
<img src="https://cdn4.telesco.pe/file/fqXI3Xj7SOQHnyhjSsW8rji3UjtoEk-wYlTSRQFMgSxRn_89B3UbHcMhDlQ5SOWR7Y2O446awa-LFPrazbBddvbuWPggNReTDCA-YUIM-Wp7PIB9avLc7mGs5QBCG47UtHrByTm2OdJliTu5FOH3zvjgJKM3ity7GRwOo4OF3sBM4jtD30G5am3IRk6kSXUFmpwPVAwkLBC-TCJn553PFPrE1RUbVimNn1nJU-yBrrv4IxX34O4h_7EmvmGWhG0qUVH_nYLtdqrTqQ-Y0fclfj8AkquO-7BMe9G5e5HYsKrWoEGtL42BviWfxf0WyggkxF2OXNr_RjKEyDqa6ZgGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 467K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 03:41:54</div>
<hr>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwkNtBgB6UJPdyEFUzox8kj6oI_TMRqv6B67L6nKUgNdocwHlCJglWoKN7t3ZpZgoL9ILcD8ATqusXFpqy0I_BgEJ_AzRwHExuPVlAPQ195cyIH6BPu2B6cqtdsky8ZSMLwCiUndqt7IpgcfEz5FMXFXa6Zyh-iNE3lp6WUKIuIzUjvbFxHAa5WPfu9I14KBqZGD6aAf6lvtcvSIFL6Yb84WtcSU__euZN-IHvUY9bPAViYBqDJWEOHRY1uRgKzN4MD_07vOR-_qjwx7ib4m2_55Uto-z9TJKO2hu-hFomfbBAteZKItdxxgv-p4kVcCv2mv6QFnK0zZ5JtvTbZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8PprnrHuUj6P1Qunh8ppUTWApMSOHpzLKuAYrTMjcFwskvJjqgGFG_3DN6VaFKGF1AM48s9dqnjc_vpWID9NXH8vnrQFjnABOkmnPkmmjqWmxWlYnuO_cZlWo9VIQRtOVIhLP0pFX1SDNmgGikKz8ggwxia6XeF9MtGKLmKbCtVTbh-lsBWNJRrUaUibnDyNjurBlnyJ4bSSpmfT5WUgqlzC9iaZ_Ya42g415XFTs6iKR7XU-lLNDag6ssfKJjvyY758j15DtIy0J1mxnk3XP-li8wqa1pbe3bea-JHeeXg9idgVEelQvyZ3Xm9lrrIOglP-W49PI3VxM1T10YXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30216">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx_u_xkDBvMN6Qck0kSnNxO8jyuqMRJ68Ppz5Hp0D_YkbRBW1Fm7kFtLJCO3E7iOcl5L6LY-li1WXirdikPQ2lTB_UstQdQxeSxgOJV9Z6Ue8g5_g5V4aVLptODIWYdPEGSfGLyIra9GDmBFWtqtATNSbFkuTNwq4vbn84XdSoz7ZvI7zV_oWUGKhbMcBmvtKujbvZPEU1aauOwaqBweS1MyOhlgfX4OLczneDBXxp7I4rSrz_1aNRJXiO8ewyfcDftuVTqYlt0KDL-md34nE1LTBl1b1o3RDxpLkvJGD0TG5zfMq8-0CbkUbwDh-5oSgnLUH5WkrLyp35rHrxKw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✖️
🤩
🤩
🤩
کش‌بک جبران خسارت
ویژه پیش بینی های ناموفق در کازینو و کازینو زنده
💰
تا
🤩
🤩
🤩
کش‌بک جبران خسارت کازینو
،
قابل دریافت برای واریزی‌های
5,000,000 ریال به بالا
✍️
کاربران گرامی، در صورت باخت واریزی در بخش کازینو و کازینو زنده می‌توانید بخشی از مبلغ واریزی خود را در قالب کش‌بک جبران خسارت دریافت کنید.
⚠️
برای واریزی‌های
🤩
🤩
ساعت گذشته که در کازینو یا کازینو زنده از دست داده‌اید، می‌توانید از طریق پشتیبانی زنده درخواست کش‌بک خود را ثبت نمایید.
⏲
برای استفاده از این آفر باید حداقل
🤩
🤩
ساعت از آخرین برداشت شما گذشته باشد.
🎊
با کازینو یک‌ بت‌ برنده‌ی بعدی ‌شما باشید!
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
P30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/30216" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5iOohwdnf-G_mYVgJRBpgJaUPLDFsIaYS1Z6Fln5P-_hPiAsbXJVAJLs_AyZrS0H0rgkm9H2g69-are2oOSRCU_GTSitu76yQXRsfnrKq8m1VtyFPYmv2acCWiinKVxJmI5Im87nGSenY8lzfQe7686OJfZCjHEtUHikad2uAKzDl4quXsswYJ_ZSnswb74u3pb1YeYFgtYaYXEru75UUJGCnPVnwGsvR9Egigg4A9EOOXXinf2Ftktr5oF4sSssvdhzl0QYFPLcSeV_JkMX_opRfKFVEJlxMJj_kMUG_nHVShaimsDCiBxMESORq_ss4zBsTPQKrk-cmABTFdE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8W1VLChaLGrKD2_Y5sLsL9jaZnfqcZjvNTRjK331rjw7xZ2jDEm6DdlKk00fPgjyr0KpjaI9TFE8GuIexIDNKy28_hAfcAw-c636oECLjQgJO37K0KNSIOFtcS9NKRqYjWHqkacIG2btyaLu6ZMSoaUN2OGy1HQxp-Vkv0xXC8GvIynLMSHCNO2F6sIND8kmTtVDwvCD3e1Aa_pylEth7n21DgI7KnBDW4Ri_v4C16lk3wwO4SEsX65Hr3p_pVomzf0KIYQ7ybQKK_qXIeaZlK6h0rJlHunrZMAmwvV8I9d2Ffiiagmvge_7DCJumS5lM53E-n2CDcA-HxVXQC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Iu2H3gnLgLov0a13u6c5tj7mjyWr7bdfAK6Aud92uGMACWy3h-uLB0qt1zF4eQSiJwTuVd5ojGehdlehlfQyP-QPFwpV8pqu9BJeWSjFwUNAFgplhRhn5g5NLm9SuQq2ZOBN-1PuU8bKaFTPIKEnE4CpVm413TWeNH4HcaJS5dwYG-MZrIIIHTdyhE2Y2LQZxJQvIe889mYQ3wdlHXp4RUoSqZtauz-gewslgJKl5MchIQFvU2dGLbBgGCenJvriDmFKgfGenUKck8SPmzskHSz56m29p78HBIfnVyebv6Kr0tIGMT4dkP3T_dkBEDzupFA7YuJWWrlhlwuTpStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxQ0ZYkgijpvYN8gQq2KMMgheJAVIacQnOHGvIzR2f8pB6OPVsiTf7RmZLvZy3bnqexHmT57nI99DhEBAZwJtoAqWhZeQY-MTacgy646ybdcAoXP1CCVyNxOQ8wFeENmCc3Up-rdXggmjUOMYMDf0ITfEQBgPgBmiiGrwgo4vFIuFgYMISuBkK-gkXFNRn41f0MjDOOGuzU4oW2gQV8M9SywU4SYOlONa4zpzKDXvfZNDfWEPkQrv0RgusneNxia5n0fg5BVfpMte2OSVtfd-f6ziCIV7sp-4lO5jfdZ06VNcc0ST8H00YllmHYOp3STe8Mjg0l5igXYBPB8lN7xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3VIk_G8_hRdrLsSxifKCP20kfQHR87QY7zwgj5VH7zMd9F0tR241Ieej8Y991IG--HPoela74S1Lm9Q9CPaqHH0_ZsFGDEvklvVwOKv2hlmR0ANxGKJcYnQwltyu0lO3BaNb4El6H5y6OSeADH5ZgsiSZzRr4coo5jXZ5bTWWwIbt4HaYoF1h4e-VHbVIFzHMLwvtz0tRBtm4R0XrbMo_wbwpjdNrCnfYbHXlycC6b8lcnx9Un5E57KG5Pu1SbQ9x7H3N3tn0jHOX3zPKf7Zfu8R5yVIgXLydRabvPXihUtWuJo9ADr795_8XlSk0I2_t7PD_KwZd2nL02FkfAnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8btCncxKCNox4f0KI-PrgY25AdwLNYSsDv65-13AesDAvlkrbb9RFpwyvNIMIzQg9kMCrq-UW-E1o-TrDmZzKiARMVAzA8lL5Jr-iy29lD0xbPz-iMgkATiW6pRTkM7uXAtLYkvA6xIjDUymdUS40T_Ho1cCZ9nJ7ulcS2jDjGeVK7LKVYuWS26SlmXoM27-Q33_tIEFHSGTgO2Jr8gZXqwHZDhmE9xNgIKTh-FKFlENpGBRW_70eFBb-YIx0sVZhHMXipYEWFlTA_FsUbdCsdfPVajZtj_YUga-hJ4t-BwJUAjCy9armCgbb-CkW9fvqQuBbmy-NZvsOMWV-0f1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-w7hhQDVdhBLZHm7UGae26nYi5nZySGv6vsl1uxoEYWFI9F7zTmHlp2mw3V0z2rUN5gToFNrP3eM0RGuvema8WlcpaXEXwMQX2tj-DS1EIV2D_xfLuvBwFuCVZ4Mk77nCilAeWW6HHQZEWezsHry32Yg7H0JH8gBaIutjq0kFd9iRSmIK46PwXymenweMEWWzuLTG3NsWM7qRKUp-CY_cYJPKN5w1RWVJXOGof2Svp5iK3kid6g5g7f_KSzXzXPDU3U_McDh4aOeE2WLg1x4IynFV3PFSKHcU0ab35q7YHOBQEfXy0wRdgnZm55BXI1FOx0WOOTncxv2yAFSSipqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtO2v2p7Uebg_UYOnR8UabkAAX3YUD8S7mlV9lV0EtA5fKn7QHARBhiIw3BkfBXOS-ZPP2I0zQ0gsfYoP8WHd7LYKzQw1kXkYEa0gkDykDT3hznOcZs5razZKX0Vx2S9mfaTPk2kM3NRWy08sTZQ3lvx_7yJ158PqtQnWme3L5AA4baU4DL4aDX59XJo7UD6--WvQVLXor4S64wxMPgC2sCFBb_M0VXI51JS7pUoZ8k8ZJTVVHeyY8CGksThd3myPXkhELqgUJZvcbsR-3pUGu9-PXqJe-OwufCxJdQOMrQdQN9KGY5DxZ1TOyIYksBqEg_gpCQFFIZ8XYT_7dW9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYbtS3UldyLddT29fJo01lge9y101HQOp2yicoBQrGqsEgFKYROi-nMuw1IobfXj40GFuNsHkc3_VdhYUg5knqYtyCw-NEh93HHPAY8JOvm7fdxLDcmVyy3OeALGcf98pTUoxYHSjjdHMlFkBGvSy-U4y-HQ1zJe00g1kkbNV2zlfzRuuIvaoprCR4M-fM_KhhEL7F5-MXATvvLiakOumwtfYtmCW-RUGMrQ7VWqj4cPQizSx9GnyOHNLmeIKcLVKQi0gIPhmI1dX7QfSKarETaYSv1kSHW1hiap6Hk34DoA8dSib6SkZgEsQnqM_yw-EzrR92nZZ4apY4W9svd9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcRZ01_-A_mWhOe6BeKD8ZH1D2u82vXhTTXBmSfy4yHBB0tHBzuz-CkOdrj9cAWWAQ2HvzYogT_KXw22SdyoEVsARU08soFhKtSNlSlUYhYzbSd6zFC0S5NCS764gNxUoZwf6DNJbI-7LS7qmrASCXgFfcXjyn6sXyyl0K934GdArgK7H8xvQpU4LATd4Wn_qkmicg8tDQiCSfsPsrJLA_8dm-REMugrxZk1XdXxlSjiGNfiZ6mIc31XQ9ExueyIS1INILKHnYWGFBNgztzR9csWD-HXzkJi770-qnwY5gEBQgORBTzSDend1sY6TUQ4iBVxMMd6I7z_vVrWDaKmgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xtj-WChOLkjpSQVfGMxhf8-kyq7R_7FTSoY-xtNVdcKjtpoQLtaIntuX_JyUga2kd_Ou1HHReLDJIAT2yjI9YEkTjsCjly8r-wkVSpp6wIIAYNYr1e2eeYyvMDKeR3OhJ45vLabB7OpO0z0I8FYoU3XhCXruyAwEHNGpxce-n-DgBUmaPg9twMbbbKCIC8c7hopYpwUGnf6nAix_gmKIGn9PX4i4hz3pmmZl5QCOdNVuuycYNtnsok5DA_TxRvYce_LTcaO9g2GTivLTSHzYayMAQ0Da_DeC_o170hFn4Dwkras2bf1QyQJlo8SDzN7MMZArqN4RAhfMG16kF8zJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP4tzjEqchkSgHeCY4GxKtTiVyn5s4s7b7Y5wTiOkC7Q_mbZ3d3wVwGyGzIcNIM7TWWy58O-oFe3dsMWECMfO_4LUmbmfB9lOdKIEtHJ4H6yPKmJD6cx_3xtSi3tur3D2fccUMiugaoHWGaq_4H9e2t02QqKwgrR6l-3LQOANd_-e0hFrUaAAyuJJqFDJp3eU-dBDPD071UICU5umzmofNNXTz-qrUY4sU0A_qzY9R1GmU-cNEZv20ptw7WIgtl53p8pbfheST4_2WsHjq0krjqv2_5JIfu1CQkMSpRJzKyaSaYuvLGmPKbQ8HD8ehXR8_kbAHe_pzF3zfBFjtqJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loZszLfcRxgcq8-rWrHFsGkGBAt69RpwqVv2ezvUcLn9CFoYrWtO0LXHCryJP47HSZMy9Tj27hEGG3yncmMCtV3aPR1Xiho-CSQp_Xc4wX3z6ar5N45h6JXxGS3XNn_bV6dAPOWouH1oWrlX7apCWw0b68WKyIOGdaYyEn12v792Kuu3q5tb3IyUixT7f0lM-wDK1VPHllPHjlpw11XXSQoN6yfPE2pqf_UueJiF1F8V4JUR7OBul3wPsBENFwzSUjzJKPmR54Xg1BJmWl2VhOEHCsDMELJQVnd_rMHm2f4GnSN0CHHdZEdKkIPz9q4ux8lNxgE_QBMJkvXLZxhEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
‼️
طوفان یک بت ویژه درگاه های کریپتو (ارز های دیجیتال )
💰
🤩
🤩
🤩
فری‌بت ورزشی ویژه واریز از تمامی درگاه های کریپتو
🚀
برای تمامی واریزهای انجام‌شده از طریق
🤩
Fulgur Pay
🤩
کریپتوباکس
🤩
UWALET TRx
🤩
UWALET USDT
🤩
می‌توانید معادل
🤩
🤩
🤩
مبلغ واریزی خود را به‌صورت فری‌بت ورزشی دریافت کنید
.
💥
🤩
🤩
🤩
🤩
هدیه ورزشی ویژه اولین واریز
💥
🤩
🤩
🤩
فریبت رایگان ویژه واریز از طریق درگاه ریالی
💥
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💬
بلافاصله پس از شارژ حساب کاربری از پشتیبانی زنده درخواست نمایید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30197" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwFQDyfHsqO_ncFA0QaJ9d1v4caNwR0ZkNabLV5bYFq7YEeqTLSpmqw15uG1hZOMLGxF7y9YlEoY2AWIXyikLiguzFbCJy3-Fh3M00emzUP3TgyfZahN3jJXKWW4_b8vcJy9NSasXi8K4WiUmduReleXDEzHNZzPdLyPX-xxQv_0NABHSBg-ghN72yO90yCwQTOqevfdlApFyY8MBx_U-A4WfKpcD025I2Oz3mu3p4ZfCgD_DwBoLE2iNa4wMbugTcASAdw9vtpED5u4ORV4ot0xamBwvHwDqxrThC0aNNO9ktxY_yCurUKaKxR1uWNRbnfgNeW9A1pyw6h5U8r4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_9ZbLJYlGJXiYl_JIjrC6qlIBAO3rY2jHLQHjgfS3INZzos6YLQaQoIImqBHPt-JJIVGikAITZ6Bmm682a4aTi8xD6jsr6tqejv6M_eodjwK3rrseExI5uXmTwnOvMVwGMLntEHaRTXR-7LnEISuzIW7iQc9muhfdgWvRKKL2cVgREqWsDfbNrIYegwtSp7B04nknDGvNkKmKGNAwTA-1Ldzn5HO3k0V6n2HrKb504jNPL7dUy9DGSUHUx-lIxJFD8CHVfU3DBM88OLAhe3R8VtZ3bL1r_F1JLvyJmBXOVMWnlbTPz35oZ_r3vsTI5zQjf_1ZU0FDczmC_6qWZSaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSidsRWzD_HDsiqzSUsUHcBOvQBLKm4eC3tdlDHrwj2uFXDvBsMQKgA4ARFL4njlYd7WaGiuCgGYqxSbB40vn5IDYiCYp5EJ33GS1VVruWuiCKi9BDVKSw7uPJrJewct5voWKeZt4DcOG1oAjx-necjO_E6QbWHEDfRIry7SG5dqd9n8NcIeEf8nLhG3na7RTpCEWH6TWe7cXkpdyMcAQGFWl8NDwRJZUQT9T1tg4122jnMkyufcIC7KDjmH5RHuD3R1qs2oqs69LZlkx5kv-OpSZqUJufI2JsganAEcPCuob4LUudxxHvwWCu37ejSk8g6L4WF166IcZJL_-n1rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9jwnouI5mnW1Tn2VFZlWwt-Lr93cITN5RGdqFwFTmN212cYnI1yzE6IkKmIwRvDQh3lCVFOJC68b4b0_S8ayub4WJfhQexz-MoD9mm4C9-28vERVLQlXNFOEAJYqSInzDd7s5Wkbshb1EBVmdLg0D9ZD5DULVNmrpzwUiyQvHT2EdFTiDFLNXFuzp9JtzfCdHVK7DIR05LTDAoOlfhUHKoE930qD5Q7V_BQgifq241THzL3UTgP70gb0bijgcJKU1VU4Kb2q9-gT5EJbu_B8u7-z60r7hM5WDLJOIUeXCkYl2PaIXGh_Y_-6c5jTFSvkGGvH5VE9YLyAAdF7ONuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRtmJXyg-J0kL3i2lLPYf_sBfftWvn2XB7fUWJaCjYYNaLf74lsn0R-BRN2fy04H4xWOpuM9AozA_nk0QGE_AG1L_q4vF97y2rj4QsZM2XboTvU_ySFVNV_vXs3YhWQaCrS67K2X7H62-9zoxyfrsRktkqCMB1YZl3Rgh3TxybqeFBi1WK4HKvDu6Pp3zSSiiPrmqM2Ammy3Gd-PKAcw6SoOujk8wPbTHZuvZ2Sy5-rg5N6NNhrMTtUKLWc1F-Itp743hzZvKVLy_gmWO8TgXnIRt3_GJUpu_F3KKZbMrWm3gOSBGGnrrco2utQ4QI_i43PDwPqLAWS3wR9tnFzo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MvFYwPizY575iFaJyV8-gDFKby8SmFLgmh4SKao82xu_Bui6tD_OWlWRrHDZea70PI506c9Vj81rS6nvD7gnyJqriyfIofdUpoxtxtHh-4L_zQBMtrmJZEKorh6TGUlGygbRg1lTfsIqHPn6RT1_Ijwasr9_y1xNWvr3Hd0ZOuQySZF1j1wdKxJunQbBcHFBKnOr4_IWRgffWXWMUIsk3RQM6GtM2IMLcQrxCzSPue_IXXUy555lNPSGucocJuPFqmN-gbgN5oz1fdaM-9Fs0FFD6_wLZ_EH1VIyV2u5dgaDzYNozus2I8SdEdVy967foL34ql2DI5EZJ54ZG_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKMC3d_94C12Z8im3bseEh02OTeGhI6tMGSJzDs12rJm0ES4O5I6r2KLv30Whzcc7yru2KnJOVyXGLE_2Ca5WLMU2roCcAIx74fQwLzGeqG-2f5mlXXqXD1p2nwf7XNFqbZcCLmna8t5INKpEeukrnryCfz45XdWXNPTGKHFyTOBo6p0nL5vH3MqI-MTkHn9G5jOaxGDYOqGyHsWCUVZGoMHld1Br23JGtVeVKL9elB-8fweqbGXyZ_7xonq5YNODJFzbys_F3qLQvvn4EPJM1sYrfgCJUwUuGdn95nMnJ6Y8nTb7SjQK3uMGBRATkK4IP9e2nlAxOUyngXiun1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZUlfQNNhdhCbNoiDqcVC0b5MFMXG2XSOfc3RFOxSsgmhGsIcvj-DAdjsCy4HeMhDTr7wQDGMSSeac1uj0Skf2ANVXl2QmL4V0gLc_EucBlB2xT9CZg8WT2a3BwfK-dP8gIllknst9c0M0iUvGx1CzMft59WfN5UEYZvqAMjxw6_Cnroa4VlkHOXxVFb8513Q3AMqnvsy4Z3hK3lLuHwVgmI1Iru-vJ3Akx2lmOl662zig0KQ7EnjfNB3APhwjt0yGPaiS7RCxNJJvTxvwY4k6nSTRQrDK8iBArnBxIycMfqss9vKTgU9qpB6XAjAIVg3mNwjN7AmGYUSLYVqL6Skw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_WZr3WskXAV8ZhCbDrc8jQgkdaOjEJaURJOHafvK7KYDiv0PA7YirTjDaw1U_dCJ7vOKEN6a7fzpk0vVZxl1QFkkEVYsGjF2gG_rRmlTgNTnBMmJ86woZ6w7N426etn3a0p1ZyQAskkPimViBm5CM2U5ynUwt2-9ABrhR7e15Tjw-CNZpWX8swtK5e4BV8aNI079ZSVjWpjckWqgo0Wzw_-B24nql_oHlblQCnuEFk5uoR1ZtYFlHNYxi-E9Wg1VgiOkkZNuKx5Mih6trfCAzB7Kt9xRWfjKECmyHqgwUtu4tneCvft8IjZe996QSUrHMMUSDqr7E3EQ8bv-uczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVeZGgusF-PBdZaTYkSEP2EnrtKwQUgUqSQ_8fBGZwFSVhyicXcoOchDiKunlS-gh2EMzorE6wU_UVw61u3zKL4IxQk7-yjmUT1tVyUfe7p6tP-6O8nDHZs9MwCUfT5bnRNa8FiNVemKG24p7nxRNpl-2q33Dyo_LHBv8lbk_QnyCX3d5v3EfYRRWW0Rx96ZN5x2RLtwyzbEBBqVhWwM14k7vaRWrENWXksHBgrSbcNbji0Q8dsUthn85hpYmk1T2QA93tanjkGtBykiMLDvNMZhynq4R5KdrQVJ89E8gU3XPzEx4QWvZmiZrQg1gLK_6Kp5uNwjHa3NFKF83hEUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVmC5RDc0LiVQyYX49cbxsPfRxIhac1UoGhfZ1svOkn-MaiZE2lRBL9epIEzLr8EITcXOQ2C-uV7SLomEq8x-dIP2FJmhgz7XUVb9GyKoxF_jXaP1OC9Zarw-IE2WqfZ8j7OMcrHM4fAGts_6cj0GHqWxRC38giwixzMNKs6WE-aiMi6o20nlflDBKAG45TCj8Az6DT_B9jRsPQ4xslBodrSguYDnq1tJunCSRfnWw9Y1kzr-aC751yYWCh4UIoy_pd0bfGQ1_zxoaBTWfN0K5TkglE1RSADUonKAcULfkPUI9T7VCbvmGV99jls_N6goOiG8DuZ0H_lSwiRbeqftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4ME-oMSII2MxiVVWMtUa1lGsFAANbH9ptZZrRn8O9m7tojFyoDtmwisMkw1AHvUodRJLW93srg_ebTWcpWU2GHRVwlkazeKEa624BOFj4FrcU0ab5Bg4ikohFlVju5CZzjCQI5Wq2Ifbw5LtitZymnOfjyUGatscJxSi7ILxFNtp3I09OVLLz_1BdiaWPWSrsOFwPpANSfZGpvKcKpGtmpsrTwhYJ7W-O_dqg9Fw_LnT2PYtG4EKehvdFVMW8Oo85phzcl_3OQyPPQa3ToJUGZ3pVpdEAN-LU7BLdYlF7__gjo2qkpziNln0qXaBiyW9iDM4T6suRN4zG1eeRDymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9om5WKuR9cjaFvliULWxu-ackRGUMBEu3fzRMNJv3jUgBCrebKGVzpX7oC0-NjxSOXJi2ZmfIMKBort62udDU-h9RtE1Wg95Kf6ZV3SeSVH5i8q4kETjBb8i6_3LM44F-epu09ITYj3zRYsSrfQ2X_3xrmrepe6s28Opm1nYnTCLccJgCgVk5EEp4NIjyXRBFlXhFE_v4IEbLxITC4BlKOdjLM6ZwcTKwZ8Vi1La6MlxFNTGb5aitHU5yd96fd3V_CpizkTWmFK4nVCdRzh7MPouCx2kFcRdKnJ_R2CTV5jxOCycXc-5H_NLZFOR9VOmpqq0OUMf707RZBxQInA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwRud_S5v4puuIlo7fxvf3ZE7FbWjWel9rBJ0VX08rR-4CQQgla5CJFTXuOcVujzv2h4Eu1whZATIAndnUcWwfCJWPLUwbPQCVmIibuSj7QCiR1YDP-feaG6bhPGb013Wz4tP3Nr1rXkMJLMPHko_EFp5UQz4iRDvyc11718oeFU59Ho-ZfdgYYJKh9nRnZ3XQD4eHDaITfJW012-l5Lt0jRyYD4semkewrvedsSREeMeNVokrTVxmNzlfW00M_2RKFDryUX65whdgbkf0IyCkQSIfwc3svj0JrSUjlW-S5_m6GguXwKllanRJQDXylwhd3cefoN4PUPmExIGTStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qighfA2dSW9FiiwDN1N0xdyXR_U5hXSjpktW67k8Qg4WRdsWumcCAZIQld2NlRN48RbSL42y3G9N6jXh5FA9HQVl0pKv5-2LpBf5o8y08evB0vjzrGugj0uVUlJqah4DDrLPLA0rTnJHMJoAgM0sQ0AYepfnrNPne07zGVt2iOurQGJ_JUsAoazNUyPLbbzDEkELgUqF3Q7QRdiu8zlits0jcb-MnqpmrcnPunLkkj-6mCRn70CQrZbJV0wVNENhHCd-x4tHoy6NObU69fTOOd0F4wV_apXq84XelohCWxDDroV2dvaO9QxjBTDyLNUk1yLpRltRvUjUp3W4RWHwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/driLqOkT1g6RSqdPZOO7njs-RsbNrmEZ8q8ETRTF0NPr6_HhnAKOQ6riNSeJc-wNnZ8KYA8cVU72ZM5YnC8yaALufQA2c4iKj7OqWTpjmSJ1__ZUZqXP6XQztHFvWD_xG5g__7sphZ5CANPgEcAZpOzm1D074ZmbeaI-_zjSW0tbznpexvezQONTkvrNf7VnMPxfzRACNXQH0P0Wb-JtCaxpkouC1zVD2irpLFrKrOCWbnkI5pr-KaSluR5XnNgjlt2w117EOXbX1QIdBMAF1nu0V58XTS687Qa1Fs-40I2vbMjYm7DvLr7kBNsFZDVUt9bjxHzuMgvnSfaPmNJaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🫰
لذت بازی های کازینو با 100% هدیه خوش‌آمدگویی تا سقف 100 میلیون ریال
🎮
بیش از 5000 هزار بازی کازینو زنده و اسلات
💲
🤩
🤩
🤩
فریبت ویژه واریز با درگاه های کریپتو
⭐️
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💱
🤩
🤩
🤩
کشبک اسلات ماشین و کازینو زنده بدون سقف
🛎
گردونه شانس یک بت با هدایای نفیس
🪀
هر روز تا 180 فری اسپین (چرخش رایگان) در یک بت
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30173" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWneZox1XSVjfzs2o-9oEqdomOGgQPxF7LBsPnxxUbJ9GhYZ_C-fLzDqwvFIf4z5cVl4UAN8HNboZk0fclWuiSevUSwA5S9kIBKbsAsLxOure3xtVkQg9R9dEEgeVLmZeT3pSxVrtknqE_YSC2zz-gbyC6XuyzNNpdJ-7QMwHrBE9ZQW_wMG3GRF-JlsB-jSIoWSZJNskHcAqWAvUeHZA8pS4ii71ioo5BrTaJOmEn54ZGd-TR6Nj64Mj-85T1aLoHgdqAyg3aRRi0cNeQs_luN5gRpKEFd_uKZjCQ_1OJqc5Cv6xhn5sCAGmGMdGK_KLbOhiOl5m_tY0k_qvtRjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpV-59mAU-tBR7DXe_fDD5gPxUnpnKHv-xNV4Ona5l0BCtyUm7QxhVRG8uoaNhC2g6dO6V6VOm_7heIiB0uaVsiiGl-cw6r-4D90eH07mIDwem2Y3svG86_d90QgOIM6VAYxOvS6vgEjq8b9_Qh1CxzNgLoRWxU7Rn0Oxwlfncoufwb7KVfvcbarQM_IuDWhxnzv9GW527oKqWMvPkOZyuVLa6HWJy3pwDUwGhQBghNmvGJrnhndUWDylvAV06TZgjS6s9T9tpiMil0P_FKqATqePqMbTYHUmKI4QzkoZzyoQY51CY9MeoRPnSBvOPyWjVEqi0NG8jS50gw0Q0iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyXduN1jZ1gv5DO_XnC6Asbg-WCiR4FHlwBJ7ReuaxgCrRbPsRvx4cb5NIrwY-23tzUq9m2FUfAQ-3hrDSsQE4hQCuHrKfz8oQZlHQAQOq9pf41IrxzvYYowDr4Ok3crJfqPwgultPKD6Bv7LU8MkPtoDgcC1P4Hm_1dszbAsQndpgeidaR-83mT0FYWyB5m_JvpJcsWtet22HlINsx0CbeolaEsqZsZnh8v8fvXf7bFcVZ9ifA3IaEziM178uDER0nCK10ic9_BZWwhe8_HVi_MZgvWlpt3sgZX_PLKqtbkMQcb1yFIgpCkgg1jMRCe2OP0yh4xSupsluyzz_wkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-2m8YAG2wwOc2clum9yHjXn5Qil6NmBKpIUlsKt7rIbSTkQuXitmrd48Wjz7QPy1zPkzXcn0UxayUdA2UwNAsxHzS8KV2eC9kHQ-q6xLK2F5HFfOeehb4fjnN4EK7SiSq2_b2LiBS9JZW5wBQJDCzgRVVtuDsrJUIioYNwzlW9Y9YY-aNh7ZImLVF_z1RTmV_qFp8NvmmmN1vxX_BYLzxN5SqpraK6SYFeN-skQ9kcrTixI-4wjTsPpN1GM1KmnkJNuifyZZGQdKTsORTYX8EsS0IusdAlYunHa-DO8-Ihq7U07sGrEFuAm6ln8Ah0lTrRI_iRVjRVps8Lk6erd8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUB6Do67XHhluEMILsyxCWDBvv49GgL9butaw_7X0lLxht4An8XMo1UnZGADNdprJqIHdft4xq0Dr1fXU3edml7pbkBdDRPGY8Ln98KWPy4X20QNrmNGBrtDNgAjLv1YO_pESXFajPoq1NkMhJwSxboYquNheH5LyH_qGsvmX472RPSMR_P0SVRpVQ4ZrgJWCxBxTTpVGmTYUK-HMo1O5oMIbdgUtZ5tkqau84ASugk0huNrPaqOGaENuhh_DrvKFkAKe_OiHVIef0lwzsmX6__-A9yrW_kJvCUJjm2WP42Is6nSLB80F8Gsq-mRzG87GW33yZ4MXDno8KIs5kWVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=U8To5y52ETsrMMOAt8aYE7t9ffVa_yiFoshyx_j2kF0eeBCRFz8gZ0sJJD-DAKU-qfCaEhsksO95oQ5pJsDOwz_WQp-EOkmGe5Tly0cemWF6Sbpj58OzhfgdNsSc-RXXlME3s-hDBXI3lXEeeVaQ5eJgRx2P1kLF_CH1SMejF1YCLwlGhlQ4cn_NwcCarfwBim2LcCUt2ljYO7EXcEXrG2OdvatKa29GLRC_z9n3cXmp7vu1Ag-anZRrKHzEsL6NhW0XCLvmdfVRyYy0vVZbPPrytPDC2OLbopCPcy-jzCkk_FT1rP9rogzaatI2fKNCKFYnuPVaxYQNs-r0_WcvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=U8To5y52ETsrMMOAt8aYE7t9ffVa_yiFoshyx_j2kF0eeBCRFz8gZ0sJJD-DAKU-qfCaEhsksO95oQ5pJsDOwz_WQp-EOkmGe5Tly0cemWF6Sbpj58OzhfgdNsSc-RXXlME3s-hDBXI3lXEeeVaQ5eJgRx2P1kLF_CH1SMejF1YCLwlGhlQ4cn_NwcCarfwBim2LcCUt2ljYO7EXcEXrG2OdvatKa29GLRC_z9n3cXmp7vu1Ag-anZRrKHzEsL6NhW0XCLvmdfVRyYy0vVZbPPrytPDC2OLbopCPcy-jzCkk_FT1rP9rogzaatI2fKNCKFYnuPVaxYQNs-r0_WcvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNCsoB0DaETExe7zvgA2Fu5jzxlgwdTbSctVbG5eURmUNwUKqGR435mu4JesV3JwXhB5BgWq35THdufBwHh8zDcevWatTaMxdLld6WhSUbT-uQfc83iOQcGaeI7CNvt1Ff6GOt6kpSyYBaMYGnMn5bO9BaczO7vPbHyk057sxel9DXUFZhngIxvJgwgzzcVEC5x7yNvcavlxwARZDKyvqMgMPWEOIXsWjji8Q8x3vccompAXvEhNuIHyTN2ScpIZDCUdplvOtsU9RDH-Xqec8O00t9B01FYFkFbpGxN0DcMNYtIYr5dNVMaSyKUyD33Rv0mNPpiRXqyo9EZBk2XIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=NTgTBjFu7wRhI3WevLFvwtSrNFPW49h-EaaJf0rPh34sE3nW3Kgm867oSDiYT_QbLDTXQ4rw1AZcBOe7ACxrHqoF-qP3BzLF0694Jt7JbQk87mgZnvM1I7H2Qi6pkrqY0fbVnROIPH57SHb2ykoJRUrs9keKHoTHkVZj9KqqID1tPxX8w46iohlrdbquEBHmonipHPiKIDXRZiB5RFG-7-G_p-_3_HpvJDYdmiCraydfK5QDew3mdnriBJlAgQeDa77yPtLgr328gBd-M1VM48740pqxXFOPYSJ5sxiIrgVyZiVYeMCMsG9Pw1-AM_PRxg0d9tJtPRDH3GqWqpFeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=NTgTBjFu7wRhI3WevLFvwtSrNFPW49h-EaaJf0rPh34sE3nW3Kgm867oSDiYT_QbLDTXQ4rw1AZcBOe7ACxrHqoF-qP3BzLF0694Jt7JbQk87mgZnvM1I7H2Qi6pkrqY0fbVnROIPH57SHb2ykoJRUrs9keKHoTHkVZj9KqqID1tPxX8w46iohlrdbquEBHmonipHPiKIDXRZiB5RFG-7-G_p-_3_HpvJDYdmiCraydfK5QDew3mdnriBJlAgQeDa77yPtLgr328gBd-M1VM48740pqxXFOPYSJ5sxiIrgVyZiVYeMCMsG9Pw1-AM_PRxg0d9tJtPRDH3GqWqpFeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXMYXPY48l5S8Oq24Ci_7R0bVC9uNHDqeJsBS1VRsd-NVfdkP435hAWAgBFk_5Q3CzviUEC_kCFrmOdAcvRLk-maF2OyOZzy_ZKSm1sJIiBwMNF2g3VGZIZX3eFHEfr7JSk6lVFw7vHox-QQ1omz2LQKxdXr-oCzwT6OR5c0Y9_GLoGX9h6HiRUHXOI8orVz7wU7GRsm77dBvuhDXCrwV9TnP1DbUp_2msMBinZsmx9YLuPaD_DomB4FlhGokff83nc8b3dbkKV7w718xu3qdFk5siLeFzivB31QqVSn6a0lLPr41mjbv3Q4i-hM3fh86F0j6VCvJB5p-BPAqgLbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKMqrhgiKAL5QssyU4rrhJhGS-YS6hJqppreCLirM7-UPjVLJbwPKkkrVSDlAhR3WLkIUtt8JDAa40ZYDfRTP0K3yNzgQrtm8nnyPfgzpqNhwtWQhoLDiCCOPykBrD8S2y0KnV5hxplvada8v3qnOpib5cCpIosAgauqD8iGrGHc-EaKOVz8Mpr5ykTtcczkWZAPjhNBZT45vO-GEdCPy7unL1y1_vNLEkR-prO8llniMMj47o3_7uTdK8Jn16nY1qwuz8WB_2aqu1KJh8-YQlJ6P4pNB9tL-pYyIqk5CK_8peibYN1y_krMPoNbt4QkkfUgj_JNPwjhDLP8n9_enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZztIBEml9MkNkl-Bced0SnWTpifFT3UNDMVMY9zK-1GkfXEPuIAZPBtPEKAF1yk4YEt0ffrlCF8hJV0hWzj5A2KrqIDBUnoVBNd9at4qt46AnpRWJLnyTpVBIG44qWAoBVJzWDnpPDrXZWQdHV6YliNFRSShhWIDSA6SZ8plVkp-96s4W4UIjhwKObm0wGeYAs8fpGsROX0oXga2xc2rpcR34fG68fA_E5iFciBpPbGEvzQMCjiHmtlKKsZJM26YfYhGS1r-LsN4lLaDu5LHLPp75pRuCSniXDm3xo71gZk6peLmN2eEl-gXONduE3AW4AvQCUKJbKeF2imjpQ1yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLzDjHedSwnGRKrGcaKWmguyGMlZ9jGVbK12QzhVuHNeXrJ4V9Z652yx-V7TApaGR1LFaAM-AkXsAkXbmpKpGUh_0kft-ixVYVSpfgDe9P7GDSPAcSvQS6dTnhiiK4ODaIk4AOBbdR3poEOlFcKIE6oSqQ7AfdShmTFpKiw6w4K8M6gNzvlI71N65EAdgpXV2R85mP911g4CH-pmJz5sy70fj3uUAdbh3GBKjaFYc-BwyRm4vKyF_4uftFlZDf7nvcg3eVlpQ3-TN1JtF5L4DLMbGpRlSep35zBW-wOxD9mXHIzS1UXNcmdUIPHeS99YkBwtGyae2hNqOxYuz1jReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=L4TX5j51Oo6-sA6-tN8X3e7k8b3YKlkSLN5u69LW0FnwxxTyTtCognzOe3oSRGwFG9nzBOcB3oYE_F5g0AqcINRVIRnOCoVt6UsAlsFnHYv2Kfqoz1i20y_28kOijLMSXRko3O7846HAcJtsjnrYFDx1e1WT_XRHgJNxdljpwxMM55VKGwpFkXybs1QTE2a4N6mOd-GqLBWieakw6C0jPf6sBbRYVwPuuakgmK--taavR1y2WJPpheH2nGJ9BGCKW_AU3gBmHsyZ2vUO-IhbgyImahJ1G-0kZWAlrjIBy-MGNmokWHuziJXYy0BnQPAnf_XtXAL9qA9qVgeGWPcGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=L4TX5j51Oo6-sA6-tN8X3e7k8b3YKlkSLN5u69LW0FnwxxTyTtCognzOe3oSRGwFG9nzBOcB3oYE_F5g0AqcINRVIRnOCoVt6UsAlsFnHYv2Kfqoz1i20y_28kOijLMSXRko3O7846HAcJtsjnrYFDx1e1WT_XRHgJNxdljpwxMM55VKGwpFkXybs1QTE2a4N6mOd-GqLBWieakw6C0jPf6sBbRYVwPuuakgmK--taavR1y2WJPpheH2nGJ9BGCKW_AU3gBmHsyZ2vUO-IhbgyImahJ1G-0kZWAlrjIBy-MGNmokWHuziJXYy0BnQPAnf_XtXAL9qA9qVgeGWPcGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP_uUfjxLxMf5vKgY69R_9MKS0ZXpi5n9dr1tZ1vqENLWVP1HLViklwcFpbPtRcfOahKEnSLfkqsD8EXkCNq2jxJYIRJj0h2Hvw3vKQjlOeJK_DNJMHwX0OCJlf8oM1UpGOfnRKx_4I8pWj4jJ_kypF4x_RwLNBEe9uhgcwdU8e4XbntcipXCaxfJGSweZrAG1i59cZatPr_4igNLXy63vsHsus9hiB_1HP2PVElquy-wfdDAbP12q8IcvbVqi6ZN0TXzB_wQpaHIU1Omm5aDEfkVyJCsLy12rKhzkxpyKYgRitcKzENMeXAWdspx1pR3iOSG26cW3emN4_LX36d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfKEuCrKsCpfM4jAGmC0r9VxGr5CRXV3Kd1lNMTGWKWu43EQDI5sGoVaLuaFc2lcal3duOj0UriUNSfQ7TEusw_0e7NVsQ4PHjXen7YAm4FrPPmWyqnD0NkaZnoQKeBwtboVyCSJZ3exBeL9a-0IoQ_zQ5i3rLylsEzr9cjjdl0Kyi3ysAQq6zLiuGWG_tuBFK75Rfy72gqWAX2mo0HNQenWwL_MxZfqlwdvp7Ew5p0Z6MBgB3NTVU-MJp_RND7X-sTsQHXDqRO-uivlxYnt3iCb4j3oeLAMmOTHoQK_-rK8JgKxoStXn8XxUSYi9NBbILBWmwYGdjgsPO_b-nKZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFqEDfWJgDd9Zby1kMXVSDJhNQr1OijyuyBAPwBoYxpuOWiYa3ZI2d7LCU4MiISdJxjBl_DMrsjhSnuuzz9tkfPOV2dJjhwNnM5-8Gjo5EDWtYDuYPtReprx1JzwKo5e2wr_yeUw2OVbzMaAO8snJMd3DVWVVrwDXSGzVfzkkD-rYo-ST1yAB_jsvbbDShC0--a4OW-6k1vedksoj2k0OeCjEeyzWQtGXa22NO-J6QTjdoAR0w1tnRhNIZeJ2-cILKxyezr6_nsrLR2w3J5oLmW3ho6SDa02i6Wy3ctHgyDOpKHeR4cyAGhu-7-wpl_f7b4k4PqQoqLEOj3xJYVDUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4x9Y_st7TlO12qeiwrcimr8Vz1PhpciKsTdQNISeYBfqwazX-q3Yb_jf_GfHuz2lk2EQ9_C0py37Kdq6X-OtHHrDJD1-n388M2y9n9D7_lNQl6YgEYhzGekw-1Rs1BSsD_wyLP5z0T5QvcMN5iH-rPrQg1BpclecJJb0i5svkRjOAht9ttLWMvH3sJj6GcoXZyqvvoiH4mHwDOIFcNSXfpBB4iMVgizYBm18hhi_jO0HG4UpnzcSGOYglAlap-XAL3dbfWs6KavINdj6SEmsljBrHL1wk9dkWsMep0C5NlGKXa1m1y5K4PPrNlpWl7e4C3dqpWtI_a3ANFKfSSDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3YfWQfgsN_L99Hb_YkY4D7Uv4_z4RmerksopR5pc3RPZY1Nbi-JfhwcAQx7jGqb6uxVnRnLaumi2be_qLWSv86_uY7FHJgBrPWYqKiR_ZBbpVGNldjTT3j-7I1dLykE-LIYRXtYtCsXS2CaUtymIT0kHeQa59qCHjQS2upEfat9jxMqryxGAUUogb6zZCYgZzs5G1SddvXuJ5sli0bWxyQfAE9zwYK4mpnc_JWlAhppFa5nA5TFRnjUna2XJIQUFo_-OsZCr4G3BLtIUqayD7McrrTEvG9QGhf7iuP2jYxdOyvDMk-b0xq0aIOdt1F1b-2hu71gf4wRoTl651YxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czk8SD9axv3Od2UmSQPabzaK6S1XolILFxhBii2QcHhXJSYXpJ85pGpK5U81yi7awJGUo2TyvhokRLULw_Fuxqgj0bE1vKJb-oo53C4TkyUvU-UwHd9MikudnNmO8s56WByFeWDw6GKWq4oFMsPigR8CteIKw2mRxL4xRG6mmijCjoC234v3C_Q7zpoQfcNNA0lJ1Ti4fbe3Rr9B-hujrAxtvVHGc0S-lP-G67DykfG6xENj6wmRpXG08GkhNcGTZIcLhLJspU0ln_hdiMN3W7vg0SXpDGTJHk8AKbEfdD4tahPvQ9w7N-XnYhdJuMwhjpcRTLshgneagynmnhAMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxx9h9G0a6XEH8fx4_3aeMMv5g9H7EhJFWu6bAx2Xy2drAxPSt4CuFbkJj4nn9sZcEXUqEwMaZZqfhVIcFOrN7INSrkBBzAnMVrjAdHPloU7RopebpNo0BaoWPhLGFkkRyRpwU1BXr4pnHBhtANy9eqRfCf5lJsKHTHkaTs0JI_9yEqdRv9eu1dKmHPUFZ55CMKWVBzFighehIFNf2ewSDI_GWVIf35BhnUHgUQrBlMEXNLDzOFUEbwvBEM4xFMk75D9fpVnXgaBPb35rnfygN2Rcm2c2mvyOSlIrXJCMQeaB8qMuFxfSN2ZcHICTuJC30i8e4NPqW5pYWkMl3qMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYqFFmVjMOA3Wie64bwAs3Dxm32lIhQ6sn0RZvLIgahwJ8VTYWrKUabyF0R5yE1YTfHjY84il1fG2E92HjEQFQz_92nO3OMbu8C1gR9wxmHQe8xLyLfIJTMmnvGLvVjQ_e4-2m6oC-u9HYkzCoGjmzjddpTQ9L21aRNNDeDYf10FqtiRlxut_z6apurdDR3NABGuFH7_2AXrZSKYwopEOw7off3FcyqwFOgt_v-fusyLD4I6dPEzd7OcjPZnJGitcd-PFeo4e60lkYObU29kLnjXA0Ic5ixb5fttnimGjIR4ArqTtJAVneBJhTLlMbufFxHMlLYdeX4MGrjFa36T1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfC_JHIWasox3sQ9rA17Dl4Lo3YUBCgN_Ni6sKo0z2Urfr1ZWFOV69sVnJxEppCcvZpeMUoE768uaCPuAtj4LKystPI28QTX9smEU340HENz5IMnphHo_UWzSP908QbzpM2WiX7MSPzsthZBUhZXgdD0rE0oDVGk2JstYt5PCkY37GIiIWyOBm11AvocjNMiP3ekESs8Vsq44VV6ociSve3GDzUMvyg3wBfpPks4zzGYUN10sajdk4DlPAUQyhav8W4W9jZrA5Pyi4tAm-ltcpouiVroAH199ARM8TbqUCDUbGoU21oL9T_0fUSXSWmI2rHUcmJLDKUDlVOn0KRdDdOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfC_JHIWasox3sQ9rA17Dl4Lo3YUBCgN_Ni6sKo0z2Urfr1ZWFOV69sVnJxEppCcvZpeMUoE768uaCPuAtj4LKystPI28QTX9smEU340HENz5IMnphHo_UWzSP908QbzpM2WiX7MSPzsthZBUhZXgdD0rE0oDVGk2JstYt5PCkY37GIiIWyOBm11AvocjNMiP3ekESs8Vsq44VV6ociSve3GDzUMvyg3wBfpPks4zzGYUN10sajdk4DlPAUQyhav8W4W9jZrA5Pyi4tAm-ltcpouiVroAH199ARM8TbqUCDUbGoU21oL9T_0fUSXSWmI2rHUcmJLDKUDlVOn0KRdDdOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=jJmhUYmu9PwyTzsYSpO-u1Xn8jqm_uaxd2DU6vM2uivrKZW8ly8CHVimZU2SWW6vJvgbbUQSOP7s7KBnSqaT0mBxhuETl64HBsFe4OXVCkSftOq2ereWAkcKUkCH5lMTt8JqdpqIHlW9FsRhDWsOeBJzcwQrMF9Nq_aitXn2cpOC904lTvwvx5Dw51Fko-w7OC7nBkUXjhhJPj63TAN8jpCfhOBjnRsxeAhHUAvpZKxuliovqZ1iLzxf9BW8tJp0_pEN-OrBK5SN3unbqyeLVZnBYNgGFjn9tId8FFsKUhBWubuiHp34alEw2ARakzbu4C-aue8BLyILR7hehtKM0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=jJmhUYmu9PwyTzsYSpO-u1Xn8jqm_uaxd2DU6vM2uivrKZW8ly8CHVimZU2SWW6vJvgbbUQSOP7s7KBnSqaT0mBxhuETl64HBsFe4OXVCkSftOq2ereWAkcKUkCH5lMTt8JqdpqIHlW9FsRhDWsOeBJzcwQrMF9Nq_aitXn2cpOC904lTvwvx5Dw51Fko-w7OC7nBkUXjhhJPj63TAN8jpCfhOBjnRsxeAhHUAvpZKxuliovqZ1iLzxf9BW8tJp0_pEN-OrBK5SN3unbqyeLVZnBYNgGFjn9tId8FFsKUhBWubuiHp34alEw2ARakzbu4C-aue8BLyILR7hehtKM0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=YAnElo7zGA0lYu90kAHUfZhF3T-bUXeNdD0ZpKPhT2dT_Ib-FYujcz7KX9_I2iJJLV8ZO_u0WdKrIuFBSlNgq4lbIPq57_wP89sMs6w7JWUndy1RffE1nxZndd30ypTcJsy26dzQs1Yroy47O6sII7P297yLFduZvuO1vctOAFoAuIcFrt0ht7hnxTxb8W7qZyNFSDw63VBHwAbt5Y8T37It2nbzrDYqd5V3vSvRhqR3uP6U1kBrYc7HxnksrgebBDMH91FucEMH4jEj61tGG4ahGUMJQoyhd_0hzRNYeenU3Oxe5rk8nHgBt4A-r8jpB3mFNvbGBaAX2CFF9g0ROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=YAnElo7zGA0lYu90kAHUfZhF3T-bUXeNdD0ZpKPhT2dT_Ib-FYujcz7KX9_I2iJJLV8ZO_u0WdKrIuFBSlNgq4lbIPq57_wP89sMs6w7JWUndy1RffE1nxZndd30ypTcJsy26dzQs1Yroy47O6sII7P297yLFduZvuO1vctOAFoAuIcFrt0ht7hnxTxb8W7qZyNFSDw63VBHwAbt5Y8T37It2nbzrDYqd5V3vSvRhqR3uP6U1kBrYc7HxnksrgebBDMH91FucEMH4jEj61tGG4ahGUMJQoyhd_0hzRNYeenU3Oxe5rk8nHgBt4A-r8jpB3mFNvbGBaAX2CFF9g0ROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjH-r2MPyP3zC3kvrtUpHqbcTQqTQy1M1M2nS4IFjhowpyGMABsaMBFMqbXCNuKpLz6wr2tStoxCHYuH8GLmNyqoXCl6YvufZD6kSYZCw521q_G8pNX3ohFkhMysqtmPBI1eAB2SocPT8kFAf9iA3ZlijMioCytBT9QzJxJX9Pv8HiY2V2RdXkudB56_16GFQZZwAP2QKAgQqoUp2cVsI-Vt3KxgFOcN9r4UNyJZtpNfCg_JuvWv5YsXb1TUJIedWKtkFfI8m9qsoUiTSfAJkL30LYaJ8gtEeV_ujQ2XX_7vqsCu4OCb8FAucSmhdbqhh0N2qfIZK1HqcA8o1cLCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZian5eGNhl_0KP1IS51-VGlMCn-rJ94mZOiJPrnTbAbhyAZRwJm9KAWZs2qs56v-BmemjWY_C3pcmcaZ4Al2_7rXGuF1sCwA9V8v8W7V5tiB2cvwtn-SQfrUJ561XJ7MHib2pAegecZC4TZM5JC9HPFjiB8QcLqOXVHV8tjIJg_oXA6-FSqG6ml58EzifKbura6nX7G-vn54gX_QJdbhLeJ3byg44al3EGPZz7E_2ySA9O-tDZcWjk1XXdl2x7kD-0Ux0T3AAoba4cbi_-6mOQeEk0B63H271whgY79ldu3nl71u8BYL6WiW5o7d7q6DtmEHsU4Zc_ChfdrxfRmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGZIE7tVaP44ShrxmKMHG1nctzlFShn7BrcvWifo4NDgJ1bNcF4c1v22tPv-YKOjK6VPla1fhQw_ZcpIUKJMlPQIyk6yr3f9yq9yn7Xxs19GNw7UwhPo6RXEKWpbqh2kmobaw4DRT-sa9yjL2W77sFdikpWacetEzS9emjQwa3LG2k9gWU7MqFfwx3lh71s4U2ir7s1ZdTzjG9WOrCrsMM9KVnwEdl4jUDlKgOdtk4PWcn5zqDsDHbbILeCT7qrq9v3e6d5pWwxVl4nwT5AnW5r3VcnQdH_h11vvfCOInmXYX90YgNCTFWXm3guw0Dw8m8gdVm0nsbHb-qcbzj3Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=niSPPaHy_RfSiLcub41fVr1VZbF9O4wnhoNEJiuKU4Cf-u4ZijJGRGWTdl9KXYn0YyG6-2rXeBoKdWKmArqb0c6-fO5we1ubCMb2f4Lyb2fwpQVFYfDAxM89JcO5WV8xINk9RGNUod8AEHqmkubDggV2wdyq-j-Cv7f9bIPPSAdhqjYOda7m28e4-jIzsDSe6BbF_vN9H7Psxd7xOoRFG7J3Hel8rTGvYTGOws7nLmpKpxvHhMNeeauz4tUdpy_N6KmSsn_cAqYeBNHE23UCbeTW6E9LHZDr1iDnd64kq4I3vYktgsznciUr80YnHDfCXnCBsoZhBgwdXHsD2qPDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=niSPPaHy_RfSiLcub41fVr1VZbF9O4wnhoNEJiuKU4Cf-u4ZijJGRGWTdl9KXYn0YyG6-2rXeBoKdWKmArqb0c6-fO5we1ubCMb2f4Lyb2fwpQVFYfDAxM89JcO5WV8xINk9RGNUod8AEHqmkubDggV2wdyq-j-Cv7f9bIPPSAdhqjYOda7m28e4-jIzsDSe6BbF_vN9H7Psxd7xOoRFG7J3Hel8rTGvYTGOws7nLmpKpxvHhMNeeauz4tUdpy_N6KmSsn_cAqYeBNHE23UCbeTW6E9LHZDr1iDnd64kq4I3vYktgsznciUr80YnHDfCXnCBsoZhBgwdXHsD2qPDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A71NTpaUyyBXMvPGXX-JKF5Edt5gLhpNo4AFejDtAMXg32Aw-EunL7n5cqtJUrX6W9PYWAFPHr-ZOmgTMw6y1jVPciB1s2jM9P24KQgtpdnygzTubWTUM-AppGNi-gCTzviV6XE2B9kKY2lpDfG7F5nIXMxmluSB3dX8GTVRl2EzXaw7Sj25JO81igd4oUX1Tbu1PpiZWkBavHyooGXT0wCoPdePfvZPdoKNbRUu9YBmkUyv0Q9kWRmJSvc01dB9I40EreHCJCCbCB96sWJz3AV-Il5H4Nw4ZXZJtyUbEQ7fPleyzM94MxeeJDHvXg9C0QLYIovN77oADmquITOPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_JTzD9tLYs5T1T8y-20hkkDCxIjUbjA2e28Hne_l6E70afMt4Ttn993Y1ZK2W0VPWwtou8L9xdGl0acpQaVVKYRTQHPh2xwBJw5dc3K52EaZaU1k4YiFtg-a326EMmHUqlm_r37PHU8u_Au57eDnF9a0PUX7FQn_bd2pdrZ3uDBucPnIKLTtnO_XRycIWD25lkBlKqyp95xL1WUUwzSubevPotUpumeGCrWcZ0RYCICjQpRCSyQ1RVWRYeAaukwnntzx7FuURx5sOmihweMdtTCSC-sqYMS1O0Djw27qXWAnJfQVCSyTHNQ5XSTHzzevzogXcPUo6_tNUa_Fkqc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=QxqYQ7J41KHG1xyIwo754s1EiZ12M9ggD3_CloThXGfn9JVDgDWFM-vT2Cr2iZv270ngHLeNc0vtEdPjSmI-aKPXMClKH643Pp-C_saPeHMJVqb24IEyAuBalrV7Z0BEDFuXHFy3FbnRnwGxow8MQ7J-KgblyNjrjnYefyKlk1KqiwAXnRG5WtTwSgfOCbM1ojlWsVG0k5SWkXByVv46sbhVClMs-gInAhZLcrQZaCTiV_EIkKuXy5vVCq4ELL287NvG7nzjFIXITJcU3QC6-Iyh749FecIBR4TYkFlpdHdxeY4O0u-sZc0tk7pcDDULkjiYsPgGlUkK6CZXmnPfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=QxqYQ7J41KHG1xyIwo754s1EiZ12M9ggD3_CloThXGfn9JVDgDWFM-vT2Cr2iZv270ngHLeNc0vtEdPjSmI-aKPXMClKH643Pp-C_saPeHMJVqb24IEyAuBalrV7Z0BEDFuXHFy3FbnRnwGxow8MQ7J-KgblyNjrjnYefyKlk1KqiwAXnRG5WtTwSgfOCbM1ojlWsVG0k5SWkXByVv46sbhVClMs-gInAhZLcrQZaCTiV_EIkKuXy5vVCq4ELL287NvG7nzjFIXITJcU3QC6-Iyh749FecIBR4TYkFlpdHdxeY4O0u-sZc0tk7pcDDULkjiYsPgGlUkK6CZXmnPfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwvk5AFI0HHRZD2t6_wWicxWNhB3fpi0jc6mOxVYsphsdl6itINXsAPbk3mh0TsjQpXRrLBA1hJE3Zn0fPz-K_yhRHKtqRyqhpxtgIXP1AEzYZjzyJDseeADon_AwoGu045oKljMq7hlPT2yVSH2KWPI5R8EmpDzaF36tg97taePDBr7OKPDdy3vuUSVhoiZufMkeS277W1wCuV0DjT_7XWa4rE2k6hYH0oVsxPuPZG4lyNGW4av8HNgT-z_aDLe9HckChmEG_EzAeEzHj-Gio9ypgsFaFGZz0JoIPUEsistzj-lDA7QylGmZ4AeKxqHysVZywpkAtLT5dUscmnc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUMaw0JzDb6sTKjUej88IFSHcqd6_86q9BQslWutuUkeTBDWu4LBAJqeka_LSKee5UZyA8lzzMM5DtkXCQoLNe9_lINGUuz8MSb8w0-7Zu7EGU86XPSkOuZNDVr1gbjBTjDn9kkwy8gcwGs_GghpbQ06QQCM-ZATGinJ3FDYQC_oEJIlFSCgHuovIioE-HiZQWkYe_RNLSxOAbXLvCUfAvBX3hXfLhTwxf-Ttuax1n-1-CY4__FI457pfTEqiBCc_a1Qd42l8gdkWCg_EZmVjzgy8NQxG5dhPQ1msVmvcXWSSlFzf1hokVf8-yu5aYGiOyJ11vRfvyUOOaqsXm1dNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=kYQk5DxnQrsbn5lE32NEODIZ-W8r33VJX1E54b2ZYWV-j0DJS9ktmLeBzadWXoh-Nd2vrYoc34yHNwM_UEG1BUu4PqknG0r_xPj_4lZURHeQDxVDqFBWTKjhvIxFbCRETQK7pNgxaqU7Kh75Noy4zKj4Oj_QdhI3UJClXSjICZIO3INSx8nOAhGDF3XxrRVgYK_Uo1DK-FELjUvIxxe4p7e-7l6RmHnRyoZ-a1rlf9rjGn9IFgmNDsSRMbBWTrIhAN9_Mv4b0rW64ARIMLZtu6rTqrAm-dzdFEd2NjWI_lQt-gTVz0105KM8OPjZv5bfyM53r432-LvrO1QnmhNhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=kYQk5DxnQrsbn5lE32NEODIZ-W8r33VJX1E54b2ZYWV-j0DJS9ktmLeBzadWXoh-Nd2vrYoc34yHNwM_UEG1BUu4PqknG0r_xPj_4lZURHeQDxVDqFBWTKjhvIxFbCRETQK7pNgxaqU7Kh75Noy4zKj4Oj_QdhI3UJClXSjICZIO3INSx8nOAhGDF3XxrRVgYK_Uo1DK-FELjUvIxxe4p7e-7l6RmHnRyoZ-a1rlf9rjGn9IFgmNDsSRMbBWTrIhAN9_Mv4b0rW64ARIMLZtu6rTqrAm-dzdFEd2NjWI_lQt-gTVz0105KM8OPjZv5bfyM53r432-LvrO1QnmhNhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=M3g2Lpgd5JRoTbxfSbd0fgjf3Q_EmYtzhI3XBSyn6gu_5nYcnYnXxUKtDTC8GfAxA15uDkq0r_HZ5zQJRIA55ILn6qfLW9W9PLeciwhEwFQzEIcIUJ2eh92uPpjfqQlycG6BDe7Pp_EQNM-LFwmBn25N9rmR-p8Fnoquf-0AF92qyCJ0OiomBdlG_gMmKBAqpil9KrnqYTU8Htajx38w14ERXlKJ4I2113efHOFRMlvyZs1O3UHqZUQmSesiy573aK1LPfBPczJ6g9IJZ1LqRxWgRaro6FWnQ-BacV-rbtozeXh1_cE1sxF4MLWK2TxfCWnHtB_1S_0wToLon4CxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=M3g2Lpgd5JRoTbxfSbd0fgjf3Q_EmYtzhI3XBSyn6gu_5nYcnYnXxUKtDTC8GfAxA15uDkq0r_HZ5zQJRIA55ILn6qfLW9W9PLeciwhEwFQzEIcIUJ2eh92uPpjfqQlycG6BDe7Pp_EQNM-LFwmBn25N9rmR-p8Fnoquf-0AF92qyCJ0OiomBdlG_gMmKBAqpil9KrnqYTU8Htajx38w14ERXlKJ4I2113efHOFRMlvyZs1O3UHqZUQmSesiy573aK1LPfBPczJ6g9IJZ1LqRxWgRaro6FWnQ-BacV-rbtozeXh1_cE1sxF4MLWK2TxfCWnHtB_1S_0wToLon4CxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYdQb-XnXw7I4zps-fR_Wd9Rkqu7vv1Cg2G4IhZM_TEaSrXM714pFAhVbP5Y7Ss6HPneQCh4z_bR5K8YdlhXCVg842N3tI8X2IHJEB0cNv1BaNmnVu7qcstGr6lFymuRuqU70L2J95AbRRZGEoNI6e1tM_paaCgAWNSplrY0yW194SXP4VdaPwl2w0J4gVgbNV6taGChdJrny7tzauD9IDEUsN5gtcG1L-t_BFnm4fsxezz_itEkSj7BWkdMG4XGzx2l3LxI8zOSIWSt-UMOLmFZ5jtgfmFpdzaA3jMS3hp2KpPiGFh62hoFPYHsQ8X1BfNnMOZU4OPxerWYR5LbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFCl1ShKmxkyVBPKayOEFsuDU_xPB9lUYsy5eNaVIGL6daghB1UmlPIM8O3SR8ACSR5ByCvxGuorWG1jSwkmIbl3-Z7VUQKYlEVzsEosJ1OJU1b589yFRB6sCRKQfCd23RyXn-XX6YHiYrImwijS5MXoOhmNbsx6TR4z2hFzub6rbasCPA3ySw1xkMEh41uoGWBe6HvWNzP9QL5aSVIrMOGjCzrsSeI039X9LUf1Y2IJ4aKPFtrSozfTEjWdmKA1QY2aE6_dPlkFDgbl1lIu0LGIi3s6HvyYl0wWzxMMbtfIvYIdJMiTcM3iuRRZ2TX_unHzgX5xxJKO_4Lu4yZpQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQg7MSpK1bFMiD8RPvzs1xLzHXTO0gGA9wqeqkajUIQtXE59qdwbhc3Gd9GIOXJnabSomr7Uou0SFiYfNHwxRMwsVnnxp-WTtBREs4eKlWSq_ZlNdclaTNtDxFEXMpI3AruIRli7jCMNvVwe_JI2PbyXgszS3Ibx6NeWrEh22PSjfhyRl5N206d0gjPxauTMVjCN643h3UIE-zhALLHDREal8S6kSeROr9sRhubHEoKcQ2ieK4Xf4TYQAZlMUaJWD8JPuN9Wr5fgPe2gUL9F4-l-9NBm_pDopS1mdAxsfohbVkIZ-NcGn---L8k-D4Mr6xp-2c3fxxMcq4bB0nBIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLOCO-CG5Tlw0jH9Bo4gYVfoAzk7Em1Y22lowINQd1qcpMAWrFiu1fHQF2H7J3JnKy4xoa2oJw9Rs0wEe3vqWAtqFuZZbVaUiVPqL0icAzfnjgD92b-hAblLBsdi1NVhX3CRPgHbJ4ZOzq1wRKkgYHfOOiMdoyE0FgcZQfClqs-P5t4abLqw8cEbMmMrA9EYHugz3P-4v5bqwzpemYzTNaQNbi9ks56hdmWw7INGw_kRh81-g6Sf5hqu3vOg5zxqiU2vcujhatNZQcKcB5hW_CP9pmYYM7cjikcgE4_g_3N0sHKG7JAk9EUakmdE7O47lxT7AW9HShZ-nsudBqWfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Og7AWFgeen9ixVT1kIPK63ajNOnzVf-gvMgoAYctO-sfNWr9n-fLDRxe_EbqRaGNaLvoyncAkJvRAvTG4kfjhjjZmGBobcz1wwvUVUO-idO5utO4wj9SmJTXYdi3bHYXXpOvEKMULDhcPAdDJ6Pb-jDVvfTiYGxbXq3Diyzqjz6EMH7N_lts3pVC2pZQWw-buydRaP5YD2Wu0cHVQjkOUGnHKe76NQI1_pt09dIaeR12dCzNZhnU4xYr-i1YHsQlSCEhqoLWt5s2HEuyzBI2aK4Foq6BqxktIDRO4QvYAbfjKOdkkueOzaRpeiUvRsbzbiLg6cgneSDJxUEXU0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRm5WHH25Z8CRHUG0RPg_91sE3oBxe8Jb-qse-rmNIADxyn-wrvD9YgSICJ1c0xR_IcgRTasFGSmvQIICTDS2Z7NBHu_F60BkEdC1gjk_AWjtuEh4zP0bOSe5oq-7YVJtXFSb5jufX_xsJgan5UIQEcDxdZYo6XlJ5Sl-vcBxaiS6e5E_vI3RRjXuSsqvx_v30YLoqR7F1R6c5_tfquoclNLUbiOGVe4aUZWaciKNBhQl7xZjs-k1_7Fy-s8kZ4EUCmaEsdN5pzP0ze7Kek-917o55E91yN_32aHfoEIwoFtt-X63yFSIx3jBSTBcK6-OIr2a4FoWqW3ab9yg6unzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=lRodxBjltSisZmPxC2SmbPC7-Sdvh-hnptycv0N1M3_yDgPSY-OZ9Wjg8XkqEVltPmiR6fDW9aCTQOWrdA3_dn6VbWflbK8soM8TVlJrFHDGBMpLQDuYeCQ74vH0Ena3yzlyQl4i-YiqYbrWzpqCAcRzkX1tjI3wz7Ei98_WmUCbPyx4hjdwoLWsSE40W_PWZhPDA16LDP__NtCM0rmj_vrt4rHBHzKqcyiJsSMDzIC-7DRUtlASu9Da2yV6bBiGJCDNryBM4kfCHh2MLy21EEDk8-G55pQPXjUSEL7UHAa8fHWN0D027cBZTYepSXvA04jGj_KKRB8nyb1nlPOFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=lRodxBjltSisZmPxC2SmbPC7-Sdvh-hnptycv0N1M3_yDgPSY-OZ9Wjg8XkqEVltPmiR6fDW9aCTQOWrdA3_dn6VbWflbK8soM8TVlJrFHDGBMpLQDuYeCQ74vH0Ena3yzlyQl4i-YiqYbrWzpqCAcRzkX1tjI3wz7Ei98_WmUCbPyx4hjdwoLWsSE40W_PWZhPDA16LDP__NtCM0rmj_vrt4rHBHzKqcyiJsSMDzIC-7DRUtlASu9Da2yV6bBiGJCDNryBM4kfCHh2MLy21EEDk8-G55pQPXjUSEL7UHAa8fHWN0D027cBZTYepSXvA04jGj_KKRB8nyb1nlPOFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQN-LVkb_oc3Q5x3CV6iDaO7eRUXQTUftEVUq_A9JhBM7RIYsttiz6RITdxTgnGzP83mwV2hs6wNv5yYx-RpyK6dInlISu3zassTSvYoIXrQNrFp_2CUXHeaQgrWrWTwOOZP0q4SjeS-pSOfLQOe7Jrl6DRFZAu7ib7Pt-O2Q8QCBmrZylIq5a4tJ3GsAf2zQG2JrgDVK4joRqIsnhFad3sfJ1XdqX6ZZTmyMxIZ3ru509H7GoOyj0qxB1FYVXalfTKcu0Rkbnw19FVtayaToRfPNz1O7sXS52en7kI46vFmM1qYQtvg0v2jJFa9wTLusOFLEzcc-JiUCbgz3ZMv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEX-UCWzzpypXpyB5PAOaAarcKvclmeojgwvwtoJrAL2YGc0XL-r_hjM8UqR3T_bqykEjA2b3WA3vK1T1cl_y9-jKavOHJBFIwG5KNld1vg16BwHOQ-RVBjy-r_Znp8S1DJXctpT42ZB_bF2WrmmbaV42bzgcH9CfYpJvVdSrVZR9wnSwrxsF-maDTdPiNiMRdJXCs_NUHWVxPAsf8vOzUBkuTaHHbxH5tyMOENcrdd7PFHiBSSFcXWfrtcGGiYUU--kR3gJDCbFvhUDwhG4p2VDFYOlfzT1cRh2VbZ2vFeKA-Puj1-rU2scuLgM_06aZ960VpxCkT6jccEo27ZTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=Oa6JQRhlYqYYmCQrbBAgBuL6M-AIPXIzvxUBLmLhXbN7DJX9ajcVfNPt86SPbqL3uaVzHI2uazlVYJIkaQGDqoJC59DCOfAzrza5KO3J2RUc0_vAmvkeWxJ2l0Ifwm4anrFU_E6Kfz2mChEm-3oT6c-1nH_ErTLnqzmvLRK0lAkIXS7s0XNLJwBswS6L-k5z_EP-kHpzteC1If1Ii4ZoaIKA_uMyJqaZwsvI4V-AvNiiNtqhMKU_FeglDXz5q47jxVE7Q-1qFUNxVMoXRRTro-oZRBo633Lz9xD9UWKnBWzMlw2vXvwVF79Vgmhl3a5JjWo1Ekwk1_RTdzpbOPki9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=Oa6JQRhlYqYYmCQrbBAgBuL6M-AIPXIzvxUBLmLhXbN7DJX9ajcVfNPt86SPbqL3uaVzHI2uazlVYJIkaQGDqoJC59DCOfAzrza5KO3J2RUc0_vAmvkeWxJ2l0Ifwm4anrFU_E6Kfz2mChEm-3oT6c-1nH_ErTLnqzmvLRK0lAkIXS7s0XNLJwBswS6L-k5z_EP-kHpzteC1If1Ii4ZoaIKA_uMyJqaZwsvI4V-AvNiiNtqhMKU_FeglDXz5q47jxVE7Q-1qFUNxVMoXRRTro-oZRBo633Lz9xD9UWKnBWzMlw2vXvwVF79Vgmhl3a5JjWo1Ekwk1_RTdzpbOPki9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqCIz3ZlxH9IyRDJ2JvJwBEcZ6DG6EVDuNMK2mFhauhy9_y6ewD2psG2NNPr_gyr3-1GG4SiC_cGHRS9ZOfdo84h-POCO1-aRnxnsEk28PI6sjuybq4BdkZocl9kyTPkchrm-NHHSviBQYYT6uEHk_rOdd0f5csDWsFMBt8kFleH2NTUiLv5I14bxDOZt0bKrPTtRHV2RKdCvQ6kRTJxnp-485w9bqOJrUUiCbFakn6nShhVCIM7XvzGMV0PXLmp5Q7TcshSdFgOH3iqb5ijYlfLyn2HgmnxbKYyYmLfjhYeo_8NwFjnjCkV8bI0fgazzRTjGF2go1WpllhdzJJO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGxm0Vcjt61w1-Q1wOtbIC41vQQ9xEiLtV63u8o5zASepq9-L2DsfLJOKAVMQ0k56PAzrrp12TQuzVpuFWiwLDyovvIydoqM1HPlT5uBRq5ytdKC0FSgAVY_v13g2qV21Wz2RhHSxlD3OWPjc07F4CDXzIasQe42wcM2zui-Glqv5FpuQgERFPf3YNJolmHB6MOg22ATDXyAAIhernrgvKQvVtbooC1M-ZJfmAt2_ViRcK_7g5u1qICV_-lrmYkctedplDOD1spNHUMtRt7WiSfJYvyyCiAx0L4TOhOfqRnEBW_5CueDfDHLYvpK8XIQ1b2vV1mWc5k_WpYAzn0onQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlhapGhTWweq_yc550WAukhnJ5im7qcY9qjjFUdTIDA0jHnmDUPzkHTBTTatqipeg0xV-0aSaFymXi_2UOAttWT7JSEtf2963Zw3yEvCEczZ7IQY7Qjgm9nn_stdPfYF88aJilM6LKI7S0IORIC4rd-KtHbK9n3GXS2nLEFd0xPxjOUrud2mVDnedun6m1b09GcAgi1SKe-QxByHTmovow1Kvq81R8fN6qDQljWskPM75sRkzNgsIjKsirozY0DXwNCxqYluWvyuoA3tG-uEv5Ma1mv28PI3BfcKM_9cQC30kOGra-7I91H1JPuCPx9wQmS2iwTd-SoY_jkQop1Qew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix5zQogZ33jyfSLLaNWgez6oiX0BRbRtFHTmQV5kWkH6M4cXhIjjVUVLVOWNCFyUjh5M471l8epqKgftDQUldjMAb5gos0QLRsezy5pIpFeK_kj4EP-qhzEeqwTDfDxtWUG4qNQua3j3tRvAxj9VB1akvpYRBaWYP1V_ytfi-RMbwqKXGy6fFyekQXXDHQrcG7sGLcypacqa7z6HId-WPK2ARu8yqJMdr35x67-bvTOXKP5Ds9PWYSeDtlAzWmtV7bwJEgSWYh-qcikjrsDzj62dwsD9A67lx5IxxLskPhmKAYrf2sl9ySEyNYjt6GymTnBIeaC8B09qoQXjStfNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulEwUInt8nVhZneLeUj-Y_TFF-JI9zpEQOyafeevzoaVUAMWdDiOtpCeDstQq5jFq84WQrTcky2wacQCqGsFIFh4ER_J7VxBs-T08fcaMYehpniNinjLlEeuXHFx9iUSGYQdVgzaJyXR0mn5v1s0lVZMeH8vtxKVIihBQTiqjVd81QBEJHp-x5AM-WigkX7knVvZNtp3zzzLjUU8S-hTMGfHEcjbFgdl6U2g8lYEMJUpRzZ-Z9eWgNc0fIQRXE43SGolgM5QsC6q74y_DHvpJG6_N-pPtHMmD3gxHJOpVePj03r7QQxePA6eP0QcYVR9g9I6Sxnp9CXNgca3k-QUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORUFJe1FLdEpv5MgMb7ulBv-kj9tsQjhOi-suhHEfDD_8QYTLXiSaFKel4aYuZtTZzBOEH5aPifVcXj_f-fBrpr3EEoXAFaRVQhSGF2IMl2bMoX7f6V-mx7e0AM3WSGY6i-pxVJiKzSeCHEUNUY8EdG5FyvhJly9uYC88Ct5M4v_MSVZ2TzUJt2yvOMTsZHHxwkN-Okz2S8BtRUT547aPVKTzm380V76OyQhudrKAyOL1LPfUk_qlJMNt9xNgT-I3GooEh4DS4kxL3RMLK_OCnHMWpuJWy2jg_2Jf9glmXfv17ImBIUHBrg3LrOLiWVVFLnFnFUINz9LyqG7GMe13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY37NNFiXb5BP_W9BB_G7onVJrDakUPG3XZQFYWMTZf6Anf3Axl_X8ljjmD76RxDEMFlbRtclXHXQQuTFQt96J9Jfh5ALaeCOm5dIbGCKHxesXoRe-FZYti8CX0LejC5D-M1ApzTDBXYtFtme9zibh0flvcblfADfyapH_6vQj-3BJyX-l6OaSBKpVhBJLunVZiGro9UMHMgdf_c0NK9aaBcyosbLzQuW0MzNyYLs2ZKRvvDAw8MkE9ouoLFbbWNxhFMt3OVz-jBj-c4lpZBEk7LwUtHgHNSkHu5nMk-EE0nWXQtR5YddNl7mtClK9eCu24BBjGA9sM3GMSq3izCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5bDyk3Jh_ZAdvGyjLcESBHtKzHuvDTcJwspexwivDkGKmHZ6KH-uY46MZ8ahpkxmp7KL4reqKLlURIDRNDY53SJz7opgNkMmgFetBfGAHzqK8w_Yzq3OORN2RQmVTdLn9yqM3VOikgc3sj8lQ3FyNb7fsxTFobm24kjI2wYq-j2KJ__dz02MR6qkFDOQNxLhoCLvFM1nlRPfH3Ka1f8B2UKsTwjNXdX4H2Pb7yCR3WSnb7uegQBincLXOwBAwus-JVxua-B85J_t_npfhzq2KFXj2jhNjZtXrvENk_aDbY2btRnOYJysLgyA8BC6IEYmHFQzxqOWmRb3dBwAoz4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvUKKPzAptybzXRC-V5cRqGjo4Luf2L0eyetjVDQzeCDZTYcJoVU6lLEWopI9TWLedwUfht59i3veU4tuYpGp7xRe-v1b0tNeM13eYWtbh35LAW9r8KUobPT3xuknQk8mJqRzKmN45dGUhiK8MSnrQTuwlAZ8RbQsLIb3GT7EGt37-8olEmWRS8GwPshou0eQfOoJ9oGUfaDlqJbMaBV2OisGE3O7IXjkVP7KFXo1wN2FicLjbcnk7KSzQsOmyHHXH1-BHLpZrGi-ZJlM8hiAvXQAJoX19D0dAnx-xvko5284gwQSGOToHrXGgJkMhdXwj2F97ayI8hqTZS5yjjRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpZ0xXyuEdL2UixqOIQOszYhoMRgB28L59K-Mk5IKXC13lbgj_UKRDmEvFUW47hw1TbaLTDs6VgCU-9Enwh6A1-7E3y-4glimB-fGCnm0NQzW5cDamhPhpvkmlDPT8Ajy0J4P9dYHHWxUFXIrefFdC7b6nORwPyjoe4NtnnaM_QauheEwqqLOqURmg9-AvIue9SNJW0y_lB0IiDu70TxMMVu68CB6rncp6g4hoD8WEtOoeaILYManJ8pumZNGvZGt9lkfXd8n1jiYNJhA2usgdoBnXmJ_eco37SxDYIkY02l4-Mjh3C1gikFfsLW3Sj5s0Ji8VacApgLB00J_5G_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxr8841hjEgnSWIjsNZKQI0gVlZJMjfDTU8J_ZnFj87Mq5MunnTF2z5yIBo9X6iScyfcneU2Fg8J1tXygmS1r7oEEjbzi_WTTTlA2fg-jRr7XH-7vuAm3eqlCApAMPSVnS53hBXRMXVOLihFS0mjsQNHVwCzqoHFd12YOvm2PodyBpceH1a_5Z6BwmqRmLqjBpxR4RJ8yDngwRWSNgtE_FTW7ImPETTAqxEtkCdW5cJDDzjLF6gYhOFfNStorlNXVKQi1hqQH-pKcWjRYbEF-12ePBcMz5FNIqTOlzrd-vup1Scplx-vIdVEeyh2WwBpUZCiN9RCbmEt9MEUnY960w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGx4Ae09e9qgkb87QFt09rI9GPkPNHDLUXcIzHZUcsyr3vnqyW6VItOSFZMbIMwwTBxBdE8ha10V0UVNWK485tTnOf4-TnPIBwaE_eyPByntg3ttuN3YDmhNH27TfEJdOGZOrd28puTew8E_eavkHydbmNKVAieBGRbF_kNVzpK4Fc7GzBZz6xEiGr50xoRfxye9HPKkT12wNtQwUu1KmvCS1P5G-N6Gx3YAplAzYDYIAHc-UNYSYyGRk7w0rh6ns4aqS2pAk1xgLhHOzROY7q9Qwgi_5eMa7zyeFoeVUG7wz5RL3fIxUAkczENQGaCMFyJpmP9usSd_S-vJz3epUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
