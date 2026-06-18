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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-660805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNYq4Oy-0mp2tRJRp8IgFqoD5Nqh19rG_LnGbwi23qJ_Q8NoRDas2tGZXYrcO9xYDKromt31dfjiH_DsUqxIyPwPj3M5INZMT7s412jFeKFe9BDfUqGCpkEMhB1ZVAjmxilXTSG-0x55xDH0FuyMwppHJ0D-w_Iz1U4Ko20r3JjquXV288LA-fB9y7TN-HL-PvE1uQ-ScgITMfXS_g9CLN42hGy8om2wgDbV71sOghiBdvc9xbyiguZSggxsikYuSQd1G4U1ltyzyhovlU_GGLSzncGwXWFQC3OG20ekC7oRaU1ohT5xYOfcZqOd2csPMeBiAcF-B5N6ALFoz9QgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/660805" target="_blank">📅 14:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3660da3d6.mp4?token=ANU93xqDllcAjcMH3EKbatR2y_-skM0aifGeTt6RYiRj9MmF2B5FgAPpwB6F1LoDkww1sExhCEJMhueOOG12PAjsS0aeGWHMeEeOAuz1KimCKilIthnxGu8d4zGsNy1xUWtfMSjgwgvADFe3xiid55YLCrxJe78VS2R670eyP6zASDbMqSmPZQYb3myi1Mhjis8aDfLYPoETXUJ1GzORHpSabGTbmqIuU96-Mqwnsv3oXsyviEGaXQq4VLxofi3PNg5Xc-Blc0rMSRvcz7DkCoibq6aiENcJszaEnic3UdxuOD3FJr9n9DoK3gJKk6ZFiBZ9HMpZonJP1yCvOHpASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3660da3d6.mp4?token=ANU93xqDllcAjcMH3EKbatR2y_-skM0aifGeTt6RYiRj9MmF2B5FgAPpwB6F1LoDkww1sExhCEJMhueOOG12PAjsS0aeGWHMeEeOAuz1KimCKilIthnxGu8d4zGsNy1xUWtfMSjgwgvADFe3xiid55YLCrxJe78VS2R670eyP6zASDbMqSmPZQYb3myi1Mhjis8aDfLYPoETXUJ1GzORHpSabGTbmqIuU96-Mqwnsv3oXsyviEGaXQq4VLxofi3PNg5Xc-Blc0rMSRvcz7DkCoibq6aiENcJszaEnic3UdxuOD3FJr9n9DoK3gJKk6ZFiBZ9HMpZonJP1yCvOHpASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی پوتین را تهدید کرد؛ اگر اوکراین بسوزد، مسکو هم خواهد سوخت
رئیس‌جمهور اوکراین در یک مصاحبه با تهدید پوتین:
🔹
اگر پوتین نخواهد این جنگ را پایان دهد و بخواهد آن را ادامه دهد، ما ساکت نخواهیم نشست. ما پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/660804" target="_blank">📅 14:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb1bea6b1.mp4?token=YoVi9baxaBkdVcAIWU9TuqYVWIBnuvKVnJgWBdrTe8af9w8Kuh-YEjC2Gp0YRJpu0Em4-JRlXhZrwltvzaduMC-bvPZyJkeKiceCoSLWeeh1EaChUHH0QJvz7TVW-rLCqwxUeY8FoR5YvY7qXiyzjCwwfEfdy4wUDHk1L6ZjHQBvvw_Ez695UhLZp6uGzEUXoJUm1WvuWPZpZ7akRjPGDdphoTyHX5N_CovfnGMo9xK5fPyJ89PrYDVyT_tIg-zMDL7Fkrhc--qU1-Qok8_hWmcb7p11U9AreXXVO1YaLQnH4Gk3s5Lr0w1Hz6eWtGRV1xkrw21_iUOGOk2jm65dsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb1bea6b1.mp4?token=YoVi9baxaBkdVcAIWU9TuqYVWIBnuvKVnJgWBdrTe8af9w8Kuh-YEjC2Gp0YRJpu0Em4-JRlXhZrwltvzaduMC-bvPZyJkeKiceCoSLWeeh1EaChUHH0QJvz7TVW-rLCqwxUeY8FoR5YvY7qXiyzjCwwfEfdy4wUDHk1L6ZjHQBvvw_Ez695UhLZp6uGzEUXoJUm1WvuWPZpZ7akRjPGDdphoTyHX5N_CovfnGMo9xK5fPyJ89PrYDVyT_tIg-zMDL7Fkrhc--qU1-Qok8_hWmcb7p11U9AreXXVO1YaLQnH4Gk3s5Lr0w1Hz6eWtGRV1xkrw21_iUOGOk2jm65dsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از مساوی پرتغال تا چهارتایی کرواسی؛ دور اول حوصله کسی رو سر نبرد
🔹
قسمت پنجم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/660803" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1irBYp7WVhUwrOsdWPFGeJ3YCPRpxjqa0YprG9u62CiZ0zvfq8inXlqcWhhc0kNFbuKhhjg3Gtl5aAdWyY8uPpag2cGb-1gC0k_KXg8JV2g2T5kB4aszrHrgJAnB3PMWJXnwjzSJ8SB7vs9eckbaiTOo4ETuwHrVhDJSDwhoL4YsV6pv33a28xA9_4IPhTBkgmjH29k5ntlznt8lS2Tvlw9UBWYpHwUO6eKwhfoztiazoeKu48FeJyL4B9ELYBvtgpUp7no-MXk-kpQG6ipN4SK37C_AYbeATtzChNBPBXIob2vJEwlbvPapHyCv5JeNQ_jC1M7Pk2JDd80qSdPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کشورهایی بر سکوی المپیادهای جهانی ایستاده‌اند؟
🔹
چین در هر پنج المپیاد جهانی ریاضی، زیست‌شناسی، شیمی، فیزیک و انفورماتیک رتبه نخست را در اختیار دارد.
🔹
ایران در چهار رشته از پنج المپیاد، در میان ۱۰ کشور برتر جهان قرار گرفته است.
🔹
فهرست برترین‌ها نشان می‌دهد کشورهای آسیایی سهم پررنگی در صدر جدول المپیادهای علمی جهان دارند.
@amarfact</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/660802" target="_blank">📅 14:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQwcjxsIoXZXD1SRUX20xP1Rz35xtV1B7S5Dy07-W_Fdw3cyg3xNBbOh9L72ScrByefdZzRlK0F2QJ-N_Yj8etS-iIbapz-gSiIPRsh0cBMuYHYHo8wQAAHpbcRRha0kNb9gQ2eECJHbUXaWk3hkMTjQDO0MdX8LYLjjGeXlmzZBpm-PfLd01y-iDwMKxwAu39APlGnPGNxLrm6neBSDdATrIQ913VqF6BTRoCxGQjw8JDt_xLJBz5Qi0B8kwDO5qHWQjIfW1jlnqo3Z0o6r2MH2raVuuwfJVqZsPNHiuF57MSO8MGghlgFbzFkooD3d9owZHIBrtnEramZxD2kuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال گروسی از توافق: اکنون نوبت کار فنی است
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
خوب است که این تفاهم‌نامه (آمریکا و ایران) وجود دارد. اکنون کار فنی آغاز شده است. اکنون زمان آن رسیده است که با همکاران آمریکایی و ایرانی خود بنشینیم و تدوین گام‌های مشخصی را که باید برداشته شود، آغاز کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660801" target="_blank">📅 14:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX054MQLcv1cQ1g5BSMab4ybSnlaj5gsnFejsWTbK3hLSRMmKYOE7R_qPPNwSyL49hABOFQN3v5hLHlLRdcp6E-wdQoAjG0ZWN0-DcswxfGPMFitScLcfGqIMXERqBzzHhBzB4D8YhEWxZvT_ujEF995faxnW36Y5z5iuFsKwqTMroabsPgeMcjFPrzkso3Mg9fZ2D5DZ8sFz0BtihETkO98-dQYqhYUhggnDRQyrr0Z7yc35NnAXNTfWtWAI6fHmk6r1FvIso3pXvF7MiqeCqqahd6_ld19cGU_lFr758-heuS6h7mP82kxeV4eedb1hAQvS_Ld5cXhhqyXukZ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«آندرداگ» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/660800" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تیزر قسمت هفدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم راحله خمسه که به دلیل تصادف شدید در دوران دانشجویی روح از جسم جدا شده و بخاطر تجربیاتی که در برزخ داشته‌اند تغییرات چشم‌گیری در نوع حجاب و رفتار ایشان بعد از کما رؤیت می‌شود و همچنین ارتباط با ارواح بعد از بازگشت به دنیا ادامه یافته را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: راحله خمسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/660799" target="_blank">📅 14:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtoGemK0-8IMtjRht_17akmdNDgLTEn-oaZteZnDRN0tIcBiNXWkDMs9h7ri5vGzHACPDSQZJExnoyZVo8kvf5adl4wtFp82YcSu9WrfYYLHtbPDP7Z7leO9AK-SKLs356gZyplhG57h2lZLKmT-yACXP96q5cW67ax8xsSo2mvD1CV-9y4iDWW4AnyartzMiPwv3F8PlNbqsq76efvaYYPCBQIho3CfyZyLdC_BDwJ6ld9u59stDNiFLY2d0cqP8xUwDmR9b4iY1sbHY6fFc_LPmWhrTROlY5ADlslRvt-nDVeb5WiAfDN9hOCoIJ1e3KGI9koV04N3sBtO3yjwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که آمریکایی‌‌ها زیر پست‌های جمهوری‌خواهان و جنبش MAGA دارن منتشر میکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/660798" target="_blank">📅 14:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1e2cb577.mp4?token=fdWrf1GB_DMlvaOV0YaD1618DpoTXcxuoJxg6B8Tj2MNeHs5596yDRZssK58RH01h06cLBkt_8YumiurarVuq8BeVpH7LCUwQ6wUu5bkrO4dmtz8XGcHoiwGTW_OA9FYHx8i6dQEUS3PQrZ7w-GoJemiBfIQuJRhNQcV7weZNCS-ccqJwe4y3lnOsdWXNSQs70gDqRNb6ONvq-k-LZbK62E64Vk8pirNaTxI0EH5--nVuK8wB6Qa0maZE9c8ghDf9gEu7KeFSMcARQRF15QPV5NUTgc7UQhWPOSaZqVME2qjsmcfUDlAVugHu3PSSzW9_oxoUexMS3HOnSYnMe5CY308YjL-VNnRUEUMxOHRJB4_dTbKsVmAYd8YdVMPrujoXpmO7JbPyZGiPdgVFzKQqAAEyWpEdQ2plP9Ue7P6aaHqV9be41xceLJC8J5XHPU09nOjeL98vYpw6rattnyiQTMzU17ATD9lujCJQ8nIssnyM8dNWStJMy5KCnKwFEYlP_CTNAzV_AHoqVkZeaYF6TJs2yQqxFGrbmPmViOOiEx9IgDPBRy65qS9x4S0hzsimy_U89WMDOfF5Crg57c-32-rtRVO-Vbvye-P-m5C5vq0hGIMMl5Nq3XtFWnlrf3w8KWsJiTD_UVN6XZdH7BJNJDhAUHPwRI417DJz7d9om0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1e2cb577.mp4?token=fdWrf1GB_DMlvaOV0YaD1618DpoTXcxuoJxg6B8Tj2MNeHs5596yDRZssK58RH01h06cLBkt_8YumiurarVuq8BeVpH7LCUwQ6wUu5bkrO4dmtz8XGcHoiwGTW_OA9FYHx8i6dQEUS3PQrZ7w-GoJemiBfIQuJRhNQcV7weZNCS-ccqJwe4y3lnOsdWXNSQs70gDqRNb6ONvq-k-LZbK62E64Vk8pirNaTxI0EH5--nVuK8wB6Qa0maZE9c8ghDf9gEu7KeFSMcARQRF15QPV5NUTgc7UQhWPOSaZqVME2qjsmcfUDlAVugHu3PSSzW9_oxoUexMS3HOnSYnMe5CY308YjL-VNnRUEUMxOHRJB4_dTbKsVmAYd8YdVMPrujoXpmO7JbPyZGiPdgVFzKQqAAEyWpEdQ2plP9Ue7P6aaHqV9be41xceLJC8J5XHPU09nOjeL98vYpw6rattnyiQTMzU17ATD9lujCJQ8nIssnyM8dNWStJMy5KCnKwFEYlP_CTNAzV_AHoqVkZeaYF6TJs2yQqxFGrbmPmViOOiEx9IgDPBRy65qS9x4S0hzsimy_U89WMDOfF5Crg57c-32-rtRVO-Vbvye-P-m5C5vq0hGIMMl5Nq3XtFWnlrf3w8KWsJiTD_UVN6XZdH7BJNJDhAUHPwRI417DJz7d9om0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت مردم لبنان به شهرک حداثا
🔹
ساکنان شهرک حداثا در جنوب لبنان در حال بازگشت به منازل خود هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/660797" target="_blank">📅 14:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Lha3sCsoX7_yeeQMqH9N72uhkeyT1f1gmzlFSu6jUArAdtRyEC-7DTibg5j4ZgamTyYoAixVwKHDr3XrWX_Hfyn5i02ikAGa35HKhXbiavMe-WoNA0Wh-jOoLSZNVf_L2JexeF8xNF20KQrJ63UqQqtGmCURs8MWJ5Zgy_FIz5a1_lcb2H1VhP8WLFYu8UxYjetDgIwd-YDstz6f-NSnrAaaHrMJyT6Lp4RD-NhsIRX2En0TW6o3I6dni5d23sX4S1t0FnMPjGXWi34YzD_aAOnvWqdK459IkDtMNT9AR0jLkVJkVvBhtD2BukMNMqFnuDhoRUfVYht1FdIkLycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/660796" target="_blank">📅 13:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سکوت معنادار نتانیاهو پس از انتشار سند تفاهم ایران و آمریکا
🔹
بیش از ۱۲ ساعت از انتشار رسمی سند تفاهم ایران و آمریکا گذشته، اما نتانیاهو که پیش‌تر از «پیروزی کامل» سخن می‌گفت، هنوز واکنشی نشان نداده است.
🔹
همچنین برخی گزارش‌ها حاکی از نارضایتی نتانیاهو از مفاد تفاهم، به‌ویژه گنجانده شدن موضوع لبنان در چارچوب آتش‌بس است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660795" target="_blank">📅 13:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMWPjZ_NhvYm4f_fmJf5URNSOWU4Myt7z0zfgDdukqnA0AJ49_JhDS20EceKBV1hKWwf-q591VS-b0YsRBJk3At1hhWCuHuvkZ-6sM1BeatqeRPWgT5SUhJlf_OpNBVDfoAUyl46d9bAIuTuJ_yF9mSa0bRem_pnrZLH2-GcvbpXgtGTsYAdDfrgAb_jCOV8EDF3gJrCCVUDnnT-c7sdrnbPxPZAjwQX64opeCFbrJLgNlod1mBNwmO9QudzrhrpRvCskZ_zPigbmBxnfuLz8pLCBsyHR-dmxFlqQyRRnqCFp9OJk-IjD20vLWlwQsAHRf58NPUB8tHXtW8iMtUY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گلزنان جام جهانی در پایان دور اول مرحله گروهی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660794" target="_blank">📅 13:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660792">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله اسرائیل به جنوب لبنان یک شهید و یک زخمی برجا گذاشت
🔹
حمله پهپادی امروز اسرائیل به یک خودرو در جنوب لبنان، یک شهید و یک زخمی برجا گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660792" target="_blank">📅 13:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e201c6ac.mp4?token=rzKTbJM_1NGY04FmdeC3FfK-42iDvc6dLaJaxD4K6KS0d190adZ3RZBWcMpNikxS_KXGgEWvmJ3iRYxsQL7ES_14iQJ-uEPdyba3HaPSbkabHBu5uFSDgJZOLaDfwplVYSWvCA2ck0U4tMTd9Ro2C1Z8kMHyCRWyN5V9MDCC4bly1Mg4iOoTECLqhjXAUYlt4_y_30f5UyRoaAa6zduiRgAaXx07SP4G1TUWtQdwsooy7qvgpJ4mJ5YKXGSXTrjbqCUbdvbURBQh4iohYtunevT4hnH0daD1OXGmP98XEPBLIWqgtyCorT6Auyx461mUeZt4jgcGo-iWi9TiYyt6Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e201c6ac.mp4?token=rzKTbJM_1NGY04FmdeC3FfK-42iDvc6dLaJaxD4K6KS0d190adZ3RZBWcMpNikxS_KXGgEWvmJ3iRYxsQL7ES_14iQJ-uEPdyba3HaPSbkabHBu5uFSDgJZOLaDfwplVYSWvCA2ck0U4tMTd9Ro2C1Z8kMHyCRWyN5V9MDCC4bly1Mg4iOoTECLqhjXAUYlt4_y_30f5UyRoaAa6zduiRgAaXx07SP4G1TUWtQdwsooy7qvgpJ4mJ5YKXGSXTrjbqCUbdvbURBQh4iohYtunevT4hnH0daD1OXGmP98XEPBLIWqgtyCorT6Auyx461mUeZt4jgcGo-iWi9TiYyt6Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور ارشد آمریکایی: با ایران سند تسلیم امضا کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660791" target="_blank">📅 13:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fno49PS4ivCU8O5cga0SzUu5yW74xfbVNUmDVnrOIyNJfPUXX1wy-gC1PMrvHgDJYXu0IqctAj0dZmLr3s_L5cWdlITvjhq7usizCGsFTpHU5oUO3Qjg7AKbZJ73XmmZ9sJnZuIpgfR3ZGC8twKBkyeii7C3Jiv6LU3eAIBF0sINCw6R67dffMjMptDski8__1MrhmGepW3_uo69Pmc8lzsNFonpwtNByWrGstEBUrTV0101PagT7GM1GWrS763A4ss_ZK1073HufYrH_QlY_bUy74qufUUXSYZODwwOCbbv8v6F1KbEKNT8PPqqhmwsBzJBuSFScuEDApUXINgfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف تلویحی خبرنگار آکسیوس به «پیروزی کامل ایران»
🔹
باراک راوید، خبرنگار آکسیوس پستی از یک کاربر اسرائیلی را بازنشر کرده که در واکنش به انتشار مفاد سند یادداشت تفاهم میان ایران و آمریکا نوشت است: «به ما وعده پیروزی کامل دادند فقط نگفتند که طرف پیروز کیست.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660790" target="_blank">📅 13:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b647c3af5.mp4?token=rTUkO-hEJtc8XhFjy3osMMVIDgN9PCxKF7L5Zx3VQO1Mm_HnUwwNQfLhIZPV3PqifS-FEi83vInKvTUx-vDEUp5KA4kWE7f02ShhSgcaqJqtwy0Cm4fmXPV5O0byn2Fs68sBAYuGz1S5P51brpuNlod5ie8Xx8NNA1sFaGG97-Hfq9LIbuQFzFyan9TSuvyasbJxUC_-jpv8cJgjRuj7mbInZFB3AXeKflOG4RPpNdxeVV9qEGbCf2th3hZDwRH7xa-uGYTVBxGqOqvKBaMxpCtr8n5xEQtTEg8WMxewnWyxsAb2cAnLC3aN8v5NhA58RhvnXJkXTL5zYVJC68qCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b647c3af5.mp4?token=rTUkO-hEJtc8XhFjy3osMMVIDgN9PCxKF7L5Zx3VQO1Mm_HnUwwNQfLhIZPV3PqifS-FEi83vInKvTUx-vDEUp5KA4kWE7f02ShhSgcaqJqtwy0Cm4fmXPV5O0byn2Fs68sBAYuGz1S5P51brpuNlod5ie8Xx8NNA1sFaGG97-Hfq9LIbuQFzFyan9TSuvyasbJxUC_-jpv8cJgjRuj7mbInZFB3AXeKflOG4RPpNdxeVV9qEGbCf2th3hZDwRH7xa-uGYTVBxGqOqvKBaMxpCtr8n5xEQtTEg8WMxewnWyxsAb2cAnLC3aN8v5NhA58RhvnXJkXTL5zYVJC68qCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سناتور تندرو درباره موشکهای ایران: ترجیح می‌دهم ایران موشک نداشته باشد، اما معتقدم باید بتواند از خود دفاع کند، وگرنه جنگ بی‌پایان می‌شود و بدون نیروی زمینی نمی‌توان ایران را به تسلیم کامل واداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660789" target="_blank">📅 13:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRtdRh3eSXBUiq6K9AG1xXJZqZKNWZDiXL5ki5h5kZRt7HVUubOMpUM5X0PRTTSUVnL-NEzZSDFqKQksr42aBbqpbZJ9YiUYBM6i34fMs1brKbKW2O2hEvJZ3NOkZ0xpPceq7tDwtZzOHIZQGtQ41ZKBAyzdXrNBFyHUvyyZUrVcf4GcVLcak6berh_okLEZQRL9Yr0Pd5C77C-HyzfyGqYyFAl9ys6-mXyq8y0fJKh55V5lJEJQZF7TekvTNdbGdDQBsuDN34OVdI6HiCjMkn5-56rI0X73ySF7L6UHUdTpEX_6x3tt_V_AqMtxY3Lq5jou-CFn8H5zQr4e_Ob7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ خرداد ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
قیمت دلار امروز به محدوده ۱۵۷ هزار تومان بازگشت و در میانه کریدور ۱۵۰ هزار تومانی متوقف شد.
🔹
این عقب‌نشینی همزمان با آغاز فضای جدید سیاسی و اعلام مذاکرات ۶۰ روزه ایران و آمریکا رخ داده و باعث کاهش تحرک در بازار ارز شده است.
🔹
افزایش خوش‌بینی نسبت به نتایج مذاکرات، تقاضای سفته‌بازی را کاهش داده و قیمت‌ها را در وضعیت نسبتاً منجمد قرار داده است.
🔹
در همین حال یورو نیز بدون تغییر نسبت به روز گذشته در سطح ۱۸۰ هزار تومان معامله می‌شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660788" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGy4o7q5kh3eCRZu6vB_4xLCsVx2zcGy5x7EUm73Ew0SNfpenHSqLDABppagB_0PJmQzhea89Op-TAZunzS0560J7L_Y3n4VeILQ32v-dtWDkfgoqnVELeEXXOg2WNrqVketLyYj3InTr9gy4cGErIoo-etqhmRRdLDWUmP_Wtm1rVPyeIsdSB2h0GO43fh70okC2cHZsbX94unR5047B6J-6WnE40HBd0gagZAtZgZozsnGH77nXyGpV8m9Fc0v0Szx39H1FUbg0Tr76R9_AhfxuwLxUCRvTjKBNcOL2Z1ILcK-g0OFQ7_H-zh8fyAqaW1u8pV-FVbXjj0I5MgQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای جلسات فوق‌محرمانه ترامپ | خشم ترامپ از افشای مذاکرات جنگ ایران | احتمال ضبط گفت‌وگوهای طبقه‌بندی‌شده
🔹
مایکل گودوین در یادداشتی می‌نویسد گزارش‌هایی منتشر شده که نشان می‌دهد مشاوران کاخ سفید به‌طور ناگهانی نگران این موضوع شده‌اند که گفت‌وگوهای فوق‌محرمانه درباره امنیت ملی در اتاق وضعیت ضبط شده و به نیویورک تایمز درز کرده باشد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223914</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660787" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660786">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
نانسی پلوسی: توافق با ایران شکست برای آمریکاست
رئیس سابق مجلس نمایندگان آمریکا:
🔹
ما یک توافق خوب با ایران را پاره کردیم، وارد جنگ شدیم و متأسفانه شاهد تلفات جانی نیروهای آمریکایی بودیم و این یک شکست محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660786" target="_blank">📅 13:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4Lh0f2dajyaMCDKECP-DCgKfqNW7hAHLvpWLD1V7iUbIxxa_hUXwFtCT94Vov6eL6-FDqPGJXg6gDRWK79uGqXimsWxAzPBr0Ox0CDYXqiN6gpU6bzMyJ_LnGnM6zoWWotHrcxq0D8e-9pt9tLxMaf1DKkP9Rh2j_f8ismN8_37HaRKEEvHF5gJooadyRrWtpYWPcp2zRoDex6ZwK1s_uW3LtHOJ7BQ3UL9NsY_1CVMavjcU3eBAoBFAaAe0g_FBfVXxBxl-JEafE9_LkrsewrO2ieNYQoW7xX5XOZiS8GiT6XSDdkisgFp7JPrHD45ujW5-yonsJXxYPCf29N5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم
🔸
«مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ فَمِنْهُم مَّن قَضَى نَحْبَهُ وَمِنْهُم مَّن یَنتَظِرُ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660785" target="_blank">📅 13:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rawbG6taLGIS2BOPxpmHJeZAjD8OAba-CPO6LZgi6LedK7gledNkVqMloKvqYW_Z78qtv4fwNq2bljX5R51_DRiZ_yEbV36e0Zbarnj7VeFJoDTrMPY0hNYWB8hTMFC7CNDguJVofJBnm0O5_j_8o5Cr2V5zS-ePvc468j1JVPym1B4ii7NErLqseBYnTuPo-utFSsZCSeHlZcCggd9TFw1EU7jZXHDQboTSfFECJg3LaIIgnsBWAUrkiULVFHOV_9I3_thS6wlnGUWSZWL-qzH10nUF70X1pTfJoxTgKp48LzI71YDGBzaWlPNDt1cK1-bwkKL7kgEOUqG6w2KybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طالبان استفاده از گوشی هوشمند را برای همه کارمندان و مجاهدین ممنوع کرد
🔹
متخلفان مجازات شرعی می‌شوند و دستگاهشان خرد می‌گردد. تنها استثنا با دستور کتبی رهبر طالبان ممکن است. هدف: جلوگیری از درز اطلاعات و کنترل اخبار. نگرانی از گسترش ممنوعیت به همه شهروندان.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660784" target="_blank">📅 13:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21440bf8c.mp4?token=UIF7fO1s2RuC5TEWr2JIYUcRg8tF8wJKtifL_DXKFJKV9g32dMUqhdPxoXvvPEjUhj48wesCbO1BjWo-Oz72n12g04f4_tqZdkztIG0Mmy2zzLoCzRTKVPzqdnXc7dxeduGO43LpwEes_UVGFX4PMuI8yDQ5fOuEBHkdUjLP_0MPlUBegIKeq2JQKHGF6GHdepewwr8p-tZZ3uWMc_sASMBO829VApPZVFEEK5i4kFELzJKF5TzfhTd4zUcqKWlMcGTLFuWZSnv5KJaZ024afI5Bvq2Tjy_11aVaayT97145s-rXmLj6cc3Hk5Z-v5yoIGOsEtxRvdmwT__sJgMshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21440bf8c.mp4?token=UIF7fO1s2RuC5TEWr2JIYUcRg8tF8wJKtifL_DXKFJKV9g32dMUqhdPxoXvvPEjUhj48wesCbO1BjWo-Oz72n12g04f4_tqZdkztIG0Mmy2zzLoCzRTKVPzqdnXc7dxeduGO43LpwEes_UVGFX4PMuI8yDQ5fOuEBHkdUjLP_0MPlUBegIKeq2JQKHGF6GHdepewwr8p-tZZ3uWMc_sASMBO829VApPZVFEEK5i4kFELzJKF5TzfhTd4zUcqKWlMcGTLFuWZSnv5KJaZ024afI5Bvq2Tjy_11aVaayT97145s-rXmLj6cc3Hk5Z-v5yoIGOsEtxRvdmwT__sJgMshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای اکسیوس از انتشار متن کامل توافق ایران و آمریکا
🔹
متن کامل یادداشت تفاهم ایالات متحده و ایران، توسط یک مقام ارشد دولتی در جلسه توجیهی با خبرنگاران آمریکایی ارائه شده است.
🔹
این یادداشت تفاهم پایان جنگ را اعلام می‌کند، از ایران می‌خواهد تنگه هرمز را…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660783" target="_blank">📅 13:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8PVGamkA1d_gPs6Av0jNEZCzptNVd6WoYgCzcXPqR6-7ZGysUxabjGIOdrKH-FyIfZPwCtqXrh9UVDbbOwiBSoKsf1BRv-JlZeznF3hKVHKRshtyy1a2_rIvkv45PObkU2rM5sT7mv-pIZ20aFs23KZI-f1EBtx3MBzfy7S4-cvIqtmQoeE1iMwcMcpa2Y3fBbWCaGkPc2I_DXlV5-l7TFaNupDfk0xf_F-_wESNCMYj8cYeY1wGkn4ZI_wIL7d-hauivKSoqQ3gCVS3HMFp_ulg-W2Jh2O_IryQvkv-1TzNykd35xjjsMO4BxxswGvVR1NiZtzCEbqQC1B-AlV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pg0R8KuowwzgM3rQhoNqkgbuqi05dnWhrwUnk1hsu6zp7B-etDPssp7r8MsGu1sw7uBVoG_2U3P_FsO82_jkbJMeufwzKlNGkNFTEHowqbmFQ9AECSPLZ8rGEydWE-lhteU-QZ5IBQNzW0B0YZOwXy6Ul1uIK0o41AXtTUiXK8pJsL0aitF7ubTYObPxK0Y6xaEB10Ilg9dPypDFWCKPDXRAB0Enq2tX6PoEiI-MGdRyo0URb5Z3b2UhDMAUYX6paZ9FhNZ8-azAR_G0ZELoRY33UI4yzM5nWnwD3DL2XKZMoD-ZZLjVjvgFaKWCoLN_7olwctwUOUePZtXDq9136Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcmh5hCAR7-92HCLUClA-AX0OiFM_DymicotqgvRiFPbPANHL945354hVk8cUoUS5UKPhOIu-44noyFQ5-pb8Jaw_vHEfq_W3u58teltKASl2kefioJY2hMT5ecschZeZz_ABDjbPzLfheJSn9lKnTNYjKA0qTb0FAkg4B4Q_3quTflIOvKvsTlFQ5s5yiciEcGVBLkbP_i_WN2q27xNY3TsnUOt-_it-SENeLUIlnLnSQDn1MoxLbEOY9Jvz_A-O-1Pk0J-3EoKvarCmR39Y90N3-UhuVtfyYuEoRsU6VzOM2PuuQigPZ_epXbvqW8h8gi4nPzwJM-hXrOuzdoezw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18315aa54b.mp4?token=lesbUTxMNWcSZ-MO6Rh3CubUmEeB8o9eeLJMhcoEjAFMMPtdouLvFNxcVqQE8A0U_2zY9xv_oob49G3ZliNL2AstYOK8Virn6Wdn22OuQT3ab04felNRsqZKqP3Ppx64w-MIUonyDCJkoOpTJ72iNhNf661Smsb2BV7RCZlt-jrzOEGyfvRO9Wr3bRR_AB0jtC0iamn3eGDa-oVJ5BEZwFUbl2muzTLdeVNwKquRmzs8A_xmHv-7wdnFSARFOjUocEdB3Odqd6KQqEQ-vehWwX7U7PrkFj8q5VL2jY-EAXwd2iWV5x9yPNJqLh3m9iSHaICDKjY9HwY4AlLxTwai14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18315aa54b.mp4?token=lesbUTxMNWcSZ-MO6Rh3CubUmEeB8o9eeLJMhcoEjAFMMPtdouLvFNxcVqQE8A0U_2zY9xv_oob49G3ZliNL2AstYOK8Virn6Wdn22OuQT3ab04felNRsqZKqP3Ppx64w-MIUonyDCJkoOpTJ72iNhNf661Smsb2BV7RCZlt-jrzOEGyfvRO9Wr3bRR_AB0jtC0iamn3eGDa-oVJ5BEZwFUbl2muzTLdeVNwKquRmzs8A_xmHv-7wdnFSARFOjUocEdB3Odqd6KQqEQ-vehWwX7U7PrkFj8q5VL2jY-EAXwd2iWV5x9yPNJqLh3m9iSHaICDKjY9HwY4AlLxTwai14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پهپادی جالب از گردباد افینگهام، ایلینوی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660779" target="_blank">📅 12:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ حملات رژیم صهیونیستی به کفرتبنیت و حداثا در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660778" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKe9uhmfgML1le-HjS-yzJU8cyugv7vPZJYhJgGwq2-4Q-jpaFH0pIuSWVQmZqDz9xWc3m63cbyaJyyqV_2yfvuBPcbSTOv7m_f0nwhlj_t4o-qNB_sf0c5xthGdLJ5_GVb1uEZQW1d3Jb-qS8gW9DQvcQMkrExgDHhx3iBE91mOXkvJ1uef5im0P5d1hDMgSRb1aMSHOR58q1fpn7IoWUyIywFYaJgLkmrwHLsbwuL9Aw2vBmAsldcYEkV_H9uh2-QUwgZYQqtvKWdlcAX08vkvVFIU9ESFP6ZXEQmfwN7Q1HpTJhxeL3tJqoRxLZ4ooWFBMeQHQjouQW5ARng42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور رامین رضاییان از ایران؛
ترکیب منتخب دور اول جام جهانی از نگاه «Who scored
»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660776" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ترامپ: منتقدان به توافق با ایران حسود هستند
🔹
رئیس‌جمهور آمریکا در واکنش به منتقدان به امضای تفاهم با ایران در شبکه تروث سوشال نوشت «این احمق‌هایی که فکر می‌کنند من به‌اندازه کافی با ایران سخت‌گیری نکرده‌ام، در حالی که بازار بورس همین الان به بالاترین رکورد…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660775" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5NSwdTkCYIjNbJcOgmAXky_RpRnzajqCE8zC0-SYA3peZXnHEacrxIDzV_uTja8VQ4gcTmCD-XYcDAhM9SUC43wO0wj9Yl2SWbQ4N230YVHzGaLVvIHXOT3ivuHw_bHCHDa0sYJor7XasMRyluNqGsAmmEwNYJGCNlYMnsXlyaWUWfsoq7DcXsmN4n_1Q1-0BE9wv7vkaXMQJv7sjJt9AEq8cKrpn_wSii8aEwVbRNqX39Kn-guXwR75M2ZTd-SR0rvkF5sZ-yMgnC8xKtl-H9zsb36-D9rpA5F4WCuN7LlPzAiY0WBIGgRoVrmULpO8oAa14rMHdM3EdxZirAIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کسانی از توافق ترامپ با ایران ضرر می‌کنند؟ | جنجال در میان جنگ‌طلبان واشنگتن | ترامپ از ایران فریب خورد!
🔹
پس از انتشار گزارش‌هایی درباره تلاش دونالد ترامپ برای پایان دادن به جنگ با ایران از طریق یک توافق، چهره‌های تندرو و نئوکان‌های سیاست خارجی در آمریکا واکنش‌های شدیدی نشان داده‌اند.
ترجمه گزارش ریسپانسیبل استیت کرفت را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223852</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660774" target="_blank">📅 12:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4GOm4BzLE-JdvkQXotsJlOIPgiEUxGV4fn0hfWnISAiubpG95dnvZd_bv_0VH8kknnKHELEvTdf9qNy_z3YhDnER49FkdTNcyFO77qnewAknQiQn6vcOUPXHvNF0elYwhT20-xL-NDCmNT4rbBhcYjI6Ctbi4HoCWYGgqr0qquz33MbiwEjGbzzVLTFydB60W_RLvqQc4rsUEJvuvRMyFaWRdp-kc6BJGU7GU5CMAZyLoZGRLtaB7_VISNN0PEleOXFlICD94FhX349D7XwOd5eVnGdK6pA9PjU0kKNYpy35E2DE8EOEKzTbhFWRRySyHs8I9VnQwNZip4jSpxGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOnTuG0gY1jj2UgEMg5R0ZPi5DccOybijz0DjP4WuqiVTM6OBzuyL9NtLjZHVy0PHA0R4p82Ra0LN0V5BsE0kcwl085RvmgPDm3UVZLzEKe3CHM_MNE9aSTFFX2AdBLXdJUje9EcQpLXvLBMGbA93o2leIOezkCUl9FIg-9LtUzuG6dCC9ezKtl7JKFqk9hrIA4CCTDXff1ft7dbzNpoHCkCniSaWW3Uo5gsQ6l3CuYb-FGHzG83meCHtldiZwpBr-r128qVGm84VAERE2-rgsmYib-hnm6cKTkXrL_Co-1FA1N-_Q96KhXoziDO0GiUQSGGShURP3_H5ryhAbT6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIrgR_ucC-5ayMOiTp2W6R3GhJnrbakrA-bATbyP0k0qgyMusDavWVxbLlycfvAQ6TwN2zkFsAXxQZ19uGmbnPvf-pYpHXzUQtFWHjUOEMmo6q_PGaJU76QI1QgXHr75qrbBCnE5QAWxZ18Ez-_gdLrKYlmOxIVc_LbI88G5uawkaTIM0L-RIoJsm8Ate0Bo0HqKCW4dwE5yOyXorJwr8mFgwJ0SI2l4eXfhHnRr1tvcUnKJZdbqZi4A_srl4-Rgne4OVg7iN2HRO0GA8h47GLs2zB5IJHK3Ta_IK8rXPpM8QQ3DtIJlOMVgOg5f7mqESkro2nqknlsjpSnFNi3jjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQCwo_XtoOkuSVQ-WAXfaFN9gioo-ryVsFqXbRcbBQNWi3icTee774fv1tqp0KGr573UmvMXGnkAE5HrihzkZ7LoVe1KYGhAudeaP_1BflOvTl-W3z0VCKj3n0PKBICkFsd8o6vri8HBx-sNHhp04wgTQxw6zErqEdKRyVa14wfXrzoR4manMNTFleYfTn8JFtEnu8HcvrNIDwP4PjJ9XoByZuFiIqDtG1SDWay7A5-SVoMs7kp-UsVk6C4DOfZcHmg4LPAJUsZ4Jkm1XlAg2dtG_m5wuORFFVkQhCiExQBOuF0Bv3Easx4_L_87OMCO0p7euK7PJr3dfp7EX3zRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwiaH0h_ZfBEOWu7IlfoEARKN08jwc8cwwTeYhjpKcHB8xgqjvIA1NAm8fWwSIVGT5tnFAsMWGYlgzkoUz6DKULNkrBFbRNtUbpqKoZ1h9GCLkJVWieqNZbZb36Ccc2tMGryE1i75jQjpSSbz9KRmmjj0WgIMW24P9m7YLsWM-iSRVln245_u2aDtVaancggCMFjC3nt9Tvrq2ZkGUzx_L9VD9ggEtBDqnTjL1GTyxMq4l7IISBKrvO9tzqkqytRxx67qVmIbLzZQU2FXHMclVZzkvyGcgNJJkyHlBFjC5vRiK72JTClu49E7eONO9MPOCUtTT1KGxOqEi16ab_NqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XD0wbeVsoXaUwHtapEJxn63QQ_qv73Ac7ZkOTg6GRY5InWudE9bnUKSlyNXF-R5Rph8Mdo4RnjcAMrwEWs3bH49-xTq6ryxRO29jnP2BznJSh4DGc6d0LEVJdoMdyxqDTKUrbHSZX9CuVMs0Pv1wtUzQe-2lMRjLXQyjkWErxxJAX8jPvbTHQU5fVmU3XUOfh7ox47WcQQZ3sfNh5ajCCyL7ibhPCa6rQ70GW1MUjr2hIEcyXuTza0KvrILnlyKxET7_2hu4qiLD1tVMBFBss4xDdBRo5vs8titXEGBV4meuv4Q0CDJSLUFBJNNB-OeV1cDsXy6xMAjmIdDbTy4tmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3kUVfFmGxt-9bPXceWRPNmyzL10B4pGjM7D-OPGVqW16tMtDUOiCe7Aoo395Z7ceOMLX7kXh9DETHSP5-7zeKIyIoUTn32eOv7GNb10AfXwJsugW8xt8Qx7JmX3ueDL0bTYz62rqd7uE7SWwIq-wOM1pI9M6wr_bm94S-fBwuDCp_OkJaLWQ7wIdi537mjzzedxETWaIlTyyu5hvueY2jiGgEf0bZY5GlmZiyD1UJJAD4GVdbW7JSwBlluA4NgCC9o-jebsb-L06lrNv1hRj3Es3qUj4eB9hqqwv7zCaieGwVmuopR6T6HyPseoNygdQJjpYhleZV08TjEgi0zriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1Tpm7XTB0FE69znvsjT90-YIlfnX3BdiyDlUDUQh5_MJo9Q5vr9dxYB8yYHKCtma-OCDdqKmsXRyraA_3AJ0N0j3edOnTDDp_VsC-wFdXoMWdJCz3Wa_ROp8bFoHlyQfUIp0BPxvodk3Rtp8K2zsvl16_XcuBKwuT_ni_DQAKeD3HfgkHFGUC9IJpLGYrDNG64vUeNbjTE3sHmqDxIjmuEIF_uzmfsJgIMG531V_GPjOqV8xWak-L2F20IPn-mpiKlGjGo4igVVgjVpsztW2oBA1y3aAIzAs8EM3oBqGCUC-MJXlr0Do62MX6OWSAugy7Y8zJkRXpt0tYRJPu6omw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ثبت لحظات هیجان‌انگیز فوتبال در پشت دروازه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660766" target="_blank">📅 12:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4503c3828c.mp4?token=ftl3xK5GLIG9_sochkNB4CydBb3sUHzHFw1JGO3NMuORgLalbBB_XATXSa3CZgQoPfrCTyTWd9DuCPxgX4LNJ-6-4efy-M0C1zkqOF-wQ0XwLFXVfXKIBwIuyVBPiG5DH7VBrMepofUFhybvibHSmdKS23VwBPhlx6Am6KvyGDojpSMxkccsHKFAXw8dG91c-IdM0kWgWOjv09aBMsYltEsUHBjAxBUCcsEbiz8s7XUobABOXx9ttDMP_H7hP70OjFUfktmhY2F5n2-4bgMBjZfxpOMAv57jdxYKir9KNUh2ttVbE4WwT4AoGcQ3PgU4i35aE4euZWW4ognM-rXi9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4503c3828c.mp4?token=ftl3xK5GLIG9_sochkNB4CydBb3sUHzHFw1JGO3NMuORgLalbBB_XATXSa3CZgQoPfrCTyTWd9DuCPxgX4LNJ-6-4efy-M0C1zkqOF-wQ0XwLFXVfXKIBwIuyVBPiG5DH7VBrMepofUFhybvibHSmdKS23VwBPhlx6Am6KvyGDojpSMxkccsHKFAXw8dG91c-IdM0kWgWOjv09aBMsYltEsUHBjAxBUCcsEbiz8s7XUobABOXx9ttDMP_H7hP70OjFUfktmhY2F5n2-4bgMBjZfxpOMAv57jdxYKir9KNUh2ttVbE4WwT4AoGcQ3PgU4i35aE4euZWW4ognM-rXi9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشایی‌ترین مسیر ریلی جهان
زیباترین مسیر ریلی جهان در کانادا
🔹
قطار گردشگری Rocky Mountaineer از میان کوه‌های راکی عبور می‌کند و مناظر خیره‌کننده‌ای مثل کوه‌های برفی و دریاچه‌های فیروزه‌ای را به نمایش می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660765" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660764" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
المیرا شریفی مقدم، مجری صداوسیما: مسیر تشییع رهبر شهید انقلاب در تهران تغییر خواهد کرد/ با توجه به پیش‌بینی حضور ۱۵ تا ۲۰ میلیون نفر از سراسر کشور در تهران برای شرکت در مراسم تشییع رهبر انقلاب، مسیر خیابان دماوند تا آزادی پاسخگوی این میزان جمعیت نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660763" target="_blank">📅 12:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCsGh8tQ2t8PO4h7vHsxX12SXN8bT8peCTJzYH922FeGeE7fGB2uJi68EeQ4pGQbafqBvW17i6-0kpEzDevKbEIXqPFIvHuwrM5sMoVC-rXSha_4vv6Mu0t9PRhF4HA2IulwuZvuI4xXCrfLkiRrHNF_9VIBjBX19e6d_yx5JwP-GPLIyKqGO6bTnQWFgpOnVDN5XK-0aNCCfwYYwhpKGdFA2HOb2ORt_79EtRF-vkUE1FnoLpg7k6tcCnVYOj_8Q-SpbplhvTVugp3gjhq8KT-si0pAKbmeNWAgfSHVwhnQkVt7ct6RZkVJHrDYJeCThZ-96rdbECUSbbKu_bqr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: اسرائیل برای ماندن نیروهایش در جنوب لبنان با آمریکا مذاکره می‌کند
🔹
رویترز به نقل از دو مقام اسرائیلی گزارش داد تل‌آویو در حال رایزنی با واشنگتن برای حفظ حضور نظامی خود در جنوب لبنان است.
🔹
اسرائیل با تأکید بر ضرورت حفظ «حائل امنیتی»، در برابر فشارها برای عقب‌نشینی از مناطق جنوب رود لیتانی مقاومت می‌کند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660762" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrnQCpfIb0jCpwlroUikRXxgqRtqmyOPol7NKwwvtkxnipAKE-kjVDLdZkJACM3QWoGcx4qKjh1XMKwnTTZvYfSrgYl4hICt829LLrGzw6eiNro4728ToTG8DbwriimSVihykS6cfMCYYSJxwvicLblvUYId3WRVBz9Fw641ewSLH4uwoC2Q45NCyDvNSyaservBJM-DrHarUSdtXSxOV5gmkXOkYVpksIEwxJid60fHwahKkxDWKSpWpSs8dASUOOuhFzLAv4I4S6htvWhPf70dzuYFTW5hYq7AmO03eJCXcJYVLT4igWsoXqjQKctTwE9bEbO1mfUiTUuvNrz2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: منتقدان به توافق با ایران حسود هستند
🔹
رئیس‌جمهور آمریکا در واکنش به منتقدان به امضای تفاهم با ایران در شبکه تروث سوشال نوشت «این احمق‌هایی که فکر می‌کنند من به‌اندازه کافی با ایران سخت‌گیری نکرده‌ام، در حالی که بازار بورس همین الان به بالاترین رکورد تاریخ خود رسید و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. عظمت را به آمریکا بازگردانیم»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660761" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4ZnYu7au4LaWV9qu4mBkKOhLBw4qQatswBcUBil-GiT737uN5cm2svaTMj5Ggpu0Vl-ts0SLU-bZhObYV1plR0INnHKtRXyPU7DKwzaojQS0-lI_rmSOKSuWuT1hgFoLe_SVguazxKpRPBmeGvoxA69zcfP0gS5WXSB4cFJ-p-pqx_l8sIHMIdp4HtoTmETWrTB_bwD4YR0b2ZVwty4jVZIRPYFybbPsm0YFR4THrzGzfH8Py73rzfT20Oed6CMjcoR9s9_VsALNabyacdGcm2S9Ysz9MBkdIhKzUzXEmBKPDk59-qjruiGwJgjjhiXCqijIhacslTjHQKZ1E17jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده جنگ روانی؛ چه کسانی افکار عمومی را هدایت می‌کنند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660760" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fa1acf22.mp4?token=lKPyNvFS9DOKEffpukJmEt5p2IrFp-obG--tkh2H6bglrUKUoodE9ttNAWPyObufe5UpTbPQNPkF4HgWDnUpWk_xDprP7_0xhZDKVcsNGBLxEal0ZTYmb1geuJceZKvJL-CbbElbiXfQDe6CNCgi6990H-MU9xby376q1Q98OQZ0MMQmBpNV-y2UC_uQ3AVS5ZnavGdKkIOPc0qS088LhEQD4_FBbbjZHw6J7ZLcGmUytYw8xNV84cynkOMHpHllMv0gMzVSUFbxn1us_shDqaZpJlwEtzEdCp635bKKB4YyQikFSaItKC0xrYwSvuxpQb3QD67ywq0laA6wmuElDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fa1acf22.mp4?token=lKPyNvFS9DOKEffpukJmEt5p2IrFp-obG--tkh2H6bglrUKUoodE9ttNAWPyObufe5UpTbPQNPkF4HgWDnUpWk_xDprP7_0xhZDKVcsNGBLxEal0ZTYmb1geuJceZKvJL-CbbElbiXfQDe6CNCgi6990H-MU9xby376q1Q98OQZ0MMQmBpNV-y2UC_uQ3AVS5ZnavGdKkIOPc0qS088LhEQD4_FBbbjZHw6J7ZLcGmUytYw8xNV84cynkOMHpHllMv0gMzVSUFbxn1us_shDqaZpJlwEtzEdCp635bKKB4YyQikFSaItKC0xrYwSvuxpQb3QD67ywq0laA6wmuElDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر لحظۀ امضای رئیس جمهور کشورمان پای یادداشت تفاهم نامۀ اسلام‌آباد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660759" target="_blank">📅 11:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
درخشش سه‌شیرها در شب پیروزی شیرین مقابل کرواسی/ انگلیس خط و نشان کشید
🔹
انگلیس ۴ــ۲ کرواسی
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660758" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
مذاکرات پیچیده اسرائیل و واشنگتن درباره لبنان
رویترز به نقل از یک مقام اسرائیلی نزدیک به بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
🔹
اسرائیل مذاکرات پیچیده‌ای با واشنگتن درباره حضور خود در جنوب لبنان انجام می‌دهد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660757" target="_blank">📅 11:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52901b859.mp4?token=QXT0zSwPwwHTj8xy5QXp1hdQYtdhzk_G2i82jeRu4BPftGtXS-r5QF6aqRjuWEifb_O9V5kwiOm2_UQNV4FSMvfoHdpA3qH3fWEVnyQ1CqP0r-fbsU_AOwefDjq1TEOXX88HO1zJamSL-OrICQ5tUQmOavwHL0CEMucoxWNMDmrTfF4dGBcAxg8EXE5BCkqWKPrmjxP-LxqddvLisCeal8TOxXhDsXc6udoabPkNzpwp0vU5j3RUKNry67fbyX6sAuK4vjWMlGDfmFdTfGZiMU9cgR5FYgfr9ziOjwNoYoVqrL472uANEJ97fedbQYN2YEI6gAyVLPocyXS5mePUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52901b859.mp4?token=QXT0zSwPwwHTj8xy5QXp1hdQYtdhzk_G2i82jeRu4BPftGtXS-r5QF6aqRjuWEifb_O9V5kwiOm2_UQNV4FSMvfoHdpA3qH3fWEVnyQ1CqP0r-fbsU_AOwefDjq1TEOXX88HO1zJamSL-OrICQ5tUQmOavwHL0CEMucoxWNMDmrTfF4dGBcAxg8EXE5BCkqWKPrmjxP-LxqddvLisCeal8TOxXhDsXc6udoabPkNzpwp0vU5j3RUKNry67fbyX6sAuK4vjWMlGDfmFdTfGZiMU9cgR5FYgfr9ziOjwNoYoVqrL472uANEJ97fedbQYN2YEI6gAyVLPocyXS5mePUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار اوباش قمه‌کش در جنوب تهران؛ ۶ مهاجم در چنگال پلیس
مرکز اطلاع رسانی پلیس تهران:
🔹
ماجرا از یک خصومت شخصی شروع شد؛ فردی کینه‌توز ، اوباش محلی را فراخواند و در یک یورش دسته‌جمعی، با سلاح‌های سرد (قمه و چاقو) به مغازه حمله‌ور شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660756" target="_blank">📅 11:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای رسانه پاکستانی: شهباز شریف امروز عازم سوئیس می شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660755" target="_blank">📅 11:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cad599f3.mp4?token=Q5PqGTEzXOV4T0mLx5NtNQWtN27UgM2PSbS9fc-MZrVKFE0DMcKc8rE-C8jtCiUCL-C6FPLd98j_xeSLjdaSaYGOvTHyOPHdQWH3EzUN9hDkkgDWtsxAjUFKgJl_dzh_umt0RCNzaxmfg1dhymWRuPelpuwIhz3WerVX2WMjmrBuzmOZbt--OmatBk3fU2syZ_-95VCqMwUq_BGpmkAp1CVqsiz6I45JinS6xPmkrjBSICSNWWHRs4ShFZR9If7MK99vuSIUMzd204FMBG9PTc3QJCf_LRlHKPeoMOJtVyRfitIr7futZ60QMMoGJAxO3IByQyR9M1ueVNBdTOvd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cad599f3.mp4?token=Q5PqGTEzXOV4T0mLx5NtNQWtN27UgM2PSbS9fc-MZrVKFE0DMcKc8rE-C8jtCiUCL-C6FPLd98j_xeSLjdaSaYGOvTHyOPHdQWH3EzUN9hDkkgDWtsxAjUFKgJl_dzh_umt0RCNzaxmfg1dhymWRuPelpuwIhz3WerVX2WMjmrBuzmOZbt--OmatBk3fU2syZ_-95VCqMwUq_BGpmkAp1CVqsiz6I45JinS6xPmkrjBSICSNWWHRs4ShFZR9If7MK99vuSIUMzd204FMBG9PTc3QJCf_LRlHKPeoMOJtVyRfitIr7futZ60QMMoGJAxO3IByQyR9M1ueVNBdTOvd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگستث، وزیرجنگ آمریکا: برای مدت طولانی، ناتو یک ببر کاغذی و یک خیابان یک طرفه بوده است، دیگر نه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660754" target="_blank">📅 11:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660753">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سوئیس از برگزاری دور اولیه مذاکرات ایران و آمریکا در روز جمعه خبر داد
🔹
سوئیس از برگزاری نشستی با حضور نمایندگانی از آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مربوطه در روز جمعه برای مذاکرات اولیه خبر داد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660753" target="_blank">📅 11:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660752">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu_MAv9U6eAv4Yh0NAmipVTMHe4XUlaS2LZSWzZoJryrnRLSBVYxwpTDUz3bVgxZduCWTvVHzgWhh2ePCDLStv4JHOMAMdQG9Y-myEA4SGQLDUYoopdcHWL3YRoBDlTEj83KcEuBNc0Gdl0LNMfFNu99IL9rXmYdUbISMdCHzoPGlmQEU1ygruRVC1998UMiiVxGJ9Kot8bnsiZBCbAzVl2w_p7ByuLJHe1FLYP3PXRStCbHcrQTn6EASBIFg_SVmai9KcWz-3_Wf3awAKe3Cyx75qaglRI9VWCcqvTWVmNQjhDV-nbYyvb2xGl4LUmfKPTpSWWq_da1Nz10D77EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل حسینی
🔹
همراهان عزیز خبرفوری؛ عشق به امام حسین (ع) از کودکی در دل‌ها جوانه می‌زند. در این شب‌های پرفضیلت محرم، منتظر دریافت ویدئوهای کوتاه از مداحی و عرض ارادت کودکان شما به ساحت مقدس اهل‌بیت (ع) هستیم.
🔹
منتخب  ویدئوها در کانال خبرفوری بازنشر خواهد شد.
🔸
ویدئو های خود را با الوفوری به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660752" target="_blank">📅 11:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cd354ae1.mp4?token=HyCMeo58rSG5blTH6JQZMo8C6rmrmjbMLqX7Hm4iLffgZV7q4fry7pzpG4Y0Rj8z7AOggmSiiwdKpu6P-o8ITwZFfaXi659rUa5VpUT1zZZ4-uO9x3CaIkIG10bsYo7hOhsqaSvRHVCktUkTPFjiw6bFVqCg_JKOb01L7jQQ7jO3es-huJXDyKAsv13tfajx2vV1iqqALwIar2VrvYljwxqsqP0wZqO4owiYQR25R0RIiNvc5eWIOt0FnTnMb6gA-iJZT503dWrVToPoupBwxhzdnX0EywRspeSlNfRcVjKblIDT4hl8rBcDqxxCMh-FJ00pa7_y_esjgXZcWZWeqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cd354ae1.mp4?token=HyCMeo58rSG5blTH6JQZMo8C6rmrmjbMLqX7Hm4iLffgZV7q4fry7pzpG4Y0Rj8z7AOggmSiiwdKpu6P-o8ITwZFfaXi659rUa5VpUT1zZZ4-uO9x3CaIkIG10bsYo7hOhsqaSvRHVCktUkTPFjiw6bFVqCg_JKOb01L7jQQ7jO3es-huJXDyKAsv13tfajx2vV1iqqALwIar2VrvYljwxqsqP0wZqO4owiYQR25R0RIiNvc5eWIOt0FnTnMb6gA-iJZT503dWrVToPoupBwxhzdnX0EywRspeSlNfRcVjKblIDT4hl8rBcDqxxCMh-FJ00pa7_y_esjgXZcWZWeqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بیش‌تر از حمله اوکراین به پالایشگاه مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660748" target="_blank">📅 11:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد که در مذاکراتی که قرار است در سوئیس بین واشنگتن و تهران برگزار شود، شرکت خواهیم کرد./تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660747" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پیام حسن روحانی پس از امضای یادداشت تفاهم ایران و آمریکا
حسن روحانی:
🔹
باید از دستاورد تفاهم اولیه ایران و آمریکا حراست کرد و نسبت به توطئه و عهدشکنی دشمن هوشیار بود.
🔹
وی با تقدیر از نقش رهبری، نیروهای مسلح و انسجام ملی، تأکید کرد امروز ایرانیان به هویت خود می‌بالند.
🔹
روحانی همچنین گفت همسایگان ایران می‌توانند از ثمرات امنیت و توسعه مشترک منطقه بهره‌مند شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660746" target="_blank">📅 11:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGT2HanXq2dYLaa8JGskmBPNprUbNvz0w7nCpPG2Z4tJENfX1ewz28QhD1iLayN16faQoLh_NPayAjZvi9Rsupv_9nwj5yFxD7CMQbKjya8LklvwI5z8YGkZyRsoJ1hZbyecIEGfIQhP5wcWbMKn1kuDF7Ffpr5Iw6uQNXfjwpwxTXz4-rfebnK5KYzTLKcpT-4CgRFmQSPg6EpFmcgpC3FY_otQnA8lrvwa12m3MIWY5a8URwg2n6VBycMxLdL9kyy15KZJchvZfUr1wjg0gMs0hGUuBZToJhVIous-E5244GtnYvWq0DRUiWSc2XQoe-0IBJOSUdbeFuE6HxCVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور اندی کیم: ترامپ ما را به یک جنگ بی‌ملاحظه با ایران فرستاد تا ما را در موقعیت بدتری نسبت به قبل قرار دهد
سناتور اندی کیم:
🔹
ترامپ آمریکا را وارد جنگی پرهزینه با ایران کرد که ۱۳ کشته، ده‌ها میلیارد دلار هزینه و آسیب به امنیت ملی آمریکا به‌جا گذاشت.
🔹
او مدعی شد توافق پایان جنگ، ایران را قدرتمندتر و ثروتمندتر کرده، در حالی که ابهام‌ها درباره برنامه هسته‌ای و تنگه هرمز باقی مانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660745" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9627f0fd63.mp4?token=G7Kg6h6VMW_edta6ZWx5E1EI3S466xonblugPinX27j1q8unV2eWmtG2t35_raM47qCi7mZqx6XtJ2GesRWi8VQiWNWfxMgzZ6N9n5sgntP5nGAKGTPwICH13kwHz0FdA6nP-AoqPjClabcr4ed2k9MKujhdCnMVO0APgE9MZ0cacRAei2uLJyysOWGounuui4EVyokvU8vkJyVR9q0YSm3KebiG4_mDG2rSrb4RyzlFC_w8HJqYepfMKJCGVSMNLGkePsjAYfwU0MoUlURIKoNWefRDgZuEU1LD4b69ZZJo-rC8qyJCg5JDXnPSaMYSRB6zxdMEQR4svab-pxvTVycZ20Qq8OzcYoLBLaKvEETPYfQ0m3xJxmjEmzNMsI5BcjShzbKK2_aCyPgAO3wUaIERwuvh8OZ92oNfOi86nbGuLYqpiP4l1b6yyHCz3s6eggfgDFSXrZhLud0AEMDjNCSFmPQvmFpzvwSKPCwQF-lB6Q1aq3uVX5xnSLzPombcqeku82egyMm4am9QDEAJPjyI1596YMCwr61M6WswIh0Z20Z_g95Pa9q_8vrJNLmqjQ3yH9Qd8XIQmWwZ506WZ_yZSlH7vKhPd1IiNcV1CZ1QdIzTzzez90YUJ5hI37wPlI1JV0Ue7sdxhI6l0n65pS50eLSxDyMrtpJrALgwYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9627f0fd63.mp4?token=G7Kg6h6VMW_edta6ZWx5E1EI3S466xonblugPinX27j1q8unV2eWmtG2t35_raM47qCi7mZqx6XtJ2GesRWi8VQiWNWfxMgzZ6N9n5sgntP5nGAKGTPwICH13kwHz0FdA6nP-AoqPjClabcr4ed2k9MKujhdCnMVO0APgE9MZ0cacRAei2uLJyysOWGounuui4EVyokvU8vkJyVR9q0YSm3KebiG4_mDG2rSrb4RyzlFC_w8HJqYepfMKJCGVSMNLGkePsjAYfwU0MoUlURIKoNWefRDgZuEU1LD4b69ZZJo-rC8qyJCg5JDXnPSaMYSRB6zxdMEQR4svab-pxvTVycZ20Qq8OzcYoLBLaKvEETPYfQ0m3xJxmjEmzNMsI5BcjShzbKK2_aCyPgAO3wUaIERwuvh8OZ92oNfOi86nbGuLYqpiP4l1b6yyHCz3s6eggfgDFSXrZhLud0AEMDjNCSFmPQvmFpzvwSKPCwQF-lB6Q1aq3uVX5xnSLzPombcqeku82egyMm4am9QDEAJPjyI1596YMCwr61M6WswIh0Z20Z_g95Pa9q_8vrJNLmqjQ3yH9Qd8XIQmWwZ506WZ_yZSlH7vKhPd1IiNcV1CZ1QdIzTzzez90YUJ5hI37wPlI1JV0Ue7sdxhI6l0n65pS50eLSxDyMrtpJrALgwYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی پرتغال-کنگو در چارچوب رقابت های گروه K جام جهانی ۲۰۲۶
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660744" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkSbdhlcKO8SP4A8G50kC0XPQpeFD0u0UL7j2YtIlxH4DTB-LsfrLQ-6VsWEEbpwiSugk5EbA-SB0QTwUFTT3FwEeI3Uz8A9-pwMymw6IIp6k5NSFbVcsHP-q7udBWm_ZemmH4VxsuQ38yIBuWrNWXHjLxRnT8SxKuxcGnpJiIV1UAcd43JQo-4YEB_nkXxhv62KHrGQaeQS-FX37-ZI-Or8On8LrfCIyR12ZyaswtA0amUPFT4qtnsordWOs_pMLvjfFbAYoXHT7zg-zRdJS3cYCjpZEjpqc1s78IqZTKFScR8Nb8dLd_X7ZX7VEd39oWl4_YHcJHqw7PVFouwjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیرس مورگان، مجری مشهور آمریکایی: این توافق ایران تقریباً به اندازه هر توافق دیگری در تاریخ سیاره زمین از «تسلیم بی‌قید و شرط» فاصله دارد
🔹
خوشحالم که رئیس جمهور ترامپ از این رسوایی بیرون می‌آید، اما شرط می‌بندم اگر دوباره فرصت داشت، هرگز وارد آن نمی‌شد یا مزخرفات نتانیاهو را باور نمی‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660743" target="_blank">📅 11:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رئیس کمیسیون انرژی: تفاهم‌نامه با آمریکا یک پیروزی مهم برای ایران است
🔹
دشمن به اهداف خود نرسید و بازگشت آزادانه درآمدهای نفتی از دستاوردهای مهم این توافق است.
🔹
ادامه مسیر به عملکرد طرف مقابل بستگی دارد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660742" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دروس و ضرایب امتحانی آزمون ارشد ۱۴۰۶ اعلام شد
🔹
رئیس اتحادیه مشاوران املاک: نرخ مجاز افزایش اجاره ۲۷ درصد است
🔹
روسیه: همسو با تهران برای لغو تحریم‌ها علیه ایران تلاش خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660741" target="_blank">📅 10:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4120a36b2.mp4?token=dYJfEDMLcPga2wGLMWJbWVTh66VEje2jnnLXHOMHCdd9usWphPYuyv5dsNTURu_CGZho9SlUNcHLW1OyiAhG7y3EhM1uIYyEwmIIyN68Pnn23zlHte2Ikrv2uURXr4poUkkdkArSX3xUOmKgXjZyRKV1NHZhUrbObtKRhoNGlmkzylX4UyRnKOiYDbCTtAvXnxcld3dCBYuCMTkVodV4nTDRK7HNFLfEfZHxkzjfXEfn8fVuc7EI8imjgfOO0O2PWhCF8DJarLEHtNskj03V1pSzh1LUA4rmmqiRoKgiFzdsQ7NhAB5eyz3R1gGfeQa4I5a9CI9EsfWhKXLIr70M9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4120a36b2.mp4?token=dYJfEDMLcPga2wGLMWJbWVTh66VEje2jnnLXHOMHCdd9usWphPYuyv5dsNTURu_CGZho9SlUNcHLW1OyiAhG7y3EhM1uIYyEwmIIyN68Pnn23zlHte2Ikrv2uURXr4poUkkdkArSX3xUOmKgXjZyRKV1NHZhUrbObtKRhoNGlmkzylX4UyRnKOiYDbCTtAvXnxcld3dCBYuCMTkVodV4nTDRK7HNFLfEfZHxkzjfXEfn8fVuc7EI8imjgfOO0O2PWhCF8DJarLEHtNskj03V1pSzh1LUA4rmmqiRoKgiFzdsQ7NhAB5eyz3R1gGfeQa4I5a9CI9EsfWhKXLIr70M9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت اینترنشنال از امتیازهایی که ترامپ مجبور شد به ایران بدهد
مجری اینترنشنال:
🔹
امتیازاتی که ترامپ به جمهوری اسلامی داده یعنی کمپین فشار حداکثری، تحریم و... کشک!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660740" target="_blank">📅 10:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660732">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2J1xbQkV4YONIqQLMyl4P54pT59YmvSok3K40wjPSw6GB2ugWxByFObkllVKWsMHwaYAbQtZKGKkoSSpryK3wgtpL6PXuBU74GhDD_EiN09GrIf2GNkKBSnqSzdxcH81rF56gTsKPHNHWaMgFZenGzy_78_1jWMdC-6OFJfB3HEDXMvO3xr_Oscd9Ry8vEB99C2Rrfnq7JkiFeE0oz3aX05KRhWu5YrSNwJRTC1RNr_VH92Df50SAGBZQh25I023iPn99Gdt3-0dMWuTnuF4E5vBC4jExXM5g3lC6aCgcXGd5sNjHdzY4RbVUfywEtebcSDgIm-zyJqxaPUfgKH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEA4q74ZX3LxcBz_zD031PqgxTdrSQfdptE48yoy-uQLOC2BuCA4L5vn7j2c7Lm_YqLxTLM_DCPY9x633fZMJtzTSWPvvKIXRcijb3hEsoRlWV4X_Y0BwUTGU-2rbKMZkb32ApBmPFC7BuPKhq0jHdEVqB94q9P0WhOU0rlZXtkF1SFop98wjm1IdEnvGrw60V3z8Jv6iw2Q0bpbkD0sxKJRbjc0uFJjnjJGN-vKzf-Msb-i1XnfjCMrrHgDedXOFnKmBQJsgmm7QRKrlKRGol2iU641LssXIatEvYNNI1H-tz9kWoBhGSaH5EE9gr713ixvPr9pmp7Y1mxPYUIxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEfy9nKWm3bwMCOrZ3BCmPtpCaDwX7KRQ2wIvCfLcrUd-tfftCRfQQ26tzkxwJqWEc5rDSUoerLiN6MaHVj7ql5vrUMRrvvFvAHV5bSSXzHgCAz-awU7NrMxPvVDjBcpNdqG9wdIwCa7Q2OSuv35T1Y0-MoO8Qag_vG4Dined70AEAsMOoGHHnV7ShQ-XmFwDZFi9IwIwKED_vsUUrpjkmd8QONY-FjlmSYHsfXo4KjaxirYRkiIP6ZpUmeYpS2AivlruVee_p-HC6wiJ2hBBDhLMDd03bB0YhgtDi4hTtpv1afeSIg9q0EgDXcpdlAq8QQhRFR7qzqm9tMcpqLfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G34-LcsqAY6aewqXrOD4-RMr1EjOeTXTdFTDYx1vwFI8T_vd1K-6PhFsoWX8YDmI0Yt3KSbVkF69xRPMfEpsCH5qjnfpCXxyzgLqqdufOuZvF8JU3Tdcha9y0CWSaiF0T06tHOkgpWME7iUlV4iaMFVFrkaSM61YBL2fbVKUpNzWN4ZdZqeim-ZZceIcwB40dr3u9OvAHnSOcnN3en78GNmsdYrDNTuco_CLf0b7xMyH0aAuY3kX4d9EbD4zSzdV9GHEqHRPm-WAzZh5b5l06MTk7aUJ_8Ia7smdgb8Bv53SArT0PLzdGVlHl_egp-QgBRa1_HmNqA_yUnPE0_kihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afWAvf7lmIDGo1P0ODkvJs8K6QFdgeEZByQHqCVNpNukrCWXn7U78kq9gANel6WSTHMa-BI0SIM2V4-IUnu-GkBYJoAdogzkU2lUcvF28y7qud0lmQAuC1wej5pa-q88RTO8gojHXr8PKCphFJ59YxJ2jQHd_yWkbWdnmaGqISo97czStofugWjA-L3BYgwp45uCO-0mBsl-9sNZt7iJsf64veUt-GImkd3ImhERryNyvivG6fCbpgEW4Asizvj3CnVY4vJovOXSJZ3s0tVGvwsLXlBnd_ocHDKxWHy4IPRtRwI_6em572FW1yljCE5h_S4EGnd1X6-6c8-CnvWCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXelC51VRHHBZ6a-IK2iodE1hHMpgq0cj0yxnsSQLj2LH8cQ89yfkjv78ANzH6SK2OGuOh5hGswbQxVCTo6otd54xmqtEr7m2T9l7rBRps0EoOZWGJvI6nhA-sPFMGWnyfZMxrXs4sFZ3sQQBrmnU46IHojwz0P58pDOl9zFKRsT9gSQzw7SlkOSE9EaNnFpjj2BEirZ4twNa3IPK00OJDy5RMBHNytLY6gi0vgw5HxRh2ZlgxeiFr1Oxlw77jKRH10WiXIe7WOhGLpZM1vBscWdEfnaIQayfAVvvOzwW7pP8mWCnteh1TC-XHNYOV8-e_LA7cHLZOvzR6J2bAQUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RArd1Mqg2ojIaL88nWAX-z1kFz45LQjvL3z3tu-a2lcuV7ir_yzFEn0QTibRRm9FHju6Sa-DFNS8l8Mr9Rd4Xi8u-_hOwjmOCkhreD3ZHjCy5danr2jeGtfNshqDwGxamJuh7pAlIjocuuf_QHZN76lp065RRJcuNVyGugL6eXk8i9GDfyX11gGPe6ocGOfbS9IZOC1yxOudw5SW1ZBRUdu1TUyAHKsRWe3MpgdELG4KN8wMMrhvnFusdmMWRFcbr3BGdEBbS8ys9ZGISAYvwEI33H4gj-pfsnQ1lUfClfARhuINBp21cYT7Kd40RHxMLNHaqaim1HoXb0oKXdvjKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نقشه تأسیسات اصلی فرماندهی مرکزی ایالات متحده که در جریان جنگ رمضان مورد حمله ایران قرار گرفت
🔹
Camp Buehring → اردوگاه بوهرینگ (کویت)
🔹
Ali Al Salem → پایگاه هوایی علی السالم (کویت)
🔹
Camp Arifjan → اردوگاه عریفجان (کویت)
🔹
NSA Bahrain → فعالیت پشتیبانی دریایی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660732" target="_blank">📅 10:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660731">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaXKSXDcs-rT5DGFO-4oM_XcAPpc61JT5xZseYMWCh5o3AXM-9e2_LaTVKtsRoLrMsh6fq8znxgfzlVUqgKKY5UGovmJeBHz7D2iV1OCkkPXeQxyK9LkoBBD5L4jLUvgiVjqGxLS7Tr0tpQcnAbVaP_owRrZ4N_9XFbJNDfCpZH7WH3Evdlnzqcd9GHEhDMDRXLAlv-r9OJ_0Xl2CvP8R4BuG6yEnLO-m9ZZ7POZ3CZOvDkE15pr1J6tBITB5U996hydkBx8nYjvTwsN6XUWFmr37VB9ELlkIfjxrxN3-LOnHotDBfa6iz0QM1xA7LFZyXRpM4Q6w0NWzGLmfUf9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بمب یک تنی آمریکایی ـ صهیونی در سنندج خنثی شد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660731" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660730">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XISONFoKwl2rbtOJ8iMjfqykjBAPJCU3YCldardNOGu20crqGdh3GK6fObnEFu1RZBkkNnOb88AsnkgYV_-R6_Q7yJ83tUPWF3-AcpwjAcx6PAX--yRYMdQeVIBIxKsMS4yckrmp5ZsiYTCbVTRoJXuh87sC04M-B1DEmqClg59reNl-SyPcs_0TG89sj93JR7kP2q2Cq-pkg9WfNOdJlw_pcrJzulYoCW27v81QZCf5lrjcrkQuVt7W2OVBPB4Vp9B9p3-OAs-J7Fj-5Tk9clvVYRmCTBw6Nn8LjyfPP3SGsCIRmYKq4nkdafKpdVPo1yI9Ks528N-yQqo_7WE1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه تأسیسات اصلی فرماندهی مرکزی ایالات متحده که در جریان جنگ رمضان مورد حمله ایران قرار گرفت
🔹
Camp Buehring → اردوگاه بوهرینگ (کویت)
🔹
Ali Al Salem → پایگاه هوایی علی السالم (کویت)
🔹
Camp Arifjan → اردوگاه عریفجان (کویت)
🔹
NSA Bahrain → فعالیت پشتیبانی دریایی بحرین (پایگاه نیروی دریایی آمریکا در بحرین)
🔹
ISA Air Base → پایگاه هوایی عیسی (بحرین)
🔹
Al Dhafra Air Base → پایگاه هوایی الظفره (امارات متحده عربی)
🔹
Long Range AD/Radar Sites at Different Locations → سامانه‌های پدافند هوایی و سایت‌های راداری برد بلند در نقاط مختلف
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660730" target="_blank">📅 10:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660729">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac200c8262.mp4?token=TrUSqR1zcVX7Zhs--1MzICcMdAOycjIx3dpaYVRp_DkNq055GyhChoJQK4v93ABuLAMzlZ0PcB7UgdXezjFP6eOfrXqf4fVIXGmnXayV1E0DDbBoBhsr08Cg8QRm9gS5ZQ-16DVtFxyJSDmYRHsIEJgLHWDfJQ037eN50EsmY6GIVaPXZA4LyI-kL3FxVlXZZXN2JyjWKzVBFUHc5kHaGIdonNpcsRCtx6S1YXc5EGFWqnC-qckEiwUPnaYcYEbF3oDOZat-hGxTpA0zWGkA6A5HJJI6Wbk5_MvJdmivC4DeL3GQiCc5ueLPSLGKIcy6eP0ME2BVKksqVoC2ntcUCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac200c8262.mp4?token=TrUSqR1zcVX7Zhs--1MzICcMdAOycjIx3dpaYVRp_DkNq055GyhChoJQK4v93ABuLAMzlZ0PcB7UgdXezjFP6eOfrXqf4fVIXGmnXayV1E0DDbBoBhsr08Cg8QRm9gS5ZQ-16DVtFxyJSDmYRHsIEJgLHWDfJQ037eN50EsmY6GIVaPXZA4LyI-kL3FxVlXZZXN2JyjWKzVBFUHc5kHaGIdonNpcsRCtx6S1YXc5EGFWqnC-qckEiwUPnaYcYEbF3oDOZat-hGxTpA0zWGkA6A5HJJI6Wbk5_MvJdmivC4DeL3GQiCc5ueLPSLGKIcy6eP0ME2BVKksqVoC2ntcUCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: توافق ایران به امپراطوری آمریکا پایان داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660729" target="_blank">📅 10:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdrfYEx-kU-HBRD5YfUYERbG490Uz522Eb0wh7LedgwcDZu6fjiw7lptxTVuuna-Emay-E67-bqMyO77UtvHQiSvw3mB4M9h32vyQkuIpQWdZaw5IKpIUzd_ossgD9Uaj9mmgGn4DYvtJ_EDW5707wHDyBF2f7dsxI1246IhhUBHAtZTHRdNFg-Lqcc4tHKnZWcOd6LvXvjSNsOJ6StIr-UrrMxYojkXYOs98yLFui7kVUFAjXMieUa2bEfHjdee-QTUUVHs38h5kJis0vgTGfDPkKdxeTEnQuL7ncCMXh4kwQj9QKhYuIEqENeq3JFMSzkRQr2RT5CikVELwMKxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوزان رایس، مشاور امنیت ملی دولت باراک اوباما در دوره امضای توافق برجام: این یک سند تسلیم وحشتناک و حیرت‌انگیز است که با صدها میلیارد دلار غرامت تکمیل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660727" target="_blank">📅 10:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4254c932f0.mp4?token=h_X5IJCF2jVl6Sl_CTZId5FKl2kK-NGcR42dauB7XMvCnKwwSsWWyQUuYYp4IPWMHkRxVqbZFtJNQLpBH299qZFnC6Zavpp_duF1FIdGFEPkrehcl2lqj89Fo2EBniXJi3brDjhy14feIq2otK4jCKLVwmOL7oZx2yCHVbj8oJBczGuzesRaJCx7B2XxGoh6RqzUZNmIPr-reYkjQpQrSrPEcSutNvJg_1Crc5U-EXgX9YJg24XFgEE406m3QPNVt7DKxn92UbYb8vPUGVlnHtYhmVvHvedlXCkX2K4i8wTCoOKWZR4J8itaT6NwS5W1x3wO_O5eQEhTpQMwmpEoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4254c932f0.mp4?token=h_X5IJCF2jVl6Sl_CTZId5FKl2kK-NGcR42dauB7XMvCnKwwSsWWyQUuYYp4IPWMHkRxVqbZFtJNQLpBH299qZFnC6Zavpp_duF1FIdGFEPkrehcl2lqj89Fo2EBniXJi3brDjhy14feIq2otK4jCKLVwmOL7oZx2yCHVbj8oJBczGuzesRaJCx7B2XxGoh6RqzUZNmIPr-reYkjQpQrSrPEcSutNvJg_1Crc5U-EXgX9YJg24XFgEE406m3QPNVt7DKxn92UbYb8vPUGVlnHtYhmVvHvedlXCkX2K4i8wTCoOKWZR4J8itaT6NwS5W1x3wO_O5eQEhTpQMwmpEoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ گل برتر دور اول مرحله گروهی جام جهانی ۲۰۲۶ به انتخاب FOX
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660726" target="_blank">📅 10:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238281eef9.mp4?token=plGp15okGyPS7Y8VQuVWnsAi-XTVCTZY7eR6oiT8RpwPbCbCHFR5YQAqRUaeW82SAGIU5bmhRCCsxlv_SmMwOUk3452UQ_1omydANH16Dq4e569bH7he0w3l0xvkvMln3-BskS4ii9XWYrPBYtFhUi-a260d-E94mN6C-9GSMZDnk-SFU8hLqTJjXclHGbj3qwQCD_zDqAgWRpOAx20yehw5N7e3llNxlxWvVdJ_U4Sg6Yso82iMLuves9L-comlhL1nWl_P45M88BALFpnHtoEgm1UsiT5oQhsSeI8t8ZwOLMF9Qv8M9YZIOv5YbrLUGD9tyqa-t9OL2v4rr7VHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238281eef9.mp4?token=plGp15okGyPS7Y8VQuVWnsAi-XTVCTZY7eR6oiT8RpwPbCbCHFR5YQAqRUaeW82SAGIU5bmhRCCsxlv_SmMwOUk3452UQ_1omydANH16Dq4e569bH7he0w3l0xvkvMln3-BskS4ii9XWYrPBYtFhUi-a260d-E94mN6C-9GSMZDnk-SFU8hLqTJjXclHGbj3qwQCD_zDqAgWRpOAx20yehw5N7e3llNxlxWvVdJ_U4Sg6Yso82iMLuves9L-comlhL1nWl_P45M88BALFpnHtoEgm1UsiT5oQhsSeI8t8ZwOLMF9Qv8M9YZIOv5YbrLUGD9tyqa-t9OL2v4rr7VHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور کریس مورفی: این توافق جنون‌آمیز است، ترامپ تسلیم شد و ایران پیروز شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660725" target="_blank">📅 10:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f359529c05.mp4?token=kFNXvkKQ5DCIMzUjVN4ZOvE6Lmya5_1e3I7GSkXcfQtKNK2RiT2uyCWE9odOL2-4a5tDxwKvpc02NRzobAdiuoPJ41f5ZAU0BUcxA2-KqfotIT5rI4xdWXMCFn0Ni4Z4EqQd238HygqmkNiNeHdOxn-SEt-M8IngNjJYqCRGL4LFU5mWVg8MsHJxP-bqCdLB7dnpVEXBXuS-tkuxObUAKg11S-UZ0VvcSU4ULBDNATQs5I_3K1zOZP9tL74yq6plDuFZkwVCHaCQQOzdPd8xq6j7VvUb04t124hPhQ-wv76ZA5JtKRXlccPb4E4_EqEiAenpMD5Kphb0JtNa534S5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f359529c05.mp4?token=kFNXvkKQ5DCIMzUjVN4ZOvE6Lmya5_1e3I7GSkXcfQtKNK2RiT2uyCWE9odOL2-4a5tDxwKvpc02NRzobAdiuoPJ41f5ZAU0BUcxA2-KqfotIT5rI4xdWXMCFn0Ni4Z4EqQd238HygqmkNiNeHdOxn-SEt-M8IngNjJYqCRGL4LFU5mWVg8MsHJxP-bqCdLB7dnpVEXBXuS-tkuxObUAKg11S-UZ0VvcSU4ULBDNATQs5I_3K1zOZP9tL74yq6plDuFZkwVCHaCQQOzdPd8xq6j7VvUb04t124hPhQ-wv76ZA5JtKRXlccPb4E4_EqEiAenpMD5Kphb0JtNa534S5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه نماینده اسپانیا به ترامپ: تولدت مبارک آقای نسل‌کش!
🔹
نماینده اسپانیا در پارلمان اروپا در اظهاراتی آتشین و کنایه‌آمیز، ضمن گرامیداشت تولد دونالد ترامپ، او را «آقای نسل‌کش» خطاب کرد و با لحنی گزنده، انفعال اروپا در برابر تحولات منطقه را به باد انتقاد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660724" target="_blank">📅 10:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660723">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-g-SRPt2Wl92uA1-FIya35AxBFmMkXxOcpPEPjWaj0SPc7e1wSwCo3ZV0yl0hmhD6xf1eCH4Ds3o8tgHP545an-dc3ezprC2B95AnbzPaLTqrjPVXoDE2XfzahuKOp6lA-Yx_XtS1LeiderxSBjdVsHqSr5GoDRtyVI6ps2tcpuyKhEkvbr4wA_Q79X_BlzPZei8OFKkMVv9FdHD6QtoDocxNsqUoLaECxU_JS09IJm5IKOD5c3j7NVm_Qeglk53_bcxq2U8Hgb-2UbsvR0upRfJr1FP1DX2o68WqtUsyRnY38aHriOPMRMbubmiGwtzReh9T5G1xrqwiFqsqyiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ابطحی به امضای توافق ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660723" target="_blank">📅 10:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igNwrZO8OU9h5Nuv7qcF6vSRWp4kAg9gN3g2I9VjftD1u1GEpOujoGwCC-uER2uDAYTa_eL2ZECS8To0xRK6jBqbGebLu3LG_DHxbmWAD1N7cm38lvlYZhYcX7RNBWWUzD4m4RMNMA2jOrV8pIRQmyJfgGxi5McdbeN8QgWMvW4nIzm-wepiyRWsovm9eA0oG09S_Msps73YYLk53ZogCepgQ3Sm9GrqDXcFimrP22Jx_f_sVm-1oE9Xai-D0trVz_dpECcMYgur_476PynMs40ajA4JK2-DXl6EGXBQbf8HunD044Qc5HVFZqQ-SYQ4Fsm0E54Ec-k7Y_hsjCgCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاری که کمال‌گرایی با آدم می‌کنه #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660722" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqhNPX0YHPqmMmRWjJ752e3QlV1thW4JsdaCdFDqvcMeRPuLEgP_gczbDAjqvFz4007YjJmywJC9rCQuw7EI6UEqmgEsXlcIHAUUlnHG06UmBIj4p10FyiTeDPGOb8GLLiQ5WQWxPeBPaBODIiQp4s9zmX1yIVHJ92pErps62PyErcncSxFqNRpmfn9vBvSCa7wDd01zFuTG6AwcpjR8FItmpY8voz7-XPN5_Rw3ogEayIdPYOsckxwOFJ_pXwXM1w-GLHpeR4rzNtey-XzFPmjsqNFsxvbK_KPp6n4kcA745cW0HbsxlBW3WR9Pht5bJJOpIuwKhthOJaFe5WyQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660721" target="_blank">📅 09:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLrKVAE_KxfTTF9kYGVEVcXYURss-Z1PRyxYFH3L4V0UFMTCBR4Woq0aKRnFXkkvFvBf84w9obDGioCgna5mwgxbNiumW05AmTqapH9AXzwIU3pfG0DuMBxV39yaELz0NHOfNU8imseq5_Q9WBwyUDKcK0XGtPaGubfJFfZJ9cN3W62o3lTn_E3vA-stfKsL4G4aDKEdsbtLnbCR3l4I9WxltGOE3sis2Ea1hi0-2fEqfnr0lkW90qK-3tHl-aS7RIm6c5325OwJMfnbYt6ui04nP7jJpvGkxTu06hI2zyfAFUds2DmAZg3WbsNhizrQN_lO2qroGzbyat7PtrvdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازی پاناما و غنا با ۴۲ هزار و ۹۴۲ تماشاگر، کمترین تعداد تماشاگر را در دور اول جام جهانی ۲۰۲۶ ثبت کرد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660720" target="_blank">📅 09:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سوئیس از برگزاری دور اولیه مذاکرات ایران و آمریکا در روز جمعه خبر داد
🔹
سوئیس از برگزاری نشستی با حضور نمایندگانی از آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مربوطه در روز جمعه برای مذاکرات اولیه خبر داد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660719" target="_blank">📅 09:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifd7pNgXax7cY4RyuBmbjcewD8tgzEzCdcNcOTeg8PBlIrG8F-2P_sL7qXbG2RJ7pCU3d1FesR9UB6w9nnifZtKGHSG1mDMpfTrssOXZvwv0FVUGKE2virfXnGrrBm0DznUrlxS1rabSDta6EiaKJ4fbVFA_kEscp4Sp5viAZKe_mOaN6qgZeq72B2F65BCIBx4ZbQCxaOGF9xfEOPDK8vUTYfpM0RbZRFwC3uNyYSKaUftganZ939q79M--b0kTIJh4ObBP-uHEKjszp81UnEiPN3CxddKvHev_Vdr54vin7xJ5x-grbMVbnNI-VfLWk5M1BeKDL89d4lhuJbCO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثروتمندترین کشورهای جهان در ۲۰۲۶؛ لوکزامبورگ در صدر
🔹
بر اساس گزارش صندوق بین‌المللی پول (IMF)، ایرلند و سوئیس در رتبه‌های دوم و سوم و سنگاپور نیز با ۱۰۷,۷۶۰ دلار، ثروتمندترین اقتصاد آسیا شناخته شد.
🔹
آمریکا در جایگاه هفتم و ماکائو در رتبه دهم این فهرست قرار دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/660718" target="_blank">📅 09:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660716">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK78Xm1snz1Gou3O4eiMlLHR869ok2gW_Z0jTNAwr0O0LIF6ygXi43bZzg0nAyCY1B78aNpL_WkLC9ObGBBdG6wN7dR5GOOZ1NqNQu_xAa_rx0Rp_--TLoBrc8Pp3x81sgyHE_WAB59jp4F6o1qDU8axAtm0ye00zajAUenx1mnrbHpoD3X6_oJxO5r-TV87q1_UW46kl5oq_j0vOn-iR3QE-mqSCkLsvt9xUN7nCcQNXJFqvZqTTLdTabFVfcTpn1vdp29XclI7lqjwDMPlwI9XkVnn8sV4XeHkDnirw65_QeestHCMo-oKCQlNVarcNJEUEGuwVFhsya3tv54kHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت از ترامپ و مکرون در ورسای
🔹
دونالد ترامپ شامگاه چهارشنبه به دعوت امانوئل مکرون، رئیس‌جمهور فرانسه، در کاخ ورسای حاضر شد و تفاهم‌نامه پایان جنگ با ایران را امضا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660716" target="_blank">📅 09:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwAIl_NaYjESlD8O-W_4Tire4iLmllfFlWQEN8t4CmlqX83xmIqAhFb3Hdc9NrTBy9rmIAUsGV_Ngn10zO_F-574isG2wPt9HTTYlZsMJAoBjCUqw_ctcxBGIiEurf6m3G5FUIJofnSYXOPh1zngblIhGx3ypn_ElmzyBs0p-UVHfg_rOejnViIay5zA5pLtiouq1SFBtoa9-seBdanZ5taem6xNnvCmhfYfMsJ2BcejrwRMPol9L9-DhNEdtwGtsHR3c-lQ7WwPqCjC9K8zOe2UMI7cQQ1m2j85dUocPW915wpL3AJ4G2e4jNqlk6lzHTX3zocR4wo6RpuXHjWqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه بازی‌‌‌‌‌‌‌‌‌‌‌‌‌‌های امروز؛
پنج‌شنبه ۲۸ خرداد ۱۴۰۵
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660715" target="_blank">📅 09:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660713">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqaoMoQ1zj2RC6c-OO4lG0qoRHL_L3JQ_HjAX48FR8MH5cCvPYpZJcMsGfBVfv818tQ7LG8RHemH-IUTlWgqgAgIwZ-zeZnFF5hqkbK3WKaRjvRa9c70R9oQCuMGM4KkdK7CxCwaB3om8C2PnOjraWtqDzvpgfi3pAsEjHPB1AORTFIH1jwjNQ0aVWGdn1uVaaReK1043Cq5QVmwGv44DY4aXpwj_sUCeBOeyATINp44qH_Biwd9mPF0VGt-bTk8TU-_whEarw6EaRVxMmDo3OaRWQltqm-45OtsutVTleKNLxr55TBE7POmzLHmeTtSOkQoCoqlS24xEJwmghqpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلسم بزرگ؛ رونالدو در ۱۰ بازی اخیرش در تورنمنت‌های بزرگ گل نزده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660713" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660712">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0572ec6d.mp4?token=WmicQv0q9itw_3Kdo2Eqily6B6vDcsnKJFRUgIAmEc9lWwo7ELkJHR_v3TOyHai1ak2C0YeeXSThR-FLNM7vCgNIuzj-qatIFRsAsX2SRpF5or0ZgFL9_c2D4z8MEc96ti8vTn3kVEXoaw1b8UNRRRXpQcSt27s73dpF-uw-ug0JhaGX-tktJnOwiBg0V0sqZEpDDNHJbSVIWV1OwTJaViPtjaPS8HT_-wizHpSxNUi8iCkf5MekCzBFIvXWSz-hk358Pz_2HAlMbEMbFL3Oz4Q6ldIGPbk24mzLZUP-L8iY-pUARGp4GsMjZVCW5NjlaECkYH7E9HrqFFaGlIH6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0572ec6d.mp4?token=WmicQv0q9itw_3Kdo2Eqily6B6vDcsnKJFRUgIAmEc9lWwo7ELkJHR_v3TOyHai1ak2C0YeeXSThR-FLNM7vCgNIuzj-qatIFRsAsX2SRpF5or0ZgFL9_c2D4z8MEc96ti8vTn3kVEXoaw1b8UNRRRXpQcSt27s73dpF-uw-ug0JhaGX-tktJnOwiBg0V0sqZEpDDNHJbSVIWV1OwTJaViPtjaPS8HT_-wizHpSxNUi8iCkf5MekCzBFIvXWSz-hk358Pz_2HAlMbEMbFL3Oz4Q6ldIGPbk24mzLZUP-L8iY-pUARGp4GsMjZVCW5NjlaECkYH7E9HrqFFaGlIH6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد«فلسطین آزاد» هوادار تیم فوتبال انگلیس روی آنتن زنده بی‌بی‌سی؛ خبرنگار بی‌بی‌سی برآشفته شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660712" target="_blank">📅 09:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660710">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd638263.mp4?token=aTh2I7AL7_m7BgZNE1u7mIMAWTGnf5TvGoENAzTmxsLN0oIdIbuL7a8FBHyLa7_PTW118HZylpcnir2vb_CV85ZR1nAKYrmfWziYI4dRqX9TYV_Q3UfEB00iEeKsZpXTwZvn4qEReJ_smF3Gtj_TIPK5WVPb37pMIO8z3GcntNopqTqgU-ec4epS4owO98LtRvTith0yEdvThguJpSblCinEb6szs6rUzEKJQcb7klotEqe7v2PpmNpDBXl5IiDxlZN7ghtYLt24sb0FsyeAEMKHcUysEASy2kojUmTgoQ1hwjOT7TKQpSaPvM7pzXhuIyf4wI_R7wqrJ2hfwXKX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd638263.mp4?token=aTh2I7AL7_m7BgZNE1u7mIMAWTGnf5TvGoENAzTmxsLN0oIdIbuL7a8FBHyLa7_PTW118HZylpcnir2vb_CV85ZR1nAKYrmfWziYI4dRqX9TYV_Q3UfEB00iEeKsZpXTwZvn4qEReJ_smF3Gtj_TIPK5WVPb37pMIO8z3GcntNopqTqgU-ec4epS4owO98LtRvTith0yEdvThguJpSblCinEb6szs6rUzEKJQcb7klotEqe7v2PpmNpDBXl5IiDxlZN7ghtYLt24sb0FsyeAEMKHcUysEASy2kojUmTgoQ1hwjOT7TKQpSaPvM7pzXhuIyf4wI_R7wqrJ2hfwXKX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اگر به بمباران ایران ادامه می دادیم، کشتی‌ها دیگر نمی‌توانستند تردد کنند
🔹
ذخایر نفت ما هم حدود ۴ هفته دیگر تمام می‌شد. ذخایر جهان واقعاً تمام می‌شد.
🔹
اگر با ایران توافق نمی‌کردیم روزی ۷۰۰ میلیون دلار ضرر می‌کردیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660710" target="_blank">📅 09:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2666505efe.mp4?token=BPpA4YyLSg-oMY3F8zNhYxoGjuhgIC-Kk8jPWVtNv5MRrHUOo79FwN2l6MnZOk5FlAEmpk7BC7ztBc4XK6Jq5naIJHO95RR11hb780f4Ai2AWPLhTWjiD8UNU-GvK1DQaU65872UAbomaA5LIx_WRdcyskxtfxwTKlwrIyrulu-pI_NzdY5hqm_wWcENqMo023oRu8UyYzolpWruFazrjELCRJuMfIfL7JXHXWHEkepMCvL6Qdx2Sy-rul66OW638QWVxn856csB44Yeo_v6fM-VpYRAPR8RBDMt9caOq3DUdMUUO2_kqALt-PscgEo11jrb8oQkmoF2t17q33Z7_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2666505efe.mp4?token=BPpA4YyLSg-oMY3F8zNhYxoGjuhgIC-Kk8jPWVtNv5MRrHUOo79FwN2l6MnZOk5FlAEmpk7BC7ztBc4XK6Jq5naIJHO95RR11hb780f4Ai2AWPLhTWjiD8UNU-GvK1DQaU65872UAbomaA5LIx_WRdcyskxtfxwTKlwrIyrulu-pI_NzdY5hqm_wWcENqMo023oRu8UyYzolpWruFazrjELCRJuMfIfL7JXHXWHEkepMCvL6Qdx2Sy-rul66OW638QWVxn856csB44Yeo_v6fM-VpYRAPR8RBDMt9caOq3DUdMUUO2_kqALt-PscgEo11jrb8oQkmoF2t17q33Z7_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی کیروش از پیروزی غنا در اولین مسابقه خود در جام‌جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660709" target="_blank">📅 09:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660708">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9508847445.mp4?token=dLS0OnyWzPDgvpmBURzojKiunRyxCEqWQXNQiQK5A8uGXFJhbjoANgAwiUaK7a8VnGGfytfXqzlDSrS5Hagx-rNZcMg7VCGsE8gAJ_varELnbRe8cXW7pL-BHaMDLYyVdPw_Xyb_C2nBlULRYhLtJEjFEDophMejSvPRPpeFL41nhhbqlzr6DxPvh7gbcBYbgBMNUU-dLnWBUIboLCf8iTRKsjExOvBo3u-on-vuid-AzrfQXLAVby83PFb73tP59Enx5Q4c6bPL4vRxaE6BEf2ExQBKF3s5evZPXDw6ZtSJ_4lTSEYK1qUL3ezxyc9JM4AV-IixXeEme4CU6jc6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9508847445.mp4?token=dLS0OnyWzPDgvpmBURzojKiunRyxCEqWQXNQiQK5A8uGXFJhbjoANgAwiUaK7a8VnGGfytfXqzlDSrS5Hagx-rNZcMg7VCGsE8gAJ_varELnbRe8cXW7pL-BHaMDLYyVdPw_Xyb_C2nBlULRYhLtJEjFEDophMejSvPRPpeFL41nhhbqlzr6DxPvh7gbcBYbgBMNUU-dLnWBUIboLCf8iTRKsjExOvBo3u-on-vuid-AzrfQXLAVby83PFb73tP59Enx5Q4c6bPL4vRxaE6BEf2ExQBKF3s5evZPXDw6ZtSJ_4lTSEYK1qUL3ezxyc9JM4AV-IixXeEme4CU6jc6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه امضای تفاهم‌نامه ایران توسط ترامپ
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/660708" target="_blank">📅 09:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660706">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست
مشاور نخست وزیر رژیم صهیونیستی:
🔹
ما خود را ملزم به بخش مربوط به لبنان در یادداشت تفاهم ایران و آمریکا نمی‌دانیم و تا زمان خلع سلاح حزب الله از جنوب لبنان عقب‌نشینی نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/660706" target="_blank">📅 08:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875b08b05b.mp4?token=jhFIvc2HsJiPjcaxFa1kmpysC0pRHwCQ41WR1WL-hIFo5e8U-ONH_zrpFftx2IOt-PzHldnIRJXw_3_24qx5QRhZzxQEWEIUd8k-KK7SSyt4xCSjm_qlP90pg_UsCxfNiGeB2JLN28lSToBHTsJclsgKU3HXURJnKu3jyTx7L7mx3Tzt7rv7JQIQyA33it7GHT0D2i-0L9F47sRh8aV3CMUZy2kykmzdaJ-EkolW0H9dV0iodhh_qZEa5SDhHLy4-JSspOSMy9_skGyR48T7TkDr8Fo1PW-FfZQmqy64QVJqkkxEsq3F-kfhMwM2pB4OFuzrzRiTC3RM7xZ8eAQt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875b08b05b.mp4?token=jhFIvc2HsJiPjcaxFa1kmpysC0pRHwCQ41WR1WL-hIFo5e8U-ONH_zrpFftx2IOt-PzHldnIRJXw_3_24qx5QRhZzxQEWEIUd8k-KK7SSyt4xCSjm_qlP90pg_UsCxfNiGeB2JLN28lSToBHTsJclsgKU3HXURJnKu3jyTx7L7mx3Tzt7rv7JQIQyA33it7GHT0D2i-0L9F47sRh8aV3CMUZy2kykmzdaJ-EkolW0H9dV0iodhh_qZEa5SDhHLy4-JSspOSMy9_skGyR48T7TkDr8Fo1PW-FfZQmqy64QVJqkkxEsq3F-kfhMwM2pB4OFuzrzRiTC3RM7xZ8eAQt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبدالباری عطوان، تحلیلگر مشهور جهان عرب: سرانجام آمریکا تسلیم قدرت ایران شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/660704" target="_blank">📅 08:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وام‌گرفتن گران‌تر می‌شود
🔹
بانک مرکزی قصد دارد نرخ سود سپرده و نرخ سود تسهیلات را در ۲ مرحله و در هر مرحله ۵ درصد افزایش دهد.
🔹
با این حال این امکان نیز وجود دارد به یکباره ۱۰ درصد افزایش را اعمال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/660703" target="_blank">📅 08:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204da3dd8c.mp4?token=JSSIkF7bP1DG7cdEZA9t_BXavZ0VapZFM6pfbjori-DqJbiDOTfEzDumJCFklbjDqRrym3bZZ_QfCEG6qokjN_GMJF-f-2KBMebvYPMAU3HXv-sdol80oH1hO41nPLuEY1h3sqIrqLJdLNZuVnYyA-fnT1vHIshO4ozl2iC_nInx5EClDPoGHHzMU8I5YvBAazZqrjBvh9bIdE2C3R55u6ziBYxUBjDiS2y0oOTYj1bpzsoqa43arPOTnsqrH9-LSHleghLTcJirbpQ92n8ikcTdkgBhmqlFtabrseljg3kZV1Vnb0077xBGauEsxWOuqbq9Vqm6cIslPQt-wOfYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204da3dd8c.mp4?token=JSSIkF7bP1DG7cdEZA9t_BXavZ0VapZFM6pfbjori-DqJbiDOTfEzDumJCFklbjDqRrym3bZZ_QfCEG6qokjN_GMJF-f-2KBMebvYPMAU3HXv-sdol80oH1hO41nPLuEY1h3sqIrqLJdLNZuVnYyA-fnT1vHIshO4ozl2iC_nInx5EClDPoGHHzMU8I5YvBAazZqrjBvh9bIdE2C3R55u6ziBYxUBjDiS2y0oOTYj1bpzsoqa43arPOTnsqrH9-LSHleghLTcJirbpQ92n8ikcTdkgBhmqlFtabrseljg3kZV1Vnb0077xBGauEsxWOuqbq9Vqm6cIslPQt-wOfYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب گودی کمر  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/660699" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3009c87001.mp4?token=lKfzEqE4hKGVzemUs4IfQOkGbZv3S-1k2TdyjxvpNRg0cWOrGN5r1yIb1VOwmR8ZQ_6dSfOzPoy1mhnbutwOXywTMeJR0QcyfhBeeHWW22FsN1JkIjU5B2Krg3FGLIrt4qN5VFERJ5e8usaTbRRjfJuyO8hqdad_DwzYKEgIxIGSZWtbLskmKN_OgBGI0i6ESM0xA-X2_T1nUxea0RmXFFHCpUn9m-9_CRzMkF3zq56HkWsupjK4aNuYbgQA6r1tCke-snWtXSp5NwhQLDhRSc-2GzpaN4ChXIW-1oEpyvKWVxEdCi1-mwoe13BMf0MuZ4DjLy1RH6C4VGGMj6L-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3009c87001.mp4?token=lKfzEqE4hKGVzemUs4IfQOkGbZv3S-1k2TdyjxvpNRg0cWOrGN5r1yIb1VOwmR8ZQ_6dSfOzPoy1mhnbutwOXywTMeJR0QcyfhBeeHWW22FsN1JkIjU5B2Krg3FGLIrt4qN5VFERJ5e8usaTbRRjfJuyO8hqdad_DwzYKEgIxIGSZWtbLskmKN_OgBGI0i6ESM0xA-X2_T1nUxea0RmXFFHCpUn9m-9_CRzMkF3zq56HkWsupjK4aNuYbgQA6r1tCke-snWtXSp5NwhQLDhRSc-2GzpaN4ChXIW-1oEpyvKWVxEdCi1-mwoe13BMf0MuZ4DjLy1RH6C4VGGMj6L-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد شدید بازیکن ازبکستانی به فیلمبردار مسابقات، در بازی با کلمبیا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/660698" target="_blank">📅 07:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siuan1bXcD3BbXM3mkPfyNc0kNJWzjWfzcEZ7YV5vnb5Ksj33iPv_Vz0YTsfJBwbsQmLVTr5eaRkIlRI1SIMMGQ-16ljS07Mwl7p_0mHRVMZ50AB3-5JWby_Va5NMJnJQ_372IkD8ubIyPgs8Fa_2iG2Enp5DUZ8Z7TjpMtt6M8XdQVZbezptbzShGduDnEbS0F-5_PzFj2T2HAJ6iro4vCEbbWk_p8uGVXUpQmnmxfyALrao2HTYzlf_gBJ6s7BASoCKUnLNB6n5FgmpXADG2U1KdTBhCmU9SNVQ8zaIhD2B0pvU857uKuTVopXT4vgy9_E4SweMZ2iI4l8U9LzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول رسمی تمام گروه‌های جام جهانی بعد از پایان دور اول رقابت‌‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/660694" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هشدار روزنامه کیهان: بعضی سخنران‌های تجمعات شبانه، در پوشش انقلابیگری تفرقه افکنی می‌کنند
روزنامه کیهان:
🔹
متاسفانه در این شب‌ها، هر چند اندک برخی سخنرانان هیجانی در پوشش انقلابی‌گری و با نادیده گرفتن اوامر رهبر انقلاب در حفظ وحدت و انسجام ملی، اقدام به پراکندن بذر انشقاق و تفرقه در میان مردم می‌کنند.
🔹
لازم است نهادهای برگزارکننده در راستای امر رهبری بر این تریبون‌ها نظارت داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660693" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf019f3a86.mp4?token=D04PQ9fSSFoZ2nLzj43LRyJL-ALh-SsYNxm5kXPFo7rantAjXvIWPMVCawiir70XH6_gvQxXrY3aWsvN9I4V0ynHtsj6nKa0pRGeLP6uvt78TRa6k8nXceCNE56pT2k30teKJ0lra6CXiOqZ9e4h-jHel9QCBgiC09iIjbbfnfhE838bPThvKdqthisF_1biDz3vpy_uSh1W-l-Mq6Sp2jEVx9ZKyvjMLbV335VPPZ-ilae4A8m4rAB96U5JS9sqj4epnH7Q5WhLkBy2kNhH7zdEsa31BaOYJ7ILGRNKxb4RDMAfiLBfN8IftCw_6F0v4BG5Xa_MQhmEgttTLcOW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf019f3a86.mp4?token=D04PQ9fSSFoZ2nLzj43LRyJL-ALh-SsYNxm5kXPFo7rantAjXvIWPMVCawiir70XH6_gvQxXrY3aWsvN9I4V0ynHtsj6nKa0pRGeLP6uvt78TRa6k8nXceCNE56pT2k30teKJ0lra6CXiOqZ9e4h-jHel9QCBgiC09iIjbbfnfhE838bPThvKdqthisF_1biDz3vpy_uSh1W-l-Mq6Sp2jEVx9ZKyvjMLbV335VPPZ-ilae4A8m4rAB96U5JS9sqj4epnH7Q5WhLkBy2kNhH7zdEsa31BaOYJ7ILGRNKxb4RDMAfiLBfN8IftCw_6F0v4BG5Xa_MQhmEgttTLcOW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: یادداشت تفاهم با ایران، امضا شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/660692" target="_blank">📅 07:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کاخ سفید: مراسم امضای تفاهم‌نامه در ژنو برگزار نمی‌شود
شبکه «فاکس نیوز:
🔹
«امضای رسمی [تفاهم‌نامه] که قرار بود در ژنو انجام شود، پس از امضای آن [توسط ترامپ در] ورسای لغو شد».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660691" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toU1WWUelVztSLG00uakHDsNw5hXscRe2f_0rEgDavC48wUS5UObJl78dgGEkcG6YfOFe_TP_xBpyHkXCeAK2qJXHGBoLB9eKy9wi7cQQhulrAU33b-ILZZ4-OJxRFasN2ApAWLo6hGOie5eGjXvSmGoP_xjAnj8tI6-GWQYKZzXURHkLigM64aHYyl0iVIk68oSySxcSbyg5OvJC86OW-aqVyhu3TNVR0df3bySE6tzBD2PQD7NLorFRawDXjGkMZ3RUGY_s1nBbDrKizNwqHg5hPW4AMscnGbvnct6Odx2JVTwFplb-x18UMTQyCE5wEpLuXVdlHTJlc_RtCj1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxcGH20HsGbpsuanXz4HfZ2f31MoUV7ayDbeUshXgpBS_Gpma9DhSNpW-9i66Z5HUGLLmc6PDf475eDgyqOeVY1fb_Iu9UJEzmx5V2UPsAzxdq94gGWjjPWHaet9wgdYi0V3t-5CrRRu8bYPDyvC84ALU5WD3S9S4SmNw5gu5kb87Eik8Nod5A9xHuqRlVs6csYlaBjnMpQ496M1_7Sq8Z4vZx6RS13fJ9er1MyvJVYVvKkG-Ocd454mebYHCPHVfg5kqInJE342joumBrQJ4Kei-SudIaROI4Yt8Dtc4MjiRGubyb9Yfdh1ZiHiJBdj1hEGvUNtNkiJ-t6WKBxA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEhvykU-c5Iri59Wevji1Oa3DtoeGAvl5ZQwyt9h4_GCUK7oJT_QdUWZkDcRkKDxKeBAANu4LrCzEqDGDsEE4bQ3pT5jYpCD79D-sTstZBWFSxxzxAAY-atsm0P-tSOVWUBJA8nxa2kgrAWbe93KrAJ3gb2fpsf4DcOpXZxrAqV8_loSYFYovpyh1sRTXfeVZu6gE6wqycfKpcjASFTt6dvn2AK6OM30SdZSMu5xwOhNGA59hHAA7n7XSNWoZGYuEbwWcl-HCX-EbOd4h3wstdDhqOnhH81xnUocwBrQ1GODLorLyII0irTqhEU2Y7d76PPbWlPcfgtdPb0riMezFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkAzF4NpuNXWNDnX3UWuJgCm_b8BpOthWOEQ59H2KunATAxh1z9k0z_Cs5MPdFRAwKSMnuyrWQtDP1mnRA3Lm_CerGQp1hgv_GAyoMJa55qJ-HIneZaWlnxd4DeuLj_-0oHEsRySB1GzIKYqfP0s42pzNIWK0jONPeTh0GEFxSGjfzufdgtud2vq0vSBzLgpEgUqwwAIpsYKrq4pniq4ycYiOm8GuLKo1BqHR1hulz-Pj_BKtKGJz7OHE4fyhomOFARGk2mq52A_49Vqz-RgGsAo2585XCd0heOVwkwHugtLRCd68vD8ykjtmeKWmnp5D9dRu4dz3RGAQzil-FwGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHIeSeQlXiqvkRFiqzdC3hbFZurmsB4E_LNjmedf_gfA7UyTVgX8HXpOd86pP3CF0mxLC3PQp5oyOyFevkK2gJ4A8Wg9EXVcGwU4VJJONFOLC_GftRRGPUDBg5H2_ZTHlCUvPUiM0b1o9I8k6r9eJjtHIHUiHsKMKzoaocZP1AMOlCkA_9r0YWhd6k5WMNK3RCf10CfUe2u5Kk6XjDQfgKaFrf-SbySJl8e-rcBqYmZtnxDIOPz3bPnA6BWIcUb4cxgZL2TLYs6_y4q-oWKVQ3fZSfFUsoMMkSbWbrkRlaY5k5W6dMZFbxJCp6ZXYzeG9Bmr01KXHT3iGpPkZ7GCRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
🔹
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند. @AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/660685" target="_blank">📅 07:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660683">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db2b6199.mp4?token=u2F7RYNSVdXkeqHXKS2mE3XSFlHuacasnUVjvWDR2AcLdstMgbcy6TpXuJrb6ZL2tilZC36rBBE6CxkTQNfJOuv77Y1cMjLu5DnT0H1TrFnm_9dIcKACuBye75asIfWZBmfxSZbZ7YbqSEpXXJyQeP5ohLi2lv1PZSnYq2RRWwG-6C9Y_Hp4l7zDpAJmStx794sh2EHxc90h1g-X63JsA_EJOopfDsjJuT59OF4ZES1MKJu9viozQZsG-FpmX3ZMENr5fRt5kTwcidkd5mlQrYjzapmE5g1LY7Dz4LzJP3iz058dlrJ2xbMLJ9aPv1S9JcBD8r_NG2Et4Pcr-1-7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db2b6199.mp4?token=u2F7RYNSVdXkeqHXKS2mE3XSFlHuacasnUVjvWDR2AcLdstMgbcy6TpXuJrb6ZL2tilZC36rBBE6CxkTQNfJOuv77Y1cMjLu5DnT0H1TrFnm_9dIcKACuBye75asIfWZBmfxSZbZ7YbqSEpXXJyQeP5ohLi2lv1PZSnYq2RRWwG-6C9Y_Hp4l7zDpAJmStx794sh2EHxc90h1g-X63JsA_EJOopfDsjJuT59OF4ZES1MKJu9viozQZsG-FpmX3ZMENr5fRt5kTwcidkd5mlQrYjzapmE5g1LY7Dz4LzJP3iz058dlrJ2xbMLJ9aPv1S9JcBD8r_NG2Et4Pcr-1-7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاریس تفاهم‌نامه ایران را امضا کرد  آکسیوس به نقل از مقام‌های آمریکایی نوشت:
🔹
ترامپ شخصاً نسخه‌ای از این توافق را در جریان ضیافت شام با رئیس جمهور فرانسه در کاخ ورسای امضا کرد. عکسی از توافق امضا شده برای ایرانی‌ها و کشورهای میانجی ارسال شد»./فارس…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/660683" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌سوم</div>
  <div class="tg-doc-extra">ابونصر فارابی</div>
