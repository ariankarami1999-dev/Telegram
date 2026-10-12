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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
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
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/8072" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/8071" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nQcRPXmfHUEasTt9dreG4OkoyioskEgg4LzflJoZHpQKtaD1-zcXknltcc3RxPsYni4qHohLZ7vRg-OuV4b3H4iSn6gcKv3xcPkUQvMuNJ7-CGpS1yUplqNiqfSLeFPP3qw7lZySonr2sbOF_W44bByuKxxgfdPXQORhNwB3qTs1RBNNJ2FYy9P89DkdSXGvhaFyEhXVt6hcnN4M1OVsgMaGjQq0MCJkuRyh5lpmVIVuRCqx4lzsuxaG3uQDMp98FVD6VcluR0x5quyKEZIO6Av-3KQeaMiVrF6xYy1pkT02nNB0ZObpWSRN8q1H7YTdZm5h7ENmD7Sh87Qsgx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GimF5x4u1Gvu9u1oXZqnXugDi7x4ORvYmuxggHaglAkmkDvUPtopIOzTyLsKAb0xyIqE4aPkUYVSgwDmrYnndzAAUlr4m8p0t4hgg5BMPDlM95ij57ommH9UMuE3Wrk3y7Oke8MQPuFyP6k0FoFnvguuGSk3Bi60Xl_D5Y4_gl1hvvtQuLuDNyNy1QBkCGBCXvkYoxepODaK0NgBPp9uzLHNbqx2oaEmcLa42eaj4nth3lcD1iTJtEpcKx-aNT-7gCJ9fW0DG-CSIwjBUR0VOyG6ttMnsUPyr2OlUDOhz3tkxlWkglFckA8uJSKIh_LCecl0743Eu8qq6oMgt1ydtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbkHuvhTA49mnbBw_DoOJoqDqdYuxeseNCDNDp_W7iOJfBoh_Pp1pjCE9gSYjM_7d-y3E0IBfpgNNbSOAa1rLTVge7qdicxjGk6JdyMqNGJlfdZweeP6QWsWfQj0uurdJnDGCDkVbnPH0QNbJS9PmQTroHe42tM71cafHVkArFxU20SZuHaccp9XQEYXM2s3gckIIrnh0vi1M4x-4kJzPXA-jITHjGiE11tsDS58bDQwsUZIMaGD3obXW3W180L-CnuY54UTZnSCDtoI_v-FnK0XCy420Ru-p7wBlLy4YS9r3FslY1cAORExv3LMuCTHESCWvp-PwlQlLjBlWDngcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گیمی که اراس درست کرده
بر پایه کار میثاق</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8064" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8063" target="_blank">📅 23:17 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQVSMmqBIQvCSaGQnwYeHw4iVevJ3F-EwlnEk3YthsdK8xNcH48WAddaDJIxYipPgfyW_6dQxlhPpTth1e5snRqJLqt-fxYWSz0R32QKYokODEvAhSwOjJHVWQH4HNnFX4IQmuf8TQO8Zmt7yThfo-Hec88HV1qj2NmEkWToOZxunbxVqwS01Dhl87eMkxViXKIABiCfF3P9GvD7uq8xz_BtQKBeGg7NjMwAhqNf_7r-df_1Dw8nGirvPSZKPo26GrtYFJTcM7D3Wa_X9zllfVIPwcV1kni86SCm1XUKz60lXopdIGycAaycL4bZfKYZr1zpJeVvTJu2t42T1ljbRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=hNSP38bkSkeI29znsQy0AE9Uv1ObRBoSwNjDwZLC4ppT9zRlKm3-N6YaVagphzD8TNKuGfAmwMa87h23NO9Oxd6Y5Av2OyioVSyXfFUWevxCUh8r7eRq_C3Gt5QR6Uxc6cOcuW7nNDwSwnbOGcKYIdqSuXfg9YQ61uPS-au-Ih8k9PrUTH5VfVp-kyV2GKqAzKOgfHtpyD3mluh7VIFdFOL9HaeSk7dHNE-cnU_q8AWlyYPCrmZn5gQeouwjRATmjh3TrPFtnPg-puxFFfXtrYYWOvKNGvBL7u5gquV-peHcDfNGqUIEqQv0C7U6erm0RD3rFSnqzrAGcNksWeaaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=hNSP38bkSkeI29znsQy0AE9Uv1ObRBoSwNjDwZLC4ppT9zRlKm3-N6YaVagphzD8TNKuGfAmwMa87h23NO9Oxd6Y5Av2OyioVSyXfFUWevxCUh8r7eRq_C3Gt5QR6Uxc6cOcuW7nNDwSwnbOGcKYIdqSuXfg9YQ61uPS-au-Ih8k9PrUTH5VfVp-kyV2GKqAzKOgfHtpyD3mluh7VIFdFOL9HaeSk7dHNE-cnU_q8AWlyYPCrmZn5gQeouwjRATmjh3TrPFtnPg-puxFFfXtrYYWOvKNGvBL7u5gquV-peHcDfNGqUIEqQv0C7U6erm0RD3rFSnqzrAGcNksWeaaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RLOIOejFbnyTLq35t_ahPQvlFyt3liBbzvkjMt5LrUOFszAbK7bMk2sVO1F7gtHX2qAJVos0JVWvJ5gKRYy7lfFhM8FP32krw7zvKXNW_SLxsISIoH1xjvIbuBPMYyAPpE1d69kJ9MLH5MkmZQ5EB2SaOh016FU1XI2PjtHjZMIViPcX5uiJ2YLStecZON0yOTVRLsm1GMOphj8ifBVlBli-NHyOFZwgX_IWWxgQjBmIIXvTOxmbwBZEvC3Pl6jgEy1F7uoxBZ2gUlYBhVLOfOsBBXV8zSSfOFNYhHhOXj43CH868RF3Jc3P9R-bGKUGaMCd5kfZkaJrNfj4HryrdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=U9V7tT0oYc0NpN9nssGRSqTU7yuk66wQ6OSx-nqGLVzikTpiizErMFR6yf5fH-wlgINE4xJp2FCrmC3tPQGavvIxfoQlIOc4uIqg8QUyTh5uUfeYHEBqkpHljuTjuK8FX1ivIo1r-6IFNqqTXk70aMSzzY3Eqiaz-cphkdmM8S_ba7dp_-rEee0_XW-Cclgp9Gg_Aqe2WpyYH3EeAZoZCehWdo-BYgPNe5C_3bwipyDPluhaMW8hjlIgwNvmHF8dftEjwCaeeCPCy81TcfjTo0rgN4_3m0hyoS3PWdBNrzHciQgoHfPwU2yZV_lqs7BK6auFB-_tAQRqXwVkk8dm-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=U9V7tT0oYc0NpN9nssGRSqTU7yuk66wQ6OSx-nqGLVzikTpiizErMFR6yf5fH-wlgINE4xJp2FCrmC3tPQGavvIxfoQlIOc4uIqg8QUyTh5uUfeYHEBqkpHljuTjuK8FX1ivIo1r-6IFNqqTXk70aMSzzY3Eqiaz-cphkdmM8S_ba7dp_-rEee0_XW-Cclgp9Gg_Aqe2WpyYH3EeAZoZCehWdo-BYgPNe5C_3bwipyDPluhaMW8hjlIgwNvmHF8dftEjwCaeeCPCy81TcfjTo0rgN4_3m0hyoS3PWdBNrzHciQgoHfPwU2yZV_lqs7BK6auFB-_tAQRqXwVkk8dm-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwofNSnCRmNiKPMHqyvbpDILfpUe0x-mAvHS9r11gt2tYNPdF9n0BsWdbScrIfts4bWFbwLnPwy7aPfXOHbzOFG0kXNyRirawnRFAEX5yGGBpitr62n7qfcUfbHS1TZu8HnmtFNn4h377mRnNW9N8yarz76SM4stGB1fzTiRotbHrv7OK_R_T4kKyT8c7B2FFbvnXHxRRgSUXxvdulKenc3bfQhiC2wXZhSLqSHEgcJZDdGSCYy5x24bllkPYicrYn6sq3KxqBjrSod-KBHTArOFAyeiud5NTZWD7WovWFyGhAcwe6M6wSK7Li585rSQSqOEhj5bc4cMpMWueE0J0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDxK4FDM5r_D1q1KZcxz5IYjSBtZLajDL4s1M5upe5LKqaVPju6sj49F1rkyECW8CoEe3A3SGMefOjD9DrM1fpSe4eBV7ZVfoL20wT11MYNFA-2uVANd7IuUktwKKbN8QfcXPan5f9ZDxof9yYsxPeaF1FqL-ag38Bk2rqtrygXD7Cz-o9jr8XEnLgbnPFURKaqbWjovERTg4SHYVJJrZ_4E19jECCELcKCnE9bL9CB3ZoWRA1bTkg0bE9b1gj4Qa66DlLcG6gR_efOjuzSiCHE_MbdwvhhiwO2t33oT8lxRvQMszE3f2A6mGbsyzCUnfR9IgGHKlGi7_chhJaM2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_ODA6GOH1gQD_JpGHzLeHvB-yA3BgoFMiMwADzL7ZGjjlgMer8Bt2b8Pvv0tLeUMphdaQ4S4ZEncOaW2c4scH_VIL1XacJLWNJ-TUh7ehLbU6jtEmpivQwDwM_pVeOSiPF_gAgP_XYmQhgPtxE40syC51BFlwdUuXSEbXS8n6GhaWLv4-7HYvXkJRnFozsSNv5MKy2S_PCYCcQzK45tpWFiyHRNDQBS3-4JC5FIZj-iUdvUOa4rL3ULbPObIDXxaVSo6w8RqCET-fRg3Pk7vfnhML5iD7-N0cfBXFZh3twxUsIvV-omTBqdtphsNZfRovT0mfTEz3Kk4FxCmHHY7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5Y_NTU-im2qg3ZSZJVaYM95tnYEPxPMVeubZUlrE0p8bbs90LNz_JLzsBHe-uMF0Ap7y4UKPliEQj3og1Ru2yjsgQE5u8dwAKSNtbzIGVtCC7skGPOnCLAoJ_KbGHne1A2_8Ko_0PIWBcw4bzjJrxxjdHVhuQRbqTbQc13FtP4mim2Fy07N-IrM4v00z_tpmEJI5vBrc54UnbLek7ViraNkx_YIBTSSABYyVYrdxZ3z3naEZH2qOZ8nTOWOT7yx9OkqKaSkSjLLdFQOd8pjoC12rQG92x1bVyXg8SFZlnFb1Zf0sTqFJrOKmM4CL06YEgkJ3gNtcByn64gcCDQmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwT-IcwSh-HHm8N7QBe_gFTnjUZwd38MJkoXZiRFAOy16yvNNpcKPqLbFVICT0lmsZIJmDegQUlMDJ7DNIcwrs_bo0Fmok889ixUf8DiI37IyU3e9QhHpKGAhK3Leh4AwCYDLJ33Q0ymcclcSG5Da6-97VK_l4qAGI7ErfxU2t-RF-lmMs-NCZZYLmyl7kc5kI2niN9BkWTqUtCKN683a3w0s-od3W5EPAj8fCwhdzbEVA50UUSyw30PCdYTJknIJXCmJKi0vER9A8oNLLxgPFryNUu4SRg2X0-u7tE6CPXw1nV-HSoM5cttfOd883nzYuqbgBykgLK_A7xxS1Z15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=jsp2mA0aX8BNThcijSPp3VxF8pbIDk7gQAEdm4V3n9LHxajgZuY03SmWRNM8J-6PkGfAS4ZWNxEKkY7Fx3If2r4TMCjvOvQuB69xSElxwVKpqcG4-9r8nIQFSYBucGWuMdDRRsGyklayxMOEb9S31Qv-Ep1twkUeTz6Cs6rA4m9PHSyX9Zrdj7OvpKtujJIYgkWAh_aVjwKVECkmloI0NQRjgV3_kUQV_7RUkrDMx8qKcqSOEMlcMAjN45R1V1VCICoJImDfoGZA4ZgeLjj27eyHLsbyfRMez9jTQ4jDQhV217RDddq9x_uSV9bRF-H8KN4PKkl9D4lhTDNOVFjeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=jsp2mA0aX8BNThcijSPp3VxF8pbIDk7gQAEdm4V3n9LHxajgZuY03SmWRNM8J-6PkGfAS4ZWNxEKkY7Fx3If2r4TMCjvOvQuB69xSElxwVKpqcG4-9r8nIQFSYBucGWuMdDRRsGyklayxMOEb9S31Qv-Ep1twkUeTz6Cs6rA4m9PHSyX9Zrdj7OvpKtujJIYgkWAh_aVjwKVECkmloI0NQRjgV3_kUQV_7RUkrDMx8qKcqSOEMlcMAjN45R1V1VCICoJImDfoGZA4ZgeLjj27eyHLsbyfRMez9jTQ4jDQhV217RDddq9x_uSV9bRF-H8KN4PKkl9D4lhTDNOVFjeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnMsTGAME9MZ-aZFcnCmvF2MTnAmnpOacjI1RFWU6dmAO1nm8wbL9_G5KEMneHcmqX-4B8VXjNfPb4X25_9M9D4gyNAknWUFh0cupBh1n4Nf3FvrIqZiKB6BtU3BTHiHFlQCVXdR14-7XEULYzc60jD5WQQJ0LOjoeb6CYv4L_-lGYDkBa0nPiB5MaPKDGbeCeCx0Ms-xxsKUgY1YKKzsof-rujdK0KFrXAYd6mHcD5KvPgF2e4IWDDA49l5ZJjkdtQovNNhEgZcSfiSVDvwpO31E5IWH9hnczeAvL-iIRmhrFoIReDEoLSWXMxZxSXGwfiBhDi3KiGb6exxUVkuuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXWY0S-XBuWyWtNVkcoCnh9CV8OL3k4eCka_CQSGXkTAAwbcBRcX83zH-Mhi7v_4pZIVYbaCIDIYUmP7JnpNNyk6r2lcEoBQntyQKiWzwSQylvm3jp4M2gXnt6RaAkrg0KEBdGYx7vjXzzMGFl4DHzgUmOrXjGH5f-iuLFtmNS420bs68C1jdxBCOoZdtIlgoJzLKjcDCiK4PEquqMHqshieT1VDs_NNCSrvF_mxB5haiCJ57d4Y2KsgvqT73ECSzWmThSEUDFhREqtI_OxgeN0yOJN_mOyao1ohT7WgEWnJ0wbfOd2mPyB_XHCGal1xeEDjKFSkY0TO8XIj3oF59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVcDcXnn2BKzk8-uCG3rEbt8tMwFidxhViW3IS783A5IhPzr3b2mc-wgqe1fkV31o1WB_4juKOBmVlBufIwuzbJpYLBjt_HJxcGcCKPylWu8hzQn0QkMHd8DxpmKZJL06UTPoH75x54qx1WFfAg2em_4mTNa_UNnjUMDKuddCcjVb1b3kWWfJ1SkJrEyMPyDGvOoyvoGMsG_k9nhOlKpCLDqGj3Kxy2GfXOFgClZuBwLFJOuRPeGuq-SAc7Xr3uM1J4g7XCw0WEJUl6Df8K1f7NBnIB91ERvvUMXvtNgh7lpKFHqWnhkpr0xfIwujgFa1fYCjDEnkVXKbvQwMxKAwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=OMfA62MNtcRY5z67xqJfEIHHwIaPh1yWdFKDECuUfui7_SNrDBX5K9aHwa-UF-FGZvDAaGdLYFCDuGCodflmUEvpVE63oeH504EP6QltCDstUa7oF6UBDPizv0sUEO9lxVocmSRbn7_oWkOh8v4QrLjiiZ41j3SpX4K62gmaYCRYxRl1kK_i-2OHfX6AKGic2KDTambpfSHPnwK1QXTfvfphIRPCVNdQf1KEl--DUQwKJLKEOWvYHm2RMpwLJ9K6zMvILAiHJxmpnSwSkgStLtpt40ERaWa9S6pWHcqlOOWp8PGvUQ_veqhy8FYQq7zUFmVKUP9hKgBbP-ZaOKQTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=OMfA62MNtcRY5z67xqJfEIHHwIaPh1yWdFKDECuUfui7_SNrDBX5K9aHwa-UF-FGZvDAaGdLYFCDuGCodflmUEvpVE63oeH504EP6QltCDstUa7oF6UBDPizv0sUEO9lxVocmSRbn7_oWkOh8v4QrLjiiZ41j3SpX4K62gmaYCRYxRl1kK_i-2OHfX6AKGic2KDTambpfSHPnwK1QXTfvfphIRPCVNdQf1KEl--DUQwKJLKEOWvYHm2RMpwLJ9K6zMvILAiHJxmpnSwSkgStLtpt40ERaWa9S6pWHcqlOOWp8PGvUQ_veqhy8FYQq7zUFmVKUP9hKgBbP-ZaOKQTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWy43wy05bqb7jjVH-BZtXtZeNHlxKGn0-zyBr6Wom2cyo4FFP9Q51QkznqwBBD2tL5P5m3CebkJ-NKS5QFcSMQI9IaBX2LYpiSWzXUldLZxSrWZmq0oExmUgA9foF0KlSqPBd_tFzP_6MNL32IwNloKKNCmVNZdYN_4SLpGecXvtFBAn_SJ323snZlHPP4O34pOP0ZHlQ4k-lQO0vzsPpiGKUvP0BpvcfAjGud4bZD9pXsx13bNuHkpdXRuvO-1X3rGAS-3Yl8Gxp5OboKA7ABBsV5DuTkrlLWGgC4Yug7RQ5b_KY8CxXC5tGfl7jt1a82TqdY8rDyt_m5B_mYHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4WBZECtaHsjOPQhHSBFKD_rLCulWUOz3DmCMB0vVZEXlVpD7qFD9uz9kDw1_cBDnEO6fGPGA-xZ_31CsCKOSYfkwbXE6rwS7Q2iLsI2IaYbGzFpsj3zdeKCgVZh4JRTA6hOGYBUHlXza8PkAmip5JuUGJpM53QE3uKUOBSvTx6IDob9boFEn2OEmnf9Oy4wkj261PG2ieMz5SpOoqyyYp2LIfPR2lb7Bo463cFuZCcBzYAPv0XGIJ3hd3ZnDDTgzATs1Lt50VAk6_Rd5aT2299pJezZMRYKKiDEsD45I78C7bpjagZeVcU5esPmMW-HkvAaDfEbuIDztQpdrajvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C369b30MUTVyU0uC53CdJDVmKTLCSkC6rZ3D1v_EXhwJXrFcFnxggvIeMzRivtXr-mt5mUg8pr_1CgrM_KrJ_eKT86LJ8Sn6Y60fPjwAgntJTKG2a6Soese6aEWf1G8ctsVZfSPhmp5Nks22-RU9rJSCi5ZJrrg7cJHSQOjSy_mJDKIcNlA1CXMT3zCK-aW5Sy8X331WE7PQ-jRSAqOsimLc2kNCGaEl6TM_ItBhDcMC0jo7-rT5MQHt9F06kz7eL2vsl03UFJvZTLcB2gZsZ9qi3btDkmDEqbWcrm2mXmG0iUxG_wJsKgt5_guscn15Yy8H5S-dgwFEvFncGJAH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvreDOBGqjhxED9IwHOEnt5ZojomPXX_sGH9iCq5pzkwCfbynshiqs-RX5rHHYIQ0T0SSrmQlMoNPT1tVuIZXPM9iiSrCKr5tpKM7fak-vKfS_ZMwyiAYL2qbz4jHlnXfnYf3SuHglunAAJsvzC0kp1dpuL5pxKamy21ZdeFwFkFO4ZLe4XNhn2WyiOMFLC6-TIKVXN_Nx32Me7J7-ZXylWbDUuu-yw4I8Ea6GRvuymVdIpCfy9aK_zlKJ3ek9PMmCWoH7-SRBWxYAQFkfKwi1jpyEw39QYjWzRnNRTf65slIhd45c1jtGOKqTwQjwcO8bXc7rr1aElnsejZCEQ75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgVHfC3Ntu2rmcLfJyWhxcn3OuiJ00S9PDlNREr1wtlPt-Z3DHDgb9SwKjkQd8gLCgJv74jU_rz1gDuudrFvCktt_8teRAeznxsBcwgLOleFFc4UxMwkXy7B0_LL4SR11yo1niFaIw5xZks38BX9VepDiriVo-6UJ8IqXDkUELKvz3FQe-JaZ5l-KvHI0io2JqB0HZOq_E7iDBbyFxjQUOs65roA9AX95tw-IKthuB5xYEYUrRnwUuL6Cvm05OnXek_i2wk0Zne7WRFBCyhqrXlqzCX_BdsSgpuoyJdzGHNq69cQcwctwXnCXDkQVDfKQgmUbj0lRwKsa6szb0Prsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZh5kzCOcpllgt8H4aVPU7TZnrchAQzrwmlZNjfiwZImfzR4n3lR1hTSFKllQjnBHwVk12wxlBPNv644vtsZGdBno3V5sIXSOO9oKO4EBdm-b1o68QZoXk-aScJzyQgMlcXTDBDXwgRBFjMOPsMyFnchKU4ufGkzSDYKM79frbHK9RzC20q00pSvCrJYofxirvlTT1g56ZziFfI-9w6LvdjgtOzzukozBessalCHYYVGomkrbS42CRJEdY9Ckr7g9LQEdVHYhggHpI_0yQDFJvXwRpu685znLzMyMx4GoH2qDhIindb1yiZ6l95nxl57LAvL6t1kgJLpqD0PYEGBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoyJELNYrkRdZjP5nM1psY_9hKJ6z4O-52samc8qoS7eBeblo9A893HK5eOpcY3UqMnJ9rqtxG_Ir98LY2OTe33c09Ah7WJhfmDc0HGsNh6XVRUfPt-IKczwbTSSzSIIGuwmcdPtz3VlGcO2s39oZZvqA7ufktofsyOJrKZdaj_oxwQ0yanXQEL5xpbdwlPBy-KUzLLbTtIPvbhAauE32eNQKAtGWIQwQ96DntPYb7UZ0MM1YLzyC6J--LArmoO7P_YlzxloqexmmvfEADbOll-gh7F8i_hl8xmvL1YuvlaIWjvSj3nt6E40uC2w3SweyQn6i8jQPxzKTmMgXElM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4G6HE3i0WNRML7abqmZU8nftiGHNNfLerO_Uw6Zckyl3AZx8LBx6cVZKSoowsvxfuuaQ6nL1q5LckTyUKsM-WCfenLJFHg01y8xSarV7sN0i_IcU21GRyIx5IPPQqjte3bOk0Vrk9AayB0OeXu9XK3YjYtofVEvSTCap3bK-0QRCfTo5BBLtSeP6chlIf0BKrJsk3M9psu6TagIrSE8Z1TweJ0dD8VtCSRhM0jd9QgYIDEbFkcKHLuL75Hbjvhaw7VQhmr4BzV8nnkewYG3i4ZumK4UfcsrXQzjJaMAnll0i3JZi4FIwa1AlnQf-6qEBRQQl0vALhIpvr_PTaLMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R78-PDTJd84lHAJSn-mwGaF2_x0_owxlPcqb54EhCYMYvDlrbHjnzaeKJvtOyFcOMwEoMXDImqhdNqBfUXLeXclJ-Wq5iBSMwM3aY9mkWq1b-Y2zcjTg1bSiEvX_z-VIz-3EiUTBgfmjHEZOHxgh1Gz4xUql4pgiyLxehNctQI0qdD43WqnRsEq330yiRdR52rkwWENGwByBSO44Igiryzj-gLf0QshfRg8QkOevOnHllnW0iq5IG1J7FdwXSyK01KDMN14iGiIj3XSG1ZemGTrKcXyoIZt2v8JkJrepIIbvwkhsOjG6RVyRp3AV5sb96aR8CmUI4mjyqbKU_YVkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyoW88QXcqDsC9LBtxLCLZUacBdJLwu4GEfA1gu7cUyYOb7o3-1SuhM8Ybqt8xp4t5FDhbQjjEEV622m8PH7pS7e2HMevPZtJk_jto9f1t0XWrDLq3DFqvrzPA32IFBVeMcnIMQxYwjoK-pA4wuVsoPckRN_vpupD14TUCRKFVHEt6s4qx4UXCRw6LzfIKWyp3yEFqfKsHdRWKqrKVbfRLxkts1EsBJ0KtnVsI_1w6BnIiJ4a17bPbVLIPakSKESZ-zdIzkhF-iVewZaFUwGjp_k2pBvVaN2ZRngntI4d_qnK42mypcmuvk11K59OW7tT9MjAvpUQrqg3hM43EHiPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoXvQzXxmvzVgcTlzhB_5pD1k-RViOyyc9jBYBYaubGgmGalGs8i8Lc4u4ERAk5yhhhKAtefjHjycevAWNZ09hw8rBObE69-wdPhOztWdXzzO3GijNMFKhD4FEE4k_N4fvon78UnCCPnbtsr99hbHJ9WuwgDzYw_Pnp4_wv9aaCfSlcGfLZurKwtXqQ9m_gVVIsgYzMwhxzb1JWtyXqEEI4M8hti5IDzwTk64LKqIuJa3qWWSenICt22Q6C9o_y2pOOZ0UT2pZWj75h4ms3oZCjObub2Yd92PEEoru01XaETdw6lB5v8tXIfrtqIqf58V2brW1it7RaCMXtUMGVx0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCcyUBmXQETTU-6kw402npJkbp52u7ChdtKZTAXMUt5yl1pNxnQ1-udwXCrIE5-Ap8qJ93tE5zP4rVHfNAVKRwaF1Tbnb_0n1CSQYsbxplFQXc1cwbTX5tHCPTNi6zaRbrSdTX2Ya8pJf9OC-KFsywT_VcmLgoxPFTxdsxUQWeac2XSqxXhjH_TlOLe-ttG3p6y0Wca5O_6cK7F2_Rd3qRRnd4mCybM2WRwTW1DtrmyPHilAvPfTA5ZrhePxvMV_CRsMsjK0pObv8YswMcF8I5aGn57yXVadsDeLYKQ1X9XEK3XShQjN0D09mU2-aOGTryuTR_ZWxmZV4Pnx_jTXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VROChUUF6UFrbRqb7z0zndvPlpNUmKX9g8D7kIx5q73-QzNxghgRMd7kVGeo4KJLg1vmNqYb_MndZ8XsBRXfLNKCTc4d8PVAKPD1yy1JJWgvZoA81KHnB083GxKEIFylF-q2wWqL2r1e5VHw1QSgR4hMleUxfhIUqqB37jqOLjW5AU9VVuzc_E0ZDfTaPKWBx7KSDSyWJntZHO1JOEFca029z6MmQiavKmO90PqS0DyFtNG-N_ZZfH6sfT-xOu43ep0QkLbfPlW3EvFHlBte2xovFWlz-VfsmkVKz4q10Frdj4F9XsfyOeO0r34W1HH3Bu_0z0tslgTbF8LFVMAphg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNtr4HLet8dY-L3A2w9EY9wTrZDDQ6o3MREizXM8JdT8ymVy8WZzQQIbRah1alnp_clmkuFiCEcg2G5ziRhbRgadHYOHbCk4Iym8FcUspdQsKyIIM7WbA2b_kyLFF8Kn-Nw9yroOUKZBCMH3ijZyi8N3gF-LcjHOk0gYdv5KXrvMHX_31oMyFWCTkgGVS_n07-4xSdB0LeQxZMrev3eQO4PrE8DJLmlADFWZV0Ov3YZCzXyhSoedpybcUBUp-70ly-H8G5Sg-ua_pauYZz088SXhwIIbu9v5jqDm05D9DNTUyTpEKCoQYDqNH-KRv2nf5n-Zcf2-fLwFgFk5wEZ9cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Fwg0rQdfviA0kVhe1ErATzn5tnWze2cgtDg8wKHwLbBkoDHgkYxigd_2TBwhBbSK_xQYuBdeJz33ViRC8cvPW_ma4_-fOeSH2ah4Y-TBJKg7h1BCIRBrfyKbUAOmY4trESchLpsosGb0ZbC1dwm7xJIML_UBdOx4Kqp1HOSvwS5gkq9hyAeL6o3DBC2KCzZWLqD1pOVJDyDDE28Kvp3z0X9iduRS1kRVmH3lPCX3Ln9n2qg1yuyC5WBMdjNM09hAywXqQThWyKM9WnJbct9AqlI1BLiiSZmMLtIn0Xt5-vEJxAPrKMLknPde7EGh1CluzvvbCLC0cN4N2zzlqhWDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Fwg0rQdfviA0kVhe1ErATzn5tnWze2cgtDg8wKHwLbBkoDHgkYxigd_2TBwhBbSK_xQYuBdeJz33ViRC8cvPW_ma4_-fOeSH2ah4Y-TBJKg7h1BCIRBrfyKbUAOmY4trESchLpsosGb0ZbC1dwm7xJIML_UBdOx4Kqp1HOSvwS5gkq9hyAeL6o3DBC2KCzZWLqD1pOVJDyDDE28Kvp3z0X9iduRS1kRVmH3lPCX3Ln9n2qg1yuyC5WBMdjNM09hAywXqQThWyKM9WnJbct9AqlI1BLiiSZmMLtIn0Xt5-vEJxAPrKMLknPde7EGh1CluzvvbCLC0cN4N2zzlqhWDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmSveMxiW8-A2kLwDW7cEhHXYmQqSkZD56RxpOJhtKX51ISZOdS_NiJoVFqQ8FGpqkNge9pNkXy5gKWRtuHPUuAqXynFcPazlNiuN1EytQXDOkpWEGvL49kz2-K9NqBVLVBdsWbfDqnEudjb2uR6RMYQsrMd0AhGm7yAHcjCeu2rJqIyrUdAWVg-si5_lbJfzArgg7uKPiO6Y7ouOUZhONc1bywZhUbW94DuMZW1GWXD-kkRBc8siSabA-SSa80DOLUuO5Nq16lbCegadJ_nmHMxk9oyl2bqMFM1ErjfUM5yUi-2Fmi_Us6pDb6B_K0eElIFzcGdUQcJcjhiTr2bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKOCOfX_dStU9u1ACbdVOpmMD72bKzhEu2IB_QshgyHFBEZCKwV1PvEYnED8MZEg6IyuXyys9zAHeuYQ-sO0uV6NJM1xEDLFwKVIBdMgmjUdi03YsIDQ-F2GWRm3K6TZKkhdsUWCbwSQkl3qD8pJ1Tks6gGMdyqLds18nQoh_TwCmJNj938WRBbliYbRPpob95WY_ZCIq2SE5jgSb3lRCabh4W6JXh2mOijfeCK4Dy_qWVVOkmYV3G9W_Den9z3CU8vM3ljlCM1lJ5X4PoX168uGqBh3UkdBxKo8hgY91qXbtg9_snh4ocm23yADtqPFaFN1O4BSDgUSB3ct-ZftFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lytvIlfx7zAmfl5TXBgYzwaazYia4b1WpOP222qitpka_E8Wak4mAQpdqeNzjofrrk5-ANwR2C1T2xY11pC8QR-9RHqyKhtkdMalxT7Qp88SWAHZLwCIcBWhIpz4oTFzIkQTQdkt9mTVT0Rt_H6WW9KnQtCV6rHvoe8VNvSwSZgtBovGA2r9COy0r3QZQlWhvLilbVlsSjy9iyUTddghqEfmG5yaufcSMjlMHNkeivKD2HyI7KZ4olTlcI-SIrvWvGIyfkSVqyB_h9NkWfEmlW6kq1Jcu3or48nRGWLYdN2QPxnD-C1XBtY-yarY19HWtYUIzGyH34kHT2jnQ-HqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZ1KbsR27Eoo5pUNS3ksGsAZ6kUeNvpnwhxxvKccqtA-89Lmj2WEKAE6PYx_E3WayusVGZSeW9prmLjV3ptCLA80vS6Dywh-lEqT88XkeKS8dOmjAzxoxTPQpkRcQK9h_H_Qd95dWLwiiBHDne6CakQuzHW0vW0x_WxegBdGNQB_HpVptQgS4hVzrBrK9LFJYN7WJBC2oUiX4gP1eT0OHbsyLhBkFPLk7CPXUWAAptzXFXw3MAATQ2z-qRC8CtAZasXtF9hxUhBDJN2gjHa_iL9CGQkeyi1XmcJ78OVjGmx8Tjit4wVrN2cCwMcRQQOq3NML7GsrISDKz1VS9sbwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaFaOGunOHCHfpUbMniMcW--twElUiidVNKvYyjxF9CL8ozNObOkpOyyrMjs78ImvSuAB2zgaKw9BYTwgbzPOdXurpbs5iTTUj7MUnv9QVuvF24KRKSKdZ12IJorfbMOrYQep_8Tr54Ix-CsBnIvlWBzwZRohKV0PZhJkuN00xnGuMJRBra2o2aNiBFaiY94BoM6PVP3PWtVZD111W8P8h2q7ZjZegZ3DZxT2ulPP-I5EvyU_Opx0vrtMuUap2s7C0bq5OGkMRCMJW3C0QRDj2DcrqH59mBx6Ny3vje6mV_KM7_sa621zJSxxhP4Ko5yRZ2FxK-Twa1vx5z7-_Rodg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtyg_fRFXN8EjvIiuy69hO_sy5UBYHWAga7ydEEgbwCXxcqrmXgPcYWnBCjgiWvTjAWDPs7gewd90ybDVNoi46Q0jiw1hXnmh2fFOwdB8kylKqfSDmkg_OGlHsecsUXgDqViZ9RNYwsPUYwlav1ME_3Thk_PnNGUedNWuYwdRXYYPUFo1t5yjQKCfIiDbC0rqU36eXtsyorkXeeuNTEEGAmQSDLSadZZcx_514gBc171euXmbXNnadpDC9xKl0eOcm_5Q25qrGCC5Su8sW4dCcUar6K6E4TgvYutYZ7pkguBwEy4XGo7fopD9mUJo4aJgI-FXhH0MQVomd9fi70khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGULovC4mkkjMYKBI-odsTX36xrMeMrYFMMQwccmhu3lgeFqRv0erTWjPRJRaULU2O4em6KyPxv7Wm-_Y0ar2P-hLyGO8okg5lWvGTQYMw07bm6J2Rtc7E79hRweaGney5FrABN1GKwzNPNhH1FfRUZhbdtgGt5n4DxJDJzltcX5rI13WPVoZuJH3nYNlNg9QzZelAXbDUoBbEJiKENQTKBG9d8JxH2vudDoyVK2PnhkRKpaAPeQTR0Cr_SAFWrIBlfeQuVMvx44TyFN0B8IhnyXBXvRkraXI2rbHM_CQUKfhYuXyeRMbxfVo-epmsK5lYkyeAsKxW42NPerGqovNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtWKXL7nJGK738Fkooxdf08jLrRNQt0POzQSmnxotJqREalnRSFVPZcqmuR-ocmMUa7FZfBtON2RNafgMSwVKsapvcjcIo-2jmn_YupR_Gonldy_1DYYgmrMvLfEC-fOtny0EE_sjEm-YMIK0yMWpXzYvzLJbFSUYXN9n0r3mwUyNPDmUiWQSO-fmL2JO1NDoZHVHONRUo1TepAnxhz4H1b0gLkb0u3F-BQjM_w10oLVLJ8djSWZqSbIkI3a5GCHlqt21mK5nhiWmj_6MIYGKHrdoap2tHcZiOP9MTbagYCsX7B3UJ143wQPzngyPg4MuI10D37HRybrpmI10Q14SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5BE8A13JrGC-wWhNzzSHuiFFdRfLSSxnD2DmwVtRBgPttI7mgwzYJhngCBEFpVFaLlJZSHhw3ZdphdAafuAepjh7ChRcem0D6JX1H5ElzBlrF-j4F8SBqov04dgcZgGAxXfd4ugJumylA7Ubwppk1bNWsmVT2dVTCbtz1fysFvOjkHezX3kG8TsG7vk5PKDil1L4pPNY7NDDYvSKeYbzydNEfpy4P89XU0UqYqchoWwC5_8JGZ8wa2rTkw0TmJRGrtHr_9DU6nRtAtmoPuKxFew4Pw27gGF6u1gpri76PjvgQ8bmN99qAShBNh9Bo411UVXE7Lo4BBDhUHmYQfjkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYNqS21kUfvWIk44P3p1f6Ff4DUN1y36XVjrlMVQKw736_XCP8zl282p9CZoUyTMqj9x4kb6Ced_4Ajojkamtwr91RE8ZD3N8kJyJvcIT4HXc4cisXfYSyBiSc8bUyV1bJ1nFl-1aIFeP-JGn7h8uy7vnkk5_3DwYIsuEv1aZJm9UtsnUlWr6ZKE8-R6tFsYJtupy1uNwlMzcLfrroBXDweUWXOtVQkZxbOLPYsIWFmb2a3sWodWonlZjfajewdK4wCg61S13G3j3mNT6TQcITyl_JD1d-7bMXGGwpKlPuKqJQsiCVmfz5_KsOIxF6BmAT5VPujL6Kn467bkdSBW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE2COd2WCGNnp8Js5IFsuFBl11jJBiOyBgx4yeW73IJAL0NpMX1_Pyxm8gDet90beTGmBzxOBauYAZasSuYXE8I6s8BQ4y5vMOtEkbDD9wkBqlp0iopYub8W6XE_mQG91o6SSfheU189yu4f2tuaOch8f5zWCMNdUlcLoqQhYbNqyjYQMmY0YSlOTqVFjCxqra7Vi_nPEihw06PDgZ32prL76U-AJjZUXbjhVvEkv-Nr2Gwn9xX_eRSzPfEpYFJCd2ExR9OfyPzPuHOmb6nRrupiSBKU1XCLj2io9JA3CykcLw9aiPED7jEgVwlpCYOdnyDo5rBpOufVXrI5Us5QaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhyWS1tn-fpGFTqPjeuukC6sNFqL6HlCrXj086OBPYB2vIGo_eorRRvzX5NHwaD-eMzHob4ivL_Q7edXT1B9NRrIuvJTbzwSRWicfuqNq4NtfpPHd6b9PeMY8S9xYdb9aLF3qWTqQQLMhqJ-NCnPZzZOpCez_166OypiDnQ0ddF0wn05Yk5q5DYSoDaQDuaNr69UY9OWKgXA0hO3qBWA5-W_FZMGl6GeKI9Cr8U08o14Vi6FrDNzrAcUHw6bmSnCfDgXRMtR-4b7V3LrilRfjjoGTykxJnuHYXFNEiflojOPFhb1mm1W8vMQSQuJJUyd2eS6s13HJ_yn99CajJB0vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Mjxn2ziOQFmjJx4KMsVYa29vkr1LRYJ0Mc8CxwuEP3YqwGkG9bUkVV8EJtyDoYzG5xKDX_fIb2RLYz3Sep4yuHfTX4Mz41iPcZvYaHUVP5cwkzTWK6b5ootlNnwC4t7_JAd3rLXbdpii77FRIYSb7XR-XZhaHfNSr1PwND2XNMfJxkkNQi0DveGz_Y61HP9HfRQBZmxcp2suIr_PfIUHqopNMAjF_hflL-W1H-z9W-mThhxEEpQYW7Gg6Jb7AtXNtCywczLYnbdthgmgj9pDOIc9RtcpMrh4plKh2Bpy3mh2UV1QQpolKItjZbHOHkmDV9-QzGph7qodOxtxOTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-yR2j0xGNQ1IM0JRLhD7BYeNN6dXL0mADOwdb1nQoy2Jq2kQUE1EhIG70tqzehH50It5zYbyV3TwHItADEMUr9TWo3hFq9bcuBIwyK-9RMILV9DWSsLsDLyQfBPMbQsfbwKyDci5K5NtUZcgvUok9VJQKq7sZLpAo5ZDa4fagwwQQfkW_KPT_utRgEfHcerGZZmP7CJ_Phlcz1hT4zD7XD2gFj7mRalwR0F0x_BugorTCdRt97QPKbINueDdLga1IQ9vFcd3m0te823izpup19GSwG33Uo50ARSLIei3jGNbl6GaAMBqb9e4QU4XI6zLNplo6TnZLMXh6ugdgVDLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJNkpc3EsY7xz1VjVKkNQKGgVUixEtGHzt8kvARh8TiBhq6OC1W41eJLoHRnKoXMI6idYbz7PYo-Jk2yV_Kqho7dFnyHo1J1XxTi5PFZlxdj_TxUUtLy5mDa3VeHWCOSnDVObOBnk3H9aQZxRTs-08k2tM5rzwP4M8g_PKc2nHRzJ4L6hKYxCwejGo7c05UVxqPGGOLCXr8T610NLY-6wfJDMbWsJl7-UoH3OoKlwpr_ssEqHxJLqi6qK57EWvJ_5aG-7KIqNlxXwsaNrfkbdq28BepdVbuIqY23-WgWBI0PnREW9rheOGji6QmzOBSGpcgVf0dGBM3_oo5j5JSa7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR9SwQKjPYveuSRepg4sfk0IxDKzXl8zPO_sP4dMsytPSy2YvmKEhasN0n37OluYIjJdSAZmv6HgfzCr20kLMympr4HWnBvI0ZiFxnwAhmdzzXK9zccxOUoDbvjJzWKLj_38j-eZgfdPcLLE4qYIrUeor5QFPKU1EdRhvPFH8_-xFBzt2JAB7d5Z9ghyYfor6FCIoCv6d-209p2F11z1iGDtyd0Otxzaw5oEPl5oe19BIr3ks1mjmXM1P00x963-wc9Gjc1Eo6miXxDe3NvNqIo3mUgq65IfvzRj9VCSDxFDBdF0DDQze99cf6fO4UuDpEZBo37moJNZquAFQbRh9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyteEOMTeKc9YwW7kFPv_YyaII_7uqZFba-o-zpd0YdjkkvxiPQlGIDlohzEHwS4EXP-WBotzxukQNdzPF7ta4op4ol2VvW6ly0ea5PzS5ygPZSRpKkRp4eiY_BCM1yoHgpiyemRA7mVhmg8Xzn3M_sdHwkhSdon6vJKfuxW4l-QvYZ3uz9kOePJK5WZRW8C2Gtb9jlh3sDA9V6Zhh18tdI0EikruBt3urTsrZPBMrJxLDkOLi6UC2mKpvjwQhrriTkyZxK5LrkHMvOKLOHQ05j5BH7xsYBojnT_qeS2ZH7IOljZerI4LmJe-oo035ZML02WoVQuCHgRJEQwsvciuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI6X5lwzAWCnl13aNruk8BW5pHVgU0_81RfHI2WhzH3p_Fm-m8rVLVZhyCp_eBIZXgtEv77Ft6Cj6AQnaD_6JsTlDN-cALIDZHqNeleUwYo8jHgRzIhh615K2T80fOhKmFksg_wPjIR1ZZuQRWOM8MficS8zYvoyACCy90orVM9MRBXx_T0o0eiVxwc4-dQ4Iamvc1320AcP6P-2LVmUE9Oi5vqnaAQQawUqHOX08f-V_3pHLg9V0WqtiNYtFTbLCAiVSBHHYrEIjLRoF06XHdarWd4E83DjCWj0TME80licBZDDdx_jEcv4irCW40FqDPeHDDpaq0SnygkIcX2whg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k46UMOxDgxeeBRqmDhSZ7Lavxslobflma_Q2-A8NEtZuLFJoV7kZBrcUN2KlCgOS-MBXpuk2Z_W8yaxAmB6t6IpUXX8_G7qek552OA5cUvdG5JBbJAnwWCUxdLcxyQJ7dUqLv4m-5vU0J-9BPszDNkUAhhsGOI2lZMES1a1zja4IgpMy7BEQD4dkYO97aN-KLbcGG6QANtBLS7od7pIaWejr8vnBiGLBuIUtwF4pVWK33hHAyMtg96VEOL8iiV3VNvVvmtdefyr8Ux9xNcig12rrDy_T9PIA2xvjvdlNKYZ6vEPLOBhCM9FrzrdUP5T0GIZK2-zlWbqSNgs2W4LO0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJ013I2R_08Y8AY3-o78klyibT5DkSq8lbZixfd7xwICc0CEEUN24-utlOTQFaZC8-MzP437yz6kfbhvY3xKdXVtmF7ec4XisxJeR7p8L2lsE6k7CU8v0kOHHPfYbjwSI-iTUbWVRXCYrS9ILq-MNFLj5Lk1pmCE-y1U2PWJFXpARSAUaJhbgADwRHQACnQh6UNU5fgPCRPzVfATDxyp91JAS_C5H0g1IXpxAE1pAkUy3eYjo_gsIIyKTL_6PQrNUupzw3LgCY9KKvsMrVw5hD499JV681urkSBE5tIII7txQxH46pwcQ8kBhtKkFSBojmXRJVFL-kwRRU6mN59GHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq5gkuEUrXdf4x8t_p6cr13dRRARipg4hPS9CUbZ3qtTzTBDcTLcLMAuYDYR5Vc090_7fYQrRu1aVc9AyFKjAAGphojeXX3ojwX2mlJRnRKuoiRRJEk2oaQwEgitJVPiNQRk0y988fW25uEKgdwrUBH60gJWw9ZG_QLWG7ICBsPo3MODVHIG0kgTzIPZkBXPgXnv87TL2Gcnmreu0QR7TQTgh0g13T0KdLaj0IjAS6LFJcyXRF3mP14kdzHziZumNfDxSHOy0iD3DeKFhr7qq6puAp3Dn1TjcTw67427j3ZCVOtyN7AIafcOAUEhFxT_eeHQ9YXou96cJvgIcu5SLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkhV89h5K4M47yXaQvBMDTfllpzdGg_-cljvx4_5m3FuVU4Rp6SHyKVCXy90Yxwv-TXvTDDKipeV_FkWP6ebokkkd4jYRdAQ9OiiDd_9a925fOxUwu06meXe-LI2OIeZlcVqchb1hj2pHBRRbECMToKuQ3lxd_3gdWBZjpZiaQtiSx5glWYaptErB3vb4bq8zzqxkhPvHc8LRVB9Dn9ar9Ie093WjYHXHyqBwHN6H7MqWtoHlW2HfYK2tO3pA8FvXj_lzPdZpBGmn6Utr5W5l8yDrFnFunFJCDjTpql2LK-ziQ7Im4k2P4fr0K5x3aPW9Wd2lWw6Yvp09bXKTIyrew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvzv9p_S1vvPy22N-doQdnE0dsP2BETDHAKVg9F57QooCHyNnG2uL-7VYdA6FkrFK5d1TqkHoQ0yWsSYJn9AdvfWVVvfWyffpPTMEQz1kqi7g3qO744Y5sXygH80vwe-3mZz26g5o6EeQyfG6QhNQVHrKje7gKxxa9_T75Ujj-2m5KOTJD7tWvSTk5bfaIS-_PxvRt1vgbM46tSb5LMQj5UtWbr-yJon-kbG_kJ4ANsyn0CadfysrrXbgfHP8jSG2WzwFjJF2ZTt9ff3W7WEPx-y5Hb-WH-dnbO3w_Gz78y8VLgQn7XpP3oEl-FvMnG0l6SfMA9FUQT10Hm_fcdYsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXb8hpRQiWVBPdj3rgSZ_B-hRk-aqGt_W8nUyJSc01tRoM2eh4z8plUBjbZPB2te8zZicHa0LpTTS9thAYTaJ9OYdfcMeh2sJFoyXYXK2Y017U8CCl1D8sNo-SrmiFwqCYLYTTyK0ywBVF2P5J6d_hJ2Da5zdikVevpHO5dtVa4347rTQbQrGLfxTmvgCzJTZ9F67Nz9RWdAGzCbu3VDZVbEtAnepgzQCQhy2TcoIygHduqQGgtdkAdVMATarzEq9I4luK26_ZYTQrCsBcRad0920rLDkf7lSPL2MVzp9INMUUayD7HsZfHJoAhrUPkP5i2dj3hsdgceX6kyIqrnJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_AvakWeujFDfqtVLLmqtBY7SQzN-89269zrz2_y41_zjoHIq5OLkElL9l5-O4uaU9vnU-A0tCVQOr3gn7Skpt_kVplSLVYDVyiiX-L1SQSu07B78KD1wh8Mb5dKw_dkZRN9wiWb_U8IB9xRuJIPyXLFCPccOt90WQ2g3ixYkdA4_44MgegltOX2fewOSvBI3Fi9LXbH3sThmhye6Qgl2VNMsHEHRcU954eQN--OKfnL-fFF_ZvyEP1n3SVQ3WNikSHUvJ31Wt-KPuujHtvjMgWC0Db9kRmf47nQXvH_v9HF1agSaP4Je2-j-X-oRrCdjSYHd8U0UcdxCNErdap3hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsEsGkWJiM3woS8sAAebHnr6HKFTgCPVU8HiqqeSTyCxU8noH-HXpKKHJ4z6tOSB_Zf6NHjB9ItS53CnbpNKdeSfylVvxa0OoNkKkVtWb5vEhQ_nFDE5OOlFsB_z6qSqn2AHK_Dm1kPb2TU81edbkDmbXEXspAmMMC9ydyXLAIgNWWSdTnCEnFjm1x_ftC8hNYNNreWNlAHpQbFtiwtJoTUdoOoUlR_TcXmoX96AAFNI7laivZX2H2tO6oIoMpY-eZ-bB5Lsf9qrLE9TPJ1a61jVDLCHosJxupy7cAMNS-JN1ukfVsFwiBFyLziWGcTTYTPJg7WV9qiawpQY_99orA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk4VgSvDXQouDrro3pYKf4QhLnPYMW_0Z-qi15tI1TMbmLsls_d-8nG0i16yEjwl_txQ7WAvvM27VlNiQGrhnakfzmBAClX0xRVR_feHtl3_lNxvc845fUdVyu84RimB9wJkh2TnhAHcDvcHppwVGsvhTnHNpapdlIgnYHsGkKnkOQpww_d2a9LK1W4AeDpoZpCYowSy9SIOcVP16vWLOknFoUnvZ2s6_chPH-DGq4IpMEFfZraACaGYKJPa9PnrMX25F5JG7EQvLeErAuBcLqFDguKNGC4uZLFHWcoEdpeHCajb0yACnpjcB5S4H3r1191xtUWI6valw4OIi1zA0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL0DuArtAxBtbMsiX2-CLBKWbDTohwK0oVEiYwbAwLwq9JoGUKIyYpunrm9Lx3VW84fx7UZwt9M-JCRE0dYRsAfBYTtvoD8LWNVt9AdHK8HFjbf5xFfUz0jZZrDvQOJSkdtkBciIuuXZvS0FnxtyUBMwwmMg-aNN7bhvdB3qGt5-ZCEEDti7_pJyWHROxe_MxcT0k7mNid5W3GES6H149gFVQqWd-Zmg93Hg40t76HdRhKEoj_7gcgiVp-l3IHSJfFdL-tpVSpiTfDmvDRMmWc4hI0H-3hPdIYBo1_cTHyaedYxsATibPwOYupX1RNt9TAKaMn7pRt6FMRWl6j97ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myVtvHW5HoBd6zu5L4gMuQO2x088VkbzrGph7SKevBot_15fDZeo26sP64kqrfxor6RMzRxzHtZm7fGWbH01bVPUHfNbOeDBpv1SWIEJsZJnfxw2lpVo_AtA-wZfrR2w5bdSxFeYcWBVvFkw8UfCXTUTDXooWF7tGdhei5dLkz0a2eVnRWPjfh56-DF0B4CzQ7YU2bRYUVJK-JxQyApeEeg4pzSAgPW2y6CB3fLV-gVh-SjOwojkyvMICV_KS4H70iZP9uyeHWkj34AN4mdirGDmaozZ-awZ5Wqzfda4ysjRe2w1TTMVy-8lHWYmlARz44R5a6kA-Pu4i84VfZ6_oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDGqT-dTvwb3jHx3otqmRmB6myJu8KZJHPgBXCFKC21OpUKRxbRHGGdiDy_zBt5V8ZkU8ifySDkKyD_7irCoLP_AW9U4QFu6KSZU3NYci_QttFGK1evzbN3jgTGQKog1SQjRNhuiy48iRoB82iPBtq8Z0_uaP09ySwD7QVP-OvaITj9I48thfrGol2RlE3nczIyEWK1-Lj5JjJzfArfdgZQPDEsuO3AS_BMcVoc8SZJufy6vqJXk8hirvYCuczE3g4imV2mEiv_w7Ec2Xp-EfAiuuNIP_8fqZxIM6HumXKLqr2qWWMKhqOv7_zyTE50OXmF-zC3XxWCSRlCCRdaTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVSt-mgeOr2zKJYt-8YulioY2vCjCEt8DjrBWSbMoBIr2iSLqt0YPWK0cUabP0TxKsB-lxrLGN8w14uYRHZt3Oed_0wD2mvC350ktiK2de5Ni36dwHIbCBAyOsAdEARKHpYTZUmYeu7YA2ZvjFtQEYjcabz_hzNqZYuQ1ojhdr1ag358A_hVfgOk3Jv3rLEjWlbYq2R_XXY42iuBvh7us6rr1X3jnmMyUqvZ4T2tnRXgVfz_cujEzvD_viigSzr7_fEgvkp0B5UjlAH_Awm1UuhvBu6UA9H53U9a6nyOZd2PABAOr8EcHx5GSzt_UKbzWgK6famT_Ya7NwYsRLpsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyxQBnsMFyFuvrptUU3u-S7llCA0wj-wnEDJ1p01nbCt5tT77x9UKSOS3CEQKfD-xgVcER_EkeaFQPEa-LvONXQU_27RpqPkpoDY-jB3I6E7KEjwqjaRGENtOSmb3ozAcn01hnerMd80AZhcnHBxGn96f4Iiw-zZvG7XPejVVB21T9sWNFk4BbrEBkmi-aRVHt7xTlCFAdNwJFSlUpNqAnfJYddeqtNm6lsUpH0FRC9ZDRq74P7ijI5Z1M4BqzPSfR68dF3iomz8EmfW-t3Y7HjG7QmSm08iOqybp5vlCSuMnyXLgnOy2Gr8EiilKLHyNo6ZemfvQOe4hqpT_lF7Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHqsvge6tQT5SEy5xW1M7T6tA-88vspAkhy3ab_QkOaZIIylcAcLKUSrAHh1kCDUArVl8iuU_aLqjWNB7YKWZ0hXvkw4gnhwhWHAQ5mN5FZh9oWoYLT1gUfNwj1LCKpwt2Tock24xxfxW9jhsv6epnjs6MTc96zEXPiUtyfEh1th_WkF5MOMKZMgere7c-3Pmr4uj_yKP8eJ_gVRVfk6YsaGjT2ZQ_UZNLlekwMcKkzg7cYGOQ4HKXF-bY9sLfCD1llgeZ6IcRfqMuvuGpbSc91vBS7L_u6zw6Bm8sU2noSqb_yZfWWOC1lGiYF5YbQaUEmnwf7WiiY4Hr1w_D5Xqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epDkEc_RYkDpRmJYlwQrr1R152TTtrT8-Fx17tKPtShVn57gFF6djyj7qU3CT81jNeZ7zb0wii_PVRKFtHjPjkqNxVGnNjBQLlcounWOzbUOQ4h5VLey7aMd7u3BF4krbmhqnu88sD7GFB8nCt75uvvZIh-UJmRJogfbqFcRPDbv7iVelDERCtTXS6e97vVfKdoMUce-XNNRojAdWyhFRcjpLpQNp2JzTFWRY1VpaeeJAiYfOjtCWvsxZfWSccshwu4dZNt_OpLUNHM9WjBSnZELEdFZPfo_2-QMy42vMWF7R52kEhtAW83J-vEvzKOFivBEu3VB0yDMsS3c9g9xHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vlq7rTSUBT6XB_97KfsV5OIuNX1QWopvA7JeXUpedjMbZtevbibnAC3j1kYG_JM_MHo1CW1VO95C32Lb0IqQtxEMuznj-pKDSI48DLBU4D7z-PPi6-8hH52i6FrYcKgoGB88bbObCnl-LkTAUw_hcowoZpwp5UnilPgqSxxcKSLqEfu2zGYTs4tcW5BjNgpwPvepiFlTaMBHnNQkaDb4f2GKaJKRCo1XfWbiWDPirFpyEgiW5JNjEh4paHxLam6yQObXLxrObea1SbChQ6JraZWZ-_GiH1tThTwN4sTQ92P_aMC3z8XpQUziLgsqdcucUv1u631FTTgFilxrjBI2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aufcnx5LxjnBpr6iOkpBQZVckZAzPTiGZ6W65tun6ET9Wi3EPFenFDxlIn4-ODohZabI_rOch_OWG9qZQh2MxOZghKm3__EsMjSyilh85qgrZp-swidcmO-Iv6CZ-3j-jvhQDbzpVULG1kjWCYUA01v1Xc4tfHggg6XxXtkUiPxrd2AtnTa6XyQ_qailZjdcMEOEIq8xI1cmV7MsN5KFgB4tlNV6j_YfxYSUwew_KnWfapgg6QfSJCryqNbKLn11ME5Hbv4hMYPqxrvRV_JUFuyxxSZ_vooa1-zKLy-YzHK3_GA67K3cPVDBYYoV5WrFwL8tF27mep0RbPUEDCD62Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JteruLBd-oKhrm5xyL94HbT0NFrhnmTWfWpFRzU3e1oMnhoXLnLWE4qmekQCbTnASZ6Yf07DQFy_w08ehPAXv-NKaH2VIr-eOodSbGHhC0XfQMxnN-jqt5lrSuNH0tQuSf5bStco78a0sQiUJJ73O7h9DbKlsoZl8XKm1TyBONTDZELD0m-SKIyQqEbP9FFFS6a8PnmtilM8mjDPaUz_-b2orl2SZVNv1RBjcgjj4eTS0sJSrx5xA7CYn6cKE_aY09KSuUNtymWIx3U0v57hk2gg3AtzDrFtIinrk4W6m_VaijNvaEAbWdDaQeM2m2okwUOzNVbcCvQ8tsQYTHN28g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxKhbwQJqJW7eDd1loR3tvZE-aSQO5eHmLlOnli8EfOjTAYoQPaWojLG4CcPL1E9biLodvJQFZbFG0jvzGzPErIOgrxn0egs_WHseloxkFpsO6PF1Oh08wfRcHB0y575a9s1ilf-cfDqIZ0eUg78q85Z9uw_sB0EP-GObeszZX8kw5z6Q5ByPKuXNKWVzB4LOpsAcCMO22FkQ47lqHx1BEODUZmahVnSXZs2GRCXVYXSokiYjBSMCFY48fvq3QpJE7KzY9hezGtF_4hRyV9QuqxEDMTsEg08P_mkHk_HKfM1N45j5PJXTK8DlnphHs7mXoJ8zXkq7ErZZyYmwp0FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXZSt_lMAsgEy5wUD7TdCamCPzXI1ZJsXqS4T7e1eO_oiFUTDqTqWBpsSJJdiHkVLJuh1RO2iHfTmVZF_YuO1X8-YksNgmyi_Czal8xPQ30nfv0kOxkpElwL0q1K4csS8uBU4wRS0P5OwrWAIgNQNXAlRCASKjjPlaIh86bGacPGeI5eg8LGL5iU_XPAH4qzS68OWyUOIZI50X5dfkviKhlJYR6jmOWFcXYrwlX89Os1ugTDuDBJFuUPCD1lUEKz_PCvTrTzYnEWcX-FhIyfnwmfjmfR-aOUnNe37w3550jF_kGwFGVB9zS2bNIzYSRH2HB4LypgV_zWvTcHzXJ9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaL6FwgudWbWKHsWoYrCkMHyzxc_CQf5fg-1aqhbmq7k62LU_80HF2SE7nmhbOGby4nxT7Z7u7N2ykjLs6Ss9nwWrxlwLxKj5PXEC3rCxcVU3GDcKQr1K7o7V0_y5KgRGyB2rDOgkk8Gfq98TcUZNu943Jg1NxtVcSMOtZmyaF9QFFsxQuESU2tR1aAIg9viqqc_WdgR-UHI-wQ7ECGR18Mx8mxvKAPKdrHo9FiDnNimzqlzRnq4TNt3fjOXjDEYQ1PAmFsjVcPlOlgNZeQL37DhjfRoXXGw_MoKa6t-HMmUXvfThUlCJpnpUac-ZWPw_DTOIerN2glYyLQRdJbLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNJIdf-ELWv_fwoPpvsOsRaKj28yQG_6IkKnmNi6IoCf59Cw-QUzDBLQLxHTwmiIwFgokZ146IKqqyYxA3BtPLfIc-FceNsVBJvvf6g8hFbSG6DSGhnUG7PshCu1tiEh87M978JnUl2JfCN-FxW_ll_s-XIgptEtiAQtH01_fDsQ66RxYf-0ZQdDL1UXS0Nkoac8nOiaeHeiI7IfTmaiIwRzSYrWaUD5wNo6wewDOk_zEWN4d0nHhjO8lHUob7x6VP8zb71vPLdk2-YtcqJPVaoiGOmBYWRrmB95Jn8AWe5Rp0VDnQnx-aB-73QyZdSkOUmDI7hTEPHbv-VyMnNptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhJWksEUeFjValqfREpSDfHm6llvlBmlGM5qEQb2clDMaPzYFx_geC6Zgpshv1UXrkoYjhnc0_UiFnBkQvYL3Ab-fCNsIpa1DkQGKKGnttNFMmu7py3h184zKZfJci2wBNjGmXTqgym3z_gO_OTSkrQyeudKwc33YFFQt-OwyrK_IEloQmNh1iXX4ZV3-owOeBRNHFG1gB8tkzjezK8bZhkEM3akaVo_yWQ_33gl6PnCj1zrz-TG4MfUL49DwQ0ytN2--QVp235Zx1J7QMO03MCsO0Qj4tvEjqBCEJGevw7fpsbwSRYDnox-zblrkgex-gBL7-LGN-WS35zoPKb6GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlaTLBadUuOp-8tnw5-7hqkUKVtmN8BraeWDewE4-dICAMYnQjWom6OBUFCVxmv90jz3Jtk-a3Isg7DZRcVJ6JmJB0_y_lhKbtKnMLGIuvlZgtcITC_q7re3uvsPL3hW8j69VG99xIdEAS69Se7pLF-RqGM-r7maJxRRGLggXcqqARO3_bRPQKOMBCC1Om4qsOpb5bXhLDJcdybE72VFzK5OJy50t0j-UKU1ZJtoK2ZCq1Zh6n-8Vh3tokiDj3J6Re3mvuFaXAinesHZ4XFcwkrK8SEpFHjfreIbWxZz4La2aE0IOyWemxTLe3FgyQHQUWv5X2ceJrgM7E4x8Zpang.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNBZQGRmAikvG_6MFwNYfE4s3qwgeZrd4Zzg__SVOYlnDqDNA1YjV8JMBYM7de4JwMpIDN3_E6BMAaCU3kX0ddKjqiN3o-Cve75Tmy4o1tJQHzSRtJ70TY-hFfI-gg9pvZ3PlKYM1EO2A8KaEFybiMi9sdOMdwJUZdJFRBt2n7yKKlVbVzhw6aC9GXOhYOB9VoJnAG1CIFRIiG44mszxdBgLGm_0pLfbjEFXQwDpKa9BwbY9iXuXt1mqB_zsPDvI1aw0hkXCxFaWDbUAstdt4vAUh12lHJHyJEoLflDrZAv4wz5oudlg-WN_JS8bstn72GM37kWsZCcltasJaT0q6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REUoGj8uzFWiSVDvU_wb11f6ytKajrY_tGBOvTKrhO2zOdLSdE_ZWlkDpx_Dp3_dRwYsf2eQ0uz2T0lcUy0L8AcYjQmcNvfIJeKPqBvcck5TjZr93Iy1LFUJi9IFPWSUrPWxqq0W9a1U4BFbCTveOI15kqI8zUMFmIYxZZWiT74tt3OIRXPy7reN9fvqCWmNn6KCpsrCZdk6PS446FV9DJn1NDww0RS3wkORYKkSpBb4gekqAHvPsXzZJnuEfXMUstLYdfGIfOXxXvsPP-reBWppnT82j4IsEuPOi-EU66fPHhHL9NmOiRpFMhY-VDa1XGmDa8TtPJWl9dxMNf9gWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6U75wuoPb5g15QcssGa_qzpc1wqfASeF9FL-mK1dojaZ8cDYkIqvg-oRYcTyCQvXZrZWBcuMtlKyZvcGisIh-kFzG9Ai28712kl_2KBfVAVEHSDR6-umvn2jOltLd1JWQhBTFwtp3b1YmROHrXPfmd0S2-aKg8LHOsVybtthrKDv20lf0_Lytqu_4apaUm5xopDascYd7EjT6N1qv-sN9eFrRPA0_4mJ01zrClk0bkIZhpVyGif7uXhACpgjn9knG1fUIsApkGBabGAC9PiyX8o2cAqCsN8CQVsVMnRJi5ukdqZ5JXKjAs5EcEdnEh4A7q0_O2gSnuRShCaimVBOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGwEbYSLuvsK04TYVXm29QHUuPKEhno5Tmuv1WaYDabYamizFwzqYzX6P5AQS-g3r2ovwXk_PFW58WY9OPvcoKUEbo7ethuDDnf0h_2qiENaGz5DHElE-xuGQCdtXeOlVq_upiXrATkR05Nrg2szok9dbi4aOpczTr6JiTXn3Zgl6inmmGFscr1nAyWtMTjJ6UIUNRBKU7PCHjwT2wMjajkuM4ChvL0z-CtIxl2AkIyBrpgnkv_oI7AlZlMb-tCrR4P5AKk85BaRIT1dbl89r-Xib5RjdoSTCiYvUxUC92ox4nrIlJOx1v7C2lHB_YsWBjsLHYDeGJTtoXGTMckIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2-RxqomBIXmZcjYSZEAJfWGS46aEANGx9rYPU3LwFAqYaNO-gJGHHUJlDZuc__i5qQLm2JNFrfjtw_mY9cCe_nXPnFPpuzotKKzTBPaZIuK7lJ2D2_jWEKak0tNMOwwLWfzScqATcJWPG-oRQH5ProZeBSVhF_DcYC9mMwLdP0JCfaNO6qe_2hqQOYw7SwDvVIxKWRQrErYRh-LREH6BMW1_Kxq5Tsth75i5rFghycbAhMQnzbll2YhM-z669BIT8HIR2yH9y6JI_d5LVUuy_ySifl8AdMpH2LORuGogT1R5YR42hx1aP3VP8k8vRvwO16BpOr4KvQsgT_IlUDg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzxfOTyXyICucHbQOO2DQmfrEIiKsjdRJpuRUP7uAXs4IKP_HHPWeFi0qeEhnMiqg8Hoip_PnZcopvykUqVb6aOrblt0-pF1NGgMn_tM-9RzAyyxQ6faao_Wt3PQra0tjFYufaa9d2i4vQr-_KxGuKNq17sJ0ZSjxeD_tF_kaqmUBd-CHebZIuIEhsP4I4K3tj6BDiUFonxARjHK3yEwfCIA_f2bIXGOqGSOuc_MdA4SGPn_Fh5_z1fmtQOoroxtw0m0KxDxgUbB8QT4NTIlNf5TK0LZiPjkGWm8lQ4WuF9RBRLsFHCCJRFmDds53U8wByifdOYPkrTHqgVvPzG60w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbtcBs6sZZioXSUpjPwCJ0CU3QL42UC9xjdOD7-pj5IzsqSwS5bFPUFUJm6Fnqo62eE1juKD9486NXFOVnORCDQLOOHSmqruJQjlRHMxlrYIDRnJGhh1Zlp0kZ3pmxSaOrEiI5mGo00XSG4uOs7rAlmgfd3K2cPW37p10XCiARF0rESYNdPuTdBYBAMp0mPA0EPhvGP6i2OACG0tWs0py5k4tfcGBjWGpCA_60Tuf3njUBWoOBQcSGigheIubIGG8ji8OSLEE7YJSHYItFz4ahZf2oFrlg1ObOZyeYux_jaiY5PgZzPvJxvkqcAkUa4P5hchP7RynwCaHEP0rJhJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0aLjZx0SU31RBQAWALhWUHwsFqP2I7wJz03yELqzhOcxS5TI95FIDtG2QqYx1q2t7vgUDrx-TTU4D_dfnlxqeQhK5tjY3ze8TqFF9Aw9FutCYyLzv5UDNuyk8z5x2fgOL4IbafPSu6uG3GEDFjpkC2pA5h1ukGAadYr0QrcdpN0mpdexcM-4iQoIMwwLPP42quEBbTwAv1OCNQwrLw1OqVYrYdGJW6rz0OEyaS1tqPjI80ONTQ_5tU1VNAmSMAQwm5a1Wl7mvm_d8kZyFJw_JLTKDWOK7er-g0eWz9irfhr00nGGdiCiR3fxZAy5GZ-rTvQjEOijIs4y3x1DvYRpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md1RU2vn5zQeyOyt3aSkT4B4gUj1iR9ew8CwzFBbiz7rpew1qTNH7sX-vzQEzinpCLoOxLMvDwY4oU2q0YZM7cDBVTiGEhNkJSRcGaWar2eiwxn2As4xBuogYJFksCGovZToGMWFbbrfhq_499uzQ7Qbx0Kh5mfXr0wgt0Lra_sd9r41rfLlFJhMsfK9HkCBgnlR11cOVCXzFWdkq0CHLdKq2rFfwYCEfg6w5eHPjgcfnDU57wdd2S81f9itBbt4sW6x3pbJpUi2hWCP2f8yolY6Zq8NlQg9nOq3iOzAZM0_MmOyMM6-WEKrP2fMAbs1n6WbVvpIdViwfE8YAvwI7g.jpg" alt="photo" loading="lazy"/></div>
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
