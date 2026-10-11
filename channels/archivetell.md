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
<img src="https://cdn4.telesco.pe/file/CUOd7a2k2qFO7tvQcL5aJxQ1QBFCgKVSs4EMWwUrtcoayu-RMxbHUWCpxEa9kuGulmTbj_PikFK2hdRSsOZlGZnBh8acGuld3arotnt37uun2TAkHOw-R98QmBQ49X0PcD-vpwrtp049JpQ3rdl55Ajx4BKx2NecMaQhkLPznXeh4xuu_TIUdiLRRFYvCdkmDKKaDi0VJazeKVHs_E5IWqbUCCavxJBYAp6T-WL-AIoRUkf00wy7QzxTajOqi0hXdPiRpVJmuAeistcyL_BLenRFxWHEC--9c4Sz2OCRNWKe__xWYj4eyoZEyk7S33LOSWWiEPv23k5X5QZmst_CiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmVr0jLW27hdlePlFJ2Gh-bmm-OJRYF8saisnZkAK7jYWslSAhMbjtpAbhJTJcwfL-x-IYF-HBKFE2iVGlEC88SonyoARJ-NMuxvEJZugxm_6lboO9TS-DqzKyfTLJuGfBEar4wxGXO3RLI1CKG93r7wbOCjHdnpy44t-7jyAw3qu4rvC8qXOn1lkTCyU1emjDW6ZmV7lJ6oWoeDiZY69nBhusFJay7YCe6ja8jaxpSt5EQg9Q4Era0mbOWGhzJfJJGZTT9dCDRT7Y9Tli8ECQUwoYAg7WLZDGmYtggQY1haIBMNYZPYP9EJq6C3EjS1sOercTMa2B6UooEuKt9X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑨𝑺</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Game (1).html</div>
  <div class="tg-doc-extra">5.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVPNWAWYKVO4IS05Sjd1kNSrxB7TlQZ5HsLRkJDu9X2hYGD7VgQmak-_YyUav5CYGPGnJLt2I19R7tgli9LnXNto_5zGnqasCx9n6Of8y0d7HkLtidzykDz0hif0UosFKNKKwJMcBbO49mswvIqD9I12jtXiPK301lDOkhjsZ7ZgCjvMy1bINp8IbKcJMwtk63dOolTDkGw7lVZh9qDu-HtN8sZhSK-SU1bGexhTGg5ldWUWilw5luPBv4bg5fi0YzVN_QBOOKxexUjErIqzwL84-yRMfG58UixfVdDhdcPG79-k6Kx60WKyGZLmc9qEorhiCFPn6sUJNOXzuBDGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoAhpD1t3SgU2Jp7-xf1EGgTkdl2fhkCl7RUUF8uccl0CMfCbjMDyoHta84Fc_QqIh8iwsphXnqHaVT4U0fKy8cJ0e0Gy5Ja9npJgMHuZ0liOvI8Cj7zo56Un9B2_tPLy5mA42gQOD4MWFwKDkf1Ygcm9rl5nnaAjNPInLpMtBlEcrAd81i4E1TdO34G6wGS0qoQ2pRRQblkK9zRem48_BTCFz2hhdbQAvelS6Y9AxzW_-RZ9iX3MRtun4V72OF7DKSjjhlWycwwiPp134_9OStWJq2ihoK_soIJW359ClhhSWtFDc4VDNuStL1egk5u_vdxzWeuyxuWr-EX9XTvag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
