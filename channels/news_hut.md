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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LladEuRVWOXufEgB68FdTi2sMUZSuuwIsFBDeSv5cYSoLswBgd6yTuSZcKUzwVfq4vI-r_ABEpTb3IQVw4PCzLRsQ28lR0xeDsDbr6vvdk-IMg0MD9U0ub7Zp3kc69YANnfkZZpNO7TIlyBLzVmqUdA9NmbBmXPOvEAVfPffktWY5bkzaVtSWTVMrwzdf5ifbrP2_voE69d4d7aWNS4zB1s50CnmoXnFDUHua0WLxnlUNdPdynMiOqtXF5UAUznasT4u4wz64ybhQJ2af-eJ94SvmyIWiYnXoIboI2oCKYrVDOJOjWRyJMjjBm0UK1MwN4MGwTxE2EDmPdPkOq2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQVUZ9qaa8VoL555zTz7uiTTTJ93fYRbriWVe5x-tUay-ybdVp9SCssgmKzdRuqIJs7q8RT7Ct3ndJTSKcDcDp2OriFpewDcoeRWYCPV6rBfOmI-oiykPvO9EPxelkJbxL3voxou9fN1W29kq15jei4EWemhEbQ_u0o14ZGGQPJIiOvchXMZYd0qjtNVnhaOLVy4jPq9RtbDgW1TiyaozJHeoTMXYTmvcQL-ZOjEqqE69ZMRjCVA-U-ElBL70tfMRfIKmD4pUpgYp2tAKnrfgru_N8Emf7grRac5mcZHWkCpvBVaZ0lM4TatjnRo9KWG9ZdnqyJPmGxfIT38MQMjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVgeQmSJWoXiQQ4u55m8BLoCSUKZiFhV6si8msKnpA22zPz9Ruix9Dv5dNS_MRgzRQEIEiv7dCI4TZ1naSc2qlWhIf1i217mw_b2fJx2oixn0uHKoC98cIlAkJFCwlDlhjNSn2dzwH6AyEH2EZNtAY1s8GAmF3wSRFeU2-LuFk1h1S7HlLzcrSmebmWP47Fj2tLwpxusfQIhJ-9M-Yk24Mr9V7xkLoE9T3DFxSllroZlW1XIIsqWV79huCgl1n4gn8gER5pCYTHonCciMDUk84hgOZPI_NrXjyG4YgTWLwivlunSfQH0b67rbVQ6wvnwNCVq1UIWYM77Xy94WWCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up4sN4VBxQdOYs4yWnNdLD9U5iUJVLrNNFgVN_1cNg6cFxMK99arCB9pDgZYKfmaUG2apVBFZ0Axtq37HPOOGMKzM9jZvMrLAWUjRQ3CYVd9ODG1cLuoZglSyx5BOvLOD_BnuPlamPxyHhFuxbbPGpgQV1TKoya8ry6YRhuCnF5HO-bmcy3DqvO2xlen7xxaZEhSNc8Is378nw01iRbEUgpD1JsskHtCFHyXIKrL0PGRxOnc8yzVTm_ih1gUyzz-sm76b7tSv-sKEs9Ag7iz6kjYOs86y_J7jcOYyM02XUr6wO0yXYyGPMWon8fPbIffbg7vHXCYgsjjg9KMayUpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=edSUS0DUY8pUVymDG1rqy6caukCjA5YbARiI16D32AC6HDIPAmSTbkkyKTuyhfTIGQQdJNN45m1JhpswRA_o5sGb8YmsPqLpHUSUpQl2R0we__Cf_qSo3MSlvctoJF9-zHkOomXOrRUmByXrjckXvqE_MJ3H9KK5PV43-4o0xAKro5wTVHB0EWGNxBC-SWHHklPnFyeEgdBX0NreaulvZq1x8MteA8gmoR8VR51h3Af7wUAK_jc4siBDCRmHUugJRH-LEzzjAblAL6OOUCNNAyCsu-gWqI1R0dnMn4w57KF6xziQC-eF4rbKutxfnd1EB9MbV0SLs4KSIRRHQFewHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=edSUS0DUY8pUVymDG1rqy6caukCjA5YbARiI16D32AC6HDIPAmSTbkkyKTuyhfTIGQQdJNN45m1JhpswRA_o5sGb8YmsPqLpHUSUpQl2R0we__Cf_qSo3MSlvctoJF9-zHkOomXOrRUmByXrjckXvqE_MJ3H9KK5PV43-4o0xAKro5wTVHB0EWGNxBC-SWHHklPnFyeEgdBX0NreaulvZq1x8MteA8gmoR8VR51h3Af7wUAK_jc4siBDCRmHUugJRH-LEzzjAblAL6OOUCNNAyCsu-gWqI1R0dnMn4w57KF6xziQC-eF4rbKutxfnd1EB9MbV0SLs4KSIRRHQFewHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTf6IrKne6mBbw7Z1F1p0escidBZhVz5cyhAO709NpMKngk_hjdE32uMDYpGdwN4dV8MGwhtRDCU7eZIXQoY0iWSkIdQVGs5uaKZ7LVbOC8-MI8Tgp4FJ3p_cY2SZMe-_EGHK_YKzIkljhEXcUvS23dpO8RYFATuP0S0T5cLvd-wtgAlCJDY19imkomOCT9vhH31WBpR5N_UDqSTduFzl7tc7neFuLKA8kTe2oCVRZgaPh9QuDDHoz2bwWAcYTROzJjTbeqAP03gHDvpiska31H3GjY5O70RxC2rviSaty9TmM63wpOnXLhE4onOtZsJsMVBUt-LyPIB8tAZ3KtBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=fEeTFf1qYU0paK9QtD0ntV0KH6KV_-8WU7YIYW10157Ad9_KsxGXSzb6yHuuBOpNuzMsT6mS3YlVgg38zepHDpT_Ot4j3aVBRPRmwMKfotTbV0T2bCyhqrWVEWpvSViRzU_PW8FnNiKoJV062IDgPSwz8OlHo5MDD0qvh-kHlXse1LKFOY3dATdZJh_-hY3Nyni_h48P87gKofIN4HFsAtZOdefiq5K3opa0AcV31uNkAhPBzSPhm_G2YZTxyo8U_wnhe0zw8gM93tZO5-9zK6HXpsEPSZlsuZ_O5Y9iE4I_8ebGAV0v4W1sbdyOecDaJvCwFuVDlcLZEJKRzGUrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=fEeTFf1qYU0paK9QtD0ntV0KH6KV_-8WU7YIYW10157Ad9_KsxGXSzb6yHuuBOpNuzMsT6mS3YlVgg38zepHDpT_Ot4j3aVBRPRmwMKfotTbV0T2bCyhqrWVEWpvSViRzU_PW8FnNiKoJV062IDgPSwz8OlHo5MDD0qvh-kHlXse1LKFOY3dATdZJh_-hY3Nyni_h48P87gKofIN4HFsAtZOdefiq5K3opa0AcV31uNkAhPBzSPhm_G2YZTxyo8U_wnhe0zw8gM93tZO5-9zK6HXpsEPSZlsuZ_O5Y9iE4I_8ebGAV0v4W1sbdyOecDaJvCwFuVDlcLZEJKRzGUrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=H82P0sx7duUgDhzwOil5kMVagNWYC9G9m4fwZy0VW7VvPxNhBSsFHBKJn16Yf3gVyswffi4OR2-xAKMKEl9YJp65vVUDaHlhM_Xs-pFYqgveODkSG0cMXDkl0-pFtaL78-4lMRVtYSrEltvokpNLWDQqJGk5Cd5PFEhmVpVqQwi6c5wQOpS58_zGgcEUt1u23MY5SRGVagDlmK8wEwKVOlDNmksbF-dk1EnvH2L-GXWN62DmZlewht5G7tQYlWkFRF64a283VueuVFNV5PN4q9Wyz-GcPVaOT62OxQdzq_H8m_JN2tipcAPiRZAK4jLyQeHFTgJIZhiWLddzCPE7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=H82P0sx7duUgDhzwOil5kMVagNWYC9G9m4fwZy0VW7VvPxNhBSsFHBKJn16Yf3gVyswffi4OR2-xAKMKEl9YJp65vVUDaHlhM_Xs-pFYqgveODkSG0cMXDkl0-pFtaL78-4lMRVtYSrEltvokpNLWDQqJGk5Cd5PFEhmVpVqQwi6c5wQOpS58_zGgcEUt1u23MY5SRGVagDlmK8wEwKVOlDNmksbF-dk1EnvH2L-GXWN62DmZlewht5G7tQYlWkFRF64a283VueuVFNV5PN4q9Wyz-GcPVaOT62OxQdzq_H8m_JN2tipcAPiRZAK4jLyQeHFTgJIZhiWLddzCPE7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=qzqTu5h_VT2UWGAjyqe3gEAXYLdZ2IhFBfQlNKlmVpNkZyZwIbMPoWVaBXaSRaAKnnTt1ZFwaWFtJw4rxqi49xpkg4Y4UFdU4hDRkf5PXuMeo5zJum44e5IRycD6SqmU746pNN_c62F25EEapTiiwLm7rcwSQ6YnNcHm9bYR25qpQY5ZKfbM1sH8qs1gQ22qlVG6BkgV36DGJGTS1yTeOegm5s9knRrDPZi8hYmm4napr1SdL_cBxwyQt9n2Xrrwx15U2r6jEYTz_IywZBz-U5JbXbgidyCO6i_7yqnZoislFaES60CGjgWzEiyZVrCSz4hBs5pxT_9J32HqqVE_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=qzqTu5h_VT2UWGAjyqe3gEAXYLdZ2IhFBfQlNKlmVpNkZyZwIbMPoWVaBXaSRaAKnnTt1ZFwaWFtJw4rxqi49xpkg4Y4UFdU4hDRkf5PXuMeo5zJum44e5IRycD6SqmU746pNN_c62F25EEapTiiwLm7rcwSQ6YnNcHm9bYR25qpQY5ZKfbM1sH8qs1gQ22qlVG6BkgV36DGJGTS1yTeOegm5s9knRrDPZi8hYmm4napr1SdL_cBxwyQt9n2Xrrwx15U2r6jEYTz_IywZBz-U5JbXbgidyCO6i_7yqnZoislFaES60CGjgWzEiyZVrCSz4hBs5pxT_9J32HqqVE_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=jXzsCjZZa18FLi4vcPIrwbs3TsF3OhpbCkfDRIYosqQWclXWqV_XsuSZykdKwa3u4DKBvYFZBPnFCqljDgPbf0qkYT2yFhfDL9XizESj_PRy4n0vf1uWGNGtfenRtazceixpvOzqBLNEBRqFwViIcTY78cwbmJdm9NLGdWNlcx2C9pTqCI9d59Qcv6eSNtczXv16isM2eAHt7Z0nO4GYlKMlXHTNgkFNmJGmWQhe4aoge_TTjD59UmHZvHPjFg8ZiauNsWrV7rbT92FldIIg74xK-fqiYJuqJ6FmlD_kN13-CftyWo_yL3JaESR8rk1-eXQKEPIEsIAidYc03v4djQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=jXzsCjZZa18FLi4vcPIrwbs3TsF3OhpbCkfDRIYosqQWclXWqV_XsuSZykdKwa3u4DKBvYFZBPnFCqljDgPbf0qkYT2yFhfDL9XizESj_PRy4n0vf1uWGNGtfenRtazceixpvOzqBLNEBRqFwViIcTY78cwbmJdm9NLGdWNlcx2C9pTqCI9d59Qcv6eSNtczXv16isM2eAHt7Z0nO4GYlKMlXHTNgkFNmJGmWQhe4aoge_TTjD59UmHZvHPjFg8ZiauNsWrV7rbT92FldIIg74xK-fqiYJuqJ6FmlD_kN13-CftyWo_yL3JaESR8rk1-eXQKEPIEsIAidYc03v4djQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=AGAAu6aXvr6-APLBQBW4EM_60ksVshFNU9KKqDn4aUzszrypiexlc-Np1bF9-YDvgE-zKUfdE0Pw9zDqWov4UhMFp0mY12dgiIeV5E3lsT7JtbjOw_DBbG1GkXUT7Qv7fr4ps0gmuVMMTy0-YboG8HGLlVT-1iqGzje1S2XmjlgQi9ehADMiyE7CGkn84DDmsJVXVbHtS-SaeKn6dWk33JFomB5e_f2yhVnNBwMRS5E6qzSi_UX91vidV3j2VPwPjpA6pH8IY5oiKgnzbr74Wp6yqASi5L2MkwzYf7DIHHPfgmxz1WBRu3jQjG-kfEmjnU73jgAOPF0fUAe-VfKCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=AGAAu6aXvr6-APLBQBW4EM_60ksVshFNU9KKqDn4aUzszrypiexlc-Np1bF9-YDvgE-zKUfdE0Pw9zDqWov4UhMFp0mY12dgiIeV5E3lsT7JtbjOw_DBbG1GkXUT7Qv7fr4ps0gmuVMMTy0-YboG8HGLlVT-1iqGzje1S2XmjlgQi9ehADMiyE7CGkn84DDmsJVXVbHtS-SaeKn6dWk33JFomB5e_f2yhVnNBwMRS5E6qzSi_UX91vidV3j2VPwPjpA6pH8IY5oiKgnzbr74Wp6yqASi5L2MkwzYf7DIHHPfgmxz1WBRu3jQjG-kfEmjnU73jgAOPF0fUAe-VfKCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=ZLflZSXMwJMky-wc0xYbfsEcHAbuNj1LiAHjHUVMiHRJUj8aH6OznuWsyDGK5pC2FrQ6pfEnlpEqmN9r5SUYzAT7SEejPCO9fUoekohDH3rjtgM5sVFEehmePditmLT_19DUwd3632WgovLp6kX2rUSsUl1iuovTioTt_Cnl8DqK2eQXkBpga0GvJuodsrFBn17qE3G2YpDFQnYYVX6KcceCXUUhmTcDOWDnhSGXrvkhHaQTqYZ4mYk0jpMOZ7Wgb9nKBLqYlglyzF1vBttMObRjMEv_jSsJnEwwQGVeFnpgurbjnUzvYR45fQZiIcrq9mGLqX-Pph9b4NPCRV7Ymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=ZLflZSXMwJMky-wc0xYbfsEcHAbuNj1LiAHjHUVMiHRJUj8aH6OznuWsyDGK5pC2FrQ6pfEnlpEqmN9r5SUYzAT7SEejPCO9fUoekohDH3rjtgM5sVFEehmePditmLT_19DUwd3632WgovLp6kX2rUSsUl1iuovTioTt_Cnl8DqK2eQXkBpga0GvJuodsrFBn17qE3G2YpDFQnYYVX6KcceCXUUhmTcDOWDnhSGXrvkhHaQTqYZ4mYk0jpMOZ7Wgb9nKBLqYlglyzF1vBttMObRjMEv_jSsJnEwwQGVeFnpgurbjnUzvYR45fQZiIcrq9mGLqX-Pph9b4NPCRV7Ymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxofeDPAjiB-vlq3TVgP7gx9AdW_ZAQnBbyHX4cLFhvTI4kzc3nU1FXQY9IfQrAPD3vYp5nzsMLNfAuI_dzidPm1wRZSNpoQieXhDJa-_RWjXwn913OG_aMxKTbBdakH51bPtBRQCD6R6XvlBwGlrKMVqzaI_4qaM3eDVHsYEQtBqYiM5DKPVNJZIzzb6Logcz3vK3BEKkjfDlS1VQjV6xvV-LeTolKxpxbjzBx4DUkp6FvtTtP-5VwuYuOQuDqhxcoGVglC0JCV7DJHxrQzC6CUJ2KYbiwV-LIUiE56djAxbTBRhE1Mlc9e9HqmhbB3ABB8AU-ldpB6PQQTWpk8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaMmwd47t-yYmCcwzuB9Ff0ZwjGEs7l7kVC0SM35W9qlY73hTza_Dfvt_EJG4xQXXqsegmS-MQZQgn0YSIbxvwKSxgytrAXHsb_cZ2G2HOvIRPbFfmDmqE8uhEjMXecRx0tzDJqwx4UZe4Df21Tu1Iplh0Xh_xDiFWz-61hXA4tcJ9qpxz5LKexJHFZUYCyjUc2xPWbHs9Y8rbjquwMzjG3w3gTbZToR4a0iK7p4XTKelQfZyTXNjatfqSxHolN_OIMbDTQif14xbhycLIQUhIBZ6wgxzEPMU_XKkQ5oUPikKZd-RaDEe-12qdQxWEOt0YkygOJJqGWFW3X6Rr18fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJmeN3EMfW4qXOnn5lpkRL0G0aRI-W6rsnQUJXGhvlgavq9BuqPT7d2kdYcSqpI5kXbEYNT8UkP40WFWIw0uwX9fCBXMw8vWcVqRM1tedxuf6t7BQwwYjour3RWfAacmjAsKaenozRwGN-9Bgovd5t8wxd57VewOlLAhLLXzHkzED1b8j-nCefzvDpXLVWI2K4SbGSRprpDDtNTgSCDxUldd4Evo-EbMHmYanqWJflSo6LJJLyyfw1qNduoRsdJLwcYOvo7_BY1t4AKFLCTp4_XUwvCoENh6ubzq_ZzJmCKCylHQ8TC78kZEjZ-F7zKbSUgCG77EV2Lo6ivU7vJvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=OVDkvIfSQDbANAhmM4j6pRvn1qN697I9adXwizDGsBVSktv9OsLg19Ls6KHr5sq2UgnSOpZhH9bRAUjzlMRqf89UzhC6fu1TZ6U4cV6G6ZF6JvGwk47nO7a0MLhr21DFXsmjTLvLx4aWv8d7BAd8qutyKKenAgEH16EHwPdNH3zJLjKXHWoSj-KfXL4KIA7a8LWHUSrU0S1dw53HBcL0iswxoVJOYAP4dHaUSoxwiPBKEFsKoiq-DiCoLXa8NLi8gea7RX7L_uZ6X9Pz0T435xrbbNcQ_EiLAbBGngctpsIzKjUwdx9ws9bH_XHP6xZiJH6l7xu5ikSmrYniM7YkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=OVDkvIfSQDbANAhmM4j6pRvn1qN697I9adXwizDGsBVSktv9OsLg19Ls6KHr5sq2UgnSOpZhH9bRAUjzlMRqf89UzhC6fu1TZ6U4cV6G6ZF6JvGwk47nO7a0MLhr21DFXsmjTLvLx4aWv8d7BAd8qutyKKenAgEH16EHwPdNH3zJLjKXHWoSj-KfXL4KIA7a8LWHUSrU0S1dw53HBcL0iswxoVJOYAP4dHaUSoxwiPBKEFsKoiq-DiCoLXa8NLi8gea7RX7L_uZ6X9Pz0T435xrbbNcQ_EiLAbBGngctpsIzKjUwdx9ws9bH_XHP6xZiJH6l7xu5ikSmrYniM7YkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8ACmaG-X_5hvrg_nOrwv2aysjH44zChb9xY_CAKaxNAUauF11OGO8sD2UFBh4zZVuOMhSh-wklqF-ku6vFUc3a1DDfwMDVYTPdp0e19XQt92wWq1ZV76LV2w-wRuSgss8AAKKZ2PcRDRKCPJ4mBFoZyJ85FF_A_C6iUiw3kWBaD5F4nNeKY6686x0rsYy44w_Q2YH4ZnBI1Erans8AjjHIbEijLt76sWS4W2iVctwM1wj5IjUEd6YsfNJ3PEb3H1fJOWNUiGPcAjPL36tKNy7Dc0NozVVF94asqzSNp0Hy50Tkut7epuljUK3fGMnA4H9X5bxQEEyzT9x67aAXYHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CluCxWme4ao1qQTslXbEBVtBzpXAl9aP5dl022HaO-1o6GdAj6xK3d6QdaoDPpbKFh7EyvE8WKiuUVvHYioA9ARcf4JcdAGtEyyUh64-LcdfIa0vT7Wci1NZbNbCGmI8g12SVCgih-0B3Gur3z0BO-Aaz65glnetuwXTXnUqWNExjUdUSE31LooElNGGQpZY2Tm5CSpEFh6hIUgoGckiwhnDyg6hhu5sWwFcgstdfD4wtK9FtkghvD1Sf52rHBsfWC4sTVBeJa21bueHQ5XOueqzNkHSPmckGjdT-kwbaQDT-il5YN1sqAQklR9eT37NGfViGk1129Ooi0P8mgWFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_6dZsAEVR5di0tYdOKb8MQlkY0IRefM1ZJMullmNwfcHGC9_lSIVg137Cf15eEn0LYJCKld0dmthfKSXm97VbA2QCiVpNPpGFB0ATn8EI_XHPW5gliDZie7NUO4ras8z9-g-sc0em5OBEb2n8UPyd4GWZ8lc5S4xDaXxgdDZwCoz8LkH9MlATSWvlCKVvaH7uKk9NEgddJr5tHTHVqSaVmGLgKdYD59v6e50XVbYgjjnMiQfAEUMNjjhzSG8QAHDnNSMKJNUuejg3V7qOpbz7LmSAfhueu0lEfBntAG6bFEJPdfcs-My1KVXIJKQ_TG_FBExFJX9yhTm4L1M2RkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=N1N0DrbbJN8-0QmtSAwU-6UWBGXiUusqEjnbkVzHEt34vfjiyU2u7Qhg7bAJO7vyBUQpPYmavql2T_fXozLU1Eci8CNPVlct-kRH5jL49E9_RHiek75ny2lAtucPC7fNkIBOHvKwXIyoEduNgnLV0DK20AegthgRy4oqTmJdcLekbf4t6V7SmyhvzFiGkyfdBE6LHDFVk-wflGHRg7vc8zzHlgS31Fia9ELuZY228buraFl86Y6bp2S_zgq79Dyuw2vkPxDy6wJaKBHmRdc7L9wr8FNQxP8ixm0ZHbl_TZNqNCX_DQiCYIWTZ31Saijct5ZHoHRWVPfEKJ-i0SVuHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=N1N0DrbbJN8-0QmtSAwU-6UWBGXiUusqEjnbkVzHEt34vfjiyU2u7Qhg7bAJO7vyBUQpPYmavql2T_fXozLU1Eci8CNPVlct-kRH5jL49E9_RHiek75ny2lAtucPC7fNkIBOHvKwXIyoEduNgnLV0DK20AegthgRy4oqTmJdcLekbf4t6V7SmyhvzFiGkyfdBE6LHDFVk-wflGHRg7vc8zzHlgS31Fia9ELuZY228buraFl86Y6bp2S_zgq79Dyuw2vkPxDy6wJaKBHmRdc7L9wr8FNQxP8ixm0ZHbl_TZNqNCX_DQiCYIWTZ31Saijct5ZHoHRWVPfEKJ-i0SVuHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=MQ60fI-mOwDdRP4-_f5mWKGc91YUQv1tZu1s_9IrPbvgDha2v4Ne6SHyrjgYC6K2HH4B4UHfEmVvaq6fxmCkWT0tmTatcJ3V5oFbKi8xDgOGTkkrUvohC09gBIJeKV1WsOaKXSzhbUfdk0Gyf6BRHvl3txRruhTg2sflk-QwmL2ungnbgoNxXNign6rsdXqh4XVHGW3W8xt_jEK3wK-ckyp-zmd0fd9YSuOcKR84vQuPhymAur9nyqAXexaCA2d0E8LSGh0vH2XQ2qhEGAS20JLMtq5fua7S0yN2G4ewZmPRZM6FHH6wmoQtBYdzoWGsY0llP-GMfXJwqiaTpr_NK5nS-_4fOv-GPdHEyR7b1l-PSQk8UGuHbSbV3oMutbUaO-kGKRpEiU8cc5prUGD--UV1WxmoTE-fdJiy8eJHDNlMZ1dcqSiWul5ozK3Iqip6dKPf0IikquQoVkIgE-6clDEnJLCjE4oc66Oh_E3s5ga4rYNjhNHbNl0kfJGO09_LqLvgSStRm5Vi35wssMy3mlwPUlEEHXIxkMovXNsJKcr0U3VR8A-ooNzYfc5rm8ZJCW4dGMRAmBmJmcVwuIMWtUCQcLM3BkrrNQzkKRfjlsFKsU4hdvqh7NqmXQF9fuKst5X33E-xqtxKwmNoTE1Zyv_Mhowj8yw0WtudKB2nTY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=MQ60fI-mOwDdRP4-_f5mWKGc91YUQv1tZu1s_9IrPbvgDha2v4Ne6SHyrjgYC6K2HH4B4UHfEmVvaq6fxmCkWT0tmTatcJ3V5oFbKi8xDgOGTkkrUvohC09gBIJeKV1WsOaKXSzhbUfdk0Gyf6BRHvl3txRruhTg2sflk-QwmL2ungnbgoNxXNign6rsdXqh4XVHGW3W8xt_jEK3wK-ckyp-zmd0fd9YSuOcKR84vQuPhymAur9nyqAXexaCA2d0E8LSGh0vH2XQ2qhEGAS20JLMtq5fua7S0yN2G4ewZmPRZM6FHH6wmoQtBYdzoWGsY0llP-GMfXJwqiaTpr_NK5nS-_4fOv-GPdHEyR7b1l-PSQk8UGuHbSbV3oMutbUaO-kGKRpEiU8cc5prUGD--UV1WxmoTE-fdJiy8eJHDNlMZ1dcqSiWul5ozK3Iqip6dKPf0IikquQoVkIgE-6clDEnJLCjE4oc66Oh_E3s5ga4rYNjhNHbNl0kfJGO09_LqLvgSStRm5Vi35wssMy3mlwPUlEEHXIxkMovXNsJKcr0U3VR8A-ooNzYfc5rm8ZJCW4dGMRAmBmJmcVwuIMWtUCQcLM3BkrrNQzkKRfjlsFKsU4hdvqh7NqmXQF9fuKst5X33E-xqtxKwmNoTE1Zyv_Mhowj8yw0WtudKB2nTY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7GlyFn7qnEIh8nD79iEchXA9n5DA2-eaOVF7mROiwWtX9xWMmBK3CuWgR-KNirYtz3kz2yXh0v8o0F5i-UJ7eWjzUAh6jvKb6SCCGSfjOcMnsPgwb2-w4cL5fHtQtJH8OidJsCtrIvufaY6IZwsUVSeRnz50yfzry4plaWYHCknXdnyN45MJLIgPoK52aMcfuSxS1ydJn5aBx79ih6QsUHWhDP3g253xEegriEgNhZFYxemu-ZWKjmBJvEhliyngLIESlknQroHuWz9OM1HX-8JhGehGrYKP2Zt-aPdqVR8NUdE81JGEzff1nkzUAu6jwGbIOf0yo5tglZ5oYbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=PosyWw30B-laFtbU3vwdLTd0zBQ2FTAUwFvXzEdfBK9TwZybm-p--clb7xq5PLpbZFyYXmxiiiFyDcjWN_nViPur5npzCVWI5Kt04mr26j02g7Lgun_Wzxf3gbIpbY8M9126QTP4zDgZb-JmxjQ4TwxWcVE5gH9VHXdxL75S-8TORtDcQOa_LdM4EQPIC0takQmk56eZFxWe0H1CpTphxAevScvdfIq56JXrTOoy42CFkJnwogn_nwJmE2H8cVdFidWQBCVb-WLKxR_DnQZDKZpaKCqouj5zLNwOxCxFTS9SzMswrRm-QZREr-SDXDTWkJmVIpQydb_Hcrvg40AS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=PosyWw30B-laFtbU3vwdLTd0zBQ2FTAUwFvXzEdfBK9TwZybm-p--clb7xq5PLpbZFyYXmxiiiFyDcjWN_nViPur5npzCVWI5Kt04mr26j02g7Lgun_Wzxf3gbIpbY8M9126QTP4zDgZb-JmxjQ4TwxWcVE5gH9VHXdxL75S-8TORtDcQOa_LdM4EQPIC0takQmk56eZFxWe0H1CpTphxAevScvdfIq56JXrTOoy42CFkJnwogn_nwJmE2H8cVdFidWQBCVb-WLKxR_DnQZDKZpaKCqouj5zLNwOxCxFTS9SzMswrRm-QZREr-SDXDTWkJmVIpQydb_Hcrvg40AS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCnp6X-I_1ELGYMHwISDkj8enNM5gFGReQEngRosma7gWGtGBPki_jGNOlDrAzfmxTP5YZNo9zTiVPBMBMC72t7CuA36hEe3G8w7KzJ4sV3V3rGSVuB5IvOWdG_uhtmiCBJ0zDZWKjZccvXGngHlZQrclpYTVsVnepfEQWDL08j0GNHUBjEh66qUW0P1gcrRjE_dOKaM5QJGW6z7iv5jVmX6V70m7i8HTF32BCQN1oti1WgLATOUIauAJBYMmg6pIPczQv_A3qGbtgWfoqLjiuL_5y7ugIvxqDbPfATKFYShpBm4JS2jAocLWVBeLYr3L-_UCM_rRZPGJNdCpkKWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=jq9T6ZRT1IwXNSvx12PMZP4fqP5gHMduuKlqgnBXdGAWfBza-E-87IO8tx3Qwg1sRZqNF2GJQv8-qy24diRT0YZ7fpVNzWTGslWIkIJTCRbCixZTK6tYVAKw-uN906e-SBh-toHSoVEr_NR8frZxzt8l_tYkA8-7_OAsh8rkbQZbH5ZpdzRnbpBRGE0Of9-xqqs7Wjw5SM9vsPEE-sPPSmYcI03ZxJ-Z1-lZyNU5kQxJqItQBWKOHOp5ZnmWrvp2cqnt2XBr_wN4d1aGFQumSl9hb4uhd_tgQ1PHGwz9-YNoNlbGtfdwpn1YFWo4WqT4_r1SymyXcrKNsCOnHstzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=jq9T6ZRT1IwXNSvx12PMZP4fqP5gHMduuKlqgnBXdGAWfBza-E-87IO8tx3Qwg1sRZqNF2GJQv8-qy24diRT0YZ7fpVNzWTGslWIkIJTCRbCixZTK6tYVAKw-uN906e-SBh-toHSoVEr_NR8frZxzt8l_tYkA8-7_OAsh8rkbQZbH5ZpdzRnbpBRGE0Of9-xqqs7Wjw5SM9vsPEE-sPPSmYcI03ZxJ-Z1-lZyNU5kQxJqItQBWKOHOp5ZnmWrvp2cqnt2XBr_wN4d1aGFQumSl9hb4uhd_tgQ1PHGwz9-YNoNlbGtfdwpn1YFWo4WqT4_r1SymyXcrKNsCOnHstzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYlOO5CHvIw8DksmfDlUdlHoiqyTBfxjHR7K1Li_HaZZWPEA8JiHPB2HGmj10wBRdAOPd259ic97xey83tuj9eWw-d-Xwy8YqM0ztmzeCo1nsrusWpkBUbY4QW13sjbdYCvC_d7yqBF3D2L7FYsL709ESHZKHftbRYH2_D__N7PjIH78OFcvLJtoImq4gOfcJCVCp2gE_9hjdl0IKxpkYsZMMf7Prgc2am04CcZn3fkH9-eJ-8WE3JDCz3tv-QZ0Gnh_7YCVmSLz00xDa28-7o8yByQ58eGNGi4xg86So1q5F457O3MIl5_D0VBl3tPr-JuHptLyktmaCyBI23p4og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=cLDFN5BcDWECfvBPYW_JQjNvhIqHeZxiVtTZfG9k_CPCF0dAoqXKrRU6VQ1JfXnWunCfS4iNqpJok3NjnjOevy-L0JXIfbJYRmaHMjFqza3QYHIC_DgTMTMsEqcVjA2CHdcs_6yt6c9owiGelJaa6_EC1P6L78Jz1323Y62S4bYYBOn-nBKcWWuGhMFzAcPjl-pBwmDMYESQ6qqH8WxpqQ2NWLC3Ts5DTBz8bsor45SS7coxX6zPl9F4or_UTVzQ4e9zd_E1B63uYJNjnLi_4if8Rx_L3We8V5ODAJGqb3_Ovlo2UY8W8aqx96UzA_7heBDj3JtMETjET0apfxxSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=cLDFN5BcDWECfvBPYW_JQjNvhIqHeZxiVtTZfG9k_CPCF0dAoqXKrRU6VQ1JfXnWunCfS4iNqpJok3NjnjOevy-L0JXIfbJYRmaHMjFqza3QYHIC_DgTMTMsEqcVjA2CHdcs_6yt6c9owiGelJaa6_EC1P6L78Jz1323Y62S4bYYBOn-nBKcWWuGhMFzAcPjl-pBwmDMYESQ6qqH8WxpqQ2NWLC3Ts5DTBz8bsor45SS7coxX6zPl9F4or_UTVzQ4e9zd_E1B63uYJNjnLi_4if8Rx_L3We8V5ODAJGqb3_Ovlo2UY8W8aqx96UzA_7heBDj3JtMETjET0apfxxSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ILaPyKXzrqum32d_NnIoQCcpxihPfv4u1S0kvBJTlxsaPBeS9A6r8G9xRtxDLStNmsoWwkMlCKBn67Dk1SBit0x3-7_il7BlJLLeQJwRrs-2A1azIX3pGhFqA26JZdpIuoVfJzJTvGRLgaN7T-FY0bRfm8kDSbzZSNQDNWH4dAGTGf7OA2SDpXThc8A5HVhJJbV40_gFZ13ba7txqrr80pbsgKfPIzsvRjuqWm5fyuyXsaogu_Jx-5ZW7RIQxKw2WJOw_r5eMJ_yT2TkcXbkZ-AqV9hLUmfW2jym35eDz9JlQ1oBZ3q6-nIDQtbdwtU-3EzH4SVIilbowXqY0o07WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=ILaPyKXzrqum32d_NnIoQCcpxihPfv4u1S0kvBJTlxsaPBeS9A6r8G9xRtxDLStNmsoWwkMlCKBn67Dk1SBit0x3-7_il7BlJLLeQJwRrs-2A1azIX3pGhFqA26JZdpIuoVfJzJTvGRLgaN7T-FY0bRfm8kDSbzZSNQDNWH4dAGTGf7OA2SDpXThc8A5HVhJJbV40_gFZ13ba7txqrr80pbsgKfPIzsvRjuqWm5fyuyXsaogu_Jx-5ZW7RIQxKw2WJOw_r5eMJ_yT2TkcXbkZ-AqV9hLUmfW2jym35eDz9JlQ1oBZ3q6-nIDQtbdwtU-3EzH4SVIilbowXqY0o07WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDv10YdHOBq3rh-7pDWzv5hCVBsLLahbdzN9vMMgmrUZ8U_iP55BiK33odV_CtogssPzdhAXZQfyAL5B6zUWoYt4f8AaDintAZYV9BqhaZH-CH6P220boV9W7hIhDrZh8kUrLrwMSlCHi1BvJdhB_FT9E6nJZ5CgnwHRAPrCLqVNUWOEZca0c05SpLqYMKkfBaKAvfnkg9Ke5_DGQMOrXjVtjUQXqOnPE8yurRX0DoHISbQw9CyvPNcxh32vCXoXODR6wTY63i8WygfULMxOm3mOND57YJY9CqY9YymMhpN16ErAUpVxH0tjSN30UPtY2n7HdHU3gpjU_rOXBA2vxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=OH9R9dM93KCFUZg9vnKWhuMpaUBY0KBbk9fn_ecenkCdcHawRIU2kSwMfzKZCIQ84gCqy3ftiC9oq_wR7zpW6E6wyCx2HmwiKhZ52xJEPyvtOi0DO4btvdaNlnFheCL5pOVTw_lT6vkwyrA7EA2v_6ZQUCw31LLBlT6cFQqo8Bt-3XpJFblxD9RfYMhGCJLMgEMR0On-DTZApeIBzl17HNLukkUiR5g3zwKMFvNroLte9RsHxjR_On83y9WNNwgUj-lTNBnEbFf8p8PZMh-XTchhNXuLvSmBUfGkAr6YSWRcng8Plr9bccV-1HUFHS8Zbk7pl8GjhgcOrd2AYWNnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=OH9R9dM93KCFUZg9vnKWhuMpaUBY0KBbk9fn_ecenkCdcHawRIU2kSwMfzKZCIQ84gCqy3ftiC9oq_wR7zpW6E6wyCx2HmwiKhZ52xJEPyvtOi0DO4btvdaNlnFheCL5pOVTw_lT6vkwyrA7EA2v_6ZQUCw31LLBlT6cFQqo8Bt-3XpJFblxD9RfYMhGCJLMgEMR0On-DTZApeIBzl17HNLukkUiR5g3zwKMFvNroLte9RsHxjR_On83y9WNNwgUj-lTNBnEbFf8p8PZMh-XTchhNXuLvSmBUfGkAr6YSWRcng8Plr9bccV-1HUFHS8Zbk7pl8GjhgcOrd2AYWNnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4PSQTMor6aO26yd_j-5b8e4cJgodTQOsFNVT7OvzcvgmK15QDZwK0CIBUiNYOMHua1wKckp7f0_XXDLVXZfbEQsEdHh2HXlAAAVbUy65SO-Pc93uyP4vV3wLK60Gz3kysBbFyncMWOl55UBP3WEJO0FgU77Ohojwb7UDZ88UOloTz41vquG0ys4aXKWBL8yR9xEhSqmr7gNn8zCBwMsxSQEgj6LLNURGMovOE1_7UvLu1eOdPna4vhfXt1jEFMw26VH_qsYFvsIfwptbOVTtMHrJL3iv1JznXtEjtmXH9r7lvgH_8LeqLlaYyk-yNc6TqMaOWCDAPhY0jNtKy05cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BKvqU4dOD0jDvAiDqAnVMpURDp84ndj-BRJVTVECqiv_BfzGQ0eFyf27mRbC4JrPFHgvMAbVcg1dvJIBRAt1xzQGh0AyLG5YredTATw84q-FWeHnl_J-66WIIlPqf0yXMVMsmlEf_oX1eAOirj05Tx4d1AYs3Op7L5kaTtsa8vku_kelRs_b6RHgZjSi2CWSJ49hSPrDcNrmRSkb2PFhD7-IOpGmcclum2P13Fd4QKazVTl1Fna3U4TV277bhfMzJKGmJbBSHrItBHyQzB4h-wmslm20kAqoKNYHwbGWcHpKTfstDYaD2Rp1UMwHMP7PNEHSUW0qnUoi1IjHqbeyIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BKvqU4dOD0jDvAiDqAnVMpURDp84ndj-BRJVTVECqiv_BfzGQ0eFyf27mRbC4JrPFHgvMAbVcg1dvJIBRAt1xzQGh0AyLG5YredTATw84q-FWeHnl_J-66WIIlPqf0yXMVMsmlEf_oX1eAOirj05Tx4d1AYs3Op7L5kaTtsa8vku_kelRs_b6RHgZjSi2CWSJ49hSPrDcNrmRSkb2PFhD7-IOpGmcclum2P13Fd4QKazVTl1Fna3U4TV277bhfMzJKGmJbBSHrItBHyQzB4h-wmslm20kAqoKNYHwbGWcHpKTfstDYaD2Rp1UMwHMP7PNEHSUW0qnUoi1IjHqbeyIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=aaMgaGF-vtCKTnitvp9g5APzMxaxejgLyd1DdI1CQVEVPxYagVZIeqBKXIGhAPs9sgduUgF4SacIeW9-CKqBzkhyWaJADfAH6WnTUD7YASJ-13IfeHqYfbYog_rRD30EC9AUbtQWyTpgwxmqu1xKqUG1VQuEFMvENh2FrYZZi9X7vfZb3-Nnt4dDRDomItUiDfoLlkyhzjT0HlCaIaeQsjW4a_Gx2vO-R0dhu6V7inS7NMbl76mkqKrBbLsZ3S0kY5EM5yaMBfG9nkFbFjSEueX1GM9mfYWiavF6BCfUkV3ZKuO9jWzMN_JqJynAXxMsMZWcij7tNwAX0XyRtQQaqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=aaMgaGF-vtCKTnitvp9g5APzMxaxejgLyd1DdI1CQVEVPxYagVZIeqBKXIGhAPs9sgduUgF4SacIeW9-CKqBzkhyWaJADfAH6WnTUD7YASJ-13IfeHqYfbYog_rRD30EC9AUbtQWyTpgwxmqu1xKqUG1VQuEFMvENh2FrYZZi9X7vfZb3-Nnt4dDRDomItUiDfoLlkyhzjT0HlCaIaeQsjW4a_Gx2vO-R0dhu6V7inS7NMbl76mkqKrBbLsZ3S0kY5EM5yaMBfG9nkFbFjSEueX1GM9mfYWiavF6BCfUkV3ZKuO9jWzMN_JqJynAXxMsMZWcij7tNwAX0XyRtQQaqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Sx7QoFYF7N9ltPz8OKUGJl5m48HKoxnyiZoX3idekQJaINI8jraP47URyZCfc2Qw-dkMpdpcLaK4NPVvh7sDKoTndskPnp5HY5hbUuJRbkKY56ikiMr06KWEx3hAg1MuCEkUfP59gJF-1297_P5Mk0FcMM5UPHpKNj4_PjWu4JxoRvfqQ3JhrmZquvcVHU25lloLWSHJhCJv0S_Vt1FUywE4Jwu839M875ok3V3X8PMRyxaStkpL3WCxLRQLNivcpmyKQYtqs71fGnHRRsxduIneLn19gd7MzoutfahMzJKepVGLBreEhRZsOAhki352Ma_4-Q7T5b6NNToN6qHF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Sx7QoFYF7N9ltPz8OKUGJl5m48HKoxnyiZoX3idekQJaINI8jraP47URyZCfc2Qw-dkMpdpcLaK4NPVvh7sDKoTndskPnp5HY5hbUuJRbkKY56ikiMr06KWEx3hAg1MuCEkUfP59gJF-1297_P5Mk0FcMM5UPHpKNj4_PjWu4JxoRvfqQ3JhrmZquvcVHU25lloLWSHJhCJv0S_Vt1FUywE4Jwu839M875ok3V3X8PMRyxaStkpL3WCxLRQLNivcpmyKQYtqs71fGnHRRsxduIneLn19gd7MzoutfahMzJKepVGLBreEhRZsOAhki352Ma_4-Q7T5b6NNToN6qHF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=iql7r3XuOqaNyJcWWeTwQ_UCef4I1EV3SUVQgSFF_q1HPBWqJuuT1QbTKJmGJ-mSrvqHwmaOfTb4UzOiE2tC-I9gG3-d7zg2OiD0YsIGEJxJbw61zro5S9vrxi5NsACYu9C-EVY97YTVgyBwL_KKe7M74PQKk-HVM-PclyGcqg3cyzkdFUkGrFXU-s0H2AyknZ2g1V1a9OqDQpfRnyuu2ShaKi43MLk3fFjWzbVXS4AZRn6TtZxWU12JfBxnSjKLF8Tpj5Xs4kgULliXE_k9GuRU3pY0AmCn2Ob4Xkt92yGAYLWKrdrtcf1CuBr3Jg1wdG-SaLcPjRNKVPNKUageqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=iql7r3XuOqaNyJcWWeTwQ_UCef4I1EV3SUVQgSFF_q1HPBWqJuuT1QbTKJmGJ-mSrvqHwmaOfTb4UzOiE2tC-I9gG3-d7zg2OiD0YsIGEJxJbw61zro5S9vrxi5NsACYu9C-EVY97YTVgyBwL_KKe7M74PQKk-HVM-PclyGcqg3cyzkdFUkGrFXU-s0H2AyknZ2g1V1a9OqDQpfRnyuu2ShaKi43MLk3fFjWzbVXS4AZRn6TtZxWU12JfBxnSjKLF8Tpj5Xs4kgULliXE_k9GuRU3pY0AmCn2Ob4Xkt92yGAYLWKrdrtcf1CuBr3Jg1wdG-SaLcPjRNKVPNKUageqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcCL47lI8O-IM36k62-A-Y2tpfvqQ-PhMaCXQELp6mzeZyRGxbu4CIfTp8gDVkBGGJTAr8z_FCe43UQnlJdOYrY3Z-pFiR-lylxGdFgETfpm9QOPl9oPXonOHBlFtv5BA58MTu_yAYDxOUY1npzEiIaqAMG6BfWKnglaF8z4stx4fHtIGQLUsxbrg8x2pNue32pjUrfcXDJ_Pb00RgJAKalJXkMhEbMSFYRh-CO0YaaT3QU-gMn3-wlUhtmfRbgQeq0nVNtR9dWyn4yUtnvcsf8OpV1dPru5IoNxGka6fUoIsVUynVgbiGBDU636Ur1bT2BsLY6zqESxZ6i3Z3VgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAtyp9RA-FTSdl_C-U2XqeCN_G6h8KnrjfxtY7pgZtPnE7xLSFBgkmKoecxF_6uqoETJUCYKJa5x5o8ymmDN3KcYGUNAbIetuvIN-MbCd0RkWF5i53NGxM6b8fcIWS4faWZmP7q3Ov7smMD8wha_ppmYXdfex3dVtUq4NR16pZKIZSJtPme1VQlHNiI3WjSgG-iSAMoq6MJOLbLXq-OhmKzPZF3CZos_TXRNCVRRvuUwqU5ZYGFW4jeAYTuPIB2ggg6keQo9eMBQ9AjJVWhFPzuuLA3hJbe75uOxlE2_HSI2dw3-v0ZB7jHSNO7WoMtl8M5EO1iz69XoAXkDTCjMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOMn7NIfQ3OU4fyWZDPhBeJBlyPDu1MjEi0URsYB0UjMRN6PYR7SaOQEZC0sKZSmD2_AVJ1uLT7AmCtvtl-UThRm-4kCwO45rFG6rEFKAHVgw3z4ijZlOzAUk68NRJANsKqxRc-6tqAFnyVBNDweqWy9FVFvY_106z2GOlc5usdfgGG9F8KfBUGMg8pTUROgfknbhaYo3MiWK5foF_o4yr8LB6NtJ804EI4vDc-zY1OPCmQVzG9KTPTdXPgRdDplcSryV5jX0alinr2GSW3aPuVhFBsYS24WIg3hQaWxorRkQ-GjdvhueeH_ACafHrHWRBZ17MRKW61UasSNIVR7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDyHlZ_U3B7eozGviGdjs0JlDJw97dv4KNysvi_ajwrL6A_h1KzvygZdvsBBPuWHhw7VKP78_X9R-MGTiPgN_y9SUt85gZi-2KmETuNlMXgz_C0BWrjJwTukDbyWlAeUX0POuux_9Q9xixDxJJKWfKMJbShzkspTeiFfZXq1Uv6Zcz7OGG5fQaeCa3hXwi-_8wlVcCAovHEosrN8fapkLfwN4hsVz6lVPemNaUpu6KXMs0oJttrJunViZKtMa6KOKhlvyNi5Ptq6f654pnZsmRLB7tICOvsXVjaT79KXOwIFfVjCwxBxJsIwkePxNZWO927uUuy8VyVhMHXqCRCeMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIrsSpiMwIL2NRdFUMHLUXqurOgflNdds0OuYInCkSFLpRtEbdAsj0CenR6iR87oNIiD3JyfegLH6qaFzOnI71JOTh-o56funnBuDkzN1yY1RAKPYH1OFKzRDM3qY5fqMe5a8QsmaOlZhqj0HsRqzl9dq4xDrlKqFoI7aKK_2b07aRivlC6nOY95glVB-ZBt1xbSKe7Tm2826xQsjsP5WmCVikjgQyq08KIbUDGR9kUbjm_XkIGtQcHcGzn6vv9Kq8bG7qi_SeJZVkYRJUosevMrd-q1Nf9iIEdrvGcL-MpSdYTiP1HuvLwV7j6TrtCfPKqjunAzDCgvuPSjzw5cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=tlIIX-_66kWdElyCeMPDLlsGUnOldRtA1ZMmc07R2PWsNefvJcZQ3JGfrBwoB13wtAQHUJXQzc696UnPJ43LLgYYgTxZDuPJnQpdW30CF6bVJXLu1n-IDN_6d8AXpZ_hFipGxYKJ3oYQsGM5CgM1GUbS8GBDaj5I4JwYuZOwVMjEQ7sCqcRZPIr-dJ4eBM9fhNa0oy3RaYZlXZL1nYOgN6fknlBKVd3dV-j2-X-QSj2lX-u641YxdlLPp0P0X4WWaoAywm-pe0jx560YjWXRmo_gsUB61TB3WsLq2eWEXF0Lrb2aREQSD9eUvyrBpjjE9yDjPCPfbmlj_dbyQRSisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=tlIIX-_66kWdElyCeMPDLlsGUnOldRtA1ZMmc07R2PWsNefvJcZQ3JGfrBwoB13wtAQHUJXQzc696UnPJ43LLgYYgTxZDuPJnQpdW30CF6bVJXLu1n-IDN_6d8AXpZ_hFipGxYKJ3oYQsGM5CgM1GUbS8GBDaj5I4JwYuZOwVMjEQ7sCqcRZPIr-dJ4eBM9fhNa0oy3RaYZlXZL1nYOgN6fknlBKVd3dV-j2-X-QSj2lX-u641YxdlLPp0P0X4WWaoAywm-pe0jx560YjWXRmo_gsUB61TB3WsLq2eWEXF0Lrb2aREQSD9eUvyrBpjjE9yDjPCPfbmlj_dbyQRSisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSD_dMdyUenZ-fH9YPyKMFOVrYfC1QuZCFZlniQ5h5jwszWQ-gbZmEDL5_gi0J1tWIt_V-qux3S3FZv41iAvLtdpQsycqB5olOlFmcwWr30QtVUC7lBTIvPCcYD-0bTUVI-AtRF0oaoVC41I6Z--I4qnOfV5v9BxfQKE3BR9YK6lwf7baNuoWx8j9q9W0_ZDX9nOShArK45VwmsCa7tB59zehUVy8N4R5Ey_P0jWrnFpwm51b4PufyORtlMSIAO4Ez4XnZKObVe1C7W3_QcJ8iC0oD2ZS7K011BDH_Y-QkuFmFg8HBdDowg9bUlDfamUXPXC-GxkkVhU-WgLnoWPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZ_Axt0ZOItFIVL7xDIfWTpVF0oJaMWOUKgdjF2WSSX8ZJaT7jkAo6Q_khb0UdMtY82jjBZxM5Z3PvtBfxG7WTJrz5Jp2GfwN3Wqzv45Jq-YSP4PSolBIKqwMza8KPj6JI2uqoX0c8eG9LjGy4Ds8fEJVCxpx96gDBs7tPk5VaODI-ju9hIfQBS5F0tlR6GeE8Jni-EAOQoGb43IqTwgPqFSncf0dwg8BHVMk4yHRqlH22Q-1wnzImPzFSLLkkzuZkX-7FDIuvmX_ttitzPNMgbOPpXD0yPStm7hf1XAQSYu3-zy6kfrCCrdOmcMjQH4ECdS_OrA9f-1uqg_fAHDbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns84KzhO1LiC6Cb1oGBYOR79hjJyVlBWhlWsYCfkuUCBR7n3JU9--m1y2DSNHgw6mjXxXuRkNL0_Z57q_Ys99OPX9KRHnjnB7F4RWkCGZp6ejIDawE1XKpAtJTcBqpn6cK9k0Pu7GOA3KCERB4Hj3sYZpuSGAaIIbRm0J75oFS2h6Ifu9ZKC8LwMBm2-1Y0ZHqKHMy2qPGU42j8xYO90vr6mPjN6nvGHKHFPbCdYMi0w-Le7BWicO1s9Gli94-C_U5eeOm8NNYQql3sZaJZ5ClhSIzlIelzOLbCwOjDiqsBpIkefJZW00flFgaDCBWy11NZaFhZWQL4-luZZQvNihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjJX9sWNax9plTg-LCKHpOZfxan6Vft4pIVtwT_1yzG5C5OGtouayJoZcSJ2UGU8YKi40zHBdyFaqkBw-YVtNrb3ci2v6s9PQeZXNLr-Aa9BRrZJzxYeB1lJpU7epM-_E-w-J4Y0XfHfX3jFr6Iky0IMO21q7i4pE52RxeHSBqh_RlbZbUSngdmucrIrbQgV9JkJVMgtxXd2-RoIpYvqMz4k_xbSqwEcNn7EbW2SLbN9-RMA9EcFOqW8Dm4P2FdSnDM8jWdcDhIgUAliP0RBsp1FccV532jWVhs8qfOFaJ9GnE6v7qQ8yoJTfwgySnNiumt-8pxwenQIkb6gbmJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVwD-azWo-1qxcN9xp0P98rSZ1FZt8eK_r7ACJ0jf8F2m24pacLJm4Q8L3Md1RUfJ0zOE9jXgGrin087CRDCha6mu-21Unxjc6GmacNctl8aM6c93CdU5PYv_LsPj-VxCg4x9YRS61PEvFW2eCh2KsQ8lGQszoVsdtYHcSII92dBCdomRTRLeB_AgKmgiAwfAZgH5kd7pZ7PHCHECoJI8bR-OW9zBFvw7AZKifDTLEdGVJTGpjj6th_gc_0Cfo5khtBe2v5NyuvW5FWLsy_BCmf7rY74kyI6Gz5zpVXL5A2S0_Bk4L05xU9CSeOfUNc42DjXJQNvK_euVgxzel72Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqdwUGYaoqJ6fPq9k0gaYv1CG1Br1YxiB2fmVtEyIuzvRlyCEZ10xUh8QJN1A1oxiCK_vmEe-VRENyTwUsiimYP6YLkWwoMl2RHCxNwazvjrfuCItst2BAGyXO0v6f4n-uHfO8mDs4hI4q1_QxmxG0aiaFFnBWPmd4jT0bQWxuH3PjaP0GMrfMq-9jb6sPRo9qQ-4CNl9UxGCcZJV4tHahegFuxBmBAZ2PURH45fE5_qXAWeGLCxzT-UIJWa9XsB_dVDoIOoG9ucXvoKDV6PE7qrIKlH3xYmIEXkjak52i4WfEL9znfZDwx-XaTsB-bWr1QMlH9MYYiHDh2ztQn3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=Qlgh-mEjc9y13ROdkkSzaQ0JZnSXIj_WtlKyKvfyOTvXZutSSMqP8ARJGL36_nGJX98Aon5GOjxG9VLuczEWwDIzfNb8Ma0K6Wuks9KUlBvVxAUpjjITLMaa_QRxDJnc6NIm-iwQfZkyN2gWkLgHjJgI_9BMSwJrR6IWruddyTPpp0QK8ukZkOj6-kVIPZ7kRgHRMALlo3z5CE8cBWxo3Jxg3vehTOYq0ar_fk9qswBjBrhixg_U1urQdV6M_1S2cKATUO3S9lSt-GOm2jXPxcvKN3bTMSX2xktihgcJUYQEpK0M0rQ2-cVeGCNeaUL1WlStJk5WzaCwibBXsyjQeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=Qlgh-mEjc9y13ROdkkSzaQ0JZnSXIj_WtlKyKvfyOTvXZutSSMqP8ARJGL36_nGJX98Aon5GOjxG9VLuczEWwDIzfNb8Ma0K6Wuks9KUlBvVxAUpjjITLMaa_QRxDJnc6NIm-iwQfZkyN2gWkLgHjJgI_9BMSwJrR6IWruddyTPpp0QK8ukZkOj6-kVIPZ7kRgHRMALlo3z5CE8cBWxo3Jxg3vehTOYq0ar_fk9qswBjBrhixg_U1urQdV6M_1S2cKATUO3S9lSt-GOm2jXPxcvKN3bTMSX2xktihgcJUYQEpK0M0rQ2-cVeGCNeaUL1WlStJk5WzaCwibBXsyjQeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=vHOAESC8q1Vsp2F3CHaSXo2TZb4PHFOmlFMd8DwNQevnS44BChHow6GcaCug2PBA2BYWLNWwbXxSdDt3HRZPPM-o2a6r_k0HJqrYgNm-rdYYDD0V6uUEbgoLLZNJjduZmnTnHyjO5HmuD6KS5qpZ3PdS-DC-bAKYx333hj1AWLDcMZwVucOGNdc3F3ORAVsvWg5ST7VPsANvEjq0nBM5kmx8MZedJqS0IpvPSY0unLBo7yqPQhEXw6GVghlZsbrGL1IRDK_dZNxaz-li8H4KF7s4nOQtpkXgQvagN4CDt-Am0CQEFSEaJYn3u0nUqgwDUht7Ix0Zziy1Vn3TLqI4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=vHOAESC8q1Vsp2F3CHaSXo2TZb4PHFOmlFMd8DwNQevnS44BChHow6GcaCug2PBA2BYWLNWwbXxSdDt3HRZPPM-o2a6r_k0HJqrYgNm-rdYYDD0V6uUEbgoLLZNJjduZmnTnHyjO5HmuD6KS5qpZ3PdS-DC-bAKYx333hj1AWLDcMZwVucOGNdc3F3ORAVsvWg5ST7VPsANvEjq0nBM5kmx8MZedJqS0IpvPSY0unLBo7yqPQhEXw6GVghlZsbrGL1IRDK_dZNxaz-li8H4KF7s4nOQtpkXgQvagN4CDt-Am0CQEFSEaJYn3u0nUqgwDUht7Ix0Zziy1Vn3TLqI4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=NvL9kadwQbjNqgudJtveyrWjS2jQAv87pe8Xghmv5UOcwwgeNCCHqC3hRs6u6TA1aXZPLChidZ16o1D-d6YqUr0AGZsxr5rvgwuCS51AWEVDxJjUgPMWw_VE7vxg2tfILQm1fSpffHv2qdwKhy9MFXneGEw38y_bgd5_mzEoVoJ0dFmt33FwJP2BHhktv8-Hy7s-rLAktaohpyyDTX62E5zUho7flpZHiASgZFiNp1i2BlecC3wk6No3FhQOZpyHIt3mri3IFaS25oDr4InIRs-xo3m8b4EendCmqdpgjy49qhbIC0OB8TW-Gso5Fjgf-uStK7BT0_v0UR73m0m9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=NvL9kadwQbjNqgudJtveyrWjS2jQAv87pe8Xghmv5UOcwwgeNCCHqC3hRs6u6TA1aXZPLChidZ16o1D-d6YqUr0AGZsxr5rvgwuCS51AWEVDxJjUgPMWw_VE7vxg2tfILQm1fSpffHv2qdwKhy9MFXneGEw38y_bgd5_mzEoVoJ0dFmt33FwJP2BHhktv8-Hy7s-rLAktaohpyyDTX62E5zUho7flpZHiASgZFiNp1i2BlecC3wk6No3FhQOZpyHIt3mri3IFaS25oDr4InIRs-xo3m8b4EendCmqdpgjy49qhbIC0OB8TW-Gso5Fjgf-uStK7BT0_v0UR73m0m9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSIKVhbr9kj1ruGcmijgy8XB22gT4v8vCJswgDKz3hvR4Q3iy22mx2UWZPqOvJSDB7yteGoQog0OEy-XoJIB3sMfmE_o2SeCCSeOQ_X1x_HOAwjzp_w1La94c6rrYYcrudvF9iWw8wdOBF1_UNGkch2yKyxaZ3n1vDr3sO66ui6nrxmkvidJkoiwJDJTw_rQfs8wajCjw4CmqQ18_w7KA_kb7nW9Dtt51LqzmGpgi_ArI5Fks8mJx1u-eDjBWxFDhbKicUtoto5gYRrmGRKjoNdLvPI0Mnu-LHLrcW1xVU4qbyQfG0PgnG6c_CxdtM0mTXFgD8RoOD4FRS9bZ1kt-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=b-RFWOXuBqVZO0-ZLkbEnSNJ-_uen0cg9bgTkNso_olhqqpKvdiOPCT23vzTNJ_yX5dZQdn7pFfxZ4OHUAbWkZS38zGhMsqJVVL04LeGaSHsLyFhWqdi8Sfj5__LJk1FNxyIY5EWYfomam-EtqjfDyRzW9eGXfaZBgqgCitET24Fm7tUVBtwe2nOQiM9Twp9KQyjRG_bhi5wy5fyO5SRuWGstbOSwr9w13EFOfe3yqdaJkgX3DK8AYqX25QxERv6gN5J8E9FSBuEy1tEN_CoZq6ogJAzR-zKm_TpbWvdjehLx7pCJzgXD6UdH7PA1EXOMjJCdCK8WQip8rjX7JKNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=b-RFWOXuBqVZO0-ZLkbEnSNJ-_uen0cg9bgTkNso_olhqqpKvdiOPCT23vzTNJ_yX5dZQdn7pFfxZ4OHUAbWkZS38zGhMsqJVVL04LeGaSHsLyFhWqdi8Sfj5__LJk1FNxyIY5EWYfomam-EtqjfDyRzW9eGXfaZBgqgCitET24Fm7tUVBtwe2nOQiM9Twp9KQyjRG_bhi5wy5fyO5SRuWGstbOSwr9w13EFOfe3yqdaJkgX3DK8AYqX25QxERv6gN5J8E9FSBuEy1tEN_CoZq6ogJAzR-zKm_TpbWvdjehLx7pCJzgXD6UdH7PA1EXOMjJCdCK8WQip8rjX7JKNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=ulKH9CZxrSKxhmrOkhwnsccMHUISkgzoTtq6qBvllTugnVcku3gEG9EjAMQpKSc8zy8SPn365k-AiAmh_3J3_ixMI615pWJkAgZkFvlF1cDJjR7nvvmhBLz5v7GXIbKx5kR4ShiwnSKehIFxusPAYAt2Yrc3N7HfL19t4tgopo0OlEN6WuUcAEHHAENDX_dxAhUB4MBLqLkSiz_r4YlpMz0Gwt2MhmeUsizoruDnmT5mssSSYwnwZ_L8jeSXG-USpHCqjtfiNQz_EeWwDCeM_PnCQCG-CODRHSjaJlgqQQ13wuo2CXSFuZwg-cWxBX0N2MIyrwnCJ4gMi51eaPiogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=ulKH9CZxrSKxhmrOkhwnsccMHUISkgzoTtq6qBvllTugnVcku3gEG9EjAMQpKSc8zy8SPn365k-AiAmh_3J3_ixMI615pWJkAgZkFvlF1cDJjR7nvvmhBLz5v7GXIbKx5kR4ShiwnSKehIFxusPAYAt2Yrc3N7HfL19t4tgopo0OlEN6WuUcAEHHAENDX_dxAhUB4MBLqLkSiz_r4YlpMz0Gwt2MhmeUsizoruDnmT5mssSSYwnwZ_L8jeSXG-USpHCqjtfiNQz_EeWwDCeM_PnCQCG-CODRHSjaJlgqQQ13wuo2CXSFuZwg-cWxBX0N2MIyrwnCJ4gMi51eaPiogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=WXaau5-njJFnIxJDtFg2kXu-9gwEe3To1rK2W4Cbh1g09aHYEupYsrF4vJNnzh1tDSsJUp6-uwI3vyVkL21sVXramjfFAuxMoHDoKSQ_Ktrz765InTfbLllb6nFYkf3DqnVdmjDP7k5psh3dsKuKUuKF4dy-QBUJOJsmzOCPB7iPQKASqPUK_aU5m4MEqU9PRxob4Ngqu8JaVYnIRUrA5ThCXfEQMActFwPaOirILWA-9jWouQsD5HJIL3ALu5ysKFMQv6XLGEnKwtbHesyY3Mvha6AvSq9gXR60FjbY8YrdUkpN6vWCobyEn0Ug8dGUUwZqnlRJZEHsUn-mg0Rp2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=WXaau5-njJFnIxJDtFg2kXu-9gwEe3To1rK2W4Cbh1g09aHYEupYsrF4vJNnzh1tDSsJUp6-uwI3vyVkL21sVXramjfFAuxMoHDoKSQ_Ktrz765InTfbLllb6nFYkf3DqnVdmjDP7k5psh3dsKuKUuKF4dy-QBUJOJsmzOCPB7iPQKASqPUK_aU5m4MEqU9PRxob4Ngqu8JaVYnIRUrA5ThCXfEQMActFwPaOirILWA-9jWouQsD5HJIL3ALu5ysKFMQv6XLGEnKwtbHesyY3Mvha6AvSq9gXR60FjbY8YrdUkpN6vWCobyEn0Ug8dGUUwZqnlRJZEHsUn-mg0Rp2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=K0pKFbxSpvOZMzysa9TmQg9Zpt_tIkB6CvaL2uHhVyu2DaQ0RJxbEO2-9LssPfsNTpx8x8e3xFsCJWwYkJjmJWkvK-DuPpKW19nuI_jJD1ZsSlw0JVPI34Q6k6O7hQ_4AHEfTt-YiP6-fg2zetohJm36Ih8sNnJKazB24yQTH-2grQ_n5UO9DIQYtZirlR5Ml-m6LFQik9qoPXy8COboVFgKFrEko5CC2wwBmE1MDFiStUM142yBy1TvGjB7gDDnjr_CmoLkR4AK3h83zOG3Yi-lVPoQuezRxfAbxRiBUnrFwbXRbRuWaSjnCEm7_C2i4mrUfjWAkUdH1qUI0diTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=K0pKFbxSpvOZMzysa9TmQg9Zpt_tIkB6CvaL2uHhVyu2DaQ0RJxbEO2-9LssPfsNTpx8x8e3xFsCJWwYkJjmJWkvK-DuPpKW19nuI_jJD1ZsSlw0JVPI34Q6k6O7hQ_4AHEfTt-YiP6-fg2zetohJm36Ih8sNnJKazB24yQTH-2grQ_n5UO9DIQYtZirlR5Ml-m6LFQik9qoPXy8COboVFgKFrEko5CC2wwBmE1MDFiStUM142yBy1TvGjB7gDDnjr_CmoLkR4AK3h83zOG3Yi-lVPoQuezRxfAbxRiBUnrFwbXRbRuWaSjnCEm7_C2i4mrUfjWAkUdH1qUI0diTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWM6kQm1XxQmgsF9NKxNa5Yb6Low0BKVuXWPCN9ZUcplMOiVKg6x8o4HwXvcYLiJlmx8uPmKQicLhAQ0ByRdWiOu_xwG-dGppX-TRToSm5uzOm0e54uxhtKrcIevYLoboFI1hwdOuSXPHwkxFOT5Hy_z2iqjmF_GCvE9NDZhiweqkaKC63ouYxkDiuiVkk3LY5E-ar4WxqbklqqootQ6uRoYtkxbXP7-5FLFEaPyMTX9FAF4scVBRFJXKhUIDMOX0YHlEw_PSj8UO7LXum46zSRPc_sIXV6UMr2vOpyZUcq7GxOMfBiOKwPQg_hBp60wcRSC_TYmjcV1Xay2UlxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnQsi6c5jS-0GfpjNFoG_V2JlCb4lgDmzRPXYs0RKhIwABtm4MTOpw36C0sSf_1Wc6BWp7PBl1eOhA4BE6OceryVSaJQjJn8gFrJGHV7iszvYMIlvS7MH9TH0wyEj-EEcRPE146EpX0XFeFr2pcGavE7HD4aSjWGdddGDQI4iGRhBon0foCWb9A-K1VLYjdAbOZzMabGPNQbs3_5j-VeGz3Xf5kX7iKGIqJjI_xMtpk0ECeTscWjr71zjQ-u599UwuLXTtMKXABAUiHoqsOQ-j77nV-neiEyEiOE18SrMl6qhv9esP8DVyMXCETKqOS1TtKYoqNpcVguGyIuHlt1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjnci2vnGnpj2RePfuxKgvthMrZaJviMhiDQbvi0ruWEknv52G9ltcFKCYUaPHic2ijNiO3IDyeO5mb2nIilsdl5fSaUpO4tW5YOVtB84LwzuOxThTI0WqzDjXgpGqus_PsnRBb6ROmuPWbo-VPiZXF4QWChC8M73wW7obbN8oab-jOt395UI6xb9otjYyzLngM46wIFGaltGL8l0__FNAq7MGIHQmexLh4UH515ysKnirkUnwNlh61mkmqWIbpSmP1p_QvDlvb0NlpTa9GmNIwQ95ghRmaful7r3XDRxMT_XykUg9UQU78lD-PKLG_TzuelKaKGPS0XlC3PuRMZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PZC_Ulqs1ZU23af-x6mpZFR-EB1ZDWljzVAWoz9Q9AzGMUGKRGiMjgKwC9J_dsKQcPiV8iLEOJOjHi0oalWhFVe6sKqQiMUrS7RNQ-ZS3dxBAQ5qYwnTwZzqg7nzWHQ8sdb7DNSb4xwszoaAOEUmBBsV9DcWx5i_BBbU3LnibF4DxmQhiMO9zdISfeAlaczLxBtO751g3qgrYTCp0-0HMUY2hat0ym2ffdQlk1WIoQjFQkKnNyXhqQemhthUBNVD7XdiGHzmj6NMfB044ax7AUzUcTq4yNLaIGtZRS8slYEfbgmPPu4Rh41h8xKMwjy-MgAnE5G8TxnWtlZy4YX72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
