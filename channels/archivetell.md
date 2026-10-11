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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-8072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙎𝙪𝙥𝙥𝙤𝙧𝙩 «👨🏻‍💻» پشتیبانی</strong></div>
<div class="tg-text">💵
ماهانه بالای دویست میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
🟣
این کانال ممبراشو غرق دلار کرده با سود ترید
جا نمونین ازش لینکش
👇
👇
https://t.me/+Wtmxpziyw-40ZjVk
https://t.me/+Wtmxpziyw-40ZjVk</div>
<div class="tg-footer">👁️ 417 · <a href="https://t.me/ArchiveTell/8072" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 424 · <a href="https://t.me/ArchiveTell/8071" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">samsung_root_guide.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💎
آموزش کامل روت کردن گوشی های سامسونگ
✨
فقط گوشی های سامسونگ One UI نسخه 8 به پایین قابلیت روت دارند
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQsMY622sjLZEeuPIs0yElyLazmiELwemGIvz1LK2FVOmPHmHTZ9NC4Ub4WqhXkIwxB-30OToe7EuURH9Y25Pw2jl6jQZih5ByARddSTDy_u5g-67J_IYg1Ewx1sX6-nQw2QfeUBYRoG5FcfLGxCrxUTvN4oughb9XP5wdyUvN9fKwQoJzevzVXU7W3gwefuntrcADNdXUHpP4wjmu8n4yXvXttrRjVhnENwUCXruSIlC7vI46jncUGJVyAl3dQLZ8zUExIwCtKbB4dCgsYN5vL46ZGxzQe3F90Tj7-GUi7YbrSWYv7B3yT2uw6xcWB9ALzq7A0JVi1FkqT3LmUEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
دستیار هوش مصنوعی شخصی‌تون، فقط روی کلود خودتون
با
Talorys
یه AI
Agent
متن‌باز و کاملاً خصوصی داشته باشید که روی اکانت
Cloudflare
خودتون اجرا می‌شه
قابلیت ها :
😀
چت هوشمند
😀
حافظه شخصی
😀
تسک و یادداشت
😀
یادآور و اتوماسیون
بدون سرور اضافه، بدون جمع‌آوری هیچ داده‌ای و کاملاً رایگان (روی پلن فری کلودفلر)
نصبش هم فقط با یه دستور سادس :
npx create-talorys@latest
😀
لینک پروژه
اگه به حریم خصوصی و سلف‌هاست اهمیت می‌دی، این پروژه ارزش امتحان کردن داره
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRAtUiIJv2wtrFKIzqdSKLhAaiHE2mYjxFQdzqCzzGpeCEoEiKx4aior-8IqMMqh8EvEb_kef6zzOynNchJix_Vy4FK0OfoAvAoTSKwIIQb3OG8I765XvEF3rst-j5TVIb7neO7iPh3uC-LstY__PjKyRqmrugCOUvVepiWs7iGbe3N2lAEilsRLo_uoGHmgbla41GeIoEqLf6Whaog07rhIK7210lrda6rAEeCibpWmVe6wjcA-0IvmKfkymB91ygx7aeYg7T8u9iOHcVwAIpEOqGSkv7Mtgmp3Uuj2916hIJ-VV3uM7NbzUQoa0af0bbboYVdUnumGx81-uzzpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmVr0jLW27hdlePlFJ2Gh-bmm-OJRYF8saisnZkAK7jYWslSAhMbjtpAbhJTJcwfL-x-IYF-HBKFE2iVGlEC88SonyoARJ-NMuxvEJZugxm_6lboO9TS-DqzKyfTLJuGfBEar4wxGXO3RLI1CKG93r7wbOCjHdnpy44t-7jyAw3qu4rvC8qXOn1lkTCyU1emjDW6ZmV7lJ6oWoeDiZY69nBhusFJay7YCe6ja8jaxpSt5EQg9Q4Era0mbOWGhzJfJJGZTT9dCDRT7Y9Tli8ECQUwoYAg7WLZDGmYtggQY1haIBMNYZPYP9EJq6C3EjS1sOercTMa2B6UooEuKt9X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8063">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑨𝑺</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Game (1).html</div>
  <div class="tg-doc-extra">5.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJGl-myINdDPGHTCqUyFnMuaAoadhSsCeVNNKevWWC8-y6EmDahjp9jT3yANegC9GMiH9MdEpGrmK3rjPRJ-kSClE8CrtL3DHa5Sig-cKD9iArVBBY6KZieOlAeQPxADiuKcTYKqT9B3WoleZoccFcF4NRPVSXM42blU2OI3D20x7MbmAFLQmafLgemESZu-5ONKc2evSZCvm7kPNqjW0y8G6QeZVOCmWhqD71YcuMDxSD22LbieVQvJhN0B4Uy0n5PgfMRyaLWwcNWWP1KLakQXA6HejJo0y0lzbzA-QorqGqplLT-gFTomWERHnIO-Li3bkTgWEvwxoj2M8VHctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFnepikXynfwi_pdb0pAaq6q5raDlW15miN5Y8ms0EzL1IqitFPIulnDu32HELyaHMnl3AfpbYcSGO2GUsoSC4oHm9O1Lls4TuloqjoO0gsQu-FzEfLC_PLL0Zux6IPRguV5B1iXzmcvUfoM2vghR9jkb0Vw4kDojiSAuqs7F3385bYm6jCOA-kTLZYgy7JoXhY8JAqxjgLDPA2j8gbYi-12qplXhb2-A9d5tZSCPmB8o7LHmdad1_jgko0Ea40P2ZmvgUTdeRtMHbUpILDZaAk9WWsxBPjnU0ei2GcUcuVhj5ZyPtjbksEaO5boi86_lIG0RYNgHf0Y0t4vKUuydg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptELzV1hC_x9rEIpINk64X0LkMHq-3b2dmMUiNoPqbOD0Mr0GmFObP8iwa_iQtCpZslrIkUBNjd5M3gs8vMfmhqS3jrY-Tek8wcjVOSiqtdI5wZUvkdnU7IPWAoLLzdf2IK6e4cbGygQ0aI03oK9MxZCkEHyS69frqRdM1WGMTSPFd-1lti3UM9qqoyMIeY0_za8asUb_h3rwCOlU3aFYex6uSKVSKL-9Ss1-XgiT3fMvVmZd7rMO64dGuu70G87TKEt40E-rLmiwMytSk6EKrb1bVEnbFKDfUdhfSBsWiNzt2qxUnXFOwWp0zZE5zMs8CHE1hn4hV5XqdmDwRW46Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htt4DNAW5ODDf1hh343DbV-PYPf24BpMBbymbCNth_Ca3yt5o0beVckOfYKKtvaoQhQm_sCYomW3jTjXUUgR-6CuCi32B5qdWPIMKAblyJiMWpUDGDyc4cGuvVm5cF6tG93c_hBRavi3QbwaOL-g2q3BeIZpZSfYtmOj0I-IDQ0BZuI4c1kv9VAygjKNNJ_TX4SIwf8Y9GCuONGYu8r997pZ-fF70lncDl-0RhJfSOzm1cPVm4vPALStULe2uTETlBY-OtHmeWtteCI1DVVxU79_9_m1bdFBjm100EPtmUfq-KaYDhD00agdDOQkqGk-6a8L-ikvARoHx1k0XPi-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni2TqB6WubMfTRzsnWmZtliePVRpruLDcJKzA3VXG-saUR76mPbrceJFRiqpJeMgJ7j5Wq6naq-vI_aHGOcnHvBoNrxta4GqVweLhmkcbROR6edAaQzFtQWME89k7v7zGwifzgmUI_TMx4n2G_58XROkUVWVif77cIwNGJ032ykHyC3eirnt9AP0db_utXmPFyF87qvCmfnr85l_tKpAbngPO8zEAGZJ_E65MHZ0-2farSgMLcoTlaRWX17Fdwyk36y3CnQXpajHaBKREzRiClldpgiDxo6PEprqpARZ2o_-kXpny338wK8obP3dLOkmlBci3k-F6IE20jzAmq_6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjMG3ancHjMoicqsaDowObEvVbuBLEB_wem-edPxzX8xzQYRtUe1HIp04g3eSN9g1f0CutHiwDuHrlK24et3sf0SZuNQAEMbD0jK2F4bT4ANW8JSFQyRZURYkcVwd1LqpbBgPyamZ2TNl8tjmNkit_mLWYg5z5wEymv0rzDyfsofqjjmT-uweO2TDG4rQVTbPWT7MukZTjRLw4GHgGux75ctbDvz5LaAvG8dPvnWfORtHUx2F4i58JhHAdTKSqlSxfL9etiFeijXQDegzmAgmYmVkDoKNMc-DoGvFcM56jWKyMPuJYQ1mc0lLFZEJVUHe8fmFApzwZiWdq_qFqtf3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIzuDsgrucJWWvXPgyayfCF6YK0sxp7fzdKdpLGKsGDNGAL3ftCcNlf22KE2j8J_8Ydy1ai4pWGD7EeJST9_DE8qE18hkcVfB-5Nx55GNdleKqSaSY7nWD_kCtEjPq0MVi-PXRdK1hfNenxZLA2lzFz9SP73d2u4Ob6JcRlm0TykSphjQGOp3tSPtSQPZNcS6rudD7WhjiaLTkDCwvJ1XhUyIJIjV1fX3pR7w4dMUfsotGLkLjelKY9YUtbD4x75sS_0pkr6gCeW9Q5LVRt4TmYNhqgNT5NJ5OoNDVKU0kKsO-H-PXOCHY5sTkkf78PAdkibms3jXuqta-PzQ9vmvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib0bNNUfxqWEB-s0aqHqm4G_z3-ksEo7ummmUt9b6yrwDzTR_FSHuPJtcdTQsJrHcHJBGC7KFYVIAoUoPPfZe5d-Ax4hVBJpfl53sCvhyoyQN3fkk2J3MHUzVy5Z26TijSSWbf7e26EHNszRmxk2fG8BbCbcsPCyC2XcPpZtGr8CFIlPWrhZrOZ5_yyrzXHi4euyo2vnUq9OKxd_IJIvJDkHdNjqOtI3WpFL4b773r6Vas3F1fW39ykd7VgsbTfqA_0J_IdRbh-pEuK-CYZfGxA-S6CFZr3TUg7qLnroM6V3fwWMzmMGHIF7jEGTAsqMcTwJ-9IP-ozfL2Z2cK_9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=pjjspLQBN4-bAHUd0y1SvoPO-0QvERuwR5JwhygdVq4plxTTeBc0HdQLdS--S8yGPqmCFRXzWO_iApWYmGWxB53tMvwmjrqpx2--_3wG-tOKnaqdASZMJ5PEmc7VPjk_mGS5oXBjNRoHPTe1ddXQFGSBtiNOr_PBkuMVnYJ1jv_6j0nrnC7KYXEAR8I7BicZEHFO-f097orAKqN_2ucD7FX0LHh5pIUzbRDbH1fsWz_ARUoT7UXMsX0fqLNyCd9Cvc4So0th8MLZ2jyqT7l2DfOd-V8unaaCX8_1jPd8ck170wVmvME20KWSdREsTN-7ACacclFRZ4p8FC2ljbm8UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=pjjspLQBN4-bAHUd0y1SvoPO-0QvERuwR5JwhygdVq4plxTTeBc0HdQLdS--S8yGPqmCFRXzWO_iApWYmGWxB53tMvwmjrqpx2--_3wG-tOKnaqdASZMJ5PEmc7VPjk_mGS5oXBjNRoHPTe1ddXQFGSBtiNOr_PBkuMVnYJ1jv_6j0nrnC7KYXEAR8I7BicZEHFO-f097orAKqN_2ucD7FX0LHh5pIUzbRDbH1fsWz_ARUoT7UXMsX0fqLNyCd9Cvc4So0th8MLZ2jyqT7l2DfOd-V8unaaCX8_1jPd8ck170wVmvME20KWSdREsTN-7ACacclFRZ4p8FC2ljbm8UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwoeN3zWLlE13FrjHPIspMXwVHJnSHBA2uQJSyN6dgoNI9uo3Sw9usDQ4Ne5OgrfZ3In690Wd5fZHqiVcEUwj-HTJ0X0Y24bRJfboJAEayonuCF4vBatNr_M9xpkvbJADOutg-t_iWbL8_otk89Efu-441Sto20Lg3wX4rOk7EL-smSKXbJ2u0WtL3PgXWjL1QaCyuOY9UoI0jTF_H4-rr3k94OjJlzt2HmCQeqilarnLFqy-Gi0AVSFBq0iNzKXhJ2Y14ilfbu7HMWOn3gL7aBErw522i0NGPUwgGwd3o2AMQhUrMPKxloQaDPchnGWqMwTBn2UY4jxCK0tI-3img.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P59KuDFK8ebpYm0cOMInH3Jn9tnLZVTc877uGscQlQhNVciBKGpXxcM9apWOPhmj-TewmP_CbQxAMQ-mFLI5HImN6aDCK_qkllU4GooVAsxMlkQscSC2vQ6Rxi57NYHPl20BEOQxqCWS6pZg3Lm0yVMO6CGKddvL9dDGHCU4yqr2_1_WHXFtUzNVZdke4EYJJqe0bc9_MxCuCofcrRlb-Qa4GTKIJKUFZgwOzA8j1_aORcvvCgf4K3SA1G2vZgizNDf0C8is9jQldSHI323zP7RQf9uZ65HX7NofBmKLYEqJPwiicB2wxphaqM1RNs6nZk-L60RQvo2WwvD7ef23VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8MSYLfBWo2W-7bqVK28vNkZElzGwvWsrM83y1IS6p_-QPI5HERfkDQfC_1u-cYz0w6OsaFCsW_TYCbIIM925nvmndrA4FzfvpyblegN1ZbGbcZSHY6De7tKUcHgGeWS4QNkogPgJczDivsq9hBm47nVxYCz2Ri89NDviwnqwPTzssMzjNGPW3bRqRWVginbqrdkCslOUDq9hCV4-ygJP1SG2otwZDy5DX80xUnUq4GILJyFtvVLdfNTFhlPk5RIHoPDAyO9Oe7kjJ91HBgc4tDyp6NWzU9tdqEFvGn8ZzSkrYgZHRqs4ErB6CUMr3kE2E65nPZb-DltNwdyLjNh8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=EHCZ8zfVcoOwzSUbxgonhdmxNdavjhtfatFwkZWjMZ7TDzCIs3mp_4e2u7bqlLQbVFYk93_bhrOfx3AgygH2l1MczL4eNRStnKGBDmB5Y5yB23jL6DCiQn8WI7jd38OBLwDO3SRRqLbmeI7he4KAMLKD_G0pIvarY9VZVKxulTjt2qcPDh5bfvOEL_RvXQA7g7aaHBw5JjiJFstAicjkJjfk6u7gWCHR-p9oHT_ulU1F7r_vtCk7Cz0H4bSHl-XwOxislGGS4Y8u1QRHCQgg_-C5AG2CYqv12BTIIykYwiSxbd8m37YBILVDX4Xd7Ftj_KReP4PIv-3PuOq1V1Hiow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=EHCZ8zfVcoOwzSUbxgonhdmxNdavjhtfatFwkZWjMZ7TDzCIs3mp_4e2u7bqlLQbVFYk93_bhrOfx3AgygH2l1MczL4eNRStnKGBDmB5Y5yB23jL6DCiQn8WI7jd38OBLwDO3SRRqLbmeI7he4KAMLKD_G0pIvarY9VZVKxulTjt2qcPDh5bfvOEL_RvXQA7g7aaHBw5JjiJFstAicjkJjfk6u7gWCHR-p9oHT_ulU1F7r_vtCk7Cz0H4bSHl-XwOxislGGS4Y8u1QRHCQgg_-C5AG2CYqv12BTIIykYwiSxbd8m37YBILVDX4Xd7Ftj_KReP4PIv-3PuOq1V1Hiow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCqnj7a3vFDWWc8B_G07woVq6KVLVYlTk05q9ChckMh7EqnFRkzNFSin3uBmI8uXn2djywscEk4hrxvzci3DgkYHp6HP9pluDa9YZcCzToyzBRd6Q1tUOkBMgMFeC3bLctdpNU8MButhM-OO7BMOgzikC8gop84mThG1SZ2LQM6aXw-R7YaP3JsVZmBls0akvPgm0D7t0F25veX79BC8FxMpbXV00kbjs47jUOu3p_c-qRJL-NrlNv8jxlWDh9l4d6Bn5JVEDLp4Z23eZ0zzHwHIRFIATMjsR-XQj4MC3hPXZFf7wcgEw-ji2aYf7j6sJkkLV-ml91Rh-TFCAHnAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUkO6B32paVwAPz2FdZY5oOeJ3FnSR625o6n8-7PxmWXhDH3ZxyEq5P5LTQ451jJ_SStXfoJPOtKFWWHVCV74x359raqMZMcAVmVheHDB3TcgwCcRQ-FTQTW2Nm6yZdEhpB3wo4Yr8TkYT5ydAQmL-lDo4hAJS09lvwkoRux-A6Tv1h9S357K34kRyqzQkCE_7qWQZDgde2tQvsFrhQmYWJPUvh5aajrOPHAk8SG15fxOBfyVcQd_cCOAp0ICQ8j2N9WR-6jb-eRLa3VrYHuP5WkN-HWlmYNWnAk3KNoHKwFWJPhSbhILKzRbtnnry8zQX3zt0KFrsBaQcKYOcrZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epWKYLN9zBl6Apq1wWa-K-dJZeISv-1f39Yljhx4BhNABFRAfOSTeFct32wuL6h11jHDUxNwlcuI-l5sj9Z7U295t_89MFRYzJKWPAc0sUm5Ee7csJ7m8zoYDrI_4pK7uuKCEmQ6818K3M7kOWHldgx-DR1lu4lqsbpGB-qhot69tMt4sIu8nGk1sBScHAqXLRJM0Sx408qrQUq5zhik2CYcfINVI0HRn9tQd9ROTF8Q4BXClMWyrcR4PxTFXr4nWiRZW1CUrDIGnE0skWFB0XHQV8v152xJ3E5WU3AyOttutkg1tes3ET-A3YbBffyq8MsE8lgQXj2Sb-D86kWavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1J_jq4fybwrKhdD_1n5F4PzdworI_JJfCLLcUI5G9i8xhOV4F7jVhAG6GpaQaP9WNwpSL73DdZxK4X_a6AuOZ-HOFOWmTMlTcry0r0Q_maBucDxALTmau-wCBzx4nCKlYbBEWgtMUayxREbROm9-UcWipHA1qrpDljFxvla2Pp8uReiFwveIX9JMUrygOfbOYKwxyLCfDs1G4lvK4rKlMKfeONaqesN5RMqL1RP4dBD-SQITWHB367o8sKoJpxd9tnh3qR8Bv015U5iD7RYcnNS28ZCJ5hDbKdfO4M7mICkSSTNq74O8sXe8wFq4H2HGOuDBbG1pGopvqZzDOsCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6N1bLxllGlVGrTVl9hhuIwkYfvuCjCNDf8zBfxcmVzxHwVMre-OQu2Es6eS-AboEZ589VNdJ3yD3uxDT-1-eU1r84ndjw19zt0_jjf8Wb6bqmWQsvi3DhG2O4ttzDR52gRpptt7axj0QxW5rIgNZsVaqfUbTFbTcPuxVkCbeAqhLijZvp3KmS7cI3R6rXwZR25XhAI4may8tuFEpIMVt6SHNbQyilCp916fudIxv1c1rr8TbyhP4AvdThAH0u_zAyGtezBPKWvwuUntNXMT7nLeTfnbV7zpIxSsx-z8eWPZ-ZgZ0HMbKr7-C0fVhHmFRGY-1I1VaOBgmSe_tWAxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_nB0jQb76dkTBFEZR2rcvcFVv8YeW9KT_SLiqNojgt4Fy59N7NJM2fYQwW5Y0bJDqiHbKUvdhMp0We7sjxzBEoNf5SPAXqddldDyxIPRSxz7qRWxNGfXv58rLFbZ0_UQinHDbAypKqJs8wnLFZRwKo2xJp92aRzxQEwoGmh5iebpVhebhR8GiadupBqL6UGnqHCr5Fpc255aLblsOoP9LrxxO3uV0skstkj-968voUZebakwVIqxF-J9PwISnlkpHaN2t5z8CJWQZ7U4qHD8ek5uTSU-loqra2uk_X-CMYHZSwFI5boqt6Vrn1eIc-bnFui-EfmySdtRW4pkP5PDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxjv8ZKFMEa-HeQI2FpUYpjRf9FJ-RTSulwocY6pj2p8QiPdNAC4NPBiLt-6CsA-BkovWLKym7840SfIEVzUPBZWQhfCWHMhpm7bAsnfn-vgLkqJdUApP6lmImHcKLIjH87RSXQAmyp-LjQCQwYWJ55EF1U6elHlDUF4NgEQMUWOsyxIgMkUhCO8sfCzHtjD2e92FxnVTG2CPFYVQipvU5UQwBTKDAWX6Zm1z4mJ-BVxGvdgKXwTxcKdDYsExEvHTBLgOJH7mkwqVsH4dXHxxAamVm1peXIPxqFqqZussVuHTiGlMr1ozO-SkDCzd6epI8aFKoWpM466pqzJyWUxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCPlfyTXxCdhMkpfFOF7N9-vTvBkmV-0us_PNcxaHnjgXiJGZzeMiqmXWm7jbJup0o3ArFwEcyOAqoPP47Pp9oqsAAB3bHsue5QwrhLB5960gBAZgiammG6tB5Cd9eK_dBENQmPEyM4_D1-ZKafM581ybfBbKxHtbj3XuXnQzTYuJ2JbmdNwsoMoSGqBVRFIAtvxIbppxBDOvnZzrs7zr-9ZrfiqdzOspHDUONmNXzXq-6hHw3T8qTLAswSxezCleHpxxjje7XaPS3jyU-IZ33gSHHV0ZfQRo8br5m8fC1sZ4Dj2WHCwWn7vfvrIsLJZQdauvvXhdzbP5fW5Vr5xUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1LN9dumToqUjHKApgElsF6A_J07QbY-0StS2etqY78VQqKtYm2h14DS6D6NQNTXDeNNOrE-hqzT8bYEbAH-SLbn69O7bE8eD9BEuJnqqyjRQqgdb3gAOxUiw7IkmJY5ilKKPct6VRpi-aFC6BKAmqKgW2RNpelujJ2C2bl71QrVod6RxI3sH6Dzwktg7UGYfArbtWMbeJHKrJVwxEocOyAdFEDpi0IsT7M0SA09wBb6WoppZpvi3XPT9fTIStmOGN60TyKxHBEHt3tQTaByC6gVKuo16lqPQf3hlTbwIDqL6tvWgLMKns6l165983HAmb3_1RDMzA8WuZFjrDlBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFSzvBU6tAm1WGNt0Cq0d013poe_WIX2PD_u6OR3sl1vXf58MtxCHcCNA-c9EeCi6CeO585nEUcEmhTbbaAryNw__LBRGSoPvLUIqOxoQn7MFCs9DF1MOr6z5PJWqSOtbI7_BK8xYsV0SKzpoleEPXxqDdKZPsmqqMeWeK0SMK7Q6FqHO3B_82Zb4SdLvazXaEDo2fFmzyW54mrtfJ6EWGhwa3ntvjvX2--xkaex8_fab4SUMQuJV4bdJVReaswpKLLyza-9RAQHcgT8imosPS9nsBqZ51pOH5BpInCfEX9j7aIiCNqgQRESi_whpl6ZocJKI6oZ3ASQzQCf4q-4wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDYqIKbyPU9sIgotlMqZiLKZ8fovJnPEm2Nx6dBwcn9J_vBXeok4qysBE_7TYTVj3w0TUT-kwz_lNrgyB5oujygCxwBG27JM5zkZuA_AhNnpRAb7jYZz2b0OoOrQabd5OnurqqTMXQUTo0dl9OYDIbaHANPxD1fBadkUhGgLFvRrNZXnDETzRN9i6PIBS9EShp24t5Ob-3oKJEStUYN0q_MRxdkmframQP-4_7bq3ueWHNMBT1C5Ujch6I3nUCZAHf1VDxF61JbqnX2KXS2BKfyZA61eBjeD-Tc1v1IB64JiyNlCx00W2soKxMbddUuOtpxDdrWmlle3atih-t4cGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwc9mkhR6pQjHEZKZRRDKaKM3rbFWH90_bJ-2FTKvkS3RRvW7VnP2_0CLiKRSe1SSz1_yOp-e7fqZ9L4xmRbaw-FK65ARKaxaRKb6lqmROLLevlTFzZMKssDAIXTfVUsPOcArN-0Th85mrI-uaZmhT23l-r7buLAjVK-EgvrJqsFOMuwn2Gzj5K0jIm5-jHeyJWigLbcijlCh1uxNlK1o9miaCkN8Vo_Ry8Kdd-yGnF7aqBJLQgzbeNWGfRw3tJQiZ0ooIClpBr4F0KSlQpk78-cOexE5gDdYWm_JybkkcF95BXNurvk6w_RwfIyO-Rv7lmYHNuqsX6FoGNr_MZs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/stFnd8V6XN14mTaXwUfczBuLz8fMekQMH2s4I_l9orlFc28dEWWA1NRKoPcVvk08C8bf7eFacAv4xQCopxihZmzXuLEzsHm14b-0vQU1Qd1ScRcefvzjoboIR1Iscvw7gA3NbsNee4IL8MGbAlyKIlvsm1V02AqaaT0EMfxJ0J0zRuN5y909WIXigj5WsEfOYrx19rZdGNTGQ3pO9IO2dORycft4jQRDu1O8XXEehodJh8beohvrJPQkdDZJNUcEDw72TM1IGa1wR-k2YiGJIMZ4pHObRixQmrQILeUVYWbVdFPTWA9NmDsX3gTUftqi0NEhNR3bee3rdWrgsa5-VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMEtRmkJuPc8Y1UrF-CsAWaUNq3zOwpItBzVwOtJZAqOaoefVF04Gd3yYj2uYcNx1rdd_I26XPZS0osMirnFxSIAMD4ixhjqqDN5pkAYRVhZEPb-26-btMpvJKPE_h2lyORTk5ZzFoe6FykWbKZLk3au_EO_wFXo_wlCsKYId7WCYUCmqNSrtt6c5zAn1kTaVZDUhwfenElLXETWdsY24c5Kbz6Uhyw8yfNOxTP30NI1Xd_pU-mFYWv-kAzYICz38ONl_vWZ66RJg8T0PI8dXk5VIWPUKSrdOkdOMdgQ4Hn9pOOKVyafl4_9WxqeFvpFkh0i3TaNDSw5ecmiULwfMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GNo_6JWy8HVgeGQso_OSg_k-rNv7rlA1m0r9NKQwFTYXzvpEZP6UgJWir9Asz_Hiyp0-taKKLWQqu77puT907TUi5inXenvaouXfRM93NjPjpjrtdBCERjF2xkfKpwXx39sIG0Q-aqo32b8qXWzeXwewK1NVTAguODhBgP4MSbK0VXm1NM0PMDfDbxwEeu_9tLhHFSj9qsq3h4HyoTs6FEWLGWKWm1EnVE9P-0dhAUpAuKszWzPaPJ3Ff75apZibN-YTSd8cOxIOzneYtvXnD8tVf-cDM2teTvN6SyeRrZncSh--0O7XnkPcnhwYYdxY-iiOMuOgTHPh77F1oDtEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GNo_6JWy8HVgeGQso_OSg_k-rNv7rlA1m0r9NKQwFTYXzvpEZP6UgJWir9Asz_Hiyp0-taKKLWQqu77puT907TUi5inXenvaouXfRM93NjPjpjrtdBCERjF2xkfKpwXx39sIG0Q-aqo32b8qXWzeXwewK1NVTAguODhBgP4MSbK0VXm1NM0PMDfDbxwEeu_9tLhHFSj9qsq3h4HyoTs6FEWLGWKWm1EnVE9P-0dhAUpAuKszWzPaPJ3Ff75apZibN-YTSd8cOxIOzneYtvXnD8tVf-cDM2teTvN6SyeRrZncSh--0O7XnkPcnhwYYdxY-iiOMuOgTHPh77F1oDtEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-jEFwzNaDaXAmykWojduAWGA9drFnURwyFAd0u7q3w0b0Fqsj6HtU4_QEw6AgxdIUuN7Rme-vCzsQBZC_NhqB_iQMcancriy5p2jUS6xi4IHuJ8Gz_IbOwP_4XekdDBse13YFkaeFN2fvwh5yfQkUgNwbgYQaHAC09ehB__wXw-hyg_52klGyk-1c_81dA52Jw1rV-AVsp0BFPMoI7lQ_4kOjv_yYDIpvfeCBUiDdoM95uRC5LJIpMHYtFF_xoWzb9I8fyypw2uoVs47FgtGIKt_RDogxtb8AgZR8pnOHP14AWwv0E--iZ61aJ1rM1yGC0op_uQt1Lg_GJzfDK9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1C3zmA_nqG511kC4etzcE2dFo9SwTlSZ-RBHskdPEGvJj5WjDh_C0EOQ7CrHHkt_L-OXt699bEUqht7iO_PBfcYp5FRxLlzFk4tk5NvCCPl-0JYOmTNalGHnV2IAycozdZ6lHUS2KTlw4lqcnQKB8hxXWXRsyQ06qlxO17Xl_SIQ8xq8p8cmlIH3KlCD5pBGMgIXkuBIHhs3Fe7WfsAwFTzI-ttFxqIz2Q41ohVirWnQKXxVi-6PDc15Wa-hcWcTJlZMdsTPivy9jaH-wD8NjJOP-ddB1BbPbP8B3AyQOnkB54dOGp1aRSKufDXUt0q9UpcvK2V-bPZQuI6_74Mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sahETui0TY3kfOzFA47246kAV9o3DVJNUC_wW4dw9zAiyZOYmcM0mgRKkAL9Xeq7qQXhHXLi_WBILZDe7zBzQ4Nef3c4Tfgd8vykbaS3B1LFZIgv-z7lC_i7twdhjumhWcvZiEl_UiBel6YzxncIzZl9dl2Oj_0XUbR5i_dQTV1Ly0ifGTPjbngRsCQUezvSxBSK4rIM47AtVTBXUaHubplcJwRTXQtZUqiDKcs1VCljS48lZEnbMDJHFSHOxgq0shewzkD-foqL9uXanT0jpaud8pov2KPhEguTVfoiZciueByuioT7CEQkvzkgJHYtvn4_9wwjPObVt74u5Ir7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPxfX75WWTRDssf06BVi7a-s-nUev74muO6rrdEzRQtq50OLQuQnI5Set05wrgoclUV9qCBddTMz-lh7E2Aa1UZHWuXYNA4mr6pIdVek0up6Y79xDbfc5AWZJIHeLKkEYfyb8oLIMN2dBOOASWNlzaWbs9TP-zow-mypky3ZU7KHVzM9vhX6IWeZ3-I0PV5OBatpupZY3O4obot9DE-AYfu6RP4eBPCaYCFin12l5zwbcT9PMBEJj7wP0G1hzsMNOXIvWCywfCBR8rHUwanjaqfLKAYy6GD2QnrpW941rR2KZOiZG8mnquVwUFR96QknEbJ71IbzSHADxlU5vmoavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUZIO-t9Yi0-ePkiIWb5hw5dL99nFfOU6BPpLIONuu3YqnDg36DGd4cFETpylkAkkxt08k8TDVmBIhC_gi6Qa84Ut7wgUzc4EnuSVse7QxboLAc7vOzT5YWdaDw7M_OvGfyaJKiPbOGGl9N-v9yI6lg-hVFl0y0sLJHuA0d9vUElfGAWEPW7r5WAL3d2uTD7YEqlTUZL0KPVYHlcp1I6thqFZVBpCVmBhNJuO6Vj8Xj3fVhdhF2L6U3NjsI8yS-e0SUqI4AKT4VsA2U4zbsiMwTtzmvvS7O3pXxelBLFz42pnAADS9pUQLeB10DasLF1HTiXdXts3vtroWyxqzrgRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puX7xTe3SLPnyOQLrlWIwdqh7cu90sCXHg8Rcte7dabanWwIEh6PEmCEHwTjWzVJA_h2eyYdtGXwKmHZJ2Nl8gWiJ_tDIoNz0M5Qy29H_8dQx5kFC3EwajQn67uaL6UnllnHdeUTLeJPN4f3KnfJiJgcEjLCSM3Mr0GaMK1D6qdTWht5cQtvrb_yVhVDppLyuuj_lbCy6BuT_z-epGGpM1D_JhN6IUDffITXfzlp8CCVcwyN8NEQbB6nKEC2qrMHqXdBZZKBemqrIRsZgCRFMbCByMR9uU2fuU2MxfaH05rRW83R9QjbSbKSiHDmW2rBS4-OTPwhTldXYW2IpU0pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avodn9QaXIov3YL4-Hq1HFceQ7Dq_kHN_v7ut82V08RezFyRVoOaRrtQ1sYOzfKUqTZuK7hnVX7hm6v7lzg8Lix4NBURNSADX3fsJCrODO7pMnobqZaUl2C6lYYxlaXqQuEm_Q5worUAiLUrE2dAOpNzO5qV2FJEcI0NIXWv8jVRdxG3JaYT6uFHKmSPcg9ejD-MRd-9YIEG8mRyfXmAzuHNmOl9j7fAq52gyVWzXpRGZS1yRlmxXNjZHq_5sWFn80xq2p7W6q8MVvrsuyME7E47LNsIANyH7qljowxwZQ2KP4SKTcRY_W7VHcT1sGtO8BbwPWPEKi-jK5GvhTrEww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NOkbhsy6376NCQcv_ztkp6PJ_OleOCKDIYSRIJffY41IhssMr5R3eHGRK2D4dqKUTGrza9hAzAWUyhSX-ADSiq-aP-OdeBKPKxcC6cgPlQbzc1RgEERXssbsdneG9Ciwquh-LWrl0H8hqT-Ig-Yh_fzUWNoUX9a423U4sJ3YVG9xQom8Ua9uBgoTMUkjoH8bTxUJGouEUteHBKtm-jXy-3h1NJbwqRceBOR6N5lrTMh6zE2Drt0Vuk2umw2zUAzO6fZQbuVYhAUbbRXOSPK0fiIJJPhjeF-LdJ4biGVUWeUpNiBCXJWWi6ybtoZRNv-yqkW7fuT6SkoO6NNUQIBHJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wBwad5yjSIHdXuDUiT2pRJBa3r0LnVHgSXSEwm5fu62uiqCjgQ9tL94WliyRfyPlT_pEBghGrX3Sx2Gfg5NxcoGi4Lebnd99mfZtgZNymWAwvHdDjXu6JOlNLa42zwHXYKo_W3bBBosRe5Xa6un6oPxy1MmfJMFv_VnII-Voi3uMFgjTHVtHLh7Piu0zduICBv53dD4xmenrnTKYGNjAsKmqiU-cUIPj0WsSHa6bgz5Fcf8TCm8_Csn1lFP190gcYGCROxqwnUfy98br0h5gvWc_FeGU6_XH_ME_uuEeEsP_BJxELmqtjrO-IUNioN1DqWBi4baotBPBnwVmbD5GhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-GJ2hI-7v3Vw-zIEcRJfieBOazZWnwMfB-2E6KmpWNwPYSXs0B_U85_q2ot-j2mENfnfWSWGvatjpeQgH21x5MC5U1QLXo1RsMOgk65yT99yHlCWNxeuwwBd2adUa2AWIP3ttuAvQof5yQX3EaUHPB_fa2wfynu7ca_LzkfPg1i6F4BMFf7XU4hvjbvMt99RcL3G3RAJYzCRnBOZXIPUyFBe7GfcxWyA7R9zLI6msVe6zlnUhuNKYGa5jWz7ShunQco-8pYMGfhLY0oFk-9t0WqtWyoxEXtDIay5Iju3JKLyLNPdMZb-n_sNrzJ4Uf8MbMwljoX3tDawMZ5bTMKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSLkVqjX0cFc2tLuQcC3hRA1RhVvZ0AbpDKSHR0cUirsTuOosQ0X-8skU2YWh_Sr6AJbZ40oV4lrTpEnuMqvMITwqlPVWg7FldjN313Fhn3WS0o6zPflOU-HBld13UM8qvcHMPYR0v3vIFIglZrmw05QTrWRg_JmD5nCVUAKB17vw17CUI_JHNB71Ybx8AtIaAyreQ8bFVSlGbeITYRSxZNiBpRt-3HXSIvJfMpqvaZfJYPaMeweOINQjud22cmq3xLW0NwjspLaWcJ_IXpr9LN8wMkWt9YyY_QmJWoHkIfXPXbeZhE9T4e3UjcgKlMNm8hasEPGUs0DEULTOLefgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCExrSlIiF6cyaM-ySMkkLdK6m_zLii5-FI4AeAKE8x0AwWampQfmKzhn2mYjKg1di9dLObmK2zh2d6P-JJ9I6kbH7Xia9Alh29ng1zfyETvmJRAzIm9K3-sKd6XE9cz7fRlnqhDWkCPZpyWobnuoHS7hyrH2j2mwUTXu-nJGduSOdow3NbMxWD53_cLvIM5RPWX-MRI2Q5Uoaz8B1-3Y5LvAtNbgMmrTgo2OO1bKPx24q2_XcxaGei_K6WNacQTe8Vnumyrkl2pOWOG9Ema1GvgH32jeGFFFHLqH3F6TgmPmI3P_unL2oEg_cF1xpNNarlyJJ9jfkLZeZeAu8mRQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKRIkxilR4SHHeVGsqy-jxekZH23RYYEK1hsFs60rwC-VpgRiTSX5iN1QNATa_IFX3RDgZmhTXEYBMvH-gsNIsckTQEAw0ivrw6NNlgzE-6DKlCaOfxXpb_F5BRTKnETZ3Mi9iGHXt7wRBG9AiLW_t0RkcDF5t8HuCXkLzewKvongFEXDZBehAEUH5Q5t7QlDAGRxGcALzqMZc1W_x_xeKxKbNxGERVmgnijkN2DOt63S8hv2rA-sSzTq2PyluKeuehn84gNcgOf9jI_ScamPnuLZu2vTC5BzyWx7cHeDeQqZVlaalvguNxYIL9usDaSStSloMspZsGNhQjecf6blw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvzYAV9jvR6D8VP8tMch3mqfHjucbzHwydtyS6ICpitLUX5FMu_F4Gv5iIQV9tx1XLEWOheSGrdswtODeO7zwg7wJqoxLt1l5V2OaX0PzvEI2ERdEWdPXESvhw3JWDNYtxNggCDWhd72v-D0a18y_TTf_WpdtZwqlFqk7_d4MrLOwSWk8eewXq0aOxzZ8UAuztLwT43LwZw_bEoZqUlN4UVvlFabHcSSfReGVh3xnXrvXFP9fsQP1uT3UmVUdENvkMQ53i9LO1TzwxYkbBUuFlNDCEU5tU-ANVgIgmVJos4r2SYI8KCQm_yPae1vf61rGTPmiARA2EezAVpQs7ZjoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG8bVcrpurH1lahNllrLbuq7QdOzh-eNQmUcoZ_WWtPYO60D697g9QgAGLUnYGtrmPDD2Vmytfk1sJT0py3KqZsubEpn9-ENbrrduGyHYAg9nD3OSRktQl4hus1FyKlkBJNtLRLMjK-WzaR1TCMyvRvI65JcvM3TB9JaGRJJ9-YSUzIC3BGYJHxLhqQGOlbqfit5_90elEx4zajA0Cl_NQadjcaUm_U634DfTHjWL0yYxPdNvTEe7hNr5EPrlGbw2BLHyIOKj0_IAvuVsUKrncy2T7oAEnH07J9Um8PaEhtjqPiMSMt3nInibN52Bjeh2tuLa6hmtm3tBQjjef4yVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6g0rxqmGiuxiEu-9bHTIT0xfqq1g0T8f_Yy-W0ARbVjJyRH_QHDjcP8ewnwMJb6QWdxQom9e8wjyAfKtwrgW_BgsvaxEtTQ_1sjYqbHHwn2B1NAFkVxhy8YpAp0GU-aQ7iwFNrFMZZTnb-vI0BQVHXWxbBqzNXrb9GDqn6lWz1_5F4Lns_kMbEDUuHQS5EAR2-SGeppN0uaMr_X6cpn0oL-z2NczI9iWN2JPgP1BokFf8HCSLbXckU3Mom9DZ1OvSouUyCi6W-Yo59gtnsYGLNiF1FYbnsWGgX5cBn5QKWQB0j4C6ZZuJfWr_N6wRp9RoJ4nI0Esp9TikL0FI1-Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfTPSlYu89Gdwpg589b9BNlQNvy-ricXEskhq2Vw6Ftl3Jyv2gcchtjTpZOT-ki-GC8BH8kjflXVV5z0GcTfzjWsnr0vJnJhnamajfSxkmVCGmTpzCR57GZmm6f6aYLfD71SC-8zYhuk6lG0qAV-M5pJjTNfEQwEMMc0w_Jqws1qfUPc8g74RXp2DqQAk5cDCSFSfpKF1E_-LZBpFx_LOjeD5SLaYc_fixeyVRnQqHEb2MWEpBm3paskcyfPtOx0pkRtcEJL5mquIeeIoTXCUs9rs6H5u5ew2ybEl1fKjH_bTr6kQM7KTCcRBzKQY6ThqER-TOzwKPGU0QMyW-5WYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adt3LBxQ84DqK1QLf1uGbSGEY6wPic3OPU12i5YbyTd9VhpK2qIfUq_aI7B-7EeFKQmY6j60VMVH_N7_d9h62VCKfh_J119FjWS36FnHosxMmuFkm15qQFCRQk86LN3edLbYUbmBeEYhAlxTTV9J2a-YQlilPMp25l3jdUShCBGIYZI0v8sLt9SB9EvBleLIIP0ASjWI28Qsfsmui2IeDPnFJOjT8wvYNivU3oBwZhGpf7nrWRJLMvF-ZP5soJtk_kKiYrC6ViT9ONCbHA-pQgS39Pu_cx2jUfDljsc29aRA7B5ccMoh4JjJvLvDIDKlUAeVexDL6k1M0nSwjG9UmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2_a2yUwC2eytzZaKpRuiZ378BoZnw6Z1_K-ON0ZyxMFZCpPd8xV5Hff4m0j4daPYrBhftIR_2TPceUwApKC1dJVQeGVzIdJBTOmzYwd1ISaym8I6jgYXoWOONuKtgKuv-f0PDk4hkt1G66tRPrrwOyEtAUzStkiojOfPSZW5tAGjW49_pkk--xWc2nZYhPzya6gvDUSPyi1X7W3VYSBnQbZY-n5H044mTPsdrcaSZrJR3X_VOQng4Mk3lVcHI6aB1rz31RZweX_WQwF9B9tcU23GuNFEVth1j7GuU3NOjoIPOIzIJEChy1kBpnKv_9dQoVWIcPwBvzpq3wYeBD6DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKmcWpUuncB3nhkCj2A6mdNs2LLWh5vkbrCq3b3kg_kjtzv2m1fH_m7-Eiu2PURqMEacmrYa0c1k08mU6nGSC-icwuIHON27q4rEuoeEF7DXuGPnjZZ6y2VP4617ZTopxP7JUJMlCMMksJdm8vMANnqTmrHHwUXkq-DqrW91WZdWbgibe0OLal-SM36mdI293_tmbXvppsSJ0yrET3yI0EKRfP94m8wgoY2_tOIT478QAFp-4XKIU0kPKWnzoFsa3PIB1mk9HmVRXXELy7-wSwbigyqJZe9Q_VE9FcqM_zeSXlvJdaNaShcPYmwswBUAJTLnh9s_AZAN21GTtYqTmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdQV9pA3YXDNyxSbz2oDsk2sVyfrnpYAdOOCFlix0frGYpIrRadLeA-BqD2lQTR_niYbr9ZR6DXb16DbdLYycjBO_6fGzC4VkMQwnCqVnv2E5XsIFBsbBhOOZS3WYUVWfW5eoO4g1rUcH9B0kN6Bap-pCmFy8ubsurj8MURqz-lb0qievJhIrT4cyYvrY3qFcYs0dHtk9yMbXgUaRq6Bj36H9oVLLxqIrt-5C45ibzeC7gEHveKnHf20QFDOMonGMCyy_XtQZYW2o40RfhQTyuJApqxee1bIZ5gJfUvDRunpmGtHidrPBD0F3G_Ue2dnOq-4FIrcCon19u-Us2sntw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P39kU2-BZ-nvq2dL5nXDqyurN4K02OABmg2m17yi8uelpZ4K_AuRDxbiJniXP5Hv_WTu4OGbwx1paCvcgrwkAl-Qu_yKCwaszR7Mb6NBX9A-5fwA0ndJ10TBrKWr4bjqNkqSju3DrC548gGMOl9O0wEJCthTiJ_Wvqt1JvdqiBN6cYBT04lTwdxC7rVA8oQFkcOFZLUSnnFmVhb8lqjb9saEhEs30V8dTZzbnxZtBf9nZFYqnmFBsD9OM0UoTk17JY8f4CLbs_1oGh_THvx0o2izJQsgD6nV1dq8r672CZs_NiO7PAr6KyZxhoozMKOnHw4TIfOiSVlp_p2wH8vy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmm5n2hr3Bd6xnpfZl_B-RjbAV09k3ukNSrZfFzJeb_EJ1eRB2AYw0g8D2955_BGF8ISDbuAPwZP-Lxpe-U7MCGI98kDvLPYJIJ6A7UtozuDjolryIqcNyajCkUPLLB1bD5OqtLbLtczOLDwMQBa3Zi354KtXiw_lDXGVYCDeMcPh3D8C2jNJKYO9Q79EJ8Qw4OMvQ8flcaUMeOjpdwzmxhyWHjOx_kHMdz4e5MIp4RkCG9El_X2xLCpzUmGr5UDnKxbM_dZxPc9TjD_l5yXClqbwmEJ0RWtKoVLCcE67rft-n--PiafaZyerpmKu_Mu6fq-Ke76Yr8IKKjBmj2AVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEOdRA_d-Ih4bfbUff_3nbA3W8XawTFPFA3vItpZR8-3rejASERxgSYK8gBcleRPXZOai7Y7gEFx62Jw4e3GhxdrJZXjb5N3LAlXcWl2kh2RDkTkYLdxwxfJFVidItqRX_mpz8Gf10oNZ34nWaYyU96S-8TmPYk3oSY2BbwbwUHK69lvI5Cvd260LfFI8QntoWcDzIN0ZMdD77NgV3FKWqxvcmSxwkXViSJpBXnPQWN8EOPvgE62SaW-7sTCABjUHvfApPznmtKRE3MZQGophmnMQcGsL3ofWicEGkKYEtsVi-5SxGddOH_dQni_9viDiAgwV5rwDyaus92SPcbNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJMVhagdUkeg_lBGftw1NUcQ9jvCDc9UGcU9UHD1Kkp0WvE-7bOmkEJyNpD8dkQY1UHFuK9c5OrIwTZfxt_Mc3_YJB7e1ZrPITWr8usfjjbKMG9S1lp5M7zEOJWVTwjtly2UI8tnieThLQ267xQZcE9ncTvL7tfkovhG88fbsRD-s_eEMVOQjcoPPuawkNDBvHjhwDnrcxaNwi9Z84AX2fCqdlfTKwG99PZydeyPpTHLo-in8Hj2kA-Ptq-BBMqiDv_7sHMTuwVHzuoVws5JOah5SEl_X9AjiiRNlNDAJlIo9-CJ7ZoCWwpz3DOfEqkKQHvPEo1X1AXHX8Jmy2c5dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV5oa5ylqP3_CpsqXsM2axCw68JcyegpPaLOjOjOBak1tXz4vqs26qA-ZHtzaUVKCRodovI7pNtTMXT4U50M0oTHUkoXBscpgnDEksLmKgUe9UUJeHhWqgGY8rTlUbqQIBFDX-dueiy7KBJa09uAJUNJq2RESRxcajsBST-P1yMFt5b0PcGJardU2jAPPmeNZohp-ZCVSlm138go2lDzuTenVznO7ZmPpM5XPjO3n4oZ5CE25zedvQF9OHOzDrGSMmE0CiOy7XYWxDQGm5LvQQX_5UtqgtyE_vt1mvwzxMCgbPbnV1VN0ugjaTC_agHMjVE--hQbm4-5DEYbzqMhNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0uOgMOUPbO89EfM_T6grkasIL4SK9tc2XR7FSigx-Y_7FEY_HLmwV-3K7e7k-hNad3AnpEjH75aj2JHaLOU-eWQo7o_wtKqsL7rhorajNwiK9q9q2ykmL6zk30y-ZXQpo7ZmdhjeYBuW0jEIjh3GYQ6ISSkBseWBnqTZwM9Bn1NNqWtBgTkIM-h68SgGKKEROXX0I5VWrDydpqPrkF8nPHd2k3oo-U4POMaTLeqVJbgksMKT9Mvj16ablQb_JyAJUErByuNU_oVGjdJWQ15VwF36eumIsg6TfawSBirUaV8ne1KhrhX50I2Rz_DwXzSg8Al2HBNi9lIxMGMcgCyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQdl-bgtAd6hZ-d5XZJwI9zXlfwVaEK8gRmLtXsJG3midN8viRRScwfwBZFnZ5rK-0gEeDkz56gZ3iKCLKRS8dKVFbHYZKcM_m4-FK0EQBwspjpIA96gdo1CCMuzL1v7SYq63mcmd_efcqQJqg6owggU2ed0oIhv1dHF5iRtR8lFgeKAn1nKG_XF5LQwsxZFc-AXHel0DQyfimHILIKSzGckQKExyfXA_n58v2LT_PeB83NVyAj7SF3L4w8yYZ5l3HUy8exIK5sxQESigaOCnzEqX0QyHgmOLLCU2yqx0UWO5_0EXg8fnZqIp55dIN7xDU8kfAxnQRu_Bt_Mi8Npjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjMXNZNj5O9gaJN0VjvQ60zAAIIOua3VclST7GIQxVO_vjgZsdPh6Un7RjKMhuqOtn9x9IfvkOIPuAkaYKgSOcsDuNFtK7y0a3Pq9JBuSX0dAXz9zVWtslqq5ZCSW9u5986w8bS7JFesPFbQBoFFcK6a54-yR8JKuQbzzy2AzAeKChBE-WNty11x9tTAfWzvzPqaTaNF5vLHQ2exI5ycS3gdf_s4ByKrmlhFnNk0m3w9ZyXv5r652tudli9jh_wFSMBnB0X4Be5I7kXYfRhtzO2etwoKK08H2A990oy1aXQL_rn2Y--IdVyUz_Z0Xd6O9Q1xEo5saP-LsDoA8P3O1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDb_FjiXvQEzpRbjRhh-i_ciFq8s4epgyjklgVX0j8jl9z3urkYn27H7eKLa407gF8Oa5zP-d-wrINySpGYcsv3bErbFvWLc5cZ8vD0lCNa5KNQkdy1saVgEA5nzsFXtZYzYhLA-iw36U8gqybq5UcxIFtTHNQvbiQ1DumbuelbUS6o3YIt_oYafeW5G-KRXZFs0V-wDafe4vlefj9LtzMusmQ1tb_5TfotZUpfqntoxRkHXnx9Xf3mawvj2PwfRUHuLMMd_CpGX-odhN6V7VmRUuk69CGTKXXNkUGDgR2KaCGKIi8sZRTEuRZY1vy2m3-mI4h4_d4GsISdtq7HNzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvmH8YoODfs7efYZRS5W7xpcE-NJ9bTkCeDIscH-42Zk_Ng1sHlp-caw5HSlkTEjHaE9SPSzh2p4SRFhkm5jgdlKyUUlSYqOfSpzSJOndoMNqpcjbK389JM1d4mqIsejFUhxnkcR5vv8z50aEqWKcDwBsMLx90GO80_G8IfWtrt5QUzLPPF2ROrZBP4Fesy8vakerQkrjicmX4XL8OWZrKJKQT6lsloSQgdBbdQI8tkzupVE7suXoiHE4u358WWa3NSJkrp41NG3QclP0VfSIp2V7DDT8W7S8v1YClKTydjplOnoHSueWwUHUN3FMEOGkn70RSPmDcrhkR0IY1BhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzcyGmLaov4egUWSd1EK02XepJlL03RDco6PZs-1HwKBpPI6o9F_lR41qDArtDhmu-j0J3NxBFGJdkfkS0lf5oqh107fF__aa9TxTWEKhCjRr1bBtT7GQRbiyqpZjhLkUiB93yCiLS9sJv_ZBzRqY2zSUASrTo0jBA60CP1Jrc3S1Zdrchj7JkcTDGqjd5Fv2PjvG_tDzUNYADmns0tEllVqnyUk8Odxt57gHlJO8eBH7bTvLj-lKB7dnd_U7rOH8kqPcrNYe-Z_31B0GUhnyxfo3s2u_MHRuCwuKw1wCQ2tkuzrQkFsCrhL68mkTGJhrCT0ZfSLQLnSdCpHG-Z58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYJ0w06ZlGYRhr2bxv1JmkoMo4srzEq7e1bZ5qyg7XSni8Joj8W2JWtyW54mcw3lJ-1iJY8cZWEMb5nkepc3bZtKU2Pzha27rGDNYVehCUnFRCA1yZL7MbLXYaLJ96RZHyMt3s_4k_9EYNSTFv2SYCsBeAoqboF_F6_Mz243UcxKJihpAq5pavL7eeD9nu9xCMaHSffo_m143V2KI31PiNaCVqv6DFPy_thRDptOi2WQOuXo3BeQQK3n64orw6N_ZLP4gQ9XqDBoQO7C1UdqvGwAAys1ny2arOiD5owCypeve961nmk97ItCo3pcnae6kE1WAFcdqQt9-pl0OMw_pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJOFKd7OoCn2j5hsSmgTCBcOctxwhXfOCUyZ21tIR_ASxSL7HnvXFlkiLnABpPVLU4abGCJwlExzqG50yRJPQij7C5_9J1mPPO5NjX2kyZ4aBoJKdCyjIOv_RuHB4VxE9VPxB8f47h8GIXarYnM8ByCHnnedUpiHEJRIEaRm6BzDTrpzcxkyMgigg9yq-Eg5aR4V2J6Od_-Z7DEzAlIFJ4LrSwhBeizGAB-DqIl5VTTevdYWwMFaxaHv5QZ8yw4x1UFtHt00VgeuTfB8jARlaHn1r7QpaBSy8OyJCyZ9B5ND99-hEe0JcttBNvlD2nWfzmoTAslZvk9mYzpUEzuohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRu-NqK7A6wzqHqRXg3rmvxWpCbOIV2-P8rpR4KEWYHB6C_BaEye6L1hcmx48Dz1p44i5h8yIanFZrHfiFOIf44kRZ-HBVGuOPgWRKMuZdLLTdd5J3xXBF1zJe4sMQNGh932-RDq2WtKT79Zg5YO1IgIOBLyGY0ERHKqJMa5QiNe_9H1C-Qe4jqPwDWkxj93-f81ncB_Qj8hef0Lln4FXx_cFw0t5DygcVclHhSnl1r2TcvaoVc3HnNsh0L4F3wugaPZigDaW_Q8AjePlk84AKqwfEcebyjImZ-VBzjQh9U448_IWa6iQmoAymLJTnSGUPKR_3DF9GaYVYmcLsQ9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBZHoqxhKZJ1JIPqKvYd30s6PZtDjZAabVRdz2_mBKdCllksJua9XaX33gbibvNuOVd6EFFu552qShAFH0FwhqjIxqnT7q7MRae70aafV2F8_huaWJnC6c9NSLr9KBw03VN3qA0Zzr_VWOq6xTF3bvVfVkTPkZfRrgnkcgJE-uQBKVRPQbleGOwHQBe4WmLItR7PWwoSnvgrxqP-g0U0yHpZSjv87dZVpEyUStlpXpHsjdS5BYCCYHQo0FbMF_Awlm3zbGbaB8yUu9SZyWAD8pSRWxTF9bYm9-Nu7usyhe4MIGOQ-7hA9k6UdWqfmXTOpm0ybGJAmwOqukjpGBtijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE68cgkxG5Sw3rEhoD--C-6sJBWNPU9vKwZk2GThdaC4iK6w8qQlNR4HiUfF1ewsHW6JdVwEOiiL1rlzpqd-UqH0wQJOrPfuGDrlEucqOmjlaeejrT3aqdWpXiLOA2JFbU33-5GNQMv2wdjY-sCYiZW7rK8OIG5NXoDrcwBkKB2mEgyHbEE6DzhSFa1l6hFmaGUPEyHF4uZUDR30k73uyHuKO6pYyV89kQnG-y-_yd8macMUDuPA76-3RzPVcnA8B6jpSXW1uRAVYG-2Qd-6VA_yJ0Ui692_aBbgtw2fOBSSS-iB4vEzLspkqV_19E_Y2gXt89jx1-v1wl_9g0ghlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMS1k8ih_AEezQaChS_N0qecn6U-aRIbwbUMU1S2HVDvD5MouIIEkMYBXryOzPcoDA7UhnQSB0Vw3fkonQqt0up5A35ROOO-n3obiPYMrqO4Wilst_DjijCwbKUlhITUXjAsEBxYdipf2FXriUfHSgC3jMtSF667fFpnkgpqanjlgO4bDAKmK3SvE22sPc71Olh7BC9flVIQfuMrsR2bXza3NaV6nh_jsSbxMyzdHvXARCDqW3MJlZgCCju7_uBjqUnnsuznLDT9W23udzWYZvX6zfetUuC7_patSqGH2l5H0sM4QzCZHcPoHtq97E1ukoZt4JzgZ0Zs9KbE3jMXLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc86e8rRcS9jxkoN61F2hXotFTq-o3OriuaqgqTH7z2PBxUhN7K1vEnoN2nZlEEdnxlxOQNLVNr6UwF5W6Hw0ybCIdTZsBTQzzm38IeNi9qogjTrkYveKDtJBOoVUGLVD9Rmvv886Ymi46FF4E7uTs70Rt0lWpzk7E_BBq8NYJ40kFnOeAC7R8gffjea8y7WnNatyvO5-fUE8h1o_jFd7AvU2AO7y3qGH0CPSHBkId0FgnY9HoMGp-4kHtdgob2d46l9XRTd1Rx5M9orKbPpanGMumd_flZ0SXBYNNf-lMlX0Po5Tto1tWqCN2WZkhYkPqGl46HMtOzyR0VGxdayQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZzoBkvpk4JEbC2QVCws-SFxqc9ugAmcmtK7MoFSySfRohBmluqSNnvImyHjk4SrFBqgWgBaaNgne1qLdKjxSLd2q9ks1lGnOZ3fbDwWqyBn4GWLfTCvv-CNZLXx4cDiNcm2ByR_tPFGoQUPRvf8MyiV9Ltv_pBDjl4VltMqMq1DyKqa_hJ5M_pOh3UsKhbBdyWjywLu5Wzu1ou9J_OWHbSyt6Hj0esPpsH5zxiwadwCCCiEB_1DoTOjiN38dcxG-eOvC6Mkz6rBgDbG2GNMinLO7FOph93K8ZKQWz_5ZVZVdfbVPU4dNuBbhX_RFA7JVX9hmF887oidGaVTTsfgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghy_enC79VS-7L00n--6e5RmINy9_pp-M01NAV8JARs0jJZzitgGsiLzhTLCE0-Lkmh30OcZOhuyLZicXGgJ8OutfI1kDUWjdAOsmyaT12CjcJMHkzWuvITLEka-Gf72uTl_AjezYqSXwNunt6z4d4qnqxrJtaT0CGGw0n_Lm8z0Qwum9zWTUvuuOmOmx8VWqhKD42Q0S31IhtH_6iQiDYjyxGGpVG9bXMNG4E80CA9E9pyHmPu_mXL1XtiKYXDPq4yjQ4aK3dIwlgrn7Q5R-maTBW1hD4xWmmEBs0aZNpo-pnv8G2LIoxMoRC8rDsnAduwDqjj1KKgNYdtgQiemWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJ5hTVah__soUZYzXOZ-wl_wtn80FF6mS_CkS_5IyY53FZeTIyAPXEVvrjj518OtBSzmlUMDO8j9eniGvbz5E0QQzT_riKbR03SyfcjmGaR7aGKE9awdnkZbe4ks_TVqsPN-tLl5Bon695TrnwHtL1TgDOMbaQYPwhVwBysypgEUzxyBvyMPHwgoEETXfSfYTTtAPH-C1c6YMu1V7m_luLobotNUYHDf258Ny58InY3SFWmZdOi4oNjxro_mvQJSQ_aFYqWhLHVEPaRtP7tWKgsOVKgbOVUb4GjChUZf2IlB2gPIpgBbkXCQ5tXOo9GiP3BHya1WH6vH0j2CPO7FJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmE8bDSsTmNQ7JLdRh4EihJHH5rqpOSbo4iBNqyjv5Fw8njJRncOIEVrmwzioqS7IvC75y_U2pYzT2nRyfOm78Tk1zwpUt1qXqzVSjBBFZCxcH1wk9sIedIWFWiTT_3M08PSXGisT6k8ouKa_JSNmXbx38sSPdiXt_mre6ldKi0lnaLpM5O4sk9OBCoMgBJh9QMGgSFKshwzNFMCfzrM0C0gFs2-RWySZbowZJIW4ZZbkW25lPk9HiqG66jgg5I8Cxc4BrQCA4rCBk6s86sgMicbAPp6P3xNmtfulSbewSJ4WQxJ3iean3jbwsIC3zZA3FmzhZRJVCtfeK1Ms5fPTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEZxSkJMy6WLo8NxrgqQWL2J5tAjHNu1uLhj5z665k99H9Fp4VaLJqxRXknBO_n8HGgLhbtV1IgUNA1Be7qOHUViG19yDE6i24byA52wGNlk9YADJkzGBlvZy5XNR5CVgF67gwFaOt9DaYMnU4zXkTf6ZS_D9iJOFv4TJzCmg9SYUg6WyuX5jc7xoQImyLIiBjRGMSCCWlE6-fjLe1imzMj15ig-91Ovfl3euSOeQQC3JuwMln53krOKkIdHlay7aDCd6R0DmnlrgFUpizC-6ezURW3ZAOhJ5zawk9FJV-Pz0I0DCmqkMaDGUHMXI4Q9BmEoPeinhxHUWP_5oLSbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_gr00ItcPIyCHmJs10kk6VcYrxyuw7YCfInHEP5I0jtgh9ictTB55h31_ogJOFCG3Sf9nLhMPKWbJlvLGEc2XQFS3iW8H-EKOWNaSiGcQrw_BDX7XhQtRgyp54iReuRpEdmcOFy2rH0NoRhEar_tApnXteJIawV-LnJjp46kIt0tiJ5x7gFCI-5G2M9LZmEO85uDRcIWkVVCo6VlX_uwc9K35P4I3y-Jcb-JHwmegH2OI8ccrcy9HPbhwhWlWw9qbNgcokU3EpDGPF-edfZWZMm283Y5bkCni9JHdBNSEA6dPPWXa8IJLh7wlQCHAM1r3vBmbXi7ZDew8aOjD9lVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaaAsBa9qQ4SPRbdDFYNWPvkvfuQpG8i6JyEeiFFHBcZMPG2IBqANjZPoxMLLQXh4ofCNDo2u9MEPBqT1DsuME41n0DRQu8dILUWyJR_i3A7i7LbHcrd4JmQKMMKzJBmGdt0Tzv5CH9jXy71CUtmqfJYtDaGVgI63Ttp53ASIIfnzwY3PjQyO-hutgt7gTz_f_gngZQA_M7bGMh7bXyfkbkM5hbiSfQ6CALvgi2_lnu82NBnc0KqIyFEq6Gcyy3OwWNIWRR8o_gyzZsT2pYG1lS4BUSy10lIA4DoB09jK19esO8EC7u_-vx85yJGRAUVL-pNGQreMwqdF2tYrwLRBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4NAKc_aGqiyBIDyejTl2lrJl7UZAnzkaSN-KCWcODHUw2-cyMnV8-gK1Mfukp9z0Veqo8Efu6Wginf9BMDXwuU66fhUtcArLxkDuzGRTUPNZZFSzqfSYkqiHRFZC16Qyt5cHY7dXwabh-2QXgRmTR0JIyAbwtbwMSvcvewHukmOjjO4b7dEnvgQrgfb1c-tpvzYusp9an06b7LYkWltr5suR1OeR4o3TZn29bU65frTSncAdGEDNm43S2zZJDCTZMBJkTYeKZ1hGT6vcGz8VwDPMhWjACEUfrNPyl4ELsYFtag2Mw2ULl-V7zL0zSZaRdRTZTxfiwarQAdjjpoF-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYj1YHgNNT3H0s0ohSL4s5sDR087CoDD_uelXdKkq-_eipxP3tt_bBKU6rWd13QpL6i8amo2OpbYwD5wwLvwnPtSkih6x21BkUmfgnGTx2YGvj9xU8swvWMfAkhAhtQwAOoLJfUd38pTCBRkW2EWFYiuGLMXGGBWvTmUq2QH8LWoXCe-V2GXySybM6bjP7WRox5_4hXOHMdS3_tAqWgkPplv-MnViwhyJNEzce2t8vXE0fPO3RAXgW2Fhece6HoXM2e23PIb-seb6tue9cRITQVlqRK2YyUZRGX8-0sHjDw_vwege3pkiSAP8R5g-_D4NhySDm8Y84rb2kJvkxVrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxIUzqsomUVG9aZXacCid_-3EQ61yIhGxFaDtmp0TdxLSEuhemdg9TgC4PuGb3Moz3C4J_k7Z5Qj3aNiJRIqNJXTZdXkxfBkwjwVNqY6mD3KQPiVKvdyY9ntMi65cjwrS9IDiWB2nmq5NDuZ8F999ax69I3s1vAqXe2iNXTpchEpS4woIDqD0PO38J9m3jqsG7lDZRlgxBh0tlG8cG-zePf2A_IXoIlNrw3OGq_kKuT8_VgKqi13IT0C43KVTUEh97m63LhC0betdTovwPNwzc3jbSzayA3kYwGODN4N2ywMx1V6UB5x9WxTxvx5Z7j7Hf5hZLK2mgqqIc0OFwzEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZj0UZqroqfGhevoL2Bh3Snq0gjYQaykURaGovqttTWGznJKQ5RWpGODf-kORH-V9C1pGGEBujC-xtn8bbNRbxdCUDTkQpMFqjR56VZ9_epRuBYph53ypfF6b16NVr0iqKC8oB16wlFSSJW0rgjOoXCbuEMF0lLznV-xPt7lE04oVXUX1lDHQecV_c83wj6i4JtBg0cHE-7StuTliAPHe83bVfDu3oxkRRQ828iauG_qf5D0jkeR9vXFch3FxHV-6JMXCOhNP1Cf6Nkudv9HcIFTAvsJkiggAKmzHh7rnt2MiGjwbQS10pIcdAbqVmTuZdeFZoOe6SY3wcq_fvaqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2vjbsaSQbL9rB8Eg8va1BvJ0kaDYpKIF7Yu44OjKFHUEx5W2WXjJsaPNQ23nw5F-CaYYuBtsvP9vYg5I7wHtUa3RU0BElDoJRpP8ZYsGLSl1IJyne-NL7OKYpzqrwCEKKZnK1V3Xq3aXTcLyvic2R8MTTrxCz-5TNAq-jJ_sQlbpinef1F42KlXujmt_hynQowoupIPaeKBQPU6jtfeAH1X1qn-D-3DIr8FuE-kNtOx1x2oFN56dP2C9Kb4QWXeQarwGl-E0K4FIOaXDbnviz2e-Sh1nOv-xnJNRCYxSexXjz0uHm7ToJnYBuV5TSoqmeMtbU8TuK2MuCPb4KYJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdpfYfLwkGiaWahUnR-4-TxnNEHVQrXjcyZYsd_45Q67q9TOEHRJ0ozaA7DBdmZrv5rGyP8xjSnnyoEvJd5TybWC5dJzcJI5gwx616IaoK3lkrB_GWiDsfakh4FM1TwhM73bETTOjxuK3lrPUR-ukU9IwWamOq_RJjc22V7_kDRVDSjk7SooapmDo68gfgUqUtz1NTlVue-ICuqYuVv9alnKfh2ryy4J9VjCUzHa_dzAfUX8RgsKhPeTvHapmi56ohVr3Ek6VZorQn0tMfaM3MroyFutpIzZw0mhuy-TalvLU_bgEc8IkAOpWJs1iUo3HKlY6PnoVk-DLd5AxtagSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr6Ae3GDjQzV9ZUIg0sVptef884p8lrOZqWUugPix81xT34gbF-BicG_ryHRQzjsrybBx75Cj5toSLnTgZCcSs7dNDARMdh0GL9ziQqkAu6WVa4LRFof6CU9Fp6dRKcMd8W-9sLbL5tCDHoRqqJGeHh2S__9mTvIXSaoHczSZShUpReTR06WS4-qFMcun6ugf4JnjQAAZ6QyRk8u7sX79xA7NCzam4KrKnQr5czyBAp7J956bDqWondd9c6XQsgnaNyZe7oOyeWxMOaoNyBzfkizWdpNbxLUost5toYQ5cE9fTsvRwL8SWnFwC7M8HhQL1UIMIJjNVg4z8_nWoZ4YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBGbJl1DkZHQv7pV9-wGWmPw3gX6XSYp1qiV8HKaZC72qOXLfW_Ajamn6aFNdqaFQiW2IsNGdC3kVP-wmpXuap2bFjG-qVWrAaqUEcwYe1y7-DNKWqJ_FjtWFyUCD5qF6LaDBnzhzSPIVrJU3oCPhQLmlb5vh2YNBzQhRdwTEl51gZieDEN7fOygKdp3Yw8m7uuQbkLm0jaFLBubqbLtnj8fyTjSCAFLZYbV7a2RTSdBrZ146Yk2F09vJ4gqrvRUT6XUDJiT1CTZDHd69CaUYT1c6N4CRla5Okqrc08FXrbR5GOgDrEpYTIjRjNc4a6JnyfSbtym8QPzCjPzHEi53w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTwJrbhOFfyjonEI6vtzNSKyPQo2zaNNinlB1Ks0g_xAQtDBDxqTMf5jMysLd_B4dZkSBCOOkTj58N-bq4wjFyb23GGZgL-ekYWKjY3sb7Pnqsku2oT3NPmFzda2jtxg-L7grZZfyfujC1oOR_2qg3IlzSYOr6e4ymlMBT89KcH5k4iO2cSaVLCsmAmeXIEHgz_pkR41M-6lB0Gxh9KpnE17hkV1frpIpfRu7OE-tdzQSza0HznFi8CiiDmmek0piZPe_7Cjl8lSNGgmeEx_9wSKY6pmvHwLg3xRm-g_mI2Twuc8NMbh4g4AxKTkrkeW4ZJvabeK9Y2z3kFvL125cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
