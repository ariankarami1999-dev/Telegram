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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfPi8-2vHXL_Hy1Rx8B2gR4Annc3Q9geBA1CONXFF1eakcGpp4sXfnLgQpMCH58MtrH1J8clR752c7WTIS7IgjzSTvqWaWr3XOWdB8RiH8EYaTUq9uL54rrVgKnuAYn8R_x0WO4ID0JA6Q7vm7MFB3eSmVBTcBJ7y1TkTSikt2N1QcermAs9usLRntcibi7QAMQh459uiF1mfiDi4yLDZzhmK4dLc6N2BZj16LvEoIfyldPpe5xaYZPt43uMprIlChBSTV6GZDFazg3NGLAQmJwUNY7AvKCmyjqjuAIZF8sraiSxRyd-ubamCVe-OFXdwXGP8WHqlGI_pEo3xBLOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Cyc13MIDvUdrH7BgynyC9X13UgbEDAxHPV9Z6JGvuvnpqA-GnXKzNzrOOkxatU5dGtvKxY_GVMGQSbRFsvRyKrP1_jfkat58tY32niTw7l60SJDpjBsmpcfHuSfHJJxsckAlm9URTQB2AqJROOejCFdZQ55sAnCqE6oLpY_1fl1Y1OcPDw3R0uHMuqlLuLrZK0AUZ-XnxAhr-MNPIGhPz_mTKYD6iRbisoP-_bZunK0v6DYMKgVKrEM0t2_Se36y4krAeea0W2nmvWPdfDCnPtla--cUtqQ-xRaLb_4c-FqQGsdt0_cQXM3C2GsmLgTVpnUEPDVygFdngUp-rP1QSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=Hk7s9KNwWOro9L9ShzDgUw1SBdrd4tTiewDf0-S55_JJnQDAT9CPJ_FkXUi50ZwqK5zaWI_Kwm8ZtWs3JA0IT-9Kt1vmpVjwoJpKvj5cvuHlYiH5A8j2Nc5Mdujg2vYRl7Wxk-BKvyxjXRrDoldUFnRv-oQkyAs5nVgmSYyQVVLeHIo_ojI_MUyl_LnfCvxWO-u6DpQ___rdBCCijAkf9EhxXhq3m6o5T4h4V5Kj_eQeBWdhscS9CAE2eRioociBw3JBNaaD81kZElbZti9rto6bMEWXdcMDVYwx0Ew7pRP2RRwVCkcvg6BDA_MucS5Xk-mklpDKr44_-FrEfxJaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=OjPUPP9WJpYLzmhs8jZhrTf7hB2LMFWPY8ckJtqCgfMDdm99eObJ5zRwfEX_F0E7PBetDSKyfurJL3LPXZbGxS2LDfB4ZIv5UFzj965MSxhKVuBa-xCsrnm3QQvCkhr85eRcOgKT9RXis17-ai_99waVxxNz-rO7C6SeMV4KrBa3UiqzJhElTXAVwpcFKJKnANI6JWDkvFaBGjzfLvUqWJwAaPgIiKrP1G2V6p6jNhr-pheyYSGC0xTTBzzyG2MktvwMGbrp2kQX_e70AEFwgVeMAfoVwm1ZAq1CKoCbQ_MXWUBt65djZhDh0nTWvedbzGp-EmZZd2SPt6DJ7HbtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=kH8Rjewd4tqZeOPqUhEzYsIeOH67hnZl246a0WIMT72IQb3vMPqBv0yTM4FWly4x3vXZ1Qkb1ULUuJKzCRXFEq1dI26pFTbw3BiWg-CKz9lRTO8HZi1YoWqCLBtzCEYa0bwEJ5u_UP7nymHYuTtkvJQLstcGnDcKqYhj2-3mfGURyzic7K2ld1CWGcoen6r-bj4O55DEFDNDyNs4720PGy_AH7E6GV6uQoxNIOFsbn28NgkdpQCb1uI3oUMfMoTTZsb58fLauQ-4eWqD8VSfA8_DbNXDtEluJbalpOBUsoCj_BPGUPxr79wmATk_AyXmFw6vFxaShcoBH4jqUA5VVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=HO7eIVlIvYyysHnhb0fzHOLHe98X-H5ffnaVLIgTpWrUWqZdKRrvSnP1P4v6TfTp2YuPJargybb1hciFEHCVwyHv2wwtlbOX8N-c7NvZY2B8Vo3S3U6n0KpySGWAYvG8XgtPmM1YhJL5XEdVFoKQHGOf8T9yD-QOe5k9nYqbhDR_WAMzc4KJGvgRvMGoK1RiAUPfJMWd0yQzhlFJClzgA3vnPuYwpRJaQ-WVHDdfj6mKli5U1PFBQ5HFoxigkyG-kfyJK5BuSEcLRaY_DydBcIxF8aQMrjXbUYEUKW-jyQkEzpo4z2Fghf0Tcvrv3EdaPeABlytzkuEPHXgmrNDnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA-RRtN9TwBOVJgKDXGyPG0jeDcz6XTBjKSeknden88zlzA66LtuAkcrdQH1TxGZC-rbdVAETqH9SjrseGXyaf4VV8MKZ1ej3tALsdu9jsPaY4LfOAV_i8KrqQMSOV5GUt9v4b-nInb1MNGPsA-LFDtbuA7pZTQfTgOf5vB_3nHBcFBD9xBLxQtTOiF3XvlTq01d6Jz3tWkdjd9QVxadUwJGTnjoWCPyKU0Ay39Nz0k-vweSQjr6H4C8u_mhIF309QiCh7ImzwPUikT9c0zxloWCHPCoWT9ZcSYOPHd404FN9D24eYFkiNQ4gKko1Uv_w21SHYQfZUWpzQGxIBYSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=i0AV0-S0J-vSm65yGhoC4Wm4b0zdl1tfmBfeOa1JnyGSjE9T8noxAvHxF3OkrUZzDtx-vZOCB-cH6vpSru17Gd6ccKsKhFtF7UaP0yQljXg6V1X0PZfjb1ZvP3G_-lGQkPTzhTLOxRQLb8rl8ZF4CWuX55R6z6sXpgZBBkaCKqzVEbhb475yhBESoxysjdAm5Aja2YbbPZVcn0NJt_Rglkj3yq1YXhkjRSrzAPBkBNM8Ig-vckf7-8bNEC2UhV8CBLeLpCVseicM60WSsKkirnN1tOhDQZfekW_4iKDR6xOGe4Qy0lf4lRShkeWUeqHncDUEFc7WlcsucBs6QWuHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxCw4tMQs0tT0yuoDn7xuMCG1w1uPoQbqre3ZN2-z0vrat87QBW6IQgK4DAi-W13WKv5zZ4O-IJ5Uy3V3U5e8W6l8m5GXzy3lCS__Io3mQFP2iql_wX2w6vlj8IsjZpvFyby_zazFsQ1q91AFg9zV0r2d3Si65nX49H2_5WY-ILuCvQLZBDN4AYUEnIf1JHoJwlBYReZz-5OSKsLMOoCuV3IvsJnUtSB-280DZMOl5CeXfGpEC2ucC6fTR-l8_HrQ0Hm7pSegCi6BCMi_m0Fm6Ojk0Ea5t4V55tSOdYsPZjJnjcZSDPFYPGo_0pNL4wbtcRdzZf8uT_MtmFd8vWPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=YqyB11VYmahFrOK_qdEeX85KC-2tiAh7_Tiwj098J80Hb8dt3CrV9kWd5tAkcZvnn6MKfHg8wxKD18ZCb5WpROEnc6TW56lDUbUU2vR4IhkLZacZ7X1r0aPfP_f20XQ_DHWIDyhvGmUdrEHivXsckEeeuEEMpSVDV5hYOgm4A6uzIDaH6LGeAZOXdtHjFyI-K5tCItggSjYZzPPcZdLHPrrbpP0MlqVYjX0AuNV8nQuW_k4uC7s8Z4IgEntwCwoGu1Y9wjnef05XshkBPZ-FWuKchTmZJuWS0nslp1etltBqvt3l4CTW9Jlw7XZJITdjMhh1ac1jOf6Gfi3T-Tn2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Mil3TL9-pE2GufdC0RrUDNnIz1FNQdS4Ior7s0TmCBv3I9byN2KOerT42Mc-lFIEcL2P_I534wcZAZLOW0a1yfaiSspQFddnTSM7bDqwNEcO_vBMkrJhrjWmqYIWd3A6BE6_JtyDr9KHJ4U_ueKwT9FtONjOnNBGHJqRaKscJLkUNYPIImxz1tCAVXCH7Cf2100kTGsPrNUzFe0ssOU3rW-eYgg0erHe7bpM5EYFPOMb9Ho4gjlJKdXUlgQX_aIVcGjSBjgqEPPJHZnPkvSzdgjLJv_gJzoj6LlxJmnb5_HCddGw3N9BVwZlFUWo14k70XpE7pHqJMQUbo-vEM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYGnF-q4bgMd3NeOV1unJoHkNrYOoILXELuF0epnUpxyPXu1LF8HH2Nk5NE10NuSR8nsHI8KIxyvcoAp3pGJeVI8B5Y-HjcbaNMP2-0h1Ftnib7zrI321134JfDfRPkClbI1SvKCMsw8zdvKhrVcepAH--jBRdM7HoiTgkQV1jsIrRkYpksdmATjco2-AvX3H-nlHVy-VH7oTCilsN3eXQC9xX7b6fVENoqGok6NnYJ77bSQzBfH48oN5jCyOuu6bFd2TuCYNz32RB9b8ewhRPlx1NfmF5BWUE8LKeppDmWat_5G1cmRiMlKD2doNq0Y8z0WtUAnYQNX6rUr_0fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=dAnB_eBV908usYPOr6AtbwQ7mVWyHW2t3lW_ULVJWC9fi8qWTmc_J05fGGLFc1kqhK44HJI0cLxXNDxX5rOxhZDczUT6PLObIGVR071NVb7xGtG543qFP6QiAF2v0Ql8-ahurXLHLbmu-42dQVk7upG_FWFT0k9yrZwz3PTnT2ysFYK4M-a74C8RCnUXLjQJ6G3Tzz9cDIS3b53YD-fSFvw_fNnV1S2vOkAvPvcN-rzmvRpcd4NjlLTzQu_u-IXNy4K2Db_0T4oWmmTiOVfo7X9uN_E8UsLLtqQE016zXmdHHcq8UOWAsDf2PXpMmHUgOibHSA6X3wfxGOfB_kVyNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=dAnB_eBV908usYPOr6AtbwQ7mVWyHW2t3lW_ULVJWC9fi8qWTmc_J05fGGLFc1kqhK44HJI0cLxXNDxX5rOxhZDczUT6PLObIGVR071NVb7xGtG543qFP6QiAF2v0Ql8-ahurXLHLbmu-42dQVk7upG_FWFT0k9yrZwz3PTnT2ysFYK4M-a74C8RCnUXLjQJ6G3Tzz9cDIS3b53YD-fSFvw_fNnV1S2vOkAvPvcN-rzmvRpcd4NjlLTzQu_u-IXNy4K2Db_0T4oWmmTiOVfo7X9uN_E8UsLLtqQE016zXmdHHcq8UOWAsDf2PXpMmHUgOibHSA6X3wfxGOfB_kVyNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=JG04AoLYDNHk8lGDRGJfbWjImsXm2LkJ4tfyiF0Wz84J4rLIFVKX6ptz402QhzhlknimbuZjjV6Y-AzsDHPbmj6B9jBOFclhT7UOH3Mv9-HFt8Nu2c9m_8wydQr1mpDw2C7bPpFtAl_CoFR-jo_Wp2UKLlzn5HN6Dc25nsrl5wIW2J3DoF3N4DMeNldeTXekQU58phbk5DM6oNxfo8Ha81tupupUr0LkKSpMxPyeeHmD_ABSHd1fc6lbW3XBSf0mYiItbSt7muXgmLKnyJtyviroMiq2xD0OhXQ9n_nuKpZg2YcRV_9HX_s4MyH0xe2pAsAOBCvppt-JKB-oaWZbpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=JG04AoLYDNHk8lGDRGJfbWjImsXm2LkJ4tfyiF0Wz84J4rLIFVKX6ptz402QhzhlknimbuZjjV6Y-AzsDHPbmj6B9jBOFclhT7UOH3Mv9-HFt8Nu2c9m_8wydQr1mpDw2C7bPpFtAl_CoFR-jo_Wp2UKLlzn5HN6Dc25nsrl5wIW2J3DoF3N4DMeNldeTXekQU58phbk5DM6oNxfo8Ha81tupupUr0LkKSpMxPyeeHmD_ABSHd1fc6lbW3XBSf0mYiItbSt7muXgmLKnyJtyviroMiq2xD0OhXQ9n_nuKpZg2YcRV_9HX_s4MyH0xe2pAsAOBCvppt-JKB-oaWZbpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=sZrT1zlc8NPTap-dopRKKpYBg8atj6dGtRbVNL79oKCKNTM-s1Oq0kP3mp4VqLLQPbC3xP4mHk-02GKrFCJmQbIbAmQOXpXQue7dPlGSdnnG_DAGl3EgPzqtfcMZdYwEqJvqNmYGC0sJyb7Soc484aNJ7weCZnpLj068I8MdpW1SeUsarz85f1UK6Jlz0ke-FWTL6GRPWckSNOn_SvU6qTUeouXLDZs1NjzOaTMtAPg9xFPySZ090aJIag5XxsihxMBHqPzWSi81evu7oDe94SurGohlghL86UfznBjSwFe1SPZIKdT-nOr-kubqQhkL-BzHOQ-0RokTfgL1R1w8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=sZrT1zlc8NPTap-dopRKKpYBg8atj6dGtRbVNL79oKCKNTM-s1Oq0kP3mp4VqLLQPbC3xP4mHk-02GKrFCJmQbIbAmQOXpXQue7dPlGSdnnG_DAGl3EgPzqtfcMZdYwEqJvqNmYGC0sJyb7Soc484aNJ7weCZnpLj068I8MdpW1SeUsarz85f1UK6Jlz0ke-FWTL6GRPWckSNOn_SvU6qTUeouXLDZs1NjzOaTMtAPg9xFPySZ090aJIag5XxsihxMBHqPzWSi81evu7oDe94SurGohlghL86UfznBjSwFe1SPZIKdT-nOr-kubqQhkL-BzHOQ-0RokTfgL1R1w8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeYH4c6AzDZLos67gIGWV52Rii8mv_l6fD5LAnqBkiMoA9epaZ_vVNeUGlMf5pEjgBLlaE4ImF0TahX7BjPhF_nW0I9DGWMAzXpKkHGjpB4hsQZUFwiYicWhillDDFaYb17Da04FDzw-pav3N7QMyeuCFD5Bqq3-9k5fASwwVpxV2BvGrsR-JBev37CUeGJdXy2h5DprC2kqiQTeLGQX5TvzKTFJl4huVm-OsdRTTGQTixOgPz7krG6dwt8pcBw1S6vhQhN7vuBc7G0gNpfd2ZutDiRpAo5y73ucMmZcbcvK1fTs43eOIJho5uV3lSLiQVxPgD7IcJMU30rKr_uksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=ESAz2qaqDe9vsPhxwSuXDM0phvgtnm8uUY72kXrEnk-c3cGG7W7RC4RSGkLqjB0HNfx0IY7CUPOmHYujZzB0Lsgu2NUnmKEztc_nhu5KWJErac_ilbIZ-f_h3SowCMxo4vTDwrW5ZocACU5-fXqXS9CbNxHTE-nBfoTKZCqQ-oAQoFcCHf2KcKum5dVfZGeJHJmshoFE5tbyxsPLFJL4pJ5nYwmCMnJyN_1F3bpYoUE03ut8_wUv2dDgd_UM3VhtLy97o0ZEZ9a_dvQn6xj7NDw5MEa5GomFJyq1I6DAhccPQpGBYV1PzL5AIN7AcVv9h4nJuzNfBd5avZ3Y4m_uVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=ESAz2qaqDe9vsPhxwSuXDM0phvgtnm8uUY72kXrEnk-c3cGG7W7RC4RSGkLqjB0HNfx0IY7CUPOmHYujZzB0Lsgu2NUnmKEztc_nhu5KWJErac_ilbIZ-f_h3SowCMxo4vTDwrW5ZocACU5-fXqXS9CbNxHTE-nBfoTKZCqQ-oAQoFcCHf2KcKum5dVfZGeJHJmshoFE5tbyxsPLFJL4pJ5nYwmCMnJyN_1F3bpYoUE03ut8_wUv2dDgd_UM3VhtLy97o0ZEZ9a_dvQn6xj7NDw5MEa5GomFJyq1I6DAhccPQpGBYV1PzL5AIN7AcVv9h4nJuzNfBd5avZ3Y4m_uVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=Cs0zZkoOXSU1cpjqXvF4QK7SsD0y7091ZNVNHp-3S96wXQ7mLFY8JPupbg7Zfxn_4VcooEZSOhNTup3GKwGvBN_svo3dIhwVMcmeTatFte8MyNXLmEuNyN8mtdqmRhiERxyKb8ieLd6kIM5MmKinJRtCd6CecEkXFLcE4eBxQ0nwFLOansdynvdENFaArikVcHZCfYWi5SSWQU9zc-0OmUY2XX5j7szq9VDbxWhv6MFAkmQrr4gQTnePE05TDd6-UNNsRBxrQ38FO_GheuwKjK65nyMxpWiXMzRlXvpsBdUDziPPrNTjkaSwg9qJih2Ul2BlJYqZ9jXEqQUHy9qlkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=n4weodpiE3OWQlIVPKN5ZDLS8eiZ8UEFhGDXCqFDk-2VZrGMmEojwjYUyolpClkqg0McU0wuzmIXIf55kXZLnMuWrBWXqXel2ND3mBwvSSZUEYO6IJbHnBtwGWMmNqTJGyTtHY-taih8zeXMWIGcQRc_qUzRsWZhrzbXS8Jw2ZDFWa1uOQsuS0puQCpdDPJr9ST2GbklptE83_PiIyQaqNdXSuSQMUoCnOtiFmSUFlaOBxIcqhXyD81gSBR2GXiaUUjfMuISEth2n9p4bxhEkM9BOsq4HywqNRSmfusN29QP3rtM3xHuHUP5P6QxOObZCdPDgUSXYkpRHIaSVBkXxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=n4weodpiE3OWQlIVPKN5ZDLS8eiZ8UEFhGDXCqFDk-2VZrGMmEojwjYUyolpClkqg0McU0wuzmIXIf55kXZLnMuWrBWXqXel2ND3mBwvSSZUEYO6IJbHnBtwGWMmNqTJGyTtHY-taih8zeXMWIGcQRc_qUzRsWZhrzbXS8Jw2ZDFWa1uOQsuS0puQCpdDPJr9ST2GbklptE83_PiIyQaqNdXSuSQMUoCnOtiFmSUFlaOBxIcqhXyD81gSBR2GXiaUUjfMuISEth2n9p4bxhEkM9BOsq4HywqNRSmfusN29QP3rtM3xHuHUP5P6QxOObZCdPDgUSXYkpRHIaSVBkXxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=MGgeaW_pXQY_v8GJd22HNjxxOi5U6ztTd5kum8s0Dm-af1NN2GS9_C8g95_TF3JC0uK1bs12ET_w7YMmOKwkib4wbgII1FCstsC_pSCjB0nZOIuE6Ykz8pfDQJVwwu1STK4P1bS5YcR19I0udGE12RaT6T4VMXdUvahzisud_5-ZkLIoN6A8pQIgJGQj0eeczNalyLzvKYbHxPDlVtT3TyEjWrRXoOEWfSmfYNAKHfykQQvG2gD5tXWfILUrYD50P_0N6gtfK5xTT1mepyIHizKc2MCDzDMIgbGT8dbvWYrLWUc6UDpSQx9EQzF-Qj3lzUKFj9vQhkwxece9B8rsnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=MGgeaW_pXQY_v8GJd22HNjxxOi5U6ztTd5kum8s0Dm-af1NN2GS9_C8g95_TF3JC0uK1bs12ET_w7YMmOKwkib4wbgII1FCstsC_pSCjB0nZOIuE6Ykz8pfDQJVwwu1STK4P1bS5YcR19I0udGE12RaT6T4VMXdUvahzisud_5-ZkLIoN6A8pQIgJGQj0eeczNalyLzvKYbHxPDlVtT3TyEjWrRXoOEWfSmfYNAKHfykQQvG2gD5tXWfILUrYD50P_0N6gtfK5xTT1mepyIHizKc2MCDzDMIgbGT8dbvWYrLWUc6UDpSQx9EQzF-Qj3lzUKFj9vQhkwxece9B8rsnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=F8qEo_1QcaDEcXOlf4jaS9Yu0FRR7Qa8Q0KUBREmA6QHcs_uLSjM7E4ne6FYBN-qFjZ6m6APDag1b0E9KcsVT_sITE-_shPPBOmG8yaBbqCxBzxIAYNK3VzCTJ75DKxdL_qWVlz4d4MnLspa4Ch5_7w-5blnN8e-qgrpu1AHu9tftL9Yt0Mr2xZSpvBhmKW8MDYQ7Vu2mUnAcKM4RF2ocypULX65pn7D86HBfJ7uSgt-GAm78B8FJ0D6fTu5SARtoV9sBL_RaFJY8lZ1pGy52ponJYevnRPfSl6yrmwyGP1fS_eiWzfm__MAv5e6dCRp5EngM1jaPIGPTTooTYY0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=F8qEo_1QcaDEcXOlf4jaS9Yu0FRR7Qa8Q0KUBREmA6QHcs_uLSjM7E4ne6FYBN-qFjZ6m6APDag1b0E9KcsVT_sITE-_shPPBOmG8yaBbqCxBzxIAYNK3VzCTJ75DKxdL_qWVlz4d4MnLspa4Ch5_7w-5blnN8e-qgrpu1AHu9tftL9Yt0Mr2xZSpvBhmKW8MDYQ7Vu2mUnAcKM4RF2ocypULX65pn7D86HBfJ7uSgt-GAm78B8FJ0D6fTu5SARtoV9sBL_RaFJY8lZ1pGy52ponJYevnRPfSl6yrmwyGP1fS_eiWzfm__MAv5e6dCRp5EngM1jaPIGPTTooTYY0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=hduE0fsPB0LnvNTdxF6vNKZuR5xMt3iUavUDQuNpZtlio7xZfpygtSqg0whXyg6Lqo1a1OMdtIiaBma4redlFxrGceo25bXNwnr-1EJi7hqWOGQaF3dQrqhS8Qv6Xj9-fLxr1mrXmYmvq4dYfoeCRzfdet2M0ym2MUlAWM6RT6UCfOlbommlSNZSrhutEwvnGQjExusCwY8EGNAxdIbjsbl4XSBrKElIxaY6IVnsC8zZjo2clGZRIJ2xYRF7hv7Z8FZQ47Lf1iX22Le_Pk858i0jryO5gbbn6NpEziTT1iKGIYD5xhGkH2NidKyr6EcOKP2Oe6Pw0br7UwLLsBBMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=hduE0fsPB0LnvNTdxF6vNKZuR5xMt3iUavUDQuNpZtlio7xZfpygtSqg0whXyg6Lqo1a1OMdtIiaBma4redlFxrGceo25bXNwnr-1EJi7hqWOGQaF3dQrqhS8Qv6Xj9-fLxr1mrXmYmvq4dYfoeCRzfdet2M0ym2MUlAWM6RT6UCfOlbommlSNZSrhutEwvnGQjExusCwY8EGNAxdIbjsbl4XSBrKElIxaY6IVnsC8zZjo2clGZRIJ2xYRF7hv7Z8FZQ47Lf1iX22Le_Pk858i0jryO5gbbn6NpEziTT1iKGIYD5xhGkH2NidKyr6EcOKP2Oe6Pw0br7UwLLsBBMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNMozdM9PTk60o7XtElgrKsaRafzsY16f9DzA3Sf_9NJaJxVTK62c5U2Y_dPF-UXPGeRtB5HBk4xxWi5MyZ7Vvy7iER4z8jjtQwskhg_hFDllEF4m9f_woywDqQkDuN52LBzHr87rDteqcZA9SeoFOLwmZUHykesW8dQ3CUEkseQyMZ35XnPFFp4cSVj3HkM_OnLzmMYh7-0dVLECtLqMcPz4QOoGVYSo-Phpj7FwiuqdltUk2HaVb_M9fYLGIb4tb4mx_xnwVv7R5cyie-mQAYF5tyxDpCG81EFSDcUWpdOdj6Rfx-5SR5nWWkGqNTmtZFFPL850qKztH3lFh2_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVePTy3Xslh0_4Sf4FU-MvGfTqWhMHkArPh-vvYhobQR8hYOhMy25W4IZlLiLn7RGIo-CGVPSH6hfmGO0jw9OQ-bf1fE4YrotLRsVOur_cK09-vGeUZh2mtTjAUvDN-FZP6PnwscbT8wTrg7w2zT56L4dOJrHx-hZqFdGC96J4SeuObymJOiO9oT6peU6EDDRbaTONrMisDpodvSbU7gqk8hn7yzATUR1dwyJ0mUQxyuB9yu9TLuBTcZbV3VUJqJ3UnbN6HwxVJKyqoyY-9t08xwsog9FrHfGQMtz8UecQpvcAW7miZ3-vJejxCXm5zj6Pw52smdtNW1FDift3qYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=qZu8scWsbPX6PsUo3f9qXzbsUjfC7YKGWULHp8UecICrhtq2e3D-nbgEo-aXEpAJPovLV9_E4aK1JLFDdv6pV-G7Om5_7PekQ36enIf3LwWbA1TL7TfzWRRDxdM_7r5L5KNkiPp9t0H-8CfpyQ63UL_VL8qDWTdtYfLfID8PO1XDCg_PuD-ij6r7gaMYCHskoWBTa3l0QZONM6ji1HU7LrjlvZzRNCLTQbPhbVO78lxW712PrZ4tnwQdTrn1r2HPk6wNzL1pLaiqr5v6iMGqxI2jrHRcx5OTxdnQgeECtSRi8hKwEZovw9BOORAanIXajl1YaDZ6ncMrRuLSVAOhiE8Fzqde6Xeccy9bq8k7t9iuiYnfqn9PqgFrCbTMHMua98aV9Al7oOEGZyqrrwp2DYEYYmRLkdKksAC8-y6MQWUI8u6IgCHit4DQm41AtGI3steGNHmpjaU3FfoDzZ0MNSAQ0i3wSG9QjWQDcHagBihTR_-rkRP3DlZe4EJuuq3JmREqh1SB795_9n300f1vY37zYHhhTtCgKcpNQ1KNAGVAGMvkFYvcfSxlt1EAd5Y-2Yrxk-zn93Ep3WErhDS4ks7AIdpVul6-BUV1sdTwsoJ_Hp9cvob-7LcYF9hyd2Rj-UCVzNfPMrBDmHrGdU8W4oFRx5cFMUu19RWl-XcvXnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=qZu8scWsbPX6PsUo3f9qXzbsUjfC7YKGWULHp8UecICrhtq2e3D-nbgEo-aXEpAJPovLV9_E4aK1JLFDdv6pV-G7Om5_7PekQ36enIf3LwWbA1TL7TfzWRRDxdM_7r5L5KNkiPp9t0H-8CfpyQ63UL_VL8qDWTdtYfLfID8PO1XDCg_PuD-ij6r7gaMYCHskoWBTa3l0QZONM6ji1HU7LrjlvZzRNCLTQbPhbVO78lxW712PrZ4tnwQdTrn1r2HPk6wNzL1pLaiqr5v6iMGqxI2jrHRcx5OTxdnQgeECtSRi8hKwEZovw9BOORAanIXajl1YaDZ6ncMrRuLSVAOhiE8Fzqde6Xeccy9bq8k7t9iuiYnfqn9PqgFrCbTMHMua98aV9Al7oOEGZyqrrwp2DYEYYmRLkdKksAC8-y6MQWUI8u6IgCHit4DQm41AtGI3steGNHmpjaU3FfoDzZ0MNSAQ0i3wSG9QjWQDcHagBihTR_-rkRP3DlZe4EJuuq3JmREqh1SB795_9n300f1vY37zYHhhTtCgKcpNQ1KNAGVAGMvkFYvcfSxlt1EAd5Y-2Yrxk-zn93Ep3WErhDS4ks7AIdpVul6-BUV1sdTwsoJ_Hp9cvob-7LcYF9hyd2Rj-UCVzNfPMrBDmHrGdU8W4oFRx5cFMUu19RWl-XcvXnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=vqJaw_PR_IdvKEPXNdMP9ix7IhspGSWsvjDJmPGTflzBkuthPfuGtvUZ2Urz2Z9YRGIXOmjysV6JA81lqo8Y5KbFT_OHb2fHPCJMVTo5r8Y0RcEPw3u1-Kmnur8w5p3rxlPdLgzmUosxK9ocy1KGGvtXp-3grFz8xC9eN9pYKeYzE0MEsNnOUjUyf-aPHyngGw_naFI5S2KujH6yscsRLPWbfs7NHU9rzujKdzMO6sQISz4MYr-sC1Je1INZJvyfBMnd5F5ULsD25ZmrFYyIoTQVNBGfEnwg1cbwa2h__Mf4kx-Ze5kcFCUKKfwcSMv2HAzAUOI37ha5RX4CBesjLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=vqJaw_PR_IdvKEPXNdMP9ix7IhspGSWsvjDJmPGTflzBkuthPfuGtvUZ2Urz2Z9YRGIXOmjysV6JA81lqo8Y5KbFT_OHb2fHPCJMVTo5r8Y0RcEPw3u1-Kmnur8w5p3rxlPdLgzmUosxK9ocy1KGGvtXp-3grFz8xC9eN9pYKeYzE0MEsNnOUjUyf-aPHyngGw_naFI5S2KujH6yscsRLPWbfs7NHU9rzujKdzMO6sQISz4MYr-sC1Je1INZJvyfBMnd5F5ULsD25ZmrFYyIoTQVNBGfEnwg1cbwa2h__Mf4kx-Ze5kcFCUKKfwcSMv2HAzAUOI37ha5RX4CBesjLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=SePRwkZwycEntU-n6PKlZeWsfXLAzD9jLOtIy_cv9nYzt-_O-QXU9_iw8iYXV-aDZya19YalnfqilBi2jmrNuBwdtDwQNU2jrCFO4oQbhBDYVwf-iDY3EOh6cmPK3G8gYRGP8gZJO98DsRJO0KSlm45RPTUUJPXUNWpUSWt00G1oHlHdQDuhSA0dskmrTIOwAa6KsM5MkDrKhMIYWJ0J2226SCheuYsh9x9kR8PZjFqid6FABTK_J7XkjLrsACWtmqAzBxWUWI3N2avwfJcVttjlsb71zCcQGfA7M_0N4eshTYm3jLI6msr7qmKDHdF86Rl4xdbTk_NsyyI53tMvGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=SePRwkZwycEntU-n6PKlZeWsfXLAzD9jLOtIy_cv9nYzt-_O-QXU9_iw8iYXV-aDZya19YalnfqilBi2jmrNuBwdtDwQNU2jrCFO4oQbhBDYVwf-iDY3EOh6cmPK3G8gYRGP8gZJO98DsRJO0KSlm45RPTUUJPXUNWpUSWt00G1oHlHdQDuhSA0dskmrTIOwAa6KsM5MkDrKhMIYWJ0J2226SCheuYsh9x9kR8PZjFqid6FABTK_J7XkjLrsACWtmqAzBxWUWI3N2avwfJcVttjlsb71zCcQGfA7M_0N4eshTYm3jLI6msr7qmKDHdF86Rl4xdbTk_NsyyI53tMvGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=gM5L8qDILufMJyerWyG1ACYijdXyf8RRakf56Z9PPncYqlM62PBaoJsdDjt4WCKTTaM7SeJVHG6gb9iNeNNMcfII4ea7OEVzzS9ik0cBJoRS2zRAL6LpSC5NaQVOQRIKhdfheIY0jZcg1UrtC7t2I-9vmQ-RU36fVipIbRo2lhzfjtP7yLoDa8PAuMqrilyQmzTfd3aLP8XqrKxWRmgoKxkBm5fDvnsaSlzXzX9xwTSLlyIzEOpgyE-Gvo9ozvjGw0P7UQibQqW-Iix-dvsG0dKrN_uvoyBYND9-lmIb4ZYDVwvJMqiowO7FjWHOsHooTqL_iDm7yL6DEMS0kG5Rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=gM5L8qDILufMJyerWyG1ACYijdXyf8RRakf56Z9PPncYqlM62PBaoJsdDjt4WCKTTaM7SeJVHG6gb9iNeNNMcfII4ea7OEVzzS9ik0cBJoRS2zRAL6LpSC5NaQVOQRIKhdfheIY0jZcg1UrtC7t2I-9vmQ-RU36fVipIbRo2lhzfjtP7yLoDa8PAuMqrilyQmzTfd3aLP8XqrKxWRmgoKxkBm5fDvnsaSlzXzX9xwTSLlyIzEOpgyE-Gvo9ozvjGw0P7UQibQqW-Iix-dvsG0dKrN_uvoyBYND9-lmIb4ZYDVwvJMqiowO7FjWHOsHooTqL_iDm7yL6DEMS0kG5Rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kThGwpyGVJF_ALyCKrrNZQk_hpYzZsxVZ_-xKQ67rYnW_4PZvpfQCAbA2v7a9e4KCHXbthY5mDHvtka6L4SGIkHAZVaXEecgYLdlGgGMHhOU3pgf7lJ8oKrAnzNpjSew7jAoKfJzbpJTRM6VbXn1B3cmB00626com01LPqIVceXCys-GHTlkF5uO7J2reemeDE_Ia6pYrOlRmoBY-l0IaczixkyruCHPoUs2D3OAz01sMVeHXiRVxyGY5gg5vsU_egPSd2bmcx1NfSw47r1zeuJvIb51h56AaupP-Io682ei5P1EunOXSz2zFL5uh5n_BIyEpMb7IbzcE1M4P2yZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTjDoOLjHk0D8JWt0EgcT6P4hIQhePs77J81nUn7veyhrOvHp6-KwW_vLLhv-EHTchmzOM_xe4R1MNpE3UXtv1D_fNOFwc-BGipZBz67ZEJP-JPt-KbK6TsRvxGXxdZNsNTPVTdEy0un1uMcZjjOBaaKox11Ft4FculijYJSJoh7soqbVE_I3ksAP6ZuUiGrkgS0_yZcdokOjAQU6Z3ldYm9KaBlm2PLCPrYAFCkid2fOW6HH_qlIPtFrr0FL5aK9Ar6QiwJAIeUjE5EcGh_YWCMWXtTmobDAgCuLyzQxd6EG1St5anHmlbnAn1FwC1n_Z1vvgR0hLoDTNnBvaGwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdq4iRVuv1sv6_Ey26kMeNLm5VxfC8p7YBs0VRp9ffH-CZ0y8bXUT0f8gYd_b2G3HtEuedvulKCMnD0D7HfzVryHvbydAe4cs5zyjarH7fEFz4ERn5GHnQIsMjGW6uNmdloiL6EU_pr7AsuGInzLC6qqLzgdHgFnlkKjlsO2h7Sl1M6VDjWU53nbbyVN9bAMmGKRwK4blyYFPoq9edyevtatrSTG_FDlDij-wCS8N-QXPaXL13CjIOOwzwVKyPNEVUPaCSAHii-Xdpd-AbQnWFC1ARxK5t3p_n4aTSvps8lY3uRHRuKGJibovODDloQ2QfLiRhLg-N-h0blDIOs_DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n031UwpjCuacN19R6W5T5W3hkLOlZ5U0h0wZ2dIH5j0lTtFXHKDYzRTKw2WDzdskooqu1qmpKu6ZNgPDkGjtHh_32_mHQIoEiQcLcA1RrfDewY0mwOlA3MzLp6Sqe9l3wrwbiTxptRGr02ErZKtrTaXH4LG7Ft0m_aWoN3W1Y5anbHGTwO2PVpfRG-khumMftPDsRCyFlU39eX-b33YOJQ-8Mn_FXqL5WQgkps0KXWX1HUSCmA-OmXoMdSdFvhvExFOQQIJNgFrow4wcQigmHm6HVmvv6IXoei-7vLkjTtczUQk91V7X8cW94E-acsV-MzWvTu0W4tjyODL23ec6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=iBq85G3k3okjTOzxpPmYVBq_SjpJAEfCwkhjJ1gFXRyztj3N32ebClFEY-QoQLZ6a3X67jh0sfM5P5KBIlYZ6C_E8MxQsqra6GPH_7TsqkuEglUOZGibAMLdmqbrqg0ILyHlpZksvIZSjp_Yj0XgR3321nRx-B-iSEB3TYJ8TbmduAiIraOI0Sf63hNybXi6ntUJTgDvmZPH3s6xpHHLR1v4D3CPC3bdEM-y0bwHSmvpxwypG7kQ-9tZ78wahvRJy0BsKwsO-UDKi9YFOEw6SDCt65iWlpgbT7BHXJ9cEq9CkspOFddf4cMNMGyRZF4u22iG5WBwwMLUUsDsvlHq0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=iBq85G3k3okjTOzxpPmYVBq_SjpJAEfCwkhjJ1gFXRyztj3N32ebClFEY-QoQLZ6a3X67jh0sfM5P5KBIlYZ6C_E8MxQsqra6GPH_7TsqkuEglUOZGibAMLdmqbrqg0ILyHlpZksvIZSjp_Yj0XgR3321nRx-B-iSEB3TYJ8TbmduAiIraOI0Sf63hNybXi6ntUJTgDvmZPH3s6xpHHLR1v4D3CPC3bdEM-y0bwHSmvpxwypG7kQ-9tZ78wahvRJy0BsKwsO-UDKi9YFOEw6SDCt65iWlpgbT7BHXJ9cEq9CkspOFddf4cMNMGyRZF4u22iG5WBwwMLUUsDsvlHq0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=Ixpunm46vh0HBk84WC1D333qEl_nvFWEowNaqpTmb3-hPFZxcnilC8xPtCD8BqHbQiHNqkk2dy2bLVliJhgauglIgEV3i9ICaYg86giWadIyjjUet8DaHG0K_VXjyknHdsI9UtEjb3iu6RSDZNQ8BVI3QzZQZ5IjrJeDr1D39M4ETju2hWwc-y4I5zjXLyePwn2V_8UbFk0EZLHBpgJcfcyjamnm8txgwU5GFFIUWk5MLbL8-jYJKh1MKZU4TJGiPvoyba5CnhuXFGFWf9RYQQsU59Wq5KzOFlZGK1xEbdJVJeYiwE8BwY_ERw3lhtY33UCiFn3wQUQpvHbXGQajGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=Ixpunm46vh0HBk84WC1D333qEl_nvFWEowNaqpTmb3-hPFZxcnilC8xPtCD8BqHbQiHNqkk2dy2bLVliJhgauglIgEV3i9ICaYg86giWadIyjjUet8DaHG0K_VXjyknHdsI9UtEjb3iu6RSDZNQ8BVI3QzZQZ5IjrJeDr1D39M4ETju2hWwc-y4I5zjXLyePwn2V_8UbFk0EZLHBpgJcfcyjamnm8txgwU5GFFIUWk5MLbL8-jYJKh1MKZU4TJGiPvoyba5CnhuXFGFWf9RYQQsU59Wq5KzOFlZGK1xEbdJVJeYiwE8BwY_ERw3lhtY33UCiFn3wQUQpvHbXGQajGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=mmrH8qdjNOD8NHTgIy7KE9Cvs-wiyRstjxBQIidvN7jDAS_Km7WjqgcMv-IE7k-v4OEzL80rDmzKbXx4emzOGQPTdL9HdHHhoUhqeJ8S-bmmsU2uNWZIRFqX8uYDVYxhFcfOukaG6o1mVuhk57B12CxGGSJIoBKen7x9R3Pg6oySwBcUgHKS4Z38oHa5vftEM95b9x_zPfORXL4s4OnRHNeckDCpOEuDJAiYNICjAEO7WQMO8f2Kgx9GIu6SqvDYdyiPFnjAeQ6_7UuNOIF27aVbgk63c3qUqQXA4bh-q6KKd2cpSIGTSVY09BvUCYEX3GPGqZm2ryFeipS2tyRIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=mmrH8qdjNOD8NHTgIy7KE9Cvs-wiyRstjxBQIidvN7jDAS_Km7WjqgcMv-IE7k-v4OEzL80rDmzKbXx4emzOGQPTdL9HdHHhoUhqeJ8S-bmmsU2uNWZIRFqX8uYDVYxhFcfOukaG6o1mVuhk57B12CxGGSJIoBKen7x9R3Pg6oySwBcUgHKS4Z38oHa5vftEM95b9x_zPfORXL4s4OnRHNeckDCpOEuDJAiYNICjAEO7WQMO8f2Kgx9GIu6SqvDYdyiPFnjAeQ6_7UuNOIF27aVbgk63c3qUqQXA4bh-q6KKd2cpSIGTSVY09BvUCYEX3GPGqZm2ryFeipS2tyRIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-CTo8jTaMZckyzPufDlBU2Z3cUSwA1jl4UDR0Rh8pThrIsLaCiPg0f7X0WKEAx28Yrva1Uzli5jEyJj-t9Ip48gTT9_Cw0pSijet9BVvW_BaUl3JROXX6GiQH7FfvVY0fHHmPORh0DRvk1sn43rr-9MrdfgytbL5GdbWwgXYRIXqrzkJwPQmUjKpQZDqJRsrypfab2ZMJlG4YGfDWiPUpMf5sZiX8rWODa3PVeTI-q0ZOHyZz90MrN4OmgQGs3hckZ-vf013PAh7Qn59GFN31WWvHDbsj7_H9AxCDstcKg1T-4A39j6An-fsWFYiCyNJoS6Wvb64beFlyGnwqdDtxkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-CTo8jTaMZckyzPufDlBU2Z3cUSwA1jl4UDR0Rh8pThrIsLaCiPg0f7X0WKEAx28Yrva1Uzli5jEyJj-t9Ip48gTT9_Cw0pSijet9BVvW_BaUl3JROXX6GiQH7FfvVY0fHHmPORh0DRvk1sn43rr-9MrdfgytbL5GdbWwgXYRIXqrzkJwPQmUjKpQZDqJRsrypfab2ZMJlG4YGfDWiPUpMf5sZiX8rWODa3PVeTI-q0ZOHyZz90MrN4OmgQGs3hckZ-vf013PAh7Qn59GFN31WWvHDbsj7_H9AxCDstcKg1T-4A39j6An-fsWFYiCyNJoS6Wvb64beFlyGnwqdDtxkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=h2Q03DcN2IBssQSRcb91t7DWPqftgUBS85qLmtPS05skKOEl2daGX7kyat4IEYXZUQlxkVxXr6OOReWOW3miwxYlIFvW4ChMaDS3x31_3mP4wpZ8_E-WMBUN7dvZqUYN3dEZ86yxxVrPm_Drh1EU4EV-7e_-a9UK1c-9BVWB0TxEDdqlmRp6o1ifoo2gUbSMbUnwp7vogZfw4cvQIWhij0hABaqHERv46fphVpUQhKCtlpBT6ZCKRl6xJJndeaUON180U41vg9iNRkQfT3OVsYnFHteimn_Bx2fEYnDpFCSByEscb10mlS3Mp6f4nu3JC-zMIRWKmPryI3V1TfiGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=h2Q03DcN2IBssQSRcb91t7DWPqftgUBS85qLmtPS05skKOEl2daGX7kyat4IEYXZUQlxkVxXr6OOReWOW3miwxYlIFvW4ChMaDS3x31_3mP4wpZ8_E-WMBUN7dvZqUYN3dEZ86yxxVrPm_Drh1EU4EV-7e_-a9UK1c-9BVWB0TxEDdqlmRp6o1ifoo2gUbSMbUnwp7vogZfw4cvQIWhij0hABaqHERv46fphVpUQhKCtlpBT6ZCKRl6xJJndeaUON180U41vg9iNRkQfT3OVsYnFHteimn_Bx2fEYnDpFCSByEscb10mlS3Mp6f4nu3JC-zMIRWKmPryI3V1TfiGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=WKOREwNrac1f2DE1luhTC04YIOzXZp1X46u3D8fypUXJ8Hu1-XD1lVi8x-cB-aPGpGKr6bIm60cuaAmfnFhurfrx8P0JTfUC4z8HlnvdzGplsNuSzYkPL2kjyzOzAGZgtwYtA7TloU5BZ1BZW243erxspCoCztul-JKrfEsjJwJkGNLajdQYUlMXqSRSK-HTvL280pZ_zmCJTOq7rqniLltFt0kyr2TOzV5oolRzdGCP3yJdreseQOhXTMKSOv7F4vnTUSwqjtEsQyXALTrQnnVgcgEPAnNo5SO94Wpq8ICAnM1nE7wi5-R1pv9RqLZJu-PCzDBTgMV_icPtxei4Jj3el6FyrvkMTWiCuAiteh5nmvxjxoHE5kvXVOMVnI1ijFCfkoCiIuTNuGr8xg3rl_5h_zu9JqGsGTjEoO94kutzC94jet8EwXXY3PMZVlmh1OrmGnSi7G8lldmXj6GIdWc22gQFdpq6NRsbexJZvCbCM5JMvoD7ZBU6BfZQW0q6QDX_9oYWBEJWzDox26EBWKj_lPiR3Ot7HVerc2HQ8rVvokwSV0L-AdT6L1TjZmoicxAh5RzaGO7m_8GFr8S6sA8FOPsh9-RDS0Bz1bqDrJuQOKkKtsUIUXFGjMuA8Fb_zzQesJ_pbkLWn0piejY5O5f0syf_IuAA8GQE_HrPbS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=WKOREwNrac1f2DE1luhTC04YIOzXZp1X46u3D8fypUXJ8Hu1-XD1lVi8x-cB-aPGpGKr6bIm60cuaAmfnFhurfrx8P0JTfUC4z8HlnvdzGplsNuSzYkPL2kjyzOzAGZgtwYtA7TloU5BZ1BZW243erxspCoCztul-JKrfEsjJwJkGNLajdQYUlMXqSRSK-HTvL280pZ_zmCJTOq7rqniLltFt0kyr2TOzV5oolRzdGCP3yJdreseQOhXTMKSOv7F4vnTUSwqjtEsQyXALTrQnnVgcgEPAnNo5SO94Wpq8ICAnM1nE7wi5-R1pv9RqLZJu-PCzDBTgMV_icPtxei4Jj3el6FyrvkMTWiCuAiteh5nmvxjxoHE5kvXVOMVnI1ijFCfkoCiIuTNuGr8xg3rl_5h_zu9JqGsGTjEoO94kutzC94jet8EwXXY3PMZVlmh1OrmGnSi7G8lldmXj6GIdWc22gQFdpq6NRsbexJZvCbCM5JMvoD7ZBU6BfZQW0q6QDX_9oYWBEJWzDox26EBWKj_lPiR3Ot7HVerc2HQ8rVvokwSV0L-AdT6L1TjZmoicxAh5RzaGO7m_8GFr8S6sA8FOPsh9-RDS0Bz1bqDrJuQOKkKtsUIUXFGjMuA8Fb_zzQesJ_pbkLWn0piejY5O5f0syf_IuAA8GQE_HrPbS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbi-vgLTo5FBBKq_6dkcQ9qhIXx2vxq-3cznd6qeJ5M3JM1z2SF3KZy2Oss5l1efnZnDtiGrxJbs4PDbhRrP4VBl9YhAZ0fWK1xNB-mnaKh9Avc1k5xQaqRR0E0nV8g6SXSzQ1g97BwthUSu_eA4be4LNd-oANjz2RtII4BwW2bHyuULfMyElr4h3toVbGE4wthcmCZZiWU4-TtZuVIaPKYnINn1mxXqSG8tvIdaaudPw7egPFoe72lJ35yB5kPl7TxphOCx6AE2Z-JgkmyoakKt4WHL77XtTBL5pWbMnnwz32W7qqPSWHc8mm-na_ukmdKH81p7nK7_PLZvYYrf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwaDXTA1o8j3B9F4IFcFxxH2hWqSTTfSRmoE6Kk0Mh_3i18ccSlOYzMrKCy6i-8IlCJZvawLkPovy83u8SGW1FLvi82_aLKFjEWDvXMA6jQxNRFnVTZdwe-TeBVOczN7Nbou764q3Vql0Vk_jpoQpjgAmXLcfF8ahYxnoyVQVmRG3-PpNNqY0-H0_pQ_eBo52rQeCUzcH_4g070hwuqGtuFKTHvZcy7ycNg5FxutFoz4YrXfEJOCvs2NR6a1Uv_G6A0rLaKQtqcsiMCldCuLxBnVgd8LgMqfkDGRGzKVatAZ-Pyxminb6lpNkmbQ2jdXkrzDtxKUrKQbwfwmses45oRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwaDXTA1o8j3B9F4IFcFxxH2hWqSTTfSRmoE6Kk0Mh_3i18ccSlOYzMrKCy6i-8IlCJZvawLkPovy83u8SGW1FLvi82_aLKFjEWDvXMA6jQxNRFnVTZdwe-TeBVOczN7Nbou764q3Vql0Vk_jpoQpjgAmXLcfF8ahYxnoyVQVmRG3-PpNNqY0-H0_pQ_eBo52rQeCUzcH_4g070hwuqGtuFKTHvZcy7ycNg5FxutFoz4YrXfEJOCvs2NR6a1Uv_G6A0rLaKQtqcsiMCldCuLxBnVgd8LgMqfkDGRGzKVatAZ-Pyxminb6lpNkmbQ2jdXkrzDtxKUrKQbwfwmses45oRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhKIZUAS6hzg7iMJwLRirmmLmtIgUo3KAt0vJTTutUXc6DgPLDiQ3WxFK7H7FtZwBcG9wdxRww_gkabM4SnFBimV0eGgDbFpD2tyewne28Fc9qPd5yqXP_UyVSSpZCfJepNRJ-MMQykKF9vVdBVS05A5ShTm2mn1hWW3KR4F9lraGHGPKe9DeZe2gEO5gqzZjLrUYZKf0ApZcWbX2iTft-N6ah4cek4VbpayIo0xSI4AoHuw4DFAnE8JdMlIEq6JTGajx2y2cZ5jS1M9Jf6nauqkMBB5TqphWTiBGCglyUc5H4YQucba_NTbkmA1VybTW44AZLu1Z0_5OcRlEvCHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/dY0HjQ8y-PYdTeLZTOhEZaJZMZ15wfXW3n9jv-AFh2tG1mBIUfXitL9OBXpHblkiNH-gtScx_j8Gvz21c9CdolrtppCDAo0g1Veai2FhUh-bH_BMRmGQMUfnIh4PORMNte52uL_5NWA8sFhMeHpcUlzekOco46SVu7VsnayMphtnT7f_1a311mwl2a5ZiUlhD_g0_kU8T5qnrs4eo2q0IwgJZygT4chHHUwOQrOjNRg5eRmGFRBCv4Ev1mN_s7e3Iny6_9p1omhiTRn_gcdRsZxzYidlF1hsk7j0VKPvo702tBj4puh6pK6MBADKp2eRLRCVL0LOy1s0xmGUnZZ8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/nkh1pCDhOarWkemF0hFKdNNfuh9RfM3lEoRSQf_P6ZzxZjh5UCUHJpxuJNJl7aJBaz-O4tv65A9V0riGFDA87l7-jcfLqedp0kTi8oLyQtdCTqFI5ZCGQe3ZYc4ivWqyrRvtTvrv3Notcpfe06YApgBkg5cPEWVs5qU_BtPR-Uzq11ULz_7zkn3fhb6LPxBir9JuXv3Gec1utIJUE9dCeW6Dh2PeIMbEUeAXF4eWHhDoir72M9NZDZq90oJHsJ_8UC37wO5dYl1btJgzss31FgpLdr7r5jptuMcF-rHeZnFYzzwkPuiapTZmtKB31ztssQGSWiYp8WRNg8TshQ7i3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=MtOZo9Ib_Gnn6mPpO23zl9j2ZWEqe8EIbMnw1rFiyHoVUhOyqSi-zjEXjGKSw4y8aF76GmiY2cJHe5Oh_S_8aUJIE8xX0CnH7h2oNTDcCo7XNjl8sUE7PYXFPHsE5SKa-KupzaoM_9oarXoqaj5UgETK1hNHIipcz4a6qLSW6TOo-0i_x5Zy2nE9liy6jN9d4fc7qLt39D6dqK6KXb1ayfP4rVb5ctGyy3HBRE-SIpyRl5qHcLHvXtR3VYgmjlCarOU0PoH947H_LDqeTZaiMFE9Xwpk9Up2-bJtXwwvbPNnOVgyIPEWrTjcEr9FNiNUScgTXxAr4X79ktukVYw0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=MtOZo9Ib_Gnn6mPpO23zl9j2ZWEqe8EIbMnw1rFiyHoVUhOyqSi-zjEXjGKSw4y8aF76GmiY2cJHe5Oh_S_8aUJIE8xX0CnH7h2oNTDcCo7XNjl8sUE7PYXFPHsE5SKa-KupzaoM_9oarXoqaj5UgETK1hNHIipcz4a6qLSW6TOo-0i_x5Zy2nE9liy6jN9d4fc7qLt39D6dqK6KXb1ayfP4rVb5ctGyy3HBRE-SIpyRl5qHcLHvXtR3VYgmjlCarOU0PoH947H_LDqeTZaiMFE9Xwpk9Up2-bJtXwwvbPNnOVgyIPEWrTjcEr9FNiNUScgTXxAr4X79ktukVYw0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnHWitqn1ST5ZB8D3VmjIWknTK-zlE9cVMszo9VDD0V2zpqsD70gm6qqSNgbhfpoZlHtTpu2XCH0yGTSYqb0ow3UmAopWxc5FQqrTz4OOGPkKV9GCkUhHvEFDfmGXeWiDPHxLx78n8AuYkcgqohXI85FYHLJ2uxbWGpFhQKDntz-q4EzL5EdtXTeBZuTkpGjAntZQ24HuDav8-sZYWPBhZxB76BM8MtTI3_dPjIz9sCOn_1oklEtTCrE_Phk5vKin9fYvKr9kJ-cporaNtJpU6pMjsD3uCbnAIK5u7cs-ePwKlnpJFl7h3VmeGCUQ6Ufm77s97hwPkXYYGOiEuHpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=eTlAb3wK9DsJ132q8Z9EMPj15I5_QMh_ZpxilqXq8dTrGXvN90Zo28yBseNM-mDOSjgJoV2BW9O2irihThFZAW8IvM0Ulv1GI5dEBAyaJiOqkgrJZvE7CrRrQNDd-bG1jEzsFYo87GJ6llxBx5jeNHTQRIPjYLwWqd6SP_qY8d5cdqUdWw80ZlK7GyLHD0TpmkYvp9IG2dIR5qWHY9TDW6xxfNjDF2pVF83gyCx70z9xAuWdNGR8MkJXC5l2nEB-FXnjaEhFymUdi1_v9gswd-WIJDWwAGXjqRsh0q1LIYYgJKSaMJfmV6Ca7L2NgmcYBe7opzjqWmyYOeBpF9b3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=eTlAb3wK9DsJ132q8Z9EMPj15I5_QMh_ZpxilqXq8dTrGXvN90Zo28yBseNM-mDOSjgJoV2BW9O2irihThFZAW8IvM0Ulv1GI5dEBAyaJiOqkgrJZvE7CrRrQNDd-bG1jEzsFYo87GJ6llxBx5jeNHTQRIPjYLwWqd6SP_qY8d5cdqUdWw80ZlK7GyLHD0TpmkYvp9IG2dIR5qWHY9TDW6xxfNjDF2pVF83gyCx70z9xAuWdNGR8MkJXC5l2nEB-FXnjaEhFymUdi1_v9gswd-WIJDWwAGXjqRsh0q1LIYYgJKSaMJfmV6Ca7L2NgmcYBe7opzjqWmyYOeBpF9b3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apXBTOrb95bG5M-drLuAT5kTBI_7YtCxNDGx3LQz-OGC4UePL942Q0K3t4wNIKdaEp88fnEX1hXSTF3quk6cREtxL3N0lPHwVHC0I8gAaEF-vQtoYC82YcxwtXIbEnktTAR2Nkmi2jbCAuCI2hvqIK4X45wVlouD_QtCaXnBrW7nKXPSifrnELnrJ37EiiBgXA2BM8455Zs09J2X6ORIUqwZ7swjIj6FSfN-uOtzhmSvKVvneGpGg34uWXcqjNH9akhHJqB24Sc6MuM0E0A1QCs-RQoPMjfod74uDXWCjWYBsqnggqasABChj0vxzOMySC27gupTvsblDg4Ur7YfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Po5PxYUWbHflEYYMgfbp5swMspm36Jmu9F_WUWEaFMN7sRwdugWBfAp0yAUpDZlQtyWfwjOri3fOUlsfFRZ0lM2vu98KuwEv5P6lqvLXqTIqch1e0svPyXJHc7S-GmBnaTXacRm8QzFo3xyCslrLnkyP3LVovV62nGZsT4aWnbsKqartd3SWcDHagcXFmdIyFzU3_TTaeLNLMJUl7FyfCN2zLYryJrikbvvhFMoPqYhd1WErVJGVx3ytzg2kdNSSjKcyZVVGU1eVW9ddJOEqeH9B4AUTkI0_1dbT8HavvZGeLwzb_9FeTD6866LjsUVoZS0A_22tWAcOYWPEEGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=mIODlgkENv5pnWfm0Kxlm0OTHLGrk-kT48XbVyQGnflA-ReGzYPOAt0Cw68NmhsHusDSe22VFgQIIy2Zzr9qNjsnSlpuVtun6j-1uFVC0VcrQ-a_lko8KOGZTpfU8RfOmT5ijICroQGrrwAiePQtlJxa2KzMcHAdSZek7WdS-x16aW_MSt6C3ERHC0WG6YeYDUycEPovNxXxYpdPSsx_UfIi1tQFgu6oMr6kTOWPau4FAnYAKF15Ch7Ucn90tmCurG4lWIoB6oxZWJbQ1mbrzhMrPlowhLc2nFebH1xRLQMfLNsf0__nCYrOB8vTMPcmSpy-ZVcrkJgO9oCqjnAQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=mIODlgkENv5pnWfm0Kxlm0OTHLGrk-kT48XbVyQGnflA-ReGzYPOAt0Cw68NmhsHusDSe22VFgQIIy2Zzr9qNjsnSlpuVtun6j-1uFVC0VcrQ-a_lko8KOGZTpfU8RfOmT5ijICroQGrrwAiePQtlJxa2KzMcHAdSZek7WdS-x16aW_MSt6C3ERHC0WG6YeYDUycEPovNxXxYpdPSsx_UfIi1tQFgu6oMr6kTOWPau4FAnYAKF15Ch7Ucn90tmCurG4lWIoB6oxZWJbQ1mbrzhMrPlowhLc2nFebH1xRLQMfLNsf0__nCYrOB8vTMPcmSpy-ZVcrkJgO9oCqjnAQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M--a0vAQyR1WrWPMc_6bcMfSR4hfwpQ1j-Uqtas3y9GgfhxNqWTBQ-QI2hbbrLCgXjix9RPJv48i_AXQwSXFP78nNOWecPBTiZYxUOBWplJkZB5rLaZM0Skps2P9PO9-BP_geqga83glsJk2WJ4F2yzod9xBUtgLnacwhWcGO6ocYBgkGHdzYPYzhfgoKmbPoB4nuv0i0jarEs0ZodG1n7VehV6IoB45Mho08sn-AgUPbCIGS2DpmmsEZt3OkB3BYLBdtM559JmjZ4GbGQdoxqfgv0VwmlpxTE13ueY5v2EVK_aPN1V2-aWi2SkmcmUcgidsqVA4PxY5QK0OvsX3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=f7AvBnrW77RbKGcoCULr3sT9ie6Gz_wdofoQ5O5KKcUsNMaE0JUJNHwlrdwZiRqNmYgMmKPVT0KMF4acBo5hkFK77eF2vt-f79iZKzvxPboag1Re-wDfPxsKyvMs5VNn4pYlT9HscGL35wtqNF8YAvQNkxneTd-No21IfPKugO7khnv19pjEki4Nh-9HWYc6TVYqU5CkqEL4tn9n5TUWHZifsNXnqhJnoWo8Rp6e-I5hknI-D6T7NfwAqDqJ3Czae1m3-I9qVH-FKShXn3XMXuYYQ7HnVqITtuge7n1xNX_wFMPceKBsmNAWHHmOHl24ScpUxMVBfoV02yf7D8MFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=f7AvBnrW77RbKGcoCULr3sT9ie6Gz_wdofoQ5O5KKcUsNMaE0JUJNHwlrdwZiRqNmYgMmKPVT0KMF4acBo5hkFK77eF2vt-f79iZKzvxPboag1Re-wDfPxsKyvMs5VNn4pYlT9HscGL35wtqNF8YAvQNkxneTd-No21IfPKugO7khnv19pjEki4Nh-9HWYc6TVYqU5CkqEL4tn9n5TUWHZifsNXnqhJnoWo8Rp6e-I5hknI-D6T7NfwAqDqJ3Czae1m3-I9qVH-FKShXn3XMXuYYQ7HnVqITtuge7n1xNX_wFMPceKBsmNAWHHmOHl24ScpUxMVBfoV02yf7D8MFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=hvdHw7DQnpArvuKtQkjRht67RkyrD49D9t_wRdDvzsatsLmwxdTUV7zPONMm56TPwJB5gE1Ns3jFml_7AK1E1vRtTolJAMowZ3mr4RXNQTEqhYWjEidvZJv7nZz7X6cjqbvuzyoswiP1Nf2-0a6RiUHxIpMAS7oWNArxUulqNADWgJxW4k_sgaXtagwOldke-wK95ApZc79B9zpQkKidIf5gJtrrHsQk6MwyGkvXwnQJ9RmtAPCoWhxvAYfb2KzlQsHUGIRfBP69fLpFQMmdMZ1dDcbr3NdCOowRG1kC22G1umQs_PtQi9tvAegKmpRBdfaKatO66qfD-f1E6qhGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=hvdHw7DQnpArvuKtQkjRht67RkyrD49D9t_wRdDvzsatsLmwxdTUV7zPONMm56TPwJB5gE1Ns3jFml_7AK1E1vRtTolJAMowZ3mr4RXNQTEqhYWjEidvZJv7nZz7X6cjqbvuzyoswiP1Nf2-0a6RiUHxIpMAS7oWNArxUulqNADWgJxW4k_sgaXtagwOldke-wK95ApZc79B9zpQkKidIf5gJtrrHsQk6MwyGkvXwnQJ9RmtAPCoWhxvAYfb2KzlQsHUGIRfBP69fLpFQMmdMZ1dDcbr3NdCOowRG1kC22G1umQs_PtQi9tvAegKmpRBdfaKatO66qfD-f1E6qhGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=fgj9Zs7x8BMOtO-5qaxSZkOlKaE7v8vBzwmCThlGpChPWGkUhgdIn3VaXKtEwjsfiUAf0h17L86ABaDzdMNPkBriTAs9JHqtyeGy9XXzUm3HBmh1aWKu-QXHaWiXK9RKBcV_1Tee6DHHmjmMJQeYh9TezvjVadwdczmX6GQRSO0mwXiTWBhjz0hOmld-pMHESqhkgLTk8i7UWo3MoohJ_FVCzo5-Mj6bcOYDxhycNyVCzC_7YXcHSMBh4857CqGYrHF85ape_OOmIwNznfY4J_sEWzh5LXuXgBmeU1NmmJzkYHOevqraPN44qQ6VYy2nhznc0OFvOXg2KHfUv6HuPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=fgj9Zs7x8BMOtO-5qaxSZkOlKaE7v8vBzwmCThlGpChPWGkUhgdIn3VaXKtEwjsfiUAf0h17L86ABaDzdMNPkBriTAs9JHqtyeGy9XXzUm3HBmh1aWKu-QXHaWiXK9RKBcV_1Tee6DHHmjmMJQeYh9TezvjVadwdczmX6GQRSO0mwXiTWBhjz0hOmld-pMHESqhkgLTk8i7UWo3MoohJ_FVCzo5-Mj6bcOYDxhycNyVCzC_7YXcHSMBh4857CqGYrHF85ape_OOmIwNznfY4J_sEWzh5LXuXgBmeU1NmmJzkYHOevqraPN44qQ6VYy2nhznc0OFvOXg2KHfUv6HuPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzoKmJCeYRyz0IVyTzVGPV8V4rgDwP74zjOm2ZcicRvKLqe4U8qYAi8o_34P5S6N1ei5DjjBG1IQ5CFlXM3A4KaSvIwH8fHZJhWlqjUumbN-kEsLfPwHlg-VZjExyGdTyh3D-uI57fw5cA-6R3SJOz1enmGCwe3AtZw1peBis_kMDKoz-ZeGLb6uJd5dNELxTpG7-6VM0wfEdCWk2imQafYGYWqJ_NlS_Z2_z7Q0ki7LmNxOu6ryDXr7usyv0-OfvGDXFnkqsn-ExLm0kdFsQE7n_rCrGgzBrF2oXhkvOih5qYEJ5SjWG4A-ieYfDMIk-YQO_E7gVCpWTtI1kfv40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWKHtD8qrg3gXnLlddgzFaiFQjgDp2Q5xc7oM8ACm4R-uEUWxEB7nxi0gkNRtFgBTBudUtrTXZwZHyn6Fcunk3w_wGnpPPjQEAxwhp7wEPtsUd8AHYNBIRgVbw5sTcHdXDAOw8uhC368_SDgJ1OHKUs-1aYp7UlD-tHSYqcIjiP0-WGwPksB2C7MiDT6B60irveXETbc1ZC4C7lTMfXZB-Yfv2dDVsnnN2rq0zS1NDOTSZ5h23O68eyUesxJ1xTQiAPZw5l4_Y77eQAM7VRPFspYULFIPFup0RnEBhJ5jVtxDkDSf783_L22MlvlNQVuKGOoCUhkHGZdWgmi6a-fPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbNeK28lBxxZcsRbvWRONaolOhNeSeciMLVtudwv2H9wGF9Mq54NH4pmIZuJNQ9jL8gXd3Wy__zgiDkYY0WtowOaCFnxiXOw2CVj8Oe3U4pVJGGLwqej5w0fNBCQsu_ZguboTxKk-OiK7VovYA0ks0XQQCEgow2rENm_b3ids6Ne_xLdlXCXRbAVVn3RHZqHQ3wavW3Ce1bVF9FVd4RZN1PEpTDxxDzAPoRrlV1hLFwXiJv9VYzGIK1rYJkpCeBPviwYdkXj_JbDXYXaV55TsVP3umXIN-pI4rbQA_txNykdk2H9YPnURgV9Wiv1lN4XYnXRI-byUtdq0wK9SIKpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=D6CSwcVezHAd-bB6IRiIKvG8rRI12XEx3OUvJ_HgO97SdxRs6j4FLlqPImMeXMO1j2EfAlw9ZTImXLZmaQPQqg8OWd_k-0r546UP31ziMZAWY9Z3Zh12VVNNvtL9ycm8ttMmI65s4zxhBUpaszoRFxtB5cEEG0tVD1tnzIBRq6rrEuOYHoSS5FjxgueSevnhYS8IWB5__fAcYEX-4OgEa-h1HXzJ2XS8s4AzVYFDk3x8A3EJMe4quRaTe5oPP-SXaXjs4ZPf3_JsC0mVirSk1SAm5Pbav3FqjOLZuldnNy49pNEta03dKdEJkPSnbo4eDMjZgOD990rA34hoUKxgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=D6CSwcVezHAd-bB6IRiIKvG8rRI12XEx3OUvJ_HgO97SdxRs6j4FLlqPImMeXMO1j2EfAlw9ZTImXLZmaQPQqg8OWd_k-0r546UP31ziMZAWY9Z3Zh12VVNNvtL9ycm8ttMmI65s4zxhBUpaszoRFxtB5cEEG0tVD1tnzIBRq6rrEuOYHoSS5FjxgueSevnhYS8IWB5__fAcYEX-4OgEa-h1HXzJ2XS8s4AzVYFDk3x8A3EJMe4quRaTe5oPP-SXaXjs4ZPf3_JsC0mVirSk1SAm5Pbav3FqjOLZuldnNy49pNEta03dKdEJkPSnbo4eDMjZgOD990rA34hoUKxgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=lzm-S1uUDj9mTNoLiSxmV4vjcl7S1TnZDBxKEmvbwIKASCx9yZrSPpOXGKnlwDV7Y8-sZMv-tDfMX0Drnq83ZibeGg89X5ZI846FaK83-siMZOd1qYMrnw-S7NPvhNQjJ_jLWuK9sKEegF-sNi7Dfit5rxkhTSitoQdQOeG390aECFeQi5-3MEdww4EoOFa9PXHEuE9tZi062eCCjhIWFl_30EUSc7oTy-u7UJAiLvgZ3oSl5My8j0YuOfxBIc2gjQS1bbNcQ39Kkfcdlv6umLivUR1gXyWOPkA2svDo_6ie683W1wPw9A26hh_X9kG-sZoZEea8-ldYzW81fUBqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=lzm-S1uUDj9mTNoLiSxmV4vjcl7S1TnZDBxKEmvbwIKASCx9yZrSPpOXGKnlwDV7Y8-sZMv-tDfMX0Drnq83ZibeGg89X5ZI846FaK83-siMZOd1qYMrnw-S7NPvhNQjJ_jLWuK9sKEegF-sNi7Dfit5rxkhTSitoQdQOeG390aECFeQi5-3MEdww4EoOFa9PXHEuE9tZi062eCCjhIWFl_30EUSc7oTy-u7UJAiLvgZ3oSl5My8j0YuOfxBIc2gjQS1bbNcQ39Kkfcdlv6umLivUR1gXyWOPkA2svDo_6ie683W1wPw9A26hh_X9kG-sZoZEea8-ldYzW81fUBqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ZzC4sFmuJ-cz_8b1oLUI1IuyZLj3DYpeiBTZEdDuFKi2zq_71kTxBHN9TE_u9oOC1y5fbH7zBEACCBPICoGZOYCazEl2Ettj1-OHcbvGPo7Ipeq_3zxnVgT5KmqGEjRVwB4KAasSVbRvExy6cqSPu4BGLFw7ssi96NPADkxwPcsxy-NUwBoMm0GYb9rXK91QcU3oonEliO3fChKqhJbH71LxNZf9AA_8t9C9dhWjqma06BhDIu0L91d_ft5a4FDv7iguFBJM4k9h3AdspMeA5fCkArAcnrF_MukMFH3iotSVFv-Iej4RXUHcz4xZ5JMdoiv5rfeNPIlgQidb6FFiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ZzC4sFmuJ-cz_8b1oLUI1IuyZLj3DYpeiBTZEdDuFKi2zq_71kTxBHN9TE_u9oOC1y5fbH7zBEACCBPICoGZOYCazEl2Ettj1-OHcbvGPo7Ipeq_3zxnVgT5KmqGEjRVwB4KAasSVbRvExy6cqSPu4BGLFw7ssi96NPADkxwPcsxy-NUwBoMm0GYb9rXK91QcU3oonEliO3fChKqhJbH71LxNZf9AA_8t9C9dhWjqma06BhDIu0L91d_ft5a4FDv7iguFBJM4k9h3AdspMeA5fCkArAcnrF_MukMFH3iotSVFv-Iej4RXUHcz4xZ5JMdoiv5rfeNPIlgQidb6FFiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLMLlZIWwAgaTfp5obziJOO6hNfzx6AFlEWiFCM7MNSFasVnK1Mrmv4mI9uez7gZZ8Z5i_eJOHV6fHp1HSkns2jGoWf12Lk9ZWeAtbpxx-b8Biwn1J2NA9DuG1azdIJOnw80NPT-7AjSrjCpoIAT9y6QU3RauVmnlx76oRVsZUbGTQmslHFPmpPhyFUEd47WvjquUsoZrAEw5F92krO5BtRA7GfuFs7WF8aLg9zcZ7ryrg75mPGQar4fodhXXyrwmbm_FONiTB1c32Gav4HEXHM3AmGkmFm4bD4M213pYNWQ_DvSv4r9ONI4URIC5rJCgssp1Gj-_gf2A46H3kpJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhE-E8kBY35SBPMxu9eXWOQFgYxsdJLCVt7RljtQ8Is9TCR1PB0wKoIV6r-0Egrbb1VvlImeXBLuB5Y4wB9_srkqn6wpH-849QHC-JH_d2J-ViV2JXCcJcvOMpdCYlCZ-5w12VZ2l_P7VGrqx7lDoSZLHWpmCdUMnEQ-3ca_ZsAUpB88U1NV_eAx4zJm6cXJBx5-I2aQG4ipQQoXrMEbJcV8kaCUUlBvJ8afxBJ8aPAuCJymHUn8FEbez9sQz2cAt8vBQpI-OLP9Dd5DtVJT_bYae0GPmcgMJj5NbvWqXuI2_FVy-qRnHfGgJeLbNt8b2OdyUrzd0Qy_Bc76gJCESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMRGgQUAjtIeVvqLFZ0JPf-vtrQHH0NeUCqrtKrOOd12I_9RrhpEbdS-54myrL-D1nFE39VJfarVU_RlB-KegSYVAzcbH9FjUEUVScU2pXnt9Y7fsFewS0K14lQwxvHR22YRbXIds3VsIivmZoTdfyLZ0NJCDvgJZ-RU8QvjmdGGbLHWPG4tV9M7Igee32jyM1VVfR-AJpatI4QmHyYQE4Ay79kSlPD3BH1B4xdDWtKTPc_LndlMobVgHZrd_EY479jFjX0K4rFCcYBtnKQTVisu_00w3-fAXCDm5wY19sMpqcPgGdhwSduNjzi-sBCfXrg1kR1jA8T3iXQOsRmmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