</div>
<a href="https://t.me/akhbarefori/660682" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
ابونصر فارابی (معمارِ سیستم‌ها)
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «خروج از تفکر جزیره‌ای»، «طراحی زیرساختِ روابط انسانی» و «آرمان‌گراییِ عمل‌گرایانه در محیط‌های آشفته» مرور کرده‌ایم. تا زمانی که نگاه سیستمیک نداشته باشید، تغییراتِ شما فقط مثل دستمال کشیدن روی شیشه‌ی کثیفه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/660682" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660681">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16162bd5bf.mp4?token=d1iLlDe9ZFT8aOjXBqmcWLBv63ugUtwhIGJjj5NtdV-5OiZQj8syraWnC6LWQc08BTVO8fhrmbHaanEJsf4jTayOQdJOkSdKVV3_kCU57OrtM7ljwtT3y1Rz9l_wXESNabLih2TPbpjaHOKW88zpD3ZTh8-eIIVS4bfo66jw4Exv5Z5tPARGY60A-YO5ABknzP-b-v33rIeX5dK7P1Jwi9Z8I49UOYkDa4BabihPg563qMC2LMZX8BMzM1ol_dyc8vLQl9bouvLcfPbmkcA3u5bebgC2aYogNm6OSo2mRhD5ZSMiUhkmo9Ih_NntORAE7Qeyf8NZVZpDWAng3QTKBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16162bd5bf.mp4?token=d1iLlDe9ZFT8aOjXBqmcWLBv63ugUtwhIGJjj5NtdV-5OiZQj8syraWnC6LWQc08BTVO8fhrmbHaanEJsf4jTayOQdJOkSdKVV3_kCU57OrtM7ljwtT3y1Rz9l_wXESNabLih2TPbpjaHOKW88zpD3ZTh8-eIIVS4bfo66jw4Exv5Z5tPARGY60A-YO5ABknzP-b-v33rIeX5dK7P1Jwi9Z8I49UOYkDa4BabihPg563qMC2LMZX8BMzM1ol_dyc8vLQl9bouvLcfPbmkcA3u5bebgC2aYogNm6OSo2mRhD5ZSMiUhkmo9Ih_NntORAE7Qeyf8NZVZpDWAng3QTKBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابونصر فارابی و «تفکر سیستماتیک و فرار از آنارشی»
#پادکست_کافئین
| فصل‌دو،قسمت‌سوم
☕️
متفکری که هزار و صد سال پیش، در دل آشوبِ خاورمیانه، ایستاد و چارت سازمانیِ یک تمدن توسعه‌یافته را کشید و به تاریخ نشان داد: «اگر نابغه‌ترین مهره‌ها را هم داشته باشی، بدونِ تفکر سیستماتیک، خروجیِ سازمانت چیزی جز یک آشفتگیِ مطلق نیست!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/C6Est5_k60c?si=3R0oBCMYwrbR7QfX
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/660681" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660680">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7lJy5dq8vj8mg5ypHDLCqfJwjOQK8RpuKqAYkVTMqnrYbl1h3FNsDPNCwHm3dmQuTYdZUgPvC8tgqOEKHmhj3dxRelTmTDQRzIhAOi7AtMFizMoiEH-LjRqI_7PeUxvPtItkKzrkOtxpBSu5gHqevxYyNwwT3YA-bxQE2s8tZe_TnGIswRNNi46OflZTSFMWCQ4k-VFKFT1KKFiwEHunJ0DGjslzPgpnOAW9SqKyKOld8dNsINTFJ7F9sxT4nfvUxmogicODbh6rSYrNybnPXxn4xnwX1GsILyszh8GzumLH-0Zq_XfaQBSgmGkFBmL39pkGWbyVlPvQwdQrJ9crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۸ خرداد ماه
۳ محرم ۱۴۴۷
۱۸ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/660680" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660679">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8pfN5WPERRgI3dxXzY0yK9ZfNzCwTUdBk60nDXpDGp7XKyAZ6tIGTdz-Q6dNtIJHnMBcny6uNGAB-Y0vJ5WBgjVifgtgpZUNcpNZJ7mLpqBAHtkqbqjLBx-nMREDGRZfxOXUYx-L9qUwaezcueQBn9A2m8VAamKtwHNJDbMa-7ydKUjiFJDas2WWF3X3OOwhFDZaDS2lkO-W407j5PN3HMeQD860UTgaUyA7ufjAi79U2PYL6lbKO2PxZKulSqQP6nYlyxmbO2uN6XcyzDVH1IISMPL8zOPTK6QfGhZPevIdQBCGg-P42mnqX9r_0z9AMOv21WnouNYBpcqgaqB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/660679" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660677">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بقائی دربارهٔ مرحلهٔ پیش‌روی تیم مذاکره‌کننده ایرانی: کار ما به عنوان دیپلمات‌، قطعاً از کار مدافعان وطن پای لانچرها و پشت سنگرها ساده‌تر نیست. شاید دشوارتر هم باشد، چون باید چشم در چشم دشمنانی بدوزیم که می‌دانیم مرتکب چه جنایاتی شدند و برای احقاق حق مردم و تثبیت دستاوردها با آنان مذاکره کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/660677" target="_blank">📅 01:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660676">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بقائی: مردم ما، بغضشان از غم فقدان عزیزانمان -از دانش‌آموزان تا رهبر شهیدمان- را، تبدیل به یک «خشم حماسی» برای دفاع از ایران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/660676" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660675">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
بقائی: ابرقدرت بودن ایران یک شعار نیست؛ ما دو قدرت اتمی را شکست دادیم
سخنگوی وزارت خارجه:
🔹
ایران ۲ قدرت اتمی که برخی کشورهای دیگر هم همراهی‌شان می‌کردند را شکست داد. ما شعار نمی‌دهیم بلکه واقعاً ابرقدرت هستیم.
🔹
جمهوری اسلامی ایران پوست ایران است و دشمنان می‌خواستند پوست ایران را بکنند. هر انسان وطن‌دوستی فهمید که این تفکیک (میان ایران و جمهوری اسلامی) تفکیک موهومی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/660675" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660674">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بقائی درباره تفاوت ایران امروز با ۶۰ روز پیش رو: لن یضروکم الی اذی و ان یقاتلوکم یولوکم الادبار ثم لا ینصرون
آن‌ها جز آزارهایی اندک به شما نمی‌توانند رساند واگر با شما پیکار کنند با عقب‌گردی، از شما روی برمی‌تابند و شکست می‌خورند، سپس یاری نخواهند شد
این وعده خداوند است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/660674" target="_blank">📅 01:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
بقائی: ما شعار نمی‌دهیم
🔹
ما با دو قدرت اتمی و بسیاری از دولت‌هایی که حمایتشان می‌کردند و هدفشان فروپاشی ایران بود، جنگیدیم و یک وجب از خاکمان را ندادیم. هر انسان وطن‌دوستی فهمید که تفکیک جمهوری اسلامی و ایران از یکدیگر موهوم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660673" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660672">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بقائی: احساس اقتداری که امروز تک تک ایرانیان دارند، بی‌سابقه است. جنگی که علیه ما به راه انداختند، ما را مقتدرتر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/660672" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660671">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بقائی: همه امید ما این است که همانطور که مردم در صدوده روز نشان دادند، در میدان ادامه دهند و به مسئولان خودشان اعتماد کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/660671" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بقایی: تازه ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت هستند
🔹
کار ما تمام نشده تازه در ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت و انگیزه بخشی از جانب مردم هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/660670" target="_blank">📅 01:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660669">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
🔹
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/660669" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660668">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بقائی، با اشاره به تجربهٔ برجام، دربارهٔ بند ۱۴ توافق اینطور توضیح داد: ما برای پذیرفته شده این تفاهم‌نامه از سوی بازیگران بین‌المللی، به یک قاب حقوقی نیاز داریم و آن، «قطعنامه شورای امنیت سازمان ملل» است
🔹
اما در عین حال، می‌دانیم که آمریکا به تعهدات بین‌المللی خود پایبند نیست. با این وجود، با استفاده از همان سازوکار خیلی از کشورها را مورد تهاجم و تحریم قرار داده.
ضمانت اجرای این تفاهم، قدرت ماست؛ اهرم‌هایی است که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/660668" target="_blank">📅 01:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بقائی: ضمانت اجرای این تفاهم قدرت ماست، اهرم‌هایی که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/660667" target="_blank">📅 01:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8KdIPQfg2ehomozqJHnvZ9wT941VUttoLppMEdxrx8cJX6rhtXhITRSxocRjKVVWpqO1SpsA0rx88sBwMhR00vSofGFquS6_1yMcmLP-D5-_OPPMDBeVdW2wju35kJB0Bt0DeTG3z55iBMUMW6Bc50C-zMoC71nZhwfWDWsAuipw4wvGetGH9UF_eISI5fs15Ha4ja5CYXlsU5eQmhjGghMFpX52JZ0L-tiGTI-FaTriSNb_pgLXe8jXxeXj2X5n6rRSGKcodkHDqPm7ojz5iEXJuXtXOBE-SaweqnV3WYgOZqpHBPRgd-UPk6si08_VOLExive167s4CaO9XHXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفلوئنسر آمریکایی؛ آنچه ایران به دست آورد
🔹
۳۰۰ میلیارد دلار
🔹
برداشته شدن تحریم‌ها
🔹
کنترل تنگه هرمز
🔹
حفظ برنامه موشکی
🔹
عدم تخریب برنامه هسته‌ای
🔹
آنچه ایالات متحده به دست آورد:
🔹
افزایش قیمت بنزین
🔹
میلیاردها دلار هزینه
🔹
عدم دستیابی به اهداف اصلی
🔹
آمریکایی‌های کشته‌شده
🔹
ما فریب خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660666" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اگر تعرضات اسرائیل در لبنان ادامه یابد، نقض تعهدات آمریکا محسوب می‌شود
بقایی، سخنگوی وزارت خارجه:
🔹
اگر تعرضات رژیم صهیونیستی به لبنان ادامه یابد، نقض تعهدات طرف مقابل در تفاهمنامه خواهد بود
🔹
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است.
🔹
رژیم صهیونیستی نمی‌خواهد کوچکترین فرصتی به هر روند دیپلماتیکی بدهد. اما این مسئولیت آمریکاست که رژیم صهیونیستی را وادار به احترام به تعهدات آمریکا به ایران در این سند کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/660665" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
