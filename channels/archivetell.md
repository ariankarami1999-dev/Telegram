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
<img src="https://cdn4.telesco.pe/file/Zjk8FxXvqPuidEBrEEmpee4fqR5j1MdgWUfL4iZ54SiI00FER2sJSKvyww1iH7UD_rvTqplPHn_3lvdAGOirTw6oDUpPtyAEWr-Tyu31XIXzkd-oQQUsF3_KGsfzgsNzWkyI2FUlmcoW9W3sn1SO8rdVxOuqkUN6qrSo7Hl9qTWv45c2qbKhcjToRb6LV09X9vKje49ayVniWUAgi1BBHk5DzNh5nfxt7R9wU8LoU7W7KFMMrZQo3VRH05E1URFXbV5213uq_wBQwBJctnH7vY8pRBxCJEr_kVlMEPpwTV27Z_RfkKI26cly76swLmjPJEoDJMXwAZa7X-aRLboTfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRAtUiIJv2wtrFKIzqdSKLhAaiHE2mYjxFQdzqCzzGpeCEoEiKx4aior-8IqMMqh8EvEb_kef6zzOynNchJix_Vy4FK0OfoAvAoTSKwIIQb3OG8I765XvEF3rst-j5TVIb7neO7iPh3uC-LstY__PjKyRqmrugCOUvVepiWs7iGbe3N2lAEilsRLo_uoGHmgbla41GeIoEqLf6Whaog07rhIK7210lrda6rAEeCibpWmVe6wjcA-0IvmKfkymB91ygx7aeYg7T8u9iOHcVwAIpEOqGSkv7Mtgmp3Uuj2916hIJ-VV3uM7NbzUQoa0af0bbboYVdUnumGx81-uzzpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1hQkx8XLXT1dakAohzrLsb7n2tBg9RA4iO-fI8GO_b0A1QzEzbNeNNDbn6y5N-lj-uWWC7TG85LOcn1r_z5bxK56hG1zIS1JwPQCey621JgEWB0uiGsFgZd6vWC41GD-4BnDNmKzcgyKh7zPJKoxg0ZziZIlEYIan2PUaFcqtjuqWnOGxVPycMIYrrHJytcNJt46FiPBvG_FRnrWL2nsAZVbCeqUhgLb8phgbw8pGrzjt7jIRPJuZjJQxpj9yTnNBqwjQrTrk0ZEmVQr3dVmvImrIs7yG42boDs55e_r6H02lQil6zGECyUnoheuqRLtHSvCGyTOfnAHqm51ILhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
پشت‌پردهٔ عرضهٔ عجله‌ای دستیار Muse متا
⠀
‏نیویورک‌تایمز می‌گه متا با این‌که از مشکل‌های امنیتی دستیارش خبر داشت، برای عقب نموندن از رقیب‌ها عجله‌ای منتشرش کرد.
⏳
⠀
‏• به گفتهٔ سه منبع آگاه، زاکربرگ تو جلسهٔ ماه اوت و با دیدن رشد استارتاپ ۱۴ نفرهٔ Instinct‏ دستور انتشار رو داده
‏• تو تست‌ها، Muse یه‌بار بدون اجازه رمز کاربر رو عوض کرده و یه‌بار پیامک‌های خصوصیش رو خونده بود
‏• از ۸ سپتامبر منتشر شده؛ بیش از ۶٫۶ میلیون دانلود و روزانه ۱٫۸ میلیون کاربر فعال داره، طبق آمار Sensor Tower‏ گزارش شده
‏سخنگوی متا ادعای عجله به‌خاطر فشار رقابتی رو رد کرده و می‌گه انتشار رو چند ماه برای اطمینان از امنیت عقب انداخته بودن. ولی این ماجرا یه یادآوریه: دستیار هوشمندی که به پیام‌ها و حساب‌هات دسترسی داره، اگه یه لحظه از کنترل خارج بشه می‌تونه دردسر بزرگی درست کنه.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmVr0jLW27hdlePlFJ2Gh-bmm-OJRYF8saisnZkAK7jYWslSAhMbjtpAbhJTJcwfL-x-IYF-HBKFE2iVGlEC88SonyoARJ-NMuxvEJZugxm_6lboO9TS-DqzKyfTLJuGfBEar4wxGXO3RLI1CKG93r7wbOCjHdnpy44t-7jyAw3qu4rvC8qXOn1lkTCyU1emjDW6ZmV7lJ6oWoeDiZY69nBhusFJay7YCe6ja8jaxpSt5EQg9Q4Era0mbOWGhzJfJJGZTT9dCDRT7Y9Tli8ECQUwoYAg7WLZDGmYtggQY1haIBMNYZPYP9EJq6C3EjS1sOercTMa2B6UooEuKt9X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑨𝑺</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Game (1).html</div>
  <div class="tg-doc-extra">5.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pxtvt9-PoutM80JKsGeeFcmGLTET0GX1wKBrHfpl_9finArUT-CWSPos19cqwgv-yQh4KuZq5RbQx9z5oRW_BzsF6guHh72bz9pBidr3LceWxo_PmqgIJi7hIQpCqMUI948IR3ombGGNmddKBjYjOdoD4YVAdmiMBFk8Ybfh643bgaluH6_CKWlu_hUfw6M6rMpTHBMDqlsqzM-joMLztP0ClCrgqm6xR9f3OgHCKiB0Gm5PmtrkDM692UDvJ82A9XuNyNHfOhNuB_rHRZaOa7fpOWnLZmbvmZygky6UywOrooTI9xza0zj6bxCJrYbbkSrFUvXAenaVFSHICIMq_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_cKJiZndijAyvtjb1ZIbWWWTVTLlxf1iOz7ImOEJDaJeDivh-RIqHoCOhf9ef_iVeYrAkW00begaDaYIg9Xh2Q7Lgr-Kk0luPGbbSfkqOeilolXyUzt10U3biRYgpiUs4xU0KkQ46fFT2_GiUK8oOg5JLnlgR30c2Jsrbx99VnXl0npWreQtXfSsgdfH5tQmkiq-6T3mnXfPG9TcDAV-L90_lT1mNNNcc3PB4dDE_XlJXqWpR8Okbhue5eKs9O6-P30rIqISvTRg0la30arRQswoO78_4wXpgwCloU54T5UTec1dLgc7Vk9NZFXOGTh_CnadvQWbrjs82IwxGo4_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=c3xueuF2Lk5f20r8z9jmTcuky6wlo6cRRL5-lhugJX8Mfl7BKFLnVMpcKfs2wMMBCkCrX4LVSG3IOVf9fh07OommwrvP9qcx6_V7BmW9Xre7-tWyqLdy44YQu4X_fBM_NJ52oWlrmMPLB41J38O9KmZvbmABCPbpa6LBXg1Xfv3oIEWWGRk80wKuq42C9QeodoXZCH9cdy6xblw7laIPsJqra9IEtrDC-naXieTK6dprbyoXuDxQUBvE09nERtontcahRHLYdlbXaHWqu6lXXqaWprDPa408ndBncRmzHkdfsYgVfpaDLRPWHP2Us46CC56bnVFVKoB23ctpfPuf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=c3xueuF2Lk5f20r8z9jmTcuky6wlo6cRRL5-lhugJX8Mfl7BKFLnVMpcKfs2wMMBCkCrX4LVSG3IOVf9fh07OommwrvP9qcx6_V7BmW9Xre7-tWyqLdy44YQu4X_fBM_NJ52oWlrmMPLB41J38O9KmZvbmABCPbpa6LBXg1Xfv3oIEWWGRk80wKuq42C9QeodoXZCH9cdy6xblw7laIPsJqra9IEtrDC-naXieTK6dprbyoXuDxQUBvE09nERtontcahRHLYdlbXaHWqu6lXXqaWprDPa408ndBncRmzHkdfsYgVfpaDLRPWHP2Us46CC56bnVFVKoB23ctpfPuf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/He5c1vjxmJl0B2VKUXdt6TgN9HkMbqy-nvsQIL0x7QbpEGRGx3Fm8oc4JmJVSAYUjmbu9wmce5LzDY1LAXdMWA6Oes1PzqnHPXm1Mn0DJa3dAB1jVZcLk9ni7YR-024l_9qYXjfAziIveBgnq3LPh6-1wuBdn9fS3YEmb3yvbpBlEbyZNfwyIt8qmHfTPB8LbtF5HbQYk06pPxVawpWWNQxoaLFLlmLXmu5NHvtUqWtknieH5NDAF-bH8LE3OMqGr7SDiGH8r4gwEXcODcIPwNej9rJgBa5skp13CXsMqbGxRXHXMIO2dd63pqywZLvPOWYq9KrC6D7cyF_Gm4CA7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJhjg58Fj09Y5eTDcZt6o_XBbGQW_xhdx70keOjyE82xwvxJKPpy4h0a68Zjcwg8ZqyJgt9kRMkEUy9UHDzM7Rw4J94oNoI51EF5Fd1me0sU6KyDMmfbeM-6yF4HKmo3KiXFhz7PjOKBiI0Tkyjh26K4CRljARBMAwOkeIzhvMYDM7lDzX1JGIX3KWNmh--VyE6hlLWXtmQaPr_PzcVVe9oGr5_DgojLjM_lHUdSIAsImKa2vN5hpKomUMkV6wso5vEz_Wt8YSh9AZmWixRtu46z1qx_RMoYOF9urxLw8bYiC9EBHAyBHFbUDGs-PwXZyZ3u7NYAPYdPyzV_G3-YTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6zKcIty2SlkaSq4dkosYQjLb_OyXVsLOtCUnIVTFjQqMzznJ0LYEphEvg3zKz09IqNV7kz8_jTWfNrh42sdGpJOkmpTaSUlDABElPT7S4sChvWCYQ-FHyEurtVrSp_ojF2ivxzWUMBJbOPxL-waCoqlofH529LB8zF7Oo2fcfX6Gs7CAvPxYRSTQ3fwtSu4HUqYastesQ4l3JujeVDypIGrBIR2-dds0mUIYY_U1eFR-X_lj52OiiKSl3ShJAW5whdLhgFYM3l_Z_PQIZ-Jls-0nS-KwW9z1BLQdLBUQvbQxMDCVlOc49tviKPopygS3wAO6wlyb9Fybml6HGpS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovEehB3K7FW_Rxb3fwRvwPqLvC5vrVJcQY2iV-bj_48wapvJLw-bsR2S3-wlTK5tgmLjVMXG_kSi7bGYDMnz0nKKkcmdfdx_qixn3q-V1ZvO7vAyU1FchXFK0DaaV3axnDT_jGPmPgeSlyK1Ud1nnvlGzHxeFmg9d5v4HWPGgRhqi2yNbt3aceMyF4vzYgF6gD3ACJxhuxtAqqxA7YB_fS_oZXHdRwb2hyd-O2FqJud2hKagVnc3pSKqVoWu9DYi6HlxcPMMbtIpGJtxCU0ToAceJS7zGIxb9QuZz8RySjBYx8fgc3pLdotAGSh1JSWpOSCKRplRqhfTAEGXqzXhfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDgF-N0Cd9mKv5MI4okv8b8Kefpnl8yiyvspp1U7OtvYMzxWTk1UII1AYQLc6Ck7tGfqfLDSC1wlmby4ru-Wb1AOYyRwpeBoAg5w7xbUxgVqBAp7sVGHPx0Ul3uYRgw5suc9d29Q4RzDUL7JGWEJsMBU6fcKsukOMcF2mqw7RcI0qxUinbOHDHy0x8FeCb_fMjN02aXkGvuYLz0OOecE-kVJrkwjynAAIyhYvzhuY0KQWY8oeFlL6GRqnWCRsB5p1Scap9FdB7nCZ05CVqKRJ0L9L-xh99a8S0xs4hq1AeWAZZd995ykhST_nLBMNGOsIFud9HKm7qKar5ikZyCZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eULaqRAYKTKQ7YEL-gz0hJbHN03julxqha7RrRaOCeCqztCe6tK1rDD-rJ9-SyZwYRU06ThoUZWrOe8Ymumg7Tm9lQct7-alYhDHKmD1LbncIKlF-oPPMuZwrKCutAwzD7gcm-h8faJ0IvgwFNZejlo7B-cleYoYlCQa5NNSHeqLajNm8wkostTSjcNCJkiI8DMB_zc55muSTEJhGArABLxajDOCumBfvHi3ijt6OhSwMZ7EY28VExfCPL0zjrH3lUNFLBYssnhgAe8CrTY-esuLjMO-cPyxakQh0WGQW_BiiYCAFIRy8E36MCPO5rRUTg1kiVb7JFrB5jFu-9pzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=JTcNUHNE8Xhik-zUpXeB_t4s2usGJtaA819y1tHfthEYXTLtUWx_Kc_dO8g6cIMC4P1NItso6MZlUHNG2-iFbQ_-NscL92mo7TCgB0wCeLknzKIzWjM1yAzTc2w3ak1-lhZOv0sU-jlkAdQNFkP6KBKGnAlHh2taewyylJdeStxpAl9b0z1gS2bj6vwbGx4n61ha8zrS8QlQwJ78vkPW7PQARh6IWRaybtilHFDD2ZyPbSrE4bZ90NXHOOQK77jIf8p-MPepSfUve4MpviERAmFiL0OXNUSNNq0Cx_AtDfINQYyJ09A8zgA5IWYChlOkrtr7gUokASBVFykeBcvAyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=JTcNUHNE8Xhik-zUpXeB_t4s2usGJtaA819y1tHfthEYXTLtUWx_Kc_dO8g6cIMC4P1NItso6MZlUHNG2-iFbQ_-NscL92mo7TCgB0wCeLknzKIzWjM1yAzTc2w3ak1-lhZOv0sU-jlkAdQNFkP6KBKGnAlHh2taewyylJdeStxpAl9b0z1gS2bj6vwbGx4n61ha8zrS8QlQwJ78vkPW7PQARh6IWRaybtilHFDD2ZyPbSrE4bZ90NXHOOQK77jIf8p-MPepSfUve4MpviERAmFiL0OXNUSNNq0Cx_AtDfINQYyJ09A8zgA5IWYChlOkrtr7gUokASBVFykeBcvAyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHcfrlgj7CdgXVr5FdX6uI41qjvp-XbKddYQvcu5hukWZrV5TycfZxhaVujSTBDmOu3aL9Yhl9-NWwn05hNNkDWEAlEjLBOsaQq5MGSPFD6qGHj0-j-NzrwKAds_r-E4kNeqb2YftJz9-n4XEJ-wo1mwe6Y-pg4NecVbBZhYcozibqpMB2qVXjsgP6jMClFX-DDSlNLMvIztgPEroL22Kk0JEN6ObjLuisi2nyN7MQSmYdcWtrP_MaTvGQVUkBHzjln0pV_aBmY3uQ26chECDPy3wsCi8Zud_KHqxj2-WFxS-8TPIgEcjixuH9sNGLyGrB6iRttvTaewDSI1AUPDJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndXgB8LWjwpSrVDjjJA38n21h3UtBL29vRh4i4Pp8d8MVxkB2W0PA241iQAgXZ47WxtysmjCrk1Pyh6szEXx0tyI21PGAzNchg2yI9x_mDbLWrtUG5zEGT1VkP5Vj8ZhX5eavZ4U2Frs2t0v3Og5zquxhq2P4ophpWMtHBcSK_yfV_7v7GI7Ws0rbKdIvkpmtPm6wp20Nloz5q_N57Htgfp267avHvXDs7YyOz1eHuRJKL1YxXtSYutMSB1w7rlUl84GcdswKZMRRYufnKYPWGe5vxQfZtnmqF506_6v49pEzpAtCbmWEs_eCMVhTc6NnJWW5ACase5URC6iFUpAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8fWHVHiILhs-H1IaReoLe9WreniN2lnvXkA5wrXgFnny0RDPs7LDneBcRN_UD2X3RpnRqR1HulwwPy5D_f-NuFHhHl-0xEXijBX5Ol1E8o9-nu85tOKsMfDyBFR9c6pe3MviF-Fgwtk_OSmsXNHE2_j2zptjPkh8FswsrcF3Vr9hGSaXQf7AX0BK-bCbcX_hYv0MA0KFVP1mGCTYpGbpZBMInQDpkG4oaD4ZVgLmZ-Vjq33ZhkgJ8PPotbVf_37ZTFgFbsERSxHomzTZogG4EnPAszscOBlxx7e1r42grNhNBOMdfv6_7oI6Qut3UagUm9jAfqtqpfhnT-Hm_gfrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=CyisvQjPJ3cy7srVfv5irESZh0EwB7Oz5dEQt767_Z4P_jrMuVug0DCdNqV7y_lQS4Bo_cTOoN0vVWHmvrasp6LmNMstk4yJTZGECWZYKb5zV9TqMtpMd9ZHZI6_9ihOAOkGF5BzQcyhe2WBI1jDfEe14Bs7q4lUScIfZ9_So6WqmlTVHlO2P1v6C6OCuwNZ9HYRdfTG8DxggNm32_iILOf6eRtTd4LV9bCgHFmrjm4HVrANcLElAaXGh9_kQsijJ1NOFWt2bbFxWD3MSgSPglh0AjOW5BsgZTQkDzZS2KzcU0O1B8ZfkeFjcAB4Lqufhh7uXALbrMsBZv1vVVD3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=CyisvQjPJ3cy7srVfv5irESZh0EwB7Oz5dEQt767_Z4P_jrMuVug0DCdNqV7y_lQS4Bo_cTOoN0vVWHmvrasp6LmNMstk4yJTZGECWZYKb5zV9TqMtpMd9ZHZI6_9ihOAOkGF5BzQcyhe2WBI1jDfEe14Bs7q4lUScIfZ9_So6WqmlTVHlO2P1v6C6OCuwNZ9HYRdfTG8DxggNm32_iILOf6eRtTd4LV9bCgHFmrjm4HVrANcLElAaXGh9_kQsijJ1NOFWt2bbFxWD3MSgSPglh0AjOW5BsgZTQkDzZS2KzcU0O1B8ZfkeFjcAB4Lqufhh7uXALbrMsBZv1vVVD3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBd9qTDwYkTjTOhWMxaHnZ74wLs8nP1e4HSj9YUL3rswGorQsQMe9J5RZkti5XdhlZV4uEIyDx1r3Y7ZcIkR8DC5QXctxUXgNSOnvyqyXK_p1HyE38myngCUoyIg4zJazQK-vRhiFY5cQXtAkVvQPX5VJtUu23e2MEmV9IdXlPQUkj2Ahe1e5rpEl118WggHiQdJF7GkXsa_5_Qiml-48ldpuXl3gH14FBMPIqntHUgYz8mhZJwie7yrRNpEX7ZSWkaT8vU2qtExGkiRW8_xDvyhxbiwbDZySQ1YXKDAZnkNredZI9m7tQBJJqqSoenSL27aY8i168H0NP5Q1z2CPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzpc-FHw0B75TcpC-netkv01KXqlcUAUw5-MTL4IaJYuN9MiQhV_YvekcySMXf64FwtPvk9LQxPXKSHCo4nSRhjnaEftvXZWpiYyaL0Ly1Wc7SHsIdPPxlZepTsK1BaqvqH6mrNoIytfhGwUvYKKdyfIDCHBKEUIZ3lQV2WrPF6TKlKObbUa471biJCaJpT7hujdAeOU3cWm8dIpxlir0BlmMtojbmU16UQg_QAwlCfCrDV7ztmgemAepydk5r5Su6cQshSj9GIYZMpeb5QRPdwmxaUVYdC9fRP0etYf9C8D-_E99cM-XTKTHeET7oSTdbnjC_hHE9g-acjPU4CiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZxkssaLC6IIHfuCkEYhEWKzMYnTGGMjJAWD3Pcu1GSnSoZYTqhZjU1ePVPAINTdWttp1W0Lp0AiKhHa4MQy83FHNisGwh9KXJ0qDeakRe76myPccqDkh84eD3ObXS7Ilr1NGRl64EwWK8Rg39SJkt9iN4D5MJftYl3tvsRKtNAo_GAz-f60-wDXGdjVl8zTw6akpgym8fkeyLkgDIdhoLoTqLmXNWSy-XoZMI6LyWbywXWhxqIx96oB5oxZa5kQvuaWxwovSl8yW0ahvlzaCYSz2LeB6jQvgcU0zyekPp5XyTQRw5_AidTClttgydcRx7Cv2q57LG4DAapdReoL8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ama6dQrsp-cNXLIVXu2CNzSnuwyyBYOIZftIcoi7_LZZiJoKzmNSZlGuG3QN2YJjYZKA2JWQhngICpizpY1jGdlY0bdx8YmhvGtdrDw8YhS2osHM2FsT1MDHailH4kSy5lksTh6oR6QzW2VHVhiaAwxO0z8oKacmuHxtKptN0-YQKTfAgId1FYSO3QUwHPkZtDgwfGg3DQb5wiEzVxTALHZCqPqkhNVAoIk2_lcMC44r7smIyqYO9Kh84RTeHaOKyK8E4WXKoGcVrO7qDDaXBiG91P5K8DHiYKPwFoQujQeVC-BXhAck3XF1FKDtMYhlvup8j60FpGggynxRlnl4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKEYnsEcZH9lxyUz3jBggSRc4EK6abKKkzmDtZ02JPIsbkBBIjeRFfFmk5O03pIxZ2QqVWuIhRXOiP3i9POn6YLSfawP5kW2Bg_5ofC1jioj_oTsus6DfzX5dNpKajfvUDm3jcQjpOlSvqc1Tr5zZo9y3qCZFp6pCwFfvh-HLc4PbbEDL8F2WUeK0Rs0YE3_aJ02ewqY34Y6YXbD3RPnpuardu0xlo7qf8Qx4uR_qfBaw_NRUZOM_DblZziipwSWXSZWxqnUz8XLG1SsBUC3pxYEUme22kqdibdxi5lvFzDzpibAqVMeGmyiq0MEQmEJSCwMOY6hoQJKFoFVXewL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAazkEy1bQ5D_x_4zREto_SzVZ1LQupIn4d6V6_KNU7RxpHPMJZ2wJW_PuNL_71_V7M_LvfQ_E8pgngOStbWDMhDv1bxR3gfW98sG2jBjE0HYdTfjVe0iRdkJhrxvBYwm_atHArL2Kgd5FKjQCJcMtNc1poURVsZou_0cyaVKO9KjRbAn4V_Dy59ljAT9q7LlEffIvQAqNUVz6Rd-ZyhA1r1UgRkV_6UgXA05KBEzfprPAzAOSRRExlQmIScbJxfi1sRIBASEFAglqZ9k1vVSigsygfsIhvRzmYevcwMvxFsRKU0iHHZ8SBhdXr_njGgWO7Mc2J5fqubQsHr1lNmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xa66mx9rDl_9sm1evJZnqbeUkggIafPSiMFPXvGu30g_AbDSRuE75HCASaaKrXb_QSFe1qZ2u7JBBkrS9moRBXIWRFnbA6eXNf_ybQ9zK3iAnpj232bap-lQ1uabGnucVFEtF8i9_YRRlJCkC4BHH6F7Vq8HW4kUciPptRASkW3yZpEfhK-kz8i9J1mNa47t75oT0sY8EI9I7s50q81-6UKmlbI6Xn8-2ebezvzs-Hwsz7hPq15ybRQeKLcgx51AHE1VEVv37QXP8oWxFloj_6P0VyfcWnZXXSYW4kRO0I-uePjdx5ysE7ePMga8-qDVkp32a5ef-252eT-MJ4oAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMISS6cHCzrFnJvsm_8gPj5ytvPqAfpDXgO0KyWlIP8IvSmPQlcjDW_ahfkjM7Sl4pmP9Kq-OgLN5od0bckYzq3yg8Zlj7z9vzWsjWDFmsk03_zk1lHipfoohFiFY8BqKzju62Yv5Sw9VDUr7M7980-zCYvMSQlZ9SJmqKrwr1D2Q0g2esMzKYSS5bItMhEXzIdwdHzCZxCIWfJFRIztYhgpyeTGeRl6lLfVXVWw5fvQ-QKAKQx2yO-m5jc3A1kLyElO3oEyj5EM7QQtL2f_gZ7ZUakyak6FJfWZFsls1Z0G_q6RbC8DxwKRLBr39Y9Ag4p35_NvzVxCEfyybCvZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1VjEHPSD1s9rI-QuLiOmpQPgvgewrfPp9zLqckD3FaJ_Gc8ggXOg7g5B4Z9LXTt6VUENtpMwZtlUkVI47wNUzy3xVsPbZwzlkigHp2V1qx4G7SkCtgx1CiFGcMYOOw1bt6xRT4BRwOoQx4Ye4DP_tM3cXV4dbkLwo9BcN5LdAmS5sQK0ygTGOo_E5UAb7eWZnNwfyTsXmSv0wZlOjGAW8_W8Gk8vLh7P6fYF8RUFDC93iHqiAxpGbRw79bwf2W_Gdek1MGi-ZAj5VBH9_kRq-jWNV5A465Rqjt2ZvB9urYXzld2CfnZKNF6zpVYHFX04kxd33Yr_tbVN6IQkoxncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgDhZNIQJGJNYFMAckyb0Ya077xMOxUqPaZIwMp77d2fS61U5yBPWYAFd__zery4m1g_JfY073vEUBi6RDnuasOd1GQOoJTPd5n5-HRsqT1pkssprmH_xVRE57UMFIzFNEIUKtng-l9JaAd2uunrBzHF_Dpj_OdPdxSvUwf46TF47oBGh_AmbRCd4YTsMVhtduIgoGAmscHw1X3tps4uREPVeK-A_Ujf5rbsd2lM0mDCN0gvN4qonBcODLq4_F-H-G48JGi2Bv1azOXlL-1zaqiv-WqHcetk4OFbYF5czGQ5Y4_hQaRgRACtgIh_X9rUucM82G9iLS7as8Az134gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3_9MAFaDSQMzGSqhQ_G2MoHz-FVQJCt6QIrVyJ3Od9rP_3RbvN7Eqe6BjwiNpEqjr9Hqe7U8pUHkow34Kllf-VKj2P6-_R0m92iBCGZp8AMSXvu3zapOyLUtk-uit_r-tmt4sCd7MO9TrV04-Y-hU-HjnBaK1PTPR_iH_DxN3kdIjZTicSnFf0pk6VhlC0ZMUOtddX4F040CuI66RBkPxD5sYX_On-7q7xwn74RYbMUUFI3y_m8UFkZ5fRDm9vRrGmhE1UfH-CXg_2oesSlJX6YtWgZrTaSgfg2z4ndUc7pGp1xiatmIwFFOF9__n_mjKpk939iWd5pAP-2ycZxsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUA5K8IUPpIXxpQ9HZqrsxH2lUI1eZLqTd1urRFqe_cr1AiSl500piX8vy6geUd-Y_sCfLkoqvJZMUqv1o5iQDVDrR7Dxck_pK5FkdewVfYt5bP1bGrmou0pFEPSFMP1F3CXOm9onzPeUtRaSGSRdAd1WemXxULsXt4UHCCyoV5ymTPprtWnpQtDPIB_CeTVmfHdEeItKeiQpDREVtZvhpOSJqnRvUYZZfqUubU98MH8Yll-9NTy4orm6SJ6SiFNXCaKxiSS0Q0KoIu-O7t8j3gQHkQOvYY5UKc7rYd8PT4bDeaRZ4nu18YDQqN4l1-gXyHUquELRkq6CUGB1ka2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEA3V57zY_IIt2M_LWISp3Y7lxbvk5gHfHBzfgiq1llHHzm8hFq3N-AFKJJ1JW4K0eJV0MGwDhqecTJNSoDUCv-7Kz6zWE_y7u2nCAdMk_ciLr0y0Wr8RPGqhjFOV0I2jkD5FeXZz8y-3kNCA2EQ-5iEu4o1snWR3opJeotWasYphIK9dcc_JVQYR8RqFYFkWDj0_nDevNMv_e6vJcwHF46PW2A8_3l1CtXptq49ebvFY6SbitlnHjq7U40F44VHRtRvz_n89LTZsDNz4zeLusv_mj9GihwtdgUQwB41Ja4CX0O8R90qNYrNUShLrZ1C1mWb8_E3u8FGiSMzSfa3Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvQ_oWy6a2AOTTmVgvM3l8ytPojSC6sQAmzMktWkTpCZHkInyM1F_epvQZ2pEF6vuD165Emox8RBUQBwXEqAh-FylIf_XgfSWiCv8IwSE_yQ-hBTCMuwcjkq_n5FClGJWL53ClkdkgEpJAYIDEzDMIcQ0KiHQCcPmeMitXGFtBUkHEzEAI9Y39pGom7dTBItv2_yvAV_M0ST6wIc8YS2VTE3FLM6LRYDIPsDjyd4K-re1U2LDD5awGPikpk4vc739S4exqtXBDxicB9SghQTn8bCnIAUxa-AK2ITXvJ-Sk0_3hlSj7klHreYRBmrGcYG4HWK_0CbG95G7V_Sv_QdZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fiiU-2gAN8uPG3unbRIBy10P0lheLwfTwRgmomVt-1J_9PyYAXPBmaV4OlE9HEy9meGkSvDa144qYAfxegEGNKOAT_q2WrNVPTq66kdLXG20LLwwjt7Pp3xTlIE38ks4KAOo1uo6GFXZMB5eBka559Xd4kneeLuEqFs0O4m68ffcp2cY1mpW5lhG-7GmY3VnVZih9UYp4xEsdSHlDCVDZXk2M3fH8qrGl6rJWKDgky8b15MOUtEC3EUp5RDp50zdFiQpe0VUXe58sH6bYKreh1wgo9fmXmndwRsO9XjbJz9QMtPRwh2sdkJoUmlLoT3kUKMnHzFAw1NhUT03nLFr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=fiiU-2gAN8uPG3unbRIBy10P0lheLwfTwRgmomVt-1J_9PyYAXPBmaV4OlE9HEy9meGkSvDa144qYAfxegEGNKOAT_q2WrNVPTq66kdLXG20LLwwjt7Pp3xTlIE38ks4KAOo1uo6GFXZMB5eBka559Xd4kneeLuEqFs0O4m68ffcp2cY1mpW5lhG-7GmY3VnVZih9UYp4xEsdSHlDCVDZXk2M3fH8qrGl6rJWKDgky8b15MOUtEC3EUp5RDp50zdFiQpe0VUXe58sH6bYKreh1wgo9fmXmndwRsO9XjbJz9QMtPRwh2sdkJoUmlLoT3kUKMnHzFAw1NhUT03nLFr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqk2WqyZf03ekaAxOisSuNTK7rlD9CzuZuGUg6BmPL7eBF5kVseIXRX08vl2ekBh_C_wg47ddXdp8dnMRuEYh3evj8ro8QGFcxpRnvFRD3qpp1GsPfUQR0_LWs2cSb06kFD1Rbndz9KNw6LGqX5glKjTrOd8X_EoO4iUMOZsFLfzukt40V9ch4eUJsYrjaCbCQ6Iy07vpNdrSoRJ9m4DeO9Mcfm4eYoreNJe9XphmkoqzlPtA6OpeJfXLOeTplR04IHJLsmaFj9B2ujl2xtcX2prv4MlJo_iNT4J5GvZ6iPU4Yg9n9ljhv41-CGGrhzDehDf22HdjOMzB36iuzns5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_eCA_wvShfYxC3JqfuYveYXSAMUqRFJj5mWFlkrPVbDliDSHEIGaq5h94nhmQGOHtMEORnrQ0023ggoE9hyp67VA0vXlOfX1pJCepqSvGvkt9fvPxYI7sFpd6E01XgTs26qPU5RqFh3W6A8MS2EyFwxCWxJkeaJRjiw7C21eTUm0GU7GPPUvCKF8PNadFPfdeorllIt0DBa3-xBW7Ixn8eFNCEFyqPqDdPvD_jYuWNO1WhXaK7FIn82aT9lkfsKs7KzmYgt9PBDXTfUeo1dmYcd9a0twf2WXxu0Q9sb5x4X3K_qCi5O0qJreZ5J40nh8T06BzbXhD9A66UB8rjCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT5DiKf4rntVcdxCpsNRxpmlf1CwISN5NAzP9FoI7t8csVt3mMuV8kxeYsCTjrY79PTQHXGpQSCMBJ49T6IN8CPGLSExP7Of2pwi1a4xqrSiyoo8yS1SJFPLtqA7X1nCHzd3BtmZ4z_l1NkHq4geU09C88Fb4Y1xcvL52hCZiMRuCE33xlAYxNfh8ot0UTsHIfCTeqgXfP2HWm-JF_V73lqe46Z6X7NR2lZ0_xYYowrg5nNPXWVUo79UfZlACvynyVG_wvqcU691LpdmFNwoSz4Y2uzAbgrhNS2UcivjqB4FqEqCLIKzgcMtuScVE6jgqVNj39Z5VNC4_UavpeRIuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA1whBEvZ3ndJBGIahfYz_EdB9l5rjJNEVFSEbaNnL2K7RWEPNzjOjXY0IexUFBtuAybSc34FKJ5P8HPVt3aMvhU0Ayba_2r37UBmYdB-7mb-noK8jXgxwMgd7yHBqZulQXOvdLvqXgRqk6fnLLZ3PQHspKyz4I_DHbsouiOmD8nFnb0V872RzGlFcN7Ak2pqWb8NzcwOQFtaCcRCJ6nEonDRbmZhcqOmI0HGXEk79kFGE6YtdTQMtgTYtCuprqJXaGDbXEp6dYLe1Uf-17Pm561WbFWtkp-zFtT-6kGvZKiG45OoPPTIpAjh68KUgjPTbPkwYy9xo0jQjLMVjFaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEv8ePg2CikswkKFxCBvliUzUVYB-oMncCLSdmAMkoDx2UY74B46sUPQYEl-1hHBy5OH7OdmYCN1q_JoL5N4q9Qv9780N2c6ryhyM3LVBozhJxguCYUQGac5f37KUzyBfNduVFe7s8NXuHUd2ByOaxJdqpPD46qaV6kjI-sbGGFuwwOy8lalqFYG8VjjuV4h7SOWsFoZZ6cl0uehIg6XXmQdFBsUJOwsAJVzCnX-CbxBzUJq6LBS6mwqw2SBB9yrhoEu4HjSGji__6-ViDEAUD-FkQNg2Wcc77tP9uV0oHAzWPNuvGbdVGLtaYirIwlUrAFETRKIYsjyK2BQQ3fdAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-UpZ0GqVne64jMnfql8YaGyJUxH_Vt-P6keI6JdcEu4R-FoxCNwMbpbAvqlIMjNacKZDaNDpiG_hpbnOfWOZ-JzMMjBH3PFk7Sml1KLoXtGXyo7pMUchO0nU3FBRK9dm8hxCrpOvf5jdocrR5jpKO8be5OFmdZFCwlnqYlM6i5vhLlO36ZddIsshwxyB3JwbV8sFn7jMT_abjXYOBwhgS14Mga2eO0gabOE4aDhb11JzyU2SMrmpXGgQmTUxPxxTQTMkpLCdgTrkdyEnsZZefyh6PvHutQUZHM8F0Xu77l6Ckxo-J-iwP_p0Rum1LNOEGgqDHpunIV8ji-7Bu5-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFK49qt6_1kBVBrNPf_6SrqjWbSzBjE_s0rDI0paunY6FO1GqnMopUv7_XPgz1Vqc0YDp0jRlbbVHrpERVYl7oBrl20mSp8aMFt5h_o3Qe2FpTAyb34aUAOkKjzkhe2QBSAbubzmHLN127S9mFZTxQs0tzf1OAol2TWhUt5-Md-nrLT2PSvC6YjNCIc3bAUfAQFRVeYQMXxd6fOw0b8c4wE2B5l8PfYGFZj_pxDGNH2-6_Th_hh-BxtyvblJHpjJ0QtK8tKwFCP-FeBBcY_ltysiO_baNX3NRIUc8p0M1K8gZZKOTxCQfg5FlwXGSpY9HgXNGgBgnUz-MatN63Zxfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SOmtN3LxTGtOj-g0kcv7kcv4AwWMNx3Z5cUwCT43M7hoF_uo1GRmwFkav7dXsywrtJ3szkEV6k1tgdKc0RZtyFLzZRR69Dl1LpqDOgb3fuItOeWdIdCCFOF8ZnZd3wbZ8Qh5_11Qiykv3_l4-5w1IJOeWNrsDd_xVrOcrxN7zIWCQnWp5dymrQ9jGVUMffy_wm3HTlBMxz8Vqmcs5pxibo6wyACLZVyRX9b7HnhzauY8QO6yMFHkLXmNPpSdyZIbWFNPMMuJdpkWSVCo5Y9pc3QJZhYVj0sxT-L4znKqRmCy5VnjXz8bK8RGljCL71igcm56IgM_vVziWnZflSdMjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5nNSRAUiWFd3uAhw6Jp5tOnRNWs9lAIOxUTMS1Ef3q2Fe4tui7rrOLyjFXntg2mVyMGrgV2k_vaqYwNDsWZIKUFDG3OjZwMvmQXhcqZX1yk6YPhBhD1S_494U2fyuB3AlbjQ4BoY-I0x5D7xqvUZpXyG_LAypSw1tUYC6OfHhxSwERVc8QYOaDM49fRkMyxdcR3vRbPz9jcpcNRxKvwDJLWiQeIO0TtrVCIbIWK9lPLgQjzWKt9mn7Gikon_9CEkDGtLKFuwApnRq82I8AQSF_PouUW8T0ir1P2llKsFOBRrtSZDoncjXrly26VqnpCwEcorM58fc1qOrHusGsvCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckk_q3olfk74JoEYVv_K-03I-CtcLMYi13lFKbASX5_IPCe-Vut97aAc6jNV0AMrbe0LjhPd-NaVj75ZcYVzxOaxJioBwoqzxWGqm3pTlDs9qIJxsCED9bTcARmVjxh9Nsc7JsFP40M5EJbl_DMkseH0H65cxsRVghS9jCmDR6tVj7MSmmRFnScRE_oaQ8rhrFHL7pP026H1Zw24LEPLLcO-yC4SvZfsZzSZWR6HQ3rHgPAqtPqXpHJTRcoM1G00_7IH-bSAupf0fnvYBrEDrxoH4tagOyi7fN8O2ENfSQ76MCHwkHgWCXn6xmhOfNBqXmZCRvSbhgjy-TmvgyCERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFnJ_HLU3xfaH9LBN9UdoH0s-OCSgYhtCTR_4xnqFyX7KJPlCRfV52X2tFZPRcPwogwLTlmzYrIW_HMcJFv1E9zyG6zZ0go6GVrhDGRAKjwDA-tZqtihFLZ5VhfQa6U7QhYAZFwsXiLc289aG9yQwQBDFhFuIrCwz-sKTkd4C3C-QoumD_5Q88FGojQ0L8fMlg-fPyPRRqA3w4bE7R-MOdA0qqzyWLe4VheiMgKlQmElARPGgrocqY19PfwjSUbV5sIa3-Moh1EBD_UKcRMYO3g9h1rskbvc5-GsJ2mOxK53YQqtpk7dp8j0dcN_F49Q500juuz8iPIJyXBSMn_ZgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTxJbb83nsQe-YVXd02UQMopyeprIIlYXhDMDfAUTCtghqw7f_mC8RHoNY_X7P0PbWQONKalrHOc0n3-vjcwrSNtVCqUW3P4lJnfHGM6NgaCYPNEw111W95kPTykqF3lPbGnvUPFVfwrSgEOAWvdhAcKvXKeIBGueEQR-TuoZzNH67-r_q1p3YJxGUrIWbkdtZ7duFVUY26UXBYPxmK1iVfpD6ozXJp6mGj0tUI6WbSc20fzxOLlKiMIyAtJmUHVmit8SRhuZ0dEz9_mPlKUPExwxmvnwUxYFyT9MR9iMpywKMcEOVZBvD7xDRPfU9z3DOb8IklWapjFn4-IW6Emw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfwgnhmzcYJT8bmQ7dow07Nh4lVO4912QZV1u_wetykQYtyt75-rxz1hHOnDhrnwmaJID5y3aK1O-RnkOfk2P8pOwSthAEevObMKOQq9e9F9sPLUc0lMAiJIXwcb2ff40FWUAv8SD7z_0PTyiY3etjLqdiDWZU161S6cW8ZagWZC54-VbBa3C3tTnOzUQUL9SJ4idXFab8VN_BNYuvKk2SUJmrsD33tyMjYRa1EJ7nSo5qMhSgXw_W3hU0lzrmNHYoct1HuDyD2geBxWs7wLEnfVrSDPVcDOWGWVJ8SxH_EV5XjnCjV6RauzpWkRrtksCn9B4Z23flPX0b632B0T4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cb6MzbMaj2kIqg8VOEOH6pZQtRMp1DbbAmw-jyd2nzfzAFTAPxfuAH50G5P6Q96PicT_FCxT55xWuoDQez9zg0Laymn39MzzMSHOkGAvAK2TpnYrY3sOF542iQoEB-aL4Uu3wu7fnrv1JU_LvLQhLYs88NCBQlXwiYAFt_GNM_OP9B9cBAGLfa3PhHmDPwdW321AoFfeyKHbF-3dsIKntZqjhiOi7ukYPn-qxMuVkQRpwEPayU4uZ6z3b2AF_NnpNrz51uJuw8PSl3ZYfWESmzDS6cfJvN_sV6h01szJsWhzUlufeXjHPll4i9fr2NIDN7Gkx2GniASDkVARSerHpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YprYUmuXdvOcBtlzo3s2YPRDMY_-ELlfR77JkVKZlFmUMfH0xk0ExkRpGFTxmyy6fZGu3avBOwLXm741p7KmvFIamsNQCDrXcASNpBpawqnydn5RPz9YfduV1Ud3AkmTekDz1qJHCYCk80-HwNDS_juOICugfUJLcBv62rPDTFe-Ud4UL9JCGB_qMsf1WXas8RMOrb4c2uvkQnM2RghIDfVX7HrfK4kJ4cjksuQnajpYaq6NDFd8iH1KlGgc8jNxzb-rwMYAHjqTKdbeaxyoYcc12E2kw823fkSN3-_eR-jZz1HBQ6AoQ8C3exPBOJS6aLYcJWB9H8aQMht0p69wFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plK4eo6y5Li5zYMM2p_dyCYpdN18T_pM14rg09QpjUGgLebze0ulf-HZeJCvkNTSuXMC6mZl461RTJljtWQKg-E8LZx1QnUIc6z3tVKNtIK1vMObf54w1FnX0FTzklTY1qWcIgRsSTJ3EIVKSCdARanB9VS6a_x8UyBNXXBPIgvx_LfPVZr9j826qQu8LanKefSUk1D_00oqvdOCd6g6EN9EFoD9o178wQ88ZTOaNcKdzc5LneKnaFOowZy4JAiYhcrC12lAT3SGIGUwT7eItRXSROVxm_BLybhILAMPxjtmZAo7WbioLtnuWuxO6XiIxj1lU-sd5jb1EXUqAxYobA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnLcXZn3F6FU6URl0QiuC3ZZXvzgiJpEViDWEwvM354lGengGlLy0H9zoU4rkNTpY1qIrDu-obTiHGYAMr1DvdRRdEXMWhOi2vV8En6ybqHf3jl9dPeHtM8bgR4ndKRs2vhieceT82rPXqVXJms5qCoTIWaoqU0gtVIY_UvPqD5iwDa1vE1KEyzRXHKll8mzYdJNf4V9GZAxAfskhmiNpFgPN-xaqBl_HjTFYKZT7vcP-dYmnDe-9girrJjCp56Y32uzhIxBBWY4iJYwlYtQgKjYzIIgbB2lmzaRspfYcszvOztgKP3zUah0MQvfzXxQtwUoK1FHcBHjzCQhX3qGRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sji8MGzu8d2np8mjDU0gBJPiibyA_ZFKuTUDX-TfIu-eDkfHSnKu6O5bSqjF1kgHgs_QOFS7uBLbgoVflbwSFnkN4Ls9l9qWW0Ik_WQmYQ5UYX3ewhDVH35auXjNj6w2bWehVhJ68d1AVTMVwg7u5Smo1mDPHAifUxgiIS9jlYSd_oW6sPaTMYMhIwPz40NCmiluGPrH7GVQSt7tPoeJlkQp2Z5uT2fVPNgaGEn1h9no0886JqEoMHcjv4KuYe3WOcsxGA8XOrOwf4mCxIPvp3akcLEJTG6YdGj7lk2-4CmB89etlqEjAeQG-tBFi2wdqfz0GuKxMIiqVuTxQ9FtHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af2VIbDjwck_CMD7FfQg13lDYngNwKzbq3SV_hvBleeW9WRVvUTWvdXOND2k_Cb-x5QnAUX4LQqilrRo718ZJFHrmo6UNc0z5sgWlc2lVVAORu2EHa-21eKecFwA4nrcCzUEzhyZGjyB5z-iu-cMqND1LY1ba3TNnwBrN9m6SHW9ku-QY0rbOyOIACdRcylLzyCA2GUGKEGIkR6_--lAq5JtBX-y0veGsO-4fEaDZD5LzP_5OiU4fL4UyugFgxLwDBvOZPKleBSHPYrUjTsFwgyD1pE6JKF43Mo-qPaM1XgauVMcHMD77QO0cTQGUzHetSad371d5dHBIKeFdzIrTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6TsNg1yAqQSb2nvSfdtE0cdegJf9OUwcXdjPVxAfCjwnZsVc7oeKCSx6jRpVnJKjfiqPdd9vmkWFIAn1026Lcw11muFwpdO9GSVp459OVnsRXpx98PBepl6FfxXN37IkVuwnJhVB35T2n-X4Jb-SC2fCTruIm-EZqgMLoJi93NedU2vpHDlyrd_l4KRSuTekNTOgwiaN5auw2MhftnFzYxYm_MTqwAlpAVSuHRiv5GVxvKWShomERssYJOC-FTNwC0M-qWjo3CfnFvD1nTFAD0BV5KKOKyvqqLJrPxMS4WLxw3B9QzcLKtozb5ZyuXCy2RqFp8C7RNyAowqXWX1YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOaQO5Repx1acbBok53b6WrryL4xiNT23HxbaU7QsqlqUP4cvVpvRqxcR6rgR-17sTWQhWF5qpL_CPZFcpdQHgmtOGA7p2AvktK3oZhIuJqpac_pBce75y4pqtgKCLnJ2-1bU0ZrbKmDnoHqg6b81odO1dDCncIuT-QPdQ0I_tHEsnYwbUVZy8c6Fzp0RDMnCA4qdorwdgGtjcliMdnAvgC-c9FEmXFYOSfy5tigGOaEEMqiIdJP4lYNVNuOYkjd-hheJ3DTvjV05MFt_9QnWKM93SX1gsZMOrkZ2FYHBwhjdTFrnjjrHp2oLbCegJsbVlOy9pxRcLbwXIuDBB3zCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct7TXXovI5YyM9SaH8Ot4s3_NW9iovkOlzuwauSnujxbSJN44o1VMUHpS9cKfV9C9W8kTQmBIu6yPt8BhmytuHgqvQt-5H2QWqBa_oE0OWwdKLIiQQHzUj-oN6gZqmX7ZhYV7WtTywqtMdb8F-yUMlXvhgvvcLt0JLOhVFXFmqQK9LVsJyFixfvgwgpvxW1Sd4Mu-eac3Ogfu1avhUbfCHjeOVNbcWEcUDGIcPTZTb9e8vcA50IXFqzxf48ejmDv6R6GF_nV7WUrX_xKYBIUbQBJVeEvZBxfo9VQRIbg6bVo5UjYGM0F_fznnsBeWUsjP_qPrm3emsAG_3FSargvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLLM7D9tj58VyJEGxzF0J0LyGG0sSqPaPk9z2mQrc6VGoOEljU4Svsd2r2Vy-kEKW1H-Fb-0pfpOGsWJWeZcAy_ldpygQDmmT085xgvzGMEAzqLkeKkQTjc8Ss7_P7knnBq-GIdIE35xink_ITF6XOLK04fTs5yRkSYuCcNi4lOS9LRl8T5wl3UbbqQwjY05a04-rqyCAn1-u5Cw20T4OxJtsC-Qs4jE7KMWOdtinqkzxjcHCD-enbTDsyBvXkORnzOcRPHTwctQ_BroZyZEjsNjhleyc6AMvfXKK9Iy77gNDocvaMFV_zNR5VP1rXoM45ZrxnvN25XB_8ua8cMhOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHXjKamKfJt2aMF4HuMWD-XcXg1tXgqmWu-6gMC845uvbQxHMReTiI7HUlYixeiuuCZJRNpIAAHUWcWfCIb4w1spvBQ0WldXhnl_ZfWugreyVthHpn0sCBkJwUKOrAnL9ysJTVYPyv6TP1WhozlSUThgkIeuP45INGZ9uCCUqSkcLxIQa9liRFg7QAO2wg_xrlPIe3fCDpOBhEwEYc2_nHvKG8qKJywBS9sS5_ghbMtr_uIs1cihCVNLUO5cTW2xviaq6oAN-k8nRwMpwFOBuhsHOjuz_86_NN-qV5RoGiamyBnVIjr_6udK2Mgthpv8kuzAydAo29zVTacKZTuupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGz7A0g8L1ezWCmyA51FScy688Et2XOJfJ8Zer_b1d2mjEthNX_SASmr-7sk8rU-vkuOTjgfQo_R_ssLDk6KjJcO6UjSBBb7IzIrfTQGPNVe3DGJwDnL0N8xs7LEvf9vWf1sDV81d27sQF1hhHA3dCkZdGNABotg9zck0nmLSsRz8bDIECICLT7pqZrrvo-7VjocURJtCd6Td_XIEkJbdc5MEl8dmjcek9YPA_iRzvRgPby4bs6XRFVaOlBrNASF71iEHehwX49zuhays-Lnum3v76Ys42c2lQetf_2nsmYREEYqXlWqXWJMW-c6sqK0Y_CTagpmR5sNXLOuuOtgwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl1San2UTFIvHNFLf37LMBhWCHQ1JlREtW1pWiT8mgGvdUwUZ5X0Fw_DDE7hK7ByVkq8iGg28OZ1o2sXlS4TVxq4cJemmNluibhOFbmN7c-Ya14yW_n7Zc86C8JpE88IWvpaz5fRlDHwXMH62BU_WXpuEqRZ88Nud39qSATiSdXAzomzBl3Yx1NLZ7knIINPl6mmwz9VjpS4J6RnBFSE_YWEhN8CULVumMNIxGSRzHS7L0PyX9fJVXh8GsUzWEKXBEcTNhqTmHnWJFpkYRiQH5UbRICqMbziksJxhXILiaj07k8W9HXU2bSasooYtKbrctkKnk39kddD3zBk2zVLuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBxO1cwnAbuwfVMtbucWxeHEO19HSS-Inl_3_6VSJFVv6bBP5AEKWY4NPiGBsTs6Wtvdhx0zHIp4ukct_7AYe7-Z3wnF_Wb3QyqOtBidn78HBQ2wps6g1pnh46AL9Rei-1OaCJJkfN8xGoPrKztNhqZQT1ZYJbt0ZTWhCt1LmwzP_Ccu8fzKwynNahHg1wuta6yN9rSrpJey9LIfO9-rqY3A3647-Iq75OztghAO3r64T_EALtccWpdPbuaSnBxsAnK0oeKqF7Et7_IJ376K2AwhJtaliEAS38Vp3VKftB95m4xvmix0lQ_aAKCMwbEfuEz2SfZnX4bMcftEG2ZNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauEZvDN52o3Xh5_liGmGVaPLJsV33sTqR-9OJAIAg6v0FgZXNy42XcPpAFUX1d4dHo5GpAJgyvTdOuFgy3yLWxm-_cICocEhWfH2Gt9x-7n28N3CSYGFWcz2O7hRldBOFcymyybkOxlw5JyzLkhnnJaLW6rBnuTifNXb6MBoWwLSGv9HVMsje8fMeGtaRYeaxMLDoGovkQevBmUKjPiwyvV8j7rADffMJWEC0WNLYToj_nKdVdrYLqmdd74YzVgup9VTu9Ww31G8dZxxIFnUeK4v3n7gNK4_S7J3XWvR6_foPOxfQBqO5FcKnLI_6hDnmd-AmkzrZqdP4KOfGeJqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyJnOvz1LdNQO8u67GJ_nE3GpCFAVzjSd4HVTKXYPTwZhbxHFR96JwVVrxXgsygBUEcJn7fiHcli7IRhnlizPmJ4RtL0swSUKC9HTTk90efq6vVAlnbTsJ9JTpKYh4rVJ8Hbu1WPVKPCYLzw-k4mtjyEDToGycrMFqQNmWAUY67CJMMvJoOqJyDkHBmBinmTSwlng1TCrmDZXq16067xkTTCjYdYGp9hI5O19K3Pe36p4j9lk-zA_XnnFieb2tFd1vtx1l00yLnn2tl7PqWxHbkJh6kDvjZDxT8Y6dLkXX0sUtyM0DgkwRT7muTqipTxdDsTn8L05YYQpSnxkMLxcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYUwMTw4RwRB29QDjCJBxVMLSrcCKPbKhPEnDAh9-IkfEbsYoPMJb9GlZBaKUcsqZB0ycslNOP3YTJjVuvDV9bGwaWeqeWq-3irXNrSRXg97VQovP9U0ulxiy8uh2okkQ5PnOjYQMiR7-W1iXkac3xuA_6tnBffjaciqxJs2xXSYLr1X76AnsSZFUuNaDM9UPagzhmWqngE1lvoqfe7jzSoKvyVs7j1Nj6dVAhN8-KwCqtiNoUcoSuBpMfIHWQUsIx7VwF4rvGsAvcmVez112AvjFYs1QZ9yr1OCY4jDkXxVhUvVI4m-rvEopijyH-I3QhJ5TQ_pof0McLAailAbTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvpabZeEmE4jlWHHOnLYKvwts4LHH86i3LjxOBRqSpUrI-5bjvFpHRNrOm2oRHv1UdhraKH0OOVegoE_CLJy0P0aaoWFGDg_PmO6zwfIRyK2t_yJ3e_GMsFY-YyFH3vD3HOWrWllLC3sGSb_TEH4CjQsQqch0Tv7yZuN36NVDWKIMzfNDS5rDXSZ4aUxuiWaQf0AVh1hQs1jeuztov-csyhQoZ0eFBP3BdgIi1JrU2QS679U46yO_mpTUfsSxLv3KrHK_uTibhPPMaqhCvTwYDFxFulDk111eVCKIY89I7rRDOTOzspXF8KXtnesRKhtwhvQyNJCfwM8PXVvo2I1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCk3Y2uaoqknFPMZqJlu0DF-B4SqaFACa7DcGNA_wRAOqs0EayX4wwkyap96YVfh7C5l9E5_rfcqXdrU6te2y5Ie5z7vDhWqB_FRvkRDxa4MPFPUZ9c-dsKfaOVhjsWZ167nb7AhTq2fQ09Etkf1DIlz7V0DUmhafl72nVXxWPQVYj8c7sMHcpWGOVi2ea8exCA7VdWCHpB-f3ktfaWe_jsKz6d5B0isJsZ1S8O6sSqUyAUuFHYfGa-CPKSe2SpzGZweZPBxGfYkMuEWyuYTZvT784Smsm5FXycy2lLq_SFKLm4sS0aw9qHqE8vsx7REz_MMvbuStiEs_wanF3wHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdn_29mTSqsMpzXVhAPkcf-jH_NlFnu-NQETFkjUhqOy06TykplnULuvrZ3UnyL0zpuoKUBQhQOT5tDrzzGazLs-698evETnVtxaroj9JUBZi8ln4pmelq5uhrJV1EQBaqBRiwVCtqA9GPHiFsUC1sASpe_fbE3jF004MLYt58gfyU1hbQ3B5aWXHNQRAF1l7hnVGiv3X4irmvT5YfIJT_4kA-wWndQ0pKQIH1EPvC09fslcHAH7MXVZMrNfXXv5564QReTfJw4sjvXpx2tFBkqqgNqV3GArp9z1hW2qdRUZoNgT-q0_1frCtHvF1dD-JKE-STUSTnxIhXi_zH5s-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT0hj9U16igJPklpl5OQZNE65SQo5cZGOjWlMHSRczninFn7JCEbl9dGbiNQDCc0MddIaLTHx_XYPFoRpXrIpfVXxnnZ_fsPd5xDLGQ_jGyVqzUHiRD5ZEizbEvAYbS1qffNucmdRTLPS2G39PHNXc0-F_1nO_0KR904sZkHvTV-AnRNnshtfweTN4NrOxdW2ULqlOS90KY9lJQYNWjgw6BMTFqKqdv1es7Rkbg1xpkPcAsu3jvX0bcMHcel0tPyhx0-pJEeOvQjqh41FlkluGeH7agrDX2J-jbmzegXvBtaw-DEWI6Apkf1RQL8_fXwXpQxyh0hIWTqpT20WkInww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR6U0BPl7fcOuyQztQemOMxsUeKpG-ZIhDD73cBGtCZWuWHknWktiMZE-UZ1LkrRtcgTU4IV1TREF-Vq7Umtr906K3XF0S1bBOk0Yc-_C3XHYosaRHm1oRer9pKnEmvUoj2KyiYqtO9Ba4amrWBBbXWDqEDKeL7cynO6IakB6SEhe3mXjbJ511scJjOUCV5prOqnEoVlav-wC-p-wP1876gCVAF2hT0Q2242CXFu_9oWc4YX8UUflhnEhg_IEpNcO63qv3CNKnUBUPGXTKLnsesIJjbGMKT7uJsWnW4q4ta4HI6yW4w0LsJtpBitC3gEHOITq_JBV5uIl0atlP_1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNGX-43ZmyCt2MJZ0AJHk4iPMhqdHTESCjbHBlU-x64pzts3cgsLQ9IzMbAZP_5GPCwcig1oVVrgrWBqNJQLzOHsERv4b2UhPonSHqNfVz1bIJqntU_YhwlLlUDNuDuQNhHcw4eSBwdKeLNvFW7Scdg7PXa3z6NjcxucvjsBw7sjziVCnyl_3Y3-vPwdnGJWbpQHgj9KbBmJx07e7ocViFry5Emhd08NjA2yz9BUJ14QQrdTYH3SfroYnURPme0gTn08NUHxdXdbrw6qqLp_N155LGdK3Yj7rxLeAQDpkjLIcmioPh1B-iIT3Xf45bOV_oBMOeB75CeSCVCxjq7Uyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iil9IgoOs-z1GoMN5A38nb6AwQ1JC1AF7ZPwU9-nSOeZOUeZzgYyCUKf9WXOJRwFWKstUyvVF1WefMsFWcGlQ3qCVAt1mVamtdXmBgFkdm6ZPUdUioRWYlB-_FA7pgHCPaLE3zkj_q957vAwef74k_8a-WAXvxcOuuB9nUEjgtW-VrvwuJIfonHpKeMgK3Cau51bIdejg-B0hkeylsCea0UDCILw7R2j5MvKyQEcP0fUbnLbFvHp99qc1wqjvgiGLmvMLbqu0rLIe_toFnvkkfSMr-YgClnyOZ3wPBM9WxwVY0s4iYYj-SmxWC9Yl06OvyTPXcCYm2FPRfz6E_vhRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaCr-UcN6j7yaLpVdnL3ekzMEjNEMll3CICE6dmc-eVnz-bNns-b0Bb8btYVT35t8NWJUPoKtMUDiUdAID1TlaeXAG7DE-e4gwL3Ljujvqo_DXwWUxKRyD_Z3zBrG6LvA2dlydKQPxbZXEam7OGHjKQhzJ1OhN5hSA1SeN7iSxHIoa2HyZq3e8pEAibfISfGKTKrW7zN2lREMcQo-stpE6n34Njh4iHiqNFZnTTUcloOTRFfILME6dY46qI0-ZH8gEuLHtJjpu3kcnKVB1Q3NR-pML50jFy4jUMc-WlAmxTMmWcbS-KyO2UfEor8so-mmw7E6MZ1M7TcTzT8DMFZNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fenQfBQdUzlb12LdidyegMBtsKaiNqtZEGrYq0OiTuoHygZrYoAzdjOZtpl4265gUKN43OO7Ur9XFvkfFCfczGv1UTkirWJtimaxvVdESJpBQV-e2Y30zq8Tz3-JAQA9KuHTY-dJfBWCXIUgZei87-oLgrWzDPk5V9t9jYqmV_JRvJ9M0PVSJ6xUiCxUaC3urutAEjYmpFI0HH1o7SWMVx3nOr5OML0adp61JOEMEs5jHuslt2c8ozOQ7X2xfwh8Xug6e00NcQezkF255oPMMk6n4grqkPOTNkAXdOUaCoIOeRxBjDOsDate-sY0GY7QIATU3nv3VUHXOXY3HhNKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSBLP55g4Zp3H062GruihGtE-zYJRYBvXbyTZgapKlEJ3jGYXSdPve-ubBPxyhAT0MJ36GgCm_K8ixZyHkwJRAbQJmcnFiVcicULrM8ljaInA-B8NnB4rL_mP26LEBnmrg3NW8CSpB2vkuHUkicAmJpyGICxf90Is_b74Y7YMLEzmxzi9Qn6mYCKVuajHQ6eMXfNidsnRXqOUAEjHuES1kGNEP-uZV32XSEWN2vt6TPSMFDN6uTngwgfdQvJqefFJ4cRJIbkMeKyh3RnCEYCLpF6bvImRDPFHWh3uDF75gBsn8zdNT5DvD1EUo9vCMFd2QN7SaW5jYnC0hytsKSNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjKQDS0mESx5NxOpKHTFTSNPPELuE50BAL7UF96hJKtxqow6GEcEBe8Aa1GOs-R2HTUT_9z1uYUeXPPyMUtMrGQuzgbj18bYChBr_NdsFsu6RSFxCV6OTl3mZhxIyBcBFIzfnQSIU2oboTv7Eczuma-UlshsgfVwwPXIFn0oBbDr-4e436Xs3xLCVwOyg76PxbCNA-_zAXNTa1VykkPj7gLe0eLZyqy_zxVdLWqv-7y-hbaXDN4Q4JszhC7ERFnbFFdglykTzAcYttbHU9h1NPjlg99DnERALghYRRICQrU7GQGxGa09GLRxIiYGTgbqvtJJXQHYRmIvUgdzgM_ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jr_ZgTE3kdIOxfLzaFkD4gG2fuaVAahJcysUNo9NdbvcKOOyofS4acaF64boA-7bDr5VQfvz9lyNpvajSRYvrma5Eb7IoMBAvY1SR1KFCHIyO2F9Q71PQ3da1oqVw1Uo7o1TJij4jsoXtLLLYle8E8mEXxXtVbZln6miWi9jyQDD8jV59ySZn-yPuzGk_dssYIxu3VRfwlbr-1WWTerOJ8_vQnYMvZdjHuqqb9xwIdS6KnpfuXBNc6yR-2ISdZ7EdHAn8H1og9JAt1GW-b9DDMXr2Av-zu2WsZxJUMo9hPk0HlGWkRHl-FGcTZIajgEW3Wm9QDSoPA8juHQCTzQhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcAiPKcgi7dHjCP2916qB9khJEJ7h1WE8cXphnyhoZxuxn8RIXi73hCkvbNEW3MRylz8lx4g_yCQsZjQBRakL_l-_uixjnoPsHueYKTjKhwc2mvLojUsYX81OGn3nMxNZDEEnEpDyyVaGETWSPUyou3Xo_YIqw_FUyE1gpLjxx-wQVLhIIs7513nJL55fduCzGi1GaClwXXFY5FwthshfDpu-JIhviyOG8P-tiqSxzvz8D0yFgBWiWqj8MvehPUGd5sLWF7tbJ0O83ORPSklLJrnZjdp_kV7TBr9-HuEpGmplMgYeMLEsFeahbuM89yTXTXSPGEv6MmGJGQJgz6P6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpcfCwnxSeFbW9WknR7_frTL_tZptauP7CVTYtutNmdf6HewnBtzDK8AC_ifcs8T4hdSdvXvOFY4TCKX1GgHuioBLfGzuc0HGdjPR9gWrbe8-wcXpIsBktPdl02lN5tNredbSVQbX_LXWOumTHR_hFOssAiz-BG1X6rpzRnsSr9CLwqgjbtIRXxjLH2ydqeHqJMhxQlg40RWbKZSfljQyl3JMw9QgK6ued9N552mBN7_L5CuJDB41eKBMaWuqEGFhnVMlzrAFPerpg1OOVU2PEefn4ayRb8RW4tZqK2LPh3itpMP3I7rZ6oCNCcDoBJdRtdFSiXVR-FTUs5nMhomrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV16gZOE9rBxVX45PYbHuE5b0RUtaVoB-zBiTwqv-BqpL9uYyeFavY2EMzFmYfz2h6Po-uUKQB4lL55pNtr53JaUj1gO7UubOTmZKj_RVrftKaXz9N2HCimgXDqAyVdNOKelju7U_0f26UwncXXm6zNnTsKju3OWqc7_H_SchbnOP5YpswqaMOLd5XYJay4edvh0rZojmmVlDmloj4o2GWF6s6uJnWHthsMEXRoU76aul1K78iSCoDkwkF2iqr5HBy_IS5NHwojPSwA_1HFZlY766U42TaUGxVJOeQ6z9uFVybhcblG9EdHbqmxna6WPluo52DWPgUj6SjUHAEFIbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7sc0j3lZajLZakQy2K05i9HW-FMoxpWiHhHw_e4d-sO8tc5EhbjFGkDYKprNHmi_vQvZdX8DqdcASQpgvC56ZsE6KS2yR_qs3QFbAwzMhiK-sTwkRJqoa-ELlULBh28HMk8fdbSvcF4kuf7oS9c3gI1-SMua963GgFvNOJ1xVyh8jDq2A4McSbeN7U6wnW2SUTE41HTlTXo7kfFrzmOiQVUJ8Z88a2Rckhm2AZFhXPRUneMydlY-RKZd6VctQ0PBjflB2Utjj5NjkwhRXe75rF7oWeKq_CunYy8zIX2SI2_cxE_zNn9ZzBo7iqvJW4SXGV_J-2GhgMZNWwq0jkyew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyJPjiTaA_O117weRijkFfLIFabyuhyVLGCh1QFzZXyc40GAWCzbh2JE2o9C88rcJ41V9SfEwPHauApD1fC3iUcjcpWIXuFPqFXPh6IzK6Uls1903gPy_UmGlM9MV5GTmHw0Mo9zCBfyv-Jk-9lvC4mJpACEZ-wjeioYQkz1lwakQvR4EEmd4px9tUOQ2jkajCpACxRwU4odA7DeTDhxadsSF2nolqgKYpYUI290-FQ541j6hFfvND4uo3uoLBeGoXloFFN2t7x85NeCcwP0OpfHQCz5CkkMemtQ8FXdRgzWcdN8V3jnrqcTkdfFzjAZzC1MP3PfnTEUH8ZHTVcq8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGTZgyKyr97XJAPpFNSePn9BM01OH08pRcv7un27PAAv3oUrgIDml1QWcFdBtU-FPqMhQ6ugKL2McC6DxXVybR0z_H-tu4dJfOYB72RUGh4t-F0tVHMtBRhY6YxSnTOpvnGUwpkne1f3jCOCxBfDXrTmaRu4V_DgdJN4FQdwC-Flxje_rbBh5Cp0Q9iOy6gMe738kNJU4SaCNlqYC7Y5JmR_aHDyTW504LP_oYpxIfvqkwuGhhVDBFWE09TCAQig2lmZvpVMKpaUIi5hs-2PdgN6KDnp86GUTLnL5LB8gr9r9ufkL3u1n1WEXKczFit1kHzFyyFjOk-GCKaF26tGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vv3mo82hbs434OTgHCd6CRoztEk2RwpVmx_2rCDSItBGhFjKW7Z25lAXoFD97GnnKodCHRRtx0tMSiUlO7p130I_vcdHycYi58W1iiwawVsASekvbEQn_SmIzEEWkbtYDS09Bl_1wwTVOjPkcWxh0ORn-8oKLp4RglS6GjNo6h0wQmgo09qEK2AlvE2onk1tfSbHhcZQzzke_deuXZN3cBzumqLi849RfaviJW3rPAtwGaeucFik8Pq00wA7M7WsrGNXFyfXi2vFqP-Y1wgyzZacDlHQ3X-P0Y6JxXxGc-DUvDz-t0PpyxjwsgzaSqczquTLu7K7onvdyT3Po5b8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm42GpzFvu1swqOK0vPvbBzcf74PdQV40zQIP5poXQwV5cBB3n1Oukl3RRu9R97oetzeKYuouySca4RO-gbbNg28NAV03HE3iG_sI3ok_RJhfvWFQrMrXEIaJZl9I_pIVKLQMFCtAYcYMwmVD7iwT2jEXbGhPIbuUyzxMRjTRuap8-6VK9AWF_K8rd1N0_oC9IWvuJc49nwheK_07oDLm5G_Nwl1vyye3FeJOM3uIu3KlwU9Xgk2kczMW7BDt8ZbTF4a12BatgeUrOyR8rycMJQ8USjWQN1ec6VuNIaFuxkS30RmQCFvge5hAKWUFeWscdK6joTkrFyRLZEk7xYvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlrPHY0yMunTu7w-56GO8PUGm8svNtTutNZ5DQ0HL3p-L58AVoLNzsIa7QiYmtm0vCqb3tn85nDPj83xxayJKvdh_Ce5sMfy9HazHT9Pqa8BI1RPyvCpQ12fev2d2L8cNHfz_NtY1DhT84ECm4vaZb9xZhadeoRZmgW5B58d4yc1GFQaQL6YBVwqy0oPCOcGi9QTIpcookqwHzakjJ1avm-BunA-hACoXFR_uMSnqy52yN1dfeZB574QMLpF8gJJwPNQEN6720BCDdiujCeDSa93Z2EK_HU7Nmwe8rmuHZ8VgD93eAmJhO3kaw6uOzx4lFtrNmuf8YPpbVxwVcvAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oa9e1wFBavTUIWHcm7gUThtDgX6yjnB5fqmYCwKumOe5bVGr_yL4iEisut5jJ9MzoqxfPJO0p2F9IjpsBKgWpkQhlyFcfrOtpIh-jOJbJKoCCU-vv0uF6ieAgaWmUMUNLZgP5GkkOS9DbmkGed6UZbNoxG98CRGGhsYKFiTeXq-eCI6WYQHToEWQNN4M9fgEmBorLR4pzfpS3ONYgjn5onmiq3dvMKrnfE77DpXbIWB_OKlFMvj3bwLydmNmsDC5mrKZ1RrAEoRDX7ElE6Mt5qSq6NBxmBqhQfxWuPFEgrXGcoWL4_xPocaGHHUQR_mpFW_c6OkZouHFZJtMRvPJxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZJYo-InfZslDva4BS73SGG_rRH8DnIv7lapV0tpEtD5OA-o8QzjD04GoVj78WcSVQlTHdyEfPYPXDlEbA0GZDgW5dXjmKAVsBKRTZGe1JIQO85Tuw35xqotxC2JLjsvBw_FNJVDSOmyHcRE16ARFKtH5mox6H1mPnjP4wVpyV9obIDIy4JdXJgx1HqGPGE8gSlmQ5xGYnojBLM1H-CLu6zYC7MgUfb4y_hVELMmsWsE3f9HPTafM0Ok95BBMAPKyixgcLcqWCVt2zcU2uedodpKCQovDaRglNESTq5K6K_QSOTsdjRxs4Be-r03t43i3NBcZvZdk6-6o1ilsIed5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEFHhSt3i0RY1246yyFUwMN6DqjlOKo61EiqSJiUu7kcOasTZMk_fSc1-vytgyA5A37Xb_IqkusgZ9VTElWUHdwAeFj3jqMkAV8Idr0IfEo0nGoEqwrIBdGR2b_Hjj6GZYyRhnkc07FCG5aG9m2nW99h_bROPpwNE7F5bzjafr4uQQ1XgqqeRGAKXHbL4xOQvrBaPgdxURcV-QnW4NTjKcWM4Ippoj8LTTAKs4v_NmKE5-OFWf2rIYhTN96J9FWzMYda6AHr7Gb_WGhL4aKtDPtoxO0DwrWQO2g1iJeGxO9Vxk9zd8RA3xoBDj4aZRNld1rM8BsE4a37eNkJufaPdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4v0UeqiAdWzzL64jTOL1rhEQpJ0-nSSP3KOxNVCeY01yXaW_WTI5G_V0QiOofJVUKslyvJNgEGxD93_SWBWu-s6GhCf2lvs14QidO42EY3VanueNyZ2D1cEp5MNH23UONlUuHk0MSHPgh2n4N82x-MymUrytckVOEDHFgGXWsbY0bqTXVvTNpCJK1HVdNPL2EpqgTqXNyuPk50pU8JOdTwTqYI0YsM3iQ0rIJ95Q13XZ5FNbLaGcVlo8ohjALOZG30diORqHro0yKuGlItzmWVl48guKH0qjAeWOFBPvtvPzO-Qoi8ozn2XjnXnNNmZKmX9BNZfjfLrIiMPDiTmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbt_V3JNW3TLznnCAchaOtlJuH3Bg_5IrIU80R7Zpvr8gFmPvJWGe0sPIAyBpII2SquH9wg50wPe6w167rfeYWpx5Ue3dzty-oOCJsVkLYq-KksziPUjJxTNgu0XpN3QDHop6Hv5SPsdd4BiyevWiGctG3jkX_n2MPzaokYKmMhWpDeRaJT-kZRZkS6DonP2eRR6C-zVT83l4ogC5zMhm5gvpBPnI2YXm1PVBv4DCvik018KYofRSq1mz_qzbh175bdfkkg0isnkPVedn2YxV3mCRApqUDszRmtxkRX6nAV6FQMIVdZwO9Los6xS1Z6MdmkBqPplT-r56KXxg9p1oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUobgmXS6-lKZ0gPgS5aBiIafWFV2iqH6IdLcf3CGXhSRvksQL4uYtRniWzTkjqiyOeiIo0QCYRPi78QmqhBFwFQd131-QPIpHg0yNf437X3pYxnD_yHFqxt6qTSbGwEiC0Sakr1Btp5NeTuRs_-Fc8iGjYSEULUubxlTUEgvt7Hd0aicR9T_LQhfVLhAhyQZuGBzN9ajyR5YiypDvBOc4AcrLTyFeU_YrIKLPPxL2s-Q1naAtbmxfwhMiBTufaSIbKi3tVb4njlerbx7VQTf2w2V7Vc3irlf_r-c4A0ue8_K8HAHuuAWs6teQtJQwRQ-ZohA-RUq7Qr_I6E6m-mqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
