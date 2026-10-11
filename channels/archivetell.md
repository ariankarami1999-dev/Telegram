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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldI63klLVQHNFNS3MV845uKxzn2NZo-31-EhT50pLAdNW7jrxp8ra30XqnT3X5FYZQWZkGMKi6us2huUdhBrqxPN9g8F337ZkExtXRvuLJhxauZlxFoptETIasXTiUEY22_tTCWDUipFZnZLvWpGvDGDu3N6IfHbh8Qnq-HVRsvdTIIWlgDHDXJzoQaNeijcTDfwsbrA0mcg4AdE1pRcBjH-VxdpAiXuMKrwqmyzf-Q34xel-y0cxkVjt0Znw_WC_Y9HHItBCAF9ZKUVdIhhWofqVzUV4-S2Npc5bVzCI0AZjnQaBibHLIot1O9wFul0HPdH3_DpzvynSI84P7UPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اپ‌ Gander‌ برای باز کردن همهٔ فایل‌ها
⠀
‏اگه گوشیت ده تا اپ نصفه‌کاره برای باز کردن فایل داره، این یه اپ آفلاین همه‌کاره جای همشونه.
⭐️
⠀
‏• ده‌ها فرمت: ‏PDF‏، ‏Word‏، ‏Excel‏، ‏PowerPoint‏، عکس، ویدیو، صدا و زیپ
‏• بدون هیچ مجوزی کار می‌کنه؛ حتی دسترسی اینترنت هم نمی‌خواد
‏• حالت شب برای ‏PDF‏ و ‏Word‏، جست‌وجو داخل سند، ادامهٔ مطالعه از همون صفحه
‏• حجم فقط حدود ۵ مگابایت، روی اندروید ۸ به بالا
‌‏Gander‏ متن‌بازه (MIT) و همه‌چیز رو روی خود گوشی رندر می‌کنه. چون مجوز اینترنت نداره، از نظر فنی نمی‌تونه داده‌ای بفرسته بیرون؛ فایل زیپ رو هم بدون باز کردن، مثل یه پوشه نشون می‌ده.
⠀
‏
📌
ریپوی Gander در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 261 · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OupcgrjWgSUBWFR1b2vK4IiJe9KWzi64QuIHFz3RU1okPhFrIulxr32XOLZwj_nOu2nRW8pWRGZ88-x9C4VNcFs9BKILIvEVcon4bRD6WcwsHJDTavLwmGiEl2WC_iybBqVm-xyvd4CJcI0-oR3ZItI1_OZNRvZWyKgLllTbTA4HSFcjWYWo8XVRN59bnhF30a9XCgHLZfAe1VZTvey3sOjAg718xmU1TYAdHyrTfK7Da-qbTV6lVFgRhWI0QRhhrnKgZl09PaWdU2gECzGWwLTT70IZ7uWAg7WGpzMJbTox8BEBc_KZKWwNAU7UXPJoA-HOadK0JONdkdPsW88pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🐧
خالق لینوکس از هوش مصنوعی خوشش می‌آید
‏⠀
‏لینوس توروالدز می‌گوید برای کارهایی که در آن‌ها ضعیف است از هوش مصنوعی کمک می‌گیرد و برنامه‌نویسی را برایش لذت‌بخش‌تر کرده.
👾
‏⠀
‏در گفت‌وگوی اجلاس متن‌باز اروپا تعریف کرد که رابط پروژه‌ی سرگرمی پدال گیتارش را خودش نوشته بود ولی ظاهرش شبیه دهه‌ی هشتاد شده بود. خروجی اول هوش مصنوعی افتضاح بود؛ وقتی کد خودش را نشانش داد و گفت چه می‌خواهد، نتیجه بهتر شد.
‏هشدارش هم روشن است: برای کار واقعی و مهم باید خیلی مراقب بود. با این حال سبک کدنویسی با پرامپت را برای تازه‌کارها راه خوبی می‌داند تا لذت ساختن را بچشند و وارد برنامه‌نویسی شوند. این‌ها نقل گزارش گفت‌وگوی اوست، نه توصیه‌ی رسمی پروژه‌ی لینوکس.
‏⠀
‏
📌
گزارش گفت‌وگوی توروالدز
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8072">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/8072" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/8071" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRAtUiIJv2wtrFKIzqdSKLhAaiHE2mYjxFQdzqCzzGpeCEoEiKx4aior-8IqMMqh8EvEb_kef6zzOynNchJix_Vy4FK0OfoAvAoTSKwIIQb3OG8I765XvEF3rst-j5TVIb7neO7iPh3uC-LstY__PjKyRqmrugCOUvVepiWs7iGbe3N2lAEilsRLo_uoGHmgbla41GeIoEqLf6Whaog07rhIK7210lrda6rAEeCibpWmVe6wjcA-0IvmKfkymB91ygx7aeYg7T8u9iOHcVwAIpEOqGSkv7Mtgmp3Uuj2916hIJ-VV3uM7NbzUQoa0af0bbboYVdUnumGx81-uzzpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbkHuvhTA49mnbBw_DoOJoqDqdYuxeseNCDNDp_W7iOJfBoh_Pp1pjCE9gSYjM_7d-y3E0IBfpgNNbSOAa1rLTVge7qdicxjGk6JdyMqNGJlfdZweeP6QWsWfQj0uurdJnDGCDkVbnPH0QNbJS9PmQTroHe42tM71cafHVkArFxU20SZuHaccp9XQEYXM2s3gckIIrnh0vi1M4x-4kJzPXA-jITHjGiE11tsDS58bDQwsUZIMaGD3obXW3W180L-CnuY54UTZnSCDtoI_v-FnK0XCy420Ru-p7wBlLy4YS9r3FslY1cAORExv3LMuCTHESCWvp-PwlQlLjBlWDngcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝑹𝑨𝑺</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Game (1).html</div>
  <div class="tg-doc-extra">5.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/8063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6Qmw2053Or0ac7M-s8xrz4mPuACjH4LkonzekW6C4HZJgW3HTMRoJIxWqEcPSGtlU7Mw4NupcNGzFnv04dWqspx3pK0lPc1uaZvy5s6nWEkd9OaXXAQNxg9nkwdIbX2Y5vNtNICy8ngw5zdoEG3UDktl42vwlfW8ByJb_LRit_H7_6pcovmPW2ExtNF25Dn_sE2SgGHRv9hT31LCln6HT4v4ooeuBx3pDLzTSemxq8XO1gZ0UJPYjzYQXE0RVjFl9XvH8vRGvRBKXQTPgitU4HhZ5L14Pdu7ie2Z4dNkX6g-VXEd134alhXPuaknoJQzU2whVG_vkurCcxKKjH94w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=jjfEBQOMEVy2iVKd9qinqqCj7yEVrdUTYecwdngMP9oVoduJbfAJ7Q8ZUyw34enpYOyIttry9SKVkzF3UQJYtNH4sPC_tFT7wLJTkKFq_vEckZ01n5jgvgmWYLfCcEFiRg7DlU69fpMDUJUzC3dsVZX8wnHVMUnZfwayDW2U0eLKioS0KH_gwSd46YNKM-PbcHyhMN1EJI6WNlvIjB-2abHQJPeLvaZ2sX623xxru7A_BlKRO8_VrlLwHMk4FdW9yTSot9_EC1XLWEPy0yBCKIrnWuA1Vkh_B9NuUWJg3pzpqW9b6wTGl5IktODIf7cG867ADQ6P4ge4btByjY9NVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=jjfEBQOMEVy2iVKd9qinqqCj7yEVrdUTYecwdngMP9oVoduJbfAJ7Q8ZUyw34enpYOyIttry9SKVkzF3UQJYtNH4sPC_tFT7wLJTkKFq_vEckZ01n5jgvgmWYLfCcEFiRg7DlU69fpMDUJUzC3dsVZX8wnHVMUnZfwayDW2U0eLKioS0KH_gwSd46YNKM-PbcHyhMN1EJI6WNlvIjB-2abHQJPeLvaZ2sX623xxru7A_BlKRO8_VrlLwHMk4FdW9yTSot9_EC1XLWEPy0yBCKIrnWuA1Vkh_B9NuUWJg3pzpqW9b6wTGl5IktODIf7cG867ADQ6P4ge4btByjY9NVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txW095NnkJrZItGQW3yOCMFYVF0ORsglO893SSaJYF_CNTRa7Vc7arajD_yTLmc1GUzd5ByZ0spZVjS3nRnpUd2mxTk4N4sfyjeeAsi8JYDmkCvr8WpP1FQoD9fqHecLegaoVBBmTBU71RBKni9aUR5WKeWUK5rMWUm3waiNLYrye2OcHIs3yJyZwnRt6XhYCVsE9_fSzkq3z-RA-X4bY2R3qjgEY5Qv6x3gSERG1Sz5N16iazGkg-eqcyDckRZ407XoESihYxR-EXjqXayA3lfQtTCVADicyCIoI1yh2PQcNhE3fK_J2ql4JSowJ2gI1SN64nYClLMBBaObEnLDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKkacdSQRioUg02g8FttSSCs0BBSY-MTh_nUmrk0RW45_StJml7A_i9hPUy_N7pFJp8QHE_VSdajfE2vaBuX6hJkVtNMduEKtg-3SL9IsPU-J6yEdlaazhUQKe3HNUDQ9Hs-3ic0jmbqCJyXqEi6Fx7Xe8ysjaE1Ork-kzwik9jXEQOlyM_TO2O0t73z4WWiJxwP7Guet8hcUkE238w96-VKyCfksaLW5bujxrEUq6CE2dXtEFTvkoPqx2caSknjhT31qDx7AObH3bsCjQ-7O7AV3-CEHZqhl3sOJxjnY1BNknFWcAToHZDNf_payvLomgWD2UIlmJghUL8GMBV-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG6RMvWGCyetozzk5Km45rOprJ_2DwSH3BsNMCXVh2WawesXSIx9Xiss-Y0MElOkA_MxjEhhK6gEFCxS5TkuoW31uDmfGERD7tHZP_N_Lz_Askbd_0NpOTPE8FA5EEmgx9dXFtBhdIBJuVrzCNj4x2Dh8ffw58NyPldPkJ3caPagNkGGzIqTcwPBVeCUCZfJOMGwojnn3M8Cv3Exb4XDg4FMwHfWKC21feYA9FzLQsOGNLmaS9DMGKOIDTEWV7mDuJMJVKXgvGTlHfldCN1S0nXyc_reVE9YMvDFnOzoA-zxYgYSQOpWd4DDVJhlKZ8V-e6QL1iAvj4-Jw4rWH5GHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6bKHBxRIYFxTzTAmFLwgAaVLJlG88U-9TG3e27aRnn7TS8RFdDffy3gTxJ7JfyKs1tPAsizuCL52vz4zqLXKFgwSXue0INNA6SsY8LfYMs9PUYdyl2Do16fr1_OVNpWtNNQ91_bwuzjxp54mppf-cieT_LNz4H4o4yKBu9NpMDXFsRdbPivMI7I0wteqSuU49AJC7wqfAVC27gKOTPdpnvZrE7UVGw9lI1bL1lfTOyj134cOJTgEFJkPyEfdAtrVhW3lKHMSxKtWhbMEdcgT_E27ZaDOigka1xHl3bhvJ90gHpSALhnQnmN_Amymbm75lvQerZiILINSsmwIdkaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFRu9DoyNkDpvRLJLTZmkPj0SeKu9LeFCzIVBuu43cvlOW0WUYfpiUTp1rLLmZ78k9R2kxNThGYqdpmOTSR8zdje910gwEW6gmbislIV78vmbQMk465r3h3wSXYQOIEX3qS5UVlNgAMbeJR9PMvf22tVTOcpXhA71S3dG4RsHBYE9OUZcu5ffErDZnLpHl-MObznv1vXO6EEFEpPnEDg1pagljo_ft6xiD0rekWfwHHUQf2KCS4f-b6bdj-1HWawkm5jLV5mIt7JqRs35cQllM2zAJFmgTbMipTpDWtoYAHK2c1FhYmC495d4_rZG5-SAmZibJ_aic3aygm65jN4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=Ry0v1YjBebccCIw9G_y0YCEwOKvebyv4EB4RkF_3jvDCAnkTdoIcyQ3WqKcy6z9MVpfGVmB5YnXUC2KKp19gaxQ04LhFGarzR9rEBmu6uxaEi0ZyTSCwi5WYlnRoEjMMrD_08O9h_cBtT_Ow2SWbY6322EaN102r7I2Rkd2Plx3n-cH4W02xhgS9w9SYhs8sbTfSaSgNFcc15zSez_VqTNPD6WF02W1m6RD34jBkoISl44rlSW3oI5Ot0OImSSQsueDKMNqEpo62a6zrnwW6taWjnH_MIKaCqtoN3b79A4cjLXwMdaX2f-1e7xjFj45ER_i2Dca-CYrV8CBbi9YEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=Ry0v1YjBebccCIw9G_y0YCEwOKvebyv4EB4RkF_3jvDCAnkTdoIcyQ3WqKcy6z9MVpfGVmB5YnXUC2KKp19gaxQ04LhFGarzR9rEBmu6uxaEi0ZyTSCwi5WYlnRoEjMMrD_08O9h_cBtT_Ow2SWbY6322EaN102r7I2Rkd2Plx3n-cH4W02xhgS9w9SYhs8sbTfSaSgNFcc15zSez_VqTNPD6WF02W1m6RD34jBkoISl44rlSW3oI5Ot0OImSSQsueDKMNqEpo62a6zrnwW6taWjnH_MIKaCqtoN3b79A4cjLXwMdaX2f-1e7xjFj45ER_i2Dca-CYrV8CBbi9YEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As_nEKTanWwdwewzL2RrJNaMSN21hUcuxFO2SrzCsGQJwUIxHUWG5375f-6AFtCLnnAb41KxQAJu1KVLOv0LZvFKhR_UGrxL0vUI3Ho6E9z3xBo_1PXXURbqgLYNDk0XzuPAVpnw468hjGyuLrCqbNZDs0Qf_vPmhBtSWMQgamrC8X9JeJL-ML8yhGR1um8Q9qZoFyFge8RyKUXv-FD0bWu1K9s4Q-fKS4CUR7D9Ma-XZf8_NEdgXpHCzGyoqob0H9up5teKqTXrmd2p27gJdwgP9-3v8033QZqHArwoYmflwjwHvKrgLAlE0IBQt3gcAFQrrIDOxAoE4cOmuEGLXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyWyxHGiKZDpTcKy4nfIVeoAkRiMuERpMO8bD-XB6rAnZPi-oaTvLWc-TQUER6mPKbqbhScZp1H41uhNCz82c4SoHZJVDdQ3FQeFYoDXZ7wHJC1sOrMx8TpmtlPeJsZONDWw6SwZ9CEcz7hc_CaVmCHjARaZMGSYvxyPsSgJYDEE6FS5jlVrl-pN9HnGDJNqK7hWul_6ClNqN_C9lSQ2x421WTqQA0v51LbAV60pojIBtbTY_J0IxeouMelxwQX0xeRRVRsFb43OHhwJpMluL_TUwHnLGJv7l2SeYKfLhkLMymmDy46AlNz3vojiwDai50Y6FCYPxiBJbE3NbGl3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUx68fGkCEE-FN8Tium5NUtMm95JRxkG7tU0yw2jTIu9kEHeFbSr3TROw6TE0Myno4iQ0Z1pu8ruj2EBIuT2gcWV6CCJsKRT1TMXamqsbwA7weDuSSxpXCglsKxDd8TAGuqNhib8FhBOtTzVSIldpI4UQ5mJhUIkFoS-5trRr4CLMdqf_y8A8_iP6psPuitflEfuH1jUUXoQJpjyJHuAhEoaB7jzbmHdh74MDyzB_HYDiJ2uwF3Oy3kgN8GIv36bIcySZ9NJvyJUBtR5UwFZeb23_UhDZP6ATLwRcPXPOUIgK564i5mCcEkEilaPfrQVxYpJXnFi3eDklIDZ4U_3Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=NqzuJuEUyTAm8SiF4IA1aoo2EP-1gzbH2OD1kxHEgD5ibIwOo4avBvW3-NCPlKh6qfUKm-M0gjsPZcGFJnaRm5L5BF93J8GI5wOeMiBQWHGtXwjMhgVkxmOZNGHy5au8YKKOpllb5VsbgW6Z6Dm7mi_DJ_MwwoCXzp2Cx8siuVVEtUFMu0mJJaARk7tcBbC9UnlypL4kOcJPHr-17bVG8YIcKWHHkGbLyPEw5WVCkWLgAcodLDIhRFaortkNNGA6vn9tUMc3Bt5Skesg_P-3LZAd5eodJlNWP_TouS3OukR0W5r5KLPIUETpqvRdlWxCaBOzJ9YRm_RcTKgOd3Yb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=NqzuJuEUyTAm8SiF4IA1aoo2EP-1gzbH2OD1kxHEgD5ibIwOo4avBvW3-NCPlKh6qfUKm-M0gjsPZcGFJnaRm5L5BF93J8GI5wOeMiBQWHGtXwjMhgVkxmOZNGHy5au8YKKOpllb5VsbgW6Z6Dm7mi_DJ_MwwoCXzp2Cx8siuVVEtUFMu0mJJaARk7tcBbC9UnlypL4kOcJPHr-17bVG8YIcKWHHkGbLyPEw5WVCkWLgAcodLDIhRFaortkNNGA6vn9tUMc3Bt5Skesg_P-3LZAd5eodJlNWP_TouS3OukR0W5r5KLPIUETpqvRdlWxCaBOzJ9YRm_RcTKgOd3Yb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nypYWryHor4Ml4u7SVDZ_I3PBDGu0Rl-njrBsYL0qdD4uhuZpbXR4AjsW8qw5x3_1FJ-r-r1aJ159Jmv1hgWM_qbDbpQgAPRdczV85oAlFXZ6CPXtCt7ErDLFw3F2UFsDcrYO3yKyVwyKujqWy0uqZjduZKUTWCs2lohVuyb7ll7CIZBea58zC2iG2t_M11kX23bCRDyim5B2Nlsn49DVtc5yzLDRM0sWxMQWJYRCioNLpogA3NoqUg8YQNnMspW7NLvK4ASFGXdf9z8REfbhwgflBvXQ5K6LfZ7dod2tM5Mz4ITEUWSZKJNVHZmIMv0Qfxg12cL_EHbEQN0XgwyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iicCmDI-h_7j3xSVd1CJok7b2IUb26nWusiYNmZUAJBaMHDQ01D1OYKvxcVV8nQ8Vwxs2DntP2rILGf57QqnPRy8lbTQPdRaE69lrTggXSRTZEnvVo8OGt_I8qEsoqiGI3ztJsup72WRxyPT5yTLmaGX04X8BX-qlj582xpnEcj7yve404UZNK1RsFeJJJ4byz_YUoXCFi6dzV2l3JptfzhlVUFkTBUJs1RaU4sb33eOk1b4GgnIlw-REiWq4ydZfX3OKuD7QhzYLJVY4ugSEDQQRxFaWiPFKPTU2mX59NAKwrZQg_B4VxEUpMdeARzWX7v1fcHNeF6WCW0bQ3sCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G60UVvmbERkTYB0_ivi1bZldqw6JaJeg-HaDYrxFxLuR7B18B1v-dYQQINVfkWCEXdcgB_iTzfV6R8Q2LqqUSJmV0G6hNMzqVp0PRdmDm9xEAH4_wEZ_g6PcuQGd4cTg0CTmALAGwTmJi-knIDmnTS6e_l2Pc8kBbkjeltif94_OFBI9mVbK19V9RvqfzCYzp-UodcvViiTPDL4Ik8hpoF7dcK4z-NUNvgFWxNDwyZiQ8tFNvhmAusebkgCb5wMzLUyDKZl3P1l56b5JtDzNMGkkUJVY5ej7ZylryVBdNrdcS5KjG68eUrfgnJ9M-RP6rXN_HjNllcTSgCADtTrcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVNbxFoMjAcqs6fDScPU9StXr1o-eeW4bG1DRQOc3l-n27uL93AVA0P10FdA0kURK9ropzv_oxJqaiW_SrLbio9c109QELyAfrYr4joTVyosA2XaFCRbya5AiT1Oo1Zu-_IVnq-udcbsnZaEqJLyf6mblc3aHWO8wxkqjmzApgpUPYYfTMYUIAxYlgj6wooysuPssqQ0ARcPfEP8NH35-_5aPHGoUMUPHapDTzmZVNCUOnpWlecDLcDTqwcn33ZxNnwpEPtbCYL4MAR0XwwXdJYG1Gs5Y0UU1XZeo0pFR8inNdn9yJo_oL-Qb_9lOg4S5nCox3q872cD-JAWkDEopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YO5w5d2Q8TBEpCAd6sQZ6hNXdarNDt8UNmKvVebLHeJqR4dF6bdN3ir7gFJ_EDk-GXzTZQSu9UZaxzEnKkXvBxv3R31bYbRwGKPUhQz-rl3dw3hxjCrN7oFQPtXgKlyeGxmKBtTpISUaV8ZLEAhibTNpTkRh1GJa4xo3ZGRw619z9-YSGTLeV2956hgfqxccOy4kFazcZTSPb5IHFC3EPGslTRYMFp9gUfA4gkx9n-aEP7pmsrl8SlX2t2x4SEAE3c-r6qRUO2t0xDCptH9ErRDRZ4R2sBh98gojmHwTMZB8GqfvxkUERby-guUSBPlWgir2U8wria9OsVawO2KmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJmcnrAbaoHjSRxtSqmqT7W-HI_EPw954KqsWbQ8cZ76c7kmzUjQBu_YoSNkwLTP3groOJDzpRdrqK1cIMC_xjJiu9cKCZ09dtnzMGNW_VKy84-f57poROtNhq8lVVi0G6ckhMiasIp9kDmYveWiaSi6NkvYasPESKhS4Zd0dsNsM9L7YECEzIqoKsv-ZUOr-9GfeqQbmekMFCKj05XzhLTcX5KcAJJhuXX4WakmhocjqOqmIp3EshySfEo0lQEczIyxvfMloeB8anhTAiIoCxgAZ1oShg2p9359PQbyvoqOHHipomXuQ-xl8BGJ0iRW_uNdphUuwyXE07NijfexEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlHHqjcEgG_NLgqHye7decpFmlBqAYT6GcqXvDIZaL1z_cis6WVOajl6tJ32WegRoole0Pwi_h7Juzw7PXT1CW7Eqg9y07-jBN_NCUuna3C5IgSgzbtoPMLvk3V1nwcnb3ajC7Nr3V18ZMkCla7HnObFUPFvxCQY9OQMu02zguhUuf2SmJeSNL-EH-NOT1Cav-ZADBEcpLFGMVJrZ5-COhMoCeTlEr1BVahk90BQj_KMS_Rm10NmTUKDmoAKRckLohzGPS9y3xfprSBlM7ew0JXQsiHaQGm8ClJfJI46Spz75Eet_ZLteAbNumxT82fr3YaQ1NAwNhwzUNjGb3zhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSe8MI3fK7eL34Qcy3SiFJzjL0BOzSVpj9zhGim3FQK7zQNmZFk0Y3V0su4NwjOT789RxaLSw4mZHttZkh6DdAuL1fFS0Cx60YLJmp-a2qIkT4CgZMp4CzEl3IAXXRiBY4cgmDevnE2VIy624fZDxMNV-bzdqyVVwoNoItxeKjXgvM_iy6W2JViUD-7eUjSrWmHnMP-sTBCleDhpsNAabIwTSC0NLQJYaQczGXFD83o5Y2RV7setpxLdjbhXYoT3lepSGYgnhOHCT9_knTzhJyOxZmUKm9Av0wSgveDaa2ZJhyRWngX6ZpXSqroREaf5ZFuX4DJRibn_f-J9Bq0TIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r33iqmXrNYUkb0Y2DlMnlBJrmHGWqIGZtV7I_WVXcm097nvg_bbQxARW0XUQNRZKrcqh1tDgwxOfARYaAdDP56mBjgEgVwo7dJ28HY2h79dXFq0H65pPj8b2h_p4gF6WtOjVkDn8jLaFBmsDgpLrgM-wYGHw3wyHxal12yEZhed0fwKGFiQPRvlfidqXQQyfj_xT8XCxzmVGcUkubmywprpLkz7nWXguZmFpDjmgpnVit-3j2QXF0UsOMt36H13vUEQZ87q65D2Cd_jGCdX2uTNwLeL7RDMXAJhDSd0KCWS-NqNJW8toWwr17jxOfTOkaCHjtEepAEUlLfmLKE-wKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKx6xgYG4oN9OKnd1p8nvSi5KvpVSDJTPIUxu5nMk0siOcZ5Oqi5ltyFUYAAz_1dNxh91V5BoxguW_pqQMuctS3YeH2G0kGbp1GBmzjiCMjdVYy1KgmYnpsmt_mFFhRWvPt_CYAchaS4xm4Cu1tT3RwD1lKCGfXKF973tL3rvdx7KXCUWnEyPluRMVpvg5wzLApXtQPoefIuPXoKYYRT_VhdsZ5w7ooQ_QaK51cSHZC4FPoAlcIxAwqzKxtRFO6xRKJ2lH0KSO-RNtuysUnWnCr5CFeX8TkIIEEGWTvlnKA29wEWzhAifhUEW_xCxsoknlImLAyDbe6ARGnqBxcITQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E63jEX-8jjtDYucYsqcjfGOM9kNw7-N7EEbKcI0UBhA-PUW3G-UYRGN8lB6KU0fShVTsy3kJ0Tz1tbM5f9nS-Wif1c43RGGMHu008C16WVMUoSacQDSkYuR1XNv5FcbvNeiYljC9YLBTUYynAB2ydwszuC_rxJaAY_GMZyWu_JBRwh-BvS9yqDgOxFcDcuB-9kOReAx_XRiO2B-67Bo_PlqmYjCnaaWzPqg8A8AQZlCc93cJ29U6SAVGizzP4D9HhTxowwvlwhKkxEEG0AqUMOpMK72u2DKqHGRvgPN7FsH3gcy7FwVQLDqDDusypqF4ecJdC5P4Yt83WIrhLUB7yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8-gX5TBnAJNjvVLFFleyLkeb686N8NuGS2u5AygvD4AcWFUG6K3o5hITT8ENmYnFNpUUN5Mi58r8KZ2S5v8y_nMwYjbDeVG0JMbA8dY29_3H4lVMYnuGFTI4OnxQGhY4EZmZNMxgby_cag5WOdeZmN71Ia94jegp3Z4iDDbRK-Es_ptNmvqXpqReIDxso3OOr9LFmHw5Q2PPoGmBdp6IqiPbaqJjrRchEpiq-n4f87V0pgVdh4TB4Ng4QSeZrUBwwcJa9Po1hp8AY97eJSrgCZ_PzMwvwi5Bd07sJcgfj_9rWz5BkFd-0irNXTQfdbD_5r-sM6ef_Qc8Wpzs5jg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKCqfG4Lc3dgQcw80K7g_qEeC10IkgZFYd-TFGzibTfh9kCRiANf0N_mRMdCBG7RbMknY29-hR8p3ycQ8HOGkAAcaO4XIyB17dGcpfEViAlOTm57jt-V8TpkxWmx0p2oTgs0xIZAdXrFP1UizMTy5AfL255yLynXHNqXPeewV-mfzYBbp_zXKkV9rh2wmA-w_-pFg_oCukOc2ovj3z7VvpbjNv7vcR32a7d_8h0nLaFEMH8yM5INQa6PYKwERR_N_F_Qr8nXTDAQJflLH1TsyMD-k9kajfVwMtm-eWJHGFOKK6Hn1JACStvEl3BQkcUeVJfrRZmVtK8sGvfPcD7YoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVlKmaITf7d6k4WLcbvsVf-QtyvrIQ2BIs2OVsDbZxIfqpU4RT2O3tTpBigjyViR3L6bi2Z63xrXKbAUS5OlFXtvVo2WTU1w2n9oDW6ZmWUMOBuVt_vFXIgnEItL3AYs-ENz0LvgjDmA3nln2ozXu2JA6C2WGuUcER_gtniMf-VcEhwAJDmzGA4DUl8lJhsNnn0w2QmlRZjoxfbOhco_1jpC79lWFtjIwkndjKhMTHtqqVvZ4Ly8yn3uln1NdchnaKt6vNW0TwyaBv47tCDDXR9oZx0cXlUozn_RPojJJ5e5s7wPPJlw9UPHrrXnWUqEH8WqI1HKGhzPCVwLuUTowA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=HXS1inuAUH4u3EgKayM_mfnTfiaTHsiF5SuVSkVPFHN7zz9AfAH088_PBoakjHUGhEwMcXSG8sxEiTDn7DJrJhI9iO3wadkNZZ2kb53jdG4q7oFTYuVao_1XT2IOJRL3RCjgJKiiztd5i0poTPu2sNtlo9YgCZuJ_lzawszrgSmcIxQpvZzQZTAALpiiqNiF1OEge0rO9p9EMCw4kM89-qg7O0AN-wrNvu6y99ueSq7xzmGJvrYiMs-VYPNNQVZcO9nDHjGCQs3LuO-1b8ynMZhomucYQPYz_7CtsVA_KUa1-9wHJ-MHqRyF6xAxPgm3u7nW35F0CjUiXK7Vwn1VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=HXS1inuAUH4u3EgKayM_mfnTfiaTHsiF5SuVSkVPFHN7zz9AfAH088_PBoakjHUGhEwMcXSG8sxEiTDn7DJrJhI9iO3wadkNZZ2kb53jdG4q7oFTYuVao_1XT2IOJRL3RCjgJKiiztd5i0poTPu2sNtlo9YgCZuJ_lzawszrgSmcIxQpvZzQZTAALpiiqNiF1OEge0rO9p9EMCw4kM89-qg7O0AN-wrNvu6y99ueSq7xzmGJvrYiMs-VYPNNQVZcO9nDHjGCQs3LuO-1b8ynMZhomucYQPYz_7CtsVA_KUa1-9wHJ-MHqRyF6xAxPgm3u7nW35F0CjUiXK7Vwn1VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHD4P3N-NLm2v6mUI_kR3s1A2XrBfYojKG7K2l1hqehczUa-b3kU-38HcKch3q8gOIJKPCC4Sidq2MkByGyASqPUoRspSlWL8uOaCndv9iWyrr8MR9ZgpfKi3x_M5HcWxFXSbxU9vmq31vox6TJ1GwDitHKLQTrNxc0iRClIM7C4AyHLJ36yerjJ849TqSpdlznuoaZ5WF2_t_TgOgmGkAnh9scPY7Pvp0edYhcTWOTZPBEAQGg-Q0AKpO9fjuR-x4t9aKM0bgWd12h248-lRVRuM_1nz5YwkvN9UugknuY2umxvK8bXrPRHtLwdps9BpaPEp6bfqyx83y9OU1eMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/js_7PREQhXnwa9PWIPtvXIzVOcaDk8lPGcliShAZHkwwtVVwoeX8_6ZLtMHBvitbDB4aSwY-5tOxFux31vVBIBybQQM3zH7TOk164H1xX6jtRYQVlubzbTlrcztxgM87wdNryQ_6ijqWPR_I7iptRdgwBBCyFM2rDixg4ikWalos-GwkSjVQw2dDC3QsnIEpIRh15deey0m47VErMVFGCIVkjGwjipAZm5atUTWPXgA52knN6X5-IJwrMrbIl63S0vRpHDB5JLqRiFIPVnRnGUD_o_02TnRfXnt40VHYgZZAkzHs7aqS1jtNtowu9XLWtxoXiIjQ8SqaVsONlUmpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wa38vDz5N5AzU0qdmErGZB29eUB-yQJZs3kkeWN5TRAVRVeOM_i7irGzOU6NbBnu-pOUXS3mtBGs325zCdP3hvolIFmndOcw3suusZ17ajSnqfUMx9OvzRozYDRuOpKhS5de24SkiichDsbsg9N00rj1ePHdXBobGM6PTu55suLypRIGOljIp0ZEOY1MFM6fC1VSQUrBlNh3_ljLEQDU4_vpnIWzppbyKUevrVG3QD0mGHHTYAPGNSNbBwyRg_Zah-t4rkTp2WjJRlsh9uCuwOSddQ0wXAxtLg345tZ5rgxp1x0g9EU1g89N8c_DR0GWt45-T2GLy3A7iLrKmx1cnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_TCzDcLp_mZkPzTgI31M8cXB_RsGbW8Ae7amL09TnN6X9be1TCHfLejS2IEIW79c3SqSyOGfFyJd6dIA3v7k_A63d-hLebYJink0Wofyv-OwD0F4DGO-igbcLZdZwArLqUFl29eTGm76lrT46CcpvZd03urHh62eSMf9pQI8zUtsx99ue96WoF7ogxvHLwvZ9y4R6hzG_noNDzm7qCk8RrRI5mk6hC_CURLAIUs2ucI-1bHZUUutvGWySuEGBOwtNFz1t_SSjFsFJ3ecxB68WtRDh9HCIfxwpphTyosNFfLk6H8DgAPb2avkqniCl2Znf2Zkyv5_cJvFhddDx9kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iB_OntVFSkbOnBbtviYasO-tH4F5i2Ycm_8bNZNunCTn0A9ARFLsSkCjI4P9lMe1r95DX-AoMDEJH5xU9MKNsRTLYX_iyH0faDMBlCTu1gaH629iYL0wJn-scQLhLmsQt5ECT7o0XDSU6hu0iP69-jNY9iETjLHlc9qv7-Poa3mDyH-779NqSEhTXOOYe8z7u2vcqZ_1kkNp3TxA1ulLBDn8T5W4-eq0dDNVPRDsyet-ZsZTJY7v_jAWDu7u8H4RdpIOPmFl_3jToM-uQ3bOm8eZnOYHRZ_wvQR-TMHks8LxXlCxDk3RflzHQQKnUU1-0c3usibGNoVFmpdQyvTAZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puX7xTe3SLPnyOQLrlWIwdqh7cu90sCXHg8Rcte7dabanWwIEh6PEmCEHwTjWzVJA_h2eyYdtGXwKmHZJ2Nl8gWiJ_tDIoNz0M5Qy29H_8dQx5kFC3EwajQn67uaL6UnllnHdeUTLeJPN4f3KnfJiJgcEjLCSM3Mr0GaMK1D6qdTWht5cQtvrb_yVhVDppLyuuj_lbCy6BuT_z-epGGpM1D_JhN6IUDffITXfzlp8CCVcwyN8NEQbB6nKEC2qrMHqXdBZZKBemqrIRsZgCRFMbCByMR9uU2fuU2MxfaH05rRW83R9QjbSbKSiHDmW2rBS4-OTPwhTldXYW2IpU0pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U9yGe7_zH58g2lwlTzf8WLZzYRrVvCqEik6ok2Ta34e5075I2gZzXLVNxZIkQ5p8GV-pe4m25DtyX1XsBaIzXu3F-g964s3L7Pd_RUgW-2y9x5_uisdYxVC3kvYHbbJcow9HerclsyS0n19aO6uh93rhDwNwpkm4vyfQ_9O6DH1TAczH4squj7P7jzW4yDHanudYAjSPBEerRF_pxHqDTbfNqdU5LtTDHbE9Z9GXCWnKaUlaBC55ZXu9wL2xsTKe-mShGKypYJWYWL6FllaC_62keoTA1O8WLVaHuMPcJZ-Tps7lWK52qIpLzW-mRAwDzcqhMtiC8ICr3g_BAoInIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y0Ve7ZX8YCmGPHJKeZKqG66mXD4-o1tNKGQZwvEebJYaXl7mYTMcrT7CcYpnFsBHQvzk4AiYQGnnqJoittulszb1lbketaLjx-umgUU4Sd9Dm9GLyz29fdZcJFyM2htQDSOnyHC83o3uins6orcQPkwM2dkL9byxvPicenGzhodgZvhJrqaMVAPb4U_SeByH0sNT-erDVIcJM_jCrUMqBrTcM1aEpbDi2a4lA4Jw8OTd28StMaIVEhqk0RUCAAPpQ2A-cCrUVx9U82JlxFSfx2Kny_5ZTvPW8ex80d08tJo-FKHLLbwVY_ha-jxLz4XMGMOBGax6CESbsu2doeRXLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4J22mBJtV0SUhtOqa46qjx9g4vBvQ__rCDNR0ViLC3TYwpNYSShmFyC-LpLsvsbAAagMM6rnLkbpy2OQhnx6EPNGG1Q5bnw78WWF48YfjIE-v-5sL_2SNDh7iitlQzzX6nuzm4c1keEjPc24vs-dfD5NnRxjYoX6kv2LqwVKjlzlQyLckpJH2kO26YpMc8c6L0FnDG0u7fLpbHGDdeqmUMRf3sm3gZn503xuw68HNqg4XbPuY60s5ONNiVsPPJZgzWGY8LZuAZ5n0j2Exupgi3JY0BlSHQpYj-PnsTtwHsjMzvP6Vs0VruwNjtW6uI-hO7N1AwjITMI5QwdrYpEbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDHa0ea7MQFP1HlugUDLUYEKs-3l6b4iEySD4Dv-irXSaesdF3vcoShrXDfuwlmKbFKhF-lP427SLR-TzzsTTyyJ9ljf-daP9w_1GvwwjrlgbYgKL0SbLb-v9Vu_6zpJ0yJthJttV9e7whn3I5i2nZGy56prfvFli_P0N_hgthSN_W4awhClMiLq7Oo9ltfnErLoWWPlLV6ciZagQ--ewyGP7qnnY6nQLEH-7aypB8CUE7De7lHlMQ5V4lQrZZs9dVsbjDOSzospQ8MpEVgBUH5SVLOMQO1CrUBmT2JzyZkQ1-Mk16GSg7AyMrFZ5PVcxOv-rJx6T49Miv8JsTo5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3kzHHrQspskMm0A3RnP_hFc5JXEQ1IQ7-RlLQvLu7jh1_mfzifuFXRFFhCveVPqqtrtitYlYJJeOJ81VJrcUgCpJt5SyqHfv78SomPhbiWLpSUr35a-iBvm96YUoQp3DNmBFJkfJWWs8anHXIhPe8TpBhdI-CkGnVFmtAmgrGPahkHfn26LueRExVCPlUBP94DwvNl2D_9An91QwNqII9bb9e7xUGxCjOmEBcucpbXSCeSB4yvvB5b7uW3aIQ_Zk46NWvh_7V2sbn6b9xS8h0Jjw_kZyMD_tDiCKmDt_Us8BNh4KO9t8clhG5GsO_DO-rraj0zn1codWkfckepcUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA-7fUGwLqiZ3voIkLTIr_L4NsUpyo82U1u5t7YqHdqi4TreNt-YqstpWDY1OX-fqbX_gP_7OHtgwlnU6d3s3aWGvV78BQATEqz6lPUcovJ1MCLCn0gY4ZOAvKsqCyhvKCHUziAAoJoQBp1ZCd7Vjo7fuNThpnBvb7ALMqrPIFDfmS2jufsqmPU3SwnHrvVjnplItld6s8BEXKM2tq6uUabo7PUxdFS_biZIDonBiHzuEoaePe9i3kYKYHczWAMUXrY6NAFGuiP4teewnzSye1nuf0mZxRJnmKFSnvWaAlKrh4XodnyUzaqE0yjwdB4xdGobCTWIgR35n98_Q09DkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlSksxBL6HK4obmErqoWoQZeKRIAiLlUC1uZGbFj34Inab7t9Ld0VBW8P9S4JZFb_htZAzA3TJW-8a4h14zsNQIV-aeOk7NAxMzS7DINxVpGd209GnnAKTEZXK-hdC6joI9dQWdvj6h9iE5n0OZw22j_R6B58RN-vm5_xg5jJ6rkTsK_hCinABJIIk5cxD9_QsJH--rfxoDgPewPznuR0ckAOT597dlqcwbO-lSKyt8BC-PU_WfAUoF5vZ3zBzPFGwuGpq7VltvF8GZrHIGquY67spNkmgFY1qtxhQRkLloRFG5ZQJquJNebBflkOL7e2TkrUsDvV0_-V12-LarQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXdQNU9B1hsRwhO0xWU5DCq3zECl9s7dTY7O7ubOdBRzEtEac-lbe-zX4klZ-ZT4gCEI_LjtSxpJ33vtvFUQiSwxNprJe8yY89fhtk8k7Gq53ifoqMMUI46HR2TeG0gzwLgR1S5TxZQd4oVEdTkdtWCDaTxodc8r5uDm4GElEPgq1D3bkjdnKhkXn8CcCVSDV4q37KNB1b_mrNFjtyVColBQ1RjlZy6Natpd-zH56eWqDcG0JcSDXMwdsPtyBE1qRMwttLkJXEpBISuLinmtpVuho3V9ACNJecgwcRof5jFEeD0z0La_RMLpVMMN61D1N3DT4SGRl9bB2a_zIx2ENw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRvw8r_O9UB6X7TJ8EwohpqWdaqVEoiQL6KlV2xRuKw5XOthKxsbvzzaTKfiTQtKID2xqGlAObq6E5oksHgPeASP9Z5BykZsRCMRk9p9T07g0VAqv58J4w5D7TJtxD_MtC9BXXdwMjpMc5zUr83IhT3r8LfRxoIXhIK03Epyjr2tXlWruREXcWl0yOGZ98cUulL3p4TbFbYyurpASCBgFZqsHEuaFBsvlXTji5tjhad9Zt2LgsvXNxHGaaTRGZmGll9bzvuKsK80E7AidpflTZFT0th-vl0dhhvf1WdxxTs0uz9o9LqvCvLjpdbx3K6advLpAd8yVZpLTLYp_t6bbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSddV75OM6Lr5PoTC0v_gK881wDwf1W-9ssXC21_dtCBuU5CH-6U-n1VvsRYBDqrxeKz2EQixF5u0eqf-aoxWdVsoC2ecRDU0U6ABXIppnEalJeoCLsBcKK0HSZbyC46mPfB3KWrvyT_W4t2AwNxHkGyDJy7-xWB30_b5kBF6YlCyUQ4fFRIpOkfKuY2M7HLg8iMjKs3f9vMT_dV7MKMD4nfiah6_5XrgR5HmmLa9ybIFpqDMIO0-LvVTs_MlA7FH2PMvUXWNxsTsJn0mmAFgDNQP17Zc5ZddtPYGJ0I_CU4ctc4sfcFf49gADpYqRGwgmmPzD6ge2yXdaC4XJqkKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovCT1u-ABjWx7POTgLzrPLPy7gywDd-YH-erJM15vngUlelTcuQvNmOQ5Cgj4qgmmfpv4ApzGaaZMx4-xn4t6zL4yaqNKI7iLepX-nVNft5pJoqN0nKhAZDZoNv1OmMKvC4_hbHIsUBT_VDyE-NajoVLzJLHvP4i_oK7FKSqFgEHDyZm39j1q5qu2DpUWlGZc3e2o4Wm60Yi4LRgo3Rnu-kOzUkg5d_vVqjY27FgLKo9grL6KxEOjnW1mQjDb-OcNic4NksM0x9x_v7Sedh0BlMIhfrAc2BUY0oVCODV4p9KGJ3yiuk9YpAwcLwklOs10_Sk4kylkBl3qX3a9oStrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRnp1CsD-JoB-wugW9qlJbij6NbZYfFfoa0DKOV6iArV2k2miRgGHb_v8Kt32xwp4NMbTpmek9YkZNtg6VDE-K8ox2MoGp47cLph25KZGwuQGguLS0CliIh5kTTVtoRYXFoL_KUyqah1ckCz3Oy9k94V-KA2bHW-VSAVXcRvVKjxuQNERipTD6P5b9fIUAgr_ucSyxesJ8YOWFDR2ro0ali_qs4PVSO_qIqX73RgKdASSNpbWUC9h1f71G2Gz0wQ_foiBmPBK_HpXY4WE2ryCxprkbz6dAXBGpL2NSdrzmZG7By9CZ47Z_QQAGVhDA7k5r6RWygqcOJOx6_l88J4Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igpWiPCbuYNTWyDRaBgKvHZgAcWZmY1K5NwGGxfUAv2isuIhXrnfR-g8MvD7ttfn0QyqXcoXGXdNRLsvjh-FfeLbWEqWmEdeJFmoG0ufx35QH9KUOxsY5296SmzUrcWIPv-hES_qGm4c3qt4uBXeezn4wpRbGThc9oDBweZ9Z-j37OdckcLoIXdPlC6EYGLi8ZK7bW96yl1eF6dNh_DyviVF8_7F2qplvp0D2iTNxWHNpGQJ0SJsTh3Br3e5D6_UhDGqi1izCwqqInBEWAdWY9IiT23N6i7WC4umezT8MqPAR_VgkPsMKpt1MPggMbCBaYCqshWWssaXmoVJSxNUxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ULaKU755123KMQGDvzjYue-qpxD9ScnIkeVdTdpx1p2NIqvfisDB89jHXCSJcb2cfet1llg-2vmYUptnoHQlU8d0V6PGO5hSqVzbB_uOAEtkn-Jh0xrL99RdKLmIi62lUHlxWFEilA9W5X-YMH2A3_BtM4azUxC-v4EgChoCb4QuYoXtJLyIwCH2j40k5-D94_PY5TKuJVT54LH2Jr4FEWxIPEs7nzTrs6fh4e_oz1wpkSkvhabhrt4uOkmuM3SkRcpk99p_vgYXJSuWKdJSM7yR2RJnktTol24xWhiZXkwJS8p7v7hQbJ4K8gaEbf6oaeBjIvsyckCU-FeiuKQb7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dt7FYsW-tCYqdjXmy4Iz633EJlG6YY-WVTZ_aiwxc9iE8IosLeDGq-QDw7o-jWm14m0qD8m1KrLg6R7DbxegWDcsmcq7BMVVcg7kqCozJ_ba1RzPP_k-twOCndCJ5ZkrfgYyh1jO66t3KS3gA6hazNhwRVxa0D2glJP-5ag4zblACsKfV9_HOPZnWYWNtTdYdoDCZjNYDRoM3UKaVD0ZTM_jXsJzpfvAyD7NcAG1Wu92-TVUTEwgnBfaxCUSOrZ_O3yitRCXBKW_8yqEjSlpZPZ26g-aeweeauIUQZM7cI0MtXez9Z1kAEHFm1d3xmXIV8GzgnSGboxSgxgOav_h7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgFWgoxVWfHe3ogG0XE4WIXoYPMaNqvWVHh1boXFzO_qd0lnvyYc5rSulgzUNpp4n-QFFMYGLLIU797hAT3d0mvfVNaEZnCE5aNZiTlqkosHEh3isoPrqIXtTm_O2bvpVaLMbmJJOWSdj0mGwhTpNN4XobZC-3RBlYD9T5w-fX5m5VZiyfGQg0K57kXm675Eh9ymsLfk1CjvPxDQ2cyWh6Pu5GiRN8NuMmhJ8P0vLxe09uUS0fE7xRMq9mrg4Uh1A-3vFuF38fTGAFr6xmrWVYzry8Qgyre1MBfxYVoqLlMM3j5jTD9MIU-jxYoBNfXcHqspsB9GP0jRg4nPWAx1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Qbp7gLtgfovt9zm6R_RyAWUp5concsyt5pHP9fF3qLA5B9uRznQRdJZcmHqIOlPem1HCfUWdEYStUjNnpPQSvttk0AHwj5TunFyDJvdoJ1Vbrx7TLs9ENjj3ecJdckx9rvhnskuqU6mIwtXV1kNo5trGhc9gVdOx2sGIu74X73B2KWqd8r8Qg4CsNDosnUkuxAIlEtFRt_W2Is5v3jdQWzsrbW2JoWqu7niaj2dvfRuVww0hT7lu0UluvdUUF0pi0XuUpoMo40ey-Se_dDYX2rk-1dmEt49fIwuK0f0xYhwyc97R9gcd-hduDeqdunnPGaI9MBaIi1OmwgjXEPrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krI813TTp4Uqx6zxHG06Z3Pv42wkDH5WFgaUp7W7nvNSzcNPTsXrK4_dDpZLfgzr4xyxS7ZW5p-aExEgQofli4oSnsXxjegeEfFjZXca1eVmObUxtB2boNGVxYbb0fMgE9RP-xhGfwqRQfUCvoszomM59ARVFxcC6hM7TAPjyYPD9i_MH6C2WhFl-mw-4xZNxmL_UeMdcAlEv-MvWYRn9C5jMi9C-wfIi5lNXYbjan_Pf8iTpgzjhPtq2DFQxDngWHPXxPtV24syUjQccJHGyrxKEDRU730_6lFkLH2SdrEa-TWOrqEYW3iyEiSbFFibrv9dCHmUt4M2FSPrG11pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQPcko4Xv9RTKw4Fm8VwZdQ2cSuWYdv2K2iTFBYuw_g-TrFcFmdVrOEegclo3mWhCml26jKBlpSIgdO8CS__kcHYK9ZRizzeySbBjOMpFnK1zkvK6vbkZpRIzvka3uP6JeGFEFGO5iBPbmOLn_aII4frhsaN6HXLn7fKF4HKGxlnk45eoyhzEbHHM36sPQ1iC97UCZno0j7w0m4l9qc4TjiycwygXen3o6WJMXUEi06nRoKqxW2YF4fxlhQRhmGZa0RuB_aQiwEkYD3WqSyUZIhB5WWBdSDw-i-3oPeoM1t-OcSvXWAHKOe2olbA6R6D3RryGmB7cZthu_72mP2iMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7Fn9ClKSdNlPXCyXbfoLLcnK9EqCl9mLJUNSk6nLcJoffM6KHrG14Plin1lxsSVzwfEOs2HH8EgmYvN2bM-0LlOE43-QqRN9qMozHeJVcHahsdXfw4XfSyic8bxQLi6bzVJ9Ti5s-3FFYQAXCcBFkZmylubledQFw0FF9mXUpeYCnHRWURn8Qjn76E7XOjFe4yY2vx30-rbTe2LBVwxqFmE2M5yktAYMNwrQAVL0pMKTOn8-NuqCNr-nd5ouFnAaq_vVlM7H-ZNC_fmipQbOZD7sCY5a8kKtbkTAx21golBhIofz8MJZ6o7PpRJvA7ig-wDmuBo7-5rUtrGsZ3RmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raqW7rDubdiGiwAbNHn633QokElCYOWvM8U0COiVs3QOfYhIhsHnWlwe0nbBDWG6C6Y3-rndeYZ2XJEOZwgEv-q9AHB0Esxz68BhnNOeTtHNOOQAPLjvAuQrQbcJk0bgnKLQqTzHAm4UYMS4fwkv1Q7lzRs7Ll-DidlVl2BcxfRakeqPlEW4N8O1CPinblwtpv3Nw748B_FP2wECpZgr2FGxB-SDJU88BvmWjlCnD2OaOzBk5J0JEc7AyNI2ivzZEKcJ3m6VzJLNcsgXnFPVuSrxYB8kC_hC63RS-M5UYUCDXWhq_fhLUsDd79qJJJlk81prY6aLAdSZchvOfHBavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umQQtyrFCL-nr3W9lDNt2z3jRAo3yDWfIoMWTfQhmbFW5n5kUaVDr6c4f6fbCqq8qPn4yPODScUFswGYD_qXEgFDX2n_KciV_rraHEFW3NqxPCRypolCyoO5BuGiRSfklUZZgSc7YDiD1VxfEtKeixBENZC8M2GR8cLWR7PNmQ07lkVEyDkKh_u-0_FKXBEh9aZWDDgQ2wXiCn4WasDvob1oZ-OzCeLlToDkQgflmfcE5c1hE6vLpw8cqjPaV5d4MqVbH6fDCKF3fK-sZVoCwnSRM8j_ytwhHPuqILVSEBxCFuExxS3VXfTil7yUW5ffE2ySN7xVMZXHfSNvm_W4Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rINfLa5NSvzOosr8SykNJymp4biDZ_wkYQkLKW3HoeQhHOHBM6GSewVnqBe1exjuf9zq24g7bYMazQT9MV4gUwp8nNSBnFj6fcKC_sMn_ieglmDg15Kfior3EKTIxCyy7bucwa4vg7cqiKRQvuHS0Nq1KtRfLFNAntLyReWAgcDWJ2BXa4fj1y_w8dJOi5yo9tBa7Aw_8H7pN__l7hBxZEY1VqfPadF7HcDWCAdjNrACt2Wi4HmSW-QPEYWrK0rypDsXN3Zs5tYJNVukAMV-xEr63AHmtgALCu1yVozZcbV4ocSX50ZrLZe1YiowP5fndUTrX_RlIPdg4yA2Rxi77w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sjtjms57opbNvZaV0mNyODeZb1zeyFTQbt5w7v0GubxSmaJtFO1azOoSVF0grFXgkhK_CBkPpl5Rm37CFVycbE1cixeIyVEjpGECQuU7jFUiGmcNUDhUJpsgrKayKki8JdA_68JAO0gB6xzaGK0dKxI9JuamVfF-VlTpmqJpEW8ym_2MvIxMyxhYYbax2RBIQ0kSMp0SIzEgqksrSAMrmPl1u7GC_nxyyg_ULnDDHuOCKrYWH_pEhvllT6eea-eKVwj1VnlLbL5nU5Ntl8-0AMDbkDY-DpPTZog1Rdyzi-kQnmbmJDDZX_F3YSp2XBxSqLR1HR7rpzx6LYyAj-Ajmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViaCN-ad5r6GbwiMyg1eIRdo93Cn_N-t-KqeSfNUtiGGHXjoPjQjXuVa0COVse0o5Yo3ZBOrGvquNhZGeqgEEC8s-3c6LvqonJMt1UK6qEIIljQPx-CSCCOmc1ovWnZdHYZ4FTEAEXazz0Gq8h-0Bf-L_L3nBD-mUOJlk-COyJO9sCr1RGnYaIilhtKa3Xye8rcrU5rYwQIV5ra7xYQTBdXIjcUEyyJ6AejafALI3szDhK2WyWNEtM096HzKsNmOzwvIh_EQ6j6np8wRXHfkav2wv_oEzSPmPy7EYq-f1oAyfxd5vGC-XKoyNIcJFaKDHeK3YxTyQiyO3OcTNDfdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWFUQSZ_k-huveRH_sgE8O2eNqdW3zylMxRaFNjiR4tUMSfb26jY4haTkFh8FjVtuBTw-_Z2HS91kLQcNPEpJlTPf8_8L7YBgUzv3-lukZ4v0wZoSTqaT3Nlm-8EPxbnvBGH1y9fD8oMN1MHV70kWXoBKgEPrueaU9S7yA5nepW1UxClgkkEa-q2xWEUGx9N9XESOZ3Ca1fZwXXyvrxuAwUk45SyqFyFgJKNqcHjYoPxlh0mBGXsMvpDGiDNK5N-MOySLypHYrXpWiTbt2nxzyywpT9cFf5IBFra45A4OTOd387Oc4zHV5Qn8Q8GqlDpuQK2Bq2iplGUCvbDd_mPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alGMzZaz-CMsbLMqx_EfQlonk59cWhmDR-BxScKQtKbfuALYJpBBW8uuKw_HkpMmz4lpehjfPMvFetX0cuimr2l3rR8fgSIOiG240Aw1Vx-JVpuiNfA9bx1MhKHqtlNLgfyctGZZuyJywj53-iD8LkGk6jXp0D2qzvTUUTJi4ZJQaViZUCdXpQokD8U23ppyXwFrA0xGJ4hmkZfGHs8N-TXGpJputtV5jdyLwZzZ8jlfe5UV64ayPR3XCjZJrUGOd85-sMKzxQxTEssE8bMMNNccbovyOrc0SM9otcKN3n4YmYSpmE6-uSvLVq2-ZzLGN5oUdDMRbSUsDWTmpXtA5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUqsXm_qPUCDmI2I1PFAavR7dzjszl_hSex192rqGX663wWqwsX1yI34YQA1vJn4oR3z7QywZqBO02uQi-UC6ASZirT2Eem7UDYXvjYVFNzqCDj7n_6TJIo5n6Uw1k-9z89cQwa8dLq5WMnJPx5wFlckhJNsk2dcbnIjvX8iFrV85rv9KsUdmcbG1NZ7gjIfrtXikrtqmXUNSte45fL-zy4B53V7Y2_hg7I8lsFIzzbUCBgYbeV44mmFki2y_9kUgRRIZzk018EVPkBTFGgLv6UqYl1H_AUWCijNwMV-KyF_GtlkkrL2X34qrbIqiH8-pJueuKFnmvACHQzbhtzteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7ULcaAUgbTqrIwcKdRJTuDEsH68N0TXRo1Thq0A5TwhpQFA_hPTf-PYtH0Jc6C_Cjo_jT9-0ML5Pz8XokZ-L0o65nU_CnepmJpX_nT_q2egfezdArM-9sLeK5dzufuibOouBFSdgn1BKekNoIclP-aS31r_Xwg48Sg0KnbtgpI2A-OK60FHCpNOhdqN1aTqabj8zyytUR-nuo2GceMXW4emUNxBPWGY7MFMJqR9sexpVcVhoGSTpOM2Ef5_HoVEeyDYN4rR7uXazelHDZB7nUCL1CLTz-JwaXqzC9HnAJCcD3D7r7Y3RbbNjkbe4ryyi1rr1hkXA_ae4d6lajuSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwcwtTE6W2aGT95QMZoOV7zE1C6WntUmQx0VpeLsDQMOWjdALeZI1WZLbnLpNE7q4HV3tTpY2vW7W6lWGKn1PUVDCsA_1asR7fVLYweEmeypv6iR37tg7xYRiwyNjxrZgjr7kDfpMaSSw-Ic0fkHViMw4UUlyLqAUX04boE8WqPDM-tEl2a3RwN59uWmiC3FPujKaV30OnRNkEiU2jkO-ghlk241RnUwvbv-Qmy1RYjsZBBnOihOENdbiMSHMk70K_nI6cLrMdtqvNszcdpNkxjKKr4dwH3PhyvvziT0JJmMhRtCMPf3uvZl2qIuzSI4wF077jTjaowcchIuj5gFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nje4tzCVBGvzs1tUl0uMAE2LeQciJeKFQiAYMFk-bylxIQOMqCFNJ9z48E6xz8xi33WqQVdoJkh0f_Av9D0XX6GA2OelqrLfhvzACTODNKpE4L0Oj8bMMRs_t7pUN0mbwBvUk61-3wLLgQAQmlj-oSoCAbwwlLE0XLh5Ss54KBfuoXNLKK7FscocqWF_2QE4dXjfN2WDfXuud3ap8hWvGXbXv_z4Is0Cm9sQs3IcSNFMlsXADbO1cElqe3P9D7i4gT1bedAITrp6EgUzTIx3uio5_fPuE-vUdGf_aT2tnNvvYlBDVYNp9vMqQDH8xBLQtdNQiKAQAwq6vyqdtTkFlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOsNuSUQWARVvpksMmCYno1BrjLUdsKCGdu_mgRxRwrH66NpH6taajUw7gvCCtXYJpsi6JordT5fHALB4crI2k5X4_G8c8vregmFO5hJEAFVbjnzH1GzynPhec-MvjNTHz9UmPUK6KVLRrSgkPv_GS5x9Wok4_-agUUuektgEJdUcDLIIIKYJIGdJFfy-0U9ssFSBJyWWq-HRYGNDVBCdMOc9De3PDBjv1Qop1nFpaWF37yGgfRypvtFOfov5Tx6ZiCacJRilwOpSaESq6ikU9ZzIShD6k8kz5YanbxiV9lv16G2jIPqAn7Wk627Da8eSTKfCrApXb87Y3WyA6TBAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXPaZY_hcrTujgrKV6RjJlXY_pSK6Gu_VXavX787yAW-c84ojSEpqhoPwOJQETJfE7mpxpz0xi6VRUMj3SySUmENy8XLhIZ_DnlNFrmWWuptSxd397VUepWuWPV1YKQZha7H5h6vYUD3kpV2A0vEPExT9yepQUCm6_aPvNJWDI13vp1Syn5zPYrkdqwX9aNw5higcMExIZsUkFpT0gikDc0M7MZ5aZfNfkIYyddDEMegPYQcEhOs81-rMe7dhdmg4vHAfoDaYrMWTLB-d_9lVXGa4HJUWa73DbQkK2ut6ER9_qk5JPgrOP9EyOhurOFg6Ak7Syxk6bHc_vWXbdwQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkscCZm1kOYrTaza7I1Bn4tQ2IBWzRYG-oCY5bt9CT8ZWIQQe3zjQyd6hkpr7NBSkkyCPhuHEKu29WlzgoMZNpniGzuZN9COV0PxzdEpDIEPTsPpEL7FSUCI2H7hEGR64jO3sZa8lejJkA47qQATF7Yhe_4xGZTUFJmMZ000-sQShkZ5UjZLLbCR4rxEAjA_sCOz2BvN8JS2ZIcs1BKMdJ2M9jeydRm2hidKKWKHuKAlCbA9xsti2ympdh2Yxmuhe25RaHpRwkumgvd6p9I0nj4E9Ry3sErCugUPyZZqYLf8IRpv1ThOutktBX6zO0Py8xN5Hr4GVHKFlKc3Rtej3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WINUKJKtLuwTW2LhE6o5P0TrN-VImksExM2IGLAElR8W-NS-5K5aKVihH_0j8gefT0cy49vm-E4F1WrJeJz96WyQyboCM-zBOKhLdgMuiP7nf0zf144YdVVc4bvsExUyP6p-xtgO_8NpyjjSR5gkX-HFt-cPIFLpoU1wNfouSIFxovjj0-N2vYXP4WG2PVv40AayDtFYLJyWmZ9UcSVES2pRVHXyQ4BVgtUOOgXFbo74QtnRj6GLyQFdjT821bKfq96EzjqlU98Z1ajgrrUJ2SldmDIw1AcRTlSO-GN0pLJfxuPqvyvbtbkTlNMg3Kj5qLp-EqlmbrocuF5CflIUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZO8U9ITP_ry-fKOAyPeiU7eKfygJZK0CoGtibSafKn1vSrks0cdBLmJSJc2dRjgOav9ZYkU0g0MmpShbpZu6Fk5jhr0YX0RvdT40kUildkmA3nZ5fbCu8VNCGWCQTkS8N9AOVsLwWffhU2FMme0gr2rs9fhU7FCf2gF6ciLqfzXA51nhQYhss1cl8lDAUWz20hckiso7LKQy8J6FFbYkT-YlYrdThMo6Gc5Fx_4QUDxFfIG892hfloNSWsidyvWhNjRH6v-4NGkWGlJKxL8N0ryDAFPrtSwh886WssBGHds7NvMJuC_bM3hFqWxbCpk3Gf7e_TX80F3BzKx2fiSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uit-7PApzNvy0PEqTusoXV_ospy2nka1ekIkiCXzRO8EoGdTndBA6jPV2_wnNIRW_a9q3Ll5PKTsaGqKujeI2PMpF0NCAqdI6QRiLgZwIgPASFFjcDqZauavat9hZsVa5FyNfu87NSpxyEK6kNhHBx4NjqXiWyM91vGZBHiv4WL_YUqXzAIxVKVqRvyqUDneHa5_Yw2DGfHQT4IKpd__MygczDKFG7PjZVi4PhJCgYB5nKZOORpJJkPBV7a_HSzY5b4VNh96xwKJqPFO9GLQb1dY0Idh-nnzha4_QzTITNLpS5qHkI91_aeJ5kVOe5FhUFNpCVqP6x1bwVGmrgZxTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9EkGj3JjQ7cilNi36rdZKLk-NiQV_8dFsm7kKUs0JhTawzmfnGppUZtFH_P4XOojIaEslJaB6TrDpMvHMPlXaMLM5O3vtKmL70XD-MQk5fwT2JTuFDkU0rULwipK_X9xtkqQf3MLD2jcMS9qN7U_0iNJAmcDMx8aIYr7u5YWOXw3WkZfOCfkoUiQrys29Oh2ttfl-b2hSESMDphOManiCWQ-xulnjfsZT8cj2njxNDUGRpz_StTx_yRNBIZ3SkQNVS79QB7MLi80D2DJw97kku9Ef9RBrcBp5h5h8h7vYGMgfVpv-3odJ70TrSU0172iSpY7bB8xnhGYgJXDFCNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTvQjIGbT8XNRQGwEsMssFyOk8G5ckebZ1WyFOxqlsSfPj08_IuGAi2WuRypkYPhW-WT-ynpL4lVyX53YZ7LPIg_uCLy4nntpIbmc3LvTfWiNATIfgVdrKjZJBxvrWWcTq9enopyXBXiL2_KwbE7szFRTSYVZy7fH9rKbFp7BeF9rdS3jBledTPecLcAv9xjKHpqAUnocHtPaHyTV9eUoGA7yQXLxZp5GHTBZyCgzf-trDAxLt3_rhypilPBvNhRAF4PfL2lWMS2tlnQCAcP9vjRZTbOwFwKEce5j8-aAi3F0p7HYXuRw0P_-1xWT8BxAOGXePQVVFby3O3PrcPYvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKslWQ1i-Dk8HcRIIfiWWwIHdt-6agbz8Ds7cVrbcCS9NI45BZHAHkZs9m2AByK_fBxaMnZU1G7XvTJmyMEGamQS5rTU6GxVglQ30imuMAj9kOF5Bk95fref_P3Kyejf_TvN796SbuJUXjImD4oOWoElRdOPtnfVSbkL43spE3Lb6MzZ6pSj5tcjnnN6SXY6d_VsxpkhT6IQuSB66HjQo4B2Stue3E_5w_4bBVZgfo5t_XkZENo8UC36yTXVJldWymutwC59Cg5u3iFKAw5dFnUb9wGdaNJ1Yyb2lQA8Eu4GXzmVCm0A-2dBmOFgpAR0HyQJetHNQrQFiG9asQjpQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgHMFvahyIzCNcR_pL_oDA5TDFJDhVK-J8hXWWKbmvQWbwbJrndRMCCVtgouYKTAIDIMVQU3uhwyNu-sRKJOJwMPybnsa6SMtnj1R5FM0ZiEp4xPrXgT2m9xr5D3Zdf7pGonxoFso0vg406AgYZZcfq4wOGcJvnKxjFCOm_bJAEyeL1d2zGEMydOUZt5TlxdpB6NbQzljzKWgECLAMf_MiZNw91nU9JXfCE84n7pBMrT9y9-W1q1kjNWzquLvwyOzY-jtF91ud-n_mEmChQj93yYQKc0nCr3b9qMUmArDq50dDSkiuWSlbyNKxjv38UKxt1otJck-xwgRf9zZZV_wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQjc4ONR1PYOXu9ByVpFa82xbbVjmX-ETfZAjZpM2LftSIz_Rov6Cyu5k5jO1TXvdNMmMFm_nMO76PSVjPMxqu6olGuQKOqt0u3y4yMRiXfdBhCuN7Azxliy2j7gVCtaKbHjV8nR0mPYBTfAR1Ky_hTfQsYymmwDIf_N-5Zn6g2oyRKzlGes5e39x_WXge6DjPZD1w6_kHoZB1aeefW1j3kkZCt5HlFFlm4dw2bihYHD7ku-qHwl15Tmy48NT4MvSJZFmUM1xyV74JkBCg_Orbk2C24I_Mo21kiXm31CDI6V_F9iWOuh5eNfYJtor4p-EjvmVaiv3XrbyVMSZAZ5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBwBsZaIQ8uhpcu0C-9oCQRL6It4lmIEe7G9hQvxrgntv_swTL2HLDDCYeUI1jDeXgq99mvai6yUbi9fHwHK4VHqzGYsVtdF3woygkz_PKwxAn-Un1R_7YKrJiuDwr2WOAvjAp3qq_g8r5J7ljkADpepGVShO7i91oMAP1B_amo2_VpmBGcu3ZvgotavdNJRUiAEyh_mvXY11ZA_gzX5lA9eFKNlmYL9G2eJvdm0HPGXg0-Y6WvhuFxESup23tgUvcc_cBPTXOmW-tA4A8hEQqvATrmIrbi1qPrvER6vScp__5GPNoQFGtcDfdEQwHHZG0u0uiZwK_Ao1eyV1dlJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1PFY7qiv8Ihuo2ou1LBdacFzYhQzbxWDXWtudY32SHrdRFQMrSeo8Jpnm-40FeiD34dX5t-5VXQVtnHQHnJf6rhvLNe88SdfzkTPfXCfvLiboAkUe18qLskoqfzNjWTXiL7AaV05h7VbPCENQu90Lg6KanmnDI5OhuqrRN3q32pXc0ZMBibKiKSqRpOxPb0YN2R_qRIKpBFFJGziRqjXiEzwSIKzFe3BdIx38aC2so84jTswMb3maeROBaYDQ3ARs445S_bSZx5Diy_oVw8TX1S5QBLVVrYV8p1GUXVaWIZ_ybm0b89Lydpg1f0tvZi17oQuJLYBb6Qeyu2ww8gXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9aATqa4wy17YpJy8xSNn5FNN5-ur1WSgfucsLJoHNXqsqOIBZSL5GHExyPfMXstIt-ABHWpzPIunNpDH9FtZlnq66uOoIc1xkqs9lIlDYUZzArQAgsxFu6QaKyxeWmlAlR1VRIvGIJbKAq7OVYa-HKY4SkSooHr6u-9SmCe5KS0wYMxGrqa88dQ90G7ZQq4H5YmVA6jZADlFnoRVRtgbi7aYTN0DzUo721LEhjNWNFTZI0GBhG50v0HSNJ9OBX2gmuX5zokxgo1DdhJvzt7TQA43h2yi36P1S-M1w4upgjvujaLAi9r6dsGOXhPOcdsczmyTPbv-EYCmGz9FitP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQowwC7gC50woeEYG5Oy_C0LEZrYKMNmwKPcQNrEtyMXrbafa0IWgcNogARUkKTgQcfO2cW78jgqXIr1oSv_u7b9W_ubYXDMkPj3G6fv7SxLk-w9kRI6tSi8i0drwvYF6pFnS_NwWoujUNNPKx1Z2rmLGruC-Nme2CfPZ6HnFQ-g2qjdyjI02l0A3EqGDfSSylzoflThfgJP7qfTC_f9imS2WFnPfulBSKZezyWRjiaQtXtD_61obhIgLMzPl--jlrhYH6gDuti058XuCUC4wMQCtjTi2HnQhpLMH9orrfHoUE8G_2pGUvHpXIuJcs23pxOaJGRxZNQ4ePxJacuX0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3atKsVvsyxiXfv60WBUu1NyJxwQvpiFtNciIUI6SMs07osrgD64LJ2kWi-GU_nnssJRj_VbrSxV4Vg8tkGg8_5j7syc6svvDFrYlsNwpQp2JyRUgxSH_5_2ZYNmx1c9O5fIITAur3TTBbGhbzEIl62drimQ5FzBnSt5L6t6X1y1yiUfcW5e7wstoa_goqENCRKGeRz1zrGsInGaKW7AGi79jkOrr1Es9mLQM8dg6IAVSCA9AKXLz-cS0IvLTvxkpb1l6h2oOohMO-9_p3Q3DHWxM9UF1YLOCPcKYvxN34gyP46ibOmYPKGEbHeamyoFPO31SUKo8YEHuEllbKk7MA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
