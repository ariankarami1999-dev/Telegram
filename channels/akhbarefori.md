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
<img src="https://cdn4.telesco.pe/file/OaEZLafXy-CIBO_p8ktSRZ6anGhBcNNoXmZeA9oefFnC02loEluXwo2Q_0FQ2RJDOR9U60pGL4IuUSuG7ABH8kaGg6kUj63O0xVHXz0Zc2bLcMtGSDu8AnUMUOCfuNZHmmYGDaDraEqnr7Wc6yRJf8ws2WcUy1_Dec_xiPfZtBfwnrqHNvXuCzm89D6gqICNoDzSrLeLq1fqosAbLDwPLSbtbBr6SlAsQe8f6D16GOxCOIWQCjtEH36aiPHrTVljIeZRenkmrcgnk9srSTW0THMB5Qtr9y-MFtt7xkwog1ZKTjm1oRowYXgV1tlpbtxQRMPw4NFC91LWOlwXfChlhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 16:53:59</div>
<hr>

<div class="tg-post" id="msg-682562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcHZ-NnVc3szA0uDR-fXLT-spPPnpMWQ5MDDcVpCliEedL4BtVtDO_INFTJnuwukdkHQPcSL60rfvyugPHrQNGAsxJVXid_ohmIPofDe72CrefcUV1qQVwUDwsYrE7MN4goRJXQ8GYQFmwjy1ZL5QxQd4V8mH6TfRldENhPLlvMOQRvgK1kL4J-BHKJqGMif7JSsZr_ef9Jx4pTPQPWpr475uk-Ahhhd30y0zfttICqiefO3AS3_1GC3HTKF8Fu-mcUOy4We8kpx8_-cjh5LXOpQMVwvhj_P4ruH58kYCIl6t0hwdkkf2-nzXvyxivFB-nRWO-xs25hboT8HumH6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلمرو جدید ایران
🔹
دونالد ترامپ در ادامه مواضع جنجالی اخیر خود، در پستی نوشت تنگه هرمز؛ قلمرو جدید آمریکا. ادعایی که بیش از هر چیز، بیانگر رویکرد مداخله‌جویانه و نگاه توسعه‌طلبانه او به مناطق راهبردی جهان است. چنین تفکری، در صورت تبدیل‌شدن به سیاست عملی،…</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/682562" target="_blank">📅 16:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کارگروه ویژۀ بنزین در مجلس تشکیل شد.
🔹
پرداخت حقوق مردادماه بازنشستگان تامین اجتماعی از ظهر فردا آغاز می‌شود.
🔹
قالیباف در دیدار با همتای عراقی: امریکا عامل بروز ناامنی در منطقه و اخلال در مسیر عادی تجارت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/682561" target="_blank">📅 16:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade319937f.mp4?token=uLcAWtRK_EN9yS_tksFFP0G8G8oix9cQRTBhla6ksRII9fWiOo2eAeUHPkvhvaJDbZVUU24lT3lqYcHb-zHL6PGEBzsbhFZGlOCjMxvTO4koiiSOmIwm2WWH4EB3kNyDAWB26tCUoAy6LtQpkE3Pxb6mq6pp9a-_1zxitKEGNeprZoMO7yM_WZRlPotJNnexTBf9zNxZssI2Sdzo8T21fCpDkh3zoQb_JLKUUiGqfKVkEGrP3NK3Dvwpv4XiCpDz5FYYMuOBF4xo7yZGhvzD3-c1UUTnVUmpR-ezxqwVDLDPgIHYIjNE-zgoWWTId2czKrKh7Sd6TAxKFgBwRXGVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade319937f.mp4?token=uLcAWtRK_EN9yS_tksFFP0G8G8oix9cQRTBhla6ksRII9fWiOo2eAeUHPkvhvaJDbZVUU24lT3lqYcHb-zHL6PGEBzsbhFZGlOCjMxvTO4koiiSOmIwm2WWH4EB3kNyDAWB26tCUoAy6LtQpkE3Pxb6mq6pp9a-_1zxitKEGNeprZoMO7yM_WZRlPotJNnexTBf9zNxZssI2Sdzo8T21fCpDkh3zoQb_JLKUUiGqfKVkEGrP3NK3Dvwpv4XiCpDz5FYYMuOBF4xo7yZGhvzD3-c1UUTnVUmpR-ezxqwVDLDPgIHYIjNE-zgoWWTId2czKrKh7Sd6TAxKFgBwRXGVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از کوه دماوند و کوهنوردها که باتوم را از ترس صاعقه در کوه رها کرده‌اند!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/682560" target="_blank">📅 16:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-9gMqYwH_SepfTthhmX_O74JfRuG-pUfH6R2aRVPMkYqfm9m7mNbVcRfnvnoIyHeetuXFEeMzL8ZxbHr4ZLyLrmQ5tYA1g9BVvxeXyFlFMlK8l-_DhGsYbLPyuWZzSe2xQY6Xpbqwf8M-ke0Nm74NVBjho20lMRRc9ejRI3XcMiJMvZ4PeiCGzwjPyVibPjJ9ijG0ms2uzfhRK-2noQo8jvnkVLD-ljVh_5Pt4hJ2_cnWj2QDXIQDcQ6GroUftY9g_kDWKhrorFkmt1LGNNX3bCepT5z62HX-msPgkMdXFvH6nwB4sFvTfiJpU1dRpCAoq7Ru8K5k1fZmwalbceJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالگرد عروج عارف بزرگ شیعه؛ آیت‌الله سیدعلی قاضی طباطبایی(ره)
🔹
امروز ۶ ربیع الاول سالروز وفات فقیه عارف میرزا علی آقا قاضی طباطبایی تبریزی است، او از برجسته‌ترین استادان اخلاق و عرفان نجف بود. همچنین در فقه، اصول، حدیث و تفسیر مهارت داشت، به تربیت شاگردان و آموزش سیر و سلوک می‌پرداخت و بزرگانی چون علامه طباطبایی در مکتب او پرورش یافتند.
🔹
آیت‌الله قاضی در ۶ ربیع‌الاول ۱۳۶۶ قمری دار فانی را وداع گفت و در وادی‌السلام نجف، در نزدیکی مقام حضرت ولی‌عصر(عج)، به خاک سپرده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/682558" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDU_L5TOXyyW1a5V704cmCBBQNsRlUAmZHTe1J-RhrOpA2rfx-53ssumTybJYcrzFds7kw5XX3wRaZpi51GL_kfLz5mpM5cbdmQu7nnDPLAcdcR62bfBKmMHAEZQY5JizLomVb8I45t7InU_vPU7vr9LQp22Y1QRpEX_zQYvcJnaPRAjlb8aDSkl_hHd_SLXOW2BQ6zYuKrFXRcHfWpXv3XMFC9suKjOTiL2UAYKsqUlT5eMfu7KvXFThtQ39Kwj-gKKWePJoNvN0Nqee0xxKtMkHzFJYa5dDoE84-FMl6_iHAf0nKEJy1nAjnjdyp3gVBMDcMu9n115HCbMobLcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/682557" target="_blank">📅 16:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1284b39cc0.mp4?token=Oe-Dvvhip7WTqs1-mTP0V6DPFSDEWElOPur_IlQnjoTkf4VhB9Of6bKFwjMiAO0Xu4oWlSWrcMBCgelHN6y_1zFELbUtRClHONjpqOt_h_2a99gq8zsUQJJnUjBtNTfIIKt3yu0Z2vMI98igV5sOMlmn8QgDZPJ5jwyaSjHRre3lYUVLhxADCb5n3wnmjxwAUSR6u3rXKVj00rDfM8fuy7PV5mynKhYC2LBqDM-Qdp5MLDerPSI2wyGtVEY0_WTyttPO8JLayB5J2ZeE49GPzlf2GJP_RG2WGjStPKOGg8YP0GdUh2XLuBi8ICi3AESo5DE18etW1e5zyJRzkeWeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1284b39cc0.mp4?token=Oe-Dvvhip7WTqs1-mTP0V6DPFSDEWElOPur_IlQnjoTkf4VhB9Of6bKFwjMiAO0Xu4oWlSWrcMBCgelHN6y_1zFELbUtRClHONjpqOt_h_2a99gq8zsUQJJnUjBtNTfIIKt3yu0Z2vMI98igV5sOMlmn8QgDZPJ5jwyaSjHRre3lYUVLhxADCb5n3wnmjxwAUSR6u3rXKVj00rDfM8fuy7PV5mynKhYC2LBqDM-Qdp5MLDerPSI2wyGtVEY0_WTyttPO8JLayB5J2ZeE49GPzlf2GJP_RG2WGjStPKOGg8YP0GdUh2XLuBi8ICi3AESo5DE18etW1e5zyJRzkeWeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودنویس مغناطیسی؛ ترکیب نوآوری و طراحی
🖋
🔹
این خودنویس شفاف با سازوکاری مغناطیسی، بدون نیاز به تعویض دستی جوهر دوباره پر می‌شود و نمونه‌ای جالب از مهندسی در ابزارهای روزمره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/682556" target="_blank">📅 16:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آسوشیتدپرس: آمریکا معتقد است عمان در مذاکرات با ایران امتیازات زیادی داده است
منابع مطلع به آسوشیتدپرس:
🔹
دولت ترامپ معتقد است عمان در مذاکرات با ایران درباره مدیریت تنگه هرمز بیش از حد امتیاز داده است.
🔹
واشنگتن به‌ویژه با توافق‌های مربوط به کنترل مشترک تردد در هرمز و دریافت عوارض از کشتی‌ها مخالف است و خواستار موضع سختگیرانه‌تر عمان در برابر ایران شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/682555" target="_blank">📅 16:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682554" target="_blank">📅 16:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9gFWIJrmLop-riZ_ZyBXQI_g2rV_Hu5pGDeYJbTNGBpi-lkTAp6Diwfpp9aK7TCPS8Q2IRC-JWcIQvghHCg175-a3Sq9-7TxcXyfLmWPxXlf9l_bpkW-470qgv__GKjkfjr2QJ2N5pME8yvWSBjDMSmrHsnnY4q6A3NWf3CzbnOrOa2Wj4qMDJDIEACLyrAwzfAQjNMTtznZppq9t7g0aIK_IWuSijTK5goUDmHlTBDMJZ10mx0sIaz0v1n7cox6-zwKVgEj2bQFMTO8l_81IZCwjmgYfCyxbu_aRdaViJVoOsU3wJHxjGMQH5ax1xM_fZvCWSth5li80HhePIhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درسهای فردریک کبیر / فرمانروایی که توانست کشورش را تبدیل به امپراتوری کند
🔹
راز قدرت فردریک در اجرای گام به گام اصلاحات اجتماعی، نظامی و اقتصادی در سایه اقتدارعقلانی نظامی بود. او حاکم مقتدری بود که در عین اقتدار به دنبال اصلاحات روشنفکرانه بود. فردریک از روشنگران حمایت می کرد اما شورش را تاب نمی آورد، عاشق نوآوری های نظامی بود اما با تنبلی در ارتش و خروج از نظم پولادین سخت برخورد می کرد، دوستدار اقتصاد جدید و انقلاب در کشاورزی بود اما سخت جلوی تغییرات طبقاتی می ایستاد.
گزارش تاریخی خبرفوری را اینجا کلیک کنید
👇
khabarfoori.com/fa/tiny/news-3238189</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682553" target="_blank">📅 16:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682552">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvTtNGmZTscUHJAEnOhIw7C8lrUYeUXyv6f3Pt0OVFCmqp_CwJFRKf_pSp1S5wGK-kSjGKC0gnthiu-kAM4-ss6p5zJmYIebVFq0o1j44WLRJSFxw3vud7iXaBlN5G8CYqU0XknGMqVxpepCwZnvgeBbOYfypTu907AkGQZOd7BvfcYRripxmtgqXsQcFPay1KnTuVnHTBhVJUciRxscw4Xwl2qeRGqxIQyJ_hYiIJO_PHRLUJYMtLaJITVgzBHnM0KYN7Aq4g2SkL_3vtJFB6a_dORBR7-K7ofzNNjMMxvbAlwLIObYToSe87TESYOtu83_blciS4ksC_QXHrbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ‌های جدید کارمزد خدمات بانکی در سال ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682552" target="_blank">📅 16:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682551">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: ما به قدرتی رسیده‌ایم که معادلات را تعیین می‌کنیم و با کمک خداوند موفق به تحمیل ۳ معادله به دشمن سعودی شده‌ایم
🔹
معادلهٔ اول: محاصره؛ به این معنا که ما دشمن را در محاصره‌ای محکم قرار داده‌ایم که هیچ کشتی‌ای نمی‌تواند از آن عبور کند.
🔹
معادلهٔ دوم: هدف‌قراردادن هرگونه تجمع نیروهای سعودی، در هر مکانی که باشند.
🔹
معادلهٔ سوم: حفظ حاکمیت یمن و مقابله با هرگونه نفوذ دشمن.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682551" target="_blank">📅 16:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682550">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5969bde.mp4?token=aT3pagw8HNlfKeTjxieBxl4Pz3qa_3s-CAlV7JSzX-aAXUmj82NDFz7Fo4gq51TQih8W5j24qcmtS6j-MhL3T_cpWfrVx0WVxZVJCpJkgcYMb0wxPwq7mlUKhAe-ZdsU3I1LaAXK0Bhrp6NyI-w0HXzuP7xBpwPEh960iQVVhyw3V2l9JVWeKaSVFxex9PsLo3FvXyzZr1qBnIqrI_Cz8XSnLW1JBVhv-kvnN_xjcRxaQYIwSvJYD6ZwyqV5KVpD-QXlJnyRZCJaIvK09icS1dvH0nG1Hvi7Kyo-DnyQKNH5B2kbybE8gvgsBqbE9sJAgeP8s1glEa3kH-6I7v6dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5969bde.mp4?token=aT3pagw8HNlfKeTjxieBxl4Pz3qa_3s-CAlV7JSzX-aAXUmj82NDFz7Fo4gq51TQih8W5j24qcmtS6j-MhL3T_cpWfrVx0WVxZVJCpJkgcYMb0wxPwq7mlUKhAe-ZdsU3I1LaAXK0Bhrp6NyI-w0HXzuP7xBpwPEh960iQVVhyw3V2l9JVWeKaSVFxex9PsLo3FvXyzZr1qBnIqrI_Cz8XSnLW1JBVhv-kvnN_xjcRxaQYIwSvJYD6ZwyqV5KVpD-QXlJnyRZCJaIvK09icS1dvH0nG1Hvi7Kyo-DnyQKNH5B2kbybE8gvgsBqbE9sJAgeP8s1glEa3kH-6I7v6dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تلخ انفجار تجمع گاز و سوختگی آتش‌نشان‌ها در مهاباد
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/682550" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682549">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a99cd2a4e.mp4?token=j770pPEwvoQsRNT6wftd4Jiiz3T_l6Fx1CcPV27OI0NrCMJYN1sANI5zSwsQ2_hXl95XWLOKYpXRDnxczc_Jfnc2Kcwk9xVH6iLy1qYdJ2bDuf1JXkHlYjghh4xxV1ULoHcEVS8KlvFUW6aPm5qGv6vLAj_6h1bLIOHiw19ILufAYy3Wm8hKWRH-FLewTQm6QnT6V8VsJ2vJHnL05tBcj3h3Xa3wzBxH0e1fJDOsMjloETR5_ouM5wvagti7qrukJ6gPuLr9IdSq1twgoyHazm4ko7Oa3oP53tExKgyvroHdeBFk_9R1jbE9La3ilxopahT3L00io3LiP9vC4t_l5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a99cd2a4e.mp4?token=j770pPEwvoQsRNT6wftd4Jiiz3T_l6Fx1CcPV27OI0NrCMJYN1sANI5zSwsQ2_hXl95XWLOKYpXRDnxczc_Jfnc2Kcwk9xVH6iLy1qYdJ2bDuf1JXkHlYjghh4xxV1ULoHcEVS8KlvFUW6aPm5qGv6vLAj_6h1bLIOHiw19ILufAYy3Wm8hKWRH-FLewTQm6QnT6V8VsJ2vJHnL05tBcj3h3Xa3wzBxH0e1fJDOsMjloETR5_ouM5wvagti7qrukJ6gPuLr9IdSq1twgoyHazm4ko7Oa3oP53tExKgyvroHdeBFk_9R1jbE9La3ilxopahT3L00io3LiP9vC4t_l5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨
♦️
سوال‌ همیشگی اینه! طلا بخریم یا دلار؟؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/682549" target="_blank">📅 16:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682548">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اردوغان: تنها راه حل درگیری میان آمریکا و ایران مذاکره است.
🔹
امشب، آخرین مهلت ثبت‌نام آزمون ارشد علوم پزشکی است.
🔹
بغداد از تهران برای استثنا قائل شدن در صادرات نفت از تنگه هرمز برای این کشور درخواست کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/682548" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682547">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQgJnf9TIy9_0FqVMLqFUV4AWy6nRuh_53JSRFpvBvXivuNTd_NLzBpL0ukV84zjxJC_ibBzufvGDTacICXRsFWMqtdaJ6uZCboA5OMng72xnYkccZ1OOWBN5mQSRDTwZYmCUfkdrHjIY8VL1L32W2YENUfv4PolDSHgD7plQNULiJbY1m-6mAXNW0I4RnsA8ofZzFZCRaZyA6gRSOAMRalG2Z2DwlPsIhgFuSk-irCO-XZt2wMeLtceQMpqlS1gqVDWhLdwkoJQJRJz0p3tt0hYjSDBRGIork2Aqn6u_JkFYrapEeU59DQfBpnrart4XBGPgjIJavtwptSjVuEcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشت دریاسر، مازندران
🇮🇷
🔹
پوریا فرج‌پور
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/682547" target="_blank">📅 15:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682546">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhbs9CDmxMGv3WzqrIN66Ah-A0Sevb5Wj0J1oKLIO-ugOsU5LDAvM28vKA5RJfbjiDN89nhMqX_oi5SxHT3pYkhcJaAJvQFG_aWUTurOz8aH36qCuU5CcAfFLzQCesEUTlZXB8NtOxh0nzDSz2Bp3q2jyieD5ZjK7FAt79xklVHErHaTxIWVylJIkspCA26co2nkdCePZzYxCAfiQIUNaD88FhdyMg0dx25jze8P7Mwu3QnEnYouvhDEd0jXDNOa_DDwzTX7mtWeZdfiCUJ_OaX-9XoyiWiuyTU2cD7UGnPD100egR8Cm_6fwbN4dlgRBnpYeCkw2oA1FC3UfO0jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو شرط ضروری برای صدور مجوز سقط قانونی
🔸
سالانه حدود ۱۱ هزار درخواست سقط جنین قانونی برای بررسی و صدور مجوز به سازمان پزشکی قانونی کشور ارائه می‌شود.
🔸
برای سقط قانونی، بارداری باید کمتر از ۱۸ هفته و پنج روز باشد و سن جنین نیز با سونوگرافی اوایل بارداری تأیید شود.
@amarfact</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/682546" target="_blank">📅 15:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682545">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مصوبۀ حمایت از خریداران خودرو باطل شد
سخنگوی شورای رقابت:
🔹
دیوان عدالت اداری مصوبه ۴۷۳ شورای رقابت را که برای حمایت از خریداران خودرو در سال ۱۴۰۰ تصویب شده بود، باطل کرد.
🔹
بر اساس این مصوبه، پیش‌پرداخت خودرو در قراردادها مشمول افزایش قیمت نمی‌شد و فقط مبلغ باقی‌مانده تغییر می‌کرد؛ اما با لغو آن، در صورت افزایش قیمت خودرو، کل مبلغ قرارداد می‌تواند مشمول افزایش قیمت شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/682545" target="_blank">📅 15:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682544">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBlyxtuDvp4ttuOXA_sMQ0Ya27YPmdFzZudXV78DKZVGYCmK3yCsE2E0HJk7BuY9t9aqeUkjwtprX---6ZiVQ0V1WLJvseGQO_QL63YJr39Y84gIZMxvaunNpYa7JA7P1wo18PTlXX550Z1UI5HzovRZ_ukXOzbXnfajEIgsc1Crockmlh4ovLHN7yNAJuwEoVX6X-welaY9TCOON7SNifJk9KMiG76hQeozoN4KtzJ2RiSS-qETgqykMIYsWoMAaGd2REwtQofJQKZJXvyShdw67GqIfCFuGYEiuzKRA0TKdRUhzmFNAt1m57AxR9_93FjxlGjlf70vucnAnHFTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا رادارهای آماده فرار می‌سازد
🔹
پس از آنکه ایران در جریان جنگ، پایگاه‌ها و تجهیزات نظامی آمریکا در منطقه از جمله رادار AN/TPY-۲ در اردن را هدف قرار داد، واشنگتن به‌دنبال نسل تازه‌ای از رادارهاست که ظرف چند ساعت مستقر و در چند دقیقه جمع‌آوری شوند تا پیش از رسیدن آتش دشمن از محل بگریزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682544" target="_blank">📅 15:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682543">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc6cb8826.mp4?token=D6kcUBnr64eBxGlO7ipR95bw2IZrOPJmrHMQz_mVY8zFxiM1EdrHvzdKZDvFTGZaBtmVAMD3WLmkpHb6e4yH9sjgNxWmIGU6nuxO7EphqKEiuhnHy9Wobqr4pTcgXMlPQp4xShDDHu9YaHkqqd_6VOJgsYBjLb6zAxjES55Mv-bj51JKncYFMEf90C9QfRuVvOR960GNMjRRpC34Na4_0oYlz_bMHH_LcDRm7nl35fK1M3BeMZivCExR09_uS_ELXWaTE0leGk8FzFm2CndEVmhBUKhNfid0d_K_wS4PwzrhH5LsbH_jO52FuDiTuTCy7qtou2eKzSKqwY8LgI2VAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc6cb8826.mp4?token=D6kcUBnr64eBxGlO7ipR95bw2IZrOPJmrHMQz_mVY8zFxiM1EdrHvzdKZDvFTGZaBtmVAMD3WLmkpHb6e4yH9sjgNxWmIGU6nuxO7EphqKEiuhnHy9Wobqr4pTcgXMlPQp4xShDDHu9YaHkqqd_6VOJgsYBjLb6zAxjES55Mv-bj51JKncYFMEf90C9QfRuVvOR960GNMjRRpC34Na4_0oYlz_bMHH_LcDRm7nl35fK1M3BeMZivCExR09_uS_ELXWaTE0leGk8FzFm2CndEVmhBUKhNfid0d_K_wS4PwzrhH5LsbH_jO52FuDiTuTCy7qtou2eKzSKqwY8LgI2VAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا آیت‌الله سید مجتبی خامنه‌ای در همه پیام‌هایشان از نقش مردم حرف می‌زنند؟/
تلویزیون اینترنتی مدار
تماشای کامل این گفتگو در
👇
https://youtu.be/1mRMJX8Ack4?si=Y_ZOwFaceXt2tW1k
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682543" target="_blank">📅 15:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682542">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مصوبه تازه مجلس؛ حبس برای ارتباط با رسانه‌ها و نهادهای خارجی
🔹
مجلس با ۱۸۳ رأی موافق طرح مقابله با نفوذ سرویس‌های اطلاعاتی و نهادهای بیگانه را تصویب کرد.
🔹
طبق این طرح، مصاحبه یا ارتباط با رسانه‌های آمریکایی و صهیونیستی یا رسانه‌های تأمین‌شده توسط آنها می‌تواند…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/682542" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682541">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf54f0cb2b.mp4?token=eZgvdbgXKuDNRSoWB0WKTWCUX8xhV7Fa-yfeVVXWq1PQLHbr744CIYatyKfnUYIFA9jzQ3t1_LVRkx6l-gZNAlgFXsotiOx5Y4IAOevxOqXPfXQ_o8VnGYZojTgBYuK3eyykR3zuELLqUWmPHe-MegHzW5Jv7zoAjF6jD5OktSDJ_h8Qsc76cb5YbAd3TcrkeRQuE9mYFppIVIgL6EaR_a8lZ4caftyu2ar1wKr24ZJ5pVTVzv4Gl57xbUFO1X6z0mj15SgS6VeMj637A2HvaHO-LoeWn5qfY7INw7k8VoDSzLak2MYy9unYu5MekPew44wO9EwcZXIaeJRidaHoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf54f0cb2b.mp4?token=eZgvdbgXKuDNRSoWB0WKTWCUX8xhV7Fa-yfeVVXWq1PQLHbr744CIYatyKfnUYIFA9jzQ3t1_LVRkx6l-gZNAlgFXsotiOx5Y4IAOevxOqXPfXQ_o8VnGYZojTgBYuK3eyykR3zuELLqUWmPHe-MegHzW5Jv7zoAjF6jD5OktSDJ_h8Qsc76cb5YbAd3TcrkeRQuE9mYFppIVIgL6EaR_a8lZ4caftyu2ar1wKr24ZJ5pVTVzv4Gl57xbUFO1X6z0mj15SgS6VeMj637A2HvaHO-LoeWn5qfY7INw7k8VoDSzLak2MYy9unYu5MekPew44wO9EwcZXIaeJRidaHoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران من، تو را نمی‌شود دید و عاشق نشد؛ هر گوشه‌ات، شعری‌ست که قلبم از بر دارد
🤍
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682541" target="_blank">📅 15:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682540">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3919778d6.mp4?token=FqHyHng46SnXiIjM5UvJphcRdiLvBaSmuKapXEX0o0YKsO29Pfww5S895NeT9UVZxk9w6UAqJf_zdNcPa6wMhnB8sJWOwYNVVtRhpHGZtFClO0UR0gG674DOUjvT2i86_tN8AOuo96lyQllBoXxbC8sG8EMmaGFPRzWbNSeNCyUh6uKxky2JAaDRu46P3qMd6nilq1nEsWzLCYI2cqc4d-3aJywOzLRbujBG0ZC1Zvd7SnCiSER3XdF-P8gOzglKmLeETHJlmmoMIMdQMNoZWu-NTsk53kFxSNm5hM27AQh4uwxQJzYjsEnR12l_fjXV5zmyhQDN1JXRD60jbAuLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3919778d6.mp4?token=FqHyHng46SnXiIjM5UvJphcRdiLvBaSmuKapXEX0o0YKsO29Pfww5S895NeT9UVZxk9w6UAqJf_zdNcPa6wMhnB8sJWOwYNVVtRhpHGZtFClO0UR0gG674DOUjvT2i86_tN8AOuo96lyQllBoXxbC8sG8EMmaGFPRzWbNSeNCyUh6uKxky2JAaDRu46P3qMd6nilq1nEsWzLCYI2cqc4d-3aJywOzLRbujBG0ZC1Zvd7SnCiSER3XdF-P8gOzglKmLeETHJlmmoMIMdQMNoZWu-NTsk53kFxSNm5hM27AQh4uwxQJzYjsEnR12l_fjXV5zmyhQDN1JXRD60jbAuLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض به جنایت‌های اسرائیل در قلب تل‌آویو
🔹
اعضای حزب عربی «حدش» در تل‌آویو با اجرای یک تجمع اعتراضی، نسبت به جنگ غزه و جنایات اسرائیل در کرانه باختری اعتراض کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/682540" target="_blank">📅 15:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682539">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سهم مردم از واگذاری ایران‌خودرو چه بود؟
🔹
خودرونامه: از تغییر مدیریت ایران‌خودرو با عنوان واگذاری به بخش خصوصی، انتظار می‌رفت مسیر این خودروساز به‌طور ملموس تغییر کند؛ اما پرسش اینجاست: خروجی این تغییر برای مصرف‌کننده چه بوده است؟
🔹
محصول جدید و متفاوت کجاست؟
🔹
آیا مصرف کننده در برابر پولی که می‌پردازد واقعا خودروی باکیفیت، ایمن و با امکانات دریافت میکند؟
🔹
خرابی و مراجعات گارانتی چقدر کاهش یافته؟
🔹
رضایت مشتری و کیفیت خدمات پس از فروش چه تغییری کرده؟ و مهم‌تر از همه، چرا کارنامه‌ای شفاف و عددی از این شاخص‌ها منتشر نمی‌شود؟
🔹
اگر واگذاری ایران‌خودرو یک تجربه موفق بوده، اکنون زمان انتشار یک گزارش قابل سنجش از عملکرد پیش و پس از واگذاری است؛ گزارشی که نشان دهد سهم مصرف‌کننده از این تغییر دقیقاً چه بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/682539" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0GkH1yptd1YwWuFKM8FzkWuAPdhvvp5Eqf25ASje3r5FM2dQ_6HkyKcbhQGnKMIYfTwgHapOc2XRM1PHT0ZfT5CUOxat9OeHj9NF1Uo2jv413AR117dcb2UpLEAEWYia-uqQ0MueLYgir5wYGBKefH45VFuk4RfUcXf35m-SL8qrDgntqPB2nzC9OPP_fg3WxAvbiHsJZuLxQVNpxJHtinBV21ragNs66ZY24Xdi-Oz0IHi6tbWw0hq7le8DNqQPPHYdYhcqwbRATyzytgjAbtfzEitlbXlcnNW3b6IuL1elNa-HnBnp3gdkhW7C6Gz9PFyt7xNXyfQGguOMF_9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtVS7MeZr4puQOHAopH7RoPKwip2HtP2Po-dt35trJ07XQHHdmRM9CYJOZCc1wXOfN7PbkZ3WhbI5IAYUdGhwmr-Xto4U8HD3A1EzTB9hrfgrwInZq7NzZnlJjwKuEUzc1YtyNwirZacLWTi3xje0JwSiqon58978pGJZR4D--sAUlzITeh6wdWhzoQNc7vwvxTmqFvnikvIELzgT-ipgE-uyCwNkVMM0S0AcUuNaMMSeoZzNHK9zU7p5dZMi9a1X_jLw9Z5Ok47oDQ3O-E1iiYy2DrYWlOLGX8B8w3HgC3MpK9yu9DcxOhXe12Jap5hNKeiVUrmgVcQC_bHTIL1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRXkr70ceJcTCwj_lChVMLKBgKcXUs5YAf_ucuTiCAF_YnHA8mqe7P3yu15NSC53rI_rZc-TytF0kfBwMqfWndFfZ4hd34kZCvPKJKcpRXjRp-a0hxJUM_DO_pxMANQLGDD-XeAS0sIOZT3BqZ5G_mB-krdVK9eo2ZfEAhfRFrOYF0X8BsSkWGsxRD2tOocEBs2y09Hxog_HcupB62DtymEQK4d3LKZO3Gwmf1qYCYxmgYvK-1fzaYN42v5VARG-LkDpdCqS45yTo4HdKkJsiCebOfJKB5Dg7CxohTrgeaN_yg1OgYz3UacgKgla6pCspWAB3F3RotUBEnzzTLdo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCYh30m-HRW4bjSLKejE5JFCohqssG1VjWQHrMkmvE0IQWKoYtSIBiy7l65kxk9_35XXIzzYXvIkyiQpQAjL4UUiWqG4lzc3Mgnv3VUgk8f-nKzTounCUnoRjTKHdyJ_uOpS59KfOarrR1GBxxR1-KO9B1sNXxlDEBuyTyp18WC1Cmsw9RbCOT4lIGQvydKXfOlaCT1If8TWDk-bfH708HAjGisuvebdSzjBL38EdKptKjdDJbBTVVWziA0go0keUGjagEWwhsx_HPLlUVtmgI3ngnUP11zccff_IbqM8TSWa2RUS3pq3aKf8a9928WpxnPj_FfzL6xsY0dCkr8Y8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رفاقت طوطی با گله کرکس‌ها!
🦜
🔹
ماجرا وقتی عجیب‌تر میشه که بدونید این ماکائو بعد از از دست دادن جفتش، نه‌تنها گله خودش رو ترک کرد، بلکه غذای مورد علاقه‌اش رو هم تغییر داد تا کنار کرکس‌ها بمونه.
🔹
باورکردنی نیست ولی ازش یه فیلم گرفتن که در حال دعوا برای سهمش از یه ماهی مرده هست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/682535" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYfKGKQ0_uLxatcvapQoOR2WLXsqSXGwJc8uMYVC9LhnuHft8yjAi5a9ntZrNgf6rygyCq3I95HMou_qejvaIygpVyHoLO3n-ZYV-PzJj45fWIY36Y5YWg-I60ZfLv7m0f5qQTvUj-QFDUkQYPoJI62dvm7u2Nla2R58rl2Z2x8NsHKTgWL1MFQilVxgbeVYJJRj29X0Fm1rB2Ts__wyLjt9MWxMU7XL3Es5roNjntqdFB5Qc_h_eDysarb2QOzfVJJ5wYNFxwoz8NgoTv1FCjdtIyeEwNmsnAai2ANzv1kN0ZZanmIOgz7gAESZN-uk1YeaPtLxKhXxEV2_It9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
در جنگ رمضان قدرت مقاومت ایران را درک کردند/مقاومت از مرزهای ایران و عراق و منطقه فراتر رفته و جهانی شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682534" target="_blank">📅 14:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851bc2ea30.mp4?token=c3eXxNaL8e3Vos28tTwx_l12Es-C7dgnKea8cTjtcF8n_WRIMMseAqz053aFL05jIJgNIlfvOUmZWZSVZv5RQ5eGJUvd_OCnE0QA71yLg1547FJO2Vetc1J420uJ_U1qrAvP9pRjb4yHVvQvepB1BM8aD2bByQ41xrygNj08gl2yIcVWzzFmln2y4-TowQTwJBbZ1JCLZY5HDkdR2JcRq-1ZzLWLxenBfSVvL7uQfm0Li0pHi3NFIXUIqjv_FbJJ7scrDv_Ts0K4boGGJ9om8-7YJtU0ir1y4aRbiUy7Wia8VUlvIGdhdU8m90NaAOKrQoydnekiRIH6zm572M-n_j6o7XZAsyrKFBknugZ7A3kN54Ikpd6vkrc4QdXUYoMo-Lj_gOOq60ckuCoA5NUrgjCKnCee53n0H3j1bFWV2hMx-RdAQCHu6pENO7b3fYaJxsS-H6NW-UsJ0ETnxNcul5LXlPKxVof8HeTcU0meXFpsU0sNLFOj17nEIVPFmFXooj05W8PNJlLBWLaaIXSSSGopVTkmTRn_BKFKeMcvDreu9qT3M4vPwoSRLDFS249uEZFaAw6ezUEeZMryY-LIO7CLIDO9F_qtVR7VwyNhQRAheJZtmbO6XNsAZKGCqbpmuu76KCT9b7PMCstZ6Y88lr40H_EqxJKL_jhSu0HH-SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851bc2ea30.mp4?token=c3eXxNaL8e3Vos28tTwx_l12Es-C7dgnKea8cTjtcF8n_WRIMMseAqz053aFL05jIJgNIlfvOUmZWZSVZv5RQ5eGJUvd_OCnE0QA71yLg1547FJO2Vetc1J420uJ_U1qrAvP9pRjb4yHVvQvepB1BM8aD2bByQ41xrygNj08gl2yIcVWzzFmln2y4-TowQTwJBbZ1JCLZY5HDkdR2JcRq-1ZzLWLxenBfSVvL7uQfm0Li0pHi3NFIXUIqjv_FbJJ7scrDv_Ts0K4boGGJ9om8-7YJtU0ir1y4aRbiUy7Wia8VUlvIGdhdU8m90NaAOKrQoydnekiRIH6zm572M-n_j6o7XZAsyrKFBknugZ7A3kN54Ikpd6vkrc4QdXUYoMo-Lj_gOOq60ckuCoA5NUrgjCKnCee53n0H3j1bFWV2hMx-RdAQCHu6pENO7b3fYaJxsS-H6NW-UsJ0ETnxNcul5LXlPKxVof8HeTcU0meXFpsU0sNLFOj17nEIVPFmFXooj05W8PNJlLBWLaaIXSSSGopVTkmTRn_BKFKeMcvDreu9qT3M4vPwoSRLDFS249uEZFaAw6ezUEeZMryY-LIO7CLIDO9F_qtVR7VwyNhQRAheJZtmbO6XNsAZKGCqbpmuu76KCT9b7PMCstZ6Y88lr40H_EqxJKL_jhSu0HH-SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای آتشین ارکستر دانمارکی با فلفل‌های تند
🌶
🔹
نوازندگان ارکستر مجلسی ملی دانمارک پیش از اجرای یک قطعه کلاسیک، فلفل‌های فوق‌تند گوست‌پپر و کارولینا ریپر خوردند و با وجود اشک و سرفه، اجرا را تا پایان ادامه دادند؛ ویدئوی این چالش عجیب در فضای مجازی وایرال شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/682533" target="_blank">📅 14:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682532">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZNHbWTtDUz6TBL4UIxB4zAfys0GYnlV-S5HIeDwf3qHfWWBZn6JQu9ndcvJNRUU0nBmloOzuwOREN5PtK8TsHhOX0JkV5s94rVA-N_xjYA1mk16AT3RgP01hKCC5OYq3HXTsLM3QLnl11zopzenq3vGZ7Bay5lyuHTozF8bb1TgxDjogBRzd-arlJgTS5Em0-zQD5kFBbSu6x0d7aLj9WK0jxuJYFbu2IR3lnMUD85pisAJn9BQ3AXQ4m3Q0w0Aeb8tRIYpZBuowDadSbfubZbJIyA-6bLPVkF-ZB0qjeGi3xOyq3h4DZ2G6pZ-k75ZvyAWIKHQ-mDYB94NQTLzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به فرانسه
🔹
دیشب وزیرخارجه فرانسه در اقدامی ددمنشانه از تصمیم خود برای اخراج دو دیپلمات ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/682532" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682531">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMtJkjDbjittetz9r2frEvLg7vdJSNRVJsYQ-D6wM0XjkjCPUtyvgcxzURrJwpIIlVv1Sd9a9OLO0LhyY2xIvqhMnVmkuoJAmmFDGeOnrri2y27OUImFIyAn2Co5oHjAus9l3aPLEl1Ja0gVW-3qSXRfeXarX5Tybk3MlsUK9L3i5V3mzE4UnOYrPb5eTmsWdqlJ9Rv0NiYauOoC9ijT_LFhr7qxXW07ns19NfntkMoONcwv_fLqkqIpqxZMdeZXSlAJGqXspg7JiFNa9EOrI9WE2ujk04l_VU3sZiEBzeRfLGt4yZYJIvAzN4KH7owpIzzbHQ10alj_JLwDVXqrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی، تحلیلگر سیاسی: کاخ سفید همچنان در حال ارسال پیام به تهران است
🔹
دیروز، کاخ سفید اعلام کرد که مذاکرات ناموجود با ایران را «به حالت تعلیق» درآورده است، احتمالاً برای افزایش فشار اقتصادی. اما چیزی که کاخ سفید نمی‌گوید این است که تا همین امروز، آنها هنوز در حال ارسال پیام به تهران هستند. صداقت از ویژگی‌های ترامپ نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682531" target="_blank">📅 14:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای رویترز: جنگ منطقه، ژاپن را وادار کرده نفت عربستان را از مسیرهایی دو تا سه برابر طولانی‌تر منتقل کند
🔹
پالایشگر ژاپنی Idemitsu برای دورزدن ناامنی دریای سرخ و مسیرهای متاثر از جنگ، بخشی از نفت عربستان را از کانال سوئز و حتی دماغه امیدنیک منتقل می‌کند.
🔹
زمان حمل برخی محموله‌ها از حدود ۲۰ روز به ۵۰ تا ۶۰ روز رسیده و هزینه حمل افزایش یافته؛ نمونه‌ای دیگر از اثر مستقیم جنگ بر زنجیره تأمین آسیا./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/682530" target="_blank">📅 14:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استودلاگیل؛ شاهکار طبیعی ایسلند
🔹
دره استودلاگیل در ایسلند با ستون‌های عظیم بازالتی خود، یکی از شگفت‌انگیزترین مناظر طبیعی این کشور به‌شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/682528" target="_blank">📅 14:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90806f0a3.mp4?token=YY1fCGnpFRQ7_2Pp1B-hiSwFIV7wcKkTQ8w_ThywtmBen7iwOiqOrzyvfUt2TY6mJ77XWamA10kywL33x8OKzmnihT_dl53Jx4gxomal2hhaz2uxU3GKZwe7sfx9CIKUVA7LP_B5Ormg3v_QsezUqEvyvHJrm-cIRpzIT3PgJJiPPQmr2MYJWRnWMk1q-etYGZkNoT6idhKLLsxKmlTUsw_Vgf0YFuunB31py-OjeuZ5Dh05PqnxjtxeqKr8tlgS61OTHecAW3Gu9K8O_Z61nkzttg34GphuSj7oCSygChUV-nC_M4wbKey-LT2VXyfDgoalDwv1CsD-J1JLM8EjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90806f0a3.mp4?token=YY1fCGnpFRQ7_2Pp1B-hiSwFIV7wcKkTQ8w_ThywtmBen7iwOiqOrzyvfUt2TY6mJ77XWamA10kywL33x8OKzmnihT_dl53Jx4gxomal2hhaz2uxU3GKZwe7sfx9CIKUVA7LP_B5Ormg3v_QsezUqEvyvHJrm-cIRpzIT3PgJJiPPQmr2MYJWRnWMk1q-etYGZkNoT6idhKLLsxKmlTUsw_Vgf0YFuunB31py-OjeuZ5Dh05PqnxjtxeqKr8tlgS61OTHecAW3Gu9K8O_Z61nkzttg34GphuSj7oCSygChUV-nC_M4wbKey-LT2VXyfDgoalDwv1CsD-J1JLM8EjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل حملهٔ تروریستی به دادگستری بهبهان که عضو گروهک منافقین بود دستگیر شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682526" target="_blank">📅 14:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmUXvu2n-HNFALRtM2xpatAPycpjPYAibvtSXX8jSTmD9e3sNjP3pZxVGPDWVc5mu6ESgERTnDSfObDIyG2yvc3KGP4D4SiBkNPvvQfdQn8miUoI9w3s2Hu8LSVYLuqxeHGEABMyErM-iOVCcjCYkjB9EVJAZm3YOurphHW-MTHjfolqwXmOs0fWGCDoM7cnTt6IR5bAibeeSogOjY15Bqz3I6y-3HYpMSqo-rimnNSlTkBbsYyuuO6WQc-7Hpho1bsk14ku1Er4v7TXQ3F4bk5QFVkux6LF7LuQIFTxPGcYYomisUygC4LYJNuNPRTaC1RlDkpnUZS23HOJ9g-V8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDY5ipFYq0UmR9BIMObYD_eSBmcW5E13Uzs7LQkDAO_O18l6ezd6IpfzAlHaeaVWEL1XBrQMt1tOTaYSuHkV3aTEJWvxLduK1t6SQjJdkTsn97mYVe2ymNSgx0BX0dGDaYDv4A7WJN0jSmsTxhzzmPNj5h34N5TesiYqfnI5fNeOeFZLN4Uy5EBOuot0_4QhhFX7WkovxLSlUNYX94Di__QvE0TFtzkq4TgnHc1bryBqXqXSyXT_FoEe40hFLS96cS79asSKl2q4ec7SsbUHxqBdtJks3PrpustBEyw67LTYgrGd2KGnQFdOp9i43b7HPyckzsVVBaPiSV2_sTiyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfbr1i4NJzm09-OxP_MFMnV2AgjaXmfFn23SvVqT_59rbm8t27lrzxwj3RFXXJBLF5bVZQ9t79inVUFK7etpW2VVkt743mgNKAYkgLtZlNk3CcDnrCdNsQqHi14TglJ7WelqEQmotH7TIHrLyjGZDC3g0SW0JmLj5tvEeYNSZwC2Y4Pi9mHbb0gKXKXLD1INtxaczYL-RUXRxtS4T6JRhiCVYef6bXIBM-uT5h4Cwe9JLptd5F9anjz2KGpy5SDCNK_WXh1NOZrbXGiJQM973EK3dZvKeqWfiK0R8ewXjXLhwd6IFxKds4TVpeh_cAgATmuqp57F-POKBE-hOMQozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlDPPY59N1VzwjDhhifejbRvCUYHLbZQYDn7y8KBFF8hLkTQYN1uLTiUREeTqmudTURmZzOOJ6UD4Ma2wdJORrn8iotNJWgVuL78yAX05aCFnp4K7PlZxE6T75lSxjjeWNTnILzgxz0oUyyJJbPrXqtsgWTQbCpWGmvNpw09SxLZdvH1u75aiYc--pu7bjd3t-nr_i9Ycg1nXmJy7vLuONdc63DUx_179oPJ0LaQnSuRouzFzZ3hCkXR9MdNQO8YQa8Od3SNq6iFBBCyTZuOy7zg-2RRu-FsSZT6TvnPVFaNNFV9G0Khdaat9xlhJh-LmPvlig6RkFrPPjdJWTY56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s21rTIpr-9g5gag6FPTMfQAfFa9gzR2CI9q6sypTCzX9ru-KAAsbPldS61cU0J5P_5Qpx4yV8T45h319r3xHUzQLuSnxTfB__92IbD2qJRVXr3NFz2tnbntoGiSMLsdk6yLdtAHfSsLaXQJS5xCjmNbvtbbLEWN-8fBA09sdwmpHujxPSsVOT0MRbYbTL-wTUkxLZnhcJYOCjtPFyO7h3AgDEPXnA0pu3dh1gYImS3wGWKQrRg8yDNpMlcGlrpcj1Hg6EeVOYQPK9oJN3vIkehlR9cjiPyhr0HDxMs_V1EpVfEVID7SvhNtbIUW-U7XTv6Dqur1ppMVAQrwykdCdnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خیلی راحت ‌و آسون تی‌شرت‌هایی که دوست نداری رو تبدیل به شلوارک کن
🤩
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/682521" target="_blank">📅 14:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
داربی استقلال و پرسپولیس ۱۱ شهریور از ساعت ۱۹:۳۰ در ورزشگاه نقش جهان برگزار خواهد شد.
🔹
سرنوشت ۱۳ صیاد بندرلنگه‌ای پس از یک هفته همچنان نامعلوم است.
🔹
فرمانده انتظامی اصفهان: در ۴ ماه نخست امسال، ۱۸ زن موتورسوار در حوادث رانندگی جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/682520" target="_blank">📅 14:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/682519" target="_blank">📅 13:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682518" target="_blank">📅 13:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-voDZMLchGtLHZTzAVF7TfBkssSlSrmuLQ4boow2RXW89AINfYuE0PB1AvivER5NHMmCS9OrKERgadZFpIA-51x2wgDNR_OdB1OWedXxUNOmLNbCjpoQ9mE3m9GqHG1BS0GuAGo2sUnV7y2FC_Mhe6yy_I_mOa7hHgrlOo8w51ke8jNQD0DOl1gcbkGuDE8HA1x7NJLKpLtyB8zt5KgtIrbykusfAWt9q6pP5CbEe0v6tRc1NknLqBBWtsI7ipvJBDdLOI9mnCQ7O_nBarfUeO49KfT47myg8sqhgQkot-ZCroE_nokN_0eGdf3y8-l6eJPIWxP6egQZGVRjOaTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به فرانسه
🔹
دیشب وزیرخارجه فرانسه در اقدامی ددمنشانه از تصمیم خود برای اخراج دو دیپلمات ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682517" target="_blank">📅 13:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtmFbKSTMd1O6lGVyMSCHbY_gx1uOjKxJma9QYm9IigOro4gle-Uxhaa7-nPdCoLY87QuMT3TUBkTSSyt9ZFnY5km4otm0nQuFmURRyzCHNWaLCX3ZRL1MAojYm1O-zVitiRaLaNJgT6-YEH7HLl3hx8rm3-_sW-Q2kIYPEXDZ2bHiYq_v8-T15SCsWGM4SSNXZABKptBH7Rm83cXa2o7veEgvd5C_PamTp9KKFqPQA5PXNuJPD7hRZ-jmO--RAI1edHz_cIcs4LRfT3ffVMIYRfP91wf7asVihjH8CiAuqd-ZYGoqHSfysMvJ0thN7GIuhZ1ZULHIRZfITIi7GdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غیبت ملانیا ترامپ از ترس ایران ۲۵ روزه شد!
وبسایت Wonderwall:
🔹
ملانیا ترامپ پس از انتشار ویدئویی که سرویس مخفی آمریکا آن را تهدیدآمیز و مرتبط با ایران اعلام کرده بود، ۲۵ روز است در انظار عمومی دیده نشده است.
🔹
مشاور او می‌گوید ملانیا آرام و قاطع است و این تهدیدها باعث عقب‌نشینی او از فعالیت‌هایش به‌عنوان بانوی اول آمریکا نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/682516" target="_blank">📅 13:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682514">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عضو هیات رئیسه مجلس: واردات خودروهای کارکرده آزاد شد
🔹
واردات خودروهای نو و کارکرده ۳ تا ۵ سال ساخت با پیگیری‌های صورت گرفته، آزاد شد.
🔹
سقف واردات خودروی سواری در سال جاری به میزان ۲۰ هزار دستگاه تعیین شده است.
🔹
امکان استفاده از منشأ ارز سپرده خود یا دیگران باید در فرآیند واردات مورد توجه قرار گیرد تا متقاضیانی که منابع ارزی لازم را در اختیار دارند بتوانند بدون تحمیل فشار مضاعف بر منابع ارزی کشور نسبت به واردات خودرو اقدام کنند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/682514" target="_blank">📅 13:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682513">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: افزایش حملات دریایی ایران در تنگه هرمز
وال‌استریت ژورنال:
🔹
حملات ایران علیه کشتی‌ها در تنگه هرمز افزایش یافته و این اقدامات، آمریکا را تحت فشار قرار داده است.
🔹
واشنگتن تاکنون از واکنش نظامی گسترده خودداری کرده و تلاش کرده با فشار اقتصادی و اقدامات دریایی، بدون ورود به یک درگیری بزرگ‌تر با ایران مقابله کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/682513" target="_blank">📅 13:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682512">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d58320645c.mp4?token=LwGuwOC2KCVWHDFkWaiEoW_vwNuzkH0B_gqsfRpPDSPhb9hvPudz5xf32Gc_ZjtuFTq0hoFjE3yo-FQyruyuEmMrbmDdzwjDZaFDLXO9ia9CzAd4r_7C2CHBeiJL9VCa-OefnCCu0gmAsQINZsc6C-u-5sP01tMA0cKyviyTZStTBcnIxmmh0nOxdNTT4WNqrmobeaxLtD9ptYLB_Whye7x50py7_2MEbH5FU936G_O14X_J8zx_y7BZghbzcaTWLS87KbsvPpM5tJFbTaVeZ_Myvj1Zd8rc0e0lQ4y81jo6L7Z7qcr_xnsmqnp--RaiKF97QJvPyB3CxNLYL09pRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d58320645c.mp4?token=LwGuwOC2KCVWHDFkWaiEoW_vwNuzkH0B_gqsfRpPDSPhb9hvPudz5xf32Gc_ZjtuFTq0hoFjE3yo-FQyruyuEmMrbmDdzwjDZaFDLXO9ia9CzAd4r_7C2CHBeiJL9VCa-OefnCCu0gmAsQINZsc6C-u-5sP01tMA0cKyviyTZStTBcnIxmmh0nOxdNTT4WNqrmobeaxLtD9ptYLB_Whye7x50py7_2MEbH5FU936G_O14X_J8zx_y7BZghbzcaTWLS87KbsvPpM5tJFbTaVeZ_Myvj1Zd8rc0e0lQ4y81jo6L7Z7qcr_xnsmqnp--RaiKF97QJvPyB3CxNLYL09pRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش درست انجام کارها؛ مراقب ستون فقراتتان باشید تا سال‌ها بدون درد حرکت کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link‏</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682512" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس مجلس: مجلس در نامه‌ای به دولت آمادگی خود را برای اصلاح لایحه بودجه اعلام کرده است.
🔹
رئیس کمیسیون امور داخلی: جزئیات طرح مقابله با نفوذ بیگانگان هنوز در مجلس نهایی نشده است.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۵ هزار واحدی به ۵ میلیون و ۹۵۲ هزار واحد رسید.
🔹
معاون سیاسی-نظامی ارتش روسیه: گسترش جنگ در خاورمیانه می‌تواند به نابودی اسرائیل منجر شود.
🔹
پروازهای فلای‌دبی و ایرعربیا بر فراز فضای هوایی ایران از سر گرفته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682508" target="_blank">📅 12:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
جزئیات سهم «سوابق تحصیلی» در «کنکور» امسال
🔹
بر اساس مصوبات شورای عالی انقلاب فرهنگی و اعلام سازمان سنجش، در گروه‌های اصلی (ریاضی، تجربی و انسانی) سهم سوابق تحصیلی پایه دوازدهم حدود ۴۳ درصد با «تأثیر قطعی» و اما سهم پایه یازدهم (۶ درس نهایی) حدود ۱۷ درصد با «تأثیر مثبت» (یعنی فقط در صورتی اعمال می‌شود که به نفع داوطلب باشد و نتیجه را بهتر کند) است.
🔹
همچنین اگر داوطلبی در درسی سابقه نداشته باشد، نمره خام آن "صفر" در نظر گرفته و تراز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682507" target="_blank">📅 12:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfe029831.mp4?token=JPN1JtI0OPCr2Kjio_-JlhVvtnk1mej9_kvRnhhMvQ_Exrckpf6My99_zlt48w8nNUzXtPCJfz0PuRTIhmgo7NWhk5Kl3WcAQLqj0SfaFzqArfeATmdrtZeFGj1glCL9bJe_D8_OY_CxphoeP11g-H9e4g5VfOANWTnUoODxh40M5s_Rgq5qagzFWYnASmz6S-xySA7CPnLAnRXqVJAlaaSNnNbQ55ip6s-EiGp9yzubMaI3ffHPtODSh6FeWgPZd3BD6Ol3AwFVxue-6gXbT-O9kI3hhVFMdDJW2eYXBrtPl0pQPBaIbMzfbe1MehMfIl1_e0DF7ESI4cFGUeKN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfe029831.mp4?token=JPN1JtI0OPCr2Kjio_-JlhVvtnk1mej9_kvRnhhMvQ_Exrckpf6My99_zlt48w8nNUzXtPCJfz0PuRTIhmgo7NWhk5Kl3WcAQLqj0SfaFzqArfeATmdrtZeFGj1glCL9bJe_D8_OY_CxphoeP11g-H9e4g5VfOANWTnUoODxh40M5s_Rgq5qagzFWYnASmz6S-xySA7CPnLAnRXqVJAlaaSNnNbQ55ip6s-EiGp9yzubMaI3ffHPtODSh6FeWgPZd3BD6Ol3AwFVxue-6gXbT-O9kI3hhVFMdDJW2eYXBrtPl0pQPBaIbMzfbe1MehMfIl1_e0DF7ESI4cFGUeKN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملیات نجات گنجشک
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/682506" target="_blank">📅 12:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6lWa8gsBgpi0aLvGIOl-yc-8ZrPIIs6KuJY8oPnYDkEzC8wlbpY86oHKyx9y51qP7ilBtow9ALhfnHB0fat7MNseGbc0DNp_c8JTL_mE8I7j72Cjuvtq7dbVn6YsNx2PSyDRQ3SUfYN9o3R69j_tjqYQ5fGzoZWOAvWKV5DVlZTGriPnIxzCDfGJgdXwVKEHzT-6flpUWcBav9M_x6DrsoBMyy-pfYRVYnIaY4-L8pFIxEtK_zcNCNAcWicIyheOfFCW1PNsQjGQ4xIQnYNDXNHfyRTWR4PdUlPEu-0CgBJdw7gVjc3Zdy8zv-CBTlRnFb3LywbN1XT8Jy4nKJ6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل رایتل:
#حجم‌خواری_اینترنت
خط قرمز ماست؛ در برابر آن مماشات نخواهیم کرد
🔹
مهدی فقیهی، مدیرعامل
#رایتل
، در واکنش به طرح گلایه «حجم‌خوری»
#بسته‌های_اینترنت
از سوی برخی کاربران گفت: با صراحت اعلام می‌کنیم که تا امروز هیچ موردی از حجم‌خواری و کسر عامدانه و غیرواقعی از بسته اینترنت مشترکان مشاهده و تأیید نشده است و اجازه نخواهیم داد چنین اتفاقی در رایتل رخ دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/682505" target="_blank">📅 12:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای فرستادهٔ ترامپ در امور سوریه: دیروز یک قدم با درگیری ترکیه و اسرائیل فاصله داشتیم!
توماس باراک، نمایندهٔ ویژهٔ رئیس‌جمهور آمریکا در امور سوریه:
🔹
ما دیروز تنها یک قدم با رویارویی نظامی مستقیم میان ترکیه و اسرائیل فاصله داشتیم. حملهٔ هوایی اسرائیل به فرودگاه «ابوالظهور» در سوریه، زنگ خطری جدی برای شعله‌ورشدن یک درگیری نظامی مستقیم میان تل‌آویو و آنکارا محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/682504" target="_blank">📅 12:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
خریداران چینی همچنان نفت ایران را می‌خرند
ادعای وال‌استریت ژورنال:
🔹
شرکت چینی هنگلی با خرید نفت تحریم‌شده ایران، به یکی از حلقه‌های مهم در دور زدن تحریم‌های آمریکا تبدیل شده است.
🔹
تحریم‌ها توانسته‌اند شرکت‌ها و کشتی‌ها را هدف قرار دهند، اما به‌دلیل انگیزه اقتصادی پالایشگاه‌های چینی برای خرید نفت ارزان، محدود کردن بازار نفت ایران همچنان دشوار است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682501" target="_blank">📅 12:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a7f9e5a97.mp4?token=sac1KsikmIF_4MQ7xmNgwv1zG7WR4xM-LIPMUwDc-V4Zc-haEsfD-trkfBaaFm2ry_R9bqoYMrtTh5BkRWN6iTd-E3ePjZxoGZQhqTVNO3U8OfV5DvSlIYMyytCQYfzH0XyofnnqrPsYe1kFBM_mbu8CeYE_8AZCkI3C9YWVGbrOL_RmBOnjr8v9NvJ03_CSzm071lojNuJzERCA4BMFWXbocD3LsORKg1zl0MV4jRegjNvmsPXd3SqS-YF6D5f7CPGir6c8_HyCThAWOfT7ewTy2hqID8Fj-m-MhCSP8tI7tX5y0izBI0G4mAilxJq4tM-SeIdKYHzy2k1bu5mMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a7f9e5a97.mp4?token=sac1KsikmIF_4MQ7xmNgwv1zG7WR4xM-LIPMUwDc-V4Zc-haEsfD-trkfBaaFm2ry_R9bqoYMrtTh5BkRWN6iTd-E3ePjZxoGZQhqTVNO3U8OfV5DvSlIYMyytCQYfzH0XyofnnqrPsYe1kFBM_mbu8CeYE_8AZCkI3C9YWVGbrOL_RmBOnjr8v9NvJ03_CSzm071lojNuJzERCA4BMFWXbocD3LsORKg1zl0MV4jRegjNvmsPXd3SqS-YF6D5f7CPGir6c8_HyCThAWOfT7ewTy2hqID8Fj-m-MhCSP8tI7tX5y0izBI0G4mAilxJq4tM-SeIdKYHzy2k1bu5mMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جرم اسرارآمیز در خورشیدگرفتگی، هواپیما از آب درآمد
🔹
ویدئوی ناسا جرمی درخشان را هنگام خورشیدگرفتگی نشان می‌داد که ابتدا شهاب‌سنگ تصور شد، اما بررسی مسیر پرواز مشخص کرد این تصویر مربوط به رد یک هواپیما بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682499" target="_blank">📅 12:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF1Pwib_vWKWHzd9r0psk1HvLjromgThe92ySpwQfo7Lhg0Tnwijoukr57vszE_FLCmg0HxmfAf2ICeWh5w1bfGnNUCezukS1Rcgdty6nhCSj2k-q6jng6M_SmpeQiBGBiFfdlpl_P8K2UJyssKUdTNAS2B0MfVc0jvnWSSM1u4TKWDOxdtgo60hokPYV_gZ_C6yVYwDPFbRKXxhfiYj01BZCKLl2b_kkB8zMRbM-g8IFFm05z3N06I9nCXTN6D4T5MSDewzJyQXQx_LxWak0yzk-BfCbT0tsxdKm3HcNkRjRzE-CFGNECmPpVvqLv56AhQuOBOKOpzIwHr8rEsJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فایننشال تایمز به نقل از منابع ایرانی: هدف قرار دادن احتمالی زیرساخت‌های ایران می‌تواند جنگ را از منطقه فراتر ببرد و به اروپا برساند
🔹
تهران حمله به دارایی‌های آمریکا در کشورهای جنوب‌ شرقی اروپا، از جمله بلغارستان را ارزیابی کرده‌؛ قبرس نیز در میان اهداف احتمالی قرار گرفته
🔹
ایران می‌تواند از موشک‌های بالستیک میان‌برد خود، علیه دارایی‌های آمریکا در جنوب و جنوب‌ شرق اروپا استفاده کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/682498" target="_blank">📅 12:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Roode Sookhte</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/682497" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
رود سوخته
🎙
محسن چاوشی
#آهنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682497" target="_blank">📅 12:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان  مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/682496" target="_blank">📅 12:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwqHF_dntiZSFW31VDTs41-1IP8_Iyy6QYu2vrF5lWhvWYynGNx1RbDUsAg8Z-p2Dz21NPrpfs_qgw2PRk1kqwTmxzM1mhOY6EfyDcHB0XIw-B6JhGm1RXa1xE_z-ZJsazixI6ytJC76yYTtauve_qNynqDLm5JrOTnHWNTasMu-nHdFOD4XhYSFibq5G1q5U9yHCMb32ZdS2dJZ37YfPM4ZmNjvj-8ziTDq-0RU8g3IRkgKSqW2Hlwq-zpyOKbcpSQNF1B-GUg0_nnXYAULM_x22ZzWZHBOaZhBSacsjhs76FvErn0FcRayaO3z4c097HpX5uR51TOq1ExhFw_mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ال‌ نینو» امسال احتمالا رکوردشکن است
🔹
اداره ملی اقیانوسی و جوی ایالات متحده (NOAA) پیش‌بینی کرده است شدت پدیده «ال‌ نینو» در اواخر پاییز یا اوایل زمستان امسال به اوج خود می‌رسد و حدود ۷۰ درصد احتمال دارد که به قوی‌ترین ال‌ نینوی ثبت شده از سال ۱۹۵۰ میلادی تبدیل شود.
🔹
این پیش‌بینی نشان می‌دهد ال‌ نینوی امسال به سمت قدرت «رکوردشکن» پیش می‌رود و اوج آن در اواخر پاییز یا اوایل زمستان پیش‌بینی می‌شود.
🔹
کارشناسان هشدار می‌دهند اثرات گرمایش جهانی می‌تواند با ال نینو ترکیب شود و امواج گرما و شدت بلایای طبیعی را تشدید کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/682495" target="_blank">📅 12:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4HYOY_rnzRcNHMSsotk58L-6DbMB4OWno98xyyvo97VSJ90n_2ugeZflEvjR0f4HxqnXO7723_2MoA5A0LE6xT61kv6JycJ1Ajnkig0pvRwaafb3X0apnIrPQauS_RlpVVzinypXWPV3Nlyq76t1CtkKLvDxtElpPyuHj7pruoVV8GzL6vqE2ejao3mr1AN2jfLI3-jsO-N5BJ1A8Y-eDogc1hg-Jz9k1bOL9hWqcav7zvTRR0sNHdLf6BVv-hOu9DvJKgqontH-nEE9bdQq4ok41fKFYyy9SLIiYkMw6n_C9DRs6DXrk0pXzW37PnP5PTysc96HYoELek06_7QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: چه کسی آن مدرسه ایرانی را بمباران کرد و ۱۶۸ کودک را کشت
🔹
ترامپ: «ما نبودیم. آن موقع کلی آدم تیراندازی می‌کردن. ما غیرنظامی‌ها رو هدف قرار نمی‌دیم.»
🔹
خبرنگار: «طبق گزارش اولیه، سیستم شلخته‌تون باعث اون حمله مرگبار به مدرسه شد.»
🔹
ترامپ: «تو خبرسازی. بیرون.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682494" target="_blank">📅 12:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b2a38ba8.mp4?token=vV1fMWjVRssPGdZoKsRAXU1P5fSgI_ytTjTB8N3JGgc2ZC3u4tJUAlpZ2xDxlXhiDMMxWaKGv_ihsVN-1zdFGAgi6QLxZTVJHHcqfZssn_AXAJ4gpvBUZHVmKPFeNAxbn-rVY1oXwH0PYP-1YDj1qAxyp3Ajvi_TWwlyVwRtmBIAH82pu8cvHCyFYfUuVupwqmtFjIV35Igo2RB1TGapYNxdRrHWDv9cGGNomvnglz-T2jBBvQT3YhLhTbnAzKIHQa6R3UcQPF1co9ZiQ8O4v0w4NOz05H8RrHmX17XfmNNs3wcJCl_awmXMwl9YQDkI6CWipHrS2Z68UsqUDpIKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b2a38ba8.mp4?token=vV1fMWjVRssPGdZoKsRAXU1P5fSgI_ytTjTB8N3JGgc2ZC3u4tJUAlpZ2xDxlXhiDMMxWaKGv_ihsVN-1zdFGAgi6QLxZTVJHHcqfZssn_AXAJ4gpvBUZHVmKPFeNAxbn-rVY1oXwH0PYP-1YDj1qAxyp3Ajvi_TWwlyVwRtmBIAH82pu8cvHCyFYfUuVupwqmtFjIV35Igo2RB1TGapYNxdRrHWDv9cGGNomvnglz-T2jBBvQT3YhLhTbnAzKIHQa6R3UcQPF1co9ZiQ8O4v0w4NOz05H8RrHmX17XfmNNs3wcJCl_awmXMwl9YQDkI6CWipHrS2Z68UsqUDpIKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌های خودشیفته تو رابطه چه شکلی هستن و چطور باید باهاشون برخورد کرد؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682493" target="_blank">📅 12:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=Z7n2UM0CSHRKC4l58wQOcUg4ZuwcVE3v4kq_btf7JXkvBrTap5Og8Rhelvg9o3H3tNiueWdEafs9nZ7ll2cwkG6zekPnhvRPCfn3a3taat7G36kadeYUMb4-4qtDx-CQxRwDyLdalWPjOo1lgDurTK16dCyWNDV9V_q9URGvu_9S0LDvSVZCd5isNjURvxPBjOYzutPypG0-ZPlN84t8e-DailSKryPS6WiIaxS8k0BQYCqTxIGvH09mXdJKE9M6BD9EygciPYc8_vk6GqQXi5H4h_yUlhzds8zzJ155hffspL9oTfGEkyWC1TEuiNZDOcZzhjaFIzkdiJ91omU-qKdIfTbOJ4MdfcVPcD5QiUFDLC9tGJYzxUw6lYcc5d9wnfZB24mIjapj0DghUOXWsA3oZ-tjn9k5G7CFzymZHssrV5N4iBPjCFOXjD1C_DyJYp8PjQtkWrbILimngREwuFylu_87SP8WsjEhhA27XuooBbIooPb3yYx4uSdWcIB6dKi8bujo0JNhccYhrrgKBhnqflnB-_auMItJvCJAdR3aVotLgJvA3et2cTHb_LOn3VZrDydwvx1qtfXPS7U-fGZ5kxrgshgIEg4NxbeHL3-MqpNuI-0io2vMgEXOS5-3sVLJEzVFUrzFUIz2rgRDCnF9oohb8POdMraWXD_HZKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=Z7n2UM0CSHRKC4l58wQOcUg4ZuwcVE3v4kq_btf7JXkvBrTap5Og8Rhelvg9o3H3tNiueWdEafs9nZ7ll2cwkG6zekPnhvRPCfn3a3taat7G36kadeYUMb4-4qtDx-CQxRwDyLdalWPjOo1lgDurTK16dCyWNDV9V_q9URGvu_9S0LDvSVZCd5isNjURvxPBjOYzutPypG0-ZPlN84t8e-DailSKryPS6WiIaxS8k0BQYCqTxIGvH09mXdJKE9M6BD9EygciPYc8_vk6GqQXi5H4h_yUlhzds8zzJ155hffspL9oTfGEkyWC1TEuiNZDOcZzhjaFIzkdiJ91omU-qKdIfTbOJ4MdfcVPcD5QiUFDLC9tGJYzxUw6lYcc5d9wnfZB24mIjapj0DghUOXWsA3oZ-tjn9k5G7CFzymZHssrV5N4iBPjCFOXjD1C_DyJYp8PjQtkWrbILimngREwuFylu_87SP8WsjEhhA27XuooBbIooPb3yYx4uSdWcIB6dKi8bujo0JNhccYhrrgKBhnqflnB-_auMItJvCJAdR3aVotLgJvA3et2cTHb_LOn3VZrDydwvx1qtfXPS7U-fGZ5kxrgshgIEg4NxbeHL3-MqpNuI-0io2vMgEXOS5-3sVLJEzVFUrzFUIz2rgRDCnF9oohb8POdMraWXD_HZKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔹
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔹
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682492" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فایننشال تایمز: اگر ترامپ تصمیم به تشدید جنگ بگیرد، ایران در حال بررسی امکان هدف قرار دادن اهداف نظامی آمریکا در اروپا است
🔹
بلغارستان
🔹
قبرس
🔹
کابل‌های اینترنت در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/682491" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1CGWhAtFVk4z4eDAejuWbBJl7hOneqIQdCKK5z6xCaOWTGqEAR_TsJ80pSClienautagtSUoL7AN7X8yuRavfrfdLzVvHLbQBeV4Kj5WLKw6Lx9hBGsVl1FhtOpsZW5Nsh4ZYYWWFEM7Jjejyd6cFgHq7iaUz9PPf6QgwsbCTyY8ENTtHRmIrVF2UFOcQWF4m_l7fySaa4bm7ptRuFJYqM3B1uUQpu7hmMaf8hsEP-qiJECA2QMrV91hSx2OTmQ6nQlOsT5ZU448Amjz6bOXeZvEVc8uf1OseaHY55Mc_cFGhLRXTxvq62o-MpPrhdQm3KG_1VzXV_WE6f5nA_6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان نصب چهار اپلیکیشن‌ اصلی نمایش خانگی منتشر شد
بیش از 40 میلیون ایرانی شبکه نمایش خانگی را روی موبایل خود تماشا می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682490" target="_blank">📅 12:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b94f2770c.mp4?token=pTuiW7HHPZFKskNRki2T0dFDiRqGc52mbE_b-ZqlsX9ST0Flj_cMsLVWNBGDGklBvMxPTB9PaGipsYS65tNkU9b8FIjjcaiXCc_Tm_lFkFtbyDpqwEHQvpPxZGEhjlxlNnK9918sTDhcbUac1fkOb3NbrDz16tyNBM5pvmNynrBEUlSWEExHw2dVtY_PX2YuiRnLwg5efvHCVn3A9Q820R6iPzQJtN77jThS8HgQJ4wkj6bqqSI8qB0xOtfKh6yyvFzEySvVmkF_ZtibndLx-nhqghuos8C5cUGhTPZY-Y1LFxwfQElTaaD4noq0vFDznlH3z1TECT7QhSKI31paIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b94f2770c.mp4?token=pTuiW7HHPZFKskNRki2T0dFDiRqGc52mbE_b-ZqlsX9ST0Flj_cMsLVWNBGDGklBvMxPTB9PaGipsYS65tNkU9b8FIjjcaiXCc_Tm_lFkFtbyDpqwEHQvpPxZGEhjlxlNnK9918sTDhcbUac1fkOb3NbrDz16tyNBM5pvmNynrBEUlSWEExHw2dVtY_PX2YuiRnLwg5efvHCVn3A9Q820R6iPzQJtN77jThS8HgQJ4wkj6bqqSI8qB0xOtfKh6yyvFzEySvVmkF_ZtibndLx-nhqghuos8C5cUGhTPZY-Y1LFxwfQElTaaD4noq0vFDznlH3z1TECT7QhSKI31paIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش گرافیکی و دقیق از جراحی تعویض مفصل ران که توسط هوش مصنوعی تولید شده است
🦿
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/682489" target="_blank">📅 11:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UykVuDF3xhH4TdkA4EAo4dy_kbhPuUwwfY676N7B-YjnO4WqxZ85g7ImeUXClTQEAxTdKI8u1ELGQeqeCyrh-6WPzRZx5SoGtfBm3miLRJYxfsg31o0-DZaUHEKKSk9ciTdqDgYs9aPeTk-CdgQQTQvky6mZv7TiluoTpcXcWSGVAp7MlZl7FlnEzXYP6SAPrNNPyHz0AtW-8d-EV0nljPocDIXdPLl3_zg-Yv9wksaR_ux1C3QyYleOWuCHBnCNCr2Geiwz-Owpg9epy4Uo7S5QHU3kY7o3c1Gfv45wwSAt6-8KWbxFaqW3Ub6-NYRgUM4Cahsb-mLQOnkrsglpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودپرداز طلا؛ مسیر تازه برای دریافت فیزیکی طلا
🔹
شبکه «طلاپرداز» با همکاری طلا کارت و توسن تکنو راه‌اندازی شده تا کاربران پلتفرم‌های آنلاین طلا بتوانند شمش طلای استاندارد خریداری کرده و آن را از دستگاه‌های تحویل طلا دریافت کنند.
🔹
این زیرساخت همچنین امکان تبدیل طلای آنلاین به طلای فیزیکی و دریافت آن از دستگاه را فراهم می‌کند. قیمت طلا توسط پلتفرم‌های متصل تعیین می‌شود و طلاکارت در این فرآیند نقش زیرساختی دارد.
🔹
طلاپرداز در مرحله نخست به‌صورت تدریجی در تهران و چند استان راه‌اندازی می‌شود و قرار است در ادامه، تعداد دستگاه‌ها و پوشش جغرافیایی آن افزایش پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682487" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8fdc35e9.mp4?token=UGAl404_Ydnc3dIn2W3UVpQKtkvTdYE9PFrLEGAtIeboDf3DofYGYMGLmP3VBKE8pEeFKa7QLDKidQMqP96Z9HYYuxUPluAVLLl57_XDrx4zZJJU48Qz-8uHkx_wSo8UuhW5NJKmuaXWmlPzSbJPg4sx1LQeP1DDdV2dEACpOXTH1T1OnDAXRSS8Zt2v7WHNITbY8BZNzxFErhzhVjVPCTU1f4gnF9-sP_1UcpnnCQ9UyiYWo-SKY-KOo2ReGmnVumrlpgD-mwAFGUWlrHEDRaVN8bszmPnz-layTrISHfBQNa0TePHg9pTxw7zp6LqGZxEy6MZhscRs3URjeX1WVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8fdc35e9.mp4?token=UGAl404_Ydnc3dIn2W3UVpQKtkvTdYE9PFrLEGAtIeboDf3DofYGYMGLmP3VBKE8pEeFKa7QLDKidQMqP96Z9HYYuxUPluAVLLl57_XDrx4zZJJU48Qz-8uHkx_wSo8UuhW5NJKmuaXWmlPzSbJPg4sx1LQeP1DDdV2dEACpOXTH1T1OnDAXRSS8Zt2v7WHNITbY8BZNzxFErhzhVjVPCTU1f4gnF9-sP_1UcpnnCQ9UyiYWo-SKY-KOo2ReGmnVumrlpgD-mwAFGUWlrHEDRaVN8bszmPnz-layTrISHfBQNa0TePHg9pTxw7zp6LqGZxEy6MZhscRs3URjeX1WVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ترفند ساده و کاربردی که جای کمدت رو دو برابر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/682486" target="_blank">📅 11:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_BS0cL5UHVon7qNmI8SbExyPRKBKBmANUjq9aQ5jVWRu-e7nYM80HvO55tL1tq-yZLq-EJYwfFm0bdNH3KwxCl3BkTj8H0xEsM3CBe5oRzkTSG_24yFBf269RO8hz8ZN02jufwBt7WashHD4TAo7Ch_cZzxB3FRf7WFFMnbJmgJ1vgkiXoZGquqJknqJlM_hhKsjfcLxdrZTYji5euMb68K7xT8UAtE3_AbLnBN6KGh3t5lPN4PO6T20Ae8154_E1U6uQIpWbvVp4Tq0FpSDybvchxc14DdDE8HQDEM2ZnlUrFcF9FcyFtNExe-OW1XlG3ineeo5MWFxY0-7v-xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنک یوگور، مجری آمریکایی: ترامپ اعلام کرد که تنگه هرمز باز است و پس از اینکه ما ایران را شکست دهیم، به‌زودی به قلمرو آمریکا تبدیل خواهد شد
🔹
تنها کسانی که او را باور می‌کنند، سالمندانی هستند که فاکس‌نیوز تماشا می‌کنند و همه افراد در وال‌استریت.
🔹
اما یک چیز درست است: او امیدش را از دست می‌دهد و برای ادامه جنگ بیشتر، موضع خود را سخت‌تر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682485" target="_blank">📅 11:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e00614052.mp4?token=EorqADlVoBbcJUILhS8j5Qq6TqLTgklohjALvmZdtMOBqNEAdCVoi_j-saAT6p144INuUWJdhjC00h_U6R8N2g52b8UTALH8rBo1L3mz4RSmd74jm5H8Kb2FlesVRvnDbyFOWX-iw7FKUJPI4Q6w8qvXU1UtGeOzW3bLeSH0CcRAuk49-DTG2zc7b9MKoqQv2UwMM-EVH-4A1ni58_3XpolnIvgkpGoz4ULPsYiiKecE0lVl67zFeWA1Ofdlhs0TFc1uycyAzUcj85-BZ1jnJHikF-EiBBe0vHDdGNV8HTF-H4sQR4TmfIHUsIeT5gxqW2Rpp4FMvPw_3ihLLd3C9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e00614052.mp4?token=EorqADlVoBbcJUILhS8j5Qq6TqLTgklohjALvmZdtMOBqNEAdCVoi_j-saAT6p144INuUWJdhjC00h_U6R8N2g52b8UTALH8rBo1L3mz4RSmd74jm5H8Kb2FlesVRvnDbyFOWX-iw7FKUJPI4Q6w8qvXU1UtGeOzW3bLeSH0CcRAuk49-DTG2zc7b9MKoqQv2UwMM-EVH-4A1ni58_3XpolnIvgkpGoz4ULPsYiiKecE0lVl67zFeWA1Ofdlhs0TFc1uycyAzUcj85-BZ1jnJHikF-EiBBe0vHDdGNV8HTF-H4sQR4TmfIHUsIeT5gxqW2Rpp4FMvPw_3ihLLd3C9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید آماده بود جان خود را فدای مردم کند
🔹
جورج گلووی، نماینده پیشین پارلمان بریتانیا در گفت‌وگو با پرس‌تی‌وی: خودداری رهبر شهید ایران از رفتن به پناهگاه‌، نشانه شجاعت و دلاوری او بود و جایگاه و اعتبار ایران را بیش از پیش تثبیت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/682484" target="_blank">📅 11:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی رئیس رسازمان زندان‌ها
🔹
اصغر جهانگیر رئیس سازمان بازرسی کل کشور
🔹
دانش رئیس مرکز حفاظت و اطلاعات قوه قضاییه
🔹
سلطانی معاون قضایی قوه قضاییه
🔹
امیری اصفهانی معاون اجتماعی…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682483" target="_blank">📅 11:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq4rpQThWlfNqJ59gUN9XMzwJ1GuCqzlu9yrXH0Ub0B3ulc4XyAS1oEFY0KWrITONmI4oGRfAtZTiI15Q0Ygljccr2H5VKhTme862qqjrw6X9HiiJJCR1EiC9eD5jvg9Ws1gqNfC22Q02bG14c4-Vk68OD8LCh_7DarxklJvSHEfdlWMCCUoKf4m03T6BoZ4fUWnE43fkkOcVP0t30oQ2VXFj7qhzSCGs23azPga5ubrePBg5e63nViRy7WztygBBejM2ozmn0oEhqSUqdXQHuIrLK7f6WBEGQjDBtbgNW4SQe2pXxOVew1BZSucmE1vSM6GkMomFzxqA4Xz18Vf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی؛ پاوربانک شیائومی + ایرپاد M10 هدیه
🔋
پاوربانک ۵۰۰۰ میلی‌آمپر شیائومی
🎧
ایرپاد بی‌سیم M10 با بلوتوث 5.0
⚡️
کیس ایرپاد با قابلیت پاوربانک اضطراری
💡
جمع‌وجور، کاربردی و مناسب سفر و استفاده روزمره
💰
قیمت: ۱,۶۹۸,۰۰۰ تومان
✅
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
🛒
خرید تلفنی
👇
https://memarket24.ir/product/fast/63564/180124/</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/682481" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc52a7296.mp4?token=gF0mDEm61yp_tBWxIb6Rmd_8CiS1apm-r6BF7ReDMH8ssblhRHjYk6LSeK8xxBmamqKbwVeEXXjXMLnUduPEuaDo3LV4LYgZMQ0y1aIOgUWVYK2oszIE6vzjnT7pbbZf6pfkrRZhZnZassAqEMD1i_po8oGh3zQO2f5Bh831nnZn3Q7gGtq8enOK6kYw4MqdFpRUUIDU9PoD_8Ppkf6B3Qr9Led1y1vZU94a-7-vubjryJosSXP3H1LG8u6acisfRIMkfOhanvqz6VGuktcDfbn2GyUPqMwbmsAzMoxRQ3KnJgcyIKdI7HScTpjMWZlMHguGrLPGmZzUBfl1efpo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc52a7296.mp4?token=gF0mDEm61yp_tBWxIb6Rmd_8CiS1apm-r6BF7ReDMH8ssblhRHjYk6LSeK8xxBmamqKbwVeEXXjXMLnUduPEuaDo3LV4LYgZMQ0y1aIOgUWVYK2oszIE6vzjnT7pbbZf6pfkrRZhZnZassAqEMD1i_po8oGh3zQO2f5Bh831nnZn3Q7gGtq8enOK6kYw4MqdFpRUUIDU9PoD_8Ppkf6B3Qr9Led1y1vZU94a-7-vubjryJosSXP3H1LG8u6acisfRIMkfOhanvqz6VGuktcDfbn2GyUPqMwbmsAzMoxRQ3KnJgcyIKdI7HScTpjMWZlMHguGrLPGmZzUBfl1efpo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری یک حیوان‌آزار در تالش
پلیس راهور فراجا:
🔹
پس‌از انتشار فیلمی در فضای مجازی که در آن یک خودرو در تالش اقدام به کشیدن یک سگ کرده بود، رانندهٔ خودرو به مراجع قضایی معرفی شد.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/682478" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682476">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی رئیس رسازمان زندان‌ها
🔹
اصغر جهانگیر رئیس سازمان بازرسی کل کشور
🔹
دانش رئیس مرکز حفاظت و اطلاعات قوه قضاییه
🔹
سلطانی معاون قضایی قوه قضاییه
🔹
امیری اصفهانی معاون اجتماعی و پیشگیری از وقوع جرم قوه قضاییه
🔹
حجت الاسلام سید محسن موسوی رئیس مرکز حل اختلاف
🔹
علی کاظمی سخنگوی قوه قضاییه
🔹
ذبیح‌الله خدائیان رئیس حوزه ریاست قوه قضاییه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/682476" target="_blank">📅 10:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پرداخت معوقات همسان‌سازی و افزایش حقوق‌ها از ۱۰ شهریور
سخنگوی کمیسیون اجتماعی مجلس:
🔹
وزیر کار از آغاز اجرای احکام همسان‌سازی از دهم شهریورماه خبر و قول داده تا معوقات حقوق بازنشستگان پرداخت و همسان‌سازی انجام می‌شود.
🔹
همچنین مقرر شده است مابه‌تفاوت افزایش حقوق فروردین و اردیبهشت‌ماه نیز به بازنشستگان پرداخت شود./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/682474" target="_blank">📅 10:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbwZ7s0erbqQZhkbJd2XdhlLPQ7jEzE1PUABVJnIU92tQyhFLSr2SjfwITmCADAbILQ96PqhACg91enX3-PysPkFi3fVq8-v_g_0mTrfrZoHGoFmPbOvZZtoZ2oLCFGvCXRq2OsS-qyf4bU9A9n1ZWfI5vr_TMWq0EK23pTBVgjWV-A75AK7Rytc3bM7wpR03YrrKhgXUi4W_JL8o0rB4SMTs9_fbW8u2PhxLLPFvwoBFppZ0TGtLYp7p_xUPZnuu33Rxm7yPv2gzKYmmq84q_h4CJhYt6d7v2mTQ8CUZ6IKGJWUxnncQlS3pESks6pFbPhwOl_dCYh47xNXVzC9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس رنگی شده، از شیراز؛ سال ۱۹۱۱ میلادی، هم‌زمان با پادشاهی احمدشاه قاجار
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/682473" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سازمان سنجش: همراه داشتن هرگونه وسیله شخصی در جلسه کنکور ممنوع است
🔹
ارائه كارت شركت در آزمون و همچنین اصل كارت ملی یا اصل شناسنامه عکس‌دار برای شركت در آزمون الزامی است.
🔹
فرایند برگزاری آزمون‌های صبح رأس‌ ساعت‌ ۷:۳۰ و آزمون‌های عصر راس ساعت ۱۵:۰۰ آغاز می‌شود و دربِ حوزه‌های امتحانی به ترتیب رأس‌ ساعت‌ ۷:۰۰ صبح و ۱۴:۳۰ عصر بسته خواهد شد.
🔹
متقاضیان از همراه آوردن وسایل اضافی از جمله مواد خوراکی و آشامیدنی، كیف دستی، ساك دستی، هرگونه دستگاه ارتباطی و الکترونیکی از قبیل پیجر، تلفن همراه حتی به صورت خاموش، تبلت، قلم نوری، ساعت هوشمند، دستبند هوشمند، انگشتر هوشمند، هندزفری، کیف، جزوه، كتاب، ماشین‌حساب، هرگونه یادداشت و نظایر آن و همچنین وسایل شخصی به جلسه آزمون اكیداً خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/682472" target="_blank">📅 10:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aom3qBl14wbT80_wb9Z0NKy3ruwSObRveZXtnEMSstxga1aDbwqkYiMnIysEp8ux7V8zU3HjoIbSb8oTGAfYiqQ287csLmbAUCsgb4oKfve2GA00RePNI-ZMrAZtsYVMuuxCyIsZvowXfpIPRs-jOkO1i4oD-RZwG4dPrPjaZF5zYSTsLdKpJdnnaTQlE0HMnJUYDBsV9NSOhzw7PAMhb1m8e6OnBqZCVOP1o6mB-yRwoNs5ujZsOWtIXIacneLoUQtzu2YCCyveU5oEH9KWhZSoN6p4zeiSSFqSp_5dV_eAEqbu8GilwHyyXPGkjl2Euq8F8FP1Bk-i2FOnXTaewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا فیلم جنجالی درباره زندگی امیر تتلو است؟ | راز شباهت عجیب امیر جدیدی به تتلو | شباهتی که نمی‌توان نادیده گرفت
🔹
از همان نخستین تصاویر و خبرها درباره فیلم «بیداد» به کارگردانی سهیل بیرقی، یک پرسش ثابت در حاشیه اثر تکرار شد: آیا این فیلم، روایت پنهان یا نیمه‌مستقیمی از زندگی امیر تتلو است؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238851</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/682471" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af4bc85d6.mp4?token=vVMIYoPeM2XSlp--U_jVS44BFJqTAcLoEvn6LYbSQbK8kbIJwbxbBQpvNOEKjO_6Wym0EIEF7_NyWmuelPR9sbZoLWFgmGn4aLVHchp2DYhnUmyC3G8BQItYy8VAWNjVCagln9pBOKj2lZU36vvOstNPq4DoMWEvGXb-VuJISBhThyV7poNxOTvZdIBocYy451b1SfR5ka0Ao2wO5xjTXkSknulxZBY-1mY6bcJRjcqfQEOOonwPm99udY9INNRcHIj4XcEtT1wQKFtbAfqXszIVrmcJy-GHl3LXSghZgNLkNyoQSATqd2tzBk0x4qI_RaGlggA8XS0D6j_1MRWHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af4bc85d6.mp4?token=vVMIYoPeM2XSlp--U_jVS44BFJqTAcLoEvn6LYbSQbK8kbIJwbxbBQpvNOEKjO_6Wym0EIEF7_NyWmuelPR9sbZoLWFgmGn4aLVHchp2DYhnUmyC3G8BQItYy8VAWNjVCagln9pBOKj2lZU36vvOstNPq4DoMWEvGXb-VuJISBhThyV7poNxOTvZdIBocYy451b1SfR5ka0Ao2wO5xjTXkSknulxZBY-1mY6bcJRjcqfQEOOonwPm99udY9INNRcHIj4XcEtT1wQKFtbAfqXszIVrmcJy-GHl3LXSghZgNLkNyoQSATqd2tzBk0x4qI_RaGlggA8XS0D6j_1MRWHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علم منتظر معجزه نمی‌ماند!
🔹
واکنش کودکی که با استفاده از عینک برای اولین بار مادرش را به وضوح می بیند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682470" target="_blank">📅 10:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
📊
عملکرد هشت ماهه منتهی به ۳۱ تیرماه ۱۴۰۵ بانک سرمایه در یک نگاه
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/682469" target="_blank">📅 10:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
امارات تمام مبادلات تجاری و مالی خود را با ایران تا اطلاع ثانوی متوقف کرد
ادعای آناتولی:
🔹
خبرگزاری دولتی امارات به نقل از مدیر ارتباطات استراتژیک وزارت خارجه گزارش داد که امارات تمام مبادلات تجاری و معاملات مالی با ایران را «تا اطلاع ثانوی» به حالت تعلیق درآورد.
🔹
هنوز جزئیات بیشتری فاش نشده است. با این حال، این اعلامیه پس از آن منتشر شد که وزارت دفاع امارات مدعی شد دو موشک بالستیک ایرانی را که ناوبری دریایی را هدف قرار داده بودند، شناسایی کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/682468" target="_blank">📅 10:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813058e1ec.mp4?token=fO8R1-iYkeN6JYt6WkJixrcDoEbHxXO_xsXyvEl8usoH8hv5CZk5kbLt6zM5LOK26vZcP00fixRMOC0JOZ9ippe7Nmh-szKRO8EyhPYdZn3vqhWdU-UIBnifGS98W3bmHbSqCFMHBKMDpYUX7SLkC7dL1lXuZn_ZjIOr4ekbcTHvT-wsUoe6t3rCmTheRR5artu0Kdo0m653ocDZfnnUyJvXI5ywnWMx1ISctglbppe6GeD2z2NnqraO8cXSAGzfNQYwn4FvRBgEGkmYC3JlY26wGZUoOay1_Gae6YsOJkhyOUXOjNHQVxdIjnLQxkPQfvRPtl9HhP6FfnSEWMsVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813058e1ec.mp4?token=fO8R1-iYkeN6JYt6WkJixrcDoEbHxXO_xsXyvEl8usoH8hv5CZk5kbLt6zM5LOK26vZcP00fixRMOC0JOZ9ippe7Nmh-szKRO8EyhPYdZn3vqhWdU-UIBnifGS98W3bmHbSqCFMHBKMDpYUX7SLkC7dL1lXuZn_ZjIOr4ekbcTHvT-wsUoe6t3rCmTheRR5artu0Kdo0m653ocDZfnnUyJvXI5ywnWMx1ISctglbppe6GeD2z2NnqraO8cXSAGzfNQYwn4FvRBgEGkmYC3JlY26wGZUoOay1_Gae6YsOJkhyOUXOjNHQVxdIjnLQxkPQfvRPtl9HhP6FfnSEWMsVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزه بهشتی این مرغ تا مدت‌ها از یادتون نمی‌ره
😍
مواد لازم:
🔹
پیاز خلالی ۱ عدد نسبتا بزرگ
🔹
رب گوجه ۱ قاشق غذاخوری
🔹
رب انار ۲ قاشق غذاخوری پر
🔹
الو‌خورشتی چند‌ عدد
🔹
زرشک۲ قاشق غذاخوری
🔹
زعفران دم کرده به‌میزان لازم
🔹
آب نصف لیوان
🔹
ادویه‌ها نمک، زردچوبه، فلفل سیاه…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682463" target="_blank">📅 10:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682461">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4508f1e662.mp4?token=HebFdvHvgNcTb4o5evnaN36sjqur2lom7m4_J9YZPfW6mFGB3FyrFJWd_6i6sL2Dm3AnF8b8DbPaNEJL29-uiNYOItn2bfkDR3N8U5fxEnEI9nU7mj7Oni0ywhHbJL1oivxK_GOobmcrpbFhRUM8WC13Haf-glDYvwgXzt9X4pZ6Iru7USu5LvoqqixmJcEpTvfUdJ-9C5fSJpMoIDxFAC07bMJhGLNwBh5XX14xr93EkAg-iK7yWvV-kX04MyezctHoWORjHK0f3Zgh1EktLA6DYU4pmqbyh4z7WW9yrzK4B_pEuYAalyoXynTvYxFGlN-i-vT6Fuw3OuwuqBk-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4508f1e662.mp4?token=HebFdvHvgNcTb4o5evnaN36sjqur2lom7m4_J9YZPfW6mFGB3FyrFJWd_6i6sL2Dm3AnF8b8DbPaNEJL29-uiNYOItn2bfkDR3N8U5fxEnEI9nU7mj7Oni0ywhHbJL1oivxK_GOobmcrpbFhRUM8WC13Haf-glDYvwgXzt9X4pZ6Iru7USu5LvoqqixmJcEpTvfUdJ-9C5fSJpMoIDxFAC07bMJhGLNwBh5XX14xr93EkAg-iK7yWvV-kX04MyezctHoWORjHK0f3Zgh1EktLA6DYU4pmqbyh4z7WW9yrzK4B_pEuYAalyoXynTvYxFGlN-i-vT6Fuw3OuwuqBk-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد مرگبار کامیون با پل عابر در برزیل
🔹
دو سرنشین این خودرو، یک زن ۶۳ ساله و پسر ۴۰ ساله‌اش، جان خود را از دست دادند. یک نفر دیگر نیز به‌شدت زخمی و برای درمان به بیمارستان منتقل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/682461" target="_blank">📅 09:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682460">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe079e89c.mp4?token=FmFvix1UwGurDLE36OHzzcCJsPzFg_Ch_er97XDIiKC_bB3ClJvFGIw-oeb6S_E3ftxGEi75naDi4H2KgIIbxEHyMusxOXi-UPanpTjhvIyjnBVTB5LIEyVpFGGqi-pF3VxoGUSkybm89riL1LH1dmvK7aai3xNF1qWmxYKqv_zZwnEdFUX5bdZxhXkzlABKWvSWj7A11iQ0GyH-JmLOUJFyBMAmOhfLmFqZYI8yC69z2MbJHzhfnkGnXAIDf3r2BvIJ8oClAM5Vf2HZKyX1gjGjYWogEWL1BdWgqcTC5vJPlvK44HZxFTErJYm0_WNaAHoTMdXqNEzA1D-JTl__MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe079e89c.mp4?token=FmFvix1UwGurDLE36OHzzcCJsPzFg_Ch_er97XDIiKC_bB3ClJvFGIw-oeb6S_E3ftxGEi75naDi4H2KgIIbxEHyMusxOXi-UPanpTjhvIyjnBVTB5LIEyVpFGGqi-pF3VxoGUSkybm89riL1LH1dmvK7aai3xNF1qWmxYKqv_zZwnEdFUX5bdZxhXkzlABKWvSWj7A11iQ0GyH-JmLOUJFyBMAmOhfLmFqZYI8yC69z2MbJHzhfnkGnXAIDf3r2BvIJ8oClAM5Vf2HZKyX1gjGjYWogEWL1BdWgqcTC5vJPlvK44HZxFTErJYm0_WNaAHoTMdXqNEzA1D-JTl__MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» اینجاست!
🔹
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682460" target="_blank">📅 09:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682459">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=OOU9Zdj7BqkS-kjG5wnpFWJuZsoEGXksxHG7ZvYRvM2TSjiUZeYgQXVQj7Im6SLdmaDd35ERfSI_1eADsP_9q1yWir4VxS82eIcIXMcIH_flwAHtpzMBS9Y5C8ptkoMw0CMH45M9J3512vIpmPgBgjlsrqvr9MDAibKYF-HdQcCA3UWXt03FpCTSfnZqwfzK5YlzYnelavT8KdkNzNifAEamnNn1pkuY06rufzLJ1oes-Ayu6HenSyBbrpR7edGdvc1HaSGgdJIiU3a_KLCOa1rtdDvD3XYHLjpft2NBRtCVWSwNbbdojtrsAEnDzH5-yZEFtfh-Od6_r3DV87hCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=OOU9Zdj7BqkS-kjG5wnpFWJuZsoEGXksxHG7ZvYRvM2TSjiUZeYgQXVQj7Im6SLdmaDd35ERfSI_1eADsP_9q1yWir4VxS82eIcIXMcIH_flwAHtpzMBS9Y5C8ptkoMw0CMH45M9J3512vIpmPgBgjlsrqvr9MDAibKYF-HdQcCA3UWXt03FpCTSfnZqwfzK5YlzYnelavT8KdkNzNifAEamnNn1pkuY06rufzLJ1oes-Ayu6HenSyBbrpR7edGdvc1HaSGgdJIiU3a_KLCOa1rtdDvD3XYHLjpft2NBRtCVWSwNbbdojtrsAEnDzH5-yZEFtfh-Od6_r3DV87hCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
در جنگ رمضان قدرت مقاومت ایران را درک کردند/مقاومت از مرزهای ایران و عراق و منطقه فراتر رفته و جهانی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682459" target="_blank">📅 09:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51d81de95.mp4?token=BIF2Ym-fY7asDG1u5csqfnSebxyNQzb-1N-PS2MqL5k0KbSDvE1K7DcQAdAh7A2x8PmJjB3L0YKjc-EegVmi9rUv5SGc_z-nqdXkqFrt4J9PaOP4OqM59kHOF_WeZDsc3e-rvf1DPy5wBLdFX0VARgn_nsY_9UjnchxXRbNRmVPiNOmzs4EKQEVfOnTsOu-IYagp_WF-INcN-asN_6QR19kDxiDmWNA9k49ZfmQfxolYbnEsL4ytf1a2PLbuB_M5Zu8qOKlPGGXcWoNJLnnlXfCdM0izkmpGYSMtCZCpm7ZCJXhAtL2VV27DFNtxmxQOxmwtarD3CNyrXGrrP3PPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51d81de95.mp4?token=BIF2Ym-fY7asDG1u5csqfnSebxyNQzb-1N-PS2MqL5k0KbSDvE1K7DcQAdAh7A2x8PmJjB3L0YKjc-EegVmi9rUv5SGc_z-nqdXkqFrt4J9PaOP4OqM59kHOF_WeZDsc3e-rvf1DPy5wBLdFX0VARgn_nsY_9UjnchxXRbNRmVPiNOmzs4EKQEVfOnTsOu-IYagp_WF-INcN-asN_6QR19kDxiDmWNA9k49ZfmQfxolYbnEsL4ytf1a2PLbuB_M5Zu8qOKlPGGXcWoNJLnnlXfCdM0izkmpGYSMtCZCpm7ZCJXhAtL2VV27DFNtxmxQOxmwtarD3CNyrXGrrP3PPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای تماشایی زمین از دوربین فالکون ۹ اسپیس‌ایکس
🔹
در این تصویر، زمین مانند تیله‌ای آبی در دل تاریکی فضا دیده می‌شود؛ قاره آفریقا و توده‌های سفید ابرها نیز به‌وضوح قابل تشخیص‌اند.
🔹
این نما در فاصله‌ای حدود ۳۶ هزار کیلومتری از زمین ثبت شده و یکی از تصاویر چشمگیر واقعی از سیاره ما در فضاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/682458" target="_blank">📅 09:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئیس سازمان سنجش: نتایج اولیه کنکور در شهریور ماه و نتایج نهایی در نیمه دوم آبان‌ماه اعلام می‌شود./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/682456" target="_blank">📅 09:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv9dDI1IBtl-nVIWPq4I05UV3sXkpHOtvi_DqU9mJDMN-3dTxKAAnndJpeY9mstrhfDroE1rZRK2EhJqBgpfc_onicLsv3lptL0C55O1KRxnN6LICcbnWf6dWsqOOoZffAOYkdXu4o-iYYrNp2k3ewr4qZehGDG976CxWgOPUrZlqvoNGrTPMtDV1heXH_bX0b8lvCYOnTYx5mDhZZtfTrm_NVZf_ukURpzJh0DaKyYmy_9htZkBWwaFbLUDmUw1GsOXSf3gkEmm3r3srIDCW_PI90PfzAVe_E6d8kek5WRoJkCI2VyCIsN6t_Y-e2w6BDRc0IdWGwNb2MmmtO4Dmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس ستاد کل نیروهای مسلح در خصوص کمک به ارتش متجاوز آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682453" target="_blank">📅 09:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
مزایای رفاهی کارگران معاف از مالیات شد
🔹
با رأی هیأت عمومی دیوان عدالت اداری، امور رفاهی و انگیزشی شامل (حق مسکن، بن ارزاق کارگری، حق اولاد، حق تأهل، هزینه ایاب و ذهاب، پاداش افزایش تولید و ... ) از پرداخت مالیات معاف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/682451" target="_blank">📅 08:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCZpsJNzKQI4vfZONXwP_kVLPQOErThnf0oPTfHvlUXDFTCmnv71K8RdSIKrHoMdETCWecRPo9ZwDAO_rrXna5QFf3UDVRXaHhY1ptxrsmHvaXGXPEbUfHTkE8ytb3TD-DtQwqHyHWPIf_3viemOnKJCNXit2CytBlMVYa-X8f8TWpvmUkzbXSORs8Stq_f_cStvN0XuGE5GV3lSGQpBQr_PiW0v-I3Rcdu3Xnltm-qQxlcl6N4twGlDTgi4SZxehf_bpwuk-vd5ZH4cudXAoSe2a50xHTG_OKLs6hnTgdw6yl3NRiCIQgst_9PPDWaFoJqQdYxlY0me_T9Q1XWVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtH3p7D2Nza2H44NucsFZzIuwp7q2K-8Ufky760xItZn36YPvlXyEmMs51scKEolW0Bd3Mniab69-0uIUCtXeyRZntNxJDqG-IOuEDa7LUgpa0__OkDIHJYvtiqZffvHP0-VDTFkXFc782aJALojHZXppeXVntWTLRWG-zgM11Zcy3uVflYXJRJA8ffcDfQSyaSpetXwDLpBLBVo0GI1JRDoGpECQxTNGxSDrNYI4vPzOPODvTcs0CYsEDRyRQqesAToH3SnlK-sbONc73mlTu3Yfx7I9ziRhmqOcmpSFd8R4VyDOFpxoHP0E64TBIhGH2roE5k1zp93oNX7F-7saw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام ایرانی اولین عکس «سلفی» را ثبت کرد؟
🔹
۱۹ آگوست (مصادف با ۲۸ مردادماه) در تقویم بسیاری از کشورهای جهان به عنوان روز جهانی عکاسی نام‌گذاری شده است.
🔹
برخی از اسناد تاریخی می‌گویند که نخستین عکس خودنگار ایران را ناصرالدین شاه قاجار با قرار دادن دوربین سه‌پایه مقابل آینه و ثبت تصویر خود و زنان حرمسرا گرفته است.
🔹
برخی هم نخستین عکس خودنگار ایران را به تصویری از ملک قاسم میرزا نسبت می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682448" target="_blank">📅 08:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
انحصار وراثت غیرحضوری و خودکار شد
🔹
ازین‌پس، برای متوفیانی که تاریخ ثبت فوت آن‌ها بعد از سوم مرداد ۱۴۰۴ باشد، نیازی به اقدام از سوی ذی‌نفعان برای صدور گواهی انحصار وراثت نیست و گواهی به‌صورت خودکار و حداکثر ظرف ۲۰ روز صادر می‌شود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682447" target="_blank">📅 08:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxtcBGFBTwd2BAwYIlXcpWZtxJVj9DrBlQtE0TXEv9iYhB1N_9z2higHj7qOfOqjnmn10ggyoYHomjijKPoYUE9ujUXLgTo07IkOArVN7_ICFA_c5bAsg-1dpRmI8tOKxqzpIOPKgHzrfsuW09akI7pkhkzXhiurUPh9BLPxFsm4hck10sKlsTGev4QNfYBr_7VXdp25uzjCjy9o4b5iK9fQQNjeV9eOR_ozbjBwayfB_9EFmZLOuSexvzCxGOfmy4WI02G5HwQlL2HqKNlF07DGDBJmaohgWYRk97MQbEJFbcU13I6SgE7FAopycrHDofHzFabIT9c5BaTc2xHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاج ابو الاء الولائی: نفت عراق به فروش می‌رسد اما عراق نمی‌تواند از آن استفاده کند
دبیرکل کتائب سیدالشهداء:
🔹
نفت عراق فروخته می‌شود اما آمریکا اجازه استفاده از آن را نمی‌دهد و آسمان ما نیز اشغال شده است.
🔹
آمریکا نمی‌گذارد برق از ایران یا ترکیه بخریم یا با چین و زیمنس قرارداد ببندیم؛ مصداق "نه می‌دهم و نه اجازه رحمت می‌دهم".
🔹
استقلال کامل عراق کجاست ای بزرگان؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/682446" target="_blank">📅 08:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های دلاری دولت، این رقم کفاف همۀ مخارج ارزی دولت از تیر تا دی‌ماه امسال را پشتیبانی می‌کند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682443" target="_blank">📅 08:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
امکان ترمیم سابقه تحصیلی از امروز
وزارت آموزش و پرورش:
🔹
متقاضیان ترمیم سابقه تحصیلی سال ۱۴۰۵ می‌توانند از امروز (۲۸ تا ۳۰ مردادماه)، پیش از اعلام نتایج آزمون‌های نهایی، انصراف خود را در سامانه ثبت کنند.
🔹
ثبت انصراف در همان سامانه ثبت‌نام ایجاد و ترمیم سابقه تحصیلی و از طریق درگاه سنجش انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682442" target="_blank">📅 08:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0838610e95.mp4?token=bXtreO7jI5jTQr04x2Q2VSHG0yqaxr72B5PWXfgFghIhxW8PjRkOVPcvUijRedaBpTP_96CBMJb_kq3Ot_Q6revUsUrhZVsP0cNye8wUnBGHe99ycM1nUSnu1I3kxucwF7PfN4evHE_O4GLgzF8UccRx7q-muFZAY7lTKu6SdjoLwsG7_4vQ4OmqLMXJ8LdK99hHpa8jH2zmIfItz7h1C31-Pr2cqEgxGR8_2X9wQoZbgOr34of5oLByjP0XIGSQWL12bTMIDQ8-BlaHqvSc2ZPBikWE4FK61vUBYn0PI5U6fQebSRsrZOVOys8bIwocKymiC4Vs0ToaxmrXlipBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0838610e95.mp4?token=bXtreO7jI5jTQr04x2Q2VSHG0yqaxr72B5PWXfgFghIhxW8PjRkOVPcvUijRedaBpTP_96CBMJb_kq3Ot_Q6revUsUrhZVsP0cNye8wUnBGHe99ycM1nUSnu1I3kxucwF7PfN4evHE_O4GLgzF8UccRx7q-muFZAY7lTKu6SdjoLwsG7_4vQ4OmqLMXJ8LdK99hHpa8jH2zmIfItz7h1C31-Pr2cqEgxGR8_2X9wQoZbgOr34of5oLByjP0XIGSQWL12bTMIDQ8-BlaHqvSc2ZPBikWE4FK61vUBYn0PI5U6fQebSRsrZOVOys8bIwocKymiC4Vs0ToaxmrXlipBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک کش پیلاتس تمرین موثر برای پایین‌تنه و تقویت عضلات رو شروع کن  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/682441" target="_blank">📅 08:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcAHESzcXbfLr36gXYRa2JDBJioveO-Cfi-sFjsfxh_QwsRCTfUnPaiL0MpubFMVHkFEeGl7PdmhjbKkf6fDlnQjHUyjdYNSJJ6cnQGw25B8T1jOAGSWw70wxEW-uB6G5RitorbfcAy6Bt74eeXICVB7FNwq8frO2z29UD4NqLhUxsTAE7p1XC1Rp3sTszLUViBwnnzqJfMkwdWIMiiOOI7xetOqku2dbKEwFsnf7xD1j_7lo-1n5gLaQzlW5z2kjOHsdEt94-PlPGgCbRZjQMvSNb_44edFswHx_lFa9r1duqvIv5v4QrAbBf5zTid_lM5OYhPAWxfVHW7LRGlUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش توقیفی امارات در راه بندرعباس
🔹
نفتکش توقیف شدۀ اماراتی که در کریدور شمالی تنگۀ هرمز توقیف شده بود، به سمت بندرعباس تغییر مسیر داد.
🔹
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/682440" target="_blank">📅 07:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5HELbead846-TWh9TJzp0JUkhSBvIIxSUhiIEoZs3pG84vJMY9zSQPz9HBAP3jbLvbLGTshA4_EgULijGw5vO_FNFM7qn_C8PdK511k9OczmBdrufSJAFjJrIaBnS9ow0YMSCpIa5Pb1nhzLruejD5vLT4dWzfDzrVSagSe5Gpe9RqPocQhJOqWhzWVQ6spwyh53jt7AScWp9qea4COy0JxC6gJFOCFJlbGIO1hI3IvIZmGB18pUoK4n9D7NhNAXrqbTOi96g_y1qfbPAMbUELoYl16zOxJ-PfBiGX81d1lbh86vikO_EMb-vDOz27BVicjdnpiV53FdE1ldE9ccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۸ مرداد ماه
۶ ربیع‌الأول ۱۴۴۸
۱۹ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/682433" target="_blank">📅 07:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0v7kDK8d5zpsiIw2GaKpXBgfp24vvBiPqvqzipHdsZQ6G6pvYOtPhCzKq94lXRRGDe5pbAdz0Sr-HtWAW-4kFWxuJC9l58IEYLXzxBFJHxglQ-UEXWGLmcwZovBjjczvZpkCKNJBKve-DvFapDf_Vn7a-RcjOfi3qYHI9JJn25LB9SfYu0PfJxVSdQdreKAlvDtTLmUYCrRcEe2GMu4btLKlQFMclarrhPRy0VF_5VFwM4cgrt88LIVe3hXKKF0RL07Xq9VmYjqZwYYJIJn6tt4Z9smxoLkJC40PdVt7L1TTlySHzR4d13pXB6LojDWDuF4XfGbnVtjiuVf5iAe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی بزرگ ارکیده شاپ شروع شد!
🎉
این بار خرید از ارکیده شاپ می‌تونه براتون فقط به معنی خرید نباشه؛
شانس برنده شدن ۳ جایزه جذاب
رو هم دارید!
😍
🎁
🏆
جوایز قرعه‌کشی:
😍
👇
🥇
کرلی شیگلم | ۹,۵۰۰,۰۰۰ تومان
🥈
شیور صورت و بدن شیگلم | ۸,۳۰۰,۰۰۰ تومان
🥉
سشوار روونتا | ۷,۰۰۰,۰۰۰ تومان
🛍️
خرید کنید و شانس خودتون رو امتحان کنید؛ شاید برنده این ماه شما باشید!
💜
📌
ارکیده شاپ | انتخاب مطمئن برای خانه و آشپزخانه
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/682432" target="_blank">📅 02:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vsh7F22ywyRxuB3JqzHQTAng8w9irNvMnGd45pGfrH1MhqA4rkfcZBVmIl4gpZ-vWWM2amPCxD-33kZ_8wUM0DvgzN_S65H4pyeR76on1z2231_cAaxcv6jUFN4BzYEYvguH_6aqjwILsHyjGakgcIJz8NtPMlAw1Y-cqUaoh83xdT-NTMqD9SLNSYPrrTVqkgcnDOFR0A6GlPwUY8bn1JcqyKqbXJ1YlK-joUBIJ6PJwOMl_NcvtTJzKzKGPktegEoL68K_n3DEmCZgdzbR7Yr17ifOzP5-uwzcUd83grVJnet7kUT6JtMg1jKtAfrpolAb3151mSzWi7heJxaL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3Q_b52eUXlVkNZhmuhSLNE4o2HFxvikyWky5k-5CTJ20uOifEHd_qHiTlL2ssq7TiRAmrLRU0KzWllsFr2uCEpTZqeBbEOUSwCZH1g_17kZLl05Q7Zrku1pf_klk4YnKrxxjI2Ocyi3LibYKT95LdJI7eDq6-g2jN2e67B4uEYjwrk-2XXFHm2iHrfxLUYKku-A_4hXczMATB1lW2Nh_wrV6rGwtt1Ln8Rio8u19i-5-WIfBbgftppOqcPBDiAQpcMMujuXRslAvivxXniljY5xuQEN73kOaXlvcH3JpK8bQIRui2dv9Bze5tEA-_Soc9o5pT4quYDWdYjuzU8k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WenJgxIYGemhmqSeSMiPQu3LQMpi_L0tOaz0HidaTIPZwQp37WffRPIbds_ikel2zyuOceIOC_CEP674bxplBW1TWqcBH1XqFmQOICCHbPwFczZMzwcK6EHCyYlGZ2YXUt2gA5IrADF3OJLqWV2TxAGoAOv0faVLbbhY6Cr3v9uufUCA4NZqGK180giMfzBIRgdSbaJoUNDvtIHtRVSdbv9XI8UMiluLM8BV2odeqvmzt6_a-5ThsNF19HyGZ6vAGUwThTgezX-3OFkfdps0ph51yI3JntHD1u1NEE7gIE1O5_SeKyFWln-Rj1YNG0BIux50-GxEn5ALBNA4ADaKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd86yd0rL4iEU4kIm-LhR-xYY3uVzhQGXJu76akRrBfBkWZlGDBU7r_jjgKUghEqkIrGHdWqov3v6BKtmK_5mYb-vOnpPYimfOpzhkERQFrqPjC_CEUDlRe0lH56o74XlKFKTkzo37qLTTXHsEonhy0wwPJgzl2feYRa0aINJ8erNaglFsNnO1oTH0F4YnCS8KOOnuMfMNyVRJuRmxpp_aMYNHjAJq6uf88dlr867yEeOzOpRau1cRUGB1FcWBQCDCmJgiQ1ucahBE-KD6TgIucB8U73Pgb6iK_1gU5yubBTYXeS2a4gwb1L0UJSNbM_FAFe7HQ5b7qGMo_UpOKY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5b3epq1YSrS_fZF4CJwYOxrE39AQtQioE5CC56JRr4x5-U4sD9e_0tHw-OgHuKifLKPej4_NpKOp_LVm3r8WXOGDvv80co-yH5gUeBmj9gYi5X7rOlteUbZZAYu4PS0Su1niGYRuzJYIrcsjOaZ-DSaPQPI9ATiSnZ999ZFPGRtVjGk7obIUR9lHQg6j-XG1SXp3XWiehbuTZEOHWBleiNilJ785iPVDTh2BQdrY0BErnKyUXY1BQb3vG0KKdqxjdom1Td9yJd4RiEo9Axyn2S_nD42TrQ8a4LYlM0-UyHg5N7u8-t2YyZPbp2CcW7uGL4QGQmxEO7C4_OpjJ6qlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ سلاحی که واشنگتن دیگر به اندازه کافی ندارد
🔹
برای سردمداران آمریکا باورنکردنی بود که جنگ با ایران این‌گونه ذخایر نظامی آنها را تخلیه کند.
🔹
حالا همین داده‌هایی که در این اسلایدها می‌بینید به مهمترین نگرانی کاخ سفید تبدیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/682421" target="_blank">📅 01:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682418">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_cgjt2bSWTtL0DA8n6J5v0NlRKIkhgo3m6e03A8twVsxjNfRqxbvXZ5lIqspBrxI4IKB9zfk4BSYWXtBWRCBrptmE8HDG9FdKb8AWZbIJmVrieHF210KZZ0SS30GyvVtxHbKPvywjYOyYdqHPhLgzcO2FF3XndVuuQDjwWUAwk0O_KOaGUbrjwJJ4Rch-7bUs3YOU6eR4j1A3stAzNlt-sw4lHxjycA7hPS9IFoDfjOoT7dIVkK0pi3SEsS4a2q6G3fGXatu1my9yVGroFUttj8yD8HN5vRU_J_k0RnOSg5OuvMJyklFfZFQjeDY3rtLuFQt6QCPpbpdUR6RJhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوتیوب شمارش بازدیدهای ویدئو را زیر و رو کرد
🔹
از ۲۴ آگوست (۲ شهریور)، یوتیوب روش جدیدی برای شمارش بازدید در نظر گرفته است؛ از این به بعد همین که کاربر یک ویدیو را پخش کند، یک بازدید ثبت می‌شود و دیگر لازم نیست چند ثانیه از ویدیو بگذرد تا ویو محاسبه شود.
🔹
این سیستم که پیش‌تر فقط برای YouTube Shorts استفاده می‌شد، حالا برای تمام محتواها؛ از ویدیوهای طولانی گرفته تا لایوها اعمال شده است؛ درست مشابه روشی که تیک‌تاک و اینستاگرام استفاده می‌کنند.
🔹
یوتیوب برای محاسبه درآمد همچنان از معیار قبلی استفاده می‌کند. یعنی از این به بعد ممکن است یک ویدیو ویوهای بیشتری نشان دهد، اما این به معنی درآمد بیشتر نیست/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/682418" target="_blank">📅 01:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59505881fa.mp4?token=AoVKTCt6lm_3qpBTg21orBwa5CF-_i6P7L0f1t2uGIdrQNSk_OvFeitPfVngFoK0sQ1HUQ4t26MJpNpn7KvPmrj0CYc7UkqucDF3sbIeBhR1wzUmJtm3zmtoquzPdbjDB34T9KTRJbulUFvPf5_meHaM3UPUZTXN66Gb9EWJIY9BDAIoGXaaO1aDY3PwpUpqbpfKPEnH6-TncC1LPzNMxok1Bchprnpd-yAJXIQM4Coi2B6xHiyZBkhHYF3yhj2kwVbW9p5dbPRCOoMvgh1J9K1fZiqu5DPCthX7z6VTqEmtnqvjohUSII2DPSuyqY8a8CsoY1wa5ZYhjf_-p8YloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59505881fa.mp4?token=AoVKTCt6lm_3qpBTg21orBwa5CF-_i6P7L0f1t2uGIdrQNSk_OvFeitPfVngFoK0sQ1HUQ4t26MJpNpn7KvPmrj0CYc7UkqucDF3sbIeBhR1wzUmJtm3zmtoquzPdbjDB34T9KTRJbulUFvPf5_meHaM3UPUZTXN66Gb9EWJIY9BDAIoGXaaO1aDY3PwpUpqbpfKPEnH6-TncC1LPzNMxok1Bchprnpd-yAJXIQM4Coi2B6xHiyZBkhHYF3yhj2kwVbW9p5dbPRCOoMvgh1J9K1fZiqu5DPCthX7z6VTqEmtnqvjohUSII2DPSuyqY8a8CsoY1wa5ZYhjf_-p8YloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمریناتی ساده برای تقویت و هماهنگی چشم و دست، تمرکز و سرعت واکنش ذهنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/682415" target="_blank">📅 01:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682414">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMl9v39cAw7wO9VcRW061XFgfHPYKRSy00GCmCRG1QUDYKowfJCDeCMItQxQdeo5NO-9KyDkj1Gb1mJ5x5wOAHtv7j4Co4V43fntdtmNdNSIyOm8AXP7_mkZOFU0lVORWOfw8mq4A-dVgS7x7Xy_ofAjQIASlC_KgFwpEtxlvJh-Cq6fdttY1Fv5pXT9lWpkquCXV1yhaAkQHjEm9o7100ksSQgYOjsSmP0aT-eXSKZ1GoIimeqAV17NJ3MHQwt9iRv6I67kIcoaGsbs1utOfovToIcpKH1IXoFGW64dYZs0C7OFTUxQ4Vd9V7e_mXhBD1kz2X9fFdkSK78_y6NUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: هنوز لباس ترامپ بوی آشغال غذای هواپیما می‌دهد آن‌وقت ادعای تصاحب تنگه هرمز را می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/682414" target="_blank">📅 01:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخیره استراتژیک ۷۳۵ قلم داروی حیاتی در کشور
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
۷۳۵ قلم داروی حیاتی و ضروری برای ذخیره استراتژیک انتخاب شده که حدود ۲۴ همت برای تامین آن‌ها اختصاص یافته است.
🔹
بخشی از کمبودهای فعلی دارو ریشه در مشکلات انتقال ارز در ۴ تا ۵ ماه گذشته دارد.
🔹
هند در تامین دارو همکاری مناسبی داشته، اما محدودیت‌های دریایی و هوایی، انتقال برخی محموله‌های دارویی از هند به ایران را با مشکل مواجه کرده است.
🔹
۵۸ نوع شیرخشک، از جمله انواع مورد نیاز بیماران خاص، در ذخایر استراتژیک قرار گرفته است.
🔹
شهروندان برای پیگیری مشکلات دارویی می‌توانند با سامانه ۱۹۰ تماس بگیرند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/682413" target="_blank">📅 01:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae15cbe36.mp4?token=jnEGFiKxX5IBqKG4OSs9JnjX9i7tABRuKzXuFZXA0BkGUYmPicwweFPpOZQQZ8nMcfBCGz1c3qprWgdjtB2fgdYQ7nontDlh6fuCwTdg5g_zEPF1y5oQRdOWmfFphr23vLLyGpbwh7w_tNpr7JgSz0UznsR4kdwpZ4VPou6fDldbhQLolCbl8GK69JBwg_x8ehUG1dtgzF1tHncZ2rzUkuWjtNkBSMsexR8IpsVYhEUt_gDVgU98A2bjy8lY4WVK2oeQrf3XKSLunFDKhM8xXt0UaKCm5IK7jID3E_36Qv0IBwO6VetCYsPI9zwaIJ3EzPm2n-a5k92wHTGunrflig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae15cbe36.mp4?token=jnEGFiKxX5IBqKG4OSs9JnjX9i7tABRuKzXuFZXA0BkGUYmPicwweFPpOZQQZ8nMcfBCGz1c3qprWgdjtB2fgdYQ7nontDlh6fuCwTdg5g_zEPF1y5oQRdOWmfFphr23vLLyGpbwh7w_tNpr7JgSz0UznsR4kdwpZ4VPou6fDldbhQLolCbl8GK69JBwg_x8ehUG1dtgzF1tHncZ2rzUkuWjtNkBSMsexR8IpsVYhEUt_gDVgU98A2bjy8lY4WVK2oeQrf3XKSLunFDKhM8xXt0UaKCm5IK7jID3E_36Qv0IBwO6VetCYsPI9zwaIJ3EzPm2n-a5k92wHTGunrflig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی یک ویدیوی آموزشی؛ ۳۷ میلیون بازدید برای درس موز یک معلم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/682410" target="_blank">📅 00:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
وزارت خارجه امارات: تا اطلاع ثانوی، تمام مبادلات تجاری و تراکنش‌های مالی با ایران متوقف شد/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/682409" target="_blank">📅 00:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت نیرو: خاموشی‌های خانگی تا دوهفته دیگر به حداقل می‌رسد
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
با توجه به شرایط فعلی و آسیب‌دیدگی بخشی از نیروگاه‌های کشور، خودمان را مکلف می‌دانیم برق صنایع را به شکل مطلوب تامین کنیم.
🔹
محدودیت‌های برق در بخش خانگی احتمالا تا دو هفته آینده به حداقل مقدار  می‌رسد، اما در بخش صنعتی همچنان محدودیت‌هایی را خواهیم داشت.
🔹
سازوکاری برای تامین برق صنایع فراهم شده و مشترکان صنعتی می‌توانند در شهریورماه، با خرید برق آزاد تا سقف تعیین‌شده از طریق تابلوهای برق آزاد و برق سبز و همچنین گواهی‌های صرفه‌، برق مورد نیاز خود را تامین کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/682408" target="_blank">📅 00:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQkXCXnFVvRj_F4x2GnB_YVh3kOnZdvt0x3svuVjKtJa7YiQSSyC3fJCEBQmtqSWU0h2kXCI0rFVynfxhZj9qsXqOivkgohkS6xXbL8hwHuN4n5oGDTvEbt_iBv-OTFh57091elHdnHVDCUwjmeFoQd401U3keszlL-jtX2s41sJUVSLR2fKEfcSYx0ut5gdBN5Y3lgYfwisq450t6VcHhiPcCAzWCfvKMqLZw6Tl2arokaD72F7o_0NkoYvF0qfV3dcrB7g2D6ynMJfba9pDs_vhcXYzYOq9FO2TOtscJOFQPYn1FP_rH8C9axBj7klOFFqsDjDqwnk-9NeIrAPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواستفاده از رنج مردم در اینترنشنال؛ اینبار بیماران پروانه‌ای
🔹
شبکه اینترنشنال پس از پوشش اخبار مربوط به حملات به زیرساخت‌های برق ایران، اکنون گزارش‌هایی را درباره وضعیت بیماران پروانه‌ای و تأثیر قطعی برق بر سلامت آن‌ها منتشر کرده است. اما جای سؤال اینجاست که دلسوزیِ امروز این شبکه، با توجیه بمباران نیروگاه‌ها در دیروز چه سازگاری دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/682407" target="_blank">📅 00:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سی ان ان: ترامپ استراتژی خود در قبال ایران را تغییر داده و به فشار بلندمدت متمایل شده است
سی ان ان:
🔹
ترامپ به نمایندگان ارشد خود دستور داده است که مذاکرات با ایران را متوقف کنند، که نشان دهنده تغییری عمده در استراتژی اوست.
🔹
کاخ سفید از تلاش برای تحت فشار قرار دادن ایران در بازه کوتاه مدت فاصله گرفته و به سمت تلاش بلندمدت‌تر برای خفه کردن تهران از طریق فشار اقتصادی و نظامی مداوم حرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/682406" target="_blank">📅 00:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
با فروش مهمانسراهای سازمانی کسری بودجه دولت صفر می‌شود! / حاجی‌بازاری یارانه می‌گیرد و می‌گوید «آقای احمدی نژاد گفته پول امام زمان است»
مهدی پازوکی، اقتصاددان در
#گفت‌وگو
با خبرفوری:
🔹
۳۱ استانداری و دانشگاه‌های علوم پزشکی در تهران مهمانسرا و ساختمان‌هایی دارند که نگهداری‌شان هزینه‌زاست و گاهی به محل اقامت بستگان مسئولان تبدیل می‌شوند. اگر جای دولت بودم، این‌ها را می‌فروختم و برای مأموریت‌های اداری هزینه هتل می‌دادم.
🔹
خانه‌های سازمانی در پایتخت و مراکز استان‌ها هم نباید رایگان باشد. به‌جز مناطق نظامی و عملیاتی، ساکنان باید بخشی از حقوقشان را بابت آن پرداخت کنند تا منبع درآمدی برای دولت شود.
🔹
با شوک‌درمانی مخالفم. اگر قیمت بنزین از سال ۱۳۹۸ هر سال ۲۰ درصد بالا می‌رفت، امروز حدود ۷ تا ۸ هزار تومان بود و بدون شوک، به منبع درآمدی برای دولت تبدیل می‌شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/682405" target="_blank">📅 00:25 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
