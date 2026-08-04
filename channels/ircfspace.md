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
<img src="https://cdn1.telesco.pe/file/m6hUC8FThQqcevJN_0T2JHoYnATQWM10DdMI7Q5sRq3cei3aoCSJ-t1KQyfiLSM-7MiT1FA_k7jy6GmXKovwgnNripJsaLx8QYxXCYPpUA2YzlXi77hax-YaXIdc2JNba2X1bLCZKZwWzY17UOAi0rVOkbVLE6T892TLotUfC0szU5Y5O_xu6NlVVzvszoD1MwSPT-_Ic-D5kZ1qzBXEPj2y3SMK6Wdem5f3-8bKmvk2mkwc7fwtoHv4Fwjz_hbJDOsA3h1MfY9OimoQAwWaq80Ub8ujB6NymG-uZTIcGsHPhpPK3Iuy4rbRRBoEs-HXnyHDeJaZ_mYogDwIUSaTnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NULn6i6w4PFOqvjPHqpSyhRP-60Gphd03YmLDJJtNta2lCF3Jq70UQi-N_GIUJH04kAYAKgsz02yz0IyVtumFcSRtsZTr2YCvziEtLttfchUOyPMtbsrsshbuDmzpA9DJFv9sp551j534vWzs3n_JRQ1-eGaq19BPhAdlh49XrW9ASwAGq_lvQ4lCtvcHToP_Xxl4vUbn1yZBNGTtANQkKlv3bNg-kWVWTCLa9iELOWcAXdtasdZlC7aRYs2ISBF9SIsvApaeBSf1ZLFIatJptp2kVatd2hx6LOAEQ5v155sRVqzjYBQ3aC-3oXeYGM2pQJqpivfmzZctsbELoq52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbqK0zqD5hYmmxj1MJxxEIqjrDJWZS3XABabV5xrBu_zVfBh_Z4Nn0sGAIINwH9iv3vio5cJveeNE2H4wAxf3r9La7QCvkZ2nLKeC8arQG-SEAZWaSCNCCcxe57JHp93bG8xXyd7QezNpHlXhQrOacYdqIgxTMJ8vSJHEmQr9yFNa7kPBwTMyCKgXTXSM3Yrmz4a8gEXTCTjZQJLWsCl1rRPaJ5hB2dsLQSLOqsgrt2gGxDx8PTQMMM4h1Hp-AsLDIDThdZOsjc3rVoMdu0n4V4UjQGJV_Ii1WqDJmc4Z-ZyMg-2ts5l8VaqOA5GPzgset85sk7YSkRApB7IKWE5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gwt18iN2GqooN08svxct6hhUVjSwoachQxkYIcnaefdVpdiSmi130cxyc-6_aAHFjj-v7wIG-fhudPTpyfzZuR0mlRGTvMB_IWajo-iYmba2jeOFZz1nSfxrFCVsZCA03cQavc1svpiGPhFK7K5I6QHtiFeZV2DDNXsCNw6bAoR3AnKMtcaZT1n1Ww1KwWhcI0AJk7F92nrTk4-aUfp0H3B_ZxHFQhZJti7x4awKLoaZIrF4J668aTQXv7VsDK4M70lW-2vaK4yePe0FA1mU43QTz2iu9boEulUHtGqaCUln7NRIsuTOB4JfI0ZgzRR9p7-xsNdO-7IzmtYitudkbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqM9nhy79UcmJ3EPkPp5MSRPFLhghn7VgcH8jZPUZWVmthrjBoaLSoSCacJ1DOxASLlqUPBYJcCQAwQ_0s8DPaKe4cQIJC3RjV9eyAaByF8VVTTmE7rGR1x_E0JAou1oyDufQT0VUIkLyCUgVedeY2fczySOu9swPK8_pA9i8fQ2oFayxoMQCPOalPkWQvkx1MsiYm-EkAqlXRzcqgcgEZ1NukM4JBuv5xxd03EKKKaz1MZMm4bW0jBN9nxbk_B_t02ET6mJqTscLixGXf0ABVijpftlI1g8uCBJosqPRAnXZozCfgZxB600RvTnbdgjyNTmAllN6W-vZPdwwQUHXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5qz0DNMKaOVHTuJYP46BAYNGvUXZ8Rvs6Ne3s7x9U9QGzJ1ce_4Jbx7EXdS_gkcwsnhYCe9XjhlZ0gENIjXEW330kmJLcFwtOpk9N_pnQZRGsS1JaZrh_GDJRt7Drpe8ns3aQiMQwtJkJiZskfaHiKGZnrBEu4hcfPWWv_mjya8kJHqtQhI7fLfIFNnNQ-NUVbVdVhEbJI7fbOY6bfIWuXfgLs_dhLI8JXM_2RzfSjspJBMRYWTEEbVVFVYqe2GqUlVn4xCkmy5Zf8ZXvruKYYQKEWLICCokc1PN6wKeMuaNGUK49G4pdeBQ0y8ogUi3a7KrxR9040XKPPCFpKRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARsdnCHu_qWIaf-Jq1Q1t9Jn5UoPJy9T9NqxAUR9K-4RZCnR_Oh1yauMm8FAGWVvgVN2YkDicGdPPfElIB9Fe59ujtIvY9FCLng7neNltbaB4ju4iKovomr429qzPwu6EBikfh4Ues8ZUo7V2dS1IS3DHWWXPUWIeB4jibCT2MeMT61x0161jIkf-A_hlZuMeuOoahaCmI1_OycIP_lqMUsmrD0DREOBe8pBapA1E-B8mzxhsWHXe77hzPKRto9gdeclR7l8GNgmcI2IEGa4vAw-X5qqjhfBJxOm94qrCR8-uM19xrZYbNQL0Vg6lnXrTktNjIkV2Be-W4haMIKtzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCFOofunlR8bHuTxD20dGtd6Kqn2ADDMqNDQpPk8YoF-ZRdxAVveKIq6fxjxtEItpvR8YMcfI6Nv3Y1dAbXeNW8eJeMFMe7h1_T3ouFkhZzVoMPcTBmUjPFIdrJT7uXF44849VwEG5JhU8nK0AWHjU1AiMpoAuhq3mjHd0xJTd1fBv5iwv9b7Ujn8L9g0TqiWyU0k2My8nfUsyWP6PwM6uk13k9K1PhWw66Z8QzOSJTplmwY9BO1fk4u-eID0Z041IDblgOVN7UImh0aqxcNKGdNZR5bSk9a9VPEdgWsldG29c5cL6UsFiCWac9wqxOiQKm6t289WsM6biw5UpA6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/idAdRCeLF225chlu9xioq-vaffW2-Yl25iHM2SHBbBxIau-8qTaa2pWlVU_qMOo9Sn19QH_lbe53-9aywQfIG2aocAkvuESNiqu0KPOqYH4qd5ApnMZ-wAcFRu8ldEyHQqgWYyPKrlI8DbMGaJFMToLWlf7_1rjLAn_89IwZK_j3r__f63Ib1DaSonOa_Nw8eDFIm0wc7TrntV-a1dTu_yqa05EGDj83ooZIJZvWfYEq7TTQGGhNA1NS5QhWK_3kZChFEIZAhkT-9Fcly5p2XPrVdCsizeUM0tgjMhvOJL9-GjaYBjY9niGLxO6eKxpOCUF6A3HJWurv5ZXxliBC0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZKqFaMcxDncL1YaW1rRvHCgQP4REXYa2LLpeIrwVJvCnyw9C6onTqRYCKNGK01xK4doRAdRPwebys_0GjouqHzyY9gK12nQTWWt4td6qF4eeuhMP92CwKA0_ia-hNZusdFfTjGp7vdnL_1F6dFdvudONISU14U3U3JrGlLA5SlnOokhiBJb1vX9ZzCKLLNFfSlCbS-zYB6SS3DIGNUDiOdrz7yh4cSQ2O9lStDn2egTCAq9v9WQBHZIAj8FaP3PE7E86F6vZ744ABysPB95Vx11VypkXQF6a4WYuaX100JkQrUdQta6dJX4csxMbdQ77EEgPjBjxMDpgxKCxG6qMyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlpMd9ZnW5D2GDI3yAeOwPl__3I_TOLoHKmcelmaaJUZo168RSr_pI3EnCEsreO6X13ao-hZaQ5tFtYiOPB-4QQ9CtFCr1Nx2FKyrUeTrNE5hQqY4Uy80Rvfb5TjDnhPXYrNf3r4I_iSCR6Hzk5YFEzeQZgsKKa30X4t5y4cgTzy1Fx9R9Tbb1F57JVA3jDwYW3FU6OJm5fl6Wrkc3aInMx37WF7JlkGGft5sQ_dn_ts_94HB_BstToHylA_JxCUBa8ag6l_6Byx-u6TzaCAcNGhFMqbTEeZPb2MsmeFO6HD4JONgE030SkjLLeauqr5UoNwciG_IbhODb8qHaIGHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/emzO1-NGcqthb8XvepossUPTkYqZejxG2fgDB63xiUTn_fRGdovQZeblpPQef7XX5XvcRqRQbKlmFjxkzhxz_u6lCYnEadabPORJygtmxorSsqCck1sJb7hdJ9CHRERqgdy2epFdSA2-ZwVtZourz_r8Iep_paQYcQGZgNves0wYgqT6htxF4qrDxMcp9uIiAMXWoAFeY65p2405Nzel3MCG2uaNZLGvPiEex-ngqf0MTeWWtiTk3_4Y84pS1rqAajuKC9J_i_FvIJrvyfVHp2u0Q-OZpht1CTTdf4hK7I71uHD4IdfMg7pAF9h2I7yA7V5svcZjmgyKAP9-uPICUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ie8vqmX1idlVou37dBiQL728C-KGX4BpHnS2KcmHATIGHKymowDok60JRhgcTKrLvhGOKKecdNrHzYxt5YV7LVtXuDlulwm1QjXRFfQbjQ-yStLUIjbwpgJzV9t71-ILE1FoqMGk0LQb50_XFUIVP2WIG2TVilVF0FU5f8FYaF_5rIZrtQbFaiBUhtOzFti8vMoguD3933Hhc0PhRe1UUvAv5eL8iVhCI7_TiYfkDF1LJq1tX2B4IEM4rXW10uVaMJWBfrJAjsUAA_2o3dkz1HJGqiZqYMY6HdF5_OvXNxbnDQtV9rrIasAa5w9oYUya3sEv4WXIr3Uiv1gUJE7D0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mL6n3Q8ZKQJFVHlCdLQOMVvwiN7cUf2-Z3kZsOuuxhGQ5iTvE47sZ7nR1vNBVz0ugDFzWWwv8EjTODRqTqKcBDs8xQ9vhyqHRlivnkfXrHfdpYQMYt11Z9qSlQ6knQ4p5aGwOn3bXwRGT7Gd2OyMlC-r1IA2qCATS-QPUdu-7qu53qzMX6dFgVd9e8T1wRyNQFZ2V_-G6vo3KC2tau_bCxm6DSIvSo1fjMBYXoECPKbtCrDbzNrwhDDgSibNyuqJbxZ_Mwfj96Mex1xxy_MFd7qe6DZz7oAETOSfRAngmTVjyx7ktOY6in1PRQhuJFmZVLo7FawwlusWzE7JBnJpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZfTVsAwrE18VwMT-MvjMOs7EcfZjdhHb1QtBST8S3RPSvc6kjji2ImUmZkwBAxm-TVL7vrCcw2vDtoXKj5jHG9icP3EyQ74CZrM6sKrlmk2wDUxV6xhc5ZTO7AGt5y5UhF_IMxRQECrhEg3nqu9JyfGCJjv4mcwftPJuv1J-NS7RF99bsW3e4PBl-osEpwbMwWTXbX81oNfrdSmLLFCTqiBGvbVLP89QmgpHfHTP_ERbBGW7SXd4iw5jaqodlf2ck9mo4pkahvesTYQDmF21EAO8sTAh3V4xKAo2khkTAlc1gJY1Zy7iB-Xz5srDRF-k4cBs6VwK6io756bR2xpLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nu3TazYH7ASqDJNAMopS9a2NLnX0DZg15HdmUF_vMtYho0EU4w7tEHtq-Vx5-3E8UH0tQ5ze1CGcgHjbsORCJY_m5KlXwffSAQ_R0M06yfISkionip73reNYy8K3HEVxHj09WwyOmdhMhl8k6Jq2-7-Bdz7rU_JA5vO5Tl5RrPbXGGT_0HsCCSvBjlwO8HGdaf1mKlQ6996Jb63bTl57FNCUSsjKYpV-rwKYcegaY2S1ifZ7LxR1hC8OdvQHlM6mFy9xNAQtQ-LIHl0hbFujnVrTptXkbnL8QitU0zw0FX2T3-spd2WIPYgp-gcmKLl51pN5pDcQptl2fXamuS8WbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQ45wQs2ve3Ozzej3YJXoQ-8o3WvguYVBAvi1xX8YTHAuPT7GnPqQUTbRrxxVoOEsTmnfqJN4bttxx43tU-E4QGrwaZGi1FjRebiwHcvwplPXm8Q1bV9PYyGzCipEaGIH9Q0b38Hiea8gVUQcDoQIS8V3_2Kr_P2BThdbT_yQ9OzioZjkp75Chc7yfYNTvFUH0wVRak9vIZn4y8QvU9Av3ZjR6c03G2tx85BmOa0EODVpGz4qcJ7nCNd-_36cKYOtLgbAUg8cvwgFQj9Wee3oPGVwPZ7j5jr4Zp5sMd4WNIQb1D6-sV5imChPz5i0MJ6w53xwGDQrdeGll8yc9VTJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aHkyEfgw0-tpcsQIE92SFE6otMjUILl2KHdCGXVYNwiibW1iHiTR6y38ZvltpJBI4aSUOfibsDnAc89-aWg2ACXM4twFI-nXK44M0c1Oy3TyzyUE3yJ1IldF8GRRq3S-GtYcEDOBDKG7tHSLo84CkDWaFpIbyL1iha5FtgT-gty0GhvoGPxs5FuL7l5nVA6_9BeKGuG8Cdhj7pYfmyWmezqcVc0EstbPEYVwLQLoHPIEwTlaUaYjtt1brKUuqKndsWAIzxV3b5qwQUSE_8MY98Xv_3X-XCKExGb9eRMKd3fyHOREQAlKTukw66-lZlkbSy2i7Hp9L8fgBnDAeAf1mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gfa-WFIFmtQFYQICJWu2cGqp1F5kgE5b9GlYZnbFT6xrwLgzPNbK3nXfZcjtzkBAw2PtLADOoezBebcskejiz5A9Gb3nrcP8Q8N2iGJ0rkJKa_ZLDniAkMXDVZZuP6hU9tsiz42qn_c1ldWdk1Kdhvm61KlYX_In2bEln3crS2DhKHkAsRJBMRuyAYYFQfKog2kAA9LuDFd0rWzZwZ7pp8kz4kH2l2-WIsL8TOJ_04J56h4wwOZVwhQBRnq-4JntBl5JBDK256ezLxhPvuuLFM9khTcfDCYVbxOr6_PKVqxQyAL-CAFmU9obDbPaRRlQgdfK4W9XbDHUwv_xBXjCMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YmJezv8GR5fLmMd4BA-Szmi3Cxc0EmwIeixSo0GIq-PY99S0pQhLFEceuenO401bo7PPjsA2oHTsJSlUL9-ZfDqiJMZ4_a3u02rcLYjN3VdUzbAyPTgBvtff4ENHt5Gqlxl4o1zBPPy-sz-xL5zAt2JEsnp2BqseCBQ5HKDXszul86WqW-CFQY1KWAll5VBV6VTHn7gJ5ac8ZohhRVRDNqQl8gTWJ67S5ZovxAA8h5EeZXGyerjSzVySUVPpIUMOK8ISqWGK4wYESgi0Y4ClxMWZDLwo3MiNr74oqIr_u1pZb4Ejxdlm1rZa9UB_Z0bLuc_vdY5Ux4QggkwtqeiRIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MDN0XmLmJl4SINaOM_g1s_rGuzZKLzJrV4RYi9VvX0fOhpvLHp4rsbgtO3_bQF5mefjULS6zOUB35Y1zyol-yp4QNLi1yA09vQSkm74FFkk7ipEPjve5stj0roF-UVB1ccE7vylxGceEY5Z5c80dnqb1suvWWx_uum-BI2xTeD3NBd94Pfc4uum7E6k8b0WxQpvj96y3c8MpxZfzfeQxHPNZDLrc0ZLNRKLqLNGy_Vrvvov6MMGH2APglVOYDQ1pRSRbxIs_dJn7FIhQOm0Tf2irO77U8U5Ra4j3so_B6aNnefFr64QHKBP13ufEMZLhyj7cWAjUxWy6kbfuHbTEYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qaNELkVrHRseXo9W7lRzywq97BKfiZS3YPMRCjI1YdvSlvzKMhvZZtxTm681C9D8UFtYPsiDc2WuT9nOPEwrmx-pJ7HE5y500lAs4O2MiGLBkVvwQLbglI2QIMxU552reQfeMa34qTXeRusP8KfrvFBtyTdgH1IEtqmR8Ge79VEOj4mBpijdw9PTBBZvOyGk5mH5tXiiWCHuU5j1NXd8OniNJnKw7VvWTvGHhnUtKYxFINM1BVt0Y2W-35jo2ocq59Tu-wW-uk2xkoEKWogaah-pc-w6jSt5MzHFbEvmXgreHMfJFyp6zD0rqnlEn4EUGgusQJ4kxHQp5MnvIb60DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EFkyknvSWtGsAQ5Pp6F1MpJh_2ETLsvsawthREnZlRBRQbfQx2IhEs_AfKyTwuzXj1qPi2NtA0p-83NEJ46x6Gaa5Y8V43ZlvqLQx-kRb896cDz7UvukrTuP0pLcbdoi10sOy4mnMZqhmh89H6_QPFMLBcJLkyGBNMMk8l85Sp8LYucA-lg-BYKAYE_RkxdF94JZFOldZLdaVyfYStRcxXVPLOrcUi9GBAN13K2uyZrt7kk4I5_j8qicIf5KODrkXpKofplsqTgd9ShNcVU1miVcf4h1Jjp-lfEh0__GDCAV9J7rOzIdpCy-5fSPYXpFAsCZ5Gr1GcPFVy2NWA1cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q4kmSzf2O7I0pcIWGDfQEThjI7RhzoY7nIeMz59UFrvqFDlOmj6caeFJnn6BIrXxYXtvotTqJIbq2wEbFhx8WOpztl5hWKM-Mj5cQljI8feP9K-wbLvA_m3gLVZjm4q70ZHB2mXuRAyHMg2hjB-S3ReQcb_LvoXMvcwmF2ytV4DHUf7GBEQ-QM1H3v-m_e7ePQtdz6uTkAEovwMDXTY0l0c_7x1q6DjSpYfiCTn18_HBT_sYViOvsVDYVmjKlIMDv_UmwA4AptHLIcQUN50TQ66E7X3KA7O34ltp2-gNdoaweyyG50XxkqNsiXCeGcbBwCMePuTCjW_BH1UH8NvWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aeRX0OtCmUGPy6NAoJUsFDvlr6_CnUYMbH5_lHKGVLD7UTE8Dpd2eVEyQQxtU28_UomF0m0ychXvk1ZcLX0pwxJURx82jjnu7YFFHePbkDL30l6gSYvcisneYh2NT4Sm4Dnio31Bk-2CXWIWNq8XDKkb2AhA16MprJlaWcaSQNwAvXPXyvFxohdCiAII-UaJNhipK8O6xuxZH9BG-wa4mqyOKQZG9Ena4WO27qTRqMjk7Np6XGvR1Szah_uw8ku_dB-Qe0Pm8oIEgKq-K5RC9jvUhVyF7J_Rq-13fB4rLMxQDdJvHkNBdPgJgBNVayux3CSFyVHa592KTHIlMbEtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vYjp9CHczydDG4VTQMToXHcAgTTT-z8EJIGH0_WYEZRso3HrO2ScKDAXcdNDYhIlvLZ1wBhuqyYcEWnxNUgmcJanQ9IjSCrSo9rVVQv2yf-Fq9ryYk2kpzvMzwYBRzXoiFH3n2yQt4DCzA7TPs9_5PQSMFJupbDxGzuM7-_cIKH7xUSkNwsoXZnavpI3tZphjNMyWg2kshg-l2Ty1GtddoFx84G9SIzToQu1N1JJWeGNTVArSjvmqOwAwZjLr1pcwEJmzgNbm0cZu6Varx8PPv5o6nLOlm-kkiOLHmKP6CMLj2wvlqHVIxuVMD81r-nk_z9cwyz7hR1iF-D1m07GbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TpuvlKIFqnJnMmS1_tQ6Mn5Egi7daEQGNaqBihW5RFOOXP9Bxf26DjkTxTEJ0bEGCrY3yd454bEVh4-OMPm84YEp0qBKkTReeDYPj5cVH9NSFPClfbp1UyZXOIvaQT-ew9gTDeXk7dKzCZ_IXTZb8fe2twbU5Lrkm1z8t0vXzQrdzhhwCWFOXXiC3wIswuSu5gC_30OsnBS4vQR8vS9OQ_jjEYolxa-xXDX700d1lWZLp_-LnCkyDjcXZPDKh8qSzouh6MfRGb0mxfeFNYfc6mc0U8P7v2h5Jl9aQ1DnzPPM7RsEM9tOLfs-2QI1JSKbPeNlbwD0f91DA0B5tv9Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDAaTt95hKwOGJu0hISUcD4-SjeFNBarUbBB7XRrsBBmU8OX9xbXRz3iN6W_L9Od6CWdHP-MnOsvKTaxD8q6Lxj6IgrONe7Z7mZWIhx9uRcMVo_siOlo6FDI8hlLViHiJXKib0Enkt2-KQX65X-qTPxoqoQBNaTUUBNFfcIn7g80-nD1c76SAAZfoAgPtQHaizPFo2rs5bQ_TDSrD6EkA0CSwBtebbJlDea9DHMJh2cfcpY9KZntGCOPSsLjeW5duT4UBOWamb9C0ru9Fh9kG8ahW5lpl5WG5Niri0SnlxPLT-M7G6kg9PMx3zz3EQkHDwLIINXs4jAA72gXbr43Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDS6_-_Ex0quTDETLwnUImhUdI6Fn-F9Hvz6Xoj6JJbS8C6HRVIlRVZNnt9EuQjf8gny-IJaWetN7lyCZcHYezOblXGC9B30691QdtCOLPEHW_yD5BV3h842MBhEPQ7EtCod-cOTd-NINZ8X17YpPEAxotXJK_XuoANC8r1DFXfqmqc_9ay9wXKCIZG_26GEBGHLjHE3blmuQyIO-hDoM-QE0CeOeGeEKisOgsToECXfPjNrUBKfT0bhCqnayfqmrgi2VkYvcPCRtS-Zm-CqHy45Gj196ebVg61iDH5vGtKS_5ltuor0zLcPHEfVILVhe31lenA9lsNVh63K-A3gLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyCmD72Az-xyeQbbiw8HUxTtvK2DQZvTswEWyDrQgtEYXLahKU1KIEexvW5VRC6HDuzKavBFu_P0jpXmps-sjsgWM7FTx0a4vZQz7pvsFF9-U6MCwSl0qr4z53VjXDS73iZHu0fLc1ronpnmrxBuek40bhNV_wJoFR16Yu1tRCYqBHQOnWEFF4ZwbyZSC9Pgn4PfVVSchki-rg5WUMlIEwOh2ueA4amDYZzZJ5l-oaHoqjRymhpal5gnS3VR9FQFXhO6GRq30GviDSr1gHn4W-j9TuF3ht-InD6-PVL4MVhZkTous7py_2gzh46w-iMSNQMfzOgPG6R4R-Lbdcb-8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4cdCtK8iYeBM4P4hsLjMfQxmlEWKdFj1G4reqJV3deUjIb9Nfl1Wb3K8O-rkoP_mjojaKR1FiB_CjAcYkmkuhzXznVVP4-yV2H9b1avXNbFGrAQ4Gps-2XVvQIz-Kw3uTy8pvOXghbkLMoaO446xrS7dZTNCzto3-WjpKOiZXoqyXXl4posC4jXcLNpAuagAiZxEX_vX22Pnd7bu9nm0YwQbLOn9aCuU17243O6nzdj1HwJ82C95RQiWTyyf1PPzaq80ATqzi0VXAwb9P8nwP1xRU8gkQtzTZ_jH34DnoyGYrUksb7vsraNDrPn6aa9haczB0IuTO-L721ihsuq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8YU9uqfKtkc8fMgNGXHNgyOT_jJE_twIbTYEeONMxRhXWHmYrLyJvElMuuamPwYlczkdbsIxcv5qyrAAm8k8EEyZaeiZ0rDgbhAuMPMOyyrtHt1l-2UdOayVMNVjheQTlJU9s4UA33-El9urtS4KBxOqQN8mIFZevJ7X4CEBYPIgk6mcP3spl71RxpQFEDRjUFMUOrWDDTXw4a3r_Q91N7o_kum2_n4WpmusGobNB5cHGExecaXc-9AeSe033qnWISmVC7sHnhI-zbEshh2JM9LwFnrDL1ijN3tKhspIt46IAleVrD8EMtzB08wIi1Omxtu5NWskooNJDofAeA54w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IegxckcejopnFlaT1K_fM6eiu5B05oJpoURGuM8xNfHzf35zKCHPSgWqiQNIVUTMx5JGPBcrRLe9igVFaI2RO0lWHGZ8cTtCFnP1BX3U2qvRmOAdRClmtc55BzMe0fPsxXq8kh8CkeUv1Pf9tcjCuYMzIsWP5yxWTbXv_BH9bGo0Lw0dbfu1vAjTszPz_1qk4w6FaHJClgFZ6KCAwRvKSJo4sPDV-NN3h_5KWr4gk0PnmN9srLnfIAgeuuX8yHq49O2HwHdWEzm93cC-naU8aajOdO8-aHKLlxjwSMadGBmJfhik7T-C3zmFRFJL_77SdboxIdmRFcuPsQcX32mv4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dlTrgzpYNTETDSXtTbEFf3wELSCsG-n_U-ADqWwQyPJl5vQZxUkUcpa8Za31yA44zXfmIDs0-_YijEXKqo4MQA6VxzZsKpqTpSRSPyciWrnybUEBMt3bwfJ3v2i6mUKn9VKUOxmlAE7irU5RLjQ20F2gZUiutigcBIxv5qUxgF3cgIgOHtvT2SUInaH8j7jhKcDsW3bu9XDgGRb8M6Cpc_ztq-TsLwltbsc-5yaOdKxE9mGvvuUz4tlt5nM8a3BDrW39ciqqlHyTAazHWC8BW1xL6hVu-Q3k8PXPKytPBXMLVzLb-cJ_RZu4hBMH8nmSlGgXYJLD3uobya-nEqoOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n40x6SqLPVCkSCu5sYYjVdcqiBbmjAsI5yslAbeljW5EdXNVDBIzZEpqR14YNuoCpbIZhWy-Jz9hLEztSjxt_0sbuP-D-FhMQUsPofd5uY4Y6raAlu-0_brmG6s3xrdFD18vZ2GRBwsVHWs09QQ_c3cJCVQSZ8avT4Ktwu8IVDP_EAM698XcV6K05PUTet5WvYREAQjSs2TTm-h3Snr0DVEs5LxvOISxQn6uiiP0fpYA9hfEHnUPFjNgFLDAIW8igzQaOiSvok3L8g4VduThruEW-kbQ25OZmmrHDRBDUDggANwMxzkm0ehAFw6yI3qxrkptuuoPigN7ogu6RLFefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1TsYyPMhaSZ5KIdurS08f607O6epmfE1PpPR-Ar2oIK8Ku3BR9FYQ6GPv_Cd-P-hRKuG2tJbqWG9DA4AukkJ6iHmc5iJEtqv2aEnW3ZAAZL60VjlJoJ0-xW3fph8FTEf73sWkf0SO-BpGGY0rB1A9C29yru8mBdkvcA0FddK_BUXP_jssgon4tlNiWz641SDAT5kis-PbE7uSWyjz1wSYdR1lGJhQy2FuYfYEZchSk0JppN4erpU5OOGVaZJjHot4J9DQaU1vVLwKTBPvFvMisxdBPId-syv2AmgShSVKKtw05-SZdhPKDdO93g-mJObYnv5-vz1jpzMFX5PDQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WyzkauxwlUx9muUu-NScstlRIM3fdXraRDs3MC9JkfLew4ocahdby-ZNBUjgxHRrTwaXcjPWqOCs8EoUrRIMO6mOfZTO_MiUC0EPruCvolSh2Y89s1gXeW6D2buetzDP9aEa_5Y0FByiC_3LKQ2nDUoLEe0B0K8uIBZPg0i4nsUdKEBq7UMvki5LN7ka6zQSurVzhhqGwz2Yh-jLff1YtAgGZRX0Z7GZWG8mXE5Zc8kC3F2TF7jY0SVF7zN-Q2cTY4bQTpx_oJgkz6dxZwlBLlghu1P-OfjZMaYz1vVZKdv4LO7f8HlBv67ZC6g3ddYI7seT75JKcNwiIj2uNWIXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8aemW0A0EtnroMWDDCDyMMx-Bq389k5ivgY7Jv4xCpHS0R5DBxsW5K1d0xWsjY-FVDbKEqSXqUXGTFtCZHzoZr-WcyGMN6ot5Eh-Z96YoySSohGo8vzyVTDMWQmLVyT-INP2VGp755xitmIjoSmuuGcy3AvNSwvRyc-SPT3CNi7NN1hImMdDhO9B1nPjmtK20XYgly3T4uWE7GUHW6ygwMa-ZOktKWREQbMktNZgxUu5PoLKMzhGrWrNImYXh4l7hW7EY4eEo-jzQfabDO4z3-nhkmgTvT-X2-ejFuVhARKUV25GgEoDD3JA07dy3u-zzaiVfEJxm6jmJflDmtHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRAbl_K-5jRu0oCyxhPXAOaZ_sIQUT50gT7D2GKPjKklwuqYzh75eT7ITRZsde7H0PGL6XuRYWTxWnq8p-kOVSDUQxEVSipJhyMW-UdOUxg75kZ6uuz5ycy_-nGxNUjqAJtX1mQrunRCmSi9rITbHf376wh55c0jZ6RhsUmZb6NwPSdpRsNxdxQM3vvGmcmMWw4tpJt7Cvqn_vf5ls8O32TGfYlpLgy8e0l_Q7UcWzRFg3zV5mDKW8rYHsxy-IlbL-uRZ9jfkBBn8RBZTIRt0Y_-X5Tjiew5RZcGo2646OSLECrqXWcu-Q5EVMZKxoC-m6lUipY1UmlMvEOEUzLIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iyt8l5iUzaLHGqHoK7WHszoTL3YdlhzZNmA6CW3pBtXq_z4wHMO_INfWGtDFGiVIQxaixBG81h_EW-fRAaDZhF28dsddHVuijim8uR9l8UWNMSjzT_nBw4z5afL-s73tuhrQnmVDmcbLlbqOw4UjUYX8vLDQIspYEpzI2uXsUjcGXRKrtxZMqjjFbWiXg7k0-raIHuvDP_bOcqUOKUiwZH36UGON6FbSjNVvSWD935MH1PONtaioKUskjcjdGw2pKz1WDOgnOmqZbKqNL_Vue3P800K-QswBd718BespLsB0GDM1jWouVdXSnDQdJc4auSehWbtZWs3AyC_i5Y4TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pq6HGrJ9JwD1Fsl_s_l_aikfEqkcOVkBBvVpahEr-ns2Vkx7YsmSSzMvf3x_2qqb8EQevKoeHFQjQtPhKXfG-ZMkei_ekmSMFAA-K34Yds3YlRLbzFc9hCws6yDPOqqKHr9W9s00QD5USttjs7TtHbvRl7NxObaGHYWVn-TqXaZRuyLS0JFpFfL9dkTq_McGxWH2pfWMrbTKgGGbH8uhHDyta2KALhiZIHaV_7U66PBwJHvjrJwiQTzB-d0s-nv_RxbsctLV9_UqSDZQmOeaj5dKLtRnAExVe3UJmIek9-e233XmXgMFQn4H_3YVIky_oQxY3Bm_Ky8DqTNkUnUf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BU6X6rU7E6rR3wxMNNA5V6IEJx7Xv4uSV45LVmIzZ8Qp9Ql44ANk85SQAMtwtTnX0Qkh5GOtZDmJLR6JlNP_V0VHwA1yFZ8zeq-P1xrkeKVC1KQYpaNpcoSpVRdqmPB3w5tD_fpNlmqRaPx_k5pYZRKxnsAZelLZ4jr631gOuK2OAhf3ltQND4ss3LNVhIQJWygjDjQ5Bxj3LfproRXo5iK0aoe7GkaJ6G7n9-0rZojDW3gs-hWev8suoGW0ap2i1qwwjHp4_YznW9z1xiMvF7deGEbkdd31RFNhsiEk9ZApDPusVUKiU0qFadszo2QbE1jVBcG0rEPVoSI3nH84Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TgjTAcDyDlt4F9TmQJDtt-vjtk3X0v1GVVVM9EFguiyLqm20s_T4MP02NvWyuYDa9a-FzPv0vmNlK6UWZzWCH3mc2zPeiK84HxjDzN3ZPcJnX9TxPTYwVBiIME2iPDTse56RZHEhqWkcUnBYBCtaFdZjrooaD4M2w8qLFXVF_2a_TCcZakMW5e6rwFPxU4BpN_aBop2B_lhb7LiFVq_g733t8K4hvopBkXLp3bvxaEMP6TW5rCq3Is8qNUNbsOiEtJt9xsPoQyamhKqStMvFe8BX2up9ypUo73dQl2xP03cLMwVx4fB-Hnc4VzFXl4AFXD6N2TyXKFKlilc3kUA8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOTx1H7NibFkzSI90rXhnkMCQpKbUB4UXjaDZnLM5XBrtTXtBpFfrKccoK_4RSUEHizrKQ7P-Fkd-qTGiGSMoKkEWkBfosolYV0GSEjAFDHMdPaFILakkjm_EQyo8S42Z4Jkgdaq81Gn0Va61gjfH17x5plyMhPhi0aNAfpRiVAPGTCSLk0P1xpcdCzo6y4V2995y6sUoOA_NZvqaIenaT3vRrukOubuObjZwK8KRaqzU6e38VCM4YootReR5A1Wrn3a3rlyD4IWF5QlLuy4YsU3ZnbgS4LD4YFOrg8fXKs3WdnBuR9QYj-v4kNUcfafNF5-CS6Rdh_uWsJHvtuqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tPnDteybiOH7Hvjd-5MizAwNHLFKih1AhqTAlDStq5qs8zLhTq0kVFER2CCDVJ1RiZJS35UcohSNlW_UXEA5muuUiAxk7O9F2K64zaGu4ZnsUe9V04Fp8yE0gn3N9sBYnA9SyGxiKDZj5q8CNGwGz1_JzboxpVTdfRkoQCxWfkZawM_N06j1yGZDxeLtYaSCFDvPbPnhQgPP5q95GYv4TH4UcCuY4fvdFOtEsY1po7XUnUN4C40j1t-9vClgwG32LwNYv2o72FXeH0vgHa9Z2JjLUP5TJeWdQ0pZOTkbZkRcRdNVxp8hIXKUWz_fn7HmlzcLuJ-2U2rNig-iF2Jwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lc61rCyi-dwEygsh1bEVhLGOKJr1YpCNuTUFzydA5nyF__TQwcy55G9XXK77J4sbQ1Xic2OT4gKVG2dexX4QimHAr-YlNguHpz3dt2fmEfxgleiu3prDsZwz6Qn_v7qXfi5dkMqB0MsfC9-B5XYJzWIkp2OmFNH14VmeosLUSjsjVnIQB6zwsjR2CfkahQZLSmvDA-_9tzOyh4IGZ0FvU1wendJEkI2flyhZYJYC0X0W8vg9Iovhn1ZFjFrmZR79grqs9iloV0Z9-9Qx3WRun0_V66Lew8kiwx475d04APn-yblowN51b74wMI5uyFtlrxzla-hnNb3k_28IhVdMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JOuiHW-DTHyAnl7x3z35rg3xUZW3rr68TvnYaffD09AalM3jjG1mm94iMESzXccys8SJzprRqIdVelgrjMk94bcP-a3CFqZ0PuIja7UAhTyO0OF3jvHfgk5Vk0cXetI3VP1NH9tYUxsng22Hgsr1uAaMjJE5kwQmRUXmhE8XRZ3iZhLw3Dzz5Ad0gCQG93B07SNopu4cIHGxhHdU8CpYNwKwirQ5efPY6_GMQ0E4bMfliWpxCbUf_nF9PIbDUQ9Jx_tkRP2EIVx_PIi0VrTDYOmJSwt-6Ygc6HJgqct9vge-YSLJ0sv9w59tX48IEC_N5Pdhs20kmdNck2OowIZs9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5b9O8syhb0jYZy5pWgodvYqfEhOUkBQESqdwIRj0rIRZHSyoqtrPPbx3uxOqwQVVidRoUC4pgeL6HQRKMuywhLM05kbKRdszxDRaB_cw3wMfycKmI9_-Tt46_HDrZFllDO6xXZHIL9peVIRAdSI7e-1e6VyU7ND0lc3saQSoXj78xVDqW80_phHjP1SvEps3YrS_L0QTUFT-1Hh_pJjAa6tUQUYW4nJfrcONgR6kV2rKABK1rmzgzye2ANzHaqGCk3-Xsvop6jw551_-iaLdV1kt8VWw9NBzPYTGrqFQkflSZIzF4-MWZ-pg7QUhAz0Ny23qFwkBEbHTswnv5KZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUzlzxQN9YrYiWRIgv-7lQMFMVkC9gtZJij3UBsdIF80NSx-1pgbzu8ljKJPwB5UpFdGi1ssPs5q_bgsrOap0X0G3X2j7ZnKHOWEaA_HhOF7rk76C93AYPFCjsv9FW-2wHezGiaYhdcw-qkdn8XnmtH-n3qsaDQxXMpE9qzyV3VQLNy5CsRLiugXyRZGFtc3-8pfsvBkc-_8mZAtq0X02QFXiggx1AATEJbML_9sukgRZmZ_5u7I56UarQjAB8_xH9moE03fd_2IETdeZnyotn-lOq_ytN4Ju9-d5KzIgOvbNzGLqcf7p6MRg-hCLhBsUHB7tAitlC9T9PqBWvd0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkMy9ubmF8G7U7J4EKUJrJUT1ktXhHrdyzdK2GSdE5d7uUOvXWt-yJCSse1oqR65YM50khWDAMV019xx5oFzpUy2cteAAgzoPdzJPOPuHzoT4UKA9hEPL2T46PKKJqC2oj0IaNfQdVMijynTSfTD6NTC_8HQmtb1fMZMCrO_nItmlMTItQYod0HKxAKKWEDBJM-gjqLrpJgVFWhpd2KPmOt8ftiirORt2exvoiyNkT0gzeRL1Li76cVr2zpXLt7nqExpNQpLntSOzvDq8szwhBKvwOXvgitXOyowE1O31HT9YjOq4NymqWEwNs4fLGSStrf9BLRtOhYmcjnzmRCFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O53_Bum91Wo-kTHEHpEiIKuxTyPGoMc81_UEChFFJDcSWc_68LQ81U8DRnzr62zre6ZbMBfW7d9vUxMqHSeBJ_dvWnjCCAwcEYquasCAUJF8Oyc71aN2O6wF576expwri6Jj6xvG4faBR4ak-gov0yJDeNPrUtmk7Qvkyjhu_ySlT2mY0EZH6p-9-xUkw-P76t5P3LYIPqakojVDldxkVyj3Kn45PfVueTcyrGwmhC0FnniXP53sRA4OIbWbIp86CTdRtaSq1Krl1ZR8_tkUqTOArJGCVXAptR_TBQrp10KlEhEGHxIwdQHeU14axKId0A71HqxEKtQI9s6ay0Cxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpXUEcE9924ueVEh89oeHMwLeknjKtxYsn4mLRG6kiBBI2grKpTOmLH_wSPhiCPzoHG5y1s_9BL5IIB08WLD1-7VbgDF8BD8qErBFylabNFkH6L5yr8v4REC2f_us_oAuUE_JA79zCdRUNyQKe5Xg6MXs3kYA-KUG1KM_nxEON3TS_8SPlc-_z16V_-U_zLnBTOBYGW2sPLj-kaQgSCZyH0IeyyLNg8h7zerTJm6vLqaBCdgIERCyS-drk9HEWMKeZB7MLBS3M_xfRhPpBInniMJD5MmhWCT-X4mQ5mwj1zG7RvnhBEHW35imbQtu6RE2enSMIZ7z30CaoZ-Ta-bbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GyL_9vMIZDvEPCTD8IsZFdkWbtSLGjEjOMFdmZ2W2wpjRtK_4aAMut7F1P3kKR-ehXwsTIACFJJzIoDymHInYynJzWIaxlr69jIV8puPClSuoMDwv0EkG7NBcxYHOPAyWEhNiBzLUOHEDuTs8Vmo2n57CJmAYl8xjLfSyo4oAFU7_3pYsD1-tr9EBDf_-MfTlAkaw37P8-PfU9UqTKxgflSgcNesJNff7ULA1-zEK3tLudcO98Ochf4S6236rlDVhWM3ob5YpEnEMbFeEp0WHTgGON6rcQH5NL2FYu-cORQSsrV5EAMRj9kDbYtaN92_CsheDReqVcIovFmSeENd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjXis-eandIUXQ4CJ7zslPxBYUgO1sapu2_kkC4Dgl0F-Hbg6tPn1P3YHQBekNdfZ1cHnu1J430RRUmAMigGfN51pIS4Ky1PVIQz4Vm1GngeTE70aSZSu2QAE5VS-IXDBMEB5ZMe5byx1FNqrs0ymNdFsz1sQ3mwfNHRKHqfeHT495WbpbEYVaQeqoxYz6v6y9vnkOhimfIj4e1hKk6SGH60U3Bk0SrrVgsHaIdt3OjELE5TK2Dedjmx2IDIlWCXX3n-n6Fd_8amhT107ZDV4o8sLw_tqhZaKMg9LCwgckvDDlqn4Y2ZzM85LQ4TRWIIOq8r73IcTHkT4hh-vpeHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WNhqoInfTyL1ZXb3TiaILUqzIfJ1H9ZAls7qS_JsdobbHPLJrIMgkCTJQHxhoLrv8qWdJiUwtvMp0aJbn2rocSSTKpXlsIGG1mbZuAfN2LF_Wzf2Ozum0_NEbvWJ17U419jsx2BRV43SFErpt27Ngwt1J3jI44gtV8Pj_OgaNmaKD4fUGZsAPInOyr8Kjesvdga1TEGcUAaW1FEaUoHcRJfMIux3MFJfAAoYVjMzHIjvIymnO6XCYpWALGLbPLs82MjqxnYlw8mgbwDmJThvVCv5vnSLxOhXbBw-VTLKWarpfnBFZ-crwOOaiUi9RbZbRxlvzOHycWuyQlgd2TCDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KQ9MdPi-pEi4jnI5YiamNyUzk77H0GkJcKqG7-sU9kyhAf_lU0ioW4K4WooTc7eKWs6UgM--vT5ATbqO3SNWKIfw_RFPcrilPUBI7-cY5nNUiE254cpQgwQg_ng5N4aYNVX1BXG_xrIZtZmUHPLzH5LYvMCjFGDcDzlV5SuRaKlDQrdGc88gY3N4BQIJxwxR8VUg7TAdNVDx9mj41hMErsqFoHjcj9eH2z695Wqy8LOjl0QsOTVmSBB4UR3tc0qVt4y-qfJvICyWAW5nY84llkD5gVG2eTvn0Q9qO9vkSNDynEbBnJenCk1XNch4NTA9mPXB7TnPm9yWVidKOIalhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i496WltrZQQCo56h9jxtnWlxXzv-xakZAmliW8CKqoouxel5wXSKE6wo4jK3gS7D0b-OPOmo_PH-VOccdxzzS9Zwo0Rp_1SGkPOvoasVWGKNEC_jWJygvvfwD1hEi3l6O1IUhmsldhf-LUAci5kbvMrrcO87lF_1RH2ZeYRjjFxXBR-gcgNpUXDH_miZE_oPvkLRWnl_rHoMcce4BsDtJHkuGmjZIhWZQ_ou_CPPUWTNqbxdjitMt-91D4wRx8gweWqPufQL0PNsJiFvxFu9wnqPBVM938XwJxuyA7XIHKIC1ttJGvgwJ2LhZ3b6VopQIp6zVHPosF9FU1pJLIj1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dUs7xbhIMGj1RP9RIMPHSUeJqjCLlYsK-wPJLemK5MwB0SfLi5mPVIK_uSnZbnMIUw4dRoixwLNUI9E-nwzpRRDg4eU_Qu5CfLCnH1KetAOYvLUxiNwVGdyWJy8gOMNBU-XIXqBMxAnKJr6ayfM7_NCQ5pYpPa12XDoymE2eFGcoHkaUN0tNGVuZRwQi81y3bv6D_8ji0hhyfLrT1OQ1XyGVqtmmvtkloc4CB-m4XG1EXBeptMUDxa9X82fkd5jadTxZWzjp9NJS24RXl0wInBPIptqJKBk7U-hCO88_etn9zr8kjeGiz3Nvjdo6Z-sS9h1uEql48p8zSESPTfpq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZdqWWte1dR_mFA9IRZFGnnG5zbh8TRYcG-UYU9uQSQVIW5-874C5w-5usjQUYZwSWV4wdVw3vnRyzjgRS_Txfb3UqqKVcJkkPWPA9_eVbfFszMYt7QNx0VJ5yeUQeqlo3jbwTVibnNui9g4ehNamtsih8r6SgAaEsf4u1jcgnaSYEWz2rLAGAzTP0GbGxJ1aXQdoWEXYNka34mYAGnH-Z9jOYa7yCsZk8g8FSt3x4hsSgv2WUwDkpJHBULrH7aDsiMc-l7SNs9IDCE0kQloB6RbZLog366ZSd7-MPpuCxawkqLy8APpP0aG_z6jo8e4jBb6Ek-izg3baf-fVtsNn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SLdosM5Sj9GMNPUQnVvzvKvwDAsOOHnSyZfVL6_L80Vo6fnH_jBKCaGm4o-GtxUI4OHq1Pm1OC3XwTr0p4Y1pgP8KWW2ix__tRnP5u3Afq79OXPu4NSl4_XY3mXtPDoXRbfCiULIH5pYEztmpZvr69DaAAu_hnKn3Util-GZzkAqpjV4zne11qN53hrHlMrqT2TezLYgoNSDE0PxwYb1XKGb4EBm7AD7mXPm7AQkqfAc3iE2-xNVGUlanjLbIpTBy-xxoCEckMkcPQumx7xEoMxG4ufvMJCT2COxqw19QtW7IlQfyp3c4e4BC4oYDQ4lNUiNI8mjKv4XjZfWWEOoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sVb69Ub9s-RCPtHUGSG7T6tB_xgzZoca8Jhwi72_EDeLKknlp5jhYPRlKcgXfetVPUrtGhS03U_Tv21DjOnADxXOMjuNTt2UT3B4hsIpKS7vnFc1mmOQZNLa6r3Ob4OBhQVZtdhp4iqBcYn-0acJ7MwQEv0R8AfsUEfBZ_5klEEt5MvwZ_THz7NpbUo70bf36GjKnIb9K8Uu3he4yRQnVGmkoZJcRiUEFk6CbtSo7968xLf__FNaywdk_i-AO_tTn7nKjHRM2YrJw1V5whsNPVTaK8WHn5x0j_lRRUtl8HMY8usjn1UdLUzweg5wip8AqYbVrpWmCi7A1TLyMM_Puw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5BTdYo35G9YYIM4uYO9jtQ04vm4K4vywMOgLDAIk0xTLacpCwoNnHhTTiqGETpG3X-FHxJ9ag_bGPLiwK0-VlT8xVPlAajuYBEkddDxB-1pv2qfR2KZJg8sE_8bf_ekKv-w-yF6DjVpz8eqQALuzcurCeaP6X2VFBxOt7ETAfq45Szg1tvZDxsq6lzKBC4BrkNiRAUuOqH0FTfiTh_rxigGX_7874Fa0p7XAcM6Sr9DX0OSvQhB-xsO8dSS9SRmhzLodZc3akHCmaeQm4sBMdUObjxegLKNdoHy8axunWygGFK5fitsI_IXS9RRg4y3JtSBEczm_wHwu3rHpcyGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dwZmejZmAJ9chkkggfnljMFpfX_pXS3BQoAkycyZjbgNOIv33rKdOFwg2OC89Ysol866OmkzkyR32ifY51sFStVN19NMSi7EMmTJIdOR8I2uac40xqXXM4vX7nO6WqFv1PgsOdrqliqy7pKGC7Br06br76ODugMhFxSoES47TlVKxx8mXY75_JGR0-VkPrjcDLZTTm3bVzwhxcHZf_qti71_0TAOjVRlpZi6-5f9a8M8E5sZfLtyOLVaoW8Hdhjgz_NkJiM8Im2beyX-8yf_aFdPGYLrPZ1LEpSA7Li8piwIPiP8YrfmSflHvm4BNYXVCNAGNeEP2f2D-jt50d9aYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_Fj6iFdeGt9KBNUXabYTFWsnT-slazweq__OMh8A5jgor43W5d0KY2bIOfTg9l58An5V9CQPWhsHeEByKl3dpDlBMXbqpr6eyA5vA0MhMP80hBFWvm6KRjs2ZxlL4Kf4qmilZGDJvJh0QOCs51V0h4IT9ulRqZEyxNYz2gRVokD614bzujr9rpsE8pAxM_60MX4nrUyBDSLoPiiv6wE9GRklMr2_Mm7eoZQt1cpUwmd42mZYrNk80WBToJlksdpgBo8aElA4PaA00KhOXokB5XxjEf1Flvm4nAWlneCvcebAkN0R1oZzdvq_9lVNqgYfRNu6uUfCWhzmOdcY9ohqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M5E_4YYgbg0pVHPL8Qw0DnuJuBY4D83bIO5wrOuSYhXz8BEeUjKHkC2lIlLUUAYVi7VifiwWW1zjEc2A1x0PsquzrF_HgOBHv7vZ-LIFCQrysjzsHzidJiyOnu5UwAaZhQFucdNsIbl__LXoBhVCd4ej7RB7mZ9v2lg6zFVuydciKjxbSMW-qwoX_JkcQWBwCnlpfcAttVdxZU3TiCM1vIXrSpEoakggmAE3Kjo3RykYY6OdbOezZeawRpYM0RudDDKCi2FdVWoq__7lOc3tVng2yGMXnmTKE6h47yAvdwqYCxp_jcGP2y-zRFKUCM2HIeuA7vTFhuQpg1iMT7DJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIOdbMA22i_36vnN4ZdIBgmJmik7H3Q0iuyAwCPvpkGuTbcEJKstEndn-WziZxDaEpAUhR_XKPVAjBA13c258lRuKmekFZBOtOhwUEKRmSF727f93VOwQIg4ryOIHku6nW_Mets4wKZQcOVJcxv7l9Aaow6aQUqxRGkhon-Ywo6Q8BcBjQwLmHYVZdDAHfmcVgC9ZXF_NM6X3kqzoVCfj1pb9z-BeR7ry3nPxT11vd-NQCkd03D-1z_9r5HuNvtLp9ZZtQqgMrhp0pljs_azl04nRszvv_uJ1zpL79TUVR2bjlf_HDDrZEvyhHHTIRdjR98f9I-GAzoU_4EnPBlIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZTxP60oS9tx1PHBi--6bgL9I3fm4cNvF3Ll6zEtsXVELYx7GFbY8dwPX4w-FQxrRqKLlSwqn-JYttWDKBmYNT5N1X3vBjWCLJJHy558OwxHC7SDvhZSA2o2j0PIVW55mDH4zfF_Ejh_HwkTLFdXWSOtzdzIaiDPtojtdqNiilUNgJ1bs3GyuNK0xjvWLEme1pNiw_Z6t2runWNVGNRTr7EKHqnJunHwjWY5sBBeBC_pt63agtGEr1FiPNIIGROQKJNV_EZTvldbspl8iT_Z7IOR5VpLJJ_mWayoO0wht0SF5lMpaXPVU5L_iVfy64sQAFjfTFAnUIx9JTHQhY1zrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAJdIhBWazvFnmtwVtNZXgQmFjyNLtMWJYKCc4L6i8BALwU5wA8uAZ3shvod7uegXCEn1scmB4GVEio51NDTN7OLDEodi1pI5zzKdcqOfYzaolsezvZlmpJwV2z18jhJsLU0GlwOJZK1p5FAbcr9OHdsBYqdB-wMunX-UrHo4aoYxRgQecAwn39oO2o627Olaqge0etKdHl8iU_evZn0qREwVedn07K6Lsr1FuBJQ_JLaNw3abCd0J1eChUrwUu0BJR4MFgSiKyaKY_C7rEHlOiAwhDyQJyapzbT8gGC4Bis6_YdW2NySz381630qaN6uUJyTVy6AHN5JhuebGihMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcYUHC8SOtZUtaU6qiYytLVVRQRpaQRmWEAxEeYlutpTXhvfxm--0-ByTJ2lo9A-4QaVn0XsXS4jR0d2gz1KBdYOqIj92hsOe6LEwoi2eWsaTwXSbDn0yICPsLjlXbak11eyGxbtxhrCVLzciOcnDHNHKIeKKCqDbKWEX9vA82QIldYJKKXRNnZoD3sxyOapyXfT5pJnx62o01BEPzHrAWE2BjIK91uW1AnJ9Fp55lX03r9ZVBV34wxIVCLLatfUUZMoBlMUkXlv1urGiw4oWX66mmJp0nyM9Dc0By4PdtfxwP6Lp4BHqYgFt8UuZmXl__y3bWmB5tQtRYeIB9l7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
