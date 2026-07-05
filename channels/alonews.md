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
<img src="https://cdn4.telesco.pe/file/PgrcHjsDsPwoEtyTnsbNiYlZod5q46IfzaYKuA85kVY9z-Avmx7rg9aJll6Ls_Jxjsab2EeoNWnBrkFJTTMNp25tEe02z7OcQ3w2sNVdVosCkzBIAkp9Y6Lk1Sbpu8GWJ1G2prr-2QmwhCr139kvIPGV9fATSMNB5mZ90ccG5og415FZaMlSR7yFFhDO8UdezWpoZcRU11Da3sVxjs_P-unnE2KxdZNPANixbdC4Uvk9HKEM8KOz8DklwkeBbPaGeEK28whc0jrPEXZETw63eYhB6QywThkUKEYV7igWDZHyRNF1Py7OjSeKcMQKGe-cQMDl7NFgFzrGKhUB6FY37Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=rbyjz5g5AwH4Ypa_Wh3U9dmCIt0beuhNVVMvljlaoE_I6U2xXS1G3UC6mQaxqGCLmAHXYSZu2E39uNYTpTBNIQ-51Ts__rg5MzEUF_U54GQXZxtFSwEPpANUhATjOFL3DV7Jpz_sE9f9yxASYn4MJTq6_SJR2wAvPdilW1GITJT7kYaEMk6begJkfwWLqpmjVFNosYPIx0R2UEquG-B5dT6MsxnL-Aqc0yRUZkswVi2evyFlcHwqL00yAWfHEewFb45dPbtYOjdJkrQZ_hGCD2hUsz1B4eNWzZjYer-IQl0NokaJ_vL5QiZrXzBonAXIrecVJnQ3CaCY4HBR3eih5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=rbyjz5g5AwH4Ypa_Wh3U9dmCIt0beuhNVVMvljlaoE_I6U2xXS1G3UC6mQaxqGCLmAHXYSZu2E39uNYTpTBNIQ-51Ts__rg5MzEUF_U54GQXZxtFSwEPpANUhATjOFL3DV7Jpz_sE9f9yxASYn4MJTq6_SJR2wAvPdilW1GITJT7kYaEMk6begJkfwWLqpmjVFNosYPIx0R2UEquG-B5dT6MsxnL-Aqc0yRUZkswVi2evyFlcHwqL00yAWfHEewFb45dPbtYOjdJkrQZ_hGCD2hUsz1B4eNWzZjYer-IQl0NokaJ_vL5QiZrXzBonAXIrecVJnQ3CaCY4HBR3eih5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از مصلی و خیابان‌های اطراف
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/131863" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شبکه «فرانس ۲۴» گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از برگزاری نشست ناتو در ترکیه، با ولادیمیر پوتین، رئیس‌جمهور روسیه، و ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت‌وگو خواهد کرد.
🔴
این رایزنی‌ها در حالی انجام می‌شود که جنگ اوکراین و مسائل امنیتی اروپا از مهم‌ترین محورهای نشست پیش‌روی ناتو به شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/131862" target="_blank">📅 11:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=BORB3KBd4or2r48UGkuiBb8ip4vWu_jeXufBVx0RMgSSVgW-dBs3JrSPy-c3jW6X2oUpBCoSQ2biipPONWdjfBfZw52xz2VVA609EpTOyFi5O8oJzcRWTtHJSIQmA2GjRgYYPlivRyIoR-trXCRIZCscxtwRNpo5ecuxRZS_R6Ant5t9cKu51m4ao-6q7zj4pyL7i7gR-jJK5zRjZBwL7pLkRvQXDo41o1HRtffeOnROCuR5W2XJe8ZLZOh5ce7K2YkAUWTgtwJgcFcE2ooXub9QnBSZKUypnslkGI1af0gkKk1_zOxivgc3IWXsmoSyvWfIuZbdnoZSuhRUH7SiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b32a145c3.mp4?token=BORB3KBd4or2r48UGkuiBb8ip4vWu_jeXufBVx0RMgSSVgW-dBs3JrSPy-c3jW6X2oUpBCoSQ2biipPONWdjfBfZw52xz2VVA609EpTOyFi5O8oJzcRWTtHJSIQmA2GjRgYYPlivRyIoR-trXCRIZCscxtwRNpo5ecuxRZS_R6Ant5t9cKu51m4ao-6q7zj4pyL7i7gR-jJK5zRjZBwL7pLkRvQXDo41o1HRtffeOnROCuR5W2XJe8ZLZOh5ce7K2YkAUWTgtwJgcFcE2ooXub9QnBSZKUypnslkGI1af0gkKk1_zOxivgc3IWXsmoSyvWfIuZbdnoZSuhRUH7SiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور فرزندان و داماد آیت الله خامنه‌ای در نماز میت امروز مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131861" target="_blank">📅 11:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی ارتش: بار‌ها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم؛ یک لحظه را هم از دست نداده و غافل نمی‌شویم
🔴
اگر دشمنان خطایی کنند، حتما با پاسخ کوبنده نیرو‌های مسلح ایران مواجه خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131860" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کرملین: تماس تلفنی ۸۵ دقیقه‌ای پوتین و ترامپ درباره جنگ اوکراین
🔴
رئیس‌جمهور آمریکا پیشنهاد داد که در جریان نشست سران ناتو در ترکیه، برای پایان دادن به این درگیری کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131859" target="_blank">📅 11:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD6BEzHVWUtg6UXwIrD_Kd2DxN3xAvydAMdBSDPeImtdFpQWQ4QG2MYiaqqC5fvLlFDeFOs2MPivmjtPjUHoz4vn5EZSiZZhai7cqzvcVPEN_F5YajOHtLXi0IXmoPQVFmgTktU5l0d8hlZtJqDlE_rRTy2e5Haai0lBLIc0hKIysgN9WUfhcnTKxVl4oko_CFwF8t5Gm8626bwdUiILA4HoNDnT4ggnHZX-_mKomhiq2BMIsDE13n9LXHTjZNyIzap1Wpl4zV9ZekiUuO_Jl7Aq3UwVcyUVbfgw9KnZxhUOhvU3C4EdJWsNb49inyn0gor9XOSvJAjKKXHCQ0cIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/131858" target="_blank">📅 11:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت حمل‌ونقل قطر اعلام کرد فعالیت‌های دریایی از یکشنبه از سر گرفته می‌شود
🔴
این وزارتخانه ۸ تیر از همه شناورها خواسته بود تا اطلاع ثانوی تردد و فعالیت‌های دریایی را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131857" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ : ما هنوز هم پرچمی رو داریم که بعد از غرق شدن ناوگان اسپانیا در خلیج مانیل
🔴
روی ناو فرماندهی آمریکا برافراشته شد؛ یکی از بزرگ‌ترین پیروزی‌های دریایی تاریخ
🔴
همین چند وقت پیش هم کل ناوگان ایران رو با ۱۵۹ شناور به قعر دریا فرستادیم
🔴
همه این‌ها توی مدت خیلی کوتاهی انجام شد؛ انقدر سریع که باورکردنی نبود
🔴
ما قدرتمندترین ارتش دنیا رو داریم
🔴
از ارتشمون استفاده کردیم و نتایج فوق‌العاده‌ای گرفتیم
🔴
به ونزوئلا نگاه کنید، به ایران نگاه کنید؛ ما نابودشون کردیم، ارتششون رو از بین بردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131856" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPq_S3p3Dbgb6Yn0WWQm7OuSzK5OM6dzoQRz9CK8K0xPeJi4tPcSVi0VwawQy9lQre4G8urNWdt6Lc_6U5SCx6Og5Mm_JXjikyoQs7mkhUAtNNkpQi6ZKWngvsK7mhVVolexrce2_G5angPkPmohfV1gElJb3Jb9gB25YuUTL96fqK_NLMkl0PA-c9J9uk4thK1l-4PfQb9NQEVkEjntrq6JePQD1r0R4RA5aS6SbEuMhxYvTzG-OkvkKQGKYn48_NVhcVdTKtAnzOt0H0TkhGV_uMalo04WBTwdbfkv-UGQeGflt3CeluyNCXU2iat-ovjheHRZgXFepltDVi91ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb25OjssJNQyiR-TcJsE0stBudFW3djBh7NmnAgydPpz5-hhW-_TEGo3Zque7wmDgrUX9Us9sQ6uRv-e_zOPsKmUXPDuT21_GLBNzZNG9zfvFj8LwcyYh6lztH8VNFnzxao2Grl8fHK-71k0ApzQb3PPBKd0KLsCXmlIeVujhFC_HikT_FIPFpXB7ZEO5rlFYdVsFM7iwR1XqkTmxfpaDfo00ATxASIckxekWOjxtV4e5tOLe0k0tT772EVifOB3lGpKFyGIreLIsp3Xry9EkQ7zGRddMOlDLAfHHP5wIfG68dqyVn8DDBsIB25KNUcscHnpOKcZ26zddwnW9Fy8Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نخستین تصاویر از بوئینگ‌های ۷۷۷
عربستان که به‌تازگی وارد ایران شده‌اند
🔴
بوئینگ ۷۷۷ یکی از موفق‌ترین هواپیماهای پهن‌پیکر دوموتوره جهان به شمار می‌رود که برای پروازهای میان‌برد و دوربرد طراحی شده است.
🔴
این هواپیما با بهره‌گیری از موتورهای قدرتمند، سامانه‌های پیشرفته ناوبری و مدیریت پرواز، به یکی از ستون‌های اصلی ناوگان بسیاری از شرکت‌های هواپیمایی بزرگ جهان تبدیل شده است.
🔴
خانواده ۷۷۷ به دلیل مصرف سوخت بهینه، قابلیت اطمینان بالا و هزینه عملیاتی مناسب نسبت به هواپیماهای چهارموتوره، همچنان از محبوب‌ترین هواپیماهای دوربرد جهان محسوب می‌شود.
🔴
هواپیماهای واردشده به ایران از نوع بوئینگ 777-300ER هستند؛ پرفروش‌ترین و موفق‌ترین مدل خانواده ۷۷۷
🔴
این هواپیما به موتورهای GE90-115B، قدرتمندترین موتورهای توربوفن نصب‌شده روی یک هواپیمای مسافربری، مجهز است و با بردی در حدود ۱۳٬۶۵۰ کیلومتر و ظرفیت حدود ۳۶۰ تا ۴۰۰ مسافر (بسته به چیدمان کابین)، برای انجام پروازهای طولانی و بین‌قاره‌ای طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131854" target="_blank">📅 11:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
🔴
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
🔴
ارز‌های دیجیتال به این کشور‌ها امکان می‌دهد تا از سیستم بانکی سنتی عبور کنند
🔴
مقامات غربی به سختی در تلاش برای همگام شدن با این وضعیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131853" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گزارش بلومبرگ حاکی از آن است که روند عبور و مرور کشتی‌ها از تنگه هرمز، به‌ویژه در امتداد سواحل عمان، روز یکشنبه به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131852" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آتش‌بازی‌ها در واشنگتن، به مناسبت دویست و پنجاهمین  سالگرد استقلال ایالات متحده
🔴
ترامپ در توییتر نوشت: بهترین آتش‌بازی‌ها در تمام دوران
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131851" target="_blank">📅 10:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گزارش خبرنگار ان بی سی نیوز از مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/131850" target="_blank">📅 10:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7xbowJxtdZWQjR8VOiT78-bJQjUAEJe-1niFzMxX6_PUBuzB5KyEyzM8UsFJSBF51X_c1ErwZuNIOajbTnWvQoaSe8ybEWhYqcWg-5UUm3JEhdwTvDNSsVuQ6x9eFP6m7LGQtCAFCfCK-TH5vf5age_06lLhfE3oDI2KPRVXRVrQb9TatZUQeNXg6xpVOFOEeiqPkqRvdqylacymkaBktu9W53g2guAO8KV-n23b6iTPxnJemmoAsjZ-Ofwe8vkUd7KfHeuKQx8Qn1QU4LTg7ISAi6V7cYMHY6pvpZuabq06Sqc-F2T-0V9HMo41vIgDqENKmKTI0cBmGwH59BAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131849" target="_blank">📅 09:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترافیک سنگین در ورودی‌های پایتخت
🔴
ترافیک در محورهای چالوس و هراز در هر دو مسیر رفت و برگشت سنگین است.
🔴
محور قدیم بومهن–تهران و آزادراه قم–تهران در ورودی‌های پایتخت با ترافیک سنگین مواجه هستند.
🔴
تمامی محورهای شمالی کشور فاقد هرگونه مداخلات جوی هستند و تردد در آن‌ها بدون مشکل جوی در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131848" target="_blank">📅 09:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: امروز در تهران آمادگی اسکان نزدیک به ۳ میلیون نفر را داریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/131847" target="_blank">📅 09:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=kliw0VpCoo6DFPpS6-qoXL-1VAExrqkc6VPxCLd4DyfkK8GuIm0AIlLyI33nG7IeKNhfLrM5YIdwIYB1Lizq4eiIWUt_21wb77ILlnYIuTpgG3QGYboymjNNKLN5fkmfNBnt-VdDeaSZDVh6b4T7IxzPi03ju3exjAf7WklJfmXHFgP_I23cGZUaQDzlXJJ7RPxgoIPGcaGWJfL6RW7WU8xodUMPZ7ucHvzGKGscrO6xdUc6E9wQRSHn7wooA_H7mqYKiUnJd11EViy6J2gZlmMHTtliuj_vkKwAueT6OEp4dg6bbXwVmxxsTQWA6ADdlzaAGoW70mcVIYd6BXE1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2c1939de.mp4?token=kliw0VpCoo6DFPpS6-qoXL-1VAExrqkc6VPxCLd4DyfkK8GuIm0AIlLyI33nG7IeKNhfLrM5YIdwIYB1Lizq4eiIWUt_21wb77ILlnYIuTpgG3QGYboymjNNKLN5fkmfNBnt-VdDeaSZDVh6b4T7IxzPi03ju3exjAf7WklJfmXHFgP_I23cGZUaQDzlXJJ7RPxgoIPGcaGWJfL6RW7WU8xodUMPZ7ucHvzGKGscrO6xdUc6E9wQRSHn7wooA_H7mqYKiUnJd11EViy6J2gZlmMHTtliuj_vkKwAueT6OEp4dg6bbXwVmxxsTQWA6ADdlzaAGoW70mcVIYd6BXE1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به زودی به مریخ خواهیم رفت
🔴
ابتدا به ماه و سپس به مریخ خواهیم رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131846" target="_blank">📅 09:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imJcJNzl9GhbsH_y4DbnHFJGa1zoBELPFfD2O_h0axEbeepvp2O_OD_7kpiixTTJGP5PnfvsCuiNO-UDmEBKDDvwAapqbB5eGkKiZJ-iHXrSMr5M38xmRNFsazAPWrVGKNOm1WSx68Vx1Q03X84t5nqEi0dOJsxzhZorvzzH_JLNrhzxJHsvPvzyFVTZIHAvel9B7JP7u28y9bRzrmhA71zOrYYvg48Bj1D2y3U7Jvp4IPOv7nqpkEGCZ4RXI8znuja-LYQJhRm30gZnoaqa7agtGP40uza1vkDRryODU6xEgN5RK-0T1uxuXchuVA8UxI4aSOhR_WCgE-OVLGCOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از خیابان‌های اطراف مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131845" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnY8Ki6KjtVFnHPATVBYODaMznKNkxSp18gKF2zlA9yWO3gTR9wtHF7XMIDtQJVZ-o9xJmvn5X3j2oPRWZD84n47iQ0zt_s4eQHB2b93PGOj6mv8DHGCPCcG_tZXiQ3Ugh6rp5DrsBPNZYWJrLvCagsds0blR9QqvZWZB7wlD487QVWS60_YF0O0s6ufwzwvTOjwMBs9mXFs5jAOgkSXOg4Xr7iuxxoZNPa9RoPd-wQa-AW5TP5B-zBZKmMITG797vWdXnA_TTcwExH0WX-S-4cLzeB6WjOyh3n_nxJgcssCGEYbrucfs1SjNIOMu1N99wQfcdAflpYPeIHHlNkNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTjceXbkj5_mhyE8OrvgXarxuXoRBPeCd-nXlrzcHrzG8foxuZ_6n_UckuY5kjYOBkw4H_fY-7hXi9DK6KON8lTfIc155p6R1a44yySXKp7W9QLW8et34OySf4mtaplo4o1iI-jZJwa42A-QYefxBVLut77z6PLGp1VCbYHr-Uo2ZPUY4nHhHG4O6HLih-xpeBsbvdGXdXKIZjVQCqZapkPyWYz9xabo0ncuFU3VeFyWIsLjlrZgqHExoYLUOWhvF0QLX8xU_eWyNSk0oaQ3fEgu8BJC_fMLeCBgxb5uU-t5VONSj-Bu0-AeBBjF4yDO8oYtL4EdCL3S-lTZN0msQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده های SU-34 صفر کیلومتر نیروی هوایی روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131843" target="_blank">📅 09:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پوتین به ترامپ زنگ زد و ۲۵۰ سالگی آمریکا رو بهش تبریک گفت
🔴
همچنین پوتین ازش دعوت کرده که به روسیه سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131842" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
زلنسکی : با ترامپ صحبت کردم
🔴
احتمال واقعی برای پایان جنگ با روسیه وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131841" target="_blank">📅 08:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت دفاع چین: پکن و مسکو در ماه جاری رزمایش دریایی مشترکی را در نزدیکی شهر چینگ‌ دائو چین برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131840" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNSx7BZkG4UhXdUXspLAvVpbsTYuBBLFnwZHygxL8pQJzVJvdKGp5zModaT81Ieql9feydeTeBznMcV0V7wpneVqeZgw3rxCIMFkOK6iikzAswq3WISznpcxp__U7dK2MaVSwm312-qSFLBdMD5jtFwUgSIs41P-Eq0A2n0NxCtr3AflB9qlbleJ11AVFUFUd_JinnThtzPgnd6qv7g_WBGYArF-9cIuhpGpkTXoc_jrJpToUn-YjDmnoDnzJO0vAJz3qVAj6jx3d9aUMa28sLY9GBJpjJbeYatEbBE9EUJfNJ2BtHylA9ga33GL6ALUYbsXoidoXwb7TSiivUFmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار هیات نمایندگی حزب‌‌الله لبنان با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131839" target="_blank">📅 08:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ:همه جای دنیا تلاش میکنند شبیه ما باشند؛ اما هیچکس نمیتواند مثل آمریکا باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/131838" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131837">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
طبق گزارش ها شب گذشته پوتین و ترامپ در تماس تلفنی یک ساعته در مورد ایران و اوکراین گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/131837" target="_blank">📅 08:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131836">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=VAp0Ytku_UKfz8R73RqgEl2ee5vgtvCFzk2I2c6d9Hy25AWDe0moA32OcCP8q1SKUDWkmhZZcHLQSXI2w99mn06m6M2RbtYSSv0LzdlqkSIgPoYLDqOZ2Y4iTF9Yb9qfDZZWRkNYeJYAwhKRJcXIBmuQyIvUH_1ObU55ZoDw1Xbvsx0N5gM01X9CkB91tqFHQGN_f5dywflygSnYLY2BwNqyJlzMzejSFET9iCxZX5tJdkwQRCIekZxKLQfn5KQdGIvXIcP6d0kqsPF6NA-DKsU3GTRt7iCgSd-OUzYHG3P84l7fg3PzcHYf5P-B8TTTk-u3Ourg3-8BB9KT_-UDuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3c08acdf.mp4?token=VAp0Ytku_UKfz8R73RqgEl2ee5vgtvCFzk2I2c6d9Hy25AWDe0moA32OcCP8q1SKUDWkmhZZcHLQSXI2w99mn06m6M2RbtYSSv0LzdlqkSIgPoYLDqOZ2Y4iTF9Yb9qfDZZWRkNYeJYAwhKRJcXIBmuQyIvUH_1ObU55ZoDw1Xbvsx0N5gM01X9CkB91tqFHQGN_f5dywflygSnYLY2BwNqyJlzMzejSFET9iCxZX5tJdkwQRCIekZxKLQfn5KQdGIvXIcP6d0kqsPF6NA-DKsU3GTRt7iCgSd-OUzYHG3P84l7fg3PzcHYf5P-B8TTTk-u3Ourg3-8BB9KT_-UDuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویانفر
،
مداح
:
آقایون
سیاستمدار، بسه دیگه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/131836" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=vD3LKzhXdnYrazik4pTAVO7YyKO7Nl3gMFG_iRvGloRMMrlA3hSX6eUFHBs4qBzto5M-ksjNOs6sMa_-S1Mi_AzNjqUPCGfTTF4xCvJn9NS93mu7FIpFBF6HaZD8OP0J3QLITsVobe2psPj9R55gUBzi-hmRsqpSwwF-csfiD05QKTbn3yRoWzMSbJgdJ_IsCQreb6lScaDRn2xN29TFZl8mwRqnZkVxYJZnYvCcRJDujk0pRhwjphO_I18N28pCJCs_g49s3QaLTJu1c8oykKVld2tWePu07gVegIrK-UxQYBp-0MpuCTe018F-k5uUisxRNF4d22_Pc5kmrhaxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=vD3LKzhXdnYrazik4pTAVO7YyKO7Nl3gMFG_iRvGloRMMrlA3hSX6eUFHBs4qBzto5M-ksjNOs6sMa_-S1Mi_AzNjqUPCGfTTF4xCvJn9NS93mu7FIpFBF6HaZD8OP0J3QLITsVobe2psPj9R55gUBzi-hmRsqpSwwF-csfiD05QKTbn3yRoWzMSbJgdJ_IsCQreb6lScaDRn2xN29TFZl8mwRqnZkVxYJZnYvCcRJDujk0pRhwjphO_I18N28pCJCs_g49s3QaLTJu1c8oykKVld2tWePu07gVegIrK-UxQYBp-0MpuCTe018F-k5uUisxRNF4d22_Pc5kmrhaxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی و برخی از مسئولین تو حاشیه مراسم امروز رفتن چلوکباب خوردن
🔴
مردم هم اون بیرون زیر آفتاب، صف وایسادن تا غذای نیم پرس و تخم مرغ آب پز بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131835" target="_blank">📅 02:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کابینه امنیت ملی اسرائیل، احتمالاً فردا عصر تشکیل جلسه بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131834" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=VFWYdqvFty-G_26YwuQCGmxL0v-B64eoB5MoBpAMST1pQGd_p43ituNk8GX6jSIj6mAOcPlLv7OoCeFvoW134YorF5PwIvDblAG4IMvi_d815Xnd8C4plnAozWHteW1Cq_GoBxenmJYANIYiQ3xPO15hiCS1wGH2R_myNj58Bk5c8J_f48jAp_e7pPXOauhwdKGjz_YYKfha1najOqWPM7BFKpqZ8Xug4hplJTwabTJyFIrVfiG1L4osZ8yo0E4PPu6PqlWzqYj6kXXqL8_faPqWmh70OqDBRhjVP4_L1zwIyXBCL3yaIig0QelacGa52kOYj3l6CF3mDO46iVxpLxUC5d76YGhNRiwYytWje3LKmmPueiq7QWf01grVh30edBMsCL4oj_YeqMoHMOO8xz0HbPcwVwqgtvl8kVBZgHy8KUVwKc9OC3hhJ1BcneDgo_3mXTSFeWyKg5cvIzmTvgM0gl2QX8QvjJzAqn_yHccBwWoA0gRqyXRcTHqswThorcR_BqbBqEBpb-n0U4DMcXML58rb9CG6od94sFNfsOq8Tb6tNWiKqjKd8QVBXkzOQKIon-yOEW_z1Lph_gghGqkQ1-bWbSdLVQGr2FGfZQEIVGTOPiofOlJ8GWZX72ejDWJvLQiwf5jFKr-Oer-844aNL0G0XMmlq0pkMMMZoyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a14033e54.mp4?token=VFWYdqvFty-G_26YwuQCGmxL0v-B64eoB5MoBpAMST1pQGd_p43ituNk8GX6jSIj6mAOcPlLv7OoCeFvoW134YorF5PwIvDblAG4IMvi_d815Xnd8C4plnAozWHteW1Cq_GoBxenmJYANIYiQ3xPO15hiCS1wGH2R_myNj58Bk5c8J_f48jAp_e7pPXOauhwdKGjz_YYKfha1najOqWPM7BFKpqZ8Xug4hplJTwabTJyFIrVfiG1L4osZ8yo0E4PPu6PqlWzqYj6kXXqL8_faPqWmh70OqDBRhjVP4_L1zwIyXBCL3yaIig0QelacGa52kOYj3l6CF3mDO46iVxpLxUC5d76YGhNRiwYytWje3LKmmPueiq7QWf01grVh30edBMsCL4oj_YeqMoHMOO8xz0HbPcwVwqgtvl8kVBZgHy8KUVwKc9OC3hhJ1BcneDgo_3mXTSFeWyKg5cvIzmTvgM0gl2QX8QvjJzAqn_yHccBwWoA0gRqyXRcTHqswThorcR_BqbBqEBpb-n0U4DMcXML58rb9CG6od94sFNfsOq8Tb6tNWiKqjKd8QVBXkzOQKIon-yOEW_z1Lph_gghGqkQ1-bWbSdLVQGr2FGfZQEIVGTOPiofOlJ8GWZX72ejDWJvLQiwf5jFKr-Oer-844aNL0G0XMmlq0pkMMMZoyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های
F/A-18E/F
و حرکات نمایشی تو واشنگتن برای ۲۵۰ سالگی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131833" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm_qicqXoovpbwxHUORojiilH_AjyFr_ldm6V4ZbtTPWF_yZGHP8BN05EVkyw6_eiU30XI_VK8t1r16qnLEq3aZ1xoDNebd90G9xCuSELPEfCg_TO7mm66smJokEeYLggcdDtbg7JrfmuDvDfsYD6N4ue7WwgRqQQoe0-VzzSHqOz7IE99WpwMO8ehgeJM0VqnqoiM_FJaHZW3mgXgkHMcYVWnOny_92QK9da4nP4wNJ_0-OEgZdtsdNX0B6PcS0Z8Q8OQEmVQG4Hv2pgGJtSntujfxZv7pVBcOi6MmA0wJ4GnUf1Wg5xSXJul3TKkCJQTdSedTrsgMBsaduWc_Xkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا کامیون حمل پیکر آیت الله خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131832" target="_blank">📅 02:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnDiYDXWu4-5Zp8Ye_1StQxnizxVB_3m4cSxbon49BzjcyHMjIiVhlVffQu1PIrGfgsTvAiGZhooR0uFymdIfIJXF0kshmgz04TsIq0rIMSnG226EC7mNj3CqGHqh7OlNWFfzcBQQEJ1KmwdI7VvTQgJ09LBnVjPN8sXjwQN6tdx72SswJ8d_wtKiVeNwSTQdhSKy_a7QUYulCSIaDo31GKCHAv0VEVrzp8Q17QAddAXSyeJFpXOPBKrC3JETCU-QDpi3MLNBIT4cgNdnCqwz6e2NUyHtcZJUtUwEyj9_4kR20QXnfoHuiEXKllDErz-FICabF9tpjGft_dgkvGAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستری که برای کشتن ترامپ امروز در رسانه ها و در دست مردم حاضر در مصلی دیده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131831" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf04045170.mp4?token=sA9pQX-ld6RbmrnjfHbNJzW5Xd_9A365s6AF32EqeGobyqukW1D2l6i-yJ0ICuTkPFQoWpNNUZhOZSYfymROw4cOnloDYyayPZb1Rz5tEmMMnm_AMEdaECZslNvu60wJ4R8sbfqllJiwqrc-2NoUMJkx4g0mnqYitAX3u18do1PfCSgal4gitLHt5nIXLUv_-gmxjScvqimWLctFMapTO5kU1Sk8oTC81rDfu7zEo1AVxdiVbTmmGHdtbU3q4VU8wvwc-BCDmA0E2ZL6lvFDdDOWtwhYGON8jkk59OgCiQL-os1cJjEVZOM4Hni51H-OkKmTSF91ZCddIpwpybNznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf04045170.mp4?token=sA9pQX-ld6RbmrnjfHbNJzW5Xd_9A365s6AF32EqeGobyqukW1D2l6i-yJ0ICuTkPFQoWpNNUZhOZSYfymROw4cOnloDYyayPZb1Rz5tEmMMnm_AMEdaECZslNvu60wJ4R8sbfqllJiwqrc-2NoUMJkx4g0mnqYitAX3u18do1PfCSgal4gitLHt5nIXLUv_-gmxjScvqimWLctFMapTO5kU1Sk8oTC81rDfu7zEo1AVxdiVbTmmGHdtbU3q4VU8wvwc-BCDmA0E2ZL6lvFDdDOWtwhYGON8jkk59OgCiQL-os1cJjEVZOM4Hni51H-OkKmTSF91ZCddIpwpybNznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به قالیباف
‼️
🔴
تو چرا اسم بچه‌هات ریشه یهودی داره؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/131829" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K46Bo_fGKRWtR_8JJTNWrnKizEtgy8JX2svlhbadA1x3nwUs4AXKOhsiaQTXO44erwag-obQr6TYhczTzNaEvGworIOZGuIoWRlocx6N94naPwiHMpNuP-TFxH0I8IWVUn375R6aHVsZmTeiJJRp4yjZYkJ4Hwas0Sch8-xpqQ4Br52BvOs6mtfs5zYFz15-wvYWnLwb1wb6j5uVJx4p6YAY-qeTD1hqYNDLpTAODligB492CwUE66K9MSBwMtQQdzav-dBTPfn8l2HpaSsjSvpyjm-md8KR6LPEIHPm-lDpxgMcvbRNpQVeows1K82Fsht3pFppCVx_L_5Cd3_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: مجتبی خامنه‌ای در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/131828" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/131826" target="_blank">📅 01:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=Hkwgf3RVAILGH3rczekTmL9E85b6MLowqpDs4897zzM8pyRnZm7Kuldws-e-HGww7Vv7F-4WyJuBO-cowW5AELAusbX2EfgXUNyG3IUilSIk-QAmxJ4vyaFE4Wsdv6G3ngVyRlwMtwxRsD7BUtKzIdRPLABQ4lVzVgeQCKxJDeUAusePVgGt9Ftq9gmBkHAC0ILAwg2aMg_sMVs0F9vEMg8GirKYMJsmNuAhxcXfuMpXoA_E2rX-GzWNgp4DA4vkcSJFmmoDdfhVwl2sjccm6tw8iXxJE8ZHPc1WcxUBxSP_gJpdjRVTaW-kSQ9OL_fqIqoFx25SFp8h10DNZbvbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bbcff1e.mp4?token=Hkwgf3RVAILGH3rczekTmL9E85b6MLowqpDs4897zzM8pyRnZm7Kuldws-e-HGww7Vv7F-4WyJuBO-cowW5AELAusbX2EfgXUNyG3IUilSIk-QAmxJ4vyaFE4Wsdv6G3ngVyRlwMtwxRsD7BUtKzIdRPLABQ4lVzVgeQCKxJDeUAusePVgGt9Ftq9gmBkHAC0ILAwg2aMg_sMVs0F9vEMg8GirKYMJsmNuAhxcXfuMpXoA_E2rX-GzWNgp4DA4vkcSJFmmoDdfhVwl2sjccm6tw8iXxJE8ZHPc1WcxUBxSP_gJpdjRVTaW-kSQ9OL_fqIqoFx25SFp8h10DNZbvbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش بر فراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/131825" target="_blank">📅 00:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=unh6SQV_VoqOy05MEAobiKSphEuPdBesiXZ7mHFex6gyKUXpieevDl4a9OHPWZEVtBjayn2CfcuxQOlRdDTuA4o3aFRYJlJ7WjeIyWmprzk_6zxlydCjB-QcndwDGfjSpgyQWhzG7o9T540NLB9IZGE8WJiXomdAKs1aMioBk1NJzlgQIYcjiXH48EBE22ecRuygVzz3PevfgETjrg17C0-rLtiYa3JwZG6k797OPl6UR7VM2pYWAmTLzlyAhFM0rLKW7XIa_fGWbKLj_hpXUqEXWsdHN8yzo9QruH_t61tBsD8ZwvSPoP-sE8JkIQe2DJ5R_bYcd3DPZLsaNRzJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f30f9eab.mp4?token=unh6SQV_VoqOy05MEAobiKSphEuPdBesiXZ7mHFex6gyKUXpieevDl4a9OHPWZEVtBjayn2CfcuxQOlRdDTuA4o3aFRYJlJ7WjeIyWmprzk_6zxlydCjB-QcndwDGfjSpgyQWhzG7o9T540NLB9IZGE8WJiXomdAKs1aMioBk1NJzlgQIYcjiXH48EBE22ecRuygVzz3PevfgETjrg17C0-rLtiYa3JwZG6k797OPl6UR7VM2pYWAmTLzlyAhFM0rLKW7XIa_fGWbKLj_hpXUqEXWsdHN8yzo9QruH_t61tBsD8ZwvSPoP-sE8JkIQe2DJ5R_bYcd3DPZLsaNRzJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زمان کوچک زاده تو مجلس یقه جر داد که من به عنوان یک ایرانی راضی نیستم یک قرون از مالیاتم جز غزه خرج جای دگ بشه
🔴
بچه‌ها شما به عنوان یک ایرانی راضی هستید یک قرون از حقتون اینجوری کف خیابون ریخت و پاش بشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/131824" target="_blank">📅 00:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
قالیباف: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/131823" target="_blank">📅 00:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDl--pCZQ6cXjgK0egwV9PGS2zTMU2hlfbgRjEAMHV77ZYL4mlZnZlFRrqCKbZ0Z9LfdMfxFWSMvb0E2V48h5QUZ3zUgb8PIVjf_mzr1TcUcZ2qvdI1HvKZuOJHuzeFoCsMk8BldFefP9kb5Duo1hcPSP8QjD_Cepx2_t57yXOg8iW68fGL0BgzmSqY99j6Z0nSTE6V9N4wXIYmvcm2se6SdYI1oItqE8QCAexTQhKhD0ieqRHWbKMHBK-C-qwWUU9iG1j0XhGh66pxrQej-PDqa6bSWjMyUQzJ0wSFb59NyXM0pgmAP3g87Hil4d5KuGYlIdkV28cGUeFuhbrodUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیشترین چیزی که ایرانیا تو ۴۸ساعت اخیر دیدن
🔴
هر ۵ دقیقه پیامک میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/131822" target="_blank">📅 00:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=g0TLEzueBnG05BBiqtgT3yLDOn1qIsG9nE6qVpZ_wgTJXG4vxsFs6CUTfPB0KFJEEUvcOO_jQ2Ugv2hN0Q_jDhKjM00b--vnnTTdWDKFlWCj0LMK_zRuUII1Helcjrw2C5mOxe2dYJpz-J5qo6VUWRmlX2zG3-4MUc9zii-UWqALCDCC2wj3Dbc8tCBZ_iUk0JDb49DZg1Mtrm1ezBhvInKjK0ZAiRLEBFgkPIzRtP8wv5hcTYFDhYU1uDgxwtf3_11WHQLG_BiZq9hC10lP4lpmBuKmCHAyGt76y5bLf50y6kxE7uNXZ3Ybql9Wsv8OIZY4egpTa8ti9CAhI2T1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e4c4447.mp4?token=g0TLEzueBnG05BBiqtgT3yLDOn1qIsG9nE6qVpZ_wgTJXG4vxsFs6CUTfPB0KFJEEUvcOO_jQ2Ugv2hN0Q_jDhKjM00b--vnnTTdWDKFlWCj0LMK_zRuUII1Helcjrw2C5mOxe2dYJpz-J5qo6VUWRmlX2zG3-4MUc9zii-UWqALCDCC2wj3Dbc8tCBZ_iUk0JDb49DZg1Mtrm1ezBhvInKjK0ZAiRLEBFgkPIzRtP8wv5hcTYFDhYU1uDgxwtf3_11WHQLG_BiZq9hC10lP4lpmBuKmCHAyGt76y5bLf50y6kxE7uNXZ3Ybql9Wsv8OIZY4egpTa8ti9CAhI2T1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از متولیان مراسم تهران:
تابوت حضرت آقا، یخچال قوی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/131821" target="_blank">📅 00:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIN7vPF-STAhE5C3DdbAkrCTFO9wdFjrmT0sYwfb1WCA55WMS_O9c0ToL13fbL1p8UxLYsMzOPU56H5Z_5oO_SzbuUv1ox1wlyHYfXdd1I9PruCuQcDfX9E8YjGuNTack7IndjctV62PhzSzUwMN1W-X8uGgCHvwzFM2XBotFucgmd7s0R27U_pQeRiz3EqrxLO-kOwePJHVvwXI7oHbI48q0C4l9-MzOp_jRwJ7R5F6F4sQd3rOLNeRVjHwCwVBDYdRp2PKnI9z7BzVziSZvlLY7uE9sLMR7OijCn_LMvPc07srMtmNFl2biSde9sQMKZzYg0LAfFdC2NP1zTcg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/131820" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5nBRN17VF-u-tTh9svNhis59rnVB9QoOncCW-MW97oiVJoVoLnwEh76Ac-QONb9QqubhZOyleGFT8F4dR3WX8uuoDduSRlAJVyQu9xSty0EE4XZ5Wc_2foY1razMcs4KfKv-Jaczw0A2tdD8cXARZS6wJVXVzCwh19fNCfa2oLLWRWE4r1vU0YCqBgMZZHVXFWOXzxKbuqirMEWSbESmE5x45g-QJtL5IhtEPM7ifBMr1A8fQ6aas9kjA-hMZKlzuEoxRfofzp8lyozJQj6o6cb9nrS2azDH09JND4VqZN7xE04zp8NGs5-clYWVpoESgP-TaMVjHq489WyY2-k5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای ارتش اسرائیل در حال تخریب گسترده ساختمان‌ها در منطقه حداتا در جنوب لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/131819" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
واشنگتن پست: علیرغم ماه‌ها حملات آمریکا و اسرائیل، رژیم ایران تضعیف نشده است - و در واقع، برخلاف اظهارات ترامپ در مورد «تغییر رژیم»، در حال تقویت مجدد خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/131818" target="_blank">📅 23:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم تشییع برای مذاکره با آمریکا به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/131817" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/131816" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
سرویس های پایدار  safe vpn
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 30,000 تومان
▫️
۴۰ گیگابایت — 60,000 تومان
▫️
۶۰ گیگابایت — 90,000 تومان
▫️
۸۰ گیگابایت — 120,000 تومان
▫️
۱۰۰ گیگابایت — 150,000 تومان
▫️
۱۵۰ گیگابایت — 210,000 تومان
▫️
۲۰۰ گیگابایت — 300,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 450,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 50,000 تومان
♦️
۵۰ گیگابایت — 80,000 تومان
♦️
۷۰ گیگابایت — 105,000 تومان
♦️
۱۰۰ گیگابایت — 155,000 تومان
♦️
۱۵۰ گیگابایت — 230,000 تومان
♦️
۲۰۰ گیگابایت — 305,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 585,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 160,000 تومان
▫️
۱۰۰ گیگابایت — 200,000 تومان
▫️
۱۵۰ گیگابایت — 300,000 تومان
▫️
۲۰۰ گیگابایت — 400,000 تومان
▫️
۳۰۰ گیگابایت — 600,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 680,000 تومان
🤖
ربات خرید
@SafeVPNXBot
✅️
📞
پشتیبانی
@safevpn_secureSupport
✅️
📢
کانال اطلاع‌رسانی
@safevpn_suportt
✅️
😍
رضایت مشتریان
@safevpn_feedback
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/131815" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اختلال موقت خدمات مبتنی بر کارت بانک ملی
🔴
بانک ملی اعلام کرد خدمات مبتنی بر کارت این بانک به‌منظور به‌روزرسانی و ارتقای زیرساخت‌های فنی و افزایش پایداری سامانه‌های بانکی، بامداد یکشنبه ۱۴ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت ۰۰:۰۰ تا ۰۲:۰۰ در دسترس نخواهد بود.
🔴
این وقفه موقت در راستای اجرای عملیات فنی و ارتقای زیرساخت‌های بانکی انجام می‌شود و پس از پایان عملیات، خدمات مبتنی بر کارت مجدداً در دسترس مشتریان قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/131813" target="_blank">📅 23:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41b55a06b3.mp4?token=nx1WbHSakSop_95TValO-rXilvQRzQ6SG3ZWrYt7o7KMz4JYVCi_nVxrRkeNdJ5JM-rW4yRODpDQUe1s5wnnDoFQwGibI4QEArffnu54k0q5kTLoNa9f8ofi8c441IHRkgH4td5Wak9dtoxDqnQUEiuE8wsNqAP2Q2UF3SGkq1CFfVk0-b8MPnb5NJZ3-LKP3PFLylfJMqCB_7t-VjaaKVuyyWALLESOe7hp9uTpNnhreq2qpS1AyEnis18B0J9zbaoZ7vYpvtHKS8RWo-DVi9JrPkiXQqv7nNhwxl_GMZe54xzfhTeI3CvMbupBqIstYq5tKJvxeVJN-IbhnxMTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41b55a06b3.mp4?token=nx1WbHSakSop_95TValO-rXilvQRzQ6SG3ZWrYt7o7KMz4JYVCi_nVxrRkeNdJ5JM-rW4yRODpDQUe1s5wnnDoFQwGibI4QEArffnu54k0q5kTLoNa9f8ofi8c441IHRkgH4td5Wak9dtoxDqnQUEiuE8wsNqAP2Q2UF3SGkq1CFfVk0-b8MPnb5NJZ3-LKP3PFLylfJMqCB_7t-VjaaKVuyyWALLESOe7hp9uTpNnhreq2qpS1AyEnis18B0J9zbaoZ7vYpvtHKS8RWo-DVi9JrPkiXQqv7nNhwxl_GMZe54xzfhTeI3CvMbupBqIstYq5tKJvxeVJN-IbhnxMTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتل یک جایگاه دار پمپ بنزین در جیرفت کرمان
🔴
به گفته منابع محلی این حمله بدلیل مشکلات شخصی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/131811" target="_blank">📅 23:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روزنامه اسرائیلی: ترتیبی برای دیدار نتانیاهو و ترامپ انجام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131810" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoJpJBgZYIoprYLVwUI9NyInBWQwmPZRoZ9Nz0sfg-C0z-M2K04S0d5cyzhHvgBjb111DsRbQZxlsqKCmcXEaAN-k-KVr6dUl_ADpAptsg3QnCVxbHLISQjzh4TNIr92kZ8vClWW-7VoEvRNqs3efWovCR3WDVk39CvIkNXQA9EOIiuDYojMcQgfS6etq2Z0radxK51a5SQ1Rvtcif1VkTs8y_S4CbLwzfiPiFvfYuQ4Lo4QpWD3w2SjFHf-CaKbcPh5J-azsP78RhdE2XY_FxHK9zvR7CVi8t8Afe37CvefK_CXFu7UOiG-yoznblgsE1lAIuM-srcoKzjiqL_BDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پناهیان: حاضریم همه چی رو فدا کنیم تا آقا بازم زنده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131809" target="_blank">📅 23:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX4i3Lj8faCQGC-z9fbAcgOLI0MjLz5u2tkJy2nvWk5nqOEvOiNJgiqsYuCgOBVKn6cmBBQHlxh162F4KZUSEQ6AbFQCe1BD1UbE5wIZi07_pipjReZm-TMQDL0yE3gC2MInUuHR_wAO3pJoh2W3eQAjErqEa3wjhqK36NMwaqpg2RAvzw1pSYsKjUUGiKtblK3dbWBkgXVsNjPtveYM38UP5xkx0jyH5eqFxhiOc5MCzcZDCz0jI6jFeE6kMyDCKQ-gfQzIBzCjp7Jq7J2U-v78R43sNmJEGHqvCpYZJMXgPBIrdW1K82GGsbhCl-1eoeeh17tuMm2XejgLjzt4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131808" target="_blank">📅 23:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بیت‌کوین بزرگترین ارز دیجیتال جهان به رشد خود ادامه داد و  از مرز ۶۳۰۰۰ دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131807" target="_blank">📅 23:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBL3yQVNpuu_uGvUmOnZ-M4kQJuA19zHS-D49eTOgS542CmQDeKxA3AaelgFatAUhhpEIX0KHOuDkKIqjWHiPRBHWqoUzKuhYHyX2ICVF1749EVQYC1zndBD1GMfQZdRKHGZLymiF8ZTCQa1B_hDFzQ-lWJ3clWvVHM2LkczAuKndjD-PIffPRcjh-xhcss4vGiOSWid4kkwipZ18REdISZY088FycoQ6NnFKax1jp6nYbfhT5q5D7wPM-Tq7eWZoQElcCTJGIm0bGkG3uVK8fgxbkQo6KHuzJWdlgDlmtdlhy1l3cHK9FhtYc44GuDsOk_xvSfZEM0Z4Pdg5J3PSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با وجود گرمای هوا، که به اندازه پیش‌بینی‌ها شدید نیست، جمعیت حاضر در واشنگتن دی.سی. فوق‌العاده است! عشق به کشور ما هرگز به این شدت نبوده است. نمایش‌های هوایی در سطحی قرار دارند که قبلاً هرگز دیده نشده بود - چه خلبان‌های فوق‌العاده‌ای، چه تجهیزات عالی‌ای!
🔴
به زودی با هم ملاقات خواهیم کرد. من حدود ساعت 10 شب در یادبود لینکلن سخنرانی خواهم کرد.
🔴
حوضچه بازتاب (رفلکتینگ پول) بسیار زیبا به نظر می‌رسد، با وجود تمام آسیب‌هایی که از سوی اوباش خرابکار به آن وارد شد. ما بلافاصله پس از این آخر هفته، آن را تخلیه کرده و خسارات وارد شده را ترمیم خواهیم کرد.
🔴
روز استقلال مبارک. کشور ما از همیشه قوی‌تر است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/131806" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqeOadc7E__qAP59TXn2BgnDd0hRQEPxFhOoTcm6f2HQmbxTOsg1Gpx7aAZfeS6Xhhe_DkeqM-hKiGL3WjXSUwd2N3wwmxbOGI3pwG_H__SooCMMZeAiXmap8YYMHZtYIPkG5hR07Lara255ctdXMUN1VQW6kuwL0riSUqK8ZYEAakwLshFJLqcWFkw6IThSKhlLPOapaeup3E1ZjjcxmfEYvKSu1dgAFQ7QjqRV8s432tIV9Oqakl9EopOUw6zZatjO2w418JRLyFjvKpp4ETQTwvwd9StnleCO1LqYgpUYvanqFXYmiis1P3Fv8jEqa4M5nhLXnuzapFbcXftjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اروپا در حال یادگیری این است که وقتی جنایتکاران کشورهای جهان سوم را به داخل کشور خود راه می‌دهید، خودتان به یک کشور جهان سوم تبدیل می‌شوید.
🔴
این اتفاق به سرعت، در عرض چند لحظه رخ می‌دهد. من درست در زمان مناسب انتخاب شدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131805" target="_blank">📅 22:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fja6d7N2qGX006Rr969nlwFVfsx7muh3CvmG80By3E9PUKaX-3v438GrfKFMcNcMu_GKHQZv0Z7ldTE-h6YDp3h8KN5Bq2D-GNnHaJsbh21LtRO5cEv6Xx1FfYyI5j3GyYNNjR9p1VxKHZLAACwYx0QQiYmt0pZ6fVypDeyr9xt9MwQ4AdJYcQ4GbYnZ5uBMgsIIEPJ1_0c_C2uNl3gePFnij_fQM-JdKHEjsMirnbRPw7wDjZrxGrEtGGYZunHUdTStjeYKmcx3L-zqsx8F1tznnUJm6S8lFjCFTYEtUxgNvJqOrfPskpGipmCsNOl_Fh-4iNLU8BWtvYX0FNGz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سنگین سوخت‌رسان‌های آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/131804" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عبدالخالق عبدالله، مشاور سابق رئیس امارات: با وجود عمق روابط و همکاری‌ها با امارات و کشورهای عربی خلیج فارس، چین ایران را مهم‌ترین شریک راهبردی خود در بلندمدت می‌داند
🔴
در محاسبات چین، پایداری ایران نشانه‌ای از افول آمریکا تلقی می‌شود که در خدمت منافع پکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131803" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حوثی‌ها با انتشار ویدئو : برای همه احتمالات آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/131802" target="_blank">📅 22:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=LHksyftK-hx1iTnBrTbyRcJYOo5JyVy5RdE-IEh28gH6AAxuoRCZcaaY112p-VaxMRik8xV1rN4Kcpe-3lT1zitiyxydE8zFns7ExtTc5J1V8Uwmyw7KncwiRiZJsfD5GGq5rzrU4qWONAgRMYWutv5HZk7qdBdhnLss6iYJ0d9sWlKf1alPdUI-7vKsGZm8XoSO-Lg2sDVLaqGT90DkGC84apFXF7PfVpgo-jBKKjPuvZxPffsyyHmYdJgQ7R3ajszpYtvdCMHA4WTJqK357yUwKa7A0pGXJEsa4Kr-tlHd0v69Xni2avlfLCH-w_c90C1wud_IRwKncsqyXr3UOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=LHksyftK-hx1iTnBrTbyRcJYOo5JyVy5RdE-IEh28gH6AAxuoRCZcaaY112p-VaxMRik8xV1rN4Kcpe-3lT1zitiyxydE8zFns7ExtTc5J1V8Uwmyw7KncwiRiZJsfD5GGq5rzrU4qWONAgRMYWutv5HZk7qdBdhnLss6iYJ0d9sWlKf1alPdUI-7vKsGZm8XoSO-Lg2sDVLaqGT90DkGC84apFXF7PfVpgo-jBKKjPuvZxPffsyyHmYdJgQ7R3ajszpYtvdCMHA4WTJqK357yUwKa7A0pGXJEsa4Kr-tlHd0v69Xni2avlfLCH-w_c90C1wud_IRwKncsqyXr3UOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار تانکر سوخت در آمریکا
🔴
پلیس شهرستان مونتگومری در ایالت آلابامای آمریکا روز شنبه از انفجار یک تانکر سوخت و آتش‌سوزی در محل حادثه خبر داد.
🔴
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔴
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/131801" target="_blank">📅 22:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
واشنگتن پست: ایران در موقعیت قوی‌تری در تقابل با آمریکا قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131800" target="_blank">📅 22:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/131799" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شرکت ملی پخش فرآورده‌های نفتی:
هیچ جایگاهی بدون بنزین نمی‌ماند
🔴
سوخت هواپیماهای حامل هیات‌های خارجی تامین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131798" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌ها به
۲۹۵۴
نفر افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131797" target="_blank">📅 21:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صداسیما: از صبح تاکنون بیش از ۲۰ بار مصلی پر و خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/131796" target="_blank">📅 21:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=t2zqe_ONuZL_7xzKy5mlxtv2OYsP8ETMszBNFM4VbwPDO1ec1X_mxRGWdpqRC4S1Ji56ll9s8d2eakmE8_1HST9-gxpknB4n6y3htaahR1H2N-JR06NRfbDSvwi7LMk42M7l4uZ9ten6gkdVpagT5X5B8lztJ6XihJqaQiSEfp1m4qWx6NKsnoq7CGQM10LbNc5OLKxwvwjj8jvNaILQGPcVGSptYwC65KnT5H8nvANPhxVovLaGNdsJ3hcCoUmPvXLHm3VXU0vTllTI6x-AJknyZg-xEiGw-iP_SbYpm35E-glElpSSY4dw3VvtYBrTJO6zgT4n3zqY5qOpmy4cCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=t2zqe_ONuZL_7xzKy5mlxtv2OYsP8ETMszBNFM4VbwPDO1ec1X_mxRGWdpqRC4S1Ji56ll9s8d2eakmE8_1HST9-gxpknB4n6y3htaahR1H2N-JR06NRfbDSvwi7LMk42M7l4uZ9ten6gkdVpagT5X5B8lztJ6XihJqaQiSEfp1m4qWx6NKsnoq7CGQM10LbNc5OLKxwvwjj8jvNaILQGPcVGSptYwC65KnT5H8nvANPhxVovLaGNdsJ3hcCoUmPvXLHm3VXU0vTllTI6x-AJknyZg-xEiGw-iP_SbYpm35E-glElpSSY4dw3VvtYBrTJO6zgT4n3zqY5qOpmy4cCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که امروز زودتر، یک شبه‌نظامی متهم حزب‌الله در پی تعقیب در مجدل زون، منطقه صور، لبنان توسط نیروهای زمینی ارتش اسرائیل کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/131795" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-n7JO-yg-xQajnoiv3Fka0g1XQAp2Haz4Kje9FqefzBitOLXflcsHTVotYhZVP_M93bAinzpmN6wU-LllK1qUduOsxIfjTrawlPMwDLjXhV-FzsWE_CDYfroGwUjxTTKBCThw0D-dOepuuhnmtrJqPxG8O1pozuDnPQ-8zSwf0v2lQlos4YVHimmlbSs9yFOUcxTA3_JhgfGd0ZTIY_pJLeCEy65d41YDIgxa31UREpVo3nDysYdBCJRF13nQVS2A-mN5Fhp4lKv8MGNi9qPrpv5olsZlLOb1yCiuc2Th3St8GtzO3mtKSWAOeciMtgsPtzuPyXjrpH_kr7firWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به آکسیوس: نتانیاهو میداند رئیس کیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/131794" target="_blank">📅 21:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ادعای کانال ۱۵ اسرائیل: منابع مطلع فاش کردند که ارتش اسرائیل آماده است تا یک مقر و سنگر مستحکم حزب‌الله در منطقه «علی طاهر» را مورد تهاجم قرار دهد، اما این عملیات با دستور مستقیم نتانیاهو متوقف شده است.
🔴
این تصمیم در پاسخ به درخواست رئیس‌جمهور آمریکا، دونالد ترامپ، گرفته شده است؛ کسی که «در حال حاضر نمی‌خواهد در لبنان انفجارهایی رخ دهد»، تا مذاکرات حساسی که او با ایران در جریان دارد دچار اختلال نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/131793" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfVZG0DyavFRgltXoikjQQeIDEBifsothvsV-1-zcDdqsvKLElbWlaJQzmMt5aA4ESb_1pQ6wdwZH9krcaCZt2wuLBnd_g0WjtAYbI0fwtP5ersW8OyWQdarWjC2ZEKvingzcWJYSxFML5smKcNxo-8KIJVsnxMl5ZAY_wXH142FTxsbtlN5Qu5ubWTujKpSYnx9Lrc4H_ittoDojSvOaH7sHSdQCcGeZBccLHMQ2Y7C_-GSA77nJOjwfGmUowtOO-nLjGj_TWqV-LXySvd1cWZvvwdxXOzftFGYVQzewH_pgB5lZaFmBlB4OoeJ1I1i771Z-3f8zaMZ73apCcWDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/131792" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
آکسیوس: بسیاری از نزدیک‌ترین مشاوران ترامپ معتقدند که «بنیامین نتانیاهو» در همه چیز اشتباه می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131791" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو : ۲۵۰ سالگی آمریکا رو به ترامپ تبریک میگم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131790" target="_blank">📅 21:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
انصارالله یمن : با حضور تو تهران، محاصره دشمن رو شکست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131789" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: بنیامین نتانیاهو درخواست ملاقات در کاخ سفید را داده است که می‌تواند اوایل هفته آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131788" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم برای ادامع مذاکرات به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131787" target="_blank">📅 20:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اکسیوس : ترامپ می‌گوید که ایران «می‌خواهد به توافق برسد» اما گفت که هر دو طرف توافق کرده‌اند که مذاکرات هسته‌ای را به مدت یک هفته متوقف کنند تا وقایع مربوط به تشییع پیکر  رهبرشان به پایان برسد.
🔴
او افزود که هیچ یک از طرفین در طول این توقف به دیگری حمله نخواهد کرد.
🔴
ترامپ :  از دیدن گریه مردم ایران در تشییع آیت‌الله خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131786" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY7lh2KSVcD2YAaTaIsXejiY15l1V-a80WSJdTgLr2_IBeOHMsKpuQ__lkpuEFWPLCP_rTZxZRz5XN3P0oTG-TUzuEbnaKSk1bYKJwAhC-i__8CtNqNg1Kp9KC2JgCYHJ3P4VZ_5lUKlI-loCnkHD8by5dZIMHuj4rpRwECUzG6xfWuS0EM1Lk_bxl979e0xVYoV3vxu9whJINixFzroK-5nOPBzeYTWcULrl6LhXvMwv9-lXriErQQbW2LE457745AA0x1rsbYTWscgsexyeTDakkcvdWniiKLeiyaW55O3VDZU2LfTfmFrcYfL3xeNnw7xmiDMCtnfijzPqXsMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قبلیه بنی مطر یمن علیه آمریکا و اسرائیل اعلان جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131785" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131784">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzhGzfoL_9Wtu1H89HJX2pUbSw7WqPLLAOHA-nzde6LqKMU6F8KP6Kl9fYbTBeJcSdRl1was-27akAN5EwAf2ZYS3hMkLbu9DmhxRzNyo8PI7mzo1RIA1-E6zZx_VijPWa8vlwmcpCs7tT_fiqWQaY78MMrO4JAhawm4C0xlBeI05kDjQrljj_IsP2fkYqouuZvEBTSAFvupykzUDyRoUaVAZ9ZZGdjYKu2b3QK9K4ml6eJvA_-hfyXK5_WNOy0WyZDJ9DUGk2fH2i_0NIRKpzMoxM0T9RvyD_l3kO0iaXA78_xxHCrgLubuKLnMHpnK9I6pimMULhhtHu2brgJ-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ُ
👈
ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/131784" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رئیس‌جمهور عراق:عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/131783" target="_blank">📅 20:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مترو بهشتی تهران: شعار مرگ بر اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/131782" target="_blank">📅 20:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/131781" target="_blank">📅 20:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشکیان:
اسرائیل به همه کشورهای منطقه حمله کرد و عامل بی‌ثباتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131780" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سفیر جمهوری اسلامی در چین:  پکن از تسهیلات ویژه‌ ای در تنگه هرمز برخوردار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/131779" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcLdwhd1ZO2c0NO0q7QD7faXyaXwNZ1BLMyb75bCbiLSpib0KSI4GcimuVTYB5ZYU-EBZQoXuM_PguQ3ukbjB2iX2UDLSTUaZEMBkOjvz1WEvhHfzKw8Ex459KXUXXQtqt-QF4-s7ydBwRLAY169osFzLCl3M9obHtvSjqvW10Zk-3WVBqVkYOaMxrIeU5cWi7MafW6InMK0jz-ynw-b1UsaH-pZFWoU7Anx1Ju5hX3qa-NgD-0z0G2Uc8k_N6p4HbBmUuGx7fSFM0eR5IkKDOJrf4-LqAqP21XYO8Tnd83v8y-l4QKAUwZePdd1d4C-VfcBkye7-n1XLijiZjOIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا گوشی آیفون علی نعمتی در مراسم استقبال در فرودگاه توسط حامیان حکومت  دزدیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/131778" target="_blank">📅 19:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNDZECTpRZWan7hPuzEM8ZiZJ-PAnI7bPgHq-2Jxh4OUDGBNH01CxdO9QC7pPGMDAEjiLutzm8vZSnJE5c648ML_HN6g4s_7uDgtTe-CfIZWTAH3RfsO93FaK7wxozkjQKOMJt_DcGQFvaDcDYPQw8t1rlWFh1iXEnDd9URVJVyf-qKgm2zyV1if3RtfEXo7Z3kBzvF22oHUGG8NZyUxs9moTssvSnRGl82c66ry-iu9N5j_yj7dorQHIEp7H4Nk5INUN-P-NXLzLLUWWXDmAMBfPVZP8vZNvy5Y9ubFw-sA7ldZmV7QELYOhiW-YTnoCE8ntxBVA4asmJ3tHeBeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم برای یه لحظه هم موضوع انتقام خون رهبر شهید انقلاب رو رها نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131777" target="_blank">📅 18:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfMcuHkCA0LsvgURfrpZiIUveH34TzUZik0TQf9PTfle0z659kns7NSqOCT6PziNDr8FnFw5FQZoBzEASyjvhn9RzllW01RoydaGpavRyHsrPoQmXSFbVSkRTvmGzjfvHXSapJ25nxNvm8oErCcufR9Ccra02nenPprqB1laPPzCiSTlM541_K1OQgiDPfNYXgN-4JoqzOm9ndfbXDeQUZi8ji43qp4IwNzHshj5qZS0iZO2EbyB3j0Juql0kxY1M15vyyk9sSqZ_V6rOfid4TOTsHsWJ7B9_XiVvIKIjEe0E8uGKorHxIN_R9ZjzQLtiyruTE4Rr4w-Z4jkrNEGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ها اعلام کردند که یک فروند بالگرد MH-60S Seahawk نیروی دریایی آمریکا که از ناو هواپیمابر USS George H.W. Bush به پرواز درآمده بود، در روز چهارشنبه در شمال اقیانوس هند سقوط کرده و یک خدمه از چهار خدمه‌ی آن مفقود شده و تا به امروز پیدا نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131776" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: موفقیت ترکیه موفقیت پاکستان است.
🔴
پیشرفت پاکستان پیشرفت ترکیه است.
🔴
ما زبان‌های متفاوتی صحبت می‌کنیم و در سرزمین‌های متفاوتی زندگی می‌کنیم، اما نوری که مردم پاکستان و ترکیه را راهنمایی می‌کند، یکی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/131775" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
هشت جت تهاجمی A-10C Thunderbolt II که در خدمت وینگ بیست و سوم ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131774" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ارتش روسیه : ما 5 روستا رو تو شرق اوکراین تصرف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/131773" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131772" target="_blank">📅 18:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/131771" target="_blank">📅 18:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سردار رحیم صفوی:  بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/131770" target="_blank">📅 18:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اردوغان: ما از نزدیک تلاش‌ها برای برهم زدن توافق ایران و آمریکا را زیر نظر داریم/ نباید به اسرائیل اجازه داد دوباره بوی باروت و خون را در منطقه ما بپراکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131769" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
اردوغان : وقتی آمریکا و ایران توی اسلام‌آباد به توافق رسیدن
🔴
دنیا نفس راحتی کشید و نگرانی‌ها کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131768" target="_blank">📅 17:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کِیر استارمر می‌گوید که نمی‌تواند فاش کند از چه ژل موئی استفاده می‌کند زیرا این یک «راز دولتی بسیار سطح بالا» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/131767" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123544aa58.mp4?token=O37cty_pYKNftzf_dEX7U5lamI5iHM7FRDXEJcjDZfCng6YIVMkdlSn-k-11SRBmuVVE1QejUwzhKtPXxYVQ4lcMCvdvVUsmBOD07B7TmhhOmksd-bR7WTkgRirGoJhEKwg032hh19F3EPd1nOacQ45RWmoxLzufpUo7NQ3bAadQEXggDdU7hb5arsBNQHRRkQg0n34w2qKr86VuQhS0-P0ULqFonp92m7gLlxTOwj2NPhG0SZRTqHzXi8Qo6pqSd0WMGddfg7lk9wAd9qD-zBsir7Tlv9QX_Dqf3NUkx82zXttwP08XfZGA0Mt4zol0UIrli8AtrwMSCDl89C8zew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123544aa58.mp4?token=O37cty_pYKNftzf_dEX7U5lamI5iHM7FRDXEJcjDZfCng6YIVMkdlSn-k-11SRBmuVVE1QejUwzhKtPXxYVQ4lcMCvdvVUsmBOD07B7TmhhOmksd-bR7WTkgRirGoJhEKwg032hh19F3EPd1nOacQ45RWmoxLzufpUo7NQ3bAadQEXggDdU7hb5arsBNQHRRkQg0n34w2qKr86VuQhS0-P0ULqFonp92m7gLlxTOwj2NPhG0SZRTqHzXi8Qo6pqSd0WMGddfg7lk9wAd9qD-zBsir7Tlv9QX_Dqf3NUkx82zXttwP08XfZGA0Mt4zol0UIrli8AtrwMSCDl89C8zew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل فعال رسانه‌ای امریکایی در حال توزیع شربت نذری در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131766" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گزارش بلومبرگ، سفیر ایران در پکن اعلام کرد چین و دیگر کشورهای دوست هنگام تعیین سطح و نوع هزینه‌های خدمات دریافتی از کشتی‌های عبوری از تنگه هرمز، از «ملاحظات ویژه» برخوردار خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131765" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای الحدث به نقل از منابع آگاه:
دور جدید مذاکرات آمریکا و ایران در تاریخ ۱۱ ژوئیه [۲۰ تیر] در پاکستان برگزار خواهد شد.
🔴
دور بعدی مذاکرات بر موضوع تحریم‌ها، دارایی‌های مسدودشده ایران و پرونده هسته‌ای متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131764" target="_blank">📅 17:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhucna2DtDVtfyp3SICVvjMRcFJbDhxPOEwC5irnKWQQBv59rPT0xDL2S2zRJGXjsd3JxsTQuyQHbzWlz0QUsa695wA8tHMnN5yy49QcU3Ieecw69LBg6qw2bVc8t-6VZdCUsuoYjnESb7yrDwM7SxrJ9lv7rhepm36n2qG4OHfTgIlYL489XncxJhbxec3t6REknBJp5hw6pCpq3q5EmfhRef1v9bz1g-LdY6X-TdKeQI10yN_X7p7NIRIZ5F7JRPE-iLKIk-GZ813L7Pekg1P2a6Id2HLzbyfswtPX-k1Iy-m_Li-SGdnO3WxWrkke1LOa8YnBXWHS-nq1UKtPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مستقیم هواپیمای باری 17-C نیروی هوایی ایالات متحده از پایگاه هوایی نواتیم به پایگاه هوایی الظفره امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/131763" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=sQlrPPTl_Q_-7NDaApp62-wJ8nomxHbm-oEvt-YZHUvcw0s94ELGdrb_c3n4XuRS3m7ykknlpAutrQhl8-VWUKQnmGNuL5GuPV8KppspraYLdjlfbfKMRgTYb7I4zmWbidQ4SO-KzVSNFS8j7TDyITUWU-QCP_0cGSt_ERKUsskA-uWb450_aeG7kudT8oW0y87ID_eHkze6yZvscA4dDciu0sJxGhrBWgQpovm3p39b-gA1T7FGFauOIKtKm-BfULlq-HtH7YWIeItBFYg14gmP0VxGZPbEEtCbrt1oVdKaVo9yj6v1COY_IFS4v6gtDS5jSjivcQI9BDYKcfnXjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=sQlrPPTl_Q_-7NDaApp62-wJ8nomxHbm-oEvt-YZHUvcw0s94ELGdrb_c3n4XuRS3m7ykknlpAutrQhl8-VWUKQnmGNuL5GuPV8KppspraYLdjlfbfKMRgTYb7I4zmWbidQ4SO-KzVSNFS8j7TDyITUWU-QCP_0cGSt_ERKUsskA-uWb450_aeG7kudT8oW0y87ID_eHkze6yZvscA4dDciu0sJxGhrBWgQpovm3p39b-gA1T7FGFauOIKtKm-BfULlq-HtH7YWIeItBFYg14gmP0VxGZPbEEtCbrt1oVdKaVo9yj6v1COY_IFS4v6gtDS5jSjivcQI9BDYKcfnXjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز : هم‌زمان با مراسم تشییع رهبر جمهوری اسلامی در ایران ، آمریکا جشن دویست‌وپنجاهمین سالگرد استقلالش را برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/131762" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، هند و ایالات متحده ممکن است در برخی اولویت‌ها اختلاف‌نظر داشته باشند، اما رقابت جداگانه هر دو کشور با چین همچنان به اندازه‌ای جدی است که همکاری راهبردی بلندمدت میان دهلی‌نو و واشنگتن را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/131761" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس: پول دادن به مداحان که دیگر در تجمعات شبانه حاضر نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131760" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه تلگراف گزارش می‌دهد که یک ابرقایق ۱۳۳ میلیون دلاری که گمان می‌رود به ولادیمیر پوتین، رئیس جمهور روسیه، مرتبط باشد، به سمت بندر مورمانسک در قطب شمال در حرکت است تا خطر حملات پهپادی اوکراین را کاهش دهد.
🔴
این کشتی ۸۲ متری گریسفول توسط ناوشکن روسی سورومورسک و کشتی گشتی وووودا اسکورت می‌شود، در حالی که ناتو کاروان را زیر نظر دارد.
🔴
از این قایق تفریحی در حالی که تورهای ضد پهپاد عرشه آن را پوشانده‌اند، عکس گرفته شده و پس از ورود به دریای شمال، سیستم شناسایی خودکار آن خاموش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/131759" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر، محمد بن عبدالرحمن آل ثانی، با وزیر امور خارجه سوریه، اسعد الشیبانی، در دوحه دیدار کرد تا درباره همکاری‌های دوجانبه و آخرین تحولات در سوریه گفتگو کنند.
🔴
در این دیدار، آل ثانی مجدداً بر حمایت قطر از وحدت، حاکمیت و تلاش‌های بازسازی سوریه تأکید کرد و بر حمایت دوحه از آرمان‌های مردم سوریه برای ثبات، ایجاد دولت و بهبودی بلندمدت تاکید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131758" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