آخرین بنچمارک منتشر شده از جمنای که تونست رقبای خودش رو پشت سر بزاره
- این بنچمارک توسط خود گوگل منتشر شده و معلوم نیست چقدر راست یا دروغ هستش ولی اگر راست باشه واقعا آتیش به پا میشه رسما ( چند وقت پیش هم openai خیلی روی مدل هاش مانور میداد آخرشم چند برابر از مدل های انتروپیک ضعیف تر واقع شدند )
🤝
- توی آنتی گراویتی هم مدل های 3.7 و قدیمی تر Leaving soonخوردن و امکانش هست هرلحظه جمنای جدید منتشر بشه
🪎
- طبق آخرین اخبار جمنای 4 آرگون فقط برای پلن اولترا هستش امیدواریم نظر گوگل عوض شه
💰
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
مایکروسافت مدل Decision-1 را معرفی کرد — یک مدل هوش مصنوعی نوآورانه برای تصمیم‌گیری که Jev را پشت سر گذاشت!
پایه‌ی توسعه‌ی این مدل Qwen3.5-9B بود و شاخص‌های آن واقعاً شگفت‌انگیز است:
🎭
دقت به ۸۳.۵٪ در ۳۶ بنچمارک رسید که از نتایج GPT-6 Luna و تعدادی از مدل‌های دیگر پیشی گرفته است؛
🎭
سرعت عمل در وظایف تصمیم‌گیری ۳۵ برابر بیشتر از GPT-6 Sol است؛
🎭
هزینه بسیار پایین است: تنها ۰.۰۴۲ دلار برای هر میلیون توکن ورودی و توکن‌های خروجی رایگان هستند.
شرکت مایکروسافت از قبل این مدل را در فرآیندهای داخلی خود پیاده‌سازی کرده است. به عنوان مثال، بخش Xbox بیش از ۱۰ هزار بازخورد از گیمرها را تحلیل کرد: Decision-1 این حجم از کار را ۱۴ برابر سریع‌تر و ۲۰۰ برابر ارزان‌تر از GPT-6 Sol انجام داد.
این ابزار از طریق
مایکروسافت فاندری
در دسترس است و انتظار می‌رود به‌زودی در OpenRouter نیز ظاهر شود.
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX-f4bv0UzmoZ0tGR8a8Qu-AnD0p3hYjKR1ggG-Myt3Uz2cXXfBwaHV2WXRjexyAgP99fNQaiTm4SLy7mncSxrYTGtRchkPyUixcgQIFUe6NNSVpS5-Gusg0pu142rEgR5N0J7KYyzoadbxg4syhFM_-s5QzuBTE-GPh5V02H09dmKZavb5r8S8yJTRZ_B-9nVwJe5xQ-qgzuawpeh17nQx2ZE34V_3O6mX2kLW7v2KU5CjTw8tLiT9Fjf0ajxF960FGh-xXWvd6zrPr7kZGD57j9zd9Ra-2qFh_9AIa2x9uFga7ax30HS-5SsiI6Q4Kt8z52QQtRw4c2bwEHU-Fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
استرایپ OpenRouter را ۷.۵ میلیارد دلار خرید!
‏⠀
‏استرایپ بزرگ‌ترین خرید تاریخش را انجام داد و دروازه‌ی محبوب مدل‌های هوش مصنوعی را تصاحب کرد.
🔥
‏⠀
‏به گزارش رسانه‌ها، این توافق در اوت ۲۰۲۶ اعلام شد؛ در حالی که OpenRouter فقط چند ماه قبل حدود ۱.۳ میلیارد دلار ارزش‌گذاری شده بود. طبق همین گزارش‌ها، بنیان‌گذارها حدود ۱.۵ میلیارد دلار می‌برن و بقیه به سرمایه‌گذارها می‌رسه.
‏این پلتفرم صدها مدل هوش مصنوعی و ده‌ها ارائه‌دهنده‌ی محاسبات را پشت یک API واحد جمع کرده و استرایپ گفته محصول و نقشه‌ی راهش بدون تغییر می‌مونه.
واقعاً چرا یه شرکت پرداختی باید بزرگ‌ترین خرید تاریخش رو توی زیرساخت هوش مصنوعی انجام بده؟
🫪
‏⠀
‏
📌
گزارش تک‌کرانچ
‏
🌐
تحلیل معامله
‏⠀
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کد رفرالا میوزتون رو بندازین کامنت با هم دود کنیم
یک میلیون توکن هردو طرفتون میگیرین
https://muse.ai/join
5UYP1O
50KIY3
EAWL0N
4RUYCJ
5GD9TV
8809GX
9XQLZN</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amOIAdnhPjMzW6mfPO3tmNtE13-sPGHmhuyq_gpCwEdslVFQSC0A3zXX0Arg2WDCkzV0Rt7IZUM5Jq3QqTHstd5bfpOTV7gyttWPMtgaZeWhOdWvBs6XHFk3VWHDcGR5aSghNl8k0oTF3JV41YFz4ooSsF2rDunASaqbIYThJiE_RMQrIvx042bg7qJ2vlPcTE0k2bCsJxcEkVTdh0S-kLqvJygKVdaOsabpPMq7QyGU14kU6v1j5PHHVNt1LOa0l1yMCQUpwLeW6xfqmPNYmGT239a3uKzphiLUHRJieqPxUj1pspOakfpNVs0raf8qMZJRCBHbcp-GboX7KA8WPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
ایمیل موقت رایگان با دامنهٔ شبه‌دانشجویی
‏
🔥
بدون ثبت‌نام و بدون کارت دانشجویی، یک ایمیل موقت روی دامنه‌ای شبیه دامنهٔ دانشگاهی می‌سازی.
‏• بدون ثبت‌نام؛ ایمیل‌ها مستقیم روی سایت خوانده می‌شوند
‏• صندوق مهمان ۴۸ ساعت زنده می‌ماند
‏• خود سرویس می‌گوید صندوق‌های عادی‌اش بیش از ۲ ماه فعال می‌مانند
⚠️
این ایمیل دانشگاهی واقعی نیست و وضعیت دانشجویی را تأیید نمی‌کند؛ پس روی تخفیف‌های دانشجویی حساب نکن. خود سایت Boomlify سرویس ایمیل موقت رایگان با آدرس‌های نامحدود است و ثبت‌نام لازم ندارد.
🖱️
وب‌سایت Boomlify
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9GsQyC8WRSxBioK-zx0bSbhQ_2Ba0LY3rbR-rX-inuC-8Tofz1edZDhcHKJ-7BbWJuLi5YxGle1eZ4IdsVM7kfAUpIxWNQfK04hRpuMpFp4e-gfXsp95yFFT6SrOv7qImm5jn1YUhesIXRg1y4NFF0bl4erZLVODM9gl9zAagw94w9_CsmHbOGQwG09e67UAvmWCJgtgzlpbdMLPj8Lw437y-KA2Z8TKdXz0M406irF8Qy_G7NFyAYgJugOfYmcS_qiq_eJEeg6mKBDh_ZL3_feZJrYvR-lzMKt8npnrwNTMK7G2AKQsqerdrkrhkOipF3r1UXuVrfGaE_ovzNFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
آماده‌سازی مدیران هوش مصنوعی برای سناریوی فاجعه
‏به گفتهٔ Axios، مدیران ارشد OpenAI و Anthropic در جلسات خصوصی سناریوهای یک حادثهٔ بزرگ هوش مصنوعی را شبیه‌سازی می‌کنند.⠀
‏مدیران ارشد این شرکت‌ها از جمله داریو آمودی و سم آلتمن روی سناریوهایی مثل حملهٔ سایبری به بانک‌ها، اینترنت و زیرساخت‌های حیاتی کار می‌کنند. نگرانی اصلی‌شون موج خشم عمومی و فشار سیاسیه که بعد از اولین حادثهٔ جدی هوش مصنوعی سراغ‌شون میاد.
‏سخنگوی OpenAI گفته این مانورها «ابزار آمادگی برای نتایج محتمل» هستن، نه پیش‌بینی قطعی یک فاجعه.
⠀
‏
📌
گزارش کامل Axios
‏
🌐
خلاصهٔ فلش خبری
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=nL0Ivi_QlIj2CswqgikI1IbJ-o-EPLrQOfnoTMthoqpd1LRn2Xws3yQejv105wFO_RYvDuadZ54OLJzCByYU5APQvdaR6JrooiRp113_DjNfQUSXV2UfhhYFTmirhk9ieGGu9nscDyjHUKMI9JxCF7VRw-KH0lxLBugAfVBPlvhYHVLnyoTK9gSmZ98r4lkALMuD_uY__AXZwdSOCZZk-33a-vD-PZity94nYdBJOQ4hgT8vKyrOH4g3gxmUdlZn-YU6tIlH3m4Nx3rno0mr4hkWwhO_0nAbtpb-HgXxwTd3WWdyqvJS_xC5nHgTxdLSjixM_7Kn5LAHfX169gPVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=nL0Ivi_QlIj2CswqgikI1IbJ-o-EPLrQOfnoTMthoqpd1LRn2Xws3yQejv105wFO_RYvDuadZ54OLJzCByYU5APQvdaR6JrooiRp113_DjNfQUSXV2UfhhYFTmirhk9ieGGu9nscDyjHUKMI9JxCF7VRw-KH0lxLBugAfVBPlvhYHVLnyoTK9gSmZ98r4lkALMuD_uY__AXZwdSOCZZk-33a-vD-PZity94nYdBJOQ4hgT8vKyrOH4g3gxmUdlZn-YU6tIlH3m4Nx3rno0mr4hkWwhO_0nAbtpb-HgXxwTd3WWdyqvJS_xC5nHgTxdLSjixM_7Kn5LAHfX169gPVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام
⠀
‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه.
‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده، دکمه و فرم ‏همه‌اش با HTML و CSS و جاوااسکریپت داخل خود پیام رندر می‌شه و دیگه نیازی به باز کردن پنجره جداگانه Mini App نیست.
💡
هنوز رسماً معرفی نشده و معلوم نیست کی به نسخه اصلی برسه.
⏳
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8JQIeDtwQTpoES-ahNOaoD6OiFMqnuthPTxHsu5Bel6fmEKiNJMW-T6p0LvD02HbxgVmCYtjv-W5znhaXCt5FHFSYvdfw5XKEyW1GmCTIMfIDRL-iJvVy8ZsH8wAHvIQIvfqmdEhUuisz-__lFPHqrFDyYE8NXmfx5x7R-z4TuUyiJO7Uxa0VESNPmVD-sBz1JbFubKytYCf_DhBd9hP6TQl6gv7YRqKqfaHdYQGf2tXZ3Nb4zjyCUtb-0yvdRbBuqMk_vpIv0Uen358D9PRD376ngSUHDyHpTq62t7-0Id5CEICJgNDsG_kIs255l5PntXg7fU-3jZp6yMSlllow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎹
آهنگ‌ساز رایگان و متن‌باز Tonefold برای همه
⠀
‏بهش بگو چه آهنگی می‌خواهی، آکورد و ملودی و درام را به‌صورت میدی قابل ویرایش تحویل می‌دهد.
⠀
‏
🎼
آکورد، ملودی، بیس و درام در پیانو رول؛ نت‌به‌نت قابل ویرایش
‏
💾
خروجی MIDI و WAV و استم‌های جدا؛ افزونه‌ی VST3 و CLAP برای DAW
‏
🤖
موتور آهنگ‌سازی با Claude Agent SDK کار می‌کند؛ می‌توانی از مدل محلی Ollama هم استفاده کنی
‏خود اپ با Rust نوشته شده و برای مک و ویندوز عرضه می‌شود. قبل از هر تغییری ازت تأیید می‌گیرد؛ یعنی چیزی بدون اجازه‌ات نوشته نمی‌شود.
‏نکته‌ی حریم خصوصی: برای آهنگ‌سازی از لاگین Claude خودت استفاده می‌کند، پس متن و ایده‌ات به سرویس مدل می‌رسد.
شاهکار هاتون رو حتما برامون بفرستید ...
❤️
🤝
‏
📌
سایت رسمی Tonefold
‏
🌐
صفحه‌ی Tonefold در Product Hunt
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=vcueB6HLt_TVqSloi1ZedkBR1uFs9-J8yLB_2hU59uvdO_znE-voRnXv3ODk56GXLdhOrglSjMNuOcH4Zt5wugC5MJ2BejBQPA5DqPOMj4jhS_HVC9pQ2ma6zihv0xcvxQlSM4QYnJzaVDjFT7JwsKbcuI-vB6sefmVlkaV7Rwvh6Qs6qAu5Ts19zagxVwZqzAe-d7mXhBZdrIHaqdNTOrFMtQZtn-CJFQpe9LY94AzunXm1zKtWAcCq1kacbg6M5uA6qHmNk3dHwCROOWcgug-ULYcI4KkGPebzq8AE2h3ujpjDadB5nNG-ZBTkaCgsvOFxaQoDV2kqsjYqiUOCxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=vcueB6HLt_TVqSloi1ZedkBR1uFs9-J8yLB_2hU59uvdO_znE-voRnXv3ODk56GXLdhOrglSjMNuOcH4Zt5wugC5MJ2BejBQPA5DqPOMj4jhS_HVC9pQ2ma6zihv0xcvxQlSM4QYnJzaVDjFT7JwsKbcuI-vB6sefmVlkaV7Rwvh6Qs6qAu5Ts19zagxVwZqzAe-d7mXhBZdrIHaqdNTOrFMtQZtn-CJFQpe9LY94AzunXm1zKtWAcCq1kacbg6M5uA6qHmNk3dHwCROOWcgug-ULYcI4KkGPebzq8AE2h3ujpjDadB5nNG-ZBTkaCgsvOFxaQoDV2kqsjYqiUOCxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪐
سیارهٔ تازه‌ای که با کمک کلاد پیدا شد
⠀
‏یک برنامه‌نویس با کمک کلاد کد و کدکس، سیگنال یک سیارهٔ احتمالی را در داده‌های تلسکوپ ناسا پیدا کرد.
⠀
‏شعاع حدود ۱.۴ برابر زمین و سالی کمی بیشتر از سه روز،
‏دو هفته کار بی‌وقفه و بیش از هزار اسکریپت تحلیل داده،
‏و هنوز تأیید نشده؛ قرار است تلسکوپ تس دنبالش را بگیرد.
⠀
‏اولش خیلی‌ها فکر کردند توهم هوش مصنوعی است، ولی چند پژوهشگر سیاره‌های فراخورشیدی هم گفته‌اند می‌تواند واقعی باشد و داده‌ها برای بررسی بیشتر رسیده دست ناسا.
⠀
‏
📌
پست اصلی نویسنده در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJhjg58Fj09Y5eTDcZt6o_XBbGQW_xhdx70keOjyE82xwvxJKPpy4h0a68Zjcwg8ZqyJgt9kRMkEUy9UHDzM7Rw4J94oNoI51EF5Fd1me0sU6KyDMmfbeM-6yF4HKmo3KiXFhz7PjOKBiI0Tkyjh26K4CRljARBMAwOkeIzhvMYDM7lDzX1JGIX3KWNmh--VyE6hlLWXtmQaPr_PzcVVe9oGr5_DgojLjM_lHUdSIAsImKa2vN5hpKomUMkV6wso5vEz_Wt8YSh9AZmWixRtu46z1qx_RMoYOF9urxLw8bYiC9EBHAyBHFbUDGs-PwXZyZ3u7NYAPYdPyzV_G3-YTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6zKcIty2SlkaSq4dkosYQjLb_OyXVsLOtCUnIVTFjQqMzznJ0LYEphEvg3zKz09IqNV7kz8_jTWfNrh42sdGpJOkmpTaSUlDABElPT7S4sChvWCYQ-FHyEurtVrSp_ojF2ivxzWUMBJbOPxL-waCoqlofH529LB8zF7Oo2fcfX6Gs7CAvPxYRSTQ3fwtSu4HUqYastesQ4l3JujeVDypIGrBIR2-dds0mUIYY_U1eFR-X_lj52OiiKSl3ShJAW5whdLhgFYM3l_Z_PQIZ-Jls-0nS-KwW9z1BLQdLBUQvbQxMDCVlOc49tviKPopygS3wAO6wlyb9Fybml6HGpS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuMD7vE87D2mwYAeQF4kpCT3vP7Ne8sm-Eq39EvEHR-h3NecFtwwT-C9FRmR4NoxhQgonUvxteFcNfxLV-irRC1J5thlBUYzh9FMCiWPuISGrve3WQJCZGMu1MlCXTDZb6zs32xdjubqDEJgoYJJCC-P5mNLH4SHhFWymumn32wdfGAVd9SPUC8zczy3RsyeztdeJ7ll7qFHjCFbirCDVm9pSY5iG4cS-8IME9sC901nSk7YkW5uts2spvuoC0vt5jtUKHGAOlQ8tHsmn5wlJy96Umd7MDgz_06TQ3y8RMqvEeJL9lCZg8g1TW1EBF9JXMKS7-CUiwLtQ2UuZekfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
متد حرفه‌ای تبدیل PDFهای طولانی به Word با Antigravity
اگه تا حالا سعی کردید یه جزوه یا کتاب رو با SI به ورد تبدیل کنید، حتماً دیدید که بعد از چند صفحه کم میارن، فرمول‌ها خراب می‌شه یا پرانتزهای فارسی به هم می‌ریزه.
ما یه ابزار
متن‌باز
و کاملاً خودکار توسعه دادیم که این مشکل رو ریشه‌ای حل کرده:
✅
فایل‌های طولانی رو بدون خطای حافظه پردازش می‌کنه.
✅
فرمول‌های ریاضی (LaTeX)، جداول و متون فارسی رو کاملاً سالم و دقیق درمیاره.
✅
خروجی نهایی، یه فایل Word مرتب با فونت‌های استاندارد دانشگاهی (مثل B Nazanin) بهتون تحویل می‌ده.
🚀
نحوه استفاده:
فقط کافیه فایل PDF رو بهش بدید تا صفر تا صد کار رو خودش انجام بده. (پرامپت‌های آماده برای مدل‌های دیگه هم داخلش هست).
🔗
لینک سورس کد، ابزارها و راهنمای کامل در گیت‌هاب:
🥹
https://github.com/faithsaly5-stack/Antigravity-PDF-to-Docx
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwjius1NvGV4WdNtNwl2LtTEQtJxzjt6WUdm5OWSLlpyYzI5NNEyp-HcIJ63KbAqcQpIPhr4H_Fmhf-zcSup7U2PQCazmDcXtduOcMeRxcGpMx-ptXLNy1vysCu2c9KbWJZ0DvIfkK0t6FBiu3VrdE1v9gf0IrW929ciptHBPTgieDKiSQvHvRT7butBSLsoXbYGqGrTdvS2gu05hQ-DFs-_IqKCOd660vYSW_-vXBVdT1IE3zB_WqVDQvCRx6O-WMwo9fFTx3DOIBOUs1emhPuhgK7tWLTbCR74fwTIBIXFlh-nJ-AjMLrMvDrQLuA1w3gTT7BTKsmxJ9C5_Caf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw_9HT9HXY_dxr39O1sGmPs3XJKdQ22JCMXcQ3IDmRO_iDrPNMaTbUjruc6rxwkdCKeskcxErOdpAnJ_ypV2DTrQK7tcbr5_SMGIpkBj2FBkfJ1-WshZF3a8gSwCIgoXgZ5AQAgfnIae2AQOmmbc1dSyg0Hc78A0FTfwtdiUYVCTEKidcJP5WXqqTHyIdQTjQ1BBMbYjyk6TTD-GXFCgbSiuTlySpvSnojE47WO41647qKAa24piAf1Hrpf4zWMhbUQ-3yVr5F6c6NIkcFpPcqYSwuzRgJdLCuzF_OuGOPIDf3mQWZQPbiHrJCeb6zh_b7vPbPdCLecjLwRQoytLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#حمایتی
‏
🔐
برنامهٔ غیررسمی FoxyVPN برای ویندوز
‏به گفتهٔ سازنده، فیلترشکن فایرفاکس رو بدون اشتراک روی ویندوز بهت می‌ده.
‏
⚠️
غیررسمیه و ربطی به Mozilla نداره.
‏
📥
نسخهٔ 1.0.0+1 از بخش Releases قابل دانلوده.
‏
🔐
کل ترافیکت از این برنامه رد می‌شه؛ اول کدش رو چک کن.
دولوپر از بچه های خوب چنل
🚀
‏
📌
مخزن پروژه در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=CzxOkfXsrhbNL35ND27GyuCZU7RMswShegmJ_hOxEYZRRN8t8yxilvEhwwAa4z85WMGqFbOAFRNiSmDMIRfxemroczlRMojFQNHNDxP1ZCyyK5e0Tgf5y3lDYVbdcg34RL1yoJhBVmA5VX3CMUYAeQh6BlIkfv0klcAojfTVcbyljDaaRyXTVFuLZoWdDqYf4YqkTEW_0QAFoft_d44mjuWieuYUsCN_DtSI2cXlXQQuBNCn7NAtEFtEmfV748bT_3yesg1jNhJymfpmZSDSRd5HJH03GLOgHwAptb6O3PxiJYojxpN5swwJPTQ6UdyIVX17cdNu1b-VrR7mh7rrDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=CzxOkfXsrhbNL35ND27GyuCZU7RMswShegmJ_hOxEYZRRN8t8yxilvEhwwAa4z85WMGqFbOAFRNiSmDMIRfxemroczlRMojFQNHNDxP1ZCyyK5e0Tgf5y3lDYVbdcg34RL1yoJhBVmA5VX3CMUYAeQh6BlIkfv0klcAojfTVcbyljDaaRyXTVFuLZoWdDqYf4YqkTEW_0QAFoft_d44mjuWieuYUsCN_DtSI2cXlXQQuBNCn7NAtEFtEmfV748bT_3yesg1jNhJymfpmZSDSRd5HJH03GLOgHwAptb6O3PxiJYojxpN5swwJPTQ6UdyIVX17cdNu1b-VrR7mh7rrDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owa8iBLj8pypFCxNdYkPs_YY2-m40GPcVJwudhX6rZ-qb-asKakn-662TTbgSMwsTji8XZtgeAyuAadE5izPRYIamIii7-9KJwF0bnyPVMsCdYLt5TS1R5W86oeoiQuskm_nqUwiX-LV4ETOm8gRSpiJBnR9m1u63dLOpZUgaGXDxVR92Nk3e-t-Nb28HYRFSEyAgtrLql99yoVkpKo0YScVNcGdkThGZwEfqY5yRod_LLZVo-A57fLUpdFASU7shFXQjFfesDaKvsXTz-PhszAAtPiieB7s5Tw1yCInJ4IzsiP57yr5KdcZAoOmeLgmw5Yk4hu_PMskB2mc7nij5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
ای پی ای Tooken Club برای مدل‌های معروف هوش مصنوعی
نحوه ثبت نام توش خیلی راحته فقط کافیه ایمیلتون رو بزنید و از کپچا عبور کنید ( یا باید تصاویر مشابه انتخاب کنید یا یه شی ای که خلاف جهت بقیه حرکت میکنه رو تشخیص بدید )
‏
🤖
کلی مدل داره که میتونین استفاده کنین چند تاشو مینویسم :
claude-fable-5-1
claude-opus-5-5
gpt-6.1-sol
gpt-6-astra
glm-5.3-flash
grok-4.7
🎁
10 میلیون هم توکن میده برای استفاده اولیه که بنظر کافی هست ولی برخی مدل ها ضریب دار هستند که میتونین از بخش  instructions بررسی کنید.
Base URL :
OpenAI:
https://tooken.club/v1
Anthropic:
https://tooken.club
‏
📌
سایت اصلی سرویس
‏
🌐
کاتالوگ مدل‌ها
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZAkmkuUj5yl7kSBw_9m3ef3F8pkuVpKlL6UF9yP7_RPKvc7MONBa167xBYT9pD-SZlddKhEyO21gW1-O_TkqLzVfO9FrEWHFKdDBlra5j7wjUe9XQMUw28GGx4K-e6EAccV5Yt4gddr1dzBbgGzKtbBKvPhoo3MmHVYkA4b7Cz2ZNk1DzPZ70TW8B3YhHmZ6bcEb72DH970CHSl9nddrOaGtRlXfnRFgTAMe_O32HmVgYr07VaGQO7a5hVMFoNzp7NEqkd8qI36ZQ9cjWS4Pezy71NPYxni6RkrysMnqgAHUELpA5eq-teaxk-jKAuPYKVov0ZHMWpHJKoIl1Fijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-4iR0mkHG19YGKZEf5HO7KRLFzIN2m5VbXT3mKLzglia_UaIZyWnRSP9JW8_PETFVcArzgXOkm-gi5IzG4zDkkXAdAA8BD5Q--pazMPXipbym_kg375n0AsbvACfpEwTlxSi9Q7uoD1aNLRz0xAdlwrt2S9J4SpZBOIgO9yI9WzQZCHMC2f6AIihMAZ7CEhlN7kpveQyaNr4UUHB_Hl-mxDVGvql725xbgxspNGm6DDSRI9Pm-nHOrQAqAClXwRrjspbhN7H-5TefXD2MghQAa7ZBbxYo-NVbf1ZsMkzsLMRRluaC9pdMnWrxXE11aisk4cTC1MyonzHyurAIakGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها
⠀
‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده.
⠀
‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه
‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه
‏
⏳
اعتبار ۶ ماه بعد از تاریخ اعطا منقضی می‌شه
‏
🏷
روی اشتراک‌ها اعمال نمی‌شه
⠀
‏این اعتبار فقط روی API خود Anthropic کار می‌کنه
⠀
‏
📌
فرم دریافت اعتبار
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=Zb06f32Oelvc2JPLk4COZhPLooBo5N9kZEDEWM6PDz3xpHmNGPboLRSfutCHZNjTYhI-d0jyoE26_Rl3QVtPwwrFfgE0-rbUvcfflKlm3H-P1wIzPQpebEFyM9v_G1A3fWtmqXIJ_fLMGu4bovXwaAk52Hd41ypG0VQej5VMo5WkKXoOBNhr6Ou0e6mVFh38IKNgFIQzLOZR0wl5Utei1NIJ_DysYjNuX8G0xcj6fVqYEgCNpSEGAwcIIWeDeDHGhuMkHOtPRhLYA75q1BDInEPCbEPnNpKC3GhoqqNVywgk--zKGVc09o7sN9w2lmM7kxQkRQz5R8jdqP6zoNcejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=Zb06f32Oelvc2JPLk4COZhPLooBo5N9kZEDEWM6PDz3xpHmNGPboLRSfutCHZNjTYhI-d0jyoE26_Rl3QVtPwwrFfgE0-rbUvcfflKlm3H-P1wIzPQpebEFyM9v_G1A3fWtmqXIJ_fLMGu4bovXwaAk52Hd41ypG0VQej5VMo5WkKXoOBNhr6Ou0e6mVFh38IKNgFIQzLOZR0wl5Utei1NIJ_DysYjNuX8G0xcj6fVqYEgCNpSEGAwcIIWeDeDHGhuMkHOtPRhLYA75q1BDInEPCbEPnNpKC3GhoqqNVywgk--zKGVc09o7sN9w2lmM7kxQkRQz5R8jdqP6zoNcejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBNdQ5XECCnnUuLWkyLvCmWcSLkLB5qyGSwhjK5FVFyvuGc9GKsMqCjVP82wkzbi6X1E4Mfu-Sj6q7975W0N1cNPr655bPLFTCV_rjCRlj-tqC4l6BR8VrRBl-AWM6eUcOyO3JUp8_R821kZEvOzWoY71rSaKpLHCIgAwcWNr95aSRe-55Wu30ChhCUAzBK3kipz8qrGKkRB_eQlniHxQoyjkbbFN_EtNUQazP4GGo8NmGyawbWXgffHJmTbUz7w0_7-uQuIk6ApHfLJC5piEKvKfVlGNN0lrKdeIlck2uo2DFVfJ6u05fWtZJbHqTWEFpsYGUa5oWV-ggmuzGWn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIdASSMEDG3uogrg80A3CxYI0247q2bpN6mIlH49P0I6kDpVXLuwvCe7yQOvJPEF9pX9vbuNkalHIpZx0kXDP4fQiJxrnVAeEh3nz-8JYjlDUcsWWqS7qx7GAFPo1XtqHn4DDQnx9PAIkZczsPx6bxueH2i9Aav__S2pIn_v_g-6SwgURosoIDS92fQ7ZzpIP4cQKNEuFy8FbnCkx6f3kMFwv_1RwurI5isWeUJ5njrdHvm2IwDWWcr0WPAaS93p92EhrMG4p0HAcpkxTxXdJ2gDZZ7FOlegcd18A7HELvuBaHa953Je3lF0vaOkdpoiFl5KJ8pNQIsh0lT7vXaUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMUQZEwZq3mEIDHOjzLY0OdNvq65RLptcRBK5uIAH75C2_ythl0PWM33gqKmxm9L-hM_iKNcPu9tEkdJa4g61mBVPCsfpbsZn6mC7K3nEMhnRUdsu3KwTiVa_iq9Sip_XyaD6vpHu6LVFu1S84XwaOxfcFWkpUF5Bw0HNyUyFGio45bZ6p-bF-YNlQIhWl-jvdSurhkX6WhDdQEU1ZYhHBwaXppvzF4uaGAq9CO-KF-s9kDxsyw-V2g5UTnXTJzpgix-Uhge9UqWhEUPFkKs15viIreLScCUMrtSeCRxlXxmLXo7LnGeFFF6Wm0EuhuWMWHzE_qWXaAUGawQwe-EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scEydFymBOIDsRh4--dOrMODh6lw-1EPtrPF5YnOAYLsE9Bnh75ev97jsd9QPcwZ606IQDsptDSdYbTY2nHwwrjISRsnP-iDywoPSj0VXRD13pWyxAXqd5NPkrldVXMYodyMyA_DoRnVz9KNXu4CfrhrPPW8-bhiBorNQrpzErlBZncvpLL2gcHYa6DumnqYX8sfMeufEz3JBFLRixbkisMzIaqNd5j2EMJdXVCp9TehxAA1QwTUCi_4cVNColNcigQLFZKEvHwLp0q4i_uy4RV--TQI50itmCiECGcQlvTLIBmRSY3TeJaMV39r-9QBsUGzGcOz6s8SJaNjU5ctYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzwGW0FS7ezXUZ2Lfp8vZsMgdjaCd6KSTO2jS7HVhubX_3Q5bDTSqstzg8F7MgL8WCde9eFT7u6UphhwPsJwbdXQs_qhmcuxz2JRBIKn3z8605axx-hy6fbpoVO6YFlgM2-koJfgwTSWZNIxzRsP0ObnhYYeq7V51wqjZSWgf04Z8OVP57iui9knYH7FTv4ft0vAz0RC84bunlP_sHqEF-qH1QotwYRO2bC63XEOXOQvcjzpqV-ooLMqVmrjYhL_Te9jZVrHWIOuNBINUnpHwUsgTMZ837cYZe0Je9YPb69AhQ1HLPj4gaP-w7ys4BSfCkSK4Q3hFiRyMvjkcx8D7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVQyZrNBzRfWbQskwowrRuHyjYc90MPJ-cZQLf4YAJyDo4I_8qXsaJs8U6_KsXZwC1yARVSHXJWqTI6FCgfikdyCKhnmPPNCPNa0QSEZyFHn9qimVEnGMH_7DnHpvuCvO5ZamcS6j6BbX6rDEyu9WAhDa7AwK7x6w8xtlBmf9az7Vrgb0XHRhKdujmD9gUJHETZdsBnnfPrb08CmQ4X7pxR7GxhRaohDP00oOpsLTUhMiByK6WZiBMI5M1taP9yX7ryCrKegfDQM5zqrzMMWL3hHilG_pK4zMEq7p2kJr2SHmy1Y2l3LwOJTfkI4bq_m5wZkR06zIodZ0eiawj_QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTtIS8DC5bwiey4M3vODLnQOn_dZCGWyVVPpsAL8qLTrC63Hd9ypfN6xbgoQERGIf9UV7dDp89HePnHG6PzBhJtT9li1KDnOjWdSdsVvvWc1znPog5ZAfEfLu6J1AL1NyR_2N0SYCTRaz1SuqOXMDYIVSvnHvRPLC-sxVjm5xz8cobjVJZIvzINZBsB792FlpV8nGgOKdQV7xFhpPcn0d_feIXTSjzwM2x4w0EzPtoeAX6B79ic1X6nTAVQdAhYcdla8-l25HBTAEya3__6iITjhPnkp0EpbU-26Nyk-zrbl7aD9tXURXhbXiMJ-RZL1F8eD9xavbw05Qr4uiqxk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyOwgabL5Evez5FOuxDB88Ik7foFfknzagH3oGg5fkGZNt_wuE5tW7aXb-DEZvyqdTpllmYI93mqBjDrmSWTAtL8R_sk1HWQ3Xq44FfNsl7F43BSVeaWyYOCOnZoubhIdUMEUJaDFQrRuFaL9ZIL3k8pAZbtylISvOpWMdqvwhQlDvMbatSWJGcqWYRisfn7HlXlcrSMy6gjmkJk4336TQq6PNX0Jy2W7cB1s-wqRjf9wwTNWgCqSSUG0NiJZ2p3W3SOhJh2jkGH6u3MiotcyJYf2p-2NsM-x80A26Ip4CM87c5anrck9aeHgDdCsT60tzj8xZlBp0fvRPa7ZdBLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhG3pm8BQjHF9y_BITRJfRM7WEfHQVtMvy3pEgfd_TJ2lW1jA_D2XN18SJQrM6n2aAEnD8UGbqBhR4xEWyarxgoqZjNNC_ZRnvvUtL3mGegR2bSRoRSDN3BesTFB_NacK7CK3RfuBb0bRBWTqZdsLI1sVO0sGjomzCYVJaHhXHi2oAGca_EREwVYM0yjZmrdqHtyLrpm7G0lgSDuPF2W_-wCNG9TxKidwK5iU1IqOAiLlOZ4HCyyxD4q1QxIY3dFMC2lZzsb6LAtRzTqfbO9acuDkdhVPABLNcG7CL-HqPNAFz1CthAZO5wuN_KxR--yZHvLa4-QMPBPRiqupokv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_sTXmczXAJnfORonybvakw02b4CtG5kbn2Diduh2OMt9l-wHcb9Ng_AV9Vhla8vC7dhcTHGEUBrOvc_putCGzeRVtwx_LZoe0l9oklB5KL9mcOvpv-BCudzt1AiJSfxzZ6TpOqItN9W47DzoS38-Q9oY73U3jnyDB461IZ7Yf97S8GL8imB2vwge2QmHJUmF5NdQ3t575TMlrYsXrIrtg-Sbflq7DP02Il0YChAtQE-bes9K8O_mWyAotUZPffmPT_Xhca31OrOHnybIuylLqT9dEFXzAUFv-eWcAfJTw1vQ40N_cBGXQ_xsZak6QtRZgns0xR5HufGPh42-29A9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEhHyl79n6HQ5ABnAIk98BBDVvdlYE6Pdwa_-NPGLxq3vfR5LeFcQUJ_sLC4gJIMtLot76FrMox81Qhkb2QOWgxKQpjQSGDJJYXkBX-h1mGXvRAbGrXPaLbhI6xdFKgLhc8cIXEzT96ygpiuHLHosqMB1Rk6KeDMt0WqRYEE6vK3efwUJmE2fgupL0yb7mwTduAOfIUFYTgE5y8TF81BPpyZ1GLmYvn_0OtUhyI9rvqMlcNHkWGzPxHknNWmAiM8nw8-TSD1cGr8_kcUE6cLmHp_0kQ-lo6XDj2l4axKvRci-NK61hsSoTFrX7vhZHpCOJLXz-lhQG2nZ1HwV4nlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQuqCJnfN8fhwmYFFMGfahb2cRAcKj1zOMcJc9KDloJqd8hCx2Xo_mHCH8hmB81KjqD2715lJXu4Me8Pb6zKNNbTWSeRTHjPLpbAw2Z1bztaS7o2a0VPKrUBTxz53NLJ09KHkDef3JeIEA3yFysIJ-omkc0BgQtnnmiNeybpqGS3gxg3nd4ub4ogq0mJXQ97B_ANNhl_eok0KQdeek2X1aVKQhEeFGxQNMNMtVcWmJEALFrpWGmDktPiIsd3-E0NsBZ-aj9f0SWZo2ZE222R5Ll4hJepv-RWr2Hmz3smk0PNmDlEUNly2p1h_ibY0qsNJkYEucDTy61ZBxF5hCXlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQDqvzuwz436-ECoD8WxK1j08zJ0wdRAmtOTN98oI-nhv5tLBEDque5Y0a6khlGLeEWIaZSVmC3G16eNFricEZDbV8UF4tRRzqsAL-MjZOIISt56-wSwDq88YK4m9-6cfXP4TSyh2QnBdCReMKX9fbzhFoI3X4RK3CONSzRXPt8dEP7n43EVbXCER9e8MlGqs0WJHgDWambV_9C21JvW0fPwqMH_5j_zparVOoy7Lj7Tic8-UDoKbe0PRrJG2knDIWt5Q6_1RwDz-nqszx62kspN2kUebs88M0AYpidbP3bBcCysezO58rhVaG3Ygwz6oLRuxT58VjQAxtaR2pYGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud3p35gb5WhjZuVeinpVeX7dp06qnkC4UXaieTsbq5Wdsm06FJVaOg2zbkfb0E_ps8ql2Zaerhn19YMr9ZkkKx35bblFAXATs59RAAVnMBVbRaLCzOKWYDQ55ouo_2sYvx8x3pNdB91D7ejRDfGlFH2bwAum-omM3UkMYiW5OaJHM59IRRIOuIe2wUK7dXMBbg7hHxCg42cdek7dEYrJI2ZzeGPJ6p3wraD-VJ2uCwaf6ITF9e_xYKywLGC0OnxVZ-I50aZ3rajc4L-YirQPvQBobBzSIt_DzhIWw6UYhnIbVIlWKwSxvPpFBaUKzn6JEbP7Nm81E3QQkvj2Ozic2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Xj9ZTuee4L5w_xDGgY8gh-Wh6ZUnr8BGwy00k9ofKAp85kdYWP78EjYDt1vQnT4K6x0MewROrYNltL92P7X_oC50iX4Vkn-RSaJiMp-rIUsNhw61gxyVRtRqv83-NQGIR58G6Yrmj4ETcaCVKgMCU3UGvsEXugzmLQD8O1UWqyrtoNHXPmfFDkd4c6vukv8qK94_NE8MF1ihLeSxmziI5UDZ-NFQm9JGJ9VOhHMZj3cOi6Ga0-8bzCzsu3Sbt9nIVLFc8v5H6JsARXpwjTxQDmVWy_oa9SPCNUVOjGTX6fKPZQY3KhR2d7fV7-z4wPU3C_zu1RdpoSnVJPar8FhjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Xj9ZTuee4L5w_xDGgY8gh-Wh6ZUnr8BGwy00k9ofKAp85kdYWP78EjYDt1vQnT4K6x0MewROrYNltL92P7X_oC50iX4Vkn-RSaJiMp-rIUsNhw61gxyVRtRqv83-NQGIR58G6Yrmj4ETcaCVKgMCU3UGvsEXugzmLQD8O1UWqyrtoNHXPmfFDkd4c6vukv8qK94_NE8MF1ihLeSxmziI5UDZ-NFQm9JGJ9VOhHMZj3cOi6Ga0-8bzCzsu3Sbt9nIVLFc8v5H6JsARXpwjTxQDmVWy_oa9SPCNUVOjGTX6fKPZQY3KhR2d7fV7-z4wPU3C_zu1RdpoSnVJPar8FhjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5B1wX5bNVF8er3Hn8wmLoerrJiz12LIMVr5RGumXLJNjY2TxmY5eidFRGtcyAO8ihzYXcXxg33OXXWasnjpCizKy-UEnosuSC_akkZ9MNBG_doUeXvAGIkgAeBdFWIkfDHsQJ5Y_xrVWpb6n9w7hDiU-oWRWoGEntsr_x-4o0anZp6Xjgx30VbzrfDNZbKOVYF6qxAu5Kw2nNhmuXYRu5nqc4LUmowtAIh2FlcSaeviZPpDYmYVFayYXXPeOeVoYD34c3MC5WJf5Yewk-7-lBlnWIbY7XsaS7T11HNTtnDzG4j9AdXuEcLneFGViarShwJeAKPgIVP5gXiZ69FyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XT6UmQhwfZZedNGptPEQvGe_c-_dv4EZriVqcljhJPSTZbAKKaxjtjDe46oeLPcNutynyuq1p7_apM_8yrYN8lApjUYMztgXka4Gr4M13ybH7SvATXOdZ4RJ2qsTuSXpj4-cBX2HuUPZAq4-6-SpraiZclQ27Z6Bz_TXt6W9LG4WSe_rwZ8_erjBe_zfescSPZeXpE9wGo04fYogbsOU30hBkBIrQm9J6w0R2II6hdxcGum6fNPkv9uSVwHPOHBhfqg8kr7pLCt0wznePzit_vhK7hTITjMBBF7m4RgZGGKiiMwl7TRIqPDqitOn6PIDLuuFi__61y-cQxqZDSuCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig2l9ovcYEGeQTpKyGSRdjILvLiKKFOjda8x1hd7qkYRUIo8MawNie0YrFUZ3eGPR19gjufH6qdMEZVl7zHUhi15qFRQjV0yi0KsBJ8gk4S0GNHlqEEJpYiSwG5iEiHEeRnil_-X0Y-N-D7QOv5tHQspC6o3_bxf-nea1djOe9afe0lt8k5LCWYjdF5b9VI8GVC7dKHIJndrjSXEdTYSKlRp9eneeNP8XxYiMmGprfjb_pSNsi0sdYy4KHgtVswRS7xUCKHh0KY-3xUCXzKyRB8CX_pBbgrvWEd8flqjpJ_K6RUsWUkOo9QsCt5mpb4ZXAkz42GF8ssQuuyCvtMMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnlSCEHByYzx1O0U9j7Qr16Z9NAyvv7938NRFJDmOW9U9qV_tQ8fwufXR7KcTrwG7-8J6MhKp4cFoeU6NRGN-7nu2U39lAX2Bl9ZpKoNEWblL4zwKUDaWs6E3exl7VvY0hulSWKmLWdsUWo_ww_luOsWdw7oXQFT7rDJYnvkjdbeQDl01GUEuw6g7V_t2l8aDb5cuHdwp_EU-plKb7X9qaKx7b04EspnnPcvVxO55QJnZQaF93pRMrtHYvIq-G8e6gjcSQFZieJA0BPO1wwiPl0A2aFaJGAmzovxA4-r0STKq6XSf0XaqmjmiUbTl-fV8ly_4WwhnQEZSy-CPAHZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZwxMAwOrGxQYT5KRR4AV7gH8kmI8mI1g9QQ01CZhEkLi2yrzewAIGjlNnlyfBMAxvQoYWevT3xOYzyOY2F1jThqgoXDUDsvoHet4kGcwUZPNjWf0QfiWhgo4tYmKgq9NuaYU-6KRSWztpqVswguCUgl50TWRWE29f5AtgPBP11i3-GNpQ880RwYa6aoPPGwbiJI879c45ew4bnH0ajD70WvHge7WgJ81THJsQtrKYbg8BynMnPzGxPnniUWz3AH2FyNvzqlQMsYqtxSlA3ssP2mRyjOeN7qY95AbMxxEeIv5P7e2WUxm9ja3CUD5wua2oO9Lc4C6kjJyeSZHJXsBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn3Uoxujbc_jAhNQS6wyvPWZbVjz1mAKLXoSP2lZKICoqMfRaHHG5V2g4aEVxC-IA1LefFDvdiTPj6sLJNAOB0pZetQAA01MLPq-5p4geUZhaiLkwBdoQE0VTvnIWxk_yLS9FJHtTXIBTNGvmkHo0Uu2rj6M_WfnmmCCfGcxDWYTiJ_PzGDReW2bZ2qjlAUfzhpfbGWhJmEHp-LcjAk5FU4nozpLZ8M0z0COcW5FzN5b-8JU6jerC5SUYAfNcoEj-UiAtWrmIYszA6pjNg7K9Dmn8-lZkZaemNDtftIJjtYTBu4Zm-UDjuVWtnBRizEEzTWm9KP2yTHt2cf-PSz5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFWjeCMGGFuhyP_W4r-jj_HDaihi4NvIKsWfScWJEvOg53qFxbpvRx9KjMSgp9m0ooXztKkE6GnHNc-R39NHbqpXu7P-mlzlVE_kLWu_B6NMk--B1hcSqs0FI2YyNkSGhs_tMnc-F48lcj0TYToWG6PYySFeuXuEmlBHvEDFYNbS71RFBKvoZ7-n7Wl_5g9CjdD7H2z6GNgti3WC7JW_VrC5LxsbZu9FZ1xFfvRDbtq0eMjZ3ssPVQ8gFVDp69CgBEE_t-k5UpITCh0Ncdn8H7AY7MJXPEwE618Z80jDCyOsIfTLFHWZ-l3Y4eP6bvqbRJxz-ZXzdeqXJFautXiQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JgvydCKvz2ZDu1xnznJmlcV3R0SeImINEB6wcmTlwTJBzizpQQeW2jCaKsmcV58a2cr65xGuuw0Iv7N8ISXZioQIucohgPvwapcsf9xtghsrXleeOgitNKo5lgQTEokpvmZ1S2q4RJaobTFX45vDfIZl0QEPrpWu8m5flq2Q6btjBw-S0-a4JKwORv4jqjIILGmDv_IAhdEtJz4e7qW9N0dI3ib7AyffMzSgbKxcp1ia9k5ePXwahsBBSnfvZso-5qMIt_FK36wALRq6mvi32Vxw50-ogrE-CJb7Tuw2rAWYi2Zs5d3y42pLhh0k0tTUsjc_m01OQaE_HWf4HKCoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihKoFiGdCkwZSefWJYJWGoszlU-WlmRa0VBvGNlLzrIUrhlwDbKND5ILi_pSjRi_IvMtE5oURDS1y-4iDBx3iW9YjcjM5gHoKqMky_0yIb6LGy193jLOCmDPcJeebQkZHaan2dOX5VAWcP2OvXS0Lwc0fI69CT4pU3FNmTEBEa4wlej4YyIuxnZUs6zo3DOebVCVoqyJtVaM9akuO5bHwDv9aCqB-TjrMSItp4m2XSJDRqrtJlOCTE_5BiU7n0ar5FfSM6Z8r8f-Taz8bZdTlgC0IN1H2hiGdBQuSL8q4JvnGbKbvYMZs_q46OF5ql8MNbx9-G9A_mS3FmJWR3v7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVT-XpTrb3mfgNuvDi_ACLZno8S-h20kqnkFMSNzDkNlOzL-dmLtuLpjlxd67Flu5-vgl_wx_-DfG0t6Ldjd6nhB3zGlocDzn8LfD9q-VlzubVi9-iXhE8G0yt7Z_nMc9_JrDh_gBi8m9H8Vvq962eU3JtD8ojyRtx8i2GKRwwyGQWUout1PBEtsjXojRI8nwHanGaARx2MwPB0Qyw8FgokKjxctT4E0YnOROkR1PxVRlGcNQ9-u3t-p0D2AfaYCogLu4boD9M5dmYdhH5xsljKFGPrLmCwJ-GYqUnog68BgUmY5rKc1BoZ-Ux072mgwU98KyBSNbaeutYIXopHIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7bKvN2n0d79g2NI9UhSu2kvUSSXSxgusPFZlDF2TbGPLhkTvXJbJsUjHgYMyxFLt17IQ_c2iTAWgCE7CpfxA9IYrVyCmmYOkv_0PKFIW1KUJ8Xq3m-3a4wseH_Ae7awVwQaCXViwvxEH2K1mwEC8EDscJ-bOZa_Dc5Y18dIqZ92LaWUyZ_xYxHuKxwS9wXbOOSEwjt2W_TCoWlRF8jbHmlrEcNUz1o_lWhCQGa3kXQheX_kQgtO2PjIVe3bnUNCKhBtnZvNmtPrX3tnreHiBazfil90QYuBmGZmPG1hfAXpasjiZiGRLF_t3KyCvN1DYOjj_-VTNLQmSRaU4QgC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8FmchNJmpUwJaNevzWq4mHFBGjcjqwoJ_q6v5lxLqvlLPQ4EwT6GHFEV3f9Y0pqMbb0LAWfx01aAUCVFrP2SWkUgbvkg3CULBTtMm3g76sbzPdoIgfyBzz-Rg4Upt-UAbSImMk2jmkGjGUr09m8iNjIAsyszIL_oSHJAkiNixFIvfiyqegzll-vu5E6ysERocv2WfzRA_B7QzpnAAmllb64-PoOkgAAPIao8mbEfT95ciuqdWZkLIXfOhYHnJTR1zvUoAQBvGUvAZvTTPHqm7HfcRULShlcFcf5Ee6mopXlEgTNgzxblaU6MdDsclkA87qo5Vcg_JRE4SRXbjLjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmSe_u6JtFa07NMQ9WlP3Kj-rP8-SdV4HOxTsv7NQE-HK8qSvcA4ihkn4MI6sirRgQi9IBLSqTlB5LOY6AxbP-nie8MJxQjPBCHtpt3wnK4sJohOTqGe5_7RTt5dFT2u5Xer3ddGx_PF9ETntU4xQ6FGXDKYKZgtrkAn7jDvJNADva21KOrH1pzvix4iBLQQVIAqTbOQ6WenPn0LpzJmz9KFvywyy9jfrkpOX-7HBhbQRiJtRvEYTjlSOytgcU9iRUg1ixB3ynZjt5U8rGCc70nDWs0UVWgYkX7Z3cSjbEPOFx_XrVcL7PxlahWGEoiuxsqPokFkpFSZN6E0US2jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azXkqREHctFcPHJ7lFJTL2EMb9b8HVtIpkWT-pg8JekewTLRhKTC851xYYvgxxoR7IHaL50D5rbLkmW8r-GphAw6bWma8eWk_Jxd9KSrm2ien_vGJVd4swrls-aqlQL8bVJfG-4hF7yfRhQp0ih9TdU-5h1T6AEXhGAacN4xD_pa9bKkwYqHCzTzIGxWwzHw4wqBv99BMcjparfIdvt-TZuiqLo2uuwufyjwm7RSPrHf5_cui9aeJffJJeu4kvlOQOx8J6gOTuTVntMmUZA2G56iYZfNynQN6-lq85fc9PNshUbzvutx4WoIQ00Fus8bHkDeM2llWUYatNqENN_gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRHO7JDPK2geKhVfjsYblhjnMaWnMTFdLnUZqboaGgkZ4vTs_5jhKiPna6i3r52q95UUy0nhX7t92EboaJDkc_7-6LTuNgNoGGFuKXfw2Wjqab3iJGQowI2TEghWFSqZ3Ngvu-EbI7mSIs1eEGXPUXKke8gZgHGl7msi_E0yanmDdi5nlGHIx4Qj49y1IMVzvNqxtqwqDHYur0p1UixBVN2flFolHMDtVFAunSmBjhdGvE78m3p8wHF3698NWvev0LyGqJx368hUSipG99Y76Ls5R5_R12Xnegq9gX3JJF3W54zGNvp_oFKzaZvrGtWV9hOkiT3X6cHzEFhoKkOBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcL6xgm5rszFMPqcHh3oN9I69nvJfRtK_jShaRQp4b05XyLPOi19aw1oqOWey1aWMP8196k1tnqUaC6ifE95aT8zb7kYRsPtZUZlA4PjnhcPRma4hmBdgvojyfdnX2DDT4_L2ABQztptDac0to_cIocGChlut5mw7w27Rx7uT4Gf56JSO5D6j6hf3-y_Lkftml-ejRzTWx9v1yfy0Bx5LNtJ5ZLtstAD1Gn_zm47exW6pvpW5Z6LTJl-fAxZkRUkIoOcNxoFt_AGql-rGcr1Fp14twP8dBIfPgs3iZ_3wGhNa79J9OCgCUfstnE9f03IkOMnZXBuIDbNg_e2Ol5srQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DojuKihBQ8CCdx_4H6cDepVRYMrvBEYD7e7rX9BCY87HGgevYUTz1egzmJRrCBLW4Bf6jfDWaIXECCDwXPQp9J0Zed_YRHFt4IiDb0ATa7WFni7weSceoSiQTlYNJiAkK2wbBjYiAKFDNO1dhB4unDX5iPOvPcLF0ZJPmrk3uUIKodJd9WnV8HyC7buqHE16miRqeXdvOi6mCJ1jIIb_3kla0C63D2gKzHOqJ-jVStnUEI4vmaoOApOP3RxWtr89_p2Oi5QX_zkl0nSowlxHCFmh3f4n7gEK95PqHkqBOIFgTAFzToStT34S8xJv7N6BP8Zpp8jpx0NidMd_GgSY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtVgXgmCC0NwQbO37K_OAewJ3-LXXxO5UEy4sneBesLlvwTcGhyM3wYVZ4-jtL2Zo-R7m_ya9o1G8eTVz1oWt8JgKkwR04xfjR34kP80FtvCVZF93-9j1Rw-sdoqUQ0VHDsL47JF3ThkYsHrZ_2DVnVkKEeOCluQOviRRP-r3sxiPPE--PmQWXdC80Tkogwf2i3ZdyTtlcZCoiF6kMRfpViO1PkMB84uSja-7GivhWNmIbat7CZg0U8apgkFxdiWqZihsARAK5YBN31lbyRLO-crCnCi4QsQXS8II-5Qf-69jCx-7YAANUM2YKag6I0SAYzU87B5AgXr-qGMcrFksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7D7fmqkNY5pourKUdcLNAfQHIVJ0GB1R6KCImMCdexpGUIuEP_EZfI4txSx-9lHZNxr2qbkYL9KpZkd-ix003IV2sLfAdLZ6o_qcfA-Rq34voK-pGLGIeo0klv4GDlmgIPtKN8V7yGqjBpdhbU8DuP6stFTrlZAdCnVWnNDphMf9LLdcwAts0BBO5GDs0xasUP7HRrFL35z2epd2H_3Vbt4e-3cxgzMQyg1iSsG0oqA8yRXbaJN3WpzjHs9XNm-wyZIJxGtVqQt-N1UGtYHrchpe7uXjybbc-4cVd6svBGd7Lq3lZbYmYvDu4wNrLEqsr7PrQzhy6cZheNC9lWZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Om04wW5rGqujbMcB8ITpRt1JQmgdsdHwSKcm8dPqi4YlsFv4Yt2pxM9wrvBbm7PuWQV9chAGQenjccjBBhSy137CE5LixMVwbKU5fbJythUQ5ZM-gtn6KTcayKnVX6Av6mS8AaiqsqyTdCptEpUKfCsYzooRg_4R9EcLun-klIo2jxdor87lmAbUiqDRaqL_Dut6EtE29b-4dXs5MkPqs2F87zlHMFpcDDOboF6g7H1kDNBuELp0g4RTFmkiDbPF7wc6MLAhaMC2bgbmN6nauM2Re-B3b5xYmjYEVqgq-uI7som0Gd6VClIK1SmwNBsdPHiGtvpUNAcp2UF5R3lkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2NYrONlXQ1Pq9oeXCjrdFCamOTQEZiztlRGbaFwdLswCL6zOR5-BYtSA2sY5hZtJMgd9gEr7Im8lTrGuxOmiF-eIbq8CW6UO2HtuGOmHAaN4H0-x0070k9U3tGfFfV28Pwfo4VLYhQ7tYB3AmRg7JJKTZjF7ES92KNpIIND4jGmlnGHvd7Sgb6xOAwQSWvwW3b49ThqR23I1lHU4sGPp2J9VK5t8ok0RK_utM9cJOhJZzEbZ1vml-xtv7tlgVZylBOvIh9E4yE9XEdGT6V9pTiX8vdDUeJJpKwEj_SO8Cg5K3AKqQrLpFQu8xtSzpLIArvvWihdudtrRkeTmT4o0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsfN1gr74KtmBBhjC6edI0_hDg_Utwl2bJEAt7shnT4t8BZMEJOaZHBa9Ifc5zcREC-itnA-5Q5PdW-DUvSaI_upP-_u0DVWPSa3MxnCm5bQ9-3tFrpYEXz69PTeWYYWGnDKoVnBuSIEbjZ3faSsx2Up9U388JKL_Mnh3YkxE7rSXzIsz5GFWF3zrzdEKaAe2miOgniNaTvTqaU8cZqrfyEHNjvqXZ42QiFISa-ZhsKyjW1BvbEifrIpP5nAdrjU_Bnv87LzY4zONq4TuqcxJSi4QsqladrAZpgA7VJ6lMtdDeLSgL7sWf7RHgFWyB6Wt2YoPwmZ3r5wRHEjvDNoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN7ZzArIduuo4dhjKkD3HNDYCA1QHbe_NdfzKxwIuFPIn_xnku-XEIzchDhNve9CVUv9NsfR8NeTkqRERNhiCmt9KmOMRwdESj4U80pV97L9fskLOD_4rEQpEgHimkdxdgQXEObG5fJDPLGJohRyCRhxuC7sfYroLDJSZr_kayzx89CiXx1BgeThrRcoY0ag-fA66309RujXr7hL6S1ChbGoWvSJn2IiiB15Y9GvnNB8P1sOrDOthLkx7GYZ1p4mQK-u_J6C2NWblqCNdx8izCHIL-yYf846gyqqBt9kopTeVllbK6ylH5Tsa13OQh23BS0119_b6tfEzq51gPZYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4TaSj00mWowXeJjMhC2ehkhJSh-7cN9IL2Ngdh2HLZpaeOR9yqtzCSDS5ROQiRdpDy_0Gn_awaLktvYqeRizfaZg2vDnEQL0Cvid-A3Nb-Tkq-4wiHP7oUDnaZ_5k-AUwLMRtAwQjGISvXNZhEW9TvQEFVFvsSLvR1ftfJau3pjL8IhoDTmMrFgR79dex1Azh22oWRcFuQLbX09dSPrUr4Iu1xsK206ZWF9Ls8Bt_V5nJ82rzDB_BagBhDKpZ-T5VbnpJBHZbT2TcDUsZWELihpcTIlPmHy7fbDFpPSnqbt7LyayLqykpmCzfkZlou7u7RtAhCvZQSdAwz_jGz5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA_8BXzvnN83pf_1frTazK7ReCzH2yUZubt0QIvbIVQkKXzDnb83T7OHZHwYG_lrjKl8yVzOa_PNsku6Z6gmG0X4Mk5v4JQWqR0YoERYUzB0PcdxS0xYXmH3nrUPunBnUZU1HMLau7bRDABFGwGooyp1Ghb-Ebro0cQmlPaegAU1w2oDQMRPfSSqp5rfg4EIJFOzkmvUj8l7n8Wyg3rqoNH3FC9F9ekcPmt_h0Ul5Jm8VjvJhERCPrYgu6w5csZ9PQ7aJZXqDROLVkoiTUinJj8hM-B5ZQ9GuiJADqlyUIT3orPsmKpWbTPg_Oo5L5MhGgCNYeeIhq8E0-YADLRtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd8xuKsyLKwFrluZbnAws621IdlmnY6T9-Plwb8FfT78n_ABatPHzgvkfO7u396BpoUcnzz1JqHhnMgKVbajZOjzq7rbDd6VHVVUyCYs7z6vuJ1I6JnuRzv5Il0zZ87muaGcIR86ocMv5wBWXZLx985Jt6YqXkF24VkXiWU069P2R0K2TiFhC2Z7zq9fuCRiVvK9zbr3tpzSDMapEqU0IJbKexgLJ5wCPw6wkl_D2dYVfSzyVFeMPDY1vRrPXbp07ANr1OHbIpUqWURoD5wf_hLI_OFcQzWk5VO16ZFJ00P_Ve1XMlg3lkzb0Dmm_kN-rMgD11v4RYrjRr3awZlvrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhWonR07C_re1YY12ckdIKEACEksvp1wPUgh6Sn51-hHVJDyp_Rgm1BNgR3pqxOy5KLiUwzI5J0bzhjtDvnFOM_aa7hGI5Kx-eKNaKgH7kp2719xJ5Al2gL41gKVHrKqJrepxwZn8K7WP6Oo4JkdqhYsXDIfHy4cFGFhhWXHB6Cu2JWPGkpMJKsdtOyvV1VBLJonabVCXFnI3tH36Z3Y4b06ublc54F-r8mgKDTnRJHdJcBR0xU14fIrWnTxFpN9epHqIDsCQlz_h6BJO5NCc_32Uk1VrTa1VwdKzEjUk6keEJuhuPQ0w65_Bp_FggeXIyXtoiNJ3ePapkxj1RKeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJDwXVgW97PBVqYm-MtIOlyGXNYBoDwxzQPy5e_cGWHAjtEN6g5ijscgGOINJbp8DILvaRECGnKciUKl42zyHbAwuWtHI1W44tgvdJIOjIqQV_cZPak81ITanyyusk6dfhAdYBTxsBQ8CBQeUxwMyegVVDlWIw9njH7xzeeZ7hjORDGjqaXFNvnyRADE4otBiO2Xdiv3t3CZ3Epf-aH3eEYC4bjupabXYRfxtLm6TloEkZNOQjB7EMeB1hyxY3ZveFHr-uQPugLzdsUswnmOBPMEpbvzJMhT9eW4bMi3yzPmyPC_9tksiVnrY5y7kX0K3Sj71tTkWJ8dTljl19Zg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPp97FhXCSSxpCCo854wuflT3FYbBLGRJYGr3OeijZLTibbHsvs6lOiy5tGpkJOVR8mmYhcJNxs2AVi3A-QvBSjNTy241lqq9_yYp9YRqLFnDVvcrfGG2qgxUc1bwOZW9riT38DCcyBU1BJ0jZK0u2fLFr-R-tDkbzPnyxiQpX_66j_w0dncl1hdJZFFRt1npifkDdLMKykBPPGYgsnXXUgZmPoHQw_0QnJWo6gwmaxaii1eKN041LZLe1eH5sTEsAcmjHX6j8RobO8s4NsS3FxL-8YgxHAj1aSNQ784ZnQ_3jC46Sfi7LojbY_3gRX22q6Znr7DcFoH0SdCS38Epw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOSVgwQUHLZIKxIawTfpy-6lMv_0GLTvh1zQaCZzylk6J4y5qod4MyH8AoLVRb4EPG_wewTArumQ_0K0qUSKm8SPw6nXTA681n3KJsLYmza5FOcus_s7jj_9Djif_ijbcKOdmoGjWTTkzqsqSY7QaD_sphYvzDPxnZRnjroCcV3wv30Fm2UkPnx800iVZACYKRY6UFid0WAQhLf9ds7KI_YANTrsasJRL9ebaK1_EjIxdoLzgJmBqLJ1DCfYt_R7QSsTJoE5O6KsMTugA9aMMtWumGiCpIuXkYn2O3U-hvIsmVBOzhyNiPIYVU14vzrHeAssu8_efPvb59d_tZ0KOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeCP2uGiZyI8ZcyPjHMzXPlopaMBRhTQawZiGNl7ADTLXaIdNAMqYl-DxZvEvDL02PO84SaY0QEIte4GbasoZc77Zj2OUW0kWJqhl05OR8yzio-4KDAIxSNj-3y_LEOshAEVDVSqGkaF2Oth9IrZ8KOH9J4VwumJuxP-uEn2ZCZsZnh9i2GFwq_NA6aZSa82P7tC-K1JR_inxDuWPJVdXHkAntaylUSTpBRmQ0Ghwet5QzpgAI0YeA3aG2ju9SE1XoZunm15NtoQF6C0ZRRxsmMGVInD-yz56nhNwciuWundzOKqqG-HeSGjge-6ar2RjhrF5x21AziYia9E8-s8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7f0QGxP2jZdUd3AspiUFf5VdeHqi6a_DlSLIMp94QTUAZTZnJa8wYfa4uiIO-zEyyNW6WVlHUMwKn84KlD9z6HltEq1wvYZ8_DSDWHvDPrx3jVdFjHQjFN4XO-tecI4NFJijt1Ptv0bHArccJXQhLJOMdCzhJYwmmVnHk-tGdJpRphpFiUuQXmT7w0bTty-MXZ18ZFSv0qhba6LDhoIBXr2l33qAzq0oLQCcfheqUy-5ilxHxUFlMrOsUAFksKtxTyLXvJmmgSIG9MTwqAmApVMIxReab55YkKsz7Neypt6We9jqZMncq8XZT5gMWV6NQIZ_SCPfikHq8CpzuDgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKx1mivJdnJQK4G_qm_HgWpmrKm4yyI0SaxWpjm7OkplHmJohy-B_rtknZEHQWT8Nr3Hua7Z2gqT3mVn_TrH6ipqCz4EyqqaCFZm8Culs6qLhipoFdPTnHFli5X-qZepjp-nf41iZ6VAnIFD59Cqg8IP4-WFw5GvALDzIQ9ZOq63t2kja-vR6AYlJi0baH2Qggm7provxBmXgXYsdX2RcXagWBQXii0HY84QvTseT5urQetcD6IkSyq_H6krw6_6CsM-N8Vg0pJBDYfNosJmxICKUYN1oxqAUdHHMQBIYhzCQr31RTx74CluDzXopyCH7sDxyrqAk9W1wr1_9dsxgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orSlmmyj2a3h5WY-v_o5uZSIHa2EWMXa66zZtwTfVRok0CmnIHXUYUoklwOc3F5vECmxNxIahs3QxI8ck8KFyKhmbH4w43oh81DDOBUcdtqgPFB-2tPCRsgEf1ugH6jh32VUnKsXX-yspnt-Lie3gvcIKWKXA5Vv1ExoQGDoVczcv72e4DKrvT_dHyB56cLQcvWF6KvaCH_7PUhSNMfzPmOdhF9SUUX2GNIj6SaPy23acxKHrSzgz28gKNlVOylOq46KHksLpxh6x42Ud9MDKVY_2QR8FnMloegkCWJuYp4qG-UOfG8TeQwElcoBZgxNilhsCG4vG3DMzZ6MvzEPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3tRcH_TPMH6U0sXqR7sV0IqQPvacbhQ9tnpU1SlRsRESTlvucDWe3KkNtCKdiLHx3DH_lNv6fBVtgjBHju3WOBKfwwVBhPmbRRF_DMNpeTpFEOh0OnB9g9ohIdgDTgkpinDOJyONgw_JwCTXmTxp1b9zjrE-Mo2FG69CEMz0XHaVObpUw5HeF0BZkCE-7MSGHKRugZAz87mcxx2JjuTaBZ-AZ6TbP5wPg8Ye-3PSnAKbVnplp9d07onuWdxo_2vr_dNcAfFR0V5UPHuGhDcWSEmQHC2e8BEuoHVqmTMfJLo-LHHDgtRwjWNQ71mRxSMlxfKFsxwYYbL5UzxAoNfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcMTZqLyimlstZFEurYmA_OwHr42i7A_OIrdzW_uWUrKCLB6Wkk44rtckDEaImes3xS_1DMpVZCPUEkwtm6jd6iLk3TSK5BjsJT67asJVE8krvJyUVuJjhTIX4mjhbUM0RYJrYDQzewCypyeZ5aKQ6ZD1ydexhgWcqTwdWTn8fJMpBCvsmAvWXn_WE72Y8j1PmOdGQdNbxKjdoSC15rSE3dBqfcV-95DU8QU9ptGcAemWMgPkduXEKhHM9u9qOC1v0mpLD9qweZC41MLw52nYnixqSdQLNj1Mvrojge26I127kJxLqvHNch3g9Y35nM9cp37KXb-l73CzzvWHHfyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfstIWlcBY7h6fPtTOM3eh6jrCAP1gQUNpr54lbGGTdGZvurKarXmaBuHG_dlH_hDWYDncTSPQzO0SM_atkE3N3dLMW7hxDjbFI4FWIhOV6m6-wp-6UkuT4tp5jJEapk1BrbY4eV6dXAdbx2_DWAxXSb9l9gnACTY0DrBE6RffD4iSCDrngBIi89hokvBw6jXvkSYkO9eu5pywGPNEO4F71UEFG8cBpk_EExt4zlSwBHx4A9QaAKG-f6W0UvvCx2ZUTvg1tJ9PzGwk2B1GS7OfJByv6KklQIPs52Xr2gaSf6YHGWSIA2LZ-aHnF5j9ca8VUHys6ThLPt_YSnwcWqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyvcyuk3JHHfzOXm-cM1cIKwiz28HFWXKEjWRqLX2FwVjLk1GyhKuUSi6gAKk7XxP31AndxrZIwypXlRzK822kMxhJV0UXq4XkkpBsIkeotPQ2mSsN1-OyhFNthB7jirbUsYirouocidrEm4aEPdVbnSEEAcEzIRHqvwC_4OcZl6C9AG5c-TWYPe3UL-E7c-VOsRblHlGS4hW22SQu5VkIv_Yu9L96GOZa58JlzGKMdfnTGzkhwghORnRVr0m8BGYVtAzIdZvkqNAFHUZUGD-dFp1aZ_InGhfz_eNxYxZ9HoWzE3PYlN3izaJEY-zpHt4bnQF_wn7dozdUJ4YSklfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjhYzaS9Wgzmiwa1IuHk_2d7yu8xe1bv3tI8AXn_rCftsF5_4TAwg9aJaquJoWWsSyXGrMGoOtPf53OZXV42axOaKSdqUQi8CxL0CqN-IsyN8HHup7vzG5gZmMEnbhTvf15Xj1SU6T7hy4YrTXDOVubcTJoMSBYIAkJkn_2soCTtCrK1HHKrjJ-Tok-v6N_5gJzghbXoSvHI1FwGnPXYxFa2px6NPx5p3p4YlPimXJXO257PmJRtzPF5cIkAL0-RlkfTlntfs6KZQO9Gvti5K6cqOnvku1TKoGllqUPwC7t5qIdogp0ISDf5W8GpLy_0KyP1yhJcRV-bVl4D9IgVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6_TPSPwdhlq4SDdnsg0ki6eQjm2kMAH_k3N58wYy1Aj8NqTSGNfvXkSbAU8dF2SRZm8FxicgFhvpDjr5ESnuoIqRdLeajwwmoWxkTL82c5eAQQeZFOl0dkiLkVPJljbMojKMr25Bsqg_l-GbNLiio8uxwsvOOqhGnrFvPGHNf6o-I7csvYYQpLmLqybhmF7ZkeIOssXjDOLqeq3w6iFwImQEovSyLgiBalmoV1OThXcmvM7uroEXkU9v59BiW3_fImjeIXaGUwG8h9BZB8e0IW3UEQcuTC6Loac81OvUuOpCGRhmsXtcgjsUCjnqfwm5Rw7XGx4wxbvjce0blu1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AN1cgjQ2fkWc6OS5FDSLRffNDNthV30eDpcmlh6AsVa-70ESnj_dye41hrXE102-sMJ0J3NPdgLhIlj-3Hpk2Etq-BTtUJBroff3TewVK9cgId_suyn-rZco2qTz1dTC9EXwkojCZ5MljE_TnA9Qvp2uDgWwM6QZhDMFejdPmoo0cMuqLvVkHilENqHZmiR_jbH8icjTj4R83peiemVg4TpTDXnvd0nBuiVNZibsg4DDDuPZ5ZIKS8-4VV67EOgmB4R4FEqmxa6dBouCeZNz8YGPTKQRQCedgbmi60DxckzL_sprmRbG1tpgWgBl5XTHcWX2STq-PmQ0HCjjCcyQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOyIBvzg7eYdLqYYrTxwJpWxSkXZjyhCLpB-B9RxnS0ADiTMvhmM5ig41m10wmjsk3xCEb3wilds1lW4e-W2hUGU-xc9gQPG1577a6fcoaCp15nKJDMQrn5lCBhr1xTyny3AyjyOvMsSu3QSwp6JkZGWyPbQwn31HJCLfRf937fcyN5XFzsReiVFgAwnT6iNaSQu2B3N7SXzHicIXC0ETxzsfGSzT8bFbQw0FHzk6yYP7oP4d1ghbSioYfbuANrP19FcyN7gw_L5lrPRgne8J0P1fUgOPCkaiGGkjYBoIg93Dxo1q0PHie1H4UiZN4T-DkY1AmK2cJ00fGp4hk4VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B51-hom1PoU1CI-O826XDCLlPOah4-az70jMdPaahBkb74u8mPo1FnSIl9o15pF0FDFlqK2OKnVuZgUpQY8S4ximSvXUkOf_v_8RDX2s8HopZ4VYFODtRbU8JScSO9HjLw0ZmEtjZ0siolFGpWS7GFd3pAkffd8VznX5D7k-KS8iL2KmeWVRe0kcUGIV5lwtyb6_gMn4RXD0NScdk4tiapKgsnyeDQf_Knx9dK6_4fjW9BLCv2cbvgkH-4rQYejKPzuZyP2eC1W78FQimXm0YXmgi3Hf1kirX2z7COFiRgSbw0fuvE9PMJoDCRXLt0EI4UwBaPctxwz_asSuytpa-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orm-PDMrpG_AZK6tZPBZBtg9rTp1ZtSYGPnOPkgJi04G7Wtak-fLEe6I070xBqB-Ru5xoOH9pZDBMBsq4jHjhJMISzjethCE2mhjMaUBm2X_QullZ2BXOMteB3BIl5bamfELKLtFR4wIRZnf0QckmNCRa5aDz0LlGqmnnepiNkTOmAg-cL8JKYmRsQbXDBlgJ7_cwbqVZDu6Dxp7PdrRhWAUl4ooDO2QrATddoP0RK5_Bfu5e0huWpPBomCnkrfqHG1UxkiXNzp1qsE076ryPH2YHNgDVOLl9NAUmRXCMn77zGUBR4EOMA0LSarVOn2NCKmk2hO9u08AlWjnC96gZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-I3q9G1tC1OinYaA1_t8u5A8lizSAGsV-QYwvMCn0iKlnayqCJ3thCGBjdlJplNcBfqNBPtguwm9SPn-6oz2S_I4pLAEAh4vtBYJEj9XkGaPu7LW265cmpm8aqgpH84MNEcOY0XtTLtiJ6xG8bIx1F8KJdq52HgC3I4bZ_S6I92KxFy6nYgL3w0Pc2nJ60z0kWTQ-du9XW3-l-cFUbjeKj_Lip33tY3UNjvlf9fpiz7XDpgO32wWd4LYhEZLAQhwpK0sD3q30cRVwggRjmx59UNArqxTMrE_U1iyrIS0ArueVTYGxa6V4x3w5fZwzbLGZWE2BrOyjrUaZn5B8vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhyM-Z0DznUlY6Wdjac0VXeGz3OZh0lD1OZgz3pKm-07NNvvMBFi1zkfJMBfcSqsnLsNSb1vPT0hH_csHL3RDHUHGh4mM5J0e86lHrC24v_Txwc3ItVXaKQTK88ECTfLu6fB0t9z5o-CGfVbYC4Sl8rGYqRPNssXmnU-RVHEBWnTQ9KrA-LDVOnpfk8Rx9jZgeTZD_ehuG4P-_nsCBW8MV_9cdqsQU1xl22aemo5ZvqyQMPqsZNvbvTO0CA68_Zrp2hHT5vRZycJw7WRMeVz6gBgu46d6m2fguTNcl_edsA2-rPq9mrTSiEWZsnGoosMJBNAgtUw1ggtqSSj9jV5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRpgL6rXiSS1tfXtqy0Oo3vZNcsFII73_BnzuHvv19J3rNqmjvSyyQLm8wGVWJ1p0jKZN1Wg7HERqeinmlLUxH4QExgFhUZ_SKl6U4w3J1chgIvYoEk86NrXxYIDD4p7UcQuJgzxFnOLcAdsvFIk27KZt1XiPCgH2MXmPALH2UOSv3HOryYQYMTixSHDimMrAXJ6nACX85-_DaVCpmjQmbANyloY6KRtNrIlWZpver5vaLjReA0Pd2NYoQYQf8kT3oU9oqObe1r77uTxXd1z6PUmqVgJ1_xc9ZUELnUud_IYQcIzM43tNSKb0NSBfN3lN1RC5Ju1TXbidZrywUVQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbZ7y2lqyQyXNqvJnwEq4P6iQ_Xm8qbjVB77YyX0ByfmXKqRTQCCsCzN0_P2isUBL1sZ3wQ4G4-cOTbReUYBMM2JNsRK4pS-fXmXZGpxwYL5WMgKf5HIs0yPiM9uPjD2F-BOGPJJSGQM_qEBE4b6MO67JRQmIvabnxZ_OBZibmzEIwtKJeYG_svSCb7pk5gemkBm_YzlZxQ_ot4_okjB0jtEHqLFHMsaXkuFQuDzG_LadXp3xs1U7kc0PDkvdv-lYCzQaK4bjluFVlQaYqnDsBfpjDNaOSW0Jlq570VeeEVxW1xtIECo8JfcqswdrsFzKk_3wpVgZ1Z9q0ToTcW7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkjVEvU4m3MBThpcHfuluiFM9hW9fqoh6g_nf16W3--FHpu-ItlDqwUtYTjbGvPP54PaNC2LbSl3zjoVtPAZV1MG4Zk6FEg3cSWdLRG6Neo8c5WeerkkvmE2Db1-qbgiisfNGefYUBivFnZtjhoCL_5Kq7pMftZ0pXypYnmsp2UE5up51skCTP5ZzgPwn-WenJjpKMR5K-LGNwKS-fnJ4yvkRwfYl34We7Z2wILCqS3oAp6prjCKvv0fBacKVoAIFKpG_z1RrDtJtIKOnGqVwU5A5vo1HLfwz7MRfDwFoMOy_L-etsTT3nkpf0s71z4LsXHVRAhD1eIjWicCcf6_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbA8ZcDYJ-7TChFod1XqO6BQVmkyUwQr6ZZgNOaDApCCbuaSgmqgRVtXaRbheJE2x0MvW9XFkLM3p6OonVgHJMBW7a3dhJKo19jVXg61jcvSsLhn7AmBDglXINs-1_pv6K3YK143dofgISQlV7dXmKFnOHFmJaOx4dYAI9FqwXwCtahOEiuSg_PWPl6LZhe43j-5dIfUudsJf-cCx2YUCQuHwx3QqgAQW__4I-U7fLrVg1588E2EeBnIlAKZxQpo0RrEeEa8SU9N5YPGV2MbD4QyyQjFwcY9iL8e2xf8W5ChiFUYvNhOzOVnX8ODH9mOKluBO40HJMubmvhH9i_gnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/at7nC5vsleIxJQdPKPNkIL1P7qB2frdHyuTG2cTzQXFvdSZeLxc92t6X8PGMdm4eUUR9XoKEN72Js61eFVvi20KDj2Bsjt88hn5PzOn8xwDSMhC8WggXoMjRGjPivV1LhbpA3Jm9_lSNImaLm8tSct4cUWCQ3LN55oY37u7_Fu2kCeomIA4PmGAxLVvfQMnqGHNdZ98YnSjieMoqaeUiafIs1N6Mx1mfcNx1OrZ0ioxoHVaFUHEqSeiA75VUeQEWTFD58C6f85i0tWcGHEyWRsSdk6keaVHuMTmw0L4iQxWcgcWvF69sxmPkAl10brBEYuMV_FT3NyagxI_NnzVitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCuQRQ_4HeCOKa3R_j0fKMN7ktheFlX85kzjovoItN088CelCzvsg8r9pvHUKCmNzKjCQPOq1Es9U5Kjk57Z4hOK_oR05c-KgBtgPF4Oa8bye9KEsiPtR2Z5rNO8OFpzCtHSS4emGoFxlEaat2DLQ4jQ6-WEcQawPAVLOcOXqd9A6UUV3zt_WAwNBF1qCS8u18FbdR_D_cSOgPfuuhjDhPw8D82cFxbPZwGpztJJJ4jDlY5suEPBevVO9vAfwnArvI5WRVlK2ZN_tM1RbWXjXZ2FR-m6nnHzgAd92kSabct_C4ICs8A_ZdwcyZGqcjrKE-6iKedanaQ_p1L_gEGwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqj1RF_fjsc5ZPN7iK3-O5K4DDxeS7FmgarCZs398jiZzzPvjoTiPkFFFrwA2Za17xfjhv8usSFCaJ3ih0sRG3bvuluTlVG_R-uAeXyA8NwiSBKROO5xTnpX7Bfu1AVmXwq8tn3Dkgi_kmpbcyDMID20-MgWg5dhHlAipYMpBmCkvZ-xy8P2cEXGkoE6Peiu2LLM93e782ykEpmDV5sRaAX7_vPH8aJL8FN43pFpACVUazzM_j0SVusxs3PDOOGYCywpZNqILstcSfzxCIWQfaqGdnwOIgsSgOz61SWN1U5B3eXsAevJy0YYhqeHbY7WAvu9i8ICbwA-kJz1V5JQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f53-CkbFGUgQ3DrVnSCvOciMNB55J_iUHWvWmoP1wZBqnyGtXO3QlU5UnOkVbin65iUKWnaUI1RCfNNcDIziRQEANlYcQZu58gygvCrgx-PuDMVkyajOOBZzSuL-SnCz3wVKxvAh7UNl2fyl43rFUPaC-DMHsJirmYj5Lw_i8lFOm4KMuGPu17-NOT-CWdTvz8TCCkoytCFo2_y-LKzhAhU29-R9ZfX6pBL7oKoVMk-NjWprS3CQMj_L6zPnYxbiLxvHG29kRMXISXWt-vK8yURREnT8dN4NaH50HDmD8Jy0SomD4TMaEc6LcBdoglg2J_znJ1O-odU6LcxiLfTJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY80QnBkiO6k35mZPiFv93frTzITkIV00E-TClCVD66dAjkvinZCzIsrDIYhhyY9LaayZWzGCo688Sawaa5SBgJk4xmQzqGTVkLt3Hcwsx9UeD7GqfYBlgTuuUZJxUb2H4psAKN_CJhuVydVk_4JZM5VuzD1FDNzoW6EssHQoEvj1Y7OVXKSyTay3bCezghyUu_IKP7fqTJ4tSg9LpLYT6vjbrhzJdvjRRhb2KbFkG75_8ypmP23xbGYgxqOuWMx9El7Nn6NuNDOwo14pBBdBZs3VfnvWutAVO7CvCO-xWv3OOKNduJuBziY0pfFoMfz8AiuHYvtmWkMV6bTaNk8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5CL_Vhzck-2gOeab9SWqFxHg4hCMN332uqvtoHuHUqFBXiA3BR78UGSKgW3x58Lh4iaVYrN4k_OIyzlcln6syXun8fn1bPIT7K-fIel9weYq6K_kXXDH93nWBljldxuaiSEYTWbD7ROn63f3L4DSe78SxGvPxyAFwO0x7qnItD7sEukbzAbL_gg3F_jSvBAw1cjvGrGbz-eNAzm3nq_8r2CLlWljvtei_-d6C1XaFhh_AEz1-AHcHTcB0gVqO7mT87ypXfkig2nzmV-LdU2pqqz2kwRTziGdmhbE8Yahb4A8PJX87pm86Etgok0OmfOUB6reo4FzuKwpWoWzx4vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpxN1Ew4oNa54ABB7DRcQ_SY5yAtPTy04mZnYtX244a91E-22pptuYWF3eLaLDO4A7gVzlLdpEpa67xtP8UaH9G_EcGCGvuNF3dXeNyRyywsc3TjmwVz8a27dKZDVLCgQW3nXdOn8jQ3f9s0F3cnzVzr1iZXBZ8DcRJdDMja3OEe6eOW1FZKvqcyNurF0H6X6dtSqjMZQADCypQMwW7PhG5GUqUEUJGkBA9YzmmXE3FqQQyCK7hdl-hJKz1xCjft7VQI7cvSRCbxY7yjc5NSUMGrX01W6LwSVDwqCy7GXPPWyrI13_cG74zozZtMar44IfbktoTD4MWri6wacqvQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKoOAUoUTtBznYPTpd6qBCs_KLbP3ssQT929O0PCvjuBSZh_oMDlrXd2vS40r5W4fXmKMlwofrg6LSLSST9VBGJKeldLTMZgX-5u8uHWXzizXGzcKXtg_vfNovZbKUhyGJQNV6HZp8p8PRn0KC8lJ5fA5ijdQQ0qJdPNItbbrOymAzPEUJaifw_TpseA3YiIDT6T9iriJVNeDEqOpm_LN-0-l4bPqHVuDLB0nUmOzL6XQFJdoX1oGjwyfVRvzueVNH6GxSyVUaQ-b-RXAqnjTPjN-zletZ1ss_rFsGYWLRdepzHL-1BprYJehXsxBxfoJl4BbKVqj9846S3sglh3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=GuJDGRiVpud1AnpVcgfD6wKtjN_pA0D0Oa4-oxTVt_H3qglw_AOmkD6fNZi62HBa8fcIBtZRP6DkE1g689LNSP3heDTyQjq9upY1nORlW1SBhbCZyz-M68Il7MIjv5eHpZDP0vTqqeKopQgxfn3OfuVspCDsqOhVQBFpXQJMtJt5uNFAEnu5wuUbX5tRhrcp3nDVlA-WAGn2p4MDndnlJw8YIWki_RlUVKjvtKYl6hFNFyCr8iqR_XIVoMV4OcQhFhWPWKvYixGd1simml0FAV-sl8JewQI4fkyx1pSLYkrdCr2f5tEdvDyCRHozBg_rOPeKtWNy2rhjXmwgDV_J0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=GuJDGRiVpud1AnpVcgfD6wKtjN_pA0D0Oa4-oxTVt_H3qglw_AOmkD6fNZi62HBa8fcIBtZRP6DkE1g689LNSP3heDTyQjq9upY1nORlW1SBhbCZyz-M68Il7MIjv5eHpZDP0vTqqeKopQgxfn3OfuVspCDsqOhVQBFpXQJMtJt5uNFAEnu5wuUbX5tRhrcp3nDVlA-WAGn2p4MDndnlJw8YIWki_RlUVKjvtKYl6hFNFyCr8iqR_XIVoMV4OcQhFhWPWKvYixGd1simml0FAV-sl8JewQI4fkyx1pSLYkrdCr2f5tEdvDyCRHozBg_rOPeKtWNy2rhjXmwgDV_J0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
