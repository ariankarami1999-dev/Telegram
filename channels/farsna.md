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
<img src="https://cdn4.telesco.pe/file/E51r2ihFDPB3LIor6PUirMpysPrcwBIoO_7sgc-jKRrXN7QHDOJP1usWsi_NZEAfSbMK5pSpjsDnZfJRvdtBZOrTWE3Vh6Koyn69Uu7VgrFLwoohDiFCAkANjEC5HHqGCe97a9tLs43eXKeGX4X_a87SPJFSlTTCBnsh6XGyNHfqXOSS9iRAb4AoLI-115utW2kXa75XFeEfHRlFldbUzn20S2IHflGBbpbzHcXL3XLT4KOHqH8zdP_dfLV7v51SdEvkBYKY91IK4CCQmZqBi71WjqAL71rHj175Y_qZQg2ojZabDSEpDNrYGqsH3irjPPKPfOQ8SZS5urNkxWFdMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-464702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwAcSrx7jiqzTuKd9fOIPHR8ZR12A8kxLdX08SBiSHRY1AvGCqsuMvCCrsOjFNPu8bnVSgDRe4X7nZackcyFD3WoOWtfB4T5l250GTtYu_PZhoCH6qPRPe14CI7wlerN0yLT1u-6eFjTf-jZjSKeI9j4YsIke6vcQ91zpdtGK4SWXACeo0iyQlp_vL9A01f0yu3ldxzCMEZXtlsvQq9RB2AZDMlTzTC7LfAevuyZLlsTbidqqzQZeRXtNXs7heXeB54UbmxK3WsY5qaGuo4BfpFRaQ5l5imWgCMz6coFRq7gevEF8xaTL15m4AaSaE6Jowr6pbVnv4V2GONaQETyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبیتکس هم در مسیر ماراتن‌ جنجالی بلوبانک می‌دود؟
🔹
پس از پایان ماراتن جنجالی کیش که با تامین مالی بلوبانک برگزار شد، حالا تبلیغات ماراتن نوبیتکس در شبکه‌های اجتماعی دست به دست می‌شود.
🔹
نوبیتکس که در زمینۀ رمزارز فعالیت دارد، خرداد امسال هک شد و به دنبال…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/464702" target="_blank">📅 10:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKa9kBoeSZ_Vu3RDqLH77tUuNHZE3M1Css-Xq5QoH8MB0-0s7SNUW3ngM6CMMC7YHAb9KGPYAMeJzaoCePVWOeM0AOA7vAzvzzMBaHKTK02U_9nw3-97t_c0ITYWsCU0VM3zB9LisNfzvgofvXudGqB7gBeetooh3Eduuy6bjipatP5FMs--9Wr9kfse3UKfjJpMVef_PG3zCPXhWspLNeJ_37mvX1p-iHCKZ8HanbvFM6LRmgwCb5AjOXq4V9Xk8YudiywopcCZx3NxOSINL9T_BtliWkuKgbpolLS0h34Qe3q8yG8Pb62NRPqQPJAZ7lMbvZcl48vw-eNMXvfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام جرم دادستانی علیه عوامل برگزاری دوی ماراتن تهران
🔹
درپی برگزاری مسابقۀ دو ماراتن در بوستان ولایت که در آن موازین قانونی و شرعی رعایت نشده بود، دادستانی تهران علیه عوامل و دست‌اندرکاران برگزاری این رقابت اعلام جرم کرد و برای آن‌ها پروندۀ قضایی تشکیل داد.…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/464701" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9CIz7C0-tzsGah-JlyPuT930BV1Ag0uCi9_L2kW26jS83t1AvZkq09hDzhDBdWQfp-o3h8RvIZaoJ8uBXgtXy8HhYvzaOv0hK_hW2Y8ovW05AoJhzdzKxQjrnjBFOrjUKL0_pSUaXn_Hngf2HXB1iXfe9IKycLN6DJ2HVCDVu8WWzMuWrBcyBfH2fIsjW_6k5OCOY7ZLhjHXMoZEx_SrqQDi7uSPSE3JbEwjkaSUkFro3lyWqf6eOgdX0Q1BPHXcqfUg1Tro8FbrXbrxdRWDMUhu26b7i-6MPOCsp2OgtJdGunaOI-WrpMqf-GMFu7D3_3eCfUujgXaPHg4TRjeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: هنوز رأی پرونده‌های عباس عبدی و صادق زیباکلام صادر نشده
🔹
برای عباس عبدی پرونده‌ای به‌اتهام «ایجاد اختلاف بین اقشار جامعه» و «انتشار مطالب خلاف واقع» تشکیل شده و در حال رسیدگی است.
🔹
برای صادق زیباکلام هم پرونده‌ای در دادسرای ویژهٔ امور…</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/464700" target="_blank">📅 10:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuzXOHFqETXjnyvIFhmrMlLvnZbgY8jRcs9WVwml-Uw3Y7hm5rL53YLPUQnS4rNZouZ917dedovhpyyvBbDWHb5w_Frg4AnP5_1fzq9F25Hx8GKbrfHjIF8IihGMzT_XcdXneQ5wANDttWBfZm_weQ_6Qk12j8kcZFqrIRpDhZ_9gEaitJWklGUfeAdBK-QBDLp9YfratoPMGfbiWuCJQfgUBHs02oJPs20Qo6jm175rAjG4cEryva5QGgyuO5jwGjsHRWCTW99Azuu83cmiAiy880JDDeWG6Tb5r_M_L-l-wx73NTmWxYg_FEQyKI5uUFstgg7NSU_-aKnr9yw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران علیه فلاحت‌پیشه و یک رسانه اعلام جرم کرد
🔹
پس از انتشار اظهارات یک نماینده اسبق مجلس که دوره‌ای ریاست کمیسیون امنیت ملی را در زمان نمایندگی‌اش برعهده داشت، دادستانی تهران علیه این فرد اعلام جرم کرد.
🔹
برای فرد مورد اشاره و همچنین رسانه منتشرکننده…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/464699" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFRlz2bnpro61m5fEn2KuRMuvfQvNRrgsIFfCq9teUSEu5CmgQtlGto47zs510jem6V1WkXBnHdlFi736hKwaHhcbTnjqBokE17qckJCAb509dkfOP3qPqj18T4q4ynOrT7fLC6nFf0-FJNIW_Qx_J6SHfIVkONawEnlD_-Sj7bnf15ojyHSsnMmk2vc3qht88y3k29c1I9CsjfxwLmO68VqcrjaPTawd37Hu9putHmwJqtInmeNqVb3UPOgTwKZZSufyXUwXYACN95yysypNT_wRe4qWSTpu38aQ5iy56qXrManTHCVyPIYFNCbzactMrXO2ZbrdkJauESOx1wkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریاض سوختش را از اروپا گدایی می‌کند
عربستان که یکی از صادرکنندگان بزرگ گازوئیل و بنزین در جهان بود، حالا به‌دلیل حملات یمن و از کارافتادن خط لولهٔ شرق‌غرب برای تامین سوخت مجبور به خرید هزاران تن گازوئیل از مدیترانه و بنزین از اروپا شده است.
🔹
این اختلال‌ها حتی صادرات نفت عربستان به اروپا را تحت‌تاثیر قرار داده و آرامکو تحویل محموله‌های نفت خام برنامه‌ریزی‌شده برای سپتامبر(شهریور و مهر) را لغو یا به‌تعویق انداخته است.
🔹
همچنین اختلال در مسیر صادراتی عربستان، ریاض را مجبور به استفاده از تنگهٔ هرمز کرده است؛ مسیری که هزینهٔ حمل، بیمه و ریسک عبور نفتکش‌ها را به‌شدت افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/464698" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کمیتۀ ملی المپیک پاداش بازی‌های آسیایی را به فدراسیون روئینگ واریز کرد  پاداش ورزشکاران به شرح زیر است:
🔹
کیمیا زارع، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔸
زینب نوروزی، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔹
فاطمه مجلل، دارای مدال طلا و برنز: ۳.۴ میلیارد…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/464697" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انهدام تیم سرقت‌های مسلحانه در ایران‌شهر
🔹
فرمانده انتظامی جنوب سیستان‌وبلوچستان: درپی انهدام یک تیم مسلح سارق در ایران‌شهر، یکی‌ از اشرار به‌هلاکت رسیده و یکی دیگر از اعضای این تیم دستگیر شد.
🔹
در بازرسی از محل درگیری با این اشرار، ۲ سلاح جنگی کلاشینکف، ۶ خشاب و مقادیری مهمات جنگی کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/464696" target="_blank">📅 09:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f5d1489.mp4?token=DqGCVrBOAIY8qkxovYQoNDGYfRVbAyj1INeSuZkrTRrJmhfjctRTh0BN1S3dCXeAhIl4rvp8zKEOyOkdjZ9dNsaHV7VA2HK242nICIUnUZ0v-szwe0ByaDf2q5cccZ2XKBlABqS9QfbTScOF_UJ2BJ_OzZ010wieKuKJpugZq8uJHMLHx3lEjkniAAunl8_pw60He3kGo8mC_xEa7SCZiB0nt863mfG_UYFu5HH4WVMtV1lbAKPbUOA94fXO3e1Kd-M3jBiqJPxCvMrWwccq7h4Xlc2nzuCoIDAfACY4fpSqXEQyjv2vCDvHNzzPj42ajMQ7esiTTKVJgANW9ucz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f5d1489.mp4?token=DqGCVrBOAIY8qkxovYQoNDGYfRVbAyj1INeSuZkrTRrJmhfjctRTh0BN1S3dCXeAhIl4rvp8zKEOyOkdjZ9dNsaHV7VA2HK242nICIUnUZ0v-szwe0ByaDf2q5cccZ2XKBlABqS9QfbTScOF_UJ2BJ_OzZ010wieKuKJpugZq8uJHMLHx3lEjkniAAunl8_pw60He3kGo8mC_xEa7SCZiB0nt863mfG_UYFu5HH4WVMtV1lbAKPbUOA94fXO3e1Kd-M3jBiqJPxCvMrWwccq7h4Xlc2nzuCoIDAfACY4fpSqXEQyjv2vCDvHNzzPj42ajMQ7esiTTKVJgANW9ucz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ساخته‌شده با هوش مصنوعی از نخستین لحظات جست‌وجوی پیکر شهید نصرالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/464695" target="_blank">📅 09:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiOqvH40wN9aGt4J1q8B2SSCnewQwQ9OQYNMfV7QwwGYPGweMUuW_a2v6FMcH0d45aEi3xesc40TYyq_SrdDuakybaIf8POmlLhZm4M79NG6NFHn9Jo0ej6E0oiArf5JXyH2D7H1EPPsCfNcKuFyzDbbEoccCFwe8wA2ZgGHuICY_6HHAgzXE9LgNaksi3gMFfRLVvHwdx4icm6YQt12OJdcRTrdSQpRjqh7RCG2Jpk3WSIexc7n_sIEBs2Gh0GvUBsXHCSFujLdVn4h7QNI0r4w0VIxxVVBWk3Dyq7r1M2F75RGYBqMpaG6-h1KGSUvM9lFHPH0NdJRKX-FGjQ0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCZsydZFsC-I3_yElZS2i8VR7PmTLktT-g4jc3uNQQc976_F0geVt4wWNl29xjmZX2fADIWvVeo4qMIJzE0HmPky3d-0scjC4D0MspRPUFRwVqzgaP_F0yI0c8I6gsksoNUFjD5DutH2_40e9STh6b6L4DWz7x2FGDva_55zk6O-DxxBlaz5ZNxN-BgirQFg_e1xqLfsQe7UJp8Ttvaiw0fi8S64I-3S_ZqXoKtdx5asilFJ7nollKdzZ0SEwVmXassLiESVWI8Ca-V8ZRXzikZenL2A_6E_xuZXMLDPwe4s4d5kgLP4uvbtzLrRMSNlv8hf9Mj8OTEszx8eR3sjcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سقوط بالگرد در کانادا با ۴ کشته
🔹
پلیس کانادا اعلام کرد یک بالگرد در ۵۰ کیلومتری مونترال سقوط کرده و هر ۴ سرنشین آن در محل حادثه جان باخته‌اند.
🔹
مقامات کانادا هنوز هویت قربانیان و علت این حادثه  را اعلام نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/464692" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=k3Ng7moizlSieU77e0wwvkYDz7xacwbjGw44T1rn1AIFEcktwo30BAHALZKSHm5OMfDCCFqS2aaaPJHuzIvj3BHVejtnFWLexdLRn20j04T0sbf25d5n07h_XjES3qOps1uoYIF1AfSEOimjrY0UWatKjDL46ueRw3c9FUauTD_FACFMIwMspkHBM-A4-G8wyPkLfGfQPY4ORyU0_53eDRUskrHMBS_CS8NL9PW4_xfJxoFfS_pqFqitR13wN7Tdxg1Diga88OEOu5byHZUZo7CQrJcmoDzbQAQIjYP_u6X73WSX0bMxskB1wVVmD2IR3otQZgIonyZGjHYV_wolwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=k3Ng7moizlSieU77e0wwvkYDz7xacwbjGw44T1rn1AIFEcktwo30BAHALZKSHm5OMfDCCFqS2aaaPJHuzIvj3BHVejtnFWLexdLRn20j04T0sbf25d5n07h_XjES3qOps1uoYIF1AfSEOimjrY0UWatKjDL46ueRw3c9FUauTD_FACFMIwMspkHBM-A4-G8wyPkLfGfQPY4ORyU0_53eDRUskrHMBS_CS8NL9PW4_xfJxoFfS_pqFqitR13wN7Tdxg1Diga88OEOu5byHZUZo7CQrJcmoDzbQAQIjYP_u6X73WSX0bMxskB1wVVmD2IR3otQZgIonyZGjHYV_wolwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز برای شمال کشور رگبار و برای گلستان و شمال‌شرق سمنان هشدار نارنجی سیلاب صادر شده.
🔹
سایر نقاط کشور جو آرامی دارند.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/464691" target="_blank">📅 08:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464688">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UequzsC4Q3HEh4zuLZnpsUARo6qUeLtyvHmdf0T2hv5fkh7yRq6BwpN09zlmAdCeegBevO6eeoW2vQy_kL417KumxHfz9rM7mNdt7ky9IfpzwMAUs7sz62M1wLvATB-JMKPywCDiROSYMA--iRAeTtwLRdeFAUJ3UtCnnOsXZi-0AMrLpcTLjiIl3Z37p_iEwOg-m9V7VtUFy2heXLym7TRmK-TquUO3NaEIYjQaZI49pDTaZb0L_v1ijvoN0tFonJO-LLnpwH0hBBGu89o6Qm51QFsKnYkLKsUjU5zU47YipTP1QS7vb17Lqwy1PFzf7bbDqloPb00zCSB3Min_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6dsf9p87cp7aRmYjNGfUlxtlK5MxpMXaugZxBlK7nhZOc8wbvkaFoUYh0h5sy0bFBlpAmUfFtrYZYRrzELech9_vY6Gsq18VIVZvcdbmgw-HLzamsIlL-7QOqQqMmpybWO74rcvqLyaGDl9a9DmpLMTRXUnoIKQllw_f9KpeEcSkj2ECDtp8PpU272FqfBeGMpzsa0WVv3Sl38pItemTAvD8DaFnVlAneSCBrOdseNaabssyeYFby7wCv31sd5vEKXPajT81Gsu4l9OEAYWNtCkFATzlzLpbBEZe38Umhg2MSur6pwR-eYE8jh59Mufdzff8--EgGekC0PpbGYv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onVA-NR8Urvld-hTJoNDyQPFVThMnN_isPjiTcZrCQesF_6VIhgJW-Wn2WRlSE4K3korwESjIkaSiwnMpMwZnL7OFmu23fG-aoz67KK_H-CVo94ZQTWtkZ_Gko04NH3pZ4vgg0X4LRv4H8gr4lPtqBSRrH8nx9Pg_NJt_Ke-bJSTt41725wDMO-a4Tsr1o_eokt_Ye6QI-x8wRjqGxb_H58M89B8Hsl4hgW0wzEoWhx_Mn_Zx9edzPW27QY6IoMn_njOO6dP2CVgPSmpiIiAzQAB8YzuSb0xMdw3N9Fu07rY0BMrnHiYvosoSCmb-5sp6ENjdUWsPnc_7PZPT_Lcng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقچی در نیویورک با وزرای خارجهٔ فیلیپین و نیکاراگوئه و معاون امور بشردوستانهٔ سازمان ملل دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/464688" target="_blank">📅 08:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPYdLVtJGHNNS4pITyjmFRsEvpAUun_s0U-DwEfL6D9FXA5TDWx3B4hfzu49xdGMjhh-A0Y-R01KT_tQQ3x7eOGpJTVfXhJihsPNxmV448fX6EgLY6BzElireWxsScPJjtyZRjrqhTeiOB7rXao4gkCcSBV1NoiJXcdegDXkb_VeVzwNwkXzxgE9pu9g6vRhG4U4NxGfIW4QfYVJZmrvGR93igv5BzsqdUGs1nGd0mcImuzB_fjQz_5FcTqJTLvkYx391E2O_BAUfJgihl_2evbGspBzprSfE7KF7cX0PsweHp7yv5woaASsaLKat8zqqVdwTxhMbqf5uwWm0oIeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuacBHUdevWmjmoI0uX-HHVU4ssnOoT_LseG446uZqB_qy05O-nlRzP5EYZfhiX7I2EG1brdMNf8w7nfbFVf-voRvSfDn64SaraBOrd9tzKpZyo1454sYpRIz6O0R7Wsv0zcStI2hZjLhijsB92m_am7xNOMB9u1ltDZU8FIcvm34k2DJrT_usRGVxQ4Es1_S3Z3Ih_rf1cH47RsMKwNmD_fd7B5IMEbWOSZwZTIDE0mgfyczkaiJFT3OXzxGN9I_SCmSC3RqY39nvCDAXJUxSy7M5odckHTuNw98aE2VYT1JLRlKpxTq6FlipW-b7fcHSudz4IZrbiFX3QPoEKyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOTKDzoFGUengOTzp2Ekuc2eHhqe9-U4XhHyEpqBlTki2qK2_ZtBMHqj0dXIow4b9RhwY-d-2hO4oGnsHLtnFUWJA1RY3t7pEZLFmx5FwpVsoF7A7TsFIZ2tbXPzHmihDeSNENOWP4mbfw7Q7N4TzFDeSTw9aHjZMyxfzNR5jGLb2XnkZUWH55O-YiA1lPFP_f8ObFqY6ATACa5vdqlJaXYdu7Cyp1xYdtctng3z_sle3Ps0cXMSn0F45ftZJNgaLSDg8xOsF5fwMTuJIXgeP1NJpaNAIFKdL0Hlst2pLquCIdQ8aRoT76OjS8d1zGzU_LhK4nQmqZvvTBe2juDRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_kq4ZsZeY7yiMW-a6M5lvFKxYkGNYAFIcJOphMISHn-rpcLKTtBLk0_DZXXsOQ9VGk9rYaJIQ1mhRDtpW0piNXpzRrVkjwpkVkM49A1lhdpLVcLff7yBnQHZcsbfDWZP1ahzI9Ag_C3hbdUG5M4LfMf6W_QYJ_t0LjoEeU7HnhcmXu3iV5EFOkQMoXst96WuiA_F8VrC7eUvj0wNirQ8WD_9txTn3l2DHJkVXV18aF5QUHb2xYsCrWZGnzbYZe34LyTxc1zE7GrzLp3vTzdQf0HyPDNwqzks3ThcubbnDuypbxodvcbGknaQCdwdzT7AgxSpJcmlIYqxX2Fmjg5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KREt8BAX2sl8UcytMhV9fcl3d1fH7q_kvus0jCoUHY8u3WcMu8qAMGRZwzDd3gD_xvtetHtQB_xykwN6Gd97GyAkNZgwzl38-LJL0dOmJ7PTlksHh7CvZjfR3UUfsOzJsZuuyCv7jS-xal2guNnHUuUK_0jbc4RTHbxu0iCMEA9G-1TJhtZ_XEV6A4ERVN0YTjTfIx08LXwNwOnWd0bF_tMIoFYz-pP0VNhLBp8h4yUXjpdZW_pSVJ-KFd4INrpzOKBr6IipIkFNSPqL507t0m6yG1zLUWPPim_UWcFodqRWAEVwAaiW_G8KUpqk0IeNSEe5NMnYrL5SsYDcJNpjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgRSlqdzwVxodFZ8C3Ke74kZL5GuSI8ztRg4l-ys_yTJfpPqm9ogTLj1JzGl0zlz-X7U-z3w0KGyGRIRVoNhgsPO2AG6D3EfBAVtH1qZ-lUy0DpR3zP1xEFdOAGetCJAQA8flDolawA1D6t-GUDKzbIOeZNfhWAH3p4Qz2fcllA38hWed3zkFVFB6WR72qio6ZSaQDPlsCuTuZTAmiSzMRTtn5BgxG_yaQKrFu_P0FJOZ9QSa0Sd6Hj8VopkswPVJAGOwBGWAp4xDwVOxyTLmC6laH43u19UTw2Tpf1t_Khhb1_YODFRUFB0s9bvGJWEmCvIeIIQIQmOERX6dTAMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyQCGvDSF5P-pqUAYxWe6NgJ4-AGUbW67C_5tqWpYUT2oLgUOGE_ZaTRzRREEjnowNv6aNoRhuGUfAkxsG6cKZYKpPL4nmvfNWY59JJlsBna_SxYivLe7mhQXeplpmZqSb3wZa3JOl_Kr3Pfv1sJnaccz7JhIgFBdHmy4sc3S4t9mAF4K6loyA9vIDczHBKU9pljW29EbEV6cDcMQ1uZNQr0AgChnElDsOOVqNGtgpP0NLWRgGfj2iNkA_gEu6NJ4lArkFJT7aKMOcJC73FbrOhsKn9xFXl_HrRv9cX5gsSRBmVssIlPlKcZZE7XJ0mHi1ETcR2QXbQ6PJM2uFP4fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اسکلۀ صیادی بندرعباس
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/464681" target="_blank">📅 08:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fc9366f5.mp4?token=ITL8y-surme4sNITJX-3D6U_70Wj-yXPWGK5ojjc_pkTULaAD6RSqGbff2lA9DExe-Q9n2woNqfiRVGd0Vaim3KOCWIpkBOp9K76QKi4jOcT7AGEb0WaCBzQOG5MvKiBRxaZ0qyiIelJgNZF2P4e9tOjqUD-kO70LyAKGIAWXF7JG8MRPpJVtEF__jHCBu0E8QVYIZ_6af4ivDv5beTyvi6HFW9-q_8qPn15qosf3YO9fUiorfvXgdSWgfaTat_EFWttEMQXu7bvAWxOoNEIvXZ03m57ftf19kIFDYGlF8tjBtj9tOizIQxvbBDwMUCMc0YvarJnZAuQtfwE_WvEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fc9366f5.mp4?token=ITL8y-surme4sNITJX-3D6U_70Wj-yXPWGK5ojjc_pkTULaAD6RSqGbff2lA9DExe-Q9n2woNqfiRVGd0Vaim3KOCWIpkBOp9K76QKi4jOcT7AGEb0WaCBzQOG5MvKiBRxaZ0qyiIelJgNZF2P4e9tOjqUD-kO70LyAKGIAWXF7JG8MRPpJVtEF__jHCBu0E8QVYIZ_6af4ivDv5beTyvi6HFW9-q_8qPn15qosf3YO9fUiorfvXgdSWgfaTat_EFWttEMQXu7bvAWxOoNEIvXZ03m57ftf19kIFDYGlF8tjBtj9tOizIQxvbBDwMUCMc0YvarJnZAuQtfwE_WvEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکات نمایشی آریا مام‌عبدالله و محمد سعیدآبادی در فینال ترامپولین  @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/464680" target="_blank">📅 08:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a8898d3d.mp4?token=RU3Q9_rgw7OlJrozNOB0OqsmqiJ_Tpqa895nDtAtfbUs6yuDH66EtOs9hfQTUEOCR99tLV6a8SMmTHRfEftwWh9OCjXQQgQUYbi1px-CFUC1lPRZEOPfJFNj6RMhQZuG8S08z7FLA_hTo3wfGqxipX9lUTuDoesTP6ccaxe5BXZtU8PPd7iyprkQVhT86xLW-7dAOtfU4Xc0-o6DIrqIZw-vF03Du4-7kSnlKYZGclB14FXFU68A0RRTP_EDd4kx1VN-FVnEqLDmPQcBllan5ufBcNfAonNAozIuCvfAXOEDmFB7901Tgc8HhQoVGa2517jRcQt0UHUQWOJwPkSkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a8898d3d.mp4?token=RU3Q9_rgw7OlJrozNOB0OqsmqiJ_Tpqa895nDtAtfbUs6yuDH66EtOs9hfQTUEOCR99tLV6a8SMmTHRfEftwWh9OCjXQQgQUYbi1px-CFUC1lPRZEOPfJFNj6RMhQZuG8S08z7FLA_hTo3wfGqxipX9lUTuDoesTP6ccaxe5BXZtU8PPd7iyprkQVhT86xLW-7dAOtfU4Xc0-o6DIrqIZw-vF03Du4-7kSnlKYZGclB14FXFU68A0RRTP_EDd4kx1VN-FVnEqLDmPQcBllan5ufBcNfAonNAozIuCvfAXOEDmFB7901Tgc8HhQoVGa2517jRcQt0UHUQWOJwPkSkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود تاریخی ترامپولین مردان به فینال بازی‌های آسیایی ناگویا
🔹
آریا مام‌عبدالله با امتیاز ۵۷.۷۴ و کسب رتبۀ پنجم، و محمدسعید آبادی با امتیاز ۵۳.۸۶ و کسب رتبۀ هشتم، جواز حضور در فینال را از آن خود کردند تا نخستین فینالیست‌های تاریخ این رشته از ایران باشند.  @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/464678" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=aDDhOzpuMwF4XYAZIOBYZh80EEgSZRkCle1Ts9_R5IwDV6W6nT21jrYilfnu0IzQ0lEAPWCRP0wV9eW6yGq6FnQ2E3nUavDn5OHKRPCYc1GDrs1WhkiPhNovjySA4RrJ3938Ot_BffDbnO39wD4sOKH0dISwMUx_Uu457JqyOzfwfHSpxSOGgGzz4pCRDjftndl-vLteZEJnJb0C7B1WDrh4VTX5gu0vzzHvw1lHDTt-GsIjxWCxNVb9FeY6yJkfro5vl1Q9DAjHhUg3anGlBh2AgPHkIiwYbSQ2_NqZZPeuXh-wS8Z94vxaDgnoOog8RUp2cZNkB77JLuVpwYg7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=aDDhOzpuMwF4XYAZIOBYZh80EEgSZRkCle1Ts9_R5IwDV6W6nT21jrYilfnu0IzQ0lEAPWCRP0wV9eW6yGq6FnQ2E3nUavDn5OHKRPCYc1GDrs1WhkiPhNovjySA4RrJ3938Ot_BffDbnO39wD4sOKH0dISwMUx_Uu457JqyOzfwfHSpxSOGgGzz4pCRDjftndl-vLteZEJnJb0C7B1WDrh4VTX5gu0vzzHvw1lHDTt-GsIjxWCxNVb9FeY6yJkfro5vl1Q9DAjHhUg3anGlBh2AgPHkIiwYbSQ2_NqZZPeuXh-wS8Z94vxaDgnoOog8RUp2cZNkB77JLuVpwYg7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا می‌توان از ابتلا به آب مروارید چشم پیشگیری کرد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/464677" target="_blank">📅 08:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هوای پایتخت همچنان ناسالم است
🔹
شاخص کیفیت هوای امروز پایتخت با قرار گرفتن روی عدد ۱۰۵، همچنان در وضعیت ناسالم برای گروه‌های حساس است.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/464676" target="_blank">📅 07:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg-NRjpGGmm6CTC2zNMwQCrNclivE8TVjmC5Xvzn7A6J2yECL9PGAo2VJeWQ47mwk457IkMkSfJUIxsodFDkrmvwRcPYPrjo_n9FhV9qxtUvoU67xWTs8lblQLcGnDjm9mPpRRjwK83kPzr4Tsk1b2Ip4X8lerim9SOfPnRVjPQpfTl7Rk83zNl4dldWAyEvtJ7TspdC_72C3nB88IltJNT0j3BOng1pUYl2ZApBY5a_W8l70VvZrUP7iy3DniNBG6dbUw-Xj3yoddnNPG9wDbsEN5riaErB8bnxlC2yJ1S4yO9VqKl9-kEVSvLdlYnxrUb-EazbBIB9-36kv-6VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تاریخی ترامپولین مردان به فینال بازی‌های آسیایی ناگویا
🔹
آریا مام‌عبدالله با امتیاز ۵۷.۷۴ و کسب رتبۀ پنجم، و محمدسعید آبادی با امتیاز ۵۳.۸۶ و کسب رتبۀ هشتم، جواز حضور در فینال را از آن خود کردند تا نخستین فینالیست‌های تاریخ این رشته از ایران باشند.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/464675" target="_blank">📅 07:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240a3a3a6a.mp4?token=R2FY998xc4EJ_7s5JuLKpT25_4EFf7W0TdGEAy1Fufx2SfpX3hW-k6YAYjD4Irh0hHKS9pbXi5MyPrUJqEbIH9SIxE9R7kVslq69fnZJMmhE0wu7QFe9kfeuCbvHBJ6tx36LShlJdpGb2Sd-6xRtGICw7ouyO4NOQlKV1a_a7cJVxXM8qqXIa45NzSgSg0H1KMSgrihuOMxYkIiAgtRh_QWZoad-FdvdbbsABaeL1vYYAsTXj1lXpUTwxjhyDCH-SLgTeRYs5UrMg7PfvRg8t9ChOEuQ8NU1uf6sRHYm3C0c1-Aq1-qBc1_DEHmvrx6Q6wDLDGLnAUE4R8QSVKETyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240a3a3a6a.mp4?token=R2FY998xc4EJ_7s5JuLKpT25_4EFf7W0TdGEAy1Fufx2SfpX3hW-k6YAYjD4Irh0hHKS9pbXi5MyPrUJqEbIH9SIxE9R7kVslq69fnZJMmhE0wu7QFe9kfeuCbvHBJ6tx36LShlJdpGb2Sd-6xRtGICw7ouyO4NOQlKV1a_a7cJVxXM8qqXIa45NzSgSg0H1KMSgrihuOMxYkIiAgtRh_QWZoad-FdvdbbsABaeL1vYYAsTXj1lXpUTwxjhyDCH-SLgTeRYs5UrMg7PfvRg8t9ChOEuQ8NU1uf6sRHYm3C0c1-Aq1-qBc1_DEHmvrx6Q6wDLDGLnAUE4R8QSVKETyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پادگان آموزشی جان‌فدا در پایتخت افتتاح شد
🔹
در نخستین مرحله از طرح جان فدا، اولین مرکز آموزشی جان‌فدا در میدان امام حسین(ع) تهران افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/464674" target="_blank">📅 07:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شکست تنیس دوبل مردان در گام اول
🔹
کسری رحمانی و علی یزدانی در دور نخست تنیس دوبل مردان، نتیجه را ۲ بر صفر (۶-۴، ۶-۴) به حریفان چینی واگذار کردند. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/464673" target="_blank">📅 07:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔸
کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۷، ۸ و ۹ شارژ شد
.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/464672" target="_blank">📅 07:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QtkCm5jkfKejkQOyho9oCX84SpqGqDALKAn4yQVjWFhXUgtCmfL4E_B-hhp-JQmTkJCRY0EPmg8q1m87ywRbaWiRYy1x68la0EStf30hnvr_BObr7oEujPE6pzgu7R_Yb7YWHKyw1R-4fZ4N08438E9l-O_h2I4rgIE2x7g78GtQAFW1G1xVSW1rVf1TcI4RCNAPl0UL-oFG4FkY6oA1GxALkbkVnZ9oYXfq6th3P4jiMuzcn9MZDCe_zEPS-QdO3rMj_Ah5LAK1JBGPy07eKR2UsNqrikSsxktCPxUJk8jn2V8TBJUgjUTEVIsbGqshOLtYn_qs1FC67mH-dVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالمندان امسال به مدرسه می‌روند
🔹
شهرداری تهران: امسال درحال طراحی برنامه‌ای هستیم که سالمندان وارد مدارس شوند و به‌عنوان «زنگ خرد و تجربه» با دانش‌آموزان ارتباط برقرار کنند تا تجربه و دانش نسل سالمند به نسل جدید منتقل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/464664" target="_blank">📅 07:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464663">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آذرپیوند به یک‌چهارم نهایی کوراش صعود کرد</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/464663" target="_blank">📅 06:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464662">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4iZ0oSRYUwmsce4i3SCT97k8qFbzHeCdysk1s3ugsTuq8u5P2_nzf-fMQi8DPz_xV26qDGAH2pjPtNUq3hTqoU9Ina_iEKjGbry1m-84WzKuzdaRH-1yzNuRTWuZWDLBF0PggV-fKTSUHlGbsZgyxtuGfLW_Bd3WZJOr9unsmt4z9HsbKzO1dCXY_kKDkzLtNFNpRgX9nyHL53Q1nkGFxuF7BkJkBYqe9t71F26RlOjJDcqRmYWnWsL6q0sckbqFtgxAVoAXvH5qDQHlvXEqQ0_mwCUj3b4UJ53t9fufzqJTYDRHDRHIop4rqyjYVaTQEGTw8iIERpVqILFK-5Ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به گدایی رأی افتاد
🔹
در حالی‌که یک‌ماه و ۸ روز به انتخابات میان‌دوره‌ای کنگره مانده است، ترامپ به سبک خاص خود با کنار هم قرار دادن ادعاهای بزرگ، از شهروندان آمریکایی خواست به او و حزب جمهوری‌خواه رأی بدهند.
🔹
ترامپ مدعی شد که شاخص‌های مختلف اقتصادی آمریکا به بالاترین سطوح تاریخی خود رسیده‌اند اما رسانه‌ها از پوشش این دستاوردها خودداری می‌کنند.
🔹
ترامپ پس از دستاوردسازی‌های عجیب و غریب و در حالی که پیش از این مدعی شده بود انتخابات برای او اهمیتی ندارد، نوشت: «در انتخابات میان‌دوره‌ای به نامزدهای جمهوری‌خواه و "ترامپ" رأی دهید. ما آمریکا را دوباره باعظمت کرده‌ایم».
🔸
در حالی‌که ترامپ از موفقیت اقتصادی سخن می‌گوید، داده‌های اخیر نشان می‌دهند فشار هزینه‌ها همچنان مسئلۀ مهمی برای اقتصاد آمریکاست.
🔸
در این راستا هفتۀ گذشته آسوشیتدپرس گزارش داد تورم در ماه اوت افزایش یافته و رشد قیمت انرژی، مواد غذایی و کالاهای مصرفی فشار بیشتری بر خانوارها وارد کرده است. هم‌زمان نرخ وام مسکن ۳۰ ساله به ۶.۹۵ درصد رسید که بالاترین سطح در بیش از ۱۸ ماه گذشته بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/464662" target="_blank">📅 06:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464661">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تیم میکس تیراندازی آمادۀ تقابل با کرۀجنوبی
🔸
بیتا عاشق‌زاده و میلاد رشیدی در یک‌هشتم نهایی میکس تیراندازی با کمان، بنگلادش را ۱۵۸ بر ۱۵۴ شکست دادند و به یک‌چهارم نهایی رسیدند.
🔹
تیم میکس ریکرو با ترکیب مبینا فلاح و محمدحسین گلشنی در یک‌هشتم نهایی ۶ بر ۲ مقابل…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/464661" target="_blank">📅 06:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464660">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd3qxrB59qiOUYh9Y8BRBLLRblN476OAaSsYsPgQ_VNtZU-yZmS2qMImAdmIM_xCzKy9vh-b1W5Z3oKXX1pMrlV2thJ0tVsiVqYjGWv8Pmx7sXST6-8EK2kNrpVbwgLKxYqH6UqxB9RtqaXhzdljP_KqVpMYQq6ofU8SL5LboS2zcckmP63iB1QtCHppHXLAu4Zesf_H6cI83sVzxVk2x2_l5CUsB3rbq0P7dwEdyIoTUGEbzKwmI4wealOYuvGiUMOFDxLbwoKOztcTddUYL4yZYdswAoQLflwE7ZJH8XxjiYBVYrlJukJm6vuGxhKumjyEXF9vSMyMFEFqgkIzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع بی‌‌دردسر والیبال ایران در ناگویا
🔹
تیم ملی والیبال ایران در نخستین دیدار خود در بازی‌های آسیایی ناگویا، بامداد امروز مقابل قرقیزستان به میدان رفت و در دیداری یک‌طرفه با نتیجۀ ۳ بر صفر به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/464660" target="_blank">📅 06:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5CJJei7PBWh6o3k32phOTi9fCtb6V87TWfDtCSe_wI1ZftpeRlfKquJk54P9bW3gy4j5XXEfJQGMjKrhSaROd9PeYG4fZhQbrLr8C56gQfXqg_Mc6j_GVX90YoFznLQnTBDObsFGnbe-DwuOW_W-nS91SsccwBXTlOg5zd4q_JthJL71lwNl2lMTiQDL2n_-DC43mmAq5TtHjb6hc6SM_zPJKYzOfxpbV_f3zl4wTgzk08-pW_7sTUdlixoNuQmEKs3mwKYz5VKdeqIgRRXcRifJWE5dzZk8vjnfmmAYhWxXhtQQnPGlQ6wWIMykrHg-Hab630L8nMJE-052sY2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست تنیس دوبل مردان در گام اول
🔹
کسری رحمانی و علی یزدانی در دور نخست تنیس دوبل مردان، نتیجه را ۲ بر صفر (۶-۴، ۶-۴) به حریفان چینی واگذار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464659" target="_blank">📅 06:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کمیتۀ ملی المپیک پاداش بازی‌های آسیایی را به فدراسیون روئینگ واریز کرد
پاداش ورزشکاران به شرح زیر است:
🔹
کیمیا زارع، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔸
زینب نوروزی، دارای مدال طلا و نقره: ۴ میلیارد تومان
🔹
فاطمه مجلل، دارای مدال طلا و برنز: ۳.۴ میلیارد تومان
🔸
مهسا جاور، سها فخری، ساقی ملکی، هنگامه کامیاب، امیرحسین محمودپور، دارای مدال نقره: هر نفر ۱ میلیارد تومان
📝
همچنین به کادر فنی ۵۰درصد پاداش ورزشکاران، معادل ۸.۲ میلیارد تومان تعلق می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464658" target="_blank">📅 06:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آذرپیوند به یک‌چهارم نهایی کوراش صعود کرد؛ عیدی‌وندی حذف شد
🔹
طاهره آذرپیوند در وزن ۵۷- کیلو پس از استراحت، حریف هندی را ۳ بر صفر شکست داد و به یک‌چهارم نهایی رفت.
🔹
پردیس عیدی‌وندی پس از استراحت، به حریف فیلیپینی باخت و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/464657" target="_blank">📅 06:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90240f4664.mp4?token=HEYJaOlNmUQD3lwGCTEKpLatTyUpvj2V-rfbXBy582vYmqmMCjM0XOHifPUqScTnPmJ_KkC9xlUW2Jh1C2NzJosT10DzVu8dBGyATsEsWJd04NA1Y2HQQzl2SJwoepCpKeDxE0fZ7Bbvx905DVFcfxMDSrF3rum7itdKtsYRnjE_tZ6C3TTzywGs8Z_oAy_km3pHtOtvr2HfOmX5CCPPkcKbMgrN1k2ADKz3XGEjRz9VLXoJf-xBw2-CarYD57JiNj3MwWwlyppGqzSQusfNgahu8mZhMQVNHN6AGJLMlVrMrfS03dpZbgwuL7XTryh2FGwXdfyrQ7iyGRYDLispBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90240f4664.mp4?token=HEYJaOlNmUQD3lwGCTEKpLatTyUpvj2V-rfbXBy582vYmqmMCjM0XOHifPUqScTnPmJ_KkC9xlUW2Jh1C2NzJosT10DzVu8dBGyATsEsWJd04NA1Y2HQQzl2SJwoepCpKeDxE0fZ7Bbvx905DVFcfxMDSrF3rum7itdKtsYRnjE_tZ6C3TTzywGs8Z_oAy_km3pHtOtvr2HfOmX5CCPPkcKbMgrN1k2ADKz3XGEjRz9VLXoJf-xBw2-CarYD57JiNj3MwWwlyppGqzSQusfNgahu8mZhMQVNHN6AGJLMlVrMrfS03dpZbgwuL7XTryh2FGwXdfyrQ7iyGRYDLispBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف تیم‌های کامپوند مردان و زنان
🔹
تیم کامپوند ایران در یک چهارم نهایی به مصاف تیم کره‌جنوبی رفت که ۲۳۹ بر ۲۳۴ شکست خورد و حذف شد.
🔹
کامپوند زنان با ترکیب گیسا بایبوردی، بیتا عاشق‌زاده و شیوا بختیاری در مرحله یک هشتم در تیر طلایی مقابل تایلند باخت و حذف…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/464656" target="_blank">📅 06:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxYi1aBpAGI8y3dzD7Cd1jfLt46HJhY40EjQT6bPFV0qFAEkiSryuCoInivOnJ4QQO86RQfhfsGQFv-v0OS1sLBVLCKo9WzXrfLjHF6FEcxim2UNTXR5xqcGbJ-fhCo3Tm1h8yWYTdOwUlTp4Mnj_3Yxbzn32AA8vms5jkTK77vfcnQWBhNPXAlhW4YN7PzI5yvyVDK-chlPflmSiI5kVdIBFMECgRs7uZES-zeHcmlt9Cu1F1CLaNi0Zi_-jdIYYUi4dMhSnJWSPQyDeipi-_yH3yd6yjzcqLeCfMDvZO6KTl6ePXBuDPM0_eUijSqLe1XOgsbQz_ZaBlvAG2E4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس اعلای اسلامی عراق: هرگونه همکاری با دشمن ایران حرام، و شکستن محاصرۀ ایران واجب است
🔹
همام حمودی، رئیس مجلس اعلای اسلامی عراق محاصرۀ ظالمانه و غیرانسانی تحمیل شده توسط ترامپ بر پروازهای ایران را محکوم کرد.
🔹
او گفت این محاصره مغایر با قوانین بین‌المللی و قانون اساسی عراق، به‌ویژه مادۀ ۸ است که بر حسن همجواری تأکید دارد.
🔹
حمودی تاکید کرد هرگونه مشارکت در محاصره و تجاوز نظامی، اقتصادی و رسانه‌ای علیه ایران حرام بوده و شکستن این محاصره واجب است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/464655" target="_blank">📅 05:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE8f935FQ0HU71YUKI2swAIgZaB0KCufX52x0r4pWLlDZGSDBpfQ9qCpvwUEzYt3ucfBBOlQwyAP3g1xzFG7LpHtc6A7YH7X1GfWsdBdd3YrpyQnVIE5TER3lpim4urhid-iUVokf6GWnYfwviKEmnRP1AHsRiUtc_NELCdLEoZy3hiRIvfkzWDk-_Exnzo5RFjDvX6ifjVDl2yoNfCp_RpGXEgssgrnvHQlVbglNKWMOp7zU7j50PdQEGaMj0kr8GsJLSRjB2oWVW8ILdsYKnhMA3m9UGzSW3zN2YeIEp6SwnfrEgSFvz3AF-coGZlyINaPwvXgXhenl0vpwLEAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ قاطع وزیر خارجۀ ایسلند به توهین نتانیاهو در سازمان ملل
🔹
وزیر خارجۀ ایسلند در سخنان خود در مجمع عمومی سازمان ملل در پاسخ به نخست‌وزیر رژیم صهیونیستی گفت: بزدلان اخلاقی آن رهبرانی هستند که بارها قوانین بین‌المللی را نقض می‌کنند.
🔹
نتانیاهو در جریان سخنرانی خود در مجمع عمومی سازمان ملل زمانی که با حجم انبوه نمایندگانی که سالن را ترک می‌کردند روبه‌رو شد، آن‌ها را «بزدلان اخلاقی» خطاب کرده بود.
🔹
وزیر خارجۀ ایسلند در سخنان خود گفت: «ما واژه‌های بزدلان اخلاقی را از این تریبون شنیده‌ایم. به نظر من، بزدلان اخلاقی آن رهبران جهان هستند که از نشستن پای میز مذاکره برای صلح عادلانه و پایدار خودداری می‌کنند. کسانی که دسترسی به کمک‌های بشردوستانه را برای مردم نیازمند انکار می‌کنند و بزدلان اخلاقی آن رهبرانی هستند که بارها قوانین بین‌المللی را نقض می‌کنند و به آن احترام نمی‌گذارند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/464654" target="_blank">📅 05:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حذف تیم‌های کامپوند مردان و زنان
🔹
تیم کامپوند ایران در یک چهارم نهایی به مصاف تیم کره‌جنوبی رفت که ۲۳۹ بر ۲۳۴ شکست خورد و حذف شد.
🔹
کامپوند زنان با ترکیب گیسا بایبوردی، بیتا عاشق‌زاده و شیوا بختیاری در مرحله یک هشتم در تیر طلایی مقابل تایلند باخت و حذف شد.
@Sportfars</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/464653" target="_blank">📅 05:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGPvtck52SrSqterEtS85bg0tclnYAL6m2E-LlzXL1Lt9o6ZoslBx_N0g-cr8cimFAnnsTnDi01vRLoh8ke1dF_E9EASb40UYAgU6xHitom_mENw79pLzp6YXxgrCD5v2QOf0HgAQXOycgy6Tdkw4HMRI0WsKdP5PVtiMGMdn3SsmGd4_DMcsxftOViip43FGFc05Mx5XJqRw7-lRKjvnPNvlxZBRtVahjpwPOqvDfKZh4C8dAlNy9WRuEfdQM13a-tJ4jRdhtuVJovC-FWnmQbUnaGLD-zk5ssM92qrHASvbrc-XmLwsSiXV1pqbHfbgvvLhge00jNlQea-Oq4Hww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیک‌تاک دادگاهی شد
🔹
برای نخستین‌بار در آمریکا، یک دادگاه در آلاباما موارد مربوط به آسیب تیک‌تاک به سلامت روان نوجوانان را بررسی می‌کند.
🔹
آلاباما می‌گوید طراحی و الگوریتم تیک‌تاک کاربران جوان را به استفادۀ مداوم سوق داده و آنها را در معرض محتوای آسیب‌زا قرار…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/464652" target="_blank">📅 04:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObFwBR4cMfumj1NJmFqAxlmQRPq5e_e1pROH2txCzrr0txv-FO3Cg6gnmv0GsHmTjCXOPXX5dU6b0sHjH-v9v70iJ_BXMBa_liNVdaI1QZq245Y372G1SnEHGvS60NOUGqC5_NiDQ0TPSFw0_urpokpVzjyJZKywIFEjxPb3VAzrP8Oa9-53d6f8XzDpjKiOf2kWueB83YxcZpy487Q3TKpHVQg_CdhZ9gSu4TJaJkN5zY86dVJjBqjaDD_OSWFIbK-eYM4kuiEL3pSNCGAzhdnqHMr-XH0JjKNW8eNcSFe8f18wCVfyp0TqYBWzyVeNsj2SdK4fgFKNQ8p_x7cczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع گازوئیل اروپا؛ تازه‌ترین ضربۀ جنگ علیه ایران بر اعتبار آمریکا
🔸
تهدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای کاهش صادرات گازوئیل به خارج از کشور، بر خلاف وعده‌اش دربارۀ غرق کردن جهان در سوخت‌های آمریکایی است و خطراتی برای این کشور به‌همراه دارد.
🔹
به گزارش پولیتیکو، کارشناسان انرژی می‌گویند که این اقدام تنش‌ها بین آمریکا و اروپا را تشدید می‌کند و در عین حال اعتبار آمریکا را به عنوان یک شریک تجاری به خطر می‌اندازد.
🔹
آن‌ها افزودند که این اقدام می‌تواند کشورها را وادار کند که به‌دنبال تأمین‌کنندگان دیگر بروند و در آینده، توانایی ترامپ را برای استفاده از انرژی به عنوان ابزار چانه‌زنی محدود کند.
🔹
یک مشاور دولت ترامپ که نامش فاش نشد، در این‌باره گفت: «این به اعتبار ما آسیب می‌زند. کل فرضیۀ سلطۀ انرژی این بود که ایالات متحده بتواند سوخت متحدانمان را در سراسر جهان تأمین کند.»
🔗
شرح کامل گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/464651" target="_blank">📅 04:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd5f86386f.mp4?token=mN0XltNvIhuP4dlC652U2AZHAV-hbLca_uEg8KLHhnFD5h5YHLotvDuJVaQ6aUgXLnMY7M8oZVaa1gmz5CNyU_EwCQHxOnUrfYYk08iEWedrs_NA9wgu3xt3qulhA0th_gVZrAfC7oT10vg6bcOkVp1SAhR-7UQKXQ5Ce1XBD_MOpr_4hzweJTYbj2FNEvNGsI0RO_0NKhgNL7BfNQwqxvd6ozlqTWr2jNoIZoZZnENzYOzra7y--LJcn8fYma6ELNISszL_BTZtDB4RuEURVP9yayKUZDBLu3HQi4vhrAUQPMVN0aJbxbnCRpJ-CztanjaFwCV3fwLRnghidmN48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd5f86386f.mp4?token=mN0XltNvIhuP4dlC652U2AZHAV-hbLca_uEg8KLHhnFD5h5YHLotvDuJVaQ6aUgXLnMY7M8oZVaa1gmz5CNyU_EwCQHxOnUrfYYk08iEWedrs_NA9wgu3xt3qulhA0th_gVZrAfC7oT10vg6bcOkVp1SAhR-7UQKXQ5Ce1XBD_MOpr_4hzweJTYbj2FNEvNGsI0RO_0NKhgNL7BfNQwqxvd6ozlqTWr2jNoIZoZZnENzYOzra7y--LJcn8fYma6ELNISszL_BTZtDB4RuEURVP9yayKUZDBLu3HQi4vhrAUQPMVN0aJbxbnCRpJ-CztanjaFwCV3fwLRnghidmN48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): برای حرف دیگران منظور خوب پیدا کن
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/464650" target="_blank">📅 04:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZvG61VYaN12GOPOF3ar5nvhmAZH6QxwqUcbf05iJPZI_nXI0Ip4YeMhhW8E9-PdCIvvVAMZRaHfAbwGaBBUBJ2qxem3wcCwkAa7VfT2Lx0SFAFN7BtZffV0RE6wgiZXVPj8x-V3nxx7ZXYWg86ffS-6LJWbQzfJn6X5BjAia_3ZMsnljo2RpGdTlN50pCYhk2MItBHQPPYnzravmYIJl4GHu1YXMtL2iOHNccbSRIPYHTd-lFkaJ3XLjJESFNfGjOw0DorjU_QvIqBipRP9e5UFsHWZrvQs1_NmcNHcxBVjAsH3QjFL6siYbI1Tga6vnWYxhoCZ-zOsdCBPLoSt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افسر فرانسوی: تنگۀ هرمز به بن‌بست ترامپ تبدیل شده است
🔹
افسر سابق ارتش فرانسه با اشاره به ناتوانی آمریکا در تأمین امنیت عبور کشتی‌ها از تنگۀ هرمز در برابر پهپادهای ایرانی گفت: این آبراه به «بن‌بست ترامپ» تبدیل شده و ایران از تنگۀ هرمز به‌عنوان اهرمی قدرتمند در برابر واشنگتن استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/464649" target="_blank">📅 03:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید
🔹
پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.
🔹
این پلتفرم می‌گوید محدودیت‌های ایجادشده از سوی پلیس امنیت اقتصادی و برخی نهادهای مرتبط، امکان دسترسی به بخشی از ذخایر و ایفای تعهدات به کاربران را با مشکل مواجه کرده است.
🔹
در روزهای اخیر شماری از کاربران میلی‌گلد در فضای مجازی از تأخیر در تسویۀ ریالی و دریافت طلای فیزیکی خود گلایه کرده‌اند. برخی کاربران نیز با طرح ادعای «خالی‌فروشی» دربارۀ میزان واقعی طلای پشتوانۀ معاملات این پلتفرم ابراز نگرانی کرده‌اند.
🔹
این نگرانی‌ها در حالی مطرح شده که طبق ضوابط بانک مرکزی، سکوهای آنلاین باید معادل تعهدات مربوط به طلای فروخته‌شده را در خزانه نگهداری کنند و طلاهای ذخیره‌شده نیز ظرف سه‌ماه به شمش استاندارد با عیار حداقل ۹۹۵ تبدیل شود.
🔹
با این حال میلی گلد مدعی است سازوکارهای حاکمیتی و بوروکراسی موجود، دسترسی این پلتفرم به ذخایر بانکی را محدود کرده و در نتیجه تحویل طلای کاربران با مشکل مواجه شده است. این شرکت پیش‌تر نیز اعلام کرده بود طلای کاربران در خزانه‌های بانکی نگهداری می‌شود.
🔸
حالا با توجه به نگرانی‌های اخیر دربارۀ دسترسی کاربران به طلای خود و ادعاهای مطرح‌شده دربارۀ پشتوانۀ معاملات، اتصال هرچه سریع‌تر تمامی پلتفرم‌ها و گزارش برخط موجودی و تعهدات آنها به سامانۀ ناظر، بیش از گذشته اهمیت پیدا کرده و می‌تواند بخشی از نگرانی کاربران را برطرف کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/464648" target="_blank">📅 03:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/464647" target="_blank">📅 02:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d41660dc6.mp4?token=LJh67KJgNlj96NbMPMZ2uklSaBUYC7OAMwSSXXCCm72KAqkcfsTn_bO_LVnHyxHQUdo0UxyYY9B5gsOMN3obQTb9eIequ5O73FWuetqjd68CiKjMfl-l2W5Dq_azrmZFIQE2usADudy2-GlulJ2Bd3OpZQILfYYQoXnOBODrphTuPNy9a2j15iT6TyUizeYAmsrm9SED93_bzi0qoGSsI8XPIO6unMAVPb3XbRW6aVcZnfRFArx7GWv-0By8vtyPHpCL5prKO26UORG1crn87FNv8Wyb5jqZwuFiCirMG8LSIw3FFr4X_oSA9fApp6CPRGvv5l6YCATsVBY9EWc5eV-n20Ow-Xr0CDqPKEIHaU7bn4_ivH_imuG5LsNwqFU5FAXkZhpXvWkhiBgHt7uD18ssXjLrQ2OWSauRQddJqbqpjxZl08rj8s3Dfz8fKeUvqdC0qTGFemGi05RQsCzSrZkEuFAJgjPeRfLRNSl1eq4KiKr-9Wlk1IaaQ7sOLmu_eBvGqGKyupGNZt03Cku-3PkXrhThnYIXZ6khCisctL99uEQoh94s0bLh7TX-FqPDdDG1Lwx13kXjMnr6KekNYT0Y1BdyPIzpZixOiT4MCUZWkBmBV_lsXAKNAPiw9R-kOc-xOCjtzKMao3YreGRYTVrNq2JmasXHVIaA4HT1_dM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d41660dc6.mp4?token=LJh67KJgNlj96NbMPMZ2uklSaBUYC7OAMwSSXXCCm72KAqkcfsTn_bO_LVnHyxHQUdo0UxyYY9B5gsOMN3obQTb9eIequ5O73FWuetqjd68CiKjMfl-l2W5Dq_azrmZFIQE2usADudy2-GlulJ2Bd3OpZQILfYYQoXnOBODrphTuPNy9a2j15iT6TyUizeYAmsrm9SED93_bzi0qoGSsI8XPIO6unMAVPb3XbRW6aVcZnfRFArx7GWv-0By8vtyPHpCL5prKO26UORG1crn87FNv8Wyb5jqZwuFiCirMG8LSIw3FFr4X_oSA9fApp6CPRGvv5l6YCATsVBY9EWc5eV-n20Ow-Xr0CDqPKEIHaU7bn4_ivH_imuG5LsNwqFU5FAXkZhpXvWkhiBgHt7uD18ssXjLrQ2OWSauRQddJqbqpjxZl08rj8s3Dfz8fKeUvqdC0qTGFemGi05RQsCzSrZkEuFAJgjPeRfLRNSl1eq4KiKr-9Wlk1IaaQ7sOLmu_eBvGqGKyupGNZt03Cku-3PkXrhThnYIXZ6khCisctL99uEQoh94s0bLh7TX-FqPDdDG1Lwx13kXjMnr6KekNYT0Y1BdyPIzpZixOiT4MCUZWkBmBV_lsXAKNAPiw9R-kOc-xOCjtzKMao3YreGRYTVrNq2JmasXHVIaA4HT1_dM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واردات سامسونگ و ال‌جی آزاد شد
🔹
سازمان توسعه تجارت ایران در نامه‌ای به گمرک اعلام کرد: با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🔸
با وجود آنکه تولیدکنندگان لوازم خانگی کره‌ای پس…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/464646" target="_blank">📅 02:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d9a21acc.mp4?token=rwaV-MlJmDkLXTqQ5tW0EBvUSxmOcaT5sPQ2yX8rLh4ne9BuD-VkEdIVcx7htQBD2BgntwPvKt0DgcJhKV3fwWqeIPItzuPCS2Io8G1y__r1LFOYDv_e3WHW1j903LPhV6H2qGx1M2oLMKCjbO1EwjRNP2j4Ue4Ia-gE3pkNo3UoqUCvgitLbbmKuu3IBkJesZweCK9Mv4CLNHxBtHymsC28LvlH4uf_N0xwWYSwJ1DngJUvzvFl-qJb2BhR-BsVWPa2coJQtVGDSsraLcjGoh3Xng9MaT83sO681kttqxxzNdajZUmGwzJqlMHZXiVb8k5yi1mF1khIPW-1kMZsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d9a21acc.mp4?token=rwaV-MlJmDkLXTqQ5tW0EBvUSxmOcaT5sPQ2yX8rLh4ne9BuD-VkEdIVcx7htQBD2BgntwPvKt0DgcJhKV3fwWqeIPItzuPCS2Io8G1y__r1LFOYDv_e3WHW1j903LPhV6H2qGx1M2oLMKCjbO1EwjRNP2j4Ue4Ia-gE3pkNo3UoqUCvgitLbbmKuu3IBkJesZweCK9Mv4CLNHxBtHymsC28LvlH4uf_N0xwWYSwJ1DngJUvzvFl-qJb2BhR-BsVWPa2coJQtVGDSsraLcjGoh3Xng9MaT83sO681kttqxxzNdajZUmGwzJqlMHZXiVb8k5yi1mF1khIPW-1kMZsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از شهید سید حسن نصرالله در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464645" target="_blank">📅 01:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ab1fbf97.mp4?token=A5GrLyOWy6fI3Ady9hU67_5zXr-O_NonQ5kTBwiYIWGgBcGrDxTRA5itzQw_AxsKN4pth8SY3Hn3baGojG3aV7X3ely8yyAsUvNwRah_GZsUK2DvJCpa9t7xYZfLCF7DTdusufY4uj7bUxeTPyGje_cpqMJ0rVQaAYsYPBrVEVwmXDyS7QfICL7orTaD2g4JSvPshq2FvTGsMAFUHl-n_3iWDPBJOQJoKfFBVvod47we33llLPUCdcZXSHInflgCbIJ3z6NzzGancuCiRK8XgBBz0e71q31k9taJt2m7Xfqci5l6cHsZm0q3kK1hQB4kx6vtjqG5VdZRBnrlgsOulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ab1fbf97.mp4?token=A5GrLyOWy6fI3Ady9hU67_5zXr-O_NonQ5kTBwiYIWGgBcGrDxTRA5itzQw_AxsKN4pth8SY3Hn3baGojG3aV7X3ely8yyAsUvNwRah_GZsUK2DvJCpa9t7xYZfLCF7DTdusufY4uj7bUxeTPyGje_cpqMJ0rVQaAYsYPBrVEVwmXDyS7QfICL7orTaD2g4JSvPshq2FvTGsMAFUHl-n_3iWDPBJOQJoKfFBVvod47we33llLPUCdcZXSHInflgCbIJ3z6NzzGancuCiRK8XgBBz0e71q31k9taJt2m7Xfqci5l6cHsZm0q3kK1hQB4kx6vtjqG5VdZRBnrlgsOulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای اعتراض صنفی سلف دانشگاه رازی کرمانشاه چه بود؟
🔸
ظهر شنبه ۴ مهرماه توزیع ناهار در سلف‌سرویس خوابگاه پسرانۀ دانشگاه رازی کرمانشاه با اختلال و معطلی مواجه شد؛ اتفاقی که با واکنش اعتراضی شماری از دانشجویان و بازتاب در رسانه‌های خارج از کشور همراه شد، اما بررسی میدانی و شواهد عینی حاکی از ماهیت کاملاً صنفی این رخداد به دنبال تغییر فرآیند پیمانکاری و نقص فنی سامانه است.
🔹
براساس روال معمول دانشگاه، ساعت توزیع ناهار دانشجویان از حدود ساعت ۱۱:۳۰ تا ۱۳:۳۰ است. با این حال، به‌دلیل تغییرات اخیر در واگذاری امور تغذیه به پیمانکار جدید و ناهماهنگی‌های اجرایی، محمولۀ غذا با تأخیر و حوالی ساعت ۱۲:۴۵ به خوابگاه رسید. این معطلی طولانی در شرایطی رخ داد که دانشجویان برای حضور در کلاس‌های بعدازظهر نیاز به صرف به‌موقع غذا داشتند.
🔹
در پی این ناهماهنگی، تعدادی از دانشجویان در ورودی سلف‌سرویس خوابگاه در اقدامی نمادین، حدود ۱۰۰ سینی و ظرف غذا را روی زمین چیدند و خواستار رسیدگی فوری مسئولان شدند.
🔹
بررسی میدانی خبرنگار فارس حاکی از این بود، فضای اعتراضی کاملاً صنفی بوده و هیچ‌گونه شعار هنجارشکنانه، درگیری یا تنش فیزیکی شکل نگرفت. ماجرا تنها معطلی بچه‌ها بر سر نرسیدن به‌موقع ناهار بود و مباحثی که برخی شبکه‌ها دربارۀ بهداشت یا کیفیت غذا مطرح کردند واقعیت ندارد.
🔹
پس از این و در پی این ماجرا، معاونت دانشجویی دانشگاه رازی ضمن پذیرش مسئولیت این رخداد، از دانشجویان عذرخواهی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464644" target="_blank">📅 01:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f797003eb.mp4?token=dqatQm4NK5jV_xI3-AoYg6i3hfcj7N5pfsKNL9hWb0CbJ6zlQa_xA2xUxIh1kP4-WCt6AnhBEqVmt122y1cELFuF3jNqMS0sxu_kHp6H9AYioJMfupSGKfi_CAL40bF_49bOGNphiX_kyF6k4Zs7gaBJrBOskBX481d2MprlYVaMTC0DJRxZFXOMWsW2ajSma1i4JL_k2NlknOzBF74r-xU-rQAtRAo2ymeNCrEFQkHKRh729FohtYaE3WAhweXFzQL_t6Dx1BuTKnsOZ4F_9XsCfFImLXofafiSjiVvujd8pihs-Igvrkylyf0xjqFRtlIUvp50yyANun9NS1NXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f797003eb.mp4?token=dqatQm4NK5jV_xI3-AoYg6i3hfcj7N5pfsKNL9hWb0CbJ6zlQa_xA2xUxIh1kP4-WCt6AnhBEqVmt122y1cELFuF3jNqMS0sxu_kHp6H9AYioJMfupSGKfi_CAL40bF_49bOGNphiX_kyF6k4Zs7gaBJrBOskBX481d2MprlYVaMTC0DJRxZFXOMWsW2ajSma1i4JL_k2NlknOzBF74r-xU-rQAtRAo2ymeNCrEFQkHKRh729FohtYaE3WAhweXFzQL_t6Dx1BuTKnsOZ4F_9XsCfFImLXofafiSjiVvujd8pihs-Igvrkylyf0xjqFRtlIUvp50yyANun9NS1NXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ کوله‌بری در کردستان
🔹
ربایش، ترور و اخاذی گروهک‌های تروریستی و تجزیه‌طلب در غرب کشور از کوله‌بران
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464643" target="_blank">📅 01:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfG-lJ0qHfQTxIXbMe46a8X6vIHvgK_tArq2fZzcJy2Cjr5ib4Gnk2Sb3EHN7aKqAjef__BO1xrK_MFpl9NYcSvbSxNFWJ1gfTfP8vrgql9o0a8FaQfGyoOaDzYgT6JPyl4vGZRURgzIz2eIZJ5UkhYzqLl7KMT5tsNNP-0l4IbknnuhRW-mQ7Pld7V_dxlAJlmKPBYfgtIgwGbK4bCZRGd6oDfqps9Z5pdwoTyJJ8hLvNw4mwYKhwbgKxSCvqOwOzxztLMxfxy8GZoccX0y_CW35ScSjJG1810WB4B6afpY0e4Df38OWgyosBrvPgGphXcs9-HM5jpMJoDFCM20kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار نهاد مدیریت آبراه خلیج فارس به مالکان کشتی‌ها در خصوص الزام شناورها به تردد از مسیرهای نامعتبر توسط برخی چارترها
🔹
گزارش‌های رسیده به این نهاد مبنی بر اینکه برخی چارترها، شناورها را مجبور به تردد از مسیرهای نامعتبر می‌کنند. این کار علاوه‌بر ایجاد…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464642" target="_blank">📅 01:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464641" target="_blank">📅 01:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌ عراقچی: از شروط خود کوتاه نمی‌آییم؛ بازشدن تنگۀ هرمز منوط به محقق‌شدن این شروط است
🔹
شروط ما مشخص است و هرگونه حرکت روبه‌جلو برای بازشدن تنگۀ هرمز منوط به محقق‌شدن این شروط است و از آن‌ها هم کوتاه نخواهیم آمد.
🔹
اولین واکنش را از رئیس‌جمهور آمریکا دیدیم،…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464640" target="_blank">📅 00:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز، باز می‌شد، رد کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464639" target="_blank">📅 00:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz_2EQIodFy1nWk3Qw5qmsjbW_DJ4uuyKKT6dYgBzyLjtaQkWY0WgWQvNollXcciFm_fSJ3YN3slRL3uyt6ednYYhqc0NJ05xvHLNJep9u_-KKu33RtBIFCedPUlCsSLiZvrR_dGOKlkj0Iov1jmAiAhQLL8eWnwWzWzUIlZyga7ObHshnBCL4dYixF4iy-d-cXnbI9ZJ7TLJ7TjMEED4BLsoFCWIZfUa8ae3vZhcA-oL8i9DhCHzejKo1Bix41hF6JnYZ0smKPmJcLDZQsAboXBBO7fKKAYqOgUL1Q2NPv4mBAFhzTzNkt9s_xyNayL5kKb6If9UxyJ5iNg1bb2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار نهاد مدیریت آبراه خلیج فارس به مالکان کشتی‌ها در خصوص الزام شناورها به تردد از مسیرهای نامعتبر توسط برخی چارترها
🔹
گزارش‌های رسیده به این نهاد مبنی بر اینکه برخی چارترها، شناورها را مجبور به تردد از مسیرهای نامعتبر می‌کنند. این کار علاوه‌بر ایجاد احتمال وقوع خسارت‌های مالی و جانی برای شناور، مالک، کاپیتان و خدمه، عبور آتی آن شناور از تنگۀ هرمز را نیز با محدودیت جدی مواجه می‌کند.
🔹
در صورت احراز تحلف چارترها، این شرکت‌ها به لیست عدم سازگاری اضافه شده و عبور کلیه شناورهای مربوط به آن‌ها از تنگۀ هرمز با محدودیت مواجه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464638" target="_blank">📅 00:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNY56bj6TsAEiTWsGdUNxny928syKGMqUkh0ZdvBoiIQ7BsdPpcfpQvrjEd4J_B_XJEgy3CS-9W85jTcnzzoL2yinyxtzEjOuUXgm5Gph2p-XNS1ExqpRB2hcTjlsybx00HbpFFRK9pDTRSdq2G1IrIgOdb6yjMTuzapBPUAHq-Co6bdvDTQuZIJgxg9d0bOOuYnuqo5-W5BphnjKjqBRO9ZvInAcq3B05OcaDtVs3eMR0XYT-gb1Mf4DqacrOPK3Bzo5NXrC-2CIss84UNYirAbw2z0mY4h2cyhgvR5tICovNndkrLDVAlZT6W-3B3C_XxuRAKux63FHe5n7oFsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: احیای اعتماد به سازمان ملل، نیازمند خاتمه‌دادن به بی‌کیفرمانی عاملان و آمران جنایات شدید بین‌المللی است
🔹
وزیر امور خارجه در دیدار با خلیل الرحمن، رئیس هشتادویکمین اجلاس مجمع عمومی سازمان ملل: تحقق شعار «بازسازی اعتماد به سازمان ملل متحد» بیش از همه مستلزم توقف نقض‌های فاحش اصول بنیادین منشور به‌ویژه اصل احترام به حاکمیت ملی کشورها و منع توسل به زور مندرج در بند ۲ منشور، جلوگیری از استفادۀ ابزاری از شورای امنیت، و نیز خاتمه‌دادن به بی‌کیفرمانی عاملان و آمران جنایات شدید بین‌المللی خصوصا تجاوز، نسل‌کشی و جنایات جنگی ارتکابی توسط رژیم صهیونیستی است.
🔹
تجاوز نظامی آمریکایی-اسرائیلی که در روز ۹ اسفند ۱۴۰۴ در حین مذاکرات هسته‌ای شروع شد و تا امروز به اشکال مختلف از جمله محاصره دریایی و تحریم اقتصادی ادامه یافته است هیچ منطقی جز زورگویی و قلدری ندارد و وضعیت ناامنی موجود در تنگه هرمز نیز نتیجه همین اقدامات تجاوزکارانه و مداخله‌جویانه است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464637" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs1iBKhH3eYYPgjCw2IkwgsVujBhnebtqmI7IR_gkrVh2Ix-M_CtyWzo67h9b5EyYqbFIRtzJt6fOxFhLlDO6UzvHlEsJHdEsJ7vZwo2uHkmXHg4r9r6j8W4Ihz2zUbbN5HcQh_G5K1PhrzCSeVGzvAfkWOXzsqmj_0YlcLYICsRNmtnphsyipWOPkyaiLsXu4yKpGLXoguhc-cVgRmG0asTkak_tjaRXiRdubczHmxJboEMgPA15HMuKreMGj_GBzxykV0HyAK0Rc4olyd5u9U5M_GmZFprr0GGBkwJVwb0J5TpgQd_pWAk9dFqwGW6pmgV0WdF-TokqAlpotHfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفره‌ای برای همه
🔹
حضرت ابراهیم(ع) در مهمان‌نوازی زبانزد بود و عادت داشت که تا مهمانی سر سفره‌اش نمی‌آمد، غذا نمی‌خورد. روزی یک شبانه‌روز گذشت و هیچ مهمانی نیامد؛ پس ایشان برای یافتن مهمان به صحرا رفت و با پیرمردی روبه‌رو شد.
🔹
وقتی از حال او جویا شد، فهمید که آن پیر، بت‌پرست و بیگانه با دین خداست. ابراهیم(ع) افسوس خورد و گفت: «ای کاش خداپرست بودی تا لحظه‌ای نمکِ ما را می‌چشیدی!» و او را مهمان نکرد. پیرمرد هم راهش را گرفت و رفت.
🔹
در همان لحظه جبرئیل نازل شد و پیام داد: «ای ابراهیم، خداوند می‌فرماید: این پیرمرد ۷۰ سال مشرک و بت‌پرست بود و ما روزی‌اش را قطع نکردیم؛ حال یک روز که سفره‌اش به تو واگذار شد، به جرم بیگانگی غذا را از او دریغ کردی؟!»
🔹
ابراهیم(ع) بی‌درنگ به دنبال پیرمرد دوید و او را بازگرداند. پیرمرد با تعجب پرسید: «علت آن رد کردنِ اول و این پذیرفتنِ آخر چیست؟» ابراهیم(ع) سرزنش و عتاب خداوند را برایش بازگو کرد. پیرمرد شگفت‌زده شد و گفت: «نافرمانیِ چنین خدای مهربانی از جوانمردی و مروت به دور است!» پس همان‌جا خداپرست شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464636" target="_blank">📅 00:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این محدوده نزدیک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464635" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS4rAR8u3ENfKKoPIcOvsnKz8E66-Di831phkgw02a9ZvJY_PyJUYPUvBW8CxuzDX5WYab4gCr28hbRSJCft2qzjmVKWjpc_Kf4FWDBpXsdB0Dr3DcaloPLL9SUbBaZuuhHCx_MdABFa-77MCCRF3Xw_e2oVKUB_JPOZ6xPs1UAFBI25C6Er43yS2fTk_sfdBTNDMbIMFgCpw-gFrkP-RC1HKwbOezk_W7JPeyWOKBC2tUIBaa_BCLWZFY6NnOm0zgBs5i6_Fbe0pd_uawGH2zvatzCaJqxqL8zIhgCsVhlYH8abS6Z5TwIwgDM-Zktq0tpO_wSXtEDUU6WX4EZZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464634" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx2xiz6a4SuyPner6-Vjn1ShAE0FxDLC0InzxWu3ZG2fXRKygqLdkYWaw21-XmSb5SdYYckYDmv8dnxGFzV-f29iyYxRfoZmRdx751TKoOYBsEy86jgMbF_1Bnm2pxKmmkpsLMJCS7-MD2y7Wjwww4TLAw3sf_dbUC3J7RlOJbamdP22YY3-n-EYKXKLY09eKyYDp5JTNth17Y2nokrfUwaqOa1yQf_5l__tas4N8KX381H8246FnSFV7GXRHIjNZhtSUuq55es0_t1SWpX7LCwmPvH6dwXCudlPQqOdn2nE2CmuwuSi6fypbNaiYYJW3U2UgCQ7zNFcWI3e8nVivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKdMfbUPfR6lwaRDMhgx1q8bwc0kKm0qfeMSdtFLDoS_x0LJt7cFWTVNOoLwt-m_vxD8NpViOQkjhTRSFnwd39hoKnmKtyKhMyJBCfKEEao6Uso2XoTWdlctxqA_ey0uKB0_vBE_KXJc2GisBa1rNRU-r5us_LeOj-tpEyA3AxaBL-7Rjt4HylCHDwRSQN6nXwXXOZcZcQ3jA4ymRpZO4UjXn51lkr__rtWFGynGPFEQ3KNzQBOpmZa50f64RX5acEa1imVXPGNkCcO-cwR6JqdWBiVFTY6odIpW2BMW7igKRiep1JTiht3P4fQTR3SNkp3v4_F-h1BpOWjbdQ3VuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S14QtXM2ZIGDbKfRotEMiOqZdhBLLY1_Detco_UH1X7MhSl1kM_ttlcm_Ar_3rD4V4eUn_Hx4awsWAPVyJ_sw9s5kXh06I-rC6vEySAMo8dzVQgokz_sW_ZXZ1ai85P13YaTKIC8LUgnRlvqdurEcDdhtG4Twu2PNFNBMsoG0ZgiZAVar6gRbHps1aGrx3vMF_ZavdjROpk4862VAf9ZYeQZmltTEyDux5KF_aNYKpU6IsPDOhrX-UjLVpUa1nvLVicUbm-RfDropAjWupDyA1436yxmMoIXYs07BvCx55w51KDH-VT8iS2z0NSmjbX8rnVVkWHR8TIC2twMQBSSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JktuMWYCUhQ0LRX7lsA7biCB-0EIJ5yaWYSDCYMxEFDnLzgbib9e_rqm90dlCwhO5_KGUOL5XBxjJM0JtMB-sMnJD7FG0-AKYUGzrtLFwBREWpuy879qlBBQ0RodQRTLd7zgAdOsg5lZL5pXb5ekum4PCw_2gde9kf7TCttq0iW-wpe__p-B4Uja6CU7x6mSJKY0iz1EZNnfs4556GeA7K5GFE2QP5Gw0fxB2C4YrhAhmsJW25jmf3MvU52WbBAuce-wZwjsHmNHJIuIvMdAnpg9AfZFQRwoR0MeyyMlHztr_cHKl5nPnKfLyMpQQpKaYLQbfCTJ4sp9g0RLkvhDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh403N477eesB504JCrugduGZfLb1aIoJ0TkwUniVd1HpaDZtcegJQyskZwJ2AIfj3cF1DYH7l4PnEt6QqWYOD3J99O9hc_J9jKc5hQarB7xMMqfGzrqs28vwSqWByJxp3G7S49tKoyP7-IUNlTNtJDnFWIP5_vn6PQzrdHG_Ua9zXJB5uMF5r91bXcCDq4IayjXfPQji4wLhGdujWsHDxa_yg1Zi9HIThvofqqSE63w9r5pUR_KRLq9cbto5A7hk3a5fun9HT-k2Q87VcF_zmhS2_6_sqBZ6Yr66ol3IejPGvkYyxNnBhdzoX8-Qtl_8IOihe8i4pbYNgC7YL4dfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuoZU8BKOHkE4S4FL6RfDm_Yd_zCxo0Ey2KtIp226HWxL_PwWCb_prL4grJfNOssgXSIewOVO95JKLYLi4frxtCOcW1wr2lEnm8Vy8P1ibS7qNymRYzkgXG7v3kUSQlDkqliMMHQGiwXN8Ur494kyxi2HqnyenzFWvnteNBfBVqmk-n-f2w7et7UjpDNRIZ2A17NpXPCZdmt63xtsYBjb9VeXgp-yOmi6EIy0F1q6hYDLdivWPT4hI4mf5cEf_Nu9lcFm-LqqcSvEIePCxwUR5oJcSDHMft5A69XOwfwuQ1SB7WHRYWw_hLXNHk7JRYyxLnC-0Qpvdxt2J2WWZ7Xzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پیکر سردار شهید «حسین ظریفی» در گناباد تشییع شد
🔹
شهید سردار سرتیپ پاسدار حسین ظریفی فرماندهٔ قرارگاه سجاد سراوان در عملیات مقابله با اشرار مسلح که منجر به درک واصل‌شدن تیم تروریستی واقع در شهرستان سروان شد، به درجهٔ رفیع شهادت نائل آمد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464628" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری فارس</strong></div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
لطفا برای
افزایش شدید قیمت داروها
چاره‌ای اندیشیده شود. چهار ماه پیش هزینه داروهای من حدود ۲ میلیون و ۵۰۰ هزار تومان بود اما اکنون برای همان داروها باید تقریباً دو برابر پرداخت کنم؛ آن هم برای داروهای ایرانی و تولید داخل. با این افزایش قیمت، بسیاری از مردم توان ادامه درمان را ندارند. خواهشمندیم
ارز ترجیحی برای دارو را برگردانید
.
🔹
من به‌عنوان یک شهروند ایرانی نسبت به
هزینه‌های تلفن ثابت
اعتراض دارم. چرا حتی اگر از تلفن ثابت استفاده چندانی نکنیم، باز هم باید هر ماه مبلغ قابل‌توجهی پرداخت کنیم؟ کسانی که بیشتر استفاده می‌کنند هزینه بیشتری پرداخت کنند؛ چرا افرادی که مصرف کمی دارند باید همان هزینه‌ها را بپردازند؟ ما این مبالغ را با سختی و نارضایتی پرداخت می‌کنیم.
🔹
اواخر سال گذشته شرکت
پارس‌خودرو
طرحی با عنوان «
مشارکت در ساخت
» ارائه کرد و مشتریان با پرداخت مبالغی مانند ۶۲۵ میلیون تومان، معادل ۵۰ درصد قیمت تمام‌شده خودرو در آن زمان، پذیرفتند خودرو در سال ۱۴۰۶ تحویل شود و ریسک افزایش قیمت را نیز بپذیرند. اما اکنون مشخص شده که شرکت قصد دارد در
زمان تحویل مابقی مبلغ را بر اساس قیمت تمام‌شده سال ۱۴۰۶ محاسبه کند
! ما می‌خواهیم بدانیم چرا سازمان‌های نظارتی (مانند وزارت صمت و شورای حمایت از مصرف‌کننده) اجازه می‌دهند که از سرمایه خانوارها در چنین قراردادهای ناعادلانه‌ای استفاده شود؟ من و صدها و شاید هزاران نفر مثل من تمام اندوخته سال‌ها کار و  زندگی خود را در این طرح سرمایه‌گذاری کرده‌ایم صرف کرده‌ایم. خواهشمندیم دستگاه‌های نظارتی موضوع را بررسی کنند و اجازه ندهند حقوق مشارکت‌کنندگان تضییع شود. ما فقط خواهان اجرای عادلانه قرارداد و حفظ حقوق خود هستیم.
🔹
به‌دلیل عدم مراجعه
مأمور گاز منطقه ۵ تهران
(ریاحی)، طی هشت ماه گذشته چندین بار به اداره مربوطه مراجعه کرده‌ام اما هنوز مشکل حل نشده است. متأسفانه
نحوه پاسخگویی و برخورد کارکنان نیز مناسب نیست
؛ حتی هنگام مراجعه یکی از کارکنان حدود ساعت ۱۰ صبح مشغول خوردن صبحانه بود و پاسخگو نبود و برای ثبت شکایت نیز به‌جای فرم مربوط، یک برگه باطله جلوی من گذاشتند.
🔹
چند روز است
امکان برداشت وجه از پلتفرم «میلی» برای کاربران با مشکل مواجه شده
و بسیاری از افراد نمی‌توانند سرمایه خود را برداشت کنند. این وضعیت باعث نگرانی و استرس کاربران درباره سرمایه‌شان شده است.
🔹
فاضلاب‌های
محدودۀ بیمارستان یازهرای دزفول
کاملاً گرفته و پر از زباله است و کسی برای پاک‌سازی آن اقدام نمی‌کند. پارسال با بارندگی، فاضلاب وارد خیابان‌ها و حتی منازل مردم شد و خسارت زیادی به فرش و وسایل زندگی وارد کرد. از طرفی کابل‌های تلفن نیز به سرقت می‌رود و مخابرات اعلام می‌کند مردم باید خودشان کابل را خریداری کنند تا برای اتصال اقدام کنیم. بسیاری از مردم توان پرداخت این هزینه‌ها را ندارند.
🔹
ما ساکن
تهران
هستیم و با اعتماد به
تبلیغات یک مرکز ایمپلنت
، پارسال برج هشت برای ایمپلت یک واحد دندان مراجعه کردیم. همان روز اول کل هزینه را پرداخت کردیم اما حالا با گذشت بیش از ۱۰ ماه،
درمان هنوز کامل نشده
و دندان نیمه‌کاره مانده و برای روکش آن نیز پاسخ روشنی دریافت نمی‌کنیم. با وجود پیگیری‌های متعدد، هنوز کسی مسئولیت این تأخیر را نمی‌پذیرد. نمی‌دانیم برای شکایت باید به کجا مراجعه کنیم.
🔹
چند روز پیش از
دیجی‌کالا
جت ۲ کیلو گوشت خورشتی و ۲ کیلو سردست خریداری کردم. گوشت بوی نامطبوع داشت و پس از وزن کردن، مشخص شد در مجموع حدود ۶۰۰ گرم کسری دارد و دو استخوان نیز داخل گوشت خورشتی بوده است. موضوع را بلافاصله با
پشتیبانی
مطرح کردم، اما
پس از ۲۴ ساعت گفتند
چون گوشت شسته شده،
امکان پیگیری ندارند
؛ در حالی که خود پشتیبانی قبلاً درباره نحوه نگهداری آن راهنمایی متفاوتی داده بود.
🔹
ما پرسنل مراکز بهداشتی و درمانی دا
نشگاه علوم پزشکی جندی‌شاپور اهواز
نسبت به
عدم تعطیلی پنجشنبه‌ها
اعتراض داریم. در شرایط گرمای شدید خوزستان، در حالی که کارکنان ستادی پنجشنبه‌ها تعطیل هستند، ما که بسیاری از پرسنل را بانوان و مادران شاغل تشکیل می‌دهند تنها یک روز جمعه را برای رسیدگی به خانواده داریم. با توجه به تعطیلی پنجشنبه‌ها در برخی از دانشگاه‌های علوم پزشکی استان‌های دیگر، از مسئولان دانشگاه تقاضا داریم با نگاهی عدالت‌محور و برای حفظ سلامت روان و بنیان خانواده پرسنل و با توجه به شروع مدارس، نسبت به این موضوع تجدیدنظر کنند.
🔹
فاصله شهرستان
قوچان تا مرز ترکمنستان
حدود ۸۵ کیلومتر و تا عشق‌آباد نیز حدود ۱۵ کیلومتر است. با توجه به اهمیت این مسیر، از وزیر محترم راه و شهرسازی تقاضا داریم موضوع احداث
راه‌آهن قوچان-اجگیران-عشق‌آباد
را بررسی و برای اجرای این طرح مهم اقدام کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsnaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464627" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a148085b.mp4?token=hgm4nDv44KoafWtbBHUVD0HJ7kb6hs7Xa-2581ekrfY69NTefqs6NYJLShLtSvZvHWhS9NLBFbqGGtAoUFGrYNog1QAxdf_-aZ5LfdIISBq7YP58vfOjiPq70YWl016hDsxujMo-s9deG-3h0u63QxFjD6TLsWB7ClmSpAn4H1KjMBZFFfjZMsB3Kd6QViq7-Beu70o6p7Fe9y17qSDgfk8zBZ5PorXIs7v0IANnwNUkA2eDB4N6XxMLNt8p1eOLPRBGAEWtNuLyNdT_DB6ZMzrN4HBfTRLiqz2aCjxFVJOvhH8XsDvjix5_djIy9ygkIZfu3uT4La5zq2SuxVStuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a148085b.mp4?token=hgm4nDv44KoafWtbBHUVD0HJ7kb6hs7Xa-2581ekrfY69NTefqs6NYJLShLtSvZvHWhS9NLBFbqGGtAoUFGrYNog1QAxdf_-aZ5LfdIISBq7YP58vfOjiPq70YWl016hDsxujMo-s9deG-3h0u63QxFjD6TLsWB7ClmSpAn4H1KjMBZFFfjZMsB3Kd6QViq7-Beu70o6p7Fe9y17qSDgfk8zBZ5PorXIs7v0IANnwNUkA2eDB4N6XxMLNt8p1eOLPRBGAEWtNuLyNdT_DB6ZMzrN4HBfTRLiqz2aCjxFVJOvhH8XsDvjix5_djIy9ygkIZfu3uT4La5zq2SuxVStuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی محکمی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.  @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/464626" target="_blank">📅 23:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=W2uXYtsJzX7IAHi4u7HA4FVASkAL7bs0dogALAzfv2WifbOcTc8Pqh-6_s-LCosgHbHKinYR_7_OXgCdH1fB1nKi7S6VQQ1ow4OfK3iVEYFaEStsPuvCpOZdPIZGSOA_AJ9Wdd-buQAX-OJkBL-n6dCnBRc0P-BAqJMpxGGaDFtHA01REOz74RjrGVW8hckrplmP4TC36LjibSyBI925b74t_lifZqi2JRz_THYB9smKFRJbW9wxKn0P7Qjx55ddeq-LJnm5JOGl547lZ85rP5fo-YZJnWAFjvuZOtV3nYnBxt63Bi0hcGHQU1Rz8nKSM0Sa3wB2vHnmNpjsCO4m8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594ed02de3.mp4?token=W2uXYtsJzX7IAHi4u7HA4FVASkAL7bs0dogALAzfv2WifbOcTc8Pqh-6_s-LCosgHbHKinYR_7_OXgCdH1fB1nKi7S6VQQ1ow4OfK3iVEYFaEStsPuvCpOZdPIZGSOA_AJ9Wdd-buQAX-OJkBL-n6dCnBRc0P-BAqJMpxGGaDFtHA01REOz74RjrGVW8hckrplmP4TC36LjibSyBI925b74t_lifZqi2JRz_THYB9smKFRJbW9wxKn0P7Qjx55ddeq-LJnm5JOGl547lZ85rP5fo-YZJnWAFjvuZOtV3nYnBxt63Bi0hcGHQU1Rz8nKSM0Sa3wB2vHnmNpjsCO4m8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: از ترامپ و نتانیاهو و دیگر قاتلان امام شهیدمان نخواهیم گذشت؛ این موضوع دیر و زود دارد اما سوخت‌‌وسوز ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464625" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313b69d364.mp4?token=bnposFo26ybXEdtHCFhn8xb6dvL4dSbw5OCAgdlLYO7Uasg6WbudnUWgrNd-V3Dsq1iO_lugecLHWLrhlKj6_w1VQeY-aZY7nSuBehpPcElp9PCkr6B0qluxzk76C7nTLH6gk-42qj036i5TsrEOL6oGNIQNnjKbXdmtfaXSbFs6n-SGFS8Zv2n7WgectvG-Rd8Da9wsEOofB24xB7G_pcj4xsAUALchxjRgKdGSFz62NW69oL-Y8TT0YqNf6n8MAZqrzMLQcZ6LAb66g-zYzx2icWlpJhxK4wPtTJGGiwBu7z0UECDI_ROJrfsrlD3mFb4bIlPXLbH1nDoq88RfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: هر کشتی‌ که خارج از مسیر تعیین‌شده توسط ایران از تنگهٔ هرمز عبور کند، امنیت نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464624" target="_blank">📅 23:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2c3d0ca7.mp4?token=SNQO86zf7w80cWT_uGa0ZZBiwjADN9kavsT9j9y9r43XVYkggnMZ1mRX624Pqvw5rUx-YFNO8URToOZqMpPMCMa4qOK0fQ01Dvwv6o6er0GPwr71TYyNvyHcN82Fh9qlSGOVZ_3bd-Fh8sAQnyRRYFdAckdaulwVQYCmTua7V8TGXcuVEbUeRXzC2mJ80yzfIJRKEnHLR4IrrQJ5PllU8IMA9ySDsFun3xRQfLI3_7CJyVbQwurbr5t1_ajb8f748foDY4f5UAI6zp3gJQL4gmJG4xV9am6TrMjJ2QwQFyb_OpqoMvbqputewmBirYU_19swDEigEq1qakWH-32yYIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2c3d0ca7.mp4?token=SNQO86zf7w80cWT_uGa0ZZBiwjADN9kavsT9j9y9r43XVYkggnMZ1mRX624Pqvw5rUx-YFNO8URToOZqMpPMCMa4qOK0fQ01Dvwv6o6er0GPwr71TYyNvyHcN82Fh9qlSGOVZ_3bd-Fh8sAQnyRRYFdAckdaulwVQYCmTua7V8TGXcuVEbUeRXzC2mJ80yzfIJRKEnHLR4IrrQJ5PllU8IMA9ySDsFun3xRQfLI3_7CJyVbQwurbr5t1_ajb8f748foDY4f5UAI6zp3gJQL4gmJG4xV9am6TrMjJ2QwQFyb_OpqoMvbqputewmBirYU_19swDEigEq1qakWH-32yYIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: اراده کرده‌ایم که کوچک‌ترین عقب‌نشینی در برابر دشمن نداشته باشیم و او را سرکوب کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/464623" target="_blank">📅 23:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoS7YArFJ96qVwrmpeb6vvmu5tvP_1-pTboccVVviZq5dmlxjHHa-dVAd68-8dviyfihJdxx1ArulPXTExQ0bn9Wz-JM4T80GQeqb51EXaGqPEbQR1AP946uPavzYAKR8ZpWAG9gQRTKVAbmd5xtB2toeDB_2cFLw6QRzJ27HG-N4e_pwSmO6KoeU82DcmMS9iUwmmV1OXf_uijGFnUnKulJkWkQbx0HmRHjmNdokWcCwpgrVZGSz8NPrM14-wVyJba2gJu3BpZEvQOftUhcIghU9C3I7Mj7VN3IDmXCRR2B7WsiT9TPomYckcF1TVwSt6VWXfhwcUDga3Ftfc9yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما برایمان از شباهت‌های جنگ تحمیلی اول و سوم بنویسید
🔹
در جنگ تحمیلی ۸ ساله، مسجدها یکی از کانون‌های حضور و همراهی مردم بودند و در جنگ اخیر، میدان‌ها و فضاهای شهری به محل حضور مردم تبدیل شدند. شما چه شباهت‌هایی میان این دو تجربه می‌بینید؟
🔹
دهه ۶۰، در میانه جنگ تحمیلی، مسجد فقط محل عبادت نبود؛ بلکه در بسیاری از محله‌ها به مرکز رفت‌وآمد و همدلی مردم تبدیل شده بود. کمک‌های مردمی در مسجدها جمع می‌شد، جوان‌ها از همان‌جا راهی جبهه می‌شدند و مردم هر طور که می‌توانستند درگیر جنگ و پشتیبانی از آن بودند.
🔹
سال‌ها گذشت و نسل‌ها تغییر کرد. در جنگ اخیر نیز میدان‌ها و فضاهای شهری محل تجمع و حضور مردم شد و شکل دیگری از همدلی و همراهی مردم به نمایش درآمد.
🖼
به نظر شما مردم در این دو دوره چه تجربه‌های مشترکی داشتند و چه چیزهایی تغییر کرده است؟
🔸
خاطره، روایت یا تجربه خودتان را با هشتگ
#دفاع_مقدس_سوم
در سامانه فارس تعاملی منتشر یا از طریق
@Interactive_Fars
و
@fars_ma
ارسال کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/464622" target="_blank">📅 23:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: هم موشک‌ها و هم پهپادهایمان نسبت به جنگ پیشرفته‌تر شده و هم به فناوری‌های نظامی جدید دست پیداکردیم که در صورت خطای دشمن ضربه‌ای کوبنده به آن بزنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/464621" target="_blank">📅 23:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910aa6b505.mp4?token=gPCKuC1wHoETQZGNCRMOzAWzy15P5w7IbgqRekyCrtvSai1HOl5xG8ci9czUhxQCrjSmiCU2874-WRB0quCKmL6vAXz3Zlc9CMvUgnhLAICcjWouUsA-We9Y-4aBZfPpTnblU8QySsjr6CIo5VpAbuje8XKiH3iDh5JbMvq6Y6qKEqv0CegL4DB_DwXcc9UuE6pESUOq1vsy94v1QuN9OneIp5dNteyGgmE0FCj95o-NbvpNx79VYi__ncsG-9g-PDGK9w9IvJxUspCbNn2-fwk3eCLvw6UmzcMi_T5JLGOeU7jkuuUKEiuxhdgR5KBG0OrzryyrYoKxb4IPHmRqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910aa6b505.mp4?token=gPCKuC1wHoETQZGNCRMOzAWzy15P5w7IbgqRekyCrtvSai1HOl5xG8ci9czUhxQCrjSmiCU2874-WRB0quCKmL6vAXz3Zlc9CMvUgnhLAICcjWouUsA-We9Y-4aBZfPpTnblU8QySsjr6CIo5VpAbuje8XKiH3iDh5JbMvq6Y6qKEqv0CegL4DB_DwXcc9UuE6pESUOq1vsy94v1QuN9OneIp5dNteyGgmE0FCj95o-NbvpNx79VYi__ncsG-9g-PDGK9w9IvJxUspCbNn2-fwk3eCLvw6UmzcMi_T5JLGOeU7jkuuUKEiuxhdgR5KBG0OrzryyrYoKxb4IPHmRqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سخنگوی ارشد نیروهای مسلح: کشورهای همسایه توقع نداشته باشند که از خاک آن‌ها به ایران حمله شود و ما تماشاگر باشیم
🔹
اگر کشورهای منطقه به دشمن ما کمک نمی‌کردند امروز خودشان روزگار بهتری داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/464620" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebce47bd5.mp4?token=NtATjtUeY8R0rNhaoPPCxC84zbejK2NHuXuJKTjGoSiHACSFgXHP8ZrFQUEpDZYOUA9ETutbCHZBpMzjG4GSmr5fCiy_OvK3qheD_NTYiXMnbAptq1yzLp6Np6zm0oPDxsmZVLUoQl-UfOMovupubWkWhxt3jB3iYbVyegrGXuusRQGEvgngaAqAXlAhLHwHViIBl2myPrKCm6EJybwnDZA5QQXEPm6QNm9Md9FYFKjtPEpFEOM75Fuhr-wl2I4PkEDVx6dR-hNSpmk-QuwdpXeH1YZbanKa2g0jt0c9JAESpeIuX-Wd_QDYhSPaMlHIjqGHw0YrxBMxmltqXe5s6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebce47bd5.mp4?token=NtATjtUeY8R0rNhaoPPCxC84zbejK2NHuXuJKTjGoSiHACSFgXHP8ZrFQUEpDZYOUA9ETutbCHZBpMzjG4GSmr5fCiy_OvK3qheD_NTYiXMnbAptq1yzLp6Np6zm0oPDxsmZVLUoQl-UfOMovupubWkWhxt3jB3iYbVyegrGXuusRQGEvgngaAqAXlAhLHwHViIBl2myPrKCm6EJybwnDZA5QQXEPm6QNm9Md9FYFKjtPEpFEOM75Fuhr-wl2I4PkEDVx6dR-hNSpmk-QuwdpXeH1YZbanKa2g0jt0c9JAESpeIuX-Wd_QDYhSPaMlHIjqGHw0YrxBMxmltqXe5s6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها همۀ توانی که برای جنگ جهانی سوم کنار گذاشته بودند را مقابل ایران به‌کار گرفتند و دستاوردی نداشتند  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/464619" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464618">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc560477a.mp4?token=QcNxOv5z1QvDEe_FlNTsqLiXoqROVAz5gyOI6nnvDhdrcvG6t2vlquBmnYcTCTNPEOVMynBCET2DqNxipZZCuPkBbIZSxgf1PAJMJ-Cz_2SrHgnt-8Xr5kXc-E7LlycPoKo5XCkC3cbclPm4r7spQxG1jTN6D8mI5pClNY3u4Q79UipiQE2ZZ6gPDEYiFnukuWr-CPFDZuLsuv8G71-YFcROfrGySAC6T16u5iVvShsxcVs4F8JoKs5Dnn2oTsvIjK1ytSoMHBxjAfIxUf1MQhFdYwUkDG_cfUXSdXkqOmWLo9Nu493jc7mqBIMzRwtTAOJXYmMudxZf6EuTcepr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc560477a.mp4?token=QcNxOv5z1QvDEe_FlNTsqLiXoqROVAz5gyOI6nnvDhdrcvG6t2vlquBmnYcTCTNPEOVMynBCET2DqNxipZZCuPkBbIZSxgf1PAJMJ-Cz_2SrHgnt-8Xr5kXc-E7LlycPoKo5XCkC3cbclPm4r7spQxG1jTN6D8mI5pClNY3u4Q79UipiQE2ZZ6gPDEYiFnukuWr-CPFDZuLsuv8G71-YFcROfrGySAC6T16u5iVvShsxcVs4F8JoKs5Dnn2oTsvIjK1ytSoMHBxjAfIxUf1MQhFdYwUkDG_cfUXSdXkqOmWLo9Nu493jc7mqBIMzRwtTAOJXYmMudxZf6EuTcepr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: حضور مردم ایران یکی از ارکان اصلی ما در مقابل دشمن است  @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/464618" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464617">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b656c15c7.mp4?token=AQrBcw_qTuxpFyMMATIb5PGH6dU-0SDikav0ec-jcemRXrpThvqb5PoV9qxLqOdkEvCk2wRKqpBuCq3rWaoQ7qPzMbEdLCQJVFeN8kVmoWWtIYLdFzP3upq8g58hrcsPis-hM_mJc6OelzsnVQT6Sh7YYp-F43Ll7aTAi0yZclNtqXlnOdIQDwUYSk37PkoZD2kC-b9Ya6JSMtXvKe6Dnn5mOcM6Bq-9U_j8sLv2j_7JQik3JF5-4uhZToFKyx_g-Yokpi-oMkgo2YQjA9B064Fk-xcgbcZQopSOUGk4r7coLee1baEXvZwmsSHqYVr816Y9b1AuNKjbVpO5BsNbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b656c15c7.mp4?token=AQrBcw_qTuxpFyMMATIb5PGH6dU-0SDikav0ec-jcemRXrpThvqb5PoV9qxLqOdkEvCk2wRKqpBuCq3rWaoQ7qPzMbEdLCQJVFeN8kVmoWWtIYLdFzP3upq8g58hrcsPis-hM_mJc6OelzsnVQT6Sh7YYp-F43Ll7aTAi0yZclNtqXlnOdIQDwUYSk37PkoZD2kC-b9Ya6JSMtXvKe6Dnn5mOcM6Bq-9U_j8sLv2j_7JQik3JF5-4uhZToFKyx_g-Yokpi-oMkgo2YQjA9B064Fk-xcgbcZQopSOUGk4r7coLee1baEXvZwmsSHqYVr816Y9b1AuNKjbVpO5BsNbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: ایران مجرب‌ترین کشور جهان در جنگ نامتقارن است  @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/464617" target="_blank">📅 23:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrMGRDguxQ9cLZaYnxPdFB9rwqwp3uGkPhW1wpxoGdqCVgG6lOX-dwl3-Nahtb2r6gAN80pzRhFMcIzgonul2AvjiA-ucPrDi4yt78_QYutdgtrQ7X4WYNnsOkapancEbo1dKqbcAU68pBh27I-KZTPAPt6aGN7AAKv8feJxXar_MS0sGmBl4IzTfs906OcnofGnexnvlD0dF7z0dFUmb5uN3kD0X6uPDxabz0DIQwzQY3pd3JU-XSSoXue0hkRfFBCMksu2uSIzPsDJXodzSfivMaqqw8LvOEhoqU4e2vr7y_jqpaHERQePULsOVAxAiEMlZfvKXuNc-WwHr33lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0dX-IWnKC5uMq19LtsoFpE1cnNgi8X_91xAqw_W-kjlJkeSg_Ky5gPm89PAhTeXVBa7iGXqlSk6t6pVyGjAUVbG6P5cEs53_ah2V3whK4gnKac8Rj90u7bEkJxXoAq6amsh7IBJ8AeFokQajOSKIVEPMtJ6rPN05QFcPtkK25EG5mWFhGdXWlZZ1tW36JKTdeRvQ8sEbOfA6A5D6sWP3JyWZsauMIkrdL_xEINcKWa5SEMDEoX5pUcY981pDr4G3ixZ5q_aRw0zKgiVADVW7G9ih7iISQM0c6xSfjsEfJAMIcjUduXkE4OkNN4vWe39BRjUkKu5LeNUqRnEC1ngCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yykd1_iigYhnJouldtrL7ttODZOYb91zetk_xCqPppYTrI_JVl9urMfIvqXyXDAxJtSudztbkZB65DZzELUtN9O93L-HVMOx4xXKwr0sPmixKhkQZetzZGuXvlaiwhIBlnk1qqQIW1gBp17xEowTlkk9ltbWyrUDqk0zD7q8DneojexJMhv56WZ2-LSbEZwIKDZUveaDy0RABfJJf2h-ifftdXaj_uS8YwMfAp4-jBscvbRG4Z3SSCeLrD0vPN-P3y4z7ck7h98DCudvG8mQ-yeZwIBas158mOboG_Vz5ybchFOiACQ4vm9IkW8aQTefdTGMksxQk55_1ZQxaSRiyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حملات شبانۀ اسرائیل به جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/464614" target="_blank">📅 23:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab20f1aec.mp4?token=sE4_EeGjHlskXHno5QANHhhxZTc4jkHrLNb952vIzG_q8MliQcWk9EcrxOd5p3IV-BaLhPqXkP5jTcAW1qyV_qDQnGtpGNd7JLfvDxuXEnHAN4rSDIXGy46UYg1Nu1s6hHHJAHP8EJxVbTNmFLIV8oQDTZIkiMWTE0pxVNY3J4UvA1VHmaxo-mb_6t14kUqFFs9aRpvIpTTzSuvRuD5VO5qzy3jASBqQee97m4yUZY3hSMJ63-hkdxzCPNyflkricdrfyb19hP-re4FHPoUpUTznwuHxCC9zpurJunDsZrm8rrus-jbTnMFgk8PmL2KGH5BWOhg4gqn_rWz-KXuvCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab20f1aec.mp4?token=sE4_EeGjHlskXHno5QANHhhxZTc4jkHrLNb952vIzG_q8MliQcWk9EcrxOd5p3IV-BaLhPqXkP5jTcAW1qyV_qDQnGtpGNd7JLfvDxuXEnHAN4rSDIXGy46UYg1Nu1s6hHHJAHP8EJxVbTNmFLIV8oQDTZIkiMWTE0pxVNY3J4UvA1VHmaxo-mb_6t14kUqFFs9aRpvIpTTzSuvRuD5VO5qzy3jASBqQee97m4yUZY3hSMJ63-hkdxzCPNyflkricdrfyb19hP-re4FHPoUpUTznwuHxCC9zpurJunDsZrm8rrus-jbTnMFgk8PmL2KGH5BWOhg4gqn_rWz-KXuvCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارشد نیروهای مسلح: ایران مجرب‌ترین کشور جهان در جنگ نامتقارن است
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464613" target="_blank">📅 22:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee88ddd6e.mp4?token=tdICPvGhtrrkea23zZVCrdKHbehZTfMmMDO7OCpyrrVs5eYE3GOOLUoy4xvylu2mwneL_L28TaNvRvANvhzgZSDmXFkCoHoMr-sWyfGTDpab66BV7QAZJ0QQuUu-Q9DY1Z9OXLWUvl46bjqmFgN_JLhx3atNjNtQfXcDeMFv8o78nkJh85nXvWTAiOMWwyKbv2H9_fuv7-gFh8NAJ0SJrYX_WedcX_SYW2oIoGbYiJNj_ohulc2A0T6__4a_S-cnCHYxy9CfsvwF917Qq9Zlc7-6IovA7MgVQP9QKuamEHOT-yE7fXgx7KYz7tg4raa8XI8LzuiaIGZ62A_CUtgTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee88ddd6e.mp4?token=tdICPvGhtrrkea23zZVCrdKHbehZTfMmMDO7OCpyrrVs5eYE3GOOLUoy4xvylu2mwneL_L28TaNvRvANvhzgZSDmXFkCoHoMr-sWyfGTDpab66BV7QAZJ0QQuUu-Q9DY1Z9OXLWUvl46bjqmFgN_JLhx3atNjNtQfXcDeMFv8o78nkJh85nXvWTAiOMWwyKbv2H9_fuv7-gFh8NAJ0SJrYX_WedcX_SYW2oIoGbYiJNj_ohulc2A0T6__4a_S-cnCHYxy9CfsvwF917Qq9Zlc7-6IovA7MgVQP9QKuamEHOT-yE7fXgx7KYz7tg4raa8XI8LzuiaIGZ62A_CUtgTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در بازگشت از نیویورک: صحبت‌های ترامپ نحوۀ سخرانی من در سازمان ملل را تغییر داد  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464612" target="_blank">📅 22:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d245dc30.mp4?token=mwR-kjvE-KbI9l1ahFVQrFvUy5wLCl6GsYzYr3fNcz4QEcKDgjHk2oelHjnvGFpGUnaF8JWf22_W_FHhENUnRs1wfizHe9FpLEB9l1OW0H9boRBJwjeFY-rGbstqr6Crff80-T9WHr_g4H350vE_4LPirZQtbOkC4w90qSiNRAOZ5Qp_pn6kCjjv4JFmD0tsDKskjLAPDWI4ZcSWfADLeebhRWuz_W_LEefonjaLu5Efc8v1UNaJLSaL-HJqtFXqK1JZgetMVkpGNT508afmG17qaOI26oFA7YInDVJeRPimMnOAQLAZ_KnwM8hs8tptlXHg2wj1kybXlVtMmT4eaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d245dc30.mp4?token=mwR-kjvE-KbI9l1ahFVQrFvUy5wLCl6GsYzYr3fNcz4QEcKDgjHk2oelHjnvGFpGUnaF8JWf22_W_FHhENUnRs1wfizHe9FpLEB9l1OW0H9boRBJwjeFY-rGbstqr6Crff80-T9WHr_g4H350vE_4LPirZQtbOkC4w90qSiNRAOZ5Qp_pn6kCjjv4JFmD0tsDKskjLAPDWI4ZcSWfADLeebhRWuz_W_LEefonjaLu5Efc8v1UNaJLSaL-HJqtFXqK1JZgetMVkpGNT508afmG17qaOI26oFA7YInDVJeRPimMnOAQLAZ_KnwM8hs8tptlXHg2wj1kybXlVtMmT4eaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پزشکیان نیویورک را به مقصد تهران ترک کرد
🔹
رئیس‌جمهور پس از شرکت و سخنرانی در مجمع عمومی سازمان ملل نیویورک را به مقصد تهران ترک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464611" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
آن‌که گفت هیهات منّا الذّله!
🗓
۲۶ سپتامبر، سالروز شهادت سید مقاومت، شهید سیدحسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464610" target="_blank">📅 22:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6447471c66.mp4?token=DHTYS42GGclTe9rLh_2Ry38MItUE7hMD8xclst2q6WKgQSP6kEMeDNjSgqdCI_r5EAdBWkVY0v35pHrL07fXD6GpY8vDnJNujs__hDB8DcrW518ICptJ293fPEdPOdQM1d36o9bxeTU99TCTjxZysB-vr9ZlcwhxJWI-7yLv36_XspqdKxb2_Iut_vjm7MpULdVDLuYTjWoPtmmv2saPcmCmLA1goU0snU-ZL6VCDuMzspDMYMk76ng1umvVkFyoVZRNMaXgldD5bD8aG089oyXewqq6VP4XSllxms74i2bjh0wkKxixgn7mW1EQDjVBRyVfQ15zfOoFM7YFcau37g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6447471c66.mp4?token=DHTYS42GGclTe9rLh_2Ry38MItUE7hMD8xclst2q6WKgQSP6kEMeDNjSgqdCI_r5EAdBWkVY0v35pHrL07fXD6GpY8vDnJNujs__hDB8DcrW518ICptJ293fPEdPOdQM1d36o9bxeTU99TCTjxZysB-vr9ZlcwhxJWI-7yLv36_XspqdKxb2_Iut_vjm7MpULdVDLuYTjWoPtmmv2saPcmCmLA1goU0snU-ZL6VCDuMzspDMYMk76ng1umvVkFyoVZRNMaXgldD5bD8aG089oyXewqq6VP4XSllxms74i2bjh0wkKxixgn7mW1EQDjVBRyVfQ15zfOoFM7YFcau37g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🔹
رژیم صهیونیستی که وحشیانه‌ترین کارها را در غزه انجام داده و نتوانسته آنان را وادار به تسلیم کند می‌خواهد ایران با ۹۲ میلیون نفر را تسلیم کند؟
🔹
نتانیاهو ترامپ…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464609" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd04dde131.mp4?token=iYkOrJnaKhqmytAotNdrr9VaiW-EnjuS8_1CkP2-cAy-cz40iAcU8uoxafPjgwZx-VFYz4dohJo7gXDZcEUMZomD3azO3au2psR-GbJqkFrga9dxC7BVV8aTw1CHQ7y2BZdMSw4kWV3FbD6RR006I3w8-rhMoHh83sGjQSP-7EEtO4DKeZ3a-Ohr4NPyRA4a6pmRY4P_MARNWmHowssZw1m4lWpX05DEAYsIZpBgzMl7KEBgE9bIQSU1wjBsCks1C5MnwPKx0hY7s5P2iIZ_vVwMs0WYo311BLj-8zHdiYZxdN4AGEbCitby6rSIWKi9DEiiwopDR_UW2JyGZ7_A9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd04dde131.mp4?token=iYkOrJnaKhqmytAotNdrr9VaiW-EnjuS8_1CkP2-cAy-cz40iAcU8uoxafPjgwZx-VFYz4dohJo7gXDZcEUMZomD3azO3au2psR-GbJqkFrga9dxC7BVV8aTw1CHQ7y2BZdMSw4kWV3FbD6RR006I3w8-rhMoHh83sGjQSP-7EEtO4DKeZ3a-Ohr4NPyRA4a6pmRY4P_MARNWmHowssZw1m4lWpX05DEAYsIZpBgzMl7KEBgE9bIQSU1wjBsCks1C5MnwPKx0hY7s5P2iIZ_vVwMs0WYo311BLj-8zHdiYZxdN4AGEbCitby6rSIWKi9DEiiwopDR_UW2JyGZ7_A9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۰شب ایستادگی گناباد پای انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464608" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=Gd246c_7L3TTAtkGATYv5qT4hH7kv3394jBKsrE8auUMpoS_ezZQzSg2B5WdJPdo4GPvyOiIn57pzVYMmqNphNd8meE7i6Nxd8OLqR8fxASQUGbtmyHI63DB2v-LOoQEM0Oi6ydW1BjgiODE9gf8Mcu4ShcWkslI5WuMLAux4d6iUWIzRhrih8SHJ1QxwIEwl9Wuc4pFeDwLc5Oby6ma0dNmAoFLwqhxRbsdm3dSnUJGNS9jkKQOaovVvdVHVZw09Gel4Onv3MP8nBMYGjLHKwQHwazoNVjcOVADtilY0sZli5tgC-KSHMTOpMUTuG3oKMuz6X1GL6BK3ro6S9sCPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=Gd246c_7L3TTAtkGATYv5qT4hH7kv3394jBKsrE8auUMpoS_ezZQzSg2B5WdJPdo4GPvyOiIn57pzVYMmqNphNd8meE7i6Nxd8OLqR8fxASQUGbtmyHI63DB2v-LOoQEM0Oi6ydW1BjgiODE9gf8Mcu4ShcWkslI5WuMLAux4d6iUWIzRhrih8SHJ1QxwIEwl9Wuc4pFeDwLc5Oby6ma0dNmAoFLwqhxRbsdm3dSnUJGNS9jkKQOaovVvdVHVZw09Gel4Onv3MP8nBMYGjLHKwQHwazoNVjcOVADtilY0sZli5tgC-KSHMTOpMUTuG3oKMuz6X1GL6BK3ro6S9sCPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم
🔹
چطور باور کنیم که آمریکا که رهبر و بچه‌های مدارس ما را شهید کرده حرف‌هایش را اجرا می‌کند؟ @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464607" target="_blank">📅 22:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325d9f4c33.mp4?token=SwAn9MQJ0CIDTcKta8lJOvqLy0uu8Hfjjy1PYJoK-mXDJrUhNOqumrZrmN4yc81AQmUxxuBGclG1_3Ilr4Yewe1AFXozD8NS5dk6sWz5fk_sqMaDp96rlWqc0VPLH7PFtPEGzM5pRcEROgfO3IsInaxztAxTBEGZfzQgjbU2wJLTIGsthHSFGV2ox7H2njHZ6ovgx0orWNMeYZA5Dywb0fohJ-c5IQ3s1hPxzvENWfR0jZasOD1INVMWHBzNzDmMAw8s4uFsr2lBN7f6BoW9E02ISQB7Vo4Gcim_Nu8XxJoKY0zlFZIGr8tZUQqqW_hS3wTa-7I_O2_V4tyUmli16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325d9f4c33.mp4?token=SwAn9MQJ0CIDTcKta8lJOvqLy0uu8Hfjjy1PYJoK-mXDJrUhNOqumrZrmN4yc81AQmUxxuBGclG1_3Ilr4Yewe1AFXozD8NS5dk6sWz5fk_sqMaDp96rlWqc0VPLH7PFtPEGzM5pRcEROgfO3IsInaxztAxTBEGZfzQgjbU2wJLTIGsthHSFGV2ox7H2njHZ6ovgx0orWNMeYZA5Dywb0fohJ-c5IQ3s1hPxzvENWfR0jZasOD1INVMWHBzNzDmMAw8s4uFsr2lBN7f6BoW9E02ISQB7Vo4Gcim_Nu8XxJoKY0zlFZIGr8tZUQqqW_hS3wTa-7I_O2_V4tyUmli16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم
🔹
چطور باور کنیم که آمریکا که رهبر و بچه‌های مدارس ما را شهید کرده حرف‌هایش را اجرا می‌کند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464605" target="_blank">📅 22:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am5KDUh17EqnfZPgdy2IZwSmrUFGK24OZ7wtHeZCmsoKRMNmN_F9PvqYog4IUH-otCIyXjJhoy7QacK3t4YN5sGDazdWmyv_uwm_7KTe8EgFSbCen5jyncoYu-5njna83-zddyopqkG6Pi7Tofn0oCgJEJX43O4WHuN4bWw_r7vEr6OD_ldyF9xSm8_GxZEujlfWTweEmE0sTd_x-MIkac-AB71hAigQ0D0TWYtWalgw0zxmS6CnrjZyBSYO-EV1UkLSGjcVDZoe4Bbcf4SAjojgdcTlWOnKO7b8IbjyvGktnTcN9-SAdNrq4qsbcknneuIaulZlEkNxZvLogYuCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا اصلاح‌طلبان جنگ سوم را هم به ایران تحمیل می‌کنند؟
🔹
در شرایطی که ایران ۲ بار در میانهٔ مذاکره هدف حمله قرار گرفته، دوباره همان نسخهٔ قدیمی روی میز آمده است: «صلح، مذاکره و تفاهم»؛ اصلاح‌طلبان مخالفان خود را به جنگ‌طلبی متهم می‌کنند و خود را در جایگاه مدافعان…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464604" target="_blank">📅 21:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25a6c32c.mp4?token=sH1_FVmTFTxQNNSJt8CG0LOjAxxMjN2FjRy1_hFwshaGMrVv-xJVsZHtqUCG3PBCE7uQFkNlTUup61AXCCLDBPgfRS1nmvkvoTHZJ3tq9XssJS6T7oizY1Dfm0laph8KvQBB1raX8xg1wBTSw4GbdbiAV3skuoP2Pj77vYzrJdEV37-lHb3jgoz2azLEwEknaUF2664k3esfdi2ISbov9QHfjsdoOzrUDPgfI1O9BYFsA54_Nm_AK1UU6aiWU5aZdatsVR1ZgWZfZ-K4e6LYnoIdmcECLhlyMlrsFTtj_KDZ4DpQNGhLihHq1nUrHMo26zfx1OQP2DuNwvcIeQiAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25a6c32c.mp4?token=sH1_FVmTFTxQNNSJt8CG0LOjAxxMjN2FjRy1_hFwshaGMrVv-xJVsZHtqUCG3PBCE7uQFkNlTUup61AXCCLDBPgfRS1nmvkvoTHZJ3tq9XssJS6T7oizY1Dfm0laph8KvQBB1raX8xg1wBTSw4GbdbiAV3skuoP2Pj77vYzrJdEV37-lHb3jgoz2azLEwEknaUF2664k3esfdi2ISbov9QHfjsdoOzrUDPgfI1O9BYFsA54_Nm_AK1UU6aiWU5aZdatsVR1ZgWZfZ-K4e6LYnoIdmcECLhlyMlrsFTtj_KDZ4DpQNGhLihHq1nUrHMo26zfx1OQP2DuNwvcIeQiAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز سرباز در منزل یک سرباز شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464603" target="_blank">📅 21:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d6a51cd6c.mp4?token=iOAeM_QwsFYJT_9dWzN5n9gu50aq9-77lU18aa3XN32KMAbbHHmwo1H7R1G3Tl9sxAQbDaLMht_MAds6XTfOQlj5KzuQVxom2yRGRWHSnTplkAYNANqKptGlbL5AcwxWgmMemYOYzweLP3kXnzT__UiJaMV86eizUAmKuPkoLOiZ6cvi7WeD_VLf7OwIOYzhBOhwF_Ks3_T7_RweRtpkPD7Ld1FlOgin8PhB8Rya9BKq8dM3ml-y2ffMJshQhlpHJwya2maZEi-9fJ1jPyKbXm5Z_bRydfAVLG77OlJpo6lP1-i81ds3mETjBWnHnXZzShvBJK2zVYq5IAus3cKd0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d6a51cd6c.mp4?token=iOAeM_QwsFYJT_9dWzN5n9gu50aq9-77lU18aa3XN32KMAbbHHmwo1H7R1G3Tl9sxAQbDaLMht_MAds6XTfOQlj5KzuQVxom2yRGRWHSnTplkAYNANqKptGlbL5AcwxWgmMemYOYzweLP3kXnzT__UiJaMV86eizUAmKuPkoLOiZ6cvi7WeD_VLf7OwIOYzhBOhwF_Ks3_T7_RweRtpkPD7Ld1FlOgin8PhB8Rya9BKq8dM3ml-y2ffMJshQhlpHJwya2maZEi-9fJ1jPyKbXm5Z_bRydfAVLG77OlJpo6lP1-i81ds3mETjBWnHnXZzShvBJK2zVYq5IAus3cKd0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اعلام جرم دادستانی تهران علیه عوامل متخلف یک تئاتر
🔹
درپی بروز رفتار خلاف عرف و شئون در یک تئاتر، دادستانی تهران علیه عوامل آن اعلام جرم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464602" target="_blank">📅 21:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1H4hYPPcaiGEuHLuOnb7o6Guh0ttwDOE69okSuIoLOna_S1C_RhpArlpW3I5QYrZbt_FHuMrnHhtJlgvGh5YNllMbgvHj8hNZ2etjLdMSE4eP2G_deTM-p4jfCE3gc8kvt1CJK0pvXjZ1NP1b-52DzGukiGbyrk0BVSF64ef6L_SLwdc4h_ujeo8sIRSBVt2prrdwbmFO6xZDDgBzq_s8oAk8BCYw94jXc7zeYxCbqsALeXX0Qt7fTjPExe72FGU-R-ngOsswlFnDTYFbfquMhXk8kTwp1iJb8-RcAtVSHThov8CdXy8XF9hfWUTpX5kr2bWN0-q2P2KxBomBguKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید ارتشی پس‌از ۴۰ سال تفحص شد
🔹
پیکر شهید علی‌اکبر گندمی پس از ۴۰  سال‌ دوری از وطن، کشف و شناسایی شد.
🔹
شهید گندمی در اسفند سال ۱۳۶۱ و درحالی که ۲۴ سال سن داشت در عملیات کربلای۴  در سومار کرمانشاه به شهادت رسید.
🔹
مراسم وداع با پیکر این شهید فردا در معراج شهدای تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464601" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_J2gB4-MdFOkhA-GOBi_j0PpR7IFHWHu4Td0Bzdii9JdmIxdPF5sTYwl1t9BdJsNg7ts-KcE8q78moYhUDqIF8EIWnYj4D_qeAGQtaJA8BSrW_TUSR4507bm3pqn-pS6XakeafMqgT1d-xOFoRKTzxsyX7AZ9I2qZktawPlY4nyoF7ZZDCcEUTdolaRjOubfotTqzwCtD6WCcL-p7Ik_-Hz5kVqck8BaRRYpPNOjTTOhdQNHcwDh6w6oBYisJCgy39W-vBn8veXwTiJPT9V_fqtC8RBZGsaSJWOxjfSbwvpgb5pOB0BPwgCDl-ZfLdrib22T9H0rR2oZF4kUoejuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: چگونه می‌توان از خلع سلاح هسته‌ای سخن گفت اما زرادخانۀ هسته‌ای اسرائیل  را نادیده گرفت؟
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464600" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروابط عمومی چادرملو</strong></div>
<div class="tg-text">توسعه جبهه‌های جدید استخراج و اکتشاف در چادرملو
🔹
عملیات آماده‌سازی جبهه‌های جدید استخراج، باطله‌برداری و اکتشاف در محدوده‌های معدنی چادرملو در حال انجام است؛ اقداماتی که با هدف توسعه ذخایر و تأمین مواد اولیه مورد نیاز زنجیره تولید دنبال می‌شود.
🔹
در این برنامه، همزمان با ادامه فعالیت در معادن فعال، شناسایی و ارزیابی محدوده‌های جدید نیز در دستور کار قرار گرفته است.
🔹
توسعه فعالیت‌های اکتشافی و آماده‌سازی جبهه‌های جدید استخراج، بخشی از برنامه چادرملو برای افزایش دسترسی به ذخایر معدنی و استمرار تأمین خوراک واحدهای تولیدی است.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/464599" target="_blank">📅 21:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3321f40cb8.mp4?token=fvwr4OKrYOAxRs7sgDrWAO3icyKja3hFa5dP0renKf5052zZnO6qZp0-wLHxoti0j_a2ARQYk4Y6YEacgvILGHOJaIodjYy1h2YenvX2Y3pI2sSdCvIVSFNAYzeSnlGufODMnS0XMCycIArVJWiOdTfRScWbBj92Dhh4ejecxfvaLDyPK8jejyuAZoRO-B3CHvAWTC6Khy5PsYmg3zZepXmWeJo1DxpmCH2cSmeaJgOOeZQkxdh-ga-RJTwd8viVrOw2TAGF4pUZTh8xVrZgWllKtJK35oL9tHvviKdIm7kO3kL8XHFSKWEkks29wAhqOtR3UtzdZ553BUIept6BQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3321f40cb8.mp4?token=fvwr4OKrYOAxRs7sgDrWAO3icyKja3hFa5dP0renKf5052zZnO6qZp0-wLHxoti0j_a2ARQYk4Y6YEacgvILGHOJaIodjYy1h2YenvX2Y3pI2sSdCvIVSFNAYzeSnlGufODMnS0XMCycIArVJWiOdTfRScWbBj92Dhh4ejecxfvaLDyPK8jejyuAZoRO-B3CHvAWTC6Khy5PsYmg3zZepXmWeJo1DxpmCH2cSmeaJgOOeZQkxdh-ga-RJTwd8viVrOw2TAGF4pUZTh8xVrZgWllKtJK35oL9tHvviKdIm7kO3kL8XHFSKWEkks29wAhqOtR3UtzdZ553BUIept6BQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرباز یعنی کسی که پای عهدش با این خاک ایستاده؛ با هر لباسی و در هر شغلی.
🇮🇷
⚙️
روز سرباز گرامی باد
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bank</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/464598" target="_blank">📅 21:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/464597" target="_blank">📅 21:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861b5f45bb.mp4?token=vtTh1FBWcGLYLNmOxqd52T68xDJQWPdwk4wpQiHjX8LT6XP6W03I2vFd0AaLQauL_4qTWN1yjDfvG9q_9endHxmyyxWmiDEjKPMj_oHGccRzOprEYnuqbxO0zv-JmYHR6EOAuLEFwt_b8-kaSdlrpD9x6rdlIx3_SF53APsYVEcqPjdzcjydS7Y0AubN6Z_223b0cLr7ix2bz3PaSFQYdmUdWUcTQNOeOR0gbWI0y_6BOkWCb2gcm12BDR8MsyRAPK9uMTU7hjKY9t9uLNcv3x8UBtS6F7s55-q-qM2cA7PETN81J5WatKZAauihDOJmMqdtwZU18FPenDCffHZ_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861b5f45bb.mp4?token=vtTh1FBWcGLYLNmOxqd52T68xDJQWPdwk4wpQiHjX8LT6XP6W03I2vFd0AaLQauL_4qTWN1yjDfvG9q_9endHxmyyxWmiDEjKPMj_oHGccRzOprEYnuqbxO0zv-JmYHR6EOAuLEFwt_b8-kaSdlrpD9x6rdlIx3_SF53APsYVEcqPjdzcjydS7Y0AubN6Z_223b0cLr7ix2bz3PaSFQYdmUdWUcTQNOeOR0gbWI0y_6BOkWCb2gcm12BDR8MsyRAPK9uMTU7hjKY9t9uLNcv3x8UBtS6F7s55-q-qM2cA7PETN81J5WatKZAauihDOJmMqdtwZU18FPenDCffHZ_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم خطاب به سایپا: اول خودروهای معوق را تحویل دهید بعد ثبت نام کنید
🔹
در حالی که سایپا طرح فروش بدون قرعه‌کشی کوئیک و سهند را برای مالکان خودروهای فرسوده اعلام کرده، تأخیر در تحویل برخی خودروهای ثبت‌نامی قبلی سایپا همچنان محل گلایه متقاضیان است.
🔹
برخی مشتریان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464596" target="_blank">📅 21:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b6126dca.mp4?token=BJB7o_1--Tptgdh_POUDUdDV0Kc3oM_meXjrHcxXdLP0MpcUuk2YZ4Zd6DARJ2y2XIncsjGnBXZOaOylXiKMVeSrKS8UA8YToQ2FePvMUKQXVG_nCCGL3h1tXbHSq9PbrhmgvBKMBG1Do-9snjQPrG5fbhHiQRiCeZ8wiPjFkVZRIgh1ksGhc7cHtfaIvvwAWCDIbi1QHodk9JRbhPS1BDix316ufiMpVT2wdj6RAXW4IC13ANd-hGRf10gx2oVG4F3i2MM_tAIx5fsM54B0CXHD21L3W1Fn55tGdx6KhsufERGj_jNgHnQkk-K2tyvcEaKbypLLaic56WKNPAIG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b6126dca.mp4?token=BJB7o_1--Tptgdh_POUDUdDV0Kc3oM_meXjrHcxXdLP0MpcUuk2YZ4Zd6DARJ2y2XIncsjGnBXZOaOylXiKMVeSrKS8UA8YToQ2FePvMUKQXVG_nCCGL3h1tXbHSq9PbrhmgvBKMBG1Do-9snjQPrG5fbhHiQRiCeZ8wiPjFkVZRIgh1ksGhc7cHtfaIvvwAWCDIbi1QHodk9JRbhPS1BDix316ufiMpVT2wdj6RAXW4IC13ANd-hGRf10gx2oVG4F3i2MM_tAIx5fsM54B0CXHD21L3W1Fn55tGdx6KhsufERGj_jNgHnQkk-K2tyvcEaKbypLLaic56WKNPAIG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشریۀ اکونومیست: آمریکا از خاورمیانه خارج می‌شود و ایران ابرقدرت مطلق منطقه خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464595" target="_blank">📅 21:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9505bf3674.mp4?token=Hnza6JulVz6aCUa3D_VuXzdFL3P8IE8R9-N5oRHAgYGVAM45eKBIUYEfwZqMCR0EAmVM4PrPCE1SwBYPnUu32RX_1G_pWTUsN3bvQKgvetaN8WRa6xG6wEICRNVfJz2Pi1RG85k-JGMxhXRkc8ZcCyGsVWmP4wgC1NPlL5mvqA6b_HMCY5F6Gac0P0kRMlPauC8fNlTV_3jFmEoYIkzwGV2QkqIUN8UZDv_RVRhITZ5ObIOnUMS7-_ZfMOs37g_UEYWIjAUctDZqYh0cFfn5vPE9fPD77YSmK96FYG8D5prVpg8B9pWpXkuecrJCnNoLUJC-oudM_UYu50hR0vU3I4POeRHzNrs_yvAubaEHt4fTPrwOPrgC5eI8EkQDOWgPa4TyC2SQtG9jb3AJikDtnaZ5Tea7mk7HFjZNiZaEueEMdA6CI15-zdz8BbquMOuqcCHTbnyco2WFls_DGEuSnY0qPABg-GzsN9o2o6hKCkAYaRx0J2naMDqOL6QQnF5jjsB7zIq2GDTrpMR3oHfa3FsrHzsEefG3zwhzD6mL_R2urJcRJmbJ7ZQBQw5DQFBX6g8hs9PLKeW2NDwsWSCuh53ObJ-_1TzfwB1nCBOdRp-QOsXZ1EfYg_huN1VM9_l9O46gFlpanKBFLp6soK1N4Y12baqk7IQjE3My0o_VhyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9505bf3674.mp4?token=Hnza6JulVz6aCUa3D_VuXzdFL3P8IE8R9-N5oRHAgYGVAM45eKBIUYEfwZqMCR0EAmVM4PrPCE1SwBYPnUu32RX_1G_pWTUsN3bvQKgvetaN8WRa6xG6wEICRNVfJz2Pi1RG85k-JGMxhXRkc8ZcCyGsVWmP4wgC1NPlL5mvqA6b_HMCY5F6Gac0P0kRMlPauC8fNlTV_3jFmEoYIkzwGV2QkqIUN8UZDv_RVRhITZ5ObIOnUMS7-_ZfMOs37g_UEYWIjAUctDZqYh0cFfn5vPE9fPD77YSmK96FYG8D5prVpg8B9pWpXkuecrJCnNoLUJC-oudM_UYu50hR0vU3I4POeRHzNrs_yvAubaEHt4fTPrwOPrgC5eI8EkQDOWgPa4TyC2SQtG9jb3AJikDtnaZ5Tea7mk7HFjZNiZaEueEMdA6CI15-zdz8BbquMOuqcCHTbnyco2WFls_DGEuSnY0qPABg-GzsN9o2o6hKCkAYaRx0J2naMDqOL6QQnF5jjsB7zIq2GDTrpMR3oHfa3FsrHzsEefG3zwhzD6mL_R2urJcRJmbJ7ZQBQw5DQFBX6g8hs9PLKeW2NDwsWSCuh53ObJ-_1TzfwB1nCBOdRp-QOsXZ1EfYg_huN1VM9_l9O46gFlpanKBFLp6soK1N4Y12baqk7IQjE3My0o_VhyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرباز ایران کیست؟
🔹
مردم در تجمعات مردمی پاسخ می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464594" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
منابع لبنانی از حملۀ توپخانه‌ای رژیم اشغالگر صهیونیستی به نقاطی در زوطر شرقی، تمشیط و بیت‌یاحون در جنوب لبنان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464593" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGKPkxRqqjGU3iMHKjsAHOy-scg0ElUR4e3K623sG32i3saqO7fQgEyzjL64qJrDw1fAX62JLBW1l5UJ-6mBy57QGTUW36V_DGFlJQHHd827GJOTsM6BXMrst7Z5JNCqmjOsPKgh8igIE690uv_63SWd_7jV75xMfh63Vk2fAb5rlzeag-tRvL_YhtvPPgSpV22pFscLXLqcXVDkIFtlQJ6PkofKitAnIqCLFzU2tJMkx5pV83-1UY27x9jp1Uu4gU61zIbK6smyJraOBLClgbeQZLQ33muh3fn558qXGwP2DxAZ7CnJKY1Xx6bRBfffILIvY9e9AsEGsOhU-FiqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Voql43_1FBmwjv2SZDvQznAD-m-2GjHq33aIU7RcQG6PT31U4X40hdUKbf7Z5BJNIBcL4Jm8l1oEwakJot_gX91fgpx82JZRkjOADW787cMdvJvDMHNSKyuZ4mD056BReauSnqfoxjKEyNOuO_KqkKlwJrQNA3d0kbI1HQz4vuF5GmRlVZyYqv5KCH7pPtuB8YI5Pnh80EGeAFMxJcl0FFM_rr7T5X4bVrAyPt-03bm22rL2mQAaFpdAX0lxUOKHO1zAu84dUm_9URGEulSOckEEHZHUKiWcjaUI32obe2QNSMnytxNt9uf3pL31P_tdbZV0z-Usjr3Rx-dRiol2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6D6QO9QgjavbBJhKwOgVfOrIC4IjnKv8LV85KBInAH11rLIMQTNAKYYI1G_ibpdc-0CC6_-WLJWnTBmq59NqOQMpoBzQAo744pcOVzlfTBPALNy8C0ySRgzzDyBKKDnwfmvs658WhigCbFlIPJZx2AAguJqJ0eT_fPCVAUW5qXq4aLcUdKnzQGmEKuuCU__3fHgQDxUg52CzXW0Wr7HCgSmzIHdRgVbGfuczAYxgnCEVuQGVAwYngePInRvgyXEOUPwOhx1pt1JXND6IFt9rrn93ToBWTgdmg_uT_O9TEsgzbUX5mvNH4BoQRbmO7A9yqGaAek_xksNoujrFzBJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmS0RFj6pltQQ18_H1B1mtAT-tyBmSHRy-2g0uZLNrXNvCRCfHHY0rNUDuITJN_p8tdk0bqfnf31YDWu_3PzutncnwStbQlt7k7d4VAm2P4EYm07Zr6fvB9XP2ZAbvCIkmgPHSHHGA5pbL4HTaB9v1Cr0uZHdI7oGN4nz600HflLjZU2juqWUrMg4D3cbZ1Svtfku2yY5wKCIUnInXPVbUGAHvEIrOgTIqyyPp8Uex6bRzh0JlX7uhH_RQn8VUN5P7hsaWBE01yf2aLDWGeYABMZJYnNA-c4itLH-EPZgWuhqxRpGw15tPnGA2GAC9M5J35_wIx9xixYElh-LpgjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsSukDxJXPfHBq01fkJY50v_ZRM7Udxrnl3pKbRAkc6TiLxNZQPA3ND6txVpHbtRljx-a4Mb69TKD8RbqCz9ijbbXQ-sOUc64Wygc4UFg9tIi8Ox7GWgLzs1bMYp3PEn04vu1grkq1I3Ifv54-Xmal_pD-WeSs8FUT__aqQMAm3QojmR7bHKaQAwi-iOEgueJKzKvrBziI-u-LrW8pJSysEWqyZdfA06J_QR0hqP_QlUkzfId5n3cB4hnO9IzkqGHu_xIDHHLobV4wiuyfBnphhGdxxXdxnC02WtMF2HuSpp9TV0q-tchR4TVPKzuYv7rfkr-Xpu8zN59hKzImQZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0gT-yOLoZEGLKhNaq4Mu9CuQS4uK8JaguNyNvfp5zpxd4kgVktm5-G7ZeiUMyfNGM60vlVqULDNkeYDAE5BNzZV4fQ2m-jcrwxuMn7sEFJDFCKj4gu7VBZGLNF_4Z0A-5gop5EbGnlJNh5EYchivbtzR_kSBtwRfjM4sOirH-RM0C2mI4DXdE9dIAMtpxisajwnyTsIF1Zg4Z3ctDFIX24-HI53F4QcktuKeYxV7e9WXrsRL6cYnafrMs9qeaEGs8RXojZSovlP8wdp7wxlzaHlg7qdOmUZwhR68MvGkvG2qUM48qiOnsQyZDLQRSAoPeHYYfPT8KDBqp_H9TqliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puFFiKeuZXi9ZPTn1DQUa40vCOGHKpTLifwa35S1UMNSwiQFfPyusVVMTpEZtBtgtZDdWNC-bxz7xJlRkbQZ7zR1s31Y0fSwDoHzGvZhLwEIIc-hTaNeAVV6Uu62B4WU9rhPuj5Dwjufylsk73LvRN337DXNaFMCbzMeoJswXR8kpIyXI3o4ibLYJeZt5M6_9XSSweAMKo6F9dBIMsZ7KqasUZn3XQiGfHsennRLlVxllR7XeYAgFk3D7j0UHZRH6vzc4iqW9B88rxacKq6MkDDe64hxMNNE8aZOuokAjP6gaJWMjbaemSnHC3YljLb6YNMYRBfzx0kWK7a2m1h5Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یک قرن روشنایی؛ روایت کبریتی که از تبریز برخاست
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464586" target="_blank">📅 20:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dc7e782f.mp4?token=BtqMGnkAEH_dHtOVOPVcTRhD2W3TTtFdZSaui24kFaFSFB8PeUBuLJg4QaFbHtXw51sl4GdayBSy2X2wxyRpXshZqJNxii8_zt5As4yHTGwdVq2k4sTqoy63-dLYDI0es_hkKZK8S9Hsb0kv8YFXBhUiyYvp4EFkIv9Zct2EN35bpVKaQV-Gpb7iFSY7jX3vSSQb3yRAZw1I8McpOTKzCHUnIx8mz8nl8KuXCwzlGqTqnusPkNhHePvtxQTXClYOTz-OIL4_Gegs5bl6hH5icqZ2dtHOB85zu16I1FoA_9cR8uI3WLvzvlCPAejAxiaEeeoCU6Cwnkhd7FUMXNP5Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dc7e782f.mp4?token=BtqMGnkAEH_dHtOVOPVcTRhD2W3TTtFdZSaui24kFaFSFB8PeUBuLJg4QaFbHtXw51sl4GdayBSy2X2wxyRpXshZqJNxii8_zt5As4yHTGwdVq2k4sTqoy63-dLYDI0es_hkKZK8S9Hsb0kv8YFXBhUiyYvp4EFkIv9Zct2EN35bpVKaQV-Gpb7iFSY7jX3vSSQb3yRAZw1I8McpOTKzCHUnIx8mz8nl8KuXCwzlGqTqnusPkNhHePvtxQTXClYOTz-OIL4_Gegs5bl6hH5icqZ2dtHOB85zu16I1FoA_9cR8uI3WLvzvlCPAejAxiaEeeoCU6Cwnkhd7FUMXNP5Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیئت دیپلماتیک کوبا حین سخنرانی ترامپ جلسۀ مجمع عمومی سازمان ملل را به‌نشانۀ اعتراض ترک کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464585" target="_blank">📅 20:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2hRABXFYRETCZyoUGcL0fEOzLqKNx5yM8WQVNL0-l44bFJH23SAvcsFyfRslGJ5hH4ut3t9pb6Xaz5E1YLfSvQ3eqBPMx1etn13Q9tRV-vzhPozz4-YBK5rslxktd8fqHAGVdU30BqG9pN-4PxNIeThiXNBfqciJfgm31ynJ4J6uUGWWLfA3RJu_V_OpyHjVZ2ClYUJvXOSJ6ci4UNrceyoJElCeQ1lRsCDmCbArQHT93gTogxbR9ybn9Fz6TPDU65Pfw_lpP8tJDRiagHGTtBFOv-8G-NTspAu_Oluv_GpgVQkUC3rLWu33Ikk0WOlufJy6JzjNVPN_A4cp1U5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واردات خودروهای لوکس در شرایط جنگی؛ بر اساس کدام قانون صورت می‌گیرد؟  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464584" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e42be5851.mp4?token=R9s__0TwDxMx396XFQAZgMxVNmhu6ev2P881csMvnS0nFYF6Ol4SMxEOJM_82Um9tIJBhlsLpv5nG_Z7Wc9RzkG37WNUIg-iMV8pWf-o5KoL1imTAxIx8F4f2BoPjlZDj6-twsyT91C2fLPlJAZzlXsj7vLhiKwCbApj0pt6Fx0c-_R9JGmrmO6ZU_lGnVocmsQfS67t_ZIWM_HHFr-GbhqBssZy5VYSG6PgdbqyDOdx9K5VVfvvSz9I8gWVaMExuLtz8alGNwbiPWD5Q3Na0_RKW6ViISASXfe8llPKsEuCd6FObyKgN5xlwlcNc6zIq4Ijhawik-hYHNdqWRQfQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e42be5851.mp4?token=R9s__0TwDxMx396XFQAZgMxVNmhu6ev2P881csMvnS0nFYF6Ol4SMxEOJM_82Um9tIJBhlsLpv5nG_Z7Wc9RzkG37WNUIg-iMV8pWf-o5KoL1imTAxIx8F4f2BoPjlZDj6-twsyT91C2fLPlJAZzlXsj7vLhiKwCbApj0pt6Fx0c-_R9JGmrmO6ZU_lGnVocmsQfS67t_ZIWM_HHFr-GbhqBssZy5VYSG6PgdbqyDOdx9K5VVfvvSz9I8gWVaMExuLtz8alGNwbiPWD5Q3Na0_RKW6ViISASXfe8llPKsEuCd6FObyKgN5xlwlcNc6zIq4Ijhawik-hYHNdqWRQfQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران شکست نخواهد خورد
🎙
نماهنگ جدید محمود کریمی به زبان انگلیسی.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464583" target="_blank">📅 20:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756a67dce4.mp4?token=C7sNtqMxMOppnHSj41K7KccDW3G93VewtqSNC1xrlu-6MdDfIouXZPb8zEKdmHHDABS0ONNrNLIa4qwvuaM-kaTqCIePEE932z7lArgblBoUw2TmblMKwftJA3IL4XNA2aiF-sHkT1pH4eBxSnm-T8dDldmJpLlIW_Duo9PNEMCrorJkgoH53oy6NUluF0WLcgen7r8LF4wAjS0-ymH3qDiPLoV5ZGbiEpaXlDXJ1MKIzR6eLwzuSLetP7eHu9WMAvVFtLspJBdrKm6zO4df8dIxHKXcY8A-7rwIq3p-IxeCLZ5OkFnrb8nFP0FRPG6JZZ25_PKf_d7AIpA7egA7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756a67dce4.mp4?token=C7sNtqMxMOppnHSj41K7KccDW3G93VewtqSNC1xrlu-6MdDfIouXZPb8zEKdmHHDABS0ONNrNLIa4qwvuaM-kaTqCIePEE932z7lArgblBoUw2TmblMKwftJA3IL4XNA2aiF-sHkT1pH4eBxSnm-T8dDldmJpLlIW_Duo9PNEMCrorJkgoH53oy6NUluF0WLcgen7r8LF4wAjS0-ymH3qDiPLoV5ZGbiEpaXlDXJ1MKIzR6eLwzuSLetP7eHu9WMAvVFtLspJBdrKm6zO4df8dIxHKXcY8A-7rwIq3p-IxeCLZ5OkFnrb8nFP0FRPG6JZZ25_PKf_d7AIpA7egA7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بازدید سخنگوی ارتش از خبرگزاری فارس  عکس: صادق نیک گستر @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464582" target="_blank">📅 20:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwQsxOX4csa9QM3GrVlK5F5Bvc2WgIjExDjtHySZ1icc2tO4CHMv7pldyhBiMzBZ-ZrCortyOjTpooq6ACUMX3j26JwpZhQp4ToiUP_1eTkzd3fdVjcdzetgD2labOerQ0HUqu-PYq2MkJ-wVFQZrW_KKzDzRwCEHMIWsKK-asRZsh2kHvBKS-5FZCTFAn0wBzwUMsu-tyiKWb1JC90EfoHT5IDHFSE0b32I6-uBz7eb2bRK5GGWZvH6lr7kh59aGzvYROKpM43A5-d1Za5p3hQjuracT8cBadWCWSaEnJ6-_ZbuA7X3K5ViNZLQnI6NtKld1QJl3eYKAEpUh_a2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاوروف: روسیه بر آزادی فوری مادورو و همسرش و تکرارنشدن چنین حوادثی در آینده تأکید دارد
🔹
آمریکا اوایل امسال، با نقض تمام قوانین و هنجارهای اخلاقی با حمله به ونزوئلا مادورو و همسرش را دستگیر و بدون محاکمه آنها را زندانی کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464580" target="_blank">📅 20:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmr8SY2-kONIyDAZiSuawBPOA19R1mgh4WF8NHh_rNRw90pfMF-9OqnGVboqpqrKHwAqU9Kf2cMYC2Jg-fx9QtWcyyXkUOereBLToCPj1q6u5fWndadKvfdUZqCADyFg4dBNGWnnWkXInYKSYMUyy0ysckbzcMIBwMhfEKqGaDc2zIIt5Nd2xp03IgMCWrxsr8q5PYg4cHunC2mF7mRNqOpUdEWSmwRgymFcvs4HFbVm5ZSegh7ZMRcfgED3xsF_EgBFrIZ-krO70S_BRggbqLWij9ngX7W0JQIXnahmdmOh770JjtlMZvWVnu5y7i8-UiI5mMUy7aUAjxYiaqYg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  لاوروف: روسیه معتقد است زمان آن رسیده که به دولت فلسطین رسمیت داده شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464579" target="_blank">📅 20:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464578">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر خارجۀ روسیه در سازمان ملل: روسیه ترور رهبر ایران، خانوادۀ او و مقامات ایران را غیرقابل‌قبول می‌داند.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464578" target="_blank">📅 19:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464577">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogJw8kCuS-82ibSyH0C886goh464JSsdKY1J-3JndmzjePd3fEooxlUHBSI-X4KY74vdHokzOEOwJHLrK0QjMH5osxs-bDtadSQgdJdKI1qnejVoYIHJmpDQaWVVBzJxqldzl9xxQP4QN3GvmIW2zhscIPqRsgMH5S44nNtjqrLvnPcXSfmsr3Gz8TFjqW12BA8Dm71Z7fKilNXMxJ0usDfnANMZFN3ix55u3B7DAjbeWcu2ghkX8PCL3PYmRUaIBiXmy5SjG608b3PIEZCRpbIdUg3D3Ii_SllY2H_M9V4mGaiotxU2bNkCdS8FyaAUL2Z4BrQLW4AcRkOKhUDu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه در سازمان ملل: روسیه ترور رهبر ایران، خانوادۀ او و مقامات ایران را غیرقابل‌قبول می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464577" target="_blank">📅 19:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464576">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuIWG3wtpjw3O3nK9Wq5aOyIt79v9h605i1hLpQimqnDHiIy8dAm3lbO5fdbwop1akTx9rtRea_yC8JGQK1z7MYSDEbCyO0BBdy_gCCEM4yxxe4Sf0CnY8cmhjrih_acRsDlLF6mcDsNyTW404KjV8JnKG26eU-lUC7_KT9ov_US5c-DnKaWu0yYjuYsqC-mHzL8AOkw60umeekATt2hfiIgR_a5xoqLb-GUOO-I43xaRryWFcHD41qlwshSZz7V6IKGpNI6Mm1Y7nZ7ooc5rzcr1W_OEC1ALCBFYddmJVSHqS3PfAXfKYAhfDbn4G_gRyTnc3D7lbT0laM68ORj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری عاملان شهادت مأمور ناجا در کمتر از ۲۴ ساعت
🔹
دادستان زنجان: عاملان شهادت سرهنگ دوم مجید بهرامی در کمتر از ۲۴ ساعت دستگیر و با قرار تأمین راهی زندان شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464576" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464575">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۳ فوتی در حادثۀ واژگونی مینی‌بوس در بزرگراه کردستان تهران
🔹
آتش‌نشانی تهران: برخورد یک دستگاه مینی‌بوس با چند دستگاه خودرو منجر به واژگونی مینی بوس در بزرگراه کردستان شد؛ در این حادثه ۳ نفر جان خود را از دست دادند و ۱۷ نفر مصدوم شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464575" target="_blank">📅 19:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قطعی برق بی‌اعتنا به وعده‌های وزیر نیرو
🔹
هوا تا ۱۰ درجه خنک شده، مصرف برق پایین آمده و وزیر نیرو می‌گوید، ناترازی ۲۰ هزار مگاواتی پایان یافته اما برق طبق اطلاع قبلی در خانه‌های مردم تا ۲ ساعت قطع می‌شود.
🔹
اما این فقط برق خانه‌ها نیست که قطع می‌شود، خالقی،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464574" target="_blank">📅 19:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdK0N_lX1N6ATUu9Rr35B8uB5ArEWaCNl2IW1YxUvcmR2qq9yBRidkkFu6CCJ0OA8MZHIWQXEvZOkGlX_NMb2s_-ffbA4vGIF98QwAGZIhCl5WYkApNSyo87lYb9iSRMufTwUGx2pD3YSyWySm8gaxXyWaZeYnYVyTsMPvyef5EztcOnws9jBbcokFcFl-XdmLAjuFn_Um-nal2YCjNZIt-XUzkGNBksxftQleSp_apdNNuJXgkQbncn3Zlhu5681QeNiydW7I6Y9jyokvDDVlC1fLhI1DX8fsX0gwRXcE0HVPSmi4qbCc4ffN-R_y8VxsSlZhJ1bmAaP5X6rQvjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبی
:
دبیر سرش به کار خودش باشد
نایب رئیس اول فدراسیون فوتبال در واکنش به صحبت‌ دبیر:
🎙
موضوعاتی را که علیرضا دبیر مطرح کردند، باعث تعجب ما شد؛ به این دلیل که تکلیف فوتبال سال‌هاست مشخص شده و خیلی جلوتر از کشتی، تکلیف فوتبال تعیین شده است.
🎙
فکر می‌کنم عدم مطالعه دقیق در این بخش‌ها باعث شده مطالبی تعجب‌آور از سوی این عزیزمان مطرح شود. مجمع عمومی فدراسیون فوتبال دارای اساسنامه، دستور کار، اختیارات و تشکیلات مشخص است و طبیعی است که اجازه دخالت به فدراسیون کشتی نمی‌دهد.
🎙
برگزاری این تعداد مسابقه، امری خاص است که به سازماندهی، امکانات، بودجه و سخت‌افزار نیاز دارد. برای این ۴۰۰ هزار مسابقه باید ۴۰۰ هزار کوبل داوری اعزام کنیم که اصلاً موضوع ساده‌ای نیست. در کنار آن، بحث امنیت، پزشکی و بسیاری از موارد دیگر را نیز باید در نظر بگیریم.
🎙
این کارها نه دوستانه است و نه خصمانه. نمی‌دانیم باید اسمش را چه بگذاریم. ان‌شاءالله این‌گونه نباشد و هرکس سرش در کار خودش باشد و موضوعات مربوط به خود را پیگیری کند.
📺
دبیر امروز گفته بود: نظام باید یکبار در مورد فوتبال تصمیم بگیرد! دولت، مجلس و‌ وزارت ورزش دارند برای فوتبال هزینه می‌کنند؛ باید ببینند از فوتبال چه می‌خواهند.
@Sportfars</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464573" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e665a077a.mp4?token=d2xG4jLgGb5uIC4ptimEt8ZNwAlLEjS3Qsl3-goe8kJDwrcZ6FnUU8bEf_S8jKeWA4M7JjFBnz_907R9dUbX75E7B4BiMPS0NgKE98ERlWQrN9W1zXnJok9iOm4lOHBqxjyOG-2VoVelbmqwpa_1E-tjna8z808IAQSH1MaEM6RWEqBKb9xCXKCNcF9X_5tGokUVh_AEGbNTQVCk6_LyUQBw_f1deOPxLFezdgeCiTCnkLoFqwBmvZlSPVX-DcYMclF80xThZH5vvwcx7VqC_GcUF43o6qX6XCramUktW6DmBFOyiuV8P9abrbDZT1fGk55SKsBTCnE_1xC7Mfz62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e665a077a.mp4?token=d2xG4jLgGb5uIC4ptimEt8ZNwAlLEjS3Qsl3-goe8kJDwrcZ6FnUU8bEf_S8jKeWA4M7JjFBnz_907R9dUbX75E7B4BiMPS0NgKE98ERlWQrN9W1zXnJok9iOm4lOHBqxjyOG-2VoVelbmqwpa_1E-tjna8z808IAQSH1MaEM6RWEqBKb9xCXKCNcF9X_5tGokUVh_AEGbNTQVCk6_LyUQBw_f1deOPxLFezdgeCiTCnkLoFqwBmvZlSPVX-DcYMclF80xThZH5vvwcx7VqC_GcUF43o6qX6XCramUktW6DmBFOyiuV8P9abrbDZT1fGk55SKsBTCnE_1xC7Mfz62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: طبق برآوردها حدود ۱۵۰۰ مگاوات ماینر غیرمجاز در کشور فعال است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464572" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlwFai9zHjnkc2iZTXAbQzk3GH9SLDRLNYf5e9_7IlGec1t9nrAnUmGcHGQ20vgGsxyu_E5WvqH4ZsnDKi8goXwBGAInlq1Pr7qu3HsquDvu1cVNRcOJmcKLfa56GXaXT5R7iAezj6wmprG3bQ8TxSNZqX_CKnK2OSVGW4pFXhSLddVoHXfXmuToso8YE1CHTEmlX5KmdjNe6IAZcL0SoBtZEazfwWX6yX6-6AhT23lkY15RMT0h_9x4uUuXzxXnSsZ0V69rG0mb_aaSl_uuVVjDr671S0JE8YFUOL5f1SZ_ibeTCLpGnWraIx18uhs9FS6qEh1zH4k4oIYaeXtzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واردات سامسونگ و ال‌جی آزاد شد
🔹
سازمان توسعه تجارت ایران در نامه‌ای به گمرک اعلام کرد: با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🔸
با وجود آنکه تولیدکنندگان لوازم خانگی کره‌ای پس از برجام بازار ایران را ترک کردند، اکنون مسیر واردات این محصولات دوباره باز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/464571" target="_blank">📅 18:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464570">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9u6y2k3rYrUSa5YokufOO4IzPeKda3K9ZJdAAz-L5vZcLd7-MZMhH73pNUyUNhcD2VBb9CeXTQCbtzAyoPpRpfWA_w67MduoSDkiDd_osmoYcPdU-HaDcNBtVL8MbPviYygFrtUfWZhZ-eNdA5oS-Y2WbhyN7ij-xiErU0Y2JipCR3PjbrAIB0In8SoO_SDPsISrjs9F9kTkT_osjYSMLEFT7c2NCPtm8r6fves3fNqpw6zasEbYNyn40ylvEZTfkqVgJSBTRXbQTH68r0HtahxDJh74u5Wqm_qDzclLPQMnSRh5m6tNeqRBPxBsv4MRSvQOjxERQYCuRDD3eQvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد اوکراین به خاکستر نشست
🔹
کارخانۀ فولاد آرسلور میتال اوکراین  هفتۀ گذشته هدف یک حمله موشکی روسیه قرار گرفت. این چهارمین حمله به این کارخانه در پنج هفته گذشته بود.
🔹
بزرگ‌ترین تولیدکنندۀ فولاد اوکراین حالا اعلام کرده است که تولید در این کارخانه را از سر نخواهد گرفت. این شرکت به دولت اوکراین اطلاع داد که ادامۀ کار در این کارخانه دیگر به شکلی ایمن و پایدار ممکن نیست.
🔸
بخش فولاد اوکراین یکی از قوی‌ترین بخش‌های اقتصاد این کشور است و پیش‌تر حدود ۱۵ درصد صادرات اوکراین را تشکیل می‌داد. این بخش حالا هم از حملات روسیه و هم از محدودیت‌های تجاری اروپا فشار می‌بیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464570" target="_blank">📅 18:39 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
