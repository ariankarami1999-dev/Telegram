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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 09:34:16</div>
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
<div class="tg-footer">👁️ 837 · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmVr0jLW27hdlePlFJ2Gh-bmm-OJRYF8saisnZkAK7jYWslSAhMbjtpAbhJTJcwfL-x-IYF-HBKFE2iVGlEC88SonyoARJ-NMuxvEJZugxm_6lboO9TS-DqzKyfTLJuGfBEar4wxGXO3RLI1CKG93r7wbOCjHdnpy44t-7jyAw3qu4rvC8qXOn1lkTCyU1emjDW6ZmV7lJ6oWoeDiZY69nBhusFJay7YCe6ja8jaxpSt5EQg9Q4Era0mbOWGhzJfJJGZTT9dCDRT7Y9Tli8ECQUwoYAg7WLZDGmYtggQY1haIBMNYZPYP9EJq6C3EjS1sOercTMa2B6UooEuKt9X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBIb6nj--0g13EY1k49lr8sO1kALtJexLgOQoT9Hjqhg4HBk9aysvauIMSTzF3vWY6gahIeJmZiglIJ_1nCZhkzaeeLDd0xMUJAUxXdftYXLyClGmvlZFopgeih9zDDfWuYnSTaiBkR6pRkFU-Knz69JyAVGyuen1EnjJUV80FvbbpJo76-kRHVGMZHdH92XaI0P0SEHOFLnaMMm9js-mfF94O7-J4uM0FhcPuNDFG4jmx8JdHxR3kPpU7oT0leIURuZ0-Takex1DEKMBlr59lLvjQdv7iNtyvS4TDopOe04HnOLKxTzeu76OLevNVh9_yAWD0LKa9XosmgpBtW-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTplawqkVEQF9cKfHE0xK2QqZDOTxQM2tXqspgaah5JVlFP88zi7OTaDT9aMOgeOKzZPjW80vB6kHbRJS3rpLV5OGDAHcJfsjLS4bMA9AaFLiCAHO_0V6fMtRwmR7f7sht1PQjScOyjFQWRzQqZ5pDM-zzEIjEPC2GM0qtjtU51rl9LfSiO9bH_GsD4B7UjdJ-M6OsKldlIdlTRZEjjkcnLDgxoAHN8qF1YAUixcxlqZisl3WexVHKgI0xgnIT4Vq1kbCUiCROWkLIlyJi8K3_5vWgoUaAGPWifVUSU3dTTqFz0GnlkUTBkbXaNY7pu5BhetcDF2Heqjv9q1OTxQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLDpZhrPwUPAQqW_rDT7OP3mQEvsBGRBh9pWj8RHAton4PaGbUV00bwPDyINkyNZgZTU-fDxzBXTvWQMj1MYKnrOLgIUFoOZmxIBSrPUtZEsn4BLn3Vo1JCQUhmuoR-9Go-CgvCF6Ms9aZH1etQTeq-1dqGklbPIXa3KgdNRbC2oglLUAgDu9XbDO4WpNgfacAGZwn4J8OHAnBKMGPAZjRkEMiW8ozXdudj7Yc-15zwaIF6v6_mXmsD1OZL8UfufhD2Q0rHdxIJm64F91U8rUpUiedZJEIMVoOa3kcDISLzbHefkGD3b79U_3Dn5rxMRuXHIPxz5H01qaky_gdQi6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYo0V6w8FrgBBB_G1_B_aIawZstWUGqdKy3Nn1dI2LVeGvTopODmaW5JA1jMzuExhyO8LhMroICXjnFpjKgeROsZLV4FWK14EA4jvcEzLmYKjaX3A97uQ-tfdYoJntTPsz50E2E61BgZzv1x4qyf19OzuMCfqnDMnCJX93Yrn6na1tzAfqx78Z03QDkrlKscegxohnaOr-mpFULP4P_AbtnUsP7zUBAaB8wlQHwyHjJcwR3itlZLZbsgcH2FdyHtyxi-geo3YDFSr3RsU_ldzE4obbiPau4PkAFd9WCg3JTfWiROTcX_jfDmUK94_YZL_xyCMiJ3y4H8n1zsuJLt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_sTXmczXAJnfORonybvakw02b4CtG5kbn2Diduh2OMt9l-wHcb9Ng_AV9Vhla8vC7dhcTHGEUBrOvc_putCGzeRVtwx_LZoe0l9oklB5KL9mcOvpv-BCudzt1AiJSfxzZ6TpOqItN9W47DzoS38-Q9oY73U3jnyDB461IZ7Yf97S8GL8imB2vwge2QmHJUmF5NdQ3t575TMlrYsXrIrtg-Sbflq7DP02Il0YChAtQE-bes9K8O_mWyAotUZPffmPT_Xhca31OrOHnybIuylLqT9dEFXzAUFv-eWcAfJTw1vQ40N_cBGXQ_xsZak6QtRZgns0xR5HufGPh42-29A9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5B1wX5bNVF8er3Hn8wmLoerrJiz12LIMVr5RGumXLJNjY2TxmY5eidFRGtcyAO8ihzYXcXxg33OXXWasnjpCizKy-UEnosuSC_akkZ9MNBG_doUeXvAGIkgAeBdFWIkfDHsQJ5Y_xrVWpb6n9w7hDiU-oWRWoGEntsr_x-4o0anZp6Xjgx30VbzrfDNZbKOVYF6qxAu5Kw2nNhmuXYRu5nqc4LUmowtAIh2FlcSaeviZPpDYmYVFayYXXPeOeVoYD34c3MC5WJf5Yewk-7-lBlnWIbY7XsaS7T11HNTtnDzG4j9AdXuEcLneFGViarShwJeAKPgIVP5gXiZ69FyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCWEGQpAPbm6HLeYIucb2R_Pzv5VXw_UaIMxAbXpjESzPphB2tDfBj3tjTzAiHQlrqu3nM-UEx8cTHtNyNicVqZh35YLW4NXXXD4uB1T0md4nVnineG4UHH8p2T6uqd_QHCGM_bdgwQXD_RwU_JtxTvOoDRkAtbzbIlL7KWDjEK72DQl4Ny2_zWUzlNEbHK9Zbesh5KJeOVQN062aye5YEfNoXryNwp1WFbGDAiUrZM5GiyyOMlgEzsGJG5Y_izFq6u4b95GVroicvEkVxHYZE-IJSuYJcONexGNVs2xbTF1ExUYEJkOPJ6BOARWvRpCGKEa0SowFFDPmqadgJNR_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn3Uoxujbc_jAhNQS6wyvPWZbVjz1mAKLXoSP2lZKICoqMfRaHHG5V2g4aEVxC-IA1LefFDvdiTPj6sLJNAOB0pZetQAA01MLPq-5p4geUZhaiLkwBdoQE0VTvnIWxk_yLS9FJHtTXIBTNGvmkHo0Uu2rj6M_WfnmmCCfGcxDWYTiJ_PzGDReW2bZ2qjlAUfzhpfbGWhJmEHp-LcjAk5FU4nozpLZ8M0z0COcW5FzN5b-8JU6jerC5SUYAfNcoEj-UiAtWrmIYszA6pjNg7K9Dmn8-lZkZaemNDtftIJjtYTBu4Zm-UDjuVWtnBRizEEzTWm9KP2yTHt2cf-PSz5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QloeCemtzTBbx0UzOVbr2sXIXf05P_dLYDk2GIrGGKWvujD1kvNFtoJlcQUZz1axsKcNOiqoKow_BxVdiNB7gmzKYImYqAsyJnl4u0dyV5onLaEinvzKkLZOcV1N1FlkORYwQFia1cvJjeK-dektDFcJrBpxOHnIzvLJCc0immnv_NEBYZza7ljVHlsj7aThiWTQXSreANZTe-w1k5TzV6NH2gJxIJXIAqINV8CNOK8PbcN3sda-KVqUQn06gLPwPLRe_Z7TlY5PnBON8yAM0pY3tN7PSfKzvaD7yrr5VW8M5j8I3PKOD9IUNUQ6HrDRduHfCIdWpjlIZjJPze33dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZeZKmYg3MMUjRjuAShzhQpmCR3uEpK65AhO2V8IQMVaNBTq--9ol4BYqUgbIMJMXhwvkgFcz6EsTB202XJ33TLkd7ISN0Frcs8xEGHnWtVj5EY9W87r9J4Y1VInKRnrJ5xloiPRzJoxso9eaTLHjJC3t4JZcggo3PNH-CdEAPDz0R2a2PYiQQV5ZyCAzYKnp5M6ygUBuDyzCqfopO-ZCvolm1TvduXPLvYSdDs90-oKZCaEoKZOGBL30KG_sn5YqT7k1MuztYKwCxt9wG65RbjydDVdoI678_MGqqQLb-RVeM-Rr9see4Fqr8zcpEJ8tYcyDWynFRPlDXuDDjvwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMbMYtTl5K6fbpHw5cJ8S0Mp_tGmx_nfmirptaqqXTQGOX09FmmcCTadU3xpCtbIXy-SCu46XNbxI50UzWVP422S1d8aMdq2YLs1UsMlmnKhb6M2IDN1XTivWjZVoVPuvA2Wy1fooFajvGhfI-ceOovW59ccxetbRTTXmZKwSyu-4G2GpmNZ-tNhr_XXpAY2lFYSqzXGKlym4w66ILsU-f68Ma84gQTzdGmYXP4EMHNLJGsmQlXdw_NS-6f-g4Pm3Pn2z_FpIrnBCTBE0RHySoAhngklchv-B5OgUvzyMKchKKocxsk7qew__1REk2g7V0rYhTx0MZV3vVCjIH5T_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9tML7DVO7sIWKVzvRBN8l3D8aY0cp7QxWdJipj8TtFAqwW9C9wTtU8vNyY2hRqhVOT6Ote9lXYnUgp4WOuBIzKEBHXN-uND4gOy--yIfXp9EYBok7POF9XA6ksnZFrKRQT_TnlTlFaQEPjYEcAI8NlIbmkEPa0Mfy5SyrOwWM7k3BIbgQRw9XCxIbzgLHbo-zaZf2n8uuJ3Yjo8T3Lac46-ytH-6a7k-ce_rWhZDWHqvhhmxw2GK_ZQ2epoMLIGTpweCEIibFqO8A1GuZIzwEeeb6bfdqyjXuVVRdEQKPLeswXsyFexTNjYLeDTjNsErfd1_ez71Ndv7vLaT2CFJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLueh1v5kEfJgpfaT8CKa2MHZ6QnWFekdoMhUvPWmBYscauRiGloBeTEbJtDwaohneGdw1BlUrj8wSSgIdn3o7YmYVuGWD7_aoZXR1Cql34_MvwxYWA1tI_h890exCBUndnz6sPGH6lX3fMvBDJubxWRlOs_Thias80fc6UVf7t-AIlkqSiPdNA_KnLeTsjO8s3lzzeii1DVqfg8DOnIz5xhn2DnqZBDEEm58_ccqroWwGhRADKb-YOwVp7LFCyPwTgx-vRwPm81DpYbZW6GXMh1yDOCh7c5SbHtjs9lwVX4uFZCzupY2NuqcVDrdR-ZQ8SyglYqS2D4wEM42ZIjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzvlbs8SBA9ZWL3e024yy4Ftt8RrPmg5vkX3ITHhT-nCla8t8V1Y4t3El6zuLYyEOn0Uo5KHUPVtaJUfYdx9AxvCTEb4qMpXJ_IXieLtbDYtW-QbV-BvxfqF4VXL1A_zxpSyzZ1TyQJs_ozu8omp-nl-LbIMKG7rZtPOe7MzTq-fLhnK_oN9ZLRpGARdgQTCmQVuC8amck0tSonfE83RhS555WrAJMCjV9nJoInqc_C_ot9Qy6xrxyQtTV65CXFMi0wYZMsKXrwr2WU9JYOjA79YHcftq_7Ljgxx3z_IofFJuZQYPpXJoWQNL7Z1HD1cqLDN_ZaWtiFXJFAkag0smQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3eEN287pRw-T5SHBtfPqTgnPGIzb9XPyqHts9Jt22s-z467RVYrn2g0cFKaiM-8ZYNBx-fvjxurrDw5Qg1gWS8jBlUXN30LWaO5E9LVIrjETAoZcjW0l0IDbbLSeFfu86IvVqwwdpzkGEcC1PPNP3h3T6QnE-h2BYNU3uEXMwgLCl3jkDz1i-Jwn5WIhqeNcj7CoHJnYJHBwJHRsIq1JEB9JwMSK56e-olahMU1Pma3hvQPApDJzF3p3FJKABJgTzVIv_GBspx8Htty44PUl8WcJokCSglXpztnl-pIYt10fIoAlcgHcLh9YgY58Fc7Jueuv9-R9aZFEXmG3mPICw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGarFgN5vgLwwwvga7ozdoiRBO4B2MnH8HvG3lPeSKxtOxhMVx1utAMQwsBHmWdxny8l0GkRwcPiZftafV-LPn-1iayUGbR77aizF9Ad10emC8iBXvweiVraCHDuTDMkUAaCAGMYyotZdDV2_QwS2VtA7JSgOKQHBE8xdxRVyCEOfZzh-Q3H8yIh_Y6QSYnmickItalJ65GWwtWA0MFJTd9YKqUB9pbVAb50Z2HyguzgSFAJMwvJ-dXBZ6SseTfUfhvxtdTLggOfzi71COHAaF9c29vKtUphGvUUf7K5L7TAoIZhHiic4HvIoOfo_vvoFlIOxvxHPRGOekd4kv-K1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCS-3xU5SH4DiZbpPgF5IvkETSF-diNquRuZuAZQq0I-4zsPPrQt_OERJzaG-jvaBV30x6dCXlF_tw7CdqEX1_jqrWo9F-5_kgV8s7lxsIkUEH1vXyhkU8cc7LZMZw4pG4ZOlxR9XOXSG1q1dDpQe4TYit-lSPUGnTTXexxqyVs5P-nPen1Db1p7HQYQp18xQ38aZhN4o_m6CoFcc30aTaZKzKqPakqGQzdW-kAKHk-309YWFlAJeIwPDyuOjGdOFUsjpCzklW5d6fM8uQn4oX4LE2J6XUIKyY-KFYsZ6sB9_jlIo2DmX-2YGVTcr0e25jBvZ-vZym1Zc2FdFPY_nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-y4atvrVwylcctgZO52HVQGYA5X3VFxpOWcOcmuxpAGBFp6bLiMcGiS01Nq8xjZs7AZm2pc9scC1a2TjWqWaWSNPC-s6HZCSdYGJxuNzmj6oXixMEt3oyx2LX-Z1QNxR6Zi-HMqyHebPuFG3R_7-hQy6ROfhPseE9lBmkt8gdd0rruIIw5giSlqHD3m6xA6p0dIRVPGyu4zoZ6DInX81XsN7egexEONZ89nGUAQTKccrhv7Wezqeo7dgoeCiNYm1W9IbFLyWhAcY3ZV_PYArE5G5UpyNglmC7cHPrNKScwUeYeCjdwuXG9vuFZugiXKmIC9kHwz48a-bQhQbYXYfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_vFNzJE7PktlrlAzE76rVS6DGOf4yhNHfPaQIzGSFzzJSb4nYzTQLlFMbvW4dkKWmX9iCk4Xu9QZIuq6ctEJgmfldyCUcrTonHCizbmQ9wDFUBaEDSdqJOSJG27kUjmy3Tpq9u4tP_Wt5ljNRq1vSerUED66kUCnomBBgzeWTLlBfxyJigxTtAZ5CLTdtM6Voc5I29GKtbtemgRi008vWPmvHPiS_hUjLu7jP3anmZISvFxv-HwbyaIXiSfteE5k6g63RpIj7VzZrsGyLLBqzqo8QZeXgejUkVez0lzmQ0XdnIgFBnEHfWq6BcTbHYVYeVNdunVlo0f3q_2lEPWuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJIGkMhGAFr0HcALWjnFlVFvhfewm0B0107Cbt0f2Yi1eVWMh-FZItHAeO00ZvtDxiHoNmSR-F2Oi7kYZQ-Sj8UGxTAEKetguyY4vTOm2SGhWifdtAzXRUIE8EH-P8xWmlmrA1IsOpY3ko-MJ82ixMGZUQwJHA_XfqF9cUXIJKRZCjPY7xZfX6RwqX1lqTBmUYuABHo1V9qje_HqdG2wmMjlAetDEJasbMm7IeorbSn3mzwzZrDbFBJppM7pWu2tv6UgFb6ECJeqiUcSp8Mt1vHGftTFtaXDaK0FN6W5Q6u4luGGQ3za1J-UF3QYbuiCFeBP7g-tI0llIHFkmKwbGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T02mmY6tmr2qxHdVN9s_duf1FRMPdQf5ZyNbHjzw43_FMkONT3EMjESnRX2r9Qg1KfGzUlE7-_vsDQmiqmmEca3Akv7SgaIme3t1t5RHqoX4dHzUPglMmSq8MLZlRZyhEWhGrIvMu02UTWHO0eE5WRKM3ATM4TXVjpoNAU4YH1ShSHWfukfPjJnrcX5IitAobowrkOljQQ9gsbBJRgtbUV50Z__7RfYalm30_wzNwQooWz1wDyZIptL6TyWlU55qmApL8ZKRi3u9tjteOeBhlsMKKaH9BMBN1p3Zdgmt687uEe0VRqiJ6KYbmcWGkGIDOcETTcXypdC9Gxlm2nVxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7BuLywca2TR_0uIi7IKA44lTLdf4x3InIAgPlSO0I8dqTK-fVNrh5ZJoFYMsg1qIWOu06-aMa01PEqCwjptfDRILPAh4-S2Qo6Jzk-4fgKi69UJ0MM7AIfRp4wY_N5Pe9ChO3cI3cQOs5oHPZ4NJjTvDBoKJa0siX2dm_oa5oM2a3vxzECRbpBZ6xsnb0ljiPTvIu-TCaurqml4GXLQZWoVYmxylNywVtq6pa7Li51NGEcA0zDn9t_LhLdt4XY-2brbdJ3sQ9-hmEIV61pNvSThKjfxQklK03xCYBu8FFrj86AeYQJpnZ0O8_gRpkR3R9hAOvm9RHzX9EP_j2mfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd-5suHr5-LNqhiaKDuOmo9iQZ49BSQwfflGYE6BfZvqQ2v6cbpWjel0NQP8W5HtgYTK4ITOTS_sNZcRgkuUdFW3ULgfmPBMBH4aHIHpXLPAmLcTB9PPjeCUsNnUP6z9dCmMB93kd96Eo2lmQvscoKjyAi1uft5YO6d5LYfZyvPnMCdNJc1-Eyq9AcJI__zr4IYqWIQ6N_oEk_RBG-EotAgSqxw0zzNMxmQY_aJaQohnq_W2ZubD2joAKwRMS2nOucfJ-ciSvUDbuQOFdk8Orx0j0dLW1ry1kAjsYAjPKUShkW24pcCAFQAtsp9e6R6NwRkj7eJnyg2HSFwF5b4oQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmAiIDBqOHZWBPq3xP-LwOR8w9mY4sRcilbxV0FZsR1gPC3zFH-t2t6XBOWe2FoOQhDX0l-O5lLVWCjT12iDVwa1zIged3xU0065vcKjN3xdxE1vmBTL7dyS0HfCIki-U5s68WtDS7mlT8FYM1ezOYkRGV_OiMmw-KUOFDj5JQAhbkoQTFoZKyWaxr_67eQcg_r6HWFBPpVCdMyZYHwa3KLMrYoknWOzcNa6f2Uu15tYbWXVVPGJwhtPlyfeyeptVOQGNdtwpTa0QFd8ZJ91YSgbSbk8RlJRujTp8sdVg90KCdt7TAFpXJcjcA4EIbd2FPzkGn6PYtT4d-Pzrnyo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2wdbbm4YFLitFs0dX7jRIugsvNSrTARN96tEYy_0dk2EE0sMkQHxjkwdLv_viTm4XtIsGKx1Lyw8HztOwIj7j9g4l22p9CGpx6St8D6F3UthSddvN_fFntF0MdtRCq8SAhlae7lXtJLg8mcBOYaoAfqou6k3N3NSrlbBRBDatFt4hHedYFNVj9GLCwmKpv6oHyMzwmHd37J_HlUR1lNCbq0NnGQoYlGWcwfMMdnpgffBm3g6mZPHImQw4BOohxN6x74Q8e_H0w-uMHSP835yhcA8ilWxtVyRB2cjfb74r9MFel5Bh8_thgts1HiMc8tKagkx7Oz6CGp9YlLx8e7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeGyI4t3M1rR6AvNAheeQ0gR4Q_LXDMxoa23todj45Fc55qh3cPhgjaLXIlzK2xoEBQH3z9f6Nm07sT50UCDLzqpX1BEVZAM5hWGBrs1KRCuaqvyRLfxbI3A6hEUcHH5HH6kyyzqiRj9A6_WtHvlWTENfBTTIBdbkygNgGj788MuC9pmkZZVamhngVgxjAWzPSMHfN3g0ZZZuZiLiqvmMJMz53oTnTOk4tMgr_4RT0s7DKM3Vto8YHSS2TlgS_cMrouPC-xuDCW9OWc4clKl8brydPVVMreuz685NEwzdLGkElYVa-OVx9EwMgE4AwWE3gFEvazOTFiHMoEVdu_RHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1byszbYiRy6rg5uWA0kBEXUTxy6DyVrCoRXcUKjEbfmIr2kG9iqQUTpFStjMtYy0n72WqdQgzKjhuFhQOO6-MaHdF1LJ5elkXP4c1WTPRcdGoL-VEqCyFCIDLQEU_DroCcFr4yCLY3ThLj_qPQf5wjQdE3AK7W4UgUGg_IYqZvI1mkEskOb45CI2RaxkklgWUJnRYlVpycRoiOTfSemimkf15SCh7fnYuqLAQrZqMJ1XFkhergAJREFD7SbV8-tJo15klmMOwjyJ23QXtDpMm68dMTQCLHuGKXuo2vYxsZFjCcwalIic482QzjVimGgDECC1VjpAUWeqfiFc9J3AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzkXRnNO9MRy58kw_os1Bv85vVQbgAu-KdU1iLRsV278rx5qtf9srVx-nt5Z083zUWU0mrgSOCXUkvAu22sf3xhkJv4OAaO4kVaujtN1zdnYmq7MioMSTLk0LB-lI2A6sBOq4hq5dIEjmJMZV-ClsUZcl55jWKhziRBpOLRmE1zQgFThuVmhL096Irlgg6S0ENzDNwyi5hQ0nBXBZpX2SyNLKvmVgEBQRevgFJPvUjub9YAPOZ_M61U21XtRCMEPr9krAu-MvW8Rkul6RAhknamzBUTu7yGvrFHGaqizXyopsl-EP3ulUOM7x_pZz-CvJGSPzhPJdm-xsZjCwrh2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwGC-_c9sqAodIQsvtwExJsFqQJP_J2LE1BievewvvqArC-PKglz1Wx4tDs5xjujtTDdwWG6GRXB5qwFxZcy9ViNf2amalJTMIeiSfk9kCYazo8oD2p-raJas7h_VEE5287mewgv55Kd8M8Po8I4_gsd5QTfqpZI8k8-jpYGFxjI0Ws1CioyUseeiZ3A1pHA71N7iMeqqZEFKjBCcY_jGPTG5MfD2BeCjfAHF6ZsDThkHAJurXOq0sI-ie3ftyPqdoXh2A5j_QelRKL4CbrGMqE_wDe8McBmiO7k2ZC5Sh4Yk6Uetl8jvY4qMexUBH6FOO9JMNHT4Pz7HgdVyT8GYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppgPapx6Vpz6wk4OfKTl0EUstUsa3nrywNRpfZV_TLsXe5YAHYLMpOLGgXM3b1IixkNnS7PZZX6kGtbkMiwCkYWEa9wj4K75X6sDYH02umTNabQ0othSNbs5X-hyvBRa9g9SUejUibbz9NRbfiXJ3BAvLsQjm8YVwH9zOVOQ_tRqU8C23RhYA1pd9majPD0xt4awAJa-mR9dM7p1H1wC5YydIAsjyctKplODraSqYUN6sEsWmUV2b1j2avO5Qn0a5lgN03psYQiwoyYKMWJUzReCnkI5RHd2gUPDUI16R0Uj6up4ihXfPWOO1nhawatmRY7L8C948CkXKkXYQg6LTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e75TeqxJKG8aiSppPTXhTqjcXMl8yv_CdVjeUiEEquu_oOG0NU2wWypOyeACWZYfFdBI6Dsl0SZNgwKT77RYaAkgBDfF6V21-IxP3Mgoj0iMWC6HtuAyyk0uuqdML9CvOCCozRse6LTQ1eoPWPm7EYrQLUVuu7tfeawd1MZkd-dqdFd-4l01VYwfrShtENL_8Sf5kSLxv5rMaOaPazm9bq81syEYlbLcj65-AHmZf7GdpxC7bvpDH7JxP6zSrwwSLHDFd7v7moRYnp3nptqwTUcTj7Xl2NiKPZ1g6C_ast6uEbJZVUKF4-7B8MgAQNZr6Wb6wuYA_ivZssWA8zVf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t97FyZkeajSMzMDG1JddRfsxvnWgn7NmTlmEgL4w4k3TnUr30drm2nYJMgGX4dCyNWbuHg2LaIDuKcOC47sBARZ0aPpTTOoWcsWRKiTEeBcdQ-PefnPDa6lthbZmQQyHE3EWUMddumdFg7kvWVfUEMoSCxbwMkXKh1ubGDalWeZ85i1oizK66J6QBliJYZpkMeEw1dpxnDV7wrvEmQMq_NPftczq8g7IICVAebXWSwYhmW6YOTK6te3zJXtnMM1EwXAGB4-x_le6tacg-uy1bUmMKKuGv-Uq--9w4uZtVHwBm6byK4OTpNKfadCNKWwjY3ynmfm8p5e5R9ZkvYToBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNLNdYbzLL9vPzTVJI4SdYHMeEn1Y4rUPZcc3aVIsBZHetk7QAjy-okDX5tsKrp9toLPKap-7DjOrB-m_njiHZp3-JbhyARSB6iGbXTO6JJxOGUc-0Tj55--hSDzEIc94cyEGAwwfxZchg8bfzGJXj_5LZNT_apTt-DVoa4dGw8zbU_TaeiSsu2pPbii-2rwb3NbNoMORb-jpH4dtD70D97W2z97lACboMueP-0TU0aNMSbcTm9R89aDKl6gBOwX5FOrkaIXpQbC_a6sJe2SJKw9kvNUFLqxHl1pvKvuS7ytY6DVMuFETjlBz-WsZmxmAvaPfgXVb1GWFPXJZhTsdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vecU-VmtBWRf6mJP8Mjq53YeKdDjujCg3TwWw1wv5ga__tzyNfsxwbIG6PUTFNr3c2s7myYv3E3t5q7AYrW6_erLqKILg8Q_INHNXd3dsvXY1jVW_1h7p_pIJD_TosmWouy7JUHryEKzCcTeKOhWZdKy1O7WMh9BwocjHKWbE3rgAbQ-L5xOnChbPXM8xpVxLd1GYgFd4i7R8n7AbPugOy5FA3bGjSriwM22px_pwIivJZsftxniQE06BmaIrEOjlc7GWKITYsfXVf1zZScsoh1L3S7OxYTvTcYtglsyPG5T_cyI-ZDM0zJde2NlrJEr1CAoLDo5ZumFlBc_0pauAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdlgI1alGEyHbmFrnAdd7rDqeRnmiErMwPlZrSnE14Agn2q0d1IXz-3GSFLp1eFGQwdYVd3xFQpv9ZSlfeo68GWlQtFYdVwVWsiivv16QNugmG_uMwyycxiI8v4kTq1uFfFQljUOLUEFmyOH2ZhM3L1XGxjPxkH7wmmtFi595dCBHYx2Yv9je9OEZ1vBMK6YWgj-koj9WmvtRhW-naEnbV_dB8AmyR1IyrP3K9610nC7Wj7651uY8212ws4fk0ZZ8SYdzkxrPMY5r3W33LmNSuulDnB5t_6KGYIVHB5WtGfy710tqPCqg3gutPMsh3CZpIk-65VGOjMyJU-wBjDdyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saeidYapDYbdF1pBXeJlw0BrE5nSkIpbYRes_FJjUi5S5lMtAysyONTo-I1O2Dq93NJRZvI1N0jYfBRJ9pjysYbyBC6p3xRdBDIO3l4Do5QyQztzuaN9tjVqvafYMIUuJViLb17zkNtrOLmApofPqaxWKOtypawhz_Bt8cv_CBB9dy1zAOsmtqelNfjfPMYGbAftDH8eF_4vmWT0e6k6IcHqIYZvetjAQSWrhtDYpesv4QLjGiG3XLfZU3Ih6ME0g4sv0MtVKy8GnxuCdnGYYAbDPhv623IAA-okuAV6GaZB-k8DYvDYxF6z9WB8IMhclrVrIG7BKlTbW2asVtxcnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGqGsBZpp4TD6U0PTEmcxlT9BTSmHODfz662RlpaI6HtP2ewFzdoT9COZulh77ekgbODrUX2GvZmtn6OO5-26UJ4LBoCXY6iI6Ep-L_kf0VGfyjhYD-b6B6ETdzbtIn7miaod6RzOWgwRkPetwBLjJNq3G6TAUgRca_6EeQVQSJ4TN6m-sKG0VlpjTq6fIuFnHAqRzRH-r0yuiXR36dSltkSHiEPrtirpQ2zDOSrfTgi8BljHs97HcHK6K8FkFEbo839sfGBg2DApEQl5ckR8wkqqCdFPb813K6l1rI3qctNa7qF4e5ifl3R3vKsT0bXZQkcLcRrZFyiMxgpOm-hZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaQyGMMaP7bEMVqMU4vNXuwmDh4gUn2feD1-wav3U9SZXlVkQbceX0ydZwPGXCjAwll8doeBv1MhRsDuqzmj25hB-2va2VBNv0NZ8IWAmRTIQWzm9cwFqH57gzyOpbt42pmEQXXlgHHbHHN3aQiAHWzDlTYEq7Knke1-6cCWW9zdRs70BVwRYZYDLfGJ-qg5b-nqbMxxqFqV-KBIy1yRNzaYAKRvWDalr8hOwHp2Qyt_tNvWuh5A-hTaAh9sAFQs6IQc0HoaBCA5COrVyNMo6jb9vvb4iGgkvBhUKfbtZzzfhyWnBuzlRUM9QcL8GNu5NK_NUNAZl8nFp7JJATzGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AE0kbFhhkmUvR1ivG6vMJs2zZIm8sos3yDf8EsCgXrGk6GsrIHYg3Gfz17tqCXNrqbqIr2ewi-r-IsRTpCof60C72hoZZoIbMFxpJjt1csejUC-_3zcy6v4q2K6brnfMGTPVtxn3OuJ78_hvuQgblc15VwGq89Jp-JpLqGQvoi7qXQa5Y7mdNCpy9hjadlxm6Jo079rlkFdzRjRsmR641lHoeburzab104I9Titx3xZMrX8M5-LqAYtLU9SaJ5G3KT75eIF57pLHeSgtG5PHtZNuptme4Cko36GcpiquF0X3CXTGQ630VLWrMXd-GObTFRKdjrqQFVBcj41xAR0RqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWuvl-vnRdWoxVoXH_D4pQc5trbP2_-VRpiEL9qA9PoTal8lVlFPRkT4f84kDmcEBvQFOcUz6dKVUuflLGHLOwmHolO9X31vo2lFnwbSmBxbIE2QnUxZQOnqFi-jZgOcFKwqH-J38qvqhGQm8qq7e2t76Bf96c1_t8hgzN5slXNbYNuFrvv1s5jnYz-6oLtxgjqdP6Qze7E62sf3iPt9Pr9zdA0xkiMeNEczD4v3_Wet_uEN5DYijcWPBmP8gaxcjxCfyUtK_xHRVfsAZt-nJq7oIuoRoktm4pIkHM5NPQSXDVtDI6C7d98vn309vVJaBFA2zTyVZH7T5DsfgBX0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMHfVgICxFlQXD5GcDz6DXkXokP9Ik0E3T83SB-1zBp_k9yj-IszHZK4xwCSO9SPb2TZ5Kztlev5tY9yGK2wx_sZgnknczIOvW0kLJU7kjZEn2xGU23gv5PJjOTgSuijlKXjHd3P7LbSUrR2khYJNb3dn5qW84OlZEby2nNS_Tld-2FS8sWFmI3OJUCVOj4tuQosUQYfB0fRuoDgxiOGBgGqzAPN3L3kYB2gM8_p_LxlWjumDxvmY5i3KkAqbo8qOt-lGDcml_AYkCO22AsgFTtKEReWyCrrTJLAQUq_7yTn9mPDeXwxypVozyfFkOigpbCEeawf8NurDwpO8ocLcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEkTi0iQHstiXdPkURgPohJMHaGlzWME8U_b35cqBMpcLQ98wvFQJZi9eDPU-Xy-NUI2n_w8IvX0FWGVGAa6Cce7aT-O-hLjwWk--ws_Bjln8uzripVjPyUZmaYpa4vaPyvEUsDEKUVs5fZtjYFKRINszzbhiUSO5bWXtxZ2VEvfvc3ccnZsnGjVK5AjdvqRZg-Zph5fgzmpQjB4c09c2Pqua4ugQ3vpJtz406DnXg0DY5WS8svTBatW23bwqd4gU7c12f91d-LMXs0FeCIYtEVeKSyjSX0MyhVZuhHgYSv87Z5XWNqRKbkGJu1KFR4gpRAO28nzg59rV8PTSlbkPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM3wvVsxnnlLJ1nP4NjXJdiDTwYwxIwL-9ij6s1_6oxHJrM_N1cTFBzWhqsL4t51nJahcykAoMUluUP9DH6xZDl2675G7-nkiUDs-32vo8Qh6rtYsrGNurTAWggXAiQvbI_2I4vQMSy-cF2gaaQs3Vr7fVRgtehyOR-_svPM9BsRrEwLivR-tDDJYmm0sFPRG8MW3806hAEMcZV5wos8lP6B57Tp4L0KxgEeY1y-j4AH1E0Vz7UkM29WbAVg3r9pOF51nW6ASMYT2KNsmak-UfbqPlONQqWPORVQf9vqkbo01YdzvQDyqCpzrJCunyaaefqjrqPgrGBl5yqyUV8-oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZtG2mXlsZLovq6_QJyFSYvfORQeK3rId5YSww-w3bVL5V8DWkwBq7mrVPMJe0Eq3XdxG5-vdw8VOfW9a4LERpaJ3uUBI1B7BczMV9ikPL41-9KzhavmLAnWJiw32dowLasnwFOE5E-Jtu7zu1lJhFy6v_kKbKChf1dXbklyW4zwb1GvGnGr1EBBGso230ljmFY2QCza7AqdUyAFbVSGvCuVc7t0Ajxu3ShW5ONpNSsCWL0H1_RoCYtA-QKo58vpaBE8yTboPwzsTdAegBGErkMSqP1qqQvid3RHyR9Eq_jid_divA3-VqNHF_wl-jHUOG26wPJA5cgm5ja_d7nxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5juWkXC_v-Z-QzMyy4rgJnnKuicrZdXVpxfdHW5KtwBZBce9YlrZ2Ttz3oDRUWEpOKXFClmmrVxK-axyOarZ8l8B_vT0Nn5jovqGwuVKjHFQfMQrmWUsVxgMxQ3UDT0FwG2d_vBCQgqozAIQ2EloR_y-IrPqj3G6AmRYCXP5YCr8_8E3Fohdvse5NCFu1fynr-UoCrbunk5buFuPbigtwl8rwe6nKWxtUVCWjOzsFQYbo-Bj5BdTeXm2S3G1qfqfszR-ICrKhS6JhwtN15rpjm5vjBV6rsfF9MJE6gBtT4awkvPWLKyg3ZxEIMfeYmSBN03DJh1HpIXBKNh7U_JOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4VeKDu4mcKkPjqxjhB1t4E4CKReLh14iiv-KDHjc8Wqv9S7aoZGgM7kXdig0j8U51A9Anb3Gex0ahpyjplADW6wrKI7zkkBV7Fk0iOaBZE6R9ONoCpdZlaRsAOSD2_ymppwu9q9BFu0KQ4IJPts1KGzOZRymvCBBmQ_wEMEyxxNtWN3QFO24wpVlQGXjyJzEe2ZQQ3Y4QDvlDrgaKAYnzQ9HANqlbp7Q1kBtCImSWNGrv1J9UvVwKBdAxyJkQLjGL0LcF_gfy_OT-ADCh6Yvm63fVnqaV9e8Di6uk7mnFnSLipzU4ZYWjVEt2IYZFm4HExu5TLVlugdMIhwvk17RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vepzUqHYDbpks8k0eYMB9BLCg9yMVw53oXly-9JUKuzmBnLxkHBHpx_qD29VUimMxeQW0e5ynPGm7gaAD4pXc3bJXd7DQDf_qAhnEbsiu9OuHmKgbAAUhS5O2-zTsxTxkDP1NCMy2mH3XxqjR9C-ePW2kmvdvyOXvc0uYCIzGNd5U80dqAR8E_r_uxV_xg3uvZqNGChmT9Ygq1epr3s6mHu9pUMSQuVHw8D_xw3f470StghQ_nNmcNzVOXbEBV5mh4kcycAW1b_7l8_xSSjHKfN1GOxV09SJ1DoLKKu_2uHrIQl8ZYeZ_avg6fyuP7oPB5HQrxlGS14qEURnnd9o0w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=WfXwDEmlj2ufh_OP7AsFNF-32LZ2bTaurAk7cRKCwG2DW1i3bXlf_DK5r-TTPTcDH46iFGweUiRjC9Nwh8Bt0fmhHKM73bXAEGVBXz-dP44HwnnV4GXymyXu1qgZTRxzbLUoH_9ZXGJ2UvhLa5OieO6ETkmypyOWP6PUX23t1qvBJJ_vKGYysDxKIflQ3KJYQs_N9330Ol-sPQCZw4g80S1oSi0GivjA22ZOeJfdIG31r5Hzf3b60LjDjzGjoTK0ggcuh9Jq6olxVRtF9ubsmhVEKDt52Wzyzv1VeJorDJZamFS4PusHv0TVQHkhNyMXWje1XWeG7vaLut2zlxBqwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=WfXwDEmlj2ufh_OP7AsFNF-32LZ2bTaurAk7cRKCwG2DW1i3bXlf_DK5r-TTPTcDH46iFGweUiRjC9Nwh8Bt0fmhHKM73bXAEGVBXz-dP44HwnnV4GXymyXu1qgZTRxzbLUoH_9ZXGJ2UvhLa5OieO6ETkmypyOWP6PUX23t1qvBJJ_vKGYysDxKIflQ3KJYQs_N9330Ol-sPQCZw4g80S1oSi0GivjA22ZOeJfdIG31r5Hzf3b60LjDjzGjoTK0ggcuh9Jq6olxVRtF9ubsmhVEKDt52Wzyzv1VeJorDJZamFS4PusHv0TVQHkhNyMXWje1XWeG7vaLut2zlxBqwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
