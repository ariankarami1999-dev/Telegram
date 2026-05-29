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
<img src="https://cdn4.telesco.pe/file/ibArnC4A7L1VTOkvFXxWu1Oj-0qth_PHX5DaSVZSeG35dnpi6WcXxs8SFDdLiw8GqK9wP4cKJVn0B2Bs_Q3EqOMz_vUvcsPMrotljWlHkSRL8I0x7Y6KBzqG7AYQ1sicIOI6cJEUbRv_NMCRnjUaZi7kgHtYmibVi0N705nl2XhmqBZJXDJr5hYWh5PiZD3IGR7Doj5C3lsybl2Voi2hDmWtFTbRbSVv09Wf3pvIyGBFDyTSAIq7TBTsY6wxmmQfm5Gv5oe8ktyEtA6R_92siaipxJ7tbptPkiBRvNt7qZn-uqinR5MDkKW5OfJcax0R_FIkLUPkq5So1e3U3G0HXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-654695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1PgebOQTUlQ5sczuJqozh2fp3LRX4BXesTzXAKggsrxMmrMbHw3O0CzetAacDWdkr2ZgVZeyfBYAML9neRfUNd4vcHZC7SQEWgEGfTjp8mpmxyNOk3i-GiSRG6l84HNrzBHl7Hfpz_0mlITG4Rr9DSFFA5AUSMrV5Eb1WBtedVPo4m6Pb2hc0qIRxGCHO9T6yBzBuvgkoWFVZPtJoNtgru2d2ulPc1kwQFQkbl1n9dohZiJKb56xrxykpfeP1F6Fft04xvjDwXcsGp7M-GV8mvwhII-w6_Eg1QSzVhgF9qs74NxzFmHo40ruSLKnORg_1bLEAWTjSp0X2yT2iqTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی دوستانه| گل سوم ایران توسط مهدی طارمی
🔹
گامبیا ۱ــ ۳ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/654695" target="_blank">📅 20:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osbbJEU_sMB-pfhsg7aquctx8RnOqISF2aRXpdWFaacXkjYydrBpiNACcQq-ihQvPjBnZnPthL1X4zypj0NLIXSUM6S9w4XlDip-lvTStJuEEdGkqS1qHeGyZiV2VfISx-qpifUAdVy3ZjlIY3Q4PZj5CLgE_5B-rP3hxwYjhTgatkd5xFwcaxrQd5r4Q9DkwgamuoFKfW7NMePjJOniq1RSLOANE24xLJdpKxRaRKt3zLXfcRn3KowxqGQ3yJyyp7Lx_c3MDXzaUbz9RGn8kr_nlplHvwyiPSoJwXclLIYS3hACyXrkqnYbLVctU_sFKF0WacctDN05n5iqcsKm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تاکنون تفاهمی با آمریکا نهایی نشده است  بقایی درباره ادعای از بین بردن مواد هسته‌ای توسط ترامپ:
🔹
در این مرحله تمرکز ما بر خاتمه جنگ هست و درباره جزییات غنی سازی و اورانیوم غنی شده، صحبتی نداریم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/654694" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ترامپ خواسته‌های خود را فهرست کرد  ترامپ مدعی شد:
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد آزاد کشتی‌ها در هر دو جهت، بدون هیچ عوارضی، باز شود. تمام مین‌های آبی (بمب‌ها)، در صورت وجود، منهدم خواهند…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/654693" target="_blank">📅 20:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwzMxp8WbPiFdOai-LknuMsxQruoTcOvUQ0gJMmTpAM_ucWnQ9B8_x86oG6jeiaikmgq6wUCt4shglQwpHPa5JG3IcKlHDW4Vf7YmpOxlXajdAAl78EynTXUS2YU5rNy6bFOMRM6voe-XHwn-oI2KU_x8bMP7hXhmcbstHGhZM_G58DUE9X_GTm1WosvbLQOQ7W4r8lA-8pqgzEVbl8U6N5Q_3jEPHLoAK7VHwEPOVFsg1hmYbmDKF_I0piuae4jhoetSxAubbnU95z_M0b-uRh6XTgInjtCtuUN_NwEM_zbUb7WQhX_bAW4K_KzutBoNXtlPFsbjG9MaV6LklNMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه رکود در بازار مسکن تهران؛ معاملات به زیر ۴۰۰۰ سقوط کرد
🔹
بازار مسکن پایتخت با شدیدترین رکود تاریخ خود مواجه شده است. میانگین معاملات ماهانه که در دهه ۹۰ بیش از ۱۴ هزار فقره بود، حالا به زیر ۴۰۰۰ رسیده است. یعنی بازار مسکن تهران فقط ۳۵ تا ۴۰ درصد توان طبیعی خود کار می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/654692" target="_blank">📅 20:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پیشنهاد گروسی: قزاقستان اورانیوم غنی‌شده ایران را نگهداری کند  مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
قزاقستان آماده است در صورت توافق ایران و آمریکا، ذخایر اورانیوم غنی‌شده ایران را در بانک بین‌المللی اورانیوم خود ذخیره کند.
🔹
«ما محلی داریم که این [اورانیوم…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/654691" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رد و بدل پیام‌ها ادامه دارد  واکنش بقایی به ترامپ:
🔹
ما از ۴۷ سال پیش خداحافظی کردیم و دیگر بر اساس بایدهای دیگران عمل نمی‌کنیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/654690" target="_blank">📅 20:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db29ecf26.mp4?token=QjPgzzXNpReBfyJOkMC0D9k9ejWAQzAW_urXs8G1RST9kidjUQnr0a6Zn6BzVzx7yszKY-7nvapx8TYwr9tPSPXDZHT0wJnZ116kxSW4uEgQYdqCdfmCpKnPf4YP_hXxY4H2S5yU9L-ofopyffy1vRxxgPVfZ4bA--HCZ3xYyv_PCoDfq9fIP5a-vQsxjb35udXwywjLLunlubg6jgiVjoZ1pAQzYtu_OgoW3yWzFdomiDZKMTYbLwaoQseQP-f8Vki4jebjr9_MAMVOXv9Rh4wPWtTjo40AbI3gRLauPtV2eEHABnHwA5h2j1D9w-RIJkWntnyoMi7GA-I9q7-_rTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db29ecf26.mp4?token=QjPgzzXNpReBfyJOkMC0D9k9ejWAQzAW_urXs8G1RST9kidjUQnr0a6Zn6BzVzx7yszKY-7nvapx8TYwr9tPSPXDZHT0wJnZ116kxSW4uEgQYdqCdfmCpKnPf4YP_hXxY4H2S5yU9L-ofopyffy1vRxxgPVfZ4bA--HCZ3xYyv_PCoDfq9fIP5a-vQsxjb35udXwywjLLunlubg6jgiVjoZ1pAQzYtu_OgoW3yWzFdomiDZKMTYbLwaoQseQP-f8Vki4jebjr9_MAMVOXv9Rh4wPWtTjo40AbI3gRLauPtV2eEHABnHwA5h2j1D9w-RIJkWntnyoMi7GA-I9q7-_rTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داغ‌ترین خبرهای حوزه فناوری؛ رقابت غول‌های تکنولوژی جدی‌تر شد
🔹
گوگل و اپل چه در سر دارند؟
با هوش‌ مصنوعی ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/654689" target="_blank">📅 20:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654688">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
الجزیره: ممکن است همه چیز برای اعلام رسمی توافق آماده باشد  نورالدین الدغیر خبرنگار الجزیره در تهران:
🔹
ممکن است همه چیز برای اعلام رسمی توافق آماده باشد، با وجود برخی اختلاف‌نظرها بین تهران و واشنگتن در پرونده‌هایی که در مسیر حل شدن هستند، و احتمالاً مشکل…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/akhbarefori/654688" target="_blank">📅 20:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654687">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بازی دوستانه| گل دوم ایران به تیم ملی گامبیا روی شلیک رامین رضاییان
🔹
گامبیا ۱ــ ۲ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/654687" target="_blank">📅 20:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654686">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تشکیل ستاد برای برگزاری مراسم تشییع رهبر شهید انقلاب
رئیس شورای هماهنگی تبلیغات اسلامی استان تهران:
🔹
ستاد ویژه‌‌ای برای آماده‌سازی شرایط یک تشییع ده‌ها میلیونی برای قائد شهید امت تشکیل شده و مجموعه‌های مختلف در حال انجام هماهنگی‌ها برای برگزاری باشکوه این مراسم در موعدی که مشخص خواهد شد، هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654686" target="_blank">📅 20:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654685">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrU675l8EMELEbWeMOtmGoA7AneFM-L0pvKQhhcNMp1NBNYeM20IiMoce0S1sV-vAVGqs942hblF_-w4niwUvc_-hPVAeSlUUNWbiWCVxGIcB8sra3W7jNBqz6nWRIu8NtCN2XVmFF3J_K_bjoT51RoUrFEVoGRbVIwYcgOynAr2-TqFdweSFvUdvpbVcsU1b9XbYZL7dmOTOeVd6V7teYFMVOQ4XiIoqQAyAl1-9I1gk2lIjF2t1ao1sS89Ds6FisGuYYEsklDDLc_dp0Ltw_TTBAwc2tY6aatM6HBmmV8xdy_0EI5g0SMyXJ1xe3aaYqURFa0wyk2lvsaomLReJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر هوایی از برگزاری مراسم روز عرفه در گلزار شهدای دانش آموزان مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/654685" target="_blank">📅 20:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654684">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57c518d9c.mp4?token=NfnFfibZyUD3aIi7hy68yTa4kqgUZEY5BQApS2k7clnbs2vY6fuwzb2KI43_CC1OSYims2qUQ3hSVEypmKXH7QIjtdbjHe3LriMgbvC7y1mVgh880izZVtEKXX03XAsqWxcNc_CMtjFqP-dRYB6O1NzUJjzbaq_5fRkGkKGtVOdKcDPTjaEB49nsC-OYmpCDGKCFWyXO4XxzW07c8e-kbGnVE2rHD_FAJklqPDD9YmBlV3nUdKD4-wmN4t7fK2RfIviPbH8WIBvO-ciyfQN2tJFwawFfNls8IJ_poRkoZIL0KGToB76TqLDSxdBf6ILCLuwHm1t3Yr9-oRKuFKK06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57c518d9c.mp4?token=NfnFfibZyUD3aIi7hy68yTa4kqgUZEY5BQApS2k7clnbs2vY6fuwzb2KI43_CC1OSYims2qUQ3hSVEypmKXH7QIjtdbjHe3LriMgbvC7y1mVgh880izZVtEKXX03XAsqWxcNc_CMtjFqP-dRYB6O1NzUJjzbaq_5fRkGkKGtVOdKcDPTjaEB49nsC-OYmpCDGKCFWyXO4XxzW07c8e-kbGnVE2rHD_FAJklqPDD9YmBlV3nUdKD4-wmN4t7fK2RfIviPbH8WIBvO-ciyfQN2tJFwawFfNls8IJ_poRkoZIL0KGToB76TqLDSxdBf6ILCLuwHm1t3Yr9-oRKuFKK06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی دوستانه| گل تساوی ایران به تیم ملی گامبیا توسط آریا یوسفی
🔹
گامبیا ۱ــ ۱ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/654684" target="_blank">📅 20:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654683">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
الجزیره: پست ترامپ درباره رفع محاصره بنادر، شرط نخست ایران پیش از مذاکره هسته‌ای بود   یک منبع مطلع به خبرنگار الجزیره:
🔹
ایران بر اعلام رسمی و عمومی این موضوع پافشاری کرده و آن را گامی کلیدی برای ایجاد اعتماد می‌داند، در حالی که ترامپ آن را فرعی قلمداد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/654683" target="_blank">📅 20:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654682">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
الجزیره: پست ترامپ درباره رفع محاصره بنادر، شرط نخست ایران پیش از مذاکره هسته‌ای بود   یک منبع مطلع به خبرنگار الجزیره:
🔹
ایران بر اعلام رسمی و عمومی این موضوع پافشاری کرده و آن را گامی کلیدی برای ایجاد اعتماد می‌داند، در حالی که ترامپ آن را فرعی قلمداد…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654682" target="_blank">📅 20:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654681">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743207010.mp4?token=V3Uk5g3qcN9qULgFCBg66T8cts25X0VoQ43HIFYzuY7RU0bvVzVE5E7SW1fOKCMNgeVYNLfNfV1Tunr6FGQqr86XvcCojEaw3EiXFzFuhHGOdWCK8vzLXzgoZCNJtCU47AzTQ5zIWdQ2GmsvlyhXF-XhQFYGkqFfnxnQnAfx88h_NZwO2aVfDgfU0e7SEABH8JUTaQEeMNqcws5onZSuVMWcbmm20jJ5x6kGfGW8_h2VsbPt-ZQ2U1-Qd3ux4QetcXv0wO-OQTfJvfa-8rRsOiW6HeVkgBX-DqTXXkQAdwpDnCfHXmCFACkdhSKwVfhWLXvgTj19wZ4Nwv6gsmtd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743207010.mp4?token=V3Uk5g3qcN9qULgFCBg66T8cts25X0VoQ43HIFYzuY7RU0bvVzVE5E7SW1fOKCMNgeVYNLfNfV1Tunr6FGQqr86XvcCojEaw3EiXFzFuhHGOdWCK8vzLXzgoZCNJtCU47AzTQ5zIWdQ2GmsvlyhXF-XhQFYGkqFfnxnQnAfx88h_NZwO2aVfDgfU0e7SEABH8JUTaQEeMNqcws5onZSuVMWcbmm20jJ5x6kGfGW8_h2VsbPt-ZQ2U1-Qd3ux4QetcXv0wO-OQTfJvfa-8rRsOiW6HeVkgBX-DqTXXkQAdwpDnCfHXmCFACkdhSKwVfhWLXvgTj19wZ4Nwv6gsmtd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی دوستانه| گل اول تیم ملی گامبیا به ایران در دقیقه ۴۲
🔹
گامبیا ۱ــ ۰ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654681" target="_blank">📅 20:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654680">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عراقچی: توافق نهایی منوط به کنار گذاشتن خواسته‌های زیاده‌خواهانه و مواضع متناقض آمریکاست‌
عراقچی در گفت‌وگو وزیر خارجهٔ عمان:
🔹
ایران در پیگیری حقوق حقه و منافع مشروع خود جدی و ثابت‌قدم است‌.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654680" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTX6Ruws-_L88imeAxxuqfoyDvGkFHEl_7ffpRyHceO_Vz5Vog7Cg6WWepEfn2tAo7gHSNYeWHxar2wj50-AF8hrG5rxzqkt8x7LbTzK-6FYe_7qETOt_oBiMIpT5exc4DY7iceZNKoz11gb0TxWEJSImW711E6TCVg5ZQYuyFBLWZeiUtHkEfJM_atHWVZfwwNrw3ibiklSfKInzQBT8rye0x1_RJgSqKwHxhvGOkLB9i_ErjMgQnsaAeOBj7XiN9CNhSmckmQJeCC4zZN5c1z6URuftwtbuEGfXeynlut-MJWfUyWf3qHmMt8aBkc3mS5BrESErwSBDfQLl0vq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد گروسی: قزاقستان اورانیوم غنی‌شده ایران را نگهداری کند
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
قزاقستان آماده است در صورت توافق ایران و آمریکا، ذخایر اورانیوم غنی‌شده ایران را در بانک بین‌المللی اورانیوم خود ذخیره کند.
🔹
«ما محلی داریم که این [اورانیوم غنی‌شده ایران] می‌تواند با خیال راحت در آن ذخیره شود»، پیشنهادی که به اعتقاد او هم ایران و هم آمریکا می‌توانند آن را بپذیرند. / انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654679" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea1186453.mp4?token=v7ekAoiKP_Yt2sD-J0jYc7c0jRiVBnA6bEkzkFY4EZt2C4F3e58QJkjvM8stlmjRXQlMpCUYjSzVIbSwD0yhvCiyfBmB2eyIaGH3KnPE95y7L85sTy9IAPWJRbmpYGecNbRxerucfNKjDZq5c9Pv3FTgEHZpEe44yTcgqD_LMYK7leZLrhU9zDA_Dn8SoNi6zOFceD5bitYcoYfHhLwzKsDAQtHoPYotUiV9ymoE_r1IYlWFz0JzWBXpUNJwFRWvBxCewpbIFW529iRbr16iVhwtt4LADrLEZwl53G-2OQZQ9jz_rvtTfKnVunASlxvaPm-RS1Ctim6uGCnH955paQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea1186453.mp4?token=v7ekAoiKP_Yt2sD-J0jYc7c0jRiVBnA6bEkzkFY4EZt2C4F3e58QJkjvM8stlmjRXQlMpCUYjSzVIbSwD0yhvCiyfBmB2eyIaGH3KnPE95y7L85sTy9IAPWJRbmpYGecNbRxerucfNKjDZq5c9Pv3FTgEHZpEe44yTcgqD_LMYK7leZLrhU9zDA_Dn8SoNi6zOFceD5bitYcoYfHhLwzKsDAQtHoPYotUiV9ymoE_r1IYlWFz0JzWBXpUNJwFRWvBxCewpbIFW529iRbr16iVhwtt4LADrLEZwl53G-2OQZQ9jz_rvtTfKnVunASlxvaPm-RS1Ctim6uGCnH955paQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی دوستانه| گل اول تیم ملی گامبیا به ایران در دقیقه ۴۲
🔹
گامبیا ۱ــ ۰ ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/654678" target="_blank">📅 19:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رئیس‌جمهور بلاروس: در صورت تجاوز به بلاروس از سلاح هسته‌ای استفاده خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/654677" target="_blank">📅 19:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ترامپ خواسته‌های خود را فهرست کرد  ترامپ مدعی شد:
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد آزاد کشتی‌ها در هر دو جهت، بدون هیچ عوارضی، باز شود. تمام مین‌های آبی (بمب‌ها)، در صورت وجود، منهدم خواهند…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/654676" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654675">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ما از ایران در مورد مواد هسته‌ای و مهم‌تر از آن، آنچه در مذاکرات بر سر آن توافق شده است، تضمین‌های شفاهی دریافت کرده‌ایم
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/654675" target="_blank">📅 19:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654674">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ما از ایران در مورد مواد هسته‌ای و مهم‌تر از آن، آنچه در مذاکرات بر سر آن توافق شده است، تضمین‌های شفاهی دریافت کرده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/654674" target="_blank">📅 19:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654673">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkuQxsz3glG1nibg3gYhTzbQo97Gnk1fXne_VKerMQTLy7d1T_yNauvgeS5jMhwaPxLQG3nJzhgLY8Rwf9Zgc38X_TZhoO5MIy4SHyhKXQOox437Xc-xX2LRorOnPBTD273juYxfx4q210Ejw1l_FCT26rkD3Nax5pHmbddiYF8Crkz1de8O4_gqJUmdqzp_Ve710O54frjsiayLPtLchFUwLXPuL-TbUaZV6ansnqkAbV9uhFyUjX4_jUrI06ECSKYP668OeRGeqgLbF_Bu_Lcjn3atrWIf_vD4IjdHDUI3oIIAQ_wg8KZBLf0_j1FvJGiM97Dlt59CIRdI21v_KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر کاهشی شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/654673" target="_blank">📅 19:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654672">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ترامپ خواسته‌های خود را فهرست کرد  ترامپ مدعی شد:
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد آزاد کشتی‌ها در هر دو جهت، بدون هیچ عوارضی، باز شود. تمام مین‌های آبی (بمب‌ها)، در صورت وجود، منهدم خواهند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654672" target="_blank">📅 19:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNsmJI1H0pckr3KOf5Nj6glPTVqQhvElCOEUuk-n6KMMlMmuX40drtRq3VG1vfY1L3MwAWLDsXIwMpQ-VrTflzPOj_qQhx-x1eH_Na5MegMiUVVkKFp0qPtta0hIPfj_DilVC1zIMwf70SR0g_7lngFTLWVDHndT4QZ8XJ3jaj6GpE9rQ1aziDtHM3_hqFI8Z7Fyrxo_F_WQChrecjM1MnvhoSI3ngelzlOSjh18d1y9nwgxaVypuqDS_66BCpwDKsuo1E_WC5AXa0mWmZhYfIVCwr6GD5McdlKChcE4qeFKwQewCBjFOxxyOBh0X_aPfRKV1f8v1Fu80isisI0l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی ادعاهای ترامپ قیمت نفت به ۹۱.۴۸ دلار کاهش یافت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/654671" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c4690ec8.mp4?token=gWtuQxLkQ0losSVu5LvIVD9MsaJKtLfOGnnYIRUlNrdFtPz1oIPJhg1_giFd5SFfM_Yi0xbnY-sz-bCs0Nq394bsi5QdSKK7NwS4z5iiDJo6XdfUJs41paKcFs3rF4rFbePiQcPGberM-LQ2aYkKABlg7J_y6aBoO7fe-64TElZt4c3GEJr-CGq-A1h5PPxigB8gksHtCN-nXteT4s_ZXAVpYJLvfmlmDz0ggOeECT6QOP-SpJyiVQi6fo1J5H5wOtVhvEvu1FtRok996onHcCKrS5QqnWadzLDKKEhpG_VmEN3dsNnLKqe5Z-LWm27srHw0l4GNB-QgwfsTJHKNwifd_F6qq_F9DQXnpjyFvJvUqRcXw66BRTSkz54T1VCq0gRnGauzHxbMlaBm_3qZgZQ3bSfKSYMuLFbzst2GpyF2z59V6yJmJgsSPg6SC2DOEAMRC42i5P9sCAx6R5h4IrXjIfnOu6djj8M3rqfhoBccBqKL8giE8UR3hhanU365mwwdkilxZsiKCnLE98H_1o0GMNq-0KjeUOkBMuhwtmEkZnWVuhZ0dVRZJOa6a12Yk8Kqrkmgd-BIl0upJkJQpPJSVzNjSWZ90c8Ta-XfQ-w5llV4slhvtObot1t3MDFuY4gKoP8h-JWKJvP9vOBHKQInCYmKyAe4ozpU3lR81RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c4690ec8.mp4?token=gWtuQxLkQ0losSVu5LvIVD9MsaJKtLfOGnnYIRUlNrdFtPz1oIPJhg1_giFd5SFfM_Yi0xbnY-sz-bCs0Nq394bsi5QdSKK7NwS4z5iiDJo6XdfUJs41paKcFs3rF4rFbePiQcPGberM-LQ2aYkKABlg7J_y6aBoO7fe-64TElZt4c3GEJr-CGq-A1h5PPxigB8gksHtCN-nXteT4s_ZXAVpYJLvfmlmDz0ggOeECT6QOP-SpJyiVQi6fo1J5H5wOtVhvEvu1FtRok996onHcCKrS5QqnWadzLDKKEhpG_VmEN3dsNnLKqe5Z-LWm27srHw0l4GNB-QgwfsTJHKNwifd_F6qq_F9DQXnpjyFvJvUqRcXw66BRTSkz54T1VCq0gRnGauzHxbMlaBm_3qZgZQ3bSfKSYMuLFbzst2GpyF2z59V6yJmJgsSPg6SC2DOEAMRC42i5P9sCAx6R5h4IrXjIfnOu6djj8M3rqfhoBccBqKL8giE8UR3hhanU365mwwdkilxZsiKCnLE98H_1o0GMNq-0KjeUOkBMuhwtmEkZnWVuhZ0dVRZJOa6a12Yk8Kqrkmgd-BIl0upJkJQpPJSVzNjSWZ90c8Ta-XfQ-w5llV4slhvtObot1t3MDFuY4gKoP8h-JWKJvP9vOBHKQInCYmKyAe4ozpU3lR81RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبیه‌سازی مفهومی در نیروگاه قدیمی آبشار نیاگارا؛ اجرای صاعقه‌وار AC/DC با کویل تسلا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/654670" target="_blank">📅 18:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی اعجاب‌آور وزارت نیرو به نیروگاه‌های خصوصی؛ ۲۳۰ همت!
مصطفی رجبی، معاون وزیر نیرو در
#گفتگو
با خبرفوری:
🔹
مهم‌ترین چالش اساسی صنعت برق این است که به لحاظ اقتصادی و درآمدی پایداری لازم را ندارد و کار سختی در تامین سرمایه دارد. در حال حاضر مطالبات نیروگاه‌های خصوصی از وزارت نیرو بیش از ۲۳۰ همت است.
🔹
بخشی از این مطالبات به حوزه نیروگاه‌های خصوصی و تولید برق، بخشی به مطالبات بانک‌ها از صنعت برق و بخشی به پیمانکاران و تامین‌کنندگان تجهیزات برمی‌گردد؛ به خصوص در حوزه انتقال و توزیع.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654669" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKeMKjOZyVY7roizhbNWCgZZ9E2DSo_qcXjUpwkwRa1pjHNzEDpxyKBtrmQ0-LE-BDRNNS1N3gg_zYmuEqyvDDRq9AKNy9iKBBbE-bKBPULyVeTLdGACQw_CONr2FJ9pIvd_EXGaU1fFWbMOUQZXZ3BKBcfSfitKdBD4WoqQJVA6tG1dl2mxUZUFtFgx9amloc77GZ3wkQ6GwpUWt6e_fE8D5OZl-Tw3OQUUByZ3QcZ8DZ9-_b-v_OC1ExDkGk0mcK4HMHYBztFT4F7UZ7PDmu30EYk3tQkmTAAxSzUhGEbmv8h1hLHcriDGmQr_VO6duvYGsdBKEPfZvBUlwRP3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد ادعا کرد: در حال اتخاذ تصمیم نهایی درباره ایران هستیم #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654668" target="_blank">📅 18:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ترامپ مدعی شد: محاصره دریایی ایران از همین حالا برداشته خواهد شد #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/654667" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ مدعی شد: محاصره دریایی ایران از همین حالا برداشته خواهد شد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654666" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نماهنگ “ایرانی پیروز میدانی”
🔹
كربلايى حسين طاهرى
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654665" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYCGvHN_R1EuTJmzK8sfTikuPfDaTmyVZ9ehK5_TWZWPRZ3YwkX5LCTCGarQ73ltrnI2Ik_26pmyFOsCUG4793EXG0gEfcF6-c_GaDv7ZrXLbRaPn2gDXEScWCcT-sm20hWatuci951zbj3yprkivMVdTVA_31pJlPVDgC0rOLCGM9dHPtS2hdZW35Sb4HKb6ZjCtWiQnFxnHmXCqOxmJkOJGTn1ZeYkYaaqDcBdBuFXwKvNVYd86_zP_vBco2J6FEQC2FkI8IXnf6mRcEY8uFHuWYHev_SalG9VDgePacmTLT6rCsgc7WHThGigWRWa4AC0KTXRQBDputMq9PjJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم فوتبال ایران مقابل گامبیا در دیدار دوستانه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654664" target="_blank">📅 18:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654663">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای سنت‌کام درباره تغییر مسیر ۱۱۵ کشتی
🔹
سازمان تروریستی سنت‌کام در بیانیه‌ای گفته که محاصره علیه ایران ادامه دارد و در همین راستا تا کنون مسیر ۱۱۵ کشتی تغییر داده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654663" target="_blank">📅 18:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654662">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ورود وزیر خارجه پاکستان به واشنگتن
🔹
محمد اسحاق دار وزیر امور خارجه پاکستان قرار است امروز با همتای آمریکایی خود و مشاور امنیت ملی ایالات متحده دیدار و درباره مسائل دوجانبه و منطقه‌ای رایزنی کند.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654662" target="_blank">📅 18:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b55812279.mp4?token=hCtVrZpv8onZtedJF6xgiQVak5S3M_FWsMBFzeTfLI6KzX7uTv6Nz0NZsFGQRy64Dnuax7vDXyUy7A63FBmGBd3TmX_v_kaEVsFw9ftXByj7odPo5bPKrpCWnB0y_6IaWoqEmvWPXw53b-OFfdy2FQzaC1-5twhfilfEZX-MUJM3cdXj7HRRQ-mMWUASvsCedNEA2hER5Zp0iwt2yriapglIsUbUq1Q2JGMlzwe_uvy4HPPgi-fRU6BnQ4w79y8MSCsDS3Rw9Cb9Zlg27LZtF7aXBkkxs-ZkD9aHw5pD1C5aXmz7yxoiFV_N5gHiNdGKYiBUsbweJ8Q1g2KvGPO9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b55812279.mp4?token=hCtVrZpv8onZtedJF6xgiQVak5S3M_FWsMBFzeTfLI6KzX7uTv6Nz0NZsFGQRy64Dnuax7vDXyUy7A63FBmGBd3TmX_v_kaEVsFw9ftXByj7odPo5bPKrpCWnB0y_6IaWoqEmvWPXw53b-OFfdy2FQzaC1-5twhfilfEZX-MUJM3cdXj7HRRQ-mMWUASvsCedNEA2hER5Zp0iwt2yriapglIsUbUq1Q2JGMlzwe_uvy4HPPgi-fRU6BnQ4w79y8MSCsDS3Rw9Cb9Zlg27LZtF7aXBkkxs-ZkD9aHw5pD1C5aXmz7yxoiFV_N5gHiNdGKYiBUsbweJ8Q1g2KvGPO9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عواقب درگیری دوباره ایران و آمریکا؛ ۵۰۰ میلیارد دلار خاکستر شد
🔹
با تشدید تنش‌های نظامی آمریکا و ایران در چند شب اخیر، بازارهای سهام آسیا قتل‌عام شدند و موجب ترس سرمایه‌گذاران آسیایی‌ شد.
🔹
طی ساعاتی، نزدیک به ۵۰۰ میلیارد دلار از ارزش بازار ژاپن، کره جنوبی و تایوان ناپدید شد. کره جنوبی ۲۴۵ تریلیون وون، ژاپن ۱۷.۳ تریلیون ین و تایوان ۶.۴ تریلیون دلار تایوان  را از دست دادند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/654660" target="_blank">📅 17:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654659">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl1X1DB7OoQlsiZAAYJqwOC3Tw0q8xiu5BvMzrQGkn8zw4pSgthOLmLnsJSMlrGJ2KLlWQveQbyX7kNUuXckYeqfkj_g8-zFWRVzGnPPRV22K8nmzv6yLsq0jUn_UvwLTwYWqS08IZfC4SA76tUZu_gDZi2rkuJCYQ7CuEMSLtKIDXazsRHComjlAvbsVPwFdu_P2PwPmnDUvp-LIls6BasJCAxmXe-vaSCoJEH6pOJNQkkR3ziC--6CCgNpywHroAqr3ubmoCrzAZezmy9dcffkH3cJRT_AgUfF-QtmpOHCHnJFdReA0LAmcIypOF3fbbIFij68OryPGYD0qzjw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با برگزاری مجلس یادبود شهدای خانواده امام شهید و رهبر معظم انقلاب اسلامی، ختم مشترک قرآن کریم به نیت شادی روح آن عزیزان برگزار می‌گردد.
دعوتید برای مشارکت در این ختم معنوی از طریق آدرس زیر:
urls.st/khatmq3</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/654659" target="_blank">📅 17:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_F029_f7EBMinS9oRdiJQ1gXdVpyHwGRxmSpVkhYjYkrw0TiEa78qEpz-QTkLPZ7i07Dd8aa5A7-nrwXS20cIeh1KcvJ9hiX7a5WxooaL2obPTo1cy6DjNaysfnm6u5HePAbUMg-Kow53EUvCoNF3dDVInqJ80isDQv3B-ApO60BlMTOVtZ9dykUR2O-5nlUI9VNc-FxEKnPNxJ-c9JdIjcz7lXaZcQ_9ceXGtHqjs_juK99ihOsHq4z1rCAvMICPrW1_fWRfNSh2U_PZZEjskoMYD9sM3VC_5u0wUVFROLjHdW5kX58ixOs1ZzyS2iuSTfrK4tdhpamIC48LMwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار مطرح آمریکایی: ما توسط احمق‌های شرور اداره می‌شویم  آرون روپار، خبرنگار مطرح آمریکایی:
🔹
قابل توجه است که وزارت امور خارجه تهدید دیوانه‌وار ترامپ مبنی بر منفجر کردن [عمان] یکی از وفادارترین متحدان ما در خاورمیانه را بزرگنمایی می‌کند. ما توسط احمق‌های…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/654657" target="_blank">📅 17:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بالاخره تلفات اسرائیل افشا شد؛ ۶۴۷۶ خانه اسرائیلی در جنگ با ایران از بین رفت
جروزالم‌پست:
🔹
فرماندهی پدافند غیرعامل ارتش اسرائیل اعلام کرد در جنگ با ایران ۶۴۷۳ واحد مسکونی در اسرائیل تخریب شده؛ همچنین بیش از ۷۵۰۰ نفر در طول درگیری به بیمارستان منتقل یا بستری شده‌اند.
🔹
طبق اعلام ارتش اسرائیل، در جبهه داخلی ۶۸۳ نفر زخمی شده‌اند که شامل ۲۲ نفر با جراحات شدید، ۴۶ نفر متوسط و ۶۱۵ نفر سطحی است. همچنین تا زمان برقراری آتش‌بس، ۲۴ نفر کشته شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/654656" target="_blank">📅 17:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaaddf8487.mp4?token=CU8nUmi5ixHFiUA-JMC2xlSvfd448wuiC4Z2qoiXmAyyMf0-IGo1NRqXbnvvrDw6HZGKRnLm_Vhw-NpPanO-Gp8CGmVuy9pY2aaSa1PvTSickYlQB57ufP9uR_OxSpZaeTEBjGTrcOZQaiBZN_2N7Y9g-Hxo5oZCjreadgL0sNgl6CNkdnhpJy10vP7eEwgPk3UH9qiFnrye-eVJ2XAHpKK9a49IF0QOdqVy1kKcklwalHl7eMaFkMDK7OSjbX5VOhaEN1QSZ_qe9dNFWTH5EhrW-MECEm_42ED43WC18yeYF50m-6GbW-9ZFAYHymOGFluRoUNvc4-fojJGRhXnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaaddf8487.mp4?token=CU8nUmi5ixHFiUA-JMC2xlSvfd448wuiC4Z2qoiXmAyyMf0-IGo1NRqXbnvvrDw6HZGKRnLm_Vhw-NpPanO-Gp8CGmVuy9pY2aaSa1PvTSickYlQB57ufP9uR_OxSpZaeTEBjGTrcOZQaiBZN_2N7Y9g-Hxo5oZCjreadgL0sNgl6CNkdnhpJy10vP7eEwgPk3UH9qiFnrye-eVJ2XAHpKK9a49IF0QOdqVy1kKcklwalHl7eMaFkMDK7OSjbX5VOhaEN1QSZ_qe9dNFWTH5EhrW-MECEm_42ED43WC18yeYF50m-6GbW-9ZFAYHymOGFluRoUNvc4-fojJGRhXnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوپرگل شگفت انگیز عثمان دمبله به عنوان بهترین گل فصل لیگ فرانسه انتخاب شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/654655" target="_blank">📅 17:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcVoFEHBhUAoKTVS72Tw93-o4bL2NbKTY1ln0O6h5bxWxnSm_XC1YS1OK2kqkv_AkPBHPCks_hRkK-OkaFH18UP8qGbixUe5g4B14xbZgdDKej_X4lYhZsWyhsk-40LMupxmTRChFW4zWeSyo3cbZg8cRDA_UqsENiwvsMNwsVfdZIAXxo7A5UThCh0YUZjdL86O-17r1Wrdj2_X2T0YevmUjnSIVMt2wfe-DMffon9WDvBWHROkNHXnBEklT5ELGGJ4iDbe8WlNMAK34SjkRdxcICidpJAI4h5jEuJ30kSj7ltAjWEhS_WT-lnQqjrm4RX5bYvXFaMKbLozObYHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: پول نقطه کور مذاکرات ایران و ترامپ شد
/
تهران کوتاه نمی‌آید
نیویورک‌تایمز:
🔹
ایران شرط آغاز هرگونه مذاکره معنادار با دولت ترامپ را آزادسازی میلیاردها دلار از دارایی‌های مسدود شده خود اعلام کرده است.
🔹
تهران از یک شرط کوتاه نیامده؛ بدون دسترسی به این وجوه در بانک‌های خارجی، گفت‌وگویی شکل نخواهد گرفت. موضوعی که به «نقطه کور» توافق احتمالی تبدیل شده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/654654" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/654652" target="_blank">📅 16:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edce9e0728.mp4?token=BH9QJL_7uBZs24PqRe_rU02NwiURvwShoztXJ-8d5J9lYZrR9zT84ufFB-NApyWLXBlnY8rEzgoLpTapDJfjRUJ5vhJp2pl7abYuzo0OB2NM14NuMaBVUvHUwd5g28gYFA5yufInoWJMgq1j-HrPEmBPqaIg729svk480CyBJn6IytcvFG6sx9Bebzivo93sPpaW83-7Br-xpQSI1cWFrA1tydJYnwYJkr5T8_2ELSfvghJ_TC9mlSdXmowuLV4kfDIQFSzerNY1XGalaPkh8ESoQJsb741RnJ5ekcm36C6YWgy4gd6e_-ElKJApDRPns6OELpMFQdPK3aMPXsAFmX9K4cAFC22J8_mWwdhsePgUfv39PcCFJjxDVX2b6owyZi6xUDAgdbAY3Sx8v20fLo--_ogFcKQRi5sioNIB-RrthlCP6IIfgcrhth0a8tYe6nsP4RbcYzU0bZWOoieMC0pg78KK0DNtkc9qlUr8Acn0kbHFjv4wDz7HAeSUTdowwSSgQ7W5XpuqahopwjQMU0nzAnmmJ_rvFDgQ6QdjypPnwJt-aHb_8ISrXeucFDgxZ2nlQJteNGiR5ENWbK7Tq04Ps3qI8Q0bhKDnbFCLU9sY5DGJRV1Bc_dUhKNkSt-_-6guYX7lpolD2IpPmCpsKSBIUKxr4Gjs9QgJjJELhtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edce9e0728.mp4?token=BH9QJL_7uBZs24PqRe_rU02NwiURvwShoztXJ-8d5J9lYZrR9zT84ufFB-NApyWLXBlnY8rEzgoLpTapDJfjRUJ5vhJp2pl7abYuzo0OB2NM14NuMaBVUvHUwd5g28gYFA5yufInoWJMgq1j-HrPEmBPqaIg729svk480CyBJn6IytcvFG6sx9Bebzivo93sPpaW83-7Br-xpQSI1cWFrA1tydJYnwYJkr5T8_2ELSfvghJ_TC9mlSdXmowuLV4kfDIQFSzerNY1XGalaPkh8ESoQJsb741RnJ5ekcm36C6YWgy4gd6e_-ElKJApDRPns6OELpMFQdPK3aMPXsAFmX9K4cAFC22J8_mWwdhsePgUfv39PcCFJjxDVX2b6owyZi6xUDAgdbAY3Sx8v20fLo--_ogFcKQRi5sioNIB-RrthlCP6IIfgcrhth0a8tYe6nsP4RbcYzU0bZWOoieMC0pg78KK0DNtkc9qlUr8Acn0kbHFjv4wDz7HAeSUTdowwSSgQ7W5XpuqahopwjQMU0nzAnmmJ_rvFDgQ6QdjypPnwJt-aHb_8ISrXeucFDgxZ2nlQJteNGiR5ENWbK7Tq04Ps3qI8Q0bhKDnbFCLU9sY5DGJRV1Bc_dUhKNkSt-_-6guYX7lpolD2IpPmCpsKSBIUKxr4Gjs9QgJjJELhtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمار ثبت اختراع در کشورهای خاورمیانه در ۲۰ سال اخیر به گزارش بانک جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/654651" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHPmYw16rSRMcKEm7Wyz59sG_L0utOVfEMz53RBsyo0phUadkNlxvcc29e9a9-cUnzkiHGuq3Ezka9wgQaEbxQR_7bYkr3I2DUWD52eya3sKUB1NL_SSCr6xUus_TxWiXFd4H4cxpEtYvdlZjF9YI2f1_Yh56LD0D0UzVBh2_6E47u3uWn1_cCYJgIsrFSurilT7V1kH_-Ut3_cGxYgtLnDpo1ieK625mbovt39cXrp72lAdhajTlJ1lC-3EkWAKYm7JXnNz2L-_K25NtNu-yZnG4ByM94Iqvtkg-B8XG3kK3AeyZo4nvCCTEpVJy3RtlxRLzrfALtYAgey4hgLtUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: دوستان ما در چین و بسیاری از کشورهای دیگر نباید نگران تنگه هرمز باشند
سرلشکر محسن رضایی:
🔹
آمریکا را وادار خواهیم کرد محاصره دریایی را یا از طریق مذاکره پایان دهد یا در صورت مقاومت، از طریق اقدام مستقیم به آن پایان می‌دهیم.
🔹
در طول جنگ ۱۲ روزه، یک وجه از قدرت خود را به نمایش گذاشتیم؛ در جنگ رمضان، وجه دیگری را نشان دادیم.
🔹
اگر درگیری ادامه پیدا کند، بعد سومی را آشکار می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/654650" target="_blank">📅 16:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwOCFza7-cCQQKbjQCZN0vOp7j4JmsKh_2kfob2TjCWnrEKViS1y07mBoWxbMAzacm5RhJ3toymYRB_-7CTRNXFU1cJ0YRiaYAa3q2t3xg4cmP8i9ZvsDH5B7JQSzr3RbbxaweklXboUt_Y-HaqZba5TZgynblgtCAOyaBCcsOys81jkb1FXVfvC-Bm8HzXcbySWRLHHnxX20IXERDQPJley681NSNtReIM9XIjJalVHOa7JBgpSgxxAofGTdDYjXSrPkdPSWixleatubFWLZuBwk2YUUu5XWcAXzsFpB-Qp5_N8j9-60k63vRVjLDSkWuvVkeRywHsdAARr3VmA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایران "آرش‌کمانگیر" را رونمایی کرد
الجزیره:
🔹
ایران از اولین استفاده جنگی سامانه پدافندی بومی «آرش کمانگیر» برای سرنگونی پهپاد پیشرفته آمریکایی در تنگه هرمز خبر داد.
🔹
به گفته کارشناسان، سرمایه‌گذاری ایران بر سامانه‌های «ارزان، متحرک و بومی» که برخلاف رادارهای ثابت، شناسایی آن‌ها دشوار است، طراحی شده که تهدیدی جدی برای پرنده‌های متخاصم محسوب می‌شود/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/654649" target="_blank">📅 16:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAt8AmlcOxlEqKbuoNKghirwL-MNrVgULeE0S51hpmyAN7H3SS3ppzH2Me7vXBOM9KcjxLNKqHB8mLgnRdG8p6xrEkhZ4ab2Y_Tc6avu9bO8KdWgVMW0T6DaNaY3oml_xcTh1VuI5PB1u6E1ygGJkrKo51ohJfNGeCv53b6zQRmdxl-N0co70_JmNxNN4skE83FTaMVLhG4PD98PodD3c3BasU2TNtrltzQ67mguPXkSjQwUopADWi_xmdqlOVUBA-b9ZI5tGpXV5c9M-Jb6AzTdU-YVvWwhbvWv7QZXlzajEJidnv3HGjTZOMoJocO-wIVbsJgXiatF60SPDnCY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در پیامی ۳ بندی موضع ایران در خصوص مذاکره با آمریکا را اعلام کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654648" target="_blank">📅 16:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: اورآسیا جایگاه ویژه‌ای در دیپلماسی اقتصادی ایران دارد
🔹
رئیس‌جمهور در پیام به نشست شورای عالی اتحادیه اقتصادی اورآسیا، با اشاره به تجاوز علیه ایران، نسل‌کشی در غزه، حملات به لبنان و دیگر چالش‌های جهانی، خواستار توجه جدی‌تر جامعه بین‌المللی به این مسائل شد.
🔹
پزشکیان همچنین با تأکید بر باور ایران به سازوکارهای چندجانبه منطقه‌ای، همگرایی اقتصادی و همکاری‌های منطقه‌ای را عامل رشد پایدار و رفاه مشترک دانست و اعلام کرد اتحادیه اقتصادی اورآسیا جایگاه ویژه‌ای در سیاست خارجی و دیپلماسی اقتصادی جمهوری اسلامی ایران دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/654647" target="_blank">📅 16:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a670753acd.mp4?token=fRJzYN9QCubGWgs17mBnvPIpJjPCcNAQBRLxd6RjLrE2ATCauWZJPGAofIfkD0ZVEbxSYB4H0BkNJRYOrpsSlCH6Q58XNa7YwDsgj1bd82Ur4l_R1ChNRgPRWuHtkxiES9S4QqxmmXXh14Nb5XdtetWjtEX45GFQdUhoorArbeuoGR08jHPpp0BTPtXrepFzQqhcPYPg5G6ygrWbKRYE4658mMlEtWLYB2aZCotCuoZxjz5OJYgNL9FlCnQDmr67f3YiNTLU4d2ZnNHuGQ0IhB1lBxuTO-KNweJOEzsgNmAxI1vGHKbnKs2Be6ekdW1vMNG9TC1MwoL_RHob5bzSs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a670753acd.mp4?token=fRJzYN9QCubGWgs17mBnvPIpJjPCcNAQBRLxd6RjLrE2ATCauWZJPGAofIfkD0ZVEbxSYB4H0BkNJRYOrpsSlCH6Q58XNa7YwDsgj1bd82Ur4l_R1ChNRgPRWuHtkxiES9S4QqxmmXXh14Nb5XdtetWjtEX45GFQdUhoorArbeuoGR08jHPpp0BTPtXrepFzQqhcPYPg5G6ygrWbKRYE4658mMlEtWLYB2aZCotCuoZxjz5OJYgNL9FlCnQDmr67f3YiNTLU4d2ZnNHuGQ0IhB1lBxuTO-KNweJOEzsgNmAxI1vGHKbnKs2Be6ekdW1vMNG9TC1MwoL_RHob5bzSs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجسمه ۲۱ متری مسی در هند پایین آورده می‌شود
🔹
مجسمه لیونل مسی در کلکته هند به دلیل ناایمنی پایین آورده می‌شود؛ این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند مجسمه در برابر وزش باد تکان می‌خورد و به‌طور خطرناکی ناپایدار است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654646" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مدارس نمونه دولتی و هیات امنایی حذف می‌شوند!
رمضان رحیمی، دبیر دوم کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
کمیسیون آموزش مجلس به دنبال کاهش تنوع مدارس است و مدارس هیات امنایی سال گذشته، امسال عادی اعلام می‌شوند.
🔹
مدارس نمونه دولتی مقطع متوسطه اول هم مانند مدارس هیئت امنایی قرار است در سال جاری به صورت عادی اداره شوند و هدف از این طرح، عدالت آموزشی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654644" target="_blank">📅 15:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b5583546.mp4?token=JiL4tcjShrzZVWPgE_Wv6VfrJ5tCnT-Rt0z2f5xPapKUAI-V7xyQ4a_0327NUpA096URACI1vUufkBwJnDkU6SO5GdKnL7VGfLQ_sBwfJtZx-ap7J4iC0-_ZeQDoMCQTNCs49lrv1Yi2pyv0JmiJRjaP7b85MWDe6dq1DYuO9fkA1RacFQqHolb8O3Ybbs6_Ii_TzLWaodfAjj9WFT3JVbh101HTQ1z5FDqd2V0kA-Mq_ohnfbIw7amx6qB2zUktuazSPostGK4DsDzOBL3oUtL587W5OKtfrsbU5SbYN3IJwgptIJNdhHr0R9DSoqMS4CpucsDt-0a2pt80f6O1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b5583546.mp4?token=JiL4tcjShrzZVWPgE_Wv6VfrJ5tCnT-Rt0z2f5xPapKUAI-V7xyQ4a_0327NUpA096URACI1vUufkBwJnDkU6SO5GdKnL7VGfLQ_sBwfJtZx-ap7J4iC0-_ZeQDoMCQTNCs49lrv1Yi2pyv0JmiJRjaP7b85MWDe6dq1DYuO9fkA1RacFQqHolb8O3Ybbs6_Ii_TzLWaodfAjj9WFT3JVbh101HTQ1z5FDqd2V0kA-Mq_ohnfbIw7amx6qB2zUktuazSPostGK4DsDzOBL3oUtL587W5OKtfrsbU5SbYN3IJwgptIJNdhHr0R9DSoqMS4CpucsDt-0a2pt80f6O1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم ایران در کربلا برافراشته شد
🔹
زائران حرم امام حسین(ع) با برافراشتن پرچم ایران در صحن حرم حمایت خود را از ایران اعلام کردند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654643" target="_blank">📅 15:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
الجزیره: اسرائیل بزرگترین مانع رسیدن ایران و آمریکا به توافق است
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔹
به نظر می‌رسد که اسرائیل بخش بزرگی از موانع رسیدن به امضای توافق بین تهران و واشنگتن را تشکیل می‌دهد.
🔹
اطلاعات حاکی از آن است که نقش اسرائیل [در عدم امضای توافق] پیچیده و چندوجهی است و فقط به بحث لبنان ختم نمی‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654642" target="_blank">📅 15:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای خبرگزاری CNN: ترامپ قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/654641" target="_blank">📅 15:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoeRtIouyVGMgp3BUqy0hd4oWwHaVNkV5EJ2e5ywxr5TdAHnLyajd8F8v7ROdcod1mzGfQ2HHZEpx2afDLlumq2TP9lpr6aTIHE835JaH5OBGdVdq45OPoNwQDf_OxVukaf49jNzvRkJZEtn9FOxRYpGaYmn84H6sgKjHW0Q-DkYEpKSh-eE_SZhMNW_VBaZKUb-aNSRo0WtLrVphccJkIpz1w9jyB9LGo8ryyV_nA68eFmHYcYxBznLBkQYCznHpysm6W7xxpeRSVCHlnIWD-qwyBihunnBBPd15A6oglQnH4HFJhlD4iGFBgs99L1gPzuy9nPOGfgOUIMftBUK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: سفارش‌های دفاعی آمریکا در جریان جنگ با ایران به رکوردی بی‌سابقه رسید
بلومبرگ:
🔹
سفارش‌های آمریکا برای کالاهای سرمایه‌ای دفاعی در ماه آوریل به دومین سطح بالای ثبت‌ شده در تاریخ صعود کرد.
🔹
بر اساس ارقام اداره سرشماری آمریکا سفارش‌ های دفاعی ماه گذشته ۷ درصد افزایش یافت و به ۲۲.۲ میلیارد دلار رسید؛ آن هم پس از افزایش ۲۶ درصدی در ماه مارس./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/654640" target="_blank">📅 15:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654639">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی هفته/ از ۲ تا ۷ خرداد ۱۴۰۵  تحولات مذاکرات ایران و آمریکا
🔹
ادامه مذاکرات ایران و آمریکا و انتشار خبرهایی درباره نزدیک شدن دو طرف به توافق و نقش‌آفرینی قطر و عمان. همچنین انتشار سند غیررسمی اولیه تفاهم» توسط صداوسیما   افزایش تنش‌ها در خلیج…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/654639" target="_blank">📅 14:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654637">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569463b846.mp4?token=pUvUQmnpUKwF3mF2ph2pzvRU6QOmj8D0oDAtotFilzANOwTPxenJZp4FPwd4HOgXXg_XvbjxbIBYrY6cqpJvsTyC7PL_vIV540B16UixkO0qs5vnwN7EonjEBvRxxYPUhJxjtTziJjTPR_aUOwFYa8aymRoTzy7jfGWjY-5SfRkU3iv-j-bFe419JhPe5Vel0zsEvkaR6ELa5QgWukNtwMmNnr7vN8wyAgs6KaBfbNbtfIgXt4gBjK43cx_YkX2Z90sJwcmT8faJMKOdGK_OumxDI94_8zIaHZaw7MeKWyXebE6EziD1NSYtrfDLVzUv7GwF2L4kM8BuBBLOldW5AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569463b846.mp4?token=pUvUQmnpUKwF3mF2ph2pzvRU6QOmj8D0oDAtotFilzANOwTPxenJZp4FPwd4HOgXXg_XvbjxbIBYrY6cqpJvsTyC7PL_vIV540B16UixkO0qs5vnwN7EonjEBvRxxYPUhJxjtTziJjTPR_aUOwFYa8aymRoTzy7jfGWjY-5SfRkU3iv-j-bFe419JhPe5Vel0zsEvkaR6ELa5QgWukNtwMmNnr7vN8wyAgs6KaBfbNbtfIgXt4gBjK43cx_YkX2Z90sJwcmT8faJMKOdGK_OumxDI94_8zIaHZaw7MeKWyXebE6EziD1NSYtrfDLVzUv7GwF2L4kM8BuBBLOldW5AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پهپاد آمریکایی بر فراز یمن
🔹
برخی منابع با انتشار تصاویری از ساقط شدن یک فروند پهپاد آمریکایی در صبح امروز بر فراز استان مارب یمن خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/654637" target="_blank">📅 14:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وزیر علوم: امتحانات دانشجویان تحصیلات تکمیلی حضوری است
سیمایی صراف:
🔹
با توجه به حضوری شدن آموزش، امتحانات دانشجویان تحصیلات تکمیلی به صورت حضوری برگزار می‌شود، اما درباره نحوه برگزاری امتحانات مقطع کارشناسی هنوز تصمیم‌گیری نهایی انجام نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654636" target="_blank">📅 14:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ2irbOBdXTdj6QEaQNLVSyebHSa-RVQiNA-geR4Rm32vuwk7pkrgozRVz8q_rW-FnH89BkxGb4nWSySnpF82SGEj25ll8ZK-zO8inZ3b5iDGEAsnySWwyTJvfTYswQwYj9zQgg_JHCVAyHJY2NwsS123NM-lQYmrky8OugcRGd_1tH-X0-hakQQbVabn5zpKG7RB-O-BOrnTxwsAnqWTMR4mkCtnMnkRBb0TO1QvCYi3rNbiHqG4RaQdMW6bIVHnLaXe7hh18lmMoXQ_A0Ssohp-NrZK0mDqE_bZqPyZU0t3Yhxix2_vn9oEurdxpgkgakozJJosYRQymVPeu6IUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس تازه ارتش آمریکا؛ یک ژنرال چهار ستاره تندرو که دوست صمیمی هگست است | کریستوفر لانو کیست؟
🔹
وال‌استریت ژورنال به بررسی صعود سریع ژنرال کریستوفر لانو در ارتش آمریکا و احتمال انتصاب او به عنوان رئیس جدید ستاد ارتش ایالات متحده پرداخته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3218501</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654635" target="_blank">📅 14:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b644ee0bda.mp4?token=ONSKtxGNrvkLZMfFYk_60AiX-1Bd8in-7BgPevGrRRBGZVydkjxov1ETwlXg1YecyraFnb5h5g0Ky1GMyOdgjs9ogC0kSX87pJn8Ma-e_yaQKKDnuFS5N4kwllBPDeBaAA_hd9rCnb0jcH7wMwF7YbBz2G1pcKboEpkAwKCB52jGMOyjAaa29iCjoTOARDyTZXw23ms5_39WFL-_ZOfORR6_ur2EfgfPpaUViD_ISRVbQ5fXWYR1oEnKb7IXS2_h3fkk7dWMtzEoQcCfRrVKCz84mHy4gN0prPlol2h_FycIlUVB3aBHSz38_YNN_djcFRZCHBGsqCAbmOs8ybmFEVCMaQ8Zu9hY8QH3tNlDY5HwYF1tf6IIxieGmqhw-Uvz62q1krp6uL4hbv_6kFEdSGXr0duMOR1ICNhN4mUDhJrS2SKgd-biY9E-9W9Q71mXYKFdHa_KOondKfbRHJgu2yE9BG-WusA3zEpAU-fBWBkWfrKc0ZcFyJYeBjbb8PDPUuhcKdY5jZ8G7spiFu8XSV7zCuTjGBDeji1Q9eHlytBaqtKxe_1eGD05sxvgOOhvXILVPZyjScbnpZXHiYcqURSpMvcZ0R4qECtcq2b5Yqdgop11UdquCLrZ0DEEi7DNRXtJa1fVdNMiWjTCqt5e_V4C8JmLdv3DA8Ah3OdsATI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b644ee0bda.mp4?token=ONSKtxGNrvkLZMfFYk_60AiX-1Bd8in-7BgPevGrRRBGZVydkjxov1ETwlXg1YecyraFnb5h5g0Ky1GMyOdgjs9ogC0kSX87pJn8Ma-e_yaQKKDnuFS5N4kwllBPDeBaAA_hd9rCnb0jcH7wMwF7YbBz2G1pcKboEpkAwKCB52jGMOyjAaa29iCjoTOARDyTZXw23ms5_39WFL-_ZOfORR6_ur2EfgfPpaUViD_ISRVbQ5fXWYR1oEnKb7IXS2_h3fkk7dWMtzEoQcCfRrVKCz84mHy4gN0prPlol2h_FycIlUVB3aBHSz38_YNN_djcFRZCHBGsqCAbmOs8ybmFEVCMaQ8Zu9hY8QH3tNlDY5HwYF1tf6IIxieGmqhw-Uvz62q1krp6uL4hbv_6kFEdSGXr0duMOR1ICNhN4mUDhJrS2SKgd-biY9E-9W9Q71mXYKFdHa_KOondKfbRHJgu2yE9BG-WusA3zEpAU-fBWBkWfrKc0ZcFyJYeBjbb8PDPUuhcKdY5jZ8G7spiFu8XSV7zCuTjGBDeji1Q9eHlytBaqtKxe_1eGD05sxvgOOhvXILVPZyjScbnpZXHiYcqURSpMvcZ0R4qECtcq2b5Yqdgop11UdquCLrZ0DEEi7DNRXtJa1fVdNMiWjTCqt5e_V4C8JmLdv3DA8Ah3OdsATI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رقابت تولید تلفن همراه جهان در ۳۴ سال گذشته
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654634" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654628">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enyGsdhM-kkrG9WTJG3kFomoeWdE2gZDFoJlRizVAbhiV5t_vj1yy0DkApXb876L-YvKhe2Q5pYxNC3Wg4kpGMSJLz47sGbogclU2v_yLnHE4QIZQ-NLZXXSAyqgztBF3Dk64hQmudMVYPZR1az_Xj6HghXnNsNhOq3ez6HN-7UEa0LlhpsJ2E6vQDYfmga8rnqALnM_WnqJKX6bxvdBv2GyooTtGGTv_heJID2x0BaSUtcT7p3qfvLa2U2hS0i478mBLxH5Vg7W3PSt7fFgoF0PJjfENUbT6QaEG4W0iX2dosAp6ly7_3dqA26UKP5TBpj_gBlthi0ps3irVfz1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTSkdg-rA-3IJ7koQnIrLnj9Vtak1FrU7yi7ujEvyX2cgHhl6hpSFSlQCTx4ryhG0rj59p0kxgfCaMqIzm09vm3tlo6flyCf6Y3Q_Mpix7LwbMnfkPGwealrUPXx-hAbwJjxnZM2gaHw2eyfiD48yR-smvRbWNfIGmKo0vMKS_VPN88YVROw52hFTXrFbEyf6SQbnaHUvHItqV8VzRiCvvcyyJ5F5kD-F7Bu5PdDxHI-LHsSUeeIK170OJbH2PAz7ZBbeQlGXfl_bV-0zbh2KfYsrDF3kZ7a9CZr_3pXufoptJ4G_Oza0E57yaeNPHr0avzFhJB9hmWosqtVqvHbow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2nv4_kX4H0cK1ZKjgoh_HGdgo-L9bXDMavYHbo2WToTTCjOgX_Pu8G7Q2A_8InoG_jb6sKWFHsvjkKvcbGXAMWYJwhlyRWzRpXoxzK9ATRAjcW4xQpi_r0dE3c190OxQzEmQWqGkwJf512OUIkiYfHIw20h-2aghXq0LMcVLOSNdtH5u6KHuf09ujTHNKdrFT7jBLoDoBy-lHT8ooZ1NfMClqJqgBOiBBfRsNmMK-KisWnZMsqPKhhtUvdNRQNoccdG9LBzx2YwqPBUoBAu2-phdO0OniX64RKPdDX6iZWSxRmHq11addi_1lg8h-IDmvYy2IqCjJLCHyIbMWKGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fELZa90uQx1a38Ovn1r8I2IXmW-XVCY36rqYHV_MX1hiKUrd2JMaHVAZcU2qdMc2czqqpsS_47z_dwgNKbX6LQ9Y-tghw8_3dpwoOA5ev3C2vfNTbGBiwv9LLGMVhMQy8FDWi7pV7CEkGZj6G80ABLWkX8qII1h2gGJ6QsxYC1OECCaLHxoSrlIp_nyH-5JaG7vfcO1MuqN6beTEBh2bG8rxF8YLR84Ajn-52kEhNgtHfmJruSlcmkQbSnM5SX0lgRZqTDjRSO2YEpLOliG8cWxWp4PG0LU4U6RrXJqdrVYg16HtxkAhPBlA57Inv7kapVP01utcPrBMf5krHUrL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhWBlpAW0W8zijMprxKhBl6eELCnhO2zPR8C4Q8BTF1iDca_MyMsC7_f124k3RL5Xbl_SoVlgDzi-Z1HU6aZR4CTRaVhsOEUuiWCWVdhu_9Or2QXfw8WIOayCSCd-YrLuaTTSuPGQ8lKa2ycnQUpQ6reuC5UdsL_hgFeWI2Y8qY0LBhJtb3M35ejgHGqUlz6uk0mM5gKwJavSy5NfqEsUBjOa-A6SoK-4er0fmskXQnliD7xNydv_41S5YtLtZ2PslfocvobB3DkzByIAR-PEzjq9vX5xe9fOZwVcjiY2zyABJksVZnBpniruPjFE5eA7UPCQl_dvghUmUg83HNULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm3pEh0Qa3NVyqvJ2p23OA3mOE8noXnLvSiVdDo07EmQmPcF2HZ8_dbWDTQpPtGxydqAhWNtPOK1KjCMH7eJlSG-Yn4anfpW7dQuCvCo8Hhml98f5C9Uwtu-uB3oQ5VVZeWaROMmYizb0c8ABmFtWU7h5H2OV3uFyCfn24XGF555JmIk7c_WOGQ5dnnAe-KUEHIjGyqFSpM9I7A86M1zOsPXi6I8HUFTsJH9sQ__Fh9VVitjvkzH7BoCB6mayIkybUZ_I6tRYemRZzrXc6XjtlGSp0q0Ob1v3yjYIQGDt24woVHhVHp6xSqguBktWOlNrWXEP29QetfPpaHbxbCSJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مخاطبین گرامی خبرفوری،با حمایت و همراهی شما، این حرکت می‌تواند به اقدامی مؤثر در کاهش آسیب‌های ناشی از مصرف پلاستیک و حفظ طبیعت تبدیل شود.
‌
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654628" target="_blank">📅 14:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654627">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بانک‌ها ۱۰۲ همت از طلب خود را از مردم گرفتند
اعظم قویدل، سخنگوی سازمان ثبت اسناد و املاک کشور در
#گفتگو
با خبرفوری:
🔹
در سال ۱۴۰۴، ۱۸ میلیون و ۱۸۱هزار و ۶۹۶ فقره سند رسمی شامل اسناد فوت، وکالت، اجاره و تعهدنامه در دفاتر اسناد رسمی تنظیم شد. همچنین ۱۸۱ هزار و ۸۵۶ پرونده اجرایی در ادارات اجرای اسناد رسمی تشکیل و ۱۱ هزار و ۶۹۷ مزایده برگزار شد.
🔹
در نتیجه رسیدگی به پرونده‌های بانکی و وصول معوقات، حدود ۱۰۲ همت از مطالبات بانک‌ها در سال گذشته از طریق ادارات اجرای اسناد رسمی وصول شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654627" target="_blank">📅 14:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654626">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
صداوسیما: عبور کشتی‌ها از تنگه هرمز نسبت به هفته‌های گذشته شتاب بیشتری گرفته است
خبرنگار صداوسیما در تنگه هرمز:
🔹
در ۲۴ ساعت گذشته ۲۴ فروند کشتی با هماهنگی نیروی دریایی سپاه و وزارت امور خارجه از تنگه هرمز عبور کردند.
🔹
کشتی‌های کشورهای متخاصم حق عبور از تنگه هرمز را ندارند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/654626" target="_blank">📅 14:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORuMYhEv91AVbcBJHr1mGzaHDy_-SXrG5yrCyNog2P_kToYs5t-CjnbodKUCAehG87V-P72_ApEUaROKfSGMXJ0f6UkgaTcSol2P7zITpcjinS39L-970M3M4QpKYbLQoTIf4pfGkVcgfh5Y_eD2D2tVnKpZATxD2hDj-X_NOarCMftnao_DC4LfJXiPzJN3aq68vhK5kLkF2345JjCF52PMexa-muzX0B9VC8BYTLHrC35kFICZekC5hgadgd-g_YX1yFQOm9Kxg6olm42oSkpajNN6NOwM7gl1xxi_nbwoifkcYYa_OsYCPifK233f6W7Xh1K-25Lp2FydQxdIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حجت‌الاسلام و المسلمین ابوترابی: مجلس باید دیده‌بانی امین برای منافع ملّی و فراجناحی باشد نه جایگاهی برای سهم‌ خواهی‌های خُرد
خطیب نماز جمعه تهران:
🔹
همه‌ی آحاد ملت باید از وحدت و صفوف به هم پیوسته ملت حفاظت نمایند و اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند
🔹
تاکید رهبر شهید بر قرار گرفتن ایران بر قلل رفیع دانش و تولید علم از این حقیقت الهام می‌گیرد که اقتدار دستاورد دانش و علم است
🔹
آمریکا و رژیم صهیونیستی این واقعیت را درک کرده‌اند که نیروی نظامی حتی حضور مستقیم آمریکا، قدرت بازآرایی واقعیت‌های سیاسی در غرب آسیا را به طور کلی از دست داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654623" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd00e0a65.mp4?token=e9CWyQrAogHokmS_MWTH-OgvoNtGmjfM4I2PtKOWPOomq9I8m1Q_5PeMCr70JYitg8wcEI5yASGHoZvuXOnMybFYRCNMp9ngfjdgg1mwrVnY9Sc6fexzoahuuJeZWxR-hLeVOsAswTzvE-d_565KY4HOu013GU-Fz3_bVoIK90Es5k6OhsIR7eqvIBDWXOVlwh7zi8eWxVS9C2VbS2ecDuAi2jm2MFM4SLcsRq9AnAnOFvO2oNSXUpPhaDuvDcu4kjdkGtME4144sdxqrNYeT5XVI0ImS2Mjz3_JIazwTIyx2NNWrW-2KKgrOaXim7C0M5D9W7d4eUGs5xHtC_bqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd00e0a65.mp4?token=e9CWyQrAogHokmS_MWTH-OgvoNtGmjfM4I2PtKOWPOomq9I8m1Q_5PeMCr70JYitg8wcEI5yASGHoZvuXOnMybFYRCNMp9ngfjdgg1mwrVnY9Sc6fexzoahuuJeZWxR-hLeVOsAswTzvE-d_565KY4HOu013GU-Fz3_bVoIK90Es5k6OhsIR7eqvIBDWXOVlwh7zi8eWxVS9C2VbS2ecDuAi2jm2MFM4SLcsRq9AnAnOFvO2oNSXUpPhaDuvDcu4kjdkGtME4144sdxqrNYeT5XVI0ImS2Mjz3_JIazwTIyx2NNWrW-2KKgrOaXim7C0M5D9W7d4eUGs5xHtC_bqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهار در ارتفاعات تالش
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654622" target="_blank">📅 14:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fea825c6.mp4?token=cZwKuQHCdFm3E7LHAo4WuZx02SYNbr_T2IcovI-pgWuS2e2l9vhZWXZqNjYubmrTjXB4eI8ZWf6Cx5bo5-dYHWH6LnYdilNwqkx14sf2HaXjjXGryIv90trqizN_ckjAHNET__kHoRo9bY1UPnLLJ20FT3bU0av5zrafwaErg8c4ID7cFFeTG9sKHAu-tYJJFd7HXfUV8dqzcAKVBaLY2EmXum2B1NBJfVwTXOVBTbm4C4ZVNqt-tPSaYGEgRvSgKsXupHTBlYgWFA49FlEptcDYwptlvsqeZ8LUp296G9bcTPCA-6wgAZ4-P8XjG-bhEhYY7zddVsJUm2n23iwOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fea825c6.mp4?token=cZwKuQHCdFm3E7LHAo4WuZx02SYNbr_T2IcovI-pgWuS2e2l9vhZWXZqNjYubmrTjXB4eI8ZWf6Cx5bo5-dYHWH6LnYdilNwqkx14sf2HaXjjXGryIv90trqizN_ckjAHNET__kHoRo9bY1UPnLLJ20FT3bU0av5zrafwaErg8c4ID7cFFeTG9sKHAu-tYJJFd7HXfUV8dqzcAKVBaLY2EmXum2B1NBJfVwTXOVBTbm4C4ZVNqt-tPSaYGEgRvSgKsXupHTBlYgWFA49FlEptcDYwptlvsqeZ8LUp296G9bcTPCA-6wgAZ4-P8XjG-bhEhYY7zddVsJUm2n23iwOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به آمریکا می‌رود
🔹
طبق اعلام منابع پاکستانی، اسحاق دار، وزیرخارجه پاکستان، در تاریخ ۲۹ مه (۸ خرداد) در واشنگتن با روبیو دیدار خواهد کرد./ انتخاب
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654621" target="_blank">📅 14:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6sH5c8bez38EsMuD5-AI1x5rZQ405viOFPwE6e_MdjXrBxxaqTCXcAi5FBaCV4nMrSdSzBKK_agUQ6OplJ-XA3XFX7IT6oFRhUA1sEgJ_IcxGDdAH9AlVR5SvqqHUE6aV8d4e-aME7ehJH47TbStI5ZDsihwhzy1iBsfFpFIl83yGxnejCpJSDKDYvUUhgB3U2tHAA32v03Tc6vXWaJ32CHPCwNzo9tsjXLADdOzzJhe8Rob7M_m97odJaSXG4aF-kkqeqXr3ouhWXtbxDKFDlZ_zT1ZwsKo_xj5EZyXjDKslffiQ-VykN2X7NrCsO-Kgu9qDJLTOhivrdNMJqOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد معتمدی: چند رادارشان منهدم شد و حاصل شد برگشت آب به دریاچهٔ ارومیه
🔹
حالا فکر کنید اگر کلا شرشان از منطقهٔ ما کم می‌شد همه‌چیز چقدر پربرکت‌تر بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654620" target="_blank">📅 13:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHh1TVL-eVe0IPuFsr-gQ5UGOeXr4Do9lCzCnILN5QzAJ8GEGuNxxcrWbhh9n-1cKbox8NZEbJIuyc8lDfOTsNAWZElwe0op76e_GQSFx5D3827GATxHF7xtoPBGuksnSgKdnKYZDe3BZCIktsaPYnm5rwugU1kiLbMCnCbuOqy9-4f3I5umuKCzuXCaJOQv-IgA8cV6Zc8gm8VXuAtCQCEG9hzIJ8eR0gxRk4HEuKGvmRFdMkw2Uc_Jtm6EN3sDE8kwW_GblbXWFyE8V2CfcqgrXFKx2W_cw45cS-X1HjwGneYB3M-c-_BKw99QBKK9zJWdXOsnI3er-TOlglAt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز : پیشنهاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران در چارچوب توافق صلح
نیویورک‌تایمز:
🔹
یکی از عناصر جدید و غافلگیرکننده در توافق پروژه صلح ایران، پیشنهاد ایجاد صندوق سرمایه‌گذاری برای ایران با حجم ۳۰۰ میلیارد دلار است. ایران ابتدا این مبلغ را غرامت خسارات جنگ (برآورد ۳۰۰ میلیارد تا ۱ تریلیون دلار) مطرح کرده بود اما طرف آمریکایی آن را به‌عنوان یک صندوق سرمایه‌گذاری بین‌المللی بازتعریف کرده تا از به‌کار بردن واژه «غرامت» اجتناب شود.
🔹
این ایده به استیو ویتکاف و جرد کوشنر نسبت داده شده و شامل پیشنهادهایی مانند تقویت پروژه‌های املاک و مستغلات در تهران و سازوکار سرمایه‌گذاری گسترده‌تر به‌عنوان مشوق توافق است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654619" target="_blank">📅 13:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550993e97.mp4?token=cBTE4eUByS6HQUgv8GfUsmTNRNSzDDWTySaZO3MiP8qYq20ScRfpQZGqWxgvAtYpzNrGzF7dvLyNLl-DrKWSpKJBQzgMvu7SthB8aVi54DeE-FIM75LZnef37AYL-TLf9Wvv_zRB2UL1PXd5Firvw7mTgXURKkCUUVrssMVXwg8Ml8acqni1-TKIy27Cd3u_sMbsCBPUDtMk-b11nNZby-bOrfZRa8m8mRApvjDkLV6FTQN-NMcD9w5bVklQccd5py23rZfnvIqBkFxD5BygQFRs3yS6mMD0_o5A8gxCIPDGNnL4AClv9oK6q4LlPvdJ53uaePUvNHjUuqq3l7zG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550993e97.mp4?token=cBTE4eUByS6HQUgv8GfUsmTNRNSzDDWTySaZO3MiP8qYq20ScRfpQZGqWxgvAtYpzNrGzF7dvLyNLl-DrKWSpKJBQzgMvu7SthB8aVi54DeE-FIM75LZnef37AYL-TLf9Wvv_zRB2UL1PXd5Firvw7mTgXURKkCUUVrssMVXwg8Ml8acqni1-TKIy27Cd3u_sMbsCBPUDtMk-b11nNZby-bOrfZRa8m8mRApvjDkLV6FTQN-NMcD9w5bVklQccd5py23rZfnvIqBkFxD5BygQFRs3yS6mMD0_o5A8gxCIPDGNnL4AClv9oK6q4LlPvdJ53uaePUvNHjUuqq3l7zG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در رودخانه فرات، در شمال شرقی سوریه
🔹
به دلیل سیل گسترده، وضعیت بحرانی در استان‌های دیرالزور و رقه اعلام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654617" target="_blank">📅 13:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDyYH6gAG1uF--1iPQC0BP69X_N6M2Wu8phb1MgCLRJMrNv833LYMHMt48h3XwSY8ingQrtSp09IOLA1DIV5ofOhwrh9RU_coP5Q5wEPcq3yIoRttCc5_nUrbzU_5wFAUzFxXNJa9U1ipc0yjm2wbEuvG_epySQXmNUp6HdfogeskYDN1aC6YBUn0duvpD3AuIw_mo984-gTupYCNuQIuJIbeVJx3QHkIej0JOhrWQQDykc6oFPSE4VGOqGWUPJSWFuEdao5CGPKK0QiVxuftGUg7RVj55eAO3KZa-pUR4LvEbGj6lE91oo8Pv8Vc4HAEjIgsAdJBuXlgRt8XK_SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: به قدرت ایرانی‌ها تعظیم کنید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654616" target="_blank">📅 13:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شایعه‌سازی برای یک گنج در ایران
🔹
رسانه‌های غربی دوباره شایعه‌سازی کردند؛ آن هم درباره یک گنج بزرگ که احتمالا از نفت هم با ارزش‌تر می‌شود.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/654615" target="_blank">📅 13:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی هفته/ از ۲ تا ۷ خرداد ۱۴۰۵
تحولات مذاکرات ایران و آمریکا
🔹
ادامه مذاکرات ایران و آمریکا و انتشار خبرهایی درباره نزدیک شدن دو طرف به توافق و نقش‌آفرینی قطر و عمان. همچنین انتشار سند غیررسمی اولیه تفاهم» توسط صداوسیما
افزایش تنش‌ها در خلیج فارس
🔹
انتشار گزارش‌هایی از تحرکات نظامی و درگیری‌های محدود دریایی و فعالیت پدافند هوایی و حمله به شناورها و پاسخ متقابل ایران
اظهارات جدید ترامپ درباره ایران
🔹
آمریکا «به توافق بسیار نزدیک شده» اما همچنان اختلاف‌هایی باقی مانده است. مذاکرات با ایران را به تحولات منطقه و توافق‌های عربی مرتبط است.
🔹
گسترش رایزنی‌های دیپلماتیک ایران با کشورهای منطقه از جمله قطر و پاکستان/ همچنین ایران و قزاقستان ۱۴ سند همکاری مشترک امضا کردند
واکنش رسانه‌ها و فضای سیاسی داخلی به اخبار مذاکرات
🔹
برخی جریان‌ها خواستار انتشار جزئیات توافق احتمالی شدند و فضای رسانه‌ای کشور تحت تاثیر اخبار مذاکرات قرار گرفت.
مهم‌ترین اخبار جهان
🔹
ادامه تنش‌ها در خاورمیانه
🔹
نگرانی درباره امنیت تنگه هرمز
🔹
افزایش فشارها بر رژیم صهیونیستی
🔹
ادامه بحران انرژی و اقتصاد جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654614" target="_blank">📅 13:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654613">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzDqQ6NVADSZH9exEXblwIEKIMwF9Tacjgmpx8jD_7u-uoo5JxIqpf4aDXS7G3-rGrIE0l8HQnji03l7y5MjUrb9I_Uf_TlU8nUxbYXfZueYiOCwJ1L3Hd4DdTxMkKylBZ3z-jHSaiKOGSa4cjkrBrAoC85OPYyzKJQ-UhfprcCe-M2R1XUTQmH6aY-7VDYYHB6hH6FmSBAL0jVJnoHKd_eKGn31vV32EY6FMCA-9Xcv0PacKVUa3L_b-ZCq_CUlYBvqYDdCR_yAV4L-N_5NVjVwUozr_8KqaKyCceebybfroXYOSiiYxsqLKPkz-CEQ_xjmONpmBbpbrYLwYLYV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهی برای معامله نیست | چرا ترامپ نمی‌تواند ایران را وادار به عقب‌نشینی کند؟
🔹
یادداشت تازه آتلانتیک درباره بن‌بست و سردرگمی دولت دونالد ترامپ در مذاکرات با ایران است. نویسنده توضیح می‌دهد که ترامپ پس از ماه‌ها تهدید، فشار نظامی و تحریم، اکنون با واقعیتی روبه‌رو شده که برخلاف انتظارش، ایران حاضر نیست تحت فشار کامل تسلیم شود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3218537</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654613" target="_blank">📅 13:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2738688f66.mp4?token=iS8e0d7B3AOTfm2wuMh0GamTPKscBJjaFiofPXpFS4IEdJwuiOBTn06ZWQn8WkhioHUfU34x1AudMsx0csOXsHe1oW9DQEhupe8eR1XQFEfE_BayXqzYstv6R6HPnuxEGBwFivvSbJHph3wke7P8J6pPma4Hx_p6OgksMqb1of8kmCwN4-s_ftqoXGLe2ZbiBvs5c8QON1tbBX2PDzWLh30fl-JupEmq29Sh6oVoHkmn0qz7VCFpac6GXZkV8i39ZrfdFw6sINdb5orkeELE-TxbYIGVMB4beVHrc_0mmpGkIdzBUb1XYqeuNuugfCkhyTa512u_nGGYitFUhca2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2738688f66.mp4?token=iS8e0d7B3AOTfm2wuMh0GamTPKscBJjaFiofPXpFS4IEdJwuiOBTn06ZWQn8WkhioHUfU34x1AudMsx0csOXsHe1oW9DQEhupe8eR1XQFEfE_BayXqzYstv6R6HPnuxEGBwFivvSbJHph3wke7P8J6pPma4Hx_p6OgksMqb1of8kmCwN4-s_ftqoXGLe2ZbiBvs5c8QON1tbBX2PDzWLh30fl-JupEmq29Sh6oVoHkmn0qz7VCFpac6GXZkV8i39ZrfdFw6sINdb5orkeELE-TxbYIGVMB4beVHrc_0mmpGkIdzBUb1XYqeuNuugfCkhyTa512u_nGGYitFUhca2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مأموریت امام زمان الان چیه؟</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654612" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjVlH1isgW14Wq_Ri3kbtXy8hTAoOVeZ7aT_v8MngWeQxz2edd1HurMwklCZw8nL5etIuf7pQU6SfSvFzM4wJUa7AzvD9_o5-dVSyUhqxDG6-93JkvQbdVRwSM7Gp5Tv6KzerI94n-5t4jbyrXgLgoRL7zASKJ4QFp5enFHIkK8pDf1yp92XfMQmO48-CRnEyPQHGwKFBbJq7JXiSHMCKCL9SrPlsg93ZeVE0UfCM7kNiG74yu5htdEKO2nJyeA8_28LD3x2aS2hlMYHS93FZPO1XCaxMD9pg_KpqqE2mtr1liDpUI4929gdhiNftw7K0lol-OjeiXkusbufGLz_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هلاکت ۲ عامل اصلی آشوب‌های دی‌ماه دره‌دراز کرمانشاه
🔹
۲ نفر از عناصر اصلی آشوب‌های دی‌ماه سال گذشته در منطقهٔ دره‌دراز کرمانشاه به نام‌های مجتبی ویسی و میثم ویسی، روز گذشته در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654611" target="_blank">📅 12:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy2Q8SN-P1pU8w0TEH1N-3AYqptRRqN5KjzscXq-_XSSirbr2HNhvvpl-QF6z7R3Ipd5SrpD44uTnRSVDCfh3l-MxWrVq6yvJSa65HL0CWGy8XrhsS8252x-IVzsvaMuWLj1fWR5Hs24IExdrUOMIfPhhKjxe88pe5ANefz5hqlKbOAsPcIZHpj-a1zrLR3heDI94oBE_vNgY8qcg58n3WPtvtOzKbrlbBDrXUme15NuE6VjlY-t1x5ktAPzhCfkVC2IYYGZm42mi9B1-sMRoP87vsTPmfVwhFnKN7HzC5cwM7P2ybCtgqNHisoDO8tk1DSagW5sAMRv9_8TTMF14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقی‌ها ۱۶ همت پول به بورس تزریق کردند
🔹
در هفته اول خرداد، سهامداران حقیقی بیش از ۱۶ هزار میلیارد تومان نقدینگی تازه وارد بورس کردند که باعث شد شاخص کل ۸.۳ درصد رشد کند و به کانال ۴ میلیون برگردد؛ شاخص در پایان هفته روی ۴ میلیون و ۷۳ هزار واحد ایستاد.
🔹
بیشترین مقصد پول حقیقی‌ها صندوق‌های سهامی، گروه بانکی و فلزات اساسی بود. میانگین ارزش معاملات خرد هم از ۱۳ همت عبور کرد. صنعت لبنیات با حدود ۲۱ درصد، داغ‌ترین صنعت هفته لقب گرفت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/654610" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1567d3d1f9.mp4?token=uY9G_5PIiu3GXwQ-3pOrYVAhr33erW5sYRtFlLWlXD1b6N-ucfRM6nKL_tjUTzbk3e5Kxe6xgl2TtYBAwwBt-viIf-bmy3NxorapaB3VDyycvg_jYmboBjiBLcfUvKXcp0wRopSNGJkQ3V-geOKs2c0Rn09AWT5KB67OtDtj2QHzjM8qKHwAWuwLYllZ_okZdbUZr8rPSlQG1LHopJUyxa4LlXqYKn8pwlUnaoCaIpXOuWJxwOAX0E0ZY4dTQ7WWb9zs6U1SNT4YcyqPUy5cBNJciCUOQjSBFHM35MS3tILUlLeorEOljFAf4Reb3Wp9E-LT4T_R3is_szOewinARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1567d3d1f9.mp4?token=uY9G_5PIiu3GXwQ-3pOrYVAhr33erW5sYRtFlLWlXD1b6N-ucfRM6nKL_tjUTzbk3e5Kxe6xgl2TtYBAwwBt-viIf-bmy3NxorapaB3VDyycvg_jYmboBjiBLcfUvKXcp0wRopSNGJkQ3V-geOKs2c0Rn09AWT5KB67OtDtj2QHzjM8qKHwAWuwLYllZ_okZdbUZr8rPSlQG1LHopJUyxa4LlXqYKn8pwlUnaoCaIpXOuWJxwOAX0E0ZY4dTQ7WWb9zs6U1SNT4YcyqPUy5cBNJciCUOQjSBFHM35MS3tILUlLeorEOljFAf4Reb3Wp9E-LT4T_R3is_szOewinARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: ایران یا توافق می‌کند یا با نیروی نظامی مواجه می‌شود
پیت هگزث در جمع سربازان آمریکایی:
🔹
همانطور که رئیس جمهور در جلسه کابینه گفت... ایران یا می‌تواند با یک توافق از طریق مذاکره، کار را به روش درست انجام دهد - یا می‌تواند با شخص من در سمت چپ معامله کند. که اتفاقاً من بودم - اما این من نیستم. شماها هستید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/654609" target="_blank">📅 12:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd34f8637c.mp4?token=cXZlWlNUflm6L9jc7g4Y7jnaRNRlng4S7n4_vEJxdhi81MQ_HQF4UgPdYxsV8cpzxo4pHZLGIQz4X-cifIRAuo0z_M3R3ybU9DLCiRMS28G8NoV9fq_aNcu7LSha0QTTbORQb8PvNhs5yIrYVA-eFJ1PVWp0bydUntJcplOYO_2v2Thwij0KDzQ0Z0A5GZea6ZHFDplUqiEfUSnHcSqLGgFBEEteG9rfwsHPkvw5EnSVQ9l4c7hT6MAtMWsbEYT6CkU2osBsa7Z-CjwsNipdxIJ_zbHIZJmBovw-YrrLJ2_-DJvRfshTvDqKa1zSsFPriYsKvFDbMLnzp-dHU6_BiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd34f8637c.mp4?token=cXZlWlNUflm6L9jc7g4Y7jnaRNRlng4S7n4_vEJxdhi81MQ_HQF4UgPdYxsV8cpzxo4pHZLGIQz4X-cifIRAuo0z_M3R3ybU9DLCiRMS28G8NoV9fq_aNcu7LSha0QTTbORQb8PvNhs5yIrYVA-eFJ1PVWp0bydUntJcplOYO_2v2Thwij0KDzQ0Z0A5GZea6ZHFDplUqiEfUSnHcSqLGgFBEEteG9rfwsHPkvw5EnSVQ9l4c7hT6MAtMWsbEYT6CkU2osBsa7Z-CjwsNipdxIJ_zbHIZJmBovw-YrrLJ2_-DJvRfshTvDqKa1zSsFPriYsKvFDbMLnzp-dHU6_BiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از حرکت فلامینگوها در میان کانال های آب دریاچه مهارلو
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/654608" target="_blank">📅 12:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
لوازم آرایشی تا ۸۰ درصد گران‌تر شد
مسعود گل‌کار تهرانی، نایب رییس اتحادیه آرایشی‌ و بهداشتی و عطریات تهران در
#گفتگو
با خبرفوری:
🔹
واردات لوازم آرایش درحال حاضر تقریبا به صورت کوله‌بری و ته‌‌لنجی وارد می‌شود. قیمت لوازم آرایشی به طور میانگین بین ۵۰ تا ۸۰ درصد افزایش داشته است.
🔹
۸۰ درصد کالاهای آرایشی و بهداشتی تا الان تقلبی وارد می‌شده است که بیشترین آن از کشور چین می‌باشد و پس از آن هند، پاکستان، و کشورهای سمت غرب ایران هستند. این کالاها از اروپا وارد نمی‌شود چون تولید چنین کالایی آنجا صورت نمی‌گیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654607" target="_blank">📅 12:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b5942bb5.mp4?token=j_yWz5mHEM6pBwFyi0esu--H8C3FO-7XP14dM-IdNcQ-jxApVcs3x66gmYKjdVcuHJQ82b_MBbIrH82oZwy49ecNmYZLn7DrZcG_jH8T2b7vSBxwF8k-ixM8VvKv98nxR1MK1sietI26p5ZO6iGTQmaRee6dtlBvS0Pq24Cywa2qR-eU-N1zbAYyeBFshZtkHdsRSB3Klng71Wvhu5MjVB3hgCVebNPTr3zO8ZMA_7eMyamKvmQDfp81cneT8LIv3C48qpBOfAf6Etj_d_t-hutR4u-8YNgZXMJZg5EjGr0p_RDl_mz6KMAX4cL2d28GvgMLgVBrolkl32BAO7m5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b5942bb5.mp4?token=j_yWz5mHEM6pBwFyi0esu--H8C3FO-7XP14dM-IdNcQ-jxApVcs3x66gmYKjdVcuHJQ82b_MBbIrH82oZwy49ecNmYZLn7DrZcG_jH8T2b7vSBxwF8k-ixM8VvKv98nxR1MK1sietI26p5ZO6iGTQmaRee6dtlBvS0Pq24Cywa2qR-eU-N1zbAYyeBFshZtkHdsRSB3Klng71Wvhu5MjVB3hgCVebNPTr3zO8ZMA_7eMyamKvmQDfp81cneT8LIv3C48qpBOfAf6Etj_d_t-hutR4u-8YNgZXMJZg5EjGr0p_RDl_mz6KMAX4cL2d28GvgMLgVBrolkl32BAO7m5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معجون اوتمیل یک صبحانه مقوی و خوشمزه برای بچه‌ها و بزرگترها #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654606" target="_blank">📅 12:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8d7516f6.mp4?token=WVdcCrpVoyGIYMmgfZ_qJnM_cLrSHFCW8jUL-KM4r0LqWsZ0XXUO2iiep_v1GDjEi_nsBPEpyi05rVVdCni4GfnFCe4sdL9Fobw1dPdvybQLB6Vy2KQHzaBGj-o6f9augzt3FIhQFUHKM-FnF3ViCg5APWGfS0hOZMZINTX7ag_jjuBBGIgnzVcxIdp23qPezuxf_e3XbdBKTUQdsMZltdlNKpNLNX1wXiTm_E9V-iEpnoNH9-4FerXZFiTrc4TBo5CmctvweZmj_9r6iPvL32ZISKrYIt0wQ7GhN0osIvDFwiwVOc_Mkx7FqdrgqSQ3Bif6kgYhZyR6aQy2zFMa8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8d7516f6.mp4?token=WVdcCrpVoyGIYMmgfZ_qJnM_cLrSHFCW8jUL-KM4r0LqWsZ0XXUO2iiep_v1GDjEi_nsBPEpyi05rVVdCni4GfnFCe4sdL9Fobw1dPdvybQLB6Vy2KQHzaBGj-o6f9augzt3FIhQFUHKM-FnF3ViCg5APWGfS0hOZMZINTX7ag_jjuBBGIgnzVcxIdp23qPezuxf_e3XbdBKTUQdsMZltdlNKpNLNX1wXiTm_E9V-iEpnoNH9-4FerXZFiTrc4TBo5CmctvweZmj_9r6iPvL32ZISKrYIt0wQ7GhN0osIvDFwiwVOc_Mkx7FqdrgqSQ3Bif6kgYhZyR6aQy2zFMa8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت کنونی در مریخ از دید مریخ‌نورد Curiosity
🔹
این ویدئو در روز ۱۳۵۳‌امِ حضور مریخ‌نورد روی سیاره تهیه شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/654605" target="_blank">📅 11:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ترامپ به بیمارستان رفت اما از مجروحان جنگ ایران عیادت نکرد!
سی‌بی‌اس‌نیوز:
🔹
وقتی ترامپ روز سه‌شنبه برای معاینه شش ماهه خود به مرکز پزشکی والتر رید رفت، با اعضای سرویس آمریکایی نیز دیدار کرد اما به گفته یک مقام نظامی، او هیچ یک از ۱۴ سرباز مجروح در جنگ با ایران را ندید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654604" target="_blank">📅 11:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktv_RSMChjLUbhh8FaCJiGeoTsyVFQi5aGqZx0O4xgR10cSQ25qavMaoRDzr4qamhcfn8C8GpjkpYyvQYF-r4YYKodMSn41XxBKdCAqYbA0v91Llontxe1YvmxbuGoAncBksklBK4ay_bzRzuDXXL2TN6rrMJ70vmBX-bIo0HpgkTVW9T4MMJNyx8NRgg0yOklc9EghDfkBou8HgaCrfTztVVRPiaJXIzftRFWK0z-O-u6p694H5EBUKmjMibB4OmL-BfPzK3--V-xvc1jlAtAQa8qsJxSuVt9pmwWaWMqmIF7_mq9iHIjZ4Ku5J80xluLK4Iu0vKhfORemEAIM__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسبت قیمت یک متر مسکن به یک گرم طلا در ۱۰ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654603" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoaDmYL7auMAVJ1L6GDghB-0osxNSnKHdjeUzjFTW4KCrJW-s8MXrFUBVmdpM1an2oZDGUD6s_L-oYdIQyxhJ9Lh3M-0ml5RzxoJl_GSBiCqKDw4svYjDpEuWggQZ9qVj7IjCyWhYS89Ae06c9cOxgqFmP5X5nDqCzvYPOsZ_nG-U81_Cjpjnc4bxC1vgtgCn-dP35ZOuE1UkVqV7ahB2l77aBiNaRwh29KTPXDz-kx3XU8Djqbdt8RJ-5SkTmQO3p8tF_ZmjhmB_l5ThGeEiSD9vs0g0qHNBsTiNtuttqNGSs5qL6-tqoxe3qO3Fewjhj8BukAFtPnWzfH5fI5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه گروه‌های خونی بیشتر در معرض سکته مغزی هستند؟
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654601" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3811cf74e2.mp4?token=P7BNvKqrJ_pP_iSsMhaUPoLJD4lb1PhmU3UZaCeMtVH-lqeFQCE-cnSRTv8de5ZW-RVOAUeQViJPLK383dIrdr6oC-gRstoeIqDmLHGwfUJpDKNavQ_tCq8cHZC9PxsDOy0TwtT1zOUxEDS7iKoJMViI4Z85ITeHH_DxdVgiD3cShviX8qWcqJ7Hu-K1HFYm7AINbsHtQpagPe79vTtdpupe1pdDzOT6lZwOCeSZuu1-73UF-NauMETdpJWzVbzPkd8X5plRJ71r31Omt066wAFqsJR0DwjSWa2FFV9GMTpEeCT4xqR6r-rMGfKzLRuOwCyLCF12xpGu-Qk53WiDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3811cf74e2.mp4?token=P7BNvKqrJ_pP_iSsMhaUPoLJD4lb1PhmU3UZaCeMtVH-lqeFQCE-cnSRTv8de5ZW-RVOAUeQViJPLK383dIrdr6oC-gRstoeIqDmLHGwfUJpDKNavQ_tCq8cHZC9PxsDOy0TwtT1zOUxEDS7iKoJMViI4Z85ITeHH_DxdVgiD3cShviX8qWcqJ7Hu-K1HFYm7AINbsHtQpagPe79vTtdpupe1pdDzOT6lZwOCeSZuu1-73UF-NauMETdpJWzVbzPkd8X5plRJ71r31Omt066wAFqsJR0DwjSWa2FFV9GMTpEeCT4xqR6r-rMGfKzLRuOwCyLCF12xpGu-Qk53WiDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: آتش‌بس با ایران همچنان برقرار است
ونس:
🔹
اگر وضعیت فعلی جنگ با ایران را با ۵-۶ هفته پیش مقایسه کنید، به نظرم کاملاً مشهود است که آتش‌بس تا حد زیادی برقرار است.
🔹
در زمان برقراری آتش‌بس گاهی تنش‌های جزئی و پراکنده رخ می‌دهد.
🔹
این نوع آتش‌بس‌ها همیشه تا حدی پیچیده و بی‌نظم هستند؛ گاهی اوقات نیروهای رده‌پایین با مقامات سطوح بالا هماهنگ نیستند و ارتباط درستی ندارند. بعضی وقت‌ها هم افراد مرتکب اشتباه می‌شوند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654599" target="_blank">📅 11:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654598">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3a90562c.mp4?token=KI2O3IDk_n36a_0EtI3rkyEkIk_G_s12zOcOra4wD68MY2qzt7cDjUBw4bpNeerXBFsQ72-E_FgX3YdglcD4zj5tWcvCl7PN0Vg_uEgqhksTXKwR1M3zjfdOU1Kl0wk0zHuNn1bVqNNMsrTg_vpkNYGKKnuxQOnXn5bDNy2oyE55LQk5p1jAWnZTPNMnJ9fFr42KnTeUh_TG8bPiNL-VU8RyENx0088dSzZfgqzXMXxG0VuQ28XLmLXHbj9sT3mVNtBAsk1X1iWyhlBWeaDeVYICgT1_qBFyygarM76NZY2kEmuxnmp9SkBS9gB5lTYNsWVEzKxJPPenSOBCUW6fAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3a90562c.mp4?token=KI2O3IDk_n36a_0EtI3rkyEkIk_G_s12zOcOra4wD68MY2qzt7cDjUBw4bpNeerXBFsQ72-E_FgX3YdglcD4zj5tWcvCl7PN0Vg_uEgqhksTXKwR1M3zjfdOU1Kl0wk0zHuNn1bVqNNMsrTg_vpkNYGKKnuxQOnXn5bDNy2oyE55LQk5p1jAWnZTPNMnJ9fFr42KnTeUh_TG8bPiNL-VU8RyENx0088dSzZfgqzXMXxG0VuQ28XLmLXHbj9sT3mVNtBAsk1X1iWyhlBWeaDeVYICgT1_qBFyygarM76NZY2kEmuxnmp9SkBS9gB5lTYNsWVEzKxJPPenSOBCUW6fAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه ارومیه دوباره پرآب شد
🔹
تصاویر جدید از وضعیت فعلی دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/654598" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654597">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGciVeHvKM4KspQWKd3EYGNQJVWwDDcV4iF2CKFxxrt4bI5tb97pq3EWm6zyGSi66GMBaxgpiqP12EXP4dCXpgMm_pwqtyf-frVB3cFBVlhSb2OL8qUrlKBsVCf8kuwCaZlHlTTW9t-2nBS8Sj4NJmdsGXhbtQ6Cm-u3nYBDpcQKqV5jkezxS7z4qf7zE13rCm02eyMxuQ9Pdk3jDuQEApjTpYCMKLWyfLmYRqlSJfhdtUQS5TwRYaFSu8P_woboA-pbnIAwGycS-HFq2QYhxyoWZOZJmkKpGcAdhZ9t51XOdRlQVhh-BGNZCuwjpVM2HddaX3xq0kUNdPImBEdLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صحنه عجیب، زیبا و تاریخی از غروب زمین در پشت ماه، از زاویه دید فضانوردان ماموریت آرتمیس ۲ ناسا
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/654597" target="_blank">📅 10:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654596">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db822NoSg8Sk59QQJUGyvQ7udphyMF0nZIDuyJ1twA2wWylRxQJbxN9jYOGbllsUetFOTVyYdf54xJEItu24rzZGcSWShWX4SGYHu4m6zK-aqBOamTeceoB6UeRl2xp7a-BqUxaPcX-UHt7OSSJV2m4NeF3BBdf0b4df8bfPfAEQ_c0gAp7cstAUyfh19ELqWDujzrsdoNZ8nQTOUA59oI3aRlJk8V3OF9iXj3E8APYIyxuma2tqQBm6nmjre-zGEACAhWq_xn5C3z2AKoUoMWlUvOk3GFXOAVAWYYLWvNv_-aOmE0evt9hh2LUOhi8YrN8_U8j6H5iR-zNivkqvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندار جم: یک هواگرد متخاصم منهدم شد/ هم‌اینک وضعیت شهر عادی است
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654596" target="_blank">📅 10:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654595">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
آموزش‌وپرورش: در همه پیام‌رسان‌های ایرانی می‌توان آزمون برگزار کرد
آموزش‌وپرورش:
🔹
مدارس برای اخذ آزمون‌های غیرحضوری می‌توانند از انواع پیام‌رسان‌های ایرانی با اولویت شاد استفاده کنند.
🔹
خبر "مجاز بودن برگزاری آزمون صرفا در سامانه شاد" تکذیب می‌شود.
🔹
فرآیند ارزشیابی پایانی نوبت دوم مدارس از روز شنبه نهم خرداد آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654595" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654594">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsWaFTCz_-7X2crblswjs-qdQ2ysqBT4sbzUWPL0PC6M5PG0sqyRAN7QLe9DFcxTZrN7A7p6WBwJjXZuM6Zp7n9sd1bjQJaF4WlYvjZR6OE1tEH8jPNKO7lAKCbWeU6VNnz0X0Dcgd-1pVxBF7Lz64Ywi_MAGkGDmvN_LXkFuaLT6vwPfPnw0qU5m7uXArQxWgeJcWcLsiIQp6tJ590ZCwpSmgzlxqV9udPfnLnMs0xSUi5uiIp1eL20F4-uyhti0KgD0N8ZJj6xwqtXmKbCTK8AlwxlRNFkA_0dsa1UsZ4Q8Hcy1BbrfBzIL6DNmLLRUK3Wl04dIjQOIqNiV2q_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استاديوم‌های میزبان جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654594" target="_blank">📅 10:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654593">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2f826a9.mp4?token=JlJLXpxBj5FbW-whlz4Xzz_PwzPr507kbAV30kiXGIMG_IQXSA9OR_IQrvUIv-Ssed33C0Ll7X_GZcDomGFALln0fFEKdkJEIJZaFB-lBjHeC97XZwJEXVcRgazcDz9tCoyGzZcq5Nyb_Musw-0-TiHEbijYMQx7M6UghxiBYYjKz11f-fo9TGWpx4w3CorIUs25iVln7gg4BJ1hD6jpeExByuIa8lr-eH1GH2TD4OOqlYsD-yij3oKGXuJ6VNnaN6sYK2ut_eZFd7JSRBEkHh_uIYl9fKWssacDHTRcri7CpU3RAlgCMgdCZuOzJ47dD2Rg34mNAZZNlT0hZlH6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2f826a9.mp4?token=JlJLXpxBj5FbW-whlz4Xzz_PwzPr507kbAV30kiXGIMG_IQXSA9OR_IQrvUIv-Ssed33C0Ll7X_GZcDomGFALln0fFEKdkJEIJZaFB-lBjHeC97XZwJEXVcRgazcDz9tCoyGzZcq5Nyb_Musw-0-TiHEbijYMQx7M6UghxiBYYjKz11f-fo9TGWpx4w3CorIUs25iVln7gg4BJ1hD6jpeExByuIa8lr-eH1GH2TD4OOqlYsD-yij3oKGXuJ6VNnaN6sYK2ut_eZFd7JSRBEkHh_uIYl9fKWssacDHTRcri7CpU3RAlgCMgdCZuOzJ47dD2Rg34mNAZZNlT0hZlH6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه ترسناک در شهربازی تگزاس
🔹
۸ نفر پس از توقف ناگهانی ترن هوایی، در بالاترین نقطه مسیر معلق ماندند و عملیات نجات آن‌ها با حضور آتش‌نشانی و تجهیزات ویژه انجام شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/654593" target="_blank">📅 10:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vccwU-OTCumepWd7VrPy0eSGMrLh-THqHbAUcb6KcA3wCCWP5dgyNEcnOPUGd0ri597Y_ncybor0-j4sS1kK7mRSeck00YkxUJOPESXZ8JhB7-s5h5b-ar3dIz0U9J2GOi_3cslLrrqmJD-jJFmo8VnBwJ8X7PCDQ4Y4maeNzr03go5wa7rj43Re8LItCNcXhDOIphF7xY26pucHxwCeWIYGXojXTLwcNGotn2v0kU4DS2AYhMGE8mXNiwAaWn74m6p8lTvBeYevO6En4S8qDiZuynCWSyjLUjke_WUQYkJScfk2xOnETO-lgqxxTgPHxeL3k_wiUezQWcssaAFEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtL570j_O5GD_mWwK5my1rgEyHT11UVSy2IJgZ4QJvQ1lyNvAKf2nreJGjKHtKuj44-JqsN6ZloyYkogyY--mL5brlRyJhxe8JZYLURlKkGZaj-3dvptnbfrH0CyHh6KxSCNMutZunrQrf69cygqblnIHkSerHbwAR6e63zKefEdO6nmOYazFHwak0f5EGKDwD6rT98sGYg-AK8O0H54IEw3igV7P1PP4KBO4b_9JN9UZcxbg3O2c3Z7cotfyY_pknFMk6Vx200GvyADajiBhNUf3kUFFcC_LTqWC54b3r8NRhlhQu9JD5gsv5Zm1jpsVHNIK-PiOfB8AKDp-oY5aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناشناخته‌ترین بازیکن جام جهانی ۲۰۲۶ حالا دیگر ناشناخته نیست!
🔹
تیم پِین، مدافع نیوزیلند و یکی از حریفان ایران در جام جهانی ۲۰۲۶، تا چند روز پیش فقط ۴ هزار فالوور در اینستاگرام داشت.
🔹
یک اینفلوئنسر آرژانتینی او را به عنوان «ناشناخته‌ترین بازیکن جام جهانی» معرفی کرد و از کاربران خواست صفحه‌اش را دنبال کنند.
🔹
همین ویدیو کافی بود تا تعداد فالوورهای این بازیکن باشگاه ولینگتون فینیکس به ۱.۴ میلیون نفر برسد!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/654591" target="_blank">📅 09:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5859f60eb.mp4?token=dApMdQfV6leIaCkRGRNA0YIQhtZpL-aGi2d8nbPw-_LrIeRyA2dREhBD5Ho2SqCZXQs1XW-vDTFgXGdOOhNbUreiHuuW-PbXUsmEubniIza7bMC8ThCzYSZ01l-ICkBiiWUYWtRqRxrcr4ifYdsr5l9YKUUZomE5uuzdEHXaSCa4h15sL4EmKxTzH6gnGh_zB3ka4nZ0mwQFrinI4uiZeHJD8I7tyUenGusvLpXn6aJa8WO2rVmy6Efyu9waHcS3WVTwKzWULK-Ss6FDKe2QGXGVbuRxIsVCSGri2bJ4XYT2hchHXY4jNAswC1pqS_GS-0NVNi4v7rWKsNA5mWO4zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5859f60eb.mp4?token=dApMdQfV6leIaCkRGRNA0YIQhtZpL-aGi2d8nbPw-_LrIeRyA2dREhBD5Ho2SqCZXQs1XW-vDTFgXGdOOhNbUreiHuuW-PbXUsmEubniIza7bMC8ThCzYSZ01l-ICkBiiWUYWtRqRxrcr4ifYdsr5l9YKUUZomE5uuzdEHXaSCa4h15sL4EmKxTzH6gnGh_zB3ka4nZ0mwQFrinI4uiZeHJD8I7tyUenGusvLpXn6aJa8WO2rVmy6Efyu9waHcS3WVTwKzWULK-Ss6FDKe2QGXGVbuRxIsVCSGri2bJ4XYT2hchHXY4jNAswC1pqS_GS-0NVNi4v7rWKsNA5mWO4zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه عجیب، زیبا و تاریخی از غروب زمین در پشت ماه، از زاویه دید فضانوردان ماموریت آرتمیس ۲ ناسا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/654590" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82564870e9.mp4?token=tAlpahvCJoGIaShpQbuAKEnV6MzBAq-sxSeDoi4D76LchUEHjAYLV9flZ-e7HzjbJq93TTeICCRYE-1ANFTGWAJbArkc6ZZxr5nX9V74N5JSl_nc_lDgB-dctTYke0HKyaOtMQNscJwEuch4dnmmgrNA7bLLxtvv45KPtqkn2A1IVpd1Du1SDZzTm4OTHy7loIj4qLMqw3HJ_I-x-KkCKSXivw6SNSbMzqayp88t1r6ZpEtvkH26z-v2dndTx5r_y4yfK6jlihWXRQMlfy2WgDU7xsfGLwDqknz7PEpovy5bb0kz0kq4EfrZHlB71hHRNKg9YZc4QfQs1xs2eso10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82564870e9.mp4?token=tAlpahvCJoGIaShpQbuAKEnV6MzBAq-sxSeDoi4D76LchUEHjAYLV9flZ-e7HzjbJq93TTeICCRYE-1ANFTGWAJbArkc6ZZxr5nX9V74N5JSl_nc_lDgB-dctTYke0HKyaOtMQNscJwEuch4dnmmgrNA7bLLxtvv45KPtqkn2A1IVpd1Du1SDZzTm4OTHy7loIj4qLMqw3HJ_I-x-KkCKSXivw6SNSbMzqayp88t1r6ZpEtvkH26z-v2dndTx5r_y4yfK6jlihWXRQMlfy2WgDU7xsfGLwDqknz7PEpovy5bb0kz0kq4EfrZHlB71hHRNKg9YZc4QfQs1xs2eso10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از مجسمه‌های بادی غول‌پیکر یامال، مسی و پولیسیچ در فاصله ۱۳ روز تا جام جهانی در اسکله «سانتا مونیکا»
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654589" target="_blank">📅 09:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e24de456.mp4?token=DyODWx5WLB5SfarDZXESpk2xzMKwO8uT27eVqbxdGqAHF_vFtLPPsfjOoWvlo0K6ycqy8g5JQEIE6C9lQewPt9XuJbAc8Wq8sPAYgoiiaGbnMrwJVPz_QZibxFDm1MV0ULokZphfSewGWmBP-yfdqenjwoL6pyMkRVKiDhUjmlqlNSu1jMz1WQUTh1k2pvVfLF6z_48-s8EEtdv8VQuF9WJHFb7dCF1DKYcfgtWdhov6ggxpb5inGiMWnxG2-LR6skll32r1shPRZK34qKSSkbn-mmfT2cQaFKJPGUQO-PbQxu_APmYbQbi2OiaCXppfCLBHQNhDzUHT2incty1prw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e24de456.mp4?token=DyODWx5WLB5SfarDZXESpk2xzMKwO8uT27eVqbxdGqAHF_vFtLPPsfjOoWvlo0K6ycqy8g5JQEIE6C9lQewPt9XuJbAc8Wq8sPAYgoiiaGbnMrwJVPz_QZibxFDm1MV0ULokZphfSewGWmBP-yfdqenjwoL6pyMkRVKiDhUjmlqlNSu1jMz1WQUTh1k2pvVfLF6z_48-s8EEtdv8VQuF9WJHFb7dCF1DKYcfgtWdhov6ggxpb5inGiMWnxG2-LR6skll32r1shPRZK34qKSSkbn-mmfT2cQaFKJPGUQO-PbQxu_APmYbQbi2OiaCXppfCLBHQNhDzUHT2incty1prw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الکس یانگر رئیس سابق MI6: ایران در جنگ دست بالا را دارد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654587" target="_blank">📅 09:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سازمان سنجش: مهلت ثبت‌نام آزمون سراسری امشب (۸ خرداد) به پایان می‌رسد و تمدید نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/654586" target="_blank">📅 09:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df31a1411.mp4?token=k3SvlBsfsBVlhi1oCtvuD3zqVCyDIb6caxpQa7Vob-RHnfvTqWRm9HeFcTVavKgf2XFe3vsE-uD-qOlW4bPG2KUVXZ8qPTxY0Tb3AEzSZNpX8m8zpizhz4b-Wsf_6C5i7AT1OetIOtDXN_iRHNXOysbARMvObm5pr9chuHM4FIwcFqe9CvYb90wHWGXEXxOmKDE2o1FlJjJq4r9O-FOcm3a6ggdhvDvcrTW58819SxjhwaWVEVMPXqrFQUDZzgVBEdixOF0EGaTccv6I5XddaBIZlynIIjMXYFcRaRW0TSjk1iyBqG5EWOCvXaF4zZm0X8FhcTz46I014hUtGphnEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df31a1411.mp4?token=k3SvlBsfsBVlhi1oCtvuD3zqVCyDIb6caxpQa7Vob-RHnfvTqWRm9HeFcTVavKgf2XFe3vsE-uD-qOlW4bPG2KUVXZ8qPTxY0Tb3AEzSZNpX8m8zpizhz4b-Wsf_6C5i7AT1OetIOtDXN_iRHNXOysbARMvObm5pr9chuHM4FIwcFqe9CvYb90wHWGXEXxOmKDE2o1FlJjJq4r9O-FOcm3a6ggdhvDvcrTW58819SxjhwaWVEVMPXqrFQUDZzgVBEdixOF0EGaTccv6I5XddaBIZlynIIjMXYFcRaRW0TSjk1iyBqG5EWOCvXaF4zZm0X8FhcTz46I014hUtGphnEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودداری شهردار نیویورک از حضور در رژه روز اسرائیل
🔹
این اقدام ممدانی او را به نخستین شهردار نیویورک تبدیل می‌کند که در بیش از ۶۰ سال گذشته این رویداد را نادیده گرفته و در آن حضور نیافته است.
🔹
برخی رسانه‌ها اقدام شهردار نیویورک را پاسخ یک مقام مسلمان به جنایات رژیم صهیونیستی در غزه عنوان کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/654585" target="_blank">📅 08:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFf0aBRlK47q-vlgXp95R95Sw3xlEUctmW3kp6BCs6PjbRaxKPVyOClQFkmCio18e-fwgshIX_04is1rEjSpdzgzTfVX34ajMsAzCEQbPPo9Wd18e8WCaFYqHSvIWwrrttKyBInoOx9R7V_nJ8kLLXVizswGMOw9XM8MlewvnE7rDH3ANp0jlCij13SjNXt_tUsVwtFkH3vpmS0rpze3I_0NrY1LvdkOoHqOwLjfY3GEwk2QmVMf5nDdzczIwA5UHr8X9nAoGz1GdNXM5PojjOS9HulAF8po4GS-tl5hqTUL5wlLfeLxndyC-OI589fxOczdhj62sa6ZgnDCgOsMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران ۱۵ پله بالاتر از عربستان در جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/654584" target="_blank">📅 08:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo3es8sYo5830FAc0EKO7ZWrt374EYE5Y0fY2-xvrTRkhDMCjA3I76hBEL9UNyKpHRtMK9LSj5ujRodh8kIwgJ0t5UM8qXyPfznW38Tni5bkppYynMQcw4TjSWsXasmlfy--M6Fiqrk-mj005cmETnfbR73B_4u2SHDEkYqAV9KduFS0TrzfxlWS4ieyRNZ9OwxZ06sVOdcX_a3PD29DSpo2UR9LnfEN1kuu5Ty4I_FZWu1ZqU1Z2u9C2rsW0lJ6oTbFyWTpkB_9jGOsB4Thl7mJDM4RPoquyrAJnOxWdLEwtzhs1waVbEDPp6OXX_agMibOiHtd9jk8h7U8ynQ9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین با النینو وارد منطقه خطر شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/654582" target="_blank">📅 08:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
جی‌دی ونس: تعیین تاریخ دقیقی برای امضای یادداشت تفاهم با ایران دشوار است
جی‌دی ونس:
🔹
در مذاکرات با ایران پیشرفت‌هایی حاصل شده، اما اختلاف بر سر غنی‌سازی و ذخایر اورانیوم همچنان باقی است.
🔹
رسیدن به توافق نهایی زمان‌بر و نیازمند حل جزئیات فنی است، اما دو طرف به مرحله حل مسائل باقی‌مانده نزدیک شده‌اند.
🔹
توافق احتمالی می‌تواند به بازگشایی تنگه هرمز برای کشتیرانی منجر شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/654581" target="_blank">📅 08:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61dc42e1c.mp4?token=vnAbQQYh7q8zbRB6rAFmdh0gyzsSR-f3kXAVO0Dtw6XGs3pQvXa4XrxfTT2cQAPhMITqV6IcMLR6E9GANQOvCj5CJxsEMkCuU9Ge4buqwkw5BfoFRds4CEn42yapVanHR7kCt0Zt4n_jYZCjBnovtvam6ZksR7vQ_LmxYYduWhm1Y9IdcWJ6SzZt_30wUZMvQti8bHtIuyXgS3TXCzDUS3-DqE2jsS6ETCFZuVrXw5AE5GO6OpMJhofPkP3FD4JIp2GVxuN3IEwHG2X9HDpddkCgDC_kD0Jm9xPi5INZtIje5YVRjyRGRGIESHV1iO0rW54Kte0ikkEBfHwnausbeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61dc42e1c.mp4?token=vnAbQQYh7q8zbRB6rAFmdh0gyzsSR-f3kXAVO0Dtw6XGs3pQvXa4XrxfTT2cQAPhMITqV6IcMLR6E9GANQOvCj5CJxsEMkCuU9Ge4buqwkw5BfoFRds4CEn42yapVanHR7kCt0Zt4n_jYZCjBnovtvam6ZksR7vQ_LmxYYduWhm1Y9IdcWJ6SzZt_30wUZMvQti8bHtIuyXgS3TXCzDUS3-DqE2jsS6ETCFZuVrXw5AE5GO6OpMJhofPkP3FD4JIp2GVxuN3IEwHG2X9HDpddkCgDC_kD0Jm9xPi5INZtIje5YVRjyRGRGIESHV1iO0rW54Kte0ikkEBfHwnausbeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکست آزمایش راکت شرکت آمازون با انفجار شدید
🔹
راکت «نیو گلن» متعلق به شرکت Blue Origin، بامداد پنجشنبه در جریان یک آزمایش زمینی موتور در سکوی پرتاب «ال‌سی-۳۶» واقع در کیپ کاناورال ایالت فلوریدا دچار انفجار شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654580" target="_blank">📅 08:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOsKXP0svVSt5HuKNl95zWJhCLAk3aOWHgeXj7euuAhxztfxa0LvjQLBrwgj2a1q8rj14mgH3PwjtrmQmi0kKXXTWrVTVMQf8VasU9Mr-DmPm1k6jSCHNqEBZQAKDMKu_l6zj5KEksmtWn3vHbeck1GdvSutcv2C1tRSwrxdlFEYufenQ1qNoUBZKklrcO2SVOLHL-XSUFiMpe7KxsaAeb7Qc3oHF1y8gJ4RfHw20D5BWu2n0H7Yh6gav-NbtXi14SI5Sku9ql9rAqrz_rffTCKHg103Dfu32IhAtIGYDB8X8VfqZdXXxPRjwqRWIhkoMXXhbHJiGumwudv0FU-Btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: سیاست ایران گسترش همکاری با کشورهای مسلمان و همسایه در همهٔ زمینه‌هاست
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654579" target="_blank">📅 08:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d77c76ec4.mp4?token=A1yg65irEINtSihP_yRKA-06vndMJ4psffqm0cWLRclTWjkzEmUK9KWCCn8nYfTIbFNbz0VlU8Py4Ok289_pkTIsvKecWIb6f8xdcIZ9K8gzUGldu6tLlVrcfSni4imnO2Ppd7bSReTu9pcmSx7Z2iwCJOeM5tYP3_7quT0qMTPuhnsNZk4iCplh-eY1pee8iHGbSfPWcN6JnFuLNm7EAJ860H_ORqVksQPtRu-8qHRzTcgSukBmpwG2Pas9BAppyucqtmnUVtYI7S2kGSccd66p5vQaQ4hI3N0jpruCeWl_1pIJVT0i1QuwM4FvdtLMOItht52w53gsLSsGW1OU4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d77c76ec4.mp4?token=A1yg65irEINtSihP_yRKA-06vndMJ4psffqm0cWLRclTWjkzEmUK9KWCCn8nYfTIbFNbz0VlU8Py4Ok289_pkTIsvKecWIb6f8xdcIZ9K8gzUGldu6tLlVrcfSni4imnO2Ppd7bSReTu9pcmSx7Z2iwCJOeM5tYP3_7quT0qMTPuhnsNZk4iCplh-eY1pee8iHGbSfPWcN6JnFuLNm7EAJ860H_ORqVksQPtRu-8qHRzTcgSukBmpwG2Pas9BAppyucqtmnUVtYI7S2kGSccd66p5vQaQ4hI3N0jpruCeWl_1pIJVT0i1QuwM4FvdtLMOItht52w53gsLSsGW1OU4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موتورسیکلت برقی خودران در خیابان‌های چین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654578" target="_blank">📅 08:21 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
