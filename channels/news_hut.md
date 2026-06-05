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
<img src="https://cdn4.telesco.pe/file/qeghiE8jeUaI8iy7zxIkIG0DnkQ3UgsNuSCjJ2lwj8uOgij4MwKXcJK7gT4TA29EGphsBdLksGURx2IoiQzq_ScWSecjUzg6EOFPGiEHO3Zs5ZWma1jYXre2Va82CO_pQ1caR4nH7fEIY-ZovabaB6OvpJX7sYmScLjup-95iPuAZL1h3uHTHCR_9MLHX0xYns1e5nmu9doYWDXZKCrHATJB4JTL7H-dDqFos3eRjqkNpxNXbpfKnpNciYVms_GOOkKb_Fv8hYuYRR8SfYxxLXlaODCgBSyhErSFs1KIn-3NUFgUK_hGbQDpXO4AFq3M6skobeWEu0l5Zq373IA9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 03:13:42</div>
<hr>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4ZD0Y3Efj9HCxDsHNectq2yecEM-BjsYiayyKOI80AB1hFyTkVA3nSpN2EPfy8SEAW_mcR8PTxPZMXUZ8J4yrb5uwiGwEIdxkhtvp54aly1n1d8U_sS1ggmi7CoLWKXn7KQoAvBPFZyMlk02bLYVvj5aPNHkb4uvP1o4iT25L_Qh5SPiNGx4F_eI_SqLddVFwwbnYy_2f87_5Yc_ID7zHGxHKrReFWGB5audEd6Lfs3DFOlSEWA8Kd4nER-RWDNM0moA0klptKYLBd5SdobS69bhp9iv2RSLTKeVcs_ZUGU-L5rCMK7oTh2df1wbYKc7wrFqVTVBUgImJxNol1P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5enZftL_oUXzwdzfG104wQSgK1hlaG7wAOhvSZf6lENQXMP_kLhYGcli0jS8xfSIXxt4juk2Tc4lvCAMih1sTMVZ2tQLnA2M_VQXJHunBqwfKMyrB-7GGJVhaxAeyJBPOVtq_-IHOBlAndaqigbAkY9V2kEyzRIYxc8HCGA4kT6BZA0bIEnnhPc_Gz2evaWJJ2GWlQpOihsh2pDUo9JQtr6ygGC-xd9hfoPCHfjdErvM96k4JM2mZrRaEJlI1cbeWQipsP582qZeiemccnLJGc-5RnxEb6i13lIHFGz83aNnuFdlc-QZvp47ZvtP-xqrIYkQXxbQeOa799rdI_-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
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
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhi1INbTD-9KGiid6nSyRXysoyi90ao5Atu6VcuzAbXInzeUrKW8GrsWDN0r8qjn3v_RIBso6Unu6xegfDMhBaTdomDlGgKuF9krbP6nAXk1cpAxQ6b1jX642AeTAOl5wlxkaHXSMDpx9BgLHL-juKbcoJYg6pXbcxj_onu4PqwsgGMOr5xcV4-3p10erIV4C5zGDyzaabAnzKUQy4IyTCXcI-jZ_4U4sbxfupiR6ZWShkzbkghmAurrUFHhreTwYK-qL-8Hf3AcKnqnGutZq8GehrMJHWtnoP0u-OFKbBX2UGiwgEyYU005pxEbYpW11cqh37OcQIhqp1um3NYhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVgeQmSJWoXiQQ4u55m8BLoCSUKZiFhV6si8msKnpA22zPz9Ruix9Dv5dNS_MRgzRQEIEiv7dCI4TZ1naSc2qlWhIf1i217mw_b2fJx2oixn0uHKoC98cIlAkJFCwlDlhjNSn2dzwH6AyEH2EZNtAY1s8GAmF3wSRFeU2-LuFk1h1S7HlLzcrSmebmWP47Fj2tLwpxusfQIhJ-9M-Yk24Mr9V7xkLoE9T3DFxSllroZlW1XIIsqWV79huCgl1n4gn8gER5pCYTHonCciMDUk84hgOZPI_NrXjyG4YgTWLwivlunSfQH0b67rbVQ6wvnwNCVq1UIWYM77Xy94WWCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ru0uFLg-MjRQdRgTw19pAyHYgJAVqqpNywZ6lU3VD8FlwTflCvlCx2RqP3s0cPf4a9T_RT2WFeTvs-xhBxbDW_CKwrrxOKd6YbLQvG-VceRVL1nXMJ1ql1xgocFwQnS4hQMyuijhoTflwi7yFGgyupzxZR2puyK-VBvyMlDZ3B4Zz8Qx90r3P0yBELi60tSaAbhrhIy1cER2wzm-iSLWBnGRj3alzkU3NGpkQgHhhKuVaHrc0s1Hl-jUZvO4PDqs23SBMxxee-EfZfM-b0QGNIjX4W8_bZAejUReecmBRP6HaP8qHdaMmfU6JTTtyHraeURjLnH-58Rj1oXEsQYL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ru0uFLg-MjRQdRgTw19pAyHYgJAVqqpNywZ6lU3VD8FlwTflCvlCx2RqP3s0cPf4a9T_RT2WFeTvs-xhBxbDW_CKwrrxOKd6YbLQvG-VceRVL1nXMJ1ql1xgocFwQnS4hQMyuijhoTflwi7yFGgyupzxZR2puyK-VBvyMlDZ3B4Zz8Qx90r3P0yBELi60tSaAbhrhIy1cER2wzm-iSLWBnGRj3alzkU3NGpkQgHhhKuVaHrc0s1Hl-jUZvO4PDqs23SBMxxee-EfZfM-b0QGNIjX4W8_bZAejUReecmBRP6HaP8qHdaMmfU6JTTtyHraeURjLnH-58Rj1oXEsQYL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OehIvZkB6AMJFtJ4xHIgqjOX8ofQ-BeWnrUPlUPoRFCUYuEYubiKNA9cTcirEY_6u8OrNf1B62GDvUu0iAVHlgUdcTBBbLC-1vdV3yAgsHEQoU0VTegx00jC7pw8vHGrQFhUOsDFdh5jPOJr76igBKnQOTz-QQK2TdkGsGh7upl3e7QmnPaBFKD716ZbdhoQVKmJOrIx_W8f7nljK65hOfMEigZ442egqGq-vnFtbLOvZUw8H5TD0_JmqDK1i3Oyt_N-CqMIbU5ItdROz2PoivFJ_owxZgKj18bpxC-0RvG0ZL0ctvp3YeLBEZoSMMPURU18y8I-841rHtxKys11JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A4R2AsnA1FwKqgsMerlpwj5RkB7sTtp_bKkAfYNG1qDvd_DbyvHEyF_rk6yicSG9hdRHOmh7uO_EqgJG08lEFGzGUiD5waY62mel4Bm86Pn8YMq1ywpTvOUQKk6HzmU1RaihPh9AkdFOkJ7w2auN7dQGuO-avm3KTXAyYIWtNe6-MCOtCu7984wwkeVZupmDDVEI5hM8p-32-gxG5Xw-Krn8mJQDwdS85IklDdMvIQpROSAfpHne9VWN8HK0YnAh9t4arIhbITNWoSuk22SPsiMT6so8LcHm99BT0A2-1nEvm8Xx6Frf2CWSRJ4OUlapo1gwj-m-4-r87hVx7UQpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cDi66_mNSLcCd3J2g1GblkjelDaquKpVGgGb-qbv0O3-OAciAM-Dn6NF17O9xr0qlgaSLe833oIv5YBg6Mx0bDbmtLSLmGffMGFtU8kFwV-I4ijy05uaTgWp621KCIfv4x9Tp1ygBUfw9QLJhW3j52ryN242FyEMNfb9r3bfzlGsuCD9esxb_9QvUwLfSM0s_5NBuvhuJ0o1WyEj-Q6o82K0ZsfAUCpiiJLCGru8110VJZqqpoZP9Vu6f6lppdZGQgFi262BweqO9_YziNHIW7ytGlaWNlOEoKu2XNGroB72ZpS6V6qyq2vuoepfzfLL4OJr3fT-FbqaEA7D46BFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nT_GuD1h8D6GxcagBaznAHidqU4rfFGtGufPxumde6Ku_l9qKgsCbohHR-DNRTrRVwnu83T5U1nHYNaGt5Q1VSphvZZDduqksx-Rryp27VZpbD_CoU7mt5p7Anj-bN5Gs2KXv0LKfWMaFR67PUbLdysv3b8IR8cyvFxDBIwAr54MCYTa79N-BF-Dnjh9mQ2fIdVKhVnjVL5HnkJUb8cy0H87YjCeeDwB3CCgYfOz8rOD0BiWJDBgT9ZZtbQCewkiFymyZXNyeG85QDF0Udh8XStlJWwSXF25zwsaYjJTaiIHP1LjbEUp-1yNi7pZM2iulmKIV2sJeupNOPlVQpnCJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9A-v9wbyl0UxMfufyme9Y7dV1xIX79ALbikF1noLO03NUWlb9Qlk8IlTSaXaObeLBoFf8Mt6KnDABYPwVBomTIAaip7DuypKKQlPPsAMvy16n2rr6tQXZcko6DCvxF_U-FVS3sClxRqNNE1x37uKft1sKSsfFT-JiJmZAh3NUjkC3-Tb8S5ce9P-oVfQlYMKWvDzYuIY3YkBlPTcXWcB_8JwGMKKaZgQtoyuqz-4ZGl3C4_EZMMVWd-jyrN_RiZrQvUt9b90LPf-0OJ3RQz9lYyYW-lSF_2JzVXRQTX1_EPSjQTwOjj5ffcpAXC-dBZcTaUJ33Fulqy_ZHm-Re1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=RFHwVinMtcYGuqQEwJaqb7EHfnNsYo1tZkbaym3PzGNrtVXwSi0GjkIjHXRbTh17DN39qgHJT_zGVQOZQtv9wO0Iwq7XoDQoUKhXaMYG-CK1VbRhn49pq0DPHTyf8H0H99Zfkw6Ic4ZUoikUlRUco5paUxeoIvpG7TB9TQqihCTSvJlUjWpPdy4kk-ucetLtQPZlpSrwwAjcjPspc-Bk_Yd1OUKVwtPKrM2Ipv_q8D0nrdjPqr5FXerq-ICO2eRcucI7koLF0g7KrLx_KcvYJYJzzCJsAUOTwETW6wWF_kEIQxSLgWrpOE4_yZseiQkjw4a0_sxL7D6_5ydXfxJC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=RFHwVinMtcYGuqQEwJaqb7EHfnNsYo1tZkbaym3PzGNrtVXwSi0GjkIjHXRbTh17DN39qgHJT_zGVQOZQtv9wO0Iwq7XoDQoUKhXaMYG-CK1VbRhn49pq0DPHTyf8H0H99Zfkw6Ic4ZUoikUlRUco5paUxeoIvpG7TB9TQqihCTSvJlUjWpPdy4kk-ucetLtQPZlpSrwwAjcjPspc-Bk_Yd1OUKVwtPKrM2Ipv_q8D0nrdjPqr5FXerq-ICO2eRcucI7koLF0g7KrLx_KcvYJYJzzCJsAUOTwETW6wWF_kEIQxSLgWrpOE4_yZseiQkjw4a0_sxL7D6_5ydXfxJC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxq8wiJouZdUybB-E-_oW64PQsAD9ODxyxcZQdLjL9rh1RnueRu97bK6rF-todr1iZLKCopQ2QrQDtagnHXMx4Ga_7jqfLOVw_JMLWqF15ZJhPMKYOQpSz0KQv8l6NzRx_jvKqKIHRCybBtqjQfSC86lXmX-L5D-UFJb48NGExYm2Tu03ur6DWOFyTnV7tYQf-j2cQthIg5ICeR6XNtOl4nUEFBM0bJMApryZ-IMiszpgNHyOt2-Z1vQEEsy3D54T0sIzoeKzyvL0J8lDiK2pz8rKo8EX3bZtX7hT6er2oWRJSQuLqEFE-dVAhnbCG3T34EorRSjV3nzJxK_nHGMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=vgzqIJYr-tXR7nLxrHjNIoLdg5DISYMov1V59Ra_yT2JcELq6RtJ_3-JpmfxGtk1LJonSPRBD-zAe8PZM-n6hoxy0-ph8UNL2l_tXJeC-nSOUhSfd2T3_2-JkB2Gy6MHG_0GSRSwYYi7d-D5Lz6yVqSL9jUAOulWCc9oJP7jft51Jam9QjiGd0XG4pPHqFlBjxuR90R6tEqAsg1iWpkS1oqmhFokR6IuUx9Ro6n6gmQWtORaIa88pkjsKIdYxi_xrEYfwLeybu7wTejftg35JL4-T7QL0kvjdAvcGl0Radv6RBnBHx2gt6lRr-qw_L4B4k2N7bFzNm7gnchGYgevlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=vgzqIJYr-tXR7nLxrHjNIoLdg5DISYMov1V59Ra_yT2JcELq6RtJ_3-JpmfxGtk1LJonSPRBD-zAe8PZM-n6hoxy0-ph8UNL2l_tXJeC-nSOUhSfd2T3_2-JkB2Gy6MHG_0GSRSwYYi7d-D5Lz6yVqSL9jUAOulWCc9oJP7jft51Jam9QjiGd0XG4pPHqFlBjxuR90R6tEqAsg1iWpkS1oqmhFokR6IuUx9Ro6n6gmQWtORaIa88pkjsKIdYxi_xrEYfwLeybu7wTejftg35JL4-T7QL0kvjdAvcGl0Radv6RBnBHx2gt6lRr-qw_L4B4k2N7bFzNm7gnchGYgevlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=QMuMOCT0Qu4E0aw01Awkq9Do3y-cbAx2n2SyUsWFQJ8d589FMXPfWCgdEQeb1oUub4wozNyEpzIhQ8r5wbYeaMsZUauf2dy9nrWYNNAbcSYT_i_7pEEWGItv3vQBBX59e8SQeyUF5mLXJuvMoyAEt_Qf-8eFZhgccyH-E5uhpLvDB7KgZC_aImg30xSJHJaiEu8Zh6uvZNa6gaOdDkQ8BM4hUmZ-XzxvnCAy_619R2srsplxPhiEtauQORj0oB4_wqaQurz3A-XDCHSIvB3L_zt0nLr5V1_a-8i2_IOhvFx5CEkN5qxSCgPyliMWDBp3AVIrSGzrpGx2r9zI8nY5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=QMuMOCT0Qu4E0aw01Awkq9Do3y-cbAx2n2SyUsWFQJ8d589FMXPfWCgdEQeb1oUub4wozNyEpzIhQ8r5wbYeaMsZUauf2dy9nrWYNNAbcSYT_i_7pEEWGItv3vQBBX59e8SQeyUF5mLXJuvMoyAEt_Qf-8eFZhgccyH-E5uhpLvDB7KgZC_aImg30xSJHJaiEu8Zh6uvZNa6gaOdDkQ8BM4hUmZ-XzxvnCAy_619R2srsplxPhiEtauQORj0oB4_wqaQurz3A-XDCHSIvB3L_zt0nLr5V1_a-8i2_IOhvFx5CEkN5qxSCgPyliMWDBp3AVIrSGzrpGx2r9zI8nY5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=MFD7esdWGyBYSUbzRM9L6x8msLOeUPPsuRKuWSGTSLaeYoxZoebqzE0NohKUh8L4F3LROr9uIiJBNUsJ-K2rcoBd9iqSV01fLYnv1PKP1Lccn4NNtSoL4GEa7XmgsxIe-JmKtr_zDzIbi0VzPjlUF9fnPde3VmnDhrte6e_wGnZGVWnYaOT8spOL5VXebpr3cd2Z5GSPfQ6G1wzbFfCPpge7_JJOcPeNUdxg6rd2y3GMWsazVpalZbuT7QmCUt3WbtBFcV9Ij6pchy7hfuvm8b33eaw8xxn9DxABIPfUq_tsDMV1wGzWY-nce-nttebhNTJZKawTVqXlqERJQARX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=MFD7esdWGyBYSUbzRM9L6x8msLOeUPPsuRKuWSGTSLaeYoxZoebqzE0NohKUh8L4F3LROr9uIiJBNUsJ-K2rcoBd9iqSV01fLYnv1PKP1Lccn4NNtSoL4GEa7XmgsxIe-JmKtr_zDzIbi0VzPjlUF9fnPde3VmnDhrte6e_wGnZGVWnYaOT8spOL5VXebpr3cd2Z5GSPfQ6G1wzbFfCPpge7_JJOcPeNUdxg6rd2y3GMWsazVpalZbuT7QmCUt3WbtBFcV9Ij6pchy7hfuvm8b33eaw8xxn9DxABIPfUq_tsDMV1wGzWY-nce-nttebhNTJZKawTVqXlqERJQARX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=YOKLPmfaFmAS4SvG4zOKx6yUhwagQdRQ01ztAxB33SZCvltF_pAVUGCyHbBsvpV4XB6X7hO103o_yyQrWYtbkSAGAp4_AfoNHpAQnrWQc2EPjJqkiXmbMoy_e1cZmC-W7XdbE2Po685h9HXhnVxnd2SJ_Q9nW0LmzV5qBF0J_sU4F0ToqkZzRwwBrcKrWf5qYahRYUrEdk-SQdtjcUF1e2IB7Ek6jinYfNXwI0hG0BHdP6APpVcCg1BmRHfCSRXmgXy-kcmkR_H-x5ua75v0PrlzrOp9zinIA13kt_3HNXeqH0hrpnUuLIXHbNZGgCgxjcbp0sPRzm1_4f6McGYcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=YOKLPmfaFmAS4SvG4zOKx6yUhwagQdRQ01ztAxB33SZCvltF_pAVUGCyHbBsvpV4XB6X7hO103o_yyQrWYtbkSAGAp4_AfoNHpAQnrWQc2EPjJqkiXmbMoy_e1cZmC-W7XdbE2Po685h9HXhnVxnd2SJ_Q9nW0LmzV5qBF0J_sU4F0ToqkZzRwwBrcKrWf5qYahRYUrEdk-SQdtjcUF1e2IB7Ek6jinYfNXwI0hG0BHdP6APpVcCg1BmRHfCSRXmgXy-kcmkR_H-x5ua75v0PrlzrOp9zinIA13kt_3HNXeqH0hrpnUuLIXHbNZGgCgxjcbp0sPRzm1_4f6McGYcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt74OvlvRjuJmKaFvcaUSSC6UoV5U5k4iJpRLr2oNJhg2ohcu8l_j0jJWLKXyY9gbNCzzR_rHrElvEuZb1SeT9QXf6aVMiyyf2gi5Yy9KKULRvSVBm3OxtN_xE-AOngRd3WzQwRwHVF8J0yxu1_CEqSeWXsSy4gtwmEUB3KyPrRGJL4v6_Z3X11s41Gjh4Snv97rxKNK4WAoHyEuoaqPloVGWo4cBlihzShogCB1-3W-dn7DQ8PL7HYvom-ryGNuwC-tQHRWg-dwsKR2y0sovia6Xsps0wCc38TOFygJgp4YeIyySFEo7Rofo9MQqPPVLr4u5HCuqUHnskEAMc-S4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgmyDa3X7TMg9sLdecojhT2DHLAF5HseX_sAB9IztrEwnETr8fqnsEdWh69PKgJJqNj0UKbGFDU869sUXyI60pjcU8Z1sF2KN7rioTGkeFv6YdMVicN3geXSAK2wqlp3U4M8Prt7zbVqcCT6vRimdvZJPcOBnh0682cJF3XifXVBU9BVVNBS1AD0qI4Zsz8ARmw5q8Qs_Bxl6v7WQo4aeRHScx_se0q11EdntNi1WpqoubVLpM0ZJJ-fUThJIPyYv3gMXIWEEnKZRUhxss9UeiTUKW-gSlYYfPOHVD3Bq_VMdtAwZ83GgWkF2SVSLzCSlYLeRV-pPK-32498Tr7FzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI1asuDjy6ZfrH5hos1XLOMbg43-ldrx0LSvC7H2jdJC1ALmM6fcnkmUF65mqWA6xuvjwUXD0N8ZNnZplRtuLSDIv1gtnDyPCKIjRgGdqNZuMHC5_wxzDifuVogt-52zBXQw5LlbTymGfmF8fkTQq0Dg9jtqgpXs0iDlu9EpdB75EpdqU-s4qYqH7RH8TU8X_3chPBuDutckec1Pw3U5VmK0d6uVgxQ4LJMq9pDoEo8RTivQEmVdHJE5uWbJi1T2pASoNlf56lEncsaYRVoe_i2dXr-2BeABwyfFKsVNYS1Y-P_BiLEnqwqwylxnvan6NIQMNR1tSgc9XWZIJxk83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=NkuNcGFML89DeGKEWhN3NbC_lrMqkkMW30H4DxR4qNCNW63gssf7MfDDUzmQ19TBYfHGVmBYBA5ygH9V6X0g3gBxZYe6_5xYf4K3BFiJB80xk_0blFYXbpRVqfm4HFBvd6egGa6odR2FSc5u_OZZrkub5uu2fq2fDb7Z756XZ_yuzCi06TB66DWMFdu4MWSw97KtaVRCTgRS5OtsXTh78aYA16XZR5sqbsqwg1Y1fcfz9d6468Ygdybza5qXZooyOmsKtbbxtSsAZjnFbO1-jew2ebcbupCAuHj3RzOmbYepcwzNMnD3Ton1OEDzwtilm65W8X8lnyZWYPQ5EDRlQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=NkuNcGFML89DeGKEWhN3NbC_lrMqkkMW30H4DxR4qNCNW63gssf7MfDDUzmQ19TBYfHGVmBYBA5ygH9V6X0g3gBxZYe6_5xYf4K3BFiJB80xk_0blFYXbpRVqfm4HFBvd6egGa6odR2FSc5u_OZZrkub5uu2fq2fDb7Z756XZ_yuzCi06TB66DWMFdu4MWSw97KtaVRCTgRS5OtsXTh78aYA16XZR5sqbsqwg1Y1fcfz9d6468Ygdybza5qXZooyOmsKtbbxtSsAZjnFbO1-jew2ebcbupCAuHj3RzOmbYepcwzNMnD3Ton1OEDzwtilm65W8X8lnyZWYPQ5EDRlQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdTrX3ACWz7fnhMG080Nfe9Gpst1O-Yf7D0FQIeL2AAV5BSNRvMA_lSoaDpQC55NfZY-Ryhr022YigICi8_m_p6ZCb5yAo2aAahT3_eIoLZKQnsz-4_GZEuoIp5R83WnTaeSn2uVvzQ_XSc6VuvoI_BI9pRc5kEqPbZBJlKtZltHTtw28aLjO8wWRg0p01fKxsgbf4GEf-mC-f213OgzWL4Kc3GQUDXPy2bYWOX-gwLLACzVxxAEdaFjnrwU1UCtRoHVDbi3vJKfgWJJiq5iVpx0fnuBYEGZk1hibzPoqDlQ6JJ2277TjHsiRd7x9W1sYVHMoEZKuXLIYQPdjBpsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
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
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcMOXZX_sS0fHjrrCkKHgsOWTtM-KteumoLAHaVr0NjAVIt37Yh1DvZHgdf_uCHDvLuGOnJ2MejIhVZpWJ15WFL8IJkih_irQYAUUtHbY-cgFqnH4G6W5plhruhdNfPLSLBPoxq-3RVoOWL3lEEGMHrUVdsgS1jPUE8buhn1gn9TYeZudl984dJ5ZkHLmbkoJP6qqqDRCQCocQhDTTsoiwNrJF2X-NkedC5NB_mLuzSzqr-zvkksQSUHXNdcB3bwCbupSVqsPzRhCcHosguvojf8giE87ajXiroxOSzVPXmHyC9RwuwQPS5rp1I9xhIyx_tuIug9lWjazbBw9LxY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0AYswjWSQ5ZYecrcC8Q8l8z5_e-MfQhucBS6hKTGnc4wbuDetIS5gOjfcyM-bvFhofmU4fEaHpVw8dxnkhq8mCRjvxyLWaSeQMno4OApUYpaJO_5iGv7QzDBDNwc46uqnth1xHkCQV26ZZgXvQ2aK-6HLckQYFlvvlRkRgiDuW9jK4uVUJ9Je6sytsAtvgSuQOlxfOo6wdIOJnG6r9cgZUiSZ5CpaWTSRTIyAQEb12db_FjI6nPY4O5QnYk4cbsSjNGvLZYR_kKnDGAEzVuR9sWaUYy-G995u2SQSBcZJfSqG1vIK4ZONz6bJbPQ408juB8A-HR46LxTaNJVMjqlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=AlsfRrkaRrEMXXn8zU6HQ6_R6KitVr8-3qOKFLMUFlPtpEmuNKZLyaSr82j7peJIMcCeszTtSaAaXWm5HMDBYNa1Q_JF9voRgO9VZdgqXiQ7SXX39kPusj739TA6_7L_1PPe870rg-1EtgOyAiFWX0l3lMK6S2RcTG9TEH2TqOuK8qLmx6vzgY3_-SFHClCFQ4zQIN7nEJSzPgcC2VKuxGFt1rUrUopOK8-VvdAD-eEWPhdoaKeWGC099QEObO9I_gWIUFYtE7GNN7n_Mh4pCrfFtaFZRhX1s-FtLYfi4qNp6rmjG9oEjr3LcTWAdZfoOTcZA0AzRbur7sFarJbt7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=AlsfRrkaRrEMXXn8zU6HQ6_R6KitVr8-3qOKFLMUFlPtpEmuNKZLyaSr82j7peJIMcCeszTtSaAaXWm5HMDBYNa1Q_JF9voRgO9VZdgqXiQ7SXX39kPusj739TA6_7L_1PPe870rg-1EtgOyAiFWX0l3lMK6S2RcTG9TEH2TqOuK8qLmx6vzgY3_-SFHClCFQ4zQIN7nEJSzPgcC2VKuxGFt1rUrUopOK8-VvdAD-eEWPhdoaKeWGC099QEObO9I_gWIUFYtE7GNN7n_Mh4pCrfFtaFZRhX1s-FtLYfi4qNp6rmjG9oEjr3LcTWAdZfoOTcZA0AzRbur7sFarJbt7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=R-DKK3DvCEPXAexUVNL06eK2WlVnpiUE10avWfNgslHyo2IrnnojK1snPjq_eSRMg2sfVY1ByqL6PK0bgK_vOan_EYEjiONYFVNrnhLO7oxW88CZezKCw5ihfEtd6L7uallMO8EwlJcccZ0fO2jOp23sVsjnQcVMfQWb2C5oiWv9wkDHA3NT41UGTIjL80ma7lWtbaJvnRov75K0MLBHWMDjj2wVPA_eVAa4-QlMuIH1mMHdg61MGVLam3C1m1S-nCEkzCPBbO-JOySjEXpc1FgFE39_WVSlTFu1UvY_mRU5nlSJBaOBfUrh7OYDxKftty5UnGCN8wwlOmvWF-Nq3l3esJLiGXMCwY6qluJL3qt8WZ7sv971sWF4E9ExBi-fBeqwZaghEHWvDQ9wrSzau2xNiUuc79GkDmEaVxN4kkzCwQEYYL8-qq-hLT-OZdu6dkgDppQSQaXFF2uapxx3-6QQ6yVNVk8HKJw54B4OO3Ax0vFsALtP_abuApnPGPshnRTceoEnKwbBcd3JwtwtBkXg3bI420xW_w_sUrx2qYMcFmMsp6rn-soW1t17hA1C6_x9taVtdje-P1EVylV8n5uFSgmObHIoTezHHho7cs-tAdzRx_p4E_BZdFlBt43j8IlRiTbUvIAjarV6O7Z_jtDTM6SGa05SNGorDhGNMKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=R-DKK3DvCEPXAexUVNL06eK2WlVnpiUE10avWfNgslHyo2IrnnojK1snPjq_eSRMg2sfVY1ByqL6PK0bgK_vOan_EYEjiONYFVNrnhLO7oxW88CZezKCw5ihfEtd6L7uallMO8EwlJcccZ0fO2jOp23sVsjnQcVMfQWb2C5oiWv9wkDHA3NT41UGTIjL80ma7lWtbaJvnRov75K0MLBHWMDjj2wVPA_eVAa4-QlMuIH1mMHdg61MGVLam3C1m1S-nCEkzCPBbO-JOySjEXpc1FgFE39_WVSlTFu1UvY_mRU5nlSJBaOBfUrh7OYDxKftty5UnGCN8wwlOmvWF-Nq3l3esJLiGXMCwY6qluJL3qt8WZ7sv971sWF4E9ExBi-fBeqwZaghEHWvDQ9wrSzau2xNiUuc79GkDmEaVxN4kkzCwQEYYL8-qq-hLT-OZdu6dkgDppQSQaXFF2uapxx3-6QQ6yVNVk8HKJw54B4OO3Ax0vFsALtP_abuApnPGPshnRTceoEnKwbBcd3JwtwtBkXg3bI420xW_w_sUrx2qYMcFmMsp6rn-soW1t17hA1C6_x9taVtdje-P1EVylV8n5uFSgmObHIoTezHHho7cs-tAdzRx_p4E_BZdFlBt43j8IlRiTbUvIAjarV6O7Z_jtDTM6SGa05SNGorDhGNMKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLTGUHohvp1STc1L2IWSJYioSTg8f50BI5nw_ArOT-GNiMEbXixmQiEpWZBLfssKaE8KVqM9GgZ4Gsv_3vFxUsZnDebAo3Cugo41vnWWC98QGRenZ4Bq_m-RtjqlDAjI_8VZsbde99FlrswGHuBJ53n0BnR5Usdu0sxb42f5m2aprDLhY-YZBLaLm-u_8Z0pRr-u1gRoUDidCBIL46035wCLHqD13iHDJVEvvDqfBvDuIfyCVfp2PAWZAHNRf4Dql4eD6VArDIRXAIXXkdG8gxAkb3W3KbAOvr9DOvwfIdrIRxtZKKNyDpPtahGnq2qKjl8mSvkEdF4POC2np_ymUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Dk3f6B2UANwQRPIAYZ6auYfCL2w1PVSHMKCY6bX8yABwyvO-Ax5Xuhthm8g_5Yw5iyWZs1hK20j_H6CC3t1_HiNx_LdoHsLdNE0FmFFEI9xTkJoLdS6pbYVPrgwQ7hcdxkKIBUU5kIwBVkveK6KtSW96TmLctB0XaUHEcBblPkjkCbC0qJoUm8msMlU4uqUU3c8A9B9qFdW50ntrHtdubphpRnDD810hvBxKiqywLF41GWQiZuOKEtvX0uOe3wV30cFwEHhnsj2BVIThytMDt_DdviHDyGS4HwufsNRsx0LD4fHRVtXa_B-qKXm7CxqFog_1Kvp6DxAwvV8qDxjhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=Dk3f6B2UANwQRPIAYZ6auYfCL2w1PVSHMKCY6bX8yABwyvO-Ax5Xuhthm8g_5Yw5iyWZs1hK20j_H6CC3t1_HiNx_LdoHsLdNE0FmFFEI9xTkJoLdS6pbYVPrgwQ7hcdxkKIBUU5kIwBVkveK6KtSW96TmLctB0XaUHEcBblPkjkCbC0qJoUm8msMlU4uqUU3c8A9B9qFdW50ntrHtdubphpRnDD810hvBxKiqywLF41GWQiZuOKEtvX0uOe3wV30cFwEHhnsj2BVIThytMDt_DdviHDyGS4HwufsNRsx0LD4fHRVtXa_B-qKXm7CxqFog_1Kvp6DxAwvV8qDxjhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPF-u15bGhE2R7F7UoDP1T3ATFV6X1YhA7vY8tNcRhC3ZNUKFExAAhUB3PJa5CLE7DfDy27sEurSqYdmwev_euU96UPPY6lpyzVUdYAGh1jx4hhDw0DNoXjpewRYAtLs1XtalqRoyk5cFBqJ-eEkR2AB-VfrDGX9Zektz5PXMTVZkHqeXTYMReS-8xS0v6iwpxjkHjKH8lx_ZwhVoxfqg8zh20CLUc70JiBMbaq_gbnhLwsRXP0EqQ4zQ2H2eSzRKiEbUx_hoTs84zA09NpbwGxKfdDR-UaIRVkaVAgSR_w-kvB15PqvqZaF3paAWZC9n6jwNhvyKIfsztBLwGKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=SaAICjwZQU-f9chjEZmYd-vXdMlH6739QskqJHG62Kh3kBDTfrpK86GhiGKqg53DoHQH430Zcipi1GhddI_5jXpqDQrwVWUfy4-jnuR1L8xMhcd5aKx4POcSjifrt29ikkTDCYTCc3kRvqIojzwoTG4Fx0R7pe0ks3z8LcDd53Ey6uzm5ENCZ0hxqxQTXihfuOy9nhv3oCCAby3vyzjCgJnXTmR0wXZ9XUxHIWgBEkDoZnVV7M4nz1VLzqWs_UUZ5UZgL5iTec6agqLO4R5NwA23BX-xKGF2chPY7pHm6pNnyUyfqURwZDo6SXPrkTbGusaqdM2qDZcmoVY-6WcXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=SaAICjwZQU-f9chjEZmYd-vXdMlH6739QskqJHG62Kh3kBDTfrpK86GhiGKqg53DoHQH430Zcipi1GhddI_5jXpqDQrwVWUfy4-jnuR1L8xMhcd5aKx4POcSjifrt29ikkTDCYTCc3kRvqIojzwoTG4Fx0R7pe0ks3z8LcDd53Ey6uzm5ENCZ0hxqxQTXihfuOy9nhv3oCCAby3vyzjCgJnXTmR0wXZ9XUxHIWgBEkDoZnVV7M4nz1VLzqWs_UUZ5UZgL5iTec6agqLO4R5NwA23BX-xKGF2chPY7pHm6pNnyUyfqURwZDo6SXPrkTbGusaqdM2qDZcmoVY-6WcXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Z6CDx3yyD3YYQLgVTmUEq3r3Z_y5nQNYTK0XNNopzhWHkJWoW8CbwkjxVdrNkBY7epwTeXc_ial5g4ZOl7O1sDiN1nc-sC0mCKp-65ozyFYVABAEg_8WCmRMzOshwoythJgtpWX4G-qo43zd336ZYQELv8YF2Bdu8ArU1-pdAwI6cHGHmKuf3CPM4IfmNQWBNO4N8if1BVbdgv1OiSTjy7ki0R6BeMjdMy0W6oKaIm-NYT2TvRqiFKAD4bJiHq-FQLG0mOnM1Yxb1w1k8UqLbodY6U_XAqGQlNNkFqreE_hhj2hMJzKs730BJ7ArkRACgYQ1TXZ9yGzijWx9pG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=BYRaKL1vzjY2LhMj1oT1N7bZa8DKzpMtPFUduV1zEDCf19iooL9-JRdTT9yuJ--8A4_NzuWdZAg2oB1LcQbwNV49bAAswob50a6OU5jrfZav88L4hEso4_mqC6U3iyTt31OnlAYJlDZIJFO8kWl3QZob3aY4NWzSLQehOb0DX75A9j1lrWUl-o4AYaBZOxDvrkCEQABotCPJ-Er5T6shzZGnp4pyjeRy211GizEVeoNM-KRZAmnx2jvtIv0Owi-hvN17JH60EO7Aaj3iBqk3yIeRNuZnun3vcv5aNLMKrCdgWwte0XrxkLMw4QB6h6SlukrNMd9I2fJrsrG9K3T3IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=BYRaKL1vzjY2LhMj1oT1N7bZa8DKzpMtPFUduV1zEDCf19iooL9-JRdTT9yuJ--8A4_NzuWdZAg2oB1LcQbwNV49bAAswob50a6OU5jrfZav88L4hEso4_mqC6U3iyTt31OnlAYJlDZIJFO8kWl3QZob3aY4NWzSLQehOb0DX75A9j1lrWUl-o4AYaBZOxDvrkCEQABotCPJ-Er5T6shzZGnp4pyjeRy211GizEVeoNM-KRZAmnx2jvtIv0Owi-hvN17JH60EO7Aaj3iBqk3yIeRNuZnun3vcv5aNLMKrCdgWwte0XrxkLMw4QB6h6SlukrNMd9I2fJrsrG9K3T3IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=vg4topI3xbwnWil03jSg-mWqvjhxnlF140wGIOp2-79SbJLhVCzSQC6C5XCJJQYHLsBmbO1sQ3F8mMcNmRBbMXg2td5NBOTCvvIl3dKLo1vIjXf19yPQildOXNyDrr-O7-EKrHZrXdWSxL89bXktuZ5lMiGuiUJIXfF7tN3x-l9sYNYsfFN_ddTJC4cQ0qEU8b_Jpu2jaxcHNW2CXZF7HS2T2TwfrmDTZS6mJ5Z3BLaf8maH4PeI2sfcL5BHTuXZNMsFRwzHW2PiZz35a10QRHO2prIAALTuswHRc4RMLUzdjO9fAs0wcC6LkuWmDpH4Ai_mXOfeUaza6-YcrLIXIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=vg4topI3xbwnWil03jSg-mWqvjhxnlF140wGIOp2-79SbJLhVCzSQC6C5XCJJQYHLsBmbO1sQ3F8mMcNmRBbMXg2td5NBOTCvvIl3dKLo1vIjXf19yPQildOXNyDrr-O7-EKrHZrXdWSxL89bXktuZ5lMiGuiUJIXfF7tN3x-l9sYNYsfFN_ddTJC4cQ0qEU8b_Jpu2jaxcHNW2CXZF7HS2T2TwfrmDTZS6mJ5Z3BLaf8maH4PeI2sfcL5BHTuXZNMsFRwzHW2PiZz35a10QRHO2prIAALTuswHRc4RMLUzdjO9fAs0wcC6LkuWmDpH4Ai_mXOfeUaza6-YcrLIXIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctrqkMrSNe13veEYowale70DWFc3mNQaCJtyFYwhR73SGeDkuKDG3Rwi9opw6xi8SCePcmwvLZDj6rZS6EDrw3RynOKbctugfZgPNm3ZeOaz7Uy1Qu3bK0GBQSyW1PA6MMU2aVuZIWc5hq2YAOqs6DC1Xr65B0WwNcKEr_eI2KjaTH1Ct5i470U11FdX_-FPZ2K1-1AEuu8ihs9DfVGI7Y91hYkeQmsAQkEHPinboSmIt44yUVIROVtME14jk3NkO9lCKaxWZNU5daYRhlHmHlkv3Aq6acRBpMqqWKMmvEcX-klYZX9Vlt208itGEm_0ndohlysNBORYDBUTOgPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=IS4Mxofu4vTd4yoj2O77tr_-5NWXtJe6uaDnVhQi9jq38o1C2iHoxWHvNE8KIqYKxsve2zltWA4l167B-OxqmM0Got6NAtSyTAXEhLel0nWNTDILhhRYSxIIt1mnpGzVfBdHrSle1D3zBPRWg-33mdulI03ErpYfvdjX9gAOflsWX2yK4EqV88JKs5Vhat8bkNULjC74hZuq5d8YgUV1_G7AtCPOzXTr8A2s14LimNWp_ayou05Ujcf8vjrt22kCcIt1yY4VhN7ejOaiLiTr2Ur9bfnE2JLxHbw72iCaFwfKFW2yrAmR7GgvHRaiwB-sMiamsVb0qMd0IllUNM58Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=IS4Mxofu4vTd4yoj2O77tr_-5NWXtJe6uaDnVhQi9jq38o1C2iHoxWHvNE8KIqYKxsve2zltWA4l167B-OxqmM0Got6NAtSyTAXEhLel0nWNTDILhhRYSxIIt1mnpGzVfBdHrSle1D3zBPRWg-33mdulI03ErpYfvdjX9gAOflsWX2yK4EqV88JKs5Vhat8bkNULjC74hZuq5d8YgUV1_G7AtCPOzXTr8A2s14LimNWp_ayou05Ujcf8vjrt22kCcIt1yY4VhN7ejOaiLiTr2Ur9bfnE2JLxHbw72iCaFwfKFW2yrAmR7GgvHRaiwB-sMiamsVb0qMd0IllUNM58Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1r7F1NlZE7WJh8k7_5zqGlg3Hf_G9WqSyRhK5yjHlpgpXHxoskBtXYwtY0cZ-X12kjbnjxyjXTVnoNXEHVLphi57LMyJfnMvbIGJhK_MhiH5j5ULzkb8krlaBKhD4Kxlm_tKi9otUUFPSfGj85TXVr9pXwP3VOzeliLPd-oB6xOc9UyC07ci9aM4yhbYqyVx6wKNr_CA02J5oPPs4WXwgLUSXzeFv0uO1tBLsVYJKaQ7vy8P4MuPDLB4Pvu_yY192ibcKTF1VI2PDYqOiPGIUxJ_6VjVmE3jfCvii3zZxfmz67v1B0dEmPcS3sZUY1n3ZvirfXEAF83UYPo5V8YgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=JmxBrEBGIW3CCovfZalsZKggosLroZHE879-KE_C4qujQzWZEhSBW0L4w6cr000TGKtmZT7u_lwnV-wn5mRlmb0aQUXVXEjecxcGHBHSFALJ4HxgBuuQg8Q7jTFGY0wZqcOxEGDK-dHQTwsa31WeNsW8wf6B5KamvXx1KetWsGkrRwjDUkRdBdnZb-cD7dJo3jlJmvPto65vPzMXKgJvyPQ_F3magGFvWLv_oVqGc6zGPZfxk7vBBfz_XGhZlkf4FSGkVJunzxzXcE1gTjz-g-xMImCW-T1yqSCUdtMt4Eh5d8Su8oeIYc8ZITTM5J0Kr8lfavYUihQ-XHjKlm9TKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=JmxBrEBGIW3CCovfZalsZKggosLroZHE879-KE_C4qujQzWZEhSBW0L4w6cr000TGKtmZT7u_lwnV-wn5mRlmb0aQUXVXEjecxcGHBHSFALJ4HxgBuuQg8Q7jTFGY0wZqcOxEGDK-dHQTwsa31WeNsW8wf6B5KamvXx1KetWsGkrRwjDUkRdBdnZb-cD7dJo3jlJmvPto65vPzMXKgJvyPQ_F3magGFvWLv_oVqGc6zGPZfxk7vBBfz_XGhZlkf4FSGkVJunzxzXcE1gTjz-g-xMImCW-T1yqSCUdtMt4Eh5d8Su8oeIYc8ZITTM5J0Kr8lfavYUihQ-XHjKlm9TKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=c8Sb-179P28uoZKxOJNt9GSMVDPXVMX-qvwaJdFn2UZmLzxK3AMXLA1S0r1XRmnipU38GKCeHJENiQkGq3EMMdJgOcSNtzI5wf1hQElXPj9fvTC99ptPGQECLjcF250fTuTwPTJmNxhciwHhwxbQ7qtPUiODSj8oi565529xjtVQsFLSd4tsQ0ZbHKlPHIwlWaSIvC-9MCUAsHjNvw1GX8L5c6fbX2SwMMiJxD6jJltWrFOCwwmN0PG5gL5UKt2jtqmDBow20ICxs-H3inCW4_YZyERB1IGa1uyBB3KddESQqNdSl9_znMLBVquUvE_aXhf1lGKSIvLiTKdmOflPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=c8Sb-179P28uoZKxOJNt9GSMVDPXVMX-qvwaJdFn2UZmLzxK3AMXLA1S0r1XRmnipU38GKCeHJENiQkGq3EMMdJgOcSNtzI5wf1hQElXPj9fvTC99ptPGQECLjcF250fTuTwPTJmNxhciwHhwxbQ7qtPUiODSj8oi565529xjtVQsFLSd4tsQ0ZbHKlPHIwlWaSIvC-9MCUAsHjNvw1GX8L5c6fbX2SwMMiJxD6jJltWrFOCwwmN0PG5gL5UKt2jtqmDBow20ICxs-H3inCW4_YZyERB1IGa1uyBB3KddESQqNdSl9_znMLBVquUvE_aXhf1lGKSIvLiTKdmOflPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=F0sufz7E5wMHX2xXaHzWKwvD-MsnvBv7NNExiFYgeYQKfsuOlSdxuvRSvCyFskUdJqhAZwT57impPPXNO1J8iTQoc5X_qr4z4WsXbh0IK6vbuBf9FALKx4bRnF7Z_UNk8u0g0O_Z3ZbSnR6Ts4VLRTlg4iPIy4f2TlFQn1Bq_HwKt-EEsNOMLsyYuLnOg8-9qQn8Bc2X4a0xuwcg6ctTU5NHW2kN6x6fyNbZuULsx3evZllrwrMEFOx8LHL9b7ycf7od-niMWZ8O4k6L43Z6vXOpPcZa3hbBokIEqfMBj1absPnYN0-k6Kjzjv7xfZCVk-Dt-w-jBjllGJdOY1x1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=F0sufz7E5wMHX2xXaHzWKwvD-MsnvBv7NNExiFYgeYQKfsuOlSdxuvRSvCyFskUdJqhAZwT57impPPXNO1J8iTQoc5X_qr4z4WsXbh0IK6vbuBf9FALKx4bRnF7Z_UNk8u0g0O_Z3ZbSnR6Ts4VLRTlg4iPIy4f2TlFQn1Bq_HwKt-EEsNOMLsyYuLnOg8-9qQn8Bc2X4a0xuwcg6ctTU5NHW2kN6x6fyNbZuULsx3evZllrwrMEFOx8LHL9b7ycf7od-niMWZ8O4k6L43Z6vXOpPcZa3hbBokIEqfMBj1absPnYN0-k6Kjzjv7xfZCVk-Dt-w-jBjllGJdOY1x1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=JTCHJ-DdYlQMzuOqEa5TtPLb2tM46pDCXPxXvlO_7OG1y30WH_dl_7FOtp64CjKUthobbLNPF1rguILe_IncN8fvN__NJGmVgwkew0Ltza3EOQSvsYcxI9TLBnLkVo1ppTZiHkFaRT9djDFd1AbUcRX4ZvRCiX-YJJRFKea1oSFBCIiMJuHQ1ElqBAh4lqf-bl1yX_OcIvd7gWgrpw8zr3zLFqPT2bDS4VDeS2BOUtDj_L3WxE7acczqqK5O0N32mXPCSDNgDO1pxzZzadSXllEK2aJwe0w3LTKBgeejEfOFkLy7ZPtXEh7or1MJZIUQ2KFpxrcn-rspfWGMoo85ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=JTCHJ-DdYlQMzuOqEa5TtPLb2tM46pDCXPxXvlO_7OG1y30WH_dl_7FOtp64CjKUthobbLNPF1rguILe_IncN8fvN__NJGmVgwkew0Ltza3EOQSvsYcxI9TLBnLkVo1ppTZiHkFaRT9djDFd1AbUcRX4ZvRCiX-YJJRFKea1oSFBCIiMJuHQ1ElqBAh4lqf-bl1yX_OcIvd7gWgrpw8zr3zLFqPT2bDS4VDeS2BOUtDj_L3WxE7acczqqK5O0N32mXPCSDNgDO1pxzZzadSXllEK2aJwe0w3LTKBgeejEfOFkLy7ZPtXEh7or1MJZIUQ2KFpxrcn-rspfWGMoo85ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjnQDseK4_dL-0L9OEDdxlrrCPZRu1ZrmALvYqe5QRjw2Or9d3XaJhKm8vRUPgENTNs8BkpViC76mp4V3v6BLwOvngnpL-GA3RgDpIg7BtI1Xy9koeZhMxyHmzNtjydRKlr4JSq6d7B3K1uiyqZSaJzuRK9RK2fAKt7gDjNkzHP4fi5xens0rBThUBIm-qN_2FLhCfxTK8-MiAcT0JXekkT90HA5EEgAGr4e_iQYsAbdNg1sV9bSKfV6bjBYHD5bJBjoyq4d_rzF98SXNLbw1S9WfSKuBn6eLVP3a8mWqvTUll5perMOwonGU0yesJQ90H5uNymWdTDvAOJjfRZK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agu1ZEAs6El8z4Yh8EW6uSzfyHgjFY4x6AJrrGzzvmSq0oJS3d16sJEBEqjmOAEp6Z0th3pVZpV66_O-xp90nZ6XEi-VGXbuVpsHaoXIokklW3i3MoFXe_oUxk2Ticp9otwXnHUeR7UDdynJtg_gyvWE8u9cSOg8Q9r7FnprDu6p2bAvWOYPdgaK4QegCbbpUACxZ2K-Ztuo0A66AXN62JYr3Il7jg00wMK5Vq0a_naxwAtaVSRrDac5tm9yiaP5r7xsxi9pNSkhgwNrCLrvj2YseKeermeMvc7_7K3s7WoPRVWCC3IfVpTD8e4PHK6E4Q0u8b_S8l2MX3aAcgOYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPOOm_1ZzpGgAIuenAmQ8-WBCAkBBrlINClhSULfSBfbPx-s_6ewaRpk4tHULcwiLVkiuDKxNqgMDUtNCVBjXz_pJLQnxya4qp5256Zr9SJMVgrrL5lqGDE7ygXfIggND-P1SU1ZxVucFV8zGMt2OE2wAD9ehPDGuValMYu1QkZMe0V2nrH56eV3DB6Wng0DAHvwRtRXWmfOxfEAQsIAdJLrGMWfLObceWFfn4QJ314JAgnjLch0iG-Hoi2cyMQJ8PRDPWUVJYOCQiLZ1tpPFGmrA4YLDJ_GCdp7ubFluxi0sb6YfSFMbZZr4xD5fURzsKhti9_D0pSPTlRR7SiPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZCwX8kS9Mq7ZT_mD-w1W9uIZyIIboy-rwpS53_O7zoAptDbM1tevYJ82RWMVkJUToj79hiPcdfWQ4DfoFhub1hn085kNBWa4VhY-tsCvzidUY8y4qO1QfLiWoxOXD0asK8QGqNalsP0OdRtlt6PgNn0T-zRrm9K8xiTmWnxKPiMQRKEhpJMapPD_7JhgU3qUnpDVfVBya8Ouk54HsMz3Zj7U8BIXCv2rn3yOXsCMqYhbWUD4kuG_fnq75jED5vmfMMpX64kjGb1GQZVvLjjp2ISOJsrp0Qwfpg2kp-hPlJuVeIaciAuGKVZKvwoMYcdFBSszruB2Cgqi8e49nQAaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haQSW1KA1BVz-ONlShl5J_5xNNFG-7RSCQUYGRQ03-V49bTD2-ozCnR53T9UmiRQDxUvVnAXrKyA9xrtrt1RkpxTEdAwKH1diFWZR-CrFsmGkRbft-mauLouspQx9HYHQkPZ7P-hf39D4TmFJVOtu3N9x8q666nvZ5HRFFXN3k4VM4XjCzEHr9SC7WRw5ndpMdPzH7sbsZDmLowg_LiBuqi03z34JzxY2Xq1NAMdyHB-l_qtq1KOMr2_9fF5n1HKBk9G1Q7b8sLgnMvI7q18tSNyKhDdrEFbC2X1FluixLH5kHI3yPglN1bujeOCQ765tp02ah2qRoLpAmOpxzQNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=nYx5OEeTDEKvSNRkk6nPUt5icZnxk2R90Mszl9jafxR1D9z5aanb9QT0cyAutlPb4bqHLQVCdr-8xmv5kYnAyHDTKBeNOZZC1XEZ3w89_GQcSL4eQuZwzju_vpKucxqbtVhY3wpRYF9jBeqbxXnApRJ080UEMFDTyYXt1eZDfzR8RrvwAw0N1VKluBBPB2jXT7GJqI49dPfzbkAnIWKKbZUE7N7FMNF-1FgzrH9DOlZxx6PUmaj8pNpRFdqcKdnW-PXh8Jn4W5dO7F3lLGT9BDgDV3VRiSxQKRXOvz0KE6UHR02RpwnZB4Vs2j8Zatkp15WT21oasUoRQLz-RfSryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=nYx5OEeTDEKvSNRkk6nPUt5icZnxk2R90Mszl9jafxR1D9z5aanb9QT0cyAutlPb4bqHLQVCdr-8xmv5kYnAyHDTKBeNOZZC1XEZ3w89_GQcSL4eQuZwzju_vpKucxqbtVhY3wpRYF9jBeqbxXnApRJ080UEMFDTyYXt1eZDfzR8RrvwAw0N1VKluBBPB2jXT7GJqI49dPfzbkAnIWKKbZUE7N7FMNF-1FgzrH9DOlZxx6PUmaj8pNpRFdqcKdnW-PXh8Jn4W5dO7F3lLGT9BDgDV3VRiSxQKRXOvz0KE6UHR02RpwnZB4Vs2j8Zatkp15WT21oasUoRQLz-RfSryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyvDYgu3Wn7Z-DEL5ttW4cU7ntgdndrn-wJXqQslcSrdygG3y26GoYDpJp4gVjgkQNb9KvPudo4oMAgCnJSzyobJPYNeQjT0KtrCMlJhtoD3MNxykfJ5gGCmFwUNsAusfzrRVQT6u-tBa6UeV8I2bxxIoXWXEFUeVVx-vOQzFcCxmyWNETeq4RIpk0-ULVphdQT6vydg4Mhv6oUODVCzgv7vvBnTHVY3Mq8r3P-x6l477zx3pUlte6a7KkCUYGaqHCSxTBFHYj29bssWCk3fa7NRH1xC-oawj2DNuVx6L678xOe9bVqdum9oGR7SwqtlYYPrnldLg9O2pLb_oTeYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X77W5O2SEr0Swia_TngQRlR12yvsLtJ94oNdPugtgDV9FZAT8GT7BnnGBN1tf88YUAwUBCFI-Tbwemhvz_QO4mzb8JGkJOByqQs7hsSgOOveH9LJoXlSBP0vbS3uY9lnexoEbQMfhHYhmGIUKtTPlpS9I2G2sldBT0BBHtlpjrk2UaN0bdEL1IFw5Ug-gQ9sR4AA6oLUN-uimtZhmZ2XzjIdOM3q8B3aWx8EeAJSfk6UsNr948P6Xvge1aqU2HgAo5MV4OmGfCHjFs9EkdU7bMuEcJc-CH08gxrX0_425-k6azmEAMj-21oK7MlYb-de-ymfkEwKojFWtqaopHDr7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0DEgRFhm5UHf3XP8A-C2yUIijn3HvB4zlUC6mtwxAnlF5p4JSVcPbWjchQeyjeZwkThnihPm2U57CWV1WKhbAJPC5vBm2BaRkx8gU4EeAFl7cS2Eddlom10ugSRH-oqrCj573-LxHz9O-m9HS2_fjkUu39jgUKlMszCmENdC4GtePb4CeqLhQqN8_Asv7QhuRsm-SMsf_cASVOlmWC7bXzKj7trC5jFGA78sqhtdWLu4Un5z6Cjl4PfcJF9xaEQeajF-NHKdUqSlyy57zp6KdIdKHvikrAyxLZfPtPSmllmT-1vBFaSoPIzFXYlFONASHcZS9TO6VUc2_G94HaX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDHifrdzwJOXbdSsLHhO0tbmBcOAal38OgXVfUn9Ipx5oTgxW0wK1jQOGqeF5TJKp72HoWFE78JNfRqQ9oqBPxTl1W3X3BE6I1LH31IY8P3WDIg2PF_S63i94qLOiAmvLk-SDIJ5CRJfNrZmr4-EPwT0TXQD6_5HqnQahjrBJ2GUqvujSHXDlOa0MrF803uX_de2ppehfgI1g5Gh3GEPpA0FfbojlilLP6eZhFSbEei1xsDJSx9WdSI0HajlCrM5RVQN_PIXrw5wDibBLIMq_5yhLL75kpHf4Npbi_hUG2AoIwqGygPIhYsuTI2aVyQ8ojRngc9SvDa0WHEnWL-sHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBb3_Fc_ecbrR_94o56q-cns51dn8jDNkG7TaERA3pi2_rZD4ARZ597HfNhTRLtW0G1xAf1ApUz-f9X-ef51MD_WwclbRbWQUIMV9pbAphnIZZXNYV4Vtn9Eagmo3VgD8DNEqcJdA_DX4X47Lvdw5mJy1yQ87EYxIEdw8MEu3QQFeUnKItiI_qcvbvdWvYD55MV2O2_3jWDMo3fHQQdXOuFE0FjmQ9kDq5z666roBAWxwZR3A3ZvmKoqNVNf0DEapI3AXGgN4uTPYUxOJbhGnGQ31XaSYmE0UeJtRBN4AT55RCu3U4zfJiukcQZzPV_1F-PMiZTA6QiYWU1sr-qMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmYnZ1v3aeYdeGSw6DPUJvnFa1CUZ_Tor4kcxEH8Xk59T95kDlV3o38iYsPqfK9MBvd_6V1BaG7qU8di4wpHkqhw7VJKhPZCpaZ8OsBOyAGeT2XOnR7LmXJ8Ep6VhxyLLPE9kjMjRxmhM_DmS8IhVD-8jxWFEBc7DCo70ut878jhZmDnNuL241ewkCM0jP65qByZogUMmvtyjZ3YvA7_T0U_8nKkLH5JOGF00WZ17tKyGcFAOtG23tbptBDtChopfGuNYSEiouveH6JiPExVfX49VWoGllX_ihUGNquG_DYxOdc2hEYnchC1ZpKKvfu5QreUucgEeY5_qh_FmnqiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=r50aElNBYZt8-wnAdujXTmG5O5arHOubnAfeqqgGOuO3YhIPduzt3EP4clAzG235wbrmDMqmwnlOFOoMiRSQU304SvH1ikeRKdsON11nPjaeKVLKTn8JVbwkETar5jVi4MJi3CaZ-RQD79g6aB7KkBra83e9wkQW7fh6S000DxPWvW5Fv7mx_P2k2uVzvvYCGiaL0Qf-TGPft_F5-f6_JkoEoFIuAqwnfYpZEs-OEbCKdxGKiLA7_7X4v4d6GoopoY5UcCRi2Nw0CeT5GhgxjtTpn_H6Rm5VqJLy__pkf4Kzvk-Kh4jUgSipOTUD7TwNUwlLpfl0JS5vZaONnf2_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=r50aElNBYZt8-wnAdujXTmG5O5arHOubnAfeqqgGOuO3YhIPduzt3EP4clAzG235wbrmDMqmwnlOFOoMiRSQU304SvH1ikeRKdsON11nPjaeKVLKTn8JVbwkETar5jVi4MJi3CaZ-RQD79g6aB7KkBra83e9wkQW7fh6S000DxPWvW5Fv7mx_P2k2uVzvvYCGiaL0Qf-TGPft_F5-f6_JkoEoFIuAqwnfYpZEs-OEbCKdxGKiLA7_7X4v4d6GoopoY5UcCRi2Nw0CeT5GhgxjtTpn_H6Rm5VqJLy__pkf4Kzvk-Kh4jUgSipOTUD7TwNUwlLpfl0JS5vZaONnf2_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=GuEIkmjNE-lZ2FK4sCqguAyoqwX-3RyHpfi09IejkLFEm39m7Sda51Hxowx3rFfDkmqMBBwmb27mvDcGQYufJz0pdp-PORFbfBNX2qIm37ctcXE_xppDX7w4cCRPI56annuBeUhA_zJuyMMGeRrPLbAV1Wumn9JND4XiqMEpucpqH6VjIkQ4nXItLzHdcJOIlWwaFLsQLs2hs6w65wabshwfgBVcLBVC04rda4ePh2Eije75I-WCuAfuxNqeEvBxyd62qt4pLjayiNne41IVqqK1m5ObDO3sjKUzqLlkBpWFAi2AGEX2MUZdSY6xyg11IYkFeKEn2Ijt_FMxXnTJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=GuEIkmjNE-lZ2FK4sCqguAyoqwX-3RyHpfi09IejkLFEm39m7Sda51Hxowx3rFfDkmqMBBwmb27mvDcGQYufJz0pdp-PORFbfBNX2qIm37ctcXE_xppDX7w4cCRPI56annuBeUhA_zJuyMMGeRrPLbAV1Wumn9JND4XiqMEpucpqH6VjIkQ4nXItLzHdcJOIlWwaFLsQLs2hs6w65wabshwfgBVcLBVC04rda4ePh2Eije75I-WCuAfuxNqeEvBxyd62qt4pLjayiNne41IVqqK1m5ObDO3sjKUzqLlkBpWFAi2AGEX2MUZdSY6xyg11IYkFeKEn2Ijt_FMxXnTJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=aO5_gyDZg0YvvYgngg0PRhj-VE9WT1HcfUZBJcZMY9oxaPVQjUJ2vpgKyZLgfFDja4vzrxChov9q0hge6I3BZS8j7KAAMRjy62jLkQAumYR4Mr3WIAEExH--eC8HRMB__uC51hsEoZjm-9xHjKAYmY3r0ocp64BZGUkXbfn_0gR2koal5He-HNl6OoEDlQJe90niL7iXfa-BC52liO4J4Dfm9s9gqavnQtW1fV0p2tsbEnJ60CwvIbq9O3NOEi8WWPZEx3adU29qPTRWYcYQc0O6YnUxFQdVt29QbUlKsjF0I7bPSHhRHsbYiD6vPFIwQhUmXUVbJ1WyyX6OD2m-rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=aO5_gyDZg0YvvYgngg0PRhj-VE9WT1HcfUZBJcZMY9oxaPVQjUJ2vpgKyZLgfFDja4vzrxChov9q0hge6I3BZS8j7KAAMRjy62jLkQAumYR4Mr3WIAEExH--eC8HRMB__uC51hsEoZjm-9xHjKAYmY3r0ocp64BZGUkXbfn_0gR2koal5He-HNl6OoEDlQJe90niL7iXfa-BC52liO4J4Dfm9s9gqavnQtW1fV0p2tsbEnJ60CwvIbq9O3NOEi8WWPZEx3adU29qPTRWYcYQc0O6YnUxFQdVt29QbUlKsjF0I7bPSHhRHsbYiD6vPFIwQhUmXUVbJ1WyyX6OD2m-rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgZHFw62b0cNETKz3SrUS0L8a-EDRJ7frmkiAPMcjZxKGFnPvx9EO6eqch6sw7ApC0r7gn_qd5ZWbBZdU9kJVE70h7q2gEDtZfb0kbt-pLpHvVk9yChuMVbZCE0moP24b3R5FWnNgL6Sdsn6iq_RXpXieQ4-YFZXVbpEaM060mAOM7SOEHZ16BcoS2qXFV_nd7cwCCNXsQJF0XJXLGLubBUN6d5Rh7n0ecuUKUB-VgdFc-CdN-Cex3bAiEOrW-1dMwSt3aXGRMjqg8Gn_PEZhECu_lZxNRuMx-HkgPARQYIOkVqh2NlteR54mDG4rZ_k8RmTzm-hgc5dhI7EEAtMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=qTqyIYhkhC0S0dP_2knO8qz12y2591A-uYvskSAaqE4iji42xw-HMTlLYl7kiXPUXZ-PJDgUgGsvHlYZsG9n9Z3IUUEJg_o5h3OFhtpqzQxV0daIDqo2H9rd7sJtuqd7YorPwoF0SRGf07E5qJq85WJm_sgFHI54Dqgz3Gy8hUaEDMR7s-sbVQW9zH7_76szkwIHuEo9wEK7E83KiA-ZcihoFWMJD5AEdT99qIigPxV9nfgszc9BuxjasdOasru6xnD9YCQGFx4BhGATekfS37rjDomFB0cy3w1wQrsU8gci79eAPHTxJF8XChW7W84MB914pWNskT5izA3swdU0Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=qTqyIYhkhC0S0dP_2knO8qz12y2591A-uYvskSAaqE4iji42xw-HMTlLYl7kiXPUXZ-PJDgUgGsvHlYZsG9n9Z3IUUEJg_o5h3OFhtpqzQxV0daIDqo2H9rd7sJtuqd7YorPwoF0SRGf07E5qJq85WJm_sgFHI54Dqgz3Gy8hUaEDMR7s-sbVQW9zH7_76szkwIHuEo9wEK7E83KiA-ZcihoFWMJD5AEdT99qIigPxV9nfgszc9BuxjasdOasru6xnD9YCQGFx4BhGATekfS37rjDomFB0cy3w1wQrsU8gci79eAPHTxJF8XChW7W84MB914pWNskT5izA3swdU0Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=n9xFE0cQqFGhgM_Bq7uSXqYwk9kpTAtbsgQt-vVDr6UjhVh1efaBaIbUAYxvf-LGeV4-jD7aNwpZefarJmihd8MTpMr6W103ir9DiDBbGJ_XdIrc8AB_SXEdc6Iy0ILw05uDlV_r_GlkrZ8UwaWB2TlbfYtkxK0TEKZUsyMa3wPktpo-UcenPNoXXshueSXhBgZ0JRSiBwoaVV-XRcJtFP2y2S4nflOD2cd73VQpW4AkEa8rDIKZ1aBcwGvg2CdTLZ5bttIgTbZzwZdtlwZfnY7e5woBhYCZI0lpcpPthS7H_ayZBQFsmgXTdTFzkxoPmwbdRg7T2LY07ZbNtDMiIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=n9xFE0cQqFGhgM_Bq7uSXqYwk9kpTAtbsgQt-vVDr6UjhVh1efaBaIbUAYxvf-LGeV4-jD7aNwpZefarJmihd8MTpMr6W103ir9DiDBbGJ_XdIrc8AB_SXEdc6Iy0ILw05uDlV_r_GlkrZ8UwaWB2TlbfYtkxK0TEKZUsyMa3wPktpo-UcenPNoXXshueSXhBgZ0JRSiBwoaVV-XRcJtFP2y2S4nflOD2cd73VQpW4AkEa8rDIKZ1aBcwGvg2CdTLZ5bttIgTbZzwZdtlwZfnY7e5woBhYCZI0lpcpPthS7H_ayZBQFsmgXTdTFzkxoPmwbdRg7T2LY07ZbNtDMiIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=Qh6VUdAnjOyUEPwIc7ac6lBymVXcLJLlivMchiY6izFP3wXZqNny1tkqAaE7Mx7HmQcwrZEAKTIgUJLcm-A6rl1DeHfog3vAL16wgsSnT5sORT05ZBTXJBrom5QH3nGK4pcxqdJ-9kqgSkjtDykKN2rwC-AN_RjP2NCyhVpjZud8yPkafm0TW0U43q4CHgDv4S8-RC3BBecoSf5t1kT7BALuK9brAAgTjLOkQQ1FPvK-DaFwvPRr025lWXlBW-sV-JVvKTRl13aYlNQIQYKPgRLbftJX5OiTnHR7PqiQo2WZWSaholNztEtBwf2QjYA7L3WyUgcgFd3t7mGBz5MJBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=Qh6VUdAnjOyUEPwIc7ac6lBymVXcLJLlivMchiY6izFP3wXZqNny1tkqAaE7Mx7HmQcwrZEAKTIgUJLcm-A6rl1DeHfog3vAL16wgsSnT5sORT05ZBTXJBrom5QH3nGK4pcxqdJ-9kqgSkjtDykKN2rwC-AN_RjP2NCyhVpjZud8yPkafm0TW0U43q4CHgDv4S8-RC3BBecoSf5t1kT7BALuK9brAAgTjLOkQQ1FPvK-DaFwvPRr025lWXlBW-sV-JVvKTRl13aYlNQIQYKPgRLbftJX5OiTnHR7PqiQo2WZWSaholNztEtBwf2QjYA7L3WyUgcgFd3t7mGBz5MJBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=hvJvu-4XyHaxFVTzouswb2OHtXyMBARPU9aTTlT6YyG6iPk4EpdPv5Dtf_GZeJ-Q7RtTgXdfo6uuxi1jBVVHqBiugMZE6IbGYd4RheeN3WFlSf-x7rFFshfB5W1r4kAjznvN9IDTbPnLnufW_6b9WfYVztYX3p_rbZIsvj_u0B1SAkj_1bRU2rXBo2TjTAtoDzTGtEQEGYBL2uE79ryrJrCQB6Q4w-mR821jd_YeqqxrAR_b-lDWahxz9VGS-JVVgvStATE5NN7JktpdNIw-vWek02U2-qJRyRYftbiCNwDWE0EtzHXGZAyVWMdxyPB0HGhv3ApSFSeAITjdzDGB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=hvJvu-4XyHaxFVTzouswb2OHtXyMBARPU9aTTlT6YyG6iPk4EpdPv5Dtf_GZeJ-Q7RtTgXdfo6uuxi1jBVVHqBiugMZE6IbGYd4RheeN3WFlSf-x7rFFshfB5W1r4kAjznvN9IDTbPnLnufW_6b9WfYVztYX3p_rbZIsvj_u0B1SAkj_1bRU2rXBo2TjTAtoDzTGtEQEGYBL2uE79ryrJrCQB6Q4w-mR821jd_YeqqxrAR_b-lDWahxz9VGS-JVVgvStATE5NN7JktpdNIw-vWek02U2-qJRyRYftbiCNwDWE0EtzHXGZAyVWMdxyPB0HGhv3ApSFSeAITjdzDGB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-sv7d0ypLxIPBOYR_A94pSYBYmJEhJTGVg_rKsKu4SpQo0lEzoYke0iVrEDbjaOaRUC1apB02ovp7WK19HJ-3ZRUO7MTjY8qyKpFbJLqIPaWcgXrGW3lClpisvGTr9KUBbJ6z6AoG11JCi0pOB057hpMFTpVApQpO0LtLg4pHKTZhVYAZiOyKNLdT79DWddRB6dc2tlJMPGpXaDPDnv71Vd-Ebw_vgKqksih5B1W_pOcVmz7MX4qx5wKRGzEH5_PZGjfxJ87C_JRwXxWmk-D4RuXvocFpOUUeQjCBwjNl9G5jtWarDJZoWpjsn0UIryASnj-WKzDMR6mBRPcDTstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFew7Awj_bEHDhrAV98DKRGlUa4DezA9zmThMGhUge739pbh4NLDXs0bRt0sc6p1IL7MGyzCpwu2y21YkrNk7kuTy0Ou3XJsG245W5Pcg6LWgPnTMQ5CNT_xTHmQlTLlnsHkDUD521ouCxBE7gd73yKzwra6UpXjm49Sd_bg_W8MRJLTeEjO6qCHmCCI9aQ0E5KaxP9yjzcCQYpjA9NpfB3kpDBLBBmFK1g_TMSQJCLVEHKP6F5Mdd9sfFaJcEo6bMqB3Ko7oBrshlAS7Re6ei9U_TdRqS24Wl1UeysMzdU6z57qe8EqzKp9tXHub3xiBpOTrcwiemy7Km_bRot_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw9pOuMwrT8H3fSfQ_JZuG-7bN8_xBpIA8kjXRbJlBhXIa_9QzNUJHzcVpZI2eQrLeMuZPcdWmegWTje99OV4sbWYlbX0VKjxwe5Fi3HtL86zAZan4_s5pTNjXF46Ph7M4TQSzwRM70RBs3lto4oTVGAFlc6SAfevaBnNexY3ub2CJz5KWAb-TFRlDgi46yGGKyLLWujbD9a9IDrmj5n8dE7D3wvzRnqp_nG5uML2Dcy9rkQ7wJiLhPcRlA3tkNcVcDYtt1XlvipwHoEUIUUhlvNbtq_pj9FnK-WFo22PdtNFZBWqfZ9Ub4e_NGRT4crDopeggCNPa71kkodEf6GVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vis7jv2gRzaRZsIqhx8rJXLho7CJSCCMvnYOTw9hYG86O0lfd2dSsJm4WNpL5kVTcUnRGOukJMhbhYQNEcArhHB0DpPhZ0qSNDaFulObqzgyBnITT_eMsHxbuAMJh4sToe7wDeUwdtwuhWxmApPD1iQwOGXWcQ1J6BctNWEYr1a5mcoDUq0ypWr5fE2_SthVtJyI29QAeGxZ1Bt__Vos1YHbYyMee7pghBcIUsy7nQ31GuZwwbdNMW9j_blIz4HfB5oDhd2WXrsMB9c49axf1cpM-Q33YADmDymzznUNYcGvaUd0nhw6qKdQZMcWtBY-akHivWwgWprxaPCbuPMRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L58WooTmCXZn-shYhN4i0R3c4aEOMRA4dgtcZozZNn5vmlpQWYEVMVdVjiIc6ixcR9uvYvyFUZGZSHb3aZ26S8otHPuLKtck_NtFh9P5TP5P2tlHEldqPmiEsdS4gaizxjfrsQbPdxyZRDRj5oewK74H2iP4ZOsmQd_lbxr5m0IWw8ePL9KsVOByLqIN1n86e0ulD4dKi7dFf3yFtXVZWB8Iwdc1vStXI-jYikjrsndTczonvWj7XVaf7xPuAsBjE5IFR8hK20Fri6UspENcLDYmI5vkLPgyDZwL2xP1omXNFDBgIGLbn_5I1BtQ9vXu_rXwtD-vy0bAg1ZXGBhSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3nSGbDiWf0txTvCxncM55DftNiAxyL5tJTLyuQy0_QOTeVzWLm3dXA3CmY_Qquqen5Ymy4RyglwV_K6dvGG7smIi6eALZ6VNT3E1USrNnhszec2osAzwLDAms5_uMbClksm0PGQd7bF2tBUPByA1SCNW9nknYbQ8l1wSL45u9gUHwVwliZJlN-rRKcMFwAhuxkTgo_fJ9IEjmB9zENzguch-YkARPUYQg8N4JpjiAS-swaMEGZ0mMwizDSxea20-aSIvP1HbWAnmGZWiE6AUTKNRzsHvhzKxik6473UOqlZtIuWo4UFWCfLqbTHjxK4qMmQK6HVvqs1tynwDuXOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0KPenK4FojUMqJY3niqCV9bhvEV_06_jWsqKrRbuZqNIBziGmXfiOL2jBAts4XgoOxOyo9gJVPAwUT8vV0euR2CjnbYPLzurZRPi8YuO1Kj0FZNdTwY_9FWtLENaB9fkoF4asoK9fI4_WlJEmnXKiabbRmQIIuNqf09fBQtsij8K9m5cwUCv29Scc-cXLmgEtjHeXI14TBjirGdgRYAwUxjFqzMDaQ5pB29U4GBUYme5BJIeJ6K_aKIfjz62s6QWoIo8C80iUI-0pbMo6MKpfJKdN-bQ5mEAhNcjhc04UwVmZ5oD3WFcDDFCdrFirXJTp8CUHjNSFmbARcq4DGhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
