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
<img src="https://cdn4.telesco.pe/file/NyyQXODx296Ul0I2fe8VnDpI_XRWPIvsSadZj3VH2RgQ_lsAIpsETtXTwoSkZ2uIVOvQXsXqo7sPf9Ch0Pw2iSwBTpizLjjxjoeTcTU0CzHxEl72fcaX91f0ULKcdLlW62aPseQCCvUf1E7ZB1XpGYOja1lcARX6Wt5LuXLT00KkkerU2whwt5AS2vNCJmRMINAp_RqXMx8oPlS9Yqb9BIlE-X_NjOfJtD2pbS4-bM8AaiJs6CzWTOPgULr4PLPsQBUHLrt3jiBvlJE6hWXItothLRiZa3FZZGCxn-7aSbDo5p4VQXmSeM_wndMETVaxQHOxwg8voTlJ7hLf_6R4jA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-8075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6lEds4Ss1Oe-N7WszB9Eyp57Gn5Eao0G6ZaLRFJcDYCv-lO1_pIS-_dry-6m7_X-_kODSi_vDpm9hrYItWCcvX7MB-6nh_DD5F5CD_Ob7YACXkWqXlcxUVY9YcQB08B9MClcywPlfTChQovLahk7E-T61QR0hexDEs31Z_DDOLmapqOs49dTLpAkS0STaShkM7YVXO-xthro-qBPlpMeDUnwG2dawHM5yJCTzuZQD9Xz4EuuWqk6zVn1Hwgwihc2j-OE3834iG41zYrxAwv-0p09yIiXmQiiKW-Eber-tr2lo1PhnoLbBx_VSmvcA220eEkN_6mDMyJUKSf0f_CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💬
چت تیمی EdgeChat بدون نگه‌داری سرور
‏⠀
‏این سیستم چت متن‌باز کلاً روی زیرساخت کلودفلر اجرا می‌شه.
‏⠀
‏• گروه و پیام خصوصی و صدا و فایل، با مدیریت و دعوت اعضا
‏• پل دوسویه با تلگرام؛ هر طرف از ورودی همیشگی خودش استفاده می‌کنه
‏• نصب و به‌روزرسانی خودکار، بدون نگه‌داری یه سرور همیشه‌روشن
‏⠀
‏نکته‌ی حریم خصوصی: رمزنگاری پیام‌ها سمت سروره، نه سرتاسری؛ پس به محیط اجرا و صاحب کلیدها باید اعتماد داشته باشی.
‏
📌
صفحه‌ی پروژه در گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/ArchiveTell/8075" target="_blank">📅 18:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8074">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/8074" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8073">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/8073" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8070">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/8070" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8069">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpqdNIkw2g7PQbwroLUCjw7B9D7Rpb7WFHhbQIfoeHHjS5aOVIjbvuKzVpye_-VxiUADfZDJKP9p3T7qYgHbxIGZxfERyDKrdoyQA1AiEmLdBk2et9bIjpI7etiFOti_nbWrdKDM_cnXROiDgiHb73iPSvL7ucHZrREtrFk3nmf_2x4aUf5UGXq_PVCuKg8nTOok4YO9XMv5VyK33-q7mmYqJAcG8W93rGIVLtQShK_NaV45Ba20VXxqItk5jxQIASzWaJ_bD8XKEMgPNl3WenTOtq_6xrvUo9T_JPqClaPKB7GZAouqoTzw8PE11eC20xmMEKtI8Dfk9tOznfTDbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/8069" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8068">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nQcRPXmfHUEasTt9dreG4OkoyioskEgg4LzflJoZHpQKtaD1-zcXknltcc3RxPsYni4qHohLZ7vRg-OuV4b3H4iSn6gcKv3xcPkUQvMuNJ7-CGpS1yUplqNiqfSLeFPP3qw7lZySonr2sbOF_W44bByuKxxgfdPXQORhNwB3qTs1RBNNJ2FYy9P89DkdSXGvhaFyEhXVt6hcnN4M1OVsgMaGjQq0MCJkuRyh5lpmVIVuRCqx4lzsuxaG3uQDMp98FVD6VcluR0x5quyKEZIO6Av-3KQeaMiVrF6xYy1pkT02nNB0ZObpWSRN8q1H7YTdZm5h7ENmD7Sh87Qsgx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی GTA 5 کاملا رایگان - نسخه وب
https://gta.deloskiyt.pl/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8068" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8067">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/8067" target="_blank">📅 10:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8066">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/8066" target="_blank">📅 00:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbkHuvhTA49mnbBw_DoOJoqDqdYuxeseNCDNDp_W7iOJfBoh_Pp1pjCE9gSYjM_7d-y3E0IBfpgNNbSOAa1rLTVge7qdicxjGk6JdyMqNGJlfdZweeP6QWsWfQj0uurdJnDGCDkVbnPH0QNbJS9PmQTroHe42tM71cafHVkArFxU20SZuHaccp9XQEYXM2s3gckIIrnh0vi1M4x-4kJzPXA-jITHjGiE11tsDS58bDQwsUZIMaGD3obXW3W180L-CnuY54UTZnSCDtoI_v-FnK0XCy420Ru-p7wBlLy4YS9r3FslY1cAORExv3LMuCTHESCWvp-PwlQlLjBlWDngcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://t.me/ArchiveTelll
تو گپ بیاین ازین شاهکارا زیاد میبینین
منتظرتونم
❤️
😂</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/8065" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-GnMwLvd5_4H54RSJq1t6dP_EInhaLc2I7d81qTUo24hMkjkfmzwFhHubcTeazyVHOvec7bC0qISuQscaGOwXXQ9zponIkokGYWZhYneCHnchNwocZ5gvtBXYsRBLS22bq_dNpDaw-_R-5t6d6JNSWiX1JPY7E9eWOpbmo6q87rqHj3Mh_cRRYAT9sbXB7i_BEmB82__XtYRJi09iFuU7o-vLbUDg3NPUo2L-LEL2f1yiSxGjbDzmnKt61KFlEQK0cnYHf5yZlP11VlHnIzd-BZaWFMOla-17G_xOwRZEoryOCC8NE7k7YrNlP2403Qw6yW56ejaf41MvJLPWn9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNzHxbMUHL63ZqzCBzSMSUIuVZiRb3SMMaGFHxKjJaTb8oiZDCLAPhfU8qGxHFF4cBeddTP-kNB2Rn73w6PJwc3HYpyhdb73qHPKIeEu7Qv_7VTVFo7jjf3XeiAt0jP7Xgfx0UXzPDjYofaTP74z9WWClhL2mvdmY-T67KUfFMUMMgzCfkLZIyA4WbV6BMm3NzxWwbEcoR9su1s1fL_aqp-WzgRdlC5qNGTzUqcRuqY2GVhNwahQm1K9itrBM8zaRLr8Enb95hyOddZcC9O2l9mcovtWN9zKm7MMREkAyIcpq5MEdpd38eoe4hh5zjSuPLnf5gTqtSGRntg4ZDVUNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8061" target="_blank">📅 20:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8058">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8058" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iT9XjzSv6sJ27GUxNO1GLz-52M5CIuH7pzYQHmS8DT9GMQRrrc74Z3f-XAQyXEoob7a7WK-5nl2NI7_9CxHnX9XkjVj1u8o1PtLGlo7TY9wXQB7UOSzuGlC1fb_W_xCtccokKwlMguBDnty0MqKCWQqO-flB81-wwZGXYQ2q8sbfKzx5veLXVQyvmvA2AsPB7kYRGtdSgde7Jb6N0S6v01fwzs3nohkEtSunNecyyQHD-SR0egeT6SqJYRs32faLwVWxYh4oLupJ58icuI1roKiCwkWR4GBCaO0v_6zOMXMgzFV716EgCfgmD4cf3H2e-kmO1QfeKvJzcN66w9ewUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wd8Kfq7Tn_3hBwmE-icU-5YIlpl9Vi8gpdOc2DnpyHOp2mTxJNnGm03OmZi8vvYl6ctdDZVYdJOKrl5MfOfKGEniV0ZIEf94oiLVBoXln44n7wrYB0CMxBeSWuFxfeW13uUVrbPUVBGIk7j-M-C4qUV43gU9DfEcBQaTW6ysQBjxiaBkKy-TgLfe8mdgPY0jHJvJGsq1mW50IrD2uNKSEAdyP4_4Cfw7FhvtFuJFL5smwGMLTbUk-viG_Xelc5yivWFK8jWKNOfKdcUD8hj4ZFNhFl0-tz1WaRxF8T_SPs6PSMA5espZh5UtKdOmnJg0xlpFU8RR3PAwDT4zYWF7fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Py7MB7AaJLmZf4-cfhelRMgCFETzfaAEbm_IsEjLiXbA4AxUVnSz3AxupknrUvdGlGH9Lrd9k75vzoejMB737hmrWkKHrWbfMjlp6V-SFk3EhdPYNfOBkOGgAasmmoKjPbTii3CFF28faqoA3OjKbC9TxwI5ri0-y5V0vb6FwXu6MaXwbwxAYEYS5JOl0qqen6QzdBZuKRa1PW6yaFkgow066SK3Y0MAMQE4pPdJaTsTDrjT4lHoWnphvQaT4eZIzVExsV8H5PpC6feIsASp6ihkSyNV6RM3El16QcG_NE4CnzIIKZjwvWD7Z_FtA8myogIzE2RIQN9aX9v1JoWINQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=GrsCZEeY5_pDEPhgx-aOjBdEZK6A5g3y1c5O4fvG7STxJo_BSUTHSP2xjYt9r5SfzIxwSzkvW_Io1a0B2DsND_Tpq8d_aO63A0OfO9o3b3c6boTADsjNrVa7fFJTkRB5iy0DaLvydJPyR62593bNJFnBOXrShqDVqzbWX7bNviITeI2WkX9N9OHCFg0wNzZmyZYdAI30wUX0_VkTc3xgw_CgUiowxMDn3fTc9o5gdhhxuk7lIzsgYRPlSW9FiZsoJFXfAWQf5xCbP139xNxALJbhQZVzuCkDjMwceVnnLwGEGAOvojH4qkzP7dRKbop1BEN9MI_0sHTTXFU77oG50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=GrsCZEeY5_pDEPhgx-aOjBdEZK6A5g3y1c5O4fvG7STxJo_BSUTHSP2xjYt9r5SfzIxwSzkvW_Io1a0B2DsND_Tpq8d_aO63A0OfO9o3b3c6boTADsjNrVa7fFJTkRB5iy0DaLvydJPyR62593bNJFnBOXrShqDVqzbWX7bNviITeI2WkX9N9OHCFg0wNzZmyZYdAI30wUX0_VkTc3xgw_CgUiowxMDn3fTc9o5gdhhxuk7lIzsgYRPlSW9FiZsoJFXfAWQf5xCbP139xNxALJbhQZVzuCkDjMwceVnnLwGEGAOvojH4qkzP7dRKbop1BEN9MI_0sHTTXFU77oG50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X39O4cabT0e0jr_G5vUYWg2Xwn-MzT73QE3mIjbTa72Lbn7_E2FD_ffWekEA4kPloeT10_3vjM7mp2ko5pVFAVZ2mellVJFdf3iGrFJDXv1Ps4Y-nBB38GTcHr9PxDpKZilDxqrY0fLuXlkCD_lK9KOPpEJsBVG8boezLkk6tGf_rHUKnAh3An-tG4281gwtKeYL7aqzoVxuLHkhQKPa9-ysj1eABFiikoev9r1Zm6hdze-BN78lYJXOcKrSVEm9U5ymgAo-wyVYQWuYA-yhHqk2PH0rwiSpLg7V6HQtVGpsqfw6WXE-5JiX2-qGZk7rU32abpCzdKu1CAQkASMiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpgIk8dN9rw7Ho_r_CzIhXdnlrYunIjjpBQB8DsQDk-sQJguPz4HazLRqjZ9kCqNvafTdWyTAnwCxMJBQ8XOqkaMmzvaMOdERKO1ImSM8h9rVZhUWKi88WmpAubWNtXRM0MpOEX_yLcstxUHwucE3m-XYH2QLQy_axB-eizXieIQCoXH5w_1hPUw-Pi69EvlnY-xbWNVlaHzBHhsi9OycmhMD12fXN-TGS-5Q_xLzsRZXfR0l38YpXPQkALGgmNkDTOJtPfmCi2sfy3jO1AzgdD2A44onhTv886K6hnfwjtKQygvAUmFnphkqiIUCAAtK2byj6Ka17OymZwxfevX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e000VW4DSxsVc5IitMEu16lhV7Y2dokRNez1OZ8mbv9P_L_w3lQqRMYiRDnVKZpBsbXoX0_Dvl8FUs_LO5T3tx93rMobGzWkcSMu4ooM_o1YX5e-ey8hlO-4r5IY-0UsKb5QBQUMJWHxCPYd5PA7CrEUCH6DKgHsk_yd84qJXh775S9Gqqq_84PGrH8LcjInFNXZECNTgCJRcy_PI_IzfSf-kO0kDdW90Cp18NYyW-tmtn665ZjxUo1uJxp5CKtYSV93Oc3FopjEXmCwd21K7VUTgU_ZgShekjpiHM2LZS6Q_up39XlCOFlvor2ismcoYWPb9FBO6mss5tV4jqq6UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvI3fZejrDHNQImRMB1_nGWEhRYnQaY3Xd5v2CESbNb-L8J0SR3BFlOqaX2VEqgBWfbSVGy7LqxrHr2hwuK0dufr5Sqe3uX0zVANMC6YL4h3NwrzFJSHalKkAAB7jIoa0tQQ4KPVgi99xOs1GVpqyfKm3fSCxyeJWz37ocAnKhGxzdBAroHWSzGiv1KE82nsfBoUSsaq_0tMPm14dd6BA2FtMXhJuzggsBvTEeIcSP-BPD4Xt4b8p-jgQJcT3C_DwLLGYto5NmAAhZx89FWo2BTTIH7F8fwH3OE1j6ch3Q1zS9dddJBuCTRJQ-E3FApeQftLvPSFYm94LA_GhDPhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2ClwyM0cMgpGVwijtAipgIF0jnyfpPGvsrWykpKyB7rt9RUtYFKnt60jS1uCoULi_RJYhY5rivMm_YuUy0fYGJ1ewBt_uEfCSJyEeyefEaGXUCcIk2-1p7igtRo8AD6y_I4XLvW5rxlsCL41KE2vwme2RJjDeXS989OhsBG54DuYNx5pelttyelHZ-DcAgnoQyNLysb3ft_cSL-ytWkxOj8p4uFYOa76L7eqLUTbNjOuJgrLAyzGaW2VMJecw0NeLPtpeFzt1CT-1UDscuYLuxr188d-Q7IcQVqEpw8jlORVcFDReeVLIgSxbiQI0vgMbaZF7j-Z8z93t1uyFko_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RDeJZbpprCVtE5pb9rrjLs0PC4FxIoQWRzu4xtiupp6ovgyW6zVW8WLyaI5dNhnONpEVBhcB9seSJt1bgWIsZ29auTTTMjtsmN7LLg4xTsm0Zqq4bkwlZ90lwB6MmYyU6hQatnNrckzKaM7N7kqSG3nIrlkpg1fsHTwM3sfq2a7b7vmUFq9Iw5VQVZnmnol7UN3lus46FVdzIVub3KSgqHZ2qcMDGjmweP1iL9q5kfX8bg5wpMqnBqsnStxyOTFtdQuinNwFiXVB6pD43R7m6LJ6deSPp6znN_bob8PTow-RN4KECsjeDAZunico5roeKfVduZ0pCHPztIXU3RZiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RDeJZbpprCVtE5pb9rrjLs0PC4FxIoQWRzu4xtiupp6ovgyW6zVW8WLyaI5dNhnONpEVBhcB9seSJt1bgWIsZ29auTTTMjtsmN7LLg4xTsm0Zqq4bkwlZ90lwB6MmYyU6hQatnNrckzKaM7N7kqSG3nIrlkpg1fsHTwM3sfq2a7b7vmUFq9Iw5VQVZnmnol7UN3lus46FVdzIVub3KSgqHZ2qcMDGjmweP1iL9q5kfX8bg5wpMqnBqsnStxyOTFtdQuinNwFiXVB6pD43R7m6LJ6deSPp6znN_bob8PTow-RN4KECsjeDAZunico5roeKfVduZ0pCHPztIXU3RZiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iADzH0ixthSVRmZPru4e_WvrPoRj5PgA5JXCogPLJVRBdnnkq-zRSX-n0aj02rR2CJjqJ1SXzzEmRr7Jnj0ZS5iGBlzKvil0K_XXBOQerwT8eGMFDHfvJgcos6iJ6C8YkCg5nOe_1IEckhHfINKQMw0IYMfkd2XK75TUp7QP74GBHWAhOMiDGbpbFRCUdMaSFOnfvuSzDfQJlrZq7_aHSr_VT9dB_r8X7XiX7odFbNSaR0OyqZ_Q5DgMwYrlWrgVlQsPjYmXMZMVi4M6UEJ-u2T2oP5UHTQiz1WzcailmcltSGz-O_BcS28wd4Tfs8hw-xXl6by0dvswsrY2E5v2hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhTJ02UuMbusl1t1DnlMoG7LN4NFdY10X1rN1nEmNZdhYHTq7VF6rJCoXQRwGnVFXbIlq7Qj2bo0-eGbR1q-By2EbVohyCNoJeFbQXHo9mI7FdkjDXt_gqHe4-0t2Epl1iarRRTDK43pFVW-JrfbyATngVQ6HH6grg76NgeGVFVm6YgKIrt5LfpFqBhrPOIcxPNSazhT_TUGSdjCJnyiSLJ4f1V7ihHNL9v4CvL4qpKnP6qyJo_yz4KZNCdooHKcahKGZLmbC3NwXnmUqym499g-6F5YFfADeyHgANcbh7S5y4oSowFO8Zou4SGVPAR0_tHVJ2TVT2wIL6Onz0TAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8dCLFjiukaVxcemlx4w_e7reg-8kP158qVO1dsVZfxMT-uuir-pWuDvj_bymUEQu0BpM3MYh6ersiBgogjJiTeDI-GYWA8gsSeFYv7mWhOGsESh7T_r9K06BrFO7GQM3V969QYopI-vaYSfXvkBoAmF4Ja0Uby_aa29MguJYeOmFYrCS47tAF-9C0NxluFadyAqJdw_kmSrZSR72q6_F3zuLjA4Rg8BuVH6hAJkhbi1JnNhCYD4sGiPFMEHSJtk1bhJpO8Vg0gnJFHEOHxksL_4oAdQlRXpCAbp_egKrnuIfjrjmflN1e9QHrbQxRiHCRjYHfRkM8r5ZjWdQiTMIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=Jy-iKYSNM5L6bJMH-Pnq_C78dYxSa6mY-cESYTKCapT2P8_KpZBkFxjl2mGppLaBs6ew-wS7h0LByz70PVsklBdmBMBSsb3fKTjDZ-9obF-a1mndJPxjLybvPkOBnpUjl4uXLrVeFO1U6R8woWh5bgFmpcDAaQYhmFNUEBXjsYt1yQdkG59eGnPRIVuKAj170LErNfrTBqD_m7sNKRQpXbOfuSSbSQRpk3YBjE4HxDsRZiRbL2rB1RuzsgunpMoyJYaGV5NwzCQYIDtSI0BvAkl15tAPvkvyMJMGs9tr36Ynr4RzpMpIcCecPirQmbGl6L30ixYGZ9aNLcA5ZBrSzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=Jy-iKYSNM5L6bJMH-Pnq_C78dYxSa6mY-cESYTKCapT2P8_KpZBkFxjl2mGppLaBs6ew-wS7h0LByz70PVsklBdmBMBSsb3fKTjDZ-9obF-a1mndJPxjLybvPkOBnpUjl4uXLrVeFO1U6R8woWh5bgFmpcDAaQYhmFNUEBXjsYt1yQdkG59eGnPRIVuKAj170LErNfrTBqD_m7sNKRQpXbOfuSSbSQRpk3YBjE4HxDsRZiRbL2rB1RuzsgunpMoyJYaGV5NwzCQYIDtSI0BvAkl15tAPvkvyMJMGs9tr36Ynr4RzpMpIcCecPirQmbGl6L30ixYGZ9aNLcA5ZBrSzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZuK2cp_aIfG-QfbI4k9jVWA2e5b_y7pZ4mm4CEb8qlJgUWDGSyj1vVFLLW3wDRcI8_S9h0kTs7S98397mlYgLPjNblmKgnKqMWHse20O8yaaQ3bPAnGW-Rizmcgbs5yl51Jz-16X055fZzV5ngqg1utyR4BK3NLzvsoShnc-objsAystO4gbMzuseJgjyRwWv-wPa0CFUewzvLiwTj7SAp2SXRp9EVfY8nQG8PIhIYPOiwgJWXI-6ElQAoYUEHfdNUe-kpqSKDAfROdLk9RInOUqbTXBdozlZZQfO2zpwWzUftJzY4fwsLG5we__fFjTbEvsJirY6EtVCMp54jwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFHSuQXR3oEXHV_UwkStnvoPWxXvl-Lq6Gx1hYlAqG_4ERe-PB1b92sGACPQ1cPwvP4wTLsmj0-z3DDN2uTKKbZ34re_wjnrrHdJwrQ-2HY-zGSO_GRDfBs2qD9bjQjj5_I3oaif2afY7wNkCfDVI3nqmqrK0OAIoDUrSWwKqk93nkrcWA-UyAfRkF3o8Hmope3Qu-8sAs7Zi588jmzpn_10NqaC0POSY_MaxCyq-LJIn6pe6gt83veJjnHLskYL1qBA2wexv00kxey6Xf3VImsQfPNtgggfhmDzutD3fhmscP8wObdDEj4ru47kPrEcmFg0BFBwObn-QDwsoNhsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hls6dqMZqZIex-sXZX_GYMKKtff7OMPDpkBB_p_7uJmBTqQ4Pw4MSzV3zI4lV8mVDk56k46fV4YRR46K7AH4QMZPFTEpJQ6NABPw8fkdxVJeyxXBC8A71w2jDICj253zRvApnvKhkEGS-p0FkSmDxYUdAm0vXzPtiCPCQS6tyt7mrL7vysisOE4TogQs4fXQGA22MLnRiy2C0-oN-cznb4ZarOhNcf-PPFw2lq_rgLP_dI7hMk3F8XWfaH-Wi1JbHb2Yq0KudY5Gye8OCya_3tbtvK0dMmNBOYoqnOAv9_diXDWnEa9B3fmRdZ7G-al0k3I2ddmg2MdmqIlILGNzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIQN4aE8ZwuI9e24zRA7lMmExPlTRh4uWQSBaX7mVZNslEcJbFswKa-fN2uTP1lMQ1gObBr3OTMZ8XtT80NaClRlWRmfwngYl3hkB5GjVgl696h2gg481ttK8v-15Esu1QqYttfh53WAsahGfuSxoV8gI7wt32HAk2VF1NJPMxh2EHPimLcluwYQZd-s1aMcPD8vF6s3lTdivL6wuCynu9PFjBcVmVr3HgiowdBA4L3deroeihd6N5ZOHZKKL918PfWvqXbm-Uy5sBlggXeeIfO-Sj-bA8AgiwG7a0wJ2lhoJN5fXzzbuWMnAOzSao2OdAxv_at1cIHJVH9fTmhZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_bCX_dV6FfXUe7uV2QNZhx3NCfIgvcguzX_cryI4pLvT0mACfJuXG19exDNBwfFFGAjPQ-Qf_b4IA0kJR441EaT7y1t5rg3I389o5ABYtmO0FbZ3zgpZvI1wSzTh19dXAiDBsnkfWW_7zBQvjAGgtwXk1tJh7C0seu6UDwBxajBdFG8L4d_ZbfZvZE5NRO0ONOAecqbQxyFJNZFzAnKsAi0GL9XBjocB7xEU1iXOH8n1lVVRl7BptGO4f09A6u6LU18kl-ghDyY3GCsshUAAOQUzkKq5TwHtE3GRpaGGwePlOnTzCX73elkgV-onPHulGJXstGGUmd0ggL09L4MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gls-J3jkMnPMPcShTlAKthsZaBT0fMZ5DXSQs-K192XlRHMEV9nxPuigta51tvmn-YIwrjRMbDmzwCYAOpSMZp2flGFHf2N1GhZNdmM9Fzm-2VK56ODjy_hkVMxvlJxIwa6Wj6PBkWcV5w_LALhA03cbkz3Y4xrsI3X5oyULdoIsJBfKtFJy9oUfmun-uZaobq0SUew2c4VF2JV0EeiLjvR8b14Km5p8te5FZwED-aDzEgA8cW8KPIrV1aGWiJiAuPmdpXBXrMUBCTgsUt5XEGigU0p6TnVSULwuJ0PpXaek85k8_E3hNVRKVoqY4KWkSArXrXlgNN56j_ybfoGL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B04WX01afFeKmDvXd8rBRv2pti8zeQivNQKuJjB9prKOEyt7pkW7oXwBZl5titbFW_yTGHDZjONy-qxtP8GVHt3jyaQ9LYWBVrVK7p4JHbSg1c9NIpfb_wo1PQONpWrtWuh2cJZVBRVaJSemTAVPljlchF2lWVN33mEpYSBe1wDmob73nmt3ff58pZ_Am6JjTwxkdXvZII77yhCcw57PcLSor6i4xegYVtdEqb1ZflawXbcFcMFVN9KJz6zo9i0fXajNvSZwKyCocC7rKPOZwhTzfD5DY1kP7PhDIbGXowFX3DpU7UvWsux4eSt43sGBhvseueX3A_yEQstWJRGrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhaSVASMMrN_XIR4c7qQgN99R5H9-o2BcIknRpDC5--GISUCjk6iJepS3gNH1JlzglLdO8XtPxy79HCF49oo11ZiuoPZAqYH58hF-h6N7ED0YYKHRWLk8u_zzdpRbJxqFNPOz_TConwdfxYKaC-U31F7hVXknVUxh8p8Xk09q9yC2AXdo0PeU10nPp5mF5eUvRM1QL8_A-J0zh4nd1G-wL4B8WR2aMNRPihrFXap8fuRKdf-0RLC8esLoBmdaFh5mYEWrzqa-QI_8hFEj82o31FKRpJyhg_dlFo4skqlCpWLsKyQWzde7C_do9vJ2BzEW1NB2nsoxw2Z0S0yfn99Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtrmjcaKKfzUTJE-aFxOHcqpNUdiY3hfbZQMxa_eVQf89YwQwPT45lErqAg5gSLc5eOM9P8G20NCMooefkXoykWJx5lMrB5FhTCjbCoTJAtf-ShplaR63yX_QVYTr0Z6HhDRShntCc2LPPFz3vIqbvPGhGgJ3NBf8aPkaXy-qJZgmoxnej4E4sGXuUg3ND9idfz4Ne-r8h-NAVgVMRCY8DkgIBVJv7buQTLDBxdr5h9kJVshRnxJ0vUpJp_4ZDbpLCUMex6bSOp_0IMbshd8rx1cqsNQ82CV7XojJ-9URJ5uRkctrgywQtvJK5eObHMz2lSYmU2RLwIgNsEuc1sWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlA5lBA1qt_Lh8RqcnbQwihz22jMQ8f-OdnANct4_0fHd3StZGXq8wJAwsW0o0Bl_mlc4_6r-AJm_LDNio1QGcnjD2PCeN16Zq6uN1mKC8RcCzuFt8Mwi6GMNi_pHFrBm5-d2yGYmi4iBInYaZJ5OSrzaY8fouqP4FJj7So4_CcsXgWyPhBQoreR5et3R2G2TBXqdEkFFJMq8WaQm6mCvS9R0YEiNC1Y1h1j0gggTWynOeloq8GAQWPOXqxk7exY9_VO3R-CPh144tmzP88EwbXmhGgWEa3_2HqgUFbW_wCjdZJgESN6G0S9dRJkFFBugt4q8mUVrEa8v8hI848YfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISrw2AP-98pc__yxpfbDtVowYSYlE7FpmydGEbLcpeSK9pat1wu-cq7UbFVwArY4MwVoTwFTo70NP8xj394EXWcsrlyWY3f4R1mYFDixFZPYc8qATDea89IOTEdJfrFJ--EJOF0VegnHVpd8HlIQJcTdb_Qy2sNMfs3Tk701n-Vn4l2nk9jgYBsQEFOk8NXZnjKfpzuRIrhyfdz_NcOuYso8LftZwtbSaSI0DJpTDUPQHpSFaZNDsIrPVOv5ygqeKnsta9-jPB8H3WnsYkoHQZdzTHWBW5kJdDFH1u7gvk5OeTy1GfmcriGg3lRc28jNSBgnYG9Jo-MLnKGHWB_7zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux5j6LaAzKXhv-nWs0n0lz6OvCzy5B7ZqY7ka6HWdEeXfcxJqYtcpF7EYMXdbWMfFW-cveoj50_yLQ2e47SrkuoAf9HZKkqKheAdUAZviwE9SD5OZLu1KMr37JoztaR_XCAe3Ai8jpIDOc0p6_xdeOh4VlCoBfGmtGOE7ZfvhmKCXHSU7pDCSypmDL_o0DXvy_zkcuHe9PPwpOBWG5GCn1ILJFyArGXl16bxi5nsHc4oAKc69ZUjtRQldRoa1i0iln2jcAuPDXkMn53u-hiUuB0MfSTl4elcgwRBtUPcBpxTLQ6N6PcCuZP5m6C6bis7C-04b6DfItDe2DKHdop7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxO4hE47IdiuV35UuwsNdycL_631-Q9pPLPpyZWmguIxziJQUFiBF-95sglquFicuQtY9pfdNkAyiztDV_9QzU601HICn1LfQiXP8Ijvm3qjkYZ38SOfAc6lQ9-viUcz2dLAPbGyR0dZ4BD62mnJFliV69dwsZyZ2h1vPz9q-0weXJBFan3bR8nTLUpJumIZRczXHb7HpJy7j9sKAqLDV-vSJbtR75njx81nqu-mOOCpLqVekYv4YYv781imP6fY20eszdlcGbJLU3wQjfbKnlWYOBKP0IgT6hfm2m5ryePvtqR6FLkQnImVM1VQlAWDigxTj-vNajt-yKey0gEM3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjN_wsWVLbVE6wvGQz_h5hcvE1DAnzehIzjs6kbfKzibLZyD7-dzw2UJ7STqB33vultHgL0jyCTxPX5lJSfvd7K8QcpMMzjyfRxoJiBanSYz_3EbBFJCvYV9wGvtjVWoFp29HNdbn49g09LM8b0zOhGQUEhaQGSA9tFCTQ6Njra20keHCqUXZxPHsPgXq9S3w2wErrYcTzDZiZlure2yKmtNnlHmZ_GVRVcIZ-e-CzwYqy4o4MLUJBwoD-X9j6Yil_ykVpaqiJO1-IVYN2uszp-ic1JCSZ5iiOSvWaMqrEnx2wEwGqfqEQFQMDnRSxqW-ynN2pq4cbONB9c6OZO78g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=vCKi2OgVczsFQNooNrRXyHh6oVZUHX4wJ4ebW0tTyfONwaXX_vBk6BhWbuzzWPfNFdozaVJlZjbGeDb9LLVTejided6eun-hRt_TZmMqRKBfHwgP0x0TSQ1n7pIDSeNJH9jvtDBGR0NleHzCVch25-pV4J0KQy0HtTiE1jBhOQFFi1fJYiIbtVPFBXFSKlZVgb2IfPCTEXS5h51Wpr6uPEFgK0RN7plKSCNb8JuMJB_36NIoHCmtfmRXTSzQqfmF9E_jsuI7DWrH1bkxz_g87cp5v9I7nAwPyoJkCKV6T9DV6Vrol3XfNP6e9TRU_8oX1csTpuKX1madJ75DNUgYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=vCKi2OgVczsFQNooNrRXyHh6oVZUHX4wJ4ebW0tTyfONwaXX_vBk6BhWbuzzWPfNFdozaVJlZjbGeDb9LLVTejided6eun-hRt_TZmMqRKBfHwgP0x0TSQ1n7pIDSeNJH9jvtDBGR0NleHzCVch25-pV4J0KQy0HtTiE1jBhOQFFi1fJYiIbtVPFBXFSKlZVgb2IfPCTEXS5h51Wpr6uPEFgK0RN7plKSCNb8JuMJB_36NIoHCmtfmRXTSzQqfmF9E_jsuI7DWrH1bkxz_g87cp5v9I7nAwPyoJkCKV6T9DV6Vrol3XfNP6e9TRU_8oX1csTpuKX1madJ75DNUgYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgkV69nT_HsMeO-lGxK5xOSk0WIo-AV4PcbLH44sRR_3ENwN5HTsS--y1P1K1G8fMvWjvu3CbENNC33RqDl7dQ8EVOj2XFehswdPQnRZsZtE76Cgg-6lH8JglSyf4wW_4gqno17rrEBwmU5IL7aVn1jr85VB7yW6wPWovkrFFbFsQYcoBhbpJq2tKqkkPuIkvFQhCQflD3c0_AF2pedcjXrn6nj2tTrJiygXBRqF6iNS9tbC6RsoB2RpMe_UBOc24iaoNm78iJfoZ3jiaLjLpiQZd3ZPr3dsuCn6mD7woVnMOn1u_65LswqqL4nA0tYFu6EyCtIiTFFOzVzECVTQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Le-RTIojxm_vWd3ZmyNPzKCjn6vv0QwJb1Gqj7zYJg5IQCUq1kle15fULzmHG4TWUF0FWeVBBDfTlzShzfhbeXQxAHbINHttmyvFEkHspWghQXsVadW1Mey8YzC6Wa-bght4M7gc0LnDW-TSiq-ooMZDvVfAGxuwAbVOOSYUx7eV7w7ByrJCeVm405MM_vdNqFG19WoqdCMmBtX7KCLwEx6KCKQZOJvjnifwqmBttM_CGMm8PsEn4kCdaZq-NbSLUk9gM_764C9kQJvaU1cL_y7q8HJyXAznNzo2tVz0CbaZoEZAymXkBDwKUlcUa2CCQosksx2-vkAabeBM_u1eiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io4_dbpCSjZYK0jy6iinzjCEdyHTtE6regYJhJBjZFPBd9HFGCo-YV1yyVo5FvXGVLS9eGU7jaWmIBr_T_E201m4Y7xDaYQAbxbmIjGJbq3-9lzDf9C9wjTgrnpDxSF9nyHxnrneQt_JGz5rd__ik2bTM4vKWdwi3Son7o8M8s0a0GlZ_3t8EBMbnNt0DKVULSWl9-DgVUOT6z3S6y95GNOHO4LwtfPypC5jtngY8aUyl1hLM2onZGQ3FgEm4S-acBmT8ByQKtO4PhCMB_9CnUKD1mn65XAnikvMs6S0PaknzelBJksgEloTGbyKPFvGqVmLl_0jBwLSYPsLESpoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8Wb-DbG9YaVYN_KuupkQxIV3lmvOEnyWyNL6af6JEPoVkPYyIyaex-XowZwtFRpU3f0AXN8JLGXDPgkliMmVQg2bUqmD55LL0VnGko8RLnx-a4BxTNs_insCvjcc_QSfAHRmWQ4LowhzZ4g66L0GsqbkzNwL-mybQJGzbiCdAa2mTd4LAZJa3ct-BXtjAd3mCyCDpBKWuWmMu7oC3XD5ULDz8Etk-pB6rvqSz8O8J7qpyhqOYLhjCMZ9Gcn75Q3G_EQv7VAhEUSttB_MBOaYZO2eCD6_2DGMuNsIhFPElbzWYDe3dLwxzWSIuhDOAXkYy4B1O9CxP_4W8Wi1RVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6rLnX6Qk2YsCt6hwdmxkYUicIdJuKyI65iRtkd0P1MO5iROh7XjB4iFN-OzJqYJfMAGO9-wgjZGiCH75QU4hWYRhoxw8UN-U8aRQ2Wzq6PVJa0kt37J-ZkN_7QrVCj36MbatPcibCGGg16TleVj-ktGTrrm1nJy5XN3FOHnOEmUjvoIdOM0E3_oeyHbMbW_7d8e8cZRDzZ0a4LUIixjdotACifvVh7IuW9YSwq8gZ6sx2U064pcTARQGbaKesQq3seTui7DpZt7ZUTubQlzezNXIgdTrBdTxVgPHKg8uvc1Ajs0c3Yf9VYYANF02J_6IaG4bmRs-0epvlNOuEQrzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWv6_txOsH13oNWeh5FbGcURCbstjt9DZodZ9oD8Gou5YhcOnE4TLW05knawFXneZytzaMTZAcGHDWzkEWO851P6ENaQSvUiCfZxCQOOL6IuNMft7ID7nv_BOv7EkDQw1BIEqfUZSABBG7gTYeREr64COzeIgf42gY5qFEi6XPPO9eeClu5Ah8b7PkpRoY4VmnbHAvE9b4Vs1g0LX-utOr4BEsfr1zo6ylKkHb53vqKmkiGuUsJgBid-tYKhIn-KDcRfjeAXiLhQYgcicNwe4Kg5jncpYGhOSyY6Oju46l1eVg0uzsFhN3hWVrsjB79ngz-2lsZltt1sDCdOjXdARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_07Z-1nkw0xZ9umkmdRDKCZFRxTSL-805ESkAHc3tuyLUE5K5zfj5_J7EwHtN62qRRzOR47B4QGtjpJ-CQ6ibQZzSwLZ2EjqH-CZKYrfePKnK655UwU39Z5WCUwv-w65BE5wIwssTH5SLWMvx9_DPewUqjFB5lEaM4ey2zR7vDxOnjGsR2JvW03W38rlLdUWEDhy2jwtpMnBotj9KGsG9IU67i9Wty5IecS1zj1qQYm4qCBOB8owPUoXt29ohIjWkEX3ywjhoyrZrpniH_fehiH7t_ijUp5NsLOxkmHPN1fzTBWAmy1VFII2F1AM3cM8f98j8HZxkl_KK9x9L6NKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNwqOEKUN_-bPL07eFMjgz0SMt_uTaTYMV5W8VRsPccb4zrQP3wwtakF8nMHWxprYaLGB2n-Kg9QvdKQb9MpbTZzF9yEg-pkCK4CyZUEogabBDL96EeORRoXI6kH1WEYY7vfaSAvQCKWMVjbqAA8to7Q-zRsqGTtmo_iTTDSFLtA41JDvTVYEHgwJCmIEA-QGzfc9CkbSouFTGffyAKdibmQGWBQt9X5YCDVhdKXfU1EwM19bzbWSgN4oCxF5JQz8sXKkyUHg_kyagVfNHFmkmjdKNNbhNetGZ03Sbd5b13_e4Jv7xA3iCv2pc6J8zgRjNbl4MUte6_4qQoBtlQLEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXVUDd_wR1mBu5tJajrmDHb27FC1O0CXnEZIikGZ0AxF-Wi1P-qLa3_-vQzvb9f8I0JmbxgahYi58FjMQwuSEhU-5PzOEQiM-C_fU64vFwSvUZycMMq1JCFSQE6j8SgpulH04bKiUoMoJwMi3SsY0v1pTE-7gCVzbP84DDYBZj4fETzLgp3x5iqq8v-YL6eu-hxyhlDahfz2ZlAfHdmLsHiENRLlgl2rgJQwN3HS1jWShg4H6Ib889ql8sMVFeQzr7FL1Dtgz4CLjnrpnI2dYB0CBX0k21HFw5s5hCr1uSOy6BhfUH3eqSuO0pEkImxfXN0GVG9gPRovDZ31JTRhzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
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
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq8jfu1Boi49ue9EvkpvIvc4F5gAVA6fdcsStKtxZaZ7_SWYHmV0FWQXKQDR4fnrEku2LlB9xq2pFKdwFv8N1HKROGbevCbI1vNAt2bb7eLYz1C4tywYC-HVWvdGKHE3vPGlUzsln9r8H8l7T6nrKznQJTCoVRdtBRMk2JtSioMSShJBhZLX22aj7iK-zhbSnOhcrPjq_MbbHkd_CmxuS2471eN38J1C8_xTpQWAW5HnFkUOBBO9kcLmYh0uN5EnqUQ3BG3C2Tk-a1x0SCteRoYMNV0tQu8wXY35LGKUwNHdQoGeK7nsE9-mH3t1zzuCUEBOeskFOSoNvKVtXWt9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeGehJNX6XtUtblOMUfTzcVGvTKPMCfmxIxeW0D6PoZF8ZDnFjEbs00ff888XHjJBXOebDGErgu-zo92QRW_uqZ9INd43KYdXbtMhEVGkOqvQz6ImQw6jRCKlKvC8S4g44LWiOr6JNQXVrPhbP6p4ogKbNbvMFHSe1nNT4ROr3d6eK4_iDvh2bYi0LkinQoKOhRclG045aOADJbRHREStpJHKCaUCrEq4TKjIiXIXXGf-TFBn5oJ2tMr6Sw9Yx_gOVP4G9oJfTXqFZRtLdp-LI-JbK9X9g0foa_zuE6JOo7fFe5YpCSkp8tSy5EcMrbWZjOlwwrAVwGO1wWD0Bet5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St8zfIEMX9emDLEcpzZY7wA0gTj4f6VPGrgqGN-LykW04EpkAkZKVl-mZk1cyeB7l9NjCWcq9DmewUpmsGyczYyEea7e8DwPqGfXSKCzjNiiqV6kbP8cmcOmlLLI6xxdiIV8R2HGVb9Aj1E04817OmmJphqEXqkQZJTZNtI3JVzCa9YCgfvtx32ZOqZhPmEUaUcNxI31jC9IZGFI0KDxeK31WHUjUJYB-6InOF-xMuWRQ7iCODrGOkNcuUL-elGX11PlDumsyA8B_mSzKR3uCeAbuAJuRj3VY0TD9LmllXoCiKfUW_DYPQe9kZd5ciSrW_ya0vwgWTHka-dPpWhl6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS2AGDIrYpASlJxyaa1sKt2wwrfQXgH6va4xtjGqTH58DEALE8E_6kcSkK8LJAy48kN4C-QojbF5iBIBDpA3dvW5kzEae2gvP1wmVE7qIJ_h8FtMQ4u2PUS7Ijlo4JVUTfii9AzK4H60a4dtc_ttEU2gUMei_TpM-QWkzYJhQTYmRKC5_a73-cH9w2HfRhLAsSvteR5vFqpreOhB8oFs4EgcoyV5trpV9RL5HC49aenDsckimFWL11H_naW-6W299KozpBPd_z7bsLyTBjCWymeKC0ZKzbsmutfzYUhy9GovXglOfkCHXFohld9aBc3xIIc_gbhjmKKZnt5yJ1-A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFtVJLXZVj-aQ0VjpRSPQ1sdhXnZZYwFW6SMbrQhkZvwez_fvw9_6TZrRJHONdWrHumhrOOzuO4XJDF2FOH_WGqhG-GXLT0a3hqaUUgcFRelyCMCY4xJUqug3SkRWINfQplL92Xb-Xuw388NuEh3r1fyQUA6AldSvQleHGwOaIotWcQrVM5BurbcIz1YbqVjszKQw3uauS1qc5pO84VRKgZ3xPLoG3AEwOqzdusiBG0eKQFOQJ8hb3KFKTKv0y6pS-LKyKco8P5l5U8LdmsqZJaI0z7GnSrQJQy9id13Cq8RV42ZRaygUWW_E0qhAImSdUdK6VR-LoZ0AzrJlt01fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k39Ibc5wxp8UMw7WCZ2hKc0myI_9ru53n87002Ukz4q_Muh0Ppa3tBFlc7o4py031F4-jA4gYZCvKIV2bT0sq0J4Y2cKIUqOQ3DtFX_Tm3YuAyeAoYyNuGwKYiqagNxp2mivekEdY2GSCVCUcYkZrWxJuhhz4_pa8RlhDtf0dTP2UsT8bPraB6EuEjIvXc3jzELh0shrVM2NKy2tAu6Gk7dsZmUidin82hDNor3dkMFE1LBUNWjzKB8UarXZlQ_4bcFoa0dSCtiWfBr0j0Ugwje1zBKotQr05z_A7k3PXgOSy2QWxhtRIHhMO5hhISGEib81_yo9pAZcH8kidhn74Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR1Cu2Ah1BBBLbsidsJh3mKnchZDxNtKpadLKQDUaqRkwGVuK4zUWd_RsmP5xiqH2gRx3VM2IP6BKfaFhs-d1fSq0p7wsoo6i5I7kv6ZhX9o0bONTGwOVpEatwouwU9FDc6eIxKFdHqjtRRHjp1dDrWki3-g-i1vWGVRmmke9rfp4FCwSBaeKnYM0xn1TvHQFEIciiZlEXvA09Gh_1Rik0p9Pt1d9xZAHhcNRNegnnx5hvbJqw_MN7fcMDK-Fm41CgNQmYzrWxVkoW4uyhddtJcJmeQrCbJ2C6SDaDPnad3Dd35_Bh6Y-kLPOJ4iQmnRSXeckbchoSlqeiY48ZAD6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtI458tvGrXrMJoGSKddm3l66SuQ5VbkQPcPJvS0N5Zpbmc1UYxKQbT4fZo9pDIg6ic3kRE11ffxtqAq_0ENS7pi5t4UpiJ1FiiIz3u2dfb-dXCSV9dYmpxRY8pyDgqoI82ThxDIFX2DDdng7pdSwZfHzQkabRx33wICHtQC8UVTBEekltFClUJnx2NsKX0jKQIE4rmaBXr1zD2hupxgg2FfSZ5xOwgRsp4l2tzBGH3SwPn5r_EUNuf_PfMHVUjm4grBFSndqkTnrWSFUlIEJa1abR_66rnBf_azbh21v4QYzGWTQTTo0f9lspjdEdi6x26pIbj7lx9H-_Wlyw3gXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApJbB-9ydlaarKb49PvXxk9jR2DimeUqv7vsIrbpVf-JPZljJnin0XJS7gTI9wngJFt_QytH8RCAIDT8-2KeWOPD-sj5vrlzHecGtw3jXsSuQDspVftcM-e_lyAX2VsWXQBy0KMDoKkyG5tXyFZnpPznCU7oZAek6Mu2Ye_n0v8P5nBsiCQ_EZaiq4Aq4T5s4Uw9Qy55JlHjh_cOS-XVeWaq9D6UFsUhVdEmHjS8DiFHcrF2TMVK50TUAcpX0Gn0Cnog16SoAVY2dCf8wDU-tCZeUsAtcTfPvEZtGwwLyN6L3MEWNhA2B2VbvFcmsTivpcJ54I_XM3xofk-7hG68zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPtvkFSx0LnO8Sut_3qmxX5NiaSy7TtyotFuFxZilJR4QKccrb81GIsN8xUr7OM3AJikiiUaxDClLY6HsRAGSZ56gYGxzb6fXYNcqOTwDh7EASabYa1RxUx0VznrutIc_aj_4UaowSeqKCBLlDg0jyipmrODvYS2wsLT_yoPn-XYsAvoSWUgHn2X5c-OK5H9730prkN0P7_4onKROS3bQNJud5QeN-mathK17JKGetxCU5j_pPJoulg_Kw9ZXQx6VEmZRwsJGq1eDli3cYnZM8Y6rvUUAPXbCxBwIEnINuggZY6xV20H43SVypm8czchZFvu-iyIICKD3xdgr1_yfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X0m_W034KVY1cqPvlj9VtHB4T6L_S_GU6II9tXuU8zpVil00ARfHo89dJplFTrGCsSh6jk9cQjyT2FzOKKmU0OLApnyPwUf_faCsmRLcQviV6k3UUbSze9yNaOGk3LwBHntzy2PA96p_H-EOAYGtsHpav-fOSu7fhDoGBB8KaegJP2yc_umaYLDsumGqTyaH8gpTpvgCsogBd17I5jKksblBMRi_B4gOl452FR6fWjGxwbXO1031q_JKvpVRbYMtFYCMAG-KIN6XwlIgfLTJgmAqrl6QFhD56KY4JVVIMTloqPpYLnZ_Ihu5ipiljPJcNA1_jFb0_ygtATgeRP10fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NIVQ3-NphNykOJ5kK1KeNEhAC1cNzRKIz5MTg-YKqF79SZ0CIzB0G7CFfNs2wZEZPwWTIbK4qCVhHcHvJGlkSoQruPih6_AUJnuiYZW05DvzcmCC78xVeV4A3gKCv6-5w1xNLi_WLEQg8V0FNA7CKAMANGNNev47i23TRfGnZ8g1cJ18gQpl9gGE9d4SR_VEJqHOnV0OyruHD5WrNpHc7BkKgY1wh1rakltU_OdrJa-1Lebd9scTfJDMKXD9CJdMJFFef8FrXGfTxTpIrpNF-dkU3JbRmGlhFUMWSrPW3ct2TBazmXJpFDJJQ_pSoYAUH29O6-ClkuHdUN6IDlETAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE27kimqyQpFUtUjDxVQlh04AHthgddzG-apEI6n2YHbgdxZM-D91TIp8lOATmWywtUZ-XQq1CsFWjAabm2cZIRjkDe8Xw6udPeEayGVor9A3bcS3hrRMIH1a1mKWnOUaSj3OnAY5tcPp6qmUKVW87_Pejdenaa8lWnquEkvaHco-4vDz6rKNv5LeATHlklRaa7EAhXddNJGQOBW-IvJWMW0KRU1SYGqqRkRqUSZrfcXk5l0BDUCtwt96oEr4v-LufwihhmrhBLn6Gz0MNB_3yyPB5tq4QoCocu8BZVCARg15_mJJNbuKq6OtS2JrZJ2BaGuv0Efu9-ojJNWmFlndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojYitjrwuTX7kTjvuuP371UidAU0_Uc6F8KI2_fj0RuX-NuXwsLi1kLncWejPNR58HPEEVLOL5G4vzxnKQdKE0dmuHIhTiu9Yju9Bwek9e0s0eEP1WD3BhGrppdz9ZQNchTcNtFaKq0AF4asetdhkf5IGpEhCZCmf7gixFUOmn4PeLJDkMErUQtiePzmxX0xqIrFZXVE84yKvmi_YzVZ8kuGpCkbDSoP7Vgw_LKiOydohZoFpR7LlYIuwtA59V5NUGy_745OXrakyKencuuySOHsT4blOMnQr1O2m67r01hbMKp9ftx41DyhgjLDTsLxl0Y8NP9FNRfpVRapteJylQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDg2KY2vGcTbJQqV5zaNaMH4M4vyJXwBVHfIq-pzi-P9etC1AOLLr48wRKb_e6WxJ9VsYnMHsDClz9Fj_NYZJ3DfE2FK7LIVXbaSJvFKLIxlhs38H0xAyTMmNAcsX36EzSDrl0xBFQ7qGgGfLWHUbk-DudjQmWkKIi5cdoUwqGjtuWuO4ALqGiJp4Yzs5tDrhOmREiZnKqNDmWl2rFatOW-s1Vnz6tTMA9Qp3bvI_g4l2lxKC4qtINXbK6psA9FEjLbxFhqkEukS3xjlBSnctUGhZrUMyH2WKv5C4DTw8oTznqdpKlJkS4nqtlS4K59sT2D04kU_nxEkzKsk8L2zHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPUIDEn-nFyRbz7J5l6S2pytwvwN3wCxb6Hrya-7sMhlY_7oSph661N3GbbYPboLLyhUfPQQ7ZAAdJ0Vftdkm2Lzw7HukOX5psAchIOkfrZDYybK1HbNDsnsr2oK_WxtSl6t_6AmbUPdS0rT6NVzeYUR10-2tI5b-IlRtcNXgmEKxmWpX14Tn7P8sJ7C9Zbmim9HRL1ghcVb3B89avBnZEDXEecFcWvZFcYh1XIuKVzLMlTKvizeWFbLuEvUfoO62Wl3qn_pgCLuiRDcVUGskZuFIO1RsKHCKd9Ec6EDKyzQtQ_qLWWkPokTINRlDVB1vsdYhrdXdItJ3OifRcurZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKzBLfUtnILOaRN-wz2RWYJDX5Bkz30sn3omDsRiKCVnoRup5eIyhuecIWUZ8RUiudGOEr8x6vEROcxJDt1cG7pCyXvE2ATcOULiD3SY55bixTgcTDQoAk6IRgY_c5AcDmGtO2z9ojdKtOoE-dvPxEI3AqrOaQHbX_TuO2KJRe0Zqea80lqrohW68vodyz3gM_xmBplNz5IqBKXgv8Is5oboYNLsOvuQSynPE5VlRWOqReSSbvjjFONyvooXTNdv6lkcGv6If1wvwabIL8tV65XcVY6Nboxmvj1VAoFs-6xEEq6OickR5_q2JYUBE67An36pd36hRyObw43t_wTbnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnK5DYIuM6AiefWgkX0FylVswL7iR9C79Jg4F96U0t_Y-XEdFF-t6MatMWXlMqdv5lOs9piVrOHJkFnBphyAlAlxG8Rw6Ostpxk_hMJHHtOCLVTd7xoyx_Bt26bMshUqMyHLr9Fl8QBRJ9saqRsnOXXzwyc64r0eQSOleCQjA2Su0iVqxRT3XAFE8sy5mH1f9kxBDePesjd_ce0GQrzm8ExLNRVLcbQZ4fwdS7fidYdUkosNJvB4smQ-rThKgtyDiRPfeH-TJm5xQbccce7WuQMroTl5aeZ_SDUrERb7SoL2uDkUiAOy-kp3h33sWnv_v-Nxzi5uXnVMtftr3pTsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOhnI1uKE_VVej2xqJxc3_nfjxjiuPmu0xiDMUdmtQsLjAKGoI0EJEMalUiUBW-GObEXCmeFYmoXDhecLz6AsruC3k8UabdSwl2Q5HdOXc02kzE8r-xXsi6qsKu2eg_dByllIvRWL_1JuvLTx0Vfc-gOjxT5Ymt5-kWWL1YW69iUTKhnWTdQNigLpiBQOhGWX6vA3E8LRb7i3AiX47pSX-PNyag3haR4SSIv7aKV3akZt-8VVZLgVeA81efPMhlNtNSkDZc7FC0W1myXydogGMKRcuDzoEk3Gh8wCbs-Zz7ihaUAF3bHQTaYGQzyhU9wCxJoGxas0O-R8R7cSfuFUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf5vTKTfYzD3-2n0JsR3rNQFo78KZ4jk3zzVM6m16_ByqeBi-pTk8neBg1KbP07m0_xoOHNz6sSiDrzjRdEv6gOkoG4IygdyVQ5MHwDCxj0eEaXMIBqf566RgWEQMpCkPDYAv1-JE4U7_HwKueWVMvK5CE7O8_pqT6fH3pz8OBJacfbbz2VlquJkLoXdLJrhRpnyPQy2T8KKvxucyX7WZC4V7YEQUvCN3TQzAZYUxk2WV5fNP5jpxt-20_K9FRP_qOsMPlaAV1DffVgreRzVa5jl04mzHclOsXOiXxXgsfkHNk2EiOEiKAI2iFGk62wH1iPnyMa_4znFoF9W7CXq6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSmlYlGGi1azVXCP9xoOUE-jVuYfe6uA4tgGaCMSJjE3cnu0YfjUctc8AGfCVppvglz6Ot4iZtvjCfFQnatFZH3eG9WCL11WoX8r9wCo8qtoxid1a0x5d-qOMkGn6BkZ6AmuII4ZYbPFECWooyNY5IgqBuY9VgA9rMmMxtrT5zhLNSUx9z9N5IYQ62Vuk1hspYPgZluLVsFjOubi_uO9IbRvlV6zzoH0bdbhk-2fOcSmp_8ynaGqoOqYMrfKz1mHu-XOng9u3KFtTtEYMjzXlKa8X7E9r5Hhypf_MvJQILHumiFcfLly5pMA1EBBHOvZJGutApHf5sfFfzJ5GbgW2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToLbIBJvK17oWS9HzKVnRjTfPmDhMXQLBv1stTz86rXBS7InqnD6lJnSe7xU2t8YzIGTrgkkU5nq_wrklGC63gn6vG47yCSDb10ngWlHzhY1BWcvjKVqACxrE9s21w90TTZmAQIJTaMFR8kNBeaE4q7_oLM87dHkGmgwrICiBGy-6gbqrR4CGD8FDLz79aqFf4JBBuEan_Qmnk9VzA2MXU8gzE-Q9hbvf3Rjbfx-sjWllVBDwNg5AM5M1cFM2PP4JwKegbHoW52VByj_zTwMS6TGHXaC703APIkjmeUMaQZfC6lopb4koPaCMjqejr5l619yS4PXQYXjw9c0XLzoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCBDufjK85ocefirGRYZVM98k1doJ2OqejtPD6qBKmq63AqfZ0pKCwAa-Qg5j96Jdgm-IldzIL_XvrG1ciFQrW2gsexfASPFd_IN8iW5BfdQY3COb9V4YnvRn55QWaItogMjCOZ9nf9wQv6usMTgic70h8p4IvwVg9QQprO7HVvgErDvJiDLM89ZNIz1K41VvnlWGHLUx3nB6iGy9mVDQ7xTmkaq9W2XypKjbJ8_v8h9q28B0i4cMuj_5usycGGndpj8Ar_Aepqu_X0-U3jmKGaQzTJfsGPJykPQim-QHIQ2yXU-dqc1iMnwhlUjL7Q2Pb-c8I8LKpKO7YtOjv4WvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3YNtaKXfRmdQGKBmAOzb0BU3TEbT84yh12pLIuE2dMRXOQvtHlwNZxzC0utiOX00PskDDyHkNXatH3uxnCmV2v8LqQQcxQ387RFfnF4Z5mHmBJduGpgDN4hnJkxFFrkVT0UpO2l1CDT4AdVGIWKTkGSqCYvPy6KxH9w7H9Ar1Xn7pHrZl7eej9K0SXGtZLbbwG4sBhOAu6nKlhvYy-FhtvTGL70SJWdPZBuIvkzSqRGOWABa1nEhDHDeB5cizaKUFbFzjXkvEqe8o9pmS5_ePQO2ZR6KXz0xlF329n9q6HT2kIYxJnt8iGA4ei_L12pteMCpU6OWXakGUg6J3f2UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeksguI9VfHEDxIzGBv7eymJwgT9rN1YH3uHJQoI6hqrx4q1AU-cgcKuCI4D3KWAEW4YQ_Zqa5gDpyYVJw4lFxr0iD7rKgPWtjmi4hgdqvT2zkcbE6ZqH15-DYGakRVSQldSzvnf4yXEB6ubU-_BGkeCTD2AdHUhJd0AtAaD0_Dg2mBqJyvCPJQBscpWs0mCDQdrTahBXjQPcA9_qdUUYQuS6K_oXM1xTEG7BsQkoPtUQsi8JBCB48XNVU7l04QOEvxzlVOfc3grcBGaFsbv1yexAQesRODGNXDH-l_U1Ic5VL0tTCDIZX-9ol4rbi69l5O20fUIxtBgg2ScS-XBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPV3DNclnsY5Njsut12Q3Iwhpa_D7Jc4vKK7QXqzebsW-8fMuKyySJ6La2nojq49NUqbIREppK3PiajkBxKocxk0IOkxwLC2k9__r_3zrzzc88P2SoQj66zc4ZlBC_IB8mmkNFnmbn9FNGROFubU56RbozlizH98JiyJT4502Vs79y-YlYbdmluX_FeM-dUYUsPJlhatojgj2N8w8qqmP_SC6xNp6TtLdiUlW_0eQrdBJfPRqSI-SA9wQNoVSDp2k27_av3srF0rTbmXwzg2JkIPuuL3SsiMAyq7jRmuAB0i9EfiCTx2MZNzxRj128NCmxu0_pBiQ6rLlee-FQJznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXoEalR1p78HhscOAKL_ay0G3Brv06dircE7NeFdmUpm51tXkl2ScuFkP7HEKgYjwdwD_lAX_BZ24hd-lUgs9m2vb_zWOwki-p6baXRe5giM90Puuc-dEWCh8rgjjDYJpuvoW2e0zDHXsmMbkDMT6OmBfqYNFqZbdBzSF1kpEMfbMhDaa1Pcz4P9TIduRlNTSrQWwM1kTAVN2vaAD2fY5gKvmFeuF_GS6e6ieBSDO8X03VfQ5l0DDch5vkUOO7kkNIaSYoUBW9WbapWq1eWvZcP_6N0pTdJpQKgvhdvM-4uOnESPobiP6W-iPOrMhOWBg5jyyGH8x8rK-X580B5JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksCT_NA0XXsNLhXPpa6jMcNL4NA5tEDSCcN_2dyLE1LprJBxWwjmZwvMQ-kPOw2QihP1POyTz7psEVctGgcbyzl7jFfqArv5Bs9Q7-qacrxSoOJ6kpx10vQsFR9YtowqQCVWQr5MRJ0tZA3mN5wuFAVBQfHAzRveAi-EkQx1pOjYGJn6IzSyyekTKjBPkIYAqgmKgcB5FIPXbYRH8R1kR2jFlPnuBGQ3VSuN5_6W7rV4zoq6LuuhkirhHR4bx1CijE9BOLr4Zhy2cvjm7xoC2FxAJJbScF3vACwJpa4I-20xjIqVCtBQOZ1ylXTX0Re4YZ5NPGLYfS8J9ywgapMpFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iITo6BmU9kpimALuatf2CmlD8MzLWLH88aY43B_M8oOpHM4GFQs3yoj8ZzgHLGIGwWvijXEGMeSu_ELCwvZ5dw4aH2A2tOfzMBgYWBAuNXMBgUBDLBbk9fmX-X1VAULbtMTD9SznG6XEhaDD_oWmLHSGYBAqOIBVcKUL733FWf0F3ypLawvrN6Ct9DbIlX4OHPv4eQAoD6QjwyqWRQmPodZuyvv4H22Dc79yZc4moJrF3HneIilbyIPN5w_9tRG-k33c8a1mCDJSHId6nz-e7FcHmYmricjJtwNoMKGtWlLls6IgsOnxHS4ZIiI7Vgn3VoDcWJLh6ZV5MjOj8blvqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D21COXR4LUl_iWdZpXNjoleuKFCmS5A5VK2M0QVGIQmADSpP3txg8BkImUQ4vnxj7ybsJMOkU12-9CQdS2EAtXw7Y3HRXD5nnkJDTodw6qQnnMcFVKamBXc_kGtmlFvlN9Qmoovnd_nIVtSMWGcZ4E4M0dcUOJlCedq-6a14YxXoOstbgcuPD2QFbgCXxuM4WkvUul-lDBmrzZnN0oNeFa9BHbWd4wtc6YBreI5XPUCOMpJQtEA2fX2rZ-_BYp7Eni1DMGssRuE0kuvI9869-Tg4UZBFeF9l0WnQbvmy5Ru4AaDdWlVU8TNePfCi1MnC6zs4q1z1m1gdkUk9YJHH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax3GHa5TGEVGM7iTu3kR26qlrVxkaUA0dIImPW2IHHw69Bmbe4-5arDJuu5qbi205UIXBoYntkDuw7iQm8CUtx7UoC9UORJIF8ZuwFhJucHPrHfExyGJuYWnIaSC0nhjOaVP9OPgvH5FN_CKCCsRR2Iwhy_bkmGcHtE8_FzBYf9ctv402-vrt8VtAx5i0gXoQg5NmOzO0_Lm649mQZxlE-jXMPXZsgs4lqccKcGuAal8Aqxw1irF1hFrisztxvwr0z6i0kgrSAzpHTdHmQwRribD66FwacC_6ez-RWRKz2ZAsPi3LJkE3jByC11kWSxUExqncQGBYqos44rwton1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koaX4Xf2b-sGsw7z_LFSViy654Jq2JfrW9Kk4WPTBT4gyWmtDsFsemjxr6FTAvd3vffsOYAC3aLlaEqJkQFeCzsbAsuWv5GlgSRklIklSk-tvkMvysmGQfvcuEuQapUUWjQBBbauqupQ4p9R6d8CitoN5nfsiTxOE2QoP1imK1S4MocaX-ZM01HsMwGhGWIcSqGu9aHIfxPG0ZBBYcUxapCyHWEEPujirCgE5Z2GpmRre1EitV36fSGdcTbXqfuZGPUq8RICXOqew7rpHwy0X1rPEiYUhwnWhyfjoX76h7yJbftflxYdxeIeRtv1vM8isv6G5kZhSkcg7wSJTscgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLm-_qbWm20H3ANe5aAt0SY7gLrWBXM61865An6RcdLPgLGlhGjSSkv0IgUxr2X0PNJvX8kCOuZ0vN6q_SPmODoJn8aBvXhuhD7PFG1qwcNI2srD24tEYhDt54MiB-6-cFkUk18y-91SzbsGr1LFiduJZgzjhZR-2E75EbM42zGEKwI5kZMBmMeQE6-Kr4PIqmMMgCSy_9j7NdeMkokJGqelaw9kd9cG-rba934O6NuIZB7-ENfvIoZjarVVFswo6dYAns4JLMGohilOhMOKhMqtuTXJUUl-nX6g67XPQu5S_Zaibh5PhbUoTF-nb__SFulLeqgBB3Y1NA4rKAmLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqDYXMvovBMX9mCf6dpMNVqtArcrKV1EkfO_ga8D7KYjkK1_7qtO77V38rxlHfwjxYIdinpBHWIIcPnhzITSAh_fynC2ijV7rK_qC77PcmfTRUxPPV_sIgmnCe1JIFEnD21gw13RJWYFgUhRkur3Y1pWh1Y8irb961dCHkQfN81xOND96MSDTHFdi-RUrUwwHUKOtKhBW1pnR5vunOrO1Is_yWEqHqC0PafFUUtJsVDyuR6tVJcUziwT6-UNJKvJHrf6vZFjfDdIQ0qGXlbe8VeNSYK41DM-ThPjU7rqwZtwWoExIiub41cktyjaUx3_ZXzrHeXeDQv4oY8Z_avu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxJxqWmd6kBi1OUYtQ_2u35agNJj7kC-O3IVtMi5UJnc7XCG8WpbbC4Ukcv55qAeVUk5U9r9h0g85XhFwQkMSqWryCGKIfLf8woJyvGZNvzyUKTtdsQfuTUDW0yjDJoYkaqv3vkIxEUwgQ5D5g52JjzPD31yCmQjPhhFMP42x-rVtPuzj8ky5BACuG5qlxDA28u0uT3bBdxrcX9D3wEV1HkVOdToNhhwMN-J7CM3LpaG6wU-Ch_J5AUmhIhmA9wSXQEQAtYcdeQ-Pt35zEDYaxj7c_tXUw0LmwH0WtResGBNDraECd2bmOrCWlgpKnjvDLmsiBIoG7KJb6Wl-p8M9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdqaqhgRe7mNRUt6OToEoNhRhUDHUK1wWSq_rcWNJRCKvL7NdYAh8HLuKAdQKy3YCaeEsoji2tbY7sSiRE7bPhNXs8r5gJ5dbVtNg0hs-sHuAxetaE6uTRvMNTEO8A3Dsa3Mo6-sCPyqDisDNpMUS0ZtAk5psHyeJ0POdXdFlAMIkPGMHuXE3ftJ5kobUlupnYSHMA4wYf16IV9MsatDDBTOHkOncyhwLi7hj4gAkywLtxrmai4oKYpB1AITOcD6NmyOJwz3Uyjs-7ebCICGRAIzfzBWtIEWt41h9rXJUl8uba5VBssCiiSciCoHPDNG-wrHoyI1vrohfqL1KlV1Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwT9tspvUVXb32rRkaMylOnsCnCz8Oeq2o_ApIsqqEqPjheRmDQDy6oZQmpL-CnHfWyf8fID2vETTRZtXctetqEqZheIQfDIb1tbj3uiGO-CCqvwbMaO2EWtrxx87ePoEoAnSqkjG4pAh6ECDsxxXNh5zNaKMpdjtL8bfxwtujV9P44DCyWJ5td_XW_qZq8rDiQHvZ7TWgVL49oSvSza0eam_fMGO5K6geOapyQeAUNER0XKy5ClpwSLN2nRQJ0pu13JOR5MbHNbjhGLe9q-Wxe5xTQKMqJ2IoX-lW_WhaGd0xAGPNAdH73fIPX-rsCehhe5eIkRo8-L_AJZdDnuCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdlZHLWCq8tsL4krMemV9O3ckzxIhAOSQaHm2VrBMfKvwabGNe-kcc1rGbkd-WPBIlECC6INWc_8ps_lQH96VT5DlGdXDaShIlsCJSUjfU7BvZf4OGBfSxJ-9pUH5qRHWgYJxQBemWvFebF62JyqYz6Tw9RsPP4nrCjW_YXPhct1ugjEOs0RcxNvdN79I5EkaXEXNEMfM-QG_oPn7xEa6EdaQR39fiRyDI3RzRzK35viZeJ0ZpKpLmD5wGL5Kjg_Re5FseNo9w_gMUjojF3ZIjmPqRwLN0qGf0oQu892SZyRYp5dDecoKlW6__9ZG_B4fqxs2bbV7mgKO_Xu8vcxFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWdkP1U0Irj9XthnvVbR5mioxzASwi4g_EgeHxeo_Eji6lsiYdHFCQRtL5NeVl8ZEuZksK2OY5oqJ_wvhW7m4o9DwS66YeRthisM45LPOxBlJVauqE2LPGDrO6uDdxYxa3xjE5clmFohV8Zjk0lPb-QN4kNkY-Zfj6YaNyYrlrsI-EfH6PwDopJOvaU4O3C7mwq_zLdXMPEBv-zwpryraZHWT6KSVU5Ah8JmpgDiSwrkiZxniAptVpgB4U5zMWC2gL8g0j7cV5for7WiRfzrpIb1PSGXgcV5gI9Errt3jEwSBbEpmAFb-dxn5_-sJkrdTMTzBb1ustD7LrEOTkyhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQdnG0up3CcWsqjZEDa5qxWfuvKAg3--gfZiEBgiB7ZSXXc3boBSEHLfQ7j2so2cPPF3sygBMYaMHIRB4s8Jrm3Plp2fE4MYLQbGApwUMStClOEyhOP_stZ1xH87SNqSEJopkjK6OKlEPwSfdXbX16jAKiYIDvU2nidu3qO_lJ0zO835OEbwwCLvolem2oFhWccR9veCXwg9bqTE2ssFkYne1Pn9a_6rTI1iW9wOA9pyn9cO_QGRlxpHeqs_6rJC5pnT-jigzHpIuUGDMLW1_Yj2dw42JwyfD_q-c--uGMHAYANO8ZaoNDceCXEji9pebsluQ-vvD0B9iFQqOTNkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMhagxQ7WarCTm0WDvATN5Yk1YmdwEK8G-TpTe4K2bexwlu7cTExDkQ70KaydBuIjQdKsegU5d9v1W_jjFXC8mtWI7Vf6b7qhFFt4-ZCSusi4-3VyEcOGOqaCxvFbnG0n6Z3Rl3ryxRpPCU6uIx_opVb24M0iGaHkoMyYbNIyIPkS4RyDryg1t3E99gD6UE36WQcWxyU3QYGI1H2QXEFnlbmBDZp9PKjhnPMG9Ul4TUMvdBUbjAZJBUeQfDF1qJAmZru2Sg-bBlbkU7WW9nFCU8ZtPIouqyqj-NQk5HhyV60wVIE-ish1VXidp9kUcuSSxB4gS5j7sk0SxEQnRzWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4RLwm5I5HM2PQI3DxEXKKPsy2QrVo5MA15uyycvqCmh5Irj2copGSSVFga6EnPV1ScONl6hTlaX5m6Li6FF0z-b3XvuyTvczMOovLGvhPuFsIpVr2v06xLSUYxxB0r8z8bMiXTOa48N58CYyckUr6mOSzCht8DN4ey_MLwmMK4mWSWj-WTkB11cjTJGpj8P2AzcqZ2gIOyc5mxnCe76KDQcIX_rZ3HrQC4qr5pi0XbgncjjkgwZ3PwTQw73whNupBXjR0wJaLkFnxO5tcAGaQ3GnnmqkKW8VPvwybNI79THfLOfKHf4sn0CoRoP9ttUbHRqus8ADFvH3RvYY-l60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7UQrR6mYr7QWyWzBhTLsoF1p6UPQft8yjpIlAbZDpWIKIoGaBaqmsQGoyEA38fyCmHMFqAzYE3fjnU-4wSavxSBNZ4N7UfPprRU569H9ddiRDrsZj2ktLXnb1tE9SisiiTweLjf2nX0uAz4SGPwXEw1vhs603Axik77zdOCgjmBUWIdMaJmtxpJtR7e84vtGEeFeD4b2kz052STNt_efgADoHsRcTQVC27lgq93ZAQLcH44OUWaoVxl5FdX7Vsv1Qx3pLjXnhDVUx-T-jUE4VaO-nucJ7h_m-1ZWI0_LiWNpBSqJgHPhFpA_icLzmvxUu9w_ChUf847kegriDDK3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPIHIuSTcuul_9W2rfceO8GYU8qSsCPhPBEylHxlAzk2NubRIQnHekHHowxm5QzkOcLxi5JlJnsfL9XNB4ysONVXSGantCbVXOQMH486zhXm266FpVzknDcIZwrlGYY9VbfnlZkvyGcPsAtMvuVblKkfTYZpIdExAp34Hzu7lhS83l4eiMSLqLIB3711KNS47fF4PHDF3-HdfQRbihj-fPXXWnpV5ZEPvHuk_Myi2sQ6SiM2fpJQsq6zutQMqoB7NK1NPL0JyKbgwZqhNakT-gxmffsENgyo4PXrzXu7iNWiVsxOGxs79J3z8HjP5d4aTn5MM86f2OJKo0uqx-7y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQnTwuIAP0q4OFvyXoxyumP03A6y1qLuczvt1ia1xcHdBpMW1CUARvXR5Y6IEhPOarIXKwzFa7on5jSnc05rR7ztZgD43nmL-j_XjgJJUMrrgAxq_J2096KvIZx3a6KQc-1MZE2W1qA1ed2OHQAnI3beHwF-TdXD-AnWTqqupgxa8UyJdxIcp8XCkQ6ke4ZGlDb-PQWmpeNY7nDN_7BbsXOLkEJHCtCd5FG9tLh6Xz5qVkKTvF2r-UzuuWRvh1tVaRcgk6nB1dcNeWQxj27f-bif--QloQTc0f1WxxM1PsXP0ymiSM7xaN4FpIN9w0mYSb8tNKBtL9JQHG7sxLctwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UErxRT1b6t5QQ6TsNJJZgQZRUX5rvY2jFUowyauEEs27m9EETICXFgGybRF9zCg6nj8TXOyiX_yTBuHFx7tRsGoImChQF_BNMyuJaR0bvonqu2Q4rwmxyrz8ouOB1fyYsZCc0csbQbGMI08ymjMiPqGPyoPb_zZhGBVyge00H2sJk8wFyqCVMJp6GKs9qLzX0bdGJJ-fGsBlPblsiUl-kfiCpa4EytXJ-KTjFCJmnEPb8Rpaae2u8IY2p3m4aTQyMPxfrOq9trRju5_TEQ9b4X_PpGb-FMwYw4A32362hwV6_K8naSZRZq8CdUDywSZsV5C-yvJhxP2gPds92h-ovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
