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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
<hr>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmVr0jLW27hdlePlFJ2Gh-bmm-OJRYF8saisnZkAK7jYWslSAhMbjtpAbhJTJcwfL-x-IYF-HBKFE2iVGlEC88SonyoARJ-NMuxvEJZugxm_6lboO9TS-DqzKyfTLJuGfBEar4wxGXO3RLI1CKG93r7wbOCjHdnpy44t-7jyAw3qu4rvC8qXOn1lkTCyU1emjDW6ZmV7lJ6oWoeDiZY69nBhusFJay7YCe6ja8jaxpSt5EQg9Q4Era0mbOWGhzJfJJGZTT9dCDRT7Y9Tli8ECQUwoYAg7WLZDGmYtggQY1haIBMNYZPYP9EJq6C3EjS1sOercTMa2B6UooEuKt9X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 480 · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 520 · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8063">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑨𝑺</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Game (1).html</div>
  <div class="tg-doc-extra">5.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 540 · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJhjg58Fj09Y5eTDcZt6o_XBbGQW_xhdx70keOjyE82xwvxJKPpy4h0a68Zjcwg8ZqyJgt9kRMkEUy9UHDzM7Rw4J94oNoI51EF5Fd1me0sU6KyDMmfbeM-6yF4HKmo3KiXFhz7PjOKBiI0Tkyjh26K4CRljARBMAwOkeIzhvMYDM7lDzX1JGIX3KWNmh--VyE6hlLWXtmQaPr_PzcVVe9oGr5_DgojLjM_lHUdSIAsImKa2vN5hpKomUMkV6wso5vEz_Wt8YSh9AZmWixRtu46z1qx_RMoYOF9urxLw8bYiC9EBHAyBHFbUDGs-PwXZyZ3u7NYAPYdPyzV_G3-YTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6zKcIty2SlkaSq4dkosYQjLb_OyXVsLOtCUnIVTFjQqMzznJ0LYEphEvg3zKz09IqNV7kz8_jTWfNrh42sdGpJOkmpTaSUlDABElPT7S4sChvWCYQ-FHyEurtVrSp_ojF2ivxzWUMBJbOPxL-waCoqlofH529LB8zF7Oo2fcfX6Gs7CAvPxYRSTQ3fwtSu4HUqYastesQ4l3JujeVDypIGrBIR2-dds0mUIYY_U1eFR-X_lj52OiiKSl3ShJAW5whdLhgFYM3l_Z_PQIZ-Jls-0nS-KwW9z1BLQdLBUQvbQxMDCVlOc49tviKPopygS3wAO6wlyb9Fybml6HGpS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwjius1NvGV4WdNtNwl2LtTEQtJxzjt6WUdm5OWSLlpyYzI5NNEyp-HcIJ63KbAqcQpIPhr4H_Fmhf-zcSup7U2PQCazmDcXtduOcMeRxcGpMx-ptXLNy1vysCu2c9KbWJZ0DvIfkK0t6FBiu3VrdE1v9gf0IrW929ciptHBPTgieDKiSQvHvRT7butBSLsoXbYGqGrTdvS2gu05hQ-DFs-_IqKCOd660vYSW_-vXBVdT1IE3zB_WqVDQvCRx6O-WMwo9fFTx3DOIBOUs1emhPuhgK7tWLTbCR74fwTIBIXFlh-nJ-AjMLrMvDrQLuA1w3gTT7BTKsmxJ9C5_Caf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soeJtw4oNaty6VDwGVlE3orLXehT9JCHb_H4wJbNTKSb6cJ9A3WGfhQT8wDGWour4UHhivk5rqy5BixCZjTEayLx0Rr7FoVanE2rGKm79jv6_yhfJdRI1ufnXO6sC5uhON80LBFiFpa2tJn3hndgvjAFiALcEMdniu1CfsSHDT8asEWe0LqVihQXRRntJDHw7_T0s19MuxYO7TOPso3SQDnbxvGkTN1GqwbnrOHzCbLKf6d_Wp1cpoRsKRejP4OoX5ekhxJYJnBj668rIET1hBkkG91unhUQYfDWdkRy817_Eu34XoCDjlgJNB5KTYISBP_q8loOqAPHXuCHV_q1aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9QRC-2NgiL0mYQCajC0PyjGy0nvKXv4YPLt-w6_tWFYwkCFzQdWolkKTqPKovN4-8KrDyijtUiv4tM9IYRrWmpu5pye335JUjzTbiFBrof-HgQLrVCrXFjofRcZPAVAXoCMLg0JUT7xuRCb6qhbUZoKxyYty4XZ8ObhE8TcF-cOoCBmNnJ0cw8UHMHNw6QbQX2DeURdLksrDU70sLW86DShCpkDB5TEQVXO5ntFs3OnpWuItJVXTIrQr8Dzs4L1CD-XhSaEsw-99DGI805X-a-WYbAn2B64oYpDt4CNnLSvm-mSuHOAg0YkchEsuiwYk5izz8bjjWtruDSPcMIuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSnGuUUXuXMnn2bbr3Uu39sE5BV_uUQCnaKdCPJI5Km49g1dW5SBizBw9-czdYjKJ2wq6ACYjb9fXY6PPGRs1wWNVcRO1iGg8QaU1dfRUmyjijjfEyyuiuMwKtNodZ2Kg33G0ptEOKgPCVGrbEfvjbZLErFH_V7PTF5OEwECQvXG-gUri6UfrhgJlXhrcvyE0y6JgtXlvhQ1DtzdVPSSvHWkxb5ZyYOwsD4YEOSkyES2Xp1M40VT_HJmfKFBqGzLlo86BZ-ttMz41v1Kk6DM3j8_SAJJ4HQg5jl2qrYoEQGSGp4ACSfFF3HQUiySUBdm-ucNVQuvzz-M-3bM4yP25g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=qafh8WSWXbNro7U1c2F4ubXyDyiIWsIvd0xjIDMIh6osg75jzcE-8DwScaUipGHkJpS0ST5jN98dLynrsIburJJ3vRQisai2daJdV3uWKYGyVrXrL7T_3hYAKKGl7AnfpgvcjQcRwhL5FAg9AosXU5MMuh3SHOj4OE3qEW7SjHfihRk_2qHAkeLkFjjUrxCHjdx8_KnlB-xXl5JS1NbHYRt6-yVXkhGR_ywf0m6raWgWXDYwaoI4_ffyTvGEm6WYhtGBroHQZCkIbEWkRI5BTJtkojtqr1AVHenkCdr1eABNYXueqcjQRijg0cnK8GXkc0A3RD87R2nufjy7yi6ZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=qafh8WSWXbNro7U1c2F4ubXyDyiIWsIvd0xjIDMIh6osg75jzcE-8DwScaUipGHkJpS0ST5jN98dLynrsIburJJ3vRQisai2daJdV3uWKYGyVrXrL7T_3hYAKKGl7AnfpgvcjQcRwhL5FAg9AosXU5MMuh3SHOj4OE3qEW7SjHfihRk_2qHAkeLkFjjUrxCHjdx8_KnlB-xXl5JS1NbHYRt6-yVXkhGR_ywf0m6raWgWXDYwaoI4_ffyTvGEm6WYhtGBroHQZCkIbEWkRI5BTJtkojtqr1AVHenkCdr1eABNYXueqcjQRijg0cnK8GXkc0A3RD87R2nufjy7yi6ZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFNpJ91BZIBWu0Zn1KNcwQwtNLcFIihKgBDvZaYhbxT7qHt2pjB8i74ZZzun19gTJcX51XxEbu-EfRmxfK7YV3pgG3-ck446SUb_j55-2hoQ20QxUZXTOippPhHs2TvkQ57aivnkoSkedumRL01Naqjw8NfYB5o3RDlAiLo8Bfp4ACdKcuCABLWWhuJY-HrSg5a870jF562hlfCQvs_ndu0tpTIdI44jxlKLhI9ok8_u2XS6sLYeySfjZGkjgoo4T56-ofXKGnwiARasYizR5VT8XWvTLrPdWNxGP8vZ_JSJBjYm13_vrFIS5n9CVuq1hPKEs3HeUw48bvCXOB1NMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtUQWLNigYzAgVlgvRO6DMbVOzSqvaxEd2ZANsAYEFhy8_HyEvYE7_ov2Zc5-ZReD0L9kT85L5OXcTYSTT0rwVWzmyjECvz90YtmdpMhImaOxvG2TY9L-CkxZ8LlDHfHMlVEWBlp99QGQ8CeziUgaCgM14Fr4mtegv2m6BC8bnwyjtp0jLlMkd0UbhYaukJxw9Lz4zVnRlLz48-WPmZVEuV1vjv6gDwcW9bOd45UaetJIAGG1T0KSg-bfhhdsO3uo56GxfZKdmKlpA5F7XRVnoJoGKc46xRA9BIdbeL_h_FbIShEwcyR1OyBZW4NFnOiPXEwa9BCLHsPnoS0_xcR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBFJx172bcwqYyc9YTh8_MR-7CEIEjip-t8FFck3xH7LP9LrfRprZIrmGMz9crzXoe1DlBcgusLPmObVG62tucgQPFLUY3c1RsWcGOOih5V2Q0XgtX4_lnjlnj7LyALLzQQmqBivwSqBBvqeBZ_gVPqSfxTD5Ni_EtHSeOHSDrW8cbt2ktZvEhu2RqVYdJTPYeZnwayqnijnub_QkyF5woy5_2tP7b0wAd6tSUO57fyf8iA255lnj55ICqkah5hstwgYsis7fALw9opfjbAOV52sG4tyyDflizjNh91VIa0A2g9XIS7vbkteDeMnj4WYs8vVD-V8TjHlAkvH3WG5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sr5Y3VnET-P1lxxjZ7l_6irSUeRixKykMwlcTwhCUbpF2hYRCQSUHr82R7IXYa28VR4WdkWUAezx1NfizQaByXSOWeyn5qspjxnOVbako97qOzdlvS313efQYc0L8z-_7vZkIjL1mq1REPU6Dc9qPXuoxIQQdydReN4CHjHwKP8DInUleQ5olfamRJEiEJZZNO_wpjpO-l1HIqhBT_Fg95k12QCEkHVvXCIIJEnBJV9jTrBhluKWHUrHBT4hVZmt34ih20wZf-OYYsEjqfugHdwJjWclTUWzb7bLrDvzm0nKsMetPaVwhMUomIvxFyHviKvLqQSmZDlNx2jtSnOggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzwGW0FS7ezXUZ2Lfp8vZsMgdjaCd6KSTO2jS7HVhubX_3Q5bDTSqstzg8F7MgL8WCde9eFT7u6UphhwPsJwbdXQs_qhmcuxz2JRBIKn3z8605axx-hy6fbpoVO6YFlgM2-koJfgwTSWZNIxzRsP0ObnhYYeq7V51wqjZSWgf04Z8OVP57iui9knYH7FTv4ft0vAz0RC84bunlP_sHqEF-qH1QotwYRO2bC63XEOXOQvcjzpqV-ooLMqVmrjYhL_Te9jZVrHWIOuNBINUnpHwUsgTMZ837cYZe0Je9YPb69AhQ1HLPj4gaP-w7ys4BSfCkSK4Q3hFiRyMvjkcx8D7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVQyZrNBzRfWbQskwowrRuHyjYc90MPJ-cZQLf4YAJyDo4I_8qXsaJs8U6_KsXZwC1yARVSHXJWqTI6FCgfikdyCKhnmPPNCPNa0QSEZyFHn9qimVEnGMH_7DnHpvuCvO5ZamcS6j6BbX6rDEyu9WAhDa7AwK7x6w8xtlBmf9az7Vrgb0XHRhKdujmD9gUJHETZdsBnnfPrb08CmQ4X7pxR7GxhRaohDP00oOpsLTUhMiByK6WZiBMI5M1taP9yX7ryCrKegfDQM5zqrzMMWL3hHilG_pK4zMEq7p2kJr2SHmy1Y2l3LwOJTfkI4bq_m5wZkR06zIodZ0eiawj_QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRGcp_c43WWvDGm2dl9AKsKvEdFEjQHfUU4jmfz3xtkgoLNSaD8t9Osulsk0sPODhtcv7yUKvgP_KMH0A9UE5yPfdTMSkbtfPRjxRuuir99sbAuPJbxrZViughJLeEj5KXJM17f5AOZEhEzqYkbhnbfcX0kg9U8qhcb3qe__fYPlPPNbuHNVrFdDQOgG1abNGoQyxdJ_0p0usXxaZ22abO9l0el84DLSLM00uSHyD1V-g2ogCwnECimvjKkvYL0QflgAyqNuI39-C5Sr6k_V8i4ZSp2rUIpnKTT1RmWFVno885fsHzluZGX73XXlvvdAZZJmm4FQwnsZzUrBlrMiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nu6l_B9tUwM4rmh90gyUrIDQKo2KZlwSe0_xsILibZOJu9wImrwpCvx3-oThhAapoiMwQyQQp00eNuvkWsLeDYE4GRvLZyuoDpKMLY9C5SEIKK5xHB0zGbRhiyuovLf0jpLPRMSXiaMykM6dPKV0Za1HFk1ryTFGYYnTAyQkYSrbBfkTxp7P68ANqnSpw3Ocqx9U4AYHp0tx9Ikhnkqt3ot9EqY94yIpWkiz09Uumlx0gP5ubCM4vtRKNs1yV5FxvGVWdNHreWIjxCyrHxuwk8mLSiMg-Y3QHFy0pVkShtIAQRsR6XLdKR7WQFbzqYTpjQ9sj0l17qs-KSc_nvX8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pyks2zS7z47gPQd_xFimNNZbqj34mxCQJtXhktm4JQ-LWnLSgRsFIAMhIy4URDdISrWO-k_6x7OBQf_uIjun5ehbzFmHf4uRdfMoeI0UMy9ra0rw36ndzQdr4mAjj44y-v_JS1nSQ-fHICxhhZpThhVXYSCX2YEfX-fGs1ezc56WevB_eRu6G-t6Cp6OhMrRx9sniYLQRFULLP2WZ5oQ-aZqMuIMs8LRNGEwfgxATNTT3X7WPL1eVHEURIop2OQJyTsUNxopLRVcZCRncQp9xdMsLjStDb83WxtJfta0fMSdcQQMiuCT88_SGDpIXg_hnLjwNDsRnKP-HGJBmDDaaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-mYNgcacyvLCa6o4rcKeqfTNCC1EKrmwaqY6SDbKjeSWYs2saDwPwwLZWXk826DwH3pJqky2xyLfV7PXxehoFCoX-kpLoYV_jIptFxVrqk7Dj0-6lAuF16D_kZSneBW9HZ4sNId8jLmdU3rYb01AEs5f0kP3h9SzDIX5sLYxOMGHrg4vyI0qf8vN2cgY88xSWCubiA_BSHX73XJF4H93bJBsv5iTnUwo0oXjCxnVuewdIjzHzMBhYYgyg4Qa0qL9aaZ9BHAeGtUSIR_NiGhpmI6VnO-0Myu-Tr2q4YGwRpDvXmIqipUF9qF811gipDt5jAuzj0-WXnQUabmYkuK3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQuqCJnfN8fhwmYFFMGfahb2cRAcKj1zOMcJc9KDloJqd8hCx2Xo_mHCH8hmB81KjqD2715lJXu4Me8Pb6zKNNbTWSeRTHjPLpbAw2Z1bztaS7o2a0VPKrUBTxz53NLJ09KHkDef3JeIEA3yFysIJ-omkc0BgQtnnmiNeybpqGS3gxg3nd4ub4ogq0mJXQ97B_ANNhl_eok0KQdeek2X1aVKQhEeFGxQNMNMtVcWmJEALFrpWGmDktPiIsd3-E0NsBZ-aj9f0SWZo2ZE222R5Ll4hJepv-RWr2Hmz3smk0PNmDlEUNly2p1h_ibY0qsNJkYEucDTy61ZBxF5hCXlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4FRS-o_IX7SpoMqALc4T7hczGONb2RKA21QPphUcQYkGjeN9pm4P6b-NpCfXsSVBAejlR6e96OYZa5UaIBcqOPHIlcqFHVe-3ViocxZROPWwucqjH56DBOXj4JusKQsuA4wIBFi9ovBhbReXZ_xlbDJkEuEpuLxmNfoPFMvSc55AaZ6afxuFAm5t4hmKH9GUwgrZv4zBJlnSPO4duGcoOBPOgAYMK8IGvX7jNDXgCBfjgjNowWD_-lGhB_b1UP83SO4_ubmNU5PFOn6LruV16bSrK9sgUG_4_WnREY8gFVLuIDTlcKofdXvqsaCHIcACOz6GAQJ9Q9dKjBm5hCzMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbNYD7L_zdc_dEl2qHBv_-ataPkepH43iCMQjh5nQC26WxTT5byuZAYihRTyjXBs3ANRWif_8LU95dOOsypywKYTbHYbur6L2eKjEHOghJYEru-Cxqw3gRgCEm4mlPzLfK65l8fWRMtu0VjdBTmwbJZiVGai_MlKHLjw6yRfhDo6YXI07o2G4z1pSEPO4fniWhWbTomV72wjk5PRZZeze8pdB7TG-jJqgFpITWloC2kgUa3iXPR-SI4LO39r3FcCLNcvHzOwd0zkNQ91omUuxTBp0XP5Ycw4GxtdZsrrw77WijpclmKRNvKdEVfpUwL1a7sYfohfFCyKuuiNdCfkxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fNGY61vfUyCuHuAzFz4DVljSd7Ypj3xugQO8reR-C6Wp-uM_wUCZwZEFpKpK0AzNXnkygnjeFxHKOTXjsIL8bUcXtuNydIQsVIGkmXRDDAcmXJ_xcKyW6eBj6uspcfXPPsZMQ3FtwBu-tqKKwvQcRWWy45dgVYsQqh7H8KYP8oZUSBIOrBxPVWpItOoWyQxZV4TWgYoltcX1rrhzTiNKfme4QLP5tyZfwHw1MA_R_s_zDrunScLNw3b4GlKcac-kCQ2-Uh8svVnNLaaR0BPFDfWzZlf8w_QuOV10K55d_BfYGpnT7GhVFRXUQ0SkVMoY-yFNBz3qMKzQ1_rJT_BkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fNGY61vfUyCuHuAzFz4DVljSd7Ypj3xugQO8reR-C6Wp-uM_wUCZwZEFpKpK0AzNXnkygnjeFxHKOTXjsIL8bUcXtuNydIQsVIGkmXRDDAcmXJ_xcKyW6eBj6uspcfXPPsZMQ3FtwBu-tqKKwvQcRWWy45dgVYsQqh7H8KYP8oZUSBIOrBxPVWpItOoWyQxZV4TWgYoltcX1rrhzTiNKfme4QLP5tyZfwHw1MA_R_s_zDrunScLNw3b4GlKcac-kCQ2-Uh8svVnNLaaR0BPFDfWzZlf8w_QuOV10K55d_BfYGpnT7GhVFRXUQ0SkVMoY-yFNBz3qMKzQ1_rJT_BkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5B1wX5bNVF8er3Hn8wmLoerrJiz12LIMVr5RGumXLJNjY2TxmY5eidFRGtcyAO8ihzYXcXxg33OXXWasnjpCizKy-UEnosuSC_akkZ9MNBG_doUeXvAGIkgAeBdFWIkfDHsQJ5Y_xrVWpb6n9w7hDiU-oWRWoGEntsr_x-4o0anZp6Xjgx30VbzrfDNZbKOVYF6qxAu5Kw2nNhmuXYRu5nqc4LUmowtAIh2FlcSaeviZPpDYmYVFayYXXPeOeVoYD34c3MC5WJf5Yewk-7-lBlnWIbY7XsaS7T11HNTtnDzG4j9AdXuEcLneFGViarShwJeAKPgIVP5gXiZ69FyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqs20-w6yqn1-dUq9XVXHTVUKd2ez3dA-ymMMOLqdBzoZgspfA1TaM2grSXNOfVCoj4u4k9rn-nsrq1yMcwyD2RgAT8nWBscf77C5Cmkk-cf9U3iacy8Oh1NWNllTlipP63RWpuTV7HCtMf4J0GNCr8M2Rd6po9yitHpvkVXfXlntGM-rXmvOZK8s29EqH6MJ2-8tb_Og-AWjACxDH74syJl68Zq2IrnkbgL23KKHSEsubrbt2p0d3AB6KCtIVRGVGNRLuAT8W4fBaAxrMRbpxOIRvskttrKlvMWIJpzfs324XPu1hvetn7kpwFXmdx1rwfO9VqvaYyFn1DVpQhOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTPnnx1MrwpNAYT8jwqhv8E3M_bFCv09moyNfEroIZ_qeD5xuz472H7mX8rJ3Z-V4wozBXENbLmrFOmgmkJ2xlEA7ZPUjbecI1_yC3TrYYf6U_sUpxEh2o9Z51VSkDzt4dVinZ7J0pDxAgCQMJRwgHdql8MtiFZhxYY7uwtr4OkGyx1UZNnadVJkNUPvNV1vsbYGtmxrmUFMPLIJTWzA20-zphcDnlW7WZULoBo2h7AMIntvRsu8DsZxYEcFCxaKE5Q4yjEPkMOOCCtwjxqCWvvQRBLM2M4fvktMF08mZ4VGWJVB3yTB2Nhb1lpi6SGRvsYJ1tFjTjzeNM0Y8JNt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXVVFq33aa03hpfK7dUGwyI5rnfBsJOjo2SoZbMBdsTTHr3WhFmmp5PhSBERFZGvmYYmVkQzOTMAtEGD7K_l0Nf-XfMLJLZK7Xf8ObQ8LytBtkiDZcocMLOUSgQH7_I30U1znkdX1wObcCmcEeRaUxFuNK3ipi0Fu5KRd_h72K_c_rb8DaFZrtjPrkkFxzAS3xC1nnO0kmU3BF15avZedXZQM8riRkBkbMpf4JMX3Pgk-V_dqDkhJ3tUk_8f10-dWCoJTa69z2e8RIkwP7n89Ite7b08XMnhabzal6iy3RaFTYSsqu3x484XsCliNO9msNrgl64V0a5xlEL_8fOxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwJFZJn0H4XqP0bRJMJeO8vMOU6plUeoD3nhr4TWinyIeSGcWt1YIarJZwWEAN2tKrAr0sNPNXuaBOl-wpReRVa1SMsUo72-uKS6N_MVBdKyUAcTgMLRO5w40Hg-3Gv7OJ7XB7pJFm9VEoaGU5V_zLMpRt-CtTV1MOECSaolT-1QMFxaytYZc0cjK0z-hhDmc76tF8nNo_TVU2epa79jjVGygos9TfBoA8_1fSkDAxRa4GaRyzeCaUQ6G0xscztiioz4JJPhx9e4gEslld4a0ot6XCx4K_MMIaWfI6xNOjst-Mw-_cCR3vV-sZJfKVRjHxCb984Uw7mclhdFxh-M9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH9yZIN6J9X7aeP1omPhWUWibABwi3i0Us6CGlKfoLmFE649FShOY8CM2EI_o0j4--D0uOJbbp3_g6ZciptCgYlFfJ2CDsMoYlGUC73syA-0ByMbp1gnM8jIKT-XUo-rBTsLqECMYQP4Dq5hVxE9a1fZhxVn9loowwgf9yKIlDnD952Tqw82cdJUQJxrjAjPM6NK0Fu_R2GI5ycMOxA8AkFXu6BL7c1s71BOxjWJ2LlLp7x3nKCV7ks_DmVPfB6QEJONNh86D2KgdppLD4kXP9bieMdiKkpOh4gY9EW6Srpfn91ghxeaYnlmngzTghZ9ceAWk8_sXzq7SCJPt9hOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIQJ-vsNu1I456i6O6q1PXAs4KxLtwxQDkREifjTQKVVoOs_hMgHoQ2Em4j-hDi_h-V2vptBkJC2dw8dF5oCeY_ipGD94XbRO_K6gJ14i18jA-_dZlmgJE0KyCRtrEEMh71puHkgjQDLHOXVfntYduBWvI9972xSbYGshH0Udklh0XD33LYa5pohXlgaoNmhcjxADuP3UgPruxHHzAbC0vJo64eLKIyoY_zOEUgjgH3P89gP4_vea4iLffOI4zVkJOG9cv5Sm74s9IVfU5mh5QvRG1u8iJazop8N0XI41jYXJnM4dyrRUdkiswsSN9rBFhTevKG1kFrrnK0uPqTncA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ch8LvLaN4_2NifDCb1LBvk-LwF7Ocnwu5PZQTT7h3eHRZsflUVrxFbr_mJYQdqX1n8LXcQ8VZScHH0Mx_X7wF64mmwd8etFOnGZc938DZk3wPSB48dt17TSj_5nWdFsvwQ4LM490B6KRTuBOrzFLC2kNpiz6ib1k1IbksaPEQI3oa4rtyxcpSNk_99onM3ekGu_C9ZOekTAvwiJjdHMv_NPy5mBaY-NtEzeooxATi_um_G1DaA77iE4HDymut6Phc4GtHeZ5QgORuo-932dtRLsuvAxawmLZXk9mIyH0Qu1PhetJBFa1INIvh7MLsD_zqwl1d4Cc4Cf0gyB6oI8KKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krpXIbxDH33qzgWfIxiMufUAw_gF075mrz8hZRuUwuVNwOs0jJ7me-XWjozUg9PHLkuCseZlplhoJIchukx22j4ZtlIAs51nVYId04NQ0IXUetRQ58LIjRsPyD_IYucwHq9vdAiWwLpcz9WdTbyJLglQbYe-Z_hSSbOcQaaUBgM3GLP4y_Gi84V5b4RJogUNKchxuWYHPvhIFuM6Hqu3Kzf4yOhbcF7pYP-9byuLSXyxNcM765pL6GdzAz1lQoru4YXAOvBB92pJEwEBqavfUbZxP6O37fDEWANMUX-iBYzV2xAP36HgFojaRkenqZEq5EB60GWSAwCwcCqTxC_kKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoSxOdGmcce48BsWOCY2N6bTNQ5DzunVrC7gUJ5W4VFLMQHefu8bPZTGnE7l-efSWSXfEeKN0cCL8waOdWdNV-07KTWDooJWp5inQ5PaHQfqZCJdpBFdGYEZrcopXks76q8E12XG6UqfuhnUj2Q5GRf3NMBOnApfBasZCxN3wKHpx-QERgKVbSUJJ4gJ1PNC7MbQGvVIh1ttr-W1hU1ILWPOgdP8q6DiWMie1DPHgkdhvVFHrYhVmtp2ypH1UWq_eSLDLnn0s-Gqmi2SMRgyJ4Tq4IIYf5xBM7-diEiPMsbisPVhBn5kKt8uPw-qas6zZZ8lkCMlOiqnMZRikR0RMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZliDtbMnW63L8Bl1WkgyV_RuxgHOLu0_971xkicPn2Q9wSBaM9m8ivwgzZRLebPGBki4tyUDhcq6lTmu2W30SRMUDVVNq9kixAIYh4MjSNJtQrMAGvTQKVNZKxaLMeBNDugv_gKE5gbdHfYR7sxoKC07IBLkYFegBimVu3KmKwFv91zu2cPItVQuVohshDJr0kmfXmpWKkE9v2huRD-5ujhXgSC8qsry4wHawYvbDssAdVRoGVy9uPVIr0sZCo3xN3aqgfV7zBdOinJfyuKbHXkgDxAfGgnCgLiEzP_6ftZ7Eowavoov1WN3ujQB5mWFXX9XF9up8XHR_Y3JqOHZLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRY_HXpRvjQ0UGpHJBYSZWfZxGqAQCMs86dlMMfalKLFCLFqzNRGhKscDqzLECPL2kuL8evtvvX5tRr2l9hcSXjVuJOLp2fLSDewDWTumkf8AHORijxYC1Kq3d0Kpvncz_P9_azF3NQXeWzOdEPxGlD5m4VPkCJS24-2tTMCkQbhLuFaUAjMXmw0o5o-yceKkvm2RzsCBDAHiLMQjYwU6_Mi1nMOxxBBXAv-6m-FSKAOFMY5xqsWdCOFHkE6dbQiVCKb4R35wNlmTQkWDlxOQ6PwLF3yXor8K_IC6onc-MoxYFQlZI7hHgcZ0P4fze_Ry92Skm2Xs1pQlNkX8SzDeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkECPKoWxNhZ56JN6t8b6E6FcrEzbaJC1eMn__QybXy4acsZcHfZM-wMn99MOsKBxwUr3lWw03Hn8CO8JB7KaXFe91BOgH8PoL5tmzfXp7shlhsCfJoEXZPqy9ZvKefMwuLdCKbsp1gwIKNBUbg7dXRsnhXBrO7P-TEUesx1e5WL9pJp1exGIqXtHnY2PE_8a6hKwrPRZU0B28e4WtZLTulrdbKBFKtvYVfajJSE7-QZueOsInbu-mOWLkrmZDy5POFQE1TRSRqjLDlDDpPUp9Mffdybw-jU4tFkEASyBA9CI1VXiymveGKxu9rd5XCq5RqmEgVdgBbnLMWkN698KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F4WvdHSrTtOx5fnl8STk-xb86l5PggVm49xguDicGRBjKp2Iuo-EHR_gkmSbNSYIEaG3tB484opoRXE7gXnF7j4SXTeh93tEb9gMdRrQy29uN3ZT2fyu5FnQlPLnc8BLN6pEXFcZ_kpkFhshFN8ltntZ0vco988KnZlW9t7xkMVzKlHGIDHAKTOUlXv9T61kF2zGppON2F0mYypDySqZL1AYC1G4UxiSSK6yHZXCWdXrx9BpcU_d4ICT-dQcc7EJ1UjekhPOOGnPWX268X2wxE1zOsBsrFxidb8WCg2xZM5iSAwuCrDzjH1foKiLpLDaYHyUwBx5ZECZlOumIlNHsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_ENZyVPNTAATT6F3hsJD9ymPubkRgD4erViLWoDJ0MbV_z4L5Ya7l3YqL9_Z1708ThWnauTfCNzlv4cP_ufwcqWSCg04_IczlzXMJ-tzEUDF-NXcsaRYj1dFvcVEqza0szHBRbDiGE--j-VNdA5OryIeWysGQb2ADTAhrLvyFvOnaDI8xufXn8OPQHYxchVnzcmHuSgzndZiqe22Kf-9pKmAyCch3s3xgOzOv9FASIqySxMPOHy5M9tD72ZDAcDmBk1rYv5S23uzFKl5LZKV3tcDyT6k8jMbpYoQT0ihxw4ZWSVDcbAd-1eubbkRCab1cZvZ3iW4nQhhby5-vjsCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELa7nxvqu8i0EbhlvfGFzM8Xx3tU9PRdecpK9Hqh9oSABuiULf3lrugW-hwNTCEl9JvONVOss8F0LRXxcOYOOsxbbBvI11WxdhR5MuKB_FPxEwggXMiAW1HsUX2Y1w16NehjBkj9BVTqw4IGhn4cIbHhj2DGTS0i74oOBeXh6iR3pn8Q7kVDUPvVyWrn1bjAfr5X2fYmyni1EqzL9aekwlwl9dJXP2SWZrbFHIBWYENErkVrjRsz61xQxYNTRxGXrO0ItJLT3fzx1EK-pVzkKvFiozm66PQRPAuy0rE3lQIbp1qAkbsLK95ahNT7DcmmaSlDl3ltqUEn42UfBvEoOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhkDNFmx89nI4kRYbgRBY08PQF_hNBXRtigVOkZ4jfFQ9sIg9FTpU3etvSbAOXZPxIePmtlU-f5LywtMiUVP7_i0cgCS1lIvpfuKSg-AL23ZK-JCoIlnfOteoHzBzfDBKNLx1SyxjEOADkUC0vbT90zeslUYDyIDDGqBliAa_6J3AmOCcNA_vEoLWMsGZY-becLX3FZ6UA-isJjcqHWLy11c9XWb1KItuwdEBUgT9MM9M78N7FRFZvlriz-g_yAGtJdMpbunOIpo5vhTdGtulXiX4dY4Yy-hfMMflEj8oQvW5wA9KJjLpo3HW1LhbULxjC05QP2ili2ecs4vfbf1gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3n6w7PeqZXc52omL4OiO3fT_x-5XQCDg6xd06agkg94D44PVdRKZA__GDKBqs1QUWuVx8NVWFGrnPU3vpBV8ssRVUr-l6W4kPUvrB4LKNLe6VrtcOCvSaIpOZjlJwGLZW1fFDHF2g0wZ5nKPi9oj8xHcOnMUBrH-aT8GHlL6n0mZHhSmu9Sn_JM5SSt9ItBBnBpfCd_6rYEEkLCRiay_mFOilu7I2rJquh9KDp_egoAUj8CFWdmqdG5yPFgtPg_DXEaPDYBiT6duSJtBoHkEsRbTKnr5_5IrUHBxZ49PjIHirk0kaITSs2PJdmTXs6gkGICWSGJCg0wYei7oucaMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W1nqJvOZiQKLekEJ6plC3C_Frrt0qDu_OD3iRP00mgSe2jT8b5fpg62LcQcQ3rj69KqSStCHBnuDvpfMSEQMbewjxVZupq7TXoSKjUk5zBf1mcuvLkViqbdwXGMGO712yZVY-A2OomrvvTyPpph7Cv7sfzJBWI2Q02ygX24If8DT0a64GQuQ_-5WJiIfSgkgfwUvo3u4IwxwUNDO5yUbJxqms3ZHr6k0J6XQ22fU_JUlgdmUMIvzBF-nWUFvl8rdHVbd3Zaqob_S4Lsk9zsCeTVriNAuFzqK6X2ijlzzPLsxw6yCyUglIFrq9JTolYBzDMBE2KQDMGXhnnT-nUhc3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd84WWi-O8JUHaQOf99cp-t0rXNmjmjYw8sqjcRsABQ4aACl4eQKAyZQnP66489uwRCacufqah4Qb3Y0J5Rl5_a9xaCtTozf2sMtf1hb_iPvzdb63kgXMtHdzzKHvOgMRHl7FJpTjy0g2rBBNdc5-o6u5A7hg1bXzfb7SyFB4pwB1pGApYeZbR2MtlAcmHp-_q9wmJiyYXsh6jE8VYnmCil_q9fOd1ltDUsbjzDmI2AwBAzC_lk_DdFj8cMdd6asa9gl9lHxt8uqaQl05mCwXuQVYQ8CQ1nej_1YAMFf2-j9x8ZsaFRRh2FmF6wRKpJ_bozluMAPo-PKRTL0kmAu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goCz6cR62WBcO2fVMm_1jfCLqhtksGAYP8wmm-LPgtJJiCWVzQe_W6A0ZkU5yadIfEbEW7WuIY-bL7grGLtUgKDaLyjtcjB1br73F8E0zI_fszzPK-O2JGJy66NtMjMXLpmiRC4Dsm2pa7mUz-1SZGGBGs9NNYprkKOH0HIp1XlHgyscjpya18ND8QOGEbD8PVdK3BpsABH6ovUSvWcxwxSBnqa5HzQ94aDJZdv_lo5Dto_oWw32ujJHAeiKKgP9Idv1CVDb_mXn-yKFkgN3F76Q3i2xg_FWWx1I7sA5Jn1w8D1nDdEHRoDmiZa3jtJ0NBGJHKb8v1FXS6WXvgTeJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB7NqPI3eTBKp3TOd4ACe0OlXDLHJ6ngj4sCH_oCQWoRln8ofg1CoXmN1rrH18xp0mOLofbyeUv-Uz-HWPn_W4EzoLBur_Qqbc56Jx3DFV-yvpt_06ituK9iHPRUJKMvL8ApJyZU3_QQO6eJIphckoExAEezsD2RMAUbBSMhe42LshmVxl50sL4-Jy3SYczRU1SRE6Jy1RkbDpCvzzhWV4d1QJo-eIlKciD1gQqoP19c4P4aJEcali0GCo5aSwBKAYKDrqy0yOaB3xbNDjUvfStk5w2SXhsLuYui694oo0-ErVVGJjrXvf-a-oye7MTCMPeP31FvpwtBF5WHyueBmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwlOnMTMiNjku6_3N2K0WB0rXcPlWLbfQqG8pF9zusFz78BMlCytTV2uyBsn_-4dDHW3-NWDuQ96ANh7BhBIMuM6NbLNgqNqy3epWdtXCGKB4DrCM2GQpj9P6jf0TLk6V-5kneOFSkXP469xDHb0p-ck1ChhDK7QMM5T41tG80evHAtcE-dQz3oqcAlvhlYuUC1cMKSdhcWVn1LJR16l0nYdoTStGz5W9TVAaGZXVBII57nmcJTHmlbXjk9j8K0vJecEKu16_wOlZLwKjwcLt2AI4r7q52dBSfvGpOgZl9oUbe1RFC0OSKkqCRlcKm9YGBk67JB-PTwIgImtWBA4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeBK5tF-qldGLMWRhupQgc3-256ArEau-0WMWEFFLA_bhjYKvkczzmguKEbx2G28thwxxybJZO69v9ZsYeQoTZPwX3BIupimv9GTOoMQGk_3FnCPjQS6JRBZB3zzWPJ_ck5PYkG8BvE-S3J9Rwwj9SkeuuweRLDQ5JlBykfzAfrQRShkTSck8vKDboaX5EebV7JfKmGbSfbHrqEIPggF7tGz9RrrBpwTjsFxFyRyMUyt92GblwTSX2tn1QtfvqissJJXIt6Zw295MpVEPlJDD19I_r-WLJDFjLrfdHFSod4fZiQ2SqNV3RepnVlKMJ4yXpxtF9W2N607h5F1BpTzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch8zu8i25fDmMlcOY9eglaYTwtCXLhGYq5MlLhlr41KPVRS4P4DokPnL0VhmwK37Oy7HLUfG4nB9I0ylxsJrlyXRO17ZjDdoPeKk0X01e0PqT5GRYLKOyBd5h41UwwWbX-Q03M6tiU2Hg-sXIZTYcygiUS3mFK2b1iaP_bOxUBNoPt7BlvHQF_Hgx1E8rGi0C2Q52Yfvw82pjsIvdHZ8AZq1IFBd5Uu39M1YnW8AwvnyElNKSV9VpTtmvTuI0d24sWcwLsvv-r7SgZkKuD-HIsc2iyckJB5FcRiB7vVg6mkpekusBZE090FpkeAFdQj5Cb6tfdl_kc6mPh8SqAjcmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLiYJHEYR_KcenNiH5hCa9OmzV8YQl5034c4Jn5po81AnTihQXbagA64kwOBCb-cc707POtsezoSIM0rFpdVD1w1rMrqQfp8ZqUGmDq_CUDmvWPHj2Xq3_OxIgXAYfElayf_YelLToUDv05aG0QNwxZ6xoNr9WcvAZLArBL7uWA7VdtAl3E7r5xXREpt2AVqYWw-LDtU7lVsdGDAA_dpsF820V4S-TbAihRNr8n1ZqbfIhrLJ5P_WTPPyURSaBQqP6DQ-awr-Ui2_zc-h29BqcGNnR8J0kKMhi92Tt3oVGCAyXHkpnJpBOUjIcG7KGCDKG2R5hFoRGv3kDCuEn8lGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXuNpE0wFTPkEZaJgOUt1i61lSnWKj7Fxhb1AW6mIMsVOnZCYz7FQq4RrUzy9v4JwlYUPCBdSPWTD-pWPpRbSAwp7dKOGlJcuNYPT_AarHTkEGkOTAX0-mCvQhjsdcD0emrPjBwWk7WrrKJRkkxLNOBAzyXxJf2hquUw3vs06muj3yLaywz0NCqZJUbMA-YTZSXAmpLviJro1YbkHYhZ3o2TtjK5lsbJbdXeRCxG4azFUhPu8csQmMGSBUY_VU2mgb6VdoptTLlJ73TNDZvS7WUxj3DSoxOdwgcIQ30-JKJSaS3FjG6MimgEFu3mdfDQWhj57RxS7FsVLN48qupY1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhe2Ga24HHUCB99-CICGyrASVAlqO4aGzIvihQMMgvY_hD8rsl762eIyf9clhMateOUe8Ysh0-QVSvsQDo3R_H3OwB3joJ1fz7tuhzLTQiqMNpmMCOQ2kjI99e1txnsBfK-ilMWIufejpHXjWG7ZDIavfrt30ajNgBtAnkvZhK0ULFmgOdkOQrJelh3mkxRKR50enFD1TYHbgqQwOGR2gDI3Pkdgn-3BLkahWtAc7KtFndbuvwflHSgTuBtAyGUUikx_5O94owvFYScHgzSwoGpcTqjJoupJYaae3iYNlY6KZ6AVuN0NK45_4c1YMaMt9LoH8XHfnimAMyU6ABVhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6QhYzhxy-V1-eFgEoVnxeWrpTJ080mdtW-Y0PK-Tg3M4fqni62EBMfVSNh4YFiNMgHFbhhiNIRJgs7RN8W35Aanp9_Sc8_aw80NZ8qMotE8ngdyi-qodhuPulQKNCiPeU_OuLsoWoHY-9MnUJpnXz0vYnr6YxhrU_ZLu6xSoGmOvnXvvCUwUci7R2wgqdO7qSRdnrLnxEPtQNw07V4QHqd4jBggePA3uLvZVhbo4zaFHt_9_o7EeiMICX5034ACoivAwMyJMrdFEnHkEiG_xrsUNwEqbdMr2FAYhH5tQv4aqVNO_Y425v5APNIwfpnV5dVVMDx_oJaM25TqR-45Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdezg_GNRRkjfNxJ-Y3VgJ9m0L76OjTB18l3EmLyZZxEA2JKPBOjG9Dsu9XEGPoeVWW6c4kstDhk7YBnKNLFHDxAzfbuDZmZj5MoGoEeVXHH1kuIcIGITPVkMYeZPn0HrYLUqosslnBox0yOgbIObK0FvKhGLoysTYFHATArkZVR2bOlyJxBvDXSoCc2miN_7-TeR288p78d0VRH7mIdDjqWjTEg8B_KM7UgAkmWNWwZx-4ImNqdmPc-QuDO0C_UTqf9zGnGhzz4DEGKUi686WgLNMLYki0H6_2EkCejdNQur6WWCSJOKO0J8kJf4kR2DSM-qYl6OVIj0XzzVuBleg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ixp8AoYYR8puWSLuNOB0yrMyf32zmn8So-G3gOAuC_ilO1FxMrGxC94lxWaK-ml9yP7Hp0B9JLxUEy_ZMd-0l6gQXOTu2gZNmidekZGcBa94gZek1M9-ipBog88IQN-MaH2QxrjTqiQQQ0QKtyChw347mvUWdvJCBtPe6TTQnXtGiv2Zr_qUztPXr6vLFbcDZKitvfxtFNcYhTmAjCt-tklFHjomVBoidw2wixlhsC75unA30EEjOj4dPsmuOmo0fQfgDPEweiQW2mPg1tn8PXlclgtGNCzMWjW40PrL2f1rzo4FE7TAMH1ioNe9XhFdN2UQthfd1ehLs-rsSrcirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3tRcH_TPMH6U0sXqR7sV0IqQPvacbhQ9tnpU1SlRsRESTlvucDWe3KkNtCKdiLHx3DH_lNv6fBVtgjBHju3WOBKfwwVBhPmbRRF_DMNpeTpFEOh0OnB9g9ohIdgDTgkpinDOJyONgw_JwCTXmTxp1b9zjrE-Mo2FG69CEMz0XHaVObpUw5HeF0BZkCE-7MSGHKRugZAz87mcxx2JjuTaBZ-AZ6TbP5wPg8Ye-3PSnAKbVnplp9d07onuWdxo_2vr_dNcAfFR0V5UPHuGhDcWSEmQHC2e8BEuoHVqmTMfJLo-LHHDgtRwjWNQ71mRxSMlxfKFsxwYYbL5UzxAoNfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcMTZqLyimlstZFEurYmA_OwHr42i7A_OIrdzW_uWUrKCLB6Wkk44rtckDEaImes3xS_1DMpVZCPUEkwtm6jd6iLk3TSK5BjsJT67asJVE8krvJyUVuJjhTIX4mjhbUM0RYJrYDQzewCypyeZ5aKQ6ZD1ydexhgWcqTwdWTn8fJMpBCvsmAvWXn_WE72Y8j1PmOdGQdNbxKjdoSC15rSE3dBqfcV-95DU8QU9ptGcAemWMgPkduXEKhHM9u9qOC1v0mpLD9qweZC41MLw52nYnixqSdQLNj1Mvrojge26I127kJxLqvHNch3g9Y35nM9cp37KXb-l73CzzvWHHfyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rACT70Xxgnl-UiJyhunnEpy0LH6yLTwG4m3WQWaWBQCPsNyPMWyL4Es8cIs_xBe_8oeRxgwOoFvStAFjjLwwRayB5QKbwgl-fkrayLI7UK50hZJ4YIQgLC4oSVw0DtE9jg0qIgb8Oy4nO3l1amoLGHbEfEUfhRtT1ZkMar_R_PXq_RDwlPDg0JJmtkcjE87gqG88gaWfcao1iChAvEayC8vpKq4JQLPvebYw4G3jGgax5TYxjihlOOi1btfeJBz_zlM9PnwOisqZuBshF7GHIDwlmwkqkPEfhgSyAvBa8xn10gWFmRg_TSE47l4HwsyPBfWTleh5DVN_E4Jic9mHeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGGaPaG4t7cfshxZswAGM0OTk9wCJdIZUoO6ZXPKNI2e6hcSby0tcBCVRnAkXzHXu4w9x35FuzvstKOP6gUq8tu56pti8OEfKTacw76WGAQI-NfjQ7zeF8GNYcCvk7y_YxBa3j4nerUe_2Vv5IyknE7XRtfW8hhhIctLFs0uX7QAMOhqoDOspp7WsdAgnqYb1_0x5FzmzeUpXGLuSoxgY31_rfGah-jwTdqFGh_O16kFCksgExLLLYbfH_fseRNRwtPdWpeN2-P7oh5oasSrtVxVfFIvSyHmupXPFm5rNWdFs3L4RGf9bSbbhLDvxPUVoVvwJzGOZeWa2X-cpCF6_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjhYzaS9Wgzmiwa1IuHk_2d7yu8xe1bv3tI8AXn_rCftsF5_4TAwg9aJaquJoWWsSyXGrMGoOtPf53OZXV42axOaKSdqUQi8CxL0CqN-IsyN8HHup7vzG5gZmMEnbhTvf15Xj1SU6T7hy4YrTXDOVubcTJoMSBYIAkJkn_2soCTtCrK1HHKrjJ-Tok-v6N_5gJzghbXoSvHI1FwGnPXYxFa2px6NPx5p3p4YlPimXJXO257PmJRtzPF5cIkAL0-RlkfTlntfs6KZQO9Gvti5K6cqOnvku1TKoGllqUPwC7t5qIdogp0ISDf5W8GpLy_0KyP1yhJcRV-bVl4D9IgVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGo-tsYzmlGW4B5JWPp1CML4YhgbvSrH-9jakCVui24g-xieSS6rk6y5zpEl3Tqee-hRwWmO6RBz0sOm9DmM4C4QuAKrz6LMU0AnECWSkBWM_CoBPM9WVWV9c_JpLzW8dBPO9MFqz2KTaFEaHCmXQCyfXgOSzf62rxv6Zji-ynRcruRoPtwxW6Zz1puaX3YYB4F7MDVYtaBlVYIR6HgTrYlwK2hkDKCCtIS0gLlb2gksMmrg6_LHbAWYSt9ZSBXysrIBl8TfC3CMIWr1DejOdOLaoXJp-6lOUOS0w-iVQzFnGGVk-KakNMl84_A48lzQ2NCFQfSHo0uMpdQNEG-6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AW-mGVobhfhFgb56T32SaQOBM4dOCpigetuwEXkw1D3PzMukeW-KqR0rvZTA8rPrxr01ML4F8kk3gDVu0OCb-2FGc8m4hhwRX0Mn1NARFwD5pL0wZXe0Ovy3M9LNwWvR2h8xjGTIAFKkKcXm3oxrrDcxherEZGoN3YmsWXweKVWX6Kan-Xc--R5fDZ53ezlosDmSbpkjIfhOGWPQfpri2EYyjz-jKhFcEtoLTC-cm3DulDOnvMD43Vw-BgVHgrYvrwHFmVviuhbmZXP1oznABzc7ZBSILYKxn3f1_J3-gCaaabBztJ_Jl7es5SelZNxb6oV8NE64SWaj0M6h5nTa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlcaRQKZ1ZVcRanZgP4h9-iLf18DTprnuxjiFpT56HqrpFqga_E4asa2dEtexcdz2INGh7eY5DVyIUlInO_KUBZBNf1tDeEPi2GpdVvR_ygGl1AYvj1LPKAg-Wp802BDH3MQixVRJNiv5diF1u-AJSLbbzCMZWj1Jmeu4IxS39w9MHLaLnxKX6zZnNoD5KBAzqNls9zPOri_mqosqoWxM4ksD1i0qHPJpcNAlNgthXDS7FjU3fQ7Usbh9o1Qtyf5iIqYuAGMUrm8vtUd6nxCg3cjhh8L1FJKtqXpumX8ZWpsT8cX9IAzinAEu78Rm2rH-TOl8g3aNT4AOpfhcn0q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfAIoA5t04-Yxb1ZmH7MAvwgQ-rYDW354y0qNKIVoFq8rRplbzlmuavV641BtOyHUPCeDN-74Gw8pM4-8LLl7U5ohw89Qqy-YG_cOCJVFJ-VG4LZ8vXSbE5xxdt2UzwCPabvA3MZxv5q5DEy6-oaLz3lr9tbCWvVDXR7HJ9_9TJjHXsXwL-Ug3h4wDY0S82wRRl7BdpKGsSrrb3xe6FVpT5Zs-Jd8FXvInygH62Sn0taqGSovz3SrH54FiBVZmYWgvlSEspGhjaXTwuWZsfTYBD9rTPEogWtF0TPd1YegwE_yri2yQaVrX41yE_eqPyzJCfLLpUVCG7s4nQDxgxrZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu-qGvyQY1dC-Jn7mkX3I4KJagahD_gcH94mWfVKCRoLLFEbHZlag46rgXyc2B34EJpEefUXiMl9gOTEC412oJKyDSFzYypqHLX4-6ICAQR-ASNeZ5HIUDInYIKKCQJj1cIcH6LV0llnT2jZVZhcRJgRzSMwbfh651DoI5kdjOaonQfo1oFQGBUNFz_vcKsNkNtafBhmwKXZxS-MOBXb4ximukHbuFHS_nuBCaRTQfMF1kF2Jpgdy3FU2MSwHH6lKJRXjVPqbg8apbyivzIzYaGrIv_2nnVTFx9IF8LEMDJ5uTHNk2byTFCY720aF09UsAw98HOMQ6vvYA_uASQX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spzv0s7RrKy6im8RemeLgB772lD_gVThtlmiFoTRmur98O1e0qGXzsDlLotzhnruBOJV3S8ZxkFXvqHZHslWHe4kkxuGu220KNP49eLSm9eo9qU8G_vzmZF2DoGy08Nrpubs2N_aeOXf4FuyolV8znJmWdlAEg1LlqE8uo8j6C817u1q2XQnERRmg-RfY0tNuxV2nuSQU6GqUsaCPjRJFe0VdZLPPTs-Z6soqlK2bOC32u-a1k5cppRrfhaSmJeek_ncYT4tTnoy_LzIIwCsfXDiPjtv6thPihuczO687x8xEYJaWJWq7nwha78Nonq7HDHN5VtVDAYtmNjlelYeuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6QI7E9RuJ3xta_VsHFGh4d97DRhrkp0Xi5aGkHAlfuYvx1vtm7RoeqyCQYXlbqSHU28_uTdM4UYQ9YCSmB4oo59xEf0-9SS78R35NXvPEt5QD0ovKR_4413lucWbIiJ54nEAcJP7xL38-w-7X0Wjn8Xo0o7izpBdkKZOV-hwmZSsiNIVIuhNryhAkdcd4oJIvgTcV8tWLeRfpRYZyAOMMxqB10gvfVO1egmka5IgrlB3FQ9wx_u4hUDCKrPwXRwL0tBdp3n-dGGD1Of71iX8Q6Gzm8ht7FJGYXwcqZexl6y3mc6UXHuwY09_rMUrcD-Mnrtsb0WaUVmrnDLqWlZcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esNjmxQKDvIasgVwuRYUSLNtGU4aVLbGiAmN5Q_6ebJmYJ_RtES5lTUUab1KjLvlta-9C057BSN5Ej9DFBltMEr28rkklBjcKtlw7F-Fv7awREzSDwdSlhdUnSAuSvfn0ARZ8ivYo-4x7c-do1Ahs2-trF5VOPzkUAxKumzmSbC_Nsb0NKulQ55RhIy_Odu-O3trUWE3crqdZUNtuwNIa8DlbyaFw_Wj4tnnB0VUSCbo-zHiUvu8Fxxzkx9kNf9jNvPktTzyKlfxBePdbT1TP7hUnL0ceF0AEogRcT7yUbO2yzf-95ALkv-dOud98fS_h9YLzkD7jV2tMYfldstF2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Txkx8ADkzgm_OwvU-ERF8FhKptdWz8nngTmddkpBA1qZ1qG-_fvVhQtUr7bvciNuv2M_VTw2NDtis-oRYbs9XJYexxBRjkt-e84J-iR_Ai0AU7iTpZBNjYZZx2dkTKx9jLIV-faKn2qOcc1UUe6HU1UK-Z9_1WUiTVe6fq-_bt9SSHza3_cSDvS4modiGP5CM1Wiyi_SXxv6eoHmOIjzJdkWq1i5FwZquQY_44zqNWTc4Rj88BRM0LTLS5RduodKIVFyxuLo3Uo3nUyugTcvFaenXzWo1dwZtrMZkzi0tw-DcI3zjK6-stlJynHRkZ2-C8TpdOY2lnZhklm281xUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZ-YsfOh-kZCe_DpdYRsEMv6LEzkOHFUxTFD_KdKEu2Sz6wFTCTka2DxECXR0tCnPJAlvWuhU2DJ5suMA0Z4y7PfnTyWU2y56enXSwav56-YODZ4BAXpxNzfCrqZFDNN34rZwUtNSGzOz1V31uCt8EDOnW0Fh-dCi1j1uM9RizWw0NO-xhWFQm-ge_9jFszEoKKXR1PoeeXpDDMkB05DCcTLcm1u5oQEBgXqFHNEEnCyGP3dUbTidawQHLNlAxcbC2WvWnK2rJJ22xmuQs32YmOOhw5VwynLDihISdMRzTmdkWV2TuZ2MWEdaoZQ729FALmNyiK_f75fIKxwLscMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rj30XOIMT9VlvNeYZv5J5UFpWnkz_6o6jFlYyg9dDPKuclf0CUlQczLX7C6KR0RfKOMxqc8Z0hIx-qsd29WAr7-rTbV5KYxMVb-0YPgyw2iO0_rBiNp9GN9B311RKW-Kvmc00UuTSpv0nTv4G4hzpIr6ufq4ksdZjZZ-shFzQmMCuHjsnci90wLE909tIf6ZW0g4QEOkRlE_mk_LTU7ryCpbaFOpS71Vvu5YkmsjPS7zgyrD-ilYDMxTQrJlOJ7Up0K3IybVvAngVW4tIbk8o6iLCVskTVTVL1ca6qsda1HF32GjKwnt0TOVzsinQq-JS2tGHFK_DNc0Znv2MguObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GiuI0h57GkD7b3u7VAyePTBsyEnBDD4PLsB3gZ6bApxZBojjkPilCZ5vhe3MRGQm7qz6wgvxcyQa2Rk2_C0FVs1R3Sw9fsqGs-PvRph95KROQ83l8wqYXn6ToDgXoTOJYlyeBxjQwmn4qAO7iKOIlAdrl0VJKkdxSrlV9vxWz-g9MOh8Z5QZuB76drLisXwyfASTLNOx9c-2h0zeP5_H4b8EWYSCs3sk3Cy8RY0uy065eLE5XYtkp91U_cpWGrvnDtzzBaRPtQy0LS3prVaBXWB2j5rnYhhVg38doqno6P9B9-kpQGU0ciyw8eEabT08C8iTJZ58H-eRAwx5gJkYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAHKFi-I6mIbL8_oWveNTDdhukCcpeN5NaUrC165Ch2SHK0S5EUElodQ5FWVEzO5ACRxGFTANNg6POrpgCX2mj-mPJIDjKDyfGYLdLXZpnT1SVXM-t5rb3e864B9M6y_o3IphtODKrlyfwya22dBezOJl9d9o9zHkKHmr2YYSNE-sVd01YhCqdpmW7jQjmxgPNSsAsuQT2Ma0icJbNUfpoFdwoJ7xBNh4cgiG5d6xZ7w7eRh4lFO43d_QHGeqw7GRXYmW5wsLZpeIFLDsutilCwchH38q5XJM1TImWgDuC5qe2EUFadYUHa0wqXlKRcm_F3aQtMcglxM7PJ5yQkg1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovUGEe0I0QW4Nt8FIGBHe3mU4ZGSlwc6U19WV5wCupcEZ38rucpeLtTEr7h0mk-yjvhsgPjv2YXijuwBBOvkq7fpgjxbgVXEM9cCW2scrWNhQlM6IId5-ySOTyxz_Ng14lQehZ9AmKr3XBbi9PTvURfXqVvZTKr59G9l9fTOS2g0a8WykVSRLCLi3jtqL2nmUfrbbRWfC3DC4xnlQIr0tEMAdMPD4mMa66N5csXPxevtRhC7dGCGlOuVclS15etV0cmIW5q4vn8gnoits_UhnW8otouVzJImmLqKpY6VORetR7Zag5HQZgo92AjX1e7ggj-GQRQipQokUiIPz4trHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om-Td4FZb4I0pR8c_4M-rmXHXA9MiATXoRyZtjShQqxOJaJEGbJDvY9A5SpGX6QwZK4jV4qJ-6bL3epNc3RwhxTMRu313YOUc_xkkSsKtYkcy1iWTj5pn9mjxDosJ8kf05lECqBpX80cb6-qo1gp1udMcHtuZYsAD0Ls9-JZpyvnMNM3hbM00_UY9bmwYlR2UMdTAXpqPM1-qDOIFChdZpGQywSvZAxEnSL1XdDAVJpbNbNrlwGPWh8k834MkaVEwxSYobSf1OpR3ztuhk1rHHUbKlE3d4jXY50Bl8roCTUVPRqIQd7peBVCaGp_h6tQA-5M47r4d2tFmjerXdjLhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTbBArd9wUKn2axFr-4rV0roRkK122pNhGPk8FlabkAJCfW149etLomcWcHf3JWq_TXcASvQoMulbnL3C28IhVzURdhIjkB6rOGIbV_sC1Z36T1dMUByg7X7j0FJfpuJHt5r-EEtdUIwnzK8Lu0nzD-lfO9hth6k_STrmRwc1pNw7e0I5rTBf0VgNS3OfvnF8Q2AZI4b07YiDzmvUj5DWBRK1pAoDHHL1sZ98bGAr3d1wooyOQ-7dnNFdzIYTgczb3YStXwGpiTnqth-qpnRGnR7tE5770uZUW8_Nr1k1uPMDLlaieDmw3eBy8l1tOAWz36tw7oDlvswingftceLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgoT08XdiepAdCtkgqeeRbERQeEKqo-m3ykFKkzpuSc8N_FQ1xRYPu6WIWgWeckOHwNgaUWbkOMgIQv6As0fHnIhHJjUnwQF0MgsprXVbT-3y95108XyF9k4_Bf5XypOg4cN2clICIZgc796_pH3vRvE2u_pfPczz3VKgljvo3Ne2yByGvgtabx5PcJWGSYsYo_qdD35W23lE9XCG0rKyOdOtm4dc_5SFWEtSDWRxt0vTXsRPJuYuaYnEpsk08BYa5J780CYSVXiYR-9T7MpFG0VCxqnpnOrceYl84E_OakbcviaV_FKzCGZTAZZDOCA5iE7-d9KiUyRM5liBJo7oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9cKdDcfPPYUZHGUKXeCFj2MefpHlKq94hyXFV05xntyOlbR1AJEVEWvZY2Jf4bMMrWH2_HzJtaSSQ1e5Auv6I-ClbCZpC1On4TKENBfHIyuaRy55slk9kb685HqMuoJzu2k5L6sRJKDPEN4wDpwqUtbGymKj-UoYY7d1nv39kHgAQ8qdTaUWJTuMm7U7Ojrf-lF53QtpqMtUBLYgv7sk4tuNB4YleDHf5y4BEYanFSa6p_CRhwtfdVGC5UMhOa_LEAqzWVkgoXx_83tAlzFyJDIg6ecW8mkyY7KWzd1luYqo-ItWiuHBrFJ8wbXvgQTyWvdy8fM9-l_mvsMqcDUXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N92D0xGNt6a2ooi0tjqKD8YhnZdryRNCFLchgHWiVpyC0K5E4OOyQSTXn7cwuoMYGBpZ6iwGx45lkjMTpM2hDDSK96L7rP0zva_DrfYeiJXT9VbHB_sPmjPmOQnUDu8qt7_jFNJeDmk_ZFCb4vE3wshQm4WktNNGFMRHJas_S9yThArF7lThdV_lEtpZog_lEe13PnFThqaCCk98ZFLpWCVYGicrpxU_w8GTQ5IBFlXItsCUBgjpvCi8GYCWfcdAnwo5EfX4tBwPhU7O_EL4s42LDDGkeuFBuF34mjpY0n6aNpJ7DlyORQK-45GOVCJbpx_i0nMlygdW_JsxV56n8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=N92D0xGNt6a2ooi0tjqKD8YhnZdryRNCFLchgHWiVpyC0K5E4OOyQSTXn7cwuoMYGBpZ6iwGx45lkjMTpM2hDDSK96L7rP0zva_DrfYeiJXT9VbHB_sPmjPmOQnUDu8qt7_jFNJeDmk_ZFCb4vE3wshQm4WktNNGFMRHJas_S9yThArF7lThdV_lEtpZog_lEe13PnFThqaCCk98ZFLpWCVYGicrpxU_w8GTQ5IBFlXItsCUBgjpvCi8GYCWfcdAnwo5EfX4tBwPhU7O_EL4s42LDDGkeuFBuF34mjpY0n6aNpJ7DlyORQK-45GOVCJbpx_i0nMlygdW_JsxV56n8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3M4Xkfivxi6GzOHfwMyooTBLcel0Y4jhUaenRdTaTHhQhpxW9OKPM0Vy05LBKuYoQgyWcH5EiFtsHjhKT8810zsAm-RTiZxTLODjJE7S5dTcX6_M1QNMssCkFJ97t4_vgXCSOjL1BbzCJg7KKRSYgrKI6DPhrKLMwJIVeukh2ZenHKhQryc18yJJLcUpQXpAzHC2kgAEPdIbwgaLqcohvCu3psa6yd6lpxXdkphynZjKHexr7P-147UPKPWwfaABAiwyBsyhr4urKjJBj5kSnfyIgDlUtdAOyn17Qr9lMNosa_lMXq2wLPuC6QHoWagIDjx5JjmM-JLAtY96XZmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
