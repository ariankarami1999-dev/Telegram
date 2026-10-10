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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 392 · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjIFBr24L2kplmJLijQbKjYeGj6NWvnoEC9QguSL5yMjue_5YAdx5fEFI2eqqhZKOwjiHWOk3HAN1UAFXAnGZ_b5-T0Vn0DIOdxYAEh8yCYrLL2SXoP-a1jUAQeNDXcH1FfAmprTApWdEVLWdBl0763b5FmqYFQjppCym5qiLMqJQetD7WBs_w4jHEY9e1R6IEzUGpgBw_V_VUIiY31G0V_9Qfgrlhn_oo8P3R7GXkc8oqnR3KI5R4Qc5PRJg4pBrpCljEAI03ulzQqtuKRKAuDc3MJf3tXsyBlAFJvVz51MXyjp2QWzBlDoJRm00dvtvlazGWLp20qlU8Leh-XL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6zKcIty2SlkaSq4dkosYQjLb_OyXVsLOtCUnIVTFjQqMzznJ0LYEphEvg3zKz09IqNV7kz8_jTWfNrh42sdGpJOkmpTaSUlDABElPT7S4sChvWCYQ-FHyEurtVrSp_ojF2ivxzWUMBJbOPxL-waCoqlofH529LB8zF7Oo2fcfX6Gs7CAvPxYRSTQ3fwtSu4HUqYastesQ4l3JujeVDypIGrBIR2-dds0mUIYY_U1eFR-X_lj52OiiKSl3ShJAW5whdLhgFYM3l_Z_PQIZ-Jls-0nS-KwW9z1BLQdLBUQvbQxMDCVlOc49tviKPopygS3wAO6wlyb9Fybml6HGpS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwjius1NvGV4WdNtNwl2LtTEQtJxzjt6WUdm5OWSLlpyYzI5NNEyp-HcIJ63KbAqcQpIPhr4H_Fmhf-zcSup7U2PQCazmDcXtduOcMeRxcGpMx-ptXLNy1vysCu2c9KbWJZ0DvIfkK0t6FBiu3VrdE1v9gf0IrW929ciptHBPTgieDKiSQvHvRT7butBSLsoXbYGqGrTdvS2gu05hQ-DFs-_IqKCOd660vYSW_-vXBVdT1IE3zB_WqVDQvCRx6O-WMwo9fFTx3DOIBOUs1emhPuhgK7tWLTbCR74fwTIBIXFlh-nJ-AjMLrMvDrQLuA1w3gTT7BTKsmxJ9C5_Caf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inHMD0VAJI-qcSRO3DWI8HLbKNoc3KJmemdmnbkUKgjpxB1FV0-J22WfMkJoyOCez26qjnPXjBaoKKfYor5WkDq7GKuOGffo5KCKCQ7pfJa_6jLOG6sZgDfdwBHUyQJy0NDEku_eYCxIEe695HQhnOskUMHRqkICt4MGLFHi9OnySn1g88lQeZWg73BE-ouysMTpb4BUrCYjmSsQUqNap5SCcJUPWTCr6_0cuPdvc59Ies7-6g9hjThnLnxQFizGI8t49JWlXt58ahv0oYB1J5-TGFluAZZ37CzdGNiQyBIm9YZviUiwbLmPxFGMm4GpTR6qcu7IWHztYlaR0BBgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kk3J8ChTKacDMjai8-qavCYG49AndCSAXEuti8F26VLKz24DEBNt_QqjF3PkayvW1w00E5BKYdThE8Qe0S35EhuNZFRv6F0H41NtfuX8O8gYSnompMjFmaujdt2JUFL-Kl9I_ZJiETYNzT7mgi8Jm7F1Ktaei7pJcPgk-oVPk9j72WOjx-9cOTqyMQCmzAdSANCi6xNpYZSEKgqnw_WyXRQPYU-D7YqD2s2Z00YVeLPt4EIFkxJ7-EF15YnxfyeIdvQMjMK094KN1QDpoSvcIn53nDg1ssZv-taYbf8gROil9cYhvmaAlbbK0d8Evs33UP9yV8gRRDBzwU2h7Gmd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHIaYxf5w64Nt7JuDr8Tj678XBAcjg7LBQqLnju13GdtS7m2PDhmLtJre2WSGNcoIt_YR8NNFR64Gcm7R8WbwYfMLDNMnXC-UDMBoDHUaS-WSXuxTwHr_t3g1P_W9qjI2uPxM5AtV1uWCza3Zki7Y2PSpWsjgI_gsTESf_XSlten16OZ3YoPRfgkMaWS5MxPEkmU9hYi9uxVDZiDYjWzkMwdRzaQi9tFoq2eNBjP6Hbf_7rEN6a7SSlVlp58YrM0MS2_BfREbtS_XFMp0t8hFslC_60Sd_RfkPLf2W5y8AAYFPa3gxOwVD6eJVvEqBG3uMyKoQ_GWPnWgLW1Lq6dHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=friZ9jkmSRRLslXdFbjLnbdim4wpCOC8TmWaVHTckp9aLr5IfHCxnvbhGbv7dZqS-5N2F2XbZvWd-D2gkn_zekTv11GTWV6ZF3p6GG4YQL6SrSCRuXtADUhWOrO8sqmta31AHarde_2m0nGnA47_-wsUux9vyKQuu_1n_ni_zhfY2Xvg5h4Z73m2JCHEEA3GWxkq6oOhUuRF-3GK0I588cUsBFs2yOJb5Wac8GY1QXdOLznNaU2JPERP6nTD6GBnVYSBdbGQtcofWhUisbqK5vmMY5P-aoxRzrZda8TdqS-08HnPW_5062JTNMbZFiTOp1_hF86iqLRcJ8A8Uv0_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=friZ9jkmSRRLslXdFbjLnbdim4wpCOC8TmWaVHTckp9aLr5IfHCxnvbhGbv7dZqS-5N2F2XbZvWd-D2gkn_zekTv11GTWV6ZF3p6GG4YQL6SrSCRuXtADUhWOrO8sqmta31AHarde_2m0nGnA47_-wsUux9vyKQuu_1n_ni_zhfY2Xvg5h4Z73m2JCHEEA3GWxkq6oOhUuRF-3GK0I588cUsBFs2yOJb5Wac8GY1QXdOLznNaU2JPERP6nTD6GBnVYSBdbGQtcofWhUisbqK5vmMY5P-aoxRzrZda8TdqS-08HnPW_5062JTNMbZFiTOp1_hF86iqLRcJ8A8Uv0_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm32IyPkvVTXoBzoePTfhcbn08ycOp_t_XbEq7zScX4OGYqX5i5xH0zkGDgNs9MaLR54obINRB2pWxs2LOVlQ-aOFSjFWIav6wObCgKdUwybJs2fV02sDhpA9pUGVd1SusqWPd1Qrtvi0BVqRzhBoHtpN_MRmviXAAC-x62UeppSAdh9vr7gOGhlULMBc2m1lKCbZda1qqmDpNkhz21KWah-tYKa5cpbsjQC3e9aSFyeLBJpqGef3v7uEdmMWsv5r2XOAeJF41Oon_1y3S2bhlcK0bRMYboEwQupNG1UCSaNk_sHieURE3aqzznjMPwzl87EywyZtZR1WPUQDuvtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7oeZWD3YbW-35rKHkWtZAy7V1J_0egxCLLUVDQaqq-GLxjdrYD-_qRzZTH24oiTZ3CM0nvTU27fYhHKhMpylG1NdJDQ2uodpDMxcYjgw-CyARh5BaGwZynlzsZry_EpouLLazAPertZzOYAcy5c06Ib4Q-jwWDAL-8jUqD-Qys0eQ6mwoZ72s_ZFFGPIwEZIynf2NBmwVGANZK-7674q7nHbltvs0CXzLocyRe4m3j6IPOK9-W-znSBpuJq9-Lc5JEMYCxiOMpRjg61VzuzvKHwGKnvjZMPVgGCrxTzg_qVdrnuJRs5kegfuHap7SyjJweF0LPU-fUiO2dCguF2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTNgMwA3dF4jOfwWhAVU_6wNh79Lrnx0yABnxWk6lh1LC8kzzy5W-ZozUt3_lxXKJ5_G2lZSXQsGg7bDEGPWXkQk0BqFfdtgJOvTIN9BnAdNVf7oKjN9bG_PA15zTaG0CIf_aVnncFj4Xoc2eKOoOgNaXAmfizXdu1cz1F_2sKYJSJpsWES8fDZR59YHZp-J_ypCozBhpuARIT5n53WkO3RzF0gJHkfO8MfmINwLK-Ll8Xz2Me9l03-pXgU9dAiBjy-eBNe7FZpK6od59PsgtLHPonq7vaHOphZhNy4n24hqfTtCU_TgnProGBNU7-R9UfgPV2tdtDSfiX1usKKrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYZ3Nvsg5PEcCr6xeiKAPlrL7DMtM4bShoTPNfRC5737R8HBsLDaNVoAQLRjpYZb6IVJD8c3kx0W0-J2J2XdYJdj5B3yqxyZ2NPaadViQVz75EKSCAxs4ptBQiq2Jv1zpLPtk79-oFY7JKmVWi7zCbtpouAzxVgYhffguYXqxYh4_n55d5NqqnnVb_i8nOoRL_NXhTlxx3FQESadtfzEJ6PwF88NmW07TrizBhjR4tZAv5UrCUJKltsc_5DahOR2gskEN2L3E4iY6nJoW2jpcjw7eq9DXS5P9XE66n7FMhBjY_gEVGfK_M1UVxNoNDwFu4OkgfiiJWI89KGvdnXs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0Txk-l8xSnDbaFAkiciNwhwaS67LeZAMPNEcvd5skjEvT8NEAtvnhegy8fC7Eau0-myQeCvIJjS1gXa-wJ2NLt__echg3TxM_xRujpzZASvxXNIybMiR2mxqbQL_N_kPOlHRQTD_hoa68ZytW0i-iA7z8D3Hyt65d77yOR3S26k92Vuy_FD3L-2fHbgeCyymzXpUQl3AsY1LDn7MeMAtnAsMyBGDnX-DKkNS14LTFYbFBUWcsMgeFXfMQnEg3a9ZM91ZvRBGArepaN03aG-HJ3S89WeRBPaxwxyxbROQjsmAavoO6rk9BRYdBLAgBAdTx9DPtV2q8xahWQY6gbTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSXYEKBlkMHxjX6mBGOTWYxBBmu5h4zDknMc73U6I950luxqXWprdW9bMxkFHqqLN6mfZkIHjo2ZM6RR9kcP-OGM9uNYZVXoXD8CS9cb4wjRepvjYUEl2pglWRaRlaip6Swi70Z35kG04h7N0B9Y0PM9sN8k4tGGBchjsPDD6tUV7ZyoV2gNPRyovpcQuU5rer_YLpQs9xtPSvAMeeNSUTGXT8nf6r-SBQy9PGZHsbILwEstrdH4i52qL3hgoOxodyrZUvqITqxJNDxnJNoGrvwvWjUYxo27uG-fsvd5ziq7q7xCHYm5iKwWPMl2bwdOy6p7IOaWrJtJqbESF1xmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMP6lvIGpwUDvkt1ih7r58ihXI3SAY7HHK1Jb8fS945RYteMUqfROfUtA2IsCMEff3Rkjk-W6qg_sgSEMD4ZJaUnb3LlIjQRbBbEVG2_l3LFhrFUDSdbVlQlhB4xeEyjmfmEanM3QABlgTaumZQID9V8puvS1UHe0kMpQfURvzyscAvkqTa1vci71M4GnkCoS35wbFaxAJPg9AmkDElPlxMmbtxZvWX3eGMzPG6vi7CkEzrXfgbiwHpQV3Gm9891DdTwzUrwc7ZnysCsmRgxksr1Wd2D4RNtvmuTqT8aj8tmFkZ1Qy5p7-VidSWGLiTN4qSh9A8NJ-E2T3wcNE2WAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFwhHStf-S9lXEqAT4fVr4VHYAiiWzqU6jTcGG9ctB7TURFatfF-2jjxxpxWSWM5GL_hFWxNvsgIqStATBm23EVsokGIJsS4Uc1vLYHKvX-OlhT8VrE4BPtDOyE20O6gOi_r0s4cQ2tZKWJxFCravCAnVEz32j2Ep7fq2qzGAWtyvpZ1Z1A2c2BMxbdtdfLJPfT59guURoAfcyQKuNrVwdsEy3m-f-H7V4ZhC28YluaJ9lC-eoey6OLBnKe7VM2OHZ35cot9XU5JlW2JY2LN44PKFy5cMWHPEMDGe9PWNloJ_la-b2H0ZxYoR4wRpomC9Dbdwz3upFKSQzPFI1o4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhMQNwRArGUqsuZSOG5GC8TdgzZZxAZ5dLp25XIbCRU-J71cNPgoHDz_5vDs89FFw2jazO-Rhnvw4iBq5vbLE9g14sjXdhg43brkW2pdrSv13GibBicAuTturHME-LGUQLltyejSsfONEXwi1NADLfW--PuaXHphoCyibgZFGI1p02gqvBL2JtkmCn2A5wbx6nkeLy_pTt1oEOZZijVC8jiosugjrgNBa2EBQuVVGEFCwZd3gRn-CxKhlU0P0l6cz2coBHPPjqNnhvVGwzvAYSiFXegwg6gtA7yMEXWUKW3auR7Y1BQEI_0MLynrOQAjeZVtBKJ_qG_Bjk2fgxgy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHinxd6GJaLZD9LdMaWKMM5jIksL3akIoqM4v4kGnXRyjGBx94FRwuACEegfo-7twUHJVdqyot55Gegq3NYeL1M9y6lVmnCiaA28BMY2-tOy1f7LvzeK-aWptwAWVnHcnITWmZH_WVYTLd5tCbzr4bK-qP8dtAJylUCEclwuNm7VrtPNtast_VuufmlkgQA9GK8GEAbbX_REt2bwAOYdsG2Ruv-hneC8qgQHVZb9937mFoaZAETq-8VPUzI-d8m5vLtLRM_KiYOx88xKRwcwCsQoMq-yGdfzSU7hc0J79RqqP_Usphy8QHEFjuMZmHdfeAfBNAhCGJjpcFw-KyviRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngOQIN_qYss_B-OYEJMgW-K8GpDb4MO96HItmbp9B0TOKhK3o7sn_-gU98qD71P7NfmpZnc7A0gN4qZZg2gdibOU8yN-bV49rhA8AuyTYA6UgOP-WnAc2OSkq8jK8GmwqM9Eep-ym6nlscQFLTQMVONoRsUxvHCCucEZW30TeO3abR6awgFtTm-Ws32a3pst8izTLs3j6axw55SIRIRR1Q47g1YKhqTNrtLCGNEcKReTwRYJOkX7nLKIihD2pgFrOUeU8N3lM5_tvLaOuCUanH2CRT_5kztiH4980436mY0IVKY8MnHrpN8sk2bXwwJFwzLFTYiTABs7suZ2rO429Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np3zI1pAR_DihiedN-NbFXe-GhKiMFggNqyCPjq3LxidIi_SCVSeDmhML0-IZbJ46tQtuTmrHnFYvbkasIAJRCWUe1d4T3-h1HV3o6U5HqU503oaxC8Z4ZicjZYVKXyQOlCn4qH2075raHwvEwisn-YRyiIxr4vBzK34Crts35HvKUOJcD_BZB3RO5PkRqtd2HU-GOe3a_jWpvBwenfChhk_b7-ooekCSC5t_oTkkHWmdVWUMdZDIIQtBt-RgHdqUOLM3Z17E8RU4q5M1uYnOiYln9JYr0wLveHcc-SRhFDkhZC0ZOJKu_gtp0FuEZz9RYcTfkowvcaXhFdNbhB-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFaYmj0ppCBGwhFs_tZOhA3XPRYYbbePutibebHLwR3jGirfbxsUgaVrwvQg9i634Bg8yGjQRE4mWUFbxEpZzzYK0JLw3W4cxmUizeLdPB7xouf7xoNpnuPzjYfvpXwsWQDkMTsLvDSNh-wXiOaKzLAuT3PygSmreCu-9H8UFKckfW82JrYWFe3fx1gDbFmQJ0o_1QtPbqozIAY6cWyLeT4fv3kbkuT2k2wNWNyB2r3EbzzsTxYyUrFKDQNq9mq76P_9nhHOVBhGAofc-CQVwH_KwfwCRcZVo_0w6yQDwXccOs0jDjdSzDTBstN2ZsTyrk1U9HKKb9h873dDfG9GKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNLsLdc58uJzjw7k5sEtpRK9CE-Is0ctpkkXxgJyUqXjSElvCSHm45eRvqHcPsKWDyilx8AN4LjWSWouNw9ZdA5oDWq0yvrVhCkTg3RZjAdLctWq-lStPbBsifTwWEUPAE9lIdR_cpoghuIJ6UpaNtBw34zf1PXNp9fQsx_lzZ7MEBV_aYh25tiQav6jjqUwe-M9WJiZvLI8BLSguDNkZrvJR35PP0irlu8Yblrlvb212h4Y20XyHR4Hq1kGplG__UD3SKhmtPUmXG_QY0wwg5LFmM5ky5BEpI_bsaiZmnCPsx3tbJfdjBwFSLbEcHJnA29y1rLcLDV9Kh-so_lmnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=DXqNeWZCy9sLoOLXXnuaD4gjzbwh9pk7Qq2u7iG8D3CApR5KL8wEdR5swkdHz52q5EP0v1cbBMvTO5MieFwezN46wzSDUcLTgUYiiopzOZMS-N3CkWfuztho9fbDEKP7fKj4zrFlCcjNvR-uHHg4v6xTm4QFWMggcfprbs915-gliCfkB1qfjs-tPYY8JToB3eWub_LJB_kb1464M8z_1ECnNUiWbljJJZZdIk0I2N3zT-lgui6UwC2wdyjtQ6Alp-mpjYiycvigVn0Rdkgp_o1MWFpyiA_P_zU6hsYYcBYMnL5AOcmATBnrb7ZqN6He0-S_zJE62ChKyDHTUIcKbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=DXqNeWZCy9sLoOLXXnuaD4gjzbwh9pk7Qq2u7iG8D3CApR5KL8wEdR5swkdHz52q5EP0v1cbBMvTO5MieFwezN46wzSDUcLTgUYiiopzOZMS-N3CkWfuztho9fbDEKP7fKj4zrFlCcjNvR-uHHg4v6xTm4QFWMggcfprbs915-gliCfkB1qfjs-tPYY8JToB3eWub_LJB_kb1464M8z_1ECnNUiWbljJJZZdIk0I2N3zT-lgui6UwC2wdyjtQ6Alp-mpjYiycvigVn0Rdkgp_o1MWFpyiA_P_zU6hsYYcBYMnL5AOcmATBnrb7ZqN6He0-S_zJE62ChKyDHTUIcKbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6uP5rFyro9mA3SHvAup2cQw8AazJWyOC3sfFXqdQ-smqfFjdlG-ndD-xdMmHdbfi3OXYBlHzS8-OLLUv3v2nQAcEFQ5ZAnR1wtdP3UKUFc0af_fUDR9uk6V338oxDNfxPpaFejlRmjydL11-CfjyhrhuqhgjymmFKNB71glmrCHEXwz-TeG0IBpj8d0B3wcm_VmeVG3MNGCQ8SYH4WW-e_p3zSo1tRlqYRHgHeWawn1LAA8Lei4fq77eSaW9LVlBhoH2thinhoEInTrHy1UZsvxv2-ZT2iQmj2TKUg4Z8hZz-c23IBTTPM2W6kLImjm_9m_ylk1b6RkG54veanSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hb6dhxUIrCQeubqDfG944p5_T-jV07UQRewr5sayuisIVjzvcCyen-oVNim7Ty7rQ-JwUm2aTHe9fiiQqTFjAV2IXe8bS3qXgA0YOuKFMmUBu8yylRw6ziWCszFQqwyGsqpZoo0M7fE5r0I0frzSmQwA3qdjCf3u-AsCTSNzFeRISyY-e1piqfjCuV7f6tI2JK_NqEq5dG1rul1Y341seIhsFDinL2aiHY9Dgdk4v5O6LaNI7KptMg33MmJSBLJCceoLNHX802YdsVdhxr-7oCAe2RdoR4SXRMfXTENzgLHwWFuVDxdqMlcB8Wjpx0t7notXErVE4ktHyCwJ2LBh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ivb4A4ZoSg4pU4xDDC-3_410vObTrPqx4-0y8JhJXuIb5T-_htuygd3-LvKgktcVazLYDzrO7ihDB_0CoAPIvWuu-uwul1tf5duq1CMVt5bGVnIndctwoY74EymBYCROnIwL_wlLBlaKZN0iozr8mfAilYdJ-lr73Ar-e0scU7JsPsxNoqoGgqq2PaqJYGv8sBzIrt_r3UZBDwQ59sAWU3aJXVaIhvaNM6-YAUKut3gXj5BqBonIo23OCZNwnnOIUFRYcuOZfsEFDPmMMMtL0mDWubCpGxj212RyXp7QlhUQ-ydmVSyWh7WtnQsexzSLmf0AHqPDODNkMwEEPVtBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgPvtLebjysfY7NIlkGm7ZYd3F2t6pk2X43dJnc0RHk5hJi0-F8c_HzqprfSZ6Q30Tw7onRCdsiQA-JieeZQkzad05k5EaNTRKBcY_JeoRs4r4x21btz-yTbACDQFDPePvpUFxloyUFswxxorWXGRT8UQyPjKwsvb3op9q2ADvI5vqrrVKw9auNZnKym6Q2mu7AhdVLsClmnwYj4-BUxOiNeEIGERz1oxE0mcs14wge19w96nt87r5svCJ324abGyTqyq9_6ye4c1ZMEOzXJb18MPEfP6c2i9PBpQmga4t2pm-A6snsE618UmNKc2uY8nIIVK1yHFzHUyW2Ch0jEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7umwAdL7puC1q_PosVty_ZBHbFE7D_gruuYjFyHlPzcZTSpkwW4F6rjIi_sscHuFLzA0-ZzLABqQDfO6q3OFJe77rlqhpbt8_OPeGN3L7x_pYup1tUzp49Qqv4dDVmGMcrPvWKC6woYP_21uR_Rz_74kH3Y5bZTKCgMAmI8YSJZZm-WOrXS28cA8T55HMAXHw8Pz1UMJzw6l9LI--zGDitI-pQsLtKlLynKPLdpzcArYKmuMBHejXEaxN-KH7Qhdwcb9zmDq2om66w7gdR0i5vUKrbBl8mU4gCwFJ2mmVow5uEmzMKj6Hdzmtz5OGPqP-ncckvuRacVhIDywBelmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXVeQymLOuclxZSm51r53R9iIk-y7uozpQjfoFcbdf6KU4B6M4X9m6U290Wvs00GHz2SVqYCHug0oSqhcKhFHNNaGTyHJ9GPHfDplMvHMfFNJ0YVX1SasImNuHN6GLMVksc4pGDU0JAvMfxNQVfHAd2PFAVVAFCDgqHSAbJprgN5zSdSc4zog_fiJjgZGt9OGbv2EZncvnrRU_TVjyG6-wRPTPgjJGb8IuCM_T_G6_IvvZpi9mwC0Z9pXKiEXZfNU1YqK1hXhfdUuYADw_yB07i0LFRK3tWAKmWWvX7sMYPrdGnHr8z_AuQrwu7WtqYiUZRST5g5qLpzRN14z7adUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C75X1hfwAqiKDM8Ey5ztO8IPBrLfA-SrmJJeLKcLFgWTlsK1LSkd0RYDloNGcoHPWm3fBp3HET_3LgdlQKAuA6IVPGT_GrtA7Kzpar54EYrBhaVH7dCOLxiMaowLCqmZJnmh8ioHLL4rq6TTNmUOE1fdI5hsezYzTYo-ChZWe27USh4QDP67VR8RTpsMD_HUdrMowrs71vjcOuqkfj5FXlDI29aFdb4YQSSSkofCK5-1E3qRSzIGcExVs0fUt_9aBnxfF2lVaQ24oa8D8QdmH5ptPuP2F6olwagAT99t3wtA_3-ALG298ec6SXZ0riicL-xDfbek9uZZELpuoxwEUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hxBKguVKGDBxT20XlVjvYSQ_f0YT1qCwNKbYy0WytZy4N6KqGGwE6roFgBUp5lAvb1Iwh75Cufy837TFOJPW6D-NXHuV2fD_iQx1Xnm6z7TDbjx4eiGUvbolzruv2AyAkcWkiY8SnBXJqEMZnzWTpbVYwzxScKhi0oWDc7g4fJ_fKbe5jTM0AokcEluEHjTj6_4ucTx-QVl-BtCrSGd-Wt7DX1QlGtUCXdrYLKiwZ7hhZSRPCi4z9ZunLMaLOyw667BGtVFbEQXVCw3Hl3hsAY33dkqCIw0DFY3VUYo4cZZgn021WoeAJYvkWQRNp5xH0JfQPsYMq-O2Rb9hde6-UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8DlAZxVXcpTPXJDXAstz2A9fFb7rBbmzxvaRtz_q2Taya4-O3ebQ1_hUHp1SbgONGus5Io7FxLnZjXMJ0oDw7T8FaM8AaAYsQszlSFhdsdLIKr6VKeQjdeFejaYDfqJLridcIQNIl0HzbbD8qgAWP--pEmDWJ-OZScW7booVrc7nQhzwX1iKqDfIvT6uRFE1HYkWhpA09mE-D3cBeKZ6eVKPAMAH7FOoibWlIi4T57Zq01_5sJIBj_670wA7wEVj4EqmP-9-WmW5h73Ly9WuZrWrI02yX-cGzxysJ-Ky2T_p4ji7tb8dlBnIGQWmlVKcSPYHIOgp2CTh-9ilCRlSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yscueq0mFEyctd28KTfCTaCU6uWWAtpwU31tAy6ZFQEi2m0jY6z94Oyf9pA3rfgIYaJ1_ICPv0wR1-IyR_zePcyM_0Bzuju2OAx_yLWBgnGpuIePAqukkd7Gc-DRhF1umVYsdjeiK5yQDOewUvN2OK4Eyi-oa1GQpxgPyl3zSp-4fMAr8SqpELFLk4pn22_sv1Vfvog7ZVjVjh19vMJj-sNiHr7oALKUH4sjc0BrPn519_E-qqz_eC7qfvBABJbpFwHNRfmE413u3HsHw9gKmCqz0x-fX-2V8-nzdVjPbQqZjkD-dH69TA-f4uDzhdBhf1i6WwNvW4P9hNKecGgTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwunIxe8J0H4y2_4U_3-AEoNALWxFJK6ofHTJSASGFHLOZVTL0rUazMg-NGsMbTEJsU2IL0Vywpf021fJvrhYaFa2eMN_yVbmCyi5PSgxhulWWLTTjbTFdwMrAEA1iybX5kcJyXDoRZD41AIZqntD17TIbTmAGe1htudPy1FJZp3f26Uvm0-Wb0jCwExT1KB_3zsoqrDXLxppqSW8rVeD-bAqhIcNbzTljYzu6xf8UtHDG1yYNkgFWiv4c5OCLebhMr8eV9_0kf6IFeE9FfwaqWQ6pIxAe30QgaamwChMPaNdF5LqtzKrudrYiLIg4gvmvqx6_rgjBF0gJmZWtIeiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itI8SCFoOK0FvAWZh8Tjox3OiG4Do6PKtugPW3CPn5bmabc8Lj76NsVOJRWRcsMW2NuvaVSFR2cVtCo-l1CJ5TQzYhE6I9EgeO_KGNgGA6-ZfJffPE0hLjiBxsO4zKhkMu9o31bKRHqLTDwHMgmnMxxRMBHCBNuGJpYQCUTGep2SQYz9_zFFzt6oKNtuI8cgKn1AM_yK2t4rmHobkD4Xn2iTSlbkEgTivLE1cKY8Ufn04Hzon07TlPwX2Jh35ETmpVZa4JOG_yYjIr_xRTD4EoITQYlMgO3--ZPwMAfkRM2lR9qpb7xoiJmB6OX2JSUDMbVbKoQRnC9vEU3WAULrYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP9i5JPMMnWmJNhcHA8T2BomgHYN1PfJEwWqDDbGZfZHKK79Ip8cP6cp8Wlo_hVFHRjJ7IydNVo9KbUfcK0cWA0n9HR5A8w9o1zPrUXaOOId2j0o4_fmWT90lGDCxTIQkV4xqep2XZWOPxD3toQf9NIg5o8CeOotUXLnF8zOuLx8837fYBtJ0Vl5Mlz8PWLThwzUW28D_ccskV3ejuI9YUe1DTA-bRwKTxYApasu7xUGu8xuQK6ECUhqvo-KxyZtu2Ujomsu5TaiJgHmc-9AAGBQ_R5K6iFRtf1G6GghcLoXjEyPrGIvTWds6ng2ghszEvkrdf1RlvfTPc_CmukRYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m7KvBSpuzWbptJ2jwTuQp5BP51teYi41Kog2r92ynzoPDdLKDgvbVH2WnvinYOfjxvKjr5xim4HggAQ9cEDDjw5BG4okn1GrvW7LKBZ3MwU67fuEPA_ht8Jxu3wpb2Vb0XTSgO2gO0iAruZ05wtUB8tw4DbhGlnqJLXgbeaAL7QokOfZ-EmrYLRvicOQc6rEpmbDxTQYpf94QxkKRaA_3-HPLKQdPH_gCKnItJCOp9xH7fm-vvW2URRXgn8yv3IXAc774vZRyZLtddvw2gc3zV4AySJRAamL6rZdE8_S1IQNuE0vK0zh0hoa-BFRGfxG1Zr22nSAmmyAarFBh1AS4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOUVE4QM0zLgsVnyDE0TPyTo6EzNlHYyPIvXPM_0jlm_5TTLyDVePRgFavZwI3hjF0ptE4K9so_Q6J3UNE4salqdlEdbi5xGw6OTtsgHcCBNBygK-W27IiBlzZm6j8QmCeqy1a6KjJ-HmU4pUKoT290xRVBuMnTEVJolJzOXcYGpBpoNK3fV_SobrQPpEU_6p7XRxgk_5M05-gxjuGYSqSzu23wV6c08s0P3YduOr7Q3dQrtEe88Al4P0vKR-oqIXTsVzLowbXE-YTtj0bxHCOwFMlLyJFb48SQh32dF85CKOfCkAvq5ajDedV5K8imCtxtLahSbjtdPcHLYv0DSoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJLQFyAEx_kZiIxbx0wEk-ea7C-hkmKNaE_jrPR17BiaWOEXHWecW2jgcOnl-Lt4wuTOUc_26VCwbNUgVmVE3SfwasI3_LPytxwhg-ejEABzbw5ZFTY6IIWPtmjW9xOvggiGn5fQTwJJwgxwWa5DRRjo-ju8VoYp6rGxfYxT_U3G6f9FnJ_gp1ioPmxIQRdOiNNfSkf830aCX9hRMqFQn2GUxti5vOUz4_airL9Pl8m83d_cpDRVD0pTMfu2qvbF_6mBTDbdwWu8tdbNsHnh8-TLZxdUBlsubn9SeGq9upR4WDJOabhfb3DP9XY1mq_3yhbJo7k2wJA-Mef5qH7N5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJEd_L0vHPp2vmCmh_Q08cyx_kDRiioHlK7AJOYJcxf8MR-jzy_iEd735JGwtoX_ygmkQda-hjPAdOFbZDwa_sUYnn3uwQfCnC-7mZkcFKt7gptLQvJyyMAB_50J0YabDt4e7I8vfL2_sHPe2Dv6CFc1Lrh26Ap5yMV6YmxCwIPSmTatXF1-QG653SQfKy9Cp95prbdxfDzymV4mjhXadDMbgHQlIZ0UvqHKqm4RnmRCHCaLh-VKOTFOvdJeM1IBr2SkHlfQZ4OO-Op46pI6isG3k_CmVgy2Hk5nix8O-65JiNoB3q6LztQF2IhPMc3wdg8pcNVrV-HakfEoZZgd8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoWNjRn025CifAUpcy3B7M3sc0vLW9AOxVgtalZyJku2srwoyflmdgg6w4Wozm7utJkpNHSe1HyiTTY5Cyxipl4Gcf3-HP-iP1sYLCZDDTESxsv-tPzjxaWxrKlAbhLsFBITzXpE8PFTHeN2S27XgypPR0SsFoKJnXm_1BTW9HB-3CSBaelv9gMSRaW_xTzxIiHiGJs30Jrmaev1FUvWNwU4VGpnTfyJf9UPfE_aaUzwG3CT2czeeIQ9FCCih8ItPJnKflJO1NW0rpvhQvDGzWXQyXvqFkP1ytFgcg_YmAQuSezhUy-H7fMFlSHoN4x79OITY8QlTtTiBQXfwCYroA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je-7kU8U42sHgQwAsl_s_qcC612B720BwiupN1QZRxBG1efpms1WG0QlODkhBDJX_BrmfXS5N9k2uN9FNwDZWdVaC-H59pf0MYNz5A9XXm_jucAKmuSjaxNrwwpOuFoYvtTdjk4YKuKxhrjmWn7traOpIDc88I8K5C9HE7AE9XOkS7B9GLi4xzPUh8jeeQmIxA7cDbyrlBy7fpqunAqXMKJWD8QM8QmjnsKIE56lRYABh8Jiu29q4j8AFL94bRj2L_Gtj_YBAOI-mos_OnZxKGKrCz6zLVMDCsxBoNvlmoZQNlQ13fZa6Wyb46mCHCq7Sp9l0fHG2qH9HgLAUnRbLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ikQ1X1aR79CyJIL28hHPQFXeUh5-QyxbiHspey5Kt0AaPEk_FptZ7xr9OKA1mpCD7lUwwTnRSS7jkhnWoRq3d3X4yO03bkiDyE84Z9DNaVqkF3WQjkzXKGJyS1jL2xOIMrl8xA9FRdz7cKsT9lx2TEP2hg4bWeRso_yrKoOZJsVQ56-bcGKjoTdSzP_zKQXpOugL4Pw0h0vwzf9u16lmbSlA8O2h0c21s23CNdeFUelWeyNAXDPFoQ_OD2ff5Scj1ZdBiOM_H3fYvPG8ryoPTz9PECdUctjUVs7fhVGKJwBsyuRKWsZrPtB-G5nCCPMZQn5M6T9doPYfQJLjH1C5xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTZuJ79QwzDyWa4J_zZjt3TXujAjyDV_wZLe6n5cF2v-IhD8qgyhrHOO5Eu6YqI1m4I5AMw_f9GgDdFcPc5TdYeN-JVaZLwufLvl9oNDpxsHqxb5gJBuMLfP_syQ3tG3HsF0l-L0k5AAhO110ZLHaHgHlEj6sNbgAOtdHJjB9Jmkj7lUI4wlz6YtjkyDG_Ebq1gvtoYPQ3YhLK0mXb132oxZzqvQnLYRalETAoS-aQM4F9D_xlPPwRYBWKgk5IlWJF1Ll22DqvLUDtua90N5SWzfsAEounJatoDiUJvptfVd_ToZslW-fhLVLk3CRW1o8q9aw_mvv_ktzUroPndk-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLjflVhr_F8Ev3oCLEYC-ioeoQq6y8L5M2EGKqa8bcCdjVzvuLR8SPo9y8r8wEiV4POvkz2h_5Ixxm9_nFcU8PrJbYGyPQlA-rsJo70taf8xlUYfByiQcjSuQ1q_F7N82CyJwDWrP6m_12fAaXCkx9Nrjst_DfdJzcyby9Vcuxd1u00GBC4BCAVF_RWX32-zjoEHwa42UO8roeNVW70ic5z8Cu6Ae9o3pBYY5LCmr3CNjpoE2sbIgpp8HrXGNcRbmtwqD91HXCfmXjE0KWLjL4AZH9xbMGcaKB9GrbYKcCCxMWnjF9DKKJz6HhjHicrVSdNqXdaqDqh7neQA74-7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbdCRX5ASvIxRPXyKJURbOIRHuqy7L1Up8gTDcC_sNQue-SrKpPQxoVr1IGXjEHaCzbZDifpeCtdM6P0FdVqtDePErvC7XWhPvs692KoH7QlfuleEOLCnuq3EvJ3XAswhPchVQDAfEOlRzh88WePc-Dc3q9sjLhE9VnrwmcoOc5SY0e50tS7TiEB5Bb0auFWpZfitY37IB9FqGD9kX2P5S3SaTZsL9gMnDnkeBqJOL6rx5v2Lg_u0Cb4apfPRGjRL7uJuWy-5qnWunWAzE5CXNapj1TEhsM4DWNnOqm0BVvkgPVDWDa04IhzCKNxgPWm4pfB9AG_dvJS1gQe6AUJMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o37Q9BhQLwziM9g3SpEg5AXuTQb53ebK0Jygtw9JzL5kfb0Q7CHzdJoNbFN69V41wmlehCVhQw8qfGSUw-exY9ZY_YM8bpf-ENj8oRnGNI5YZXUT9B_oSotCmnrdJe6eK_2OnRvBZxmS8EZE3JWX0-18y514kiwreodHKs_aBwuZLYyJkEzmIqfRSVIJd7kzfLvFHquyGLM5Cw3lZYVSeObCw8h9f1XXb1-zVzJWvmc6fEzeVCCPOG-iaGa15Mi65j3QD_4oRCrQ1Wqdi_p5vcgjcmfTZVG3Y974LDOhTegpNTjENVB61mfXnM3up4H1IVXHpBPHPa4vBLpVQKIB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcRJNceqJtzJxc3APt1_q0TAqqBpFWi_0ChW5HBAgjg6DTi8lb4w-3k41OeU1bvxc5ZEQyzzOBBzAoRSc7TIvsce6_a2wOI54N0hDiJmeilujXn0b9BPn1NZ23MBeB8FqWyROSHDD48YVUhHhwBhWO22HvFtTloeTpdDfrVnGw-hvp62RhDBvwkwNnTyLgXQ3lcxlLUBzs8T48Ck_K_GcnxWfBcMC13XY60avR3SSPpsb6O6AVDldyD2jujde2p0TDp2VHicxsq56lkOrQS-nd3Hyeh72wBWl-hJQXbyQIuzfrutLMtHyqB5YQ4CS11XTipF2mTbTgNBrynUWvlDMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5pgkHz7K7ZuaUttKRlARo8U9LgJ7Bv0phgBba5F5hPPuJpVaDVvVvSjESSVADHpY3k9OCKAlDE_Tw3RgBLLrNySJCeCcvl3onw4hUwSVYBUTZhRhWSPWNUIm161OylfU6uYb6nBKAhQdzFwYq3t34wr-26FLSOuG1l_2PmN-rd8cQ8nac9gNt6BswUQRXpupMlV9IUY_u7tPXELYfwxf8ej53TYmuR_0Mz4srYbvYyjknwREgwSYlbb1mlZ0uojsPDwJ0wHal_TGvqImKOGOlKpsBFy7aCtkyoa_L3JEwdvRsxpuX9UUTZrLXVOgl96BZpl5ait3UD8H0nPSOusnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2atlwniddfMAL3gIpFv0vKJIlfzDzXJGqkFpgQCwUXDggV4t833bPUB4kJQGS2F1sMsZr23V2ZYwZoJYiJTIgK0uVWYxhfA1E-tua6XyCHAokoGNWMfQcGu7B3jqZzAtqAjXZS7AJ2k3qjWKtP7FbWmfoom7eZGoSkBczYvE2p1uq0RijvhRifP3Qy0i72-f6tBIhw3XFS_f2MJk3il68imxDAbhcIjEtJ1zr4ZSJ7CP-D4Vldl5s8FWA0A2OARJ2IG9knjG3UwHS8a36aF79TpLK0AtW1lNAl5z1Vqk4tOruVp7QeIc-ZtA9KgI4ctc-LlpvvqnBfGvOM1jYjs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNCl1qlAalQVe5Voh7Lqo9ttsGjGodpjfesJlHTc5eG-6K3FKJYMBPDS7vBQjoKnY7X2nt2FPDSBa0UbhjbaR3M4jA2Si3h9KEWiouKVFwrTJq8zkI95snj9Ll5zeG0ATCs2V2-8Eq_YOI-L5fRhexMusq9O9F4qoP_R7Gp8gO5yUv2KK2WHk0AmX2rHAkUjhVx6o-selzuOcBKwvsQp-iiEO7fbg2Zt83Rn01k90H1uzEwJ1bonjz2UD2E0CBlKXmGBjEks4nzezf0UZQVVri0R2jOnlvGYRbCaWqgxr2PSHjYcXuptq5CNfIToKlKYs-T88E_xu7oMJ8nlkjFtEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMoKpfb6r_PaeemBK9iMUWH04t774q3IzdKdN3oiA0xwhUlF9pR-hTbcken3pw6tsDhGgRVbQ9cmdQCX4iol2ta3tsLI7r1HWUK8_0WLoeNfRea-urooGQgT2OAA6avJ2cYI0d90U5WnNZncejIc-yi77-R5gv6lRW_aUXi7kYUnz6mhziaxSjnfE9L4fBR794yIQlQcURV9TvQJwRaZ96yErw0aHQ3cbS168zqiGgejfqLehQrXv6SyngnLveU5Xs3lgzQ6Y2agvdBpA3KRgrSi7e64hqJl3VMJ1GzZ5GBribE6O7DoWEySCYuAvU8AMv-AoUhiszkfv2szqxJIIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dthW7MwvbBPmxe3gqKUWnedO0Ea3caQHeynE4xOn6OR0vMnYH7v1BNcP9he-9CeHngDk_V967Jzpjrzb_rztkaKsD3iVpi0CJH6MCARGFzwOtS4Km8-NVXHy8Yu_lcgHpski5MFu5nhFtiLGfqf2h-4sJ9Uwga1b25p87pTroCVh684uwnPVxBitYmfddhMZNhmXo0g2UV0k1lzNqF4BZF5_cpjUZT3W6xVsE-O-e1_YR659SQy3y4PwmtRW1Z18o7fqd3lt430Ah6MVjKvuyxigkgfRB3sx8w15nOqhegCsZFxzFMQLRox8W6uDacoIk0NarEHlDSkhOVkU-kGOcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzu8q8C0KM04Z4na9-QwVsYQStbVAZ34I58EFiUWqhzvmOb7SnB80a8oL13sL9DFssgOuNgTLczfYorToK7rZ16Dk6sgwwly9GeInoBVxWaM0HTFbMzPLwqFkd9XQucoGhjFX2o-MWDwvq2DiMn0f_4QHTcvAeBLh1uEQ6ADUuUlplZEgPHfFWmPxidfbjOLZY-Ufq-e4IyrXz9etlHIHwFPPviRWu6fKDnrxMXk1iBZ5tPdxLakDM2_lqfTr7zxDgROAPs7B1tEP5MfTQN5igLY8eyr7xVGLXiE6KlpyfQR3m8z3YmcVtjf-1y2AckCCn7PYuS5M2a_EwOd9ECh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bK1Vgv6hLemtGigiIaHXeFCE9Qg4uFPr9CP3Qrh5-aStWRO9TLPx3bkhjgWfLjmKauwTVJIG0MfzAh5x3FkwwfAArhVJO6BH4u0ZWh_IbKvO_7fNuwjO522_aM7HQQhTj5kaUtbJIL4-9_EVnbhrAeFbbZ6Dd2jvHDC16C1wV5HsLjDoeucbuyibK6EuTI8mzbuvcdu-9-9zZEHqQBFRADq2-eoZBn_ME83fhmsaD-F3koNaoRlq-tpIvqqIn0sCaW5uI_JdOn64jB4PSWRkJQ8itRIUmgZKeroHw3wmKJtDR0upUzThozvfn5hMR0GJsBaBtXHK1CRJ0AiGDp3N2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJOOy8Ch-i9VP2y0ne2K95wDFXP8lhZ7EvxMLM3BUwQURd03w-DurosZl0J-bHzbVnoU9yQ6qsCSl1wACz7PRScdUAoNnakpcb32kjR-2tOtK9v9Jrtc_41ukM9xflKuaGFROzVhhBl1FmuMjPk8DNUZXqpaJqQ1PlnR3-7MZZXIsZb2SpcBMp4DqFeGTDUQDt3_qk24mklHGp16kP9Ls68lX-HsU70o3v-txTdTPblSCchufs-IweLIZKMoSkJ44GgXuiZqZMEeRAXcyci4taW9isibB8wiaq9SFTxjy6I1lTpzhGg9elma7LsZf3ACo67JnQrNPcTcGJ6mjxadsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyaZ6WhX-TOcx_JQrFX5YlpH2y7lw2SduMufaTMFHIn1_O3fMaVhsxqN1egRAdslMwcxkpQoTfgzqD9iUM7igtpNhjRCQS7h6spJxMR7wH827mRBTFhBQvyzaaUB_JtUKGmsVup2n1NFF9sB5vKwa3_01dMaSRM2ncDcydtsO6YVYJnOuCI2sD02Qz7-rCyujFEDxEgwPIw5qqnCf05M7bGNmK5qUZerODtN4hHucNwRiNVlOTCnFrn-BGJVmaElfxV74xhRVtbtgyyYrFn9i3r0-_4xT9_51JkOnwC9BSryv4bTMzsD4djpljcI86nW8pL_E-O108qHRHeN-gp_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx-HSJLFNZE_76N5RTWA79RWqPYkQorDTOHPkL3rbvCa0FCJKEhJEa_CIIC4QG9a30khb-dlH4-3YCvG0PFQYIWjX5b8a54Sp-UGImU8AhJz0twBCg-8O5r8ou0Zh6yT_6nFqC2daFoCBiTrPdxFCC9tdc-WOPm65DI-EqJr1cviNdY2_Ii0-BAT9o7C6XCeneHw8TGAphgAie6B8PnF_T-fJBZzNZoh9Quw1klH3B8PiToyB1Kw_n-tzS7inyqzfbeOUREOo8Jv6l1R0KeRPW9xK6gtCA9D9Id2s2FSLULQfLLmAubieL2hezoPynkgxyH6SD06ChQ0LKQHl85hSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABiz8Fh9qAHhMtFVgOzlthPceJTzrXw6_lL-srDGKzA0QQ7QZhKH4AMH21VQ8-PysbfaEeIWonmRHhfdbj3U02betuQ1pU7mNxUuY_tVVH6ux3qZmwgWcbF00lFb3-fhyjZrP0d7SwPl_KdZ9qyHBDLeNkozzj6Z6pyE7ynryIS6x9wLVhoaX3DlfggCTFik3oG08a5n0VP6vVvwaswXkrbtW5dXrV6eTMioTbH7OWYD8UkQ-IXL9nq7KJz_AdYthn4Ynnww2S1bqoR5ugBV41rxr42f8Q3nIOCMZwEr2QMUDbcMLSaA-ZYyiLv48jV04x2INuMT_ScdWeg2YxcN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNihYYEK-sUUyBsrP98FvSyw-CFZsFBq0h-m6efU0yUOmsSmCzXiOE-Vyod6UESprcXnIG8HU14Q5hQzQuSMtM6LrW36Ot-prH37NsVyy5DjpAJc1X4ukJF1SA-g0yX45MGA0YEM8J6qJSi_KdjwOwsNIjQJaHnawUfZdlB54rWmcoYiKq-gjUzVl1rkHOtcbLZAueG88L6hGFLMGox4FjYAEFHmcdnDS62EX2x_IeApnjPrtO8MKQatGU82jKvbyPqIEZlZig1xcn9mHhGwNkAjgstfcPDW5xjAgPTsQzpPyHed-LvV3i-Oyq4UgVQjPmyrgfNRNlSexgTSTb8m6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGhvkMP96IlgSBHmAiP0rVFrjeVYnDc3T40IesXJw4Eh_B59OU6NbGIOX2q2nD8CQK7lADSZUqW0jDssxafRkfPRMmbiLEZdCdYNCq6C3j2ECnuvlJGeYqxb3g-H2P6PplE76nEYlVqkFv5Eow7oZteWlTYqkm7Or16cNHAIKjlTTvz96yVEvk0ehAhMQlOFMCcfrBzYaTwvQyqHbdVIuC0U1nc0TxiEbZTNw3orlNxnaK_WAvjqP4ahMnoRAdYD5HG26aiXmJOUJ6eR7n_JlFgAmZ5_Kw9oiO6ElHTkLwvM6KOeXXm0FcyXh5-2hdS2PjQapZheRaijtIX79XKFng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peP4haMGAhAx775MdBCRErd9uDEFZZ96Sc0l8-pgCszjK7CUUPjc0xbS35zANE-uMBKWWtjT2O3v_XOe7ER7MehYat7fttGghx8N51Ll8D3NLOpYJqmF-VS8pYejns7C0XqEBX8zcCDri3WAnsxkX62JFmmrwvbBU-aTbXQ1YaheLftxShsXQTd9vj7BqSlXvdJ291vVXcfou1sRcOb84gWaEx9YOgVT_ip4TbJHSahar_giaUEjkW-ZdGxpPlQCBy8AHHQnaXssxMIlaxjupxStYUXGazPOP6lKv4Ped0rqerAYZnp4Vm0LoXpDuASFy-XCN1lpA0qpHljULy8b2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkWfOpx-obfFxFLqvDCa_kjsPFW8Xne6R4DuW8gpJEOcA0DAlU4P7XuSgUsZwEnHmwZAuuMubnP-jOMa15sXXntch7vVRpsMiB8HggCse1BbDma5s9GZ4FCtSz77zl7nihPEGExtwYyd4UQLOfLn_pZaE2X9RiiP_r3D4KArkGm3PpviuY5XkND_wCHR0xEtcNqE8pvOcnGdy4jn3We78a5TyTgLhHJg2-ObbZETUGILwFQ6yzzFfaiJsiY0Ac6v7UVFP0nLbx-DRZJWVc3ewWXsn05itwhYW652surLeZS4YisoxzmhU9T47cpV5fUVjp1clFP7dJvJCutK0-MN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvlkGXu92_K9dTXQV2mLIDSlsfsWFgzspgulw3EwLJCpO7BKnNqIqxYVD2Poa8t6w383q433671wb50y9uv6eOPfYkz6sGv8o_uzj1FzpC62gEVTWMOG1tupITTF8Qymn7XXz7jzwKuqWcvuddqINC7O0pyqqGC8cTNSU8eULlQL9PVw84o8opHXWk6suBL4CheyivThLVWE65sFG6kUQszTBfNhQZ9OGWorI2qzf-KZZa7k3h_0KQpfw44oFO0h73o3y9KsolHrfcZ-giWe39b57s5Vie8YqTuItXDZfuRUt7xHS1pOExwzgTr2BwFOph38bedC_bUc-EGg8jjRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIKmHQmSxEOgqbuKUYl-iW_uf_IZPMD7DHiy59_ObJBLgiI10QyEyyTQA-hOc0WHxI0W26eaU90Dd2EcZ9X7aZtm31SRp7-BsxvyCUvykUmyEIqWPUEKR90TbM1irVlas-ibifTG6d4IjaaEwEBxRNJMsKV13TYXkdrEfOmttXofu_oGxEb1F9FjZZIAH8fc3CG5Zgc4u3mvptoC2j04p7tOp0mW0hL_o4O01I6DOz3RPZdAxKjBfXJhPXL-2Kn7tLigEisgJbB6fVVGPCfrmvC97qaes_d5eDorO2E31Ai3ZxHYQsZ_-Pi9q6ZO5mdtwDIn-jZT7aIs6m83CnD4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMTQygmqE9X0fhZS9kYXuZEiLeL-Dn58lcYrC6w7Kij7QdyULM_wAcsPOEsKZwWJq1EdV_lt3nNpxa-YFg0yUogMxvfPRw8P0gKyYr_b1YWPCCkJFiFmuYT5TFMmY4P1q-UYsHHTHoLhfSWTQwWikxZaj_Edg7Clvh90sX7CxxhHD4EJh_mt8KbhN5tULp-v1LXcEq5sMUPRcRGBEMKi6IB5s9fjxtFZEFjfUQd3wog-DynsvzX_jGY3AQ7hBwCM0vAnjItLZhUs9pajVH-c_uEp7eU09Mh2NuRAWlZm3u0ui01kBEeXFp3EAouxtJ8Z7BNeNnbUxS62Bm2oow713Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLsKDNsVh_ksAQlciZDGouPqljmInV45JVuolFWFFZm5CP4-aMCUJOaJ1cuWTXV82blcZMw8zCzDE_VxnPovsvJsUBM3NQR1luqamySt9BV1a3Znm7pHk4-TQOb2qoOvG1156-z6QaXz4-vRX_EYlS-wPVdXWLdWta8hUdNNVZHxHzLubEyoRClr7hL76V5TCYqHep5eClNsLW6unE_GoJkIorygU8wZ-rKBt23WiZ3OUQMsWffbrvdw2p9f2CrBH3MNz-iLUR2YI4xD45oLmrZAY76PCqSQolnbUL_8xScAG7NlhascyG7alPe213ikDSOXB1QAMyJHQ4CHGqc_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMy8w3FednaC3ns52EZ53qBycCSD-OWVJS2EV1fwgmB2vd_hVzRLkzO6Tg-Tt8HrK4sflaa5m6DCyXgvnHrrQJ8DDKZsTF90UymCQFgEczyhPHrwfliMwpgzgVAm1wEwL3LeG8LvcvvHCazkezVtDOMwB_fmnN74Xa6lNcUPZ_wDoSm8noQfrLIUoES8oes5gOdPQQBuq7f6UmZHC37_0Sqn7ODeuGq9y0gS8xZCUgyLpngilUUCH5TMOVqV2kJNnyL-N9D7sMislfqJ3TbXO20AL7PfUzZHZ94djr8sj5RyaNtl5wicFoxZZdOYHnvhXlT3c5ZSZDNwdgJc1ecb9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYqkJtyy36WW3BLo2FIDiS1CRJEP0r5ECLavco-w48ffTj1uVBMK-B9bcO23teN-oqRqx3K63PoEPnYIGoZZadNmmFYSCzCmOwqZjNTwUC9GD5x2rhbLxk7GWSZhrxv_mUhpe54m3dd7Ded8ZXxyrszslL9_i_fpdvPdaX2E6ooMWcUKS1oBvyL5bsFBgB5Rn1PwlZvTmyeCkB4HD_MOx-nJnM4jY-pz3igshXcY3shwkaJWi6Vg3BmbwiumABWhO0Fziqb5fK74HaB1I18JjhMkHdtBGQ3HDRe9GYVtITVWDsNAUuEuOEtIpKGuHW9aZtzZoHo0s47naYTRmtQHhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcvkOKXKIUtaC4hpCurokBlBH-IIPX_8k8FGEsd9WoBJAThtBkK-HGfK6QWPlDQwSbL58Hm1DfGAX1hLJ27jUz4VPID7G_rmSBvovzK6AmFM4UiXx3TB_N9R9JJqBrzXsFaeNDOUff9_Bc-nCJX-fVQd3AtgfqTZIcrLl3iJWy8sKa7zC-7GwUI_Of_BplzGgrBBDlw_TGd-sxKeaX87EU1y1t-s8UXwJphzcUDunEAypl9XVX3nlIp5q0brnBmckFsihLX0zlqHXrxE1hn78RMae7dQYuEVN4ffvtxuKptk2OrIfSJ87qcBNNYxqFqwXRrhyJ27FafLNi6NafLJDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2EYv1alFdvRNGB9HtnO2zm_d2BzO7Y72X7bmyLP23pP-vuFC6BBKsbL6mGvjGmgYiiZC8IYU-NiFvvBhI9lb3CXHc9MexiRM_9f1qqy0eEtZtAm7QfeG_PVfdtnEUBEZRShujyeCbQGnb_Y8ZVYpJNKuFet49umTy-IGCOk2UIZrIKKfzJSCGA-32bZtc3_KCAh-Y6bOJvnnDg0nk3aAPmQcxBuY_Povvr984PJ8ruAlc6a1M37PekDDLMl-qgNy0KkB8j_vbbzMgmYIaoyV0C7_JhsGryOhUs7Ut-O_uGNsJFhbuiN7526NrQHrtSay-HhrBN2IT9kGzL-2LgBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCVxD0F2ZILmQX-D6MFvwppYAAQWESeAwe3EJH3FSFODiYg8ftsDjgOxRjpnBPV72iPG8cqbz_bQ4z6QXtRaaCWK_GWx0EvxnfI17b3uglwEwV-kFIWwtoHffIXZ3rYEc-1GYv247DWTmC8EF8ubfTktlEaScP5h-jUYZSYUPmY3DRbSYekecCyLRCcZVJnG_Hlm27XTSGXqOrnlJpYkhVjQ_uBSXvg8e-VkeFl23iKfNlBFSsfPJq3eYBR6ta7DFMT28-LQkvZD2Uh2mzZFQIgC4XUL0QiJJc0lQRbxlUp-6griLZdMoz3UMlUXABAwz2BuSx3bJzsfJo-6VYwcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVT81NaT7qVvHayXgHUWtZgZJ_VPM0W-_4qPWnaKC-jZiPfyBJqBSgaFYdDNbBpOt-1pwbI2ZbZcxbvyC3ZwlRS4pLdHn0KNYotPpAKdiM-TaCp28ImJYGFMA032NLPnWaNDmwctegwb0mNUeVvUN4AOBMFJuVrDUV1t6PaO2RvcUsIzzLuueBQ0p_GurR9RRP2uvxWEbK3t2fkeC0F-ip-Qy2WzaCaFJWiHT312YnzjKVN1wOOFpvImdSStNNhSpbY8aqOXQVcFdnHEtRbNlM2to2jBWO9gHyh_2bf3NZZB2DkU8h0Fl049f2kx6MkwIFQ4J32YGMU3Y6uH0hRb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afkmfrs4mptjL6_ojM1betjVFb_Ajna-ikn4U9ZwzLm-mjmkb5CI_OEgT0aFKPkhTzrSb4fHsNRkXZG2MLdKr0bsEMuAdHTIYYjaOLlN_-F8e0J6TTqBqQiZqTKscRsB0AKUViF_pF4PZztACJr9WLLPZ8NlmYia4v4KcrAB6thF1BXS_LrVcpa1dbM8N8_59mtLlFnqMgcZTHiXsRB4Bce9g07gcPhJaTma3oxwmvSVqBvWRK3Py29by3FmFR3p07l9watQ2EEuh_dRkAe_GkoT4PVOdu7y3jeqqB06oioew7n0aJ5Pj-XLE1ffgE2kwFIYk3iGwzH2IOBgLoQB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTbgjN9clHlh53436QYj3S9VTLp5u4XiqUCwMF7E9sm6ADDPcm9EB1hnCGvzFB43arSUDojr2ViXRo1PC5_O2B3DOhisUlPnYxgO-RDbXNnUJxTsdgaX80cMEU3sGKWnZfcMtgD14lZEjuEQO9An2qceRHd_kYlMBuqPeF4u5ATF1YKMajcKT5uI7g2CKY8QIlQGeUg6m2PsWv-ADkRXqvm1D3CgXFoEyA1Bt7FAXk9eRo3WV2RcnCFMc9dsESpzMj0xTY41cjCEFoa-RHlzC2qcpK9EjRuCgBfwHqjZ1ef8BL2N558b9Mrm-pVW4QGekMZP_wzLr-Nu_G1HzCnuSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHMqcUiuJdGvAgsGInh0IzJ-UwKIfiTEC-x_rtsUfWkmpuZDjm0v8US0zWf7AcfoTBay_B42Cv-lAx1hMryehYOSDaRUWMmt5rlIbnjGjoc0jcC1Eerv4JHC8fF-l2iG8lGZWYtPavOmkWVEpAoybXZx-sZDtZLNKYh4BcwCZbqBSVwjYRQ0GUoDeGBfBbqqOFQHUX2_OZ3uzROPHVjhrhK7TMsfKMIANhnW3I2cTYsOYhLIVmwhpV1modYtGTYFjz8wOGnUQnnEy73tMuHlIFRE9ftGsu1_kB8sBhHA2Pw3oyAWKlNrILJSTV1pMsibl9iA0qQ_8rI6ssbbMGRwgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF0CypEgCA34Jvsr0nwRrg3ndt-fUhud1Ys4T1XnJc5gUlqEMNmXrfnNOFxEwOmCsWmLsJILiM1hmP1B9Lc3hcUND7baROC5VCzFOnD_W4_9HeFIwJ5-insNXP-72gEAmaQdUBHRQqd1LLbT22ByPxhu_5-HCqqvjLqZYfF3GMK7MtynqqW8NekJOo_y9PlKm8fAk681eGuzWaLm1eCnxgo1d84BhF9GXsHKOeMaWdVERraENpEbziuZzKoDeGXNqKu9ZdvNghyMvtWH4AU6DO69uO_7a4OH3SU8Z0eIN-MJBX2rmM0B3-8Zgs2pnOArk1MlMVAhkx_e4psQYw_jmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWFmQJTIAdZYsA_HCxZmkH108zuBT1TYscP5LcfoZ8BVBjaD_k4kz5bHA0RB1nuRxDpP3ASPsUpl1KhxrQoaC2Fj3VUnao_D4Mjljs1zmZ1F-cfQ6ORg_wvj1DIKYJP4NuNnmpY41FWcxhUZuh6majwYEJtR9XqZSZZdPh3zLXr_Yhoj5lRthExiNHLanQILsjRhAqj0_D82of_9yzxSKkmsOF3uIgmLuGafeUxM0KmkHP1w7vuUA9jhWNFi7P67fFXyd--6HXkO91RZ1p8_AhvjMQxNivBVxP-u90g5RwhmZ76H2d2V8yqZaOJDRw2duVyZT8_Pk8KUVIghN62T-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlB5C1Li2RLr_hgKak_ad6os8GE8gxwRKMH9nK9swnTWBoGwVbNOuiudApntkgP-t9dLQer4f607f5sQITQFYuID4mWwMT1TNEOUgpFfy0aRj3V_mq85clkQibo4otd7V7wou1ZN9pZyxu5gtga9NAQ58RVZlbgYkWefDerHZuHlUUwV24oHnrTq3xH0TI7seUyb2C9Yab6D80y0uBDOgatxevLUvi1yALdXLxLwhnQeRnoGIFyAAQx8WZZS3vh7AcLj_HAyC0RWGSCcY1HVymPl-vb2u_Faj2-IWkVy0Xh-CrIm4Zpem2bff3kGcWZ8GIZpVSEywYUaTUZGUCi4Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sItJtC-2_BooVrxYhcSQ51Tsz-gfLkegkO7CKpY9JQpBlyziTuOSACx1BD8NW-tWWWbBlp5N5cFiDPdue9NqO1Hi5t2pHa1OwnPlAt6VzMDz4R2c7NuwVdmV0zIbdTI0W9W1DbJPyOXBNATT3EWkHzQKZS8UFEy17ZoHLK4N47iQPMOOUPLe6DoE1Qzt0zg3h6J1JzTGG5cufnzm0_6wXe310zMcB2vGhaWXuMQelsJHPby_9tfgGqKyNxp7IdihDiX-bKFsDPbrdr-ePqcrhKHIVWbgDFr4VyxDSYI8c0Dd5r42IQsNeR2egU5CVKKgOIkxHy5Hk3TPKF5S6HZM6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh0X1ihnNmZfvNZZHSCDV6Z5NtUW2mpHaDrdTWQt-0D0tdFWOVk5vI0tGyGZSZnQztZA1tSd-WxyqJ7sGc9asFFzUOCOUJaiAzaHmiCu7pM291OqmjI6p9crGGPtUNFJ2TNgnPnSKlM_PP_uStmgiTEspR62jWZRGJu75QHo1qzf1jNRacELzJliHax5RMZJCIuaWz8F7S-G0DI7YGawkWgTPWvLZBWZ8KuA9wdVcMKa0wwyctyFPp10e2CfBvCCZ3-NiZPIJLVGUOkqvTSHzrIBNCf7i62G8J_zaxOPHoridXAmaaDMIjckPBgjkCXMHgIX_acZRDVp4g5cxTlNuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=A7I0fy5BT1WuCSuusC1TY2MGROYNMepXPnAVVEba_e2SzMz34eulLeIIxsULdkMPEP3Bn2WDrjB8Ev1Gkfo9QVvBBac6t4gPWisZ6lQXEssN7k2iKGgmD81GeVeNaL4qcogEH7JUY6KkdckcxWjjDR2scw5YLamUwl-BHb7xD795Rypk2M4x8_htObpQZ17RSELHaLkDuZ4wtiwsRxXw5BNTkLN59OMJs8lyP6CcaO1sdJ3ziWqn8ilozuPo2RfBeNjs4PoifNphlXOTiahTJYZYzGbaq92V5H0R5qdqYTN8RvWUEiE6K60WyuXdsYqViqYxCkgqGhfXNQHslHZiFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=A7I0fy5BT1WuCSuusC1TY2MGROYNMepXPnAVVEba_e2SzMz34eulLeIIxsULdkMPEP3Bn2WDrjB8Ev1Gkfo9QVvBBac6t4gPWisZ6lQXEssN7k2iKGgmD81GeVeNaL4qcogEH7JUY6KkdckcxWjjDR2scw5YLamUwl-BHb7xD795Rypk2M4x8_htObpQZ17RSELHaLkDuZ4wtiwsRxXw5BNTkLN59OMJs8lyP6CcaO1sdJ3ziWqn8ilozuPo2RfBeNjs4PoifNphlXOTiahTJYZYzGbaq92V5H0R5qdqYTN8RvWUEiE6K60WyuXdsYqViqYxCkgqGhfXNQHslHZiFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faTOYDJKlXagS3kJNxq0rPXPZ12OlTkVsjsuZ6K28XhDjR6gf4qiaUkdwGDr2G2sViUbcmxnk5kAgrDF5Z61i1K1tNjQnMNSytFJnDqKj5wN2J-lLCVF4Y8x6szK-hEx_bolEE-_uiy_UFSD3SrolC_9KHasceGjN0BSH71KZK4gw-lHABh-5UZfhkhTpgg1X26STbxWqyA08Hn8ttkuzxhclA8TpKyHuuS8ZibH9lycnemQ3IJ6f7HSTaFn0_3RtUyaJbHRkiIWJH77tniPUh6xLm8BRREhBjxBDNPkE557G6SXTJ4K8Tnku73FEiJyTgzXyHVe3cMXztUZcjYeLA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtTuHCbMqYWxAYE5PZIitrDGnBVlI42jC128oVK-5jTLKMjopG-HH_CobbKeN9qeYVBeiP7vuaV-uZjgOBNpoVgPg0rtOWGp7kBOzLuzCcnxzmCG0OVq6wPxYJhwrI5wiRO6OzZCck8aWq0UyneuhT7VM03NuzR1Vuj6O-aHUAlzU5Q_UqlvYSGdgS_zsnLtUpPUNYfc4wVRMFVwxK7jqNKtO8OtY6bjZLQaoVR308ruvpDL5Zf0G5-Hnqhu76dBMDwFn7EcFVZ6-xwMJVdHIuu1DfvQZzRS_YunZWjl8s7qCfXFzeIPhoMXw9NYa027ezMZdl_jwGVCglqZv_QkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
