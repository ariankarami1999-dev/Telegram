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
<img src="https://cdn4.telesco.pe/file/k4VVmg45X3Jzwu-adEyTDaLinrk8qJ-UNy_lRVRjCfxmDLx5m2gsSwUQ8cP1b5GMcCfyfxRKkxlv7EszxZZAuSNG6GOEg99Qo35Njj9kUo-CASJyyfpF3mYUzV3qo_rwEBKoiy3GuGrE3C-Fvd4MRubMDW4kgocucUtmCjeG4oj2CjTdp_GrlmsXUvboUi0JZxCUnlYtFRAqDDQR8uhFp43fQvG-746o0WKHXyrQYY6pT3qwnXYjRPhRafDbgOGY6RAYJDJKyBVuLShmIQrJ0BhEbvFZZpVwRev5KbGQRKdxa_TO4anj4WAclGlNKhsIjH6VJviE1cH2xmx4r2OpXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 03:46:48</div>
<hr>

<div class="tg-post" id="msg-694431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faH008c8hmabWXIm3afmgR2qo2A5Ty7caSLe8ytiSz5f5CPvJ7Qi0MQwcRDr8baPZsd2HhfZWakgP-vBOLdl4FzveWEhydZY5QXeklNxWKdic-RcTkQS1u06xbKbpzmrKHdp7D1q_3685aUWQcz_yRax5NBksW92MoaCU8offvbnuvFjwL7SyJTq6k_ktEwuMzPNGgN7hvQYlI-R2Zd1jWi6NECk2UY3qwOxs4er9j08uVp0oD357j0YFNhXf4fj3_-U_Yd6ScldIG1ziylVq5wJqB4lpLffecBI5i-_cgwFsGB8LqwuaNN_A6pZJV7ZXbMDY7H3jtZM2axj5djLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
زرنگ؛ همراهِ باهوش، در دسترس و به‌صرفه
✔️
مشاورهٔ راهگشا
✔️
برنامه‌ریزیِ شخصی‌سازی‌شده
✔️
رفع اشکالِ گام‌به‌گام و ریشه‌ای
✔️
آزمون‌های سنجشی و تحلیلی
🔥
با هوش مصنوعی زرنگ، به بهترین نتیجهٔ خودت می‌رسی.
همین الان رایگان شروع کن:
🔗
zerang.app
〰️
〰️
〰️
🔥
@zerang_app
| زرنگ، هوش مصنوعی درسی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694431" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx88qIF3k6mm9w1nVFP3FeRF5OP9YIBTyV-7zzwUbD78ySWd8dELAr-rGSxul1zqTxlDgd6WkqcFR6Ue_eq-JRB9Ss0Xzrt-_88IfIMwlV7_UwWH-z_Rh-4v53L7T4LLU1rqZOIAcLqDB7AV2pDRj_yfWT-yFiglNuQ-y5xrh5jIvo4dKBVZ77mtTPU7PDWW3ZIxepro4dmFuqi0Ko4WX6zKWJZtXEh_j4OBV5ub27MCLiQyBRs-ROMSSCkmaFCybMzR04S67dEWGjecY9br7SWWc4i6ajQ8g-qV82vSbok6Hukm7t0LNOHU7Oq1r4bZAu2hJI0BJHM7gA-ceauhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
OSCARTEAM | اتاق معاملاتی حرفه‌ای
اگر از کانال‌های شلوغ و سیگنال‌های بی‌منطق خسته شدی، اینجا فرقش رو حس می‌کنی.
📈
اینجا فقط سیگنال نمی‌گیری؛ کنار تیم معامله می‌کنی و یاد می‌گیری.
🔥
نزدیک به ۸ سال تجربه در بازارهای مالی
✅
سیگنال‌های شفاف با ورود، حد سود و حد ضرر مشخص
📊
تحلیل‌های اختصاصی و نواحی دقیق بازار
🎙
لایو ترید؛ کنار اعضا هم‌زمان وارد معامله می‌شیم و لحظه‌به‌لحظه مدیریت و خروج رو اعلام می‌کنیم.
🧠
آموزش مدیریت سرمایه و روانشناسی معامله‌گری
🤝
منتورینگ و پشتیبانی واقعی کنار اعضا
هدف ما فقط چند سود مقطعی نیست؛ ساختن معامله‌گرهاییه که بتونن به سود مستمر برسن.
💎
🚀
اگر کیفیت برات مهمه، جای تو اینجاست.
https://t.me/oscarteamm
https://t.me/oscarteamm</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/694430" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa4b7cfe9.mp4?token=JxfEz8hxhPIIuhBgsqJPHV7vsNxpFVWPvglr5Cb09SoSmr2QVOPa-kq9WvlhRQXHmKmdNjh--0by2eIW70xaPVwBjHbw-C5XMuRRP8ME9sDc0ETahmZ9iTLK51w_W64q5PqsMOXjvMxADjj0WjzjLxmGFr7S5s9h3JVyz_cJJUJdtcy2q5sYhNLFOYDfqkjyZ3zscT_IdpTxatdVNpUF3ArDN5IMWWNBNqH1P6Pwbj_RmkhV2-89y5cDPPwYvm1oc9RrJGXeqpOZaVs6p044oXo3u0ecMyQIpqYwLJlBgr0dVNCfJTfbWhfJYEpdfscBIVFBtuA-K-XgLTCAbjY7_58hunqW0BWGjjPWghJ2iXPndNAx14ebzVsbvUuiAvNeK6AFnm_8HeQYPk2eV_-wTi37FfKU6IYuGE1Yixtnt8kAdTQHhggPuTqjJ4GqBDS-ASq9_ZZcSBzQBFOEGeWyYiviFevMCElReRFDPVbsSl6Cl1QnpPAIdkZo4xsq1lo3Sydg0Lf4UlLIRJGGK0wgfdYJtvI7LWCblYH_UaDtmEzklDgt7bMfSLa9k52mdl-wVxanYWFKn_MmjyiNNhkTL9IqPhe02SG9VFvWAimDSrvzOkSgAmgP3zBvGBLdAGe-SzwUGYr098AuWdkyxs_6CJciI0w6FXUWl7ePLKAlThU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa4b7cfe9.mp4?token=JxfEz8hxhPIIuhBgsqJPHV7vsNxpFVWPvglr5Cb09SoSmr2QVOPa-kq9WvlhRQXHmKmdNjh--0by2eIW70xaPVwBjHbw-C5XMuRRP8ME9sDc0ETahmZ9iTLK51w_W64q5PqsMOXjvMxADjj0WjzjLxmGFr7S5s9h3JVyz_cJJUJdtcy2q5sYhNLFOYDfqkjyZ3zscT_IdpTxatdVNpUF3ArDN5IMWWNBNqH1P6Pwbj_RmkhV2-89y5cDPPwYvm1oc9RrJGXeqpOZaVs6p044oXo3u0ecMyQIpqYwLJlBgr0dVNCfJTfbWhfJYEpdfscBIVFBtuA-K-XgLTCAbjY7_58hunqW0BWGjjPWghJ2iXPndNAx14ebzVsbvUuiAvNeK6AFnm_8HeQYPk2eV_-wTi37FfKU6IYuGE1Yixtnt8kAdTQHhggPuTqjJ4GqBDS-ASq9_ZZcSBzQBFOEGeWyYiviFevMCElReRFDPVbsSl6Cl1QnpPAIdkZo4xsq1lo3Sydg0Lf4UlLIRJGGK0wgfdYJtvI7LWCblYH_UaDtmEzklDgt7bMfSLa9k52mdl-wVxanYWFKn_MmjyiNNhkTL9IqPhe02SG9VFvWAimDSrvzOkSgAmgP3zBvGBLdAGe-SzwUGYr098AuWdkyxs_6CJciI0w6FXUWl7ePLKAlThU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
🔥
این دریل رو می‌خوای؟ قسطی هم می‌تونی بخری!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل: 2
,798,000 تومان
💥
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
✅
امکان پرداخت 4 قسط 560 هزار تومن
💳
پرداخت درب منزل
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/fast/46482/180124/</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/694429" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407e5a5ce3.mp4?token=rpLBSlAbqKxhoK-djhqM3a3eDQdnq0ANfD7_mrU921TRV8LEPRiD4wCS-APEvfJux8FujgvBlfwVFSw4xrhIUc6alh9Wc6sLV7pDVfNBUDc5D0EsQdUIno6gcPJFATkQAksx0WDANle4TdNBgImUolbV_g10yHevnvlg7ZiTNQ3CJo8Ae5lgIntc11nZvXEeB9xDgcN_DzgAU3_BvTMT-E1Ke6bYFT7RkPSYsuqak_6xoyOFhrhlC6aOANXwCozWlBEenEuNlIfvEI0j6o8iDM15MJ1MXmsvSHdpKGRDolftC2eeCtIefnms8_edHojruNvTncORUzhHs4Pwk33J-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407e5a5ce3.mp4?token=rpLBSlAbqKxhoK-djhqM3a3eDQdnq0ANfD7_mrU921TRV8LEPRiD4wCS-APEvfJux8FujgvBlfwVFSw4xrhIUc6alh9Wc6sLV7pDVfNBUDc5D0EsQdUIno6gcPJFATkQAksx0WDANle4TdNBgImUolbV_g10yHevnvlg7ZiTNQ3CJo8Ae5lgIntc11nZvXEeB9xDgcN_DzgAU3_BvTMT-E1Ke6bYFT7RkPSYsuqak_6xoyOFhrhlC6aOANXwCozWlBEenEuNlIfvEI0j6o8iDM15MJ1MXmsvSHdpKGRDolftC2eeCtIefnms8_edHojruNvTncORUzhHs4Pwk33J-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای ماه درخشان در ارتفاع ۸۰۰ میلی‌متری
🌒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694428" target="_blank">📅 00:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
لارا ترامپ، عروس رئیس‌جمهور آمریکا: ایران می‌خواهد جنگ را تا انتخابات ادامه بدهد
🔹
جنگ با ایران ممکن است منجر به شکست ترامپ در انتخابات آتی شود.
🔹
ترامپ به‌شدت از نحوه پیش رفتن اوضاع با ایران متنفر است و آرزو داشت که اوضاع سریع‌تر پیش می‌رفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/694427" target="_blank">📅 00:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9wZQYC-h1fiZXrPOqBmJiTlxUipMX0kuiUjdj4sq3O2-fgLpWiY4Kc5PxNR13W6IsZysXKtrij_0ZTMBjVYVNvS3SwUD6CS3s-a52VsWOHVguXHd635GdTjYrYdYG129iL72GgSlPzjG27_yGnhQjSCCUDJBHKbBHPJteMTNdtNjc8hPTEdk6Oj0Aayoc4NdFmzetWvRDsMqGIl6te_2RheZTE6UuUx4A5Mj0Jy8iEl-QZ9K6dkJ4QCE_qLKWWDrecUQ9f3SdQXu7_VjE6b04gsK4-Njoz3SOvA-umpoQRiSxFDv2oVg-SDYxlOi7IbjwZ4IAc0EmULqEjaLMto_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری راحله امینیان، مجری صداوسیما از مزار شهید سیدحسن نصرالله
🔹
امروز جمعی از شخصیت‌های فرهنگی، هنری، ورزشی و خانواده شهدا با سفر به لبنان، بر سر مزار شهید سیدحسن نصرالله حاضر شدند.
🔹
حجت‌الاسلام والمسلمین پناهیان، حاج سعید حدادیان، حاج حسین یکتا، وحید یامین‌پور، ژیلا صادقی، راحله امینیان و بهنام ابوالقاسم‌پور از جمله حاضران در این مراسم بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694425" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8313255238.mp4?token=qk5OYv6MrE3JpPdMn5ht5gLD-hKOTH3CEyXxmZEcfEHJabDwn7K_EF9sC7zhKpT2PfWgRw8_yWrGYEEuUJS-v98YGsNEJDEcwTmB2iKwyz_aShCL8WY5PWpkooIl_4X6tg9r5ipPhFyo8ESpl6cd27Ii8ok1HPFL1xAc9TaY-i26uUIFRhnelcObwInaCKm5oUrfFNxpo_st-bGwoNBORPwptnvkuQe8u046FgHu4xMQog2b9Aq9JtpkegD6RJLDrPMvA0nKAHbyOudqAeMzc8NA344NmYaIGp1FToNA62sq_QfSk8_A2FZ8iUPXbYqDavAKBM4RtMNSzo31QWp3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8313255238.mp4?token=qk5OYv6MrE3JpPdMn5ht5gLD-hKOTH3CEyXxmZEcfEHJabDwn7K_EF9sC7zhKpT2PfWgRw8_yWrGYEEuUJS-v98YGsNEJDEcwTmB2iKwyz_aShCL8WY5PWpkooIl_4X6tg9r5ipPhFyo8ESpl6cd27Ii8ok1HPFL1xAc9TaY-i26uUIFRhnelcObwInaCKm5oUrfFNxpo_st-bGwoNBORPwptnvkuQe8u046FgHu4xMQog2b9Aq9JtpkegD6RJLDrPMvA0nKAHbyOudqAeMzc8NA344NmYaIGp1FToNA62sq_QfSk8_A2FZ8iUPXbYqDavAKBM4RtMNSzo31QWp3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مردم آزادی‌خواه سراسر جهان در حمایت از ایران/ این پرچم حذف شدنی نیست
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/694424" target="_blank">📅 00:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌ستیزم بی‌امان با اهریمنان
🔹
ارکستر ملی ایران در دفاع از میهن در کازان به اجرا پرداخت
🔹
ارکستر ملی ایران‌ امشب در شهر کازان با استقبال بی‌نظیر مردم این شهر روسیه روبه‌رو شد.
🔹
یکی از قطعات اجرا شده به رهبری استاد رحیمیان و خوانندگی مجتبی عسگری، قطعه ایران استوار بود که در دفاع از میهن عزیزمان اجرا شد.
🔹
اجرای امشب بخشی از برنامه‌های هفته فرهنگی جمهوری اسلامی ایران است  به دعوت و میزبانی دولت روسیه، از سوم مهرماه در شهر سن‌پترزبورگ آغاز شد و بعد از مسکو و کازان، در آستاراخان نیز پیگیری خواهد شد.
🔹
این رویداد به همت سازمان فرهنگ و ارتباطات اسلامی و با هدف گسترش تعاملات فرهنگی و هنری میان ایران و روسیه در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/694423" target="_blank">📅 00:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTfqb4ZX5iLptRrb2l6oFwQDHlCH0LVW863PFVkj_o4qzg28Bf02sGebxcODctXpiyMfWvj5NZtUxPIYUzPhKu-MlWeUshUIP1IW2b2aiIMD-QySRqQH5h2WzklA3xGlx9Cz67SZ9Ga8pa1-c5aymPw84pA2_8O5NksJsCWrnz5pFW3XQAP5wUzTsjtrqMubd_x67_ozjfw1xFK62dR7BXUkcXkHwTGT5f3Z4SosH3f-fewDlqePVf0djPcuVEvUv-hK8F9FxEW8CHfMYnlyJ_QN6Ljrfg-jG2vlmq5YjRo79WlC7DQCil6NLLwHYds-QRhlDbnF3eOUfvEGs4Op3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Shv4Rxx76s5VXT645ZPW3clBzwiOxudY1ypSMPOiPi4LIdOzY2_P3_ejNeUUD3fOJgEnREo9dRwOEV0IIZvZMFeIRIZuYaNpRpVfDVQJ712pm3GfVRn7SBq0MPfE79oeX8lDyePAVQLPbuF9rDj6GM1sgwxTcbhMNRkOe7nijHEydOpOUZUsvarrkWscS6N_P4YPt7MPc8_CTKbR7OLxliEDNMtvXDvcaJpktR4LGRyog2NOilxy4yffoanyImXgNaI8ZWNl09bfNp_inzG2HyBAzr-NhCjG98TY9yUrQ2GkypiYKrj2Cq2vd67HRZWhdSn92uLwf3pq-48JLoP-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EM-WkEDmDzQIpUnVsUcPi3usnuvs7n1bUCRAkk0ArjePbNcEzydXsvUhnVqbTCc27_5og0i1iy5o415rU_fgwYmGzRQ1h2oKE_L5mElU2SfrTyFGHREn3-xWOfeA7A3k2LyriKV12ph1El2x4Z__4OPqr6TCshiTfkCngdwg1qE2OjNQfK167-s4XLTIwPcmbPLb-n2dIU61ZsvlvywL4Qx2nWAqIuXzkaZxwglxk-_ASyHCaCZ2pFiXhDzTLpYGhIqc_SK-2emoszWgx8uqZJYQoFS0qpN0TJ7uFiJPXXS1Th7hudF1Hb0JC4m5fBRygHdksBFZncz-G8K3cAWeew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اهدای چفیه و انگشتر متبرک آیت‌الله سید مجتبی خامنه‌ای به خانواده شهیدان سیدعباس موسوی و سیدحسن نصرالله
🔹
جمعی از فعالان جبهه فرهنگی انقلاب اسلامی در جریان سفر به لبنان، با خانواده شهید سیدعباس موسوی و شهید سیدحسن نصرالله دیدار کردند.
🔹
حجت‌الاسلام والمسلمین پناهیان، حاج حسین یکتا و حاج سعید حدادیان از جمله فعالان جبهه فرهنگی انقلاب حاضر در این دیدار بودند.
🔹
در این دیدار، چفیه و انگشتر متبرک رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی خامنه‌ای، به خانواده شهدا اهدا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/694420" target="_blank">📅 00:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پخش برای نخستین‌بار/ در نخستین روز فروردین، هم‌زمان با نوروز و عید فطر، منزل شهید مهدی نصر، از فرماندهان هوافضای سپاه، در اصفهان هدف حمله قرار گرفت. او به همراه مادر، همسر و دو فرزندش به شهادت رسید
🔹
زینب نصر، دختر سه‌ساله شهید، لحظاتی بعد زنده از زیر آوار نجات یافت.
🔹
تصاویر این ویدیو بسیار دلخراش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/694419" target="_blank">📅 00:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU6sFuEZoa7BEqxc1hPsJ7XIFmatfZ51vLErAJXUhVaSjJDgg_HgFGpjzGQkrONGCxZa_Ju2aP8XX-HWNeBLqWeKObSSqJjfJ6XOqpMmm56Reem-lXPJWr398-4XAw76ozhOFF1QhuaZIP92lgTHc19wZ5RChtLzfMRiexlXNG6ShRaEfCRKdxCgNi8mKsnuKB6o__HfkaIWme-RE_0HhOgL2TfFPaVCkZBFsn3KiDubs0rRa8vMMng94Vqd3-J3avelw7gAn0DCnzilVuHt-APuOcG77xwCrveaEBZxEBxt947i2ZquRvwNQ_Jq4_wqF01UvdDy7qV4TdsBtaFtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری پربازدید از ساعت هوشمند در دست رئیس سازمان پدافند غیرعامل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/694418" target="_blank">📅 00:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694417">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
خیالبافی ترامپ برای آمریکا: بالاترین نرخ ثروت شخصی و پایین ترین سطح فقر در کشور را داریم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/694417" target="_blank">📅 00:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=iILluudVl2UFxHguKDmUqyjsZ2bj_HR4QwSog47sZpBro9JUlNBdftsIfRrruLcAqC4n-f4pYGu_JMhr7nuldIiyRpXdJ4mYWzMtavB1ojX0fiVSy1ER-0QWV9ladf7HJn_884LdwAs_9qzDoMYOqrrdnqOIWgZxQKpxozA1rVZns5MN-8aqmabVbL7F9zfmBQK_FHXrn5Xl8otriyI-TyNK60DE01IJTEoIcciO2LnOVYlztarlKTw1_0BVOsm5u1QPU1VrFehdc0sRTivdwBHcUPcD-RzWNdXrRez6Jx9lKBSRZffIBl3TB1YC3ZsvHYabAHtJBnWyGtuac6_Vcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=iILluudVl2UFxHguKDmUqyjsZ2bj_HR4QwSog47sZpBro9JUlNBdftsIfRrruLcAqC4n-f4pYGu_JMhr7nuldIiyRpXdJ4mYWzMtavB1ojX0fiVSy1ER-0QWV9ladf7HJn_884LdwAs_9qzDoMYOqrrdnqOIWgZxQKpxozA1rVZns5MN-8aqmabVbL7F9zfmBQK_FHXrn5Xl8otriyI-TyNK60DE01IJTEoIcciO2LnOVYlztarlKTw1_0BVOsm5u1QPU1VrFehdc0sRTivdwBHcUPcD-RzWNdXrRez6Jx9lKBSRZffIBl3TB1YC3ZsvHYabAHtJBnWyGtuac6_Vcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاد امام و شهدا در مسیر بیروت؛ سفر جمعی از شخصیت‌های فرهنگی، هنری و ورزشی ایران به لبنان با حضور حاج سعید حدادیان و حسین یکتا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694416" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=tSo5tas44AG4y2KHfnfKefJ1kN9T-ADpqaYAKZWjuZgodzmdd5zSXf9fsPJc1N7apaFx8GOwIDiw8MZqgRK84_xVWjYujhRvpaQDFyIF7rM7IXNDrmv1gViqeGOe0RbJGyKDF1gCOhKrT5FcSd4RpgdTWLfyXY9O-yTIEbWDLWpF9ZGfZqvYlMFm81fV5y0REKGXGtcSGit4k4I-F6lH6soP0n0Xwj9oPqWXhGUJYA_oxkQ5XV4Qh6eDxXZKJX0NwdUMVPHqjAn8gVNnjbCFZ1j5VLjPYUU1FZGR_iA5vTlO6jZKThj4e4VjdqncR6fLU5egPHW23uQtjXHTOq_wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=tSo5tas44AG4y2KHfnfKefJ1kN9T-ADpqaYAKZWjuZgodzmdd5zSXf9fsPJc1N7apaFx8GOwIDiw8MZqgRK84_xVWjYujhRvpaQDFyIF7rM7IXNDrmv1gViqeGOe0RbJGyKDF1gCOhKrT5FcSd4RpgdTWLfyXY9O-yTIEbWDLWpF9ZGfZqvYlMFm81fV5y0REKGXGtcSGit4k4I-F6lH6soP0n0Xwj9oPqWXhGUJYA_oxkQ5XV4Qh6eDxXZKJX0NwdUMVPHqjAn8gVNnjbCFZ1j5VLjPYUU1FZGR_iA5vTlO6jZKThj4e4VjdqncR6fLU5egPHW23uQtjXHTOq_wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری ثبت نامی‌های خودروی لاماری با شرکت وارد کننده، که به‌دلیل محاصره دریایی چیزی وارد نکرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/694415" target="_blank">📅 00:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694413">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh9JCKsAN0t3nNa2PHvR0y2H_iJxvXex58jwoHGqOj5sz97lzLBlt0yeJhEUnDhHxPa6kyL20RR14j45J0KwLgIIPltlRDTmdEzXyy9eA-NPFbezL9mjwmvKPPrhx0r9AkDG53LmOKEXkRSe3Jaq9E7ozdPTmSCt6hxRmbOkWGK7JaDdkbhq2JPaSopyeYR_LquVS3oK5V0zC9Bb92gy3JZGo5i2wPCqS3c2zoev_S3NSwhhUrMpTAI6fI-OQf-92tAaztQqRLQfzKYiryppc747DdtutlhMV8OXaiOc1XlEjLzHl-09tWpUsjE8b9_UDJ51zlRZqh9HZCdJ_R13-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت یامین‌پور از سفر به لبنان در سالگرد شهادت سیدحسن نصرالله
پس از جنگ رمضان و شهادت حضرت آقا، اولین بار است به لبنان آمده‌ام. دشمنان هر کاری از دستشان برآمده کرده‌اند، که راه آمد و شد بین ایران و لبنان را دشوار کنند. چاه کنده‌اند بر سر راه‌مان‌؛ دیوار کشیده‌اند بین‌مان. به خیال خامشان محاصره‌مان کرده‌اند.
اول پروازهای مستقیم را ممنوع کردند، بعد مانع روادید را اضافه کردند، سفیرمان را عنصر نامطلوب معرفی کردند، حالا پروازهای واسط را هم دارند لغو می‌کنند... اما پیوند دو ملت مقاوم از جنس موهبتی الهی است. ما هم‌دردیم، هم‌اشک... هم‌سرنوشت.
دوستان لبنانی‌ام را ماه‌هاست ندیده‌ام. مشتاقند از ایران بشنوند. تصویر تجمعات شبانه برای‌شان شوق انگیز بوده.
دکتر محمد از اعضای حزب‌الله است، می‌گوید من فکر میکنم مردم ایران از زمان ارتحال امام تا زمان شهادت آقا خیلی رشد کرده‌اند. درسته؟
تصدیق میکنم.
اینرا کنار مزار سید حسن نصرالله می‌گوید و مرد ورزیده‌ای را نشانم می‌دهد که محافظ سید بوده‌. می‌گوید این مرد ورزیده بعد از شهادت سید، عمل قلب باز کرد. و من یاد سحرگاه ۱۰ اسفند می‌افتم که بین مرگ و زندگی دست و پا میزدم.
﻿
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/694413" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198ec3ad92.mp4?token=OFDSVMLteceTrkueggzut3k45g_Xk8oyX8KsJ3zpKHkgbiHU-hnLMqoONdN1ccT8th0DSrC6bXbhAx1Uh65Jd6Q8DK_nys6_isPyWyMjV2wGYQvjGrCf5hHlbKsnxDBZ6w-lftwu1QztSvMujlQOoj_LC46BLkCCAonp_IBFoPexrRZ1ZW-JMFkITfmHenufbTcOsziMllKOREFScCYwK5ZP4fv85nSMoJzBHrNjf_AkX63NTCklLAY9A3VpdAShO_1qTA1_PL-TapOD3a6TmzWZs4w8OgAGBOmpxzZnYP2wlZ1vfYkbF7fVrofiv10LB8QLiT53fS9hNQhmmCvUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198ec3ad92.mp4?token=OFDSVMLteceTrkueggzut3k45g_Xk8oyX8KsJ3zpKHkgbiHU-hnLMqoONdN1ccT8th0DSrC6bXbhAx1Uh65Jd6Q8DK_nys6_isPyWyMjV2wGYQvjGrCf5hHlbKsnxDBZ6w-lftwu1QztSvMujlQOoj_LC46BLkCCAonp_IBFoPexrRZ1ZW-JMFkITfmHenufbTcOsziMllKOREFScCYwK5ZP4fv85nSMoJzBHrNjf_AkX63NTCklLAY9A3VpdAShO_1qTA1_PL-TapOD3a6TmzWZs4w8OgAGBOmpxzZnYP2wlZ1vfYkbF7fVrofiv10LB8QLiT53fS9hNQhmmCvUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدری در تهران پس از قبولی دخترش در دانشگاه دولتی، ۶ آپارتمان ۸۰ متری به نام او خرید
او درباره دلیل این کار گفته:
🔹
یکی را برای خرید ماشین، سه‌تا را برای خرید خانه و دو تای دیگر را برای تأمین هزینه‌های زندگی و اجاره در نظر گرفته‌ام.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/694412" target="_blank">📅 00:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi02h1qEU2RQSbcSCFHlHdtChBYJ6ApkE5NBQC1gW8YS8kTr5Dp4clzQpX8uSHtvF9cnR_9lCCbD1KVE-keqWWoLi-h8p8w29ctlPJbTHCfmU_bsk474qMKC9-IFkEnxuCTUEccO71EdMiTVSCg08fePwez5MtUCOUahaXkTiEKDHT6C25pd9B_Rn_32JsYBAL-N2kbWLza3Z4qQT83w36fsnj63wIou66motWeA0F4MgGi2uCbToyCWA8zzifUmhNlWZEzRupDWfpbuQA3wCM_78-h9bSCV6BGhsomsWrAmzjJ8iY1tDT-CmGl1Su_jZuY3ZAKMFjAtk0aJKXGNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/694411" target="_blank">📅 00:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
در لابلای خبرها، پربازدیدترین‌ها را از دست ندهید
🔹
🔹
ماجرای چاقوکشی در کابین خلبان | دسیسه جدید اسرائیل برای پرونده‌سازی علیه ایران؟
👇
khabarfoori.com/fa/tiny/news-3248971
🔹
طرح جدید آمریکا علیه اقتصاد ایران: احتمال محاصره زمینی، پس از محاصره هوایی قوت گرفت
👇
khabarfoori.com/fa/tiny/news-3248887
🔹
پشت‌پرده ادعاهای جدید نتانیاهو | آیا ایران به زودی به اسرائیل حمله پیش‌دستانه می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3249092
🔹
قدرت خرید خانوارها آب رفت؛ کالابرگ چقدر از سفره مردم را پوشش می‌دهد؟ | شما نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3248958
🔹
یک تجربه متفاوت برای صرفه‌جویی در انرژی
👇
khabarfoori.com/fa/tiny/news-3248841
♦️
برای خبرهای بیشتر، کافیست کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/694410" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=WqAL-q-IFWgdYe59cNHkqxOP5T8iAVTRnLxkvA_qbdCJ-gNy_mDIM5VetWeq69eGB1c_fi8Zb3PhAvZ3j9dvk59KHmnPP5jTyayVflcLstkbWAXEkrRoiff1toFFV1SFMbq9JpPXyxISZIzbbB3A1_vqaLJIYrjh2f92u-RCkuzEPIci1HTgWal84j4q1AfPVcgUnRXzPX9gaLz42cgYFqf_QY0KD99w75n2eUS78Pl1OatAGJQbUhaDzsxg16galuNL8itIfTChsF8WBP2fC5qD98r8ffLDLqqz7WUQyZ0SsEy_ZbwwGkKL-mE0_j3dq1ffxzw1KNf4EGSU_PzeOWxfdHa2FYUoWytXyufls_D8ltnX41sOuCamEa2WbvV8oSrtVfpm6hgFJDH63lrTxN6LWnl7IpWtbXKwUDREyOZgkczOvojzWg3VxlJLD5DKINrw3n0nSbH-TWtFIyzoi8xHjSc04NfKco3WkIziCklzzcv7pCY4XrhLXbzLcbf02ocXVidEHywns0b-nPdT7wtaAPSBi9S_oGueIej9DhJcbZp6UgnDzIBh7_aINdK64pt83ZyYCZVjRaVlv4Nt6TE9wuGGHNju34dTgyxN-CQOnMzCjyRsR3DvBKUF1JP4FZ5uoqN8SWRhMhKjo4m944oS6QuH2rp2oky0RQKt4UY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=WqAL-q-IFWgdYe59cNHkqxOP5T8iAVTRnLxkvA_qbdCJ-gNy_mDIM5VetWeq69eGB1c_fi8Zb3PhAvZ3j9dvk59KHmnPP5jTyayVflcLstkbWAXEkrRoiff1toFFV1SFMbq9JpPXyxISZIzbbB3A1_vqaLJIYrjh2f92u-RCkuzEPIci1HTgWal84j4q1AfPVcgUnRXzPX9gaLz42cgYFqf_QY0KD99w75n2eUS78Pl1OatAGJQbUhaDzsxg16galuNL8itIfTChsF8WBP2fC5qD98r8ffLDLqqz7WUQyZ0SsEy_ZbwwGkKL-mE0_j3dq1ffxzw1KNf4EGSU_PzeOWxfdHa2FYUoWytXyufls_D8ltnX41sOuCamEa2WbvV8oSrtVfpm6hgFJDH63lrTxN6LWnl7IpWtbXKwUDREyOZgkczOvojzWg3VxlJLD5DKINrw3n0nSbH-TWtFIyzoi8xHjSc04NfKco3WkIziCklzzcv7pCY4XrhLXbzLcbf02ocXVidEHywns0b-nPdT7wtaAPSBi9S_oGueIej9DhJcbZp6UgnDzIBh7_aINdK64pt83ZyYCZVjRaVlv4Nt6TE9wuGGHNju34dTgyxN-CQOnMzCjyRsR3DvBKUF1JP4FZ5uoqN8SWRhMhKjo4m944oS6QuH2rp2oky0RQKt4UY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور هیات ایرانی در منزل جوان‌ترین شهید مقاومت در بیروت
🔹
در این دیدار، چفیه و انگشتر متبرک آیت‌الله سید مجتبی خامنه‌ای به خانواده این شهید اهدا گردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/694409" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=d72GRWcMeaHC8a_50NNMW-RXXicXVxIVRTrg1cHFwUAgMo3aLkr-x31Op1K-mH6zaG5seQBok7ZiYvdqFA8_VrOFrAj_ic9IkLRFg-_12lh0QBO4zuBKlzD9tI4KjABXVUbftc2Jg-kI7NfqP_GSnN0Xc8tuNUMIFSUthlCxs5PwkbQgksRO2X0YbAA8dw5YCFAsaYV2hxbH9h2L0_4wpS4Rvl9SI1WhvudVf_A1ebfZYeC1OuSZComtr0ifgSwwsjGhblx0t1idWAoswp6j9Ia3A6KdFzOscP7fqePNQkOpPfL2saPbbX0279ZWed8slrvzhGhTpU3wEAtxxjFaypMZeUj31Mvj2_nTTx9pO8sFY3yICNCxe-Gbxll96fbdxiLR9ZLyPd7i-Dttfm3f2TWvJ1agu1K7NZGQMbIo_s8fcV31eO0HQ8LZSl3AawYf2L39hkBs82F5tSMfIKfkACvoS6NtobFHH4hBuQ09BnKJS6qw2H0MXwTBLcSOWeh1ujv95dX3KEDaaLbb5jYtPzxYxBWPK5eVVmrAjxQSwUyDsxi4fUMWcMT-p5qbPbqGtUbX4cp9-z2utSXB4i150CCvCBJkzeffvQVZoAObY1L6iItW63BzJQiEs-UHyXHTNthA6qWOAjwshb2kQiI9wPuBCOFxE_RQg1jZzkH9KBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=d72GRWcMeaHC8a_50NNMW-RXXicXVxIVRTrg1cHFwUAgMo3aLkr-x31Op1K-mH6zaG5seQBok7ZiYvdqFA8_VrOFrAj_ic9IkLRFg-_12lh0QBO4zuBKlzD9tI4KjABXVUbftc2Jg-kI7NfqP_GSnN0Xc8tuNUMIFSUthlCxs5PwkbQgksRO2X0YbAA8dw5YCFAsaYV2hxbH9h2L0_4wpS4Rvl9SI1WhvudVf_A1ebfZYeC1OuSZComtr0ifgSwwsjGhblx0t1idWAoswp6j9Ia3A6KdFzOscP7fqePNQkOpPfL2saPbbX0279ZWed8slrvzhGhTpU3wEAtxxjFaypMZeUj31Mvj2_nTTx9pO8sFY3yICNCxe-Gbxll96fbdxiLR9ZLyPd7i-Dttfm3f2TWvJ1agu1K7NZGQMbIo_s8fcV31eO0HQ8LZSl3AawYf2L39hkBs82F5tSMfIKfkACvoS6NtobFHH4hBuQ09BnKJS6qw2H0MXwTBLcSOWeh1ujv95dX3KEDaaLbb5jYtPzxYxBWPK5eVVmrAjxQSwUyDsxi4fUMWcMT-p5qbPbqGtUbX4cp9-z2utSXB4i150CCvCBJkzeffvQVZoAObY1L6iItW63BzJQiEs-UHyXHTNthA6qWOAjwshb2kQiI9wPuBCOFxE_RQg1jZzkH9KBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مداحی عربی سعید حدادیان در محل مزار شهید سید حسن نصرالله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/694408" target="_blank">📅 23:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694406">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2c7mbxRNvHwaqXs9drlH_xBqglGV5wsv7wCxCOct5TfvcXE75aiu3vbsTEtk_KRwAqZktA35niDF-30dE0qpSgODz2kwY_OPjap-k2YXHrlpufxdpElzE7YTVBAI_ALvunj5UFZVrSgw-TPNvn9wMjVFfN3VCn7pt_HkP3c2zEHnfJJ3Ikp4gbZga5OLmnD803sRi3sHorpuDh3y0H5JMrt-FqAHHuQJwP0ejXLGeF4LzGRz5UufEwBZ_9nz5TeeK1i0LimcU6piDMwXsiLQs6XVL2XOP5PDi2eoN2MCzeDKYzNDlC_w6zWqoVjC55bmo4kcyaLu4SlLkO9iwjR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه چهارم ایران در توسعه اپلیکیشن و امنیت سایبری
🔸
مسابقات WorldSkills بزرگ‌ترین رقابت بین‌المللی مهارت‌های فنی و حرفه‌ای است که نمایندگان ۸۰ کشور در رشته‌های تخصصی با یکدیگر رقابت می‌کنند.
🔸
۲۲ نماینده ایران در WorldSkills ۲۰۲۶ شانگهای با کسب
۷ مدال افتخار
به کار خود پایان دادند؛ ایران در توسعه اپلیکیشن و امنیت سایبری نیز به
رتبه چهارم
دست یافت.
@amarfact</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/694406" target="_blank">📅 23:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2qyx0wOVRCsEU5DTT1Nr4qm_KHZZ2AMrEXPlQ0NWwX79-trhMM1dLSujyDBA3YX9fvygatYXM0clcUKZ7FlXcKTUEaSQuUDGC_CVa_roa6uDi4ovOdt8X6Ifmn6ZarN6mzuiSvWZuZC36Z1zNl2BKa7q3w8Q1SbL3wt_qx4R_93BTOfSzKWXpssclCvftY5l1l5Mbd2QYZIf1_nMVeDlBa4zM9UnVaVwPaSaBaPZNMoCdRD3_pX7FCbyl77z_lnk6bq55__feVf6yQ_H8o0qWxQQ_OEI1Mff2dxuP570ffNd_Hs9OmTOm-J9b1CZ-KvY1wi-gVHRoc9Ql2kelZhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت کنم، خدانگهدار تیم ملی پرتغال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/694405" target="_blank">📅 23:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d458bb77ec.mp4?token=BgUxhGhqrVrGuIvJ_K5J5_48jPTf0bvD89x4UEBBPbbeBz_g8ZPp18ktTLcwHTnpYS2Uct3a_bTplLS0pz58H0ME8uyNrricaJ-sT2aPUj3wIDHNb4flyTCIQuKQMLgn61KTJN-EslP32wPm446tmSFO2WFN01AJPT8l56DTt3UrXleVESAY2O6tdA4Ej2QPFx5IY2MSmMvEd6wzOywMIsj061MBvQC7z27SGIbIkBmcqJg64TmFySlVVCY4AbIqGVRctfp2_ybYtkTo1lZFPqiyCSo8Ov92WYo7ZHDTS4svHRLbgcDc2Fu-IopMkjQfdXWViN3jfXEMRqPbYG2w94i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d458bb77ec.mp4?token=BgUxhGhqrVrGuIvJ_K5J5_48jPTf0bvD89x4UEBBPbbeBz_g8ZPp18ktTLcwHTnpYS2Uct3a_bTplLS0pz58H0ME8uyNrricaJ-sT2aPUj3wIDHNb4flyTCIQuKQMLgn61KTJN-EslP32wPm446tmSFO2WFN01AJPT8l56DTt3UrXleVESAY2O6tdA4Ej2QPFx5IY2MSmMvEd6wzOywMIsj061MBvQC7z27SGIbIkBmcqJg64TmFySlVVCY4AbIqGVRctfp2_ybYtkTo1lZFPqiyCSo8Ov92WYo7ZHDTS4svHRLbgcDc2Fu-IopMkjQfdXWViN3jfXEMRqPbYG2w94i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر بیژن مرتضوی در واکنش به بازگشت او به ایران: او با خواسته قلبی خودش و برای دلتنگی وطن و برای ماندن در کنار مردم در شرایط جنگی وارد ایران شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/694403" target="_blank">📅 23:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d514ae73.mp4?token=YcBibjN4EK4sntphDB_Fn7bU-tUO5hKN9VVIbJIjVr3rvi0s0Yh9l6cO7Uw2_PjxqXv8LaDhn9jm-g9cCPwC01vNUB-demv1_h6OXY_rRVkKDBK-tzkGOT66JmGayfJEF6IdoFqACHHzi2_qNXTZaKb-rVofzZVlcAopkkA5vwNsPfm-9vhnrFQjXExpoDBmfb9KngzA19ne0DoJslOxeBda89K_I8yzYUW7tz1l7lZczRRpNPNB3zCaAJZzCR89iGTc-_z0URrP-bOfKNI0rrxqHuiu6UjULjbmq6PkweE6dhn2f-EHfts1LsBYmv_2l9fGUZmEVejoTGMk6K1rQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d514ae73.mp4?token=YcBibjN4EK4sntphDB_Fn7bU-tUO5hKN9VVIbJIjVr3rvi0s0Yh9l6cO7Uw2_PjxqXv8LaDhn9jm-g9cCPwC01vNUB-demv1_h6OXY_rRVkKDBK-tzkGOT66JmGayfJEF6IdoFqACHHzi2_qNXTZaKb-rVofzZVlcAopkkA5vwNsPfm-9vhnrFQjXExpoDBmfb9KngzA19ne0DoJslOxeBda89K_I8yzYUW7tz1l7lZczRRpNPNB3zCaAJZzCR89iGTc-_z0URrP-bOfKNI0rrxqHuiu6UjULjbmq6PkweE6dhn2f-EHfts1LsBYmv_2l9fGUZmEVejoTGMk6K1rQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصور کنید تخم‌مرغی که میبیند، اصلا از مرغ نیست/ تولید تخم‌مرغ مصنوعی در چین
🐣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694402" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a96b8f8a.mp4?token=B0hOCmames_DSLQlMlPLLG2nz3kMEdx3lxm4TR1cUo1lvTZHSPxYF6LiEGrhWIXcbBG6Ea2HmSXRhWeUlUtm5rfCSMCfIleVW_tcxHoBxKGJOkXFagUM1srmCdZgPE4sJHFU-lIIHIOn5AYCpULty5hjqsb05VORhvyt1-ytbAXUEOw9qPC89M82HLmZDkabhplLMTHLjJtPOwerr8PZkuwUfSdSxApsRj1sLVAZnhDsDKAfX5k0U1gl6ihjb0X3mxejSxn3EIv9woGkUxOAUjIz3bJV4wTvYvQ27TPwn-huISy_QcWVRO46Xd67DxYmbQd6_HxxatcELFJ8inJiLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a96b8f8a.mp4?token=B0hOCmames_DSLQlMlPLLG2nz3kMEdx3lxm4TR1cUo1lvTZHSPxYF6LiEGrhWIXcbBG6Ea2HmSXRhWeUlUtm5rfCSMCfIleVW_tcxHoBxKGJOkXFagUM1srmCdZgPE4sJHFU-lIIHIOn5AYCpULty5hjqsb05VORhvyt1-ytbAXUEOw9qPC89M82HLmZDkabhplLMTHLjJtPOwerr8PZkuwUfSdSxApsRj1sLVAZnhDsDKAfX5k0U1gl6ihjb0X3mxejSxn3EIv9woGkUxOAUjIz3bJV4wTvYvQ27TPwn-huISy_QcWVRO46Xd67DxYmbQd6_HxxatcELFJ8inJiLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶
عادت روزانه برای محافظت از سلامت چشم
🔹
این چند عادت ساده که می‌تونه به حفظ سلامت چشم‌ها کمک جدی کنه رو جدی بگیرید تا در طولانی‌مدت، کمتر با خستگی و آسیب‌های چشمی مواجه بشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694401" target="_blank">📅 23:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8266cea7.mp4?token=SAVtCj4uJHDuMJUu2mVWklXMopS6PKZCrM2-G8QQLz-m5l84vtVD_B9X3IljCZSTLhmF7CaOGGKOeThIZBFUhG23gO-gd0RDwpTg3P-VWSv78_xUy0vXL0r3aP4ZPxnnybd1GebsBL1bxXDkTOymIAQCYaalc9r96O3dzOqj5E1CEVi6lMLd5MZu-1GVF1m8Kx6J1hS-PQSXZSQojegv6O0EzAZcKKXjSYm4Q3cByCIivwqH23ci4HovYhIouYaBzPsO1pt0B3O0pxevcBJNXQXNGGJki79idJAf51tQt-Jk2FjbIFxgRYFWyGZDOnbmqtc_i9UPHU0d_xDIJUFFzTUEdtNrT3fOVNYMUWpvjBOuXLwyVhQY1RmqThXjjcqoLjecsxOyl5ulkD8_YNcNFtIJ_qMR3N0CwYcRWLnYDSeV-XZJBvSSiY8rwkb_5p1JVvupzXW1S670_NaAa00YYwRI62JVI6wZNvDEEAK9g6zFX3VwV9jNthMDIh2xLMhKtdQjZ0DEb51QZFvSPCx6yr-XDimlyG51J8OcZ8Eas7Cm_KZyxkafW_7KSte4KnM2bu56wzobeiTxdNzW7E3SppUDZ_oLSdZ1V7jJBsi-zEXR9uU60HjBOxwAVwl_ZFdjcD0b3Xz5GtPuilU7uBo0KLE7yU1cMFrcA54f8zoM21E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8266cea7.mp4?token=SAVtCj4uJHDuMJUu2mVWklXMopS6PKZCrM2-G8QQLz-m5l84vtVD_B9X3IljCZSTLhmF7CaOGGKOeThIZBFUhG23gO-gd0RDwpTg3P-VWSv78_xUy0vXL0r3aP4ZPxnnybd1GebsBL1bxXDkTOymIAQCYaalc9r96O3dzOqj5E1CEVi6lMLd5MZu-1GVF1m8Kx6J1hS-PQSXZSQojegv6O0EzAZcKKXjSYm4Q3cByCIivwqH23ci4HovYhIouYaBzPsO1pt0B3O0pxevcBJNXQXNGGJki79idJAf51tQt-Jk2FjbIFxgRYFWyGZDOnbmqtc_i9UPHU0d_xDIJUFFzTUEdtNrT3fOVNYMUWpvjBOuXLwyVhQY1RmqThXjjcqoLjecsxOyl5ulkD8_YNcNFtIJ_qMR3N0CwYcRWLnYDSeV-XZJBvSSiY8rwkb_5p1JVvupzXW1S670_NaAa00YYwRI62JVI6wZNvDEEAK9g6zFX3VwV9jNthMDIh2xLMhKtdQjZ0DEb51QZFvSPCx6yr-XDimlyG51J8OcZ8Eas7Cm_KZyxkafW_7KSte4KnM2bu56wzobeiTxdNzW7E3SppUDZ_oLSdZ1V7jJBsi-zEXR9uU60HjBOxwAVwl_ZFdjcD0b3Xz5GtPuilU7uBo0KLE7yU1cMFrcA54f8zoM21E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجلس تعطیل نیست؛ وکلای ملت در مدار تصمیم و پیگیری
🔹
گزارش صداوسیما از جلسات مستمر  نظارتی و تقنینی صحن علنی و کمیسیون‌های تخصصی مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/694400" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff253eeddb.mp4?token=GaVrIvhbGEsaTPby3FGlNPZ63PIZzGz5QBlHBWPvzJ2p-sAr3d_Sh79YupDoFsA1KP2gicb_CjffQ1nOAaOdyFkWYgRWkPeW6mh1bhkm-7UPSKn8T5SZntE70SJajGj-55WXy81LL1db8GRXt5ZCC71Nsj7syJAmWJVtmFWSphaL1akDDTL8IP_e36eO-mTn4K5AlUDwaQzTU4IaIACpdFkPTolV-2N3KsPiKiPwX8FVsxNornEfKBwEw5r-h-ttnujocSjXFWhWSU2mpm1wBrXnw2Cyxh5xRK3t0ZoRt0O8jN6IkbFCUYJkr9f4jOLwHihfGBqsTP9dx0cZYdTRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff253eeddb.mp4?token=GaVrIvhbGEsaTPby3FGlNPZ63PIZzGz5QBlHBWPvzJ2p-sAr3d_Sh79YupDoFsA1KP2gicb_CjffQ1nOAaOdyFkWYgRWkPeW6mh1bhkm-7UPSKn8T5SZntE70SJajGj-55WXy81LL1db8GRXt5ZCC71Nsj7syJAmWJVtmFWSphaL1akDDTL8IP_e36eO-mTn4K5AlUDwaQzTU4IaIACpdFkPTolV-2N3KsPiKiPwX8FVsxNornEfKBwEw5r-h-ttnujocSjXFWhWSU2mpm1wBrXnw2Cyxh5xRK3t0ZoRt0O8jN6IkbFCUYJkr9f4jOLwHihfGBqsTP9dx0cZYdTRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات هگست جنایتکار: ابرهوش (هوش مصنوعی) شرایط جنگی را با گذشته تغییر داده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/694399" target="_blank">📅 23:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa-aP7Riwy8JAqVW0Qbs8nFBcWRwUVEZ53uFGMT-QGHFVjbe2EpQeE-AcGrA7z4d0yz_z2yMHJAviNqTAfImkOo8YBBSsAVkpteMpuhjo0dj2WFCsqzS0C4hatPLc0m2AQEeNEHb1zcg8x5x5nxxCG33N92qyUM36kZ_u3gAudPbImj3jN2eog7zRoseUhCFtS-cvXCVrHDPxtUMdHF5p8ZYYnzGlmXMJg9tnvJEwmIVptcQhpz7etV4uJY0l1OykVC5ml2ieqfqSjMrWTM2EhIrcrdDX9FqxttUjaARRZlYuAMhd-vibvrhZ_Yfks4IZXhllLKCqwyjhz7lrRFUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده ادعاهای جدید نتانیاهو/ آیا ایران به زودی به اسرائیل حمله پیش‌دستانه می‌کند؟
🔹
تحلیلگران نزدیک به نهادهای امنیتی اسرائیل معتقدند که نتانیاهو در تلاش است ایرانی‌ها را به این باور برساند که اسرائیل از پیش موافقت ترامپ را برای حمله دریافت کرده، تا تهران را به «حمله پیش‌دستانه» سوق دهد و در نتیجه برای پاسخ اسرائیل مشروعیت بین‌المللی فراهم کند. به عبارت دیگر، آنچه نتانیاهو از آن سخن می‌گوید، ممکن است بیش از آنکه پیش‌بینی یک حمله قریب‌الوقوع ایران باشد، تلاشی برای ایجاد «پیش‌دستانه معکوس» باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249092</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/694398" target="_blank">📅 23:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694397">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رئیس پیشین پژوهشگاه میراث فرهنگی: مواردی دیدیم که نماینده مجلس دنبال گنج و دفینه است/حتی امام جمعه یک شهر در حفاری قاچاق حضور داشته است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694397" target="_blank">📅 23:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4388ac600e.mp4?token=HcrOZCuG75-Ie0afIV-47pTRVe-qegQ7ZK4Cra0SWXH4BmzFoPDCYGRfz3qircFPrpV1v3BynI5DwddNy05f9IoN5dHeEsygg7L7f4mPGEh6GUzN8aapHWbM0VWVR_ZF-hEqj-RtXWUsyRZd5f-Uw0gzgBHh7cJflxgdX-g1LbfbmfoeLz2MwHuf5fw-6YMs877HbHksqyCJuFVUfZmuWIUhlfx9G8E_6sHHGpgzA_gXa8Tc2VhsvUIoAZwt0zcIpmn3oN2VWX5GwSn-XI7uRW6vJSE-6a879mqjgO6EhQ7J9ajcs91qwGtoB8Jyv79HVHyNyQfuIeWuJEQMwMJwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4388ac600e.mp4?token=HcrOZCuG75-Ie0afIV-47pTRVe-qegQ7ZK4Cra0SWXH4BmzFoPDCYGRfz3qircFPrpV1v3BynI5DwddNy05f9IoN5dHeEsygg7L7f4mPGEh6GUzN8aapHWbM0VWVR_ZF-hEqj-RtXWUsyRZd5f-Uw0gzgBHh7cJflxgdX-g1LbfbmfoeLz2MwHuf5fw-6YMs877HbHksqyCJuFVUfZmuWIUhlfx9G8E_6sHHGpgzA_gXa8Tc2VhsvUIoAZwt0zcIpmn3oN2VWX5GwSn-XI7uRW6vJSE-6a879mqjgO6EhQ7J9ajcs91qwGtoB8Jyv79HVHyNyQfuIeWuJEQMwMJwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختاپوس‌ها به‌دلیل نداشتن استخوان، می‌توانند حتی از کوچک‌ترین سوراخ‌ها نیز عبور کنند
🐙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/694396" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PltG7nqrlVdZiOJDUEv5_zAwGKFb3cHPbTHDobEMcntgRQXlHCiAISxM7OBSf3RwrCFNSwj2RwU2z05NpT0t6U-LXuGjGble-BxalW6nTGOjyaxH2nUeI2xnQcZ63c9J4bRz7yg5eiD9c0QjMAqW7Sixmrpz6qBAgseOqDYJvsE91l8Atwhw0yAQljhPbyU8SVKIw22so-X0KKxFvKZTHyv0hC3S9ZrOLOH4AtAzFay-hADbQlZ_q2tKFgUZcX3HZ7GY1jFdrjIXflNOVXOxnQW24ujfx0ZyjSw2d2muycSsFMK3JjwPntzIn9C92DQZfao1SNEVANU19ods0GAd6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مینی صهیون
🔹
طی روزهای اخیر حکومت امارات در اقدامات آشکار نقش اسرائیل منطقه ای را علیه ایران بازی کرده است. از ادعای مالکیت بر سه جزیره ایرانی در سازمان ملل تا دیدار  نتانیاهو و محمد بن‌زاید که بنا بر گزارش‌های اسرائیلی، ایران یکی از محورهای اصلی آن بوده است. امارات در سال‌های اخیر به اسرائیل نزدیک‌تر شده روندی که می‌تواند به معنای بازی کردن نقش اسرائیل در برابر ایران از سوی یک همسایه باشد.در مقابل، ایران درباره پیامدهای بسیار خطرناک حضور اسرائیل در منطقه هشدار داده و تأکید کرده کشورهای منطقه نباید اجازه دهند از خاک و ظرفیت آنها برای اقداماتی علیه ثبات منطقه استفاده شود؛ هشداری که نشان می‌دهد همکاری امنیتی همسایگان با آمریکا و اسرائیل، از نگاه ایران موضوعی قابل اغماض نیست.
🔹
هشتصدوهفتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694394" target="_blank">📅 23:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694393">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSr4796TLrCd8FJ6t-IbYh1DpGi2UiSxHbvOEKxZvKqA47gIS5_gWteV4qlodghAA6ifUQ7s0YuJUn7pThunTlxU_kDlgKy-ZwD5nzeFDnnxI_afik4Sct6aZgtYmE3jMibJAqK3ogIjyoEQjRpthU5AXCL8cEpbGAd6EBUixy466JDC3NPMNS7ly4QeCs2O7A6tOSouCHKBcZLTWK4KshQUFHwIuPukYKRH11OA3N3IUzFZCgQWCZ2fKhpeQRa3K4KNycauhO6ZO6SYXZzfMOH1Avk8l61yQixPbF2C6LEtXvabSJxrH3TiDvKNc2UwrIV88TD0pkuFb6wwEiXntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژیلا صادقی وارد لبنان شد/ اولین استوری پس از ورود به لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694393" target="_blank">📅 23:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694392">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اظهارات مضحک وزیر جنگ جنایتکار آمریکا: بخاطر عملیات چکش نیمه شب ایران هیچوقت نمی‌تواند سلاح هسته ای داشته باشد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/694392" target="_blank">📅 23:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694391">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bb44b9f4.mp4?token=YgUBNr51pMCrVoI_UJpkAmyK0Sfd4mGMp1cxIuHkb2I8rLcVkec14FyIpittJkAnv5uHJmtqFBEsGoGAfjQgxlWCwOb1KcU4iAgDUahIE_kcYFm2nFa0AUKHx2mXAjeeWxArEUj5AtDM4a7Iva8gRODvcwNRYmbBWmRCBzvZBtPbhLtVM7Xjm3EIU63DxggtDTmoZms4EjFRZ6N3El5ciDDltVMjxg82b_aA9mdcCqaSakcKs3mRff-JOW-wSWMOXAM2pUk-tQ-_-rrf-LBYSdF95ExXZuTWczWEy1eEHmr8cvLmeZ6acJTW998vXIQkGg1kSMfhPMOR-M-JPlcyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bb44b9f4.mp4?token=YgUBNr51pMCrVoI_UJpkAmyK0Sfd4mGMp1cxIuHkb2I8rLcVkec14FyIpittJkAnv5uHJmtqFBEsGoGAfjQgxlWCwOb1KcU4iAgDUahIE_kcYFm2nFa0AUKHx2mXAjeeWxArEUj5AtDM4a7Iva8gRODvcwNRYmbBWmRCBzvZBtPbhLtVM7Xjm3EIU63DxggtDTmoZms4EjFRZ6N3El5ciDDltVMjxg82b_aA9mdcCqaSakcKs3mRff-JOW-wSWMOXAM2pUk-tQ-_-rrf-LBYSdF95ExXZuTWczWEy1eEHmr8cvLmeZ6acJTW998vXIQkGg1kSMfhPMOR-M-JPlcyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تنظیمات، قدرت WiFi کامپیوتر و لپ‌تاپت رو می‌تونی به بیشترین مقدار قابل تنظیم برسونی و اتصال وای‌فای پایدارتری داشته باشی
💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/694391" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 2- میدان دوم، مروت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694389" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان دوم - مروت
🔹
مروت به معنای جوانمردی‌ ست و با روانی نرینه که درون تمامی افراد چه زن و چه مرد وجود دارد باید صورت گیرد، درواقع این امر که بر خودسازی نیز گذر دارد هیچگونه ارتباطی به هیچ‌نوع جنسیتی ندارد
🔹
بازداشتن نگاه از اطرافیان زمانی که دچار طمع و توقع می‌شود، اصلی‌ترین پله برای دستیابی به مروت می‌باشد؛ همه را یکسان بدانید و با مرامی جاودانه برخورد داشته باشید
🔹
با خود عاقلانه_با خلق به صبر_با خدا به نیاز رفتار شود
🔹
احترام به نفس سبب آرامش درونی و بهتر زیستن و در مقابل همچنین باعث بهتر رفتار کردن با دیگران خواهد شد؛ و در آخر خواهید توانست خالق خود را همچون معشوق خود دانید و از دل و جان دوستش داشته باشید
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/694389" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4772c9c21.mp4?token=kr4Xq-4Qf5dlmL5IhaY-z0uVihW54G0pCBOB0r7AirK8Ug2qC9tSwhN3qIaeePOOsdSO36Jt7BdG7di-CZJhKh7Zq-gyPMm-OlO260CJ-WqzW5n-yJWMC3Pzb3J33ZO3ZRURblJsGoRrJnCkIrLZHQDTQ_Q0UUS5lLAY4ARVKzXqJ8fmPFjcvGJ1NlF5jA16g0zoh0ZiFvBAwNGhudMna_rf-pzYmLwA_BqfWKnRXIStj9JtH_haak_MsNM3NY3J-Nck2-FIDjd8_wiKxsFboxz0vy6kQiAqnIpHgscYN5INvwXvEvBNZehQxnZ-x57oSRElLdMFfPW9KJSaTwUwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4772c9c21.mp4?token=kr4Xq-4Qf5dlmL5IhaY-z0uVihW54G0pCBOB0r7AirK8Ug2qC9tSwhN3qIaeePOOsdSO36Jt7BdG7di-CZJhKh7Zq-gyPMm-OlO260CJ-WqzW5n-yJWMC3Pzb3J33ZO3ZRURblJsGoRrJnCkIrLZHQDTQ_Q0UUS5lLAY4ARVKzXqJ8fmPFjcvGJ1NlF5jA16g0zoh0ZiFvBAwNGhudMna_rf-pzYmLwA_BqfWKnRXIStj9JtH_haak_MsNM3NY3J-Nck2-FIDjd8_wiKxsFboxz0vy6kQiAqnIpHgscYN5INvwXvEvBNZehQxnZ-x57oSRElLdMFfPW9KJSaTwUwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ساواک سرکرده منافقین را اعدام نکرد؟
محمدرضا سرآبندی، نویسنده و پژوهشگر ارشد حوزه امنیت:
🔹
در حالی که تمام بنیان‌گذاران و کادرهای رده‌بالای سازمان در ضربه سال ۵۰ تیرباران شدند، مسعود رجوی چطور از اعدام قسر در رفت؟/ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/Zo0LTywDKh8
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/694388" target="_blank">📅 23:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال اطلاع رسانی جانفدا</strong></div>
<div class="tg-text">🧩
لگویی ها هم به آموزش نظامی-امدادی جانفدا پیوستند.
@ir_janfadaa</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/694387" target="_blank">📅 22:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij6KxGXFJUxCZQ6jDJknPof5WX_e5c2-AnqqrMvWU2zBSbmijOOAuLUs5y03rQeI6gwggBCoQSJ9zHKEyEl-glZYvXIsF_3pHkBBrFn_tRwRlT8pMIIDwmYQuA9a0fLLtqa_JN3n8gvsP6f6fRj0g0PdyW8I1scOvZCMhCAG3Z46VfTER4y7RfeyNkP0ybk5z1zdtmiBTkFamz34AoFFoVqq77AWC_6buoTraqsbX4VXCb03wCSwShAzuQg0ZX4VIpYLTPlU6gWVt_8wWbP7MxuziHh2pYEGEqDraTDiZ41Vbm9W2oXXO7YvD4z1obEo_SBXZumsruoGXsEoj8HXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وکیل امیرتتلو اعلام کرد تتلو امروز یک زندانی را با کمک مالی خود آزاده کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694386" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اظهارات خصمانه و مضحک وزیر جنگ جنایتکار آمریکا: کشورهایی مثل ایران تیترهای فریبکارانه درباره روحیه پایین سربازان آمریکایی می‌گویند/ نیروی دریایی، هوایی و کل دفاع ایران از بین رفته است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694385" target="_blank">📅 22:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de8888e46.mp4?token=LilNYhWDnb64urkQ9KBr9Rh8NykNNEOngNt5MQS_wOPbiBQ_vvWLe3v7QA3BfRLj9SrdQpDxUReYSg7iPxIqBrozIJcVJ5RHhwJ0xRioHlk1kYdlpqew5UEQdqwRozw_3truhOxOmZoP_nSqLDIe4m2jntLnehihOayqS76Z-Nrg-NR09nFow8oqIQU90TZjNrS5lp9pBwVcufi1mT2cqXtp4RnEbqFazrrL6S6dgT8PkPZqFwJzFI0EC49LZWghVbBQ8fD5lMckK9WXmQVRD0ZRjKOCCxKyLpXBI_svyInCKdBclCc2S44B5iM6jACU74_RCH2D_bvSRdCxox2wUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de8888e46.mp4?token=LilNYhWDnb64urkQ9KBr9Rh8NykNNEOngNt5MQS_wOPbiBQ_vvWLe3v7QA3BfRLj9SrdQpDxUReYSg7iPxIqBrozIJcVJ5RHhwJ0xRioHlk1kYdlpqew5UEQdqwRozw_3truhOxOmZoP_nSqLDIe4m2jntLnehihOayqS76Z-Nrg-NR09nFow8oqIQU90TZjNrS5lp9pBwVcufi1mT2cqXtp4RnEbqFazrrL6S6dgT8PkPZqFwJzFI0EC49LZWghVbBQ8fD5lMckK9WXmQVRD0ZRjKOCCxKyLpXBI_svyInCKdBclCc2S44B5iM6jACU74_RCH2D_bvSRdCxox2wUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریزش و نازک‌شدن موها گاهی می‌تواند نشانه کمبود برخی ویتامین‌ها باشد/ ویتامین‌های مؤثر بر سلامت مو آشنا شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694384" target="_blank">📅 22:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1896c5e643.mp4?token=bs4FHc9OyMG_HhmC31Sua0zKIxA9strklfFWJbth4FbyP8IZpoOWwGKK6ZHpb0fZ3T8rD-1KvG7z97349uCKQzsiQeE_bsTeYCGu244iRHFsPkSQhRj2V6aCKIVVppqyREaX49Mc8x5IuY3cVtl2EEdmKiscRMFLYq3fE-EGaqQu4b7PXQ_-PB5Hgd2YHEnCuTDaDVDHazwbe8AglOh_BbsLc_1xFSt_z1kAvXeoOBs2x9NhxB-4QYASgtdA9qSvO2wQaBWSNn6_WhUA5TqFshfPq2Ab_sEwi-vgPFrHaFQLRgeGXHlnLJ77biLN2jUDyACaqqTp-C0912YSxtb6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1896c5e643.mp4?token=bs4FHc9OyMG_HhmC31Sua0zKIxA9strklfFWJbth4FbyP8IZpoOWwGKK6ZHpb0fZ3T8rD-1KvG7z97349uCKQzsiQeE_bsTeYCGu244iRHFsPkSQhRj2V6aCKIVVppqyREaX49Mc8x5IuY3cVtl2EEdmKiscRMFLYq3fE-EGaqQu4b7PXQ_-PB5Hgd2YHEnCuTDaDVDHazwbe8AglOh_BbsLc_1xFSt_z1kAvXeoOBs2x9NhxB-4QYASgtdA9qSvO2wQaBWSNn6_WhUA5TqFshfPq2Ab_sEwi-vgPFrHaFQLRgeGXHlnLJ77biLN2jUDyACaqqTp-C0912YSxtb6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات خصمانه و مضحک وزیر جنگ جنایتکار آمریکا: کشورهایی مثل ایران تیترهای فریبکارانه درباره روحیه پایین سربازان آمریکایی می‌گویند/ نیروی دریایی، هوایی و کل دفاع ایران از بین رفته است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694383" target="_blank">📅 22:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293ef9dc4.mp4?token=Xq5x_j_TgzP51rbq7vWwBCsoxdzPqQKziZFC4WobXZdBXbBiNtBsPRvWKq-qIoqi861FASVapYphlh7nlvhxhiBB7_g26JHtzXjwJbuzU_K4Sp7IWFwRmsCovKxJNuTN6n4f7FRLoKMO0K0WhF60ATCAiAKzVBpnzWf2s2wG8q2c8AGSNy3g42_zQaEiJeUbZSuqAbxxUtSSy8IN6NYCaY2eljSsp3eNLezF5zhFW_EXZkPfs3WjttqZXy6HCkj-5jJF-gkJYFgJBE_i7CND_v2YsCTKdICzVtMd6iS7yXdL6yX1-fyZq9pPoh3xcHPFyBJmkIDAQsVFnHnkA2jaxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293ef9dc4.mp4?token=Xq5x_j_TgzP51rbq7vWwBCsoxdzPqQKziZFC4WobXZdBXbBiNtBsPRvWKq-qIoqi861FASVapYphlh7nlvhxhiBB7_g26JHtzXjwJbuzU_K4Sp7IWFwRmsCovKxJNuTN6n4f7FRLoKMO0K0WhF60ATCAiAKzVBpnzWf2s2wG8q2c8AGSNy3g42_zQaEiJeUbZSuqAbxxUtSSy8IN6NYCaY2eljSsp3eNLezF5zhFW_EXZkPfs3WjttqZXy6HCkj-5jJF-gkJYFgJBE_i7CND_v2YsCTKdICzVtMd6iS7yXdL6yX1-fyZq9pPoh3xcHPFyBJmkIDAQsVFnHnkA2jaxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: کمتر از یک سال دیگر، ایمپلنت‌های نورالینک در مغز انسان کاشته می‌شوند و می‌توانند امکان دیدن طول موج‌هایی فراتر از محدوده دید طبیعی انسان را فراهم کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/694382" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOVEdCpt_ONdy75Lb-N_oPoelwlbJ2y-5btRK_GyTVhA2_CODVnJ8RZdW9AerYE8w09IcRx47tHLbFctwncMMBDp6bcJk2Lwmq_5bXl0jllDqoecrftsaoZMzRbPekRESA-2XppH-pT_n6JP1X_CqILZRIEDG9FPHuNdUeOVr1SNXbrXLP4FnyVuqJShptFzBcw2kGOxic42kat6I5fX2_nbZLF-nWC7MawJgSq1gcagwcwncjj0vbwSZrtYgOxtCsl3fnX6gNeVF83BKMlwXDDkSuBU623kEUqOSWs69qUHrX6X3JRoqqFPr5WJ671ZOIUpKSZ-as-LxhqZB0sNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رزمایش و اجتماع ۱۱۰ هزار نفری
جان فدایان استان البرز
📅
جمعه ۱۰ مهر ماه
🕣
ساعت ۱۴
📍
کرج، بلوار جمهوری
✅
اعلام حضور با ارسال عدد ۱۱۰ به ۱۰۰۰۱۱۸۸
#ایران_کوچک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/694381" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تصاویری از انفجار داخل نیروگاه حرارتی دمشق
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/694380" target="_blank">📅 22:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شلیک موشک از ایران به اردن در ساعات گذشته کذب است/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/694379" target="_blank">📅 22:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سردار نقدی: من از هوش مصنوعی سوال کردم که اگر بخواهیم برای مردم افغانستان خانه بسازیم، چقدر پول نیاز داریم، گفت که ۶.۵ میلیون خانوار در افغانستان هستند و می‌توانید با ۷۰ میلیارد دلار  برای هر کدام یک خانه بسازید
🔹
آمریکا ۳ هزار میلیارد دلار در افغانستان خرج کرده است و الان پرچمش زیر پای مردم افغانستان است. اگر کمتر از سه درصد از این مبلغ را برای مردم خرج کرده بود، پرچمش تا ۲۰۰ سال بالا بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/694378" target="_blank">📅 22:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر بخواهید یک رفتار اجتماعی را در جامعه بیشتر ببینید، کدام را انتخاب می‌کنید؟</h4>
<ul>
<li>✓ رعایت حقوق دیگران</li>
<li>✓ رعایت قانون</li>
<li>✓ صداقت و اعتماد</li>
<li>✓ مسئولیت‌پذیری</li>
<li>✓ همدلی و کمک به دیگران</li>
<li>✓ فرهنگ گفت‌وگو</li>
<li>✓ پذیرش تفاوت‌ها</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/694377" target="_blank">📅 22:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/694376" target="_blank">📅 22:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7fa291f3.mp4?token=ETDJt22BC-CZKEjSd341qhYQSYBNO42T7TrRJhQsynCUuSJ0Cns1uhhchEOTpBycomj7HWJ6H5tggeTw-Sqj0k8Me_K5EHzpqxjkox2pJ2_H-r7gUHPdmlCDQcma-PJzBdoZOb5IRs3Q_q9pCQDClujpkdosgT_ImQDK9OZkSYoBil-iIoMdiIwq0qsIolv49aStAHosadfc-hmzvtYtpJeq3g7XOvgVkp8S98Fo95W8I2ErH_mQnjqUdmuaOGa8Cw4aXefwMPFAX1JLtshv6DCJ9qpEXeHFMaKW1kBndS26yUOcSLxwfItaNFOsgRV8JSG9JjGq0TaRqfeTrapgPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7fa291f3.mp4?token=ETDJt22BC-CZKEjSd341qhYQSYBNO42T7TrRJhQsynCUuSJ0Cns1uhhchEOTpBycomj7HWJ6H5tggeTw-Sqj0k8Me_K5EHzpqxjkox2pJ2_H-r7gUHPdmlCDQcma-PJzBdoZOb5IRs3Q_q9pCQDClujpkdosgT_ImQDK9OZkSYoBil-iIoMdiIwq0qsIolv49aStAHosadfc-hmzvtYtpJeq3g7XOvgVkp8S98Fo95W8I2ErH_mQnjqUdmuaOGa8Cw4aXefwMPFAX1JLtshv6DCJ9qpEXeHFMaKW1kBndS26yUOcSLxwfItaNFOsgRV8JSG9JjGq0TaRqfeTrapgPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری منتسب به ریاض از برخاستن دود منتشر شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694375" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaXjER-xKMPHLEyVwxGczCMBo0IZxq-mVSKQB15GFdeZRddYpEl0dOTVws4R52kkl3d8hUb0ETPQ7x0a0BtbTEjuIvz7kAoNqW5Iv6uVvPQj2GC0-B1F1gBPXX3KP5azezpOVqP_ukksZw2y4aYRQA9L9E06lR3uk4hzMRNvJ9_fgIEvz1oPzB4GM7xPc_TXn0sBlJ4Go5vylASIeQlg02cWkZswpeqLDkUHCnV7OTC9NGW8SgKjFDpxNyDgYgQNsNDD6BprJzhmCb3xrGyJ-bSFXT68xRSbsUSqcvwEGEELlGruFokLoh2rYhMbyExA9hSn4QxTISLQi9Q__qwz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سنگین اسنپ‌فود به اتهام انحصارگرایی علیه این برند/ وقتی دو صفحه‌ خالی حرف می‌زند!
🔹
در سال های اخیر مدام اسنپ‌فود با این اتهام مواجه شده که در بازار سفارش آنلاین رستورانی در ایران، انحصار ایجاد کرده‌است؛ ادعایی که اخیراً نیز با حکم دیوان عدالت اداری نقض شد.
🔹
این‌بار پاسخ اسنپ‌فود اما نه بیانیه بود نه مصاحبه! این برند دست به اقدامی عجیب زده و فقط ۲ صفحه سفید در مجله اندیشه پویا به چاپ رسانده‌.
🔹
در این‌ صفحات فقط یک مربع صورتی می‌بینید که زیرش نوشته شده:
مساحت این کادر معادل ۱/۵ درصد از مساحت کل این دو صفحه است؛ درست به‌میزانِ سهم اسنپ‌فود از کل بازار رستوران‌های ایران در قالب سرمایه‌گذاری مشترک.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/694374" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfc2058ed.mp4?token=FXXzb3PiLKs2TeJCX8SLSX3AAEZ74Z8iY8FRG_4rpwhvIyKi2S4CBidEyNsfsIw1ihZUwWJzVBj4HNbim7OQNsmHsHq4o9nKw7y3MHTTJiW0lUXcgdiP5przGZ05p8OS44kKZ_dP3BrnIYIS_T8y5TgdMWZG2K45FJfiAbt4k-abLTfSY8R8rAQFKth8ampwvc5UyIvFIfzvchJMDjSjvmiyf8-6ynvOi_qOq8A3zRokRmMXjMJTgdXLsJ6SpEuh-ojw4GbwEwaeKKmCWME0XpIRnfHagzZuDMUBhr-1lJ3DO2x2VcT5iB1YFzeU_dxjTBXAazqxVBKWjy1PEkcmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfc2058ed.mp4?token=FXXzb3PiLKs2TeJCX8SLSX3AAEZ74Z8iY8FRG_4rpwhvIyKi2S4CBidEyNsfsIw1ihZUwWJzVBj4HNbim7OQNsmHsHq4o9nKw7y3MHTTJiW0lUXcgdiP5przGZ05p8OS44kKZ_dP3BrnIYIS_T8y5TgdMWZG2K45FJfiAbt4k-abLTfSY8R8rAQFKth8ampwvc5UyIvFIfzvchJMDjSjvmiyf8-6ynvOi_qOq8A3zRokRmMXjMJTgdXLsJ6SpEuh-ojw4GbwEwaeKKmCWME0XpIRnfHagzZuDMUBhr-1lJ3DO2x2VcT5iB1YFzeU_dxjTBXAazqxVBKWjy1PEkcmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خط گاز نیروگاه تشرین در حومه دمشق
🔹
منابع خبری از وقوع انفجار در خط لوله انتقال گاز به نیروگاه حرارتی «تشرین» در منطقه «حران العوامید» واقع در نزدیکی فرودگاه بین‌المللی دمشق خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/694373" target="_blank">📅 22:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695824e8cc.mp4?token=AyVis5Lmb9YSY7uQ0-chdphDKXmj6grY04KOo83HEPoWeUoVXym0_3Jm5thSAW630aet2vqTIUuAJXThU2sWj3ffcuH8dZARJliXfhIeGT6xGfTYU_73OPWTisoRYgxM-NbwMJfMqn9aUF-MJyXjJkcn6GRoIA-HNAWq_f2FheyejPOI75VANQCTSSefgqF0Yz-_yQj4J-Cf-tI74zBRVYvCXsUS5A-CptIWzCDFSSxofSTQjWh5eYA9ngUsMlhFZ_7Jp1_xiGYkoM1fV1ECTscicNtHIXoevMjQtiBkOzApp77WbvbOrHGEuAauGIB5tQ2OCC2spRBAiV0-PZs3rVixVkNZXNqpd_61RJkntE3QonUCtSJFkNvB-8TEoKkWPKbDV70eVJudp6XHwo8adf03fvKBS_OHOS6J5hutGcvWqPYG7ZGEv9QHQ9uiRKQOhaZFkQB5lDGQ98aiEGmU143X9GV45lk2RoROkFIvNHdSJj_yBOo8aNVrda_uoyswOBMAffKJKx8oxxK-yqro41ipVeVIkjXc0MuCUL278ck_fuG9EgN2y9mNpA_5OTmP3-MTgitcWDdAsl3Y2wlYWQdkGVPpzGKCdI5uroOsnhYf3kyEgRGXWqUkAu2hheYxaBncWFtBk71QwJb68mVothdUS5KhbHSiJDuHMf4ntBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695824e8cc.mp4?token=AyVis5Lmb9YSY7uQ0-chdphDKXmj6grY04KOo83HEPoWeUoVXym0_3Jm5thSAW630aet2vqTIUuAJXThU2sWj3ffcuH8dZARJliXfhIeGT6xGfTYU_73OPWTisoRYgxM-NbwMJfMqn9aUF-MJyXjJkcn6GRoIA-HNAWq_f2FheyejPOI75VANQCTSSefgqF0Yz-_yQj4J-Cf-tI74zBRVYvCXsUS5A-CptIWzCDFSSxofSTQjWh5eYA9ngUsMlhFZ_7Jp1_xiGYkoM1fV1ECTscicNtHIXoevMjQtiBkOzApp77WbvbOrHGEuAauGIB5tQ2OCC2spRBAiV0-PZs3rVixVkNZXNqpd_61RJkntE3QonUCtSJFkNvB-8TEoKkWPKbDV70eVJudp6XHwo8adf03fvKBS_OHOS6J5hutGcvWqPYG7ZGEv9QHQ9uiRKQOhaZFkQB5lDGQ98aiEGmU143X9GV45lk2RoROkFIvNHdSJj_yBOo8aNVrda_uoyswOBMAffKJKx8oxxK-yqro41ipVeVIkjXc0MuCUL278ck_fuG9EgN2y9mNpA_5OTmP3-MTgitcWDdAsl3Y2wlYWQdkGVPpzGKCdI5uroOsnhYf3kyEgRGXWqUkAu2hheYxaBncWFtBk71QwJb68mVothdUS5KhbHSiJDuHMf4ntBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازار رویا فروشی داغ شد
🔹
بدترین اتفاقی که در تورم برای پول شما اتفاق می‌افته، فقط کاهش قدرت خرید نیست؛ تورم گاهی کاری می‌کنه که از ترس فقیر شدن تصمیمی بگیرید که واقعاً فقیرتون کنه.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/694372" target="_blank">📅 22:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVem9s-U-JN2_20i6aQv45TDJL2bgDuG_y4QJ_ZLXm2dEqFaVE_h6o3sO2eiwqroUBcCkVk70Rt0rbHQjF0FY56vCusUCWFTKKGycPcKeOB3sq4YgiHKlfLWzV0K_1Mlf7NF8_yVC4DLTDDFBdFhiC_qemVKPvqcD2jmb4HBaFN3sNmcJleHi5ivwduqIXASLLPouckCs-6VsAZVj2L4cXVDZvgmNl6R-7l5oD5cjtZVRa0F0AskAvOM3pfodYKMt-DMmgOqlzkPwITaHfaCWwgfrbb63YgEPNMDD2qAh_pe4xmoQuI5eT9Ei3MAWK_XcWg1YjkWk_Z6ErVvQpv-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار خط گاز نیروگاه تشرین در حومه دمشق
🔹
منابع خبری از وقوع انفجار در خط لوله انتقال گاز به نیروگاه حرارتی «تشرین» در منطقه «حران العوامید» واقع در نزدیکی فرودگاه بین‌المللی دمشق خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/694371" target="_blank">📅 22:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28df4dcbc.mp4?token=b3gulB_0giM4Xs0FE2cyC0MEF1O8guOeYwOploUcb-Px_yiPtPrHIbNblpmN-3CMj6ilFddDMhWaKetSaoheX-2Jkp2-eMuES_DIEPKrOqBC1QikebQ1r8Pbcf1hMduncf9Bn_Sak6oeSf3w3ofVi8ukA-1LuYObc2RIVlLlmdlQq25H__Cn28rml7FlotujwGD552mysWg-BdCh72UGIZnHX0Y1rXd2eD4Ri_y2J6iKGirCRFhWXY0EgL2-NWgfhPlhUN0Pu-zS2j6Hhw-TMXddz6B5A7TdWgo6na66oNQE4F1sJ6OzxoXchjlitHsNBqIuWwDQYpMpryIUSrW0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28df4dcbc.mp4?token=b3gulB_0giM4Xs0FE2cyC0MEF1O8guOeYwOploUcb-Px_yiPtPrHIbNblpmN-3CMj6ilFddDMhWaKetSaoheX-2Jkp2-eMuES_DIEPKrOqBC1QikebQ1r8Pbcf1hMduncf9Bn_Sak6oeSf3w3ofVi8ukA-1LuYObc2RIVlLlmdlQq25H__Cn28rml7FlotujwGD552mysWg-BdCh72UGIZnHX0Y1rXd2eD4Ri_y2J6iKGirCRFhWXY0EgL2-NWgfhPlhUN0Pu-zS2j6Hhw-TMXddz6B5A7TdWgo6na66oNQE4F1sJ6OzxoXchjlitHsNBqIuWwDQYpMpryIUSrW0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان گستاخانه دبیرکل ناتو: جنگ با ایران برای ما «نفع» دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694370" target="_blank">📅 22:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ تلویحا از برنامه‌ریزی برای آشوب در ایران گفت  ترامپ:
🔹
خیلی زود خواهید دید که [در ایران] اتفاقاتی خواهد افتاد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/694368" target="_blank">📅 22:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد
🔹
در بحران بعدی ناچار از قطع برق می‌شویم، چون استارلینک به عنوان ابزار جدید حاکمیت‌گریز، اساسا دیگر مبتنی بر شبکه ما نیست
🔹
استارلینک حتی رجیستری و احراز هویت کاربران…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/694367" target="_blank">📅 22:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f37b5a00.mp4?token=Lo3uFgEE4BwT1eFtSVl44uhAYe39ol6xJKRMjrUdzBx-f9dHJNajmYfSL8nY9G7q-ySJS-3nRtTOFXQzUPPccOdTXaxA0Lwyd1M9JFqdPFwu7V59SK3j6L6htjzzihPyIjZr-2JFhL-G1fr0X8oKoJWQKLXLkvYT_4GgmMBwFO5Jvlb5SzTrRoW9S_d132QGlBE9HLVroN3TI2I3atQrx1XjmyPDeLv6cTaJkVkkG6Ye_21wTGeBycqRRrh3vI-YSa5J1A-jfg9-xZwitwnB1qiM_wWlFO4WmCTPgu7ywNHG1l4rmNNPcan2KBSp-e7Wf_twCerBitqiBH1H3VfIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f37b5a00.mp4?token=Lo3uFgEE4BwT1eFtSVl44uhAYe39ol6xJKRMjrUdzBx-f9dHJNajmYfSL8nY9G7q-ySJS-3nRtTOFXQzUPPccOdTXaxA0Lwyd1M9JFqdPFwu7V59SK3j6L6htjzzihPyIjZr-2JFhL-G1fr0X8oKoJWQKLXLkvYT_4GgmMBwFO5Jvlb5SzTrRoW9S_d132QGlBE9HLVroN3TI2I3atQrx1XjmyPDeLv6cTaJkVkkG6Ye_21wTGeBycqRRrh3vI-YSa5J1A-jfg9-xZwitwnB1qiM_wWlFO4WmCTPgu7ywNHG1l4rmNNPcan2KBSp-e7Wf_twCerBitqiBH1H3VfIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خط گاز نیروگاه تشرین در حومه دمشق
🔹
منابع خبری از وقوع انفجار در خط لوله انتقال گاز به نیروگاه حرارتی «تشرین» در منطقه «حران العوامید» واقع در نزدیکی فرودگاه بین‌المللی دمشق خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/694366" target="_blank">📅 22:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARHILEC5Whz6M8y9nVbfHwphyUDJVHdu1ITizp0ZI1wrXbsw5AmobH4Q485Hh2ykm3yNA4RqBcc6olDyhF-kTLQ5MWd5jQEi517_lw5CahX1T6V7n-jThcyZF9wm_582rs5uev4uVifPopEJDNz0U8wyEwSwvYnhaBOjxhDgsW9j8f7crpBXX5B0iBb5TGWVKXTTNz14isEOJsCJGgiNY3A801rTj8SdpbCZ02ikb9VRjDf2Q6OmdM_sbjpv2BxgCfQH4vkiHr_O__Sk9aYwG0Ts1UN2rBZjziqDLtk8gvKF3iC6LvljmnfK1cL7_tGbDHv1ieJautYfq0-6hTj3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
فشارسنج سخنگو فارسی؛ اندازه‌گیری فشار، راحت و دقیق!
🔥
این فشارسنج رو می‌خوای؟ قسطی هم می‌تونی بخری!
❤️
مناسب سالمندان و افرادی که نیاز به کنترل منظم فشار خون دارن
🔊
اعلام نتیجه به زبان فارسی
📊
اندازه‌گیری فشار خون و ضربان قلب
🏠
مناسب استفاده در منزل
✅
امکان پرداخت 4 قسط 560 تومنی
🔥
قیمت ویژه: فقط
1,990,000 تومان
برای اطلاع از جزئیات و خرید
👇
برای کسب اطلاعات و نحوه پرداخت بزن رو لینک
👇
https://memarket24.ir/product/fast/63656/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694365" target="_blank">📅 22:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_DVXkQfNIGkla3FaNWqxVhh55MIhLuCDwEiDys5kG7hKlk4KvI9jwoLWl6ePUWB-1CxDjULaaC-2Ht4GxlaFr6QkzpwwQKWlTkxWmetq5uwdVcWp2DP-o5c-fweElD8k1UVOQ4wWSLGUGvX6GBmzdbOxSqEapPA6kos7oMEq7WTPzhbaHUW48LvYnPTB-DEdb-B4rDLxr372p5zcMAw9bjh5_RaKZOO7je0ntfeelUTMofP8pO4--LNjXODV8ZBPlIF6cGODjrepmflFxEp5YO_L9BRjjQK5pECfXsPParwe3oES4TfWcxdKT7g_piIDhjQYmUOhZfZHL4akq4hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت مهم یک فعال اقتصادی با رویکرد اشتغال و ارزش افزوده بازار: وقت آن رسیده ادبیات جدیدی به صنعت پتروشیمی وارد شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694364" target="_blank">📅 22:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
به صدا در آمدن آژیرهای خطر در پایگاه آمریکایی الازرق اردن در پی رصد تهدید موشکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694363" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153bb6e443.mp4?token=p-bdngjvEYFQmPNUZcoLaX0ogUtXCSvEQjMebb46xmqPdW3t3hBr6dWH6riatCDeNaFzKeqy_UlDN9Jakc2gbFGWORBcX9DMsg1yb8aQGmHwXSbKv6X-tKShERwtwkB1OvT782a1bl7iJc6YpYpLmcVM4aaP-ZKjDjOYQ6RqPgBRD_-cvWlsVO7t5_m3jaEmS8R-Rs4PlhQU5d700VoPmGgatp8QTT00zd0It5D2b_yX4W1xfbfD2uOXXqwmYiTDtu96bYX9guFdA6JH3v33UKH38b0de4aWFRI2Ek2EqaBo827YJshn7-6DoSe6skXStTg16IWaPVV5I6gQRq41tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153bb6e443.mp4?token=p-bdngjvEYFQmPNUZcoLaX0ogUtXCSvEQjMebb46xmqPdW3t3hBr6dWH6riatCDeNaFzKeqy_UlDN9Jakc2gbFGWORBcX9DMsg1yb8aQGmHwXSbKv6X-tKShERwtwkB1OvT782a1bl7iJc6YpYpLmcVM4aaP-ZKjDjOYQ6RqPgBRD_-cvWlsVO7t5_m3jaEmS8R-Rs4PlhQU5d700VoPmGgatp8QTT00zd0It5D2b_yX4W1xfbfD2uOXXqwmYiTDtu96bYX9guFdA6JH3v33UKH38b0de4aWFRI2Ek2EqaBo827YJshn7-6DoSe6skXStTg16IWaPVV5I6gQRq41tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر بعد از غذا آب سرد بنوشید، چه اتفاقی برای بدن می‌افتد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/694362" target="_blank">📅 21:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ترامپ جانی به قتل‌عام شهروندان عادی ایران افتخار کرد!/  ایران ۴۵۰۰ نفر را در جنگ از دست داد و ما به زودی پیروز خواهیم شد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/694361" target="_blank">📅 21:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694360">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2375a1c05f.mp4?token=tEgUH0O8tUsRoPSiGxGKJHbhFH5WO67R27tql7wUkdgRP1gpr9H4UW_IEApkEWWfAGD75MAQLYQk_L4yOM7Pq-EIpeKGfM8z_tceo87MDEpsxnmCcySDRDHOV_0Ygnus6RIl7zeftRyuINnTtzQjLfE1X1-bqabZiPNJOnEDEDdTZjjXubmj-hb522J8fxAM40imsMpxr75V6twc-fo_TklhumPFsuUhbWihrlJqnuqN4tpNcxDNSe6DyoZQ40OLCuPesw9YcZOjpYStXbhbgEtQFTA4G0ISjlgUUI69YBlbumIr-V6D_K7C4hrZXzI8UrrWv2LZPehlD1xwg9nrjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2375a1c05f.mp4?token=tEgUH0O8tUsRoPSiGxGKJHbhFH5WO67R27tql7wUkdgRP1gpr9H4UW_IEApkEWWfAGD75MAQLYQk_L4yOM7Pq-EIpeKGfM8z_tceo87MDEpsxnmCcySDRDHOV_0Ygnus6RIl7zeftRyuINnTtzQjLfE1X1-bqabZiPNJOnEDEDdTZjjXubmj-hb522J8fxAM40imsMpxr75V6twc-fo_TklhumPFsuUhbWihrlJqnuqN4tpNcxDNSe6DyoZQ40OLCuPesw9YcZOjpYStXbhbgEtQFTA4G0ISjlgUUI69YBlbumIr-V6D_K7C4hrZXzI8UrrWv2LZPehlD1xwg9nrjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودشیفتگی بی‌پایان ترامپ: در آینده هیچکس مثل من عمل نخواهد کرد/ بهترین سیستم هوایی دنیا را درست خواهم کرد
🔹
نیروی هوایی ایران را نابود کردیم/ کنترل کامل تنگه هرمز را در دست داریم! #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/694360" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694359">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
هشدار فارن افرز به آمریکا در مورد آمادگی ایران برای حمله پیش‌دستانه
فارن افرز نوشت:
🔹
ایران بیش از گذشته آمادگی خود را برای انجام حملات پیش‌دستانه نشان داده است؛ برای نمونه، در ماه ژوئیه، ایران به پایگاهی در اردن که میزبان نیروهای نظامی آمریکا بود، حمله موشکی انجام داد؛ در حالی که بلافاصله پیش از آن، هیچ حمله‌ای از سوی آمریکا صورت نگرفته بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/694359" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مشاور پیشین امنیت ملی آمریکا: ایران تسلیم نخواهد شد و آمریکا باید هرچه زودتر، حتی با پذیرش توافق بد، به جنگ پایان دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/694358" target="_blank">📅 21:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اخبار منتشر شده در فضای مجازی درباره وقوع حادثه امنیتی در شهرستان‌های سیب و سوران و مهرستان صحت ندارد./ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/694357" target="_blank">📅 21:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9e6f197c.mp4?token=vo6ntQ_lY_ICaJ78W34tMET3KYOHdAB8YiOr97UkuUybrWuKtiZ00HdoTOxnTXnnMxQlqoj39WhgVXhKSqSFdq5lKjCj1VzZRRnffPlyO4Az3fm-CqGnQMjc3tJbP-LMA5xaT4-tlxLfNGZkQI4bMmWObn2yiVI053yG_0aJhW72bMIeS2kmrCllUvF-zbx8qqfOkQSNxVL0tHXH2cIUtU5qrFETEc6J2Z2ZqQmk9Wc2Am2gSB3MNIAofJ5Fgrw23A7N4WvHaAGkk_DF90ZtK919KDUCcS06OWn-6UCrgJuOAb-jZtXQulWdxhZR4O5YuSWLjXGVDoNzQAmYvWNw0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9e6f197c.mp4?token=vo6ntQ_lY_ICaJ78W34tMET3KYOHdAB8YiOr97UkuUybrWuKtiZ00HdoTOxnTXnnMxQlqoj39WhgVXhKSqSFdq5lKjCj1VzZRRnffPlyO4Az3fm-CqGnQMjc3tJbP-LMA5xaT4-tlxLfNGZkQI4bMmWObn2yiVI053yG_0aJhW72bMIeS2kmrCllUvF-zbx8qqfOkQSNxVL0tHXH2cIUtU5qrFETEc6J2Z2ZqQmk9Wc2Am2gSB3MNIAofJ5Fgrw23A7N4WvHaAGkk_DF90ZtK919KDUCcS06OWn-6UCrgJuOAb-jZtXQulWdxhZR4O5YuSWLjXGVDoNzQAmYvWNw0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت مضحک جدید ترامپ: آمریکا ۱۸ نفر را در جنگ با ایران از دست داد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/694356" target="_blank">📅 21:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
خبرنگار ارشد امنیتی روسیه: به گفته منابع اطلاعاتی, یک حمله غافلگیرانه به ایران در شرف وقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/694355" target="_blank">📅 21:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اظهارات ترامپ جانی: آمریکا در طول ۲۳ سال حضور در عراق ۴۱۰۰ کشته در عراق داد/ ۲۳ هزار نفر هم آسیب‌های بسیار بدی دیدند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694354" target="_blank">📅 21:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه ساخت هر متر مسکن ملی، ۴ برابر شد
عبدالجلال ایری، سخنگوی کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
تعداد متقاضیان مسکن حمایتی از حدود ۷.۵ میلیون نفر به بیش از ۱۰ میلیون نفر رسیده و از این تعداد، تنها ۸۵۰ هزار نفر تشکیل پرونده داده‌اند.
🔹
از سال ۱۴۰۰ باید سالانه یک میلیون واحد مسکونی احداث می‌شد، اما این هدف تاکنون محقق نشده است.
🔹
هزینه ساخت هر مترمربع واحدهای نهضت ملی مسکن از حدود ۴.۵ میلیون تومان به ۱۵ تا ۲۰ میلیون تومان رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/694353" target="_blank">📅 21:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رییس سازمان برنامه و ‌بودجه: برای اقشار کم درآمد یک کالابرگ ویژه در نظر گرفتیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694352" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0416abbe41.mp4?token=MM0Sz7nmvirT8p22v2REHzvyjC8_Lw4ltxDNOozz4UyQ6noXEkeWVXmZB73E40aFBUJkZoT8rqtC_yw1HAEvaSh0a527VcxD1CdEJZyFCSTraC8nzEXnW8yjztRNDwePmqPLWksFfTzAXAxvKvEZv-PsZgglqQ5OcjQMpFK0oe_v--ClP5u6BmxAlEXVuoYm3ADrw1v7L3CeeklPFiVOaqn1l5xwLOgPJu0LnXkwJjz9ap8ker4pjPgdbxD9sCVc5iJlPinnpt7ksyknJQkvEQm4H7iYlsB1Y_QA-Ri7LeyVRxH12r1n50RM5U7CiTyiHUdicXLkJNBKasMOFJLOhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0416abbe41.mp4?token=MM0Sz7nmvirT8p22v2REHzvyjC8_Lw4ltxDNOozz4UyQ6noXEkeWVXmZB73E40aFBUJkZoT8rqtC_yw1HAEvaSh0a527VcxD1CdEJZyFCSTraC8nzEXnW8yjztRNDwePmqPLWksFfTzAXAxvKvEZv-PsZgglqQ5OcjQMpFK0oe_v--ClP5u6BmxAlEXVuoYm3ADrw1v7L3CeeklPFiVOaqn1l5xwLOgPJu0LnXkwJjz9ap8ker4pjPgdbxD9sCVc5iJlPinnpt7ksyknJQkvEQm4H7iYlsB1Y_QA-Ri7LeyVRxH12r1n50RM5U7CiTyiHUdicXLkJNBKasMOFJLOhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه یاوه‌گویی‌های ترامپ: به زودی متوجه خواهید شد که اتفاقاتی در مورد ایران رخ خواهد داد  ترامپ:
🔹
نفتی که ما طی سه روز گذشته از تنگه هرمز خارج کرده‌ایم، بیشتر از هر مقدار نفتی در تاریخ است. تقریباً کنترل کامل تنگه هرمز را در دست داریم. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/694351" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
اظهارات مضحک ترامپ: در دوره اول ریاست جمهوری‌ام داعش را حذف کردم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694350" target="_blank">📅 21:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1469edb195.mp4?token=m8JpD-abQDk-JHpV_mmDHE7gRVHsI12o69U0Sii2eq8RXkAynJsQjMGIihDoCYDgU2Z6CbA45Z4lzE8c8hXj_vMZBqzGK6q0CXX_2peDg0roagyQi7nN9MQyAYtIGX88F49kJ4xlBMVUHoJnl0FtOmDqC402B3mHOLQI0MJnSkOJBQKoq_ODJVZzW-0PfQ1ML5bQTKUrkXEFys-EcFgvFp1z38fkDUEXEmJFydriJhJ5lntQBK2SiZL5ikOkmyfdqN1dkziFU09izbNUSjWRxGPqmOs-g2Vc_6npacObdyFyGmf9zGiQH5ODj5RkA0D5nL-wccKTMq-0Y1voDDQJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1469edb195.mp4?token=m8JpD-abQDk-JHpV_mmDHE7gRVHsI12o69U0Sii2eq8RXkAynJsQjMGIihDoCYDgU2Z6CbA45Z4lzE8c8hXj_vMZBqzGK6q0CXX_2peDg0roagyQi7nN9MQyAYtIGX88F49kJ4xlBMVUHoJnl0FtOmDqC402B3mHOLQI0MJnSkOJBQKoq_ODJVZzW-0PfQ1ML5bQTKUrkXEFys-EcFgvFp1z38fkDUEXEmJFydriJhJ5lntQBK2SiZL5ikOkmyfdqN1dkziFU09izbNUSjWRxGPqmOs-g2Vc_6npacObdyFyGmf9zGiQH5ODj5RkA0D5nL-wccKTMq-0Y1voDDQJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج خفت‌بار ارتش جنایتکار آمریکا بعد از ۲۳ سال از عراق / ترامپ: آخرین نیروهای آمریکایی عراق را ترک می‌کنند؛ مأموریت ما در این کشور پایان یافت  ترامپ:
🔹
ما عراق را با یک نخست وزیر عالی ترک می‌کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/694349" target="_blank">📅 21:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=T_6KQCjTCNCFLa48QfoUAb4-60VI9sfab3u3i4Oo-H0laUfAGh6VPK6OCZj6XtscichC6FEhmlBJNSMJ472U0RmLdVgcCGj_i1MQ2qMfZqu7QXrZH857bgC3_maqGNWESJkXMo70I8G_3dbDJDk9nw_W9tMdFVIAcPPpP9NfMSO-ngMyL4gc7nX8YUPoPDOJj8r7_VsiWMRA1bMliRfJs-fNWFug5Pr4LyBaO8yGiMsEbJP9qdhlObKpcIioNc6usGMNH787QFrEM6-O9_JjPbBa0sbPiCcDHCq752a6vdCeVmNLCP7TBZeBGltEVzMVE0p2zj2mGclrwd-ypHWJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=T_6KQCjTCNCFLa48QfoUAb4-60VI9sfab3u3i4Oo-H0laUfAGh6VPK6OCZj6XtscichC6FEhmlBJNSMJ472U0RmLdVgcCGj_i1MQ2qMfZqu7QXrZH857bgC3_maqGNWESJkXMo70I8G_3dbDJDk9nw_W9tMdFVIAcPPpP9NfMSO-ngMyL4gc7nX8YUPoPDOJj8r7_VsiWMRA1bMliRfJs-fNWFug5Pr4LyBaO8yGiMsEbJP9qdhlObKpcIioNc6usGMNH787QFrEM6-O9_JjPbBa0sbPiCcDHCq752a6vdCeVmNLCP7TBZeBGltEVzMVE0p2zj2mGclrwd-ypHWJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی از هدف‌قرارگرفتن مقر گروهک‌های تجزیه‌طلب در کویسنجقِ اربیل خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/694348" target="_blank">📅 21:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خروج خفت‌بار ارتش جنایتکار آمریکا بعد از ۲۳ سال از عراق / ترامپ: آخرین نیروهای آمریکایی عراق را ترک می‌کنند؛ مأموریت ما در این کشور پایان یافت  ترامپ:
🔹
ما عراق را با یک نخست وزیر عالی ترک می‌کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/694347" target="_blank">📅 21:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa94f7617.mp4?token=Gq35H38Q2mTGQvouFHwFS4rdPNKHNbwAVXjrcmByKN10eY9AvHtcZ5cvDkdJnEbTWwrn-fu7QVa_eL8FAWoqfhGvCEQ3vxOd3UrG5rQ3nT4TKLIOPIDDI1fwDpFrGIEwoRo_zXZ70dWKOD22LvF1DrxLOnmnXPtB4itrY-98opEVRT-lth_JBY0U7ZkXajZ7Q-QWu9qQJ0udNYKv7iL_ZSUybT9rYLMpD_KTwPRvHbB5lpJz6qNnkXlKAb6UA3TFzIimvB5DOjVamGvH1hzv4O2oNJrB_mXjyLd0_SZbz36PBs8BKrvB8NA6QRplD1lg5zbgaRJzIOwHTHhbNt5DNCKG_dqAIwxnRrZe7VfBUjLEtTiuAys9bnbU6o1j9JAJHJTNLsj7b7n7RyTpJ6IPUpAnR6R206IA-xlJHTGCOSx1RgnmXvzRkyyOVbvCbeY92Y8nLEV33NR9XzccSw8YN99usJQf79O_E5lgVoN7ztG5ynWEG5VLCGrBumXki2JApf3LOHU12Fvqbd7iBWBlhF4BOUEnXd4eYuPcQIFgM5WUQ2mDZD1joDiQ5pCnbMr1iCiQhQ6WOZexzrIq4zb_TjpvpUc0tYSUorIrhIXoTpV0Fo5Y8b5kvtJsT_2qn_UV7V9G84mei0olrCuSHO051QBp0KLyF_YuJm4SohL-0cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa94f7617.mp4?token=Gq35H38Q2mTGQvouFHwFS4rdPNKHNbwAVXjrcmByKN10eY9AvHtcZ5cvDkdJnEbTWwrn-fu7QVa_eL8FAWoqfhGvCEQ3vxOd3UrG5rQ3nT4TKLIOPIDDI1fwDpFrGIEwoRo_zXZ70dWKOD22LvF1DrxLOnmnXPtB4itrY-98opEVRT-lth_JBY0U7ZkXajZ7Q-QWu9qQJ0udNYKv7iL_ZSUybT9rYLMpD_KTwPRvHbB5lpJz6qNnkXlKAb6UA3TFzIimvB5DOjVamGvH1hzv4O2oNJrB_mXjyLd0_SZbz36PBs8BKrvB8NA6QRplD1lg5zbgaRJzIOwHTHhbNt5DNCKG_dqAIwxnRrZe7VfBUjLEtTiuAys9bnbU6o1j9JAJHJTNLsj7b7n7RyTpJ6IPUpAnR6R206IA-xlJHTGCOSx1RgnmXvzRkyyOVbvCbeY92Y8nLEV33NR9XzccSw8YN99usJQf79O_E5lgVoN7ztG5ynWEG5VLCGrBumXki2JApf3LOHU12Fvqbd7iBWBlhF4BOUEnXd4eYuPcQIFgM5WUQ2mDZD1joDiQ5pCnbMr1iCiQhQ6WOZexzrIq4zb_TjpvpUc0tYSUorIrhIXoTpV0Fo5Y8b5kvtJsT_2qn_UV7V9G84mei0olrCuSHO051QBp0KLyF_YuJm4SohL-0cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناریوی عراق برای ایران کلید خورد؟
🔹
این روزها این سوال خیلی زیاد مطرح میشه که آیا آمریکا همون بلایی رو داره سر ایران میاره که سر عراق هم اورد؟ اگر اتفاقاتی که برای عراق افتاد رو کنار اتفاقات امروز ایران قرار بدیم، شباهت‌های عجیبی می‌بینیم، اما یک تفاوت خیلی بزرگ این وسط دیده میشه...
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694346" target="_blank">📅 21:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyHvCoUxnsDFTkmtr3WCeWfssXCMcVnqKyylWEegtIn8xndgK4do8xLmw_uPvgbXQG1-yt9eOyn6lRMHAVqddVa1CY9MBE1hNPHuQ72I3Zv9Khq4O72sqH6BLNwNzU40qNVUGh9kzeJIUN8JYBmtmF_h7HcTciUEdv68k9F4m6YvTJ327jcLPtYhYIpqTQQCNtytoq-E0_EkHIA-Ujj0RVqcffixNXPIkOJHpemoWra_l4kpm8RQRGSqr_HsBKc5UeCry9XCegg3OW6BaTKNhZrLO0uEI1Q1sSFB-NDnwG__MH-yDKLlwV9IahXPxBWWPVT4dYj1VvejyyR-jnOwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار: من حق انتخاب داشتم که در عراق بمانم یا آنجا را ترک کنم و تصمیم گرفتم که وقت آن رسیده که آمریکایی‌ها به خانه برگردند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/694345" target="_blank">📅 21:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uufIrPS2Hb3MHDoVxx12Af3At-nB3cTfY_RgciskRELFGybaj1aCy6oZZtKe6xLy3379C7hVegCUCbfaOcciFvH7526f-pBxWjwspx2lEe-bY2-Vcscp7uSJLbqEyz4sdS8R9IB6KgXOgwwtp7fYyJkMOzTP8kSFger5G1FxJ3CjXOUhIqD06lyNd_IvGmgsJg6TWu34L2oOPBcFMvLMoMmm2fEBuuY4KWZcCHBtZbVFHG-fy7jFsUlCk7-4_AhIwLBs4XV3DdoRfzUVEAro7IGrgJT9CBh9ATfJrHkSnpE-T4OsU_ZN1wBJEoj47s8RpEJnhEwKP1B8T-NgDFBBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پشت پرده مصاحبه رتبه‌های برتر کنکور
تبلیغ یا تجربه واقعی؟
اگر یک رتبه برتر بابت معرفی مؤسسه‌ای پول گرفته باشد،
آیا خانواده‌ها نباید این موضوع را بدانند؟
💎
گزارش‌هایی درباره ادعای پرداخت تا ۲۰ میلیارد تومان برای خرید مصاحبه با رتبه‌های برتر منتشر شده است.
گزارش‌های زومیت، خبرفوری و شرق را ببینید.
https://B2n.ir/ur5426</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694344" target="_blank">📅 21:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دیوید پین، افسر سابق ستاد فرماندهی ارتش آمریکا: ایران یک شکست سنگین دیگر به آمریکا تحمیل و آمریکا را وادار کرده پس از ۲۳ سال، نیروهایش را از عراق خارج کند
🔹
ترامپ همچنین ظاهرا در حال برنامه‌ریزی برای خروج تمام نیروهای آمریکایی از سوریه، کویت و بحرین است…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/694343" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa908d5cad.mp4?token=XGXkzrIOOzTRJpMLqGyJuBMAVKY9Sn6TCH9Pd1uPhvNiwaTonx_fTIV5tQamlzcQ5vykN33vSlMOgk1pjBScfUSzoAg4wIhenGLzWcn2gQtnirAjWPQBlLZ2q_zD6bakQfegKAchLCJcWCmGcNlmzgSINjIRAFOu9agO6f1KBReZz8m232Z26T2fArdt6-xWseAyOU7V6NOSExVv17uUe1dtOXQG5-sEzlySLptInk_qflOjp2S2ATxEIFAdw0T3iMpXEmjt5TC3bYUHS7-BGWQfMBt06EwoojzPrhUH-gRgPwePQ35sqxZb_HDFnSOjsPW2lOSna2vIEU8PaKZaLwQPy_Qcpp4G5Q2JBtFD45tU5ngkF34UU6Va4QHDzU0BZ3jOJbTwHSwO1B4Uls12g9pAvFNQ-bOX5bzTnF9daJyGe6QQ1uR6kSH8cthwkQOcgh31lcjcdSXUKzHKmygrHQ3pwLkbFHbs0FeyVoUZmjNsM5pPFEMjvKLaL5nuN9aYw9R6Ob8ECITqzYKD6YiGI_iGygF7VpwoUwNe_pRRSZhBsYOqffiwgPVvCqMXIqTNzAnmjCdNNheSMa-bax3NJs9EWGCUcrf0ZtvD5MMMUrnxUuFeNOjmMiP6t7LITglEBmtIPrN4qsBhI8afCF4c1REZkn-lLnESVOKavN2mKAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa908d5cad.mp4?token=XGXkzrIOOzTRJpMLqGyJuBMAVKY9Sn6TCH9Pd1uPhvNiwaTonx_fTIV5tQamlzcQ5vykN33vSlMOgk1pjBScfUSzoAg4wIhenGLzWcn2gQtnirAjWPQBlLZ2q_zD6bakQfegKAchLCJcWCmGcNlmzgSINjIRAFOu9agO6f1KBReZz8m232Z26T2fArdt6-xWseAyOU7V6NOSExVv17uUe1dtOXQG5-sEzlySLptInk_qflOjp2S2ATxEIFAdw0T3iMpXEmjt5TC3bYUHS7-BGWQfMBt06EwoojzPrhUH-gRgPwePQ35sqxZb_HDFnSOjsPW2lOSna2vIEU8PaKZaLwQPy_Qcpp4G5Q2JBtFD45tU5ngkF34UU6Va4QHDzU0BZ3jOJbTwHSwO1B4Uls12g9pAvFNQ-bOX5bzTnF9daJyGe6QQ1uR6kSH8cthwkQOcgh31lcjcdSXUKzHKmygrHQ3pwLkbFHbs0FeyVoUZmjNsM5pPFEMjvKLaL5nuN9aYw9R6Ob8ECITqzYKD6YiGI_iGygF7VpwoUwNe_pRRSZhBsYOqffiwgPVvCqMXIqTNzAnmjCdNNheSMa-bax3NJs9EWGCUcrf0ZtvD5MMMUrnxUuFeNOjmMiP6t7LITglEBmtIPrN4qsBhI8afCF4c1REZkn-lLnESVOKavN2mKAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جانفدا؛ جایی که آموزش رزمی و نظامی از ادعا عبور می‌کند و به مهارت می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/694342" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434276c19e.mp4?token=ZW9ZfJP4RPZgP53J1-OfxRaVVJzwbhTFElk7eNbFKZkNAInNxfk2UA3_iUVeq6kbpZaOuMEjmmLJb4lYG06smhHin0KVuf8gpkBosqPPx4-KXFgCryCNdJ-mgCZWVxwFt0AFE88OwvlsvqoC9IEi9ZmlkX8mE5FFdrGWPjgdGYrnKHu6fEUjOxwIwhpnCwZrX8nibse4rWqxcwk9fE7de4hMfxQBLqclETWDmGTwp9mkbdr9vKnVMZHXMGjv9JFvayGjGk8qd3ZJPC3w1dS_52GKJN2W9JxZqFm-GfciZDpl1YXnbWzuv3fUwao1EC9Par9sM7GFx-28zjjDYnBfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434276c19e.mp4?token=ZW9ZfJP4RPZgP53J1-OfxRaVVJzwbhTFElk7eNbFKZkNAInNxfk2UA3_iUVeq6kbpZaOuMEjmmLJb4lYG06smhHin0KVuf8gpkBosqPPx4-KXFgCryCNdJ-mgCZWVxwFt0AFE88OwvlsvqoC9IEi9ZmlkX8mE5FFdrGWPjgdGYrnKHu6fEUjOxwIwhpnCwZrX8nibse4rWqxcwk9fE7de4hMfxQBLqclETWDmGTwp9mkbdr9vKnVMZHXMGjv9JFvayGjGk8qd3ZJPC3w1dS_52GKJN2W9JxZqFm-GfciZDpl1YXnbWzuv3fUwao1EC9Par9sM7GFx-28zjjDYnBfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک لحظه غفلت در تقاطع، می‌تواند به چنین تصادف عجیبی منجر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/694341" target="_blank">📅 20:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fde2c606d.mp4?token=LlhMgIUFu4u-5wTbLOE1wF-Ufj5Tmc9kSCg0Y3uPUga-tjEzrUELXR4amSAa0eELQEVUDZt5QIP7v08nVzCuvE7Ztb2roVt9CRdaRfEreIDWriOWue3ZYeN4du7xh0mRnWIM1GSTD-zRujhrB_RExjzABtqFpPfsGVi31cPkSFaP3GlJSou0R4WyMoTPsTaLsAnxanETNLRfM0iwAwjrFVPSwBa5vlK7KUQW5mj3o5GE-8x8Cf2CntDcrr4AI1r2yBWhTnePxNNDfl2TmyMqZlURi7Sv_sQvTXAvEyIRnZWQTC6CtnL6vyDJ5-aEG84WhOdTyuK3PtyuQG_N3mzUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fde2c606d.mp4?token=LlhMgIUFu4u-5wTbLOE1wF-Ufj5Tmc9kSCg0Y3uPUga-tjEzrUELXR4amSAa0eELQEVUDZt5QIP7v08nVzCuvE7Ztb2roVt9CRdaRfEreIDWriOWue3ZYeN4du7xh0mRnWIM1GSTD-zRujhrB_RExjzABtqFpPfsGVi31cPkSFaP3GlJSou0R4WyMoTPsTaLsAnxanETNLRfM0iwAwjrFVPSwBa5vlK7KUQW5mj3o5GE-8x8Cf2CntDcrr4AI1r2yBWhTnePxNNDfl2TmyMqZlURi7Sv_sQvTXAvEyIRnZWQTC6CtnL6vyDJ5-aEG84WhOdTyuK3PtyuQG_N3mzUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغزتان نسبت به حرف‌هایی که مدام به خودتان می‌زنید، شکل می‌گیرد
🧠
🔹
هر بار می‌گویی «نمی‌توانم»، «سخت است» یا «ضعیفم»، در واقع داری این باورها را در ذهنت تقویت می‌کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/694340" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMvhSCvsxkkHCe75NLGyyU9MVzIf9lAgy6cIuegaUUbwYs7YLlQUFzkeCsf57A0shdpkD0fPCjwoTJqBz58VfaqDdKu1FDlXFEaTYWo-k30zu-48cGw1MsC2X8seXjvnZSZzP20WFqntMfy1MiRWhN5rSPmlATP-Ju-8t5FKdc4hCF3Ima6WHkqz39GWGc5EVUN1fd-gWiqNw0Jg5F9UqUQlOhR-Q5mxzc_cC2GpWcQ23kqMAmDoN8c19ZYxCYVfaJ9qF4NLdY9YYms_ll_2p9yFJcMjli0ZVoPxadGN8pjAOFbP-qfKuJuNF9YrVeAfSAPIRBm6doDtVIPjMeT9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت تایمز اسرائیل از طرح جدید دیوارنگاره میدان انقلاب تهران
🔹
تایمز اسرائیل با انتشار طرح اخیر دیوارنگاره میدان انقلاب، آن را اثری توصیف کرده است که در آن یک قهرمان اسطوره‌ای ایرانی در حال هدف قرار دادن ناوهای هواپیمابر آمریکا به تصویر کشیده شده است.
🔹
این رسانه همچنین به پیام‌های درج‌شده بر دیوارنگاره اشاره کرده و شعار «لشکر شیطان در خلیج فارس غرق خواهد شد» را بیان کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/694338" target="_blank">📅 20:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02175437b7.mp4?token=qpwO1LdOdX6uMDt5C4tX74fqwNsl9vkBNzUnpKSzFTBpkBnaq_pBK_nl12yzF0WTUrTnVonQFtempm11dxBdJjBNAMsk-S5Fla_Sgi15iTkluhFIRj0dfhC2ULw-DDzCBbgtBOwnfmLf0INobaLii6-b-GfIx2zYmo0BIHfI9PZUeXdj2dQs0cHrrNmTolpQZcwTXlViRVhI_v6vCQdfmaQJiLeH6TTXDOwr7JlvpxSOtJndW-E4JzpweazJRKGjLmi2TkRdk-faKBmfY1hxFSf5H-zE5CWUAcjZ-VTWAAj2pGftQJ_JK26Sr8_EcMjHSh9_S_zD0goRBeC20VjEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02175437b7.mp4?token=qpwO1LdOdX6uMDt5C4tX74fqwNsl9vkBNzUnpKSzFTBpkBnaq_pBK_nl12yzF0WTUrTnVonQFtempm11dxBdJjBNAMsk-S5Fla_Sgi15iTkluhFIRj0dfhC2ULw-DDzCBbgtBOwnfmLf0INobaLii6-b-GfIx2zYmo0BIHfI9PZUeXdj2dQs0cHrrNmTolpQZcwTXlViRVhI_v6vCQdfmaQJiLeH6TTXDOwr7JlvpxSOtJndW-E4JzpweazJRKGjLmi2TkRdk-faKBmfY1hxFSf5H-zE5CWUAcjZ-VTWAAj2pGftQJ_JK26Sr8_EcMjHSh9_S_zD0goRBeC20VjEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی در گمرک اسلام‌قلعه هرات
🔹
مقام‌های محلی ولایت هرات افغانستان اعلام کردند آتش‌سوزی رخ‌داده در گمرک اسلام‌قلعه مهار شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/694337" target="_blank">📅 20:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد جدید میانجی‌ها؛ موضوع جلسه هیئت دولت با عراقچی
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
پیشنهاد میانجی‌ها درباره اجرای همزمان تعهدات ایران و آمریکا، امروز در جلسه هیئت دولت با حضور آقای عراقچی مطرح شده و درحال‌حاضر در دست بررسی است.
🔹
بر اساس این پیشنهاد، ایران و آمریکا به‌صورت همزمان اقداماتی را که برای رسیدن به توافق درباره تنگه هرمز و رفع برخی محدودیت‌ها و موانع مطرح شده، اجرا می‌کنند تا مسئله اقدام اول از سوی یکی از طرفین برطرف شود.
🔹
این پیشنهاد از سوی میانجی‌ها به طرفین منتقل شده و پس از بررسی جزئیات، درباره نحوه اجرای آن تصمیم‌گیری خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694336" target="_blank">📅 20:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پیش‌بینی بانک سرمایه‌گذاری آمریکا از آینده بازار طلا
🔹
مورگان استنلی می‌گوید واردات طلای چین در مسیر ثبت بالاترین سطح از سال ۲۰۱۷ قرار دارد.
🔹
شورای جهانی طلا هم اعلام کرده واردات این کشور در ۸ ماه نخست سال از ۱۰۰۰ تن فراتر رفته است.
🔹
مورگان استنلی تقاضای فیزیکی، نگرانی از بدهی عمومی دولت‌ها و احتمال افت بازده اوراق را سه پشتوانه بلندمدت احتمال افزایش قیمت طلا می‌داند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/694335" target="_blank">📅 20:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آژانس امنیت هوانوردی اروپا: آسمان ۶ کشور عربی بحرین، کویت، قطر، امارات، عمان و عربستان سعودی تا ۱۶ نوامبر خطرناک است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/694333" target="_blank">📅 20:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18db35ecd.mp4?token=J4ZxGDlKyl5ZVaKPaEvqKEmo9GSmPwJcl_9foI8ZFGIVxl2OJevS1AOq8oMYhmqV0wopWoLGr5vWOvmUpaJB9NDAWWF5fS9FPHPVJ4M-M2SJWgTFf8kOmfwKaTNRJ31Ie7iyDX8gaDeCJ-sXYVquomnBj1pl-aqbw7oAOUuwwvssh8iZf94BmNig8MAKNrYxYDymAhALIlDA9BOiOdS15ipCWa9cFoCmJdkBj-lJuPiyUEhhhp7XPp2ED-BQQpja-LR75oS3PH6xmiPjOeVw_0Khu7KEEA8YgFxSpNCw5cSMJUVt-_cDNHUYNIhkQcgiyI5yDEW4irgR4E__n7TMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18db35ecd.mp4?token=J4ZxGDlKyl5ZVaKPaEvqKEmo9GSmPwJcl_9foI8ZFGIVxl2OJevS1AOq8oMYhmqV0wopWoLGr5vWOvmUpaJB9NDAWWF5fS9FPHPVJ4M-M2SJWgTFf8kOmfwKaTNRJ31Ie7iyDX8gaDeCJ-sXYVquomnBj1pl-aqbw7oAOUuwwvssh8iZf94BmNig8MAKNrYxYDymAhALIlDA9BOiOdS15ipCWa9cFoCmJdkBj-lJuPiyUEhhhp7XPp2ED-BQQpja-LR75oS3PH6xmiPjOeVw_0Khu7KEEA8YgFxSpNCw5cSMJUVt-_cDNHUYNIhkQcgiyI5yDEW4irgR4E__n7TMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله، ساختمان‌های با ارتفاع متفاوت را به شکل متفاوتی به لرزه درمی‌آورد
🏢
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/694332" target="_blank">📅 20:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNCxqJ8yzLo9uyA0dvclqxIwKlioKxkqtWX30rNt5Uxv0s758naXWHahO7bMwm89m8SkAB4nLtZUN9v45swOseu6Zs3ZzAIKiqWX4rkUl1H9PuIXAFJuzHQaIEdmFgqOCVww8BewvbH8kcFR7JRQlitEAzHHXDuUvEdC7MdQiCrjo8UmMy9qRa16Ucu9wvS8rWsQMiagaLyvDeFoWFLwY-1cElZhz9nxM22THpbH-z6qUYwTy1dzpsT4TwZHV4Q-gQULylx0-Bzx4oqj36fS0l0i-M5qH332wn4BT34bXlAEH_4R4uR7CgDdIELwsPZSP3HRuQ0qUMz_rqwQPerPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694331" target="_blank">📅 20:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
وزیر اقتصاد: افزایش اعتبار کالابرگ تا آخر هفته مشخص می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/694330" target="_blank">📅 20:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد
🔹
در بحران بعدی ناچار از قطع برق می‌شویم، چون استارلینک به عنوان ابزار جدید حاکمیت‌گریز، اساسا دیگر مبتنی بر شبکه ما نیست
🔹
استارلینک حتی رجیستری و احراز هویت کاربران را نیز بی اثر خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/694329" target="_blank">📅 20:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
یاوه‌گویی دبیرکل ناتو: اروپا باید به ایران حمله می‌کرد
روته:
🔹
صریح بگویم، اروپا ظرفیت آن را نداشت که توانایی هسته‌ای ایران را از بین ببرد. ما نمی‌توانستیم، ظرفیت آن را نداشتیم. در ۱۰ سال می‌توانیم و باید این کار را انجام دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/694328" target="_blank">📅 20:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">20-2 Ane Manaee (1404-02-05)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/694327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیستم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
غلبه هوای نفس بر حقیقت، نقطه آغاز فتنه‌هاست و ریشه اختلاف میان امیرالمؤمنین علی علیه‌السلام با مردم [ 00:00]
🔹
روش و تاثیرگذاری متفاوت شهید صدر و آیت‌الله مصباح، یکی در عرصه مبارزه نرم و فکری و یکی در عرصه‌ مرجعیت و رهبری انقلابی [03:06]
🔹
اعتبارسنجیِ طاعت و تبعیت از حق، با آزمون صداقت در هنگامه "عظیم شدن امر" [23:27]
🔹
وسواسِ افراطی در طهارت یا بی‌تفاوتی در حق الناس، هر دو نشانه بی‌اعتمادی به خداست و از مصادیق "فی قلوبهم مرض" [25:00]
🔹
نقد به مفهوم "اعتماد به نفس" در روانشناسی مدرن و توصیه به “سوء‌ظن به نفس”، برای پذیرش نور هدایت [27:44]
🔹
طاعت، شاخصه‌ کلیدی ولایت است و اعتماد به ولیّ خدا نشانه ولایت پذیری [29:47]
🔹
رابطه‌ میان "فرار از میدان جهاد" با "فساد در زمین" و "قطع رحم"، از طریق ایجاد تفرقه و گسست اجتماعی! [34:09]
🔹
تفاوت انسان و حیوان از منظر قرآن؛ انسانِ فاقد چشم ملکوت‌بین، گوشِ باطن‌شنوا و دلِ فهم‌مند، حیوانیست حس گرا و زمین گیر! [38:24]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/694327" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX21O6rGFqUxffFDrTCsZ5ASs8TyOJYSCkh57rLyIlyAVPDmmFFNK7owoD8Z9W_knVbthM0xBEISU-kKMy7qWFCOryeFpkxBR75mlzLLkJzoMJOYsDFV0Jm5qwrKJpEq7-megTFx0FpzuVrCzZQGd_Fr5ogr3FWUzPaygs3RofqYw5uiUccVnQSiDIVfWb7mfkZs1vLekCEJ4h6cb8FHOuIMLzsVR4mJuaNeLgrn8iH-QiL8Pv1iB9yAnobSgvXUsi-wFa9O61PY4RlZEQEnIj6cmSQy4i0-RIgR4PU9NMGrqS2hhiwyTrF87jpUVa8_zJN8wHn8-RxEdD43YCA93w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haPnlZPYlww4QwyBzQdgyXTHowSlWsjfxxM9h7IrooGcnKvqao1Eg3JCZOJEujQapXCOrtL3IUClieBhyjY7pKoGVAO3i4Csn--gQwwVRSNSxj0-gDKeAqiBiL8stKBFGE44OE6rTtOaXmqt2X6NFjJaSYAWzVRU3PV4zzm0J-D6EkP7hJapcoDVp-unmq0nLxQJ1nX6GSWDGo_xqz-5LMunkynXjRc1AkT3PmMf9zLhQt1bMZu_pdSY54Qpy4u3d-Qj0qv3O1R4kpOYvZpFIRKBxSA8-r0EPWjA1zEcCmB7x_PtMrfxcoTpRGXRBjrShIQWRrsuXusUmtqySnyFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGoYOafp35-Zry0yK3oAPrIeTv5eR_3KF7ylV10p12MxRQlKaDpJNEE0Z-_vhnHnLUxAze3C2JJuUS2KStwUm167xcfsfNr7nIHZGkcF-yEfCjawfSTaa6Fb6ZrIgTg_VKd65HA_gwbQSFDusVL-0Y906yl0ikGT0tegPhPQJRC1cQFp2fJ3tjl8cP-tcSd6iAFPX5Kg2hQPOHkdwS4J9K5TneQTK43FEfRncRs04pGl3mjFeE9AcdJHPkA44LaN41WLlCOM89WPltdfJxO6_4xkqUhDcNZbNiEk_E3t8dnskycf88IqR6bjMQWeI7woCJlKZj4-8BbLigJG-aK7zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری جلسه هیأت امنای سازمان فرهنگ هنری شهرداری تهران به ریاست شهردار تهران و با حضور حجت‌الاسلام قمی و حجت‌الاسلام طائب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694324" target="_blank">📅 20:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpUJZ7VzXrHPHKdnXMN30XcwuNSi1W6j0iJzVNakGvJhvoY3eRTo5ej6JQZ8ttpHGPos0y6SYw-hWdtLmTedwWhxKRhFvInb0-9OvXhzgYV6BXXSKWAECMxFGeigDLfwdIsDoTZPY9g3M_eIsmiS409AY1SIEuTLpJjGpfJVqguWmMkUCEIUoGK9wTLIjm4COy2-1PXpjpk-YooESDJbj3l31k8df2w_nTF8xQihCj0iV_Vdn6phFJ7J_-6H2Tc6J2r-De5B193ipf9hsJ14NW8xDv6eyNL_ADZ4Ui-0K6OQ0gSIstWbJxBMy8nd-itqsINAeenzJlGbV9O5WIsJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e19VurabI-eWnaCJzmXViysiUAb9k2aMOWkXCsFYVYICnF0skJBE0NMwrwCsr2P0b1mRhATlYiJ3ohr_ahglPnwqM1IK02ZtilBD3GpA4tDrKl-Ps78E8jQ3H5s6HAqzxep0XONamr7o_cHsK3EyrrTHNO6Kco3ziJzp6I3uGawYTQNFZQCzzNGoaomoGSsOU8h88-I-lNAI1qlwMJf7HFVrKW7Ej867iEthqNShOiCV91bXTFTav9LaUfLp5vIWcOIXzv59aPXTl2UFvv4Be5-TtKIy9NLoZQWDp-iDCaj-Vh_appNLWKbbqy17_UAKtZnhmROPFJruI5knrP__sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار پزشکیان با روحانی و کروبی در مراسم ختم احمد ناطق نوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694321" target="_blank">📅 20:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فرودگاه تبوک عربستان: پرواز فلای‌دبی با ۱۸۰ صهیونیست ساعت ۵:۴۰ فرودگاه را به مقصد تل‌آویو ترک کرده‌ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/694319" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDiCBctDNJJwKEZnf-w91XphCrDZ3WFcAxznDSF567I4cErzd39bG7Y5k1UXPfrUm_IpQWBusd73rcn7oO6uwuJ3kSJAhq2fjr9hEzmEvEJV92XQ5zy83SBdYHjv3Qni7rt8bpq3bxlkGMhiF4bQGMJzdc0nWECDlfzh1gKM0quPo0H9FAUL9uz4RgNkgBAKoqfwQ1xmmhCKwaxLDB_QO7rKkwm7xeWVZlI5dhHRuDCpfK-ZuHpiIwMLTxkYGTCEKQklR8e4fwiJtSnHuIDPf7wnITeKADg9Oa0puKdxcQ6DjFlMuW1X9q6979KKc-1ZXXGZ7fMVv_JEiaxUSWhOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شایعه مرگ جکی چان تکذیب شد
🔹
تصویر جعلی «۱۹۵۴–۲۰۲۶» باعث انتشار شایعه درگذشت جکی چان شد؛ گزارش‌ها تأکید دارند او زنده و همچنان فعال است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/694318" target="_blank">📅 19:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
وزیر اقتصاد:
افزایش اعتبار کالابرگ تا آخر هفته مشخص می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/694317" target="_blank">📅 19:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
انتظار ثبات ارزی با مداخله بانک مرکزی
🔹
با اعلام سیاست مداخله ۲ میلیارد دلاری بانک مرکزی در بازار ارز، نرخ‌ها در بازار آزاد وارد مسیر تعدیلی شدند و این روند در معاملات فردایی نیز بازتاب یافت. افزایش عرضه ارز در بازار می‌تواند از فشار تقاضا بکاهد و در کوتاه‌مدت به کاهش نوسانات و تعدیل قیمت‌ها منجر شود.
🔹
همزمان، در راستای تقویت سمت عرضه و مدیریت تقاضای بازار آزاد، سقف تخصیص ارز به هر کارت ملی از هزار دلار به ۱۰ هزار دلار افزایش یافته است. این سیاست می‌تواند بخشی از تقاضای ارزی را به مسیرهای رسمی منتقل کرده و از فشار بر بازار غیررسمی بکاهد.
🔹
در کنار اقدامات سیاستگذار، افزایش نرخ ارز به سطوح بالا، ریسک ورود و خرید در این قیمت‌ها را نیز افزایش داده است. در چنین شرایطی، رفتار معامله‌گران و انتظارات نسبت به تداوم عرضه ارز، سیاست‌های بانک مرکزی و تحولات سیاسی، می‌تواند در تعیین مسیر روزهای آینده بازار نقش مهمی داشته باشد.تداوم عرضه، همراه با سیاست‌های مکمل برای مدیریت تقاضا و کاهش نوسان، از مهم‌ترین متغیرهای اثرگذار بر روند بازار ارز در روزهای آینده خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/694316" target="_blank">📅 19:46 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
