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
<img src="https://cdn4.telesco.pe/file/li5gdq7LJk4jqDFPBT3Xwog_LsHcchQDUGaupdzRu8keTQpOiNn6bKqeQmU7T6VdJ65Eb5_0Lal_ui3bvOEl49Si1Z0uZF4zb83bp97uanxfdi0y3LEqtny7Fztkqhag17BXBjaPjYlMT7iw6h9i2bufAqo3YQQAx2MqimkbCYrFPDlTjIxh-X_vBmi8pSScrC9iGVCcgSg1EB2D5d7CCdeSTcgRZWoFoTjzSbLMC3pLhqCiFYLhJY-2TgWg-ZsAVhXiz1Wgf0zk-nENA4AXuR_ZbBI-iDAn7vy8uKyzMil9ccufvRCL727NkR28u8DdGHovNLQh0usWDyeP5Vtapg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-675979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وقوع زلزله۷.۱ ریشتری در ژاپن
🔹
زمین لرزه ای به بزرگی ۷.۱ ریشتر جزیره کیوشو در ژاپن را لرزاند.
🔹
در این رابطه هشدار سونامی صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/675979" target="_blank">📅 11:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای کشته‌شدن یک زن در میدان علیخانی اصفهان کذب است
🔹
از ساعتی پیش، ادعاهایی در فضای مجازی از سوی برخی رسانه‌های معاند مطرح شده و عنوان شده شب گذشته خانمی با هویت معلوم در اطراف میدان علیخانی اصفهان کشته شده است.
🔹
براساس اعلام دادگستری استان اصفهان ادعای مورد اشاره کذب بوده و گزارشی مبنی بر کشته‌شدن زنی با هویت عنوان شده در محل مورد نظر واصل نشده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/675978" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiXGFMxIEUdXvLyB0ZZUHFh82Y6N6tVCVCHGXXq59v7G94-0ndh3ckuTLHQhwSTsSsXu2pm6G-IUZdB7_sTnK08r0kkHssJgxN31QcBK4WUIx91Ftq5w1nOyCm2lohxUtu28VDY7d14t-yGxh4v5wLzMferwwSn9zrSY5rWPm515MVhAG5mgZJv-gpxtZhLfWTlVJEf4xaWXPX9fjprqTBEqQJzWQwQTmpv2pXZ7JnpVgjKcsbs39DhmLkZ29JhPIE4BcuniWJPXnJVPzd5Gh6MJmcG8vER9sjkYxfDnyH3bqPlbU9EcvCd7wHRW3Fy5BSLLL_CHxco071R7o9eaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق؛ عامل اصلی آتش‌سوزی خانه‌ها
🔹
بیش از ۴۰٪ آتش‌سوزی‌های ساختمان‌های مسکونی ناشی از مشکلات برقی مانند اتصال کوتاه، نوسان برق و سیم‌کشی‌هاست.
🔹
طرح «پلاک ایمن» امکان بازدید رایگان کارشناسان آتش‌نشانی از واحدهای مسکونی را فراهم کرده تا مخاطرات ایمنی ساختمان‌ها شناسایی و پیشگیری شوند.
@amarfact</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/675977" target="_blank">📅 11:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buheFm2qeDIQTPtyeqvuIKnkw60B4ibH7tws_nyg6x2auzMrSVJC4Vhh5L4yRgxtjD4go82g0ox2WccjKZGDousmF_jG9bEZKNqkp_OcH5zcWQF8zoDqOQmfnXd2MN8O-TYfQD0gDeB03KmWeA--Bzk7VRBhJlVlTAKN8Gfc4yibneKIO7noZjs-IySVgutBMF_ONoD8LAcwXt4-YKCUfi9OQiDKNBLk8SXglRpU4JAFiACe_VXcZAtWcsSilSWIcTUQc_v_lX4Q1tL8RoM3JuP8RAxfFX7jvcIoX6Dg-fYmc7dia6CWq-P-xfqzF2P2wEyqFSLxrHU984TIvDMEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نشنال اینترست آمریکا را «بازنده» درگیری می‌داند؟
🔹
داشتن قوی‌ترین ارتش جهان روی کاغذ، لزوماً به معنای پیروزی در میدان نیست.
🔹
بر اساس این گزارش، ترامپ در رسیدن به اهداف خود ناکام مانده و توان بازدارندگی تهران همچنان پابرجاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/675976" target="_blank">📅 11:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
عرضه مرحله‌ای بلیت پروازهای اربعین
🔹
سازمان هواپیمایی کشوری اعلام کرد عرضه بلیت پروازهای ویژه اربعین همزمان با صدور تدریجی مجوزهای عملیاتی شرکت‌های هواپیمایی و بارگذاری برنامه پروازی در سامانه‌های فروش انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/675975" target="_blank">📅 11:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ صدور شناسه برای کالاهای تقلبی
سید احمد حسینی، رئیس اتحادیه لوازم یدکی خودرو در
#گفتگو
با خبرفوری:
🔹
اجرای نادرست قانون مبارزه با قاچاق کالا و ارز و صدور شناسه برای برخی کالاهای تقلبی، زمینه عرضه لوازم یدکی تقلبی را در بازار فراهم کرده و کالاهای اصلی نیز توان رقابت با کالاهای تقلبی را از دست داده‌اند.
🔹
افزایش شدید قیمت خودرو و هزینه‌های نگهداری آن نیز باعث شده بسیاری از مردم به سمت خرید قطعات و کالاهای ارزان‌قیمت و تقلبی بروند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/675973" target="_blank">📅 11:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سخنگوی دولت: سهمیه بنزین ۳ هزار تومانی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/675972" target="_blank">📅 10:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675971">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند  فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675971" target="_blank">📅 10:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoF06wrR_DKPTK6jGwL1AuFeewOwv6t1y-H8haO_j1eqqV32Um7hO9iwEiB_LrEL1sAyemv5BM8kitQWJQLLuj7izZldVtoDE4cX7_SH9Eh93NNKS_4VeGOTdREyVTTAjFYrTXO3vzSRU48fBKbsLsI83bmDCTWcWBmGIFq6z7wgXfCYBChrand2GJ2M0larIFkzE6rrRw7K61Cwdr8wLlxVLVOwiy2mI-j8mH46IfRKQIBf3h2-yXIOaeKaDykRTBi0eUXdMqX367Hve_sMe-yatFWQM3IrB5ATXa-jS9WYU78QewM1R-1NeKFzw22bbFQ29x0JDQqFyZ5zj41afQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebc664648.mp4?token=IpKBjpmDXlb64U9QCHa0KPRfv-a22-KSjXz5_Jtng1gMe7zMGSqbXP7o6NROYv8B_i3terqepBjXHGGhadRHjOvsHonhp0GukhgMsOWmfJpqZg6mB_hkVPB8D9LULVuCbEOta599M_igWpI0XN1Ilvw08oliZ6c0PPIepqEX4u3iQhBrO0Pir264ay9bSCy_8DE-W7WLZVzKo0U2ZKb43-LVGUiYBHNo0N6MsGYdb-RDnG3sI7bl14qMuXau9QQ4rnsso4X3QY_-qjg3i0kOvsJyr0bi73iiCNDO2cqYtOkEoFYwEuGcSod1xe6utTaoQrPowuCZESz1zR4Ub0zYUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebc664648.mp4?token=IpKBjpmDXlb64U9QCHa0KPRfv-a22-KSjXz5_Jtng1gMe7zMGSqbXP7o6NROYv8B_i3terqepBjXHGGhadRHjOvsHonhp0GukhgMsOWmfJpqZg6mB_hkVPB8D9LULVuCbEOta599M_igWpI0XN1Ilvw08oliZ6c0PPIepqEX4u3iQhBrO0Pir264ay9bSCy_8DE-W7WLZVzKo0U2ZKb43-LVGUiYBHNo0N6MsGYdb-RDnG3sI7bl14qMuXau9QQ4rnsso4X3QY_-qjg3i0kOvsJyr0bi73iiCNDO2cqYtOkEoFYwEuGcSod1xe6utTaoQrPowuCZESz1zR4Ub0zYUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه گرین به کاخ سفید؛ مردم آمریکا نان می‌خواهند، نه انیمیشن
🔹
مارجری تیلور گرین، نماینده سابق کنگره آمریکا، با بازنشر انیمیشنی که حساب رسمی کاخ سفید درباره دستگیری آدم‌فضایی‌ها در دولت ترامپ منتشر کرده بود، نوشت: مردم توانایی خرید بنزین، مواد غذایی، پرداخت اجاره خانه و تأمین هزینه‌های مراقبت‌های بهداشتی را ندارند و این مزخرفات عجیب و شرم‌آوری است که حساب رسمی کاخ سفید منتشر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/675969" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند
فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.
🔹
در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند.
🔹
برج مراقبت دریایی چابهار با اصابت ۱۱ موشک فرو ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/675968" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم اما اگر جنگی به ما تحمیل شود خیلی خوب دفاع می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/675967" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
فردا ادارات کرمانشاه تعطیل شد
🔹
ادارات و بانک‌های استان کرمانشاه، فردا چهارشنبه  به دلیل گرمای هوا و ضرورت مدیریت مصرف انرژی، تعطیل است./ایسنا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/675966" target="_blank">📅 10:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ قلاده خرس قهوه‌ای در ارتفاعات جنگل‌های هیرکانی لنگرود مقابل دوربین‌ها ظاهر شدند
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/675965" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675963">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جلسه شورای هماهنگی مجلس با حضور قالیباف برگزار شد
🔹
رئیس‌جمهور لبنان: ادامه نقض توافق از سوی اسرائیل را نمی‌پذیریم
🔹
استاندار ایلام: از اول ماه صفر تاکنون تردد زوار اربعین از مرز مهران به یک میلیون نفر رسیده است.
🔹
چین ۱۱ جنگنده جی-۲۰ نزدیک مرز هند مستقر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675963" target="_blank">📅 10:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675962">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تحقیق کنگره آمریکا از اینفانتینو به دلیل دخالت‌های ترامپ در جام جهانی
🔹
معاون رئیس کمیته قضایی مجلس نمایندگان آمریکا، با ارسال نامه‌ای رسمی به اینفانتینو خواستار ارائه تمام اسناد مربوط به روابط فیفا با دونالد ترامپ و تیم او شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/675962" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاستا آلفردو رو با این روش درست کن ببین چی می‌شه
😍
مواد لازم:
🔹
پاستا یک بسته
🔹
سینه مرغ یک عدد
🔹
قارچ به تعداد دلخواه‌تون
🔹
خامه نصف بسته
🔹
شیر یک لیوان
🔹
سیر ۱ یا ۲ حبه
🔹
کره یا روغن مقدار لازم
🔹
نمک و فلفل سیاه به مقدار لازم  #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675961" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0a93054.mp4?token=q3bea-qD2-rp7Q_y1jcHOWWb7s4WGey74LvaX--8mUTXxqR2cjpplpMLl9IUzDIpTOgw5tIPUuz1AdddUny_ZQzIVJSa8kEcDwrUFKGG3dhroMfe7dnnjHdIuRwH9u7w6IaZ5uDNbQVgicHPEl46hN_eO8SoXkUBpTn_KYCwB9z1X8lZxPFiFrUtqJ5o9oULigSuWsTs2Y4XqQgI62bVgoNE4xkfGIjBe75RUOeybHemN8Pp0ffNu8_0HhUVcZvBFCjVJMOubwjHh2xwthkrkpmrofDvBmvUQLvv5EGfBKRONGCk7kWzjJ3f6xgV8ZBrF7k56ojYm8bWZg6eGJXUZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0a93054.mp4?token=q3bea-qD2-rp7Q_y1jcHOWWb7s4WGey74LvaX--8mUTXxqR2cjpplpMLl9IUzDIpTOgw5tIPUuz1AdddUny_ZQzIVJSa8kEcDwrUFKGG3dhroMfe7dnnjHdIuRwH9u7w6IaZ5uDNbQVgicHPEl46hN_eO8SoXkUBpTn_KYCwB9z1X8lZxPFiFrUtqJ5o9oULigSuWsTs2Y4XqQgI62bVgoNE4xkfGIjBe75RUOeybHemN8Pp0ffNu8_0HhUVcZvBFCjVJMOubwjHh2xwthkrkpmrofDvBmvUQLvv5EGfBKRONGCk7kWzjJ3f6xgV8ZBrF7k56ojYm8bWZg6eGJXUZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخازن ذخیره‌سازی گاز عربستان هم منفجر شده است
🔹
نیروهای مسلح یمن دیروز تاسیسات بقیق را با پهپاد هدف قرار دادند. سعودی‌ها مدعی بودند که پهپادها را رهگیری‌ کرده‌اند اما چند ساعت بعد فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در این تاسیسات را متوقف کردند.
🔹
حالا این تصاویر نشان می‌دهد، سعودی‌ها روی دو مخزن ذخیره‌سازی گاز، پوشش‌های خنک‌کننده سفید و سیاه نصب کرده‌اند تا از گسترش آتش یا انتقال حرارت به سایر مخازن جلوگیری کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675960" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: مرگ لیندسی گراهام، اسرائیل را با چالشی جدید در آمریکا روبه‌رو می‌کند؛ چراکه او نقش واسطه‌ای مهم در کاهش اختلافات ترامپ و نتانیاهو درباره ایران داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/675959" target="_blank">📅 09:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA6vl3_IiWJVbaRwZwuMsyUSVxPoM0FRAkkBAtupp_ZlaUTMUuJpttOXa_m0lAMPn-lY3UxV3ZOVhGEh1E2K1PSbpJE6Zea1CeE4uvz4sv4-VVmW4X0bRndqfWZNsB3pAzezELJIrF_3ZlQXlRzwk94vfqsKQcxYtgebyRQcE_gpYf3lJiCphE-7efFfZHJljKbzJOqTA8nIvJQJsXS0WPlVbMn8ol2E44V84fCgyZpFIzozg2cr8dklRWNlNt35dXmbPOHQ1jU56zA32zjoU7HxMohFktbVke-nUvRuw8NSIhNTLmj22KW5TcBhDPEIDU8XN22Vezwz6ZGf4Fvoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم شوکه کننده کریستیانو رونالدو
خبرنگار عربستانی نزدیک به باشگاه النصر:
🔹
این ستاره پرتغالی احتمالا در فصل آینده در کمتر از ۵۰ درصد مسابقات النصر به میدان خواهد رفت. رونالدو معتقد است نباید در تعداد زیادی از مسابقات بازی کند و برای جلوگیری از خستگی، باید از سفرهای مداوم و فشار مسابقات بکاهد.
🔹
رونالدو تصمیم گرفته پس از پایان قراردادش، از النصر جدا شود و آخرین فصل حضورش در این تیم را با آرامش سپری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/675958" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی هیئت رئیسه مجلس: صبح امروز جلسه شورای هماهنگی مجلس شورای اسلامی با حضور دکتر قالیباف، اعضای هیات رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/675957" target="_blank">📅 09:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
صدور آنی کارت سوخت به کجا رسید؟
🔹
متقاضیان می‌توانند با مراجعه به سامانه درخواست خود را به‌صورت کاملاً الکترونیکی ثبت کنند، رمز کارت را از طریق پیامک دریافت کرده و گزینه دریافت حضوری کارت را انتخاب کنند.
🔹
زمان صدور کارت از حدود یک ماه در روش قدیمی به یک روز کاهش یافته است. امکان ثبت غیرحضوری درخواست، پیگیری الکترونیکی مراحل صدور و تحویل حضوری فوری کارت، بدون نیاز به ارسال پستی، فراهم شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/675956" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCzz2Rx0pqosOGnlV-NFnsuLPV6ngfdNpU6F7rhJOyDH4Z7H-WpBFOLfUZ1njrDRwl4QCzwizccS2SIod2qe8DZAZLeDOHXFCZwzZXmH43oDRyyf5AHdARkK-kQpS2CnGeAOXQWnjmqKRE79zLXzjyWyFPt-Jx48AvEX024F2aQlf2pVkWqzG3hbAjkommbc7zp1qzg9zTehYNnDmv9QnxAEQOYpa41S1sQcOs-3rNnCqHakpyvko265y2KybNgCl56IESITDDVg3c4JDtduEf-Ap8WBINrlT-fkP9pBUIP3WXmBC52JECaPgUJLNvFGfsUAMJ3DVvaM8imbbqfApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۴۲ هزار واحدی شاخص بورس
🔹
شاخص کل بورس تهران ۴۲ هزار واحد مثبت شد و در آستانه ورود به کانال ۵.۱ میلیون واحد قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/675955" target="_blank">📅 09:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دوتا متریال ساده، یک آباژور مینیمال جذاب درست کن
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675954" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حملات گسترده پهپادی به صحرای شرقی اردن
🔹
منابع محلی و خبری از حملات گسترده پهپادها به صحرای شرقی اردن خبر دادند. این حملات در حالی رخ داده که هنوز جزئیات دقیقی درباره منشأ، اهداف و تلفات احتمالی آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/675953" target="_blank">📅 09:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه‌ فرود اسپیس‌ایکس استارشیپ بین پروازهای ۱۲ و ۱۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/675952" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حملات گسترده پهپادی به صحرای شرقی اردن
🔹
منابع محلی و خبری از حملات گسترده پهپادها به صحرای شرقی اردن خبر دادند. این حملات در حالی رخ داده که هنوز جزئیات دقیقی درباره منشأ، اهداف و تلفات احتمالی آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/675951" target="_blank">📅 09:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
انفجارهای مهیب منطقه شرقی عربستان را لرزاند
🔹
منابع محلی از وقوع دست‌کم ۶ انفجار شدید در منطقه شرقی عربستان سعودی، در نزدیکی تأسیسات نفتی و گازی خبر دادند که صدای آن به‌ وضوح شنیده شده، اما آژیرهای هشدار در این منطقه فعال نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675950" target="_blank">📅 08:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
‌
#چند_خبر_کوتاه
🔹
صادرات قند هم آزاد شد
🔹
عراقچی با وزرای خارجه عمان و عربستان تلفنی گفتگو کرد
🔹
وزارت دفاع روسیه: روسیه از سرنگونی ۳۵۶ پهپاد اوکراینی خبر داد
🔹
رژیم صهیونیستی مقر رادیو قرآن را در قلقیلیه کرانه باختری پلمب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675949" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
معاون وزیر رفاه: تمامی فروشگاه‌های زنجیره‌ای و شرکت‌های حقوقی چندشعبه‌ای تا پایان شهریور فرصت دارند به شبکۀ ملی کالابرگ متصل شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675947" target="_blank">📅 08:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675946" target="_blank">📅 08:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زانو درد رو تحمل نکن
🦵
🔹
گاهی با چند تغییر ساده و انجام تمرینات صحیح، می‌شه فشار روی زانو رو کم کرد و درد رو تا حد زیادی کاهش داد #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/675945" target="_blank">📅 08:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه العربیه سعودی از تحرکات کشورهای عربی از جمله عربستان برای کاهش تنش در منطقه خبر داد.
🔹
هاآرتص: نتانیاهو با متحدان کمتر و گزینه‌های نامطلوب به دیدار ترامپ می‌رود
🔹
زلزله ۶ ریشتری در استان چینگهای چین را لرزاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675944" target="_blank">📅 07:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEOB7vRsoRP6w-wz-cOpV61FAMno6d5vgye-l1T5efWUVVDDsD9EuFpjzCWPtGJGJVzYC1QnbCd6aoSxW-SbNoEEQxk6LayY9YU_mtvpCfrBuH_GF77nQ8ID77gW_Vgh9FoMr9cInRYjTt6MrJbjBqXwBWx8dajMiQkejESqfkrKLToAEuYd9yrsz1Hq54xz3Tof7xTEqCNceYyZdmTtLOCKg_p8NU56zHhCLFHLXnBKWnryeoeQsUF6grBFMWjjtahgwBYfOAu3gqyxhAhTr_gQ5RoIH5kKNE8RxH-7Z4PAiyQo3cKaKbCW2nimKxLVca6qSqPBBvuLag_cY9UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۶ مرداد ماه
۱۳ صفر ‌۱۴۴۸
۲۸ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675943" target="_blank">📅 07:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای رهگیری یک پهپاد در مرز اردن با فلسطین اشغالی
🔹
رژيم صهیونیستی مدعی شد که یک پهپاد را در مرز اردن با فلسطین اشغالی رهگیری کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/675942" target="_blank">📅 06:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
مدارس از مهر حضوری هستند
وزیر آموزش‌وپرورش:
🔹
تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/675941" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675940">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شنیده شدن صدای آژیر در مجاورت نوار غزه
🔹
رسانه‌های محلی فلسطینی از شنیده شدن صدای آژیر در منطقه "كيسوويم" در نزدیک نوار غزه گزارش می دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/675940" target="_blank">📅 05:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675939">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucSgwekfRxqoc_IA9eyHx3v2LtlEkJgegn4in6j3PfZlzHWPjO6OygA4VUTxzWfBcz3WzvOzp-Z4kX5L3sSyjO03Pf8S72ZQCTRt_8-v9yBfRk8IexpVNO5txbsH63mD2fbzn6RXhp4ATWCfeYzhFUMbBjHXZ3jZ2Ux2fd96uOLF8buavPPEKx2KnZ_fw0HL3zFH06oWLbpv5SuuAC4_LfvqhHyytVa88yVmV5hZpGsrcP7Vp2fbFHqzt0kDwzQuUt2m__e8cUBrcmE13DxdG1EzWfRmfCSrjRv5kljgUADH0liY2WMKWYTf1vgcRxCORucWwbwYqhBJnVy1o-wMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عربی از حمله پهپادی به پایگاه تروریست‌های تجزیه طلب در شمال عراق خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/675939" target="_blank">📅 05:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675938">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/675938" target="_blank">📅 05:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اکونومیست: حمله زمینی آمریکا به ایران نامحتمل است
🔹
یک نشریه انگلیسی تحلیل کرد که هرگونه حمله زمینی آمریکا به ایران، خطرات بسیار بزرگی را برای نیروهای این کشور به همراه خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/675937" target="_blank">📅 05:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czo0vE-CeWlggnZ67Lv3CtMoZmnOqNuVVWu_RhY6ABy80vo4i3KFBSfwVr8xhurVSescAg53lXs9m2F92_82X1v1Fix0JkPWajUcKPETQy3nPctUPo3UXVr7eBIF3Dsmu8ccwJaOZdT29-jHJdASpi72DuCgcEoNwkSVzw_An5g8FmJZLJ2QwvXz1AcPkkd7D2g4tvsX6xVbzNaZoXlHm-dPXjGCd8t2KBa9Ox05vIr8Jgctfm7ldA1aPFuM7s2739yYUeMgBXO6GwCi6vjPpTk3rJECyDyWF1XrE3gvpLnjSe8Yl37fBDelKFhxFmG4ME7fyv2MCh-fX3LKg2BCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/675936" target="_blank">📅 04:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
بلومبرگ: تمرکز مذاکرات ایران و عمان بر بازگشایی تنگه هرمز است
🔹
یک شبکه آمریکایی به نقل از منابع مطلع ادعا کرد که ایران و عمان در تلاش هستند تا برای از سرگیری کشتیرانی از طریق تنگه هرمز به توافق برسند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/675935" target="_blank">📅 03:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675934">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/675934" target="_blank">📅 03:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675933">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔹
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/675933" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675932">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7j7Gj3ZO124eubdh0utRnBAUKL1mf6vB3-oUM1BClUYI7tnKip1YR7OYa43T_EyBIOrG8LLVvNEVtPIAtrGJjO67B3UJznvpcdQ-WSVeow9hxeTh39pkz4ftuF0S-VVnlin0sIclFgCMMdNAVD3MNPJHQD5O9raxwnKjnIBLc4GVeFWqHPILxKN_j25j7lp8UtAgJfddUwlrKYIhLQof6hhpJfgCVrZBoc5Ah85rd--GJMB69fmcMIOQ21WaY65LUiUlWjC7mlIr7KjlpePS13SL3y20u4-xOGiE1KPdLapavwa24BOG9_Hjy3cBQba6tg5l4_1eITIwb_HFWN7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت آمریکا در مورد کاهش شدید ذخایر مهمات دقیق، به‌ویژه موشک‌های تهاجمی و پدافندی تمرکز دارد.
🔹
طبق تحلیل‌های مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، ذخایر برخی از این موشک‌ها به شدت کاهش یافته: مثلاً حدود ۳۰٪ تاماهاوک‌ها، نزدیک به نیمی از Patriot و THAAD، و بخش قابل توجهی از JASSM کاهش یافته است. بازسازی کامل این ذخایر ممکن است ۳ تا ۶ سال طول بکشد، حتی با افزایش تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/675932" target="_blank">📅 02:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675931">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ابراز بی‌اطلاعی گروسی از زمان بازگشت بازرسان به ایران
🔹
مدیرکل آژانس اتمی در مصاحبه با شبکه «بی‌بی‌سی» با بیان اینکه ایران هنوز عضو معاهده «ان‌پی‌تی» است، گفت که تهران باید اجازه ورود بازرسان را بدهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/675931" target="_blank">📅 02:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675930">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/675930" target="_blank">📅 01:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن صدای آژير خطر در کنسولگری آمریکا در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/675929" target="_blank">📅 01:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار و آتش‌سوزی در مخفیگاه‌های جدایی‌طلبان تروریست ضدایرانی در أربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/675925" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که کنسولگری آمریکا در أربیل
هدف قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/675924" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
منابع عراقی: بیش از ۷ انفجار در حومۀ اربیل، مقر احزاب خرابکار و تروریستی را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/675923" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات به تجزیه‌طلب‌های ضدایرانی در أربیل
رسانه عراقی:
🔹
تاسیسات راداری و مقرهای تروریستی در مناطق خلیفان و سوران در استان اربیل هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/675921" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/675920" target="_blank">📅 00:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/675919" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
گزارش‌هایی از حمله به یک میدان گازی در شمال عراق
🔹
منابع محلی بامداد سه‌شنبه از حمله به میدان گازی «خورمور» در استان سلیمانیه واقع در منطقه کردستان عراق خبر دادند.
🔹
همزمان پهپادهای تهاجمی خارجی نیز در آسمان «اربیل»، مرکز منطقه کردستان عراق، به سمت اهداف خود پرواز می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/675918" target="_blank">📅 00:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی: نباید در مورد NPT کاری کنیم که بهانه دست دنیا بدهیم
🔹
اگر حفظ نظام جمهوری اسلامی نیازمند حرکت جدیدی باشد مطمئن باشید مجوزش را خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/675917" target="_blank">📅 00:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیباترین گل جام‌جهانی به انتخاب فیفا
🔹
گل سیدنی لوپز کابرال، بازیکن کیپ‌ورد به آرژانتین در مرحله ۱/۱۶ نهایی، عنوان زیباترین گل جام جهانی ۲۰۲۶ را به خودش اختصاص داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/675916" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4dR7K84yk4kezEYOuIMtrXK-bdlKPf3jJy1rJbnXh6TbNAmeHvI_Cv53pNVuzdagoKB2f3s1ixdrkMsYk4-QF46h5Trk2FFQjyH-NXglyMTOraFZi6wMfNceiFecaGcS-IRrqgynPatRxuhzyR8bcQjR-Azmers6chLqt1dEJm2GRuy5UGZ_E8c6rBepCZ5zFVtqfBrmPgl2PGAIyvehw-XDlKJLSA801ZKJzmnGrZi1JqohCw5_nz0zRMq52qTgNK9pmzjBBaGyEN3UIL5yrwu5svIAVkdBafsZFgPxY_EWlxgqYLti69phSS72f157iCX9OV-Ur5gcSX244kSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/675915" target="_blank">📅 00:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0144687c28.mp4?token=ZTzRMsmrSV5kvME-Od5_vnmy0F86P6cbYIybm4dxV7e6OXJ7WETyFC0iPZ0k9s8Mfbp3SV6deP7gpB-djGYDQ4oY-hTXnOhAeYp_cOuh70oTvFnCU_SG9a-IH4mLTP8YR7w4AqJAz_k1j7tTD2IjHzS-MsgQVFiy-XaS9KbUHDT117DR8CQkijCsODRNJ6m0LH7umqacTGwbvaYWGndc4L_3AXf42KhMfNztQKcgitU3QctDOoKNZ-1DhG-JyHqoeiVLlslvoo_3_0-sFrtc2F4WVtO8WesVIzcS2IMq36bPfFx975B0mEkie_fFMiqau3g5Th0tx32lzjlWhp_ICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0144687c28.mp4?token=ZTzRMsmrSV5kvME-Od5_vnmy0F86P6cbYIybm4dxV7e6OXJ7WETyFC0iPZ0k9s8Mfbp3SV6deP7gpB-djGYDQ4oY-hTXnOhAeYp_cOuh70oTvFnCU_SG9a-IH4mLTP8YR7w4AqJAz_k1j7tTD2IjHzS-MsgQVFiy-XaS9KbUHDT117DR8CQkijCsODRNJ6m0LH7umqacTGwbvaYWGndc4L_3AXf42KhMfNztQKcgitU3QctDOoKNZ-1DhG-JyHqoeiVLlslvoo_3_0-sFrtc2F4WVtO8WesVIzcS2IMq36bPfFx975B0mEkie_fFMiqau3g5Th0tx32lzjlWhp_ICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی تصاویری از سقوط پهپاد آمریکایی در نزدیکی سد حدیثه در استان الانبار منتشر کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/675914" target="_blank">📅 23:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقاومت عراق، اتهام عربستان مبنی بر نقش داشتن عراق در حمله به تأسیسات نفتی این کشور را رد کرد
🔹
ترامپ سه‌شنبه میزبان زلنسکی و نتانیاهو در کاخ سفید؛ ایران و اوکراین محور گفت‌وگوها
🔹
مقاومت عراق: هرگونه اقدام «احمقانه» از سوی عربستان با پاسخی سخت روبه‌رو خواهد شد
🔹
واشنگتن پست: طرح آمریکا در حمله به قایق‌های مظنون به حمل موادمخدر شکست خورده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/675913" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای پلیس چینی «کلاه ایمنی» را زیر نظر می‌گیرند؛ تخلف کنی، هم هشدار می‌گیری هم امتیاز منفی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/675911" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQsPF2bN2ogJtjMGYbqCvtwiUsZpzuxpJQoWGmYCBdfLORsWitfGbsNNUnhgHkqXmcCGPxWkJxn3WZGB0HmXbAMG1QdxhV_TCJHKOJC46zni_xEaBMdnJYc69AJ_1-RhcUFs6mGwbOaA_RiVxrlTfWjbxDy9XRsZoDLnweqGoaAoYZk7lxpsn4VREwd4W8N7G6nj5mSFafst4C2h4QyNNSNWH3meEZ5hbeQuU-J35a9sWR-kkaFk45KIlbW_OJIll_fkrITK0Qy7B6KjpbiBc7LvXf5C4CMzfusALOMMCyESBUgP2kS4gROz_59QfL9vN3HXcIWyEZKOQf_TTq7z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاله ظریف در الجزیره: پنج دهه استراتژی پنهان اسرائیل برای سوق دادن آمریکا و ایران به سمت رویارویی دولت‌های متوالی اسرائیل تلاش‌های دیپلماتیک را تضعیف کرده و تنش‌ها بین واشنگتن و تهران را تشدید کرده‌اند
🔹
در حالی که بنیامین نتانیاهو، نخست وزیر اسرائیل، برای دیدار با دونالد ترامپ، رئیس جمهور آمریکا آماده می‌شود، دلیل خوبی وجود دارد که انتظار داشته باشیم او از این دیدار برای منصرف کردن هر اقدامی در جهت پایان دادن به خصومت‌ها در خلیج فارس استفاده کند. این انتظار ریشه در یک سابقه تاریخی دارد که بیش از پنج دهه را در بر می‌گیرد.
🔹
اطلاعات از طبقه‌بندی خارج شده، خاطرات مقامات ارشد آمریکایی، گزارش‌های تحقیقاتی و تحقیقات دانشگاهی، این ارزیابی را بیشتر تقویت می‌کنند. در مجموع، این منابع به یک الگوی تکرارشونده اشاره می‌کنند: دولت‌های متوالی اسرائیل، اغلب با حمایت عناصری در درون تشکیلات امنیتی این کشور، بارها تلاش کرده‌اند تا مانع تلاش‌ها برای پایان دادن به درگیری‌های منطقه‌ای یا تلاش‌ها برای مدیریت تنش بین ایالات متحده و ایران شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/675910" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
ترامپ: در حال انجام مذاکرات عمیق با ایران هستیم
👇
khabarfoori.com/fa/tiny/news-3233599
🔹
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان
👇
khabarfoori.com/fa/tiny/news-3233622
🔹
دوئل‌های توییتری قالیباف و ترامپ و الگوی جدید گفتمان دیپلماتیک - نظامی ایران
👇
khabarfoori.com/fa/tiny/news-3233428
🔹
نیما تکیدو؛ ستاره‌ای که رسانه‌های رسمی نمی‌شناسند اما میلیون‌ها دنبال‌کننده دارند
👇
khabarfoori.com/fa/tiny/news-3233431
🔹
پایان ۵۰ سال فرار؛ قاتل خواننده انقلابی به دام افتاد
👇
khabarfoori.com/fa/tiny/news-3233468
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/675909" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی‌های سگ زرد درباره ایران: در حال حاضر، مذاکرات سازنده‌ای در جریان است. ایران می‌گوید: "لطفاً، لطفاً، هیچگونه محاصره‌ای اعمال نکنید."
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/675908" target="_blank">📅 23:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwxJYvu-p2G5C8w0Oc4ZD_OUsgPKkYdiJK-bHXWKwzU1HOKu2h8MFxZY7YllCzaYldvHjLweQH6ZO32VfWnKoL9uoGB7Og5_pGc9CHYk76vomOI50vLt37zNFqW31WdV7eYFMtoG6nwHOaD17haLx0uPflDxuTO5qAWLY86Zxynl4Y6sT0x4KvjIEhzddjyliZTA1BI4t8-11rxyWjon9XjnLZyN6gSESjhhpi9yXoeKwZGjXHDkgF1tNWa7rE8UkJDHD5G_jjORbFstz0UIQOPFOkXJTTNoQeCIxMbpu-o3ycYNNbjaX1CNR3MLvA2HPAuCBSHZwd4yaLneo0Z8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrJn_3ExNKnYwnLbiKU5F3for4upt1sNb3G_HWUmnz7l0PjNDQeQVP1qAr2tRPAjB9FH18aIMJ_cUTNTmaV36hwqZv8zu91MgPtRSWGvWKrSO2xo5CHN1v6Uw8KL1nuZsV6HwJ_u3pfz7yyg3svH7nzBHr1C1-9YuGrq-VeB-uZa4rtvSCtTfjAFNF617cuYjuPTMG8X2pHV94Q5RKAnN7IKqOz7Wno53rCgsByM_sptCi78k4Lwt23bQ4euncQEN_DXiCNwjAbIcvD0FZToFtQibbKh9PXo-b7pAssqarfnKBv1d-O4XDMXm-tLBxYNRNLm_vRj46w92h4tku66ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-4sYnb9mvT5Fcs8nJX9_1-aPtquVOM-AMuOzXdPYk7geJnlD_lNKXwjLCygbaIKjzuJtBet3KXS92rTQOHLz2EN11R9_Gp-n-vlbiGbz7HEcwPkbTRv9y_2odi0g0Sh9s7mcuVHgc1z6myF1-TFCS3fv_ZWk67jmfxLCI61oGIxgcz_fAm3aI-ObXhEE5tswYv1cwbyf7tmh-dD8v1G-gCY9aGpMVxS5Uh5IfjFxBuBp9DMYDSNQQtfd79KrIFXFabRBfI7eLK9x2jv1uK7RTF5-tbxcS7WHKiPJ1Tth_I8xvGp4d3GsuN2xrc62vUMsCxuX5n3Fg_d4sdNhPStIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKecR7AtOcy32c9-VhPdbMBaCrj5gT65yakjXLFdbof8_7-knvSUvvISfphfMNmo3PEBypCJzTGPQRrqygG9CLuzySXu3gxE9d5sYYHybdPACq1_Q0EXvUSr6R8ta6r5W7QE4_gO77g9uk7oSlkaJ6wOvFL7YkTkscA9OKW4ek9FgF0w-WavyuhxhD7pGO6qqiBdzXokTJhmwFTFjda1kSpywX95V9ik3I07-qE1z9i8GBSl0IZ861S3BnEpnus-gBbgcBMIalA5A5SejkMPLLXA2c1z6beRQZoVMsMVCS9g98mR2B7fOfpBs6Sk4cI-N944sguJjsYSEETJ7cu3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujv_ZrxAU9d-yS-TIMqRw-faGaQaHIFdtQerQNkXGrLBS_jg1h0AuNyoYxLKGVPhbGt80J9Tu-wTvcnA_mqpJ-0k1G42TMYqx_ikeCPqeGt67pUr37-tbiPwf9GW4yVJ9UUr0ybYSYjQux_cddqi6UlMSlIbIazUQv9s4YX2M2GOs3Ilv_cUG9P1-IUARMrl6QBhw05ggGD5qNHZQTFa1v8XLDs7r9p8VmjIJJIvSekGOXxfkpkwGNvPdCDgh_aBj-G3d5LdE-ycd_zcjXetn5zFvG202a2IDZXGCYIeCZtv6kKh93AfBDrMUASdrV1yXTCkvPkOAYDOqJfeRzZCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs_bjuNLz2oGfgi7uMrJk2dY6Y9DyTLtVi1BTQMDD1u3Bk9ZSBz8wLZybMP6Hdq-SPKURgARLZ19Q4Yf-55EKUlTOHpfwESD98dMDMWMPMFEZBFLg5RSDo-rcpjNbhG0E9guI4yoAYedud2e285tqaMy64-p65wTkc5mtW-jFmSYGKWV5KVYFNDAeuVyfT4qqb4gjl4rTULp26MJKPtbX8iTZofFSwk1dnWqdkwob5hMXTg3krb-BeSWAM-cTutpTN9tkHk0usZr9dCGqPVYm4tlPV92HasJyMAbB8s278B-IIk7bdSwUhFlbmyxVcYdHe611XTACOA_Hk1yYnXETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvnUlNzabJd3jK7CQ4_facXdnf7zZIAN0NqLP9o3GNuwKI7I-z3zx8bmfyT_Nk1ICPizgNxICsRKCQL1YcxngXIUkqBhqIAbpT_FOSqGmzxoxw6uV6iBLPJDgVrFk3up6qTgXRMYb4wpmH_1oPbA26dkyuWWmG87H4itmNVQywc3DXxHCBLHKRjKa9b_sv7kcMM8fu0zgpYzYZIY8CtbFIfvpg_kVHk717nwwV4FSC0XWgDA-z6uWkJkQzyvhCD7Dun2atyZqyZglahcZ2RwHI7pgm83eQ8t-Iyy6aC904eue-eja7aIZtyn_z3S2OPjOgY_42HMeL_igrANSP3Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRkRYovyK3PSC6dRq9P68SHlggLsECK0W1L5SosMoviKG5WjQQzpH2qavx1Lj_-Ip_QiuGJRlgl-GJ7jWqnfVk_MGF_eAuAyq8YfAE3d8iF6Emwd9Ubu2FKtAZsg3wGvN9HBj95bVWyAcrJhu7b3AabKfTVAnNOT1-wa7kdWFjtwN1db8wGl0PgI4bWhJ4IVOwOlEEmIPrcDosGuivgDJP2z5qUsAzfsjkeh_XywDu4K2SgP7wOWjMv5-dISNhHDYPZvd-h3Z3mCz2JlFxE-iO3FEj6-aUbnBSQ001xzlGh-QYjGUwLWz7_mFn0Xq8zJBtRbNvBXV3gy9vw9l5LgNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸
عادت طلایی برای بالا بردن انرژی و تبدیل شدن به بهترین نسخه خودت
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675900" target="_blank">📅 23:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ساقط شدن پهپاد آمریکایی در الانبار عراق
🔹
منابع عراقی از ساقط شدن یک پهپاد وابسته به آمریکا در استان الانبار عراق خبر دادند؛ پهپادی که گفته می‌شود پس از هدف قرار گرفتن با آتش مستقیم در منطقه «الفیافی» سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/675899" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: ما هیچگاه با آمریکا به تفاهم نمی‌رسیم
🔹
ما نباید هیچگاه با آمریکا در آتش‌بس باشیم، اصلا آتش‌بس با آمریکا معنا ندارد و این به معنای آن نیست که مذاکره نکنیم، و نباید دوگانه جنگ و آتش‌بس را بپذیریم.
🔹
نباید اجازه دهیم آمریکا هرموقع…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/675898" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: نمی‌شود ایرانی‌ها را خرید باید شکستشان داد
ترامپ:
🔹
نمی‌شود آن‌ها را با رشوه خرید. باید آن‌ها را شکست داد و ما داریم حسابی آن‌ها را شکست می‌دهیم. خواهیم دید که نتیجه چه خواهد شد
🔹
همان اتفاقی که در ونزوئلا افتاد، در ایران هم دارد رخ می‌دهد فقط مردم متوجّهش نمی‌شوند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/675897" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZnEchUP1VwfLHlRgMiBXma-6C7Vu9QKv_wDJk4aTv3tQLhB3Ntz5y-2HxMP6mSodQ5Mbhb2S2II6Y8CY2P4iyvEntBArEg1zBacaWC9o48gB53NS_fgtY6jdE7NyDcXw_Iq5OQrxSZpETfaGv3l4b8N6-YU82NVNN2fs9Jz-_vIvejF2vum1v_0uQ36IuWOF7gvLNhoAj_iqf3wUU1rkDmT1zmdJrjRN-URMVbo4ezo2l4s3xqkGRXIPnKhl6SLaaMIGHUlpv-GKuUryhbGlofR1mmd2R3aLv9AcdQfOuuxOEQvfXFNOYkxBV7SxkZiW2ZDtsdhhY5Oei3vXzz8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دینار تو بازار کمه؟
🤯
هرجایی دینار نباشه، توی دینارز هست!
خرید راحت و بی‌دردسر دینار از دینارز برای سفر اربعین.
🏴
@dinarz_app
🔹
نرخ و ثبت سفارش:
https://dinrz.ir/9v6
🔹
تلفن پشتیبانی
۰۲۱۲۸۴۲۸۴۱۲
🔹
پشتیبانی در بله
@dinarz_support</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/675896" target="_blank">📅 23:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای خوک نجس دربارهٔ ایران: مذاکرات دوستانه‌ای در جریان است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/675895" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی سگ زرد با شعارهای تند معترضان علیه او مختل شد
🔹
معترضان او را با عبارت «حامی آزارگران کودکان(پدوفیل‌ها)» خطاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/675894" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حاجی بابایی: تنگه هرمز؛ نمود اقتدار ایران در برابر آمریکای مستاصل  نایب رئیس مجلس:
🔹
این آبراهه به بازدارنده‌ای قدرتمند تبدیل شده؛ هر کشور تحریم‌کننده، با واکنش قاطع ایران مواجه می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/675893" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Zqz2flf1VLx9VTkWmDa1Q_2QsiKFhwhn1ShqGyGq7synaaCA_tlaVjWtDFOgcrr5bz04xIAcUEG7RFDZY4z5nsOYrhBppjmV8oOlRG6-AvotNFeYceh04xS-nJdvQCwJ6xRIprHyjlnksql4b-08wofyOLsJ9oqqVQGLzd8mXcyH5wI5EdXoj3XejHDFbezQ-w7fFsUkx5nRYo9KW3CIvhCDH2VkP3JkkiUuIUy-BnZGpYa72eOrxIK-2iGvZix9APtZyH0fFiV81rh4v9DQHtQ7BSvRWSswDirbfyGf6J6DFHanmLGvukqYjclTJLjr3ZSMPgq5BhggvzudIc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان را بشناسید
🔹
یک سناریو در رابطه با جنگ عربستان و یمن، از سرگیری جنگ زمینی است. دو احتمال در این رابطه وجود دارد. یا عربستان مانند جنگ قبلی مستقیم وارد جنگ زمینی با یمن می شود و یا شروع به تحریک شورشی های داخل یمن کرده و آنها را به سمت جنگ با صنعا سوق می دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233622</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/675892" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684fac0bac.mp4?token=bY9ibzux0bj-TwCWrTtW8tPUoWCbASuXidwEwr3TvybWuZ4_Fqr5ApvAVlf0MI9MXDprdCRPtEYNy7oGFkom43b9--CStYjBDdKU0li435eqBWnylSMxPRz7sB7qtErZaFTpGquBznpbJFeCVEV1i43LA0nqrTwLt29HS90o437OP0hr16nxvHZzlFRKWzBq_nfDaEb7Q9dbFi2CR_GD_BRX0Qk5LQdY3-3xXnuhm308nxKausEyxZBZf4puyfsFTx_EVKvk6hKr7hfRWzCMIlnNIIvwSdG6sXSt5mdSxyQNG7r-8kX93xKgF_EDuhOs0bSCYukN0PqZbDeMmOPuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684fac0bac.mp4?token=bY9ibzux0bj-TwCWrTtW8tPUoWCbASuXidwEwr3TvybWuZ4_Fqr5ApvAVlf0MI9MXDprdCRPtEYNy7oGFkom43b9--CStYjBDdKU0li435eqBWnylSMxPRz7sB7qtErZaFTpGquBznpbJFeCVEV1i43LA0nqrTwLt29HS90o437OP0hr16nxvHZzlFRKWzBq_nfDaEb7Q9dbFi2CR_GD_BRX0Qk5LQdY3-3xXnuhm308nxKausEyxZBZf4puyfsFTx_EVKvk6hKr7hfRWzCMIlnNIIvwSdG6sXSt5mdSxyQNG7r-8kX93xKgF_EDuhOs0bSCYukN0PqZbDeMmOPuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی: تنگه هرمز؛ نمود اقتدار ایران در برابر آمریکای مستاصل
نایب رئیس مجلس:
🔹
این آبراهه به بازدارنده‌ای قدرتمند تبدیل شده؛ هر کشور تحریم‌کننده، با واکنش قاطع ایران مواجه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/675891" target="_blank">📅 23:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ef574baa.mp4?token=o0I4hCpDASgdMvcotmR9cQ5sar4L__hQTBix1Adwvi4KA8djE5D1VzGa5KljuN6P1WWh5YWuvAhUG9WA_EK6a71skuDW5239CUUis-lZ8vl8P-5X0goioEl8qbvz9k-jk7LDXE4oJAgoMk5EXXYCwsuGPt2Tk-nxUC9lNbQJkEQwsOdu_SXK-OBIf7PgP1X6MWurdBLAzJ_-SqMj99GA4pdhZw7x_NdYsQJ2lQS_eVcHOnvuWxT5K9CHXhRQLwBeiAGcDm4GS59UmphS5fBdlZjBPfOsJD4E4z9Kyz8fhVDelIy_Ez5DwT_mDqqzQbPj6_DwMOrSqjJWgMbFS4popQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ef574baa.mp4?token=o0I4hCpDASgdMvcotmR9cQ5sar4L__hQTBix1Adwvi4KA8djE5D1VzGa5KljuN6P1WWh5YWuvAhUG9WA_EK6a71skuDW5239CUUis-lZ8vl8P-5X0goioEl8qbvz9k-jk7LDXE4oJAgoMk5EXXYCwsuGPt2Tk-nxUC9lNbQJkEQwsOdu_SXK-OBIf7PgP1X6MWurdBLAzJ_-SqMj99GA4pdhZw7x_NdYsQJ2lQS_eVcHOnvuWxT5K9CHXhRQLwBeiAGcDm4GS59UmphS5fBdlZjBPfOsJD4E4z9Kyz8fhVDelIy_Ez5DwT_mDqqzQbPj6_DwMOrSqjJWgMbFS4popQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: از پدر و مادرتان بهتر هستم
خوک هار:
🔹
من بیشتر از پدر و مادرتان برای شما کار کرده‌ام، قبول؟ قصد ندارم از پدر و مادرتان انتقاد کنم، اما من نسبت به شما از آن‌ها بهتر بوده‌ام.
🔹
کمی ناراحتم زیرا ممکن است در دو سال و نیم آینده، رئیس‌جمهور متفاوتی داشته باشید؛ شاید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/675890" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرزند ارشد شهید سیدحسن نصرالله: شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔹
ساعت کاری ادارات کردستان روز سه‌شنبه از ۷ تا ۱۱ تعیین شد
🔹
وزیر بهداشت: در تجاوز اخیر آمریکا ۶۰ نفر از هموطنان شهید شدند
🔹
یمن: پهپادهای ما با موفقیت به اهداف خود در عربستان اصابت کردند
🔹
وزیر علوم: آموزش در کشور هنوز مهارتی نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/675889" target="_blank">📅 22:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67b6a03b0.mp4?token=eh0_0gBELJgCE9kc5K36zOO6Bm4dKiV8RoJIkoVvnW50uYpHZoQeyIFkHyDdPqzOHrlD5-whiJhXUAVUkt1ZQ4wzjttnX6C3xOfFmevf0dvD6Zxzyd92ocMZE5jSJz9TfBftAYJXP3avWhLAeOhvZukja0wiSVaULg2dyZS6kxU3slaCF4K4XEmz_aR-qMK4QcdcAAoRwuJ7UgwBqxHXiWYWzOZek8MrhZcIF_598Jb16IOFAuSGt6r9HNxIM6dezAqxa59VFQg-RBQGkrrzDv44lT01b9_JHZN7rxPDBUD29MBcSyvg75HY3-ptOKu0vU57M0InSSH6jFdi1yG9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67b6a03b0.mp4?token=eh0_0gBELJgCE9kc5K36zOO6Bm4dKiV8RoJIkoVvnW50uYpHZoQeyIFkHyDdPqzOHrlD5-whiJhXUAVUkt1ZQ4wzjttnX6C3xOfFmevf0dvD6Zxzyd92ocMZE5jSJz9TfBftAYJXP3avWhLAeOhvZukja0wiSVaULg2dyZS6kxU3slaCF4K4XEmz_aR-qMK4QcdcAAoRwuJ7UgwBqxHXiWYWzOZek8MrhZcIF_598Jb16IOFAuSGt6r9HNxIM6dezAqxa59VFQg-RBQGkrrzDv44lT01b9_JHZN7rxPDBUD29MBcSyvg75HY3-ptOKu0vU57M0InSSH6jFdi1yG9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: ممکن است بقیهٔ دنیا مرا دوست نداشته باشند، اما مهم نیست
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/675888" target="_blank">📅 22:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0841c94803.mp4?token=uL3tX_SVb_G4wha5bn3O7Y-k-7JE3zJKfCqXhgjXtA5zeLJ6rYtzbH3AyAcVpV30qP5DsZpzi6gm1iFYkkEwc3_5kW3JVT9QTS2GjnWmV55HxX7SuREM16tmKaluj3SvroIEowzbl6HSKcUXD5F-X0DV-zvPo-FJOTeoWORP_3ro7aaO3rG3GBZ2H4hJDxLNv94UXo_-2nkK2JRfMCHqYqdaU8kaVmHgb9I8FcAk91gqPJUc-z8E6b3K4n8H531bEY2Vviv6ETHrULJ3kwF1xiE0oPsXX2Kz-CpDjH2XoE9RTHGb3MBgg1CTKUBUo9lvXG32npxcZ4LoLQFaCGYW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0841c94803.mp4?token=uL3tX_SVb_G4wha5bn3O7Y-k-7JE3zJKfCqXhgjXtA5zeLJ6rYtzbH3AyAcVpV30qP5DsZpzi6gm1iFYkkEwc3_5kW3JVT9QTS2GjnWmV55HxX7SuREM16tmKaluj3SvroIEowzbl6HSKcUXD5F-X0DV-zvPo-FJOTeoWORP_3ro7aaO3rG3GBZ2H4hJDxLNv94UXo_-2nkK2JRfMCHqYqdaU8kaVmHgb9I8FcAk91gqPJUc-z8E6b3K4n8H531bEY2Vviv6ETHrULJ3kwF1xiE0oPsXX2Kz-CpDjH2XoE9RTHGb3MBgg1CTKUBUo9lvXG32npxcZ4LoLQFaCGYW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشیدنی آلبالوییِ خنک؛ طعم ناب تابستون در یک لیوان
🍒
😍
مواد لازم:
🔹
۷۰۰ گرم آلبالو
🔹
۲ لیتر آب داغ
🔹
نصف فنجان شکر دانه‌ریز
🔹
۲ برش لیموترش
🔹
کمی کمتر از نصف آب لیموترش
🔹
۴ عدد میخک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/675887" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b575b358.mp4?token=YmCPE5hzTZPoPD01btVAbcIiI5tfMec2b3itOSBAX9w3mnLPkHNvw79cxZ2OuV_EvGl6S7Ez9V2t_pgIeVbcIwoNIQvDbu_hT7T37o-x4NbixF3niqfsapRBOhNSUhHl-rgCgpGAGlMaQYdvEt4Vp75gvBbAqKi4hYBHrQTLUfchqeKY9z2ouiCWEclmM6tbxm34gJb_IbyDlFDDgDevjItLlN6XFVP0dyZozVyrs0q96Uj_Y9JCAr6dtGkvy2Mhz_nWZDXENUM4Me7R_xj0gLfp5O25xRdGoniUZb_ZEV_c7tPAafwLMsznjbpMnFOKj8tpzDFhxPDPnQRTBUznNorc-yXBq1Jb7tzx6FjrhsE4SEinwqXfJStvGRjTkRceeqeXND28BpEryGux2_y4x3_W1owob3sTVIhicRPuC0TRw2T6L3l7ShAdCPVHKl_eM1W5WvAlZzXMJ5fHa_DR2asp6CxRmwnTay0cevbZPlcinMp8gDRgmFvPL5xHSfTQUK4f_UEdRj5T1iifhmXdFtBRrDksVlgurcU-wwma4kuq17Y2ejNH9OkWyCzjzDzUplI6LSSwMi9hS7sfeGz2nx0LBfpKnIn8fEYemG-ONTh-KxXEG-IVuMeiDsd6yOMJVm-eTO7Xkm4nMIGYxogaMkpjK1apSPaBCT100x25Tqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b575b358.mp4?token=YmCPE5hzTZPoPD01btVAbcIiI5tfMec2b3itOSBAX9w3mnLPkHNvw79cxZ2OuV_EvGl6S7Ez9V2t_pgIeVbcIwoNIQvDbu_hT7T37o-x4NbixF3niqfsapRBOhNSUhHl-rgCgpGAGlMaQYdvEt4Vp75gvBbAqKi4hYBHrQTLUfchqeKY9z2ouiCWEclmM6tbxm34gJb_IbyDlFDDgDevjItLlN6XFVP0dyZozVyrs0q96Uj_Y9JCAr6dtGkvy2Mhz_nWZDXENUM4Me7R_xj0gLfp5O25xRdGoniUZb_ZEV_c7tPAafwLMsznjbpMnFOKj8tpzDFhxPDPnQRTBUznNorc-yXBq1Jb7tzx6FjrhsE4SEinwqXfJStvGRjTkRceeqeXND28BpEryGux2_y4x3_W1owob3sTVIhicRPuC0TRw2T6L3l7ShAdCPVHKl_eM1W5WvAlZzXMJ5fHa_DR2asp6CxRmwnTay0cevbZPlcinMp8gDRgmFvPL5xHSfTQUK4f_UEdRj5T1iifhmXdFtBRrDksVlgurcU-wwma4kuq17Y2ejNH9OkWyCzjzDzUplI6LSSwMi9hS7sfeGz2nx0LBfpKnIn8fEYemG-ONTh-KxXEG-IVuMeiDsd6yOMJVm-eTO7Xkm4nMIGYxogaMkpjK1apSPaBCT100x25Tqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: از پوتین می‌پرسم آیا ماهواره‌های روسیه به ایران کمک می‌کنند
؟
🔹
ترامپ، دوشنبه ۲۷ ژوئیه در پاسخ به سوال خبرنگاران درباره ادعای کمک روسیه به ایران، گفت که شخصاً این موضوع را با پوتین، مطرح خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/675886" target="_blank">📅 22:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b898eeb1cf.mp4?token=ME_G3IfYA7wa6W4qtrXW4RVdGS3_TSvj9_UIhLApGbIvOJskvc70pj6Y74uKMl8eCD2i9x3ShVudNjjDxlS9IBnppKwDEq7Hy4U6yvmXWWFf9qYFeXgoCGZgtlmOzA4hg51DTSAQEQ7J1k6tEvaMCyorX_bDO2UKU22eCDg7LSv_jDvnSKMhmH2GrNJ_dwW-q0Ps-7BSrp4fwWcWxzecVnE5vCmO0xxZRzNa1nRqmfEigbXI_Gjw78og-UzrCIi-hkpL32lpZN2X3HwVuetF9FvDM7eHRygkwdN-627-kFEKrxcmeTBltxKjvd0qkkiax13yWTE1E2meKIEgj_RFmQ_wf8bM6wKJf2-TrmgSkvmoCy0evFBwZr0nzCm1x3-yGjbv4kbf8wmzRJoHjVL9zb2kMt72XdsiA5491NEMSSJY0Ws2BlUtCn6SG5PVJP2n-HG_JFpws4yZP3ZSVpq53XckfiUoHrE4AVAX5E_c_-T-hz1uLWuqeJn8a3q72prZM78pJPc7EEUVeGc9eX_rKiw9jEXPJfzSWusb94vUyRaFQdUpD4-64sWhJQXo1mnhy_3pjNNyub7L1UPwVqjNVwhICDoPQpDqy-4TCqH7VhHDpcy98YdXG4uNeX1mWLqSzuzcotF2-hYNkuWwyleBY-wvv3dPUTXCQnm9d4ms5AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b898eeb1cf.mp4?token=ME_G3IfYA7wa6W4qtrXW4RVdGS3_TSvj9_UIhLApGbIvOJskvc70pj6Y74uKMl8eCD2i9x3ShVudNjjDxlS9IBnppKwDEq7Hy4U6yvmXWWFf9qYFeXgoCGZgtlmOzA4hg51DTSAQEQ7J1k6tEvaMCyorX_bDO2UKU22eCDg7LSv_jDvnSKMhmH2GrNJ_dwW-q0Ps-7BSrp4fwWcWxzecVnE5vCmO0xxZRzNa1nRqmfEigbXI_Gjw78og-UzrCIi-hkpL32lpZN2X3HwVuetF9FvDM7eHRygkwdN-627-kFEKrxcmeTBltxKjvd0qkkiax13yWTE1E2meKIEgj_RFmQ_wf8bM6wKJf2-TrmgSkvmoCy0evFBwZr0nzCm1x3-yGjbv4kbf8wmzRJoHjVL9zb2kMt72XdsiA5491NEMSSJY0Ws2BlUtCn6SG5PVJP2n-HG_JFpws4yZP3ZSVpq53XckfiUoHrE4AVAX5E_c_-T-hz1uLWuqeJn8a3q72prZM78pJPc7EEUVeGc9eX_rKiw9jEXPJfzSWusb94vUyRaFQdUpD4-64sWhJQXo1mnhy_3pjNNyub7L1UPwVqjNVwhICDoPQpDqy-4TCqH7VhHDpcy98YdXG4uNeX1mWLqSzuzcotF2-hYNkuWwyleBY-wvv3dPUTXCQnm9d4ms5AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنجره متفاوتی به حضور رهبر شهید ایران در چادر عشایر اردبیل؛ مردادماه سال ۱۳۷۹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/675885" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اقدام به محاصره به منزله توسعه جنگ است
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی‌های تجاری و نفتکش ایران در آب‌های ساحلی و سرزمینی کشور ما نموده است.
🔹
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می‌گردد و همان‌طور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی‌گذارند و با آن برخورد خواهند نمود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/675884" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675883">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10282ab1b3.mp4?token=aVLanIHBDUSNCsG7vzwoxyzdmQUWGvlKnC3QorXpg5MiaNzRYyMY4fK2F9u_5zV9kwqWiM3hQoElK2h_vQ-G7dUigLJhO64kaHgyxKPrqbuaiEHiBcBFuDPBePmqLnnTox7yzpLqikxgeJhes7Tqsvz2iMK0Dx3kWChrGKWNo9uvb09u9iRcCl_g620sRraqIQuBH7VpG2fx40L8fPcT85MDh7wg33Q6MyjwTuSzi3ZQORF_4XdTjBfeNCdjJd1-WNQJ9AksrFqGQxgkTtzPOqZXmBmtTAngWo4SQPQuTG9yY7T2og88gtUzldtMGwvjZXdTuvcVE54ezBk-ZHjzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10282ab1b3.mp4?token=aVLanIHBDUSNCsG7vzwoxyzdmQUWGvlKnC3QorXpg5MiaNzRYyMY4fK2F9u_5zV9kwqWiM3hQoElK2h_vQ-G7dUigLJhO64kaHgyxKPrqbuaiEHiBcBFuDPBePmqLnnTox7yzpLqikxgeJhes7Tqsvz2iMK0Dx3kWChrGKWNo9uvb09u9iRcCl_g620sRraqIQuBH7VpG2fx40L8fPcT85MDh7wg33Q6MyjwTuSzi3ZQORF_4XdTjBfeNCdjJd1-WNQJ9AksrFqGQxgkTtzPOqZXmBmtTAngWo4SQPQuTG9yY7T2og88gtUzldtMGwvjZXdTuvcVE54ezBk-ZHjzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: نتانیاهو با فروش F-35 به ترکیه مخالف است
🔹
خوک هار: «هیچ‌کس به من نمی‌گوید چه چیزی باید بفروشیم یا نه.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/675883" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675882">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c645f1ae8b.mp4?token=mhAL7BHbxWEeHTLVTQRiTiYLWommJrqXO8ojD4Zaxoso8xgJmvso1dM6M0TLWZ9LFWzg8srF4-6qPpwmhDPSXbtF6-_zosSKIirRGoq67e998C5PoabREgrr5c4SzXtPPVpRCkPS0msJ9elAxDL0UgwNZ-VyGCyedt1J_ZUtgOEIc88GJD_BN1-sZWz05rrZjdJj1L81NwLjkevHVcO4PHkLzpakhp24gw2zVbW8J4O15JYEPO-mY70HY5NHVNx3qx07WprHkYN9no8zKX4r7IR1MuhIv8_RS31aBgshgFBelFxmIIRQjoBbdhnMJs-a11EaZ1Febve6EiBfVja1YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c645f1ae8b.mp4?token=mhAL7BHbxWEeHTLVTQRiTiYLWommJrqXO8ojD4Zaxoso8xgJmvso1dM6M0TLWZ9LFWzg8srF4-6qPpwmhDPSXbtF6-_zosSKIirRGoq67e998C5PoabREgrr5c4SzXtPPVpRCkPS0msJ9elAxDL0UgwNZ-VyGCyedt1J_ZUtgOEIc88GJD_BN1-sZWz05rrZjdJj1L81NwLjkevHVcO4PHkLzpakhp24gw2zVbW8J4O15JYEPO-mY70HY5NHVNx3qx07WprHkYN9no8zKX4r7IR1MuhIv8_RS31aBgshgFBelFxmIIRQjoBbdhnMJs-a11EaZ1Febve6EiBfVja1YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادات اشتباه رانندگی بیش از قطعات بی‌کیفیت، عامل کاهش عمر موتور و خرابی‌های سنگین خودرو هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/675882" target="_blank">📅 22:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675881">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آتش‌سوزی در کلانتری ورامین تکذیب شد.
🔹
نخست‌وزیر عراق: اجازه حمله از عراق به کشورهای همسایه را نمی‌دهیم.
🔹
رهبر اپوزیسیون رژیم صهیونیست: عربستان با اسرائیل سازش هم بکند، نباید هسته‌ای شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/675881" target="_blank">📅 22:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1365c9a34.mp4?token=iOUoYNIR4RwO7FeSD8_K7Zf2lfpLLTPlVAI4dEwn0mii0Tpp1ULJ-817laYesLo-LAXpLOMdVFdDJfxZOV6DKngxe6hmia0pOJVBZZfiqbs9e7wGX9GHLHjzYumRTwyXHZr4Ebn9KVRrs3Qm9Kkcrnh8fuG3gkPQnX1wbGTtAYmQk9OUuJBRNaQMDYWZEhuJaLeWeqN-v0zZGlbOLYqOtMEDuKsrt8yPB1Ko1dULmncRxH93DH9s2_a4xoJiSfXv1GKvka6DMPYpes-Mn5z-_34FPPjGd3N7nsZc0xu8eidUDQWf4tAp-ZT7TbwRJhTNdsseh1j1s9rjfvyqKRzsG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1365c9a34.mp4?token=iOUoYNIR4RwO7FeSD8_K7Zf2lfpLLTPlVAI4dEwn0mii0Tpp1ULJ-817laYesLo-LAXpLOMdVFdDJfxZOV6DKngxe6hmia0pOJVBZZfiqbs9e7wGX9GHLHjzYumRTwyXHZr4Ebn9KVRrs3Qm9Kkcrnh8fuG3gkPQnX1wbGTtAYmQk9OUuJBRNaQMDYWZEhuJaLeWeqN-v0zZGlbOLYqOtMEDuKsrt8yPB1Ko1dULmncRxH93DH9s2_a4xoJiSfXv1GKvka6DMPYpes-Mn5z-_34FPPjGd3N7nsZc0xu8eidUDQWf4tAp-ZT7TbwRJhTNdsseh1j1s9rjfvyqKRzsG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: رفاقت ۷۰ ساله را از دست داده‌ام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/675880" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هشدار هوانوردی آمریکا در منطقه بحرین
🔹
اداره هوانوردی آمریکا (FAA) به دلیل افزایش تنش‌های نظامی، به خلبانان هشدار داد هنگام پرواز در حریم هوایی بحرین و آب‌های بین‌المللی تا ۲۷ اکتبر با احتیاط کامل عمل کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/675879" target="_blank">📅 22:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvns6WiPZf5RONSYbxdo3l_ecFA31z-W5LTV1O7UKP0tDk-neoefNcAjwr14J0fG2hySW242ExU5_g-oi4o3iTD1vxUrqeVtKfdGxHfY_0Ufdn4Dq-pAOfjeY_ryFiJ72BTzA92pxZhposyWcOjVSuOH6BCnX6avB1F_zwbSghyspXyy74BhlayqrkHOBNdX870Gv2WvOIiVRzXeDopJvZxat8XiXSqxry2XpK9966rPPRJq-i_D3YgjcsqiT3xmVlxSqa2CIe_jFmGkm-rmJVJrFGZEJQjA_lMgUe0wJE9Ci7yUjvlXvFCMV3xdJxhNkh1bMGsyPHQmEI4tPr-R1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده شده از رهبر معظم انقلاب اسلامی آیت‌الله سیدمجتبی خامنه‌ای در نماز جمعه نصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/675878" target="_blank">📅 22:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c4ea3de2.mp4?token=QtMrvaDauECrzwlGrfnNpg0hnnkd0xm2F3o3HedJHCAgC10kf4LZMThzqQ_pIPQHBUwvnweZxq4qIfbIEKqvUm-qrHENGgsfprsfwCJ-XB-rAwZUV1K5dP763-v3dP7q5C35UyFAi-BCAQnWLStpWTnQGUdjd2YZ42hZ7NfIaJcdzQ3V03vxVr8iQM5hwjjfMPZsg-AbCera_Xd91abL8nQbsAdeu7tKrmPBi4swNmeNp15517SvkbUdo_Vwo8MkhgBmwsfZmboDfV0kqbEzzgFvVGX5bRYRnYBduXJRhCxxezWXczfXEsUFzlbPrfl1HLM6TzdSdzD2ujwPe2Bm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c4ea3de2.mp4?token=QtMrvaDauECrzwlGrfnNpg0hnnkd0xm2F3o3HedJHCAgC10kf4LZMThzqQ_pIPQHBUwvnweZxq4qIfbIEKqvUm-qrHENGgsfprsfwCJ-XB-rAwZUV1K5dP763-v3dP7q5C35UyFAi-BCAQnWLStpWTnQGUdjd2YZ42hZ7NfIaJcdzQ3V03vxVr8iQM5hwjjfMPZsg-AbCera_Xd91abL8nQbsAdeu7tKrmPBi4swNmeNp15517SvkbUdo_Vwo8MkhgBmwsfZmboDfV0kqbEzzgFvVGX5bRYRnYBduXJRhCxxezWXczfXEsUFzlbPrfl1HLM6TzdSdzD2ujwPe2Bm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلچینی از هوشمندانه‌ترین ضربات ایستگاهی دنیای فوتبال
⚽️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/675877" target="_blank">📅 22:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک پنجم مصرف روزانه سوخت کشور قاچاق می‌شود/ عضو کمیسیون انرژی: روزانه ۲۰ میلیون لیتر سوخت از کشور قاچاق می‌شود
غلامرضا دهقان ناصرآبادی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
روزانه ۲۰ میلیون لیتر سوخت از کشور قاچاق می‌شود که معادل یک پنجم مصرف روزانه سوخت کشور است و بخش عمده این قاچاق مربوط به بنزین می‌باشد.
🔹
اگر قرار باشد سوخت به‌ صورت دو یا سه نرخی عرضه شود، دولت باید زیرساخت انتقال سهمیه سوخت به کارت بانکی افراد را فراهم کند.
🔹
در غیر این صورت دولت باید سوخت را با قیمت فوب خلیج‌فارس در اختیار مصرف‌کنندگان قرار دهد تا از قاچاق گسترده سوخت جلوگیری شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/675876" target="_blank">📅 21:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr9NKv8DgUtZggHVoLTTmfTc65uZ-he34-JtjdemBrMn--EI-re5OulwXwrQISj0qKJ6m2umRunLawRWkhgWdO9yb_jQ7Tx1SNzDPK_ou7jvN5pm1sc9WTIwBfqxYfDvW6sJlb0D8yaj1K75CJ4PadEOesL2zwhCB36oHWqWRc36GNBAFM3SHFT9-jiveSq_rAZXOIh-hefE9eMb81Ev5fu7IpyGuT6P4sKTSw6GS9e3GcrZwfAqai1FTXB-bFQMlLWuQ2lEBjhi4ZnOW5kjQ5zEsEwvASh6qaFK9u3dZNtS1nk5qHgHKgnH1AYjy8IER0tzopIAlHsUhm_fURb5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت پس اخبار منتشر شده درباره مذاکرات مجددا کاهش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/675875" target="_blank">📅 21:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
آشفتگی در آسمان اروپا
🔹
نقص فنی گسترده در سازمان مدیریت ترافیک هوایی اروپا (Eurocontrol) موجب تأخیرهای طولانی‌مدت و به‌هم‌ریختگی پروازها در سراسر حریم هوایی اروپا شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/675874" target="_blank">📅 21:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ddc468dc0.mp4?token=SB7kc_A7ulChzvqINa194SPizY0ywUoDW8St2gHt61XjMYSqfH6Zyub5Uxf7LRAELhM5AnfhlDUNVM6xNHnDc6y1vXX1vy4xNbgZNNiKaVwqPb_gcvrwIdY65H-b1pPipxZA3GAnW-ebpa4YR91_94WXhvcjHe2l3E5VuxDHt5KW7qHnPJDekPtFBvSsz3YeKq6O7q2JX5D9pqerXGfLdQM2DqlKf7YE9X9MmSTndfa5vQijKIHUV-mCJRbuwZs9Zt92m7lQ4Qal8n0TdjaOsZb3zyF3AqMwP_Tf0chNZWEUa2rjUE0OGUB-uXCTCvuPxCW_IYgtCxfAMrQWxlusX4nDUI-L5UGiIIqJaeSQNbU7Tqw5mnO_8kja3xCPV1k-_sEC9MDNpEZgygkVgRaYKrl72hN68Vl168tE9w69Cyp-hxh5FJEqLMgqoSsGxpvugwbMg3zMW7KqMv48hfSDyTJuzhXcmZPRct4Jhv-K1aEcaqGTa5sktZehEnpMClCDJh8210RbjdZm-p1RkrMe1qBjetj8q0jGLyJ_0RuSOLih4IV5fw3jZnXkgXIS6C_rY4X5_80zvlTgHZiF51jUxE-ml6OpxYiuoPXQsr_eKXWTAWUiTFL5l-Z7GyGt5CqlWiz4cRDjDVRc88YVaWmmXhrwc6rO-Yccr6dTvpQ0aZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ddc468dc0.mp4?token=SB7kc_A7ulChzvqINa194SPizY0ywUoDW8St2gHt61XjMYSqfH6Zyub5Uxf7LRAELhM5AnfhlDUNVM6xNHnDc6y1vXX1vy4xNbgZNNiKaVwqPb_gcvrwIdY65H-b1pPipxZA3GAnW-ebpa4YR91_94WXhvcjHe2l3E5VuxDHt5KW7qHnPJDekPtFBvSsz3YeKq6O7q2JX5D9pqerXGfLdQM2DqlKf7YE9X9MmSTndfa5vQijKIHUV-mCJRbuwZs9Zt92m7lQ4Qal8n0TdjaOsZb3zyF3AqMwP_Tf0chNZWEUa2rjUE0OGUB-uXCTCvuPxCW_IYgtCxfAMrQWxlusX4nDUI-L5UGiIIqJaeSQNbU7Tqw5mnO_8kja3xCPV1k-_sEC9MDNpEZgygkVgRaYKrl72hN68Vl168tE9w69Cyp-hxh5FJEqLMgqoSsGxpvugwbMg3zMW7KqMv48hfSDyTJuzhXcmZPRct4Jhv-K1aEcaqGTa5sktZehEnpMClCDJh8210RbjdZm-p1RkrMe1qBjetj8q0jGLyJ_0RuSOLih4IV5fw3jZnXkgXIS6C_rY4X5_80zvlTgHZiF51jUxE-ml6OpxYiuoPXQsr_eKXWTAWUiTFL5l-Z7GyGt5CqlWiz4cRDjDVRc88YVaWmmXhrwc6rO-Yccr6dTvpQ0aZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه جنگی یمن فیلمی مرتبط با پهپاد مسلح «بیرقدار آکنجی» ترکیه‌ای متعلق به عربستان و لحظه انهدام آن را منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/675873" target="_blank">📅 21:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراقچی: سکوت و بی‌تفاوتی جهانی، جنایت را به الگویی برای تکرار تبدیل می‌کند.
🔹
یمن: اقتصاد عربستان به دلیل تجاوزگری‌ها دچار فرسایش شده است.
🔹
مسکو: اقدامات تروریستی کی‌یف ابعاد بین‌المللی گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/675872" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S924HKW5lhBIlHuaBtjnPx49YAoK0HcmBpnOlZh4xk08TUXOcVQq3YYHkdkN1CkRp9O9iIaPUDLpCgOShjmIacaWjCnFl_AwCHlvmzGSEwDWFL7IQ_Q15KA0DX12-lQ7WdzfvsokL1nnSOxW0Mze5P863siCLR8CNxXYRJb1wzvoCaW8ucyREC-RAzf2uCEUcEkE6dybc3JxPYaxxd93wHRPn4NpKHMBUzEEAjbzLVdOo2F3kmGW7ZXRFHxO0EC9Gw9kJt3dCyKKs19GPF62QH_h38AVOlO0RhIMVa0jPYDGNAqixCEgITeQEY43gSCnjx2qmmsV_uCCTwnLcvPXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoR1kNVdqliy0Wcw8XxCVgz5TYQ9KVtV3yd_0Gs1K7pbUOFq55yV0YbciXA-fJ3FSRLNCIq_EgLw5KSWMZx6OQpNcYCYElKpHrRLI0abF8ckEqc2vOQnLj576XTOj-jThIqrerMX07YrlOugEXnAizp35UVIwTA6U9c1WWiJpYt98YwOCYF06jvrkhv34nGmnZNHSXXyoBFBCpaysoVHx5xjNsTPqiRwvcz3zRVcjLkiq10R3w33jTg6fW3ndFXjZvIy5H_0lir6H7SC3MvMcK6xedXwIoVROlA5ir5XWRo74i1zNcT9c_dy1PPM4cAc8BxZCaulkZUSFJe6tJeofw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران؛ دهمین کشور قدرتمند در حوزه سایبری!
🔸
در این شاخص، ۸ مولفه اصلی از جمله نظارت و پایش گروه‌های داخلی، کنترل محیط اطلاعاتی، توسعه رقابت‌پذیری تجاری و ... سنجیده می‌شود که در بعضی از آن‌ها، ایران رتبه‌های بالاتری را کسب کرده است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/675870" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675868">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e84c6426.mp4?token=aAfnCNTvZXkg-aM1jCPh3kVNYomxtjQ8b9GnyT3TYV75Zy4dQ3KhSHRqKaQLogLieZ2tbro70NgjBCA5KzsfK3VpEjRqxd_w5V55DilJ2_ZQHFKxhVm9H5bjVQTw837X4APokN9xw1I63uVHgfgEKOuRPuUW7HiKTYYvNiCedQS6E1ieixu0SAcRbz5akIcZJOMHxylj-6I3o_6ipEvEIXe0OqVBbsHwEpuNkcTCqTXDPoFh9pU0M8GcLNrKc3XszVtw2eIywGXBJePcspk0XDmfge2-GtIjlDrTpTRCpq544atx9-1Y87_tZvBj2DE9Yrd9Br8kyZDm9J_CminTwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e84c6426.mp4?token=aAfnCNTvZXkg-aM1jCPh3kVNYomxtjQ8b9GnyT3TYV75Zy4dQ3KhSHRqKaQLogLieZ2tbro70NgjBCA5KzsfK3VpEjRqxd_w5V55DilJ2_ZQHFKxhVm9H5bjVQTw837X4APokN9xw1I63uVHgfgEKOuRPuUW7HiKTYYvNiCedQS6E1ieixu0SAcRbz5akIcZJOMHxylj-6I3o_6ipEvEIXe0OqVBbsHwEpuNkcTCqTXDPoFh9pU0M8GcLNrKc3XszVtw2eIywGXBJePcspk0XDmfge2-GtIjlDrTpTRCpq544atx9-1Y87_tZvBj2DE9Yrd9Br8kyZDm9J_CminTwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقر تروریست‌های تجزیه‌طلب در اربیل همچنان در آتش می‌سوزد
🔹
ظهر امروز پایگاه‌ تجزیه‌طلبان مستقر در کردستان عراق مورد هدف پهپادهای انتحاری قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/675868" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675867">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
شلیک دوباره به کنسولگری آمریکا در تورنتو
🔹
کنسولگری آمریکا در مرکز تورنتو بامداد دوشنبه برای دومین بار در سال جاری هدف تیراندازی قرار گرفت.
🔹
پلیس اعلام کرد مأمور مستقر در محل حوالی ساعت ۴:۴۵ صبح صدای چند گلوله را شنیده و سپس یک خودروی سفیدرنگِ بدون پلاک را دیده که با سرعت از صحنه گریخته است؛ تعقیب این خودرو ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/675867" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675866">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: در سیستم ما مماشات با مسئولین خطاکار خیلی بالاست و بیشتر رفاقت‌پروری وجود دارد/ گاهی بعضی افراد خاطی در سیستم ارتقا هم پیدا می‌کنند و جایگاه بالاتری می‌گیرند
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/675866" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675865">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
دیدار با ۱۴ معصوم در تجربه‌ای باورنکردنی؛ ۳ روز فرصت برای پرسیدن هر سؤال
🔹
00:16:50 خونریزی در مغز با تزریق آمپول اشتباه
🔹
00:29:40 آرامشی تکرار نشدنی با حضور سیزده مرد و یک بانو
🔹
00:33:10 فرصت ۳ روزه برای پاسخ گرفتن از هر پرسشی
🔹
00:38:30 ریزش لجن از قلب نزدیک‌ترین دوست به خاطر حسادت و توهین به اهل بیت
🔹
00:42:20 نگاه آزاردهنده به نامحرم، لذت بهشت را از بین برد
🔹
01:00:00 چرخ ستارگانی به تعداد فرزندان، روی سر هر انسان
🔹
01:07:10 روییدن میوه در گلخانه پسر با دعای پدر در برزخ
🔹
قسمت چهاردهم (پرسش)، فصل پنجم
🔹
#تجربه‌گر
: حسین صاحبی بزاز
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/675865" target="_blank">📅 21:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675864">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9kRFyMV10WnLdtBmwcGbEhZmHOMcOr4TIWtDliw1nh60lvqC0JrTNBPGxJMz8K_hSBbwhu6RNiG9DiEowSPvnYQI1ooTVsmyxUu_BAWpxngJE0ysDskFgwxrjX19ltlcmGyc8OADDoTbqnX-5qHlOaTxTpZ9EdKzm4ZcDDTcwcLdSM9Z3eAbKO0WhrFijqem8HyLVQMEiMReLEqPB5N7YaLZIQzyV9VaNS-VAeKob16XqrbhkzKvPcEncwAaFyGgcrobyR39oVSzj8S6IOnudqh2jBSHY_LsuiBbnBAJsQ9Bb3ltrBjJdk2-cOI3ujuxPHNZO2AoDS-twxHRhbN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بیمه شخص ثالث چه خسارت‌هایی رو پوشش می‌ده؟
خسارت‌های
بیمه شخص ثالث
به دو دسته تقسیم می‌شن:
🔸
خسارت مالی
: آسیب به اموال دیگران، مثل خودرو یا موتور
🔸
خسارت جانی
: هزینه‌های درمان، نقص عضو یا فوت
✅
بیمه‌بازار در دونستن تفاوت این دو به شما کمک می‌کنه تا موقع خرید، فقط به
قیمت توجه نکنید
و
پوشش مناسب‌تری
انتخاب کنید.
👈
مقایسه و خرید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/675864" target="_blank">📅 21:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای باکو: ایران تلویزیون دولتی آذربایجان را به فهرست «رسانه‌های متخاصم» اضافه کرد
آناتولی:
🔹
آژانس توسعه رسانه‌های آذربایجان روز دوشنبه اعلام کرد که ایران، کانال تلویزیونی دولتی AzTV این کشور را در فهرست «سازمان‌های رسانه‌ای متخاصم» خود قرار داده است.
🔹
این آژانس نگرانی خود را از این اقدام ادعایی ابراز می‌کند و می‌گوید فعالیت‌های برخی از رسانه‌های ایرانی در آذربایجان طبق «اصل عمل متقابل» «غیرقانونی» تلقی می‌شود.
🔹
تهران هنوز قرار گرفتن AzTV در این فهرست را تأیید نکرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/675862" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR6R1zBbsUSOF1ptUBMNfXBHzHgkRZZ0jZ1gsAhkNpMGNih-crb-lLFnDsqNWoQ2hUcpTsmIXtRiL2qDConqYCN2eUV1uWYPuMegsA59n0JU84-oKE-6-V_mKwSshv29SlAEWHC_JhGmQOlwyMi0yxsOKtUyURGijY0b45w4FLR0PLVEWrtiRTy5QA_9HfO4pIRiPzzYeVoGtOWj38Bkb732jPqoO7RLpZ9z8iQqNz_5yz7zLfwMhFEWqfQ7zA3ccASFwrDeCFCeUyJWSbMAOSpAG2xlRe5x1gsVaWN3ELYWb2hrdPYmPPkOr6HZfdirLGVAFRJeWe0rVv9qckjh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این علامت‌های روی لباس رو ندونی، ممکنه با یک شست‌وشو لباست رو خراب کنی
👕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/675860" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
