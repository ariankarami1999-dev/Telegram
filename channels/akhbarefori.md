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
<img src="https://cdn4.telesco.pe/file/ODSb7qYGPBSP8CPij_bTJauttfoMmkYDajAkfCyexnIg6cXBE-3-SKgtMVwmtq6QYOj8DuOGWRyPrHREQQwXk5d8zT0StXV2y2NLf6nXKmHVZ8JIq7_KIS2U5AalaerSoht-r9jL8SuhGdP6Kp_FMDZKzpebEHWE3bs5TWLd-WY_pH4suARqj3cfLuWjzTTcc0HV3OR_TkqZ_KnC88byIsmhxUUKqYtoZYLj7rYlaCE_AFqPqmclqj0_srzQCK0lg8_jkLgq_eWl_e3waIbz_4kW9wg4oMz0lWSnbZb-e7KblN82BmO5oOVF0YlIbI2dormFLM52d3U70TsjZfq5Lw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 01:00:47</div>
<hr>

<div class="tg-post" id="msg-654911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0Eyw3H4W5qJ_d8GRWu84bK45ZvI4s5XHx5f8hO1Wn8FHqbkO4BbvK5g5ae4ky0OW-N9mItbWX0WPWeSt6NifQ8WDG7clM_JK1ckgWhpQ9O0qJIzKLcQV5pQ_Wk01G05gpCSxRwvF0ad53AzsDRce3LLAxU90jAuEd_09CjxPhHD7VGwpk5VBdN46cUr0deyD1zFl6WA41afiqML_NEImH9czQaTzlLY9b5Wq-OTPpSGvKEd0bwhIKDvUjuw5-AW-VvuNAO-Lqhq7MGdqArk2XSu2R-rzUHcDQNrYU-vvJlPxW6Wjt2d4_op4VgHTgokCwpgDpCdit3kofEAe49UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/akhbarefori/654911" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9A755W2WF6NrkQZL_QsqK5RV_QSCGEZ7ZYNZPqruabpVYzE4BmvwRKwbpzWft8ktHK6hjoZI30tg4iEYV131wArsHojjMc0gRIAcxH7xJGTrFGYeKHdYGmFf9SctW7WKI2KkIG6QcgT_Z4tEEId_fTjf-ILqssLSxbLV9WSxUT-zCGfre5T4WjMYQYUe6qIzGnYVVhlxRG63GEqvqa6iwtohcMpSA2R68Jt49jubEBSpoALPnr_0zOwsZAuSOn_I0parGUrx66Xzv4GXXyn1ulZpl92bVm1U-VSfiEMl1Kd8l9iVuMMxuNUzGRAoGWwNDRR3HaEcHiEssWulAISUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجاره کشی
🔹
شرایط کشور باعث نابسامان شدن بازار مسکن شد به طوری که بعضی صاحبخانه ها غیر منطقی نرخ اجاره خانه را افزایش دادند و از شرایط موجود سو استفاده کردند. در خصوص وضعیت به وجود آمده وزیر راه و شهرسازی: تعیین سقف افزایش اجاره بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می شود. در حال حاضر بیش از هر زمان دیگری نیازمند همدلی مردم در تمام امور مخصوصاً در بازار مسکن هستیم
🔹
هفتصدوشصت‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/654910" target="_blank">📅 00:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfqtxKm7316yTeZOzwWxxgIDK0OcGhxzBDUPaTX4cklZ7lMEfoWBugM_B9I6ZlVNiinj7ZhWiEpsX0o8Bl2C39DbAkZIFsqLTYh-BLeKoODpyWEjKaSXlm_aMT4Ge59mRD4zb_aHWD64QcZGWrGDDeFdcEUOBbc-_I_AhZhXNC7aXk_VdnVno1pT935PUdkXc_SdBw52aIJp0dP43fJ05uRuyLovPCH9Thx68fDV34840g9DAo_N934YTbeJwgHJD70lrd0fXHiuPM3JPc2KaOKkH7ZToMmfqInInY_WAwS6iZqmJw_S_8CW85qg4WsIfaCLcUgTL-3CUQt9CxMiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر دیده نشده از شهیدان: سپهبد محمد باقری، سید حسن نصرالله، سپهبد محمد پاکپور و سپهبد حسین سلامی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/654908" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8n2TlvxH_vU78-wYzjMnAqCoZjdaDh6XyWKMUbm5qruMD1nbgETck8URoa7bb_6Olm77_EsJ6CiyUENk4BhUeAWrc8RhOlwMy1T5YFvNbTLn5B8hqZ4h9GyXjL4I-2VolwrnsgBgVF5uNjC0rnftfYdUYLmxEBrq2MAq2OHtNEQjlRY4J3RGrkP_poLF6JxzqpYM0E2p3FySnXYKdt6gBAJp6HSNE2VzWKX33zRbzyeRKyk4Yoj2-I1qhDIbTcoL72ZPotH_4fcH3pZOQYmoi1w7gYInnd6smA3IIB3oTqwsy8BtRNR5O9URlS93J43IQUctCQwwBVX35TgdFTj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ چیزی که هیچ‌وقت نباید دور بیندازید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/654907" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654906">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در بیروت: اسرائیل خیز بلندی برای اشغال شهر نبطیه برداشته است/ دشمن در ۵ محور در حال تلاش برای نفوذ به شهر نبطیه است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/654906" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654905">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoSoTQ3or2SRD-IgFJMs8JK4N9DKIAWORiVuVVm2Finau2ska8DWTbKCZcWcvFeyc3cvS4O3qVdL-mAb-qFWJ8irCOYyxYwZtGXVBtsPT72_6JIAYcO5XK1F7a5VyHi1KDyJJ0ZuI-24wcys4d229vXu0lbCwD4G5M4g1JHYF8TuAKlW5q7MT1_mEz0KIfAEX91Jq2Lw55rYpPimayjdmgKBS5xpewvNdGGTJP7_eTSuFfsLfQiCEWCYBtI3FUhXFmi3gVn-dcVXojqX3X8K4uUMIOny5u7J2Da0SWe9rMXfgbQz1rO7SivwxzXg975cO4hR6U-bAjmBAguNTuYtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران بعد از جنگ برای سلاح‌های خود مشتری پیدا کرد
ادعای دنفس اکسپرس:
🔹
ارمنستان برای اولین بار سامانه پدافند هوایی کوتاه‌برد مجید AD-08 ساخته ایران را در رژه نظامی ۲۹ مه ۲۰۲۶ به نمایش گذاشت. این اتفاق نشانه روشنی از فاصله‌ گرفتن ایروان از مسکو و روی آوردن به تهران است.
🔹
سامانه AD-08 این بار روی شاسی ایوکو دیده شد، نه روی شاسی معروف ARAS-2. موشک این سامانه با هدایت فروسرخ غیرفعال، از رادار یا سامانه الکترواپتیکی تغذیه می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/654905" target="_blank">📅 23:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654904">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در بیروت: اسرائیل قصد دارد شهر نبطیه و صور را در لبنان اشغال کند تا دست آمریکا در مذاکرات با ایران پر شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/654904" target="_blank">📅 23:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654903">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: قدرت و اقتدار نیروهای مسلح پشتوانه محکم وزارت خارجه در صیانت از منافع ملی ایران در عرصه دیپلماسی است
🔹
فداکاری‌ و رشادت نیروهای مسلح جمهوری اسلامی ایران در دفاع از کیان ایران مایه افتخار هر ایرانی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/654903" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3219059
🔹
تاریخ برگزاری کنکور سراسری و ارشد مشخص شد/ سهم سوابق تحصیلی و سهمیه جنگ زدگان
👇
khabarfoori.com/fa/tiny/news-3218868
🔹
ماجرای حضور رئیس‌جمهور با تی‌شرت آستین کوتاه در یک جلسه رسمی چیست؟
👇
khabarfoori.com/fa/tiny/news-3219063
🔹
عکس عجیب نابغه ایرانی که نفر اول جهان را شکست داد
👇
khabarfoori.com/fa/tiny/news-3218974
🔹
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
👇
khabarfoori.com/fa/tiny/news-3218959
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654902" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654901">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
داروهای افسردگی به کمبود خورد!
وحید شریعت، رئیس انجمن روانپزشکی ایران در
#گفتگو
با خبرفوری:
🔹
داروهای روانپزشکی، از افسردگی تا دوقطبی و اسکیزوفرنی، با کمبود مواجه شده‌اند. نگرانی اصلی این است که این لیست در ماه‌های آینده، بزرگتر شود و داروهای فعلی هم قابل تأمین نباشند.
🔹
سرچشمه بحران روانی امروز یک چیز واحد نیست، بلکه تصمیمات کلان حاکمیت و نوع نگاه به مسائل است که روی همه چیز سایه انداخته و رسانه‌ها باید با دیدن واقع‌گرایانه یعنی نه بدبینانه کاذب و نه خوشبینانه کاذب به اصلاح شرایط کمک کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/654901" target="_blank">📅 23:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654900">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎬
#تماشا_کنید
💫
دکتراخلاقی در نشست بررسی راهکارهای گسترش تأمین مالی غیرنقد عنوان کرد:
✨
بانک تجارت با تکیه بر تأمین مالی زنجیره‌ای و به‌کارگیری ترکیب ابزارهای نوین، آماده همراهی با مسیر جدید تأمین مالی کشور است
💠
دکتر اخلاقی با تأکید بر ضرورت عبور از الگوهای سنتی و حرکت به سمت ابزارهای نوین مالی، گفت: بانک تجارت با ظرفیت بالای تأمین مالی گسترده و بهره‌گیری هم‌زمان از ترکیب ابزارها، می‌تواند نقش مؤثری در هدایت منابع به سمت تولید و پایداری بنگاه‌های اقتصادی ایفا کند.
مشروح خبر
👇
www.tejaratbank.ir/news/2417055-bt.html</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/654900" target="_blank">📅 23:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654899">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f7bfc0ac.mp4?token=oU72IQjFaJow7rjx731Tt07HM0DcMgMBwzm_QlnrH-E2ga69TnHYZxrSkCE2wiwjH6-zB_jygigqrNs765gJ85xiJPkc2iF7W-I-DjrRKUME2iVaBa7wQAz57bI_l-f6QnSWHg6n_tSOewGHiLKhvCPVKT1QqsQCZ1BEYhs8NnAdOcBwq7X4439vosPhPbyDeET7qf6jCz9Scu7V7gcABqRSkOXMILdGOXIMoXRBNSKW8ERI833l-rfTkz5IeDMLRTFgYwSwbGrxCWfSom7qmf6cit-DutxRCTaWnOAL6U03TJZx7FLjm0JXMeGAGMZ4Br2mmsQwSKNfW61A0AEavgutSJw7Lhg8dvRBu98o1luqwLkpZLRlk5TbXi2hWfLpOPCuVU8Nrzfys6IU_vGn0Z2yw0pJr0E3KHFjfRltSF-qqSGHnRVf8l396UDbGXuRyGABRp9KfNjnMsgFwzvmTXGnHXHLGD4oLmJBZY6HSTkWBIqHtp-q9wT1Uwp2BNmc1zr2v4w5S9BrYrCWRrpp9XkQm-z42NfcWl3jI8mHQ8pEWEJvUzIvWsy6m_bG7-ZCDL_8foSK_CHP3aLcfRWauy3BHjNWMZS8yK48j9ETlq5ISbxsZwG5VowRrWH9HCNLkX94hdyRWN76tjO2LtFCcWIDjln1lWeFnB29bGlpDnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f7bfc0ac.mp4?token=oU72IQjFaJow7rjx731Tt07HM0DcMgMBwzm_QlnrH-E2ga69TnHYZxrSkCE2wiwjH6-zB_jygigqrNs765gJ85xiJPkc2iF7W-I-DjrRKUME2iVaBa7wQAz57bI_l-f6QnSWHg6n_tSOewGHiLKhvCPVKT1QqsQCZ1BEYhs8NnAdOcBwq7X4439vosPhPbyDeET7qf6jCz9Scu7V7gcABqRSkOXMILdGOXIMoXRBNSKW8ERI833l-rfTkz5IeDMLRTFgYwSwbGrxCWfSom7qmf6cit-DutxRCTaWnOAL6U03TJZx7FLjm0JXMeGAGMZ4Br2mmsQwSKNfW61A0AEavgutSJw7Lhg8dvRBu98o1luqwLkpZLRlk5TbXi2hWfLpOPCuVU8Nrzfys6IU_vGn0Z2yw0pJr0E3KHFjfRltSF-qqSGHnRVf8l396UDbGXuRyGABRp9KfNjnMsgFwzvmTXGnHXHLGD4oLmJBZY6HSTkWBIqHtp-q9wT1Uwp2BNmc1zr2v4w5S9BrYrCWRrpp9XkQm-z42NfcWl3jI8mHQ8pEWEJvUzIvWsy6m_bG7-ZCDL_8foSK_CHP3aLcfRWauy3BHjNWMZS8yK48j9ETlq5ISbxsZwG5VowRrWH9HCNLkX94hdyRWN76tjO2LtFCcWIDjln1lWeFnB29bGlpDnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزگاری که سهم زنان در بهترین حالت زاییدن نوزاد پسر بود، شیرزن بی تکرار تاریخ ایران پناهگاه آزادگان بود ...
ویدئو کامل
👇
https://youtube.com/@caffeinepodcast2025?si=nNwcikUeYdjW2ckV
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654899" target="_blank">📅 23:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رضایی: محاصره دریایی یا با مذاکره و یا زور پایان می‌یابد
🔹
سخنگوی کمیسیون امنیت ملی مجلس تصریح کرد که محاصره دریایی ایران یا از طریق مذاکره یا با اقدام نظامی پایان خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/654898" target="_blank">📅 23:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx-Kz5AGj7HqbEgKbSwc6XDJLDZqmQiDKhQ3saWGrbJqXlYqqaavSC8Xs4DVil046GuST6C52z3nkJIq62ikQO9LZK_qFjFqtW4WeOCXXz_tAv01YHcopowvEc_7zdeARskB5af8DaVjb-poc7Y4qibrg2eUAO8tYmoINsZ9JCHSzgh2gLdvTazKkUWaRdTMjvM88v8rGX1VFZdYXF8Pc4ahxvrjP7TL4nin_uWhdF7PChyGkWcjZ_gvHOXd6rOv0_TYls_DcNFA8W313wjKjTd11-mct6O-pXg6Kjy-LxHk-ey44OkhqhLOyc1xJnOCMXfq9J3hkz5IPnWrpkwBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران چه بر سر بورس کشورهای منطقه آورد؟
🔹
بورس‌های ابوظبی و دبی به‌ دلیل وابستگی بالا به گردشگران و سرمایه‌گذاران خارجی، افت‌های دورقمی را تجربه کرده‌اند.
🔹
بورس بحرین هم با توجه به اقتصاد بدهی‌زده و تاب‌آوری پایین، منفی شده است. در مقابل، بورس مسقط با حفظ مسیر تجاری عمان، بیش از ۱۰٪ رشد کرده و تنها بازار سبزپوش منطقه است.
🔹
بورس‌های عربستان، کویت و قطر نیز به‌دلیل درگیری کمتر و تاب‌آوری بالاتر، زیان‌های ابتدایی را جبران کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/654897" target="_blank">📅 22:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051195522a.mp4?token=DA3Pd1BKN7mPGHlLyTFzXc6PD0GE086Z9Hi_xpxvie-b2Q7JWkthQkJIavAGYmWVdlUAxr2NeLxfPYGlpMMmKAKXH2mZUgiRN3hNQOH6BHSMN8_E7DAFcgPZPXQ6dBDiVQNAedoF_4mDTj3rHNMRnwQyW7fvJsRqhUHe_xiSlE_o9JfIOePyWH5vWH7tck9CGgTfG5Y5FmCkSy_ZLePocv3CLu_lklVL_kLWXSSM9w5Q38ARZwT5kpGqM8sKqraaFN60uOfiOYQL4MJ6Bnju9jrVnKUatpXXpuRI8OU8uKmYdBQLyN4OHpWfZViiNV4_C_Q3jagBYLEmFJsH_YNOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051195522a.mp4?token=DA3Pd1BKN7mPGHlLyTFzXc6PD0GE086Z9Hi_xpxvie-b2Q7JWkthQkJIavAGYmWVdlUAxr2NeLxfPYGlpMMmKAKXH2mZUgiRN3hNQOH6BHSMN8_E7DAFcgPZPXQ6dBDiVQNAedoF_4mDTj3rHNMRnwQyW7fvJsRqhUHe_xiSlE_o9JfIOePyWH5vWH7tck9CGgTfG5Y5FmCkSy_ZLePocv3CLu_lklVL_kLWXSSM9w5Q38ARZwT5kpGqM8sKqraaFN60uOfiOYQL4MJ6Bnju9jrVnKUatpXXpuRI8OU8uKmYdBQLyN4OHpWfZViiNV4_C_Q3jagBYLEmFJsH_YNOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه بالا بردن جام قهرمانی لیگ قهرمانان اروپا توسط مارکینیوش، کاپیتان پاری‌سن‌ژرمن
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654896" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654894">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d00b4012d.mp4?token=mVvBJqhVakH1NPUgGGfadmGsAQPSTGk3gjQ4p1yHPFGsbnha132iI0D50DHxHSqFHbBLGMSMblUSyUvR3QxpoCNhgkpuXZ2WwQksandm97megummKtUmdoFqfZ_Z9N2_HUhowWCFbFWQ688cqEhs2domfzzNOghe2IegrfyaOtKy6Nhc-qRkRLR4zgN4LAIVL-LYNuLyymxTs242aiLtai_HiUxGht2v_Sxz1xxTUdiHA3Yj7RynPyBzn3FyNddGbtYqN9Hlo24X0K3auUsb6zhcZ_ye6C88hXhjyRbHVdLe0lbNrWSakSfo8uncuJy_HQx3SqlIwgtyCU97StDRoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d00b4012d.mp4?token=mVvBJqhVakH1NPUgGGfadmGsAQPSTGk3gjQ4p1yHPFGsbnha132iI0D50DHxHSqFHbBLGMSMblUSyUvR3QxpoCNhgkpuXZ2WwQksandm97megummKtUmdoFqfZ_Z9N2_HUhowWCFbFWQ688cqEhs2domfzzNOghe2IegrfyaOtKy6Nhc-qRkRLR4zgN4LAIVL-LYNuLyymxTs242aiLtai_HiUxGht2v_Sxz1xxTUdiHA3Yj7RynPyBzn3FyNddGbtYqN9Hlo24X0K3auUsb6zhcZ_ye6C88hXhjyRbHVdLe0lbNrWSakSfo8uncuJy_HQx3SqlIwgtyCU97StDRoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در  شهر بوستون در آمریکا
🔹
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگ‌ترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654894" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654889">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای سنتکام: برای اطمینان از اجرای کامل محاصره دریایی ایران، ۵ کشتی تجاری را از کار انداختیم و ۱۱۶ کشتی را تغییر مسیر دادیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/654889" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654888">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 60</div>
</div>
<a href="https://t.me/akhbarefori/654888" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصتم
رائفی‌پور:
🔹
0:07:10 خاص و ویژه بودن کوروش
🔹
0:19:20 عزت اسلام و حیات زمین در گروی ۱۲ خلیفه بعد از پیامبر است
🔹
0:26:15 معنای لغوی عاشورا در عربی
🔹
0:41:00 روایتی از حسادت صحابه نسبت به حضرت علی(ع)
🔹
0:55:50 اموالی که باعث آتش در قلب ها می شود
🔹
1:01:20 وحی‌الهی در معراج با صدای حضرت علی(ع) برای پیامبر
🔹
1:26:00 پشیمانی ابوبکر از آتش زدن درب خانه حضرت زهرا(ص)
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/654888" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654887">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
انفجار در  شهر بوستون در آمریکا
🔹
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگ‌ترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/654887" target="_blank">📅 22:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654886">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e21b66fdb.mp4?token=ipG72VWYq6YKkcx3L0d5PXPTGcaGyKEQrGAX5rh75Inq3ssB5jjgJfWP16jQ7oWs-9XiIofFgE35Ol85vN0is5iaQvw-FCFqe2PM34-ENWvP_0wA5yf3FIO1djgKBxlUBzzVZj1EXZt8XynmB2DSXzkWWOTxFpzC3Nh8QevZFr-kZoHldzdUFe6MboIsbmyMHo5lOZI6y9B5CWehPAndEl-M5TIzv0SyF2mzxS_fPZjsXsKtlbbfvnL0fyCKvDX3RVqR0hU0PkrifCQYz54WxPDm47IMHHdpU3J2Zq38YXZF1XsHxURc55R3ActoqaDHx_QLo8X5Imw39J1hLQ38Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e21b66fdb.mp4?token=ipG72VWYq6YKkcx3L0d5PXPTGcaGyKEQrGAX5rh75Inq3ssB5jjgJfWP16jQ7oWs-9XiIofFgE35Ol85vN0is5iaQvw-FCFqe2PM34-ENWvP_0wA5yf3FIO1djgKBxlUBzzVZj1EXZt8XynmB2DSXzkWWOTxFpzC3Nh8QevZFr-kZoHldzdUFe6MboIsbmyMHo5lOZI6y9B5CWehPAndEl-M5TIzv0SyF2mzxS_fPZjsXsKtlbbfvnL0fyCKvDX3RVqR0hU0PkrifCQYz54WxPDm47IMHHdpU3J2Zq38YXZF1XsHxURc55R3ActoqaDHx_QLo8X5Imw39J1hLQ38Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از ۱۰ سال فینال به وقت اضافه کشید
🔹
آرسنال ۱ - ۱ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654886" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654885">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سرانه مصرف لبنیات به کمتر از ۵۰ کیلو رسید
ظفری رئیس هیئت مدیره اتحادیه تعاونی‌های فرآورده‌های لبنی کشور در
#گفتگو
با خبرفوری:
🔹
سرانه مصرف لبنیات الان به کمتر از ۵۰ کیلو رسیده است. شیرخام حدود ۳۳ درصد افزایش قیمت داشته و به تبع آن محصولات لبنی نیز افزایش قیمت داشته‌اند.
🔹
قبلا ۱۲۰۰ واحد تولیدی بودند که الان کمتر از ۲۵۰ واحد مشغول به کار هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/654885" target="_blank">📅 21:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654884">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb1GVyB8dOYzeMZB7-r7PtZSeLD3_9pVpFa4JaRJpeGLJAd10J0oThDw8k4hqA7QyPr-emsSEAAJcN_-J4RDwrND_PJ48K6yBhLvKNTdtAbZMnwDNC4rIuNeOiUbYuq3JrNT5dTDEu10R8mPZSVIWFDCkdFjtcxQtnPCaST0_IxV8D8Jk3Ep-_k08kUAxKxBQGMoJIwtd-Yf0HedkyRFWbn3KD1_Y5juhdUTCZ9Byah_4wkWQ-iwxHnDB9aqEg3glgs7IAPfHrJN5pRHTdbutdEb6F53xkbN-qQmXRsK1pQTMxr8h9al53eCFoeeJ0kJzgbwizTeYuZ3-gwJjsgThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار‌ وزارت بهداشت درباره نوشیدن قهوه در تابستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654884" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654883">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25bca53dd.mp4?token=QRwzKsRDpms6r6UtG8FKDHTRRphGD9QWmUWOxH5B4g9Di0DzMREMK7FQ3v6V5dT6OjpN3nmsSW-o_5NqkqDTCti8j2lfgC2wznZyWJmro7wl_dfxsXmgLEQqTXcVfVb8dCICobYxTVjuGtV_pLo0SG3bsWjRLVvynFUc3NzlLtHU934gHjZ57fy1lPFuScJId_RVKIDzTtzLBo2Twus7jGBd5TA8P8SpW2-DnbRgcqzBVBC9RPC7E-hz73XoFCQCuHGqX_F4vU9Q1tSr4a2bAZad4gH6G97JG4a-tuPn_U97-jKfJW4f_RITOjqHFAdifc7Ec9CjcVt-j74agzALiwQCHe7uD-yP-pNz5-7dI-1OAX3bzmP6Vpqzp81zRmYNLVWhXY_odod9CRa_LEyn8X5hT2bP_shyhOeMC1srz36TE6_DpK9iH6jCuMi-xopOA-Ugzq2HcEM8nxdWNpAlRi8EkiKbXBSXK3-cuc9EazadNfk1b2T90Thrc52G1la7q_0WDlpl7BeWWlL-ToRWSIOvsgx7NQsk0NcVfS1qUux0sHZvgHdXiGchDOqwQ7SFjzYd21_Z_kg9LbJTU-hrkeIUW9dsAQF_d_Vik6MFZ-TliqxVWLGnZbZqgvtW8bxVYtHiygPxoaE2VnKkEce4HLcjNyd9vrLway_aCEQGpeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25bca53dd.mp4?token=QRwzKsRDpms6r6UtG8FKDHTRRphGD9QWmUWOxH5B4g9Di0DzMREMK7FQ3v6V5dT6OjpN3nmsSW-o_5NqkqDTCti8j2lfgC2wznZyWJmro7wl_dfxsXmgLEQqTXcVfVb8dCICobYxTVjuGtV_pLo0SG3bsWjRLVvynFUc3NzlLtHU934gHjZ57fy1lPFuScJId_RVKIDzTtzLBo2Twus7jGBd5TA8P8SpW2-DnbRgcqzBVBC9RPC7E-hz73XoFCQCuHGqX_F4vU9Q1tSr4a2bAZad4gH6G97JG4a-tuPn_U97-jKfJW4f_RITOjqHFAdifc7Ec9CjcVt-j74agzALiwQCHe7uD-yP-pNz5-7dI-1OAX3bzmP6Vpqzp81zRmYNLVWhXY_odod9CRa_LEyn8X5hT2bP_shyhOeMC1srz36TE6_DpK9iH6jCuMi-xopOA-Ugzq2HcEM8nxdWNpAlRi8EkiKbXBSXK3-cuc9EazadNfk1b2T90Thrc52G1la7q_0WDlpl7BeWWlL-ToRWSIOvsgx7NQsk0NcVfS1qUux0sHZvgHdXiGchDOqwQ7SFjzYd21_Z_kg9LbJTU-hrkeIUW9dsAQF_d_Vik6MFZ-TliqxVWLGnZbZqgvtW8bxVYtHiygPxoaE2VnKkEce4HLcjNyd9vrLway_aCEQGpeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار گروه هکری جبهه پشتیبانی سایبری به شهرک نشینان صهیونیست
‌
این گروه اعلام کرد:
🔹
منتظر حملات شدید سایبری ما باشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/654883" target="_blank">📅 21:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654882">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6e036557.mp4?token=umLmo2cFDCax-QpAIg8eUTTwyh5yf3ElUvz2RD-N2GRvZJE3vReiqP1bRUE4_qjepSwUKDzSzrnFlGtDy0U2ng9LTBjEsFJvUnxwuomc3q5krzaSE54gPUr967Zhn3SSZ4A0Mzlyeh2zXIV75974Hte4rm2pFLbAojvG5ZzY5c3Ld7fdxLfNWuuAZo6BES2jiscepJn-oW0aWyOms7tHrSh99mm-6G-IZ6udHf2zKOU17rjC_aByT1rzTCYyFiV7BhkCUIFvb2b777R7sTbFiaKxfJiA-3aSlRZYxF2FQKpNUrkQN6YiWAgoFdRFVNv6nmv1PRQFQYp0ovnvoxJHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6e036557.mp4?token=umLmo2cFDCax-QpAIg8eUTTwyh5yf3ElUvz2RD-N2GRvZJE3vReiqP1bRUE4_qjepSwUKDzSzrnFlGtDy0U2ng9LTBjEsFJvUnxwuomc3q5krzaSE54gPUr967Zhn3SSZ4A0Mzlyeh2zXIV75974Hte4rm2pFLbAojvG5ZzY5c3Ld7fdxLfNWuuAZo6BES2jiscepJn-oW0aWyOms7tHrSh99mm-6G-IZ6udHf2zKOU17rjC_aByT1rzTCYyFiV7BhkCUIFvb2b777R7sTbFiaKxfJiA-3aSlRZYxF2FQKpNUrkQN6YiWAgoFdRFVNv6nmv1PRQFQYp0ovnvoxJHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لو رفته از عوامل پشت صحنه جنگ ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654882" target="_blank">📅 21:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654881">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV3p3e-f5b7I7ZJyWRwptWcC2tL6BhVnmXG9msWH8xsua8cjySTStbY0-bH4ZyuPfhqGJk2iUnfmnfYQ_HEUMosfD8qSx5EMdNqYPyHRTTv947YQGwzU87MbTfzEABLR0XbyoChLRGbRTPNKqzJFSBFTpysD5hZl9Xb_AYcNhFsD4pnGQ-79NVfyOw84CWdOgCM62vYmtdbJPGxq55Hg8bXCdKM8W7hcnenxQOhycv6OGvFtzGimG1YNsMPH9saGIueY2VN02iP0qnRTwSaIAq6wbtY2Hl5pqfcd_GLSc7M3KKD6LqQ7k4wbvJjaOpRwWjLGk24UnIlPg0zFPq0Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل مساوی پاریسن ژرمن به آرسنال در دقیقه ۶۴ از نقطه پنالتی
🔹
آرسنال ۱ _ ۱ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/654881" target="_blank">📅 21:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654880">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
🔹
یکی از مهمترین محورهای توافق ایران و آمریکا بازتعریف قواعد عبور و مرور در تنگه هرمز است
🔹
ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
🔹
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654880" target="_blank">📅 21:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654879">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf2a505e.mp4?token=FrQnqGDLANIfgTs4llTWCK5klT41cidLH_rVZiWxY7qEeJFmXqAx182ET5zpH3hVJkg0xCYDf8wVsIMQlabyKbG_XfBbx_SaLWR4Au2F7NGq0O0ldkVUqiHcP1YCXuQ6j7knQcjq2qElkKOUQdrYRolVs6W3gvGUQVquAPx4H_Yi838_wXaiDRdiTGO2qmMyep2Tdh8TQIvf8AYYFINQ8Q9NKkAp2acrp3jXABzIdHlObZE7xKVDJ9DR_pze_MvqM-adOjYP5cCGP2zQbyFfKgEnkDCry8NxUHajmyiFhJ-pTVsjyOJ3dBtzNd3VwBRQ1Wdc0jhim5xqhZ7jYS9Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf2a505e.mp4?token=FrQnqGDLANIfgTs4llTWCK5klT41cidLH_rVZiWxY7qEeJFmXqAx182ET5zpH3hVJkg0xCYDf8wVsIMQlabyKbG_XfBbx_SaLWR4Au2F7NGq0O0ldkVUqiHcP1YCXuQ6j7knQcjq2qElkKOUQdrYRolVs6W3gvGUQVquAPx4H_Yi838_wXaiDRdiTGO2qmMyep2Tdh8TQIvf8AYYFINQ8Q9NKkAp2acrp3jXABzIdHlObZE7xKVDJ9DR_pze_MvqM-adOjYP5cCGP2zQbyFfKgEnkDCry8NxUHajmyiFhJ-pTVsjyOJ3dBtzNd3VwBRQ1Wdc0jhim5xqhZ7jYS9Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنثی‌سازی بمب و موشک دو جنگ اخیر در تهران ۱۰۰ رقمی شد
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/654879" target="_blank">📅 21:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
🔹
یکی از مهمترین محورهای توافق ایران و آمریکا بازتعریف قواعد عبور و مرور در تنگه هرمز است
🔹
ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
🔹
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
🔹
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده/صداوسیما
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654878" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cczobadjQStpFB4PGLqR45mVgvO5rL91zgleHtPxAURxDNUxOdGLwb6ByFqI-NlZX9JlzdhJZA8I8u7cZuT9fmDDHdllanpflckplle_alUf9tUaiVclHBQWJ56VfH5KtGmHmjvyT4HoFNDeehbR-sGRxL_6LD3J8LDFf0puD4120B4Zk54O7op3lyhOlJY4sUZ5QHj9SEShLo0dZwn2L_ab-UnfzaGB6tPWDsyF-WRWNG3o3ZyECTUP8nsjsgEgIKtaptE7-4hpPQ7iuuyZshknpprLjq-o9Qp13pRKAwmyA3gutXU5SMFx0KtadMsmjxTLkFZ-LZ1VzwS_QLiw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکانت سفارت ایران در آفریقای‌جنوبی: تنها راهی که کشتی‌ها می‌توانند بدون هماهنگی با ایران از تنگه هرمز عبور کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/654877" target="_blank">📅 21:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654876">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تناقض کاخ سفید در توضیح علت کبودی دستان ترامپ
🔹
مجری CNN:  «در گزارش آمده که موضوع کبودی دست ترامپ با تحریک جزئی بافت نرم ناشی از دست دادن مکرر همخوانی دارد...»
🔹
دکتر راینر، استاد پزشکی دانشگاه جورج واشنگتن:  «این گزارش توضیح نمی‌دهد که چرا دست چپ او هم…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654876" target="_blank">📅 21:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654875">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نشست نتانیاهو و دیگر مقامات نظامی صهیونیست تا لحظاتی دیگر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/654875" target="_blank">📅 21:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654873">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f71830e2.mp4?token=EgL4S6zGG7P0TiPBxevjCRuiTrPBfcyidLkdB5SMP1X7s-WprpwEtpfKQLjYDdbWdcx2HY8pAKW12YdwfGevjYcSxxImSN3bTZ7RqQdUBZV6xP0LYEOeBBRb5rUXfzxg-vHW4TiZfIfntPOFdeUUZf2wdbZhlh3vfHeqApxdKkz-JlUOnvjQ8eUuC_Clbybe-Wc-yQwQMWl0dVLwuOU-EpaUMaxyRJ18LxAxzdogmeNRYNE8HBU-zh8WmS0su4tSYAPj9kdPJfQUJyg1ATRxXwC6gRctN8PjoogLiUtwFti0ckTfCM-hGVVADBgx14OZAFsg3W6pgICg8AbJWrH8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f71830e2.mp4?token=EgL4S6zGG7P0TiPBxevjCRuiTrPBfcyidLkdB5SMP1X7s-WprpwEtpfKQLjYDdbWdcx2HY8pAKW12YdwfGevjYcSxxImSN3bTZ7RqQdUBZV6xP0LYEOeBBRb5rUXfzxg-vHW4TiZfIfntPOFdeUUZf2wdbZhlh3vfHeqApxdKkz-JlUOnvjQ8eUuC_Clbybe-Wc-yQwQMWl0dVLwuOU-EpaUMaxyRJ18LxAxzdogmeNRYNE8HBU-zh8WmS0su4tSYAPj9kdPJfQUJyg1ATRxXwC6gRctN8PjoogLiUtwFti0ckTfCM-hGVVADBgx14OZAFsg3W6pgICg8AbJWrH8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرسنال به پاریسن ژرمن در دقایق ابتدایی
🔹
آرسنال ۱_ ۰ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654873" target="_blank">📅 20:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRfi7BnxHamO9qnINAEWYqs3MBN7fgOc_UbJSdom4JnYkVRTOx3FxJNE_DC0cU4mkr4yQSQ9m4u113AwKPIbtMm-gZMENMIrdHfQA_Qi2ByCpx9-aRHsb-GUeAiLfbMDzPvb3oiN5NU5q7hCH65AxEJoREFT1eZb_MnnKFcDThpo93D-hg-_-QuPRT_g24KsD9rvC_Z7q6Y8WlqJfoAf4Zn04PKq4_lryWx8DuRBJViAem3G4i6POZ2N-I6gLBxBk1V5mB0qdUw8R4q9IOZHFn6CCxvpBw1dJQvGWnXQvVnkNaXq6uhnVJchXEK4M4FDIV91Xi8NdY48n_EoU1JxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEkAnweMRo-fXrNk93Lf6J5lO6v8E8alMF1ldokwjspOrErcl_ok0l7ZOs8-s-g8xpwTDUK6EfCueQfFTKeTPIdzjinFrywEeJ0AS5Bu50wGtsJRlHM4oaeqrmAE2uRmn-st_8ZR-n-4rHIjcJx-MtooPcs3d-_-AyYnke16Dk2RvJ7taqRg1kVEDUZ14B6DQsndFsT372XZ_0mIxZI6Vt4ZgNzi9YiQD2IjE8OagD-JK0TNxB8AhThyXJikkxV12562t-VQQCim_-Ml1pJDd9HFt06i2A6_UIRYAh0GLFqM6zGFKm7AR91ZWM7WhX-khRTZeQqPlAFzlMj-yvMOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4zGggcGj2Q_llKgNukQVtbOwNp0y0sDr0yZt2pFynJusAcf8SPH0vUNJovrFLdBtrBXT6U84R_y1zoc1VcxFoLLIUzwCublfkCsIp68wnp8PpYrQOUlJ3f9dlyzJmyIqYtoMl3diGGE6A3zUOy-U8mNWPICTFkTh_QiY4CVrDDBJ1xqmldsvTFWxD8BhooaPF7xV4E1sQFhF_7rBUKK9ENEAAXcQDFyEVqS9kK5EOPfaxwlXVWUwvPLB5E6-Ppm9Hb6B89yXJedkx0eSy8FLddhdElw_m0wfaA4q9fJSEzinymMpJwqivcR0iy4Kvq_trUPM5ZaqzZGlHhH7skJ-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس‌جمهور برای مدیریت انرژی کت خود را درآورد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/654870" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvQswiNkvT_NTTmmfueN5EZcI1Lngzx5HH10_U_MJqF7IQwX13WpUjSJ7oKXNzrvnv7Yx9fFtsZVdWCVs-qYEfo0T9LCt-DSnStKi_4R-SvQf6r7p_MbxReSAyrVxGGOY7qryOs4gK3CIzqB0FVWRG7U1MBk4NiZJwl_YSlvzjOVQZSw2pWPikCrrLYeNNHHX1eEP4vF5DfG-RwtuRR-LvQEd0IPpdHhd6gip6JfotbUY_mOy30kdhfYDavkBmcvuU8YjmhXFx8jGa-oUAeZCm0Uf5HSgHgd-UJzjXLOr6tHocj5_OAiyWJPScGvevJVcnOW319nE19bc-hNWin-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این گروه‌های خونی بیشتر در معرض سکته مغزی در سنین پایین هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654869" target="_blank">📅 20:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
۹۰ درصد پول پروازهای لغوشده تسویه شد
‌
معاون هوانوردی سازمان هواپیمایی:
🔹
طبق مستنداتی که شرکت‌های هواپیمایی ارائه می‌دهند بیش از ۹۰ درصد از بلیت‌ها تعیین‌تکلیف‌ شده است؛ ۱۰ درصد باقی‌مانده نیز کسانی هستند که اقدام به آغاز فرایند استرداد بلیت‌های خود نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654868" target="_blank">📅 20:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
در تجربه مرگ موقت، آینده‌ای تاریک از خود دید؛ تصویری که باعث ترک اعتیاد و تغییر شد
🔹
06:00 عذاب کسی که به نامحرم نگاه بد و دست درازی داشته
🔹
10:45 نوشیدن اشک دیگران توسط جهنمیان برای رفع تشنگی
🔹
18:50 رؤیت افرادی با چهره هایی بسیار زشت
🔹
22:50 کدامین گناهکاران مورد عنایت قرار می گیرند و بخشوده می‌شوند؟
🔹
28:30 چگونگی مورد شفاعت قرار گرفتن تجربه‌گر توسط حضرت زهرا
🔹
35:50 حس تولد دوباره بعد از  تجربه
🔹
47:50 سفارش اهمیت به مادر و همسرم در طبقه اول جهنم
🔹
01:07:40 ماجرای شنیدنی دعای هدایت شدن درحق بدهکار توسط طلبکار
🔹
قسمت دوم، (منفی هفت)، فصل چهارم
🔹
#تجربه‌گر
: دانیال قاسمعلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654867" target="_blank">📅 20:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: آمریکا یک کشتی فله‌بر را در خلیج عمان از کار انداخت
‌
خبرگزاری آسوشیتدپرس:
🔹
یک کشتی فله‌بر لیان استار که با پرچم گامبیا به سوی ایران در حرکت بود، هشدارهای مکرر نیروهای آمریکایی را در طول شب هنگام تلاش برای ورود به یک بندر ایرانی نادیده گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/654866" target="_blank">📅 20:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654865">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
آزمون‌ساز شبکه شاد پولی شد
🔹
در حالی وزارت آموزش‌ و پرورش اولویت برگزاری امتحانات را در سامانه شاد اعلام کرده است که آزمون‌ساز شاد بسته‌هایی با نرخ‌های متفاوت ارائه می‌دهد.
🔹
از بسته ۵۰۰ آزمون به قیمت ۷۴۹ هزار تومان تا بسته ۳ هزار آزمون به قیمت ۳ میلیون تومان در آزمون‌ساز شاد به فروش می‌رسد. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/654865" target="_blank">📅 20:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اعلام آمادگی گروسی برای کمک به حل اختلافات بین ایران و آمریکا
‌
🔹
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد ذخایر هسته‌ای یک نقطه اختلاف بین ایران و آمریکا است و برای کمک به حل آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654863" target="_blank">📅 19:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرسنال به پاریسن ژرمن در دقایق ابتدایی
🔹
آرسنال ۱_ ۰ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654862" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اعتراف نخست‌وزیر لبنان به جنایات گسترده رژیم صهیونیستی در خاک این کشور
نخست‌وزیر لبنان:
🔹
اسرائیل تنها مناطق مشخصی را هدف قرار نمی‌دهد، بلکه سیاست تخریب فراگیر را اجرا می‌کند. اسرائیل با این اقدامات، به کوچ اجباری و جمعی ساکنان نیز دامن می‌زند.
🔹
تصمیم گرفتیم به‌سوی مذاکرات برویم، زیرا این گزینه را مناسب‌ترین مسیر و کم‌هزینه‌ترین راهکار می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654861" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام قهرمانی اروپا راهی ورزشگاه شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654860" target="_blank">📅 19:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItS6Jg2qMkI-fCQqJIjvnToIU6c8gn70eflznkyCe9l8aRGahm2vg8v51okVAqAI71r4gacDClGhFpH1KjNquPTJuwt-N1eLlNnUsX9alvFvxfn-Gds3CwUuhFCWSsmfvVad9YSLZjBaNIDCvj5k3dci2E1EsP7MqIYtuChTOIbhA1S-2tXTKRd89rDZXP0oivBDtH94i_x0jST2q_xo8bchTumS4q7F6NohLjUFe9TQhutNoB5be4VHTz6ccdrPkV_gzteuborFGkY91U-yynsvHIfh7b6vJnYq9W1X9SN_2YhQ4evla1H5Gp7x7Ms2TA6y_hNwur6bdc_ZbU3QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره کمک نظامی چین به ایران در جنگ با آمریکا
🔹
برخی منابع به ان‌بی‌سی نیوز می‌گویند ایران ممکن است از موشک چینی برای سرنگونی جت جنگنده آمریکایی استفاده کرده باشد.
🔹
افراد آشنا به این موضوع گفته‌اند که چین ممکن است یک رادار هشدار اولیه دوربرد در اختیار ایران قرار داده باشد که هواپیماهای رادارگریز را که برای فرار از شناسایی طراحی شده‌اند، شناسایی می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654859" target="_blank">📅 19:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654858">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQCfynls1vGMURgi_9dC8r6FMUZzfV55LCifaVpi-aAiGg7ZWeOoPEAAY5jlwBezBA07wtOHOFXQxzBNHdjTpOwADysOp6a2j58hBZ3Q_WCCghB6zdFErmri4ooR3N2S7zJcLwfiyvak2GEctsd4bn6Q4QlMn8p-KggVD-MLyFS0HAd3chkPDRqDIDiKXa5gcjhuqs4oz36iYa33IhuK2TbUvadnNgHXwCrzWE12mPPk8aKAqITTzBy8rFohhnEoXyXXDONXKOc6ycw0ENQfbM5vO7lDOOhQg-s3Bw6092X-5OYRjhJLVHvoAHPg9sPQnJndIUHykqfvgwl33nWlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از رنگین‌کمان در ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654858" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بارورسازی ابرها قیمت خورد؛ هر هزار متر مکعب حدود ۲۵ دلار!
جوادیان‌زاده، کارشناس ارشد توانیر و رییس سابق سازمان توسعه و بهره‌برداری فناوری‌های نوین آب‌های جوی در
#گفتگو
با خبرفوری:
🔹
افزایش بارشی که برای باروری‌سازی ابرها می‌تواند اتفاق بیفتد بین ۱۵ تا ۲۰ درصد است اما برای کل کشور اثرگذار نیست.
🔹
حدود ۳۰ تا ۴۰ درصد این افزایش بارش تبدیل به رواناب می‌شود که به شکل منابع آبی زیرزمینی یا پشت سدها ذخیره می‌شود و داخل رودخانه‌ها جریان پیدا می‌کند.
🔹
قیمت تمام شده بارورسازی ابرها برای هر هزار متر مکعب حدود ۲۵ دلار است و روش ارزانی نسبت به سایر روش‌ها است، اما روش پایداری نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654857" target="_blank">📅 19:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4pXEYoyRA4gOW3ogS6tm7xFf0Yu9q4RzLQWMw3AP1BVwFKRHSdzhnJ93LueLLWmouzR0NaKelyUoSnOKqt-79KXYcFYF-ggRYTU4kviMavq-OOnDKWShbDIG-ViPE92ma9LhsU6-nyEtLSUa38vOWIqTvxhskbAhkrgUKk_Iar0_xaPO8UxokN6CZU6yragFHl_y6HjDmg1mD7Ez2BHjfkj3JjrNToc1DhLKfmJM5qWjJUxEE8kM4Et9UVqG6N5i8ExuAhEOcnr3gU8pNP7PXr1iPXA9FrgBrK4TRRZVPWpf9NDkjxN5p067ok8sI4GHkeHyiX4oZV_MwdQSbJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندان بختیشوع؛ بنیان‌گذارهای پزشکی علمی در جهان اسلام
🔹
خاندان بختیشوع یکی از مشهورترین خانواده‌های پزشک در تاریخ ایران و جهان اسلام بود. ریشه‌های این خاندان به سنت پزشکی جندی‌شاپور در دوره ساسانی و پیش از اسلام می‌رسید؛ جایی که دانش ایرانی، یونانی و هندی در هم آمیخته بود. بختیشوعیان پس از فتح ایران این میراث علمی را حفظ کردند، به بغداد بردند و برای چند قرن پزشکان برجسته خلفای عباسی، استادان پزشکی و از پایه‌گذاران بیمارستان‌های علمی جهان اسلام شدند.
#نامداران_تاریخ
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654856" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز توسط نیروهای مسلح جمهوری اسلامی ایران با اقتدار کامل اعمال می‌شود
قرارگاه مرکزی خاتم الانبیا:
🔹
با توجه به یکپارچگی این مسیر، تأکید می‌شود کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفاً ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران انقلاب اسلامی هستند. هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.
🔹
همچنین هشدار داده می‌شود هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی ایران قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/654855" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W615WHkIQkHaSMUMbFXQWCWrXX20akHwjOfIlPTfqh6GG2mQFniuqZ-K2aYhcJXHXTF6x5ZCQ5isC90zcKmduEol5HFydEqbAcZ6FqWrCdkUmXt0VG5uzHwnti9iCnE5DZY4dVhgQ7oUZ9Gy-Z_fx67ybAKMVIFr51CQw3LRWjS0xtRJmerUIi3G0-c2C04IGnUVcOQ4UWlObsnaRaNeYyIJ0hmkznNKf0zIARQAqc9QrKnXXpHxvKl9UAOtHmAp_CWtkFYccq6ONpf6WiYxSCjxGLJiwFVRtQKUu43w3XTbs3lLD49XrKUy2HX6FGBmmdc5ljkRg2qU_mFMXYMFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ رکورددار تریدرها شد!
🔹
دفتر اخلاق دولت آمریکا فاش کرد که ترامپ در سه‌ ماهه اول ۲۰۲۶ نزدیک به ۳۹۰۰ معامله ثبت کرده است. یعنی روزی بیش از ۴۰ معامله که میانگین روزانه‌اش را از بسیاری از تریدرهای حرفه‌ای وال‌استریت هم بالاتر برده است.
🔹
در تمام سال ۲۰۲۵، او هر فصل حداکثر ۲۵۰ معامله انجام می‌داد. اما سه‌ ماهه اول ۲۰۲۶، ناگهان ۱۵ برابر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654854" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
گمرک مهلت تردد خودروهای پلاک خارجی دارای مجوز ورود موقت را تا پایان تیرماه ۱۴۰۵ تمدید کرد
🔹
این تسهیلات شامل خودروهایی است که مجوز ورود موقت آنها تا ۲۹ اسفند ۱۴۰۴ صادر شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/654853" target="_blank">📅 18:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654852">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب‌الله، شهرک‌نشینان صهیونیست را وادار به فرار کرد
🔹
موج شلیک موشک‌های انتقامی حزب‌الله به مناطق شمال فلسطین  اشغالی، سبب فرار صهیونیست‌های مهاجر به پناهگاه‌ها شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654852" target="_blank">📅 18:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjFE8-KDrVvIWUPaZIp5BOBrsT94XUZBcomSsGVPf4vqXYCvH-O5FlJc5KWutoaNJ9SRGxNeSU83yddYSsSZR-s1S2pgQkBzVOMX-EPo_H1_zxbHbCluPominIiSPLmbLV9kSk1HkANHYqRpNbvdpu0aqpPZLBzMArb2BJnQ-2u5YKkVTcSNIsueLqbTOHesy9Sb5tn7O23VEYJDVn6RFXlUkpfeE06hNjKTb4V8q1hr0sfkkFR6gR9smRgM19r-W-7HypoH8RJj6kLQagtVk2jVN40wnsIdTFvVbQ33teH09mvFmUztwSjEukQfucUPp_JEBwPnZdib5n4x_KxzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقلال و تراکتور، نماینده ایران در رقابت‌های آسیایی
🔹
تیم‌های استقلال و تراکتور به عنوان تیم‌های اول و دوم جدول لیگ تا پایان هفته بیست و دوم، به عنوان نمایندگان ایران در لیگ نخبگان آسیا معرفی خواهند شد.
🔹
همچنین تیم سپاهان به عنوان تیم سوم لیگ به عنوان نماینده ایران در لیگ قهرمانان آسیا ۲ معرفی شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/654851" target="_blank">📅 18:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654849">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaYuUHMCaeKFEVe0J33jfSZTW0XPk65P99RQrTYdtMPmiNy7SEW5eigXAqpaAoX-4BikuDQ9Baqiwv85-UIN3hSmRJQpotdwenSRqbfA_1SIfp_5Ks4OeTWfoQ7m0d6-Mmivx45KwOgZ30n7Q4oPaROSgfLY9vSCYEJAjeS25fz_eYXlbryeZwp1syiPlaQTCuPLnFJTg0XbAaW_hG4sXR_00TmZ8WFGLsIc7vmesGQnaBNd6mzEOo-tK_HOGjJJn7HpzZ3AelrtHD2LKQLISA4EWW2OzmQ5y29G_qZiyoOK-moF4wmlueRBOL-dSus2iNEAgKECUdz1GMPV6byFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7s-7_sTtybFZeRNGl0h0LqqR8hyesAdVL34zJ5SaYBJlrlOxoKlIDl4kzU9MR9JVGRpFcu7FH31nH2DVxyyELIdGXIDPhNL8h8G5Vf_pK7bGgQJZ_JszGqjTDE72oZOre1IhV1BzLzrLQ3jPdAxpEY22WVMsyS9pwyLR67n5cmWDBv30hNyMW8sMxdP0_SQU48keHZQwsjafEUvevVO1GX8mhgDXBWIoVWmXa69UDaxWna9v1ntbZqnvSPPPyOhCjOeD4dqaqA16ijm4Y5Y07YEHnqjeAhJw0F2gu4cEPKMCCAnWd_GR6Drw1a8Zed6uKKDxNVva2sfXhvnAyEPAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لونا، شیر ماده که در پارک حیات وحش در کره جنوبی زندگی می‌کند و بخاطر خوشگلی و قیافه منحصر به فردش در دنیا معروف شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654849" target="_blank">📅 18:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654848">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654848" target="_blank">📅 18:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654847">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIqHQ-AfCONHJmQxbpVTg5M1dHk7-N2Lz3e7KRFO_wNvzm5aHA0S1B3x4GbVwLiY7I543B2oHU8r5-Ub9ZVWLx4_eaM9XC_s5_kWYr3s-3cBW27z9zS8m9vzjvJkwQgs2jsvonubKhnDGWipt3dSocbK-emFlQIcVNDam-TOZwHYMrv54ydwAt8AYR6XGQSdLwBWLATnj1ST4zbtl_AnOEdaoKpQJVh1skSsR5hDGQx_uYWLQTFKkYntmotQ7jruxPICiLBdLCtUg5iPsTA8iVVglGOuOQQELaqxHDGOPwjfl4xIFQTCxcYrE9UDIAhxSzh6QUV7EHghWdTz_FyQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرواز همای، خواننده: هزینه تاریخ نخوندن و اینترنشنال دیدنتون برای ایران خیلی گرون تموم شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654847" target="_blank">📅 18:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654846">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سی‌ان‌ان: نقشه رژیم تغییر کرد/ تهران نه، واشنگتن!
سی‌ان‌ان:
🔹
نتانیاهو پشت درهای بسته اذعان کرده اسرائیل نفوذ محدودی بر نتیجه مذاکرات پایان جنگ با ایران دارد. او خواهان حمله به تأسیسات نفتی ایران بوده و کوشنر و ویتکاف را متهم کرده ترامپ را به سمت پایان دادن به خصومت‌ها برده‌اند.
🔹
اسرائیل آن‌قدر روی «تغییر رژیم در ایران» حساب کرده بود که احتمال «تغییرات سیاسی در واشنگتن» را ندید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654846" target="_blank">📅 18:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654845">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجهیز جنگنده‌های سوخو ۳۰ ارمنستان به موشک‌های هدایت‌شونده ایرانی
🔹
به گفته کارشناسان نظامی، در رژه هوایی روز ملی ارمنستان در میدان جمهوری ایروان، جنگنده‌های سوخو-۳۰SM نیروی هوایی ارمنستان با بمب‌های گلایدر (هدایت‌شونده دقیق) ایرانی یاسین پرواز کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654845" target="_blank">📅 17:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان وحشتناک در شهر بیکانر در هند
🔹
طوفان گرد و غبار عظیم، شهر بیکانر در ایالت راجستان در هند را تقریباً در تاریکی فرو برد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654844" target="_blank">📅 17:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این فقط روایتِ حمله به یک کارخانه نیست...!
🔹
روایتِ حمله به قلبِ صنعت فولاد ایران است.
به جایی که هزاران کارگر شریف ، زندگی، نان و آینده‌ی خانواده‌هایشان را در دلِ آتش و فولاد ساخته‌اند.
🔹
وقتی زیرساخت‌های فولاد خوزستان هدف حملات آمریکایی‌صهیونیستی قرار می‌گیرد، فقط آهن و ماشین‌آلات آسیب نمی‌بینند...
بلکه معیشت کارگران، توسعه‌ی کشور و امیدِ یک نسل هدف گرفته می‌شود.
🔹
اما این داستان، داستانِ سقوط نیست...
داستان آنهایی‌ست که از میان دود، از دلِ آوار و از میان خاکسترِ کوره‌ها دوباره می‌ایستند.
کارگرانی که باور دارند:شاید بتوان کارخانه را ویران کرد..اما اراده‌ی ساختن را هرگز.
✅
روابط عمومی شرکت فولاد خوزستان این اثر را به ساحت کلیه کارگران شریف و خستگی ناپذیر صنعت فولاد ایران علی الخصوص همکاران خود در گروه فولاد خوزستان که به حق جانفدای جبهه اقتصادی ایران عزیز هستند، پیشکش می نماید.
🎬
We Rise From Ash
📱
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654843" target="_blank">📅 17:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ده‌ها نظامی اسرائیلی همچنان در امارات هستند
🔹
این نیروها در اوایل ماه مارس برای اداره و حفاظت از سامانه‌های گنبد آهنین که رژیم اسرائیل به این کشور فرستاده بود، اعزام شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/654842" target="_blank">📅 17:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این لابی‌ها مانع ارتباط مطلوب ایران و آمریکا می‌شوند!
🔹
در آمریکا لابی‌های پرقدرتی وجود دارد که اساس سیاست خارجی آنها را شکل می‌دهند. دو لابی به شدت قدرتمند که جنگ با ایران از دل همین‌ها طرح‌ریزی شد.
🔹
کدام لابی‌ها؟ ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/654841" target="_blank">📅 17:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654840">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2ieizoR4qkX9ntX9EthEyh3FxRk8MjhG1V-FMM2Mr56ivoetuTt1s_TLhKUApO6IUzp0cxx-8_ctDR62HcmLga_v0FkvB_GZs_sy3AtAQHL5yMKOH8bYttalKUFbuWhVo-9Ap24zm5vbr1B_Z29AN22XXIg2ob8Psrs8LLvdSA32OqL_tjaB7Us9gabiCY-DLU9O4vflHOURxa9jvBhmSjgVmNF2kIgs47tpSaQQx32Tb-YFwCvEjMxHACoJYtKZQ9f_LkGl1xD4q-eWPTZCZvBIlJ4T7aZNenh4vV5f85eC9Q1cDtbXmvQSCAEQ2kSzpxsaKcv8s_YNH82phecQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۸ درصدی ذخایر نفت جهان
🔹
آمارهای ثبت‌شده حاکی از آن است که ذخایر نفت جهان که در هفته‌های دهم تا دوازدهم سال جاری میلادی در قله حدودی ۲ میلیارد و ۷۸۰ میلیون بشکه قرار داشت، با یک شیب تند و بی‌وقفه در مسیر نزولی قرار گرفته است.
🔹
طی تنها ۱۰ هفته این ذخایر با خروج و مصرف بالغ بر ۲۲۰ میلیون بشکه، به سطح ۲ میلیارد و ۵۶۰ میلیون بشکه سقوط کرده‌اند. دنیا همچنان تشنه نفت است و تقاضای فزاینده جهانی برای جبران کمبود عرضه، با سرعت در حال بلعیدن ذخایر روی خشکی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654840" target="_blank">📅 17:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654839">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
با اعلام سازمان لیگ: باشگاه‌ها براساس جدول لیگ به آسیا معرفی می شوند
مدیرعامل پرسپولیس تا ریاست جمهوری هم رفت! اما پرسپولیس به آسیا نمی‌رود
دبیر سازمان لیگ:
🔹
ادامه مسابقات ممکن نبود، طبق قانون و عرف به جدول ثابت شده رجوع کردیم.
· پیمان حدادی، مدیرعامل پرسپولیس، تا نهاد ریاست جمهوری هم برای دفاع از حقوق باشگاه پیش رفت و با انتخاب پیشکسوتانی مثل محسن خلیلی، برای حفظ جایگاه باشگاه تلاش زیادی کرد.
🔹
اما پرسپولیس در رتبه ششم است، بنابراین نمی‌تواند به آسیا برود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/654839" target="_blank">📅 17:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654838">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvIJlxVSwv-XIaaZXq-hZiAiVnqSbJk-U3jbNuUQqBa-rpVtGTwKH7E0OYxTuMbKPoPRpUYoFjP90zmmMEDJ--gzhqF20cUjGgAZ7vpd0VBOdul54tyboR1L32RkeTlHJ4E9EGAeSjYTsEeabjXLakodjg5NQFfxaGRGrEgy-5lwYag8J4EnNH22pmVrIO_Vqmu5Pb35FKb50wC-vgzU0mTscUjKfsly_rTj4Npg1WGlDXipIk5Fa05ZtXSDYqUASm2RfbSiLzTa9SGw1nsJP6h1p1WQy8cXd5r_S_Kd5jNZWQkgrfyOdh67IVCEREuBiVhTCQAvQxtkr7YnRsYICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن با دلار ارزانتر از ۹ سال پیش شد
🔹
میانگین نرخ دلاری هر متر مسکن در تهران از ابتدای سال ۱۴۰۵ به حدود ۱۱۰۰ دلار رسیده است. این شاخص از ابتدای سال ۱۳۹۵ حدود ۱۱۹۰ دلار بود. یعنی مسکن امروز به دلار آزاد، از ۹ سال پیش هم ارزانتر شده است.
🔹
در شرایط تورم شدید، مسکن همیشه پناهگاه امن سرمایه بوده و این تقاضای اضافی می‌تواند قیمت دلاری را بالا ببرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654838" target="_blank">📅 17:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654837">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIFmuRuTpcFoR0jmISQtBDmxZoo2F6jlfidcMNsta_LQENhopTsTWV7BI_rMsSW7EnqJqt4eJ-j8y2FcN8UzIXaqiH6Gd2Sz8vcnTcmgegLG3mWock96x7ZNFAFBaHIbmHgA56Af_sC5UN_HFYcYbFT9Kr9a5TwKZ11tEttXZ1OfUCCm6gD192f2StJ4slLW_U3wvmtnKBZU_VJ3fWCOB9bOCQTbjR1l93G8w2Q--szGSHZDLG0kJSg3HtN_mHvgz3RIvQ3V4iTpmI-81WeqT1Cvma1bl7dSc_7IUhJRgtY6PbCZmb7W9tIy2Y4bb2pTOdJDWf2tfkY425t0KFzX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین نقشه از وضعیت جنوب لبنان پس از تحولات نظامی اخیر
اسرائیل
🔹
زرد:
منطقه تحت کنترل ارتش اسرائیل در چارچوب خط زرد
🔹
قرمز:
منطقه‌ای که ارتش اسرائیل پس از آتش‌بس به تصرف درآورده است
🔹
نارنجی:
منطقه‌ای که تحت تهدید و حملات ارتش اسرائیل است اما نیروهای زمینی به آن نرسیده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654837" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654836">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در کشور آنفلوآنزا شیوع پیدا کرده؟
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
شیوع علائم عفونت‌های تنفسی تا ۲ خرداد در مراجعین سرپایی ۵٪ و در بستری‌ها ۷٪ گزارش شده است.
🔹
در میان افراد دارای علائم تنفسی، حدود ۸٪ مبتلا به آنفلوانزا هستند و ویروس غالب در گردش آنفلوانزای نوع B است.
🔹
طبق داده‌های نظام مراقبت، آنفلوانزای نوع B در گردش شدت یا تابلوی بالینی غیرطبیعی نسبت به حالت مورد انتظار ندارد.
🔹
برخلاف پیک قبلی که نوع A بیشتر کودکان را درگیر کرده بود، این بار درگیری بیشتر در بزرگسالان دیده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/654836" target="_blank">📅 17:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654835">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk3UWEMad2Wsx1iwhNv_x4rdpSAfjNPdskxktav8sVZB6OGMpJhUjqorkZPtTcQTYSvZjsMVhgbJ-mggh4XnhUh-Ti_Xg9TQgvHdpWfXCGXYqR5jMCxpoV1kWlzbtBlle74TJFeUaS8Zq76QU-lasLlU4R-svGjEaCtuAUVubFzhyJoCGJMcv8z1R_755MEU71wQgVwSZcoUT2q95E1mRHRB4B7KNGO52ndebHB_PmWexonUZZF63J-5_egg5ls4155K5Os_Qm2n-5I2dMU5XlmngJamKeaAL1Eb3c06dfyL3-zKp546I-gAHtf9aBzlg3tpQMgWzw06AtkrIE78jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمان از مشاهدۀ یک مین دریایی در غرب تنگۀ هرمز خبر داد
مرکز امنیت دریایی عمان:
🔹
درپی مشاهده یک شیء شناور مشکوک به مین دریایی در غرب مسیر تردد ساحلی کشتی‌ها در تنگۀ هرمز و در آب‌های سرزمینی عمان، از تمامی دریانوردان، ماهیگیران و شناورها درخواست می‌شود با نهایت احتیاط در این منطقه تردد کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654835" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654834">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گندم ایرانی قاچاق شد
یک منبع آگاه:
🔹
گندم کشاورزان در بازار عراق به قیمت کیلویی ۸۰ هزار تومان فروخته می‌شود؛ یعنی ۳۲ هزار تومان بالاتر از نرخ تضمینی. این اتفاق در شرایطی رخ داده که کشاورزان از فروردین‌ماه تاکنون ۱.۸ میلیون تن گندم را به سیلوهای دولتی تحویل داده‌اند، اما به گفته آن‌ها هنوز ریالی دریافت نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654834" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654833">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
افشاگری تازه بلومبرگ از تلفات نیروهای آمریکا در حمله اخیر ایران
بلومبرگ:
🔹
در جریان حمله اخیر ایران به یک پایگاه نظامی در کویت که در واکنش به نقض آتش‌بس از سوی نیروهای آمریکا صورت گرفت، چند نظامی آمریکایی زخمی شدند و ۲ فروند پهپاد ام‌کیو ۹ ریپر نیز آسیب دید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654833" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654832">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAo_RITspVZg0pvwNkJoMutn1sFMUk9dkCibkYpXI1zxffQurNKQyRi4hgnlfkVH9tBu1gNoIcmyGeQnsfIo7ERPJQAbwdKW9vHRX_MuDKpp8h6ILLpmMB3uyEHVy6UR0s5Bh9vdOXpds5W51Y3Z-j5pyJQZlPwOe1EIBrVOGJ4eaDN0a41xyx5Q44Ru-UOeX8xSFQklLFzci0GPz5AEejIXjAJoosgcOsKLR8d4qnYaSFcWFgOqDYRm6RCaFOE6IfeylcgNhwAijmfxvR0SnJTFdabfElygIhKwCdBXX466pNMKW16gcxTQ-gWOeRb3mN11rp-0XVgbF1Bzht-1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس امروز همه را حیرت‌زده کرد!
🔹
بازار سهام امروز صحنه یک حمله همه جانبه تمام سبز بود. ۹۹ درصد نمادها در دامنه مثبت بسته شدند و ارزش صفوف خرید در دقایق پایانی به ۲۷ همت رسید.
🔹
شاخص کل بورس با جهشی خیره کننده ۸۰ هزار واحدی در ارتفاع ۴ میلیون و ۱۵۳ هزار واحد قرار گرفت.
🔹
حقیقی‌ها هم امروز ۲.۶ همت از صندوق‌های درآمد ثابت خارج کردند و ۴.۹ همت نقدینگی تازه به بازار تزریق کردند. ارزش کل معاملات خرد نیز از مرز ۹ همت عبور کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654832" target="_blank">📅 16:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654831">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7856964316.mp4?token=oIINE-586bILRQUIKd-BhECpWQa3MczG0mAdaGczdRmTNMxCJHp4FVpI4kas2xUlfTJ_EnHUhGQY3A0-angI65_Ev0D6rI_hc2VarK2UPhF3_Z8XtgDkvJsF5buvbKOBtFvMAIFiYhR9X3scDg7Si3RZyiQEjMpSFt3QXxLZl7c_PkfXAwizYUQqS3DrWeZoLadIAyt5P30_CrXxw6pPUX-buJ1le-URFaWG_TjAKjcbfVe5jWRSRE86lrSiqttTYzag0UZSJ4eh7MkW9mNQh-JCKLGqrta2glhp3ieyEvjTRwAeC7k65sXudQXbcEeNtfLp3NWMEGPOXeMWjJxsH7DJOm5NEyJc52gyn9h-qDPQHuuQ2VVmw5KF5orU22jr-OurfwobB3OfwIc8SGHkGeyAtThIFO3FNuhP9jv1vE7k7Kw10-y8Y8ZdPuhP4nxerWEb_bgxr-x18T25ZJ_EZTOadJoPIdiQy0JL04L5ETJfQ-sIsJzll5BIp5Qy7texfwEUwhaJ-sN9aoYVzYWWW63o1uCWEbDs3Th4RHzieOvZTZlLAiHC_aGwGe4xSVnygnOfMD1Yso-07QCEUNVyK3NF-dNUglM-Et1OppbOswgol-2gpFDXU_QIQCxkqXDiVwyWsGYixAxGlcorZmzFdSo6VGNyvX1q18NJAL9H6YU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7856964316.mp4?token=oIINE-586bILRQUIKd-BhECpWQa3MczG0mAdaGczdRmTNMxCJHp4FVpI4kas2xUlfTJ_EnHUhGQY3A0-angI65_Ev0D6rI_hc2VarK2UPhF3_Z8XtgDkvJsF5buvbKOBtFvMAIFiYhR9X3scDg7Si3RZyiQEjMpSFt3QXxLZl7c_PkfXAwizYUQqS3DrWeZoLadIAyt5P30_CrXxw6pPUX-buJ1le-URFaWG_TjAKjcbfVe5jWRSRE86lrSiqttTYzag0UZSJ4eh7MkW9mNQh-JCKLGqrta2glhp3ieyEvjTRwAeC7k65sXudQXbcEeNtfLp3NWMEGPOXeMWjJxsH7DJOm5NEyJc52gyn9h-qDPQHuuQ2VVmw5KF5orU22jr-OurfwobB3OfwIc8SGHkGeyAtThIFO3FNuhP9jv1vE7k7Kw10-y8Y8ZdPuhP4nxerWEb_bgxr-x18T25ZJ_EZTOadJoPIdiQy0JL04L5ETJfQ-sIsJzll5BIp5Qy7texfwEUwhaJ-sN9aoYVzYWWW63o1uCWEbDs3Th4RHzieOvZTZlLAiHC_aGwGe4xSVnygnOfMD1Yso-07QCEUNVyK3NF-dNUglM-Et1OppbOswgol-2gpFDXU_QIQCxkqXDiVwyWsGYixAxGlcorZmzFdSo6VGNyvX1q18NJAL9H6YU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر سابق سازمان سیا(CIA): انتقام حق ایران است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/654831" target="_blank">📅 16:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654830">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czQSmFgf_zNWF0V-ImLcXzZbmKwERAJft35pkTMVIZzF9gp9wLyt9tS-0PzbyvjZmBgj56s76yC3JjR3_Nc4b87u2e3hrriU3DamUkZae6F-hg3CQAf4rhA-TmnYxe9dW6p-f5p7HqwRgeuifwmPdMThj9XGcUX4p_sV3_sQi27t2DwFX-wWahWZ40d13hxa4aRzbiIAWVChK39Ncc4AQhzqi5KhT9VJ1jma2XWSdjriozq60urtcHoag9ikaR6jonR64Pv1H0biPdF78aY7Y-vp3CnTbkjuU7oaBk4eBCGUgDVfMxXxBI9BQ0tbPPMA2vswNmwjT7zLFHbeXsxGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند خبر کوتاه از دنیای تکنولوژی #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654830" target="_blank">📅 16:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654829">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxFXGErHjrkagnfdXQzSvev7UPcwqzP6IolDw3YFpqML9uvRj8LrzBrXMmu-h9yvkJT_VnbVeltxuK8U8yiwRtQDOU4_U_fwFyC8rFLKNkMk_4uED2ZXLbIk06kTul2iE0TZS0mVV6bEVImbH6ByTaiO6ChSzvazmjXxfLQOsH_Hd4-hdYqVkEmki8t-Cynrt3VBWfgyWP6pejE22_FcXc-hLrtOmWzjD_MKnwdHZxMZOkZ48A9kkHVcw49u80ZOdT7Va4nTFEZxzpO-vAFJDqpwuSJ4QaFTHhsir2b-7RFN3ITLotTw-xn9T7E-adPp3CIO1vwaWMltp8I8axYyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف نام یک بازیگر از پلتفرم بدلیل وطن پرستی!
آرمان درویش نوشت:
🔹
«حذف نام از پلتفرم مهم نیست، باید در یاد مردم بمانیم …تا ابد برای ایران»
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654829" target="_blank">📅 16:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رجبی مشهدی: مشترکان خانگی که مصرف خود را در مقایسه با دوره مشابه سال قبل حداقل ۱۰ درصد کاهش دهند مشمول تخفیف تا ۳۰ درصد در بهای قبض‌های برق‌شان می‌شوند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/654828" target="_blank">📅 16:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5hLjqHB13yhSi97CtENgr2PBfrhTgJiapI0i-IwZuGg2kKcbcTLE-h3S5-NmobJz28VLG1kYuRZWyLJWycEmpbfwNhzpY2U0DL6JoSbZfvvHvafklDU9g6rReKldiGwLew-SVEcM3TLxDF-7L2ibGTKt2Pp35F0Yz2LpCLM9JAynXqsdGVoOAyUYgh-fE6CERcLEwLeglJlbx4LxNnZQxsQRKRZIjcdSMwnnG-emVgQtVEly0mZtMYITYQewnbGCMcEVCYpLYAqJpqspmvSyzO5sLLsW83HzjewUGNO-A-gUwBeSOYSMLLH6hKlFauDRZmyksUCMljiZVM_AmmDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNlDD9DWbpBTtz6CijNE9xFJ7oRVrDgugIakC4xK8yyMye8wYyI_Q7tfQxEbOS3Qyy6-UtCprHn-UxTuqgTV6ZIg4pyUcRSAhPLPi4LkPImTW04_WVmqhTAYgRiRN77MCcmFybxoIdbSCCMAU764KKPSwY_9DsPmDfSJ2wZUwpWqvnX-J5jLIDSo37JruBnkmRWOtLpKCWl6QQwtkrmbpLqJo5hgelQup3h2MZVIDcNlCUsY_GADwSDqzipIG-LsEE3J7Fstk4taSJMSRHghHQSxlR7zlxtrdsYzGThT5jKEwl1EgtOPUnPC76e5XifIpSGP_J3SLcT1hD_JBZF-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSiVFutNONm__K6Bf-YGF1HEQjUiAS_jR7D_CdLuytr5R53NHy-zCevSZEWQzx7lJ8lmHpdth45mN19ptpojbn1ZxU9N5ZPjkP9K8uzeMWqsPr9u3jMc0F93eN5Ilqw5mB2y_4zcFNVsIPRKR1uDDVfDbRyThZT4sY7FWnqoSFII9TUMajVm5s2vxf1iSZOEL1U_qzrrfbsudH05CFg4oVwoaylO8hGUUgKMrtoSaxZz9eoi3fe8G4VqsPHmTiu6tYtKBA1VLV1AWYsnEH6EdTl7-F9fPNlXyQLP4s2pw0rN-s-nIbh5RSor-T1d6pCGke-0WDN1AqPMpkg71PnYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUZvZaH8zRxrfLEPddHILOaPHcCIIAaIGMf2y9XgkeDARw6_dR27ZRJdIfm6b3xNzM2Oglrd056aDOk7iRkQP31pMXUh2De6qqV4Qa7z5bewH5TKz_kI-NBebiC2WH0EubOUIQ4KRp_GG9JdPXBtb-5fcUIoVcCpPcKq2uCaf5R2cRkcG7ApHQU-XSXKRVBrqvxDkXEGHtSVrLl_3g4IGsVjU1VE7mMr4HxNqrgO1p_5xjV1CK92KWAGP5Opr5H4mtTwAtniCcdWXBHwzRNOe_w0WODGPYEW5_joM-_JRsqqWTlZqcoIiKeHw87ADVndlzfgUMjTh-aJmVUm39aX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PG0dB1QM7OI3YU3MDRMvY00lrJjDBSZ0kOX5WLxkPfhhjGllzo6khx-HpvuDirjlJ_CMpfkOBlCJiKYRIa-8itTNSIQv79Ih5FmiCgm7UlfZhhepSXVFqnNGu5R4gn6YUz5nhZoEa_zQD5FWfjHDoLWRa-lYluAohDM-W6um99fLsaV0rd0u7jykqOUeCX7Sc2cMBjwfskRNPXL3AEq8QD9lmfqAtpkzYj4xFVoa9Ya90YVMB3bHdzJVdNstQTKlXNhwPBtIYaMcpD8xjBpc48DilsYyxrp_8hoB0TOZ2hwe4ztaz4QrF507JRL4sGL2fA4T1Ir4LrQWJcQFiPagrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی‌هایی تکان‌دهنده از آینده بازار طلا و نفت
🔹
بانک‌ها و موسسات اقتصادی مطرح آخرین برآوردها و پیش‌بینی‌های خود را از بازار طلای زرد و سیاه اعلام کردن.
🔹
این پیش‌بینی‌ها را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/654823" target="_blank">📅 16:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/637b15c089.mp4?token=I0sxb0viwJqUM-Ogl34DoMm7eS8q5IMRyWMwQIbMq1tUaAnvK_6obEtmjw_Wi91gHDgov0v0CusrsK8YaIP6nR_necQKwD_REf0nS9Iq-qcgrKV_0LqweEzzBRuMnlZAny8l6UNm55jqSiVE--Kwo-otlsdB2mmYNLAywxG52AT0LrjEQykh_f04GLQeyjZXvKIy9ZttPZGQgrd9SctBDzdvam_mnGaO9GDxEs70Tcm9CADV4_reCf4iduIju9jCfS0ZxtGHTl3XI4RLqRB4pijIjbGnfsH80rsKyK4qYZxJNlXCwUamzUJZgT42f1RPlJzE7OvtBhlyD2yTJ_SUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/637b15c089.mp4?token=I0sxb0viwJqUM-Ogl34DoMm7eS8q5IMRyWMwQIbMq1tUaAnvK_6obEtmjw_Wi91gHDgov0v0CusrsK8YaIP6nR_necQKwD_REf0nS9Iq-qcgrKV_0LqweEzzBRuMnlZAny8l6UNm55jqSiVE--Kwo-otlsdB2mmYNLAywxG52AT0LrjEQykh_f04GLQeyjZXvKIy9ZttPZGQgrd9SctBDzdvam_mnGaO9GDxEs70Tcm9CADV4_reCf4iduIju9jCfS0ZxtGHTl3XI4RLqRB4pijIjbGnfsH80rsKyK4qYZxJNlXCwUamzUJZgT42f1RPlJzE7OvtBhlyD2yTJ_SUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست، وزیرجنگ آمریکا مدعی شد: محاصره دریایی ایران همچنان به قوت خود باقی است
🔹
ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654822" target="_blank">📅 16:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfeQcZx0Vtr5jNaNv_v_omyoe4C4dk8C_vU0oHLdMAn9O5Gl1w9JO5S0ElUu4dTzu9iTvTov3pXSmYKTvEDomwOKVd-_AF37Cc_3wbqrICyXu6I2xPiY2szloHgMH5yA8b_5Bn1quXN7-_5N6ThG-nVbym-wmDH6xmrz0fVcypwYES0u02vwElyaiOREruW80u3CUp_E9IN0OzVMIsn2OBm4VmD8gxXHbULHJE41R4RKooWsCjJtVsRqpeevxA8hL4I7FdoVwjS_ALq-sKAMD43scs6GwbZG0fAVT06RqODkLpdku-QsZw7nwUND7CsSdWFpkhtzhrg2LPoGYJKAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: یک چهارم نفتکش‌ها مخفیانه از خلیج‌فارس فرار کردند
بلومبرگ:
🔹
تقریباً یک چهارم نفتکش‌های بزرگ غیرایرانی که در آغاز جنگ ایران در خلیج‌ فارس گرفتار شده بودند، توانسته‌اند به آرامی و مخفیانه از خلیج فارس خارج شوند.
🔹
۲۹ کشتی از ۱۰۹ کشتی بزرگتر، که قادر به حمل ۷۰۰۰۰۰ بشکه یا بیشتر هستند و هنگام بسته شدن تنگه هرمز پس از آغاز درگیری در ۲۸ فوریه، سرگردان بودند، اکنون از این گلوگاه عبور کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654821" target="_blank">📅 16:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6b4dc58f.mp4?token=HZPTx_KLrw1be8A3W-Bid_YLIONDW1D-4VQOWaF8vkA9DARZh3aATK-1B0lPFHVZ-CLq39bOkzUsFXAdhi6DuODRBtU7wwrMirl0cupPJ_XfSfP9_SfxmrKqqaIdMxLtVg8V5itAczAyXwduyh1cDin68szTlKUQTGPm3IRNvN7ohmJSPpGlTPVKkt5ojG1Qav6RPKKFyp5YhBFJ1EAiOKOxrqhOP7U9fFfY6GHRvsRQNfiWR_CCSyWGdsuBu-b0rF0-Clc-FaMhw6dxyzRu8xsXoN5YlzzVDHug-EMcZ96fRoxPHb4WO6XFOfCxPr379TMPhGpa7xhsIhIW13XTFEsw48bNfGeS6xINYvhAoMdfbiBqVPPRNjV0RAwJuQy768goMapIrBwxuaPIqlhi5naO2lWXtXiGG2U9sBXS1-_Hb7F8ObkwT9dj8e09MKq6-3vM4sJGXIVORB2BJxrFlxJF7aKx9Dx5qy3nyIzclmOjnqc5XFtbsmcoYMCGKmwsolU_FWNordPHyUwDkyR0zVZ2JJEi001qFpEDd0MjtDfh1zL9KrloycPT7BpaDhTPfcqESBFvks-A3vQ0qJ_lplDw4wcbFBaaKQ_xXAbz-cK2R18latYcBsynN5Dr-RU7wZhwutERmpdg3mKPnLjv_Axp-YbHF0LmFh4SYWpj1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6b4dc58f.mp4?token=HZPTx_KLrw1be8A3W-Bid_YLIONDW1D-4VQOWaF8vkA9DARZh3aATK-1B0lPFHVZ-CLq39bOkzUsFXAdhi6DuODRBtU7wwrMirl0cupPJ_XfSfP9_SfxmrKqqaIdMxLtVg8V5itAczAyXwduyh1cDin68szTlKUQTGPm3IRNvN7ohmJSPpGlTPVKkt5ojG1Qav6RPKKFyp5YhBFJ1EAiOKOxrqhOP7U9fFfY6GHRvsRQNfiWR_CCSyWGdsuBu-b0rF0-Clc-FaMhw6dxyzRu8xsXoN5YlzzVDHug-EMcZ96fRoxPHb4WO6XFOfCxPr379TMPhGpa7xhsIhIW13XTFEsw48bNfGeS6xINYvhAoMdfbiBqVPPRNjV0RAwJuQy768goMapIrBwxuaPIqlhi5naO2lWXtXiGG2U9sBXS1-_Hb7F8ObkwT9dj8e09MKq6-3vM4sJGXIVORB2BJxrFlxJF7aKx9Dx5qy3nyIzclmOjnqc5XFtbsmcoYMCGKmwsolU_FWNordPHyUwDkyR0zVZ2JJEi001qFpEDd0MjtDfh1zL9KrloycPT7BpaDhTPfcqESBFvks-A3vQ0qJ_lplDw4wcbFBaaKQ_xXAbz-cK2R18latYcBsynN5Dr-RU7wZhwutERmpdg3mKPnLjv_Axp-YbHF0LmFh4SYWpj1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد مرموز رسانه‌های اسرائیل؛ باراک راوید کیست؟
🔹
چرا او از تمام خبرهای محرمانه و پشت‌پرده‌های مذاکرات ایران و آمریکا خبر دارد؟
🔹
درباره باراک راوید در این ویدئو اطلاعات شگفت‌انگیزی خواهید شنید
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/654820" target="_blank">📅 15:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4bd69983.mp4?token=ZTCjEUGehuOKoqt4M389aosU4VNhWbaP3YXhVVIfsDnTKZ7QESQDPiCDdhVZXckvWeO_tw3BKVhC5syHQ6MQFLIehd7afiI8Inr35NaLQfu5y1m5lH3yD0kzkwBrdlRMz5BOpl88wIBdlMrPDwfTGXKvvAkCbxks8XZuzWynf-nGieLxH9p3s09EUX9gJq2OK2pLB1wA3F5uEE_RHsKVZISQHnZnVF2JR4RHYicQ3V91Y07jV851BFzTHFkgWnDC0ucjL-8sOY3nuW6Ea_1XAjEEsZe8549WoCwl_ubaowYJrUR2Y_B6Pj-A3M9vcvBa-_Zmzbp5A8qi7XLGLTgHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4bd69983.mp4?token=ZTCjEUGehuOKoqt4M389aosU4VNhWbaP3YXhVVIfsDnTKZ7QESQDPiCDdhVZXckvWeO_tw3BKVhC5syHQ6MQFLIehd7afiI8Inr35NaLQfu5y1m5lH3yD0kzkwBrdlRMz5BOpl88wIBdlMrPDwfTGXKvvAkCbxks8XZuzWynf-nGieLxH9p3s09EUX9gJq2OK2pLB1wA3F5uEE_RHsKVZISQHnZnVF2JR4RHYicQ3V91Y07jV851BFzTHFkgWnDC0ucjL-8sOY3nuW6Ea_1XAjEEsZe8549WoCwl_ubaowYJrUR2Y_B6Pj-A3M9vcvBa-_Zmzbp5A8qi7XLGLTgHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش دوم تجهیزات پزشکی هم به بندر ماهشهر رسید
🔹
در فاصله یک روز پس از ورود بخش اول، دومین پارت از تجهیزات پزشکی مورد نیاز بیمارستان‌های بندر ماهشهر و بندر امام خمینی(ره) اهدایی پتروشیمی امیرکبیر وارد این شهر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654819" target="_blank">📅 15:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2YtI-zj6sDybB6Y--4zKWQRQ_lhvsChhxJyhlYpFbMvmFjAq334FXq1MU59Pc_ir6B1x_CpcxZ4gCxNYaW4mWWWvMNuMnMYmtkqw9DQu_rXKJKslXpdx1DBz5ol1--98_6AQKSrWDG3aAPFUGJ5KBI9xa5XXIXhE6o5fNk1n-qrouJmhkvsN5IqgKlfjJ8M6qZaei32Rbp-0RBQ_D2SAWhxglcQ0T8PFzSeg0dDc5r6HrW-J1hiKDE3X5c400vwRA3c4WdJ8feYQDowFJOSZPAmfOpK_E_QSjPJb8sKu2VxEESyO54lww720iZNxQJ7jSPjXzcmUfUR0MaCRf4RwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفحه‌اول وبگاه روزنامه اسرائیلی: آمریکا تازه دارد می‌فهمد که ما در موضوع ایران سرش کلاه گذاشتیم
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654818" target="_blank">📅 15:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
رجبی مشهدی: مشترکان خانگی که مصرف خود را در مقایسه با دوره مشابه سال قبل حداقل ۱۰ درصد کاهش دهند مشمول تخفیف تا ۳۰ درصد در بهای قبض‌های برق‌شان می‌شوند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654817" target="_blank">📅 15:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654816">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV_gqrH9ezcXA40acz-k1yqm0HIC1JLLSSQJsLRL5LCpFpacQ6jc_2bwAabPCVbaNOOV6v9AhY7OcR2gSgNCl1rUAudSkVYuxC0Dkj_9iLVDmiffBQaXux_59Pv9UkKaaJ4EfhbPMixp_Ko5SybDKhvdgVC_kC7gIL4Ad58k9uCnW302L1hs2LLKwRWib-qIRl1AjYlc-Sr8BirNCijRXZsoE3WpYlnAj9cvtQtFL3ZROZSQf0NT49yk4grQJ6Vs_nzZDK_NQi2RVBYG8vWb9jrDdx_3x0VEUdRufqG_JQvI1gvmBlcoX5SE0RGdNnJe9ujLXUCxvwIxr6gk5S5nsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ جدید ایران و آمریکا در این زمان آغاز خواهد شد
🔹
توافق موقت می تواند به ترامپ زمان لازم را برای آرام کردن اوضاع در آمریکا بدهد. او همچنین، می تواند با خیال راحت به دیگر مسائل خارجی مورد علاقه اش مانند جنگ در کوبا و مساله چین و تایوان بپردازد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3218694</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654816" target="_blank">📅 15:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654815">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edac40a70.mp4?token=tpnb_f92SKGwW6uinCkbW56GQ4Z13ybN4nUzyBp3awv1cUMLfK7AgjhU1alUJD0qG-bj2eWnjLEjcGo75d0YPjVfGP1-5hAmEGQH4EmGm2xXGhlpXZ6rfiS6bYmpP47DpBqesANDGzeOqsXQ0JOHFdH3v8Dcp_fr3_jpazGVIdpNPtxYp2Ba_tgnHsxPWX9N3ncdiCASS1i6y-XcM_13aQAkwMwxupUgDBMiKlwPvL_z1Ri8-QtsbWgTqCamdGAanRE-LjW8R4f2clIMQK5xq1Y9IVJX8yITQjpxMUhkBS7AZr2A9st92iC-4H1pEQPpQ-Ir5ZB-Eb4i_8AnT65Fnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edac40a70.mp4?token=tpnb_f92SKGwW6uinCkbW56GQ4Z13ybN4nUzyBp3awv1cUMLfK7AgjhU1alUJD0qG-bj2eWnjLEjcGo75d0YPjVfGP1-5hAmEGQH4EmGm2xXGhlpXZ6rfiS6bYmpP47DpBqesANDGzeOqsXQ0JOHFdH3v8Dcp_fr3_jpazGVIdpNPtxYp2Ba_tgnHsxPWX9N3ncdiCASS1i6y-XcM_13aQAkwMwxupUgDBMiKlwPvL_z1Ri8-QtsbWgTqCamdGAanRE-LjW8R4f2clIMQK5xq1Y9IVJX8yITQjpxMUhkBS7AZr2A9st92iC-4H1pEQPpQ-Ir5ZB-Eb4i_8AnT65Fnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنجره نما؛ ترفند جدید دکور برای دیوار خالی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/654815" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مخالفت شهید لاریجانی با راه‌اندازی موسسه و بنیاد حفظ آثار با بودجه دولتی و بیت‌المال
محمدرضا لاریجانی، فرزند شهید لاریجانی:
🔹
شهید دکتر علی لاریجانی در زمان حیات مبارک خود مکرراً نسبت به تاسیس بنیاد و یا موسسه و از این قبیل که وابسته به بودجه‌ی بیت المال باشد نهی می‌کردند.
🔹
فلذا هرگونه اقدام در این راستا مورد تایید آن شهید سعید و خانواده‌ی ایشان نمی‌باشد.
🔹
اما در خصوص کیفیت حفظ و نشر میراث فکری و عملی بنده‌ی خدا، شهید دکتر علی لاریجانی جمعی از همراهان و دوستان شهیدان لاریجانی در سازوکاری عاری از بودجه‌ و یا حمایت دولتی در حال پیگیری امور می‌باشند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654814" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654813">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKYi5S2R2DAbcf71xmCmh5HvvBA525HmlHQYLGz0wvnt6bgpWOczmw8sk3GIYhjT0yhkY5AET0Q02uzRvmhX_ZSqFu4ArVJbLuqcG8cXodX-5l2cUu1NcwS2g0IuZztZjooXm84Vmt70Od5fgAxb66H1nuV71VVFIgWQ61QYqFMRUIfI7CQ39O16gUmmHMVo2MV6Vyeg-7g36JOxI3pjCTJqjG_utMOm-KbujOG3dGEISkxF4W1P9CjBW1BSGA1yKIjce4Y9gWc9EnTefdnMuXVuRTRPMxPG7_U79Y3Qa3qcsuMhBhF33MnB6QR6sDf8zn88C5oGyNmobxEVrPhPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سومین نقره دختران دوومیدانی ایران در قهرمانی آسیا
🔹
در ادامه بیست‌ودومین دوره مسابقات دوومیدانی قهرمانی جوانان آسیا، هانیه شه‌پری در سومین روز از این مسابقات به مدال نقره دوی ۳۰۰۰ متر رسید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654813" target="_blank">📅 15:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گروسی: ما با ایران گفتگوی حداقلی داریم
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔹
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/654812" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/194d328b0d.mp4?token=pucj_2fbN_e4YfT2FXTguiv1CSrJFJc8ndmbC76UFUikzfxEt8D7IA875AQDdPL08uR5i_aLKnEfoFVsAGxdLpDxBTZeZF6AKmGmW1dJOL7RTCQbLKAOlGE0WAm48rKiEcjy8xf21VEIDWDCP3TyHR13x6Z20COIAE_2J9dq_QZwmYh1bbTC8J95JlXKxFrIkZ6UIj5HDDMJ3-h6BP5k94U88rhkbXC-b-EU7K3NSkPD8_SuCcPF-XLchm2_AyboDh6F33NFT3Ow2UHq5Jha7Br5q1wyv6aPeHxZfIHqg6TQKtS3pw8DU66457AYUFey5CT115glwfuvKxt7zQyhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/194d328b0d.mp4?token=pucj_2fbN_e4YfT2FXTguiv1CSrJFJc8ndmbC76UFUikzfxEt8D7IA875AQDdPL08uR5i_aLKnEfoFVsAGxdLpDxBTZeZF6AKmGmW1dJOL7RTCQbLKAOlGE0WAm48rKiEcjy8xf21VEIDWDCP3TyHR13x6Z20COIAE_2J9dq_QZwmYh1bbTC8J95JlXKxFrIkZ6UIj5HDDMJ3-h6BP5k94U88rhkbXC-b-EU7K3NSkPD8_SuCcPF-XLchm2_AyboDh6F33NFT3Ow2UHq5Jha7Br5q1wyv6aPeHxZfIHqg6TQKtS3pw8DU66457AYUFey5CT115glwfuvKxt7zQyhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مناظره جنجالی درباره نقش حوادث ۱۸ و ۱۹ دی در تحقق جنگ ایران و اسرائیل
🔹
سعید آجورلو، استاد دانشگاه: ۱۸ و ۱۹ دی باعث شد که ترامپ بگوید حالا وقت حمله است. گفتند در جنگ ۱۲ روزه آسمان داشتیم و زمین نداشتیم؛ این نوبت از زمین شروع کنیم و بعد از آسمان بیایم، اما معکوس شد. در آمریکا جنبش «نه به پادشاه» راه افتاد و در ایران مردم برای حمایت از دفاع ملی به خیابان آمدند. اشتباهات اقتصادی و اجتماعی بود، اما توییت ترامپ که «نجات در راه است» یا فراخوان پهلوی، زمینه‌ساز حمله بود. مشخص شد سمت دیگر سلطنت‌طلبی، تجزیه ایران است.
🔹
شهرام اتفاق، فعال اپوزیسیون: مطالبات مردم با رایزنی در بالا، یا جنبش کف خیابان، یا از جنگ میسر می‌شود! من موافق گرفتن کلانتری نیستم و نمی‌دونم چه کسی آتش زده است! جنبش اجتماعی باید عاری از خشونت باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654811" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8027339a.mp4?token=FfDCY2VcmoELROx0Tjbk3Wid7baOHJD1cwaV19AKK3dvhLKxW2xRDODhxeBtz6_hwlZUiJDG-KwPrGsQ2exm63Z-qHHnGS1jWe_SoWSA6xNdjX_dMZdye0TZgMYnOKwZLbJLDLALLEQlfOYYMJ_ai8gZQ82QlYa2ElBzu6G2iKgvZhrYPYJBrJdqUSn6u_bNDiXQwTGLvyB6rs-TeF_MAe26AOeQ3MXq-LU4kaKM1e7IA9Zy6ydoyOKBCR549_MWLsBZDhilci4bIB9t3SC7HI9DrUDexYO_zYWqCXlCl3c5RGMdtmiJlIUQeKTPXwBd19RrHbfAG7519FWAMuXGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8027339a.mp4?token=FfDCY2VcmoELROx0Tjbk3Wid7baOHJD1cwaV19AKK3dvhLKxW2xRDODhxeBtz6_hwlZUiJDG-KwPrGsQ2exm63Z-qHHnGS1jWe_SoWSA6xNdjX_dMZdye0TZgMYnOKwZLbJLDLALLEQlfOYYMJ_ai8gZQ82QlYa2ElBzu6G2iKgvZhrYPYJBrJdqUSn6u_bNDiXQwTGLvyB6rs-TeF_MAe26AOeQ3MXq-LU4kaKM1e7IA9Zy6ydoyOKBCR549_MWLsBZDhilci4bIB9t3SC7HI9DrUDexYO_zYWqCXlCl3c5RGMdtmiJlIUQeKTPXwBd19RrHbfAG7519FWAMuXGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست، وزیرجنگ آمریکا مدعی شد: محاصره دریایی ایران همچنان به قوت خود باقی است
🔹
ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654810" target="_blank">📅 15:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وزیر شهرسازی: تعیین سقف افزایش اجاره‌بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/654809" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پشت‌پرده پیشنهاد صندوق ۳۰۰ میلیارد دلاری آمریکا به ایران
ادعای تایمز اسرائیل:
🔹
ویتکاف و کوشنرد پیشنهاد یک صندوق سرمایه‌گذاری در ایران را در صورت دستیابی به توافق نهایی داده‌اند. دو دیپلمات که در جریان آخرین پیش‌نویس قرار گرفتند، آن را «یک صندوق سرمایه‌گذاری بین‌المللی» نامیدند.
🔹
جزئیات این صندوق در دوره مذاکرات اولیه ۶۰ روزه بین ایران و آمریکا که این تفاهم‌نامه آغاز می‌شود، مورد بحث قرار خواهد گرفت. برخی از واسطه‌ها، پیشنهاد ترویج پروژه‌های املاک و مستغلات را نیز داده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654808" target="_blank">📅 14:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm_DFLh0NKwEpgDGsvW7f-2oVpKco6lRp3-pKmb3Nzkr9EqV3vtiDIIDoGNz0DgGAHzJrmxEXrXTh6ZIFhmTL72bnFphaGvjvz_t-IUliGF1GuC8glA6-RUJHmq2ZMKYf2qaIjdz7-3ESLYdUj62gfuMNWEbCX1rlyw0uxcWl59a_yzeR_ho5DcRcyS-dGyTz3ysiTzToXOeY_6-3OmyjSqORuFuiuweHyOJURXR-GLyvESHo7w9gzpWE0bEyV-XEFT7s0CQYp9xoN1so4sIjswYxbUOFZPXdlxHduHfHLAgG9mkisFEfdkFepThhv9q0KBecc1iqkzqJ1oRPdPcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین از جمع ۱۰ دارایی برتر جهان حذف شد
🔹
تشدید ضررهای بیت‌کوین، این رمزارز را از جمع ۱۰ دارایی برتر جهان از نظر ارزش بازار خارج کرد و آن در جایگاه سیزدهم قرار داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/654807" target="_blank">📅 14:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
توقیف
اموال ۷۴ خائن به وطن ساکن خارج از کشور در گلستان
دادگستری گلستان:
🔹
اموال ۷۴ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن که ساکن خارج از کشور هستند به نفع مردم توقیف شد؛ اموال توقیف‌شدهٔ این افراد شامل حساب‌های بانکی، خودرو و املاک ثبتی است.
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/654806" target="_blank">📅 14:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/654805" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654804">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بهار در ارتفاعات زنجان؛ دشت گل سرخه‌سنگ
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654804" target="_blank">📅 14:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تیزر قسمت دوم، فصل چهارم
🔹
دانیال قاسمعلی روایت کرد که پس از تجربه مرگ موقت، آینده‌ای تاریک از خود دید؛ تصویری که به گفته او باعث ترک اعتیاد و تغییر جدی در مسیر زندگی‌اش شد. او این تجربه را هشداری برای بازنگری در رفتارها و ارزش‌های زندگی دانست
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: دانیال قاسمعلی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/654803" target="_blank">📅 14:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
قطر: عوارض موقت عبور از تنگه هرمز قابل مذاکره است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654801" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654800">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf0218167.mp4?token=bqKQoFVnWVsM9cI0SzOvQuYIr3COdz1FNixsG2KFNo0Tco1e7nVaXtRQy64wQhJ_Mktb5QFz29zZfii_iQ3QtbugVVuBd5FnC8EJ3Fi3eDWe43Wj6OWTJ1xcam8NiBWGe1l9m6vzxOmthbHRUa_q90UfEtnTy03tM31Lve3Y3qPeoZowOXb653azy4xNm2WH74j7FthWms-qPueyDhqBwrxibko45mZN-s0TMKRm46vZG_AxJc6IFo3NpfYKJWO-jLw6rSb3-H7KbvKopMij2VvD7PVw1FPAvMKfuoevVG62AFMWq6B5HLkBuG7hkztvFkMGjROnd7VU6ax9tsPczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf0218167.mp4?token=bqKQoFVnWVsM9cI0SzOvQuYIr3COdz1FNixsG2KFNo0Tco1e7nVaXtRQy64wQhJ_Mktb5QFz29zZfii_iQ3QtbugVVuBd5FnC8EJ3Fi3eDWe43Wj6OWTJ1xcam8NiBWGe1l9m6vzxOmthbHRUa_q90UfEtnTy03tM31Lve3Y3qPeoZowOXb653azy4xNm2WH74j7FthWms-qPueyDhqBwrxibko45mZN-s0TMKRm46vZG_AxJc6IFo3NpfYKJWO-jLw6rSb3-H7KbvKopMij2VvD7PVw1FPAvMKfuoevVG62AFMWq6B5HLkBuG7hkztvFkMGjROnd7VU6ax9tsPczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجله فرانسوی: مکرون به زنش قول داده که فکر گلشیفته رو برای همیشه از سرش بیرون کند و دیگر خیانت نکند
!
🔹
پیش‌تر ادعا شده بود که سیلی حاشیه‌ساز همسر مکرون به او به دلیل چت‌های صمیمی مکرون با گلشیفته فراهانی بوده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/654800" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654799">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e46f0cb1.mp4?token=UCvZ-nOT5R6LbApTaw0B9pD0c4J4vdmD1wy_mpp4dopxWa0EY6S6xUVCcJtSQnSXNKjx1xEYcnGLof0sdhp9F32QJg5H1hNl3JbvTcbRWUy4S75e0tpPucet1xySbG2KWkUsHn5Wgkl0X7bXXMsuPXYZ9BnYIdlyJvivq3bi8gr2N_5VsN-DfwNJcUSsdbDcyvjfxUllQCjo0OybZ0Y0sjiGaymwZihmkWE5eIKZMR2qF1zAW4jsjy7ddSfArCpt2S3iuZKUEUHRI90iK3vlLm313ygOvxppwtEYxf4w3DBt00gVbNqbXNF0nDQV_-w1QSzKFg7eroK1YB6cR7Ww6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e46f0cb1.mp4?token=UCvZ-nOT5R6LbApTaw0B9pD0c4J4vdmD1wy_mpp4dopxWa0EY6S6xUVCcJtSQnSXNKjx1xEYcnGLof0sdhp9F32QJg5H1hNl3JbvTcbRWUy4S75e0tpPucet1xySbG2KWkUsHn5Wgkl0X7bXXMsuPXYZ9BnYIdlyJvivq3bi8gr2N_5VsN-DfwNJcUSsdbDcyvjfxUllQCjo0OybZ0Y0sjiGaymwZihmkWE5eIKZMR2qF1zAW4jsjy7ddSfArCpt2S3iuZKUEUHRI90iK3vlLm313ygOvxppwtEYxf4w3DBt00gVbNqbXNF0nDQV_-w1QSzKFg7eroK1YB6cR7Ww6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری فیزیکی شب گذشته هواداران پاری‌سن‌ژرمن و آرسنال در خیابان‌های بوداپست (محل برگزاری فینال لیگ قهرمانان اروپا)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654799" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654798">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPHfiVTPEgV9h1_hdGG3-XplDWY8eitrQkJSOrLkUxVwYWLpxMHVWe9zoO0kZtlwAdzAAhu1BbJw6ATRA_Yy3ex4v0REnsYBTVw_GLL5SBm-ObOboq4nbUGgc3ZzMksgV1csA_uoQXBJHX8qVUMePFfRHT4A6Gu8ClxadoxPgOH1XUVqeJWkyU7HpF4PNU1gT2HR5CaGRdHNeWSA47WKq_zEKUreU3S1U2VZX7EuVU8T5RKZOiVrZLM2-_nNb6Xx3cs8c15BMWXQXZ75bfpWAOdOxXoO9JT0R1oCtyUVNFhQBIvpQVBJv3NA0rZwzJtzHjK7rxq-ECOxmFJ_Ov1gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها|
#فوری_کتاب
| ساعت ۲۰
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654798" target="_blank">📅 14:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654797">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مجلس فردا میزبان‌ وزیر راه خواهد بود
سخنگوی هیئت‌رئیسۀ مجلس:
🔹
یکشنبه نشست وبیناری مجلس با حضور وزیر راه و شهرسازی با محوریت بازسازی اماکن خسارت‌دیدۀ ناشی از جنگ تحمیلی سوم برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/654797" target="_blank">📅 13:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تشدید حملات اسرائیل به لبنان؛ یک محله در صور به طور گسترده تخریب شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/654796" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
