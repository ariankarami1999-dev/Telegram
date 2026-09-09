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
<img src="https://cdn4.telesco.pe/file/To_ia5UqGf7zNHbw8l-MZOk3Np1Bl98jyI7iObfbfRug4ogc2JM-7o9Crm9YfqgzhSJiJUZKiDEBI6ukUWPOihpwHnw-EQt6FMRWTgPKFCJLWkae9kmSMhVRP9STiYZtk6ZtwMbVGm_JgqdxEAxyj_E5JZq1LFLs9Y5xFm5RQgVUFTClY9iypR-BXD8xZ_Ku5RN0GBQNodz35XwswwNoo7nSUgaHlSaPShtKM7akCq9g4jWkf4KWUZDN4kqYc2mvDmZhrc1TXeaB9qevninPMRn2d3rC8Ig3uFhZlvp8TCpF0TOfRFunhNrS8w3I4OxqW-3xj_phLAi0uS8lcpN9EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
<hr>

<div class="tg-post" id="msg-688595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b6a408ed.mp4?token=IxtbAoFuCxY9nviSK-TbWFwgI9EjcR4fzMoBIT9isNb2ljK5EcWuYQNtt981-N7HDh6qsRjmln_J-Oy4nB52tHFKB7ZMUuOlSkopB4SswWBtZK8-hz0Wnf-IGJV7socr9Sty4SI7-T4IUvzsM9CHC3qkOgYp2CRdSvwN4LjABdZy01iI8o1NMw3BHrF4cxyUwktrM390noszT7t80XyrIgHZbIGc_aGq5u-Amzy2YGPEd6ITTRADi1ANWma1yP6JlMCddgvIfAkiX5sbIXpHdaHG6Fsu2TN3I35ozCsRdnCSX6nLQSDsJGTe9bfvXzcQ-FixnVESLfnPe-UQVRBcyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b6a408ed.mp4?token=IxtbAoFuCxY9nviSK-TbWFwgI9EjcR4fzMoBIT9isNb2ljK5EcWuYQNtt981-N7HDh6qsRjmln_J-Oy4nB52tHFKB7ZMUuOlSkopB4SswWBtZK8-hz0Wnf-IGJV7socr9Sty4SI7-T4IUvzsM9CHC3qkOgYp2CRdSvwN4LjABdZy01iI8o1NMw3BHrF4cxyUwktrM390noszT7t80XyrIgHZbIGc_aGq5u-Amzy2YGPEd6ITTRADi1ANWma1yP6JlMCddgvIfAkiX5sbIXpHdaHG6Fsu2TN3I35ozCsRdnCSX6nLQSDsJGTe9bfvXzcQ-FixnVESLfnPe-UQVRBcyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
لحظاتی از تست آیفون Duo
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/688595" target="_blank">📅 22:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3cc34dfb.mp4?token=eE_USQfkYngTA-YgTwN4luUejn6PvRSkbEKqgpBCfYmYp7jPvLn3CUCUZm0kL0CQZ0rVr7f8L3DwXT7ApUVPfrn20k--e9Bz33c_ll-crFhoFuxpxNz6HFJWfH2WFM38v8NDcidwOjWyVvHC9ePhU2sz7MCM7wEMFXCefDVtRSE_pT4gEnMYjuhWgjEhUMZ-TetJ0N0t44u1PXhPIKG77YoUMRciBsp9h0u5Txo14fimbJ4Z9T-D9-t78EAxw0CWVCpa5-DOcwAEj2XKFTJ3x_sJImMSC0kUJBd1JVZhPwyh_la2dlrAevtianqN9uxU-ldf6oy5E07BiCVUEoV4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3cc34dfb.mp4?token=eE_USQfkYngTA-YgTwN4luUejn6PvRSkbEKqgpBCfYmYp7jPvLn3CUCUZm0kL0CQZ0rVr7f8L3DwXT7ApUVPfrn20k--e9Bz33c_ll-crFhoFuxpxNz6HFJWfH2WFM38v8NDcidwOjWyVvHC9ePhU2sz7MCM7wEMFXCefDVtRSE_pT4gEnMYjuhWgjEhUMZ-TetJ0N0t44u1PXhPIKG77YoUMRciBsp9h0u5Txo14fimbJ4Z9T-D9-t78EAxw0CWVCpa5-DOcwAEj2XKFTJ3x_sJImMSC0kUJBd1JVZhPwyh_la2dlrAevtianqN9uxU-ldf6oy5E07BiCVUEoV4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: «یادم میاد پوشک بچه‌هام رو عوض می‌کردم. فکر می‌کنید دونالد ترامپ تا حالا پوشک عوض کرده؟»
🔹
یکی از تماشاگران داد می‌زند: «آره، پوشک خودش رو!»
🔹
اوباما: «من تقریباً همینو می‌خواستم بگم!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/688593" target="_blank">📅 22:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای رویترز: پاکستان هشدار عربستان سعودی را به ایران منتقل کرده است تا تهران برای مهار انصارالله، پس از تشدید حملات آنها علیه عربستان، اقدام کند
🔹
یک مقام ایرانی تأیید کرد که پاکستان این پیام را به تهران منتقل کرده است. به گفته این مقام، پاسخ ایران این بوده است که «ایران بر انصارالله کنترل ندارد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/688592" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات میان دوره‌ای پایان خواهد یافت
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/688591" target="_blank">📅 22:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3ZHd3tKPyfdKmiMCq__OZ9Zd2gaovZ_OMpTy2HJCUoRDhG8KBokpNSYKwGHEdOlcTTg3F-Sw3UEvx5_YS9Xs3JKRxK7DOZhJVwhJq7L-VfwL8YuRtMtv6gBgoA4iCsCIpH5vT6FPEz6HBdi8jYAHNGr8Uea3k9xj9hxybxaBDA7gDi-RwK1ZfCC4JIrKE9-BXGtyZgy1gCJiYfujK429Gz7eiV8AkLFn4CYAPK8KE6N2zS5zCaQn29h6SJuKouW2a1J6F3QMbye2dB5umuI-s1TxkMFPRBzocUEdClj-6nkcGgkLspaYPUQrtSNk5p2sJn9HBL0lqfqGEF31scE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به شرط‌ها و شروط‌ها
🔹
سخنگوی سپاه پاسداران، شروط جدید ایران برای توقف جنگ را اعلام کرد. توقف کامل جنگ، عدم تهدید مجدد، عقب‌نشینی ارتش اسرائیل از لبنان، پایان یافتن محاصره یمن، آزاد شدن ۲۴ میلیارد دلار دارایی مسدود ایران و عدم هرگونه مداخله در توان هسته‌ای و موشکی کشور، شروط ایران برای پایان جنگ است. اگر دشمن خواهان پایان این وضعیت است، باید دست از اقدامات پیشین خود بردارد.
🔹
هشتصدوپنجاه‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/688589" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6b3SAYC8PbZcUxO3gWxUORWgCGr4RCa1evn2YvXYVZ5l1py55xxbBGyYRPrHmaWJ_hKEXySCX_AmuGjDW8A4KX1f1ph651FBcecggU5pCt_kbsmpWkPYGS4797IHMi36UbO-vtc01wscn-vVOPQCleR5JXFbTF1x0UNSDamYdwSAxE1soMRW-IbjLiifjHxZwxkOSPCUOgOCYp5Vt8bYiU09tedBAI1tNmyFIpL_bWarU9-H7QRrO5W7dagTO2cpukeGZR3a93zAttWI9ulR7OrWNKQiu0Qx7pO7MvzhpyNOGlJAiSlUn4QIlN6Gyf-Nkoo5FKnK2LNGteNRtK8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراتر از خرید آنلاین؛ تجربه بیمه‌ بازار تا دریافت خسارت ادامه دارد
🔹
تجربه مشتری در بیمه بدنه فقط به خرید بیمه‌نامه ختم نمی‌شود. طبق داده‌های بیمه‌بازار، ۷۱.۸٪ کاربران بالاترین امتیاز را برای توصیه این سرویس ثبت کرده‌اند و تجربه ساده و باکیفیت خرید، یکی از مهم‌ترین عوامل رضایت مشتریان بوده است.
🔹
این همراهی بعد از خرید هم ادامه دارد؛ در «دستیار دریافت خسارت»، کاربران به‌طور میانگین در حدود ۱۶ ثانیه به مشاور متصل می‌شوند و رضایت از این سرویس ۹.۷ از ۱۰ است. همچنین در سرویس «خسارت آنی»، میانگین زمان پرداخت خسارت حدود ۴۵ دقیقه است و ۹۵٪ پرداخت‌ها در کمتر از یک ساعت انجام می‌شود.
🔹
این داده‌ها نشان می‌دهد تجربه خوب در بیمه آنلاین، فقط قیمت و خرید آسان نیست؛ پشتیبانی سریع، مسیر شفاف دریافت خسارت و پرداخت به‌موقع هم بخش مهمی از آن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/688588" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حادثه امنیتی برای هواپیمای زلنسکی
🔹
به گزارش AFP، یک پهپاد هنگام سفر زلنسکی به اسلو، به هواپیمای حامل رئیس‌جمهور اوکراین بسیار نزدیک شد؛ این حادثه خطر برخورد پهپاد با هواپیمای زلنسکی را ایجاد کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/688585" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نمایندۀ ایران در آژانس: این قطعنامه مبنای قانونی ندارد و نتیجه‌ای درپی نخواهد داشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/688584" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1607b03a78.mp4?token=hV4yM_wyF3Oz0-I76bcKKMmhcRiiJKOD0G_buxoxM3ffhCawzG7clCxRxuTIvggqylDkGJiJcFQ13g1m5m0ABkOeLnWM8TpNWR_nG0rsIDaeEkpaW480tzDHRRrZVKdI17fsR3QW_nGrGRlICJzxWPeerIDyhFE-TCssb1wtwQrRDW9qfte61tfUuGwNLkzE53CD3pHhkUSvhNH8rH5wh83C6WHyBETiqe9IkMp4vxSGWep1fdBskrLb8P-Z6uTF59tGZe4KRK-YQ2cG7n4RUXaaPjzpL2rxXO8hfa3h2u6TXsTi2U8_9N9L_S6Odnv6XwRkL64SFecGWvDkB-qCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1607b03a78.mp4?token=hV4yM_wyF3Oz0-I76bcKKMmhcRiiJKOD0G_buxoxM3ffhCawzG7clCxRxuTIvggqylDkGJiJcFQ13g1m5m0ABkOeLnWM8TpNWR_nG0rsIDaeEkpaW480tzDHRRrZVKdI17fsR3QW_nGrGRlICJzxWPeerIDyhFE-TCssb1wtwQrRDW9qfte61tfUuGwNLkzE53CD3pHhkUSvhNH8rH5wh83C6WHyBETiqe9IkMp4vxSGWep1fdBskrLb8P-Z6uTF59tGZe4KRK-YQ2cG7n4RUXaaPjzpL2rxXO8hfa3h2u6TXsTi2U8_9N9L_S6Odnv6XwRkL64SFecGWvDkB-qCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به قطر
🔹
رویترز به نقل از شاهدان عینی از شنیده‌شدن صداهای انفجار در دوحه قطر خبر داده است. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688583" target="_blank">📅 21:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688582">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO4tA6LxLE_yxmxTftxLbNgb0NhDAreLIuZ4FfY4KHmCq4JhZY4XhpBQph5n8r19djjHWWqYxn93UHttUfWDbp2Bm8CJMWg3zW2ebKYgW2fKrPRV9Clm0pfhoboJEMWakSE91Q7zF03O-LHIU047UcrciY9qZvtIpW68w0LXfBAzSNrwk-b4puwGJyKKxyzQuJljXwZQrMWcNEyqrSpjXb1qJ8ao57nbjcJOC_en4_VnaXm3-k7StenT1oa5dHZrsj95Zw8UaeFj9ikl71q8MPddYIF7y6ULfrYQwsg43nKEqeaFaU0HDSm8yCVEuZJKE-pt95HyzB64Rrgl_EkLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیو آیفون ۱۸ پرو لو رفت؛ داینامیک آیلند سه قسمتی می‌شود!
🔹
ویدیوی فاش‌شده از iOS 27: داینامیک آیلند آیفون ۱۸ پرو همزمان سه فعالیت زنده را نمایش می‌دهد و حدود ۲۰ درصد کوچک‌تر می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688582" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJJe6N-1aEGfFpRY9vp_YvNvw8WZKY1Ek0FyNIzIWAm5JM9uGUaadEGtnvs1HHIwM2NubhjI9Qbl6sJ3CB6bTL-0ElD2jOLs6uzl5FspyjH5mI0Y-yqb_BZa7n1cKgpoXrAePBMQf9mkA4bLKCictMIQO6yIGhhNMDo7A-UzHVwgKUjpT32zANDn34pUG1I-gF79a_9EzPAZeIqfot7oWNIs_CtTiIC0z3FOMyM5tLC5BjX4Hr89G_oMTsBEXFP71GDYK-I86IisgPISjQ0VtiAimJtAomYBT5IjdesQwLNXxznLzmK0QkMGuqYemFZgGCD2XAeOtpvHlBBJEkTkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSg1b76_yv8-sCVXPbiW7qBJpIeSLIUVO3TZ20-G1mRdipb4pyO8cr5xgFDPDqXakB6vJz1G3hr_UuS4W8-TTOerqxoB_59xW-hWiJ-kIUb39SzZ83d-fyN61WC0jXT1LYcFObnEmqfltsSJlV_pgc9uYkXODbOzvzIop6gKJd4Ot5dh58jsrodt0esPNDicFduXO-72jtex8FUmrocghKoLCJoe7HDwPM3QqBLT8QiOZtvI8gxw1Ct-r5rSzU_VSkwAD2OAMwNprOas2UNoty5RDSbwqZn0cUJfavSYDneIA8YY4FUWXZXwzL150xjnrwWOPdT8Ht-jj4W_hq5GTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSD6GCsnDeOsKpyc-niZpw54SErblxgL8URIg6UcW6V7Qj14DKZwKS3dC0Oa8_gwIUhBCv3mnN2RBrNHpyr54at4RX3OkldfevpVsfjh-uLWM-f1uZzwcr0VB5Awtdz8Ab6g3qwirjrNTpvLQGC7nXOrr0V9xsrmOGcgbXyaT9D8w0NTorQ3tkfC34ZpzRePtrZEi3VQM1L1D_6I3j3TFMq4mMYGPM_Nk14G6-xnv2itRbJqbdW0tHZ645bc5KTZDh5jT1n7sMFsf8r7WVnBfecN4-pl7TU4BrzCT6451dPh0HqvYkZ0Ce7ptAi3Tjd6f4ZZrJpsp7PlyEHtIToMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HX0R3ZDG2BI2jwtUJ1Iwk3KzmD8TBkPOqUt8q3mgeH7YFouD0VT_5pNBDhTecZvnqH676CLvCQbHmFYsuYISPVwXMvauz3Sxdp6rN6YI_BhjxPHMbFSI164_EOS9-2rWPIenuOgsEuIEAjDPbJ3yk4GyqcfS-OHX68rnc4rhdLuUEzynhB2rB6v0kx9yBTlpexzcQ1iuv1NFeUmP39YzD8VmwjaxLjz50UESpD8gGKBjbVbiiX-Xmw0opmwkZz2y0yTw79mEx--iA2h5r62aK7v8YSXiQvtoo54XH5sZM2-Kpw7UeOBKmLL7MlFNMDXx5B9cfaD31TAjSQTW6ribtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0HtrVCIp_w4Kk6i8e_cd4wWEnLwzF9yHxzgKDAZlDzc2JQVYkMHXy7MWB9ahfmN-tshbmmMxl07MiuksZYBV3LFrxWcvREbgc2cbFf4YXhb7EKuezl5bGjVG1GE3qc1uZiR9OGsI0U5LXKBaj83EyN23BRlRysvi9NoCl8UZ0XeYk2gbEzrOdr2f5JQ01zK7hI5mWROR_6YhVefvr4mV39qOVCtZbGSjn0tM3RI4byeV4FTNXNSQIt1MxEmu-uQp6SIMXyb9-YnGUBKGIEEfOvQlgS2AkVJnaowMTogH20yt-7YCNOXBEJ7qFKJSSy7BMgH9Ix7xESWW-o0aTFc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzR5dwwlHMR8GiVHPxmdxb_UFrG9FqJClC1bGKnZNsFktN9KH7G1NWG24Xw_7b_2YFn3zOe3nKxphwmGzgpDrjn3iAUlEVj-ewF2_Wllo0Zmww0fZZITVjEUanHGlvR86Vr1Z9XiWpfv8aL7YmjYZhewTXTv-pUJividYhLG1557o_RXR7WgOGVAt4Npw28g7vYyG8-NDMTHU0sZSD_dh1ntLH-8uKYaAU6YGxvFzDFDKyPlfKq9lxKvTuL0nx1edxIbceadWn0IaZz8tiTmzNf8Teg3OoHSwDDqGsCIQCCa1ISuzwm5C9TUf-94XWPHITXM41seBwLN92XYZ9ob1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzkD1gwIh_I5uA88zJjwT_VwvoiGVELJ14wkpmZXBOhLelwGFiUZoZ6M3YlooXf6FzhZBHL3vQyfK4ArTq5Q-1bX9K7bysIZ4jas03exJUMr7DUyyLJt4FQ1WCOnnrhCTCpfLwfRqXqoID2_-kk0b7CRbSLguVqCNSAYmaE6QlZwOfMELzE_OYxofnmltVd_CBnwBV7M-gYkj3uYVUgRg6oT0CTL9m2BLHliL2Nr1RmTc-lNFF2lmmv-dLEDEMzYKpCAa9LLqc8yOVF2eCF55tFmnrvCrd2S3EKSeEzWuAxfS-RjdQ28vvgVPZpaeANTdQhwjkii71q5UOSgWF8sTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nr4n-AHyjHuiXC1zO19atG3gY84x4ozeMEDfhinO8Dz8EknL8hnbA56RUtcnX-gxisCgNbKT1XtPbtqHqLMmeddg5HBRDNq_KzYUQ_xzODl3AoYLPVAuvUMu_nPX3UwycHElVtbu4356bEbZgYdU2Pdubr53s-BA9cxQE5jNVhJpvY2WMZb8keE3GmO0jL03CZD5PW41CZkaB8_Q4iA0CpLHobGhTUfekrNkzvGYnIA3urhdTAk05od00ezKAKjh5tea1m-pZKRTVHCPTMycXe3H0_u_aLR3jDboZ2mEaKJX5PC3Djq8JYgvSTGqE1Kjik7Xyt-APMIRV3IaZhvQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTlwZ8lAoIA2qSq1_2eCiLUA7s8T_qqbWtwTICMtTcWOF-AX8YUOw5mYbWWxvHhNBAp3H8qF0Xa-eSYUxhR3RKKZWktu9P3UYUqm7HL9EY7S-ccNGrKcs4LxhNg8ytclnHIJ3wFl1pd-nMKnPLxw5iqfMM8KmdugncHf42yb9VnciXU95NQYLZe-pc87yhe8bELMrIJdRe_9rJvOcSJVVynWkFOXAMA_ssJSKDN4X2-TESRVRCNLsqou4XbbxbxRNHSRMRh5ETwks5k97J2j8jY3AVzLqvgEQeO89IcrCYwTYGHW6O17kJeAiJViyc89xFprvpxvI0HmqWkpMBeWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iP-sifMaXr2O-2FUyODqCxjZOIwZS6622tWXYsArpDP7LtweSvLH4Snv3eVkv3z-EzO3-JI2xBlz-8Ee11MFRHuUIQVtvtfxlKQCDZP_JgG4YhbPyHYETDoZF92Ot-RXDo_UMDGjYHU6xDmSuICxb7IukgCLc2KnLu1yEMdlfIuyzZljHH6ZuvYaOIG1vGX513TgUuYLqJRHbvhfc5fAJzA6Depa0iTha_ieEmj0xPU8j9m7i1sDMj97-N8YG4I9ohAIjvCdQF5emLS8qP-shBaK-iZACeeXTlRPKCmE1kkjHwfQ7dE2DSDvemlnRMlzsEh8Sy1kBVX6etliblxA2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
صدای شما؛ بازتاب مشکلات و چالش‌های خانواده‌ها برای ثبت‌نام و خرید اقلام سال تحصیلی جدید.
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن کوتاه ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688572" target="_blank">📅 21:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPocYP01sKVeR-yl8NzvixaJccKbWpjgM2_b0solCXukcv0jek_Wjdu7v9qCwd8AQUT5YN3b7gJ40YFSQ__e1OGX99OZlU64xP3Wea0uzxSqci39KsPSlJb1GbcV7fqekV1v7A8hcfWYNnrfuj8CganXKtl0j0j5JpX6xrALMEKDCp7AA18_e00ERX9rZrUUvAOu5BY4aNRtOpmTlYQld8omIEYzxgG3HISDTyN3YS1lwjSqJHXl8DLyVAchrF0wAmtxlIkhd1Yp1elB2aDFagn-C5AW-aimkjNy8ZtLAp-ulbNKUJitfCuTiFYkegYRUbcLWSarjcrFkD6ND1XvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار میلیونی اضطراب | از رمل و اسطرلاب تا اینستاگرام؛ رونق جادو و جنبل در ایران | مردم از چه چیزی می‌ترسند؟
🔹
رواج پدیده‌هایی چون فال‌گیری، طلسم، رمل و گرایش به پیش‌بینی‌های غیبی در ایران امروز، بیش از آنکه صرفا یک باور خرافی سنتی باشد، پدیده‌ای بازتولیدشونده و آینه‌ای تمام‌نما از وضعیت زیست اجتماعی و روانی جامعه است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3243482</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/688571" target="_blank">📅 21:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو کودک‌کش: ‌‌متعهد به‌سقوط نظام ایران هستیم
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688570" target="_blank">📅 20:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8edb534d6.mp4?token=LXsw-uMWn-OdZAgLKk7vBaTLCHGg1QcCEIrROegEtHa-5kPJW9cxU8NZ3SPmlYf_NldDXlPXuXNvjHURgrEBsU-kp48LoMtrqYM4RInwSdSE9ap61rVSxueMqG4MCIvyI1allzLbwanoHXK-ougzo1u6HXqXV2nLWigzllf1LAj1Y29bQiF61eVYHV_IEjmbJj_Jr6hQ23snDQQIxQUxg-gE4wjvY3wRDEy03joNf40B6EKjowOYC698-LeW_O_EFuATiY8keubjzlx10cbxa-mRn5gb63HgwPaDF3iZOrf_l90bYZO-rvCcx0p4lpXe2VpmJA02Z4sioiHDMbgDJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8edb534d6.mp4?token=LXsw-uMWn-OdZAgLKk7vBaTLCHGg1QcCEIrROegEtHa-5kPJW9cxU8NZ3SPmlYf_NldDXlPXuXNvjHURgrEBsU-kp48LoMtrqYM4RInwSdSE9ap61rVSxueMqG4MCIvyI1allzLbwanoHXK-ougzo1u6HXqXV2nLWigzllf1LAj1Y29bQiF61eVYHV_IEjmbJj_Jr6hQ23snDQQIxQUxg-gE4wjvY3wRDEy03joNf40B6EKjowOYC698-LeW_O_EFuATiY8keubjzlx10cbxa-mRn5gb63HgwPaDF3iZOrf_l90bYZO-rvCcx0p4lpXe2VpmJA02Z4sioiHDMbgDJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688569" target="_blank">📅 20:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688568">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1620deb33.mp4?token=JYAasy5b1j5iodVQXF4E6-n9sYYzZk24Nh3K8C2oFx3ivmSttTUDUOL1HDlMGEKYAkbnjy0ntapYm81vAMvusYy7PbwenK0UN2DzEPaqyYjOY2b_0XGYhfhsWx6IcOnWD12s5fq6TN9Covsykkmfv7e63pRdpQ3nvflv3DZsWTZaTomg4mfCcpg83d2KoyeChRQssy1KEegtYfz3NOPS50cwwmJiLjD_Qco3xo8qLLXxHpdxXRSySqu_nlCi1zzzhHm73UjhqmWD6dVDPBfdim8eC14IU8aPy-22bgHf6oQ0I420eHWZmqqmJcH24udmy_iOrA2sJb6VOle_7T_Gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1620deb33.mp4?token=JYAasy5b1j5iodVQXF4E6-n9sYYzZk24Nh3K8C2oFx3ivmSttTUDUOL1HDlMGEKYAkbnjy0ntapYm81vAMvusYy7PbwenK0UN2DzEPaqyYjOY2b_0XGYhfhsWx6IcOnWD12s5fq6TN9Covsykkmfv7e63pRdpQ3nvflv3DZsWTZaTomg4mfCcpg83d2KoyeChRQssy1KEegtYfz3NOPS50cwwmJiLjD_Qco3xo8qLLXxHpdxXRSySqu_nlCi1zzzhHm73UjhqmWD6dVDPBfdim8eC14IU8aPy-22bgHf6oQ0I420eHWZmqqmJcH24udmy_iOrA2sJb6VOle_7T_Gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رعد و برق آسمان دیشب ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688568" target="_blank">📅 20:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMMfdsJ2hrB5iL8jhSlfk3wRu5qfLezL2g8NyiUzQo_xdQIkY68-2hjPioKmHQU71zMGpFprdkogKtw8I036pUVh9HiFNx5NTEPbtt-bxD4yb_aCS_2cHblnzpF3wtPvRdoMaN9B0gFV8aN3F7HTpQ_m3p62ii1xANGoSKL-Cm3LyxA5Lo-mw8b-J5vHflfccd6vRsedl5vLt_ziGCEOlDr3Uv7O9IjS2Djha0p5JZOTcvS2kjBtlI5pbz8Cyn1HVEMs1eOw8RD128FysL9Mn6GZJ3BuC3YdxNQBVGQsUAJhY1IpU51APEw3ld6pFI9AkHVnLiO_XNtiz2JxW6wy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TydvU_ZhGdEvA337-3Yr7prM84ylJnf-Ig9wQ_a8A1Ofb39fnOG1uuxj7ArLPauil0BCd52L5MKhiGE8myghMQaY-LoAG5O5QUDTORuhn2LPT-AcgDvKk6-vqHWFurtdCBf4oCO2J44k6n_q-Ogy-X04Muw7zh1J3zSSpfvjphokKgcrTYD81gN7UFYvMYcIZcfPyY1jo_yulj4UTfXJbmJ4OCZ3UuCWt5JISubXZfAGTLbV6a7rv7URjFpSqSKrMX_aZ3IIpAp-dya3a3JIOQQyq7TVZ064nQomNo7MNDOrXd6eoxrMBNe0n9L4Cp877QyH-WNTtF9uphqdyzlgjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2MlS86gOx3ggTsNjHVhMwFXXVNLLFbAGBBUAysFSTzFosLU6s5JNYHuYgSNev4DU2NjLc12Plg5d6Wh5ucG8qGRXJVjbk76kaiIK7_eyyfyjAeg5Cm86aCGqNI1MjQ0PBOvfcKM0b7Ag2gdu1Gm33ktw5LaLpyvQqUD5kgBTaw_4CPoE2WrOmeSWd4JNDQuSDUNA38DKfqaADabRO9-jSi0oGmmOAS66G2XdlmEfzLldlDZ_I0GBCT55m4FCnqWly7G2kGA5TAeTCovMe7ok4coOf4bfObg4oCDoMCNuyO0glzYM6UsPs0dSHYV6M7Bej8-_0NJzq1qywBb-62asQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAIGZK6oE42g_LnyiOLD3vkYs-9UleKoSGNniNDh9ftuNGNN-E3UJtnISemNggqQdfPKXxNkWkLHR9X_FMEwQCRakMv3394oQzZlqiwVC_56xdH--VA9XEor27zjnFnk-W1tLD0RcmglA7H2N-Cjg4PP0jH-WSwsgN-mKMjBUS_O-LR4-4Rc-I5HObr4AIeWiiYppT4gv7nTxVZUs5Ct8FET2VoONqGHrbIkzEitMdYhxcRMy40URUZIdJQ5fKtcZaBsnRP4x-R1csazIiLZBXvJKPxjeyldOm97UtWwuaiCtywyKnfydCvZaSFb6zelERlqHNqcf5_1eMIKlMnwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqMO-h8OWoF1vpoKdSHUp6T5hwV1iz3J4121uhHBRJqb0VDoUJkkH5369pd31RflquYbdJ113SxGSUO3QZQWnQVuPo48Kur9Lke5XJLXHaPCIogCRmoy7PhyD2mosaIwrVajvrMJnfgsTUjh_2EoFNy0NULV3V9PF-uU1tq-pZEK7oeh8qZJr1-C3nBre955ogg01kHxo6j3eajnhCWsoObqpFHFUCMEzNPSmnOXmQzmnUGqp9r2YesvV0PC0TukTzYRrBunXnRyKs9WxmLuWrfkKDZThzlWX3wJUBsjGwDVu37WnmQie9Ob5XsitAuNCpRoqSllliwyYP0uT846Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCuFO2Q1-0DFDefA-2vZ_dIwckfx1VMmAnfkEUO_e4zbxM-k6L6kzGYC9ajd55CY4_oXTKRDTiXXgIGkN44vAPKCF7jlINKd6xSzE8N6uWXZfv_9KjgFt59bLeWBl-Xhl5AYwrn-u07EDszoiomTzRZDfmQ7MNX3_SG4ws4Aod4gt-RC5R4JXQ-cVeGXyrZ-jfpe4VI1s1CzvzZdRFk-f1z2LeZZ_YEfvPdrmIA8ubYEmMt7IRIA9YYr4UTgpk0hcrgWDji7a0PjcLUpFU1lDCawLeTST5I5lzRx9imVg_xwU6bYxegKspilcJzbloFvIoRzzxkFRn-Lz3feOGyw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUl_YbuBVMa1WyIWyOXO-mc5iik18WLzdvyuV0Kmj3igntGL1t22w8hKEKMcXMdmXrGulapkb7G_bYTLo3atkYJ_EJOHQo8PAyg-jVd8KKng8Ni5J391bMUQ0uVRiSlFUCc9-f0IRfRopCX9odD0b7ZiazXjSVpfLXEt7N3RsiOHSSrK8wnV5xGcTqJWKNgsPeDWShrBBDV0nFuZnix3wHhrKp51W4uoPncmsHKyQPrz5LHlrVPdYLutadSCEQcGuEUp7XBOa-MJko_31L3waIR9F667kJoyfMevXvazaR57Lchd1_yJJACwvYtgzPYAmyGeXe0uP-TPiprxURMA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYgCQt5m2y9-gkPtRmJVYQOJ3OOnNi9LM6Atv5PhduNmZ2WFQJ5XJX9u36MNfQGLP5bryRDBOq6NPgmbIEqfWwsTUi8WXJLNEsExgG6FK7IvSYSuGONkZea70GN_-RFvAhaR2VSfIHGnCEUjxQP1WKsKSQaa1wgp2P3rWcoDqkpikraVcgBRyvAhuw01WCxQyIWQPkxk5Lms5EQF5XyNmuzi4SNl-uyvi9P-Ht5PCXl1ISz7zPjg1Fgc0h4iacgh9rlG-XEt5_x8E5Au0uAMeQisPCOPhtiQnTOROGfAUY1nyByxlR8v0ZMbt7ALkX7L8r0IDXh7b17WQTxKUrvWPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
✨
هیچ قدم خیری کوچک نیست؛ وقتی مقصدش، گره‌گشایی از زندگی دیگری باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم‌برخوردار، قدمی برای همراهی بیشتر برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688560" target="_blank">📅 20:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7f2cZIGDmFxuTCLW7RSEEeMdwxeByRmMhL0Iff6y6XLT4cFRajaaw4k1kzp3V2bBKLYOuh1_puI-7FDd0QY1pqcIZxk4heDDLdxNzmbHs0rN7swnHlE9-puxGLPPqURWlKu8FPk3fk7zZMXNgEUvv2P4QZ-L0wP4FQF6rNcjyny5EXFy3zv1Z9t4aqLdyiQvPRI93m6w2wSf2f6-EiPLHYq0BLrTK-2Kmfl8bychthUvdAWlR5-QvEV3VopUtohFTs7y4LHAok6pMyh_Mj5_FzC3WCcfc_EoAM9ElTnri7Bycq4gCZ_zZpeDRLa_e_OCXLtXRl9sQIHrFgZvvNZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: به گسترۀ ایران، از اعماق زمین تا اوج آسمان، به زودی خواهید دید...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688559" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aab97ef7d.mp4?token=LjaIMIS0fiQnaNtd3316VVaoKV3_tyW5d3Lf3DSb0pnUZGdB_mhcAHc9MgMN_jvb4hENKFMuqCt9VK8D5MG5LtylhT1fJR1uvVAaHPVO5-ibik7NrvJP5VzkiOISjdzKEEARVoBwW_YKDIi4cNb2z6y-e-eTc_jH26mBpwh9yJMfEAggq_ibUrv4vkc0aNm2r63y7OwlyViLS9lV_1INjbUDrOmVtXGIVN0AL6ItY-fuyJOasc1qpX88FKIa4TNkIc1bfEIzi3gAAazqWVggI1ircIeke62u_LbET0szBoymXL3wGRngMR9V40BGIL_8h9VcMozI0BH2UW7n9nhspw8DOB5JajZG6EjFIchznqF41PcOBS2MxsBV4FIdRFdORYIuTryDwKpWBCvQH4Xd_GzO2-A7NuAeRt8_B00EPEtdGK7CZGWm7cqBHRY04phIldnOQ7ADmYuDnlvsymMatYY453X9LuqHHC00PG7gMmj7O5FhUcWhfyETJhz4XkLsVm_afiC5m4rY1qitmg1-iOcuA7oM13WGr2dli15G1U3yku0h2O8bHmuQFvGZPd7JllT1Cn5anPerBSSJEUBRv7VJyCRCCvhiLQRJacQrJd-f6teh7DustKM-CDukk9GYb0evcdsh8GIssg5EodkWJbhpCi_EbVdYms0r0ntUQYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aab97ef7d.mp4?token=LjaIMIS0fiQnaNtd3316VVaoKV3_tyW5d3Lf3DSb0pnUZGdB_mhcAHc9MgMN_jvb4hENKFMuqCt9VK8D5MG5LtylhT1fJR1uvVAaHPVO5-ibik7NrvJP5VzkiOISjdzKEEARVoBwW_YKDIi4cNb2z6y-e-eTc_jH26mBpwh9yJMfEAggq_ibUrv4vkc0aNm2r63y7OwlyViLS9lV_1INjbUDrOmVtXGIVN0AL6ItY-fuyJOasc1qpX88FKIa4TNkIc1bfEIzi3gAAazqWVggI1ircIeke62u_LbET0szBoymXL3wGRngMR9V40BGIL_8h9VcMozI0BH2UW7n9nhspw8DOB5JajZG6EjFIchznqF41PcOBS2MxsBV4FIdRFdORYIuTryDwKpWBCvQH4Xd_GzO2-A7NuAeRt8_B00EPEtdGK7CZGWm7cqBHRY04phIldnOQ7ADmYuDnlvsymMatYY453X9LuqHHC00PG7gMmj7O5FhUcWhfyETJhz4XkLsVm_afiC5m4rY1qitmg1-iOcuA7oM13WGr2dli15G1U3yku0h2O8bHmuQFvGZPd7JllT1Cn5anPerBSSJEUBRv7VJyCRCCvhiLQRJacQrJd-f6teh7DustKM-CDukk9GYb0evcdsh8GIssg5EodkWJbhpCi_EbVdYms0r0ntUQYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: قانون حجاب قابلیت اجرایی شدن نداشت؛ اجرای آن مشکلاتی برای کشور بوجود می‌آورد/ کرامت خانم‌ها در این قانون دیده نشده بود
🔹
پیگیری موضوع گواهینامه موتورسیکلت زنان ناشی از توجه رئیس‌جمهور به حقوق بانوان بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/688558" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc890f1a08.mp4?token=WDXO36vMIxPD6_Kmj25mCfAGbgnUrd-r6sImz_HizKx6DI4P1ZIPDb-MKlhFS4QKJA0enJpOV8NXHKFo12on24c2NTAzzawoU7mT3jSHh4_-mfjtomqaQFFN_-u2roan580Iy-DNw1tw_8QQ1jyRUoft33TYRHr2FuXZWjTS035kbXJSPcmdNWrsJ09l6noa8Y2mMuVIqUiyXbRxs7EuwYZPUz1ztuZTY28YWoY1Y0kFYkp3ZtTZJQqgjI3gkRrXTvnWnzQdzBCyGMnG8r7rTYTfQa5hZHK813MOzdtT2PPIoyOPdz6SA7Df_qqyyQMUoIkY7VGmha7cgusxtxZXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc890f1a08.mp4?token=WDXO36vMIxPD6_Kmj25mCfAGbgnUrd-r6sImz_HizKx6DI4P1ZIPDb-MKlhFS4QKJA0enJpOV8NXHKFo12on24c2NTAzzawoU7mT3jSHh4_-mfjtomqaQFFN_-u2roan580Iy-DNw1tw_8QQ1jyRUoft33TYRHr2FuXZWjTS035kbXJSPcmdNWrsJ09l6noa8Y2mMuVIqUiyXbRxs7EuwYZPUz1ztuZTY28YWoY1Y0kFYkp3ZtTZJQqgjI3gkRrXTvnWnzQdzBCyGMnG8r7rTYTfQa5hZHK813MOzdtT2PPIoyOPdz6SA7Df_qqyyQMUoIkY7VGmha7cgusxtxZXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیمو رو تازه نگه دار، بدون دردسر!
🍋
✨
🔹
یه ترفند ساده که باعث می‌شه دیرتر خشک و بی‌طعم بشه #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688557" target="_blank">📅 20:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXu_9RTc6i6UJUH75okBo7RC9PG8C5TH7N3phgKC3ml2CgREIIG7LYXvAzCRt0Rb9qQbA2xC1oIhsMp0zDekLTouA7k4tHofqzipPs8o3OyojnSBgcASk4ElcD-9vNTLhJl4WXQPqYIEFlRh_LMcsag-_4wUDDAx5mr1cqc5IbsvIzmZTY1d5HJqfm81t9UpzfofuW3tjt4StnKX8J6kq5A9skd9p8KUr-L7ZNB-CoT15PsoIHk7vSLHy9e5MhhYkcQ8uuUaJ2veYYs8r5Fz_l9Sxvh0nDfmNw11ztNM5qFvxwD5L7HIDgqvJD5ukgRbTvULJwTd61uRlRS5pIaBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب قطعنامه غرب علیه برنامه هسته‌ای ایران در شورای حکام
🔹
قطعنامه پیشنهادی آمریکا و سه کشور اروپایی با ۲۳ رأی موافق، ۸ ممتنع و ۳ مخالف در شورای حکام آژانس تصویب شد.
🔹
در این قطعنامه، ادعاهای غرب علیه برنامه هسته‌ای ایران تکرار و پیامدهای حملات آمریکا و…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688556" target="_blank">📅 20:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdf72d5b6.mp4?token=f-YNx7l_x5jp7zNPGGOYR8M08mbCYc36MbFPc-Ry7Mf6yQBdEa8XfuB5KQoet2kzy-B3u_zjjgUTogpK6BcD5CmSKiW3wp4SYBvZCWazFN-Or0xjhxji60weffyt9BjCaSOmgMgiR4YkwdpbdkmSOANopqXbSs1D0K1W05RqZ2rg-uaVikxc_PBKbO3TWM6590tgi9XAy8h8MbQILdnP2kAgUs7l9Wkv0NkwOkVpNaVeEGUCjxfOm8jzIdOxDzyNV8Dj00x_4QCZ3EtD6IQ-0EE4wo5ZjByou9E1HuFtDJWC9sJIuB-jUq6Zj609zOWNQoNP4wE9jj2HWeYDvQ10zSz-30dqA8Zj8R8ozhFlAqE-6rELbwM6tXm_zNrFNkE4l9SzD_sG96w6z7yRMvLBs4i_3c30VAltSaWcc7KNUnM1SE25kb_FcvI9_aPC4KIaLFIYEzVeJiyFBuecSULLw08lCQO5AZjNvLAsDD4g2xUxHo3_woPAQ2iKglOD07wwPUuTWfkwOVgObnIvC7CW8NMWIUj7n2tXX6sjKm1i6zAep8qNEwvECq-waTYsJAY7XpFEbrEZPYL3N45vphA0Gfhv_ErzsCseaIV-_4OZ57Yww8ZNtWwnG7h9dFj6hkqpijxvGQ6_eNlCQnUXx3T-kdA-xTTVkpXcXMaKfQ2oSRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdf72d5b6.mp4?token=f-YNx7l_x5jp7zNPGGOYR8M08mbCYc36MbFPc-Ry7Mf6yQBdEa8XfuB5KQoet2kzy-B3u_zjjgUTogpK6BcD5CmSKiW3wp4SYBvZCWazFN-Or0xjhxji60weffyt9BjCaSOmgMgiR4YkwdpbdkmSOANopqXbSs1D0K1W05RqZ2rg-uaVikxc_PBKbO3TWM6590tgi9XAy8h8MbQILdnP2kAgUs7l9Wkv0NkwOkVpNaVeEGUCjxfOm8jzIdOxDzyNV8Dj00x_4QCZ3EtD6IQ-0EE4wo5ZjByou9E1HuFtDJWC9sJIuB-jUq6Zj609zOWNQoNP4wE9jj2HWeYDvQ10zSz-30dqA8Zj8R8ozhFlAqE-6rELbwM6tXm_zNrFNkE4l9SzD_sG96w6z7yRMvLBs4i_3c30VAltSaWcc7KNUnM1SE25kb_FcvI9_aPC4KIaLFIYEzVeJiyFBuecSULLw08lCQO5AZjNvLAsDD4g2xUxHo3_woPAQ2iKglOD07wwPUuTWfkwOVgObnIvC7CW8NMWIUj7n2tXX6sjKm1i6zAep8qNEwvECq-waTYsJAY7XpFEbrEZPYL3N45vphA0Gfhv_ErzsCseaIV-_4OZ57Yww8ZNtWwnG7h9dFj6hkqpijxvGQ6_eNlCQnUXx3T-kdA-xTTVkpXcXMaKfQ2oSRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن هست، اما اجرا نه؛ معمای برگزاری کنسرت در تهران
🔹
در حالی که کنسرت‌ها در استان‌های مختلف کشور آغاز شده‌اند، سالن‌های با ظرفیت بالا در تهران به دلیل مشکلات و محدودیت‌های مختلف، فعلاً امکان میزبانی از اجراهای موسیقی را ندارند.
🔹
این شرایط باعث شده پایتخت همچنان در انتظار بازگشت کنسرت‌ها باشد و مردم تهران چشم‌انتظار اعلام زمان و مکان برگزاری اجراهای جدید باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/688555" target="_blank">📅 20:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از دریا در جنوب جاسک
🔹
حوالی ساعت ۱۹:۲۰ امشب صدای انفجاری از سمت دریا در مناطق جنوبی شهرستان جاسک شنیده شد.
🔹
بر اساس گزارش‌های محلی، شماری از مردم ساکن در مناطق ساحلی جاسک این صدا را شنیده‌اند.
🔹
تاکنون جزئیاتی درباره منشأ، محل دقیق…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/688554" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14-1 Ane Manaee (1404-01-30)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/688553" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه چهاردهم؛ بخش اول
حجت‌الاسلام امینی‌خواه
🔹
در تقابل ایمان و کفر، برتری عددی و ظاهری سهم کفار، اما نصرت و هدایت الهی سهم مؤمنان [01:06]
🔹
ایمان در برابر سه‌گانه کفر، فسق و عصیان...ضدیت‌ نهفته در تقابل‌های معنایی، کلید فهم عمیق مفاهیم قرآنی‌ [06:43]
🔹
قرآن و رتبه‌بندی کفار؛ بالاترین مرتبه ظلم و استکبار از آن کسانیست که "سد عن سبیل‌الله" کنند [13:00]
🔹
در هندسه تقابلی قرآن، عمل صالحی که از دل ایمان می‌جوشد، در مقابل فسق و عصیانیست که از دل کفر می جوشد [15:43]
🔹
نجات از خسران، فقط با "تواصی به حق و صبر"حاصل می‌شود که خود زاییده عمل صالح است ]22:55[
🔹
تبیین سنت الهی "فی تضلیل"، و نقشه‌های اهل کفر که ابزاریست برای نابودی خودشان![25:01]
🔹
نقش انگیزه اعمال در پیشگاه خدا و تفکیک کفاری که راه خدا را می‌بندند از آنانی که صرفا از مسیر خدا دورند! [34:00]
🔹
شهر قم؛ خط قرمز خدا! هر دستی که برای تعدی دراز شد، بریده شد [41:19]
🔹
”قوانین مدیریتی خداوند” در جهان؛ نصرت الهی برای مؤمنان، آزادی برای کافرانِ خوشگذران و نابودی برای براندازان! [48:50]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688553" target="_blank">📅 20:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688552">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipyj8Nhi8i2s5bR9-UNVvbEsHhSpfnGxUEyx4Z7dBmzSC3T36zGemSbXBQl6V-Xx0CwuBEq6-KXLOvdwtN1ciC9WiQMa1Xwc70k5ATon-cylW6Jsji9iReQkFS5xYMWdQQaxCHC5uK6CzyeMJsB77IViXTiaLs8oqY5w6ysZO6eqCMipYdH2YqhSWsmvB7ABymjde-HeyZNxENLG8L6y-LX9ya0bgarvpJDhSDxwPUQM58ierY867Hy7IlnDpZcg0B9-jFupMKhSIWl_TBZPrlNXc3f1fxmmkn_CIfj5X4ABvC-KzgjCo8TWAsdcUdlAilmGbT2ZQrIRoTGn7KtMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنتی: ایران در برابر زورگویی سر خم نمی‌کند
رئیس شورای نگهبان:
🔹
برای مقابله با فشار اقتصادی، به همان روحیه جهادی و تحرک میدان نظامی نیاز داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688552" target="_blank">📅 20:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تصویب قطعنامه غرب علیه برنامه هسته‌ای ایران در شورای حکام
🔹
قطعنامه پیشنهادی آمریکا و سه کشور اروپایی با ۲۳ رأی موافق، ۸ ممتنع و ۳ مخالف در شورای حکام آژانس تصویب شد.
🔹
در این قطعنامه، ادعاهای غرب علیه برنامه هسته‌ای ایران تکرار و پیامدهای حملات آمریکا و اسرائیل به تأسیسات هسته‌ای ایران نادیده گرفته شده است.
🔹
شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/688551" target="_blank">📅 20:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار از دریا در جنوب جاسک
🔹
حوالی ساعت ۱۹:۲۰ امشب صدای انفجاری از سمت دریا در مناطق جنوبی شهرستان جاسک شنیده شد.
🔹
بر اساس گزارش‌های محلی، شماری از مردم ساکن در مناطق ساحلی جاسک این صدا را شنیده‌اند.
🔹
تاکنون جزئیاتی درباره منشأ، محل دقیق و علت این انفجار در دست نیست و مراجع رسمی نیز هنوز توضیحی در این‌باره ارائه نکرده‌اند./ فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/688550" target="_blank">📅 19:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
صادرات نفت عربستان از ینبع ۵۰ درصد کاهش یافت
🔹
بر اساس گزارش آژانس اطلاعات انرژی آمریکا، صادرات نفت از بندر ینبع عربستان در ماه اوت نسبت به ژوئیه حدود ۵۰ درصد کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/688549" target="_blank">📅 19:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688548">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er-Gh407ibCKcdGNFFdErJNBvsSzTZAl22hz9it89gW9SuX9XCzadI5OxlOXfRzHyDubklc5jAAPMx-FL-6PH-Y8yeHFcUvKRQcpc3OmlFjDM4_o05yOnLyK3Aiy-XvpIB5RVOWce1j6Np5K3XXemHMSOm-MqUyXTwNzcvEYG2pHCpEgZjpo7viBHgxwQZanS1mBxTEsAZ6tpWQpvNtI_fRdpEefbnkg-AckA81UgJ9FrkI14e0rkkvGHsYRj9HkyymMjb-AJxP5BBNnREO1dNi5BWMbqLLuNZ8T3SeD5kIrL_BjyysJmeOJfvFw7X0bDBUsdong_xposMQgXDBrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المانیتور: اسرائیل خود را برای حمله به ایران آماده می‌کند | آماده‌باش در تل‌آویو همزمان با اعیاد یهودی | فضای اسرائیل به شدت ملتهب است
🔹
نهادهای امنیتی و نظامی صهیونیستی در آستانه آغاز «اعیاد بزرگ یهودی»، ارتش را در بالاترین سطح آماده‌باش قرار داده‌اند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3243946</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/688548" target="_blank">📅 19:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a2830fbb.mp4?token=ffJHbQBbo2bePmUq8AboifN31zVbabse_Pq4zVPrACXIhnZsRsTk37gvrhmwODT_QkkdglE38xP3RyHRmSr_ZH9QKfrS7HVpJhemx9LEAy4pdvUP8ERp5sgT1_FqdmAzOYhgdRHRt4PjnVKHl-57yFBmd8KfuFYOdrnB6cglkzxuqcLQ_xoe0y3B6qZx-KxhxmdwhbVX1wJOkkAToPcXiKRClyjRjNe40QCYzjfxsMI4XISSyWhumT6lxh369pFq5IsFIyCgHP_iCxtD6GAy4R4UZGGEG7g4-pXZdc5jPF-HoU9KlxisARqH-KMq5gu735F3kMoMcFXHwdPz4C57AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a2830fbb.mp4?token=ffJHbQBbo2bePmUq8AboifN31zVbabse_Pq4zVPrACXIhnZsRsTk37gvrhmwODT_QkkdglE38xP3RyHRmSr_ZH9QKfrS7HVpJhemx9LEAy4pdvUP8ERp5sgT1_FqdmAzOYhgdRHRt4PjnVKHl-57yFBmd8KfuFYOdrnB6cglkzxuqcLQ_xoe0y3B6qZx-KxhxmdwhbVX1wJOkkAToPcXiKRClyjRjNe40QCYzjfxsMI4XISSyWhumT6lxh369pFq5IsFIyCgHP_iCxtD6GAy4R4UZGGEG7g4-pXZdc5jPF-HoU9KlxisARqH-KMq5gu735F3kMoMcFXHwdPz4C57AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ فرمان اجرایی تغییر نام دریاچه انتاریو، دریاچه‌ای که با کانادا مشترک است، به دریاچه آمریکا را امضا کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/688547" target="_blank">📅 19:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اقدامات فرهنگی-اجتماعی تهران در طول پنج سال گذشته چگونه بوده است؟!
اعضای شورای شهر پایتخت روایت می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/688546" target="_blank">📅 19:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688545">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c699dc9372.mp4?token=QT8xjcK1SPb3AD5P2ceYRKhcbdGHLONgTQxV9gpDliKVmOieqai2FXR9G_pdOEIvqPkC3p2AeOIo6Iz-cmxaeaFVKnMkDD-KxNlQ-a1oqZMejD68gO5qJmoaBAu7GhktZWkT9Zo0abCS2vVr179vMpg8NhnohlR60UVeqSyr8_Mgchdv9DrGsMbxY4L0-6mDDzHYa0gKTxopJto8LPL336ScD-NaaYOSYw-7PlXHD1jfumlwjcphDxVQIylxLRRiozXN5WGW7ZlyeE88WLIr6H-6XP927I_x6adbiVPaFHtfn7L3hH8exeAhKc-yEaTvLJqLyWJ2YvkCtomoAvLChg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c699dc9372.mp4?token=QT8xjcK1SPb3AD5P2ceYRKhcbdGHLONgTQxV9gpDliKVmOieqai2FXR9G_pdOEIvqPkC3p2AeOIo6Iz-cmxaeaFVKnMkDD-KxNlQ-a1oqZMejD68gO5qJmoaBAu7GhktZWkT9Zo0abCS2vVr179vMpg8NhnohlR60UVeqSyr8_Mgchdv9DrGsMbxY4L0-6mDDzHYa0gKTxopJto8LPL336ScD-NaaYOSYw-7PlXHD1jfumlwjcphDxVQIylxLRRiozXN5WGW7ZlyeE88WLIr6H-6XP927I_x6adbiVPaFHtfn7L3hH8exeAhKc-yEaTvLJqLyWJ2YvkCtomoAvLChg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مالباخته می‌زنه رو دنده ۵ و دزد جا می‌مونه
😂
🏃‍♂️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688545" target="_blank">📅 19:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3301d22639.mp4?token=lXc9_yLaaTWs0rgyt8q5toftbRe1urdYVFHKWgkjXeB-f-11CCZKlEaf_zlk7jo10IbuQbygGeNPCHw3wTY4is3b3zAsmNs-8oJEZV-ZbVGgTcrK9zJL2tnGzRfB9cJezFXR1kAqQ5-v4090cYbD45wlZOb11uMsgV5xGoQzo0bR-cXfeber-CEpI2Ge4nFVWk2HOqZnqpDnC7lzBBWP2z8SBn9hE6W4IFPKuRWo6W7blZKPyjA3r2LZznB_9ay5SR1ykG3Dr9lg9aKEN6GbRk_5BZNGq_SLLvLoQsfvUnqDaxlefl15a0oCFUqDAK7wpOyyVcoUJokhUNYQgVD-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3301d22639.mp4?token=lXc9_yLaaTWs0rgyt8q5toftbRe1urdYVFHKWgkjXeB-f-11CCZKlEaf_zlk7jo10IbuQbygGeNPCHw3wTY4is3b3zAsmNs-8oJEZV-ZbVGgTcrK9zJL2tnGzRfB9cJezFXR1kAqQ5-v4090cYbD45wlZOb11uMsgV5xGoQzo0bR-cXfeber-CEpI2Ge4nFVWk2HOqZnqpDnC7lzBBWP2z8SBn9hE6W4IFPKuRWo6W7blZKPyjA3r2LZznB_9ay5SR1ykG3Dr9lg9aKEN6GbRk_5BZNGq_SLLvLoQsfvUnqDaxlefl15a0oCFUqDAK7wpOyyVcoUJokhUNYQgVD-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از بالگردهای بلک هاوک آمریکایی آسیب دیده در حملات ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688544" target="_blank">📅 19:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ایران: اجرای عادی پادمان‌ها در شرایط فعلی ممکن نیست
🔹
ایران در یادداشتی به شورای حکام تأکید کرد آژانس نمی‌تواند با نادیده گرفتن حملات آمریکا و اسرائیل به تأسیسات هسته‌ای ایران، خواستار اجرای عادی پادمان‌ها شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688543" target="_blank">📅 19:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb6ace5a9.mp4?token=kMDIaj6CFo9IU1j_Zdmjg22o3HKV7qPAOQBNtr3fj6wL4jFt6KcFdponpVb0KONwbVBNsQmfvT49E-sHLDpxcU4uzG2SI4t5TzG4QsPEluV53tbTweS18wR-zKRClroQ9xv1PHqsxn7V-bVuEqRul9pf-XYVn1sDfPBB3GhdfYD8WBB9Ay7aYGi_fQWwJABXLhars8_b412bNnjeSSXRi-F1Nl0J0yVVn6pBL9zj0m85bBp2M4aOMe7fBdvk-OCEGkcMuq9cyHhK9iNrJ2ulP8j5fCYvgx1VKZY3scm8yy1WhMUufK-SVqA1XQthZ6XtiaH-z2U3a0007sHbhn8wTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb6ace5a9.mp4?token=kMDIaj6CFo9IU1j_Zdmjg22o3HKV7qPAOQBNtr3fj6wL4jFt6KcFdponpVb0KONwbVBNsQmfvT49E-sHLDpxcU4uzG2SI4t5TzG4QsPEluV53tbTweS18wR-zKRClroQ9xv1PHqsxn7V-bVuEqRul9pf-XYVn1sDfPBB3GhdfYD8WBB9Ay7aYGi_fQWwJABXLhars8_b412bNnjeSSXRi-F1Nl0J0yVVn6pBL9zj0m85bBp2M4aOMe7fBdvk-OCEGkcMuq9cyHhK9iNrJ2ulP8j5fCYvgx1VKZY3scm8yy1WhMUufK-SVqA1XQthZ6XtiaH-z2U3a0007sHbhn8wTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاسر جبرائیلی: شهید رئیسی از حذف ارز ۴۲۰۰ پشیمان شد
🔹
این ماجرا پشت پرده‌ای دارد که فعلاً افشا نمی‌کنم؛ اقتصاد کشور را به آمریکا سپرده‌ایم و با این وضعیت نمی‌توان با آمریکا جنگید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688542" target="_blank">📅 19:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بیانیه مشترک ایران، روسیه و چین درباره پرونده سوریه
🔹
سه کشور حملات اسرائیل به سوریه را محکوم و بر ضرورت پاسخگویی به عامل تجاوزات تأکید کردند.
🔹
ایران، روسیه و چین همچنین نسبت به سیاسی‌سازی گزارش‌های آژانس و اتکا به اطلاعات غیرقابل‌اثبات هشدار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/688541" target="_blank">📅 19:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سید حسن خمینی: اگر مردم با یک تصمیم حکومت همدل نباشند، تحت هیچ شرایطی آن تصمیم به سرانجام نمی‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/688540" target="_blank">📅 18:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6461051.mp4?token=rczZbBB2hxA3Mknu0qsutXs7oNjfo7T8DLQsK2joBWo4Pyo6IGg7etT5CeOHtKkC2tunxUJ2oLyMshuMgfHCEIPbEMuXobFSvS9jEfU7xXJfqAQbK6YfcpOXtY53Qt_aVPc-UYyaDLOLkQYLh0_PUqX_4oJZD1nvLaxtrhBICSUB4mO2Gks5fRLEVrSpUtUUcQCevv5rARCKJQnrB3Qh0Zr7rTxglNBL_Q_Rx4gONZD-w1O_LdP_o57KZgEteYe1oPlATovi2Squ1xJvF3eS4GugQI4K7WptW8DawhrQs_yq3V0A8gXQx1HSJV3bwDi-nVdmnGEcysr05G6QFsedYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6461051.mp4?token=rczZbBB2hxA3Mknu0qsutXs7oNjfo7T8DLQsK2joBWo4Pyo6IGg7etT5CeOHtKkC2tunxUJ2oLyMshuMgfHCEIPbEMuXobFSvS9jEfU7xXJfqAQbK6YfcpOXtY53Qt_aVPc-UYyaDLOLkQYLh0_PUqX_4oJZD1nvLaxtrhBICSUB4mO2Gks5fRLEVrSpUtUUcQCevv5rARCKJQnrB3Qh0Zr7rTxglNBL_Q_Rx4gONZD-w1O_LdP_o57KZgEteYe1oPlATovi2Squ1xJvF3eS4GugQI4K7WptW8DawhrQs_yq3V0A8gXQx1HSJV3bwDi-nVdmnGEcysr05G6QFsedYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوراخ کردن دیوار، نقشه سارق طلافروشی در بیرجند برای سرقت ۳ کیلو طلا
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688539" target="_blank">📅 18:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeZFEtBoc1Ov0doSTIo8rS0cN19w9Lr5d5p9pNlZf80jlCE9ndBM6SFh1HUUlwtIVDFuUxuNXjT5jEXQTC5sXQlgLGwg6NmtMpXqd2AoAls6MvtEMHpk7cposqgUeNjQ6zn6RymQ1KMoJF9C5VNJvDCYjYRiP8NNedM5Yiwwl74nnrc4bzu_9J5BK_eGTCVcq89bxisKf1bl174dr54GJr3roKjBl2IGaJlIHg0upF5LFVX7zcJItCxEJq5A0PtWeLLCorTjSmOiAl_vL7CH5Qdk8sIeQIb0qqNGZVJuKYpe22XrMHQO5sgOvwDvJhroPwn6tsoQGNaJP2OB0ALjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون برای ماکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688538" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjNSP3YHgU2W3VjuKKu-5AW2A5pTc_J5EENORTUAxZkhjWgD57PzcFG5P4rJawsjjwq0JMIrgDFVlxdCsW-Ux1jZSVQD8F9Xml3HS0AYq-hGTRG6zT6ZBwIC7gZpnxoww2eidSpibzdnefWWzIQHlOudHjqLv2IJlm9hPjw1ryAx6inZW9mbZstVbA332P0MSu_oIaySbI_w_bdBncNAQ0U1_09bXJok5ysue5yTMf7DAnKiVszkTLoxvmfCkylcLQZaBtuf0EciTbOBRYhudMYxra5ZXLNHZgn2hI0EJO0V__l87f7B_KdSX0k33yPzeu0IHONLxN3bjE-M6PUMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688537" target="_blank">📅 18:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab3de9162.mp4?token=ERhNlnHVvfvnlfc2LTF860LNH638WLWYVyJ6S5rlHPW3crRzuQOAvVUZuyg1fXCbeZBJRDynjYE-fBhFnfFCGfgYgzvK-T4VaQ4sprQNNAsxjQf_MAZdf1_anNDNps2h6t10Fr8w63ilv70XdJLpMR6Ch3IvgB92wIWrJkQoZKAs0eLfasG303D9ErthZK8JWbHiKDv3vYzroY0gE1X1XoDB2jof0CGRckgocKJT6Uk0T8brrqwNiH79Fhu3IxZ5yqGqrrQYMeKsYUFyeMJqQaauULqE1Na7nNCV4V2SPbJmMLG63EE-NVN_PfUJ1eCR3Ld-ob_aMGB6jqkOtsycyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab3de9162.mp4?token=ERhNlnHVvfvnlfc2LTF860LNH638WLWYVyJ6S5rlHPW3crRzuQOAvVUZuyg1fXCbeZBJRDynjYE-fBhFnfFCGfgYgzvK-T4VaQ4sprQNNAsxjQf_MAZdf1_anNDNps2h6t10Fr8w63ilv70XdJLpMR6Ch3IvgB92wIWrJkQoZKAs0eLfasG303D9ErthZK8JWbHiKDv3vYzroY0gE1X1XoDB2jof0CGRckgocKJT6Uk0T8brrqwNiH79Fhu3IxZ5yqGqrrQYMeKsYUFyeMJqQaauULqE1Na7nNCV4V2SPbJmMLG63EE-NVN_PfUJ1eCR3Ld-ob_aMGB6jqkOtsycyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو آیفون ۱۸ پرو لو رفت؛ داینامیک آیلند سه قسمتی می‌شود!
🔹
ویدیوی فاش‌شده از iOS 27: داینامیک آیلند آیفون ۱۸ پرو همزمان سه فعالیت زنده را نمایش می‌دهد و حدود ۲۰ درصد کوچک‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688536" target="_blank">📅 18:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
جزئیات طرح اسقاط موتور سیکلت‌ها و خودروهای فرسوده  مدیر ستاد نوسازی ناوگان و اسقاط خودرو فرسوده
🔹
تسهیلات این طرح از ۴۰۰ میلیون تا ۱.۲ میلیارد تومان با نرخ سود ۴ درصد به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688535" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMTjk2KBDFf5mYybxoJtnTb-TGT6ItSDZHa1qRFHADKnvDmh_5FDroSiqqPY94tUW3xLS1KMJTcdB-7exxl5LkI9kbYPAuEG2UsWKHFXMV9Rqnssq7aReu3BGRiUkNhCGqtD2jALHOn6W8h3X4UYxU-HhA72j3AUZbZSol_9OjiKhecdfD2tEkhIksPrJsT3hT5e-2m-d8NCq94jf2XHNDkDh7PPsYXJzA5AkyogEBuRsjgBU5AoZDhZc0miZZudwSkC68Vqy4B3eoGYgAtk86ld5x31cNYH1lzY2_zmpQLeJITRe1jgD7uVcQ36GTozctXD0gP9wlJTRpo7cmGt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به بیش از ۱۰۱ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688534" target="_blank">📅 18:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66489c4e4.mp4?token=VCD8QIRGUW4CFTaqkh1pkPwvISISYYsxPv5zEpeuxS4PiuM22FAh84SIL6shQvsioWxiZw234tkQGPPatWR7TCpOlEx4itFXsJRknNJuq04t6Wx0OXYzCk6QelIc47d5snSAe_DOf1XpgsSszVNCo6Zl6yTVqH7bp07Q097KaIh-ZtqAN6sYulUH2va9TzwEK_cbFo0FH0h1CLemeOtvaHaWls9wXicvqqdzHwmvJON6nA6wmHaJJLYDnyLtr9PySETuNj8beDdftj8TbHtAKHc5c9doOEFrF957waP4y_gUHFWFBBZ8BEUjNfhF4nzW6e9usOpMLwfRWkPssxf7Nb79_qYscsah7CkLfKdd2N1uHi4xfiPMYdP-ZlRBziQjcRNC-nyT7nVJCHJ34wrogn6JGeuLxG43Xb7tOGaAOhVb-aBrlYBOkHi_fPqZJ8ps0mHlqCN1Uve2mDh_T7NtzZbVz4qav-Je1877ljZ6DyO_xezCDy4nBIWRD-l9IUeQVvAHCo1i6leFv4IRlPRfb09k2IqNXD1DHRnSVAKgy5TQsGybrmsWrKO8DvlQGGLFt6mGDesorb6IHesknkqY_lBJANZCD7zM2jR4Rdrr6vRy789MMb2PS4y-X7TjeLp6o5OsN8XHYSQZO6Jwmfu_dUupzkhDMT2h0bDdM06iU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66489c4e4.mp4?token=VCD8QIRGUW4CFTaqkh1pkPwvISISYYsxPv5zEpeuxS4PiuM22FAh84SIL6shQvsioWxiZw234tkQGPPatWR7TCpOlEx4itFXsJRknNJuq04t6Wx0OXYzCk6QelIc47d5snSAe_DOf1XpgsSszVNCo6Zl6yTVqH7bp07Q097KaIh-ZtqAN6sYulUH2va9TzwEK_cbFo0FH0h1CLemeOtvaHaWls9wXicvqqdzHwmvJON6nA6wmHaJJLYDnyLtr9PySETuNj8beDdftj8TbHtAKHc5c9doOEFrF957waP4y_gUHFWFBBZ8BEUjNfhF4nzW6e9usOpMLwfRWkPssxf7Nb79_qYscsah7CkLfKdd2N1uHi4xfiPMYdP-ZlRBziQjcRNC-nyT7nVJCHJ34wrogn6JGeuLxG43Xb7tOGaAOhVb-aBrlYBOkHi_fPqZJ8ps0mHlqCN1Uve2mDh_T7NtzZbVz4qav-Je1877ljZ6DyO_xezCDy4nBIWRD-l9IUeQVvAHCo1i6leFv4IRlPRfb09k2IqNXD1DHRnSVAKgy5TQsGybrmsWrKO8DvlQGGLFt6mGDesorb6IHesknkqY_lBJANZCD7zM2jR4Rdrr6vRy789MMb2PS4y-X7TjeLp6o5OsN8XHYSQZO6Jwmfu_dUupzkhDMT2h0bDdM06iU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آیا وضعیت درآمدهای نفتی بدتر از سال ۹۸ و ۹۹ است؟
🏛️
رئیس‌کل بانک مرکزی یادآوری می‌کند که کشور
در سال‌های ۹۷ تا ۹۹ شرایطی سخت‌تر از امروز را تجربه کرده است. دوره فشار حداکثری که
صادرات نفت در برخی ماه‌ها نزدیک به صفر
شده بود.
💵
به گفته همتی، مجموع وصولی ارزی دولت در دو سال ۹۸ و ۹۹ تنها
حدود ۲۰ میلیارد دلار
بود؛ اما طبق گفته دستیار ارزی وی
درآمدهای نفتی امروز دست‌کم ۵۰ درصد بیشتر
از آن سال‌ها است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688533" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttdkJB3b6pBk8GGqv6ckmbdXZ6hGWL3PHgVahQmFQcDu6gtyqNHAroqeY22t0H1GpaQ43gF7NOF-Ea-UVz_e-aHyQPahSMOiEgzrTEngDUNbloi3dOJ3Y7c545LWEARfnptO7wbewKGAX2-3QLCBLy1JfN1fjXmi4qR0IoMBtCpazQ0LEuNVUap8Qm8-2NaS7gBRwAZb00ZcpUmsbybNVaiT__JMJpb_4qripp8jB_ps6PH00lkU5QgEMgI3-KKDYemagO2S-wLGrk7x_jCwsuEDMceX2yR1lW5AIHTTU3RzocCbRaxWW9F6VTpx2jeEE-maLaeWqv3JES2oZwsAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از سطح مبتدی تا پیشرفته این حروف اضافه در مکالمه انگلیسی به کارتون میاد #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688532" target="_blank">📅 18:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده شدن آژیر هشدار در منطقه خمیس مشیط عربستان سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688531" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نشریه Foreign Affairs: آمریکا نمی‌تواند ایران را خفه کند
🔹
با وجود فشار تحریم‌ها و جنگ، ایران با سازوکارهای دور زدن تحریم و ذخایر بالای شرکت‌ها، همچنان توان حفظ بخشی از تولید و صادرات خود را دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/688530" target="_blank">📅 17:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd1dc3311a.mp4?token=WWmpbTPujRl2944tMxF49WYg8y1bPfjwUfNGWwrc3AiQLC3GoCqVHApTxzZsMIuKJZPXiNTHXpiWpBUIDjph61wd9tuZx9YJpGX43UhuKGIMOAIQYhO36foh2eX7uLa-q_Gwd1J2dxYwdne-c412p0dUogxGnJuz0c83FxTPXChGOnPBRMmXcJO02IScg_vRpi2zz6Ilk-xkzpahEJvtHUzbpcFaVFx9JzbDpiNb_5BDDD_lG2R0Kg1wNM2g1JlrbI16pJQQ9FLvawz9jfP_5o0ZHSGr3jVUJh5dNROj_2YpD2Qjz3PmIIahkkOje9B9LRz2Ecf80WKCVLM4fRqFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd1dc3311a.mp4?token=WWmpbTPujRl2944tMxF49WYg8y1bPfjwUfNGWwrc3AiQLC3GoCqVHApTxzZsMIuKJZPXiNTHXpiWpBUIDjph61wd9tuZx9YJpGX43UhuKGIMOAIQYhO36foh2eX7uLa-q_Gwd1J2dxYwdne-c412p0dUogxGnJuz0c83FxTPXChGOnPBRMmXcJO02IScg_vRpi2zz6Ilk-xkzpahEJvtHUzbpcFaVFx9JzbDpiNb_5BDDD_lG2R0Kg1wNM2g1JlrbI16pJQQ9FLvawz9jfP_5o0ZHSGr3jVUJh5dNROj_2YpD2Qjz3PmIIahkkOje9B9LRz2Ecf80WKCVLM4fRqFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب
این روزهای افتخارآفرینی نیروهای مسلح و ایستادگی ملت ایران را پیش‌بینی کرده بودند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/688528" target="_blank">📅 17:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c1d39a8e.mp4?token=Kli4746PhG1OsPz3fx85rSpSqqjpLp4cZ4-2reXwQGrEFpIlrxSMz9LI3ICnFF9fGL5qD4kvnh5MntDcmf7lpFM1v0jc3gy3eLpozrfJGObPz1gCMatiBoS_ouasdbtJv1tcdEG5ij7TtTYmA7kei9JbK8_oHqWCkWzk5pNCvtIQwWJq2sjTA7haH72ex8jeN5B7DEXrZHBlCHWu5oQ-dprFeFsT24PMnRcK80PlaXi23EOcBNmB9n_Yc876yavgij3VWZgaihUIc15cC996gmrENDAZkpxteetVwRXS7HevROKM3t5QsovqcoqF6B8zGARC9NCtkWtdq16VFUnzP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c1d39a8e.mp4?token=Kli4746PhG1OsPz3fx85rSpSqqjpLp4cZ4-2reXwQGrEFpIlrxSMz9LI3ICnFF9fGL5qD4kvnh5MntDcmf7lpFM1v0jc3gy3eLpozrfJGObPz1gCMatiBoS_ouasdbtJv1tcdEG5ij7TtTYmA7kei9JbK8_oHqWCkWzk5pNCvtIQwWJq2sjTA7haH72ex8jeN5B7DEXrZHBlCHWu5oQ-dprFeFsT24PMnRcK80PlaXi23EOcBNmB9n_Yc876yavgij3VWZgaihUIc15cC996gmrENDAZkpxteetVwRXS7HevROKM3t5QsovqcoqF6B8zGARC9NCtkWtdq16VFUnzP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: حمله یمن به پالایشگاه جیزان، قیمت نفت را به ۱۰۰ دلار رساند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/688527" target="_blank">📅 17:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزارت نفت عراق: یک کشتی که برای ذخیره نفت کوره استفاده می‌شد، توسط یک منبع ناشناخته در آب‌های سرزمینی ما مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688526" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پاداش جام جهانی برای هیئت‌رئیسه فدراسیون فوتبال گران تمام شد
🔹
سازمان بازرسی بابت پاداش ۲۰ هزار دلاری اعضای هیئت‌رئیسه پس از برد مقابل ولز شکایت کرده و ظاهراً برای برخی مدیران کیفرخواست صادر شده است.
🔹
مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان و میرشاد ماجدی این پاداش را دریافت نکرده یا بازگردانده‌اند؛ نام تاج در این کیفرخواست مطرح نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/688525" target="_blank">📅 16:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای رویترز: در پی حمله به نفتکش «هرکولس استار» در نزدیکی دبی، یک نفر کشته و یک نفر دیگر مفقود شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/688524" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6786c383.mp4?token=FrMOc5YnnrWrW56HGE3xUFyEeSwuNxp1fCcrSleFsEjXveHmhrq7mnsCN1FcXs2QJEMrBDQDYAxbAUb--q_huFenWsE4YQvRHbS3-mAyUXLp1wvDyN1_kC3NETMcW3d2w7-578_zrTPGByKjsozW43heYL4BgwCCoROVbEeub-XhBAhrRwyfRodpkQ2l22w16q5x8b1eHQI-pu3LE7ShoHGG4TSaxXzjOq-eTMIddbCIvYg-njka5fAnzqxrrymoi38Q3ftN8CJNEAyS4jlpPPbmfvgxscjAH8xzxzTVCeBqaqhVnVJrU40GpckFuxdeL4CzB9EZIPUj_j6UVMmAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6786c383.mp4?token=FrMOc5YnnrWrW56HGE3xUFyEeSwuNxp1fCcrSleFsEjXveHmhrq7mnsCN1FcXs2QJEMrBDQDYAxbAUb--q_huFenWsE4YQvRHbS3-mAyUXLp1wvDyN1_kC3NETMcW3d2w7-578_zrTPGByKjsozW43heYL4BgwCCoROVbEeub-XhBAhrRwyfRodpkQ2l22w16q5x8b1eHQI-pu3LE7ShoHGG4TSaxXzjOq-eTMIddbCIvYg-njka5fAnzqxrrymoi38Q3ftN8CJNEAyS4jlpPPbmfvgxscjAH8xzxzTVCeBqaqhVnVJrU40GpckFuxdeL4CzB9EZIPUj_j6UVMmAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا دهانه چیکشلوب؛ نقطه پایان عصر دایناسور‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/688523" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آخرین وضعیت پل ارتباطی لارستان به بندر خمیر بعد از حمله دشمن/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/688522" target="_blank">📅 16:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آمریکا در فکر انتقال پایگاه‌هایش به زیر زمین
سی‌ان‌ان:
🔹
آسیب‌پذیری پایگاه‌های آمریکا در برابر حملات موشکی و پهپادی ایران، پنتاگون و نهادهای اطلاعاتی آمریکا را به بررسی تغییر آرایش نظامی در خاورمیانه و حتی انتقال بخشی از تأسیسات به زیر زمین واداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/688521" target="_blank">📅 16:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عذرخواهی رئیس دانشگاه سمنان از دانشجوهای عراقی بابت حمله‌ای که چند روز پیش به خوابگاهشان شده بود
🔹
تعرض و توهین دانشجویان عراقی دانشگاه سمنان به یک خانم تکذیب شد.  #اخبار_سمنان در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/688520" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym0ONy_iJF6PMYO2YcI1Vm3ch6MBPd0YfhXKyPKYGqIOhxUjjCzRzZosHmwGM00ZHHhXtWuDf1K5KFuT4-wykFu4rJkZsfCjKoM3pyGjVfh3_Dbi1UvwWRfCEoegBMuQE4fmvYs2xdqora1OlUQKqRLmkMh5gn-P_vGXO8tNqaxt7Tpoet565ngicgHSxXwK2iNw41kIVHwlNFWeT2sGUR2JA96_6BScPf3K2mcKjEtKdKvptnx4F4tnLGnFl7TlWNdNAWgrXbPDZPZ0RcTngdwjEw2aLiNPBpTq82DUAynNXSMoO2mnRhPCNEQJ0E6YQ7CAXZHy_13ljB8Q2lLCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جدید سی‌ان‌ان: تحلیل تصاویر ماهواره‌ای نشان می‌دهد که ساخت‌وساز در سایت هسته‌ای «کوه کلنگ»  در نزدیکی نطنز، که در عمق زمین قرار دارد، افزایش چشمگیری داشته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/688519" target="_blank">📅 16:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ضربات ایران، آمریکا را به فکر یک طرح پدافندی جدید انداخت
دیفنس نیوز:
🔹
پنتاگون در حال بررسی طرحی برای تبدیل هواپیماهای ترابری و سوخت‌رسان به سکوی پرتاب پهپادهای خودران و مجهز به هوش مصنوعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/688518" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c03f1eee0.mp4?token=up787YeheOpfFCC7MBqGSn07X5dhuebsgV0gzyfDO-ZSQWnOyR9vD_ptOTlKY9TkFHLvg2Kk4FNp7chC-h1IHgVek2wV0gVttnuAUVkaF8DySxb9C8nnO3HnnbG4DQGOZEjCukGYFygoCEA7Pk5Pvj3TiReDreUNjK70NF7pBjGJ9H9UbqosybhalqvMuxFl7qq1H4kmMGJ2cALxZ3mDp1ULjZX9ciOyAfKcwfGFOs93k_9WrH6quH-TFb6Z_nNVvgr6esWzjQi1JbptEUdbCd1AJIAQtAYxEZGwg_SsuNpJ8UzMiDEuwAuRhtuNBmJxFHXFUPosn3nLElXOI9R2X1En-rl3PRG1D03PWm4KE2LX9vZOf43FSgrWZbiwSlIT1R9SKeHAS9btgfDdfG574nRXd5F12cdmHSDqfTa8e2pjl-gFH4sJ7HA0wA6aquY0w_leOB5O7qGmWLjvYmztS8L4h_TDv1q3OppW_VhWIBWAmr38ouY-eVHcrrau1k37OmWROn31GFCggeDp6Q85uFIaTeQnI1xaXSXJyvS97HEhpfonZerHr6uKayg9etaWVQOHiNBeTaQkjMaMRZT4G8osZyg1jhcH2VIEFAq69h7bElA4URnYG6UOcQ9E5RVhD5Mbsj6TQbkSqsprbSIrdFnZxOOMAXjvCLmTbuYTJSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c03f1eee0.mp4?token=up787YeheOpfFCC7MBqGSn07X5dhuebsgV0gzyfDO-ZSQWnOyR9vD_ptOTlKY9TkFHLvg2Kk4FNp7chC-h1IHgVek2wV0gVttnuAUVkaF8DySxb9C8nnO3HnnbG4DQGOZEjCukGYFygoCEA7Pk5Pvj3TiReDreUNjK70NF7pBjGJ9H9UbqosybhalqvMuxFl7qq1H4kmMGJ2cALxZ3mDp1ULjZX9ciOyAfKcwfGFOs93k_9WrH6quH-TFb6Z_nNVvgr6esWzjQi1JbptEUdbCd1AJIAQtAYxEZGwg_SsuNpJ8UzMiDEuwAuRhtuNBmJxFHXFUPosn3nLElXOI9R2X1En-rl3PRG1D03PWm4KE2LX9vZOf43FSgrWZbiwSlIT1R9SKeHAS9btgfDdfG574nRXd5F12cdmHSDqfTa8e2pjl-gFH4sJ7HA0wA6aquY0w_leOB5O7qGmWLjvYmztS8L4h_TDv1q3OppW_VhWIBWAmr38ouY-eVHcrrau1k37OmWROn31GFCggeDp6Q85uFIaTeQnI1xaXSXJyvS97HEhpfonZerHr6uKayg9etaWVQOHiNBeTaQkjMaMRZT4G8osZyg1jhcH2VIEFAq69h7bElA4URnYG6UOcQ9E5RVhD5Mbsj6TQbkSqsprbSIrdFnZxOOMAXjvCLmTbuYTJSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی تمام‌خودران تسلا در تگزاس
🔹
تسلا سرویس «سایبرکب» را در آستین تگزاس راه‌اندازی کرده؛ تاکسی دو نفره‌ای بدون فرمان و پدال که برای رقابت با اوبر و ویمو وارد بازار شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/688517" target="_blank">📅 16:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
والا: نتانیاهو نگران وضعیت انتخاباتی لیکود است
🔹
طبق نظرسنجی‌های این هفته، لیکود به رهبری نتانیاهو ۲۰ تا ۲۱ کرسی به دست می‌آورد و نتانیاهو از افزایش مخالفت‌ها و درخواست‌ها برای برکناری خود نگران است.
🔹
کنست مجموعا ۱۲۰ کرسی دارد که بین احزاب چپی،عربی و راست‌گرا تقسیم می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/688516" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812edfda29.mp4?token=C-d_TFRzt_zYpESqPR8T3ZPSc6g2trdb-Tn384Nu_winRV3Y8yBJgw7RX39Zk1Q9SvP5slbaEkzUccyI3eE7XcnHcJ1y1Sx1IApULLiatAdMbW41-CO9UicwIOBib2bJuzw2-dRZqeCLe10D53S5FR_VkCP7r-g_UuomhqeIeMOEGkOJHJ7x8ZKqc0gfL_9Yj7zbbIZ0iKnULGp4QwDqRwDCOk--oqjV562BqSgcdXxZ2neTnsEhC3tN6q0HCecHKbpFUCUF0QzvQQT7G9Ny2K4erB-Abv3YXmCsOYAxbRWe7T0eTKHSF4Y73n6X2ioncTFCFE4b-mGvriTzB2HMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812edfda29.mp4?token=C-d_TFRzt_zYpESqPR8T3ZPSc6g2trdb-Tn384Nu_winRV3Y8yBJgw7RX39Zk1Q9SvP5slbaEkzUccyI3eE7XcnHcJ1y1Sx1IApULLiatAdMbW41-CO9UicwIOBib2bJuzw2-dRZqeCLe10D53S5FR_VkCP7r-g_UuomhqeIeMOEGkOJHJ7x8ZKqc0gfL_9Yj7zbbIZ0iKnULGp4QwDqRwDCOk--oqjV562BqSgcdXxZ2neTnsEhC3tN6q0HCecHKbpFUCUF0QzvQQT7G9Ny2K4erB-Abv3YXmCsOYAxbRWe7T0eTKHSF4Y73n6X2ioncTFCFE4b-mGvriTzB2HMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به خرید طلا علاقه داری، این چهار اشتباه رو‌ انجام نده
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/688514" target="_blank">📅 16:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuyIyoOW7GNcxeIVRLDfY8MYLHvd7uP4W992ICq6mEqRPyKaDmXiuRcBiYWANj_KOhYTTUyqT3GV37MZ0feo4MnZ7IZhT_hafDhmtxrRzjCBVb-IRyieR3PS3y-U80kKhoXQlvnOQQyDmp8BfJjZxQSnSBdRHdqbdDM8tayPBPVSUJVyua2q_GPswoJXfeX8y0udq7Z-_Kd2lNuYLgYG3IAqWYqKUQPAmg5pSdRUCsuoZoeUCLNuxGiD6PqFt3wO6vsh1_pNKfT5jYtiVBJ1ZEJxfjHlhBKnNxHiyaKyyObtlZd2jYatBa4UqEEdIhCQelWq3KvlEv9dVjp7Si3ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات ارتش آمریکا باز هم افزایش یافت
🔸
طبق داده‌های پنتاگون، تلفات نظامی آمریکا در درگیری با ایران به ۸۳۸ نفر رسیده که شامل ۱۸ کشته و ۸۲۰ زخمی است.
🔸
برخی منابع و منتقدان معتقدند تلفات واقعی می‌تواند بسیار بیشتر از رقم اعلامی باشد.
@amarfact</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/688513" target="_blank">📅 16:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiCAp35Gk8MBw21Rx9bONsHviFK3pt4xMPobzSneDpeATMkvqHdd5oIqwSI2Ngoi54lZtVeCKvv1k8ObBIfqUy2bKd9PzUG59cN8Oo8tR8kya46d2xqJpvz86e_YJb8frY3DKMTxZv6N9FHFSO6Y7a02EzwZISOSE7qB-JV9W5rR9zsCU6zCiJGRrFGK0EeUmwt8Nhn7y4FQjYnQjIaJkAadYr27kCZ1O5FVS0W1umkK-dkQl9emhvbKNxv-u_JwvnZeDJH9qgFMybhH9TuHzh18p8_de2G3vWpJdbCex6yj_1ElFbQBPyNZVvinOC59kymEcmS6tP8UuV8Zzh6_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☀️
💜
#خنک_ترش_کن
🍦
با محصولات تابستونه سحرخیز یه خوراکی خنک و خوشمزه درست کن، عکس یا ویدئو بگیر و در مسابقه شرکت کن؛ جایزه ببر!
🎁
💚
۱۰٪ تخفیف + حمایت از کودکان محک
👇
شرایط مسابقه
https://zaya.io/d2nr9
🛒
خرید محصولات تابستانه
https://zaya.io/ba5mo
🎁
عضویت در باشگاه مشتریان سحرخیز و دریافت امتیاز ۲ برابر
https://zaya.io/4g7k9</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/688512" target="_blank">📅 16:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8O9A5zpBvgxTJQ6SNB5p-79951kzjOVeJFOm9kIXr76S5W-JIlrnJ6U0CIhP21tuAat0SJaOtHjDp_JtLdoB5Ve4sJopl4pbOV2HrZdI6kMOZAGXp7S4Zh2W-tk7xRwfFUnbr9u2DUl0R59JntcjoV78ysu4KHTvsoh9mTwLlpjhF8XBAJ_NUDA1g1NYgsOyjYTLS_yHBqhq9VAHv8x7kiqjCaHYk-UonTazDIHM3Qztpo23DA8rRjQ8pyYGoyMaQfqDNLS7XpC_PYsEAfxq1EhTD7BYmMCLgtqzhwlA2_e7ci8fpZGbPlV0kBREN7UAxIsgZFt7bMTL9Fa56XVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/688511" target="_blank">📅 15:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695aaa457c.mp4?token=PJa6bOcXGYqp_WZ75OYU770Yubtxi9gT_qzkP_W6BSQgvjGHVYdAVOeEpE-W-Nh2Ryf8lubX9Souye-VHjLfeS7olRVYUSCTgAjXB5M15v89gr8nJw2FJalUg2vGmZUUNHmNX5WCwp4STTh7QYKxoj3enpE_5b4yPjuHANwBcciiaKV8czNHR06sh8Z9itUpgG8_eqdAIoMPJgyc0zqb8PhxvDWdjEwR9_-E5mJN3hxNjKadKExhXNR69czGKaq7st6UuWfm8uNQLiKO9y-_Zb0Bx0Z6_zKr2L_ICvrTkeavKXrJMjt81bK8fIORDukKqmAkz_Q7BnXcPEbF-lXKng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695aaa457c.mp4?token=PJa6bOcXGYqp_WZ75OYU770Yubtxi9gT_qzkP_W6BSQgvjGHVYdAVOeEpE-W-Nh2Ryf8lubX9Souye-VHjLfeS7olRVYUSCTgAjXB5M15v89gr8nJw2FJalUg2vGmZUUNHmNX5WCwp4STTh7QYKxoj3enpE_5b4yPjuHANwBcciiaKV8czNHR06sh8Z9itUpgG8_eqdAIoMPJgyc0zqb8PhxvDWdjEwR9_-E5mJN3hxNjKadKExhXNR69czGKaq7st6UuWfm8uNQLiKO9y-_Zb0Bx0Z6_zKr2L_ICvrTkeavKXrJMjt81bK8fIORDukKqmAkz_Q7BnXcPEbF-lXKng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو بعضی از فرودگاه‌های کشورهای همسایه، چمدان‌هایی که توسط مسافران در فرودگاه جا گذاشته شده بودن، حالا وارد یک مزایده بزرگ شدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/688509" target="_blank">📅 15:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما اصلی‌ترین علت کم‌تحرکی و پایین بودن سرانه ورزش همگانی در کشور چیست؟</h4>
<ul>
<li>✓ هزینه بالای باشگاه‌ها</li>
<li>✓ کمبود فضاهای ورزشی رایگان</li>
<li>✓ کمبود وقت</li>
<li>✓ عدم فرهنگ‌سازی مناسب</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/688508" target="_blank">📅 15:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d675398c3c.mp4?token=OrkRfBsVRxmVIRBEY1iXSUzwhyFmgH9nY1MsT5hlyj0kC3vp2Fx-iL3qtfWRc56y449hvslCOa0GxN5wvXBYtaUAZIysR2d1jjNexl56Vj0cVRWq6v008LqrPN8ehcpWy_A2qrcjS6sDE2o4-nBHHqx6iMDSUF6-huSVFkHnPIX-6LGBgIuvWgT5pYxwjKsNMZ-5JAgeyKBZ7jSKp_Hgh4xpSlBfzgr01mJV0-7Tj9ACemHQTptatxFlEKBnYJQYQv5VhfKxqt_LbpPjd9xaMDbFq0V07QVKT40oE-FZ7TLVUmWIiIxBX0GEjnCvOCmKx2s5GIzeQXyH9-PTQCk_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d675398c3c.mp4?token=OrkRfBsVRxmVIRBEY1iXSUzwhyFmgH9nY1MsT5hlyj0kC3vp2Fx-iL3qtfWRc56y449hvslCOa0GxN5wvXBYtaUAZIysR2d1jjNexl56Vj0cVRWq6v008LqrPN8ehcpWy_A2qrcjS6sDE2o4-nBHHqx6iMDSUF6-huSVFkHnPIX-6LGBgIuvWgT5pYxwjKsNMZ-5JAgeyKBZ7jSKp_Hgh4xpSlBfzgr01mJV0-7Tj9ACemHQTptatxFlEKBnYJQYQv5VhfKxqt_LbpPjd9xaMDbFq0V07QVKT40oE-FZ7TLVUmWIiIxBX0GEjnCvOCmKx2s5GIzeQXyH9-PTQCk_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی رئیس دانشگاه سمنان از دانشجوهای عراقی بابت حمله‌ای که چند روز پیش به خوابگاهشان شده بود
🔹
تعرض و توهین دانشجویان عراقی دانشگاه سمنان به یک خانم تکذیب شد.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/688507" target="_blank">📅 15:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhsVWNCPHgJSVLyV3Usp5FXvVizNEnQ24Ndz2na51n3XahfmGOCn2_Ca3c6d9Vc_B1wc1F4DzmTXXOE90Df9olbDloZmzr2nD2K-4H6RE2lG5b9tS4sm2JPWxuQJZsZ-OrBtBzsCZsDPFv2V3a4jUYlvYQAu-2YHGcOHxzf3AtrClbveGyoqTLLChjastETEO14sZpkHkAlpw0sdXuTpqf8xPacEQZEgde35EvnpunUDRsBEWaL0fPxGOM0XlgntPPf5ist5T322TxysmaNZ8PJ47P5XlDHwQI4JfwQ5Mhj8GR7RHSbYfSBB8yNsgd1gvxVjqYXmEI4Aqs3cQbpruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در دل خودکار چه اتفاقی می‌افته که فکرها و کلمات، سر از کاغذ درمیارن؟
🖊️
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688506" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از منابع آگاه: تلاش‌های آمریکا برای تدوین برنامه‌هایی برای حملات قاطع علیه تأسیسات هسته‌ای زیرزمینی ایران ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/688505" target="_blank">📅 15:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شروط جدید ایران برای توقف جنگ اعلام شد  سخنگوی سپاه:
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ۱- ضمن توقف کامل جنگ،  ۲- از تهدید مجدد دست بکشد، ۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،  ۴- محاصرهٔ یمن پایان یابد، ۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/688504" target="_blank">📅 15:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرفوری
pinned «
♦️
شروط جدید ایران برای توقف جنگ اعلام شد  سخنگوی سپاه:
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ۱- ضمن توقف کامل جنگ،  ۲- از تهدید مجدد دست بکشد، ۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،  ۴- محاصرهٔ یمن پایان یابد، ۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688503" target="_blank">📅 15:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بانک‌ها از SSL خارجی به گواهی داخلی کوچ می‌کنند
🔹
بانک‌های ایرانی به دلیل تحریم‌ها ملزم به مهاجرت از گواهی‌های SSL بین‌المللی به گواهی‌های صادرشده از سوی مرکز ریشه ایران شده‌اند. این تصمیم پس از آن گرفته شد که طی یک ماه گذشته گواهی امنیتی بانک‌ها پی‌درپی لغو و سایت آنها موقتاً از دسترس خارج شد.
🔹
بانک‌ها تاکنون با تغییر صادرکننده گواهی یا انتقال دامنه از دات‌کام به دات‌نت یا دات‌آی آر سرویس خود را دوباره برقرار می‌کردند، اما این راه‌حل گاهی فقط چند روز دوام داشت.
🔹
گواهی داخلی نیز یک چالش دارد؛ مرکز ریشه ایران به‌صورت پیش‌فرض در فهرست مراکز مورد اعتماد مرورگرها و سیستم‌عامل‌های رایج قرار ندارد. این مشکل در اپلیکیشن‌های بانکی قابل حل است، اما در کامپیوترهای شخصی نیازمند راهکاری برای ایجاد زنجیره اعتماد است.
🔹
تغییر مداوم دامنه بانک‌ها نیز می‌تواند تشخیص سایت اصلی را دشوارتر و خطر فیشینگ را بیشتر کند. / پیوست
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/688502" target="_blank">📅 15:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ارمنستان و ترکیه مقصد جدید ایرانی‌های متقاضی آزمون تافل
مصطفوی، عضو کمیسیون آموزش و تحقیقات مجلس:
🔹
دولت در حال پیگیری رفع هرچه زودتر تحریم‌های ناعادلانه آزمون‌های دولینگو و تافل است.
🔹
وزارت علوم پیگیری خواهد کرد تا کسانی که نمی‌توانند در آزمون خارج کشور شرکت کنند، پول خود را پس بگیرند./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/688501" target="_blank">📅 15:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم  سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/688499" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688496">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6l8n2x9EnubjJJF4gEukc1Io8qXeVgDTtbyh-pt9XM5tDon_UJ_PTwaRRRI_U3Ff0ja-j3bxkcJ00NkX2s02TZyGmKVFEiU09rZWJio8vs5gIJ08hrZuULLb0GCV3q6p-zSUNUMJz6pks4RMaOEjqrq4C_4vmjbo_E5ySGBtnqXVgfdOZ6dO2BOPO8o7Br0bC59XblhiL6Obc6DuGLGA1ieA3nSrHrZ1EtbQIuNGEIB4sw7qJx8fLiGzabtG_oC3PDFrGsBWJADhp6g7Nke2lfHS9C7055QFvUZS_-Qs2uOFZdB9wNVUMgOlPC84houaNvnDrH-cVJHLd9LB1LNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👕
از یک تیشرت ساده تا یک کسب‌وکار خانگی
🔹
کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ چاپ طرح روی تیشرت رفتیم؛ ایده‌ای ساده…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/688496" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688495">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
الجزیره به نقل از متن پیش‌نویس قطعنامه آمریکا و اروپا: ایران همچنان به تعهدات هسته‌ای خود پایبند نیست و باید درباره مواد هسته‌ای و دسترسی به تأسیسات، فوراً شفاف‌سازی کند. این پیش‌نویس همچنین خواستار ورود جدی و بدون پیش‌شرط تهران به مذاکرات برای حل دیپلماتیک این موضوع شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/688495" target="_blank">📅 14:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688494">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
واریز یارانه دو میلیون تومانی به حساب کالابرگ مشمولان طرح کارت امید مادران
معاون رفاه وزارت تعاون کار و رفاه اجتماعی:
🔹
این یارانه حمایتی شامل ۳۳۴ هزار مادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/688494" target="_blank">📅 14:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688493">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/688493" target="_blank">📅 14:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداد عادل: به‌دلیل شرایط جنگ، فعلا نمی‌توانیم آن‌طور که باید وارد مساله حجاب شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/688492" target="_blank">📅 14:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برداشت ۶۰۰ همتی دولت از منابع صندوق توسعه‌ملی
داوود منظور، رئیس‌سابق سازمان برنامه و بودجه:
🔹
رشد نقدینگی و ناترازی در دولت زمینه‌ساز بروز تورم در کشور شده است که دولت به کمک فروش اوراق و همچنین برداشت از صندوق توسعه ملی به‌دنبال مدیریت این وضعیت است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/688491" target="_blank">📅 14:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688489">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sO8v0MDF3QkxaMcows-Y7zT3YbbsAny3yx2geRpNvwYzWcx_AjLDQ4qI_jLfYz-6TVrkHIi8VVjKf7hUc_-zjqKuv54SgHedwbYLJZIB0-psQW0UNVmSlbYnKp_hNrb5FPxaIAxuBD24L8-I-IwL4hDiX07nl1B6vESc1flyGLSY4X6164k77XLWh2JgamiKglVsJzxtR-ABW0r_tRmTcfuLxAlJvI7L6BOhMHGNeCA38sRbVJNOOF9x5NMESAVnW9J6DDGjyJIil5mkwCpXWtuhKd-NKL2A-_XHDt6ZrortJFMEZNXxN8RIpoQAlOLmR9gUHX3E-GWJx_YCA0lMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL_8PnXZc5uOE96hW5nMbCUsvvngNMmgGUfocg82f20x6UPIwmHEwu10bDSKn4_2cUHf_A-VcdATjWY7sUHLowvgELFP7ZuPb_3egt77_0lYgdorpih1o0deMcXABTX8cccVpE5ShOyqpD76k5zUZaW04ypOpf7zBA3tw7WocgWaN6Ppt8iUJK3gR2R1VPp953OojIA-TASpib3Qx24U8ZF4PQdWZ_T_Cw9DmRylx1RnUmK06lL2vHmvpP8VSJcE01dsyiQM-NyTloFExu1MqwfNzW_tucDHVvkIGEB9qyJ3XcV5ox71ImE7NcN9ciUxzUrpKvILorAydplc8f6SLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این هوش‌مصنوعی مثل یک‌خواهر بزرگ‌تر راهنماییت می‌کنه کدوم لباس‌هاتو ست کنی، چه لباسی بخری و کجا چی بپوشی
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/688489" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688488">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎉
فروش فصل پاییز شروع شد
🎉
جا نمونی !
🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
*
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه*
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/688488" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPpkSPIhE8bMVj7W5GGJAgHjcMvqs53ZURGiE-H9eb-yVkELHpAxbXWOsLI16sHcFgwBq_QuWdGiGLjcSQeglQuH_XGHJI5GD7l_WlvBRR7RKoBSb_eaTBX_KvwhdHcEKcNDyb__fuQyHFkZwBwNPwZ4xa_Nss5Mi1vHfrp1BPDXp4nCYvBnfKU68Dp6p_oYwwLHjlEmNVPfClYwp88zPvDIMWGOtAtisUsWQNmALztzY_Z-9xEOxp9NZfQ0hvDsx9azxYPdmCiy6dOIPtInlr9Fl9TS4OT5jeHZ84IR-F5Mbk1jMyAYJTp0M9koTYaRFKKlw-_5jF-kR33IgkuXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhRzfWrVMoF4FQzZFMBr5_adkwwsD790Aq21FB8GI5f5a9MflfZYxo5f2j1TKq3bYYq604eYsBiqVKzeUHE2kwFZ-Bnm_l2M67gz617EhwwVRkCh6ugvW3gQBluKoTRWU8I3tuOXIwM1pVEKNsN42xovDLhsrUcJ7Q2P_oCR4HEIhbCrorR5DlLIk95D_6EaJOczCzZoXZrz4eIzYQORMz8oSiq5mGhk0tT_QkmZsclPKeqxrKbP25arYQcKmVU78K-qKgdAKHQFCQHombFDnYkNzsho6OnatK109BjktY5aO1I3K4hcHPH7yxmAnAYNLblTH_ShEP3_m1nzIuHDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBWRN32vSSWYImvAa9Q2Q4_3vQvX78EeaSyaEiqGXFl6sHZAHH-pzs2s-dwz2TTLZroAArVQlgGU1KW696p7LWJu1tJ-O34C1c2Jm2ZJaGW9GcuqS9wLrr8uC1v9Oqv9G7Uvi10jBGEUwpwMCH2ygJO1byzS9vUzpQwlbjxqiIgu0889ZGrEn1zNMEgEIBt9JSLSFffzdtPqOBQAHwV1AiDXdcfadiOSIw-qtLG7FqT-ypDiDDIDDcAirSTGRKbzuIQNC_1oT9AXY6rIbpb6EtNgM2ep9fDBrFN5L607_cz-NVnHfa5vE5bqPrrctP5M9H3tc4SsO2En52_1KHZ42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7GLaYOMAGJiM1pECX3FLSp809FdoK_BpPLdGPIjb1QnvpUcnH7F8bne_JE5bbH7bOFNhBcsyngbngvrPN_cv9jUqb42Htjnb7e2aFIk3RDhlYMrlTiR-aiv2_nQUgty8AD8HaHZbBZF6nZCtvfpGiCbcgm2I8mH9Sa-OTg60iG7dFeFQCLUu1t2YZLgKVmAsNCTA8OPR9W9d_1L-ak2fS2C0anHNVAvSE6BFGqjAyClqdbXzcNPXoGwBStgR7hhCWdfLdT4E8DftCWQYOMACq8Z6OYHlfzwXHOMhukIOkH287JTKDyCO_xFNcoWhge9LzOQGhSU-KZJFAEo5osT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usJMakPppxisIHpAsdC-bFwltodHjiPSzEH4Nj8d_AbcDPNsgfCkrOIv519KSUhFqu53ljPqDGEJLezXnqAOWlNuR7qtkCURdgpL4nicye-m9F8rKIo-R45T6J2Ffyof55XYGEF91MoLSnH1WukEr6MO7YWwFXSiizo37xKXJRNhfxeEVDfB2pL2vhMTvO3aFkvPykqDNQoyDdtNd04xfB9JYBzCMCcK214iwUI1qw67N7fF8T1D6dE8CSjwp_lvEgiy482PWF3hMlr6jqQwrxDY_Xk9mymtWYs-CrtTQUFVOVB2-ujleRude_n12EaIDhemWFPzjbeizRZC7Hkx1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
تجربیات شما از گرانی، کمبود  و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/688483" target="_blank">📅 13:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYH8O_kXsmRkvNQ9EOKatD8kuhjQsUBZ-bWt20WTFs8_QRLBNIkkVcCy3bibYaHa7wUiLr8gam9L-9BywZmBctn0XByEFk158wBUNmXJPIhVEWCs0rESRp3MhkFl5-ls_9JGevg_2mUpcJCIyZqQ1VPUBa3SW13-yt_UVCCeOe-NrGuNdvVuYJITSq9pQKySbMULSbJqq7BZY_eDeTSdhjJAte3lJibtTF3aCRP9X0m2NVP7FHG7Gfkw-JWr4VcUjIyOf-_3nSZFxg-Y1OLFZ9FSYi_fwhSRRIemK193UrlEiMjJWipHGZ9THWVYs4hisZcsT2zjDhKuQugijtcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه خریدار آپارتمان پیش‌فروشی هستی این حقوق رو از دست نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/688482" target="_blank">📅 13:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir_z5ixsZJjI3YMZCwiMbeUsfnXPRGjThKlrGimpjskhb7SEWBj71MPe6u6OwcjdI0_NkJZrW5vKbea351rGFZFPT3uAuN1LLgxdYwmmgS2pprI_JENr5Zo09lLNEGG-9iRwrDQiSmmqVwl21GhUBR9CDFQvet0UCbTcGgHK4QmtuJS75tDv5VxySEl4Lo_GwpiVFVFA0MwRirfLQgvaky_XbmxlsEMSkNpfeRwc7N6ZS1pcMaosZNmTV-qGzpYfTo79Vz8FnR1eeIdGfOrsRhi7j0DvAFVaPtHRMgbqevJAoAwyYwTcqDAbOJiSBFLFc6BLFzZD9SGycJUzPWgCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تعرض ارتش تروریستی آمریکا به شناورهای ایرانی و پاسخ دفاعی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/688481" target="_blank">📅 13:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای پنگوئن‌ها با میانجیگری کارکنان باغ‌وحش پایان یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/688479" target="_blank">📅 13:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعا شد که ۴.۵ میلیون دانش‌آموز هوش مصنوعی را آموزش دیدند
احسان عظیمی‌راد، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
از سال ۱۴۰۳ آموزش‌های مرتبط با هوش مصنوعی برای دانش‌آموزان و معلمان آغاز شده و طبق گزارش‌های ارائه‌شده حدود ۴ تا ۴.۵ میلیون دانش‌آموز با این فناوری آشنا شده‌اند هرچند این به معنای تسلط کامل آنها بر هوش مصنوعی نیست.
🔹
حدود یک میلیون دانش‌آموز و ۲۰۰ هزار معلم نیز در برنامه‌های آموزشی مرتبط با هوش مصنوعی هدف‌گذاری شده‌اند و در بخش معلمان این آموزش‌ها آغاز شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/688478" target="_blank">📅 13:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjOJ4voUSDfQG01LleCeAyNZhR3aTdBMvbtRLdyMCBTCzlu3hRb33SJojK0yMNou4CH5BdYZR_H-N1XDOZ1GjyWg1Gt-4aTNpQ_6j5EGnFhd42D2EsAHELdHpX7TJaMG_BXQGpTsQ4pKmMsNp-FhxfgJ15UZRomXZPmBf6r7bOmdv52sudF4hFdMBeYA6apm7xC2yJf_b7lijSVkRnd4pU7OIpUG6SsndL0FGnFPB06PNrjVfh-FgUjbD_LKTMb2Kyye06mjsBrX__-w0y7ngPN_0kvFEciBFyMmIBnrClhe3S7N-bFsTw4rEYkfAu-VRcq9FsUhp4O2X4wBlnuaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند
ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/688477" target="_blank">📅 13:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp8XKuYSI0lIwAljZH2cy-BYLfNRd7ipKBp_6CvRN-37r3prgBu6dKAb1X5IHZudkiU7WdXJif73kMTH836Bei29e7jcXXh04SQ8Gmp5dwSYFXvDqHs9PX6KBdV3QMiyf7LiwfX-i_mkREKj9AysptCGd1aA4BFXK6JIY0rKVRZIKDUDDoO-D8HHPUMYkchLfPJyOjz6HiVgVJT3ej8rNzoZK3C__nGcBdn58R6MFPBbe6PP7g_7l_M1PpFihahjr5QaQLS4d6r5dT7ntBpRhsazH9heB66uVjetUncCrz-5fDmMTjo3iebMiRnXUhekBAp0CCHNziAe31pUQSYfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا/ عبور بلندقامتان ایران از سد دیوار چین با طعم صدرنشینی
🔹
ایران ۳ - ۱ چین
🇮🇷
۲۵ | ۲۳ | ۲۵ | ۲۵
🇨🇳
۲۳ | ۲۵ | ۲۲ | ۲۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/688476" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم: آقای رئیس‌جمهور! مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟ من می‌تونم کجا بیام؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/688475" target="_blank">📅 13:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688474">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
«پروسیجرال» کنترل ذهنی پروازها نیست؛ یک اصطلاح تخصصی در ناوبری هوایی و روشی استاندارد برای ارائه خدمات کنترل ترافیک هوایی است
🔹
مرتضی دهقان، معاون وزیر راه و شهرسازی و مدیرعامل شرکت فرودگاه‌ها و ناوبری هوایی، با تأکید بر این موضوع گفت: کنترل پروازها در فضای کشور بر اساس تلفیقی از دستورالعمل‌ها، فرایندها و تجهیزات انجام می‌شود و همه تجهیزات نیز محدود به رادار نیست.
🔹
عبور شرکت‌های هواپیمایی خارجی از آسمان ایران نیز نشان می‌دهد که این شرکت‌ها به دریافت خدمات ایمن و استاندارد کنترل ترافیک هوایی در فضای کشور اطمینان دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/688474" target="_blank">📅 13:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بستری کودکان زیر ۷ سال همچنان رایگان است/ رئیس مرکز طبی کودکان: در تمامی بیمارستان‌های دولتی درمان بستری کودکان زیر ۷ سال که کد ملی داشته و ایرانی باشند رایگان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/688473" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منظور: ردیف‌های متفرقه در بودجه ۱۱۰۰ هزار میلیارد تومان است!
رئیس سابق سازمان برنامه و بودجه:
🔹
دولت باید سراغ ردیف‌های متفرقه که با رقم ۱۱۰۰ همتی، ۲۵ درصد کل بودجه را تشکیل می‌دهد و بخش سایر هزینه‌ها در بودجه دستگاه‌ها برود و از این مسیر هزینه‌ها را کاهش دهد./ تلویزیون‌اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/688468" target="_blank">📅 12:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/688467" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدن دنیا از چشم یک موشک که از جو خارج می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/688466" target="_blank">📅 12:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV57od2U2gohUp4BhThRb1t5dooTZppKjCC17j0SXXx3yxiSR9QZ660oAg7bwCdTv43kUvo-H5JpfsHb3JfYShZbpVQ1AR2KbgOHpEIQVPosanHVvRT03VUWbAAN7Ogq9a0tqoqv1VkaHieX4ocYR1e89Z8f_-FrJWyakGEVCVgLOIBnK3PkNhFVqZd8TjqZI506uk_wRl7BFN4QI4bnpCvlYXr8JKGE7Nmt727ipdmlBlSIh9mWjd1ITG4GXcIR7Ot1Kbt2JoGCAr9Wl4_49sJu-W7wa2alDsbqQnBYvknzVqSp-HO4zElIt8eW-j-SkwsP0TXND1c4G850gVGDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
پک ویژه «عاشقی»؛ نجوای کربلا در کنارت…
کربلا، همیشه در قلب ماست. اما گاهی دلمان بیش از هر زمان دیگری هوای آن سکوتِ پرمعنا و نجوای آرامش‌بخش را می‌کند. پک ویژه «عاشقی» از مجموعه «قرار»، مجموعه‌ای از چهار یادگار متبرک است که برای یک دلِ بی‌قرار گردآوری شده تا گوشه‌ای از آن فضای معنوی را به خانه شما بیاورد.
این پک شامل اقلام زیر است:
📖
زیارت عاشورا
🌹
عطر متبرک حرم سیدالشهدا (ع) حجم ۲۰ میل
🧱
مهر تربت خالص کربلا
📿
تسبیح تربت خالص کربلا
💰
قیمت اصلی:
۱,۴۶۴,۰۰۰ تومان
✨
قیمت ویژه با تخفیف:
۱,۲۱۴,۰۰۰ تومان
📩
جهت ثبت سفارش این هدیه ارزشمند:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/688465" target="_blank">📅 12:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/688464" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688462">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تجربه واقعی از پلتفرم‌های انلاین/ خالی فروشی یا تحویل فیزیکی؟
🔹
پلتفرم‌‌های فروش آنلاین طلا این روزها متهم به خالی‌فروشی هستند و مردم برای خرید از این سایت ها دچار تردید شدند.
🔹
چالش خرید از این پلتفرم‌ها چقدر می‌تواند قابل اعتماد باشد و آیا پس از خرید رنگ طلا را خواهیم دید؟! یک خبرنگار این چالش را انجام داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/688462" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688461">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی درباره بدهی دولت به واردکنندگان کالا
داوود لپه‌چی، رئیس انجمن حبوبات کشور در
#گفتگو
با خبرفوری:
🔹
بزرگترین مشکل فعلی بدهی ۴ میلیارد یورویی دولت به واردکنندگان کالاهای اساسی است که حدود ۱۸ ماه است پرداخت نشده و بسیاری از واردکنندگان با ورشکستگی و مشکلات بانکی مواجه شده‌اند.
🔹
واردکنندگان حبوبات کالاها را با قیمت مصوب وزارت جهاد تأمین و به سامانه‌های مربوطه عرضه کرده‌اند، اما با وجود گذشت ۱۸ ماه، هنوز ارز تعهدی خود را دریافت نکرده‌اند و این موضوع چرخه تأمین کالاهای اساسی را با خطر جدی مواجه کرده است.
🔹
با وجود بسته بودن مسیرهای جنوبی در جنگ ۴۰ روزه و شرایط نیمه‌جنگی واردات حبوبات از طریق مرزهای شمالی غربی و دریای خزر انجام شده و خوشبختانه هیچ کمبودی در بازار نداریم و پیش‌بینی می‌شود تا پایان سال نیز مشکلی در تأمین حبوبات وجود نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/688461" target="_blank">📅 12:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/688458" target="_blank">📅 12:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYVnkAFbi3Q9vJkxTph8cbl9a3TFJctGjPxtYSVqVeFirh_vOHBnIaPf7PlnVNDN19183gOvXVgdT8lsDGT9uzIhEiFcFOmiSSnypUPZrn3vlfKbo2pAFAOH20vv5cSwpPwKyUOkO9pbiRlwca1A7Zy8U-jWJSJcoiMzIofJ59DT-VttPAW1QvR6UW3swX1w-CCNm_2ERpaea7QdLmKrRgZl1fW027P927jaaQuYcpwMFLdcTowAjQgYI0Hp-Mu89v16hzjZdLP9Ly5GkMwy9jkoH9dk3O94g3Ij76xT0ZE2JU5KuEQ-7c7Fc4sBFke055m6lgeVGpBh0iPhyKcnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBM5AKnN38R9tPiH6qT0ADJdrW0M0nP-x_mqtvbAuXoSzQAAw8VoVOz3a2UV0YFmOmndDWYwAFKm68mD2GOlXJl8MFbnDMFxaq93yrcAa2BF6eoRQ6XsZ_eVrNg5jkgWwMq3P9s_EAEeyR_GRnArWOz7MmZgWAsEBRlJsG7LwidFF8S_hKKz_kqHZp-56aWtX2-fHNyxBNOHzzHFVpkqz0uTLu_0meWrfwSz0U_u8imu_GvQMQI8K_VzmkjLgNxDpGludLoEKCI8nA-mWDCdPJYB517wrDGPT4lhALgTFU_Uz2sfYsOj6GDjteRwAll_3P_uzL9z05L6vmcbsDQlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع معترضان مقابل سفارت آمریکا در سئول علیه جنگ با ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/688454" target="_blank">📅 12:21 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
