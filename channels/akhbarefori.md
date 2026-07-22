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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
<hr>

<div class="tg-post" id="msg-674319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/674319" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
🔹
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/674318" target="_blank">📅 01:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند
/ فارس
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/674317" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک خاتم الانبیاء: کارکنان پدافند مردانه ایستادند تا ایران استوار بماند
🔹
جمهوری اسلامی ایران امروز با منفورترین جنایتکاران عالم روبه‌رو است؛ دشمنانی که هیچ‌گونه پایبندی به اصول انسانی، اخلاقی و حقوق بین‌الملل ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/674316" target="_blank">📅 00:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
جنگنده‌های نیروی هوایی ارتش جمهوری اسلامی ایران بر فراز آسمان تهران به پرواز درآمدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/674315" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674314">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/674314" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674313">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/674313" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674312">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0ipRLQgECld7ylbS1TH1sxULs8HX7HIVDDvs_o1SXnIiNynF7YtbShvrSisLFmJSAieJVN9GrYW7BvphTtAL50n6CnUQLjas3Bn_14KmdbVyQ-UMS5CQWZNEQNurvkgtsWnk3PZQMtgEAR4DjNrkS0YHfQx8PkNQvu7vPVxpFNriw9mveiyj5aMZhKIl-pNcelBavmw84jtd_RRAu0wIBc2TXug7d_2TzYOEL426EQtSYl9AHt0toqXAbcObz9TwAr9ygw3Yyl_ajQhv9q7B3yCqMAK_OFiLK2EpV0kfeDBon1LHZC1q6N3ERgbFSKnoK0LO--YL-ys2HE03H8zQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره: منابعی در ایران می‌گویند پرونده کوه کلنگ (کوه تبر)، طبق روایت اسرائیل و موساد درباره این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن مدیریت می‌شود
🔹
برخی منابع نیز می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/674312" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674311">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/674311" target="_blank">📅 00:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674310">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پاکستان انصارالله یمن را تهدید کرد
🔹
پاکستان به جنبش انصارالله یمن هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/674310" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674309">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674309" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674308">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
🔹
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/674308" target="_blank">📅 00:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674307">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای سنتکام: تنگه هرمز همچنان باز است
🔹
فرماندهی مرکزی آمریکا (سنتکام) مدعی شد که تنگه هرمز همچنان باز است و کشتی‌های تجاری با حمایت نظامی آمریکا به عبور از آن ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/674307" target="_blank">📅 00:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674306">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزارت خارجه انگلیس اعلام‌کرد که دیپلمات‌های این کشور موقتا از ایران خارج شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674306" target="_blank">📅 00:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674305">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔹
این اقدام پس از تشدید دوباره جنگ علیه ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/674305" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674304">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آمریکا و عربستان توافق هسته‌ای امضا کردند
🔹
وزارت انرژی آمریکا گزارش داد که آمریکا و عربستان سعودی، یک توافقنامه همکاری هسته‌ای و همچنین یک توافقنامه تضمین‌های دوجانبه امضا کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/674304" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674303">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی زائران اربعین در میسان در جنوب عراق به سمت کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/674303" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674302">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بیانیه نیروهای مسلح یمن در ساعات آینده
🔹
رسانه‌های یمنی خبر دادند که سرتیپ یحیی سریع سخنگوی نیروهای مسلح  این کشور به زودی بیانیه مهمی درباره انجام یک عملیات ویژه را اعلام خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/674302" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674301">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
۶۰ لیتر سهمیه بنزین مرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری در کارت‌های هوشمند سوخت شخصی شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674301" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674300">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده تد لیو، سفیر آمریکا در سازمان ملل، مایک والتز را درباره جنگ با ایران به چالش کشید
🔹
شما حتی نمی‌دانید در این جنگ با ایران چند نظامی آمریکایی زخمی شدند. واقعاً باید از خودتان خجالت بکشید که حتی ابتدایی‌ترین واقعیت‌ها را هم نمی‌دانید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/674300" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674299">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW4wiRDUO6pJpfiGOHoAxHAamb-c4W33vA33RGx2Z34PGuL4bSHU9nFaH7hlZKo8bRmDtxuVAainan39yWqS4ZWtyi1vWz74xt3k0GsFdSW7GX_sVboS4cDp5df4-d_1FCWM2PVLjsosfoovRpY9JpO93oz4TVITDEnECZvhKujUVzFz8shuuFxTkx_9nOUTC2mLKUvYiYGbe2_xvJGKVyOVNoMJGI7hggwpSVwsC7EbQNdpcstzqrgZGHqqRWRvaiihrVXnIYNHawyAFD8_0yxvdfDz_Idji1NTAGgQkHQZQ27JnfaXE-yarTlQLmEe2QZ3X2U1mHe1gT2SV2hdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/674299" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674298">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMzs3sV83G7tmUODt4BzoidHJfwiwmdpV0FndA1vHHj46MpPUkfFqJHmSVQzTzfW_VViaB4naezy6c0utYdqDMNj9FpqGFW5DjQ6qF8warSdaseuEg1-FheRptm9q-avO_IWgGYwMa5YCUW3-EZ-_lb1Dwrs7NRri7Wu0UUWLuVThoK9e6pDdIIBtePRxHcht0fFL2IHWCe4FwcVCEwuVi4XiOqjAtLXEpG8kkFh6VDsqxUSElxXlCRZ2dkd4X2i9L0iocIipQ9B8lvwqLqfL74y4Mr1JDJupORRHeC04-oxVIt22fQULIiHRoqHrYtT-wSCC6aeTjy4UlmYwfGFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خبر منتظر نمی‌ماند
با کانال خبری ما، تازه‌ترین اخبار و تحولات را سریع، دقیق و بی‌واسطه دنبال کنید.
📲
عضو شوید و کانال را با دیگران به اشتراک بگذارید.
@Parstimesnewsiran</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/674298" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unYgsAD2cPuBmpj8Cstb4pQTBlQBLPMB3RV_rgr1iNebLdhvTRoUZ0-Ne_Nkr54c1z2mqDqDQM2flQ8CLNiCZTNUqeCviKbdLH1eVY1ZfVuZRVjCTHT6cCeCe9k4ILv5oSjoRCFLrWUl6mp9ylN_O3qHaxsruqobPwZvPFr02vb4VEnQyBE6DcRUxBaci0HTt147LM-UZHHaMHEIeURlIwqeyozZwWVPGs1KejaR2y6DG7OvMUoV0m5mj3Ne6NP77imS2Y6zKkbglJ_K8L9p9i9RkriswTgnGdaawOZbzoXwkvYhLzN_h52tIgN3FmRQDRFQTTnL4h7Zq6Z28msLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مگاتخفیف
سوپرمارکت
۴۵دقیقه‌ای دیجی‌کالا
شروع شد!
🔥
🎁
کد تخفیف
۵۰۰ هزار تومانی
➗
تا۷۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
🫂
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
6TFG
🫂
۳۰۰ هزارتومان ویژه کاربران قدیمی
(۳ کد ۱۰۰ تومانی):
GD33
فقط امروز
⏰
بزن بریم خرید سر ماه در دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/674296" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afp7JiGwtbAHfQOMyco9Y2ATQ2CeJSIQf2CWtBwQlqZJdqHOFFUBsXdp3_rA5Ix6KiDVxl4VxN2J25TCJ2imcJQGakr_eRVi42ESwrqGkueCtQDyNVx9Ly-CISwYXWvEBPQdpi6x14VX2dfCTw-gCcLUPpNvRxm_Nr_oJmaIRlCAqxvpeTIbChFYNzYCI-2htuWll2ddn6d_EvlKJuwVhPrCJZHpBD2qCwTXSeMflpEh7iRu0WpMQvecFkHawR93R5_AlrzMJ29CEJFn4Id_5jBaM6RFkMtICHlg718C4K8cI-qUSNNz7DX3sNogWT7LxWkcLwZ-YhlvsCdtBKlCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/674295" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن رقص شیطان زرد پایگاه نظامی است
ترامپ متوهم
:
🔹
ما در حال ساخت یک تأسیسات نظامی عظیم در کاخ سفید هستیم. این یک سالن رقص است، اما همچنین یک تأسیسات نظامی بزرگ، یک پایگاه پهپاد در بالا و چیزهای عظیمی در زیر آن است... این یک پروژه باورنکردنی است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/674294" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما به همین ترتیب در جمهوری اسلامی ایران در حال پیروزی هستیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/674293" target="_blank">📅 23:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه امنیتی در مرز لبنان و فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/674292" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbGeFA7ey6Mibc5JcyMQcvPHFbp_tZ5wT_ibCYZVFHQSRiXj4mBbF9W_NYAlMftb9qZe9athbZT_xDiSg2439-dRrOQUh-EaZ5Dob2IvlxnU9eTvVqSiGhJYAR8-R6fZYpTStgh-AIHUcIyOc7Ob_vix-zpsH0RS4zRfYEeCaOW0QwD_IaGNF1ESQpBG4tatVAawEJ5QEg7imal59_oHw_RzF48x5BZ4Dgz6XLBBHxZx1cHJpzxkoxuZaWb1wVMMsF8HSOlTefHx1hCyTX5LtMqISlkCVEyUQZYTSrd4iz-zFsUDj2bazlqydmG76hQNpJVUaXADpLveuasBajSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه انگلیس اعلام‌کرد که دیپلمات‌های این کشور موقتا از ایران خارج شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/674291" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
🔹
رئیس ستاد کل نیروهای مسلح یمن در پیامی ضمن تبریک انتخاب خلیل الحیه به ریاست حماس، تصریح کرد که اگر دشمن اسرائیلی بار دیگر برای آغاز جنگ علیه نوار غزه اقدام کند، یمن آمادگی کامل دارد که فوراً به تشدید عملیات نظامی بازگردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/674290" target="_blank">📅 23:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKtIA7vbYwuuFryng_X5m6ebghx85hBQN2RKQSqsq5dVxypTWqNikItckcnEG9BfYJhNi59Ojzl0JpoB6PBF4QRTVPbuN-kLNfMBql15XXA7_dmsNAUkNlZ-jeSu5IqqXewC2e_HBj0AgvnXdPttojW2ZsRSxxOhZvcXx93QBrufE3ffrJloG3QOhOZq7FPXNH517pweMvY_vVk1OMUBQI7287JZ3uDAVUZYmI7OqkrJ0alTNDkgqvaAeKrdBDyXluyB5_WNGty6pRanQpJK-HPmE9k_YqhPAxWcssF3LbFkcEIRj1TQFcXHbvBIGYBiBogd4USI5ccJGp5sQEQv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار موسوی: به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک کشان، قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/674289" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhOkNx91--RmLInCBA0jemJjJpUvzB0ldT5pLJctO3MzkmJkON7mVq4FgP03uXNNdHEgqCI2-TeR-Q19iBAIdWGS1_lwfDyCp1pGl6fZuCB4SR4kFKl60qRUhfdD5tKQYb31lf0GepNGFekI4C638p1-OquUtSYesWY03I8tcni710AtZcWklbPWamiXV2Xs61XcIFwlTm06SBD4nkagCHqSKaAmrNJPYH733x9SQICTi634W-RSzkBoxWvMr5nccVdS71KWilxiCkR2LtC64hOgD8RbywaKzp61LrGTAst4MAd6e25cX5Zh_u5nXiQZ6Cgyy1jaA_4Tgi3Az7dqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: جنون آمریکا را با غافلگیری در فناوری‌های تهاجمی پاسخ می‌دهیم
🔹
هرگونه تعدی به زیرساخت‌های ایران، در قیمت انرژی ایالت‌هایتان تاثیر تصاعدی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/674288" target="_blank">📅 23:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674287">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سفر مخفیانه رئیس جدید موساد به آمریکا درباره ایران
🔹
رسانه آمریکایی صهیونیستی آکسیوس روز چهارشنبه گزارش داد که رئیس جدید آژانس جاسوسی اسرائیل دو هفته پیش برای گفت‌وگو درباره جنگ علیه ایران به واشنگتن سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/674287" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674286">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
با امضای تفاهم نامه حمل و نقل شهری، شمارش معکوس مطالبه گری آن روشن شد
🔹
نصرتی معاون عمران وزیر کشور در مراسم امضای تفاهمنامه همکاری در زمینه تامین و توسعه ناوگان حمل و نقل عمومی شهری کشور: در راستای این تفاهم نامه ۱۸۴ خودروی نردبان آتش نشانی، ۱۷۴ آمبولانس امدادی و هزار دست لباس امداد و نجات در حوزه ایمنی تامین خواهد شد.
🔹
در قرار داد اصلی مقرر شد که چهار هزار اتوبوس در دو فاز ساخته و تحویل شود که فاز نخست آن یک برنامه زمانی چهارماهه برای ساخت ۲ هزار دستگاه اتوبوس است و همچنین با همراهی وزارت نفت و بر اساس تأکیدات رئیس‌ جمهور و وزیر کشور، قرارداد خرید این تعداد اتوبوس و تعدادی واگن قطار برای ۹ کلانشهر کشور که با کمبود واگن روبرو هستند، به ارزش ۲.۵ میلیارد دلار وارد مرحله اجرا شده است.
🔹
رسانه ها یکماه بعد، از میزان پیشرفت توسعه ناوگان حمل و نقل از ما دولتی ها سوال کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/674286" target="_blank">📅 23:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674285">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع خبری از اصابت یک فروند پهپاد به پایگاه موفق السلطی اردن (مقر تروریست‌های آمریکایی)  گزارش می‌دهن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/674285" target="_blank">📅 23:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای شیطان زرد: من [جنگ با ایران] را یک درگیری محدود می‌نامم
🔹
ما با جمهوری اسلامی ایران یک درگیری محدود داریم.
🔹
آن‌ها می‌خواهند به توافق برسند، اما من می‌گویم که آن‌ها برای توافق آماده نیستند.
🔹
آن‌ها برای توافق آماده نیستند. خیلی زود آماده خواهند شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/674284" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tObVzKsD-NdhoFB94TOijRg4tdKvmV2xzT_eAtrPo5LQi2oOPt14u78YnkBLhyfLTqOvA5tkBOsni44i07hGYgJoU5C8fyecqn1r7PaIL7bQRNIYmdw-Pp1m5llHydvX3ZUCHb9590WHarDrc_5GUf_3kmsfEph1sPVqaP_jcm3T-ctZq8U7axulnml-0wlH-vQQJJ-YJ2kOlmRmhKn7eoetZVOrcifTuPsjjRZkprWP4oro2O4ipAw_pDTmPgaIabHqthPMi0oGO1NplEVieX6uZiJ6FgOcvLZK9xvDnNR_9T_0CtMtbEMBl28sKy7abB5cC5rrShqFeyY_oud5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تازه بریتانیا به شهروندانش در غرب آسیا؛ آماده اختلال در پروازها باشید
دولت بریتانیا:
🔹
از شهروندان بریتانیایی که در حال حاضر در غرب آسیا حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشند
🔹
در جنگ قبلی ایران، بریتانیا، ۱۵ ساعت قبل از جنگ این هشدار را داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/674283" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع محلی: ایران مواضع نظامیان آمریکایی در شرق اردن را هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/674282" target="_blank">📅 23:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال ماریو نوفل از جو کنت، رئیس مرکز ملی مبارزه با تروریسم آمریکا که در اعتراض به جنگ نظامی با ایران استعفا داده بود: آیا از گستردگی مراسم تشییع‌ها در ایران شگفت‌زده شدید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/674281" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ترامپ به سنتکام دستور داد دروازه‌های جهنم را به روی ایران باز کند
👇
khabarfoori.com/fa/tiny/news-3232437
🔹
پشت پرده اظهارنظر جنجالی هگست درباره یک بمب مرموز
👇
khabarfoori.com/fa/tiny/news-3232388
🔹
قالیباف به ترامپ: اگر ما نفت نفروشیم، کسی در منطقه نفت نخواهد فروخت
👇
khabarfoori.com/fa/tiny/news-3232438
🔹
یک چپِ دیگر رسوا شد | جنجال تصاویر تفریحات لوکس خانم وزیر در هتل لاکچری
khabarfoori.com/fa/tiny/news-3232133
🔹
عکس شکیرا بدون آرایش و با موی بسته
👇
khabarfoori.com/fa/tiny/news-3232381
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/674280" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH7K6UehmwT8nfKNwYRb2i-O5TWHcmQu0L68pN63gUZ2LZJCOM2h3KClTew0PZX5A3lGP_lZ-3tdHPQibKkJJUL6bNgYfmeRSFDJQzyEKQXgm67H6K-_GU8BSp2R-jbxf6XSpXNERFer68cTWnEgBz7AdEvu3JibIfdwwFv8j9UH12_njWFARPezZOPpWIHIVOK2FOZqQTt8eQ-DK4bjn1X_jsk3uO9SKlNpZO2xMt7A3-Y2hoH9kQB8zc32fmZNaUcFrGGNHXQhEhTizFRmWK-s4YoHrFHCsA49OkuHuMQ9F1Ggw8xWDUvyDgqBoh0gKlwlreefh7x9pZ6eZXNodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪🏻
راپیدو ۱۸۰ NMX؛ از جذاب‌ترین گزینه‌های نیکران‌موتور در کلاس اسکوتر
🔹
۱۷۵ سی‌سی
🔹
تک‌سیلندر، ۴زمانه، ۴ سوپاپ
🔹
سواری نرم
🔹
هندلینگ عالی
💬
برای مشاهده قیمت و سایر مشخصات موتورسیکلت ۱۸۰ NMX، روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/nda</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/674279" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPSRx2k-gFrh3a4EBwc41YfvILfbS3Gt292LeFYrmMsvgTG9ouhUCoCzoTFnuONDENRWvKwacr69AzVZ-fImg4mjGiQMhoS9gL9icJynO1_8-J-gg_Nu66T6rqUW8CAwcMfYu58DzoBrUdHtyv-VQ0BNJVrxzbGO-SbNvrBcCZH8y2ikc0gCiV4xRW3x0sGx2Gd3rlREA-No1DkGl7O_iR-I00LgEq5c3y5pfnLjKsU8zHao5iCPYlXkRjkWk0UDhcfQMnzNaQSREsQWrGiPBX61PV75db7CeGYQ41Z6oUNtMsZmpKNz71isO88Gd51BADJ0wTN8mpgqPBJrqfj_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ننگ بر آنکه خواسته، شمر به ما کمک کند…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/674278" target="_blank">📅 23:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
انفجارهای کنترل‌شده در محور دامغان ـ چشمه‌علی برای پایداری صخره‌ها
اداره‌کل راهداری و حمل و نقل جاده‌ای سمنان:
🔹
به منظور پیشگیری از وقوع هرگونه حادثه ناگوار و جلوگیری از ریزش احتمالی توده‌های سنگی در محور دامغان به چشمه علی، محدوده بعد پل آستانه، عملیات «انفجار کنترل‌شده و برنامه‌ریزی‌شده» جهت پایداری صخره‌ها و ارتقای سطح ایمنی محور در دستور کار قرار دارد.
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/674277" target="_blank">📅 23:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1097566db.mp4?token=pJ-aiXEHQGjbRfsUPwxu-2pSqknNIcdhQnJNEv6e5OPzmP8QX2yFPQGGBJLQY7N8S57AhOwfGmOwECWqVD1Inu9X9AWzOLy6MuQih774pL5cxn61Gp1_9z9SM6DHUSMam0x8pw7jKxrxdchP6VN2kLJS2FNUsZyAhSnXRJrmu0MUa2JdKAycKjZ_FIFUdcAwJEpDVRz8xwxUpC5KiSBlUeP1Zt5IPPmAAWkt9qO0krCSL2-IIwgQ-O9VS4zdSN1_uQ3BgCBMEET7iDH2gmtnvPeAZtfPEadJKjcJY_wbtlpH1_J4FQv5dypbwGvmZf51mVInrNcUAnmeCzCuZNztuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1097566db.mp4?token=pJ-aiXEHQGjbRfsUPwxu-2pSqknNIcdhQnJNEv6e5OPzmP8QX2yFPQGGBJLQY7N8S57AhOwfGmOwECWqVD1Inu9X9AWzOLy6MuQih774pL5cxn61Gp1_9z9SM6DHUSMam0x8pw7jKxrxdchP6VN2kLJS2FNUsZyAhSnXRJrmu0MUa2JdKAycKjZ_FIFUdcAwJEpDVRz8xwxUpC5KiSBlUeP1Zt5IPPmAAWkt9qO0krCSL2-IIwgQ-O9VS4zdSN1_uQ3BgCBMEET7iDH2gmtnvPeAZtfPEadJKjcJY_wbtlpH1_J4FQv5dypbwGvmZf51mVInrNcUAnmeCzCuZNztuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما به هیچ‌چیزی نیاز نداریم
🔹
ما به تنگهٔ هرمز نیازی نداریم، اما کاری که می‌کنیم به خاطر این است که چاره‌ای جز انجام آن نداریم.
🔹
نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/674276" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674275">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تناقض گویی دوباره شیطان زرد: به تنگه‌ها نیاز نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/674275" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674274">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9c789150.mp4?token=QJVPS-0JuPLOhfpXkQrGQCHEASKrn8JLkBLybmIIp1bQmSDN5o9KqpH1InOJiwGK687mKUMhkz2IvT5g6xlMiQQOgRvx7F1F66hC3wwW8Y8RrrWEsY2jq0JObUuxgNB_h5qrqVwqGkqDRM4sCxwGw68v4NECdqKUzQjvcYHym5KyUT-FbSGEu8l3-MHot2aiDTZpkSmR_Q5GhwrXnAXbMM1ahA-TLJgwB5E_4peTxafesIwOWlKFr9_e1glbqlRGXIh8ujiKZanjx3XDv1yq0d7ndOdKTukmxCyQTNwGFw_zR3Heaif8UpVVm40aG-X3y5vQIXEWcTp4TNAJhWJEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9c789150.mp4?token=QJVPS-0JuPLOhfpXkQrGQCHEASKrn8JLkBLybmIIp1bQmSDN5o9KqpH1InOJiwGK687mKUMhkz2IvT5g6xlMiQQOgRvx7F1F66hC3wwW8Y8RrrWEsY2jq0JObUuxgNB_h5qrqVwqGkqDRM4sCxwGw68v4NECdqKUzQjvcYHym5KyUT-FbSGEu8l3-MHot2aiDTZpkSmR_Q5GhwrXnAXbMM1ahA-TLJgwB5E_4peTxafesIwOWlKFr9_e1glbqlRGXIh8ujiKZanjx3XDv1yq0d7ndOdKTukmxCyQTNwGFw_zR3Heaif8UpVVm40aG-X3y5vQIXEWcTp4TNAJhWJEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی: ایران مواضع نظامیان آمریکایی در شرق اردن را هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/674274" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رایزنی دیپلمات‌های پاکستان، عربستان و چین در تهران
🔹
سفرای پاکستان، عربستان و چین در جمهوری اسلامی ایران در محل سفارت اسلام‌آباد در تهران دیدار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/674273" target="_blank">📅 23:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حمله پهپادی و موشکی به مواضع نظامیان آمریکایی در شرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/674272" target="_blank">📅 23:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674271">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD-efVz8-5HyhaFhWm0NZErL4i_scimpTXqx7PMXUrxEaV9hvNvj3ycjpzVxhbLbSGfZBkTAsoQe7Vt-DQAp82-JtOxlIKksYMBhmwoFocF-6gPLMD8gGv53Eb85woAptiFuT_hT50UeAoyTBZ0PrG4vhh384wXmYkMZ4_5Y1v3ftjeOuoCH2hS5_M0Yp1Hn_GjdhRQWudlbsEfnvXqgs3xDR_9v5KyMniuTNitQeN_d3VXzU4eTk_v7QcIXfD5m6089n_KekDUxgYZ9_g1Vw5DoLwZe5XagCTezAbDlqNjf_L0JB5e7A_FR3ac87hPyb9vhYAUsmnU66WAxVU0BAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برسد به دست زائران اربعین
🏴
🔹
امسال هم با بسته‌های ویژه و مقرون‌به‌ صرفه رومینگ اربعین، ارتباطی پایدار و بی‌دغدغه را در طول این سفر معنوی برای شما فراهم کرده‌ایم.
📲
درگاه‌های فعال‌سازی:
🔹
کد دستوری: ستاره ۱ ستاره ۴۰ مربع
🔹
اپلیکیشن همراه من
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/674271" target="_blank">📅 23:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: هیچ انفجار یا حادثه‌ای مرتبط با تجاوز دشمن در شهرستان سیریک رخ نداده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/674270" target="_blank">📅 23:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674269">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله پهپادی و موشکی به مواضع نظامیان آمریکایی در شرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/674269" target="_blank">📅 23:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8nsSJJkP0yWui24rAIAJsEFDd3Tur5HqYPq8DYWy1AV0QIGoVrvxOUeLBh2je34Kk02uJwCBqNZycdPirQv4NL2L6ESp6iAionj9BcRKtkQWZWNzBskJ2_DF1FTQ1pxii2cPVhP0uslW9n_k-xHhzOkex0M2ryeNvj63o4bfzN4a6M6kMKYMpwn_bgujq8NZyQlAM77-rcCwB80hX3UicCbAzKqIfvYzkNpnMyX670JQHc7wVqRn4_-uJwCCYWn6VAavabS2aBvBCQBhYcMpvcddWgIScFEPnZzYO6VPAD2xqArzo3q_Doog0dmUxj-yNIvTAoAP0kYTRj-XkhEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاتر تحصیلی شفق تولید انواع دفاتر مشق طلقی فانتزی وکلاسیک ،رحلی،و....
تماس
☎️
09129318455
دریافت لیست قیمت
@Ghamilou73</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674268" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
برخی منابع خبر دادند که در اردن هم صدای چند انفجار شنیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/674267" target="_blank">📅 23:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a597158.mp4?token=jrWbKG-aFQoxvwU-CAiCtCKpwRwGKim4EoXwGE9DQ6vLFy0SDEY_oNy-uhWFGDbP_UY2vZVo5UriCMa8MT2P2__f29wxuXJIHT2qNznqYtly05OHomX1i4hHOE2N24cMNd-l_BK9P1RsAPjGChgYcw7kWRoDd6r6dq8tsArz35c3gKU2fIA4baUmSedrxqmUQFkyUYym9UJrUlwDGIi0YxmYSyCmk37GVY4uOiUP9cdojsj3SyMAO9UHZ2a3_K9BA80Ge_FY5LdHzXniNk5bMp9KPjLKqB_5JSVSiA-J7ykplY1S5n6s_5B8zw207XmRCvkOvGyI3i55XSjHPYcvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a597158.mp4?token=jrWbKG-aFQoxvwU-CAiCtCKpwRwGKim4EoXwGE9DQ6vLFy0SDEY_oNy-uhWFGDbP_UY2vZVo5UriCMa8MT2P2__f29wxuXJIHT2qNznqYtly05OHomX1i4hHOE2N24cMNd-l_BK9P1RsAPjGChgYcw7kWRoDd6r6dq8tsArz35c3gKU2fIA4baUmSedrxqmUQFkyUYym9UJrUlwDGIi0YxmYSyCmk37GVY4uOiUP9cdojsj3SyMAO9UHZ2a3_K9BA80Ge_FY5LdHzXniNk5bMp9KPjLKqB_5JSVSiA-J7ykplY1S5n6s_5B8zw207XmRCvkOvGyI3i55XSjHPYcvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/674266" target="_blank">📅 23:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10fe99630.mp4?token=FovCBpJPgj_jhzuWGMKiV4RD2jSBfsa64GoYXoxeffE55NNPTBfCrqzaXpfqd38oZ7jLNwecI9UvgumXYUvWml4vANXEJU3vBIV9c6nH1brKqUby8f-ZW-muxdc8LfZrtYSrkMPSbwCBLA5caye9-fIaRDhA-ecbCLd2XCyJSkgJVX9ZmQi0sgmozQP2HniJWoSXIjafAnJrC8jmHkKbOOZJB1oDvSq_5hURrVFBS-TmsY3AK1L6Z6xCsbnI6PO0IKnaSXntW7dMJPBJ_TVWZ5pNcqPQcAlyjNSwm9MvZOFggNP0gaIDp8oaynnGTqotuz6YkNhVSNQMBQsEgrLngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10fe99630.mp4?token=FovCBpJPgj_jhzuWGMKiV4RD2jSBfsa64GoYXoxeffE55NNPTBfCrqzaXpfqd38oZ7jLNwecI9UvgumXYUvWml4vANXEJU3vBIV9c6nH1brKqUby8f-ZW-muxdc8LfZrtYSrkMPSbwCBLA5caye9-fIaRDhA-ecbCLd2XCyJSkgJVX9ZmQi0sgmozQP2HniJWoSXIjafAnJrC8jmHkKbOOZJB1oDvSq_5hURrVFBS-TmsY3AK1L6Z6xCsbnI6PO0IKnaSXntW7dMJPBJ_TVWZ5pNcqPQcAlyjNSwm9MvZOFggNP0gaIDp8oaynnGTqotuz6YkNhVSNQMBQsEgrLngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا در امارات و قطر و... هیچ تجمع و تظاهرات و واکنشی درباره جنگ رخ نداد، درحالیکه آنها وسط جنگ بودند؟
🔹
پاسخ این است که این کشورها ملت ندارند. چرا؟
چون آن خاک قصه‌ای ندارد و ساکنانش خاطره‌ آغازین مشترک ندارند
🔹
آن‌ها در آنجا فقط به‌سر می‌برند. به‌همین‌ دلیل مثل مُرده‌ها بی‌واکنش اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/674265" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8D0HbKKsP2dJcRUE5Ywwj_DfBoKkQP-5H6rxE2ZVSQsmcFZn66iGTCGW9Crt-9Mz76A8Q1uwl9s5E3jWJUBi5BU1rhTcwd0WvMcSBst5Whw1SdZWe6pwwkcv7s8EPiv_f7RnZOw0iLuDvRfftFtZalsDhetztRvN_U4NFa_CdataDigC6tonFyZpYG13a6tzSMaGIapuo3oRec0L0siKvDEjMEpDqw_wqrZZYcV4H0tsbufGwh4omLFtUiOgS1PTrXbN3c57lFlrMMnARRX8jJt3Hqoz5YZyTPY_Y-PnAICQ4iJcjRG2Wl5FabxEL-tC2-lYs7X5wLhbvHCsXQ2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهار چهره جهاد؛ از امر به معروف تا ایستادگی در برابر فاسقان
🔹
امام علی(ع) جهاد را مفهومی فراگیر می‌دانند، نه صرفاً جنگ با سلاح. از نگاه ایشان، جهاد بر چهار پایه استوار است: امر به معروف، نهی از منکر، استقامت و صداقت در میدان‌های دشوار، و بیزاری از فاسقان.…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/674264" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
واشنگتن پست: کشته شدن نیروهای پدافندی آمریکا،آسیب پذیر‌ی‌‌ها را مقابل ایران نشان داد
🔹
کشته شدن ۴ نظامی آمریکایی در روزهای اخیر در جریان درگیری‌های با ایران در حالی که همگی به یگان‌های پدافند هوایی تعلق داشتند، آسیب‌پذیری آن‌ها را مقابل حملات موشک‌های بالستیک و پهپادهای ایران نشان داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/674263" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مهرداد خدیر: به رسانه‌های مستقل اعتماد کنید
🔹
مهرداد خدیر با تأکید بر نقش رسانه‌های مستقل گفت روزنامه‌نگاران حرفه‌ای و باسابقه باید امکان روایت واقعیت‌های جامعه را داشته باشند. به جای محدود کردن رسانه‌های داخلی، باید زمینه فعالیت آزادانه‌تر آن‌ها فراهم شود تا اعتماد عمومی تقویت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/674262" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
انفجاری دوباره در اربیل عراق
🔹
منابع خبری از انفجار در حریم هوایی مرکز اقلیم کردستان عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/674261" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedd684453.mp4?token=DN-w99pqfi27kFAPU2ETE6vOC7qM9G1XUxg0AsVjwIf4Xto0jwpFiOV-hGOEEHfnzSPd5C4eFKGtwZ_QZ7IZ7uWM6P4HNhGht_4ssS5dFUGXYXFM2io4zHke9HZ4184WglTIjY_4RS8R7slbuNbmoZGNrdkNZTmnktcqaCRXGcOSpd5UPgZDWMRSts9hJ73TuD81_LfNpG-PcdN47Xw2Z2dOio_aySC8mzp15q2kO5eqnwlTtXADkXtETMN1w3tlK3nRdZq9jQ3bWCSuJXc8bi2CCp8yh4GCuNNshl3AUjEKW8YNSvn-QLPf31dtUhi6i7Fn0VNNfIICApdkXoyLKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedd684453.mp4?token=DN-w99pqfi27kFAPU2ETE6vOC7qM9G1XUxg0AsVjwIf4Xto0jwpFiOV-hGOEEHfnzSPd5C4eFKGtwZ_QZ7IZ7uWM6P4HNhGht_4ssS5dFUGXYXFM2io4zHke9HZ4184WglTIjY_4RS8R7slbuNbmoZGNrdkNZTmnktcqaCRXGcOSpd5UPgZDWMRSts9hJ73TuD81_LfNpG-PcdN47Xw2Z2dOio_aySC8mzp15q2kO5eqnwlTtXADkXtETMN1w3tlK3nRdZq9jQ3bWCSuJXc8bi2CCp8yh4GCuNNshl3AUjEKW8YNSvn-QLPf31dtUhi6i7Fn0VNNfIICApdkXoyLKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر همه دنیا هم مقابل‌مان بایستند، ما کنار خلیج فارس می‌ایستیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/674260" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
در پی دستور رئیس‌جمهور، برق صنایع با هدف جلوگیری از توقف تولید، حفظ اشتغال و پیشگیری از بیکاری قطع نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/674259" target="_blank">📅 22:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
انگلیس هشدار امنیتی سفر به سرزمین‌های اشغالی را ارتقاء داد
🔹
شبکه ۱۵ رژیم صهیونیستی گزارش داد که دولت انگلیس با ارتقای سطح هشدار امنیتی برای سفر به سرزمین‌های اشغالی و کشورهای خاورمیانه، نسبت به بی‌ثباتی‌های قریب‌الوقوع در حوزه هوانوردی هشدار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/674258" target="_blank">📅 22:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجواد موگویی|حرف بی‌حساب</strong></div>
<div class="tg-text">روزهای جنگی- ۸۶
چهارشنبه ۱۴۰۵/۴/۳۱
ماجرای جنگ ۲
به‌روایت جواد موگویی
روایت بیستم‌‌و‌یکم:
ماجرای جنگ تعطیل شدنی نیست!
https://t.me/javadmogoei</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/674257" target="_blank">📅 22:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674256">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYh117F2OheAcyp5FkfCqtIc-L0vgBeZZe8vgbXtIbjAhUTQNejbTo7TUVZ92hkFvvHNBP9TWjaAee65IQPzT1eWjxmPTGvqEj4uqmzO9X2Iwwa0gTyg-0oylmJGjgrj1jw7oKA8TOABCREuhmRV-zsDdLZWF5NxxUyVbd-5fU6iDBT-HI4UU9YqTauFImTvPbaGYiP44tyFKkZDse-E8R2iPxC1lxiK1ooWDFAtKx3ocr3oDU__CzH5AIBMC4PL4NNxZfs_7hD4Z9QaFLjVPLoL8-qrNdNvEH_N0FfOj-_WSytLy7jIx2UWR6rLDEgTeH-XRWmL4W3iixn-j7pPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: احتمال نقش روسیه در حملات موفق اخیر ایران به تاسیسات سازمان سیا در منطقه
🔹
تحلیلگران اطلاعاتی ایالات متحده در حال بررسی این موضوع هستند که آیا روسیه در حملات اخیر پهپادی به تاسیسات سیا در سراسر خلیج فارس به ایران کمک کرده است یا خیر، اگرچه هنوز به نتیجه‌ای نرسیده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/674256" target="_blank">📅 22:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674255">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رویترز: پهپادهای ایران تاسیسات سازمان سیا را در منطقه هدف گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/674255" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5XDjCfzaUkQ_2IThi85A8q2q8FYj3qQDtMjtc-qgwi_ytmYB4RKrW_FraZM3v1xZqvAXy56ouDLby0cC_hbSe0InxrA3JW7yfeN1UBmN95aYLeUMPQ3Fa672xSOD0mDIa7CzrvQXAANjP2U9_PHyYDFUn085_JB8iGs4Pd8DJms1HEE-4LOaj1qa9ymZiz7Y_XH8qA45zq0DxbNH7F6IJlb3u71qKaU-IPuqai87855zClBzv1ulz29Vpzac5c6XCAp5GF-PGtI64VJ2rz8KEpzoUp8K0rtvr_9uwZgOh965pm5NDWg2IjMqXnuVggUfxdjKEmzUpDf6oy1iwL2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در اسپانیا خطاب به آمریکا: تا می‌توانید تابوت آماده کنید
🔹
سفارت جمهوری اسلامی ایران در اسپانیا در توئیتی خطاب به سران رژیم آمریکا نوشت: ما بدون هیچ‌گونه تردید، درنگ یا ملاحظه‌ای کسانی را که به ایران بزرگ تعرض کنند، تعقیب کرده و از بین می‌بریم. به آن‌ها توصیه می‌شود تا می‌توانند تابوت آماده کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/674254" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyExKBSXCTdMnVHX2qv_Sv35wNxajW-WFlvCj7swP-J2GEnmCGp2TVV6QjRx9R9iI0WZIHXtChFuRUi5XGI0jukLcPXSG-zgwe15Jpb-wNN2scJFZvag5cqJ8kwQjNus6zYtivw8auZpSASAOWdOskc-MhmQgj-6ErcbdMsvcxX_5_nEBq6Tzye3MpCHRg9EdKPR6X3JC66fmWvuKVrLTa-X8RaNa1IgyyCjDOz5yME90klEmp3KeSExeumLhQ2omG9rJoYL35DAuEhS0yMRfDlCV0Y1O_vROx2yNJjXM6cdVAo9sbzgOy4q0H6WasCItxYPuTbmL-t5zBcdR4F7Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی در واکنش به خاکسپاری قطعه‌های تازه پیدا شده پیکر شهدای میناب: این سوگ تنها متعلق به یک ملت نیست؛ هشداری است به وجدان جامعه جهانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/674253" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674251">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=CmIJXUxwX4TjpD2aFfY68iHfQ8YvV_j7TQcKCiZ0WoZjYt9MxryYp1n5mjlBG7UaIT2FCMKnSEnx0kxAMPzOHazFvm7ISO5_GYLw3yqIAF1dX_KO2zHw2A1bDCoe4NS1Ner6ulxDfflaGlu76QTwIyY8-Q8wUhKBhdA8vu2RqwhjBD7OD8dxVjJj_SD9PY2lAPkCkjgs3njzKJj6-K7joKV59dlvYtrzuyHeJ7d2KeLpMnurcXhnSppfDuOMjnsCzvR31w02-vULluyofkFg_xOg2Rt7Gl9FE_8l7iN8_ouTgDfje-xXaeAiWg68CYcHCrt8YZPYSSMEGPwEsWtDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=CmIJXUxwX4TjpD2aFfY68iHfQ8YvV_j7TQcKCiZ0WoZjYt9MxryYp1n5mjlBG7UaIT2FCMKnSEnx0kxAMPzOHazFvm7ISO5_GYLw3yqIAF1dX_KO2zHw2A1bDCoe4NS1Ner6ulxDfflaGlu76QTwIyY8-Q8wUhKBhdA8vu2RqwhjBD7OD8dxVjJj_SD9PY2lAPkCkjgs3njzKJj6-K7joKV59dlvYtrzuyHeJ7d2KeLpMnurcXhnSppfDuOMjnsCzvR31w02-vULluyofkFg_xOg2Rt7Gl9FE_8l7iN8_ouTgDfje-xXaeAiWg68CYcHCrt8YZPYSSMEGPwEsWtDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: حکام کشورهای عربی در جریان باشند ایران از عملیات زمینی نسبت به آن‌ها ترسی ندارد/ ممکن است صبح بیدار شوند و با اتفاقی مواجه شوند که انتظارش را ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/674251" target="_blank">📅 22:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مقر گروهک‌های تجزیه طلب در اربیل هدف قرار گرفت
🔹
منابع خبری گزارش دادند که مقر گروهک‌های تجزیه طلب در اربیل در شمال عراق هدف حمله موشکی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/674250" target="_blank">📅 22:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
واکنش قرارگاه مرکزی خاتم‌الانبیا(ص) به تهدید ترامپ
قرارگاه مرکزی خاتم‌الانبیا(ص):
🔹
رئیس‌جمهور یاغی آمریکای جنایتکار و کودک‌کش، بار دیگر ایران را تهدید به هدف قرار دادن زیرساخت‌های کشور نموده است.
🔹
علاوه بر اخطار شب گذشته، ما تأیید می‌کنیم که تنگه هرمز همچنان بسته است و در صورتی که به هر کشتی اجازه عبور داده شود، فقط باید از مسیر تعیین‌شده و طبق ترتیبات اعلام شده قبلی باشد.
🔹
اگر آمریکا به تهدیدات خود عمل کند، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات حتی یک قطره نفت را نمی‌دهند و زیرساخت‌های نفت، گاز و برق و تأسیسات اقتصادی منطقه را هدف قرار خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674249" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt-W9PxHFftvqwUxUkUu0jgdmh-Jco1LbiTV9eNKl6amNHwm85aeg4z65zzD4iMf2jwsnWNVoPEEp3rZ6K-4NzZr9UNclJYHMepbFPqHNnP-OWU8bTSiYDqzZo-d_sq11jneDeyGC_BPPliUKFU7mA-5z4lli3Gh6kqIUusrSVoaaaBZzWw1jOhUHoTza68s3nA_IcnHrwz7jIzmSeUi5-Mw8zzp5L6AKOoZOrMhjnC_DFmYwzcQ9nhJlCHZoVNY3RrvoKEwZDpTqN6CYnPesWlFo0S8SdrPxsr_33dXB8hgdCecplJCNcTtqUo-Bs3zauf7Tm0f0Q_O51fvxaqNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فواید ورزش؛ فراتر از کاهش وزن
🔹
ورزش منظم فقط به کاهش وزن محدود نمی‌شود؛ از سلامت قلب و استخوان‌ها تا بهبود خواب و کاهش استرس، فواید زیادی برای بدن دارد.
🔹
همچنین فعالیت بدنی روزانه می‌تواند به افزایش قدرت عضلات، کنترل قند خون و بهبود عملکرد بدن کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674248" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNNZJckQlELXtpVvzdjJD3BhX1RxZO8Xk-0cMkpCwMBFTc4h5ZW4i59ETFZu-ztnqBl4YDC5vFP7sxvL5ZhAs2jRwmdWxnB75Iq_14C_Wbzyj8UVBbFC_pB_vlNZWyzbi1YCwXPdgz3FJIVQEOK7B13bK6-cBRwSBIPQ2kKu7Hyo8fSn0eVR8br7gbDqipzuvbL9Db_QhcPW8mHGBxil2QllrlkDczfkLEb1l4kXlVNTHne1onPAX03WhpEvoFCQbhy4aaqp39ZC9egAg5rLSqDWHddO60SmGEUo9bSaiMaNfeqy_YEhem0Sxg0zirvTiKQPoL-Pb1QShcEwHxh0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به لفاظی اخیر رئیس جمهور امریکا: هرگونه تجاوز به ایران، از جمله به زیرساخت‌های ما، پاسخی قوی و قاطع را به همراه خواهد داشت
🔹
کسانی که به چنین تجاوزی کمک کنند، با هر نوع پشتیبانی که باشد، نیز اهداف مشروع تلقی خواهند شد.
🔹
دکترین دفاعی ما روشن است: چشم در برابر چشم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674247" target="_blank">📅 22:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749211c579.mp4?token=dVEEKg5ZXO2H2wdetWWawQ_p4lrBMvQU2LsS9S0hua7zGjG9DX7b7QS3Ej65o6wjuiW17mRVTd9UIQVUlMa5M-oglYwzU1MiSK2TCYDFTeeb44LsUUvv9tc7WEtnBrgmPJesQZM1itesn9JG7cLd9lzH-yfnjpaLVsDnYa7Ss_rF2611EaaDOV0vJ4ljzTy0seqcYCL0g7G9AHEnuZbx_DK8yzfsGAskARWR9CnNIVMGVUwfH1ToELZKJMginJPn9iXaaPETqd85ebny--FUOnN1AsASd6Ol7FfqNXbBSpS12RXTMpJrTumX5yfNRnAc7pBOClKMcBwpE4zaDtG04A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749211c579.mp4?token=dVEEKg5ZXO2H2wdetWWawQ_p4lrBMvQU2LsS9S0hua7zGjG9DX7b7QS3Ej65o6wjuiW17mRVTd9UIQVUlMa5M-oglYwzU1MiSK2TCYDFTeeb44LsUUvv9tc7WEtnBrgmPJesQZM1itesn9JG7cLd9lzH-yfnjpaLVsDnYa7Ss_rF2611EaaDOV0vJ4ljzTy0seqcYCL0g7G9AHEnuZbx_DK8yzfsGAskARWR9CnNIVMGVUwfH1ToELZKJMginJPn9iXaaPETqd85ebny--FUOnN1AsASd6Ol7FfqNXbBSpS12RXTMpJrTumX5yfNRnAc7pBOClKMcBwpE4zaDtG04A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: اگر واقعیت و جزئیات عملیات اصفهان منتشر شود، خواهید فهمید دشمن برتری عملیات زمینی نسبت به ما ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674246" target="_blank">📅 22:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای جدید در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/674245" target="_blank">📅 21:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
برق در کویت سهمیه‌بندی شد
خبرگزاری فرانسه:
🔹
با ادامه حملات ایران، دولت کویت برق را جیره‌بندی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674244" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFg1GBB58ZeUZ3uvrchUHPxXXbsx3y_03JuieiphhFCfJyUmkgw9lD6BnpI-HnJ2vgRYctsRr9FC65zyvCmhzVgyl6iz6OMs70dyg6EgkJ_0mvKSYsnV8N799H91zkxfzjbPVRt-jkNrWrqGIoKX-Ur-FqD5H1BDmDp0oBLwVDv-9cFn3SDEIj5i-NqRywOhwhd49FKZL8T_QpuS1tSEcoH16ykB27W2UKyXK0XMGsc0vAXfnAJqUSETG-vL962KxM-R77vSP6_XTr5HDzQpclisDoNHEOJneYuynaTVG-Zyhg75Vv1k0K85pMTy0xAdDY-UNQkyelgS1ZYpgqP8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران به شرکت‌های کشتیرانی: مسیر مین‌گذاری شده جنوب تنگه هرمز مسیر نابودی سرمایه شماست فریب آمریکای کودک‌کش را نخورید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/674243" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NARacWBMzuHvZnn-N1s7ftD7yRatPfZyNrgXxhIJU5QvNFXy4TzvmpbLvxv90IUWvyKyErcQZSB5GQDSQeKYzvyl__ZhsIhQck0lAAxXX3aeXMWqygSbAWj1uBWEH-hU-c9QXsxwp6bwkGJMF0LyT4zCyh9yUjYV55mNbhAypI7su17v1P2tdfFNQkyLxZFkqs7DgTm_uUwfywXUi14VIXxmEbBwPzMsOByi9HpjxEmFgKJQe5u-H0F1SBhggXmA_ZKfqSu4J7_J1OlFpZqulTXThxJlORmxIeAEZZuuVF9c5hhCBdrZK9iwVw8bJj9TNfkrBusJ5_yg4GZQx4DPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده هوافضا: شلیک‌های موثر و هدفمند ما تا برگشتن آرامش ادامه خواهد داشت  سردار سید مجید موسوی:
🔹
در نظام محاسباتی ما خاک، خاک است، تهران تا جنوب یکپارچه برای ایران هستند. شلیک‌های موثر و هدفمند ما از سراسر ایران بر سر دشمن تا برگشتن آرامش به خط ساحلی جنوب…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/674242" target="_blank">📅 21:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=Yl6ji_hHS6s23AaI9-GnlaWXgQyXofjHvkSbeHsoaz79B-u-MF9MSyXwihJNY4Fm2hYmxoXZStHXWnniyJbOPr-a4O1zEaXM-73s5JBRWGuvNjY3M_BD5bvsAvOXL1fRG15NuXx7-7Bwf9t0ZjR3NINBI5i1u4FVGrT3mw2B2XOZI9V-qBrxy7IscR4e0k00N1vO_CE1NwUckr-N3U6Ctz0inIvHTJ7Y3twHNlOY0YmT5Jb6SHYcGP5nlnii9jG0sdlL267chMz90NpJEW9pEDDaGbzVkN2k1KTgQ54gBvHr5_eGmwGddMSbsqXBwm2Xz7eNXcfOpPT6To5J1A_nZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=Yl6ji_hHS6s23AaI9-GnlaWXgQyXofjHvkSbeHsoaz79B-u-MF9MSyXwihJNY4Fm2hYmxoXZStHXWnniyJbOPr-a4O1zEaXM-73s5JBRWGuvNjY3M_BD5bvsAvOXL1fRG15NuXx7-7Bwf9t0ZjR3NINBI5i1u4FVGrT3mw2B2XOZI9V-qBrxy7IscR4e0k00N1vO_CE1NwUckr-N3U6Ctz0inIvHTJ7Y3twHNlOY0YmT5Jb6SHYcGP5nlnii9jG0sdlL267chMz90NpJEW9pEDDaGbzVkN2k1KTgQ54gBvHr5_eGmwGddMSbsqXBwm2Xz7eNXcfOpPT6To5J1A_nZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: تلفات دشمن در حملات به اردن و کویت چشم‌گیر بود؛ آمریکا جرئت اعلام تلفات خود را ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/674241" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هیچ‌گونه انفجار یا آتش‌سوزی در جزیره خارگ رخ نداده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/674240" target="_blank">📅 21:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cepZ3VnVaZQPOWUMrOXyjOJ3N40UjB9NgBfqm8Oh3O2_KwfttXaYK43h1YEawEDDKeSoo27HJw4MO-jEn3aIcBWzVJLOwQX48fCwak9t4Al3g32V0ZThcPwyUeU1uS9ZXVSnjhlGsWbKseassF5TIyTtoqk4z8efbsUlJjaqTqJvpEvWAiRbhH-KG82HSzhigKoMfLnLEvRaXP00p6Ix0zhx4W3_x3y013zOoslKqDtOuxXrOEVEYvqHs69cf9mjP25w3yHTnvDmbz-q-Cheo0gaZ-k7mmSEAuvm38mqSGeNf3tZiWFpLbODCDvZpmkXoWfMGD9TzUe26J_uDqm1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگه هرمز استفاده نکنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674239" target="_blank">📅 21:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای جدید در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/674238" target="_blank">📅 21:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
منابع عربی: صدای چند انفجار در کویت شنیده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/674237" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=qGqsmG__u4ZcTH4o5txioYv2JBcA_tO-XhmNE5VG3DBL-0ZC3woGf7LtJIqyhlLvgP0vhDJChS6EpOfEwjSVRvHx2W7J0ke2s_nMB6jPAXpE-871V7nU-2muxXs0R9RmE2aFmSkbcvOyG2h-HzBLWLuHhqFIJOvdS-pLJLiIa4CJ2G5_ynlvcJvnCegIPE9x4XZv1Ge1--4PPBCA5zZidYhVdul5SDlaftJdyW-mXrcNKzUzzVPjl_YD5XCHgxR2BkxA5ZsMIL_YS8SE-qT-48fOqEXq6_6HSDqxgq2zvUXO91lyxakV0_0KzI-3tx0ESzfrDg0jAvDkvVk4JfTNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=qGqsmG__u4ZcTH4o5txioYv2JBcA_tO-XhmNE5VG3DBL-0ZC3woGf7LtJIqyhlLvgP0vhDJChS6EpOfEwjSVRvHx2W7J0ke2s_nMB6jPAXpE-871V7nU-2muxXs0R9RmE2aFmSkbcvOyG2h-HzBLWLuHhqFIJOvdS-pLJLiIa4CJ2G5_ynlvcJvnCegIPE9x4XZv1Ge1--4PPBCA5zZidYhVdul5SDlaftJdyW-mXrcNKzUzzVPjl_YD5XCHgxR2BkxA5ZsMIL_YS8SE-qT-48fOqEXq6_6HSDqxgq2zvUXO91lyxakV0_0KzI-3tx0ESzfrDg0jAvDkvVk4JfTNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: پنتاگون هیچ سخنی درباره تلفاتی که در حملات ایران به ما وارد می‌شود نمی‌گوید و پنهانکاری می‌کند؛ اداره این کشور به دست یک دیکتاتور افتاده و این یک وضعیت رعب‌آور و نگران‌کننده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674236" target="_blank">📅 21:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
شبکه خبری آی۲۴نیوز: نتانیاهو خبیث، همچنان منتظر تأیید رسمی از سوی کاخ سفید برای یک دیدار احتمالی با ترامپ در هفته آینده است
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/674235" target="_blank">📅 21:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814d014f61.mp4?token=cbMM2O7TwNoG5mUdnmKitTN1fH6I680VC2fEfY2lUAupmQuDXBwGIMCvc_v5T1l7mDxKyDjm-LNEd-ePLl-65yGk6efV0mcJqUlpgoC-otL0bZEg-tLcQXMc886Gg1nkeva6CgMHrytMA0LON_k9pyq3Y--lOPQDIH_WH0Oo8ZwdNBvOuWIA0uI7IQQTGh1VZj9OqcwoVWO5T21tsJv3EeUkx_wYMmwRZ3I47sTrcwL6WpKU9WgjTq8aTX4MXWrau-VwuRbSVi70yLE5CWZYQZF6dXcW9L0P8wIfv7nZ2aunTCB9ycAqTbCWNYUwEB3hohQ-gPaDKBTJCSoNbFtu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814d014f61.mp4?token=cbMM2O7TwNoG5mUdnmKitTN1fH6I680VC2fEfY2lUAupmQuDXBwGIMCvc_v5T1l7mDxKyDjm-LNEd-ePLl-65yGk6efV0mcJqUlpgoC-otL0bZEg-tLcQXMc886Gg1nkeva6CgMHrytMA0LON_k9pyq3Y--lOPQDIH_WH0Oo8ZwdNBvOuWIA0uI7IQQTGh1VZj9OqcwoVWO5T21tsJv3EeUkx_wYMmwRZ3I47sTrcwL6WpKU9WgjTq8aTX4MXWrau-VwuRbSVi70yLE5CWZYQZF6dXcW9L0P8wIfv7nZ2aunTCB9ycAqTbCWNYUwEB3hohQ-gPaDKBTJCSoNbFtu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همدلیِ واقعی، فراتر از یک استوری و هشتگ
🤝
🔹
برای مردم گرم و صمیمی جنوب، تو این شرایط گرمای هوا و آسیب‌های جنگ چه کاری از دست ما ساخته است؟
🔹
پاسخ آسان‌تر و نزدیک‌تر از آن چیزی است که فکرش را می‌کنید:
مدیریت مصرف برق تو و خونه خودمون
🔹
فقط ۲ ساعت کاهش مصرف در روز = پایداری برق در جنوب کشور
🔹
این ویدیو راهکار عملی را به شما نشان می‌دهد.
👆
دانلود کنید، منتشر کنید و صدای این قرار همدلی باشید.
#قرار_همدلی
#صرفه_جویی
#همدلی_با_جنوب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674234" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وحشت کشتیرانی از عبور از تنگه هرمز و باب‌المندب
شبکه «سی‌بی‌اس»:
🔹
برخلاف اصرار واشنگتن بر ایمنی مسیرها، مالکان کشتی‌ها به دلیل تهدیدات موجود، حاضر به ریسک عبور از تنگه هرمز و باب‌المندب نیستند؛ فعالان این حوزه وضعیت فعلی تردد در این مناطق را «وحشتناک» توصیف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/674233" target="_blank">📅 21:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3lGSntbC-J8CCf4CnIvtVaA4Qt6PsrIPmyL6ef-gkDtR5T6RAOoP_D_0nCR3gnkMsKJhK25c4tciisr6jbS-iE-8t7Z99GEl6j2z4Qnf0NgMREJ0TEnTxPA1aHLeW2_eRzCmfy0aLlVkNbafTI95H0MFih8S6vBgbLcKTUnQQCbJavOT8RUlqQYJ8rq8g3FP6imw-1jM22PyY3Bwyx6Ffhz79yIYU2UOECIGT9U6QTkfX-GSKYazgEzhE1dh0ug_VeskL7EKCDpclRP6xdy6q19TeYG_vfbiFjZidT8d34KdW0HsQDUSziDsffr9DjsxQV2SfXKLA2IYGtEqlGDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر دلت هوای زیارت اربعین کرده، این فرصت را از دست نده...
‼️
🔸
با پویش «زیارت به نیابت امام شهید» می‌توانی هم به نیابت از رهبر شهید انقلاب در پیاده‌روی اربعین سهیم باشی و هم شانس حضور در سفر کربلا را پیدا کنی.
🔸
به همت هیئت قرار، ۱۰۰۱ نفر به قید قرعه راهی کربلای معلی خواهند شد.
📲
برای پیوستن به پویش و شرکت در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674232" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e2bb7ae0.mp4?token=keO9YnNd7MobFwuqLVxB0hF2_8BVVtO6bTseUZ_AJs_Q-MbfT65v76NPCIpCLrOUHCKl499VWpyl0esS_C9uXyJysLUyPAILxk8Evl59XuFjbYtVdeO9qr0irC-VsvRT337jU4W4RdBQ1IJuI-4voKfchs7uXtwYa-R-5tx_09cy2b-vVMYIOel8zc-mbQ5N_RraX8WmYvFgEbXYGs4F7pHzpDr9QuvQPXJVTUAzXbpWPGvTR9-vITfbLzfCfPilowUJMD7FKPF3vkg_22wjI177JzaqfaPONI9R4gRCaYjj4plcXxdc3zFgH8HDi7PwQjuIR3VkMFPo9-XRriJ_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e2bb7ae0.mp4?token=keO9YnNd7MobFwuqLVxB0hF2_8BVVtO6bTseUZ_AJs_Q-MbfT65v76NPCIpCLrOUHCKl499VWpyl0esS_C9uXyJysLUyPAILxk8Evl59XuFjbYtVdeO9qr0irC-VsvRT337jU4W4RdBQ1IJuI-4voKfchs7uXtwYa-R-5tx_09cy2b-vVMYIOel8zc-mbQ5N_RraX8WmYvFgEbXYGs4F7pHzpDr9QuvQPXJVTUAzXbpWPGvTR9-vITfbLzfCfPilowUJMD7FKPF3vkg_22wjI177JzaqfaPONI9R4gRCaYjj4plcXxdc3zFgH8HDi7PwQjuIR3VkMFPo9-XRriJ_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: بادیگارد (۱۳۹۴)
🔹
ژانر: درام، اکشن، سیاسی
🔹
خلاصه: اگر از فیلم‌هایی که فقط اکشن نیستند و در کنار هیجان، شما را به فکر فرو می‌برند لذت می‌برید، «بادیگارد» را از دست ندهید. ابراهیم حاتمی‌کیا در یکی از مهم‌ترین آثارش، داستان محافظی را روایت می‌کند…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/674231" target="_blank">📅 21:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhpdgfwyO9A2HnTOcVwXCR5-zE7JwGZN2yY2DxLUixlNabo0-DM295-gkbNZYBWGn6H4gXkcJpjpKavIMMMQ1gSzUxSAmEv3iqqWeGTGYnsPSWKra9IIIs15swKkSPLB_U496W_1dl8MiagP153MWjT01H1RCn_dWMVLJgS6sDP0ncC9kNbpHu9w0kn8ef6fgL6kbGDJIbIQqFJsZSU5mwdcXmhSsSxH2XreVfqeclcz05H6p2YSHcsdcBm9ht79UWBS2WcNy4CrcqDwG79DaF2cBAK96hirYLmwWGsZSqtneTB5yjqUs-mEuQKhVYD8ckB3LK08BOiem77uC33bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی‌های خوک زرد: از این لحظه، هر زمان که ایران به یک کشتی در تنگه هرمز شلیک کند، خواه با موشک، موشک، پهپاد، یا وسیله یا سلاح دیگر، ایالات متحده یک پل یا نیروگاه واحد، اعم از نزدیک یا داخل تهران، پایتخت، را بمباران و نابود خواهد کرد #Devil
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/674230" target="_blank">📅 21:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08b79843b.mp4?token=BU1C-gzrEkU6czeSK_3pax9lV9bKbZgL7z_ST8ZMDPBNff8N4AJ8x96cN59E39uDtYbK1oOQItjn_iLedTQ7u-8O9Ml6EyUSXMwTn64lFqKZD1zW1nd4zmaWh_rJFi991TzNrZqpknrJOp9Igh0TF23-oNxrpIP2HirB-npeM6xSi1dKyWMH4brMS0sLtH62WobEsXYcood9IMwvVA0EmPIzuSekF9G07-ZykI2o7UXyjdhz8nV4pR8L0BBMOny-bFXGsKnwtm3BeYpC8y97uKWUyVQVHlJdynWTK8dFfebVTYOGShh2-n0D3l8Ps0WpFecLpcgAyGRXvCacfsC7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08b79843b.mp4?token=BU1C-gzrEkU6czeSK_3pax9lV9bKbZgL7z_ST8ZMDPBNff8N4AJ8x96cN59E39uDtYbK1oOQItjn_iLedTQ7u-8O9Ml6EyUSXMwTn64lFqKZD1zW1nd4zmaWh_rJFi991TzNrZqpknrJOp9Igh0TF23-oNxrpIP2HirB-npeM6xSi1dKyWMH4brMS0sLtH62WobEsXYcood9IMwvVA0EmPIzuSekF9G07-ZykI2o7UXyjdhz8nV4pR8L0BBMOny-bFXGsKnwtm3BeYpC8y97uKWUyVQVHlJdynWTK8dFfebVTYOGShh2-n0D3l8Ps0WpFecLpcgAyGRXvCacfsC7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به بهای جان، پای این عهد ایستاده‌ایم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/674229" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هشدار مشاور رهبر انقلاب به آمریکا؛ هرگونه خطای محاسباتی بازار انرژی را به آتش می‌کشد
🔹
علی‌اکبر ولایتی با تأکید بر ورود ایران به مرحله جدید بازدارندگی، هشدار داد هرگونه خطای محاسباتی علیه ایران، امنیت بازار انرژی و اقتصاد جهانی را با پیامدهای گسترده‌ای مواجه خواهد کرد و واشنگتن با تهدید ایران به ثبات نمی‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/674228" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c551e6f36.mp4?token=l9wr_Ve58X37ljUvsgXJH0J-U5NcfbD2QL2z7vpG2wfdN0MxS3ejYsb3A5XW0-63vaMFTd-9DGiep8XmtVE2cfunkhSblpnhYdXGAtRM98bHpciprzUZI7XwS7Z_0nafq0MVCgF6zgjKVW4yxlWcT4y2OC99G6gDHtqGgm9z76OJLSi0o2VOTDrzXRucM0NpknlsjAyFN3iLif3f8l8a8n7WLEvdRnyVKZmNeePDxteBz9RUx_FBQwfOeE8hg6-YMk6jo_KKDJsnyYB6KQqXBxDRL8pG_0wwWEjzO4ybGZPoqSazfaxgxotYxZM1nVfVkxrhGBr0LpWE_wE7cuFvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c551e6f36.mp4?token=l9wr_Ve58X37ljUvsgXJH0J-U5NcfbD2QL2z7vpG2wfdN0MxS3ejYsb3A5XW0-63vaMFTd-9DGiep8XmtVE2cfunkhSblpnhYdXGAtRM98bHpciprzUZI7XwS7Z_0nafq0MVCgF6zgjKVW4yxlWcT4y2OC99G6gDHtqGgm9z76OJLSi0o2VOTDrzXRucM0NpknlsjAyFN3iLif3f8l8a8n7WLEvdRnyVKZmNeePDxteBz9RUx_FBQwfOeE8hg6-YMk6jo_KKDJsnyYB6KQqXBxDRL8pG_0wwWEjzO4ybGZPoqSazfaxgxotYxZM1nVfVkxrhGBr0LpWE_wE7cuFvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زد و خورد شدید پلیس ضد شورش هند با دانشجویان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/674227" target="_blank">📅 20:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی بانک سینا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFV5Y59MmQrbrdOTw-aZTjmT0cewQWY6dgXi7LIXLNMjE4Ri1QECq3URf-CPI8cqd18rjSUyY2Xlzwr1z0i5DlGba2e6DE-kupor19ULJXuDZod1Lr8wzxYd6czq113LfL4oK3km280NXKzBJZJR-1YCPCIeL53Xsk7kNIKh3hzrUoBU4Ek-JOpLhqVCmL7iulZ1mJXuHHYS6LHmSIRoC4fTohGdQbH4p40thjQDLnKPPtvlXfWmNZlbh4F3v_NdAzKqrGXosaTPuNwTCeZ5iwU_U8k-o1LwKYvypv_8RSOlB6RephBfpEI7_7wvswQ09rJMmUTJymzu4aQbvADHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
تایید عملکرد درخشان بانک سینا در مجمع عمومی عادی سالانه بانک
✅
مجمع عمومی عادی سالانه بانک سینا با حضور ۷۵.۸۸ درصد از سهامداران،برگزار شد.
🟦
در این مجمع، دکتر علی ابدالی، مدیرعامل بانک سینا، با اشاره به نتایج اجرای چهار راهبرد اصلی بانک اعلام کرد: سرمایه بانک در سال ۱۴۰۴ از ۳.۵ به ۷.۸ همت افزایش یافته و بر اساس برنامه‌ریزی‌های انجام‌شده، تا پایان سال جاری به ۲۷ همت خواهد رسید.
🟨
همچنین ۹۵ درصد درآمدهای بانک سینا از فعالیت‌های عملیاتی تامین شده و منابع بانک سینا با رشدی مناسب از حدود ۱۲۰ همت به نزدیک ۲۰۰ همت، این بانک را به باشگاه بانک‌های ۲۰۰ همتی و به جمع پنج بانک برتر خصوصی کشور رسانده است؛ رشدی که در کنار افزایش مقیاس بانک، با مدیریت هزینه تجهیز و بهبود کیفیت منابع همراه بوده است.
▫️
@sina_bank_ir
| بانک سینا
▫️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/674226" target="_blank">📅 20:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ7WKYd5ApOwr5A8L72sLbD9Mg5SgI211nPwVffEy9-c6CHNtAcf1OkWw0Cw5kVt8RKZ3Fby8GM42hCkFdcrdVgaBn42bVu5o4EcqNous_tjlJ38agSAaG5gSIB2rx8QTz5Z3hw0D8YkShlYGEf1wuNBYXq77wtqCAL-smYDbUHd2K5s5K-sCBdM5BylanJsvxGGHv_TrBij1U53IbDS7-cJCKvO10SlMQE74Cj1IZK9L6uO5EspHQ5brE9RuQ4-PdFICI3g64aUYQKfKwli73Nnc5qqOnp2IzutS8b55oKi_Mve_BF5DTs6XQd1QxttpMxbnY_hi08o9J60e2VGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قمری وفا: عنوانی که درباره بابک زنجانی به کار بردم نادرست بود
مدیر سابق روابط عمومی بانک مرکزی ضمن توضیح درباره روند انتشار مطالب، از بابک زنجانی و شرکت‌های وابسته به او عذرخواهی کرد.
این شفافیت و پذیرش اشتباه، اتفاقی ارزشمند و کمیاب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/674225" target="_blank">📅 20:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG4RNseZHseuoOKdaeMZzNVdH4Y13xq3q8mPAsGfAq8sgoLRtjwUunXguXo2E3xnLl5Ygo_XgNUogXieUPTMG8BBRYI5vsLIcAcQ7dQx-TfkgTbaPjs7Vx5ivFDvVtCGgyA3KXRVflfv6sRUI84EHQkAMURwQg9TGZGn7Pr5dR8ntneVACv4fcBVZ8a4Oy0KY1JrQ0aYalvwKX9v2o6RYRNVPJKiRykeD8ZSFLQVLyk2GcEQl4pfdO5U6A9bGpcCvG0mfHEtuBwQZXBg2PUMJ0RsoHaka0wDHqkTyWUHgFkzmy_ksc5CY3XUKo-R7_rrEpTID3NIEnFiBiNnX_OWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مورفی، سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔹
توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/674224" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQswILMUgtmcARQPjNYTWF3a10uL9Z1lhJjR1EVaErLGs4dwUT0BFQUsZLkt79ltoQOvB9tTJOMmJZa9HahjMyeTOREgAyPw8lr7DEXegsXRg7XXUJHF_uRP03-XiJvQO8iZPDIAw6eMT0mB-p8o-MOhPCyCCSp3_6apumHfrpWq118b0SHqAwEiUSA-vQnNhotBexzkGR8-u4Me8tZk2Z7O9dh7QElUaOaMZmDUcUhu82L_484kzNaHvzQdGgLI5KfuqUalkc4Kd18wPAaOmfMF0HqFLz7Hg8XSXGkkVSxxIXmur8hIJnc0dW86dApm_tZvgVVrw-mCoQueXRnlrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته است.
#جاسوس_موساد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/674223" target="_blank">📅 20:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol2emVWwIytGEHoXiOUpkg_hWzRDcj-8a8IOuwhDX6HM6BGWXevDsdHppjW_rvM4I7Uj-vcPzhEXanNEJry9DqB9O20y_yELCTcsXitT6yZNU2r-TGIiOW3ekiJi6o0LYmO4xgfMZ4HIXnufj9R_qpPAxbB9EQhxEQcKV2w68FM_k9BIf2t_RuSSS479inxIilKjpVJky9weeJJY5AEh49Dy7UGufgpg4KFqyUbX0HM3P2gcLBe-DW_Xq1u57iIEcfvd76IkPq5417OGr1FIgghFKa58U8jUOVx6Wu8AU5FqjS00lme70NcBsIAxDvTBnJDWsPC_gkiI6_nWTVj3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پستی که سگ‌زرد بازنشرکرد: ترامپ به سنتکام دستور داد دروازه‌های جهنم را به روی ایران باز کند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/674222" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm2xdWwFEV6W8QY3bLTfzD9j6QS8e39HSgVdPrai-Cvo-6gfAnHU1BfkescGwR1uNxFyGONUoShAGYh_LDg6OcqxR5wsv61aR0EW7alp_u6C9bwTPOVqA90P4d5QIBTcnYOBoJT_SnV87LxpVuxrYi7v7VD8JIZLAJB9YjYqcqPtugRGfRIScD8mMXV1ViXG2NgxHkE9PgGIBKSMxHmH04PUQ5U1vsUWhmiLryGjqCK0nOvcurfKsYX2ojoVuJR-hdQ2egqjANy6NkSlKq1FxcBf2ECqhS_62RJN2QwEt0D1Ub3bB17XwSGCAllo3RAzsGzBdJKTsFfkpBalvHgY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاخ سیاه
روابط عمومی سپاه پاسداران گزارشی از ضربات سنگین به پایگاه‌های آمریکایی در منطقه را ارائه و اعلام کرد:
🔹
عملیات تنبیه متجاوز ادامه دارد، چرا که اگر متجاوز تنبیه نشود و هزینه سنگینی بابت عهدشکنی و زیر پا گذاشتن توافقات نپردازد، تصور خواهد کرد که هر وقت اراده کند می‌تواند جنگ را از سر گیرد و هر وقت تحت فشار قرار گیرد به آن خاتمه دهد. سپاه در ادامه هشدار جدی به آمریکایی‌ها داد و اعلام کرد: اگر تجاوزات دشمن ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
🔹
هشتصدوشانزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/674221" target="_blank">📅 20:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وقتی انصراف از سقط، سرنوشت یک مادر را دگرگون کرد
🔹
00:05:25 رؤیت آیات بازدارنده از سقط جنین در هنگام تصمیم‌گیری من نسبت به آن
🔹
00:25:40 صحبت کردن نوزاد ۶ روزه با روح من
🔹
00:31:50 نیرو و قدرت گرفتن از امید همسرم به بازگشت من در میان تمام ناامیدی‌ها
🔹
00:45:00 حق‌الناس از مهم‌ترین اعمالی‌ است که بررسی خواهد شد
🔹
00:55:20 طلب مداوم مرگ برای من توسط یکی خدمه بیمارستان
🔹
01:03:30 بخشیدن جان دوباره به من به خاطر جان بخشیدن به نوزادم
🔹
01:12:00 تحول اقتصادی در زندگی بعد از پشیمانی از سقط و متولد شدن دخترم
🔹
قسمت نهم (بهار)، فصل پنجم
🔹
#تجربه‌گر
: حدیث ایرانمنش
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/674220" target="_blank">📅 20:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35db5cd9f.mp4?token=TpwhYTax2ZRU-76dmFWoFlSzGcFZkHPdIelRuyG2lzNWgChdzn2_vKmpG98qrGCdYsBKEhx-T9DdsLoD4DWvbgNmIphBQGUUWYKqPc_LYWcMGEkadTvOplwM56Cy0NdXK-MofYO1Bv9VC3yLd8vwvwt6RieVOxitm_aqbik1kYfWBGg6z8bUh_qrUEgdcawM9hEj5f9NNrrPa0-grWxLGtJboIxfwIhR6SE14pqcq1czHAuEtMrtLLMP-WHnz7c16SDD9olN_HpsnJEfrAOzOJZH-9czoOkmR0F1JJEGw105-ETyMSxrGQ7o_R_z41UmserqM6sH8yIyWaJ7zuqkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35db5cd9f.mp4?token=TpwhYTax2ZRU-76dmFWoFlSzGcFZkHPdIelRuyG2lzNWgChdzn2_vKmpG98qrGCdYsBKEhx-T9DdsLoD4DWvbgNmIphBQGUUWYKqPc_LYWcMGEkadTvOplwM56Cy0NdXK-MofYO1Bv9VC3yLd8vwvwt6RieVOxitm_aqbik1kYfWBGg6z8bUh_qrUEgdcawM9hEj5f9NNrrPa0-grWxLGtJboIxfwIhR6SE14pqcq1czHAuEtMrtLLMP-WHnz7c16SDD9olN_HpsnJEfrAOzOJZH-9czoOkmR0F1JJEGw105-ETyMSxrGQ7o_R_z41UmserqM6sH8yIyWaJ7zuqkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی شما در پویش «ایران وطنم»، تجلی همبستگی و غرور ملی است؛ هم‌وطنانی که با گویش‌های شیرین محلی، پیام ایستادگی و دلگرمی را به مردم صبور جنوب کشور مخابره می‌کنند.
🔹
این آواهای ماندگار ثابت می‌کند که اقوام ایرانی با وجود تفاوت در لهجه‌ها، در بزنگاه‌های دشوار، پیکری واحد و یکپارچه هستند.
🔸
شما نیز می‌توانید با ارسال پیام صوتی، راوی همدلی شهرتان با مردم مقاوم جنوب ایران باشید.
👇
#همه_باهم_برای_ایران
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/674219" target="_blank">📅 20:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99980af4d6.mp4?token=K-Imlka5uJGf1c_qkFqPALoLkNN-X03i-m2Zz0_SGBK-_dSRQ91yRf2K1nTGsBL3cG3MVqNYdALTPXJnt9de-ek5O2R4Y1p3PPSgYbONgIoJazoZdP9nd9JCCZIySAW2DCEp3qMidxLdX3_PfiOmGGyprmHInqxRpI6YHhlXRq8JEGENP51YGWO0cXjRqHhpzgmxdnCUt2faNHXSOPBpLrr7PpmbqACDLhWwWDoIy3IgjSA79ZNEFqQoKqnkHaeRNCz1pFLYMAlsd_0-B3arSe9MtoObBNuA4UwIvKgr5RmND_hRnmtizlfM0SXWzPnMSxIgpinwa4XzPbdwfy0Tqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99980af4d6.mp4?token=K-Imlka5uJGf1c_qkFqPALoLkNN-X03i-m2Zz0_SGBK-_dSRQ91yRf2K1nTGsBL3cG3MVqNYdALTPXJnt9de-ek5O2R4Y1p3PPSgYbONgIoJazoZdP9nd9JCCZIySAW2DCEp3qMidxLdX3_PfiOmGGyprmHInqxRpI6YHhlXRq8JEGENP51YGWO0cXjRqHhpzgmxdnCUt2faNHXSOPBpLrr7PpmbqACDLhWwWDoIy3IgjSA79ZNEFqQoKqnkHaeRNCz1pFLYMAlsd_0-B3arSe9MtoObBNuA4UwIvKgr5RmND_hRnmtizlfM0SXWzPnMSxIgpinwa4XzPbdwfy0Tqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در جنگل‌های تونس
🔹
بخش‌های وسیعی از جنگل‌های کوه «سیدی علی المکی» در استان بنزرت تونس دچار حریق شده و عملیات برای مهار آن ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/674218" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
